from typing import Any

class GSLDoubleArray:
    """GSLDoubleArray(size_t n, size_t stride=1, data=None)

    File: /build/sagemath/src/sage/src/sage/libs/gsl/array.pyx (starting at line 7)

    EXAMPLES::

        sage: a = WaveletTransform(128,'daubechies',4)
        sage: for i in range(1, 11):
        ....:     a[i] = 1
        sage: a[:6:2]
        [0.0, 1.0, 1.0]"""
    def __init__(self, size_tn, size_tstride=..., data=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/gsl/array.pyx (starting at line 17)

                EXAMPLES::

                    sage: from sage.libs.gsl.array import GSLDoubleArray
                    sage: a = GSLDoubleArray(10)
        """
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, i) -> Any:
        """GSLDoubleArray.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/libs/gsl/array.pyx (starting at line 83)

        EXAMPLES::

            sage: from sage.libs.gsl.array import GSLDoubleArray
            sage: a = GSLDoubleArray(10)
            sage: for i in range(10):
            ....:     a[i] = i
            sage: a[3:7]
            [3.0, 4.0, 5.0, 6.0]"""
    def __len__(self) -> Any:
        """GSLDoubleArray.__len__(self)

        File: /build/sagemath/src/sage/src/sage/libs/gsl/array.pyx (starting at line 46)

        EXAMPLES::

            sage: from sage.libs.gsl.array import GSLDoubleArray
            sage: a = GSLDoubleArray(10)
            sage: len(a)
            10"""
    def __setitem__(self, size_ti, x) -> Any:
        """GSLDoubleArray.__setitem__(self, size_t i, x)

        File: /build/sagemath/src/sage/src/sage/libs/gsl/array.pyx (starting at line 68)

        EXAMPLES::

            sage: from sage.libs.gsl.array import GSLDoubleArray
            sage: a = GSLDoubleArray(10)
            sage: a[5] = 3
            sage: a
            [0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0]"""
