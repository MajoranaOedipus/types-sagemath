from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.coalgebras import Coalgebras as Coalgebras
from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory
from sage.misc.lazy_import import LazyImport as LazyImport

class Bialgebras(Category_over_base_ring):
    """
    The category of bialgebras.

    EXAMPLES::

        sage: Bialgebras(ZZ)
        Category of bialgebras over Integer Ring
        sage: Bialgebras(ZZ).super_categories()
        [Category of algebras over Integer Ring, Category of coalgebras over Integer Ring]

    TESTS::

        sage: TestSuite(Bialgebras(ZZ)).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: Bialgebras(QQ).super_categories()
            [Category of algebras over Rational Field, Category of coalgebras over Rational Field]
        """
    def additional_structure(self) -> None:
        """
        Return ``None``.

        Indeed, the category of bialgebras defines no additional
        structure: a morphism of coalgebras and of algebras between
        two bialgebras is a bialgebra morphism.

        .. SEEALSO:: :meth:`Category.additional_structure`

        .. TODO:: This category should be a :class:`CategoryWithAxiom`.

        EXAMPLES::

            sage: Bialgebras(QQ).additional_structure()
        """
    class ElementMethods:
        def is_primitive(self):
            """
            Return whether ``self`` is a primitive element.

            EXAMPLES::

                sage: # needs sage.modules
                sage: s = SymmetricFunctions(QQ).schur()
                sage: s([5]).is_primitive()                                             # needs lrcalc_python
                False
                sage: p = SymmetricFunctions(QQ).powersum()
                sage: p([5]).is_primitive()
                True
            """
        def is_grouplike(self):
            """
            Return whether ``self`` is a grouplike element.

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).schur()                                # needs sage.modules
                sage: s([5]).is_grouplike()                                             # needs lrcalc_python sage.modules
                False
                sage: s([]).is_grouplike()                                              # needs lrcalc_python sage.modules
                True
            """
    class Super(SuperModulesCategory): ...
    WithBasis: Incomplete
