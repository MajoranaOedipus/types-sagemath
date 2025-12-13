from sage.categories.algebra_ideals import AlgebraIdeals as AlgebraIdeals
from sage.categories.category_types import Category_ideal as Category_ideal, Category_in_ambient as Category_in_ambient
from sage.categories.commutative_algebras import CommutativeAlgebras as CommutativeAlgebras
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings

class CommutativeAlgebraIdeals(Category_ideal):
    """
    The category of ideals in a fixed commutative algebra `A`.

    EXAMPLES::

        sage: C = CommutativeAlgebraIdeals(QQ['x'])
        sage: C
        Category of commutative algebra ideals in
         Univariate Polynomial Ring in x over Rational Field
    """
    def __init__(self, A) -> None:
        """
        EXAMPLES::

            sage: CommutativeAlgebraIdeals(ZZ['x'])
            Category of commutative algebra ideals in
             Univariate Polynomial Ring in x over Integer Ring

            sage: CommutativeAlgebraIdeals(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: A (=Integer Ring) must be a commutative algebra

            sage: CommutativeAlgebraIdeals(IntegerModRing(4))
            Traceback (most recent call last):
            ...
            TypeError: A (=Ring of integers modulo 4) must be a commutative algebra

            sage: CommutativeAlgebraIdeals(Partitions(4))                               # needs sage.combinat
            Traceback (most recent call last):
            ...
            TypeError: A (=Partitions of the integer 4) must be a commutative algebra

        TESTS::

            sage: TestSuite(CommutativeAlgebraIdeals(QQ['x'])).run()
        """
    def algebra(self):
        """
        EXAMPLES::

            sage: CommutativeAlgebraIdeals(QQ['x']).algebra()
            Univariate Polynomial Ring in x over Rational Field
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: CommutativeAlgebraIdeals(QQ['x']).super_categories()
            [Category of algebra ideals in Univariate Polynomial Ring in x over Rational Field]
        """
