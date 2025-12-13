from sage.categories.homset import HomsetWithBase as HomsetWithBase
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modules.free_module_pseudomorphism import FreeModulePseudoMorphism as FreeModulePseudoMorphism
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing as OrePolynomialRing
from sage.structure.sequence import Sequence as Sequence
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FreeModulePseudoHomspace(UniqueRepresentation, HomsetWithBase):
    """
    This class implements the space of pseudomorphisms with a fixed twist.

    For free modules, the elements of a pseudomorphism correspond to matrices
    which define the mapping on elements of a basis.

    This class is not supposed to be instantiated directly; the user should
    use instead the method :meth:`sage.rings.module.free_module.FreeModule_generic.pseudoHom`
    to create a space of pseudomorphisms.

    TESTS::

        sage: F = GF(125)
        sage: M = F^2
        sage: Frob = F.frobenius_endomorphism()
        sage: PHS = M.pseudoHom(Frob)
        sage: h = PHS([[1, 2], [1, 1]])
        sage: e = M((4*F.gen()^2 + F.gen() + 2, 4*F.gen()^2 + 4*F.gen() + 4))
        sage: h(e)
        (z3, 2*z3^2 + 3*z3 + 3)
    """
    Element = FreeModulePseudoMorphism
    @staticmethod
    def __classcall_private__(cls, domain, codomain, twist):
        """
        Constructs the space of pseudomorphisms with a given twist.

        INPUT:

        - ``domain`` -- a free module,  the domain of this pseudomorphism

        - ``codomain`` -- a free module, the codomain of this pseudomorphism

        - ``twist`` -- a twisting morphism/derivation or the corresponding
          Ore polynomial ring

        TESTS::

            sage: F = GF(125)
            sage: Frob = F.frobenius_endomorphism()
            sage: M = F^2
            sage: H = M.pseudoHom(Frob)
            sage: type(H)
            <class 'sage.modules.free_module_pseudohomspace.FreeModulePseudoHomspace_with_category'>

            sage: TestSuite(H).run()
        """
    def __init__(self, domain, codomain, ore) -> None:
        """
        Initialize this pseudohom space.

        INPUT:

        - ``domain`` -- a free module,  the domain of this pseudomorphism

        - ``codomain`` -- a free module, the codomain of this pseudomorphism

        - ``ore`` -- the underlying Ore polynomial ring (built from the
          twisting morphism and derivation)

        TESTS::

            sage: F = GF(125)
            sage: Frob = F.frobenius_endomorphism()
            sage: M = F^2
            sage: M.pseudoHom(Frob)
            Set of Pseudoendomorphisms (twisted by z3 |--> z3^5) of
            Vector space of dimension 2 over Finite Field in z3 of size 5^3
        """
    def __reduce__(self):
        """
        TESTS::

            sage: F = GF(125)
            sage: Frob = F.frobenius_endomorphism()
            sage: M = F^2
            sage: H = M.pseudoHom(Frob)
            sage: loads(dumps(M)) is M
            True
        """
    def ore_ring(self, var: str = 'x'):
        """
        Return the underlying Ore polynomial ring, that is
        the Ore polynomial ring over the base field twisted
        by the twisting morphism and the twisting derivation
        attached to this homspace.

        INPUT:

        - ``var`` -- string (default: ``x``) the name of
          the variable

        EXAMPLES::

            sage: Fq.<z> = GF(7^3)
            sage: Frob = Fq.frobenius_endomorphism()
            sage: V = Fq^2
            sage: H = V.pseudoHom(Frob)

            sage: H.ore_ring()
            Ore Polynomial Ring in x over Finite Field in z of size 7^3 twisted by z |--> z^7

            sage: H.ore_ring('y')
            Ore Polynomial Ring in y over Finite Field in z of size 7^3 twisted by z |--> z^7
        """
    def matrix_space(self):
        """
        Return the matrix space used for representing the
        pseudomorphisms in this space.

        EXAMPLES::

            sage: Fq.<z> = GF(7^3)
            sage: Frob = Fq.frobenius_endomorphism()
            sage: V = Fq^2
            sage: W = Fq^3
            sage: H = V.pseudoHom(Frob, codomain=W)
            sage: H.matrix_space()
            Full MatrixSpace of 2 by 3 dense matrices over Finite Field in z of size 7^3
        """
    def basis(self, side: str = 'left'):
        """
        Return a basis for the underlying matrix space.

        The result does not depend on the `side` of the homspace, i.e.
        if matrices are acted upon on the left or on the right.

        EXAMPLES::

            sage: Fq = GF(7^3)
            sage: Frob = Fq.frobenius_endomorphism()
            sage: V = Fq^2
            sage: PHS = V.pseudoHom(Frob)
            sage: PHS.basis()
            [Free module pseudomorphism (twisted by z3 |--> z3^7) defined by the matrix
            [1 0]
            [0 0]
            Domain: Vector space of dimension 2 over Finite Field in z3 of size 7^3
            Codomain: Vector space of dimension 2 over Finite Field in z3 of size 7^3,
            Free module pseudomorphism (twisted by z3 |--> z3^7) defined by the matrix
            [0 1]
            [0 0]
            Domain: Vector space of dimension 2 over Finite Field in z3 of size 7^3
            Codomain: Vector space of dimension 2 over Finite Field in z3 of size 7^3,
            Free module pseudomorphism (twisted by z3 |--> z3^7) defined by the matrix
            [0 0]
            [1 0]
            Domain: Vector space of dimension 2 over Finite Field in z3 of size 7^3
            Codomain: Vector space of dimension 2 over Finite Field in z3 of size 7^3,
            Free module pseudomorphism (twisted by z3 |--> z3^7) defined by the matrix
            [0 0]
            [0 1]
            Domain: Vector space of dimension 2 over Finite Field in z3 of size 7^3
            Codomain: Vector space of dimension 2 over Finite Field in z3 of size 7^3]
        """
