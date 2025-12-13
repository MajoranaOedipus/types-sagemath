from _typeshed import Incomplete
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.combinat.composition import Composition as Composition
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class SuperPartition(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    A super partition.

    A *super partition* of size `n` and fermionic sector `m` is a
    pair consisting of a strict partition of some integer `r` of
    length `m` (that may end in a `0`) and an integer partition of
    `n - r`.

    EXAMPLES::

        sage: sp = SuperPartition([[1,0],[2,2,1]]); sp
        [1, 0; 2, 2, 1]
        sage: sp[0]
        (1, 0)
        sage: sp[1]
        (2, 2, 1)
        sage: sp.fermionic_degree()
        2
        sage: sp.bosonic_degree()
        6
        sage: sp.length()
        5
        sage: sp.conjugate()
        [4, 2; ]
    """
    @staticmethod
    def __classcall_private__(cls, lst):
        """
        Construct a superpartition in the correct parent.

        EXAMPLES::

            sage: SuperPartition([[1],[1]]).parent()
            Super Partitions
            sage: SuperPartition([[1],[1]])
            [1; 1]
            sage: SuperPartition([-1, 1])
            [1; 1]
            sage: SuperPartition([[1,1],[1]])
            Traceback (most recent call last):
            ...
            ValueError: [[1, 1], [1]] not in Super Partitions
            sage: SuperPartition([-1,1])
            [1; 1]
            sage: SuperPartition([])
            [; ]

            sage: SP = SuperPartitions(8,4)([[3,2,1,0],[2]])
            sage: SuperPartition(SP) is SP
            True
        """
    def __init__(self, parent, lst, check: bool = True, immutable: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SP = SuperPartition([[1],[1]])
            sage: TestSuite(SP).run()
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid super partition.

        EXAMPLES::

            sage: SP = SuperPartition([[1],[1]])
            sage: SP.check()
        """
    def __richcmp__(self, other, op) -> bool:
        """
        Check whether ``self`` is equal to ``other``.

        .. TODO::

            This overwrites the equality check of
            :class:`~sage.structure.list_clone.ClonableArray`
            in order to circumvent the coercion framework.
            Eventually this should be solved more elegantly.

            For now, two elements are compared by their defining lists.
        """
    def to_list(self) -> list:
        """
        The list of two lists with the antisymmetric and symmetric parts.

        EXAMPLES::

            sage: SuperPartition([[1],[1]]).to_list()
            [[1], [1]]
            sage: SuperPartition([[],[1]]).to_list()
            [[], [1]]
        """
    def to_composition(self) -> Composition:
        """
        Concatenate the antisymmetric and symmetric parts to a composition.

        OUTPUT:

        - a (possibly weak) composition

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).to_composition()
            [3, 1, 2, 2, 1]
            sage: SuperPartition([[2,1,0],[3,3]]).to_composition()
            [2, 1, 0, 3, 3]
            sage: SuperPartition([[2,1,0],[3,3]]).to_composition().parent()
            Compositions of nonnegative integers
        """
    def to_partition(self) -> Partition:
        """
        Concatenate and sort the antisymmetric and symmetric parts
        to a partition.

        OUTPUT: a partition

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).to_partition()
            [3, 2, 2, 1, 1]
            sage: SuperPartition([[2,1,0],[3,3]]).to_partition()
            [3, 3, 2, 1]
            sage: SuperPartition([[2,1,0],[3,3]]).to_partition().parent()
            Partitions
        """
    def antisymmetric_part(self) -> list:
        """
        The antisymmetric part as a list of strictly decreasing integers.

        OUTPUT: list

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).antisymmetric_part()
            [3, 1]
            sage: SuperPartition([[2,1,0],[3,3]]).antisymmetric_part()
            [2, 1, 0]
        """
    a_part = antisymmetric_part
    def symmetric_part(self) -> list:
        """
        The symmetric part as a list of weakly decreasing integers.

        OUTPUT: list

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).symmetric_part()
            [2, 2, 1]
            sage: SuperPartition([[2,1,0],[3,3]]).symmetric_part()
            [3, 3]
        """
    s_part = symmetric_part
    def bosonic_degree(self) -> int:
        """
        Return the bosonic degree of ``self``.

        The *bosonic degree* is the sum of the sizes of the
        antisymmetric and symmetric parts.

        OUTPUT: integer

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).bosonic_degree()
            9
            sage: SuperPartition([[2,1,0],[3,3]]).bosonic_degree()
            9
        """
    degree = bosonic_degree
    def fermionic_degree(self) -> int:
        """
        Return the fermionic degree of ``self``.

        The *fermionic degree* is the length of the antisymmetric part.

        OUTPUT: integer

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).fermionic_degree()
            2
            sage: SuperPartition([[2,1,0],[3,3]]).fermionic_degree()
            3
        """
    fermionic_sector = fermionic_degree
    def bi_degree(self) -> tuple:
        """
        Return the bidegree of ``self``, which is a pair consisting
        of the bosonic and fermionic degree.

        OUTPUT: a tuple of two integers

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).bi_degree()
            (9, 2)
            sage: SuperPartition([[2,1,0],[3,3]]).bi_degree()
            (9, 3)
        """
    def length(self) -> int:
        """
        Return the length of ``self``, which is the sum of the
        lengths of the antisymmetric and symmetric part.

        OUTPUT: integer

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).length()
            5
            sage: SuperPartition([[2,1,0],[3,3]]).length()
            5
        """
    def bosonic_length(self) -> int:
        """
        Return the length of the partition of the symmetric part.

        OUTPUT: integer

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).bosonic_length()
            3
            sage: SuperPartition([[2,1,0],[3,3]]).bosonic_length()
            2
        """
    def shape_circled_diagram(self) -> Partition:
        """
        A concatenated partition with an extra cell for each antisymmetric part

        OUTPUT: a partition

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).shape_circled_diagram()
            [4, 2, 2, 2, 1]
            sage: SuperPartition([[2,1,0],[3,3]]).shape_circled_diagram()
            [3, 3, 3, 2, 1]
        """
    @staticmethod
    def from_circled_diagram(shape, corners) -> SuperPartition:
        """
        Construct a super partition from a circled diagram.

        A circled diagram consists of a partition of the concatenation of
        the antisymmetric and symmetric parts and a list of addable cells
        of the partition which indicate the location of the circled cells.

        INPUT:

        - ``shape`` -- a partition or list of integers
        - ``corners`` -- list of removable cells of ``shape``

        OUTPUT: a :class:`SuperPartition`

        EXAMPLES::

            sage: SuperPartition.from_circled_diagram([3, 2, 2, 1, 1], [(0, 3), (3, 1)])
            [3, 1; 2, 2, 1]
            sage: SuperPartition.from_circled_diagram([3, 3, 2, 1], [(2, 2), (3, 1), (4, 0)])
            [2, 1, 0; 3, 3]
            sage: from_cd = SuperPartition.from_circled_diagram
            sage: all(sp == from_cd(*sp.to_circled_diagram()) for sp in SuperPartitions(4))
            True
        """
    def to_circled_diagram(self) -> list:
        """
        The shape of the circled diagram and a list of addable cells

        A circled diagram consists of a partition for the outer shape
        and a list of removable cells of the partition indicating the
        location of the circled cells

        OUTPUT: list consisting of a partition and a list of pairs of integers

        EXAMPLES::

            sage: SuperPartition([[3,1],[2,2,1]]).to_circled_diagram()
            [[3, 2, 2, 1, 1], [(0, 3), (3, 1)]]
            sage: SuperPartition([[2,1,0],[3,3]]).to_circled_diagram()
            [[3, 3, 2, 1], [(2, 2), (3, 1), (4, 0)]]
            sage: from_cd = SuperPartition.from_circled_diagram
            sage: all(sp == from_cd(*sp.to_circled_diagram()) for sp in SuperPartitions(4))
            True
        """
    def conjugate(self) -> SuperPartition:
        """
        Conjugate of a super partition.

        The *conjugate* of a super partition is defined by conjugating
        the circled diagram.

        OUTPUT: a :class:`SuperPartition`

        EXAMPLES::

            sage: SuperPartition([[3, 1, 0], [4, 3, 2, 1]]).conjugate()
            [6, 4, 1; 3]
            sage: all(sp == sp.conjugate().conjugate() for sp in SuperPartitions(4))
            True
            sage: all(sp.conjugate() in SuperPartitions(3,2) for sp in SuperPartitions(3,2))
            True
        """
    def zee(self) -> Integer:
        """
        Return the centralizer size of a permutation of cycle
        type symmetric part of ``self``.

        OUTPUT: a positive integer

        EXAMPLES::

            sage: SuperPartition([[1,0],[3,1,1]]).zee()
            6
            sage: SuperPartition([[1],[2,2,1]]).zee()
            8
            sage: sum(1/sp.zee() for sp in SuperPartitions(6,0))
            1
        """
    def sign(self) -> int:
        """
        Return the sign of a permutation of cycle type the
        symmetric part of ``self``.

        OUTPUT: either `1` or `-1`

        EXAMPLES::

            sage: SuperPartition([[1,0],[3,1,1]]).sign()
            -1
            sage: SuperPartition([[1,0],[3,2,1]]).sign()
            1
            sage: sum(sp.sign()/sp.zee() for sp in SuperPartitions(6,0))
            0
        """
    def dominates(self, other) -> bool:
        """
        Return ``True`` if and only if ``self`` dominates ``other``.

        If the symmetric and anti-symmetric parts of ``self`` and ``other``
        are not the same size then the result is ``False``.

        EXAMPLES::

            sage: LA = SuperPartition([[2,1],[2,1,1]])
            sage: LA.dominates([[2,1],[3,1]])
            False
            sage: LA.dominates([[2,1],[1,1,1,1]])
            True
            sage: LA.dominates([[3],[2,1,1]])
            False
            sage: LA.dominates([[1],[1]*6])
            False
        """
    def add_horizontal_border_strip_star(self, h) -> list:
        """
        Return a list of super partitions that differ from ``self``
        by a horizontal strip.

        The notion of horizontal strip comes from the Pieri rule for the
        Schur-star basis of symmetric functions in super space (see
        Theorem 7 from [JL2016]_).

        INPUT:

        - ``h`` -- number of cells in the horizontal strip

        OUTPUT: list of super partitions

        EXAMPLES::

            sage: SuperPartition([[4,1],[3]]).add_horizontal_border_strip_star(3)
            [[3, 1; 7],
             [4, 1; 6],
             [3, 0; 6, 2],
             [3, 1; 6, 1],
             [4, 0; 5, 2],
             [4, 1; 5, 1],
             [3, 0; 5, 3],
             [3, 1; 5, 2],
             [4, 0; 4, 3],
             [4, 1; 4, 2],
             [4, 1; 3, 3]]
            sage: SuperPartition([[2,1],[3]]).add_horizontal_border_strip_star(2)
            [[2, 1; 5], [2, 0; 4, 2], [2, 1; 4, 1], [2, 0; 3, 3], [2, 1; 3, 2]]
        """
    def add_horizontal_border_strip_star_bar(self, h) -> list:
        """
        List super partitions that differ from ``self`` by a horizontal strip.

        The notion of horizontal strip comes from the Pieri rule for the
        Schur-star-bar basis of symmetric functions in super space (see
        Theorem 10 from [JL2016]_).

        INPUT:

        - ``h`` -- number of cells in the horizontal strip

        OUTPUT: list of super partitions

        EXAMPLES::

            sage: SuperPartition([[4,1],[5,4]]).add_horizontal_border_strip_star_bar(3)
            [[4, 1; 8, 4],
             [4, 1; 7, 5],
             [4, 2; 7, 4],
             [4, 1; 7, 4, 1],
             [4, 2; 6, 5],
             [4, 1; 6, 5, 1],
             [4, 3; 6, 4],
             [4, 2; 6, 4, 1],
             [4, 1; 6, 4, 2],
             [4, 3; 5, 5],
             [4, 2; 5, 5, 1],
             [4, 1; 5, 5, 2],
             [4, 3; 5, 4, 1],
             [4, 1; 5, 4, 3]]
            sage: SuperPartition([[3,1],[5]]).add_horizontal_border_strip_star_bar(2)
            [[3, 1; 7],
             [4, 1; 6],
             [3, 2; 6],
             [3, 1; 6, 1],
             [4, 2; 5],
             [4, 1; 5, 1],
             [3, 2; 5, 1],
             [3, 1; 5, 2]]
        """

class SuperPartitions(UniqueRepresentation, Parent):
    """
    Super partitions.

    A super partition of size `n` and fermionic sector `m` is a
    pair consisting of a strict partition of some integer `r` of
    length `m` (that may end in a `0`) and an integer partition of
    `n - r`.

    INPUT:

    - ``n`` -- integer (default: ``None``)
    - ``m`` -- if ``n`` is specified, an integer (optional: default ``None``)

    Super partitions are the indexing set for symmetric functions
    in super space.

    EXAMPLES::

        sage: SuperPartitions()
        Super Partitions
        sage: SuperPartitions(2)
        Super Partitions of 2
        sage: SuperPartitions(2).cardinality()
        8
        sage: SuperPartitions(4,2)
        Super Partitions of 4 and of fermionic sector 2
        sage: [[2,0],[1,1]] in SuperPartitions(4,2)
        True
        sage: [[1,0],[1,1]] in SuperPartitions(4,2)
        False
        sage: [[1,0],[2,1]] in SuperPartitions(4)
        True
        sage: [[1,0],[2,2,1]] in SuperPartitions(4)
        False
        sage: [[1,0],[2,1]] in SuperPartitions()
        True
        sage: [[1,1],[2,1]] in SuperPartitions()
        False
    """
    @staticmethod
    def __classcall_private__(self, n=None, m=None, **kwargs):
        """
        Return the corresponding parent based upon input.

        TESTS::

            sage: from sage.combinat.superpartition import *
            sage: isinstance(SuperPartitions(), SuperPartitions_all)
            True
            sage: isinstance(SuperPartitions(3), SuperPartitions_n)
            True
            sage: isinstance(SuperPartitions(3,2), SuperPartitions_n_m)
            True

        ::

            sage: SP = SuperPartitions(5,2)
            sage: SP2 = SuperPartitions(int(5),int(2))
            sage: SP3 = SuperPartitions(ZZ(5),int(2))
            sage: SP is SP2
            True
            sage: SP is SP3
            True

        ::

            sage: SP = SuperPartitions(5)
            sage: SP2 = SuperPartitions(int(5))
            sage: SP3 = SuperPartitions(ZZ(5))
            sage: SP is SP2
            True
            sage: SP is SP3
            True
        """
    def __init__(self, is_infinite: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: SP = SuperPartitions()
            sage: TestSuite(SP).run()
        """
    Element = SuperPartition
    class options(GlobalOptions):
        NAME: str
        module: str
        display: Incomplete
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[1],[2,1]] in SuperPartitions()
            True
            sage: [[],[]] in SuperPartitions()
            True
            sage: [[0],[]] in SuperPartitions()
            True
            sage: [[],[0]] in SuperPartitions()
            True
            sage: [-1, 2, 1] in SuperPartitions()
            True
            sage: [2, -1, 1, 0] in SuperPartitions()
            True
            sage: [2, 0, 1, -1] in SuperPartitions()
            False
            sage: [] in SuperPartitions()
            True
            sage: [0] in SuperPartitions()
            True
        """

class SuperPartitions_n_m(SuperPartitions):
    n: Incomplete
    m: Incomplete
    def __init__(self, n, m) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: SP = SuperPartitions(3,2)
            sage: TestSuite(SP).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[3,2,1,0],[2]] in SuperPartitions(8,4)
            True
            sage: [[3,2,1,0],[]] in SuperPartitions(6,3)
            False
            sage: [[],[]] in SuperPartitions(0,0)
            True
            sage: [[0],[]] in SuperPartitions(0,1)
            True
            sage: [[],[]] in SuperPartitions(0,1)
            False
            sage: [-3,-2,-1,0,2] in SuperPartitions(8,4)
            True
            sage: [0] in SuperPartitions(0,0)
            False
            sage: [] in SuperPartitions(0,0)
            True
            sage: [0] in SuperPartitions(0,1)
            True
        """
    def __iter__(self):
        """
        An iterator for super partitions of degree ``n`` and sector ``m``.

        EXAMPLES::

            sage: SuperPartitions(6,2).cardinality()
            28
            sage: SuperPartitions(6,4).first()
            [3, 2, 1, 0; ]
        """

class SuperPartitions_n(SuperPartitions):
    n: Incomplete
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: SP = SuperPartitions(3)
            sage: TestSuite(SP).run()
        """
    def __contains__(self, x) -> bool:
        """
        EXAMPLES::

            sage: SuperPartitions(7)([[],[3,3,1]]) in SuperPartitions()
            True
            sage: SuperPartitions()([[],[3,3,1]]) in SuperPartitions(7)
            True
            sage: [[],[]] in SuperPartitions(0)
            True
            sage: [[0],[]] in SuperPartitions(0)
            True
            sage: [0] in SuperPartitions(0)
            True
            sage: [] in SuperPartitions(0)
            True
            sage: [1] in SuperPartitions(0)
            False
        """
    def __iter__(self):
        """
        An iterator for super partitions of degree ``n``.

        EXAMPLES::

            sage: SuperPartitions(1).list()
            [[; 1], [1; ], [0; 1], [1, 0; ]]
            sage: SuperPartitions(6).cardinality()
            80
        """

class SuperPartitions_all(SuperPartitions):
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: SP = SuperPartitions()
            sage: TestSuite(SP).run()
        """
    def __iter__(self):
        """
        Iterate over all super partitions.

        EXAMPLES::

            sage: SP = SuperPartitions()
            sage: it = SP.__iter__()
            sage: [next(it) for i in range(6)]
            [[; ], [0; ], [; 1], [1; ], [0; 1], [1, 0; ]]
        """
