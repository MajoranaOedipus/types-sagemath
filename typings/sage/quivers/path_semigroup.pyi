from .paths import QuiverPath as QuiverPath
from .representation import QuiverRep as QuiverRep
from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.monoids import Monoids as Monoids
from sage.categories.semigroups import Semigroups as Semigroups
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PathSemigroup(UniqueRepresentation, Parent):
    """
    The partial semigroup that is given by the directed paths of a quiver,
    subject to concatenation.

    See :mod:`~sage.quivers.representation` for a definition of this
    semigroup and of the notion of a path in a quiver.

    Note that a *partial semigroup* here is defined as a set `G` with a
    partial binary operation `G \\times G \\to G \\cup \\{\\mbox{None}\\}`,
    which is written infix as a `*` sign and satisfies associativity in
    the following sense: If `a`, `b` and `c` are three elements of `G`,
    and if one of the products `(a*b)*c` and `a*(b*c)` exists, then so
    does the other and the two products are equal. A partial semigroup
    is not required to have a neutral element (and this one usually has
    no such element).

    EXAMPLES::

        sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 2:{3:['d']}})
        sage: S = Q.path_semigroup()
        sage: S
        Partial semigroup formed by the directed paths of Multi-digraph on 3 vertices
        sage: S.variable_names()
        ('e_1', 'e_2', 'e_3', 'a', 'b', 'c', 'd')
        sage: S.gens()
        (e_1, e_2, e_3, a, b, c, d)
        sage: S.category()
        Category of finite enumerated semigroups

    In the test suite, we skip the associativity test, as in this example the
    paths used for testing cannot be concatenated::

        sage: TestSuite(S).run(skip=['_test_associativity'])

    If there is only a single vertex, the partial semigroup is a monoid. If
    the underlying quiver has cycles or loops, then the (partial) semigroup
    only is an infinite enumerated set. This time, there is no need to skip
    tests::

        sage: Q = DiGraph({1:{1:['a', 'b', 'c', 'd']}})
        sage: M = Q.path_semigroup()
        sage: M
        Monoid formed by the directed paths of Looped multi-digraph on 1 vertex
        sage: M.category()
        Category of infinite enumerated monoids
        sage: TestSuite(M).run()
    """
    Element = QuiverPath
    @staticmethod
    def __classcall__(cls, Q):
        """
        Normalize the arguments passed to the constructor.

        The normalization consists of making an immutable copy of ``Q``
        that is made weighted.

        INPUT:

        - ``Q`` -- a :class:`~sage.graphs.digraph.DiGraph`

        TESTS::

            sage: G1 = DiGraph({1:{2:['a']}})
            sage: G2 = DiGraph({1:{2:['b']}})
            sage: P1 = G1.path_semigroup()
            sage: P2 = G2.path_semigroup()
            sage: G1 == G2 # equality of unweighted graphs ignores edge labels
            True
            sage: P1.quiver() == P2.quiver() # edge labels no longer ignored
            False
            sage: P1 == P2
            False
        """
    def __init__(self, Q) -> None:
        '''
        Initialize ``self``.

        INPUT:

        - ``Q`` -- a :class:`~sage.graphs.digraph.DiGraph`

        EXAMPLES:

        Note that usually a path semigroup is created using
        :meth:`sage.graphs.digraph.DiGraph.path_semigroup`. Here, we
        demonstrate the direct construction::

            sage: Q = DiGraph({1:{2:[\'a\',\'b\'], 3:[\'c\']}, 2:{3:[\'d\']}}, immutable=True)
            sage: from sage.quivers.path_semigroup import PathSemigroup
            sage: P = PathSemigroup(Q)
            sage: P is DiGraph({1:{2:[\'a\',\'b\'], 3:[\'c\']}, 2:{3:[\'d\']}}).path_semigroup() # indirect doctest
            True
            sage: P
            Partial semigroup formed by the directed paths of Multi-digraph on 3 vertices

        While hardly of any use, it is possible to construct the path
        semigroup of an empty quiver (it is, of course, empty)::

            sage: D = DiGraph({})
            sage: A = D.path_semigroup(); A
            Partial semigroup formed by the directed paths of Digraph on 0 vertices
            sage: A.list()
            []

        .. TODO::

            When the graph has more than one edge, the proper category would be
            a "partial semigroup" or a "semigroupoid" but definitely not a
            semigroup!
        '''
    @cached_method
    def arrows(self):
        """
        Return the elements corresponding to edges of the underlying quiver.

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}}).path_semigroup()
            sage: P.arrows()
            (a, b, c, d)
        """
    @cached_method
    def idempotents(self):
        """
        Return the idempotents corresponding to the vertices of the
        underlying quiver.

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}}).path_semigroup()
            sage: P.idempotents()
            (e_1, e_2, e_3)
        """
    def ngens(self):
        """
        Return the number of generators (:meth:`arrows` and
        :meth:`idempotents`).

        EXAMPLES::

            sage: F = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}}).path_semigroup()
            sage: F.ngens()
            7
        """
    @cached_method
    def gen(self, i):
        """
        Return generator number `i`.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        An idempotent, if `i` is smaller than the number of vertices,
        or an arrow otherwise.

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}}).path_semigroup()
            sage: P.1         # indirect doctest
            e_2
            sage: P.idempotents()[1]
            e_2
            sage: P.5
            c
            sage: P.gens()[5]
            c
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the tuple of generators.

        .. NOTE::

            This coincides with the sum of the output of
            :meth:`idempotents` and :meth:`arrows`.

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}}).path_semigroup()
            sage: P.gens()
            (e_1, e_2, e_3, a, b, c, d)
            sage: P.gens() == P.idempotents() + P.arrows()
            True
        """
    def is_finite(self) -> bool:
        """
        This partial semigroup is finite if and only if the underlying
        quiver is acyclic.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 2:{3:['d']}})
            sage: Q.path_semigroup().is_finite()
            True
            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}})
            sage: Q.path_semigroup().is_finite()
            False
        """
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 2:{3:['d']}})
            sage: F = Q.path_semigroup()
            sage: len(F)
            9
            sage: list(F)
            [e_1, e_2, e_3, a, b, c, d, a*d, b*d]
            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}})
            sage: F = Q.path_semigroup()
            sage: len(F)
            Traceback (most recent call last):
            ...
            ValueError: the underlying quiver has cycles, thus, there may be an infinity of directed paths
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 2:{3:['d']}})
            sage: F = Q.path_semigroup()
            sage: F.cardinality()
            9
            sage: A = F.algebra(QQ)
            sage: list(A.basis())
            [e_1, e_2, e_3, a, b, c, d, a*d, b*d]
            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}})
            sage: F = Q.path_semigroup()
            sage: F.cardinality()
            +Infinity
            sage: A = F.algebra(QQ)
            sage: list(A.basis())
            Traceback (most recent call last):
            ...
            ValueError: the underlying quiver has cycles, thus, there may be an infinity of directed paths
        """
    def __iter__(self):
        """
        Iterate over the elements of ``self``, i.e., over quiver paths.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 2:{3:['d']}})
            sage: P = Q.path_semigroup()
            sage: list(P)
            [e_1, e_2, e_3, a, b, c, d, a*d, b*d]

        The elements are sorted by length. Of course, the list of elements
        is infinite for quivers with cycles. ::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['d']}, 3:{1:['c']}})
            sage: P = Q.path_semigroup()
            sage: P.is_finite()
            False
            sage: list(P)
            Traceback (most recent call last):
            ...
            ValueError: the underlying quiver has cycles, thus, there may be an infinity of directed paths

         However, one can iterate::

            sage: counter = 0
            sage: for p in P:
            ....:     counter += 1
            ....:     print(p)
            ....:     if counter==20:
            ....:         break
            e_1
            e_2
            e_3
            a
            b
            d
            c
            a*d
            b*d
            d*c
            c*a
            c*b
            a*d*c
            b*d*c
            d*c*a
            d*c*b
            c*a*d
            c*b*d
            a*d*c*a
            a*d*c*b
        """
    def iter_paths_by_length_and_startpoint(self, d, v) -> Generator[Incomplete]:
        """
        An iterator over quiver paths with a fixed length and start point.

        INPUT:

        - ``d`` -- integer; the path length
        - ``v`` -- a vertex; start point of the paths

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['d']}, 3:{1:['c']}})
            sage: P = Q.path_semigroup()
            sage: P.is_finite()
            False
            sage: list(P.iter_paths_by_length_and_startpoint(4,1))
            [a*d*c*a, a*d*c*b, b*d*c*a, b*d*c*b]
            sage: list(P.iter_paths_by_length_and_startpoint(5,1))
            [a*d*c*a*d, a*d*c*b*d, b*d*c*a*d, b*d*c*b*d]
            sage: list(P.iter_paths_by_length_and_startpoint(5,2))
            [d*c*a*d*c, d*c*b*d*c]

        TESTS::

             sage: Q = DiGraph({1:{1:['a','b', 'c', 'd']}})
             sage: P = Q.path_semigroup()
             sage: list(P.iter_paths_by_length_and_startpoint(2,1))
             [a*a,
              a*b,
              a*c,
              a*d,
              b*a,
              b*b,
              b*c,
              b*d,
              c*a,
              c*b,
              c*c,
              c*d,
              d*a,
              d*b,
              d*c,
              d*d]
             sage: len(list(P.iter_paths_by_length_and_startpoint(2,1)))
             16
        """
    def iter_paths_by_length_and_endpoint(self, d, v) -> Generator[Incomplete]:
        """
        An iterator over quiver paths with a fixed length and end point.

        INPUT:

        - ``d`` -- integer; the path length
        - ``v`` -- a vertex; end point of the paths

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['d']}, 3:{1:['c']}})
            sage: F = Q.path_semigroup()
            sage: F.is_finite()
            False
            sage: list(F.iter_paths_by_length_and_endpoint(4,1))
            [c*a*d*c, c*b*d*c]
            sage: list(F.iter_paths_by_length_and_endpoint(5,1))
            [d*c*a*d*c, d*c*b*d*c]
            sage: list(F.iter_paths_by_length_and_endpoint(5,2))
            [c*a*d*c*a, c*b*d*c*a, c*a*d*c*b, c*b*d*c*b]
        """
    def quiver(self):
        """
        Return the underlying quiver (i.e., digraph) of this path semigroup.

        .. NOTE::

            The returned digraph always is an immutable copy of the originally
            given digraph that is made weighted.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['d']}, 3:{1:['c']}},
            ....:             weighted=False)
            sage: F = Q.path_semigroup()
            sage: F.quiver() == Q
            False
            sage: Q.weighted(True)
            sage: F.quiver() == Q
            True
        """
    @cached_method
    def reverse(self):
        """
        The path semigroup of the reverse quiver.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['d']}, 3:{1:['c']}})
            sage: F = Q.path_semigroup()
            sage: F.reverse() is Q.reverse().path_semigroup()
            True
        """
    def algebra(self, k, order: str = 'negdegrevlex'):
        """
        Return the path algebra of the underlying quiver.

        INPUT:

        - ``k`` -- a commutative ring

        - ``order`` -- (optional) string, one of ``'negdegrevlex'`` (default),
          ``'degrevlex'``, ``'negdeglex'`` or ``'deglex'``, defining the
          monomial order to be used

        .. NOTE::

            Monomial orders that are not degree orders are not supported.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['d']}, 3:{1:['c']}})
            sage: P = Q.path_semigroup()
            sage: P.algebra(GF(3))
            Path algebra of Multi-digraph on 3 vertices over Finite Field of size 3

        Now some example with different monomial orderings::

            sage: P1 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'))
            sage: P2 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='degrevlex')
            sage: P3 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='negdeglex')
            sage: P4 = DiGraph({1:{1:['x','y','z']}}).path_semigroup().algebra(GF(25,'t'), order='deglex')
            sage: P1.order_string()
            'negdegrevlex'
            sage: sage_eval('(x+2*z+1)^3', P1.gens_dict())
            e_1 + z + 3*x + 2*z*z + x*z + z*x + 3*x*x + 3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x
            sage: sage_eval('(x+2*z+1)^3', P2.gens_dict())
            3*z*z*z + 4*x*z*z + 4*z*x*z + 2*x*x*z + 4*z*z*x + 2*x*z*x + 2*z*x*x + x*x*x + 2*z*z + x*z + z*x + 3*x*x + z + 3*x + e_1
            sage: sage_eval('(x+2*z+1)^3', P3.gens_dict())
            e_1 + z + 3*x + 2*z*z + z*x + x*z + 3*x*x + 3*z*z*z + 4*z*z*x + 4*z*x*z + 2*z*x*x + 4*x*z*z + 2*x*z*x + 2*x*x*z + x*x*x
            sage: sage_eval('(x+2*z+1)^3', P4.gens_dict())
            3*z*z*z + 4*z*z*x + 4*z*x*z + 2*z*x*x + 4*x*z*z + 2*x*z*x + 2*x*x*z + x*x*x + 2*z*z + z*x + x*z + 3*x*x + z + 3*x + e_1
        """
    def representation(self, k, *args, **kwds):
        """
        Return a representation of the quiver.

        For more information see the
        :class:`~sage.quivers.representation.QuiverRep` documentation.

        TESTS::

            sage: Q = DiGraph({1:{3:['a']}, 2:{3:['b']}}).path_semigroup()
            sage: spaces = {1: QQ^2, 2: QQ^3, 3: QQ^2}
            sage: maps = {(1, 3, 'a'): (QQ^2).Hom(QQ^2).identity(), (2, 3, 'b'): [[1, 0], [0, 0], [0, 0]]}
            sage: M = Q.representation(QQ, spaces, maps)
            sage: M
            Representation with dimension vector (2, 3, 2)
        """
    def S(self, k, vertex):
        """
        Return the simple module over `k` at the given vertex
        ``vertex``.

        This module is literally simple only when `k` is a field.

        INPUT:

        - ``k`` -- the base ring of the representation

        - ``vertex`` -- integer; a vertex of the quiver

        OUTPUT: :class:`~sage.quivers.representation.QuiverRep`; the simple
        module at ``vertex`` with base ring `k`

        EXAMPLES::

            sage: P = DiGraph({1:{2:['a','b']}, 2:{3:['c','d']}}).path_semigroup()
            sage: S1 = P.S(GF(3), 1)
            sage: P.S(ZZ, 3).dimension_vector()
            (0, 0, 1)
            sage: P.S(ZZ, 1).dimension_vector()
            (1, 0, 0)

        The vertex given must be a vertex of the quiver::

            sage: P.S(QQ, 4)
            Traceback (most recent call last):
            ...
            ValueError: must specify a valid vertex of the quiver
        """
    simple = S
    def P(self, k, vertex):
        """
        Return the indecomposable projective module over `k` at the given
        vertex ``vertex``.

        This module is literally indecomposable only when `k` is a field.

        INPUT:

        - ``k`` -- the base ring of the representation

        - ``vertex`` -- integer; a vertex of the quiver

        OUTPUT: :class:`~sage.quivers.representation.QuiverRep`, the
        indecomposable projective module at ``vertex`` with base ring `k`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c','d']}}).path_semigroup()
            sage: P2 = Q.P(GF(3), 2)
            sage: Q.P(ZZ, 3).dimension_vector()
            (0, 0, 1)
            sage: Q.P(ZZ, 1).dimension_vector()
            (1, 2, 4)

        The vertex given must be a vertex of the quiver::

            sage: Q.P(QQ, 4)
            Traceback (most recent call last):
            ...
            ValueError: must specify a valid vertex of the quiver
        """
    projective = P
    def I(self, k, vertex):
        """
        Return the indecomposable injective module over `k` at the
        given vertex ``vertex``.

        This module is literally indecomposable only when `k` is a field.

        INPUT:

        - ``k`` -- the base ring of the representation

        - ``vertex`` -- integer; a vertex of the quiver

        OUTPUT:

        - :class:`~sage.quivers.representation.QuiverRep`, the indecomposable
          injective module at vertex ``vertex`` with base ring `k`

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b']}, 2:{3:['c','d']}}).path_semigroup()
            sage: I2 = Q.I(GF(3), 2)
            sage: Q.I(ZZ, 3).dimension_vector()
            (4, 2, 1)
            sage: Q.I(ZZ, 1).dimension_vector()
            (1, 0, 0)

        The vertex given must be a vertex of the quiver::

            sage: Q.I(QQ, 4)
            Traceback (most recent call last):
            ...
            ValueError: must specify a valid vertex of the quiver
        """
    injective = I
    def free_module(self, k):
        """
        Return a free module of rank `1` over ``kP``, where `P` is
        ``self``. (In other words, the regular representation.)

        INPUT:

        - ``k`` -- ring; the base ring of the representation

        OUTPUT:

        - :class:`~sage.quivers.representation.QuiverRep_with_path_basis`, the
          path algebra considered as a right module over itself.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a', 'b'], 3: ['c', 'd']}, 2:{3:['e']}}).path_semigroup()
            sage: Q.free_module(GF(3)).dimension_vector()
            (1, 3, 6)
        """
    def all_paths(self, start=None, end=None):
        """
        List of all paths between a pair of vertices ``(start, end)``.

        INPUT:

        - ``start`` -- integer or ``None`` (default: ``None``); the initial
          vertex of the paths in the output; if ``None`` is given then
          the initial vertex is arbitrary.
        - ``end`` -- integer or ``None`` (default: ``None``); the terminal
          vertex of the paths in the output; if ``None`` is given then
          the terminal vertex is arbitrary

        OUTPUT: list of paths, excluding the invalid path

        .. TODO::

            This currently does not work for quivers with cycles, even if
            there are only finitely many paths from ``start`` to ``end``.

        .. NOTE::

            If there are multiple edges between two vertices, the method
            :meth:`sage.graphs.digraph.all_paths` will not differentiate
            between them. But this method, which is not for digraphs but for
            their path semigroup associated with them, will.

        EXAMPLES::

            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 2:{3:['d']}})
            sage: F = Q.path_semigroup()
            sage: F.all_paths(1, 3)
            [a*d, b*d, c]

        If ``start=end`` then we expect only the trivial path at that vertex::

            sage: F.all_paths(1, 1)
            [e_1]

        The empty list is returned if there are no paths between the
        given vertices::

            sage: F.all_paths(3, 1)
            []

        If ``end=None`` then all edge paths beginning at ``start`` are
        returned, including the trivial path::

            sage: F.all_paths(2)
            [e_2, d]

        If ``start=None`` then all edge paths ending at ``end`` are
        returned, including the trivial path.  Note that the two edges
        from vertex 1 to vertex 2 count as two different edge paths::

            sage: F.all_paths(None, 2)
            [a, b, e_2]
            sage: F.all_paths(end=2)
            [a, b, e_2]

        If ``start=end=None`` then all edge paths are returned, including
        trivial paths::

            sage: F.all_paths()
            [e_1, a, b, a*d, b*d, c, e_2, d, e_3]

        The vertex given must be a vertex of the quiver::

            sage: F.all_paths(1, 4)
            Traceback (most recent call last):
            ...
            ValueError: the end vertex 4 is not a vertex of the quiver

        If the underlying quiver is cyclic, a :exc:`ValueError`
        is raised::

            sage: Q = DiGraph({1:{2:['a','b'], 3:['c']}, 3:{1:['d']}})
            sage: F = Q.path_semigroup()
            sage: F.all_paths()
            Traceback (most recent call last):
            ...
            ValueError: the underlying quiver has cycles, thus, there may be an infinity of directed paths

        TESTS:

        We check a single edge with a multi-character label::

            sage: Q = DiGraph([[1,2,'abc']])
            sage: PQ = Q.path_semigroup()
            sage: PQ.all_paths(1,2)
            [abc]

        An example with multiple edges::

            sage: Q = DiGraph([[1,2,'abc'], [1,2,'def']], multiedges=True)
            sage: PQ = Q.path_semigroup()
            sage: PQ.all_paths(1,2)
            [abc, def]
        """
