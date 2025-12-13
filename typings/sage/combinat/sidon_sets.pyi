from sage.misc.cachefunc import cached_function as cached_function
from sage.rings.integer import Integer as Integer
from sage.sets.set import Set as Set

def sidon_sets(N, g: int = 1):
    """
    Return the set of all Sidon-`g` sets that have elements less than or equal
    to `N`.

    A Sidon-`g` set is a set of positive integers `A \\subset [1, N]` such
    that any integer `M` can be obtain at most `g` times as sums of unordered pairs of
    elements of `A` (the two elements are not necessary distinct):

    .. MATH::

        \\#\\{ (a_i, a_j) | a_i, a_j \\in A, a_i + a_j = M,a_i \\leq a_j \\} \\leq g

    INPUT:

    - ``N`` -- positive integer
    - ``g`` -- positive integer (default: `1`)

    OUTPUT: a Sage set with categories whose element are also set of integers

    EXAMPLES::

        sage: S = sidon_sets(3, 2)
        sage: sorted(S, key=str)
        [{1, 2, 3}, {1, 2}, {1, 3}, {1}, {2, 3}, {2}, {3}, {}]
        sage: S.cardinality()
        8
        sage: S.category()
        Category of finite enumerated sets
        sage: sid = S.an_element()
        sage: sid
        {2}
        sage: sid.category()
        Category of finite enumerated sets

    TESTS::

        sage: S = sidon_sets(10)
        sage: TestSuite(S).run()
        sage: Set([1,2,4,8,13]) in sidon_sets(13)
        True

    The following piece of code computes the first values of the Sloane sequence
    entitled 'Length of shortest (or optimal) Golomb ruler with n marks' with a
    very dumb algorithm. (sequence identifier A003022)::

        sage: n = 1
        sage: L = []
        sage: for i in range(1,19):
        ....:     nb = max([S.cardinality() for S in sidon_sets(i)])
        ....:     if nb > n:
        ....:         L.append(i-1)
        ....:         n = nb
        sage: L
        [1, 3, 6, 11, 17]

    The following tests check that some generalized Sidon sets satisfy the right
    conditions, using a dumb but exhaustive algorithm::

        sage: from itertools import groupby
        sage: all(all(l <= 3 for l in map(lambda s: len(list(s[1])), groupby(sorted(a + ap for a in sid for ap in sid if a >= ap), lambda s: s))) for sid in sidon_sets(10, 3))
        True
        sage: all(all(l <= 5 for l in map(lambda s: len(list(s[1])), groupby(sorted(a + ap for a in sid for ap in sid if a >= ap), lambda s: s))) for sid in sidon_sets(10, 5))
        True

    Checking of arguments::

        sage: sidon_sets(1,1)
        {{}, {1}}
        sage: sidon_sets(-1,3)
        Traceback (most recent call last):
        ...
        ValueError: N must be a positive integer
        sage: sidon_sets(1, -3)
        Traceback (most recent call last):
        ...
        ValueError: g must be a positive integer
    """
@cached_function
def sidon_sets_rec(N, g: int = 1):
    """
    Return the set of all Sidon-`g` sets that have elements less than or equal
    to `N` without checking the arguments. This internal function should not
    be call directly by user.

    TESTS::

        sage: from sage.combinat.sidon_sets import sidon_sets_rec
        sage: sorted(sidon_sets_rec(3,2), key=str)
        [{1, 2, 3}, {1, 2}, {1, 3}, {1}, {2, 3}, {2}, {3}, {}]
    """
