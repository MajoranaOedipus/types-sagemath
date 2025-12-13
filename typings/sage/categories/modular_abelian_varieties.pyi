from sage.categories.category_types import Category_over_base as Category_over_base
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.homsets import HomsetsCategory as HomsetsCategory
from sage.categories.rings import Rings as Rings
from sage.categories.sets_cat import Sets as Sets

class ModularAbelianVarieties(Category_over_base):
    """
    The category of modular abelian varieties over a given field.

    EXAMPLES::

        sage: ModularAbelianVarieties(QQ)
        Category of modular abelian varieties over Rational Field
    """
    def __init__(self, Y) -> None:
        """
        TESTS::

            sage: C = ModularAbelianVarieties(QQ)
            sage: C
            Category of modular abelian varieties over Rational Field
            sage: TestSuite(C).run()

            sage: ModularAbelianVarieties(ZZ)
            Traceback (most recent call last):
            ...
              assert Y.is_field()
            AssertionError
        """
    def base_field(self):
        """
        EXAMPLES::

            sage: ModularAbelianVarieties(QQ).base_field()
            Rational Field
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: ModularAbelianVarieties(QQ).super_categories()
            [Category of sets]
        """
    class Homsets(HomsetsCategory):
        class Endset(CategoryWithAxiom):
            def extra_super_categories(self):
                """
                Implement the fact that an endset of modular abelian variety is a ring.

                EXAMPLES::

                    sage: ModularAbelianVarieties(QQ).Endsets().extra_super_categories()
                    [Category of rings]
                """
