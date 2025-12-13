from _typeshed import Incomplete
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.graphs.digraph import DiGraph as DiGraph
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.element import Element as Element
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AuslanderReitenQuiver(UniqueRepresentation, Parent):
    '''
    The Auslander-Reiten quiver.

    Let `Q = (Q_0, Q_1)` be a finite acyclic quiver. The
    *Auslander-Reiten quiver* (AR quiver) `\\Gamma_Q` is the quiver
    whose vertices correspond to the indecompositible modules of `Q`
    (equivalently its path algebra over an algebraically closed field)
    and edges are irreducible morphisms.

    In this implementation, we denote the vertices of `\\Gamma_Q` as
    certain pairs `\\langle v, k \\rangle`, where `v \\in Q_0` and
    `k \\in \\ZZ \\setminus \\{0\\}` is called the *level*. When `k > 0`
    (resp. `k < 0`), then it corresponds to a preprojective (resp.
    postinjective) module. When the quiver is a finite type Dynkin
    quiver, we consider all modules to be preprojectives and denoted
    by a positive level.

    .. NOTE::

        We use the terminology *postinjective* instead of *preinjective*
        given that they follow from injectives by AR translation.

    ALGORITHM:

    We compute the dimension vectors of a projective `\\langle v, 1 \\rangle`
    by counting the number of (directed) paths `u \\to v` in `Q`. We then
    proceed inductively to compute all of the dimension vectors of level
    `k` by using the translation equation

    .. MATH::

        dim \\langle v, k-1 \\rangle + \\dim \\langle v, k \\rangle
        = \\sum_{u,k\'} \\dim \\langle u, k\' \\rangle,

    where the sum is over all paths from `\\langle v, k-1 \\rangle` to
    `\\langle v, k \\rangle` in `\\Gamma_Q`. More specifically, for each edge
    `(u, v, \\ell) \\in Q_1` (resp. `(v, u, \\ell) \\in Q_1`), we have
    `\\langle u, k-1 \\rangle` (resp. `\\langle u, k \\rangle`) in the sum
    (assuming the node is in the AR quiver).

    The algorithm for postinjectives is dual to the above.

    .. TODO::

        This only is implemented for the preprojectives and postinjectives
        when the quiver is not a finite type Dynkin quiver.

    .. TODO::

        Implement this for general Artinian algebras.

    EXAMPLES:

    We create the AR quivers for finite type `A_3` Dynkin quivers::

        sage: DA = DiGraph([[1, 2], [2, 3]])
        sage: AR = DA.auslander_reiten_quiver()
        sage: AR.digraph().edges(labels=False)
        [(<1, 1>, <2, 2>), (<2, 1>, <1, 1>), (<2, 1>, <3, 2>), (<3, 1>, <2, 1>),
         (<2, 2>, <3, 3>), (<3, 2>, <2, 2>)]

        sage: DA = DiGraph([[1, 2], [3, 2]])
        sage: AR = DA.auslander_reiten_quiver()
        sage: AR.digraph().edges(labels=False)
        [(<1, 1>, <2, 2>), (<2, 1>, <1, 1>), (<2, 1>, <3, 1>), (<3, 1>, <2, 2>),
         (<2, 2>, <1, 2>), (<2, 2>, <3, 2>)]

        sage: DA = DiGraph([[2, 1], [2, 3]])
        sage: AR = DA.auslander_reiten_quiver()
        sage: AR.digraph().edges(labels=False)
        [(<1, 1>, <2, 1>), (<2, 1>, <1, 2>), (<2, 1>, <3, 2>), (<3, 1>, <2, 1>),
         (<1, 2>, <2, 2>), (<3, 2>, <2, 2>)]

        sage: DA = DiGraph([[2, 1], [3, 2]])
        sage: AR = DA.auslander_reiten_quiver()
        sage: AR.digraph().edges(labels=False)
        [(<1, 1>, <2, 1>), (<2, 1>, <3, 1>), (<2, 1>, <1, 2>), (<3, 1>, <2, 2>),
         (<1, 2>, <2, 2>), (<2, 2>, <1, 3>)]

    An example for the type `D_5` Dynkin quiver::

        sage: DD = DiGraph([[5,3], [4,3], [3,2], [2,1]])
        sage: AR = DD.auslander_reiten_quiver()
        sage: AR
        Auslander-Reiten quiver of a [\'D\', 5] Dynkin quiver
        sage: len(list(DD))
        5

    An `E_8` Dynkin quiver::

        sage: DE = DiGraph([[8,7], [7,6], [5,6], [5,3], [3,4], [3,2], [2,1]])
        sage: AR = DE.auslander_reiten_quiver()
        sage: AR
        Auslander-Reiten quiver of a [\'E\', 8] Dynkin quiver
        sage: len(list(AR))
        120
        sage: len(list(RootSystem([\'E\', 8]).root_lattice().positive_roots()))
        120

    The Kronecker quiver::

        sage: D = DiGraph([[1,2,\'a\'], [1,2,\'b\']], multiedges=True)
        sage: AR = D.auslander_reiten_quiver()
        sage: for i in range(1, 5):
        ....:     for v in D.vertices():
        ....:         pp = AR(v, i)
        ....:         pi = AR(v, -i)
        ....:         print(pp, pp.dimension_vector(), "  ", pi, pi.dimension_vector())
        <1, 1> v1 + 2*v2      <1, -1> v1
        <2, 1> v2             <2, -1> 2*v1 + v2
        <1, 2> 3*v1 + 4*v2    <1, -2> 3*v1 + 2*v2
        <2, 2> 2*v1 + 3*v2    <2, -2> 4*v1 + 3*v2
        <1, 3> 5*v1 + 6*v2    <1, -3> 5*v1 + 4*v2
        <2, 3> 4*v1 + 5*v2    <2, -3> 6*v1 + 5*v2
        <1, 4> 7*v1 + 8*v2    <1, -4> 7*v1 + 6*v2
        <2, 4> 6*v1 + 7*v2    <2, -4> 8*v1 + 7*v2
    '''
    @staticmethod
    def __classcall_private__(cls, quiver):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: D = DiGraph([[1,2], [2,3], [3,1]])
            sage: D.auslander_reiten_quiver()
            Traceback (most recent call last):
            ...
            ValueError: the quiver must not have cycles
        """
    def __init__(self, quiver) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: DE = DiGraph([[7,6], [6,5], [5,3], [3,4], [2,3], [1,2]])
            sage: AR = DE.auslander_reiten_quiver()
            sage: TestSuite(AR).run()

            sage: D = DiGraph([[1,2], [3,4]])
            sage: AR = D.auslander_reiten_quiver()
            sage: TestSuite(AR).run()

            sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
            sage: AR = D.auslander_reiten_quiver()
            sage: TestSuite(AR).run()
        """
    class options(GlobalOptions):
        '''
        Set and display the global options for Auslander-Reiten quivers.
        If no parameters are set, then the function returns a copy of the
        options dictionary.

        The ``options`` to partitions can be accessed as the method
        :obj:`AuslanderReitenQuiver.options` of
        :class:`~sage.quivers.ar_quiver.AuslanderReitenQuiver`.

        @OPTIONS@

        EXAMPLES::

            sage: D = DiGraph([[1,2,\'a\'], [1,2,\'b\']], multiedges=True)
            sage: AR = D.auslander_reiten_quiver()
            sage: node = AR(2, 2)
            sage: latex(node)
            \\left\\langle 2, 2 \\right\\rangle
            sage: AR.options.latex = "dimension_vector"
            sage: latex(node)
            2 v_{1} + 3 v_{2}
            sage: AR.options.latex = "both"
            sage: latex(node)
            \\begin{gathered} \\left\\langle 2, 2 \\right\\rangle \\\\ 2 v_{1} + 3 v_{2} \\end{gathered}
            sage: AR.options._reset()
        '''
        NAME: str
        module: str
        latex: Incomplete
    def quiver(self):
        """
        Return the quiver defining ``self``.

        EXAMPLES::

            sage: DE = DiGraph([[7,8], [7,6], [5,6], [3,5], [4,3], [2,3], [1,2]])
            sage: AR = DE.auslander_reiten_quiver()
            sage: AR.quiver() == DE
            True
        """
    def projectives(self):
        """
        Return the projectives of ``self``.

        EXAMPLES::

            sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
            sage: AR = D.auslander_reiten_quiver()
            sage: AR.projectives()
            Finite family {1: <1, 1>, 2: <2, 1>}
        """
    @cached_method
    def simples(self):
        """
        Return the simples of ``self``.

        EXAMPLES::

            sage: DE = DiGraph([[7,8], [7,6], [5,6], [3,5], [4,3], [2,3], [1,2]])
            sage: AR = DE.auslander_reiten_quiver()
            sage: AR.simples()
            Finite family {1: <1, 15>,  2: <1, 14>,  3: <8, 4>,  4: <4, 15>,
                           5: <8, 3>,  6: <6, 1>,  7: <7, 15>,  8: <8, 1>}
        """
    def injectives(self):
        """
        Return the injectives of ``self``.

        EXAMPLES::

            sage: DE = DiGraph([[7,6], [6,5], [5,3], [4,3], [2,3], [1,2]])
            sage: AR = DE.auslander_reiten_quiver()
            sage: AR.injectives()
            Finite family {1: <1, 9>, 2: <2, 9>, 3: <3, 9>, 4: <4, 9>,
                           5: <5, 9>, 6: <6, 9>, 7: <7, 9>}
        """
    def digraph_preprojectives(self, max_depth, with_translations: bool = False):
        """
        Return the digraph of preprojectives of ``self`` up to ``max_depth``.

        EXAMPLES::

            sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
            sage: AR = D.auslander_reiten_quiver()
            sage: G = AR.digraph_preprojectives(3)
            sage: [node.dimension_vector() for node in G]
            [v1 + 2*v2, v2, 3*v1 + 4*v2, 2*v1 + 3*v2, 5*v1 + 6*v2, 4*v1 + 5*v2]
            sage: AR.digraph_preprojectives(0)
            Digraph on 0 vertices
        """
    def digraph_postinjectives(self, max_depth, with_translations: bool = False):
        """
        Return the digraph of postinjectives of ``self`` up to ``max_depth``.

        EXAMPLES::

            sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
            sage: AR = D.auslander_reiten_quiver()
            sage: G = AR.digraph_postinjectives(3)
            sage: [node.dimension_vector() for node in G]
            [5*v1 + 4*v2, 6*v1 + 5*v2, 3*v1 + 2*v2, 4*v1 + 3*v2, v1, 2*v1 + v2]
            sage: AR.digraph_postinjectives(0)
            Digraph on 0 vertices
        """
    @cached_method
    def digraph(self, with_translations: bool = False):
        """
        Return the digraph of ``self``.

        INPUT:

        - ``with_translations`` -- boolean (default: ``False``); if ``True``,
          then include the arrows corresponding to the translations

        EXAMPLES::

            sage: DA = DiGraph([[1,2]])
            sage: AR = DA.auslander_reiten_quiver()
            sage: G = AR.digraph(); G
            Digraph on 3 vertices
            sage: G.edges()
            [(<1, 1>, <2, 2>, None), (<2, 1>, <1, 1>, None)]
            sage: GT = AR.digraph(with_translations=True)
            sage: GT.edges()
            [(<1, 1>, <2, 2>, None), (<2, 1>, <1, 1>, None), (<2, 2>, <2, 1>, 'ART')]
        """
    def __iter__(self):
        """
        Iterate over ``self`` when possible.

        EXAMPLES::

            sage: DD = DiGraph([[3,2], [4,2], [2,1]])
            sage: AR = DD.auslander_reiten_quiver()
            sage: list(AR)
            [<1, 1>, <2, 1>, <3, 1>, <4, 1>, <1, 2>, <2, 2>, <3, 2>, <4, 2>,
             <1, 3>, <2, 3>, <3, 3>, <4, 3>]
        """
    def dimension_vectors_of_level(self, k):
        """
        Return a :class:`Family` of dimension vectors of level ``k``.

        EXAMPLES::

            sage: DA = DiGraph([[4,3], [2,3], [2,1]])
            sage: AR = DA.auslander_reiten_quiver()
            sage: AR.dimension_vectors_of_level(1)
            {1: v1, 2: v1 + v2 + v3, 3: v3, 4: v3 + v4}
            sage: AR.dimension_vectors_of_level(3)
            {1: v4, 3: v2}
            sage: AR.dimension_vectors_of_level(10)
            {}
            sage: AR.dimension_vectors_of_level(-1)
             {1: v1 + v2, 2: v2, 3: v2 + v3 + v4, 4: v4}
            sage: AR.dimension_vectors_of_level(-2)
            {1: v3 + v4, 2: v1 + v2 + v3 + v4, 3: v1 + v2 + v3, 4: v2 + v3}

            sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
            sage: AR = D.auslander_reiten_quiver()
            sage: AR.dimension_vectors_of_level(1)
            {1: v1 + 2*v2, 2: v2}
            sage: AR.dimension_vectors_of_level(3)
            {1: 5*v1 + 6*v2, 2: 4*v1 + 5*v2}
            sage: AR.dimension_vectors_of_level(-1)
            {1: v1, 2: 2*v1 + v2}
            sage: AR.dimension_vectors_of_level(-3)
            {1: 5*v1 + 4*v2, 2: 6*v1 + 5*v2}
        """
    class Element(Element):
        """
        A node in the AR quiver.
        """
        def __init__(self, parent, vertex, level) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: DA = DiGraph([[4,3], [3,2], [2,1]])
                sage: AR = DA.auslander_reiten_quiver()
                sage: TestSuite(AR(1, 3)).run()

                sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
                sage: AR = D.auslander_reiten_quiver()
                sage: TestSuite(AR(2, 3)).run()
                sage: TestSuite(AR(1, -4)).run()
            """
        def __hash__(self) -> int:
            """
            Return the hash of ``self``.

            EXAMPLES::

                sage: DA = DiGraph([[2,3], [2,1]])
                sage: AR = DA.auslander_reiten_quiver()
                sage: node = AR(1, 2)
                sage: hash(node) == hash((2, 1))
                True
            """
        def vertex(self):
            """
            Return the vertex of the quiver corresponding to ``self``.

            EXAMPLES::

                sage: DA = DiGraph([[2,3], [2,1]])
                sage: AR = DA.auslander_reiten_quiver()
                sage: node = AR(1, 2)
                sage: node.vertex()
                1
            """
        def level(self):
            """
            Return the level of ``self``.

            EXAMPLES::

                sage: DA = DiGraph([[2,3], [2,1]])
                sage: AR = DA.auslander_reiten_quiver()
                sage: node = AR(1, 2)
                sage: node.level()
                2
            """
        def translation(self):
            """
            Return the AR translation of ``self``.

            EXAMPLES::

                sage: DA = DiGraph([[4,3], [3,2], [2,1]])
                sage: AR = DA.auslander_reiten_quiver()
                sage: node = AR(1, 1)
                sage: node.translation() is None
                True
                sage: node = AR(1, 2)
                sage: node.translation()
                <1, 1>
            """
        def inverse_translation(self):
            """
            Return the inverse AR translation of ``self``.

            EXAMPLES::

                sage: DA = DiGraph([[2,3], [2,1]])
                sage: AR = DA.auslander_reiten_quiver()
                sage: node = AR(1, 1)
                sage: node.inverse_translation()
                <1, 2>
                sage: node = AR(1, 2)
                sage: node.inverse_translation() is None
                True

                sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
                sage: AR = D.auslander_reiten_quiver()
                sage: AR(2, -1).inverse_translation() is None
                True
            """
        def dimension_vector(self):
            """
            Return the dimension vector of ``self``.

            EXAMPLES::

                sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
                sage: AR = D.auslander_reiten_quiver()
                sage: node = AR(2, -4)
                sage: node.dimension_vector()
                8*v1 + 7*v2
            """

def detect_dynkin_quiver(quiver):
    """
    Determine if ``quiver`` is a finite type Dynkin quiver.

    EXAMPLES::

        sage: from sage.quivers.ar_quiver import detect_dynkin_quiver
        sage: D = DiGraph([[1,2], [2,3], [3, 4], [4,0], ['a','b'], ['b','c'], ['c','d'], ['c','e']])
        sage: detect_dynkin_quiver(D)
        D5xA5

        sage: D = DiGraph([[1,2,'a'], [1,2,'b']], multiedges=True)
        sage: detect_dynkin_quiver(D) is None
        True
        sage: D = DiGraph([[1, 2], [2, 3], [1, 3]])
        sage: detect_dynkin_quiver(D) is None
        True
        sage: D = DiGraph([[1,2], [1,3], [1,4], [1,5]])
        sage: detect_dynkin_quiver(D) is None
        True
        sage: D = DiGraph([[1,2], [2,3], [2,4], [4,5], [6,4]])
        sage: detect_dynkin_quiver(D) is None
        True
        sage: D = DiGraph([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,9], [0,3]])
        sage: detect_dynkin_quiver(D) is None
        True
        sage: D = DiGraph([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [0,4]])
        sage: detect_dynkin_quiver(D) is None
        True
    """
