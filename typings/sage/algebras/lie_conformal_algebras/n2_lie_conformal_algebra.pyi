from .graded_lie_conformal_algebra import GradedLieConformalAlgebra as GradedLieConformalAlgebra

class N2LieConformalAlgebra(GradedLieConformalAlgebra):
    """
    The N=2 super Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative ring; the base ring of this super
      Lie conformal algebra

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: F.<x> = NumberField(x^2 - 2)
        sage: R = lie_conformal_algebras.N2(F); R
        The N=2 super Lie conformal algebra over Number Field in x with defining polynomial x^2 - 2
        sage: R.inject_variables()
        Defining L, J, G1, G2, C
        sage: G1.bracket(G2)
        {0: L + 1/2*TJ, 1: J, 2: 1/3*C}
        sage: G2.bracket(G1)
        {0: L - 1/2*TJ, 1: -J, 2: 1/3*C}
        sage: G1.degree()
        3/2
        sage: J.degree()
        1

    The topological twist is a Virasoro vector with central
    charge 0::

        sage: L2 = L - 1/2*J.T()
        sage: L2.bracket(L2) == {0: L2.T(), 1: 2*L2}
        True

    The sum of the fermions is a generator of the Neveu-Schwarz
    Lie conformal algebra::

        sage: G = (G1 + G2)
        sage: G.bracket(G)
        {0: 2*L, 2: 2/3*C}
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: V = lie_conformal_algebras.N2(QQ)
            sage: TestSuite(V).run()
        """
