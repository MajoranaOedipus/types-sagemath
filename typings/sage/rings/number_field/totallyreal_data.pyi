import _cython_3_2_1
from sage.arith.misc import binomial as binomial, gcd as gcd
from sage.categories.category import ZZ as ZZ
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_ring import ZZx as ZZx
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload, SupportsInt

type Int = int | Integer | SupportsInt

__pyx_capi__: dict
easy_is_irreducible_py: _cython_3_2_1.cython_function_or_method


def hermite_constant(n: Int) -> float:
    r"""
    Return the `n`-th Hermite constant.

    The `n`-th Hermite constant (typically denoted `\gamma_n`), is defined
    to be

    .. MATH::

        \max_L \min_{0 \neq x \in L} ||x||^2

    where `L` runs over all lattices of dimension `n` and determinant `1`.

    For `n \leq 8` it returns the exact value of `\gamma_n`, and for
    `n > 9` it returns an upper bound on `\gamma_n`.

    INPUT:

    - ``n`` -- integer

    OUTPUT:

    (an upper bound for) the Hermite constant `\gamma_n`

    EXAMPLES::

        sage: hermite_constant(1) # trivial one-dimensional lattice
        1.0
        sage: hermite_constant(2) # Eisenstein lattice
        1.1547005383792515
        sage: 2/sqrt(3.)
        1.15470053837925
        sage: hermite_constant(8) # E_8
        2.0

    .. NOTE::

        The upper bounds used can be found in [CS1999]_ and [CE2003]_.

    AUTHORS:

    - John Voight (2007-09-03)
    """
    ...

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
    
    def printa(self) -> None:
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
