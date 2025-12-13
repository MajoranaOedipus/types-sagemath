from _typeshed import Incomplete
from sage.combinat.permutation import Permutation as Permutation
from sage.functions.generalized import sign as sign
from sage.geometry.voronoi_diagram import VoronoiDiagram as VoronoiDiagram
from sage.graphs.graph import Graph as Graph
from sage.groups.braid import BraidGroup as BraidGroup
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.groups.perm_gps.permgroup_named import SymmetricGroup as SymmetricGroup
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.parallel.decorate import parallel as parallel
from sage.rings.complex_interval_field import ComplexIntervalField as ComplexIntervalField
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field import NumberField as NumberField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.qqbar import QQbar as QQbar
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField
from sage.schemes.curves.constructor import Curve as Curve

roots_interval_cache: Incomplete

def braid_from_piecewise(strands):
    """
    Compute the braid corresponding to the piecewise linear curves strands.

    INPUT:

    - ``strands`` -- list of lists of tuples ``(t, c1, c2)``, where ``t``
      is a number between 0 and 1, and ``c1`` and ``c2`` are rationals
      or algebraic reals

    OUTPUT: the braid formed by the piecewise linear strands

    EXAMPLES::

        sage: # needs sirocco
        sage: from sage.schemes.curves.zariski_vankampen import braid_from_piecewise
        sage: paths = [[(0, 0, 1), (0.2, -1, -0.5), (0.8, -1, 0), (1, 0, -1)],
        ....:          [(0, -1, 0), (0.5, 0, -1), (1, 1, 0)],
        ....:          [(0, 1, 0), (0.5, 1, 1), (1, 0, 1)]]
        sage: braid_from_piecewise(paths)
        s0*s1
    """
def discrim(pols) -> tuple:
    """
    Return the points in the discriminant of the product of the polynomials
    of a list or tuple ``pols``.

    The result is the set of values of the first variable for which
    two roots in the second variable coincide.

    INPUT:

    - ``pols`` -- list or tuple of polynomials in two variables with
      coefficients in a number field with a fixed embedding in `\\QQbar`

    OUTPUT: a tuple with the roots of the discriminant in `\\QQbar`

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import discrim
        sage: R.<x, y> = QQ[]
        sage: flist = (y^3 + x^3 - 1, 2 * x + y)
        sage: sorted((discrim(flist)))
        [-0.522757958574711?,
         -0.500000000000000? - 0.866025403784439?*I,
         -0.500000000000000? + 0.866025403784439?*I,
         0.2613789792873551? - 0.4527216721561923?*I,
         0.2613789792873551? + 0.4527216721561923?*I,
         1]
    """
@cached_function
def corrected_voronoi_diagram(points):
    """
    Compute a Voronoi diagram of a set of points with rational coordinates.
    The given points are granted to lie one in each bounded region.

    INPUT:

    - ``points`` -- tuple of complex numbers

    OUTPUT:

    A Voronoi diagram constructed from rational approximations of the points,
    with the guarantee that each bounded region contains exactly one of the
    input points.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import corrected_voronoi_diagram
        sage: points = (2, I, 0.000001, 0, 0.000001*I)
        sage: V = corrected_voronoi_diagram(points)
        sage: V
        The Voronoi diagram of 9 points of dimension 2 in the Rational Field
        sage: V.regions()
        {P(-7, 0): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices and 2 rays,
        P(0, -7): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices and 2 rays,
        P(0, 0): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices,
        P(0, 1): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices,
        P(0, 1/1000000): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices,
        P(0, 7): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 3 vertices and 2 rays,
        P(1/1000000, 0): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices,
        P(2, 0): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 5 vertices,
        P(7, 0): A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 2 vertices and 2 rays}
    """
def orient_circuit(circuit, convex: bool = False, precision: int = 53, verbose: bool = False):
    """
    Reverse a circuit if it goes clockwise; otherwise leave it unchanged.

    INPUT:

    - ``circuit`` -- a circuit in the graph of a Voronoi Diagram, given
      by a list of edges

    - ``convex`` -- boolean (default: ``False``); if set to ``True`` a simpler
      computation is made

    - ``precision`` -- bits of precision (default: 53)

    - ``verbose`` -- boolean (default: ``False``); for testing purposes

    OUTPUT:

    The same circuit if it goes counterclockwise, and its reversed otherwise,
    given as the ordered list of vertices with identic extremities.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import orient_circuit
        sage: points = [(-4, 0), (4, 0), (0, 4), (0, -4), (0, 0)]
        sage: V = VoronoiDiagram(points)
        sage: E = Graph()
        sage: for reg  in V.regions().values():
        ....:     if reg.rays() or reg.lines():
        ....:         E  = E.union(reg.vertex_graph())
        sage: E.vertices(sort=True)
        [A vertex at (-2, -2),
         A vertex at (-2, 2),
         A vertex at (2, -2),
         A vertex at (2, 2)]
        sage: cir = E.eulerian_circuit()
        sage: cir
        [(A vertex at (-2, -2), A vertex at (2, -2), None),
         (A vertex at (2, -2), A vertex at (2, 2), None),
         (A vertex at (2, 2), A vertex at (-2, 2), None),
         (A vertex at (-2, 2), A vertex at (-2, -2), None)]
        sage: cir_oriented = orient_circuit(cir); cir_oriented
        (A vertex at (-2, -2), A vertex at (2, -2), A vertex at (2, 2),
         A vertex at (-2, 2), A vertex at (-2, -2))
        sage: cirinv = list(reversed([(c[1],c[0],c[2]) for c in cir]))
        sage: cirinv
        [(A vertex at (-2, -2), A vertex at (-2, 2), None),
         (A vertex at (-2, 2), A vertex at (2, 2), None),
         (A vertex at (2, 2), A vertex at (2, -2), None),
         (A vertex at (2, -2), A vertex at (-2, -2), None)]
        sage: orient_circuit(cirinv) == cir_oriented
        True
        sage: cir_oriented == orient_circuit(cir, convex=True)
        True
        sage: P0=[(1,1/2),(0,1),(1,1)]; P1=[(0,3/2),(-1,0)]
        sage: Q=Polyhedron(P0).vertices()
        sage: Q = [Q[2], Q[0], Q[1]] + [_ for _ in reversed(Polyhedron(P1).vertices())]
        sage: Q
        [A vertex at (1, 1/2), A vertex at (0, 1), A vertex at (1, 1),
         A vertex at (0, 3/2), A vertex at (-1, 0)]
        sage: E = Graph()
        sage: for v, w in zip(Q, Q[1:] + [Q[0]]):
        ....:   E.add_edge((v, w))
        sage: cir = orient_circuit(E.eulerian_circuit(), precision=1, verbose=True)
        2
        sage: cir
        (A vertex at (1, 1/2), A vertex at (0, 1), A vertex at (1, 1),
         A vertex at (0, 3/2), A vertex at (-1, 0), A vertex at (1, 1/2))
    """
def voronoi_cells(V, vertical_lines=...):
    """
    Compute the graph, the boundary graph, a base point, a positive orientation
    of the boundary graph, and the dual graph of a corrected Voronoi diagram.

    INPUT:

    - ``V`` -- a corrected Voronoi diagram

    - ``vertical_lines`` -- frozenset (default: ``frozenset()``); indices of the
      vertical lines

    OUTPUT:

    - ``G`` -- the graph of the 1-skeleton of ``V``
    - ``E`` -- the subgraph of the boundary
    - ``p`` -- a vertex in ``E``
    - ``EC`` -- list of vertices (representing a counterclockwise orientation
      of ``E``) with identical first and last elements)
    - ``DG`` -- the dual graph of ``V``, where the vertices are labelled
      by the compact regions of ``V`` and the edges by their dual edges
    - ``vertical_regions`` -- dictionary for the regions associated
      with vertical lines

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import corrected_voronoi_diagram, voronoi_cells
        sage: points = (2, I, 0.000001, 0, 0.000001*I)
        sage: V = corrected_voronoi_diagram(points)
        sage: G, E, p, EC, DG, VR = voronoi_cells(V, vertical_lines=frozenset((1,)))
        sage: Gv = G.vertices(sort=True)
        sage: Ge = G.edges(sort=True)
        sage: len(Gv), len(Ge)
        (12, 16)
        sage: Ev = E.vertices(sort=True); Ev
        [A vertex at (-4, 4),
        A vertex at (-49000001/14000000, 1000001/2000000),
        A vertex at (-7/2, -7/2),
        A vertex at (-7/2, 1/2000000),
        A vertex at (1/2000000, -7/2),
        A vertex at (2000001/2000000, -24500001/7000000),
        A vertex at (11/4, 4),
        A vertex at (9/2, -9/2),
        A vertex at (9/2, 9/2)]
        sage: Ev.index(p)
        7
        sage: EC
        (A vertex at (9/2, -9/2),
        A vertex at (9/2, 9/2),
        A vertex at (11/4, 4),
        A vertex at (-4, 4),
        A vertex at (-49000001/14000000, 1000001/2000000),
        A vertex at (-7/2, 1/2000000),
        A vertex at (-7/2, -7/2),
        A vertex at (1/2000000, -7/2),
        A vertex at (2000001/2000000, -24500001/7000000),
        A vertex at (9/2, -9/2))
        sage: len(DG.vertices(sort=True)), len(DG.edges(sort=True))
        (5, 7)
        sage: edg = DG.edges(sort=True)[0]; edg
        ((0,
          (A vertex at (9/2, -9/2),
           A vertex at (9/2, 9/2),
           A vertex at (11/4, 4),
           A vertex at (2000001/2000000, 500001/1000000),
           A vertex at (2000001/2000000, -24500001/7000000),
           A vertex at (9/2, -9/2))),
         (1,
          (A vertex at (-49000001/14000000, 1000001/2000000),
           A vertex at (1000001/2000000, 1000001/2000000),
           A vertex at (2000001/2000000, 500001/1000000),
           A vertex at (11/4, 4),
           A vertex at (-4, 4),
           A vertex at (-49000001/14000000, 1000001/2000000))),
         (A vertex at (2000001/2000000, 500001/1000000), A vertex at (11/4, 4), None))
        sage: edg[-1] in Ge
        True
        sage: VR
        {1: (A vertex at (-49000001/14000000, 1000001/2000000),
             A vertex at (1000001/2000000, 1000001/2000000),
             A vertex at (2000001/2000000, 500001/1000000),
             A vertex at (11/4, 4),
             A vertex at (-4, 4),
             A vertex at (-49000001/14000000, 1000001/2000000))}
    """
def followstrand(f, factors, x0, x1, y0a, prec: int = 53) -> list:
    """
    Return a piecewise linear approximation of the homotopy continuation
    of the root ``y0a`` from ``x0`` to ``x1``.

    INPUT:

    - ``f`` -- an irreducible polynomial in two variables
    - ``factors`` -- list of irreducible polynomials in two variables
    - ``x0`` -- a complex value, where the homotopy starts
    - ``x1`` -- a complex value, where the homotopy ends
    - ``y0a`` -- an approximate solution of the polynomial `F(y) = f(x_0, y)`
    - ``prec`` -- the precision to use

    OUTPUT:

    A list of values `(t, y_{tr}, y_{ti})` such that:

    - ``t`` is a real number between zero and one
    - `f(t \\cdot x_1 + (1-t) \\cdot x_0, y_{tr} + I \\cdot y_{ti})`
      is zero (or a good enough approximation)
    - the piecewise linear path determined by the points has a tubular
      neighborhood  where the actual homotopy continuation path lies, and
      no other root of ``f``, nor any root of the polynomials in ``factors``,
      intersects it.

    EXAMPLES::

        sage: # needs sirocco
        sage: from sage.schemes.curves.zariski_vankampen import followstrand
        sage: R.<x, y> = QQ[]
        sage: f = x^2 + y^3
        sage: x0 = CC(1, 0)
        sage: x1 = CC(1, 0.5)
        sage: followstrand(f, [], x0, x1, -1.0)             # abs tol 1e-15
        [(0.0, -1.0, 0.0),
         (0.7500000000000001, -1.015090921153253, -0.24752813818386948),
         (1.0, -1.026166099551513, -0.32768940253604323)]
        sage: fup = f.subs({y: y - 1/10})
        sage: fdown = f.subs({y: y + 1/10})
        sage: followstrand(f, [fup, fdown], x0, x1, -1.0)   # abs tol 1e-15
        [(0.0, -1.0, 0.0),
         (0.5303300858899107, -1.0076747107983448, -0.17588022709184917),
         (0.7651655429449553, -1.015686131039112, -0.25243563967299404),
         (1.0, -1.026166099551513, -0.3276894025360433)]
    """
def newton(f, x0, i0):
    """
    Return the interval Newton operator.

    INPUT:

    - ``f`` -- a univariate polynomial
    - ``x0`` -- a number
    - ``I0`` -- an interval

    OUTPUT:

    The interval `x_0-\\frac{f(x_0)}{f'(I_0)}`

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import newton
        sage: R.<x> = QQbar[]
        sage: f = x^3 + x
        sage: x0 = 1/10
        sage: I0 = RIF((-1/5,1/5))
        sage: n = newton(f, x0, I0)
        sage: n
        0.0?
        sage: n.real().endpoints()
        (-0.0147727272727274, 0.00982142857142862)
        sage: n.imag().endpoints()
        (0.000000000000000, -0.000000000000000)
    """
def fieldI(field):
    """
    Return the (either double or trivial) extension of a number field which contains ``I``.

    INPUT:

    - ``field`` -- a number field with an embedding in `\\QQbar`

    OUTPUT: the extension ``F`` of ``field`` containing  ``I`` with  an embedding in `\\QQbar`

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import fieldI
        sage: p = QQ[x](x^5 + 2 * x + 1)
        sage: a0 = p.roots(QQbar, multiplicities=False)[0]
        sage: F0.<a> = NumberField(p, embedding=a0)
        sage: fieldI(F0)
        Number Field in prim with defining polynomial
        x^10 + 5*x^8 + 14*x^6 - 2*x^5 - 10*x^4 + 20*x^3 - 11*x^2 - 14*x + 10
        with prim = 0.4863890359345430? + 1.000000000000000?*I
        sage: F0 = CyclotomicField(5)
        sage: fieldI(F0)
        Number Field in prim with defining polynomial
        x^8 - 2*x^7 + 7*x^6 - 10*x^5 + 16*x^4 - 10*x^3 - 2*x^2 + 4*x + 1
        with prim = -0.3090169943749474? + 0.04894348370484643?*I
        sage: fieldI(QuadraticField(3))
        Number Field in prim with defining polynomial x^4 - 4*x^2 + 16
        with prim = -1.732050807568878? + 1.000000000000000?*I
        sage: fieldI(QuadraticField(-3))
        Number Field in prim with defining polynomial x^4 + 8*x^2 + 4
        with prim = 0.?e-18 - 0.732050807568878?*I

    If ``I`` is already in the field, the result is the field itself::

        sage: from sage.schemes.curves.zariski_vankampen import fieldI
        sage: p = QQ[x](x^4 + 1)
        sage: a0 = p.roots(QQbar, multiplicities=False)[0]
        sage: F0.<a> = NumberField(p, embedding=a0)
        sage: F1 = fieldI(F0)
        sage: F0 == F1
        True
        sage: QuadraticField(-1) == fieldI(QuadraticField(-1))
        True
    """
@parallel
def roots_interval(f, x0):
    """
    Find disjoint intervals that isolate the roots of a polynomial for a fixed
    value of the first variable.

    INPUT:

    - ``f`` -- a bivariate squarefree polynomial
    - ``x0`` -- a Gauss rational number corresponding to the first coordinate

    The intervals are taken as big as possible to be able to detect when two
    approximate roots of `f(x_0, y)` correspond to the same exact root, where
    `f` is the product of the polynomials in `flist`.

    The result is given as a dictionary, where the keys are
    approximations to the roots with rational real and imaginary
    parts, and the values are intervals containing them.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import roots_interval, fieldI
        sage: R.<x, y> = QQ[]
        sage: K = fieldI(QQ)
        sage: f = y^3 - x^2
        sage: f = f.change_ring(K)
        sage: ri = roots_interval(f, 1)
        sage: ri
        {-138907099/160396102*I - 1/2: -1.? - 1.?*I,
         138907099/160396102*I - 1/2: -1.? + 1.?*I,
         1: 1.? + 0.?*I}
        sage: [r.endpoints() for r in ri.values()]
        [(0.566987298107781 - 0.433012701892219*I,
          1.43301270189222 + 0.433012701892219*I,
          0.566987298107781 + 0.433012701892219*I,
          1.43301270189222 - 0.433012701892219*I),
         (-0.933012701892219 - 1.29903810567666*I,
          -0.0669872981077806 - 0.433012701892219*I,
          -0.933012701892219 - 0.433012701892219*I,
          -0.0669872981077806 - 1.29903810567666*I),
         (-0.933012701892219 + 0.433012701892219*I,
          -0.0669872981077806 + 1.29903810567666*I,
          -0.933012701892219 + 1.29903810567666*I,
          -0.0669872981077806 + 0.433012701892219*I)]
    """
def roots_interval_cached(f, x0):
    """
    Cached version of :func:`roots_interval`.

    TESTS::

        sage: from sage.schemes.curves.zariski_vankampen import roots_interval, roots_interval_cached, roots_interval_cache, fieldI
        sage: R.<x, y> = QQ[]
        sage: K = fieldI(QQ)
        sage: f = y^3 - x^2
        sage: f = f.change_ring(K)
        sage: (f, 1) in roots_interval_cache
        False
        sage: ri = roots_interval_cached(f, 1)
        sage: ri
        {-138907099/160396102*I - 1/2: -1.? - 1.?*I,
         138907099/160396102*I - 1/2: -1.? + 1.?*I,
         1: 1.? + 0.?*I}
        sage: (f, 1) in roots_interval_cache
        True
    """
def populate_roots_interval_cache(inputs) -> None:
    """
    Call :func:`roots_interval` to the inputs that have not been
    computed previously, and cache them.

    INPUT:

    - ``inputs`` -- list of tuples ``(f, x0)``

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import populate_roots_interval_cache, roots_interval_cache, fieldI
        sage: R.<x,y> = QQ[]
        sage: K=fieldI(QQ)
        sage: f = y^5 - x^2
        sage: f = f.change_ring(K)
        sage: (f, 3) in roots_interval_cache
        False
        sage: populate_roots_interval_cache([(f, 3)])
        sage: (f, 3) in roots_interval_cache
        True
        sage: roots_interval_cache[(f, 3)]
        {-1.255469441943070? - 0.9121519421827974?*I: -2.? - 1.?*I,
         -1.255469441943070? + 0.9121519421827974?*I: -2.? + 1.?*I,
         0.4795466549853897? - 1.475892845355996?*I: 1.? - 2.?*I,
         0.4795466549853897? + 1.475892845355996?*I: 1.? + 2.?*I,
         14421467174121563/9293107134194871: 2.? + 0.?*I}
    """
@parallel
def braid_in_segment(glist, x0, x1, precision={}):
    """
    Return the braid formed by the `y` roots of ``f`` when `x` moves
    from ``x0`` to ``x1``.

    INPUT:

    - ``glist`` -- tuple of polynomials in two variables
    - ``x0`` -- a Gauss rational
    - ``x1`` -- a Gauss rational
    - ``precision`` -- dictionary (default: `{}`) which assigns a number
      precision bits to each element of ``glist``

    OUTPUT: a braid

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import braid_in_segment, fieldI
        sage: R.<x, y> = QQ[]
        sage: K = fieldI(QQ)
        sage: f = x^2 + y^3
        sage: f = f.change_ring(K)
        sage: x0 = 1
        sage: x1 = 1 + I / 2
        sage: braid_in_segment(tuple(_[0] for _ in f.factor()), x0, x1)     # needs sirocco
        s1

    TESTS:

    Check that :issue:`26503` is fixed::

        sage: # needs sage.rings.real_mpfr sage.symbolic
        sage: wp = QQ['t']([1, 1, 1]).roots(QQbar)[0][0]
        sage: Kw.<wp> = NumberField(wp.minpoly(), embedding=wp)
        sage: R.<x, y> = Kw[]
        sage: z = -wp - 1
        sage: f = y * (y + z) * x * (x - 1) * (x - y) * (x + z * y - 1) * (x + z * y + wp)
        sage: from sage.schemes.curves.zariski_vankampen import fieldI, braid_in_segment
        sage: Kw1 = fieldI(Kw)
        sage: g = f.subs({x: x + 2 * y})
        sage: g = g.change_ring(Kw1)
        sage: p1 = QQbar(sqrt(-1/3))
        sage: p1a = CC(p1)
        sage: p1b = QQ(p1a.real()) + I*QQ(p1a.imag())
        sage: p2 = QQbar(1/2 + sqrt(-1/3)/2)
        sage: p2a = CC(p2)
        sage: p2b = QQ(p2a.real()) + I*QQ(p2a.imag())
        sage: glist = tuple([_[0] for _ in g.factor()])
        sage: B = braid_in_segment(glist, p1b, p2b); B              # needs sirocco
        s5*s3^-1
    """
def geometric_basis(G, E, EC0, p, dual_graph, vertical_regions={}) -> list:
    """
    Return a geometric basis, based on a vertex.

    INPUT:

    - ``G`` -- a graph with the bounded edges of a Voronoi Diagram

    - ``E`` -- a subgraph of ``G`` which is a cycle containing the bounded
      edges touching an unbounded region of a Voronoi Diagram

    - ``EC0`` -- a counterclockwise orientation of the vertices of ``E``

    - ``p`` -- a vertex of ``E``

    - ``dual_graph`` -- a dual graph for a plane embedding of ``G`` such that
      ``E`` is the boundary of the non-bounded component of the complement.
      The edges are labelled as the dual edges and the vertices are labelled
      by a tuple whose first element is the an integer for the position and the
      second one is the cyclic ordered list of vertices in the region

    - ``vertical_regions`` -- dictionary (default: `{}`); its keys are
      the vertices of ``dual_graph`` to fix regions associated with
      vertical lines

    OUTPUT: a geometric basis and a dictionary

    The geometric basis is formed by a list of sequences of paths. Each path is a
    ist of vertices, that form a closed path in ``G``, based at ``p``, that goes
    to a region, surrounds it, and comes back by the same path it came. The
    concatenation of all these paths is equivalent to ``E``.

    The dictionary associates to each vertical line the index of the generator
    of the geometric basis associated to it.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import geometric_basis, corrected_voronoi_diagram, voronoi_cells
        sage: points = (0, -1, I, 1, -I)
        sage: V = corrected_voronoi_diagram(points)
        sage: G, E, p, EC, DG, VR = voronoi_cells(V, vertical_lines=frozenset((0 .. 4)))
        sage: gb, vd = geometric_basis(G, E, EC, p, DG, vertical_regions=VR)
        sage: gb
        [[A vertex at (5/2, -5/2), A vertex at (5/2, 5/2), A vertex at (-5/2, 5/2),
          A vertex at (-1/2, 1/2), A vertex at (-1/2, -1/2), A vertex at (1/2, -1/2),
          A vertex at (1/2, 1/2), A vertex at (-1/2, 1/2), A vertex at (-5/2, 5/2),
          A vertex at (5/2, 5/2), A vertex at (5/2, -5/2)],
         [A vertex at (5/2, -5/2), A vertex at (5/2, 5/2), A vertex at (-5/2, 5/2),
          A vertex at (-1/2, 1/2), A vertex at (1/2, 1/2), A vertex at (5/2, 5/2),
          A vertex at (5/2, -5/2)],
         [A vertex at (5/2, -5/2), A vertex at (5/2, 5/2), A vertex at (1/2, 1/2),
          A vertex at (1/2, -1/2), A vertex at (5/2, -5/2)], [A vertex at (5/2, -5/2),
          A vertex at (1/2, -1/2), A vertex at (-1/2, -1/2), A vertex at (-1/2, 1/2),
          A vertex at (-5/2, 5/2), A vertex at (-5/2, -5/2), A vertex at (-1/2, -1/2),
          A vertex at (1/2, -1/2), A vertex at (5/2, -5/2)],
         [A vertex at (5/2, -5/2), A vertex at (1/2, -1/2), A vertex at (-1/2, -1/2),
          A vertex at (-5/2, -5/2), A vertex at (5/2, -5/2)]]
        sage: vd
        {0: 0, 1: 3, 2: 1, 3: 2, 4: 4}
    """
def vertical_lines_in_braidmon(pols) -> list:
    """
    Return the vertical lines in ``pols``, unless
    one of the other components has a vertical asymptote.

    INPUT:

    - ``pols`` -- a  list of polynomials with two variables whose
      product equals ``f``

    OUTPUT:

    A list with the indices of the vertical lines in ``flist`` if there is
    no other component with vertical asymptote; otherwise it returns an empty
    list.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import vertical_lines_in_braidmon
        sage: R.<x, y> = QQ[]
        sage: flist = [x^2 - y^3, x, x + 3 * y - 5, 1 - x]
        sage: vertical_lines_in_braidmon(flist)
        [1, 3]
        sage: flist += [x * y - 1]
        sage: vertical_lines_in_braidmon(flist)
        []
        sage: vertical_lines_in_braidmon([])
        []
    """
def strand_components(f, pols, p1):
    """
    Compute only the assignment from strands to elements of ``flist``.

    INPUT:

    - ``f`` -- a  reduced polynomial with two variables, over a number field
      with an embedding in the complex numbers

    - ``pols`` -- a  list of polynomials with two variables whose
      product equals ``f``

    - ``p1`` -- a Gauss rational

    OUTPUT:

    - A list and a dictionary.  The first one is an ordered list of pairs
      consisting of ``(z,i)`` where ``z`` is a root of ``f(p_1,y)``
      and `i` is the position of the polynomial in the list whose root
      is ``z``. The second one attaches a number `i` (strand) to a
      number `j` (a polynomial in the list).

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import strand_components
        sage: R.<x, y> = QQ[]
        sage: flist = [x^2 - y^3, x + 3 * y - 5]
        sage: strand_components(prod(flist), flist, 1)
        ([(-0.500000000000000? - 0.866025403784439?*I, 0),
          (-0.500000000000000? + 0.866025403784439?*I, 0),
          (1, 0), (1.333333333333334?, 1)], {0: 0, 1: 0, 2: 0, 3: 1})
    """
def braid_monodromy(f, arrangement=(), vertical: bool = False):
    """
    Compute the braid monodromy of a projection of the curve defined by
    a polynomial.

    INPUT:

    - ``f`` -- a polynomial with two variables, over a number field
      with an embedding in the complex numbers

    - ``arrangement`` -- tuple (default: ``()``); an optional tuple
      of polynomials whose product equals ``f``

    - ``vertical`` -- boolean (default: ``False``); if set to ``True``,
      ``arrangements`` contains more than one polynomial, some of them
      are of degree `1` in `x` and degree `0` in `y`, and none of
      the other components have vertical asymptotes, then these
      components are marked as *vertical* and not used for the computation
      of the braid monodromy. The other ones are marked as *horizontal*. If
      a vertical component does not pass through a singular points of the
      projection of the horizontal components a trivial braid is added
      to the list.

    OUTPUT:

    - A list of braids, images by the braid monodromy of a geometric
      basis of the complement of the discriminant of `f` in `\\CC`.

    - A dictionary: ``i``, index of a strand is sent to the index of
      the corresponding factor in ``arrangement``.

    - Another dictionary ``dv``, only relevant if ``vertical`` is ``True``.
      If  ``j`` is the index
      of a braid corresponding to a vertical line with index ``i``
      in ``arrangement``, then ``dv[j] = i``.

    - A nonnegative integer: the number of strands of the braids,
      only necessary if the list of braids is empty.

    .. NOTE::

        The projection over the `x` axis is used if there are no vertical
        asymptotes. Otherwise, a linear change of variables is done to fall
        into the previous case except if the only vertical asymptotes are lines
        and ``vertical=True``.

    EXAMPLES::

        sage: # needs sirocco
        sage: from sage.schemes.curves.zariski_vankampen import braid_monodromy
        sage: R.<x, y> = QQ[]
        sage: f = (x^2 - y^3) * (x + 3*y - 5)
        sage: bm = braid_monodromy(f); bm
        ([s1*s0*(s1*s2)^2*s0*s2^2*s0^-1*(s2^-1*s1^-1)^2*s0^-1*s1^-1,
          s1*s0*(s1*s2)^2*(s0*s2^-1*s1*s2*s1*s2^-1)^2*(s2^-1*s1^-1)^2*s0^-1*s1^-1,
          s1*s0*(s1*s2)^2*s2*s1^-1*s2^-1*s1^-1*s0^-1*s1^-1,
          s1*s0*s2*s0^-1*s2*s1^-1], {0: 0, 1: 0, 2: 0, 3: 0}, {}, 4)
        sage: flist = (x^2 - y^3, x + 3*y - 5)
        sage: bm1 = braid_monodromy(f, arrangement=flist)
        sage: bm1[0] == bm[0]
        True
        sage: bm1[1]
        {0: 0, 1: 1, 2: 0, 3: 0}
        sage: braid_monodromy(R(1))
        ([], {}, {}, 0)
        sage: braid_monodromy(x*y^2 - 1)
        ([s0*s1*s0^-1*s1*s0*s1^-1*s0^-1, s0*s1*s0^-1, s0], {0: 0, 1: 0, 2: 0}, {}, 3)
        sage: L = [x, y, x - 1, x -y]
        sage: braid_monodromy(prod(L), arrangement=L, vertical=True)
        ([s^2, 1], {0: 1, 1: 3}, {0: 0, 1: 2}, 2)
    """
def conjugate_positive_form(braid):
    """
    For a ``braid`` which is conjugate to a product of *disjoint* positive
    braids a list of such decompositions is given.

    INPUT:

    - ``braid`` -- a braid `\\sigma`

    OUTPUT:

    A list of `r` lists. Each such list is another list with two elements, a
    positive braid `\\alpha_i` and a list of permutation braids
    `\\gamma_{1}^{i},\\dots,\\gamma_{n_i}^{i}` such that if
    `\\gamma_i=\\prod_{j=1}^{n_i} \\gamma_j^i` then the braids
    `\\tau_i=\\gamma_i\\alpha_i\\gamma_i^{-1}` pairwise commute
    and `\\alpha=\\prod_{i=1}^{r} \\tau_i`.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import conjugate_positive_form
        sage: B = BraidGroup(4)
        sage: t = B((1, 3, 2, -3, 1, 1))
        sage: cpf = conjugate_positive_form(t); cpf
        [[(s0*s1)^2, [s0*s2*s1*s0]]]
        sage: t == prod(prod(b) * a / prod(b) for a, b in cpf)
        True
        sage: B = BraidGroup(5)
        sage: t = B((1, 2, 3, 4, -1, -2, 3, 3, 2, -4))
        sage: L = conjugate_positive_form(t); L
        [[s0^2, [s0*s1*s2*s1*s3*s2*s1*s0]], [s3*s2, [s0*s1*s2*s1*s3*s2*s1*s0]]]
        sage: t == prod(prod(b) * a / prod(b) for a, b in L)
        True
        sage: s1 = B.gen(1)^3
        sage: conjugate_positive_form(s1)
        [[s1^3, []]]
    """
@parallel
def conjugate_positive_form_p(braid): ...
def braid2rels(L):
    """
    Return a minimal set of relations of the group
    ``F / [(b * F([j])) / F([j]) for j in (1..d)]`` where ``F = FreeGroup(d)``
    and ``b`` is a conjugate of a positive braid . One starts from the
    non-trivial relations determined by the positive braid and transform
    them in relations determined by ``b``.

    INPUT:

    - ``L`` -- tuple whose first element is a positive braid and the second
      element is a list of permutation braids

    OUTPUT:

    A list of Tietze words for a minimal set of relations of
    ``F / [(g * b) / g for g in F.gens()]``.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import braid2rels
        sage: B.<s0, s1, s2> = BraidGroup(4)
        sage: L = ((s1*s0)^2, [s2])
        sage: braid2rels(L)
        [(4, 1, -2, -1), (2, -4, -2, 1)]
    """
@parallel
def braid2rels_p(L): ...
@parallel
def relation(x, b): ...
def fundamental_group_from_braid_mon(bm, degree=None, simplified: bool = True, projective: bool = False, puiseux: bool = True, vertical=[]):
    """
    Return a presentation of the fundamental group computed from
    a braid monodromy.

    INPUT:

    - ``bm`` -- list of braids

    - ``degree`` -- integer (default: ``None``); only needed if the braid
      monodromy is an empty list

    - ``simplified`` -- boolean (default: ``True``); if set to ``True`` the
      presentation will be simplified (see below)

    - ``projective`` -- boolean (default: ``False``); if set to ``True``,
      the fundamental group of the complement of the projective completion
      of the curve will be computed, otherwise, the fundamental group of
      the complement in the affine plane will be computed

    - ``puiseux`` -- boolean (default: ``True``); if set to ``True``
      a presentation of the fundamental group with the homotopy type
      of the complement of the affine curve will be computed, adding
      one relation if ``projective`` is set to ``True``.

    - ``vertical`` -- list of integers (default: ``[]``); the indices in
      ``[0 .. r - 1]`` of the braids that surround a vertical line

    If ``projective`` is ``False`` and ``puiseux`` is
    ``True``, a Zariski-VanKampen presentation is returned.

    OUTPUT:

    A presentation of the fundamental group of the complement of the
    union of the curve with some vertical lines from its braid monodromy.

    EXAMPLES::

        sage: from sage.schemes.curves.zariski_vankampen import fundamental_group_from_braid_mon
        sage: B.<s0, s1, s2> = BraidGroup(4)
        sage: bm = [s1*s2*s0*s1*s0^-1*s1^-1*s0^-1,
        ....:       s0*s1^2*s0*s2*s1*(s0^-1*s1^-1)^2*s0^-1,
        ....:       (s0*s1)^2]
        sage: g = fundamental_group_from_braid_mon(bm, projective=True)        # needs sirocco
        sage: g.sorted_presentation()                                          # needs sirocco
        Finitely presented group
        < x0, x1 | x1^-2*x0^-2, x1^-1*(x0^-1*x1)^2*x0 >
        sage: print(g.order(), g.abelian_invariants())                         # needs sirocco
        12 (4,)
        sage: B2 = BraidGroup(2)
        sage: bm = [B2(3 * [1])]
        sage: g = fundamental_group_from_braid_mon(bm, vertical=[0]); g         # needs sirocco
        Finitely presented group
        < x0, x1, x2 | x2*x0*x1*x2^-1*x1^-1*x0^-1,
                       x2*x0*x1*x0*x1^-1*x0^-1*x2^-1*x1^-1 >
        sage: fundamental_group_from_braid_mon([]) is None                      # needs sirocco
        True
        sage: fundamental_group_from_braid_mon([], degree=2)                    # needs sirocco
        Finitely presented group < x0, x1 |  >
        sage: fundamental_group_from_braid_mon([SymmetricGroup(1).one()])       # needs sirocco
        Finitely presented group < x |  >
    """
def fundamental_group(f, simplified: bool = True, projective: bool = False, puiseux: bool = True):
    """
    Return a presentation of the fundamental group of the complement of
    the algebraic set defined by the polynomial ``f``.

    INPUT:

    - ``f`` -- a polynomial in two variables, with coefficients in either
      the rationals or a number field with a fixed embedding in `\\QQbar`

    - ``simplified`` -- boolean (default: ``True``); if set to ``True`` the
      presentation will be simplified (see below)

    - ``projective`` -- boolean (default: ``False``); if set to ``True``,
      the fundamental group of the complement of the projective completion
      of the curve will be computed, otherwise, the fundamental group of
      the complement in the affine plane will be computed

    - ``puiseux`` -- boolean (default: ``True``); if set to ``True``,
      a presentation of the fundamental group with the homotopy type
      of the complement of the affine curve is computed. If the Euler
      characteristic does not match, the homotopy type is obtained
      with a wedge of 2-spheres. One relation is added if ``projective``
      is set to ``True``.

    If ``projective`` is ``False`` and ``puiseux`` is
    ``True``, a Zariski-VanKampen presentation is returned.

    OUTPUT:

    A presentation of the fundamental group of the complement of the
    curve defined by ``f``.

    EXAMPLES::

        sage: # needs sirocco
        sage: from sage.schemes.curves.zariski_vankampen import fundamental_group, braid_monodromy
        sage: R.<x, y> = QQ[]
        sage: f = x^2 + y^3
        sage: fundamental_group(f).sorted_presentation()
        Finitely presented group < x0, x1 | x1^-1*x0^-1*x1^-1*x0*x1*x0 >
        sage: fundamental_group(f, simplified=False, puiseux=False).sorted_presentation()
        Finitely presented group < x0, x1, x2 | x2^-1*x1^-1*x0*x1,
                                                x2^-1*x0*x1*x0^-1,
                                                x1^-1*x0^-1*x1^-1*x0*x1*x0 >
        sage: fundamental_group(f, projective=True)
        Finitely presented group < x0 | x0^3 >
        sage: fundamental_group(f).sorted_presentation()
        Finitely presented group < x0, x1 | x1^-1*x0^-1*x1^-1*x0*x1*x0 >

    ::

        sage: # needs sirocco
        sage: from sage.schemes.curves.zariski_vankampen import fundamental_group
        sage: R.<x, y> = QQ[]
        sage: f = y^3 + x^3
        sage: fundamental_group(f).sorted_presentation()
        Finitely presented group < x0, x1, x2 | x2^-1*x1^-1*x0^-1*x2*x0*x1,
                                                x2^-1*x1^-1*x2*x0*x1*x0^-1 >

    It is also possible to have coefficients in a number field with a
    fixed embedding in `\\QQbar`::

        sage: from sage.schemes.curves.zariski_vankampen import fundamental_group
        sage: zeta = QQbar['x']('x^2 + x+ 1').roots(multiplicities=False)[0]
        sage: zeta
        -0.50000000000000000? - 0.866025403784439?*I
        sage: F = NumberField(zeta.minpoly(), 'zeta', embedding=zeta)
        sage: F.inject_variables()
        Defining zeta
        sage: R.<x, y> = F[]
        sage: f = y^3 + x^3 + zeta * x + 1
        sage: fundamental_group(f)                                  # needs sirocco
        Finitely presented group < x0 |  >

    We compute the fundamental group of the complement of a
    quartic using the ``puiseux`` option::

        sage: # optional - sirocco
        sage: from sage.schemes.curves.zariski_vankampen import fundamental_group
        sage: R.<x, y> = QQ[]
        sage: f = x^2 * y^2 + x^2 + y^2 - 2 * x * y  * (x + y + 1)
        sage: g = fundamental_group(f); g.sorted_presentation()
        Finitely presented group < x0, x1 | x1^-2*x0^2, (x1^-1*x0)^3 >
        sage: g = fundamental_group(f, projective=True)
        sage: g.order(), g.abelian_invariants()
        (12, (4,))
        sage: fundamental_group(y * (y - 1))
        Finitely presented group < x0, x1 |  >
    """
def fundamental_group_arrangement(flist, simplified: bool = True, projective: bool = False, puiseux: bool = True, vertical: bool = False, braid_data=None):
    """
    Compute the fundamental group of the complement of a curve
    defined by a list of polynomials with the extra information
    about the correspondence of the generators
    and meridians of the elements of the list.

    INPUT:

    - ``flist`` -- a  tuple of polynomial with two variables, over a number
      field with an embedding in the complex numbers

    - ``simplified`` -- boolean (default: ``True``); if set to ``True`` the
      presentation will be simplified (see below)

    - ``projective`` -- boolean (default: ``False``); if set to ``True``,
      the fundamental group of the complement of the projective completion
      of the curve will be computed, otherwise, the fundamental group of
      the complement in the affine plane will be computed

    - ``puiseux`` -- boolean (default: ``True``); if set to ``True``
      a presentation of the fundamental group with the homotopy type
      of the complement of the affine curve will be computed, adding
      one relation if ``projective`` is set to ``True``.

    - ``vertical`` -- boolean (default: ``False``); if set to ``True``,
      whenever no curve has vertical asymptotes the computation of braid
      monodromy is simpler if some lines are vertical

    - ``braid_data`` -- tuple (default: ``None``); if it is not the default
      it is the output of ``fundamental_group_from_braid_mon`` previously
      computed

    OUTPUT:

    - A list of braids. The braids correspond to paths based in the same point;
      each of this paths is the conjugated of a loop around one of the points
      in the discriminant of the projection of ``f``.

    - A dictionary attaching to ``j`` a tuple a list of elements
      of the group  which are meridians of the curve in position ``j``.
      If ``projective`` is ``False`` and the `y`-degree of the horizontal
      components coincide with the total degree, another key is added
      to give a meridian of the line at infinity.

    EXAMPLES::

        sage: # needs sirocco
        sage: from sage.schemes.curves.zariski_vankampen import braid_monodromy
        sage: from sage.schemes.curves.zariski_vankampen import fundamental_group_arrangement
        sage: R.<x, y> = QQ[]
        sage: flist = [x^2 - y^3, x + 3 * y - 5]
        sage: g, dic = fundamental_group_arrangement(flist)
        sage: g.sorted_presentation()
        Finitely presented group
         < x0, x1, x2 | x2^-1*x1^-1*x2*x1, x2^-1*x0^-1*x2^-1*x0*x2*x0,
                        x1^-1*x0^-1*x1*x0 >
        sage: dic
        {0: [x0, x2], 1: [x1], 2: [x0^-1*x2^-1*x1^-1*x0^-1]}
        sage: g, dic = fundamental_group_arrangement(flist, simplified=False, puiseux=False)
        sage: g.sorted_presentation(), dic
        (Finitely presented group
         < x0, x1, x2, x3 | 1, 1, 1, 1, 1, 1, 1,
                            x3^-1*x2^-1*x1^-1*x2*x3*x2^-1*x1*x2,
                            x3^-1*x2^-1*x1^-1*x0^-1*x1*x2*x3*x2,
                            x3^-1*x2^-1*x1^-1*x0^-1*x1*x2*x1^-1*x0*x1*x2,
                            x3^-1*x2^-1*x1^-1*x2*x3*x2^-1*x1*x2,
                            x3^-1*x1^-1*x0*x1,
                            x1^-1*x0^-1*x1*x0, x1^-1*x0^-1*x1*x0,
                            x1^-1*x0^-1*x1*x0, x1^-1*x0^-1*x1*x0 >,
         {0: [x0, x2, x3], 1: [x1], 2: [x3^-1*x2^-1*x1^-1*x0^-1]})
        sage: fundamental_group_arrangement(flist, projective=True)
        (Finitely presented group < x |  >, {0: [x], 1: [x^-3]})
        sage: fundamental_group_arrangement([])
        (Finitely presented group <  |  >, {})
        sage: g, dic = fundamental_group_arrangement([x * y])
        sage: g.sorted_presentation(), dic
        (Finitely presented group < x0, x1 | x1^-1*x0^-1*x1*x0 >,
         {0: [x0, x1], 1: [x1^-1*x0^-1]})
        sage: fundamental_group_arrangement([y + x^2])
        (Finitely presented group < x |  >, {0: [x]})
        sage: fundamental_group_arrangement([y^2 + x], projective=True)
        (Finitely presented group < x | x^2 >, {0: [x]})
        sage: L = [x, y, x - 1, x -y]
        sage: G, dic =fundamental_group_arrangement(L)
        sage: G.sorted_presentation()
        Finitely presented group
        < x0, x1, x2, x3 | x3^-1*x2^-1*x3*x2, x3^-1*x1^-1*x0^-1*x1*x3*x0,
                           x3^-1*x1^-1*x0^-1*x3*x0*x1, x2^-1*x0^-1*x2*x0 >
        sage: dic
        {0: [x1], 1: [x3], 2: [x2], 3: [x0], 4: [x3^-1*x2^-1*x1^-1*x0^-1]}
        sage: fundamental_group_arrangement(L, vertical=True)
        (Finitely presented group
         < x0, x1, x2, x3 | x3*x0*x3^-1*x0^-1, x3*x1*x3^-1*x1^-1,
                            x1*x2*x0*x2^-1*x1^-1*x0^-1,
                            x1*x2*x0*x1^-1*x0^-1*x2^-1 >,
         {0: [x2], 1: [x0], 2: [x3], 3: [x1], 4: [x3^-1*x2^-1*x1^-1*x0^-1]})
    """
