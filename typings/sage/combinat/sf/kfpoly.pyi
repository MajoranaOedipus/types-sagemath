from sage.combinat.partitions import ZS1_iterator as ZS1_iterator
from sage.combinat.skew_partition import SkewPartitions as SkewPartitions
from sage.combinat.skew_tableau import SemistandardSkewTableaux as SemistandardSkewTableaux
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen

def KostkaFoulkesPolynomial(mu, nu, t=None):
    """
    Return the Kostka-Foulkes polynomial `K_{\\mu, \\nu}(t)`.
    Here, `\\mu` is a partition or a skew partition, whereas
    `\\nu` is a partition of the same size.

    The Kostka-Foulkes polynomial is defined to be the sum
    of the monomials `t^{\\operatorname{charge}(T)}` over all
    semistandard tableaux `T` of shape `\\lambda / \\mu``,
    where `\\operatorname{charge}(T)` denotes the charge
    of the reading word of `T`
    (see :meth:`sage.combinat.words.finite_word.FiniteWord_class.charge`).

    INPUT:

    - ``mu`` -- partition or skew partition
    - ``nu`` -- partition
    - ``t`` -- an optional parameter (default: ``None``)

    OUTPUT:

    - the Kostka-Foulkes polynomial indexed by ``mu`` and ``nu`` and
      evaluated at the parameter ``t``.  If ``t`` is ``None`` the resulting
      polynomial is in the polynomial ring `\\ZZ[t]`.

    EXAMPLES::

        sage: KostkaFoulkesPolynomial([2,2],[2,2])
        1
        sage: KostkaFoulkesPolynomial([2,2],[4])
        0
        sage: KostkaFoulkesPolynomial([2,2],[1,1,1,1])
        t^4 + t^2
        sage: KostkaFoulkesPolynomial([2,2],[2,1,1])
        t
        sage: q = PolynomialRing(QQ,'q').gen()
        sage: KostkaFoulkesPolynomial([2,2],[2,1,1],q)
        q
        sage: KostkaFoulkesPolynomial([[3,2],[1]],[2,2],q)
        q + 1

    TESTS::

        sage: KostkaFoulkesPolynomial([2,4],[2,2])
        Traceback (most recent call last):
        ...
        ValueError: mu must be a partition or a skew partition
        sage: KostkaFoulkesPolynomial([2,2],[2,4])
        Traceback (most recent call last):
        ...
        ValueError: nu must be a partition
        sage: KostkaFoulkesPolynomial([3,2],[2,1])
        Traceback (most recent call last):
        ...
        ValueError: mu and nu must be partitions of the same size
    """
def kfpoly(mu, nu, t=None):
    """
    Return the Kostka-Foulkes polynomial `K_{\\mu, \\nu}(t)`
    by generating all rigging sequences for the shape `\\mu`, and then
    selecting those of content `\\nu`.

    INPUT:

    - ``mu``, ``nu`` -- partitions
    - ``t`` -- an optional parameter (default: ``None``)

    OUTPUT:

    - the Kostka-Foulkes polynomial indexed by partitions ``mu`` and ``nu`` and
      evaluated at the parameter ``t``.  If ``t`` is ``None`` the resulting polynomial
      is in the polynomial ring `\\ZZ['t']`.

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import kfpoly
        sage: kfpoly([2,2], [2,1,1])
        t
        sage: kfpoly([4], [2,1,1])
        t^3
        sage: kfpoly([4], [2,2])
        t^2
        sage: kfpoly([1,1,1,1], [2,2])
        0

    TESTS::

        sage: kfpoly([], [])
        1
    """
def kfpoly_skew(lamu, nu, t=None):
    """
    Return the Kostka-Foulkes polynomial `K_{\\lambda / \\mu, \\nu}(t)`
    by summing `t^{\\operatorname{charge}(T)}` over all semistandard
    tableaux `T` of shape `\\lambda / \\mu``.

    INPUT:

    - ``lamu`` -- skew partition `\\lambda / \\mu`
    - ``nu`` -- partition `\\nu`
    - ``t`` -- an optional parameter (default: ``None``)

    OUTPUT:

    - the Kostka-Foulkes polynomial indexed by ``mu`` and ``nu`` and
      evaluated at the parameter ``t``.  If ``t`` is ``None`` the
      resulting polynomial is in the polynomial ring `\\ZZ['t']`.

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import kfpoly_skew
        sage: kfpoly_skew([[3,3], [1,1]], [2,1,1])
        t
        sage: kfpoly_skew([[3,3], [1,1]], [2,1,1], 5)
        5
        sage: kfpoly_skew([[5], [1]], [2,2])
        t^2

    TESTS::

        sage: from sage.combinat.sf.kfpoly import kfpoly, kfpoly_skew
        sage: all(kfpoly_skew(SkewPartition([b,[]]), c) == kfpoly(b,c)
        ....:     for n in range(6) for b in Partitions(n)
        ....:     for c in Partitions(n))
        True
    """
def schur_to_hl(mu, t=None):
    """
    Return a dictionary corresponding to `s_\\mu` in Hall-Littlewood `P` basis.

    INPUT:

    - ``mu`` -- a partition
    - ``t`` -- an optional parameter (default: the generator from `\\ZZ['t']` )

    OUTPUT:

    - a dictionary with the coefficients `K_{\\mu\\nu}(t)` for `\\nu` smaller
      in dominance order than `\\mu`

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import *
        sage: schur_to_hl([1,1,1])
        {[1, 1, 1]: 1}
        sage: a = schur_to_hl([2,1])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1], t^2 + t)
        ([2, 1], 1)
        sage: a = schur_to_hl([3])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1], t^3)
        ([2, 1], t)
        ([3], 1)
        sage: a = schur_to_hl([4])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1, 1], t^6)
        ([2, 1, 1], t^3)
        ([2, 2], t^2)
        ([3, 1], t)
        ([4], 1)
        sage: a = schur_to_hl([3,1])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1, 1], t^5 + t^4 + t^3)
        ([2, 1, 1], t^2 + t)
        ([2, 2], t)
        ([3, 1], 1)
        sage: a = schur_to_hl([2,2])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1, 1], t^4 + t^2)
        ([2, 1, 1], t)
        ([2, 2], 1)
        sage: a = schur_to_hl([2,1,1])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1, 1], t^3 + t^2 + t)
        ([2, 1, 1], 1)
        sage: a = schur_to_hl([1,1,1,1])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1, 1], 1)
        sage: a = schur_to_hl([2,2,2])
        sage: for mc in sorted(a.items()): print(mc)
        ([1, 1, 1, 1, 1, 1], t^9 + t^7 + t^6 + t^5 + t^3)
        ([2, 1, 1, 1, 1], t^4 + t^2)
        ([2, 2, 1, 1], t)
        ([2, 2, 2], 1)
    """
def riggings(part):
    """
    Generate all possible rigging sequences for a fixed partition ``part``.

    INPUT:

    - ``part`` -- a partition

    OUTPUT: list of riggings associated to the partition ``part``

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import *
        sage: riggings([3])
        [[[1, 1, 1]], [[2, 1]], [[3]]]
        sage: riggings([2,1])
        [[[2, 1], [1]], [[3], [1]]]
        sage: riggings([1,1,1])
        [[[3], [2], [1]]]
        sage: riggings([2,2])
        [[[2, 2], [1, 1]], [[3, 1], [1, 1]], [[4], [1, 1]], [[4], [2]]]
        sage: riggings([2,2,2])
        [[[3, 3], [2, 2], [1, 1]],
         [[4, 2], [2, 2], [1, 1]],
         [[5, 1], [2, 2], [1, 1]],
         [[6], [2, 2], [1, 1]],
         [[5, 1], [3, 1], [1, 1]],
         [[6], [3, 1], [1, 1]],
         [[6], [4], [2]]]
    """
def compat(n, mu, nu):
    """
    Generate all possible partitions of `n` that can precede `\\mu, \\nu`
    in a rigging sequence.

    INPUT:

    - ``n`` -- positive integer
    - ``mu``, ``nu`` -- partitions

    OUTPUT: list of partitions

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import *
        sage: compat(4, [1], [2,1])
        [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]]
        sage: compat(3, [1], [2,1])
        [[1, 1, 1], [2, 1], [3]]
        sage: compat(2, [1], [])
        [[2]]
        sage: compat(3, [1], [])
        [[2, 1], [3]]
        sage: compat(3, [2], [1])
        [[3]]
        sage: compat(4, [1,1], [])
        [[2, 2], [3, 1], [4]]
        sage: compat(4, [2], [])
        [[4]]
    """
def dom(mup, snu):
    """
    Return ``True`` if ``sum(mu[:i+1]) >= snu[i]`` for all
    ``0 <= i < len(snu)``; otherwise, it returns ``False``.

    INPUT:

    - ``mup`` -- a partition conjugate to ``mu``
    - ``snu`` -- a sequence of positive integers

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import *
        sage: dom([3,2,1],[2,4,5])
        True
        sage: dom([3,2,1],[2,4,7])
        False
        sage: dom([3,2,1],[2,6,5])
        False
        sage: dom([3,2,1],[4,4,4])
        False

    TESTS::

        sage: dom([],[])
        True
    """
def weight(rg, t=None):
    """
    Return the weight of a rigging.

    INPUT:

    - ``rg`` -- a rigging, a list of partitions
    - ``t`` -- an optional parameter, (default: the generator from `\\ZZ['t']`)

    OUTPUT: a polynomial in the parameter `t`

    EXAMPLES::

        sage: from sage.combinat.sf.kfpoly import weight
        sage: weight([[2,1], [1]])
        1
        sage: weight([[3], [1]])
        t^2 + t
        sage: weight([[2,1], [3]])
        t^4
        sage: weight([[2, 2], [1, 1]])
        1
        sage: weight([[3, 1], [1, 1]])
        t
        sage: weight([[4], [1, 1]], 2)
        16
        sage: weight([[4], [2]], t=2)
        4
    """
