from .bibd import balanced_incomplete_block_design as balanced_incomplete_block_design
from sage.arith.misc import is_prime_power as is_prime_power
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.combinat.designs.bibd import BalancedIncompleteBlockDesign as BalancedIncompleteBlockDesign
from sage.misc.unknown import Unknown as Unknown

def resolvable_balanced_incomplete_block_design(v, k, existence: bool = False):
    """
    Return a resolvable BIBD of parameters `v,k`.

    A BIBD is said to be *resolvable* if its blocks can be partitionned into
    parallel classes, i.e. partitions of the ground set.

    INPUT:

    - ``v``, ``k`` -- integers

    - ``existence`` -- boolean; instead of building the design, return:

        - ``True`` -- meaning that Sage knows how to build the design

        - ``Unknown`` -- meaning that Sage does not know how to build the
          design, but that the design may exist (see :mod:`sage.misc.unknown`)

        - ``False`` -- meaning that the design does not exist

    .. SEEALSO::

        - :meth:`IncidenceStructure.is_resolvable`
        - :func:`~sage.combinat.designs.bibd.balanced_incomplete_block_design`

    EXAMPLES::

        sage: KTS15 = designs.resolvable_balanced_incomplete_block_design(15,3)
        sage: KTS15
        (15,3,1)-Balanced Incomplete Block Design
        sage: KTS15.is_resolvable()
        True

    TESTS::

        sage: bibd = designs.resolvable_balanced_incomplete_block_design
        sage: for v in range(40):
        ....:     for k in range(v):
        ....:         if bibd(v,k,existence=True) is True:
        ....:             _ = bibd(v,k)
    """
def kirkman_triple_system(v, existence: bool = False):
    """
    Return a Kirkman Triple System on `v` points.

    A Kirkman Triple System `KTS(v)` is a resolvable Steiner Triple System. It
    exists if and only if `v\\equiv 3\\pmod{6}`.

    INPUT:

    - ``n`` -- integer

    - ``existence`` -- boolean (default: ``False``); whether to build the
      `KTS(n)` or only answer whether it exists

    .. SEEALSO::

        :meth:`IncidenceStructure.is_resolvable`

    EXAMPLES:

    A solution to Kirkmman's original problem::

        sage: kts = designs.kirkman_triple_system(15)
        sage: classes = kts.is_resolvable(1)[1]
        sage: names = '0123456789abcde'
        sage: def to_name(r_s_t):
        ....:     r, s, t = r_s_t
        ....:     return ' ' + names[r] + names[s] + names[t] + ' '
        sage: rows = ['   '.join(('Day {}'.format(i) for i in range(1,8)))]
        sage: rows.extend('   '.join(map(to_name,row)) for row in zip(*classes))
        sage: print('\\n'.join(rows))
        Day 1   Day 2   Day 3   Day 4   Day 5   Day 6   Day 7
         07e     18e     29e     3ae     4be     5ce     6de
         139     24a     35b     46c     05d     167     028
         26b     03c     14d     257     368     049     15a
         458     569     06a     01b     12c     23d     347
         acd     7bd     78c     89d     79a     8ab     9bc

    TESTS::

        sage: for i in range(3,300,6):                                                  # needs sage.combinat
        ....:     _ = designs.kirkman_triple_system(i)
    """
def v_4_1_rbibd(v, existence: bool = False):
    """
    Return a `(v,4,1)`-RBIBD.

    INPUT:

    - ``n`` -- integer

    - ``existence`` -- boolean (default: ``False``); whether to build the
      design or only answer whether it exists

    .. SEEALSO::

        - :meth:`IncidenceStructure.is_resolvable`
        - :func:`resolvable_balanced_incomplete_block_design`

    .. NOTE::

        A resolvable `(v,4,1)`-BIBD exists whenever `1\\equiv 4\\pmod(12)`. This
        function, however, only implements a construction of `(v,4,1)`-BIBD such
        that `v=3q+1\\equiv 1\\pmod{3}` where `q` is a prime power (see VII.7.5.a
        from [BJL99]_).

    EXAMPLES::

        sage: rBIBD = designs.resolvable_balanced_incomplete_block_design(28,4)
        sage: rBIBD.is_resolvable()
        True
        sage: rBIBD.is_t_design(return_parameters=True)
        (True, (2, 28, 4, 1))

    TESTS::

        sage: for q in prime_powers(2,30):  # indirect doctest
        ....:     if (3*q+1)%12 == 4:
        ....:         _ = designs.resolvable_balanced_incomplete_block_design(3*q+1,4)
    """
def PBD_4_7(v, check: bool = True, existence: bool = False):
    """
    Return a `(v,\\{4,7\\})`-PBD.

    For all `v` such that `n\\equiv 1\\pmod{3}` and `n\\neq 10,19, 31` there
    exists a `(v,\\{4,7\\})`-PBD. This is proved in Proposition IX.4.5
    from [BJL99]_, which this method implements.

    This construction of PBD is used by the construction of Kirkman Triple
    Systems.

    EXAMPLES::

        sage: from sage.combinat.designs.resolvable_bibd import PBD_4_7
        sage: PBD_4_7(22)
        Pairwise Balanced Design on 22 points with sets of sizes in [4, 7]

    TESTS:

    All values `\\leq 300`::

        sage: for i in range(1,300,3):                                                  # needs sage.schemes
        ....:     if i not in [10,19,31]:
        ....:         assert PBD_4_7(i,existence=True) is True
        ....:         _ = PBD_4_7(i,check=True)
    """
def PBD_4_7_from_Y(gdd, check: bool = True):
    """
    Return a `(3v+1,\\{4,7\\})`-PBD from a `(v,\\{4,5,7\\},\\NN-\\{3,6,10\\})`-GDD.

    This implements Lemma IX.3.11 from [BJL99]_ (p.625). All points of the GDD
    are tripled, and a `+\\infty` point is added to the design.

    - A group of size `s\\in Y=\\NN-\\{3,6,10\\}` becomes a set of size `3s`. Adding
      `\\infty` to it gives it size `3s+1`, and this set is then replaced by a
      `(3s+1,\\{4,7\\})`-PBD.

    - A block of size `s\\in\\{4,5,7\\}` becomes a `(3s,\\{4,7\\},\\{3\\})`-GDD.

    This lemma is part of the existence proof of `(v,\\{4,7\\})`-PBD as explained
    in IX.4.5 from [BJL99]_).

    INPUT:

    - ``gdd`` -- a `(v,\\{4,5,7\\},Y)`-GDD where `Y=\\NN-\\{3,6,10\\}`

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: from sage.combinat.designs.resolvable_bibd import PBD_4_7_from_Y
        sage: PBD_4_7_from_Y(designs.transversal_design(7,8))                           # needs sage.schemes
        Pairwise Balanced Design on 169 points with sets of sizes in [4, 7]

    TESTS::

        sage: PBD_4_7_from_Y(designs.balanced_incomplete_block_design(10,10))           # needs sage.schemes
        Traceback (most recent call last):
        ...
        ValueError: The GDD should only contain blocks of size {4,5,7} but there are other: [10]
        sage: PBD_4_7_from_Y(designs.transversal_design(4,3))                           # needs sage.schemes
        Traceback (most recent call last):
        ...
        RuntimeError: A group has size 3 but I do not know how to build a (10,[4,7])-PBD
    """
