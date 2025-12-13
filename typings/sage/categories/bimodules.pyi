from sage.categories.category import Category as Category, CategoryWithParameters as CategoryWithParameters
from sage.categories.left_modules import LeftModules as LeftModules
from sage.categories.right_modules import RightModules as RightModules
from sage.categories.rings import Rings as Rings

class Bimodules(CategoryWithParameters):
    """
    The category of `(R,S)`-bimodules.

    For `R` and `S` rings, a `(R,S)`-bimodule `X` is a left `R`-module
    and right `S`-module such that the left and right actions commute:
    `r*(x*s) = (r*x)*s`.

    EXAMPLES::

        sage: Bimodules(QQ, ZZ)
        Category of bimodules over Rational Field on the left and Integer Ring on the right
        sage: Bimodules(QQ, ZZ).super_categories()
        [Category of left modules over Rational Field, Category of right modules over Integer Ring]
    """
    def __init__(self, left_base, right_base, name=None) -> None:
        """
        The ``name`` parameter is ignored.

        EXAMPLES::

            sage: C = Bimodules(QQ, ZZ)
            sage: TestSuite(C).run()
        """
    @classmethod
    def an_instance(cls):
        """
        Return an instance of this class.

        EXAMPLES::

            sage: Bimodules.an_instance()                                               # needs sage.rings.real_mpfr
            Category of bimodules over Rational Field on the left and Real Field with 53 bits of precision on the right
        """
    def left_base_ring(self):
        """
        Return the left base ring over which elements of this category are
        defined.

        EXAMPLES::

            sage: Bimodules(QQ, ZZ).left_base_ring()
            Rational Field
        """
    def right_base_ring(self):
        """
        Return the right base ring over which elements of this category are
        defined.

        EXAMPLES::

            sage: Bimodules(QQ, ZZ).right_base_ring()
            Integer Ring
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Bimodules(QQ, ZZ).super_categories()
            [Category of left modules over Rational Field, Category of right modules over Integer Ring]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of bimodules defines no additional
        structure: a left and right module morphism between two
        bimodules is a bimodule morphism.

        .. SEEALSO:: :meth:`Category.additional_structure`

        .. TODO:: Should this category be a :class:`CategoryWithAxiom`?

        EXAMPLES::

            sage: Bimodules(QQ, ZZ).additional_structure()
        """
    class ParentMethods: ...
    class ElementMethods: ...
