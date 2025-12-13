from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.power import generic_power as generic_power
from sage.categories.associative_algebras import AssociativeAlgebras as AssociativeAlgebras
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import bell_number as bell_number, catalan_number as catalan_number
from sage.combinat.combinat_cython import perfect_matchings_iterator as perfect_matchings_iterator, set_partition_composition as set_partition_composition
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.set_partition import AbstractSetPartition as AbstractSetPartition, SetPartitions as SetPartitions
from sage.combinat.set_partition_iterator import set_partition_iterator as set_partition_iterator
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def partition_diagrams(k) -> Generator[Incomplete]:
    """
    Return a generator of all partition diagrams of order ``k``.

    A partition diagram of order `k \\in \\ZZ` to is a set partition of
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}`. If we have `k - 1/2 \\in ZZ`, then
    a partition diagram of order `k \\in 1/2 \\ZZ` is a set partition of
    `\\{1, \\ldots, k+1/2, -1, \\ldots, -(k+1/2)\\}` with `k+1/2` and `-(k+1/2)`
    in the same block. See [HR2005]_.

    INPUT:

    - ``k`` -- the order of the partition diagrams

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: [SetPartition(p) for p in da.partition_diagrams(2)]
        [{{-2, -1, 1, 2}},
         {{-2, 1, 2}, {-1}},
         {{-2}, {-1, 1, 2}},
         {{-2, -1}, {1, 2}},
         {{-2}, {-1}, {1, 2}},
         {{-2, -1, 1}, {2}},
         {{-2, 1}, {-1, 2}},
         {{-2, 1}, {-1}, {2}},
         {{-2, 2}, {-1, 1}},
         {{-2, -1, 2}, {1}},
         {{-2, 2}, {-1}, {1}},
         {{-2}, {-1, 1}, {2}},
         {{-2}, {-1, 2}, {1}},
         {{-2, -1}, {1}, {2}},
         {{-2}, {-1}, {1}, {2}}]
        sage: [SetPartition(p) for p in da.partition_diagrams(3/2)]
        [{{-2, -1, 1, 2}},
         {{-2, 1, 2}, {-1}},
         {{-2, 2}, {-1, 1}},
         {{-2, -1, 2}, {1}},
         {{-2, 2}, {-1}, {1}}]
    """
def brauer_diagrams(k) -> Generator[Incomplete]:
    """
    Return a generator of all Brauer diagrams of order ``k``.

    A Brauer diagram of order `k` is a partition diagram of order `k`
    with block size 2.

    INPUT:

    - ``k`` -- the order of the Brauer diagrams

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: [SetPartition(p) for p in da.brauer_diagrams(2)]
        [{{-2, -1}, {1, 2}}, {{-2, 1}, {-1, 2}}, {{-2, 2}, {-1, 1}}]
        sage: [SetPartition(p) for p in da.brauer_diagrams(5/2)]
        [{{-3, 3}, {-2, -1}, {1, 2}},
         {{-3, 3}, {-2, 1}, {-1, 2}},
         {{-3, 3}, {-2, 2}, {-1, 1}}]
    """
def temperley_lieb_diagrams(k) -> Generator[Incomplete]:
    """
    Return a generator of all Temperley--Lieb diagrams of order ``k``.

    A Temperley--Lieb diagram of order `k` is a partition diagram of order `k`
    with block size  2 and is planar.

    INPUT:

    - ``k`` -- the order of the Temperley--Lieb diagrams

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: [SetPartition(p) for p in da.temperley_lieb_diagrams(2)]
        [{{-2, -1}, {1, 2}}, {{-2, 2}, {-1, 1}}]
        sage: [SetPartition(p) for p in da.temperley_lieb_diagrams(5/2)]
        [{{-3, 3}, {-2, -1}, {1, 2}}, {{-3, 3}, {-2, 2}, {-1, 1}}]
    """
def planar_diagrams(k) -> Generator[Incomplete, Incomplete]:
    """
    Return a generator of all planar diagrams of order ``k``.

    A planar diagram of order `k` is a partition diagram of order `k`
    that has no crossings.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: all_diagrams = [SetPartition(p) for p in da.partition_diagrams(2)]
        sage: da2 = [SetPartition(p) for p in da.planar_diagrams(2)]
        sage: [p for p in all_diagrams if p not in da2]
        [{{-2, 1}, {-1, 2}}]
        sage: all_diagrams = [SetPartition(p) for p in da.partition_diagrams(5/2)]
        sage: da5o2 = [SetPartition(p) for p in da.planar_diagrams(5/2)]
        sage: [p for p in all_diagrams if p not in da5o2]
        [{{-3, -1, 3}, {-2, 1, 2}},
         {{-3, -2, 1, 3}, {-1, 2}},
         {{-3, -1, 1, 3}, {-2, 2}},
         {{-3, 1, 3}, {-2, -1, 2}},
         {{-3, 1, 3}, {-2, 2}, {-1}},
         {{-3, 1, 3}, {-2}, {-1, 2}},
         {{-3, -1, 2, 3}, {-2, 1}},
         {{-3, 3}, {-2, 1}, {-1, 2}},
         {{-3, -1, 3}, {-2, 1}, {2}},
         {{-3, -1, 3}, {-2, 2}, {1}}]
    """
def planar_partitions_rec(X) -> Generator[Incomplete]:
    """
    Iterate over all planar set partitions of ``X`` by using a
    recursive algorithm.

    ALGORITHM:

    To construct the set partition `\\rho = \\{\\rho_1, \\ldots, \\rho_k\\}` of
    `[n]`, we remove the part of the set partition containing the last
    element of ``X``, which, we consider to be `\\rho_k = \\{i_1, \\ldots, i_m\\}`
    without loss of generality. The remaining parts come from the planar set
    partitions of `\\{1, \\ldots, i_1-1\\}, \\{i_1+1, \\ldots, i_2-1\\}, \\ldots,
    \\{i_m+1, \\ldots, n\\}`.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: list(da.planar_partitions_rec([1,2,3]))
        [([1, 2], [3]), ([1], [2], [3]), ([2], [1, 3]), ([1], [2, 3]), ([1, 2, 3],)]
    """
def ideal_diagrams(k) -> Generator[Incomplete]:
    '''
    Return a generator of all "ideal" diagrams of order ``k``.

    An ideal diagram of order `k` is a partition diagram of order `k` with
    propagating number less than `k`.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: all_diagrams = da.partition_diagrams(2)
        sage: [SetPartition(p) for p in all_diagrams if p not in da.ideal_diagrams(2)]
        [{{-2, 1}, {-1, 2}}, {{-2, 2}, {-1, 1}}]

        sage: all_diagrams = da.partition_diagrams(3/2)
        sage: [SetPartition(p) for p in all_diagrams if p not in da.ideal_diagrams(3/2)]
        [{{-2, 2}, {-1, 1}}]
    '''

class AbstractPartitionDiagram(AbstractSetPartition):
    """
    Abstract base class for partition diagrams.

    This class represents a single partition diagram, that is used as a
    basis key for a diagram algebra element. A partition diagram should
    be a partition of the set  `\\{1, \\ldots, k, -1, \\ldots, -k\\}`. Each
    such set partition is regarded as a graph on nodes
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}` arranged in two rows, with nodes
    `1, \\ldots, k` in the top row from left to right and with nodes
    `-1, \\ldots, -k` in the bottom row from left to right, and an edge
    connecting two nodes if and only if the nodes lie in the same
    subset of the set partition.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: pd = da.AbstractPartitionDiagrams(2)
        sage: pd1 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
        sage: pd2 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
        sage: pd1
        {{-2, -1}, {1, 2}}
        sage: pd1 == pd2
        True
        sage: pd1 == [[1,2],[-1,-2]]
        True
        sage: pd1 == ((-2,-1),(2,1))
        True
        sage: pd1 == SetPartition([[1,2],[-1,-2]])
        True
        sage: pd3 = da.AbstractPartitionDiagram(pd, [[1,-2],[-1,2]])
        sage: pd1 == pd3
        False
        sage: pd4 = da.AbstractPartitionDiagram(pd, [[1,2],[3,4]])
        Traceback (most recent call last):
        ...
        ValueError: {{1, 2}, {3, 4}} does not represent two rows of vertices of order 2
    """
    def __init__(self, parent, d, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd1 = da.AbstractPartitionDiagram(pd, ((-2,-1),(1,2)) )
        """
    def check(self) -> None:
        """
        Check the validity of the input for the diagram.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd1 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]]) # indirect doctest
            sage: pd2 = da.AbstractPartitionDiagram(pd, [[1,2],[3,4]]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: {{1, 2}, {3, 4}} does not represent two rows of vertices of order 2
            sage: pd2 = da.AbstractPartitionDiagram(pd, [[1],[-1]]) # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: {{-1}, {1}} does not represent two rows of vertices of order 2

            sage: pd2 = da.AbstractPartitionDiagram(pd, [[[1,2],[-1,-2]]]) # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: unhashable type: 'list'
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd1 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
            sage: pd2 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
            sage: hash(pd1) == hash(pd2)
            True
            sage: hash(pd1) == hash( ((-2,-1), (1,2)) )
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd1 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
            sage: pd2 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
            sage: pd1 == pd2
            True
            sage: pd1 == [[1,2],[-1,-2]]
            True
            sage: pd1 == ((-2,-1),(2,1))
            True
            sage: pd1 == SetPartition([[1,2],[-1,-2]])
            True
            sage: pd3 = da.AbstractPartitionDiagram(pd, [[1,-2],[-1,2]])
            sage: pd1 == pd3
            False

        Check the inherited inequality::

            sage: pd1 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
            sage: pd2 = da.AbstractPartitionDiagram(pd, [[1,-2],[-1,2]])
            sage: pd1 != pd2
            True
            sage: pd1 != ((-2,-1),(2,1))
            False
        """
    def __lt__(self, other):
        """
        Compare less than.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd1 = da.AbstractPartitionDiagram(pd, [[1,2],[-1,-2]])
            sage: pd2 = da.AbstractPartitionDiagram(pd, [[1,-2],[-1,2]])
            sage: pd1 < pd2
            True
            sage: pd2 < pd1
            False
            sage: pd2 > pd1
            True
            sage: pd1 > pd2
            False
        """
    def base_diagram(self):
        """
        Return the underlying implementation of the diagram.

        OUTPUT: tuple of tuples of integers

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd([[1,2],[-1,-2]]).base_diagram() == ((-2,-1),(1,2))
            True
        """
    diagram = base_diagram
    def set_partition(self):
        """
        Return the underlying implementation of the diagram as a set of sets.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: X = pd([[1,2],[-1,-2]]).set_partition(); X
            {{-2, -1}, {1, 2}}
            sage: X.parent()
            Set partitions
        """
    def compose(self, other, check: bool = True):
        """
        Compose ``self`` with ``other``.

        The composition of two diagrams `X` and `Y` is given by placing
        `X` on top of `Y` and removing all loops.

        OUTPUT:

        A tuple where the first entry is the composite diagram and the
        second entry is how many loop were removed.

        .. NOTE::

            This is not really meant to be called directly, but it works
            to call it this way if desired.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd([[1,2],[-1,-2]]).compose(pd([[1,2],[-1,-2]]))
            ({{-2, -1}, {1, 2}}, 1)
        """
    def propagating_number(self):
        """
        Return the propagating number of the diagram.

        The propagating number is the number of blocks with both a
        positive and negative number.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: d1 = pd([[1,-2],[2,-1]])
            sage: d1.propagating_number()
            2
            sage: d2 = pd([[1,2],[-2,-1]])
            sage: d2.propagating_number()
            0
        """
    def count_blocks_of_size(self, n):
        """
        Count the number of blocks of a given size.

        INPUT:

        - ``n`` -- positive integer

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import PartitionDiagram
            sage: pd = PartitionDiagram([[1,-3,-5],[2,4],[3,-1,-2],[5],[-4]])
            sage: pd.count_blocks_of_size(1)
            2
            sage: pd.count_blocks_of_size(2)
            1
            sage: pd.count_blocks_of_size(3)
            2
        """
    def order(self):
        """
        Return the maximum entry in the diagram element.

        A diagram element will be a partition of the set
        `\\{-1, -2, \\ldots, -k, 1, 2, \\ldots, k\\}`.  The order of
        the diagram element is the value `k`.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import PartitionDiagram
            sage: PartitionDiagram([[1,-1],[2,-2,-3],[3]]).order()
            3
            sage: PartitionDiagram([[1,-1]]).order()
            1
            sage: PartitionDiagram([[1,-3,-5],[2,4],[3,-1,-2],[5],[-4]]).order()
            5
        """
    def is_planar(self):
        """
        Test if the diagram ``self`` is planar.

        A diagram element is planar if the graph of the nodes is planar.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import BrauerDiagram
            sage: BrauerDiagram([[1,-2],[2,-1]]).is_planar()
            False
            sage: BrauerDiagram([[1,-1],[2,-2]]).is_planar()
            True
        """
    def dual(self):
        """
        Return the dual diagram of ``self`` by flipping it top-to-bottom.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import PartitionDiagram
            sage: D = PartitionDiagram([[1,-1],[2,-2,-3],[3]])
            sage: D.dual()
            {{-3}, {-2, 2, 3}, {-1, 1}}
        """

class IdealDiagram(AbstractPartitionDiagram):
    """
    The element class for a ideal diagram.

    An ideal diagram for an integer `k` is a partition of the set
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}` where the propagating number is
    strictly smaller than the order.

    EXAMPLES::

        sage: from sage.combinat.diagram_algebras import IdealDiagrams as IDs
        sage: IDs(2)
        Ideal diagrams of order 2
        sage: IDs(2).list()
        [{{-2, -1, 1, 2}},
         {{-2, 1, 2}, {-1}},
         {{-2}, {-1, 1, 2}},
         {{-2, -1}, {1, 2}},
         {{-2}, {-1}, {1, 2}},
         {{-2, -1, 1}, {2}},
         {{-2, 1}, {-1}, {2}},
         {{-2, -1, 2}, {1}},
         {{-2, 2}, {-1}, {1}},
         {{-2}, {-1, 1}, {2}},
         {{-2}, {-1, 2}, {1}},
         {{-2, -1}, {1}, {2}},
         {{-2}, {-1}, {1}, {2}}]

        sage: from sage.combinat.diagram_algebras import PartitionDiagrams as PDs
        sage: PDs(4).cardinality() == factorial(4) + IDs(4).cardinality()
        True
    """
    @staticmethod
    def __classcall_private__(cls, diag):
        """
        Normalize input to initialize diagram.

        The order of the diagram element is the maximum value found in
        the list of lists.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import IdealDiagram
            sage: IdealDiagram([[1],[-1]])
            {{-1}, {1}}
            sage: IdealDiagram([[1], [-1]]).parent()
            Ideal diagrams of order 1
        """
    def check(self) -> None:
        """
        Check the validity of the input for ``self``.

        TESTS::

            sage: from sage.combinat.diagram_algebras import IdealDiagram
            sage: pd1 = IdealDiagram([[1,2],[-1,-2]])  # indirect doctest
            sage: pd2 = IdealDiagram([[1,-2],[2,-1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the diagram {{-2, 1}, {-1, 2}} must have a propagating number smaller than the order
            sage: pd3 = IdealDiagram([[1,2,-1,-3]])    # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: {{-3, -1, 1, 2}} does not represent two rows of vertices of order 2
            sage: pd4 = IdealDiagram([[1,-2,-1],[2]])  # indirect doctest
        """

class PlanarDiagram(AbstractPartitionDiagram):
    """
    The element class for a planar diagram.

    A planar diagram for an integer `k` is a partition of the set
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}` so that the diagram is non-crossing.

    EXAMPLES::

        sage: from sage.combinat.diagram_algebras import PlanarDiagrams
        sage: PlanarDiagrams(2)
        Planar diagrams of order 2
        sage: PlanarDiagrams(2).list()
        [{{-2}, {-1}, {1, 2}},
         {{-2}, {-1}, {1}, {2}},
         {{-2, 1}, {-1}, {2}},
         {{-2, 2}, {-1}, {1}},
         {{-2, 1, 2}, {-1}},
         {{-2, 2}, {-1, 1}},
         {{-2}, {-1, 1}, {2}},
         {{-2}, {-1, 2}, {1}},
         {{-2}, {-1, 1, 2}},
         {{-2, -1}, {1, 2}},
         {{-2, -1}, {1}, {2}},
         {{-2, -1, 1}, {2}},
         {{-2, -1, 2}, {1}},
         {{-2, -1, 1, 2}}]
    """
    @staticmethod
    def __classcall_private__(cls, diag):
        """
        Normalize input to initialize diagram.

        The order of the diagram element is the maximum value found in
        the list of lists.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import PlanarDiagram
            sage: PlanarDiagram([[1,-1]])
            {{-1, 1}}
            sage: PlanarDiagram([[1, -1]]).parent()
            Planar diagrams of order 1
        """
    def check(self) -> None:
        """
        Check the validity of the input for ``self``.

        TESTS::

            sage: from sage.combinat.diagram_algebras import PlanarDiagram
            sage: pd1 = PlanarDiagram([[1,2],[-1,-2]])  # indirect doctest
            sage: pd2 = PlanarDiagram([[1,-2],[2,-1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the diagram {{-2, 1}, {-1, 2}} must be planar
            sage: pd3 = PlanarDiagram([[1,2,-1,-3]])    # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: {{-3, -1, 1, 2}} does not represent two rows of vertices of order 2
            sage: pd4 = PlanarDiagram([[1,-2,-1],[2]])  # indirect doctest
        """

class TemperleyLiebDiagram(AbstractPartitionDiagram):
    """
    The element class for a Temperley-Lieb diagram.

    A Temperley-Lieb diagram for an integer `k` is a partition of the set
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}` so that the blocks are all of size
    2 and the diagram is planar.

    EXAMPLES::

        sage: from sage.combinat.diagram_algebras import TemperleyLiebDiagrams
        sage: TemperleyLiebDiagrams(2)
        Temperley Lieb diagrams of order 2
        sage: TemperleyLiebDiagrams(2).list()
        [{{-2, -1}, {1, 2}}, {{-2, 2}, {-1, 1}}]
    """
    @staticmethod
    def __classcall_private__(cls, diag):
        """
        Normalize input to initialize diagram.

        The order of the diagram element is the maximum value found in
        the list of lists.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import TemperleyLiebDiagram
            sage: TemperleyLiebDiagram([[1,-1]])
            {{-1, 1}}
            sage: TemperleyLiebDiagram([[1, -1]]).parent()
            Temperley Lieb diagrams of order 1
        """
    def check(self) -> None:
        """
        Check the validity of the input for ``self``.

        TESTS::

            sage: from sage.combinat.diagram_algebras import TemperleyLiebDiagram
            sage: pd1 = TemperleyLiebDiagram([[1,2],[-1,-2]])  # indirect doctest
            sage: pd2 = TemperleyLiebDiagram([[1,-2],[2,-1]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: the diagram {{-2, 1}, {-1, 2}} must be planar
            sage: pd3 = TemperleyLiebDiagram([[1,2,-1,-3]])    # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: {{-3, -1, 1, 2}} does not represent two rows of vertices of order 2
            sage: pd4 = TemperleyLiebDiagram([[1,-2,-1],[2]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: all blocks of {{-2, -1, 1}, {2}} must be of size 2
        """

class PartitionDiagram(AbstractPartitionDiagram):
    """
    The element class for a partition diagram.

    A partition diagram for an integer `k` is a partition of the set
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}`

    EXAMPLES::

        sage: from sage.combinat.diagram_algebras import PartitionDiagram, PartitionDiagrams
        sage: PartitionDiagrams(1)
        Partition diagrams of order 1
        sage: PartitionDiagrams(1).list()
        [{{-1, 1}}, {{-1}, {1}}]
        sage: PartitionDiagram([[1,-1]])
        {{-1, 1}}
        sage: PartitionDiagram(((1,-2),(2,-1))).parent()
        Partition diagrams of order 2
    """
    @staticmethod
    def __classcall_private__(cls, diag):
        """
        Normalize input to initialize diagram.

        The order of the diagram element is the maximum value found in
        the list of lists.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import PartitionDiagram
            sage: PartitionDiagram([[1],[-1]])
            {{-1}, {1}}
            sage: PartitionDiagram([[1],[-1]]).parent()
            Partition diagrams of order 1
        """

class BrauerDiagram(AbstractPartitionDiagram):
    """
    A Brauer diagram.

    A Brauer diagram for an integer `k` is a partition of the set
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}` with block size 2.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: bd = da.BrauerDiagrams(2)
        sage: bd1 = bd([[1,2],[-1,-2]])
        sage: bd2 = bd([[1,2,-1,-2]])
        Traceback (most recent call last):
        ...
        ValueError: all blocks of {{-2, -1, 1, 2}} must be of size 2

    TESTS::

        sage: import sage.combinat.diagram_algebras as da
        sage: bd = da.BrauerDiagrams(2)( ((-2,-1),(1,2)) )
        sage: TestSuite(bd).run()
    """
    @staticmethod
    def __classcall_private__(cls, diag):
        """
        Normalize input to initialize diagram.

        The order of the diagram element is the maximum value found in
        the list of lists.

        EXAMPLES::

            sage: from sage.combinat.diagram_algebras import BrauerDiagram
            sage: bd = BrauerDiagram([[1,-1]]); bd
            {{-1, 1}}
            sage: bd.parent()
            Brauer diagrams of order 1
        """
    def check(self) -> None:
        """
        Check the validity of the input for ``self``.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(2)
            sage: bd1 = bd([[1,2],[-1,-2]])  # indirect doctest
            sage: bd2 = bd([[1,2,-1,-2]])    # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: all blocks of {{-2, -1, 1, 2}} must be of size 2
        """
    class options(GlobalOptions):
        '''
        Set and display the global options for Brauer diagram (algebras). If no
        parameters are set, then the function returns a copy of the options
        dictionary.

        The ``options`` to diagram algebras can be accessed as the method
        :obj:`BrauerAlgebra.options` of :class:`BrauerAlgebra` and
        related classes.

        @OPTIONS@

        The compact representation ``[A/B;pi]`` of the Brauer algebra diagram
        (see [GL1996]_) has the following components:

        - ``A`` -- list of pairs of positive elements (upper row) that
          are connected

        - ``B`` -- list of pairs of negative elements (lower row) that
          are connected

        - ``pi`` -- a permutation that is to be interpreted as the relative
          order of the remaining elements in the top row and the bottom row

        EXAMPLES::

            sage: R.<q> = QQ[]
            sage: BA = BrauerAlgebra(2, q)
            sage: E = BA([[1,2],[-1,-2]])
            sage: E
            B{{-2, -1}, {1, 2}}
            sage: BA8 = BrauerAlgebra(8, q)
            sage: BA8([[1,-4],[2,4],[3,8],[-7,-2],[5,7],[6,-1],[-3,-5],[-6,-8]])
            B{{-8, -6}, {-7, -2}, {-5, -3}, {-4, 1}, {-1, 6}, {2, 4}, {3, 8}, {5, 7}}
            sage: BrauerAlgebra.options.display = "compact"
            sage: E
            B[12/12;]
            sage: BA8([[1,-4],[2,4],[3,8],[-7,-2],[5,7],[6,-1],[-3,-5],[-6,-8]])
            B[24.38.57/35.27.68;21]
            sage: BrauerAlgebra.options._reset()
        '''
        NAME: str
        module: str
        option_class: str
        display: Incomplete
    def involution_permutation_triple(self, curt: bool = True):
        """
        Return the involution permutation triple of ``self``.

        From Graham-Lehrer (see :class:`BrauerDiagrams`), a Brauer diagram
        is a triple `(D_1, D_2, \\pi)`, where:

        - `D_1` is a partition of the top nodes;
        - `D_2` is a partition of the bottom nodes;
        - `\\pi` is the induced permutation on the free nodes.

        INPUT:

        - ``curt`` -- boolean (default: ``True``); if ``True``, then return
          bijection on free nodes as a one-line notation (standardized to look
          like a permutation), else, return the honest mapping, a list of pairs
          `(i, -j)` describing the bijection on free nodes

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(3)
            sage: elm = bd([[1,2],[-2,-3],[3,-1]])
            sage: elm.involution_permutation_triple()
            ([(1, 2)], [(-3, -2)], [1])
            sage: elm.involution_permutation_triple(curt=False)
            ([(1, 2)], [(-3, -2)], [[3, -1]])
        """
    def bijection_on_free_nodes(self, two_line: bool = False):
        """
        Return the induced bijection - as a list of `(x,f(x))` values -
        from the free nodes on the top at the Brauer diagram to the free
        nodes at the bottom of ``self``.

        OUTPUT:

        If ``two_line`` is ``True``, then the output is the induced
        bijection as a two-row list ``(inputs, outputs)``.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(3)
            sage: elm = bd([[1,2],[-2,-3],[3,-1]])
            sage: elm.bijection_on_free_nodes()
            [[3, -1]]
            sage: elm2 = bd([[1,-2],[2,-3],[3,-1]])
            sage: elm2.bijection_on_free_nodes(two_line=True)
            [[1, 2, 3], [-2, -3, -1]]
        """
    def perm(self):
        """
        Return the induced bijection on the free nodes of ``self`` in
        one-line notation, re-indexed and treated as a permutation.

        .. SEEALSO::

            :meth:`bijection_on_free_nodes`

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(3)
            sage: elm = bd([[1,2],[-2,-3],[3,-1]])
            sage: elm.perm()
            [1]
        """
    def is_elementary_symmetric(self):
        """
        Check if is elementary symmetric.

        Let `(D_1, D_2, \\pi)` be the Graham-Lehrer representation
        of the Brauer diagram `d`. We say `d` is *elementary symmetric*
        if `D_1 = D_2` and `\\pi` is the identity.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(3)
            sage: elm = bd([[1,2],[-1,-2],[3,-3]])
            sage: elm.is_elementary_symmetric()
            True
            sage: elm2 = bd([[1,2],[-1,-3],[3,-2]])
            sage: elm2.is_elementary_symmetric()
            False
        """

class AbstractPartitionDiagrams(Parent, UniqueRepresentation):
    """
    This is an abstract base class for partition diagrams.

    The primary use of this class is to serve as basis keys for
    diagram algebras, but diagrams also have properties in their
    own right. Furthermore, this class is meant to be extended to
    create more efficient contains methods.

    INPUT:

    - ``order`` -- integer or integer `+ 1/2`; the order of the diagrams
    - ``category`` -- (default: ``FiniteEnumeratedSets()``) the category

    All concrete classes should implement attributes

    - ``_name`` -- the name of the class
    - ``_diagram_func`` -- an iterator function that takes the order
      as its only input

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: pd = da.PartitionDiagrams(2)
        sage: pd
        Partition diagrams of order 2
        sage: pd.an_element() in pd
        True
        sage: elm = pd([[1,2],[-1,-2]])
        sage: elm in pd
        True
    """
    Element = AbstractPartitionDiagram
    order: Incomplete
    def __init__(self, order, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.AbstractPartitionDiagrams(2)
            sage: pd.category()
            Category of finite enumerated sets
            sage: pd = da.AbstractPartitionDiagrams(2, Sets().Finite())
            sage: pd.category()
            Category of finite sets

            sage: pd = da.PartitionDiagrams(2)
            sage: TestSuite(pd).run()

            sage: bd = da.BrauerDiagrams(2)
            sage: TestSuite(bd).run()

            sage: td = da.TemperleyLiebDiagrams(2)
            sage: TestSuite(td).run()

            sage: pld = da.PlanarDiagrams(2)
            sage: TestSuite(pld).run()

            sage: id = da.IdealDiagrams(2)
            sage: TestSuite(id).run()
        """
    def __iter__(self):
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: list(da.PartitionDiagrams(2))
            [{{-2, -1, 1, 2}},
             {{-2, 1, 2}, {-1}},
             {{-2}, {-1, 1, 2}},
             {{-2, -1}, {1, 2}},
             {{-2}, {-1}, {1, 2}},
             {{-2, -1, 1}, {2}},
             {{-2, 1}, {-1, 2}},
             {{-2, 1}, {-1}, {2}},
             {{-2, 2}, {-1, 1}},
             {{-2, -1, 2}, {1}},
             {{-2, 2}, {-1}, {1}},
             {{-2}, {-1, 1}, {2}},
             {{-2}, {-1, 2}, {1}},
             {{-2, -1}, {1}, {2}},
             {{-2}, {-1}, {1}, {2}}]

            sage: list(da.PartitionDiagrams(3/2))
            [{{-2, -1, 1, 2}},
             {{-2, 1, 2}, {-1}},
             {{-2, 2}, {-1, 1}},
             {{-2, -1, 2}, {1}},
             {{-2, 2}, {-1}, {1}}]

            sage: list(da.BrauerDiagrams(5/2))
            [{{-3, 3}, {-2, -1}, {1, 2}},
             {{-3, 3}, {-2, 1}, {-1, 2}},
             {{-3, 3}, {-2, 2}, {-1, 1}}]
            sage: list(da.BrauerDiagrams(2))
            [{{-2, -1}, {1, 2}}, {{-2, 1}, {-1, 2}}, {{-2, 2}, {-1, 1}}]

            sage: list(da.TemperleyLiebDiagrams(5/2))
            [{{-3, 3}, {-2, -1}, {1, 2}}, {{-3, 3}, {-2, 2}, {-1, 1}}]
            sage: list(da.TemperleyLiebDiagrams(2))
            [{{-2, -1}, {1, 2}}, {{-2, 2}, {-1, 1}}]

            sage: list(da.PlanarDiagrams(3/2))
            [{{-2, 1, 2}, {-1}},
             {{-2, 2}, {-1}, {1}},
             {{-2, 2}, {-1, 1}},
             {{-2, -1, 2}, {1}},
             {{-2, -1, 1, 2}}]

            sage: list(da.PlanarDiagrams(2))
            [{{-2}, {-1}, {1, 2}},
             {{-2}, {-1}, {1}, {2}},
             {{-2, 1}, {-1}, {2}},
             {{-2, 2}, {-1}, {1}},
             {{-2, 1, 2}, {-1}},
             {{-2, 2}, {-1, 1}},
             {{-2}, {-1, 1}, {2}},
             {{-2}, {-1, 2}, {1}},
             {{-2}, {-1, 1, 2}},
             {{-2, -1}, {1, 2}},
             {{-2, -1}, {1}, {2}},
             {{-2, -1, 1}, {2}},
             {{-2, -1, 2}, {1}},
             {{-2, -1, 1, 2}}]

            sage: list(da.IdealDiagrams(3/2))
            [{{-2, -1, 1, 2}},
             {{-2, 1, 2}, {-1}},
             {{-2, -1, 2}, {1}},
             {{-2, 2}, {-1}, {1}}]
            sage: list(da.IdealDiagrams(2))
            [{{-2, -1, 1, 2}},
             {{-2, 1, 2}, {-1}},
             {{-2}, {-1, 1, 2}},
             {{-2, -1}, {1, 2}},
             {{-2}, {-1}, {1, 2}},
             {{-2, -1, 1}, {2}},
             {{-2, 1}, {-1}, {2}},
             {{-2, -1, 2}, {1}},
             {{-2, 2}, {-1}, {1}},
             {{-2}, {-1, 1}, {2}},
             {{-2}, {-1, 2}, {1}},
             {{-2, -1}, {1}, {2}},
             {{-2}, {-1}, {1}, {2}}]
        """
    def __contains__(self, obj) -> bool:
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.PartitionDiagrams(2)
            sage: pd.an_element() in pd
            True
            sage: elm = pd([[1,2],[-1,-2]])
            sage: elm in pd # indirect doctest
            True
        """

class PartitionDiagrams(AbstractPartitionDiagrams):
    """
    This class represents all partition diagrams of integer or integer
    `+ 1/2` order.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: pd = da.PartitionDiagrams(1); pd
        Partition diagrams of order 1
        sage: pd.list()
        [{{-1, 1}}, {{-1}, {1}}]

        sage: pd = da.PartitionDiagrams(3/2); pd
        Partition diagrams of order 3/2
        sage: pd.list()
        [{{-2, -1, 1, 2}},
         {{-2, 1, 2}, {-1}},
         {{-2, 2}, {-1, 1}},
         {{-2, -1, 2}, {1}},
         {{-2, 2}, {-1}, {1}}]

    TESTS::

        sage: import sage.combinat.diagram_algebras as da
        sage: pd = da.PartitionDiagrams(3)
        sage: pd.an_element() in pd
        True
        sage: pd.cardinality() == len(pd.list())
        True

        sage: pd = da.PartitionDiagrams(5/2)
        sage: pd.an_element() in pd
        True
        sage: pd.cardinality() == len(pd.list())
        True
    """
    Element = PartitionDiagram
    def cardinality(self):
        """
        The cardinality of partition diagrams of half-integer order `n` is
        the `2n`-th Bell number.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pd = da.PartitionDiagrams(3)
            sage: pd.cardinality()
            203

            sage: pd = da.PartitionDiagrams(7/2)
            sage: pd.cardinality()
            877
        """

class BrauerDiagrams(AbstractPartitionDiagrams):
    '''
    This class represents all Brauer diagrams of integer or integer
    `+1/2` order. For more information on Brauer diagrams,
    see :class:`BrauerAlgebra`.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: bd = da.BrauerDiagrams(2); bd
        Brauer diagrams of order 2
        sage: bd.list()
        [{{-2, -1}, {1, 2}}, {{-2, 1}, {-1, 2}}, {{-2, 2}, {-1, 1}}]

        sage: bd = da.BrauerDiagrams(5/2); bd
        Brauer diagrams of order 5/2
        sage: bd.list()
        [{{-3, 3}, {-2, -1}, {1, 2}},
         {{-3, 3}, {-2, 1}, {-1, 2}},
         {{-3, 3}, {-2, 2}, {-1, 1}}]

    TESTS::

        sage: import sage.combinat.diagram_algebras as da
        sage: bd = da.BrauerDiagrams(3)
        sage: bd.an_element() in bd
        True
        sage: bd.cardinality() == len(bd.list())
        True

        sage: bd = da.BrauerDiagrams(5/2)
        sage: bd.an_element() in bd
        True
        sage: bd.cardinality() == len(bd.list())
        True

    These diagrams also come equipped with a compact representation based
    on their bipartition triple representation. See the
    :meth:`from_involution_permutation_triple` method for more information.

    ::

        sage: bd = da.BrauerDiagrams(3)
        sage: bd.options.display="compact"
        sage: bd.list()
        [[12/12;1],
         [13/12;1],
         [23/12;1],
         [23/13;1],
         [23/23;1],
         [/;132],
         [/;231],
         [/;321],
         [13/13;1],
         [12/13;1],
         [12/23;1],
         [13/23;1],
         [/;312],
         [/;213],
         [/;123]]
        sage: bd.options._reset()
    '''
    Element = BrauerDiagram
    options = BrauerDiagram.options
    def __contains__(self, obj) -> bool:
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(2)
            sage: bd.an_element() in bd
            True
            sage: bd([[1,2],[-1,-2]]) in bd
            True
            sage: [[1,2,-1,-2]] in bd
            False
            sage: bd = da.BrauerDiagrams(3/2)
            sage: bd.an_element() in bd
            True
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of Brauer diagrams of integer order `k` is `(2k-1)!!`.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(3)
            sage: bd.cardinality()
            15

            sage: bd = da.BrauerDiagrams(7/2)
            sage: bd.cardinality()
            15
        """
    def symmetric_diagrams(self, l=None, perm=None):
        """
        Return the list of Brauer diagrams with symmetric placement of `l` arcs,
        and with free nodes permuted according to `perm`.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(4)
            sage: bd.symmetric_diagrams(l=1, perm=[2,1])
            [{{-4, -2}, {-3, 1}, {-1, 3}, {2, 4}},
             {{-4, -3}, {-2, 1}, {-1, 2}, {3, 4}},
             {{-4, -1}, {-3, 2}, {-2, 3}, {1, 4}},
             {{-4, 2}, {-3, -1}, {-2, 4}, {1, 3}},
             {{-4, 3}, {-3, 4}, {-2, -1}, {1, 2}},
             {{-4, 1}, {-3, -2}, {-1, 4}, {2, 3}}]

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(3/2)
            sage: bd.symmetric_diagrams(l=1, perm=[2,1])
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented for integer order, not for order 3/2
        """
    def from_involution_permutation_triple(self, D1_D2_pi):
        """
        Construct a Brauer diagram of ``self`` from an involution
        permutation triple.

        A Brauer diagram can be represented as a triple where the first
        entry is a list of arcs on the top row of the diagram, the second
        entry is a list of arcs on the bottom row of the diagram, and the
        third entry is a permutation on the remaining nodes. This triple
        is called the *involution permutation triple*. For more
        information, see [GL1996]_.

        INPUT:

        - ``D1_D2_pi`` -- list or tuple where the first entry is a list of
          arcs on the top of the diagram, the second entry is a list of arcs
          on the bottom of the diagram, and the third entry is a permutation
          on the free nodes.

        REFERENCES:

        .. [GL1996] \\J.J. Graham and G.I. Lehrer, Cellular algebras.
           Inventiones mathematicae 123 (1996), 1--34.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(4)
            sage: bd.from_involution_permutation_triple([[[1,2]],[[3,4]],[2,1]])
            {{-4, -3}, {-2, 3}, {-1, 4}, {1, 2}}

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: bd = da.BrauerDiagrams(5/2)
            sage: bd.from_involution_permutation_triple([[[1,2]],[[3,4]],[2,1]])
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented for integer order, not for order 5/2
        """

class TemperleyLiebDiagrams(AbstractPartitionDiagrams):
    """
    All Temperley-Lieb diagrams of integer or integer `+1/2` order.

    For more information on Temperley-Lieb diagrams, see
    :class:`TemperleyLiebAlgebra`.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: td = da.TemperleyLiebDiagrams(3); td
        Temperley Lieb diagrams of order 3
        sage: td.list()
        [{{-3, 3}, {-2, -1}, {1, 2}},
         {{-3, 1}, {-2, -1}, {2, 3}},
         {{-3, -2}, {-1, 1}, {2, 3}},
         {{-3, -2}, {-1, 3}, {1, 2}},
         {{-3, 3}, {-2, 2}, {-1, 1}}]

        sage: td = da.TemperleyLiebDiagrams(5/2); td
        Temperley Lieb diagrams of order 5/2
        sage: td.list()
        [{{-3, 3}, {-2, -1}, {1, 2}}, {{-3, 3}, {-2, 2}, {-1, 1}}]

    TESTS::

        sage: import sage.combinat.diagram_algebras as da
        sage: td = da.TemperleyLiebDiagrams(3)
        sage: td.an_element() in td
        True
        sage: td.cardinality() == len(td.list())
        True

        sage: td = da.TemperleyLiebDiagrams(7/2)
        sage: td.an_element() in td
        True
        sage: td.cardinality() == len(td.list())
        True
    """
    Element = TemperleyLiebDiagram
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of Temperley--Lieb diagrams of integer order `k` is the
        `k`-th Catalan number.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: td = da.TemperleyLiebDiagrams(3)
            sage: td.cardinality()
            5
        """
    def __contains__(self, obj) -> bool:
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: td = da.TemperleyLiebDiagrams(2)
            sage: td.an_element() in td
            True
            sage: td([[1,2],[-1,-2]]) in td
            True
            sage: [[1,2],[-1,-2]] in td
            True
            sage: [[1,-2],[-1,2]] in td
            False
        """

class PlanarDiagrams(AbstractPartitionDiagrams):
    """
    All planar diagrams of integer or integer `+1/2` order.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: pld = da.PlanarDiagrams(1); pld
        Planar diagrams of order 1
        sage: pld.list()
        [{{-1, 1}}, {{-1}, {1}}]

        sage: pld = da.PlanarDiagrams(3/2); pld
        Planar diagrams of order 3/2
        sage: pld.list()
        [{{-2, 1, 2}, {-1}},
         {{-2, 2}, {-1}, {1}},
         {{-2, 2}, {-1, 1}},
         {{-2, -1, 2}, {1}},
         {{-2, -1, 1, 2}}]

    TESTS::

        sage: import sage.combinat.diagram_algebras as da
        sage: pld = da.PlanarDiagrams(3)
        sage: pld.an_element() in pld
        True
        sage: pld.cardinality() == len(pld.list())
        True
        sage: pld = da.PlanarDiagrams(5/2)
        sage: pld.an_element() in pld
        True
        sage: pld.cardinality() == len(pld.list())
        True
    """
    Element = PlanarDiagram
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of all planar diagrams of order `k` is the
        `2k`-th Catalan number.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: pld = da.PlanarDiagrams(3)
            sage: pld.cardinality()
            132
        """
    def __contains__(self, obj) -> bool:
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: pld = da.PlanarDiagrams(2)
            sage: pld.an_element() in pld
            True
            sage: pld([[1,2],[-1,-2]]) in pld
            True
            sage: [[1,2],[-1,-2]] in pld
            True
            sage: [[1,-2],[-1,2]] in pld
            False
        """

class IdealDiagrams(AbstractPartitionDiagrams):
    '''
    All "ideal" diagrams of integer or integer `+1/2` order.

    If `k` is an integer then an ideal diagram of order `k` is a partition
    diagram of order `k` with propagating number less than `k`.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: id = da.IdealDiagrams(3)
        sage: id.an_element() in id
        True
        sage: id.cardinality() == len(id.list())
        True
        sage: da.IdealDiagrams(3/2).list()
        [{{-2, -1, 1, 2}},
         {{-2, 1, 2}, {-1}},
         {{-2, -1, 2}, {1}},
         {{-2, 2}, {-1}, {1}}]
    '''
    Element = IdealDiagram
    def __contains__(self, obj) -> bool:
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: id = da.IdealDiagrams(2)
            sage: id.an_element() in id
            True
            sage: id([[1,2],[-1,-2]]) in id
            True
            sage: [[1,2],[-1,-2]] in id
            True
            sage: [[1,-2],[-1,2]] in id
            False
        """

class DiagramAlgebra(CombinatorialFreeModule):
    """
    Abstract class for diagram algebras and is not designed to be used
    directly.

    TESTS::

        sage: import sage.combinat.diagram_algebras as da
        sage: R.<x> = QQ[]
        sage: D = da.DiagramAlgebra(2, x, R, 'P', da.PartitionDiagrams(2))
        sage: list(D.basis())
        [P{{-2, -1, 1, 2}},
         P{{-2, 1, 2}, {-1}},
         P{{-2}, {-1, 1, 2}},
         P{{-2, -1}, {1, 2}},
         P{{-2}, {-1}, {1, 2}},
         P{{-2, -1, 1}, {2}},
         P{{-2, 1}, {-1, 2}},
         P{{-2, 1}, {-1}, {2}},
         P{{-2, 2}, {-1, 1}},
         P{{-2, -1, 2}, {1}},
         P{{-2, 2}, {-1}, {1}},
         P{{-2}, {-1, 1}, {2}},
         P{{-2}, {-1, 2}, {1}},
         P{{-2, -1}, {1}, {2}},
         P{{-2}, {-1}, {1}, {2}}]
    """
    def __init__(self, k, q, base_ring, prefix, diagrams, category=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``k`` -- the rank
        - ``q`` -- the deformation parameter
        - ``base_ring`` -- the base ring
        - ``prefix`` -- the prefix of our monomials
        - ``diagrams`` -- the object representing all the diagrams
          (i.e. indices for the basis elements)

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: R.<x> = QQ[]
            sage: D = da.DiagramBasis(2, x, R, 'P', da.PartitionDiagrams(2))
            sage: TestSuite(D).run()
        """
    def __getitem__(self, d):
        """
        Get the basis item of ``self`` indexed by ``d``.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: R.<x> = QQ[]
            sage: D = da.DiagramAlgebra(2, x, R, 'P', da.PartitionDiagrams(2))
            sage: sp = da.PartitionDiagrams(2)( [[1,2], [-1,-2]] )
            sage: D[sp]
            P{{-2, -1}, {1, 2}}
            sage: D[[1,-1,2,-2]]
            P{{-2, -1, 1, 2}}
            sage: D3 = da.DiagramAlgebra(3, x, R, 'P', da.PartitionDiagrams(3))
            sage: da.PartitionDiagrams(3)( [[1,2], [-1,-2]] )
            Traceback (most recent call last):
            ...
            ValueError: {{-2, -1}, {1, 2}} does not represent two rows of vertices of order 3
            sage: D3[sp]
            P{{-3, 3}, {-2, -1}, {1, 2}}
            sage: D3[[1,-1,2,-2]]
            P{{-3, 3}, {-2, -1, 1, 2}}
            sage: D3[[1,2,-2]]
            P{{-3, 3}, {-2, 1, 2}, {-1}}
            sage: P = PartitionAlgebra(3,x)
            sage: P[[1]]
            P{{-3, 3}, {-2, 2}, {-1}, {1}}
        """
    def order(self):
        """
        Return the order of ``self``.

        The order of a partition algebra is defined as half of the number
        of nodes in the diagrams.

        EXAMPLES::

            sage: q = var('q')                                                          # needs sage.symbolic
            sage: PA = PartitionAlgebra(2, q)                                           # needs sage.symbolic
            sage: PA.order()                                                            # needs sage.symbolic
            2
        """
    def set_partitions(self):
        """
        Return the collection of underlying set partitions indexing the
        basis elements of a given diagram algebra.

        .. TODO:: Is this really necessary? deprecate?

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: R.<x> = QQ[]
            sage: D = da.DiagramAlgebra(2, x, R, 'P', da.PartitionDiagrams(2))
            sage: list(D.set_partitions()) == list(da.PartitionDiagrams(2))
            True
        """
    class Element(CombinatorialFreeModule.Element):
        """
        An element of a diagram algebra.

        This subclass provides a few additional methods for
        partition algebra elements. Most element methods are
        already implemented elsewhere.
        """
        def diagram(self):
            """
            Return the underlying diagram of ``self`` if ``self`` is a basis
            element. Raises an error if ``self`` is not a basis element.

            EXAMPLES::

                sage: R.<x> = ZZ[]
                sage: P = PartitionAlgebra(2, x, R)
                sage: elt = 3*P([[1,2],[-2,-1]])
                sage: elt.diagram()
                {{-2, -1}, {1, 2}}
            """
        def diagrams(self):
            """
            Return the diagrams in the support of ``self``.

            EXAMPLES::

                sage: R.<x> = ZZ[]
                sage: P = PartitionAlgebra(2, x, R)
                sage: elt = 3*P([[1,2],[-2,-1]]) + P([[1,2],[-2], [-1]])
                sage: sorted(elt.diagrams(), key=str)
                [{{-2, -1}, {1, 2}}, {{-2}, {-1}, {1, 2}}]
            """

class UnitDiagramMixin:
    """
    Mixin class for diagram algebras that have the unit indexed by
    the :func:`identity_set_partition`.
    """
    @cached_method
    def one_basis(self):
        """
        The following constructs the identity element of ``self``.

        It is not called directly; instead one should use ``DA.one()`` if
        ``DA`` is a defined diagram algebra.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: P = PartitionAlgebra(2, x, R)
            sage: P.one_basis()
            {{-2, 2}, {-1, 1}}
        """

class DiagramBasis(DiagramAlgebra):
    """
    Abstract base class for diagram algebras in the diagram basis.
    """
    def product_on_basis(self, d1, d2):
        """
        Return the product `D_{d_1} D_{d_2}` by two basis diagrams.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: R.<x> = QQ[]
            sage: D = da.DiagramBasis(2, x, R, 'P', da.PartitionDiagrams(2))
            sage: sp = da.PartitionDiagrams(2)([[1,2],[-1,-2]])
            sage: D.product_on_basis(sp, sp)
            x*P{{-2, -1}, {1, 2}}
        """

class PartitionAlgebra(DiagramBasis, UnitDiagramMixin):
    '''
    A partition algebra.

    A partition algebra of rank `k` over a given ground ring `R` is an
    algebra with (`R`-module) basis indexed by the collection of set
    partitions of `\\{1, \\ldots, k, -1, \\ldots, -k\\}`. Each such set
    partition can be represented by a graph on nodes `\\{1, \\ldots, k, -1,
    \\ldots, -k\\}` arranged in two rows, with nodes `1, \\ldots, k` in the
    top row from left to right and with nodes `-1, \\ldots, -k` in the
    bottom row from left to right, and edges drawn such that the connected
    components of the graph are precisely the parts of the set partition.
    (This choice of edges is often not unique, and so there are often many
    graphs representing one and the same set partition; the representation
    nevertheless is useful and vivid. We often speak of "diagrams" to mean
    graphs up to such equivalence of choices of edges; of course, we could
    just as well speak of set partitions.)

    There is not just one partition algebra of given rank over a given
    ground ring, but rather a whole family of them, indexed by the
    elements of `R`. More precisely, for every `q \\in R`, the partition
    algebra of rank `k` over `R` with parameter `q` is defined to be the
    `R`-algebra with basis the collection of all set partitions of
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}`, where the product of two basis
    elements is given by the rule

    .. MATH::

        a \\cdot b = q^N (a \\circ b),

    where `a \\circ b` is the composite set partition obtained by placing
    the diagram (i.e., graph) of `a` above the diagram of `b`, identifying
    the bottom row nodes of `a` with the top row nodes of `b`, and
    omitting any closed "loops" in the middle. The number `N` is the
    number of connected components formed by the omitted loops.

    The parameter `q` is a deformation parameter. Taking `q = 1` produces
    the semigroup algebra (over the base ring) of the partition monoid,
    in which the product of two set partitions is simply given by their
    composition.

    The partition algebra is regarded as an example of a "diagram algebra"
    due to the fact that its natural basis is given by certain graphs
    often called diagrams.

    There are a number of predefined elements for the partition algebra.
    We define the cup/cap pair by :meth:`a()`. The simple transpositions
    are denoted :meth:`s()`. Finally, we define elements :meth:`e()`,
    where if `i = (2r+1)/2`, then ``e(i)`` contains the blocks `\\{r+1\\}`
    and `\\{-r-1\\}` and if `i \\in \\ZZ`, then `e_i` contains the block
    `\\{-i, -i-1, i, i+1\\}`, with all other blocks being `\\{-j, j\\}`.
    So we have::

        sage: P = PartitionAlgebra(4, 0)
        sage: P.a(2)
        P{{-4, 4}, {-3, -2}, {-1, 1}, {2, 3}}
        sage: P.e(3/2)
        P{{-4, 4}, {-3, 3}, {-2}, {-1, 1}, {2}}
        sage: P.e(2)
        P{{-4, 4}, {-3, -2, 2, 3}, {-1, 1}}
        sage: P.e(5/2)
        P{{-4, 4}, {-3}, {-2, 2}, {-1, 1}, {3}}
        sage: P.s(2)
        P{{-4, 4}, {-3, 2}, {-2, 3}, {-1, 1}}

    An excellent reference for partition algebras and their various
    subalgebras (Brauer algebra, Temperley--Lieb algebra, etc) is the
    paper [HR2005]_.

    INPUT:

    - ``k`` -- rank of the algebra

    - ``q`` -- the deformation parameter `q`

    - ``base_ring`` -- (default: ``None``) a ring containing ``q``; if
      ``None``, then Sage automatically chooses the parent of ``q``

    - ``prefix`` -- (default: ``\'P\'``) a label for the basis elements

    EXAMPLES:

    The following shorthand simultaneously defines the univariate polynomial
    ring over the rationals as well as the variable ``x``::

        sage: R.<x> = PolynomialRing(QQ)
        sage: R
        Univariate Polynomial Ring in x over Rational Field
        sage: x
        x
        sage: x.parent() is R
        True

    We now define the partition algebra of rank `2` with parameter ``x``
    over `\\ZZ` in the usual (diagram) basis::

        sage: R.<x> = ZZ[]
        sage: A2 = PartitionAlgebra(2, x, R)
        sage: A2
        Partition Algebra of rank 2 with parameter x
         over Univariate Polynomial Ring in x over Integer Ring
        sage: A2.basis().keys()
        Partition diagrams of order 2
        sage: A2.basis().keys()([[-2, 1, 2], [-1]])
        {{-2, 1, 2}, {-1}}
        sage: A2.basis().list()
        [P{{-2, -1, 1, 2}}, P{{-2, 1, 2}, {-1}},
         P{{-2}, {-1, 1, 2}}, P{{-2, -1}, {1, 2}},
         P{{-2}, {-1}, {1, 2}}, P{{-2, -1, 1}, {2}},
         P{{-2, 1}, {-1, 2}}, P{{-2, 1}, {-1}, {2}},
         P{{-2, 2}, {-1, 1}}, P{{-2, -1, 2}, {1}},
         P{{-2, 2}, {-1}, {1}}, P{{-2}, {-1, 1}, {2}},
         P{{-2}, {-1, 2}, {1}}, P{{-2, -1}, {1}, {2}},
         P{{-2}, {-1}, {1}, {2}}]
        sage: E = A2([[1,2],[-2,-1]]); E
        P{{-2, -1}, {1, 2}}
        sage: E in A2.basis().list()
        True
        sage: E^2
        x*P{{-2, -1}, {1, 2}}
        sage: E^5
        x^4*P{{-2, -1}, {1, 2}}
        sage: (A2([[2,-2],[-1,1]]) - 2*A2([[1,2],[-1,-2]]))^2
        (4*x-4)*P{{-2, -1}, {1, 2}} + P{{-2, 2}, {-1, 1}}

    Next, we construct an element::

        sage: a2 = A2.an_element(); a2
        3*P{{-2}, {-1, 1, 2}} + 2*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}

    There is a natural embedding into partition algebras on more
    elements, by adding identity strands::

        sage: A4 = PartitionAlgebra(4, x, R)
        sage: A4(a2)
        3*P{{-4, 4}, {-3, 3}, {-2}, {-1, 1, 2}}
         + 2*P{{-4, 4}, {-3, 3}, {-2, -1, 1, 2}}
         + 2*P{{-4, 4}, {-3, 3}, {-2, 1, 2}, {-1}}

    Thus, the empty partition corresponds to the identity::

        sage: A4([])
        P{{-4, 4}, {-3, 3}, {-2, 2}, {-1, 1}}
        sage: A4(5)
        5*P{{-4, 4}, {-3, 3}, {-2, 2}, {-1, 1}}

    The group algebra of the symmetric group is a subalgebra::

        sage: S3 = SymmetricGroupAlgebra(ZZ, 3)
        sage: s3 = S3.an_element(); s3
        [1, 2, 3] + 2*[1, 3, 2] + 3*[2, 1, 3] + [3, 1, 2]
        sage: A4(s3)
        P{{-4, 4}, {-3, 1}, {-2, 3}, {-1, 2}}
         + 2*P{{-4, 4}, {-3, 2}, {-2, 3}, {-1, 1}}
         + 3*P{{-4, 4}, {-3, 3}, {-2, 1}, {-1, 2}}
         + P{{-4, 4}, {-3, 3}, {-2, 2}, {-1, 1}}
        sage: A4([2,1])
        P{{-4, 4}, {-3, 3}, {-2, 1}, {-1, 2}}

    Be careful not to confuse the embedding of the group algebra of
    the symmetric group with the embedding of partial set partitions.
    The latter are embedded by adding the parts `\\{i,-i\\}` if
    possible, and singletons sets for the remaining parts::

        sage: A4([[2,1]])
        P{{-4, 4}, {-3, 3}, {-2}, {-1}, {1, 2}}
        sage: A4([[-1,3],[-2,-3,1]])
        P{{-4, 4}, {-3, -2, 1}, {-1, 3}, {2}}

    Another subalgebra is the Brauer algebra, which has perfect
    matchings as basis elements.  The group algebra of the
    symmetric group is in fact a subalgebra of the Brauer algebra::

        sage: B3 = BrauerAlgebra(3, x, R)
        sage: b3 = B3(s3); b3
        B{{-3, 1}, {-2, 3}, {-1, 2}} + 2*B{{-3, 2}, {-2, 3}, {-1, 1}}
         + 3*B{{-3, 3}, {-2, 1}, {-1, 2}} + B{{-3, 3}, {-2, 2}, {-1, 1}}

    An important basis of the partition algebra is the
    :meth:`orbit basis <orbit_basis>`::

        sage: O2 = A2.orbit_basis()
        sage: o2 = O2([[1,2],[-1,-2]]) + O2([[1,2,-1,-2]]); o2
        O{{-2, -1}, {1, 2}} + O{{-2, -1, 1, 2}}

    The diagram basis element corresponds to the sum of all orbit
    basis elements indexed by coarser set partitions::

        sage: A2(o2)
        P{{-2, -1}, {1, 2}}

    We can convert back from the orbit basis to the diagram basis::

        sage: o2 = O2.an_element(); o2
        3*O{{-2}, {-1, 1, 2}} + 2*O{{-2, -1, 1, 2}} + 2*O{{-2, 1, 2}, {-1}}
        sage: A2(o2)
        3*P{{-2}, {-1, 1, 2}} - 3*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}

    One can work with partition algebras using a symbol for the parameter,
    leaving the base ring unspecified. This implies that the underlying
    base ring is Sage\'s symbolic ring.

    ::

        sage: # needs sage.symbolic
        sage: q = var(\'q\')
        sage: PA = PartitionAlgebra(2, q); PA
        Partition Algebra of rank 2 with parameter q over Symbolic Ring
        sage: PA([[1,2],[-2,-1]])^2 == q*PA([[1,2],[-2,-1]])
        True
        sage: ((PA([[2, -2], [1, -1]]) - 2*PA([[-2, -1], [1, 2]]))^2
        ....:   == (4*q-4)*PA([[1, 2], [-2, -1]]) + PA([[2, -2], [1, -1]]))
        True

    The identity element of the partition algebra is the set
    partition `\\{\\{1,-1\\}, \\{2,-2\\}, \\ldots, \\{k,-k\\}\\}`::

        sage: # needs sage.symbolic
        sage: P = PA.basis().list()
        sage: PA.one()
        P{{-2, 2}, {-1, 1}}
        sage: PA.one() * P[7] == P[7]
        True
        sage: P[7] * PA.one() == P[7]
        True

    We now give some further examples of the use of the other arguments.
    One may wish to "specialize" the parameter to a chosen element of
    the base ring::

        sage: R.<q> = RR[]
        sage: PA = PartitionAlgebra(2, q, R, prefix=\'B\')
        sage: PA
        Partition Algebra of rank 2 with parameter q over
         Univariate Polynomial Ring in q over Real Field with 53 bits of precision
        sage: PA([[1,2],[-1,-2]])
        1.00000000000000*B{{-2, -1}, {1, 2}}
        sage: PA = PartitionAlgebra(2, 5, base_ring=ZZ, prefix=\'B\')
        sage: PA
        Partition Algebra of rank 2 with parameter 5 over Integer Ring
        sage: ((PA([[2, -2], [1, -1]]) - 2*PA([[-2, -1], [1, 2]]))^2
        ....:   == 16*PA([[-2, -1], [1, 2]]) + PA([[2, -2], [1, -1]]))
        True

    Symmetric group algebra elements and elements from other subalgebras
    of the partition algebra (e.g., ``BrauerAlgebra`` and
    ``TemperleyLiebAlgebra``) can also be coerced into the partition algebra::

        sage: # needs sage.symbolic
        sage: S = SymmetricGroupAlgebra(SR, 2)
        sage: B = BrauerAlgebra(2, x, SR)
        sage: A = PartitionAlgebra(2, x, SR)
        sage: S([2,1]) * A([[1,-1],[2,-2]])
        P{{-2, 1}, {-1, 2}}
        sage: B([[-1,-2],[2,1]]) * A([[1],[-1],[2,-2]])
        P{{-2}, {-1}, {1, 2}}
        sage: A([[1],[-1],[2,-2]]) * B([[-1,-2],[2,1]])
        P{{-2, -1}, {1}, {2}}

    The same is true if the elements come from a subalgebra of a partition
    algebra of smaller order, or if they are defined over a different
    base ring::

        sage: R = FractionField(ZZ[\'q\']); q = R.gen()
        sage: S = SymmetricGroupAlgebra(ZZ, 2)
        sage: B = BrauerAlgebra(2, q, ZZ[q])
        sage: A = PartitionAlgebra(3, q, R)
        sage: S([2,1]) * A([[1,-1],[2,-3],[3,-2]])
        P{{-3, 1}, {-2, 3}, {-1, 2}}
        sage: A(B([[-1,-2],[2,1]]))
        P{{-3, 3}, {-2, -1}, {1, 2}}

    TESTS:

    A computation that returned an incorrect result until :issue:`15958`::

        sage: A = PartitionAlgebra(1,17)
        sage: g = SetPartitionsAk(1).list()
        sage: a = A[g[1]]
        sage: a
        P{{-1}, {1}}
        sage: a*a
        17*P{{-1}, {1}}

    Shorthands for working with basis elements are as follows::

        sage: # needs sage.symbolic
        sage: S = SymmetricGroupAlgebra(ZZ, 3)
        sage: A = PartitionAlgebra(3, x, SR)
        sage: A([[1,3],[-1],[-3]])  # pair up the omitted nodes as `{-i, i}`, if possible
        P{{-3}, {-2, 2}, {-1}, {1, 3}}
        sage: A([[1,3],[-1],[-3]]) == A[[1,3],[-1],[-3]]
        True
        sage: A([[1,2]])
        P{{-3, 3}, {-2}, {-1}, {1, 2}}
        sage: A([[1,2]]) == A[[1,2]]
        True
        sage: A([2,3,1])  # permutations in one-line notation are imported as well
        P{{-3, 2}, {-2, 1}, {-1, 3}}
        sage: A([2,3,1]) == A(S([2,3,1]))
        True
    '''
    @staticmethod
    def __classcall_private__(cls, k, q, base_ring=None, prefix: str = 'P'):
        """
        Standardize the input by getting the base ring from the parent of
        the parameter ``q`` if no ``base_ring`` is given.

        TESTS::

            sage: R.<q> = QQ[]
            sage: PA1 = PartitionAlgebra(2, q)
            sage: PA2 = PartitionAlgebra(2, q, R, 'P')
            sage: PA1 is PA2
            True
        """
    def __init__(self, k, q, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<q> = QQ[]
            sage: PA = PartitionAlgebra(2, q, R)
            sage: TestSuite(PA).run()
        """
    def orbit_basis(self):
        """
        Return the orbit basis of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: P2 = PartitionAlgebra(2, x, R)
            sage: O2 = P2.orbit_basis(); O2
            Orbit basis of Partition Algebra of rank 2 with parameter x over
             Univariate Polynomial Ring in x over Rational Field
            sage: pp = 7 * P2[{-1}, {-2, 1, 2}] - 2 * P2[{-2}, {-1, 1}, {2}]; pp
            -2*P{{-2}, {-1, 1}, {2}} + 7*P{{-2, 1, 2}, {-1}}
            sage: op = pp.to_orbit_basis(); op
            -2*O{{-2}, {-1, 1}, {2}} - 2*O{{-2}, {-1, 1, 2}}
             - 2*O{{-2, -1, 1}, {2}} + 5*O{{-2, -1, 1, 2}}
             + 7*O{{-2, 1, 2}, {-1}} - 2*O{{-2, 2}, {-1, 1}}
            sage: op == O2(op)
            True
            sage: pp * op.leading_term()
            4*P{{-2}, {-1, 1}, {2}} - 4*P{{-2, -1, 1}, {2}}
             + 14*P{{-2, -1, 1, 2}} - 14*P{{-2, 1, 2}, {-1}}
        """
    @cached_method
    def a(self, i):
        """
        Return the element `a_i` in ``self``.

        The element `a_i` is the cap and cup at `(i, i+1)`, so it contains
        the blocks `\\{i, i+1\\}`, `\\{-i, -i-1\\}`.  Other blocks are of the
        form `\\{-j, j\\}`.

        INPUT:

        - ``i`` -- integer between 1 and `k-1`

        EXAMPLES::

            sage: R.<n> = QQ[]
            sage: P3 = PartitionAlgebra(3, n)
            sage: P3.a(1)
            P{{-3, 3}, {-2, -1}, {1, 2}}
            sage: P3.a(2)
            P{{-3, -2}, {-1, 1}, {2, 3}}

            sage: P3 = PartitionAlgebra(5/2, n)
            sage: P3.a(1)
            P{{-3, 3}, {-2, -1}, {1, 2}}
            sage: P3.a(2)
            Traceback (most recent call last):
            ...
            ValueError: i must be an integer between 1 and 1
        """
    generator_a = a
    @cached_method
    def e(self, i):
        """
        Return the element `e_i` in ``self``.

        If `i = (2r+1)/2`, then `e_i` contains the blocks `\\{r+1\\}` and
        `\\{-r-1\\}`.  If `i \\in \\ZZ`, then `e_i` contains the block
        `\\{-i, -i-1, i, i+1\\}`.  Other blocks are of the form `\\{-j, j\\}`.

        INPUT:

        - ``i`` -- half integer between `1/2` and `k-1/2`

        EXAMPLES::

            sage: R.<n> = QQ[]
            sage: P3 = PartitionAlgebra(3, n)
            sage: P3.e(1)
            P{{-3, 3}, {-2, -1, 1, 2}}
            sage: P3.e(2)
            P{{-3, -2, 2, 3}, {-1, 1}}
            sage: P3.e(1/2)
            P{{-3, 3}, {-2, 2}, {-1}, {1}}
            sage: P3.e(5/2)
            P{{-3}, {-2, 2}, {-1, 1}, {3}}
            sage: P3.e(0)
            Traceback (most recent call last):
            ...
            ValueError: i must be an (half) integer between 1/2 and 5/2
            sage: P3.e(3)
            Traceback (most recent call last):
            ...
            ValueError: i must be an (half) integer between 1/2 and 5/2

            sage: P2h = PartitionAlgebra(5/2,n)
            sage: [P2h.e(k/2) for k in range(1,5)]
            [P{{-3, 3}, {-2, 2}, {-1}, {1}},
             P{{-3, 3}, {-2, -1, 1, 2}},
             P{{-3, 3}, {-2}, {-1, 1}, {2}},
             P{{-3, -2, 2, 3}, {-1, 1}}]
        """
    generator_e = e
    @cached_method
    def s(self, i):
        """
        Return the ``i``-th simple transposition `s_i` in ``self``.

        Borrowing the notation from the symmetric group, the `i`-th
        simple transposition `s_i` has blocks of the form `\\{-i, i+1\\}`,
        `\\{-i-1, i\\}`.  Other blocks are of the form `\\{-j, j\\}`.

        INPUT:

        - ``i`` -- integer between 1 and `k-1`

        EXAMPLES::

            sage: R.<n> = QQ[]
            sage: P3 = PartitionAlgebra(3, n)
            sage: P3.s(1)
            P{{-3, 3}, {-2, 1}, {-1, 2}}
            sage: P3.s(2)
            P{{-3, 2}, {-2, 3}, {-1, 1}}

            sage: R.<n> = ZZ[]
            sage: P2h = PartitionAlgebra(5/2,n)
            sage: P2h.s(1)
            P{{-3, 3}, {-2, 1}, {-1, 2}}
        """
    generator_s = s
    @cached_method
    def sigma(self, i):
        """
        Return the element `\\sigma_i` from [Eny2012]_ of ``self``.

        INPUT:

        - ``i`` -- half integer between `1/2` and `k-1/2`

        .. NOTE::

            In [Cre2020]_ and [Eny2013]_, these are the elements `\\sigma_{2i}`.

        EXAMPLES::

            sage: R.<n> = QQ[]
            sage: P3 = PartitionAlgebra(3, n)
            sage: P3.sigma(1)
            P{{-3, 3}, {-2, 2}, {-1, 1}}
            sage: P3.sigma(3/2)
            P{{-3, 3}, {-2, 1}, {-1, 2}}
            sage: P3.sigma(2)
            -P{{-3, -1, 1, 3}, {-2, 2}} + P{{-3, -1, 3}, {-2, 1, 2}}
             + P{{-3, 1, 3}, {-2, -1, 2}} - P{{-3, 3}, {-2, -1, 1, 2}}
             + P{{-3, 3}, {-2, 2}, {-1, 1}}
            sage: P3.sigma(5/2)
            -P{{-3, -1, 1, 2}, {-2, 3}} + P{{-3, -1, 2}, {-2, 1, 3}}
             + P{{-3, 1, 2}, {-2, -1, 3}} - P{{-3, 2}, {-2, -1, 1, 3}}
             + P{{-3, 2}, {-2, 3}, {-1, 1}}

        We test the relations in Lemma 2.2.3(1) in [Cre2020]_ (v1)::

            sage: k = 4
            sage: R.<x> = QQ[]
            sage: P = PartitionAlgebra(k, x)
            sage: all(P.sigma(i/2).dual() == P.sigma(i/2)
            ....:     for i in range(1,2*k))
            True
            sage: all(P.sigma(i)*P.sigma(i+1/2) == P.sigma(i+1/2)*P.sigma(i) == P.s(i)
            ....:     for i in range(1,floor(k)))
            True
            sage: all(P.sigma(i)*P.e(i) == P.e(i)*P.sigma(i) == P.e(i)
            ....:     for i in range(1,floor(k)))
            True
            sage: all(P.sigma(i+1/2)*P.e(i) == P.e(i)*P.sigma(i+1/2) == P.e(i)
            ....:     for i in range(1,floor(k)))
            True

            sage: k = 9/2
            sage: R.<x> = QQ[]
            sage: P = PartitionAlgebra(k, x)
            sage: all(P.sigma(i/2).dual() == P.sigma(i/2)
            ....:     for i in range(1,2*k-1))
            True
            sage: all(P.sigma(i)*P.sigma(i+1/2) == P.sigma(i+1/2)*P.sigma(i) == P.s(i)
            ....:     for i in range(1,k-1/2))
            True
            sage: all(P.sigma(i)*P.e(i) == P.e(i)*P.sigma(i) == P.e(i)
            ....:     for i in range(1,floor(k)))
            True
            sage: all(P.sigma(i+1/2)*P.e(i) == P.e(i)*P.sigma(i+1/2) == P.e(i)
            ....:     for i in range(1,floor(k)))
            True
        """
    @cached_method
    def jucys_murphy_element(self, i):
        """
        Return the ``i``-th Jucys-Murphy element `L_i` from [Eny2012]_.

        INPUT:

        - ``i`` -- half integer between `1/2` and `k`

        ALGORITHM:

        We use the recursive definition for `L_{2i}` given in [Cre2020]_.
        See also [Eny2012]_ and [Eny2013]_.

        .. NOTE::

            `L_{1/2}` and `L_1` differs from [HR2005]_.

        EXAMPLES::

            sage: R.<n> = QQ[]
            sage: P3 = PartitionAlgebra(3, n)
            sage: P3.jucys_murphy_element(1/2)
            0
            sage: P3.jucys_murphy_element(1)
            P{{-3, 3}, {-2, 2}, {-1}, {1}}
            sage: P3.jucys_murphy_element(2)
            P{{-3, 3}, {-2}, {-1, 1}, {2}} - P{{-3, 3}, {-2}, {-1, 1, 2}}
             + P{{-3, 3}, {-2, -1}, {1, 2}} - P{{-3, 3}, {-2, -1, 1}, {2}}
             + P{{-3, 3}, {-2, 1}, {-1, 2}}
            sage: P3.jucys_murphy_element(3/2)
            n*P{{-3, 3}, {-2, -1, 1, 2}} - P{{-3, 3}, {-2, -1, 2}, {1}}
             - P{{-3, 3}, {-2, 1, 2}, {-1}} + P{{-3, 3}, {-2, 2}, {-1, 1}}
            sage: P3.L(3/2) * P3.L(2) == P3.L(2) * P3.L(3/2)
            True

        We test the relations in Lemma 2.2.3(2) in [Cre2020]_ (v1)::

            sage: k = 4
            sage: R.<n> = QQ[]
            sage: P = PartitionAlgebra(k, n)
            sage: L = [P.L(i/2) for i in range(1,2*k+1)]
            sage: all(x.dual() == x for x in L)
            True
            sage: all(x * y == y * x for x, y in Subsets(L, 2))  # long time
            True
            sage: Lsum = sum(L)
            sage: gens = [P.s(i) for i in range(1,k)]
            sage: gens += [P.e(i/2) for i in range(1,2*k)]
            sage: all(x * Lsum == Lsum * x for x in gens)
            True

        Also the relations in Lemma 2.2.3(3) in [Cre2020]_ (v1)::

            sage: all(P.e((2*i+1)/2) * P.sigma(2*i/2) * P.e((2*i+1)/2)
            ....:     == (n - P.L((2*i-1)/2)) * P.e((2*i+1)/2) for i in range(1,k))
            True
            sage: all(P.e(i/2) * (P.L(i/2) + P.L((i+1)/2))
            ....:     == (P.L(i/2) + P.L((i+1)/2)) * P.e(i/2)
            ....:     == n * P.e(i/2) for i in range(1,2*k))
            True
            sage: all(P.sigma(2*i/2) * P.e((2*i-1)/2) * P.e(2*i/2)
            ....:     == P.L(2*i/2) * P.e(2*i/2) for i in range(1,k))
            True
            sage: all(P.e(2*i/2) * P.e((2*i-1)/2) * P.sigma(2*i/2)
            ....:     == P.e(2*i/2) * P.L(2*i/2) for i in range(1,k))
            True
            sage: all(P.sigma((2*i+1)/2) * P.e((2*i+1)/2) * P.e(2*i/2)
            ....:     == P.L(2*i/2) * P.e(2*i/2) for i in range(1,k))
            True
            sage: all(P.e(2*i/2) * P.e((2*i+1)/2) * P.sigma((2*i+1)/2)
            ....:     == P.e(2*i/2) * P.L(2*i/2) for i in range(1,k))
            True

        The same tests for a half integer partition algebra::

            sage: k = 7/2
            sage: R.<n> = QQ[]
            sage: P = PartitionAlgebra(k, n)
            sage: L = [P.L(i/2) for i in range(1,2*k+1)]
            sage: all(x.dual() == x for x in L)
            True
            sage: all(x * y == y * x for x, y in Subsets(L, 2))  # long time
            True
            sage: Lsum = sum(L)
            sage: gens = [P.s(i) for i in range(1,k-1/2)]
            sage: gens += [P.e(i/2) for i in range(1,2*k)]
            sage: all(x * Lsum == Lsum * x for x in gens)
            True
            sage: all(P.e((2*i+1)/2) * P.sigma(2*i/2) * P.e((2*i+1)/2)
            ....:     == (n - P.L((2*i-1)/2)) * P.e((2*i+1)/2) for i in range(1,floor(k)))
            True
            sage: all(P.e(i/2) * (P.L(i/2) + P.L((i+1)/2))
            ....:     == (P.L(i/2) + P.L((i+1)/2)) * P.e(i/2)
            ....:     == n * P.e(i/2) for i in range(1,2*k))
            True
            sage: all(P.sigma(2*i/2) * P.e((2*i-1)/2) * P.e(2*i/2)
            ....:     == P.L(2*i/2) * P.e(2*i/2) for i in range(1,ceil(k)))
            True
            sage: all(P.e(2*i/2) * P.e((2*i-1)/2) * P.sigma(2*i/2)
            ....:     == P.e(2*i/2) * P.L(2*i/2) for i in range(1,ceil(k)))
            True
            sage: all(P.sigma((2*i+1)/2) * P.e((2*i+1)/2) * P.e(2*i/2)
            ....:     == P.L(2*i/2) * P.e(2*i/2) for i in range(1,floor(k)))
            True
            sage: all(P.e(2*i/2) * P.e((2*i+1)/2) * P.sigma((2*i+1)/2)
            ....:     == P.e(2*i/2) * P.L(2*i/2) for i in range(1,floor(k)))
            True
        """
    L = jucys_murphy_element
    def potts_representation(self, y=None):
        """
        Return the :class:`PottsRepresentation` with magnetic field
        direction ``y`` of ``self``.

        .. NOTE::

            The deformation parameter `d` of ``self`` must be a
            positive integer.

        INPUT:

        - ``y`` -- (optional) an integer between 1 and `d`; ignored
          if the order of ``self`` is an integer, otherwise the
          default is `1`

        EXAMPLES::

            sage: PA = algebras.Partition(5/2, QQ(4))
            sage: PR = PA.potts_representation()

            sage: PA = algebras.Partition(5/2, 3/2)
            sage: PA.potts_representation()
            Traceback (most recent call last):
            ...
            ValueError: the partition algebra deformation parameter must
             be a positive integer
        """
    class Element(DiagramBasis.Element):
        def to_orbit_basis(self):
            """
            Return ``self`` in the orbit basis of the associated
            partition algebra.

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: P = PartitionAlgebra(2, x, R)
                sage: pp = P.an_element();
                sage: pp.to_orbit_basis()
                3*O{{-2}, {-1, 1, 2}} + 7*O{{-2, -1, 1, 2}} + 2*O{{-2, 1, 2}, {-1}}
                sage: pp = (3*P([[-2], [-1, 1, 2]]) + 2*P([[-2, -1, 1, 2]])
                ....:       + 2*P([[-2, 1, 2], [-1]])); pp
                3*P{{-2}, {-1, 1, 2}} + 2*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}
                sage: pp.to_orbit_basis()
                3*O{{-2}, {-1, 1, 2}} + 7*O{{-2, -1, 1, 2}} + 2*O{{-2, 1, 2}, {-1}}
            """
        def dual(self):
            """
            Return the dual of ``self``.

            The dual of an element in the partition algebra is formed
            by taking the dual of each diagram in the support.

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: P = PartitionAlgebra(2, x, R)
                sage: elt = P.an_element(); elt
                3*P{{-2}, {-1, 1, 2}} + 2*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}
                sage: elt.dual()
                3*P{{-2, -1, 1}, {2}} + 2*P{{-2, -1, 1, 2}} + 2*P{{-2, -1, 2}, {1}}
            """

class OrbitBasis(DiagramAlgebra):
    """
    The orbit basis of the partition algebra.

    Let `D_\\pi` represent the diagram basis element indexed by the
    partition `\\pi`, then (see equations (2.14), (2.17) and (2.18) of [BH2017]_)

    .. MATH::

        D_\\pi = \\sum_{\\tau \\geq \\pi} O_\\tau,

    where the sum is over all partitions `\\tau` which are coarser than `\\pi`
    and `O_\\tau` is the orbit basis element indexed by the partition `\\tau`.

    If `\\mu_{2k}(\\pi,\\tau)` represents the Moebius function of the partition
    lattice, then

    .. MATH::

        O_\\pi = \\sum_{\\tau \\geq \\pi} \\mu_{2k}(\\pi, \\tau) D_\\tau.

    If `\\tau` is a partition of `\\ell` blocks and the `i`-th block of
    `\\tau` is a union of `b_i` blocks of `\\pi`, then

    .. MATH::

        \\mu_{2k}(\\pi, \\tau) = \\prod_{i=1}^\\ell (-1)^{b_i-1} (b_i-1)! .

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: P2 = PartitionAlgebra(2, x, R)
        sage: O2 = P2.orbit_basis(); O2
        Orbit basis of Partition Algebra of rank 2 with parameter x over
         Univariate Polynomial Ring in x over Rational Field
        sage: oa = O2([[1],[-1],[2,-2]]); ob = O2([[-1,-2,2],[1]]); oa, ob
        (O{{-2, 2}, {-1}, {1}}, O{{-2, -1, 2}, {1}})
        sage: oa * ob
        (x-2)*O{{-2, -1, 2}, {1}}

    We can convert between the two bases::

        sage: pa = P2(oa); pa
        2*P{{-2, -1, 1, 2}} - P{{-2, -1, 2}, {1}} - P{{-2, 1, 2}, {-1}}
         + P{{-2, 2}, {-1}, {1}} - P{{-2, 2}, {-1, 1}}
        sage: pa * ob
        (-x+2)*P{{-2, -1, 1, 2}} + (x-2)*P{{-2, -1, 2}, {1}}
        sage: _ == pa * P2(ob)
        True
        sage: O2(pa * ob)
        (x-2)*O{{-2, -1, 2}, {1}}

    Note that the unit in the orbit basis is not a single diagram,
    in contrast to the natural diagram basis::

        sage: P2.one()
        P{{-2, 2}, {-1, 1}}
        sage: O2.one()
        O{{-2, -1, 1, 2}} + O{{-2, 2}, {-1, 1}}
        sage: O2.one() == P2.one()
        True

    TESTS:

    Check that going between the two bases is the identity::

        sage: R.<x> = QQ[]
        sage: P2 = PartitionAlgebra(2, x, R)
        sage: O2 = P2.orbit_basis(); O2
        Orbit basis of Partition Algebra of rank 2 with parameter x over
         Univariate Polynomial Ring in x over Rational Field
        sage: PD = P2.basis().keys()
        sage: all(O2(P2(O2(m))) == O2(m) for m in PD)
        True
        sage: all(P2(O2(P2(m))) == P2(m) for m in PD)
        True
    """
    @staticmethod
    def __classcall_private__(cls, *args):
        """
        Normalize input to ensure a unique representation.

        INPUT:

        Either:

        - ``A`` -- an abstract diagram algebra

        or the arguments to construct a diagram algebra:

        - ``k`` -- the rank
        - ``q`` -- the parameter
        - ``R`` -- the base ring

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: P2 = PartitionAlgebra(2, x, R)
            sage: from sage.combinat.diagram_algebras import OrbitBasis
            sage: O2a = P2.orbit_basis()
            sage: O2b = OrbitBasis(P2)
            sage: O2c = OrbitBasis(2, x, R)
            sage: O2a is O2b and O2a is O2c
            True
            sage: O2d = OrbitBasis(2, x, QQ[x])
            sage: O2a is O2d
            True
        """
    def __init__(self, alg) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: O2 = PartitionAlgebra(2, -1, QQ).orbit_basis()
            sage: TestSuite(O2).run()
        """
    @cached_method
    def one(self):
        """
        Return the element `1` of the partition algebra in the orbit basis.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: P2 = PartitionAlgebra(2, x, R)
            sage: O2 = P2.orbit_basis()
            sage: O2.one()
            O{{-2, -1, 1, 2}} + O{{-2, 2}, {-1, 1}}
        """
    def diagram_basis(self):
        """
        Return the associated partition algebra of ``self``
        in the diagram basis.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: O2 = PartitionAlgebra(2, x, R).orbit_basis()
            sage: P2 = O2.diagram_basis(); P2
            Partition Algebra of rank 2 with parameter x over Univariate
            Polynomial Ring in x over Rational Field
            sage: o2 = O2.an_element(); o2
            3*O{{-2}, {-1, 1, 2}} + 2*O{{-2, -1, 1, 2}} + 2*O{{-2, 1, 2}, {-1}}
            sage: P2(o2)
            3*P{{-2}, {-1, 1, 2}} - 3*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}

        TESTS::

            sage: R.<x> = QQ[]
            sage: P2 = PartitionAlgebra(2, x, R)
            sage: O2 = P2.orbit_basis()
            sage: op = O2([]); op
            O{{-2, 2}, {-1, 1}}
            sage: PA = O2.diagram_basis()
            sage: P2 == PA
            True
            sage: PA([]) == P2.one()
            True
            sage: PA(op)
            -P{{-2, -1, 1, 2}} + P{{-2, 2}, {-1, 1}}
            sage: op == PA(op).to_orbit_basis()
            True
        """
    def product_on_basis(self, d1, d2):
        """
        Return the product `O_{d_1} O_{d_2}` of two elements
        in the orbit basis ``self``.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: OP = PartitionAlgebra(2, x, R).orbit_basis()
            sage: SP = OP.basis().keys(); sp = SP([[-2, -1, 1, 2]])
            sage: OP.product_on_basis(sp, sp)
            O{{-2, -1, 1, 2}}
            sage: o1 = OP.one(); o2 = OP([]); o3 = OP.an_element()
            sage: o2 == o1
            False
            sage: o1 * o1 == o1
            True
            sage: o3 * o1 == o1 * o3 and o3 * o1 == o3
            True
            sage: o4 = (3*OP([[-2, -1, 1], [2]]) + 2*OP([[-2, -1, 1, 2]])
            ....:       + 2*OP([[-2, -1, 2], [1]]))
            sage: o4 * o4
            6*O{{-2, -1, 1}, {2}} + 4*O{{-2, -1, 1, 2}} + 4*O{{-2, -1, 2}, {1}}

        We compute Examples 4.5 in [BH2017]_::

            sage: R.<x> = QQ[]
            sage: P = PartitionAlgebra(3,x); O = P.orbit_basis()
            sage: O[[1,2,3],[-1,-2,-3]] * O[[1,2,3],[-1,-2,-3]]
            (x-2)*O{{-3, -2, -1}, {1, 2, 3}} + (x-1)*O{{-3, -2, -1, 1, 2, 3}}

            sage: P = PartitionAlgebra(4,x); O = P.orbit_basis()
            sage: O[[1],[-1],[2,3],[4,-2],[-3,-4]] * O[[1],[2,-2],[3,4],[-1,-3],[-4]]
            (x^2-11*x+30)*O{{-4}, {-3, -1}, {-2, 4}, {1}, {2, 3}}
             + (x^2-9*x+20)*O{{-4}, {-3, -1, 1}, {-2, 4}, {2, 3}}
             + (x^2-9*x+20)*O{{-4}, {-3, -1, 2, 3}, {-2, 4}, {1}}
             + (x^2-9*x+20)*O{{-4, 1}, {-3, -1}, {-2, 4}, {2, 3}}
             + (x^2-7*x+12)*O{{-4, 1}, {-3, -1, 2, 3}, {-2, 4}}
             + (x^2-9*x+20)*O{{-4, 2, 3}, {-3, -1}, {-2, 4}, {1}}
             + (x^2-7*x+12)*O{{-4, 2, 3}, {-3, -1, 1}, {-2, 4}}

            sage: O[[1,-1],[2,-2],[3],[4,-3],[-4]] * O[[1,-2],[2],[3,-1],[4],[-3],[-4]]
            (x-6)*O{{-4}, {-3}, {-2, 1}, {-1, 4}, {2}, {3}}
             + (x-5)*O{{-4}, {-3, 3}, {-2, 1}, {-1, 4}, {2}}
             + (x-5)*O{{-4, 3}, {-3}, {-2, 1}, {-1, 4}, {2}}

            sage: P = PartitionAlgebra(6,x); O = P.orbit_basis()
            sage: (O[[1,-2,-3],[2,4],[3,5,-6],[6],[-1],[-4,-5]]
            ....:  * O[[1,-2],[2,3],[4],[5],[6,-4,-5,-6],[-1,-3]])
            0

            sage: (O[[1,-2],[2,-3],[3,5],[4,-5],[6,-4],[-1],[-6]]
            ....:  * O[[1,-2],[2,-1],[3,-4],[4,-6],[5,-3],[6,-5]])
            O{{-6, 6}, {-5}, {-4, 2}, {-3, 4}, {-2}, {-1, 1}, {3, 5}}

        TESTS:

        Check that multiplication agrees with the multiplication in the
        partition algebra::

            sage: R.<x> = QQ[]
            sage: OP = PartitionAlgebra(2, x).orbit_basis()
            sage: P = OP.diagram_basis()
            sage: o1 = OP.one(); o2 = OP([]); o3 = OP.an_element()
            sage: p1 = P(o1); p2 = P(o2); p3 = P(o3)
            sage: (p2 * p3).to_orbit_basis() == o2 * o3
            True
            sage: (3*p3 * (p1 - 2*p2)).to_orbit_basis() == 3*o3 * (o1 - 2*o2)
            True

            sage: R.<x> = QQ[]
            sage: P = PartitionAlgebra(2,x); O = P.orbit_basis()
            sage: all(b * bp == OP(P(b) * P(bp)) for b in OP.basis() # long time
            ....:     for bp in OP.basis())
            True

        REFERENCES:

        - [BH2017]_
        """
    class Element(PartitionAlgebra.Element):
        def to_diagram_basis(self):
            """
            Expand ``self`` in the natural diagram basis of the
            partition algebra.

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: P = PartitionAlgebra(2, x, R)
                sage: O = P.orbit_basis()
                sage: elt = O.an_element(); elt
                3*O{{-2}, {-1, 1, 2}} + 2*O{{-2, -1, 1, 2}} + 2*O{{-2, 1, 2}, {-1}}
                sage: elt.to_diagram_basis()
                3*P{{-2}, {-1, 1, 2}} - 3*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}
                sage: pp = P.an_element(); pp
                3*P{{-2}, {-1, 1, 2}} + 2*P{{-2, -1, 1, 2}} + 2*P{{-2, 1, 2}, {-1}}
                sage: op = pp.to_orbit_basis(); op
                3*O{{-2}, {-1, 1, 2}} + 7*O{{-2, -1, 1, 2}} + 2*O{{-2, 1, 2}, {-1}}
                sage: pp == op.to_diagram_basis()
                True
            """

class SubPartitionAlgebra(DiagramBasis):
    """
    A subalgebra of the partition algebra in the diagram basis indexed
    by a subset of the diagrams.
    """
    def __init__(self, k, q, base_ring, prefix, diagrams, category=None) -> None:
        """
        Initialize ``self`` by adding a coercion to the ambient space.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: BA = BrauerAlgebra(2, x, R)
            sage: BA.ambient().has_coerce_map_from(BA)
            True
        """
    def ambient(self):
        """
        Return the partition algebra ``self`` is a sub-algebra of.

        EXAMPLES::

            sage: x = var('x')                                                          # needs sage.symbolic
            sage: BA = BrauerAlgebra(2, x)                                              # needs sage.symbolic
            sage: BA.ambient()                                                          # needs sage.symbolic
            Partition Algebra of rank 2 with parameter x over Symbolic Ring
        """
    @lazy_attribute
    def lift(self):
        """
        Return the lift map from diagram subalgebra to the ambient space.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: BA = BrauerAlgebra(2, x, R)
            sage: E = BA([[1,2],[-1,-2]])
            sage: lifted = BA.lift(E); lifted
            B{{-2, -1}, {1, 2}}
            sage: lifted.parent() is BA.ambient()
            True
        """
    def retract(self, x):
        """
        Retract an appropriate partition algebra element to the
        corresponding element in the partition subalgebra.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: BA = BrauerAlgebra(2, x, R)
            sage: PA = BA.ambient()
            sage: E = PA([[1,2], [-1,-2]])
            sage: BA.retract(E) in BA
            True
        """
    class Element(DiagramBasis.Element):
        def to_orbit_basis(self):
            """
            Return ``self`` in the orbit basis of the associated
            ambient partition algebra.

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: B = BrauerAlgebra(2, x, R)
                sage: bb = B([[-2, -1], [1, 2]]); bb
                B{{-2, -1}, {1, 2}}
                sage: bb.to_orbit_basis()
                O{{-2, -1}, {1, 2}} + O{{-2, -1, 1, 2}}
            """

class BrauerAlgebra(SubPartitionAlgebra, UnitDiagramMixin):
    """
    A Brauer algebra.

    The Brauer algebra of rank `k` is an algebra with basis indexed by the
    collection of set partitions of `\\{1, \\ldots, k, -1, \\ldots, -k\\}`
    with block size 2.

    This algebra is a subalgebra of the partition algebra.
    For more information, see :class:`PartitionAlgebra`.

    INPUT:

    - ``k`` -- rank of the algebra

    - ``q`` -- the deformation parameter `q`

    - ``base_ring`` -- (default: ``None``) a ring containing ``q``; if ``None``
      then just takes the parent of ``q``

    - ``prefix`` -- (default: ``'B'``) a label for the basis elements

    EXAMPLES:

    We now define the Brauer algebra of rank `2` with parameter ``x``
    over `\\ZZ`::

        sage: R.<x> = ZZ[]
        sage: B = BrauerAlgebra(2, x, R)
        sage: B
        Brauer Algebra of rank 2 with parameter x
         over Univariate Polynomial Ring in x over Integer Ring
        sage: B.basis()
        Lazy family (Term map from Brauer diagrams of order 2 to Brauer Algebra
         of rank 2 with parameter x over Univariate Polynomial Ring in x
         over Integer Ring(i))_{i in Brauer diagrams of order 2}
        sage: B.basis().keys()
        Brauer diagrams of order 2
        sage: B.basis().keys()([[-2, 1], [2, -1]])
        {{-2, 1}, {-1, 2}}
        sage: b = B.basis().list(); b
        [B{{-2, -1}, {1, 2}}, B{{-2, 1}, {-1, 2}}, B{{-2, 2}, {-1, 1}}]
        sage: b[0]
        B{{-2, -1}, {1, 2}}
        sage: b[0]^2
        x*B{{-2, -1}, {1, 2}}
        sage: b[0]^5
        x^4*B{{-2, -1}, {1, 2}}

    Note, also that since the symmetric group algebra is contained in
    the Brauer algebra, there is also a conversion between the two. ::

        sage: R.<x> = ZZ[]
        sage: B = BrauerAlgebra(2, x, R)
        sage: S = SymmetricGroupAlgebra(R, 2)
        sage: S([2,1])*B([[1,-1],[2,-2]])
        B{{-2, 1}, {-1, 2}}
    """
    @staticmethod
    def __classcall_private__(cls, k, q, base_ring=None, prefix: str = 'B'):
        """
        Standardize the input by getting the base ring from the parent of
        the parameter ``q`` if no ``base_ring`` is given.

        TESTS::

            sage: R.<q> = QQ[]
            sage: BA1 = BrauerAlgebra(2, q)
            sage: BA2 = BrauerAlgebra(2, q, R, 'B')
            sage: BA1 is BA2
            True
        """
    def __init__(self, k, q, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<q> = QQ[]
            sage: BA = BrauerAlgebra(2, q, R)
            sage: TestSuite(BA).run()
        """
    options = BrauerDiagram.options
    def jucys_murphy(self, j):
        """
        Return the ``j``-th generalized Jucys-Murphy element of ``self``.

        The `j`-th Jucys-Murphy element of a Brauer algebra is simply
        the `j`-th Jucys-Murphy element of the symmetric group algebra
        with an extra `(z-1)/2` term, where ``z`` is the parameter
        of the Brauer algebra.

        REFERENCES:

        .. [Naz96] Maxim Nazarov, Young's Orthogonal Form for Brauer's
           Centralizer Algebra. Journal of Algebra 182 (1996), 664--693.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: z = var('z')
            sage: B = BrauerAlgebra(3,z)
            sage: B.jucys_murphy(1)
            (1/2*z-1/2)*B{{-3, 3}, {-2, 2}, {-1, 1}}
            sage: B.jucys_murphy(3)
            -B{{-3, -2}, {-1, 1}, {2, 3}} - B{{-3, -1}, {-2, 2}, {1, 3}}
             + B{{-3, 1}, {-2, 2}, {-1, 3}} + B{{-3, 2}, {-2, 3}, {-1, 1}}
             + (1/2*z-1/2)*B{{-3, 3}, {-2, 2}, {-1, 1}}
        """

class HalfTemperleyLiebDiagrams(UniqueRepresentation, Parent):
    """
    Half diagrams for the Temperley-Lieb algebra cell modules.
    """
    def __init__(self, order, defects) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: htld = da.HalfTemperleyLiebDiagrams(7, 3)
            sage: TestSuite(htld).run()
        """
    def __iter__(self):
        """
        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: list(da.HalfTemperleyLiebDiagrams(5, 3))
            [{{1, 2}}, {{2, 3}}, {{3, 4}}, {{4, 5}}]
        """
    def __contains__(self, obj) -> bool:
        """
        Check containment.

        TESTS::

            sage: import sage.combinat.diagram_algebras as da
            sage: htld = da.HalfTemperleyLiebDiagrams(7, 3)
            sage: htld.an_element() in htld
            True
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: import sage.combinat.diagram_algebras as da
            sage: htld = da.HalfTemperleyLiebDiagrams(7, 3)
            sage: htld.cardinality()
            14
        """
    class Element(AbstractPartitionDiagram):
        def defects(self):
            """
            Return the defects of ``self``.

            EXAMPLES::

                sage: import sage.combinat.diagram_algebras as da
                sage: htld = da.HalfTemperleyLiebDiagrams(7, 3)
                sage: d = htld([[1, 2], [4, 5]])
                sage: d.defects()
                frozenset({3, 6, 7})
            """
        def check(self) -> None:
            """
            Check the validity of the input of ``self``.

            EXAMPLES::

                sage: import sage.combinat.diagram_algebras as da
                sage: htld = da.HalfTemperleyLiebDiagrams(7, 3)
                sage: htld([[1,2], [3,4]])  # indirect doctest
                {{1, 2}, {3, 4}}
                sage: htld([[1,2], [-1, -2]])  # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: {{-2, -1}, {1, 2}} does not represent a half TL diagram of order 7
                sage: htld([[1,2,3], [4,5]])  # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: all blocks of {{1, 2, 3}, {4, 5}} must be of size 2
                sage: htld([[1,2], [3,4], [5,6]])  # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: {{1, 2}, {3, 4}, {5, 6}} does not have 3 defects
                sage: htld([[1,3], [2,4]])  # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: {{1, 3}, {2, 4}} is not planar
            """

class TemperleyLiebAlgebra(SubPartitionAlgebra, UnitDiagramMixin):
    '''
    A Temperley--Lieb algebra.

    The Temperley--Lieb algebra of rank `k` is an algebra with basis
    indexed by the collection of planar set partitions of
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}` with block size 2.

    This algebra is thus a subalgebra of the partition algebra.
    For more information, see :class:`PartitionAlgebra`.

    INPUT:

    - ``k`` -- rank of the algebra

    - ``q`` -- the deformation parameter `q`

    - ``base_ring`` -- (default: ``None``) a ring containing ``q``; if ``None``
      then just takes the parent of ``q``

    - ``prefix`` -- (default: ``\'T\'``) a label for the basis elements

    EXAMPLES:

    We define the Temperley--Lieb algebra of rank `2` with parameter
    `x` over `\\ZZ`::

        sage: R.<x> = ZZ[]
        sage: T = TemperleyLiebAlgebra(2, x, R); T
        Temperley-Lieb Algebra of rank 2 with parameter x
         over Univariate Polynomial Ring in x over Integer Ring
        sage: T.basis()
        Lazy family (Term map from Temperley Lieb diagrams of order 2
         to Temperley-Lieb Algebra of rank 2 with parameter x over
         Univariate Polynomial Ring in x over Integer
         Ring(i))_{i in Temperley Lieb diagrams of order 2}
        sage: T.basis().keys()
        Temperley Lieb diagrams of order 2
        sage: T.basis().keys()([[-1, 1], [2, -2]])
        {{-2, 2}, {-1, 1}}
        sage: b = T.basis().list(); b
        [T{{-2, -1}, {1, 2}}, T{{-2, 2}, {-1, 1}}]
        sage: b[0]
        T{{-2, -1}, {1, 2}}
        sage: b[0]^2 == x*b[0]
        True
        sage: b[0]^5 == x^4*b[0]
        True

    The Temperley-Lieb algebra is a cellular algebra, and we verify that
    the dimensions of the simple modules at `q = 0` is given by
    :oeis:`A050166`::

        sage: for k in range(1,5):
        ....:     TL = TemperleyLiebAlgebra(2*k, 0, QQ)
        ....:     print("".join("{:3}".format(TL.cell_module(la).simple_module().dimension())
        ....:                   for la in reversed(TL.cell_poset()) if la != 0))
          1
          1  2
          1  4  5
          1  6 14 14
        sage: for k in range(1,4):
        ....:     TL = TemperleyLiebAlgebra(2*k+1, 0, QQ)
        ....:     print("".join("{:3}".format(TL.cell_module(la).simple_module().dimension())
        ....:                   for la in reversed(TL.cell_poset()) if la != 0))
          1  2
          1  4  5
          1  6 14 14

    Additional examples when the Temperley-Lieb algebra is not semisimple::

        sage: TL = TemperleyLiebAlgebra(8, -1, QQ)
        sage: for la in TL.cell_poset():
        ....:     CM = TL.cell_module(la)
        ....:     if not CM.nonzero_bilinear_form():
        ....:         continue
        ....:     print(la, CM.dimension(), CM.simple_module().dimension())
        ....:
        0 14 1
        2 28 28
        4 20 13
        6 7 7
        8 1 1
        sage: for k in range(1,5):
        ....:     TL = TemperleyLiebAlgebra(2*k, -1, QQ)
        ....:     print("".join("{:3}".format(TL.cell_module(la).simple_module().dimension())
        ....:                   for la in reversed(TL.cell_poset())
        ....:                    if TL.cell_module(la).nonzero_bilinear_form()))
          1  1
          1  3  1
          1  4  9  1
          1  7 13 28  1
        sage: C5.<z5> = CyclotomicField(5)
        sage: for k in range(1,5):
        ....:     TL = TemperleyLiebAlgebra(2*k, z5+~z5, C5)
        ....:     print("".join("{:3}".format(TL.cell_module(la).simple_module().dimension())
        ....:                   for la in reversed(TL.cell_poset())
        ....:                    if TL.cell_module(la).nonzero_bilinear_form()))
          1  1
          1  3  2
          1  5  8  5
          1  7 20 21 13
    '''
    @staticmethod
    def __classcall_private__(cls, k, q, base_ring=None, prefix: str = 'T'):
        """
        Standardize the input by getting the base ring from the parent of
        the parameter ``q`` if no ``base_ring`` is given.

        TESTS::

            sage: R.<q> = QQ[]
            sage: T1 = TemperleyLiebAlgebra(2, q)
            sage: T2 = TemperleyLiebAlgebra(2, q, R, 'T')
            sage: T1 is T2
            True
        """
    def __init__(self, k, q, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<q> = QQ[]
            sage: TL = TemperleyLiebAlgebra(2, q, R)
            sage: TestSuite(TL).run()

            sage: TL = TemperleyLiebAlgebra(3, 0, QQ)
            sage: TestSuite(TL).run()
        """
    @cached_method
    def cell_poset(self):
        """
        Return the cell poset of ``self``.

        EXAMPLES::

            sage: R.<q> = QQ[]
            sage: TL = TemperleyLiebAlgebra(7, q, R)
            sage: TL.cell_poset().cover_relations()
            [[1, 3], [3, 5], [5, 7]]

            sage: TL = TemperleyLiebAlgebra(8, q, R)
            sage: TL.cell_poset().cover_relations()
            [[0, 2], [2, 4], [4, 6], [6, 8]]
        """
    def cell_module_indices(self, la):
        """
        Return the indices of the cell module of ``self``
        indexed by ``la`` .

        This is the finite set `M(\\lambda)`.

        EXAMPLES::

            sage: R.<q> = QQ[]
            sage: TL = TemperleyLiebAlgebra(8, q, R)
            sage: TL.cell_module_indices(4)
            Half Temperley-Lieb diagrams of order 8 with 4 defects
        """
    def cellular_involution(self, x):
        """
        Return the cellular involution of ``x`` in ``self``.

        EXAMPLES::

            sage: TL = TemperleyLiebAlgebra(4, QQ.zero(), QQ)
            sage: ascii_art(TL.an_element())
                            o o o o       o o o o
               o o o o      | `-` |       | `-` |
            2* `-` `-` + 2* `-----`  + 3* `---. |
               .-. .-.      .-. .-.       .-. | |
               o o o o      o o o o       o o o o
            sage: ascii_art(TL.cellular_involution(TL.an_element()))
                            o o o o       o o o o
               o o o o      `-` `-`       `-` | |
            2* `-` `-` + 2* .-----.  + 3* .---` |
               .-. .-.      | .-. |       | .-. |
               o o o o      o o o o       o o o o
        """

class PlanarAlgebra(SubPartitionAlgebra, UnitDiagramMixin):
    """
    A planar algebra.

    The planar algebra of rank `k` is an algebra with basis indexed by the
    collection of all planar set partitions of
    `\\{1, \\ldots, k, -1, \\ldots, -k\\}`.

    This algebra is thus a subalgebra of the partition algebra. For more
    information, see :class:`PartitionAlgebra`.

    INPUT:

    - ``k`` -- rank of the algebra

    - ``q`` -- the deformation parameter `q`

    - ``base_ring`` -- (default: ``None``) a ring containing ``q``; if ``None``
      then just takes the parent of ``q``

    - ``prefix`` -- (default: ``'Pl'``) a label for the basis elements

    EXAMPLES:

    We define the planar algebra of rank `2` with parameter
    `x` over `\\ZZ`::

        sage: R.<x> = ZZ[]
        sage: Pl = PlanarAlgebra(2, x, R); Pl
        Planar Algebra of rank 2 with parameter x over Univariate Polynomial Ring in x over Integer Ring
        sage: Pl.basis().keys()
        Planar diagrams of order 2
        sage: Pl.basis().keys()([[-1, 1], [2, -2]])
        {{-2, 2}, {-1, 1}}
        sage: Pl.basis().list()
        [Pl{{-2}, {-1}, {1, 2}},
         Pl{{-2}, {-1}, {1}, {2}},
         Pl{{-2, 1}, {-1}, {2}},
         Pl{{-2, 2}, {-1}, {1}},
         Pl{{-2, 1, 2}, {-1}},
         Pl{{-2, 2}, {-1, 1}},
         Pl{{-2}, {-1, 1}, {2}},
         Pl{{-2}, {-1, 2}, {1}},
         Pl{{-2}, {-1, 1, 2}},
         Pl{{-2, -1}, {1, 2}},
         Pl{{-2, -1}, {1}, {2}},
         Pl{{-2, -1, 1}, {2}},
         Pl{{-2, -1, 2}, {1}},
         Pl{{-2, -1, 1, 2}}]
        sage: E = Pl([[1,2],[-1,-2]])
        sage: E^2 == x*E
        True
        sage: E^5 == x^4*E
        True
    """
    @staticmethod
    def __classcall_private__(cls, k, q, base_ring=None, prefix: str = 'Pl'):
        """
        Standardize the input by getting the base ring from the parent of
        the parameter ``q`` if no ``base_ring`` is given.

        TESTS::

            sage: R.<q> = QQ[]
            sage: Pl1 = PlanarAlgebra(2, q)
            sage: Pl2 = PlanarAlgebra(2, q, R, 'Pl')
            sage: Pl1 is Pl2
            True
        """
    def __init__(self, k, q, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<q> = QQ[]
            sage: PlA = PlanarAlgebra(2, q, R)
            sage: TestSuite(PlA).run()
        """

class PropagatingIdeal(SubPartitionAlgebra):
    """
    A propagating ideal.

    The propagating ideal of rank `k` is a non-unital algebra with basis
    indexed by the collection of ideal set partitions of `\\{1, \\ldots, k, -1,
    \\ldots, -k\\}`. We say a set partition is *ideal* if its propagating
    number is less than `k`.

    This algebra is a non-unital subalgebra and an ideal of the partition
    algebra.
    For more information, see :class:`PartitionAlgebra`.

    EXAMPLES:

    We now define the propagating ideal of rank `2` with parameter
    `x` over `\\ZZ`::

        sage: R.<x> = QQ[]
        sage: I = PropagatingIdeal(2, x, R); I
        Propagating Ideal of rank 2 with parameter x
         over Univariate Polynomial Ring in x over Rational Field
        sage: I.basis().keys()
        Ideal diagrams of order 2
        sage: I.basis().list()
        [I{{-2, -1, 1, 2}},
         I{{-2, 1, 2}, {-1}},
         I{{-2}, {-1, 1, 2}},
         I{{-2, -1}, {1, 2}},
         I{{-2}, {-1}, {1, 2}},
         I{{-2, -1, 1}, {2}},
         I{{-2, 1}, {-1}, {2}},
         I{{-2, -1, 2}, {1}},
         I{{-2, 2}, {-1}, {1}},
         I{{-2}, {-1, 1}, {2}},
         I{{-2}, {-1, 2}, {1}},
         I{{-2, -1}, {1}, {2}},
         I{{-2}, {-1}, {1}, {2}}]
        sage: E = I([[1,2],[-1,-2]])
        sage: E^2 == x*E
        True
        sage: E^5 == x^4*E
        True
    """
    @staticmethod
    def __classcall_private__(cls, k, q, base_ring=None, prefix: str = 'I'):
        """
        Standardize the input by getting the base ring from the parent of
        the parameter ``q`` if no ``base_ring`` is given.

        TESTS::

            sage: R.<q> = QQ[]
            sage: IA1 = PropagatingIdeal(2, q)
            sage: IA2 = PropagatingIdeal(2, q, R, 'I')
            sage: IA1 is IA2
            True
        """
    def __init__(self, k, q, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R.<q> = QQ[]
            sage: I = PropagatingIdeal(2, q, R)
            sage: TestSuite(I).run()
        """
    class Element(SubPartitionAlgebra.Element):
        """
        An element of a propagating ideal.

        We need to take care of exponents since we are not unital.
        """
        def __pow__(self, n):
            """
            Return ``self`` to the `n`-th power.

            INPUT:

            - ``n`` -- positive integer

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: I = PropagatingIdeal(2, x, R)
                sage: E = I([[1,2],[-1,-2]])
                sage: E^2
                x*I{{-2, -1}, {1, 2}}
                sage: E^0
                Traceback (most recent call last):
                ...
                ValueError: can only take positive integer powers
            """

def TL_diagram_ascii_art(diagram, use_unicode: bool = False, blobs=[]):
    """
    Return ascii art for a Temperley-Lieb diagram ``diagram``.

    INPUT:

    - ``diagram`` -- list of pairs of matchings of the set
      `\\{-1, \\ldots, -n, 1, \\ldots, n\\}`
    - ``use_unicode`` -- boolean (default: ``False``); whether or not
      to use unicode art instead of ascii art
    - ``blobs`` -- (optional) a list of matchings with blobs on them

    EXAMPLES::

        sage: from sage.combinat.diagram_algebras import TL_diagram_ascii_art
        sage: TL = [(-15,-12), (-14,-13), (-11,15), (-10,14), (-9,-6),
        ....:       (-8,-7), (-5,-4), (-3,1), (-2,-1), (2,3), (4,5),
        ....:       (6,11), (7, 8), (9,10), (12,13)]
        sage: TL_diagram_ascii_art(TL, use_unicode=False)
         o o o o o o o o o o o o o o o
         | `-` `-` | `-` `-` | `-` | |
         |         `---------`     | |
         |                 .-------` |
         `---.             | .-------`
             |     .-----. | | .-----.
         .-. | .-. | .-. | | | | .-. |
         o o o o o o o o o o o o o o o
        sage: TL_diagram_ascii_art(TL, use_unicode=True)
         ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬
         │ ╰─╯ ╰─╯ │ ╰─╯ ╰─╯ │ ╰─╯ │ │
         │         ╰─────────╯     │ │
         │                 ╭───────╯ │
         ╰───╮             │ ╭───────╯
             │     ╭─────╮ │ │ ╭─────╮
         ╭─╮ │ ╭─╮ │ ╭─╮ │ │ │ │ ╭─╮ │
         ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬

        sage: TL = [(-20,-9), (-19,-10), (-18,-11), (-17,-16), (-15,-12), (2,3),
        ....:       (-14,-13), (-8,16), (-7,7), (-6,6), (-5,1), (-4,-3), (-2,-1),
        ....:       (4,5), (8,15), (9,10), (11,14), (12,13), (17,20), (18,19)]
        sage: TL_diagram_ascii_art(TL, use_unicode=False, blobs=[(-2,-1), (-5,1)])
         o o o o o o o o o o o o o o o o o o o o
         | `-` `-` | | | `-` | `-` | | | | `-` |
         |         | | |     `-----` | | `-----`
         |         | | `-------------` |
         `---0---. | | .---------------`
                 | | | | .---------------------.
                 | | | | | .-----------------. |
                 | | | | | | .-------------. | |
                 | | | | | | | .-----.     | | |
         .0. .-. | | | | | | | | .-. | .-. | | |
         o o o o o o o o o o o o o o o o o o o o
        sage: TL_diagram_ascii_art(TL, use_unicode=True, blobs=[(-2,-1), (-5,1)])
         ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬
         │ ╰─╯ ╰─╯ │ │ │ ╰─╯ │ ╰─╯ │ │ │ │ ╰─╯ │
         │         │ │ │     ╰─────╯ │ │ ╰─────╯
         │         │ │ ╰─────────────╯ │
         ╰───●───╮ │ │ ╭───────────────╯
                 │ │ │ │ ╭─────────────────────╮
                 │ │ │ │ │ ╭─────────────────╮ │
                 │ │ │ │ │ │ ╭─────────────╮ │ │
                 │ │ │ │ │ │ │ ╭─────╮     │ │ │
         ╭●╮ ╭─╮ │ │ │ │ │ │ │ │ ╭─╮ │ ╭─╮ │ │ │
         ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬ ⚬
    """
def diagram_latex(diagram, fill: bool = False, edge_options=None, edge_additions=None):
    """
    Return latex code for the diagram ``diagram`` using tikz.

    EXAMPLES::

        sage: from sage.combinat.diagram_algebras import PartitionDiagrams, diagram_latex
        sage: P = PartitionDiagrams(2)
        sage: D = P([[1,2],[-2,-1]])
        sage: print(diagram_latex(D)) # indirect doctest
        \\begin{tikzpicture}[scale = 0.5,thick, baseline={(0,-1ex/2)}]
        \\tikzstyle{vertex} = [shape = circle, minimum size = 7pt, inner sep = 1pt]
        \\node[vertex] (G--2) at (1.5, -1) [shape = circle, draw] {};
        \\node[vertex] (G--1) at (0.0, -1) [shape = circle, draw] {};
        \\node[vertex] (G-1) at (0.0, 1) [shape = circle, draw] {};
        \\node[vertex] (G-2) at (1.5, 1) [shape = circle, draw] {};
        \\draw[] (G--2) .. controls +(-0.5, 0.5) and +(0.5, 0.5) .. (G--1);
        \\draw[] (G-1) .. controls +(0.5, -0.5) and +(-0.5, -0.5) .. (G-2);
        \\end{tikzpicture}
    """

class PottsRepresentation(CombinatorialFreeModule):
    """
    The Potts representation of the partition algebra.

    Let `P_n(d)` be the :class:`PartitionAlgebra` over `R` with the
    deformation parameter `d \\in \\ZZ_{>0}` being a positive integer.
    Recall the multiplication convention of diagrams in `P_n(d)`
    computing `D D'` by placing `D` above `D'`.

    The *Potts representation* is the  right `P_n(d)`-module on
    `M = V^{\\otimes n}`, with `V = R^d`, with the action given as follows.
    We identify the natural basis vectors in `M` with words of length `n`
    in the alphabet `\\{1, \\dotsc, d\\}` (which we call colors). For a basis
    vector `w` and diagram `D`, define `w \\cdot D` as the sum over all `v`
    such that every part in `w D v` (consider this as coloring the nodes
    of `D`) is given by the same color.

    If `n` is a half integer, then there is an extra fixed color for the
    node `\\lceil n \\rceil`, which is called the *magnetic field direction*
    from the physics interpretation of this representation.

    EXAMPLES:

    In this example, we consider `R = \\QQ` and use the Potts representation
    to construct the centralizer algebra of the left `S_{d-1}`-action on
    `V^{\\otimes n}` with `V = \\QQ^d` being the permutation action. ::

        sage: PA = algebras.Partition(5/2, QQ(2))
        sage: PR = PA.potts_representation(2)
        sage: mats = [PR.representation_matrix(x) for x in PA.basis()]
        sage: MS = mats[0].parent()
        sage: CM = MS.submodule(mats)
        sage: CM.dimension()
        16

    We check that this commutes with the `S_{d-1}`-action::

        sage: all((g * v) * x == g * (v * x) for g in PR.symmetric_group()
        ....:     for v in PR.basis() for x in PA.basis())
        True

    Next, we see that the centralizer of the `S_d`-action is smaller
    than the semisimple quotient of the partition algebra::

        sage: PA.dimension()
        52
        sage: len(PA.radical_basis())
        9
        sage: SQ = PA.semisimple_quotient()
        sage: SQ.dimension()
        43

    Next, we get orthogonal idempotents that project onto the central
    orthogonal idempotents in the semisimple quotient and construct
    the corresponding Peirce summands `e_i P_n(d) e_i`::

        sage: # long time
        sage: orth_idems = PA.orthogonal_idempotents_central_mod_radical()
        sage: algs = [PA.peirce_summand(idm, idm) for idm in orth_idems]
        sage: [A.dimension() for A in algs]
        [16, 2, 1, 25]

    We saw that we obtain the entire endomorphism algebra since `d = 2`
    and `S_{d-1}` is the trivial group. Hence, the 16 dimensional Peirce
    summand computed above is isomorphic to this endomorphism algebra
    (both are `4 \\times 4` matrix algebras over `\\QQ`). Hence, we have a
    natural quotient construction of the centralizer algebra from the
    partition algebra.

    Next, we consider a case with a nontrivial `S_d`-action (now it is `S_d`
    since the partition algebra has integer rank). We perform the same
    computations as before::

        sage: PA = algebras.Partition(2, QQ(2))
        sage: PA.dimension()
        15
        sage: PA.semisimple_quotient().dimension()
        10
        sage: orth_idems = PA.orthogonal_idempotents_central_mod_radical()
        sage: algs = [PA.peirce_summand(idm, idm) for idm in orth_idems]
        sage: [A.dimension() for A in algs]
        [4, 2, 4, 1]

        sage: PR = PA.potts_representation()
        sage: mats = [PR.representation_matrix(x) for x in PA.basis()]
        sage: MS = mats[0].parent()
        sage: cat = Algebras(QQ).WithBasis().Subobjects()
        sage: CM = MS.submodule(mats, category=cat)
        sage: CM.dimension()
        8

    To do the remainder of the computation, we need to monkey patch a
    ``product_on_basis`` method::

        sage: CM.product_on_basis
        NotImplemented
        sage: CM.product_on_basis = lambda x,y: CM.retract(CM.basis()[x].lift() * CM.basis()[y].lift())
        sage: CM.orthogonal_idempotents_central_mod_radical()
        (1/2*B[0] + 1/2*B[3] + 1/2*B[5] + 1/2*B[6],
         1/2*B[0] - 1/2*B[3] + 1/2*B[5] - 1/2*B[6])
        sage: CM.peirce_decomposition()
        [[Free module generated by {0, 1, 2, 3} over Rational Field,
          Free module generated by {} over Rational Field],
         [Free module generated by {} over Rational Field,
          Free module generated by {0, 1, 2, 3} over Rational Field]]

    Hence, we see that the centralizer algebra is isomorphic to a product
    of two `2 \\times 2` matrix algebras (over `\\QQ`), which are naturally
    a part of the partition algebra decomposition.

    Lastly, we verify the commuting actions::

        sage: all((g * v) * x == g * (v * x) for g in PR.symmetric_group()
        ....:     for v in PR.basis() for x in PA.basis())
        True

    REFERENCES:

    - [MR1998]_
    """
    def __init__(self, PA, y) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: PA = algebras.Partition(5/2, QQ(4))
            sage: PR = PA.potts_representation()
            sage: TestSuite(PR).run()

            sage: PA = algebras.Partition(5/2, QQ(2))  # not semisimple
            sage: PR = PA.potts_representation()
            sage: TestSuite(PR).run()
            sage: PR = PA.potts_representation(2)
            sage: TestSuite(PR).run()

        ::

            sage: PA = algebras.Partition(2, QQ(4))
            sage: PR = PA.potts_representation()
            sage: TestSuite(PR).run()

            sage: PA = algebras.Partition(3, QQ(2))  # not semisimple
            sage: PR = PA.potts_representation()
            sage: TestSuite(PR).run()

        TESTS::

            sage: PA = algebras.Partition(3, QQ(0))
            sage: PA.potts_representation()
            Traceback (most recent call last):
            ...
            ValueError: the partition algebra deformation parameter must be a positive integer

            sage: PA = algebras.Partition(3, QQ(2))
            sage: PA.potts_representation(1)
            Traceback (most recent call last):
            ...
            ValueError: the magnetic field direction should not be given for integer rank

            sage: PA = algebras.Partition(5/2, QQ(4))
            sage: PA.potts_representation(6)
            Traceback (most recent call last):
            ...
            ValueError: the magnetic field direction must be an integer in [1, 4]
            sage: PA.potts_representation(0)
            Traceback (most recent call last):
            ...
            ValueError: the magnetic field direction must be an integer in [1, 4]
            sage: PA.potts_representation(3/2)
            Traceback (most recent call last):
            ...
            ValueError: the magnetic field direction must be an integer in [1, 4]
        """
    def __getitem__(self, ind):
        """
        Return the basis element indexed by ``ind``.

        EXAMPLES::

            sage: PA = algebras.Partition(4, QQ(3))
            sage: PR = PA.potts_representation()
            sage: PR[1,2,1,3]
            P[word: 1213]

            sage: PA = algebras.Partition(1, QQ(4))
            sage: PR = PA.potts_representation()
            sage: PR[2]
            P[word: 2]
            sage: PR[10]
            Traceback (most recent call last):
            ...
            AttributeError: 'PottsRepresentation_with_category' object has no attribute 'list'
        """
    def partition_algebra(self):
        """
        Return the partition algebra that ``self`` is a representation of.

        EXAMPLES::

            sage: PA = algebras.Partition(3, QQ(4))
            sage: PR = PA.potts_representation()
            sage: PR.partition_algebra() is PA
            True
        """
    def number_of_factors(self):
        """
        Return the number of factors defining ``self``.

        EXAMPLES::

            sage: PA = algebras.Partition(7/2, QQ(4))
            sage: PR = PA.potts_representation()
            sage: PR.number_of_factors()
            3
        """
    def number_of_colors(self):
        """
        Return the number of colors defining ``self``.

        EXAMPLES::

            sage: PA = algebras.Partition(3, QQ(4))
            sage: PR = PA.potts_representation()
            sage: PR.number_of_colors()
            4
        """
    def magnetic_field_direction(self):
        """
        Return the magnetic field direction defining ``self``.

        EXAMPLES::

            sage: PA = algebras.Partition(7/2, QQ(4))
            sage: PR = PA.potts_representation(2)
            sage: PR.magnetic_field_direction()
            2
        """
    def symmetric_group(self):
        """
        Return the symmetric group that naturally acts on ``self``.

        EXAMPLES::

            sage: PA = algebras.Partition(3, QQ(4))
            sage: PR = PA.potts_representation()
            sage: PR.symmetric_group()
            Symmetric group of order 4! as a permutation group

            sage: PA = algebras.Partition(7/2, QQ(4))
            sage: PR = PA.potts_representation()
            sage: PR.symmetric_group().domain()
            {2, 3, 4}
            sage: PR = PA.potts_representation(2)
            sage: PR.symmetric_group().domain()
            {1, 3, 4}
            sage: PR = PA.potts_representation(4)
            sage: PR.symmetric_group().domain()
            {1, 2, 3}
        """
    def representation_matrix(self, elt):
        """
        Return the representation matrix of ``self`` in ``self``.

        EXAMPLES::

            sage: PA = algebras.Partition(7/2, QQ(2))
            sage: PR = PA.potts_representation()
            sage: PR.representation_matrix(PA.an_element())
            [7 0 3 0 2 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]

            sage: all(b.to_vector() * PR.representation_matrix(x)  # long time
            ....:     == (b * x).to_vector()
            ....:     for b in PR.basis() for x in PA.basis())
            True

            sage: PA = algebras.Partition(2, QQ(2))
            sage: PR = PA.potts_representation()
            sage: [PR.representation_matrix(x) for x in PA.basis()]
            [
            [1 0 0 0]  [1 0 1 0]  [1 1 0 0]  [1 0 0 1]  [1 1 1 1]  [1 0 0 0]
            [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [1 0 0 0]
            [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 0]  [0 0 0 1]
            [0 0 0 1], [0 1 0 1], [0 0 1 1], [1 0 0 1], [1 1 1 1], [0 0 0 1],
            <BLANKLINE>
            [1 0 0 0]  [1 0 1 0]  [1 0 0 0]  [1 0 0 0]  [1 0 1 0]  [1 1 0 0]
            [0 0 1 0]  [1 0 1 0]  [0 1 0 0]  [0 0 0 1]  [0 1 0 1]  [1 1 0 0]
            [0 1 0 0]  [0 1 0 1]  [0 0 1 0]  [1 0 0 0]  [1 0 1 0]  [0 0 1 1]
            [0 0 0 1], [0 1 0 1], [0 0 0 1], [0 0 0 1], [0 1 0 1], [0 0 1 1],
            <BLANKLINE>
            [1 1 0 0]  [1 0 0 1]  [1 1 1 1]
            [0 0 1 1]  [1 0 0 1]  [1 1 1 1]
            [1 1 0 0]  [1 0 0 1]  [1 1 1 1]
            [0 0 1 1], [1 0 0 1], [1 1 1 1]
            ]

            sage: PA = algebras.Partition(5/2, QQ(2))
            sage: PR = PA.potts_representation()
            sage: all(PR.representation_matrix(x) * PR.representation_matrix(y)  # long time
            ....:     == PR.representation_matrix(x * y)
            ....:     for x in PA.basis() for y in PA.basis())
            True

            sage: PA = algebras.Partition(2, QQ(4))
            sage: PR = PA.potts_representation()
            sage: all(PR.representation_matrix(x) * PR.representation_matrix(y)
            ....:     == PR.representation_matrix(x * y)
            ....:     for x in PA.basis() for y in PA.basis())
            True
        """
    class Element(CombinatorialFreeModule.Element): ...

def is_planar(sp):
    """
    Return ``True`` if the diagram corresponding to the set partition ``sp``
    is planar; otherwise, return ``False``.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: da.is_planar( da.to_set_partition([[1,-2],[2,-1]]))
        False
        sage: da.is_planar( da.to_set_partition([[1,-1],[2,-2]]))
        True
    """
def to_graph(sp):
    """
    Return a graph representing the set partition ``sp``.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: g = da.to_graph( da.to_set_partition([[1,-2],[2,-1]])); g
        Graph on 4 vertices

        sage: g.vertices(sort=True)
        [-2, -1, 1, 2]
        sage: g.edges(sort=True)
        [(-2, 1, None), (-1, 2, None)]
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

        sage: import sage.combinat.diagram_algebras as da
        sage: sp1 = da.to_set_partition([[1,-2],[2,-1]])
        sage: sp2 = da.to_set_partition([[1,-2],[2,-1]])
        sage: g = da.pair_to_graph( sp1, sp2 ); g
        Graph on 8 vertices

        sage: g.vertices(sort=True)
        [(-2, 1), (-2, 2), (-1, 1), (-1, 2), (1, 1), (1, 2), (2, 1), (2, 2)]
        sage: g.edges(sort=True)
        [((-2, 1), (1, 1), None), ((-2, 1), (2, 2), None),
         ((-2, 2), (1, 2), None), ((-1, 1), (1, 2), None),
         ((-1, 1), (2, 1), None), ((-1, 2), (2, 2), None)]

    Another example which used to be wrong until :issue:`15958`::

        sage: sp3 = da.to_set_partition([[1, -1], [2], [-2]])
        sage: sp4 = da.to_set_partition([[1], [-1], [2], [-2]])
        sage: g = da.pair_to_graph( sp3, sp4 ); g
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

    The propagating number is the number of blocks with both a positive and
    negative number.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: sp1 = da.to_set_partition([[1,-2],[2,-1]])
        sage: sp2 = da.to_set_partition([[1,2],[-2,-1]])
        sage: da.propagating_number(sp1)
        2
        sage: da.propagating_number(sp2)
        0
    """
def to_set_partition(l, k=None):
    """
    Convert input to a set partition of `\\{1, \\ldots, k, -1, \\ldots, -k\\}`.

    Convert a list of a list of numbers to a set partitions. Each list
    of numbers in the outer list specifies the numbers contained in one
    of the blocks in the set partition.

    If `k` is specified, then the set partition will be a set partition
    of `\\{1, \\ldots, k, -1, \\ldots, -k\\}`. Otherwise, `k` will default to
    the minimum number needed to contain all of the specified numbers.

    INPUT:

    - ``l`` -- list of lists of integers
    - ``k`` -- integer (default: ``None``)

    OUTPUT: list of sets

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: f = lambda sp: SetPartition(da.to_set_partition(sp))
        sage: f([[1,-1],[2,-2]]) == SetPartition(da.identity_set_partition(2))
        True
        sage: da.to_set_partition([[1]])
        [{1}, {-1}]
        sage: da.to_set_partition([[1,-1],[-2,3]],9/2)
        [{-1, 1}, {-2, 3}, {2}, {-4, 4}, {-5, 5}, {-3}]
    """
def to_Brauer_partition(l, k=None):
    """
    Same as :func:`to_set_partition` but assumes omitted elements are
    connected straight through.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: f = lambda sp: SetPartition(da.to_Brauer_partition(sp))
        sage: f([[1,2],[-1,-2]]) == SetPartition([[1,2],[-1,-2]])
        True
        sage: f([[1,3],[-1,-3]]) == SetPartition([[1,3],[-3,-1],[2,-2]])
        True
        sage: f([[1,-4],[-3,-1],[3,4]]) == SetPartition([[-3,-1],[2,-2],[1,-4],[3,4]])
        True
        sage: p = SetPartition([[1,2],[-1,-2],[3,-3],[4,-4]])
        sage: SetPartition(da.to_Brauer_partition([[1,2],[-1,-2]], k=4)) == p
        True
    """
def identity_set_partition(k):
    """
    Return the identity set partition `\\{\\{1, -1\\}, \\ldots, \\{k, -k\\}\\}`.

    EXAMPLES::

        sage: import sage.combinat.diagram_algebras as da
        sage: SetPartition(da.identity_set_partition(2))
        {{-2, 2}, {-1, 1}}
    """
