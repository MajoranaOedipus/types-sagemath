import _cython_3_2_1
import sage.rings.power_series_poly as power_series_poly
import sage.rings.power_series_ring_element
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

make_powerseries_mpoly_v0: _cython_3_2_1.cython_function_or_method

class PowerSeries_mpoly(sage.rings.power_series_ring_element.PowerSeries):
    """PowerSeries_mpoly(parent, f=0, prec=infinity, int check=1, is_gen=0)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f=..., prec=..., intcheck=..., is_gen=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 18)

                EXAMPLES::

                    sage: S.<x> = QQ[]
                    sage: R.<y> = S[[]]
                    sage: f = x + 2*y + x*y
                    sage: loads(f.dumps()) == f
                    True
        """
    def do_truncation(self) -> Any:
        """PowerSeries_mpoly.do_truncation(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 83)"""
    def list(self) -> Any:
        """PowerSeries_mpoly.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 95)"""
    def polynomial(self) -> Any:
        """PowerSeries_mpoly.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 100)"""
    def __call__(self, *args, **kwds) -> Any:
        """PowerSeries_mpoly.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 76)"""
    def __iter__(self) -> Any:
        """PowerSeries_mpoly.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 119)

        Return an iterator over the coefficients of this power series."""
    def __neg__(self) -> Any:
        """PowerSeries_mpoly.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 125)

        Return the negative of this power series."""
    def __reduce__(self) -> Any:
        """PowerSeries_mpoly.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/power_series_mpoly.pyx (starting at line 72)"""
