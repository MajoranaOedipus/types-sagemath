def FiniteDimensionalCoalgebrasWithBasis(base_ring):
    """
    The category of finite dimensional coalgebras with a distinguished basis.

    EXAMPLES::

        sage: C = FiniteDimensionalCoalgebrasWithBasis(QQ); C
        Category of finite dimensional coalgebras with basis over Rational Field
        sage: sorted(C.super_categories(), key=str)
        [Category of coalgebras with basis over Rational Field,
         Category of finite dimensional vector spaces with basis over Rational Field]
        sage: C is Coalgebras(QQ).WithBasis().FiniteDimensional()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
