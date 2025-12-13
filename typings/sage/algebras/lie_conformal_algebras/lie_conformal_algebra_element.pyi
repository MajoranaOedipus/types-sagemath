from sage.arith.misc import factorial as factorial
from sage.misc.latex import latex as latex
from sage.misc.misc_c import prod as prod
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement as IndexedFreeModuleElement

class LCAWithGeneratorsElement(IndexedFreeModuleElement):
    """
    The element class of a Lie conformal algebra with a
    preferred set of generators.
    """
    def T(self, n: int = 1):
        """
        The `n`-th derivative of this element.

        INPUT:

        - ``n`` -- nonnegative integer (default: `1`); how many
          times to apply `T` to this element

        We use the *divided powers* notation
        `T^{(j)} = \\frac{T^j}{j!}`.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(QQ)
            sage: Vir.inject_variables()
            Defining L, C
            sage: L.T()
            TL
            sage: L.T(3)
            6*T^(3)L
            sage: C.T()
            0

            sage: R = lie_conformal_algebras.NeveuSchwarz(QQbar); R.inject_variables()
            Defining L, G, C
            sage: (L + 2*G.T() + 4*C).T(2)
            2*T^(2)L + 12*T^(3)G
        """
    def is_monomial(self):
        """
        Whether this element is a monomial.

        EXAMPLES::

            sage: Vir = lie_conformal_algebras.Virasoro(QQ); L = Vir.0
            sage: (L + L.T()).is_monomial()
            False
            sage: L.T().is_monomial()
            True
        """

class LCAStructureCoefficientsElement(LCAWithGeneratorsElement):
    """
    An element of a Lie conformal algebra given by structure
    coefficients.
    """
