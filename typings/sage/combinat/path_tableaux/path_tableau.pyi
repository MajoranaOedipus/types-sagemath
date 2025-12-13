from _typeshed import Incomplete
from sage.categories.sets_cat import Sets as Sets
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.latex import latex as latex
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PathTableau(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    This is the abstract base class for a path tableau.
    """
    @abstract_method
    def local_rule(self, i) -> None:
        """
        This is the abstract local rule defined in any coboundary category.

        This has input a list of objects. This method first takes
        the list of objects of length three consisting of the `(i-1)`-st,
        `i`-th and `(i+1)`-term and applies the rule. It then replaces
        the `i`-th object  by the object returned by the rule.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.local_rule(3)
            [0, 1, 2, 1, 2, 1, 0]
        """
    def size(self):
        """
        Return the size or length of ``self``.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.size()
            7
        """
    def initial_shape(self):
        """
        Return the initial shape of ``self``.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.initial_shape()
            0
        """
    def final_shape(self):
        """
        Return the final shape of ``self``.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.final_shape()
            0
        """
    def promotion(self):
        """
        Return the promotion operator applied to ``self``.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.promotion()
            [0, 1, 2, 1, 0, 1, 0]
        """
    def evacuation(self):
        """
        Return the evacuation operator applied to ``self``.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.evacuation()
            [0, 1, 2, 3, 2, 1, 0]
        """
    def commutor(self, other, verbose: bool = False):
        """
        Return the commutor of ``self`` with ``other``.

        If ``verbose=True`` then the function will print
        the rectangle.

        EXAMPLES::

            sage: t1 = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t2 = path_tableaux.DyckPath([0,1,2,1,0])
            sage: t1.commutor(t2)
            ([0, 1, 2, 1, 0], [0, 1, 2, 3, 2, 1, 0])
            sage: t1.commutor(t2,verbose=True)
            [0, 1, 2, 1, 0]
            [1, 2, 3, 2, 1]
            [2, 3, 4, 3, 2]
            [3, 4, 5, 4, 3]
            [2, 3, 4, 3, 2]
            [1, 2, 3, 2, 1]
            [0, 1, 2, 1, 0]
            ([0, 1, 2, 1, 0], [0, 1, 2, 3, 2, 1, 0])

        TESTS::

            sage: t1 = path_tableaux.DyckPath([])
            sage: t2 = path_tableaux.DyckPath([0,1,2,1,0])
            sage: t1.commutor(t2)
            Traceback (most recent call last):
            ...
            ValueError: this requires nonempty lists
            sage: t1 = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t2 = path_tableaux.DyckPath([])
            sage: t1.commutor(t2)
            Traceback (most recent call last):
            ...
            ValueError: this requires nonempty lists
            sage: t1 = path_tableaux.DyckPath([0,1,2,3,2,1])
            sage: t2 = path_tableaux.DyckPath([0,1,2,1,0])
            sage: t1.commutor(t2)
            Traceback (most recent call last):
            ...
            ValueError: [0, 1, 2, 3, 2, 1], [0, 1, 2, 1, 0] is not a composable pair
        """
    def cactus(self, i, j):
        """
        Return the action of the generator `s_{i,j}` of the cactus
        group on ``self``.

        INPUT:

        - ``i`` -- positive integer
        - ``j`` -- positive integer weakly greater than `i`

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.cactus(1,5)
            [0, 1, 0, 1, 2, 1, 0]

            sage: t.cactus(1,6)
            [0, 1, 2, 1, 0, 1, 0]

            sage: t.cactus(1,7) == t.evacuation()
            True
            sage: t.cactus(1,7).cactus(1,6) == t.promotion()
            True

        TESTS::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.cactus(1,8)
            Traceback (most recent call last):
            ...
            ValueError: integers out of bounds
            sage: t.cactus(0,3)
            Traceback (most recent call last):
            ...
            ValueError: integers out of bounds
        """
    def orbit(self):
        """
        Return the orbit of ``self`` under the action of the cactus group.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: t.orbit()
            {[0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 2, 1, 0],
             [0, 1, 2, 1, 0, 1, 0],
             [0, 1, 2, 1, 2, 1, 0],
             [0, 1, 2, 3, 2, 1, 0]}
        """
    def dual_equivalence_graph(self):
        """
        Return the graph with vertices the orbit of ``self``
        and edges given by the action of the cactus group generators.

        In most implementations the generators `s_{i,i+1}` will act
        as the identity operators. The usual dual equivalence graphs
        are given by replacing the label `i,i+2` by `i` and removing
        edges with other labels.

        EXAMPLES::

            sage: s = path_tableaux.DyckPath([0,1,2,3,2,3,2,1,0])
            sage: s.dual_equivalence_graph().adjacency_matrix()                         # needs sage.graphs sage.modules
            [0 1 1 1 0 1 0 1 1 0 0 0 0 0]
            [1 0 1 1 1 1 1 0 1 0 0 1 1 0]
            [1 1 0 1 1 1 0 1 0 1 1 1 0 0]
            [1 1 1 0 1 0 1 1 1 1 0 1 1 0]
            [0 1 1 1 0 0 1 0 0 1 1 0 1 1]
            [1 1 1 0 0 0 1 1 1 1 1 0 1 0]
            [0 1 0 1 1 1 0 1 0 1 1 1 0 1]
            [1 0 1 1 0 1 1 0 1 1 1 1 1 0]
            [1 1 0 1 0 1 0 1 0 1 0 1 1 0]
            [0 0 1 1 1 1 1 1 1 0 0 1 1 1]
            [0 0 1 0 1 1 1 1 0 0 0 1 1 1]
            [0 1 1 1 0 0 1 1 1 1 1 0 1 1]
            [0 1 0 1 1 1 0 1 1 1 1 1 0 1]
            [0 0 0 0 1 0 1 0 0 1 1 1 1 0]
            sage: s = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: s.dual_equivalence_graph().edges(sort=True)                           # needs sage.graphs
            [([0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 2, 1, 0], '4,7'),
             ([0, 1, 0, 1, 0, 1, 0], [0, 1, 2, 1, 0, 1, 0], '2,5'),
             ([0, 1, 0, 1, 0, 1, 0], [0, 1, 2, 1, 2, 1, 0], '2,7'),
             ([0, 1, 0, 1, 2, 1, 0], [0, 1, 2, 1, 0, 1, 0], '2,6'),
             ([0, 1, 0, 1, 2, 1, 0], [0, 1, 2, 1, 2, 1, 0], '1,4'),
             ([0, 1, 0, 1, 2, 1, 0], [0, 1, 2, 3, 2, 1, 0], '2,7'),
             ([0, 1, 2, 1, 0, 1, 0], [0, 1, 2, 1, 2, 1, 0], '4,7'),
             ([0, 1, 2, 1, 0, 1, 0], [0, 1, 2, 3, 2, 1, 0], '3,7'),
             ([0, 1, 2, 1, 2, 1, 0], [0, 1, 2, 3, 2, 1, 0], '3,6')]
        """

class PathTableaux(UniqueRepresentation, Parent):
    """
    The abstract parent class for PathTableau.
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: t = path_tableaux.DyckPaths()
            sage: TestSuite(t).run()

            sage: f = path_tableaux.FriezePatterns(QQ)
            sage: TestSuite(f).run()
        """

class CylindricalDiagram(SageObject):
    """
    Cylindrical growth diagrams.

    EXAMPLES::

        sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
        sage: path_tableaux.CylindricalDiagram(t)
        [0, 1, 2, 3, 2, 1, 0]
        [ , 0, 1, 2, 1, 0, 1, 0]
        [ ,  , 0, 1, 0, 1, 2, 1, 0]
        [ ,  ,  , 0, 1, 2, 3, 2, 1, 0]
        [ ,  ,  ,  , 0, 1, 2, 1, 0, 1, 0]
        [ ,  ,  ,  ,  , 0, 1, 0, 1, 2, 1, 0]
        [ ,  ,  ,  ,  ,  , 0, 1, 2, 3, 2, 1, 0]
    """
    path_tableau: Incomplete
    diagram: Incomplete
    def __init__(self, T) -> None:
        """
        Initialize ``self`` from the
        :class:`~sage.combinat.path_tableaux.path_tableau.PathTableau`
        object ``T``.

        TESTS::

            sage: T = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: D = path_tableaux.CylindricalDiagram(T)
            sage: TestSuite(D).run()

            sage: path_tableaux.CylindricalDiagram(2)
            Traceback (most recent call last):
            ...
            ValueError: 2 must be a path tableau
        """
    def __eq__(self, other):
        """
        Check equality.

        EXAMPLES::

            sage: t1 = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: T1 = path_tableaux.CylindricalDiagram(t1)
            sage: t2 = path_tableaux.DyckPath([0,1,2,1,2,1,0])
            sage: T2 = path_tableaux.CylindricalDiagram(t2)
            sage: T1 == T2
            False
            sage: T1 == path_tableaux.CylindricalDiagram(t1)
            True
        """
    def __ne__(self, other):
        """
        Check inequality.

        EXAMPLES::

            sage: t1 = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: T1 = path_tableaux.CylindricalDiagram(t1)
            sage: t2 = path_tableaux.DyckPath([0,1,2,1,2,1,0])
            sage: T2 = path_tableaux.CylindricalDiagram(t2)
            sage: T1 != T2
            True
            sage: T1 != path_tableaux.CylindricalDiagram(t1)
            False
        """
    def __len__(self) -> int:
        """
        Return the length of ``self``.

        TESTS::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: len(path_tableaux.CylindricalDiagram(t))
            7
        """
    def pp(self) -> None:
        """
        A pretty print utility method.

        EXAMPLES::

            sage: t = path_tableaux.DyckPath([0,1,2,3,2,1,0])
            sage: path_tableaux.CylindricalDiagram(t).pp()
            0 1 2 3 2 1 0
              0 1 2 1 0 1 0
                0 1 0 1 2 1 0
                  0 1 2 3 2 1 0
                    0 1 2 1 0 1 0
                      0 1 0 1 2 1 0
                        0 1 2 3 2 1 0

            sage: t = path_tableaux.FriezePattern([1,3,4,5,1])
            sage: path_tableaux.CylindricalDiagram(t).pp()
              0   1   3   4   5   1   0
                  0   1 5/3 7/3 2/3   1   0
                      0   1   2   1   3   1   0
                          0   1   1   4 5/3   1   0
                              0   1   5 7/3   2   1   0
                                  0   1 2/3   1   1   1   0
                                      0   1   3   4   5   1   0
        """
