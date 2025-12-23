r"""
Bernoulli numbers modulo p

AUTHOR:

- David Harvey (2006-07-26): initial version
- William Stein (2006-07-28): some touch up.
- David Harvey (2006-08-06): new, faster algorithm, also using faster NTL interface
- David Harvey (2007-08-31): algorithm for a single Bernoulli number mod p
- David Harvey (2008-06): added interface to bernmm, removed old code
"""
import _cython_3_2_1
import sage as sage
import sage.libs.ntl.all as ntl
from sage.arith.misc import is_prime as is_prime, primitive_root as primitive_root
from sage.rings.bernmm import bernmm_bern_modp as bernmm_bern_modp
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Sequence
from typings_sagemath import Int

def bernoulli_mod_p(p: Int) -> list[int]:
    r"""
    Return the Bernoulli numbers `B_0, B_2, ... B_{p-3}` modulo `p`.

    INPUT:

    - ``p`` -- integer; a prime

    OUTPUT:

    list -- Bernoulli numbers modulo `p` as a list
    of integers [B(0), B(2), ... B(p-3)].

    ALGORITHM:

    Described in accompanying latex file.

    PERFORMANCE:

    Should be complexity `O(p \log p)`.

    EXAMPLES:

    Check the results against PARI's C-library implementation (that
    computes exact rationals) for `p = 37`::

        sage: bernoulli_mod_p(37)
        [1, 31, 16, 15, 16, 4, 17, 32, 22, 31, 15, 15, 17, 12, 29, 2, 0, 2]
        sage: [bernoulli(n) % 37 for n in range(0, 36, 2)]
        [1, 31, 16, 15, 16, 4, 17, 32, 22, 31, 15, 15, 17, 12, 29, 2, 0, 2]

    Boundary case::

        sage: bernoulli_mod_p(3)
         [1]

    AUTHOR:

    - David Harvey (2006-08-06)
    """

def bernoulli_mod_p_single(p: Int, k: Int) -> int:
    r"""
    Return the Bernoulli number `B_k` mod `p`.

    If `B_k` is not `p`-integral, an :exc:`ArithmeticError` is raised.

    INPUT:

    - ``p`` -- integer; a prime
    - ``k`` -- nonnegative integer

    OUTPUT: the `k`-th Bernoulli number mod `p`

    EXAMPLES::

        sage: bernoulli_mod_p_single(1009, 48)
        628
        sage: bernoulli(48) % 1009
        628

        sage: bernoulli_mod_p_single(1, 5)
        Traceback (most recent call last):
        ...
        ValueError: p (=1) must be a prime >= 3

        sage: bernoulli_mod_p_single(100, 4)
        Traceback (most recent call last):
        ...
        ValueError: p (=100) must be a prime

        sage: bernoulli_mod_p_single(19, 5)
        0

        sage: bernoulli_mod_p_single(19, 18)
        Traceback (most recent call last):
        ...
        ArithmeticError: B_k is not integral at p

        sage: bernoulli_mod_p_single(19, -4)
        Traceback (most recent call last):
        ...
        ValueError: k must be nonnegative

    Check results against :class:`bernoulli_mod_p`::

        sage: bernoulli_mod_p(37)
         [1, 31, 16, 15, 16, 4, 17, 32, 22, 31, 15, 15, 17, 12, 29, 2, 0, 2]
        sage: [bernoulli_mod_p_single(37, n) % 37 for n in range(0, 36, 2)]
         [1, 31, 16, 15, 16, 4, 17, 32, 22, 31, 15, 15, 17, 12, 29, 2, 0, 2]

        sage: bernoulli_mod_p(31)
         [1, 26, 1, 17, 1, 9, 11, 27, 14, 23, 13, 22, 14, 8, 14]
        sage: [bernoulli_mod_p_single(31, n) % 31 for n in range(0, 30, 2)]
         [1, 26, 1, 17, 1, 9, 11, 27, 14, 23, 13, 22, 14, 8, 14]

        sage: bernoulli_mod_p(3)
         [1]
        sage: [bernoulli_mod_p_single(3, n) % 3 for n in range(0, 2, 2)]
         [1]

        sage: bernoulli_mod_p(5)
         [1, 1]
        sage: [bernoulli_mod_p_single(5, n) % 5 for n in range(0, 4, 2)]
         [1, 1]

        sage: bernoulli_mod_p(7)
         [1, 6, 3]
        sage: [bernoulli_mod_p_single(7, n) % 7 for n in range(0, 6, 2)]
         [1, 6, 3]

    AUTHOR:

    - David Harvey (2007-08-31)
    - David Harvey (2008-06): rewrote to use bernmm library
    """
    ...

def verify_bernoulli_mod_p(data: Sequence[Int]) -> bool:
    r"""
    Compute checksum for Bernoulli numbers.

    It checks the identity

    .. MATH::

        \sum_{n=0}^{(p-3)/2} 2^{2n} (2n+1) B_{2n}  \equiv  -2 \pmod p

    (see "Irregular Primes to One Million", Buhler et al)

    INPUT:

    - ``data`` -- list; same format as output of :func:`bernoulli_mod_p` function

    OUTPUT: boolean; ``True`` if checksum passed

    EXAMPLES::

        sage: from sage.rings.bernoulli_mod_p import verify_bernoulli_mod_p
        sage: verify_bernoulli_mod_p(bernoulli_mod_p(next_prime(3)))
        True
        sage: verify_bernoulli_mod_p(bernoulli_mod_p(next_prime(1000)))
        True
        sage: verify_bernoulli_mod_p([1, 2, 4, 5, 4])
        True
        sage: verify_bernoulli_mod_p([1, 2, 3, 4, 5])
        False

    This one should test that long longs are working::

        sage: verify_bernoulli_mod_p(bernoulli_mod_p(next_prime(20000)))
        True

    AUTHOR: David Harvey
    """
