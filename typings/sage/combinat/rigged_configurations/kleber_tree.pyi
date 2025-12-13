from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import binomial as binomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.features import FeatureNotPresentError as FeatureNotPresentError
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.dot2tex_utils import have_dot2tex as have_dot2tex
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class KleberTreeNode(Element):
    """
    A node in the Kleber tree.

    This class is meant to be used internally by the Kleber tree class and
    should not be created directly by the user.

    For more on the Kleber tree and the nodes, see :class:`KleberTree`.

    The dominating root is the ``up_root`` which is the difference
    between the parent node's weight and this node's weight.

    INPUT:

    - ``parent_obj`` -- the parent object of this element
    - ``node_weight`` -- the weight of this node
    - ``dominant_root`` -- the dominating root
    - ``parent_node`` -- (default: ``None``) the parent node of this node
    """
    parent_node: Incomplete
    children: Incomplete
    weight: Incomplete
    up_root: Incomplete
    def __init__(self, parent_obj, node_weight, dominant_root, parent_node=None) -> None:
        """
        Initialize the tree node.

        TESTS::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: RS = RootSystem(['A', 2])
            sage: WS = RS.weight_lattice()
            sage: R = RS.root_lattice()
            sage: KT = KleberTree(['A', 2, 1], [[1,1]])
            sage: parent = KT(WS.sum_of_terms([(1,5), (2,2)]), R.zero())
            sage: parent
            Kleber tree node with weight [5, 2] and upwards edge root [0, 0]
            sage: parent.parent_node
            sage: child = KT(WS.sum_of_terms([(1,3), (2,1)]), R.sum_of_terms([(1,1), (2,2)]), parent)
            sage: child
            Kleber tree node with weight [3, 1] and upwards edge root [1, 2]
            sage: child.parent_node
            Kleber tree node with weight [5, 2] and upwards edge root [0, 0]
            sage: TestSuite(parent).run()
        """
    @lazy_attribute
    def depth(self):
        """
        Return the depth of this node in the tree.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: RS = RootSystem(['A', 2])
            sage: WS = RS.weight_lattice()
            sage: R = RS.root_lattice()
            sage: KT = KleberTree(['A', 2, 1], [[1,1]])
            sage: n = KT(WS.sum_of_terms([(1,5), (2,2)]), R.zero())
            sage: n.depth
            0
            sage: n2 = KT(WS.sum_of_terms([(1,5), (2,2)]), R.zero(), n)
            sage: n2.depth
            1
        """
    @cached_method
    def multiplicity(self):
        """
        Return the multiplicity of ``self``.

        The multiplicity of a node `x` of depth `d` weight `\\lambda` in a
        simply-laced Kleber tree is equal to:

        .. MATH::

            \\prod_{i > 0} \\prod_{a \\in \\overline{I}}
            \\binom{p_i^{(a)} + m_i^{(a)}}{p_i^{(a)}}

        Recall that

        .. MATH::

            m_i^{(a)} = \\left( \\lambda^{(i-1)} - 2 \\lambda^{(i)} +
            \\lambda^{(i+1)} \\mid \\overline{\\Lambda}_a \\right),

            p_i^{(a)} = \\left( \\alpha_a \\mid \\lambda^{(i)} \\right)
            - \\sum_{j > i} (j - i) L_j^{(a)},

        where `\\lambda^{(i)}` is the weight node at depth `i` in the path
        to `x` from the root and we set `\\lambda^{(j)} = \\lambda` for all
        `j \\geq d`.

        Note that `m_i^{(a)} = 0` for all `i > d`.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['A',3,1], [[3,2],[2,1],[1,1],[1,1]])
            sage: for x in KT: x, x.multiplicity()
            (Kleber tree node with weight [2, 1, 2] and upwards edge root [0, 0, 0], 1)
            (Kleber tree node with weight [3, 0, 1] and upwards edge root [0, 1, 1], 1)
            (Kleber tree node with weight [0, 2, 2] and upwards edge root [1, 0, 0], 1)
            (Kleber tree node with weight [1, 0, 3] and upwards edge root [1, 1, 0], 2)
            (Kleber tree node with weight [1, 1, 1] and upwards edge root [1, 1, 1], 4)
            (Kleber tree node with weight [0, 0, 2] and upwards edge root [2, 2, 1], 2)
            (Kleber tree node with weight [2, 0, 0] and upwards edge root [0, 1, 1], 2)
            (Kleber tree node with weight [0, 0, 2] and upwards edge root [1, 1, 0], 1)
            (Kleber tree node with weight [0, 1, 0] and upwards edge root [1, 1, 1], 2)
            (Kleber tree node with weight [0, 1, 0] and upwards edge root [0, 0, 1], 1)

        TESTS:

        We check that :issue:`16057` is fixed::

            sage: RC = RiggedConfigurations(['D',4,1], [[1,3],[3,3],[4,3]])
            sage: sum(x.multiplicity() for x in RC.kleber_tree()) == len(RC.module_generators)
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: RS = RootSystem(['A', 2])
            sage: WS = RS.weight_lattice()
            sage: R = RS.root_lattice()
            sage: KT = KleberTree(['A', 2, 1], [[1,1]])
            sage: n = KT(WS.sum_of_terms([(1,5), (2,2)]), R.zero())
            sage: n2 = KT(WS.sum_of_terms([(2,2), (1,5)]), R.zero())
            sage: hash(n) == hash(n2)
            True
            sage: hash(n) == hash(R.zero())
            False
        """

class KleberTree(UniqueRepresentation, Parent):
    """
    The tree that is generated by Kleber's algorithm.

    A Kleber tree is a tree of weights generated by Kleber's algorithm
    [Kleber1]_. It is used to generate the set of all admissible rigged
    configurations for the simply-laced affine types `A_n^{(1)}`,
    `D_n^{(1)}`, `E_6^{(1)}`, `E_7^{(1)}`, and `E_8^{(1)}`.

    .. SEEALSO::

        There is a modified version for non-simply-laced affine types at
        :class:`VirtualKleberTree`.

    The nodes correspond to the weights in the positive Weyl chamber obtained
    by subtracting a (nonzero) positive root. The edges are labeled by the
    coefficients of the roots, and `X` is a child of `Y` if `Y` is the root
    else if the edge label of `Y` to its parent `Z` is greater (in every
    component) than the label from `X` to `Y`.

    For a Kleber tree, one needs to specify an affine (simply-laced)
    Cartan type and a sequence of pairs `(r,s)`, where `s` is any positive
    integer and `r` is a node in the Dynkin diagram. Each `(r,s)` can be
    viewed as a rectangle of width `s` and height `r`.

    INPUT:

    - ``cartan_type`` -- an affine simply-laced Cartan type

    - ``B`` -- list of dimensions of rectangles by `[r, c]`
      where `r` is the number of rows and `c` is the number of columns

    REFERENCES:

    .. [Kleber1] Michael Kleber.
       *Combinatorial structure of finite dimensional representations of
       Yangians: the simply-laced case*.
       Internat. Math. Res. Notices. (1997) no. 4. 187-201.

    .. [Kleber2] Michael Kleber.
       *Finite dimensional representations of quantum affine algebras*.
       Ph.D. dissertation at University of California Berkeley. (1998).
       :arxiv:`math.QA/9809087`.

    EXAMPLES:

    Simply-laced example::

        sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
        sage: KT = KleberTree(['A', 3, 1], [[3,2], [1,1]])
        sage: KT.list()
        [Kleber tree node with weight [1, 0, 2] and upwards edge root [0, 0, 0],
         Kleber tree node with weight [0, 0, 1] and upwards edge root [1, 1, 1]]
        sage: KT = KleberTree(['A', 3, 1], [[3,2], [2,1], [1,1], [1,1]])
        sage: KT.cardinality()
        10
        sage: KT = KleberTree(['D', 4, 1], [[2,2]])
        sage: KT.cardinality()
        3
        sage: KT = KleberTree(['D', 4, 1], [[4,5]])
        sage: KT.cardinality()
        1

    From [Kleber2]_::

        sage: KT = KleberTree(['E', 6, 1], [[4, 2]])  # long time (9s on sage.math, 2012)
        sage: KT.cardinality()  # long time
        12

    We check that relabelled types work (:issue:`16876`)::

        sage: ct = CartanType(['A',3,1]).relabel(lambda x: x+2)
        sage: kt = KleberTree(ct, [[3,1],[5,1]])
        sage: list(kt)
        [Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 0, 0],
         Kleber tree node with weight [0, 0, 0] and upwards edge root [1, 1, 1]]
        sage: kt = KleberTree(['A',3,1], [[1,1],[3,1]])
        sage: list(kt)
        [Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 0, 0],
         Kleber tree node with weight [0, 0, 0] and upwards edge root [1, 1, 1]]
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, B, classical=None):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT1 = KleberTree(CartanType(['A',3,1]), [[2,2]])
            sage: KT2 = KleberTree(['A',3,1], [(2,2)])
            sage: KT3 = KleberTree(['A',3,1], ((2,2),))
            sage: KT2 is KT1, KT3 is KT1
            (True, True)
        """
    B: Incomplete
    def __init__(self, cartan_type, B, classical_ct) -> None:
        """
        Construct a Kleber tree.

        The input ``classical_ct`` is the classical Cartan type to run the
        algorithm on and is only meant to be used internally.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['D', 3, 1], [[1,1], [1,1]]); KT
            Kleber tree of Cartan type ['D', 3, 1] and B = ((1, 1), (1, 1))
            sage: TestSuite(KT).run(skip='_test_elements')
        """
    def latex_options(self, **options):
        """
        Return the current latex options if no arguments are passed, otherwise
        set the corresponding latex option.

        OPTIONS:

        - ``hspace`` -- (default: `2.5`) the horizontal spacing of the
          tree nodes
        - ``vspace`` -- (default: ``x``) the vertical spacing of the tree
          nodes, here ``x`` is the minimum of `-2.5` or `-.75n` where `n` is
          the rank of the classical type
        - ``edge_labels`` -- boolean (default: ``True``); display edge labels
        - ``use_vector_notation`` -- boolean (default: ``False``); display edge labels
          using vector notation instead of a linear combination

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['D', 3, 1], [[2,1], [2,1]])
            sage: KT.latex_options(vspace=-4, use_vector_notation=True)
            sage: sorted(KT.latex_options().items())
            [('edge_labels', True), ('hspace', 2.5), ('use_vector_notation', True), ('vspace', -4)]
        """
    def breadth_first_iter(self) -> Generator[Incomplete]:
        """
        Iterate over all nodes in the tree following a breadth-first traversal.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['A', 3, 1], [[2, 2], [2, 3]])
            sage: for x in KT.breadth_first_iter(): x
            Kleber tree node with weight [0, 5, 0] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 3, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 3, 0] and upwards edge root [1, 2, 1]
            Kleber tree node with weight [2, 1, 2] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [1, 1, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 1, 0] and upwards edge root [1, 2, 1]
        """
    def depth_first_iter(self):
        """
        Iterate (recursively) over the nodes in the tree following a
        depth-first traversal.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['A', 3, 1], [[2, 2], [2, 3]])
            sage: for x in KT.depth_first_iter(): x
            Kleber tree node with weight [0, 5, 0] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 3, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [2, 1, 2] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 3, 0] and upwards edge root [1, 2, 1]
            Kleber tree node with weight [1, 1, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 1, 0] and upwards edge root [1, 2, 1]
        """
    __iter__ = breadth_first_iter
    def cartan_type(self):
        """
        Return the Cartan type of this Kleber tree.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['A', 3, 1], [[1,1]])
            sage: KT.cartan_type()
            ['A', 3, 1]
        """
    def digraph(self):
        """
        Return a DiGraph representation of this Kleber tree.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['D', 4, 1], [[2, 2]])
            sage: KT.digraph()
            Digraph on 3 vertices
        """
    def plot(self, **options):
        """
        Return the plot of ``self`` as a directed graph.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import KleberTree
            sage: KT = KleberTree(['D', 4, 1], [[2, 2]])
            sage: print(KT.plot())                                                      # needs sage.plot
            Graphics object consisting of 8 graphics primitives
        """
    Element = KleberTreeNode

class VirtualKleberTree(KleberTree):
    """
    A virtual Kleber tree.

    We can use a modified version of the Kleber algorithm called the virtual
    Kleber algorithm [OSS03]_ to compute all admissible rigged configurations
    for non-simply-laced types. This uses the following embeddings
    into the simply-laced types:

    .. MATH::

        C_n^{(1)}, A_{2n}^{(2)}, A_{2n}^{(2)\\dagger}, D_{n+1}^{(2)}
        \\hookrightarrow A_{2n-1}^{(1)}

        A_{2n-1}^{(2)}, B_n^{(1)} \\hookrightarrow D_{n+1}^{(1)}

        E_6^{(2)}, F_4^{(1)} \\hookrightarrow E_6^{(1)}

        D_4^{(3)}, G_2^{(1)} \\hookrightarrow D_4^{(1)}

    One then selects the subset of admissible nodes which are translates of
    the virtual requirements. In the graph, the selected nodes are indicated
    by brackets `[]`.

    .. NOTE::

        Because these are virtual nodes, all information is given
        in the corresponding simply-laced type.

    .. SEEALSO::

        For more on the Kleber algorithm, see :class:`KleberTree`.

    REFERENCES:

    .. [OSS03] Masato Okado, Anne Schilling, and Mark Shimozono.
       *Virtual crystals and Klebers algorithm*. Commun. Math. Phys. **238**
       (2003). 187-209. :arxiv:`math.QA/0209082`.

    INPUT:

    - ``cartan_type`` -- an affine non-simply-laced Cartan type

    - ``B`` -- list of dimensions of rectangles by `[r, c]`
      where `r` is the number of rows and `c` is the number of columns

    EXAMPLES::

        sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
        sage: KT = VirtualKleberTree(['C', 4, 1], [[2,2]])
        sage: KT.cardinality()
        3
        sage: KT.base_tree().cardinality()
        6
        sage: KT = VirtualKleberTree(['C', 4, 1], [[4,5]])
        sage: KT.cardinality()
        1
        sage: KT = VirtualKleberTree(['D', 5, 2], [[2,1], [1,1]])
        sage: KT.cardinality()
        8
        sage: KT = VirtualKleberTree(CartanType(['A', 4, 2]).dual(), [[1,1], [2,2]])
        sage: KT.cardinality()
        15
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, B):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT1 = VirtualKleberTree(CartanType(['C',3,1]).as_folding(), [[2,2]])
            sage: KT2 = VirtualKleberTree(CartanType(['C',3,1]), [(2,2)])
            sage: KT3 = VirtualKleberTree(['C',3,1], ((2,2),))
            sage: KT2 is KT1, KT3 is KT1
            (True, True)
        """
    base_dims: Incomplete
    def __init__(self, cartan_type, B) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['C',4,1], [[2,2]])
            sage: TestSuite(KT).run(skip='_test_elements')
        """
    def breadth_first_iter(self, all_nodes: bool = False) -> Generator[Incomplete]:
        """
        Iterate over all nodes in the tree following a breadth-first traversal.

        INPUT:

        - ``all_nodes`` -- boolean (default: ``False``); if ``True``, output all
          nodes in the tree

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['C', 2, 1], [[1,1], [2,1]])
            sage: for x in KT.breadth_first_iter(): x
            Kleber tree node with weight [1, 2, 1] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
            sage: for x in KT.breadth_first_iter(True): x
            Kleber tree node with weight [1, 2, 1] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [0, 2, 0] and upwards edge root [1, 1, 1]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
        """
    def depth_first_iter(self, all_nodes: bool = False) -> Generator[Incomplete]:
        """
        Iterate (recursively) over the nodes in the tree following a
        depth-first traversal.

        INPUT:

        - ``all_nodes`` -- boolean (default: ``False``); if ``True``, output all
          nodes in the tree

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['C', 2, 1], [[1,1], [2,1]])
            sage: for x in KT.depth_first_iter(): x
            Kleber tree node with weight [1, 2, 1] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
            sage: for x in KT.depth_first_iter(True): x
            Kleber tree node with weight [1, 2, 1] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [0, 2, 0] and upwards edge root [1, 1, 1]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
        """
    __iter__ = breadth_first_iter
    def base_tree(self):
        """
        Return the underlying virtual Kleber tree associated to ``self``.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['C', 4, 1], [[2,2]])
            sage: KT.base_tree()
            Kleber tree of Cartan type ['A', 7, 1] and B = ((2, 2), (6, 2))
        """

class KleberTreeTypeA2Even(VirtualKleberTree):
    """
    Kleber tree for types `A_{2n}^{(2)}` and `A_{2n}^{(2)\\dagger}`.

    Note that here for `A_{2n}^{(2)}` we use `\\tilde{\\gamma}_a` in place of
    `\\gamma_a` in constructing the virtual Kleber tree, and so we end up
    selecting all nodes since `\\tilde{\\gamma}_a = 1` for all `a \\in
    \\overline{I}`. For type `A_{2n}^{(2)\\dagger}`, we have `\\gamma_a = 1`
    for all `a \\in \\overline{I}`.

    .. SEEALSO::

        :class:`VirtualKleberTree`
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, B):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT1 = VirtualKleberTree(CartanType(['A',6,2]), [[2,2]])
            sage: KT2 = VirtualKleberTree(['A',6,2], [(2,2)])
            sage: KT3 = VirtualKleberTree(['A',6,2], ((2,2),))
            sage: KT2 is KT1, KT3 is KT1
            (True, True)
        """
    base_dims: Incomplete
    def __init__(self, cartan_type, B) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['A',6,2], [[2,2]]); KT
            Virtual Kleber tree of Cartan type ['BC', 3, 2] and B = ((2, 2),)
            sage: TestSuite(KT).run(skip='_test_elements')
        """
    def __iter__(self):
        """
        Iterate over all of the nodes.

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['A',6,2], [[2,2]])
            sage: L = [x for x in KT]
            sage: len(L) == KT.cardinality()
            True
        """
    def breadth_first_iter(self, all_nodes: bool = False):
        """
        Iterate over all nodes in the tree following a breadth-first traversal.

        INPUT:

        - ``all_nodes`` -- boolean (default: ``False``); if ``True``, output all
          nodes in the tree

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['A', 4, 2], [[2,1]])
            sage: for x in KT.breadth_first_iter(): x
            Kleber tree node with weight [0, 2, 0] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 0, 0] and upwards edge root [1, 2, 1]
            sage: for x in KT.breadth_first_iter(True): x
            Kleber tree node with weight [0, 2, 0] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 0, 0] and upwards edge root [1, 2, 1]
        """
    def depth_first_iter(self, all_nodes: bool = False):
        """
        Iterate (recursively) over the nodes in the tree following a
        depth-first traversal.

        INPUT:

        - ``all_nodes`` -- boolean (default: ``False``); if ``True``, output all
          nodes in the tree

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.kleber_tree import VirtualKleberTree
            sage: KT = VirtualKleberTree(['A', 4, 2], [[2,1]])
            sage: for x in KT.depth_first_iter(): x
            Kleber tree node with weight [0, 2, 0] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 0, 0] and upwards edge root [1, 2, 1]
            sage: for x in KT.depth_first_iter(True): x
            Kleber tree node with weight [0, 2, 0] and upwards edge root [0, 0, 0]
            Kleber tree node with weight [1, 0, 1] and upwards edge root [0, 1, 0]
            Kleber tree node with weight [0, 0, 0] and upwards edge root [1, 2, 1]
        """
