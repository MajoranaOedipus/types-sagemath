from sage.rings.derivation import RingDerivationWithoutTwist as RingDerivationWithoutTwist

class FunctionFieldDerivation(RingDerivationWithoutTwist):
    """
    Base class for derivations on function fields.

    A derivation on `R` is a map `R \\to R` with
    `D(\\alpha+\\beta)=D(\\alpha)+D(\\beta)` and `D(\\alpha\\beta)=\\beta
    D(\\alpha)+\\alpha D(\\beta)` for all `\\alpha,\\beta\\in R`.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: d = K.derivation()
        sage: d
        d/dx
    """
    def __init__(self, parent) -> None:
        """
        Initialize a derivation.

        INPUT:

        - ``parent`` -- the differential module in which this
          derivation lives

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: d = K.derivation()
            sage: TestSuite(d).run()
        """
    def is_injective(self) -> bool:
        """
        Return ``False`` since a derivation is never injective.

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: d = K.derivation()
            sage: d.is_injective()
            False
        """
