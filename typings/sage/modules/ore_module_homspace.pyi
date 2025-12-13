from sage.categories.homset import HomsetWithBase as HomsetWithBase
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modules.ore_module import OreModule as OreModule
from sage.modules.ore_module_morphism import OreModuleMorphism as OreModuleMorphism
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class OreModule_homspace(UniqueRepresentation, HomsetWithBase):
    """
    Class for hom spaces between Ore modules.
    """
    Element = OreModuleMorphism
    def __init__(self, domain, codomain, category=None) -> None:
        """
        Initialize this homspace.

        INPUT:

        - ``domain`` -- a Ore module

        - ``codomain`` -- a Ore module

        - ``category`` (default: ``None``) -- the category in which
          the morphisms are

        TESTS::

            sage: K.<z> = GF(7^2)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X + z)
            sage: N = S.quotient_module(X^2 + z)
            sage: Hom(M, N)  # indirect doctest
            Set of Morphisms
            from Ore module of rank 1 over Finite Field in z of size 7^2 twisted by z |--> z^7
            to Ore module of rank 2 over Finite Field in z of size 7^2 twisted by z |--> z^7
            in Category of enumerated finite dimensional Ore modules with basis over Finite Field in z of size 7^2 twisted by z |--> z^7
            sage: End(M)     # indirect doctest
            Set of Morphisms
            from Ore module of rank 1 over Finite Field in z of size 7^2 twisted by z |--> z^7
            to Ore module of rank 1 over Finite Field in z of size 7^2 twisted by z |--> z^7
            in Category of enumerated finite dimensional Ore modules with basis over Finite Field in z of size 7^2 twisted by z |--> z^7

        ::

            sage: V = M.module()
            sage: Hom(M, V)
            Traceback (most recent call last):
            ...
            ValueError: codomain must be a Ore module
        """
    def matrix_space(self):
        """
        Return the matrix space used to represent the
        morphisms in this homspace.

        EXAMPLES::

            sage: K.<z> = GF(7^2)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 + z*X + 1)
            sage: End(M).matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Finite Field in z of size 7^2

        ::

            sage: N = S.quotient_module(X^2 + z)
            sage: Hom(M, N).matrix_space()
            Full MatrixSpace of 3 by 2 dense matrices over Finite Field in z of size 7^2
        """
    def identity(self):
        """
        Return the identity morphism in this homspace.

        EXAMPLES::

            sage: K.<z> = GF(7^2)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 + z*X + 1)
            sage: End(M).identity()
            Ore module endomorphism of Ore module of rank 3 over Finite Field in z of size 7^2 twisted by z |--> z^7
        """
    def zero(self):
        """
        Return the zero morphism in this homspace.

        EXAMPLES::

            sage: K.<z> = GF(7^2)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^3 + z*X + 1)
            sage: End(M).zero()
            Ore module endomorphism of Ore module of rank 3 over Finite Field in z of size 7^2 twisted by z |--> z^7
        """
