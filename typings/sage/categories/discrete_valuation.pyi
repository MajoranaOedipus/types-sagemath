from sage.categories.category_singleton import Category_singleton as Category_singleton
from sage.categories.euclidean_domains import EuclideanDomains as EuclideanDomains
from sage.categories.fields import Fields as Fields
from sage.misc.abstract_method import abstract_method as abstract_method

class DiscreteValuationRings(Category_singleton):
    """
    The category of discrete valuation rings.

    EXAMPLES::

        sage: GF(7)[['x']] in DiscreteValuationRings()
        True
        sage: TestSuite(DiscreteValuationRings()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: DiscreteValuationRings().super_categories()
            [Category of euclidean domains]
        """
    class ParentMethods:
        @abstract_method
        def uniformizer(self) -> None:
            """
            Return a uniformizer of this ring.

            EXAMPLES::

                sage: Zp(5).uniformizer()                                               # needs sage.rings.padics
                5 + O(5^21)

                sage: K.<u> = QQ[[]]
                sage: K.uniformizer()
                u
            """
        @abstract_method
        def residue_field(self) -> None:
            """
            Return the residue field of this ring.

            EXAMPLES::

                sage: Zp(5).residue_field()                                             # needs sage.rings.padics
                Finite Field of size 5

                sage: K.<u> = QQ[[]]
                sage: K.residue_field()
                Rational Field
            """
    class ElementMethods:
        @abstract_method
        def valuation(self) -> None:
            """
            Return the valuation of this element.

            EXAMPLES::

                sage: # needs sage.rings.padics
                sage: x = Zp(5)(50)
                sage: x.valuation()
                2
            """
        def euclidean_degree(self):
            """
            Return the Euclidean degree of this element.

            TESTS::

                sage: R.<q> = GF(5)[[]]
                sage: (q^3).euclidean_degree()
                3
                sage: R(0).euclidean_degree()
                Traceback (most recent call last):
                ...
                ValueError: Euclidean degree of the zero element not defined
            """
        def quo_rem(self, other):
            """
            Return the quotient and remainder for Euclidean division
            of ``self`` by ``other``.

            EXAMPLES::

                sage: R.<q> = GF(5)[[]]
                sage: (q^2 + q).quo_rem(q)
                (1 + q, 0)
                sage: (q + 1).quo_rem(q^2)
                (0, 1 + q)

            TESTS::

                sage: q.quo_rem(0)
                Traceback (most recent call last):
                ...
                ZeroDivisionError: Euclidean division by the zero element not defined

                sage: L = PowerSeriesRing(QQ, 't')
                sage: t = L.gen()
                sage: F = algebras.Free(L, ['A', 'B'])
                sage: A, B = F.gens()
                sage: f = t*A+t**2*B/2
            """
        def is_unit(self):
            """
            Return ``True`` if ``self`` is invertible.

            EXAMPLES::

                sage: # needs sage.rings.padics
                sage: x = Zp(5)(50)
                sage: x.is_unit()
                False

                sage: # needs sage.rings.padics
                sage: x = Zp(7)(50)
                sage: x.is_unit()
                True
            """
        def gcd(self, other):
            """
            Return the greatest common divisor of ``self`` and ``other``,
            normalized so that it is a power of the distinguished
            uniformizer.
            """
        def lcm(self, other):
            """
            Return the least common multiple of ``self`` and ``other``,
            normalized so that it is a power of the distinguished
            uniformizer.
            """

class DiscreteValuationFields(Category_singleton):
    """
    The category of discrete valuation fields.

    EXAMPLES::

        sage: Qp(7) in DiscreteValuationFields()                                        # needs sage.rings.padics
        True
        sage: TestSuite(DiscreteValuationFields()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: DiscreteValuationFields().super_categories()
            [Category of fields]
        """
    class ParentMethods:
        @abstract_method
        def uniformizer(self) -> None:
            """
            Return a uniformizer of this ring.

            EXAMPLES::

                sage: Qp(5).uniformizer()                                               # needs sage.rings.padics
                5 + O(5^21)
            """
        @abstract_method
        def residue_field(self) -> None:
            """
            Return the residue field of the ring of integers of
            this discrete valuation field.

            EXAMPLES::

                sage: Qp(5).residue_field()                                             # needs sage.rings.padics
                Finite Field of size 5

                sage: K.<u> = LaurentSeriesRing(QQ)
                sage: K.residue_field()
                Rational Field
            """
    class ElementMethods:
        @abstract_method
        def valuation(self) -> None:
            """
            Return the valuation of this element.

            EXAMPLES::

                sage: # needs sage.rings.padics
                sage: x = Qp(5)(50)
                sage: x.valuation()
                2
            """
