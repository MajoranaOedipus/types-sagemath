from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.structure.list_clone import ClonableArray as ClonableArray

class AbstractTree:
    '''
    Abstract Tree.

    There is no data structure defined here, as this class is meant to be
    extended, not instantiated.

    .. rubric:: How should this class be extended?

    A class extending :class:`AbstractTree
    <sage.combinat.abstract_tree.AbstractTree>` should respect several
    assumptions:

    * For a tree ``T``, the call ``iter(T)`` should return an iterator on the
      children of the root ``T``.

    * The :meth:`canonical_labelling
      <AbstractTree.canonical_labelling>` method
      should return the same value for trees that are considered equal (see the
      "canonical labellings" section in the documentation of the
      :class:`AbstractTree <sage.combinat.abstract_tree.AbstractTree>` class).

    * For a tree ``T`` the call ``T.parent().labelled_trees()`` should return
      a parent for labelled trees of the same kind: for example,

      - if ``T`` is a binary tree, ``T.parent()`` is ``BinaryTrees()`` and
        ``T.parent().labelled_trees()`` is ``LabelledBinaryTrees()``

      - if ``T`` is an ordered tree, ``T.parent()`` is ``OrderedTrees()`` and
        ``T.parent().labelled_trees()`` is ``LabelledOrderedTrees()``

    TESTS::

        sage: TestSuite(OrderedTree()).run()
        sage: TestSuite(BinaryTree()).run()
    '''
    def pre_order_traversal_iter(self) -> Generator[Incomplete, Incomplete]:
        """
        The depth-first pre-order traversal iterator.

        This method iters each node following the depth-first pre-order
        traversal algorithm (recursive implementation). The algorithm
        is::

            yield the root (in the case of binary trees, if it is not
                a leaf);
            then explore each subtree (by the algorithm) from the
                leftmost one to the rightmost one.

        EXAMPLES:

        For example, on the following binary tree `b`::

            |   ___3____      |
            |  /        \\     |
            | 1         _7_   |
            |  \\       /   \\  |
            |   2     5     8 |
            |        / \\      |
            |       4   6     |

        (only the nodes shown), the depth-first pre-order traversal
        algorithm explores `b` in the following order of nodes:
        `3,1,2,7,5,4,6,8`.

        Another example::

            |     __1____ |
            |    /  /   / |
            |   2  6   8_ |
            |   |  |  / / |
            |   3_ 7 9 10 |
            |  / /        |
            | 4 5         |

        The algorithm explores this labelled tree in the following
        order: `1,2,3,4,5,6,7,8,9,10`.

        TESTS::

            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: ascii_art([b])
            [   ___3____      ]
            [  /        \\     ]
            [ 1         _7_   ]
            [  \\       /   \\  ]
            [   2     5     8 ]
            [        / \\      ]
            [       4   6     ]
            sage: [n.label() for n in b.pre_order_traversal_iter()]
            [3, 1, 2, 7, 5, 4, 6, 8]

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).canonical_labelling()
            sage: ascii_art([t])
            [     __1____   ]
            [    /  /   /   ]
            [   2  6   8_   ]
            [   |  |  / /   ]
            [   3_ 7 9 10   ]
            [  / /          ]
            [ 4 5           ]
            sage: [n.label() for n in t.pre_order_traversal_iter()]
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            sage: [n for n in BinaryTree(None).pre_order_traversal_iter()]
            []

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = [1 for i in t.pre_order_traversal_iter()]
            sage: len(l)
            7
        """
    def iterative_pre_order_traversal(self, action=None) -> None:
        """
        Run the depth-first pre-order traversal algorithm (iterative
        implementation) and subject every node encountered
        to some procedure ``action``. The algorithm is::

            manipulate the root with function `action` (in the case
                of a binary tree, only if the root is not a leaf);
            then explore each subtree (by the algorithm) from the
                leftmost one to the rightmost one.

        INPUT:

        - ``action`` -- (optional) a function which takes a node as
          input, and does something during the exploration

        OUTPUT:

        ``None``. (This is *not* an iterator.)

        .. SEEALSO::

            - :meth:`~sage.combinat.abstract_tree.AbstractTree.pre_order_traversal_iter()`
            - :meth:`~sage.combinat.abstract_tree.AbstractTree.pre_order_traversal()`

        TESTS::

            sage: l = []
            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: b
            3[1[., 2[., .]], 7[5[4[., .], 6[., .]], 8[., .]]]
            sage: b.iterative_pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [3, 1, 2, 7, 5, 4, 6, 8]

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).canonical_labelling()
            sage: t
            1[2[3[4[], 5[]]], 6[7[]], 8[9[], 10[]]]
            sage: l = []
            sage: t.iterative_pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: l = []

            sage: BinaryTree().canonical_labelling().\\\n            ....:     pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            []
            sage: OrderedTree([]).canonical_labelling().\\\n            ....:     iterative_pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [1]

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = []
            sage: t.iterative_pre_order_traversal(lambda node: l.append(1))
            sage: len(l)
            7
        """
    def pre_order_traversal(self, action=None) -> None:
        """
        Run the depth-first pre-order traversal algorithm (recursive
        implementation) and subject every node encountered
        to some procedure ``action``. The algorithm is::

            manipulate the root with function `action` (in the case
                of a binary tree, only if the root is not a leaf);
            then explore each subtree (by the algorithm) from the
                leftmost one to the rightmost one.

        INPUT:

        - ``action`` -- (optional) a function which takes a node as
          input, and does something during the exploration

        OUTPUT:

        ``None``. (This is *not* an iterator.)

        EXAMPLES:

        For example, on the following binary tree `b`::

            |   ___3____      |
            |  /        \\     |
            | 1         _7_   |
            |  \\       /   \\  |
            |   2     5     8 |
            |        / \\      |
            |       4   6     |

        the depth-first pre-order traversal algorithm explores `b` in the
        following order of nodes: `3,1,2,7,5,4,6,8`.

        Another example::

            |     __1____ |
            |    /  /   / |
            |   2  6   8_ |
            |   |  |  / / |
            |   3_ 7 9 10 |
            |  / /        |
            | 4 5         |

        The algorithm explores this tree in the following order:
        `1,2,3,4,5,6,7,8,9,10`.

        .. SEEALSO::

            - :meth:`~sage.combinat.abstract_tree.AbstractTree.pre_order_traversal_iter()`
            - :meth:`~sage.combinat.abstract_tree.AbstractTree.iterative_pre_order_traversal()`

        TESTS::

            sage: l = []
            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: b
            3[1[., 2[., .]], 7[5[4[., .], 6[., .]], 8[., .]]]
            sage: b.pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [3, 1, 2, 7, 5, 4, 6, 8]
            sage: li = []
            sage: b.iterative_pre_order_traversal(lambda node: li.append(node.label()))
            sage: l == li
            True

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).canonical_labelling()
            sage: t
            1[2[3[4[], 5[]]], 6[7[]], 8[9[], 10[]]]
            sage: l = []
            sage: t.pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: li = []
            sage: t.iterative_pre_order_traversal(lambda node: li.append(node.label()))
            sage: l == li
            True

            sage: l = []
            sage: BinaryTree().canonical_labelling().\\\n            ....:     pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            []
            sage: OrderedTree([]).canonical_labelling().\\\n            ....:     pre_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [1]

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = []
            sage: t.pre_order_traversal(lambda node: l.append(1))
            sage: len(l)
            7
        """
    def post_order_traversal_iter(self) -> Generator[Incomplete, Incomplete]:
        """
        The depth-first post-order traversal iterator.

        This method iters each node following the depth-first post-order
        traversal algorithm (recursive implementation). The algorithm
        is::

            explore each subtree (by the algorithm) from the
                leftmost one to the rightmost one;
            then yield the root (in the case of binary trees, only if
                it is not a leaf).

        EXAMPLES:

        For example on the following binary tree `b`::

            |   ___3____      |
            |  /        \\     |
            | 1         _7_   |
            |  \\       /   \\  |
            |   2     5     8 |
            |        / \\      |
            |       4   6     |

        (only the nodes are shown), the depth-first post-order traversal
        algorithm explores `b` in the following order of nodes:
        `2,1,4,6,5,8,7,3`.

        For another example, consider the labelled tree::

            |     __1____ |
            |    /  /   / |
            |   2  6   8_ |
            |   |  |  / / |
            |   3_ 7 9 10 |
            |  / /        |
            | 4 5         |

        The algorithm explores this tree in the following order:
        `4,5,3,2,7,6,9,10,8,1`.

        TESTS::

            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: ascii_art([b])
            [   ___3____      ]
            [  /        \\     ]
            [ 1         _7_   ]
            [  \\       /   \\  ]
            [   2     5     8 ]
            [        / \\      ]
            [       4   6     ]
            sage: [node.label() for node in b.post_order_traversal_iter()]
            [2, 1, 4, 6, 5, 8, 7, 3]

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).canonical_labelling()
            sage: ascii_art([t])
            [     __1____   ]
            [    /  /   /   ]
            [   2  6   8_   ]
            [   |  |  / /   ]
            [   3_ 7 9 10   ]
            [  / /          ]
            [ 4 5           ]
            sage: [node.label() for node in t.post_order_traversal_iter()]
            [4, 5, 3, 2, 7, 6, 9, 10, 8, 1]

            sage: [node.label() for node in BinaryTree().canonical_labelling().\\\n            ....:     post_order_traversal_iter()]
            []
            sage: [node.label() for node in OrderedTree([]).\\\n            ....:     canonical_labelling().post_order_traversal_iter()]
            [1]

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = [1 for i in t.post_order_traversal_iter()]
            sage: len(l)
            7
        """
    def post_order_traversal(self, action=None) -> None:
        """
        Run the depth-first post-order traversal algorithm (recursive
        implementation) and subject every node encountered
        to some procedure ``action``. The algorithm is::

            explore each subtree (by the algorithm) from the
                leftmost one to the rightmost one;
            then manipulate the root with function `action` (in the
                case of a binary tree, only if the root is not a leaf).

        INPUT:

        - ``action`` -- (optional) a function which takes a node as
          input, and does something during the exploration

        OUTPUT:

        ``None``. (This is *not* an iterator.)

        .. SEEALSO::

            - :meth:`~sage.combinat.abstract_tree.AbstractTree.post_order_traversal_iter()`
            - :meth:`~sage.combinat.abstract_tree.AbstractTree.iterative_post_order_traversal()`

        TESTS::

            sage: l = []
            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: b
            3[1[., 2[., .]], 7[5[4[., .], 6[., .]], 8[., .]]]
            sage: b.post_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [2, 1, 4, 6, 5, 8, 7, 3]

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).\\\n            ....:     canonical_labelling(); t
            1[2[3[4[], 5[]]], 6[7[]], 8[9[], 10[]]]
            sage: l = []
            sage: t.post_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [4, 5, 3, 2, 7, 6, 9, 10, 8, 1]

            sage: l = []
            sage: BinaryTree().canonical_labelling().\\\n            ....:     post_order_traversal(lambda node: l.append(node.label()))
            sage: l
            []
            sage: OrderedTree([]).canonical_labelling().\\\n            ....:     post_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [1]

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = []
            sage: t.post_order_traversal(lambda node: l.append(1))
            sage: len(l)
            7
        """
    def iterative_post_order_traversal(self, action=None) -> None:
        """
        Run the depth-first post-order traversal algorithm (iterative
        implementation) and subject every node encountered
        to some procedure ``action``. The algorithm is::

            explore each subtree (by the algorithm) from the
                leftmost one to the rightmost one;
            then manipulate the root with function `action` (in the
                case of a binary tree, only if the root is not a leaf).

        INPUT:

        - ``action`` -- (optional) a function which takes a node as
          input, and does something during the exploration

        OUTPUT:

        ``None``. (This is *not* an iterator.)

        .. SEEALSO::

            - :meth:`~sage.combinat.abstract_tree.AbstractTree.post_order_traversal_iter()`

        TESTS::

            sage: l = []
            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: b
            3[1[., 2[., .]], 7[5[4[., .], 6[., .]], 8[., .]]]
            sage: b.iterative_post_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [2, 1, 4, 6, 5, 8, 7, 3]

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).canonical_labelling()
            sage: t
            1[2[3[4[], 5[]]], 6[7[]], 8[9[], 10[]]]
            sage: l = []
            sage: t.iterative_post_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [4, 5, 3, 2, 7, 6, 9, 10, 8, 1]

            sage: l = []
            sage: BinaryTree().canonical_labelling().\\\n            ....:     iterative_post_order_traversal(
            ....:         lambda node: l.append(node.label()))
            sage: l
            []
            sage: OrderedTree([]).canonical_labelling().\\\n            ....:     iterative_post_order_traversal(
            ....:         lambda node: l.append(node.label()))
            sage: l
            [1]

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = []
            sage: t.iterative_post_order_traversal(lambda node: l.append(1))
            sage: len(l)
            7
        """
    def contour_traversal(self, first_action=None, middle_action=None, final_action=None, leaf_action=None) -> None:
        """
        Run the counterclockwise contour traversal algorithm (iterative
        implementation) and subject every node encountered
        to some procedure ``first_action``, ``middle_action`` or ``final_action`` each time it reaches it.

        ALGORITHM:

        - if the root is a leaf, apply `leaf_action`
        - else
            -  apply `first_action` to the root
            - iteratively apply `middle_action` to the root and traverse each subtree
              from the leftmost one to the rightmost one
            - apply `final_action` to the root

        INPUT:

        - ``first_action`` -- (optional) a function which takes a node as
          input, and does something the first time it is reached during exploration

        - ``middle_action`` -- (optional) a function which takes a node as
          input, and does something each time it explore one of its children

        - ``final_action`` -- (optional) a function which takes a node as
          input, and does something the last time it is reached during exploration

        - ``leaf_action`` -- (optional) a function which takes a leaf as
          input, and does something when it is reached during exploration.

        OUTPUT:

        ``None``. (This is *not* an iterator.)

        TESTS::

            sage: l = []
            sage: t = OrderedTree([[],[[],[],]]).canonical_labelling()
            sage: t
            1[2[], 3[4[], 5[]]]
            sage: t.contour_traversal(lambda node: (l.append(node.label()),l.append('a')),
            ....:   lambda node: (l.append(node.label()),l.append('b')),
            ....:   lambda node: (l.append(node.label()),l.append('c')),
            ....:   lambda node: (l.append(node.label())))
            sage: l
            [1, 'a', 1, 'b', 2, 1, 'b', 3, 'a', 3, 'b', 4, 3, 'b', 5, 3, 'c', 1, 'c']

            sage: l = []
            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: b
            3[1[., 2[., .]], 7[5[4[., .], 6[., .]], 8[., .]]]
            sage: b.contour_traversal(lambda node: l.append(node.label()),
            ....:   lambda node: l.append(node.label()),
            ....:   lambda node: l.append(node.label()),
            ....:   None)
            sage: l
            [3, 3, 1, 1, 1, 2, 2, 2, 2, 1, 3, 7, 7, 5, 5, 4, 4, 4, 4, 5, 6, 6, 6, 6, 5, 7, 8, 8, 8, 8, 7, 3]

        The following test checks that things do not go wrong if some among
        the descendants of the tree are equal or even identical::

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([v, v])
            sage: t = BinaryTree([w, w])
            sage: t.node_number()
            7
            sage: l = []
            sage: t.contour_traversal(first_action = lambda node: l.append(0))
            sage: len(l)
            7
        """
    def breadth_first_order_traversal(self, action=None) -> None:
        """
        Run the breadth-first post-order traversal algorithm
        and subject every node encountered to some procedure
        ``action``. The algorithm is::

            queue <- [ root ];
            while the queue is not empty:
                node <- pop( queue );
                manipulate the node;
                prepend to the queue the list of all subtrees of
                    the node (from the rightmost to the leftmost).

        INPUT:

        - ``action`` -- (optional) a function which takes a node as
          input, and does something during the exploration

        OUTPUT:

        ``None``. (This is *not* an iterator.)

        EXAMPLES:

        For example, on the following binary tree `b`::

            |   ___3____      |
            |  /        \\     |
            | 1         _7_   |
            |  \\       /   \\  |
            |   2     5     8 |
            |        / \\      |
            |       4   6     |

        the breadth-first order traversal algorithm explores `b` in the
        following order of nodes: `3,1,7,2,5,8,4,6`.

        TESTS::

            sage: b = BinaryTree([[None,[]],[[[],[]],[]]]).canonical_labelling()
            sage: l = []
            sage: b.breadth_first_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [3, 1, 7, 2, 5, 8, 4, 6]

            sage: t = OrderedTree([[[[],[]]],[[]],[[],[]]]).canonical_labelling()
            sage: t
            1[2[3[4[], 5[]]], 6[7[]], 8[9[], 10[]]]
            sage: l = []
            sage: t.breadth_first_order_traversal(lambda node: l.append(node.label()))
            sage: l
            [1, 2, 6, 8, 3, 7, 9, 10, 4, 5]

            sage: l = []
            sage: BinaryTree().canonical_labelling().\\\n            ....:     breadth_first_order_traversal(
            ....:         lambda node: l.append(node.label()))
            sage: l
            []
            sage: OrderedTree([]).canonical_labelling().\\\n            ....:     breadth_first_order_traversal(
            ....:         lambda node: l.append(node.label()))
            sage: l
            [1]
        """
    def paths_at_depth(self, depth, path=[]) -> Generator[Incomplete, Incomplete]:
        """
        Return a generator for all paths at a fixed depth.

        This iterates over all paths for nodes that are at the given depth.

        Here the root is considered to have depth 0.

        INPUT:

        - ``depth`` -- integer
        - ``path`` -- (optional) list; given path used in the recursion

        .. WARNING::

            The ``path`` option should not be used directly.

        .. SEEALSO::

            :meth:`paths`, :meth:`paths_to_the_right`, :meth:`node_number_at_depth`

        EXAMPLES::

            sage: T = OrderedTree([[[], [[], [[]]]], [], [[[],[]]], [], []])
            sage: ascii_art(T)
                 ______o_______
                /    /   /  / /
              _o__  o   o  o o
             /   /      |
            o   o_      o_
               / /     / /
              o o     o o
                |
                o
            sage: list(T.paths_at_depth(0))
            [()]
            sage: list(T.paths_at_depth(2))
            [(0, 0), (0, 1), (2, 0)]
            sage: list(T.paths_at_depth(4))
            [(0, 1, 1, 0)]
            sage: list(T.paths_at_depth(5))
            []

            sage: T2 = OrderedTree([])
            sage: list(T2.paths_at_depth(0))
            [()]
        """
    def node_number_at_depth(self, depth):
        """
        Return the number of nodes at a given depth.

        This counts all nodes that are at the given depth.

        Here the root is considered to have depth 0.

        INPUT:

        - ``depth`` -- integer

        .. SEEALSO::

            :meth:`node_number`, :meth:`node_number_to_the_right`, :meth:`paths_at_depth`

        EXAMPLES::

            sage: T = OrderedTree([[[], [[]]], [[], [[[]]]], []])
            sage: ascii_art(T)
                ___o____
               /    /  /
              o_   o_ o
             / /  / /
            o o  o o
              |    |
              o    o
                   |
                   o
            sage: [T.node_number_at_depth(i) for i in range(6)]
            [1, 3, 4, 2, 1, 0]

        TESTS:

        Check that the empty tree has no nodes (:issue:`29134`)::

            sage: T = BinaryTree()
            sage: T
            .
            sage: T.is_empty()
            True
            sage: [T.node_number_at_depth(i) for i in range(3)]
            [0, 0, 0]

        Check that we do not hit a recursion limit::

            sage: T = OrderedTree([])
            sage: for _ in range(9999):
            ....:     T = OrderedTree([T])
            sage: T.node_number_at_depth(2000)
            1
        """
    def paths_to_the_right(self, path) -> Generator[Incomplete]:
        """
        Return a generator of paths for all nodes at the same
        depth and to the right of the node identified by ``path``.

        This iterates over the paths for nodes that are at the same
        depth as the given one, and strictly to its right.

        INPUT:

        - ``path`` -- any path in the tree

        .. SEEALSO::

            :meth:`paths`, :meth:`paths_at_depth`, :meth:`node_number_to_the_right`

        EXAMPLES::

            sage: T = OrderedTree([[[], [[]]], [[], [[[]]]], []])
            sage: ascii_art(T)
                ___o____
               /    /  /
              o_   o_ o
             / /  / /
            o o  o o
              |    |
              o    o
                   |
                   o
            sage: g = T.paths_to_the_right(())
            sage: list(g)
            []

            sage: g = T.paths_to_the_right((0,))
            sage: list(g)
            [(1,), (2,)]

            sage: g = T.paths_to_the_right((0,1))
            sage: list(g)
            [(1, 0), (1, 1)]

            sage: g = T.paths_to_the_right((0,1,0))
            sage: list(g)
            [(1, 1, 0)]

            sage: g = T.paths_to_the_right((1,2))
            sage: list(g)
            []
        """
    def node_number_to_the_right(self, path):
        """
        Return the number of nodes at the same depth and to the right of
        the node identified by ``path``.

        This counts the nodes that are at the same depth as the given
        one, and strictly to its right.

        .. SEEALSO::

            :meth:`node_number`, :meth:`node_number_at_depth`, :meth:`paths_to_the_right`

        EXAMPLES::

            sage: T = OrderedTree([[[], [[]]], [[], [[[]]]], []])
            sage: ascii_art(T)
                ___o____
               /    /  /
              o_   o_ o
             / /  / /
            o o  o o
              |    |
              o    o
                   |
                   o
            sage: T.node_number_to_the_right(())
            0
            sage: T.node_number_to_the_right((0,))
            2
            sage: T.node_number_to_the_right((0,1))
            2
            sage: T.node_number_to_the_right((0,1,0))
            1

            sage: T = OrderedTree([])
            sage: T.node_number_to_the_right(())
            0
        """
    def subtrees(self):
        '''
        Return a generator for all nonempty subtrees of ``self``.

        The number of nonempty subtrees of a tree is its number of
        nodes. (The word "nonempty" makes a difference only in the
        case of binary trees. For ordered trees, for example, all
        trees are nonempty.)

        EXAMPLES::

            sage: list(OrderedTree([]).subtrees())
            [[]]
            sage: list(OrderedTree([[],[[]]]).subtrees())
            [[[], [[]]], [], [[]], []]

            sage: list(OrderedTree([[],[[]]]).canonical_labelling().subtrees())
            [1[2[], 3[4[]]], 2[], 3[4[]], 4[]]

            sage: list(BinaryTree([[],[[],[]]]).subtrees())
            [[[., .], [[., .], [., .]]], [., .], [[., .], [., .]], [., .], [., .]]

            sage: v = BinaryTree([[],[]])
            sage: list(v.canonical_labelling().subtrees())
            [2[1[., .], 3[., .]], 1[., .], 3[., .]]

        TESTS::

            sage: t = OrderedTree([[], [[], [[], []], [[], []]], [[], []]])
            sage: t.node_number() == len(list(t.subtrees()))
            True
            sage: list(BinaryTree().subtrees())
            []
            sage: bt = BinaryTree([[],[[],[]]])
            sage: bt.node_number() == len(list(bt.subtrees()))
            True
        '''
    def paths(self) -> Generator[Incomplete]:
        """
        Return a generator for all paths to nodes of ``self``.

        OUTPUT:

        This method returns a list of sequences of integers. Each of these
        sequences represents a path from the root node to some node. For
        instance, `(1, 3, 2, 5, 0, 3)` represents the node obtained by
        choosing the 1st child of the root node (in the ordering returned
        by ``iter``), then the 3rd child of its child, then the 2nd child
        of the latter, etc. (where the labelling of the children is
        zero-based).

        The root element is represented by the empty tuple ``()``.

        .. SEEALSO::

            :meth:`paths_at_depth`, :meth:`paths_to_the_right`

        EXAMPLES::

            sage: list(OrderedTree([]).paths())
            [()]
            sage: list(OrderedTree([[],[[]]]).paths())
            [(), (0,), (1,), (1, 0)]

            sage: list(BinaryTree([[],[[],[]]]).paths())
            [(), (0,), (1,), (1, 0), (1, 1)]

        TESTS::

            sage: t = OrderedTree([[], [[], [[], []], [[], []]], [[], []]])
            sage: t.node_number() == len(list(t.paths()))
            True
            sage: list(BinaryTree().paths())
            []
            sage: bt = BinaryTree([[],[[],[]]])
            sage: bt.node_number() == len(list(bt.paths()))
            True
        """
    def node_number(self):
        """
        Return the number of nodes of ``self``.

        .. SEEALSO::

            :meth:`node_number_at_depth`, :meth:`node_number_to_the_right`

        EXAMPLES::

            sage: OrderedTree().node_number()
            1
            sage: OrderedTree([]).node_number()
            1
            sage: OrderedTree([[],[]]).node_number()
            3
            sage: OrderedTree([[],[[]]]).node_number()
            4
            sage: OrderedTree([[], [[], [[], []], [[], []]], [[], []]]).node_number()
            13

        EXAMPLES::

            sage: BinaryTree(None).node_number()
            0
            sage: BinaryTree([]).node_number()
            1
            sage: BinaryTree([[], None]).node_number()
            2
            sage: BinaryTree([[None, [[], []]], None]).node_number()
            5

        TESTS:

        Check that we do not hit a recursion limit::

            sage: T = OrderedTree([])
            sage: for _ in range(9999):
            ....:     T = OrderedTree([T])
            sage: T.node_number()
            10000
        """
    def depth(self):
        """
        Return the depth of ``self``.

        EXAMPLES::

            sage: OrderedTree().depth()
            1
            sage: OrderedTree([]).depth()
            1
            sage: OrderedTree([[],[]]).depth()
            2
            sage: OrderedTree([[],[[]]]).depth()
            3
            sage: OrderedTree([[], [[], [[], []], [[], []]], [[], []]]).depth()
            4

            sage: BinaryTree().depth()
            0
            sage: BinaryTree([[],[[],[]]]).depth()
            3

        TESTS:

        Check that we do not hit a recursion limit::

            sage: T = OrderedTree([])
            sage: for _ in range(9999):
            ....:     T = OrderedTree([T])
            sage: T.depth()
            10000
        """
    def canonical_labelling(self, shift: int = 1):
        """
        Return a labelled version of ``self``.

        The actual canonical labelling is currently unspecified. However, it
        is guaranteed to have labels in `1...n` where `n` is the number of
        nodes of the tree. Moreover, two (unlabelled) trees compare as equal if
        and only if their canonical labelled trees compare as equal.

        EXAMPLES::

            sage: t = OrderedTree([[], [[], [[], []], [[], []]], [[], []]])
            sage: t.canonical_labelling()
            1[2[], 3[4[], 5[6[], 7[]], 8[9[], 10[]]], 11[12[], 13[]]]

            sage: BinaryTree([]).canonical_labelling()
            1[., .]
            sage: BinaryTree([[],[[],[]]]).canonical_labelling()
            2[1[., .], 4[3[., .], 5[., .]]]

        TESTS::

            sage: BinaryTree().canonical_labelling()
            .
        """
    def to_hexacode(self):
        """
        Transform a tree into a hexadecimal string.

        The definition of the hexacode is recursive. The first letter is
        the valence of the root as a hexadecimal (up to 15), followed by
        the concatenation of the hexacodes of the subtrees.

        This method only works for trees where every vertex has
        valency at most 15.

        See :func:`from_hexacode` for the reverse transformation.

        EXAMPLES::

            sage: from sage.combinat.abstract_tree import from_hexacode
            sage: LT = LabelledOrderedTrees()
            sage: from_hexacode('2010', LT).to_hexacode()
            '2010'
            sage: LT.an_element().to_hexacode()
            '3020010'
            sage: t = from_hexacode('a0000000000000000', LT)
            sage: t.to_hexacode()
            'a0000000000'

            sage: OrderedTrees(6).an_element().to_hexacode()
            '500000'

        TESTS::

            sage: one = LT([], label='@')
            sage: LT([one for _ in range(15)], label='@').to_hexacode()
            'f000000000000000'
            sage: LT([one for _ in range(16)], label='@').to_hexacode()
            Traceback (most recent call last):
            ...
            ValueError: the width of the tree is too large
        """
    def tree_factorial(self):
        """
        Return the tree-factorial of ``self``.

        Definition:

        The tree-factorial `T!` of a tree `T` is the product `\\prod_{v\\in
        T}\\#\\mbox{children}(v)`.

        EXAMPLES::

            sage: LT = LabelledOrderedTrees()
            sage: t = LT([LT([],label=6),LT([],label=1)],label=9)
            sage: t.tree_factorial()
            3

            sage: BinaryTree([[],[[],[]]]).tree_factorial()
            15

        TESTS::

            sage: BinaryTree().tree_factorial()
            1
        """

class AbstractClonableTree(AbstractTree):
    """
    Abstract Clonable Tree.

    An abstract class for trees with clone protocol (see
    :mod:`~sage.structure.list_clone`). It is expected that classes extending
    this one may also inherit from classes like :class:`~sage.structure.list_clone.ClonableArray` or
    :class:`~sage.structure.list_clone.ClonableList` depending whether one
    wants to build trees where adding a child is allowed.

    .. NOTE:: Due to the limitation of Cython inheritance, one cannot inherit
       here from :class:`~sage.structure.list_clone.ClonableElement`, because
       it would prevent us from later inheriting from
       :class:`~sage.structure.list_clone.ClonableArray` or
       :class:`~sage.structure.list_clone.ClonableList`.

    .. rubric:: How should this class be extended ?

    A class extending :class:`AbstractClonableTree
    <sage.combinat.abstract_tree.AbstractClonableTree>` should satisfy the
    following assumptions:

    * An instantiable class extending :class:`AbstractClonableTree
      <sage.combinat.abstract_tree.AbstractClonableTree>` should also extend
      the :class:`ClonableElement <sage.structure.list_clone.ClonableElement>`
      class or one of its subclasses generally, at least :class:`ClonableArray
      <sage.structure.list_clone.ClonableArray>`.

    * To respect the Clone protocol, the :meth:`AbstractClonableTree.check`
      method should be overridden by the new class.

    See also the assumptions in :class:`AbstractTree`.
    """
    def check(self) -> None:
        """
        Check that ``self`` is a correct tree.

        This method does nothing. It is implemented here because many
        extensions of :class:`AbstractClonableTree
        <sage.combinat.abstract_tree.AbstractClonableTree>` also extend
        :class:`sage.structure.list_clone.ClonableElement`, which requires it.

        It should be overridden in subclasses in order to check that the
        characterizing property of the respective kind of tree holds (eg: two
        children for binary trees).

        EXAMPLES::

            sage: OrderedTree([[],[[]]]).check()
            sage: BinaryTree([[],[[],[]]]).check()
        """
    def __setitem__(self, idx, value) -> None:
        """
        Substitute a subtree.

        .. NOTE::

            The tree ``self`` must be in a mutable state. See
            :mod:`sage.structure.list_clone` for more details about
            mutability.  The default implementation here assume that the
            container of the node implement a method ``_setitem`` with signature
            `self._setitem(idx, value)`. It is usually provided by inheriting
            from :class:`~sage.structure.list_clone.ClonableArray`.

        INPUT:

        - ``idx`` -- a valid path in ``self`` identifying a node

        - ``value`` -- the tree to be substituted

        EXAMPLES:

        Trying to modify a non mutable tree raises an error::

            sage: x = OrderedTree([])
            sage: x[0] =  OrderedTree([[]])
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.

        Here is the correct way to do it::

            sage: x = OrderedTree([[],[[]]])
            sage: with x.clone() as x:
            ....:     x[0] = OrderedTree([[]])
            sage: x
            [[[]], [[]]]

        One can also substitute at any depth::

            sage: y = OrderedTree(x)
            sage: with x.clone() as x:
            ....:     x[0,0] = OrderedTree([[]])
            sage: x
            [[[[]]], [[]]]
            sage: y
            [[[]], [[]]]
            sage: with y.clone() as y:
            ....:     y[(0,)] = OrderedTree([])
            sage: y
            [[], [[]]]

        This works for binary trees as well::

            sage: bt = BinaryTree([[],[[],[]]]); bt
            [[., .], [[., .], [., .]]]
            sage: with bt.clone() as bt1:
            ....:     bt1[0,0] = BinaryTree([[[], []], None])
            sage: bt1
            [[[[[., .], [., .]], .], .], [[., .], [., .]]]

        TESTS::

            sage: x = OrderedTree([])
            sage: with x.clone() as x:
            ....:     x[0] = OrderedTree([[]])
            Traceback (most recent call last):
            ...
            IndexError: list assignment index out of range

            sage: x = OrderedTree([]); x = OrderedTree([x,x]); x = OrderedTree([x,x]); x = OrderedTree([x,x])
            sage: with x.clone() as x:
            ....:     x[0,0] = OrderedTree()
            sage: x
            [[[], [[], []]], [[[], []], [[], []]]]
        """
    def __setitem_rec__(self, idx, i, value) -> None:
        """
        TESTS::

            sage: x = OrderedTree([[[], []],[[]]])
            sage: with x.clone() as x:              # indirect doctest
            ....:     x[0,1] = OrderedTree([[[]]])
            sage: x
            [[[], [[[]]]], [[]]]
        """
    def __getitem__(self, idx):
        """
        Return the ``idx``-th child of ``self`` (which is a subtree) if
        ``idx`` is an integer, or the ``idx[n-1]``-th child of the
        ``idx[n-2]``-th child of the ... of the ``idx[0]``-th child of
        ``self`` if ``idx`` is a list (or iterable) of length `n`.

        The indexing of the children is zero-based.

        INPUT:

        - ``idx`` -- integer; or a valid path in ``self`` identifying a node

        .. NOTE::

            The default implementation here assumes that the container of the
            node inherits from
            :class:`~sage.structure.list_clone.ClonableArray`.

        EXAMPLES::

            sage: x = OrderedTree([[],[[]]])
            sage: x[1,0]
            []
            sage: x = OrderedTree([[],[[]]])
            sage: x[()]
            [[], [[]]]
            sage: x[(0,)]
            []
            sage: x[0,0]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range

            sage: u = BinaryTree(None)
            sage: v = BinaryTree([u, u])
            sage: w = BinaryTree([u, v])
            sage: t = BinaryTree([v, w])
            sage: z = BinaryTree([w, t])
            sage: z[0,1]
            [., .]
            sage: z[0,0]
            .
            sage: z[1]
            [[., .], [., [., .]]]
            sage: z[1,1]
            [., [., .]]
            sage: z[1][1,1]
            [., .]
        """

class AbstractLabelledTree(AbstractTree):
    """
    Abstract Labelled Tree.

    Typically a class for labelled trees is constructed by inheriting from
    a class for unlabelled trees and :class:`AbstractLabelledTree`.

    .. rubric:: How should this class be extended ?

    A class extending :class:`AbstractLabelledTree
    <sage.combinat.abstract_tree.AbstractLabelledTree>` should respect the
    following assumptions:

    * For a labelled tree ``T`` the call ``T.parent().unlabelled_trees()``
      should return a parent for unlabelled trees of the same kind: for
      example,

      - if ``T`` is a binary labelled tree, ``T.parent()`` is
        ``LabelledBinaryTrees()`` and ``T.parent().unlabelled_trees()`` is
        ``BinaryTrees()``

      - if ``T`` is an ordered labelled tree, ``T.parent()`` is
        ``LabelledOrderedTrees()`` and ``T.parent().unlabelled_trees()`` is
        ``OrderedTrees()``

    * In the same vein, the class of ``T`` should contain an attribute
      ``_UnLabelled`` which should be the class for the corresponding
      unlabelled trees.

    See also the assumptions in :class:`AbstractTree`.

    .. SEEALSO:: :class:`AbstractTree`
    """
    def __init__(self, parent, children, label=None, check: bool = True) -> None:
        '''
        TESTS::

            sage: LabelledOrderedTree([])
            None[]
            sage: LabelledOrderedTree([], 3)
            3[]
            sage: LT = LabelledOrderedTree
            sage: t = LT([LT([LT([], label=42), LT([], 21)])], label=1)
            sage: t
            1[None[42[], 21[]]]
            sage: LabelledOrderedTree(OrderedTree([[],[[],[]],[]]))
            None[None[], None[None[], None[]], None[]]

        We test that inheriting from `LabelledOrderedTree` allows construction from a
        `LabelledOrderedTree` (:issue:`16314`)::

            sage: LBTS = LabelledOrderedTrees()
            sage: class Foo(LabelledOrderedTree):
            ....:     def bar(self):
            ....:         print("bar called")
            sage: foo = Foo(LBTS, [], label=1); foo
            1[]
            sage: foo1 = LBTS([LBTS([], label=21)], label=42); foo1
            42[21[]]
            sage: foo2 = Foo(LBTS, foo1); foo2
            42[21[]]
            sage: foo2[0]
            21[]
            sage: foo2.__class__
            <class \'__main__.Foo\'>
            sage: foo2[0].__class__
            <class \'__main__.Foo\'>
            sage: foo2.bar()
            bar called
            sage: foo2.label()
            42
        '''
    def label(self, path=None):
        """
        Return the label of ``self``.

        INPUT:

        - ``path`` -- ``None`` (default) or a path (list or tuple of
          children index in the tree)

        OUTPUT: the label of the subtree indexed by ``path``

        EXAMPLES::

            sage: t = LabelledOrderedTree([[],[]], label = 3)
            sage: t.label()
            3
            sage: t[0].label()
            sage: t = LabelledOrderedTree([LabelledOrderedTree([], 5),[]], label = 3)
            sage: t.label()
            3
            sage: t[0].label()
            5
            sage: t[1].label()
            sage: t.label([0])
            5
        """
    def labels(self):
        """
        Return the list of labels of ``self``.

        EXAMPLES::

            sage: LT = LabelledOrderedTree
            sage: t = LT([LT([],label='b'),LT([],label='c')],label='a')
            sage: t.labels()
            ['a', 'b', 'c']

            sage: LBT = LabelledBinaryTree
            sage: LBT([LBT([],label=1),LBT([],label=4)],label=2).labels()
            [2, 1, 4]
        """
    def leaf_labels(self):
        '''
        Return the list of labels of the leaves of ``self``.

        In case of a labelled binary tree, these "leaves" are not actually
        the leaves of the binary trees, but the nodes whose both children
        are leaves!

        EXAMPLES::

            sage: LT = LabelledOrderedTree
            sage: t = LT([LT([],label=\'b\'),LT([],label=\'c\')],label=\'a\')
            sage: t.leaf_labels()
            [\'b\', \'c\']

            sage: LBT = LabelledBinaryTree
            sage: bt = LBT([LBT([],label=\'b\'),LBT([],label=\'c\')],label=\'a\')
            sage: bt.leaf_labels()
            [\'b\', \'c\']
            sage: LBT([], label=\'1\').leaf_labels()
            [\'1\']
            sage: LBT(None).leaf_labels()
            []
        '''
    def __eq__(self, other):
        """
        Test if ``self`` is equal to ``other``.

        TESTS::

            sage  LabelledOrderedTree() == LabelledOrderedTree()
            True
            sage  LabelledOrderedTree([]) == LabelledOrderedTree()
            False
            sage: t1 = LabelledOrderedTree([[],[[]]])
            sage: t2 = LabelledOrderedTree([[],[[]]])
            sage: t1 == t2
            True
            sage: t2 = LabelledOrderedTree(t1)
            sage: t1 == t2
            True
            sage: t1 = LabelledOrderedTree([[],[[]]])
            sage: t2 = LabelledOrderedTree([[[]],[]])
            sage: t1 == t2
            False
        """
    def shape(self):
        """
        Return the unlabelled tree associated to ``self``.

        EXAMPLES::

            sage: t = LabelledOrderedTree([[],[[]]], label = 25).shape(); t
            [[], [[]]]

            sage: LabelledBinaryTree([[],[[],[]]], label = 25).shape()
            [[., .], [[., .], [., .]]]

            sage: LRT = LabelledRootedTree
            sage: tb = LRT([],label='b')
            sage: LRT([tb, tb], label='a').shape()
            [[], []]

        TESTS::

            sage: t.parent()
            Ordered trees
            sage: type(t)
            <class 'sage.combinat.ordered_tree.OrderedTrees_all_with_category.element_class'>
        """
    def as_digraph(self):
        """
        Return a directed graph version of ``self``.

        .. WARNING::

            At this time, the output makes sense only if ``self`` is a
            labelled binary tree with no repeated labels and no ``None``
            labels.

        EXAMPLES::

           sage: LT = LabelledOrderedTrees()
           sage: t1 = LT([LT([],label=6),LT([],label=1)],label=9)
           sage: t1.as_digraph()
           Digraph on 3 vertices

           sage: t = BinaryTree([[None, None],[[],None]])
           sage: lt = t.canonical_labelling()
           sage: lt.as_digraph()
           Digraph on 4 vertices
        """

class AbstractLabelledClonableTree(AbstractLabelledTree, AbstractClonableTree):
    """
    Abstract Labelled Clonable Tree.

    This class takes care of modification for the label by the clone protocol.

    .. NOTE:: Due to the limitation of Cython inheritance, one cannot inherit
       here from :class:`~sage.structure.list_clone.ClonableArray`, because it would prevent us to
       inherit later from :class:`~sage.structure.list_clone.ClonableList`.
    """
    def set_root_label(self, label) -> None:
        """
        Set the label of the root of ``self``.

        INPUT:

        - ``label`` -- any Sage object

        OUTPUT: none, ``self`` is modified in place

        .. NOTE::

            ``self`` must be in a mutable state. See
            :mod:`sage.structure.list_clone` for more details about
            mutability.

        EXAMPLES::

            sage: t = LabelledOrderedTree([[],[[],[]]])
            sage: t.set_root_label(3)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with t.clone() as t:
            ....:     t.set_root_label(3)
            sage: t.label()
            3
            sage: t
            3[None[], None[None[], None[]]]

        This also works for binary trees::

            sage: bt = LabelledBinaryTree([[],[]])
            sage: bt.set_root_label(3)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with bt.clone() as bt:
            ....:     bt.set_root_label(3)
            sage: bt.label()
            3
            sage: bt
            3[None[., .], None[., .]]

        TESTS::

            sage: with t.clone() as t:
            ....:     t[0] = LabelledOrderedTree(t[0], label = 4)
            sage: t
            3[4[], None[None[], None[]]]
            sage: with t.clone() as t:
            ....:     t[1,0] = LabelledOrderedTree(t[1,0], label = 42)
            sage: t
            3[4[], None[42[], None[]]]
        """
    def set_label(self, path, label) -> None:
        """
        Change the label of subtree indexed by ``path`` to ``label``.

        INPUT:

        - ``path`` -- ``None`` (default) or a path (list or tuple of children
          index in the tree)

        - ``label`` -- any sage object

        OUTPUT: nothing, ``self`` is modified in place

        .. NOTE::

            ``self`` must be in a mutable state. See
            :mod:`sage.structure.list_clone` for more details about
            mutability.

        EXAMPLES::

            sage: t = LabelledOrderedTree([[],[[],[]]])
            sage: t.set_label((0,), 4)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: with t.clone() as t:
            ....:     t.set_label((0,), 4)
            sage: t
            None[4[], None[None[], None[]]]
            sage: with t.clone() as t:
            ....:     t.set_label((1,0), label = 42)
            sage: t
            None[4[], None[42[], None[]]]

        .. TODO::

            Do we want to implement the following syntactic sugar::

                with t.clone() as tt:
                    tt.labels[1,2] = 3 ?
        """
    def map_labels(self, f):
        """
        Apply the function `f` to the labels of ``self``.

        This method returns a copy of ``self`` on which the function `f` has
        been applied on all labels (a label `x` is replaced by `f(x)`).

        EXAMPLES::

            sage: LT = LabelledOrderedTree
            sage: t = LT([LT([],label=1),LT([],label=7)],label=3); t
            3[1[], 7[]]
            sage: t.map_labels(lambda z:z+1)
            4[2[], 8[]]

            sage: LBT = LabelledBinaryTree
            sage: bt = LBT([LBT([],label=1),LBT([],label=4)],label=2); bt
            2[1[., .], 4[., .]]
            sage: bt.map_labels(lambda z:z+1)
            3[2[., .], 5[., .]]
        """

def from_hexacode(ch, parent=None, label: str = '@'):
    """
    Transform a hexadecimal string into a tree.

    INPUT:

    - ``ch`` -- a hexadecimal string

    - ``parent`` -- kind of trees to be produced. If ``None``, this will
      be ``LabelledOrderedTrees``

    - ``label`` -- a label (default: ``'@'``) to be used for every vertex
      of the tree

    See :meth:`AbstractTree.to_hexacode` for the description of the encoding

    See :func:`_from_hexacode_aux` for the actual code

    EXAMPLES::

        sage: from sage.combinat.abstract_tree import from_hexacode
        sage: from_hexacode('12000', LabelledOrderedTrees())
        @[@[@[], @[]]]
        sage: from_hexacode('12000')
        @[@[@[], @[]]]

        sage: from_hexacode('1200', LabelledOrderedTrees())
        @[@[@[], @[]]]

    It can happen that only a prefix of the word is used::

        sage: from_hexacode('a'+14*'0', LabelledOrderedTrees())
        @[@[], @[], @[], @[], @[], @[], @[], @[], @[], @[]]

    One can choose the label::

        sage: from_hexacode('1200', LabelledOrderedTrees(), label='o')
        o[o[o[], o[]]]

    One can also create other kinds of trees::

        sage: from_hexacode('1200', OrderedTrees())
        [[[], []]]
    """
