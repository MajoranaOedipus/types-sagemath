from .eisenstein_extension_generic import EisensteinExtensionGeneric as EisensteinExtensionGeneric
from .generic_nodes import pAdicCappedAbsoluteRingGeneric as pAdicCappedAbsoluteRingGeneric, pAdicCappedRelativeFieldGeneric as pAdicCappedRelativeFieldGeneric, pAdicCappedRelativeRingGeneric as pAdicCappedRelativeRingGeneric, pAdicFixedModRingGeneric as pAdicFixedModRingGeneric, pAdicFloatingPointFieldGeneric as pAdicFloatingPointFieldGeneric, pAdicFloatingPointRingGeneric as pAdicFloatingPointRingGeneric
from .padic_ZZ_pX_CA_element import pAdicZZpXCAElement as pAdicZZpXCAElement
from .padic_ZZ_pX_CR_element import pAdicZZpXCRElement as pAdicZZpXCRElement
from .padic_ZZ_pX_FM_element import pAdicZZpXFMElement as pAdicZZpXFMElement
from .qadic_flint_CA import qAdicCappedAbsoluteElement as qAdicCappedAbsoluteElement
from .qadic_flint_CR import qAdicCappedRelativeElement as qAdicCappedRelativeElement
from .qadic_flint_FM import qAdicFixedModElement as qAdicFixedModElement
from .qadic_flint_FP import qAdicFloatingPointElement as qAdicFloatingPointElement
from .unramified_extension_generic import UnramifiedExtensionGeneric as UnramifiedExtensionGeneric
from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.integer_ring import ZZ as ZZ

class UnramifiedExtensionRingCappedRelative(UnramifiedExtensionGeneric, pAdicCappedRelativeRingGeneric):
    """
    TESTS::

        sage: R.<a> = ZqCR(27,1000)                                                     # needs sage.libs.ntl
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.libs.ntl
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'FLINT') -> None:
        """
        A capped relative representation of `\\ZZ_q`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic ring.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name,
          unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R.<a> = ZqCR(27,10000); R  # indirect doctest                         # needs sage.libs.ntl
            3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1

            sage: R.<a> = ZqCR(next_prime(10^30)^3, 3); R.prime()                       # needs sage.libs.ntl
            1000000000000000000000000000057
        """

class UnramifiedExtensionFieldCappedRelative(UnramifiedExtensionGeneric, pAdicCappedRelativeFieldGeneric):
    """
    TESTS::

        sage: R.<a> = QqCR(27,1000)                                                     # needs sage.libs.ntl
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.libs.ntl
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'FLINT') -> None:
        """
        A representation of `\\QQ_q`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with rational coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic field.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name,
          unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R.<a> = Qq(27,10000); R  # indirect doctest                           # needs sage.libs.ntl
            3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1

            sage: R.<a> = Qq(next_prime(10^30)^3, 3); R.prime()                         # needs sage.libs.ntl
            1000000000000000000000000000057
        """

class UnramifiedExtensionRingCappedAbsolute(UnramifiedExtensionGeneric, pAdicCappedAbsoluteRingGeneric):
    """
    TESTS::

        sage: R.<a> = ZqCA(27,1000)                                                     # needs sage.libs.flint
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.libs.flint
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'FLINT') -> None:
        """
        A capped absolute representation of `ZZ_q`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic ring.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name,
          unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R.<a> = ZqCA(27,10000); R  # indirect doctest                         # needs sage.libs.flint
            3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1

            sage: R.<a> = ZqCA(next_prime(10^30)^3, 3); R.prime()                       # needs sage.libs.flint
            1000000000000000000000000000057
        """

class UnramifiedExtensionRingFixedMod(UnramifiedExtensionGeneric, pAdicFixedModRingGeneric):
    """
    TESTS::

        sage: R.<a> = ZqFM(27,1000)                                                     # needs sage.libs.flint
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)     # long time             # needs sage.libs.flint
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'FLINT') -> None:
        """
        A fixed modulus representation of Zq.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic field.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R.<a> = ZqFM(27,10000); R  # indirect doctest                         # needs sage.libs.flint
            3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1

            sage: R.<a> = ZqFM(next_prime(10^30)^3, 3); R.prime()                       # needs sage.libs.flint
            1000000000000000000000000000057
        """

class UnramifiedExtensionRingFloatingPoint(UnramifiedExtensionGeneric, pAdicFloatingPointRingGeneric):
    """
    TESTS::

        sage: R.<a> = ZqFP(27,10000); R == loads(dumps(R))                              # needs sage.libs.flint
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'FLINT') -> None:
        """
        A floating point representation of `\\ZZ_q`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in `\\ZZ_p`.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R.<a> = ZqFP(27,10000); R  # indirect doctest                         # needs sage.libs.flint
            3-adic Unramified Extension Ring in a defined by x^3 + 2*x + 1
            sage: R.<a> = ZqFP(next_prime(10^30)^3, 3); R.prime()                       # needs sage.libs.flint
            1000000000000000000000000000057

        TESTS:

        Check that :issue:`23228` has been resolved::

            sage: a % R.prime()                                                         # needs sage.libs.flint
            a
        """

class UnramifiedExtensionFieldFloatingPoint(UnramifiedExtensionGeneric, pAdicFloatingPointFieldGeneric):
    """
    TESTS::

        sage: R.<a> = QqFP(27,10000); R == loads(dumps(R))                              # needs sage.libs.flint
        True
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'FLINT') -> None:
        """
        A representation of `\\QQ_q`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with rational coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic field.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R.<a> = QqFP(27,10000); R  # indirect doctest                         # needs sage.libs.flint
            3-adic Unramified Extension Field in a defined by x^3 + 2*x + 1
            sage: R.<a> = Qq(next_prime(10^30)^3, 3); R.prime()                         # needs sage.libs.ntl
            1000000000000000000000000000057
        """

class EisensteinExtensionRingCappedRelative(EisensteinExtensionGeneric, pAdicCappedRelativeRingGeneric):
    """
    TESTS::

        sage: R = Zp(3, 1000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
        sage: W.<w> = R.ext(f)                                                          # needs sage.libs.ntl sage.rings.padics
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.geometry.polyhedron
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'NTL') -> None:
        """
        A capped relative representation of an Eisenstein extension of `\\ZZ_p`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic ring.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R = Zp(3, 10000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
            sage: W.<w> = R.ext(f); W  # indirect doctest                               # needs sage.libs.ntl
            3-adic Eisenstein Extension Ring in w defined by x^3 + 9*x - 3
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            30000

            sage: R.<p> = Zp(next_prime(10^30), 3, print_pos=False); S.<x> = ZZ[]; f = x^3 + p^2*x - p                  # needs sage.libs.ntl
            sage: W.<w> = R.ext(f); W.prime()                                           # needs sage.libs.ntl
            1000000000000000000000000000057
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            9
        """

class EisensteinExtensionFieldCappedRelative(EisensteinExtensionGeneric, pAdicCappedRelativeFieldGeneric):
    """
    TESTS::

        sage: R = Qp(3, 1000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
        sage: W.<w> = R.ext(f)                                                          # needs sage.libs.ntl
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.geometry.polyhedron
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'NTL') -> None:
        """
        A capped relative representation of an Eisenstein extension of `\\QQ_p`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with rational coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic field.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R = Qp(3, 10000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
            sage: W.<w> = R.ext(f); W  # indirect doctest                               # needs sage.libs.ntl
            3-adic Eisenstein Extension Field in w defined by x^3 + 9*x - 3
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            30000

            sage: R.<p> = Qp(next_prime(10^30), 3, print_pos=False); S.<x> = ZZ[]; f = x^3 + p^2*x - p                  # needs sage.libs.ntl
            sage: W.<w> = R.ext(f); W.prime()                                           # needs sage.libs.ntl
            1000000000000000000000000000057
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            9
        """

class EisensteinExtensionRingCappedAbsolute(EisensteinExtensionGeneric, pAdicCappedAbsoluteRingGeneric):
    """
    TESTS::

        sage: R = ZpCA(3, 1000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
        sage: W.<w> = R.ext(f)                                                          # needs sage.libs.ntl sage.rings.padics
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.geometry.polyhedron
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation) -> None:
        """
        A capped absolute representation of an Eisenstein extension of `\\ZZ_p`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic ring.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R = ZpCA(3, 10000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
            sage: W.<w> = R.ext(f); W                                                   # needs sage.libs.ntl
            3-adic Eisenstein Extension Ring in w defined by x^3 + 9*x - 3
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            30000

            sage: R.<p> = ZpCA(next_prime(10^30), 3, print_pos=False); S.<x> = ZZ[]; f = x^3 + p^2*x - p
            sage: W.<w> = R.ext(f); W.prime()                                           # needs sage.libs.ntl
            1000000000000000000000000000057
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            9
        """

class EisensteinExtensionRingFixedMod(EisensteinExtensionGeneric, pAdicFixedModRingGeneric):
    """
    TESTS::

        sage: R = ZpFM(3, 1000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
        sage: W.<w> = R.ext(f)                                                          # needs sage.libs.ntl sage.rings.padics
        sage: TestSuite(R).run(skip='_test_log',max_runs=4)                             # needs sage.geometry.polyhedron
    """
    prime_pow: Incomplete
    def __init__(self, exact_modulus, poly, prec, print_mode, shift_seed, names, implementation: str = 'NTL') -> None:
        """
        A fixed modulus representation of an eisenstein extension of `\\ZZ_p`.

        INPUT:

        - ``exact_modulus`` -- the original polynomial defining the extension.
          This could be a polynomial with integer coefficients, for example,
          while ``poly`` has coefficients in a `p`-adic ring.

        - ``poly`` -- the polynomial with coefficients in :meth:`base_ring`
          defining this extension

        - ``prec`` -- the precision cap of this ring

        - ``print_mode`` -- dictionary of print options

        - ``shift_seed`` -- unused

        - ``names`` -- a 4-tuple, ``(variable_name, residue_name, unramified_subextension_variable_name, uniformizer_name)``

        EXAMPLES::

            sage: R = ZpFM(3, 10000, print_pos=False); S.<x> = ZZ[]; f = x^3 + 9*x - 3
            sage: W.<w> = R.ext(f); W  # indirect doctest                               # needs sage.libs.ntl
            3-adic Eisenstein Extension Ring in w defined by x^3 + 9*x - 3
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            30000

            sage: R.<p> = ZpFM(next_prime(10^30), 3, print_pos=False); S.<x> = ZZ[]; f = x^3 + p^2*x - p
            sage: W.<w> = R.ext(f); W.prime()                                           # needs sage.libs.ntl
            1000000000000000000000000000057
            sage: W.precision_cap()                                                     # needs sage.libs.ntl
            9
        """
    def fraction_field(self) -> None:
        """
        Eisenstein extensions with fixed modulus do not support fraction fields.

        EXAMPLES::

            sage: S.<x> = ZZ[]
            sage: R.<a> = ZpFM(5).extension(x^2 - 5)                                    # needs sage.libs.ntl
            sage: R.fraction_field()                                                    # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            TypeError: This implementation of the p-adic ring
            does not support fields of fractions.
        """
