from sage.categories.category import Category as Category
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings

class NoetherianRings(Category):
    """
    The category of Noetherian rings.

    A Noetherian ring is a commutative ring in which
    every ideal is finitely generated.

    See :wikipedia:`Noetherian ring`

    EXAMPLES::

        sage: from sage.categories.noetherian_rings import NoetherianRings
        sage: C = NoetherianRings(); C
        Category of noetherian rings
        sage: sorted(C.super_categories(), key=str)
        [Category of commutative rings]

    TESTS::

        sage: TestSuite(C).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: from sage.categories.noetherian_rings import NoetherianRings
            sage: NoetherianRings().super_categories()
            [Category of commutative rings]
        """
    class ParentMethods:
        def is_noetherian(self, proof: bool = True):
            """
            Return ``True``, since this in an object of the category
            of Noetherian rings.

            EXAMPLES::

                sage: ZZ.is_noetherian()
                True
                sage: QQ.is_noetherian()
                True
                sage: ZZ['x'].is_noetherian()
                True
                sage: R.<x> = PolynomialRing(QQ)
                sage: R.is_noetherian()
                True

                sage: L.<z> = LazyLaurentSeriesRing(QQ)                                 # needs sage.combinat
                sage: L.is_noetherian()                                            # needs sage.combinat
                True
            """
    class ElementMethods: ...
