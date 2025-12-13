import sage.geometry.abc
from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import Element as Element

class Polyhedron_base0(Element, sage.geometry.abc.Polyhedron):
    """
    Initialization and basic access for polyhedra.

    See :class:`sage.geometry.polyhedron.base.Polyhedron_base`.

    TESTS::

        sage: from sage.geometry.polyhedron.base0 import Polyhedron_base0
        sage: P = Polyhedron(rays=[[1, 0, 0]], lines=[[0, 1, 0]])
        sage: Polyhedron_base0.Vrepresentation(P)
        (A line in the direction (0, 1, 0),
        A vertex at (0, 0, 0),
        A ray in the direction (1, 0, 0))
        sage: Polyhedron_base0.vertices.f(P)
        (A vertex at (0, 0, 0),)
        sage: Polyhedron_base0.rays.f(P)
        (A ray in the direction (1, 0, 0),)
        sage: Polyhedron_base0.lines.f(P)
        (A line in the direction (0, 1, 0),)
        sage: Polyhedron_base0.Hrepresentation(P)
        (An equation (0, 0, 1) x + 0 == 0, An inequality (1, 0, 0) x + 0 >= 0)
        sage: Polyhedron_base0.inequalities.f(P)
        (An inequality (1, 0, 0) x + 0 >= 0,)
        sage: Polyhedron_base0.equations.f(P)
        (An equation (0, 0, 1) x + 0 == 0,)
        sage: Polyhedron_base0.base_ring(P)
        Integer Ring
        sage: Polyhedron_base0.backend(P)
        'ppl'
        sage: Polyhedron_base0.change_ring(P, ZZ, backend='field').backend()
        'field'
        sage: Polyhedron_base0.base_extend(P, QQ)
        A 2-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex, 1 ray, 1 line
    """
    def __init__(self, parent, Vrep, Hrep, Vrep_minimal=None, Hrep_minimal=None, pref_rep=None, mutable: bool = False, **kwds) -> None:
        """
        Initialize the polyhedron.

        See :class:`sage.geometry.polyhedron.base.Polyhedron_base` for a description of the input
        data.

        TESTS::

            sage: p = Polyhedron()    # indirect doctests

            sage: from sage.geometry.polyhedron.backend_field import Polyhedron_field
            sage: from sage.geometry.polyhedron.parent import Polyhedra_field
            sage: parent = Polyhedra_field(AA, 1, 'field')                              # needs sage.rings.number_field
            sage: Vrep = [[[0], [1/2], [1]], [], []]
            sage: Hrep = [[[0, 1], [1, -1]], []]
            sage: p = Polyhedron_field(parent, Vrep, Hrep,                              # needs sage.rings.number_field
            ....:                      Vrep_minimal=False, Hrep_minimal=True)
            Traceback (most recent call last):
            ...
            ValueError: if both Vrep and Hrep are provided, they must be minimal...

        Illustration of ``pref_rep``.
        Note that ``ppl`` doesn't support precomputed data::

            sage: from sage.geometry.polyhedron.backend_ppl import Polyhedron_QQ_ppl
            sage: from sage.geometry.polyhedron.parent import Polyhedra_QQ_ppl
            sage: parent = Polyhedra_QQ_ppl(QQ, 1, 'ppl')
            sage: p = Polyhedron_QQ_ppl(parent, Vrep, 'nonsense',
            ....:                       Vrep_minimal=True, Hrep_minimal=True, pref_rep='Vrep')
            sage: p = Polyhedron_QQ_ppl(parent, 'nonsense', Hrep,
            ....:                       Vrep_minimal=True, Hrep_minimal=True, pref_rep='Hrep')
            sage: p = Polyhedron_QQ_ppl(parent, 'nonsense', Hrep,
            ....:                       Vrep_minimal=True, Hrep_minimal=True, pref_rep='Vrepresentation')
            Traceback (most recent call last):
            ...
            ValueError: ``pref_rep`` must be one of ``(None, 'Vrep', 'Hrep')``

        If the backend supports precomputed data, ``pref_rep`` is ignored::

            sage: p = Polyhedron_field(parent, Vrep, 'nonsense',
            ....:                      Vrep_minimal=True, Hrep_minimal=True, pref_rep='Vrep')
            Traceback (most recent call last):
            ...
            TypeError: ..._init_Hrepresentation() takes 3 positional arguments but 9 were given

        The empty polyhedron is detected when the Vrepresentation is given with generator;
        see :issue:`29899`::

            sage: from sage.geometry.polyhedron.backend_cdd import Polyhedron_QQ_cdd
            sage: from sage.geometry.polyhedron.parent import Polyhedra_QQ_cdd
            sage: parent = Polyhedra_QQ_cdd(QQ, 0, 'cdd')
            sage: p = Polyhedron_QQ_cdd(parent, [iter([]), iter([]), iter([])], None)
        """
    def base_extend(self, base_ring, backend=None):
        """
        Return a new polyhedron over a larger base ring.

        This method can also be used to change the backend.

        INPUT:

        - ``base_ring`` -- the new base ring

        - ``backend`` -- the new backend, see
          :func:`~sage.geometry.polyhedron.constructor.Polyhedron`
          If ``None`` (the default), attempt to keep the same backend.
          Otherwise, use the same defaulting behavior
          as described there.

        OUTPUT: the same polyhedron, but over a larger base ring and possibly with a changed backend

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(1,0), (0,1)], rays=[(1,1)], base_ring=ZZ);  P
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices and 1 ray
            sage: P.base_extend(QQ)
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 2 vertices and 1 ray
            sage: P.base_extend(QQ) == P
            True

        TESTS:

        Test that :issue:`22575` is fixed::

            sage: Q = P.base_extend(ZZ, backend='field')
            sage: Q.backend()
            'field'
        """
    def change_ring(self, base_ring, backend=None):
        """
        Return the polyhedron obtained by coercing the entries of the
        vertices/lines/rays of this polyhedron into the given ring.

        This method can also be used to change the backend.

        INPUT:

        - ``base_ring`` -- the new base ring

        - ``backend`` -- the new backend or ``None`` (default), see
          :func:`~sage.geometry.polyhedron.constructor.Polyhedron`.
          If ``None`` (the default), attempt to keep the same backend.
          Otherwise, use the same defaulting behavior
          as described there.

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(1,0), (0,1)], rays=[(1,1)], base_ring=QQ); P
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 2 vertices and 1 ray
            sage: P.change_ring(ZZ)
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices and 1 ray
            sage: P.change_ring(ZZ) == P
            True

            sage: P = Polyhedron(vertices=[(-1.3,0), (0,2.3)], base_ring=RDF); P.vertices()
            (A vertex at (-1.3, 0.0), A vertex at (0.0, 2.3))
            sage: P.change_ring(QQ).vertices()
            (A vertex at (-13/10, 0), A vertex at (0, 23/10))
            sage: P == P.change_ring(QQ)
            True
            sage: P.change_ring(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: cannot change the base ring to the Integer Ring

            sage: P = polytopes.regular_polygon(3); P                                   # needs sage.rings.number_field
            A 2-dimensional polyhedron in AA^2 defined as the convex hull of 3 vertices
            sage: P.vertices()                                                          # needs sage.rings.number_field
            (A vertex at (0.?e-16, 1.000000000000000?),
             A vertex at (0.866025403784439?, -0.500000000000000?),
             A vertex at (-0.866025403784439?, -0.500000000000000?))
            sage: P.change_ring(QQ)                                                     # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: cannot change the base ring to the Rational Field

        .. WARNING::

            The base ring ``RDF`` should be used with care. As it is
            not an exact ring, certain computations may break or
            silently produce wrong results, for example changing the
            base ring from an exact ring into ``RDF`` may cause a
            loss of data::

                sage: P = Polyhedron([[2/3,0],[6666666666666667/10^16,0]], base_ring=AA); P         # needs sage.rings.number_field
                A 1-dimensional polyhedron in AA^2 defined as the convex hull of 2 vertices
                sage: Q = P.change_ring(RDF); Q                                         # needs sage.rings.number_field
                A 0-dimensional polyhedron in RDF^2 defined as the convex hull of 1 vertex
                sage: P.n_vertices() == Q.n_vertices()                                  # needs sage.rings.number_field
                False
        """
    def is_mutable(self):
        """
        Return ``True`` if the polyhedron is mutable, i.e. it can be modified in place.

        EXAMPLES::

            sage: p = polytopes.cube(backend='field')
            sage: p.is_mutable()
            False
        """
    def is_immutable(self):
        """
        Return ``True`` if the polyhedron is immutable, i.e. it cannot be modified in place.

        EXAMPLES::

            sage: p = polytopes.cube(backend='field')
            sage: p.is_immutable()
            True
        """
    @cached_method
    def n_equations(self):
        """
        Return the number of equations. The representation will
        always be minimal, so the number of equations is the
        codimension of the polyhedron in the ambient space.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[1,0,0],[0,1,0],[0,0,1]])
            sage: p.n_equations()
            1
        """
    @cached_method
    def n_inequalities(self):
        """
        Return the number of inequalities. The representation will
        always be minimal, so the number of inequalities is the
        number of facets of the polyhedron in the ambient space.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[1,0,0],[0,1,0],[0,0,1]])
            sage: p.n_inequalities()
            3

            sage: p = Polyhedron(vertices = [[t,t^2,t^3] for t in range(6)])
            sage: p.n_facets()
            8
        """
    n_facets = n_inequalities
    @cached_method
    def n_vertices(self):
        """
        Return the number of vertices. The representation will
        always be minimal.

        .. WARNING::

            If the polyhedron has lines, return the number of vertices in
            the ``Vrepresentation``. As the represented polyhedron has
            no 0-dimensional faces (i.e. vertices), ``n_vertices`` corresponds
            to the number of `k`-faces, where `k` is the number of lines::

                sage: P = Polyhedron(rays=[[1,0,0]],lines=[[0,1,0]])
                sage: P.n_vertices()
                1
                sage: P.faces(0)
                ()
                sage: P.f_vector()
                (1, 0, 1, 1)

                sage: P = Polyhedron(rays=[[1,0,0]],lines=[[0,1,0],[0,1,1]])
                sage: P.n_vertices()
                1
                sage: P.f_vector()
                (1, 0, 0, 1, 1)

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[1,0],[0,1],[1,1]], rays=[[1,1]])
            sage: p.n_vertices()
            2
        """
    @cached_method
    def n_rays(self):
        """
        Return the number of rays. The representation will
        always be minimal.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[1,0],[0,1]], rays=[[1,1]])
            sage: p.n_rays()
            1
        """
    @cached_method
    def n_lines(self):
        """
        Return the number of lines. The representation will
        always be minimal.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0]], rays=[[0,1],[0,-1]])
            sage: p.n_lines()
            1
        """
    def is_compact(self):
        """
        Test for boundedness of the polytope.

        EXAMPLES::

            sage: p = polytopes.icosahedron()                                           # needs sage.groups sage.rings.number_field
            sage: p.is_compact()                                                        # needs sage.groups sage.rings.number_field
            True
            sage: p = Polyhedron(ieqs=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,-1,0,0]])
            sage: p.is_compact()
            False
        """
    def Hrepresentation(self, index=None):
        """
        Return the objects of the H-representation. Each entry is
        either an inequality or a equation.

        INPUT:

        - ``index`` -- either an integer or ``None``

        OUTPUT:

        The optional argument is an index running from ``0`` to
        ``self.n_Hrepresentation()-1``. If present, the
        H-representation object at the given index will be
        returned. Without an argument, returns the list of all
        H-representation objects.

        EXAMPLES::

            sage: p = polytopes.hypercube(3, backend='field')
            sage: p.Hrepresentation(0)
            An inequality (-1, 0, 0) x + 1 >= 0
            sage: p.Hrepresentation(0) == p.Hrepresentation()[0]
            True
        """
    def Hrepresentation_str(self, separator: str = '\n', latex: bool = False, style: str = '>=', align=None, **kwds):
        """
        Return a human-readable string representation of the Hrepresentation of this
        polyhedron.

        INPUT:

        - ``separator`` -- string (default: ``'\\n'``)

        - ``latex`` -- boolean (default: ``False``)

        - ``style`` -- either ``'positive'`` (making all coefficients positive)
                       or ``'<='``, or ``'>='``; default is ``'>='``

        - ``align`` -- boolean or ``None''; default is ``None`` in which case
                       ``align`` is ``True`` if ``separator`` is the newline character.
                       If set, then the lines of the output string are aligned
                       by the comparison symbol by padding blanks.

        Keyword parameters of
        :meth:`~sage.geometry.polyhedron.representation.Hrepresentation.repr_pretty`
        are passed on:

        - ``prefix`` -- string

        - ``indices`` -- tuple or other iterable

        OUTPUT: string

        EXAMPLES::

            sage: P = polytopes.permutahedron(3)
            sage: print(P.Hrepresentation_str())
            x0 + x1 + x2 ==  6
                 x0 + x1 >=  3
                -x0 - x1 >= -5
                      x1 >=  1
                     -x0 >= -3
                      x0 >=  1
                     -x1 >= -3

            sage: print(P.Hrepresentation_str(style='<='))
            -x0 - x1 - x2 == -6
                 -x0 - x1 <= -3
                  x0 + x1 <=  5
                      -x1 <= -1
                       x0 <=  3
                      -x0 <= -1
                       x1 <=  3

            sage: print(P.Hrepresentation_str(style='positive'))
            x0 + x1 + x2 == 6
                 x0 + x1 >= 3
                       5 >= x0 + x1
                      x1 >= 1
                       3 >= x0
                      x0 >= 1
                       3 >= x1

            sage: print(P.Hrepresentation_str(latex=True))
            \\begin{array}{rcl}
            x_{0} + x_{1} + x_{2} & =    &  6 \\\\\n                    x_{0} + x_{1} & \\geq &  3 \\\\\n                   -x_{0} - x_{1} & \\geq & -5 \\\\\n                            x_{1} & \\geq &  1 \\\\\n                           -x_{0} & \\geq & -3 \\\\\n                            x_{0} & \\geq &  1 \\\\\n                           -x_{1} & \\geq & -3
            \\end{array}

            sage: print(P.Hrepresentation_str(align=False))
            x0 + x1 + x2 == 6
            x0 + x1 >= 3
            -x0 - x1 >= -5
            x1 >= 1
            -x0 >= -3
            x0 >= 1
            -x1 >= -3

            sage: c = polytopes.cube()
            sage: c.Hrepresentation_str(separator=', ', style='positive')
            '1 >= x0, 1 >= x1, 1 >= x2, 1 + x0 >= 0, 1 + x2 >= 0, 1 + x1 >= 0'
        """
    def Hrep_generator(self) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over the objects of the H-representation
        (inequalities or equations).

        EXAMPLES::

            sage: p = polytopes.hypercube(3)
            sage: next(p.Hrep_generator())
            An inequality (-1, 0, 0) x + 1 >= 0
        """
    @cached_method
    def n_Hrepresentation(self):
        """
        Return the number of objects that make up the
        H-representation of the polyhedron.

        OUTPUT: integer

        EXAMPLES::

            sage: p = polytopes.cross_polytope(4)
            sage: p.n_Hrepresentation()
            16
            sage: p.n_Hrepresentation() == p.n_inequalities() + p.n_equations()
            True
        """
    def Vrepresentation(self, index=None):
        """
        Return the objects of the V-representation. Each entry is
        either a vertex, a ray, or a line.

        See :mod:`sage.geometry.polyhedron.constructor` for a
        definition of vertex/ray/line.

        INPUT:

        - ``index`` -- either an integer or ``None``

        OUTPUT:

        The optional argument is an index running from ``0`` to
        ``self.n_Vrepresentation()-1``. If present, the
        V-representation object at the given index will be
        returned. Without an argument, returns the list of all
        V-representation objects.

        EXAMPLES::

            sage: p = polytopes.simplex(4, project=True)
            sage: p.Vrepresentation(0)
            A vertex at (0.7071067812, 0.4082482905, 0.2886751346, 0.2236067977)
            sage: p.Vrepresentation(0) == p.Vrepresentation() [0]
            True
        """
    @cached_method
    def n_Vrepresentation(self):
        """
        Return the number of objects that make up the
        V-representation of the polyhedron.

        OUTPUT: integer

        EXAMPLES::

            sage: p = polytopes.simplex(4)
            sage: p.n_Vrepresentation()
            5
            sage: p.n_Vrepresentation() == p.n_vertices() + p.n_rays() + p.n_lines()
            True
        """
    def Vrep_generator(self) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over the objects of the V-representation
        (vertices, rays, and lines).

        EXAMPLES::

            sage: p = polytopes.cyclic_polytope(3,4)
            sage: vg = p.Vrep_generator()
            sage: next(vg)
            A vertex at (0, 0, 0)
            sage: next(vg)
            A vertex at (1, 1, 1)
        """
    def inequality_generator(self) -> Generator[Incomplete]:
        """
        Return  a generator for the defining inequalities of the
        polyhedron.

        OUTPUT: a generator of the inequality Hrepresentation objects

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[1,1]])
            sage: for v in triangle.inequality_generator(): print(v)
            An inequality (1, 1) x - 1 >= 0
            An inequality (0, -1) x + 1 >= 0
            An inequality (-1, 0) x + 1 >= 0
            sage: [ v for v in triangle.inequality_generator() ]
            [An inequality (1, 1) x - 1 >= 0,
             An inequality (0, -1) x + 1 >= 0,
             An inequality (-1, 0) x + 1 >= 0]
            sage: [ [v.A(), v.b()] for v in triangle.inequality_generator() ]
            [[(1, 1), -1], [(0, -1), 1], [(-1, 0), 1]]
        """
    @cached_method
    def inequalities(self):
        """
        Return all inequalities.

        OUTPUT: a tuple of inequalities

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[2,2,2]])
            sage: p.inequalities()[0:3]
            (An inequality (1, 0, 0) x + 0 >= 0,
             An inequality (0, 1, 0) x + 0 >= 0,
             An inequality (0, 0, 1) x + 0 >= 0)

            sage: # needs sage.combinat
            sage: p3 = Polyhedron(vertices=Permutations([1, 2, 3, 4]))
            sage: ieqs = p3.inequalities()
            sage: ieqs[0]
            An inequality (0, 1, 1, 1) x - 6 >= 0
            sage: list(_)
            [-6, 0, 1, 1, 1]
        """
    def inequalities_list(self):
        """
        Return a list of inequalities as coefficient lists.

        .. NOTE::

            It is recommended to use :meth:`inequalities` or
            :meth:`inequality_generator` instead to iterate over the
            list of :class:`~sage.geometry.polyhedron.representation.Inequality` objects.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[2,2,2]])
            sage: p.inequalities_list()[0:3]
            [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

            sage: # needs sage.combinat
            sage: p3 = Polyhedron(vertices=Permutations([1, 2, 3, 4]))
            sage: ieqs = p3.inequalities_list()
            sage: ieqs[0]
            [-6, 0, 1, 1, 1]
            sage: ieqs[-1]
            [-3, 0, 1, 0, 1]
            sage: ieqs == [list(x) for x in p3.inequality_generator()]
            True
        """
    def equation_generator(self) -> Generator[Incomplete]:
        """
        Return a generator for the linear equations satisfied by the
        polyhedron.

        EXAMPLES::

            sage: p = polytopes.regular_polygon(8,base_ring=RDF)
            sage: p3 = Polyhedron(vertices = [x+[0] for x in p.vertices()], base_ring=RDF)
            sage: next(p3.equation_generator())
            An equation (0.0, 0.0, 1.0) x + 0.0 == 0
        """
    @cached_method
    def equations(self):
        """
        Return all linear constraints of the polyhedron.

        OUTPUT: a tuple of equations

        EXAMPLES::

            sage: test_p = Polyhedron(vertices = [[1,2,3,4],[2,1,3,4],[4,3,2,1],[3,4,1,2]])
            sage: test_p.equations()
            (An equation (1, 1, 1, 1) x - 10 == 0,)
        """
    def equations_list(self):
        """
        Return the linear constraints of the polyhedron. As with
        inequalities, each constraint is given as [b -a1 -a2 ... an]
        where for variables x1, x2,..., xn, the polyhedron satisfies
        the equation b = a1*x1 + a2*x2 + ... + an*xn.

        .. NOTE::

            It is recommended to use :meth:`equations` or
            :meth:`equation_generator()` instead to iterate over the
            list of
            :class:`~sage.geometry.polyhedron.representation.Equation`
            objects.

        EXAMPLES::

            sage: test_p = Polyhedron(vertices = [[1,2,3,4],[2,1,3,4],[4,3,2,1],[3,4,1,2]])
            sage: test_p.equations_list()
            [[-10, 1, 1, 1, 1]]
        """
    def vertices_list(self):
        """
        Return a list of vertices of the polyhedron.

        .. NOTE::

            It is recommended to use :meth:`vertex_generator` instead to
            iterate over the list of :class:`~sage.geometry.polyhedron.representation.Vertex` objects.

        .. WARNING::

            If the polyhedron has lines, return the vertices
            of the ``Vrepresentation``. However, the represented polyhedron
            has no 0-dimensional faces (i.e. vertices)::

                sage: P = Polyhedron(rays=[[1,0,0]],lines=[[0,1,0]])
                sage: P.vertices_list()
                [[0, 0, 0]]
                sage: P.faces(0)
                ()

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[1,1]])
            sage: triangle.vertices_list()
            [[0, 1], [1, 0], [1, 1]]
            sage: a_simplex = Polyhedron(ieqs = [
            ....:          [0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]
            ....:      ], eqns = [[1,-1,-1,-1,-1]])
            sage: a_simplex.vertices_list()
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
            sage: a_simplex.vertices_list() == [list(v) for v in a_simplex.vertex_generator()]
            True
        """
    def vertex_generator(self) -> Generator[Incomplete]:
        '''
        Return a generator for the vertices of the polyhedron.

        .. WARNING::

            If the polyhedron has lines, return a generator for the vertices
            of the ``Vrepresentation``. However, the represented polyhedron
            has no 0-dimensional faces (i.e. vertices)::

                sage: P = Polyhedron(rays=[[1,0,0]],lines=[[0,1,0]])
                sage: list(P.vertex_generator())
                [A vertex at (0, 0, 0)]
                sage: P.faces(0)
                ()

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[1,1]])
            sage: for v in triangle.vertex_generator(): print(v)
            A vertex at (0, 1)
            A vertex at (1, 0)
            A vertex at (1, 1)
            sage: v_gen = triangle.vertex_generator()
            sage: next(v_gen)   # the first vertex
            A vertex at (0, 1)
            sage: next(v_gen)   # the second vertex
            A vertex at (1, 0)
            sage: next(v_gen)   # the third vertex
            A vertex at (1, 1)
            sage: try: next(v_gen)   # there are only three vertices
            ....: except StopIteration: print("STOP")
            STOP
            sage: type(v_gen)
            <... \'generator\'>
            sage: [ v for v in triangle.vertex_generator() ]
            [A vertex at (0, 1), A vertex at (1, 0), A vertex at (1, 1)]
        '''
    @cached_method
    def vertices(self):
        """
        Return all vertices of the polyhedron.

        OUTPUT: a tuple of vertices

        .. WARNING::

            If the polyhedron has lines, return the vertices
            of the ``Vrepresentation``. However, the represented polyhedron
            has no 0-dimensional faces (i.e. vertices)::

                sage: P = Polyhedron(rays=[[1,0,0]],lines=[[0,1,0]])
                sage: P.vertices()
                (A vertex at (0, 0, 0),)
                sage: P.faces(0)
                ()

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[1,1]])
            sage: triangle.vertices()
            (A vertex at (0, 1), A vertex at (1, 0), A vertex at (1, 1))
            sage: a_simplex = Polyhedron(ieqs = [
            ....:          [0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]
            ....:      ], eqns = [[1,-1,-1,-1,-1]])
            sage: a_simplex.vertices()
            (A vertex at (1, 0, 0, 0), A vertex at (0, 1, 0, 0),
             A vertex at (0, 0, 1, 0), A vertex at (0, 0, 0, 1))
        """
    @cached_method
    def vertices_matrix(self, base_ring=None):
        """
        Return the coordinates of the vertices as the columns of a matrix.

        INPUT:

        - ``base_ring`` -- a ring or ``None`` (default); the base ring
          of the returned matrix. If not specified, the base ring of
          the polyhedron is used.

        OUTPUT:

        A matrix over ``base_ring`` whose columns are the coordinates
        of the vertices. A :exc:`TypeError` is raised if the coordinates
        cannot be converted to ``base_ring``.

        .. WARNING::

            If the polyhedron has lines, return the coordinates of the vertices
            of the ``Vrepresentation``. However, the represented polyhedron
            has no 0-dimensional faces (i.e. vertices)::

                sage: P = Polyhedron(rays=[[1,0,0]],lines=[[0,1,0]])
                sage: P.vertices_matrix()
                [0]
                [0]
                [0]
                sage: P.faces(0)
                ()

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[1,1]])
            sage: triangle.vertices_matrix()
            [0 1 1]
            [1 0 1]
            sage: (triangle/2).vertices_matrix()
            [  0 1/2 1/2]
            [1/2   0 1/2]
            sage: (triangle/2).vertices_matrix(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        TESTS:

        Check that :issue:`28828` is fixed::

                sage: P.vertices_matrix().is_immutable()
                True
        """
    def ray_generator(self) -> Generator[Incomplete]:
        """
        Return a generator for the rays of the polyhedron.

        EXAMPLES::

            sage: pi = Polyhedron(ieqs = [[1,1,0],[1,0,1]])
            sage: pir = pi.ray_generator()
            sage: [x.vector() for x in pir]
            [(1, 0), (0, 1)]
        """
    @cached_method
    def rays(self):
        """
        Return a list of rays of the polyhedron.

        OUTPUT: a tuple of rays

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,0,1],[0,0,1,0],[1,1,0,0]])
            sage: p.rays()
            (A ray in the direction (1, 0, 0),
             A ray in the direction (0, 1, 0),
             A ray in the direction (0, 0, 1))
        """
    def rays_list(self):
        """
        Return a list of rays as coefficient lists.

        .. NOTE::

            It is recommended to use :meth:`rays` or
            :meth:`ray_generator` instead to iterate over the list of
            :class:`~sage.geometry.polyhedron.representation.Ray` objects.

        OUTPUT: list of rays as lists of coordinates

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,0,1],[0,0,1,0],[1,1,0,0]])
            sage: p.rays_list()
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            sage: p.rays_list() == [list(r) for r in p.ray_generator()]
            True
        """
    def line_generator(self) -> Generator[Incomplete]:
        """
        Return a generator for the lines of the polyhedron.

        EXAMPLES::

            sage: pr = Polyhedron(rays = [[1,0],[-1,0],[0,1]], vertices = [[-1,-1]])
            sage: next(pr.line_generator()).vector()
            (1, 0)
        """
    @cached_method
    def lines(self):
        """
        Return all lines of the polyhedron.

        OUTPUT: a tuple of lines

        EXAMPLES::

            sage: p = Polyhedron(rays = [[1,0],[-1,0],[0,1],[1,1]], vertices = [[-2,-2],[2,3]])
            sage: p.lines()
            (A line in the direction (1, 0),)
        """
    def lines_list(self):
        """
        Return a list of lines of the polyhedron.  The line data is given
        as a list of coordinates rather than as a Hrepresentation object.

        .. NOTE::

            It is recommended to use :meth:`line_generator` instead to
            iterate over the list of :class:`~sage.geometry.polyhedron.representation.Line` objects.

        EXAMPLES::

            sage: p = Polyhedron(rays = [[1,0],[-1,0],[0,1],[1,1]], vertices = [[-2,-2],[2,3]])
            sage: p.lines_list()
            [[1, 0]]
            sage: p.lines_list() == [list(x) for x in p.line_generator()]
            True
        """
    def base_ring(self):
        """
        Return the base ring.

        OUTPUT:

        The ring over which the polyhedron is defined. Must be a
        sub-ring of the reals to define a polyhedron, in particular
        comparison must be defined. Popular choices are

        * ``ZZ`` (the ring of integers, lattice polytope),

        * ``QQ`` (exact arithmetic using gmp),

        * ``RDF`` (double precision floating-point arithmetic), or

        * ``AA`` (real algebraic field).

        EXAMPLES::

            sage: triangle = Polyhedron(vertices = [[1,0],[0,1],[1,1]])
            sage: triangle.base_ring() == ZZ
            True
        """
    def backend(self):
        """
        Return the backend used.

        OUTPUT:

        The name of the backend used for computations. It will be one of
        the following backends:

         * ``ppl`` the Parma Polyhedra Library

         * ``cdd`` CDD

         * ``normaliz`` normaliz

         * ``polymake`` polymake

         * ``field`` a generic Sage implementation

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1, 0], [0, 1], [1, 1]])
            sage: triangle.backend()
            'ppl'
            sage: D = polytopes.dodecahedron()                                          # needs sage.groups sage.rings.number_field
            sage: D.backend()                                                           # needs sage.groups sage.rings.number_field
            'field'
            sage: P = Polyhedron([[1.23]])
            sage: P.backend()
            'cdd'
        """
    def cdd_Hrepresentation(self):
        """
        Write the inequalities/equations data of the polyhedron in
        cdd's H-representation format.

        .. SEEALSO::

            :meth:`write_cdd_Hrepresentation` -- export the polyhedron as a
            H-representation to a file.

        OUTPUT: string

        EXAMPLES::

            sage: p = polytopes.hypercube(2)
            sage: print(p.cdd_Hrepresentation())
            H-representation
            begin
             4 3 rational
             1 -1 0
             1 0 -1
             1 1 0
             1 0 1
            end
            <BLANKLINE>

            sage: triangle = Polyhedron(vertices=[[1,0], [0,1], [1,1]], base_ring=AA)   # needs sage.rings.number_field
            sage: triangle.base_ring()                                                  # needs sage.rings.number_field
            Algebraic Real Field
            sage: triangle.cdd_Hrepresentation()                                        # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be ZZ, QQ, or RDF
        """
    def write_cdd_Hrepresentation(self, filename) -> None:
        """
        Export the polyhedron as a H-representation to a file.

        INPUT:

        - ``filename`` -- the output file

        .. SEEALSO::

            :meth:`cdd_Hrepresentation` -- return the H-representation of the
            polyhedron as a string.

        EXAMPLES::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(ext='.ext')
            sage: polytopes.cube().write_cdd_Hrepresentation(filename)
        """
    def cdd_Vrepresentation(self):
        """
        Write the vertices/rays/lines data of the polyhedron in cdd's
        V-representation format.

        .. SEEALSO::

            :meth:`write_cdd_Vrepresentation` -- export the polyhedron as a
            V-representation to a file.

        OUTPUT: string

        EXAMPLES::

            sage: q = Polyhedron(vertices = [[1,1],[0,0],[1,0],[0,1]])
            sage: print(q.cdd_Vrepresentation())
            V-representation
            begin
             4 3 rational
             1 0 0
             1 0 1
             1 1 0
             1 1 1
            end
        """
    def write_cdd_Vrepresentation(self, filename) -> None:
        """
        Export the polyhedron as a V-representation to a file.

        INPUT:

        - ``filename`` -- the output file

        .. SEEALSO::

            :meth:`cdd_Vrepresentation` -- return the V-representation of the
            polyhedron as a string.

        EXAMPLES::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(ext='.ext')
            sage: polytopes.cube().write_cdd_Vrepresentation(filename)
        """
