import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

__pyx_capi__: dict
prime_range: _cython_3_2_1.cython_function_or_method

class arith_int:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def gcd_int(self, inta, intb) -> Any:
        """arith_int.gcd_int(self, int a, int b)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 246)"""
    def inverse_mod_int(self, inta, intm) -> Any:
        """arith_int.inverse_mod_int(self, int a, int m)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 310)"""
    def rational_recon_int(self, inta, intm) -> Any:
        """arith_int.rational_recon_int(self, int a, int m)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 370)

        Rational reconstruction of a modulo m."""
    def xgcd_int(self, inta, intb) -> Any:
        """arith_int.xgcd_int(self, int a, int b)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 293)"""

class arith_llong:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def gcd_longlong(self, longlonga, longlongb) -> Any:
        """arith_llong.gcd_longlong(self, long long a, long long b)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 408)"""
    def inverse_mod_longlong(self, longlonga, longlongm) -> Any:
        """arith_llong.inverse_mod_longlong(self, long long a, long long m)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 467)"""
    def rational_recon_longlong(self, longlonga, longlongm) -> Any:
        """arith_llong.rational_recon_longlong(self, long long a, long long m)

        File: /build/sagemath/src/sage/src/sage/rings/fast_arith.pyx (starting at line 528)

        Rational reconstruction of a modulo m."""
