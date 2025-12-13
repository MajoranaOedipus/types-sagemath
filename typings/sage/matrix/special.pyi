from .constructor import matrix as matrix
from sage.categories.rings import Rings as Rings
from sage.misc.misc_c import running_total as running_total
from sage.misc.prandom import randint as randint, shuffle as shuffle
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Matrix as Matrix, RingElement as RingElement, parent as parent
from sage.structure.sequence import Sequence as Sequence

def matrix_method(func=None, name=None):
    """
    Allow a function to be tab-completed on the global matrix
    constructor object.

    INPUT:

    - ``*function`` -- a single argument; the function that is being
      decorated

    - ``**kwds`` -- a single optional keyword argument
      ``name=<string>``. The name of the corresponding method in the
      global matrix constructor object. If not given, it is derived
      from the function name.

    EXAMPLES::

        sage: from sage.matrix.constructor import matrix_method
        sage: def foo_matrix(n): return matrix.diagonal(range(n))
        sage: matrix_method(foo_matrix)
        <function foo_matrix at ...>
        sage: matrix.foo(5)
        [0 0 0 0 0]
        [0 1 0 0 0]
        [0 0 2 0 0]
        [0 0 0 3 0]
        [0 0 0 0 4]
        sage: matrix_method(foo_matrix, name='bar')
        <function foo_matrix at ...>
        sage: matrix.bar(3)
        [0 0 0]
        [0 1 0]
        [0 0 2]
    """
@matrix_method
def column_matrix(*args, **kwds):
    """
    Construct a matrix, and then swap rows for columns and columns for rows.

    .. NOTE::

        Linear algebra in Sage favors rows over columns.  So,
        generally, when creating a matrix, input vectors and lists are
        treated as rows.  This function is a convenience that turns
        around this convention when creating a matrix.  If you are not
        familiar with the usual :func:`matrix`
        constructor, you might want to consider it first.

    INPUT:

    Inputs are almost exactly the same as for the :func:`matrix`
    constructor, which are documented there.  But see
    examples below for how dimensions are handled.

    OUTPUT:

    Output is exactly the transpose of what the :func:`matrix`
    constructor would return.  In other words, the
    ``matrix`` constructor builds a matrix and then this function
    exchanges rows for columns, and columns for rows.

    EXAMPLES:

    The most compelling use of this function is when you have a
    collection of lists or vectors that you would like to become the
    columns of a matrix. In almost any other situation, the
    :func:`matrix` constructor can probably do the
    job just as easily, or easier. ::

        sage: col_1 = [1,2,3]
        sage: col_2 = [4,5,6]
        sage: column_matrix([col_1, col_2])
        [1 4]
        [2 5]
        [3 6]

        sage: v1 = vector(QQ, [10, 20])
        sage: v2 = vector(QQ, [30, 40])
        sage: column_matrix(QQ, [v1, v2])
        [10 30]
        [20 40]

    If you only specify one dimension along with a flat list of entries,
    then it will be the number of columns in the result (which is different
    from the behavior of the ``matrix`` constructor).  ::

        sage: column_matrix(ZZ, 8, range(24))
        [ 0  3  6  9 12 15 18 21]
        [ 1  4  7 10 13 16 19 22]
        [ 2  5  8 11 14 17 20 23]

    And when you specify two dimensions, then they should be number of
    columns first, then the number of rows, which is the reverse of how
    they would be specified for the ``matrix`` constructor. ::

        sage: column_matrix(QQ, 5, 3, range(15))
        [ 0  3  6  9 12]
        [ 1  4  7 10 13]
        [ 2  5  8 11 14]

    And a few unproductive, but illustrative, examples. ::

        sage: A = matrix(ZZ, 3, 4, range(12))
        sage: B = column_matrix(ZZ, 3, 4, range(12))
        sage: A == B.transpose()
        True

        sage: A = matrix(QQ, 7, 12, range(84))
        sage: A == column_matrix(A.columns())
        True

        sage: A = column_matrix(QQ, matrix(ZZ, 3, 2, range(6)) )
        sage: A
        [0 2 4]
        [1 3 5]
        sage: A.parent()
        Full MatrixSpace of 2 by 3 dense matrices over Rational Field
    """
@matrix_method
def random_matrix(ring, nrows, ncols=None, algorithm: str = 'randomize', implementation=None, *args, **kwds):
    '''
    Return a random matrix with entries in a specified ring, and possibly with additional properties.

    INPUT:

    - ``ring`` -- base ring for entries of the matrix

    - ``nrows`` -- integer; number of rows

    - ``ncols`` -- (default: ``None``) number of columns. If ``None``
      defaults to ``nrows``.

    - ``algorithm`` -- (default: ``\'randomize\'``) determines what properties
      the matrix will have.  See examples below for possible additional
      arguments.

      - ``\'randomize\'`` -- create a matrix of random elements from the
        base ring, possibly controlling the density of nonzero entries

      - ``\'echelon_form\'`` -- creates a matrix in echelon form

      - ``\'echelonizable\'`` -- creates a matrix that has a predictable
        echelon form

      - ``\'subspaces\'`` -- creates a matrix whose four subspaces, when
        explored, have reasonably sized, integral valued, entries

      - ``\'unimodular\'`` -- creates a matrix of determinant 1

      - ``\'unitary\'`` -- creates a (square) unitary matrix over a
        subfield of the complex numbers

      - ``\'diagonalizable\'`` -- creates a diagonalizable matrix. if the
        base ring is ``QQ`` creates a diagonalizable matrix whose eigenvectors,
        if computed by hand, will have only integer entries. See the
        documentation of :meth:`~sage.matrix.special.random_diagonalizable_matrix`
        for more information

    - ``implementation`` -- (``None`` or string or a matrix class) a possible
      implementation. See the documentation of the constructor of
      :class:`~sage.matrix.matrix_space.MatrixSpace`.

    - ``*args, **kwds`` -- arguments and keywords to describe additional
      properties. See more detailed documentation below

    .. warning::

        Matrices generated are not uniformly distributed. For unimodular
        matrices over finite field this function does not even generate
        all of them: for example ``Matrix.random(GF(3), 2, algorithm=\'unimodular\')``
        never generates ``[[2,0],[0,2]]``. This function is made for
        teaching purposes.

    .. warning::

        An upper bound on the absolute value of the entries may be set
        when the ``algorithm`` is ``echelonizable`` or ``unimodular``.
        In these cases it is possible for this constructor to fail with
        a :exc:`ValueError`.  If you *must* have this routine return
        successfully, do not set ``upper_bound``.  This behavior can
        be partially controlled by a ``max_tries`` keyword.

    .. NOTE::

        When constructing matrices with random entries and no
        additional properties (i.e. when ``algorithm=\'randomize\'``),
        most of the randomness is controlled by the ``random_element``
        method for elements of the base ring of the matrix, so the
        documentation of that method may be relevant or useful.

    EXAMPLES:

    Random integer matrices.  With no arguments, the majority of the entries
    are zero, -1, and 1, and rarely "large." ::

        sage: from collections import defaultdict
        sage: total_count = 0
        sage: dic = defaultdict(Integer)
        sage: def add_samples(*args, **kwds):
        ....:     global dic, total_count
        ....:     for _ in range(100):
        ....:         A = random_matrix(*args, **kwds)
        ....:         for a in A.list():
        ....:             dic[a] += 1
        ....:             total_count += 1.0

        sage: expected = lambda n : 2 / (5*abs(n)*(abs(n) + 1)) if n != 0 else 1/5
        sage: expected(0)
        1/5
        sage: expected(0) == expected(1) == expected(-1)
        True
        sage: expected(100)
        1/25250
        sage: add_samples(ZZ, 5, 5)
        sage: while not all(abs(dic[a]/total_count - expected(a)) < 0.001 for a in dic):  # long time
        ....:     add_samples(ZZ, 5, 5)

    The ``distribution`` keyword  set to ``uniform`` will limit values
    between -2 and 2. ::

        sage: expected = lambda n : 1/5 if n in range(-2, 3) else 0
        sage: total_count = 0
        sage: dic = defaultdict(Integer)
        sage: add_samples(ZZ, 5, 5, distribution=\'uniform\')
        sage: while not all(abs(dic[a]/total_count - expected(a)) < 0.001 for a in dic):  # long time
        ....:     add_samples(ZZ, 5, 5, distribution=\'uniform\')

    The ``x`` and ``y`` keywords can be used to distribute entries uniformly.
    When both are used ``x`` is the minimum and ``y`` is one greater than
    the maximum. ::

        sage: expected = lambda n : 1/30 if n in range(70, 100) else 0
        sage: total_count = 0
        sage: dic = defaultdict(Integer)
        sage: add_samples(ZZ, 4, 8, x=70, y=100)
        sage: while not all(abs(dic[a]/total_count - expected(a)) < 0.001 for a in dic):  # long time
        ....:     add_samples(ZZ, 4, 8, x=70, y=100)

        sage: expected = lambda n : 1/10 if n in range(-5, 5) else 0
        sage: total_count = 0
        sage: dic = defaultdict(Integer)
        sage: add_samples(ZZ, 3, 7, x=-5, y=5)
        sage: while not all(abs(dic[a]/total_count - expected(a)) < 0.001 for a in dic):  # long time
        ....:     add_samples(ZZ, 3, 7, x=-5, y=5)

    If only ``x`` is given, then it is used as the upper bound of a range
    starting at 0. ::

        sage: expected = lambda n : 1/25 if n in range(25) else 0
        sage: total_count = 0
        sage: dic = defaultdict(Integer)
        sage: add_samples(ZZ, 5, 5, x=25)
        sage: while not all(abs(dic[a]/total_count - expected(a)) < 0.001 for a in dic):  # long time
        ....:     add_samples(ZZ, 5, 5, x=25)

    To control the number of nonzero entries, use the ``density`` keyword
    at a value strictly below the default of 1.0.  The ``density`` keyword
    is used to compute the number of entries per row that will be nonzero, but the
    same entry may be selected more than once.  So the value provided will
    be an upper bound for the density of the created matrix.  Note that for
    a square matrix it is only necessary to set a single dimension. ::

        sage: def add_sample(*args, **kwds):
        ....:     global density_sum, total_count
        ....:     total_count += 1.0
        ....:     A = random_matrix(*args, **kwds)
        ....:     density_sum += float(A.density())

        sage: # needs sage.libs.linbox (otherwise timeout)
        sage: density_sum = 0.0
        sage: total_count = 0.0
        sage: add_sample(ZZ, 5, x=-10, y=10, density=0.75)
        sage: expected_density = (1 - (4/5)^3)
        sage: float(expected_density)
        0.488
        sage: while abs(density_sum/total_count - expected_density) > 0.001:
        ....:     add_sample(ZZ, 5, x=-10, y=10, density=0.75)

        sage: # needs sage.libs.linbox (otherwise timeout)
        sage: density_sum = 0.0
        sage: total_count = 0.0
        sage: add_sample(ZZ, 5, x=20, y=30, density=0.75)
        sage: while abs(density_sum/total_count - expected_density) > 0.001:
        ....:     add_sample(ZZ, 5, x=20, y=30, density=0.75)

        sage: # needs sage.libs.linbox (otherwise timeout)
        sage: density_sum = 0.0
        sage: total_count = 0.0
        sage: add_sample(ZZ, 100, x=20, y=30, density=0.75)
        sage: expected_density = (1 - (99/100)^75)
        sage: float(expected_density)
        0.529...
        sage: while abs(density_sum/total_count - expected_density) > 0.001:
        ....:     add_sample(ZZ, 100, x=20, y=30, density=0.75)

    For a matrix with low density it may be advisable to insist on a sparse
    representation, as this representation is not selected automatically. ::

        sage: A = random_matrix(ZZ, 5, 5)
        sage: A.is_sparse()
        False
        sage: A = random_matrix(ZZ, 5, 5, sparse=True)
        sage: A.is_sparse()
        True

    For algorithm testing you might want to control the number of bits,
    say 10,000 entries, each limited to 16 bits.  ::

        sage: # needs sage.libs.linbox (otherwise timeout)
        sage: A = random_matrix(ZZ, 100, 100, x=2^16); A
        100 x 100 dense matrix over Integer Ring (use the \'.str()\' method to see the entries)

    One can prescribe a specific matrix implementation::

        sage: K.<a> = FiniteField(2^8)                                                  # needs sage.rings.finite_rings
        sage: type(random_matrix(K, 2, 5))                                              # needs sage.libs.m4ri sage.rings.finite_rings
        <class \'sage.matrix.matrix_gf2e_dense.Matrix_gf2e_dense\'>
        sage: type(random_matrix(K, 2, 5, implementation=\'generic\'))                    # needs sage.rings.finite_rings
        <class \'sage.matrix.matrix_generic_dense.Matrix_generic_dense\'>

    Random rational matrices.  Now ``num_bound`` and ``den_bound`` control the
    generation of random elements, by specifying limits on the absolute value of
    numerators and denominators (respectively).  Entries will be positive and
    negative (map the absolute value function through the entries to get all
    positive values).  If either the numerator or denominator bound (or both)
    is not used, then the values default to ``2``::

        sage: A = random_matrix(QQ, 2, 8, num_bound=20, den_bound=4)
        sage: A.dimensions()
        (2, 8)
        sage: type(A)
        <class \'sage.matrix.matrix_rational_dense.Matrix_rational_dense\'>
        sage: all(a.numerator() in range(-20, 21) and
        ....:     a.denominator() in range(1, 5)
        ....:     for a in A.list())
        True

        sage: A = random_matrix(QQ, 4, density=0.5, sparse=True)
        sage: type(A)
        <class \'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse\'>
        sage: A.density() <= 0.5
        True

        sage: A = random_matrix(QQ, 3, 10, num_bound = 99, den_bound = 99)
        sage: positives = list(map(abs, A.list()))
        sage: A1 = matrix(QQ, 3, 10, positives)
        sage: all(abs(A.list()[i]) == A1.list()[i] for i in range(30))
        True
        sage: all(a.numerator() in range(100) and
        ....:     a.denominator() in range(1, 100)
        ....:     for a in A1.list())
        True

        sage: A = random_matrix(QQ, 4, 10, den_bound = 10)
        sage: all(a.numerator() in range(-2, 3) and
        ....:     a.denominator() in range(1, 11)
        ....:     for a in A.list())
        True

        sage: A = random_matrix(QQ, 4, 10)
        sage: all(a.numerator() in range(-2, 3) and
        ....:     a.denominator() in range(1, 3)
        ....:     for a in A.list())
        True

    Random matrices over other rings.  Several classes of matrices have specialized
    ``randomize()`` methods.  You can locate these with the Sage command::

        search_def(\'randomize\')

    The default implementation of :meth:`~sage.matrix.matrix2.randomize` relies
    on the ``random_element()`` method for the base ring.  The ``density`` and
    ``sparse`` keywords behave as described above. Since we have a different
    randomisation when using the optional meataxe package, we have to make sure
    that we use the default implementation in this test::

        sage: K.<a> = FiniteField(3^2)                                                  # needs sage.rings.finite_rings
        sage: A = random_matrix(K, 2, 5, implementation=\'generic\')                      # needs sage.rings.finite_rings
        sage: type(A)
        <class \'sage.matrix.matrix_generic_dense.Matrix_generic_dense\'>
        sage: A.base_ring() is K                                                        # needs sage.rings.finite_rings
        True
        sage: TestSuite(A).run()

        sage: A = random_matrix(RR, 3, 4, density=0.66)
        sage: type(A)
        <class \'sage.matrix.matrix_generic_dense.Matrix_generic_dense\'>
        sage: A.base_ring() is RR
        True
        sage: TestSuite(A).run()

        sage: A = random_matrix(ComplexField(32), 3, density=0.8, sparse=True)
        sage: A.is_sparse()
        True
        sage: type(A)
        <class \'sage.matrix.matrix_generic_sparse.Matrix_generic_sparse\'>
        sage: A.base_ring() is ComplexField(32)
        True
        sage: TestSuite(A).run()

    Random matrices in echelon form.  The ``algorithm=\'echelon_form\'`` keyword,
    along with a requested number of nonzero rows (``num_pivots``) will return
    a random matrix in echelon form.  When the base ring is ``QQ`` the result has integer
    entries.  Other exact rings may be also specified. ::

        sage: A = random_matrix(QQ, 4, 8, algorithm=\'echelon_form\', num_pivots=3)
        sage: A.base_ring()
        Rational Field
        sage: (A.nrows(), A.ncols())
        (4, 8)
        sage: A in sage.matrix.matrix_space.MatrixSpace(ZZ, 4, 8)
        True
        sage: A.rank()
        3
        sage: A == A.rref()
        True

    For more, see the documentation of the :func:`~sage.matrix.constructor.random_rref_matrix`
    function.  In the notebook or at the Sage command-line, first execute the following to make
    this further documentation available::

        from sage.matrix.constructor import random_rref_matrix

    Random matrices with predictable echelon forms.  The ``algorithm=\'echelonizable\'``
    keyword, along with a requested rank (``rank``) and optional size control
    (``upper_bound``) will return a random matrix in echelon form.  When the
    base ring is ``ZZ`` or ``QQ`` the result has integer entries, whose magnitudes
    can be limited by the value of ``upper_bound``, and the echelon form of the
    matrix also has integer entries.  Other exact rings may be also
    specified, but there is no notion of controlling the size.  Square matrices
    of full rank generated by this function always have determinant one, and
    can be constructed with the ``unimodular`` keyword. ::

        sage: A = random_matrix(QQ, 4, 8, algorithm=\'echelonizable\', rank=3, upper_bound=60)
        sage: A.base_ring()
        Rational Field
        sage: (A.nrows(), A.ncols())
        (4, 8)
        sage: A in sage.matrix.matrix_space.MatrixSpace(ZZ, 4, 8)
        True
        sage: A.rank()
        3
        sage: all(abs(x)<60 for x in A.list())
        True
        sage: A.rref() in sage.matrix.matrix_space.MatrixSpace(ZZ, 4, 8)
        True

    For more, see the documentation of the :func:`~sage.matrix.constructor.random_echelonizable_matrix`
    function.  In the notebook or at the Sage command-line, first execute the following to make
    this further documentation available::

        from sage.matrix.constructor import random_echelonizable_matrix

    Random diagonalizable matrices.  The ``algorithm=\'diagonalizable\'`` keyword,
    along with a requested matrix size (``size``) and optional lists of
    eigenvalues (``eigenvalues``) and the corresponding eigenspace
    dimensions (``dimensions``) will return a random diagonalizable matrix.
    When the eigenvalues and dimensions are not specified the result will have
    randomly generated values for both that fit with the designated size. ::

        sage: A = random_matrix(QQ, 5, algorithm=\'diagonalizable\',  # random
        ....:                   eigenvalues=[2,3,-1], dimensions=[1,2,2]); A
        sage: all(x in ZZ for x in (A - (2*identity_matrix(5))).rref().list())
        True
        sage: all(x in ZZ for x in (A - 3*identity_matrix(5)).rref().list())
        True
        sage: all(x in ZZ for x in (A - (-1)*identity_matrix(5)).rref().list())
        True
        sage: A.jordan_form()                                                           # needs sage.combinat sage.libs.pari
        [ 2| 0| 0| 0| 0]
        [--+--+--+--+--]
        [ 0| 3| 0| 0| 0]
        [--+--+--+--+--]
        [ 0| 0| 3| 0| 0]
        [--+--+--+--+--]
        [ 0| 0| 0|-1| 0]
        [--+--+--+--+--]
        [ 0| 0| 0| 0|-1]

    For more, see the documentation of the :func:`~sage.matrix.constructor.random_diagonalizable_matrix`
    function.  In the notebook or at the Sage command-line, first execute the following to make
    this further documentation available::

        from sage.matrix.constructor import random_diagonalizable_matrix

    Random matrices with predictable subspaces.  The ``algorithm=\'subspaces\'``
    keyword, along with an optional rank (``rank``) will return
    a matrix whose natural basis vectors for its four fundamental subspaces, if computed as
    described in the documentation of the :func:`~sage.matrix.constructor.random_subspaces_matrix`
    contain only integer entries.  If ``rank``, is not set, the
    rank of the matrix will be generated randomly. ::

        sage: B = random_matrix(QQ, 5, 6, algorithm=\'subspaces\', rank=3); B  # random
        sage: B_expanded = B.augment(identity_matrix(5)).rref()
        sage: (B.nrows(), B.ncols())
        (5, 6)
        sage: all(x in ZZ for x in B_expanded.list())
        True
        sage: C = B_expanded.submatrix(0, 0, B.nrows() - B.nullity(), B.ncols())
        sage: L = B_expanded.submatrix(B.nrows() - B.nullity(), B.ncols())
        sage: B.right_kernel() == C.right_kernel()
        True
        sage: B.row_space() == C.row_space()
        True
        sage: B.column_space() == L.right_kernel()
        True
        sage: B.left_kernel() == L.row_space()
        True

    For more, see the documentation of the :func:`~sage.matrix.constructor.random_subspaces_matrix`
    function.  In the notebook or at the Sage command-line, first execute the following to make
    this further documentation available::

        from sage.matrix.constructor import random_subspaces_matrix

    Random unimodular matrices.  The ``algorithm=\'unimodular\'``
    keyword, along with an optional entry size control (``upper_bound``)
    will return a matrix of determinant 1. When the base ring is ``ZZ``
    or ``QQ`` the result has integer entries, whose magnitudes
    can be limited by the value of ``upper_bound``. ::

        sage: C = random_matrix(QQ, 5, algorithm=\'unimodular\', upper_bound=70); C  # random
        sage: det(C)
        1
        sage: C.base_ring()
        Rational Field
        sage: (C.nrows(), C.ncols())
        (5, 5)
        sage: all(abs(x)<70 for x in C.list())
        True

    For more, see the documentation of the :func:`~sage.matrix.constructor.random_unimodular_matrix`
    function.  In the notebook or at the Sage command-line, first execute the following to make
    this further documentation available::

        from sage.matrix.constructor import random_unimodular_matrix

    TESTS:

    We return an error for a bogus value of ``algorithm``::

        sage: random_matrix(ZZ, 5, algorithm=\'bogus\')
        Traceback (most recent call last):
        ...
        ValueError: random matrix algorithm "bogus" is not recognized

    AUTHOR:

    - William Stein (2007-02-06)

    - Rob Beezer (2010-08-25) Documentation, code to allow additional types of output
    '''
@matrix_method
def diagonal_matrix(arg0=None, arg1=None, arg2=None, sparse: bool = True):
    """
    Return a square matrix with specified diagonal entries, and zeros elsewhere.

    FORMATS:

      1. diagonal_matrix(entries)

      2. diagonal_matrix(nrows, entries)

      3. diagonal_matrix(ring, entries)

      4. diagonal_matrix(ring, nrows, entries)

    INPUT:

    - ``entries`` -- the values to place along the diagonal
      of the returned matrix.  This may be a flat list, a
      flat tuple, a vector or free module element, or
      a one-dimensional NumPy array.

    - ``nrows`` -- the size of the returned matrix, which
      will have an equal number of columns

    - ``ring`` -- the ring containing the entries of the
      diagonal entries.  This may not be specified in
      combination with a NumPy array.

    - ``sparse`` -- boolean (default: ``True``); whether or not
      the result has a sparse implementation

    OUTPUT:

    A square matrix over the given ``ring`` with a size
    given by ``nrows``.  If the ring is not given it
    is inferred from the given entries.  The values on
    the diagonal of the returned matrix come from ``entries``.
    If the number of entries is not enough to fill the whole
    diagonal, it is padded with zeros.

    EXAMPLES:

    We first demonstrate each of the input formats with various
    different ways to specify the entries.

    Format 1: a flat list of entries.  ::

        sage: A = diagonal_matrix([2, 1.3, 5]); A
        [ 2.00000000000000 0.000000000000000 0.000000000000000]
        [0.000000000000000  1.30000000000000 0.000000000000000]
        [0.000000000000000 0.000000000000000  5.00000000000000]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Real Field with 53 bits of precision

    Format 2: size specified, a tuple with initial entries. Note that a short list of entries
    is effectively padded with zeros.  ::

        sage: A = diagonal_matrix(3, (4, 5)); A
        [4 0 0]
        [0 5 0]
        [0 0 0]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring

    Format 3: ring specified, a vector of entries. ::

        sage: A = diagonal_matrix(QQ, vector(ZZ, [1,2,3])); A
        [1 0 0]
        [0 2 0]
        [0 0 3]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Rational Field

    Format 4: ring, size and list of entries. ::

        sage: A = diagonal_matrix(FiniteField(3), 3, [2, 16]); A
        [2 0 0]
        [0 1 0]
        [0 0 0]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Finite Field of size 3

    NumPy arrays may be used as input. ::

        sage: # needs numpy
        sage: import numpy
        sage: entries = numpy.array([1.2, 5.6]); entries
        array([1.2, 5.6])
        sage: A = diagonal_matrix(3, entries); A
        [1.2 0.0 0.0]
        [0.0 5.6 0.0]
        [0.0 0.0 0.0]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Real Double Field

        sage: # needs numpy
        sage: j = complex(0,1)
        sage: entries = numpy.array([2.0+j, 8.1, 3.4+2.6*j]); entries
        array([2. +1.j , 8.1+0.j , 3.4+2.6j])
        sage: A = diagonal_matrix(entries); A
        [2.0 + 1.0*I         0.0         0.0]
        [        0.0         8.1         0.0]
        [        0.0         0.0 3.4 + 2.6*I]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Complex Double Field

        sage: # needs numpy
        sage: entries = numpy.array([4, 5, 6])
        sage: A = diagonal_matrix(entries); A
        [4 0 0]
        [0 5 0]
        [0 0 6]
        sage: A.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring

        sage: entries = numpy.array([4.1, 5.2, 6.3])                                    # needs numpy
        sage: A = diagonal_matrix(ZZ, entries); A                                       # needs numpy
        Traceback (most recent call last):
        ...
        TypeError: unable to convert 4.1 to an element of Integer Ring

    By default returned matrices have a sparse implementation.  This can be changed
    when using any of the formats.  ::

        sage: A = diagonal_matrix([1,2,3], sparse=False)
        sage: A.parent()
        Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

    An empty list and no ring specified defaults to the integers. ::

        sage: A = diagonal_matrix([])
        sage: A.parent()
        Full MatrixSpace of 0 by 0 sparse matrices over Integer Ring

    Giving the entries improperly may first complain about not being iterable::

        sage: diagonal_matrix(QQ, 5, 10)
        Traceback (most recent call last):
        ...
        TypeError: 'sage.rings.integer.Integer' object is not iterable

    Giving too many entries will raise an error. ::

        sage: diagonal_matrix(QQ, 3, [1,2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: number of diagonal matrix entries (4) exceeds the requested matrix size (3)

    A negative size sometimes causes the error that there are too many elements. ::

        sage: diagonal_matrix(-2, [2])
        Traceback (most recent call last):
        ...
        ValueError: number of diagonal matrix entries (1) exceeds the requested matrix size (-2)

    Types for the entries need to be iterable (tuple, list, vector, NumPy array,
    etc)::

        sage: diagonal_matrix(x^2)                                                      # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: 'sage.symbolic.expression.Expression' object is not iterable

    TESTS::

        sage: A = diagonal_matrix(reversed(range(4)))

    AUTHOR:

    - Rob Beezer (2011-01-11): total rewrite
    """
@matrix_method
def identity_matrix(ring, n: int = 0, sparse: bool = False):
    """
    Return the `n \\times n` identity matrix over the given
    ring.

    The default ring is the integers.

    EXAMPLES::

        sage: M = identity_matrix(QQ, 2); M
        [1 0]
        [0 1]
        sage: M.parent()
        Full MatrixSpace of 2 by 2 dense matrices over Rational Field
        sage: M = identity_matrix(2); M
        [1 0]
        [0 1]
        sage: M.parent()
        Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
        sage: M.is_mutable()
        True
        sage: M = identity_matrix(3, sparse=True); M
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: M.parent()
        Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring
        sage: M.is_mutable()
        True
    """
@matrix_method
def lehmer(ring, n: int = 0):
    """
    Return the `n \\times n` Lehmer matrix.

    The default ring is the rationals.

    Element `(i, j)` in the Lehmer matrix is
    `min(i, j)/max(i, j)`.

    See :wikipedia:`Lehmer_matrix`.

    EXAMPLES::

        sage: matrix.lehmer(3)
        [  1 1/2 1/3]
        [1/2   1 2/3]
        [1/3 2/3   1]
    """
@matrix_method
def zero_matrix(ring, nrows=None, ncols=None, sparse: bool = False):
    """
    Return the `nrows \\times ncols` zero matrix over the given
    ring.

    The default ring is the integers.

    EXAMPLES::

        sage: M = zero_matrix(QQ, 2); M
        [0 0]
        [0 0]
        sage: M.parent()
        Full MatrixSpace of 2 by 2 dense matrices over Rational Field
        sage: M = zero_matrix(2, 3); M
        [0 0 0]
        [0 0 0]
        sage: M.parent()
        Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
        sage: M.is_mutable()
        True
        sage: M = zero_matrix(3, 1, sparse=True); M
        [0]
        [0]
        [0]
        sage: M.parent()
        Full MatrixSpace of 3 by 1 sparse matrices over Integer Ring
        sage: M.is_mutable()
        True
        sage: matrix.zero(5)
        [0 0 0 0 0]
        [0 0 0 0 0]
        [0 0 0 0 0]
        [0 0 0 0 0]
        [0 0 0 0 0]

    TESTS:

    Check that :issue:`38221` is fixed::

        sage: # needs sage.groups
        sage: G = CyclicPermutationGroup(7)
        sage: R = GF(2)
        sage: A = G.algebra(R)
        sage: zero_matrix(A, 3, 3)
        [0 0 0]
        [0 0 0]
        [0 0 0]
    """
@matrix_method
def ones_matrix(ring, nrows=None, ncols=None, sparse: bool = False):
    """
    Return a matrix with all entries equal to 1.

    CALL FORMATS:

    In each case, the optional keyword ``sparse`` can be used.

      1. ones_matrix(ring, nrows, ncols)
      2. ones_matrix(ring, nrows)
      3. ones_matrix(nrows, ncols)
      4. ones_matrix(nrows)

    INPUT:

    - ``ring`` -- (default: ``ZZ``) base ring for the matrix
    - ``nrows`` -- number of rows in the matrix
    - ``ncols`` -- number of columns in the matrix;
      if omitted, defaults to the number of rows, producing a square matrix
    - ``sparse`` -- (default: ``False``) if ``True`` creates a sparse representation

    OUTPUT:

    A matrix of size ``nrows`` by ``ncols`` over the ``ring`` with every
    entry equal to 1.  While the result is far from sparse, you may wish
    to choose a sparse representation when mixing this matrix with
    other sparse matrices.

    EXAMPLES:

    A call specifying the ring and the size.  ::

        sage: M= ones_matrix(QQ, 2, 5); M
        [1 1 1 1 1]
        [1 1 1 1 1]
        sage: M.parent()
        Full MatrixSpace of 2 by 5 dense matrices over Rational Field

    Without specifying the number of columns, the result is square. ::

        sage: M = ones_matrix(RR, 2); M
        [1.00000000000000 1.00000000000000]
        [1.00000000000000 1.00000000000000]
        sage: M.parent()
        Full MatrixSpace of 2 by 2 dense matrices over Real Field with 53 bits of precision

    The ring defaults to the integers if not given. ::

        sage: M = ones_matrix(2, 3); M
        [1 1 1]
        [1 1 1]
        sage: M.parent()
        Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

    A lone integer input produces a square matrix over the integers. ::

        sage: M = ones_matrix(3); M
        [1 1 1]
        [1 1 1]
        [1 1 1]
        sage: M.parent()
        Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

    The result can have a sparse implementation. ::

        sage: M = ones_matrix(3, 1, sparse=True); M
        [1]
        [1]
        [1]
        sage: M.parent()
        Full MatrixSpace of 3 by 1 sparse matrices over Integer Ring

    Giving just a ring will yield an error. ::

        sage: ones_matrix(CC)
        Traceback (most recent call last):
        ...
        ValueError: constructing an all ones matrix requires at least one dimension
    """
@matrix_method
def elementary_matrix(arg0, arg1=None, **kwds):
    """
    Create a square matrix that corresponds to a row operation or a column operation.

    FORMATS:

    In each case, ``R`` is the base ring, and is optional. ``n`` is the size
    of the square matrix created.  Any call may include the ``sparse`` keyword
    to determine the representation used.  The default is ``False`` which
    leads to a dense representation.  We describe the matrices by their
    associated row operation, see the output description for more.

    - ``elementary_matrix(R, n, row1=i, row2=j)``

      The matrix which swaps rows ``i`` and ``j``.

    - ``elementary_matrix(R, n, row1=i, scale=s)``

      The matrix which multiplies row ``i`` by ``s``.

    - ``elementary_matrix(R, n, row1=i, row2=j, scale=s)``

      The matrix which multiplies row ``j`` by ``s``
      and adds it to row ``i``.

    Elementary matrices representing column operations are created
    in an entirely analogous way, replacing ``row1`` by ``col1`` and
    replacing ``row2`` by ``col2``.

    Specifying the ring for entries of the matrix is optional.  If it
    is not given, and a scale parameter is provided, then a ring containing
    the value of ``scale`` will be used.  Otherwise, the ring defaults
    to the integers.

    OUTPUT:

    An elementary matrix is a square matrix that is very close to being
    an identity matrix.  If ``E`` is an elementary matrix and ``A`` is any
    matrix with the same number of rows, then ``E*A`` is the result of
    applying a row operation to ``A``.  This is how the three types
    created by this function are described.  Similarly, an elementary matrix
    can be associated with a column operation, so if ``E`` has the same number
    of columns as ``A`` then ``A*E`` is the result of performing a column
    operation on ``A``.

    An elementary matrix representing a row operation is created if ``row1``
    is specified, while an elementary matrix representing a column operation
    is created if ``col1`` is specified.

    EXAMPLES:

    Over the integers, creating row operations. Recall that row
    and column numbering begins at zero.  ::

        sage: A = matrix(ZZ, 4, 10, range(40)); A
        [ 0  1  2  3  4  5  6  7  8  9]
        [10 11 12 13 14 15 16 17 18 19]
        [20 21 22 23 24 25 26 27 28 29]
        [30 31 32 33 34 35 36 37 38 39]

        sage: E = elementary_matrix(4, row1=1, row2=3); E
        [1 0 0 0]
        [0 0 0 1]
        [0 0 1 0]
        [0 1 0 0]
        sage: E*A
        [ 0  1  2  3  4  5  6  7  8  9]
        [30 31 32 33 34 35 36 37 38 39]
        [20 21 22 23 24 25 26 27 28 29]
        [10 11 12 13 14 15 16 17 18 19]

        sage: E = elementary_matrix(4, row1=2, scale=10); E
        [ 1  0  0  0]
        [ 0  1  0  0]
        [ 0  0 10  0]
        [ 0  0  0  1]
        sage: E*A
        [  0   1   2   3   4   5   6   7   8   9]
        [ 10  11  12  13  14  15  16  17  18  19]
        [200 210 220 230 240 250 260 270 280 290]
        [ 30  31  32  33  34  35  36  37  38  39]

        sage: E = elementary_matrix(4, row1=2, row2=1, scale=10); E
        [ 1  0  0  0]
        [ 0  1  0  0]
        [ 0 10  1  0]
        [ 0  0  0  1]
        sage: E*A
        [  0   1   2   3   4   5   6   7   8   9]
        [ 10  11  12  13  14  15  16  17  18  19]
        [120 131 142 153 164 175 186 197 208 219]
        [ 30  31  32  33  34  35  36  37  38  39]

    Over the rationals, now as column operations. Recall that row
    and column numbering begins at zero.  Checks now have the
    elementary matrix on the right.  ::

        sage: A = matrix(QQ, 5, 4, range(20)); A
        [ 0  1  2  3]
        [ 4  5  6  7]
        [ 8  9 10 11]
        [12 13 14 15]
        [16 17 18 19]

        sage: E = elementary_matrix(QQ, 4, col1=1, col2=3); E
        [1 0 0 0]
        [0 0 0 1]
        [0 0 1 0]
        [0 1 0 0]
        sage: A*E
        [ 0  3  2  1]
        [ 4  7  6  5]
        [ 8 11 10  9]
        [12 15 14 13]
        [16 19 18 17]

        sage: E = elementary_matrix(QQ, 4, col1=2, scale=1/2); E
        [  1   0   0   0]
        [  0   1   0   0]
        [  0   0 1/2   0]
        [  0   0   0   1]
        sage: A*E
        [ 0  1  1  3]
        [ 4  5  3  7]
        [ 8  9  5 11]
        [12 13  7 15]
        [16 17  9 19]

        sage: E = elementary_matrix(QQ, 4, col1=2, col2=1, scale=10); E
        [ 1  0  0  0]
        [ 0  1 10  0]
        [ 0  0  1  0]
        [ 0  0  0  1]
        sage: A*E
        [  0   1  12   3]
        [  4   5  56   7]
        [  8   9 100  11]
        [ 12  13 144  15]
        [ 16  17 188  19]

    An elementary matrix is always nonsingular.  Then repeated row
    operations can be represented by products of elementary matrices,
    and this product is again nonsingular.  If row operations are to
    preserve fundamental properties of a matrix (like rank), we do not
    allow scaling a row by zero.  Similarly, the corresponding elementary
    matrix is not constructed.  Also, we do not allow adding a multiple
    of a row to itself, since this could also lead to a new zero row.  ::

        sage: A = matrix(QQ, 4, 10, range(40)); A
        [ 0  1  2  3  4  5  6  7  8  9]
        [10 11 12 13 14 15 16 17 18 19]
        [20 21 22 23 24 25 26 27 28 29]
        [30 31 32 33 34 35 36 37 38 39]

        sage: E1 = elementary_matrix(QQ, 4, row1=0, row2=1)
        sage: E2 = elementary_matrix(QQ, 4, row1=3, row2=0, scale=100)
        sage: E = E2*E1
        sage: E.is_singular()
        False
        sage: E*A
        [  10   11   12   13   14   15   16   17   18   19]
        [   0    1    2    3    4    5    6    7    8    9]
        [  20   21   22   23   24   25   26   27   28   29]
        [1030 1131 1232 1333 1434 1535 1636 1737 1838 1939]

        sage: E3 = elementary_matrix(QQ, 4, row1=3, scale=0)
        Traceback (most recent call last):
        ...
        ValueError: scale parameter of row of elementary matrix must be nonzero

        sage: E4 = elementary_matrix(QQ, 4, row1=3, row2=3, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: cannot add a multiple of a row to itself

    If the ring is not specified, and a scale parameter is given, the
    base ring for the matrix is chosen to contain the scale parameter.
    Otherwise, if no ring is given, the default is the integers. ::

        sage: E = elementary_matrix(4, row1=1, row2=3)
        sage: E.parent()
        Full MatrixSpace of 4 by 4 dense matrices over Integer Ring

        sage: E = elementary_matrix(4, row1=1, scale=4/3)
        sage: E.parent()
        Full MatrixSpace of 4 by 4 dense matrices over Rational Field

        sage: # needs sage.symbolic
        sage: E = elementary_matrix(4, row1=1, scale=I)
        sage: E.parent()
        Full MatrixSpace of 4 by 4 dense matrices over
         Number Field in I with defining polynomial x^2 + 1 with I = 1*I

        sage: # needs sage.rings.complex_double sage.symbolic
        sage: E = elementary_matrix(4, row1=1, scale=CDF(I))
        sage: E.parent()
        Full MatrixSpace of 4 by 4 dense matrices over Complex Double Field

        sage: # needs sage.rings.number_field sage.symbolic
        sage: E = elementary_matrix(4, row1=1, scale=QQbar(I))
        sage: E.parent()
        Full MatrixSpace of 4 by 4 dense matrices over Algebraic Field

    Returned matrices have a dense implementation by default,
    but a sparse implementation may be requested.  ::

        sage: E = elementary_matrix(4, row1=0, row2=1)
        sage: E.is_dense()
        True

        sage: E = elementary_matrix(4, row1=0, row2=1, sparse=True)
        sage: E.is_sparse()
        True

    And the ridiculously small cases.  The zero-row matrix cannot be built
    since then there are no rows to manipulate. ::

        sage: elementary_matrix(QQ, 1, row1=0, row2=0)
        [1]
        sage: elementary_matrix(QQ, 0, row1=0, row2=0)
        Traceback (most recent call last):
        ...
        ValueError: size of elementary matrix must be 1 or greater, not 0

    TESTS::

        sage: E = elementary_matrix('junk', 5, row1=3, row2=1, scale=12)
        Traceback (most recent call last):
        ...
        TypeError: optional first parameter must be a ring, not junk

        sage: E = elementary_matrix(5, row1=3, scale='junk')
        Traceback (most recent call last):
        ...
        TypeError: scale must be an element of some ring, not junk

        sage: E = elementary_matrix(ZZ, 5, row1=3, col2=3, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: received an unexpected keyword: col2=3

        sage: E = elementary_matrix(QQ, row1=3, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: size of elementary matrix must be given

        sage: E = elementary_matrix(ZZ, 4/3, row1=3, row2=1, scale=12)
        Traceback (most recent call last):
        ...
        TypeError: size of elementary matrix must be an integer, not 4/3

        sage: E = elementary_matrix(ZZ, -3, row1=3, row2=1, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: size of elementary matrix must be 1 or greater, not -3

        sage: E = elementary_matrix(ZZ, 5, row2=1, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: row1 or col1 must be specified

        sage: E = elementary_matrix(ZZ, 5, row1=3, col1=3, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: cannot specify both row1 and col1

        sage: E = elementary_matrix(ZZ, 5, row1=4/3, row2=1, scale=12)
        Traceback (most recent call last):
        ...
        TypeError: row of elementary matrix must be an integer, not 4/3

        sage: E = elementary_matrix(ZZ, 5, col1=5, col2=1, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: column of elementary matrix must be positive and smaller than 5, not 5

        sage: E = elementary_matrix(ZZ, 5, col1=3, col2=4/3, scale=12)
        Traceback (most recent call last):
        ...
        TypeError: column of elementary matrix must be an integer, not 4/3

        sage: E = elementary_matrix(ZZ, 5, row1=3, row2=-1, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: row of elementary matrix must be positive and smaller than 5, not -1

        sage: E = elementary_matrix(ZZ, 5, row1=3, row2=1, scale=4/3)
        Traceback (most recent call last):
        ...
        TypeError: scale parameter of elementary matrix must an element of Integer Ring, not 4/3

        sage: E = elementary_matrix(ZZ, 5, row1=3)
        Traceback (most recent call last):
        ...
        ValueError: insufficient parameters provided to construct elementary matrix

        sage: E = elementary_matrix(ZZ, 5, row1=3, row2=3, scale=12)
        Traceback (most recent call last):
        ...
        ValueError: cannot add a multiple of a row to itself

        sage: E = elementary_matrix(ZZ, 5, col1=3, scale=0)
        Traceback (most recent call last):
        ...
        ValueError: scale parameter of column of elementary matrix must be nonzero

    AUTHOR:

    - Rob Beezer (2011-03-04)
    """
@matrix_method
def circulant(v, sparse=None):
    """
    Return the circulant matrix specified by its 1st row `v`.

    A circulant `n \\times n` matrix specified by the 1st row `v=(v_0...v_{n-1})` is
    the matrix `(c_{ij})_{0 \\leq i,j\\leq n-1}`, where `c_{ij}=v_{j-i \\mod b}`.

    INPUT:

    - ``v`` -- list or a vector of values

    - ``sparse`` -- ``None`` by default; if ``sparse`` is set to ``True``, the output
      will be sparse.  Respectively, setting it to ``False`` produces dense output.
      If ``sparse`` is not set, and if ``v`` is a vector, the output sparsity is determined
      by the sparsity of ``v``; else, the output will be dense.

    EXAMPLES::

        sage: v = [1,2,3,4,8]
        sage: matrix.circulant(v)
        [1 2 3 4 8]
        [8 1 2 3 4]
        [4 8 1 2 3]
        [3 4 8 1 2]
        [2 3 4 8 1]
        sage: m = matrix.circulant(vector(GF(3),[0,1,-1],sparse=True)); m
        [0 1 2]
        [2 0 1]
        [1 2 0]
        sage: m.is_sparse()
        True

    TESTS::

        sage: m = matrix.circulant(vector(GF(3),[0,1,-1],sparse=False))
        sage: m.is_sparse()
        False
        sage: matrix.circulant([0,1,-1]).is_sparse()
        False
        sage: matrix.circulant([0,1,-1], sparse=True).is_sparse()
        True
    """
@matrix_method
def block_matrix(*args, **kwds):
    '''
    Return a larger matrix made by concatenating submatrices
    (rows first, then columns). For example, the matrix

    ::

        [ A B ]
        [ C D ]

    is made up of submatrices A, B, C, and D.

    INPUT:

    The :func:`block_matrix` function takes a list of submatrices to add
    as blocks, optionally preceded by a ring and the number of block rows
    and block columns, and returns a matrix.

    The submatrices can be specified as a list of matrices (using
    ``nrows`` and ``ncols`` to determine their layout), or a list
    of lists of matrices/column vectors, where each list forms a row.

    - ``ring`` -- the base ring

    - ``nrows`` -- the number of block rows

    - ``ncols`` -- the number of block cols

    - ``sub_matrices`` -- matrices (see below for syntax)

    - ``subdivide`` -- boolean, whether or not to add
      subdivision information to the matrix

    - ``sparse`` -- boolean, whether to make the resulting matrix sparse

    EXAMPLES::

        sage: A = matrix(QQ, 2, 2, [3,9,6,10])
        sage: block_matrix([ [A, -A], [~A, 100*A] ])
        [    3     9|   -3    -9]
        [    6    10|   -6   -10]
        [-----------+-----------]
        [-5/12   3/8|  300   900]
        [  1/4  -1/8|  600  1000]

    If the number of submatrices in each row is the same,
    you can specify the submatrices as a single list too::

        sage: block_matrix(2, 2, [ A, A, A, A ])
        [ 3  9| 3  9]
        [ 6 10| 6 10]
        [-----+-----]
        [ 3  9| 3  9]
        [ 6 10| 6 10]

    One can use constant entries::

        sage: block_matrix([ [1, A], [0, 1] ])
        [ 1  0| 3  9]
        [ 0  1| 6 10]
        [-----+-----]
        [ 0  0| 1  0]
        [ 0  0| 0  1]

    A zero entry may represent any square or non-square zero matrix::

        sage: B = matrix(QQ, 1, 1, [ 1 ] )
        sage: C = matrix(QQ, 2, 2, [ 2, 3, 4, 5 ] )
        sage: block_matrix([ [B, 0], [0, C] ])
        [1|0 0]
        [-+---]
        [0|2 3]
        [0|4 5]

    One can specify the number of rows or columns as keywords too::

        sage: block_matrix([A, -A, ~A, 100*A], ncols=4)
        [    3     9|   -3    -9|-5/12   3/8|  300   900]
        [    6    10|   -6   -10|  1/4  -1/8|  600  1000]

        sage: block_matrix([A, -A, ~A, 100*A], nrows=1)
        [    3     9|   -3    -9|-5/12   3/8|  300   900]
        [    6    10|   -6   -10|  1/4  -1/8|  600  1000]

    It handles base rings nicely too::

        sage: R.<x> = ZZ[\'x\']
        sage: block_matrix(2, 2, [1/2, A, 0, x-1])
        [  1/2     0|    3     9]
        [    0   1/2|    6    10]
        [-----------+-----------]
        [    0     0|x - 1     0]
        [    0     0|    0 x - 1]

        sage: block_matrix(2, 2, [1/2, A, 0, x-1]).parent()
        Full MatrixSpace of 4 by 4 dense matrices over Univariate Polynomial Ring in x over Rational Field

    Subdivisions are optional. If they are disabled, the columns need not line up::

        sage: B = matrix(QQ, 2, 3, range(6))
        sage: block_matrix([ [~A, B], [B, ~A] ], subdivide=False)
        [-5/12   3/8     0     1     2]
        [  1/4  -1/8     3     4     5]
        [    0     1     2 -5/12   3/8]
        [    3     4     5   1/4  -1/8]

    Without subdivisions it also deduces dimensions for scalars if possible::

        sage: C = matrix(ZZ, 1, 2, range(2))
        sage: block_matrix([ [ C, 0 ], [ 3, 4 ], [ 5, 6, C ] ], subdivide=False )
        [0 1 0 0]
        [3 0 4 0]
        [0 3 0 4]
        [5 6 0 1]

    If all submatrices are sparse (unless there are none at all), the result
    will be a sparse matrix. Otherwise it will be dense by default. The
    ``sparse`` keyword can be used to override this::

        sage: A = Matrix(ZZ, 2, 2, [0, 1, 0, 0], sparse=True)
        sage: block_matrix([ [ A ], [ A ] ]).parent()
        Full MatrixSpace of 4 by 2 sparse matrices over Integer Ring
        sage: block_matrix([ [ A ], [ A ] ], sparse=False).parent()
        Full MatrixSpace of 4 by 2 dense matrices over Integer Ring

    Consecutive zero submatrices are consolidated.  ::

        sage: B = matrix(2, range(4))
        sage: C = matrix(2, 8, range(16))
        sage: block_matrix(2, [[B,0,0,B],[C]], subdivide=False)
        [ 0  1  0  0  0  0  0  1]
        [ 2  3  0  0  0  0  2  3]
        [ 0  1  2  3  4  5  6  7]
        [ 8  9 10 11 12 13 14 15]

    Ambiguity is not tolerated.  ::

        sage: B = matrix(2, range(4))
        sage: C = matrix(2, 8, range(16))
        sage: block_matrix(2, [[B,0,B,0],[C]], subdivide=False)
        Traceback (most recent call last):
        ...
        ValueError: insufficient information to determine submatrix widths

    Giving only a flat list of submatrices does not work::

        sage: A = matrix(2, 3, range(6))
        sage: B = matrix(3, 3, range(9))
        sage: block_matrix([A, A, B, B])
        Traceback (most recent call last):
        ...
        ValueError: must specify either nrows or ncols

    Vectors are interpreted as column vectors::

        sage: m = matrix([[1, 2], [3, 4]])
        sage: v = vector([5, 6])
        sage: matrix.block([
        ....:     [m, v],
        ....:     [0, 1],
        ....:     ])
        [1 2|5]
        [3 4|6]
        [---+-]
        [0 0|1]

    To interpret vectors as row vectors, :meth:`~sage.modules.free_module_element.FreeModuleElement.row`
    can be used::

        sage: matrix.block([
        ....:     [m, 0],
        ....:     [v.row(), 1],
        ....:     ])
        [1 2|0]
        [3 4|0]
        [---+-]
        [5 6|1]

    TESTS::

        sage: A = matrix(ZZ, 2, 2, [3,5,8,13])
        sage: block_matrix(A)
        [ 3  5]
        [ 8 13]
        sage: block_matrix([[A, 0r], [1r, A]])
        [ 3  5| 0  0]
        [ 8 13| 0  0]
        [-----+-----]
        [ 1  0| 3  5]
        [ 0  1| 8 13]
        sage: block_matrix([[A, 3r+1jr], [1r, A]])
        [        3.0         5.0|3.0 + 1.0*I         0.0]
        [        8.0        13.0|        0.0 3.0 + 1.0*I]
        [-----------------------+-----------------------]
        [        1.0         0.0|        3.0         5.0]
        [        0.0         1.0|        8.0        13.0]

    This is not implemented for now, but it might be implemented in the future
    if there is no ambiguity::

        sage: matrix.block([
        ....:     [m, 0],
        ....:     [v, 1],
        ....:     ])
        Traceback (most recent call last):
        ...
        ValueError: incompatible submatrix widths

    Error reporting when non-ring elements are passed in::

        sage: matrix.block([
        ....:     ["abc"],
        ....:     ])
        Traceback (most recent call last):
        ...
        ValueError: an element of parent <class \'str\'> was passed in,
         but only matrices, vectors and ring elements are accepted
        sage: matrix.block([
        ....:     [(1, 2)],
        ....:     ])
        Traceback (most recent call last):
        ...
        ValueError: an element of parent <class \'tuple\'> was passed in,
         but only matrices, vectors and ring elements are accepted
        sage: matrix.block([
        ....:     [[1, 2]],
        ....:     ])
        Traceback (most recent call last):
        ...
        ValueError: an element of parent <class \'list\'> was passed in,
         but only matrices, vectors and ring elements are accepted
        sage: matrix.block([
        ....:     [EllipticCurve(\'37a1\').0],
        ....:     ])
        Traceback (most recent call last):
        ...
        ValueError: an element of parent Abelian group of points on
         Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field was passed in,
         but only matrices, vectors and ring elements are accepted
    '''
@matrix_method
def block_diagonal_matrix(*sub_matrices, **kwds):
    """
    Create a block matrix whose diagonal block entries are given by
    sub_matrices, with zero elsewhere.

    See also :meth:`block_matrix`.

    EXAMPLES::

        sage: A = matrix(ZZ, 2, [1,2,3,4])
        sage: block_diagonal_matrix(A, A)
        [1 2|0 0]
        [3 4|0 0]
        [---+---]
        [0 0|1 2]
        [0 0|3 4]

    The sub-matrices need not be square::

        sage: B = matrix(QQ, 2, 3, range(6))
        sage: block_diagonal_matrix(~A, B)
        [  -2    1|   0    0    0]
        [ 3/2 -1/2|   0    0    0]
        [---------+--------------]
        [   0    0|   0    1    2]
        [   0    0|   3    4    5]
    """
@matrix_method
def jordan_block(eigenvalue, size, sparse: bool = False):
    """
    Return the Jordan block for the given eigenvalue with given size.

    INPUT:

    - ``eigenvalue`` -- eigenvalue for the diagonal entries of the block
    - ``size`` -- size of the square matrix
    - ``sparse`` -- (default: ``False``) if ``True``, return a sparse matrix

    EXAMPLES::

        sage: jordan_block(5, 3)
        [5 1 0]
        [0 5 1]
        [0 0 5]

    TESTS::

        sage: jordan_block(6.2, 'junk')
        Traceback (most recent call last):
        ...
        TypeError: size of Jordan block needs to be an integer, not junk
        sage: jordan_block(6.2, -1)
        Traceback (most recent call last):
        ...
        ValueError: size of Jordan block must be nonnegative, not -1
    """
@matrix_method
def companion_matrix(poly, format: str = 'right'):
    """
    Create a companion matrix from a monic polynomial.

    INPUT:

    - ``poly`` -- a univariate polynomial, or an iterable containing
      the coefficients of a polynomial, with low-degree coefficients first.
      The polynomial (or the polynomial implied by the coefficients) must
      be monic.  In other words, the leading coefficient must be one.
      A symbolic expression that might also be a polynomial is not
      proper input, see examples below.

    - ``format`` -- (default: ``'right'``) specifies one of four
      variations of a companion matrix.  Allowable values are
      ``'right'``, ``'left'``, ``'top'`` and ``'bottom'``, which indicates
      which border of the matrix contains the negatives of the coefficients.

    OUTPUT:

    A square matrix with a size equal to the degree of the polynomial.
    The returned matrix has ones above, or below the diagonal, and the
    negatives of the coefficients along the indicated border of the
    matrix (excepting the leading one coefficient).
    See the first examples below for precise illustrations.

    EXAMPLES:

    Each of the four possibilities.  Notice that the coefficients are
    specified and their negatives become the entries of the matrix.  The
    leading one must be given, but is not used.  The permutation matrix
    ``P`` is the identity matrix, with the columns reversed.  The last three
    statements test the general relationships between the four variants.  ::

        sage: poly = [-2, -3, -4, -5, -6, 1]
        sage: R = companion_matrix(poly, format='right'); R
        [0 0 0 0 2]
        [1 0 0 0 3]
        [0 1 0 0 4]
        [0 0 1 0 5]
        [0 0 0 1 6]
        sage: L = companion_matrix(poly, format='left'); L
        [6 1 0 0 0]
        [5 0 1 0 0]
        [4 0 0 1 0]
        [3 0 0 0 1]
        [2 0 0 0 0]
        sage: B = companion_matrix(poly, format='bottom'); B
        [0 1 0 0 0]
        [0 0 1 0 0]
        [0 0 0 1 0]
        [0 0 0 0 1]
        [2 3 4 5 6]
        sage: T = companion_matrix(poly, format='top'); T
        [6 5 4 3 2]
        [1 0 0 0 0]
        [0 1 0 0 0]
        [0 0 1 0 0]
        [0 0 0 1 0]

        sage: perm = Permutation([5, 4, 3, 2, 1])
        sage: P = perm.to_matrix()
        sage: L == P*R*P
        True
        sage: B == R.transpose()
        True
        sage: T == P*R.transpose()*P
        True

    A polynomial may be used as input, however a symbolic expression,
    even if it looks like a polynomial, is not regarded as such when used
    as input to this routine.  Obtaining the list of coefficients from a
    symbolic polynomial is one route to the companion matrix. ::

        sage: x = polygen(QQ, 'x')
        sage: p = x^3 - 4*x^2 + 8*x - 12
        sage: companion_matrix(p)
        [ 0  0 12]
        [ 1  0 -8]
        [ 0  1  4]

        sage: # needs sage.symbolic
        sage: y = var('y')
        sage: q = y^3 - 2*y + 1
        sage: companion_matrix(q)
        Traceback (most recent call last):
        ...
        TypeError: input must be a polynomial (not a symbolic expression, see docstring),
        or other iterable, not y^3 - 2*y + 1
        sage: coeff_list = [q(y=0)] + [q.coefficient(y^k)
        ....:                          for k in range(1, q.degree(y) + 1)]
        sage: coeff_list
        [1, -2, 0, 1]
        sage: companion_matrix(coeff_list)
        [ 0  0 -1]
        [ 1  0  2]
        [ 0  1  0]

    The minimal polynomial of a companion matrix is equal to the
    polynomial used to create it.  Used in a block diagonal
    construction, they can be used to create matrices with
    any desired minimal polynomial, or characteristic polynomial.  ::

        sage: t = polygen(QQ, 't')
        sage: p = t^12 - 7*t^4 + 28*t^2 - 456
        sage: C = companion_matrix(p, format='top')
        sage: q = C.minpoly(var='t'); q                                                 # needs sage.libs.pari
        t^12 - 7*t^4 + 28*t^2 - 456
        sage: p == q                                                                    # needs sage.libs.pari
        True

        sage: p = t^3 + 3*t - 8
        sage: q = t^5 + t - 17
        sage: A = block_diagonal_matrix( companion_matrix(p),
        ....:                            companion_matrix(p^2),
        ....:                            companion_matrix(q),
        ....:                            companion_matrix(q) )
        sage: A.charpoly(var='t').factor()                                              # needs sage.libs.pari
        (t^3 + 3*t - 8)^3 * (t^5 + t - 17)^2
        sage: A.minpoly(var='t').factor()                                               # needs sage.libs.pari
        (t^3 + 3*t - 8)^2 * (t^5 + t - 17)

    TESTS::

        sage: companion_matrix([4, 5, 1], format='junk')
        Traceback (most recent call last):
        ...
        ValueError: format must be 'right', 'left', 'top' or 'bottom', not junk

        sage: companion_matrix(sin(x))                                                  # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: input must be a polynomial (not a symbolic expression, see docstring),
        or other iterable, not sin(x)

        sage: companion_matrix([2, 3, 896])
        Traceback (most recent call last):
        ...
        ValueError: polynomial (or the polynomial implied by coefficients) must be monic,
        not a leading coefficient of 896

        sage: F.<a> = GF(2^2)                                                           # needs sage.rings.finite_rings
        sage: companion_matrix([4/3, a+1, 1])                                           # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        TypeError: unable to find common ring for coefficients from polynomial

        sage: A = companion_matrix([1])
        sage: A.nrows(); A.ncols()
        0
        0

        sage: A = companion_matrix([])
        Traceback (most recent call last):
        ...
        ValueError: polynomial cannot be specified by an empty list

        sage: companion_matrix([QQ.one()]).parent()
        Full MatrixSpace of 0 by 0 dense matrices over Rational Field

    AUTHOR:

    - Rob Beezer (2011-05-19)
    """
@matrix_method
def random_rref_matrix(parent, num_pivots):
    """
    Generate a matrix in reduced row-echelon form with a specified number of nonzero rows.

    INPUT:

    - ``parent`` -- a matrix space specifying the base ring, dimensions and
      representation (dense/sparse) for the result.  The base ring must be exact.

    - ``num_pivots`` -- the number of nonzero rows in the result, i.e. the rank

    OUTPUT:

    A matrix in reduced row echelon form with ``num_pivots`` nonzero rows. If the
    base ring is `ZZ` or `QQ` then the entries are all integers.

    .. NOTE::

        It is easiest to use this function via a call to the
        :func:`~sage.matrix.constructor.random_matrix`
        function with the ``algorithm='echelon_form'`` keyword.  We provide
        one example accessing this function directly, while the remainder will
        use this more general function.

    EXAMPLES:

    Matrices generated are in reduced row-echelon form with specified rank. If the
    base ring is `QQ` the result has only integer entries.  ::

        sage: from sage.matrix.constructor import random_rref_matrix
        sage: matrix_space = sage.matrix.matrix_space.MatrixSpace(QQ, 5, 6)
        sage: A = random_rref_matrix(matrix_space, num_pivots=4); A  # random
        [ 1  0  0 -6  0 -3]
        [ 0  1  0  2  0  3]
        [ 0  0  1 -4  0 -2]
        [ 0  0  0  0  1  3]
        [ 0  0  0  0  0  0]
        sage: A.base_ring()
        Rational Field
        sage: (A.nrows(), A.ncols())
        (5, 6)
        sage: A in sage.matrix.matrix_space.MatrixSpace(ZZ, 5, 6)
        True
        sage: A.rank()
        4
        sage: A == A.rref()
        True

    Matrices can be generated over other exact rings. ::

        sage: B = random_matrix(FiniteField(7), 4, 4,  # random
        ....:                   algorithm='echelon_form', num_pivots=3); B
        [1 0 0 0]
        [0 1 0 6]
        [0 0 1 1]
        [0 0 0 0]
        sage: B.rank() == 3
        True
        sage: B.base_ring()
        Finite Field of size 7
        sage: B == B.rref()
        True

    TESTS:

    Rank zero::

        sage: random_matrix(QQ, 1, 1, algorithm='echelon_form', num_pivots=0)
        [0]

    Rank of a matrix must be an integer. ::

        sage: random_matrix(QQ, 120, 56, algorithm='echelon_form', num_pivots=61/2)
        Traceback (most recent call last):
        ...
        TypeError: the number of pivots must be an integer

    Matrices must be generated over exact fields. ::

        sage: random_matrix(RR, 40, 88, algorithm='echelon_form', num_pivots=39)
        Traceback (most recent call last):
        ...
        TypeError: the base ring must be exact

    Matrices must have the number of pivot columns be less than or equal to the number of rows. ::

        sage: C = random_matrix(ZZ, 6,4, algorithm='echelon_form', num_pivots=7); C
        Traceback (most recent call last):
        ...
        ValueError: number of pivots cannot exceed the number of rows or columns

    Matrices must have the number of pivot columns be less than or equal to the number of columns. ::

        sage: D = random_matrix(QQ, 1,3, algorithm='echelon_form', num_pivots=5); D
        Traceback (most recent call last):
        ...
        ValueError: number of pivots cannot exceed the number of rows or columns

    Matrices must have the number of pivot columns be greater than zero. ::

        sage: random_matrix(QQ, 5, 4, algorithm='echelon_form', num_pivots=-1)
        Traceback (most recent call last):
        ...
        ValueError: the number of pivots must be zero or greater

    AUTHOR:

    Billy Wonderly (2010-07)
    """
@matrix_method
def random_echelonizable_matrix(parent, rank, upper_bound=None, max_tries: int = 100):
    """
    Generate a matrix of a desired size and rank, over a desired ring, whose reduced
    row-echelon form has only integral values.

    INPUT:

    - ``parent`` -- a matrix space specifying the base ring, dimensions and
      representation (dense/sparse) for the result.  The base ring must be exact.

    - ``rank`` -- rank of result, i.e the number of nonzero rows in the
      reduced row echelon form

    - ``upper_bound`` -- if designated, size control of the matrix entries is desired
      Set ``upper_bound`` to 1 more than the maximum value entries can achieve.
      If ``None``, no size control occurs. But see the warning below.  (default: ``None``)

    - ``max_tries`` -- if designated, number of tries used to generate each new random row;s
      only matters when upper_bound!=None. Used to prevent endless looping. (default: 100)

    OUTPUT: a matrix not in reduced row-echelon form with the desired
    dimensions and properties

    .. warning::

        When ``upper_bound`` is set, it is possible for this constructor to
        fail with a :exc:`ValueError`.  This may happen when the ``upper_bound``,
        ``rank`` and/or matrix dimensions are all so small that it becomes
        infeasible or unlikely to create the requested matrix.  If you *must*
        have this routine return successfully, do not set ``upper_bound``.

    .. NOTE::

        It is easiest to use this function via a call to the
        :func:`~sage.matrix.constructor.random_matrix`
        function with the ``algorithm='echelonizable'`` keyword.  We provide
        one example accessing this function directly, while the remainder will
        use this more general function.

    EXAMPLES:

    Generated matrices have the desired dimensions, rank and entry size. The
    matrix in reduced row-echelon form has only integer entries. ::

        sage: from sage.matrix.constructor import random_echelonizable_matrix
        sage: matrix_space = sage.matrix.matrix_space.MatrixSpace(QQ, 5, 6)
        sage: A = random_echelonizable_matrix(matrix_space, rank=4, upper_bound=40)
        sage: A.rank()
        4
        sage: max(map(abs,A.list())) < 40
        True
        sage: A.rref() == A.rref().change_ring(ZZ)
        True

    An example with default settings (i.e. no entry size control). ::

        sage: C = random_matrix(QQ, 6, 7, algorithm='echelonizable', rank=5)
        sage: C.rank()
        5
        sage: C.rref() == C.rref().change_ring(ZZ)
        True

    A matrix without size control may have very large entry sizes. ::

        sage: D = random_matrix(ZZ, 7, 8, algorithm='echelonizable', rank=6); D  # random
        [    1     2     8   -35  -178  -239  -284   778]
        [    4     9    37  -163  -827 -1111 -1324  3624]
        [    5     6    21   -88  -454  -607  -708  1951]
        [   -4    -5   -22    97   491   656   779 -2140]
        [    4     4    13   -55  -283  -377  -436  1206]
        [    4    11    43  -194  -982 -1319 -1576  4310]
        [   -1    -2   -13    59   294   394   481 -1312]

    Matrices can be generated over any exact ring. ::

        sage: # needs sage.rings.finite_rings
        sage: F.<a> = GF(2^3)
        sage: B = random_matrix(F, 4, 5, algorithm='echelonizable', rank=4,
        ....:                   upper_bound=None)
        sage: B.rank()
        4
        sage: B.base_ring() is F
        True

    Square matrices over ZZ or QQ with full rank are always unimodular. ::

        sage: E = random_matrix(QQ, 7, 7, algorithm='echelonizable', rank=7)
        sage: det(E)
        1
        sage: E = random_matrix(ZZ, 7, 7, algorithm='echelonizable', rank=7)
        sage: det(E)
        1

    TESTS:

    Matrices must have a rank zero or greater, and less than
    both the number of rows and the number of columns. ::

        sage: random_matrix(QQ, 3, 4, algorithm='echelonizable', rank=-1)
        Traceback (most recent call last):
        ...
        ValueError: matrices must have rank zero or greater.
        sage: random_matrix(QQ, 3, 8, algorithm='echelonizable', rank=4)
        Traceback (most recent call last):
        ...
        ValueError: matrices cannot have rank greater than min(ncols,nrows).
        sage: random_matrix(QQ, 8, 3, algorithm='echelonizable', rank=4)
        Traceback (most recent call last):
        ...
        ValueError: matrices cannot have rank greater than min(ncols,nrows).

    The base ring must be exact. ::

        sage: random_matrix(RR, 3, 3, algorithm='echelonizable', rank=2)
        Traceback (most recent call last):
        ...
        TypeError: the base ring must be exact

    Works for rank==1, too. ::

        sage: random_matrix(QQ, 3, 3, algorithm='echelonizable', rank=1).ncols()
        3


    AUTHOR:

    Billy Wonderly (2010-07)
    """
@matrix_method
def random_subspaces_matrix(parent, rank=None):
    """
    Create a matrix of the designated size and rank whose right and
    left null spaces, column space, and row space have desirable
    properties that simplify the subspaces.

    INPUT:

    - ``parent`` -- a matrix space specifying the base ring, dimensions, and
      representation (dense/sparse) for the result.  The base ring must be exact.

    - ``rank`` -- the desired rank of the return matrix (default: ``None``)

    OUTPUT:

    A matrix whose natural basis vectors for its four subspaces, when
    computed, have reasonably sized, integral valued, entries.

    .. NOTE::

        It is easiest to use this function via a call to the
        :func:`~sage.matrix.constructor.random_matrix`
        function with the ``algorithm='subspaces'`` keyword.  We provide
        one example accessing this function directly, while the remainder will
        use this more general function.

    EXAMPLES:

    A 6x8 matrix with designated rank of 3.  The four subspaces are
    determined using one simple routine in which we augment the
    original matrix with the equal row dimension identity matrix.  The
    resulting matrix is then put in reduced row-echelon form and the
    subspaces can then be determined by analyzing subdivisions of this
    matrix. See the four subspaces routine in [Bee]_ for more. ::

        sage: from sage.matrix.constructor import random_subspaces_matrix
        sage: matrix_space = sage.matrix.matrix_space.MatrixSpace(QQ, 6, 8)
        sage: B = random_subspaces_matrix(matrix_space, rank=3)
        sage: B.rank()
        3
        sage: B.nullity()
        3
        sage: (B.nrows(), B.ncols())
        (6, 8)
        sage: all(x in ZZ for x in B.list())
        True
        sage: B_expanded = B.augment(identity_matrix(6)).rref()
        sage: all(x in ZZ for x in B_expanded.list())
        True

    Check that we fixed :issue:`10543` (echelon forms should be immutable)::

        sage: B_expanded.is_immutable()
        True

    We want to modify B_expanded, so replace it with a copy::

        sage: B_expanded = copy(B_expanded)
        sage: B_expanded.subdivide(B.nrows()-B.nullity(), B.ncols())
        sage: C = B_expanded.subdivision(0, 0)
        sage: L = B_expanded.subdivision(1, 1)
        sage: B.right_kernel() == C.right_kernel()
        True
        sage: B.row_space() == C.row_space()
        True
        sage: B.column_space() == L.right_kernel()
        True
        sage: B.left_kernel() == L.row_space()
        True

    A matrix to show that the null space of the L matrix is the column space of the starting matrix. ::

        sage: A = random_matrix(QQ, 5, 7, algorithm='subspaces', rank=None)
        sage: (A.nrows(), A.ncols())
        (5, 7)
        sage: all(x in ZZ for x in A.list())
        True
        sage: A_expanded = A.augment(identity_matrix(5)).rref()
        sage: all(x in ZZ for x in A_expanded.list())
        True
        sage: C = A_expanded.submatrix(0, 0, A.nrows() - A.nullity(), A.ncols())
        sage: L = A_expanded.submatrix(A.nrows() - A.nullity(), A.ncols())
        sage: A.right_kernel() == C.right_kernel()
        True
        sage: A.row_space() == C.row_space()
        True
        sage: A.column_space() == L.right_kernel()
        True
        sage: A.left_kernel() == L.row_space()
        True

    TESTS:

    The designated rank of the L matrix cannot be greater than the
    number of desired rows, nor can the rank be negative. ::

        sage: random_matrix(QQ, 19, 20, algorithm='subspaces', rank=21)
        Traceback (most recent call last):
        ...
        ValueError: rank cannot exceed the number of rows or columns.
        sage: random_matrix(QQ, 19, 20, algorithm='subspaces', rank=-1)
        Traceback (most recent call last):
        ...
        ValueError: matrices must have rank zero or greater.

    AUTHOR:

    Billy Wonderly (2010-07)
    """
@matrix_method
def random_unimodular_matrix(parent, upper_bound=None, max_tries: int = 100):
    """
    Generate a random unimodular (determinant 1) matrix of a desired size over a desired ring.

    INPUT:

    - ``parent`` -- a matrix space specifying the base ring, dimensions
      and representation (dense/sparse) for the result.  The base ring
      must be exact.

    - ``upper_bound`` -- for large matrices over QQ or ZZ,
      ``upper_bound`` is the largest value matrix entries can achieve.  But
      see the warning below.

    - ``max_tries`` -- if designated, number of tries used to generate each new random row;
      only matters when upper_bound!=None. Used to prevent endless looping. (default: 100)

    A matrix not in reduced row-echelon form with the desired dimensions and properties.

    OUTPUT: an invertible matrix with the desired properties and determinant 1

    .. warning::

        When ``upper_bound`` is set, it is possible for this constructor to
        fail with a :exc:`ValueError`.  This may happen when the ``upper_bound``,
        ``rank`` and/or matrix dimensions are all so small that it becomes
        infeasible or unlikely to create the requested matrix.  If you *must*
        have this routine return successfully, do not set ``upper_bound``.

    .. NOTE::

        It is easiest to use this function via a call to the
        :func:`~sage.matrix.constructor.random_matrix`
        function with the ``algorithm='unimodular'`` keyword.  We provide
        one example accessing this function directly, while the remainder will
        use this more general function.

    EXAMPLES:

    A matrix size 5 over QQ. ::

        sage: from sage.matrix.constructor import random_unimodular_matrix
        sage: matrix_space = sage.matrix.matrix_space.MatrixSpace(QQ, 5)
        sage: A = random_unimodular_matrix(matrix_space)
        sage: det(A)
        1

    A matrix size 6 with entries no larger than 50. ::

        sage: B = random_matrix(ZZ, 7, algorithm='unimodular', upper_bound=50)
        sage: det(B)
        1
        sage: all(abs(b) < 50 for b in B.list())
        True

    A matrix over the number Field in `y` with defining polynomial `y^2-2y-2`. ::

        sage: # needs sage.rings.number_field
        sage: y = polygen(ZZ, 'y')
        sage: K = NumberField(y^2 - 2*y - 2, 'y')
        sage: C = random_matrix(K, 3, algorithm='unimodular')
        sage: C  # random
        [      -1/7*y + 47/35       3/5*y - 127/70 -2917/70*y + 4419/70]
        [                   1          1/2*y - 1/2     -104/3*y + 211/6]
        [         1/3*y - 1/3                y - 1      -35/6*y - 149/6]
        sage: det(C)
        1
        sage: C.base_ring() is K
        True

    TESTS:

    Unimodular matrices are square. ::

        sage: random_matrix(QQ, 5, 6, algorithm='unimodular')
        Traceback (most recent call last):
        ...
        TypeError: a unimodular matrix must be square.

    Only matrices over ZZ and QQ can have size control. ::

        sage: F.<a> = GF(5^7)                                                           # needs sage.rings.finite_rings
        sage: random_matrix(F, 5, algorithm='unimodular', upper_bound=20)               # needs sage.rings.finite_rings
        Traceback (most recent call last):
        ...
        TypeError: only matrices over ZZ or QQ can have size control.

    AUTHOR:

    Billy Wonderly (2010-07)
    """
@matrix_method
def random_unitary_matrix(parent):
    """
    Generate a random (square) unitary matrix of a given size
    with entries in a subfield of the complex numbers.

    INPUT:

    - ``parent`` -- :class:`sage.matrix.matrix_space.MatrixSpace`; a
      square matrix space over a subfield of the complex numbers
      having characteristic zero.

    OUTPUT:

    A random unitary matrix in ``parent``. A :exc:`ValueError` is
    raised if ``parent`` is not an appropriate matrix space (is not
    square, or is not over a usable field).

    ALGORITHM:

    The method described by Liebeck and Osborne [LieOs1991]_ is used
    almost verbatim.

    .. WARNING:

        Inexact rings may violate your expectations; in particular,
        the rings ``RR`` and ``CC`` are accepted by this method but
        the resulting matrix will usually fail the ``is_unitary()``
        check due to numerical issues.

    EXAMPLES:

    This function is not in the global namespace and must be imported
    before being used::

        sage: from sage.matrix.constructor import random_unitary_matrix

    Matrices with rational entries::

        sage: n = ZZ.random_element(10)
        sage: MS = MatrixSpace(QQ, n)
        sage: U = random_unitary_matrix(MS)
        sage: U.is_unitary() and U in MS
        True

    Matrices over a quadraric field::

        sage: n = ZZ.random_element(10)
        sage: K = QuadraticField(-1,'i')
        sage: MS = MatrixSpace(K, n)
        sage: U = random_unitary_matrix(MS)
        sage: U.is_unitary() and U in MS
        True

    Matrices with entries in the algebraic real field (slow)::

        sage: # long time
        sage: n = ZZ.random_element(4)
        sage: MS = MatrixSpace(AA, n)
        sage: U = random_unitary_matrix(MS)
        sage: U.is_unitary() and U in MS
        True

    Matrices with entries in the algebraic field (slower yet)::

        sage: # long time
        sage: n = ZZ.random_element(2)
        sage: MS = MatrixSpace(QQbar, n)
        sage: U = random_unitary_matrix(MS)
        sage: U.is_unitary() and U in MS
        True

    Double-precision real/complex matrices can be constructed as
    well::

        sage: n = ZZ.random_element(10)
        sage: MS = MatrixSpace(RDF, n)
        sage: U = random_unitary_matrix(MS)
        sage: U.is_unitary() and U in MS
        True
        sage: MS = MatrixSpace(CDF, n)
        sage: U = random_unitary_matrix(MS)
        sage: U.is_unitary() and U in MS
        True

    TESTS:

    We raise a :exc:`ValueError` if the supplied matrix space is not
    square::

        sage: MS = MatrixSpace(QQ, 3, 4)
        sage: random_unitary_matrix(MS)
        Traceback (most recent call last):
        ...
        ValueError: parent must be square

    Likewise if its base ring is not a field::

        sage: MS = MatrixSpace(ZZ, 3)
        sage: random_unitary_matrix(MS)
        Traceback (most recent call last):
        ...
        ValueError: base ring of parent must be a field

    Likewise if that field is not of characteristic zero::

        sage: MS = MatrixSpace(GF(5), 3)
        sage: random_unitary_matrix(MS)
        Traceback (most recent call last):
        ...
        ValueError: base ring of parent must have characteristic zero

    Likewise if that field is not a subfield of the complex numbers::

        sage: R = Qp(7)
        sage: R.characteristic()
        0
        sage: MS = MatrixSpace(R, 3)
        sage: random_unitary_matrix(MS)
        Traceback (most recent call last):
        ...
        ValueError: base ring of parent must be a subfield of the complex
        numbers
    """
@matrix_method
def random_diagonalizable_matrix(parent, eigenvalues=None, dimensions=None):
    '''
    Create a random matrix that diagonalizes nicely.

    To be used as a teaching tool. The eigenvalues will be elements of the
    base ring. If the base ring used is ``QQ`` then the returned matrix will
    have integer eigenvalues.

    INPUT:

    If eigenvalues and dimensions are not specified in a list,
    they will be assigned randomly.

    - ``parent`` -- the desired parent of the square matrix (a matrix space)

    - ``eigenvalues`` -- the list of desired eigenvalues (default=None)

    - ``dimensions`` -- the list of dimensions corresponding to each
      eigenspace (default=None)

    OUTPUT:

    A square, diagonalizable, matrix. Elements of the matrix are elements
    of the base ring. If the ring used is ``QQ`` then we have integer entries,
    and the eigenspaces of this matrix, if computed by hand, gives basis
    vectors with only integer entries.

    .. NOTE::

        It is easiest to use this function via a call to the
        :func:`~sage.matrix.constructor.random_matrix`
        function with the ``algorithm=\'diagonalizable\'`` keyword.  We provide
        one example accessing this function directly, while the remainder will
        use this more general function.

    EXAMPLES:

    A diagonalizable matrix, size 5. ::

        sage: from sage.matrix.constructor import random_diagonalizable_matrix
        sage: matrix_space = sage.matrix.matrix_space.MatrixSpace(QQ, 5)
        sage: A = random_diagonalizable_matrix(matrix_space)

        sage: # needs sage.rings.number_field
        sage: eigenvalues = A.eigenvalues()
        sage: S = A.right_eigenmatrix()[1]
        sage: eigenvalues2 = (S.inverse()*A*S).diagonal()
        sage: sorted(eigenvalues) == sorted(eigenvalues2)
        True

    A diagonalizable matrix with eigenvalues and dimensions designated,
    with a check that if eigenvectors were calculated by hand
    entries would all be integers. ::

        sage: eigenvalues = [ZZ.random_element() for _ in range(3)]
        sage: B = random_matrix(QQ, 6, algorithm=\'diagonalizable\',
        ....:                   eigenvalues=eigenvalues, dimensions=[2,3,1])
        sage: all(x in ZZ for x in (B-(-12*identity_matrix(6))).rref().list())
        True
        sage: all(x in ZZ for x in (B-(4*identity_matrix(6))).rref().list())
        True
        sage: all(x in ZZ for x in (B-(6*identity_matrix(6))).rref().list())
        True

        sage: # needs sage.rings.number_field
        sage: S = B.right_eigenmatrix()[1]
        sage: eigenvalues2 = (S.inverse()*B*S).diagonal()
        sage: all(e in eigenvalues for e in eigenvalues2)
        True

    Matrices over finite fields are also supported::

        sage: K = GF(3)
        sage: M = random_matrix(K, 3, 3, algorithm="diagonalizable")
        sage: M.parent()
        Full MatrixSpace of 3 by 3 dense matrices over Finite Field of size 3
        sage: M.is_diagonalizable()
        True
        sage: M  # random
        [0 0 1]
        [2 1 1]
        [1 0 0]

    TESTS:

    Eigenvalues must all be elements of the ring. ::

        sage: random_matrix(QQ, 3, algorithm=\'diagonalizable\',                          # needs sage.symbolic
        ....:               eigenvalues=[2+I, 2-I, 2], dimensions=[1,1,1])
        Traceback (most recent call last):
        ...
        TypeError: eigenvalues must be elements of the corresponding ring.

    Diagonal matrices must be square. ::

        sage: random_matrix(QQ, 5, 7, algorithm=\'diagonalizable\', eigenvalues=[-5,2,-3], dimensions=[1,1,3])
        Traceback (most recent call last):
        ...
        TypeError: a diagonalizable matrix must be square.

    A list of eigenvalues must be accompanied with a list of dimensions. ::

        sage: random_matrix(QQ,10,algorithm=\'diagonalizable\',eigenvalues=[4,8])
        Traceback (most recent call last):
        ...
        ValueError: the list of eigenvalues must have a list of dimensions corresponding to each eigenvalue.

    A list of dimensions must be accompanied with a list of eigenvalues. ::

        sage: random_matrix(QQ, 10,algorithm=\'diagonalizable\',dimensions=[2,2,4,2])
        Traceback (most recent call last):
        ...
        ValueError: the list of dimensions must have a list of corresponding eigenvalues.

    The sum of the eigenvalue dimensions must equal the size of the matrix. ::

        sage: random_matrix(QQ,12,algorithm=\'diagonalizable\',eigenvalues=[4,2,6,-1],dimensions=[2,3,5,1])
        Traceback (most recent call last):
        ...
        ValueError: the size of the matrix must equal the sum of the dimensions.

    Each eigenspace dimension must be at least 1. ::

        sage: random_matrix(QQ,9,algorithm=\'diagonalizable\',eigenvalues=[-15,22,8,-4,90,12],dimensions=[4,2,2,4,-3,0])
        Traceback (most recent call last):
        ...
        ValueError: eigenspaces must have a dimension of at least 1.

    Each eigenvalue must have a corresponding eigenspace dimension. ::

        sage: random_matrix(QQ,12,algorithm=\'diagonalizable\',eigenvalues=[4,2,6,-1],dimensions=[4,3,5])
        Traceback (most recent call last):
        ...
        ValueError: each eigenvalue must have a corresponding dimension and each dimension a corresponding eigenvalue.

    Each dimension must have an eigenvalue paired to it. ::

        sage: random_matrix(QQ,12,algorithm=\'diagonalizable\',eigenvalues=[4,2,6],dimensions=[2,3,5,2])
        Traceback (most recent call last):
        ...
        ValueError: each eigenvalue must have a corresponding dimension and each dimension a corresponding eigenvalue.

    .. TODO::

        Modify the routine to allow for complex eigenvalues.

    AUTHOR:

    Billy Wonderly (2010-07)
    '''
@matrix_method
def vector_on_axis_rotation_matrix(v, i, ring=None):
    """
    Return a rotation matrix `M` such that `det(M)=1` sending the vector
    `v` on the `i`-th axis so that all other coordinates of `Mv` are zero.

    .. NOTE::

        Such a matrix is not uniquely determined. This function returns one
        such matrix.

    INPUT:

    - ``v`` -- vector
    - ``i`` -- integer
    - ``ring`` -- ring (default: ``None``) of the resulting matrix

    OUTPUT: a matrix

    EXAMPLES::

        sage: from sage.matrix.constructor import vector_on_axis_rotation_matrix
        sage: v = vector((1,2,3))
        sage: vector_on_axis_rotation_matrix(v, 2) * v                                  # needs sage.symbolic
        (0, 0, sqrt(14))
        sage: vector_on_axis_rotation_matrix(v, 1) * v                                  # needs sage.symbolic
        (0, sqrt(14), 0)
        sage: vector_on_axis_rotation_matrix(v, 0) * v                                  # needs sage.symbolic
        (sqrt(14), 0, 0)

    ::

        sage: # needs sage.symbolic
        sage: x,y = var('x,y')
        sage: v = vector((x,y))
        sage: vector_on_axis_rotation_matrix(v, 1)
        [ y/sqrt(x^2 + y^2) -x/sqrt(x^2 + y^2)]
        [ x/sqrt(x^2 + y^2)  y/sqrt(x^2 + y^2)]
        sage: vector_on_axis_rotation_matrix(v, 0)
        [ x/sqrt(x^2 + y^2)  y/sqrt(x^2 + y^2)]
        [-y/sqrt(x^2 + y^2)  x/sqrt(x^2 + y^2)]
        sage: vector_on_axis_rotation_matrix(v, 0) * v
        (x^2/sqrt(x^2 + y^2) + y^2/sqrt(x^2 + y^2), 0)
        sage: vector_on_axis_rotation_matrix(v, 1) * v
        (0, x^2/sqrt(x^2 + y^2) + y^2/sqrt(x^2 + y^2))

    ::

        sage: v = vector((1,2,3,4))
        sage: vector_on_axis_rotation_matrix(v, 0) * v                                  # needs sage.symbolic
        (sqrt(30), 0, 0, 0)
        sage: vector_on_axis_rotation_matrix(v, 0, ring=RealField(10))
        [ 0.18  0.37  0.55  0.73]
        [-0.98 0.068  0.10  0.14]
        [ 0.00 -0.93  0.22  0.30]
        [ 0.00  0.00 -0.80  0.60]
        sage: vector_on_axis_rotation_matrix(v, 0, ring=RealField(10)) * v
        (5.5, 0.00..., 0.00..., 0.00...)

    AUTHORS:

    Sébastien Labbé (April 2010)
    """
@matrix_method
def ith_to_zero_rotation_matrix(v, i, ring=None):
    """
    Return a rotation matrix that sends the `i`-th coordinates of the
    vector v to zero by doing a rotation with the `(i-1)`-th coordinate.

    INPUT:

    - ``v`` -- vector
    - ``i`` -- integer
    - ``ring`` -- ring (default: ``None``) of the resulting matrix

    OUTPUT: a matrix

    EXAMPLES::

        sage: from sage.matrix.constructor import ith_to_zero_rotation_matrix
        sage: v = vector((1,2,3))
        sage: ith_to_zero_rotation_matrix(v, 2)                                         # needs sage.symbolic
        [             1              0              0]
        [             0  2/13*sqrt(13)  3/13*sqrt(13)]
        [             0 -3/13*sqrt(13)  2/13*sqrt(13)]
        sage: ith_to_zero_rotation_matrix(v, 2) * v                                     # needs sage.symbolic
        (1, sqrt(13), 0)

    ::

        sage: ith_to_zero_rotation_matrix(v, 0)                                         # needs sage.symbolic
        [ 3/10*sqrt(10)              0 -1/10*sqrt(10)]
        [             0              1              0]
        [ 1/10*sqrt(10)              0  3/10*sqrt(10)]
        sage: ith_to_zero_rotation_matrix(v, 1)                                         # needs sage.symbolic
        [ 1/5*sqrt(5)  2/5*sqrt(5)            0]
        [-2/5*sqrt(5)  1/5*sqrt(5)            0]
        [           0            0            1]
        sage: ith_to_zero_rotation_matrix(v, 2)                                         # needs sage.symbolic
        [             1              0              0]
        [             0  2/13*sqrt(13)  3/13*sqrt(13)]
        [             0 -3/13*sqrt(13)  2/13*sqrt(13)]

    ::

        sage: ith_to_zero_rotation_matrix(v, 0) * v                                     # needs sage.symbolic
        (0, 2, sqrt(10))
        sage: ith_to_zero_rotation_matrix(v, 1) * v                                     # needs sage.symbolic
        (sqrt(5), 0, 3)
        sage: ith_to_zero_rotation_matrix(v, 2) * v                                     # needs sage.symbolic
        (1, sqrt(13), 0)

    Other ring::

        sage: ith_to_zero_rotation_matrix(v, 2, ring=RR)
        [  1.00000000000000  0.000000000000000  0.000000000000000]
        [ 0.000000000000000  0.554700196225229  0.832050294337844]
        [ 0.000000000000000 -0.832050294337844  0.554700196225229]
        sage: ith_to_zero_rotation_matrix(v, 2, ring=RDF)
        [                1.0                 0.0                 0.0]
        [                0.0  0.5547001962252291  0.8320502943378437]
        [                0.0 -0.8320502943378437  0.5547001962252291]

    On the symbolic ring::

        sage: # needs sage.symbolic
        sage: x,y,z = var('x,y,z')
        sage: v = vector((x,y,z))
        sage: ith_to_zero_rotation_matrix(v, 2)
        [                 1                  0                  0]
        [                 0  y/sqrt(y^2 + z^2)  z/sqrt(y^2 + z^2)]
        [                 0 -z/sqrt(y^2 + z^2)  y/sqrt(y^2 + z^2)]
        sage: ith_to_zero_rotation_matrix(v, 2) * v
        (x, y^2/sqrt(y^2 + z^2) + z^2/sqrt(y^2 + z^2), 0)

    TESTS::

        sage: ith_to_zero_rotation_matrix((1,0,0), 0)
        [ 0  0 -1]
        [ 0  1  0]
        [ 1  0  0]
        sage: ith_to_zero_rotation_matrix((1,0,0), 1)
        [1 0 0]
        [0 1 0]
        [0 0 1]
        sage: ith_to_zero_rotation_matrix((1,0,0), 2)
        [1 0 0]
        [0 1 0]
        [0 0 1]

    AUTHORS:

    Sébastien Labbé (April 2010)
    """
@matrix_method
def hilbert(dim, ring=...):
    """
    Return a Hilbert matrix of the given dimension.

    The `n` dimensional Hilbert matrix is a square matrix with entries being
    unit fractions,

    .. MATH::

        H_{ij} = \\frac{1}{i+j-1},\\qquad i, j = 1,\\ldots, n.

    For more information see the :wikipedia:`Hilbert_matrix`.

    INPUT:

    - ``dim`` -- integer; the dimension of the Hilbert matrix

    - ``ring`` -- base ring (default: `\\QQ`) of the resulting matrix

    EXAMPLES::

        sage: matrix.hilbert(5)
        [  1 1/2 1/3 1/4 1/5]
        [1/2 1/3 1/4 1/5 1/6]
        [1/3 1/4 1/5 1/6 1/7]
        [1/4 1/5 1/6 1/7 1/8]
        [1/5 1/6 1/7 1/8 1/9]
    """
@matrix_method
def vandermonde(v, ring=None):
    """
    Return a Vandermonde matrix of the given vector.

    The `n` dimensional Vandermonde matrix is a square matrix with columns
    being the powers of a given vector `v`,

    .. MATH::

        V_{ij} = v_i^{j-1},\\qquad i, j = 1,\\ldots, n.

    For more information see the :wikipedia:`Vandermonde_matrix`.

    INPUT:

    - ``v`` -- vector, the second column of the Vandermonde matrix

    - ``ring`` -- base ring (default: ``None``) of the resulting matrix

    EXAMPLES:

    A Vandermonde matrix of order three over the symbolic ring::

        sage: matrix.vandermonde(SR.var(['x0', 'x1', 'x2']))                            # needs sage.symbolic
        [   1   x0 x0^2]
        [   1   x1 x1^2]
        [   1   x2 x2^2]
    """
@matrix_method
def toeplitz(c, r, ring=None):
    """
    Return a Toeplitz matrix of given first column and first row.

    In a Toeplitz matrix, each descending diagonal from left to right is
    constant, such that:

    .. MATH:: T_{i,j} = T_{i+1, j+1}.

    For more information see the :wikipedia:`Toeplitz_matrix`.

    INPUT:

    - ``c`` -- vector, first column of the Toeplitz matrix

    - ``r`` -- vector, first row of the Toeplitz matrix, counting from the
      second column

    - ``ring`` -- base ring (default: ``None``) of the resulting matrix

    EXAMPLES:

    A rectangular Toeplitz matrix::

        sage: matrix.toeplitz([1..4], [5..6])
        [1 5 6]
        [2 1 5]
        [3 2 1]
        [4 3 2]

    The following `N\\times N` Toeplitz matrix arises in the discretization of
    boundary value problems::

        sage: N = 4
        sage: matrix.toeplitz([-2, 1] + [0]*(N-2), [1] + [0]*(N-2))
        [-2  1  0  0]
        [ 1 -2  1  0]
        [ 0  1 -2  1]
        [ 0  0  1 -2]
    """
@matrix_method
def hankel(c, r=None, ring=None):
    """
    Return a Hankel matrix of given first column and whose elements are zero
    below the first anti-diagonal.

    The Hankel matrix is symmetric and constant across the anti-diagonals,
    with elements

    .. MATH::

        H_{ij} = v_{i+j-1},\\qquad i = 1,\\ldots, m,~j = 1,\\ldots, n,

    where the vector `v_i = c_i` for `i = 1,\\ldots, m` and `v_{m+i} = r_i` for
    `i = 1, \\ldots, n-1` completely determines the Hankel matrix. If the last
    row, `r`, is not given, the Hankel matrix is square by default and `r = 0`.
    For more information see the :wikipedia:`Hankel_matrix`.

    INPUT:

    - ``c`` -- vector, first column of the Hankel matrix

    - ``r`` -- vector (default: ``None``); last row of the Hankel matrix, from
      the second to the last column

    - ``ring`` -- base ring (default: ``None``) of the resulting matrix

    EXAMPLES:

    A Hankel matrix with symbolic entries::

        sage: matrix.hankel(SR.var('a, b, c, d, e'))                                    # needs sage.symbolic
        [a b c d e]
        [b c d e 0]
        [c d e 0 0]
        [d e 0 0 0]
        [e 0 0 0 0]

    We can also pass the elements of the last row, starting at the second column::

        sage: matrix.hankel(SR.var('a, b, c, d, e'), SR.var('f, g, h, i'))              # needs sage.symbolic
        [a b c d e]
        [b c d e f]
        [c d e f g]
        [d e f g h]
        [e f g h i]

    A third order Hankel matrix in the integers::

        sage: matrix.hankel([1, 2, 3])
        [1 2 3]
        [2 3 0]
        [3 0 0]

    The second argument allows to customize the last row::

        sage: matrix.hankel([1..3], [7..10])
        [ 1  2  3  7  8]
        [ 2  3  7  8  9]
        [ 3  7  8  9 10]
    """
