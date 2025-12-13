from .constructor import EllipticCurve as EllipticCurve
from _typeshed import Incomplete
from sage.arith.misc import next_prime as next_prime, prime_divisors as prime_divisors, valuation as valuation
from sage.databases.cremona import parse_cremona_label as parse_cremona_label
from sage.misc.verbose import verbose as verbose
from sage.modular.cusps import Cusps as Cusps
from sage.modular.modsym.all import ModularSymbols as ModularSymbols
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

oo: Incomplete
zero: Incomplete

def modular_symbol_space(E, sign, base_ring, bound=None):
    """
    Create the space of modular symbols of a given sign over a give base_ring,
    attached to the isogeny class of the elliptic curve ``E``.

    INPUT:

    - ``E`` -- an elliptic curve over `\\QQ`
    - ``sign`` -- integer; -1, 0, or 1
    - ``base_ring`` -- ring
    - ``bound`` -- (default: ``None``) maximum number of Hecke operators to
      use to cut out modular symbols factor.  If ``None``, use
      enough to provably get the correct answer.

    OUTPUT: a space of modular symbols

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_modular_symbols import modular_symbol_space
        sage: E = EllipticCurve('11a1')
        sage: M = modular_symbol_space(E, -1, GF(37))
        sage: M
        Modular Symbols space of dimension 1 for Gamma_0(11) of weight 2 with sign -1
         over Finite Field of size 37
    """

class ModularSymbol(SageObject):
    """
    A modular symbol attached to an elliptic curve, which is the map
    `\\QQ\\to \\QQ` obtained by sending `r` to the normalized
    symmetrized (or anti-symmetrized) integral `\\infty` to `r`.

    This is as defined in [MTT1986]_, but normalized to depend on the curve
    and not only its isogeny class as in [SW2013]_.

    See the documentation of ``E.modular_symbol()`` in elliptic curves
    over the rational numbers for help.
    """
    def sign(self):
        """
        Return the sign of this elliptic curve modular symbol.

        EXAMPLES::

            sage: m = EllipticCurve('11a1').modular_symbol()
            sage: m.sign()
            1
            sage: m = EllipticCurve('11a1').modular_symbol(sign=-1, implementation='sage')
            sage: m.sign()
            -1
        """
    def elliptic_curve(self):
        """
        Return the elliptic curve of this modular symbol.

        EXAMPLES::

            sage: m = EllipticCurve('11a1').modular_symbol()
            sage: m.elliptic_curve()
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
        """
    def base_ring(self):
        """
        Return the base ring for this modular symbol.

        EXAMPLES::

            sage: m = EllipticCurve('11a1').modular_symbol()
            sage: m.base_ring()
            Rational Field
        """

class ModularSymbolECLIB(ModularSymbol):
    cache: Incomplete
    def __init__(self, E, sign, nap: int = 1000) -> None:
        """Modular symbols attached to `E` using ``eclib``.

        Note that the normalization used within ``eclib`` differs from the
        normalization chosen here by a factor of 2 in the case of elliptic
        curves with negative discriminant (with one real component) since
        the convention there is to write the above integral as
        `[r]^{+}x+[r]^{-}yi`, where the lattice is `\\left<2x,x+yi\\right>`,
        so that `\\Omega^{+}=2x` and `\\Omega^{-}=2yi`.  We
        allow for this below.

        INPUT:

        - ``E`` -- an elliptic curve

        - ``sign`` -- integer; -1 or 1

        - ``nap`` -- integer (default: 1000); the number of ap of E to use
          in determining the normalisation of the modular symbols

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_modular_symbols import ModularSymbolECLIB
            sage: E = EllipticCurve('11a1')
            sage: M = ModularSymbolECLIB(E,+1)
            sage: M
            Modular symbol with sign 1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: M(0)
            1/5
            sage: E = EllipticCurve('11a2')
            sage: M = ModularSymbolECLIB(E,+1)
            sage: M(0)
            1

        This is a rank 1 case with vanishing positive twists::

            sage: E = EllipticCurve('121b1')
            sage: M = ModularSymbolECLIB(E,+1)
            sage: M(0)
            0
            sage: M(1/7)
            1/2

            sage: M = EllipticCurve('121d1').modular_symbol(implementation='eclib')
            sage: M(0)
            2

            sage: E = EllipticCurve('15a1')
            sage: [C.modular_symbol(implementation='eclib')(0) for C in E.isogeny_class()]
            [1/4, 1/8, 1/4, 1/2, 1/8, 1/16, 1/2, 1]

        Since :issue:`10256`, the interface for negative modular symbols in eclib is available::

            sage: E = EllipticCurve('11a1')
            sage: Mplus = E.modular_symbol(+1); Mplus
            Modular symbol with sign 1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: [Mplus(1/i) for i in [1..11]]
            [1/5, -4/5, -3/10, 7/10, 6/5, 6/5, 7/10, -3/10, -4/5, 1/5, 0]
            sage: Mminus = E.modular_symbol(-1); Mminus
            Modular symbol with sign -1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: [Mminus(1/i) for i in [1..11]]
            [0, 0, 1/2, 1/2, 0, 0, -1/2, -1/2, 0, 0, 0]

        The scaling factor relative to eclib's normalization is 1/2 for curves of negative discriminant::

            sage: [E.discriminant() for E in cremona_curves([14])]
            [-21952, 941192, -1835008, -28, 25088, 98]
            sage: [E.modular_symbol()._scaling for E in cremona_curves([14])]
            [1/2, 1, 1/2, 1/2, 1, 1]

        TESTS (for :issue:`10236`)::

            sage: E = EllipticCurve('11a1')
            sage: m = E.modular_symbol(implementation='eclib')
            sage: m(1/7)
            7/10
            sage: m(0)
            1/5

        If ``nap`` is too small, the normalization in eclib used to be
        incorrect (see :issue:`31317`), but since ``eclib`` version
        v20210310 the value of ``nap`` is increased automatically by
        ``eclib``::

            sage: from sage.schemes.elliptic_curves.ell_modular_symbols import ModularSymbolECLIB
            sage: E = EllipticCurve('1590g1')
            sage: m = ModularSymbolECLIB(E, sign=+1, nap=300)
            sage: [m(a/5) for a in [1..4]]
            [13/2, -13/2, -13/2, 13/2]

        These values are correct, and increasing ``nap`` has no
        effect.  The correct values may verified by the numerical
        implementation::

            sage: m = ModularSymbolECLIB(E, sign=+1, nap=400)
            sage: [m(a/5) for a in [1..4]]
            [13/2, -13/2, -13/2, 13/2]
            sage: m = E.modular_symbol(implementation='num')
            sage: [m(a/5) for a in [1..4]]
            [13/2, -13/2, -13/2, 13/2]
        """
    def __call__(self, r, base_at_infinity: bool = True):
        """
        Evaluates the modular symbol at {0,`r`} or {oo,`r`}.

        EXAMPLES::

            sage: m = EllipticCurve('11a1').modular_symbol(implementation='eclib')
            sage: m(0)
            1/5
        """

class ModularSymbolSage(ModularSymbol):
    def __init__(self, E, sign, normalize: str = 'L_ratio') -> None:
        """Modular symbols attached to `E` using ``sage``.

        INPUT:

        - ``E`` -- an elliptic curve
        - ``sign`` -- integer; -1 or 1
        - ``normalize`` -- either ``'L_ratio'`` (default), ``'period'``, or
          ``'none'``; For ``'L_ratio'``, the modular symbol is correctly
          normalized by comparing it to the quotient of `L(E,1)` by
          the least positive period for the curve and some small
          twists.  The normalization ``'period'`` uses the
          integral_period_map for modular symbols and is known to be
          equal to the above normalization up to the sign and a
          possible power of 2.  For ``'none'``, the modular symbol is
          almost certainly not correctly normalized, i.e. all values
          will be a fixed scalar multiple of what they should be.  But
          the initial computation of the modular symbol is much
          faster, though evaluation of it after computing it won't be
          any faster.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: from sage.schemes.elliptic_curves.ell_modular_symbols import ModularSymbolSage
            sage: M = ModularSymbolSage(E, +1)
            sage: M
            Modular symbol with sign 1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: M(0)
            1/5
            sage: E = EllipticCurve('11a2')
            sage: M = ModularSymbolSage(E, +1)
            sage: M(0)
            1
            sage: M = ModularSymbolSage(E, -1)
            sage: M(1/3)
            1/2

        This is a rank 1 case with vanishing positive twists.
        The modular symbol is adjusted by -2::

            sage: E = EllipticCurve('121b1')
            sage: M = ModularSymbolSage(E, -1, normalize='L_ratio')
            sage: M(1/3)
            1
            sage: M._scaling
            1

            sage: M = EllipticCurve('121d1').modular_symbol(implementation='sage')
            sage: M(0)
            2
            sage: M = EllipticCurve('121d1').modular_symbol(implementation='sage',
            ....:                                           normalize='none')
            sage: M(0)
            1

            sage: E = EllipticCurve('15a1')
            sage: [C.modular_symbol(implementation='sage', normalize='L_ratio')(0)
            ....:  for C in E.isogeny_class()]
            [1/4, 1/8, 1/4, 1/2, 1/8, 1/16, 1/2, 1]
            sage: [C.modular_symbol(implementation='sage', normalize='period')(0)
            ....:  for C in E.isogeny_class()]
            [1/8, 1/16, 1/8, 1/4, 1/16, 1/32, 1/4, 1/2]
            sage: [C.modular_symbol(implementation='sage', normalize='none')(0)
            ....:  for C in E.isogeny_class()]
            [1, 1, 1, 1, 1, 1, 1, 1]
        """
    def __lalg__(self, D):
        """
        For positive `D`, this function evaluates the quotient
        `L(E_D,1)\\cdot \\sqrt(D)/\\Omega_E` where `E_D` is the twist of
        `E` by `D`, `\\Omega_E` is the least positive period of `E`.

        For negative `E`, it is the quotient
        `L(E_D,1)\\cdot \\sqrt(-D)/\\Omega^{-}_E`
        where `\\Omega^{-}_E` is the least positive imaginary part of a
        non-real period of `E`.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: m = E.modular_symbol(sign=+1, implementation='sage')
            sage: m.__lalg__(1)
            1/5
            sage: m.__lalg__(3)
            5/2
        """
    def __call__(self, r, base_at_infinity: bool = True):
        """
        Evaluates the modular symbol at {0,`r`} or {oo,`r`}.

        EXAMPLES::

            sage: m = EllipticCurve('11a1').modular_symbol(implementation='sage')
            sage: m(0)
            1/5
        """
