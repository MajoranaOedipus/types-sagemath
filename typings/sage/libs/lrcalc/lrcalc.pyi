from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.permutation import Permutation as Permutation
from sage.combinat.skew_partition import SkewPartition as SkewPartition
from sage.combinat.skew_tableau import SemistandardSkewTableaux as SemistandardSkewTableaux
from sage.rings.integer import Integer as Integer

def lrcoef_unsafe(outer, inner1, inner2):
    """
    Compute a single Littlewood-Richardson coefficient.

    Return the coefficient of ``outer`` in the product of the Schur
    functions indexed by ``inner1`` and ``inner2``.

    INPUT:

    - ``outer`` -- a partition (weakly decreasing list of nonnegative integers)
    - ``inner1`` -- a partition
    - ``inner2`` -- a partition

    .. WARNING::

       This function does not do any check on its input.  If you want
       to use a safer version, use :func:`lrcoef`.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import lrcoef_unsafe
        sage: lrcoef_unsafe([3,2,1], [2,1], [2,1])
        2
        sage: lrcoef_unsafe([3,3], [2,1], [2,1])
        1
        sage: lrcoef_unsafe([2,1,1,1,1], [2,1], [2,1])
        0
    """
def lrcoef(outer, inner1, inner2):
    """
    Compute a single Littlewood-Richardson coefficient.

    Return the coefficient of ``outer`` in the product of the Schur
    functions indexed by ``inner1`` and ``inner2``.

    INPUT:

    - ``outer`` -- a partition (weakly decreasing list of nonnegative integers)
    - ``inner1`` -- a partition
    - ``inner2`` -- a partition

    .. NOTE::

       This function converts its inputs into :func:`Partition`'s.  If
       you don't need these checks and your inputs are valid, then you
       can use :func:`lrcoef_unsafe`.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import lrcoef
        sage: lrcoef([3,2,1], [2,1], [2,1])
        2
        sage: lrcoef([3,3], [2,1], [2,1])
        1
        sage: lrcoef([2,1,1,1,1], [2,1], [2,1])
        0
    """
def mult(part1, part2, maxrows=None, level=None, quantum=None) -> dict:
    """
    Compute a product of two Schur functions.

    Return the product of the Schur functions indexed by the
    partitions ``part1`` and ``part2``.

    INPUT:

    - ``part1`` -- a partition
    - ``part2`` -- a partition
    - ``maxrows`` -- integer (optional)
    - ``level`` -- integer (optional)
    - ``quantum`` -- an element of a ring (optional)

    If ``maxrows`` is specified, then only partitions with at most
    this number of rows are included in the result.

    If both ``maxrows`` and ``level`` are specified, then the function
    calculates the fusion product for `\\mathfrak{sl}(\\mathrm{maxrows})`
    of the given level.

    If ``quantum`` is set, then this returns the product in the quantum
    cohomology ring of the Grassmannian. In particular, both ``maxrows``
    and ``level`` need to be specified.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import mult
        sage: mult([2],[])
        {[2]: 1}
        sage: sorted(mult([2],[2]).items())
        [([2, 2], 1), ([3, 1], 1), ([4], 1)]
        sage: sorted(mult([2,1],[2,1]).items())
        [([2, 2, 1, 1], 1), ([2, 2, 2], 1), ([3, 1, 1, 1], 1),
         ([3, 2, 1], 2), ([3, 3], 1), ([4, 1, 1], 1), ([4, 2], 1)]
        sage: sorted(mult([2,1],[2,1],maxrows=2).items())
        [([3, 3], 1), ([4, 2], 1)]
        sage: mult([2,1],[3,2,1],3)
        {[3, 3, 3]: 1, [4, 3, 2]: 2, [4, 4, 1]: 1, [5, 2, 2]: 1, [5, 3, 1]: 1}
        sage: mult([2,1],[2,1],3,3)
        {[2, 2, 2]: 1, [3, 2, 1]: 2, [3, 3]: 1, [4, 1, 1]: 1}
        sage: mult([2,1],[2,1],None,3)
        Traceback (most recent call last):
        ...
        ValueError: maxrows needs to be specified if you specify the level

     The quantum product::

        sage: q = polygen(QQ, 'q')
        sage: sorted(mult([1],[2,1], 2, 2, quantum=q).items())
        [([], q), ([2, 2], 1)]
        sage: sorted(mult([2,1],[2,1], 2, 2, quantum=q).items())
        [([1, 1], q), ([2], q)]

        sage: mult([2,1],[2,1], quantum=q)
        Traceback (most recent call last):
        ...
        ValueError: missing parameters maxrows or level
    """
def skew(outer, inner, maxrows: int = -1) -> dict:
    """
    Compute the Schur expansion of a skew Schur function.

    Return a linear combination of partitions representing the Schur
    function of the skew Young diagram ``outer / inner``, consisting
    of boxes in the partition ``outer`` that are not in ``inner``.

    INPUT:

    - ``outer`` -- a partition
    - ``inner`` -- a partition
    - ``maxrows`` -- integer or ``None``

    If ``maxrows`` is specified, then only partitions with at most
    this number of rows are included in the result.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import skew
        sage: sorted(skew([2,1],[1]).items())
        [([1, 1], 1), ([2], 1)]
    """
def coprod(part, all: int = 0) -> dict:
    """
    Compute the coproduct of a Schur function.

    Return a linear combination of pairs of partitions representing
    the coproduct of the Schur function given by the partition
    ``part``.

    INPUT:

    - ``part`` -- a partition
    - ``all`` -- integer

    If ``all`` is nonzero then all terms are included in the result.
    If ``all`` is zero, then only pairs of partitions ``(part1,
    part2)`` for which the weight of ``part1`` is greater than or
    equal to the weight of ``part2`` are included; the rest of the
    coefficients are redundant because Littlewood-Richardson
    coefficients are symmetric.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import coprod
        sage: sorted(coprod([2,1]).items())
        [(([1, 1], [1]), 1), (([2], [1]), 1), (([2, 1], []), 1)]
    """
def mult_schubert(w1, w2, rank: int = 0) -> dict:
    """
    Compute a product of two Schubert polynomials.

    Return a linear combination of permutations representing the
    product of the Schubert polynomials indexed by the permutations
    ``w1`` and ``w2``.

    INPUT:

    - ``w1`` -- a permutation
    - ``w2`` -- a permutation
    - ``rank`` -- integer

    If ``rank`` is nonzero, then only permutations from the symmetric
    group `S(\\mathrm{rank})` are included in the result.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import mult_schubert
        sage: result = mult_schubert([3, 1, 5, 2, 4], [3, 5, 2, 1, 4])
        sage: sorted(result.items())
        [([5, 4, 6, 1, 2, 3], 1), ([5, 6, 3, 1, 2, 4], 1),
         ([5, 7, 2, 1, 3, 4, 6], 1), ([6, 3, 5, 1, 2, 4], 1),
         ([6, 4, 3, 1, 2, 5], 1), ([6, 5, 2, 1, 3, 4], 1),
         ([7, 3, 4, 1, 2, 5, 6], 1), ([7, 4, 2, 1, 3, 5, 6], 1)]
    """
def lrskew(outer, inner, weight=None, maxrows: int = -1) -> Generator[Incomplete]:
    """
    Iterate over the skew LR tableaux of shape ``outer / inner``.

    INPUT:

    - ``outer`` -- a partition
    - ``inner`` -- a partition
    - ``weight`` -- a partition (optional)
    - ``maxrows`` -- positive integer (optional)

    OUTPUT: an iterator of :class:`SkewTableau`

    Specifying ``maxrows`` = `M` restricts the alphabet to `\\{1,2,\\ldots,M\\}`.

    Specifying ``weight`` returns only those tableaux of given content/weight.

    EXAMPLES::

        sage: from sage.libs.lrcalc.lrcalc import lrskew
        sage: for st in lrskew([3,2,1],[2]):
        ....:     st.pp()
        .  .  1
        1  1
        2
        .  .  1
        1  2
        2
        .  .  1
        1  2
        3

        sage: for st in lrskew([3,2,1],[2], maxrows=2):
        ....:     st.pp()
        .  .  1
        1  1
        2
        .  .  1
        1  2
        2

        sage: list(lrskew([3,2,1],[2], weight=[3,1]))
        [[[None, None, 1], [1, 1], [2]]]

    TESTS::

        sage: from sage.libs.lrcalc.lrcalc import lrskew
        sage: list(lrskew([3,2,1],[2], weight=[]))
        []
        sage: list(lrskew([3,2,1],[2], weight=[0]))
        []
        sage: list(lrskew([3,2,1],[3,2,1], weight=[]))
        [[[None, None, None], [None, None], [None]]]
        sage: list(lrskew([3,2,1],[3,2,1], weight=[0]))
        [[[None, None, None], [None, None], [None]]]
        sage: list(lrskew([3,2,1],[3,2,1], weight=[1]))
        []
    """
