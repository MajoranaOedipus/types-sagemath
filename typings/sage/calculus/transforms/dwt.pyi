import _cython_3_2_1
import sage.libs.gsl.array
from typing import Any

DWT: _cython_3_2_1.cython_function_or_method
WaveletTransform: _cython_3_2_1.cython_function_or_method
is2pow: _cython_3_2_1.cython_function_or_method

class DiscreteWaveletTransform(sage.libs.gsl.array.GSLDoubleArray):
    """DiscreteWaveletTransform(size_t n, size_t stride, wavelet_type, size_t wavelet_k)

    File: /build/sagemath/src/sage/src/sage/calculus/transforms/dwt.pyx (starting at line 102)

    Discrete wavelet transform class."""
    def __init__(self, size_tn, size_tstride, wavelet_type, size_twavelet_k) -> Any:
        """File: /build/sagemath/src/sage/src/sage/calculus/transforms/dwt.pyx (starting at line 110)"""
    def backward_transform(self) -> Any:
        """DiscreteWaveletTransform.backward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/dwt.pyx (starting at line 137)"""
    def forward_transform(self) -> Any:
        """DiscreteWaveletTransform.forward_transform(self)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/dwt.pyx (starting at line 133)"""
    def plot(self, xmin=..., xmax=..., **args) -> Any:
        """DiscreteWaveletTransform.plot(self, xmin=None, xmax=None, **args)

        File: /build/sagemath/src/sage/src/sage/calculus/transforms/dwt.pyx (starting at line 141)"""
