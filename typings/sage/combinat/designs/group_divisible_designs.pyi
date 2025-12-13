from .incidence_structures import IncidenceStructure as IncidenceStructure
from sage.arith.misc import is_prime_power as is_prime_power
from sage.misc.unknown import Unknown as Unknown

def group_divisible_design(v, K, G, existence: bool = False, check: bool = False):
    """
    Return a `(v,K,G)`-Group Divisible Design.

    A `(v,K,G)`-GDD is a pair `(\\mathcal G, \\mathcal B)` where:

    - `\\mathcal G` is a partition of `X=\\bigcup \\mathcal G` where `|X|=v`

    - `\\forall S\\in \\mathcal G, |S| \\in G`

    - `\\forall S\\in \\mathcal B, |S| \\in K`

    - `\\mathcal G\\cup \\mathcal B` is a `(v,K\\cup G)`-PBD

    For more information, see the documentation of
    :class:`~sage.combinat.designs.incidence_structures.GroupDivisibleDesign` or
    :class:`~sage.combinat.designs.bibd.PairwiseBalancedDesign`.

    INPUT:

    - ``v`` -- integer

    - ``K``, ``G`` -- sets of integers

    - ``existence`` -- boolean; instead of building the design, return:

        - ``True`` -- meaning that Sage knows how to build the design

        - ``Unknown`` -- meaning that Sage does not know how to build the
          design, but that the design may exist (see :mod:`sage.misc.unknown`)

        - ``False`` -- meaning that the design does not exist

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    .. NOTE::

        The GDD returned by this function are defined on ``range(v)``, and its
        groups are sets of consecutive integers.

    EXAMPLES::

        sage: designs.group_divisible_design(14,{4},{2})
        Group Divisible Design on 14 points of type 2^7
    """
def GDD_4_2(q, existence: bool = False, check: bool = True):
    """
    Return a `(2q,\\{4\\},\\{2\\})`-GDD for `q` a prime power with `q\\equiv 1\\pmod{6}`.

    This method implements Lemma VII.5.17 from [BJL99] (p.495).

    INPUT:

    - ``q`` -- integer

    - ``existence`` -- boolean; instead of building the design, return:

        - ``True`` -- meaning that Sage knows how to build the design

        - ``Unknown`` -- meaning that Sage does not know how to build the
          design, but that the design may exist (see :mod:`sage.misc.unknown`)

        - ``False`` -- meaning that the design does not exist

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: from sage.combinat.designs.group_divisible_designs import GDD_4_2
        sage: GDD_4_2(7,existence=True)
        True
        sage: GDD_4_2(7)
        Group Divisible Design on 14 points of type 2^7
        sage: GDD_4_2(8,existence=True)
        Unknown
        sage: GDD_4_2(8)
        Traceback (most recent call last):
        ...
        NotImplementedError
    """

class GroupDivisibleDesign(IncidenceStructure):
    """
    Group Divisible Design (GDD).

    Let `K` and `G` be sets of positive integers and let `\\lambda` be a positive
    integer. A Group Divisible Design of index `\\lambda` and order `v` is a
    triple `(V,\\mathcal G,\\mathcal B)` where:

    - `V` is a set of cardinality `v`

    - `\\mathcal G` is a partition of `V` into groups whose size belongs to `G`

    - `\\mathcal B` is a family of subsets of `V` whose size belongs to `K` such
      that any two points `p_1,p_2\\in V` from different groups appear
      simultaneously in exactly `\\lambda` elements of `\\mathcal B`. Besides, a
      group and a block intersect on at most one point.

    If `K=\\{k_1,...,k_l\\}` and `G` has exactly `m_i` groups of cardinality `k_i`
    then `G` is said to have type `k_1^{m_1}...k_l^{m_l}`.

    INPUT:

    - ``points`` -- the underlying set. If ``points`` is an integer `v`, then
      the set is considered to be `\\{0, ..., v-1\\}`

    - ``groups`` -- the groups of the design. Set to ``None`` for an automatic
      guess (this triggers ``check=True`` and can thus cost some time)

    - ``blocks`` -- collection of blocks

    - ``G`` -- list of integers of which the sizes of the groups must be
      elements. Set to ``None`` (automatic guess) by default

    - ``K`` -- list of integers of which the sizes of the blocks must be
      elements. Set to ``None`` (automatic guess) by default

    - ``lambd`` -- integer (default: `1`); value of `\\lambda`

    - ``check`` -- boolean (default: ``True``); whether to check that the design is indeed a `GDD`
      with the right parameters

    - ``copy`` -- (use with caution) if set to ``False`` then ``blocks`` must be
      a list of lists of integers. The list will not be copied but will be
      modified in place (each block is sorted, and the whole list is
      sorted). Your ``blocks`` object will become the instance's internal data.

    EXAMPLES::

        sage: from sage.combinat.designs.group_divisible_designs import GroupDivisibleDesign
        sage: TD = designs.transversal_design(4,10)
        sage: groups = [list(range(i*10,(i+1)*10)) for i in range(4)]
        sage: GDD = GroupDivisibleDesign(40,groups,TD); GDD
        Group Divisible Design on 40 points of type 10^4

    With unspecified groups::

        sage: # needs sage.schemes
        sage: D = designs.transversal_design(4,3).relabel(list('abcdefghiklm'),inplace=False).blocks()
        sage: GDD = GroupDivisibleDesign('abcdefghiklm',None,D)
        sage: sorted(GDD.groups())
        [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['k', 'l', 'm']]
    """
    def __init__(self, points, groups, blocks, G=None, K=None, lambd: int = 1, check: bool = True, copy: bool = True, **kwds) -> None:
        """
        Constructor function.

        EXAMPLES::

            sage: from sage.combinat.designs.group_divisible_designs import GroupDivisibleDesign
            sage: TD = designs.transversal_design(4,10)
            sage: groups = [list(range(i*10,(i+1)*10)) for i in range(4)]
            sage: GDD = GroupDivisibleDesign(40,groups,TD); GDD
            Group Divisible Design on 40 points of type 10^4
        """
    def groups(self):
        """
        Return the groups of the Group-Divisible Design.

        EXAMPLES::

            sage: from sage.combinat.designs.group_divisible_designs import GroupDivisibleDesign
            sage: TD = designs.transversal_design(4,10)
            sage: groups = [list(range(i*10,(i+1)*10)) for i in range(4)]
            sage: GDD = GroupDivisibleDesign(40,groups,TD); GDD
            Group Divisible Design on 40 points of type 10^4
            sage: GDD.groups()
            [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
             [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
             [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]]

        TESTS:

        Non-integer ground set::

            sage: # needs sage.schemes
            sage: TD = designs.transversal_design(5,5)
            sage: TD.relabel({i: chr(97+i) for i in range(25)})
            sage: TD.groups()
            [['a', 'b', 'c', 'd', 'e'],
             ['f', 'g', 'h', 'i', 'j'],
             ['k', 'l', 'm', 'n', 'o'],
             ['p', 'q', 'r', 's', 't'],
             ['u', 'v', 'w', 'x', 'y']]
        """
