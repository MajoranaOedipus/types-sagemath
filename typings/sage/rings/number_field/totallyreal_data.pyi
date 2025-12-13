import _cython_3_2_1
from sage.arith.misc import binomial as binomial, gcd as gcd
from sage.categories.category import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import ZZx as ZZx
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict
easy_is_irreducible_py: _cython_3_2_1.cython_function_or_method
hermite_constant: _cython_3_2_1.cython_function_or_method
i: int
int_has_small_square_divisor: _cython_3_2_1.cython_function_or_method
lagrange_degree_3: _cython_3_2_1.cython_function_or_method
primessq_py: list

class tr_data:
    """tr_data(int n, B, a=[])

    File: /build/sagemath/src/sage/src/sage/rings/number_field/totallyreal_data.pyx (starting at line 443)

    This class encodes the data used in the enumeration of totally real
    fields.

    We do not give a complete description here.  For more information,
    see the attached functions; all of these are used internally by the
    functions in :mod:`.totallyreal`, so see that file for examples and
    further documentation."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, intn, B, a=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/totallyreal_data.pyx (starting at line 454)

                Initialization routine (constructor).

                INPUT:

                - ``n`` -- integer; the degree
                - ``B`` -- integer; the discriminant bound
                - ``a`` -- list (default: ``[]``); the coefficient list to begin with,
                  where ``a[len(a)]*x^n + ... + a[0]x^(n-len(a))``

                OUTPUT:

                the data initialized to begin enumeration of totally real fields
                with degree n, discriminant bounded by B, and starting with
                coefficients a.

                EXAMPLES::

                    sage: T = sage.rings.number_field.totallyreal_data.tr_data(2,100)
                    sage: T.printa()
                    k = 0
                    a = [0, -1, 1]
                    amax = [0, 0, 1]
                    beta =  [...]
                    gnk =  [...]
        """
    def increment(self, verbose=..., haltk=..., phc=...) -> Any:
        """tr_data.increment(self, verbose=False, haltk=0, phc=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/totallyreal_data.pyx (starting at line 579)

        'Increment' the totally real data to the next
        value which satisfies the bounds essentially given by Rolle's
        theorem, and return the next polynomial as a sequence of
        integers.

        The default or usual case just increments the constant
        coefficient; then inductively, if this is outside of the
        bounds we increment the next higher coefficient, and so on.

        If there are no more coefficients to be had, returns the zero
        polynomial.

        INPUT:

        - ``verbose`` -- boolean to print verbosely computational details
        - ``haltk`` -- integer; the level at which to halt the inductive
          coefficient bounds
        - ``phc`` -- boolean, if PHCPACK is available, use it when `k = n-5` to
          compute an improved Lagrange multiplier bound

        OUTPUT: the next polynomial, as a sequence of integers

        EXAMPLES::

            sage: T = sage.rings.number_field.totallyreal_data.tr_data(2,100)
            sage: T.increment()
            [-24, -1, 1]
            sage: for i in range(19): _ = T.increment()
            sage: T.increment()
            [-3, -1, 1]
            sage: T.increment()
            [-25, 0, 1]"""
    @overload
    def printa(self) -> Any:
        """tr_data.printa(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/totallyreal_data.pyx (starting at line 903)

        Print relevant data for ``self``.

        EXAMPLES::

            sage: T = sage.rings.number_field.totallyreal_data.tr_data(3,2^10)
            sage: T.printa()
            k = 1
            a = [0, 0, -1, 1]
            amax = [0, 0, 0, 1]
            beta =  [...]
            gnk =  [...]"""
    @overload
    def printa(self) -> Any:
        """tr_data.printa(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/totallyreal_data.pyx (starting at line 903)

        Print relevant data for ``self``.

        EXAMPLES::

            sage: T = sage.rings.number_field.totallyreal_data.tr_data(3,2^10)
            sage: T.printa()
            k = 1
            a = [0, 0, -1, 1]
            amax = [0, 0, 0, 1]
            beta =  [...]
            gnk =  [...]"""
