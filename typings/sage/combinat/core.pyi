from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Core(CombinatorialElement):
    """
    A `k`-core is an integer partition from which no rim hook of size `k`
    can be removed.

    EXAMPLES::

        sage: c = Core([2,1],4); c
        [2, 1]
        sage: c = Core([3,1],4); c
        Traceback (most recent call last):
        ...
        ValueError: [3, 1] is not a 4-core
    """
    @staticmethod
    def __classcall_private__(cls, part, k):
        """
        Implement the shortcut ``Core(part, k)`` to ``Cores(k,l)(part)``
        where `l` is the length of the core.

        TESTS::

            sage: c = Core([2,1],4); c
            [2, 1]
            sage: c.parent()
            4-Cores of length 3
            sage: type(c)
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>

            sage: Core([2,1],3)
            Traceback (most recent call last):
            ...
            ValueError: [2, 1] is not a 3-core
        """
    def __init__(self, parent, core) -> None:
        """
        TESTS::

            sage: C = Cores(4,3)
            sage: c = C([2,1]); c
            [2, 1]
            sage: type(c)
            <class 'sage.combinat.core.Cores_length_with_category.element_class'>
            sage: c.parent()
            4-Cores of length 3
            sage: TestSuite(c).run()

            sage: C = Cores(3,3)
            sage: C([2,1])
            Traceback (most recent call last):
            ...
            ValueError: [2, 1] is not a 3-core
        """
    def __eq__(self, other) -> bool:
        """
        Test for equality.

        EXAMPLES::

            sage: c = Core([4,2,1,1],5)
            sage: d = Core([4,2,1,1],5)
            sage: e = Core([4,2,1,1],6)
            sage: c == [4,2,1,1]
            False
            sage: c == d
            True
            sage: c == e
            False
        """
    def __ne__(self, other) -> bool:
        """
        Test for un-equality.

        EXAMPLES::

            sage: c = Core([4,2,1,1],5)
            sage: d = Core([4,2,1,1],5)
            sage: e = Core([4,2,1,1],6)
            sage: c != [4,2,1,1]
            True
            sage: c != d
            False
            sage: c != e
            True
        """
    def __hash__(self):
        """
        Compute the hash of ``self`` by computing the hash of the
        underlying list and of the additional parameter.

        The hash is cached and stored in ``self._hash``.

        EXAMPLES::

            sage: c = Core([4,2,1,1],3)
            sage: c._hash is None
            True
            sage: hash(c) #random
            1335416675971793195
            sage: c._hash #random
            1335416675971793195

        TESTS::

            sage: c = Core([4,2,1,1],5)
            sage: d = Core([4,2,1,1],6)
            sage: hash(c) == hash(d)
            False
        """
    def k(self):
        """
        Return `k` of the `k`-core ``self``.

        EXAMPLES::

            sage: c = Core([2,1],4)
            sage: c.k()
            4
        """
    def to_partition(self):
        """
        Turn the core ``self`` into the partition identical to ``self``.

        EXAMPLES::

            sage: mu = Core([2,1,1],3)
            sage: mu.to_partition()
            [2, 1, 1]
        """
    def to_bounded_partition(self):
        """
        Bijection between `k`-cores and `(k-1)`-bounded partitions.

        This maps the `k`-core ``self`` to the corresponding `(k-1)`-bounded partition.
        This bijection is achieved by deleting all cells in ``self`` of hook length
        greater than `k`.

        EXAMPLES::

            sage: gamma = Core([9,5,3,2,1,1], 5)
            sage: gamma.to_bounded_partition()
            [4, 3, 2, 2, 1, 1]
        """
    def size(self):
        """
        Return the size of ``self`` as a partition.

        EXAMPLES::

            sage: Core([2,1],4).size()
            3
            sage: Core([4,2],3).size()
            6
        """
    def length(self):
        """
        Return the length of ``self``.

        The length of a `k`-core is the size of the corresponding `(k-1)`-bounded partition
        which agrees with the length of the corresponding Grassmannian element,
        see :meth:`to_grassmannian`.

        EXAMPLES::

            sage: c = Core([4,2],3); c.length()
            4
            sage: c.to_grassmannian().length()                                          # needs sage.modules
            4

            sage: Core([9,5,3,2,1,1], 5).length()
            13
        """
    def to_grassmannian(self):
        """
        Bijection between `k`-cores and Grassmannian elements in the affine Weyl group of type `A_{k-1}^{(1)}`.

        For further details, see the documentation of the method
        :meth:`~sage.combinat.partition.Partition.from_kbounded_to_reduced_word` and
        :meth:`~sage.combinat.partition.Partition.from_kbounded_to_grassmannian`.

        EXAMPLES::

            sage: c = Core([3,1,1],3)
            sage: w = c.to_grassmannian(); w                                            # needs sage.modules
            [-1  1  1]
            [-2  2  1]
            [-2  1  2]
            sage: c.parent()
            3-Cores of length 4
            sage: w.parent()                                                            # needs sage.modules
            Weyl Group of type ['A', 2, 1] (as a matrix group acting on the root space)

            sage: c = Core([],3)
            sage: c.to_grassmannian()                                                   # needs sage.modules
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def affine_symmetric_group_simple_action(self, i):
        """
        Return the action of the simple transposition `s_i` of the affine symmetric group on ``self``.

        This gives the action of the affine symmetric group of type `A_k^{(1)}` on the `k`-core
        ``self``. If ``self`` has outside (resp. inside) corners of content `i` modulo `k`, then
        these corners are added (resp. removed). Otherwise the action is trivial.

        EXAMPLES::

            sage: c = Core([4,2],3)
            sage: c.affine_symmetric_group_simple_action(0)                             # needs sage.modules
            [3, 1]
            sage: c.affine_symmetric_group_simple_action(1)                             # needs sage.modules
            [5, 3, 1]
            sage: c.affine_symmetric_group_simple_action(2)                             # needs sage.modules
            [4, 2]

        This action corresponds to the left action by the `i`-th simple reflection in the affine
        symmetric group::

            sage: c = Core([4,2],3)
            sage: W = c.to_grassmannian().parent()                                      # needs sage.modules
            sage: i = 0
            sage: (c.affine_symmetric_group_simple_action(i).to_grassmannian()          # needs sage.modules
            ....:     == W.simple_reflection(i)*c.to_grassmannian())
            True
            sage: i = 1
            sage: (c.affine_symmetric_group_simple_action(i).to_grassmannian()          # needs sage.modules
            ....:     == W.simple_reflection(i)*c.to_grassmannian())
            True
        """
    def affine_symmetric_group_action(self, w, transposition: bool = False):
        """
        Return the (left) action of the affine symmetric group on ``self``.

        INPUT:

        - ``w`` -- tuple of integers `[w_1,\\ldots,w_m]` with `0\\le w_j<k`.
          If transposition is set to be ``True``, then `w = [w_0,w_1]` is
          interpreted as a transposition `t_{w_0, w_1}`
          (see :meth:`_transposition_to_reduced_word`).

        - ``transposition`` -- boolean (default: ``False``)

        The output is the (left) action of the product of the corresponding simple transpositions
        on ``self``, that is `s_{w_1} \\cdots s_{w_m}(self)`. See :meth:`affine_symmetric_group_simple_action`.

        EXAMPLES::

            sage: c = Core([4,2],3)
            sage: c.affine_symmetric_group_action([0,1,0,2,1])
            [8, 6, 4, 2]
            sage: c.affine_symmetric_group_action([0,2], transposition=True)
            [4, 2, 1, 1]

            sage: c = Core([11,8,5,5,3,3,1,1,1],4)
            sage: c.affine_symmetric_group_action([2,5],transposition=True)
            [11, 8, 7, 6, 5, 4, 3, 2, 1]
        """
    def weak_le(self, other):
        """
        Weak order comparison on cores.

        INPUT:

        - ``other`` -- another `k`-core

        OUTPUT: boolean

        This returns whether ``self`` <= ``other`` in weak order.

        EXAMPLES::

            sage: c = Core([4,2],3)
            sage: x = Core([5,3,1],3)
            sage: c.weak_le(x)                                                          # needs sage.modules
            True
            sage: c.weak_le([5,3,1])                                                    # needs sage.modules
            True

            sage: x = Core([4,2,2,1,1],3)
            sage: c.weak_le(x)                                                          # needs sage.modules
            False

            sage: x = Core([5,3,1],6)
            sage: c.weak_le(x)
            Traceback (most recent call last):
            ...
            ValueError: the two cores do not have the same k
        """
    def weak_covers(self):
        """
        Return a list of all elements that cover ``self`` in weak order.

        EXAMPLES::

            sage: c = Core([1],3)
            sage: c.weak_covers()                                                       # needs sage.modules
            [[1, 1], [2]]

            sage: c = Core([4,2],3)
            sage: c.weak_covers()                                                       # needs sage.modules
            [[5, 3, 1]]
        """
    def strong_le(self, other):
        """
        Strong order (Bruhat) comparison on cores.

        INPUT:

        - ``other`` -- another `k`-core

        OUTPUT: boolean

        This returns whether ``self`` <= ``other`` in Bruhat (or strong) order.

        EXAMPLES::

            sage: c = Core([4,2],3)
            sage: x = Core([4,2,2,1,1],3)
            sage: c.strong_le(x)
            True
            sage: c.strong_le([4,2,2,1,1])
            True

            sage: x = Core([4,1],4)
            sage: c.strong_le(x)
            Traceback (most recent call last):
            ...
            ValueError: the two cores do not have the same k
        """
    def contains(self, other) -> bool:
        """
        Check whether ``self`` contains ``other``.

        INPUT:

        - ``other`` -- another `k`-core or a list

        OUTPUT: boolean

        This returns ``True`` if the Ferrers diagram of ``self`` contains the
        Ferrers diagram of ``other``.

        EXAMPLES::

            sage: c = Core([4,2],3)
            sage: x = Core([4,2,2,1,1],3)
            sage: x.contains(c)
            True
            sage: c.contains(x)
            False
        """
    def strong_covers(self):
        """
        Return a list of all elements that cover ``self`` in strong order.

        EXAMPLES::

            sage: c = Core([1],3)
            sage: c.strong_covers()
            [[2], [1, 1]]
            sage: c = Core([4,2],3)
            sage: c.strong_covers()
            [[5, 3, 1], [4, 2, 1, 1]]
        """
    def strong_down_list(self):
        """
        Return a list of all elements that are covered by ``self`` in strong order.

        EXAMPLES::

            sage: c = Core([1],3)
            sage: c.strong_down_list()
            [[]]
            sage: c = Core([5,3,1],3)
            sage: c.strong_down_list()
            [[4, 2], [3, 1, 1]]
        """

def Cores(k, length=None, **kwargs):
    """
    A `k`-core is a partition from which no rim hook of size `k` can be removed.
    Alternatively, a `k`-core is an integer partition such that the Ferrers
    diagram for the partition contains no cells with a hook of size (a multiple of) `k`.

    The `k`-cores generally have two notions of size which are
    useful for different applications. One is the number of cells in the
    Ferrers diagram with hook less than `k`, the other is the total
    number of cells of the Ferrers diagram.  In the implementation in
    Sage, the first of notion is referred to as the ``length`` of the `k`-core
    and the second is the ``size`` of the `k`-core.  The class
    of Cores requires that either the size or the length of the elements in
    the class is specified.

    EXAMPLES:

    We create the set of the `4`-cores of length `6`. Here the length of a `k`-core is the size
    of the corresponding `(k-1)`-bounded partition, see also :meth:`~sage.combinat.core.Core.length`::

        sage: C = Cores(4, 6); C
        4-Cores of length 6
        sage: C.list()
        [[6, 3], [5, 2, 1], [4, 1, 1, 1], [4, 2, 2], [3, 3, 1, 1], [3, 2, 1, 1, 1], [2, 2, 2, 1, 1, 1]]
        sage: C.cardinality()
        7
        sage: C.an_element()
        [6, 3]

    We may also list the set of `4`-cores of size `6`, where the size is the number of boxes in the
    core, see also :meth:`~sage.combinat.core.Core.size`::

        sage: C = Cores(4, size=6); C
        4-Cores of size 6
        sage: C.list()
        [[4, 1, 1], [3, 2, 1], [3, 1, 1, 1]]
        sage: C.cardinality()
        3
        sage: C.an_element()
        [4, 1, 1]
    """

class Cores_length(UniqueRepresentation, Parent):
    """
    The class of `k`-cores of length `n`.
    """
    k: Incomplete
    n: Incomplete
    def __init__(self, k, n) -> None:
        """
        TESTS::

            sage: C = Cores(3, 4)
            sage: TestSuite(C).run()
        """
    def list(self):
        """
        Return the list of all `k`-cores of length `n`.

        EXAMPLES::

            sage: C = Cores(3,4)
            sage: C.list()
            [[4, 2], [3, 1, 1], [2, 2, 1, 1]]
        """
    def from_partition(self, part):
        """
        Convert the partition ``part`` into a core (as the identity map).

        This is the inverse method to :meth:`~sage.combinat.core.Core.to_partition`.

        EXAMPLES::

            sage: C = Cores(3,4)
            sage: c = C.from_partition([4,2]); c
            [4, 2]

            sage: mu = Partition([2,1,1])
            sage: C = Cores(3,3)
            sage: C.from_partition(mu).to_partition() == mu
            True

            sage: mu = Partition([])
            sage: C = Cores(3,0)
            sage: C.from_partition(mu).to_partition() == mu
            True
        """
    Element = Core

class Cores_size(UniqueRepresentation, Parent):
    """
    The class of `k`-cores of size `n`.
    """
    k: Incomplete
    n: Incomplete
    def __init__(self, k, n) -> None:
        """
        TESTS::

            sage: C = Cores(3, size = 4)
            sage: TestSuite(C).run()
        """
    def list(self):
        """
        Return the list of all `k`-cores of size `n`.

        EXAMPLES::

            sage: C = Cores(3, size = 4)
            sage: C.list()
            [[3, 1], [2, 1, 1]]
        """
    def from_partition(self, part):
        """
        Convert the partition ``part`` into a core (as the identity map).

        This is the inverse method to :meth:`to_partition`.

        EXAMPLES::

            sage: C = Cores(3,size=4)
            sage: c = C.from_partition([2,1,1]); c
            [2, 1, 1]

            sage: mu = Partition([2,1,1])
            sage: C = Cores(3,size=4)
            sage: C.from_partition(mu).to_partition() == mu
            True

            sage: mu = Partition([])
            sage: C = Cores(3,size=0)
            sage: C.from_partition(mu).to_partition() == mu
            True
        """
    Element = Core
