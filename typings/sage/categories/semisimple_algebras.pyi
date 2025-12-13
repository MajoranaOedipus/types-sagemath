from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.category_types import Category_over_base_ring as Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring as CategoryWithAxiom_over_base_ring
from sage.misc.bindable_class import BoundClass as BoundClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import LazyImport as LazyImport

class SemisimpleAlgebras(Category_over_base_ring):
    """
    The category of semisimple algebras over a given base ring.

    EXAMPLES::

        sage: from sage.categories.semisimple_algebras import SemisimpleAlgebras
        sage: C = SemisimpleAlgebras(QQ); C
        Category of semisimple algebras over Rational Field

    This category is best constructed as::

        sage: D = Algebras(QQ).Semisimple(); D
        Category of semisimple algebras over Rational Field
        sage: D is C
        True

        sage: C.super_categories()
        [Category of algebras over Rational Field]

    Typically, finite group algebras are semisimple::

        sage: DihedralGroup(5).algebra(QQ) in SemisimpleAlgebras                        # needs sage.groups
        True

    Unless the characteristic of the field divides the order of the group::

        sage: DihedralGroup(5).algebra(IntegerModRing(5)) in SemisimpleAlgebras         # needs sage.groups
        False

        sage: DihedralGroup(5).algebra(IntegerModRing(7)) in SemisimpleAlgebras         # needs sage.groups
        True

    .. SEEALSO:: :wikipedia:`Semisimple_algebra`

    TESTS::

        sage: TestSuite(C).run()
    """
    @staticmethod
    def __classget__(cls, base_category, base_category_class):
        """
        Implement the shorthand ``Algebras(K).Semisimple()`` for ``SemisimpleAlgebras(K)``.

        This magic mimics the syntax of axioms for a smooth transition
        if ``Semisimple`` becomes one.

        EXAMPLES::

            sage: Algebras(QQ).Semisimple()
            Category of semisimple algebras over Rational Field
            sage: Algebras.Semisimple
            <class 'sage.categories.semisimple_algebras.SemisimpleAlgebras'>
        """
    @cached_method
    def super_categories(self):
        """
        EXAMPLES::

            sage: Algebras(QQ).Semisimple().super_categories()
            [Category of algebras over Rational Field]
        """
    class ParentMethods:
        def radical_basis(self, **keywords):
            """
            Return a basis of the Jacobson radical of this algebra.

            - ``keywords`` -- for compatibility; ignored

            OUTPUT: the empty list since this algebra is semisimple

            EXAMPLES::

                sage: A = SymmetricGroup(4).algebra(QQ)                                 # needs sage.combinat sage.groups
                sage: A.radical_basis()                                                 # needs sage.combinat sage.groups
                ()

            TESTS::

                sage: A.radical_basis.__module__                                        # needs sage.combinat sage.groups
                'sage.categories.finite_dimensional_semisimple_algebras_with_basis'
            """
    class FiniteDimensional(CategoryWithAxiom_over_base_ring):
        WithBasis: Incomplete
