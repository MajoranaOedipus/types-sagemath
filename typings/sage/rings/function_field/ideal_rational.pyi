from .ideal import FunctionFieldIdeal as FunctionFieldIdeal, FunctionFieldIdealInfinite as FunctionFieldIdealInfinite
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.structure.richcmp import richcmp as richcmp

class FunctionFieldIdeal_rational(FunctionFieldIdeal):
    """
    Fractional ideals of the maximal order of a rational function field.

    INPUT:

    - ``ring`` -- the maximal order of the rational function field

    - ``gen`` -- generator of the ideal, an element of the function field

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: O = K.maximal_order()
        sage: I = O.ideal(1/(x^2+x)); I
        Ideal (1/(x^2 + x)) of Maximal order of Rational function field in x over Rational Field
    """
    def __init__(self, ring, gen) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order()
            sage: I = O.ideal(1/(x^2+x))
            sage: TestSuite(I).run()
        """
    def __hash__(self):
        """
        Return the hash computed from the data.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order()
            sage: I = O.ideal(1/(x^2+x))
            sage: d = { I: 1, I^2: 2 }
        """
    def __contains__(self, element) -> bool:
        """
        Test if ``element`` is in this ideal.

        INPUT:

        - ``element`` -- element of the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order()
            sage: I = O.ideal(1/(x+1))
            sage: x in I
            True
        """
    def __invert__(self):
        """
        Return the ideal inverse of this fractional ideal.

        EXAMPLES::

            sage: F.<x> = FunctionField(QQ)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x/(x^2+1))
            sage: ~I
            Ideal ((x^2 + 1)/x) of Maximal order of Rational function field
            in x over Rational Field
        """
    def denominator(self):
        """
        Return the denominator of this fractional ideal.

        EXAMPLES::

            sage: F.<x> = FunctionField(QQ)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x/(x^2+1))
            sage: I.denominator()
            x^2 + 1
        """
    def is_prime(self):
        """
        Return ``True`` if this is a prime ideal.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^3 + x^2)
            sage: [f.is_prime() for f,m in I.factor()]                                  # needs sage.libs.pari
            [True, True]
        """
    @cached_method
    def module(self):
        """
        Return the module, that is the ideal viewed as a module over the ring.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^3 + x^2)
            sage: I.module()                                                                                            # needs sage.modules
            Free module of degree 1 and rank 1 over Maximal order of Rational
            function field in x over Rational Field
            Echelon basis matrix:
            [x^3 + x^2]
            sage: J = 0*I
            sage: J.module()                                                                                            # needs sage.modules
            Free module of degree 1 and rank 0 over Maximal order of Rational
            function field in x over Rational Field
            Echelon basis matrix:
            []
        """
    def gen(self):
        """
        Return the unique generator of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^2 + x)
            sage: I.gen()
            x^2 + x
        """
    def gens(self) -> tuple:
        """
        Return the tuple of the unique generator of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^2 + x)
            sage: I.gens()
            (x^2 + x,)
        """
    def gens_over_base(self) -> tuple:
        """
        Return the generator of this ideal as a rank one module over the maximal
        order.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^2 + x)
            sage: I.gens_over_base()
            (x^2 + x,)
        """
    def valuation(self, ideal):
        """
        Return the valuation of the ideal at this prime ideal.

        INPUT:

        - ``ideal`` -- fractional ideal

        EXAMPLES::

            sage: F.<x> = FunctionField(QQ)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x^2*(x^2+x+1)^3)
            sage: [f.valuation(I) for f,_ in I.factor()]                                # needs sage.libs.pari
            [2, 3]
        """

class FunctionFieldIdealInfinite_rational(FunctionFieldIdealInfinite):
    """
    Fractional ideal of the maximal order of rational function field.

    INPUT:

    - ``ring`` -- infinite maximal order

    - ``gen`` -- generator

    Note that the infinite maximal order is a principal ideal domain.

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2))
        sage: Oinf = K.maximal_order_infinite()
        sage: Oinf.ideal(x)
        Ideal (x) of Maximal infinite order of Rational function field in x over Finite Field of size 2
    """
    def __init__(self, ring, gen) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal(x)
            sage: TestSuite(I).run()
        """
    def __hash__(self):
        """
        Return the hash of this fractional ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal(x)
            sage: J = Oinf.ideal(1/x)
            sage: d = { I: 1, J: 2 }
        """
    def __contains__(self, element) -> bool:
        """
        Test if ``element`` is in this ideal.

        INPUT:

        - ``element`` -- element of the function field

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: O = K.maximal_order_infinite()
            sage: I = O.ideal(1/(x+1))
            sage: x in I
            False
            sage: 1/x in I
            True
            sage: x/(x+1) in I
            False
            sage: 1/(x*(x+1)) in I
            True
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal(x/(x^2 + 1))
            sage: ~I  # indirect doctest
            Ideal (x) of Maximal infinite order of Rational function field in x
            over Finite Field of size 2
        """
    def is_prime(self):
        """
        Return ``True`` if this ideal is a prime ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal(x/(x^2 + 1))
            sage: I.is_prime()
            True
        """
    def gen(self):
        """
        Return the generator of this principal ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x+1)/(x^3+x), (x^2+1)/x^4)
            sage: I.gen()
            1/x^2
        """
    def gens(self) -> tuple:
        """
        Return the generator of this principal ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x+1)/(x^3+x), (x^2+1)/x^4)
            sage: I.gens()
            (1/x^2,)
        """
    def gens_over_base(self) -> tuple:
        """
        Return the generator of this ideal as a rank one module
        over the infinite maximal order.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x+1)/(x^3+x), (x^2+1)/x^4)
            sage: I.gens_over_base()
            (1/x^2,)
        """
    def valuation(self, ideal):
        """
        Return the valuation of ``ideal`` at this prime ideal.

        INPUT:

        - ``ideal`` -- fractional ideal

        EXAMPLES::

            sage: F.<x> = FunctionField(QQ)
            sage: O = F.maximal_order_infinite()
            sage: p = O.ideal(1/x)
            sage: p.valuation(O.ideal(x/(x+1)))
            0
            sage: p.valuation(O.ideal(0))
            +Infinity
        """
