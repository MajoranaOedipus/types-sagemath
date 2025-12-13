from sage.categories.homset import Homset as Homset
from sage.manifolds.continuous_map import ContinuousMap as ContinuousMap
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TopologicalManifoldHomset(UniqueRepresentation, Homset):
    """
    Set of continuous maps between two topological manifolds.

    Given two topological manifolds `M` and `N` over a topological field `K`,
    the class :class:`TopologicalManifoldHomset` implements the set
    `\\mathrm{Hom}(M, N)` of morphisms (i.e. continuous maps) `M \\to N`.

    This is a Sage *parent* class, whose *element* class is
    :class:`~sage.manifolds.continuous_map.ContinuousMap`.

    INPUT:

    - ``domain`` -- :class:`~sage.manifolds.manifold.TopologicalManifold`;
      the domain topological manifold `M` of the morphisms
    - ``codomain`` -- :class:`~sage.manifolds.manifold.TopologicalManifold`;
      the codomain topological manifold `N` of the morphisms
    - ``name`` -- (default: ``None``) string; the name of ``self``;
      if ``None``, ``Hom(M,N)`` will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
      ``self``; if ``None``, `\\mathrm{Hom}(M,N)` will be used

    EXAMPLES:

    Set of continuous maps between a 2-dimensional manifold and a
    3-dimensional one::

        sage: M = Manifold(2, 'M', structure='topological')
        sage: X.<x,y> = M.chart()
        sage: N = Manifold(3, 'N', structure='topological')
        sage: Y.<u,v,w> = N.chart()
        sage: H = Hom(M, N) ; H
        Set of Morphisms from 2-dimensional topological manifold M to
         3-dimensional topological manifold N in Category of manifolds over
         Real Field with 53 bits of precision
        sage: type(H)
        <class 'sage.manifolds.manifold_homset.TopologicalManifoldHomset_with_category'>
        sage: H.category()
        Category of homsets of topological spaces
        sage: latex(H)
        \\mathrm{Hom}\\left(M,N\\right)
        sage: H.domain()
        2-dimensional topological manifold M
        sage: H.codomain()
        3-dimensional topological manifold N

    An element of ``H`` is a continuous map from ``M`` to ``N``::

        sage: H.Element
        <class 'sage.manifolds.continuous_map.ContinuousMap'>
        sage: f = H.an_element() ; f
        Continuous map from the 2-dimensional topological manifold M to the
         3-dimensional topological manifold N
        sage: f.display()
        M → N
           (x, y) ↦ (u, v, w) = (0, 0, 0)

    The test suite is passed::

        sage: TestSuite(H).run()

    When the codomain coincides with the domain, the homset is a set of
    *endomorphisms* in the category of topological manifolds::

        sage: E = Hom(M, M) ; E
        Set of Morphisms from 2-dimensional topological manifold M to
         2-dimensional topological manifold M in Category of manifolds over
         Real Field with 53 bits of precision
        sage: E.category()
        Category of endsets of topological spaces
        sage: E.is_endomorphism_set()
        True
        sage: E is End(M)
        True

    In this case, the homset is a monoid for the law of morphism composition::

        sage: E in Monoids()
        True

    This was of course not the case of ``H = Hom(M, N)``::

        sage: H in Monoids()
        False

    The identity element of the monoid is of course the identity map of ``M``::

        sage: E.one()
        Identity map Id_M of the 2-dimensional topological manifold M
        sage: E.one() is M.identity_map()
        True
        sage: E.one().display()
        Id_M: M → M
           (x, y) ↦ (x, y)

    The test suite is passed by ``E``::

        sage: TestSuite(E).run()

    This test suite includes more tests than in the case of ``H``, since ``E``
    has some extra structure (monoid).
    """
    Element = ContinuousMap
    def __init__(self, domain, codomain, name=None, latex_name=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: N = Manifold(3, 'N', structure='topological')
            sage: Y.<u,v,w> = N.chart()
            sage: H = Hom(M, N) ; H
            Set of Morphisms from 2-dimensional topological manifold M to
             3-dimensional topological manifold N in Category of manifolds
             over Real Field with 53 bits of precision
            sage: TestSuite(H).run()

        Test for an endomorphism set::

            sage: E = Hom(M, M) ; E
            Set of Morphisms from 2-dimensional topological manifold M to
             2-dimensional topological manifold M in Category of manifolds over
             Real Field with 53 bits of precision
            sage: TestSuite(E).run()

        Check whether :issue:`31233` is solved::

            sage: S1 = manifolds.Sphere(1)
            sage: iota = S1.embedding()
            sage: phi = S1.identity_map()
            sage: iota * phi
            Differentiable map iota from the 1-sphere S^1 of radius 1 smoothly
             embedded in the Euclidean plane E^2 to the Euclidean plane E^2
        """
    def __call__(self, *args, **kwds):
        """
        Construct an element of ``self`` from the input.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: N = Manifold(3, 'N', structure='topological')
            sage: Y.<u,v,w> = N.chart()
            sage: H = Hom(M,N)
            sage: f = H.__call__({(X, Y): [x+y, x-y, x*y]}, name='f') ; f
            Continuous map f from the 2-dimensional topological manifold M to
             the 3-dimensional topological manifold N
            sage: f.display()
            f: M → N
               (x, y) ↦ (u, v, w) = (x + y, x - y, x*y)

        There is also the following shortcut for :meth:`one`::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: H = Hom(M, M)
            sage: H(1)
            Identity map Id_M of the 2-dimensional topological manifold M
        """
    @cached_method
    def one(self):
        """
        Return the identity element of ``self`` considered as a monoid
        (case of a set of endomorphisms).

        This applies only when the codomain of the homset is equal to its
        domain, i.e. when the homset is of the type `\\mathrm{Hom}(M,M)`.
        Indeed, `\\mathrm{Hom}(M,M)` equipped with the law of morphisms
        composition is a monoid, whose identity element is nothing but the
        identity map of `M`.

        OUTPUT:

        - the identity map of `M`, as an instance of
          :class:`~sage.manifolds.continuous_map.ContinuousMap`

        EXAMPLES:

        The identity map of a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: H = Hom(M, M) ; H
            Set of Morphisms from 2-dimensional topological manifold M to
             2-dimensional topological manifold M in Category of manifolds over
             Real Field with 53 bits of precision
            sage: H in Monoids()
            True
            sage: H.one()
            Identity map Id_M of the 2-dimensional topological manifold M
            sage: H.one().parent() is H
            True
            sage: H.one().display()
            Id_M: M → M
               (x, y) ↦ (x, y)

        The identity map is cached::

            sage: H.one() is H.one()
            True

        If the homset is not a set of endomorphisms, the identity element is
        meaningless::

            sage: N = Manifold(3, 'N', structure='topological')
            sage: Y.<u,v,w> = N.chart()
            sage: Hom(M, N).one()
            Traceback (most recent call last):
            ...
            TypeError: Set of Morphisms
             from 2-dimensional topological manifold M
             to 3-dimensional topological manifold N
             in Category of manifolds over Real Field with 53 bits of precision
             is not a monoid
        """
