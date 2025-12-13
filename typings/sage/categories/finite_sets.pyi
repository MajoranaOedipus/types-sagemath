from sage.categories.algebra_functor import AlgebrasCategory as AlgebrasCategory
from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom
from sage.categories.subquotients import SubquotientsCategory as SubquotientsCategory

class FiniteSets(CategoryWithAxiom):
    """
    The category of finite sets.

    EXAMPLES::

        sage: C = FiniteSets(); C
        Category of finite sets
        sage: C.super_categories()
        [Category of sets]
        sage: C.all_super_categories()
        [Category of finite sets,
         Category of sets,
         Category of sets with partial maps,
         Category of objects]
        sage: C.example()
        NotImplemented

    TESTS::

        sage: TestSuite(C).run()
        sage: C is Sets().Finite()
        True
    """
    class ParentMethods:
        def is_finite(self):
            """
            Return ``True`` since ``self`` is finite.

            EXAMPLES::

                sage: C = FiniteEnumeratedSets().example()
                sage: C.is_finite()
                True
            """
    class Subquotients(SubquotientsCategory):
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: FiniteSets().Subquotients().extra_super_categories()
                [Category of finite sets]

            This implements the fact that a subquotient (and therefore
            a quotient or subobject) of a finite set is finite::

                sage: FiniteSets().Subquotients().is_subcategory(FiniteSets())
                True
                sage: FiniteSets().Quotients   ().is_subcategory(FiniteSets())
                True
                sage: FiniteSets().Subobjects  ().is_subcategory(FiniteSets())
                True
            """
    class Algebras(AlgebrasCategory):
        def extra_super_categories(self):
            """
            EXAMPLES::

                sage: FiniteSets().Algebras(QQ).extra_super_categories()
                [Category of finite dimensional vector spaces with basis over Rational Field]

            This implements the fact that the algebra of a finite set
            is finite dimensional::

                sage: FiniteMonoids().Algebras(QQ).is_subcategory(AlgebrasWithBasis(QQ).FiniteDimensional())
                True
            """
