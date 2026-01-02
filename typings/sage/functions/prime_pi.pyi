r"""
Counting primes

EXAMPLES::

    sage: z = sage.functions.prime_pi.PrimePi()
    sage: loads(dumps(z))
    prime_pi
    sage: loads(dumps(z)) == z
    True

AUTHORS:

- \R. Andrew Ohana (2009): initial version of efficient prime_pi

- William Stein (2009): fix plot method

- \R. Andrew Ohana (2011): complete rewrite, ~5x speedup

- Dima Pasechnik (2021): removed buggy cython code, replaced it with
  calls to primecount/primecountpy spkg
"""

from typings_sagemath import Int
from sage.rings.integer import Integer as Integer
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

class PrimePi(BuiltinFunction):
    def __init__(self):
        r"""
        The prime counting function, which counts the number of primes less
        than or equal to a given value.

        INPUT:

        - ``x`` -- a real number
        - ``prime_bound`` -- (default: 0) a real number `< 2^{32}`; :func:`prime_pi`
          will make sure to use all the primes up to ``prime_bound`` (although,
          possibly more) in computing ``prime_pi``, this can potentially
          speedup the time of computation, at a cost to memory usage.

        OUTPUT: integer; the number of primes :math:`\leq` ``x``

        EXAMPLES:

        These examples test common inputs::

            sage: # needs sage.symbolic
            sage: prime_pi(7)
            4
            sage: prime_pi(100)
            25
            sage: prime_pi(1000)
            168
            sage: prime_pi(100000)
            9592
            sage: prime_pi(500509)
            41581

        The following test is to verify that :issue:`4670` has been essentially
        resolved::

            sage: prime_pi(10^10)                                                       # needs sage.symbolic
            455052511

        The :func:`prime_pi` function also has a special plotting method, so it
        plots quickly and perfectly as a step function::

            sage: P = plot(prime_pi, 50, 100)                                           # needs sage.plot sage.symbolic
        """

    def __call__(self, arg, coerce=True, hold=False):   # pyright: ignore[reportIncompatibleMethodOverride] 
        # TODO: the actuall implementation seems to be different from the doc
        r"""
        EXAMPLES::

            sage: # needs sage.symbolic
            sage: prime_pi.__call__(756)
            133
            sage: prime_pi.__call__(6574, 577)
            850
            sage: f(x) = prime_pi.__call__(x^2); f(x)
            prime_pi(x^2)
            sage: f(5)
            9
            sage: prime_pi.__call__(1, 2, 3)
            Traceback (most recent call last):
            ...
            TypeError: Symbolic function prime_pi takes 1 or 2 arguments (3 given)
        """

    def plot(self, xmin=0, xmax=100, vertical_lines=True, **kwds):
        """
        Draw a plot of the prime counting function from ``xmin`` to ``xmax``.
        All additional arguments are passed on to the line command.

        WARNING: we draw the plot of ``prime_pi`` as a stairstep function with
        explicitly drawn vertical lines where the function jumps. Technically
        there should not be any vertical lines, but they make the graph look
        much better, so we include them. Use the option ``vertical_lines=False``
        to turn these off.

        EXAMPLES::

            sage: plot(prime_pi, 1, 100)                                                # needs sage.plot sage.symbolic
            Graphics object consisting of 1 graphics primitive
            sage: prime_pi.plot(1, 51, thickness=2, vertical_lines=False)               # needs sage.plot sage.symbolic
            Graphics object consisting of 16 graphics primitives
        """

prime_pi: PrimePi

def legendre_phi(x: Int, a: Int) -> Integer:
    r"""
    Legendre's formula, also known as the partial sieve function, is a useful
    combinatorial function for computing the prime counting function (the
    ``prime_pi`` method in Sage). It counts the number of positive integers
    :math:`\leq` ``x`` that are not divisible by the first ``a`` primes.

    INPUT:

    - ``x`` -- a real number

    - ``a`` -- nonnegative integer

    OUTPUT: integer; the number of positive integers :math:`\leq` ``x`` that
    are not divisible by the first ``a`` primes

    EXAMPLES::

        sage: legendre_phi(100, 0)
        100
        sage: legendre_phi(29375, 1)
        14688
        sage: legendre_phi(91753, 5973)
        2893
        sage: legendre_phi(4215701455, 6450023226)
        1
    """

partial_sieve_function = legendre_phi