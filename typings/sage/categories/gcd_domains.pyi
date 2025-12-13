from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.integral_domains import IntegralDomains as IntegralDomains

class GcdDomains(Category_singleton):
    """
    The category of gcd domains
    domains where gcd can be computed but where there is no guarantee of
    factorisation into irreducibles

    EXAMPLES::

        sage: GcdDomains()
        Category of gcd domains
        sage: GcdDomains().super_categories()
        [Category of integral domains]

    TESTS::

        sage: TestSuite(GcdDomains()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: GcdDomains().super_categories()
            [Category of integral domains]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of gcd domains defines no additional
        structure: a ring morphism between two gcd domains is a gcd
        domain morphism.

        .. SEEALSO:: :meth:`Category.additional_structure`

        EXAMPLES::

            sage: GcdDomains().additional_structure()
        """
    class ParentMethods: ...
    class ElementMethods: ...
