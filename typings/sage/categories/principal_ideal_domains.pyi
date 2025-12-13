from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.unique_factorization_domains import UniqueFactorizationDomains as UniqueFactorizationDomains

class PrincipalIdealDomains(Category_singleton):
    """
    The category of (constructive) principal ideal domains.

    By constructive, we mean that a single generator can be
    constructively found for any ideal given by a finite set of
    generators. Note that this constructive definition only implies
    that finitely generated ideals are principal. It is not clear what
    we would mean by an infinitely generated ideal.

    EXAMPLES::

      sage: PrincipalIdealDomains()
      Category of principal ideal domains
      sage: PrincipalIdealDomains().super_categories()
      [Category of unique factorization domains]

    See also :wikipedia:`Principal_ideal_domain`

    TESTS::

        sage: TestSuite(PrincipalIdealDomains()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: PrincipalIdealDomains().super_categories()
            [Category of unique factorization domains]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of principal ideal domains defines no
        additional structure: a ring morphism between two principal
        ideal domains is a principal ideal domain morphism.

        EXAMPLES::

            sage: PrincipalIdealDomains().additional_structure()
        """
    class ParentMethods:
        def is_noetherian(self) -> bool:
            """
            Every principal ideal domain is Noetherian, so we return ``True``.

            EXAMPLES::

                sage: Zp(5).is_noetherian()                                                 # needs sage.rings.padics
                True
            """
        def class_group(self):
            """
            Return the trivial group, since the class group of a PID is trivial.

            EXAMPLES::

                sage: QQ.class_group()                                                      # needs sage.groups
                Trivial Abelian group
            """
        def gcd(self, x, y, coerce: bool = True):
            """
            Return the greatest common divisor of ``x`` and ``y``, as elements
            of ``self``.

            EXAMPLES:

            The integers are a principal ideal domain and hence a GCD domain::

                sage: ZZ.gcd(42, 48)
                6
                sage: 42.factor(); 48.factor()
                2 * 3 * 7
                2^4 * 3
                sage: ZZ.gcd(2^4*7^2*11, 2^3*11*13)
                88
                sage: 88.factor()
                2^3 * 11

            In a field, any nonzero element is a GCD of any nonempty set
            of nonzero elements. In previous versions, Sage used to return
            1 in the case of the rational field. However, since :issue:`10771`,
            the rational field is considered as the
            *fraction field* of the integer ring. For the fraction field
            of an integral domain that provides both GCD and LCM, it is
            possible to pick a GCD that is compatible with the GCD of the
            base ring::

                sage: QQ.gcd(ZZ(42), ZZ(48)); type(QQ.gcd(ZZ(42), ZZ(48)))
                6
                <class 'sage.rings.rational.Rational'>
                sage: QQ.gcd(1/2, 1/3)
                1/6

            Polynomial rings over fields are GCD domains as well. Here is a simple
            example over the ring of polynomials over the rationals as well as
            over an extension ring. Note that ``gcd`` requires x and y to be
            coercible::

                sage: # needs sage.rings.number_field
                sage: R.<x> = PolynomialRing(QQ)
                sage: S.<a> = NumberField(x^2 - 2, 'a')
                sage: f = (x - a)*(x + a); g = (x - a)*(x^2 - 2)
                sage: print(f); print(g)
                x^2 - 2
                x^3 - a*x^2 - 2*x + 2*a
                sage: f in R
                True
                sage: g in R
                False
                sage: R.gcd(f, g)
                Traceback (most recent call last):
                ...
                TypeError: Unable to coerce 2*a to a rational
                sage: R.base_extend(S).gcd(f,g)
                x^2 - 2
                sage: R.base_extend(S).gcd(f, (x - a)*(x^2 - 3))
                x - a
            """
        def content(self, x, y, coerce: bool = True):
            """
            Return the content of `x` and `y`.

            This is the unique element `c` of
            ``self`` such that `x/c` and `y/c`
            are coprime and integral.

            EXAMPLES::

                sage: QQ.content(ZZ(42), ZZ(48)); type(QQ.content(ZZ(42), ZZ(48)))
                6
                <class 'sage.rings.rational.Rational'>
                sage: QQ.content(1/2, 1/3)
                1/6
                sage: factor(1/2); factor(1/3); factor(1/6)
                2^-1
                3^-1
                2^-1 * 3^-1
                sage: a = (2*3)/(7*11); b = (13*17)/(19*23)
                sage: factor(a); factor(b); factor(QQ.content(a,b))
                2 * 3 * 7^-1 * 11^-1
                13 * 17 * 19^-1 * 23^-1
                7^-1 * 11^-1 * 19^-1 * 23^-1

            Note the changes to the second entry::

                sage: c = (2*3)/(7*11); d = (13*17)/(7*19*23)
                sage: factor(c); factor(d); factor(QQ.content(c,d))
                2 * 3 * 7^-1 * 11^-1
                7^-1 * 13 * 17 * 19^-1 * 23^-1
                7^-1 * 11^-1 * 19^-1 * 23^-1
                sage: e = (2*3)/(7*11); f = (13*17)/(7^3*19*23)
                sage: factor(e); factor(f); factor(QQ.content(e,f))
                2 * 3 * 7^-1 * 11^-1
                7^-3 * 13 * 17 * 19^-1 * 23^-1
                7^-3 * 11^-1 * 19^-1 * 23^-1
            """
    class ElementMethods: ...
