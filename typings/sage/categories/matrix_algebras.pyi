from sage.categories.algebras import Algebras as Algebras
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring

class MatrixAlgebras(Category_over_base_ring):
    """
    The category of matrix algebras over a field.

    EXAMPLES::

        sage: MatrixAlgebras(RationalField())
        Category of matrix algebras over Rational Field

    TESTS::

        sage: TestSuite(MatrixAlgebras(ZZ)).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: MatrixAlgebras(QQ).super_categories()
            [Category of algebras over Rational Field]
        """
