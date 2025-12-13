from sage.arith.misc import GCD as GCD
from sage.matrix.constructor import Matrix as Matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import FreeModule as FreeModule
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ

@cached_method
def basis_of_short_vectors(self, show_lengths: bool = False):
    """
    Return a basis for `\\ZZ^n` made of vectors with minimal lengths `Q(v)`.

    OUTPUT: a tuple of vectors, and optionally a tuple of values for each vector

    This uses :pari:`qfminim`.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.basis_of_short_vectors()
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
        sage: Q.basis_of_short_vectors(True)
        (((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)), (1, 3, 5, 7))

    The returned vectors are immutable::

        sage: v = Q.basis_of_short_vectors()[0]
        sage: v
        (1, 0, 0, 0)
        sage: v[0] = 0
        Traceback (most recent call last):
        ...
        ValueError: vector is immutable; please change a copy instead (use copy())
    """
def short_vector_list_up_to_length(self, len_bound, up_to_sign_flag: bool = False):
    """
    Return a list of lists of short vectors `v`, sorted by length, with
    `Q(v) <` ``len_bound``.

    INPUT:

    - ``len_bound`` -- bound for the length of the vectors

    - ``up_to_sign_flag`` -- boolean (default: ``False``); if set to ``True``,
      then only one of the vectors of the pair `[v, -v]` is listed

    OUTPUT:

    A list of lists of vectors such that entry `[i]` contains all
    vectors of length `i`.

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.short_vector_list_up_to_length(3)
        [[(0, 0, 0, 0)], [(1, 0, 0, 0), (-1, 0, 0, 0)], []]
        sage: Q.short_vector_list_up_to_length(4)
        [[(0, 0, 0, 0)],
         [(1, 0, 0, 0), (-1, 0, 0, 0)],
         [],
         [(0, 1, 0, 0), (0, -1, 0, 0)]]
        sage: Q.short_vector_list_up_to_length(5)
        [[(0, 0, 0, 0)],
         [(1, 0, 0, 0), (-1, 0, 0, 0)],
         [],
         [(0, 1, 0, 0), (0, -1, 0, 0)],
         [(1, 1, 0, 0),
          (-1, -1, 0, 0),
          (1, -1, 0, 0),
          (-1, 1, 0, 0),
          (2, 0, 0, 0),
          (-2, 0, 0, 0)]]
        sage: Q.short_vector_list_up_to_length(5, True)
        [[(0, 0, 0, 0)],
         [(1, 0, 0, 0)],
         [],
         [(0, 1, 0, 0)],
         [(1, 1, 0, 0), (1, -1, 0, 0), (2, 0, 0, 0)]]
        sage: m6 = matrix(6, [2, 1, 1, 1, -1, -1, 1, 2, 1, 1, -1, -1,
        ....:                 1, 1, 2, 0, -1, -1, 1, 1, 0, 2, 0, -1,
        ....:                 -1, -1, -1, 0, 2, 1, -1, -1, -1, -1, 1, 2])
        sage: Q = QuadraticForm(m6)
        sage: vs = Q.short_vector_list_up_to_length(8)
        sage: [len(vs[i]) for i in range(len(vs))]
        [1, 72, 270, 720, 936, 2160, 2214, 3600]

    The cases of ``len_bound < 2`` led to exception or infinite runtime before.

    ::

        sage: Q.short_vector_list_up_to_length(-1)
        []
        sage: Q.short_vector_list_up_to_length(0)
        []
        sage: Q.short_vector_list_up_to_length(1)
        [[(0, 0, 0, 0, 0, 0)]]

    In the case of quadratic forms that are not positive definite an error is raised.

    ::

        sage: QuadraticForm(matrix(2, [2, 0, 0, -2])).short_vector_list_up_to_length(3)
        Traceback (most recent call last):
        ...
        ValueError: Quadratic form must be positive definite in order to enumerate short vectors

    Check that PARI does not return vectors which are too long::

        sage: Q = QuadraticForm(matrix(2, [72, 12, 12, 120]))
        sage: len_bound_pari = 2*22953421 - 2; len_bound_pari
        45906840
        sage: vs = list(Q.__pari__().qfminim(len_bound_pari)[2])  # long time (18s on sage.math, 2014)
        sage: v = vs[0]; v  # long time
        [66, -623]~
        sage: v.Vec() * Q.__pari__() * v  # long time
        45902280
    """
def short_primitive_vector_list_up_to_length(self, len_bound, up_to_sign_flag: bool = False):
    """
    Return a list of lists of short primitive vectors `v`, sorted by length, with
    `Q(v) <` ``len_bound``.  The list in output `[i]` indexes all vectors of
    length `i`.  If the ``up_to_sign_flag`` is set to ``True``, then only one of
    the vectors of the pair `[v, -v]` is listed.

    .. NOTE::

        This processes the PARI/GP output to always give elements of type `\\ZZ`.

    OUTPUT: list of lists of vectors

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.short_vector_list_up_to_length(5, True)
        [[(0, 0, 0, 0)],
         [(1, 0, 0, 0)],
         [],
         [(0, 1, 0, 0)],
         [(1, 1, 0, 0), (1, -1, 0, 0), (2, 0, 0, 0)]]
        sage: Q.short_primitive_vector_list_up_to_length(5, True)
        [[], [(1, 0, 0, 0)], [], [(0, 1, 0, 0)], [(1, 1, 0, 0), (1, -1, 0, 0)]]
    """
def automorphism_group(self):
    """
    Return the group of automorphisms of the quadratic form.

    OUTPUT: a :class:`MatrixGroup`

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.automorphism_group()
        Matrix group over Rational Field with 3 generators (
        [ 0  0  1]  [1 0 0]  [ 1  0  0]
        [-1  0  0]  [0 0 1]  [ 0 -1  0]
        [ 0  1  0], [0 1 0], [ 0  0  1]
        )

    ::

        sage: DiagonalQuadraticForm(ZZ, [1,3,5,7]).automorphism_group()
        Matrix group over Rational Field with 4 generators (
        [-1  0  0  0]  [ 1  0  0  0]  [ 1  0  0  0]  [ 1  0  0  0]
        [ 0 -1  0  0]  [ 0 -1  0  0]  [ 0  1  0  0]  [ 0  1  0  0]
        [ 0  0 -1  0]  [ 0  0  1  0]  [ 0  0 -1  0]  [ 0  0  1  0]
        [ 0  0  0 -1], [ 0  0  0  1], [ 0  0  0  1], [ 0  0  0 -1]
        )

    The smallest possible automorphism group has order two, since we
    can always change all signs::

        sage: Q = QuadraticForm(ZZ, 3, [2, 1, 2, 2, 1, 3])
        sage: Q.automorphism_group()
        Matrix group over Rational Field with 1 generators (
        [-1  0  0]
        [ 0 -1  0]
        [ 0  0 -1]
        )
    """
def automorphisms(self):
    """
    Return the list of the automorphisms of the quadratic form.

    OUTPUT: list of matrices

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.number_of_automorphisms()
        48
        sage: 2^3 * factorial(3)
        48
        sage: len(Q.automorphisms())                                                    # needs sage.libs.gap
        48

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.number_of_automorphisms()
        16
        sage: aut = Q.automorphisms()                                                   # needs sage.libs.gap
        sage: len(aut)                                                                  # needs sage.libs.gap
        16
        sage: all(Q(M) == Q for M in aut)                                               # needs sage.libs.gap
        True

        sage: Q = QuadraticForm(ZZ, 3, [2, 1, 2, 2, 1, 3])
        sage: sorted(Q.automorphisms())                                                 # needs sage.libs.gap
        [
        [-1  0  0]  [1 0 0]
        [ 0 -1  0]  [0 1 0]
        [ 0  0 -1], [0 0 1]
        ]
    """
def number_of_automorphisms(self):
    """
    Return the number of automorphisms (of det `1` and `-1`) of
    the quadratic form.

    OUTPUT: integer `\\geq 2`

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [1, 0, 0, 1, 0, 1], unsafe_initialization=True)
        sage: Q.number_of_automorphisms()
        48

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Q.number_of_automorphisms()
        384
        sage: 2^4 * factorial(4)
        384
    """
def set_number_of_automorphisms(self, num_autos) -> None:
    """
    Set the number of automorphisms to be the value given.  No error
    checking is performed, to this may lead to erroneous results.

    The fact that this result was set externally is recorded in the
    internal list of external initializations, accessible by the
    method :meth:`list_external_initializations`.

    OUTPUT: none

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
        sage: Q.list_external_initializations()
        []
        sage: Q.set_number_of_automorphisms(-3)
        sage: Q.number_of_automorphisms()
        -3
        sage: Q.list_external_initializations()
        ['number_of_automorphisms']
    """
