import _cython_3_2_1
import sage.libs.ntl.ntl_ZZ_pContext
import sage.rings.padics.pow_computer
from sage.misc.timing import cputime as cputime
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

PowComputer_ext_maker: _cython_3_2_1.cython_function_or_method
ZZ_pContext_factory: sage.libs.ntl.ntl_ZZ_pContext.ntl_ZZ_pContext_factory
ZZ_pX_eis_shift_test: _cython_3_2_1.cython_function_or_method

class PowComputer_ZZ_pX(PowComputer_ext):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def polynomial(self) -> Any:
        """PowComputer_ZZ_pX.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 747)

        Return the polynomial (with coefficient precision prec_cap) associated
        to this ``PowComputer``.

        The polynomial is output as an ntl_ZZ_pX.

        EXAMPLES::

            sage: PC = PowComputer_ext_maker(5, 5, 10, 20, False, ntl.ZZ_pX([-5,0,1],5^10), 'FM', 'e',ntl.ZZ_pX([1],5^10))
            sage: PC.polynomial()
            [9765620 0 1]"""
    @overload
    def polynomial(self, withcoefficientprecisionprec_cap) -> Any:
        """PowComputer_ZZ_pX.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 747)

        Return the polynomial (with coefficient precision prec_cap) associated
        to this ``PowComputer``.

        The polynomial is output as an ntl_ZZ_pX.

        EXAMPLES::

            sage: PC = PowComputer_ext_maker(5, 5, 10, 20, False, ntl.ZZ_pX([-5,0,1],5^10), 'FM', 'e',ntl.ZZ_pX([1],5^10))
            sage: PC.polynomial()
            [9765620 0 1]"""
    @overload
    def polynomial(self) -> Any:
        """PowComputer_ZZ_pX.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 747)

        Return the polynomial (with coefficient precision prec_cap) associated
        to this ``PowComputer``.

        The polynomial is output as an ntl_ZZ_pX.

        EXAMPLES::

            sage: PC = PowComputer_ext_maker(5, 5, 10, 20, False, ntl.ZZ_pX([-5,0,1],5^10), 'FM', 'e',ntl.ZZ_pX([1],5^10))
            sage: PC.polynomial()
            [9765620 0 1]"""
    def speed_test(self, n, runs) -> Any:
        """PowComputer_ZZ_pX.speed_test(self, n, runs)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 830)

        Run a speed test.

        INPUT:

        - ``n`` -- input to a function to be tested (the function needs to be
          set in the source code)
        - ``runs`` -- the number of runs of that function

        OUTPUT:

        - The time in seconds that it takes to call the function on ``n``,
          ``runs`` times.

        EXAMPLES::

            sage: PC = PowComputer_ext_maker(5, 10, 10, 20, False, ntl.ZZ_pX([-5, 0, 1], 5^10), 'small', 'e',ntl.ZZ_pX([1],5^10))
            sage: PC.speed_test(10, 10^6)  # random
            0.0090679999999991878"""

class PowComputer_ZZ_pX_FM(PowComputer_ZZ_pX):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 1217)

        This class only caches a context and modulus for p^prec_cap.

        Designed for use with fixed modulus `p`-adic rings, in Eisenstein
        and unramified extensions of `\\ZZ_p`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PowComputer_ZZ_pX_FM_Eis(PowComputer_ZZ_pX_FM):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 1315)

        This class computes and stores ``low_shifter`` and ``high_shifter``, which aid in right shifting elements.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PowComputer_ZZ_pX_big(PowComputer_ZZ_pX):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 1905)

        This class caches all contexts and moduli between 1 and cache_limit, and also caches for prec_cap.  In addition, it stores
        a dictionary of contexts and moduli of
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def reset_dictionaries(self) -> Any:
        """PowComputer_ZZ_pX_big.reset_dictionaries(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 1999)

        Reset the dictionaries.  Note that if there are elements
        lying around that need access to these dictionaries, calling
        this function and then doing arithmetic with those elements
        could cause trouble (if the context object gets garbage
        collected for example.  The bugs introduced could be very
        subtle, because NTL will generate a new context object and use
        it, but there's the potential for the object to be
        incompatible with the different context object).

        EXAMPLES::

            sage: A = PowComputer_ext_maker(5, 6, 10, 20, False, ntl.ZZ_pX([-5,0,1],5^10), 'big','e',ntl.ZZ_pX([1],5^10))
            sage: P = A._get_context_test(8)
            sage: A._context_dict()
            {8: NTL modulus 390625}
            sage: A.reset_dictionaries()
            sage: A._context_dict()
            {}"""

class PowComputer_ZZ_pX_big_Eis(PowComputer_ZZ_pX_big):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 2175)

        This class computes and stores ``low_shifter`` and ``high_shifter``, which
        aid in right shifting elements.
        These are only stored at maximal precision: in order to get lower precision
        versions just reduce mod p^n.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PowComputer_ZZ_pX_small(PowComputer_ZZ_pX):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 1541)

        This class caches contexts and moduli densely between 1 and cache_limit.  It requires cache_limit == prec_cap.

        It is intended for use with capped relative and capped absolute rings and fields, in Eisenstein and unramified
        extensions of the base `p`-adic fields.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PowComputer_ZZ_pX_small_Eis(PowComputer_ZZ_pX_small):
    """File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 1744)

        This class computes and stores ``low_shifter`` and ``high_shifter``, which aid in right shifting elements.
        These are only stored at maximal precision: in order to get lower precision versions just reduce mod p^n.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PowComputer_ext(sage.rings.padics.pow_computer.PowComputer_class):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __reduce__(self) -> Any:
        """PowComputer_ext.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/pow_computer_ext.pyx (starting at line 523)

        For pickling.

        EXAMPLES::

            sage: PC = PowComputer_ext_maker(5, 10, 10, 20, False, ntl.ZZ_pX([-5, 0, 1], 5^10), 'small', 'e',ntl.ZZ_pX([1],5^10)); PC
            PowComputer_ext for 5, with polynomial [9765620 0 1]
            sage: loads(dumps(PC))
            PowComputer_ext for 5, with polynomial [9765620 0 1]"""
