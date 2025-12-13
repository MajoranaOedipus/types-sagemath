from sage.categories.manifolds import Manifolds as Manifolds
from sage.categories.metric_spaces import MetricSpaces as MetricSpaces
from sage.categories.topological_spaces import TopologicalSpaces as TopologicalSpaces
from sage.manifolds.differentiable.examples.euclidean import EuclideanSpace as EuclideanSpace
from sage.manifolds.differentiable.pseudo_riemannian_submanifold import PseudoRiemannianSubmanifold as PseudoRiemannianSubmanifold
from sage.rings.real_mpfr import RR as RR

class Sphere(PseudoRiemannianSubmanifold):
    """
    Sphere smoothly embedded in Euclidean Space.

    An `n`-sphere of radius `r`smoothly embedded in a Euclidean space `E^{n+1}`
    is a smooth `n`-dimensional manifold smoothly embedded into `E^{n+1}`,
    such that the embedding constitutes a standard `n`-sphere of radius `r`
    in that Euclidean space (possibly shifted by a point).

    - ``n`` -- positive integer representing dimension of the sphere
    - ``radius`` -- (default: ``1``) positive number that states the radius
      of the sphere
    - ``name`` -- (default: ``None``) string; name (symbol) given to the
      sphere; if ``None``, the name will be set according to the input
      (see convention above)
    - ``ambient_space`` -- (default: ``None``) Euclidean space in which the
      sphere should be embedded; if ``None``, a new instance of Euclidean
      space is created
    - ``center`` -- (default: ``None``) the barycenter of the sphere as point of
      the ambient Euclidean space; if ``None`` the barycenter is set to the
      origin of the ambient space's standard Cartesian coordinates
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the space; if ``None``, it will be set according to the input
      (see convention above)
    - ``coordinates`` -- (default: ``'spherical'``) string describing the
      type of coordinates to be initialized at the sphere's creation; allowed
      values are

          - ``'spherical'`` spherical coordinates (see
            :meth:`~sage.manifolds.differentiable.examples.sphere.Sphere.spherical_coordinates`))
          - ``'stereographic'`` stereographic coordinates given by the
            stereographic projection (see
            :meth:`~sage.manifolds.differentiable.examples.sphere.Sphere.stereographic_coordinates`)

    - ``names`` -- (default: ``None``) must be a tuple containing
      the coordinate symbols (this guarantees the shortcut operator
      ``<,>`` to function); if ``None``, the usual conventions are used (see
      examples below for details)
    - ``unique_tag`` -- (default: ``None``) tag used to force the construction
      of a new object when all the other arguments have been used previously
      (without ``unique_tag``, the
      :class:`~sage.structure.unique_representation.UniqueRepresentation`
      behavior inherited from
      :class:`~sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold`
      would return the previously constructed object corresponding to these
      arguments)

    EXAMPLES:

    A 2-sphere embedded in Euclidean space::

        sage: S2 = manifolds.Sphere(2); S2
        2-sphere S^2 of radius 1 smoothly embedded in the Euclidean space E^3
        sage: latex(S2)
        \\mathbb{S}^{2}

    The ambient Euclidean space is constructed incidentally::

        sage: S2.ambient()
        Euclidean space E^3

    Another call creates another sphere and hence another Euclidean space::

        sage: S2 is manifolds.Sphere(2)
        False
        sage: S2.ambient() is manifolds.Sphere(2).ambient()
        False

    By default, the barycenter is set to the coordinate origin of the
    standard Cartesian coordinates in the ambient Euclidean space::

        sage: c = S2.center(); c
        Point on the Euclidean space E^3
        sage: c.coord()
        (0, 0, 0)

    Each `n`-sphere is a compact manifold and a complete metric space::

        sage: S2.category()
        Join of Category of compact topological spaces and Category of smooth
         manifolds over Real Field with 53 bits of precision and Category of
         connected manifolds over Real Field with 53 bits of precision and
         Category of complete metric spaces

    If not stated otherwise, each `n`-sphere is automatically endowed with
    spherical coordinates::

        sage: S2.atlas()
        [Chart (A, (theta, phi))]
        sage: S2.default_chart()
        Chart (A, (theta, phi))
        sage: spher = S2.spherical_coordinates()
        sage: spher is S2.default_chart()
        True

    Notice that the spherical coordinates do not cover the whole sphere. To
    cover the entire sphere with charts, use stereographic coordinates instead::

        sage: stereoN, stereoS = S2.coordinate_charts('stereographic')
        sage: stereoN, stereoS
        (Chart (S^2-{NP}, (y1, y2)), Chart (S^2-{SP}, (yp1, yp2)))
        sage: list(S2.open_covers())
        [Set {S^2} of open subsets of the 2-sphere S^2 of radius 1 smoothly embedded in the Euclidean space E^3,
         Set {S^2-{NP}, S^2-{SP}} of open subsets of the 2-sphere S^2 of radius 1 smoothly embedded in the Euclidean space E^3]

    .. NOTE::

        Keep in mind that the initialization process of stereographic
        coordinates and their transition maps is computational complex in
        higher dimensions. Henceforth, high computation times are expected with
        increasing dimension.
    """
    @staticmethod
    def __classcall_private__(cls, n=None, radius: int = 1, ambient_space=None, center=None, name=None, latex_name=None, coordinates: str = 'spherical', names=None, unique_tag=None):
        """
        Determine the correct class to return based upon the input.

        TESTS:

        Each call gives a new instance::

            sage: S2 = manifolds.Sphere(2)
            sage: S2 is manifolds.Sphere(2)
            False

        The dimension can be determined using the ``<...>`` operator::

            sage: S.<x,y> = manifolds.Sphere(coordinates='stereographic'); S
            2-sphere S^2 of radius 1 smoothly embedded in the Euclidean space E^3
            sage: S._first_ngens(2)
            (x, y)
        """
    def __init__(self, n, radius: int = 1, ambient_space=None, center=None, name=None, latex_name=None, coordinates: str = 'spherical', names=None, category=None, init_coord_methods=None, unique_tag=None) -> None:
        """
        Construct sphere smoothly embedded in Euclidean space.

        TESTS::

            sage: S2 = manifolds.Sphere(2); S2
            2-sphere S^2 of radius 1 smoothly embedded in the Euclidean space E^3
            sage: S2.metric()
            Riemannian metric g on the 2-sphere S^2 of radius 1 smoothly
             embedded in the Euclidean space E^3
            sage: TestSuite(S2).run()
        """
    def coordinate_charts(self, coord_name, names=None):
        """
        Return a list of all charts belonging to the coordinates ``coord_name``.

        INPUT:

        - ``coord_name`` -- string describing the type of coordinates
        - ``names`` -- (default: ``None``) must be a tuple containing
          the coordinate symbols for the first chart in the list; if
          ``None``, the standard convention is used

        EXAMPLES:

        Spherical coordinates on `S^1`::

            sage: S1 = manifolds.Sphere(1)
            sage: S1.coordinate_charts('spherical')
            [Chart (A, (phi,))]

        Stereographic coordinates on `S^1`::

            sage: stereo_charts = S1.coordinate_charts('stereographic', names=['a'])
            sage: stereo_charts
            [Chart (S^1-{NP}, (a,)), Chart (S^1-{SP}, (ap,))]
        """
    def stereographic_coordinates(self, pole: str = 'north', names=None):
        """
        Return stereographic coordinates given by the stereographic
        projection of ``self`` w.r.t. to a given pole.

        INPUT:

        - ``pole`` -- (default: ``'north'``) the pole determining the
          stereographic projection; possible options are ``'north'`` and
          ``'south'``
        - ``names`` -- (default: ``None``) must be a tuple containing
          the coordinate symbols (this guarantees the usage of the shortcut
          operator ``<,>``)

        OUTPUT:

        - the chart of stereographic coordinates w.r.t. to the given pole,
          as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        Let `\\mathbb{S}^n_r(c)` be an `n`-sphere of radius `r` smoothly
        embedded in the Euclidean space `E^{n+1}` centered at `c \\in E^{n+1}`.
        We denote the north pole of `\\mathbb{S}^n_r(c)` by `\\mathrm{NP}` and the
        south pole by `\\mathrm{SP}`. These poles are uniquely determined by
        the requirement

        .. MATH::

            x(\\iota(\\mathrm{NP})) &= (0, \\ldots, 0, r) + x(c), \\\\\n            x(\\iota(\\mathrm{SP})) &= (0, \\ldots, 0, -r) + x(c).

        The coordinates `(y_1, \\ldots, y_n)` (`(y'_1, \\ldots, y'_n)`
        respectively) define *stereographic coordinates* on `\\mathbb{S}^n_r(c)`
        for the Cartesian coordinates `(x_1, \\ldots, x_{n+1})` on `E^{n+1}`
        if they arise from the stereographic projection from
        `\\iota(\\mathrm{NP})` (`\\iota(\\mathrm{SP})`) to the hypersurface
        `x_n = x_n(c)`. In concrete formulas, this means:

        .. MATH::

            \\left. x \\circ \\iota \\right|_{\\mathbb{S}^n_r(c) \\setminus \\{
            \\mathrm{NP}\\}}
            &= \\left( \\frac{2y_1r^2}{r^2+\\sum^n_{i=1} y^2_i},
            \\ldots, \\frac{2y_nr^2}{r^2+\\sum^n_{i=1} y^2_i},
            \\frac{r\\sum^n_{i=1} y^2_i-r^3}{r^2+\\sum^n_{i=1} y^2_i} \\right) +
            x(c), \\\\\n            \\left. x \\circ \\iota \\right|_{\\mathbb{S}^n_r(c) \\setminus \\{
            \\mathrm{SP}\\}} &= \\left( \\frac{2y'_1r^2}{r^2+\\sum^n_{i=1} y'^2_i},
            \\ldots, \\frac{2y'_nr^2}{r^2+\\sum^n_{i=1} y'^2_i},
            \\frac{r^3 - r\\sum^n_{i=1} y'^2_i}{r^2+\\sum^n_{i=1} y'^2_i} \\right) +
            x(c).

        EXAMPLES:

        Initialize a 1-sphere centered at `(1,0)` in the Euclidean plane
        using the shortcut operator::

            sage: E2 = EuclideanSpace(2)
            sage: c = E2.point((1,0), name='c')
            sage: S1.<a> = E2.sphere(center=c, coordinates='stereographic'); S1
            1-sphere S^1(c) of radius 1 smoothly embedded in the Euclidean plane
             E^2 centered at the Point c

        By default, the shortcut variables belong to the stereographic
        projection from the north pole::

            sage: S1.coordinate_charts('stereographic')
            [Chart (S^1(c)-{NP}, (a,)), Chart (S^1(c)-{SP}, (ap,))]
            sage: S1.embedding().display()
            iota: S^1(c) → E^2
            on S^1(c)-{NP}: a ↦ (x, y) = (2*a/(a^2 + 1) + 1, (a^2 - 1)/(a^2 + 1))
            on S^1(c)-{SP}: ap ↦ (x, y) = (2*ap/(ap^2 + 1) + 1, -(ap^2 - 1)/(ap^2 + 1))

        Initialize a 2-sphere from scratch::

            sage: S2 = manifolds.Sphere(2)
            sage: S2.atlas()
            [Chart (A, (theta, phi))]

        In the previous block, the stereographic coordinates have not been
        initialized. This happens subsequently with the invocation of
        ``stereographic_coordinates``::

            sage: stereoS.<u,v> = S2.stereographic_coordinates(pole='south')
            sage: S2.coordinate_charts('stereographic')
            [Chart (S^2-{NP}, (up, vp)), Chart (S^2-{SP}, (u, v))]

        If not specified by the user, the default coordinate names are given by
        `(y_1, \\ldots, y_n)` and `(y'_1, \\ldots, y'_n)` respectively::

            sage: S3 = manifolds.Sphere(3, coordinates='stereographic')
            sage: S3.stereographic_coordinates(pole='north')
            Chart (S^3-{NP}, (y1, y2, y3))
            sage: S3.stereographic_coordinates(pole='south')
            Chart (S^3-{SP}, (yp1, yp2, yp3))
        """
    def spherical_coordinates(self, names=None):
        """
        Return the spherical coordinates of ``self``.

        INPUT:

        - ``names`` -- (default: ``None``) must be a tuple containing
          the coordinate symbols (this guarantees the usage of the shortcut
          operator ``<,>``)

        OUTPUT:

        - the chart of spherical coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        Let `\\mathbb{S}^n_r(c)` be an `n`-sphere of radius `r` smoothly
        embedded in the Euclidean space `E^{n+1}` centered at `c \\in E^{n+1}`.
        We say that `(\\varphi_1, \\ldots, \\varphi_n)` define *spherical
        coordinates* on the open subset `A \\subset \\mathbb{S}^n_r(c)` for the
        Cartesian coordinates `(x_1, \\ldots, x_{n+1})` on `E^{n+1}` (not
        necessarily centered at `c`) if

        .. MATH::

            \\begin{aligned}
                \\left. x_1 \\circ \\iota \\right|_{A} &= r \\cos(\\varphi_n)\\sin(
                \\varphi_{n-1}) \\cdots
                \\sin(\\varphi_1)
                + x_1(c), \\\\\n                \\left. x_1 \\circ \\iota \\right|_{A} &= r \\sin(\\varphi_n)\\sin(
                \\varphi_{n-1}) \\cdots
                \\sin(\\varphi_1)
                + x_1(c), \\\\\n                \\left. x_2 \\circ \\iota \\right|_{A} &= r \\cos(\\varphi_{
                n-1})\\sin(\\varphi_{n-2}) \\cdots
                \\sin(\\varphi_1)
                + x_2(c), \\\\\n                \\left. x_3 \\circ \\iota \\right|_{A} &= r \\cos(\\varphi_{
                n-2})\\sin(\\varphi_{n-3}) \\cdots
                \\sin(\\varphi_1)
                + x_3(c), \\\\\n                \\vdots & \\\\\n                \\left. x_{n+1} \\circ \\iota \\right|_{A} &= r \\cos(\\varphi_1) +
                x_{n+1}(c),
            \\end{aligned}

        where `\\varphi_i` has range `(0, \\pi)` for `i=1, \\ldots, n-1` and
        `\\varphi_n` lies in `(-\\pi, \\pi)`. Notice that the above expressions
        together with the ranges of the `\\varphi_i` fully determine the open
        set `A`.

        .. NOTE::

            Notice that our convention slightly differs from the one given on
            the :wikipedia:`N-sphere#Spherical_coordinates`. The definition
            above ensures that the conventions for the most common cases
            `n=1` and `n=2` are maintained.

        EXAMPLES:

        The spherical coordinates on a 2-sphere follow the common conventions::

            sage: S2 = manifolds.Sphere(2)
            sage: spher = S2.spherical_coordinates(); spher
            Chart (A, (theta, phi))

        The coordinate range of spherical coordinates::

            sage: spher.coord_range()
            theta: (0, pi); phi: [-pi, pi] (periodic)

        Spherical coordinates do not cover the 2-sphere entirely::

            sage: A = spher.domain(); A
            Open subset A of the 2-sphere S^2 of radius 1 smoothly embedded in
             the Euclidean space E^3

        The embedding of a 2-sphere in Euclidean space via spherical
        coordinates::

            sage: S2.embedding().display()
            iota: S^2 → E^3
             on A: (theta, phi) ↦ (x, y, z) =
                                     (cos(phi)*sin(theta),
                                      sin(phi)*sin(theta),
                                      cos(theta))

        Now, consider spherical coordinates on a 3-sphere::

            sage: S3 = manifolds.Sphere(3)
            sage: spher = S3.spherical_coordinates(); spher
            Chart (A, (chi, theta, phi))
            sage: S3.embedding().display()
            iota: S^3 → E^4
            on A: (chi, theta, phi) ↦ (x1, x2, x3, x4) =
                                         (cos(phi)*sin(chi)*sin(theta),
                                          sin(chi)*sin(phi)*sin(theta),
                                          cos(theta)*sin(chi),
                                          cos(chi))

        By convention, the last coordinate is periodic::

            sage: spher.coord_range()
            chi: (0, pi); theta: (0, pi); phi: [-pi, pi] (periodic)
        """
    def dist(self, p, q):
        """
        Return the great circle distance between the points ``p`` and ``q`` on
        ``self``.

        INPUT:

        - ``p`` -- an element of ``self``
        - ``q`` -- an element of ``self``

        OUTPUT:

        - the great circle distance `d(p, q)` on ``self``

        The great circle distance `d(p, q)` of the points
        `p, q \\in \\mathbb{S}^n_r(c)` is the length of the shortest great circle
        segment on `\\mathbb{S}^n_r(c)` that joins `p` and `q`. If we choose
        Cartesian coordinates `(x_1, \\ldots, x_{n+1})` of the ambient Euclidean
        space such that the center lies in the coordinate origin, i.e.
        `x(c)=0`, the great circle distance can be expressed in terms of the
        following formula:

        .. MATH::

            d(p,q) = r \\, \\arccos\\left(\\frac{x(\\iota(p)) \\cdot
                x(\\iota(q))}{r^2}\\right).

        EXAMPLES:

        Define a 2-sphere with unspecified radius::

            sage: r = var('r')
            sage: S2_r = manifolds.Sphere(2, radius=r); S2_r
            2-sphere S^2_r of radius r smoothly embedded in the Euclidean space E^3

        Given two antipodal points in spherical coordinates::

            sage: p = S2_r.point((pi/2, pi/2), name='p'); p
            Point p on the 2-sphere S^2_r of radius r smoothly embedded in the
             Euclidean space E^3
            sage: q = S2_r.point((pi/2, -pi/2), name='q'); q
            Point q on the 2-sphere S^2_r of radius r smoothly embedded in the
             Euclidean space E^3

        The distance is determined as the length of the half great circle::

            sage: S2_r.dist(p, q)
            pi*r
        """
    def radius(self):
        """
        Return the radius of ``self``.

        EXAMPLES:

        3-sphere with radius 3::

            sage: S3_2 = manifolds.Sphere(3, radius=2); S3_2
            3-sphere S^3_2 of radius 2 smoothly embedded in the 4-dimensional
             Euclidean space E^4
            sage: S3_2.radius()
            2

        2-sphere with unspecified radius::

            sage: r = var('r')
            sage: S2_r = manifolds.Sphere(3, radius=r); S2_r
            3-sphere S^3_r of radius r smoothly embedded in the 4-dimensional
             Euclidean space E^4
            sage: S2_r.radius()
            r
        """
    def minimal_triangulation(self):
        """
        Return the minimal triangulation of ``self`` as a simplicial complex.

        EXAMPLES:

        Minimal triangulation of the 2-sphere::

            sage: S2 = manifolds.Sphere(2)
            sage: S = S2.minimal_triangulation(); S
            Minimal triangulation of the 2-sphere

        The Euler characteristic of a 2-sphere::

            sage: S.euler_characteristic()
            2
        """
    def center(self):
        """
        Return the barycenter of ``self`` in the ambient Euclidean space.

        EXAMPLES:

        2-sphere embedded in Euclidean space centered at `(1,2,3)` in
        Cartesian coordinates::

            sage: E3 = EuclideanSpace(3)
            sage: c = E3.point((1,2,3), name='c')
            sage: S2c = manifolds.Sphere(2, ambient_space=E3, center=c); S2c
            2-sphere S^2(c) of radius 1 smoothly embedded in the Euclidean space
             E^3 centered at the Point c
            sage: S2c.center()
            Point c on the Euclidean space E^3

        We can see that the embedding is shifted accordingly::

            sage: S2c.embedding().display()
            iota: S^2(c) → E^3
            on A: (theta, phi) ↦ (x, y, z) = (cos(phi)*sin(theta) + 1,
                                                 sin(phi)*sin(theta) + 2,
                                                 cos(theta) + 3)
        """
