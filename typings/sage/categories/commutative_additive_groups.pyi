from sage.categories.additive_groups import AdditiveGroups as AdditiveGroups
from sage.categories.algebra_functor import AlgebrasCategory as AlgebrasCategory
from sage.categories.cartesian_product import CartesianProductsCategory as CartesianProductsCategory
from sage.categories.category_types import AbelianCategory as AbelianCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom

class CommutativeAdditiveGroups(CategoryWithAxiom, AbelianCategory):
    """
    The category of abelian groups, i.e. additive abelian monoids
    where each element has an inverse.

    EXAMPLES::

        sage: C = CommutativeAdditiveGroups(); C
        Category of commutative additive groups
        sage: C.super_categories()
        [Category of additive groups, Category of commutative additive monoids]
        sage: sorted(C.axioms())
        ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse', 'AdditiveUnital']
        sage: C is CommutativeAdditiveMonoids().AdditiveInverse()
        True
        sage: from sage.categories.additive_groups import AdditiveGroups
        sage: C is AdditiveGroups().AdditiveCommutative()
        True

    .. NOTE::

        This category is currently empty. It's left there for backward
        compatibility and because it is likely to grow in the future.

    TESTS::

        sage: TestSuite(CommutativeAdditiveGroups()).run()
        sage: sorted(CommutativeAdditiveGroups().CartesianProducts().axioms())
        ['AdditiveAssociative', 'AdditiveCommutative', 'AdditiveInverse', 'AdditiveUnital']

    The empty covariant functorial construction category classes
    ``CartesianProducts`` and ``Algebras`` are left here for the sake
    of nicer output since this is a commonly used category::

        sage: CommutativeAdditiveGroups().CartesianProducts()
        Category of Cartesian products of commutative additive groups
        sage: CommutativeAdditiveGroups().Algebras(QQ)
        Category of commutative additive group algebras over Rational Field

    Also, it's likely that some code will end up there at some point.
    """
    class CartesianProducts(CartesianProductsCategory):
        class ElementMethods:
            def additive_order(self):
                """
                Return the additive order of this element.

                EXAMPLES::

                    sage: G = cartesian_product([Zmod(3), Zmod(6), Zmod(5)])
                    sage: G((1,1,1)).additive_order()
                    30
                    sage: any((i * G((1,1,1))).is_zero() for i in range(1,30))
                    False
                    sage: 30 * G((1,1,1))
                    (0, 0, 0)

                    sage: G = cartesian_product([ZZ, ZZ])
                    sage: G((0,0)).additive_order()
                    1
                    sage: G((0,1)).additive_order()
                    +Infinity

                    sage: # needs sage.rings.finite_rings
                    sage: K = GF(9)
                    sage: H = cartesian_product([
                    ....:     cartesian_product([Zmod(2), Zmod(9)]), K])
                    sage: z = H(((1,2), K.gen()))
                    sage: z.additive_order()
                    18
                """
    class Algebras(AlgebrasCategory): ...
