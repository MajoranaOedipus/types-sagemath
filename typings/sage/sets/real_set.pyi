from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.categories.topological_spaces import TopologicalSpaces as TopologicalSpaces
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.infinity import infinity as infinity, minus_infinity as minus_infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_lazy import LazyFieldElement as LazyFieldElement, RLF as RLF
from sage.sets.set import Set_add_sub_operators as Set_add_sub_operators, Set_base as Set_base, Set_boolean_operators as Set_boolean_operators
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class InternalRealInterval(UniqueRepresentation, Parent):
    """
    A real interval.

    You are not supposed to create :class:`InternalRealInterval` objects
    yourself. Always use :class:`RealSet` instead.

    INPUT:

    - ``lower`` -- real or minus infinity; the lower bound of the interval

    - ``lower_closed`` -- boolean; whether the interval is closed at the lower
      bound

    - ``upper`` -- real or (plus) infinity; the upper bound of the interval

    - ``upper_closed`` -- boolean; whether the interval is closed at the upper
      bound

    - ``check`` -- boolean; whether to check the other arguments for validity
    """
    def __init__(self, lower, lower_closed, upper, upper_closed, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: RealSet([0, oo])
            Traceback (most recent call last):
            ...
            ValueError: interval cannot be closed at +oo
        """
    def is_empty(self):
        """
        Return whether the interval is empty.

        The normalized form of :class:`RealSet` has all intervals
        non-empty, so this method usually returns ``False``.

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet(0, 1)[0]
            sage: I.is_empty()
            False
        """
    def is_point(self):
        """
        Return whether the interval consists of a single point.

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet(0, 1)[0]
            sage: I.is_point()
            False
        """
    def lower(self):
        """
        Return the lower bound.

        OUTPUT: the lower bound as it was originally specified

        EXAMPLES::

            sage: I = RealSet(0, 1)[0]
            sage: I.lower()
            0
            sage: I.upper()
            1
        """
    def upper(self):
        """
        Return the upper bound.

        OUTPUT: the upper bound as it was originally specified

        EXAMPLES::

            sage: I = RealSet(0, 1)[0]
            sage: I.lower()
            0
            sage: I.upper()
            1
        """
    def lower_closed(self):
        """
        Return whether the interval is open at the lower bound.

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet.open_closed(0, 1)[0];  I
            (0, 1]
            sage: I.lower_closed()
            False
            sage: I.lower_open()
            True
            sage: I.upper_closed()
            True
            sage: I.upper_open()
            False
        """
    def upper_closed(self):
        """
        Return whether the interval is closed at the lower bound.

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet.open_closed(0, 1)[0];  I
            (0, 1]
            sage: I.lower_closed()
            False
            sage: I.lower_open()
            True
            sage: I.upper_closed()
            True
            sage: I.upper_open()
            False
        """
    def lower_open(self):
        """
        Return whether the interval is closed at the upper bound.

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet.open_closed(0, 1)[0];  I
            (0, 1]
            sage: I.lower_closed()
            False
            sage: I.lower_open()
            True
            sage: I.upper_closed()
            True
            sage: I.upper_open()
            False
        """
    def upper_open(self):
        """
        Return whether the interval is closed at the upper bound.

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet.open_closed(0, 1)[0];  I
            (0, 1]
            sage: I.lower_closed()
            False
            sage: I.lower_open()
            True
            sage: I.upper_closed()
            True
            sage: I.upper_open()
            False
        """
    def __richcmp__(self, other, op):
        """
        Intervals are sorted by lower bound, then upper bound.

        OUTPUT: `-1`, `0`, or `+1` depending on how the intervals compare

        EXAMPLES::

            sage: I1 = RealSet.open_closed(1, 3)[0];  I1
            (1, 3]
            sage: I2 = RealSet.open_closed(0, 5)[0];  I2
            (0, 5]
            sage: I1 > I2
            True
            sage: sorted([I1, I2])
            [(0, 5], (1, 3]]

        TESTS:

        Check if a bug in sorting is fixed (:issue:`17714`)::

            sage: RealSet((0, 1),[1, 1],(1, 2))
            (0, 2)
        """
    element_class = LazyFieldElement
    def closure(self):
        """
        Return the closure.

        OUTPUT: the closure as a new :class:`InternalRealInterval`

        EXAMPLES::

            sage: RealSet.open(0,1)[0].closure()
            [0, 1]
            sage: RealSet.open(-oo,1)[0].closure()
            (-oo, 1]
            sage: RealSet.open(0, oo)[0].closure()
            [0, +oo)
        """
    def interior(self):
        """
        Return the interior.

        OUTPUT: the interior as a new :class:`InternalRealInterval`

        EXAMPLES::

            sage: RealSet.closed(0, 1)[0].interior()
            (0, 1)
            sage: RealSet.open_closed(-oo, 1)[0].interior()
            (-oo, 1)
            sage: RealSet.closed_open(0, oo)[0].interior()
            (0, +oo)
        """
    def boundary_points(self) -> Generator[Incomplete]:
        """
        Generate the boundary points of ``self``.

        EXAMPLES::

            sage: list(RealSet.open_closed(-oo, 1)[0].boundary_points())
            [1]
            sage: list(RealSet.open(1, 2)[0].boundary_points())
            [1, 2]
        """
    def is_connected(self, other):
        """
        Test whether two intervals are connected.

        OUTPUT:

        boolean; whether the set-theoretic union of the two intervals
        has a single connected component.

        EXAMPLES::

            sage: I1 = RealSet.open(0, 1)[0];  I1
            (0, 1)
            sage: I2 = RealSet.closed(1, 2)[0];  I2
            [1, 2]
            sage: I1.is_connected(I2)
            True
            sage: I1.is_connected(I2.interior())
            False
            sage: I1.closure().is_connected(I2.interior())
            True
            sage: I2.is_connected(I1)
            True
            sage: I2.interior().is_connected(I1)
            False
            sage: I2.closure().is_connected(I1.interior())
            True
            sage: I3 = RealSet.closed(1/2, 3/2)[0]; I3
            [1/2, 3/2]
            sage: I1.is_connected(I3)
            True
            sage: I3.is_connected(I1)
            True
        """
    def convex_hull(self, other):
        """
        Return the convex hull of the two intervals.

        OUTPUT: the convex hull as a new :class:`InternalRealInterval`

        EXAMPLES::

            sage: I1 = RealSet.open(0, 1)[0];  I1
            (0, 1)
            sage: I2 = RealSet.closed(1, 2)[0];  I2
            [1, 2]
            sage: I1.convex_hull(I2)
            (0, 2]
            sage: I2.convex_hull(I1)
            (0, 2]
            sage: I1.convex_hull(I2.interior())
            (0, 2)
            sage: I1.closure().convex_hull(I2.interior())
            [0, 2)
            sage: I1.closure().convex_hull(I2)
            [0, 2]
            sage: I3 = RealSet.closed(1/2, 3/2)[0]; I3
            [1/2, 3/2]
            sage: I1.convex_hull(I3)
            (0, 3/2]
        """
    def intersection(self, other):
        """
        Return the intersection of the two intervals.

        INPUT:

        - ``other`` -- a :class:`InternalRealInterval`

        OUTPUT: the intersection as a new :class:`InternalRealInterval`

        EXAMPLES::

            sage: I1 = RealSet.open(0, 2)[0];  I1
            (0, 2)
            sage: I2 = RealSet.closed(1, 3)[0];  I2
            [1, 3]
            sage: I1.intersection(I2)
            [1, 2)
            sage: I2.intersection(I1)
            [1, 2)
            sage: I1.closure().intersection(I2.interior())
            (1, 2]
            sage: I2.interior().intersection(I1.closure())
            (1, 2]

            sage: I3 = RealSet.closed(10, 11)[0];  I3
            [10, 11]
            sage: I1.intersection(I3)
            (0, 0)
            sage: I3.intersection(I1)
            (0, 0)
        """
    def contains(self, x):
        """
        Return whether `x` is contained in the interval.

        INPUT:

        - ``x`` -- a real number

        OUTPUT: boolean

        EXAMPLES::

            sage: i = RealSet.open_closed(0,2)[0]; i
            (0, 2]
            sage: i.contains(0)
            False
            sage: i.contains(1)
            True
            sage: i.contains(2)
            True
        """
    def __mul__(self, right):
        """
        Scale an interval by a scalar on the left or right.

        If scaled with a negative number, the interval is flipped.

        EXAMPLES::

            sage: i = RealSet.open_closed(0,2)[0]; i
            (0, 2]
            sage: 2 * i
            (0, 4]
            sage: 0 * i
            {0}
            sage: (-2) * i
            [-4, 0)
            sage: i * (-3)
            [-6, 0)
            sage: i * 0
            {0}
            sage: i * 1
            (0, 2]

        TESTS::

            sage: from sage.sets.real_set import InternalRealInterval
            sage: i = InternalRealInterval(RLF(0), False, RLF(0), False)
            sage: (0 * i).is_empty()
            True
        """
    def __rmul__(self, other):
        """
        Scale an interval by a scalar on the left.

        If scaled with a negative number, the interval is flipped.

        EXAMPLES::

            sage: i = RealSet.open_closed(0,2)[0]; i
            (0, 2]
            sage: 2 * i
            (0, 4]
            sage: 0 * i
            {0}
            sage: (-2) * i
            [-4, 0)
        """

class RealSet(UniqueRepresentation, Parent, Set_base, Set_boolean_operators, Set_add_sub_operators):
    """
    A subset of the real line, a finite union of intervals.

    INPUT:

    - ``*args`` -- arguments defining a real set. Possibilities are either:

      - two extended real numbers ``a, b``, to construct the open interval `(a, b)`, or
      - a list/tuple/iterable of (not necessarily disjoint) intervals or real sets,
        whose union is taken. The individual intervals can be specified by either

        - a tuple ``(a, b)`` of two extended real numbers (constructing an open interval),
        - a list ``[a, b]`` of two real numbers (constructing a closed interval),
        - an :class:`InternalRealInterval`,
        - an :class:`~sage.manifolds.differentiable.examples.real_line.OpenInterval`.

    - ``structure`` -- (default: ``None``) if ``None``, construct the real set as an
      instance of :class:`RealSet`; if ``'differentiable'``, construct it as a subset of
      an instance of :class:`~sage.manifolds.differentiable.examples.real_line.RealLine`,
      representing the differentiable manifold `\\RR`.
    - ``ambient`` -- (default: ``None``) an instance of
      :class:`~sage.manifolds.differentiable.examples.real_line.RealLine`; construct
      a subset of it. Using this keyword implies ``structure='differentiable'``.
    - ``names`` or ``coordinate`` -- coordinate symbol for the canonical chart; see
      :class:`~sage.manifolds.differentiable.examples.real_line.RealLine`.  Using these
      keywords implies ``structure='differentiable'``.
    - ``name``, ``latex_name``, ``start_index`` -- see
      :class:`~sage.manifolds.differentiable.examples.real_line.RealLine`
    - ``normalized`` -- (default: ``None``) if ``True``, the input is already normalized,
      i.e., ``*args`` are the connected components (type :class:`InternalRealInterval`)
      of the real set in ascending order; no other keyword is provided.

    There are also specialized constructors for various types of intervals:

    ======================================   ====================
    Constructor                              Interval
    ======================================   ====================
    :meth:`RealSet.open`                     `(a, b)`
    :meth:`RealSet.closed`                   `[a, b]`
    :meth:`RealSet.point`                    `\\{a\\}`
    :meth:`RealSet.open_closed`              `(a, b]`
    :meth:`RealSet.closed_open`              `[a, b)`
    :meth:`RealSet.unbounded_below_closed`   `(-\\infty, b]`
    :meth:`RealSet.unbounded_below_open`     `(-\\infty, b)`
    :meth:`RealSet.unbounded_above_closed`   `[a, +\\infty)`
    :meth:`RealSet.unbounded_above_open`     `(a, +\\infty)`
    :meth:`RealSet.real_line`                `(-\\infty, +\\infty)`
    :meth:`RealSet.interval`                 any
    ======================================   ====================

    EXAMPLES::

        sage: RealSet(0, 1)    # open set from two numbers
        (0, 1)
        sage: RealSet(1, 0)    # the two numbers will be sorted
        (0, 1)
        sage: s1 = RealSet((1,2)); s1    # tuple of two numbers = open set
        (1, 2)
        sage: s2 = RealSet([3,4]); s2    # list of two numbers = closed set
        [3, 4]
        sage: i1, i2 = s1[0], s2[0]
        sage: RealSet(i2, i1)            # union of intervals
        (1, 2) ∪ [3, 4]
        sage: RealSet((-oo, 0), x > 6, i1, RealSet.point(5),                            # needs sage.symbolic
        ....:         RealSet.closed_open(4, 3))
        (-oo, 0) ∪ (1, 2) ∪ [3, 4) ∪ {5} ∪ (6, +oo)

    Initialization from manifold objects::

        sage: # needs sage.symbolic
        sage: R = manifolds.RealLine(); R
        Real number line ℝ
        sage: RealSet(R)
        (-oo, +oo)
        sage: I02 = manifolds.OpenInterval(0, 2); I
        I
        sage: RealSet(I02)
        (0, 2)
        sage: I01_of_R = manifolds.OpenInterval(0, 1, ambient_interval=R); I01_of_R
        Real interval (0, 1)
        sage: RealSet(I01_of_R)
        (0, 1)
        sage: RealSet(I01_of_R.closure())
        [0, 1]
        sage: I01_of_I02 = manifolds.OpenInterval(0, 1,
        ....:                                     ambient_interval=I02); I01_of_I02
        Real interval (0, 1)
        sage: RealSet(I01_of_I02)
        (0, 1)
        sage: RealSet(I01_of_I02.closure())
        (0, 1]

    Real sets belong to a subcategory of topological spaces::

        sage: RealSet().category()
        Join of
         Category of finite sets and
         Category of subobjects of sets and
         Category of connected topological spaces
        sage: RealSet.point(1).category()
        Join of
         Category of finite sets and
         Category of subobjects of sets and
         Category of connected topological spaces
        sage: RealSet([1, 2]).category()
        Join of
         Category of infinite sets and
         Category of compact topological spaces and
         Category of subobjects of sets and
         Category of connected topological spaces
        sage: RealSet((1, 2), (3, 4)).category()
        Join of
         Category of infinite sets and
         Category of subobjects of sets and
         Category of topological spaces

    Constructing real sets as manifolds or manifold subsets by passing
    ``structure='differentiable'``::

        sage: # needs sage.symbolic
        sage: RealSet(-oo, oo, structure='differentiable')
        Real number line ℝ
        sage: RealSet([0, 1], structure='differentiable')
        Subset [0, 1] of the Real number line ℝ
        sage: _.category()
        Category of subobjects of sets
        sage: RealSet.open_closed(0, 5, structure='differentiable')
        Subset (0, 5] of the Real number line ℝ

    This is implied when a coordinate name is given using the keywords ``coordinate``
    or ``names``::

        sage: RealSet(0, 1, coordinate='λ')                                             # needs sage.symbolic
        Open subset (0, 1) of the Real number line ℝ
        sage: _.category()                                                              # needs sage.symbolic
        Join of
         Category of smooth manifolds over Real Field with 53 bits of precision and
         Category of connected manifolds over Real Field with 53 bits of precision and
         Category of subobjects of sets

    It is also implied by assigning a coordinate name using generator notation::

        sage: R_xi.<ξ> = RealSet.real_line(); R_xi                                      # needs sage.symbolic
        Real number line ℝ
        sage: R_xi.canonical_chart()                                                    # needs sage.symbolic
        Chart (ℝ, (ξ,))

    With the keyword ``ambient``, we can construct a subset of a previously
    constructed manifold::

        sage: # needs sage.symbolic
        sage: P_xi = RealSet(0, oo, ambient=R_xi); P_xi
        Open subset (0, +oo) of the Real number line ℝ
        sage: P_xi.default_chart()
        Chart ((0, +oo), (ξ,))
        sage: B_xi = RealSet(0, 1, ambient=P_xi); B_xi
        Open subset (0, 1) of the Real number line ℝ
        sage: B_xi.default_chart()
        Chart ((0, 1), (ξ,))
        sage: R_xi.subset_family()
        Set {(0, +oo), (0, 1), ℝ} of open subsets of the Real number line ℝ
        sage: F = RealSet.point(0).union(RealSet.point(1)).union(RealSet.point(2)); F
        {0} ∪ {1} ∪ {2}
        sage: F_tau = RealSet(F, names='τ'); F_tau
        Subset {0} ∪ {1} ∪ {2} of the Real number line ℝ
        sage: F_tau.manifold().canonical_chart()
        Chart (ℝ, (τ,))

    TESTS::

        sage: # needs sage.symbolic
        sage: TestSuite(R_xi).run()
        sage: TestSuite(P_xi).run()
        sage: R_xi.point((1,)) in P_xi
        True
        sage: R_xi.point((-1,)) in P_xi
        False
        sage: TestSuite(B_xi).run()
        sage: p = B_xi.an_element(); p
        Point on the Real number line ℝ
        sage: p.coordinates()
        (1/2,)
    """
    @staticmethod
    def __classcall__(cls, *args, **kwds):
        """
        Normalize the input.

        INPUT:

        See :class:`RealSet`.

        OUTPUT: a :class:`RealSet`

        EXAMPLES::

            sage: R = RealSet(RealSet.open_closed(0,1), RealSet.closed_open(2,3)); R
            (0, 1] ∪ [2, 3)

        TESTS::

            sage: # needs sage.symbolic
            sage: RealSet(x != 0)
            (-oo, 0) ∪ (0, +oo)
            sage: RealSet(x == pi)
            {pi}
            sage: RealSet(x < 1/2)
            (-oo, 1/2)
            sage: RealSet(1/2 < x)
            (1/2, +oo)
            sage: RealSet(1.5 <= x)
            [1.50000000000000, +oo)
            sage: RealSet(x >= -1)
            [-1, +oo)
            sage: RealSet(x > oo)
            {}
            sage: RealSet(x >= oo)
            {}
            sage: RealSet(x <= -oo)
            {}
            sage: RealSet(x < oo)
            (-oo, +oo)
            sage: RealSet(x > -oo)
            (-oo, +oo)
            sage: RealSet(x != oo)
            (-oo, +oo)
            sage: RealSet(x <= oo)
            Traceback (most recent call last):
            ...
            ValueError: interval cannot be closed at +oo
            sage: RealSet(x == oo)
            Traceback (most recent call last):
            ...
            ValueError: interval cannot be closed at +oo
            sage: RealSet(x >= -oo)
            Traceback (most recent call last):
            ...
            ValueError: interval cannot be closed at -oo
            sage: r = RealSet(2,10)
            sage: RealSet((2, 6), (4, 10)) is r
            True
            sage: RealSet(x > 2).intersection(RealSet(x < 10)) is RealSet(r[0], normalized=True)
            True
            sage: RealSet(x > 0, normalized=True)
            Traceback (most recent call last):
            ...
            AttributeError: ...
        """
    def __init__(self, *intervals, normalized: bool = True) -> None:
        """
        TESTS::

            sage: Empty = RealSet(); Empty
            {}
            sage: TestSuite(Empty).run()
            sage: I1 = RealSet.open_closed(1, 3);  I1
            (1, 3]
            sage: TestSuite(I1).run()
            sage: R = RealSet(RealSet.open_closed(0,1), RealSet.closed_open(2,3)); R
            (0, 1] ∪ [2, 3)
            sage: TestSuite(R).run()
        """
    def __richcmp__(self, other, op):
        """
        Intervals are sorted by lower bound, then upper bound.

        OUTPUT: `-1`, `0`, or `+1` depending on how the intervals compare

        EXAMPLES::

             sage: I1 = RealSet.open_closed(1, 3);  I1
             (1, 3]
             sage: I2 = RealSet.open_closed(0, 5);  I2
             (0, 5]
             sage: I1 > I2
             True
             sage: sorted([I1, I2])
             [(0, 5], (1, 3]]
             sage: I1 == I1
             True
        """
    def __iter__(self):
        """
        Iterate over the component intervals is ascending order.

        OUTPUT: an iterator over the intervals

        EXAMPLES::

            sage: s = RealSet(RealSet.open_closed(0,1), RealSet.closed_open(2,3))
            sage: i = iter(s)
            sage: next(i)
            (0, 1]
            sage: next(i)
            [2, 3)
        """
    def n_components(self):
        """
        Return the number of connected components.

        See also :meth:`get_interval`.

        EXAMPLES::

            sage: s = RealSet(RealSet.open_closed(0,1), RealSet.closed_open(2,3))
            sage: s.n_components()
            2
        """
    def cardinality(self):
        """
        Return the cardinality of the subset of the real line.

        OUTPUT:

        Integer or infinity; the size of a discrete set is the number
        of points; the size of a real interval is Infinity.

        EXAMPLES::

           sage: RealSet([0, 0], [1, 1], [3, 3]).cardinality()
           3
           sage: RealSet(0,3).cardinality()
           +Infinity
        """
    def is_empty(self):
        """
        Return whether the set is empty.

        EXAMPLES::

            sage: RealSet(0, 1).is_empty()
            False
            sage: RealSet(0, 0).is_empty()
            True
            sage: RealSet.interval(1, 1, lower_closed=False, upper_closed=True).is_empty()
            True
            sage: RealSet.interval(1, -1, lower_closed=False, upper_closed=True).is_empty()
            False
        """
    def is_universe(self):
        """
        Return whether the set is the ambient space (the real line).

        EXAMPLES::

            sage: RealSet().ambient().is_universe()
            True
        """
    def get_interval(self, i):
        """
        Return the ``i``-th connected component.

        Note that the intervals representing the real set are always
        normalized, i.e., they are sorted, disjoint and not connected.

        INPUT:

        - ``i`` -- integer

        OUTPUT: the `i`-th connected component as a :class:`InternalRealInterval`

        EXAMPLES::

            sage: s = RealSet(RealSet.open_closed(0,1), RealSet.closed_open(2,3))
            sage: s.get_interval(0)
            (0, 1]
            sage: s[0]    # shorthand
            (0, 1]
            sage: s.get_interval(1)
            [2, 3)
            sage: s[0] == s.get_interval(0)
            True
        """
    __getitem__ = get_interval
    def __bool__(self) -> bool:
        """
        A set is considered ``True`` unless it is empty, in which case it is
        considered to be ``False``.

        EXAMPLES::

            sage: bool(RealSet(0, 1))
            True
            sage: bool(RealSet())
            False
        """
    def ambient(self):
        """
        Return the ambient space (the real line).

        EXAMPLES::

            sage: s = RealSet(RealSet.open_closed(0,1), RealSet.closed_open(2,3))
            sage: s.ambient()
            (-oo, +oo)
        """
    def lift(self, x):
        """
        Lift ``x`` to the ambient space for ``self``.

        This version of the method just returns ``x``.

        EXAMPLES::

            sage: s = RealSet(0, 2); s
            (0, 2)
            sage: s.lift(1)
            1
        """
    def retract(self, x):
        """
        Retract ``x`` to ``self``.

        It raises an error if ``x`` does not lie in the set ``self``.

        EXAMPLES::

            sage: s = RealSet(0, 2); s
            (0, 2)
            sage: s.retract(1)
            1
            sage: s.retract(2)
            Traceback (most recent call last):
            ...
            ValueError: 2 is not an element of (0, 2)
        """
    def normalize(intervals):
        """
        Bring a collection of intervals into canonical form.

        INPUT:

        - ``intervals`` -- list/tuple/iterable of intervals

        OUTPUT: a tuple of intervals such that

        * they are sorted in ascending order (by lower bound)

        * there is a gap between each interval

        * all intervals are non-empty

        EXAMPLES::

            sage: i1 = RealSet((0, 1))[0]
            sage: i2 = RealSet([1, 2])[0]
            sage: i3 = RealSet((2, 3))[0]
            sage: RealSet.normalize([i1, i2, i3])
            ((0, 3),)
        """
    @staticmethod
    def interval(lower, upper, *, lower_closed=None, upper_closed=None, **kwds):
        """
        Construct an interval.

        INPUT:

        - ``lower``, ``upper`` -- two real numbers or infinity; they
          will be sorted if necessary

        - ``lower_closed``, ``upper_closed`` -- boolean; whether the interval
          is closed at the lower and upper bound of the interval, respectively

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT: a new :class:`RealSet`

        EXAMPLES::

            sage: RealSet.interval(1, 0, lower_closed=True, upper_closed=False)
            [0, 1)
        """
    @staticmethod
    def open(lower, upper, **kwds):
        """
        Construct an open interval.

        INPUT:

        - ``lower``, ``upper`` -- two real numbers or infinity; they
          will be sorted if necessary

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT: a new :class:`RealSet`

        EXAMPLES::

            sage: RealSet.open(1, 0)
            (0, 1)
        """
    @staticmethod
    def closed(lower, upper, **kwds):
        """
        Construct a closed interval.

        INPUT:

        - ``lower``, ``upper`` -- two real numbers or infinity; they
          will be sorted if necessary

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT: a new :class:`RealSet`

        EXAMPLES::

            sage: RealSet.closed(1, 0)
            [0, 1]
        """
    @staticmethod
    def point(p, **kwds):
        """
        Construct an interval containing a single point.

        INPUT:

        - ``p`` -- a real number

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT: a new :class:`RealSet`

        EXAMPLES::

            sage: RealSet.open(1, 0)
            (0, 1)
        """
    @staticmethod
    def open_closed(lower, upper, **kwds):
        """
        Construct a half-open interval.

        INPUT:

        - ``lower``, ``upper`` -- two real numbers or infinity; they
          will be sorted if necessary

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT:

        A new :class:`RealSet` that is open at the lower bound and
        closed at the upper bound.

        EXAMPLES::

            sage: RealSet.open_closed(1, 0)
            (0, 1]
        """
    @staticmethod
    def closed_open(lower, upper, **kwds):
        """
        Construct a half-open interval.

        INPUT:

        - ``lower``, ``upper`` -- two real numbers or infinity; they
          will be sorted if necessary

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT:

        A new :class:`RealSet` that is closed at the lower bound and
        open at the upper bound.

        EXAMPLES::

            sage: RealSet.closed_open(1, 0)
            [0, 1)
        """
    @staticmethod
    def unbounded_below_closed(bound, **kwds):
        """
        Construct a semi-infinite interval.

        INPUT:

        - ``bound`` -- a real number

        OUTPUT:

        A new :class:`RealSet` from minus infinity to the bound (including).

        - ``**kwds`` -- see :class:`RealSet`

        EXAMPLES::

            sage: RealSet.unbounded_below_closed(1)
            (-oo, 1]
        """
    @staticmethod
    def unbounded_below_open(bound, **kwds):
        """
        Construct a semi-infinite interval.

        INPUT:

        - ``bound`` -- a real number

        OUTPUT:

        A new :class:`RealSet` from minus infinity to the bound (excluding).

        - ``**kwds`` -- see :class:`RealSet`

        EXAMPLES::

            sage: RealSet.unbounded_below_open(1)
            (-oo, 1)
        """
    @staticmethod
    def unbounded_above_closed(bound, **kwds):
        """
        Construct a semi-infinite interval.

        INPUT:

        - ``bound`` -- a real number

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT:

        A new :class:`RealSet` from the bound (including) to plus
        infinity.

        EXAMPLES::

            sage: RealSet.unbounded_above_closed(1)
            [1, +oo)
        """
    @staticmethod
    def unbounded_above_open(bound, **kwds):
        """
        Construct a semi-infinite interval.

        INPUT:

        - ``bound`` -- a real number

        - ``**kwds`` -- see :class:`RealSet`

        OUTPUT:

        A new :class:`RealSet` from the bound (excluding) to plus
        infinity.

        EXAMPLES::

            sage: RealSet.unbounded_above_open(1)
            (1, +oo)
        """
    @staticmethod
    def real_line(**kwds):
        """
        Construct the real line.

        INPUT:

        - ``**kwds`` -- see :class:`RealSet`

        EXAMPLES::

            sage: RealSet.real_line()
            (-oo, +oo)
        """
    def union(self, *real_set_collection):
        """
        Return the union of real sets.

        INPUT:

        - ``*real_set_collection`` -- list/tuple/iterable of :class:`RealSet`
          or data that defines one

        OUTPUT: the set-theoretic union as a new :class:`RealSet`

        EXAMPLES::

            sage: s1 = RealSet(0,2)
            sage: s2 = RealSet(1,3)
            sage: s1.union(s2)
            (0, 3)
            sage: s1.union(1,3)
            (0, 3)
            sage: s1 | s2    # syntactic sugar
            (0, 3)
            sage: s1 + s2    # syntactic sugar
            (0, 3)
            sage: RealSet().union(RealSet.real_line())
            (-oo, +oo)
            sage: s = RealSet().union([1, 2], (2, 3)); s
            [1, 3)
            sage: RealSet().union((-oo, 0), x > 6, s[0],                                # needs sage.symbolic
            ....:                 RealSet.point(5.0), RealSet.closed_open(2, 4))
            (-oo, 0) ∪ [1, 4) ∪ {5} ∪ (6, +oo)
        """
    def intersection(self, *real_set_collection):
        """
        Return the intersection of real sets.

        INPUT:

        - ``*real_set_collection`` -- list/tuple/iterable of :class:`RealSet`
          or data that defines one

        OUTPUT: the set-theoretic intersection as a new :class:`RealSet`

        EXAMPLES::

            sage: s1 = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s1
            (0, 2) ∪ [10, +oo)
            sage: s2 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s2
            (-oo, -10] ∪ (1, 3)
            sage: s1.intersection(s2)
            (1, 2)
            sage: s1 & s2    # syntactic sugar
            (1, 2)
            sage: s3 = RealSet((0, 1), (2, 3));  s3
            (0, 1) ∪ (2, 3)
            sage: s4 = RealSet([0, 1], [2, 3]);  s4
            [0, 1] ∪ [2, 3]
            sage: s3.intersection(s4)
            (0, 1) ∪ (2, 3)
            sage: s3.intersection([1, 2])
            {}
            sage: s4.intersection([1, 2])
            {1} ∪ {2}
            sage: s4.intersection(1, 2)
            {}
            sage: s5 = RealSet.closed_open(1, 10);  s5
            [1, 10)
            sage: s5.intersection(-oo, +oo)
            [1, 10)
            sage: s5.intersection(x != 2, (-oo, 3), RealSet.real_line()[0])             # needs sage.symbolic
            [1, 2) ∪ (2, 3)

        TESTS::

            sage: s1 = RealSet([1, 2])
            sage: s2 = RealSet([2, 3])
            sage: s3 = RealSet(3, 4)
            sage: s4 = RealSet.closed_open(4, 5)
            sage: s5 = RealSet(5, 6)
            sage: s1.intersection(RealSet())
            {}
            sage: s1.intersection(s2)
            {2}
            sage: s2.intersection(s3)
            {}
            sage: s3.intersection(s4)
            {}
            sage: s4.intersection(s5)
            {}
        """
    def inf(self):
        """
        Return the infimum.

        OUTPUT: a real number or infinity

        EXAMPLES::

            sage: s1 = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s1
            (0, 2) ∪ [10, +oo)
            sage: s1.inf()
            0

            sage: s2 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s2
            (-oo, -10] ∪ (1, 3)
            sage: s2.inf()
            -Infinity
        """
    def sup(self):
        """
        Return the supremum.

        OUTPUT: a real number or infinity

        EXAMPLES::

            sage: s1 = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s1
            (0, 2) ∪ [10, +oo)
            sage: s1.sup()
            +Infinity

            sage: s2 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s2
            (-oo, -10] ∪ (1, 3)
            sage: s2.sup()
            3
        """
    def complement(self):
        """
        Return the complement.

        OUTPUT: the set-theoretic complement as a new :class:`RealSet`

        EXAMPLES::

            sage: RealSet(0,1).complement()
            (-oo, 0] ∪ [1, +oo)

            sage: s1 = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s1
            (0, 2) ∪ [10, +oo)
            sage: s1.complement()
            (-oo, 0] ∪ [2, 10)

            sage: s2 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s2
            (-oo, -10] ∪ (1, 3)
            sage: s2.complement()
            (-10, 1] ∪ [3, +oo)

        TESTS::

            sage: RealSet(x != 0).complement()                                          # needs sage.symbolic
            {0}
            sage: RealSet.real_line().complement()
            {}
            sage: _.complement()
            (-oo, +oo)
        """
    def difference(self, *other):
        """
        Return ``self`` with ``other`` subtracted.

        INPUT:

        - ``other`` -- a :class:`RealSet` or data that defines one

        OUTPUT:

        The set-theoretic difference of ``self`` with ``other``
        removed as a new :class:`RealSet`.

        EXAMPLES::

            sage: s1 = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s1
            (0, 2) ∪ [10, +oo)
            sage: s2 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s2
            (-oo, -10] ∪ (1, 3)
            sage: s1.difference(s2)
            (0, 1] ∪ [10, +oo)
            sage: s1 - s2    # syntactic sugar
            (0, 1] ∪ [10, +oo)
            sage: s2.difference(s1)
            (-oo, -10] ∪ [2, 3)
            sage: s2 - s1    # syntactic sugar
            (-oo, -10] ∪ [2, 3)
            sage: s1.difference(1,11)
            (0, 1] ∪ [11, +oo)
        """
    def symmetric_difference(self, *other):
        """
        Return the symmetric difference of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a :class:`RealSet` or data that defines one

        OUTPUT:

        The set-theoretic symmetric difference of ``self`` and ``other``
        as a new :class:`RealSet`.

        EXAMPLES::

            sage: s1 = RealSet(0,2); s1
            (0, 2)
            sage: s2 = RealSet.unbounded_above_open(1); s2
            (1, +oo)
            sage: s1.symmetric_difference(s2)
            (0, 1] ∪ [2, +oo)
        """
    def contains(self, x):
        """
        Return whether `x` is contained in the set.

        INPUT:

        - ``x`` -- a real number

        OUTPUT: boolean

        EXAMPLES::

            sage: s = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s
            (0, 2) ∪ [10, +oo)
            sage: s.contains(1)
            True
            sage: s.contains(0)
            False
            sage: s.contains(10.0)
            True
            sage: 10 in s    # syntactic sugar
            True
            sage: s.contains(+oo)
            False
            sage: RealSet().contains(1)
            False
        """
    __contains__ = contains
    def is_subset(self, *other):
        """
        Return whether ``self`` is a subset of ``other``.

        INPUT:

        - ``*other`` -- a :class:`RealSet` or something that defines one

        OUTPUT: boolean

        EXAMPLES::

            sage: I = RealSet((1,2))
            sage: J = RealSet((1,3))
            sage: K = RealSet((2,3))
            sage: I.is_subset(J)
            True
            sage: J.is_subset(K)
            False
        """
    is_included_in: Incomplete
    def is_open(self):
        """
        Return whether ``self`` is an open set.

        EXAMPLES::

            sage: RealSet().is_open()
            True
            sage: RealSet.point(1).is_open()
            False
            sage: RealSet((1, 2)).is_open()
            True
            sage: RealSet([1, 2], (3, 4)).is_open()
            False
            sage: RealSet(-oo, +oo).is_open()
            True
        """
    def is_closed(self):
        """
        Return whether ``self`` is a closed set.

        EXAMPLES::

            sage: RealSet().is_closed()
            True
            sage: RealSet.point(1).is_closed()
            True
            sage: RealSet([1, 2]).is_closed()
            True
            sage: RealSet([1, 2], (3, 4)).is_closed()
            False
            sage: RealSet(-oo, +oo).is_closed()
            True
        """
    def closure(self):
        """
        Return the topological closure of ``self`` as a new :class:`RealSet`.

        EXAMPLES::

            sage: RealSet(-oo, oo).closure()
            (-oo, +oo)
            sage: RealSet((1, 2), (2, 3)).closure()
            [1, 3]
            sage: RealSet().closure()
            {}
        """
    def interior(self):
        """
        Return the topological interior of ``self`` as a new :class:`RealSet`.

        EXAMPLES::

            sage: RealSet(-oo, oo).interior()
            (-oo, +oo)
            sage: RealSet().interior()
            {}
            sage: RealSet.point(2).interior()
            {}
            sage: RealSet([1, 2], (3, 4)).interior()
            (1, 2) ∪ (3, 4)
        """
    def boundary(self):
        """
        Return the topological boundary of ``self`` as a new :class:`RealSet`.

        EXAMPLES::

            sage: RealSet(-oo, oo).boundary()
            {}
            sage: RealSet().boundary()
            {}
            sage: RealSet.point(2).boundary()
            {2}
            sage: RealSet([1, 2], (3, 4)).boundary()
            {1} ∪ {2} ∪ {3} ∪ {4}
            sage: RealSet((1, 2), (2, 3)).boundary()
            {1} ∪ {2} ∪ {3}
        """
    @staticmethod
    def convex_hull(*real_set_collection):
        """
        Return the convex hull of real sets.

        INPUT:

        - ``*real_set_collection`` -- list/tuple/iterable of :class:`RealSet`
          or data that defines one

        OUTPUT: the convex hull as a new :class:`RealSet`

        EXAMPLES::

            sage: s1 = RealSet(0,2) + RealSet.unbounded_above_closed(10);  s1 # unbounded set
            (0, 2) ∪ [10, +oo)
            sage: s2 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s2
            (-oo, -10] ∪ (1, 3)
            sage: s3 = RealSet((0,2), RealSet.point(8)); s3
            (0, 2) ∪ {8}
            sage: s4 = RealSet(); s4  # empty set
            {}
            sage: RealSet.convex_hull(s1)
            (0, +oo)
            sage: RealSet.convex_hull(s2)
            (-oo, 3)
            sage: RealSet.convex_hull(s3)
            (0, 8]
            sage: RealSet.convex_hull(s4)
            {}
            sage: RealSet.convex_hull(s1, s2)
            (-oo, +oo)
            sage: RealSet.convex_hull(s2, s3)
            (-oo, 8]
            sage: RealSet.convex_hull(s2, s3, s4)
            (-oo, 8]
        """
    def is_connected(self):
        """
        Return whether ``self`` is a connected set.

        OUTPUT: boolean

        EXAMPLES::

            sage: s1 = RealSet((1, 2), (2, 4));  s1
            (1, 2) ∪ (2, 4)
            sage: s1.is_connected()
            False
            sage: s2 = RealSet((1, 2), (2, 4), RealSet.point(2));  s2
            (1, 4)
            sage: s2.is_connected()
            True
            sage: s3 = RealSet(1,3) + RealSet.unbounded_below_closed(-10);  s3
            (-oo, -10] ∪ (1, 3)
            sage: s3.is_connected()
            False
            sage: RealSet(x != 0).is_connected()                                        # needs sage.symbolic
            False
            sage: RealSet(-oo, oo).is_connected()
            True
            sage: RealSet().is_connected()
            False
        """
    def is_disjoint(self, *other):
        """
        Test whether the two sets are disjoint.

        INPUT:

        - ``other`` -- a :class:`RealSet` or data defining one

        OUTPUT: boolean

        .. SEEALSO:: :meth:`are_pairwise_disjoint`

        EXAMPLES::

            sage: s = RealSet((0, 1), (2, 3));  s
            (0, 1) ∪ (2, 3)
            sage: s.is_disjoint(RealSet([1, 2]))
            True
            sage: s.is_disjoint([3/2, 5/2])
            False
            sage: s.is_disjoint(RealSet())
            True
            sage: s.is_disjoint(RealSet().real_line())
            False
        """
    is_disjoint_from: Incomplete
    @staticmethod
    def are_pairwise_disjoint(*real_set_collection):
        """
        Test whether the real sets are pairwise disjoint.

        INPUT:

        - ``*real_set_collection`` -- list/tuple/iterable of :class:`RealSet`
          or data that defines one

        OUTPUT: boolean

        .. SEEALSO:: :meth:`is_disjoint`

        EXAMPLES::

            sage: s1 = RealSet((0, 1), (2, 3))
            sage: s2 = RealSet((1, 2))
            sage: s3 = RealSet.point(3)
            sage: RealSet.are_pairwise_disjoint(s1, s2, s3)
            True
            sage: RealSet.are_pairwise_disjoint(s1, s2, s3, [10,10])
            True
            sage: RealSet.are_pairwise_disjoint(s1, s2, s3, [-1, 1/2])
            False
        """
    def __mul__(self, right):
        """
        Scale a real set by a scalar on the left or right.

        EXAMPLES::

            sage: A = RealSet([0, 1/2], (2, infinity)); A
            [0, 1/2] ∪ (2, +oo)
            sage: 2 * A
            [0, 1] ∪ (4, +oo)
            sage: A * 100
            [0, 50] ∪ (200, +oo)
            sage: 1.5 * A
            [0.000000000000000, 0.750000000000000] ∪ (3.00000000000000, +oo)
            sage: (-2) * A
            (-oo, -4) ∪ [-1, 0]
        """
    def __rmul__(self, other):
        """
        Scale a real set by a scalar on the left.

        TESTS::

            sage: A = RealSet([0, 1/2], RealSet.unbounded_above_closed(2)); A
            [0, 1/2] ∪ [2, +oo)
            sage: pi * A                                                                # needs sage.symbolic
            [0, 1/2*pi] ∪ [2*pi, +oo)
        """
