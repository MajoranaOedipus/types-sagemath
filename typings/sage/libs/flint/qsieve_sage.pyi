"""
Interface to FLINT's ``qsieve_factor()``. This used to interact
with an external "QuadraticSieve" program, but its functionality has
been absorbed into flint.
"""
from typings_sagemath import Int
from sage.rings.integer import Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent


def qsieve(n: Int) -> list[tuple[Integer, int]]:
    r"""
    Factor ``n`` using the quadratic sieve.

    INPUT:

    - ``n`` -- integer; neither prime nor a perfect power

    OUTPUT:

    A list of the factors of ``n``. There is no guarantee that the
    factors found will be prime, or distinct.

    EXAMPLES::

        sage: k = 19; n = next_prime(10^k)*next_prime(10^(k+1))
        sage: factor(n)  # (currently) uses PARI
        10000000000000000051 * 100000000000000000039
        sage: qsieve(n)
        [(10000000000000000051, 1), (100000000000000000039, 1)]

    TESTS:

    The factorization of zero is undefined, to match the behavior of
    ``ZZ.zero().factor()``::

        sage: qsieve(ZZ.zero())
        Traceback (most recent call last):
        ...
        ArithmeticError: factorization of 0 is not defined
    """
