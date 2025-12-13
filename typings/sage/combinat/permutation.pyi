from _typeshed import Incomplete
from collections.abc import Generator, Iterator
from sage.arith.misc import factorial as factorial, multinomial as multinomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.finite_permutation_groups import FinitePermutationGroups as FinitePermutationGroups
from sage.categories.finite_weyl_groups import FiniteWeylGroups as FiniteWeylGroups
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.combinat.SJT import SJT as SJT
from sage.combinat.backtrack import GenericBacktracker as GenericBacktracker
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement, catalan_number as catalan_number
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.composition import Composition as Composition
from sage.combinat.permutation_cython import left_action_product as left_action_product, left_action_same_n as left_action_same_n, map_to_list as map_to_list, next_perm as next_perm, right_action_product as right_action_product, right_action_same_n as right_action_same_n
from sage.combinat.tools import transitive_ideal as transitive_ideal
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.decorators import rename_keyword as rename_keyword
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import Element as Element, get_coercion_model as get_coercion_model
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Permutation(CombinatorialElement):
    """
    A permutation.

    Converts ``l`` to a permutation on `\\{1, 2, \\ldots, n\\}`.

    INPUT:

    - ``l`` -- can be any one of the following:

      - an instance of :class:`Permutation`,

      - list of integers, viewed as one-line permutation notation. The
        construction checks that you give an acceptable entry. To avoid
        the check, use the ``check`` option.

      - string, expressing the permutation in cycle notation.

      - list of tuples of integers, expressing the permutation in cycle
        notation.

      - a :class:`PermutationGroupElement`

      - a pair of two standard tableaux of the same shape. This yields
        the permutation obtained from the pair using the inverse of the
        Robinson-Schensted algorithm.

    - ``check`` -- boolean (default: ``True``); whether to check that input is
      correct; slows the function down, but ensures that nothing bad happens

    - ``algorithm`` -- string (default: ``'lex'``); the algorithm used to
      generate the permutations. Supported algorithms are:

      - ``'lex'``: lexicographic order generation, this is the default algorithm

      - ``'sjt'``: Steinhaus-Johnson-Trotter algorithm to generate permutations
        using only transposition of two elements in the list. It is highly
        recommended to set ``check=True`` (default value).

    - ``sjt`` -- SJT (default: ``None``); the ``SJT`` object holding the
      permutation internal state. This should only be specified when
      initializing with non-identity permutation.

    .. WARNING::

        Since :issue:`13742` the input is checked for correctness : it is not
        accepted unless it actually is a permutation on `\\{1, \\ldots, n\\}`. It
        means that some :meth:`Permutation` objects cannot be created anymore
        without setting ``check=False``, as there is no certainty that
        its functions can handle them, and this should be fixed in a much
        better way ASAP (the functions should be rewritten to handle those
        cases, and new tests be added).

    .. WARNING::

        There are two possible conventions for multiplying permutations, and
        the one currently enabled in Sage by default is the one which has
        `(pq)(i) = q(p(i))` for any permutations `p \\in S_n` and `q \\in S_n`
        and any `1 \\leq i \\leq n`. (This equation looks less strange when
        the action of permutations on numbers is written from the right:
        then it takes the form `i^{pq} = (i^p)^q`, which is an associativity
        law). There is an alternative convention, which has
        `(pq)(i) = p(q(i))` instead. The conventions can be switched at
        runtime using
        :meth:`sage.combinat.permutation.Permutations.options`.
        It is best for code not to rely on this setting being set to a
        particular standard, but rather use the methods
        :meth:`left_action_product` and :meth:`right_action_product` for
        multiplying permutations (these methods don't depend on the setting).
        See :issue:`14885` for more details.

    .. NOTE::

        The ``bruhat*`` methods refer to the *strong* Bruhat order. To use
        the *weak* Bruhat order, look under ``permutohedron*``.

    EXAMPLES::

        sage: Permutation([2,1])
        [2, 1]
        sage: Permutation([2, 1, 4, 5, 3])
        [2, 1, 4, 5, 3]
        sage: Permutation('(1,2)')
        [2, 1]
        sage: Permutation('(1,2)(3,4,5)')
        [2, 1, 4, 5, 3]
        sage: Permutation( ((1,2),(3,4,5)) )
        [2, 1, 4, 5, 3]
        sage: Permutation( [(1,2),(3,4,5)] )
        [2, 1, 4, 5, 3]
        sage: Permutation( ((1,2)) )
        [2, 1]
        sage: Permutation( (1,2) )
        [2, 1]
        sage: Permutation( ((1,2),) )
        [2, 1]
        sage: Permutation( ((1,),) )
        [1]
        sage: Permutation( (1,) )
        [1]
        sage: Permutation( () )
        []
        sage: Permutation( ((),) )
        []
        sage: p = Permutation((1, 2, 5)); p
        [2, 5, 3, 4, 1]
        sage: type(p)
        <class 'sage.combinat.permutation.StandardPermutations_n_with_category.element_class'>

    Generate permutations using the Steinhaus-Johnson Trotter algorithm. The
    output is not in lexicographic order::

        sage: p = Permutation([1, 2, 3, 4], algorithm='sjt'); p
        [1, 2, 3, 4]
        sage: p = p.next(); p
        [1, 2, 4, 3]
        sage: p = p.next(); p
        [1, 4, 2, 3]
        sage: p = Permutation([1, 2, 3], algorithm='sjt')
        sage: for _ in range(6):
        ....:     p = p.next()
        sage: p
        False

        sage: Permutation([1, 3, 2, 4], algorithm='sjt')
        Traceback (most recent call last):
        ...
        ValueError: no internal state directions were given for non-identity
        starting permutation for Steinhaus-Johnson-Trotter algorithm

    Construction from a string in cycle notation::

        sage: p = Permutation( '(4,5)' ); p
        [1, 2, 3, 5, 4]

    The size of the permutation is the maximum integer appearing; add
    a 1-cycle to increase this::

        sage: p2 = Permutation( '(4,5)(10)' ); p2
        [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
        sage: len(p); len(p2)
        5
        10

    We construct a :class:`Permutation` from a
    :class:`PermutationGroupElement`::

        sage: g = PermutationGroupElement([2,1,3])                                      # needs sage.groups
        sage: Permutation(g)                                                            # needs sage.groups
        [2, 1, 3]

    From a pair of tableaux of the same shape. This uses the inverse
    of the Robinson-Schensted algorithm::

        sage: # needs sage.combinat
        sage: p = [[1, 4, 7], [2, 5], [3], [6]]
        sage: q = [[1, 2, 5], [3, 6], [4], [7]]
        sage: P = Tableau(p)
        sage: Q = Tableau(q)
        sage: Permutation( (p, q) )
        [3, 6, 5, 2, 7, 4, 1]
        sage: Permutation( [p, q] )
        [3, 6, 5, 2, 7, 4, 1]
        sage: Permutation( (P, Q) )
        [3, 6, 5, 2, 7, 4, 1]
        sage: Permutation( [P, Q] )
        [3, 6, 5, 2, 7, 4, 1]

    TESTS::

        sage: Permutation([()])
        []
        sage: Permutation('()')
        []
        sage: Permutation(())
        []
        sage: Permutation( [1] )
        [1]

        sage: Permutation([1, 2, 3, 4], algorithm='blah')
        Traceback (most recent call last):
        ...
        ValueError: unsupported algorithm blah; expected 'lex' or 'sjt'

    From a pair of empty tableaux ::

        sage: Permutation( ([], []) )                                                   # needs sage.combinat
        []
        sage: Permutation( [[], []] )                                                   # needs sage.combinat
        []
    """
    @staticmethod
    def __classcall_private__(cls, l, algorithm: str = 'lex', sjt=None, check: bool = True):
        """
        Return a permutation in the general permutations parent.

        EXAMPLES::

            sage: P = Permutation([2,1]); P
            [2, 1]
            sage: P.parent()
            Standard permutations
        """
    def __init__(self, parent, l, algorithm: str = 'lex', sjt=None, check: bool = True) -> None:
        """
        Constructor. Checks that INPUT is not a mess, and calls
        :class:`CombinatorialElement`. It should not, because
        :class:`CombinatorialElement` is deprecated.

        INPUT:

        - ``l`` -- list of ``int`` variables

        - ``check`` -- boolean (default: ``True``); whether to check that input
          is correct. Slows the function down, but ensures that nothing bad
          happens.

        - ``algorithm`` -- string (default: ``'lex'``); the algorithm used to
          generate the permutations. Supported algorithms are:

          - ``'lex'``: lexicographic order generation, this is the default
            algorithm

          - ``'sjt'``: Steinhaus-Johnson-Trotter algorithm to generate
            permutations using only transposition of two elements in the list.
            It is highly recommended to set ``check=True`` (default value).

        - ``sjt`` -- SJT (default: ``None``); the ``SJT`` object holding the
          permutation internal state. This should only be specified when
          initializing with non-identity permutation.

        TESTS::

            sage: Permutation([1,2,3])
            [1, 2, 3]
            sage: Permutation([1,2,2,4])
            Traceback (most recent call last):
            ...
            ValueError: an element appears twice in the input
            sage: Permutation([1,2,4,-1])
            Traceback (most recent call last):
            ...
            ValueError: the elements must be strictly positive integers
            sage: Permutation([1,2,4,5])
            Traceback (most recent call last):
            ...
            ValueError: the permutation has length 4 but its maximal element is
            5. Some element may be repeated, or an element is missing, but there
            is something wrong with its length.

            sage: Permutation([1, 3, 2], algorithm='sjt')
            Traceback (most recent call last):
            ...
            ValueError: no internal state directions were given for non-identity
            starting permutation for Steinhaus-Johnson-Trotter algorithm

            sage: Permutation([1, 3, 2], algorithm='sjt', check=False)
            Traceback (most recent call last):
            ...
            ValueError: no internal state directions were given for non-identity
            starting permutation for Steinhaus-Johnson-Trotter algorithm
        """
    @cached_method
    def __hash__(self) -> int:
        """
        TESTS::

            sage: d = {}
            sage: p = Permutation([1,2,3])
            sage: d[p] = 1
            sage: d[p]
            1
        """
    def size(self) -> Integer:
        """
        Return the size of ``self``.

        EXAMPLES::

            sage: Permutation([3,4,1,2,5]).size()
            5
        """
    grade = size
    def order(self) -> Integer:
        """
        Return the order of ``self``.

        EXAMPLES::

            sage: sigma = Permutation([3,4,1,2,5])
            sage: sigma.order()
            2
            sage: sigma * sigma
            [1, 2, 3, 4, 5]
        """
    def cycle_string(self, singletons: bool = False) -> str:
        """
        Return a string of the permutation in cycle notation.

        If ``singletons=True``, it includes 1-cycles in the string.

        EXAMPLES::

            sage: Permutation([1,2,3]).cycle_string()
            '()'
            sage: Permutation([2,1,3]).cycle_string()
            '(1,2)'
            sage: Permutation([2,3,1]).cycle_string()
            '(1,2,3)'
            sage: Permutation([2,1,3]).cycle_string(singletons=True)
            '(1,2)(3)'
        """
    def __next__(self):
        """
        Return the permutation that follows ``self`` on the symmetric group
        containing ``self``. If ``self`` is the last permutation, then ``next``
        returns ``False``. If the ``algorithm`` parameter is specified, the
        permutations will be generated according to it. Supported algorithms
        are:

        - ``lex``: lexicographic order generation, this is the default
          algorithm.

        - ``sjt``: Steinhaus-Johnson-Trotter algorithm to generate
          permutations using only transposition of two elements in the list.
          It is highly recommended to set ``check=True`` (default value).

        EXAMPLES::

            sage: p = Permutation([1, 3, 2])
            sage: next(p)
            [2, 1, 3]
            sage: p = Permutation([4,3,2,1])
            sage: next(p)
            False
            sage: p = Permutation([1, 2, 3], algorithm='sjt')
            sage: p = next(p); p
            [1, 3, 2]
            sage: p = next(p); p
            [3, 1, 2]

        TESTS::

            sage: p = Permutation([])
            sage: next(p)
            False
            sage: p = Permutation([], algorithm='sjt')
            sage: next(p)
            False
            sage: p = Permutation([1], algorithm='sjt')
            sage: next(p)
            False
            sage: l = [1, 2, 3, 4]
            sage: s = set()
            sage: p = Permutation(l, algorithm='sjt')
            sage: for _ in range(factorial(len(l))):
            ....:     s.add(p)
            ....:     p = p.next()
            sage: p
            False
            sage: assert(len(s)) == factorial(len(l))
        """
    next = __next__
    def prev(self):
        """
        Return the permutation that comes directly before ``self`` in
        lexicographic order on the symmetric group containing ``self``.
        If ``self`` is the first permutation, then it returns ``False``.
        Does not support the Steinhaus-Johnson-Trotter algorithm for the moment.

        EXAMPLES::

            sage: p = Permutation([1,2,3])
            sage: p.prev()
            False
            sage: p = Permutation([1,3,2])
            sage: p.prev()
            [1, 2, 3]

        TESTS::

            sage: p = Permutation([])
            sage: p.prev()
            False

            sage: p = Permutation([1,2,3], algorithm='sjt')
            sage: p.prev()
            Traceback (most recent call last):
            ...
            NotImplementedError: previous permutation for SJT algorithm is not
            yet implemented

        Check that :issue:`16913` is fixed::

            sage: Permutation([1,4,3,2]).prev()
            [1, 4, 2, 3]

        .. TODO::

            Implement the previous permutation for the Steinhaus-Johnson-Trotter
            algorithm.
        """
    def to_tableau_by_shape(self, shape):
        """
        Return a tableau of shape ``shape`` with the entries in ``self``.

        The tableau is such that the reading word (i. e., the word
        obtained by reading the tableau row by row, starting from the
        top row in English notation, with each row being read from
        left to right) is ``self``.

        EXAMPLES::

            sage: T = Permutation([3,4,1,2,5]).to_tableau_by_shape([3,2]); T            # needs sage.combinat
            [[1, 2, 5], [3, 4]]
            sage: T.reading_word_permutation()                                          # needs sage.combinat
            [3, 4, 1, 2, 5]
        """
    def to_cycles(self, singletons: bool = True, use_min: bool = True) -> list:
        '''
        Return the permutation ``self`` as a list of disjoint cycles.

        The cycles are returned in the order of increasing smallest
        elements, and each cycle is returned as a tuple which starts
        with its smallest element.

        If ``singletons=False`` is given, the list does not contain the
        singleton cycles.

        If ``use_min=False`` is given, the cycles are returned in the
        order of increasing *largest* (not smallest) elements, and
        each cycle starts with its largest element.

        EXAMPLES::

            sage: Permutation([2,1,3,4]).to_cycles()
            [(1, 2), (3,), (4,)]
            sage: Permutation([2,1,3,4]).to_cycles(singletons=False)
            [(1, 2)]
            sage: Permutation([2,1,3,4]).to_cycles(use_min=True)
            [(1, 2), (3,), (4,)]
            sage: Permutation([2,1,3,4]).to_cycles(use_min=False)
            [(4,), (3,), (2, 1)]
            sage: Permutation([2,1,3,4]).to_cycles(singletons=False, use_min=False)
            [(2, 1)]

            sage: Permutation([4,1,5,2,6,3]).to_cycles()
            [(1, 4, 2), (3, 5, 6)]
            sage: Permutation([4,1,5,2,6,3]).to_cycles(use_min=False)
            [(6, 3, 5), (4, 2, 1)]

            sage: Permutation([6, 4, 5, 2, 3, 1]).to_cycles()
            [(1, 6), (2, 4), (3, 5)]
            sage: Permutation([6, 4, 5, 2, 3, 1]).to_cycles(use_min=False)
            [(6, 1), (5, 3), (4, 2)]

        The algorithm is of complexity `O(n)` where `n` is the size of the
        given permutation.

        TESTS::

            sage: from sage.combinat.permutation import from_cycles
            sage: for n in range(1,6):
            ....:    for p in Permutations(n):
            ....:       if from_cycles(n, p.to_cycles()) != p:
            ....:          print("There is a problem with {}".format(p))
            ....:          break
            sage: size = 10000
            sage: sample = (Permutations(size).random_element() for i in range(5))
            sage: all(from_cycles(size, p.to_cycles()) == p for p in sample)
            True

        Note: there is an alternative implementation called ``_to_cycle_set``
        which could be slightly (10%) faster for some input (typically for
        permutations of size in the range [100, 10000]). You can run the
        following benchmarks. For small permutations::

            sage: for size in range(9): # not tested
            ....:  print(size)
            ....:  lp = Permutations(size).list()
            ....:  timeit(\'[p.to_cycles(False) for p in lp]\')
            ....:  timeit(\'[p._to_cycles_set(False) for p in lp]\')
            ....:  timeit(\'[p._to_cycles_list(False) for p in lp]\')
            ....:  timeit(\'[p._to_cycles_orig(False) for p in lp]\')

        and larger ones::

            sage: for size in [10, 20, 50, 75, 100, 200, 500, 1000, # not tested
            ....:       2000, 5000, 10000, 15000, 20000, 30000,
            ....:       50000, 80000, 100000]:
            ....:    print(size)
            ....:    lp = [Permutations(size).random_element() for i in range(20)]
            ....:    timeit("[p.to_cycles() for p in lp]")
            ....:    timeit("[p._to_cycles_set() for p in lp]")
            ....:    timeit("[p._to_cycles_list() for p in lp]")
        '''
    cycle_tuples = to_cycles
    def to_permutation_group_element(self):
        """
        Return a PermutationGroupElement equal to ``self``.

        EXAMPLES::

            sage: Permutation([2,1,4,3]).to_permutation_group_element()                 # needs sage.groups
            (1,2)(3,4)
            sage: Permutation([1,2,3]).to_permutation_group_element()                   # needs sage.groups
            ()
        """
    def signature(self) -> Integer:
        """
        Return the signature of the permutation ``self``. This is
        `(-1)^l`, where `l` is the number of inversions of ``self``.

        .. NOTE::

            :meth:`sign` can be used as an alias for :meth:`signature`.

        EXAMPLES::

            sage: Permutation([4, 2, 3, 1, 5]).signature()
            -1
            sage: Permutation([1,3,2,5,4]).sign()
            1
            sage: Permutation([]).sign()
            1
        """
    sign = signature
    def is_even(self) -> bool:
        """
        Return ``True`` if the permutation ``self`` is even and
        ``False`` otherwise.

        EXAMPLES::

            sage: Permutation([1,2,3]).is_even()
            True
            sage: Permutation([2,1,3]).is_even()
            False
        """
    def to_matrix(self):
        """
        Return a matrix representing the permutation.

        EXAMPLES::

            sage: Permutation([1,2,3]).to_matrix()                                      # needs sage.modules
            [1 0 0]
            [0 1 0]
            [0 0 1]

        Alternatively::

            sage: matrix(Permutation([1,3,2]))                                          # needs sage.modules
            [1 0 0]
            [0 0 1]
            [0 1 0]

        Notice that matrix multiplication corresponds to permutation
        multiplication only when the permutation option mult='r2l'

        ::

            sage: Permutations.options.mult='r2l'
            sage: p = Permutation([2,1,3])
            sage: q = Permutation([3,1,2])
            sage: (p*q).to_matrix()                                                     # needs sage.modules
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: p.to_matrix()*q.to_matrix()                                           # needs sage.modules
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: Permutations.options.mult='l2r'
            sage: (p*q).to_matrix()                                                     # needs sage.modules
            [1 0 0]
            [0 0 1]
            [0 1 0]
        """
    def to_alternating_sign_matrix(self):
        """
        Return a matrix representing the permutation in the
        :class:`AlternatingSignMatrix` class.

        EXAMPLES::

            sage: m = Permutation([1,2,3]).to_alternating_sign_matrix(); m              # needs sage.combinat sage.modules
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: parent(m)                                                             # needs sage.combinat sage.modules
            Alternating sign matrices of size 3
        """
    def __mul__(self, rp):
        """
        TESTS::

            sage: # needs sage.groups sage.modules
            sage: SGA = SymmetricGroupAlgebra(QQ, 3)
            sage: SM = SGA.specht_module([2,1])
            sage: p213 = Permutations(3)([2,1,3])
            sage: p213 * SGA.an_element()
            3*[1, 2, 3] + [1, 3, 2] + [2, 1, 3] + 2*[3, 1, 2]
            sage: p213 * SM.an_element()
            2*S[[1, 2], [3]] - 4*S[[1, 3], [2]]
        """
    def __rmul__(self, lp):
        """
        TESTS::

            sage: p213 = Permutation([2,1,3])
            sage: p312 = Permutation([3,1,2])
            sage: Permutations.options.mult='l2r'
            sage: p213*p312
            [1, 3, 2]
            sage: Permutations.options.mult='r2l'
            sage: p213*p312
            [3, 2, 1]
            sage: Permutations.options.mult='l2r'

            sage: SGA = SymmetricGroupAlgebra(QQ, 3)                                    # needs sage.groups sage.modules
            sage: SGA.an_element() * Permutations(3)(p213)                              # needs sage.groups sage.modules
            3*[1, 2, 3] + [2, 1, 3] + 2*[2, 3, 1] + [3, 2, 1]
        """
    def left_action_product(self, lp):
        """
        Return the permutation obtained by composing ``self`` with
        ``lp`` in such an order that ``lp`` is applied first and
        ``self`` is applied afterwards.

        This is usually denoted by either ``self * lp`` or ``lp * self``
        depending on the conventions used by the author. If the value
        of a permutation `p \\in S_n` on an integer
        `i \\in \\{ 1, 2, \\cdots, n \\}` is denoted by `p(i)`, then this
        should be denoted by ``self * lp`` in order to have
        associativity (i.e., in order to have
        `(p \\cdot q)(i) = p(q(i))` for all `p`, `q` and `i`). If, on
        the other hand, the value of a permutation `p \\in S_n` on an
        integer `i \\in \\{ 1, 2, \\cdots, n \\}` is denoted by `i^p`, then
        this should be denoted by ``lp * self`` in order to have
        associativity (i.e., in order to have
        `i^{p \\cdot q} = (i^p)^q` for all `p`, `q` and `i`).

        EXAMPLES::

            sage: p = Permutation([2,1,3])
            sage: q = Permutation([3,1,2])
            sage: p.left_action_product(q)
            [3, 2, 1]
            sage: q.left_action_product(p)
            [1, 3, 2]
        """
    def right_action_product(self, rp):
        """
        Return the permutation obtained by composing ``self`` with
        ``rp`` in such an order that ``self`` is applied first and
        ``rp`` is applied afterwards.

        This is usually denoted by either ``self * rp`` or ``rp * self``
        depending on the conventions used by the author. If the value
        of a permutation `p \\in S_n` on an integer
        `i \\in \\{ 1, 2, \\cdots, n \\}` is denoted by `p(i)`, then this
        should be denoted by ``rp * self`` in order to have
        associativity (i.e., in order to have
        `(p \\cdot q)(i) = p(q(i))` for all `p`, `q` and `i`). If, on
        the other hand, the value of a permutation `p \\in S_n` on an
        integer `i \\in \\{ 1, 2, \\cdots, n \\}` is denoted by `i^p`, then
        this should be denoted by ``self * rp`` in order to have
        associativity (i.e., in order to have
        `i^{p \\cdot q} = (i^p)^q` for all `p`, `q` and `i`).

        EXAMPLES::

            sage: p = Permutation([2,1,3])
            sage: q = Permutation([3,1,2])
            sage: p.right_action_product(q)
            [1, 3, 2]
            sage: q.right_action_product(p)
            [3, 2, 1]
        """
    def __call__(self, i):
        """
        Return the image of the integer `i` under ``self``.

        EXAMPLES::

            sage: p = Permutation([2, 1, 4, 5, 3])
            sage: p(1)
            2
            sage: p = Permutation(((1,2),(4,3,5)))
            sage: p(4)
            3
            sage: p(2)
            1
            sage: p = Permutation([5,2,1,6,3,7,4])
            sage: list(map(p, range(1,8)))
            [5, 2, 1, 6, 3, 7, 4]

        TESTS::

            sage: p = Permutation([5,2,1,6,3,7,4])
            sage: p(-1)
            Traceback (most recent call last):
            ...
            TypeError: i (= -1) must be between 1 and 7
            sage: p(10)
            Traceback (most recent call last):
            ...
            TypeError: i (= 10) must be between 1 and 7
        """
    def rank(self) -> Integer:
        """
        Return the rank of ``self`` in the lexicographic ordering on the
        symmetric group to which ``self`` belongs.

        EXAMPLES::

            sage: Permutation([1,2,3]).rank()
            0
            sage: Permutation([1, 2, 4, 6, 3, 5]).rank()
            10
            sage: perms = Permutations(6).list()
            sage: [p.rank() for p in perms] == list(range(factorial(6)))
            True
        """
    def to_inversion_vector(self) -> list:
        """
        Return the inversion vector of ``self``.

        The inversion vector of a permutation `p \\in S_n` is defined as
        the vector `(v_1, v_2, \\ldots, v_n)`, where `v_i` is the
        number of elements larger than `i` that appear to the left
        of `i` in the permutation `p`.

        The algorithm is of complexity `O(n\\log(n))` where `n` is the size of
        the given permutation.

        EXAMPLES::

            sage: Permutation([5,9,1,8,2,6,4,7,3]).to_inversion_vector()
            [2, 3, 6, 4, 0, 2, 2, 1, 0]
            sage: Permutation([8,7,2,1,9,4,6,5,10,3]).to_inversion_vector()
            [3, 2, 7, 3, 4, 3, 1, 0, 0, 0]
            sage: Permutation([3,2,4,1,5]).to_inversion_vector()
            [3, 1, 0, 0, 0]

        TESTS::

            sage: from sage.combinat.permutation import from_inversion_vector
            sage: all(from_inversion_vector(p.to_inversion_vector()) == p
            ....:   for n in range(6) for p in Permutations(n))
            True

            sage: P = Permutations(1000)
            sage: sample = (P.random_element() for i in range(5))
            sage: all(from_inversion_vector(p.to_inversion_vector()) == p
            ....:   for p in sample)
            True
        """
    def inversions(self) -> list:
        """
        Return a list of the inversions of ``self``.

        An inversion of a permutation `p` is a pair `(i, j)` such that
        `i < j` and `p(i) > p(j)`.

        EXAMPLES::

            sage: Permutation([3,2,4,1,5]).inversions()
            [(1, 2), (1, 4), (2, 4), (3, 4)]
        """
    def stack_sort(self) -> Permutation:
        """
        Return the stack sort of a permutation.

        This is another permutation obtained through the
        process of sorting using one stack. If the result is the identity
        permutation, the original permutation is *stack-sortable*.

        See :wikipedia:`Stack-sortable_permutation`

        EXAMPLES::

            sage: p = Permutation([2,1,5,3,4,9,7,8,6])
            sage: p.stack_sort()
            [1, 2, 3, 4, 5, 7, 6, 8, 9]

            sage: S5 = Permutations(5)
            sage: len([1 for s in S5 if s.stack_sort() == S5.one()])
            42

        TESTS::

            sage: p = Permutation([])
            sage: p.stack_sort()
            []
            sage: p = Permutation([1])
            sage: p.stack_sort()
            [1]
        """
    def to_digraph(self) -> DiGraph:
        """
        Return a digraph representation of ``self``.

        EXAMPLES::

            sage: d = Permutation([3, 1, 2]).to_digraph()                               # needs sage.graphs
            sage: d.edges(sort=True, labels=False)                                      # needs sage.graphs
            [(1, 3), (2, 1), (3, 2)]
            sage: P = Permutations(range(1, 10))
            sage: d = Permutation(P.random_element()).to_digraph()                      # needs sage.graphs
            sage: all(c.is_cycle()                                                      # needs sage.graphs
            ....:     for c in d.strongly_connected_components_subgraphs())
            True

        TESTS::

            sage: d = Permutation([1]).to_digraph()                                     # needs sage.graphs
            sage: d.edges(sort=True, labels=False)                                      # needs sage.graphs
            [(1, 1)]
        """
    def show(self, representation: str = 'cycles', orientation: str = 'landscape', **args):
        '''
        Display the permutation as a drawing.

        INPUT:

        - ``representation`` -- different kinds of drawings are available

          - ``\'cycles\'`` -- default; the permutation is displayed as a
            collection of directed cycles

          - ``\'braid\'`` -- the permutation is displayed as segments linking
            each element `1, ..., n` to its image on a parallel line

            When using this drawing, it is also possible to display the
            permutation horizontally (``orientation = "landscape"``, default
            option) or vertically (``orientation = "portrait"``).

          - ``\'chord-diagram\'`` -- the permutation is displayed as a directed
            graph, all of its vertices being located on a circle

        All additional arguments are forwarded to the ``show`` subcalls.

        EXAMPLES::

            sage: P20 = Permutations(20)
            sage: P20.random_element().show(representation=\'cycles\')                    # needs sage.graphs sage.plot
            sage: P20.random_element().show(representation=\'chord-diagram\')             # needs sage.graphs sage.plot
            sage: P20.random_element().show(representation=\'braid\')                     # needs sage.plot
            sage: P20.random_element().show(representation=\'braid\',                     # needs sage.plot
            ....:                           orientation=\'portrait\')

        TESTS::

            sage: P20.random_element().show(representation=\'modern_art\')
            Traceback (most recent call last):
            ...
            ValueError: The value of \'representation\' must be equal to \'cycles\', \'chord-diagram\' or \'braid\'
        '''
    def number_of_inversions(self) -> Integer:
        """
        Return the number of inversions in ``self``.

        An inversion of a permutation is a pair of elements `(i, j)`
        with `i < j` and `p(i) > p(j)`.

        REFERENCES:

        - http://mathworld.wolfram.com/PermutationInversion.html

        EXAMPLES::

            sage: Permutation([3, 2, 4, 1, 5]).number_of_inversions()
            4
            sage: Permutation([1, 2, 6, 4, 7, 3, 5]).number_of_inversions()
            6
        """
    def noninversions(self, k) -> list[list]:
        """
        Return the list of all ``k``-noninversions in ``self``.

        If `k` is an integer and `p \\in S_n` is a permutation, then
        a `k`-noninversion in `p` is defined as a strictly increasing
        sequence `(i_1, i_2, \\ldots, i_k)` of elements of
        `\\{ 1, 2, \\ldots, n \\}` satisfying
        `p(i_1) < p(i_2) < \\cdots < p(i_k)`. (In other words, a
        `k`-noninversion in `p` can be regarded as a `k`-element
        subset of `\\{ 1, 2, \\ldots, n \\}` on which `p` restricts
        to an increasing map.)

        EXAMPLES::

            sage: p = Permutation([3, 2, 4, 1, 5])
            sage: p.noninversions(1)
            [[3], [2], [4], [1], [5]]
            sage: p.noninversions(2)
            [[3, 4], [3, 5], [2, 4], [2, 5], [4, 5], [1, 5]]
            sage: p.noninversions(3)
            [[3, 4, 5], [2, 4, 5]]
            sage: p.noninversions(4)
            []
            sage: p.noninversions(5)
            []

        TESTS::

            sage: q = Permutation([])
            sage: q.noninversions(1)
            []
        """
    def number_of_noninversions(self, k) -> Integer:
        """
        Return the number of ``k``-noninversions in ``self``.

        If `k` is an integer and `p \\in S_n` is a permutation, then
        a `k`-noninversion in `p` is defined as a strictly increasing
        sequence `(i_1, i_2, \\ldots, i_k)` of elements of
        `\\{ 1, 2, \\ldots, n \\}` satisfying
        `p(i_1) < p(i_2) < \\cdots < p(i_k)`. (In other words, a
        `k`-noninversion in `p` can be regarded as a `k`-element
        subset of `\\{ 1, 2, \\ldots, n \\}` on which `p` restricts
        to an increasing map.)

        The number of `k`-noninversions in `p` has been denoted by
        `\\mathrm{noninv}_k(p)` in [RSW2011]_, where conjectures
        and results regarding this number have been stated.

        EXAMPLES::

            sage: p = Permutation([3, 2, 4, 1, 5])
            sage: p.number_of_noninversions(1)
            5
            sage: p.number_of_noninversions(2)
            6
            sage: p.number_of_noninversions(3)
            2
            sage: p.number_of_noninversions(4)
            0
            sage: p.number_of_noninversions(5)
            0

        The number of `2`-noninversions of a permutation `p \\in S_n`
        is `\\binom{n}{2}` minus its number of inversions::

            sage: b = binomial(5, 2)                                                    # needs sage.symbolic
            sage: all( x.number_of_noninversions(2) == b - x.number_of_inversions()     # needs sage.symbolic
            ....:      for x in Permutations(5) )
            True

        We also check some corner cases::

            sage: all( x.number_of_noninversions(1) == 5 for x in Permutations(5) )
            True
            sage: all( x.number_of_noninversions(0) == 1 for x in Permutations(5) )
            True
            sage: Permutation([]).number_of_noninversions(1)
            0
            sage: Permutation([]).number_of_noninversions(0)
            1
            sage: Permutation([2, 1]).number_of_noninversions(3)
            0
        """
    def length(self) -> Integer:
        """
        Return the Coxeter length of ``self``.

        The length of a permutation `p` is given by the number of inversions
        of `p`.

        EXAMPLES::

            sage: Permutation([5, 1, 3, 4, 2]).length()
            6
        """
    def absolute_length(self) -> Integer:
        """
        Return the absolute length of ``self``

        The absolute length is the length of the shortest expression
        of the element as a product of reflections.

        For permutations in the symmetric groups, the absolute
        length is the size minus the number of its disjoint
        cycles.

        EXAMPLES::

            sage: Permutation([4,2,3,1]).absolute_length()                              # needs sage.combinat
            1
        """
    def inverse(self) -> Permutation:
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: Permutation([3,8,5,10,9,4,6,1,7,2]).inverse()
            [8, 10, 1, 6, 3, 7, 9, 2, 5, 4]
            sage: Permutation([2, 4, 1, 5, 3]).inverse()
            [3, 1, 5, 2, 4]
            sage: ~Permutation([2, 4, 1, 5, 3])
            [3, 1, 5, 2, 4]
        """
    __invert__ = inverse
    def ishift(self, i):
        """
        Return the ``i``-shift of ``self``. If an ``i``-shift of ``self``
        can't be performed, then ``self`` is returned.

        An `i`-shift can be applied when `i` is not inbetween `i-1` and
        `i+1`. The `i`-shift moves `i` to the other side, and leaves the
        relative positions of `i-1` and `i+1` in place. All other entries
        of the permutations are also left in place.

        EXAMPLES:

        Here, `2` is to the left of both `1` and `3`. A `2`-shift
        can be applied which moves the `2` to the right and leaves `1` and
        `3` in their same relative order::

            sage: Permutation([2,1,3]).ishift(2)
            [1, 3, 2]

        All entries other than `i`, `i-1` and `i+1` are unchanged::

            sage: Permutation([2,4,1,3]).ishift(2)
            [1, 4, 3, 2]

        Since `2` is between `1` and `3` in ``[1,2,3]``, a `2`-shift cannot
        be applied to ``[1,2,3]`` ::

            sage: Permutation([1,2,3]).ishift(2)
            [1, 2, 3]
        """
    def iswitch(self, i):
        """
        Return the ``i``-switch of ``self``. If an ``i``-switch of ``self``
        can't be performed, then ``self`` is returned.

        An `i`-switch can be applied when the subsequence of ``self`` formed
        by the entries `i-1`, `i` and `i+1` is neither increasing nor
        decreasing. In this case, this subsequence is reversed (i. e., its
        leftmost element and its rightmost element switch places), while all
        other letters of ``self`` are kept in place.

        EXAMPLES:

        Here, `2` is to the left of both `1` and `3`. A `2`-switch can be
        applied which moves the `2` to the right and switches the relative
        order between `1` and `3`::

            sage: Permutation([2,1,3]).iswitch(2)
            [3, 1, 2]

        All entries other than `i-1`, `i` and `i+1` are unchanged::

            sage: Permutation([2,4,1,3]).iswitch(2)
            [3, 4, 1, 2]

        Since `2` is between `1` and `3` in ``[1,2,3]``, a `2`-switch
        cannot be applied to ``[1,2,3]`` ::

            sage: Permutation([1,2,3]).iswitch(2)
            [1, 2, 3]
        """
    def runs(self, as_tuple: bool = False) -> list | tuple:
        """
        Return a list of the runs in the nonempty permutation
        ``self``.

        A run in a permutation is defined to be a maximal (with
        respect to inclusion) nonempty increasing substring (i. e.,
        contiguous subsequence). For instance, the runs in the
        permutation ``[6,1,7,3,4,5,2]`` are ``[6]``, ``[1,7]``,
        ``[3,4,5]`` and ``[2]``.

        Runs in an empty permutation are not defined.

        INPUT:

        - ``as_tuple`` -- boolean (default: ``False``); choice of
          output format

        OUTPUT: list of lists or a tuple of tuples

        REFERENCES:

        - http://mathworld.wolfram.com/PermutationRun.html

        EXAMPLES::

            sage: Permutation([1,2,3,4]).runs()
            [[1, 2, 3, 4]]
            sage: Permutation([4,3,2,1]).runs()
            [[4], [3], [2], [1]]
            sage: Permutation([2,4,1,3]).runs()
            [[2, 4], [1, 3]]
            sage: Permutation([1]).runs()
            [[1]]

        The example from above::

            sage: Permutation([6,1,7,3,4,5,2]).runs()
            [[6], [1, 7], [3, 4, 5], [2]]
            sage: Permutation([6,1,7,3,4,5,2]).runs(as_tuple=True)
            ((6,), (1, 7), (3, 4, 5), (2,))

        The number of runs in a nonempty permutation equals its
        number of descents plus 1::

            sage: all( len(p.runs()) == p.number_of_descents() + 1
            ....:      for p in Permutations(6) )
            True
        """
    def decreasing_runs(self, as_tuple: bool = False) -> list | tuple:
        """
        Decreasing runs of the permutation.

        INPUT:

        - ``as_tuple`` -- boolean (default: ``False``); choice of output
          format

        OUTPUT: list of lists or a tuple of tuples

        .. SEEALSO::

            :meth:`runs`

        EXAMPLES::

            sage: s = Permutation([2,8,3,9,6,4,5,1,7])
            sage: s.decreasing_runs()
            [[2], [8, 3], [9, 6, 4], [5, 1], [7]]
            sage: s.decreasing_runs(as_tuple=True)
            ((2,), (8, 3), (9, 6, 4), (5, 1), (7,))
        """
    def longest_increasing_subsequence_length(self) -> Integer:
        """
        Return the length of the longest increasing subsequences of ``self``.

        EXAMPLES::

            sage: Permutation([2,3,1,4]).longest_increasing_subsequence_length()
            3
            sage: all(i.longest_increasing_subsequence_length() == len(RSK(i)[0][0])    # needs sage.combinat
            ....:     for i in Permutations(5))
            True
            sage: Permutation([]).longest_increasing_subsequence_length()
            0
        """
    def longest_increasing_subsequences(self) -> list:
        """
        Return the list of the longest increasing subsequences of ``self``.

        A theorem of Schensted ([Sch1961]_) states that an increasing
        subsequence of length `i` ends with the value entered in the `i`-th
        column of the p-tableau. The algorithm records which column of the
        p-tableau each value of the permutation is entered into, creates a
        digraph to record all increasing subsequences, and reads the paths
        from a source to a sink; these are the longest increasing subsequences.

        EXAMPLES::

            sage: Permutation([2,3,4,1]).longest_increasing_subsequences()              # needs sage.graphs
            [[2, 3, 4]]
            sage: Permutation([5, 7, 1, 2, 6, 4, 3]).longest_increasing_subsequences()  # needs sage.graphs
            [[1, 2, 6], [1, 2, 4], [1, 2, 3]]

        .. NOTE::

            This algorithm could be made faster using a balanced search tree
            for each column instead of sorted lists. See discussion on
            :issue:`31451`.
        """
    def longest_increasing_subsequences_number(self):
        """
        Return the number of increasing subsequences of maximal length
        in ``self``.

        The list of longest increasing subsequences of a permutation is
        given by :meth:`longest_increasing_subsequences`, and the
        length of these subsequences is given by
        :meth:`longest_increasing_subsequence_length`.

        The algorithm is similar to :meth:`longest_increasing_subsequences`.
        Namely, the longest increasing subsequences are encoded as increasing
        sequences in a ranked poset from a smallest to a largest element. Their
        number can be obtained via dynamic programming: for each `v` in the poset
        we compute the number of paths from a smallest element to `v`.

        EXAMPLES::

            sage: sum(p.longest_increasing_subsequences_number()
            ....:     for p in Permutations(8))
            120770

            sage: p = Permutations(50).random_element()
            sage: (len(p.longest_increasing_subsequences()) ==                          # needs sage.graphs
            ....:  p.longest_increasing_subsequences_number())
            True
        """
    def cycle_type(self):
        """
        Return a partition of ``len(self)`` corresponding to the cycle
        type of ``self``.

        This is a non-increasing sequence of the cycle lengths of ``self``.

        EXAMPLES::

            sage: Permutation([3,1,2,4]).cycle_type()                                   # needs sage.combinat
            [3, 1]
        """
    def forget_cycles(self):
        """
        Return the image of ``self`` under the map which forgets cycles.

        Consider a permutation `\\sigma` written in standard cyclic form:

        .. MATH::

            \\sigma
            = (a_{1,1}, \\ldots, a_{1,k_1})
              (a_{2,1}, \\ldots, a_{2,k_2})
              \\cdots
              (a_{m,1}, \\ldots, a_{m,k_m}),

        where `a_{1,1} < a_{2,1} < \\cdots < a_{m,1}` and `a_{j,1} < a_{j,i}`
        for all `1 \\leq j \\leq m` and `2 \\leq i \\leq k_j` where we include
        cycles of length 1 as well. The image of the forget cycle map `\\phi`
        is given by

        .. MATH::

            \\phi(\\sigma) = [a_{1,1}, \\ldots, a_{1,k_1}, a_{2,1}, \\ldots,
            a_{2,k_2}, \\ldots, a_{m,1}, \\ldots, a_{m,k_m}],

        considered as a permutation in 1-line notation.

        .. SEEALSO::

            :meth:`fundamental_transformation`, which is a similar map that
            is defined by instead taking `a_{j,1} > a_{j,i}` and is
            bijective.

        EXAMPLES::

            sage: P = Permutations(5)
            sage: x = P([1, 5, 3, 4, 2])
            sage: x.forget_cycles()
            [1, 2, 5, 3, 4]

        We select all permutations with a cycle composition of `[2, 3, 1]`
        in `S_6`::

            sage: P = Permutations(6)
            sage: l = [p for p in P if [len(t) for t in p.to_cycles()] == [1,3,2]]

        Next we apply `\\phi` and then take the inverse, and then view the
        results as a poset under the Bruhat order::

            sage: l = [p.forget_cycles().inverse() for p in l]
            sage: B = Poset([l, lambda x,y: x.bruhat_lequal(y)])                        # needs sage.combinat sage.graphs
            sage: R.<q> = QQ[]
            sage: sum(q^B.rank_function()(x) for x in B)                                # needs sage.combinat sage.graphs
            q^5 + 2*q^4 + 3*q^3 + 3*q^2 + 2*q + 1

        We check the statement in [CC2013]_ that the posets
        `C_{[1,3,1,1]}` and `C_{[1,3,2]}` are isomorphic::

            sage: l2 = [p for p in P if [len(t) for t in p.to_cycles()] == [1,3,1,1]]
            sage: l2 = [p.forget_cycles().inverse() for p in l2]
            sage: B2 = Poset([l2, lambda x,y: x.bruhat_lequal(y)])                      # needs sage.combinat sage.graphs
            sage: B.is_isomorphic(B2)                                                   # needs sage.combinat sage.graphs
            True

        .. SEEALSO::

            :meth:`fundamental_transformation`.
        """
    def foata_bijection(self) -> Permutation:
        """
        Return the image of the permutation ``self`` under the Foata
        bijection `\\phi`.

        The bijection shows that `\\mathrm{maj}` (the major index)
        and `\\mathrm{inv}` (the number of inversions) are
        equidistributed: if `\\phi(P) = Q`, then `\\mathrm{maj}(P) =
        \\mathrm{inv}(Q)`.

        The Foata bijection `\\phi` is a bijection on the set of words with
        no two equal letters. It can be defined by induction on the size
        of the word: Given a word `w_1 w_2 \\cdots w_n`, start with
        `\\phi(w_1) = w_1`. At the `i`-th step, if
        `\\phi(w_1 w_2 \\cdots w_i) = v_1 v_2 \\cdots v_i`, we define
        `\\phi(w_1 w_2 \\cdots w_i w_{i+1})` by placing `w_{i+1}` on the end of
        the word `v_1 v_2 \\cdots v_i` and breaking the word up into blocks
        as follows. If `w_{i+1} > v_i`, place a vertical line to the right
        of each `v_k` for which `w_{i+1} > v_k`. Otherwise, if
        `w_{i+1} < v_i`, place a vertical line to the right of each `v_k`
        for which `w_{i+1} < v_k`. In either case, place a vertical line at
        the start of the word as well. Now, within each block between
        vertical lines, cyclically shift the entries one place to the
        right.

        For instance, to compute `\\phi([1,4,2,5,3])`, the sequence of
        words is

        * `1`,
        * `|1|4 \\to 14`,
        * `|14|2 \\to 412`,
        * `|4|1|2|5 \\to 4125`,
        * `|4|125|3 \\to 45123`.

        So `\\phi([1,4,2,5,3]) = [4,5,1,2,3]`.

        See section 2 of [FS1978]_, and the proof of Proposition 1.4.6
        in [EnumComb1]_.

        .. SEEALSO::

            :meth:`foata_bijection_inverse` for the inverse map.

        EXAMPLES::

            sage: Permutation([1,2,4,3]).foata_bijection()
            [4, 1, 2, 3]
            sage: Permutation([2,5,1,3,4]).foata_bijection()
            [2, 1, 3, 5, 4]

            sage: P = Permutation([2,5,1,3,4])
            sage: P.major_index() == P.foata_bijection().number_of_inversions()
            True

            sage: all( P.major_index() == P.foata_bijection().number_of_inversions()
            ....:      for P in Permutations(4) )
            True

        The example from [FS1978]_::

            sage: Permutation([7,4,9,2,6,1,5,8,3]).foata_bijection()
            [4, 7, 2, 6, 1, 9, 5, 8, 3]

        Border cases::

            sage: Permutation([]).foata_bijection()
            []
            sage: Permutation([1]).foata_bijection()
            [1]
        """
    def foata_bijection_inverse(self) -> Permutation:
        """
        Return the image of the permutation ``self`` under the inverse
        of the Foata bijection `\\phi`.

        See :meth:`foata_bijection` for the definition of the Foata
        bijection.

        EXAMPLES::

            sage: Permutation([4, 1, 2, 3]).foata_bijection()
            [1, 2, 4, 3]

        TESTS::

            sage: all( P.foata_bijection().foata_bijection_inverse() == P
            ....:      for P in Permutations(5) )
            True

        Border cases::

            sage: Permutation([]).foata_bijection_inverse()
            []
            sage: Permutation([1]).foata_bijection_inverse()
            [1]
        """
    def fundamental_transformation(self) -> Permutation:
        """
        Return the image of the permutation ``self`` under the
        Renyi-Foata-Schuetzenberger fundamental transformation.

        The fundamental transformation is a bijection from the
        set of all permutations of `\\{1, 2, \\ldots, n\\}` to
        itself, which transforms any such permutation `w`
        as follows:
        Write `w` in cycle form, with each cycle starting with
        its highest element, and the cycles being sorted in
        increasing order of their highest elements.
        Drop the parentheses in the resulting expression, thus
        reading it as a one-line notation of a new permutation
        `u`.
        Then, `u` is the image of `w` under the fundamental
        transformation.

        See [EnumComb1]_, Proposition 1.3.1.

        .. SEEALSO::

            :meth:`fundamental_transformation_inverse`
            for the inverse map.

            :meth:`forget_cycles` for a similar (but non-bijective)
            map where each cycle is starting from its lowest element.

        EXAMPLES::

            sage: Permutation([5, 1, 3, 4, 2]).fundamental_transformation()
            [3, 4, 5, 2, 1]
            sage: Permutations(5)([1, 5, 3, 4, 2]).fundamental_transformation()
            [1, 3, 4, 5, 2]
            sage: Permutation([8, 4, 7, 2, 9, 6, 5, 1, 3]).fundamental_transformation()
            [4, 2, 6, 8, 1, 9, 3, 7, 5]

        Comparison with :meth:`forget_cycles`::

            sage: P = Permutation([(1,3,4),(2,5)])
            sage: P
            [3, 5, 4, 1, 2]
            sage: P.forget_cycles()
            [1, 3, 4, 2, 5]
            sage: P.fundamental_transformation()
            [4, 1, 3, 5, 2]

        TESTS:

        Border cases::

            sage: Permutation([]).fundamental_transformation()
            []
            sage: Permutation([1]).fundamental_transformation()
            [1]
        """
    def fundamental_transformation_inverse(self):
        """
        Return the image of the permutation ``self`` under the
        inverse of the Renyi-Foata-Schuetzenberger fundamental
        transformation.

        The inverse of the fundamental transformation is a
        bijection from the set of all permutations of
        `\\{1, 2, \\ldots, n\\}` to itself, which transforms any
        such permutation `w` as follows:
        Let `I = \\{ i_1 < i_2 < \\cdots < i_k \\}` be the set of
        all left-to-right maxima of `w` (that is, of all indices
        `j` such that `w(j)` is bigger than each of
        `w(1), w(2), \\ldots, w(j-1)`).
        The image of `w` under the inverse of the fundamental
        transformation is the permutation `u` that sends
        `w(i-1)` to `w(i)` for all `i \\notin I` (notice that
        this makes sense, since `1 \\in I` whenever `n > 0`),
        while sending each `w(i_p - 1)` (with `p \\geq 2`)
        to `w(i_{p-1})`. Here, we set `i_{k+1} = n+1`.

        See [EnumComb1]_, Proposition 1.3.1.

        .. SEEALSO::

            :meth:`fundamental_transformation`
            for the inverse map.

        EXAMPLES::

            sage: Permutation([3, 4, 5, 2, 1]).fundamental_transformation_inverse()
            [5, 1, 3, 4, 2]
            sage: Permutation([4, 2, 6, 8, 1, 9, 3, 7, 5]).fundamental_transformation_inverse()
            [8, 4, 7, 2, 9, 6, 5, 1, 3]

        TESTS::

            sage: all(P.fundamental_transformation_inverse().
            ....:     fundamental_transformation() == P
            ....:     for P in Permutations(4))
            True

            sage: all(P.fundamental_transformation().
            ....:     fundamental_transformation_inverse() == P
            ....:     for P in Permutations(3))
            True

        Border cases::

            sage: Permutation([]).fundamental_transformation_inverse()
            []
            sage: Permutation([1]).fundamental_transformation_inverse()
            [1]
        """
    def destandardize(self, weight, ordered_alphabet=None):
        """
        Return destandardization of ``self`` with respect to ``weight`` and
        ``ordered_alphabet``.

        INPUT:

        - ``weight`` -- list or tuple of nonnegative integers that sum to `n`
          if ``self`` is a permutation in `S_n`

        - ``ordered_alphabet`` -- (default: ``None``) a list or tuple
          specifying the ordered alphabet the destandardized word is over

        OUTPUT: word over the ``ordered_alphabet`` which standardizes to ``self``

        Let `weight = (w_1,w_2,\\ldots,w_\\ell)`. Then this methods looks for an increasing
        sequence of `1,2,\\ldots, w_1` and labels all letters in it by 1, then an increasing
        sequence of `w_1+1,w_1+2,\\ldots,w_1+w_2` and labels all these letters by 2, etc..
        If an increasing sequence for the specified ``weight`` does not exist, an error is
        returned. The output is a word ``w`` over the specified ordered alphabet with
        evaluation ``weight`` such that ``w.standard_permutation()`` is ``self``.

        EXAMPLES::

            sage: p = Permutation([1,2,5,3,6,4])
            sage: p.destandardize([3,1,2])                                              # needs sage.combinat
            word: 113132
            sage: p = Permutation([2,1,3])
            sage: p.destandardize([2,1])
            Traceback (most recent call last):
            ...
            ValueError: Standardization with weight [2, 1] is not possible!

        TESTS::

            sage: p = Permutation([4,1,2,3,5,6])
            sage: p.destandardize([2,1,3], ordered_alphabet = [1,'a',3])                # needs sage.combinat
            word: 311a33
            sage: p.destandardize([2,1,3], ordered_alphabet = [1,'a'])
            Traceback (most recent call last):
            ...
            ValueError: Not enough letters in the alphabet are specified compared to the weight
        """
    def to_lehmer_code(self) -> list:
        """
        Return the Lehmer code of the permutation ``self``.

        The Lehmer code of a permutation `p` is defined as the
        list `[c[1],c[2],...,c[n]]`, where `c[i]` is the number of
        `j>i` such that `p(j)<p(i)`.

        EXAMPLES::

            sage: p = Permutation([2,1,3])
            sage: p.to_lehmer_code()
            [1, 0, 0]
            sage: q = Permutation([3,1,2])
            sage: q.to_lehmer_code()
            [2, 0, 0]

            sage: Permutation([1]).to_lehmer_code()
            [0]
            sage: Permutation([]).to_lehmer_code()
            []

        TESTS::

            sage: from sage.combinat.permutation import from_lehmer_code
            sage: all(from_lehmer_code(p.to_lehmer_code()) == p
            ....:   for n in range(6) for p in Permutations(n))
            True

            sage: P = Permutations(1000)
            sage: sample = (P.random_element() for i in range(5))
            sage: all(from_lehmer_code(p.to_lehmer_code()) == p
            ....:   for p in sample)
            True
        """
    def to_lehmer_cocode(self) -> list[int]:
        """
        Return the Lehmer cocode of the permutation ``self``.

        The Lehmer cocode of a permutation `p` is defined as the
        list `(c_1, c_2, \\ldots, c_n)`, where `c_i` is the number
        of `j < i` such that `p(j) > p(i)`.

        EXAMPLES::

            sage: p = Permutation([2,1,3])
            sage: p.to_lehmer_cocode()
            [0, 1, 0]
            sage: q = Permutation([3,1,2])
            sage: q.to_lehmer_cocode()
            [0, 1, 1]
        """
    def reduced_word(self) -> list[int]:
        """
        Return a reduced word of the permutation ``self``.

        See :meth:`reduced_words` for the definition of reduced words and
        a way to compute them all.

        .. WARNING::

            This does not respect the multiplication convention.

        EXAMPLES::

            sage: Permutation([3,5,4,6,2,1]).reduced_word()
            [2, 1, 4, 3, 2, 4, 3, 5, 4, 5]

            Permutation([1]).reduced_word_lexmin()
            []
            Permutation([]).reduced_word_lexmin()
            []
        """
    def reduced_words_iterator(self) -> Iterator:
        """
        Return an iterator for the reduced words of ``self``.

        EXAMPLES::

            sage: next(Permutation([5,2,3,4,1]).reduced_words_iterator())
            [1, 2, 3, 4, 3, 2, 1]
        """
    def reduced_words(self) -> list:
        """
        Return a list of the reduced words of ``self``.

        The notion of a reduced word is based on the well-known fact
        that every permutation can be written as a product of adjacent
        transpositions. In more detail: If `n` is a nonnegative integer,
        we can define the transpositions `s_i = (i, i+1) \\in S_n`
        for all `i \\in \\{ 1, 2, \\ldots, n-1 \\}`, and every `p \\in S_n`
        can then be written as a product `s_{i_1} s_{i_2} \\cdots s_{i_k}`
        for some sequence `(i_1, i_2, \\ldots, i_k)` of elements of
        `\\{ 1, 2, \\ldots, n-1 \\}` (here `\\{ 1, 2, \\ldots, n-1 \\}` denotes
        the empty set when `n \\leq 1`). Fixing a `p`, the sequences
        `(i_1, i_2, \\ldots, i_k)` of smallest length satisfying
        `p = s_{i_1} s_{i_2} \\cdots s_{i_k}` are called the reduced words
        of `p`. (Their length is the Coxeter length of `p`, and can be
        computed using :meth:`length`.)

        Note that the product of permutations is defined here in such
        a way that `(pq)(i) = p(q(i))` for all permutations `p` and `q`
        and each `i \\in \\{ 1, 2, \\ldots, n \\}` (this is the same
        convention as in :meth:`left_action_product`, but not the
        default semantics of the `*` operator on permutations in Sage).
        Thus, for instance, `s_2 s_1` is the permutation obtained by
        first transposing `1` with `2` and then transposing `2` with `3`.

        .. SEEALSO::

            :meth:`reduced_word`, :meth:`reduced_word_lexmin`

        EXAMPLES::

            sage: Permutation([2,1,3]).reduced_words()
            [[1]]
            sage: Permutation([3,1,2]).reduced_words()
            [[2, 1]]
            sage: Permutation([3,2,1]).reduced_words()
            [[1, 2, 1], [2, 1, 2]]
            sage: Permutation([3,2,4,1]).reduced_words()
            [[1, 2, 3, 1], [1, 2, 1, 3], [2, 1, 2, 3]]

            Permutation([1]).reduced_words()
            [[]]
            Permutation([]).reduced_words()
            [[]]
        """
    def reduced_word_lexmin(self) -> list[int]:
        """
        Return a lexicographically minimal reduced word of the permutation
        ``self``.

        See :meth:`reduced_words` for the definition of reduced words and
        a way to compute them all.

        EXAMPLES::

            sage: Permutation([3,4,2,1]).reduced_word_lexmin()
            [1, 2, 1, 3, 2]

            Permutation([1]).reduced_word_lexmin()
            []
            Permutation([]).reduced_word_lexmin()
            []
        """
    def number_of_reduced_words(self):
        """
        Return the number of reduced words of ``self`` without explicitly
        computing them all.

        EXAMPLES::

            sage: p = Permutation([6,4,2,5,1,8,3,7])
            sage: len(p.reduced_words()) == p.number_of_reduced_words()                 # needs sage.combinat
            True
        """
    def rothe_diagram(self):
        """
        Return the Rothe diagram of ``self``.

        EXAMPLES::

            sage: p = Permutation([4,2,1,3])
            sage: D = p.rothe_diagram(); D                                              # needs sage.combinat
            [(0, 0), (0, 1), (0, 2), (1, 0)]
            sage: D.pp()                                                                # needs sage.combinat
            O O O .
            O . . .
            . . . .
            . . . .
        """
    def rank_matrix(self):
        """
        Return the rank matrix of ``self``.

        Let `P = [P_{ij}]_{i, j=1}^n` be the permutation matrix of `w \\in S_n`.
        The rank matrix is the `n \\times n` matrix with entries

        .. MATH::

            r_w(i, j) = \\sum_{a=1}^i \\sum_{b=1}^j P_{ij}.

        EXAMPLES::

            sage: w = Permutation([2, 1, 5, 4, 3])
            sage: w.to_matrix()
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 0 0 1]
            [0 0 0 1 0]
            [0 0 1 0 0]
            sage: w.rank_matrix()
            [0 1 1 1 1]
            [1 2 2 2 2]
            [1 2 2 2 3]
            [1 2 2 3 4]
            [1 2 3 4 5]
        """
    def schubert_determinant_ideal(self):
        """
        Return the Schubert determinant ideal of ``self``.

        From Lemma 3.10 [Ful1992]_, the matrix Schubert variety of
        a permutation `w \\in S_n` is defined by the ideal

        .. MATH::

            I_w = \\sum_{(i, j)} I_{r_w(i, j)+1}(i, j),

        where the sum is over the :meth:`essential set
        <sage.combinat.diagram.Diagram.essential_set>`, `[r_w(i, j)]_{i, j}`
        is the :meth:`rank_matrix` of `w`, and `I_k(i, j)` is the ideal
        generated by the `k \\times k` minors of the `i \\times j`
        matrix `[z_{ab}]_{a, b}`.

        These ideals are known to be prime of codimension equal to `\\ell(w)`
        (the length of `w`) such that `R / I_w` is Cohen-Macaulay, where `R`
        is the polynomial ring `\\QQ[z_{ab} | 1 \\leq a, b \\leq n]` from
        Prop. 3.10 of [Ful1992]_.

        EXAMPLES::

            sage: w = Permutation([3, 1, 4, 2])
            sage: Iw = w.schubert_determinant_ideal()
            sage: Iw.gens()
            [z00, z01, -z01*z10 + z00*z11, -z01*z20 + z00*z21, -z11*z20 + z10*z21]
            sage: Iw.dimension()
            13
            sage: Iw.dimension() + w.length()
            16
            sage: Iw.is_prime()
            True

            sage: w = Permutation([2, 1, 5, 4, 3])
            sage: Iw = w.schubert_determinant_ideal()
            sage: Iw.dimension()
            21
            sage: w.length() + Iw.dimension()
            25
            sage: Iw.is_prime()
            True
        """
    def fixed_points(self) -> list[int]:
        """
        Return a list of the fixed points of ``self``.

        EXAMPLES::

            sage: Permutation([1,3,2,4]).fixed_points()
            [1, 4]
            sage: Permutation([1,2,3,4]).fixed_points()
            [1, 2, 3, 4]
        """
    def number_of_fixed_points(self) -> int:
        """
        Return the number of fixed points of ``self``.

        EXAMPLES::

            sage: Permutation([1,3,2,4]).number_of_fixed_points()
            2
            sage: Permutation([1,2,3,4]).number_of_fixed_points()
            4
        """
    def is_derangement(self) -> bool:
        """
        Return whether ``self`` is a derangement.

        A permutation `\\sigma` is a derangement if `\\sigma` has no
        fixed points.

        EXAMPLES::

            sage: P = Permutation([1,4,2,3])
            sage: P.is_derangement()
            False
            sage: P = Permutation([2,3,1])
            sage: P.is_derangement()
            True
        """
    def is_simple(self) -> bool:
        """
        Return whether ``self`` is simple.

        A permutation is simple if it does not send any proper sub-interval
        to a sub-interval.

        For instance, ``[6,1,3,5,2,4]`` is not simple because it maps the
        interval ``[3,4,5,6]`` to ``[2,3,4,5]``, whereas ``[2,6,3,5,1,4]`` is
        simple.

        See :oeis:`A111111`

        EXAMPLES::

            sage: g = Permutation([4,2,3,1])
            sage: g.is_simple()
            False

            sage: g = Permutation([6,1,3,5,2,4])
            sage: g.is_simple()
            False

            sage: g = Permutation([2,6,3,5,1,4])
            sage: g.is_simple()
            True

            sage: [len([pi for pi in Permutations(n) if pi.is_simple()])
            ....:  for n in range(6)]
            [1, 1, 2, 0, 2, 6]
        """
    def recoils(self) -> list[int]:
        """
        Return the list of the positions of the recoils of ``self``.

        A recoil of a permutation `p` is an integer `i` such that `i+1`
        appears to the left of `i` in `p`.
        Here, the positions are being counted starting at `0`.
        (Note that it is the positions, not the recoils themselves, which
        are being listed.)

        EXAMPLES::

            sage: Permutation([1,4,3,2]).recoils()
            [2, 3]
            sage: Permutation([]).recoils()
            []
        """
    def number_of_recoils(self) -> Integer:
        """
        Return the number of recoils of the permutation ``self``.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).number_of_recoils()
            2
        """
    def recoils_composition(self) -> Composition:
        """
        Return the recoils composition of ``self``.

        The recoils composition of a permutation `p \\in S_n` is the
        composition of `n` whose descent set is the set of the recoils
        of `p` (not their positions). In other words, this is the
        descents composition of `p^{-1}`.

        EXAMPLES::

            sage: Permutation([1,3,2,4]).recoils_composition()
            [2, 2]
            sage: Permutation([]).recoils_composition()
            []
        """
    def descents(self, final_descent: bool = False, side: str = 'right', positive: bool = False, from_zero: bool = False, index_set=None) -> list[int]:
        """
        Return the list of the descents of ``self``.

        A descent of a permutation `p` is an integer `i` such that
        `p(i) > p(i+1)`.

        .. WARNING::

            By default, the descents are returned as elements in the
            index set, i.e., starting at `1`. If you want them to
            start at `0`, set the keyword ``from_zero`` to ``True``.

        INPUT:

        - ``final_descent`` -- boolean (default: ``False``);
          if ``True``, the last position of a non-empty
          permutation is also considered as a descent

        - ``side`` -- ``'right'`` (default) or ``'left'``;
          if ``'left'``, return the descents of the inverse permutation

        - ``positive`` -- boolean (default: ``False``);
          if ``True``, return the positions that are not descents

        - ``from_zero`` -- boolean (default: ``False``);
          if ``True``, return the positions starting from `0`

        - ``index_set`` -- list (default: ``[1, ..., n-1]`` where ``self``
          is a permutation of ``n``); the index set to check for descents

        EXAMPLES::

            sage: Permutation([3,1,2]).descents()
            [1]
            sage: Permutation([1,4,3,2]).descents()
            [2, 3]
            sage: Permutation([1,4,3,2]).descents(final_descent=True)
            [2, 3, 4]
            sage: Permutation([1,4,3,2]).descents(index_set=[1,2])
            [2]
            sage: Permutation([1,4,3,2]).descents(from_zero=True)
            [1, 2]

        TESTS:

        Check that the original error of :issue:`23891` is fixed::

            sage: Permutations(4)([1,4,3,2]).weak_covers()
            [[1, 3, 4, 2], [1, 4, 2, 3]]
        """
    def idescents(self, final_descent: bool = False, from_zero: bool = False) -> list[int]:
        """
        Return a list of the idescents of ``self``, that is the list of
        the descents of ``self``'s inverse.

        A descent of a permutation ``p`` is an integer ``i`` such that
        ``p(i) > p(i+1)``.

        .. WARNING::

            By default, the descents are returned as elements in the
            index set, i.e., starting at `1`. If you want them to
            start at `0`, set the keyword ``from_zero`` to ``True``.

        INPUT:

        - ``final_descent`` -- boolean (default: ``False``); if ``True``, the
          last position of a non-empty permutation is also considered as a
          descent

        - ``from_zero`` -- boolean (default: ``False``); if ``False``, return
          the positions starting from `1`

        EXAMPLES::

            sage: Permutation([2,3,1]).idescents()
            [1]
            sage: Permutation([1,4,3,2]).idescents()
            [2, 3]
            sage: Permutation([1,4,3,2]).idescents(final_descent=True)
            [2, 3, 4]
            sage: Permutation([1,4,3,2]).idescents(from_zero=True)
            [1, 2]
        """
    def idescents_signature(self, final_descent: bool = False):
        """
        Return the list obtained as follows: Each position in ``self``
        is mapped to `-1` if it is an idescent and `1` if it is not an
        idescent.

        See :meth:`idescents` for a definition of idescents.

        With the ``final_descent`` option, the last position of a
        non-empty permutation is also considered as a descent.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).idescents()
            [2, 3]
            sage: Permutation([1,4,3,2]).idescents_signature()
            [1, -1, -1, 1]
        """
    def number_of_descents(self, final_descent: bool = False) -> int:
        """
        Return the number of descents of ``self``.

        With the ``final_descent`` option, the last position of a
        non-empty permutation is also considered as a descent.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).number_of_descents()
            2
            sage: Permutation([1,4,3,2]).number_of_descents(final_descent=True)
            3
        """
    def number_of_idescents(self, final_descent: bool = False) -> int:
        """
        Return the number of idescents of ``self``.

        See :meth:`idescents` for a definition of idescents.

        With the ``final_descent`` option, the last position of a
        non-empty permutation is also considered as a descent.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).number_of_idescents()
            2
            sage: Permutation([1,4,3,2]).number_of_idescents(final_descent=True)
            3
        """
    def descents_composition(self) -> Composition:
        """
        Return the descent composition of ``self``.

        The descent composition of a permutation `p \\in S_n` is defined
        as the composition of `n` whose descent set equals the descent
        set of `p`. Here, the descent set of `p` is defined as the set
        of all `i \\in \\{ 1, 2, \\ldots, n-1 \\}` satisfying
        `p(i) > p(i+1)`. The descent set
        of a composition `c = (i_1, i_2, \\ldots, i_k)` is defined as
        the set `\\{ i_1, i_1 + i_2, i_1 + i_2 + i_3, \\ldots,
        i_1 + i_2 + \\cdots + i_{k-1} \\}`.

        EXAMPLES::

            sage: Permutation([1,3,2,4]).descents_composition()
            [2, 2]
            sage: Permutation([4,1,6,7,2,3,8,5]).descents_composition()
            [1, 3, 3, 1]
            sage: Permutation([]).descents_composition()
            []
        """
    def descent_polynomial(self):
        """
        Return the descent polynomial of the permutation ``self``.

        The descent polynomial of a permutation `p` is the product of
        all the ``z[p(i)]`` where ``i`` ranges over the descents of
        ``p``.

        A descent of a permutation ``p`` is an integer ``i`` such that
        ``p(i) > p(i+1)``.

        REFERENCES:

        - [GS1984]_

        EXAMPLES::

            sage: Permutation([2,1,3]).descent_polynomial()
            z2
            sage: Permutation([4,3,2,1]).descent_polynomial()
            z2*z3*z4

        .. TODO::

            This docstring needs to be fixed. This is not defined in [GS1984]_
            (the descent monomial in their (7.23) is different).
        """
    def major_index(self, final_descent: bool = False) -> Integer:
        """
        Return the major index of ``self``.

        The major index of a permutation `p` is the sum of the descents of `p`.
        Since our permutation indices are 0-based, we need to add the
        number of descents.

        With the ``final_descent`` option, the last position of a
        non-empty permutation is also considered as a descent.

        EXAMPLES::

            sage: Permutation([2,1,3]).major_index()
            1
            sage: Permutation([3,4,1,2]).major_index()
            2
            sage: Permutation([4,3,2,1]).major_index()
            6
        """
    def multi_major_index(self, composition):
        """
        Return the multimajor index of this permutation with respect to ``composition``.

        INPUT:

        - ``composition`` -- a composition of the :meth:`size` of this permutation

        EXAMPLES::

            sage: p = Permutation([5, 6, 2, 1, 3, 7, 4])
            sage: p.multi_major_index([3, 2, 2])
            [2, 0, 1]
            sage: p.multi_major_index([7]) == [p.major_index()]
            True
            sage: p.multi_major_index([1]*7)
            [0, 0, 0, 0, 0, 0, 0]
            sage: Permutation([]).multi_major_index([])
            []

        TESTS::

            sage: p.multi_major_index([1, 3, 3, 7])
            Traceback (most recent call last):
            ...
            ValueError: size of the composition should be equal to size of the permutation

        REFERENCES:

        - [JS2000]_
        """
    def imajor_index(self, final_descent: bool = False) -> Integer:
        """
        Return the inverse major index of the permutation ``self``, which is
        the major index of the inverse of ``self``.

        The major index of a permutation `p` is the sum of the descents of `p`.
        Since our permutation indices are 0-based, we need to add the
        number of descents.

        With the ``final_descent`` option, the last position of a
        non-empty permutation is also considered as a descent.

        EXAMPLES::

            sage: Permutation([2,1,3]).imajor_index()
            1
            sage: Permutation([3,4,1,2]).imajor_index()
            2
            sage: Permutation([4,3,2,1]).imajor_index()
            6
        """
    def to_major_code(self, final_descent: bool = False):
        """
        Return the major code of the permutation ``self``.

        The major code of a permutation `p` is defined as the sequence
        `(m_1-m_2, m_2-m_3, \\ldots, m_n)`, where `m_i` is the major
        index of the permutation obtained by erasing all letters smaller than
        `i` from `p`.

        With the ``final_descent`` option, the last position of a
        non-empty permutation is also considered as a descent.
        This has an effect on the computation of major indices.

        REFERENCES:

        - Carlitz, L. *q-Bernoulli and Eulerian Numbers*.
          Trans. Amer. Math. Soc. 76 (1954) 332-350.
          http://www.ams.org/journals/tran/1954-076-02/S0002-9947-1954-0060538-2/

        - Skandera, M. *An Eulerian Partner for Inversions*.
          Sém. Lothar. Combin. 46 (2001) B46d.
          http://www.lehigh.edu/~mas906/papers/partner.ps

        EXAMPLES::

            sage: Permutation([9,3,5,7,2,1,4,6,8]).to_major_code()
            [5, 0, 1, 0, 1, 2, 0, 1, 0]
            sage: Permutation([2,8,4,3,6,7,9,5,1]).to_major_code()
            [8, 3, 3, 1, 4, 0, 1, 0, 0]
        """
    def peaks(self) -> list[int]:
        """
        Return a list of the peaks of the permutation ``self``.

        A peak of a permutation `p` is an integer `i` such that
        `p(i-1) < p(i)` and `p(i) > p(i+1)`.

        EXAMPLES::

            sage: Permutation([1,3,2,4,5]).peaks()
            [1]
            sage: Permutation([4,1,3,2,6,5]).peaks()
            [2, 4]
            sage: Permutation([]).peaks()
            []
        """
    def number_of_peaks(self) -> int:
        """
        Return the number of peaks of the permutation ``self``.

        A peak of a permutation `p` is an integer `i` such that
        `p(i-1) < p(i)` and `p(i) > p(i+1)`.

        EXAMPLES::

            sage: Permutation([1,3,2,4,5]).number_of_peaks()
            1
            sage: Permutation([4,1,3,2,6,5]).number_of_peaks()
            2
        """
    def saliances(self) -> list[int]:
        """
        Return a list of the saliances of the permutation ``self``.

        A saliance of a permutation `p` is an integer `i` such that
        `p(i) > p(j)` for all `j > i`.

        EXAMPLES::

            sage: Permutation([2,3,1,5,4]).saliances()
            [3, 4]
            sage: Permutation([5,4,3,2,1]).saliances()
            [0, 1, 2, 3, 4]
        """
    def number_of_saliances(self) -> int:
        """
        Return the number of saliances of ``self``.

        A saliance of a permutation `p` is an integer `i` such that
        `p(i) > p(j)` for all `j > i`.

        EXAMPLES::

            sage: Permutation([2,3,1,5,4]).number_of_saliances()
            2
            sage: Permutation([5,4,3,2,1]).number_of_saliances()
            5
        """
    def bruhat_lequal(self, p2) -> bool:
        """
        Return ``True`` if ``self`` is less or equal to ``p2`` in
        the Bruhat order.

        The Bruhat order (also called strong Bruhat order or Chevalley
        order) on the symmetric group `S_n` is the partial order on `S_n`
        determined by the following condition: If `p` is a permutation,
        and `i` and `j` are two indices satisfying `p(i) > p(j)` and
        `i < j` (that is, `(i, j)` is an inversion of `p` with `i < j`),
        then `p \\circ (i, j)` (the permutation obtained by first
        switching `i` with `j` and then applying `p`) is smaller than `p`
        in the Bruhat order.

        One can show that a permutation `p \\in S_n` is less or equal to
        a permutation `q \\in S_n` in the Bruhat order if and only if
        for every `i \\in \\{ 0, 1, \\cdots , n \\}` and
        `j \\in \\{ 1, 2, \\cdots , n \\}`, the number of the elements among
        `p(1), p(2), \\cdots, p(j)` that are greater than `i` is `\\leq`
        to the number of the elements among `q(1), q(2), \\cdots, q(j)`
        that are greater than `i`.

        This method assumes that ``self`` and ``p2`` are permutations
        of the same integer `n`.

        EXAMPLES::

            sage: Permutation([2,4,3,1]).bruhat_lequal(Permutation([3,4,2,1]))
            True

            sage: Permutation([2,1,3]).bruhat_lequal(Permutation([2,3,1]))
            True
            sage: Permutation([2,1,3]).bruhat_lequal(Permutation([3,1,2]))
            True
            sage: Permutation([2,1,3]).bruhat_lequal(Permutation([1,2,3]))
            False
            sage: Permutation([1,3,2]).bruhat_lequal(Permutation([2,1,3]))
            False
            sage: Permutation([1,3,2]).bruhat_lequal(Permutation([2,3,1]))
            True
            sage: Permutation([2,3,1]).bruhat_lequal(Permutation([1,3,2]))
            False
            sage: sorted( [len([b for b in Permutations(3) if a.bruhat_lequal(b)])
            ....:          for a in Permutations(3)] )
            [1, 2, 2, 4, 4, 6]

            sage: Permutation([]).bruhat_lequal(Permutation([]))
            True
        """
    def weak_excedences(self) -> list:
        """
        Return all the numbers ``self[i]`` such that ``self[i] >= i+1``.

        EXAMPLES::

            sage: Permutation([1,4,3,2,5]).weak_excedences()
            [1, 4, 3, 5]
        """
    def bruhat_inversions(self) -> list:
        """
        Return the list of inversions of ``self`` such that the application of
        this inversion to ``self`` decreases its number of inversions by
        exactly 1.

        Equivalently, it returns the list of pairs `(i,j)` such that `i < j`,
        such that `p(i) > p(j)` and such that there exists no `k` (strictly)
        between `i` and `j` satisfying `p(i) > p(k) > p(j)`.

        EXAMPLES::

            sage: Permutation([5,2,3,4,1]).bruhat_inversions()
            [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4]]
            sage: Permutation([6,1,4,5,2,3]).bruhat_inversions()
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 4], [3, 5]]
        """
    def bruhat_inversions_iterator(self) -> Generator[Incomplete]:
        """
        Return the iterator for the inversions of ``self`` such that the
        application of this inversion to ``self`` decreases its number of
        inversions by exactly 1.

        EXAMPLES::

            sage: list(Permutation([5,2,3,4,1]).bruhat_inversions_iterator())
            [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4]]
            sage: list(Permutation([6,1,4,5,2,3]).bruhat_inversions_iterator())
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 4], [3, 5]]
        """
    def bruhat_succ(self) -> list:
        """
        Return a list of the permutations strictly greater than ``self`` in
        the Bruhat order (on the symmetric group containing ``self``) such
        that there is no permutation between one of those and ``self``.

        See :meth:`bruhat_lequal` for the definition of the Bruhat order.

        EXAMPLES::

            sage: Permutation([6,1,4,5,2,3]).bruhat_succ()
            [[6, 4, 1, 5, 2, 3],
             [6, 2, 4, 5, 1, 3],
             [6, 1, 5, 4, 2, 3],
             [6, 1, 4, 5, 3, 2]]
        """
    def bruhat_succ_iterator(self) -> Generator[Incomplete]:
        """
        An iterator for the permutations that are strictly greater than
        ``self`` in the Bruhat order (on the symmetric group containing
        ``self``) such that there is no permutation between one
        of those and ``self``.

        See :meth:`bruhat_lequal` for the definition of the Bruhat order.

        EXAMPLES::

            sage: [x for x in Permutation([6,1,4,5,2,3]).bruhat_succ_iterator()]
            [[6, 4, 1, 5, 2, 3],
             [6, 2, 4, 5, 1, 3],
             [6, 1, 5, 4, 2, 3],
             [6, 1, 4, 5, 3, 2]]
        """
    def bruhat_pred(self) -> list:
        """
        Return a list of the permutations strictly smaller than ``self``
        in the Bruhat order (on the symmetric group containing ``self``) such
        that there is no permutation between one of those and ``self``.

        See :meth:`bruhat_lequal` for the definition of the Bruhat order.

        EXAMPLES::

            sage: Permutation([6,1,4,5,2,3]).bruhat_pred()
            [[1, 6, 4, 5, 2, 3],
             [4, 1, 6, 5, 2, 3],
             [5, 1, 4, 6, 2, 3],
             [6, 1, 2, 5, 4, 3],
             [6, 1, 3, 5, 2, 4],
             [6, 1, 4, 2, 5, 3],
             [6, 1, 4, 3, 2, 5]]
        """
    def bruhat_pred_iterator(self) -> Generator[Incomplete]:
        """
        An iterator for the permutations strictly smaller than ``self`` in
        the Bruhat order (on the symmetric group containing ``self``) such
        that there is no permutation between one of those and ``self``.

        See :meth:`bruhat_lequal` for the definition of the Bruhat order.

        EXAMPLES::

            sage: [x for x in Permutation([6,1,4,5,2,3]).bruhat_pred_iterator()]
            [[1, 6, 4, 5, 2, 3],
             [4, 1, 6, 5, 2, 3],
             [5, 1, 4, 6, 2, 3],
             [6, 1, 2, 5, 4, 3],
             [6, 1, 3, 5, 2, 4],
             [6, 1, 4, 2, 5, 3],
             [6, 1, 4, 3, 2, 5]]
        """
    def bruhat_smaller(self):
        """
        Return the combinatorial class of permutations smaller than or
        equal to ``self`` in the Bruhat order (on the symmetric group
        containing ``self``).

        See :meth:`bruhat_lequal` for the definition of the Bruhat order.

        EXAMPLES::

            sage: Permutation([4,1,2,3]).bruhat_smaller().list()
            [[1, 2, 3, 4],
             [1, 2, 4, 3],
             [1, 3, 2, 4],
             [1, 4, 2, 3],
             [2, 1, 3, 4],
             [2, 1, 4, 3],
             [3, 1, 2, 4],
             [4, 1, 2, 3]]
        """
    def bruhat_greater(self):
        """
        Return the combinatorial class of permutations greater than or
        equal to ``self`` in the Bruhat order (on the symmetric group
        containing ``self``).

        See :meth:`bruhat_lequal` for the definition of the Bruhat order.

        EXAMPLES::

            sage: Permutation([4,1,2,3]).bruhat_greater().list()
            [[4, 1, 2, 3],
             [4, 1, 3, 2],
             [4, 2, 1, 3],
             [4, 2, 3, 1],
             [4, 3, 1, 2],
             [4, 3, 2, 1]]
        """
    def permutohedron_lequal(self, p2, side: str = 'right') -> bool:
        """
        Return ``True`` if ``self`` is less or equal to ``p2`` in the
        permutohedron order.

        By default, the computations are done in the right permutohedron.
        If you pass the option ``side='left'``, then they will be done in
        the left permutohedron.

        For every nonnegative integer `n`, the right (resp. left)
        permutohedron order (also called the right (resp. left) weak
        order, or the right (resp. left) weak Bruhat order) is a partial
        order on the symmetric group `S_n`. It can be defined in various
        ways, including the following ones:

        - Two permutations `u` and `v` in `S_n` satisfy `u \\leq v` in
          the right (resp. left) permutohedron order if and only if
          the (Coxeter) length of the permutation `v^{-1} \\circ u`
          (resp. of the permutation `u \\circ v^{-1}`) equals the
          length of `v` minus the length of `u`. Here, `p \\circ q` means
          the permutation obtained by applying `q` first and then `p`.
          (Recall that the Coxeter length of a permutation is its number
          of inversions.)

        - Two permutations `u` and `v` in `S_n` satisfy `u \\leq v` in
          the right (resp. left) permutohedron order if and only if
          every pair `(i, j)` of elements of `\\{ 1, 2, \\cdots, n \\}`
          such that `i < j` and `u^{-1}(i) > u^{-1}(j)` (resp.
          `u(i) > u(j)`) also satisfies `v^{-1}(i) > v^{-1}(j)`
          (resp. `v(i) > v(j)`).

        - A permutation `v \\in S_n` covers a permutation `u \\in S_n` in
          the right (resp. left) permutohedron order if and only if we
          have `v = u \\circ (i, i + 1)` (resp. `v = (i, i + 1) \\circ u`)
          for some `i \\in \\{ 1, 2, \\cdots, n - 1 \\}` satisfying
          `u(i) < u(i + 1)` (resp. `u^{-1}(i) < u^{-1}(i + 1)`). Here,
          again, `p \\circ q` means the permutation obtained by applying
          `q` first and then `p`.

        The right and the left permutohedron order are mutually
        isomorphic, with the isomorphism being the map sending every
        permutation to its inverse. Each of these orders endows the
        symmetric group `S_n` with the structure of a graded poset
        (the rank function being the Coxeter length).

        .. WARNING::

            The permutohedron order is not to be mistaken for the
            strong Bruhat order (:meth:`bruhat_lequal`), despite both
            orders being occasionally referred to as the Bruhat order.

        EXAMPLES::

            sage: p = Permutation([3,2,1,4])
            sage: p.permutohedron_lequal(Permutation([4,2,1,3]))
            False
            sage: p.permutohedron_lequal(Permutation([4,2,1,3]), side='left')
            True
            sage: p.permutohedron_lequal(p)
            True

            sage: Permutation([2,1,3]).permutohedron_lequal(Permutation([2,3,1]))
            True
            sage: Permutation([2,1,3]).permutohedron_lequal(Permutation([3,1,2]))
            False
            sage: Permutation([2,1,3]).permutohedron_lequal(Permutation([1,2,3]))
            False
            sage: Permutation([1,3,2]).permutohedron_lequal(Permutation([2,1,3]))
            False
            sage: Permutation([1,3,2]).permutohedron_lequal(Permutation([2,3,1]))
            False
            sage: Permutation([2,3,1]).permutohedron_lequal(Permutation([1,3,2]))
            False
            sage: Permutation([2,1,3]).permutohedron_lequal(Permutation([2,3,1]), side='left')
            False
            sage: sorted( [len([b for b in Permutations(3) if a.permutohedron_lequal(b)])
            ....:          for a in Permutations(3)] )
            [1, 2, 2, 3, 3, 6]
            sage: sorted( [len([b for b in Permutations(3) if a.permutohedron_lequal(b, side='left')])
            ....:          for a in Permutations(3)] )
            [1, 2, 2, 3, 3, 6]

            sage: Permutation([]).permutohedron_lequal(Permutation([]))
            True
        """
    def permutohedron_succ(self, side: str = 'right'):
        """
        Return a list of the permutations strictly greater than ``self``
        in the permutohedron order such that there is no permutation
        between any of those and ``self``.

        By default, the computations are done in the right permutohedron.
        If you pass the option ``side='left'``, then they will be done in
        the left permutohedron.

        See :meth:`permutohedron_lequal` for the definition of the
        permutohedron orders.

        EXAMPLES::

            sage: p = Permutation([4,2,1,3])
            sage: p.permutohedron_succ()
            [[4, 2, 3, 1]]
            sage: p.permutohedron_succ(side='left')
            [[4, 3, 1, 2]]
        """
    def permutohedron_pred(self, side: str = 'right') -> list:
        """
        Return a list of the permutations strictly smaller than ``self``
        in the permutohedron order such that there is no permutation
        between any of those and ``self``.

        By default, the computations are done in the right permutohedron.
        If you pass the option ``side='left'``, then they will be done in
        the left permutohedron.

        See :meth:`permutohedron_lequal` for the definition of the
        permutohedron orders.

        EXAMPLES::

            sage: p = Permutation([4,2,1,3])
            sage: p.permutohedron_pred()
            [[2, 4, 1, 3], [4, 1, 2, 3]]
            sage: p.permutohedron_pred(side='left')
            [[4, 1, 2, 3], [3, 2, 1, 4]]
        """
    def permutohedron_smaller(self, side: str = 'right') -> list:
        """
        Return a list of permutations smaller than or equal to ``self``
        in the permutohedron order.

        By default, the computations are done in the right permutohedron.
        If you pass the option ``side='left'``, then they will be done in
        the left permutohedron.

        See :meth:`permutohedron_lequal` for the definition of the
        permutohedron orders.

        EXAMPLES::

            sage: Permutation([4,2,1,3]).permutohedron_smaller()
            [[1, 2, 3, 4],
             [1, 2, 4, 3],
             [1, 4, 2, 3],
             [2, 1, 3, 4],
             [2, 1, 4, 3],
             [2, 4, 1, 3],
             [4, 1, 2, 3],
             [4, 2, 1, 3]]

        ::

            sage: Permutation([4,2,1,3]).permutohedron_smaller(side='left')
            [[1, 2, 3, 4],
             [1, 3, 2, 4],
             [2, 1, 3, 4],
             [2, 3, 1, 4],
             [3, 1, 2, 4],
             [3, 2, 1, 4],
             [4, 1, 2, 3],
             [4, 2, 1, 3]]
        """
    def permutohedron_greater(self, side: str = 'right') -> list:
        """
        Return a list of permutations greater than or equal to ``self``
        in the permutohedron order.

        By default, the computations are done in the right permutohedron.
        If you pass the option ``side='left'``, then they will be done in
        the left permutohedron.

        See :meth:`permutohedron_lequal` for the definition of the
        permutohedron orders.

        EXAMPLES::

            sage: Permutation([4,2,1,3]).permutohedron_greater()
            [[4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 2, 1]]
            sage: Permutation([4,2,1,3]).permutohedron_greater(side='left')
            [[4, 2, 1, 3], [4, 3, 1, 2], [4, 3, 2, 1]]
        """
    def right_permutohedron_interval_iterator(self, other):
        """
        Return an iterator on the permutations (represented as integer
        lists) belonging to the right permutohedron interval where
        ``self`` is the minimal element and ``other`` the maximal element.

        See :meth:`permutohedron_lequal` for the definition of the
        permutohedron orders.

        EXAMPLES::

            sage: p = Permutation([2, 1, 4, 5, 3]); q = Permutation([2, 5, 4, 1, 3])
            sage: p.right_permutohedron_interval(q)  # indirect doctest                 # needs sage.graphs sage.modules
            [[2, 4, 5, 1, 3], [2, 4, 1, 5, 3], [2, 1, 4, 5, 3],
             [2, 1, 5, 4, 3], [2, 5, 1, 4, 3], [2, 5, 4, 1, 3]]
        """
    def right_permutohedron_interval(self, other):
        """
        Return the list of the permutations belonging to the right
        permutohedron interval where ``self`` is the minimal element and
        ``other`` the maximal element.

        See :meth:`permutohedron_lequal` for the definition of the
        permutohedron orders.

        EXAMPLES::

            sage: p = Permutation([2, 1, 4, 5, 3]); q = Permutation([2, 5, 4, 1, 3])
            sage: p.right_permutohedron_interval(q)                                     # needs sage.graphs sage.modules
            [[2, 4, 5, 1, 3], [2, 4, 1, 5, 3], [2, 1, 4, 5, 3],
             [2, 1, 5, 4, 3], [2, 5, 1, 4, 3], [2, 5, 4, 1, 3]]

        TESTS::

            sage: # needs sage.graphs sage.modules
            sage: Permutation([]).right_permutohedron_interval(Permutation([]))
            [[]]
            sage: Permutation([3, 1, 2]).right_permutohedron_interval(Permutation([3, 1, 2]))
            [[3, 1, 2]]
            sage: Permutation([1, 3, 2, 4]).right_permutohedron_interval(Permutation([3, 4, 2, 1]))
            [[3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1], [1, 3, 4, 2],
             [1, 3, 2, 4], [3, 2, 4, 1], [3, 2, 1, 4], [3, 1, 2, 4]]
            sage: Permutation([2, 1, 4, 5, 3]).right_permutohedron_interval(Permutation([2, 5, 4, 1, 3]))
            [[2, 4, 5, 1, 3], [2, 4, 1, 5, 3], [2, 1, 4, 5, 3],
             [2, 1, 5, 4, 3], [2, 5, 1, 4, 3], [2, 5, 4, 1, 3]]
            sage: Permutation([2, 5, 4, 1, 3]).right_permutohedron_interval(Permutation([2, 1, 4, 5, 3]))
            Traceback (most recent call last):
            ...
            ValueError: [2, 5, 4, 1, 3] must be lower or equal than [2, 1, 4, 5, 3] for the right permutohedron order
            sage: Permutation([2, 4, 1, 3]).right_permutohedron_interval(Permutation([2, 1, 4, 5, 3]))
            Traceback (most recent call last):
            ...
            ValueError: len([2, 4, 1, 3]) and len([2, 1, 4, 5, 3]) must be equal
        """
    def permutohedron_join(self, other, side: str = 'right') -> Permutation:
        """
        Return the join of the permutations ``self`` and ``other``
        in the right permutohedron order (or, if ``side`` is set to
        ``'left'``, in the left permutohedron order).

        The permutohedron orders (see :meth:`permutohedron_lequal`)
        are lattices; the join operation refers to this lattice
        structure. In more elementary terms, the join of two
        permutations `\\pi` and `\\psi` in the symmetric group `S_n`
        is the permutation in `S_n` whose set of inversion is the
        transitive closure of the union of the set of inversions of
        `\\pi` with the set of inversions of `\\psi`.

        .. SEEALSO::

            :meth:`permutohedron_lequal`, :meth:`permutohedron_meet`.

        ALGORITHM:

        It is enough to construct the join of any two permutations
        `\\pi` and `\\psi` in `S_n` with respect to the right weak
        order. (The join of `\\pi` and `\\psi` with respect to the
        left weak order is the inverse of the join of `\\pi^{-1}`
        and `\\psi^{-1}` with respect to the right weak order.)
        Start with an empty list `l` (denoted ``xs`` in the actual
        code). For `i = 1, 2, \\ldots, n` (in this order), we insert
        `i` into this list in the rightmost possible position such
        that any letter in `\\{ 1, 2, ..., i-1 \\}` which appears
        further right than `i` in either `\\pi` or `\\psi` (or both)
        must appear further right than `i` in the resulting list.
        After all numbers are inserted, we are left with a list
        which is precisely the join of `\\pi` and `\\psi` (in
        one-line notation). This algorithm is due to Markowsky,
        [Mar1994]_ (Theorem 1 (a)).

        AUTHORS:

        Viviane Pons and Darij Grinberg, 18 June 2014.

        EXAMPLES::

            sage: p = Permutation([3,1,2])
            sage: q = Permutation([1,3,2])
            sage: p.permutohedron_join(q)
            [3, 1, 2]
            sage: r = Permutation([2,1,3])
            sage: r.permutohedron_join(p)
            [3, 2, 1]

        ::

            sage: p = Permutation([3,2,4,1])
            sage: q = Permutation([4,2,1,3])
            sage: p.permutohedron_join(q)
            [4, 3, 2, 1]
            sage: r = Permutation([3,1,2,4])
            sage: p.permutohedron_join(r)
            [3, 2, 4, 1]
            sage: q.permutohedron_join(r)
            [4, 3, 2, 1]
            sage: s = Permutation([1,4,2,3])
            sage: s.permutohedron_join(r)
            [4, 3, 1, 2]

        The universal property of the join operation is
        satisfied::

            sage: def test_uni_join(p, q):
            ....:     j = p.permutohedron_join(q)
            ....:     if not p.permutohedron_lequal(j):
            ....:         return False
            ....:     if not q.permutohedron_lequal(j):
            ....:         return False
            ....:     for r in p.permutohedron_greater():
            ....:         if q.permutohedron_lequal(r) and not j.permutohedron_lequal(r):
            ....:             return False
            ....:     return True
            sage: all( test_uni_join(p, q) for p in Permutations(3) for q in Permutations(3) )
            True
            sage: test_uni_join(Permutation([6, 4, 7, 3, 2, 5, 8, 1]), Permutation([7, 3, 1, 2, 5, 4, 6, 8]))
            True

        Border cases::

            sage: p = Permutation([])
            sage: p.permutohedron_join(p)
            []
            sage: p = Permutation([1])
            sage: p.permutohedron_join(p)
            [1]

        The left permutohedron::

            sage: p = Permutation([3,1,2])
            sage: q = Permutation([1,3,2])
            sage: p.permutohedron_join(q, side='left')
            [3, 2, 1]
            sage: r = Permutation([2,1,3])
            sage: r.permutohedron_join(p, side='left')
            [3, 1, 2]
        """
    def permutohedron_meet(self, other, side: str = 'right') -> Permutation:
        """
        Return the meet of the permutations ``self`` and ``other``
        in the right permutohedron order (or, if ``side`` is set to
        ``'left'``, in the left permutohedron order).

        The permutohedron orders (see :meth:`permutohedron_lequal`)
        are lattices; the meet operation refers to this lattice
        structure. It is connected to the join operation by the
        following simple symmetry property: If `\\pi` and `\\psi`
        are two permutations `\\pi` and `\\psi` in the symmetric group
        `S_n`, and if `w_0` denotes the permutation
        `(n, n-1, \\ldots, 1) \\in S_n`, then

        .. MATH::

            \\pi \\wedge \\psi = w_0 \\circ ((w_0 \\circ \\pi) \\vee (w_0 \\circ \\psi))
            = ((\\pi \\circ w_0) \\vee (\\psi \\circ w_0)) \\circ w_0

        and

        .. MATH::

            \\pi \\vee \\psi = w_0 \\circ ((w_0 \\circ \\pi) \\wedge (w_0 \\circ \\psi))
            = ((\\pi \\circ w_0) \\wedge (\\psi \\circ w_0)) \\circ w_0,

        where `\\wedge` means meet and `\\vee` means join.

        .. SEEALSO::

            :meth:`permutohedron_lequal`, :meth:`permutohedron_join`.

        AUTHORS:

        Viviane Pons and Darij Grinberg, 18 June 2014.

        EXAMPLES::

            sage: p = Permutation([3,1,2])
            sage: q = Permutation([1,3,2])
            sage: p.permutohedron_meet(q)
            [1, 3, 2]
            sage: r = Permutation([2,1,3])
            sage: r.permutohedron_meet(p)
            [1, 2, 3]

        ::

            sage: p = Permutation([3,2,4,1])
            sage: q = Permutation([4,2,1,3])
            sage: p.permutohedron_meet(q)
            [2, 1, 3, 4]
            sage: r = Permutation([3,1,2,4])
            sage: p.permutohedron_meet(r)
            [3, 1, 2, 4]
            sage: q.permutohedron_meet(r)
            [1, 2, 3, 4]
            sage: s = Permutation([1,4,2,3])
            sage: s.permutohedron_meet(r)
            [1, 2, 3, 4]

        The universal property of the meet operation is
        satisfied::

            sage: def test_uni_meet(p, q):
            ....:     m = p.permutohedron_meet(q)
            ....:     if not m.permutohedron_lequal(p):
            ....:         return False
            ....:     if not m.permutohedron_lequal(q):
            ....:         return False
            ....:     for r in p.permutohedron_smaller():
            ....:         if r.permutohedron_lequal(q) and not r.permutohedron_lequal(m):
            ....:             return False
            ....:     return True
            sage: all( test_uni_meet(p, q) for p in Permutations(3) for q in Permutations(3) )
            True
            sage: test_uni_meet(Permutation([6, 4, 7, 3, 2, 5, 8, 1]), Permutation([7, 3, 1, 2, 5, 4, 6, 8]))
            True

        Border cases::

            sage: p = Permutation([])
            sage: p.permutohedron_meet(p)
            []
            sage: p = Permutation([1])
            sage: p.permutohedron_meet(p)
            [1]

        The left permutohedron::

            sage: p = Permutation([3,1,2])
            sage: q = Permutation([1,3,2])
            sage: p.permutohedron_meet(q, side='left')
            [1, 2, 3]
            sage: r = Permutation([2,1,3])
            sage: r.permutohedron_meet(p, side='left')
            [2, 1, 3]
        """
    def has_pattern(self, patt) -> bool:
        """
        Test whether the permutation ``self`` contains the pattern
        ``patt``.

        EXAMPLES::

            sage: Permutation([3,5,1,4,6,2]).has_pattern([1,3,2])                       # needs sage.combinat
            True
        """
    def avoids(self, patt) -> bool:
        """
        Test whether the permutation ``self`` avoids the pattern
        ``patt``.

        EXAMPLES::

            sage: Permutation([6,2,5,4,3,1]).avoids([4,2,3,1])                          # needs sage.combinat
            False
            sage: Permutation([6,1,2,5,4,3]).avoids([4,2,3,1])                          # needs sage.combinat
            True
            sage: Permutation([6,1,2,5,4,3]).avoids([3,4,1,2])                          # needs sage.combinat
            True
        """
    def pattern_positions(self, patt) -> list:
        """
        Return the list of positions where the pattern ``patt`` appears
        in the permutation ``self``.

        EXAMPLES::

            sage: Permutation([3,5,1,4,6,2]).pattern_positions([1,3,2])                 # needs sage.combinat
            [[0, 1, 3], [2, 3, 5], [2, 4, 5]]
        """
    def simion_schmidt(self, avoid=[1, 2, 3]):
        '''
        Implement the Simion-Schmidt map which sends an arbitrary permutation
        to a pattern avoiding permutation, where the permutation pattern is one
        of four length-three patterns.  This method also implements the bijection
        between (for example) ``[1,2,3]``- and ``[1,3,2]``-avoiding permutations.

        INPUT:

        - ``avoid`` -- one of the patterns ``[1,2,3]``, ``[1,3,2]``,
          ``[3,1,2]``, ``[3,2,1]``

        EXAMPLES::

            sage: P = Permutations(6)
            sage: p = P([4,5,1,6,3,2])
            sage: pl = [ [1,2,3], [1,3,2], [3,1,2], [3,2,1] ]
            sage: for q in pl:                                                          # needs sage.combinat
            ....:     s = p.simion_schmidt(q)
            ....:     print("{} {}".format(s, s.has_pattern(q)))
            [4, 6, 1, 5, 3, 2] False
            [4, 2, 1, 3, 5, 6] False
            [4, 5, 3, 6, 2, 1] False
            [4, 5, 1, 6, 2, 3] False
        '''
    def reverse(self):
        """
        Return the permutation obtained by reversing the list.

        EXAMPLES::

            sage: Permutation([3,4,1,2]).reverse()
            [2, 1, 4, 3]
            sage: Permutation([1,2,3,4,5]).reverse()
            [5, 4, 3, 2, 1]
        """
    def complement(self):
        """
        Return the complement of the permutation ``self``.

        The complement of a permutation `w \\in S_n` is defined as the
        permutation in `S_n` sending each `i` to `n + 1 - w(i)`.

        EXAMPLES::

            sage: Permutation([1,2,3]).complement()
            [3, 2, 1]
            sage: Permutation([1, 3, 2]).complement()
            [3, 1, 2]
        """
    def permutation_poset(self):
        """
        Return the permutation poset of ``self``.

        The permutation poset of a permutation `p` is the poset with
        vertices `(i, p(i))` for `i = 1, 2, \\ldots, n` (where `n` is the
        size of `p`) and order inherited from `\\ZZ \\times \\ZZ`.

        EXAMPLES::

            sage: # needs sage.combinat sage.graphs
            sage: Permutation([3,1,5,4,2]).permutation_poset().cover_relations()
            [[(2, 1), (5, 2)],
             [(2, 1), (3, 5)],
             [(2, 1), (4, 4)],
             [(1, 3), (3, 5)],
             [(1, 3), (4, 4)]]
            sage: Permutation([]).permutation_poset().cover_relations()
            []
            sage: Permutation([1,3,2]).permutation_poset().cover_relations()
            [[(1, 1), (2, 3)], [(1, 1), (3, 2)]]
            sage: Permutation([1,2]).permutation_poset().cover_relations()
            [[(1, 1), (2, 2)]]
            sage: P = Permutation([1,5,2,4,3])

        This should hold for any `P`::

            sage: P.permutation_poset().greene_shape() == P.RS_partition()              # needs sage.combinat sage.graphs
            True
        """
    def dict(self):
        """
        Return a dictionary corresponding to the permutation.

        EXAMPLES::

            sage: p = Permutation([2,1,3])
            sage: d = p.dict()
            sage: d[1]
            2
            sage: d[2]
            1
            sage: d[3]
            3
        """
    def action(self, a):
        """
        Return the action of the permutation ``self`` on a list ``a``.

        The action of a permutation `p \\in S_n` on an `n`-element list
        `(a_1, a_2, \\ldots, a_n)` is defined to be
        `(a_{p(1)}, a_{p(2)}, \\ldots, a_{p(n)})`.

        EXAMPLES::

            sage: p = Permutation([2,1,3])
            sage: a = list(range(3))
            sage: p.action(a)
            [1, 0, 2]
            sage: b = [1,2,3,4]
            sage: p.action(b)
            Traceback (most recent call last):
            ...
            ValueError: len(a) must equal len(self)

            sage: q = Permutation([2,3,1])
            sage: a = list(range(3))
            sage: q.action(a)
            [1, 2, 0]
        """
    def robinson_schensted(self):
        """
        Return the pair of standard tableaux obtained by running the
        Robinson-Schensted algorithm on ``self``.

        This can also be done by running
        :func:`~sage.combinat.rsk.RSK` on ``self`` (with the optional argument
        ``check_standard=True`` to return standard Young tableaux).

        EXAMPLES::

            sage: Permutation([6,2,3,1,7,5,4]).robinson_schensted()                     # needs sage.combinat
            [[[1, 3, 4], [2, 5], [6, 7]], [[1, 3, 5], [2, 6], [4, 7]]]
        """
    def left_tableau(self):
        """
        Return the left standard tableau after performing the RSK
        algorithm on ``self``.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).left_tableau()                                 # needs sage.combinat
            [[1, 2], [3], [4]]
        """
    def right_tableau(self):
        """
        Return the right standard tableau after performing the RSK
        algorithm on ``self``.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).right_tableau()                                # needs sage.combinat
            [[1, 2], [3], [4]]
        """
    def increasing_tree(self, compare=...):
        """
        Return the increasing tree associated to ``self``.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).increasing_tree()                              # needs sage.graphs
            1[., 2[3[4[., .], .], .]]
            sage: Permutation([4,1,3,2]).increasing_tree()                              # needs sage.graphs
            1[4[., .], 2[3[., .], .]]

        By passing the option ``compare=max`` one can have the decreasing
        tree instead::

            sage: Permutation([2,3,4,1]).increasing_tree(max)                           # needs sage.graphs
            4[3[2[., .], .], 1[., .]]
            sage: Permutation([2,3,1,4]).increasing_tree(max)                           # needs sage.graphs
            4[3[2[., .], 1[., .]], .]
        """
    def increasing_tree_shape(self, compare=...):
        """
        Return the shape of the increasing tree associated with the
        permutation.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).increasing_tree_shape()                        # needs sage.graphs
            [., [[[., .], .], .]]
            sage: Permutation([4,1,3,2]).increasing_tree_shape()                        # needs sage.graphs
            [[., .], [[., .], .]]

        By passing the option ``compare=max`` one can have the decreasing
        tree instead::

            sage: Permutation([2,3,4,1]).increasing_tree_shape(max)                     # needs sage.graphs
            [[[., .], .], [., .]]
            sage: Permutation([2,3,1,4]).increasing_tree_shape(max)                     # needs sage.graphs
            [[[., .], [., .]], .]
        """
    def binary_search_tree(self, left_to_right: bool = True):
        """
        Return the binary search tree associated to ``self``.

        If `w` is a word, then the binary search tree associated to `w`
        is defined as the result of starting with an empty binary tree,
        and then inserting the letters of `w` one by one into this tree.
        Here, the insertion is being done according to the method
        :meth:`~sage.combinat.binary_tree.LabelledBinaryTree.binary_search_insert`,
        and the word `w` is being traversed from left to right.

        A permutation is regarded as a word (using one-line notation),
        and thus a binary search tree associated to a permutation is
        defined.

        If the optional keyword variable ``left_to_right`` is set to
        ``False``, the word `w` is being traversed from right to left
        instead.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).binary_search_tree()                           # needs sage.graphs
            1[., 4[3[2[., .], .], .]]
            sage: Permutation([4,1,3,2]).binary_search_tree()                           # needs sage.graphs
            4[1[., 3[2[., .], .]], .]

        By passing the option ``left_to_right=False`` one can have
        the insertion going from right to left::

            sage: Permutation([1,4,3,2]).binary_search_tree(False)                      # needs sage.graphs
            2[1[., .], 3[., 4[., .]]]
            sage: Permutation([4,1,3,2]).binary_search_tree(False)                      # needs sage.graphs
            2[1[., .], 3[., 4[., .]]]

        TESTS::

            sage: Permutation([]).binary_search_tree()                                  # needs sage.graphs
            .
        """
    def binary_search_tree_shape(self, left_to_right: bool = True):
        """
        Return the shape of the binary search tree of the permutation
        (a non labelled binary tree).

        EXAMPLES::

            sage: Permutation([1,4,3,2]).binary_search_tree_shape()                     # needs sage.graphs
            [., [[[., .], .], .]]
            sage: Permutation([4,1,3,2]).binary_search_tree_shape()                     # needs sage.graphs
            [[., [[., .], .]], .]

        By passing the option ``left_to_right=False`` one can have
        the insertion going from right to left::

            sage: Permutation([1,4,3,2]).binary_search_tree_shape(False)                # needs sage.graphs
            [[., .], [., [., .]]]
            sage: Permutation([4,1,3,2]).binary_search_tree_shape(False)                # needs sage.graphs
            [[., .], [., [., .]]]
        """
    def sylvester_class(self, left_to_right: bool = False) -> Generator[Incomplete]:
        """
        Iterate over the equivalence class of the permutation ``self``
        under sylvester congruence.

        Sylvester congruence is an equivalence relation on the set `S_n`
        of all permutations of `n`. It is defined as the smallest
        equivalence relation such that every permutation of the form
        `uacvbw` with `u`, `v` and `w` being words and `a`, `b` and `c`
        being letters satisfying `a \\leq b < c` is equivalent to the
        permutation `ucavbw`. (Here, permutations are regarded as words
        by way of one-line notation.) This definition comes from [HNT2005]_,
        Definition 8, where it is more generally applied to arbitrary
        words.

        The equivalence class of a permutation `p \\in S_n` under sylvester
        congruence is called the *sylvester class* of `p`. It is an
        interval in the right permutohedron order (see
        :meth:`permutohedron_lequal`) on `S_n`.

        This is related to the
        :meth:`~sage.combinat.binary_tree.LabelledBinaryTree.sylvester_class`
        method in that the equivalence class of a permutation `\\pi` under
        sylvester congruence is the sylvester class of the right-to-left
        binary search tree of `\\pi`. However, the present method
        yields permutations, while the method on labelled binary trees
        yields plain lists.

        If the variable ``left_to_right`` is set to ``True``, the method
        instead iterates over the equivalence class of ``self`` with
        respect to the *left* sylvester congruence. The left sylvester
        congruence is easiest to define by saying that two permutations
        are equivalent under it if and only if their reverses
        (:meth:`reverse`) are equivalent under (standard) sylvester
        congruence.

        EXAMPLES:

        The sylvester class of a permutation in `S_5`::

            sage: p = Permutation([3, 5, 1, 2, 4])
            sage: sorted(p.sylvester_class())                                           # needs sage.combinat sage.graphs
            [[1, 3, 2, 5, 4],
             [1, 3, 5, 2, 4],
             [1, 5, 3, 2, 4],
             [3, 1, 2, 5, 4],
             [3, 1, 5, 2, 4],
             [3, 5, 1, 2, 4],
             [5, 1, 3, 2, 4],
             [5, 3, 1, 2, 4]]

        The sylvester class of a permutation `p` contains `p`::

            sage: all(p in p.sylvester_class() for p in Permutations(4))                # needs sage.combinat sage.graphs
            True

        Small cases::

            sage: list(Permutation([]).sylvester_class())                               # needs sage.combinat sage.graphs
            [[]]

            sage: list(Permutation([1]).sylvester_class())                              # needs sage.combinat sage.graphs
            [[1]]

        The sylvester classes in `S_3`::

            sage: [sorted(p.sylvester_class()) for p in Permutations(3)]                # needs sage.combinat sage.graphs
            [[[1, 2, 3]],
             [[1, 3, 2], [3, 1, 2]],
             [[2, 1, 3]],
             [[2, 3, 1]],
             [[1, 3, 2], [3, 1, 2]],
             [[3, 2, 1]]]

        The left sylvester classes in `S_3`::

            sage: [sorted(p.sylvester_class(left_to_right=True))                        # needs sage.combinat sage.graphs
            ....:  for p in Permutations(3)]
            [[[1, 2, 3]],
             [[1, 3, 2]],
             [[2, 1, 3], [2, 3, 1]],
             [[2, 1, 3], [2, 3, 1]],
             [[3, 1, 2]],
             [[3, 2, 1]]]

        A left sylvester class in `S_5`::

            sage: p = Permutation([4, 2, 1, 5, 3])
            sage: sorted(p.sylvester_class(left_to_right=True))                         # needs sage.combinat sage.graphs
            [[4, 2, 1, 3, 5],
             [4, 2, 1, 5, 3],
             [4, 2, 3, 1, 5],
             [4, 2, 3, 5, 1],
             [4, 2, 5, 1, 3],
             [4, 2, 5, 3, 1],
             [4, 5, 2, 1, 3],
             [4, 5, 2, 3, 1]]
        """
    def RS_partition(self):
        """
        Return the shape of the tableaux obtained by applying the RSK
        algorithm to ``self``.

        EXAMPLES::

            sage: Permutation([1,4,3,2]).RS_partition()                                 # needs sage.combinat
            [2, 1, 1]
        """
    def remove_extra_fixed_points(self):
        """
        Return the permutation obtained by removing any fixed points at
        the end of ``self``.

        However, return ``[1]`` rather than ``[]`` if ``self`` is the
        identity permutation.

        This is mostly a helper method for
        :mod:`sage.combinat.schubert_polynomial`, where it is
        used to normalize finitary permutations of
        `\\{1,2,3,\\ldots\\}`.

        EXAMPLES::

            sage: Permutation([2,1,3]).remove_extra_fixed_points()
            [2, 1]
            sage: Permutation([1,2,3,4]).remove_extra_fixed_points()
            [1]
            sage: Permutation([2,1]).remove_extra_fixed_points()
            [2, 1]
            sage: Permutation([]).remove_extra_fixed_points()
            [1]

        .. SEEALSO::

            :meth:`retract_plain`
        """
    def retract_plain(self, m):
        """
        Return the plain retract of the permutation ``self`` in `S_n`
        to `S_m`, where `m \\leq n`. If this retract is undefined, then
        ``None`` is returned.

        If `p \\in S_n` is a permutation, and `m` is a nonnegative integer
        less or equal to `n`, then the plain retract of `p` to `S_m` is
        defined only if every `i > m` satisfies `p(i) = i`. In this case,
        it is defined as the permutation written
        `(p(1), p(2), \\ldots, p(m))` in one-line notation.

        EXAMPLES::

            sage: Permutation([4,1,2,3,5]).retract_plain(4)
            [4, 1, 2, 3]
            sage: Permutation([4,1,2,3,5]).retract_plain(3)

            sage: Permutation([1,3,2,4,5,6]).retract_plain(3)
            [1, 3, 2]
            sage: Permutation([1,3,2,4,5,6]).retract_plain(2)

            sage: Permutation([1,2,3,4,5]).retract_plain(1)
            [1]
            sage: Permutation([1,2,3,4,5]).retract_plain(0)
            []

            sage: all( p.retract_plain(3) == p for p in Permutations(3) )
            True

        .. SEEALSO::

            :meth:`retract_direct_product`, :meth:`retract_okounkov_vershik`,
            :meth:`remove_extra_fixed_points`
        """
    def retract_direct_product(self, m):
        """
        Return the direct-product retract of the permutation
        ``self`` `\\in S_n` to `S_m`, where `m \\leq n`. If this retract
        is undefined, then ``None`` is returned.

        If `p \\in S_n` is a permutation, and `m` is a nonnegative integer
        less or equal to `n`, then the direct-product retract of `p` to
        `S_m` is defined only if `p([m]) = [m]`, where `[m]` denotes the
        interval `\\{1, 2, \\ldots, m\\}`. In this case, it is defined as the
        permutation written `(p(1), p(2), \\ldots, p(m))` in one-line
        notation.

        EXAMPLES::

            sage: Permutation([4,1,2,3,5]).retract_direct_product(4)
            [4, 1, 2, 3]
            sage: Permutation([4,1,2,3,5]).retract_direct_product(3)

            sage: Permutation([1,4,2,3,6,5]).retract_direct_product(5)
            sage: Permutation([1,4,2,3,6,5]).retract_direct_product(4)
            [1, 4, 2, 3]
            sage: Permutation([1,4,2,3,6,5]).retract_direct_product(3)
            sage: Permutation([1,4,2,3,6,5]).retract_direct_product(2)
            sage: Permutation([1,4,2,3,6,5]).retract_direct_product(1)
            [1]
            sage: Permutation([1,4,2,3,6,5]).retract_direct_product(0)
            []

            sage: all( p.retract_direct_product(3) == p for p in Permutations(3) )
            True

        .. SEEALSO::

            :meth:`retract_plain`, :meth:`retract_okounkov_vershik`
        """
    def retract_okounkov_vershik(self, m):
        """
        Return the Okounkov-Vershik retract of the permutation
        ``self`` `\\in S_n` to `S_m`, where `m \\leq n`.

        If `p \\in S_n` is a permutation, and `m` is a nonnegative integer
        less or equal to `n`, then the Okounkov-Vershik retract of `p` to
        `S_m` is defined as the permutation in `S_m` which sends every
        `i \\in \\{1, 2, \\ldots, m\\}` to `p^{k_i}(i)`, where `k_i` is the
        smallest positive integer `k` satisfying `p^k(i) \\leq m`.

        In other words, the Okounkov-Vershik retract of `p` is the
        permutation whose disjoint cycle decomposition is obtained by
        removing all letters strictly greater than `m` from the
        decomposition of `p` into disjoint cycles (and removing all
        cycles which are emptied in the process).

        When `m = n-1`, the Okounkov-Vershik retract (as a map
        `S_n \\to S_{n-1}`) is the map `\\widetilde{p}_n` introduced in
        Section 7 of [VO2005]_, and appears as (3.20) in
        [CST2010]_. In the general case, the Okounkov-Vershik retract
        of a permutation in `S_n` to `S_m` can be obtained by first
        taking its Okounkov-Vershik retract to `S_{n-1}`, then that
        of the resulting permutation to `S_{n-2}`, etc. until arriving
        in `S_m`.

        EXAMPLES::

            sage: Permutation([4,1,2,3,5]).retract_okounkov_vershik(4)
            [4, 1, 2, 3]
            sage: Permutation([4,1,2,3,5]).retract_okounkov_vershik(3)
            [3, 1, 2]
            sage: Permutation([4,1,2,3,5]).retract_okounkov_vershik(2)
            [2, 1]
            sage: Permutation([4,1,2,3,5]).retract_okounkov_vershik(1)
            [1]
            sage: Permutation([4,1,2,3,5]).retract_okounkov_vershik(0)
            []

            sage: Permutation([1,4,2,3,6,5]).retract_okounkov_vershik(5)
            [1, 4, 2, 3, 5]
            sage: Permutation([1,4,2,3,6,5]).retract_okounkov_vershik(4)
            [1, 4, 2, 3]
            sage: Permutation([1,4,2,3,6,5]).retract_okounkov_vershik(3)
            [1, 3, 2]
            sage: Permutation([1,4,2,3,6,5]).retract_okounkov_vershik(2)
            [1, 2]
            sage: Permutation([1,4,2,3,6,5]).retract_okounkov_vershik(1)
            [1]
            sage: Permutation([1,4,2,3,6,5]).retract_okounkov_vershik(0)
            []

            sage: Permutation([6,5,4,3,2,1]).retract_okounkov_vershik(5)
            [1, 5, 4, 3, 2]
            sage: Permutation([6,5,4,3,2,1]).retract_okounkov_vershik(4)
            [1, 2, 4, 3]

            sage: Permutation([1,5,2,6,3,7,4,8]).retract_okounkov_vershik(4)
            [1, 3, 2, 4]

            sage: all( p.retract_direct_product(3) == p for p in Permutations(3) )
            True

        .. SEEALSO::

            :meth:`retract_plain`, :meth:`retract_direct_product`
        """
    def hyperoctahedral_double_coset_type(self):
        """
        Return the coset-type of ``self`` as a partition.

        ``self`` must be a permutation of even size `2n`.  The coset-type
        determines the double class of the permutation, that is its image in
        `H_n \\backslash S_{2n} / H_n`, where `H_n` is the `n`-th
        hyperoctahedral group.

        The coset-type is determined as follows. Consider the perfect matching
        `\\{\\{1,2\\},\\{3,4\\},\\dots,\\{2n-1,2n\\}\\}` and its image by ``self``, and
        draw them simultaneously as edges of a graph whose vertices are labeled
        by `1,2,\\dots,2n`. The coset-type is the ordered sequence of the
        semi-lengths of the cycles of this graph (see Chapter VII of [Mac1995]_ for
        more details, particularly Section VII.2).

        EXAMPLES::

            sage: # needs sage.combinat
            sage: p = Permutation([3, 4, 6, 1, 5, 7, 2, 8])
            sage: p.hyperoctahedral_double_coset_type()
            [3, 1]
            sage: all(p.hyperoctahedral_double_coset_type() ==
            ....:     p.inverse().hyperoctahedral_double_coset_type()
            ....:     for p in Permutations(4))
            True
            sage: Permutation([]).hyperoctahedral_double_coset_type()
            []
            sage: Permutation([3,1,2]).hyperoctahedral_double_coset_type()
            Traceback (most recent call last):
            ...
            ValueError: [3, 1, 2] is a permutation of odd size and has no coset-type
        """
    def shifted_concatenation(self, other, side: str = 'right'):
        '''
        Return the right (or left) shifted concatenation of ``self``
        with a permutation ``other``. These operations are also known
        as the Loday-Ronco over and under operations.

        INPUT:

        - ``other`` -- a permutation, a list, a tuple, or any iterable
          representing a permutation

        - ``side`` -- string (default: ``\'right\'``); ``\'left\'`` or ``\'right\'``

        OUTPUT:

        If ``side`` is ``\'right\'``, the method returns the permutation
        obtained by concatenating ``self`` with the letters of ``other``
        incremented by the size of ``self``. This is what is called
        ``side / other`` in [LR0102066]_, and denoted as the "over"
        operation.
        Otherwise, i. e., when ``side`` is ``\'left\'``, the method
        returns the permutation obtained by concatenating the letters
        of ``other`` incremented by the size of ``self`` with ``self``.
        This is what is called ``side \\ other`` in [LR0102066]_
        (which seems to use the `(\\sigma \\pi)(i) = \\pi(\\sigma(i))`
        convention for the product of permutations).

        EXAMPLES::

            sage: Permutation([]).shifted_concatenation(Permutation([]), "right")
            []
            sage: Permutation([]).shifted_concatenation(Permutation([]), "left")
            []
            sage: Permutation([2, 4, 1, 3]).shifted_concatenation(Permutation([3, 1, 2]), "right")
            [2, 4, 1, 3, 7, 5, 6]
            sage: Permutation([2, 4, 1, 3]).shifted_concatenation(Permutation([3, 1, 2]), "left")
            [7, 5, 6, 2, 4, 1, 3]
        '''
    def shifted_shuffle(self, other):
        """
        Return the shifted shuffle of two permutations ``self`` and ``other``.

        INPUT:

        - ``other`` -- a permutation, a list, a tuple, or any iterable
          representing a permutation

        OUTPUT:

        The list of the permutations appearing in the shifted
        shuffle of the permutations ``self`` and ``other``.

        EXAMPLES::

            sage: # needs sage.graphs sage.modules
            sage: Permutation([]).shifted_shuffle(Permutation([]))
            [[]]
            sage: Permutation([1, 2, 3]).shifted_shuffle(Permutation([1]))
            [[4, 1, 2, 3], [1, 2, 3, 4], [1, 2, 4, 3], [1, 4, 2, 3]]
            sage: Permutation([1, 2]).shifted_shuffle(Permutation([2, 1]))
            [[4, 1, 3, 2], [4, 3, 1, 2], [1, 4, 3, 2],
             [1, 4, 2, 3], [1, 2, 4, 3], [4, 1, 2, 3]]
            sage: Permutation([1]).shifted_shuffle([1])
            [[2, 1], [1, 2]]
            sage: p = Permutation([3, 1, 5, 4, 2])
            sage: len(p.shifted_shuffle(Permutation([2, 1, 4, 3])))
            126

        The shifted shuffle product is associative. We can test this on an
        admittedly toy example::

            sage: all( all( all( sorted(flatten([abs.shifted_shuffle(c)                 # needs sage.graphs sage.modules
            ....:                                for abs in a.shifted_shuffle(b)]))
            ....:                == sorted(flatten([a.shifted_shuffle(bcs)
            ....:                                   for bcs in b.shifted_shuffle(c)]))
            ....:                for c in Permutations(2) )
            ....:           for b in Permutations(2) )
            ....:      for a in Permutations(2) )
            True

        The ``shifted_shuffle`` method on permutations gives the same
        permutations as the ``shifted_shuffle`` method on words (but is
        faster)::

            sage: all( all( sorted(p1.shifted_shuffle(p2))                              # needs sage.combinat sage.graphs sage.modules sage.rings.finite_rings
            ....:           == sorted([Permutation(p) for p in
            ....:                      Word(p1).shifted_shuffle(Word(p2))])
            ....:           for p2 in Permutations(3) )
            ....:      for p1 in Permutations(2) )
            True
        """
    def nth_roots(self, n) -> Generator[Incomplete, None, Incomplete]:
        """
        Return all `n`-th roots of ``self`` (as a generator).

        An `n`-th root of the permutation `\\sigma` is a permutation `\\gamma` such that `\\gamma^n = \\sigma`.

        Note that the number of `n`-th roots only depends on the cycle type of ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: sigma = Permutations(5).identity()
            sage: list(sigma.nth_roots(3))
            [[1, 4, 3, 5, 2], [1, 5, 3, 2, 4], [1, 2, 4, 5, 3], [1, 2, 5, 3, 4],
             [4, 2, 3, 5, 1], [5, 2, 3, 1, 4], [3, 2, 5, 4, 1], [5, 2, 1, 4, 3],
             [2, 5, 3, 4, 1], [5, 1, 3, 4, 2], [2, 3, 1, 4, 5], [3, 1, 2, 4, 5],
             [2, 4, 3, 1, 5], [4, 1, 3, 2, 5], [3, 2, 4, 1, 5], [4, 2, 1, 3, 5],
             [1, 3, 4, 2, 5], [1, 4, 2, 3, 5], [1, 3, 5, 4, 2], [1, 5, 2, 4, 3],
             [1, 2, 3, 4, 5]]
            sage: sigma = Permutation('(1, 3)')
            sage: list(sigma.nth_roots(2))
            []

        For `n \\geq 6`, this algorithm begins to be more efficient than naive search
        (look at all permutations and test their `n`-th power).

        .. SEEALSO::

            * :meth:`has_nth_root`
            * :meth:`number_of_nth_roots`

        TESTS:

        We compute the number of square roots of the identity (i.e. involutions in `S_n`, :oeis:`A000085`)::

            sage: # needs sage.combinat
            sage: [len(list(Permutations(n).identity().nth_roots(2))) for n in range(2,8)]
            [2, 4, 10, 26, 76, 232]
            sage: list(Permutation('(1)').nth_roots(2))
            [[1]]
            sage: list(Permutation('').nth_roots(2))
            [[]]
            sage: sigma = Permutations(6).random_element()
            sage: list(sigma.nth_roots(1)) == [sigma]
            True
            sage: list(Permutations(4).identity().nth_roots(-1))
            Traceback (most recent call last):
            ...
            ValueError: n must be at least 1
        """
    def has_nth_root(self, n) -> bool:
        """
        Check if ``self`` has `n`-th roots.

        An `n`-th root of the permutation `\\sigma` is a permutation `\\gamma` such that `\\gamma^n = \\sigma`.

        Note that the number of `n`-th roots only depends on the cycle type of ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: sigma = Permutations(5).identity()
            sage: sigma.has_nth_root(3)
            True
            sage: sigma = Permutation('(1, 3)')
            sage: sigma.has_nth_root(2)
            False

        .. SEEALSO::

            * :meth:`nth_roots`
            * :meth:`number_of_nth_roots`

        TESTS:

        We compute the number of permutations that have square roots (i.e. squares in `S_n`, :oeis:`A003483`)::

            sage: # needs sage.combinat
            sage: [len([p for p in Permutations(n) if p.has_nth_root(2)]) for n in range(2, 7)]
            [1, 3, 12, 60, 270]
            sage: Permutation('(1)').has_nth_root(2)
            True
            sage: Permutation('').has_nth_root(2)
            True
            sage: sigma = Permutations(6).random_element()
            sage: sigma.has_nth_root(1)
            True
            sage: Permutations(4).identity().has_nth_root(-1)
            Traceback (most recent call last):
            ...
            ValueError: n must be at least 1
        """
    def number_of_nth_roots(self, n):
        """
        Return the number of `n`-th roots of ``self``.

        An `n`-th root of the permutation `\\sigma` is a permutation `\\gamma` such that `\\gamma^n = \\sigma`.

        Note that the number of `n`-th roots only depends on the cycle type of ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: Sigma = Permutations(5).identity()
            sage: Sigma.number_of_nth_roots(3)
            21
            sage: Sigma = Permutation('(1, 3)')
            sage: Sigma.number_of_nth_roots(2)
            0

        .. SEEALSO::

            * :meth:`nth_roots`
            * :meth:`has_nth_root`

        TESTS:

        We compute the number of square roots of the identity (i.e. involutions in `S_n`, :oeis:`A000085`), then the number of cubic roots::

            sage: # needs sage.combinat
            sage: [Permutations(n).identity().number_of_nth_roots(2) for n in range(2, 10)]
            [2, 4, 10, 26, 76, 232, 764, 2620]
            sage: [Permutations(n).identity().number_of_nth_roots(3) for n in range(2, 10)]
            [1, 3, 9, 21, 81, 351, 1233, 5769]
            sage: Permutation('(1)').number_of_nth_roots(2)
            1
            sage: Permutation('').number_of_nth_roots(2)
            1
            sage: Sigma = Permutations(6).random_element()
            sage: Sigma.number_of_nth_roots(1)
            1
            sage: Permutations(4).identity().number_of_nth_roots(-1)
            Traceback (most recent call last):
            ...
            ValueError: n must be at least 1
        """

class Permutations(UniqueRepresentation, Parent):
    """
    Permutations.

    ``Permutations(n)`` returns the class of permutations of ``n``, if ``n``
    is an integer, list, set, or string.

    ``Permutations(n, k)`` returns the class of length-``k`` partial
    permutations of ``n`` (where ``n`` is any of the above things); ``k``
    must be a nonnegative integer. A length-`k` partial permutation of `n`
    is defined as a `k`-tuple of pairwise distinct elements of
    `\\{ 1, 2, \\ldots, n \\}`.

    Valid keyword arguments are: 'descents', 'bruhat_smaller',
    'bruhat_greater', 'recoils_finer', 'recoils_fatter', 'recoils',
    and 'avoiding'. With the exception of 'avoiding', you cannot
    specify ``n`` or ``k`` along with a keyword.

    ``Permutations(descents=(list,n))`` returns the class of permutations of
    `n` with descents in the positions specified by ``list``. This uses the
    slightly nonstandard convention that the images of `1,2,...,n` under the
    permutation are regarded as positions `0,1,...,n-1`, so for example the
    presence of `1` in ``list`` signifies that the permutations `\\pi` should
    satisfy `\\pi(2) > \\pi(3)`.
    Note that ``list`` is supposed to be a list of positions of the descents,
    not the descents composition.  It does *not* return the class of
    permutations with descents composition ``list``.

    ``Permutations(bruhat_smaller=p)`` and ``Permutations(bruhat_greater=p)``
    return the class of permutations smaller-or-equal or greater-or-equal,
    respectively, than the given permutation ``p`` in the Bruhat order.
    (The Bruhat order is defined in
    :meth:`~sage.combinat.permutation.Permutation.bruhat_lequal`.
    It is also referred to as the *strong* Bruhat order.)

    ``Permutations(recoils=p)`` returns the class of permutations whose
    recoils composition is ``p``. Unlike the ``descents=(list, n)`` syntax,
    this actually takes a *composition* as input.

    ``Permutations(recoils_fatter=p)`` and ``Permutations(recoils_finer=p)``
    return the class of permutations whose recoils composition is fatter or
    finer, respectively, than the given composition ``p``.

    ``Permutations(n, avoiding=P)`` returns the class of permutations of ``n``
    avoiding ``P``. Here ``P`` may be a single permutation or a list of
    permutations; the returned class will avoid all patterns in ``P``.

    EXAMPLES::

        sage: p = Permutations(3); p
        Standard permutations of 3
        sage: p.list()
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    ::

        sage: p = Permutations(3, 2); p
        Permutations of {1,...,3} of length 2
        sage: p.list()
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]

    ::

        sage: p = Permutations(['c', 'a', 't']); p
        Permutations of the set ['c', 'a', 't']
        sage: p.list()
        [['c', 'a', 't'],
         ['c', 't', 'a'],
         ['a', 'c', 't'],
         ['a', 't', 'c'],
         ['t', 'c', 'a'],
         ['t', 'a', 'c']]

    ::

        sage: p = Permutations(['c', 'a', 't'], 2); p
        Permutations of the set ['c', 'a', 't'] of length 2
        sage: p.list()
        [['c', 'a'], ['c', 't'], ['a', 'c'], ['a', 't'], ['t', 'c'], ['t', 'a']]

    ::

        sage: p = Permutations([1,1,2]); p
        Permutations of the multi-set [1, 1, 2]
        sage: p.list()
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

    ::

        sage: p = Permutations([1,1,2], 2); p
        Permutations of the multi-set [1, 1, 2] of length 2
        sage: p.list()                                                                  # needs sage.libs.gap
        [[1, 1], [1, 2], [2, 1]]

    ::

        sage: p = Permutations(descents=([1], 4)); p
        Standard permutations of 4 with descents [1]
        sage: p.list()                                                                  # needs sage.graphs sage.modules
        [[2, 4, 1, 3], [3, 4, 1, 2], [1, 4, 2, 3], [1, 3, 2, 4], [2, 3, 1, 4]]

    ::

        sage: p = Permutations(bruhat_smaller=[1,3,2,4]); p
        Standard permutations that are less than or equal
        to [1, 3, 2, 4] in the Bruhat order
        sage: p.list()
        [[1, 2, 3, 4], [1, 3, 2, 4]]

    ::

        sage: p = Permutations(bruhat_greater=[4,2,3,1]); p
        Standard permutations that are greater than or equal
        to [4, 2, 3, 1] in the Bruhat order
        sage: p.list()
        [[4, 2, 3, 1], [4, 3, 2, 1]]

    ::

        sage: p = Permutations(recoils_finer=[2,1]); p
        Standard permutations whose recoils composition is finer than [2, 1]
        sage: p.list()                                                                  # needs sage.graphs sage.modules
        [[3, 1, 2], [1, 2, 3], [1, 3, 2]]

    ::

        sage: p = Permutations(recoils_fatter=[2,1]); p
        Standard permutations whose recoils composition is fatter than [2, 1]
        sage: p.list()                                                                  # needs sage.graphs sage.modules
        [[3, 1, 2], [3, 2, 1], [1, 3, 2]]

    ::

        sage: p = Permutations(recoils=[2,1]); p
        Standard permutations whose recoils composition is [2, 1]
        sage: p.list()                                                                  # needs sage.graphs sage.modules
        [[3, 1, 2], [1, 3, 2]]

    ::

        sage: p = Permutations(4, avoiding=[1,3,2]); p
        Standard permutations of 4 avoiding [[1, 3, 2]]
        sage: p.list()
        [[4, 1, 2, 3],
         [4, 2, 1, 3],
         [4, 2, 3, 1],
         [4, 3, 1, 2],
         [4, 3, 2, 1],
         [3, 4, 1, 2],
         [3, 4, 2, 1],
         [2, 3, 4, 1],
         [3, 2, 4, 1],
         [1, 2, 3, 4],
         [2, 1, 3, 4],
         [2, 3, 1, 4],
         [3, 1, 2, 4],
         [3, 2, 1, 4]]

    ::

        sage: p = Permutations(5, avoiding=[[3,4,1,2], [4,2,3,1]]); p
        Standard permutations of 5 avoiding [[3, 4, 1, 2], [4, 2, 3, 1]]
        sage: p.cardinality()                                                           # needs sage.combinat
        88
        sage: p.random_element().parent() is p                                          # needs sage.combinat
        True
    """
    @staticmethod
    def __classcall_private__(cls, n=None, k=None, **kwargs):
        """
        Return the correct parent based upon input.

        EXAMPLES::

            sage: Permutations()
            Standard permutations
            sage: Permutations(5, 3)
            Permutations of {1,...,5} of length 3
            sage: Permutations([1,2,3,4,6])
            Permutations of the set [1, 2, 3, 4, 6]
            sage: Permutations([1,2,3,4,5])
            Standard permutations of 5
        """
    Element = Permutation
    class options(GlobalOptions):
        """
        Set the global options for elements of the permutation class. The
        defaults are for permutations to be displayed in list notation and
        the multiplication done from left to right (like in GAP) -- that
        is, `(\\pi \\psi)(i) = \\psi(\\pi(i))` for all `i`.

        .. NOTE::

            These options have no effect on permutation group elements.

        @OPTIONS@

        EXAMPLES::

            sage: p213 = Permutation([2,1,3])
            sage: p312 = Permutation([3,1,2])
            sage: Permutations.options(mult='l2r', display='list')
            sage: Permutations.options.display
            list
            sage: p213
            [2, 1, 3]
            sage: Permutations.options.display='cycle'
            sage: p213
            (1,2)
            sage: Permutations.options.display='singleton'
            sage: p213
            (1,2)(3)
            sage: Permutations.options.display='list'

        ::

            sage: Permutations.options.mult
            l2r
            sage: p213*p312
            [1, 3, 2]
            sage: Permutations.options.mult='r2l'
            sage: p213*p312
            [3, 2, 1]
            sage: Permutations.options._reset()
        """
        NAME: str
        module: str
        display: Incomplete
        latex: Incomplete
        latex_empty_str: Incomplete
        generator_name: Incomplete
        mult: Incomplete

class Permutations_nk(Permutations):
    """
    Length-`k` partial permutations of `\\{1, 2, \\ldots, n\\}`.
    """
    n: Incomplete
    def __init__(self, n, k) -> None:
        """
        TESTS::

            sage: P = Permutations(3,2)
            sage: TestSuite(P).run()
        """
    class Element(ClonableArray):
        """
        A length-`k` partial permutation of `[n]`.
        """
        def check(self) -> None:
            """
            Verify that ``self`` is a valid length-`k` partial
            permutation of `[n]`.

            EXAMPLES::

                sage: S = Permutations(4, 2)
                sage: elt = S([3, 1])
                sage: elt.check()
            """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: [1,2] in Permutations(3,2)
            True
            sage: [1,1] in Permutations(3,2)
            False
            sage: [3,2,1] in Permutations(3,2)
            False
            sage: [3,1] in Permutations(3,2)
            True
        """
    def __iter__(self) -> Iterator[Permutation]:
        """
        EXAMPLES::

            sage: [p for p in Permutations(3,2)]
            [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
            sage: [p for p in Permutations(3,0)]
            [[]]
            sage: [p for p in Permutations(3,4)]
            []
        """
    def cardinality(self) -> Integer:
        """
        EXAMPLES::

            sage: Permutations(3,0).cardinality()
            1
            sage: Permutations(3,1).cardinality()
            3
            sage: Permutations(3,2).cardinality()
            6
            sage: Permutations(3,3).cardinality()
            6
            sage: Permutations(3,4).cardinality()
            0
        """
    def random_element(self):
        """
        EXAMPLES::

            sage: s = Permutations(3,2).random_element()
            sage: s in Permutations(3,2)
            True
        """

class Permutations_mset(Permutations):
    """
    Permutations of a multiset `M`.

    A permutation of a multiset `M` is represented by a list that
    contains exactly the same elements as `M` (with the same
    multiplicities), but possibly in different order. If `M` is
    a proper set there are `|M| !` such permutations.
    Otherwise, if the first element appears `k_1` times, the
    second element appears `k_2` times and so on, the number
    of permutations is `|M|! / (k_1! k_2! \\ldots)`, which
    is sometimes called a multinomial coefficient.

    EXAMPLES::

        sage: mset = [1,1,2,2,2]
        sage: from sage.combinat.permutation import Permutations_mset
        sage: P = Permutations_mset(mset); P
        Permutations of the multi-set [1, 1, 2, 2, 2]
        sage: sorted(P)
        [[1, 1, 2, 2, 2],
         [1, 2, 1, 2, 2],
         [1, 2, 2, 1, 2],
         [1, 2, 2, 2, 1],
         [2, 1, 1, 2, 2],
         [2, 1, 2, 1, 2],
         [2, 1, 2, 2, 1],
         [2, 2, 1, 1, 2],
         [2, 2, 1, 2, 1],
         [2, 2, 2, 1, 1]]

        sage: # needs sage.modules
        sage: MS = MatrixSpace(GF(2), 2, 2)
        sage: A = MS([1,0,1,1])
        sage: rows = A.rows()
        sage: rows[0].set_immutable()
        sage: rows[1].set_immutable()
        sage: P = Permutations_mset(rows); P
        Permutations of the multi-set [(1, 0), (1, 1)]
        sage: sorted(P)
        [[(1, 0), (1, 1)], [(1, 1), (1, 0)]]
    """
    @staticmethod
    def __classcall_private__(cls, mset):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(['c','a','c'])
            sage: S2 = Permutations(('c','a','c'))
            sage: S1 is S2
            True
        """
    mset: Incomplete
    def __init__(self, mset) -> None:
        """
        TESTS::

            sage: S = Permutations(['c','a','c'])
            sage: TestSuite(S).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: p = Permutations([1,2,2])
            sage: [1,2,2] in p
            True
            sage: [] in p
            False
            sage: [2,2] in p
            False
            sage: [1,1] in p
            False
            sage: [2,1] in p
            False
            sage: [2,1,2] in p
            True
        """
    class Element(ClonableArray):
        """
        A permutation of an arbitrary multiset.
        """
        def check(self) -> None:
            """
            Verify that ``self`` is a valid permutation of the underlying
            multiset.

            EXAMPLES::

                sage: S = Permutations(['c','a','c'])
                sage: elt = S(['c','c','a'])
                sage: elt.check()
            """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: [ p for p in Permutations(['c','t','t'])] # indirect doctest
            [['c', 't', 't'], ['t', 'c', 't'], ['t', 't', 'c']]

        TESTS:

        The empty multiset::

            sage: list(sage.combinat.permutation.Permutations_mset([]))
            [[]]
        """
    def cardinality(self):
        """
        Return the cardinality of the set.

        EXAMPLES::

            sage: Permutations([1,2,2]).cardinality()
            3
            sage: Permutations([1,1,2,2,2]).cardinality()
            10
        """
    def rank(self, p):
        '''
        Return the rank of ``p`` in lexicographic order.

        INPUT:

        - ``p`` -- a permutation of `M`

        ALGORITHM:

        The algorithm uses the recurrence from the solution to exercise 4 in
        [Knu2011]_, Section 7.2.1.2:

        .. MATH::

            \\mathrm{rank}(p_1 \\ldots p_n) =
            \\mathrm{rank}(p_2 \\ldots p_n)
            + \\frac{1}{n} \\genfrac{(}{)}{0pt}{0}{n}{n_1, \\ldots, n_t}
                \\sum_{j=1}^t n_j \\left[ x_j < p_1 \\right],

        where `x_j, n_j` are the distinct elements of `p` with their
        multiplicities, `n` is the sum of `n_1, \\ldots, n_t`,
        `\\genfrac{(}{)}{0pt}{1}{n}{n_1, \\ldots, n_t}` is the multinomial
        coefficient `\\frac{n!}{n_1! \\ldots n_t!}`, and
        `\\sum_{j=1}^t n_j \\left[ x_j < p_1 \\right]` means "the number of
        elements to the right of the first element that are less than the first
        element".

        EXAMPLES::

            sage: mset = [1, 1, 2, 3, 4, 5, 5, 6, 9]
            sage: p = Permutations(mset)
            sage: p.rank(list(sorted(mset)))
            0
            sage: p.rank(list(reversed(sorted(mset)))) == p.cardinality() - 1
            True
            sage: p.rank([3, 1, 4, 1, 5, 9, 2, 6, 5])
            30991

        TESTS::

            sage: from sage.combinat.permutation import Permutations_mset
            sage: p = Permutations_mset([])
            sage: p.rank([])
            0
            sage: p = Permutations_mset([1, 1, 2, 3, 4, 5, 5, 6, 9])
            sage: p.rank([1, 2, 3, 4, 5, 6, 9])
            Traceback (most recent call last):
            ...
            ValueError: Invalid permutation

        Try with greater-than-unity multiplicity in the least and greatest
        elements::

            sage: mset = list(range(10)) * 3
            sage: p = Permutations_mset(mset)
            sage: p.rank(list(sorted(mset)))
            0
            sage: p.rank(list(reversed(sorted(mset))))
            4386797336285844479999999
            sage: p.cardinality()
            4386797336285844480000000

        Should match ``StandardPermutations_n`` when `M` is the set
        `\\{1, 2, \\ldots, n\\}`::

            sage: ps = Permutations(4)
            sage: pm = Permutations_mset(list(range(1, 5)))
            sage: ps.rank([2, 3, 1, 4]) == pm.rank([2, 3, 1, 4])
            True
        '''
    def unrank(self, r):
        """
        Return the permutation of `M` having lexicographic rank ``r``.

        INPUT:

        - ``r`` -- integer between ``0`` and ``self.cardinality()-1``
          inclusive

        ALGORITHM:

        The algorithm is adapted from the solution to exercise 4 in [Knu2011]_,
        Section 7.2.1.2.

        EXAMPLES::

            sage: mset = [1, 1, 2, 3, 4, 5, 5, 6, 9]
            sage: p = Permutations(mset)
            sage: p.unrank(30991)
            [3, 1, 4, 1, 5, 9, 2, 6, 5]
            sage: p.rank(p.unrank(10))
            10
            sage: p.unrank(0) == list(sorted(mset))
            True
            sage: p.unrank(p.cardinality()-1) == list(reversed(sorted(mset)))
            True

        TESTS::

            sage: from sage.combinat.permutation import Permutations_mset
            sage: p = Permutations_mset([])
            sage: p.unrank(0)
            []
            sage: p.unrank(1)
            Traceback (most recent call last):
            ...
            ValueError: r must be between 0 and 0 inclusive
            sage: p = Permutations_mset([1, 1, 2, 3, 4, 5, 5, 6, 9])
            sage: p.unrank(-1)
            Traceback (most recent call last):
            ...
            ValueError: r must be between 0 and 90719 inclusive
            sage: p.unrank(p.cardinality())
            Traceback (most recent call last):
            ...
            ValueError: r must be between 0 and 90719 inclusive

        Try with a cardinality that exceeds the precise integer range of a
        float::

            sage: mset = list(range(10)) * 3
            sage: p = Permutations_mset(mset)
            sage: p.unrank(p.rank(mset)) == mset
            True
            sage: p.unrank(p.cardinality()-1) == list(reversed(sorted(mset)))
            True

        Exhaustive check of roundtrip and lexicographic order for a single
        multiset::

            sage: p = Permutations_mset([2, 2, 3, 3, 3, 5, 5, 5, 5, 5])
            sage: prev = None
            sage: for rank, perm in enumerate(p):
            ....:     perm = tuple(perm)
            ....:     assert p.rank(perm) == rank, (rank, perm, p.rank(perm))
            ....:     assert tuple(p.unrank(rank)) == perm, (rank, perm, p.unrank(rank))
            ....:     assert prev is None or prev < perm
            ....:     prev = perm

        Should match ``StandardPermutations_n`` when `M` is the set
        `\\{1, 2, \\ldots, n\\}`::

            sage: ps = Permutations(4)
            sage: pm = Permutations_mset(list(range(1, 5)))
            sage: ps.unrank(5) == pm.unrank(5)
            True
        """

class Permutations_set(Permutations):
    '''
    Permutations of an arbitrary given finite set.

    Here, a "permutation of a finite set `S`" means a list of the
    elements of `S` in which every element of `S` occurs exactly
    once. This is not to be confused with bijections from `S` to
    `S`, which are also often called permutations in literature.
    '''
    @staticmethod
    def __classcall_private__(cls, s):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(['c','a','t'])
            sage: S2 = Permutations(('c','a','t'))
            sage: S1 is S2
            True
        """
    def __init__(self, s) -> None:
        """
        TESTS::

            sage: S = Permutations(['c','a','t'])
            sage: TestSuite(S).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: p = Permutations([4,-1,'cthulhu'])
            sage: [4,-1,'cthulhu'] in p
            True
            sage: [] in p
            False
            sage: [4,'cthulhu','fhtagn'] in p
            False
            sage: [4,'cthulhu',4,-1] in p
            False
            sage: [-1,'cthulhu',4] in p
            True
        """
    class Element(ClonableArray):
        """
        A permutation of an arbitrary set.
        """
        def check(self) -> None:
            """
            Verify that ``self`` is a valid permutation of the underlying
            set.

            EXAMPLES::

                sage: S = Permutations(['c','a','t'])
                sage: elt = S(['t','c','a'])
                sage: elt.check()
            """
    def __iter__(self) -> Iterator:
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: S = Permutations(['c','a','t'])
            sage: S.list()
            [['c', 'a', 't'],
             ['c', 't', 'a'],
             ['a', 'c', 't'],
             ['a', 't', 'c'],
             ['t', 'c', 'a'],
             ['t', 'a', 'c']]
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of the set.

        EXAMPLES::

            sage: Permutations([1,2,3]).cardinality()
            6
        """
    def random_element(self):
        """
        EXAMPLES::

            sage: s = Permutations([1,2,3]).random_element()
            sage: s.parent() is Permutations([1,2,3])
            True
        """

class Permutations_msetk(Permutations_mset):
    """
    Length-`k` partial permutations of a multiset.

    A length-`k` partial permutation of a multiset `M` is
    represented by a list of length `k` whose entries are
    elements of `M`, appearing in the list with a multiplicity
    not higher than their respective multiplicity in `M`.
    """
    @staticmethod
    def __classcall__(cls, mset, k):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(['c','a','c'], 2)
            sage: S2 = Permutations(('c','a','c'), 2)
            sage: S1 is S2
            True
        """
    def __init__(self, mset, k) -> None:
        """
        TESTS::

            sage: P = Permutations([1,2,2],2)
            sage: TestSuite(P).run()                                                    # needs sage.libs.gap
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: p = Permutations([1,2,2],2)
            sage: [1,2,2] in p
            False
            sage: [2,2] in p
            True
            sage: [1,1] in p
            False
            sage: [2,1] in p
            True
        """
    def cardinality(self):
        """
        Return the cardinality of the set.

        EXAMPLES::

            sage: Permutations([1,2,2], 2).cardinality()                                # needs sage.libs.gap
            3
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations([1,2,2], 2).list()                                       # needs sage.libs.gap
            [[1, 2], [2, 1], [2, 2]]
        """

class Permutations_setk(Permutations_set):
    '''
    Length-`k` partial permutations of an arbitrary given finite set.

    Here, a "length-`k` partial permutation of a finite set `S`" means
    a list of length `k` whose entries are pairwise distinct and all
    belong to `S`.
    '''
    @staticmethod
    def __classcall_private__(cls, s, k):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(['c','a','t'], 2)
            sage: S2 = Permutations(('c','a','t'), 2)
            sage: S1 is S2
            True
        """
    def __init__(self, s, k) -> None:
        """
        TESTS::

            sage: P = Permutations([1,2,4],2)
            sage: TestSuite(P).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: p = Permutations([1,2,4],2)
            sage: [1,2,4] in p
            False
            sage: [2,2] in p
            False
            sage: [1,4] in p
            True
            sage: [2,1] in p
            True
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [i for i in Permutations([1,2,4],2)]
            [[1, 2], [1, 4], [2, 1], [2, 4], [4, 1], [4, 2]]
        """
    def random_element(self):
        """
        EXAMPLES::

            sage: s = Permutations([1,2,4], 2).random_element()
            sage: s in Permutations([1,2,4], 2)
            True
        """

class Arrangements(Permutations):
    '''
    An arrangement of a multiset ``mset`` is an ordered selection
    without repetitions. It is represented by a list that contains
    only elements from ``mset``, but maybe in a different order.

    ``Arrangements`` returns the combinatorial class of
    arrangements of the multiset ``mset`` that contain ``k`` elements.

    EXAMPLES::

        sage: mset = [1,1,2,3,4,4,5]
        sage: Arrangements(mset, 2).list()                                              # needs sage.libs.gap
        [[1, 1],
         [1, 2],
         [1, 3],
         [1, 4],
         [1, 5],
         [2, 1],
         [2, 3],
         [2, 4],
         [2, 5],
         [3, 1],
         [3, 2],
         [3, 4],
         [3, 5],
         [4, 1],
         [4, 2],
         [4, 3],
         [4, 4],
         [4, 5],
         [5, 1],
         [5, 2],
         [5, 3],
         [5, 4]]
         sage: Arrangements(mset, 2).cardinality()                                      # needs sage.libs.gap
         22
         sage: Arrangements( ["c","a","t"], 2 ).list()
         [[\'c\', \'a\'], [\'c\', \'t\'], [\'a\', \'c\'], [\'a\', \'t\'], [\'t\', \'c\'], [\'t\', \'a\']]
         sage: Arrangements( ["c","a","t"], 3 ).list()
         [[\'c\', \'a\', \'t\'],
          [\'c\', \'t\', \'a\'],
          [\'a\', \'c\', \'t\'],
          [\'a\', \'t\', \'c\'],
          [\'t\', \'c\', \'a\'],
          [\'t\', \'a\', \'c\']]
    '''
    @staticmethod
    def __classcall_private__(cls, mset, k):
        '''
        Return the correct parent.

        EXAMPLES::

            sage: A1 = Arrangements( ["c","a","t"], 2)
            sage: A2 = Arrangements( ("c","a","t"), 2)
            sage: A1 is A2
            True
        '''
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: A = Arrangements([1,1,2,3,4,4,5], 2)
            sage: A.cardinality()                                                       # needs sage.libs.gap
            22
        """

class Arrangements_msetk(Arrangements, Permutations_msetk):
    """
    Arrangements of length `k` of a multiset `M`.
    """
class Arrangements_setk(Arrangements, Permutations_setk):
    """
    Arrangements of length `k` of a set `S`.
    """

class StandardPermutations_all(Permutations):
    """
    All standard permutations.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: SP = Permutations()
            sage: TestSuite(SP).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [] in Permutations()
            True
            sage: [1] in Permutations()
            True
            sage: [2] in Permutations()
            False
            sage: [1,2] in Permutations()
            True
            sage: [2,1] in Permutations()
            True
            sage: [1,2,2] in Permutations()
            False
            sage: [3,1,5,2] in Permutations()
            False
            sage: [3,4,1,5,2] in Permutations()
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        TESTS::

            sage: it = iter(Permutations())
            sage: [next(it) for i in range(10)]
            [[], [1], [1, 2], [2, 1], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
    def graded_component(self, n):
        """
        Return the graded component.

        EXAMPLES::

            sage: P = Permutations()
            sage: P.graded_component(4) == Permutations(4)
            True
        """

class StandardPermutations_n_abstract(Permutations):
    """
    Abstract base class for subsets of permutations of the
    set `\\{1, 2, \\ldots, n\\}`.

    .. WARNING::

        Anything inheriting from this class should override the
        ``__contains__`` method.
    """
    n: Incomplete
    def __init__(self, n, category=None) -> None:
        """
        TESTS:

        We skip the descent and reduced word methods because they do
        not respect the ordering for multiplication::

            sage: SP = Permutations(3)
            sage: TestSuite(SP).run(skip=['_test_reduced_word', '_test_has_descent'])

            sage: SP.options.mult='r2l'
            sage: TestSuite(SP).run()
            sage: SP.options._reset()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [] in Permutations(0)
            True
            sage: [1,2] in Permutations(2)
            True
            sage: [1,2] in Permutations(3)
            False
            sage: [3,2,1] in Permutations(3)
            True
        """

class StandardPermutations_n(StandardPermutations_n_abstract):
    """
    Permutations of the set `\\{1, 2, \\ldots, n\\}`.

    These are also called permutations of size `n`, or the elements
    of the `n`-th symmetric group.

    .. TODO::

        Have a :meth:`reduced_word` which works in both multiplication
        conventions.
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: P = Permutations(5)
            sage: P.options.mult = 'r2l'
            sage: TestSuite(P).run(skip='_test_descents')
            sage: P.options._reset()
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: [p for p in Permutations(0)]
            [[]]
            sage: [p for p in Permutations(3)]
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
    def as_permutation_group(self):
        """
        Return ``self`` as a permutation group.

        EXAMPLES::

            sage: P = Permutations(4)
            sage: PG = P.as_permutation_group(); PG                                     # needs sage.groups
            Symmetric group of order 4! as a permutation group

            sage: G = SymmetricGroup(4)                                                 # needs sage.groups
            sage: PG is G                                                               # needs sage.groups
            True
        """
    def identity(self):
        """
        Return the identity permutation of size `n`.

        EXAMPLES::

            sage: Permutations(4).identity()
            [1, 2, 3, 4]
            sage: Permutations(0).identity()
            []
        """
    one = identity
    def unrank(self, r):
        """
        EXAMPLES::

            sage: SP3 = Permutations(3)
            sage: l = list(map(SP3.unrank, range(6)))
            sage: l == SP3.list()
            True
            sage: SP0 = Permutations(0)
            sage: l = list(map(SP0.unrank, range(1)))
            sage: l == SP0.list()
            True
        """
    def rank(self, p=None):
        """
        Return the rank of ``self`` or ``p`` depending on input.

        If a permutation ``p`` is given, return the rank of ``p``
        in ``self``. Otherwise return the dimension of the
        underlying vector space spanned by the (simple) roots.

        EXAMPLES::

            sage: P = Permutations(5)
            sage: P.rank()
            4

            sage: SP3 = Permutations(3)
            sage: list(map(SP3.rank, SP3))
            [0, 1, 2, 3, 4, 5]
            sage: SP0 = Permutations(0)
            sage: list(map(SP0.rank, SP0))
            [0]
        """
    def random_element(self):
        """
        EXAMPLES::

            sage: s = Permutations(4).random_element(); s  # random
            [1, 2, 4, 3]
            sage: s in Permutations(4)
            True
        """
    def cardinality(self):
        """
        Return the number of permutations of size `n`, which is `n!`.

        EXAMPLES::

            sage: Permutations(0).cardinality()
            1
            sage: Permutations(3).cardinality()
            6
            sage: Permutations(4).cardinality()
            24
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return a set of generators for ``self`` as a group.

        EXAMPLES::

            sage: P4 = Permutations(4)
            sage: P4.gens()
            ([2, 1, 3, 4], [1, 3, 2, 4], [1, 2, 4, 3])
        """
    def degree(self):
        """
        Return the degree of ``self``.

        This is the cardinality `n` of the set ``self`` acts on.

        EXAMPLES::

            sage: Permutations(0).degree()
            0
            sage: Permutations(1).degree()
            1
            sage: Permutations(5).degree()
            5
        """
    def degrees(self):
        """
        Return the degrees of ``self``.

        These are the degrees of the fundamental invariants of the
        ring of polynomial invariants.

        EXAMPLES::

            sage: Permutations(3).degrees()
            (2, 3)
            sage: Permutations(7).degrees()
            (2, 3, 4, 5, 6, 7)
        """
    def codegrees(self):
        """
        Return the codegrees of ``self``.

        EXAMPLES::

            sage: Permutations(3).codegrees()
            (0, 1)
            sage: Permutations(7).codegrees()
            (0, 1, 2, 3, 4, 5)
        """
    def element_in_conjugacy_classes(self, nu):
        """
        Return a permutation with cycle type ``nu``.

        If the size of ``nu`` is smaller than the size of permutations in
        ``self``, then some fixed points are added.

        EXAMPLES::

            sage: PP = Permutations(5)
            sage: PP.element_in_conjugacy_classes([2,2])                                # needs sage.combinat
            [2, 1, 4, 3, 5]
            sage: PP.element_in_conjugacy_classes([5, 5])                               # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: the size of the partition (=10) should be at most the size of the permutations (=5)
        """
    def conjugacy_classes_representatives(self):
        """
        Return a complete list of representatives of conjugacy classes
        in ``self``.

        Let `S_n` be the symmetric group on `n` letters. The conjugacy
        classes are indexed by partitions `\\lambda` of `n`. The ordering
        of the conjugacy classes is reverse lexicographic order of
        the partitions.

        EXAMPLES::

            sage: G = Permutations(5)
            sage: G.conjugacy_classes_representatives()                                 # needs sage.combinat sage.libs.flint
            [[1, 2, 3, 4, 5],
             [2, 1, 3, 4, 5],
             [2, 1, 4, 3, 5],
             [2, 3, 1, 4, 5],
             [2, 3, 1, 5, 4],
             [2, 3, 4, 1, 5],
             [2, 3, 4, 5, 1]]

        TESTS:

        Check some border cases::

            sage: S = Permutations(0)
            sage: S.conjugacy_classes_representatives()                                 # needs sage.combinat sage.libs.flint
            [[]]
            sage: S = Permutations(1)
            sage: S.conjugacy_classes_representatives()                                 # needs sage.combinat sage.libs.flint
            [[1]]
        """
    def conjugacy_classes_iterator(self) -> Generator[Incomplete]:
        """
        Iterate over the conjugacy classes of ``self``.

        EXAMPLES::

            sage: G = Permutations(4)
            sage: list(G.conjugacy_classes_iterator()) == G.conjugacy_classes()         # needs sage.combinat sage.graphs sage.groups
            True
        """
    def conjugacy_classes(self):
        """
        Return a list of the conjugacy classes of ``self``.

        EXAMPLES::

            sage: G = Permutations(4)
            sage: G.conjugacy_classes()                                                 # needs sage.combinat sage.graphs sage.groups
            [Conjugacy class of cycle type [1, 1, 1, 1] in Standard permutations of 4,
             Conjugacy class of cycle type [2, 1, 1] in Standard permutations of 4,
             Conjugacy class of cycle type [2, 2] in Standard permutations of 4,
             Conjugacy class of cycle type [3, 1] in Standard permutations of 4,
             Conjugacy class of cycle type [4] in Standard permutations of 4]
        """
    def conjugacy_class(self, g):
        """
        Return the conjugacy class of ``g`` in ``self``.

        INPUT:

        - ``g`` -- a partition or an element of ``self``

        EXAMPLES::

            sage: G = Permutations(5)
            sage: g = G([2,3,4,1,5])
            sage: G.conjugacy_class(g)                                                  # needs sage.combinat sage.graphs sage.groups
            Conjugacy class of cycle type [4, 1] in Standard permutations of 5
            sage: G.conjugacy_class(Partition([2, 1, 1, 1]))                            # needs sage.combinat sage.graphs sage.groups
            Conjugacy class of cycle type [2, 1, 1, 1] in Standard permutations of 5
        """
    def algebra(self, base_ring, category=None):
        """
        Return the symmetric group algebra associated to ``self``.

        INPUT:

        - ``base_ring`` -- a ring
        - ``category`` -- a category (default: the category of ``self``)

        EXAMPLES::

            sage: # needs sage.groups sage.modules
            sage: P = Permutations(4)
            sage: A = P.algebra(QQ); A
            Symmetric group algebra of order 4 over Rational Field
            sage: A.category()
            Join of Category of Coxeter group algebras over Rational Field
                and Category of finite group algebras over Rational Field
                and Category of finite dimensional cellular algebras
                    with basis over Rational Field
            sage: A = P.algebra(QQ, category=Monoids())
            sage: A.category()
            Category of finite dimensional cellular monoid algebras over Rational Field
        """
    @cached_method
    def index_set(self):
        """
        Return the index set for the descents of the symmetric group ``self``.

        This is `\\{ 1, 2, \\ldots, n-1 \\}`, where ``self`` is `S_n`.

        EXAMPLES::

            sage: P = Permutations(8)
            sage: P.index_set()
            (1, 2, 3, 4, 5, 6, 7)
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        The symmetric group `S_n` is a Coxeter group of type `A_{n-1}`.

        EXAMPLES::

            sage: A = SymmetricGroup([2,3,7]); A.cartan_type()                          # needs sage.combinat sage.groups
            ['A', 2]
            sage: A = SymmetricGroup([]); A.cartan_type()                               # needs sage.combinat sage.groups
            ['A', 0]
        """
    def simple_reflection(self, i):
        """
        For `i` in the index set of ``self`` (that is, for `i` in
        `\\{ 1, 2, \\ldots, n-1 \\}`, where ``self`` is `S_n`), this
        returns the elementary transposition `s_i = (i,i+1)`.

        EXAMPLES::

            sage: P = Permutations(4)
            sage: P.simple_reflection(2)
            [1, 3, 2, 4]
            sage: P.simple_reflections()
            Finite family {1: [2, 1, 3, 4], 2: [1, 3, 2, 4], 3: [1, 2, 4, 3]}
        """
    @cached_method
    def reflection_index_set(self):
        """
        Return the index set of the reflections of ``self``.

        .. SEEALSO::

            - :meth:`reflection`
            - :meth:`reflections`

        EXAMPLES::

            sage: P = Permutations(4)
            sage: P.reflection_index_set()
            ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4))
        """
    def reflection(self, i):
        """
        Return the reflection indexed by ``i`` of ``self``.

        This returns the permutation with cycle `i = (a, b)`.

        .. SEEALSO::

            - :meth:`reflections_index_set`
            - :meth:`reflections`

        EXAMPLES::

            sage: P = Permutations(4)
            sage: for i in P.reflection_index_set():
            ....:     print('%s %s'%(i, P.reflection(i)))
            (1, 2) [2, 1, 3, 4]
            (1, 3) [3, 2, 1, 4]
            (1, 4) [4, 2, 3, 1]
            (2, 3) [1, 3, 2, 4]
            (2, 4) [1, 4, 3, 2]
            (3, 4) [1, 2, 4, 3]
        """
    class Element(Permutation):
        def has_left_descent(self, i) -> bool:
            """
            Check if ``i`` is a left descent of ``self``.

            A *left descent* of a permutation `\\pi \\in S_n` means an index
            `i \\in \\{ 1, 2, \\ldots, n-1 \\}` such that
            `s_i \\circ \\pi` has smaller length than `\\pi`. Thus, a left
            descent of `\\pi` is an index `i \\in \\{ 1, 2, \\ldots, n-1 \\}`
            satisfying `\\pi^{-1}(i) > \\pi^{-1}(i+1)`.

            .. WARNING::

                The methods :meth:`descents` and :meth:`idescents` behave
                differently than their Weyl group counterparts. In
                particular, the indexing is 0-based. This could lead to
                errors. Instead, construct the descent set as in the example.

            .. WARNING::

                This ignores the multiplication convention in order
                to be consistent with other Coxeter operations in
                permutations (e.g., computing :meth:`reduced_word`).

            EXAMPLES::

                sage: P = Permutations(4)
                sage: x = P([3, 2, 4, 1])
                sage: (~x).descents()
                [1, 2]
                sage: [i for i in P.index_set() if x.has_left_descent(i)]
                [1, 2]
            """
        def has_right_descent(self, i, mult=None) -> bool:
            """
            Check if ``i`` is a right descent of ``self``.

            A *right descent* of a permutation `\\pi \\in S_n` means an index
            `i \\in \\{ 1, 2, \\ldots, n-1 \\}` such that
            `\\pi \\circ s_i` has smaller length than `\\pi`. Thus, a right
            descent of `\\pi` is an index `i \\in \\{ 1, 2, \\ldots, n-1 \\}`
            satisfying `\\pi(i) > \\pi(i+1)`.

            .. WARNING::

                The methods :meth:`descents` and :meth:`idescents` behave
                differently than their Weyl group counterparts. In
                particular, the indexing is 0-based. This could lead to
                errors. Instead, construct the descent set as in the example.

            .. WARNING::

                This ignores the multiplication convention in order
                to be consistent with other Coxeter operations in
                permutations (e.g., computing :meth:`reduced_word`).

            EXAMPLES::

                sage: P = Permutations(4)
                sage: x = P([3, 2, 4, 1])
                sage: x.descents()
                [1, 3]
                sage: [i for i in P.index_set() if x.has_right_descent(i)]
                [1, 3]
            """
        def __mul__(self, other):
            """
            Multiply ``self`` and ``other``.

            EXAMPLES::

                sage: P = Permutations(4)
                sage: P.simple_reflection(1) * Permutation([6,5,4,3,2,1])
                [5, 6, 4, 3, 2, 1]
                sage: Permutations.options.mult='r2l'
                sage: P.simple_reflection(1) * Permutation([6,5,4,3,2,1])
                [6, 5, 4, 3, 1, 2]
                sage: Permutations.options.mult='l2r'
            """
        def inverse(self):
            """
            Return the inverse of ``self``.

            EXAMPLES::

                sage: P = Permutations(4)
                sage: w0 = P([4,3,2,1])
                sage: w0.inverse() == w0
                True
                sage: w0.inverse().parent() is P
                True
                sage: P([3,2,4,1]).inverse()
                [4, 2, 1, 3]
            """
        __invert__ = inverse
        def apply_simple_reflection_left(self, i):
            """
            Return ``self`` multiplied by the simple reflection ``s[i]``
            on the left.

            This acts by switching the entries in positions `i` and `i+1`.

            .. WARNING::

                This ignores the multiplication convention in order
                to be consistent with other Coxeter operations in
                permutations (e.g., computing :meth:`reduced_word`).

            EXAMPLES::

                sage: W = Permutations(3)
                sage: w = W([2,3,1])
                sage: w.apply_simple_reflection_left(1)
                [1, 3, 2]
                sage: w.apply_simple_reflection_left(2)
                [3, 2, 1]
            """
        def apply_simple_reflection_right(self, i):
            """
            Return ``self`` multiplied by the simple reflection ``s[i]``
            on the right.

            This acts by switching the entries `i` and `i+1`.

            .. WARNING::

                This ignores the multiplication convention in order
                to be consistent with other Coxeter operations in
                permutations (e.g., computing :meth:`reduced_word`).

            EXAMPLES::

                sage: W = Permutations(3)
                sage: w = W([2,3,1])
                sage: w.apply_simple_reflection_right(1)
                [3, 2, 1]
                sage: w.apply_simple_reflection_right(2)
                [2, 1, 3]
            """

def from_permutation_group_element(pge, parent=None):
    """
    Return a :class:`Permutation` given a :class:`PermutationGroupElement`
    ``pge``.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: pge = PermutationGroupElement([(1,2),(3,4)])                              # needs sage.groups
        sage: permutation.from_permutation_group_element(pge)                           # needs sage.groups
        [2, 1, 4, 3]
    """
def from_rank(n, rank):
    """
    Return the permutation of the set `\\{1,...,n\\}` with lexicographic
    rank ``rank``. This is the permutation whose Lehmer code is the
    factoradic representation of ``rank``. In particular, the
    permutation with rank `0` is the identity permutation.

    The permutation is computed without iterating through all of the
    permutations with lower rank. This makes it efficient for large
    permutations.

    .. NOTE::

        The variable ``rank`` is not checked for being in the interval
        from `0` to `n! - 1`. When outside this interval, it acts as
        its residue modulo `n!`.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: Permutation([3, 6, 5, 4, 2, 1]).rank()
        359
        sage: [permutation.from_rank(3, i) for i in range(6)]
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        sage: Permutations(6)[10]
        [1, 2, 4, 6, 3, 5]
        sage: permutation.from_rank(6,10)
        [1, 2, 4, 6, 3, 5]
    """
def from_inversion_vector(iv, parent=None):
    """
    Return the permutation corresponding to inversion vector ``iv``.

    See `~sage.combinat.permutation.Permutation.to_inversion_vector`
    for a definition of the inversion vector of a permutation.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.from_inversion_vector([3,1,0,0,0])
        [3, 2, 4, 1, 5]
        sage: permutation.from_inversion_vector([2,3,6,4,0,2,2,1,0])
        [5, 9, 1, 8, 2, 6, 4, 7, 3]
        sage: permutation.from_inversion_vector([0])
        [1]
        sage: permutation.from_inversion_vector([])
        []
    """
def from_cycles(n, cycles, parent=None):
    '''
    Return the permutation in the `n`-th symmetric group whose decomposition
    into disjoint cycles is ``cycles``.

    This function checks that its input is correct (i.e. that the cycles are
    disjoint and their elements integers among `1...n`). It raises an exception
    otherwise.

    .. WARNING::

        It assumes that the elements are of ``int`` type.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.from_cycles(4, [[1,2]])
        [2, 1, 3, 4]
        sage: permutation.from_cycles(4, [[1,2,4]])
        [2, 4, 3, 1]
        sage: permutation.from_cycles(10, [[3,1],[4,5],[6,8,9]])
        [3, 2, 1, 5, 4, 8, 7, 9, 6, 10]
        sage: permutation.from_cycles(10, ((2, 5), (6, 1, 3)))
        [3, 5, 6, 4, 2, 1, 7, 8, 9, 10]
        sage: permutation.from_cycles(4, [])
        [1, 2, 3, 4]
        sage: permutation.from_cycles(4, [[]])
        [1, 2, 3, 4]
        sage: permutation.from_cycles(0, [])
        []

    Bad input (see :issue:`13742`)::

        sage: Permutation("(-12,2)(3,4)")
        Traceback (most recent call last):
        ...
        ValueError: all elements should be strictly positive integers, but I found -12
        sage: Permutation("(1,2)(2,4)")
        Traceback (most recent call last):
        ...
        ValueError: the element 2 appears more than once in the input
        sage: permutation.from_cycles(4, [[1,18]])
        Traceback (most recent call last):
        ...
        ValueError: you claimed that this is a permutation on 1...4, but it contains 18

    TESTS:

    Verify that :issue:`34662` has been fixed::

        sage: permutation.from_cycles(6, (c for c in [[1,2,3], [4,5,6]]))
        [2, 3, 1, 5, 6, 4]
    '''
def from_lehmer_code(lehmer, parent=None):
    """
    Return the permutation with Lehmer code ``lehmer``.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: lc = Permutation([2,1,5,4,3]).to_lehmer_code(); lc
        [1, 0, 2, 1, 0]
        sage: permutation.from_lehmer_code(lc)
        [2, 1, 5, 4, 3]
    """
def from_lehmer_cocode(lehmer, parent=...):
    """
    Return the permutation with Lehmer cocode ``lehmer``.

    The Lehmer cocode of a permutation `p` is defined as the
    list `(c_1, c_2, \\ldots, c_n)`, where `c_i` is the number
    of `j < i` such that `p(j) > p(i)`.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: lcc = Permutation([2,1,5,4,3]).to_lehmer_cocode(); lcc
        [0, 1, 0, 1, 2]
        sage: permutation.from_lehmer_cocode(lcc)
        [2, 1, 5, 4, 3]
    """
def from_reduced_word(rw, parent=None):
    """
    Return the permutation corresponding to the reduced word ``rw``.

    See
    :meth:`~sage.combinat.permutation.Permutation.reduced_words` for
    a definition of reduced words and the convention on the order of
    multiplication used.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.from_reduced_word([3,2,3,1,2,3,1])
        [3, 4, 2, 1]
        sage: permutation.from_reduced_word([])
        []
    """
def bistochastic_as_sum_of_permutations(M, check: bool = True):
    """
    Return the positive sum of permutations corresponding to
    the bistochastic matrix ``M``.

    A stochastic matrix is a matrix with nonnegative real entries such that the
    sum of the elements of any row is equal to `1`. A bistochastic matrix is a
    stochastic matrix whose transpose matrix is also stochastic ( there are
    conditions both on the rows and on the columns ).

    According to the Birkhoff-von Neumann Theorem, any bistochastic matrix
    can be written as a convex combination of permutation matrices, which also
    means that the polytope of bistochastic matrices is integer.

    As a non-bistochastic matrix can obviously not be written as a convex
    combination of permutations, this theorem is an equivalence.

    This function, given a bistochastic matrix, returns the corresponding
    decomposition.

    INPUT:

    - ``M`` -- a bistochastic matrix

    - ``check`` -- boolean; set to ``True`` (default) to check
      that the matrix is indeed bistochastic

    OUTPUT:

    - An element of ``CombinatorialFreeModule``, which is a free `F`-module
      ( where `F` is the ground ring of the given matrix ) whose basis is
      indexed by the permutations.

    .. NOTE::

        - In this function, we just assume 1 to be any constant : for us a
          matrix `M` is bistochastic if there exists `c>0` such that `M/c`
          is bistochastic.

        - You can obtain a sequence of pairs ``(permutation,coeff)``, where
          ``permutation`` is a Sage ``Permutation`` instance, and ``coeff``
          its corresponding coefficient from the result of this function
          by applying the ``list`` function.

        - If you are interested in the matrix corresponding to a ``Permutation``
          you will be glad to learn about the ``Permutation.to_matrix()`` method.

        - The base ring of the matrix can be anything that can be coerced to ``RR``.

    .. SEEALSO::

        - :meth:`~sage.matrix.matrix2.as_sum_of_permutations`
          to use this method through the ``Matrix`` class.

    EXAMPLES:

    We create a bistochastic matrix from a convex sum of permutations, then
    try to deduce the decomposition from the matrix::

        sage: from sage.combinat.permutation import bistochastic_as_sum_of_permutations

        sage: # needs networkx sage.graphs sage.modules
        sage: L = []
        sage: L.append((9,Permutation([4, 1, 3, 5, 2])))
        sage: L.append((6,Permutation([5, 3, 4, 1, 2])))
        sage: L.append((3,Permutation([3, 1, 4, 2, 5])))
        sage: L.append((2,Permutation([1, 4, 2, 3, 5])))
        sage: M = sum([c * p.to_matrix() for c, p in L])
        sage: decomp = bistochastic_as_sum_of_permutations(M)
        sage: print(decomp)
        2*B[[1, 4, 2, 3, 5]] + 3*B[[3, 1, 4, 2, 5]]
         + 9*B[[4, 1, 3, 5, 2]] + 6*B[[5, 3, 4, 1, 2]]

    An exception is raised when the matrix is not positive and bistochastic::

        sage: # needs sage.modules
        sage: M = Matrix([[2,3],[2,2]])
        sage: decomp = bistochastic_as_sum_of_permutations(M)
        Traceback (most recent call last):
        ...
        ValueError: The matrix is not bistochastic
        sage: bistochastic_as_sum_of_permutations(Matrix(GF(7), 2, [2,1,1,2]))
        Traceback (most recent call last):
        ...
        ValueError: The base ring of the matrix must have a coercion map to RR
        sage: bistochastic_as_sum_of_permutations(Matrix(ZZ, 2, [2,-1,-1,2]))
        Traceback (most recent call last):
        ...
        ValueError: The matrix should have nonnegative entries
    """
def bounded_affine_permutation(A):
    """
    Return the bounded affine permutation of a matrix.

    The *bounded affine permutation* of a matrix `A` with entries in `R`
    is a partial permutation of length `n`, where `n` is the number of
    columns of `A`. The entry in position `i` is the smallest value `j`
    such that column `i` is in the span of columns `i+1, \\ldots, j`,
    over `R`, where column indices are taken modulo `n`.
    If column `i` is the zero vector, then the permutation has a
    fixed point at `i`.

    INPUT:

    - ``A`` -- matrix with entries in a ring `R`

    EXAMPLES::

        sage: from sage.combinat.permutation import bounded_affine_permutation
        sage: A = Matrix(ZZ, [[1,0,0,0], [0,1,0,0]])                                    # needs sage.modules
        sage: bounded_affine_permutation(A)                                             # needs sage.libs.flint sage.modules
        [5, 6, 3, 4]

        sage: A = Matrix(ZZ, [[0,1,0,1,0], [0,0,1,1,0]])                                # needs sage.modules
        sage: bounded_affine_permutation(A)                                             # needs sage.libs.flint sage.modules
        [1, 4, 7, 8, 5]

    REFERENCES:

    - [KLS2013]_
    """

class StandardPermutations_descents(StandardPermutations_n_abstract):
    """
    Permutations of `\\{1, \\ldots, n\\}` with a fixed set of descents.
    """
    @staticmethod
    def __classcall_private__(cls, d, n):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: P1 = Permutations(descents=([1,0,4,8],12))
            sage: P2 = Permutations(descents=((0,1,4,8),12))
            sage: P1 is P2
            True
        """
    def __init__(self, d, n) -> None:
        """
        The class of all permutations of `\\{1, 2, ..., n\\}`
        with set of descent positions `d` (where the descent positions
        are being counted from `0`, so that `i` lies in this set if
        and only if the permutation takes a larger value at `i + 1` than
        at `i + 2`).

        TESTS::

            sage: P = Permutations(descents=([1,0,2], 5))
            sage: TestSuite(P).run()                                                    # needs sage.graphs sage.modules
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        ALGORITHM:

        The algorithm described in [Vie1979]_ is implemented naively.

        EXAMPLES::

            sage: P = Permutations(descents=([1,0,2], 5))
            sage: P.cardinality()
            4

        TESTS::

            sage: Permutations(descents=([], 1)).cardinality()
            1

            sage: Permutations(descents=([1,4], 6)).cardinality()
            40

            sage: def P(D, n):
            ....:     return Permutations(descents=(D, n + 1))
            sage: all(P(D, n).cardinality() == len(P(D, n).list())                      # needs sage.graphs sage.modules
            ....:     for n in range(5) for D in subsets(range(n)))
            True

            sage: n = 20
            sage: D = [6, 8, 10, 11, 12, 13, 14, 15, 17, 19]
            sage: P(D, n).cardinality()
            125291047596
        """
    def first(self):
        """
        Return the first permutation with descents `d`.

        EXAMPLES::

            sage: Permutations(descents=([1,0,4,8],12)).first()
            [3, 2, 1, 4, 6, 5, 7, 8, 10, 9, 11, 12]
        """
    def last(self):
        """
        Return the last permutation with descents `d`.

        EXAMPLES::

            sage: Permutations(descents=([1,0,4,8],12)).last()
            [12, 11, 8, 9, 10, 4, 5, 6, 7, 1, 2, 3]
        """
    def __iter__(self):
        """
        Iterate over all the permutations that have the descents `d`.

        EXAMPLES::

            sage: Permutations(descents=([2,0],5)).list()                               # needs sage.graphs sage.modules
            [[5, 2, 4, 1, 3],
             [5, 3, 4, 1, 2],
             [4, 3, 5, 1, 2],
             [4, 2, 5, 1, 3],
             [3, 2, 5, 1, 4],
             [2, 1, 5, 3, 4],
             [3, 1, 5, 2, 4],
             [4, 1, 5, 2, 3],
             [5, 1, 4, 2, 3],
             [5, 1, 3, 2, 4],
             [4, 1, 3, 2, 5],
             [3, 1, 4, 2, 5],
             [2, 1, 4, 3, 5],
             [3, 2, 4, 1, 5],
             [4, 2, 3, 1, 5],
             [5, 2, 3, 1, 4]]
        """

def descents_composition_list(dc):
    """
    Return a list of all the permutations that have the descent
    composition ``dc``.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.descents_composition_list([1,2,2])                            # needs sage.graphs sage.modules
        [[5, 2, 4, 1, 3],
         [5, 3, 4, 1, 2],
         [4, 3, 5, 1, 2],
         [4, 2, 5, 1, 3],
         [3, 2, 5, 1, 4],
         [2, 1, 5, 3, 4],
         [3, 1, 5, 2, 4],
         [4, 1, 5, 2, 3],
         [5, 1, 4, 2, 3],
         [5, 1, 3, 2, 4],
         [4, 1, 3, 2, 5],
         [3, 1, 4, 2, 5],
         [2, 1, 4, 3, 5],
         [3, 2, 4, 1, 5],
         [4, 2, 3, 1, 5],
         [5, 2, 3, 1, 4]]
    """
def descents_composition_first(dc):
    """
    Compute the smallest element of a descent class having a descent
    composition ``dc``.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.descents_composition_first([1,1,3,4,3])
        [3, 2, 1, 4, 6, 5, 7, 8, 10, 9, 11, 12]
    """
def descents_composition_last(dc):
    """
    Return the largest element of a descent class having a descent
    composition ``dc``.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.descents_composition_last([1,1,3,4,3])
        [12, 11, 8, 9, 10, 4, 5, 6, 7, 1, 2, 3]
    """

class StandardPermutations_recoilsfiner(Permutations):
    @staticmethod
    def __classcall_private__(cls, recoils):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(recoils_finer=[2,2])
            sage: S2 = Permutations(recoils_finer=(2,2))
            sage: S1 is S2
            True
        """
    recoils: Incomplete
    def __init__(self, recoils) -> None:
        """
        TESTS::

            sage: P = Permutations(recoils_finer=[2,2])
            sage: TestSuite(P).run()                                                    # needs sage.graphs
        """
    def __iter__(self):
        """
        Iterate over of all of the permutations whose recoils composition
        is finer than ``self.recoils``.

        EXAMPLES::

            sage: Permutations(recoils_finer=[2,2]).list()                              # needs sage.graphs sage.modules
            [[3, 1, 4, 2],
             [3, 4, 1, 2],
             [1, 3, 4, 2],
             [1, 3, 2, 4],
             [1, 2, 3, 4],
             [3, 1, 2, 4]]
        """

class StandardPermutations_recoilsfatter(Permutations):
    @staticmethod
    def __classcall_private__(cls, recoils):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(recoils_fatter=[2,2])
            sage: S2 = Permutations(recoils_fatter=(2,2))
            sage: S1 is S2
            True
        """
    recoils: Incomplete
    def __init__(self, recoils) -> None:
        """
        TESTS::

            sage: P = Permutations(recoils_fatter=[2,2])
            sage: TestSuite(P).run()                                                    # needs sage.graphs
        """
    def __iter__(self):
        """
        Iterate over of all of the permutations whose recoils composition
        is fatter than ``self.recoils``.

        EXAMPLES::

            sage: Permutations(recoils_fatter=[2,2]).list()                             # needs sage.graphs sage.modules
            [[4, 3, 2, 1],
             [3, 2, 1, 4],
             [3, 2, 4, 1],
             [3, 4, 2, 1],
             [3, 4, 1, 2],
             [3, 1, 4, 2],
             [1, 3, 4, 2],
             [1, 3, 2, 4],
             [3, 1, 2, 4],
             [1, 4, 3, 2],
             [4, 1, 3, 2],
             [4, 3, 1, 2]]
        """

class StandardPermutations_recoils(Permutations):
    """
    Permutations of `\\{1, \\ldots, n\\}` with a fixed recoils composition.
    """
    @staticmethod
    def __classcall_private__(cls, recoils):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(recoils=[2,2])
            sage: S2 = Permutations(recoils=(2,2))
            sage: S1 is S2
            True
        """
    recoils: Incomplete
    def __init__(self, recoils) -> None:
        """
        TESTS::

            sage: P = Permutations(recoils=[2,2])
            sage: TestSuite(P).run()                                                    # needs sage.graphs
        """
    def __iter__(self):
        """
        Iterate over of all of the permutations whose recoils composition
        is equal to ``self.recoils``.

        EXAMPLES::

            sage: Permutations(recoils=[2,2]).list()                                    # needs sage.graphs sage.modules
            [[3, 1, 4, 2], [3, 4, 1, 2], [1, 3, 4, 2], [1, 3, 2, 4], [3, 1, 2, 4]]
        """

def from_major_code(mc, final_descent: bool = False):
    """
    Return the permutation with major code ``mc``.

    The major code of a permutation is defined in
    :meth:`~sage.combinat.permutation.Permutation.to_major_code`.

    .. WARNING::

        This function creates illegal permutations (i.e. ``Permutation([9])``,
        and this is dangerous as the :meth:`Permutation` class is only designed
        to handle permutations on `1...n`. This will have to be changed when Sage
        permutations will be able to handle anything, but right now this should
        be fixed. Be careful with the results.

    .. WARNING::

        If ``mc`` is not a major index of a permutation, then the return
        value of this method can be anything. Garbage in, garbage out!

    REFERENCES:

    - Skandera, M. *An Eulerian Partner for Inversions*. Sem.
      Lothar. Combin. 46 (2001) B46d.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.from_major_code([5, 0, 1, 0, 1, 2, 0, 1, 0])
        [9, 3, 5, 7, 2, 1, 4, 6, 8]
        sage: permutation.from_major_code([8, 3, 3, 1, 4, 0, 1, 0, 0])
        [2, 8, 4, 3, 6, 7, 9, 5, 1]
        sage: Permutation([2,1,6,4,7,3,5]).to_major_code()
        [3, 2, 0, 2, 2, 0, 0]
        sage: permutation.from_major_code([3, 2, 0, 2, 2, 0, 0])
        [2, 1, 6, 4, 7, 3, 5]

    TESTS::

        sage: permutation.from_major_code([])
        []

        sage: all( permutation.from_major_code(p.to_major_code()) == p
        ....:      for p in Permutations(5) )
        True
    """

class StandardPermutations_bruhat_smaller(Permutations):
    """
    Permutations of `\\{1, \\ldots, n\\}` that are less than or equal to a
    permutation `p` in the Bruhat order.
    """
    @staticmethod
    def __classcall_private__(cls, p):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(bruhat_smaller=[2,3,1])
            sage: S2 = Permutations(bruhat_smaller=(1,2,3))
            sage: S1 is S2
            True
        """
    p: Incomplete
    def __init__(self, p) -> None:
        """
        TESTS::

            sage: P = Permutations(bruhat_smaller=[3,2,1])
            sage: TestSuite(P).run()
        """
    def __iter__(self):
        """
        Iterate through a list of permutations smaller than or equal to ``p``
        in the Bruhat order.

        EXAMPLES::

            sage: Permutations(bruhat_smaller=[4,1,2,3]).list()
            [[1, 2, 3, 4],
             [1, 2, 4, 3],
             [1, 3, 2, 4],
             [1, 4, 2, 3],
             [2, 1, 3, 4],
             [2, 1, 4, 3],
             [3, 1, 2, 4],
             [4, 1, 2, 3]]
        """

class StandardPermutations_bruhat_greater(Permutations):
    """
    Permutations of `\\{1, \\ldots, n\\}` that are greater than or equal to a
    permutation `p` in the Bruhat order.
    """
    @staticmethod
    def __classcall_private__(cls, p):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: S1 = Permutations(bruhat_greater=[2,3,1])
            sage: S2 = Permutations(bruhat_greater=(1,2,3))
            sage: S1 is S2
            True
        """
    p: Incomplete
    def __init__(self, p) -> None:
        """
        TESTS::

            sage: P = Permutations(bruhat_greater=[3,2,1])
            sage: TestSuite(P).run()
        """
    def __iter__(self):
        """
        Iterate through a list of permutations greater than or equal to ``p``
        in the Bruhat order.

        EXAMPLES::

            sage: Permutations(bruhat_greater=[4,1,2,3]).list()
            [[4, 1, 2, 3],
             [4, 1, 3, 2],
             [4, 2, 1, 3],
             [4, 2, 3, 1],
             [4, 3, 1, 2],
             [4, 3, 2, 1]]
        """

def bruhat_lequal(p1, p2):
    """
    Return ``True`` if ``p1`` is less than ``p2`` in the Bruhat order.

    Algorithm from mupad-combinat.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.bruhat_lequal([2,4,3,1],[3,4,2,1])
        True
    """
def permutohedron_lequal(p1, p2, side: str = 'right'):
    """
    Return ``True`` if ``p1`` is less than or equal to ``p2`` in the
    permutohedron order.

    By default, the computations are done in the right permutohedron.
    If you pass the option ``side='left'``, then they will be done in the
    left permutohedron.

    EXAMPLES::

        sage: import sage.combinat.permutation as permutation
        sage: permutation.permutohedron_lequal(Permutation([3,2,1,4]),Permutation([4,2,1,3]))
        False
        sage: permutation.permutohedron_lequal(Permutation([3,2,1,4]),Permutation([4,2,1,3]), side='left')
        True
    """
def to_standard(p, key=None):
    """
    Return a standard permutation corresponding to the iterable ``p``.

    INPUT:

    - ``p`` -- an iterable
    - ``key`` -- (optional) a comparison key for the element
      ``x`` of ``p``

    EXAMPLES::

        sage: # needs sage.combinat
        sage: import sage.combinat.permutation as permutation
        sage: permutation.to_standard([4,2,7])
        [2, 1, 3]
        sage: permutation.to_standard([1,2,3])
        [1, 2, 3]
        sage: permutation.to_standard([])
        []
        sage: permutation.to_standard([1,2,3], key=lambda x: -x)
        [3, 2, 1]
        sage: permutation.to_standard([5,8,2,5], key=lambda x: -x)
        [2, 1, 4, 3]

    TESTS:

    Does not mutate the list::

        sage: a = [1,2,4]
        sage: permutation.to_standard(a)                                                # needs sage.combinat
        [1, 2, 3]
        sage: a
        [1, 2, 4]

    We check against the naive method::

        sage: def std(p):
        ....:     s = [0] * len(p)
        ....:     c = p[:]
        ....:     biggest = max(p) + 1
        ....:     i = 1
        ....:     for _ in range(len(c)):
        ....:         smallest = min(c)
        ....:         smallest_index = c.index(smallest)
        ....:         s[smallest_index] = i
        ....:         i += 1
        ....:         c[smallest_index] = biggest
        ....:     return Permutations()(s)
        sage: p = list(Words(100, 1000).random_element())                               # needs sage.combinat
        sage: std(p) == permutation.to_standard(p)                                      # needs sage.combinat
        True
    """

class CyclicPermutations(Permutations_mset):
    """
    Return the class of all cyclic permutations of ``mset`` in cycle notation.
    These are the same as necklaces.

    INPUT:

    - ``mset`` -- a multiset

    EXAMPLES::

        sage: CyclicPermutations(range(4)).list()                                       # needs sage.combinat
        [[0, 1, 2, 3],
         [0, 1, 3, 2],
         [0, 2, 1, 3],
         [0, 2, 3, 1],
         [0, 3, 1, 2],
         [0, 3, 2, 1]]
        sage: CyclicPermutations([1,1,1]).list()                                        # needs sage.combinat
        [[1, 1, 1]]
    """
    @staticmethod
    def __classcall_private__(cls, mset):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: CP1 = CyclicPermutations([1,1,1])
            sage: CP2 = CyclicPermutations((1,1,1))
            sage: CP1 is CP2
            True

            sage: CP = CyclicPermutations([1,2,3,3])
            sage: CP
            Cyclic permutations of [1, 2, 3, 3]
            sage: TestSuite(CP).run() # not tested -- broken
        """
    def __iter__(self, distinct: bool = False):
        """
        EXAMPLES::

            sage: CyclicPermutations(range(4)).list()  # indirect doctest               # needs sage.combinat
            [[0, 1, 2, 3],
             [0, 1, 3, 2],
             [0, 2, 1, 3],
             [0, 2, 3, 1],
             [0, 3, 1, 2],
             [0, 3, 2, 1]]
             sage: CyclicPermutations([1,1,1]).list()                                   # needs sage.combinat
             [[1, 1, 1]]
             sage: CyclicPermutations([1,1,1]).list(distinct=True)                      # needs sage.combinat
             [[1, 1, 1], [1, 1, 1]]
        """
    iterator = __iter__
    def list(self, distinct: bool = False):
        """
        EXAMPLES::

            sage: CyclicPermutations(range(4)).list()                                   # needs sage.combinat
            [[0, 1, 2, 3],
             [0, 1, 3, 2],
             [0, 2, 1, 3],
             [0, 2, 3, 1],
             [0, 3, 1, 2],
             [0, 3, 2, 1]]
        """

class CyclicPermutationsOfPartition(Permutations):
    """
    Combinations of cyclic permutations of each cell of a given partition.

    This is the same as a Cartesian product of necklaces.

    EXAMPLES::

        sage: CyclicPermutationsOfPartition([[1,2,3,4],[5,6,7]]).list()                 # needs sage.combinat
        [[[1, 2, 3, 4], [5, 6, 7]],
         [[1, 2, 4, 3], [5, 6, 7]],
         [[1, 3, 2, 4], [5, 6, 7]],
         [[1, 3, 4, 2], [5, 6, 7]],
         [[1, 4, 2, 3], [5, 6, 7]],
         [[1, 4, 3, 2], [5, 6, 7]],
         [[1, 2, 3, 4], [5, 7, 6]],
         [[1, 2, 4, 3], [5, 7, 6]],
         [[1, 3, 2, 4], [5, 7, 6]],
         [[1, 3, 4, 2], [5, 7, 6]],
         [[1, 4, 2, 3], [5, 7, 6]],
         [[1, 4, 3, 2], [5, 7, 6]]]

    ::

        sage: CyclicPermutationsOfPartition([[1,2,3,4],[4,4,4]]).list()                 # needs sage.combinat
        [[[1, 2, 3, 4], [4, 4, 4]],
         [[1, 2, 4, 3], [4, 4, 4]],
         [[1, 3, 2, 4], [4, 4, 4]],
         [[1, 3, 4, 2], [4, 4, 4]],
         [[1, 4, 2, 3], [4, 4, 4]],
         [[1, 4, 3, 2], [4, 4, 4]]]

    ::

        sage: CyclicPermutationsOfPartition([[1,2,3],[4,4,4]]).list()                   # needs sage.combinat
        [[[1, 2, 3], [4, 4, 4]], [[1, 3, 2], [4, 4, 4]]]

    ::

        sage: CyclicPermutationsOfPartition([[1,2,3],[4,4,4]]).list(distinct=True)      # needs sage.combinat
        [[[1, 2, 3], [4, 4, 4]],
         [[1, 3, 2], [4, 4, 4]],
         [[1, 2, 3], [4, 4, 4]],
         [[1, 3, 2], [4, 4, 4]]]
    """
    @staticmethod
    def __classcall_private__(cls, partition):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: CP1 = CyclicPermutationsOfPartition([[1,2,3],[4,4,4]])
            sage: CP2 = CyclicPermutationsOfPartition([[1,2,3],[4,4,4]])
            sage: CP1 is CP2
            True
        """
    partition: Incomplete
    def __init__(self, partition) -> None:
        """
        TESTS::

            sage: CP = CyclicPermutationsOfPartition([[1,2,3,4],[5,6,7]])
            sage: CP
            Cyclic permutations of partition [[1, 2, 3, 4], [5, 6, 7]]
            sage: TestSuite(CP).run()                                                   # needs sage.combinat
        """
    class Element(ClonableArray):
        """
        A cyclic permutation of a partition.
        """
        def check(self) -> None:
            """
            Check that ``self`` is a valid element.

            EXAMPLES::

                sage: CP = CyclicPermutationsOfPartition([[1,2,3,4],[5,6,7]])
                sage: elt = CP[0]                                                       # needs sage.combinat
                sage: elt.check()                                                       # needs sage.combinat
            """
    def __iter__(self, distinct: bool = False):
        """
        AUTHORS:

        - Robert Miller

        EXAMPLES::

            sage: CyclicPermutationsOfPartition([[1,2,3,4],        # indirect doctest   # needs sage.combinat
            ....:                                [5,6,7]]).list()
            [[[1, 2, 3, 4], [5, 6, 7]],
             [[1, 2, 4, 3], [5, 6, 7]],
             [[1, 3, 2, 4], [5, 6, 7]],
             [[1, 3, 4, 2], [5, 6, 7]],
             [[1, 4, 2, 3], [5, 6, 7]],
             [[1, 4, 3, 2], [5, 6, 7]],
             [[1, 2, 3, 4], [5, 7, 6]],
             [[1, 2, 4, 3], [5, 7, 6]],
             [[1, 3, 2, 4], [5, 7, 6]],
             [[1, 3, 4, 2], [5, 7, 6]],
             [[1, 4, 2, 3], [5, 7, 6]],
             [[1, 4, 3, 2], [5, 7, 6]]]

        ::

            sage: CyclicPermutationsOfPartition([[1,2,3,4],[4,4,4]]).list()             # needs sage.combinat
            [[[1, 2, 3, 4], [4, 4, 4]],
             [[1, 2, 4, 3], [4, 4, 4]],
             [[1, 3, 2, 4], [4, 4, 4]],
             [[1, 3, 4, 2], [4, 4, 4]],
             [[1, 4, 2, 3], [4, 4, 4]],
             [[1, 4, 3, 2], [4, 4, 4]]]

        ::

            sage: CyclicPermutationsOfPartition([[1,2,3],[4,4,4]]).list()               # needs sage.combinat
            [[[1, 2, 3], [4, 4, 4]], [[1, 3, 2], [4, 4, 4]]]

        ::

            sage: CyclicPermutationsOfPartition([[1,2,3],[4,4,4]]).list(distinct=True)  # needs sage.combinat
            [[[1, 2, 3], [4, 4, 4]],
             [[1, 3, 2], [4, 4, 4]],
             [[1, 2, 3], [4, 4, 4]],
             [[1, 3, 2], [4, 4, 4]]]
        """
    iterator = __iter__
    def list(self, distinct: bool = False):
        """
        EXAMPLES::

            sage: CyclicPermutationsOfPartition([[1,2,3],[4,4,4]]).list()               # needs sage.combinat
            [[[1, 2, 3], [4, 4, 4]], [[1, 3, 2], [4, 4, 4]]]
            sage: CyclicPermutationsOfPartition([[1,2,3],[4,4,4]]).list(distinct=True)  # needs sage.combinat
            [[[1, 2, 3], [4, 4, 4]],
             [[1, 3, 2], [4, 4, 4]],
             [[1, 2, 3], [4, 4, 4]],
             [[1, 3, 2], [4, 4, 4]]]
        """

class StandardPermutations_all_avoiding(StandardPermutations_all):
    """
    All standard permutations avoiding a set of patterns.
    """
    @staticmethod
    def __classcall_private__(cls, a):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: P1 = Permutations(avoiding=([2,1,3],[1,2,3]))
            sage: P2 = Permutations(avoiding=[[2,1,3],[1,2,3]])
            sage: P1 is P2
            True
        """
    def __init__(self, a) -> None:
        """
        TESTS::

            sage: P = Permutations(avoiding=[[2,1,3],[1,2,3]])
            sage: TestSuite(P).run(max_runs=25)                                         # needs sage.combinat
        """
    def patterns(self):
        """
        Return the patterns avoided by this class of permutations.

        EXAMPLES::

            sage: P = Permutations(avoiding=[[2,1,3],[1,2,3]])
            sage: P.patterns()
            ([2, 1, 3], [1, 2, 3])
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [1,3,2] in Permutations(avoiding=[1,3,2])                             # needs sage.combinat
            False
            sage: [1,3,2] in Permutations(avoiding=[[1,3,2]])                           # needs sage.combinat
            False
            sage: [2,1,3] in Permutations(avoiding=[[1,3,2],[1,2,3]])                   # needs sage.combinat
            True
            sage: [2,1,3] in Permutations(avoiding=[])
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        TESTS::

            sage: it = iter(Permutations(avoiding=[[2,1,3],[1,2,3]]))
            sage: [next(it) for i in range(10)]                                         # needs sage.combinat
            [[],
             [1],
             [1, 2],
             [2, 1],
             [1, 3, 2],
             [2, 3, 1],
             [3, 1, 2],
             [3, 2, 1],
             [1, 4, 3, 2],
             [2, 4, 3, 1]]
        """

class StandardPermutations_avoiding_generic(StandardPermutations_n_abstract):
    """
    Generic class for subset of permutations avoiding a set of patterns.
    """
    @staticmethod
    def __classcall_private__(cls, n, a):
        """
        Normalize arguments to ensure a unique representation.

        TESTS::

            sage: P1 = Permutations(3, avoiding=([2,1,3],[1,2,3]))
            sage: P2 = Permutations(3, avoiding=[[2,1,3],[1,2,3]])
            sage: P1 is P2
            True
        """
    def __init__(self, n, a) -> None:
        """
        EXAMPLES::

            sage: P = Permutations(3, avoiding=[[2,1,3],[1,2,3]])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
            sage: type(P)
            <class 'sage.combinat.permutation.StandardPermutations_avoiding_generic_with_category'>
        """
    def patterns(self):
        """
        Return the patterns avoided by this class of permutations.

        EXAMPLES::

            sage: P = Permutations(3, avoiding=[[2,1,3],[1,2,3]])
            sage: P.patterns()
            ([2, 1, 3], [1, 2, 3])
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [1,3,2] in Permutations(3, avoiding=[1,3,2])                          # needs sage.combinat
            False
            sage: [1,3,2] in Permutations(3, avoiding=[[1,3,2]])                        # needs sage.combinat
            False
            sage: [2,1,3] in Permutations(3, avoiding=[[1,3,2],[1,2,3]])                # needs sage.combinat
            True
            sage: [2,1,3] in Permutations(3, avoiding=[])
            True
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[[2, 1, 3],[1,2,3]]).list()                  # needs sage.combinat
            [[1, 3, 2], [3, 1, 2], [2, 3, 1], [3, 2, 1]]
            sage: Permutations(0, avoiding=[[2, 1, 3],[1,2,3]]).list()
            [[]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: P = Permutations(3, avoiding=[[2, 1, 3],[1,2,3]])
            sage: P.cardinality()                                                       # needs sage.combinat
            4
        """

class StandardPermutations_avoiding_12(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[1, 2])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[1,2]).list()
            [[3, 2, 1]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: P = Permutations(3, avoiding=[1, 2])
            sage: P.cardinality()
            1
        """

class StandardPermutations_avoiding_21(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[2, 1])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[2,1]).list()
            [[1, 2, 3]]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: P = Permutations(3, avoiding=[2, 1])
            sage: P.cardinality()
            1
        """

class StandardPermutations_avoiding_132(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[1, 3, 2])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Permutations(5, avoiding=[1, 3, 2]).cardinality()
            42
            sage: len( Permutations(5, avoiding=[1, 3, 2]).list() )
            42
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[1,3,2]).list()  # indirect doctest
            [[1, 2, 3], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
            sage: Permutations(4, avoiding=[1,3,2]).list()
            [[4, 1, 2, 3],
             [4, 2, 1, 3],
             [4, 2, 3, 1],
             [4, 3, 1, 2],
             [4, 3, 2, 1],
             [3, 4, 1, 2],
             [3, 4, 2, 1],
             [2, 3, 4, 1],
             [3, 2, 4, 1],
             [1, 2, 3, 4],
             [2, 1, 3, 4],
             [2, 3, 1, 4],
             [3, 1, 2, 4],
             [3, 2, 1, 4]]
        """

class StandardPermutations_avoiding_123(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[2, 1, 3])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def cardinality(self) -> Integer:
        """
        EXAMPLES::

            sage: Permutations(5, avoiding=[1, 2, 3]).cardinality()
            42
            sage: len( Permutations(5, avoiding=[1, 2, 3]).list() )
            42
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[1, 2, 3]).list()  # indirect doctest
             [[1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
            sage: Permutations(2, avoiding=[1, 2, 3]).list()
            [[1, 2], [2, 1]]
            sage: Permutations(3, avoiding=[1, 2, 3]).list()
            [[1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """

class StandardPermutations_avoiding_321(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[3, 2, 1])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Permutations(5, avoiding=[3, 2, 1]).cardinality()
            42
            sage: len( Permutations(5, avoiding=[3, 2, 1]).list() )
            42
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[3, 2, 1]).list()  # indirect doctest
            [[2, 3, 1], [3, 1, 2], [1, 3, 2], [2, 1, 3], [1, 2, 3]]
        """

class StandardPermutations_avoiding_231(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[2, 3, 1])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Permutations(5, avoiding=[2, 3, 1]).cardinality()
            42
            sage: len( Permutations(5, avoiding=[2, 3, 1]).list() )
            42
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[2, 3, 1]).list()
            [[3, 2, 1], [3, 1, 2], [1, 3, 2], [2, 1, 3], [1, 2, 3]]
        """

class StandardPermutations_avoiding_312(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[3, 1, 2])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Permutations(5, avoiding=[3, 1, 2]).cardinality()
            42
            sage: len( Permutations(5, avoiding=[3, 1, 2]).list() )
            42
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[3, 1, 2]).list()
            [[3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
        """

class StandardPermutations_avoiding_213(StandardPermutations_avoiding_generic):
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: P = Permutations(3, avoiding=[2, 1, 3])
            sage: TestSuite(P).run()                                                    # needs sage.combinat
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Permutations(5, avoiding=[2, 1, 3]).cardinality()
            42
            sage: len( Permutations(5, avoiding=[2, 1, 3]).list() )
            42
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: Permutations(3, avoiding=[2, 1, 3]).list()
            [[1, 2, 3], [1, 3, 2], [3, 1, 2], [2, 3, 1], [3, 2, 1]]
        """

class PatternAvoider(GenericBacktracker):
    def __init__(self, parent, patterns) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.permutation import PatternAvoider
            sage: P = Permutations(4)
            sage: p = PatternAvoider(P, [[1,2,3]])
            sage: loads(dumps(p))
            <sage.combinat.permutation.PatternAvoider object at 0x...>
        """

class PermutationsNK(Permutations_setk):
    """
    This exists solely for unpickling ``PermutationsNK`` objects created
    with Sage <= 6.3.
    """
