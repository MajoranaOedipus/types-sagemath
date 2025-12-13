from sage.categories.rings import Rings as Rings
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import RingElement as RingElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FractionWithFactoredDenominator(RingElement):
    """
    This element represents a fraction with a factored polynomial
    denominator. See also its parent
    :class:`FractionWithFactoredDenominatorRing` for details.

    Represents a fraction with factored polynomial denominator (FFPD)
    `p/(q_1^{e_1} \\cdots q_n^{e_n})` by storing the parts `p` and
    `[(q_1, e_1), \\ldots, (q_n, e_n)]`.
    Here `q_1, \\ldots, q_n` are elements of a 0- or multi-variate factorial
    polynomial ring `R` , `q_1, \\ldots, q_n` are distinct irreducible elements
    of `R` , `e_1, \\ldots, e_n` are positive integers, and `p` is a function
    of the indeterminates of `R` (e.g., a Sage symbolic expression). An
    element `r` with no polynomial denominator is represented as ``(r, [])``.

    INPUT:

    - ``numerator`` -- an element `p`; this can be of any ring from which
      parent's base has coercion in
    - ``denominator_factored`` -- list of the form
      `[(q_1, e_1), \\ldots, (q_n, e_n)]`, where the `q_1, \\ldots, q_n` are
      distinct irreducible elements of `R` and the `e_i` are positive
      integers
    - ``reduce`` -- (optional) if ``True``, then represent
      `p/(q_1^{e_1} \\cdots q_n^{e_n})` in lowest terms, otherwise
      this won't attempt to divide `p` by any of the `q_i`

    OUTPUT:

    An element representing the rational expression
    `p/(q_1^{e_1} \\cdots q_n^{e_n})`.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
        sage: R.<x,y> = PolynomialRing(QQ)
        sage: FFPD = FractionWithFactoredDenominatorRing(R)
        sage: df = [x, 1], [y, 1], [x*y+1, 1]
        sage: f = FFPD(x, df)
        sage: f
        (1, [(y, 1), (x*y + 1, 1)])
        sage: ff = FFPD(x, df, reduce=False)
        sage: ff
        (x, [(y, 1), (x, 1), (x*y + 1, 1)])

        sage: f = FFPD(x + y, [(x + y, 1)])
        sage: f
        (1, [])

    ::

        sage: R.<x> = PolynomialRing(QQ)
        sage: FFPD = FractionWithFactoredDenominatorRing(R)
        sage: f = 5*x^3 + 1/x + 1/(x-1) + 1/(3*x^2 + 1)
        sage: FFPD(f)
        (5*x^7 - 5*x^6 + 5/3*x^5 - 5/3*x^4 + 2*x^3 - 2/3*x^2 + 1/3*x - 1/3,
        [(x - 1, 1), (x, 1), (x^2 + 1/3, 1)])

    ::

        sage: R.<x,y> = PolynomialRing(QQ)
        sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
        sage: f = 2*y/(5*(x^3 - 1)*(y + 1))
        sage: FFPD(f)
        (2/5*y, [(y + 1, 1), (x - 1, 1), (x^2 + x + 1, 1)])

        sage: p = 1/x^2
        sage: q = 3*x**2*y
        sage: qs = q.factor()
        sage: f = FFPD(p/qs.unit(), qs)
        sage: f
        (1/3/x^2, [(y, 1), (x, 2)])

        sage: f = FFPD(cos(x)*x*y^2, [(x, 2), (y, 1)])
        sage: f
        (x*y^2*cos(x), [(y, 1), (x, 2)])

        sage: G = exp(x + y)
        sage: H = (1 - 2*x - y) * (1 - x - 2*y)
        sage: a = FFPD(G/H)
        sage: a
        (e^(x + y), [(x + 2*y - 1, 1), (2*x + y - 1, 1)])
        sage: a.denominator_ring
        Multivariate Polynomial Ring in x, y over Rational Field
        sage: b = FFPD(G, H.factor())
        sage: b
        (e^(x + y), [(x + 2*y - 1, 1), (2*x + y - 1, 1)])
        sage: b.denominator_ring
        Multivariate Polynomial Ring in x, y over Rational Field

    Singular throws a 'not implemented' error when trying to factor in
    a multivariate polynomial ring over an inexact field::

        sage: R.<x,y> = PolynomialRing(CC)
        sage: FFPD = FractionWithFactoredDenominatorRing(R)
        sage: f = (x + 1)/(x*y*(x*y + 1)^2)
        sage: FFPD(f)
        Traceback (most recent call last):
        ...
        TypeError: Singular error:
           ? not implemented
           ? error occurred in or before STDIN line ...:
           `def sage...=factorize(sage...);`

    AUTHORS:

    - Alexander Raichev (2012-07-26)
    - Daniel Krenn (2014-12-01)
    """
    def __init__(self, parent, numerator, denominator_factored, reduce: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: df = [x, 1], [y, 1], [x*y+1, 1]
            sage: f = FFPD(x, df)
            sage: TestSuite(f).run()
        """
    def numerator(self):
        """
        Return the numerator of ``self``.

        OUTPUT: the numerator

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F.numerator()
            -e^y
        """
    def denominator(self):
        """
        Return the denominator of ``self``.

        OUTPUT:

        The denominator (i.e., the product of the factored denominator).

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F.denominator()
            x^3*y^2 + 2*x^3*y + x^2*y^2 + x^3 - 2*x^2*y - x*y^2 - 3*x^2 - 2*x*y
            - y^2 + 3*x + 2*y - 1
        """
    def denominator_factored(self):
        """
        Return the factorization in ``self.denominator_ring`` of the denominator of
        ``self`` but without the unit part.

        OUTPUT:

        The factored denominator as a list of tuple ``(f, m)``, where `f` is
        a factor and `m` its multiplicity.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F.denominator_factored()
            [(x - 1, 1), (x*y + x + y - 1, 2)]
        """
    @property
    def denominator_ring(self):
        """
        Return the ring of the denominator.

        OUTPUT: a ring

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F.denominator_ring
            Multivariate Polynomial Ring in x, y over Rational Field
            sage: F = FFPD(G/H)
            sage: F
            (e^y, [(x - 1, 1), (x*y + x + y - 1, 2)])
            sage: F.denominator_ring
            Multivariate Polynomial Ring in x, y over Rational Field
        """
    @property
    def numerator_ring(self):
        """
        Return the ring of the numerator.

        OUTPUT: a ring

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F.numerator_ring
            Symbolic Ring
            sage: F = FFPD(G/H)
            sage: F
            (e^y, [(x - 1, 1), (x*y + x + y - 1, 2)])
            sage: F.numerator_ring
            Symbolic Ring
        """
    def dimension(self):
        """
        Return the number of indeterminates of ``self.denominator_ring``.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F.dimension()
            2
        """
    def quotient(self):
        """
        Convert ``self`` into a quotient.

        OUTPUT: an element

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2*(1-x)
            sage: Hfac = H.factor()
            sage: G = exp(y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (-e^y, [(x - 1, 1), (x*y + x + y - 1, 2)])
            sage: F.quotient()
            -e^y/(x^3*y^2 + 2*x^3*y + x^2*y^2 + x^3 - 2*x^2*y - x*y^2 - 3*x^2 -
            2*x*y - y^2 + 3*x + 2*y - 1)
        """
    def univariate_decomposition(self):
        """
        Return the usual univariate partial fraction decomposition
        of ``self``.

        Assume that the numerator of ``self`` lies in the same univariate
        factorial polynomial ring as the factors of the denominator.

        Let `f = p/q` be a rational expression where `p` and `q` lie in a
        univariate factorial polynomial ring `R`.
        Let `q_1^{e_1} \\cdots q_n^{e_n}` be the
        unique factorization of `q` in `R` into irreducible factors.
        Then `f` can be written uniquely as:

        .. MATH::

            (*) \\quad p_0 + \\sum_{i=1}^{m} \\frac{p_i}{q_i^{e_i}},

        for some `p_j \\in R`.
        We call `(*)` the *usual partial fraction decomposition* of `f`.

        .. NOTE::

            This partial fraction decomposition can be computed using
            :meth:`~sage.symbolic.expression.Expression.partial_fraction` or
            :meth:`~sage.categories.quotient_fields.QuotientFields.ElementMethods.partial_fraction_decomposition`
            as well. However, here we use the already obtained/cached
            factorization of the denominator. This gives a speed up for
            non-small instances.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing

        One variable::

            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 5*x^3 + 1/x + 1/(x-1) + 1/(3*x^2 + 1)
            sage: f
            (5*x^7 - 5*x^6 + 5/3*x^5 - 5/3*x^4 + 2*x^3 - 2/3*x^2 + 1/3*x - 1/3)/(x^4 - x^3 + 1/3*x^2 - 1/3*x)
            sage: decomp = FFPD(f).univariate_decomposition()
            sage: decomp
            (5*x^3, []) +
            (1, [(x - 1, 1)]) +
            (1, [(x, 1)]) +
            (1/3, [(x^2 + 1/3, 1)])
            sage: decomp.sum().quotient() == f
            True

        One variable with numerator in symbolic ring::

            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: f = 5*x^3 + 1/x + 1/(x-1) + exp(x)/(3*x^2 + 1)
            sage: f
            (5*x^5 - 5*x^4 + 2*x - 1)/(x^2 - x) + e^x/(3*x^2 + 1)
            sage: decomp = FFPD(f).univariate_decomposition()
            sage: decomp
            (0, []) +
            (15/4*x^7 - 15/4*x^6 + 5/4*x^5 - 5/4*x^4 + 3/2*x^3 + 1/4*x^2*e^x -
             3/4*x^2 - 1/4*x*e^x + 1/2*x - 1/4, [(x - 1, 1)]) +
            (-15*x^7 + 15*x^6 - 5*x^5 + 5*x^4 - 6*x^3 -
             x^2*e^x + 3*x^2 + x*e^x - 2*x + 1, [(x, 1)]) +
            (1/4*(15*x^7 - 15*x^6 + 5*x^5 - 5*x^4 + 6*x^3 + x^2*e^x -
                  3*x^2 - x*e^x + 2*x - 1)*(3*x - 1), [(x^2 + 1/3, 1)])

        One variable over a finite field::

            sage: R.<x> = PolynomialRing(GF(2))
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 5*x^3 + 1/x + 1/(x-1) + 1/(3*x^2 + 1)
            sage: f
            (x^6 + x^4 + 1)/(x^3 + x)
            sage: decomp = FFPD(f).univariate_decomposition()
            sage: decomp
            (x^3, []) + (1, [(x, 1)]) + (x, [(x + 1, 2)])
            sage: decomp.sum().quotient() == f
            True

        One variable over an inexact field::

            sage: R.<x> = PolynomialRing(CC)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 5*x^3 + 1/x + 1/(x-1) + 1/(3*x^2 + 1)
            sage: f
            (5.00000000000000*x^7 - 5.00000000000000*x^6 + 1.66666666666667*x^5 - 1.66666666666667*x^4 + 2.00000000000000*x^3 - 0.666666666666667*x^2 + 0.333333333333333*x - 0.333333333333333)/(x^4 - x^3 + 0.333333333333333*x^2 - 0.333333333333333*x)
            sage: decomp = FFPD(f).univariate_decomposition()
            sage: decomp
            (5.00000000000000*x^3, []) +
            (1.00000000000000, [(x - 1.00000000000000, 1)]) +
            (-0.288675134594813*I, [(x - 0.577350269189626*I, 1)]) +
            (1.00000000000000, [(x, 1)]) +
            (0.288675134594813*I, [(x + 0.577350269189626*I, 1)])
            sage: decomp.sum().quotient() == f # Rounding error coming
            False

        TESTS::

            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: f = exp(x) / (x^2-x)
            sage: f
            e^x/(x^2 - x)
            sage: FFPD(f).univariate_decomposition()
            (0, []) + (e^x, [(x - 1, 1)]) + (-e^x, [(x, 1)])

        AUTHORS:

        - Robert Bradshaw (2007-05-31)
        - Alexander Raichev (2012-06-25)
        - Daniel Krenn (2014-12-01)
        """
    def nullstellensatz_certificate(self):
        """
        Return a Nullstellensatz certificate of ``self`` if it exists.

        Let `[(q_1, e_1), \\ldots, (q_n, e_n)]` be the denominator
        factorization of ``self``. The Nullstellensatz certificate is
        a list of polynomials `h_1, \\ldots, h_m` in ``self.denominator_ring``
        that satisfies `h_1 q_1 + \\cdots + h_m q_n = 1` if it exists.

        .. NOTE::

            Only works for multivariate base rings.

        OUTPUT:

        A list of polynomials or ``None`` if no Nullstellensatz
        certificate exists.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: G = sin(x)
            sage: H = x^2 * (x*y + 1)
            sage: f = FFPD(G, H.factor())
            sage: L = f.nullstellensatz_certificate()
            sage: L
            [y^2, -x*y + 1]
            sage: df = f.denominator_factored()
            sage: sum(L[i]*df[i][0]**df[i][1] for i in range(len(df))) == 1
            True

        ::

            sage: f = 1/(x*y)
            sage: L = FFPD(f).nullstellensatz_certificate()
            sage: L is None
            True
        """
    def nullstellensatz_decomposition(self):
        """
        Return a Nullstellensatz decomposition of ``self``.

        Let `f = p/q` where `q` lies in a `d` -variate polynomial ring
        `K[X]` for some field `K` and `d \\geq 1`.
        Let `q_1^{e_1} \\cdots q_n^{e_n}` be the
        unique factorization of `q` in `K[X]` into irreducible factors and
        let `V_i` be the algebraic variety `\\{x \\in L^d \\mid q_i(x) = 0\\}`
        of `q_i` over the algebraic closure `L` of `K`.
        By [Rai2012]_, `f` can be written as

        .. MATH::

            (*) \\quad \\sum_A \\frac{p_A}{\\prod_{i \\in A} q_i^{e_i}},

        where the `p_A` are products of `p` and elements in `K[X]` and
        the sum is taken over all subsets
        `A \\subseteq \\{1, \\ldots, m\\}` such that
        `\\bigcap_{i\\in A} T_i \\neq \\emptyset`.

        We call `(*)` a *Nullstellensatz decomposition* of `f`.
        Nullstellensatz decompositions are not unique.

        The algorithm used comes from [Rai2012]_.

        .. NOTE::

            Recursive. Only works for multivariate ``self``.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import *
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 1/(x*(x*y + 1))
            sage: decomp = FFPD(f).nullstellensatz_decomposition()
            sage: decomp
            (0, []) + (1, [(x, 1)]) + (-y, [(x*y + 1, 1)])
            sage: decomp.sum().quotient() == f
            True
            sage: [r.nullstellensatz_certificate() is None for r in decomp]
            [True, True, True]

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: G = sin(y)
            sage: H = x*(x*y + 1)
            sage: f = FFPD(G, H.factor())
            sage: decomp = f.nullstellensatz_decomposition()
            sage: decomp
            (0, []) + (sin(y), [(x, 1)]) + (-y*sin(y), [(x*y + 1, 1)])
            sage: bool(decomp.sum().quotient() == G/H)
            True
            sage: [r.nullstellensatz_certificate() is None for r in decomp]
            [True, True, True]
        """
    def algebraic_dependence_certificate(self):
        """
        Return the algebraic dependence certificate of ``self``.

        The algebraic dependence certificate is the ideal `J` of
        annihilating polynomials for the set of polynomials
        ``[q^e for (q, e) in self.denominator_factored()]``,
        which could be the zero ideal.
        The ideal `J` lies in a polynomial ring over the field
        ``self.denominator_ring.base_ring()`` that has
        ``m = len(self.denominator_factored())`` indeterminates.

        OUTPUT: an ideal

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 1/(x^2 * (x*y + 1) * y^3)
            sage: ff = FFPD(f)
            sage: J = ff.algebraic_dependence_certificate(); J
            Ideal (1 - 6*T2 + 15*T2^2 - 20*T2^3 + 15*T2^4 - T0^2*T1^3 -
             6*T2^5  + T2^6) of Multivariate Polynomial Ring in
             T0, T1, T2 over Rational Field
            sage: g = J.gens()[0]
            sage: df = ff.denominator_factored()
            sage: g(*(q**e for q, e in df)) == 0
            True

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: G = exp(x + y)
            sage: H = x^2 * (x*y + 1) * y^3
            sage: ff = FFPD(G, H.factor())
            sage: J = ff.algebraic_dependence_certificate(); J
            Ideal (1 - 6*T2 + 15*T2^2 - 20*T2^3 + 15*T2^4 - T0^2*T1^3 -
            6*T2^5 + T2^6) of Multivariate Polynomial Ring in
            T0, T1, T2 over Rational Field
            sage: g = J.gens()[0]
            sage: df = ff.denominator_factored()
            sage: g(*(q**e for q, e in df)) == 0
            True

        ::

            sage: f = 1/(x^3 * y^2)
            sage: J = FFPD(f).algebraic_dependence_certificate()
            sage: J
            Ideal (0) of Multivariate Polynomial Ring in T0, T1 over Rational Field

        ::

            sage: f = sin(1)/(x^3 * y^2)
            sage: J = FFPD(f).algebraic_dependence_certificate()
            sage: J
            Ideal (0) of Multivariate Polynomial Ring in T0, T1 over Rational Field
        """
    def algebraic_dependence_decomposition(self, whole_and_parts: bool = True):
        """
        Return an algebraic dependence decomposition of ``self``.

        Let `f = p/q` where `q` lies in a `d`-variate polynomial ring
        `K[X]` for some field `K`.
        Let `q_1^{e_1} \\cdots q_n^{e_n}` be the
        unique factorization of `q` in `K[X]` into irreducible factors and
        let `V_i` be the algebraic variety `\\{x \\in L^d \\mid q_i(x) = 0\\}`
        of `q_i` over the algebraic closure `L` of `K`.
        By [Rai2012]_, `f` can be written as

        .. MATH::

            (*) \\quad \\sum_A \\frac{p_A}{\\prod_{i \\in A} q_i^{b_i}},

        where the `b_i` are positive integers, each `p_A` is a products
        of `p` and an element in `K[X]`,
        and the sum is taken over all subsets
        `A \\subseteq \\{1, \\ldots, m\\}` such that `|A| \\leq d` and
        `\\{q_i \\mid i \\in A\\}` is algebraically independent.

        We call `(*)` an *algebraic dependence decomposition* of `f`.
        Algebraic dependence decompositions are not unique.

        The algorithm used comes from [Rai2012]_.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 1/(x^2 * (x*y + 1) * y^3)
            sage: ff = FFPD(f)
            sage: decomp = ff.algebraic_dependence_decomposition()
            sage: decomp
            (0, []) + (-x, [(x*y + 1, 1)]) +
            (x^2*y^2 - x*y + 1, [(y, 3), (x, 2)])
            sage: decomp.sum().quotient() == f
            True
            sage: for r in decomp:
            ....:     J = r.algebraic_dependence_certificate()
            ....:     J is None or J == J.ring().ideal()  # The zero ideal
            True
            True
            True

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: G = sin(x)
            sage: H = x^2 * (x*y + 1) * y^3
            sage: f = FFPD(G, H.factor())
            sage: decomp = f.algebraic_dependence_decomposition()
            sage: decomp
            (0, []) + (x^4*y^3*sin(x), [(x*y + 1, 1)]) +
            (-(x^5*y^5 - x^4*y^4 + x^3*y^3 - x^2*y^2 + x*y - 1)*sin(x),
             [(y, 3), (x, 2)])
            sage: bool(decomp.sum().quotient() == G/H)
            True
            sage: for r in decomp:
            ....:     J = r.algebraic_dependence_certificate()
            ....:     J is None or J == J.ring().ideal()
            True
            True
            True
        """
    def leinartas_decomposition(self):
        """
        Return a Leinartas decomposition of ``self``.

        Let `f = p/q` where `q` lies in a `d` -variate polynomial
        ring `K[X]` for some field `K`.
        Let `q_1^{e_1} \\cdots q_n^{e_n}` be the
        unique factorization of `q` in `K[X]` into irreducible factors and
        let `V_i` be the algebraic variety
        `\\{x\\in L^d \\mid q_i(x) = 0\\}` of `q_i` over the algebraic closure
        `L` of `K`. By [Rai2012]_, `f` can be written as

        .. MATH::

            (*) \\quad \\sum_A \\frac{p_A}{\\prod_{i \\in A} q_i^{b_i}},

        where the `b_i` are positive integers, each `p_A` is a product of
        `p` and an element of `K[X]`, and the sum is taken over all
        subsets `A \\subseteq \\{1, \\ldots, m\\}` such that

        1. `|A| \\le d`,
        2. `\\bigcap_{i\\in A} T_i \\neq \\emptyset`, and
        3. `\\{q_i \\mid i\\in A\\}` is algebraically independent.

        In particular, any rational expression in `d` variables
        can be represented as a sum of rational expressions
        whose denominators each contain at most `d` distinct irreducible
        factors.

        We call `(*)` a *Leinartas decomposition* of `f`.
        Leinartas decompositions are not unique.

        The algorithm used comes from [Rai2012]_.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = (x^2 + 1)/((x + 2)*(x - 1)*(x^2 + x + 1))
            sage: decomp = FFPD(f).leinartas_decomposition()
            sage: decomp
            (0, []) + (2/9, [(x - 1, 1)]) +
            (-5/9, [(x + 2, 1)]) + (1/3*x, [(x^2 + x + 1, 1)])
            sage: decomp.sum().quotient() == f
            True

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 1/x + 1/y + 1/(x*y + 1)
            sage: decomp = FFPD(f).leinartas_decomposition()
            sage: decomp
            (0, []) + (1, [(x*y + 1, 1)]) + (x + y, [(y, 1), (x, 1)])
            sage: decomp.sum().quotient() == f
            True
            sage: def check_decomp(r):
            ....:     L = r.nullstellensatz_certificate()
            ....:     J = r.algebraic_dependence_certificate()
            ....:     return L is None and (J is None or J == J.ring().ideal())
            sage: all(check_decomp(r) for r in decomp)
            True

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: f = sin(x)/x + 1/y + 1/(x*y + 1)
            sage: G = f.numerator()
            sage: H = R(f.denominator())
            sage: ff = FFPD(G, H.factor())
            sage: decomp = ff.leinartas_decomposition()
            sage: decomp  # random - non canonical depends on singular version
            (0, []) +
            (-(x*y^2*sin(x) + x^2*y + x*y + y*sin(x) + x)*y, [(y, 1)]) +
            ((x*y^2*sin(x) + x^2*y + x*y + y*sin(x) + x)*x*y, [(x*y + 1, 1)]) +
            (x*y^2*sin(x) + x^2*y + x*y + y*sin(x) + x, [(y, 1), (x, 1)])
            sage: bool(decomp.sum().quotient() == f)
            True
            sage: all(check_decomp(r) for r in decomp)
            True

        ::

            sage: R.<x,y,z>= PolynomialRing(GF(2, 'a'))
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 1/(x * y * z * (x*y + z))
            sage: decomp = FFPD(f).leinartas_decomposition()
            sage: decomp
            (0, []) + (1, [(z, 2), (x*y + z, 1)]) +
            (1, [(z, 2), (y, 1), (x, 1)])
            sage: decomp.sum().quotient() == f
            True
        """
    def cohomology_decomposition(self):
        """
        Return the cohomology decomposition of ``self``.

        Let `p / (q_1^{e_1} \\cdots q_n^{e_n})` be the fraction represented
        by ``self`` and let `K[x_1, \\ldots, x_d]` be the polynomial ring
        in which the `q_i` lie.
        Assume that `n \\leq d` and that the gradients of the `q_i` are linearly
        independent at all points in the intersection
        `V_1 \\cap \\ldots \\cap V_n` of the algebraic varieties
        `V_i = \\{x \\in L^d \\mid q_i(x) = 0 \\}`, where `L` is the algebraic
        closure of the field `K`.
        Return a :class:`FractionWithFactoredDenominatorSum`
        `f` such that the differential form
        `f dx_1 \\wedge \\cdots \\wedge dx_d` is de Rham cohomologous to the
        differential form
        `p / (q_1^{e_1} \\cdots q_n^{e_n}) dx_1 \\wedge \\cdots \\wedge dx_d`
        and such that the denominator of each summand of `f` contains
        no repeated irreducible factors.

        The algorithm used here comes from the proof of Theorem 17.4 of
        [AY1983]_.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = 1/(x^2 + x + 1)^3
            sage: decomp = FFPD(f).cohomology_decomposition()
            sage: decomp
            (0, []) + (2/3, [(x^2 + x + 1, 1)])

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: FFPD(1, [(x, 1), (y, 2)]).cohomology_decomposition()
            (0, [])

        The following example was fixed in :issue:`29465`::

            sage: p = 1
            sage: qs = [(x*y - 1, 1), (x**2 + y**2 - 1, 2)]
            sage: f = FFPD(p, qs)
            sage: f.cohomology_decomposition()
            (0, []) + (-4/3*x*y, [(x^2 + y^2 - 1, 1)]) +
            (1/3, [(x*y - 1, 1), (x^2 + y^2 - 1, 1)])
        """
    def asymptotic_decomposition(self, alpha, asy_var=None):
        """
        Return the asymptotic decomposition of ``self``.

        The asymptotic decomposition of `F` is a sum that has the
        same asymptotic expansion as `f` in the direction ``alpha``
        but each summand has a denominator factorization of the form
        `[(q_1, 1), \\ldots, (q_n, 1)]`, where `n` is at most the
        :meth:`dimension` of `F`.

        INPUT:

        - ``alpha`` -- a `d`-tuple of positive integers or symbolic variables
        - ``asy_var`` -- (default: ``None``) a symbolic variable with
          respect to which to compute asymptotics;
          if ``None`` is given, we set ``asy_var = var('r')``

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        The output results from a Leinartas decomposition followed by a
        cohomology decomposition.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: f = (x^2 + 1)/((x - 1)^3*(x + 2))
            sage: F = FFPD(f)
            sage: alpha = [var('a')]
            sage: F.asymptotic_decomposition(alpha)
            (0, []) +
            (1/54*(5*a^2 + 2*a^2/x + 11*a^2/x^2)*r^2
             - 1/54*(5*a - 2*a/x - 33*a/x^2)*r + 11/27/x^2,
            [(x - 1, 1)]) + (-5/27, [(x + 2, 1)])

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - 2*x -y)*(1 - x -2*y)**2
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = var('a, b')
            sage: F.asymptotic_decomposition(alpha)
            (0, []) +
            (-1/3*r*(a/x - 2*b/y) - 1/3/x + 2/3/y,
             [(x + 2*y - 1, 1), (2*x + y - 1, 1)])
        """
    def asymptotics(self, p, alpha, N, asy_var=None, numerical: int = 0, verbose: bool = False):
        """
        Return the asymptotics in the given direction.

        This function returns the first `N` terms (some of which could be
        zero) of the asymptotic expansion of the Maclaurin ray coefficients
        `F_{r \\alpha}` of the function `F` represented by ``self`` as
        `r \\to \\infty`, where `r` is ``asy_var`` and ``alpha`` is a tuple
        of positive integers of length `d` which is ``self.dimension()``.
        Assume that

        - `F` is holomorphic in a neighborhood of the origin;
        - the unique factorization of the denominator `H` of `F` in the local
          algebraic ring at `p` equals its unique factorization in the local
          analytic ring at `p`;
        - the unique factorization of `H` in the local algebraic ring at `p`
          has at most ``d`` irreducible factors, none of which are repeated
          (one can reduce to this case via :meth:`asymptotic_decomposition()`);
        - `p` is a convenient strictly minimal smooth or multiple point
          with all nonzero coordinates that is critical and nondegenerate
          for ``alpha``.

        The algorithms used here come from [RW2008]_ and [RW2012]_.

        INPUT:

        - ``p`` -- dictionary with keys that can be coerced to equal
          ``self.denominator_ring.gens()``
        - ``alpha`` -- tuple of length ``self.dimension()`` of positive
          integers or, if `p` is a smooth point, possibly of symbolic variables
        - ``N`` -- positive integer
        - ``asy_var`` -- (default: ``None``) a symbolic variable for the
          asymptotic expansion; if ``none`` is given, then ``var('r')`` will be
          assigned
        - ``numerical`` -- (default: 0) a natural number; if ``numerical`` is
          greater than 0, then return a numerical approximation of
          `F_{r \\alpha}` with ``numerical`` digits of precision; otherwise
          return exact values
        - ``verbose`` -- boolean (default: ``False``); print the current state of
          the algorithm

        OUTPUT:

        The tuple ``(asy, exp_scale, subexp_part)``.
        Here ``asy`` is the sum of the first `N` terms (some of which might
        be 0) of the asymptotic expansion of `F_{r\\alpha}` as `r \\to \\infty`;
        ``exp_scale**r`` is the exponential factor of ``asy``;
        ``subexp_part`` is the subexponential factor of ``asy``.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing

        A smooth point example::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - x - y - x*y)**2
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac); print(F)
            (1, [(x*y + x + y - 1, 2)])
            sage: alpha = [4, 3]
            sage: decomp = F.asymptotic_decomposition(alpha); decomp
            (0, []) + (... - 1/2, [(x*y + x + y - 1, 1)])
            sage: F1 = decomp[1]
            sage: p = {y: 1/3, x: 1/2}
            sage: asy = F1.asymptotics(p, alpha, 2, verbose=True)
            Creating auxiliary functions...
            Computing derivatives of auxiliary functions...
            Computing derivatives of more auxiliary functions...
            Computing second order differential operator actions...
            sage: asy
            (1/6000*(3600*sqrt(5)*sqrt(3)*sqrt(2)*sqrt(r)/sqrt(pi)
              + 463*sqrt(5)*sqrt(3)*sqrt(2)/(sqrt(pi)*sqrt(r)))*432^r,
             432,
             3/5*sqrt(5)*sqrt(3)*sqrt(2)*sqrt(r)/sqrt(pi)
              + 463/6000*sqrt(5)*sqrt(3)*sqrt(2)/(sqrt(pi)*sqrt(r)))
            sage: F.relative_error(asy[0], alpha, [1, 2, 4, 8, 16], asy[1])  # abs tol 1e-10  # long time
            [((4, 3), 2.083333333, [2.092576110], [-0.004436533009]),
             ((8, 6), 2.787374614, [2.790732875], [-0.001204811281]),
             ((16, 12), 3.826259447, [3.827462310], [-0.0003143703383]),
             ((32, 24), 5.328112821, [5.328540787], [-0.00008032230388]),
             ((64, 48), 7.475927885, [7.476079664], [-0.00002030232879])]

        A multiple point example::

            sage: R.<x,y,z>= PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (4 - 2*x - y - z)**2*(4 - x - 2*y - z)
            sage: Hfac = H.factor()
            sage: G = 16/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (-16, [(x + 2*y + z - 4, 1), (2*x + y + z - 4, 2)])
            sage: alpha = [3, 3, 2]
            sage: decomp = F.asymptotic_decomposition(alpha); decomp
            (0, []) + (..., [(x + 2*y + z - 4, 1), (2*x + y + z - 4, 1)])
            sage: F1 = decomp[1]
            sage: p = {x: 1, y: 1, z: 1}
            sage: asy = F1.asymptotics(p, alpha, 2, verbose=True) # long time
            Creating auxiliary functions...
            Computing derivatives of auxiliary functions...
            Computing derivatives of more auxiliary functions...
            Computing second-order differential operator actions...
            sage: asy # long time
            (4/3*sqrt(3)*sqrt(r)/sqrt(pi) + 47/216*sqrt(3)/(sqrt(pi)*sqrt(r)),
             1, 4/3*sqrt(3)*sqrt(r)/sqrt(pi) + 47/216*sqrt(3)/(sqrt(pi)*sqrt(r)))
            sage: F.relative_error(asy[0], alpha, [1, 2, 4, 8], asy[1]) # long time
            [((3, 3, 2), 0.9812164307, [1.515572606], [-0.54458543...]),
             ((6, 6, 4), 1.576181132, [1.992989399], [-0.26444185...]),
             ((12, 12, 8), 2.485286378, [2.712196351], [-0.091301338...]),
             ((24, 24, 16), 3.700576827, [3.760447895], [-0.016178847...])]
        """
    def asymptotics_smooth(self, p, alpha, N, asy_var, coordinate=None, numerical: int = 0, verbose: bool = False):
        """
        Return the asymptotics in the given direction of a smooth point.

        This is the same as :meth:`asymptotics()`, but only in the
        case of a convenient smooth point.

        The formulas used for computing the asymptotic expansions are
        Theorems 3.2 and 3.3 [RW2008]_ with the exponent of `H`
        equal to 1. Theorem 3.2 is a specialization of Theorem 3.4
        of [RW2012]_ with `n = 1`.

        INPUT:

        - ``p`` -- dictionary with keys that can be coerced to equal
          ``self.denominator_ring.gens()``
        - ``alpha`` -- tuple of length ``d = self.dimension()`` of positive
          integers or, if `p` is a smooth point, possibly of symbolic variables
        - ``N`` -- positive integer
        - ``asy_var`` -- (default: ``None``) a symbolic variable; the variable
          of the asymptotic expansion, if none is given, ``var('r')`` will be
          assigned
        - ``coordinate`` -- (default: ``None``) an integer in
          `\\{0, \\ldots, d-1\\}` indicating a convenient coordinate to base the
          asymptotic calculations on; if ``None`` is assigned, then choose
          ``coordinate=d-1``
        - ``numerical`` -- (default: 0) a natural number; if numerical is
          greater than 0, then return a numerical approximation of the
          Maclaurin ray coefficients of ``self`` with ``numerical`` digits of
          precision; otherwise return exact values
        - ``verbose`` -- boolean (default: ``False``); print the current state
          of the algorithm

        OUTPUT: the asymptotic expansion

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = 2 - 3*x
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (-1/3, [(x - 2/3, 1)])
            sage: alpha = [2]
            sage: p = {x: 2/3}
            sage: asy = F.asymptotics_smooth(p, alpha, 3, asy_var=var('r'))
            sage: asy
            (1/2*(9/4)^r, 9/4, 1/2)

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = 1-x-y-x*y
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = [3, 2]
            sage: p = {y: 1/2*sqrt(13) - 3/2, x: 1/3*sqrt(13) - 2/3}
            sage: F.asymptotics_smooth(p, alpha, 2, var('r'), numerical=3, verbose=True)
            Creating auxiliary functions...
            Computing derivatives of auxiliary functions...
            Computing derivatives of more auxiliary functions...
            Computing second order differential operator actions...
            (71.2^r*(0.369/sqrt(r) - 0.018.../r^(3/2)), 71.2, 0.369/sqrt(r) - 0.018.../r^(3/2))

            sage: q = 1/2
            sage: qq = q.denominator()
            sage: H = 1 - q*x + q*x*y - x^2*y
            sage: Hfac = H.factor()
            sage: G = (1 - q*x)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = list(qq*vector([2, 1 - q]))
            sage: alpha
            [4, 1]
            sage: p = {x: 1, y: 1}
            sage: F.asymptotics_smooth(p, alpha, 5, var('r'), verbose=True) # not tested (140 seconds)
            Creating auxiliary functions...
            Computing derivatives of auxiliary functions...
            Computing derivatives of more auxiliary functions...
            Computing second order differential operator actions...
            (1/12*sqrt(3)*2^(2/3)*gamma(1/3)/(pi*r^(1/3))
              - 1/96*sqrt(3)*2^(1/3)*gamma(2/3)/(pi*r^(5/3)),
             1,
             1/12*sqrt(3)*2^(2/3)*gamma(1/3)/(pi*r^(1/3))
              - 1/96*sqrt(3)*2^(1/3)*gamma(2/3)/(pi*r^(5/3)))
        """
    def asymptotics_multiple(self, p, alpha, N, asy_var, coordinate=None, numerical: int = 0, verbose: bool = False):
        """
        Return the asymptotics in the given direction of a multiple
        point nondegenerate for ``alpha``.

        This is the same as :meth:`asymptotics`, but only in the case
        of a convenient multiple point nondegenerate for ``alpha``.
        Assume also that ``self.dimension >= 2`` and that the
        ``p.values()`` are not symbolic variables.

        The formulas used for computing the asymptotic expansion are
        Theorem 3.4 and Theorem 3.7 of [RW2012]_.

        INPUT:

        - ``p`` -- dictionary with keys that can be coerced to equal
          ``self.denominator_ring.gens()``
        - ``alpha`` -- tuple of length ``d = self.dimension()`` of positive
          integers or, if `p` is a smooth point, possibly of symbolic variables
        - ``N`` -- positive integer
        - ``asy_var`` -- (default: ``None``) a symbolic variable; the variable
          of the asymptotic expansion, if none is given, ``var('r')`` will be
          assigned
        - ``coordinate`` -- (default: ``None``) an integer in
          `\\{0, \\ldots, d-1\\}` indicating a convenient coordinate to base the
          asymptotic calculations on; if ``None`` is assigned, then choose
          ``coordinate=d-1``
        - ``numerical`` -- (default: 0) a natural number; if numerical is
          greater than 0, then return a numerical approximation of the
          Maclaurin ray coefficients of ``self`` with ``numerical`` digits of
          precision. Otherwise return exact values.
        - ``verbose`` -- boolean (default: ``False``); print the current state of
          the algorithm

        OUTPUT: the asymptotic expansion

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y,z>= PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = (4 - 2*x - y - z)*(4 - x -2*y - z)
            sage: Hfac = H.factor()
            sage: G = 16/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (16, [(x + 2*y + z - 4, 1), (2*x + y + z - 4, 1)])
            sage: p = {x: 1, y: 1, z: 1}
            sage: alpha = [3, 3, 2]
            sage: F.asymptotics_multiple(p, alpha, 2, var('r'), verbose=True) # long time
            Creating auxiliary functions...
            Computing derivatives of auxiliary functions...
            Computing derivatives of more auxiliary functions...
            Computing second-order differential operator actions...
            (4/3*sqrt(3)/(sqrt(pi)*sqrt(r)) - 25/216*sqrt(3)/(sqrt(pi)*r^(3/2)),
             1,
             4/3*sqrt(3)/(sqrt(pi)*sqrt(r)) - 25/216*sqrt(3)/(sqrt(pi)*r^(3/2)))

            sage: H = (1 - x*(1 + y))*(1 - z*x**2*(1 + 2*y))
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (1, [(x*y + x - 1, 1), (2*x^2*y*z + x^2*z - 1, 1)])
            sage: p = {x: 1/2, z: 4/3, y: 1}
            sage: alpha = [8, 3, 3]
            sage: F.asymptotics_multiple(p, alpha, 2, var('r'), coordinate=1, verbose=True) # long time
            Creating auxiliary functions...
            Computing derivatives of auxiliary functions...
            Computing derivatives of more auxiliary functions...
            Computing second-order differential operator actions...
            (1/172872*108^r*(24696*sqrt(7)*sqrt(3)/(sqrt(pi)*sqrt(r))
              - 1231*sqrt(7)*sqrt(3)/(sqrt(pi)*r^(3/2))),
             108,
             1/7*sqrt(7)*sqrt(3)/(sqrt(pi)*sqrt(r))
              - 1231/172872*sqrt(7)*sqrt(3)/(sqrt(pi)*r^(3/2)))

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: H = (1 - 2*x - y) * (1 - x - 2*y)
            sage: Hfac = H.factor()
            sage: G = exp(x + y)/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (e^(x + y), [(x + 2*y - 1, 1), (2*x + y - 1, 1)])
            sage: p = {x: 1/3, y: 1/3}
            sage: alpha = (var('a'), var('b'))
            sage: F.asymptotics_multiple(p, alpha, 2, var('r')) # long time
            (3*(1/((1/3)^a*(1/3)^b))^r*e^(2/3), 1/((1/3)^a*(1/3)^b), 3*e^(2/3))
        """
    def grads(self, p):
        """
        Return a list of the gradients of the polynomials
        ``[q for (q, e) in self.denominator_factored()]`` evaluated at ``p``.

        INPUT:

        - ``p`` -- (default: ``None``) a dictionary whose keys are
          the generators of ``self.denominator_ring``

        OUTPUT: list

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: p = exp(x)
            sage: df = [(x^3 + 3*y^2, 5), (x*y, 2), (y, 1)]
            sage: f = FFPD(p, df)
            sage: f
            (e^x, [(y, 1), (x*y, 2), (x^3 + 3*y^2, 5)])
            sage: R.gens()
            (x, y)
            sage: p = None
            sage: f.grads(p)
            [(0, 1), (y, x), (3*x^2, 6*y)]

            sage: p = {x: sqrt(2), y: var('a')}
            sage: f.grads(p)
            [(0, 1), (a, sqrt(2)), (6, 6*a)]
        """
    def log_grads(self, p):
        """
        Return a list of the logarithmic gradients of the polynomials
        ``[q for (q, e) in self.denominator_factored()]`` evaluated at ``p``.

        The logarithmic gradient of a function `f` at point `p` is the
        vector `(x_1 \\partial_1 f(x), \\ldots, x_d \\partial_d f(x) )`
        evaluated at `p`.

        INPUT:

        - ``p`` -- (default: ``None``) a dictionary whose keys
          are the generators of ``self.denominator_ring``

        OUTPUT: list

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: p = exp(x)
            sage: df = [(x^3 + 3*y^2, 5), (x*y, 2), (y, 1)]
            sage: f = FFPD(p, df)
            sage: f
            (e^x, [(y, 1), (x*y, 2), (x^3 + 3*y^2, 5)])
            sage: R.gens()
            (x, y)
            sage: p = None
            sage: f.log_grads(p)
            [(0, y), (x*y, x*y), (3*x^3, 6*y^2)]

            sage: p = {x: sqrt(2), y: var('a')}
            sage: f.log_grads(p)
            [(0, a), (sqrt(2)*a, sqrt(2)*a), (6*sqrt(2), 6*a^2)]
        """
    def critical_cone(self, p, coordinate=None):
        """
        Return the critical cone of the convenient multiple point ``p``.

        INPUT:

        - ``p`` -- dictionary with keys that can be coerced to equal
          ``self.denominator_ring.gens()`` and values in a field
        - ``coordinate`` -- (default: ``None``) a natural number

        OUTPUT: list of vectors

        This list of vectors generate the critical cone of ``p`` and
        the cone itself, which is ``None`` if the values of ``p`` don't lie in
        `\\QQ`. Divide logarithmic gradients by their component ``coordinate``
        entries. If ``coordinate = None``, then search from `d-1` down to 0
        for the first index ``j`` such that for all ``i`` we have
        ``self.log_grads()[i][j] != 0`` and set ``coordinate = j``.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: G = 1
            sage: H = (1 - x*(1 + y)) * (1 - z*x**2*(1 + 2*y))
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: p = {x: 1/2, y: 1, z: 4/3}
            sage: F.critical_cone(p)
            ([(2, 1, 0), (3, 1, 3/2)], 2-d cone in 3-d lattice N)
        """
    def is_convenient_multiple_point(self, p):
        """
        Test if ``p`` is a convenient multiple point of ``self``.

        In case ``p`` is a convenient multiple point, ``verdict = True`` and
        ``comment`` is a string stating which variables it's convenient to use.
        In case ``p`` is not, ``verdict = False`` and ``comment`` is a string
        explaining why ``p`` fails to be a convenient multiple point.

        See [RW2012]_ for more details.

        INPUT:

        - ``p`` -- dictionary with keys that can be coerced to equal
          ``self.denominator_ring.gens()``

        OUTPUT:

        A pair ``(verdict, comment)``.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = (1 - x*(1 + y)) * (1 - z*x**2*(1 + 2*y))
            sage: df = H.factor()
            sage: G = 1 / df.unit()
            sage: F = FFPD(G, df)
            sage: p1 = {x: 1/2, y: 1, z: 4/3}
            sage: p2 = {x: 1, y: 2, z: 1/2}
            sage: F.is_convenient_multiple_point(p1)
            (True, 'convenient in variables [x, y]')
            sage: F.is_convenient_multiple_point(p2)
            (False, 'not a singular point')
        """
    def singular_ideal(self):
        """
        Return the singular ideal of ``self``.

        Let `R` be the ring of ``self`` and `H` its denominator.
        Let `H_{red}` be the reduction (square-free part) of `H`.
        Return the ideal in `R` generated by `H_{red}` and
        its partial derivatives.
        If the coefficient field of `R` is algebraically closed,
        then the output is the ideal of the singular locus (which
        is a variety) of the variety of `H`.

        OUTPUT: an ideal

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = (1 - x*(1 + y))^3 * (1 - z*x**2*(1 + 2*y))
            sage: df = H.factor()
            sage: G = 1 / df.unit()
            sage: F = FFPD(G, df)
            sage: F.singular_ideal()
            Ideal (x*y + x - 1, y^2 - 2*y*z + 2*y - z + 1, x*z + y - 2*z + 1) of
             Multivariate Polynomial Ring in x, y, z over Rational Field
        """
    def smooth_critical_ideal(self, alpha):
        """
        Return the smooth critical ideal of ``self``.

        Let `R` be the ring of ``self`` and `H` its denominator.
        Return the ideal in `R` of smooth critical points of the variety
        of `H` for the direction ``alpha``.
        If the variety `V` of `H` has no smooth points, then return the ideal
        in `R` of `V`.

        See [RW2012]_ for more details.

        INPUT:

        - ``alpha`` -- tuple of positive integers and/or symbolic entries
          of length ``self.denominator_ring.ngens()``

        OUTPUT: an ideal

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = (1 - x - y - x*y)^2
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = var('a1, a2')
            sage: F.smooth_critical_ideal(alpha)
            Ideal (y^2 + (2*a1)/a2*y - 1, x + (-a2)/a1*y + (-a1 + a2)/a1) of
             Multivariate Polynomial Ring in x, y over Fraction Field of
             Multivariate Polynomial Ring in a1, a2 over Rational Field

            sage: H = (1-x-y-x*y)^2
            sage: Hfac = H.factor()
            sage: G = 1/Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = [7/3, var('a')]
            sage: F.smooth_critical_ideal(alpha)
            Ideal (y^2 + 14/(3*a)*y - 1, x + (-3*a)/7*y + (3*a - 7)/7) of Multivariate Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in a over Rational Field
        """
    def maclaurin_coefficients(self, multi_indices, numerical: int = 0):
        """
        Return the Maclaurin coefficients of ``self`` with given
        ``multi_indices``.

        INPUT:

        - ``multi_indices`` -- list of tuples of positive integers, where
          each tuple has length ``self.dimension()``
        - ``numerical`` -- (default: 0) a natural number; if positive, return
          numerical approximations of coefficients with ``numerical`` digits of
          accuracy

        OUTPUT:

        A dictionary whose value of the key ``nu`` are the Maclaurin
        coefficient of index ``nu`` of ``self``.

        .. NOTE::

            Uses iterated univariate Maclaurin expansions. Slow.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = 2 - 3*x
            sage: Hfac = H.factor()
            sage: G = 1 / Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: F
            (-1/3, [(x - 2/3, 1)])
            sage: F.maclaurin_coefficients([(2*k,) for k in range(6)])
            {(0,): 1/2,
             (2,): 9/8,
             (4,): 81/32,
             (6,): 729/128,
             (8,): 6561/512,
             (10,): 59049/2048}

        ::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = (4 - 2*x - y - z) * (4 - x - 2*y - z)
            sage: Hfac = H.factor()
            sage: G = 16 / Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = vector([3, 3, 2])
            sage: interval = [1, 2, 4]
            sage: S = [r*alpha for r in interval]
            sage: F.maclaurin_coefficients(S, numerical=10)  # long time
            {(3, 3, 2): 0.7849731445,
             (6, 6, 4): 0.7005249476,
             (12, 12, 8): 0.5847732654}
        """
    def relative_error(self, approx, alpha, interval, exp_scale=..., digits: int = 10):
        """
        Return the relative error between the values of the Maclaurin
        coefficients of ``self`` with multi-indices ``r alpha`` for ``r`` in
        ``interval`` and the values of the functions (of the variable ``r``)
        in ``approx``.

        INPUT:

        - ``approx`` -- an individual or list of symbolic expressions in
          one variable
        - ``alpha`` -- list of positive integers of length
          ``self.denominator_ring.ngens()``
        - ``interval`` -- list of positive integers
        - ``exp_scale`` -- (default: 1) a number

        OUTPUT: list of tuples with properties described below

        This outputs a list whose entries are a tuple
        ``(r*alpha, a_r, b_r, err_r)`` for ``r`` in ``interval``.
        Here ``r*alpha`` is a tuple; ``a_r`` is the ``r*alpha`` (multi-index)
        coefficient of the Maclaurin series for ``self`` divided by
        ``exp_scale**r``;
        ``b_r`` is a list of the values of the functions in ``approx``
        evaluated at ``r`` and divided by ``exp_scale**m``;
        ``err_r`` is the list of relative errors
        ``(a_r - f)/a_r`` for ``f`` in ``b_r``.
        All outputs are decimal approximations.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: H = 1 - x - y - x*y
            sage: Hfac = H.factor()
            sage: G = 1 / Hfac.unit()
            sage: F = FFPD(G, Hfac)
            sage: alpha = [1, 1]
            sage: r = var('r')
            sage: a1 = (0.573/sqrt(r))*5.83^r
            sage: a2 = (0.573/sqrt(r) - 0.0674/r^(3/2))*5.83^r
            sage: es = 5.83
            sage: F.relative_error([a1, a2], alpha, [1, 2, 4, 8], es) # long time
            [((1, 1), 0.5145797599,
              [0.5730000000, 0.5056000000], [-0.1135300000, 0.01745066667]),
             ((2, 2), 0.3824778089,
              [0.4051721856, 0.3813426871], [-0.05933514614, 0.002967810973]),
             ((4, 4), 0.2778630595,
              [0.2865000000, 0.2780750000], [-0.03108344267, -0.0007627515584]),
             ((8, 8), 0.1991088276,
              [0.2025860928, 0.1996074055], [-0.01746414394, -0.002504047242])]
        """

class FractionWithFactoredDenominatorRing(UniqueRepresentation, Parent):
    """
    This is the ring of fractions with factored denominator.

    INPUT:

    - ``denominator_ring`` -- the base ring (a polynomial ring)

    - ``numerator_ring`` -- (optional) the numerator ring; the default is
      the ``denominator_ring``

    - ``category`` -- (default: :class:`Rings`) the category

    .. SEEALSO::

        :class:`FractionWithFactoredDenominator`,
        :mod:`~sage.rings.asymptotic.asymptotics_multivariate_generating_functions`

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
        sage: R.<x,y> = PolynomialRing(QQ)
        sage: FFPD = FractionWithFactoredDenominatorRing(R)
        sage: df = [x, 1], [y, 1], [x*y+1, 1]
        sage: f = FFPD(x, df)  # indirect doctest
        sage: f
        (1, [(y, 1), (x*y + 1, 1)])

    AUTHORS:

    - Daniel Krenn (2014-12-01)
    """
    @staticmethod
    def __classcall_private__(cls, denominator_ring, numerator_ring=None, category=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD1 = FractionWithFactoredDenominatorRing(R)
            sage: cat = Rings().Commutative()
            sage: FFPD2 = FractionWithFactoredDenominatorRing(R, R, cat)
            sage: FFPD1 is FFPD2
            True
        """
    def __init__(self, denominator_ring, numerator_ring=None, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: P.<X, Y> = ZZ[]
            sage: FractionWithFactoredDenominatorRing(P)
            Ring of fractions with factored denominator
            over Multivariate Polynomial Ring in X, Y over Integer Ring
        """
    def base_ring(self):
        """
        Return the base ring.

        OUTPUT: a ring

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing
            sage: P.<X, Y> = ZZ[]
            sage: F = FractionWithFactoredDenominatorRing(P); F
            Ring of fractions with factored denominator
            over Multivariate Polynomial Ring in X, Y over Integer Ring
            sage: F.base_ring()
            Integer Ring
            sage: F.base()
            Multivariate Polynomial Ring in X, Y over Integer Ring
        """
    Element = FractionWithFactoredDenominator

class FractionWithFactoredDenominatorSum(list):
    """
    A list representing the sum of :class:`FractionWithFactoredDenominator`
    objects with distinct denominator factorizations.

    AUTHORS:

    - Alexander Raichev (2012-06-25)

    - Daniel Krenn (2014-12-01)
    """
    def __eq__(self, other) -> bool:
        """
        Return ``True`` if ``self`` is equal to ``other``.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing, FractionWithFactoredDenominatorSum
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = FFPD(x + y, [(y, 1), (x, 1)])
            sage: g = FFPD(x*(x + y), [(y, 1), (x, 2)])
            sage: s = FractionWithFactoredDenominatorSum([f]); s
            (x + y, [(y, 1), (x, 1)])
            sage: t = FractionWithFactoredDenominatorSum([g]); t
            (x + y, [(y, 1), (x, 1)])
            sage: s == t
            True
        """
    def __ne__(self, other) -> bool:
        """
        Return ``True`` if ``self`` is not equal to ``other``.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing, FractionWithFactoredDenominatorSum
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = FFPD(x + y, [(y, 1), (x, 1)])
            sage: g = FFPD(x + y, [(y, 1), (x, 2)])
            sage: s = FractionWithFactoredDenominatorSum([f]); s
            (x + y, [(y, 1), (x, 1)])
            sage: t = FractionWithFactoredDenominatorSum([g]); t
            (x + y, [(y, 1), (x, 2)])
            sage: s != t
            True
        """
    @property
    def denominator_ring(self):
        """
        Return the polynomial ring of the denominators of ``self``.

        OUTPUT: a ring or ``None`` if the list is empty

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing, FractionWithFactoredDenominatorSum
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R)
            sage: f = FFPD(x + y, [(y, 1), (x, 1)])
            sage: s = FractionWithFactoredDenominatorSum([f])
            sage: s.denominator_ring
            Multivariate Polynomial Ring in x, y over Rational Field
            sage: g = FFPD(x + y, [])
            sage: t = FractionWithFactoredDenominatorSum([g])
            sage: t.denominator_ring
            Multivariate Polynomial Ring in x, y over Rational Field
        """
    def whole_and_parts(self):
        """
        Rewrite ``self`` as a sum of a (possibly zero) polynomial
        followed by reduced rational expressions.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominatorSum`

        Only useful for multivariate decompositions.

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing, FractionWithFactoredDenominatorSum
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: f = x**2 + 3*y + 1/x + 1/y
            sage: f = FFPD(f); f
            (x^3*y + 3*x*y^2 + x + y, [(y, 1), (x, 1)])
            sage: FractionWithFactoredDenominatorSum([f]).whole_and_parts()
            (x^2 + 3*y, []) + (x + y, [(y, 1), (x, 1)])

            sage: f = cos(x)**2 + 3*y + 1/x + 1/y; f
            cos(x)^2 + 3*y + 1/x + 1/y
            sage: G = f.numerator()
            sage: H = R(f.denominator())
            sage: f = FFPD(G, H.factor()); f
            (x*y*cos(x)^2 + 3*x*y^2 + x + y, [(y, 1), (x, 1)])
            sage: FractionWithFactoredDenominatorSum([f]).whole_and_parts()
            (0, []) + (x*y*cos(x)^2 + 3*x*y^2 + x + y, [(y, 1), (x, 1)])
        """
    def sum(self):
        """
        Return the sum of the elements in ``self``.

        OUTPUT: an instance of :class:`FractionWithFactoredDenominator`

        EXAMPLES::

            sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing, FractionWithFactoredDenominatorSum
            sage: R.<x,y> = PolynomialRing(QQ)
            sage: FFPD = FractionWithFactoredDenominatorRing(R, SR)
            sage: df = (x, 1), (y, 1), (x*y + 1, 1)
            sage: f = FFPD(2, df)
            sage: g = FFPD(2*x*y, df)
            sage: FractionWithFactoredDenominatorSum([f, g])
            (2, [(y, 1), (x, 1), (x*y + 1, 1)]) + (2, [(x*y + 1, 1)])
            sage: FractionWithFactoredDenominatorSum([f, g]).sum()
            (2, [(y, 1), (x, 1)])

            sage: f = FFPD(cos(x), [(x, 2)])
            sage: g = FFPD(cos(y), [(x, 1), (y, 2)])
            sage: FractionWithFactoredDenominatorSum([f, g])
            (cos(x), [(x, 2)]) + (cos(y), [(y, 2), (x, 1)])
            sage: FractionWithFactoredDenominatorSum([f, g]).sum()
            (y^2*cos(x) + x*cos(y), [(y, 2), (x, 2)])
        """

def diff_prod(f_derivs, u, g, X, interval, end, uderivs, atc):
    """
    Take various derivatives of the equation `f = ug`,
    evaluate them at a point `c`, and solve for the derivatives of `u`.

    INPUT:

    - ``f_derivs`` -- dictionary whose keys are all tuples of the form
      ``s + end``, where ``s`` is a sequence of variables from ``X`` whose
      length lies in ``interval``, and whose values are the derivatives
      of a function `f` evaluated at `c`
    - ``u`` -- a callable symbolic function
    - ``g`` -- an expression or callable symbolic function
    - ``X`` -- list of symbolic variables
    - ``interval`` -- list of positive integers
      Call the first and last values `n` and `nn`, respectively
    - ``end`` -- a possibly empty list of repetitions of the
      variable ``z``, where ``z`` is the last element of ``X``
    - ``uderivs`` -- dictionary whose keys are the symbolic
      derivatives of order 0 to order `n-1` of ``u`` evaluated at `c`
      and whose values are the corresponding derivatives evaluated at `c`
    - ``atc`` -- dictionary whose keys are the keys of `c` and all
      the symbolic derivatives of order 0 to order `nn` of ``g``
      evaluated `c` and whose values are the corresponding
      derivatives evaluated at `c`

    OUTPUT:

    A dictionary whose keys are the derivatives of ``u`` up to order
    `nn` and whose values are those derivatives evaluated at `c`.

    This function works by differentiating the equation `f = ug`
    with respect to the variable sequence ``s + end``,
    for all tuples ``s`` of ``X`` of lengths in ``interval``,
    evaluating at the point `c` ,
    and solving for the remaining derivatives of ``u``.
    This function assumes that ``u`` never appears in the
    differentiations of `f = ug` after evaluating at `c`.

    .. NOTE::

        For internal use by
        :meth:`FractionWithFactoredDenominator.asymptotics_multiple()`.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import diff_prod
        sage: u = function('u')(x)
        sage: g = function('g')(x)
        sage: fd = {(x,):1,(x, x):1}
        sage: ud = {u(x=2): 1}
        sage: atc = {x: 2, g(x=2): 3, diff(g, x)(x=2): 5}
        sage: atc[diff(g, x, x)(x=2)] = 7
        sage: dd = diff_prod(fd, u, g, [x], [1, 2], [], ud, atc)
        sage: dd[diff(u, x, 2)(x=2)]
        22/9
    """
def permutation_sign(s, u):
    """
    This function returns the sign of the permutation on
    ``1, ..., len(u)`` that is induced by the sublist ``s`` of ``u``.

    .. NOTE::

        This function was intended for internal use and is deprecated now
        (:issue:`29465`).

    INPUT:

    - ``s`` -- a sublist of ``u``
    - ``u`` -- list

    OUTPUT:

    The sign of the permutation obtained by taking indices
    within ``u`` of the list ``s + sc``, where ``sc`` is ``u``
    with the elements of ``s`` removed.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import permutation_sign
        sage: u = ['a', 'b', 'c', 'd', 'e']
        sage: s = ['b', 'd']
        sage: permutation_sign(s, u)
        doctest:...: DeprecationWarning: the function permutation_sign is deprecated
        See https://github.com/sagemath/sage/issues/29465 for details.
        -1
        sage: s = ['d', 'b']
        sage: permutation_sign(s, u)
        1
    """
def subs_all(f, sub, simplify: bool = False):
    """
    Return the items of `f` substituted by the dictionaries
    of ``sub`` in order of their appearance in ``sub``.

    INPUT:

    - ``f`` -- an individual or list of symbolic expressions
      or dictionaries
    - ``sub`` -- an individual or list of dictionaries
    - ``simplify`` -- boolean (default: ``False``); set to ``True`` to
      simplify the result

    OUTPUT:

    The items of ``f`` substituted by the dictionaries of ``sub`` in order
    of their appearance in ``sub``. The ``subs()`` command is used. If
    simplify is ``True``, then ``simplify()`` is used after substitution.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import subs_all
        sage: var('x, y, z')
        (x, y, z)
        sage: a = {x:1}
        sage: b = {y:2}
        sage: c = {z:3}
        sage: subs_all(x + y + z, a)
        y + z + 1
        sage: subs_all(x + y + z, [c, a])
        y + 4
        sage: subs_all([x + y + z, y^2], b)
        [x + z + 2, 4]
        sage: subs_all([x + y + z, y^2], [b, c])
        [x + 5, 4]

    ::

        sage: var('x, y')
        (x, y)
        sage: a = {'foo': x**2 + y**2, 'bar': x - y}
        sage: b = {x: 1, y: 2}
        sage: subs_all(a, b)
        {'bar': -1, 'foo': 5}
    """
def diff_all(f, V, n, ending=[], sub=None, sub_final=None, zero_order: int = 0, rekey=None):
    """
    Return a dictionary of representative mixed partial
    derivatives of `f` from order 1 up to order `n` with respect to the
    variables in `V`.

    The default is to key the dictionary by all nondecreasing sequences
    in `V` of length 1 up to length `n`.

    INPUT:

    - ``f`` -- an individual or list of `\\mathcal{C}^{n+1}` functions
    - ``V`` -- list of variables occurring in `f`
    - ``n`` -- a natural number
    - ``ending`` -- list of variables in `V`
    - ``sub`` -- an individual or list of dictionaries
    - ``sub_final`` -- an individual or list of dictionaries
    - ``rekey`` -- a callable symbolic function in `V` or list thereof
    - ``zero_order`` -- a natural number

    OUTPUT: the dictionary ``{s_1:deriv_1, ..., sr:deriv_r}``

    Here ``s_1, ..., s_r`` is a listing of
    all nondecreasing sequences of length 1 up to length `n` over the
    alphabet `V`, where `w > v` in `X` if and only if ``str(w) > str(v)``,
    and ``deriv_j`` is the derivative of `f` with respect to the derivative
    sequence ``s_j`` and simplified with respect to the substitutions in
    ``sub`` and evaluated at ``sub_final``.
    Moreover, all derivatives with respect to sequences of length less than
    ``zero_order`` (derivatives of order less than ``zero_order`` )
    will be made zero.

    If ``rekey`` is nonempty, then ``s_1, ..., s_r`` will be replaced
    by the symbolic derivatives of the functions in ``rekey``.

    If ``ending`` is nonempty, then every derivative sequence ``s_j``
    will be suffixed by ``ending``.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import diff_all
        sage: f = function('f')(x)
        sage: dd = diff_all(f, [x], 3)
        sage: dd[(x, x, x)]
        diff(f(x), x, x, x)

        sage: d1 = {diff(f, x): 4*x^3}
        sage: dd = diff_all(f, [x], 3, sub=d1)
        sage: dd[(x, x, x)]
        24*x

        sage: dd = diff_all(f, [x], 3, sub=d1, rekey=f)
        sage: dd[diff(f, x, 3)]
        24*x

        sage: a = {x:1}
        sage: dd = diff_all(f, [x], 3, sub=d1, rekey=f, sub_final=a)
        sage: dd[diff(f, x, 3)]
        24

    ::

        sage: X = var('x, y, z')
        sage: f = function('f')(*X)
        sage: dd = diff_all(f, X, 2, ending=[y, y, y])
        sage: dd[(z, y, y, y)]
        diff(f(x, y, z), y, y, y, z)

    ::

        sage: g = function('g')(*X)
        sage: dd = diff_all([f, g], X, 2)
        sage: dd[(0, y, z)]
        diff(f(x, y, z), y, z)

        sage: dd[(1, z, z)]
        diff(g(x, y, z), z, z)

        sage: f = exp(x*y*z)
        sage: ff = function('ff')(*X)
        sage: dd = diff_all(f, X, 2, rekey=ff)
        sage: dd[diff(ff, x, z)]
        x*y^2*z*e^(x*y*z) + y*e^(x*y*z)
    """
def diff_op(A, B, AB_derivs, V, M, r, N):
    """
    Return the derivatives `DD^{(l+k)}(A[j] B^l)` evaluated at a point
    `p` for various natural numbers `j, k, l` which depend on `r` and `N`.

    Here `DD` is a specific second-order linear differential operator
    that depends on `M` , `A` is a list of symbolic functions,
    `B` is symbolic function, and ``AB_derivs`` contains all the derivatives
    of `A` and `B` evaluated at `p` that are necessary for the computation.

    INPUT:

    - ``A`` -- a single or length ``r`` list of symbolic functions in the
      variables ``V``
    - ``B`` -- a symbolic function in the variables ``V``
    - ``AB_derivs`` -- dictionary whose keys are the (symbolic)
      derivatives of ``A[0], ..., A[r-1]`` up to order ``2 * N-2`` and
      the (symbolic) derivatives of ``B`` up to order ``2 * N``;
      the values of the dictionary are complex numbers that are
      the keys evaluated at a common point `p`
    - ``V`` -- the variables of the ``A[j]`` and ``B``
    - ``M`` -- a symmetric `l \\times l` matrix, where `l` is the
      length of ``V``
    - ``r``, ``N`` -- natural numbers

    OUTPUT: a dictionary

    The output is
    a dictionary whose keys are natural number tuples of the form
    `(j, k, l)`, where `l \\leq 2k`, `j \\leq r-1`, and `j+k \\leq N-1`,
    and whose values are `DD^(l+k)(A[j] B^l)` evaluated at a point
    `p`, where `DD` is the linear second-order differential operator
    `-\\sum_{i=0}^{l-1} \\sum_{j=0}^{l-1} M[i][j]
    \\partial^2 /(\\partial V[j] \\partial V[i])`.

    .. NOTE::

        For internal use by
        :meth:`FractionWithFactoredDenominator.asymptotics_smooth()` and
        :meth:`FractionWithFactoredDenominator.asymptotics_multiple()`.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import diff_op
        sage: T = var('x, y')
        sage: A = function('A')(*tuple(T))
        sage: B = function('B')(*tuple(T))
        sage: AB_derivs = {}
        sage: M = matrix([[1, 2],[2, 1]])
        sage: DD = diff_op(A, B, AB_derivs, T, M, 1, 2)  # long time (see :issue:`35207`)
        sage: sorted(DD)                                 # long time
        [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2)]
        sage: DD[(0, 1, 2)].number_of_operands()         # long time
        246
    """
def diff_seq(V, s):
    """
    Given a list ``s`` of tuples of natural numbers, return the
    list of elements of ``V`` with indices the elements of the elements
    of ``s``.

    INPUT:

    - ``V`` -- list
    - ``s`` -- list of tuples of natural numbers in the interval
      ``range(len(V))``

    OUTPUT:

    The tuple ``tuple([V[tt] for tt in sorted(t)])``, where ``t`` is the
    list of elements of the elements of ``s``.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import diff_seq
        sage: V = list(var('x, t, z'))
        sage: diff_seq(V,([0, 1],[0, 2, 1],[0, 0]))
        (x, x, x, x, t, t, z)

    .. NOTE::

        This function is for internal use by :func:`diff_op()`.
    """
def diff_op_simple(A, B, AB_derivs, x, v, a, N):
    """
    Return `DD^(e k + v l)(A B^l)` evaluated at a point `p` for
    various natural numbers `e, k, l` that depend on `v` and `N`.

    Here `DD` is a specific linear differential operator that depends
    on `a` and `v` , `A` and `B` are symbolic functions, and ``AB_derivs``
    contains all the derivatives of `A` and `B` evaluated at `p` that are
    necessary for the computation.

    .. NOTE::

        For internal use by the function
        :meth:`FractionWithFactoredDenominator.asymptotics_smooth()`.

    INPUT:

    - ``A``, ``B`` -- symbolic functions in the variable ``x``
    - ``AB_derivs`` -- dictionary whose keys are the (symbolic)
      derivatives of ``A`` up to order ``2 * N`` if ``v`` is even or
      ``N`` if ``v`` is odd and the (symbolic) derivatives of ``B``
      up to order ``2 * N + v`` if ``v`` is even or ``N + v``
      if ``v`` is odd; the values of the dictionary are complex numbers
      that are the keys evaluated at a common point `p`
    - ``x`` -- a symbolic variable
    - ``a`` -- a complex number
    - ``v``, ``N`` -- natural numbers

    OUTPUT: a dictionary

    The output is
    a dictionary whose keys are natural number pairs of the form `(k, l)`,
    where `k < N` and `l \\leq 2k` and whose values are
    `DD^(e k + v l)(A B^l)` evaluated at a point `p`.
    Here `e=2` if `v` is even, `e=1` if `v` is odd, and `DD` is the
    linear differential operator
    `(a^{-1/v} d/dt)` if `v` is even and
    `(|a|^{-1/v} i \\text{sgn}(a) d/dt)` if `v` is odd.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import diff_op_simple
        sage: A = function('A')(x)
        sage: B = function('B')(x)
        sage: AB_derivs = {}
        sage: sorted(diff_op_simple(A, B, AB_derivs, x, 3, 2, 2).items())
        [((0, 0), A(x)),
         ((1, 0), 1/2*I*2^(2/3)*diff(A(x), x)),
         ((1, 1),
          1/4*2^(2/3)*(B(x)*diff(A(x), x, x, x, x) + 4*diff(A(x), x, x, x)*diff(B(x), x) + 6*diff(A(x), x, x)*diff(B(x), x, x) + 4*diff(A(x), x)*diff(B(x), x, x, x) + A(x)*diff(B(x), x, x, x, x)))]
    """
def direction(v, coordinate=None):
    """
    Return ``[vv/v[coordinate] for vv in v]`` where
    ``coordinate`` is the last index of ``v`` if not specified otherwise.

    INPUT:

    - ``v`` -- a vector
    - ``coordinate`` -- (default: ``None``) an index for ``v``

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import direction
        sage: direction([2, 3, 5])
        (2/5, 3/5, 1)
        sage: direction([2, 3, 5], 0)
        (1, 3/2, 5/2)
    """
def coerce_point(R, p):
    '''
    Coerce the keys of the dictionary ``p`` into the ring ``R``.

    .. WARNING::

        This method assumes that it is possible.

    EXAMPLES::

        sage: from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import FractionWithFactoredDenominatorRing, coerce_point
        sage: R.<x,y> = PolynomialRing(QQ)
        sage: FFPD = FractionWithFactoredDenominatorRing(R)
        sage: f = FFPD()
        sage: p = {SR(x): 1, SR(y): 7/8}
        sage: for k in sorted(p, key=str):
        ....:     print("{} {} {}".format(k, k.parent(), p[k]))
        x Symbolic Ring 1
        y Symbolic Ring 7/8
        sage: q = coerce_point(R, p)
        sage: for k in sorted(q, key=str):
        ....:     print("{} {} {}".format(k, k.parent(), q[k]))
        x Multivariate Polynomial Ring in x, y over Rational Field 1
        y Multivariate Polynomial Ring in x, y over Rational Field 7/8
    '''
