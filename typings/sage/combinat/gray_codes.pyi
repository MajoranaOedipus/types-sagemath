from _typeshed import Incomplete
from collections.abc import Generator

def product(m) -> Generator[Incomplete]:
    '''
    Iterator over the switch for the iteration of the product
    `[m_0] \\times [m_1] \\ldots \\times [m_k]`.

    The iterator return at each step a pair ``(p,i)`` which corresponds to the
    modification to perform to get the next element. More precisely, one has to
    apply the increment ``i`` at the position ``p``. By construction, the
    increment is either ``+1`` or ``-1``.

    This is algorithm H in [Knu2011]_ Section 7.2.1.1, "Generating All
    `n`-Tuples": loopless reflected mixed-radix Gray generation.

    INPUT:

    - ``m`` -- list or tuple of positive integers that correspond to the size
      of the sets in the product

    EXAMPLES::

        sage: from sage.combinat.gray_codes import product
        sage: l = [0,0,0]
        sage: for p,i in product([3,3,3]):
        ....:     l[p] += i
        ....:     print(l)
        [1, 0, 0]
        [2, 0, 0]
        [2, 1, 0]
        [1, 1, 0]
        [0, 1, 0]
        [0, 2, 0]
        [1, 2, 0]
        [2, 2, 0]
        [2, 2, 1]
        [1, 2, 1]
        [0, 2, 1]
        [0, 1, 1]
        [1, 1, 1]
        [2, 1, 1]
        [2, 0, 1]
        [1, 0, 1]
        [0, 0, 1]
        [0, 0, 2]
        [1, 0, 2]
        [2, 0, 2]
        [2, 1, 2]
        [1, 1, 2]
        [0, 1, 2]
        [0, 2, 2]
        [1, 2, 2]
        [2, 2, 2]
        sage: l = [0,0]
        sage: for i,j in product([2,1]):
        ....:     l[i] += j
        ....:     print(l)
        [1, 0]

    TESTS::

        sage: for t in [[2,2,2],[2,1,2],[3,2,1],[2,1,3]]:
        ....:     assert sum(1 for _ in product(t)) == prod(t)-1
    '''
def combinations(n, t):
    '''
    Iterator through the switches of the revolving door algorithm.

    The revolving door algorithm is a way to generate all combinations of a set
    (i.e. the subset of given cardinality) in such way that two consecutive
    subsets differ by one element. At each step, the iterator output a pair
    ``(i,j)`` where the item ``i`` has to be removed and ``j`` has to be added.

    The ground set is always `\\{0, 1, ..., n-1\\}`. Note that ``n`` can be
    infinity in that algorithm.

    See [Knu2011]_ Section 7.2.1.3, "Generating All Combinations".

    INPUT:

    - ``n`` -- integer or ``Infinity``; size of the ground set

    - ``t`` -- integer; size of the subsets

    EXAMPLES::

        sage: from sage.combinat.gray_codes import combinations
        sage: b = [1, 1, 1, 0, 0]
        sage: for i,j in combinations(5,3):
        ....:     b[i] = 0; b[j] = 1
        ....:     print(b)
        [1, 0, 1, 1, 0]
        [0, 1, 1, 1, 0]
        [1, 1, 0, 1, 0]
        [1, 0, 0, 1, 1]
        [0, 1, 0, 1, 1]
        [0, 0, 1, 1, 1]
        [1, 0, 1, 0, 1]
        [0, 1, 1, 0, 1]
        [1, 1, 0, 0, 1]

        sage: s = set([0,1])
        sage: for i,j in combinations(4,2):
        ....:     s.remove(i)
        ....:     s.add(j)
        ....:     print(sorted(s))
        [1, 2]
        [0, 2]
        [2, 3]
        [1, 3]
        [0, 3]

    Note that ``n`` can be infinity::

        sage: c = combinations(Infinity,4)
        sage: s = set([0,1,2,3])
        sage: for _ in range(10):
        ....:     i,j = next(c)
        ....:     s.remove(i); s.add(j)
        ....:     print(sorted(s))
        [0, 1, 3, 4]
        [1, 2, 3, 4]
        [0, 2, 3, 4]
        [0, 1, 2, 4]
        [0, 1, 4, 5]
        [1, 2, 4, 5]
        [0, 2, 4, 5]
        [2, 3, 4, 5]
        [1, 3, 4, 5]
        [0, 3, 4, 5]
        sage: for _ in range(1000):
        ....:     i,j = next(c)
        ....:     s.remove(i); s.add(j)
        sage: sorted(s)
        [0, 4, 13, 14]

    TESTS::

        sage: def check_sets_from_iter(n, k):
        ....:     l = []
        ....:     s = set(range(k))
        ....:     l.append(frozenset(s))
        ....:     for i,j in combinations(n,k):
        ....:         s.remove(i)
        ....:         s.add(j)
        ....:         assert len(s) == k
        ....:         l.append(frozenset(s))
        ....:     assert len(set(l)) == binomial(n,k)
        sage: check_sets_from_iter(9,5)
        sage: check_sets_from_iter(8,5)
        sage: check_sets_from_iter(5,6)
        Traceback (most recent call last):
        ...
        AssertionError: t(=6) must be >=0 and <=n(=5)
    '''
