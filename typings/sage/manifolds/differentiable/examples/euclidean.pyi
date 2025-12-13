from sage.categories.manifolds import Manifolds as Manifolds
from sage.categories.metric_spaces import MetricSpaces as MetricSpaces
from sage.functions.trig import atan2 as atan2, cos as cos, sin as sin
from sage.manifolds.differentiable.pseudo_riemannian import PseudoRiemannianManifold as PseudoRiemannianManifold
from sage.misc.functional import sqrt as sqrt
from sage.misc.latex import latex as latex
from sage.rings.real_mpfr import RR as RR

class EuclideanSpace(PseudoRiemannianManifold):
    '''
    Euclidean space.

    A *Euclidean space of dimension* `n` is an affine space `E`, whose
    associated vector space is a `n`-dimensional vector space over `\\RR` and
    is equipped with a positive definite symmetric bilinear form, called
    the *scalar product* or *dot product*.

    Euclidean space of dimension `n` can be viewed as a Riemannian manifold
    that is diffeomorphic to `\\RR^n` and that has a flat metric `g`. The
    Euclidean scalar product is the one defined by the Riemannian metric `g`.

    INPUT:

    - ``n`` -- positive integer; dimension of the space over the real field
    - ``name`` -- (default: ``None``) string; name (symbol) given to the
      Euclidean space; if ``None``, the name will be set to ``\'E^n\'``
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the space; if ``None``, it is set to ``\'\\mathbb{E}^{n}\'`` if
      ``name`` is  ``None`` and to ``name`` otherwise
    - ``coordinates`` -- (default: ``\'Cartesian\'``) string describing the
      type of coordinates to be initialized at the Euclidean space
      creation; allowed values are

      - ``\'Cartesian\'`` (canonical coordinates on `\\RR^n`)
      - ``\'polar\'`` for ``n=2`` only (see
        :meth:`~sage.manifolds.differentiable.examples.euclidean.EuclideanPlane.polar_coordinates`)
      - ``\'spherical\'`` for ``n=3`` only (see
        :meth:`~sage.manifolds.differentiable.examples.euclidean.Euclidean3dimSpace.spherical_coordinates`)
      - ``\'cylindrical\'`` for ``n=3`` only (see
        :meth:`~sage.manifolds.differentiable.examples.euclidean.Euclidean3dimSpace.cylindrical_coordinates`)

    - ``symbols`` -- (default: ``None``) string defining the coordinate
      text symbols and LaTeX symbols, with the same conventions as the
      argument ``coordinates`` in
      :class:`~sage.manifolds.differentiable.chart.RealDiffChart`, namely
      ``symbols`` is a string of coordinate fields separated by a blank
      space, where each field contains the coordinate\'s text symbol and
      possibly the coordinate\'s LaTeX symbol (when the latter is different
      from the text symbol), both symbols being separated by a colon
      (``:``); if ``None``, the symbols will be automatically generated
      according to the value of ``coordinates``
    - ``metric_name`` -- (default: ``\'g\'``) string; name (symbol) given to the
      Euclidean metric tensor
    - ``metric_latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the Euclidean metric tensor; if none is provided, it is set to
      ``metric_name``
    - ``start_index`` -- (default: 1) integer; lower value of the range of
      indices used for "indexed objects" in the Euclidean space, e.g.
      coordinates of a chart
    - ``names`` -- (default: ``None``) unused argument, except if
      ``symbols`` is not provided; it must then be a tuple containing
      the coordinate symbols (this is guaranteed if the shortcut operator
      ``<,>`` is used)

    If ``names`` is specified, then ``n`` does not have to be specified.

    EXAMPLES:

    Constructing a 2-dimensional Euclidean space::

        sage: E = EuclideanSpace(2); E
        Euclidean plane E^2

    Each call to :class:`EuclideanSpace` creates a different object::

        sage: E1 = EuclideanSpace(2)
        sage: E1 is E
        False
        sage: E1 == E
        False

    The LaTeX symbol of the Euclidean space is by default `\\mathbb{E}^n`,
    where `n` is the dimension::

        sage: latex(E)
        \\mathbb{E}^{2}

    But both the name and LaTeX names of the Euclidean space can be
    customized::

        sage: F = EuclideanSpace(2, name=\'F\', latex_name=r\'\\mathcal{F}\'); F
        Euclidean plane F
        sage: latex(F)
        \\mathcal{F}

    By default, a Euclidean space is created with a single coordinate chart:
    that of Cartesian coordinates::

        sage: E.atlas()
        [Chart (E^2, (x, y))]
        sage: E.cartesian_coordinates()
        Chart (E^2, (x, y))
        sage: E.default_chart() is E.cartesian_coordinates()
        True

    The coordinate variables can be initialized, as the Python variables
    ``x`` and ``y``, by::

        sage: x, y = E.cartesian_coordinates()[:]

    However, it is possible to both construct the Euclidean space and
    initialize the coordinate variables in a single stage, thanks to
    SageMath operator ``<,>``::

        sage: E.<x,y> = EuclideanSpace()

    Note that providing the dimension as an argument of ``EuclideanSpace`` is
    not necessary in that case, since it can be deduced from the number of
    coordinates within ``<,>``. Besides, the coordinate symbols can be
    customized::

        sage: E.<X,Y> = EuclideanSpace()
        sage: E.cartesian_coordinates()
        Chart (E^2, (X, Y))

    By default, the LaTeX symbols of the coordinates coincide with the text
    ones::

        sage: latex(X+Y)
        X + Y

    However, it is possible to customize them, via the argument ``symbols``,
    which must be a string, usually prefixed by ``r`` (for *raw* string, in
    order to allow for the backslash character of LaTeX expressions). This
    string contains the coordinate fields separated by a blank space; each
    field contains the coordinate\'s text symbol and possibly the coordinate\'s
    LaTeX symbol (when the latter is different from the text symbol), both
    symbols being separated by a colon (``:``)::

        sage: E.<xi,ze> = EuclideanSpace(symbols=r"xi:\\xi ze:\\zeta")
        sage: E.cartesian_coordinates()
        Chart (E^2, (xi, ze))
        sage: latex(xi+ze)
        {\\xi} + {\\zeta}

    Thanks to the argument ``coordinates``, a Euclidean space can be
    constructed with curvilinear coordinates initialized instead of the
    Cartesian ones::

        sage: E.<r,ph> = EuclideanSpace(coordinates=\'polar\')
        sage: E.atlas()   # no Cartesian coordinates have been constructed
        [Chart (E^2, (r, ph))]
        sage: polar = E.polar_coordinates(); polar
        Chart (E^2, (r, ph))
        sage: E.default_chart() is polar
        True
        sage: latex(r+ph)
        {\\phi} + r

    The Cartesian coordinates, along with the transition maps to and from
    the curvilinear coordinates, can be constructed at any time by::

        sage: cartesian.<x,y> = E.cartesian_coordinates()
        sage: E.atlas()  # both polar and Cartesian coordinates now exist
        [Chart (E^2, (r, ph)), Chart (E^2, (x, y))]

    The transition maps have been initialized by the command
    ``E.cartesian_coordinates()``::

        sage: E.coord_change(polar, cartesian).display()
        x = r*cos(ph)
        y = r*sin(ph)
        sage: E.coord_change(cartesian, polar).display()
        r = sqrt(x^2 + y^2)
        ph = arctan2(y, x)

    The default name of the Euclidean metric tensor is `g`::

        sage: E.metric()
        Riemannian metric g on the Euclidean plane E^2
        sage: latex(_)
        g

    But this can be customized::

        sage: E = EuclideanSpace(2, metric_name=\'h\')
        sage: E.metric()
        Riemannian metric h on the Euclidean plane E^2
        sage: latex(_)
        h
        sage: E = EuclideanSpace(2, metric_latex_name=r\'\\mathbf{g}\')
        sage: E.metric()
        Riemannian metric g on the Euclidean plane E^2
        sage: latex(_)
        \\mathbf{g}

    A 4-dimensional Euclidean space::

        sage: E = EuclideanSpace(4); E
        4-dimensional Euclidean space E^4
        sage: latex(E)
        \\mathbb{E}^{4}

    ``E`` is both a real smooth manifold of dimension `4` and a complete metric
    space::

        sage: E.category()
        Join of Category of smooth manifolds over Real Field with 53 bits of
         precision and Category of connected manifolds over Real Field with
         53 bits of precision and Category of complete metric spaces
        sage: dim(E)
        4

    It is endowed with a default coordinate chart, which is that of
    Cartesian coordinates `(x_1,x_2,x_3,x_4)`::

        sage: E.atlas()
        [Chart (E^4, (x1, x2, x3, x4))]
        sage: E.default_chart()
        Chart (E^4, (x1, x2, x3, x4))
        sage: E.default_chart() is E.cartesian_coordinates()
        True

    ``E`` is also endowed with a default metric tensor, which defines the
    Euclidean scalar product::

        sage: g = E.metric(); g
        Riemannian metric g on the 4-dimensional Euclidean space E^4
        sage: g.display()
        g = dx1⊗dx1 + dx2⊗dx2 + dx3⊗dx3 + dx4⊗dx4
    '''
    @staticmethod
    def __classcall_private__(cls, n=None, name=None, latex_name=None, coordinates: str = 'Cartesian', symbols=None, metric_name: str = 'g', metric_latex_name=None, start_index: int = 1, names=None, unique_tag=None):
        """
        Determine the correct class to return based upon the input.

        TESTS::

            sage: E2.<x,y> = EuclideanSpace(); E2
            Euclidean plane E^2
            sage: type(E2)
            <class 'sage.manifolds.differentiable.examples.euclidean.EuclideanPlane_with_category'>

            sage: E3.<r,t,p> = EuclideanSpace(coordinates='spherical'); E3
            Euclidean space E^3
            sage: type(E3)
            <class 'sage.manifolds.differentiable.examples.euclidean.Euclidean3dimSpace_with_category'>
            sage: E3.default_frame()._latex_indices
            (r, {\\theta}, {\\phi})
        """
    def __init__(self, n, name=None, latex_name=None, coordinates: str = 'Cartesian', symbols=None, metric_name: str = 'g', metric_latex_name=None, start_index: int = 1, base_manifold=None, category=None, init_coord_methods=None, unique_tag=None) -> None:
        """
        Construct a Euclidean space.

        INPUT:

        This class also takes the following input:

        - ``base_manifold`` -- (default: ``None``) if not ``None``, must be
          a Euclidean space; the created object is then an open subset
          of ``base_manifold``
        - ``category`` -- (default: ``None``) to specify the category;
          if ``None``,
          ``Manifolds(RR).Smooth() & MetricSpaces().Complete()`` is assumed
        - ``init_coord_methods`` -- (default: ``None``) dictionary of
          methods to initialize the various type of coordinates, with each
          key being a string describing the type of coordinates; to be
          used by derived classes only
        - ``unique_tag`` -- (default: ``None``) tag used to force the
          construction of a new object when all the other arguments have
          been used previously (without ``unique_tag``, the
          :class:`~sage.structure.unique_representation.UniqueRepresentation`
          behavior inherited from
          :class:`~sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold`
          would return the previously constructed object corresponding
          to these arguments)

        TESTS::

            sage: E = EuclideanSpace(4); E
            4-dimensional Euclidean space E^4
            sage: E.metric()
            Riemannian metric g on the 4-dimensional Euclidean space E^4
            sage: TestSuite(E).run()
        """
    def cartesian_coordinates(self, symbols=None, names=None):
        """
        Return the chart of Cartesian coordinates, possibly creating it if it
        does not already exist.

        INPUT:

        - ``symbols`` -- (default: ``None``) string defining the coordinate
          text symbols and LaTeX symbols, with the same conventions as
          the argument ``coordinates`` in
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`; this is
          used only if the Cartesian chart has not been already defined; if
          ``None`` the symbols are generated as `(x_1,\\ldots,x_n)`.
        - ``names`` -- (default: ``None``) unused argument, except if
          ``symbols`` is not provided; it must be a tuple containing
          the coordinate symbols (this is guaranteed if the shortcut operator
          ``<,>`` is used)

        OUTPUT:

        - the chart of Cartesian coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        EXAMPLES::

            sage: E = EuclideanSpace(4)
            sage: X = E.cartesian_coordinates(); X
            Chart (E^4, (x1, x2, x3, x4))
            sage: X.coord_range()
            x1: (-oo, +oo); x2: (-oo, +oo); x3: (-oo, +oo); x4: (-oo, +oo)
            sage: X[2]
            x2
            sage: X[:]
            (x1, x2, x3, x4)
            sage: latex(X[:])
            \\left({x_{1}}, {x_{2}}, {x_{3}}, {x_{4}}\\right)
        """
    def cartesian_frame(self):
        """
        Return the orthonormal vector frame associated with Cartesian
        coordinates.

        OUTPUT: :class:`~sage.manifolds.differentiable.vectorframe.CoordFrame`

        EXAMPLES::

            sage: E = EuclideanSpace(2)
            sage: E.cartesian_frame()
            Coordinate frame (E^2, (e_x,e_y))
            sage: E.cartesian_frame()[1]
            Vector field e_x on the Euclidean plane E^2
            sage: E.cartesian_frame()[:]
            (Vector field e_x on the Euclidean plane E^2,
             Vector field e_y on the Euclidean plane E^2)

        For Cartesian coordinates, the orthonormal frame coincides with the
        coordinate frame::

            sage: E.cartesian_frame() is E.cartesian_coordinates().frame()
            True
        """
    def dist(self, p, q):
        """
        Euclidean distance between two points.

        INPUT:

        - ``p`` -- an element of ``self``
        - ``q`` -- an element of ``self``

        OUTPUT:

        - the Euclidean distance `d(p, q)`

        EXAMPLES::

            sage: E.<x,y> = EuclideanSpace()
            sage: p = E((1,0))
            sage: q = E((0,2))
            sage: E.dist(p, q)
            sqrt(5)
            sage: p.dist(q)  # indirect doctest
            sqrt(5)
        """
    def sphere(self, radius: int = 1, center=None, name=None, latex_name=None, coordinates: str = 'spherical', names=None):
        """
        Return an `(n-1)`-sphere smoothly embedded in ``self``.

        INPUT:

        - ``radius`` -- (default: ``1``) the radius greater than 1 of the sphere
        - ``center`` -- (default: ``None``) point on ``self`` representing the
          barycenter of the sphere
        - ``name`` -- (default: ``None``) string; name (symbol) given to the
          sphere; if ``None``, the name will be generated according to the input
        - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
          the sphere; if ``None``, the symbol will be generated according to
          the input
        - ``coordinates`` -- (default: ``'spherical'``) string describing the
          type of coordinates to be initialized at the sphere's creation;
          allowed values are

          - ``'spherical'`` spherical coordinates (see
            :meth:`~sage.manifolds.differentiable.examples.sphere.Sphere.spherical_coordinates`))
          - ``'stereographic'`` stereographic coordinates given by the
            stereographic projection (see
            :meth:`~sage.manifolds.differentiable.examples.sphere.Sphere.stereographic_coordinates`)

        - ``names`` -- (default: ``None``) must be a tuple containing
          the coordinate symbols (this guarantees the shortcut operator
          ``<,>`` to function); if ``None``, the usual conventions are used (see
          examples in
          :class:`~sage.manifolds.differentiable.examples.sphere.Sphere`
          for details)

        EXAMPLES:

        Define a 2-sphere with radius 2 centered at `(1,2,3)` in Cartesian
        coordinates::

            sage: E3 = EuclideanSpace(3)
            sage: c = E3.point((1,2,3), name='c'); c
            Point c on the Euclidean space E^3
            sage: S2_2 = E3.sphere(radius=2, center=c); S2_2
            2-sphere S^2_2(c) of radius 2 smoothly embedded in the Euclidean
             space E^3 centered at the Point c

        The ambient space is precisely our previously defined Euclidean space::

            sage: S2_2.ambient() is E3
            True

        The embedding into Euclidean space::

            sage: S2_2.embedding().display()
            iota: S^2_2(c) → E^3
            on A: (theta, phi) ↦ (x, y, z) = (2*cos(phi)*sin(theta) + 1,
                                                 2*sin(phi)*sin(theta) + 2,
                                                 2*cos(theta) + 3)

        See :class:`~sage.manifolds.differentiable.examples.sphere.Sphere`
        for more examples.
        """

class EuclideanPlane(EuclideanSpace):
    '''
    Euclidean plane.

    A *Euclidean plane* is an affine space `E`, whose associated vector space
    is a 2-dimensional vector space over `\\RR` and is equipped with a
    positive definite symmetric bilinear form, called the *scalar product* or
    *dot product*.

    The class :class:`EuclideanPlane` inherits from
    :class:`~sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold`
    (via :class:`EuclideanSpace`) since a Euclidean plane can be viewed
    as a Riemannian manifold that is diffeomorphic to `\\RR^2` and that has a
    flat metric `g`. The Euclidean scalar product is the one defined by the
    Riemannian metric `g`.

    INPUT:

    - ``name`` -- (default: ``None``) string; name (symbol) given to the
      Euclidean plane; if ``None``, the name will be set to ``\'E^2\'``
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      Euclidean plane; if ``None``, it is set to ``\'\\mathbb{E}^{2}\'`` if
      ``name`` is  ``None`` and to ``name`` otherwise
    - ``coordinates`` -- (default: ``\'Cartesian\'``) string describing the type
      of coordinates to be initialized at the Euclidean plane creation;
      allowed values are ``\'Cartesian\'`` (see :meth:`cartesian_coordinates`)
      and ``\'polar\'`` (see :meth:`polar_coordinates`)
    - ``symbols`` -- (default: ``None``) string defining the coordinate text
      symbols and LaTeX symbols, with the same conventions as the argument
      ``coordinates`` in
      :class:`~sage.manifolds.differentiable.chart.RealDiffChart`, namely
      ``symbols`` is a string of coordinate fields separated by a blank space,
      where each field contains the coordinate\'s text symbol and possibly the
      coordinate\'s LaTeX symbol (when the latter is different from the text
      symbol), both symbols being separated by a colon (``:``); if ``None``,
      the symbols will be automatically generated according to the value of
      ``coordinates``
    - ``metric_name`` -- (default: ``\'g\'``) string; name (symbol) given to the
      Euclidean metric tensor
    - ``metric_latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the Euclidean metric tensor; if none is provided, it is set to
      ``metric_name``
    - ``start_index`` -- (default: 1) integer; lower value of the range of
      indices used for "indexed objects" in the Euclidean plane, e.g.
      coordinates of a chart
    - ``base_manifold`` -- (default: ``None``) if not ``None``, must be an
      Euclidean plane; the created object is then an open subset of ``base_manifold``
    - ``category`` -- (default: ``None``) to specify the category; if ``None``,
      ``Manifolds(RR).Smooth() & MetricSpaces().Complete()`` is assumed
    - ``names`` -- (default: ``None``) unused argument, except if
      ``symbols`` is not provided; it must then be a tuple containing
      the coordinate symbols (this is guaranteed if the shortcut operator
      ``<,>`` is used)
    - ``init_coord_methods`` -- (default: ``None``) dictionary of methods
      to initialize the various type of coordinates, with each key being a
      string describing the type of coordinates; to be used by derived classes
      only
    - ``unique_tag`` -- (default: ``None``) tag used to force the construction
      of a new object when all the other arguments have been used previously
      (without ``unique_tag``, the
      :class:`~sage.structure.unique_representation.UniqueRepresentation`
      behavior inherited from
      :class:`~sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold`
      would return the previously constructed object corresponding to these
      arguments)

    EXAMPLES:

    One creates a Euclidean plane ``E`` with::

        sage: E.<x,y> = EuclideanSpace(); E
        Euclidean plane E^2

    ``E`` is both a real smooth manifold of dimension `2` and a complete metric
    space::

        sage: E.category()
        Join of Category of smooth manifolds over Real Field with 53 bits of
         precision and Category of connected manifolds over Real Field with
         53 bits of precision and Category of complete metric spaces
        sage: dim(E)
        2

    It is endowed with a default coordinate chart, which is that
    of Cartesian coordinates `(x,y)`::

        sage: E.atlas()
        [Chart (E^2, (x, y))]
        sage: E.default_chart()
        Chart (E^2, (x, y))
        sage: cartesian = E.cartesian_coordinates()
        sage: cartesian is E.default_chart()
        True

    A point of ``E``::

        sage: p = E((3,-2)); p
        Point on the Euclidean plane E^2
        sage: cartesian(p)
        (3, -2)
        sage: p in E
        True
        sage: p.parent() is E
        True

    ``E`` is endowed with a default metric tensor, which defines the
    Euclidean scalar product::

        sage: g = E.metric(); g
        Riemannian metric g on the Euclidean plane E^2
        sage: g.display()
        g = dx⊗dx + dy⊗dy

    Curvilinear coordinates can be introduced on ``E``: see
    :meth:`polar_coordinates`.

    .. SEEALSO::

        :ref:`EuclideanSpace_example1`
    '''
    def __init__(self, name=None, latex_name=None, coordinates: str = 'Cartesian', symbols=None, metric_name: str = 'g', metric_latex_name=None, start_index: int = 1, base_manifold=None, category=None, unique_tag=None) -> None:
        """
        Construct a Euclidean plane.

        TESTS::

            sage: E = EuclideanSpace(2); E
            Euclidean plane E^2
            sage: E.metric()
            Riemannian metric g on the Euclidean plane E^2
            sage: TestSuite(E).run()
        """
    def cartesian_coordinates(self, symbols=None, names=None):
        """
        Return the chart of Cartesian coordinates, possibly creating it if it
        does not already exist.

        INPUT:

        - ``symbols`` -- (default: ``None``) string defining the coordinate
          text symbols and LaTeX symbols, with the same conventions as the
          argument ``coordinates`` in
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`; this is
          used only if the Cartesian chart has not been already defined; if
          ``None`` the symbols are generated as `(x,y)`.
        - ``names`` -- (default: ``None``) unused argument, except if
          ``symbols`` is not provided; it must be a tuple containing
          the coordinate symbols (this is guaranteed if the shortcut operator
          ``<,>`` is used)

        OUTPUT:

        - the chart of Cartesian coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        EXAMPLES::

            sage: E = EuclideanSpace(2)
            sage: E.cartesian_coordinates()
            Chart (E^2, (x, y))
            sage: E.cartesian_coordinates().coord_range()
            x: (-oo, +oo); y: (-oo, +oo)

        An example where the Cartesian coordinates have not been previously
        created::

            sage: E = EuclideanSpace(2, coordinates='polar')
            sage: E.atlas()  # only polar coordinates have been initialized
            [Chart (E^2, (r, ph))]
            sage: E.cartesian_coordinates(symbols='X Y')
            Chart (E^2, (X, Y))
            sage: E.atlas()  # the Cartesian chart has been added to the atlas
            [Chart (E^2, (r, ph)), Chart (E^2, (X, Y))]

        Note that if the Cartesian coordinates have been already initialized,
        the argument ``symbols`` has no effect::

            sage: E.cartesian_coordinates(symbols='x y')
            Chart (E^2, (X, Y))

        The coordinate variables are returned by the square bracket operator::

            sage: E.cartesian_coordinates()[1]
            X
            sage: E.cartesian_coordinates()[2]
            Y
            sage: E.cartesian_coordinates()[:]
            (X, Y)

        It is also possible to use the operator ``<,>`` to set symbolic
        variable containing the coordinates::

            sage: E = EuclideanSpace(2, coordinates='polar')
            sage: cartesian.<u,v> = E.cartesian_coordinates()
            sage: cartesian
            Chart (E^2, (u, v))
            sage: u,v
            (u, v)

        The command ``cartesian.<u,v> = E.cartesian_coordinates()`` is
        actually a shortcut for::

            sage: cartesian = E.cartesian_coordinates(symbols='u v')
            sage: u, v = cartesian[:]
        """
    def polar_coordinates(self, symbols=None, names=None):
        '''
        Return the chart of polar coordinates, possibly creating it if it
        does not already exist.

        INPUT:

        - ``symbols`` -- (default: ``None``) string defining the coordinate
          text symbols and LaTeX symbols, with the same conventions as the
          argument ``coordinates`` in
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`; this is
          used only if the polar chart has not been already defined; if
          ``None`` the symbols are generated as `(r,\\phi)`.
        - ``names`` -- (default: ``None``) unused argument, except if
          ``symbols`` is not provided; it must be a tuple containing
          the coordinate symbols (this is guaranteed if the shortcut operator
          ``<,>`` is used)

        OUTPUT:

        - the chart of polar coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        EXAMPLES::

            sage: E = EuclideanSpace(2)
            sage: E.polar_coordinates()
            Chart (E^2, (r, ph))
            sage: latex(_)
            \\left(\\mathbb{E}^{2},(r, {\\phi})\\right)
            sage: E.polar_coordinates().coord_range()
            r: (0, +oo); ph: [0, 2*pi] (periodic)

        The relation to Cartesian coordinates is::

            sage: E.coord_change(E.polar_coordinates(),
            ....:                E.cartesian_coordinates()).display()
            x = r*cos(ph)
            y = r*sin(ph)
            sage: E.coord_change(E.cartesian_coordinates(),
            ....:                E.polar_coordinates()).display()
            r = sqrt(x^2 + y^2)
            ph = arctan2(y, x)

        The coordinate variables are returned by the square bracket operator::

            sage: E.polar_coordinates()[1]
            r
            sage: E.polar_coordinates()[2]
            ph
            sage: E.polar_coordinates()[:]
            (r, ph)

        They can also be obtained via the operator ``<,>``::

            sage: polar.<r,ph> = E.polar_coordinates(); polar
            Chart (E^2, (r, ph))
            sage: r, ph
            (r, ph)

        Actually, ``polar.<r,ph> = E.polar_coordinates()`` is a shortcut for::

            sage: polar = E.polar_coordinates()
            sage: r, ph = polar[:]

        The coordinate symbols can be customized::

            sage: E = EuclideanSpace(2)
            sage: E.polar_coordinates(symbols=r"r th:\\theta")
            Chart (E^2, (r, th))
            sage: latex(E.polar_coordinates())
            \\left(\\mathbb{E}^{2},(r, {\\theta})\\right)

        Note that if the polar coordinates have been already initialized, the
        argument ``symbols`` has no effect::

            sage: E.polar_coordinates(symbols=r"R Th:\\Theta")
            Chart (E^2, (r, th))
        '''
    def polar_frame(self):
        """
        Return the orthonormal vector frame associated with polar
        coordinates.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.vectorframe.VectorFrame`

        EXAMPLES::

            sage: E = EuclideanSpace(2)
            sage: E.polar_frame()
            Vector frame (E^2, (e_r,e_ph))
            sage: E.polar_frame()[1]
            Vector field e_r on the Euclidean plane E^2
            sage: E.polar_frame()[:]
            (Vector field e_r on the Euclidean plane E^2,
             Vector field e_ph on the Euclidean plane E^2)

        The orthonormal polar frame expressed in terms of the Cartesian one::

            sage: for e in E.polar_frame():
            ....:     e.display(E.cartesian_frame(), E.polar_coordinates())
            e_r = cos(ph) e_x + sin(ph) e_y
            e_ph = -sin(ph) e_x + cos(ph) e_y

        The orthonormal frame `(e_r, e_\\phi)` expressed in terms of the
        coordinate frame
        `\\left(\\frac{\\partial}{\\partial r},
        \\frac{\\partial}{\\partial\\phi}\\right)`::

            sage: for e in E.polar_frame():
            ....:     e.display(E.polar_coordinates())
            e_r = ∂/∂r
            e_ph = 1/r ∂/∂ph
        """

class Euclidean3dimSpace(EuclideanSpace):
    '''
    3-dimensional Euclidean space.

    A *3-dimensional Euclidean space* is an affine space `E`, whose associated
    vector space is a 3-dimensional vector space over `\\RR` and is equipped
    with a positive definite symmetric bilinear form, called the *scalar
    product* or *dot product*.

    The class :class:`Euclidean3dimSpace` inherits from
    :class:`~sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold`
    (via :class:`EuclideanSpace`) since a 3-dimensional Euclidean space
    can be viewed as a Riemannian manifold that is diffeomorphic to `\\RR^3` and
    that has a flat metric `g`. The Euclidean scalar product is the one defined
    by the Riemannian metric `g`.

    INPUT:

    - ``name`` -- (default: ``None``) string; name (symbol) given to the
      Euclidean 3-space; if ``None``, the name will be set to ``\'E^3\'``
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      Euclidean 3-space; if ``None``, it is set to ``\'\\mathbb{E}^{3}\'`` if
      ``name`` is  ``None`` and to ``name`` otherwise
    - ``coordinates`` -- (default: ``\'Cartesian\'``) string describing the type
      of coordinates to be initialized at the Euclidean 3-space creation;
      allowed values are ``\'Cartesian\'`` (see :meth:`cartesian_coordinates`),
      ``\'spherical\'`` (see :meth:`spherical_coordinates`) and ``\'cylindrical\'``
      (see :meth:`cylindrical_coordinates`)
    - ``symbols`` -- (default: ``None``) string defining the coordinate text
      symbols and LaTeX symbols, with the same conventions as the argument
      ``coordinates`` in
      :class:`~sage.manifolds.differentiable.chart.RealDiffChart`, namely
      ``symbols`` is a string of coordinate fields separated by a blank space,
      where each field contains the coordinate\'s text symbol and possibly the
      coordinate\'s LaTeX symbol (when the latter is different from the text
      symbol), both symbols being separated by a colon (``:``); if ``None``,
      the symbols will be automatically generated according to the value of
      ``coordinates``
    - ``metric_name`` -- (default: ``\'g\'``) string; name (symbol) given to the
      Euclidean metric tensor
    - ``metric_latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the Euclidean metric tensor; if none is provided, it is set to
      ``metric_name``
    - ``start_index`` -- (default: 1) integer; lower value of the range of
      indices used for "indexed objects" in the Euclidean 3-space, e.g.
      coordinates of a chart
    - ``base_manifold`` -- (default: ``None``) if not ``None``, must be a
      Euclidean 3-space; the created object is then an open subset of
      ``base_manifold``
    - ``category`` -- (default: ``None``) to specify the category; if ``None``,
      ``Manifolds(RR).Smooth() & MetricSpaces().Complete()`` is assumed
    - ``names`` -- (default: ``None``) unused argument, except if
      ``symbols`` is not provided; it must then be a tuple containing
      the coordinate symbols (this is guaranteed if the shortcut operator
      ``<,>`` is used)
    - ``init_coord_methods`` -- (default: ``None``) dictionary of methods
      to initialize the various type of coordinates, with each key being a
      string describing the type of coordinates; to be used by derived classes
      only
    - ``unique_tag`` -- (default: ``None``) tag used to force the construction
      of a new object when all the other arguments have been used previously
      (without ``unique_tag``, the
      :class:`~sage.structure.unique_representation.UniqueRepresentation`
      behavior inherited from
      :class:`~sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold`
      would return the previously constructed object corresponding to these
      arguments)

    EXAMPLES:

    A 3-dimensional Euclidean space::

        sage: E = EuclideanSpace(3); E
        Euclidean space E^3
        sage: latex(E)
        \\mathbb{E}^{3}

    ``E`` belongs to the class :class:`Euclidean3dimSpace` (actually to
    a dynamically generated subclass of it via SageMath\'s category framework)::

        sage: type(E)
        <class \'sage.manifolds.differentiable.examples.euclidean.Euclidean3dimSpace_with_category\'>

    ``E`` is both a real smooth manifold of dimension `3` and a complete metric
    space::

        sage: E.category()
        Join of Category of smooth manifolds over Real Field with 53 bits of
         precision and Category of connected manifolds over Real Field with
         53 bits of precision and Category of complete metric spaces
        sage: dim(E)
        3

    It is endowed with a default coordinate chart, which is that of Cartesian
    coordinates `(x,y,z)`::

        sage: E.atlas()
        [Chart (E^3, (x, y, z))]
        sage: E.default_chart()
        Chart (E^3, (x, y, z))
        sage: cartesian = E.cartesian_coordinates()
        sage: cartesian is E.default_chart()
        True

    A point of ``E``::

        sage: p = E((3,-2,1)); p
        Point on the Euclidean space E^3
        sage: cartesian(p)
        (3, -2, 1)
        sage: p in E
        True
        sage: p.parent() is E
        True

    ``E`` is endowed with a default metric tensor, which defines the
    Euclidean scalar product::

        sage: g = E.metric(); g
        Riemannian metric g on the Euclidean space E^3
        sage: g.display()
        g = dx⊗dx + dy⊗dy + dz⊗dz

    Curvilinear coordinates can be introduced on ``E``: see
    :meth:`spherical_coordinates` and :meth:`cylindrical_coordinates`.

    .. SEEALSO::

        :ref:`EuclideanSpace_example2`
    '''
    def __init__(self, name=None, latex_name=None, coordinates: str = 'Cartesian', symbols=None, metric_name: str = 'g', metric_latex_name=None, start_index: int = 1, base_manifold=None, category=None, unique_tag=None) -> None:
        """
        Construct a Euclidean 3-space.

        TESTS::

            sage: E = EuclideanSpace(3); E
            Euclidean space E^3
            sage: E.metric()
            Riemannian metric g on the Euclidean space E^3
            sage: TestSuite(E).run()
        """
    def cartesian_coordinates(self, symbols=None, names=None):
        """
        Return the chart of Cartesian coordinates, possibly creating it if it
        does not already exist.

        INPUT:

        - ``symbols`` -- (default: ``None``) string defining the coordinate
          text symbols and LaTeX symbols, with the same conventions as the
          argument ``coordinates`` in
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`; this is
          used only if the Cartesian chart has not been already defined; if
          ``None`` the symbols are generated as `(x,y,z)`.
        - ``names`` -- (default: ``None``) unused argument, except if
          ``symbols`` is not provided; it must be a tuple containing
          the coordinate symbols (this is guaranteed if the shortcut operator
          ``<,>`` is used)

        OUTPUT:

        - the chart of Cartesian coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        EXAMPLES::

            sage: E = EuclideanSpace(3)
            sage: E.cartesian_coordinates()
            Chart (E^3, (x, y, z))
            sage: E.cartesian_coordinates().coord_range()
            x: (-oo, +oo); y: (-oo, +oo); z: (-oo, +oo)

        An example where the Cartesian coordinates have not been previously
        created::

            sage: E = EuclideanSpace(3, coordinates='spherical')
            sage: E.atlas()  # only spherical coordinates have been initialized
            [Chart (E^3, (r, th, ph))]
            sage: E.cartesian_coordinates(symbols='X Y Z')
            Chart (E^3, (X, Y, Z))
            sage: E.atlas()  # the Cartesian chart has been added to the atlas
            [Chart (E^3, (r, th, ph)), Chart (E^3, (X, Y, Z))]

        The coordinate variables are returned by the square bracket operator::

            sage: E.cartesian_coordinates()[1]
            X
            sage: E.cartesian_coordinates()[3]
            Z
            sage: E.cartesian_coordinates()[:]
            (X, Y, Z)

        It is also possible to use the operator ``<,>`` to set symbolic
        variable containing the coordinates::

            sage: E = EuclideanSpace(3, coordinates='spherical')
            sage: cartesian.<u,v,w> = E.cartesian_coordinates()
            sage: cartesian
            Chart (E^3, (u, v, w))
            sage: u, v, w
            (u, v, w)

        The command ``cartesian.<u,v,w> = E.cartesian_coordinates()``
        is actually a shortcut for::

            sage: cartesian = E.cartesian_coordinates(symbols='u v w')
            sage: u, v, w = cartesian[:]
        """
    def spherical_coordinates(self, symbols=None, names=None):
        '''
        Return the chart of spherical coordinates, possibly creating it if it
        does not already exist.

        INPUT:

        - ``symbols`` -- (default: ``None``) string defining the coordinate
          text symbols and LaTeX symbols, with the same conventions as the
          argument ``coordinates`` in
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`; this is
          used only if the spherical chart has not been already defined; if
          ``None`` the symbols are generated as `(r,\\theta,\\phi)`.
        - ``names`` -- (default: ``None``) unused argument, except if
          ``symbols`` is not provided; it must be a tuple containing
          the coordinate symbols (this is guaranteed if the shortcut operator
          ``<,>`` is used)

        OUTPUT:

        - the chart of spherical coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        EXAMPLES::

            sage: E = EuclideanSpace(3)
            sage: E.spherical_coordinates()
            Chart (E^3, (r, th, ph))
            sage: latex(_)
            \\left(\\mathbb{E}^{3},(r, {\\theta}, {\\phi})\\right)
            sage: E.spherical_coordinates().coord_range()
            r: (0, +oo); th: (0, pi); ph: [0, 2*pi] (periodic)

        The relation to Cartesian coordinates is::

            sage: E.coord_change(E.spherical_coordinates(),
            ....:                E.cartesian_coordinates()).display()
            x = r*cos(ph)*sin(th)
            y = r*sin(ph)*sin(th)
            z = r*cos(th)
            sage: E.coord_change(E.cartesian_coordinates(),
            ....:                E.spherical_coordinates()).display()
            r = sqrt(x^2 + y^2 + z^2)
            th = arctan2(sqrt(x^2 + y^2), z)
            ph = arctan2(y, x)

        The coordinate variables are returned by the square bracket operator::

            sage: E.spherical_coordinates()[1]
            r
            sage: E.spherical_coordinates()[3]
            ph
            sage: E.spherical_coordinates()[:]
            (r, th, ph)

        They can also be obtained via the operator ``<,>``::

            sage: spherical.<r,th,ph> = E.spherical_coordinates()
            sage: spherical
            Chart (E^3, (r, th, ph))
            sage: r, th, ph
            (r, th, ph)

        Actually, ``spherical.<r,th,ph> = E.spherical_coordinates()`` is a
        shortcut for::

            sage: spherical = E.spherical_coordinates()
            sage: r, th, ph = spherical[:]

        The coordinate symbols can be customized::

            sage: E = EuclideanSpace(3)
            sage: E.spherical_coordinates(symbols=r"R T:\\Theta F:\\Phi")
            Chart (E^3, (R, T, F))
            sage: latex(E.spherical_coordinates())
            \\left(\\mathbb{E}^{3},(R, {\\Theta}, {\\Phi})\\right)

        Note that if the spherical coordinates have been already initialized,
        the argument ``symbols`` has no effect::

            sage: E.spherical_coordinates(symbols=r"r th:\\theta ph:\\phi")
            Chart (E^3, (R, T, F))
        '''
    def spherical_frame(self):
        """
        Return the orthonormal vector frame associated with spherical
        coordinates.

        OUTPUT: :class:`~sage.manifolds.differentiable.vectorframe.VectorFrame`

        EXAMPLES::

            sage: E = EuclideanSpace(3)
            sage: E.spherical_frame()
            Vector frame (E^3, (e_r,e_th,e_ph))
            sage: E.spherical_frame()[1]
            Vector field e_r on the Euclidean space E^3
            sage: E.spherical_frame()[:]
            (Vector field e_r on the Euclidean space E^3,
             Vector field e_th on the Euclidean space E^3,
             Vector field e_ph on the Euclidean space E^3)

        The spherical frame expressed in terms of the Cartesian one::

            sage: for e in E.spherical_frame():
            ....:     e.display(E.cartesian_frame(), E.spherical_coordinates())
            e_r = cos(ph)*sin(th) e_x + sin(ph)*sin(th) e_y + cos(th) e_z
            e_th = cos(ph)*cos(th) e_x + cos(th)*sin(ph) e_y - sin(th) e_z
            e_ph = -sin(ph) e_x + cos(ph) e_y

        The orthonormal frame `(e_r, e_\\theta, e_\\phi)` expressed in terms of
        the coordinate frame
        `\\left(\\frac{\\partial}{\\partial r}, \\frac{\\partial}{\\partial\\theta},
        \\frac{\\partial}{\\partial\\phi}\\right)`::

            sage: for e in E.spherical_frame():
            ....:     e.display(E.spherical_coordinates())
            e_r = ∂/∂r
            e_th = 1/r ∂/∂th
            e_ph = 1/(r*sin(th)) ∂/∂ph
        """
    def cylindrical_coordinates(self, symbols=None, names=None):
        '''
        Return the chart of cylindrical coordinates, possibly creating it if it
        does not already exist.

        INPUT:

        - ``symbols`` -- (default: ``None``) string defining the coordinate
          text symbols and LaTeX symbols, with the same conventions as the
          argument ``coordinates`` in
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`; this is
          used only if the cylindrical chart has not been already defined; if
          ``None`` the symbols are generated as `(\\rho,\\phi,z)`.
        - ``names`` -- (default: ``None``) unused argument, except if
          ``symbols`` is not provided; it must be a tuple containing
          the coordinate symbols (this is guaranteed if the shortcut operator
          ``<,>`` is used)

        OUTPUT:

        - the chart of cylindrical coordinates, as an instance of
          :class:`~sage.manifolds.differentiable.chart.RealDiffChart`

        EXAMPLES::

            sage: E = EuclideanSpace(3)
            sage: E.cylindrical_coordinates()
            Chart (E^3, (rh, ph, z))
            sage: latex(_)
            \\left(\\mathbb{E}^{3},({\\rho}, {\\phi}, z)\\right)
            sage: E.cylindrical_coordinates().coord_range()
            rh: (0, +oo); ph: [0, 2*pi] (periodic); z: (-oo, +oo)

        The relation to Cartesian coordinates is::

            sage: E.coord_change(E.cylindrical_coordinates(),
            ....:                E.cartesian_coordinates()).display()
            x = rh*cos(ph)
            y = rh*sin(ph)
            z = z
            sage: E.coord_change(E.cartesian_coordinates(),
            ....:                E.cylindrical_coordinates()).display()
            rh = sqrt(x^2 + y^2)
            ph = arctan2(y, x)
            z = z

        The coordinate variables are returned by the square bracket operator::

            sage: E.cylindrical_coordinates()[1]
            rh
            sage: E.cylindrical_coordinates()[3]
            z
            sage: E.cylindrical_coordinates()[:]
            (rh, ph, z)

        They can also be obtained via the operator ``<,>``::

            sage: cylindrical.<rh,ph,z> = E.cylindrical_coordinates()
            sage: cylindrical
            Chart (E^3, (rh, ph, z))
            sage: rh, ph, z
            (rh, ph, z)

        Actually, ``cylindrical.<rh,ph,z> = E.cylindrical_coordinates()`` is a
        shortcut for::

            sage: cylindrical = E.cylindrical_coordinates()
            sage: rh, ph, z = cylindrical[:]

        The coordinate symbols can be customized::

            sage: E = EuclideanSpace(3)
            sage: E.cylindrical_coordinates(symbols=r"R Phi:\\Phi Z")
            Chart (E^3, (R, Phi, Z))
            sage: latex(E.cylindrical_coordinates())
            \\left(\\mathbb{E}^{3},(R, {\\Phi}, Z)\\right)

        Note that if the cylindrical coordinates have been already initialized,
        the argument ``symbols`` has no effect::

            sage: E.cylindrical_coordinates(symbols=r"rh:\\rho ph:\\phi z")
            Chart (E^3, (R, Phi, Z))
        '''
    def cylindrical_frame(self):
        """
        Return the orthonormal vector frame associated with cylindrical
        coordinates.

        OUTPUT: :class:`~sage.manifolds.differentiable.vectorframe.VectorFrame`

        EXAMPLES::

            sage: E = EuclideanSpace(3)
            sage: E.cylindrical_frame()
            Vector frame (E^3, (e_rh,e_ph,e_z))
            sage: E.cylindrical_frame()[1]
            Vector field e_rh on the Euclidean space E^3
            sage: E.cylindrical_frame()[:]
            (Vector field e_rh on the Euclidean space E^3,
             Vector field e_ph on the Euclidean space E^3,
             Vector field e_z on the Euclidean space E^3)

        The cylindrical frame expressed in terms of the Cartesian one::

            sage: for e in E.cylindrical_frame():
            ....:     e.display(E.cartesian_frame(), E.cylindrical_coordinates())
            e_rh = cos(ph) e_x + sin(ph) e_y
            e_ph = -sin(ph) e_x + cos(ph) e_y
            e_z = e_z

        The orthonormal frame `(e_r, e_\\phi, e_z)` expressed in terms of
        the coordinate frame
        `\\left(\\frac{\\partial}{\\partial r}, \\frac{\\partial}{\\partial\\phi},
        \\frac{\\partial}{\\partial z}\\right)`::

            sage: for e in E.cylindrical_frame():
            ....:     e.display(E.cylindrical_coordinates())
            e_rh = ∂/∂rh
            e_ph = 1/rh ∂/∂ph
            e_z = ∂/∂z
        """
    def scalar_triple_product(self, name=None, latex_name=None):
        """
        Return the scalar triple product operator, as a 3-form.

        The *scalar triple product* (also called *mixed product*) of three
        vector fields `u`, `v` and `w` defined on a Euclidean space `E`
        is the scalar field

        .. MATH::

            \\epsilon(u,v,w) = u \\cdot (v \\times w).

        The scalar triple product operator `\\epsilon` is a *3-form*, i.e. a
        field of fully antisymmetric trilinear forms; it is also called the
        *volume form* of `E` or the *Levi-Civita tensor* of `E`.

        INPUT:

        - ``name`` -- (default: ``None``) string; name given to the scalar
          triple product operator; if ``None``, ``'epsilon'`` is used
        - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
          the scalar triple product; if ``None``, it is set to ``r'\\epsilon'``
          if ``name`` is ``None`` and to ``name`` otherwise.

        OUTPUT:

        - the scalar triple product operator `\\epsilon`, as an instance of
          :class:`~sage.manifolds.differentiable.diff_form.DiffFormParal`

        EXAMPLES::

            sage: E.<x,y,z> = EuclideanSpace()
            sage: triple_product = E.scalar_triple_product()
            sage: triple_product
            3-form epsilon on the Euclidean space E^3
            sage: latex(triple_product)
            \\epsilon
            sage: u = E.vector_field(x, y, z, name='u')
            sage: v = E.vector_field(-y, x, 0, name='v')
            sage: w = E.vector_field(y*z, x*z, x*y, name='w')
            sage: s = triple_product(u, v, w); s
            Scalar field epsilon(u,v,w) on the Euclidean space E^3
            sage: s.display()
            epsilon(u,v,w): E^3 → ℝ
               (x, y, z) ↦ x^3*y + x*y^3 - 2*x*y*z^2
            sage: s.expr()
            x^3*y + x*y^3 - 2*x*y*z^2
            sage: latex(s)
            \\epsilon\\left(u,v,w\\right)
            sage: s == - triple_product(w, v, u)
            True

        Check of the identity `\\epsilon(u,v,w) = u\\cdot(v\\times w)`::

            sage: s == u.dot(v.cross(w))
            True

        Customizing the name::

            sage: E.scalar_triple_product(name='S')
            3-form S on the Euclidean space E^3
            sage: latex(_)
            S
            sage: E.scalar_triple_product(name='Omega', latex_name=r'\\Omega')
            3-form Omega on the Euclidean space E^3
            sage: latex(_)
            \\Omega
        """
