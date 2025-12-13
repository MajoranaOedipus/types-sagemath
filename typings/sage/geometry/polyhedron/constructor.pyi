from sage.rings.integer_ring import ZZ as ZZ

def Polyhedron(vertices=None, rays=None, lines=None, ieqs=None, eqns=None, ambient_dim=None, base_ring=None, minimize: bool = True, verbose: bool = False, backend=None, mutable: bool = False):
    '''
    Construct a polyhedron object.

    You may either define it with vertex/ray/line or
    inequalities/equations data, but not both. Redundant data will
    automatically be removed (unless ``minimize=False``), and the
    complementary representation will be computed.

    INPUT:

    - ``vertices`` -- iterable of points. Each point can be specified as
      any iterable container of ``base_ring`` elements. If ``rays`` or
      ``lines`` are specified but no ``vertices``, the origin is
      taken to be the single vertex.

      Instead of vertices, the first argument can also be an object
      that can be converted to a :func:`Polyhedron` via an :meth:`as_polyhedron`
      or :meth:`polyhedron` method. In this case, the following 5 arguments
      cannot be provided.

    - ``rays`` -- list of rays; each ray can be specified as any
      iterable container of ``base_ring`` elements

    - ``lines`` -- list of lines; each line can be specified as any
      iterable container of ``base_ring`` elements

    - ``ieqs`` -- list of inequalities; each line can be specified as any
      iterable container of ``base_ring`` elements. An entry equal to
      ``[-1,7,3,4]`` represents the inequality `7x_1+3x_2+4x_3\\geq 1`.

    - ``eqns`` -- list of equalities; each line can be specified as
      any iterable container of ``base_ring`` elements. An entry equal to
      ``[-1,7,3,4]`` represents the equality `7x_1+3x_2+4x_3= 1`.

    - ``ambient_dim`` -- integer; the ambient space dimension. Usually
      can be figured out automatically from the H/Vrepresentation
      dimensions.

    - ``base_ring`` -- a sub-field of the reals implemented in
      Sage. The field over which the polyhedron will be defined. For
      ``QQ`` and algebraic extensions, exact arithmetic will be
      used. For ``RDF``, floating point numbers will be used. Floating
      point arithmetic is faster but might give the wrong result for
      degenerate input.

    - ``backend`` -- string or ``None`` (default). The backend to use. Valid choices are

      * ``\'cdd\'``: use cdd
        (:mod:`~sage.geometry.polyhedron.backend_cdd`) with `\\QQ` or
        `\\RDF` coefficients depending on ``base_ring``

      * ``\'normaliz\'``: use normaliz
        (:mod:`~sage.geometry.polyhedron.backend_normaliz`) with `\\ZZ` or
        `\\QQ` coefficients depending on ``base_ring``

      * ``\'polymake\'``: use polymake
        (:mod:`~sage.geometry.polyhedron.backend_polymake`) with `\\QQ`, `\\RDF` or
        ``QuadraticField`` coefficients depending on ``base_ring``

      * ``\'ppl\'``: use ppl
        (:mod:`~sage.geometry.polyhedron.backend_ppl`) with `\\ZZ` or
        `\\QQ` coefficients depending on ``base_ring``

      * ``\'field\'``: use python implementation
        (:mod:`~sage.geometry.polyhedron.backend_field`) for any field

    Some backends support further optional arguments:

    - ``minimize`` -- boolean (default: ``True``); whether to
      immediately remove redundant H/V-representation data; currently
      not used.

    - ``verbose`` -- boolean (default: ``False``); whether to print
      verbose output for debugging purposes; only supported by the cdd and
      normaliz backends

    - ``mutable`` -- boolean (default: ``False``); whether the polyhedron
      is mutable

    OUTPUT: the polyhedron defined by the input data

    EXAMPLES:

    Construct some polyhedra::

        sage: square_from_vertices = Polyhedron(vertices = [[1, 1], [1, -1], [-1, 1], [-1, -1]])
        sage: square_from_ieqs = Polyhedron(ieqs = [[1, 0, 1], [1, 1, 0], [1, 0, -1], [1, -1, 0]])
        sage: list(square_from_ieqs.vertex_generator())
        [A vertex at (1, -1),
         A vertex at (1, 1),
         A vertex at (-1, 1),
         A vertex at (-1, -1)]
        sage: list(square_from_vertices.inequality_generator())
        [An inequality (1, 0) x + 1 >= 0,
         An inequality (0, 1) x + 1 >= 0,
         An inequality (-1, 0) x + 1 >= 0,
         An inequality (0, -1) x + 1 >= 0]
        sage: p = Polyhedron(vertices = [[1.1, 2.2], [3.3, 4.4]], base_ring=RDF)
        sage: p.n_inequalities()
        2

    The same polyhedron given in two ways::

        sage: p = Polyhedron(ieqs = [[0,1,0,0],[0,0,1,0]])
        sage: p.Vrepresentation()
        (A line in the direction (0, 0, 1),
         A ray in the direction (1, 0, 0),
         A ray in the direction (0, 1, 0),
         A vertex at (0, 0, 0))
        sage: q = Polyhedron(vertices=[[0,0,0]], rays=[[1,0,0],[0,1,0]], lines=[[0,0,1]])
        sage: q.Hrepresentation()
        (An inequality (1, 0, 0) x + 0 >= 0,
         An inequality (0, 1, 0) x + 0 >= 0)

    Finally, a more complicated example. Take `\\mathbb{R}_{\\geq 0}^6` with
    coordinates `a, b, \\dots, f` and

      * The inequality `e+b \\geq c+d`
      * The inequality `e+c \\geq b+d`
      * The equation `a+b+c+d+e+f = 31`

    ::

        sage: positive_coords = Polyhedron(ieqs=[
        ....:     [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
        ....:     [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
        sage: P = Polyhedron(ieqs=positive_coords.inequalities() + (
        ....:     [0,0,1,-1,-1,1,0], [0,0,-1,1,-1,1,0]), eqns=[[-31,1,1,1,1,1,1]])
        sage: P
        A 5-dimensional polyhedron in QQ^6 defined as the convex hull of 7 vertices
        sage: P.dim()
        5
        sage: P.Vrepresentation()
        (A vertex at (31, 0, 0, 0, 0, 0), A vertex at (0, 0, 0, 0, 0, 31),
         A vertex at (0, 0, 0, 0, 31, 0), A vertex at (0, 0, 31/2, 0, 31/2, 0),
         A vertex at (0, 31/2, 31/2, 0, 0, 0), A vertex at (0, 31/2, 0, 0, 31/2, 0),
         A vertex at (0, 0, 0, 31/2, 31/2, 0))

    Regular icosahedron, centered at `0` with edge length `2`, with vertices given
    by the cyclic shifts of `(0, \\pm 1, \\pm (1+\\sqrt(5))/2)`, cf.
    :wikipedia:`Regular_icosahedron`. It needs a number field::

        sage: # needs sage.rings.number_field
        sage: R0.<r0> = QQ[]
        sage: R1.<r1> = NumberField(r0^2-5, embedding=AA(5)**(1/2))
        sage: gold = (1+r1)/2
        sage: v = [[0, 1, gold], [0, 1, -gold], [0, -1, gold], [0, -1, -gold]]
        sage: pp = Permutation((1, 2, 3))
        sage: icosah = Polyhedron(                                                      # needs sage.combinat
        ....:    [(pp^2).action(w) for w in v] + [pp.action(w) for w in v] + v,
        ....:    base_ring=R1)
        sage: len(icosah.faces(2))                                                      # needs sage.combinat
        20

    When the input contains elements of a Number Field, they require an
    embedding::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, \'x\')
        sage: K = NumberField(x^2 - 2,\'s\')
        sage: s = K.0
        sage: L = NumberField(x^3 - 2,\'t\')
        sage: t = L.0
        sage: P = Polyhedron(vertices=[[0,s], [t,0]])
        Traceback (most recent call last):
        ...
        ValueError: invalid base ring

    Converting from a given polyhedron::

        sage: cb = polytopes.cube(); cb
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron(cb, base_ring=QQ)
        A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 8 vertices

    Converting from other objects to a polyhedron::

        sage: quadrant = Cone([(1,0), (0,1)])
        sage: Polyhedron(quadrant)
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays
        sage: Polyhedron(quadrant, base_ring=QQ)
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 rays

        sage: o = lattice_polytope.cross_polytope(2)
        sage: Polyhedron(o)
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices
        sage: Polyhedron(o, base_ring=QQ)
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
        sage: x, y = p[\'x\'], p[\'y\']
        sage: p.add_constraint(x <= 1)
        sage: p.add_constraint(x >= -1)
        sage: p.add_constraint(y <= 1)
        sage: p.add_constraint(y >= -1)
        sage: Polyhedron(p, base_ring=ZZ)
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices
        sage: Polyhedron(p)
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        sage: # needs sage.combinat
        sage: H.<x,y> = HyperplaneArrangements(QQ)
        sage: h = x + y - 1; h
        Hyperplane x + y - 1
        sage: Polyhedron(h, base_ring=ZZ)
        A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 1 line
        sage: Polyhedron(h)
        A 1-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 line

    .. NOTE::

      * Once constructed, a ``Polyhedron`` object is immutable.

      * Although the option ``base_ring=RDF`` allows numerical data to
        be used, it might not give the right answer for degenerate
        input data - the results can depend upon the tolerance
        setting of cdd.

    TESTS:

    Check that giving ``float`` input gets converted to ``RDF`` (see :issue:`22605`)::

        sage: f = float(1.1)
        sage: Polyhedron(vertices=[[f]])
        A 0-dimensional polyhedron in RDF^1 defined as the convex hull of 1 vertex

    Check that giving ``int`` input gets converted to ``ZZ`` (see :issue:`22605`)::

        sage: Polyhedron(vertices=[[int(42)]])
        A 0-dimensional polyhedron in ZZ^1 defined as the convex hull of 1 vertex

    Check that giving ``Fraction`` input gets converted to ``QQ`` (see :issue:`22605`)::

        sage: from fractions import Fraction
        sage: f = Fraction(int(6), int(8))
        sage: Polyhedron(vertices=[[f]])
        A 0-dimensional polyhedron in QQ^1 defined as the convex hull of 1 vertex

    Check that non-compact polyhedra given by V-representation have base ring ``QQ``,
    not ``ZZ`` (see :issue:`27840`)::

        sage: Q = Polyhedron(vertices=[(1, 2, 3), (1, 3, 2), (2, 1, 3),
        ....:                          (2, 3, 1), (3, 1, 2), (3, 2, 1)],
        ....:                rays=[[1, 1, 1]], lines=[[1, 2, 3]], backend=\'ppl\')
        sage: Q.base_ring()
        Rational Field

    Check that enforcing base ring `ZZ` for this example gives an error::

        sage: Q = Polyhedron(vertices=[(1, 2, 3), (1, 3, 2), (2, 1, 3),
        ....:                          (2, 3, 1), (3, 1, 2), (3, 2, 1)],
        ....:                rays=[[1, 1, 1]], lines=[[1, 2, 3]], backend=\'ppl\',
        ....:                base_ring=ZZ)
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer

    Check that input with too many bits of precision returns an error (see
    :issue:`22552`)::

        sage: Polyhedron(vertices=[(8.3319544851638732, 7.0567045956967727),            # needs sage.rings.real_mpfr
        ....:                      (6.4876921900819049, 4.8435898415984129)])
        Traceback (most recent call last):
        ...
        ValueError: the only allowed inexact ring is \'RDF\' with backend \'cdd\'

    Check that setting ``base_ring`` to a ``RealField`` returns an error (see :issue:`22552`)::

        sage: Polyhedron(vertices=[(8.3, 7.0), (6.4, 4.8)], base_ring=RealField(40))    # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        ValueError: no default backend for computations with Real Field with 40 bits of precision
        sage: Polyhedron(vertices=[(8.3, 7.0), (6.4, 4.8)], base_ring=RealField(53))    # needs sage.rings.real_mpfr
        Traceback (most recent call last):
        ...
        ValueError: no default backend for computations with Real Field with 53 bits of precision

    Check that :issue:`17339` is fixed::

        sage: Polyhedron(ambient_dim=0, ieqs=[], eqns=[[1]], base_ring=QQ)
        The empty polyhedron in QQ^0
        sage: P = Polyhedron(ambient_dim=0, ieqs=[], eqns=[], base_ring=QQ); P
        A 0-dimensional polyhedron in QQ^0 defined as the convex hull of 1 vertex
        sage: P.Vrepresentation()
        (A vertex at (),)
        sage: Polyhedron(ambient_dim=2, ieqs=[], eqns=[], base_ring=QQ)
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull
         of 1 vertex and 2 lines
        sage: Polyhedron(ambient_dim=2, ieqs=[], eqns=[], base_ring=QQ, backend=\'field\')
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull
         of 1 vertex and 2 lines
        sage: Polyhedron(ambient_dim=0, ieqs=[], eqns=[[1]], base_ring=QQ, backend=\'cdd\')
        The empty polyhedron in QQ^0
        sage: Polyhedron(ambient_dim=0, ieqs=[], eqns=[[1]], base_ring=QQ, backend=\'ppl\')
        The empty polyhedron in QQ^0
        sage: Polyhedron(ambient_dim=0, ieqs=[], eqns=[[1]], base_ring=QQ, backend=\'field\')
        The empty polyhedron in QQ^0

        sage: Polyhedron(ambient_dim=2, vertices=[], rays=[], lines=[], base_ring=QQ)
        The empty polyhedron in QQ^2

    Create a mutable polyhedron::

        sage: P = Polyhedron(vertices=[[0, 1], [1, 0]], mutable=True)
        sage: P.is_mutable()
        True
        sage: hasattr(P, "_Vrepresentation")
        False
        sage: P.Vrepresentation()
        (A vertex at (0, 1), A vertex at (1, 0))
        sage: hasattr(P, "_Vrepresentation")
        True

    .. SEEALSO::

        :mod:`Library of polytopes <sage.geometry.polyhedron.library>`
    '''
