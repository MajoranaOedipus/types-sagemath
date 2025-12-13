from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.combinat.abstract_tree import AbstractClonableTree as AbstractClonableTree, AbstractLabelledClonableTree as AbstractLabelledClonableTree
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.composition import Compositions as Compositions
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute, lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.list_clone import ClonableArray as ClonableArray, ClonableList as ClonableList
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class OrderedTree(AbstractClonableTree, ClonableList, metaclass=InheritComparisonClasscallMetaclass):
    """
    The class of (ordered rooted) trees.

    An ordered tree is constructed from a node, called the root, on which one
    has grafted a possibly empty list of trees. There is a total order on the
    children of a node which is given by the order of the elements in the
    list. Note that there is no empty ordered tree (so the smallest ordered
    tree consists of just one node).

    INPUT:

    One can create a tree from any list (or more generally iterable) of trees
    or objects convertible to a tree. Alternatively a string is also
    accepted. The syntax is the same as for printing: children are grouped by
    square brackets.

    EXAMPLES::

        sage: x = OrderedTree([])
        sage: x1 = OrderedTree([x,x])
        sage: x2 = OrderedTree([[],[]])
        sage: x1 == x2
        True
        sage: tt1 = OrderedTree([x,x1,x2])
        sage: tt2 = OrderedTree([[], [[], []], x2])
        sage: tt1 == tt2
        True

        sage: OrderedTree([]) == OrderedTree()
        True

    TESTS::

        sage: x1.__hash__() == x2.__hash__()
        True
        sage: tt1.__hash__() == tt2.__hash__()
        True

    Trees are usually immutable. However they inherit from
    :class:`sage.structure.list_clone.ClonableList`, so that they can be
    modified using the clone protocol. Let us now see what this means.

    Trying to modify a non-mutable tree raises an error::

        sage: tt1[1] = tt2
        Traceback (most recent call last):
        ...
        ValueError: object is immutable; please change a copy instead.

    Here is the correct way to do it::

        sage: with tt2.clone() as tt2:
        ....:     tt2[1] = tt1
        sage: tt2
        [[], [[], [[], []], [[], []]], [[], []]]

    It is also possible to append a child to a tree::

        sage: with tt2.clone() as tt3:
        ....:     tt3.append(OrderedTree([]))
        sage: tt3
        [[], [[], [[], []], [[], []]], [[], []], []]

    Or to insert a child in a tree::

        sage: with tt2.clone() as tt3:
        ....:     tt3.insert(2, OrderedTree([]))
        sage: tt3
        [[], [[], [[], []], [[], []]], [], [[], []]]

    We check that ``tt1`` is not modified and that everything is correct with
    respect to equality::

        sage: tt1
        [[], [[], []], [[], []]]
        sage: tt1 == tt2
        False
        sage: tt1.__hash__() == tt2.__hash__()
        False

    TESTS::

        sage: tt1bis = OrderedTree(tt1)
        sage: with tt1.clone() as tt1:
        ....:     tt1[1] = tt1bis
        sage: tt1
        [[], [[], [[], []], [[], []]], [[], []]]
        sage: tt1 == tt2
        True
        sage: tt1.__hash__() == tt2.__hash__()
        True
        sage: len(tt1)
        3
        sage: tt1[2]
        [[], []]
        sage: tt1[3]
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        sage: tt1[1:2]
        [[[], [[], []], [[], []]]]

    Various tests involving construction, equality and hashing::

        sage: OrderedTree() == OrderedTree()
        True
        sage: t1 = OrderedTree([[],[[]]])
        sage: t2 = OrderedTree([[],[[]]])
        sage: t1 == t2
        True
        sage: t2 = OrderedTree(t1)
        sage: t1 == t2
        True
        sage: t1 = OrderedTree([[],[[]]])
        sage: t2 = OrderedTree([[[]],[]])
        sage: t1 == t2
        False

        sage: t1 = OrderedTree([[],[[]]])
        sage: t2 = OrderedTree([[],[[]]])
        sage: t1.__hash__() == t2.__hash__()
        True
        sage: t2 = OrderedTree([[[]],[]])
        sage: t1.__hash__() == t2.__hash__()
        False
        sage: OrderedTree().__hash__() == OrderedTree([]).__hash__()
        True
        sage: tt1 = OrderedTree([t1,t2,t1])
        sage: tt2 = OrderedTree([t1, [[[]],[]], t1])
        sage: tt1.__hash__() == tt2.__hash__()
        True

    Check that the hash value is correctly updated after modification::

        sage: with tt2.clone() as tt2:
        ....:     tt2[1,1] = tt1
        sage: tt1.__hash__() == tt2.__hash__()
        False
    """
    @staticmethod
    def __classcall_private__(cls, *args, **opts):
        """
        Ensure that trees created by the enumerated sets and directly
        are the same and that they are instances of :class:`OrderedTree`

        TESTS::

            sage: issubclass(OrderedTrees().element_class, OrderedTree)
            True
            sage: t0 = OrderedTree([[],[[], []]])
            sage: t0.parent()
            Ordered trees
            sage: type(t0)
            <class 'sage.combinat.ordered_tree.OrderedTrees_all_with_category.element_class'>

            sage: t1 = OrderedTrees()([[],[[], []]])
            sage: t1.parent() is t0.parent()
            True
            sage: type(t1) is type(t0)
            True

            sage: t1 = OrderedTrees(4)([[],[[]]])
            sage: t1.parent() is t0.parent()
            True
            sage: type(t1) is type(t0)
            True
        """
    def __init__(self, parent=None, children=None, check: bool = True) -> None:
        '''
        TESTS::

            sage: t1 = OrderedTrees(4)([[],[[]]])
            sage: TestSuite(t1).run()
            sage: OrderedTrees()("[]") # indirect doctest
            []
            sage: all(OrderedTree(repr(tr)) == tr for i in range(6) for tr in OrderedTrees(i))
            True
        '''
    def is_empty(self):
        """
        Return if ``self`` is the empty tree.

        For ordered trees, this always returns ``False``.

        .. NOTE:: this is different from ``bool(t)`` which returns whether
                  ``t`` has some child or not.

        EXAMPLES::

            sage: t = OrderedTrees(4)([[],[[]]])
            sage: t.is_empty()
            False
            sage: bool(t)
            True
        """
    def to_binary_tree_left_branch(self):
        """
        Return a binary tree of size `n-1` (where `n` is the size of `t`,
        and where `t` is ``self``) obtained from `t` by the following
        recursive rule:

        - if `x` is the left brother of `y` in `t`, then `x` becomes the
          left child of `y`;
        - if `x` is the last child of `y` in `t`, then `x` becomes the
          right child of `y`,

        and removing the root of `t`.

        EXAMPLES::

            sage: T = OrderedTree([[],[]])
            sage: T.to_binary_tree_left_branch()
            [[., .], .]
            sage: T = OrderedTree([[], [[], []], [[], [[]]]])
            sage: T.to_binary_tree_left_branch()
            [[[., .], [[., .], .]], [[., .], [., .]]]

        TESTS::

            sage: T = OrderedTree([[],[]])
            sage: T == T.to_binary_tree_left_branch().to_ordered_tree_left_branch()
            True
            sage: T = OrderedTree([[], [[], []], [[], [[]]]])
            sage: T == T.to_binary_tree_left_branch().to_ordered_tree_left_branch()
            True
        """
    def to_parallelogram_polyomino(self, bijection=None):
        """
        Return a polyomino parallelogram.

        INPUT:

        - ``bijection`` -- (default: ``'Boussicault-Socci'``) is the name of the
          bijection to use. Possible values are ``'Boussicault-Socci'``,
          ``'via dyck and Delest-Viennot'``.

        EXAMPLES::

            sage: # needs sage.combinat sage.modules
            sage: T = OrderedTree([[[], [[], [[]]]], [], [[[],[]]], [], []])
            sage: T.to_parallelogram_polyomino(bijection='Boussicault-Socci')
            [[0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0]]
            sage: T = OrderedTree( [] )
            sage: T.to_parallelogram_polyomino()
            [[1], [1]]
            sage: T = OrderedTree( [[]] )
            sage: T.to_parallelogram_polyomino()
            [[0, 1], [1, 0]]
            sage: T = OrderedTree( [[],[]] )
            sage: T.to_parallelogram_polyomino()
            [[0, 1, 1], [1, 1, 0]]
            sage: T = OrderedTree( [[[]]] )
            sage: T.to_parallelogram_polyomino()
            [[0, 0, 1], [1, 0, 0]]
        """
    def to_binary_tree_right_branch(self):
        """
        Return a binary tree of size `n-1` (where `n` is the size of `t`,
        and where `t` is ``self``) obtained from `t` by the following
        recursive rule:

        - if `x` is the right brother of `y` in `t`, then`x` becomes the
          right child of `y`;
        - if `x` is the first child of `y` in `t`, then `x` becomes the
          left child of `y`,

        and removing the root of `t`.

        EXAMPLES::

            sage: T = OrderedTree([[],[]])
            sage: T.to_binary_tree_right_branch()
            [., [., .]]
            sage: T = OrderedTree([[], [[], []], [[], [[]]]])
            sage: T.to_binary_tree_right_branch()
            [., [[., [., .]], [[., [[., .], .]], .]]]

        TESTS::

            sage: T = OrderedTree([[],[]])
            sage: T == T.to_binary_tree_right_branch().to_ordered_tree_right_branch()
            True
            sage: T = OrderedTree([[], [[], []], [[], [[]]]])
            sage: T == T.to_binary_tree_right_branch().to_ordered_tree_right_branch()
            True
        """
    def to_dyck_word(self):
        """
        Return the Dyck path corresponding to ``self`` where the maximal
        height of the Dyck path is the depth of ``self`` .

        EXAMPLES::

            sage: T = OrderedTree([[],[]])
            sage: T.to_dyck_word()                                                      # needs sage.combinat
            [1, 0, 1, 0]
            sage: T = OrderedTree([[],[[]]])
            sage: T.to_dyck_word()                                                      # needs sage.combinat
            [1, 0, 1, 1, 0, 0]
            sage: T = OrderedTree([[], [[], []], [[], [[]]]])
            sage: T.to_dyck_word()                                                      # needs sage.combinat
            [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
        """
    def to_undirected_graph(self):
        """
        Return the undirected graph obtained from the tree nodes and edges.

        The graph is endowed with an embedding, so that it will be displayed
        correctly.

        EXAMPLES::

            sage: t = OrderedTree([])
            sage: t.to_undirected_graph()
            Graph on 1 vertex
            sage: t = OrderedTree([[[]],[],[]])
            sage: t.to_undirected_graph()
            Graph on 5 vertices

        If the tree is labelled, we use its labelling to label the graph. This
        will fail if the labels are not all distinct.
        Otherwise, we use the graph canonical labelling which means that
        two different trees can have the same graph.

        EXAMPLES::

            sage: t = OrderedTree([[[]],[],[]])
            sage: t.canonical_labelling().to_undirected_graph()
            Graph on 5 vertices

        TESTS::

            sage: t.canonical_labelling().to_undirected_graph() == t.to_undirected_graph()
            False
            sage: OrderedTree([[],[]]).to_undirected_graph() == OrderedTree([[[]]]).to_undirected_graph()
            True
            sage: OrderedTree([[],[],[]]).to_undirected_graph() == OrderedTree([[[[]]]]).to_undirected_graph()
            False
        """
    def to_poset(self, root_to_leaf: bool = False):
        """
        Return the poset obtained by interpreting the tree as a Hasse
        diagram. The default orientation is from leaves to root but you can
        pass ``root_to_leaf=True`` to obtain the inverse orientation.

        INPUT:

        - ``root_to_leaf`` -- boolean (default: ``False``); ``True`` if the
          poset orientation should be from root to leaves

        EXAMPLES::

            sage: t = OrderedTree([])
            sage: t.to_poset()
            Finite poset containing 1 elements
            sage: p = OrderedTree([[[]],[],[]]).to_poset()
            sage: p.height(), p.width()                                                 # needs networkx
            (3, 3)

        If the tree is labelled, we use its labelling to label the poset.
        Otherwise, we use the poset canonical labelling::

            sage: t = OrderedTree([[[]],[],[]]).canonical_labelling().to_poset()
            sage: t.height(), t.width()                                                 # needs networkx
            (3, 3)
        """
    def left_right_symmetry(self):
        """
        Return the symmetric tree of ``self``.

        The symmetric tree `s(T)` of an ordered tree `T` is
        defined as follows:
        If `T` is an ordered tree with children `C_1, C_2, \\ldots, C_k`
        (listed from left to right), then the symmetric tree `s(T)` of
        `T` is the ordered tree with children
        `s(C_k), s(C_{k-1}), \\ldots, s(C_1)` (from left to right).

        EXAMPLES::

            sage: T = OrderedTree([[],[[]]])
            sage: T.left_right_symmetry()
            [[[]], []]
            sage: T = OrderedTree([[], [[], []], [[], [[]]]])
            sage: T.left_right_symmetry()
            [[[[]], []], [[], []], []]
        """
    def plot(self):
        """
        Plot the tree ``self``.

        .. WARNING::

            For a labelled tree, this will fail unless all labels are
            distinct. For unlabelled trees, some arbitrary labels are chosen.
            Use :meth:`_latex_`, ``view``,
            :meth:`_ascii_art_` or ``pretty_print`` for more
            faithful representations of the data of the tree.

        EXAMPLES::

            sage: p = OrderedTree([[[]],[],[]])
            sage: ascii_art(p)
              _o__
             / / /
            o o o
            |
            o
            sage: p.plot()                                                              # needs sage.plot
            Graphics object consisting of 10 graphics primitives

        .. PLOT::

            P = OrderedTree([[[]],[],[]]).plot()
            sphinx_plot(P)

        Now a labelled example::

            sage: g = OrderedTree([[],[[]],[]]).canonical_labelling()
            sage: ascii_art(g)
              _1__
             / / /
            2 3 5
              |
              4
            sage: g.plot()                                                              # needs sage.plot
            Graphics object consisting of 10 graphics primitives

        .. PLOT::

            P = OrderedTree([[],[[]],[]]).canonical_labelling().plot()
            sphinx_plot(P)
        """
    def sort_key(self):
        """
        Return a tuple of nonnegative integers encoding the ordered
        tree ``self``.

        The first entry of the tuple is the number of children of the
        root. Then the rest of the tuple is the concatenation of the
        tuples associated to these children (we view the children of
        a tree as trees themselves) from left to right.

        This tuple characterizes the tree uniquely, and can be used to
        sort the ordered trees.

        .. NOTE::

            By default, this method does not encode any extra
            structure that ``self`` might have -- e.g., if you were
            to define a class ``EdgeColoredOrderedTree`` which
            implements edge-colored trees and which inherits from
            :class:`OrderedTree`, then the :meth:`sort_key` method
            it would inherit would forget about the colors of the
            edges (and thus would not characterize edge-colored
            trees uniquely). If you want to preserve extra data,
            you need to override this method or use a new method.
            For instance, on the :class:`LabelledOrderedTree`
            subclass, this method is overridden by a slightly
            different method, which encodes not only the numbers
            of children of the nodes of ``self``, but also their
            labels.
            Be careful with using overridden methods, however:
            If you have (say) a class ``BalancedTree`` which
            inherits from :class:`OrderedTree` and which encodes
            balanced trees, and if you have another class
            ``BalancedLabelledOrderedTree`` which inherits both
            from ``BalancedOrderedTree`` and from
            :class:`LabelledOrderedTree`, then (depending on the MRO)
            the default :meth:`sort_key` method on
            ``BalancedLabelledOrderedTree`` (unless manually
            overridden) will be taken either from ``BalancedTree``
            or from :class:`LabelledOrderedTree`, and in the former
            case will ignore the labelling!

        EXAMPLES::

            sage: RT = OrderedTree
            sage: RT([[],[[]]]).sort_key()
            (2, 0, 1, 0)
            sage: RT([[[]],[]]).sort_key()
            (2, 1, 0, 0)
        """
    @cached_method
    def normalize(self, inplace: bool = False):
        '''
        Return the normalized tree of ``self``.

        INPUT:

        - ``inplace`` -- boolean (default: ``False``); if ``True``,
          then ``self`` is modified and nothing returned. Otherwise
          the normalized tree is returned.

        The normalization of an ordered tree `t` is an ordered tree `s`
        which has the property that `t` and `s` are isomorphic as
        *unordered* rooted trees, and that if two ordered trees `t` and
        `t\'` are isomorphic as *unordered* rooted trees, then the
        normalizations of `t` and `t\'` are identical. In other words,
        normalization is a map from the set of ordered trees to itself
        which picks a representative from every equivalence class with
        respect to the relation of "being isomorphic as unordered
        trees", and maps every ordered tree to the representative
        chosen from its class.

        This map proceeds recursively by first normalizing every
        subtree, and then sorting the subtrees according to the value
        of the :meth:`sort_key` method.

        Consider the quotient map `\\pi` that sends a planar rooted tree to
        the associated unordered rooted tree. Normalization is the
        composite `s \\circ \\pi`, where `s` is a section of `\\pi`.

        EXAMPLES::

            sage: OT = OrderedTree
            sage: ta = OT([[],[[]]])
            sage: tb = OT([[[]],[]])
            sage: ta.normalize() == tb.normalize()
            True
            sage: ta == tb
            False

        An example with inplace normalization::

            sage: OT = OrderedTree
            sage: ta = OT([[],[[]]])
            sage: tb = OT([[[]],[]])
            sage: ta.normalize(inplace=True); ta
            [[], [[]]]
            sage: tb.normalize(inplace=True); tb
            [[], [[]]]
        '''

class OrderedTrees(UniqueRepresentation, Parent):
    """
    Factory for ordered trees.

    INPUT:

    - ``size`` -- integer (optional)

    OUTPUT:

    - the set of all ordered trees (of the given ``size`` if specified)

    EXAMPLES::

        sage: OrderedTrees()
        Ordered trees

        sage: OrderedTrees(2)
        Ordered trees of size 2

    .. NOTE:: this is a factory class whose constructor returns instances of
              subclasses.

    .. NOTE:: the fact that OrderedTrees is a class instead of a simple callable
              is an implementation detail. It could be changed in the future
              and one should not rely on it.
    """
    @staticmethod
    def __classcall_private__(cls, n=None):
        """
        TESTS::

            sage: from sage.combinat.ordered_tree import OrderedTrees_all, OrderedTrees_size
            sage: isinstance(OrderedTrees(2), OrderedTrees)
            True
            sage: isinstance(OrderedTrees(), OrderedTrees)
            True
            sage: OrderedTrees(2) is OrderedTrees_size(2)
            True
            sage: OrderedTrees(5).cardinality()
            14
            sage: OrderedTrees() is OrderedTrees_all()
            True
        """
    @cached_method
    def leaf(self):
        """
        Return a leaf tree with ``self`` as parent.

        EXAMPLES::

            sage: OrderedTrees().leaf()
            []

        TESTS::

            sage: (OrderedTrees().leaf() is
            ....:     sage.combinat.ordered_tree.OrderedTrees_all().leaf())
            True
        """

class OrderedTrees_all(DisjointUnionEnumeratedSets, OrderedTrees):
    """
    The set of all ordered trees.

    EXAMPLES::

        sage: OT = OrderedTrees(); OT
        Ordered trees
        sage: OT.cardinality()
        +Infinity
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.combinat.ordered_tree import OrderedTrees_all
            sage: B = OrderedTrees_all()
            sage: B.cardinality()
            +Infinity

            sage: it = iter(B)
            sage: (next(it), next(it), next(it), next(it), next(it))
            ([], [[]], [[], []], [[[]]], [[], [], []])
            sage: next(it).parent()
            Ordered trees
            sage: B([])
            []

            sage: B is OrderedTrees_all()
            True
            sage: TestSuite(B).run() # long time
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: T = OrderedTrees()
            sage: 1 in T
            False
            sage: T([]) in T
            True
        """
    def unlabelled_trees(self):
        """
        Return the set of unlabelled trees associated to ``self``.

        EXAMPLES::

            sage: OrderedTrees().unlabelled_trees()
            Ordered trees
        """
    def labelled_trees(self):
        """
        Return the set of labelled trees associated to ``self``.

        EXAMPLES::

            sage: OrderedTrees().labelled_trees()
            Labelled ordered trees
        """
    Element = OrderedTree

class OrderedTrees_size(OrderedTrees):
    """
    The enumerated sets of binary trees of a given size.

    EXAMPLES::

        sage: S = OrderedTrees(3); S
        Ordered trees of size 3
        sage: S.cardinality()
        2
        sage: S.list()
        [[[], []], [[[]]]]
    """
    def __init__(self, size) -> None:
        """
        TESTS::

            sage: from sage.combinat.ordered_tree import OrderedTrees_size
            sage: TestSuite(OrderedTrees_size(0)).run()
            sage: for i in range(6): TestSuite(OrderedTrees_size(i)).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: T = OrderedTrees(3)
            sage: 1 in T
            False
            sage: T([[],[]]) in T
            True
        """
    def cardinality(self):
        """
        The cardinality of ``self``.

        This is a Catalan number.

        TESTS::

            sage: OrderedTrees(0).cardinality()
            0
            sage: OrderedTrees(1).cardinality()
            1
            sage: OrderedTrees(6).cardinality()
            42
        """
    def random_element(self):
        """
        Return a random ``OrderedTree`` with uniform probability.

        This method generates a random ``DyckWord`` and then uses a
        bijection between Dyck words and ordered trees.

        EXAMPLES::

            sage: OrderedTrees(5).random_element()  # random                            # needs sage.combinat
            [[[], []], []]
            sage: OrderedTrees(0).random_element()
            Traceback (most recent call last):
            ...
            EmptySetError: there are no ordered trees of size 0
            sage: OrderedTrees(1).random_element()                                      # needs sage.combinat
            []

        TESTS::

            sage: all(OrderedTrees(10).random_element() in OrderedTrees(10)             # needs sage.combinat
            ....:     for i in range(20))
            True
        """
    def __iter__(self):
        """
        A basic generator.

        .. TODO:: could be optimized.

        TESTS::

            sage: OrderedTrees(0).list()
            []
            sage: OrderedTrees(1).list()
            [[]]
            sage: OrderedTrees(2).list()
            [[[]]]
            sage: OrderedTrees(3).list()
            [[[], []], [[[]]]]
            sage: OrderedTrees(4).list()
            [[[], [], []], [[], [[]]], [[[]], []], [[[], []]], [[[[]]]]]
        """
    @lazy_attribute
    def element_class(self):
        """
        The class of the element of ``self``.

        EXAMPLES::

            sage: from sage.combinat.ordered_tree import OrderedTrees_size, OrderedTrees_all
            sage: S = OrderedTrees_size(3)
            sage: S.element_class is OrderedTrees().element_class
            True
            sage: S.first().__class__ == OrderedTrees_all().first().__class__
            True
        """

class LabelledOrderedTree(AbstractLabelledClonableTree, OrderedTree):
    """
    Labelled ordered trees.

    A labelled ordered tree is an ordered tree with a label attached at each
    node.

    INPUT:

    - ``children`` -- list or tuple or more generally any iterable
      of trees or object convertible to trees
    - ``label`` -- any Sage object (default: ``None``)

    EXAMPLES::

        sage: x = LabelledOrderedTree([], label = 3); x
        3[]
        sage: LabelledOrderedTree([x, x, x], label = 2)
        2[3[], 3[], 3[]]
        sage: LabelledOrderedTree((x, x, x), label = 2)
        2[3[], 3[], 3[]]
        sage: LabelledOrderedTree([[],[[], []]], label = 3)
        3[None[], None[None[], None[]]]
    """
    @staticmethod
    def __classcall_private__(cls, *args, **opts):
        """
        Ensure that trees created by the sets and directly are the same and
        that they are instances of :class:`LabelledOrderedTree`

        TESTS::

            sage: issubclass(LabelledOrderedTrees().element_class, LabelledOrderedTree)
            True
            sage: t0 = LabelledOrderedTree([[],[[], []]], label = 3)
            sage: t0.parent()
            Labelled ordered trees
            sage: type(t0)
            <class 'sage.combinat.ordered_tree.LabelledOrderedTrees_with_category.element_class'>
        """
    __hash__: Incomplete
    def left_right_symmetry(self):
        """
        Return the symmetric tree of ``self``.

        The symmetric tree `s(T)` of a labelled ordered tree `T` is
        defined as follows:
        If `T` is a labelled ordered tree with children
        `C_1, C_2, \\ldots, C_k` (listed from left to right), then the
        symmetric tree `s(T)` of `T` is a labelled ordered tree with
        children `s(C_k), s(C_{k-1}), \\ldots, s(C_1)` (from left to
        right), and with the same root label as `T`.

        .. NOTE::

            If you have a subclass of :meth:`LabelledOrderedTree`
            which also inherits from another subclass of
            :meth:`OrderedTree` which does not come with a labelling,
            then (depending on the method resolution order) it might
            happen that this method gets overridden by an
            implementation from that other subclass, and thus forgets
            about the labels. In this case you need to manually
            override this method on your subclass.

        EXAMPLES::

            sage: L2 = LabelledOrderedTree([], label=2)
            sage: L3 = LabelledOrderedTree([], label=3)
            sage: T23 = LabelledOrderedTree([L2, L3], label=4)
            sage: T23.left_right_symmetry()
            4[3[], 2[]]
            sage: T223 = LabelledOrderedTree([L2, T23], label=17)
            sage: T223.left_right_symmetry()
            17[4[3[], 2[]], 2[]]
            sage: T223.left_right_symmetry().left_right_symmetry() == T223
            True
        """
    def sort_key(self):
        """
        Return a tuple of nonnegative integers encoding the labelled
        tree ``self``.

        The first entry of the tuple is a pair consisting of the
        number of children of the root and the label of the root. Then
        the rest of the tuple is the concatenation of the tuples
        associated to these children (we view the children of
        a tree as trees themselves) from left to right.

        This tuple characterizes the labelled tree uniquely, and can
        be used to sort the labelled ordered trees provided that the
        labels belong to a type which is totally ordered.

        .. WARNING::

            This method overrides :meth:`OrderedTree.sort_key`
            and returns a result different from what the latter
            would return, as it wants to encode the whole labelled
            tree including its labelling rather than just the
            unlabelled tree. Therefore, be careful with using this
            method on subclasses of :class:`LabelledOrderedTree`;
            under some circumstances they could inherit it from
            another superclass instead of from :class:`OrderedTree`,
            which would cause the method to forget the labelling.
            See the docstring of :meth:`OrderedTree.sort_key`.

        EXAMPLES::

            sage: L2 = LabelledOrderedTree([], label=2)
            sage: L3 = LabelledOrderedTree([], label=3)
            sage: T23 = LabelledOrderedTree([L2, L3], label=4)
            sage: T23.sort_key()
            ((2, 4), (0, 2), (0, 3))
            sage: T32 = LabelledOrderedTree([L3, L2], label=5)
            sage: T32.sort_key()
            ((2, 5), (0, 3), (0, 2))
            sage: T23322 = LabelledOrderedTree([T23, T32, L2], label=14)
            sage: T23322.sort_key()
            ((3, 14), (2, 4), (0, 2), (0, 3), (2, 5), (0, 3), (0, 2), (0, 2))
        """

class LabelledOrderedTrees(UniqueRepresentation, Parent):
    """
    This is a parent stub to serve as a factory class for trees with various
    label constraints.

    EXAMPLES::

        sage: LOT = LabelledOrderedTrees(); LOT
        Labelled ordered trees
        sage: x = LOT([], label = 3); x
        3[]
        sage: x.parent() is LOT
        True
        sage: y = LOT([x, x, x], label = 2); y
        2[3[], 3[], 3[]]
        sage: y.parent() is LOT
        True
    """
    def __init__(self, category=None) -> None:
        """
        TESTS::

            sage: TestSuite(LabelledOrderedTrees()).run()
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: LabelledOrderedTrees().cardinality()
            +Infinity
        """
    def unlabelled_trees(self):
        """
        Return the set of unlabelled trees associated to ``self``.

        This is the set of ordered trees, since ``self`` is the set of
        labelled ordered trees.

        EXAMPLES::

            sage: LabelledOrderedTrees().unlabelled_trees()
            Ordered trees
        """
    def labelled_trees(self):
        """
        Return the set of labelled trees associated to ``self``.

        This is precisely ``self``, because ``self`` already is the set
        of labelled ordered trees.

        EXAMPLES::

            sage: LabelledOrderedTrees().labelled_trees()
            Labelled ordered trees
            sage: LOT = LabelledOrderedTrees()
            sage: x = LOT([], label = 3)
            sage: y = LOT([x, x, x], label = 2)
            sage: y.canonical_labelling()
            1[2[], 3[], 4[]]
        """
    Element = LabelledOrderedTree
