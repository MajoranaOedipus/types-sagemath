from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom

class FiniteWeylGroups(CategoryWithAxiom):
    """
    The category of finite Weyl groups.

    EXAMPLES::

        sage: C = FiniteWeylGroups()
        sage: C
        Category of finite Weyl groups
        sage: C.super_categories()
        [Category of finite Coxeter groups, Category of Weyl groups]
        sage: C.example()
        The symmetric group on {0, ..., 3}

    TESTS::

        sage: W = FiniteWeylGroups().example()
        sage: TestSuite(W).run()
    """
    class ParentMethods: ...
    class ElementMethods: ...
