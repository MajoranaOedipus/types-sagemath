from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial, factorial as factorial
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.combinat.combinat import catalan_number as catalan_number
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.set_partition import SetPartition as SetPartition, SetPartitions as SetPartitions, SetPartitions_set as SetPartitions_set
from sage.combinat.subset import Subsets as Subsets
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set, Set_generic as Set_generic

class SetPartitionsXkElement(SetPartition):
    """
    An element for the classes of ``SetPartitionXk`` where ``X`` is some
    letter.
    """
    def check(self) -> None:
        """
        Check to make sure this is a set partition.

        EXAMPLES::

            sage: A2p5 = SetPartitionsAk(2.5)
            sage: x = A2p5.first(); x
            {{-3, -2, -1, 1, 2, 3}}
            sage: x.check()
            sage: y = A2p5.next(x); y
            {{-3, 3}, {-2, -1, 1, 2}}
            sage: y.check()
        """

def SetPartitionsAk(k):
    """
    Return the combinatorial class of set partitions of type `A_k`.

    EXAMPLES::

        sage: A3 = SetPartitionsAk(3); A3
        Set partitions of {1, ..., 3, -1, ..., -3}

        sage: A3.first() #random
        {{1, 2, 3, -1, -3, -2}}
        sage: A3.last() #random
        {{-1}, {-2}, {3}, {1}, {-3}, {2}}
        sage: A3.random_element()  #random
        {{1, 3, -3, -1}, {2, -2}}

        sage: A3.cardinality()
        203

        sage: A2p5 = SetPartitionsAk(2.5); A2p5
        Set partitions of {1, ..., 3, -1, ..., -3} with 3 and -3 in the same block
        sage: A2p5.cardinality()
        52

        sage: A2p5.first() #random
        {{1, 2, 3, -1, -3, -2}}
        sage: A2p5.last() #random
        {{-1}, {-2}, {2}, {3, -3}, {1}}
        sage: A2p5.random_element() #random
        {{-1}, {-2}, {3, -3}, {1, 2}}
    """

class SetPartitionsAk_k(SetPartitions_set):
    k: Incomplete
    def __init__(self, k) -> None:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3); A3
            Set partitions of {1, ..., 3, -1, ..., -3}
            sage: A3 == loads(dumps(A3))
            True
        """
    Element = SetPartitionsXkElement

class SetPartitionsAkhalf_k(SetPartitions_set):
    k: Incomplete
    def __init__(self, k) -> None:
        """
        TESTS::

            sage: A2p5 = SetPartitionsAk(2.5); A2p5
            Set partitions of {1, ..., 3, -1, ..., -3} with 3 and -3 in the same block
            sage: A2p5 == loads(dumps(A2p5))
            True
        """
    Element = SetPartitionsXkElement
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A2p5 = SetPartitionsAk(2.5)
            sage: all(sp in A2p5 for sp in A2p5)
            True
            sage: A3 = SetPartitionsAk(3)
            sage: len([x for x in A3 if x in A2p5])
            52
            sage: A2p5.cardinality()
            52
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsAk(1.5).list() #random
            [{{1, 2, -2, -1}},
             {{2, -2, -1}, {1}},
             {{2, -2}, {1, -1}},
             {{-1}, {1, 2, -2}},
             {{-1}, {2, -2}, {1}}]

        ::

            sage: ks = [ 1.5, 2.5, 3.5 ]
            sage: aks = map(SetPartitionsAk, ks)
            sage: all(ak.cardinality() == len(ak.list()) for ak in aks)
            True
        """

def SetPartitionsSk(k):
    """
    Return the combinatorial class of set partitions of type `S_k`.

    There is a bijection between these set partitions and the
    permutations of `1, \\ldots, k`.

    EXAMPLES::

        sage: S3 = SetPartitionsSk(3); S3
        Set partitions of {1, ..., 3, -1, ..., -3} with propagating number 3
        sage: S3.cardinality()
        6

        sage: S3.list()  #random
        [{{2, -2}, {3, -3}, {1, -1}},
         {{1, -1}, {2, -3}, {3, -2}},
         {{2, -1}, {3, -3}, {1, -2}},
         {{1, -2}, {2, -3}, {3, -1}},
         {{1, -3}, {2, -1}, {3, -2}},
         {{1, -3}, {2, -2}, {3, -1}}]
        sage: S3.first() #random
        {{2, -2}, {3, -3}, {1, -1}}
        sage: S3.last() #random
        {{1, -3}, {2, -2}, {3, -1}}
        sage: S3.random_element() #random
        {{1, -3}, {2, -1}, {3, -2}}

        sage: S3p5 = SetPartitionsSk(3.5); S3p5
        Set partitions of {1, ..., 4, -1, ..., -4} with 4 and -4 in the same block and propagating number 4
        sage: S3p5.cardinality()
        6

        sage: S3p5.list() #random
        [{{2, -2}, {3, -3}, {1, -1}, {4, -4}},
         {{2, -3}, {1, -1}, {4, -4}, {3, -2}},
         {{2, -1}, {3, -3}, {1, -2}, {4, -4}},
         {{2, -3}, {1, -2}, {4, -4}, {3, -1}},
         {{1, -3}, {2, -1}, {4, -4}, {3, -2}},
         {{1, -3}, {2, -2}, {4, -4}, {3, -1}}]
        sage: S3p5.first() #random
        {{2, -2}, {3, -3}, {1, -1}, {4, -4}}
        sage: S3p5.last() #random
        {{1, -3}, {2, -2}, {4, -4}, {3, -1}}
        sage: S3p5.random_element() #random
        {{1, -3}, {2, -2}, {4, -4}, {3, -1}}
    """

class SetPartitionsSk_k(SetPartitionsAk_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3)
            sage: S3 = SetPartitionsSk(3)
            sage: all(sp in S3 for sp in S3)
            True
            sage: S3.cardinality()
            6
            sage: len([x for x in A3 if x in S3])
            6
        """
    def cardinality(self):
        """
        Return k!.

        TESTS::

            sage: SetPartitionsSk(2).cardinality()
            2
            sage: SetPartitionsSk(3).cardinality()
            6
            sage: SetPartitionsSk(4).cardinality()
            24
            sage: SetPartitionsSk(5).cardinality()
            120
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsSk(3).list() #random
            [{{2, -2}, {3, -3}, {1, -1}},
             {{1, -1}, {2, -3}, {3, -2}},
             {{2, -1}, {3, -3}, {1, -2}},
             {{1, -2}, {2, -3}, {3, -1}},
             {{1, -3}, {2, -1}, {3, -2}},
             {{1, -3}, {2, -2}, {3, -1}}]
            sage: ks = list(range(1, 6))
            sage: sks = map(SetPartitionsSk, ks)
            sage: all(sk.cardinality() == len(sk.list()) for sk in sks)
            True
        """

class SetPartitionsSkhalf_k(SetPartitionsAkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S2p5 = SetPartitionsSk(2.5)
            sage: A3 = SetPartitionsAk(3)
            sage: all(sp in S2p5 for sp in S2p5)
            True
            sage: len([x for x in A3 if x in S2p5])
            2
            sage: S2p5.cardinality()
            2
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsSk(2.5).cardinality()
            2
            sage: SetPartitionsSk(3.5).cardinality()
            6
            sage: SetPartitionsSk(4.5).cardinality()
            24

        ::

            sage: ks = [2.5, 3.5, 4.5, 5.5]
            sage: sks = [SetPartitionsSk(k) for k in ks]
            sage: all(sk.cardinality() == len(sk.list()) for sk in sks)
            True
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsSk(3.5).list() #random indirect test
            [{{2, -2}, {3, -3}, {1, -1}, {4, -4}},
             {{2, -3}, {1, -1}, {4, -4}, {3, -2}},
             {{2, -1}, {3, -3}, {1, -2}, {4, -4}},
             {{2, -3}, {1, -2}, {4, -4}, {3, -1}},
             {{1, -3}, {2, -1}, {4, -4}, {3, -2}},
             {{1, -3}, {2, -2}, {4, -4}, {3, -1}}]
        """

def SetPartitionsIk(k):
    """
    Return the combinatorial class of set partitions of type `I_k`.

    These are set partitions with a propagating number of less than `k`.
    Note that the identity set partition `\\{\\{1, -1\\}, \\ldots, \\{k, -k\\}\\}`
    is not in `I_k`.

    EXAMPLES::

        sage: I3 = SetPartitionsIk(3); I3
        Set partitions of {1, ..., 3, -1, ..., -3} with propagating number < 3
        sage: I3.cardinality()
        197

        sage: I3.first() #random
        {{1, 2, 3, -1, -3, -2}}
        sage: I3.last() #random
        {{-1}, {-2}, {3}, {1}, {-3}, {2}}
        sage: I3.random_element() #random
        {{-1}, {-3, -2}, {2, 3}, {1}}

        sage: I2p5 = SetPartitionsIk(2.5); I2p5
        Set partitions of {1, ..., 3, -1, ..., -3} with 3 and -3 in the same block and propagating number < 3
        sage: I2p5.cardinality()
        50

        sage: I2p5.first() #random
        {{1, 2, 3, -1, -3, -2}}
        sage: I2p5.last() #random
        {{-1}, {-2}, {2}, {3, -3}, {1}}
        sage: I2p5.random_element() #random
        {{-1}, {-2}, {1, 3, -3}, {2}}
    """

class SetPartitionsIk_k(SetPartitionsAk_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: I3 = SetPartitionsIk(3)
            sage: A3 = SetPartitionsAk(3)
            sage: all(sp in I3 for sp in I3)
            True
            sage: len([x for x in A3 if x in I3])
            197
            sage: I3.cardinality()
            197
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsIk(2).cardinality()
            13
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsIk(2).list() #random indirect test
                [{{1, 2, -1, -2}},
                 {{2, -1, -2}, {1}},
                 {{2}, {1, -1, -2}},
                 {{-1}, {1, 2, -2}},
                 {{-2}, {1, 2, -1}},
                 {{1, 2}, {-1, -2}},
                 {{2}, {-1, -2}, {1}},
                 {{-1}, {2, -2}, {1}},
                 {{-2}, {2, -1}, {1}},
                 {{-1}, {2}, {1, -2}},
                 {{-2}, {2}, {1, -1}},
                 {{-1}, {-2}, {1, 2}},
                 {{-1}, {-2}, {2}, {1}}]
        """

class SetPartitionsIkhalf_k(SetPartitionsAkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: I2p5 = SetPartitionsIk(2.5)
            sage: A3 = SetPartitionsAk(3)
            sage: all(sp in I2p5 for sp in I2p5)
            True
            sage: len([x for x in A3 if x in I2p5])
            50
            sage: I2p5.cardinality()
            50
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsIk(1.5).cardinality()
            4
            sage: SetPartitionsIk(2.5).cardinality()
            50
            sage: SetPartitionsIk(3.5).cardinality()
            871
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsIk(1.5).list() #random
            [{{1, 2, -2, -1}},
             {{2, -2, -1}, {1}},
             {{-1}, {1, 2, -2}},
             {{-1}, {2, -2}, {1}}]
        """

def SetPartitionsBk(k):
    """
    Return the combinatorial class of set partitions of type `B_k`.

    These are the set partitions where every block has size 2.

    EXAMPLES::

        sage: B3 = SetPartitionsBk(3); B3
        Set partitions of {1, ..., 3, -1, ..., -3} with block size 2

        sage: B3.first() #random
        {{2, -2}, {1, -3}, {3, -1}}
        sage: B3.last() #random
        {{1, 2}, {3, -2}, {-3, -1}}
        sage: B3.random_element() #random
        {{2, -1}, {1, -3}, {3, -2}}

        sage: B3.cardinality()
        15

        sage: B2p5 = SetPartitionsBk(2.5); B2p5
        Set partitions of {1, ..., 3, -1, ..., -3} with 3 and -3 in the same block and with block size 2

        sage: B2p5.first() #random
        {{2, -1}, {3, -3}, {1, -2}}
        sage: B2p5.last() #random
        {{1, 2}, {3, -3}, {-1, -2}}
        sage: B2p5.random_element() #random
        {{2, -2}, {3, -3}, {1, -1}}

        sage: B2p5.cardinality()
        3
    """

class SetPartitionsBk_k(SetPartitionsAk_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: B3 = SetPartitionsBk(3)
            sage: A3 = SetPartitionsAk(3)
            sage: len([x for x in A3 if x in B3])
            15
            sage: B3.cardinality()
            15
        """
    def cardinality(self):
        """
        Return the number of set partitions in `B_k` where `k` is an integer.

        This is given by (2k)!! = (2k-1)\\*(2k-3)\\*...\\*5\\*3\\*1.

        EXAMPLES::

            sage: SetPartitionsBk(3).cardinality()
            15
            sage: SetPartitionsBk(2).cardinality()
            3
            sage: SetPartitionsBk(1).cardinality()
            1
            sage: SetPartitionsBk(4).cardinality()
            105
            sage: SetPartitionsBk(5).cardinality()
            945
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsBk(1).list()
            [{{-1, 1}}]

        ::

            sage: SetPartitionsBk(2).list() #random
            [{{2, -1}, {1, -2}}, {{2, -2}, {1, -1}}, {{1, 2}, {-1, -2}}]
            sage: SetPartitionsBk(3).list() #random
            [{{2, -2}, {1, -3}, {3, -1}},
             {{2, -1}, {1, -3}, {3, -2}},
             {{1, -3}, {2, 3}, {-1, -2}},
             {{3, -1}, {1, -2}, {2, -3}},
             {{3, -2}, {1, -1}, {2, -3}},
             {{1, 3}, {2, -3}, {-1, -2}},
             {{2, -1}, {3, -3}, {1, -2}},
             {{2, -2}, {3, -3}, {1, -1}},
             {{1, 2}, {3, -3}, {-1, -2}},
             {{-3, -2}, {2, 3}, {1, -1}},
             {{1, 3}, {-3, -2}, {2, -1}},
             {{1, 2}, {3, -1}, {-3, -2}},
             {{-3, -1}, {2, 3}, {1, -2}},
             {{1, 3}, {-3, -1}, {2, -2}},
             {{1, 2}, {3, -2}, {-3, -1}}]

        Check to make sure that the number of elements generated is the
        same as what is given by cardinality()

        ::

            sage: bks = [SetPartitionsBk(i) for i in range(1, 6)]
            sage: all(bk.cardinality() == len(bk.list()) for bk in bks)
            True
        """

class SetPartitionsBkhalf_k(SetPartitionsAkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3)
            sage: B2p5 = SetPartitionsBk(2.5)
            sage: all(sp in B2p5 for sp in B2p5)
            True
            sage: len([x for x in A3 if x in B2p5])
            3
            sage: B2p5.cardinality()
            3
        """
    def cardinality(self):
        """
        TESTS::

            sage: B3p5 = SetPartitionsBk(3.5)
            sage: B3p5.cardinality()
            15
        """
    def __iter__(self):
        """
        TESTS::

            sage: B3p5 = SetPartitionsBk(3.5)
            sage: B3p5.cardinality()
            15

        ::

            sage: B3p5.list() #random
            [{{2, -2}, {1, -3}, {4, -4}, {3, -1}},
             {{2, -1}, {1, -3}, {4, -4}, {3, -2}},
             {{1, -3}, {2, 3}, {4, -4}, {-1, -2}},
             {{2, -3}, {1, -2}, {4, -4}, {3, -1}},
             {{2, -3}, {1, -1}, {4, -4}, {3, -2}},
             {{1, 3}, {4, -4}, {2, -3}, {-1, -2}},
             {{2, -1}, {3, -3}, {1, -2}, {4, -4}},
             {{2, -2}, {3, -3}, {1, -1}, {4, -4}},
             {{1, 2}, {3, -3}, {4, -4}, {-1, -2}},
             {{-3, -2}, {2, 3}, {1, -1}, {4, -4}},
             {{1, 3}, {-3, -2}, {2, -1}, {4, -4}},
             {{1, 2}, {-3, -2}, {4, -4}, {3, -1}},
             {{-3, -1}, {2, 3}, {1, -2}, {4, -4}},
             {{1, 3}, {-3, -1}, {2, -2}, {4, -4}},
             {{1, 2}, {-3, -1}, {4, -4}, {3, -2}}]
        """

def SetPartitionsPk(k):
    """
    Return the combinatorial class of set partitions of type `P_k`.

    These are the planar set partitions.

    EXAMPLES::

        sage: P3 = SetPartitionsPk(3); P3
        Set partitions of {1, ..., 3, -1, ..., -3} that are planar
        sage: P3.cardinality()
        132

        sage: P3.first() #random
        {{1, 2, 3, -1, -3, -2}}
        sage: P3.last() #random
        {{-1}, {-2}, {3}, {1}, {-3}, {2}}
        sage: P3.random_element() #random
        {{1, 2, -1}, {-3}, {3, -2}}

        sage: P2p5 = SetPartitionsPk(2.5); P2p5
        Set partitions of {1, ..., 3, -1, ..., -3} with 3 and -3 in the same block and that are planar
        sage: P2p5.cardinality()
        42

        sage: P2p5.first() #random
        {{1, 2, 3, -1, -3, -2}}
        sage: P2p5.last() #random
        {{-1}, {-2}, {2}, {3, -3}, {1}}
        sage: P2p5.random_element() #random
        {{1, 2, 3, -3}, {-1, -2}}
    """

class SetPartitionsPk_k(SetPartitionsAk_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: P3 = SetPartitionsPk(3)
            sage: A3 = SetPartitionsAk(3)
            sage: len([x for x in A3 if x in P3])
            132
            sage: P3.cardinality()
            132
            sage: all(sp in P3 for sp in P3)
            True
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsPk(2).cardinality()
            14
            sage: SetPartitionsPk(3).cardinality()
            132
            sage: SetPartitionsPk(4).cardinality()
            1430
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsPk(2).list() #random indirect test
            [{{1, 2, -1, -2}},
             {{2, -1, -2}, {1}},
             {{2}, {1, -1, -2}},
             {{-1}, {1, 2, -2}},
             {{-2}, {1, 2, -1}},
             {{2, -2}, {1, -1}},
             {{1, 2}, {-1, -2}},
             {{2}, {-1, -2}, {1}},
             {{-1}, {2, -2}, {1}},
             {{-2}, {2, -1}, {1}},
             {{-1}, {2}, {1, -2}},
             {{-2}, {2}, {1, -1}},
             {{-1}, {-2}, {1, 2}},
             {{-1}, {-2}, {2}, {1}}]
        """

class SetPartitionsPkhalf_k(SetPartitionsAkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3)
            sage: P2p5 = SetPartitionsPk(2.5)
            sage: all(sp in P2p5 for sp in P2p5)
            True
            sage: len([x for x in A3 if x in P2p5])
            42
            sage: P2p5.cardinality()
            42
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsPk(2.5).cardinality()
            42
            sage: SetPartitionsPk(1.5).cardinality()
            5
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsPk(1.5).list() #random
            [{{1, 2, -2, -1}},
             {{2, -2, -1}, {1}},
             {{2, -2}, {1, -1}},
             {{-1}, {1, 2, -2}},
             {{-1}, {2, -2}, {1}}]
        """

def SetPartitionsTk(k):
    """
    Return the combinatorial class of set partitions of type `T_k`.

    These are planar set partitions where every block is of size 2.

    EXAMPLES::

        sage: T3 = SetPartitionsTk(3); T3
        Set partitions of {1, ..., 3, -1, ..., -3} with block size 2 and that are planar
        sage: T3.cardinality()
        5

        sage: T3.first() #random
        {{1, -3}, {2, 3}, {-1, -2}}
        sage: T3.last() #random
        {{1, 2}, {3, -1}, {-3, -2}}
        sage: T3.random_element() #random
        {{1, -3}, {2, 3}, {-1, -2}}

        sage: T2p5 = SetPartitionsTk(2.5); T2p5
        Set partitions of {1, ..., 3, -1, ..., -3} with 3 and -3 in the same block and with block size 2 and that are planar
        sage: T2p5.cardinality()
        2

        sage: T2p5.first() #random
        {{2, -2}, {3, -3}, {1, -1}}
        sage: T2p5.last() #random
        {{1, 2}, {3, -3}, {-1, -2}}
    """

class SetPartitionsTk_k(SetPartitionsBk_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: T3 = SetPartitionsTk(3)
            sage: A3 = SetPartitionsAk(3)
            sage: all(sp in T3 for sp in T3)
            True
            sage: len([x for x in A3 if x in T3])
            5
            sage: T3.cardinality()
            5
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsTk(2).cardinality()
            2
            sage: SetPartitionsTk(3).cardinality()
            5
            sage: SetPartitionsTk(4).cardinality()
            14
            sage: SetPartitionsTk(5).cardinality()
            42
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsTk(3).list() #random
            [{{1, -3}, {2, 3}, {-1, -2}},
             {{2, -2}, {3, -3}, {1, -1}},
             {{1, 2}, {3, -3}, {-1, -2}},
             {{-3, -2}, {2, 3}, {1, -1}},
             {{1, 2}, {3, -1}, {-3, -2}}]
        """

class SetPartitionsTkhalf_k(SetPartitionsBkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3)
            sage: T2p5 = SetPartitionsTk(2.5)
            sage: all(sp in T2p5 for sp in T2p5)
            True
            sage: len([x for x in A3 if x in T2p5])
            2
            sage: T2p5.cardinality()
            2
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsTk(2.5).cardinality()
            2
            sage: SetPartitionsTk(3.5).cardinality()
            5
            sage: SetPartitionsTk(4.5).cardinality()
            14
        """
    def __iter__(self):
        """
        TESTS::

            sage: SetPartitionsTk(3.5).list() #random
            [{{1, -3}, {2, 3}, {4, -4}, {-1, -2}},
             {{2, -2}, {3, -3}, {1, -1}, {4, -4}},
             {{1, 2}, {3, -3}, {4, -4}, {-1, -2}},
             {{-3, -2}, {2, 3}, {1, -1}, {4, -4}},
             {{1, 2}, {-3, -2}, {4, -4}, {3, -1}}]
        """

def SetPartitionsRk(k):
    """
    Return the combinatorial class of set partitions of type `R_k`.

    EXAMPLES::

        sage: SetPartitionsRk(3)
        Set partitions of {1, ..., 3, -1, ..., -3} with at most 1 positive
         and negative entry in each block
    """

class SetPartitionsRk_k(SetPartitionsAk_k):
    k: Incomplete
    def __init__(self, k) -> None:
        """
        TESTS::

            sage: R3 = SetPartitionsRk(3); R3
            Set partitions of {1, ..., 3, -1, ..., -3} with at most 1 positive and negative entry in each block
            sage: R3 == loads(dumps(R3))
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: R3 = SetPartitionsRk(3)
            sage: A3 = SetPartitionsAk(3)
            sage: all(sp in R3 for sp in R3)
            True
            sage: len([x for x in A3 if x in R3])
            34
            sage: R3.cardinality()
            34
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsRk(2).cardinality()
            7
            sage: SetPartitionsRk(3).cardinality()
            34
            sage: SetPartitionsRk(4).cardinality()
            209
            sage: SetPartitionsRk(5).cardinality()
            1546
        """
    def __iter__(self):
        """
        TESTS::

            sage: len(SetPartitionsRk(3).list() ) == SetPartitionsRk(3).cardinality()
            True
        """

class SetPartitionsRkhalf_k(SetPartitionsAkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3)
            sage: R2p5 = SetPartitionsRk(2.5)
            sage: all(sp in R2p5 for sp in R2p5)
            True
            sage: len([x for x in A3 if x in R2p5])
            7
            sage: R2p5.cardinality()
            7
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsRk(2.5).cardinality()
            7
            sage: SetPartitionsRk(3.5).cardinality()
            34
            sage: SetPartitionsRk(4.5).cardinality()
            209
        """
    def __iter__(self):
        """
        TESTS::

            sage: R2p5 = SetPartitionsRk(2.5)
            sage: L = list(R2p5); L #random due to sets
            [{{-2}, {-1}, {3, -3}, {2}, {1}},
             {{-2}, {3, -3}, {2}, {1, -1}},
             {{-1}, {3, -3}, {2}, {1, -2}},
             {{-2}, {2, -1}, {3, -3}, {1}},
             {{-1}, {2, -2}, {3, -3}, {1}},
             {{2, -2}, {3, -3}, {1, -1}},
             {{2, -1}, {3, -3}, {1, -2}}]
            sage: len(L)
            7
        """

def SetPartitionsPRk(k):
    """
    Return the combinatorial class of set partitions of type `PR_k`.

    EXAMPLES::

        sage: SetPartitionsPRk(3)
        Set partitions of {1, ..., 3, -1, ..., -3} with at most 1 positive
         and negative entry in each block and that are planar
    """

class SetPartitionsPRk_k(SetPartitionsRk_k):
    k: Incomplete
    def __init__(self, k) -> None:
        """
        TESTS::

            sage: PR3 = SetPartitionsPRk(3); PR3
            Set partitions of {1, ..., 3, -1, ..., -3} with at most 1 positive and negative entry in each block and that are planar
            sage: PR3 == loads(dumps(PR3))
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: PR3 = SetPartitionsPRk(3)
            sage: A3 = SetPartitionsAk(3)
            sage: all(sp in PR3 for sp in PR3)
            True
            sage: len([x for x in A3 if x in PR3])
            20
            sage: PR3.cardinality()
            20
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsPRk(2).cardinality()
            6
            sage: SetPartitionsPRk(3).cardinality()
            20
            sage: SetPartitionsPRk(4).cardinality()
            70
            sage: SetPartitionsPRk(5).cardinality()
            252
        """
    def __iter__(self):
        """
        TESTS::

            sage: len(SetPartitionsPRk(3).list() ) == SetPartitionsPRk(3).cardinality()
            True
        """

class SetPartitionsPRkhalf_k(SetPartitionsRkhalf_k):
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: A3 = SetPartitionsAk(3)
            sage: PR2p5 = SetPartitionsPRk(2.5)
            sage: all(sp in PR2p5 for sp in PR2p5)
            True
            sage: len([x for x in A3 if x in PR2p5])
            6
            sage: PR2p5.cardinality()
            6
        """
    def cardinality(self):
        """
        TESTS::

            sage: SetPartitionsPRk(2.5).cardinality()
            6
            sage: SetPartitionsPRk(3.5).cardinality()
            20
            sage: SetPartitionsPRk(4.5).cardinality()
            70
        """
    def __iter__(self):
        """
        TESTS::

            sage: next(iter(SetPartitionsPRk(2.5)))
            {{-3, 3}, {-2}, {-1}, {1}, {2}}
            sage: len(list(SetPartitionsPRk(2.5)))
            6
        """

class PartitionAlgebra_generic(CombinatorialFreeModule):
    k: Incomplete
    n: Incomplete
    def __init__(self, R, cclass, n, k, name=None, prefix=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: s = PartitionAlgebra_sk(QQ, 3, 1)
            sage: TestSuite(s).run()
            sage: s == loads(dumps(s))
            True
        """
    def one_basis(self):
        """
        Return the basis index for the unit of the algebra.

        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: s = PartitionAlgebra_sk(ZZ, 3, 1)
            sage: len(s.one().support())   # indirect doctest
            1
        """
    def product_on_basis(self, left, right):
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: s = PartitionAlgebra_sk(QQ, 3, 1)
            sage: t12 = s(Set([Set([1,-2]),Set([2,-1]),Set([3,-3])]))
            sage: t12^2 == s(1) #indirect doctest
            True
        """

class PartitionAlgebraElement_generic(CombinatorialFreeModule.Element): ...
class PartitionAlgebraElement_ak(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_ak(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_ak(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

class PartitionAlgebraElement_bk(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_bk(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_bk(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

class PartitionAlgebraElement_sk(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_sk(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_sk(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

class PartitionAlgebraElement_pk(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_pk(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_pk(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

class PartitionAlgebraElement_tk(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_tk(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_tk(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

class PartitionAlgebraElement_rk(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_rk(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_rk(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

class PartitionAlgebraElement_prk(PartitionAlgebraElement_generic): ...

class PartitionAlgebra_prk(PartitionAlgebra_generic):
    def __init__(self, R, k, n, name=None) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.partition_algebra import *
            sage: p = PartitionAlgebra_prk(QQ, 3, 1)
            sage: p == loads(dumps(p))
            True
        """

def is_planar(sp):
    """
    Return ``True`` if the diagram corresponding to the set partition is
    planar; otherwise, it returns ``False``.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: pa.is_planar( pa.to_set_partition([[1,-2],[2,-1]]))
        False
        sage: pa.is_planar( pa.to_set_partition([[1,-1],[2,-2]]))
        True
    """
def to_graph(sp):
    """
    Return a graph representing the set partition ``sp``.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: g = pa.to_graph( pa.to_set_partition([[1,-2],[2,-1]])); g
        Graph on 4 vertices

        sage: g.vertices(sort=False) #random
        [1, 2, -2, -1]
        sage: g.edges(sort=False) #random
        [(1, -2, None), (2, -1, None)]
    """
def pair_to_graph(sp1, sp2):
    """
    Return a graph consisting of the disjoint union of the graphs of set
    partitions ``sp1`` and ``sp2`` along with edges joining the bottom
    row (negative numbers) of ``sp1`` to the top row (positive numbers)
    of ``sp2``.

    The vertices of the graph ``sp1`` appear in the result as pairs
    ``(k, 1)``, whereas the vertices of the graph ``sp2`` appear as
    pairs ``(k, 2)``.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: sp1 = pa.to_set_partition([[1,-2],[2,-1]])
        sage: sp2 = pa.to_set_partition([[1,-2],[2,-1]])
        sage: g = pa.pair_to_graph( sp1, sp2 ); g
        Graph on 8 vertices

    ::

        sage: g.vertices(sort=False) #random
        [(1, 2), (-1, 1), (-2, 2), (-1, 2), (-2, 1), (2, 1), (2, 2), (1, 1)]
        sage: g.edges(sort=False) #random
        [((1, 2), (-1, 1), None),
         ((1, 2), (-2, 2), None),
         ((-1, 1), (2, 1), None),
         ((-1, 2), (2, 2), None),
         ((-2, 1), (1, 1), None),
         ((-2, 1), (2, 2), None)]

    Another example which used to be wrong until :issue:`15958`::

        sage: sp3 = pa.to_set_partition([[1, -1], [2], [-2]])
        sage: sp4 = pa.to_set_partition([[1], [-1], [2], [-2]])
        sage: g = pa.pair_to_graph( sp3, sp4 ); g
        Graph on 8 vertices

        sage: g.vertices(sort=True)
        [(-2, 1), (-2, 2), (-1, 1), (-1, 2), (1, 1), (1, 2), (2, 1), (2, 2)]
        sage: g.edges(sort=True)
        [((-2, 1), (2, 2), None), ((-1, 1), (1, 1), None),
         ((-1, 1), (1, 2), None)]
    """
def propagating_number(sp):
    """
    Return the propagating number of the set partition ``sp``.

    The propagating number is the number of blocks with both a
    positive and negative number.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: sp1 = pa.to_set_partition([[1,-2],[2,-1]])
        sage: sp2 = pa.to_set_partition([[1,2],[-2,-1]])
        sage: pa.propagating_number(sp1)
        2
        sage: pa.propagating_number(sp2)
        0
    """
def to_set_partition(l, k=None):
    """
    Convert a list of a list of numbers to a set partitions.

    Each list of numbers in the outer list specifies the numbers
    contained in one of the blocks in the set partition.

    If k is specified, then the set partition will be a set partition
    of 1, ..., k, -1, ..., -k. Otherwise, k will default to the minimum
    number needed to contain all of the specified numbers.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: pa.to_set_partition([[1,-1],[2,-2]]) == pa.identity(2)
        True
    """
def identity(k):
    """
    Return the identity set partition `1, -1, \\ldots, k, -k`.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: pa.identity(2)
        {{2, -2}, {1, -1}}
    """
def set_partition_composition(sp1, sp2):
    """
    Return a tuple consisting of the composition of the set partitions
    sp1 and sp2 and the number of components removed from the middle
    rows of the graph.

    EXAMPLES::

        sage: import sage.combinat.partition_algebra as pa
        sage: sp1 = pa.to_set_partition([[1,-2],[2,-1]])
        sage: sp2 = pa.to_set_partition([[1,-2],[2,-1]])
        sage: pa.set_partition_composition(sp1, sp2) == (pa.identity(2), 0)
        True
    """
