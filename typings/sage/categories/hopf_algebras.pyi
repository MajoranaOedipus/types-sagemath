from _typeshed import Incomplete
from sage.categories.bialgebras import Bialgebras as Bialgebras
from sage.categories.category import Category as Category
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.realizations import RealizationsCategory as RealizationsCategory
from sage.categories.super_modules import SuperModulesCategory as SuperModulesCategory
from sage.categories.tensor import TensorProductsCategory as TensorProductsCategory
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class HopfAlgebras(Category_over_base_ring):
    """
    The category of Hopf algebras.

    EXAMPLES::

        sage: HopfAlgebras(QQ)
        Category of Hopf algebras over Rational Field
        sage: HopfAlgebras(QQ).super_categories()
        [Category of bialgebras over Rational Field]

    TESTS::

        sage: TestSuite(HopfAlgebras(ZZ)).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: HopfAlgebras(QQ).super_categories()
            [Category of bialgebras over Rational Field]
        """
    def dual(self):
        """
        Return the dual category.

        EXAMPLES:

        The category of Hopf algebras over any field is self dual::

            sage: C = HopfAlgebras(QQ)
            sage: C.dual()
            Category of Hopf algebras over Rational Field
        """
    WithBasis: Incomplete
    class ElementMethods:
        def antipode(self):
            """
            Return the antipode of ``self``.

            EXAMPLES::

                sage: # needs sage.groups
                sage: A = HopfAlgebrasWithBasis(QQ).example(); A
                An example of Hopf algebra with basis: the group algebra of the
                 Dihedral group of order 6 as a permutation group over Rational Field
                sage: [a,b] = A.algebra_generators()
                sage: a, a.antipode()
                (B[(1,2,3)], B[(1,3,2)])
                sage: b, b.antipode()
                (B[(1,3)], B[(1,3)])

            TESTS::

                sage: all(x.antipode() * x == A.one() for x in A.basis())               # needs sage.groups
                True
            """
    class ParentMethods: ...
    class Morphism(Category):
        """
        The category of Hopf algebra morphisms.
        """
    class Super(SuperModulesCategory):
        """
        The category of super Hopf algebras.

        .. NOTE::

            A super Hopf algebra is *not* simply a Hopf
            algebra with a `\\ZZ/2\\ZZ` grading due to the
            signed bialgebra compatibility conditions.
        """
        def dual(self):
            """
            Return the dual category.

            EXAMPLES:

            The category of super Hopf algebras over any field is self dual::

                sage: C = HopfAlgebras(QQ).Super()
                sage: C.dual()
                Category of super Hopf algebras over Rational Field
            """
        class ElementMethods:
            def antipode(self):
                """
                Return the antipode of ``self``.

                EXAMPLES::

                    sage: A = SteenrodAlgebra(3)                                        # needs sage.combinat sage.modules
                    sage: a = A.an_element()                                            # needs sage.combinat sage.modules
                    sage: a, a.antipode()                                               # needs sage.combinat sage.modules
                    (2 Q_1 Q_3 P(2,1), Q_1 Q_3 P(2,1))
                """
    class TensorProducts(TensorProductsCategory):
        """
        The category of Hopf algebras constructed by tensor product of Hopf algebras
        """
        @cached_method
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: C = HopfAlgebras(QQ).TensorProducts()
                sage: C.extra_super_categories()
                [Category of Hopf algebras over Rational Field]
                sage: sorted(C.super_categories(), key=str)
                [Category of Hopf algebras over Rational Field,
                 Category of tensor products of algebras over Rational Field,
                 Category of tensor products of coalgebras over Rational Field]
            """
        class ParentMethods: ...
        class ElementMethods: ...
    class DualCategory(Category_over_base_ring):
        """
        The category of Hopf algebras constructed as dual of a Hopf algebra
        """
        class ParentMethods: ...
    class Realizations(RealizationsCategory):
        class ParentMethods:
            def antipode_by_coercion(self, x):
                """
                Return the image of ``x`` by the antipode.

                This default implementation coerces to the default
                realization, computes the antipode there, and coerces the
                result back.

                EXAMPLES::

                    sage: # needs sage.combinat sage.modules
                    sage: N = NonCommutativeSymmetricFunctions(QQ)
                    sage: R = N.ribbon()
                    sage: R.antipode_by_coercion.__module__
                    'sage.categories.hopf_algebras'
                    sage: R.antipode_by_coercion(R[1,3,1])
                    -R[2, 1, 2]
                """
