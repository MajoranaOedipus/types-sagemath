def MonoidAlgebras(base_ring):
    """
    The category of monoid algebras over ``base_ring``.

    EXAMPLES::

        sage: C = MonoidAlgebras(QQ); C
        Category of monoid algebras over Rational Field
        sage: sorted(C.super_categories(), key=str)
        [Category of bialgebras with basis over Rational Field,
         Category of semigroup algebras over Rational Field,
         Category of unital magma algebras over Rational Field]

    This is just an alias for::

        sage: C is Monoids().Algebras(QQ)
        True

    TESTS::

        sage: TestSuite(MonoidAlgebras(ZZ)).run()
    """
