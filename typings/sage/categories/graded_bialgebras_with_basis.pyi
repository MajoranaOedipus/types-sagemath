def GradedBialgebrasWithBasis(base_ring):
    """
    The category of graded bialgebras with a distinguished basis.

    EXAMPLES::

        sage: C = GradedBialgebrasWithBasis(QQ); C
        Join of Category of ...
        sage: sorted(C.super_categories(), key=str)
        [Category of bialgebras with basis over Rational Field,
         Category of graded algebras with basis over Rational Field,
         Category of graded coalgebras with basis over Rational Field]

    TESTS::

        sage: TestSuite(C).run()
    """
