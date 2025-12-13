from sage.categories.map import Map as Map
from sage.categories.morphism import Morphism as Morphism
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix0 import Matrix as Matrix
from sage.misc.latex import latex as latex
from sage.modules.ore_module import OreQuotientModule as OreQuotientModule, OreSubmodule as OreSubmodule
from sage.structure.element import Element as Element

class OreModuleMorphism(Morphism):
    """
    Generic class for morphism between Ore modules.
    """
    def __init__(self, parent, im_gens, check: bool = True) -> None:
        """
        Initialize this Ore module.

        INPUT:

        - ``parent`` -- the hom space

        - ``im_gens`` -- the image of the generators (formatted as
          a list, a tuple, a dictionary or a matrix) or a Ore modules
          morphism

        - ``check`` (default: ``True``) -- a boolean, whether we
          should check if the given data correctly defined a morphism
          of Ore modules

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: f = M.multiplication_map(X^3)
            sage: type(f)
            <class 'sage.modules.ore_module_homspace.OreModule_homspace_with_category.element_class'>

            sage: TestSuite(f).run()
        """
    def matrix(self):
        """
        Return the matrix defining this morphism.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: f = M.multiplication_map(2)
            sage: f.matrix()
            [2 0]
            [0 2]

            sage: g = M.multiplication_map(X^3)
            sage: g.matrix()
            [            0 3*z^2 + z + 1]
            [      2*z + 1             0]
        """
    def is_zero(self) -> bool:
        """
        Return ``True`` if this morphism is zero.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2 + 1
            sage: M = S.quotient_module(P^2, names='e')
            sage: M.inject_variables()
            Defining e0, e1, e2, e3, e4, e5

            sage: f = M.hom({e0: P*e0})
            sage: f.is_zero()
            False
            sage: (f*f).is_zero()
            True
        """
    def is_identity(self) -> bool:
        """
        Return ``True`` if this morphism is the identity.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<v,w> = S.quotient_module(X^2 + z)
            sage: f = M.hom({v: v})
            sage: f.is_identity()
            True

            sage: f = M.hom({v: 2*v})
            sage: f.is_identity()
            False
        """
    def __eq__(self, other):
        """
        Return ``True`` if this morphism is equal to ``other``.

        TESTS::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: f = 2*M.multiplication_map(X^3)
            sage: g = M.multiplication_map(2*X^3)
            sage: f == g
            True
        """
    def is_injective(self) -> bool:
        """
        Return ``True`` if this morphism is injective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2
            sage: M = S.quotient_module(P^2, names='m')
            sage: M.inject_variables()
            Defining m0, m1, m2, m3, m4, m5
            sage: N = S.quotient_module(P, names='n')
            sage: N.inject_variables()
            Defining n0, n1, n2

            sage: f = N.hom({n0: P*m0})
            sage: f.is_injective()
            True

            sage: g = M.hom({m0: n0})
            sage: g.is_injective()
            False
        """
    def is_surjective(self) -> bool:
        """
        Return ``True`` if this morphism is surjective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2
            sage: M = S.quotient_module(P^2, names='m')
            sage: M.inject_variables()
            Defining m0, m1, m2, m3, m4, m5
            sage: N = S.quotient_module(P, names='n')
            sage: N.inject_variables()
            Defining n0, n1, n2

            sage: f = N.hom({n0: P*m0})
            sage: f.is_surjective()
            False

            sage: g = M.hom({m0: n0})
            sage: g.is_surjective()
            True
        """
    def is_bijective(self) -> bool:
        """
        Return ``True`` if this morphism is bijective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: f = M.multiplication_map(X^3)
            sage: f.is_bijective()
            True

            sage: N = S.quotient_module(X^2)
            sage: g = N.multiplication_map(X^3)
            sage: g.is_bijective()
            False
        """
    def is_isomorphism(self) -> bool:
        """
        Return ``True`` if this morphism is an isomorphism.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M = S.quotient_module(X^2 + z)
            sage: f = M.multiplication_map(X^3)
            sage: f.is_isomorphism()
            True

            sage: N = S.quotient_module(X^2)
            sage: g = N.multiplication_map(X^3)
            sage: g.is_isomorphism()
            False
        """
    def inverse(self):
        """
        Return the inverse of this morphism.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^2 + z
            sage: M.<e0,e1,e2,e3> = S.quotient_module(P^2)

            sage: f = M.multiplication_map(X^3)
            sage: g = f.inverse()
            sage: (f*g).is_identity()
            True
            sage: (g*f).is_identity()
            True

        If the morphism is not invertible, an error is raised::

            sage: h = M.hom({e0: P*e0})
            sage: h.inverse()
            Traceback (most recent call last):
            ...
            ValueError: this morphism is not invertible
        """
    __invert__ = inverse
    def kernel(self, names=None):
        """
        Return ``True`` if this morphism is injective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2
            sage: M = S.quotient_module(P^2, names='m')
            sage: M.inject_variables()
            Defining m0, m1, m2, m3, m4, m5
            sage: N = S.quotient_module(P, names='n')
            sage: N.inject_variables()
            Defining n0, n1, n2

            sage: f = M.hom({m0: n0})
            sage: ker = f.kernel()
            sage: ker
            Ore module of rank 3 over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: ker.basis()
            [m0 + (2*z^2+3*z+1)*m3 + (4*z^2+3*z+3)*m4 + (2*z^2+3*z)*m5,
             m1 + (z+3)*m3 + (z^2+z+4)*m4,
             m2 + (2*z^2+4*z+2)*m4 + (2*z^2+z+1)*m5]
        """
    def image(self, names=None):
        """
        Return ``True`` if this morphism is injective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2
            sage: M = S.quotient_module(P^2, names='m')
            sage: M.inject_variables()
            Defining m0, m1, m2, m3, m4, m5
            sage: N = S.quotient_module(P, names='n')
            sage: N.inject_variables()
            Defining n0, n1, n2

            sage: f = N.hom({n0: P*m0})
            sage: im = f.image()
            sage: im
            Ore module of rank 3 over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: im.basis()
            [m0 + (2*z^2+3*z+1)*m3 + (4*z^2+3*z+3)*m4 + (2*z^2+3*z)*m5,
             m1 + (z+3)*m3 + (z^2+z+4)*m4,
             m2 + (2*z^2+4*z+2)*m4 + (2*z^2+z+1)*m5]
        """
    def cokernel(self, names=None):
        """
        Return ``True`` if this morphism is injective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2
            sage: M = S.quotient_module(P^2, names='m')
            sage: M.inject_variables()
            Defining m0, m1, m2, m3, m4, m5
            sage: N = S.quotient_module(P, names='n')
            sage: N.inject_variables()
            Defining n0, n1, n2

            sage: f = N.hom({n0: P*m0})
            sage: coker = f.cokernel()
            sage: coker
            Ore module of rank 3 over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: coker.basis()
            [m3, m4, m5]
        """
    def coimage(self, names=None):
        """
        Return ``True`` if this morphism is injective.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + z^2
            sage: M = S.quotient_module(P^2, names='m')
            sage: M.inject_variables()
            Defining m0, m1, m2, m3, m4, m5
            sage: N = S.quotient_module(P, names='n')
            sage: N.inject_variables()
            Defining n0, n1, n2

            sage: f = M.hom({m0: n0})
            sage: coim = f.coimage()
            sage: coim
            Ore module of rank 3 over Finite Field in z of size 5^3 twisted by z |--> z^5
            sage: coim.basis()
            [m3, m4, m5]
        """
    def determinant(self):
        """
        Return the determinant of this endomorphism.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: M.<m0,m1> = S.quotient_module(X^2 + z)
            sage: f = M.multiplication_map(X^3)
            sage: f.determinant()
            2

        If the domain differs from the codomain (even if they have
        the same rank), an error is raised::

            sage: N.<n0,n1> = S.quotient_module(X^2 + z^25)
            sage: g = M.hom({z*m0: n0})
            sage: g.determinant()
            Traceback (most recent call last):
            ...
            ValueError: determinants are only defined for endomorphisms
        """
    det = determinant
    def characteristic_polynomial(self, var: str = 'x'):
        """
        Return the determinant of this endomorphism.

        EXAMPLES::

            sage: K.<z> = GF(5^3)
            sage: S.<X> = OrePolynomialRing(K, K.frobenius_endomorphism())
            sage: P = X^3 + z*X^2 + (z^2 + 3)*X + z^5
            sage: M = S.quotient_module(P)
            sage: f = M.multiplication_map(X^3)
            sage: f.characteristic_polynomial()
            x^3 + x^2 + 2*x + 2

        We check that the latter is equal to the reduced norm
        of `P`::

            sage: P.reduced_norm('x')
            x^3 + x^2 + 2*x + 2

        TESTS::

            sage: M.<m0,m1> = S.quotient_module(X^2 + z)
            sage: N.<n0,n1> = S.quotient_module(X^2 + z^25)
            sage: g = M.hom({z*m0: n0})
            sage: g.characteristic_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: characteristic polynomials are only defined for endomorphisms
        """
    charpoly = characteristic_polynomial

class OreModuleRetraction(Map):
    """
    Conversion (partially defined) map from an ambient module
    to one of its submodule.
    """
class OreModuleSection(Map):
    """
    Section map of the projection onto a quotient.
    It is not necessarily compatible with the Ore action.
    """
