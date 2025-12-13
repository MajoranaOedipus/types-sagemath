from .derivations import FunctionFieldDerivation as FunctionFieldDerivation

class FunctionFieldDerivation_rational(FunctionFieldDerivation):
    """
    Derivations on rational function fields.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: K.derivation()
        d/dx
    """
    def __init__(self, parent, u=None) -> None:
        """
        Initialize a derivation.

        INPUT:

        - ``parent`` -- the parent of this derivation

        - ``u`` -- a parameter describing the derivation

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: d = K.derivation()
            sage: TestSuite(d).run()

        The parameter ``u`` can be the name of the variable::

            sage: K.derivation(x)
            d/dx

        or a list of length one whose unique element is the image
        of the generator of the underlying function field::

            sage: K.derivation([x^2])
            x^2*d/dx
        """
