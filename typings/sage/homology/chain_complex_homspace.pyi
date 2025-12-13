import sage.categories.homset
from sage.homology.chain_complex_morphism import ChainComplexMorphism as ChainComplexMorphism

def is_ChainComplexHomspace(x):
    """
    Return ``True`` if and only if ``x`` is a morphism of chain complexes.

    EXAMPLES::

        sage: from sage.homology.chain_complex_homspace import is_ChainComplexHomspace
        sage: T = SimplicialComplex([[1,2,3,4],[7,8,9]])
        sage: C = T.chain_complex(augmented=True, cochain=True)
        sage: G = Hom(C, C)
        sage: is_ChainComplexHomspace(G)
        doctest:warning...
        DeprecationWarning: The function is_ChainComplexHomspace is deprecated;
        use 'isinstance(..., ChainComplexHomspace)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        True
    """

class ChainComplexHomspace(sage.categories.homset.Homset):
    """
    Class of homspaces of chain complex morphisms.

    EXAMPLES::

        sage: T = SimplicialComplex([[1,2,3,4],[7,8,9]])
        sage: C = T.chain_complex(augmented=True, cochain=True)
        sage: G = Hom(C, C)
        sage: G
        Set of Morphisms
         from Chain complex with at most 5 nonzero terms over Integer Ring
           to Chain complex with at most 5 nonzero terms over Integer Ring
           in Category of chain complexes over Integer Ring
    """
    def __call__(self, f):
        """
        `f` is a dictionary of matrices in the basis of the chain complex.

        EXAMPLES::

            sage: S = simplicial_complexes.Sphere(5)
            sage: H = Hom(S, S)
            sage: i = H.identity()
            sage: C = S.chain_complex()
            sage: G = Hom(C, C)
            sage: x = i.associated_chain_complex_morphism()
            sage: f = x._matrix_dictionary
            sage: y = G(f)
            sage: x == y
            True
        """
