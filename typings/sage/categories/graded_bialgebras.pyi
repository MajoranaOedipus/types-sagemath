def GradedBialgebras(base_ring):
    """
    The category of graded bialgebras.

    EXAMPLES::

        sage: C = GradedBialgebras(QQ); C
        Join of Category of graded algebras over Rational Field
            and Category of bialgebras over Rational Field
            and Category of graded coalgebras over Rational Field
        sage: C is Bialgebras(QQ).Graded()
        True

    TESTS::

        sage: TestSuite(C).run()
    """
