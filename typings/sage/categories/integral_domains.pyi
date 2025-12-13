from sage.categories.category_singleton import Category_contains_method_by_parent_class as Category_contains_method_by_parent_class
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.domains import Domains as Domains
from sage.misc.lazy_attribute import lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import lazy_import as lazy_import

class IntegralDomains(CategoryWithAxiom):
    """
    The category of integral domains.

    An integral domain is commutative ring with no zero divisors, or
    equivalently a commutative domain.

    EXAMPLES::

        sage: C = IntegralDomains(); C
        Category of integral domains
        sage: sorted(C.super_categories(), key=str)
        [Category of commutative rings, Category of domains]
        sage: C is Domains().Commutative()
        True
        sage: C is Rings().Commutative().NoZeroDivisors()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
    def __contains__(self, x) -> bool:
        '''
        EXAMPLES::

            sage: GF(4, "a") in IntegralDomains()                                       # needs sage.rings.finite_rings
            True
            sage: QQ in IntegralDomains()
            True
            sage: ZZ in IntegralDomains()
            True
            sage: IntegerModRing(4) in IntegralDomains()
            False
            sage: IntegerModRing(5) in IntegralDomains()
            True

        This implementation will not be needed anymore once every
        field in Sage will be properly declared in the category
        :class:`IntegralDomains() <IntegralDomains>`.
        '''
    class ParentMethods:
        def is_integral_domain(self, proof: bool = True):
            """
            Return ``True``, since this in an object of the category
            of integral domains.

            EXAMPLES::

                sage: ZZ.is_integral_domain()
                True
                sage: QQ.is_integral_domain()
                True
                sage: Parent(QQ, category=IntegralDomains()).is_integral_domain()
                True

                sage: L.<z> = LazyLaurentSeriesRing(QQ)                                 # needs sage.combinat
                sage: L.is_integral_domain()                                            # needs sage.combinat
                True
                sage: L.is_integral_domain(proof=True)                                  # needs sage.combinat
                True

                sage: ZZ['x'].is_integral_domain()
                True
            """
        def is_field(self, proof: bool = True):
            """
            Return ``True`` if this ring is a field.

            EXAMPLES::

                sage: ZZ['x'].is_field()
                False
            """
        def localization(self, additional_units, names=None, normalize: bool = True, category=None):
            """
            Return the localization of ``self`` at the given additional units.

            EXAMPLES::

                sage: R.<x, y> = GF(3)[]
                sage: R.localization((x*y, x**2 + y**2))                                    # needs sage.rings.finite_rings
                Multivariate Polynomial Ring in x, y over Finite Field of size 3
                 localized at (y, x, x^2 + y^2)
                sage: ~y in _                                                               # needs sage.rings.finite_rings
                True
            """
    class ElementMethods: ...
