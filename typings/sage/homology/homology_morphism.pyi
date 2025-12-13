from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.categories.graded_modules_with_basis import GradedModulesWithBasis as GradedModulesWithBasis
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.rings.rational_field import QQ as QQ
from sage.topology.simplicial_complex import SimplicialComplex as SimplicialComplex

class InducedHomologyMorphism(Morphism):
    """
    An element of this class is a morphism of (co)homology groups
    induced by a map of simplicial complexes. It requires working
    with field coefficients.

    INPUT:

    - ``map`` -- the map of simplicial complexes
    - ``base_ring`` -- a field (default: ``QQ``)
    - ``cohomology`` -- boolean (default: ``False``); if
      ``True``, return the induced map in cohomology rather than
      homology

    .. NOTE::

        This is not intended to be used directly by the user, but instead
        via the method
        :meth:`~sage.topology.simplicial_complex_morphism.SimplicialComplexMorphism.induced_homology_morphism`.

    EXAMPLES::

        sage: S1 = simplicial_complexes.Sphere(1)
        sage: H = Hom(S1, S1)
        sage: f = H({0:0, 1:2, 2:1})  # f switches two vertices
        sage: f_star = f.induced_homology_morphism(QQ, cohomology=True)
        sage: f_star
        Graded algebra endomorphism of
         Cohomology ring of Minimal triangulation of the 1-sphere over Rational Field
          Defn: induced by:
                Simplicial complex endomorphism of Minimal triangulation of the 1-sphere
                  Defn: 0 |--> 0
                        1 |--> 2
                        2 |--> 1
        sage: f_star.to_matrix(1)
        [-1]
        sage: f_star.to_matrix()
        [ 1| 0]
        [--+--]
        [ 0|-1]

        sage: T = simplicial_complexes.Torus()
        sage: y = T.homology_with_basis(QQ).basis()[(1,1)]
        sage: y.to_cycle()
        (0, 5) - (0, 6) + (5, 6)

    Since `(0,2) - (0,5) + (2,5)` is a cycle representing a homology
    class in the torus, we can define a map `S^1 \\to T` inducing an
    inclusion on `H_1`::

        sage: Hom(S1, T)({0:0, 1:2, 2:5})
        Simplicial complex morphism:
          From: Minimal triangulation of the 1-sphere
          To:   Minimal triangulation of the torus
          Defn: 0 |--> 0
                1 |--> 2
                2 |--> 5
        sage: g = Hom(S1, T)({0:0, 1:2, 2: 5})
        sage: g_star = g.induced_homology_morphism(QQ)
        sage: g_star.to_matrix(0)
        [1]
        sage: g_star.to_matrix(1)
        [-1]
        [ 0]
        sage: g_star.to_matrix()
        [ 1| 0]
        [--+--]
        [ 0|-1]
        [ 0| 0]
        [--+--]
        [ 0| 0]

    We can evaluate such a map on (co)homology classes::

        sage: H = S1.homology_with_basis(QQ)
        sage: a = H.basis()[(1,0)]
        sage: g_star(a)
        -h_{1,0}

        sage: T = S1.product(S1, is_mutable=False)
        sage: diag = Hom(S1,T).diagonal_morphism()
        sage: b,c = list(T.cohomology_ring().basis(1))
        sage: diag_c = diag.induced_homology_morphism(cohomology=True)
        sage: diag_c(b)
        h^{1,0}
        sage: diag_c(c)
        h^{1,0}
    """
    def __init__(self, map, base_ring=None, cohomology: bool = False) -> None:
        """
        INPUT:

        - ``map`` -- the map of simplicial complexes
        - ``base_ring`` -- a field (default: ``QQ``)
        - ``cohomology`` -- boolean (default: ``False``); if
          ``True``, return the induced map in cohomology rather than
          homology

        EXAMPLES::

            sage: from sage.homology.homology_morphism import InducedHomologyMorphism
            sage: K = simplicial_complexes.RandomComplex(8, 3)
            sage: H = Hom(K,K)
            sage: id = H.identity()
            sage: f = InducedHomologyMorphism(id, QQ)
            sage: f.to_matrix(0) == 1  and  f.to_matrix(1) == 1  and  f.to_matrix(2) == 1
            True
            sage: f = InducedHomologyMorphism(id, ZZ)
            Traceback (most recent call last):
            ...
            ValueError: the coefficient ring must be a field
            sage: S1 = simplicial_complexes.Sphere(1).barycentric_subdivision()
            sage: S1.is_mutable()
            True
            sage: g = Hom(S1, S1).identity()
            sage: h = g.induced_homology_morphism(QQ)
            Traceback (most recent call last):
            ...
            ValueError: the domain and codomain complexes must be immutable
            sage: S1.set_immutable()
            sage: g = Hom(S1, S1).identity()
            sage: h = g.induced_homology_morphism(QQ)
        """
    def base_ring(self):
        """
        The base ring for this map.

        EXAMPLES::

            sage: K = simplicial_complexes.Simplex(2)
            sage: H = Hom(K,K)
            sage: id = H.identity()
            sage: id.induced_homology_morphism(QQ).base_ring()
            Rational Field
            sage: id.induced_homology_morphism(GF(13)).base_ring()
            Finite Field of size 13
        """
    def to_matrix(self, deg=None):
        """
        The matrix for this map.

        If degree ``deg`` is specified, return the matrix just in that
        degree; otherwise, return the block matrix representing the
        entire map.

        INPUT:

        - ``deg`` -- (default: ``None``) the degree

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: S1_b = S1.barycentric_subdivision()
            sage: S1_b.set_immutable()
            sage: d = {(0,): 0, (0,1): 1, (1,): 2, (1,2): 0, (2,): 1, (0,2): 2}
            sage: f = Hom(S1_b, S1)(d)
            sage: h = f.induced_homology_morphism(QQ)
            sage: h.to_matrix(1)
            [2]
            sage: h.to_matrix()
            [1|0]
            [-+-]
            [0|2]
        """
    def __call__(self, elt):
        """
        Evaluate this map on ``elt``, an element of (co)homology.

        INPUT:

        - ``elt`` -- informally, an element of the domain of this
          map. More formally, an element of
          :class:`homology_vector_space_with_basis.HomologyVectorSpaceWithBasis`.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: f = {0:0, 1:2, 2:1}
            sage: H = Hom(S1,S1)
            sage: g = H(f)
            sage: h = g.induced_homology_morphism(QQ)
            sage: x = S1.homology_with_basis().basis()[(1,0)]
            sage: x
            h_{1,0}
            sage: h(x)  # indirect doctest
            -h_{1,0}
        """
    def __eq__(self, other) -> bool:
        """
        Return ``True`` if and only if this map agrees with ``other``.

        INPUT:

        - ``other`` -- another induced homology morphism

        This automatically returns ``False`` if the morphisms have
        different domains, codomains, base rings, or values for their
        cohomology flags

        Otherwise, determine this by computing the matrices for this
        map and ``other`` using the (same) basis for the homology
        vector spaces.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: K = simplicial_complexes.Simplex(2)
            sage: f = Hom(S1, K)({0: 0, 1:1, 2:2})
            sage: g = Hom(S1, K)({0: 0, 1:0, 2:0})
            sage: f.induced_homology_morphism(QQ) == g.induced_homology_morphism(QQ)
            True
            sage: f.induced_homology_morphism(QQ) == g.induced_homology_morphism(GF(2))
            False
            sage: id = Hom(K, K).identity()   # different domain
            sage: f.induced_homology_morphism(QQ) == id.induced_homology_morphism(QQ)
            False
        """
    def is_identity(self) -> bool:
        """
        Return ``True`` if this is the identity map on (co)homology.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: H = Hom(S1, S1)
            sage: flip = H({0:0, 1:2, 2:1})
            sage: flip.induced_homology_morphism(QQ).is_identity()
            False
            sage: flip.induced_homology_morphism(GF(2)).is_identity()
            True
            sage: rotate = H({0:1, 1:2, 2:0})
            sage: rotate.induced_homology_morphism(QQ).is_identity()
            True
        """
    def is_surjective(self) -> bool:
        """
        Return ``True`` if this map is surjective on (co)homology.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: K = simplicial_complexes.Simplex(2)
            sage: H = Hom(S1, K)
            sage: f = H({0:0, 1:1, 2:2})
            sage: f.induced_homology_morphism().is_surjective()
            True
            sage: f.induced_homology_morphism(cohomology=True).is_surjective()
            False
        """
    def is_injective(self) -> bool:
        """
        Return ``True`` if this map is injective on (co)homology.

        EXAMPLES::

            sage: S1 = simplicial_complexes.Sphere(1)
            sage: K = simplicial_complexes.Simplex(2)
            sage: H = Hom(S1, K)
            sage: f = H({0:0, 1:1, 2:2})
            sage: f.induced_homology_morphism().is_injective()
            False
            sage: f.induced_homology_morphism(cohomology=True).is_injective()
            True

            sage: T = simplicial_complexes.Torus()
            sage: g = Hom(S1, T)({0:0, 1:3, 2: 6})
            sage: g_star = g.induced_homology_morphism(QQ)
            sage: g.is_injective()
            True
        """
