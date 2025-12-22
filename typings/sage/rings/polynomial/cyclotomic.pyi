r"""
Fast calculation of cyclotomic polynomials

This module provides a function :func:`cyclotomic_coeffs`, which calculates the
coefficients of cyclotomic polynomials. This is not intended to be invoked
directly by the user, but it is called by the method
:meth:`~sage.rings.polynomial.polynomial_ring.PolynomialRing_generic.cyclotomic_polynomial`
method of univariate polynomial ring objects and the top-level
:func:`~sage.misc.functional.cyclotomic_polynomial` function.
"""
import cypari2.pari_instance
from sage.arith.misc import factor as factor
from sage.categories.category import ZZ as ZZ
from sage.combinat.subset import subsets as subsets
from sage.misc.misc_c import prod as prod
from sage.structure.element import have_same_parent as have_same_parent, parent as parent, RingElement as RingElement

from sage.rings.integer import Integer
from typings_sagemath import Int

def bateman_bound(nn: Int) -> Integer:
    """
    Reference:

    Bateman, P. T.; Pomerance, C.; Vaughan, R. C.
    *On the size of the coefficients of the cyclotomic polynomial.*

    EXAMPLES::

        sage: from sage.rings.polynomial.cyclotomic import bateman_bound
        sage: bateman_bound(2**8 * 1234567893377)                                       # needs sage.libs.pari
        66944986927
    """
def cyclotomic_coeffs(nn: Int, sparse: None | bool = None) -> list[Integer]:
    """
    Return the coefficients of the `n`-th cyclotomic polynomial
    by using the formula

    .. MATH::

        \\Phi_n(x) = \\prod_{d|n} (1-x^{n/d})^{\\mu(d)}

    where `\\mu(d)` is the Möbius function that is 1 if `d` has an even
    number of distinct prime divisors, `-1` if it has an odd number of
    distinct prime divisors, and `0` if `d` is not squarefree.

    Multiplications and divisions by polynomials of the
    form `1-x^n` can be done very quickly in a single pass.

    If ``sparse`` is ``True``, the result is returned as a dictionary of
    the nonzero entries, otherwise the result is returned as a list
    of python ints.

    EXAMPLES::

        sage: from sage.rings.polynomial.cyclotomic import cyclotomic_coeffs
        sage: cyclotomic_coeffs(30)
        [1, 1, 0, -1, -1, -1, 0, 1, 1]
        sage: cyclotomic_coeffs(10^5)
        {0: 1, 10000: -1, 20000: 1, 30000: -1, 40000: 1}
        sage: R = QQ['x']
        sage: R(cyclotomic_coeffs(30))
        x^8 + x^7 - x^5 - x^4 - x^3 + x + 1

    Check that it has the right degree::

        sage: euler_phi(30)                                                             # needs sage.libs.pari
        8
        sage: R(cyclotomic_coeffs(14)).factor()                                         # needs sage.libs.pari
        x^6 - x^5 + x^4 - x^3 + x^2 - x + 1

    The coefficients are not always +/-1::

        sage: cyclotomic_coeffs(105)
        [1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1,
         0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -2,
         -1, -1, 0, 0, 1, 1, 1]

    In fact the height is not bounded by any polynomial in `n` (Erdos),
    although takes a while just to exceed linear::

        sage: v = cyclotomic_coeffs(1181895)
        sage: max(v)
        14102773

    The polynomial is a palindrome for any n::

        sage: n = ZZ.random_element(50000)
        sage: v = cyclotomic_coeffs(n, sparse=False)
        sage: v == list(reversed(v))
        True

    AUTHORS:

    - Robert Bradshaw (2007-10-27): initial version (inspired by work of Andrew
      Arnold and Michael Monagan)

    REFERENCE:

    - http://www.cecm.sfu.ca/~ada26/cyclotomic/
    """
def cyclotomic_value(n: Int, x: RingElement) -> RingElement:
    r"""
    Return the value of the `n`-th cyclotomic polynomial evaluated at `x`.

    INPUT:

    - ``n`` -- an Integer, specifying which cyclotomic polynomial is to be
      evaluated

    - ``x`` -- an element of a ring

    OUTPUT: the value of the cyclotomic polynomial `\Phi_n` at `x`

    ALGORITHM:

    - Reduce to the case that `n` is squarefree: use the identity

    .. MATH::

        \Phi_n(x) = \Phi_q(x^{n/q})

    where `q` is the radical of `n`.

    - Use the identity

    .. MATH::

        \Phi_n(x) = \prod_{d | n} (x^d - 1)^{\mu(n / d)},

    where `\mu` is the Möbius function.

    - Handles the case that `x^d = 1` for some `d`, but not the case that
      `x^d - 1` is non-invertible: in this case polynomial evaluation is
      used instead.

    EXAMPLES::

        sage: cyclotomic_value(51, 3)
        1282860140677441
        sage: cyclotomic_polynomial(51)(3)
        1282860140677441

    It works for non-integral values as well::

        sage: cyclotomic_value(144, 4/3)
        79148745433504023621920372161/79766443076872509863361
        sage: cyclotomic_polynomial(144)(4/3)
        79148745433504023621920372161/79766443076872509863361

    TESTS::

        sage: elements = [-1, 0, 1, 2, 1/2, Mod(3, 8), Mod(3,11)]
        sage: R.<x> = QQ[]; elements += [x^2 + 2]
        sage: K.<i> = NumberField(x^2 + 1); elements += [i]                             # needs sage.rings.number_fields
        sage: elements += [GF(9,'a').gen()]                                             # needs sage.rings.finite_rings
        sage: elements += [Zp(3)(54)]                                                   # needs sage.rings.padics
        sage: for y in elements:
        ....:     for n in [1..60]:
        ....:         val1 = cyclotomic_value(n, y)
        ....:         val2 = cyclotomic_polynomial(n)(y)
        ....:         if val1 != val2:
        ....:             print("Wrong value for cyclotomic_value(%s, %s) in %s"%(n,y,parent(y)))
        ....:         if val1.parent() is not val2.parent():
        ....:             print("Wrong parent for cyclotomic_value(%s, %s) in %s"%(n,y,parent(y)))

        sage: cyclotomic_value(20, I)                                                   # needs sage.symbolic
        5
        sage: a = cyclotomic_value(10, mod(3, 11)); a
        6
        sage: a.parent()
        Ring of integers modulo 11
        sage: cyclotomic_value(30, -1.0)                                                # needs sage.rings.real_mpfr
        1.00000000000000

        sage: # needs sage.libs.pari
        sage: S.<t> = R.quotient(R.cyclotomic_polynomial(15))
        sage: cyclotomic_value(15, t)
        0
        sage: cyclotomic_value(30, t)
        2*t^7 - 2*t^5 - 2*t^3 + 2*t
        sage: S.<t> = R.quotient(x^10)
        sage: cyclotomic_value(2^128 - 1, t)
        -t^7 - t^6 - t^5 + t^2 + t + 1
        sage: cyclotomic_value(10, mod(3,4))
        1

    Check that the issue with symbolic element in :issue:`14982` is fixed::

        sage: a = cyclotomic_value(3, I)                                                # needs sage.rings.number_fields
        sage: parent(a)                                                                 # needs sage.rings.number_fields
        Number Field in I with defining polynomial x^2 + 1 with I = 1*I
    """
pari: cypari2.pari_instance.Pari
