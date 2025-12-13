import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes

setup_NTL_error_callback: _cython_3_2_1.cython_function_or_method

class NTLError(RuntimeError):
    """File: /build/sagemath/src/sage/src/sage/libs/ntl/error.pyx (starting at line 34)

        Exceptions from the NTL library.

        EXAMPLES::

            sage: a = ntl.ZZX([0])
            sage: a.quo_rem(a)
            Traceback (most recent call last):
            ...
            NTLError: DivRem: division by zero
    """
