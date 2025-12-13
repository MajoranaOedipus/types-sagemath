from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.posets.posets import Poset as Poset
from sage.combinat.subset import powerset as powerset
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.graphs.graph import Graph as Graph
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.topology.cell_complex import GenericCellComplex as GenericCellComplex

class PolyhedralComplex(GenericCellComplex):
    '''
    A polyhedral complex.

    A **polyhedral complex** `PC` is a collection of polyhedra in a certain
    ambient space `\\RR^n` such that the following hold.

    - If a polyhedron `P` is in `PC`, then all the faces of `P` are in `PC`.

    - If polyhedra `P` and `Q` are in `PC`, then `P \\cap Q` is either empty
      or a face of both `P` and `Q`.

    In this context, a "polyhedron" means the geometric realization
    of a polyhedron. This is in contrast to :mod:`simplicial complex
    <sage.topology.simplicial_complex>`, whose cells are abstract simplices.
    The concept of a polyhedral complex generalizes that of a **geometric**
    simplicial complex.

    .. NOTE::

       This class derives from
       :class:`~sage.topology.cell_complex.GenericCellComplex`, and so
       inherits its methods.  Some of those methods are not listed here;
       see the :mod:`Generic Cell Complex <sage.topology.cell_complex>`
       page instead.

    INPUT:

    - ``maximal_cells`` -- list, tuple, or dictionary (indexed by
      dimension) of cells of the Complex. Each cell is of class
      :class:`Polyhedron` of the same ambient dimension. To set up a
      :class:PolyhedralComplex, it is sufficient to provide the maximal
      faces. Use keyword argument ``partial=True`` to set up a partial
      polyhedral complex, which is a subset of the faces (viewed as
      relatively open) of a polyhedral complex that is not necessarily
      closed under taking intersection.

    - ``maximality_check`` -- boolean (default: ``True``);
      if ``True``, then the constructor checks that each given
      maximal cell is indeed maximal, and ignores those that are not

    - ``face_to_face_check`` -- boolean (default: ``False``);
      if ``True``, then the constructor checks whether the cells
      are face-to-face, and it raises a :exc:`ValueError` if they are not

    - ``is_mutable`` and ``is_immutable`` -- boolean (default: ``True`` and
      ``False`` respectively); set ``is_mutable=False`` or ``is_immutable=True``
      to make this polyhedral complex immutable

    - ``backend`` -- string (optional); the name of the backend used for
      computations on Sage polyhedra; if it is not given, then each cell has
      its own backend; otherwise it must be one of the following:

      * ``\'ppl\'`` -- the Parma Polyhedra Library

      * ``\'cdd\'`` -- CDD

      * ``\'normaliz\'`` -- normaliz

      * ``\'polymake\'`` -- polymake

      * ``\'field\'`` -- a generic Sage implementation

    - ``ambient_dim`` -- integer (optional); used to set up an empty
      complex in the intended ambient space

    EXAMPLES::

        sage: pc = PolyhedralComplex([
        ....:         Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1/7, 2/7)]),
        ....:         Polyhedron(vertices=[(1/7, 2/7), (0, 0), (0, 1/4)])])
        sage: [p.Vrepresentation() for p in pc.cells_sorted()]
        [(A vertex at (0, 0), A vertex at (0, 1/4), A vertex at (1/7, 2/7)),
         (A vertex at (0, 0), A vertex at (1/3, 1/3), A vertex at (1/7, 2/7)),
         (A vertex at (0, 0), A vertex at (0, 1/4)),
         (A vertex at (0, 0), A vertex at (1/7, 2/7)),
         (A vertex at (0, 0), A vertex at (1/3, 1/3)),
         (A vertex at (0, 1/4), A vertex at (1/7, 2/7)),
         (A vertex at (1/3, 1/3), A vertex at (1/7, 2/7)),
         (A vertex at (0, 0),),
         (A vertex at (0, 1/4),),
         (A vertex at (1/7, 2/7),),
         (A vertex at (1/3, 1/3),)]
        sage: pc.plot()                                                                 # needs sage.plot
        Graphics object consisting of 10 graphics primitives
        sage: pc.is_pure()
        True
        sage: pc.is_full_dimensional()
        True
        sage: pc.is_compact()
        True
        sage: pc.boundary_subcomplex()
        Polyhedral complex with 4 maximal cells
        sage: pc.is_convex()
        True
        sage: pc.union_as_polyhedron().Hrepresentation()
        (An inequality (1, -4) x + 1 >= 0,
         An inequality (-1, 1) x + 0 >= 0,
         An inequality (1, 0) x + 0 >= 0)
        sage: pc.face_poset()
        Finite poset containing 11 elements
        sage: pc.is_connected()
        True
        sage: pc.connected_component() == pc
        True

    TESTS:

    Check that non-maximal cells are ignored if ``maximality_check=True``::

        sage: pc = PolyhedralComplex([
        ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
        ....:         Polyhedron(vertices=[(1, 2), (0, 0)]) ])
        sage: pc.maximal_cells()
        {2: {A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices}}

    Check that non face-to-face can be detected::

        sage: PolyhedralComplex([
        ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
        ....:         Polyhedron(vertices=[(2, 2), (0, 0)]) ],
        ....:         face_to_face_check=True)
        Traceback (most recent call last):
        ...
        ValueError: the given cells are not face-to-face

    Check that all the cells must have the same ambient dimension::

        sage: PolyhedralComplex([
        ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
        ....:         Polyhedron(vertices=[[2], [0]]) ])
        Traceback (most recent call last):
        ...
        ValueError: the given cells are not polyhedra in the same ambient space

    Check that backend is passed to all the cells::

        sage: P = Polyhedron(vertices=[(0, 0), (1, 1)])
        sage: P.backend()
        \'ppl\'
        sage: pc = PolyhedralComplex([P], backend=\'cdd\')
        sage: Q = pc.maximal_cells_sorted()[0]
        sage: Q.backend()
        \'cdd\'
    '''
    def __init__(self, maximal_cells=None, backend=None, maximality_check: bool = True, face_to_face_check: bool = False, is_mutable: bool = True, is_immutable: bool = False, ambient_dim=None) -> None:
        """
        Define a PolyhedralComplex.

        See ``PolyhedralComplex`` for more information.

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[(1, 1), (0, 0)])])
            sage: pc
            Polyhedral complex with 1 maximal cell
            sage: TestSuite(pc).run()
        """
    def cells(self, subcomplex=None) -> dict:
        """
        The cells of this polyhedral complex, in the form of a dictionary:
        the keys are integers, representing dimension, and the value
        associated to an integer `d` is the set of `d`-cells.

        INPUT:

        - ``subcomplex`` -- (optional) if a subcomplex is given then
          return the cells which are **not** in this subcomplex

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: list(pc.cells().keys())
            [2, 1, 0]
        """
    def cell_iterator(self, increasing: bool = True) -> Generator[Incomplete, Incomplete]:
        """
        An iterator for the cells in this polyhedral complex.

        INPUT:

        - ``increasing`` -- boolean (default: ``True``); if ``True``, return
          cells in increasing order of dimension, thus starting with the
          zero-dimensional cells; otherwise it returns cells in decreasing
          order of dimension

        .. NOTE::

            Among the cells of a fixed dimension, there is no sorting.

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: len(list(pc.cell_iterator()))
            11
        """
    def cells_sorted(self, subcomplex=None) -> list:
        """
        The sorted list of the cells of this polyhedral complex
        in non-increasing dimensions.

        INPUT:

        - ``subcomplex`` -- (optional) if a subcomplex is given then
          return the cells which are **not** in this subcomplex

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....: Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....: Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: len(pc.cells_sorted())
            11
            sage: pc.cells_sorted()[0].Vrepresentation()
            (A vertex at (0, 0), A vertex at (0, 2), A vertex at (1, 2))
        """
    def maximal_cells(self) -> dict:
        """
        The maximal cells of this polyhedral complex, in the form of a
        dictionary: the keys are integers, representing dimension, and the
        value associated to an integer `d` is the set of `d`-maximal cells.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: len(pc.maximal_cells()[2])
            2
            sage: 1 in pc.maximal_cells()
            False

        Wrong answer due to ``maximality_check=False``::

            sage: pc_invalid = PolyhedralComplex([p1, p2, p3],
            ....:              maximality_check=False)
            sage: len(pc_invalid.maximal_cells()[1])
            1
        """
    def maximal_cell_iterator(self, increasing: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        An iterator for the maximal cells in this polyhedral complex.

        INPUT:

        - ``increasing`` -- boolean (default: ``False``); if ``True``, return
          maximal cells in increasing order of dimension.
          Otherwise it returns cells in decreasing order of dimension.

        .. NOTE::

            Among the cells of a fixed dimension, there is no sorting.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: len(list(pc.maximal_cell_iterator()))
            2

        Wrong answer due to ``maximality_check=False``::

            sage: pc_invalid = PolyhedralComplex([p1, p2, p3],
            ....:              maximality_check=False)
            sage: len(list(pc_invalid.maximal_cell_iterator()))
            3
        """
    def n_maximal_cells(self, n) -> list:
        """
        List of maximal cells of dimension ``n`` of this polyhedral complex.

        INPUT:

        - ``n`` -- nonnegative integer; the dimension

        .. NOTE::

            The resulting list need not be sorted. If you want a sorted
            list of `n`-cells, use :meth:`_n_maximal_cells_sorted`.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: len(pc.n_maximal_cells(2))
            2
            sage: len(pc.n_maximal_cells(1))
            0

        Wrong answer due to ``maximality_check=False``::

            sage: pc_invalid = PolyhedralComplex([p1, p2, p3],
            ....:              maximality_check=False)
            sage: len(pc_invalid.n_maximal_cells(1))
            1
        """
    def maximal_cells_sorted(self) -> list:
        """
        Return the sorted list of the maximal cells of this polyhedral complex
        by non-increasing dimensions.

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: [p.vertices_list() for p in pc.maximal_cells_sorted()]
            [[[0, 0], [0, 2], [1, 2]], [[0, 0], [1, 1], [1, 2]]]
        """
    def is_maximal_cell(self, c) -> bool:
        """
        Return whether the given cell ``c`` is a maximal cell of ``self``.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: pc.is_maximal_cell(p1)
            True
            sage: pc.is_maximal_cell(p3)
            False

        Wrong answer due to ``maximality_check=False``::

            sage: pc_invalid = PolyhedralComplex([p1, p2, p3],
            ....:              maximality_check=False)
            sage: pc_invalid.is_maximal_cell(p3)
            True
        """
    def is_cell(self, c) -> bool:
        """
        Return whether the given cell ``c`` is a cell of ``self``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2])
            sage: pc.is_cell(p3)
            True
            sage: pc.is_cell(Polyhedron(vertices=[(0, 0)]))
            True
        """
    def dimension(self):
        """
        The dimension of this cell complex: the maximum
        dimension of its cells.

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 2)]) ])
            sage: pc.dimension()
            2
            sage: empty_pc = PolyhedralComplex([])
            sage: empty_pc.dimension()
            -1
        """
    def ambient_dimension(self):
        """
        The ambient dimension of this cell complex: the ambient
        dimension of each of its cells.

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[(1, 2, 3)])])
            sage: pc.ambient_dimension()
            3
            sage: empty_pc = PolyhedralComplex([])
            sage: empty_pc.ambient_dimension()
            -1
            sage: pc0 = PolyhedralComplex(ambient_dim=2)
            sage: pc0.ambient_dimension()
            2
        """
    def plot(self, **kwds):
        """
        Return a plot of the polyhedral complex, if it is of dim at most 3.

        INPUT:

        - ``explosion_factor`` -- (default: 0) if positive, separate the cells of
          the complex by extra space. In this case, the following keyword arguments
          can be passed to :func:`exploded_plot`:

          - ``center`` -- (default: ``None``, denoting the origin) the center of explosion
          - ``sticky_vertices`` -- (default: ``False``) boolean or dict;
            whether to draw line segments between shared vertices of the given polyhedra.
            A dict gives options for :func:`sage.plot.line`.
          - ``sticky_center`` -- (default: ``True``) boolean or dict. When ``center`` is
            a vertex of some of the polyhedra, whether to draw line segments connecting the
            ``center`` to the shifted copies of these vertices.
            A dict gives options for :func:`sage.plot.line`.

        - ``color`` -- (default: ``None``) if ``'rainbow'``, assign a different color
          to every maximal cell; otherwise, passed on to
          :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.plot`.

        - other keyword arguments are passed on to
          :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.plot`.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(0, 0), (0, 2), (-1, 1)])
            sage: pc1 = PolyhedralComplex([p1, p2, p3, -p1, -p2, -p3])
            sage: bb = dict(xmin=-2, xmax=2, ymin=-3, ymax=3, axes=False)
            sage: g0 = pc1.plot(color='rainbow', **bb)                                  # needs sage.plot
            sage: g1 = pc1.plot(explosion_factor=0.5, **bb)                             # needs sage.plot
            sage: g2 = pc1.plot(explosion_factor=1, color='rainbow', alpha=0.5, **bb)   # needs sage.plot
            sage: graphics_array([g0, g1, g2]).show(axes=False)                        # not tested

            sage: pc2 = PolyhedralComplex([polytopes.hypercube(3)])
            sage: pc3 = pc2.subdivide(new_vertices=[(0, 0, 0)])
            sage: g3 = pc3.plot(explosion_factor=1, color='rainbow',                    # needs sage.plot
            ....:               alpha=0.5, axes=False, online=True)
            sage: pc4 = pc2.subdivide(make_simplicial=True)
            sage: g4 = pc4.plot(explosion_factor=1, center=(1, -1, 1), fill='blue',     # needs sage.plot
            ....:              wireframe='white', point={'color':'red', 'size':10},
            ....:              alpha=0.6, online=True)
            sage: pc5 = PolyhedralComplex([
            ....:         Polyhedron(rays=[[1,0,0], [0,1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[1,0,0], [0,-1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[1,0,0], [0,-1,0], [0,0,1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,-1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,-1,0], [0,0,1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,1,0], [0,0,1]])])
            sage: g5 = pc5.plot(explosion_factor=0.3, color='rainbow', alpha=0.8,       # needs sage.plot
            ....:               point={'size': 20}, axes=False, online=True)
        """
    def is_pure(self) -> bool:
        """
        Test if this polyhedral complex is pure.

        A polyhedral complex is pure if and only if all of its maximal cells
        have the same dimension.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: pc.is_pure()
            True

        Wrong answer due to ``maximality_check=False``::

            sage: pc_invalid = PolyhedralComplex([p1, p2, p3],
            ....:              maximality_check=False)
            sage: pc_invalid.is_pure()
            False
        """
    def is_full_dimensional(self) -> bool:
        """
        Return whether this polyhedral complex is full-dimensional.

        This means that its dimension is equal to its ambient dimension.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: pc.is_full_dimensional()
            True
            sage: PolyhedralComplex([p3]).is_full_dimensional()
            False
        """
    def __hash__(self) -> int:
        """
        Compute the hash value of ``self`` using its ``maximal_cells_sorted``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])
            sage: pc1 = PolyhedralComplex([p1, p2], is_mutable=False)
            sage: hash(pc1) == hash(pc1)
            True
            sage: pc2 = PolyhedralComplex([p2, p1], is_mutable=False)
            sage: hash(pc1) == hash(pc2)
            True
            sage: pc3 = PolyhedralComplex([p1, p2])
            sage: hash(pc3)
            Traceback (most recent call last):
            ...
            ValueError: this polyhedral complex must be immutable; call set_immutable()
        """
    def __eq__(self, right) -> bool:
        """
        Two polyhedral complexes are equal iff their maximal cells are equal.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])
            sage: pc1 = PolyhedralComplex([p1, p2])
            sage: pc1 == pc1
            True
            sage: pc2 = PolyhedralComplex([p2, p1])
            sage: pc1 == pc2
            True
        """
    def __ne__(self, right) -> bool:
        """
        Return ``True`` if ``self`` and ``right`` are not equal.

        EXAMPLES::

            sage: pc1 = PolyhedralComplex([
            ....: Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)])])
            sage: pc2 = PolyhedralComplex([
            ....: Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])])
            sage: pc1 != pc2
            True
        """
    def __copy__(self):
        """
        Return a mutable copy of ``self``.

        EXAMPLES::

            sage: pc1 = PolyhedralComplex([Polyhedron(vertices=[(0, 0)])])
            sage: pc2 = copy(pc1)
            sage: pc1 == pc2
            True
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is a polyhedron which is contained in this complex.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])
            sage: pc = PolyhedralComplex([p1, p2])
            sage: (p1 in pc) and (p2 in pc)
            True
            sage: Polyhedron(vertices=[(1, 2), (0, 0)]) in pc
            True
            sage: Polyhedron(vertices=[(1, 1), (0, 0)]) in pc
            False
            sage: Polyhedron(vertices=[(0, 0)]) in pc
            True
            sage: (0, 0) in pc  # not a polyhedron
            False
        """
    def __call__(self, x):
        """
        If ``x`` is a polyhedron in this complex, return it.
        Otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])])
            sage: pc(Polyhedron(vertices=[(1, 2), (0, 0)]))
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: pc(Polyhedron(vertices=[(1, 1)]))
            Traceback (most recent call last):
            ...
            ValueError: the polyhedron is not in this complex
        """
    def face_poset(self):
        """
        The face poset of this polyhedral complex, the poset of
        nonempty cells, ordered by inclusion.

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])])
            sage: poset = pc.face_poset()
            sage: poset
            Finite poset containing 11 elements
            sage: d = {i: i.vertices_matrix() for i in poset}
            sage: poset.plot(element_labels=d)                                          # needs sage.plot
            Graphics object consisting of 28 graphics primitives

        For a nonbounded polyhedral complex::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)]),
            ....:         Polyhedron(vertices=[(-1/2, -1/2)], lines=[(1, -1)]),
            ....:         Polyhedron(rays=[(1, 0)])])
            sage: poset = pc.face_poset()
            sage: poset
            Finite poset containing 13 elements
            sage: d = {i:''.join([str(v)+'\\n'
            ....:      for v in i.Vrepresentation()]) for i in poset}
            sage: poset.show(element_labels=d, figsize=15)        # not tested
            sage: pc = PolyhedralComplex([
            ....: Polyhedron(rays=[(1,0),(0,1)]),
            ....: Polyhedron(rays=[(-1,0),(0,1)]),
            ....: Polyhedron(rays=[(-1,0),(0,-1)]),
            ....: Polyhedron(rays=[(1,0),(0,-1)])])
            sage: pc.face_poset()
            Finite poset containing 9 elements
        """
    def is_subcomplex(self, other) -> bool:
        """
        Return whether ``self`` is a subcomplex of ``other``.

        INPUT:

        - ``other`` -- a polyhedral complex

        Each maximal cell of ``self`` must be a cell of ``other``
        for this to be ``True``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])
            sage: p3 = Polyhedron(vertices=[(0, 0), (1, 0)])
            sage: pc = PolyhedralComplex([p1, Polyhedron(vertices=[(1, 0)])])
            sage: pc.is_subcomplex(PolyhedralComplex([p1, p2, p3]))
            True
            sage: pc.is_subcomplex(PolyhedralComplex([p1, p2]))
            False
        """
    def is_compact(self) -> bool:
        """
        Test for boundedness of the polyhedral complex.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)])
            sage: p2 = Polyhedron(rays=[(1, 0)])
            sage: PolyhedralComplex([p1]).is_compact()
            True
            sage: PolyhedralComplex([p1, p2]).is_compact()
            False
        """
    def graph(self):
        """
        Return the 1-skeleton of this polyhedral complex, as a graph.

        The vertices of the graph are of type ``vector``. This raises
        a :exc:`NotImplementedError` if the polyhedral complex is unbounded.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: g = pc.graph(); g
            Graph on 4 vertices
            sage: g.vertices(sort=True)
            [(0, 0), (0, 2), (1, 1), (1, 2)]
            sage: g.edges(sort=True, labels=False)
            [((0, 0), (0, 2)), ((0, 0), (1, 1)), ((0, 0), (1, 2)), ((0, 2), (1, 2)), ((1, 1), (1, 2))]
            sage: PolyhedralComplex([Polyhedron(rays=[(1,1)])]).graph()
            Traceback (most recent call last):
            ...
            NotImplementedError: the polyhedral complex is unbounded

        Wrong answer due to ``maximality_check=False``::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: PolyhedralComplex([p1, p2]).is_pure()
            True
            sage: PolyhedralComplex([p2, p3], maximality_check=True).is_pure()
            True
            sage: PolyhedralComplex([p2, p3], maximality_check=False).is_pure()
            False
        """
    def is_connected(self) -> bool:
        """
        Return whether ``self`` is connected.

        EXAMPLES::

            sage: pc1 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: pc1.is_connected()
            True
            sage: pc2 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(0, 2)])])
            sage: pc2.is_connected()
            False
            sage: pc3 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 1/2)]),
            ....:         Polyhedron(vertices=[(-1/2, -1/2)], lines=[(1, -1)]),
            ....:         Polyhedron(rays=[(1, 0)])])
            sage: pc3.is_connected()
            False
            sage: pc4 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1/3, 1/3), (0, 0), (1, 2)]),
            ....:         Polyhedron(rays=[(1, 0)])])
            sage: pc4.is_connected()
            True
        """
    def connected_component(self, cell=None):
        """
        Return the connected component of this polyhedral complex
        containing a given cell.

        INPUT:

        - ``cell`` -- (default: ``self.an_element()``) a cell of ``self``

        OUTPUT:

        The connected component containing ``cell``. If the polyhedral complex
        is empty or if it does not contain the given cell, raise an error.

        EXAMPLES::

            sage: t1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: t2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: v1 = Polyhedron(vertices=[(1, 1)])
            sage: v2 = Polyhedron(vertices=[(0, 2)])
            sage: v3 = Polyhedron(vertices=[(-1, 0)])
            sage: o =  Polyhedron(vertices=[(0, 0)])
            sage: r = Polyhedron(rays=[(1, 0)])
            sage: l = Polyhedron(vertices=[(-1, 0)], lines=[(1, -1)])
            sage: pc1 = PolyhedralComplex([t1, t2])
            sage: pc1.connected_component() == pc1
            True
            sage: pc1.connected_component(v1) == pc1
            True
            sage: pc2 = PolyhedralComplex([t1, v2])
            sage: pc2.connected_component(t1) == PolyhedralComplex([t1])
            True
            sage: pc2.connected_component(o) == PolyhedralComplex([t1])
            True
            sage: pc2.connected_component(v3)
            Traceback (most recent call last):
            ...
            ValueError: the polyhedral complex does not contain the given cell
            sage: pc2.connected_component(r)
            Traceback (most recent call last):
            ...
            ValueError: the polyhedral complex does not contain the given cell
            sage: pc3 = PolyhedralComplex([t1, t2, r])
            sage: pc3.connected_component(v2) == pc3
            True
            sage: pc4 = PolyhedralComplex([t1, t2, r, l])
            sage: pc4.connected_component(o) == pc3
            True
            sage: pc4.connected_component(v3)
            Traceback (most recent call last):
            ...
            ValueError: the polyhedral complex does not contain the given cell
            sage: pc5 = PolyhedralComplex([t1, t2, r, l, v3])
            sage: pc5.connected_component(v3) == PolyhedralComplex([v3])
            True
            sage: PolyhedralComplex([]).connected_component()
            Traceback (most recent call last):
            ...
            ValueError: the empty polyhedral complex has no connected components
        """
    def connected_components(self) -> list:
        """
        Return the connected components of this polyhedral complex,
        as list of (sub-)PolyhedralComplexes.

        EXAMPLES::

            sage: t1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: t2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: v1 = Polyhedron(vertices=[(1, 1)])
            sage: v2 = Polyhedron(vertices=[(0, 2)])
            sage: v3 = Polyhedron(vertices=[(-1, 0)])
            sage: o =  Polyhedron(vertices=[(0, 0)])
            sage: r = Polyhedron(rays=[(1, 0)])
            sage: l = Polyhedron(vertices=[(-1, 0)], lines=[(1, -1)])
            sage: pc1 = PolyhedralComplex([t1, t2])
            sage: len(pc1.connected_components())
            1
            sage: pc2 = PolyhedralComplex([t1, v2])
            sage: len(pc2.connected_components())
            2
            sage: pc3 = PolyhedralComplex([t1, t2, r])
            sage: len(pc3.connected_components())
            1
            sage: pc4 = PolyhedralComplex([t1, t2, r, l])
            sage: len(pc4.connected_components())
            2
            sage: pc5 = PolyhedralComplex([t1, t2, r, l, v3])
            sage: len(pc5.connected_components())
            3
            sage: PolyhedralComplex([]).connected_components()
            Traceback (most recent call last):
            ...
            ValueError: the empty polyhedral complex has no connected components
        """
    def n_skeleton(self, n):
        """
        The `n`-skeleton of this polyhedral complex.

        The `n`-skeleton of a polyhedral complex is obtained by discarding
        all of the cells in dimensions larger than `n`.

        INPUT:

        - ``n`` -- nonnegative integer; the dimension

        .. SEEALSO::

            :meth:`stratify`

        EXAMPLES::

            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]),
            ....:         Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])])
            sage: pc.n_skeleton(2)
            Polyhedral complex with 2 maximal cells
            sage: pc.n_skeleton(1)
            Polyhedral complex with 5 maximal cells
            sage: pc.n_skeleton(0)
            Polyhedral complex with 4 maximal cells
        """
    def stratify(self, n):
        """
        Return the pure sub-polyhedral complex which is constructed from the
        `n`-dimensional maximal cells of this polyhedral complex.

        .. SEEALSO::

            :meth:`n_skeleton`

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: pc = PolyhedralComplex([p1, p2, p3])
            sage: pc.stratify(2) == pc
            True
            sage: pc.stratify(1)
            Polyhedral complex with 0 maximal cells

        Wrong answer due to ``maximality_check=False``::

            sage: pc_invalid = PolyhedralComplex([p1, p2, p3],
            ....:                                maximality_check=False)
            sage: pc_invalid.stratify(1)
            Polyhedral complex with 1 maximal cell
        """
    def boundary_subcomplex(self):
        """
        Return the sub-polyhedral complex that is the boundary of ``self``.

        A point `P` is on the boundary of a set `S` if `P` is in the
        closure of `S` but not in the interior of `S`.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: bd = PolyhedralComplex([p1, p2]).boundary_subcomplex()
            sage: len(bd.n_maximal_cells(2))
            0
            sage: len(bd.n_maximal_cells(1))
            4
            sage: pt = PolyhedralComplex([p3])
            sage: pt.boundary_subcomplex() == pt
            True

        Test on polyhedral complex which is not pure::

            sage: pc_non_pure = PolyhedralComplex([p1, p3])
            sage: pc_non_pure.boundary_subcomplex() == pc_non_pure.n_skeleton(1)
            True

        Test with ``maximality_check == False``::

            sage: pc_invalid = PolyhedralComplex([p2, p3],
            ....:                                maximality_check=False)
            sage: pc_invalid.boundary_subcomplex() == pc_invalid.n_skeleton(1)
            True

        Test unbounded cases::

            sage: pc1 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,0], [0,1]])])
            sage: pc1.boundary_subcomplex() == pc1.n_skeleton(1)
            True
            sage: pc1b = PolyhedralComplex([Polyhedron(
            ....:         vertices=[[1,0,0], [0,1,0]], rays=[[1,0,0],[0,1,0]])])
            sage: pc1b.boundary_subcomplex() == pc1b
            True
            sage: pc2 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[-1,0], [1,0]], lines=[[0,1]])])
            sage: pc2.boundary_subcomplex() == pc2.n_skeleton(1)
            True
            sage: pc3 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,0], [0,1]]),
            ....:         Polyhedron(vertices=[[1,0], [0,-1]], rays=[[1,0], [0,-1]])])
            sage: pc3.boundary_subcomplex() == pc3.n_skeleton(1)
            False
        """
    def relative_boundary_cells(self) -> list:
        """
        Return the maximal cells of the relative-boundary sub-complex.

        A point `P` is in the relative boundary of a set `S` if `P` is in the
        closure of `S` but not in the relative interior of `S`.

        .. WARNING::

            This may give the wrong answer if the polyhedral complex
            was constructed with ``maximality_check`` set to ``False``.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(1, 2), (0, 2)])
            sage: p4 = Polyhedron(vertices=[(2, 2)])
            sage: pc = PolyhedralComplex([p1, p2])
            sage: rbd_cells = pc.relative_boundary_cells()
            sage: len(rbd_cells)
            4
            sage: all(p.dimension() == 1 for p in rbd_cells)
            True
            sage: pc_lower_dim = PolyhedralComplex([p3])
            sage: sorted([p.vertices() for p in pc_lower_dim.relative_boundary_cells()])
            [(A vertex at (0, 2),), (A vertex at (1, 2),)]

        Test on polyhedral complex which is not pure::

            sage: pc_non_pure = PolyhedralComplex([p1, p3, p4])
            sage: (set(pc_non_pure.relative_boundary_cells())
            ....:  == set([f.as_polyhedron() for f in p1.faces(1)] + [p3, p4]))
            True

        Test with ``maximality_check == False``::

            sage: pc_invalid = PolyhedralComplex([p2, p3],
            ....:                                maximality_check=False)
            sage: (set(pc_invalid.relative_boundary_cells())
            ....:  == set([f.as_polyhedron() for f in p2.faces(1)]))
            True

        Test unbounded case::

            sage: pc3 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,0], [0,1]]),
            ....:         Polyhedron(vertices=[[1,0], [0,-1]], rays=[[1,0], [0,-1]])])
            sage: len(pc3.relative_boundary_cells())
            4
        """
    def is_convex(self) -> bool:
        """
        Return whether the set of points in ``self`` is a convex set.

        When ``self`` is convex, the union of its cells is a Polyhedron.

        .. SEEALSO::

            :meth:`union_as_polyhedron`

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(0, 0), (1, 1), (2, 0)])
            sage: p4 = Polyhedron(vertices=[(2, 2)])
            sage: PolyhedralComplex([p1, p2]).is_convex()
            True
            sage: PolyhedralComplex([p1, p3]).is_convex()
            False
            sage: PolyhedralComplex([p1, p4]).is_convex()
            False

        Test unbounded cases::

            sage: pc1 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,0], [0,1]])])
            sage: pc1.is_convex()
            True
            sage: pc2 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[-1,0], [1,0]], lines=[[0,1]])])
            sage: pc2.is_convex()
            True
            sage: pc3 = PolyhedralComplex([
            ....:         Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,0], [0,1]]),
            ....:         Polyhedron(vertices=[[1,0], [0,-1]], rays=[[1,0], [0,-1]])])
            sage: pc3.is_convex()
            False
            sage: pc4 = PolyhedralComplex([Polyhedron(rays=[[1,0], [-1,1]]),
            ....:                          Polyhedron(rays=[[1,0], [-1,-1]])])
            sage: pc4.is_convex()
            False

        The whole 3d space minus the first orthant is not convex::

            sage: pc5 = PolyhedralComplex([
            ....:         Polyhedron(rays=[[1,0,0], [0,1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[1,0,0], [0,-1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[1,0,0], [0,-1,0], [0,0,1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,-1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,-1,0], [0,0,1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,1,0], [0,0,-1]]),
            ....:         Polyhedron(rays=[[-1,0,0], [0,1,0], [0,0,1]])])
            sage: pc5.is_convex()
            False

        Test some non-full-dimensional examples::

            sage: l = PolyhedralComplex([Polyhedron(vertices=[(1, 2), (0, 2)])])
            sage: l.is_convex()
            True
            sage: pc1b = PolyhedralComplex([Polyhedron(
            ....:         vertices=[[1,0,0], [0,1,0]], rays=[[1,0,0],[0,1,0]])])
            sage: pc1b.is_convex()
            True
            sage: pc4b = PolyhedralComplex([
            ....:         Polyhedron(rays=[[1,0,0], [-1,1,0]]),
            ....:         Polyhedron(rays=[[1,0,0], [-1,-1,0]])])
            sage: pc4b.is_convex()
            False
        """
    def union_as_polyhedron(self):
        """
        Return ``self`` as a :class:`Polyhedron` if ``self`` is convex.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: p3 = Polyhedron(vertices=[(0, 0), (1, 1), (2, 0)])
            sage: P = PolyhedralComplex([p1, p2]).union_as_polyhedron()
            sage: P.vertices_list()
            [[0, 0], [0, 2], [1, 1], [1, 2]]
            sage: PolyhedralComplex([p1, p3]).union_as_polyhedron()
            Traceback (most recent call last):
            ...
            ValueError: the polyhedral complex is not convex
        """
    def product(self, right):
        """
        The (Cartesian) product of this polyhedral complex with another one.

        INPUT:

        - ``right`` -- the other polyhedral complex (the right-hand factor)

        OUTPUT: the product ``self x right``

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc_square = pc.product(pc)
            sage: pc_square
            Polyhedral complex with 1 maximal cell
            sage: next(pc_square.maximal_cell_iterator()).vertices()
            (A vertex at (0, 0),
             A vertex at (0, 1),
             A vertex at (1, 0),
             A vertex at (1, 1))
        """
    def disjoint_union(self, right):
        """
        The disjoint union of this polyhedral complex with another one.

        INPUT:

        - ``right`` -- the other polyhedral complex (the right-hand factor)

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(-1, 0), (0, 0), (0, 1)])
            sage: p2 = Polyhedron(vertices=[(0, -1), (0, 0), (1, 0)])
            sage: p3 = Polyhedron(vertices=[(0, -1), (1, -1), (1, 0)])
            sage: pc = PolyhedralComplex([p1]).disjoint_union(PolyhedralComplex([p3]))
            sage: set(pc.maximal_cell_iterator()) == set([p1, p3])
            True
            sage: pc.disjoint_union(PolyhedralComplex([p2]))
            Traceback (most recent call last):
            ...
            ValueError: the two complexes are not disjoint
        """
    def union(self, right):
        """
        The union of this polyhedral complex with another one.

        INPUT:

        - ``right`` -- the other polyhedral complex (the right-hand factor)

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(-1, 0), (0, 0), (0, 1)])
            sage: p2 = Polyhedron(vertices=[(0, -1), (0, 0), (1, 0)])
            sage: p3 = Polyhedron(vertices=[(0, -1), (1, -1), (1, 0)])
            sage: pc = PolyhedralComplex([p1]).union(PolyhedralComplex([p3]))
            sage: set(pc.maximal_cell_iterator()) == set([p1, p3])
            True
            sage: pc.union(PolyhedralComplex([p2]))
            Polyhedral complex with 3 maximal cells
            sage: p4 = Polyhedron(vertices=[(0, -1), (0, 0), (1, 0), (1, -1)])
            sage: pc.union(PolyhedralComplex([p4]))
            Traceback (most recent call last):
            ...
            ValueError: the given cells are not face-to-face
        """
    def join(self, right):
        """
        The join of this polyhedral complex with another one.

        INPUT:

        - ``right`` -- the other polyhedral complex (the right-hand factor)

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc_join = pc.join(pc)
            sage: pc_join
            Polyhedral complex with 1 maximal cell
            sage: next(pc_join.maximal_cell_iterator()).vertices()
            (A vertex at (0, 0, 0),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
        """
    def wedge(self, right) -> None:
        """
        The wedge (one-point union) of ``self`` with ``right``.

        .. TODO::

            Implement the wedge product of two polyhedral complexes.

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc.wedge(pc)
            Traceback (most recent call last):
            ...
            NotImplementedError: wedge is not implemented for polyhedral complex
        """
    def chain_complex(self, subcomplex=None, augmented: bool = False, verbose: bool = False, check: bool = True, dimensions=None, base_ring=..., cochain: bool = False) -> None:
        """
        The chain complex associated to this polyhedral complex.

        .. TODO::

            Implement chain complexes of a polyhedral complex.

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc.chain_complex()
            Traceback (most recent call last):
            ...
            NotImplementedError: chain_complex is not implemented for polyhedral complex
        """
    def alexander_whitney(self, cell, dim_left) -> None:
        """
        The decomposition of ``cell`` in this complex into left and right
        factors, suitable for computing cup products.

        .. TODO::

            Implement :meth:`alexander_whitney` of a polyhedral complex.

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc.alexander_whitney(None, 1)
            Traceback (most recent call last):
            ...
            NotImplementedError: alexander_whitney is not implemented for polyhedral complex
        """
    def set_immutable(self) -> None:
        """
        Make this polyhedral complex immutable.

        EXAMPLES::

            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc.is_mutable()
            True
            sage: pc.set_immutable()
            sage: pc.is_mutable()
            False
        """
    def is_mutable(self) -> bool:
        """
        Return whether ``self`` is mutable.

        EXAMPLES::

            sage: pc1 = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc1.is_mutable()
            True
            sage: pc2 = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])],
            ....:                        is_mutable=False)
            sage: pc2.is_mutable()
            False
            sage: pc1 == pc2
            True
            sage: pc3 = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])],
            ....:                        is_immutable=True)
            sage: pc3.is_mutable()
            False
            sage: pc2 == pc3
            True
        """
    def is_immutable(self) -> bool:
        """
        Return whether ``self`` is immutable.

        EXAMPLES::

            sage: pc1 = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])])
            sage: pc1.is_immutable()
            False
            sage: pc2 = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])],
            ....:                        is_mutable=False)
            sage: pc2.is_immutable()
            True
            sage: pc3 = PolyhedralComplex([Polyhedron(vertices=[[0], [1]])],
            ....:                        is_immutable=True)
            sage: pc3.is_immutable()
            True
        """
    def add_cell(self, cell) -> None:
        """
        Add a cell to this polyhedral complex.

        INPUT:

        - ``cell`` -- a polyhedron

        This **changes** the polyhedral complex, by adding a new cell and all
        of its subfaces.

        EXAMPLES:

        Set up an empty complex in the intended ambient space, then add a cell::

            sage: pc = PolyhedralComplex(ambient_dim=2)
            sage: pc.add_cell(Polyhedron(vertices=[(1, 2), (0, 2)]))
            sage: pc
            Polyhedral complex with 1 maximal cell

        If you add a cell which is already present, there is no effect::

            sage: pc.add_cell(Polyhedron(vertices=[(1, 2)]))
            sage: pc
            Polyhedral complex with 1 maximal cell
            sage: pc.dimension()
            1

        Add a cell and check that dimension is correctly updated::

            sage: pc.add_cell(Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)]))
            sage: pc.dimension()
            2
            sage: pc.maximal_cells()
            {2: {A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices}}
            sage: pc.is_convex()
            True

        Add another cell and check that the properties are correctly updated::

            sage: pc.add_cell(Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)]))
            sage: pc
            Polyhedral complex with 2 maximal cells
            sage: len(pc._cells[1])
            5
            sage: pc._face_poset
            Finite poset containing 11 elements
            sage: pc._is_convex
            True
            sage: pc._polyhedron.vertices_list()
            [[0, 0], [0, 2], [1, 1], [1, 2]]

        Add a ray which makes the complex non convex::

            sage: pc.add_cell(Polyhedron(rays=[(1, 0)]))
            sage: pc
            Polyhedral complex with 3 maximal cells
            sage: len(pc._cells[1])
            6
            sage: (pc._is_convex is False) and (pc._polyhedron is None)
            True

        TESTS::

            sage: pc.add_cell(Polyhedron(vertices=[[0]]))
            Traceback (most recent call last):
            ...
            ValueError: the given cell is not a polyhedron in the same ambient space
            sage: pc.add_cell(Polyhedron(vertices=[(1, 1), (0, 0), (2, 0)]))
            Traceback (most recent call last):
            ...
            ValueError: the cell is not face-to-face with complex
            sage: pc.set_immutable()
            sage: pc.add_cell(Polyhedron(vertices=[(-1, -1)]))
            Traceback (most recent call last):
            ...
            ValueError: this polyhedral complex is not mutable
        """
    def remove_cell(self, cell, check: bool = False) -> None:
        """
        Remove ``cell`` from ``self`` and all the cells that contain ``cell``
        as a subface.

        INPUT:

        - ``cell`` -- a cell of the polyhedral complex

        - ``check`` -- boolean (default: ``False``); if ``True``,
          raise an error if ``cell`` is not a cell of this complex

        This does not return anything; instead, it **changes** the
        polyhedral complex.

        EXAMPLES:

        If you add a cell which is already present, there is no effect::

            sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
            sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
            sage: r = Polyhedron(rays=[(1, 0)])
            sage: pc = PolyhedralComplex([p1, p2, r])
            sage: pc.dimension()
            2
            sage: pc.remove_cell(Polyhedron(vertices=[(0, 0), (1, 2)]))
            sage: pc.dimension()
            1
            sage: pc
            Polyhedral complex with 5 maximal cells
            sage: pc.remove_cell(Polyhedron(vertices=[(1, 2)]))
            sage: pc.dimension()
            1
            sage: pc
            Polyhedral complex with 3 maximal cells
            sage: pc.remove_cell(Polyhedron(vertices=[(0, 0)]))
            sage: pc.dimension()
            0

        TESTS:

        Check that :exc:`ValueError` and empty complex are treated properly::

            sage: p = Polyhedron(vertices=[[1]])
            sage: pc = PolyhedralComplex([p])
            sage: pc.remove_cell(Polyhedron(vertices=[[0]]), check=True)
            Traceback (most recent call last):
            ...
            ValueError: trying to remove a cell which is not in the polyhedral complex
            sage: pc.remove_cell(Polyhedron(vertices=[(1, 1)]))
            Traceback (most recent call last):
            ...
            ValueError: the given cell is not a polyhedron in the same ambient space
            sage: pc.remove_cell(p)
            sage: pc.dimension()
            -1
            sage: pc = PolyhedralComplex([Polyhedron(vertices=[[0]])], is_mutable=False)
            sage: pc.remove_cell(Polyhedron(vertices=[[0]]))
            Traceback (most recent call last):
            ...
            ValueError: this polyhedral complex is not mutable

        Check that this function is coherent with
        :meth:`~sage.topology.simplicial_complex.SimplicialComplex.remove_face`::

            sage: v1 = (1, 0, 0, 0); v2 = (0, 1, 0, 0); v3 = (0, 0, 1, 0); v4 = (0, 0, 0, 1)
            sage: Z = PolyhedralComplex([Polyhedron(vertices=[v1, v2, v3, v4])]); Z
            Polyhedral complex with 1 maximal cell
            sage: Z.remove_cell(Polyhedron(vertices=[v1, v2]))
            sage: Z
            Polyhedral complex with 2 maximal cells
            sage: [c.vertices_list() for c in Z.maximal_cells_sorted()]
            [[[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]],
             [[0, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0]]]

            sage: v0 = (0, 0, 0, 0)
            sage: S = PolyhedralComplex([Polyhedron(vertices=[v0, v1, v2]), Polyhedron(vertices=[v2, v3])])
            sage: S.maximal_cells()
            {1: {A 1-dimensional polyhedron in ZZ^4 defined as the convex hull of 2 vertices},
             2: {A 2-dimensional polyhedron in ZZ^4 defined as the convex hull of 3 vertices}}
            sage: S.remove_cell(Polyhedron(vertices=[v0, v1, v2]))
            sage: S
            Polyhedral complex with 4 maximal cells
            sage: [c.vertices_list() for c in S.maximal_cells_sorted()]
            [[[0, 0, 0, 0], [0, 1, 0, 0]],
             [[0, 0, 0, 0], [1, 0, 0, 0]],
             [[0, 0, 1, 0], [0, 1, 0, 0]],
             [[0, 1, 0, 0], [1, 0, 0, 0]]]

            sage: T = PolyhedralComplex([Polyhedron(vertices=[[1], [2]]), Polyhedron(vertices=[[1], [-3]])])
            sage: T.remove_cell(Polyhedron(vertices=[[-3], [1]]))
            sage: [c.vertices_list() for c in T.maximal_cells_sorted()]
            [[[1], [2]], [[-3]]]
            sage: [c.vertices_list() for c in T.cells_sorted()]
            [[[1], [2]], [[-3]], [[1]], [[2]]]
        """
    def is_simplicial_complex(self) -> bool:
        """
        Test if this polyhedral complex is a simplicial complex.

        A polyhedral complex is **simplicial** if all of its (maximal) cells
        are simplices, i.e., every cell is a bounded polytope with `d+1`
        vertices, where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(0, 0), (1, 1), (1, 2)])
            sage: p2 = Polyhedron(rays=[(1, 0)])
            sage: PolyhedralComplex([p1]).is_simplicial_complex()
            True
            sage: PolyhedralComplex([p2]).is_simplicial_complex()
            False
        """
    def is_polyhedral_fan(self) -> bool:
        """
        Test if this polyhedral complex is a polyhedral fan.

        A polyhedral complex is a **fan** if all of its (maximal) cells
        are cones.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(0, 0), (1, 1), (1, 2)])
            sage: p2 = Polyhedron(rays=[(1, 0)])
            sage: PolyhedralComplex([p1]).is_polyhedral_fan()
            False
            sage: PolyhedralComplex([p2]).is_polyhedral_fan()
            True
            sage: halfplane = Polyhedron(rays=[(1, 0), (-1, 0), (0, 1)])
            sage: PolyhedralComplex([halfplane]).is_polyhedral_fan()
            True
        """
    def is_simplicial_fan(self) -> bool:
        """
        Test if this polyhedral complex is a simplicial fan.

        A polyhedral complex is a **simplicial fan** if all of its (maximal)
        cells are simplicial cones, i.e., every cell is a pointed cone (with
        vertex being the origin) generated by `d` linearly independent rays,
        where `d` is the dimension of the cone.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[(0, 0), (1, 1), (1, 2)])
            sage: p2 = Polyhedron(rays=[(1, 0)])
            sage: PolyhedralComplex([p1]).is_simplicial_fan()
            False
            sage: PolyhedralComplex([p2]).is_simplicial_fan()
            True
            sage: halfplane = Polyhedron(rays=[(1, 0), (-1, 0), (0, 1)])
            sage: PolyhedralComplex([halfplane]).is_simplicial_fan()
            False
        """
    def subdivide(self, make_simplicial: bool = False, new_vertices=None, new_rays=None):
        """
        Construct a new polyhedral complex by iterative stellar subdivision of
        ``self`` for each new vertex/ray given.

        Currently, subdivision is only supported for bounded polyhedral complex
        or polyhedral fan.

        INPUT:

        - ``make_simplicial`` -- boolean (default: ``False``); if ``True``,
          the returned polyhedral complex is simplicial

        - ``new_vertices``, ``new_rays`` -- list (optional); new generators
          to be added during subdivision

        EXAMPLES::

            sage: square_vertices = [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]
            sage: pc = PolyhedralComplex([
            ....:         Polyhedron(vertices=[(0, 0, 0)] + square_vertices),
            ....:         Polyhedron(vertices=[(0, 0, 2)] + square_vertices)])
            sage: pc.is_compact() and not pc.is_simplicial_complex()
            True
            sage: subdivided_pc = pc.subdivide(new_vertices=[(0, 0, 1)])
            sage: subdivided_pc
            Polyhedral complex with 8 maximal cells
            sage: subdivided_pc.is_simplicial_complex()
            True
            sage: simplicial_pc = pc.subdivide(make_simplicial=True)
            sage: simplicial_pc
            Polyhedral complex with 4 maximal cells
            sage: simplicial_pc.is_simplicial_complex()
            True

            sage: fan = PolyhedralComplex([Polyhedron(rays=square_vertices)])
            sage: fan.is_polyhedral_fan() and not fan.is_simplicial_fan()
            True
            sage: fan.subdivide(new_vertices=[(0, 0, 1)])
            Traceback (most recent call last):
            ...
            ValueError: new vertices cannot be used for subdivision
            sage: subdivided_fan = fan.subdivide(new_rays=[(0, 0, 1)])
            sage: subdivided_fan
            Polyhedral complex with 4 maximal cells
            sage: subdivided_fan.is_simplicial_fan()
            True
            sage: simplicial_fan = fan.subdivide(make_simplicial=True)
            sage: simplicial_fan
            Polyhedral complex with 2 maximal cells
            sage: simplicial_fan.is_simplicial_fan()
            True

            sage: halfspace = PolyhedralComplex([Polyhedron(rays=[(0, 0, 1)],
            ....:             lines=[(1, 0, 0), (0, 1, 0)])])
            sage: halfspace.is_simplicial_fan()
            False
            sage: subdiv_halfspace = halfspace.subdivide(make_simplicial=True)
            sage: subdiv_halfspace
            Polyhedral complex with 4 maximal cells
            sage: subdiv_halfspace.is_simplicial_fan()
            True
        """

def cells_list_to_cells_dict(cells_list) -> dict:
    """
    Helper function that returns the dictionary whose keys are the dimensions,
    and the value associated to an integer `d` is the set of `d`-dimensional
    polyhedra in the given list.

    EXAMPLES::

        sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
        sage: p2 = Polyhedron(vertices=[(1, 1), (0, 0)])
        sage: p3 = Polyhedron(vertices=[(0, 0)])
        sage: p4 = Polyhedron(vertices=[(1, 1)])
        sage: sage.geometry.polyhedral_complex.cells_list_to_cells_dict([p1, p2, p3, p4])
        {0: {A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex,
          A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex},
         1: {A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices},
         2: {A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices}}
    """
def exploded_plot(polyhedra, *, center=None, explosion_factor: int = 1, sticky_vertices: bool = False, sticky_center: bool = True, point=None, **kwds):
    """
    Return a plot of several ``polyhedra`` in one figure with extra space
    between them.

    INPUT:

    - ``polyhedra`` -- an iterable of
      :class:`~sage.geometry.polyhedron.base.Polyhedron_base` objects

    - ``center`` -- (default: ``None``, denoting the origin) the center of
      explosion

    - ``explosion_factor`` -- (default: 1) a nonnegative number; translate
      polyhedra by this factor of the distance from ``center`` to their center

    - ``sticky_vertices`` -- (default: ``False``) boolean or dict; whether to
      draw line segments between shared vertices of the given polyhedra. A dict
      gives options for :func:`sage.plot.line`.

    - ``sticky_center`` -- (default: ``True``) boolean or dict. When ``center``
      is a vertex of some of the polyhedra, whether to draw line segments
      connecting the ``center`` to the shifted copies of these vertices. A dict
      gives options for :func:`sage.plot.line`.

    - ``color`` -- (default: ``None``) if ``'rainbow'``, assign a different
      color to every maximal cell and every vertex; otherwise, passed on to
      :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.plot`

    - other keyword arguments are passed on to
      :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.plot`

    EXAMPLES::

        sage: from sage.geometry.polyhedral_complex import exploded_plot
        sage: p1 = Polyhedron(vertices=[(1, 1), (0, 0), (1, 2)])
        sage: p2 = Polyhedron(vertices=[(1, 2), (0, 0), (0, 2)])
        sage: p3 = Polyhedron(vertices=[(0, 0), (1, 1), (2, 0)])
        sage: exploded_plot([p1, p2, p3])                                               # needs sage.plot
        Graphics object consisting of 20 graphics primitives
        sage: exploded_plot([p1, p2, p3], center=(1, 1))                                # needs sage.plot
        Graphics object consisting of 19 graphics primitives
        sage: exploded_plot([p1, p2, p3], center=(1, 1), sticky_vertices=True)          # needs sage.plot
        Graphics object consisting of 23 graphics primitives
    """
