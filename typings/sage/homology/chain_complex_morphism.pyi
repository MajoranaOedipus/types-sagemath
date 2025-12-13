from sage.categories.chain_complexes import ChainComplexes as ChainComplexes
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism
from sage.matrix.constructor import block_diagonal_matrix as block_diagonal_matrix, zero_matrix as zero_matrix

def is_ChainComplexMorphism(x):
    """
    Return ``True`` if and only if ``x`` is a chain complex morphism.

    EXAMPLES::

        sage: # needs sage.graphs
        sage: from sage.homology.chain_complex_morphism import is_ChainComplexMorphism
        sage: S = simplicial_complexes.Sphere(14)
        sage: H = Hom(S,S)
        sage: i = H.identity()                  # long time (8s on sage.math, 2011)
        sage: S = simplicial_complexes.Sphere(6)
        sage: H = Hom(S,S)
        sage: i = H.identity()
        sage: x = i.associated_chain_complex_morphism()
        sage: x # indirect doctest
        Chain complex morphism:
          From: Chain complex with at most 7 nonzero terms over Integer Ring
          To: Chain complex with at most 7 nonzero terms over Integer Ring
        sage: is_ChainComplexMorphism(x)
        doctest:warning...
        DeprecationWarning: The function is_ChainComplexMorphism is deprecated;
        use 'isinstance(..., ChainComplexMorphism)' instead.
        See https://github.com/sagemath/sage/issues/38103 for details.
        True
    """

class ChainComplexMorphism(Morphism):
    """
    An element of this class is a morphism of chain complexes.
    """
    def __init__(self, matrices, C, D, check: bool = True) -> None:
        """
        Create a morphism from a dictionary of matrices.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = simplicial_complexes.Sphere(1); S
            Minimal triangulation of the 1-sphere
            sage: C = S.chain_complex()
            sage: C.differential()
            {0: [],
             1: [-1 -1  0]
                [ 1  0 -1]
                [ 0  1  1],
             2: []}
            sage: f = {0:zero_matrix(ZZ,3,3),1:zero_matrix(ZZ,3,3)}
            sage: G = Hom(C,C)
            sage: x = G(f); x
            Chain complex endomorphism of
             Chain complex with at most 2 nonzero terms over Integer Ring
            sage: x._matrix_dictionary
            {0: [0 0 0]
                [0 0 0]
                [0 0 0],
             1: [0 0 0]
                [0 0 0]
                [0 0 0]}

        Check that the bug in :issue:`13220` has been fixed::

            sage: # needs sage.graphs
            sage: X = simplicial_complexes.Simplex(1)
            sage: Y = simplicial_complexes.Simplex(0)
            sage: g = Hom(X,Y)({0: 0, 1: 0})
            sage: g.associated_chain_complex_morphism()
            Chain complex morphism:
              From: Chain complex with at most 2 nonzero terms over Integer Ring
              To: Chain complex with at most 1 nonzero terms over Integer Ring

        Check that an error is raised if the matrices are the wrong size::

            sage: C = ChainComplex({0: zero_matrix(ZZ, 0, 1)})
            sage: D = ChainComplex({0: zero_matrix(ZZ, 0, 2)})
            sage: Hom(C,D)({0: matrix(1, 2, [1, 1])})  # 1x2 is the wrong size.
            Traceback (most recent call last):
            ...
            ValueError: matrix in degree 0 is not the right size
            sage: Hom(C,D)({0: matrix(2, 1, [1, 1])})  # 2x1 is right.
            Chain complex morphism:
              From: Chain complex with at most 1 nonzero terms over Integer Ring
              To: Chain complex with at most 1 nonzero terms over Integer Ring
        """
    def in_degree(self, n):
        """
        The matrix representing this morphism in degree `n`.

        INPUT:

        - ``n`` -- degree

        EXAMPLES::

            sage: C = ChainComplex({0: identity_matrix(ZZ, 1)})
            sage: D = ChainComplex({0: zero_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
            sage: f = Hom(C,D)({0: identity_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
            sage: f.in_degree(0)
            [1]

        Note that if the matrix is not specified in the definition of
        the map, it is assumed to be zero::

            sage: f.in_degree(2)
            []
            sage: f.in_degree(2).nrows(), f.in_degree(2).ncols()
            (1, 0)
            sage: C.free_module(2)
            Ambient free module of rank 0 over the principal ideal domain Integer Ring
            sage: D.free_module(2)
            Ambient free module of rank 1 over the principal ideal domain Integer Ring
        """
    def to_matrix(self, deg=None):
        """
        The matrix representing this chain map.

        If the degree ``deg`` is specified, return the matrix in that
        degree; otherwise, return the (block) matrix for the whole
        chain map.

        INPUT:

        - ``deg`` -- (default: ``None``) the degree

        EXAMPLES::

            sage: C = ChainComplex({0: identity_matrix(ZZ, 1)})
            sage: D = ChainComplex({0: zero_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
            sage: f = Hom(C,D)({0: identity_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
            sage: f.to_matrix(0)
            [1]
            sage: f.to_matrix()
            [1|0|]
            [-+-+]
            [0|0|]
            [-+-+]
            [0|0|]
        """
    def dual(self):
        """
        The dual chain map to this one.

        That is, the map from the dual of the codomain of this one to
        the dual of its domain, represented in each degree by the
        transpose of the corresponding matrix.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: X = simplicial_complexes.Simplex(1)
            sage: Y = simplicial_complexes.Simplex(0)
            sage: g = Hom(X,Y)({0:0, 1:0})
            sage: f = g.associated_chain_complex_morphism()
            sage: f.in_degree(0)
            [1 1]
            sage: f.dual()
            Chain complex morphism:
              From: Chain complex with at most 1 nonzero terms over Integer Ring
                To: Chain complex with at most 2 nonzero terms over Integer Ring
            sage: f.dual().in_degree(0)
            [1]
            [1]
            sage: ascii_art(f.domain())
                        [-1]
                        [ 1]
             0 <-- C_0 <----- C_1 <-- 0
            sage: ascii_art(f.dual().codomain())
                        [-1  1]
             0 <-- C_1 <-------- C_0 <-- 0
        """
    def __neg__(self):
        """
        Return ``-x``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism()
            sage: w = -x
            sage: w._matrix_dictionary
            {0: [-1  0  0  0]
                [ 0 -1  0  0]
                [ 0  0 -1  0]
                [ 0  0  0 -1],
             1: [-1  0  0  0  0  0]
                [ 0 -1  0  0  0  0]
                [ 0  0 -1  0  0  0]
                [ 0  0  0 -1  0  0]
                [ 0  0  0  0 -1  0]
                [ 0  0  0  0  0 -1],
             2: [-1  0  0  0]
                [ 0 -1  0  0]
                [ 0  0 -1  0]
                [ 0  0  0 -1]}
        """
    def __add__(self, x):
        """
        Return ``self + x``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism()
            sage: z = x+x
            sage: z._matrix_dictionary
            {0: [2 0 0 0]
                [0 2 0 0]
                [0 0 2 0]
                [0 0 0 2],
             1: [2 0 0 0 0 0]
                [0 2 0 0 0 0]
                [0 0 2 0 0 0]
                [0 0 0 2 0 0]
                [0 0 0 0 2 0]
                [0 0 0 0 0 2],
             2: [2 0 0 0]
                [0 2 0 0]
                [0 0 2 0]
                [0 0 0 2]}
        """
    def __mul__(self, x):
        """
        Return ``self * x`` if ``self`` and ``x`` are composable morphisms
        or if ``x`` is an element of the base ring.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism()
            sage: y = x*2
            sage: y._matrix_dictionary
            {0: [2 0 0 0]
                [0 2 0 0]
                [0 0 2 0]
                [0 0 0 2],
             1: [2 0 0 0 0 0]
                [0 2 0 0 0 0]
                [0 0 2 0 0 0]
                [0 0 0 2 0 0]
                [0 0 0 0 2 0]
                [0 0 0 0 0 2],
             2: [2 0 0 0]
                [0 2 0 0]
                [0 0 2 0]
                [0 0 0 2]}
            sage: z = y*y
            sage: z._matrix_dictionary
            {0: [4 0 0 0]
                [0 4 0 0]
                [0 0 4 0]
                [0 0 0 4],
             1: [4 0 0 0 0 0]
                [0 4 0 0 0 0]
                [0 0 4 0 0 0]
                [0 0 0 4 0 0]
                [0 0 0 0 4 0]
                [0 0 0 0 0 4],
             2: [4 0 0 0]
                [0 4 0 0]
                [0 0 4 0]
                [0 0 0 4]}

        TESTS:

        Make sure that the product is taken in the correct order
        (``self * x``, not ``x * self`` -- see :issue:`19065`)::

            sage: C = ChainComplex({0: zero_matrix(ZZ, 0, 2)})
            sage: D = ChainComplex({0: zero_matrix(ZZ, 0, 1)})
            sage: f = Hom(C,D)({0: matrix(1, 2, [1, 1])})
            sage: g = Hom(D,C)({0: matrix(2, 1, [1, 1])})
            sage: (f*g).in_degree(0)
            [2]

        Before :issue:`19065`, the following multiplication produced a
        :exc:`KeyError` because `f` was not explicitly defined in degree 2::

            sage: C0 = ChainComplex({0: zero_matrix(ZZ, 0, 1)})
            sage: C1 = ChainComplex({1: zero_matrix(ZZ, 0, 1)})
            sage: C2 = ChainComplex({2: zero_matrix(ZZ, 0, 1)})
            sage: f = ChainComplexMorphism({}, C0, C1)
            sage: g = ChainComplexMorphism({}, C1, C2)
            sage: g * f
            Chain complex morphism:
              From: Chain complex with at most 1 nonzero terms over Integer Ring
              To: Chain complex with at most 1 nonzero terms over Integer Ring
            sage: f._matrix_dictionary
            {0: [], 1: []}
            sage: g._matrix_dictionary
            {1: [], 2: []}
        """
    def __rmul__(self, x):
        """
        Return ``x * self`` if ``x`` is an element of the base ring.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism()
            sage: 2*x == x*2
            True
            sage: 3*x == x*2
            False
        """
    def __sub__(self, x):
        """
        Return ``self - x``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = simplicial_complexes.Sphere(2)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism()
            sage: y = x - x
            sage: y._matrix_dictionary
            {0: [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0],
             1: [0 0 0 0 0 0]
            [0 0 0 0 0 0]
            [0 0 0 0 0 0]
            [0 0 0 0 0 0]
            [0 0 0 0 0 0]
            [0 0 0 0 0 0],
             2: [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]}
        """
    def __eq__(self, x):
        """
        Return ``True`` if and only if ``self == x``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = SimplicialComplex(is_mutable=False)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism(); x
            Chain complex morphism:
              From: Trivial chain complex over Integer Ring
              To: Trivial chain complex over Integer Ring
            sage: f = x._matrix_dictionary
            sage: C = S.chain_complex()
            sage: G = Hom(C,C)
            sage: y = G(f)
            sage: x == y
            True
        """
    def is_identity(self) -> bool:
        """
        Return ``True`` if this is the identity map.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S = SimplicialComplex(is_mutable=False)
            sage: H = Hom(S,S)
            sage: i = H.identity()
            sage: x = i.associated_chain_complex_morphism()
            sage: x.is_identity()
            True
        """
    def is_surjective(self) -> bool:
        """
        Return ``True`` if this map is surjective.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S1 = simplicial_complexes.Sphere(1)
            sage: H = Hom(S1, S1)
            sage: flip = H({0:0, 1:2, 2:1})
            sage: flip.associated_chain_complex_morphism().is_surjective()
            True

            sage: # needs sage.graphs
            sage: pt = simplicial_complexes.Simplex(0)
            sage: inclusion = Hom(pt, S1)({0:2})
            sage: inclusion.associated_chain_complex_morphism().is_surjective()
            False
            sage: inclusion.associated_chain_complex_morphism(cochain=True).is_surjective()
            True
        """
    def is_injective(self):
        """
        Return ``True`` if this map is injective.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: S1 = simplicial_complexes.Sphere(1)
            sage: H = Hom(S1, S1)
            sage: flip = H({0:0, 1:2, 2:1})
            sage: flip.associated_chain_complex_morphism().is_injective()
            True

            sage: # needs sage.graphs
            sage: pt = simplicial_complexes.Simplex(0)
            sage: inclusion = Hom(pt, S1)({0:2})
            sage: inclusion.associated_chain_complex_morphism().is_injective()
            True
            sage: inclusion.associated_chain_complex_morphism(cochain=True).is_injective()
            False
        """
    def __hash__(self):
        """
        TESTS::

            sage: C = ChainComplex({0: identity_matrix(ZZ, 1)})
            sage: D = ChainComplex({0: zero_matrix(ZZ, 1)})
            sage: f = Hom(C,D)({0: identity_matrix(ZZ, 1), 1: zero_matrix(ZZ, 1)})
            sage: hash(f)  # random
            17
        """
