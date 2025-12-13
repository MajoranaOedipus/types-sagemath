from .base6 import Polyhedron_base6 as Polyhedron_base6
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class Polyhedron_base7(Polyhedron_base6):
    """
    Methods related to triangulation and volume.

    TESTS::

        sage: # needs sage.combinat
        sage: from sage.geometry.polyhedron.base7 import Polyhedron_base7
        sage: P = polytopes.associahedron(['A', 3])
        sage: Polyhedron_base7.centroid(P)
        (81/632, 36/79, 81/632)
        sage: Polyhedron_base7.triangulate(P)
        (<0,1,2,13>, <0,1,7,13>, <0,2,5,13>, <0,6,7,12>, <0,6,8,13>,
         <0,6,12,13>, <0,7,12,13>, <1,2,7,12>, <1,2,12,13>, <1,7,12,13>,
         <2,3,7,12>, <2,3,12,13>, <3,4,7,12>, <3,11,12,13>, <6,8,9,12>,
         <6,8,12,13>, <6,9,10,12>, <8,9,12,13>)
        sage: Polyhedron_base7.volume(P, measure='induced')
        79/3
    """
    def centroid(self, engine: str = 'auto', **kwds):
        """
        Return the center of the mass of the polytope.

        The mass is taken with respect to the induced Lebesgue measure,
        see :meth:`volume`.

        If the polyhedron is not compact, a :exc:`NotImplementedError` is
        raised.

        INPUT:

        - ``engine`` -- either 'auto' (default), 'internal',
          'TOPCOM', or 'normaliz'.  The 'internal' and 'TOPCOM' instruct
          this package to always use its own triangulation algorithms
          or TOPCOM's algorithms, respectively. By default ('auto'),
          TOPCOM is used if it is available and internal routines otherwise.

        - ``**kwds`` -- keyword arguments that are passed to the
          triangulation engine (see :meth:`triangulate`)

        OUTPUT: the centroid as vector

        ALGORITHM:

        We triangulate the polytope and find the barycenter of the simplices.
        We add the individual barycenters weighted by the fraction of the total
        mass.

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: P.centroid()
            (1/4, 0, 0)

            sage: P = polytopes.associahedron(['A', 2])                                 # needs sage.combinat
            sage: P.centroid()                                                          # needs sage.combinat
            (2/21, 2/21)

            sage: P = polytopes.permutahedron(4, backend='normaliz')    # optional - pynormaliz
            sage: P.centroid()                                          # optional - pynormaliz
            (5/2, 5/2, 5/2, 5/2)

        The method is not implemented for unbounded polyhedra::

            sage: P = Polyhedron(vertices=[(0, 0)], rays=[(1, 0), (0, 1)])
            sage: P.centroid()
            Traceback (most recent call last):
            ...
            NotImplementedError: the polyhedron is not compact

        The centroid of an empty polyhedron is not defined::

            sage: Polyhedron().centroid()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero

        TESTS::

            sage: Polyhedron(vertices=[[0,1]]).centroid()
            (0, 1)
        """
    def triangulate(self, engine: str = 'auto', connected: bool = True, fine: bool = False, regular=None, star=None):
        """
        Return a triangulation of the polytope.

        INPUT:

        - ``engine`` -- either 'auto' (default), 'internal',
          'TOPCOM', or 'normaliz'.  The 'internal' and 'TOPCOM' instruct
          this package to always use its own triangulation algorithms
          or TOPCOM's algorithms, respectively. By default ('auto'),
          TOPCOM is used if it is available and internal routines otherwise.

        The remaining keyword parameters are passed through to the
        :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`
        constructor:

        - ``connected`` -- boolean (default: ``True``); whether the
          triangulations should be connected to the regular
          triangulations via bistellar flips. These are much easier to
          compute than all triangulations.

        - ``fine`` -- boolean (default: ``False``); whether the
          triangulations must be fine, that is, make use of all points
          of the configuration

        - ``regular`` -- boolean or ``None`` (default:
          ``None``); whether the triangulations must be regular. A
          regular triangulation is one that is induced by a
          piecewise-linear convex support function. In other words,
          the shadows of the faces of a polyhedron in one higher
          dimension.

          * ``True``: Only regular triangulations.

          * ``False``: Only non-regular triangulations.

          * ``None`` (default): Both kinds of triangulation.

        - ``star`` -- either ``None`` (default) or a point. Whether
          the triangulations must be star. A triangulation is star if
          all maximal simplices contain a common point. The central
          point can be specified by its index (an integer) in the
          given points or by its coordinates (anything iterable.)

        OUTPUT:

        A triangulation of the convex hull of the vertices as a
        :class:`~sage.geometry.triangulation.element.Triangulation`. The
        indices in the triangulation correspond to the
        :meth:`~sage.geometry.polyhedron.base0.Polyhedron_base0.Vrepresentation` objects.

        EXAMPLES::

            sage: cube = polytopes.hypercube(3)
            sage: triangulation = cube.triangulate(
            ....:    engine='internal')  # to make doctest independent of TOPCOM
            sage: triangulation
            (<0,1,2,7>, <0,1,5,7>, <0,2,3,7>, <0,3,4,7>, <0,4,5,7>, <1,5,6,7>)
            sage: simplex_indices = triangulation[0]; simplex_indices
            (0, 1, 2, 7)
            sage: simplex_vertices = [cube.Vrepresentation(i) for i in simplex_indices]
            sage: simplex_vertices
            [A vertex at (1, -1, -1),
             A vertex at (1, 1, -1),
             A vertex at (1, 1, 1),
             A vertex at (-1, 1, 1)]
            sage: Polyhedron(simplex_vertices)
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices

        It is possible to use ``'normaliz'`` as an engine. For this, the
        polyhedron should have the backend set to normaliz::

            sage: P = Polyhedron(vertices=[[0,0,1], [1,0,1],            # optional - pynormaliz
            ....:                          [0,1,1], [1,1,1]],
            ....:                backend='normaliz')
            sage: P.triangulate(engine='normaliz')                      # optional - pynormaliz
            (<0,1,2>, <1,2,3>)

            sage: P = Polyhedron(vertices=[[0,0,1], [1,0,1],
            ....:                          [0,1,1], [1,1,1]])
            sage: P.triangulate(engine='normaliz')
            Traceback (most recent call last):
            ...
            TypeError: the polyhedron's backend should be 'normaliz'

        The normaliz engine can triangulate pointed cones::

            sage: # optional - pynormaliz
            sage: C1 = Polyhedron(rays=[[0,0,1], [1,0,1],
            ....:                       [0,1,1], [1,1,1]],
            ....:                 backend='normaliz')
            sage: C1.triangulate(engine='normaliz')
            (<0,1,2>, <1,2,3>)
            sage: C2 = Polyhedron(rays=[[1,0,1], [0,0,1],
            ....:                       [0,1,1], [1,1,10/9]],
            ....:                 backend='normaliz')
            sage: C2.triangulate(engine='normaliz')
            (<0,1,2>, <1,2,3>)

        They can also be affine cones::

            sage: K = Polyhedron(vertices=[[1,1,1]],                    # optional - pynormaliz
            ....:                rays=[[1,0,0], [0,1,0], [1,1,-1], [1,1,1]],
            ....:                backend='normaliz')
            sage: K.triangulate(engine='normaliz')                      # optional - pynormaliz
            (<0,1,2>, <0,1,3>)
        """
    def volume(self, measure: str = 'ambient', engine: str = 'auto', **kwds):
        """
        Return the volume of the polytope.

        INPUT:

        - ``measure`` -- string. The measure to use. Allowed values are:

          * ``ambient`` (default): Lebesgue measure of ambient space (volume)
          * ``induced``: Lebesgue measure of the affine hull (relative volume)
          * ``induced_rational``: Scaling of the Lebesgue measure for rational
            polytopes, such that the unit hypercube has volume 1
          * ``induced_lattice``: Scaling of the Lebesgue measure, such that the
            volume of the hypercube is factorial(n)

        - ``engine`` -- string. The backend to use. Allowed values are:

          * ``'auto'`` (default): choose engine according to measure
          * ``'internal'``: see :meth:`triangulate`
          * ``'TOPCOM'``: see :meth:`triangulate`
          * ``'lrs'``: use David Avis's lrs program (optional)
          * ``'latte'``: use LattE integrale program (optional)
          * ``'normaliz'``: use Normaliz program (optional)

        - ``**kwds`` -- keyword arguments that are passed to the
          triangulation engine

        OUTPUT: the volume of the polytope

        EXAMPLES::

            sage: polytopes.hypercube(3).volume()
            8
            sage: (polytopes.hypercube(3)*2).volume()
            64
            sage: polytopes.twenty_four_cell().volume()
            2

        Volume of the same polytopes, using the optional package lrslib
        (which requires a rational polytope)::

            sage: I3 = polytopes.hypercube(3)
            sage: I3.volume(engine='lrs')                               # optional - lrslib
            8
            sage: C24 = polytopes.twenty_four_cell()
            sage: C24.volume(engine='lrs')                              # optional - lrslib
            2

        If the base ring is exact, the answer is exact::

            sage: P5 = polytopes.regular_polygon(5)                                     # needs sage.rings.number_field
            sage: P5.volume()                                                           # needs sage.rings.number_field
            2.377641290737884?

            sage: polytopes.icosahedron().volume()                                      # needs sage.groups sage.rings.number_field
            5/12*sqrt5 + 5/4
            sage: numerical_approx(_)  # abs tol 1e9                                    # needs sage.groups sage.rings.number_field
            2.18169499062491

        When considering lower-dimensional polytopes, we can ask for the
        ambient (full-dimensional), the induced measure (of the affine
        hull) or, in the case of lattice polytopes, for the induced rational measure.
        This is controlled by the parameter ``measure``. Different engines
        may have different ideas on the definition of volume of a
        lower-dimensional object::

            sage: P = Polyhedron([[0, 0], [1, 1]])
            sage: P.volume()
            0
            sage: P.volume(measure='induced')                                           # needs sage.rings.number_field
            1.414213562373095?
            sage: P.volume(measure='induced_rational')                  # optional - latte_int
            1

            sage: # needs sage.rings.number_field
            sage: S = polytopes.regular_polygon(6); S
            A 2-dimensional polyhedron in AA^2 defined as the convex hull of 6 vertices
            sage: edge = S.faces(1)[4].as_polyhedron()
            sage: edge.vertices()
            (A vertex at (0.866025403784439?, 1/2), A vertex at (0, 1))
            sage: edge.volume()
            0
            sage: edge.volume(measure='induced')
            1

            sage: # optional - pynormaliz
            sage: P = Polyhedron(backend='normaliz',
            ....:                vertices=[[1,0,0], [0,0,1],
            ....:                          [-1,1,1], [-1,2,0]])
            sage: P.volume()
            0
            sage: P.volume(measure='induced')                                           # needs sage.rings.number_field
            2.598076211353316?
            sage: P.volume(measure='induced', engine='normaliz')
            2.598076211353316
            sage: P.volume(measure='induced_rational')                  # optional - latte_int
            3/2
            sage: P.volume(measure='induced_rational',
            ....:          engine='normaliz')
            3/2
            sage: P.volume(measure='induced_lattice')
            3

        The same polytope without normaliz backend::

            sage: P = Polyhedron(vertices=[[1,0,0], [0,0,1], [-1,1,1], [-1,2,0]])
            sage: P.volume(measure='induced_lattice', engine='latte')   # optional - latte_int
            3

            sage: # needs sage.groups sage.rings.number_field
            sage: Dexact = polytopes.dodecahedron()
            sage: F0 = Dexact.faces(2)[0].as_polyhedron()
            sage: v = F0.volume(measure='induced', engine='internal'); v
            1.53406271079097?
            sage: F4 = Dexact.faces(2)[4].as_polyhedron()
            sage: v = F4.volume(measure='induced', engine='internal'); v
            1.53406271079097?
            sage: RDF(v)    # abs tol 1e-9
            1.53406271079044

            sage: # needs sage.groups
            sage: Dinexact = polytopes.dodecahedron(exact=False)
            sage: F2 = Dinexact.faces(2)[2].as_polyhedron()
            sage: w = F2.volume(measure='induced', engine='internal')
            sage: RDF(w)    # abs tol 1e-9
            1.5340627082974878

            sage: all(polytopes.simplex(d).volume(measure='induced')                    # needs sage.rings.number_field sage.symbolic
            ....:        == sqrt(d+1)/factorial(d)
            ....:     for d in range(1,5))
            True

            sage: I = Polyhedron([[-3, 0], [0, 9]])
            sage: I.volume(measure='induced')                                           # needs sage.rings.number_field
            9.48683298050514?
            sage: I.volume(measure='induced_rational')                  # optional - latte_int
            3

            sage: T = Polyhedron([[3, 0, 0], [0, 4, 0], [0, 0, 5]])
            sage: T.volume(measure='induced')                                           # needs sage.rings.number_field
            13.86542462386205?
            sage: T.volume(measure='induced_rational')                  # optional - latte_int
            1/2

            sage: Q = Polyhedron(vertices=[(0, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0)])
            sage: Q.volume(measure='induced')
            1
            sage: Q.volume(measure='induced_rational')                  # optional - latte_int
            1/2

        The volume of a full-dimensional unbounded polyhedron is infinity::

            sage: P = Polyhedron(vertices=[[1, 0], [0, 1]], rays=[[1, 1]])
            sage: P.volume()
            +Infinity

        The volume of a non full-dimensional unbounded polyhedron depends on the measure used::

            sage: P = Polyhedron(ieqs = [[1,1,1], [-1,-1,-1], [3,1,0]]); P
            A 1-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 ray
            sage: P.volume()
            0
            sage: P.volume(measure='induced')
            +Infinity
            sage: P.volume(measure='ambient')
            0
            sage: P.volume(measure='induced_rational')                  # optional - pynormaliz
            +Infinity
            sage: P.volume(measure='induced_rational',engine='latte')
            +Infinity

        The volume in `0`-dimensional space is taken by counting measure::

            sage: P = Polyhedron(vertices=[[]]); P
            A 0-dimensional polyhedron in ZZ^0 defined as the convex hull of 1 vertex
            sage: P.volume()
            1
            sage: P = Polyhedron(vertices=[]); P
            The empty polyhedron in ZZ^0
            sage: P.volume()
            0

        TESTS:

        The cache of the volume is being pickled::

            sage: P = polytopes.cube()
            sage: P.volume()
            8
            sage: Q = loads(dumps(P))
            sage: Q.volume.is_in_cache()
            True

        Induced volumes work with lrs (:issue:`33410`)::

            sage: P = Polyhedron([[0, 0], [1, 1]])
            sage: P.volume(measure='induced', engine='lrs')             # optional - lrslib
            1.414213562373095?
        """
    def integrate(self, function, measure: str = 'ambient', **kwds):
        """
        Return the integral of ``function`` over this polytope.

        INPUT:

        - ``self`` -- Polyhedron

        - ``function`` -- a multivariate polynomial or
          a valid LattE description string for polynomials

        - ``measure`` -- string, the measure to use

          Allowed values are:

          * ``ambient`` (default): Lebesgue measure of ambient space,
          * ``induced``: Lebesgue measure of the affine hull,
          * ``induced_nonnormalized``: Lebesgue measure of the affine hull
            without the normalization by `\\sqrt{\\det(A^\\top A)}` (with
            `A` being the affine transformation matrix; see :meth:`affine_hull`).

        - ``**kwds`` -- additional keyword arguments that
          are passed to the engine

        OUTPUT: the integral of the polynomial over the polytope

        .. NOTE::

            The polytope triangulation algorithm is used. This function depends
            on LattE (i.e., the ``latte_int`` optional package).

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: x, y, z = polygens(QQ, 'x, y, z')
            sage: P.integrate(x^2*y^2*z^2)                              # optional - latte_int
            8/27

        If the polyhedron has floating point coordinates, an inexact result can
        be obtained if we transform to rational coordinates::

            sage: P = 1.4142*polytopes.cube()
            sage: P_QQ = Polyhedron(vertices=[[QQ(vi) for vi in v] for v in P.vertex_generator()])
            sage: RDF(P_QQ.integrate(x^2*y^2*z^2))                      # optional - latte_int
            6.703841212195228

        Integral over a non full-dimensional polytope::

            sage: x, y = polygens(QQ, 'x, y')
            sage: P = Polyhedron(vertices=[[0,0], [1,1]])
            sage: P.integrate(x*y)
            0
            sage: ixy = P.integrate(x*y, measure='induced'); ixy        # optional - latte_int
            0.4714045207910317?
            sage: ixy.parent()                                          # optional - latte_int
            Algebraic Real Field

        Convert to a symbolic expression::

            sage: ixy.radical_expression()                              # optional - latte_int
            1/3*sqrt(2)

        Another non full-dimensional polytope integration::

            sage: R.<x, y, z> = QQ[]
            sage: P = polytopes.simplex(2)
            sage: V = AA(P.volume(measure='induced'))                                   # needs sage.rings.number_field
            sage: V.radical_expression()                                                # needs sage.rings.number_field sage.symbolic
            1/2*sqrt(3)
            sage: P.integrate(R(1), measure='induced') == V             # optional - latte_int, needs sage.rings.number_field sage.symbolic
            True

        Computing the mass center::

            sage: (P.integrate(x, measure='induced')                    # optional - latte_int, needs sage.rings.number_field sage.symbolic
            ....:     / V).radical_expression()
            1/3
            sage: (P.integrate(y, measure='induced')                    # optional - latte_int, needs sage.rings.number_field sage.symbolic
            ....:     / V).radical_expression()
            1/3
            sage: (P.integrate(z, measure='induced')                    # optional - latte_int, needs sage.rings.number_field sage.symbolic
            ....:     / V).radical_expression()
            1/3

        TESTS:

        Testing a three-dimensional integral::

            sage: P = polytopes.octahedron()
            sage: x, y, z = polygens(QQ, 'x, y, z')
            sage: P.integrate(2*x^2*y^4*z^6 + z^2)                      # optional - latte_int
            630632/4729725

        Testing a polytope with non-rational vertices::

            sage: P = polytopes.icosahedron()                                           # needs sage.groups sage.rings.number_field
            sage: P.integrate(x^2*y^2*z^2)                              # optional - latte_int, needs sage.groups sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be ZZ, QQ, or RDF

        Testing a univariate polynomial::

            sage: P = Polyhedron(vertices=[[0], [1]])
            sage: x = polygen(QQ, 'x')
            sage: P.integrate(x)                                        # optional - latte_int
            1/2

        Testing a polytope with floating point coordinates::

            sage: P = Polyhedron(vertices=[[0, 0], [1, 0], [1.1, 1.1], [0, 1]])
            sage: P.integrate('[[1,[2,2]]]')
            Traceback (most recent call last):
            ...
            TypeError: LattE integrale cannot be applied over inexact rings

        Integration of zero-polynomial::

            sage: R.<x, y, z> = QQ[]
            sage: P = polytopes.simplex(2)
            sage: P.integrate(R(0))
            0
            sage: P.integrate('[]')  # with LattE description string
            0

        ::

            sage: R.<x, y, z> = QQ[]
            sage: P = Polyhedron(vertices=[(0, 0, 1), (0, 1, 0)])
            sage: P.integrate(x^2)
            0
        """
