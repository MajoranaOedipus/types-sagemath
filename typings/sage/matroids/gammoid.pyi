from _typeshed import Incomplete
from collections.abc import Generator
from sage.graphs.digraph import DiGraph as DiGraph
from sage.matroids.matroid import Matroid as Matroid
from sage.matroids.minor_matroid import MinorMatroid as MinorMatroid

class Gammoid(Matroid):
    """
    The gammoid class.

    INPUT:

    - ``D`` -- a loopless digraph representing the gammoid
    - ``roots`` -- a subset of the vertices
    - ``groundset`` -- (optional) a subset of the vertices

    OUTPUT: :class:`Gammoid`; if ``groundset`` is not specified,
    the entire vertex set is used (and the gammoid will be strict)

    EXAMPLES::

        sage: from sage.matroids.gammoid import Gammoid
        sage: D = digraphs.TransitiveTournament(5)
        sage: M = Gammoid(D, roots=[3, 4]); M
        Gammoid of rank 2 on 5 elements
        sage: M.is_isomorphic(matroids.Uniform(2, 5))
        True
        sage: D.add_vertex(6)
        sage: N = Gammoid(D, roots=[3, 4])
        sage: N.loops()
        frozenset({6})
        sage: O = Gammoid(D, roots=[3, 4, 6])
        sage: O.coloops()
        frozenset({6})
        sage: O.full_rank()
        3
        sage: P = Gammoid(D, roots=[3, 4], groundset=[0, 2, 3]); P
        Gammoid of rank 2 on 3 elements
    """
    def __init__(self, D, roots, groundset=None) -> None:
        """
        See the class definition for full documentation.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgedict = {1: [2], 2: [3], 4: [1, 5], 5: [2, 3, 8],
            ....:             6: [4, 7], 7: [5, 8]}
            sage: D = DiGraph(edgedict)
            sage: M = Gammoid(D, roots=[1, 2, 3])
            sage: N1 = Gammoid(D, groundset=range(1, 8), roots=[1, 2, 3])
            sage: N2 = M.delete(8)
            sage: N1 == N2
            True

        TESTS::

            sage: from sage.matroids.gammoid import Gammoid
            sage: D = DiGraph([(0, 0), (0, 1), (1, 1)], loops=True)
            sage: M = Gammoid(D, roots=[1])
            Traceback (most recent call last):
            ...
            ValueError: cannot add edge from 0 to 0 in graph without loops
            sage: D = DiGraph([(0, 1), (0, 1)], multiedges=True)
            sage: M = Gammoid(D, roots=[1])
            sage: M.is_isomorphic(matroids.Uniform(1, 2))
            True
            sage: M = Gammoid(D, roots=[3])
            Traceback (most recent call last):
            ...
            ValueError: roots must be a subset of the vertices
            sage: M = Gammoid(D, roots=[1], groundset=[3])
            Traceback (most recent call last):
            ...
            ValueError: groundset must be a subset of the vertices

        ::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgedict = {1: [2], 2: [3], 4: [1, 5], 5: [2, 3, 8],
            ....:             6: [4, 7], 7: [5, 8]}
            sage: D = DiGraph(edgedict)
            sage: M = Gammoid(D, roots=[]); M
            Gammoid of rank 0 on 8 elements
            sage: M = Gammoid(D, roots=[], groundset=[]); M
            Gammoid of rank 0 on 0 elements

        ::

            sage: from sage.matroids.gammoid import Gammoid
            sage: M = Gammoid(digraphs.TransitiveTournament(5), roots=[3, 4])
            sage: TestSuite(M).run()
            sage: TestSuite(M).run(verbose=True)
            running ._test_category() . . . pass
            running ._test_new() . . . pass
            running ._test_not_implemented_methods() . . . pass
            running ._test_pickling() . . . pass
        """
    def __hash__(self):
        """
        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: D = digraphs.TransitiveTournament(5)
            sage: M1 = Gammoid(D, roots=[3, 4])
            sage: M2 = Gammoid(D, roots=[2, 3])
            sage: hash(M1) == hash(M2)
            False
            sage: N1 = M1.delete(2)
            sage: N2 = Gammoid(D, roots=[3, 4], groundset=[0, 1, 3, 4])
            sage: hash(N1) == hash(N2)
            True
            sage: D.delete_edge(0, 4)
            sage: M3 = Gammoid(D, roots=[3, 4])
            sage: hash(M1) == hash(M3)
            False
        """
    def __eq__(self, other):
        """
        Compare two matroids.

        For two graphic matroids to be equal, all attributes of the underlying
        graphs must be equal.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: ``True`` if ``self`` and ``other`` have the same digraph,
        roots, and groundset; ``False`` otherwise

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: D = digraphs.TransitiveTournament(5)
            sage: M1 = Gammoid(D, roots=[3, 4])
            sage: M2 = Gammoid(D, roots=[2, 3])
            sage: M1 == M2
            False
            sage: N1 = M1.delete(2)
            sage: N2 = Gammoid(D, roots=[3, 4], groundset=[0, 1, 3, 4])
            sage: N1 == N2
            True
        """
    def __ne__(self, other):
        """
        Compare two matroids.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: ``False`` if ``self`` and ``other`` have the same digraphs,
        roots, and groundset; ``True`` otherwise

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgedict = {1: [2], 2: [3], 4: [1, 5], 5: [2, 3, 8], 6: [4, 7],
            ....:             7: [5, 8]}
            sage: D = DiGraph(edgedict)
            sage: M = Gammoid(D, roots=[1, 2, 3])
            sage: D.relabel([1, 2, 3, 4, 5, 6, 7, 'a'])
            sage: N = Gammoid(D, roots=[1, 2, 3])
            sage: M == N
            False
            sage: M.delete(8) == N.delete('a')
            True
        """
    def __reduce__(self):
        '''
        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(E, F, name)`` where ``E`` is
        the groundset, ``F`` is the dictionary of flats, and ``name`` is a
        custom name.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgelist = [(0, 4), (0, 5), (1, 0), (1, 4), (2, 0), (2, 1), (2, 3),
            ....:             (2, 6), (3, 4), (3, 5), (4, 0), (5, 2), (6, 5)]
            sage: D = DiGraph(edgelist)
            sage: M = Gammoid(D, roots=[4, 5, 6])
            sage: M.rename("Example Gammoid: " + repr(M))
            sage: M == loads(dumps(M)), loads(dumps(M))  # indirect doctest
            (True, Example Gammoid: Gammoid of rank 3 on 7 elements)
            sage: M.reset_name()
            sage: loads(dumps(M))
            Gammoid of rank 3 on 7 elements
        '''
    def digraph(self):
        """
        Return the digraph associated with the gammoid.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgelist = [(0, 4), (0, 5), (1, 0), (1, 4), (2, 0), (2, 1), (2, 3),
            ....:             (2, 6), (3, 4), (3, 5), (4, 0), (5, 2), (6, 5)]
            sage: D = DiGraph(edgelist)
            sage: M = Gammoid(D, roots=[4, 5, 6])
            sage: M.digraph() == D
            True
        """
    def digraph_plot(self):
        """
        Plot the graph with color-coded vertices.

        Vertices that are elements but not roots will be shown as blue. Vertices that
        are roots but not elements are red. Vertices that are both are pink, and vertices
        that are neither are grey.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: D = digraphs.TransitiveTournament(4)
            sage: M = Gammoid(D, roots=[2, 3])
            sage: M.digraph_plot()
            Graphics object consisting of 11 graphics primitives
        """
    def groundset(self):
        """
        Return the groundset of the matroid.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgelist = [(0, 4), (0, 5), (1, 0), (1, 4), (2, 0), (2, 1), (2, 3),
            ....:             (2, 6), (3, 4), (3, 5), (4, 0), (5, 2), (6, 5)]
            sage: D = DiGraph(edgelist)
            sage: M = Gammoid(D, roots=[4, 5, 6])
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
        """
    def gammoid_extension(self, vertex, neighbors=[]):
        """
        Return a gammoid extended by an element.

        The new element can be a vertex of the digraph that is not in the starting set,
        or it can be a new source vertex.

        INPUT:

        - ``vertex`` -- a vertex of the gammoid's digraph that is not already in the
          groundset, or a new vertex
        - ``neighbors`` -- (optional) a set of vertices of the digraph

        OUTPUT:

        A :class:`Gammoid`. If ``vertex`` is not already in the graph, then the
        new vertex will be have edges to ``neighbors``. The new vertex will have
        in degree `0` regardless of whether or not ``neighbors`` is specified.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgedict = {1: [2], 2: [3], 4: [1, 5], 5: [2, 3, 8],
            ....:             6: [4, 7], 7: [5, 8]}
            sage: D = DiGraph(edgedict)
            sage: M = Gammoid(D, roots=[2, 3, 4], groundset=range(2, 9))
            sage: M1 = M.gammoid_extension(1)
            sage: M1.groundset()
            frozenset({1, 2, 3, 4, 5, 6, 7, 8})
            sage: N = Gammoid(D, roots=[2, 3, 4])
            sage: M1 == N
            True
            sage: M1.delete(1)
            Gammoid of rank 3 on 7 elements
            sage: M == M1.delete(1)
            True
            sage: M2 = M.gammoid_extension(9); sorted(M2.loops())
            [8, 9]
            sage: M4 = M.gammoid_extension(9, [1, 2, 3])
            sage: M4.digraph().neighbors_out(9)
            [1, 2, 3]
            sage: M4.digraph().neighbors_in(9)
            []

        TESTS::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgedict = {1: [2], 2: [3], 4: [1, 5], 5: [2, 3, 8],
            ....:             6: [4, 7], 7: [5, 8]}
            sage: D = DiGraph(edgedict)
            sage: M = Gammoid(D, roots=[2, 3, 4], groundset=range(2, 9))
            sage: M.gammoid_extension(2)
            Traceback (most recent call last):
            ...
            ValueError: cannot extend by element already in groundset
            sage: M.gammoid_extension(1, [2, 3, 4])
            Traceback (most recent call last):
            ...
            ValueError: neighbors of vertex in digraph cannot be changed
            sage: M.gammoid_extension(9, [9])
            Traceback (most recent call last):
            ...
            ValueError: neighbors must already be in graph
        """
    def gammoid_extensions(self, vertices=None) -> Generator[Incomplete]:
        """
        Return an iterator of Gammoid extensions.

        This will only consider extensions from vertices that are already present
        in the digraph.

        INPUT:

        - ``vertices`` -- (optional) a list of vertices not in the digraph

        OUTPUT:

        An iterator of Gammoids. If ``vertices`` is not specified, every vertex
        not already in the groundset will be considered.

        EXAMPLES::

            sage: from sage.matroids.gammoid import Gammoid
            sage: M = Gammoid(digraphs.TransitiveTournament(5), roots=[3, 4],
            ....:             groundset=[0, 1, 4])
            sage: [sorted(M1.groundset()) for M1 in M.gammoid_extensions()]
            [[0, 1, 2, 4], [0, 1, 3, 4]]
            sage: N = Gammoid(digraphs.TransitiveTournament(5), roots=[3, 4])
            sage: [sorted(N1.groundset()) for N1 in N.gammoid_extensions()]
            []

        ::

            sage: from sage.matroids.gammoid import Gammoid
            sage: edgelist =[(i, i+1) for i in range(10)]
            sage: M = Gammoid(DiGraph(edgelist), roots=[9], groundset=[0])
            sage: sum(1 for M1 in M.gammoid_extensions(vertices=[3, 4, 5]))
            3
            sage: sum(1 for M1 in M.gammoid_extensions())
            9
            sage: set([M1.is_isomorphic(matroids.Uniform(1, 2))
            ....:      for M1 in M.gammoid_extensions()])
            {True}
            sage: len([M1 for M1 in M.gammoid_extensions([0, 1, 2])])
            Traceback (most recent call last):
            ...
            ValueError: vertices must be in the digraph and not already in the groundset
        """
