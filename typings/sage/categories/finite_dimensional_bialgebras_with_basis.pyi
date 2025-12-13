def FiniteDimensionalBialgebrasWithBasis(base_ring):
    """
    The category of finite dimensional bialgebras with a distinguished basis.

    EXAMPLES::

        sage: C = FiniteDimensionalBialgebrasWithBasis(QQ); C
        Category of finite dimensional bialgebras with basis over Rational Field
        sage: sorted(C.super_categories(), key=str)
        [Category of bialgebras with basis over Rational Field,
         Category of finite dimensional algebras with basis over Rational Field]
        sage: C is Bialgebras(QQ).WithBasis().FiniteDimensional()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
