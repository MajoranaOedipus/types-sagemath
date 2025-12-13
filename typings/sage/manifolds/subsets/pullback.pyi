from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.metric_spaces import MetricSpaces as MetricSpaces
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.manifolds.chart import Chart as Chart
from sage.manifolds.scalarfield import ScalarField as ScalarField
from sage.manifolds.subset import ManifoldSubset as ManifoldSubset
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module import FreeModule_generic as FreeModule_generic
from sage.modules.free_module_element import vector as vector
from sage.rings.complex_double import CDF as CDF
from sage.rings.infinity import infinity as infinity, minus_infinity as minus_infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.rings.real_lazy import CLF as CLF, RLF as RLF
from sage.sets.real_set import RealSet as RealSet
from sage.symbolic.ring import SR as SR

class ManifoldSubsetPullback(ManifoldSubset):
    """
    Manifold subset defined as a pullback of a subset under a continuous map.

    INPUT:

    - ``map`` -- an instance of :class:`~sage.manifolds.continuous_map.ContinuousMap`,
      :class:`ScalarField`, or :class:`Chart`

    - ``codomain_subset`` -- an instance of :class:`~sage.manifolds.subset.ManifoldSubset`,
      :class:`RealSet`, or :class:`~sage.geometry.convex_set.ConvexSet_base`

    EXAMPLES::

        sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
        sage: M = Manifold(2, 'R^2', structure='topological')
        sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2

    Pulling back a real interval under a scalar field::

        sage: r_squared = M.scalar_field(x^2+y^2)
        sage: r_squared.set_immutable()
        sage: cl_I = RealSet([1, 4]); cl_I
        [1, 4]
        sage: cl_O = ManifoldSubsetPullback(r_squared, cl_I); cl_O
        Subset f_inv_[1, 4] of the 2-dimensional topological manifold R^2
        sage: M.point((0, 0)) in cl_O
        False
        sage: M.point((0, 1)) in cl_O
        True

    Pulling back an open real interval gives an open subset::

        sage: I = RealSet((1, 4)); I
        (1, 4)
        sage: O = ManifoldSubsetPullback(r_squared, I); O
        Open subset f_inv_(1, 4) of the 2-dimensional topological manifold R^2
        sage: M.point((1, 0)) in O
        False
        sage: M.point((1, 1)) in O
        True

    Pulling back a polytope under a chart::

        sage: # needs sage.geometry.polyhedron
        sage: P = Polyhedron(vertices=[[0, 0], [1, 2], [2, 1]]); P
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
        sage: S = ManifoldSubsetPullback(c_cart, P); S
        Subset x_y_inv_P of the 2-dimensional topological manifold R^2
        sage: M((1, 2)) in S
        True
        sage: M((2, 0)) in S
        False

    Pulling back the interior of a polytope under a chart::

        sage: # needs sage.geometry.polyhedron
        sage: int_P = P.interior(); int_P
        Relative interior of a
         2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
        sage: int_S = ManifoldSubsetPullback(c_cart, int_P, name='int_S'); int_S
        Open subset int_S of the 2-dimensional topological manifold R^2
        sage: M((0, 0)) in int_S
        False
        sage: M((1, 1)) in int_S
        True

    Using the embedding map of a submanifold::

        sage: M = Manifold(3, 'M', structure='topological')
        sage: N = Manifold(2, 'N', ambient=M, structure='topological'); N
        2-dimensional topological submanifold N
         immersed in the 3-dimensional topological manifold M
        sage: CM.<x,y,z> = M.chart()
        sage: CN.<u,v> = N.chart()
        sage: t = var('t')
        sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
        sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
        sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
        sage: N.set_immersion(phi, inverse=phi_inv, var=t,
        ....:                 t_inverse={t: phi_inv_t})
        sage: N.declare_embedding()

        sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
        sage: S = M.open_subset('S', coord_def={CM: z<1})
        sage: phi_without_t = N.continuous_map(M, {(CN, CM): [expr.subs(t=0)
        ....:                                                 for expr in phi.expr()]})
        sage: phi_without_t
        Continuous map
         from the 2-dimensional topological submanifold N
          embedded in the 3-dimensional topological manifold M
         to the 3-dimensional topological manifold M
        sage: phi_without_t.expr()
        (u, v, u^2 + v^2)
        sage: D = ManifoldSubsetPullback(phi_without_t, S); D
        Subset f_inv_S of the 2-dimensional topological submanifold N
         embedded in the 3-dimensional topological manifold M
        sage: N.point((2,0)) in D
        False
    """
    @staticmethod
    def __classcall_private__(cls, map, codomain_subset, inverse=None, name=None, latex_name=None):
        """
        Normalize arguments and delegate to other constructors.

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: P = Polyhedron(vertices=[[0, 0], [1, 2], [3, 4]]); P
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: S = ManifoldSubsetPullback(c_cart, P); S
            Subset x_y_inv_P of the 2-dimensional topological manifold R^2
            sage: S is ManifoldSubsetPullback(c_cart, P)
            True
        """
    def __init__(self, map, codomain_subset, inverse, name, latex_name) -> None:
        """
        Construct a manifold subset that is a pullback.

        TESTS::

            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: r_squared = M.scalar_field(x^2+y^2)
            sage: r_squared.set_immutable()
            sage: cl_I = RealSet([1, 4]); cl_I
            [1, 4]
            sage: cl_O = ManifoldSubsetPullback(r_squared, cl_I); cl_O
            Subset f_inv_[1, 4] of the 2-dimensional topological manifold R^2
            sage: TestSuite(cl_O).run(skip='_test_elements')
        """
    def some_elements(self) -> Generator[Incomplete]:
        """
        Generate some elements of ``self``.

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(3, 'R^3', structure='topological')
            sage: c_cart.<x,y,z> = M.chart() # Cartesian coordinates on R^3
            sage: Cube = polytopes.cube(); Cube
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
            sage: McCube = ManifoldSubsetPullback(c_cart, Cube, name='McCube'); McCube
            Subset McCube of the 3-dimensional topological manifold R^3
            sage: L = list(McCube.some_elements()); L
            [Point on the 3-dimensional topological manifold R^3,
             Point on the 3-dimensional topological manifold R^3,
             Point on the 3-dimensional topological manifold R^3,
             Point on the 3-dimensional topological manifold R^3,
             Point on the 3-dimensional topological manifold R^3,
             Point on the 3-dimensional topological manifold R^3]
            sage: list(p.coordinates(c_cart) for p in L)
            [(0, 0, 0),
             (1, -1, -1),
             (1, 0, -1),
             (1, 1/2, 0),
             (1, -1/4, 1/2),
             (0, -5/8, 3/4)]

            sage: # needs sage.geometry.polyhedron
            sage: Empty = Polyhedron(ambient_dim=3)
            sage: McEmpty = ManifoldSubsetPullback(c_cart, Empty, name='McEmpty')
            sage: McEmpty
            Subset McEmpty of the 3-dimensional topological manifold R^3
            sage: list(McEmpty.some_elements())
            []
        """
    def __contains__(self, point) -> bool:
        """
        Check whether ``point`` is contained in ``self``.

        EXAMPLES::

            sage: # needs sage.geometry.polyhedron
            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(3, 'R^3', structure='topological')
            sage: c_cart.<x,y,z> = M.chart() # Cartesian coordinates on R^3
            sage: Cube = polytopes.cube(); Cube
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
            sage: Cube.vertices_list()
            [[1, -1, -1],
            [1, 1, -1],
            [1, 1, 1],
            [1, -1, 1],
            [-1, -1, 1],
            [-1, -1, -1],
            [-1, 1, -1],
            [-1, 1, 1]]
            sage: McCube = ManifoldSubsetPullback(c_cart, Cube, name='McCube'); McCube
            Subset McCube of the 3-dimensional topological manifold R^3
            sage: p = M.point((0, 0, 0)); p
            Point on the 3-dimensional topological manifold R^3
            sage: p in McCube
            True
            sage: q = M.point((2, 3, 4)); q
            Point on the 3-dimensional topological manifold R^3
            sage: q in McCube
            False
        """
    def is_open(self):
        """
        Return if ``self`` is (known to be) an open set.

        This version of the method always returns ``False``.

        Because the map is continuous, the pullback is open if the
        ``codomain_subset`` is open.

        However, the design of :class:`~sage.manifolds.subset.ManifoldSubset` requires that open subsets
        are instances of the subclass :class:`sage.manifolds.manifold.TopologicalManifold`.
        The constructor of :class:`ManifoldSubsetPullback` delegates to a subclass
        of :class:`sage.manifolds.manifold.TopologicalManifold` for some open subsets.

        EXAMPLES::

            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2

            sage: # needs sage.geometry.polyhedron
            sage: P = Polyhedron(vertices=[[0, 0], [1, 2], [3, 4]]); P
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.is_open()
            False
            sage: McP = ManifoldSubsetPullback(c_cart, P, name='McP'); McP
            Subset McP of the 2-dimensional topological manifold R^2
            sage: McP.is_open()
            False
        """
    def is_closed(self):
        """
        Return if ``self`` is (known to be) a closed subset of the manifold.

        EXAMPLES::

            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2

        The pullback of a closed real interval under a scalar field is closed::

            sage: r_squared = M.scalar_field(x^2+y^2)
            sage: r_squared.set_immutable()
            sage: cl_I = RealSet([1, 2]); cl_I
            [1, 2]
            sage: cl_O = ManifoldSubsetPullback(r_squared, cl_I); cl_O
            Subset f_inv_[1, 2] of the 2-dimensional topological manifold R^2
            sage: cl_O.is_closed()
            True

        The pullback of a (closed convex) polyhedron under a chart is closed::

            sage: # needs sage.geometry.polyhedron
            sage: P = Polyhedron(vertices=[[0, 0], [1, 2], [3, 4]]); P
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: McP = ManifoldSubsetPullback(c_cart, P, name='McP'); McP
            Subset McP of the 2-dimensional topological manifold R^2
            sage: McP.is_closed()
            True

        The pullback of real vector subspaces under a chart is closed::

            sage: V = span([[1, 2]], RR); V
            Vector space of degree 2 and dimension 1 over Real Field with 53 bits of precision
            Basis matrix:
            [1.00000000000000 2.00000000000000]
            sage: McV = ManifoldSubsetPullback(c_cart, V, name='McV'); McV
            Subset McV of the 2-dimensional topological manifold R^2
            sage: McV.is_closed()
            True

        The pullback of point lattices under a chart is closed::

            sage: W = span([[1, 0], [3, 5]], ZZ); W
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [1 0]
            [0 5]
            sage: McW = ManifoldSubsetPullback(c_cart, W, name='McW'); McW
            Subset McW of the 2-dimensional topological manifold R^2
            sage: McW.is_closed()
            True

        The pullback of finite sets is closed::

            sage: F = Family([vector(QQ, [1, 2], immutable=True), vector(QQ, [2, 3], immutable=True)])
            sage: McF = ManifoldSubsetPullback(c_cart, F, name='McF'); McF
            Subset McF of the 2-dimensional topological manifold R^2
            sage: McF.is_closed()
            True
        """
    def closure(self, name=None, latex_name=None):
        """
        Return the topological closure of ``self`` in the manifold.

        Because ``self`` is a pullback of some subset under a continuous map,
        the closure of ``self`` is the pullback of the closure.

        EXAMPLES::

            sage: from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: r_squared = M.scalar_field(x^2+y^2)
            sage: r_squared.set_immutable()
            sage: I = RealSet.open_closed(1, 2); I
            (1, 2]
            sage: O = ManifoldSubsetPullback(r_squared, I); O
            Subset f_inv_(1, 2] of the 2-dimensional topological manifold R^2
            sage: latex(O)
            f^{-1}((1, 2])
            sage: cl_O = O.closure(); cl_O
            Subset f_inv_[1, 2] of the 2-dimensional topological manifold R^2
            sage: cl_O.is_closed()
            True
        """
