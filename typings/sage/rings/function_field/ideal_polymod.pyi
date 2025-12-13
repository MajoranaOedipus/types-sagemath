from .ideal import FunctionFieldIdeal as FunctionFieldIdeal, FunctionFieldIdealInfinite as FunctionFieldIdealInfinite
from sage.arith.power import generic_power as generic_power
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import infinity as infinity
from sage.structure.richcmp import richcmp as richcmp

class FunctionFieldIdeal_polymod(FunctionFieldIdeal):
    """
    Fractional ideals of algebraic function fields.

    INPUT:

    - ``ring`` -- order in a function field

    - ``hnf`` -- matrix in hermite normal form

    - ``denominator`` -- denominator

    The rows of ``hnf`` is a basis of the ideal, which itself is
    ``denominator`` times the fractional ideal.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: K.<x> = FunctionField(GF(2)); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x^3*y - x)
        sage: O = L.maximal_order()
        sage: O.ideal(y)
        Ideal (y) of Maximal order of Function field in y defined by y^2 + x^3*y + x
    """
    def __init__(self, ring, hnf, denominator: int = 1) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3*y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: TestSuite(I).run()
        """
    def __bool__(self) -> bool:
        """
        Test if this ideal is zero.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3*y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y); I
            Ideal (y) of Maximal order of Function field in y defined by y^2 + x^3*y + x
            sage: I.is_zero()
            False
            sage: J = 0*I; J
            Zero ideal of Maximal order of Function field in y defined by y^2 + x^3*y + x
            sage: J.is_zero()
            True

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y>=K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y); I
            Ideal (y) of Maximal order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x
            sage: I.is_zero()
            False
            sage: J = 0*I; J
            Zero ideal of Maximal order of Function field in y defined by y^2 + y + (x^2 + 1)/x
            sage: J.is_zero()
            True
        """
    def __hash__(self):
        """
        Return the hash of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3*Y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(1/y)
            sage: { I: 2 }[I] == 2
            True

            sage: # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(1/y)
            sage: { I: 2 }[I] == 2
            True
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is in this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(7)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal([y]); I
            Ideal (y) of Maximal order of Function field in y
            defined by y^2 + 6*x^3 + 6
            sage: x * y in I
            True
            sage: y / x in I
            False
            sage: y^2 - 2 in I
            False

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal([y]); I
            Ideal (y) of Maximal order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x
            sage: x * y in I
            True
            sage: y / x in I
            False
            sage: y^2 - 2 in I
            False

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal([y]); I
            Ideal (y) of Maximal order of Function field in y
            defined by y^2 - x^3 - 1
            sage: x * y in I
            True
            sage: y / x in I
            False
            sage: y^2 - 2 in I
            False

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal([y]); I
            Ideal (y) of Maximal order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x
            sage: x * y in I
            True
            sage: y / x in I
            False
            sage: y^2 - 2 in I
            False
        """
    def __invert__(self):
        """
        Return the inverse fractional ideal of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(7)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: ~I
            Ideal ((1/(x^3 + 1))*y) of Maximal order of Function field in y defined by y^2 + 6*x^3 + 6
            sage: I^(-1)
            Ideal ((1/(x^3 + 1))*y) of Maximal order of Function field in y defined by y^2 + 6*x^3 + 6
            sage: ~I * I
            Ideal (1) of Maximal order of Function field in y defined by y^2 + 6*x^3 + 6

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: ~I
            Ideal ((x/(x^2 + 1))*y + x/(x^2 + 1)) of Maximal order
            of Function field in y defined by y^2 + y + (x^2 + 1)/x
            sage: I^(-1)
            Ideal ((x/(x^2 + 1))*y + x/(x^2 + 1)) of Maximal order
            of Function field in y defined by y^2 + y + (x^2 + 1)/x
            sage: ~I * I
            Ideal (1) of Maximal order of Function field in y defined by y^2 + y + (x^2 + 1)/x

        ::

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: ~I
            Ideal ((1/(x^3 + 1))*y) of Maximal order of Function field in y defined by y^2 - x^3 - 1
            sage: I^(-1)
            Ideal ((1/(x^3 + 1))*y) of Maximal order of Function field in y defined by y^2 - x^3 - 1
            sage: ~I * I
            Ideal (1) of Maximal order of Function field in y defined by y^2 - x^3 - 1

        ::

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: ~I
            Ideal ((x/(x^2 + 1))*y + x/(x^2 + 1)) of Maximal order
            of Function field in y defined by y^2 + y + (x^2 + 1)/x
            sage: I^(-1)
            Ideal ((x/(x^2 + 1))*y + x/(x^2 + 1)) of Maximal order
            of Function field in y defined by y^2 + y + (x^2 + 1)/x
            sage: ~I * I
            Ideal (1) of Maximal order of Function field in y defined by y^2 + y + (x^2 + 1)/x
        """
    def intersect(self, other):
        """
        Intersect this ideal with the other ideal as fractional ideals.

        INPUT:

        - ``other`` -- ideal

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3*Y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: J = O.ideal(x)
            sage: I.intersect(J) == I * J * (I + J)^-1
            True
        """
    def hnf(self):
        """
        Return the matrix in hermite normal form representing this ideal.

        See also :meth:`denominator`

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y*(y+1)); I.hnf()
            [x^6 + x^3         0]
            [  x^3 + 1         1]

        ::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y*(y+1)); I.hnf()
            [x^6 + x^3         0]
            [  x^3 + 1         1]
        """
    def denominator(self):
        """
        Return the denominator of this fractional ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y/(y+1))
            sage: d = I.denominator(); d
            x^3
            sage: d in O
            True

        ::

            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y/(y+1))
            sage: d = I.denominator(); d
            x^3
            sage: d in O
            True
        """
    @cached_method
    def module(self):
        """
        Return the module, that is the ideal viewed as a module
        over the base maximal order.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: F.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.module()
            Free module of degree 2 and rank 2 over Maximal order
            of Rational function field in x over Finite Field of size 7
            Echelon basis matrix:
            [          1           0]
            [          0 1/(x^3 + 1)]
        """
    @cached_method
    def gens_over_base(self) -> tuple:
        """
        Return the generators of this ideal as a module over the maximal order
        of the base rational function field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3*Y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: I.gens_over_base()
            (x^4 + x^2 + x, y + x)

            sage: # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: I.gens_over_base()
            (x^3 + 1, y + x)
        """
    def gens(self) -> tuple:
        """
        Return a set of generators of this ideal.

        This provides whatever set of generators as quickly
        as possible.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3*Y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: I.gens()
            (x^4 + x^2 + x, y + x)

            sage: # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: I.gens()
            (x^3 + 1, y + x)
        """
    @cached_method
    def basis_matrix(self):
        """
        Return the matrix of basis vectors of this ideal as a module.

        The basis matrix is by definition the hermite norm form of the ideal
        divided by the denominator.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.denominator() * I.basis_matrix() == I.hnf()
            True
        """
    def is_integral(self):
        """
        Return ``True`` if this is an integral ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.is_integral()
            False
            sage: J = I.denominator() * I
            sage: J.is_integral()
            True

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.is_integral()
            False
            sage: J = I.denominator() * I
            sage: J.is_integral()
            True

            sage: K.<x> = FunctionField(QQ); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.is_integral()
            False
            sage: J = I.denominator() * I
            sage: J.is_integral()
            True
        """
    def ideal_below(self):
        """
        Return the ideal below this ideal.

        This is defined only for integral ideals.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<t> = K[]
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.ideal_below()
            Traceback (most recent call last):
            ...
            TypeError: not an integral ideal
            sage: J = I.denominator() * I
            sage: J.ideal_below()
            Ideal (x^3 + x^2 + x) of Maximal order of Rational function field
            in x over Finite Field of size 2

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.ideal_below()
            Traceback (most recent call last):
            ...
            TypeError: not an integral ideal
            sage: J = I.denominator() * I
            sage: J.ideal_below()
            Ideal (x^3 + x) of Maximal order of Rational function field
            in x over Finite Field of size 2

            sage: K.<x> = FunctionField(QQ); _.<t> = K[]
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, 1/y)
            sage: I.ideal_below()
            Traceback (most recent call last):
            ...
            TypeError: not an integral ideal
            sage: J = I.denominator() * I
            sage: J.ideal_below()
            Ideal (x^3 + x^2 + x) of Maximal order of Rational function field
            in x over Rational Field
        """
    def norm(self):
        """
        Return the norm of this fractional ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: i1 = O.ideal(x)
            sage: i2 = O.ideal(y)
            sage: i3 = i1 * i2
            sage: i3.norm() == i1.norm() * i2.norm()
            True
            sage: i1.norm()
            x^3
            sage: i1.norm() == x ** F.degree()
            True
            sage: i2.norm()
            x^6 + x^4 + x^2
            sage: i2.norm() == y.norm()
            True

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: i1 = O.ideal(x)
            sage: i2 = O.ideal(y)
            sage: i3 = i1 * i2
            sage: i3.norm() == i1.norm() * i2.norm()
            True
            sage: i1.norm()
            x^2
            sage: i1.norm() == x ** L.degree()
            True
            sage: i2.norm()
            (x^2 + 1)/x
            sage: i2.norm() == y.norm()
            True
        """
    @cached_method
    def is_prime(self):
        """
        Return ``True`` if this ideal is a prime ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.is_prime() for f,_ in I.factor()]
            [True, True]

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.is_prime() for f,_ in I.factor()]
            [True, True]

            sage: K.<x> = FunctionField(QQ); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.is_prime() for f,_ in I.factor()]
            [True, True]
        """
    def valuation(self, ideal):
        """
        Return the valuation of ``ideal`` at this prime ideal.

        INPUT:

        - ``ideal`` -- fractional ideal

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<t> = K[]
            sage: F.<y> = K.extension(t^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x, (1/(x^3 + x^2 + x))*y^2)
            sage: I.is_prime()
            True
            sage: J = O.ideal(y)
            sage: I.valuation(J)
            2

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.valuation(I) for f,_ in I.factor()]
            [-1, 2]

        The method closely follows Algorithm 4.8.17 of [Coh1993]_.
        """
    def prime_below(self):
        """
        Return the prime lying below this prime ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.prime_below() for f,_ in I.factor()]
            [Ideal (x) of Maximal order of Rational function field in x
            over Finite Field of size 2, Ideal (x^2 + x + 1) of Maximal order
            of Rational function field in x over Finite Field of size 2]

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.prime_below() for f,_ in I.factor()]
            [Ideal (x) of Maximal order of Rational function field in x over Finite Field of size 2,
             Ideal (x + 1) of Maximal order of Rational function field in x over Finite Field of size 2]

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.prime_below() for f,_ in I.factor()]
            [Ideal (x) of Maximal order of Rational function field in x over Rational Field,
             Ideal (x^2 + x + 1) of Maximal order of Rational function field in x over Rational Field]
        """

class FunctionFieldIdeal_global(FunctionFieldIdeal_polymod):
    """
    Fractional ideals of canonical function fields.

    INPUT:

    - ``ring`` -- order in a function field

    - ``hnf`` -- matrix in hermite normal form

    - ``denominator`` -- denominator

    The rows of ``hnf`` is a basis of the ideal, which itself is
    ``denominator`` times the fractional ideal.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: K.<x> = FunctionField(GF(2)); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x^3*y - x)
        sage: O = L.maximal_order()
        sage: O.ideal(y)
        Ideal (y) of Maximal order of Function field in y defined by y^2 + x^3*y + x
    """
    def __init__(self, ring, hnf, denominator: int = 1) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(5)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3*y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: TestSuite(I).run()
        """
    def __pow__(self, mod):
        """
        Return ``self`` to the power of ``mod``.

        If a two-generators representation of ``self`` is known, it is used
        to speed up powering.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^7 - x^3*Y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: J = O.ideal(x + y)
            sage: S = I / J
            sage: a = S^100
            sage: _ = S.gens_two()
            sage: b = S^100  # faster
            sage: b == I^100 / J^100
            True
            sage: b == a
            True
        """
    def gens(self) -> tuple:
        """
        Return a set of generators of this ideal.

        This provides whatever set of generators as quickly
        as possible.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 - x^3*Y - x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: I.gens()
            (x^4 + x^2 + x, y + x)

            sage: # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(x + y)
            sage: I.gens()
            (x^3 + 1, y + x)
        """
    def gens_two(self) -> tuple:
        """
        Return two generators of this fractional ideal.

        If the ideal is principal, one generator *may* be returned.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<t> = K[]
            sage: F.<y> = K.extension(t^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: I  # indirect doctest
            Ideal (y) of Maximal order of Function field
            in y defined by y^3 + x^6 + x^4 + x^2
            sage: ~I  # indirect doctest
            Ideal ((1/(x^6 + x^4 + x^2))*y^2) of Maximal order of Function field
            in y defined by y^3 + x^6 + x^4 + x^2

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: I  # indirect doctest
            Ideal (y) of Maximal order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x
            sage: ~I  # indirect doctest
            Ideal ((x/(x^2 + 1))*y + x/(x^2 + 1)) of Maximal order
            of Function field in y defined by y^2 + y + (x^2 + 1)/x
        """

class FunctionFieldIdealInfinite_polymod(FunctionFieldIdealInfinite):
    """
    Ideals of the infinite maximal order of an algebraic function field.

    INPUT:

    - ``ring`` -- infinite maximal order of the function field

    - ``ideal`` -- ideal in the inverted function field

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: K.<x> = FunctionField(GF(3^2)); R.<t> = PolynomialRing(K)
        sage: F.<y> = K.extension(t^3 + t^2 - x^4)
        sage: Oinf = F.maximal_order_infinite()
        sage: Oinf.ideal(1/y)
        Ideal (1/x^4*y^2) of Maximal infinite order of Function field
        in y defined by y^3 + y^2 + 2*x^4
    """
    def __init__(self, ring, ideal) -> None:
        """
        Initialize this ideal.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/y)
            sage: TestSuite(I).run()
        """
    def __hash__(self):
        """
        Return the hash of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/y)
            sage: d = { I: 1 }

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(1/y)
            sage: d = { I: 1 }
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is in this ideal.

        INPUT:

        - ``x`` -- element of the function field

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/y)
            sage: 1/y in I
            True
            sage: 1/x in I
            False
            sage: 1/x^2 in I
            True
        """
    def __pow__(self, n):
        """
        Raise this ideal to ``n``-th power.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: J = Oinf.ideal(1/x)
            sage: J^3
            Ideal (1/x^3) of Maximal infinite order of Function field
            in y defined by y^3 + y^2 + 2*x^4
        """
    def __invert__(self):
        """
        Return the inverted ideal of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: J = Oinf.ideal(y)
            sage: ~J
            Ideal (1/x^4*y^2) of Maximal infinite order
            of Function field in y defined by y^3 + y^2 + 2*x^4
            sage: J * ~J
            Ideal (1) of Maximal infinite order of Function field
            in y defined by y^3 + y^2 + 2*x^4

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: J = Oinf.ideal(y)
            sage: ~J
            Ideal (1/x*y) of Maximal infinite order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x
            sage: J * ~J
            Ideal (1) of Maximal infinite order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x
        """
    def gens(self) -> tuple:
        """
        Return a set of generators of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(x + y)
            sage: I.gens()
            (x, y, 1/x^2*y^2)

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(x + y)
            sage: I.gens()
            (x, y)
        """
    def gens_two(self) -> tuple:
        """
        Return a set of at most two generators of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(x + y)
            sage: I.gens_two()
            (x, y)

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(x + y)
            sage: I.gens_two()
            (x,)
        """
    def gens_over_base(self) -> tuple:
        """
        Return a set of generators of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = K[]
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(x + y)
            sage: I.gens_over_base()
            (x, y, 1/x^2*y^2)
        """
    def ideal_below(self):
        """
        Return a set of generators of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = K[]
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/y^2)
            sage: I.ideal_below()
            Ideal (x^3) of Maximal order of Rational function field
            in x over Finite Field in z2 of size 3^2
        """
    def is_prime(self):
        """
        Return ``True`` if this ideal is a prime ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/x)
            sage: I.factor()
            (Ideal (1/x^3*y^2) of Maximal infinite order of Function field
            in y defined by y^3 + y^2 + 2*x^4)^3
            sage: I.is_prime()
            False
            sage: J = I.factor()[0][0]
            sage: J.is_prime()
            True

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(1/x)
            sage: I.factor()
            (Ideal (1/x*y) of Maximal infinite order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x)^2
            sage: I.is_prime()
            False
            sage: J = I.factor()[0][0]
            sage: J.is_prime()
            True
        """
    @cached_method
    def prime_below(self):
        """
        Return the prime of the base order that underlies this prime ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(3^2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/x)
            sage: I.factor()
            (Ideal (1/x^3*y^2) of Maximal infinite order of Function field
            in y defined by y^3 + y^2 + 2*x^4)^3
            sage: J = I.factor()[0][0]
            sage: J.is_prime()
            True
            sage: J.prime_below()
            Ideal (1/x) of Maximal infinite order of Rational function field
            in x over Finite Field in z2 of size 3^2

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(1/x)
            sage: I.factor()
            (Ideal (1/x*y) of Maximal infinite order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x)^2
            sage: J = I.factor()[0][0]
            sage: J.is_prime()
            True
            sage: J.prime_below()
            Ideal (1/x) of Maximal infinite order of Rational function field in x
            over Finite Field of size 2
        """
    def valuation(self, ideal):
        """
        Return the valuation of ``ideal`` with respect to this prime ideal.

        INPUT:

        - ``ideal`` -- fractional ideal

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(y)
            sage: [f.valuation(I) for f,_ in I.factor()]
            [-1]
        """
