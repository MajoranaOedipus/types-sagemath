from sage.categories.category_singleton import Category_contains_method_by_parent_class as Category_contains_method_by_parent_class, Category_singleton as Category_singleton
from sage.categories.gcd_domains import GcdDomains as GcdDomains
from sage.misc.lazy_attribute import lazy_class_attribute as lazy_class_attribute
from sage.misc.misc_c import prod as prod

class UniqueFactorizationDomains(Category_singleton):
    """
    The category of (constructive) unique factorization domains.

    In a constructive unique factorization domain we can
    constructively factor members into a product of a finite number
    of irreducible elements.

    EXAMPLES::

        sage: UniqueFactorizationDomains()
        Category of unique factorization domains
        sage: UniqueFactorizationDomains().super_categories()
        [Category of gcd domains]

    TESTS::

        sage: TestSuite(UniqueFactorizationDomains()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: UniqueFactorizationDomains().super_categories()
            [Category of gcd domains]
        """
    def additional_structure(self) -> None:
        """
        Return whether ``self`` is a structure category.

        .. SEEALSO:: :meth:`Category.additional_structure`

        The category of unique factorization domains does not define
        additional structure: a ring morphism between unique factorization
        domains is a unique factorization domain morphism.

        EXAMPLES::

            sage: UniqueFactorizationDomains().additional_structure()
        """
    def __contains__(self, x) -> bool:
        '''
        EXAMPLES::

            sage: GF(4, "a") in UniqueFactorizationDomains()                            # needs sage.rings.finite_rings
            True
            sage: QQ in UniqueFactorizationDomains()
            True
            sage: ZZ in UniqueFactorizationDomains()
            True
            sage: IntegerModRing(4) in UniqueFactorizationDomains()
            False
            sage: IntegerModRing(5) in UniqueFactorizationDomains()
            True

        This implementation will not be needed anymore once every
        field in Sage will be properly declared in the category
        :class:`UniqueFactorizationDomains() <UniqueFactorizationDomains>`.
        '''
    class ParentMethods:
        def is_unique_factorization_domain(self, proof: bool = True):
            """
            Return ``True``, since this in an object of the category of unique factorization domains.

            EXAMPLES::

                sage: UFD = UniqueFactorizationDomains()
                sage: Parent(QQ, category=UFD).is_unique_factorization_domain()
                True
            """
    class ElementMethods:
        def radical(self, *args, **kwds):
            """
            Return the radical of this element, i.e. the product of its
            irreducible factors.

            This default implementation calls ``squarefree_decomposition`` if
            available, and ``factor`` otherwise.

            .. SEEALSO:: :meth:`squarefree_part`

            EXAMPLES::

                sage: Pol.<x> = QQ[]
                sage: (x^2*(x-1)^3).radical()
                x^2 - x
                sage: pol = 37 * (x-1)^3 * (x-2)^2 * (x-1/3)^7 * (x-3/7)
                sage: pol.radical()
                37*x^4 - 2923/21*x^3 + 1147/7*x^2 - 1517/21*x + 74/7

                sage: Integer(10).radical()
                10
                sage: Integer(-100).radical()
                10
                sage: Integer(0).radical()
                Traceback (most recent call last):
                ...
                ArithmeticError: radical of 0 is not defined

            The next example shows how to compute the radical of a number,
            assuming no prime > 100000 has exponent > 1 in the factorization::

                sage: n = 2^1000-1; n / radical(n, limit=100000)
                125

            TESTS::

                sage: radical(pol)
                37*x^4 - 2923/21*x^3 + 1147/7*x^2 - 1517/21*x + 74/7

                sage: Integer(20).radical()
                10
            """
        def squarefree_part(self):
            """
            Return the square-free part of this element, i.e. the product
            of its irreducible factors appearing with odd multiplicity.

            This default implementation calls ``squarefree_decomposition``.

            .. SEEALSO:: :meth:`radical`

            EXAMPLES::

                sage: Pol.<x> = QQ[]
                sage: (x^2*(x-1)^3).squarefree_part()
                x - 1
                sage: pol = 37 * (x-1)^3 * (x-2)^2 * (x-1/3)^7 * (x-3/7)
                sage: pol.squarefree_part()
                37*x^3 - 1369/21*x^2 + 703/21*x - 37/7

            TESTS::

                sage: squarefree_part(pol)
                37*x^3 - 1369/21*x^2 + 703/21*x - 37/7
            """
