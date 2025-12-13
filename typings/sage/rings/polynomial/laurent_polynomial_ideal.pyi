from sage.arith.misc import GCD as GCD
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing_univariate as LaurentPolynomialRing_univariate
from sage.structure.richcmp import op_EQ as op_EQ, op_GE as op_GE, op_GT as op_GT, op_LE as op_LE, op_LT as op_LT, op_NE as op_NE

class LaurentPolynomialIdeal(Ideal_generic):
    def __init__(self, ring, gens, coerce: bool = True, hint=None) -> None:
        """
        Create an ideal in a Laurent polynomial ring.

        To compute structural properties of an ideal in the Laurent polynomial ring
        `R[x_1^{\\pm},\\ldots,x_n^{\\pm}]`, we form the corresponding ideal in the
        associated ordinary polynomial ring `R[x_1,\\ldots,x_n]` which is saturated
        with respect to the ideal `(x_1 \\cdots x_n)`. Since computing the saturation
        can be expensive, we employ some strategies to reduce the need for it.

        - We only create the polynomial ideal as needed.

        - For some operations, we try some superficial tests first. E.g., for
          comparisons, we first look directly at generators.
        - The attribute ``hint`` is a lower bound on the associated polynomial ideal.
          Hints are automatically forwarded by certain creation operations (such as
          sums and base extensions), and can be manually forwarded in other cases.

        INPUT:

        - ``ring`` -- the ring the ideal is defined in
        - ``gens`` -- list of generators for the ideal
        - ``coerce`` -- whether or not to coerce elements into ``ring``
        - ``hint`` -- an ideal in the associated polynomial ring (optional; see above)

        EXAMPLES::

            sage: R.<x,y> = LaurentPolynomialRing(IntegerRing(), 2, order='lex')
            sage: R.ideal([x, y])
            Ideal (x, y) of Multivariate Laurent Polynomial Ring in x, y
            over Integer Ring
            sage: R.<x0,x1> = LaurentPolynomialRing(GF(3), 2)
            sage: R.ideal([x0^2, x1^-3])
            Ideal (x0^2, x1^-3) of Multivariate Laurent Polynomial Ring in x0, x1
            over Finite Field of size 3

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([~x + ~y - 1])
            sage: print(I)
            Ideal (-1 + y^-1 + x^-1) of
             Multivariate Laurent Polynomial Ring in x, y over Rational Field
            sage: I.is_zero()
            False
            sage: (x^(-2) + x^(-1)*y^(-1) - x^(-1)) in I
            True

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: I1 = P.ideal([x*y*z + x*y + 2*y^2, x + z])
            sage: I2 = P.ideal([x*y*z + x*y + 2*y^2 + x + z, x + z])
            sage: I1 == I2
            True
            sage: I3 = P.ideal([x*y*z + x*y + 2*y^2 + x + z, x + z, y])
            sage: I1 < I3
            True
            sage: I1.minimal_associated_primes()
            (Ideal (-1/2*z^2 + y - 1/2*z, x + z) of Multivariate
              Laurent Polynomial Ring in x, y, z over Rational Field,)

            sage: K.<z> = CyclotomicField(4)                                            # needs sage.rings.number_field
            sage: J = I1.base_extend(K)                                                 # needs sage.rings.number_field
            sage: J.base_ring()                                                         # needs sage.rings.number_field
            Cyclotomic Field of order 4 and degree 2
        """
    def set_hint(self, hint) -> None:
        """
        Set the hint of this ideal.

        The hint is an ideal of the associated polynomial ring, which is
        assumed to be contained in the associated ideal. It is used internally
        to speed up computation of the associated ideal in some cases;
        normally the end user will have no need to work with it directly.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: I = P.ideal([x^2*y + 3*x*y^2])
            sage: I.hint()
            Ideal (0) of Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: I.set_hint(P.polynomial_ring().ideal([x + 3*y]))
            sage: I.hint()
            Ideal (x + 3*y) of Multivariate Polynomial Ring in x, y, z over Rational Field
        """
    def hint(self):
        """
        Return the hint of this ideal.

        The hint is an ideal of the associated polynomial ring, which is
        assumed to be contained in the associated ideal. It is used internally
        to speed up computation of the associated ideal in some cases;
        normally the end user will have no need to work with it directly.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: I = P.ideal([x^2*y + 3*x*y^2])
            sage: I.hint()
            Ideal (0) of Multivariate Polynomial Ring in x, y, z over Rational Field
        """
    def __contains__(self, f) -> bool:
        """
        Implement containment testing (in) for Laurent polynomial ideals.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x^2*y + 3*x*y^2])
            sage: x + 3*y in I
            True

        This also works in the univariate case::

            sage: P.<x> = LaurentPolynomialRing(QQ)
            sage: I = P.ideal([x^2 + 3*x])
            sage: 1 + 3*x^-1 in I
            True
        """
    def gens_reduced(self) -> tuple:
        """
        Return a reduced system of generators.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: J = P.ideal([x^2 - y^-2, x * y^3 + 2 * y^2+ y])
            sage: J.gens_reduced()
            (x + 6*y + 5, 3*y^2 + 4*y + 1)
        """
    def change_ring(self, R, hint=None):
        """
        Coerce an ideal into a new ring.

        This operation does not forward hints, but a new hint can be
        specified manually.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x + y])
            sage: Q.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: I.change_ring(Q)
            Ideal (x + y) of Multivariate Laurent Polynomial Ring in x, y, z
             over Rational Field
        """
    def base_extend(self, F):
        """
        Form the base extension of ``self`` to the base ring ``F``.

        This operation forwards hints.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x + y])
            sage: K.<z> = CyclotomicField(3)                                            # needs sage.rings.number_field
            sage: I.base_extend(K)                                                      # needs sage.rings.number_field
            Ideal (x + y) of Multivariate Laurent Polynomial Ring in x, y
             over Cyclotomic Field of order 3 and degree 2
        """
    def apply_map(self, f, new_ring=None, new_base_ring=None, apply_to_hint=None):
        """
        Return the new ideal obtained by applying ``f`` to each generator.

        By default, this does not forward hints. To do so, set ``apply_to_hint``
        to specify a function to apply to generators of ``hint``.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x + 1, y - 1])
            sage: I.apply_map(lambda z: z + 2)
            Ideal (x + 3, y + 1) of Multivariate Laurent Polynomial Ring in x, y
             over Rational Field
            sage: K.<i> = CyclotomicField(4)                                            # needs sage.rings.number_field
            sage: I.apply_map(lambda z: z + 2, new_base_ring=K)                         # needs sage.rings.number_field
            Ideal (x + 3, y + 1) of Multivariate Laurent Polynomial Ring in x, y
             over Cyclotomic Field of order 4 and degree 2
        """
    def apply_coeff_map(self, f, new_base_ring=None, forward_hint: bool = True):
        """
        Apply a function to coefficients.

        This operation forwards hints by default.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<z> = CyclotomicField(3)
            sage: P.<x,y> = LaurentPolynomialRing(K, 2)
            sage: I = P.ideal([x + z, y - z])
            sage: h = K.hom([z^2])
            sage: I.apply_coeff_map(h)
            Ideal (x - z - 1, y + z + 1) of Multivariate Laurent Polynomial Ring
             in x, y over Cyclotomic Field of order 3 and degree 2
            sage: K1.<z1> = CyclotomicField(12)
            sage: h1 = K.hom([z1^4])
            sage: I.apply_coeff_map(h1, new_base_ring=K1)
            Ideal (x + z1^2 - 1, y - z1^2 + 1) of Multivariate Laurent Polynomial Ring
             in x, y over Cyclotomic Field of order 12 and degree 4
        """
    def toric_coordinate_change(self, M, forward_hint: bool = True):
        """
        Compute the toric change of coordinates defined by the integer matrix ``M``.

        This operation forwards hints by default.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<z> = CyclotomicField(3)
            sage: P.<x,y> = LaurentPolynomialRing(K, 2)
            sage: I = P.ideal([x + 1, y - 1])
            sage: M = Matrix([[2,1], [1,-3]])
            sage: I.toric_coordinate_change(M)
            Ideal (x^2*y + 1, -1 + x*y^-3) of Multivariate Laurent Polynomial Ring
             in x, y over Cyclotomic Field of order 3 and degree 2
        """
    def __add__(self, other):
        """
        Return the sum of two ideals in the same ring.

        Currently this operation does not support coercion.

        This operation forwards hints.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x+y])
            sage: J = P.ideal([y+1])
            sage: (I+J).groebner_basis()
            (x - 1, y + 1)
        """
    def normalize_gens(self):
        """
        Redefine the ideal with a normalized set of generators.

        For two ideals returned by this function, equality testing can be done
        by comparing generators.

        This operation forwards hints.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([~x+y])
            sage: J = P.ideal([y+1])
            sage: I + J
            Ideal (y + x^-1, y + 1) of Multivariate Laurent Polynomial Ring
             in x, y over Rational Field
            sage: (I + J).normalize_gens()
            Ideal (x - 1, y + 1) of Multivariate Laurent Polynomial Ring
             in x, y over Rational Field
        """
    def polynomial_ideal(self, saturate: bool = True):
        """
        Return the associated polynomial ideal.

        By default, the ideal is saturated with respect to the product of the
        polynomial ring generators; this is necessary for testing equality and inclusion.
        As saturation can be quite time-consuming, it can be disabled by setting
        ``saturate=False``; however, the result will then depend not just on the original ideal
        but also on the choice of generators.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x^2*y + 3*x*y^2])
            sage: I.polynomial_ideal()
            Ideal (x + 3*y) of Multivariate Polynomial Ring in x, y over Rational Field
            sage: P.<t> = LaurentPolynomialRing(QQ)
            sage: J = P.ideal(t^2 - t^-1)
            sage: J.polynomial_ideal()
            Principal ideal (t^3 - 1) of Univariate Polynomial Ring in t over Rational Field
            sage: J = P.ideal([t^2 - t^-1, t + t^-1])
            sage: J.polynomial_ideal()
            Principal ideal (1) of Univariate Polynomial Ring in t over Rational Field
            sage: J = P.ideal([t^2 - t^-1, t - t^-1])
            sage: J.polynomial_ideal()
            Principal ideal (t - 1) of Univariate Polynomial Ring in t over Rational Field
        """
    def groebner_basis(self, saturate: bool = True):
        """
        Return the reduced Groebner basis for the specified term order.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x + y])
            sage: J = P.ideal([y + 1])
            sage: (I + J).groebner_basis()
            (x - 1, y + 1)
        """
    def is_one(self):
        """
        Determine whether or not ``self`` is the unit ideal.

        This requires saturation of the polynomial ideal.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([~x + ~y - 1, x + y])
            sage: I.is_one()
            True
        """
    def is_binomial(self, groebner_basis: bool = False):
        """
        Determine whether every generator of ``self`` is a binomial.

        If ``groebner_basis`` is True, this becomes intrinsic (for a choice of
        term order).

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: I = P.ideal([x + y])
            sage: I.is_binomial()
            True
        """
    def associated_primes(self):
        """
        Return associated primes of this ideal.

        These are computed from the polynomial ideal, but it is not necessary to
        saturate. Instead, we omit primes containing any polynomial generator.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: p = z^2 + 1; q = z^3 + 2
            sage: I = P.ideal((p*q^2, y - z^2))
            sage: tuple(sorted(I.associated_primes(), key=str))
            (Ideal (y + 1, z^2 + 1) of
              Multivariate Laurent Polynomial Ring in x, y, z over Rational Field,
             Ideal (z^2 - y, y*z + 2, y^2 + 2*z) of
              Multivariate Laurent Polynomial Ring in x, y, z over Rational Field)
        """
    def minimal_associated_primes(self, saturate: bool = False):
        """
        Return minimal associated primes of this ideal.

        These are computed from the polynomial ideal, but it is not necessary to
        saturate. Instead, we omit primes containing any polynomial generator.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: p = z^2 + 1; q = z^3 + 2
            sage: I = P.ideal((p*q^2, y - z^2))
            sage: tuple(sorted(I.minimal_associated_primes(), key=str))
            (Ideal (z^2 + 1, -z^2 + y) of
              Multivariate Laurent Polynomial Ring in x, y, z over Rational Field,
             Ideal (z^3 + 2, -z^2 + y) of
              Multivariate Laurent Polynomial Ring in x, y, z over Rational Field)
        """
    def radical(self):
        """
        Return the radical of this ideal.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: I = P.ideal(((x+1)^2, (y+1)^3, ((x+1)*z)^4 + (y+1)^3 + 10*(x+1)^2))
            sage: I.radical()
            Ideal (y + 1, x + 1) of Multivariate Laurent Polynomial Ring in x, y, z
             over Rational Field
        """
    def dimension(self):
        """
        Return the dimension of this ideal.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ, 3)
            sage: I = P.ideal(((x+1)^2, (y+1)^3, ((x+1)*z)^4 + (y+1)^3 + 10*(x+1)^2))
            sage: I.dimension()
            1
        """
