r"""
Generic numerical approximation function
"""
from typing import SupportsFloat
from typings_sagemath import Int
from sage.rings.real_mpfr import RealNumber
from sage.rings.complex_mpfr import ComplexNumber

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
def numerical_approx_generic(x: object, prec: Int) -> RealNumber | ComplexNumber:
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
