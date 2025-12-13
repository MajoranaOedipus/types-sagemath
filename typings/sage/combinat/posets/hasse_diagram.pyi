from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial
from sage.combinat.posets.hasse_cython import IncreasingChains as IncreasingChains
from sage.graphs.digraph import DiGraph as DiGraph
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.rest_index_of_methods import gen_rest_table_index as gen_rest_table_index
from sage.rings.integer_ring import ZZ as ZZ
from typing import Iterator

class LatticeError(ValueError):
    '''
    Helper exception class to forward elements without meet or
    join to upper level, so that the user will see "No meet for
    a and b" instead of "No meet for 1 and 2".
    '''
    fail: Incomplete
    x: Incomplete
    y: Incomplete
    def __init__(self, fail, x, y) -> None:
        """
        Initialize the exception.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import LatticeError
            sage: error = LatticeError('join', 3, 8)
            sage: error.x
            3
        """

class HasseDiagram(DiGraph):
    """
    The Hasse diagram of a poset. This is just a transitively-reduced,
    directed, acyclic graph without loops or multiple edges.

    .. NOTE::

       We assume that ``range(n)`` is a linear extension of the poset.
       That is, ``range(n)`` is the vertex set and a topological sort of
       the digraph.

    This should not be called directly, use Poset instead; all type
    checking happens there.

    EXAMPLES::

        sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
        sage: H = HasseDiagram({0:[1,2],1:[3],2:[3],3:[]}); H
        Hasse diagram of a poset containing 4 elements
        sage: TestSuite(H).run()
    """
    def linear_extension(self) -> list[int]:
        """
        Return a linear extension.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,2],1:[3],2:[3],3:[]})
            sage: H.linear_extension()
            [0, 1, 2, 3]
        """
    def linear_extensions(self) -> Iterator[list[int]]:
        """
        Return an iterator over all linear extensions.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,2],1:[3],2:[3],3:[]})
            sage: list(H.linear_extensions())                                           # needs sage.modules
            [[0, 1, 2, 3], [0, 2, 1, 3]]
        """
    def greedy_linear_extensions_iterator(self) -> Iterator[list[int]]:
        '''
        Return an iterator over greedy linear extensions of the Hasse diagram.

        A linear extension `[e_1, e_2, \\ldots, e_n]` is *greedy* if for
        every `i` either `e_{i+1}` covers `e_i` or all upper covers
        of `e_i` have at least one lower cover that is not in
        `[e_1, e_2, \\ldots, e_i]`.

        Informally said a linear extension is greedy if it "always
        goes up when possible" and so has no unnecessary jumps.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: N5 = HasseDiagram({0: [1, 2], 2: [3], 1: [4], 3: [4]})
            sage: for l in N5.greedy_linear_extensions_iterator():
            ....:     print(l)
            [0, 1, 2, 3, 4]
            [0, 2, 3, 1, 4]

        TESTS::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: list(HasseDiagram({}).greedy_linear_extensions_iterator())
            [[]]
            sage: H = HasseDiagram({0: []})
            sage: list(H.greedy_linear_extensions_iterator())
            [[0]]
        '''
    def supergreedy_linear_extensions_iterator(self) -> Iterator[list[int]]:
        '''
        Return an iterator over supergreedy linear extensions of the Hasse diagram.

        A linear extension `[e_1, e_2, \\ldots, e_n]` is *supergreedy* if,
        for every `i` and `j` where `i > j`, `e_i` covers `e_j` if for
        every `i > k > j` at least one lower cover of `e_k` is not in
        `[e_1, e_2, \\ldots, e_k]`.

        Informally said a linear extension is supergreedy if it "always
        goes as high possible, and withdraw so less as possible".
        These are also called depth-first linear extensions.

        EXAMPLES:

        We show the difference between "only greedy" and supergreedy
        extensions::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 2: [3, 4]})
            sage: G_ext = list(H.greedy_linear_extensions_iterator())
            sage: SG_ext = list(H.supergreedy_linear_extensions_iterator())
            sage: [0, 2, 3, 1, 4] in G_ext
            True
            sage: [0, 2, 3, 1, 4] in SG_ext
            False

            sage: len(SG_ext)
            4

        TESTS::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: list(HasseDiagram({}).supergreedy_linear_extensions_iterator())
            [[]]
            sage: list(HasseDiagram({0: [], 1: []}).supergreedy_linear_extensions_iterator())
            [[0, 1], [1, 0]]
        '''
    def is_linear_extension(self, lin_ext=None) -> bool:
        """
        Test if an ordering is a linear extension.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,2],1:[3],2:[3],3:[]})
            sage: H.is_linear_extension(list(range(4)))
            True
            sage: H.is_linear_extension([3,2,1,0])
            False
        """
    def cover_relations_iterator(self) -> Iterator[tuple[int, int]]:
        """
        Iterate over cover relations.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[2,3], 1:[3,4], 2:[5], 3:[5], 4:[5]})
            sage: list(H.cover_relations_iterator())
            [(0, 2), (0, 3), (1, 3), (1, 4), (2, 5), (3, 5), (4, 5)]
        """
    def cover_relations(self) -> list[tuple[int, int]]:
        """
        Return the list of cover relations.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[2,3], 1:[3,4], 2:[5], 3:[5], 4:[5]})
            sage: H.cover_relations()
            [(0, 2), (0, 3), (1, 3), (1, 4), (2, 5), (3, 5), (4, 5)]
        """
    def is_lequal(self, i, j) -> bool:
        """
        Return ``True`` if i is less than or equal to j in the poset, and
        ``False`` otherwise.

        .. NOTE::

            If the :meth:`lequal_matrix` has been computed, then this method is
            redefined to use the cached data (see :meth:`_alternate_is_lequal`).

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[2], 1:[2], 2:[3], 3:[4], 4:[]})
            sage: x,y,z = 0, 1, 4
            sage: H.is_lequal(x,y)
            False
            sage: H.is_lequal(y,x)
            False
            sage: H.is_lequal(x,z)
            True
            sage: H.is_lequal(y,z)
            True
            sage: H.is_lequal(z,z)
            True
        """
    def is_less_than(self, x, y) -> bool:
        """
        Return ``True`` if ``x`` is less than but not equal to ``y`` in the
        poset, and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[2], 1:[2], 2:[3], 3:[4], 4:[]})
            sage: x,y,z = 0, 1, 4
            sage: H.is_less_than(x,y)
            False
            sage: H.is_less_than(y,x)
            False
            sage: H.is_less_than(x,z)
            True
            sage: H.is_less_than(y,z)
            True
            sage: H.is_less_than(z,z)
            False
        """
    def is_gequal(self, x, y) -> bool:
        """
        Return ``True`` if ``x`` is greater than or equal to ``y``, and
        ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: Q = HasseDiagram({0:[2], 1:[2], 2:[3], 3:[4], 4:[]})
            sage: x,y,z = 0,1,4
            sage: Q.is_gequal(x,y)
            False
            sage: Q.is_gequal(y,x)
            False
            sage: Q.is_gequal(x,z)
            False
            sage: Q.is_gequal(z,x)
            True
            sage: Q.is_gequal(z,y)
            True
            sage: Q.is_gequal(z,z)
            True
        """
    def is_greater_than(self, x, y) -> bool:
        """
        Return ``True`` if ``x`` is greater than but not equal to
        ``y``, and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: Q = HasseDiagram({0:[2], 1:[2], 2:[3], 3:[4], 4:[]})
            sage: x,y,z = 0,1,4
            sage: Q.is_greater_than(x,y)
            False
            sage: Q.is_greater_than(y,x)
            False
            sage: Q.is_greater_than(x,z)
            False
            sage: Q.is_greater_than(z,x)
            True
            sage: Q.is_greater_than(z,y)
            True
            sage: Q.is_greater_than(z,z)
            False
        """
    def minimal_elements(self) -> list[int]:
        """
        Return a list of the minimal elements of the poset.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4],4:[]})
            sage: P(0) in P.minimal_elements()
            True
            sage: P(1) in P.minimal_elements()
            True
            sage: P(2) in P.minimal_elements()
            True
        """
    def maximal_elements(self) -> list[int]:
        """
        Return a list of the maximal elements of the poset.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4],4:[]})
            sage: P.maximal_elements()
            [4]
        """
    @cached_method
    def bottom(self) -> int | None:
        """
        Return the bottom element of the poset, if it exists.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4],4:[]})
            sage: P.bottom() is None
            True
            sage: Q = Poset({0:[1],1:[]})
            sage: Q.bottom()
            0
        """
    def has_bottom(self) -> bool:
        """
        Return ``True`` if the poset has a unique minimal element.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4],4:[]})
            sage: P.has_bottom()
            False
            sage: Q = Poset({0:[1],1:[]})
            sage: Q.has_bottom()
            True
        """
    def top(self) -> int | None:
        """
        Return the top element of the poset, if it exists.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4,5],4:[],5:[]})
            sage: P.top() is None
            True
            sage: Q = Poset({0:[1],1:[]})
            sage: Q.top()
            1
        """
    def has_top(self) -> bool:
        """
        Return ``True`` if the poset contains a unique maximal element, and
        ``False`` otherwise.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4,5],4:[],5:[]})
            sage: P.has_top()
            False
            sage: Q = Poset({0:[1],1:[]})
            sage: Q.has_top()
            True
        """
    def is_bounded(self) -> bool:
        """
        Return ``True`` if the poset contains a unique maximal element and a
        unique minimal element, and ``False`` otherwise.

        EXAMPLES::

            sage: P = Poset({0:[3],1:[3],2:[3],3:[4,5],4:[],5:[]})
            sage: P.is_bounded()
            False
            sage: Q = Poset({0:[1],1:[]})
            sage: Q.is_bounded()
            True
        """
    def is_chain(self) -> bool:
        """
        Return ``True`` if the poset is totally ordered, and ``False`` otherwise.

        EXAMPLES::

            sage: L = Poset({0:[1],1:[2],2:[3],3:[4]})
            sage: L.is_chain()
            True
            sage: V = Poset({0:[1,2]})
            sage: V.is_chain()
            False

        TESTS:

        Check :issue:`15330`::

            sage: p = Poset(DiGraph({0:[1],2:[1]}))
            sage: p.is_chain()
            False
        """
    def is_antichain_of_poset(self, elms) -> bool:
        """
        Return ``True`` if ``elms`` is an antichain of the Hasse
        diagram and ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2, 3], 1: [4], 2: [4], 3: [4]})
            sage: H.is_antichain_of_poset([1, 2, 3])
            True
            sage: H.is_antichain_of_poset([0, 2, 3])
            False
        """
    def dual(self):
        """
        Return a poset that is dual to the given poset.

        This means that it has the same elements but opposite order.
        The elements are renumbered to ensure that ``range(n)``
        is a linear extension.

        EXAMPLES::

            sage: P = posets.IntegerPartitions(4)                                       # needs sage.combinat
            sage: H = P._hasse_diagram; H                                               # needs sage.combinat
            Hasse diagram of a poset containing 5 elements
            sage: H.dual()                                                              # needs sage.combinat
            Hasse diagram of a poset containing 5 elements

        TESTS::

            sage: H = posets.IntegerPartitions(4)._hasse_diagram                        # needs sage.combinat
            sage: H.is_isomorphic( H.dual().dual() )                                    # needs sage.combinat
            True
            sage: H.is_isomorphic( H.dual() )                                           # needs sage.combinat
            False
        """
    def interval(self, x, y) -> list[int]:
        """
        Return a list of the elements `z` of ``self`` such that
        `x \\leq z \\leq y`.

        The order is that induced by the ordering in ``self.linear_extension``.

        INPUT:

        - ``x`` -- any element of the poset

        - ``y`` -- any element of the poset

        .. NOTE::

            The method :meth:`_precompute_intervals()` creates a cache
            which is used if available, making the function very fast.

        .. SEEALSO:: :meth:`interval_iterator`

        EXAMPLES::

            sage: uc = [[1,3,2],[4],[4,5,6],[6],[7],[7],[7],[]]
            sage: dag = DiGraph(dict(zip(range(len(uc)),uc)))
            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram(dag)
            sage: I = set([2,5,6,4,7])
            sage: I == set(H.interval(2,7))
            True
        """
    def interval_iterator(self, x, y) -> Iterator[int]:
        """
        Return an iterator of the elements `z` of ``self`` such that
        `x \\leq z \\leq y`.

        INPUT:

        - ``x`` -- any element of the poset

        - ``y`` -- any element of the poset

        .. SEEALSO:: :meth:`interval`

        .. NOTE::

            This becomes much faster when first calling :meth:`_leq_storage`,
            which precomputes the principal upper ideals.

        EXAMPLES::

            sage: uc = [[1,3,2],[4],[4,5,6],[6],[7],[7],[7],[]]
            sage: dag = DiGraph(dict(zip(range(len(uc)),uc)))
            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram(dag)
            sage: I = set([2,5,6,4,7])
            sage: I == set(H.interval_iterator(2,7))
            True
        """
    closed_interval = interval
    def open_interval(self, x, y) -> list[int]:
        """
        Return a list of the elements `z` of ``self`` such that `x < z < y`.

        The order is that induced by the ordering in ``self.linear_extension``.

        EXAMPLES::

            sage: uc = [[1,3,2],[4],[4,5,6],[6],[7],[7],[7],[]]
            sage: dag = DiGraph(dict(zip(range(len(uc)),uc)))
            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram(dag)
            sage: set([5,6,4]) == set(H.open_interval(2,7))
            True
            sage: H.open_interval(7,2)
            []
        """
    def rank_function(self):
        '''
        Return the (normalized) rank function of the poset,
        if it exists.

        A *rank function* of a poset `P` is a function `r`
        that maps elements of `P` to integers and satisfies:
        `r(x) = r(y) + 1` if `x` covers `y`. The function `r`
        is normalized such that its minimum value on every
        connected component of the Hasse diagram of `P` is
        `0`. This determines the function `r` uniquely (when
        it exists).

        OUTPUT:

        - a lambda function, if the poset admits a rank function
        - ``None``, if the poset does not admit a rank function

        EXAMPLES::

            sage: P = Poset([[1,3,2],[4],[4,5,6],[6],[7],[7],[7],[]])
            sage: P.rank_function() is not None
            True
            sage: P = Poset(([1,2,3,4],[[1,4],[2,3],[3,4]]), facade = True)
            sage: P.rank_function() is not None
            True
            sage: P = Poset(([1,2,3,4,5],[[1,2],[2,3],[3,4],[1,5],[5,4]]), facade = True)
            sage: P.rank_function() is not None
            False
            sage: P = Poset(([1,2,3,4,5,6,7,8],[[1,4],[2,3],[3,4],[5,7],[6,7]]), facade = True)
            sage: f = P.rank_function(); f is not None
            True
            sage: f(5)
            0
            sage: f(2)
            0

        TESTS::

            sage: P = Poset([[1,3,2],[4],[4,5,6],[6],[7],[7],[7],[]])
            sage: r = P.rank_function()
            sage: for u,v in P.cover_relations_iterator():
            ....:     if r(v) != r(u) + 1:
            ....:         print("Bug in rank_function!")

        ::

            sage: Q = Poset([[1,2],[4],[3],[4],[]])
            sage: Q.rank_function() is None
            True

        test for issue :issue:`14006`::

            sage: H = Poset()._hasse_diagram
            sage: s = dumps(H)
            sage: f = H.rank_function()
            sage: s = dumps(H)
        '''
    def rank(self, element=None):
        """
        Return the rank of ``element``, or the rank of the poset if
        ``element`` is ``None``. (The rank of a poset is the length of
        the longest chain of elements of the poset.)

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: H.rank(5)
            2
            sage: H.rank()
            3
            sage: Q = HasseDiagram({0:[1,2],1:[3],2:[],3:[]})
            sage: Q.rank()
            2
            sage: Q.rank(1)
            1
        """
    def is_ranked(self) -> bool:
        """
        Return ``True`` if the poset is ranked, and ``False`` otherwise.

        A poset is *ranked* if it admits a rank function. For more information
        about the rank function, see :meth:`~rank_function`
        and :meth:`~is_graded`.

        EXAMPLES::

            sage: P = Poset([[1],[2],[3],[4],[]])
            sage: P.is_ranked()
            True
            sage: Q = Poset([[1,5],[2,6],[3],[4],[],[6,3],[4]])
            sage: Q.is_ranked()
            False
        """
    def covers(self, x, y) -> bool:
        """
        Return ``True`` if y covers x and ``False`` otherwise.

        EXAMPLES::

            sage: Q = Poset([[1,5],[2,6],[3],[4],[],[6,3],[4]])
            sage: Q.covers(Q(1),Q(6))
            True
            sage: Q.covers(Q(1),Q(4))
            False
        """
    def upper_covers_iterator(self, element) -> Iterator[int]:
        """
        Return the list of elements that cover ``element``.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: list(H.upper_covers_iterator(0))
            [1, 2, 3]
            sage: list(H.upper_covers_iterator(7))
            []
        """
    def lower_covers_iterator(self, element) -> Iterator[int]:
        """
        Return the list of elements that are covered by ``element``.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: list(H.lower_covers_iterator(0))
            []
            sage: list(H.lower_covers_iterator(4))
            [1, 2]
        """
    def cardinality(self):
        """
        Return the number of elements in the poset.

        EXAMPLES::

            sage: Poset([[1,2,3],[4],[4],[4],[]]).cardinality()
            5

        TESTS:

        For a time, this function was named ``size()``, which
        would override the same-named method of the underlying
        digraph. :issue:`8735` renamed this method to ``cardinality()``
        with a deprecation warning. :issue:`11214` removed the warning
        since code for graphs was raising the warning inadvertently.
        This tests that ``size()`` for a Hasse diagram returns the
        number of edges in the digraph. ::

            sage: L = posets.BooleanLattice(5)
            sage: H = L.hasse_diagram()
            sage: H.size()
            80
            sage: H.size() == H.num_edges()
            True
        """
    def moebius_function(self, i, j):
        '''
        Return the value of the Möbius function of the poset
        on the elements ``i`` and ``j``.

        EXAMPLES::

            sage: P = Poset([[1,2,3],[4],[4],[4],[]])
            sage: H = P._hasse_diagram
            sage: H.moebius_function(0,4)
            2
            sage: for u,v in P.cover_relations_iterator():
            ....:     if P.moebius_function(u,v) != -1:
            ....:         print("Bug in moebius_function!")
        '''
    def bottom_moebius_function(self, j):
        """
        Return the value of the Möbius function of the poset
        on the elements ``zero`` and ``j``, where ``zero`` is
        ``self.bottom()``, the unique minimal element of the poset.

        EXAMPLES::

            sage: P = Poset({0: [1,2]})
            sage: hasse = P._hasse_diagram
            sage: hasse.bottom_moebius_function(1)
            -1
            sage: hasse.bottom_moebius_function(2)
            -1
            sage: P = Poset({0: [1,3], 1:[2], 2:[4], 3:[4]})
            sage: hasse = P._hasse_diagram
            sage: for i in range(5):
            ....:   print(hasse.bottom_moebius_function(i))
            1
            -1
            0
            -1
            1

        TESTS::

            sage: P = Poset({0:[2], 1:[2]})
            sage: hasse = P._hasse_diagram
            sage: hasse.bottom_moebius_function(1)
            Traceback (most recent call last):
            ...
            ValueError: the poset does not have a bottom element
        """
    def moebius_function_matrix(self, algorithm: str = 'cython'):
        """
        Return the matrix of the Möbius function of this poset.

        This returns the matrix over `\\ZZ` whose ``(x, y)`` entry
        is the value of the Möbius function of ``self`` evaluated on
        ``x`` and ``y``, and redefines :meth:`moebius_function` to use it.

        INPUT:

        - ``algorithm`` -- ``'recursive'``, ``'matrix'`` or ``'cython'``
          (default)

        This uses either the recursive formula, a generic matrix inversion
        or a specific matrix inversion coded in Cython.

        OUTPUT: a dense matrix for the algorithm ``cython``, a sparse matrix otherwise

        .. NOTE::

            The result is cached in :meth:`_moebius_function_matrix`.

        .. SEEALSO:: :meth:`lequal_matrix`, :meth:`coxeter_transformation`

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: H.moebius_function_matrix()                                           # needs sage.libs.flint sage.modules
            [ 1 -1 -1 -1  1  0  1  0]
            [ 0  1  0  0 -1  0  0  0]
            [ 0  0  1  0 -1 -1 -1  2]
            [ 0  0  0  1  0  0 -1  0]
            [ 0  0  0  0  1  0  0 -1]
            [ 0  0  0  0  0  1  0 -1]
            [ 0  0  0  0  0  0  1 -1]
            [ 0  0  0  0  0  0  0  1]

        TESTS::

            sage: # needs sage.libs.flint sage.modules
            sage: H.moebius_function_matrix().is_immutable()
            True
            sage: hasattr(H,'_moebius_function_matrix')
            True
            sage: H.moebius_function == H._moebius_function_from_matrix
            True
            sage: H = posets.TamariLattice(3)._hasse_diagram
            sage: M = H.moebius_function_matrix('matrix'); M
            [ 1 -1 -1  0  1]
            [ 0  1  0  0 -1]
            [ 0  0  1 -1  0]
            [ 0  0  0  1 -1]
            [ 0  0  0  0  1]
            sage: _ = H.__dict__.pop('_moebius_function_matrix')
            sage: H.moebius_function_matrix('cython') == M
            True
            sage: _ = H.__dict__.pop('_moebius_function_matrix')
            sage: H.moebius_function_matrix('recursive') == M
            True
            sage: _ = H.__dict__.pop('_moebius_function_matrix')
            sage: H.moebius_function_matrix('banana')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm
        """
    @cached_method
    def coxeter_transformation(self, algorithm: str = 'cython'):
        """
        Return the matrix of the Auslander-Reiten translation acting on
        the Grothendieck group of the derived category of modules on the
        poset, in the basis of simple modules.

        INPUT:

        - ``algorithm`` -- ``'cython'`` (default) or ``'matrix'``

        This uses either a specific matrix code in Cython, or generic matrices.

        .. SEEALSO:: :meth:`lequal_matrix`, :meth:`moebius_function_matrix`

        EXAMPLES::

            sage: # needs sage.libs.flint sage.modules
            sage: P = posets.PentagonPoset()._hasse_diagram
            sage: M = P.coxeter_transformation(); M
            [ 0  0  0  0 -1]
            [ 0  0  0  1 -1]
            [ 0  1  0  0 -1]
            [-1  1  1  0 -1]
            [-1  1  0  1 -1]
            sage: P.__dict__['coxeter_transformation'].clear_cache()
            sage: P.coxeter_transformation(algorithm='matrix') == M
            True

        TESTS::

            sage: # needs sage.libs.flint sage.modules
            sage: P = posets.PentagonPoset()._hasse_diagram
            sage: M = P.coxeter_transformation()
            sage: M**8 == 1
            True
            sage: P.__dict__['coxeter_transformation'].clear_cache()
            sage: P.coxeter_transformation(algorithm='banana')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm
        """
    def order_filter(self, elements) -> list[int]:
        """
        Return the order filter generated by a list of elements.

        `I` is an order filter if, for any `x` in `I` and `y` such that
        `y \\ge x`, then `y` is in `I`.

        EXAMPLES::

            sage: H = posets.BooleanLattice(4)._hasse_diagram
            sage: H.order_filter([3,8])
            [3, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        """
    def principal_order_filter(self, i) -> list[int]:
        """
        Return the order filter generated by ``i``.

        EXAMPLES::

            sage: H = posets.BooleanLattice(4)._hasse_diagram
            sage: H.principal_order_filter(2)
            [2, 3, 6, 7, 10, 11, 14, 15]
        """
    def order_ideal(self, elements) -> list[int]:
        """
        Return the order ideal generated by a list of elements.

        `I` is an order ideal if, for any `x` in `I` and `y` such that
        `y \\le x`, then `y` is in `I`.

        EXAMPLES::

            sage: H = posets.BooleanLattice(4)._hasse_diagram
            sage: H.order_ideal([7,10])
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
        """
    def order_ideal_cardinality(self, elements):
        """
        Return the cardinality of the order ideal generated by ``elements``.

        `I` is an order ideal if, for any `x` in `I` and `y` such that
        `y \\le x`, then `y` is in `I`.

        EXAMPLES::

            sage: H = posets.BooleanLattice(4)._hasse_diagram
            sage: H.order_ideal_cardinality([7,10])
            10
        """
    def principal_order_ideal(self, i) -> list[int]:
        """
        Return the order ideal generated by `i`.

        EXAMPLES::

            sage: H = posets.BooleanLattice(4)._hasse_diagram
            sage: H.principal_order_ideal(6)
            [0, 2, 4, 6]
        """
    def lequal_matrix(self, boolean: bool = False):
        """
        Return a matrix whose ``(i,j)`` entry is 1 if ``i`` is less
        than ``j`` in the poset, and 0 otherwise.

        INPUT:

        - ``boolean`` -- flag (default: ``False``); whether to
          return a matrix with coefficients in `\\GF(2)` or in `\\ZZ`

        .. SEEALSO::

            :meth:`moebius_function_matrix`, :meth:`coxeter_transformation`

        EXAMPLES::

            sage: P = Poset([[1,3,2],[4],[4,5,6],[6],[7],[7],[7],[]])
            sage: H = P._hasse_diagram
            sage: M = H.lequal_matrix(); M                                              # needs sage.modules
            [1 1 1 1 1 1 1 1]
            [0 1 0 1 0 0 0 1]
            [0 0 1 1 1 0 1 1]
            [0 0 0 1 0 0 0 1]
            [0 0 0 0 1 0 0 1]
            [0 0 0 0 0 1 1 1]
            [0 0 0 0 0 0 1 1]
            [0 0 0 0 0 0 0 1]
            sage: M.base_ring()                                                         # needs sage.modules
            Integer Ring

            sage: P = posets.DiamondPoset(6)
            sage: H = P._hasse_diagram
            sage: M = H.lequal_matrix(boolean=True)                                     # needs sage.modules
            sage: M.base_ring()                                                         # needs sage.modules
            Finite Field of size 2

        TESTS::

            sage: H.lequal_matrix().is_immutable()                                      # needs sage.modules
            True
        """
    def prime_elements(self) -> tuple[list[int], list[int]]:
        """
        Return the join-prime and meet-prime elements of the bounded poset.

        An element `x` of a poset `P` is join-prime if the subposet
        induced by `\\{y \\in P \\mid y \\not\\ge x\\}` has a top element.
        Meet-prime is defined dually.

        .. NOTE::

            The poset is expected to be bounded, and this is *not* checked.

        OUTPUT:

        A pair `(j, m)` where `j` is a list of join-prime elements
        and `m` is a list of meet-prime elements.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3], 2: [4], 3: [4]})
            sage: H.prime_elements()
            ([1, 2], [2, 3])
        """
    def meet_matrix(self):
        """
        Return the matrix of meets of ``self``, when ``self`` is a
        meet-semilattice; raise an error otherwise.

        The ``(x,y)``-entry of this matrix is the meet of ``x`` and
        ``y`` in ``self``.

        This algorithm is modelled after the algorithm of Freese-Jezek-Nation
        (p217). It can also be found on page 140 of [Gec81]_.

        .. NOTE::

            If ``self`` is a meet-semilattice, then the return of this method
            is the same as :meth:`_meet`. Once the matrix has been computed,
            it is stored in :meth:`_meet`. Delete this attribute if you want to
            recompute the matrix.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: H.meet_matrix()                                                       # needs sage.modules
            [0 0 0 0 0 0 0 0]
            [0 1 0 0 1 0 0 1]
            [0 0 2 0 2 2 2 2]
            [0 0 0 3 0 0 3 3]
            [0 1 2 0 4 2 2 4]
            [0 0 2 0 2 5 2 5]
            [0 0 2 3 2 2 6 6]
            [0 1 2 3 4 5 6 7]

        REFERENCE:

        .. [Gec81] Fundamentals of Computation Theory
          Gecseg, F.
          Proceedings of the 1981 International Fct-Conference
          Szeged, Hungaria, August 24-28, vol 117
          Springer-Verlag, 1981

        TESTS::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[2,3],1:[2,3]})
            sage: H.meet_matrix()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

            sage: H = HasseDiagram({0:[1,2],1:[3,4],2:[3,4]})
            sage: H.meet_matrix()                                                       # needs sage.modules
            Traceback (most recent call last):
            ...
            LatticeError: no meet for ...
        """
    def is_meet_semilattice(self) -> bool:
        """
        Return ``True`` if ``self`` has a meet operation, and
        ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: H.is_meet_semilattice()                                               # needs sage.modules
            True

            sage: H = HasseDiagram({0:[1,2],1:[3],2:[3],3:[]})
            sage: H.is_meet_semilattice()                                               # needs sage.modules
            True

            sage: H = HasseDiagram({0:[2,3],1:[2,3]})
            sage: H.is_meet_semilattice()                                               # needs sage.modules
            False

            sage: H = HasseDiagram({0:[1,2],1:[3,4],2:[3,4]})
            sage: H.is_meet_semilattice()                                               # needs sage.modules
            False
        """
    def join_matrix(self):
        """
        Return the matrix of joins of ``self``, when ``self`` is a
        join-semilattice; raise an error otherwise.

        The ``(x,y)``-entry of this matrix is the join of ``x`` and
        ``y`` in ``self``.

        This algorithm is modelled after the algorithm of Freese-Jezek-Nation
        (p217). It can also be found on page 140 of [Gec81]_.

        .. NOTE::

            If ``self`` is a join-semilattice, then the return of this method
            is the same as :meth:`_join`. Once the matrix has been computed,
            it is stored in :meth:`_join`. Delete this attribute if you want
            to recompute the matrix.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: H.join_matrix()                                                       # needs sage.modules
            [0 1 2 3 4 5 6 7]
            [1 1 4 7 4 7 7 7]
            [2 4 2 6 4 5 6 7]
            [3 7 6 3 7 7 6 7]
            [4 4 4 7 4 7 7 7]
            [5 7 5 7 7 5 7 7]
            [6 7 6 6 7 7 6 7]
            [7 7 7 7 7 7 7 7]

        TESTS::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[2,3],1:[2,3]})
            sage: H.join_matrix()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element

            sage: H = HasseDiagram({0:[2,3],1:[2,3],2:[4],3:[4]})
            sage: H.join_matrix()                                                       # needs sage.modules
            Traceback (most recent call last):
            ...
            LatticeError: no join for ...
        """
    def is_join_semilattice(self) -> bool:
        """
        Return ``True`` if ``self`` has a join operation, and
        ``False`` otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,3,2],1:[4],2:[4,5,6],3:[6],4:[7],5:[7],6:[7],7:[]})
            sage: H.is_join_semilattice()                                               # needs sage.modules
            True
            sage: H = HasseDiagram({0:[2,3],1:[2,3]})
            sage: H.is_join_semilattice()                                               # needs sage.modules
            False
            sage: H = HasseDiagram({0:[2,3],1:[2,3],2:[4],3:[4]})
            sage: H.is_join_semilattice()                                               # needs sage.modules
            False
        """
    def find_nonsemidistributive_elements(self, meet_or_join) -> None | tuple:
        """
        Check if the lattice is semidistributive or not.

        INPUT:

        - ``meet_or_join`` -- string ``'meet'`` or ``'join'``
          to decide if to check for join-semidistributivity or
          meet-semidistributivity

        OUTPUT:

        - ``None`` if the lattice is semidistributive OR
        - tuple ``(u, e, x, y)`` such that
          `u = e \\vee x = e \\vee y` but `u \\neq e \\vee (x \\wedge y)`
          if ``meet_or_join=='join'`` and
          `u = e \\wedge x = e \\wedge y` but `u \\neq e \\wedge (x \\vee y)`
          if ``meet_or_join=='meet'``

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1, 2], 1:[3, 4], 2:[4, 5], 3:[6],
            ....:                   4:[6], 5:[6]})
            sage: H.find_nonsemidistributive_elements('join') is None                   # needs sage.modules
            False
            sage: H.find_nonsemidistributive_elements('meet') is None                   # needs sage.modules
            True
        """
    def vertical_decomposition(self, return_list: bool = False):
        '''
        Return vertical decomposition of the lattice.

        This is the backend function for vertical decomposition
        functions of lattices.

        The property of being vertically decomposable is defined for lattices.
        This is *not* checked, and the function works with any bounded poset.

        INPUT:

        - ``return_list`` -- boolean (default: ``False``); if ``False`` (the
          default), return an element that is not the top neither the bottom
          element of the lattice, but is comparable to all elements of the
          lattice, if the lattice is vertically decomposable and ``None``
          otherwise. If ``True``, return list of decomposition elements.

        EXAMPLES::

            sage: H = posets.BooleanLattice(4)._hasse_diagram
            sage: H.vertical_decomposition() is None
            True
            sage: P = Poset( ([1,2,3,6,12,18,36], attrcall("divides")) )
            sage: P._hasse_diagram.vertical_decomposition()
            3
            sage: P._hasse_diagram.vertical_decomposition(return_list=True)
            [3]
        '''
    def is_complemented(self) -> int | None:
        """
        Return an element of the lattice that has no complement.

        If the lattice is complemented, return ``None``.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram

            sage: H = HasseDiagram({0:[1, 2], 1:[3], 2:[3], 3:[4]})
            sage: H.is_complemented()                                                   # needs sage.modules
            1

            sage: H = HasseDiagram({0:[1, 2, 3], 1:[4], 2:[4], 3:[4]})
            sage: H.is_complemented() is None                                           # needs sage.modules
            True
        """
    def pseudocomplement(self, element) -> int | None:
        """
        Return the pseudocomplement of ``element``, if it exists.

        The pseudocomplement is the greatest element whose
        meet with given element is the bottom element. It may
        not exist, and then the function returns ``None``.

        INPUT:

        - ``element`` -- an element of the lattice

        OUTPUT:

        An element of the Hasse diagram, i.e. an integer, or
        ``None`` if the pseudocomplement does not exist.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3], 2: [4], 3: [4]})
            sage: H.pseudocomplement(2)                                                 # needs sage.modules
            3

            sage: H = HasseDiagram({0: [1, 2, 3], 1: [4], 2: [4], 3: [4]})
            sage: H.pseudocomplement(2) is None                                         # needs sage.modules
            True
        """
    def orthocomplementations_iterator(self) -> Iterator[list[int]]:
        '''
        Return an iterator over orthocomplementations of the lattice.

        OUTPUT: an iterator that gives plain list of integers

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,2], 1:[3,4], 3:[5], 4:[5], 2:[6,7],
            ....:                   6:[8], 7:[8], 5:[9], 8:[9]})
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            [[9, 8, 5, 6, 7, 2, 3, 4, 1, 0], [9, 8, 5, 7, 6, 2, 4, 3, 1, 0]]

        ALGORITHM:

        As ``DiamondPoset(2*n+2)`` has `(2n)!/(n!2^n)` different
        orthocomplementations, the complexity of listing all of
        them is necessarily `O(n!)`.

        An orthocomplemented lattice is self-dual, so that for example
        orthocomplement of an atom is a coatom. This function
        basically just computes list of possible orthocomplementations
        for every element (i.e. they must be complements and "duals"),
        and then tries to fit them all.

        TESTS:

        Special and corner cases::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram()  # Empty
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            [[]]
            sage: H = HasseDiagram({0:[]})  # One element
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            [[0]]
            sage: H = HasseDiagram({0:[1]})  # Two elements
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            [[1, 0]]

        Trivial cases: odd number of elements, not self-dual, not complemented::

            sage: H = posets.DiamondPoset(5)._hasse_diagram
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            []
            sage: H = posets.ChainPoset(4)._hasse_diagram
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            []
            sage: H = HasseDiagram( ([[0, 1], [0, 2], [0, 3], [1, 4], [1, 8], [4, 6], [4, 7], [6, 9], [7, 9], [2, 5], [3, 5], [5, 8], [8, 9]]) )
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            []
            sage: H = HasseDiagram({0:[1, 2, 3], 1: [4], 2:[4], 3: [5], 4:[5]})
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            []

        Complemented, self-dual and even number of elements, but
        not orthocomplemented::

            sage: H = HasseDiagram( ([[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [0, 6], [3, 7], [5, 7], [6, 7]]) )
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            []

        Unique orthocomplementations; second is not uniquely complemented,
        but has only one orthocomplementation::

            sage: H = posets.BooleanLattice(4)._hasse_diagram  # Uniquely complemented
            sage: len(list(H.orthocomplementations_iterator()))                         # needs sage.groups
            1
            sage: H = HasseDiagram({0:[1, 2], 1:[3], 2:[4], 3:[5], 4:[5]})
            sage: len([_ for _ in H.orthocomplementations_iterator()])                  # needs sage.groups
            1

        "Lengthening diamond" must keep the number of orthocomplementations::

            sage: H = HasseDiagram( ([[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [2, 5], [3, 5], [4, 5]]) )
            sage: n = len([_ for _ in H.orthocomplementations_iterator()]); n           # needs sage.groups
            3
            sage: H = HasseDiagram(\'M]??O?@??C??OA???OA??@?A??C?A??O??\')
            sage: len([_ for _ in H.orthocomplementations_iterator()]) == n             # needs sage.groups
            True

        This lattice has an unique "possible orthocomplement" for every
        element, but they can not be fit together; orthocomplement pairs
        would be 0-11, 1-7, 2-4, 3-10, 5-9 and 6-8, and then orthocomplements
        for chain 0-1-6-11 would be 11-7-8-0, which is not a chain::

            sage: H = HasseDiagram(\'KTGG_?AAC?O?o?@?@?E?@?@??\')
            sage: list(H.orthocomplementations_iterator())                              # needs sage.groups
            []
        '''
    def find_nonsemimodular_pair(self, upper) -> tuple[int, int]:
        """
        Return pair of elements showing the lattice is not modular.

        INPUT:

        - ``upper`` -- boolean; if ``True``, test whether the lattice is
          upper semimodular. Otherwise test whether the lattice is
          lower semimodular.

        OUTPUT:

        ``None``, if the lattice is semimodular. Pair `(a, b)` violating
        semimodularity otherwise.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1, 2], 1:[3, 4], 2:[4, 5], 3:[6], 4:[6], 5:[6]})
            sage: H.find_nonsemimodular_pair(upper=True) is None
            True
            sage: H.find_nonsemimodular_pair(upper=False)
            (5, 3)

            sage: H_ = HasseDiagram(H.reverse().relabel(lambda x: 6-x, inplace=False))
            sage: H_.find_nonsemimodular_pair(upper=True)
            (3, 1)
            sage: H_.find_nonsemimodular_pair(upper=False) is None
            True
        """
    def antichains_iterator(self) -> Iterator[list[int]]:
        """
        Return an iterator over the antichains of the poset.

        .. NOTE::

            The algorithm is based on Freese-Jezek-Nation p. 226.
            It does a depth first search through the set of all
            antichains organized in a prefix tree.

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = posets.PentagonPoset()
            sage: H = P._hasse_diagram
            sage: H.antichains_iterator()
            <generator object ...antichains_iterator at ...>
            sage: list(H.antichains_iterator())
            [[], [4], [3], [2], [1], [1, 3], [1, 2], [0]]
            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0:[1,2],1:[4],2:[3],3:[4]})
            sage: list(H.antichains_iterator())
            [[], [4], [3], [2], [1], [1, 3], [1, 2], [0]]
            sage: H = HasseDiagram({0:[],1:[],2:[]})
            sage: list(H.antichains_iterator())
            [[], [2], [1], [1, 2], [0], [0, 2], [0, 1], [0, 1, 2]]
            sage: H = HasseDiagram({0:[1],1:[2],2:[3],3:[4]})
            sage: list(H.antichains_iterator())
            [[], [4], [3], [2], [1], [0]]

        TESTS::

            sage: H = Poset()._hasse_diagram
            sage: list(H.antichains_iterator())                                         # needs sage.modules
            [[]]
        """
    def are_incomparable(self, i, j) -> bool:
        """
        Return whether ``i`` and ``j`` are incomparable in the poset.

        INPUT:

        - ``i``, ``j`` -- vertices of this Hasse diagram

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = posets.PentagonPoset()
            sage: H = P._hasse_diagram
            sage: H.are_incomparable(1,2)
            True
            sage: V = H.vertices(sort=True)
            sage: [ (i,j) for i in V for j in V if H.are_incomparable(i,j)]
            [(1, 2), (1, 3), (2, 1), (3, 1)]
        """
    def are_comparable(self, i, j) -> bool:
        """
        Return whether ``i`` and ``j`` are comparable in the poset.

        INPUT:

        - ``i``, ``j`` -- vertices of this Hasse diagram

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = posets.PentagonPoset()
            sage: H = P._hasse_diagram
            sage: H.are_comparable(1,2)
            False
            sage: V = H.vertices(sort=True)
            sage: [ (i,j) for i in V for j in V if H.are_comparable(i,j)]
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 4),
             (2, 0), (2, 2), (2, 3), (2, 4), (3, 0), (3, 2), (3, 3), (3, 4),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        """
    def antichains(self, element_class=...):
        """
        Return all antichains of ``self``, organized as a prefix tree.

        INPUT:

        - ``element_class`` -- (default: ``list``) an iterable type

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = posets.PentagonPoset()
            sage: H = P._hasse_diagram
            sage: A = H.antichains()
            sage: list(A)
            [[], [0], [1], [1, 2], [1, 3], [2], [3], [4]]
            sage: A.cardinality()
            8
            sage: [1,3] in A
            True
            sage: [1,4] in A
            False

        TESTS::

            sage: # needs sage.modules
            sage: TestSuite(A).run()
            sage: A = Poset()._hasse_diagram.antichains()
            sage: list(A)
            [[]]
            sage: TestSuite(A).run()
        """
    def chains(self, element_class=..., exclude=None, conversion=None):
        """
        Return all chains of ``self``, organized as a prefix tree.

        INPUT:

        - ``element_class`` -- (default: ``list``) an iterable type

        - ``exclude`` -- elements of the poset to be excluded
          (default: ``None``)

        - ``conversion`` -- (default: ``None``) used to pass
          the list of elements of the poset in their fixed order

        OUTPUT:

        The enumerated set (with a forest structure given by prefix
        ordering) consisting of all chains of ``self``, each of
        which is given as an ``element_class``.

        If ``conversion`` is given, then the chains are converted
        to chain of elements of this list.

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = posets.PentagonPoset()
            sage: H = P._hasse_diagram
            sage: A = H.chains()
            sage: list(A)
            [[], [0], [0, 1], [0, 1, 4], [0, 2], [0, 2, 3], [0, 2, 3, 4], [0, 2, 4],
             [0, 3], [0, 3, 4], [0, 4], [1], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4],
             [3], [3, 4], [4]]
            sage: A.cardinality()
            20
            sage: [1,3] in A
            False
            sage: [1,4] in A
            True

        One can exclude some vertices::

            sage: # needs sage.modules
            sage: list(H.chains(exclude=[4, 3]))
            [[], [0], [0, 1], [0, 2], [1], [2]]

        The ``element_class`` keyword determines how the chains are
        being returned::

            sage: P = Poset({1: [2, 3], 2: [4]})
            sage: list(P._hasse_diagram.chains(element_class=tuple))
            [(), (0,), (0, 1), (0, 1, 2), (0, 2), (0, 3), (1,), (1, 2), (2,), (3,)]
            sage: list(P._hasse_diagram.chains())
            [[], [0], [0, 1], [0, 1, 2], [0, 2], [0, 3], [1], [1, 2], [2], [3]]

        (Note that taking the Hasse diagram has renamed the vertices.) ::

            sage: list(P._hasse_diagram.chains(element_class=tuple, exclude=[0]))
            [(), (1,), (1, 2), (2,), (3,)]

        .. SEEALSO:: :meth:`antichains`
        """
    def chain_polynomial(self):
        """
        Return the chain polynomial of the poset.

        The coefficient of `q^k` is the number of chains of `k`
        elements in the poset. List of coefficients of this polynomial
        is also called a *f-vector* of the poset.

        EXAMPLES::

            sage: P = posets.ChainPoset(3)
            sage: H = P._hasse_diagram
            sage: t = H.chain_polynomial(); t
            q^3 + 3*q^2 + 3*q + 1
        """
    def linear_intervals_count(self) -> Iterator[int]:
        """
        Return the enumeration of linear intervals w.r.t. their cardinality.

        An interval is linear if it is a total order.

        OUTPUT: an iterator of integers

        .. SEEALSO:: :meth:`is_linear_interval`

        EXAMPLES::

            sage: P = posets.BubblePoset(3,3)
            sage: H = P._hasse_diagram
            sage: list(H.linear_intervals_count())
            [245, 735, 438, 144, 24]
        """
    def is_linear_interval(self, t_min, t_max) -> bool:
        """
        Return whether the interval ``[t_min, t_max]`` is linear.

        This means that this interval is a total order.

        EXAMPLES::

            sage: # needs sage.modules
            sage: P = posets.PentagonPoset()
            sage: H = P._hasse_diagram
            sage: H.is_linear_interval(0, 4)
            False
            sage: H.is_linear_interval(0, 3)
            True
            sage: H.is_linear_interval(1, 3)
            False
            sage: H.is_linear_interval(1, 1)
            True

        TESTS::

            sage: P = posets.TamariLattice(3)
            sage: H = P._hasse_diagram
            sage: D = H._leq_storage
            sage: a, b = H.bottom(), H.top()
            sage: H.is_linear_interval(a, b)
            False
            sage: H.is_linear_interval(a, a)
            True
        """
    def diamonds(self) -> tuple[list[tuple[int]], bool]:
        """
        Return the list of diamonds of ``self``.

        A diamond is the following subgraph of the Hasse diagram::

                    z
                   / \\\n                  x   y
                   \\ /
                    w

        Thus each edge represents a cover relation in the Hasse diagram.
        We represent his as the tuple `(w, x, y, z)`.

        OUTPUT: a tuple with

        - a list of all diamonds in the Hasse Diagram,
        - a boolean checking that every `w,x,y` that form a ``V``, there is a
          unique element `z`, which completes the diamond.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1,2], 1: [3], 2: [3], 3: []})
            sage: H.diamonds()
            ([(0, 1, 2, 3)], True)

            sage: P = posets.YoungDiagramPoset(Partition([3, 2, 2]))                    # needs sage.combinat sage.modules
            sage: H = P._hasse_diagram                                                  # needs sage.combinat sage.modules
            sage: H.diamonds()                                                          # needs sage.combinat sage.modules
            ([(0, 1, 3, 4), (3, 4, 5, 6)], False)
        """
    def common_upper_covers(self, vertices) -> list[int]:
        """
        Return the list of all common upper covers of ``vertices``.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1,2], 1: [3], 2: [3], 3: []})
            sage: H.common_upper_covers([1, 2])
            [3]

            sage: from sage.combinat.posets.poset_examples import Posets
            sage: H = Posets.YoungDiagramPoset(Partition([3, 2, 2]))._hasse_diagram     # needs sage.combinat sage.modules
            sage: H.common_upper_covers([4, 5])                                         # needs sage.combinat sage.modules
            [6]
        """
    def common_lower_covers(self, vertices) -> list[int]:
        """
        Return the list of all common lower covers of ``vertices``.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1,2], 1: [3], 2: [3], 3: []})
            sage: H.common_lower_covers([1, 2])
            [0]

            sage: from sage.combinat.posets.poset_examples import Posets
            sage: H = Posets.YoungDiagramPoset(Partition([3, 2, 2]))._hasse_diagram     # needs sage.combinat sage.modules
            sage: H.common_lower_covers([4, 5])                                         # needs sage.combinat sage.modules
            [3]
        """
    def sublattices_iterator(self, elms, min_e) -> Iterator[set[int]]:
        """
        Return an iterator over sublattices of the Hasse diagram.

        INPUT:

        - ``elms`` -- elements already in sublattice; use set() at start
        - ``min_e`` -- smallest new element to add for new sublattices

        OUTPUT: list of sublattices as sets of integers

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1:[3], 2:[3]})
            sage: it = H.sublattices_iterator(set(), 0); it
            <generator object ...sublattices_iterator at ...>
            sage: next(it)                                                              # needs sage.modules
            set()
            sage: next(it)                                                              # needs sage.modules
            {0}
        """
    def maximal_sublattices(self) -> list[set[int]]:
        """
        Return maximal sublattices of the lattice.

        EXAMPLES::

            sage: L = posets.PentagonPoset()                                            # needs sage.modules
            sage: ms = L._hasse_diagram.maximal_sublattices()                           # needs sage.modules
            sage: sorted(ms, key=sorted)                                                # needs sage.modules
            [{0, 1, 2, 4}, {0, 1, 3, 4}, {0, 2, 3, 4}]
        """
    def frattini_sublattice(self) -> list[int]:
        """
        Return the list of elements of the Frattini sublattice of the lattice.

        EXAMPLES::

            sage: H = posets.PentagonPoset()._hasse_diagram                             # needs sage.modules
            sage: H.frattini_sublattice()                                               # needs sage.modules
            [0, 4]
        """
    def kappa_dual(self, a) -> int | None:
        """
        Return the minimum element smaller than the element covering
        ``a`` but not smaller than ``a``.

        Define `\\kappa^*(a)` as the minimum element of
        `(\\downarrow a_*) \\setminus (\\downarrow a)`, where `a_*` is the element
        covering `a`. It is always a join-irreducible element, if it exists.

        .. NOTE::

            Element ``a`` is expected to be meet-irreducible, and
            this is *not* checked.

        INPUT:

        - ``a`` -- a join-irreducible element of the lattice

        OUTPUT:

        The element `\\kappa^*(a)` or ``None`` if there
        is not a unique smallest element with given constraints.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [6], 4: [6], 5: [6]})
            sage: H.kappa_dual(3)
            2
            sage: H.kappa_dual(4) is None
            True

        TESTS::

            sage: H = HasseDiagram({0: [1]})
            sage: H.kappa_dual(0)
            1
        """
    def skeleton(self) -> list[int]:
        """
        Return the skeleton of the lattice.

        The lattice is expected to be pseudocomplemented and non-empty.

        The skeleton of the lattice is the subposet induced by
        those elements that are the pseudocomplement to at least one
        element.

        OUTPUT:

        List of elements such that the subposet induced by them is
        the skeleton of the lattice.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3, 4], 2: [4],
            ....:                   3: [5], 4: [5]})
            sage: H.skeleton()                                                          # needs sage.modules
            [5, 2, 0, 3]
        """
    def is_convex_subset(self, S) -> bool:
        """
        Return ``True`` if `S` is a convex subset of the poset,
        and ``False`` otherwise.

        A subset `S` is *convex* in the poset if `b \\in S` whenever
        `a, c \\in S` and `a \\le b \\le c`.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: B3 = HasseDiagram({0: [1, 2, 4], 1: [3, 5], 2: [3, 6],
            ....:                    3: [7], 4: [5, 6], 5: [7], 6: [7]})
            sage: B3.is_convex_subset([1, 3, 5, 4])  # Also connected
            True
            sage: B3.is_convex_subset([1, 3, 4])  # Not connected
            True

            sage: B3.is_convex_subset([0, 1, 2, 3, 6])  # No, 0 < 4 < 6
            False
            sage: B3.is_convex_subset([0, 1, 2, 7])  # No, 1 < 3 < 7.
            False

        TESTS::

            sage: B3.is_convex_subset([])
            True
            sage: B3.is_convex_subset([6])
            True
        """
    def neutral_elements(self) -> set[int]:
        """
        Return the list of neutral elements of the lattice.

        An element `a` in a lattice is neutral if the sublattice
        generated by `a`, `x` and `y` is distributive for every
        `x`, `y` in the lattice.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [4], 2: [3], 3: [4, 5],
            ....:                   4: [6], 5: [6]})
            sage: sorted(H.neutral_elements())                                          # needs sage.modules
            [0, 4, 6]

        ALGORITHM:

        Basically we just check the distributivity against all element
        pairs `x, y` to see if element `a` is neutral or not.

        If we found that `a, x, y` is not a distributive triple, we add
        all three to list of non-neutral elements. If we found `a` to
        be neutral, we add it to list of neutral elements. When testing
        we skip already found neutral elements, as they can't be our `x`
        or `y`.

        We skip `a, x, y` as trivial if it is a chain. We do that by
        letting `x` to be a non-comparable to `a`; `y` can be any element.

        We first try to found `x` and `y` from elements not yet tested,
        so that we could get three birds with one stone.

        And last, the top and bottom elements are always neutral and
        need not be tested.
        """
    def kappa(self, a) -> int | None:
        """
        Return the maximum element greater than the element covered
        by ``a`` but not greater than ``a``.

        Define `\\kappa(a)` as the maximum element of
        `(\\uparrow a_*) \\setminus (\\uparrow a)`, where `a_*` is the element
        covered by `a`. It is always a meet-irreducible element, if it exists.

        .. NOTE::

            Element ``a`` is expected to be join-irreducible, and
            this is *not* checked.

        INPUT:

        - ``a`` -- a join-irreducible element of the lattice

        OUTPUT:

        The element `\\kappa(a)` or ``None`` if there
        is not a unique greatest element with given constraints.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2, 3], 1: [4], 2: [4, 5], 3: [5], 4: [6], 5: [6]})
            sage: H.kappa(1)
            5
            sage: H.kappa(2) is None
            True

        TESTS::

            sage: H = HasseDiagram({0: [1]})
            sage: H.kappa(1)
            0
        """
    def atoms_of_congruence_lattice(self) -> list:
        '''
        Return atoms of the congruence lattice.

        In other words, return "minimal non-trivial" congruences:
        A congruence is minimal if the only finer (as a partition
        of set of elements) congruence is the trivial congruence
        where every block contains only one element.

        .. SEEALSO:: :meth:`congruence`

        OUTPUT:

        List of congruences, every congruence as
        :class:`sage.combinat.set_partition.SetPartition`

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: N5 = HasseDiagram({0: [1, 2], 1: [4], 2: [3], 3:[4]})
            sage: N5.atoms_of_congruence_lattice()                                      # needs sage.combinat sage.modules
            [{{0}, {1}, {2, 3}, {4}}]
            sage: Hex = HasseDiagram({0: [1, 2], 1: [3], 2: [4], 3: [5], 4: [5]})
            sage: Hex.atoms_of_congruence_lattice()                                     # needs sage.combinat sage.modules
            [{{0}, {1}, {2, 4}, {3}, {5}}, {{0}, {1, 3}, {2}, {4}, {5}}]

        ALGORITHM:

        Every atom is a join-irreducible. Every join-irreducible of
        `\\mathrm{Con}(L)` is a principal congruence generated by a
        meet-irreducible element and the only element covering it (and also
        by a join-irreducible element and the only element covered by it).
        Hence we check those principal congruences to find the minimal ones.
        '''
    def congruence(self, parts, start=None, stop_pairs=None):
        '''
        Return the congruence ``start`` "extended" by ``parts``.

        ``start`` is assumed to be a valid congruence of the lattice,
        and this is *not* checked.

        INPUT:

        - ``parts`` -- list of lists; congruences to add
        - ``start`` -- a disjoint set; already computed congruence (or ``None``)
        - ``stop_pairs`` -- list of pairs; list of pairs for stopping computation

        OUTPUT:

        ``None``, if the congruence generated by ``start`` and ``parts``
        together contains a block that has elements `a, b` so that ``(a, b)``
        is in the list ``stop_pairs``. Otherwise the least congruence that
        contains a block whose subset is `p` for every `p` in ``parts`` or
        ``start``, given as :class:`sage.sets.disjoint_set.DisjointSet_class`.

        ALGORITHM:

        Use the quadrilateral argument from page 120 of [Dav1997]_.

        Basically we take one block from todo-list, search quadrilateral
        blocks up and down against the block, and then complete them to
        closed intervals and add to todo-list.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [3], 2: [4], 3: [4]})
            sage: cong = H.congruence([[0, 1]]); cong                                   # needs sage.modules
            {{0, 1, 3}, {2, 4}}
            sage: H.congruence([[0, 2]], start=cong)                                    # needs sage.modules
            {{0, 1, 2, 3, 4}}

            sage: H.congruence([[0, 1]], stop_pairs=[(1, 3)]) is None                   # needs sage.modules
            True

        TESTS::

            sage: H = HasseDiagram(\'HT@O?GO?OE?G@??\')
            sage: H.congruence([[0, 1]]).number_of_subsets()                            # needs sage.modules
            1
            sage: H = HasseDiagram(\'HW_oC?@@O@?O@??\')
            sage: H.congruence([[0, 1]]).number_of_subsets()                            # needs sage.modules
            1

        Check :issue:`21861`::

            sage: H = HasseDiagram({0: [1, 2], 1: [3], 2: [4], 3: [4]})
            sage: tmp = H.congruence([[1, 3]])                                          # needs sage.modules
            sage: tmp.number_of_subsets()                                               # needs sage.modules
            4
            sage: H.congruence([[0, 1]], start=tmp).number_of_subsets()                 # needs sage.modules
            2
            sage: tmp.number_of_subsets()                                               # needs sage.modules
            4
        '''
    def find_nontrivial_congruence(self):
        """
        Return a pair that generates non-trivial congruence or
        ``None`` if there is not any.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram({0: [1, 2], 1: [5], 2: [3, 4], 3: [5], 4: [5]})
            sage: H.find_nontrivial_congruence()                                        # needs sage.modules
            {{0, 1}, {2, 3, 4, 5}}

            sage: H = HasseDiagram({0: [1, 2, 3], 1: [4], 2: [4], 3: [4]})
            sage: H.find_nontrivial_congruence() is None                                # needs sage.modules
            True

        ALGORITHM:

        See https://www.math.hawaii.edu/~ralph/Preprints/conlat.pdf:

        If `\\Theta` is a join irreducible element of a `\\mathrm{Con}(L)`,
        then there is at least one join-irreducible `j` and one
        meet-irreducible `m` such that `\\Theta` is both the principal
        congruence generated by `(j^*, j)`, where `j^*` is the unique
        lower cover of `j`, and the principal congruence generated by
        `(m, m^*)`, where `m^*` is the unique upper cover of `m`.

        So, we only check join irreducibles or meet irreducibles,
        whichever is a smaller set. To optimize more we stop computation
        whenever it finds a pair that we know to generate one-element
        congruence.
        """
    def principal_congruences_poset(self):
        """
        Return the poset of join-irreducibles of the congruence lattice.

        OUTPUT:

        A pair `(P, D)` where `P` is a poset and `D` is a dictionary.

        Elements of `P` are pairs `(x, y)` such that `x` is an element
        of the lattice and `y` is an element covering it. In the poset
        `(a, b)` is less than `(c, d)` iff the principal congruence
        generated by `(a, b)` is refinement of the principal congruence
        generated by `(c, d)`.

        `D` is a dictionary from pairs `(x, y)` to the congruence
        (given as DisjointSet) generated by the pair.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: N5 = HasseDiagram({0: [1, 2], 1: [4], 2: [3], 3: [4]})
            sage: P, D = N5.principal_congruences_poset()                               # needs sage.combinat sage.modules
            sage: P                                                                     # needs sage.combinat sage.modules
            Finite poset containing 3 elements
            sage: P.bottom()                                                            # needs sage.combinat sage.modules
            (2, 3)
            sage: D[(2, 3)]                                                             # needs sage.combinat sage.modules
            {{0}, {1}, {2, 3}, {4}}
        """
    def congruences_iterator(self) -> Iterator:
        """
        Return an iterator over all congruences of the lattice.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram('GY@OQ?OW@?O?')
            sage: it = H.congruences_iterator(); it
            <generator object ...>
            sage: sorted([cong.number_of_subsets() for cong in it])                     # needs sage.combinat sage.modules
            [1, 2, 2, 2, 4, 4, 4, 8]
        """
    def is_congruence_normal(self) -> bool:
        """
        Return ``True`` if the lattice can be constructed from the one-element
        lattice with Day doubling constructions of convex subsets.

        Subsets to double does not need to be lower nor upper pseudo-intervals.
        On the other hand they must be convex, i.e. doubling a non-convex but
        municipal subset will give a lattice that returns ``False`` from
        this function.

        EXAMPLES::

            sage: from sage.combinat.posets.hasse_diagram import HasseDiagram
            sage: H = HasseDiagram('IX?Q@?AG?OG?W?O@??')
            sage: H.is_congruence_normal()                                              # needs sage.combinat sage.modules
            True

        The 5-element diamond is the smallest non-example::

            sage: H = HasseDiagram({0: [1, 2, 3], 1: [4], 2: [4], 3: [4]})
            sage: H.is_congruence_normal()                                              # needs sage.combinat sage.modules
            False

        This is done by doubling a non-convex subset::

            sage: H = HasseDiagram('OQC?a?@CO?G_C@?GA?O??_??@?BO?A_?G??C??_?@???')
            sage: H.is_congruence_normal()                                              # needs sage.combinat sage.modules
            False

        TESTS::

            sage: HasseDiagram().is_congruence_normal()                                 # needs sage.combinat sage.modules
            True
            sage: HasseDiagram({0: []}).is_congruence_normal()                          # needs sage.combinat sage.modules
            True

        ALGORITHM:

        See http://www.math.hawaii.edu/~jb/inflation.pdf
        """

__doc__: Incomplete
