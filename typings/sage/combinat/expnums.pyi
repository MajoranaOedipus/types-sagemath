r"""
Bell and Uppuluri-Carpenter numbers

AUTHORS:

- Nick Alexander
"""
from typings_sagemath import Int
from sage.rings.integer import Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

def expnums(n: Int, aa: Int) -> list[Integer]:
    r"""
    Compute the first `n` exponential numbers around
    `aa`, starting with the zero-th.

    INPUT:

    - ``n`` -- C machine int

    - ``aa`` -- C machine int

    OUTPUT: list of length `n`

    ALGORITHM: We use the same integer addition algorithm as GAP. This
    is an extension of Bell's triangle to the general case of
    exponential numbers. The recursion performs `O(n^2)`
    additions, but the running time is dominated by the cost of the
    last integer addition, because the growth of the integer results of
    partial computations is exponential in `n`. The algorithm
    stores `O(n)` integers, but each is exponential in
    `n`.

    EXAMPLES::

        sage: expnums(10, 1)
        [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147]

    ::

        sage: expnums(10, -1)
        [1, -1, 0, 1, 1, -2, -9, -9, 50, 267]

    ::

        sage: expnums(1, 1)
        [1]
        sage: expnums(0, 1)
        []
        sage: expnums(-1, 0)
        []

    AUTHORS:

    - Nick Alexander
    """
    ...
def expnums2(n: Int, aa: Int) -> list[Integer]:
    r"""
    A vanilla python (but compiled via Cython) implementation of
    expnums.

    We Compute the first `n` exponential numbers around
    `aa`, starting with the zero-th.

    EXAMPLES::

        sage: from sage.combinat.expnums import expnums2
        sage: expnums2(10, 1)
        [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147]
    """
    ...
