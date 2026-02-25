r"""
Generic numerical approximation function
"""
from typing import SupportsFloat, SupportsInt, overload
from typings_sagemath import ComplexInexactSage, Real
from sage.rings.real_mpfr import RealNumber
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SymbolicRing
from gmpy2 import mpc

from sage.rings.imaginary_unit import NumberFieldElement_gaussian

type _mpfr_prec_t = SupportsInt
type _signed_inf = PlusInfinity | MinusInfinity

from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.real_mpfr import RealField as RealField
from sage.rings.complex_double import CDF as CDF

def digits_to_bits(d: SupportsFloat | None) -> int:
    """
    EXAMPLES::

        sage: from sage.arith.numerical_approx import digits_to_bits
        sage: digits_to_bits(None)
        53
        sage: digits_to_bits(15)
        54
        sage: digits_to_bits(-1)
        Traceback (most recent call last):
        ...
        ValueError: number of digits must be positive

    TESTS::

        sage: digits_to_bits("10")
        Traceback (most recent call last):
        ...
        TypeError: must be real number, not str
    """
@overload
def numerical_approx_generic(
    x: Real | _signed_inf, prec: _mpfr_prec_t
) -> RealNumber: ...
@overload
def numerical_approx_generic(
    x: complex | mpc | NumberFieldElement_gaussian | ComplexInexactSage, 
    prec: _mpfr_prec_t
) -> ComplexNumber: ...
@overload
def numerical_approx_generic(
    x: Expression[SymbolicRing], prec: _mpfr_prec_t
) -> RealNumber | ComplexNumber:
    """
    Generic implementation of ``numerical_approx`` using coercion or
    conversion to a real or complex field.

    EXAMPLES::

        sage: from sage.arith.numerical_approx import numerical_approx_generic
        sage: numerical_approx_generic(pi, 20)                                          # needs sage.symbolic
        3.1416
        sage: numerical_approx_generic(int(42), 20)
        42.000
        sage: numerical_approx_generic(float(4.2), 20)
        4.2000
    """
