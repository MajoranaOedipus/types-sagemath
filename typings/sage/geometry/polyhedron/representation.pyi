from _typeshed import Incomplete
from collections.abc import Generator
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Vector as Vector
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

INEQUALITY: int
EQUATION: int
VERTEX: int
RAY: int
LINE: int

class PolyhedronRepresentation(SageObject):
    """
    The internal base class for all representation objects of
    ``Polyhedron`` (vertices/rays/lines and inequalities/equations)

    .. NOTE::

        You should not (and cannot) instantiate it yourself. You can
        only obtain them from a Polyhedron() class.

    TESTS::

        sage: import sage.geometry.polyhedron.representation as P
        sage: P.PolyhedronRepresentation()
        <sage.geometry.polyhedron.representation.PolyhedronRepresentation object at ...>
    """
    INEQUALITY = INEQUALITY
    EQUATION = EQUATION
    VERTEX = VERTEX
    RAY = RAY
    LINE = LINE
    def __len__(self) -> int:
        """
        Return the length of the representation data.

        TESTS::

            sage: p = Polyhedron(vertices=[[1,2,3]])
            sage: v = p.Vrepresentation(0)
            sage: v.__len__()
            3
        """
    def __getitem__(self, i):
        """
        Supports indexing.

        TESTS::

            sage: p = Polyhedron(vertices=[[1,2,3]])
            sage: v = p.Vrepresentation(0)
            sage: v.__getitem__(1)
            2
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.geometry.polyhedron.representation import Hrepresentation
            sage: pr = Hrepresentation(Polyhedron(vertices = [[1,2,3]]).parent())
            sage: hash(pr) == hash(tuple([0,0,0,0]))
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare two representation objects.

        This method defines a linear order on the H/V-representation objects.
        The order is first determined by the types of the objects,
        such that inequality < equation < vertex < ray < line.
        Then, representation objects with the same type are ordered
        lexicographically according to their canonical vectors.

        Thus, two representation objects are equal if and only if they define
        the same vertex/ray/line or inequality/equation in the ambient space,
        regardless of the polyhedron that they belong to.

        INPUT:

        - ``other`` -- anything

        OUTPUT: boolean

        EXAMPLES::

            sage: triangle = Polyhedron([(0,0), (1,0), (0,1)])
            sage: ieq = next(triangle.inequality_generator());  ieq
            An inequality (1, 0) x + 0 >= 0
            sage: ieq == copy(ieq)
            True

            sage: square = Polyhedron([(0,0), (1,0), (0,1), (1,1)], base_ring=QQ)
            sage: square.Vrepresentation(0) == triangle.Vrepresentation(0)
            True

            sage: ieq = square.Hrepresentation(0); ieq.vector()
            (0, 1, 0)
            sage: ieq != Polyhedron([(0,1,0)]).Vrepresentation(0)
            True

            sage: H = Polyhedron(vertices=[(4,0)], rays=[(1,1)], lines=[(-1,1)])
            sage: H.vertices()[0] < H.rays()[0] < H.lines()[0]
            True

        TESTS:

        Check :issue:`30954`::

            sage: P = (1/2)*polytopes.cube()
            sage: Q = (1/2)*polytopes.cube(backend='field')
            sage: for p in P.inequalities():
            ....:     assert p in Q.inequalities()
        """
    def vector(self, base_ring=None):
        """
        Return the vector representation of the H/V-representation object.

        INPUT:

        - ``base_ring`` -- the base ring of the vector

        OUTPUT:

        For a V-representation object, a vector of length
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.ambient_dim`. For
        a H-representation object, a vector of length
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.ambient_dim`
        + 1.

        EXAMPLES::

            sage: s = polytopes.cuboctahedron()
            sage: v = next(s.vertex_generator())
            sage: v
            A vertex at (-1, -1, 0)
            sage: v.vector()
            (-1, -1, 0)
            sage: v()
            (-1, -1, 0)
            sage: type(v())
            <class 'sage.modules.vector_integer_dense.Vector_integer_dense'>

        Conversion to a different base ring can be forced with the optional argument::

            sage: v.vector(RDF)
            (-1.0, -1.0, 0.0)
            sage: vector(RDF, v)
            (-1.0, -1.0, 0.0)

        TESTS:

        Checks that :issue:`27709` is fixed::

            sage: C = polytopes.cube()
            sage: C.vertices()[0].vector()[0] = 3
            sage: C.vertices()[0]
            A vertex at (1, -1, -1)
        """
    def polyhedron(self):
        """
        Return the underlying polyhedron.

        TESTS::

            sage: p = Polyhedron(vertices=[[1,2,3]])
            sage: v = p.Vrepresentation(0)
            sage: v.polyhedron()
            A 0-dimensional polyhedron in ZZ^3 defined as the convex hull of 1 vertex
        """
    def __call__(self):
        """
        Return the vector representation of the representation
        object. Shorthand for the vector() method.

        TESTS::

            sage: p = Polyhedron(vertices=[[1,2,3]])
            sage: v = p.Vrepresentation(0)
            sage: v.__call__()
            (1, 2, 3)
        """
    def index(self):
        """
        Return an arbitrary but fixed number according to the internal
        storage order.

        .. NOTE::

            H-representation and V-representation objects are enumerated
            independently. That is, amongst all vertices/rays/lines there
            will be one with ``index()==0``, and amongst all
            inequalities/equations there will be one with ``index()==0``,
            unless the polyhedron is empty or spans the whole space.

        EXAMPLES::

            sage: s = Polyhedron(vertices=[[1],[-1]])
            sage: first_vertex = next(s.vertex_generator())
            sage: first_vertex.index()
            0
            sage: first_vertex == s.Vrepresentation(0)
            True
        """
    def __add__(self, coordinate_list):
        """
        Return the coordinates concatenated with ``coordinate_list``.

        INPUT:

        - ``coordinate_list`` -- list

        OUTPUT: the coordinates of ``self`` concatenated with ``coordinate_list``

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]])
            sage: v = p.Vrepresentation(0); v
            A vertex at (1, 0)
            sage: v + [4,5]
            [1, 0, 4, 5]
        """
    def __radd__(self, coordinate_list):
        """
        Return ``coordinate_list`` concatenated with the coordinates.

        INPUT:

        - ``coordinate_list`` -- list

        OUTPUT: ``coordinate_list`` concatenated with the coordinates of ``self``

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]])
            sage: v = p.Vrepresentation(0); v
            A vertex at (1, 0)
            sage: [4,5] + v
            [4, 5, 1, 0]
        """
    def count(self, i):
        """
        Count the number of occurrences of ``i`` in the coordinates.

        INPUT:

        - ``i`` -- anything

        OUTPUT: integer; the number of occurrences of ``i`` in the coordinates

        EXAMPLES::

            sage: p = Polyhedron(vertices=[(0,1,1,2,1)])
            sage: v = p.Vrepresentation(0); v
            A vertex at (0, 1, 1, 2, 1)
            sage: v.count(1)
            3
        """

class Hrepresentation(PolyhedronRepresentation):
    """
    The internal base class for H-representation objects of
    a polyhedron. Inherits from ``PolyhedronRepresentation``.
    """
    def __init__(self, polyhedron_parent) -> None:
        """
        Initialize the PolyhedronRepresentation object.

        TESTS::

            sage: from sage.geometry.polyhedron.representation import Hrepresentation
            sage: pr = Hrepresentation(Polyhedron(vertices = [[1,2,3]]).parent())
            sage: tuple(pr)
            (0, 0, 0, 0)
            sage: TestSuite(pr).run(skip='_test_pickling')
        """
    def is_H(self):
        """
        Return ``True`` if the object is part of a H-representation
        (inequality or equation).

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: pH.is_H()
            True
        """
    def is_inequality(self):
        """
        Return ``True`` if the object is an inequality of the H-representation.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: pH.is_inequality()
            True
        """
    def is_equation(self):
        """
        Return ``True`` if the object is an equation of the H-representation.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]], eqns = [[1,1,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: pH.is_equation()
            True
        """
    def A(self):
        """
        Return the coefficient vector `A` in `A\\vec{x}+b`.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]])
            sage: pH = p.Hrepresentation(2)
            sage: pH.A()
            (1, 0)

        TESTS:

        Checks that :issue:`27709` is fixed::

            sage: C = polytopes.cube()
            sage: C.inequalities()[0].A()[2] = 5
            sage: C.inequalities()[0]
            An inequality (-1, 0, 0) x + 1 >= 0
        """
    def b(self):
        """
        Return the constant `b` in `A\\vec{x}+b`.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,1,0],[0,0,1],[1,-1,0,],[1,0,-1]])
            sage: pH = p.Hrepresentation(2)
            sage: pH.b()
            0
        """
    def neighbors(self) -> Generator[Incomplete]:
        """
        Iterate over the adjacent facets (i.e. inequalities).

        Only defined for inequalities.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,0,1],[0,0,1,0,],[0,1,0,0],
            ....:                        [1,-1,0,0],[1,0,-1,0,],[1,0,0,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: a = list(pH.neighbors())
            sage: a[0]
            An inequality (0, -1, 0) x + 1 >= 0
            sage: list(a[0])
            [1, 0, -1, 0]

        TESTS:

        Checking that :issue:`28463` is fixed::

            sage: P = polytopes.simplex()
            sage: F1 = P.Hrepresentation()[1]
            sage: list(F1.neighbors())
            [An inequality (0, 1, 0, 0) x + 0 >= 0,
             An inequality (0, 0, 1, 0) x + 0 >= 0,
             An inequality (0, 0, 0, 1) x + 0 >= 0]

        Does not work for equalities::

            sage: F0 = P.Hrepresentation()[0]
            sage: list(F0.neighbors())
            Traceback (most recent call last):
            ...
            TypeError: must be inequality
        """
    def adjacent(self):
        """
        Alias for neighbors().

        TESTS::

            sage: p = Polyhedron(ieqs = [[0,0,0,2],[0,0,1,0,],[0,10,0,0],
            ....:     [1,-1,0,0],[1,0,-1,0,],[1,0,0,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: a = list(pH.neighbors())
            sage: b = list(pH.adjacent())
            sage: a==b
            True
        """
    def is_incident(self, Vobj):
        """
        Return whether the incidence matrix element (Vobj,self) == 1.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,0,1],[0,0,1,0,],[0,1,0,0],
            ....:     [1,-1,0,0],[1,0,-1,0,],[1,0,0,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: pH.is_incident(p.Vrepresentation(1))
            True
            sage: pH.is_incident(p.Vrepresentation(5))
            False
        """
    def __mul__(self, Vobj):
        """
        Shorthand for ``self.eval(x)``.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,0,1],[0,0,1,0,],[0,1,0,0],
            ....:      [1,-1,0,0],[1,0,-1,0,],[1,0,0,-1]])
            sage: pH = p.Hrepresentation(0)
            sage: pH*p.Vrepresentation(5)
            1
        """
    def eval(self, Vobj):
        """
        Evaluate the left hand side `A\\vec{x}+b` on the given
        vertex/ray/line.

        .. NOTE::

          * Evaluating on a vertex returns `A\\vec{x}+b`

          * Evaluating on a ray returns `A\\vec{r}`. Only the sign or
            whether it is zero is meaningful.

          * Evaluating on a line returns `A\\vec{l}`. Only whether it
            is zero or not is meaningful.

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[-1,-1]])
            sage: ineq = next(triangle.inequality_generator())
            sage: ineq
            An inequality (2, -1) x + 1 >= 0
            sage: [ ineq.eval(v) for v in triangle.vertex_generator() ]
            [0, 0, 3]
            sage: [ ineq * v for v in triangle.vertex_generator() ]
            [0, 0, 3]

        If you pass a vector, it is assumed to be the coordinate vector of a point::

            sage: ineq.eval( vector(ZZ, [3,2]) )
            5
        """
    def incident(self) -> Generator[Incomplete]:
        """
        Return a generator for the incident H-representation objects,
        that is, the vertices/rays/lines satisfying the (in)equality.

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[-1,-1]])
            sage: ineq = next(triangle.inequality_generator())
            sage: ineq
            An inequality (2, -1) x + 1 >= 0
            sage: [ v for v in ineq.incident()]
            [A vertex at (-1, -1), A vertex at (0, 1)]
            sage: p = Polyhedron(vertices=[[0,0,0],[0,1,0],[0,0,1]], rays=[[1,-1,-1]])
            sage: ineq = p.Hrepresentation(2)
            sage: ineq
            An inequality (1, 0, 1) x + 0 >= 0
            sage: [ x for x in ineq.incident() ]
            [A vertex at (0, 0, 0),
             A vertex at (0, 1, 0),
             A ray in the direction (1, -1, -1)]
        """
    def repr_pretty(self, **kwds):
        """
        Return a pretty representation of this equality/inequality.

        INPUT:

        - ``prefix`` -- string

        - ``indices`` -- tuple or other iterable

        - ``latex`` -- boolean

        OUTPUT: string

        EXAMPLES::

            sage: P = Polyhedron(ieqs=[(0, 1, 0, 0), (1, 2, 1, 0)],
            ....:                eqns=[(1, -1, -1, 1)])
            sage: for h in P.Hrepresentation():
            ....:     print(h.repr_pretty())
            x0 + x1 - x2 == 1
            x0 >= 0
            2*x0 + x1 >= -1
        """

class Inequality(Hrepresentation):
    """
    A linear inequality (supporting hyperplane) of the
    polyhedron. Inherits from ``Hrepresentation``.
    """
    def type(self):
        """
        Return the type (equation/inequality/vertex/ray/line) as an
        integer.

        OUTPUT:

        Integer. One of ``PolyhedronRepresentation.INEQUALITY``,
        ``.EQUATION``, ``.VERTEX``, ``.RAY``, or ``.LINE``.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: repr_obj = next(p.inequality_generator())
            sage: repr_obj.type()
            0
            sage: repr_obj.type() == repr_obj.INEQUALITY
            True
            sage: repr_obj.type() == repr_obj.EQUATION
            False
            sage: repr_obj.type() == repr_obj.VERTEX
            False
            sage: repr_obj.type() == repr_obj.RAY
            False
            sage: repr_obj.type() == repr_obj.LINE
            False
        """
    def is_inequality(self):
        """
        Return ``True`` since this is, by construction, an inequality.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: a = next(p.inequality_generator())
            sage: a.is_inequality()
            True
        """
    def is_facet_defining_inequality(self, other):
        """
        Check if ``self`` defines a facet of ``other``.

        INPUT:

        - ``other`` -- a polyhedron

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.slack_matrix`
            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`

        EXAMPLES::

            sage: P = Polyhedron(vertices=[[0,0,0],[0,1,0]], rays=[[1,0,0]])
            sage: P.inequalities()
            (An inequality (1, 0, 0) x + 0 >= 0,
             An inequality (0, 1, 0) x + 0 >= 0,
             An inequality (0, -1, 0) x + 1 >= 0)
            sage: Q = Polyhedron(ieqs=[[0,1,0,0]])
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            True
            sage: Q = Polyhedron(ieqs=[[0,2,0,3]])
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            True
            sage: Q = Polyhedron(ieqs=[[0,AA(2).sqrt(),0,3]])                           # needs sage.rings.number_field
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            True
            sage: Q = Polyhedron(ieqs=[[1,1,0,0]])
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            False

        ::

            sage: P = Polyhedron(vertices=[[0,0,0],[0,1,0]], lines=[[1,0,0]])
            sage: P.inequalities()
            (An inequality (0, 1, 0) x + 0 >= 0, An inequality (0, -1, 0) x + 1 >= 0)
            sage: Q = Polyhedron(ieqs=[[0,1,0,0]])
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            False
            sage: Q = Polyhedron(ieqs=[[0,-1,0,0]])
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            False
            sage: Q = Polyhedron(ieqs=[[0,0,1,3]])
            sage: Q.inequalities()[0].is_facet_defining_inequality(P)
            True

        TESTS::

            sage: p1 = Polyhedron(backend='normaliz', base_ring=QQ, vertices=[  # optional - pynormaliz
            ....:     (2/3, 2/3, 2/3, 2/3, 2/3, 2/3, 2/3, 2/3, 2/3),
            ....:     (1, 1, 1, 9/10, 4/5, 7/10, 3/5, 0, 0),
            ....:     (1, 1, 1, 1, 4/5, 3/5, 1/2, 1/10, 0),
            ....:     (1, 1, 1, 1, 9/10, 1/2, 2/5, 1/5, 0),
            ....:     (1, 1, 1, 1, 1, 2/5, 3/10, 1/5, 1/10)])
            sage: p2 = Polyhedron(backend='ppl', base_ring=QQ, vertices=[
            ....:     (2/3, 2/3, 2/3, 2/3, 2/3, 2/3, 2/3, 2/3, 2/3),
            ....:     (1, 1, 1, 9/10, 4/5, 7/10, 3/5, 0, 0),
            ....:     (1, 1, 1, 1, 4/5, 3/5, 1/2, 1/10, 0),
            ....:     (1, 1, 1, 1, 9/10, 1/2, 2/5, 1/5, 0),
            ....:     (1, 1, 1, 1, 1, 2/5, 3/10, 1/5, 1/10)])
            sage: p2 == p1                                                      # optional - pynormaliz
            True
            sage: for ieq in p1.inequalities():                                 # optional - pynormaliz
            ....:     assert ieq.is_facet_defining_inequality(p2)
            sage: for ieq in p2.inequalities():                                 # optional - pynormaliz
            ....:     assert ieq.is_facet_defining_inequality(p1)
        """
    def contains(self, Vobj):
        """
        Test whether the halfspace (including its boundary) defined
        by the inequality contains the given vertex/ray/line.

        EXAMPLES::

            sage: p = polytopes.cross_polytope(3)
            sage: i1 = next(p.inequality_generator())
            sage: [i1.contains(q) for q in p.vertex_generator()]
            [True, True, True, True, True, True]
            sage: p2 = 3*polytopes.hypercube(3)
            sage: [i1.contains(q) for q in p2.vertex_generator()]
            [True, True, False, True, False, True, False, False]
        """
    def interior_contains(self, Vobj):
        """
        Test whether the interior of the halfspace (excluding its
        boundary) defined by the inequality contains the given
        vertex/ray/line.

        EXAMPLES::

            sage: p = polytopes.cross_polytope(3)
            sage: i1 = next(p.inequality_generator())
            sage: [i1.interior_contains(q) for q in p.vertex_generator()]
            [False, True, True, False, False, True]
            sage: p2 = 3*polytopes.hypercube(3)
            sage: [i1.interior_contains(q) for q in p2.vertex_generator()]
            [True, True, False, True, False, True, False, False]

        If you pass a vector, it is assumed to be the coordinate vector of a point::

            sage: P = Polyhedron(vertices=[[1,1],[1,-1],[-1,1],[-1,-1]])
            sage: p = vector(ZZ, [1,0] )
            sage: [ ieq.interior_contains(p) for ieq in P.inequality_generator() ]
            [True, True, False, True]
        """
    def outer_normal(self):
        """
        Return the outer normal vector of ``self``.

        OUTPUT: the normal vector directed away from the interior of the polyhedron

        EXAMPLES::

            sage: p = Polyhedron(vertices=[[0,0,0],[1,1,0],[1,2,0]])
            sage: a = next(p.inequality_generator())
            sage: a.outer_normal()
            (1, -1, 0)
        """

class Equation(Hrepresentation):
    """
    A linear equation of the polyhedron. That is, the polyhedron is
    strictly smaller-dimensional than the ambient space, and contained
    in this hyperplane. Inherits from ``Hrepresentation``.
    """
    def type(self):
        """
        Return the type (equation/inequality/vertex/ray/line) as an
        integer.

        OUTPUT:

        Integer. One of ``PolyhedronRepresentation.INEQUALITY``,
        ``.EQUATION``, ``.VERTEX``, ``.RAY``, or ``.LINE``.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: repr_obj = next(p.equation_generator())
            sage: repr_obj.type()
            1
            sage: repr_obj.type() == repr_obj.INEQUALITY
            False
            sage: repr_obj.type() == repr_obj.EQUATION
            True
            sage: repr_obj.type() == repr_obj.VERTEX
            False
            sage: repr_obj.type() == repr_obj.RAY
            False
            sage: repr_obj.type() == repr_obj.LINE
            False
        """
    def is_equation(self):
        """
        Test if this object is an equation.  By construction, it must be.

        TESTS::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: a = next(p.equation_generator())
            sage: a.is_equation()
            True
        """
    def contains(self, Vobj):
        """
        Test whether the hyperplane defined by the equation contains
        the given vertex/ray/line.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: v = next(p.vertex_generator())
            sage: v
            A vertex at (0, 0, 0)
            sage: a = next(p.equation_generator())
            sage: a
            An equation (0, 0, 1) x + 0 == 0
            sage: a.contains(v)
            True
        """
    def interior_contains(self, Vobj):
        """
        Test whether the interior of the halfspace (excluding its
        boundary) defined by the inequality contains the given
        vertex/ray/line.

        .. NOTE::

            Return ``False`` for any equation.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: v = next(p.vertex_generator())
            sage: v
            A vertex at (0, 0, 0)
            sage: a = next(p.equation_generator())
            sage: a
            An equation (0, 0, 1) x + 0 == 0
            sage: a.interior_contains(v)
            False
        """

class Vrepresentation(PolyhedronRepresentation):
    """
    The base class for V-representation objects of a
    polyhedron. Inherits from ``PolyhedronRepresentation``.
    """
    def __init__(self, polyhedron_parent) -> None:
        """
        Initialize the PolyhedronRepresentation object.

        TESTS::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: a = next(p.inequality_generator())
            sage: a
            An inequality (-1, 1, 0) x + 0 >= 0
            sage: TestSuite(a).run(skip='_test_pickling')
        """
    def is_V(self):
        """
        Return ``True`` if the object is part of a V-representation
        (a vertex, ray, or line).

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0],[1,0],[0,3],[1,3]])
            sage: v = next(p.vertex_generator())
            sage: v.is_V()
            True
        """
    def is_vertex(self):
        """
        Return ``True`` if the object is a vertex of the V-representation.
        This method is over-ridden by the corresponding method in the
        derived class Vertex.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0],[1,0],[0,3],[1,3]])
            sage: v = next(p.vertex_generator())
            sage: v.is_vertex()
            True
            sage: p = Polyhedron(ieqs = [[1, 0, 0, 0, 1], [1, 1, 0, 0, 0], [1, 0, 1, 0, 0]])
            sage: r1 = next(p.ray_generator())
            sage: r1.is_vertex()
            False
        """
    def is_ray(self):
        """
        Return ``True`` if the object is a ray of the V-representation.
        This method is over-ridden by the corresponding method in the
        derived class Ray.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[1, 0, 0, 0, 1], [1, 1, 0, 0, 0], [1, 0, 1, 0, 0]])
            sage: r1 = next(p.ray_generator())
            sage: r1.is_ray()
            True
            sage: v1 = next(p.vertex_generator())
            sage: v1
            A vertex at (-1, -1, 0, -1)
            sage: v1.is_ray()
            False
        """
    def is_line(self):
        """
        Return ``True`` if the object is a line of the V-representation.
        This method is over-ridden by the corresponding method in the
        derived class Line.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[1, 0, 0, 0, 1], [1, 1, 0, 0, 0], [1, 0, 1, 0, 0]])
            sage: line1 = next(p.line_generator())
            sage: line1.is_line()
            True
            sage: v1 = next(p.vertex_generator())
            sage: v1.is_line()
            False
        """
    def neighbors(self) -> Generator[Incomplete]:
        """
        Return a generator for the adjacent vertices/rays/lines.

        EXAMPLES::

             sage: p = Polyhedron(vertices = [[0,0],[1,0],[0,3],[1,4]])
             sage: v = next(p.vertex_generator())
             sage: next(v.neighbors())
             A vertex at (0, 3)
        """
    def adjacent(self):
        """
        Alias for neighbors().

        TESTS::

            sage: p = Polyhedron(vertices = [[0,0],[1,0],[0,3],[1,4]])
            sage: v = next(p.vertex_generator())
            sage: a = next(v.neighbors())
            sage: b = next(v.adjacent())
            sage: a==b
            True
        """
    def is_incident(self, Hobj):
        """
        Return whether the incidence matrix element (self,Hobj) == 1.

        EXAMPLES::

            sage: p = polytopes.hypercube(3)
            sage: h1 = next(p.inequality_generator())
            sage: h1
            An inequality (-1, 0, 0) x + 1 >= 0
            sage: v1 = next(p.vertex_generator())
            sage: v1
            A vertex at (1, -1, -1)
            sage: v1.is_incident(h1)
            True
        """
    def __mul__(self, Hobj):
        """
        Shorthand for self.evaluated_on(Hobj).

        TESTS::

            sage: p = polytopes.hypercube(3)
            sage: h1 = next(p.inequality_generator())
            sage: v1 = next(p.vertex_generator())
            sage: v1.__mul__(h1)
            0
        """
    def incident(self) -> Generator[Incomplete]:
        """
        Return a generator for the equations/inequalities that are satisfied on the given
        vertex/ray/line.

        EXAMPLES::

            sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[-1,-1]])
            sage: ineq = next(triangle.inequality_generator())
            sage: ineq
            An inequality (2, -1) x + 1 >= 0
            sage: [ v for v in ineq.incident()]
            [A vertex at (-1, -1), A vertex at (0, 1)]
            sage: p = Polyhedron(vertices=[[0,0,0],[0,1,0],[0,0,1]], rays=[[1,-1,-1]])
            sage: ineq = p.Hrepresentation(2)
            sage: ineq
            An inequality (1, 0, 1) x + 0 >= 0
            sage: [ x for x in ineq.incident() ]
            [A vertex at (0, 0, 0),
             A vertex at (0, 1, 0),
             A ray in the direction (1, -1, -1)]
        """

class Vertex(Vrepresentation):
    """
    A vertex of the polyhedron. Inherits from ``Vrepresentation``.
    """
    def type(self):
        """
        Return the type (equation/inequality/vertex/ray/line) as an
        integer.

        OUTPUT:

        Integer. One of ``PolyhedronRepresentation.INEQUALITY``,
        ``.EQUATION``, ``.VERTEX``, ``.RAY``, or ``.LINE``.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[0,0,0],[1,1,0],[1,2,0]])
            sage: repr_obj = next(p.vertex_generator())
            sage: repr_obj.type()
            2
            sage: repr_obj.type() == repr_obj.INEQUALITY
            False
            sage: repr_obj.type() == repr_obj.EQUATION
            False
            sage: repr_obj.type() == repr_obj.VERTEX
            True
            sage: repr_obj.type() == repr_obj.RAY
            False
            sage: repr_obj.type() == repr_obj.LINE
            False
        """
    def is_vertex(self):
        """
        Test if this object is a vertex.  By construction it always is.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,1],[0,1,0],[1,-1,0]])
            sage: a = next(p.vertex_generator())
            sage: a.is_vertex()
            True
        """
    def homogeneous_vector(self, base_ring=None):
        """
        Return homogeneous coordinates for this vertex.

        Since a vertex is given by an affine point, this is the vector
        with a 1 appended.

        INPUT:

        - ``base_ring`` -- the base ring of the vector

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(2,0)], rays=[(1,0)], lines=[(3,2)])
            sage: P.vertices()[0].homogeneous_vector()
            (2, 0, 1)
            sage: P.vertices()[0].homogeneous_vector(RDF)
            (2.0, 0.0, 1.0)
        """
    def evaluated_on(self, Hobj):
        """
        Return `A\\vec{x}+b`.

        EXAMPLES::

            sage: p = polytopes.hypercube(3)
            sage: v = next(p.vertex_generator())
            sage: h = next(p.inequality_generator())
            sage: v
            A vertex at (1, -1, -1)
            sage: h
            An inequality (-1, 0, 0) x + 1 >= 0
            sage: v.evaluated_on(h)
            0
        """
    def is_integral(self):
        """
        Return whether the coordinates of the vertex are all integral.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = Polyhedron([(1/2,3,5), (0,0,0), (2,3,7)])
            sage: [ v.is_integral() for v in p.vertex_generator() ]
            [True, False, True]
        """

class Ray(Vrepresentation):
    """
    A ray of the polyhedron. Inherits from ``Vrepresentation``.
    """
    def type(self):
        """
        Return the type (equation/inequality/vertex/ray/line) as an
        integer.

        OUTPUT:

        Integer. One of ``PolyhedronRepresentation.INEQUALITY``,
        ``.EQUATION``, ``.VERTEX``, ``.RAY``, or ``.LINE``.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,1],[0,1,0],[1,-1,0]])
            sage: repr_obj = next(p.ray_generator())
            sage: repr_obj.type()
            3
            sage: repr_obj.type() == repr_obj.INEQUALITY
            False
            sage: repr_obj.type() == repr_obj.EQUATION
            False
            sage: repr_obj.type() == repr_obj.VERTEX
            False
            sage: repr_obj.type() == repr_obj.RAY
            True
            sage: repr_obj.type() == repr_obj.LINE
            False
        """
    def is_ray(self):
        """
        Test if this object is a ray.  Always ``True`` by construction.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,1],[0,1,0],[1,-1,0]])
            sage: a = next(p.ray_generator())
            sage: a.is_ray()
            True
        """
    def homogeneous_vector(self, base_ring=None):
        """
        Return homogeneous coordinates for this ray.

        Since a ray is given by a direction, this is the vector with a
        0 appended.

        INPUT:

        - ``base_ring`` -- the base ring of the vector

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(2,0)], rays=[(1,0)], lines=[(3,2)])
            sage: P.rays()[0].homogeneous_vector()
            (1, 0, 0)
            sage: P.rays()[0].homogeneous_vector(RDF)
            (1.0, 0.0, 0.0)
        """
    def evaluated_on(self, Hobj):
        """
        Return `A\\vec{r}`.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[0,0,1],[0,1,0],[1,-1,0]])
            sage: a = next(p.ray_generator())
            sage: h = next(p.inequality_generator())
            sage: a.evaluated_on(h)
            0
        """

class Line(Vrepresentation):
    """
    A line (Minkowski summand `\\simeq\\RR`) of the
    polyhedron. Inherits from ``Vrepresentation``.
    """
    def type(self):
        """
        Return the type (equation/inequality/vertex/ray/line) as an
        integer.

        OUTPUT:

        Integer. One of ``PolyhedronRepresentation.INEQUALITY``,
        ``.EQUATION``, ``.VERTEX``, ``.RAY``, or ``.LINE``.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[1, 0, 0, 1],[1,1,0,0]])
            sage: repr_obj = next(p.line_generator())
            sage: repr_obj.type()
            4
            sage: repr_obj.type() == repr_obj.INEQUALITY
            False
            sage: repr_obj.type() == repr_obj.EQUATION
            False
            sage: repr_obj.type() == repr_obj.VERTEX
            False
            sage: repr_obj.type() == repr_obj.RAY
            False
            sage: repr_obj.type() == repr_obj.LINE
            True
        """
    def is_line(self):
        """
        Test if the object is a line.  By construction it must be.

        TESTS::

            sage: p = Polyhedron(ieqs = [[1, 0, 0, 1],[1,1,0,0]])
            sage: a = next(p.line_generator())
            sage: a.is_line()
            True
        """
    def homogeneous_vector(self, base_ring=None):
        """
        Return homogeneous coordinates for this line.

        Since a line is given by a direction, this is the vector with a
        0 appended.

        INPUT:

        - ``base_ring`` -- the base ring of the vector

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(2,0)], rays=[(1,0)], lines=[(3,2)])
            sage: P.lines()[0].homogeneous_vector()
            (3, 2, 0)
            sage: P.lines()[0].homogeneous_vector(RDF)
            (3.0, 2.0, 0.0)
        """
    def evaluated_on(self, Hobj):
        """
        Return `A\\vec{\\ell}`.

        EXAMPLES::

            sage: p = Polyhedron(ieqs = [[1, 0, 0, 1],[1,1,0,0]])
            sage: a = next(p.line_generator())
            sage: h = next(p.inequality_generator())
            sage: a.evaluated_on(h)
            0
        """

def repr_pretty(coefficients, type, prefix: str = 'x', indices=None, latex: bool = False, style: str = '>=', split: bool = False):
    """
    Return a pretty representation of equation/inequality represented
    by the coefficients.

    INPUT:

    - ``coefficients`` -- tuple or other iterable

    - ``type`` -- either ``0`` (``PolyhedronRepresentation.INEQUALITY``)
      or ``1`` (``PolyhedronRepresentation.EQUATION``)

    - ``prefix`` -- string (default: ``'x'``)

    - ``indices`` -- tuple or other iterable

    - ``latex`` -- boolean

    - ``split`` -- boolean (default: ``False``); if set to ``True``,
      the output is split into a 3-tuple containing the left-hand side,
      the relation, and the right-hand side of the object

    - ``style`` -- either ``'positive'`` (making all coefficients positive), or
      ``'<='`` or ``'>='``

    OUTPUT: a string or 3-tuple of strings (depending on ``split``)

    EXAMPLES::

        sage: from sage.geometry.polyhedron.representation import repr_pretty
        sage: from sage.geometry.polyhedron.representation import PolyhedronRepresentation
        sage: print(repr_pretty((0, 1, 0, 0), PolyhedronRepresentation.INEQUALITY))
        x0 >= 0
        sage: print(repr_pretty((1, 2, 1, 0), PolyhedronRepresentation.INEQUALITY))
        2*x0 + x1 >= -1
        sage: print(repr_pretty((1, -1, -1, 1), PolyhedronRepresentation.EQUATION))
        -x0 - x1 + x2 == -1
    """
