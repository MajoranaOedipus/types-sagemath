from .eisenstein_extension_generic import EisensteinExtensionGeneric as EisensteinExtensionGeneric
from .generic_nodes import pAdicCappedAbsoluteRingGeneric as pAdicCappedAbsoluteRingGeneric, pAdicCappedRelativeFieldGeneric as pAdicCappedRelativeFieldGeneric, pAdicCappedRelativeRingGeneric as pAdicCappedRelativeRingGeneric, pAdicFixedModRingGeneric as pAdicFixedModRingGeneric, pAdicFloatingPointFieldGeneric as pAdicFloatingPointFieldGeneric, pAdicFloatingPointRingGeneric as pAdicFloatingPointRingGeneric
from .pow_computer_relative import PowComputer_relative_maker as PowComputer_relative_maker
from .relative_ramified_CA import RelativeRamifiedCappedAbsoluteElement as RelativeRamifiedCappedAbsoluteElement
from .relative_ramified_CR import RelativeRamifiedCappedRelativeElement as RelativeRamifiedCappedRelativeElement
from .relative_ramified_FM import RelativeRamifiedFixedModElement as RelativeRamifiedFixedModElement
from .relative_ramified_FP import RelativeRamifiedFloatingPointElement as RelativeRamifiedFloatingPointElement
from _typeshed import Incomplete
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import Morphism as Morphism

class pAdicRelativeBaseringInjection(Morphism):
    """
    The injection of the unramified base into the two-step extension.

    INPUT:

    - ``R`` -- an unramified `p`-adic ring or field
    - ``S`` -- an eisenstein extension of ``R``

    EXAMPLES::

        sage: # needs sage.libs.ntl
        sage: K.<a> = Qq(125)
        sage: R.<x> = K[]
        sage: W.<w> = K.extension(x^3 + 15*a*x - 5*(1+a^2))
        sage: f = W.coerce_map_from(K); f
        Generic morphism:
          From: 5-adic Unramified Extension Field in a defined by x^3 + 3*x + 3
          To:   5-adic Eisenstein Extension Field in w defined by x^3 + 15*a*x - 5*a^2 - 5 over its base field
    """
    def __init__(self, R, S) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(125)
            sage: R.<x> = K[]
            sage: W.<w> = K.extension(x^3 + 15*a*x - 5*(1+a^2))
            sage: f = W.coerce_map_from(K)
            sage: type(f)
            <class 'sage.rings.padics.relative_extension_leaves.pAdicRelativeBaseringInjection'>
        """
    def section(self):
        """
        Map back to the base ring.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(125,2)
            sage: R.<x> = K[]
            sage: W.<w> = K.extension(x^3 + 15*a*x - 5*(1+a^2))
            sage: f = W.coerce_map_from(K)
            sage: g = f.section()
            sage: g(a + w - w)
            a + O(5^2)
        """

class pAdicRelativeBaseringSection(Morphism):
    """
    The map from a two-step extension back to its maximal unramified subextension.

    EXAMPLES::

        sage: # needs sage.libs.ntl
        sage: K.<a> = Qq(2^10)
        sage: R.<x> = K[]
        sage: W.<w> = K.extension(x^4 + 2*a*x^2 - 16*x - 6)
        sage: f = K.convert_map_from(W); f
        Generic morphism:
          From: 2-adic Eisenstein Extension Field in w defined by x^4 + 2*a*x^2 - 16*x - 6 over its base field
          To:   2-adic Unramified Extension Field in a defined by x^10 + x^6 + x^5 + x^3 + x^2 + x + 1
    """
    def __init__(self, S, R) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(2^10)
            sage: R.<x> = K[]
            sage: W.<w> = K.extension(x^4 + 2*a*x^2 - 16*x - 6*a)
            sage: f = K.convert_map_from(W); type(f)
            <class 'sage.rings.padics.relative_extension_leaves.pAdicRelativeBaseringSection'>
        """

class RelativeRamifiedExtensionRingFixedMod(EisensteinExtensionGeneric, pAdicFixedModRingGeneric):
    """
    Two-step extension ring with fixed-mod precision.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: A.<a> = ZqFM(2^10)
        sage: R.<x> = A[]
        sage: W.<w> = A.extension(x^4 + 2*a*x^2 - 16*x - 6*a); W
        2-adic Eisenstein Extension Ring in w defined by x^4 + 2*a*x^2 - 16*x - 6*a over its base ring
        sage: w^4 + 2*a*w^2 - 16*w - 6*a == 0
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: A.<a> = ZqFM(5^4)
            sage: R.<x> = A[]
            sage: W.<w> = A.extension(x^3 - 25*(a+1)*x + 10*(a^2+2))
            sage: TestSuite(W).run(max_samples=16)      # long time
        """

class RelativeRamifiedExtensionRingCappedAbsolute(EisensteinExtensionGeneric, pAdicCappedAbsoluteRingGeneric):
    """
    Two-step extension ring with capped absolute precision.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: A.<a> = ZqCA(2^10)
        sage: R.<x> = A[]
        sage: W.<w> = A.extension(x^4 + 2*a*x^2 - 16*x - 6*a); W
        2-adic Eisenstein Extension Ring in w defined by x^4 + 2*a*x^2 - 16*x - 6*a over its base ring
        sage: w^4 + 2*a*w^2 - 16*w - 6*a == 0
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: A.<a> = ZqCA(5^4)
            sage: R.<x> = A[]
            sage: W.<w> = A.extension(x^3 - 25*(a+1)*x + 10*(a^2+2))
            sage: TestSuite(W).run(max_samples=16)      # long time
        """

class RelativeRamifiedExtensionRingCappedRelative(EisensteinExtensionGeneric, pAdicCappedRelativeRingGeneric):
    """
    Two-step extension ring with capped relative precision.

    EXAMPLES::

        sage: # needs sage.libs.ntl
        sage: A.<a> = ZqCR(2^10)
        sage: R.<x> = A[]
        sage: W.<w> = A.extension(x^4 + 2*a*x^2 - 16*x - 6*a); W
        2-adic Eisenstein Extension Ring in w defined by x^4 + 2*a*x^2 - 16*x - 6*a over its base ring
        sage: w^4 + 2*a*w^2 - 16*w - 6*a == 0
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: A.<a> = ZqCR(5^4)
            sage: R.<x> = A[]
            sage: W.<w> = A.extension(x^3 - 25*(a+1)*x + 10*(a^2+2))
            sage: TestSuite(W).run(max_samples=16)      # long time
        """

class RelativeRamifiedExtensionFieldCappedRelative(EisensteinExtensionGeneric, pAdicCappedRelativeFieldGeneric):
    """
    Two-step extension field with capped relative precision.

    EXAMPLES::

        sage: # needs sage.libs.ntl
        sage: A.<a> = QqCR(2^10)
        sage: R.<x> = A[]
        sage: W.<w> = A.extension(x^4 + 2*a*x^2 - 16*x - 6*a); W
        2-adic Eisenstein Extension Field in w defined by x^4 + 2*a*x^2 - 16*x - 6*a over its base field
        sage: w^4 + 2*a*w^2 - 16*w - 6*a == 0
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: A.<a> = QqCR(5^4)
            sage: R.<x> = A[]
            sage: W.<w> = A.extension(x^3 - 25*(a+1)*x + 10*(a^2+2))
            sage: TestSuite(W).run(max_samples=16)      # long time
        """

class RelativeRamifiedExtensionRingFloatingPoint(EisensteinExtensionGeneric, pAdicFloatingPointRingGeneric):
    """
    Two-step extension ring with floating point precision.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: A.<a> = ZqFP(2^10)
        sage: R.<x> = A[]
        sage: W.<w> = A.extension(x^4 + 2*a*x^2 - 16*x - 6*a); W
        2-adic Eisenstein Extension Ring in w defined by x^4 + 2*a*x^2 - 16*x - 6*a over its base ring
        sage: w^4 + 2*a*w^2 - 16*w - 6*a == 0
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: A.<a> = ZqFP(5^4)
            sage: R.<x> = A[]
            sage: W.<w> = A.extension(x^3 - 25*(a+1)*x + 10*(a^2+2))
            sage: TestSuite(W).run(max_samples=16)      # long time
        """

class RelativeRamifiedExtensionFieldFloatingPoint(EisensteinExtensionGeneric, pAdicFloatingPointFieldGeneric):
    """
    Two-step extension field with floating point precision.

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: A.<a> = QqFP(2^10)
        sage: R.<x> = A[]
        sage: W.<w> = A.extension(x^4 + 2*a*x^2 - 16*x - 6*a); W
        2-adic Eisenstein Extension Field in w defined by x^4 + 2*a*x^2 - 16*x - 6*a over its base field
        sage: w^4 + 2*a*w^2 - 16*w - 6*a == 0
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, approx_modulus, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: A.<a> = QqFP(5^4)
            sage: R.<x> = A[]
            sage: W.<w> = A.extension(x^3 - 25*(a+1)*x + 10*(a^2+2))
            sage: TestSuite(W).run(max_samples=16)      # long time
        """
