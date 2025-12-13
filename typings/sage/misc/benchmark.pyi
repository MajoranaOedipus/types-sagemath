from sage.all import *
from sage.misc.misc import cputime as cputime

def benchmark(n: int = -1):
    """
    Run a well-chosen range of Sage commands and record the time it
    takes for each to run.

    INPUT:

    - ``n`` -- integer (default: -1); the benchmark number; the default
      of -1 runs all the benchmarks

    OUTPUT:

        list -- summary of timings for each benchmark.
        int -- if n == -1, also return the total time

    EXAMPLES::

        sage: from sage.misc.benchmark import *
        sage: _ = benchmark()
        Running benchmark 0
        Benchmark 0: Factor the following polynomial over
            the rational numbers: (x^97+19*x+1)*(x^103-19*x^97+14)*(x^100-1)
        Time: ... seconds
        Running benchmark 1
        Find the Mordell-Weil group of the elliptic curve 5077A using mwrank
        Time: ... seconds
        Running benchmark 2
        Some basic arithmetic with very large Integer numbers: '3^1000001 * 19^100001
        Time: ... seconds
        Running benchmark 3
        Some basic arithmetic with very large Rational numbers: '(2/3)^100001 * (17/19)^100001
        Time: ... seconds
        Running benchmark 4
        Rational polynomial arithmetic using Sage. Compute (x^29+17*x-5)^200.
        Time: ... seconds
        Running benchmark 5
        Rational polynomial arithmetic using Sage. Compute (x^19 - 18*x + 1)^50 one hundred times.
        Time: ... seconds
        Running benchmark 6
        Compute the p-division polynomials of y^2 = x^3 + 37*x - 997 for primes p < 40.
        Time: ... seconds
        Running benchmark 7
        Compute the Mordell-Weil group of y^2 = x^3 + 37*x - 997.
        Time: ... seconds
        Running benchmark 8
    """
def bench0():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench0()[0])
        Benchmark 0: Factor the following polynomial over
            the rational numbers: (x^97+19*x+1)*(x^103-19*x^97+14)*(x^100-1)
    """
def bench1():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench1()[0])
        Find the Mordell-Weil group of the elliptic curve 5077A using mwrank
    """
def bench2():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench2()[0])
        Some basic arithmetic with very large Integer numbers: '3^1000001 * 19^100001
    """
def bench3():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench3()[0])
        Some basic arithmetic with very large Rational numbers: '(2/3)^100001 * (17/19)^100001
    """
def bench4():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench4()[0])
        Rational polynomial arithmetic using Sage. Compute (x^29+17*x-5)^200.
    """
def bench5():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench5()[0])
        Rational polynomial arithmetic using Sage. Compute (x^19 - 18*x + 1)^50 one hundred times.
    """
def bench6():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench6()[0])
        Compute the p-division polynomials of y^2 = x^3 + 37*x - 997 for primes p < 40.
    """
def bench7():
    """
    Run a benchmark.

    BENCHMARK::

        sage: from sage.misc.benchmark import *
        sage: print(bench7()[0])
        Compute the Mordell-Weil group of y^2 = x^3 + 37*x - 997.
    """
