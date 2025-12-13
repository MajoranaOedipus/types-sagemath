from .design_catalog import transversal_design as transversal_design
from .designs_pyx import is_pairwise_balanced_design as is_pairwise_balanced_design
from .group_divisible_designs import GroupDivisibleDesign as GroupDivisibleDesign
from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial, is_prime_power as is_prime_power, is_square as is_square
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.unknown import Unknown as Unknown

def biplane(n, existence: bool = False):
    """
    Return a biplane of order `n`.

    A biplane of order `n` is a symmetric `(1+\\frac {(n+1)(n+2)} {2}, n+2, 2)`-BIBD.
    A symmetric (or square) `(v,k,\\lambda)`-BIBD is a `(v,k,\\lambda)`-BIBD with `v` blocks.

    INPUT:

    - ``n`` -- integer; order of the biplane

    - ``existence`` -- boolean; instead of building the design, return:

      - ``True`` -- meaning that Sage knows how to build the design

      - ``Unknown`` -- meaning that Sage does not know how to build the
        design, but that the design may exist (see :mod:`sage.misc.unknown`)

      - ``False`` -- meaning that the design does not exist

    .. SEEALSO::

        * :func:`balanced_incomplete_block_design`

    EXAMPLES::

        sage: designs.biplane(4)                                                        # needs sage.rings.finite_rings
        (16,6,2)-Balanced Incomplete Block Design
        sage: designs.biplane(7, existence=True)                                        # needs sage.schemes
        True
        sage: designs.biplane(11)                                                       # needs sage.schemes
        (79,13,2)-Balanced Incomplete Block Design

    TESTS::

        sage: designs.biplane(9)                                                        # needs sage.libs.gap
        (56,11,2)-Balanced Incomplete Block Design

    Check all known biplanes::

        sage: [n for n in [0,1,2,3,4,7,9,11]                                            # needs sage.schemes
        ....:  if designs.biplane(n, existence=True) is True]
        [0, 1, 2, 3, 4, 7, 9, 11]
    """
def balanced_incomplete_block_design(v, k, lambd: int = 1, existence: bool = False, use_LJCR: bool = False):
    """
    Return a BIBD of parameters `v,k, \\lambda`.

    A Balanced Incomplete Block Design of parameters `v,k,\\lambda` is a collection
    `\\mathcal C` of `k`-subsets of `V=\\{0,\\dots,v-1\\}` such that for any two
    distinct elements `x,y\\in V` there are `\\lambda` elements `S\\in \\mathcal C`
    such that `x,y\\in S`.

    For more information on BIBD, see the
    :wikipedia:`corresponding Wikipedia entry <Block_design#Definition_of_a_BIBD_.28or_2-design.29>`.

    INPUT:

    - ``v``, ``k``, ``lambd`` -- integers

    - ``existence`` -- boolean; instead of building the design, return:

        - ``True`` -- meaning that Sage knows how to build the design

        - ``Unknown`` -- meaning that Sage does not know how to build the
          design, but that the design may exist (see :mod:`sage.misc.unknown`)

        - ``False`` -- meaning that the design does not exist

    - ``use_LJCR`` -- boolean; whether to query the La Jolla Covering
      Repository for the design when Sage does not know how to build it (see
      :func:`~sage.combinat.designs.covering_design.best_known_covering_design_www`). This
      requires internet.

    .. SEEALSO::

        * :func:`steiner_triple_system`
        * :func:`v_4_1_BIBD`
        * :func:`v_5_1_BIBD`

    .. TODO::

        Implement other constructions from the Handbook of Combinatorial
        Designs.

    EXAMPLES::

        sage: designs.balanced_incomplete_block_design(7, 3, 1).blocks()                # needs sage.schemes
        [[0, 1, 3], [0, 2, 4], [0, 5, 6], [1, 2, 6], [1, 4, 5], [2, 3, 5], [3, 4, 6]]
        sage: B = designs.balanced_incomplete_block_design(66, 6, 1,         # optional - internet
        ....:                                              use_LJCR=True)
        sage: B                                                              # optional - internet
        (66,6,1)-Balanced Incomplete Block Design
        sage: B.blocks()                                                     # optional - internet
        [[0, 1, 2, 3, 4, 65], [0, 5, 22, 32, 38, 58], [0, 6, 21, 30, 43, 48], ...
        sage: designs.balanced_incomplete_block_design(216, 6, 1)
        Traceback (most recent call last):
        ...
        NotImplementedError: I don't know how to build a (216,6,1)-BIBD!

    TESTS::

        sage: designs.balanced_incomplete_block_design(85,5,existence=True)
        True
        sage: _ = designs.balanced_incomplete_block_design(85,5)                        # needs sage.libs.pari

    A BIBD from a Finite Projective Plane::

        sage: _ = designs.balanced_incomplete_block_design(21,5)                        # needs sage.schemes

    Some trivial BIBD::

        sage: designs.balanced_incomplete_block_design(10,10)
        (10,10,1)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(1,10)
        (1,0,1)-Balanced Incomplete Block Design

    Existence of BIBD with `k=3,4,5`::

        sage: [v for v in range(50) if designs.balanced_incomplete_block_design(v,3,existence=True)]                    # needs sage.schemes
        [1, 3, 7, 9, 13, 15, 19, 21, 25, 27, 31, 33, 37, 39, 43, 45, 49]
        sage: [v for v in range(100) if designs.balanced_incomplete_block_design(v,4,existence=True)]                   # needs sage.schemes
        [1, 4, 13, 16, 25, 28, 37, 40, 49, 52, 61, 64, 73, 76, 85, 88, 97]
        sage: [v for v in range(150) if designs.balanced_incomplete_block_design(v,5,existence=True)]                   # needs sage.schemes
        [1, 5, 21, 25, 41, 45, 61, 65, 81, 85, 101, 105, 121, 125, 141, 145]

    For `k > 5` there are currently very few constructions::

        sage: [v for v in range(300) if designs.balanced_incomplete_block_design(v,6,existence=True) is True]           # needs sage.schemes
        [1, 6, 31, 66, 76, 91, 96, 106, 111, 121, 126, 136, 141, 151, 156, 171, 181, 186, 196, 201, 211, 241, 271]
        sage: [v for v in range(300) if designs.balanced_incomplete_block_design(v,6,existence=True) is Unknown]        # needs sage.schemes
        [51, 61, 81, 166, 216, 226, 231, 246, 256, 261, 276, 286, 291]

    Here are some constructions with `k \\geq 7` and `v` a prime power::

        sage: # needs sage.libs.pari
        sage: designs.balanced_incomplete_block_design(169,7)
        (169,7,1)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(617,8)
        (617,8,1)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(433,9)
        (433,9,1)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(1171,10)
        (1171,10,1)-Balanced Incomplete Block Design

    And we know some nonexistence results::

        sage: designs.balanced_incomplete_block_design(21,6,existence=True)
        False

    Some BIBDs with `\\lambda \\neq 1`::

        sage: designs.balanced_incomplete_block_design(176, 50, 14, existence=True)
        True
        sage: designs.balanced_incomplete_block_design(64,28,12)                        # needs sage.libs.pari
        (64,28,12)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(37,9,8)                          # needs sage.libs.pari
        (37,9,8)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(15,7,3)                          # needs sage.schemes
        (15,7,3)-Balanced Incomplete Block Design

    Some BIBDs from the recursive construction ::

        sage: designs.balanced_incomplete_block_design(76,16,4)                         # needs sage.libs.pari
        (76,16,4)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(10,4,2)                          # needs sage.libs.pari
        (10,4,2)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(50,25,24)                        # needs sage.schemes
        (50,25,24)-Balanced Incomplete Block Design
        sage: designs.balanced_incomplete_block_design(29,15,15)                        # needs sage.libs.pari sage.schemes
        (29,15,15)-Balanced Incomplete Block Design
    """
def BruckRyserChowla_check(v, k, lambd):
    """
    Check whether the parameters passed satisfy the Bruck-Ryser-Chowla theorem.

    For more information on the theorem, see the
    :wikipedia:`corresponding Wikipedia entry <Bruck–Ryser–Chowla_theorem>`.

    INPUT:

    - ``v``, ``k``, ``lambd`` -- integers; parameters to check

    OUTPUT: ``True`` -- the parameters satisfy the theorem

    - ``False`` -- the theorem fails for the given parameters

    - ``Unknown`` -- the preconditions of the theorem are not met

    EXAMPLES:

        sage: from sage.combinat.designs.bibd import BruckRyserChowla_check
        sage: BruckRyserChowla_check(22,7,2)
        False

    Nonexistence of projective planes of order 6 and 14

        sage: from sage.combinat.designs.bibd import BruckRyserChowla_check
        sage: BruckRyserChowla_check(43,7,1)                                            # needs sage.schemes
        False
        sage: BruckRyserChowla_check(211,15,1)                                          # needs sage.schemes
        False

    Existence of symmetric BIBDs with parameters `(79,13,2)` and `(56,11,2)`

        sage: from sage.combinat.designs.bibd import BruckRyserChowla_check
        sage: BruckRyserChowla_check(79,13,2)                                           # needs sage.schemes
        True
        sage: BruckRyserChowla_check(56,11,2)
        True

    TESTS:

    Test some non-symmetric parameters::

        sage: from sage.combinat.designs.bibd import BruckRyserChowla_check
        sage: BruckRyserChowla_check(89,11,3)
        Unknown
        sage: BruckRyserChowla_check(25,23,2)
        Unknown

    Clearly wrong parameters satisfying the theorem::

        sage: from sage.combinat.designs.bibd import BruckRyserChowla_check
        sage: BruckRyserChowla_check(13,25,50)                                          # needs sage.schemes
        True
    """
def steiner_triple_system(n):
    """
    Return a Steiner Triple System.

    A Steiner Triple System (STS) of a set `\\{0,...,n-1\\}`
    is a family `S` of 3-sets such that for any `i \\not = j`
    there exists exactly one set of `S` in which they are
    both contained.

    It can alternatively be thought of as a factorization of
    the complete graph `K_n` with triangles.

    A Steiner Triple System of a `n`-set exists if and only if
    `n \\equiv 1 \\pmod 6` or `n \\equiv 3 \\pmod 6`, in which case
    one can be found through Bose's and Skolem's constructions,
    respectively [AndHonk97]_.

    INPUT:

    - ``n`` -- return a Steiner Triple System of `\\{0,...,n-1\\}`

    EXAMPLES:

    A Steiner Triple System on `9` elements ::

        sage: sts = designs.steiner_triple_system(9)
        sage: sts
        (9,3,1)-Balanced Incomplete Block Design
        sage: list(sts)
        [[0, 1, 5], [0, 2, 4], [0, 3, 6], [0, 7, 8], [1, 2, 3],
         [1, 4, 7], [1, 6, 8], [2, 5, 8], [2, 6, 7], [3, 4, 8],
         [3, 5, 7], [4, 5, 6]]

    As any pair of vertices is covered once, its parameters are ::

        sage: sts.is_t_design(return_parameters=True)
        (True, (2, 9, 3, 1))

    An exception is raised for invalid values of ``n`` ::

        sage: designs.steiner_triple_system(10)
        Traceback (most recent call last):
        ...
        EmptySetError: Steiner triple systems only exist for n = 1 mod 6 or n = 3 mod 6

    REFERENCE:

    .. [AndHonk97] A short course in Combinatorial Designs,
      Ian Anderson, Iiro Honkala,
      Internet Editions, Spring 1997,
      http://www.utu.fi/~honkala/designs.ps
    """
def BIBD_from_TD(v, k, existence: bool = False):
    """
    Return a BIBD through TD-based constructions.

    INPUT:

    - ``v``, ``k`` -- integers; computes a `(v,k,1)`-BIBD

    - ``existence`` -- boolean; instead of building the design, return:

      - ``True`` -- meaning that Sage knows how to build the design

      - ``Unknown`` -- meaning that Sage does not know how to build the
        design, but that the design may exist (see :mod:`sage.misc.unknown`)

      - ``False`` -- meaning that the design does not exist

    This method implements three constructions:

    - If there exists a `TD(k,v)` and a `(v,k,1)`-BIBD then there exists a
      `(kv,k,1)`-BIBD.

      The BIBD is obtained from all blocks of the `TD`, and from the blocks of
      the `(v,k,1)`-BIBDs defined over the `k` groups of the `TD`.

    - If there exists a `TD(k,v)` and a `(v+1,k,1)`-BIBD then there exists a
      `(kv+1,k,1)`-BIBD.

      The BIBD is obtained from all blocks of the `TD`, and from the blocks of
      the `(v+1,k,1)`-BIBDs defined over the sets `V_1\\cup \\infty,\\dots,V_k\\cup
      \\infty` where the `V_1,\\dots,V_k` are the groups of the TD.

    - If there exists a `TD(k,v)` and a `(v+k,k,1)`-BIBD then there exists a
      `(kv+k,k,1)`-BIBD.

      The BIBD is obtained from all blocks of the `TD`, and from the blocks of
      the `(v+k,k,1)`-BIBDs defined over the sets `V_1\\cup
      \\{\\infty_1,\\dots,\\infty_k\\},\\dots,V_k\\cup \\{\\infty_1,\\dots,\\infty_k\\}`
      where the `V_1,\\dots,V_k` are the groups of the TD. By making sure that
      all copies of the `(v+k,k,1)`-BIBD contain the block
      `\\{\\infty_1,\\dots,\\infty_k\\}`, the result is also a BIBD.

    These constructions can be found in
    `<http://www.argilo.net/files/bibd.pdf>`_.

    EXAMPLES:

    First construction::

        sage: from sage.combinat.designs.bibd import BIBD_from_TD
        sage: BIBD_from_TD(25,5,existence=True)                                         # needs sage.schemes
        True
        sage: _ = BlockDesign(25,BIBD_from_TD(25,5))                                    # needs sage.schemes

    Second construction::

        sage: from sage.combinat.designs.bibd import BIBD_from_TD
        sage: BIBD_from_TD(21,5,existence=True)                                         # needs sage.schemes
        True
        sage: _ = BlockDesign(21,BIBD_from_TD(21,5))                                    # needs sage.schemes

    Third construction::

        sage: from sage.combinat.designs.bibd import BIBD_from_TD
        sage: BIBD_from_TD(85,5,existence=True)                                         # needs sage.schemes
        True
        sage: _ = BlockDesign(85,BIBD_from_TD(85,5))                                    # needs sage.schemes

    No idea::

        sage: from sage.combinat.designs.bibd import BIBD_from_TD
        sage: BIBD_from_TD(20,5,existence=True)
        Unknown
        sage: BIBD_from_TD(20,5)
        Traceback (most recent call last):
        ...
        NotImplementedError: I do not know how to build a (20,5,1)-BIBD!
    """
def BIBD_from_difference_family(G, D, lambd=None, check: bool = True):
    """
    Return the BIBD associated to the difference family ``D`` on the group ``G``.

    Let `G` be a group. A `(G,k,\\lambda)`-*difference family* is a family `B =
    \\{B_1,B_2,\\ldots,B_b\\}` of `k`-subsets of `G` such that for each element of
    `G \\backslash \\{0\\}` there exists exactly `\\lambda` pairs of elements
    `(x,y)`, `x` and `y` belonging to the same block, such that `x - y = g` (or
    x y^{-1} = g` in multiplicative notation).

    If `\\{B_1, B_2, \\ldots, B_b\\}` is a `(G,k,\\lambda)`-difference family then
    its set of translates `\\{B_i \\cdot g; i \\in \\{1,\\ldots,b\\}, g \\in G\\}` is a
    `(v,k,\\lambda)`-BIBD where `v` is the cardinality of `G`.

    INPUT:

    - ``G`` -- a finite additive Abelian group

    - ``D`` -- a difference family on ``G`` (short blocks are allowed)

    - ``lambd`` -- the `\\lambda` parameter (optional, only used if ``check`` is
      ``True``)

    - ``check`` -- boolean (default: ``True``); whether or not we check the output

    EXAMPLES::

        sage: G = Zmod(21)
        sage: D = [[0,1,4,14,16]]
        sage: sorted(G(x-y) for x in D[0] for y in D[0] if x != y)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        sage: from sage.combinat.designs.bibd import BIBD_from_difference_family
        sage: BIBD_from_difference_family(G, D)
        [[0, 1, 4, 14, 16],
         [1, 2, 5, 15, 17],
         [2, 3, 6, 16, 18],
         [3, 4, 7, 17, 19],
         [4, 5, 8, 18, 20],
         [5, 6, 9, 19, 0],
         [6, 7, 10, 20, 1],
         [7, 8, 11, 0, 2],
         [8, 9, 12, 1, 3],
         [9, 10, 13, 2, 4],
         [10, 11, 14, 3, 5],
         [11, 12, 15, 4, 6],
         [12, 13, 16, 5, 7],
         [13, 14, 17, 6, 8],
         [14, 15, 18, 7, 9],
         [15, 16, 19, 8, 10],
         [16, 17, 20, 9, 11],
         [17, 18, 0, 10, 12],
         [18, 19, 1, 11, 13],
         [19, 20, 2, 12, 14],
         [20, 0, 3, 13, 15]]
    """
def v_4_1_BIBD(v, check: bool = True):
    """
    Return a `(v,4,1)`-BIBD.

    A `(v,4,1)`-BIBD is an edge-decomposition of the complete graph `K_v` into
    copies of `K_4`. For more information, see
    :func:`balanced_incomplete_block_design`. It exists if and only if `v\\equiv 1,4
    \\pmod {12}`.

    See page 167 of [Stinson2004]_ for the construction details.

    .. SEEALSO::

        * :func:`balanced_incomplete_block_design`

    INPUT:

    - ``v`` -- integer; number of points

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: from sage.combinat.designs.bibd import v_4_1_BIBD  # long time
        sage: for n in range(13,100):                            # long time
        ....:    if n%12 in [1,4]:
        ....:       _ = v_4_1_BIBD(n, check = True)

    TESTS:

    Check that the `(25,4)` and `(37,4)`-difference family are available::

        sage: assert designs.difference_family(25,4,existence=True)
        sage: _ = designs.difference_family(25,4)
        sage: assert designs.difference_family(37,4,existence=True)
        sage: _ = designs.difference_family(37,4)

    Check some larger `(v,4,1)`-BIBD (see :issue:`17557`)::

        sage: for v in range(400):                                      # long time
        ....:     if v%12 in [1,4]:
        ....:         _ = designs.balanced_incomplete_block_design(v,4)
    """
def BIBD_from_PBD(PBD, v, k, check: bool = True, base_cases=None):
    """
    Return a `(v,k,1)`-BIBD from a `(r,K)`-PBD where `r=(v-1)/(k-1)`.

    This is Theorem 7.20 from [Stinson2004]_.

    INPUT:

    - ``v``, ``k`` -- integers

    - ``PBD`` -- a PBD on `r=(v-1)/(k-1)` points, such that for any block of
      ``PBD`` of size `s` there must exist a `((k-1)s+1,k,1)`-BIBD

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    - ``base_cases`` -- caching system, for internal use

    EXAMPLES::

        sage: from sage.combinat.designs.bibd import PBD_4_5_8_9_12
        sage: from sage.combinat.designs.bibd import BIBD_from_PBD
        sage: from sage.combinat.designs.bibd import is_pairwise_balanced_design
        sage: PBD = PBD_4_5_8_9_12(17)                                                  # needs sage.schemes
        sage: bibd = is_pairwise_balanced_design(BIBD_from_PBD(PBD,52,4),52,[4])        # needs sage.schemes
    """
def PBD_4_5_8_9_12(v, check: bool = True):
    """
    Return a `(v,\\{4,5,8,9,12\\})`-PBD on `v` elements.

    A `(v,\\{4,5,8,9,12\\})`-PBD exists if and only if `v\\equiv 0,1 \\pmod 4`. The
    construction implemented here appears page 168 in [Stinson2004]_.

    INPUT:

    - ``v`` -- integer congruent to `0` or `1` modulo `4`

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: designs.balanced_incomplete_block_design(40,4).blocks()  # indirect doctest           # needs sage.schemes
        [[0, 1, 2, 12], [0, 3, 6, 9], [0, 4, 8, 10],
         [0, 5, 7, 11], [0, 13, 26, 39], [0, 14, 25, 28],
         [0, 15, 27, 38], [0, 16, 22, 32], [0, 17, 23, 34],
        ...

    Check that :issue:`16476` is fixed::

        sage: from sage.combinat.designs.bibd import PBD_4_5_8_9_12
        sage: for v in (0,1,4,5,8,9,12,13,16,17,20,21,24,25):                           # needs sage.schemes
        ....:     _ = PBD_4_5_8_9_12(v)
    """

table_7_1: Incomplete

def v_5_1_BIBD(v, check: bool = True):
    """
    Return a `(v,5,1)`-BIBD.

    This method follows the construction from [ClaytonSmith]_.

    INPUT:

    - ``v`` -- integer

    .. SEEALSO::

        * :func:`balanced_incomplete_block_design`

    EXAMPLES::

        sage: from sage.combinat.designs.bibd import v_5_1_BIBD
        sage: i = 0
        sage: while i<200:                                                              # needs sage.libs.pari sage.schemes
        ....:    i += 20
        ....:    _ = v_5_1_BIBD(i+1)
        ....:    _ = v_5_1_BIBD(i+5)

    TESTS:

    Check that the needed difference families are there::

        sage: for v in [21,41,61,81,141,161,281]:                                       # needs sage.libs.pari
        ....:     assert designs.difference_family(v,5,existence=True)
        ....:     _ = designs.difference_family(v,5)
    """
def PBD_from_TD(k, t, u):
    """
    Return a `(kt,\\{k,t\\})`-PBD if `u=0` and a `(kt+u,\\{k,k+1,t,u\\})`-PBD otherwise.

    This is theorem 23 from [ClaytonSmith]_. The PBD is obtained from the blocks
    a truncated `TD(k+1,t)`, to which are added the blocks corresponding to the
    groups of the TD. When `u=0`, a `TD(k,t)` is used instead.

    INPUT:

    - ``k``, ``t``, ``u`` -- integers such that `0\\leq u \\leq t`

    EXAMPLES::

        sage: from sage.combinat.designs.bibd import PBD_from_TD
        sage: from sage.combinat.designs.bibd import is_pairwise_balanced_design
        sage: PBD = PBD_from_TD(2,2,1); PBD
        [[0, 2, 4], [0, 3], [1, 2], [1, 3, 4], [0, 1], [2, 3]]
        sage: is_pairwise_balanced_design(PBD,2*2+1,[2,3])
        True
    """
def BIBD_5q_5_for_q_prime_power(q):
    """
    Return a `(5q,5,1)`-BIBD with `q\\equiv 1\\pmod 4` a prime power.

    See Theorem 24 [ClaytonSmith]_.

    INPUT:

    - ``q`` -- integer; a prime power such that `q\\equiv 1\\pmod 4`

    EXAMPLES::

        sage: from sage.combinat.designs.bibd import BIBD_5q_5_for_q_prime_power
        sage: for q in [25, 45, 65, 85, 125, 145, 185, 205, 305, 405, 605]: # long time
        ....:     _ = BIBD_5q_5_for_q_prime_power(q/5)
    """
def BIBD_from_arc_in_desarguesian_projective_plane(n, k, existence: bool = False):
    """
    Return a `(n,k,1)`-BIBD from a maximal arc in a projective plane.

    This function implements a construction from Denniston [Denniston69]_, who
    describes a maximal :meth:`arc
    <sage.combinat.designs.bibd.BalancedIncompleteBlockDesign.arc>` in a
    :func:`Desarguesian Projective Plane
    <sage.combinat.designs.block_design.DesarguesianProjectivePlaneDesign>` of
    order `2^k`. From two powers of two `n,q` with `n<q`, it produces a
    `((n-1)(q+1)+1,n,1)`-BIBD.

    INPUT:

    - ``n``, ``k`` -- integers; must be powers of two (among other restrictions)

    - ``existence`` -- boolean; whether to return the BIBD obtained through
      this construction (default), or to merely indicate with a boolean return
      value whether this method *can* build the requested BIBD.

    EXAMPLES:

    A `(232,8,1)`-BIBD::

        sage: from sage.combinat.designs.bibd import BIBD_from_arc_in_desarguesian_projective_plane
        sage: from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign
        sage: D = BIBD_from_arc_in_desarguesian_projective_plane(232,8)                 # needs sage.libs.gap sage.modules sage.rings.finite_rings
        sage: BalancedIncompleteBlockDesign(232,D)                                      # needs sage.libs.gap sage.modules sage.rings.finite_rings
        (232,8,1)-Balanced Incomplete Block Design

    A `(120,8,1)`-BIBD::

        sage: D = BIBD_from_arc_in_desarguesian_projective_plane(120,8)                 # needs sage.libs.gap sage.modules sage.rings.finite_rings
        sage: BalancedIncompleteBlockDesign(120,D)                                      # needs sage.libs.gap sage.modules sage.rings.finite_rings
        (120,8,1)-Balanced Incomplete Block Design

    Other parameters::

        sage: all(BIBD_from_arc_in_desarguesian_projective_plane(n,k,existence=True)
        ....:     for n,k in
        ....:       [(120, 8), (232, 8), (456, 8), (904, 8), (496, 16),
        ....:        (976, 16), (1936, 16), (2016, 32), (4000, 32), (8128, 64)])
        True

    Of course, not all can be built this way::

        sage: BIBD_from_arc_in_desarguesian_projective_plane(7,3,existence=True)
        False
        sage: BIBD_from_arc_in_desarguesian_projective_plane(7,3)
        Traceback (most recent call last):
        ...
        ValueError: This function cannot produce a (7,3,1)-BIBD

    REFERENCE:

    .. [Denniston69] \\R. H. F. Denniston,
       Some maximal arcs in finite projective planes.
       Journal of Combinatorial Theory 6, no. 3 (1969): 317-319.
       :doi:`10.1016/S0021-9800(69)80095-5`
    """

class PairwiseBalancedDesign(GroupDivisibleDesign):
    """
    Pairwise Balanced Design (PBD).

    A Pairwise Balanced Design, or `(v,K,\\lambda)`-PBD, is a collection
    `\\mathcal B` of blocks defined on a set `X` of size `v`, such that any block
    pair of points `p_1,p_2\\in X` occurs in exactly `\\lambda` blocks of
    `\\mathcal B`. Besides, for every block `B\\in \\mathcal B` we must have
    `|B|\\in K`.

    INPUT:

    - ``points`` -- the underlying set; if ``points`` is an integer `v`, then
      the set is considered to be `\\{0, ..., v-1\\}`

    - ``blocks`` -- collection of blocks

    - ``K`` -- list of integers of which the sizes of the blocks must be
      elements; set to ``None`` (automatic guess) by default

    - ``lambd`` -- integer; value of `\\lambda`, set to `1` by default

    - ``check`` -- boolean; whether to check that the design is a `PBD` with
      the right parameters

    - ``copy`` -- (use with caution) if set to ``False`` then ``blocks`` must be
      a list of lists of integers. The list will not be copied but will be
      modified in place (each block is sorted, and the whole list is
      sorted). Your ``blocks`` object will become the instance's internal data.
    """
    def __init__(self, points, blocks, K=None, lambd: int = 1, check: bool = True, copy: bool = True, **kwds) -> None:
        """
        Constructor.

        EXAMPLES::

            sage: designs.balanced_incomplete_block_design(13,3) # indirect doctest
            (13,3,1)-Balanced Incomplete Block Design
        """

class BalancedIncompleteBlockDesign(PairwiseBalancedDesign):
    """
    Balanced Incomplete Block Design (BIBD).

    INPUT:

    - ``points`` -- the underlying set. If ``points`` is an integer `v`, then
      the set is considered to be `\\{0, ..., v-1\\}`

    - ``blocks`` -- collection of blocks

    - ``k`` -- integer; size of the blocks. Set to ``None`` (automatic guess)
      by default

    - ``lambd`` -- integer; value of `\\lambda`, set to `1` by default

    - ``check`` -- boolean; whether to check that the design is a `PBD` with
      the right parameters

    - ``copy`` -- (use with caution) if set to ``False`` then ``blocks`` must be
      a list of lists of integers. The list will not be copied but will be
      modified in place (each block is sorted, and the whole list is
      sorted). Your ``blocks`` object will become the instance's internal data.

    EXAMPLES::

        sage: b=designs.balanced_incomplete_block_design(9,3); b
        (9,3,1)-Balanced Incomplete Block Design
    """
    def __init__(self, points, blocks, k=None, lambd: int = 1, check: bool = True, copy: bool = True, **kwds) -> None:
        """
        Constructor.

        EXAMPLES::

            sage: b=designs.balanced_incomplete_block_design(9,3); b
            (9,3,1)-Balanced Incomplete Block Design
        """
    def arc(self, s: int = 2, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        '''
        Return the ``s``-arc with maximum cardinality.

        A `s`-arc is a subset of points in a BIBD that intersects each block on
        at most `s` points. It is one possible generalization of independent set
        for graphs.

        A simple counting shows that the cardinality of a `s`-arc is at most
        `(s-1) * r + 1` where `r` is the number of blocks incident to any point.
        A `s`-arc in a BIBD with cardinality `(s-1) * r + 1` is called maximal
        and is characterized by the following property: it is not empty and each
        block either contains `0` or `s` points of this arc. Equivalently, the
        trace of the BIBD on these points is again a BIBD (with block size `s`).

        For more informations, see :wikipedia:`Arc_(projective_geometry)`.

        INPUT:

        - ``s`` -- (default: `2`) the maximum number of points from the arc
          in each block

        - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear
          Programming (MILP) solver to be used. If set to ``None``, the default
          one is used. For more information on MILP solvers and which default
          solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- parameter for use with MILP solvers over
          an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES::

            sage: # needs sage.schemes
            sage: B = designs.balanced_incomplete_block_design(21, 5)
            sage: a2 = B.arc(); a2  # random
            [5, 9, 10, 12, 15, 20]
            sage: len(a2)
            6
            sage: a4 = B.arc(4); a4  # random
            [0, 1, 2, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20]
            sage: len(a4)
            16

        The `2`-arc and `4`-arc above are maximal. One can check that they
        intersect the blocks in either 0 or `s` points. Or equivalently that the
        traces are again BIBD::

            sage: r = (21-1)//(5-1)
            sage: 1 + r*1
            6
            sage: 1 + r*3
            16

            sage: B.trace(a2).is_t_design(2, return_parameters=True)                    # needs sage.schemes
            (True, (2, 6, 2, 1))
            sage: B.trace(a4).is_t_design(2, return_parameters=True)                    # needs sage.schemes
            (True, (2, 16, 4, 1))

        Some other examples which are not maximal::

            sage: # needs sage.numerical.mip
            sage: B = designs.balanced_incomplete_block_design(25, 4)
            sage: a2 = B.arc(2)
            sage: r = (25-1)//(4-1)
            sage: len(a2), 1 + r
            (8, 9)
            sage: sa2 = set(a2)
            sage: set(len(sa2.intersection(b)) for b in B.blocks())
            {0, 1, 2}
            sage: B.trace(a2).is_t_design(2)
            False

            sage: # needs sage.numerical.mip
            sage: a3 = B.arc(3)
            sage: len(a3), 1 + 2*r
            (15, 17)
            sage: sa3 = set(a3)
            sage: set(len(sa3.intersection(b)) for b in B.blocks()) == set([0,3])
            False
            sage: B.trace(a3).is_t_design(3)
            False

        TESTS:

        Test consistency with relabeling::

            sage: b = designs.balanced_incomplete_block_design(7,3)                     # needs sage.schemes
            sage: b.relabel(list("abcdefg"))                                            # needs sage.schemes
            sage: set(b.arc()).issubset(b.ground_set())                                 # needs sage.schemes
            True
        '''
BIBD = BalancedIncompleteBlockDesign
