from sage.manifolds.vector_bundle_fiber_element import VectorBundleFiberElement as VectorBundleFiberElement
from sage.symbolic.ring import SR as SR
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule as FiniteRankFreeModule

class VectorBundleFiber(FiniteRankFreeModule):
    """
    Fiber of a given vector bundle at a given point.

    Let `\\pi: E \\to M` be a vector bundle of rank `n` over the field `K`
    (see :class:`~sage.manifolds.vector_bundle.TopologicalVectorBundle`) and
    `p \\in M`. The fiber `E_p` at `p` is defined via `E_p := \\pi^{-1}(p)` and
    takes the structure of an `n`-dimensional vector space over the field `K`.

    INPUT:

    - ``vector_bundle`` -- :class:`~sage.manifolds.vector_bundle.TopologicalVectorBundle`;
      vector bundle `E` on which the fiber is defined
    - ``point`` -- :class:`~sage.manifolds.point.ManifoldPoint`;
      point `p` at which the fiber is defined

    EXAMPLES:

    A vector bundle fiber in a trivial rank 2 vector bundle over a
    4-dimensional topological manifold::

        sage: M = Manifold(4, 'M', structure='top')
        sage: X.<x,y,z,t> = M.chart()
        sage: p = M((0,0,0,0), name='p')
        sage: E = M.vector_bundle(2, 'E')
        sage: e = E.local_frame('e')
        sage: Ep = E.fiber(p); Ep
        Fiber of E at Point p on the 4-dimensional topological manifold M

    Fibers are free modules of finite rank over
    :class:`~sage.symbolic.ring.SymbolicRing`
    (actually vector spaces of finite dimension over the vector bundle
    field `K`, here `K=\\RR`)::

        sage: Ep.base_ring()
        Symbolic Ring
        sage: Ep.category()
        Category of finite dimensional vector spaces over Symbolic Ring
        sage: Ep.rank()
        2
        sage: dim(Ep)
        2

    The fiber is automatically endowed with bases deduced from the local frames
    around the point::

        sage: Ep.bases()
        [Basis (e_0,e_1) on the Fiber of E at Point p on the 4-dimensional
         topological manifold M]
        sage: E.frames()
        [Local frame (E|_M, (e_0,e_1))]

    At this stage, only one basis has been defined in the fiber, but new bases
    can be added from local frames on the vector bundle by means of the method
    :meth:`~sage.manifolds.local_frame.LocalFrame.at`::

        sage: aut = E.section_module().automorphism()
        sage: aut[:] = [[-1, x], [y, 2]]
        sage: f = e.new_frame(aut, 'f')
        sage: fp = f.at(p); fp
        Basis (f_0,f_1) on the Fiber of E at Point p on the 4-dimensional
         topological manifold M
        sage: Ep.bases()
        [Basis (e_0,e_1) on the Fiber of E at Point p on the 4-dimensional
         topological manifold M,
         Basis (f_0,f_1) on the Fiber of E at Point p on the 4-dimensional
         topological manifold M]

    The changes of bases are applied to the fibers::

        sage: f[1].display(e) # second component of frame f
        f_1 = x e_0 + 2 e_1
        sage: ep = e.at(p)
        sage: fp[1].display(ep) # second component of frame f at p
        f_1 = 2 e_1

    All the bases defined on ``Ep`` are on the same footing. Accordingly the
    fiber is not in the category of modules with a distinguished basis::

        sage: Ep in ModulesWithBasis(SR)
        False

    It is simply in the category of modules::

        sage: Ep in Modules(SR)
        True

    Since the base ring is a field, it is actually in the category of
    vector spaces::

        sage: Ep in VectorSpaces(SR)
        True

    A typical element::

        sage: v = Ep.an_element(); v
        Vector in the fiber of E at Point p on the 4-dimensional topological
         manifold M
        sage: v.display()
        e_0 + 2 e_1
        sage: v.parent()
        Fiber of E at Point p on the 4-dimensional topological manifold M

    The zero vector::

        sage: Ep.zero()
        Vector zero in the fiber of E at Point p on the 4-dimensional
         topological manifold M
        sage: Ep.zero().display()
        zero = 0
        sage: Ep.zero().parent()
        Fiber of E at Point p on the 4-dimensional topological manifold M

    Fibers are unique::

        sage: E.fiber(p) is Ep
        True
        sage: p1 = M.point((0,0,0,0))
        sage: E.fiber(p1) is Ep
        True

    even if points are different instances::

        sage: p1 is p
        False

    but ``p1`` and ``p`` share the same fiber because they compare equal::

        sage: p1 == p
        True

    .. SEEALSO::

        :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`
        for more documentation.
    """
    Element = VectorBundleFiberElement
    def __init__(self, vector_bundle, point) -> None:
        """
        Construct a fiber of a vector bundle.

        TESTS::

            sage: M = Manifold(3, 'M', structure='top')
            sage: X.<x,y,z> = M.chart()
            sage: p = M((0,0,0), name='p')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: Ep = E.fiber(p)
            sage: TestSuite(Ep).run()
        """
    def construction(self) -> None:
        """
        TESTS::

            sage: M = Manifold(3, 'M', structure='top')
            sage: X.<x,y,z> = M.chart()
            sage: p = M((0,0,0), name='p')
            sage: E = M.vector_bundle(2, 'E')
            sage: E.fiber(p).construction() is None
            True
        """
    def dimension(self):
        """
        Return the vector space dimension of ``self``.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: X.<x,y,z> = M.chart()
            sage: p = M((0,0,0), name='p')
            sage: E = M.vector_bundle(2, 'E')
            sage: Ep = E.fiber(p)
            sage: Ep.dim()
            2
        """
    dim = dimension
    def base_point(self):
        """
        Return the manifold point over which ``self`` is defined.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: p = M.point((3,-2), name='p')
            sage: Ep = E.fiber(p)
            sage: Ep.base_point()
            Point p on the 2-dimensional topological manifold M
            sage: p is Ep.base_point()
            True
        """
