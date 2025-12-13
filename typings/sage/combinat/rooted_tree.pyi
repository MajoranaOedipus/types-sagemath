from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.abstract_tree import AbstractClonableTree as AbstractClonableTree, AbstractLabelledClonableTree as AbstractLabelledClonableTree
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute, lazy_class_attribute as lazy_class_attribute
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.list_clone import NormalizedClonableList as NormalizedClonableList
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

@cached_function
def number_of_rooted_trees(n):
    """
    Return the number of rooted trees with `n` nodes.

    Compute the number `a(n)` of rooted trees with `n` nodes using the
    recursive formula ([SL000081]_):

    .. MATH::

        a(n+1) = \\frac{1}{n} \\sum_{k=1}^{n} \\left( \\sum_{d|k} d a(d) \\right) a(n-k+1)

    EXAMPLES::

        sage: from sage.combinat.rooted_tree import number_of_rooted_trees
        sage: [number_of_rooted_trees(i) for i in range(10)]
        [0, 1, 1, 2, 4, 9, 20, 48, 115, 286]

    REFERENCES:

    .. [SL000081] Sloane's :oeis:`A000081`
    """

class RootedTree(AbstractClonableTree, NormalizedClonableList, metaclass=InheritComparisonClasscallMetaclass):
    '''
    The class for unordered rooted trees.

    The *unordered rooted trees* are an inductive datatype defined
    as follows: An unordered rooted tree is a multiset of
    unordered rooted trees. The trees that belong to this
    multiset are said to be the *children* of the tree. The tree
    that has no children is called a *leaf*.

    The *labelled rooted trees* (:class:`LabelledRootedTree`)
    form a subclass of this class; they carry additional data.

    One can create a tree from any list (or more generally iterable)
    of trees or objects convertible to a tree.

    EXAMPLES::

        sage: RootedTree([])
        []
        sage: RootedTree([[], [[]]])
        [[], [[]]]
        sage: RootedTree([[[]], []])
        [[], [[]]]
        sage: O = OrderedTree([[[]], []]); O
        [[[]], []]
        sage: RootedTree(O)  # this is O with the ordering forgotten
        [[], [[]]]

    One can also enter any small rooted tree ("small" meaning that
    no vertex has more than `15` children) by using a simple
    numerical encoding of rooted trees, namely, the
    :func:`~sage.combinat.abstract_tree.from_hexacode` function.
    (This function actually parametrizes ordered trees, and here
    we make it parametrize unordered trees by forgetting the
    ordering.) ::

        sage: from sage.combinat.abstract_tree import from_hexacode
        sage: RT = RootedTrees()
        sage: from_hexacode(\'32001010\', RT)
        [[[]], [[]], [[], []]]

    .. NOTE::

        Unlike an ordered tree, an (unordered) rooted tree is a
        multiset (rather than a list) of children. That is, two
        ordered trees which differ from each other by switching
        the order of children are equal to each other as (unordered)
        rooted trees. Internally, rooted trees are encoded as
        :class:`sage.structure.list_clone.NormalizedClonableList`
        instances, and instead of storing their children as an
        actual multiset, they store their children as a list which
        is sorted according to their :meth:`sort_key` value. This
        is as good as storing them as multisets, since the
        :meth:`sort_key` values are sortable and distinguish
        different (unordered) trees. However, if you wish to define
        a subclass of :class:`RootedTree` which implements rooted
        trees with extra structure (say, a class of edge-colored
        rooted trees, or a class of rooted trees with a cyclic
        order on the list of children), then the inherited
        :meth:`sort_key` method will no longer distinguish different
        trees (and, as a consequence, equal trees will be regarded
        as distinct). Thus, you will have to override the method by
        one that does distinguish different trees.
    '''
    @staticmethod
    def __classcall_private__(cls, *args, **opts):
        """
        Ensure that rooted trees created by the enumerated sets and directly
        are the same and that they are instances of :class:`RootedTree`.

        TESTS::

            sage: from sage.combinat.rooted_tree import (RootedTrees_all,
            ....:    RootedTrees_size)
            sage: issubclass(RootedTrees_all().element_class, RootedTree)
            True
            sage: issubclass(RootedTrees_size(3).element_class, RootedTree)
            True
            sage: t0 = RootedTree([[],[[]]])
            sage: t0.parent()
            Rooted trees
            sage: type(t0)
            <class 'sage.combinat.rooted_tree.RootedTrees_all_with_category.element_class'>

            sage: t1 = RootedTrees()([[],[[]]])
            sage: t1.parent() is t0.parent()
            True
            sage: type(t1) is type(t0)
            True

            sage: t1 = RootedTrees(4)([[],[[]]])
            sage: t1.parent() is t0.parent()
            True
            sage: type(t1) is type(t0)
            True
        """
    def __init__(self, parent=None, children=[], check: bool = True) -> None:
        """
        TESTS::

            sage: RT4 = RootedTrees(4)
            sage: t1 = RT4([[],[[]]])
            sage: TestSuite(t1).run()

        Some bad inputs are refused::

            sage: RT4(69)
            Traceback (most recent call last):
            ...
            TypeError: input (69) is not a valid tree
        """
    def sort_key(self):
        """
        Return a tuple of nonnegative integers encoding the rooted
        tree ``self``.

        The first entry of the tuple is the number of children of the
        root. Then the rest of the tuple is obtained as follows: List
        the tuples corresponding to all children (we are regarding the
        children themselves as trees). Order this list (not the
        tuples!) in lexicographically increasing order, and flatten
        it into a single tuple.

        This tuple characterizes the rooted tree uniquely, and can be
        used to sort the rooted trees.

        .. NOTE::

            The tree ``self`` must be normalized before calling this
            method (see :meth:`normalize`). This does not matter
            unless you are inside the :meth:`clone` context manager,
            because outside of it every rooted tree is already
            normalized.

        .. NOTE::

            By default, this method does not encode any extra
            structure that ``self`` might have. If you have a subclass
            inheriting from :class:`RootedTree` which allows for some
            extra structure, you need to override :meth:`sort_key` in
            order to preserve this structure (for example, the
            :class:`LabelledRootedTree` class does this in
            :meth:`LabelledRootedTree.sort_key`). See the note in the
            docstring of
            :meth:`sage.combinat.ordered_tree.OrderedTree.sort_key`
            for a pitfall.

        EXAMPLES::

            sage: RT = RootedTree
            sage: RT([[],[[]]]).sort_key()
            (2, 0, 1, 0)
            sage: RT([[[]],[]]).sort_key()
            (2, 0, 1, 0)
        """
    def __hash__(self):
        """
        Return a hash for ``self``.

        This is based on :meth:`sort_key`.

        EXAMPLES::

            sage: RT = RootedTree
            sage: hash(RT([[],[[]]])) == hash((2, 0, 1, 0)) # indirect doctest
            True
        """
    def normalize(self):
        """
        Normalize ``self``.

        This function is at the core of the implementation of rooted
        (unordered) trees. The underlying structure is provided by
        ordered rooted trees. Every rooted tree is represented by a
        normalized element in the set of its planar embeddings.

        There should be no need to call ``normalize`` directly as it
        is called automatically upon creation and cloning or
        modification (by ``NormalizedClonableList``).

        The normalization has a recursive definition. It means first
        that every sub-tree is itself normalized, and also that
        sub-trees are sorted. Here the sort is performed according to
        the values of the :meth:`sort_key` method.

        EXAMPLES::

            sage: RT = RootedTree
            sage: RT([[],[[]]]) == RT([[[]],[]])  # indirect doctest
            True
            sage: rt1 = RT([[],[[]]])
            sage: rt2 = RT([[[]],[]])
            sage: rt1 is rt2
            False
            sage: rt1 == rt2
            True
            sage: rt1._get_list() == rt2._get_list()
            True
        """
    def is_empty(self):
        """
        Return if ``self`` is the empty tree.

        For rooted trees, this always returns ``False``.

        .. NOTE::

            This is not the same as ``bool(t)``, which returns whether
            ``t`` has some child or not.

        EXAMPLES::

            sage: t = RootedTrees(4)([[],[[]]])
            sage: t.is_empty()
            False
            sage: bool(t)
            True
            sage: t = RootedTrees(1)([])
            sage: t.is_empty()
            False
            sage: bool(t)
            False
        """
    def graft_list(self, other):
        """
        Return the list of trees obtained by grafting ``other`` on ``self``.

        Here grafting means that one takes the disjoint union of
        ``self`` and ``other``, chooses a node of ``self``,
        and adds the root of ``other`` to the list of children of
        this node. The root of the resulting tree is the root of
        ``self``. (This can be done for each node of ``self``;
        this method returns the list of all results.)

        This is useful for free pre-Lie algebras.

        EXAMPLES::

            sage: RT = RootedTree
            sage: x = RT([])
            sage: y = RT([x, x])
            sage: x.graft_list(x)
            [[[]]]
            sage: l = y.graft_list(x); l
            [[[], [], []], [[], [[]]], [[], [[]]]]
            sage: [parent(i) for i in l]
            [Rooted trees, Rooted trees, Rooted trees]

        TESTS::

            sage: x = RootedTrees(1)([])
            sage: y = RootedTrees(3)([x, x])
            sage: l = y.graft_list(x); l
            [[[], [], []], [[], [[]]], [[], [[]]]]
            sage: [parent(i) for i in l]
            [Rooted trees, Rooted trees, Rooted trees]

            sage: x = RootedTree([[[], []], []])
            sage: y = RootedTree([[], []])
            sage: len(set(x.graft_list(y)))
            4
        """
    def graft_on_root(self, other):
        """
        Return the tree obtained by grafting ``other`` on the root of ``self``.

        Here grafting means that one takes the disjoint union of
        ``self`` and ``other``, and adds the root of ``other`` to
        the list of children of ``self``. The root of the resulting
        tree is the root of ``self``.

        This is useful for free Nap algebras.

        EXAMPLES::

            sage: RT = RootedTree
            sage: x = RT([])
            sage: y = RT([x, x])
            sage: x.graft_on_root(x)
            [[]]
            sage: y.graft_on_root(x)
            [[], [], []]
            sage: x.graft_on_root(y)
            [[[], []]]
        """
    def single_graft(self, x, grafting_function, path_prefix=()):
        """
        Graft subtrees of `x` on ``self`` using the given function.

        Let `x_1, x_2, \\ldots, x_p` be the children of the root of
        `x`. For each `i`, the subtree of `x` comprising all
        descendants of `x_i` is joined by a new edge to
        the vertex of ``self`` specified by the `i`-th path in the
        grafting function (i.e., by the path
        ``grafting_function[i]``).

        The number of vertices of the result is the sum of the numbers
        of vertices of ``self`` and `x` minus one, because the root of
        `x` is not used.

        This is used to define the product of the Grossman-Larson algebras.

        INPUT:

        - ``x`` -- a rooted tree

        - ``grafting_function`` -- list of paths in ``self``

        - ``path_prefix`` -- tuple (default: ``()``)

        The ``path_prefix`` argument is only used for internal recursion.

        EXAMPLES::

            sage: LT = LabelledRootedTrees()
            sage: y = LT([LT([],label='b')], label='a')
            sage: x = LT([LT([],label='d')], label='c')
            sage: y.single_graft(x,[(0,)])
            a[b[d[]]]
            sage: t = LT([LT([],label='b'),LT([],label='c')], label='a')
            sage: s = LT([LT([],label='d'),LT([],label='e')], label='f')
            sage: t.single_graft(s,[(0,),(1,)])
            a[b[d[]], c[e[]]]
        """

class RootedTrees(UniqueRepresentation, Parent):
    """
    Factory class for rooted trees.

    INPUT:

    - ``size`` -- integer (optional)

    OUTPUT:

    the set of all rooted trees (of the given size ``size`` if
    specified)

    EXAMPLES::

        sage: RootedTrees()
        Rooted trees

        sage: RootedTrees(2)
        Rooted trees with 2 nodes
    """
    @staticmethod
    def __classcall_private__(cls, n=None):
        """
        TESTS::

            sage: from sage.combinat.rooted_tree import (RootedTrees_all,
            ....:    RootedTrees_size)
            sage: RootedTrees(2) is RootedTrees_size(2)
            True
            sage: RootedTrees(5).cardinality()
            9
            sage: RootedTrees() is RootedTrees_all()
            True

        TESTS::

            sage: RootedTrees(0)
            Traceback (most recent call last):
            ...
            ValueError: n must be a positive integer
        """

class RootedTrees_all(DisjointUnionEnumeratedSets, RootedTrees):
    """
    Class of all (unordered, unlabelled) rooted trees.

    See :class:`RootedTree` for a definition.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: sum(x**len(t)                                                         # needs sage.symbolic
            ....:     for t in set(RootedTree(t) for t in OrderedTrees(6)))
            x^5 + x^4 + 3*x^3 + 6*x^2 + 9*x
            sage: sum(x**len(t) for t in RootedTrees(6))                                # needs sage.symbolic
            x^5 + x^4 + 3*x^3 + 6*x^2 + 9*x

            sage: TestSuite(RootedTrees()).run() # long time
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = RootedTrees()
            sage: 1 in S
            False
            sage: S([]) in S
            True
        """
    def unlabelled_trees(self):
        """
        Return the set of unlabelled trees associated to ``self``.

        EXAMPLES::

            sage: RootedTrees().unlabelled_trees()
            Rooted trees
        """
    def labelled_trees(self):
        """
        Return the set of labelled trees associated to ``self``.

        EXAMPLES::

            sage: RootedTrees().labelled_trees()
            Labelled rooted trees

        As a consequence::

            sage: lb = RootedTrees()([[],[[], []]]).canonical_labelling()
            sage: lb
            1[2[], 3[4[], 5[]]]
            sage: lb.__class__
            <class 'sage.combinat.rooted_tree.LabelledRootedTrees_all_with_category.element_class'>
            sage: lb.parent()
            Labelled rooted trees
        """
    @cached_method
    def leaf(self):
        """
        Return a leaf tree with ``self`` as parent.

        EXAMPLES::

            sage: RootedTrees().leaf()
            []
        """
    Element = RootedTree

class RootedTrees_size(RootedTrees):
    """
    The enumerated set of rooted trees with a given number of nodes.

    The number of nodes of a rooted tree is defined recursively:
    The number of nodes of a rooted tree with `a` children is `a`
    plus the sum of the number of nodes of each of these children.

    TESTS::

        sage: from sage.combinat.rooted_tree import RootedTrees_size
        sage: for i in range(1, 6): TestSuite(RootedTrees_size(i)).run()                # needs sage.combinat
    """
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: for i in range(1, 6):                                                 # needs sage.combinat
            ....:     TestSuite(RootedTrees(i)).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = RootedTrees(3)
            sage: 1 in S
            False
            sage: S([[],[]]) in S
            True
        """
    def __iter__(self):
        """
        An iterator for ``self``.

        This generates the rooted trees of given size. The algorithm
        first picks a partition for the sizes of subtrees, then picks
        appropriate tuples of smaller trees.

        EXAMPLES::

            sage: from sage.combinat.rooted_tree import *
            sage: RootedTrees(1).list()
            [[]]
            sage: RootedTrees(2).list()                                                 # needs sage.combinat
            [[[]]]
            sage: RootedTrees(3).list()                                                 # needs sage.combinat
            [[[[]]], [[], []]]
            sage: RootedTrees(4).list()                                                 # needs sage.combinat
            [[[[[]]]], [[[], []]], [[], [[]]], [[], [], []]]
        """
    def check_element(self, el, check: bool = True) -> None:
        """
        Check that a given tree actually belongs to ``self``.

        This just checks the number of vertices.

        EXAMPLES::

            sage: RT3 = RootedTrees(3)
            sage: RT3([[],[]])     # indirect doctest
            [[], []]
            sage: RT3([[],[],[]])  # indirect doctest
            Traceback (most recent call last):
            ...
            ValueError: wrong number of nodes
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: RootedTrees(1).cardinality()
            1
            sage: RootedTrees(3).cardinality()
            2
        """
    @lazy_attribute
    def element_class(self):
        """
        TESTS::

            sage: S = RootedTrees(3)
            sage: S.element_class
            <class 'sage.combinat.rooted_tree.RootedTrees_all_with_category.element_class'>
            sage: S.first().__class__ == RootedTrees().first().__class__                # needs sage.combinat
            True
        """

class LabelledRootedTree(AbstractLabelledClonableTree, RootedTree):
    """
    Labelled rooted trees.

    A labelled rooted tree is a rooted tree with a label
    attached at each node.

    More formally:
    The *labelled rooted trees* are an inductive datatype defined
    as follows: A labelled rooted tree is a multiset of labelled
    rooted trees, endowed with a label (which can be any object,
    including ``None``). The trees that belong to this multiset
    are said to be the *children* of the tree. (Notice that the
    labels of these children may and may not be of the same type
    as the label of the tree). A labelled rooted tree which has
    no children (so the only information it carries is its label)
    is said to be a *leaf*.

    Every labelled rooted tree gives rise to an unlabelled rooted
    tree (:class:`RootedTree`) by forgetting the labels. (This is
    implemented as a conversion.)

    INPUT:

    - ``children`` -- list or tuple or more generally any iterable
      of trees or objects convertible to trees

    - ``label`` -- any hashable Sage object (default: ``None``)

    .. NOTE::

        It is required that all labels are comparable.

    EXAMPLES::

        sage: x = LabelledRootedTree([], label = 3); x
        3[]
        sage: LabelledRootedTree([x, x, x], label = 2)
        2[3[], 3[], 3[]]
        sage: LabelledRootedTree((x, x, x), label = 2)
        2[3[], 3[], 3[]]
        sage: LabelledRootedTree([[],[[], []]], label = 3)
        3[None[], None[None[], None[]]]

    Children are reordered using the value of the :meth:`sort_key` method::

        sage: y = LabelledRootedTree([], label = 5); y
        5[]
        sage: xyy2 = LabelledRootedTree((x, y, y), label = 2); xyy2
        2[3[], 5[], 5[]]
        sage: yxy2 = LabelledRootedTree((y, x, y), label = 2); yxy2
        2[3[], 5[], 5[]]
        sage: xyy2 == yxy2
        True

    Converting labelled into unlabelled rooted trees by
    forgetting the labels, and back (the labels are
    initialized as ``None``)::

       sage: yxy2crude = RootedTree(yxy2); yxy2crude
       [[], [], []]
       sage: LabelledRootedTree(yxy2crude)
       None[None[], None[], None[]]

    TESTS::

        sage: xyy2._get_list() == yxy2._get_list()
        True
    """
    @staticmethod
    def __classcall_private__(cls, *args, **opts):
        """
        Ensure that trees created by the sets and directly are the same and
        that they are instances of :class:`LabelledRootedTree`.

        TESTS::

            sage: issubclass(LabelledRootedTrees().element_class, LabelledRootedTree)
            True
            sage: t0 = LabelledRootedTree([[],[[], []]], label = 3)
            sage: t0.parent()
            Labelled rooted trees
            sage: type(t0)
            <class 'sage.combinat.rooted_tree.LabelledRootedTrees_all_with_category.element_class'>
        """
    def sort_key(self):
        """
        Return a tuple of nonnegative integers encoding the labelled
        rooted tree ``self``.

        The first entry of the tuple is a pair consisting of the
        number of children of the root and the label of the root. Then
        the rest of the tuple is obtained as follows: List
        the tuples corresponding to all children (we are regarding the
        children themselves as trees). Order this list (not the
        tuples!) in lexicographically increasing order, and flatten
        it into a single tuple.

        This tuple characterizes the labelled rooted tree uniquely, and
        can be used to sort the labelled rooted trees provided that the
        labels belong to a type which is totally ordered.

        .. NOTE::

            The tree ``self`` must be normalized before calling this
            method (see :meth:`normalize`). This does not matter
            unless you are inside the :meth:`clone` context manager,
            because outside of it every rooted tree is already
            normalized.

        .. NOTE::

            This method overrides :meth:`RootedTree.sort_key`
            and returns a result different from what the latter
            would return, as it wants to encode the whole labelled
            tree including its labelling rather than just the
            unlabelled tree. Therefore, be careful with using this
            method on subclasses of :class:`RootedOrderedTree`;
            under some circumstances they could inherit it from
            another superclass instead of from :class:`RootedTree`,
            which would cause the method to forget the labelling.
            See the docstrings of :meth:`RootedTree.sort_key` and
            :meth:`sage.combinat.ordered_tree.OrderedTree.sort_key`.

        EXAMPLES::

            sage: LRT = LabelledRootedTrees(); LRT
            Labelled rooted trees
            sage: x = LRT([], label = 3); x
            3[]
            sage: x.sort_key()
            ((0, 3),)
            sage: y = LRT([x, x, x], label = 2); y
            2[3[], 3[], 3[]]
            sage: y.sort_key()
            ((3, 2), (0, 3), (0, 3), (0, 3))
            sage: LRT.an_element().sort_key()
            ((3, 'alpha'), (0, 3), (1, 5), (0, None), (2, 42), (0, 3), (0, 3))
            sage: lb = RootedTrees()([[],[[], []]]).canonical_labelling()
            sage: lb.sort_key()
            ((2, 1), (0, 2), (2, 3), (0, 4), (0, 5))
        """
    def __hash__(self):
        """
        Return a hash for ``self``.

        EXAMPLES::

            sage: lb = RootedTrees()([[],[[], []]]).canonical_labelling()
            sage: hash(lb) == hash(((2, 1), (0, 2), (2, 3), (0, 4), (0, 5))) # indirect doctest
            True
        """

class LabelledRootedTrees(UniqueRepresentation, Parent):
    """
    This is a parent stub to serve as a factory class for labelled
    rooted trees.

    EXAMPLES::

        sage: LRT = LabelledRootedTrees(); LRT
        Labelled rooted trees
        sage: x = LRT([], label = 3); x
        3[]
        sage: x.parent() is LRT
        True
        sage: y = LRT([x, x, x], label = 2); y
        2[3[], 3[], 3[]]
        sage: y.parent() is LRT
        True

    .. TODO::

        Add the possibility to restrict the labels to a fixed set.
    """
    @staticmethod
    def __classcall_private__(cls, n=None):
        """
        TESTS::

            sage: from sage.combinat.rooted_tree import LabelledRootedTrees_all
            sage: LabelledRootedTrees_all() == LabelledRootedTrees()
            True
        """

class LabelledRootedTrees_all(LabelledRootedTrees):
    """
    Class of all (unordered) labelled rooted trees.

    See :class:`LabelledRootedTree` for a definition.
    """
    def __init__(self, category=None) -> None:
        """
        TESTS::

            sage: TestSuite(LabelledRootedTrees()).run()
        """
    def unlabelled_trees(self):
        """
        Return the set of unlabelled trees associated to ``self``.

        EXAMPLES::

            sage: LabelledRootedTrees().unlabelled_trees()
            Rooted trees
        """
    def labelled_trees(self):
        """
        Return the set of labelled trees associated to ``self``.

        EXAMPLES::

            sage: LabelledRootedTrees().labelled_trees()
            Labelled rooted trees
        """
    Element = LabelledRootedTree
