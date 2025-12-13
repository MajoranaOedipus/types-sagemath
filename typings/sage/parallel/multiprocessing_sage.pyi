from . import ncpus as ncpus
from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.fpickle import call_pickled_function as call_pickled_function, pickle_function as pickle_function

def pyprocessing(processes: int = 0):
    """
    Return a parallel iterator using a given number of processes
    implemented using pyprocessing.

    INPUT:

    - ``processes`` -- integer (default: 0); if 0, set to the number
      of processors on the computer

    OUTPUT: a (partially evaluated) function

    EXAMPLES::

        sage: from sage.parallel.multiprocessing_sage import pyprocessing
        sage: p_iter = pyprocessing(4)
        sage: P = parallel(p_iter=p_iter)
        sage: def f(x): return x+x
        sage: v = list(P(f)(list(range(10)))); v.sort(); v
        [(((0,), {}), 0), (((1,), {}), 2), (((2,), {}), 4), (((3,), {}), 6), (((4,), {}), 8), (((5,), {}), 10), (((6,), {}), 12), (((7,), {}), 14), (((8,), {}), 16), (((9,), {}), 18)]
    """
def parallel_iter(processes, f, inputs) -> Generator[Incomplete, Incomplete]:
    """
    Return a parallel iterator.

    INPUT:

    - ``processes`` -- integer
    - ``f`` -- function
    - ``inputs`` -- an iterable of pairs (args, kwds)

    OUTPUT: iterator over values of ``f`` at ``args, kwds`` in some random order

    EXAMPLES::

        sage: def f(x): return x+x
        sage: import sage.parallel.multiprocessing_sage
        sage: v = list(sage.parallel.multiprocessing_sage.parallel_iter(2, f, [((2,), {}), ((3,),{})]))
        sage: v.sort(); v
        [(((2,), {}), 4), (((3,), {}), 6)]
    """
