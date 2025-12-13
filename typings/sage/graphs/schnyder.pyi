from .all import DiGraph as DiGraph
from _typeshed import Incomplete
from sage.sets.set import Set as Set

class TreeNode:
    """
    A class to represent each node in the trees used by ``_realizer`` and
    ``_compute_coordinates`` when finding a planar geometric embedding in
    the grid.

    Each tree node is doubly linked to its parent and children.

    INPUT:

    - ``parent`` -- the parent TreeNode of ``self``
    - ``children`` -- list of TreeNode children of ``self``
    - ``label`` -- the associated realizer vertex label

    EXAMPLES::

        sage: from sage.graphs.schnyder import TreeNode
        sage: tn = TreeNode(label=5)
        sage: tn2 = TreeNode(label=2,parent=tn)
        sage: tn3 = TreeNode(label=3)
        sage: tn.append_child(tn3)
        sage: tn.compute_number_of_descendants()
        2
        sage: tn.number_of_descendants
        2
        sage: tn3.number_of_descendants
        1
        sage: tn.compute_depth_of_self_and_children()
        sage: tn3.depth
        2
    """
    parent: Incomplete
    children: Incomplete
    label: Incomplete
    number_of_descendants: int
    def __init__(self, parent=None, children=None, label=None) -> None:
        """
        INPUT:

        - ``parent`` -- the parent TreeNode of ``self``
        - ``children`` -- list of TreeNode children of ``self``
        - ``label`` -- the associated realizer vertex label

        EXAMPLES::

            sage: from sage.graphs.schnyder import TreeNode
            sage: tn = TreeNode(label=5)
            sage: tn2 = TreeNode(label=2,parent=tn)
            sage: tn3 = TreeNode(label=3)
            sage: tn.append_child(tn3)
            sage: tn.compute_number_of_descendants()
            2
            sage: tn.number_of_descendants
            2
            sage: tn3.number_of_descendants
            1
            sage: tn.compute_depth_of_self_and_children()
            sage: tn3.depth
            2
        """
    def compute_number_of_descendants(self):
        """
        Compute the number of descendants of ``self`` and all descendants.

        For each TreeNode, sets result as attribute ``self.number_of_descendants``.

        EXAMPLES::

            sage: from sage.graphs.schnyder import TreeNode
            sage: tn = TreeNode(label=5)
            sage: tn2 = TreeNode(label=2,parent=tn)
            sage: tn3 = TreeNode(label=3)
            sage: tn.append_child(tn3)
            sage: tn.compute_number_of_descendants()
            2
            sage: tn.number_of_descendants
            2
            sage: tn3.number_of_descendants
            1
            sage: tn.compute_depth_of_self_and_children()
            sage: tn3.depth
            2
        """
    depth: int
    def compute_depth_of_self_and_children(self) -> None:
        """
        Compute the depth of ``self`` and all descendants.

        For each TreeNode, sets result as ``attribute self.depth``.

        EXAMPLES::

            sage: from sage.graphs.schnyder import TreeNode
            sage: tn = TreeNode(label=5)
            sage: tn2 = TreeNode(label=2,parent=tn)
            sage: tn3 = TreeNode(label=3)
            sage: tn.append_child(tn3)
            sage: tn.compute_number_of_descendants()
            2
            sage: tn.number_of_descendants
            2
            sage: tn3.number_of_descendants
            1
            sage: tn.compute_depth_of_self_and_children()
            sage: tn3.depth
            2
        """
    def append_child(self, child) -> None:
        """
        Add a child to list of children.

        EXAMPLES::

            sage: from sage.graphs.schnyder import TreeNode
            sage: tn = TreeNode(label=5)
            sage: tn2 = TreeNode(label=2,parent=tn)
            sage: tn3 = TreeNode(label=3)
            sage: tn.append_child(tn3)
            sage: tn.compute_number_of_descendants()
            2
            sage: tn.number_of_descendants
            2
            sage: tn3.number_of_descendants
            1
            sage: tn.compute_depth_of_self_and_children()
            sage: tn3.depth
            2
        """

def minimal_schnyder_wood(graph, root_edge=None, minimal: bool = True, check: bool = True):
    """
    Return the minimal Schnyder wood of a planar rooted triangulation.

    INPUT:

    - ``graph`` -- a planar triangulation, given by a graph with an embedding

    - ``root_edge`` -- a pair of vertices (default: from ``-1`` to ``-2``);
      the third boundary vertex is then determined using the orientation and
      will be labelled ``-3``

    - ``minimal`` -- boolean (default: ``True``); whether to return a
      minimal or a maximal Schnyder wood

    - ``check`` -- boolean (default: ``True``); whether to check if the input
      is a planar triangulation

    OUTPUT:

    A planar graph, with edges oriented and colored. The three outer
    edges of the initial graph are removed. For the three outer vertices the
    list of the neighbors stored in the combinatorial embedding is in the order
    of the incident edges between the two incident (and removed) outer edges,
    and not a cyclic shift of it.

    The algorithm is taken from [Bre2000]_ (section 4.2).

    EXAMPLES::

        sage: from sage.graphs.schnyder import minimal_schnyder_wood
        sage: g = Graph([(0,-1),(0,-2),(0,-3),(-1,-2),(-2,-3),
        ....:  (-3,-1)], format='list_of_edges')
        sage: g.set_embedding({-1:[-2,0,-3],-2:[-3,0,-1],
        ....:  -3:[-1,0,-2],0:[-1,-2,-3]})
        sage: newg = minimal_schnyder_wood(g)
        sage: newg.edges(sort=True)
        [(0, -3, 'red'), (0, -2, 'blue'), (0, -1, 'green')]
        sage: newg.plot(color_by_label={'red':'red','blue':'blue',                      # needs sage.plot
        ....:  'green':'green',None:'black'})
        Graphics object consisting of 8 graphics primitives

    A larger example::

        sage: g = Graph([(0,-1),(0,2),(0,1),(0,-3),(-1,-3),(-1,2),
        ....: (-1,-2),(1,2),(1,-3),(2,-2),(1,-2),(-2,-3)], format='list_of_edges')
        sage: g.set_embedding({-1:[-2,2,0,-3],-2:[-3,1,2,-1],
        ....: -3:[-1,0,1,-2],0:[-1,2,1,-3],1:[-2,-3,0,2],2:[-1,-2,1,0]})
        sage: newg = minimal_schnyder_wood(g)
        sage: newg.edges(sort=True, key=lambda e:(str(e[0]),str(e[1])))
        [(0, -1, 'green'),
         (0, -3, 'red'),
         (0, 2, 'blue'),
         (1, -2, 'blue'),
         (1, -3, 'red'),
         (1, 0, 'green'),
         (2, -1, 'green'),
         (2, -2, 'blue'),
         (2, 1, 'red')]
        sage: newg2 = minimal_schnyder_wood(g, minimal=False)
        sage: newg2.edges(sort=True, key=lambda e:(str(e[0]),str(e[1])))
        [(0, -1, 'green'),
         (0, -3, 'red'),
         (0, 1, 'blue'),
         (1, -2, 'blue'),
         (1, -3, 'red'),
         (1, 2, 'green'),
         (2, -1, 'green'),
         (2, -2, 'blue'),
         (2, 0, 'red')]

    TESTS::

        sage: minimal_schnyder_wood(graphs.RandomTriangulation(5))
        Digraph on 5 vertices
        sage: minimal_schnyder_wood(graphs.CompleteGraph(5))
        Traceback (most recent call last):
        ...
        ValueError: not a planar graph
        sage: minimal_schnyder_wood(graphs.WheelGraph(5))
        Traceback (most recent call last):
        ...
        ValueError: not a triangulation
        sage: minimal_schnyder_wood(graphs.OctahedralGraph(),root_edge=(0,5))
        Traceback (most recent call last):
        ...
        ValueError: not a valid root edge
    """
