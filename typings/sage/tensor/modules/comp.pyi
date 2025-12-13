from _typeshed import Incomplete
from collections.abc import Generator
from sage.parallel.decorate import parallel as parallel
from sage.parallel.parallelism import Parallelism as Parallelism
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class Components(SageObject):
    '''
    Indexed set of ring elements forming some components with respect
    to a given "frame".

    The "frame" can be a basis of some vector space or a vector frame on some
    manifold (i.e. a field of bases).
    The stored quantities can be tensor components or non-tensorial quantities,
    such as connection coefficients or structure coefficients. The symmetries
    over some indices are dealt by subclasses of the class :class:`Components`.

    INPUT:

    - ``ring`` -- commutative ring in which each component takes its value
    - ``frame`` -- frame with respect to which the components are defined;
      whatever type ``frame`` is, it should have a method ``__len__()``
      implemented, so that ``len(frame)`` returns the dimension, i.e. the size
      of a single index range
    - ``nb_indices`` -- number of integer indices labeling the components
    - ``start_index`` -- (default: 0) first value of a single index;
      accordingly a component index i must obey
      ``start_index <= i <= start_index + dim - 1``, where ``dim = len(frame)``.
    - ``output_formatter`` -- (default: ``None``) function or unbound
      method called to format the output of the component access
      operator ``[...]`` (method __getitem__); ``output_formatter`` must take
      1 or 2 arguments: the 1st argument must be an element of ``ring`` and
      the second one, if any, some format specification.

    EXAMPLES:

    Set of components with 2 indices on a 3-dimensional vector space, the frame
    being some basis of the vector space::

        sage: from sage.tensor.modules.comp import Components
        sage: V = VectorSpace(QQ,3)
        sage: basis = V.basis() ; basis
        [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        sage: c = Components(QQ, basis, 2) ; c
        2-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]

    Actually, the frame can be any object that has some length, i.e. on which
    the function :func:`len()` can be called::

        sage: basis1 = V.gens() ; basis1
        ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        sage: c1 = Components(QQ, basis1, 2) ; c1
        2-indices components w.r.t. ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        sage: basis2 = [\'a\', \'b\' , \'c\']
        sage: c2 = Components(QQ, basis2, 2) ; c2
        2-indices components w.r.t. [\'a\', \'b\', \'c\']

    By default, the indices range from `0` to `n-1`, where `n` is the length
    of the frame. This can be changed via the argument ``start_index``::

        sage: c1 = Components(QQ, basis, 2, start_index=1)
        sage: c1[0,1]
        Traceback (most recent call last):
        ...
        IndexError: index out of range: 0 not in [1, 3]
        sage: c[0,1]  # for c, the index 0 is OK
        0
        sage: c[0,1] = -3
        sage: c1[:] = c[:] # list copy of all components
        sage: c1[1,2]  # (1,2) = (0,1) shifted by 1
        -3

    If some formatter function or unbound method is provided via the argument
    ``output_formatter``, it is used to change the output of the access
    operator ``[...]``::

        sage: a = Components(QQ, basis, 2, output_formatter=Rational.numerical_approx)
        sage: a[1,2] = 1/3
        sage: a[1,2]
        0.333333333333333

    The format can be passed to the formatter as the last argument of the
    access operator ``[...]``::

        sage: a[1,2,10] # here the format is 10, for 10 bits of precision
        0.33
        sage: a[1,2,100]
        0.33333333333333333333333333333

    The raw (unformatted) components are then accessed by the double bracket
    operator::

        sage: a[[1,2]]
        1/3

    For sets of components declared without any output formatter, there is no
    difference between ``[...]`` and ``[[...]]``::

        sage: c[1,2] = 1/3
        sage: c[1,2], c[[1,2]]
        (1/3, 1/3)

    The formatter is also used for the complete list of components::

        sage: a[:]
        [0.000000000000000 0.000000000000000 0.000000000000000]
        [0.000000000000000 0.000000000000000 0.333333333333333]
        [0.000000000000000 0.000000000000000 0.000000000000000]
        sage: a[:,10] # with a format different from the default one (53 bits)
        [0.00 0.00 0.00]
        [0.00 0.00 0.33]
        [0.00 0.00 0.00]

    The complete list of components in raw form can be recovered by the double
    bracket operator, replacing ``:`` by ``slice(None)`` (since ``a[[:]]``
    generates a Python syntax error)::

        sage: a[[slice(None)]]
        [  0   0   0]
        [  0   0 1/3]
        [  0   0   0]

    Another example of formatter: the Python built-in function :func:`str`
    to generate string outputs::

        sage: b = Components(QQ, V.basis(), 1, output_formatter=str)
        sage: b[:] = (1, 0, -4)
        sage: b[:]
        [\'1\', \'0\', \'-4\']

    For such a formatter, 2-indices components are no longer displayed as a
    matrix::

        sage: b = Components(QQ, basis, 2, output_formatter=str)
        sage: b[0,1] = 1/3
        sage: b[:]
        [[\'0\', \'1/3\', \'0\'], [\'0\', \'0\', \'0\'], [\'0\', \'0\', \'0\']]

    But unformatted outputs still are::

        sage: b[[slice(None)]]
        [  0 1/3   0]
        [  0   0   0]
        [  0   0   0]

    Internally, the components are stored as a dictionary (:attr:`_comp`) whose
    keys are the indices; only the nonzero components are stored::

        sage: a[:]
        [0.000000000000000 0.000000000000000 0.000000000000000]
        [0.000000000000000 0.000000000000000 0.333333333333333]
        [0.000000000000000 0.000000000000000 0.000000000000000]
        sage: a._comp
        {(1, 2): 1/3}
        sage: v = Components(QQ, basis, 1)
        sage: v[:] = (-1, 0, 3)
        sage: v._comp  # random output order of the component dictionary
        {(0,): -1, (2,): 3}


    .. RUBRIC:: ARITHMETIC EXAMPLES:

    Unary plus operator::

        sage: a = Components(QQ, basis, 1)
        sage: a[:] = (-1, 0, 3)
        sage: s = +a ; s[:]
        [-1, 0, 3]
        sage: +a == a
        True

    Unary minus operator::

        sage: s = -a ; s[:]
        [1, 0, -3]

    Addition::

        sage: b = Components(QQ, basis, 1)
        sage: b[:] = (2, 1, 4)
        sage: s = a + b ; s[:]
        [1, 1, 7]
        sage: a + b == b + a
        True
        sage: a + (-a) == 0
        True

    Subtraction::

        sage: s = a - b ; s[:]
        [-3, -1, -1]
        sage: s + b == a
        True
        sage: a - b == - (b - a)
        True

    Multiplication by a scalar::

        sage: s = 2*a ; s[:]
        [-2, 0, 6]

    Division by a scalar::

        sage: s = a/2 ; s[:]
        [-1/2, 0, 3/2]
        sage: 2*(a/2) == a
        True

    Tensor product (by means of the operator ``*``)::

        sage: c = a*b ; c
        2-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
        sage: a[:], b[:]
        ([-1, 0, 3], [2, 1, 4])
        sage: c[:]
        [-2 -1 -4]
        [ 0  0  0]
        [ 6  3 12]
        sage: d = c*a ; d
        3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
        sage: d[:]
        [[[2, 0, -6], [1, 0, -3], [4, 0, -12]],
         [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
         [[-6, 0, 18], [-3, 0, 9], [-12, 0, 36]]]
        sage: d[0,1,2] == a[0]*b[1]*a[2]
        True
    '''
    def __init__(self, ring, frame, nb_indices, start_index: int = 0, output_formatter=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.comp import Components
            sage: Components(ZZ, [1,2,3], 2)
            2-indices components w.r.t. [1, 2, 3]
        """
    def copy(self):
        """
        Return an exact copy of ``self``.

        EXAMPLES:

        Copy of a set of components with a single index::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ,3)
            sage: a = Components(QQ, V.basis(), 1)
            sage: a[:] = -2, 1, 5
            sage: b = a.copy() ; b
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: b[:]
            [-2, 1, 5]
            sage: b == a
            True
            sage: b is a  # b is a distinct object
            False
        """
    def __getitem__(self, args):
        """
        Return the component corresponding to the given indices.

        INPUT:

        - ``args`` -- list of indices (possibly a single integer if
          ``self`` is a 1-index object) or the character ``:`` for the full list
          of components

        OUTPUT:

        - the component corresponding to ``args`` or, if ``args`` = ``:``,
          the full list of components, in the form ``T[i][j]...`` for the
          components `T_{ij...}` (for a 2-indices object, a matrix is returned)

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, [1,2,3], 2)
            sage: c[1,2]    # unset components are zero
            0
            sage: c.__getitem__((1,2))
            0
            sage: c.__getitem__([1,2])
            0
            sage: c[1,2] = -4
            sage: c[1,2]
            -4
            sage: c.__getitem__((1,2))
            -4
            sage: c[:]
            [ 0  0  0]
            [ 0  0 -4]
            [ 0  0  0]
            sage: c.__getitem__(slice(None))
            [ 0  0  0]
            [ 0  0 -4]
            [ 0  0  0]
        """
    def __setitem__(self, args, value) -> None:
        """
        Set the component corresponding to the given indices.

        INPUT:

        - ``args`` -- list of indices (possibly a single integer if
          ``self`` is a 1-index object); if ``[:]`` is provided, all the
          components are set
        - ``value`` -- the value to be set or a list of values if
          ``args = [:]`` (``slice(None)``)

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, [1,2,3], 2)
            sage: c.__setitem__((0,1), -4)
            sage: c[:]
            [ 0 -4  0]
            [ 0  0  0]
            [ 0  0  0]
            sage: c[0,1] = -4
            sage: c[:]
            [ 0 -4  0]
            [ 0  0  0]
            [ 0  0  0]
            sage: c.__setitem__(slice(None), [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
            sage: c[:]
            [0 1 2]
            [3 4 5]
            [6 7 8]
        """
    def items(self) -> Generator[Incomplete]:
        """
        Return an iterable of ``(indices, value)`` elements.

        This may (but is not guaranteed to) suppress zero values.

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components, CompWithSym

            sage: c = Components(ZZ, (ZZ^2).basis(), 3)
            sage: c[0,1,0], c[1,0,1], c[1,1,1] = -2, 5, 3
            sage: list(c.items())
            [((0, 1, 0), -2), ((1, 0, 1), 5), ((1, 1, 1), 3)]

            sage: c = CompWithSym(ZZ, (ZZ^2).basis(), 3, sym=((1, 2)))
            sage: c[0,1,0], c[1,0,1], c[1,1,1] = -2, 5, 3
            sage: list(c.items())
            [((0, 0, 1), -2),
            ((0, 1, 0), -2),
            ((1, 0, 1), 5),
            ((1, 1, 0), 5),
            ((1, 1, 1), 3)]
        """
    def display(self, symbol, latex_symbol=None, index_positions=None, index_labels=None, index_latex_labels=None, format_spec=None, only_nonzero: bool = True, only_nonredundant: bool = False):
        '''
        Display all the components, one per line.

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        INPUT:

        - ``symbol`` -- string (typically a single letter) specifying the
          symbol for the components
        - ``latex_symbol`` -- (default: ``None``) string specifying the LaTeX
          symbol for the components; if ``None``, ``symbol`` is used
        - ``index_positions`` -- (default: ``None``) string of length the
          number of indices of the components and composed of characters \'d\'
          (for "down") or \'u\' (for "up") to specify the position of each index:
          \'d\' corresponds to a subscript and \'u\' to a superscript. If
          ``index_positions`` is ``None``, all indices are printed as
          subscripts
        - ``index_labels`` -- (default: ``None``) list of strings representing
          the labels of each of the individual indices within the index range
          defined at the construction of the object; if ``None``, integer
          labels are used
        - ``index_latex_labels`` -- (default: ``None``) list of strings
          representing the LaTeX labels of each of the individual indices
          within the index range defined at the construction of the object; if
          ``None``, integers labels are used
        - ``format_spec`` -- (default: ``None``) format specification passed
          to the output formatter declared at the construction of the object
        - ``only_nonzero`` -- boolean (default: ``True``); if ``True``, only
          nonzero components are displayed
        - ``only_nonredundant`` -- boolean (default: ``False``); if ``True``,
          only nonredundant components are displayed in case of symmetries

        EXAMPLES:

        Display of 3-indices components w.r.t. to the canonical basis of the
        free module `\\ZZ^2` over the integer ring::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, (ZZ^2).basis(), 3)
            sage: c[0,1,0], c[1,0,1], c[1,1,1] = -2, 5, 3
            sage: c.display(\'c\')
            c_010 = -2
            c_101 = 5
            c_111 = 3

        By default, only nonzero components are shown; to display all the
        components, it suffices to set the parameter ``only_nonzero`` to
        ``False``::

            sage: c.display(\'c\', only_nonzero=False)
            c_000 = 0
            c_001 = 0
            c_010 = -2
            c_011 = 0
            c_100 = 0
            c_101 = 5
            c_110 = 0
            c_111 = 3

        By default, all indices are printed as subscripts, but any index
        position can be specified::

            sage: c.display(\'c\', index_positions=\'udd\')
            c^0_10 = -2
            c^1_01 = 5
            c^1_11 = 3
            sage: c.display(\'c\', index_positions=\'udu\')
            c^0_1^0 = -2
            c^1_0^1 = 5
            c^1_1^1 = 3
            sage: c.display(\'c\', index_positions=\'ddu\')
            c_01^0 = -2
            c_10^1 = 5
            c_11^1 = 3

        The LaTeX output is performed as an array, with the symbol adjustable
        if it differs from the text symbol::

            sage: latex(c.display(\'c\', latex_symbol=r\'\\Gamma\', index_positions=\'udd\'))
            \\begin{array}{lcl}
             \\Gamma_{\\phantom{\\, 0}\\,1\\,0}^{\\,0\\phantom{\\, 1}\\phantom{\\, 0}} & = & -2 \\\\\n             \\Gamma_{\\phantom{\\, 1}\\,0\\,1}^{\\,1\\phantom{\\, 0}\\phantom{\\, 1}} & = & 5 \\\\\n             \\Gamma_{\\phantom{\\, 1}\\,1\\,1}^{\\,1\\phantom{\\, 1}\\phantom{\\, 1}} & = & 3
            \\end{array}

        The index labels can differ from integers::

            sage: c.display(\'c\', index_labels=[\'x\',\'y\'])
            c_xyx = -2
            c_yxy = 5
            c_yyy = 3

        If the index labels are longer than a single character, they are
        separated by a comma::

            sage: c.display(\'c\', index_labels=[\'r\', \'th\'])
            c_r,th,r = -2
            c_th,r,th = 5
            c_th,th,th = 3

        The LaTeX labels for the indices can be specified if they differ
        from the text ones::

            sage: c.display(\'c\', index_labels=[\'r\', \'th\'],
            ....:           index_latex_labels=[\'r\', r\'\\theta\'])
            c_r,th,r = -2
            c_th,r,th = 5
            c_th,th,th = 3

        The display of components with symmetries is governed by the parameter
        ``only_nonredundant``::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: c = CompWithSym(ZZ, (ZZ^2).basis(), 3, sym=(1,2)) ; c
            3-indices components w.r.t. [
            (1, 0),
            (0, 1)
            ], with symmetry on the index positions (1, 2)
            sage: c[0,0,1] = 2
            sage: c.display(\'c\')
            c_001 = 2
            c_010 = 2
            sage: c.display(\'c\', only_nonredundant=True)
            c_001 = 2

        If some nontrivial output formatter has been set, the format can be
        specified by means of the argument ``format_spec``::

            sage: c = Components(QQ, (QQ^3).basis(), 2,
            ....:                output_formatter=Rational.numerical_approx)
            sage: c[0,1] = 1/3
            sage: c[2,1] = 2/7
            sage: c.display(\'C\')  # default format (53 bits of precision)
            C_01 = 0.333333333333333
            C_21 = 0.285714285714286
            sage: c.display(\'C\', format_spec=10)  # 10 bits of precision
            C_01 = 0.33
            C_21 = 0.29

        Check that the bug reported in :issue:`22520` is fixed::

            sage: c = Components(SR, [1, 2], 1)                                         # needs sage.symbolic
            sage: c[0] = SR.var(\'t\', domain=\'real\')                                     # needs sage.symbolic
            sage: c.display(\'c\')                                                        # needs sage.symbolic
            c_0 = t
        '''
    def swap_adjacent_indices(self, pos1, pos2, pos3):
        """
        Swap two adjacent sets of indices.

        This method is essentially required to reorder the covariant and
        contravariant indices in the computation of a tensor product.

        INPUT:

        - ``pos1`` -- position of the first index of set 1 (with the convention
          ``position=0`` for the first slot)
        - ``pos2`` -- position of the first index of set 2 equals 1 plus the
          position of the last index of set 1 (since the two sets are adjacent)
        - ``pos3`` -- 1 plus position of the last index of set 2

        OUTPUT: components with index set 1 permuted with index set 2

        EXAMPLES:

        Swap of the two indices of a 2-indices set of components::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ, 3)
            sage: c = Components(QQ, V.basis(), 2)
            sage: c[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: c1 = c.swap_adjacent_indices(0,1,2)
            sage: c[:], c1[:]
            (
            [1 2 3]  [1 4 7]
            [4 5 6]  [2 5 8]
            [7 8 9], [3 6 9]
            )

        Swap of two pairs of indices on a 4-indices set of components::

            sage: d = c*c1 ; d
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: d1 = d.swap_adjacent_indices(0,2,4)
            sage: d[0,1,1,2]
            16
            sage: d1[1,2,0,1]
            16
            sage: d1[0,1,1,2]
            24
            sage: d[1,2,0,1]
            24
        """
    def is_zero(self):
        """
        Return ``True`` if all the components are zero and ``False`` otherwise.

        EXAMPLES:

        A just-created set of components is initialized to zero::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ,3)
            sage: c = Components(QQ, V.basis(), 1)
            sage: c.is_zero()
            True
            sage: c[:]
            [0, 0, 0]
            sage: c[0] = 1 ; c[:]
            [1, 0, 0]
            sage: c.is_zero()
            False
            sage: c[0] = 0 ; c[:]
            [0, 0, 0]
            sage: c.is_zero()
            True

        It is equivalent to use the operator == to compare to zero::

            sage: c == 0
            True
            sage: c != 0
            False

        Comparing to a nonzero number is meaningless::

            sage: c == 1
            Traceback (most recent call last):
            ...
            TypeError: cannot compare a set of components to a number
        """
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- set of components or 0

        OUTPUT: ``True`` if ``self`` is equal to ``other``,  or ``False`` otherwise

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, [1,2,3], 2)
            sage: c.__eq__(0)  # uninitialized components are zero
            True
            sage: c[0,1], c[1,2] = 5, -4
            sage: c.__eq__(0)
            False
            sage: c1 = Components(ZZ, [1,2,3], 2)
            sage: c1[0,1] = 5
            sage: c.__eq__(c1)
            False
            sage: c1[1,2] = -4
            sage: c.__eq__(c1)
            True
            sage: v = Components(ZZ, [1,2,3], 1)
            sage: c.__eq__(v)
            False
        """
    def __ne__(self, other):
        """
        Non-equality operator.

        INPUT:

        - ``other`` -- set of components or 0

        OUTPUT: ``True`` if ``self`` is different from ``other``, or ``False``
        otherwise

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, [1,2,3], 1)
            sage: c.__ne__(0)  # uninitialized components are zero
            False
            sage: c1 = Components(ZZ, [1,2,3], 1)
            sage: c.__ne__(c1)  # c and c1 are both zero
            False
            sage: c[0] = 4
            sage: c.__ne__(0)
            True
            sage: c.__ne__(c1)
            True
        """
    def __pos__(self):
        """
        Unary plus operator.

        OUTPUT: an exact copy of ``self``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, [1,2,3], 1)
            sage: c[:] = 5, 0, -4
            sage: a = c.__pos__() ; a
            1-index components w.r.t. [1, 2, 3]
            sage: a[:]
            [5, 0, -4]
            sage: a == +c
            True
            sage: a == c
            True
        """
    def __neg__(self):
        """
        Unary minus operator.

        OUTPUT: the opposite of the components represented by ``self``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: c = Components(ZZ, [1,2,3], 1)
            sage: c[:] = 5, 0, -4
            sage: a = c.__neg__() ; a
            1-index components w.r.t. [1, 2, 3]
            sage: a[:]
            [-5, 0, 4]
            sage: a == -c
            True
        """
    def __add__(self, other):
        """
        Component addition.

        INPUT:

        - ``other`` -- components of the same number of indices and defined
          on the same frame as ``self``

        OUTPUT: components resulting from the addition of ``self`` and ``other``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(ZZ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: b = Components(ZZ, [1,2,3], 1)
            sage: b[:] = 4, 5, 6
            sage: s = a.__add__(b) ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [5, 5, 3]
            sage: s == a+b
            True

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: s_par = a.__add__(b) ; s_par
            1-index components w.r.t. [1, 2, 3]
            sage: s_par[:]
            [5, 5, 3]
            sage: s_par == s
            True
            sage: b.__add__(a) == s  # test of commutativity of parallel comput.
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def __radd__(self, other):
        """
        Reflected addition (addition on the right to ``other``).

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(ZZ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: b = Components(ZZ, [1,2,3], 1)
            sage: b[:] = 4, 5, 6
            sage: s = a.__radd__(b) ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [5, 5, 3]
            sage: s == a+b
            True
            sage: s = 0 + a ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s == a
            True
        """
    def __sub__(self, other):
        """
        Component subtraction.

        INPUT:

        - ``other`` -- components, of the same type as ``self``

        OUTPUT: components resulting from the subtraction of ``other`` from ``self``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(ZZ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: b = Components(ZZ, [1,2,3], 1)
            sage: b[:] = 4, 5, 6
            sage: s = a.__sub__(b) ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [-3, -5, -9]
            sage: s == a - b
            True

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: Parallelism().get('tensor')
            2
            sage: s_par = a.__sub__(b) ; s_par
            1-index components w.r.t. [1, 2, 3]
            sage: s_par[:]
            [-3, -5, -9]
            sage: s_par == s
            True
            sage: b.__sub__(a) == -s # test of parallel comput.
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def __rsub__(self, other):
        """
        Reflected subtraction (subtraction from ``other``).

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(ZZ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: b = Components(ZZ, [1,2,3], 1)
            sage: b[:] = 4, 5, 6
            sage: s = a.__rsub__(b) ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [3, 5, 9]
            sage: s == b - a
            True
            sage: s = 0 - a ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [-1, 0, 3]
            sage: s == -a
            True
        """
    def __mul__(self, other):
        """
        Component tensor product.

        INPUT:

        - ``other`` -- components, on the same frame as ``self``

        OUTPUT: the tensor product of ``self`` by ``other``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(ZZ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: b = Components(ZZ, [1,2,3], 1)
            sage: b[:] = 4, 5, 6
            sage: s = a.__mul__(b) ; s
            2-indices components w.r.t. [1, 2, 3]
            sage: s[:]
            [  4   5   6]
            [  0   0   0]
            [-12 -15 -18]
            sage: s == a*b
            True
            sage: t = b*a
            sage: aa = a*a ; aa
            Fully symmetric 2-indices components w.r.t. [1, 2, 3]
            sage: aa[:]
            [ 1  0 -3]
            [ 0  0  0]
            [-3  0  9]

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: Parallelism().get('tensor')
            2
            sage: s_par = a.__mul__(b) ; s_par
            2-indices components w.r.t. [1, 2, 3]
            sage: s_par[:]
            [  4   5   6]
            [  0   0   0]
            [-12 -15 -18]
            sage: s_par == s
            True
            sage: b.__mul__(a) == t  # test of parallel comput.
            True
            sage: a.__mul__(a) == aa  # test of parallel comput.
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization

        Tensor product with a set of symmetric components::

            sage: s = b*aa; s
            3-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (1, 2)
            sage: s[:]
            [[[4, 0, -12], [0, 0, 0], [-12, 0, 36]],
             [[5, 0, -15], [0, 0, 0], [-15, 0, 45]],
             [[6, 0, -18], [0, 0, 0], [-18, 0, 54]]]
            sage: Parallelism().set('tensor', nproc=2)
            sage: s_par = b*aa; s_par
            3-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (1, 2)
            sage: s_par[:] == s[:]
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def __rmul__(self, other):
        """
        Reflected multiplication (multiplication on the left by ``other``).

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(ZZ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: s = a.__rmul__(2) ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [2, 0, -6]
            sage: s == 2*a
            True
            sage: a.__rmul__(0) == 0
            True
        """
    def __truediv__(self, other):
        """
        Division (by a scalar).

        EXAMPLES::

            sage: from sage.tensor.modules.comp import Components
            sage: a = Components(QQ, [1,2,3], 1)
            sage: a[:] = 1, 0, -3
            sage: s = a.__truediv__(3) ; s
            1-index components w.r.t. [1, 2, 3]
            sage: s[:]
            [1/3, 0, -1]
            sage: s == a/3
            True
            sage: 3*s == a
            True
        """
    def trace(self, pos1, pos2):
        """
        Index contraction.

        INPUT:

        - ``pos1`` -- position of the first index for the contraction (with the
          convention position=0 for the first slot)
        - ``pos2`` -- position of the second index for the contraction

        OUTPUT:

        - set of components resulting from the (pos1, pos2) contraction

        EXAMPLES:

        Self-contraction of a set of components with 2 indices::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ, 3)
            sage: c = Components(QQ, V.basis(), 2)
            sage: c[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: c.trace(0,1)
            15
            sage: c[0,0] + c[1,1] + c[2,2]  # check
            15

        Three self-contractions of a set of components with 3 indices::

            sage: v = Components(QQ, V.basis(), 1)
            sage: v[:] = (-1,2,3)
            sage: a = c*v ; a
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s = a.trace(0,1) ; s  # contraction on the first two indices
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s[:]
            [-15, 30, 45]
            sage: [sum(a[j,j,i] for j in range(3)) for i in range(3)]  # check
            [-15, 30, 45]
            sage: s = a.trace(0,2) ; s[:]  # contraction on the first and last indices
            [28, 32, 36]
            sage: [sum(a[j,i,j] for j in range(3)) for i in range(3)]  # check
            [28, 32, 36]
            sage: s = a.trace(1,2) ; s[:] # contraction on the last two indices
            [12, 24, 36]
            sage: [sum(a[i,j,j] for j in range(3)) for i in range(3)]  # check
            [12, 24, 36]
        """
    def contract(self, *args):
        """
        Contraction on one or many indices with another instance of
        :class:`Components`.

        INPUT:

        - ``pos1`` -- positions of the indices in ``self`` involved in the
          contraction; ``pos1`` must be a sequence of integers, with 0 standing
          for the first index position, 1 for the second one, etc. If ``pos1``
          is not provided, a single contraction on the last index position of
          ``self`` is assumed
        - ``other`` -- the set of components to contract with
        - ``pos2`` -- positions of the indices in ``other`` involved in the
          contraction, with the same conventions as for ``pos1``. If ``pos2``
          is not provided, a single contraction on the first index position of
          ``other`` is assumed

        OUTPUT: set of components resulting from the contraction

        EXAMPLES:

        Contraction of a 1-index set of components with a 2-index one::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ, 3)
            sage: a = Components(QQ, V.basis(), 1)
            sage: a[:] = (-1, 2, 3)
            sage: b = Components(QQ, V.basis(), 2)
            sage: b[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: s0 = a.contract(0, b, 0) ; s0
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s0[:]
            [28, 32, 36]
            sage: s0[:] == [sum(a[j]*b[j,i] for j in range(3)) for i in range(3)]  # check
            True
            sage: s1 = a.contract(0, b, 1) ; s1[:]
            [12, 24, 36]
            sage: s1[:] == [sum(a[j]*b[i,j] for j in range(3)) for i in range(3)]  # check
            True

        Parallel computations (see
        :class:`~sage.parallel.parallelism.Parallelism`)::

            sage: Parallelism().set('tensor', nproc=2)
            sage: Parallelism().get('tensor')
            2
            sage: s0_par = a.contract(0, b, 0) ; s0_par
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s0_par[:]
            [28, 32, 36]
            sage: s0_par == s0
            True
            sage: s1_par = a.contract(0, b, 1) ; s1_par[:]
            [12, 24, 36]
            sage: s1_par == s1
            True
            sage: Parallelism().set('tensor', nproc = 1)  # switch off parallelization

        Contraction on 2 indices::

            sage: c = a*b ; c
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s = c.contract(1,2, b, 0,1) ; s
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s[:]
            [-285, 570, 855]
            sage: [sum(sum(c[i,j,k]*b[j,k] for k in range(3)) # check
            ....:      for j in range(3)) for i in range(3)]
            [-285, 570, 855]

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: c_par = a*b ; c_par
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: c_par == c
            True
            sage: s_par = c_par.contract(1,2, b, 0,1) ; s_par
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s_par[:]
            [-285, 570, 855]
            sage: s_par == s
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization

        Consistency check with :meth:`trace`::

            sage: b = a*a ; b   # the tensor product of a with itself
            Fully symmetric 2-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: b[:]
            [ 1 -2 -3]
            [-2  4  6]
            [-3  6  9]
            sage: b.trace(0,1)
            14
            sage: a.contract(0, a, 0) == b.trace(0,1)
            True

        TESTS:

        Check that :issue:`32355` is fixed::

            sage: from sage.tensor.modules.comp import CompFullyAntiSym
            sage: a = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: a[0,1] = 1
            sage: b = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: b[0,1], b[0,2] = 2, 3
            sage: a.contract(0, 1, b, 0, 1)
            4
            sage: a.contract(0, 1, b, 1, 0)
            -4
            sage: a.contract(1, 0, b, 0, 1)
            -4
            sage: a.contract(1, 0, b, 1, 0)
            4
            sage: Parallelism().set('tensor', nproc=2)  # same tests with parallelization
            sage: a.contract(0, 1, b, 0, 1)
            4
            sage: a.contract(0, 1, b, 1, 0)
            -4
            sage: a.contract(1, 0, b, 0, 1)
            -4
            sage: a.contract(1, 0, b, 1, 0)
            4
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def index_generator(self) -> Generator[Incomplete]:
        """
        Generator of indices.

        OUTPUT: an iterable index

        EXAMPLES:

        Indices on a 3-dimensional vector space::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ,3)
            sage: c = Components(QQ, V.basis(), 1)
            sage: list(c.index_generator())
            [(0,), (1,), (2,)]
            sage: c = Components(QQ, V.basis(), 1, start_index=1)
            sage: list(c.index_generator())
            [(1,), (2,), (3,)]
            sage: c = Components(QQ, V.basis(), 2)
            sage: list(c.index_generator())
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0),
             (2, 1), (2, 2)]
        """
    def non_redundant_index_generator(self) -> Generator[Incomplete, Incomplete]:
        """
        Generator of non redundant indices.

        In the absence of declared symmetries, all possible indices are
        generated. So this method is equivalent to :meth:`index_generator`.
        Only versions for derived classes with symmetries or antisymmetries
        are not trivial.

        OUTPUT: an iterable index

        EXAMPLES:

        Indices on a 3-dimensional vector space::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ,3)
            sage: c = Components(QQ, V.basis(), 2)
            sage: list(c.non_redundant_index_generator())
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0),
             (2, 1), (2, 2)]
            sage: c = Components(QQ, V.basis(), 2, start_index=1)
            sage: list(c.non_redundant_index_generator())
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1),
             (3, 2), (3, 3)]
        """
    def symmetrize(self, *pos):
        """
        Symmetrization over the given index positions.

        INPUT:

        - ``pos`` -- list of index positions involved in the
          symmetrization (with the convention position=0 for the first slot);
          if none, the symmetrization is performed over all the indices

        OUTPUT:

        - an instance of :class:`CompWithSym` describing the symmetrized
          components

        EXAMPLES:

        Symmetrization of 2-indices components::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ, 3)
            sage: c = Components(QQ, V.basis(), 2)
            sage: c[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: s = c.symmetrize() ; s
            Fully symmetric 2-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: c[:], s[:]
            (
            [1 2 3]  [1 3 5]
            [4 5 6]  [3 5 7]
            [7 8 9], [5 7 9]
            )
            sage: c.symmetrize() == c.symmetrize(0,1)
            True

        Full symmetrization of 3-indices components::

            sage: c = Components(QQ, V.basis(), 3)
            sage: c[:] = [[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]], [[19,20,21], [22,23,24], [25,26,27]]]
            sage: s = c.symmetrize() ; s
            Fully symmetric 3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: c[:], s[:]
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]],
             [[[1, 16/3, 29/3], [16/3, 29/3, 14], [29/3, 14, 55/3]],
              [[16/3, 29/3, 14], [29/3, 14, 55/3], [14, 55/3, 68/3]],
              [[29/3, 14, 55/3], [14, 55/3, 68/3], [55/3, 68/3, 27]]])
            sage: all(s[i,j,k] == (c[i,j,k]+c[i,k,j]+c[j,k,i]+c[j,i,k]+c[k,i,j]+c[k,j,i])/6  # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
            sage: c.symmetrize() == c.symmetrize(0,1,2)
            True

        Partial symmetrization of 3-indices components::

            sage: s = c.symmetrize(0,1) ; s   # symmetrization on the first two indices
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1)
            sage: c[:], s[:]
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]],
             [[[1, 2, 3], [7, 8, 9], [13, 14, 15]],
              [[7, 8, 9], [13, 14, 15], [19, 20, 21]],
              [[13, 14, 15], [19, 20, 21], [25, 26, 27]]])
            sage: all(s[i,j,k] == (c[i,j,k]+c[j,i,k])/2   # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
            sage: s = c.symmetrize(1,2) ; s   # symmetrization on the last two indices
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (1, 2)
            sage: c[:], s[:]
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]],
             [[[1, 3, 5], [3, 5, 7], [5, 7, 9]],
              [[10, 12, 14], [12, 14, 16], [14, 16, 18]],
              [[19, 21, 23], [21, 23, 25], [23, 25, 27]]])
            sage: all(s[i,j,k] == (c[i,j,k]+c[i,k,j])/2   # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
            sage: s = c.symmetrize(0,2) ; s   # symmetrization on the first and last indices
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 2)
            sage: c[:], s[:]
            ([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]],
             [[[1, 6, 11], [4, 9, 14], [7, 12, 17]],
              [[6, 11, 16], [9, 14, 19], [12, 17, 22]],
              [[11, 16, 21], [14, 19, 24], [17, 22, 27]]])
            sage: all(s[i,j,k] == (c[i,j,k]+c[k,j,i])/2   # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
        """
    def antisymmetrize(self, *pos):
        """
        Antisymmetrization over the given index positions.

        INPUT:

        - ``pos`` -- list of index positions involved in the antisymmetrization
          (with the convention position=0 for the first slot); if none, the
          antisymmetrization is performed over all the indices

        OUTPUT: an instance of :class:`CompWithSym` describing the
        antisymmetrized components

        EXAMPLES:

        Antisymmetrization of 2-indices components::

            sage: from sage.tensor.modules.comp import Components
            sage: V = VectorSpace(QQ, 3)
            sage: c = Components(QQ, V.basis(), 2)
            sage: c[:] = [[1,2,3], [4,5,6], [7,8,9]]
            sage: s = c.antisymmetrize() ; s
            Fully antisymmetric 2-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: c[:], s[:]
            (
            [1 2 3]  [ 0 -1 -2]
            [4 5 6]  [ 1  0 -1]
            [7 8 9], [ 2  1  0]
            )
            sage: c.antisymmetrize() == c.antisymmetrize(0,1)
            True

        Full antisymmetrization of 3-indices components::

            sage: c = Components(QQ, V.basis(), 3)
            sage: c[:] = [[[-1,-2,3], [4,-5,4], [-7,8,9]], [[10,10,12], [13,-14,15], [-16,17,19]], [[-19,20,21], [1,2,3], [-25,26,27]]]
            sage: s = c.antisymmetrize() ; s
            Fully antisymmetric 3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: c[:], s[:]
            ([[[-1, -2, 3], [4, -5, 4], [-7, 8, 9]],
              [[10, 10, 12], [13, -14, 15], [-16, 17, 19]],
              [[-19, 20, 21], [1, 2, 3], [-25, 26, 27]]],
             [[[0, 0, 0], [0, 0, -13/6], [0, 13/6, 0]],
              [[0, 0, 13/6], [0, 0, 0], [-13/6, 0, 0]],
              [[0, -13/6, 0], [13/6, 0, 0], [0, 0, 0]]])
            sage: all(s[i,j,k] == (c[i,j,k]-c[i,k,j]+c[j,k,i]-c[j,i,k]+c[k,i,j]-c[k,j,i])/6  # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
            sage: c.symmetrize() == c.symmetrize(0,1,2)
            True

        Partial antisymmetrization of 3-indices components::

            sage: s = c.antisymmetrize(0,1) ; s  # antisymmetrization on the first two indices
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 1)
            sage: c[:], s[:]
            ([[[-1, -2, 3], [4, -5, 4], [-7, 8, 9]],
              [[10, 10, 12], [13, -14, 15], [-16, 17, 19]],
              [[-19, 20, 21], [1, 2, 3], [-25, 26, 27]]],
             [[[0, 0, 0], [-3, -15/2, -4], [6, -6, -6]],
              [[3, 15/2, 4], [0, 0, 0], [-17/2, 15/2, 8]],
              [[-6, 6, 6], [17/2, -15/2, -8], [0, 0, 0]]])
            sage: all(s[i,j,k] == (c[i,j,k]-c[j,i,k])/2  # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
            sage: s = c.antisymmetrize(1,2) ; s  # antisymmetrization on the last two indices
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (1, 2)
            sage: c[:], s[:]
            ([[[-1, -2, 3], [4, -5, 4], [-7, 8, 9]],
              [[10, 10, 12], [13, -14, 15], [-16, 17, 19]],
              [[-19, 20, 21], [1, 2, 3], [-25, 26, 27]]],
             [[[0, -3, 5], [3, 0, -2], [-5, 2, 0]],
              [[0, -3/2, 14], [3/2, 0, -1], [-14, 1, 0]],
              [[0, 19/2, 23], [-19/2, 0, -23/2], [-23, 23/2, 0]]])
            sage: all(s[i,j,k] == (c[i,j,k]-c[i,k,j])/2  # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True
            sage: s = c.antisymmetrize(0,2) ; s  # antisymmetrization on the first and last indices
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 2)
            sage: c[:], s[:]
            ([[[-1, -2, 3], [4, -5, 4], [-7, 8, 9]],
              [[10, 10, 12], [13, -14, 15], [-16, 17, 19]],
              [[-19, 20, 21], [1, 2, 3], [-25, 26, 27]]],
             [[[0, -6, 11], [0, -9, 3/2], [0, 12, 17]],
              [[6, 0, -4], [9, 0, 13/2], [-12, 0, -7/2]],
              [[-11, 4, 0], [-3/2, -13/2, 0], [-17, 7/2, 0]]])
            sage: all(s[i,j,k] == (c[i,j,k]-c[k,j,i])/2  # Check of the result:
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True

        The order of index positions in the argument does not matter::

            sage: c.antisymmetrize(1,0) == c.antisymmetrize(0,1)
            True
            sage: c.antisymmetrize(2,1) == c.antisymmetrize(1,2)
            True
            sage: c.antisymmetrize(2,0) == c.antisymmetrize(0,2)
            True
        """

class CompWithSym(Components):
    '''
    Indexed set of ring elements forming some components with respect to a
    given "frame", with symmetries or antisymmetries regarding permutations
    of the indices.

    The "frame" can be a basis of some vector space or a vector frame on some
    manifold (i.e. a field of bases).
    The stored quantities can be tensor components or non-tensorial quantities,
    such as connection coefficients or structure coefficients.

    Subclasses of :class:`CompWithSym` are

    * :class:`CompFullySym` for fully symmetric components.
    * :class:`CompFullyAntiSym` for fully antisymmetric components.

    INPUT:

    - ``ring`` -- commutative ring in which each component takes its value
    - ``frame`` -- frame with respect to which the components are defined;
      whatever type ``frame`` is, it should have some method ``__len__()``
      implemented, so that ``len(frame)`` returns the dimension, i.e. the size
      of a single index range
    - ``nb_indices`` -- number of indices labeling the components
    - ``start_index`` -- (default: 0) first value of a single index;
      accordingly a component index i must obey
      ``start_index <= i <= start_index + dim - 1``, where ``dim = len(frame)``.
    - ``output_formatter`` -- (default: ``None``) function or unbound
      method called to format the output of the component access
      operator ``[...]`` (method __getitem__); ``output_formatter`` must take
      1 or 2 arguments: the 1st argument must be an instance of ``ring`` and
      the second one, if any, some format specification.
    - ``sym`` -- (default: ``None``) a symmetry or a list of symmetries among
      the indices: each symmetry is described by a tuple containing the
      positions of the involved indices, with the convention ``position=0``
      for the first slot; for instance:

        * ``sym = (0, 1)`` for a symmetry between the 1st and 2nd indices
        * ``sym = [(0,2), (1,3,4)]`` for a symmetry between the 1st and 3rd
          indices and a symmetry between the 2nd, 4th and 5th indices.

    - ``antisym`` -- (default: ``None``) antisymmetry or list of antisymmetries
      among the indices, with the same convention as for ``sym``

    EXAMPLES:

    Symmetric components with 2 indices::

        sage: from sage.tensor.modules.comp import Components, CompWithSym
        sage: V = VectorSpace(QQ,3)
        sage: c = CompWithSym(QQ, V.basis(), 2, sym=(0,1))  # for demonstration only: it is preferable to use CompFullySym in this case
        sage: c[0,1] = 3
        sage: c[:]  # note that c[1,0] has been set automatically
        [0 3 0]
        [3 0 0]
        [0 0 0]

    Antisymmetric components with 2 indices::

        sage: c = CompWithSym(QQ, V.basis(), 2, antisym=(0,1))  # for demonstration only: it is preferable to use CompFullyAntiSym in this case
        sage: c[0,1] = 3
        sage: c[:]  # note that c[1,0] has been set automatically
        [ 0  3  0]
        [-3  0  0]
        [ 0  0  0]

    Internally, only non-redundant components are stored::

        sage: c._comp
        {(0, 1): 3}

    Components with 6 indices, symmetric among 3 indices (at position
    `(0, 1, 5)`) and antisymmetric among 2 indices (at position `(2, 4)`)::

        sage: c = CompWithSym(QQ, V.basis(), 6, sym=(0,1,5), antisym=(2,4))
        sage: c[0,1,2,0,1,2] = 3
        sage: c[1,0,2,0,1,2]  # symmetry between indices in position 0 and 1
        3
        sage: c[2,1,2,0,1,0]  # symmetry between indices in position 0 and 5
        3
        sage: c[0,2,2,0,1,1]  # symmetry between indices in position 1 and 5
        3
        sage: c[0,1,1,0,2,2]  # antisymmetry between indices in position 2 and 4
        -3

    Components with 4 indices, antisymmetric with respect to the first pair of
    indices as well as with the second pair of indices::

        sage: c = CompWithSym(QQ, V.basis(), 4, antisym=[(0,1),(2,3)])
        sage: c[0,1,0,1] = 3
        sage: c[1,0,0,1]  # antisymmetry on the first pair of indices
        -3
        sage: c[0,1,1,0]  # antisymmetry on the second pair of indices
        -3
        sage: c[1,0,1,0]  # consequence of the above
        3

    .. RUBRIC:: ARITHMETIC EXAMPLES

    Addition of a symmetric set of components with a non-symmetric one: the
    symmetry is lost::

        sage: V = VectorSpace(QQ, 3)
        sage: a = Components(QQ, V.basis(), 2)
        sage: a[:] = [[1,-2,3], [4,5,-6], [-7,8,9]]
        sage: b = CompWithSym(QQ, V.basis(), 2, sym=(0,1))  # for demonstration only: it is preferable to declare b = CompFullySym(QQ, V.basis(), 2)
        sage: b[0,0], b[0,1], b[0,2] = 1, 2, 3
        sage: b[1,1], b[1,2] = 5, 7
        sage: b[2,2] = 11
        sage: s = a + b ; s
        2-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
        sage: a[:], b[:], s[:]
        (
        [ 1 -2  3]  [ 1  2  3]  [ 2  0  6]
        [ 4  5 -6]  [ 2  5  7]  [ 6 10  1]
        [-7  8  9], [ 3  7 11], [-4 15 20]
        )
        sage: a + b == b + a
        True

    Addition of two symmetric set of components: the symmetry is preserved::

        sage: c = CompWithSym(QQ, V.basis(), 2, sym=(0,1)) # for demonstration only: it is preferable to declare c = CompFullySym(QQ, V.basis(), 2)
        sage: c[0,0], c[0,1], c[0,2] = -4, 7, -8
        sage: c[1,1], c[1,2] = 2, -4
        sage: c[2,2] = 2
        sage: s = b + c ; s
        2-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ], with symmetry on the index positions (0, 1)
        sage: b[:], c[:], s[:]
        (
        [ 1  2  3]  [-4  7 -8]  [-3  9 -5]
        [ 2  5  7]  [ 7  2 -4]  [ 9  7  3]
        [ 3  7 11], [-8 -4  2], [-5  3 13]
        )
        sage: b + c == c + b
        True

    Check of the addition with counterparts not declared symmetric::

        sage: bn = Components(QQ, V.basis(), 2)
        sage: bn[:] = b[:]
        sage: bn == b
        True
        sage: cn = Components(QQ, V.basis(), 2)
        sage: cn[:] = c[:]
        sage: cn == c
        True
        sage: bn + cn == b + c
        True

    Addition of an antisymmetric set of components with a non-symmetric one:
    the antisymmetry is lost::

        sage: d = CompWithSym(QQ, V.basis(), 2, antisym=(0,1))  # for demonstration only: it is preferable to declare d = CompFullyAntiSym(QQ, V.basis(), 2)
        sage: d[0,1], d[0,2], d[1,2] = 4, -1, 3
        sage: s = a + d ; s
        2-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
        sage: a[:], d[:], s[:]
        (
        [ 1 -2  3]  [ 0  4 -1]  [ 1  2  2]
        [ 4  5 -6]  [-4  0  3]  [ 0  5 -3]
        [-7  8  9], [ 1 -3  0], [-6  5  9]
        )
        sage: d + a == a + d
        True

    Addition of two antisymmetric set of components: the antisymmetry is preserved::

        sage: e = CompWithSym(QQ, V.basis(), 2, antisym=(0,1))  # for demonstration only: it is preferable to declare e = CompFullyAntiSym(QQ, V.basis(), 2)
        sage: e[0,1], e[0,2], e[1,2] = 2, 3, -1
        sage: s = d + e ; s
        2-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ], with antisymmetry on the index positions (0, 1)
        sage: d[:], e[:], s[:]
        (
        [ 0  4 -1]  [ 0  2  3]  [ 0  6  2]
        [-4  0  3]  [-2  0 -1]  [-6  0  2]
        [ 1 -3  0], [-3  1  0], [-2 -2  0]
        )
        sage: e + d == d + e
        True
    '''
    def __init__(self, ring, frame, nb_indices, start_index: int = 0, output_formatter=None, sym=None, antisym=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: C = CompWithSym(ZZ, [1,2,3], 4, sym=(0,1), antisym=(2,3))
            sage: TestSuite(C).run()
        """
    def __getitem__(self, args):
        """
        Return the component corresponding to the given indices.

        INPUT:

        - ``args`` -- list of indices (possibly a single integer if
          ``self`` is a 1-index object) or the character ``:`` for the full list
          of components

        OUTPUT:

        - the component corresponding to ``args`` or, if ``args`` = ``:``,
          the full list of components, in the form ``T[i][j]...`` for the components
          `T_{ij...}` (for a 2-indices object, a matrix is returned).

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: c = CompWithSym(ZZ, [1,2,3], 4, sym=(0,1), antisym=(2,3))
            sage: c.__getitem__((0,1,1,2)) # uninitialized components are zero
            0
            sage: c[0,1,1,2] = 5
            sage: c.__getitem__((0,1,1,2))
            5
            sage: c.__getitem__((1,0,1,2))
            5
            sage: c.__getitem__((0,1,2,1))
            -5
            sage: c[0,1,2,1]
            -5
        """
    def __setitem__(self, args, value) -> None:
        """
        Set the component corresponding to the given indices.

        INPUT:

        - ``args`` -- list of indices (possibly a single integer if
          ``self`` is a 1-index object) ; if ``[:]`` is provided, all the
          components are set
        - ``value`` -- the value to be set or a list of values if
          ``args = [:]``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: c = CompWithSym(ZZ, [1,2,3], 2, sym=(0,1))
            sage: c.__setitem__((1,2), 5)
            sage: c[:]
            [0 0 0]
            [0 0 5]
            [0 5 0]
            sage: c = CompWithSym(ZZ, [1,2,3], 2, antisym=(0,1))
            sage: c.__setitem__((1,2), 5)
            sage: c[:]
            [ 0  0  0]
            [ 0  0  5]
            [ 0 -5  0]
            sage: c.__setitem__((2,2), 5)
            Traceback (most recent call last):
            ...
            ValueError: by antisymmetry, the component cannot have a nonzero value for the indices (2, 2)
        """
    def swap_adjacent_indices(self, pos1, pos2, pos3):
        """
        Swap two adjacent sets of indices.

        This method is essentially required to reorder the covariant and
        contravariant indices in the computation of a tensor product.

        The symmetries are preserved and the corresponding indices are adjusted
        consequently.

        INPUT:

        - ``pos1`` -- position of the first index of set 1 (with the convention
          position=0 for the first slot)
        - ``pos2`` -- position of the first index of set 2 = 1 + position of
          the last index of set 1 (since the two sets are adjacent)
        - ``pos3`` -- 1 + position of the last index of set 2

        OUTPUT: components with index set 1 permuted with index set 2

        EXAMPLES:

        Swap of the index in position 0 with the pair of indices in position
        (1,2) in a set of components antisymmetric with respect to the indices
        in position (1,2)::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: V = VectorSpace(QQ, 3)
            sage: c = CompWithSym(QQ, V.basis(), 3, antisym=(1,2))
            sage: c[0,0,1], c[0,0,2], c[0,1,2] = (1,2,3)
            sage: c[1,0,1], c[1,0,2], c[1,1,2] = (4,5,6)
            sage: c[2,0,1], c[2,0,2], c[2,1,2] = (7,8,9)
            sage: c[:]
            [[[0, 1, 2], [-1, 0, 3], [-2, -3, 0]],
             [[0, 4, 5], [-4, 0, 6], [-5, -6, 0]],
             [[0, 7, 8], [-7, 0, 9], [-8, -9, 0]]]
            sage: c1 = c.swap_adjacent_indices(0,1,3)
            sage: c._antisym   # c is antisymmetric with respect to the last pair of indices...
            ((1, 2),)
            sage: c1._antisym  #...while c1 is antisymmetric with respect to the first pair of indices
            ((0, 1),)
            sage: c[0,1,2]
            3
            sage: c1[1,2,0]
            3
            sage: c1[2,1,0]
            -3
        """
    def __add__(self, other):
        """
        Component addition.

        INPUT:

        - ``other`` -- components of the same number of indices and defined
          on the same frame as ``self``

        OUTPUT: components resulting from the addition of ``self`` and ``other``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: a = CompWithSym(ZZ, [1,2,3], 2, sym=(0,1))
            sage: a[0,1], a[1,2] = 4, 5
            sage: b = CompWithSym(ZZ, [1,2,3], 2, sym=(0,1))
            sage: b[0,1], b[2,2] = 2, -3
            sage: s = a.__add__(b) ; s  # the symmetry is kept
            2-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (0, 1)
            sage: s[:]
            [ 0  6  0]
            [ 6  0  5]
            [ 0  5 -3]
            sage: s == a + b
            True

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: s_par = a + b ; s_par
            2-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (0, 1)
            sage: s_par[:] == s[:]
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization

        Addition with different symmetries::

            sage: c = CompWithSym(ZZ, [1,2,3], 2, antisym=(0,1))
            sage: c[0,1], c[0,2] = 3, 7
            sage: s = a.__add__(c) ; s  # the symmetry is lost
            2-indices components w.r.t. [1, 2, 3]
            sage: s[:]
            [ 0  7  7]
            [ 1  0  5]
            [-7  5  0]

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: s_par = a + c ; s_par
            2-indices components w.r.t. [1, 2, 3]
            sage: s_par[:] == s[:]
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def __mul__(self, other):
        """
        Component tensor product.

        INPUT:

        - ``other`` -- components, on the same frame as ``self``

        OUTPUT: the tensor product of ``self`` by ``other``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompWithSym
            sage: a = CompWithSym(ZZ, [1,2,3], 2, sym=(0,1))
            sage: a[0,1], a[1,2] = 4, 5
            sage: b = CompWithSym(ZZ, [1,2,3], 2, sym=(0,1))
            sage: b[0,1], b[2,2] = 2, -3
            sage: s1 = a.__mul__(b) ; s1
            4-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (0, 1), with symmetry on the index positions (2, 3)
            sage: s1[1,0,0,1]
            8
            sage: s1[1,0,0,1] == a[1,0] * b[0,1]
            True
            sage: s1 == a*b
            True
            sage: c = CompWithSym(ZZ, [1,2,3], 2, antisym=(0,1))
            sage: c[0,1], c[0,2] = 3, 7
            sage: s2 = a.__mul__(c) ; s2
            4-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (0, 1), with antisymmetry on the index positions (2, 3)
            sage: s2[1,0,2,0]
            -28
            sage: s2[1,0,2,0] == a[1,0] * c[2,0]
            True
            sage: s2 == a*c
            True

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: Parallelism().get('tensor')
            2
            sage: s1_par = a.__mul__(b) ; s1_par
            4-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (0, 1), with symmetry on the index positions (2, 3)
            sage: s1_par[1,0,0,1]
            8
            sage: s1_par[:] == s1[:]
            True
            sage: s2_par = a.__mul__(c) ; s2_par
            4-indices components w.r.t. [1, 2, 3], with symmetry on the index positions (0, 1), with antisymmetry on the index positions (2, 3)
            sage: s2_par[1,0,2,0]
            -28
            sage: s2_par[:] == s2[:]
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def trace(self, pos1, pos2):
        """
        Index contraction, taking care of the symmetries.

        INPUT:

        - ``pos1`` -- position of the first index for the contraction (with
          the convention position=0 for the first slot)
        - ``pos2`` -- position of the second index for the contraction

        OUTPUT:

        - set of components resulting from the (pos1, pos2) contraction

        EXAMPLES:

        Self-contraction of symmetric 2-indices components::

            sage: from sage.tensor.modules.comp import Components, CompWithSym, \\\n            ....:   CompFullySym, CompFullyAntiSym
            sage: V = VectorSpace(QQ, 3)
            sage: a = CompFullySym(QQ, V.basis(), 2)
            sage: a[:] = [[1,2,3],[2,4,5],[3,5,6]]
            sage: a.trace(0,1)
            11
            sage: a[0,0] + a[1,1] + a[2,2]
            11

        Self-contraction of antisymmetric 2-indices components::

            sage: b = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: b[0,1], b[0,2], b[1,2] = (3, -2, 1)
            sage: b.trace(0,1)  # must be zero by antisymmetry
            0

        Self-contraction of 3-indices components with one symmetry::

            sage: v = Components(QQ, V.basis(), 1)
            sage: v[:] = (-2, 4, -8)
            sage: c = v*b ; c
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (1, 2)
            sage: s = c.trace(0,1) ; s
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s[:]
            [-28, 2, 8]
            sage: [sum(v[k]*b[k,i] for k in range(3)) for i in range(3)] # check
            [-28, 2, 8]
            sage: s = c.trace(1,2) ; s
            1-index components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s[:] # is zero by antisymmetry
            [0, 0, 0]
            sage: c = b*v ; c
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 1)
            sage: s = c.trace(0,1)
            sage: s[:]  # is zero by antisymmetry
            [0, 0, 0]
            sage: s = c.trace(1,2) ; s[:]
            [28, -2, -8]
            sage: [sum(b[i,k]*v[k] for k in range(3)) for i in range(3)]  # check
            [28, -2, -8]

        Self-contraction of 4-indices components with two symmetries::

            sage: c = a*b ; c
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1), with antisymmetry on the index positions (2, 3)
            sage: s = c.trace(0,1) ; s  # the symmetry on (0,1) is lost:
            Fully antisymmetric 2-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s[:]
            [  0  33 -22]
            [-33   0  11]
            [ 22 -11   0]
            sage: [[sum(c[k,k,i,j] for k in range(3)) for j in range(3)] for i in range(3)]  # check
            [[0, 33, -22], [-33, 0, 11], [22, -11, 0]]
            sage: s = c.trace(1,2) ; s  # both symmetries are lost by this contraction
            2-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s[:]
            [ 0  0  0]
            [-2  1  0]
            [-3  3 -1]
            sage: [[sum(c[i,k,k,j] for k in range(3)) for j in range(3)] for i in range(3)]  # check
            [[0, 0, 0], [-2, 1, 0], [-3, 3, -1]]
        """
    def non_redundant_index_generator(self) -> Generator[Incomplete]:
        """
        Generator of indices, with only ordered indices in case of symmetries,
        so that only non-redundant indices are generated.

        OUTPUT: an iterable index

        EXAMPLES:

        Indices on a 2-dimensional space::

            sage: from sage.tensor.modules.comp import Components, CompWithSym, \\\n            ....:  CompFullySym, CompFullyAntiSym
            sage: V = VectorSpace(QQ, 2)
            sage: c = CompFullySym(QQ, V.basis(), 2)
            sage: list(c.non_redundant_index_generator())
            [(0, 0), (0, 1), (1, 1)]
            sage: c = CompFullySym(QQ, V.basis(), 2, start_index=1)
            sage: list(c.non_redundant_index_generator())
            [(1, 1), (1, 2), (2, 2)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: list(c.non_redundant_index_generator())
            [(0, 1)]

        Indices on a 3-dimensional space::

            sage: V = VectorSpace(QQ, 3)
            sage: c = CompFullySym(QQ, V.basis(), 2)
            sage: list(c.non_redundant_index_generator())
            [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
            sage: c = CompFullySym(QQ, V.basis(), 2, start_index=1)
            sage: list(c.non_redundant_index_generator())
            [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: list(c.non_redundant_index_generator())
            [(0, 1), (0, 2), (1, 2)]
            sage: c = CompWithSym(QQ, V.basis(), 3, sym=(1,2))  # symmetry on the last two indices
            sage: list(c.non_redundant_index_generator())
            [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1), (1, 0, 1),
             (2, 0, 1), (0, 0, 2), (1, 0, 2), (2, 0, 2), (0, 1, 1),
             (1, 1, 1), (2, 1, 1), (0, 1, 2), (1, 1, 2), (2, 1, 2),
             (0, 2, 2), (1, 2, 2), (2, 2, 2)]
            sage: c = CompWithSym(QQ, V.basis(), 3, antisym=(1,2))  # antisymmetry on the last two indices
            sage: list(c.non_redundant_index_generator())
            [(0, 0, 1), (1, 0, 1), (2, 0, 1), (0, 0, 2), (1, 0, 2),
             (2, 0, 2), (0, 1, 2), (1, 1, 2), (2, 1, 2)]
            sage: c = CompFullySym(QQ, V.basis(), 3)
            sage: list(c.non_redundant_index_generator())
            [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 2),
             (1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 3)
            sage: list(c.non_redundant_index_generator())
            [(0, 1, 2)]

        Indices on a 4-dimensional space::

            sage: V = VectorSpace(QQ, 4)
            sage: c = Components(QQ, V.basis(), 1)
            sage: list(c.non_redundant_index_generator())
            [(0,), (1,), (2,), (3,)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: list(c.non_redundant_index_generator())
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 3)
            sage: list(c.non_redundant_index_generator())
            [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 4)
            sage: list(c.non_redundant_index_generator())
            [(0, 1, 2, 3)]
            sage: c = CompFullyAntiSym(QQ, V.basis(), 5)
            sage: list(c.non_redundant_index_generator())  # nothing since c is identically zero in this case (for 5 > 4)
            []
        """
    def symmetrize(self, *pos):
        """
        Symmetrization over the given index positions.

        INPUT:

        - ``pos`` -- list of index positions involved in the
          symmetrization (with the convention ``position=0`` for the first
          slot); if none, the symmetrization is performed over all the indices

        OUTPUT:

        - an instance of :class:`CompWithSym` describing the symmetrized
          components

        EXAMPLES:

        Symmetrization of 3-indices components on a 3-dimensional space::

            sage: from sage.tensor.modules.comp import Components, CompWithSym, \\\n            ....:   CompFullySym, CompFullyAntiSym
            sage: V = VectorSpace(QQ, 3)
            sage: c = Components(QQ, V.basis(), 3)
            sage: c[:] = [[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]], [[19,20,21], [22,23,24], [25,26,27]]]
            sage: cs = c.symmetrize(0,1) ; cs
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1)
            sage: s = cs.symmetrize() ; s
            Fully symmetric 3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: cs[:], s[:]
            ([[[1, 2, 3], [7, 8, 9], [13, 14, 15]],
              [[7, 8, 9], [13, 14, 15], [19, 20, 21]],
              [[13, 14, 15], [19, 20, 21], [25, 26, 27]]],
             [[[1, 16/3, 29/3], [16/3, 29/3, 14], [29/3, 14, 55/3]],
              [[16/3, 29/3, 14], [29/3, 14, 55/3], [14, 55/3, 68/3]],
              [[29/3, 14, 55/3], [14, 55/3, 68/3], [55/3, 68/3, 27]]])
            sage: s == c.symmetrize() # should be true
            True
            sage: s1 = cs.symmetrize(0,1) ; s1   # should return a copy of cs
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1)
            sage: s1 == cs    # check that s1 is a copy of cs
            True

        Let us now start with a symmetry on the last two indices::

            sage: cs1 = c.symmetrize(1,2) ; cs1
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (1, 2)
            sage: s2 = cs1.symmetrize() ; s2
            Fully symmetric 3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s2 == c.symmetrize()
            True

        Symmetrization alters pre-existing symmetries: let us symmetrize w.r.t.
        the index positions `(1, 2)` a set of components that is symmetric
        w.r.t. the index positions `(0, 1)`::

            sage: cs = c.symmetrize(0,1) ; cs
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1)
            sage: css = cs.symmetrize(1,2)
            sage: css # the symmetry (0,1) has been lost:
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (1, 2)
            sage: css[:]
            [[[1, 9/2, 8], [9/2, 8, 23/2], [8, 23/2, 15]],
             [[7, 21/2, 14], [21/2, 14, 35/2], [14, 35/2, 21]],
             [[13, 33/2, 20], [33/2, 20, 47/2], [20, 47/2, 27]]]
            sage: cs[:]
            [[[1, 2, 3], [7, 8, 9], [13, 14, 15]],
             [[7, 8, 9], [13, 14, 15], [19, 20, 21]],
             [[13, 14, 15], [19, 20, 21], [25, 26, 27]]]
            sage: css == c.symmetrize() # css differs from the full symmetrized version
            False
            sage: css.symmetrize() == c.symmetrize() # one has to symmetrize css over all indices to recover it
            True

        Another example of symmetry alteration: symmetrization over `(0, 1)` of
        a 4-indices set of components that is symmetric w.r.t. `(1, 2, 3)`::

            sage: v = Components(QQ, V.basis(), 1)
            sage: v[:] = (-2,1,4)
            sage: a = v*s ; a
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (1, 2, 3)
            sage: a1 = a.symmetrize(0,1) ; a1 # the symmetry (1,2,3) has been reduced to (2,3):
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1), with symmetry on the index positions (2, 3)
            sage: a1._sym  # a1 has two distinct symmetries:
            ((0, 1), (2, 3))
            sage: a[0,1,2,0] == a[0,0,2,1]  # a is symmetric w.r.t. positions 1 and 3
            True
            sage: a1[0,1,2,0] == a1[0,0,2,1] # a1 is not
            False
            sage: a1[0,1,2,0] == a1[1,0,2,0] # but it is symmetric w.r.t. position 0 and 1
            True
            sage: a[0,1,2,0] == a[1,0,2,0] # while a is not
            False

        Partial symmetrization of 4-indices components with an antisymmetry on
        the last two indices::

            sage: a = Components(QQ, V.basis(), 2)
            sage: a[:] = [[-1,2,3], [4,5,-6], [7,8,9]]
            sage: b = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: b[0,1], b[0,2], b[1,2] = (2, 4, 8)
            sage: c = a*b ; c
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (2, 3)
            sage: s = c.symmetrize(0,1) ; s  # symmetrization on the first two indices
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1), with antisymmetry on the index positions (2, 3)
            sage: s[0,1,2,1] == (c[0,1,2,1] + c[1,0,2,1]) / 2 # check of the symmetrization
            True
            sage: s = c.symmetrize() ; s  # symmetrization over all the indices
            Fully symmetric 4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s == 0    # the full symmetrization results in zero due to the antisymmetry on the last two indices
            True
            sage: s = c.symmetrize(2,3) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (2, 3)
            sage: s == 0    # must be zero since the symmetrization has been performed on the antisymmetric indices
            True
            sage: s = c.symmetrize(0,2) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 2)
            sage: s != 0  # s is not zero, but the antisymmetry on (2,3) is lost because the position 2 is involved in the new symmetry
            True

        Partial symmetrization of 4-indices components with an antisymmetry on
        the last three indices::

            sage: a = Components(QQ, V.basis(), 1)
            sage: a[:] = (1, -2, 3)
            sage: b = CompFullyAntiSym(QQ, V.basis(), 3)
            sage: b[0,1,2] = 4
            sage: c = a*b ; c
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (1, 2, 3)
            sage: s = c.symmetrize(0,1) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1),
               with antisymmetry on the index positions (2, 3)

        Note that the antisymmetry on `(1, 2, 3)` has been reduced to
        `(2, 3)` only::

            sage: s = c.symmetrize(1,2) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (1, 2)
            sage: s == 0 # because (1,2) are involved in the original antisymmetry
            True
        """
    def antisymmetrize(self, *pos):
        """
        Antisymmetrization over the given index positions.

        INPUT:

        - ``pos`` -- list of index positions involved in the antisymmetrization
          (with the convention ``position=0`` for the first slot); if none, the
          antisymmetrization is performed over all the indices

        OUTPUT:

        - an instance of :class:`CompWithSym` describing the antisymmetrized
          components

        EXAMPLES:

        Antisymmetrization of 3-indices components on a 3-dimensional space::

            sage: from sage.tensor.modules.comp import Components, CompWithSym, \\\n            ....:  CompFullySym, CompFullyAntiSym
            sage: V = VectorSpace(QQ, 3)
            sage: a = Components(QQ, V.basis(), 1)
            sage: a[:] = (-2,1,3)
            sage: b = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: b[0,1], b[0,2], b[1,2] = (4,1,2)
            sage: c = a*b ; c   # tensor product of a by b
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (1, 2)
            sage: s = c.antisymmetrize() ; s
            Fully antisymmetric 3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: c[:], s[:]
            ([[[0, -8, -2], [8, 0, -4], [2, 4, 0]],
              [[0, 4, 1], [-4, 0, 2], [-1, -2, 0]],
              [[0, 12, 3], [-12, 0, 6], [-3, -6, 0]]],
             [[[0, 0, 0], [0, 0, 7/3], [0, -7/3, 0]],
              [[0, 0, -7/3], [0, 0, 0], [7/3, 0, 0]],
              [[0, 7/3, 0], [-7/3, 0, 0], [0, 0, 0]]])

        Check of the antisymmetrization::

            sage: all(s[i,j,k] == (c[i,j,k]-c[i,k,j]+c[j,k,i]-c[j,i,k]+c[k,i,j]-c[k,j,i])/6
            ....:     for i in range(3) for j in range(3) for k in range(3))
            True

        Antisymmetrization over already antisymmetric indices does not change anything::

            sage: s1 = s.antisymmetrize(1,2) ; s1
            Fully antisymmetric 3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s1 == s
            True
            sage: c1 = c.antisymmetrize(1,2) ; c1
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (1, 2)
            sage: c1 == c
            True

        But in general, antisymmetrization may alter previous antisymmetries::

            sage: c2 = c.antisymmetrize(0,1) ; c2  # the antisymmetry (2,3) is lost:
            3-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 1)
            sage: c2 == c
            False
            sage: c = s*a ; c
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 1, 2)
            sage: s = c.antisymmetrize(1,3) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 2),
               with antisymmetry on the index positions (1, 3)
            sage: s._antisym  # the antisymmetry (0,1,2) has been reduced to (0,2), since 1 is involved in the new antisymmetry (1,3):
            ((0, 2), (1, 3))

        Partial antisymmetrization of 4-indices components with a symmetry on
        the first two indices::

            sage: a = CompFullySym(QQ, V.basis(), 2)
            sage: a[:] = [[-2,1,3], [1,0,-5], [3,-5,4]]
            sage: b = Components(QQ, V.basis(), 2)
            sage: b[:] = [[1,2,3], [5,7,11], [13,17,19]]
            sage: c = a*b ; c
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1)
            sage: s = c.antisymmetrize(2,3) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with symmetry on the index positions (0, 1),
               with antisymmetry on the index positions (2, 3)

        Some check of the antisymmetrization::

            sage: all(s[2,2,i,j] == (c[2,2,i,j] - c[2,2,j,i])/2
            ....:     for i in range(3) for j in range(i,3))
            True

        The full antisymmetrization results in zero because of the symmetry on the
        first two indices::

            sage: s = c.antisymmetrize() ; s
            Fully antisymmetric 4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ]
            sage: s == 0
            True

        Similarly, the partial antisymmetrization on the first two indices results in zero::

            sage: s = c.antisymmetrize(0,1) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 1)
            sage: s == 0
            True

        The partial antisymmetrization on the positions `(0, 2)` destroys
        the symmetry on `(0, 1)`::

            sage: s = c.antisymmetrize(0,2) ; s
            4-indices components w.r.t. [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1)
            ], with antisymmetry on the index positions (0, 2)
            sage: s != 0
            True
            sage: s[0,1,2,1]
            27/2
            sage: s[1,0,2,1]  # the symmetry (0,1) is lost
            -2
            sage: s[2,1,0,1]  # the antisymmetry (0,2) holds
            -27/2
        """

class CompFullySym(CompWithSym):
    '''
    Indexed set of ring elements forming some components with respect to a
    given "frame" that are fully symmetric with respect to any permutation
    of the indices.

    The "frame" can be a basis of some vector space or a vector frame on some
    manifold (i.e. a field of bases).
    The stored quantities can be tensor components or non-tensorial quantities.

    INPUT:

    - ``ring`` -- commutative ring in which each component takes its value
    - ``frame`` -- frame with respect to which the components are defined;
      whatever type ``frame`` is, it should have some method ``__len__()``
      implemented, so that ``len(frame)`` returns the dimension, i.e. the size
      of a single index range
    - ``nb_indices`` -- number of indices labeling the components
    - ``start_index`` -- (default: 0) first value of a single index;
      accordingly a component index i must obey
      ``start_index <= i <= start_index + dim - 1``, where ``dim = len(frame)``.
    - ``output_formatter`` -- (default: ``None``) function or unbound
      method called to format the output of the component access
      operator ``[...]`` (method __getitem__); ``output_formatter`` must take
      1 or 2 arguments: the 1st argument must be an instance of ``ring`` and
      the second one, if any, some format specification.

    EXAMPLES:

    Symmetric components with 2 indices on a 3-dimensional space::

        sage: from sage.tensor.modules.comp import CompFullySym, CompWithSym
        sage: V = VectorSpace(QQ, 3)
        sage: c = CompFullySym(QQ, V.basis(), 2)
        sage: c[0,0], c[0,1], c[1,2] = 1, -2, 3
        sage: c[:] # note that c[1,0] and c[2,1] have been updated automatically (by symmetry)
        [ 1 -2  0]
        [-2  0  3]
        [ 0  3  0]

    Internally, only non-redundant and nonzero components are stored::

        sage: c._comp  # random output order of the component dictionary
        {(0, 0): 1, (0, 1): -2, (1, 2): 3}

    Same thing, but with the starting index set to 1::

        sage: c1 = CompFullySym(QQ, V.basis(), 2, start_index=1)
        sage: c1[1,1], c1[1,2], c1[2,3] = 1, -2, 3
        sage: c1[:]
        [ 1 -2  0]
        [-2  0  3]
        [ 0  3  0]

    The values stored in ``c`` and ``c1`` are equal::

        sage: c1[:] == c[:]
        True

    but not ``c`` and ``c1``, since their starting indices differ::

        sage: c1 == c
        False

    Fully symmetric components with 3 indices on a 3-dimensional space::

        sage: a = CompFullySym(QQ, V.basis(), 3)
        sage: a[0,1,2] = 3
        sage: a[:]
        [[[0, 0, 0], [0, 0, 3], [0, 3, 0]],
         [[0, 0, 3], [0, 0, 0], [3, 0, 0]],
         [[0, 3, 0], [3, 0, 0], [0, 0, 0]]]
        sage: a[0,1,0] = 4
        sage: a[:]
        [[[0, 4, 0], [4, 0, 3], [0, 3, 0]],
         [[4, 0, 3], [0, 0, 0], [3, 0, 0]],
         [[0, 3, 0], [3, 0, 0], [0, 0, 0]]]

    The full symmetry is preserved by the arithmetics::

        sage: b = CompFullySym(QQ, V.basis(), 3)
        sage: b[0,0,0], b[0,1,0], b[1,0,2], b[1,2,2] = -2, 3, 1, -5
        sage: s = a + 2*b ; s
        Fully symmetric 3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
        sage: a[:], b[:], s[:]
        ([[[0, 4, 0], [4, 0, 3], [0, 3, 0]],
          [[4, 0, 3], [0, 0, 0], [3, 0, 0]],
          [[0, 3, 0], [3, 0, 0], [0, 0, 0]]],
         [[[-2, 3, 0], [3, 0, 1], [0, 1, 0]],
          [[3, 0, 1], [0, 0, 0], [1, 0, -5]],
          [[0, 1, 0], [1, 0, -5], [0, -5, 0]]],
         [[[-4, 10, 0], [10, 0, 5], [0, 5, 0]],
          [[10, 0, 5], [0, 0, 0], [5, 0, -10]],
          [[0, 5, 0], [5, 0, -10], [0, -10, 0]]])

    It is lost if the added object is not fully symmetric::

        sage: b1 = CompWithSym(QQ, V.basis(), 3, sym=(0,1))  # b1 has only symmetry on index positions (0,1)
        sage: b1[0,0,0], b1[0,1,0], b1[1,0,2], b1[1,2,2] = -2, 3, 1, -5
        sage: s = a + 2*b1 ; s  # the result has the same symmetry as b1:
        3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ], with symmetry on the index positions (0, 1)
        sage: a[:], b1[:], s[:]
        ([[[0, 4, 0], [4, 0, 3], [0, 3, 0]],
          [[4, 0, 3], [0, 0, 0], [3, 0, 0]],
          [[0, 3, 0], [3, 0, 0], [0, 0, 0]]],
         [[[-2, 0, 0], [3, 0, 1], [0, 0, 0]],
          [[3, 0, 1], [0, 0, 0], [0, 0, -5]],
          [[0, 0, 0], [0, 0, -5], [0, 0, 0]]],
         [[[-4, 4, 0], [10, 0, 5], [0, 3, 0]],
          [[10, 0, 5], [0, 0, 0], [3, 0, -10]],
          [[0, 3, 0], [3, 0, -10], [0, 0, 0]]])
        sage: s = 2*b1 + a ; s
        3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ], with symmetry on the index positions (0, 1)
        sage: 2*b1 + a == a + 2*b1
        True
    '''
    def __init__(self, ring, frame, nb_indices, start_index: int = 0, output_formatter=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.comp import CompFullySym
            sage: C = CompFullySym(ZZ, (1,2,3), 2)
            sage: TestSuite(C).run()
        """
    def __getitem__(self, args):
        """
        Return the component corresponding to the given indices of ``self``.

        INPUT:

        - ``args`` -- list of indices (possibly a single integer if
          ``self`` is a 1-index object) or the character ``:`` for the full list
          of components

        OUTPUT:

        - the component corresponding to ``args`` or, if ``args`` = ``:``,
          the full list of components, in the form ``T[i][j]...`` for the
          components `T_{ij...}` (for a 2-indices object, a matrix is returned)

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompFullySym
            sage: c = CompFullySym(ZZ, (1,2,3), 2)
            sage: c[0,1] = 4
            sage: c.__getitem__((0,1))
            4
            sage: c.__getitem__((1,0))
            4
            sage: c.__getitem__(slice(None))
            [0 4 0]
            [4 0 0]
            [0 0 0]
        """
    def __setitem__(self, args, value) -> None:
        """
        Set the component corresponding to the given indices.

        INPUT:

        - ``indices`` -- list of indices (possibly a single integer if
          ``self`` is a 1-index object); if [:] is provided, all the components
          are set
        - ``value`` -- the value to be set or a list of values if
          ``args = [:]``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompFullySym
            sage: c = CompFullySym(ZZ, (1,2,3), 2)
            sage: c.__setitem__((0,1), 4)
            sage: c[:]
            [0 4 0]
            [4 0 0]
            [0 0 0]
            sage: c.__setitem__((2,1), 5)
            sage: c[:]
            [0 4 0]
            [4 0 5]
            [0 5 0]
            sage: c.__setitem__(slice(None), [[1, 2, 3], [2, 4, 5], [3, 5, 6]])
            sage: c[:]
            [1 2 3]
            [2 4 5]
            [3 5 6]
        """
    def __add__(self, other):
        """
        Component addition.

        INPUT:

        - ``other`` -- components of the same number of indices and defined
          on the same frame as ``self``

        OUTPUT: components resulting from the addition of ``self`` and ``other``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompFullySym
            sage: a = CompFullySym(ZZ, (1,2,3), 2)
            sage: a[0,1], a[1,2] = 4, 5
            sage: b = CompFullySym(ZZ, (1,2,3), 2)
            sage: b[0,1], b[2,2] = 2, -3
            sage: s = a.__add__(b) ; s  # the symmetry is kept
            Fully symmetric 2-indices components w.r.t. (1, 2, 3)
            sage: s[:]
            [ 0  6  0]
            [ 6  0  5]
            [ 0  5 -3]
            sage: s == a + b
            True

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: Parallelism().get('tensor')
            2
            sage: s_par = a.__add__(b) ; s_par
            Fully symmetric 2-indices components w.r.t. (1, 2, 3)
            sage: s_par[:]
            [ 0  6  0]
            [ 6  0  5]
            [ 0  5 -3]
            sage: s_par == s
            True
            sage: s_par == b.__add__(a)  # test of commutativity of parallel comput.
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization

        Addition with a set of components having different symmetries::

            sage: from sage.tensor.modules.comp import CompFullyAntiSym
            sage: c = CompFullyAntiSym(ZZ, (1,2,3), 2)
            sage: c[0,1], c[0,2] = 3, 7
            sage: s = a.__add__(c) ; s  # the symmetry is lost
            2-indices components w.r.t. (1, 2, 3)
            sage: s[:]
            [ 0  7  7]
            [ 1  0  5]
            [-7  5  0]
            sage: s == a + c
            True

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: Parallelism().get('tensor')
            2
            sage: s_par = a.__add__(c) ; s_par
            2-indices components w.r.t. (1, 2, 3)
            sage: s_par[:]
            [ 0  7  7]
            [ 1  0  5]
            [-7  5  0]
            sage: s_par[:] == s[:]
            True
            sage: s_par == c.__add__(a)  # test of commutativity of parallel comput.
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """

class CompFullyAntiSym(CompWithSym):
    '''
    Indexed set of ring elements forming some components with respect to a
    given "frame" that are fully antisymmetric with respect to any permutation
    of the indices.

    The "frame" can be a basis of some vector space or a vector frame on some
    manifold (i.e. a field of bases).
    The stored quantities can be tensor components or non-tensorial quantities.

    INPUT:

    - ``ring`` -- commutative ring in which each component takes its value
    - ``frame`` -- frame with respect to which the components are defined;
      whatever type ``frame`` is, it should have some method ``__len__()``
      implemented, so that ``len(frame)`` returns the dimension, i.e. the size
      of a single index range
    - ``nb_indices`` -- number of indices labeling the components
    - ``start_index`` -- (default: 0) first value of a single index;
      accordingly a component index i must obey
      ``start_index <= i <= start_index + dim - 1``, where ``dim = len(frame)``.
    - ``output_formatter`` -- (default: ``None``) function or unbound
      method called to format the output of the component access
      operator ``[...]`` (method __getitem__); ``output_formatter`` must take
      1 or 2 arguments: the 1st argument must be an instance of ``ring`` and
      the second one, if any, some format specification.

    EXAMPLES:

    Antisymmetric components with 2 indices on a 3-dimensional space::

        sage: from sage.tensor.modules.comp import CompWithSym, CompFullyAntiSym
        sage: V = VectorSpace(QQ, 3)
        sage: c = CompFullyAntiSym(QQ, V.basis(), 2)
        sage: c[0,1], c[0,2], c[1,2] = 3, 1/2, -1
        sage: c[:]  # note that all components have been set according to the antisymmetry
        [   0    3  1/2]
        [  -3    0   -1]
        [-1/2    1    0]

    Internally, only non-redundant and nonzero components are stored::

        sage: c._comp # random output order of the component dictionary
        {(0, 1): 3, (0, 2): 1/2, (1, 2): -1}

    Same thing, but with the starting index set to 1::

        sage: c1 = CompFullyAntiSym(QQ, V.basis(), 2, start_index=1)
        sage: c1[1,2], c1[1,3], c1[2,3] = 3, 1/2, -1
        sage: c1[:]
        [   0    3  1/2]
        [  -3    0   -1]
        [-1/2    1    0]

    The values stored in ``c`` and ``c1`` are equal::

        sage: c1[:] == c[:]
        True

    but not ``c`` and ``c1``, since their starting indices differ::

        sage: c1 == c
        False

    Fully antisymmetric components with 3 indices on a 3-dimensional space::

        sage: a = CompFullyAntiSym(QQ, V.basis(), 3)
        sage: a[0,1,2] = 3  # the only independent component in dimension 3
        sage: a[:]
        [[[0, 0, 0], [0, 0, 3], [0, -3, 0]],
         [[0, 0, -3], [0, 0, 0], [3, 0, 0]],
         [[0, 3, 0], [-3, 0, 0], [0, 0, 0]]]

    Setting a nonzero value incompatible with the antisymmetry results in an
    error::

        sage: a[0,1,0] = 4
        Traceback (most recent call last):
        ...
        ValueError: by antisymmetry, the component cannot have a nonzero value for the indices (0, 1, 0)
        sage: a[0,1,0] = 0   # OK
        sage: a[2,0,1] = 3   # OK

    The full antisymmetry is preserved by the arithmetics::

        sage: b = CompFullyAntiSym(QQ, V.basis(), 3)
        sage: b[0,1,2] = -4
        sage: s = a + 2*b ; s
        Fully antisymmetric 3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
        sage: a[:], b[:], s[:]
        ([[[0, 0, 0], [0, 0, 3], [0, -3, 0]],
          [[0, 0, -3], [0, 0, 0], [3, 0, 0]],
          [[0, 3, 0], [-3, 0, 0], [0, 0, 0]]],
         [[[0, 0, 0], [0, 0, -4], [0, 4, 0]],
          [[0, 0, 4], [0, 0, 0], [-4, 0, 0]],
          [[0, -4, 0], [4, 0, 0], [0, 0, 0]]],
         [[[0, 0, 0], [0, 0, -5], [0, 5, 0]],
          [[0, 0, 5], [0, 0, 0], [-5, 0, 0]],
          [[0, -5, 0], [5, 0, 0], [0, 0, 0]]])

    It is lost if the added object is not fully antisymmetric::

        sage: b1 = CompWithSym(QQ, V.basis(), 3, antisym=(0,1))  # b1 has only antisymmetry on index positions (0,1)
        sage: b1[0,1,2] = -4
        sage: s = a + 2*b1 ; s  # the result has the same symmetry as b1:
        3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ], with antisymmetry on the index positions (0, 1)
        sage: a[:], b1[:], s[:]
        ([[[0, 0, 0], [0, 0, 3], [0, -3, 0]],
          [[0, 0, -3], [0, 0, 0], [3, 0, 0]],
          [[0, 3, 0], [-3, 0, 0], [0, 0, 0]]],
         [[[0, 0, 0], [0, 0, -4], [0, 0, 0]],
          [[0, 0, 4], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
         [[[0, 0, 0], [0, 0, -5], [0, -3, 0]],
          [[0, 0, 5], [0, 0, 0], [3, 0, 0]],
          [[0, 3, 0], [-3, 0, 0], [0, 0, 0]]])
        sage: s = 2*b1 + a ; s
        3-indices components w.r.t. [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ], with antisymmetry on the index positions (0, 1)
        sage: 2*b1 + a == a + 2*b1
        True
    '''
    def __init__(self, ring, frame, nb_indices, start_index: int = 0, output_formatter=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.comp import CompFullyAntiSym
            sage: C = CompFullyAntiSym(ZZ, (1,2,3), 2)
            sage: TestSuite(C).run()
        """
    def __add__(self, other):
        """
        Component addition.

        INPUT:

        - ``other`` -- components of the same number of indices and defined
          on the same frame as ``self``

        OUTPUT: components resulting from the addition of ``self`` and ``other``

        EXAMPLES::

            sage: from sage.tensor.modules.comp import CompFullyAntiSym
            sage: a = CompFullyAntiSym(ZZ, (1,2,3), 2)
            sage: a[0,1], a[1,2] = 4, 5
            sage: b = CompFullyAntiSym(ZZ, (1,2,3), 2)
            sage: b[0,1], b[0,2] = 2, -3
            sage: s = a.__add__(b) ; s  # the antisymmetry is kept
            Fully antisymmetric 2-indices components w.r.t. (1, 2, 3)
            sage: s[:]
            [ 0  6 -3]
            [-6  0  5]
            [ 3 -5  0]
            sage: s == a + b
            True
            sage: from sage.tensor.modules.comp import CompFullySym
            sage: c = CompFullySym(ZZ, (1,2,3), 2)
            sage: c[0,1], c[0,2] = 3, 7
            sage: s = a.__add__(c) ; s  # the antisymmetry is lost
            2-indices components w.r.t. (1, 2, 3)
            sage: s[:]
            [ 0  7  7]
            [-1  0  5]
            [ 7 -5  0]
            sage: s == a + c
            True

        Parallel computation::

            sage: from sage.tensor.modules.comp import CompFullyAntiSym
            sage: Parallelism().set('tensor', nproc=2)
            sage: a = CompFullyAntiSym(ZZ, (1,2,3), 2)
            sage: a[0,1], a[1,2] = 4, 5
            sage: b = CompFullyAntiSym(ZZ, (1,2,3), 2)
            sage: b[0,1], b[0,2] = 2, -3
            sage: s_par = a.__add__(b) ; s_par  # the antisymmetry is kept
            Fully antisymmetric 2-indices components w.r.t. (1, 2, 3)
            sage: s_par[:]
            [ 0  6 -3]
            [-6  0  5]
            [ 3 -5  0]
            sage: s_par == a + b
            True
            sage: from sage.tensor.modules.comp import CompFullySym
            sage: c = CompFullySym(ZZ, (1,2,3), 2)
            sage: c[0,1], c[0,2] = 3, 7
            sage: s_par = a.__add__(c) ; s_par  # the antisymmetry is lost
            2-indices components w.r.t. (1, 2, 3)
            sage: s_par[:]
            [ 0  7  7]
            [-1  0  5]
            [ 7 -5  0]
            sage: s_par == a + c
            True
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization
        """
    def interior_product(self, other):
        """
        Interior product with another set of fully antisymmetric components.

        The interior product amounts to a contraction over all the `p` indices
        of ``self`` with the first `p` indices of ``other``, assuming that
        the number `q` of indices of ``other`` obeys `q\\geq p`.

        .. NOTE::

            ``self.interior_product(other)`` yields the same result as
            ``self.contract(0,..., p-1, other, 0,..., p-1)``
            (cf. :meth:`~sage.tensor.modules.comp.Components.contract`), but
            ``interior_product`` is more efficient, the antisymmetry of ``self``
            being not used to reduce the computation in
            :meth:`~sage.tensor.modules.comp.Components.contract`.

        INPUT:

        - ``other`` -- fully antisymmetric components defined on the same frame
          as ``self`` and with a number of indices at least equal to that of
          ``self``

        OUTPUT:

        - base ring element (case `p=q`) or set of components (case `p<q`)
          resulting from the contraction over all the `p` indices of ``self``
          with the first `p` indices of ``other``

        EXAMPLES:

        Interior product of a set of components ``a`` with ``p`` indices with a
        set of components ``b`` with ``q`` indices on a 4-dimensional vector
        space.

        Case ``p=2`` and ``q=2``::

            sage: from sage.tensor.modules.comp import CompFullyAntiSym
            sage: V = VectorSpace(QQ, 4)
            sage: a = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: a[0,1], a[0,2], a[0,3] = -2, 4, 3
            sage: a[1,2], a[1,3], a[2,3] = 5, -3, 1
            sage: b = CompFullyAntiSym(QQ, V.basis(), 2)
            sage: b[0,1], b[0,2], b[0,3] = 3, -4, 2
            sage: b[1,2], b[1,3], b[2,3] = 2, 5, 1
            sage: c = a.interior_product(b)
            sage: c
            -40
            sage: c == a.contract(0, 1, b, 0, 1)
            True

        Case ``p=2`` and ``q=3``::

            sage: b = CompFullyAntiSym(QQ, V.basis(), 3)
            sage: b[0,1,2], b[0,1,3], b[0,2,3], b[1,2,3] = 3, -4, 2, 5
            sage: c = a.interior_product(b)
            sage: c[:]
            [58, 10, 6, 82]
            sage: c == a.contract(0, 1, b, 0, 1)
            True

        Case ``p=2`` and ``q=4``::

            sage: b = CompFullyAntiSym(QQ, V.basis(), 4)
            sage: b[0,1,2,3] = 5
            sage: c = a.interior_product(b)
            sage: c[:]
            [  0  10  30  50]
            [-10   0  30 -40]
            [-30 -30   0 -20]
            [-50  40  20   0]
            sage: c == a.contract(0, 1, b, 0, 1)
            True

        Case ``p=3`` and ``q=3``::

            sage: a = CompFullyAntiSym(QQ, V.basis(), 3)
            sage: a[0,1,2], a[0,1,3], a[0,2,3], a[1,2,3] = 2, -1, 3, 5
            sage: b = CompFullyAntiSym(QQ, V.basis(), 3)
            sage: b[0,1,2], b[0,1,3], b[0,2,3], b[1,2,3] = -2, 1, 4, 2
            sage: c = a.interior_product(b)
            sage: c
            102
            sage: c == a.contract(0, 1, 2, b, 0, 1, 2)
            True

        Case ``p=3`` and ``q=4``::

            sage: b = CompFullyAntiSym(QQ, V.basis(), 4)
            sage: b[0,1,2,3] = 5
            sage: c = a.interior_product(b)
            sage: c[:]
            [-150, 90, 30, 60]
            sage: c == a.contract(0, 1, 2, b, 0, 1, 2)
            True

        Case ``p=4`` and ``q=4``::

            sage: a = CompFullyAntiSym(QQ, V.basis(), 4)
            sage: a[0,1,2,3] = 3
            sage: c = a.interior_product(b)
            sage: c
            360
            sage: c == a.contract(0, 1, 2, 3, b, 0, 1, 2, 3)
            True
        """

class KroneckerDelta(CompFullySym):
    """
    Kronecker delta `\\delta_{ij}`.

    INPUT:

    - ``ring`` -- commutative ring in which each component takes its value
    - ``frame`` -- frame with respect to which the components are defined;
      whatever type ``frame`` is, it should have some method ``__len__()``
      implemented, so that ``len(frame)`` returns the dimension, i.e. the size
      of a single index range
    - ``start_index`` -- (default: 0) first value of a single index;
      accordingly a component index i must obey
      ``start_index <= i <= start_index + dim - 1``, where ``dim = len(frame)``.
    - ``output_formatter`` -- (default: ``None``) function or unbound
      method called to format the output of the component access
      operator ``[...]`` (method ``__getitem__``); ``output_formatter`` must
      take 1 or 2 arguments: the first argument must be an instance of
      ``ring`` and the second one, if any, some format specification

    EXAMPLES:

    The Kronecker delta on a 3-dimensional space::

        sage: from sage.tensor.modules.comp import KroneckerDelta
        sage: V = VectorSpace(QQ,3)
        sage: d = KroneckerDelta(QQ, V.basis()) ; d
        Kronecker delta of size 3x3
        sage: d[:]
        [1 0 0]
        [0 1 0]
        [0 0 1]

    One can read, but not set, the components of a Kronecker delta::

        sage: d[1,1]
        1
        sage: d[1,1] = 2
        Traceback (most recent call last):
        ...
        TypeError: the components of a Kronecker delta cannot be changed

    Examples of use with output formatters::

        sage: d = KroneckerDelta(QQ, V.basis(), output_formatter=Rational.numerical_approx)
        sage: d[:]  # default format (53 bits of precision)
        [ 1.00000000000000 0.000000000000000 0.000000000000000]
        [0.000000000000000  1.00000000000000 0.000000000000000]
        [0.000000000000000 0.000000000000000  1.00000000000000]
        sage: d[:,10] # format = 10 bits of precision
        [ 1.0 0.00 0.00]
        [0.00  1.0 0.00]
        [0.00 0.00  1.0]
        sage: d = KroneckerDelta(QQ, V.basis(), output_formatter=str)
        sage: d[:]
        [['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]
    """
    def __init__(self, ring, frame, start_index: int = 0, output_formatter=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.comp import KroneckerDelta
            sage: d = KroneckerDelta(ZZ, (1,2,3))
            sage: TestSuite(d).run()
        """
    def __setitem__(self, args, value) -> None:
        """
        Should not be used (the components of a Kronecker delta are constant).

        EXAMPLES::

            sage: from sage.tensor.modules.comp import KroneckerDelta
            sage: d = KroneckerDelta(ZZ, (1,2,3))
            sage: d.__setitem__((0,0), 1)
            Traceback (most recent call last):
            ...
            TypeError: the components of a Kronecker delta cannot be changed
        """
