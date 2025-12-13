import sage.categories.homset
from .simplicial_complex_morphism import SimplicialComplexMorphism as SimplicialComplexMorphism

def is_SimplicialComplexHomset(x) -> bool:
    """
    Return ``True`` if and only if ``x`` is a simplicial complex homspace.

    EXAMPLES::

        sage: S = SimplicialComplex(is_mutable=False)
        sage: T = SimplicialComplex(is_mutable=False)
        sage: H = Hom(S, T)
        sage: H
        Set of Morphisms from Simplicial complex with vertex set () and facets {()}
         to Simplicial complex with vertex set () and facets {()}
         in Category of finite simplicial complexes
        sage: from sage.topology.simplicial_complex_homset import is_SimplicialComplexHomset
        sage: is_SimplicialComplexHomset(H)
        doctest:warning...
        DeprecationWarning: the function is_SimplicialComplexHomset is deprecated;
        use 'isinstance(..., SimplicialComplexHomset)' instead
        See https://github.com/sagemath/sage/issues/37922 for details.
        True
    """

class SimplicialComplexHomset(sage.categories.homset.Homset):
    def __call__(self, f):
        """
        INPUT:

        - ``f`` -- dictionary with keys exactly the vertices of the domain
          and values vertices of the codomain

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(3)
            sage: T = simplicial_complexes.Sphere(2)
            sage: f = {0:0,1:1,2:2,3:2,4:2}
            sage: H = Hom(S,T)
            sage: x = H(f)
            sage: x
            Simplicial complex morphism:
              From: Minimal triangulation of the 3-sphere
              To: Minimal triangulation of the 2-sphere
              Defn: [0, 1, 2, 3, 4] --> [0, 1, 2, 2, 2]
        """
    def diagonal_morphism(self, rename_vertices: bool = True):
        """
        Return the diagonal morphism in `Hom(S, S \\times S)`.

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S.product(S, is_mutable=False))
            sage: d = H.diagonal_morphism(); d
            Simplicial complex morphism:
              From: Minimal triangulation of the 2-sphere
              To:   Simplicial complex with 16 vertices and 96 facets
              Defn: 0 |--> L0R0
                    1 |--> L1R1
                    2 |--> L2R2
                    3 |--> L3R3

            sage: T = SimplicialComplex([[0], [1]], is_mutable=False)
            sage: U = T.product(T, rename_vertices=False, is_mutable=False)
            sage: G = Hom(T, U)
            sage: e = G.diagonal_morphism(rename_vertices=False); e
            Simplicial complex morphism:
              From: Simplicial complex with vertex set (0, 1) and facets {(0,), (1,)}
              To:   Simplicial complex with 4 vertices and
                    facets {((0, 0),), ((0, 1),), ((1, 0),), ((1, 1),)}
              Defn: 0 |--> (0, 0)
                    1 |--> (1, 1)
        """
    def identity(self):
        """
        Return the identity morphism of `Hom(S,S)`.

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S, S)
            sage: i = H.identity()
            sage: i.is_identity()
            True

            sage: T = SimplicialComplex([[0,1]], is_mutable=False)
            sage: G = Hom(T, T)
            sage: G.identity()
            Simplicial complex endomorphism of
             Simplicial complex with vertex set (0, 1) and facets {(0, 1)}
              Defn: 0 |--> 0
                    1 |--> 1
        """
    def an_element(self):
        """
        Return a (non-random) element of ``self``.

        EXAMPLES::

            sage: S = simplicial_complexes.KleinBottle()
            sage: T = simplicial_complexes.Sphere(5)
            sage: H = Hom(S,T)
            sage: x = H.an_element()
            sage: x
            Simplicial complex morphism:
              From: Minimal triangulation of the Klein bottle
              To:   Minimal triangulation of the 5-sphere
              Defn: [0, 1, 2, 3, 4, 5, 6, 7] --> [0, 0, 0, 0, 0, 0, 0, 0]
        """
