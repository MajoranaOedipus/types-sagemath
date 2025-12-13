from _typeshed import Incomplete
from collections.abc import Iterator
from sage.arith.misc import Sigma as Sigma, binomial as binomial, factorial as factorial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.tableau import Tableau as Tableau
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PlanePartition(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    A plane partition.

    A *plane partition* is a stack of cubes in the positive orthant.

    INPUT:

    - ``PP`` -- list of lists which represents a tableau
    - ``box_size`` -- (optional) a list ``[A, B, C]`` of 3 positive integers,
      where ``A``, ``B``, ``C`` are the lengths of the box in the `x`-axis,
      `y`-axis, `z`-axis, respectively; if this is not given, it is
      determined by the smallest box bounding ``PP``

    OUTPUT: the plane partition whose tableau representation is ``PP``

    EXAMPLES::

        sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
        sage: PP
        Plane partition [[4, 3, 3, 1], [2, 1, 1], [1, 1]]

    TESTS::

        sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
        sage: TestSuite(PP).run()
        sage: hash(PP) # random
    """
    @staticmethod
    def __classcall_private__(cls, PP, box_size=None):
        """
        Construct a plane partition with the appropriate parent.

        EXAMPLES::

            sage: p = PlanePartition([[2,1],[1]])
            sage: TestSuite(p).run()

            sage: p.parent()
            Plane partitions
            sage: p.category()
            Category of elements of Plane partitions
            sage: type(p)
            <class 'sage.combinat.plane_partition.PlanePartitions_all_with_category.element_class'>
        """
    def __init__(self, parent, pp, check: bool = True) -> None:
        """
        Initialize a plane partition.

        TESTS::

            sage: a = PlanePartitions()([[2,1],[1]])
            sage: b = PlanePartitions([2,2,2])([[2,1],[1]])
            sage: c = PlanePartitions(4)([[2,1],[1]])
            sage: a == b
            True
            sage: a is b
            False
            sage: a == c
            True
            sage: a is c
            False
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        .. TODO::

            This overwrites the comparison check of
            :class:`~sage.structure.list_clone.ClonableArray`
            in order to circumvent the coercion framework.
            Eventually this should be solved more elegantly,
            for example along the lines of what was done for
            `k`-tableaux.

            For now, this compares two elements by their underlying
            defining lists.

        INPUT:

        - ``other`` -- the element that ``self`` is compared to

        OUTPUT: boolean

        TESTS::

            sage: t = PlanePartition([[2,1],[1]])
            sage: t == 0
            False
            sage: t == PlanePartitions(4)([[2,1],[1]])
            True

            sage: s = PlanePartition([[3,1],[1]])
            sage: s != []
            True

            sage: t < s
            True
            sage: s < t
            False
            sage: s > t
            True
        """
    def check(self) -> None:
        """
        Check to see that ``self`` is a valid plane partition.

        EXAMPLES::

            sage: a = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: a.check()
            sage: b = PlanePartition([[1,2],[1]])
            Traceback (most recent call last):
            ...
            ValueError: not weakly decreasing along rows
            sage: c = PlanePartition([[1,1],[2]])
            Traceback (most recent call last):
            ...
            ValueError: not weakly decreasing along columns
            sage: d = PlanePartition([[2,-1],[-2]])
            Traceback (most recent call last):
            ...
            ValueError: entries not all nonnegative
            sage: e = PlanePartition([[3/2,1],[.5]])
            Traceback (most recent call last):
            ...
            ValueError: entries not all integers
        """
    def to_tableau(self) -> Tableau:
        """
        Return the tableau class of ``self``.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.to_tableau()
            [[4, 3, 3, 1], [2, 1, 1], [1, 1]]
        """
    def z_tableau(self, tableau: bool = True) -> Tableau:
        """
        Return the projection of ``self`` in the `z` direction.

        If ``tableau`` is set to ``False``, then only the list of lists
        consisting of the projection of boxes size onto the `xy`-plane
        is returned instead of a :class:`Tableau` object. This output will
        not have empty trailing rows or trailing zeros removed.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.z_tableau()
            [[4, 3, 3, 1], [2, 1, 1, 0], [1, 1, 0, 0]]
        """
    def y_tableau(self, tableau: bool = True) -> Tableau:
        """
        Return the projection of ``self`` in the `y` direction.

        If ``tableau`` is set to ``False``, then only the list of lists
        consisting of the projection of boxes size onto the `xz`-plane
        is returned instead of a :class:`Tableau` object. This output will
        not have empty trailing rows or trailing zeros removed.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.y_tableau()
            [[4, 3, 2], [3, 1, 0], [3, 0, 0], [1, 0, 0]]
        """
    def x_tableau(self, tableau: bool = True) -> Tableau:
        """
        Return the projection of ``self`` in the `x` direction.

        If ``tableau`` is set to ``False``, then only the list of lists
        consisting of the projection of boxes size onto the `yz`-plane
        is returned instead of a :class:`Tableau` object. This output will
        not have empty trailing rows or trailing zeros removed.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.x_tableau()
            [[3, 2, 1, 1], [3, 1, 1, 0], [2, 1, 1, 0], [1, 0, 0, 0]]
        """
    def cells(self) -> list[tuple[int, int, int]]:
        """
        Return the list of cells inside ``self``.

        Each cell is a tuple.

        EXAMPLES::

            sage: PP = PlanePartition([[3,1],[2]])
            sage: PP.cells()
            [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (1, 0, 0), (1, 0, 1)]
        """
    def number_of_boxes(self) -> Integer:
        """
        Return the number of boxes in the plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[3,1],[2]])
            sage: PP.number_of_boxes()
            6
        """
    def pp(self, show_box: bool = False) -> None:
        """
        Return a pretty print of the plane partition.

        INPUT:

        - ``show_box`` -- boolean (default: ``False``); if ``True``,
          also shows the visible tiles on the `xy`-, `yz`-, `zx`-planes

        OUTPUT: a pretty print of the plane partition

        EXAMPLES::

            sage: PlanePartition([[4,3,3,1],[2,1,1],[1,1]]).pp()
                    __
                   /\\_\\\n                __/\\/_/
             __/\\_\\/\\_\\\n            /\\_\\/_/\\/\\_\\\n            \\/\\_\\_\\/\\/_/
             \\/_/\\_\\/_/
                \\/_/\\_\\\n                   \\/_/
            sage: PlanePartition([[4,3,3,1],[2,1,1],[1,1]]).pp(True)
                ______
               /_/_/\\_\\\n              /_/_/\\/_/\\\n             /_/\\_\\/\\_\\/\\\n            /\\_\\/_/\\/\\_\\/\\\n            \\/\\_\\_\\/\\/_/\\/
             \\/_/\\_\\/_/\\/
              \\_\\/_/\\_\\/
               \\_\\_\\/_/
        """
    def plot(self, show_box: bool = False, colors=None):
        '''
        Return a plot of ``self``.

        INPUT:

        - ``show_box`` -- boolean (default: ``False``); if ``True``,
          also shows the visible tiles on the `xy`-, `yz`-, `zx`-planes
        - ``colors`` -- (default: ``["white", "lightgray", "darkgray"]``)
          list ``[A, B, C]`` of 3 strings representing colors

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.plot()                                                             # needs sage.plot
            Graphics object consisting of 27 graphics primitives
        '''
    def contains(self, PP) -> bool:
        """
        Return ``True`` if ``PP`` is a plane partition that fits
        inside ``self``.

        Specifically, ``self`` contains ``PP`` if, for all `i`, `j`,
        the height of ``PP`` at `ij` is less than or equal to the
        height of ``self`` at `ij`.

        EXAMPLES::

            sage: P1 = PlanePartition([[5,4,3], [3,2,2], [1]])
            sage: P2 = PlanePartition([[3,2], [1,1], [0,0], [0,0]])
            sage: P3 = PlanePartition([[5,5,5], [2,1,0]])
            sage: P1.contains(P2)
            True
            sage: P2.contains(P1)
            False
            sage: P1.contains(P3)
            False
            sage: P3.contains(P2)
            True
        """
    def plot3d(self, colors=None):
        '''
        Return a 3D-plot of ``self``.

        INPUT:

        - ``colors`` -- (default: ``["white", "lightgray", "darkgray"]``)
          list ``[A, B, C]`` of 3 strings representing colors

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.plot3d()                                                           # needs sage.plot
            Graphics3d Object
        '''
    def complement(self, tableau_only: bool = False) -> PP:
        """
        Return the complement of ``self``.

        If the parent of ``self`` consists only of partitions inside a given
        box, then the complement is taken in this box. Otherwise, the
        complement is taken in the smallest box containing the plane partition.
        The empty plane partition with no box specified is its own complement.

        If ``tableau_only`` is set to ``True``, then only the tableau
        consisting of the projection of boxes size onto the `xy`-plane
        is returned instead of a :class:`PlanePartition`. This output will
        not have empty trailing rows or trailing zeros removed.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.complement()
            Plane partition [[4, 4, 3, 3], [4, 3, 3, 2], [3, 1, 1]]
            sage: PP.complement(True)
            [[4, 4, 3, 3], [4, 3, 3, 2], [3, 1, 1, 0]]
        """
    def transpose(self, tableau_only: bool = False) -> PP:
        """
        Return the transpose of ``self``.

        If ``tableau_only`` is set to ``True``, then only the tableau
        consisting of the projection of boxes size onto the `xy`-plane
        is returned instead of a :class:`PlanePartition`. This will
        not necessarily have trailing rows or trailing zeros removed.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.transpose()
            Plane partition [[4, 2, 1], [3, 1, 1], [3, 1], [1]]
            sage: PP.transpose(True)
            [[4, 2, 1], [3, 1, 1], [3, 1, 0], [1, 0, 0]]

            sage: PPP = PlanePartitions([1, 2, 3])
            sage: PP = PPP([[1, 1]])
            sage: PT = PP.transpose(); PT
            Plane partition [[1], [1]]
            sage: PT.parent()
            Plane partitions inside a 2 x 1 x 3 box
        """
    def is_SPP(self) -> bool:
        """
        Return whether ``self`` is a symmetric plane partition.

        A plane partition is symmetric if the corresponding tableau is
        symmetric about the diagonal.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_SPP()
            False
            sage: PP = PlanePartition([[3,3,2],[3,3,2],[2,2,2]])
            sage: PP.is_SPP()
            True
            sage: PP = PlanePartition([[3,2,1],[2,0,0]])
            sage: PP.is_SPP()
            False
            sage: PP = PlanePartition([[3,2,0],[2,0,0]])
            sage: PP.is_SPP()
            True
            sage: PP = PlanePartition([[3,2],[2,0],[1,0]])
            sage: PP.is_SPP()
            False
            sage: PP = PlanePartition([[3,2],[2,0],[0,0]])
            sage: PP.is_SPP()
            True

        TESTS::

            sage: PlanePartition([]).is_SPP()
            True
        """
    def is_CSPP(self) -> bool:
        """
        Return whether ``self`` is a cyclically symmetric plane partition.

        A plane partition is cyclically symmetric if its `x`, `y`, and `z`
        tableaux are all equal.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_CSPP()
            False
            sage: PP = PlanePartition([[3,2,2],[3,1,0],[1,1,0]])
            sage: PP.is_CSPP()
            True

        TESTS::

            sage: PlanePartition([]).is_CSPP()
            True
        """
    def is_TSPP(self) -> bool:
        """
        Return whether ``self`` is a totally symmetric plane partition.

        A plane partition is totally symmetric if it is both symmetric and
        cyclically symmetric.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_TSPP()
            False
            sage: PP = PlanePartition([[3,3,3],[3,3,2],[3,2,1]])
            sage: PP.is_TSPP()
            True

        TESTS::

            sage: PlanePartition([]).is_TSPP()
            True
        """
    def is_SCPP(self) -> bool:
        """
        Return whether ``self`` is a self-complementary plane partition.

        Note that the complement of a plane partition (and thus the property of
        being self-complementary) is dependent on the choice of a box that it is
        contained in. If no parent/bounding box is specified,  the box is taken
        to be the smallest box that contains the plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_SCPP()
            False
            sage: PP = PlanePartition([[4,4,4,4],[4,4,2,0],[4,2,0,0],[0,0,0,0]])
            sage: PP.is_SCPP()
            False
            sage: PP = PlanePartitions([4,4,4])([[4,4,4,4],[4,4,2,0],[4,2,0,0],[0,0,0,0]])
            sage: PP.is_SCPP()
            True

        TESTS::

            sage: PlanePartition([]).is_SCPP()
            True
        """
    def is_TCPP(self) -> bool:
        """
        Return whether ``self`` is a transpose-complementary plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_TCPP()
            False
            sage: PP = PlanePartition([[4,4,3,2],[4,4,2,1],[4,2,0,0],[2,0,0,0]])
            sage: PP.is_TCPP()
            True

        TESTS::

            sage: PlanePartition([]).is_TCPP()
            True
        """
    def is_SSCPP(self) -> bool:
        """
        Return whether ``self`` is a symmetric, self-complementary
        plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_SSCPP()
            False
            sage: PP = PlanePartition([[4,3,3,2],[3,2,2,1],[3,2,2,1],[2,1,1,0]])
            sage: PP.is_SSCPP()
            True
            sage: PP = PlanePartition([[2,1],[1,0]])
            sage: PP.is_SSCPP()
            True
            sage: PP = PlanePartition([[4,3,2],[3,2,1],[2,1,0]])
            sage: PP.is_SSCPP()
            True
            sage: PP = PlanePartition([[4,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,0]])
            sage: PP.is_SSCPP()
            True

        TESTS::

            sage: PlanePartition([]).is_SSCPP()
            True
        """
    def is_CSTCPP(self) -> bool:
        """
        Return whether ``self`` is a cyclically symmetric and
        transpose-complementary plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_CSTCPP()
            False
            sage: PP = PlanePartition([[4,4,3,2],[4,3,2,1],[3,2,1,0],[2,1,0,0]])
            sage: PP.is_CSTCPP()
            True

        TESTS::

            sage: PlanePartition([]).is_CSTCPP()
            True
        """
    def is_CSSCPP(self) -> bool:
        """
        Return whether ``self`` is a cyclically symmetric and
        self-complementary plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_CSSCPP()
            False
            sage: PP = PlanePartition([[4,4,4,1],[3,3,2,1],[3,2,1,1],[3,0,0,0]])
            sage: PP.is_CSSCPP()
            True

        TESTS::

            sage: PlanePartition([]).is_CSSCPP()
            True
        """
    def is_TSSCPP(self) -> bool:
        """
        Return whether ``self`` is a totally symmetric self-complementary
        plane partition.

        EXAMPLES::

            sage: PP = PlanePartition([[4,3,3,1],[2,1,1],[1,1]])
            sage: PP.is_TSSCPP()
            False
            sage: PP = PlanePartition([[4,4,3,2],[4,3,2,1],[3,2,1,0],[2,1,0,0]])
            sage: PP.is_TSSCPP()
            True

        TESTS::

            sage: PlanePartition([]).is_TSSCPP()
            True
        """
    def to_order_ideal(self):
        """
        Return the order ideal corresponding to ``self``.

        .. TODO::

            As many families of symmetric plane partitions are in bijection
            with order ideals in an associated poset, this function could
            feasibly have options to send symmetric plane partitions
            to the associated order ideal in that poset, instead.

        EXAMPLES::

            sage: PlanePartition([[3,2,1],[2,2],[2]]).to_order_ideal()                  # needs sage.graphs sage.modules
            [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 2, 0),
             (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 0, 1)]
            sage: PlanePartition([[2,1],[1],[1]]).to_order_ideal()                      # needs sage.graphs sage.modules
            [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (2, 0, 0)]
        """
    def maximal_boxes(self) -> list:
        """
        Return the coordinates of the maximal boxes of ``self``.

        The maximal boxes of a plane partitions are the boxes that can be
        removed from a plane partition and still yield a valid plane partition.

        EXAMPLES::

            sage: sorted(PlanePartition([[3,2,1],[2,2],[2]]).maximal_boxes())
            [[0, 0, 2], [0, 2, 0], [1, 1, 1], [2, 0, 1]]
            sage: sorted(PlanePartition([[2,1],[1],[1]]).maximal_boxes())
            [[0, 0, 1], [0, 1, 0], [2, 0, 0]]
        """
    def cyclically_rotate(self, preserve_parent: bool = False) -> PP:
        """
        Return the cyclic rotation of ``self``.

        By default, if the parent of ``self`` consists of plane
        partitions inside an `a \\times b \\times c` box, the result
        will have a parent consisting of partitions inside
        a `c \\times a \\times b` box, unless the optional parameter
        ``preserve_parent`` is set to ``True``. Enabling this setting
        may give an element that is **not** an element of its parent.

        EXAMPLES::

            sage: PlanePartition([[3,2,1],[2,2],[2]]).cyclically_rotate()
            Plane partition [[3, 3, 1], [2, 2], [1]]
            sage: PP = PlanePartition([[4,1],[1],[1]])
            sage: PP.cyclically_rotate()
            Plane partition [[3, 1, 1, 1], [1]]
            sage: PP == PP.cyclically_rotate().cyclically_rotate().cyclically_rotate()
            True

            sage: # needs sage.graphs sage.modules
            sage: PP = PlanePartitions([4,3,2]).random_element()
            sage: PP.cyclically_rotate().parent()
            Plane partitions inside a 2 x 4 x 3 box
            sage: PP = PlanePartitions([3,4,2])([[2,2,2,2],[2,2,2,2],[2,2,2,2]])
            sage: PP_rotated = PP.cyclically_rotate(preserve_parent=True)
            sage: PP_rotated in PP_rotated.parent()
            False
        """
    def bounding_box(self):
        """
        Return the smallest box `(a, b, c)` that ``self`` is contained in.

        EXAMPLES::

            sage: PP = PlanePartition([[5,2,1,1], [2,2], [2]])
            sage: PP.bounding_box()
            (3, 4, 5)
        """

PP: Incomplete

class PlanePartitions(UniqueRepresentation, Parent):
    """
    Plane partitions.

    ``PlanePartitions()`` returns the class of all plane partitions.

    ``PlanePartitions(n)`` return the class of all plane partitions with
    precisely `n` boxes.

    ``PlanePartitions([a, b, c])`` returns the class of plane partitions
    that fit inside an `a \\times b \\times c` box.

    ``PlanePartitions([a, b, c])`` has the optional keyword ``symmetry``, which
    restricts the plane partitions inside a box of the specified size satisfying
    certain symmetry conditions.

    - ``symmetry='SPP'`` gives the class of symmetric plane partitions. which
      is all plane partitions fixed under reflection across the diagonal.
      Requires that `a = b`.

    - ``symmetry='CSPP'`` gives the class of cyclic plane partitions, which
      is all plane partitions fixed under cyclic rotation of coordinates.
      Requires that `a = b = c`.

    - ``symmetry='TSPP'`` gives the class of totally symmetric plane partitions,
      which is all plane partitions fixed under any interchanging of coordinates.
      Requires that `a = b = c`.

    - ``symmetry='SCPP'`` gives the class of self-complementary plane partitions.
      which is all plane partitions that are equal to their own complement
      in the specified box. Requires at least one of `a,b,c` be even.

    - ``symmetry='TCPP'`` gives the class of transpose complement plane
      partitions, which is all plane partitions whose complement in the box
      of the specified size is equal to their transpose. Requires `a = b` and
      at least one of `a, b, c` be even.

    - ``symmetry='SSCPP'`` gives the class of symmetric self-complementary
      plane partitions, which is all plane partitions that are both
      symmetric and self-complementary. Requires `a = b` and at least one of
      `a, b, c` be even.

    - ``symmetry='CSTCPP'`` gives the class of cyclically symmetric transpose
      complement plane partitions, which is all plane partitions that are
      both symmetric and equal to the transpose of their complement. Requires
      `a = b = c`.

    - ``symmetry='CSSCPP'`` gives the class of cyclically symmetric
      self-complementary plane partitions, which is all plane partitions that
      are both cyclically symmetric and self-complementary. Requires `a = b = c`
      and all `a, b, c` be even.

    - ``symmetry='TSSCPP'`` gives the class of totally symmetric
      self-complementary plane partitions, which is all plane partitions that
      are totally symmetric and also self-complementary. Requires `a = b = c`
      and all `a, b, c` be even.

    EXAMPLES:

    If no arguments are passed, then the class of all plane partitions
    is returned::

        sage: PlanePartitions()
        Plane partitions
        sage: [[2,1],[1]] in PlanePartitions()
        True

    If an integer `n` is passed, then the class of plane partitions of `n`
    is returned::

        sage: PlanePartitions(3)
        Plane partitions of size 3
        sage: PlanePartitions(3).list()
        [Plane partition [[3]],
         Plane partition [[2, 1]],
         Plane partition [[1, 1, 1]],
         Plane partition [[2], [1]],
         Plane partition [[1, 1], [1]],
         Plane partition [[1], [1], [1]]]

    If a three-element tuple or list `[a,b,c]` is passed, then the class of all
    plane partitions that fit inside and `a \\times b \\times c` box is returned::

        sage: PlanePartitions([2,2,2])
        Plane partitions inside a 2 x 2 x 2 box
        sage: [[2,1],[1]] in PlanePartitions([2,2,2])
        True

    If an additional keyword ``symmetry`` is pass along with a three-element
    tuple or list `[a, b,c ]`, then the class of all plane partitions that fit
    inside an `a \\times b \\times c` box with the specified symmetry is returned::

        sage: PlanePartitions([2,2,2], symmetry='CSPP')
        Cyclically symmetric plane partitions inside a 2 x 2 x 2 box
        sage: [[2,1],[1]] in PlanePartitions([2,2,2], symmetry='CSPP')
        True

    .. SEEALSO::

        - :class:`PlanePartition`
        - :class:`PlanePartitions_all`
        - :class:`PlanePartitions_n`
        - :class:`PlanePartitions_box`
        - :class:`PlanePartitions_SPP`
        - :class:`PlanePartitions_CSPP`
        - :class:`PlanePartitions_TSPP`
        - :class:`PlanePartitions_SCPP`
        - :class:`PlanePartitions_TCPP`
        - :class:`PlanePartitions_SSCPP`
        - :class:`PlanePartitions_CSTCPP`
        - :class:`PlanePartitions_CSSCPP`
        - :class:`PlanePartitions_TSSCPP`
    """
    @staticmethod
    def __classcall_private__(cls, *args, **kwds):
        """
        Return the appropriate parent based on arguments.

        See the documentation for :class:`PlanePartitions` for more information.

        TESTS::

            sage: PlanePartitions()
            Plane partitions
            sage: PlanePartitions([3,3,3])
            Plane partitions inside a 3 x 3 x 3 box
            sage: PlanePartitions(3)
            Plane partitions of size 3
            sage: PlanePartitions([4,4,4], symmetry='TSSCPP')
            Totally symmetric self-complementary plane partitions inside a 4 x 4 x 4 box
            sage: PlanePartitions(4, symmetry='TSSCPP')
            Traceback (most recent call last):
            ...
            ValueError: the number of boxes may only be specified if no symmetry is required
        """
    def __init__(self, box_size=None, symmetry=None, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions(box_size=[2,2,1])
            sage: TestSuite(PP).run()                                                   # needs sage.modules
        """
    Element = PlanePartition
    def __contains__(self, pp) -> bool:
        """
        Check to see that ``pp`` is a valid plane partition.

        EXAMPLES::

            sage: [[3,2,1],[2,1]] in PlanePartitions()
            True
            sage: [[3,2,1],[1,2]] in PlanePartitions()
            False
            sage: [[3,2,1],[3,3]] in PlanePartitions()
            False
        """
    def box(self) -> tuple:
        """
        Return the size of the box of the plane partition of ``self``
        is contained in.

        EXAMPLES::

            sage: P = PlanePartitions([4,3,5])
            sage: P.box()
            (4, 3, 5)

            sage: PP = PlanePartitions()
            sage: PP.box() is None
            True
        """
    def symmetry(self) -> str:
        """
        Return the symmetry class of ``self``.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,2], symmetry='SPP')
            sage: PP.symmetry()
            'SPP'
            sage: PP = PlanePartitions()
            sage: PP.symmetry() is None
            True
        """

class PlanePartitions_all(PlanePartitions, DisjointUnionEnumeratedSets):
    """
    All plane partitions.
    """
    def __init__(self) -> None:
        """
        Initialize the class of all plane partitions.

        .. WARNING::

            Input is not checked; please use :class:`PlanePartitions` to
            ensure the options are properly parsed.

        TESTS::

            sage: from sage.combinat.plane_partition import PlanePartitions_all
            sage: P = PlanePartitions_all()
            sage: TestSuite(P).run()
        """
    def an_element(self):
        """
        Return a particular element of the class.

        TESTS::

            sage: P = PlanePartitions()
            sage: P.an_element()
            Plane partition [[2, 1], [1]]
        """

class PlanePartitions_box(PlanePartitions):
    """
    All plane partitions that fit inside a box of a specified size.

    By convention, a plane partition in an `a \\times b \\times c` box
    will have at most `a` rows, of lengths at most `b`, with entries
    at most `c`.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize the class of plane partitions that fit in a box of a
        specified size.

        EXAMPLES::

            sage: PP = PlanePartitions([4,3,2])
            sage: TestSuite(PP).run()           # long time                             # needs sage.modules
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2,1],[1]] in PlanePartitions([2,2,2])
            True
            sage: [[3,1],[1]] in PlanePartitions([2,2,2])
            False
            sage: [[2,1],[1],[1]] in PlanePartitions([2,2,2])
            False
            sage: [[2,1,1],[1]] in PlanePartitions([2,2,2])
            False
        """
    def to_poset(self):
        """
        Return the product of three chains poset, whose order ideals are
        naturally in bijection with plane partitions inside a box.

        EXAMPLES::

            sage: PlanePartitions([2,2,2]).to_poset()                                   # needs sage.graphs sage.modules
            Finite lattice containing 8 elements
        """
    def from_order_ideal(self, I) -> PP:
        """
        Return the plane partition corresponding to an order ideal in the
        poset given in :meth:`to_poset`.

        EXAMPLES::

            sage: I = [(1, 0, 0), (1, 0, 1), (1, 1, 0), (0, 1, 0),
            ....:      (0, 0, 0), (0, 0, 1), (0, 1, 1)]
            sage: PlanePartitions([2,2,2]).from_order_ideal(I)                          # needs sage.graphs sage.modules
            Plane partition [[2, 2], [2, 1]]
        """
    def from_antichain(self, A) -> PP:
        """
        Return the plane partition corresponding to an antichain in the poset
        given in :meth:`to_poset`.

        EXAMPLES::

            sage: A = [(1,0,1), (0,1,1), (1,1,0)]
            sage: PlanePartitions([2,2,2]).from_antichain(A)
            Plane partition [[2, 2], [2, 1]]
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all partitions that fit inside a box.

        EXAMPLES::

            sage: list(PlanePartitions([1,2,1]))                                        # needs sage.modules
            [Plane partition [], Plane partition [[1]], Plane partition [[1, 1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality()
            ....:     for b in cartesian_product([range(4)]*3)
            ....:     if (PP := PlanePartitions(b)))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of plane partitions inside an `a \\times b \\times c`
        box is equal to

        .. MATH::

            \\prod_{i=1}^{a} \\prod_{j=1}^{b} \\prod_{k=1}^{c}
            \\frac{i+j+k-1}{i+j+k-2}.

        EXAMPLES::

            sage: P = PlanePartitions([4,3,5])
            sage: P.cardinality()
            116424
        """
    def random_element(self) -> PP:
        """
        Return a uniformly random plane partition inside a box.

        ALGORITHM:

        This uses the
        :meth:`~sage.combinat.posets.posets.FinitePoset.random_order_ideal`
        method and the natural bijection with plane partitions.

        EXAMPLES::

            sage: P = PlanePartitions([4,3,5])
            sage: P.random_element()  # random                                          # needs sage.graphs sage.modules
            Plane partition [[4, 3, 3], [4], [2]]
        """

class PlanePartitions_n(PlanePartitions):
    """
    Plane partitions with a fixed number of boxes.
    """
    def __init__(self, n) -> None:
        """
        Initialize the class of plane partitions with ``n`` boxes.

        .. WARNING::

            Input is not checked; please use :class:`PlanePartitions` to
            ensure the options are properly parsed.

        TESTS::

            sage: PP = PlanePartitions(4)
            sage: type(PP)
            <class 'sage.combinat.plane_partition.PlanePartitions_n_with_category'>
            sage: TestSuite(PP).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2,1],[1]] in PlanePartitions(4)
            True
            sage: [[2,1],[1]] in PlanePartitions(3)
            False
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all plane partitions of a fixed size.

        EXAMPLES::

            sage: list(PlanePartitions(2))
            [Plane partition [[2]], Plane partition [[1, 1]], Plane partition [[1], [1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality() for n in range(9) if (PP := PlanePartitions(n)))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the number of plane partitions with ``n`` boxes.

        Calculated using the recurrence relation

        .. MATH::

            PL(n) = \\sum_{k=1}^n PL(n-k) \\sigma_2(k),

        where `\\sigma_k(n)` is the sum of the `k`-th powers of
        divisors of `n`.

        EXAMPLES::

            sage: P = PlanePartitions(17)
            sage: P.cardinality()
            18334
        """

class PlanePartitions_SPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    symmetric.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([3,3,2], symmetry='SPP')
            sage: TestSuite(PP).run()                                                   # needs sage.graphs sage.modules
            sage: PlanePartitions([4,3,2], symmetry='SPP')
            Traceback (most recent call last):
            ...
            ValueError: x and y dimensions (4 and 3) must be equal
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2,1],[1]] in PlanePartitions([2,2,2], symmetry='SPP')
            True
            sage: [[2,1],[1]] in PlanePartitions([1,1,1], symmetry='SPP')
            False
            sage: [[2,1],[2]] in PlanePartitions([2,2,2], symmetry='SPP')
            False
        """
    def to_poset(self):
        """
        Return a poset whose order ideals are in bijection with
        symmetric plane partitions.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,2], symmetry='SPP')
            sage: PP.to_poset()                                                         # needs sage.graphs
            Finite poset containing 12 elements
            sage: PP.to_poset().order_ideals_lattice().cardinality() == PP.cardinality()            # needs sage.graphs sage.modules sage.rings.finite_rings
            True
        """
    def from_order_ideal(self, I) -> PP:
        """
        Return the symmetric plane partition corresponding to an order ideal
        in the poset given in :meth:`to_poset()`.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,2], symmetry='SPP')
            sage: I = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 0, 0)]
            sage: PP.from_order_ideal(I)                                                # needs sage.graphs
            Plane partition [[1, 1, 1], [1, 1], [1]]
        """
    def from_antichain(self, A) -> PP:
        """
        Return the symmetric plane partition corresponding to an antichain
        in the poset given in :meth:`to_poset()`.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,2], symmetry='SPP')
            sage: A = [(2, 2, 0), (1, 0, 1), (1, 1, 0)]
            sage: PP.from_antichain(A)
            Plane partition [[2, 2, 1], [2, 1, 1], [1, 1, 1]]
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all symmetric plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([2,2,1], symmetry='SPP'))                        # needs sage.graphs sage.modules sage.rings.finite_rings
            [Plane partition [],
             Plane partition [[1, 1], [1, 1]],
             Plane partition [[1, 1], [1]],
             Plane partition [[1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality()                                  # needs sage.graphs sage.modules
            ....:     for a, b in cartesian_product([range(4)]*2)
            ....:     if (PP := PlanePartitions([a, a, b], symmetry='SPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of symmetric plane partitions inside an `a \\times a \\times b`
        box is equal to

        .. MATH::

            \\left(\\prod_{i=1}^{a} \\frac{2i + b - 1}{2i - 1}\\right)
            \\left(\\prod_{1 \\leq i < j \\leq a} \\frac{i+j+b-1}{i+j-1}\\right).

        EXAMPLES::

            sage: P = PlanePartitions([3,3,2], symmetry='SPP')
            sage: P.cardinality()
            35
        """
    def random_element(self) -> PP:
        """
        Return a uniformly random element of ``self``.

        ALGORITHM:

        This uses the
        :meth:`~sage.combinat.posets.posets.FinitePoset.random_order_ideal`
        method and the natural bijection between symmetric plane partitions
        and order ideals in an associated poset.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,2], symmetry='SPP')
            sage: PP.random_element()  # random                                         # needs sage.graphs
            Plane partition [[2, 2, 2], [2, 2], [2]]
        """

class PlanePartitions_CSPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    cyclically symmetric.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([3,3,3], symmetry='CSPP')
            sage: TestSuite(PP).run()                                                   # needs sage.graphs sage.modules sage.rings.finite_rings
            sage: PlanePartitions([4,3,2], symmetry='CSPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (4,3,2) must all be equal
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2,1],[1]] in PlanePartitions([2,2,2], symmetry='CSPP')
            True
            sage: [[2,1],[1]] in PlanePartitions([1,1,1], symmetry='CSPP')
            False
            sage: [[2,1],[2]] in PlanePartitions([2,2,2], symmetry='CSPP')
            False
        """
    def to_poset(self):
        """
        Return a partially ordered set whose order ideals are in bijection with
        cyclically symmetric plane partitions.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='CSPP')
            sage: PP.to_poset()                                                         # needs sage.graphs
            Finite poset containing 11 elements
            sage: PP.to_poset().order_ideals_lattice().cardinality() == PP.cardinality()            # needs sage.graphs
            True
        """
    def from_antichain(self, acl) -> PP:
        """
        Return the cyclically symmetric plane partition corresponding to an
        antichain in the poset given in :meth:`to_poset()`.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='CSPP')
            sage: A = [(0, 2, 2), (1, 1, 1)]
            sage: PP.from_antichain(A)
            Plane partition [[3, 3, 3], [3, 2, 1], [3, 1, 1]]
        """
    def from_order_ideal(self, I) -> PP:
        """
        Return the cyclically symmetric plane partition corresponding
        to an order ideal in the poset given in :meth:`to_poset`.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='CSPP')
            sage: I = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 1, 2),
            ....:      (1, 0, 2), (0, 2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 2)]
            sage: PP.from_order_ideal(I)                                                # needs sage.graphs
            Plane partition [[3, 3, 3], [3, 3, 3], [3, 3, 2]]
        """
    def random_element(self) -> PP:
        """
        Return a uniformly random element of ``self``.

        ALGORITHM:

        This uses the
        :meth:`~sage.combinat.posets.posets.FinitePoset.random_order_ideal`
        method and the natural bijection between cyclically symmetric plane
        partitions and order ideals in an associated poset.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='CSPP')
            sage: PP.random_element()  # random                                         # needs sage.graphs
            Plane partition [[3, 2, 2], [3, 1], [1, 1]]
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all cyclically symmetric plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([2,2,2], symmetry='CSPP'))                       # needs sage.graphs sage.modules
            [Plane partition [],
             Plane partition [[2, 2], [2, 2]],
             Plane partition [[2, 2], [2, 1]],
             Plane partition [[2, 1], [1]],
             Plane partition [[1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality() for n in range(5)                # needs sage.graphs sage.modules
            ....:     if (PP := PlanePartitions([n]*3, symmetry='CSPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of cyclically symmetric plane partitions inside an
        `a \\times a \\times a` box is equal to

        .. MATH::

            \\left(\\prod_{i=1}^{a} \\frac{3i - 1}{3i - 2}\\right)
            \\left(\\prod_{1 \\leq i < j \\leq a} \\frac{i+j+a-1}{2i+j-1}\\right).

        EXAMPLES::

            sage: P = PlanePartitions([4,4,4], symmetry='CSPP')
            sage: P.cardinality()
            132
        """

class PlanePartitions_TSPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    totally symmetric.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([3,3,3], symmetry='TSPP')
            sage: TestSuite(PP).run()                                                   # needs sage.graphs sage.modules
            sage: PlanePartitions([4,3,2], symmetry='TSPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (4,3,2) must all be equal
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2,1],[1]] in PlanePartitions([2,2,2], symmetry='TSPP')
            True
            sage: [[2,1],[1]] in PlanePartitions([1,1,1], symmetry='TSPP')
            False
            sage: [[2,1],[2]] in PlanePartitions([2,2,2], symmetry='TSPP')
            False
        """
    def to_poset(self):
        """
        Return a poset whose order ideals are in bijection with totally
        symmetric plane partitions.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='TSPP')
            sage: PP.to_poset()                                                         # needs sage.graphs
            Finite poset containing 10 elements
            sage: (PP.to_poset().order_ideals_lattice().cardinality()                   # needs sage.graphs sage.modules sage.rings.finite_rings
            ....:     == PP.cardinality())
            True
        """
    def from_antichain(self, acl) -> PP:
        """
        Return the totally symmetric plane partition corresponding to an
        antichain in the poset given in :meth:`to_poset()`.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='TSPP')
            sage: A = [(0, 0, 2), (0, 1, 1)]
            sage: PP.from_antichain(A)
            Plane partition [[3, 2, 1], [2, 1], [1]]
        """
    def from_order_ideal(self, I) -> PP:
        """
        Return the totally symmetric plane partition corresponding
        to an order ideal in the poset given in :meth:`to_poset`.

        EXAMPLES::

            sage: PP = PlanePartitions([3,3,3], symmetry='TSPP')
            sage: I = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1)]
            sage: PP.from_order_ideal(I)                                                # needs sage.graphs
            Plane partition [[3, 2, 1], [2, 1], [1]]
        """
    def __iter__(self) -> Iterator:
        """
        An iterator for totally symmetric plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([2,2,2], symmetry='TSPP'))                       # needs sage.graphs sage.modules
            [Plane partition [],
             Plane partition [[2, 2], [2, 2]],
             Plane partition [[2, 2], [2, 1]],
             Plane partition [[2, 1], [1]],
             Plane partition [[1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality() for n in range(5) if (PP := PlanePartitions([n]*3, symmetry='TSPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of totally symmetric plane partitions inside an
        `a \\times a \\times a` box is equal to

        .. MATH::

            \\prod_{1 \\leq i \\leq j \\leq a} \\frac{i+j+a-1}{i+2j-2}.

        EXAMPLES::

            sage: P = PlanePartitions([4,4,4], symmetry='TSPP')
            sage: P.cardinality()
            66
        """

class PlanePartitions_SCPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    self-complementary.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([4,3,2], symmetry='SCPP')
            sage: TestSuite(PP).run()
            sage: PlanePartitions([5,3,1], symmetry='SCPP')
            Traceback (most recent call last):
            ...
            ValueError: dimensions (5,3,1) cannot all be odd
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [[2,1],[1]] in PlanePartitions([2,2,2], symmetry='SCPP')
            True
            sage: [[2,1],[1]] in PlanePartitions([3,2,2], symmetry='SCPP')
            False
            sage: [[2,1],[1]] in PlanePartitions([2,1,1], symmetry='SCPP')
            False
            sage: [[2,1],[2]] in PlanePartitions([2,2,2], symmetry='SCPP')
            False
        """
    def __iter__(self) -> Iterator:
        """
        An iterator for self-complementary plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([3,2,2], symmetry='SCPP'))
            [Plane partition [[1, 1], [1, 1], [1, 1]],
             Plane partition [[2, 1], [1, 1], [1]],
             Plane partition [[2, 2], [1, 1]],
             Plane partition [[2], [2], [2]],
             Plane partition [[2, 1], [2], [1]],
             Plane partition [[2, 2], [2]]]

        TESTS::

            sage: PP = PlanePartitions([3,4,5], symmetry='SCPP')
            sage: len(set(PP)) == PP.cardinality()
            True

            sage: all(len(set(PP)) == PP.cardinality()
            ....:     for b in cartesian_product([range(4)]*3)
            ....:     if is_even(prod(b)) and (PP := PlanePartitions(b, symmetry='SCPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of self complementary plane partitions inside a
        `2a \\times 2b \\times 2c` box is equal to

        .. MATH::

            \\left(\\prod_{i=1}^{r}\\prod_{j=1}^{b}
            \\frac{i + j + c - 1}{i + j - 1}\\right)^2.

        The number of self complementary plane partitions inside an
        `(2a+1) \\times 2b \\times 2c` box is equal to

        .. MATH::

            \\left(\\prod_{i=1}^{a} \\prod_{j=1}^{b} \\frac{i+j+c-1}{i+j-1} \\right)
            \\left(\\prod_{i=1}^{a+1} \\prod_{j=1}^{b} \\frac{i+j+c-1}{i+j-1} \\right).

        The number of self complementary plane partitions inside an
        `(2a+1) \\times (2b+1) \\times 2c` box is equal to

        .. MATH::

            \\left(\\prod_{i=1}^{a+1} \\prod_{j=1}^{b} \\frac{i+j+c-1}{i+j-1} \\right)
            \\left(\\prod_{i=1}^{a} \\prod_{j=1}^{b+1} \\frac{i+j+c-1}{i+j-1} \\right).

        EXAMPLES::

            sage: P = PlanePartitions([4,4,4], symmetry='SCPP')
            sage: P.cardinality()
            400

            sage: P = PlanePartitions([5,4,4], symmetry='SCPP')
            sage: P.cardinality()
            1000
            sage: P = PlanePartitions([4,5,4], symmetry='SCPP')
            sage: P.cardinality()
            1000
            sage: P = PlanePartitions([4,4,5], symmetry='SCPP')
            sage: P.cardinality()
            1000

            sage: P = PlanePartitions([5,5,4], symmetry='SCPP')
            sage: P.cardinality()
            2500
            sage: P = PlanePartitions([5,4,5], symmetry='SCPP')
            sage: P.cardinality()
            2500
            sage: P = PlanePartitions([4,5,5], symmetry='SCPP')
            sage: P.cardinality()
            2500
        """

class PlanePartitions_TCPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    transpose-complement.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([3,3,2], symmetry='TCPP')
            sage: TestSuite(PP).run()                                                   # needs sage.graphs sage.modules

            sage: PlanePartitions([3,3,3], symmetry='TCPP')
            Traceback (most recent call last):
            ...
            ValueError: z dimension (3) must be even

            sage: PlanePartitions([4,3,2], symmetry='TCPP')
            Traceback (most recent call last):
            ...
            ValueError: x and y dimensions (4 and 3) must be equal
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all transpose complement plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([3,3,2], symmetry='TCPP'))                       # needs sage.modules
            [Plane partition [[2, 2, 1], [2, 1], [1]],
            Plane partition [[2, 1, 1], [2, 1, 1], [1]],
            Plane partition [[2, 2, 1], [1, 1], [1, 1]],
            Plane partition [[2, 1, 1], [1, 1, 1], [1, 1]],
            Plane partition [[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of transpose complement plane partitions inside an
        `a \\times a \\times 2b` box is equal to

        .. MATH::

            \\binom{b+1-1}{a-1} \\prod_{1\\leq i,j \\leq a-2}
            \\frac{i + j + 2b - 1}{i + j - 1}.

        EXAMPLES::

            sage: P = PlanePartitions([3,3,2], symmetry='TCPP')
            sage: P.cardinality()
            5
        """

class PlanePartitions_SSCPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    symmetric self-complementary.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([2, 2, 4], symmetry='SSCPP')
            sage: TestSuite(PP).run()                                                   # needs sage.modules

            sage: PP = PlanePartitions([4, 4, 2], symmetry='SSCPP')
            sage: TestSuite(PP).run()           # long time                             # needs sage.modules

            sage: PlanePartitions([4, 2, 2], symmetry='SSCPP')
            Traceback (most recent call last):
            ...
            ValueError: x and y dimensions (4 and 2) must be equal

            sage: PlanePartitions([4, 4, 3], symmetry='SSCPP')
            Traceback (most recent call last):
            ...
            ValueError: z dimension (3) must be even
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all symmetric self-complementary plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([4,4,2], symmetry='SSCPP'))                      # needs sage.modules
            [Plane partition [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
             Plane partition [[2, 2, 2, 1], [2, 1, 1], [2, 1, 1], [1]],
             Plane partition [[2, 2, 1, 1], [2, 2, 1, 1], [1, 1], [1, 1]],
             Plane partition [[2, 2, 2, 1], [2, 2, 1], [2, 1], [1]],
             Plane partition [[2, 2, 1, 1], [2, 1, 1, 1], [1, 1, 1], [1, 1]],
             Plane partition [[2, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality()
            ....:     for a, b in cartesian_product([range(5), range(0, 5, 2)])
            ....:     if (PP := PlanePartitions([a, a, b], symmetry='SSCPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of symmetric self-complementary plane partitions inside a
        `2a \\times 2a \\times 2b` box is equal to

        .. MATH::

            \\prod_{i=1}^a \\prod_{j=1}^a \\frac{i + j + b - 1}{i + j - 1}.

        The number of symmetric self-complementary plane partitions inside a
        `(2a+1) \\times (2a+1) \\times 2b` box is equal to

        .. MATH::

            \\prod_{i=1}^a \\prod_{j=1}^{a+1} \\frac{i + j + b - 1}{i + j - 1}.

        EXAMPLES::

            sage: P = PlanePartitions([4,4,2], symmetry='SSCPP')
            sage: P.cardinality()
            6
            sage: Q = PlanePartitions([3,3,2], symmetry='SSCPP')
            sage: Q.cardinality()
            3
        """

class PlanePartitions_CSTCPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    cyclically symmetric and transpose-complement.
    """
    def __init__(self, box_size) -> None:
        """
        TESTS::

            sage: PP = PlanePartitions([2,2,2], symmetry='CSTCPP')
            sage: TestSuite(PP).run()                                                   # needs sage.modules

            sage: PlanePartitions([4,3,2], symmetry='CSTCPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (4,3,2) must all be equal

            sage: PlanePartitions([3,3,3], symmetry='CSTCPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (3,3,3) must all be even
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all cyclically symmetry transpose complement plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([2,2,2], symmetry='CSTCPP'))                     # needs sage.modules
            [Plane partition [[2, 1], [1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality()
            ....:     for n in range(0, 5, 2)
            ....:     if (PP := PlanePartitions([n]*3, symmetry='CSTCPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of cyclically symmetric transpose complement plane partitions
        inside a `2a \\times 2a \\times 2a` box is equal to

        .. MATH::

            \\prod_{i=0}^{a-1} \\frac{(3i+1)(6i)!(2i)!}{(4i+1)!(4i)!}.

        EXAMPLES::

            sage: P = PlanePartitions([6,6,6], symmetry='CSTCPP')
            sage: P.cardinality()
            11
        """

class PlanePartitions_CSSCPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    cyclically symmetric self-complementary.
    """
    def __init__(self, box_size) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: PP = PlanePartitions([2,2,2], symmetry='CSSCPP')
            sage: TestSuite(PP).run()                                                   # needs sage.modules
            sage: PlanePartitions([4,3,2], symmetry='CSSCPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (4,3,2) must all be equal
            sage: PlanePartitions([3,3,3], symmetry='CSSCPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (3,3,3) must all be even
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all cyclically symmetric self-complementary plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([2,2,2], symmetry='CSSCPP'))                     # needs sage.modules
            [Plane partition [[2, 1], [1]]]
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of cyclically symmetric self-complementary plane partitions
        inside a `2a \\times 2a \\times 2a` box is equal to

        .. MATH::

            \\left( \\prod_{i=0}^{a-1} \\frac{(3i+1)!}{(a+i)!} \\right)^2.

        EXAMPLES::

            sage: P = PlanePartitions([6,6,6], symmetry='CSSCPP')
            sage: P.cardinality()
            49
        """

class PlanePartitions_TSSCPP(PlanePartitions):
    """
    Plane partitions that fit inside a box of a specified size that are
    totally symmetric self-complementary.
    """
    def __init__(self, box_size) -> None:
        """
        TESTS::

            sage: PP = PlanePartitions([4,4,4], symmetry='TSSCPP')
            sage: TestSuite(PP).run()                                                   # needs sage.modules
            sage: PlanePartitions([4,3,2], symmetry='TSSCPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (4,3,2) must all be equal
            sage: PlanePartitions([3,3,3], symmetry='TSSCPP')
            Traceback (most recent call last):
            ...
            ValueError: x, y, and z dimensions (3,3,3) must all be even
        """
    def to_poset(self):
        """
        Return a poset whose order ideals are in bijection with
        totally symmetric self-complementary plane partitions.

        EXAMPLES::

            sage: PP = PlanePartitions([6,6,6], symmetry='TSSCPP')
            sage: PP.to_poset()                                                         # needs sage.graphs sage.modules
            Finite poset containing 4 elements
            sage: PP.to_poset().order_ideals_lattice().cardinality() == PP.cardinality()            # needs sage.graphs sage.modules
            True
        """
    def from_antichain(self, acl) -> PP:
        """
        Return the totally symmetric self-complementary plane partition
        corresponding to an antichain in the poset given in :meth:`to_poset()`.

        EXAMPLES::

            sage: PP = PlanePartitions([6,6,6], symmetry='TSSCPP')
            sage: A = [(0, 0, 1), (1, 1, 0)]
            sage: PP.from_antichain(A)
            Plane partition [[6, 6, 6, 5, 5, 3], [6, 5, 5, 4, 3, 1], [6, 5, 4, 3, 2, 1],
                             [5, 4, 3, 2, 1], [5, 3, 2, 1, 1], [3, 1, 1]]
        """
    def from_order_ideal(self, I) -> PP:
        """
        Return the totally symmetric self-complementary plane partition
        corresponding to an order ideal in the poset given in :meth:`to_poset`.

        EXAMPLES::

            sage: PP = PlanePartitions([6,6,6], symmetry='TSSCPP')                      # needs sage.graphs
            sage: I = [(0, 0, 0), (0, 1, 0), (1, 1, 0)]
            sage: PP.from_order_ideal(I)                                                # needs sage.graphs
            Plane partition [[6, 6, 6, 5, 5, 3], [6, 5, 5, 3, 3, 1], [6, 5, 5, 3, 3, 1],
                             [5, 3, 3, 1, 1], [5, 3, 3, 1, 1], [3, 1, 1]]
        """
    def __iter__(self) -> Iterator:
        """
        Iterate over all totally symmetric self-complementary plane partitions.

        EXAMPLES::

            sage: list(PlanePartitions([4,4,4], symmetry='TSSCPP'))                     # needs sage.graphs sage.modules
            [Plane partition [[4, 4, 2, 2], [4, 4, 2, 2], [2, 2], [2, 2]],
             Plane partition [[4, 4, 3, 2], [4, 3, 2, 1], [3, 2, 1], [2, 1]]]

        TESTS::

            sage: all(len(set(PP)) == PP.cardinality() for n in range(0,11,2)           # needs sage.graphs sage.modules
            ....:     if (PP := PlanePartitions([n]*3, symmetry='TSSCPP')))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the cardinality of ``self``.

        The number of totally symmetric self-complementary plane partitions
        inside a `2a \\times 2a \\times 2a` box is equal to

        .. MATH::

            \\prod_{i=0}^{a-1} \\frac{(3i+1)!}{(a+i)!}.

        EXAMPLES::

            sage: P = PlanePartitions([6,6,6], symmetry='TSSCPP')
            sage: P.cardinality()
            7
        """
