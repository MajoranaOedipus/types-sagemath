from .simplicial_complex import Simplex as Simplex, SimplicialComplex as SimplicialComplex
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.categories.simplicial_complexes import SimplicialComplexes as SimplicialComplexes
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ

def is_SimplicialComplexMorphism(x):
    """
    Return ``True`` if and only if ``x`` is a morphism of simplicial complexes.

    EXAMPLES::

        sage: from sage.topology.simplicial_complex_morphism import is_SimplicialComplexMorphism
        sage: S = SimplicialComplex([[0,1],[3,4]], is_mutable=False)
        sage: H = Hom(S,S)
        sage: f = {0:0,1:1,3:3,4:4}
        sage: x = H(f)
        sage: is_SimplicialComplexMorphism(x)
        doctest:warning...
        DeprecationWarning: The function is_SimplicialComplexMorphism is deprecated;
        use 'isinstance(..., SimplicialComplexMorphism)' instead.
        See https://github.com/sagemath/sage/issues/38103 for details.
        True
    """

class SimplicialComplexMorphism(Morphism):
    """
    An element of this class is a morphism of simplicial complexes.
    """
    def __init__(self, f, X, Y) -> None:
        """
        Input is a dictionary ``f``, the domain ``X``, and the codomain ``Y``.

        One can define the dictionary on the vertices of `X`.

        EXAMPLES::

            sage: S = SimplicialComplex([[0,1],[2],[3,4],[5]], is_mutable=False)
            sage: H = Hom(S,S)
            sage: f = {0:0,1:1,2:2,3:3,4:4,5:5}
            sage: g = {0:0,1:1,2:0,3:3,4:4,5:0}
            sage: x = H(f)
            sage: y = H(g)
            sage: x == y
            False
            sage: x.image()
            Simplicial complex with vertex set (0, 1, 2, 3, 4, 5) and facets {(2,), (5,), (0, 1), (3, 4)}
            sage: y.image()
            Simplicial complex with vertex set (0, 1, 3, 4) and facets {(0, 1), (3, 4)}
            sage: x.image() == y.image()
            False
        """
    def __eq__(self, x):
        """
        Return ``True`` if and only if ``self == x``.

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: i
            Simplicial complex endomorphism of Minimal triangulation of the 2-sphere
              Defn: 0 |--> 0
                    1 |--> 1
                    2 |--> 2
                    3 |--> 3
            sage: f = {0:0,1:1,2:2,3:2}
            sage: j = H(f)
            sage: i==j
            False

            sage: T = SimplicialComplex([[1,2]], is_mutable=False)
            sage: T
            Simplicial complex with vertex set (1, 2) and facets {(1, 2)}
            sage: G = Hom(T,T)
            sage: k = G.identity()
            sage: g = {1:1,2:2}
            sage: l = G(g)
            sage: k == l
            True
        """
    def __call__(self, x, orientation: bool = False):
        """
        Input is a simplex of the domain. Output is the image simplex.

        If the optional argument ``orientation`` is ``True``, then this
        returns a pair ``(image simplex, oriented)`` where ``oriented``
        is 1 or `-1` depending on whether the map preserves or reverses
        the orientation of the image simplex.

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(2)
            sage: T = simplicial_complexes.Sphere(3)
            sage: S
            Minimal triangulation of the 2-sphere
            sage: T
            Minimal triangulation of the 3-sphere
            sage: f = {0:0,1:1,2:2,3:3}
            sage: H = Hom(S,T)
            sage: x = H(f)
            sage: from sage.topology.simplicial_complex import Simplex
            sage: x(Simplex([0,2,3]))
            (0, 2, 3)

        An orientation-reversing example::

            sage: X = SimplicialComplex([[0,1]], is_mutable=False)
            sage: g = Hom(X,X)({0:1, 1:0})
            sage: g(Simplex([0,1]))
            (0, 1)
            sage: g(Simplex([0,1]), orientation=True)                                   # needs sage.modules
            ((0, 1), -1)

        TESTS:

        Test that the problem in :issue:`36849` has been fixed::

            sage: S = SimplicialComplex([[1,2]],is_mutable=False).barycentric_subdivision()
            sage: T = SimplicialComplex([[1,2],[2,3],[1,3]],is_mutable=False).barycentric_subdivision()
            sage: f = {x[0]:x[0] for x in S.cells()[0]}
            sage: H = Hom(S,T)
            sage: z = H(f)
            sage: z.associated_chain_complex_morphism()
            Chain complex morphism:
              From: Chain complex with at most 2 nonzero terms over Integer Ring
              To:   Chain complex with at most 2 nonzero terms over Integer Ring
        """
    def associated_chain_complex_morphism(self, base_ring=..., augmented: bool = False, cochain: bool = False):
        """
        Return the associated chain complex morphism of ``self``.

        EXAMPLES::

            sage: # needs sage.modules
            sage: S = simplicial_complexes.Sphere(1)
            sage: T = simplicial_complexes.Sphere(2)
            sage: H = Hom(S, T)
            sage: f = {0:0, 1:1, 2:2}
            sage: x = H(f); x
            Simplicial complex morphism:
              From: Minimal triangulation of the 1-sphere
              To:   Minimal triangulation of the 2-sphere
              Defn: 0 |--> 0
                    1 |--> 1
                    2 |--> 2
            sage: a = x.associated_chain_complex_morphism(); a
            Chain complex morphism:
              From: Chain complex with at most 2 nonzero terms over Integer Ring
              To:   Chain complex with at most 3 nonzero terms over Integer Ring
            sage: a._matrix_dictionary
            {0: [1 0 0]
                [0 1 0]
                [0 0 1]
                [0 0 0],
             1: [1 0 0]
                [0 1 0]
                [0 0 0]
                [0 0 1]
                [0 0 0]
                [0 0 0],
             2: []}
            sage: x.associated_chain_complex_morphism(augmented=True)
            Chain complex morphism:
              From: Chain complex with at most 3 nonzero terms over Integer Ring
              To:   Chain complex with at most 4 nonzero terms over Integer Ring
            sage: x.associated_chain_complex_morphism(cochain=True)
            Chain complex morphism:
              From: Chain complex with at most 3 nonzero terms over Integer Ring
              To:   Chain complex with at most 2 nonzero terms over Integer Ring
            sage: x.associated_chain_complex_morphism(augmented=True, cochain=True)
            Chain complex morphism:
              From: Chain complex with at most 4 nonzero terms over Integer Ring
              To:   Chain complex with at most 3 nonzero terms over Integer Ring
            sage: x.associated_chain_complex_morphism(base_ring=GF(11))
            Chain complex morphism:
              From: Chain complex with at most 2 nonzero terms over Finite Field of size 11
              To:   Chain complex with at most 3 nonzero terms over Finite Field of size 11

        Some simplicial maps which reverse the orientation of a few simplices::

            sage: # needs sage.modules
            sage: g = {0:1, 1:2, 2:0}
            sage: H(g).associated_chain_complex_morphism()._matrix_dictionary
            {0: [0 0 1]
                [1 0 0]
                [0 1 0]
                [0 0 0],
             1: [ 0 -1  0]
                [ 0  0 -1]
                [ 0  0  0]
                [ 1  0  0]
                [ 0  0  0]
                [ 0  0  0],
             2: []}
            sage: X = SimplicialComplex([[0, 1]], is_mutable=False)
            sage: Hom(X,X)({0:1, 1:0}).associated_chain_complex_morphism()._matrix_dictionary
            {0: [0 1]
                [1 0],
             1: [-1]}
        """
    def image(self):
        """
        Compute the image simplicial complex of `f`.

        EXAMPLES::

            sage: S = SimplicialComplex([[0,1],[2,3]], is_mutable=False)
            sage: T = SimplicialComplex([[0,1]], is_mutable=False)
            sage: f = {0:0,1:1,2:0,3:1}
            sage: H = Hom(S,T)
            sage: x = H(f)
            sage: x.image()
            Simplicial complex with vertex set (0, 1) and facets {(0, 1)}

            sage: S = SimplicialComplex(is_mutable=False)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: i.image()
            Simplicial complex with vertex set () and facets {()}
            sage: i.is_surjective()
            True
            sage: S = SimplicialComplex([[0,1]], is_mutable=False)
            sage: T = SimplicialComplex([[0,1], [0,2]], is_mutable=False)
            sage: f = {0:0,1:1}
            sage: g = {0:0,1:1}
            sage: k = {0:0,1:2}
            sage: H = Hom(S,T)
            sage: x = H(f)
            sage: y = H(g)
            sage: z = H(k)
            sage: x == y
            True
            sage: x == z
            False
            sage: x.image()
            Simplicial complex with vertex set (0, 1) and facets {(0, 1)}
            sage: y.image()
            Simplicial complex with vertex set (0, 1) and facets {(0, 1)}
            sage: z.image()
            Simplicial complex with vertex set (0, 2) and facets {(0, 2)}
        """
    def is_surjective(self):
        """
        Return ``True`` if and only if ``self`` is surjective.

        EXAMPLES::

            sage: S = SimplicialComplex([(0,1,2)], is_mutable=False)
            sage: S
            Simplicial complex with vertex set (0, 1, 2) and facets {(0, 1, 2)}
            sage: T = SimplicialComplex([(0,1)], is_mutable=False)
            sage: T
            Simplicial complex with vertex set (0, 1) and facets {(0, 1)}
            sage: H = Hom(S,T)
            sage: x = H({0:0,1:1,2:1})
            sage: x.is_surjective()
            True

            sage: S = SimplicialComplex([[0,1],[2,3]], is_mutable=False)
            sage: T = SimplicialComplex([[0,1]], is_mutable=False)
            sage: f = {0:0,1:1,2:0,3:1}
            sage: H = Hom(S,T)
            sage: x = H(f)
            sage: x.is_surjective()
            True
        """
    def is_injective(self):
        """
        Return ``True`` if and only if ``self`` is injective.

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(1)
            sage: T = simplicial_complexes.Sphere(2)
            sage: U = simplicial_complexes.Sphere(3)
            sage: H = Hom(T,S)
            sage: G = Hom(T,U)
            sage: f = {0:0,1:1,2:0,3:1}
            sage: x = H(f)
            sage: g = {0:0,1:1,2:2,3:3}
            sage: y = G(g)
            sage: x.is_injective()
            False
            sage: y.is_injective()
            True
        """
    def is_identity(self) -> bool:
        """
        If ``self`` is an identity morphism, returns ``True``.
        Otherwise, ``False``.

        EXAMPLES::

            sage: T = simplicial_complexes.Sphere(1)
            sage: G = Hom(T,T)
            sage: T
            Minimal triangulation of the 1-sphere
            sage: j = G({0:0,1:1,2:2})
            sage: j.is_identity()
            True

            sage: S = simplicial_complexes.Sphere(2)
            sage: T = simplicial_complexes.Sphere(3)
            sage: H = Hom(S,T)
            sage: f = {0:0,1:1,2:2,3:3}
            sage: x = H(f)
            sage: x
            Simplicial complex morphism:
              From: Minimal triangulation of the 2-sphere
              To:   Minimal triangulation of the 3-sphere
              Defn: 0 |--> 0
                    1 |--> 1
                    2 |--> 2
                    3 |--> 3
            sage: x.is_identity()
            False
        """
    def fiber_product(self, other, rename_vertices: bool = True):
        """
        Fiber product of ``self`` and ``other``.

        Both morphisms should have
        the same codomain. The method returns a morphism of simplicial
        complexes, which is the morphism from the space of the fiber product
        to the codomain.

        EXAMPLES::

            sage: S = SimplicialComplex([[0,1],[1,2]], is_mutable=False)
            sage: T = SimplicialComplex([[0,2],[1]], is_mutable=False)
            sage: U = SimplicialComplex([[0,1],[2]], is_mutable=False)
            sage: H = Hom(S,U)
            sage: G = Hom(T,U)
            sage: f = {0:0,1:1,2:0}
            sage: g = {0:0,1:1,2:1}
            sage: x = H(f)
            sage: y = G(g)
            sage: z = x.fiber_product(y)
            sage: z
            Simplicial complex morphism:
              From: Simplicial complex with 4 vertices and facets {...}
              To:   Simplicial complex with vertex set (0, 1, 2) and facets {(2,), (0, 1)}
              Defn: L0R0 |--> 0
                    L1R1 |--> 1
                    L1R2 |--> 1
                    L2R0 |--> 0
        """
    def mapping_torus(self):
        """
        The mapping torus of a simplicial complex endomorphism.

        The mapping torus is the simplicial complex formed by taking
        the product of the domain of ``self`` with a `4` point
        interval `[I_0, I_1, I_2, I_3]` and identifying vertices of
        the form `(I_0, v)` with `(I_3, w)` where `w` is the image of
        `v` under the given morphism.

        See :wikipedia:`Mapping torus`

        EXAMPLES::

            sage: C = simplicial_complexes.Sphere(1)            # Circle
            sage: T = Hom(C,C).identity().mapping_torus() ; T   # Torus
            Simplicial complex with 9 vertices and 18 facets
            sage: T.homology() == simplicial_complexes.Torus().homology()               # needs sage.modules
            True

            sage: f = Hom(C,C)({0:0, 1:2, 2:1})
            sage: K = f.mapping_torus(); K                      # Klein Bottle
            Simplicial complex with 9 vertices and 18 facets
            sage: K.homology() == simplicial_complexes.KleinBottle().homology()         # needs sage.modules
            True

        TESTS::

            sage: g = Hom(simplicial_complexes.Simplex([1]),C)({1:0})
            sage: g.mapping_torus()
            Traceback (most recent call last):
            ...
            ValueError: self must have the same domain and codomain
        """
    def induced_homology_morphism(self, base_ring=None, cohomology: bool = False):
        """
        Return the map in (co)homology induced by this map.

        INPUT:

        - ``base_ring`` -- must be a field (default: ``QQ``)

        - ``cohomology`` -- boolean (default: ``False``); if
          ``True``, the map induced in cohomology rather than homology

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(1)
            sage: T = S.product(S, is_mutable=False)
            sage: H = Hom(S,T)
            sage: diag = H.diagonal_morphism()
            sage: h = diag.induced_homology_morphism(QQ); h                             # needs sage.modules
            Graded vector space morphism:
              From: Homology module of
                    Minimal triangulation of the 1-sphere over Rational Field
              To:   Homology module of
                    Simplicial complex with 9 vertices and 18 facets over Rational Field
              Defn: induced by:
                Simplicial complex morphism:
                  From: Minimal triangulation of the 1-sphere
                  To:   Simplicial complex with 9 vertices and 18 facets
                  Defn: 0 |--> L0R0
                        1 |--> L1R1
                        2 |--> L2R2

        We can view the matrix form for the homomorphism::

            sage: h.to_matrix(0)  # in degree 0                                         # needs sage.modules
            [1]
            sage: h.to_matrix(1)  # in degree 1                                         # needs sage.modules
            [1]
            [1]
            sage: h.to_matrix()   # the entire homomorphism                             # needs sage.modules
            [1|0]
            [-+-]
            [0|1]
            [0|1]
            [-+-]
            [0|0]

        The map on cohomology should be dual to the map on homology::

            sage: coh = diag.induced_homology_morphism(QQ, cohomology=True)             # needs sage.modules
            sage: coh.to_matrix(1)                                                      # needs sage.modules
            [1 1]
            sage: h.to_matrix() == coh.to_matrix().transpose()                          # needs sage.modules
            True

        We can evaluate the map on (co)homology classes::

            sage: x,y = list(T.cohomology_ring(QQ).basis(1))                            # needs sage.modules
            sage: coh(x)                                                                # needs sage.modules
            h^{1,0}
            sage: coh(2*x + 3*y)                                                        # needs sage.modules
            5*h^{1,0}

        Note that the complexes must be immutable for this to
        work. Many, but not all, complexes are immutable when
        constructed::

            sage: S.is_immutable()
            True
            sage: S.barycentric_subdivision().is_immutable()
            False
            sage: S2 = S.suspension()
            sage: S2.is_immutable()
            False
            sage: h = Hom(S, S2)({0: 0, 1: 1, 2: 2}).induced_homology_morphism()        # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: the domain and codomain complexes must be immutable
            sage: S2.set_immutable(); S2.is_immutable()
            True
            sage: h = Hom(S, S2)({0: 0, 1: 1, 2: 2}).induced_homology_morphism()        # needs sage.modules
        """
    def is_contiguous_to(self, other):
        """
        Return ``True`` if ``self`` is contiguous to ``other``.

        Two morphisms `f_0, f_1: K \\to L` are *contiguous* if for any
        simplex `\\sigma \\in K`, the union `f_0(\\sigma) \\cup
        f_1(\\sigma)` is a simplex in `L`. This is not a transitive
        relation, but it induces an equivalence relation on simplicial
        maps: `f` is equivalent to `g` if there is a finite sequence
        `f_0 = f`, `f_1`, ..., `f_n = g` such that `f_i` and `f_{i+1}`
        are contiguous for each `i`.

        This is related to maps being homotopic: if they are
        contiguous, then they induce homotopic maps on the geometric
        realizations. Given two homotopic maps on the geometric
        realizations, then after barycentrically subdividing `n` times
        for some `n`, the maps have simplicial approximations which
        are in the same contiguity class. (This last fact is only true
        if the domain is a *finite* simplicial complex, by the way.)

        See Section 3.5 of Spanier [Spa1966]_ for details.

        ALGORITHM:

        It is enough to check when `\\sigma` ranges over the facets.

        INPUT:

        - ``other`` -- a simplicial complex morphism with the same
          domain and codomain as ``self``

        EXAMPLES::

            sage: K = simplicial_complexes.Simplex(1)
            sage: L = simplicial_complexes.Sphere(1)
            sage: H = Hom(K, L)
            sage: f = H({0: 0, 1: 1})
            sage: g = H({0: 0, 1: 0})
            sage: f.is_contiguous_to(f)
            True
            sage: f.is_contiguous_to(g)
            True
            sage: h = H({0: 1, 1: 2})
            sage: f.is_contiguous_to(h)
            False

        TESTS::

            sage: one = Hom(K,K).identity()
            sage: one.is_contiguous_to(f)
            False
            sage: one.is_contiguous_to(3) # nonsensical input
            False
        """
