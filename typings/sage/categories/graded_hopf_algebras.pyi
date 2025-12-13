def GradedHopfAlgebras(base_ring):
    """
    The category of graded Hopf algebras.

    EXAMPLES::

        sage: C = GradedHopfAlgebras(QQ); C
        Join of Category of Hopf algebras over Rational Field
            and Category of graded algebras over Rational Field
            and Category of graded coalgebras over Rational Field
        sage: C is HopfAlgebras(QQ).Graded()
        True

    TESTS::

        sage: TestSuite(C).run()

    .. NOTE::

        This is not a graded Hopf algebra as is typically defined
        in algebraic topology as the product in the tensor square
        `(x \\otimes y) (a \\otimes b) = (xa) \\otimes (yb)` does
        not carry an additional sign. For this, instead use
        :class:`super Hopf algebras
        <sage.categories.hopf_algebras.HopfAlgebras.Super>`.
    """
