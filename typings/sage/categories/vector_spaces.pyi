from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category import Category as Category
from sage.categories.category_types import Category_module as Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory as DualObjectsCategory
from sage.categories.fields import Fields as Fields
from sage.categories.filtered_modules import FilteredModulesCategory as FilteredModulesCategory
from sage.categories.graded_modules import GradedModulesCategory as GradedModulesCategory
from sage.categories.modules import Modules as Modules
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory

class VectorSpaces(Category_module):
    """
    The category of (abstract) vector spaces over a given field.

    ??? with an embedding in an ambient vector space ???

    EXAMPLES::

        sage: VectorSpaces(QQ)
        Category of vector spaces over Rational Field
        sage: VectorSpaces(QQ).super_categories()
        [Category of modules over Rational Field]
    """
    @staticmethod
    def __classcall_private__(cls, K, check: bool = True):
        """
        INPUT:

        - ``K`` -- a field
        - ``check`` -- boolean (default: ``True``); whether to check that `K`
          is a field

        EXAMPLES::

            sage: VectorSpaces(QQ) is VectorSpaces(QQ, check=False)
            True

        By default, it is checked that ``K`` is a field::

            sage: VectorSpaces(ZZ)
            Traceback (most recent call last):
            ...
            ValueError: base must be a field or a subcategory of Fields(); got Integer Ring

        With ``check=False``, the check is disabled, possibly enabling
        incorrect inputs::

            sage: VectorSpaces(ZZ, check=False)
            Category of vector spaces over Integer Ring
        """
    def __init__(self, K) -> None:
        """
        EXAMPLES::

            sage: VectorSpaces(QQ)
            Category of vector spaces over Rational Field
            sage: VectorSpaces(ZZ)
            Traceback (most recent call last):
            ...
            ValueError: base must be a field or a subcategory of Fields(); got Integer Ring

        TESTS::

            sage: C = QQ^10      # vector space                                         # needs sage.modules
            sage: TestSuite(C).run()                                                    # needs sage.modules
            sage: TestSuite(VectorSpaces(QQ)).run()
        """
    def base_field(self):
        """
        Return the base field over which the vector spaces of this
        category are all defined.

        EXAMPLES::

            sage: VectorSpaces(QQ).base_field()
            Rational Field
        """
    def super_categories(self):
        """
        EXAMPLES::

            sage: VectorSpaces(QQ).super_categories()
            [Category of modules over Rational Field]
        """
    def additional_structure(self) -> None:
        """
        Return  ``None``.

        Indeed, the category of vector spaces defines no additional
        structure: a bimodule morphism between two vector spaces is a
        vector space morphism.

        .. SEEALSO:: :meth:`Category.additional_structure`

        .. TODO:: Should this category be a :class:`CategoryWithAxiom`?

        EXAMPLES::

            sage: VectorSpaces(QQ).additional_structure()
        """
    class ParentMethods:
        def dimension(self):
            """
            Return the dimension of this vector space.

            EXAMPLES::

                sage: M = FreeModule(FiniteField(19), 100)                              # needs sage.modules
                sage: W = M.submodule([M.gen(50)])                                      # needs sage.modules
                sage: W.dimension()                                                     # needs sage.modules
                1

                sage: M = FiniteRankFreeModule(QQ, 3)                                   # needs sage.modules
                sage: M.dimension()                                                     # needs sage.modules
                3
                sage: M.tensor_module(1, 2).dimension()                                 # needs sage.modules
                27
            """
    class ElementMethods: ...
    class WithBasis(CategoryWithAxiom_over_base_ring):
        def is_abelian(self):
            """
            Return whether this category is abelian.

            This is always ``True`` since the base ring is a field.

            EXAMPLES::

                sage: VectorSpaces(QQ).WithBasis().is_abelian()
                True
            """
        class CartesianProducts(CartesianProductsCategory):
            def extra_super_categories(self):
                """
                The category of vector spaces with basis is closed under Cartesian products::

                    sage: C = VectorSpaces(QQ).WithBasis()
                    sage: C.CartesianProducts()
                    Category of Cartesian products of vector spaces with basis over Rational Field
                    sage: C in C.CartesianProducts().super_categories()
                    True
                """
        class TensorProducts(TensorProductsCategory):
            def extra_super_categories(self):
                """
                The category of vector spaces with basis is closed under tensor products::

                    sage: C = VectorSpaces(QQ).WithBasis()
                    sage: C.TensorProducts()
                    Category of tensor products of vector spaces with basis over Rational Field
                    sage: C in C.TensorProducts().super_categories()
                    True
                """
        class FiniteDimensional(CategoryWithAxiom_over_base_ring):
            class TensorProducts(TensorProductsCategory):
                def extra_super_categories(self):
                    """
                    Implement the fact that a (finite) tensor product of
                    finite dimensional vector spaces is a finite dimensional vector space.

                    EXAMPLES::

                        sage: VectorSpaces(QQ).WithBasis().FiniteDimensional().TensorProducts().extra_super_categories()
                        [Category of finite dimensional vector spaces with basis over Rational Field]
                        sage: VectorSpaces(QQ).WithBasis().FiniteDimensional().TensorProducts().FiniteDimensional()
                        Category of tensor products of finite dimensional vector spaces with basis over Rational Field
                    """
        class Graded(GradedModulesCategory):
            """
            Category of graded vector spaces with basis.
            """
            def example(self, base_ring=None):
                """
                Return an example of a graded vector space with basis,
                as per :meth:`Category.example()
                <sage.categories.category.Category.example>`.

                EXAMPLES::

                    sage: Modules(QQ).WithBasis().Graded().example()                    # needs sage.combinat sage.modules
                    An example of a graded module with basis:
                     the free module on partitions over Rational Field
                """
        class Filtered(FilteredModulesCategory):
            """
            Category of filtered vector spaces with basis.
            """
            def example(self, base_ring=None):
                """
                Return an example of a graded vector space with basis,
                as per :meth:`Category.example()
                <sage.categories.category.Category.example>`.

                EXAMPLES::

                    sage: Modules(QQ).WithBasis().Graded().example()                    # needs sage.combinat sage.modules
                    An example of a graded module with basis:
                     the free module on partitions over Rational Field
                """
    class FiniteDimensional(CategoryWithAxiom_over_base_ring):
        class TensorProducts(TensorProductsCategory):
            def extra_super_categories(self):
                """
                Implement the fact that a (finite) tensor product of
                finite dimensional vector spaces is a finite dimensional vector space.

                EXAMPLES::

                    sage: VectorSpaces(QQ).FiniteDimensional().TensorProducts().extra_super_categories()
                    [Category of finite dimensional vector spaces over Rational Field]
                    sage: VectorSpaces(QQ).FiniteDimensional().TensorProducts().FiniteDimensional()
                    Category of tensor products of finite dimensional vector spaces over Rational Field
                """
    class DualObjects(DualObjectsCategory):
        def extra_super_categories(self):
            """
            Return the dual category.

            EXAMPLES:

            The category of algebras over the Rational Field is dual
            to the category of coalgebras over the same field::

                sage: C = VectorSpaces(QQ)
                sage: C.dual()
                Category of duals of vector spaces over Rational Field
                sage: C.dual().super_categories() # indirect doctest
                [Category of vector spaces over Rational Field]
            """
    class CartesianProducts(CartesianProductsCategory):
        def extra_super_categories(self):
            """
            The category of vector spaces is closed under Cartesian products::

                sage: C = VectorSpaces(QQ)
                sage: C.CartesianProducts()
                Category of Cartesian products of vector spaces over Rational Field
                sage: C in C.CartesianProducts().super_categories()
                True
            """
    class TensorProducts(TensorProductsCategory):
        def extra_super_categories(self):
            """
            The category of vector spaces is closed under tensor products::

                sage: C = VectorSpaces(QQ)
                sage: C.TensorProducts()
                Category of tensor products of vector spaces over Rational Field
                sage: C in C.TensorProducts().super_categories()
                True
            """
    class Filtered(FilteredModulesCategory):
        """
        Category of filtered vector spaces.
        """
    class Graded(GradedModulesCategory):
        """
        Category of graded vector spaces.
        """
