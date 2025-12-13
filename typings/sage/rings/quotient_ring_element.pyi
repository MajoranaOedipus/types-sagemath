from sage.features import FeatureNotPresentError as FeatureNotPresentError
from sage.structure.element import RingElement as RingElement
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

class QuotientRingElement(RingElement):
    """
    An element of a quotient ring `R/I`.

    INPUT:

    - ``parent`` -- the ring `R/I`

    - ``rep`` -- a representative of the element in `R`; this is used
      as the internal representation of the element

    - ``reduce`` -- boolean (default: ``True``); if ``True``, then the
      internal representation of the element is ``rep`` reduced modulo
      the ideal `I`

    EXAMPLES::

        sage: R.<x> = PolynomialRing(ZZ)
        sage: S.<xbar> = R.quo((4 + 3*x + x^2, 1 + x^2)); S
        Quotient of Univariate Polynomial Ring in x over Integer Ring
         by the ideal (x^2 + 3*x + 4, x^2 + 1)
        sage: v = S.gens(); v
        (xbar,)

    ::

        sage: loads(v[0].dumps()) == v[0]
        True

    ::

        sage: R.<x,y> = PolynomialRing(QQ, 2)
        sage: S = R.quo(x^2 + y^2); S
        Quotient of Multivariate Polynomial Ring in x, y over Rational Field
         by the ideal (x^2 + y^2)
        sage: S.gens()                                                                  # needs sage.libs.singular
        (xbar, ybar)

    We name each of the generators.

    ::

        sage: # needs sage.libs.singular
        sage: S.<a,b> = R.quotient(x^2 + y^2)
        sage: a
        a
        sage: b
        b
        sage: a^2 + b^2 == 0
        True
        sage: b.lift()
        y
        sage: (a^3 + b^2).lift()
        -x*y^2 + y^2
    """
    def __init__(self, parent, rep, reduce: bool = True) -> None:
        """
        An element of a quotient ring `R/I`.  See
        ``QuotientRingElement`` for full documentation.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: S.<xbar> = R.quo((4 + 3*x + x^2, 1 + x^2)); S
            Quotient of Univariate Polynomial Ring in x over Integer Ring
             by the ideal (x^2 + 3*x + 4, x^2 + 1)
            sage: v = S.gens(); v
            (xbar,)
        """
    def lift(self):
        """
        If ``self`` is an element of `R/I`, then return ``self`` as an
        element of `R`.

        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: a.lift()                                                              # needs sage.libs.singular
            x
            sage: (3/5*(a + a^2 + b^2)).lift()                                          # needs sage.libs.singular
            3/5*x
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if quotient ring element is nonzero in the
        quotient ring `R/I`, by determining whether the element
        is in `I`.

        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: bool(a)     # indirect doctest                                        # needs sage.libs.singular
            True
            sage: bool(S(0))                                                            # needs sage.libs.singular
            False

        TESTS::

            sage: bool(a - a)                                                           # needs sage.libs.singular
            False
        """
    def is_unit(self):
        """
        Return ``True`` if ``self`` is a unit in the quotient ring.

        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(1 - x*y); type(a)                     # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: a*b                                                                   # needs sage.libs.singular
            1
            sage: S(2).is_unit()                                                        # needs sage.libs.singular
            True

        Check that :issue:`29469` is fixed::

            sage: a.is_unit()                                                           # needs sage.libs.singular
            True
            sage: (a+b).is_unit()                                                       # needs sage.libs.singular
            False
        """
    def __pari__(self):
        """
        The Pari representation of this quotient element.

        Since Pari does not support quotients by non-principal ideals,
        this function will raise an error in that case.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal(x^3, y^3)
            sage: S.<xb,yb> = R.quo(I)                                                  # needs sage.libs.singular
            sage: pari(xb)                                                              # needs sage.libs.pari sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: Pari does not support quotients by non-principal ideals

        Note that the quotient does work in the case that the ideal is principal::

            sage: I = R.ideal(x^3 + y^3)
            sage: S.<xb,yb> = R.quo(I)                                                  # needs sage.libs.singular
            sage: pari(xb)^4                                                            # needs sage.libs.pari sage.libs.singular
            Mod(-y^3*x, x^3 + y^3)
            sage: pari(yb)^4                                                            # needs sage.libs.pari sage.libs.singular
            Mod(y^4, x^3 + y^3)
        """
    def __int__(self) -> int:
        """
        Try to convert ``self`` (an element of `R/I`) to an integer by
        converting its lift in `R` to an integer.  Return a TypeError
        if no such conversion can be found.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: int(S(-3))                # indirect doctest
            -3
            sage: type(int(S(-3)))
            <... 'int'>
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to <class 'int'>
        """
    def __neg__(self):
        """
        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: -a                     # indirect doctest                             # needs sage.libs.singular
            -a
            sage: -(a+b)                                                                # needs sage.libs.singular
            -a - b
        """
    def __pos__(self):
        """
        TESTS::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: (a+b).__pos__()                                                       # needs sage.libs.singular
            a + b
            sage: c = a+b; c.__pos__() is c                                             # needs sage.libs.singular
            True
        """
    def __invert__(self):
        """
        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: ~S(2/3)                                                               # needs sage.libs.singular
            3/2

        TESTS::

            sage: S(2/3).__invert__()                                                   # needs sage.libs.singular
            3/2

        Note that a is not invertible as an element of R::

            sage: a.__invert__()                                                        # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: float(S(2/3))                                                         # needs sage.libs.singular
            0.6666666666666666
            sage: float(a)                                                              # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to <class 'float'>
        """
    def __hash__(self):
        """
        TESTS::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]
            sage: S.<a,b> = R.quo(x^2 + y^2)
            sage: c = a*a + b
            sage: hash(a) != hash(b)
            True
        """
    def lt(self):
        """
        Return the leading term of this quotient ring element.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = PolynomialRing(GF(7), 3, order='lex')
            sage: I = sage.rings.ideal.FieldIdeal(R)
            sage: Q = R.quo(I)
            sage: f = Q(z*y + 2*x)
            sage: f.lt()
            2*xbar

        TESTS::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: (a + 3*a*b + b).lt()                                                  # needs sage.libs.singular
            3*a*b
        """
    def lm(self):
        """
        Return the leading monomial of this quotient ring element.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = PolynomialRing(GF(7), 3, order='lex')
            sage: I = sage.rings.ideal.FieldIdeal(R)
            sage: Q = R.quo(I)
            sage: f = Q(z*y + 2*x)
            sage: f.lm()
            xbar

        TESTS::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: (a+3*a*b+b).lm()                                                      # needs sage.libs.singular
            a*b
        """
    def lc(self):
        """
        Return the leading coefficient of this quotient ring element.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y,z> = PolynomialRing(GF(7), 3, order='lex')
            sage: I = sage.rings.ideal.FieldIdeal(R)
            sage: Q = R.quo(I)
            sage: f = Q(z*y + 2*x)
            sage: f.lc()
            2

        TESTS::

            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)                   # needs sage.libs.singular
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: (a + 3*a*b + b).lc()                                                  # needs sage.libs.singular
            3
        """
    def variables(self):
        """
        Return all variables occurring in ``self``.

        OUTPUT:

        A tuple of linear monomials, one for each variable occurring
        in ``self``.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: a.variables()
            (a,)
            sage: b.variables()
            (b,)
            sage: s = a^2 + b^2 + 1; s
            1
            sage: s.variables()
            ()
            sage: (a + b).variables()
            (a, b)
        """
    def monomials(self):
        """
        Return the monomials in ``self``.

        OUTPUT: list of monomials

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = QQ[]; S.<a,b> = R.quo(x^2 + y^2); type(a)
            <class 'sage.rings.quotient_ring.QuotientRing_generic_with_category.element_class'>
            sage: a.monomials()
            [a]
            sage: (a + a*b).monomials()
            [a*b, a]
            sage: R.zero().monomials()
            []
        """
    def reduce(self, G):
        """
        Reduce this quotient ring element by a set of quotient ring
        elements ``G``.

        INPUT:

        - ``G`` -- list of quotient ring elements

        .. WARNING::

            This method is not guaranteed to return unique minimal results.
            For quotients of polynomial rings, use
            :meth:`~sage.rings.polynomial.multi_polynomial_ideal.MPolynomialIdeal.reduce`
            on the ideal generated by ``G``, instead.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')
            sage: I1 = ideal([a*b + c*d + 1, a*c*e + d*e,
            ....:             a*b*e + c*e, b*c + c*d*e + 1])
            sage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))
            sage: I2 = ideal([Q(f) for f in I1.gens()])
            sage: f = Q((a*b + c*d + 1)^2  + e)
            sage: f.reduce(I2.gens())
            ebar

        Notice that the result above is not minimal::

            sage: I2.reduce(f)                                                          # needs sage.libs.singular
            0
        """
