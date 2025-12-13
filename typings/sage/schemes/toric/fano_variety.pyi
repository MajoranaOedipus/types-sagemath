from _typeshed import Incomplete
from sage.categories.fields import Fields as Fields
from sage.geometry.cone import Cone as Cone
from sage.geometry.fan import FaceFan as FaceFan, Fan as Fan
from sage.geometry.lattice_polytope import LatticePolytope as LatticePolytope
from sage.misc.latex import latex as latex
from sage.misc.misc_c import prod as prod
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.schemes.toric.toric_subscheme import AlgebraicScheme_subscheme_toric as AlgebraicScheme_subscheme_toric
from sage.schemes.toric.variety import ToricVariety_field as ToricVariety_field, normalize_names as normalize_names
from sage.structure.all import coercion_model as coercion_model

DEFAULT_COEFFICIENT: str
DEFAULT_COEFFICIENTS: Incomplete

def is_CPRFanoToricVariety(x):
    """
    Check if ``x`` is a CPR-Fano toric variety.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    - ``True`` if ``x`` is a :class:`CPR-Fano toric variety
      <CPRFanoToricVariety_field>` and ``False`` otherwise.

    .. NOTE::

        While projective spaces are Fano toric varieties mathematically, they
        are not toric varieties in Sage due to efficiency considerations, so
        this function will return ``False``.

    EXAMPLES::

        sage: from sage.schemes.toric.fano_variety import is_CPRFanoToricVariety
        sage: is_CPRFanoToricVariety(1)
        doctest:warning...
        DeprecationWarning: The function is_CPRFanoToricVariety is deprecated; use 'isinstance(..., CPRFanoToricVariety_field)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
        sage: FTV = toric_varieties.P2()
        sage: FTV
        2-d CPR-Fano toric variety covered by 3 affine patches
        sage: is_CPRFanoToricVariety(FTV)
        True
        sage: is_CPRFanoToricVariety(ProjectiveSpace(2))
        False
    """
def CPRFanoToricVariety(Delta=None, Delta_polar=None, coordinate_points=None, charts=None, coordinate_names=None, names=None, coordinate_name_indices=None, make_simplicial: bool = False, base_ring=None, base_field=None, check: bool = True):
    '''
    Construct a CPR-Fano toric variety.

    .. NOTE::

        See documentation of the module
        :mod:`~sage.schemes.toric.fano_variety` for the used
        definitions and supported varieties.

    Due to the large number of available options, it is recommended to always
    use keyword parameters.

    INPUT:

    - ``Delta`` -- reflexive :class:`lattice polytope
      <sage.geometry.lattice_polytope.LatticePolytopeClass>`. The fan of the
      constructed CPR-Fano toric variety will be a crepant subdivision of the
      *normal fan* of ``Delta``. Either ``Delta`` or ``Delta_polar`` must be
      given, but not both at the same time, since one is completely determined
      by another via :meth:`polar
      <sage.geometry.lattice_polytope.LatticePolytopeClass.polar>` method.

    - ``Delta_polar`` -- reflexive :class:`lattice polytope
      <sage.geometry.lattice_polytope.LatticePolytopeClass>`. The fan of the
      constructed CPR-Fano toric variety will be a crepant subdivision of the
      *face fan* of ``Delta_polar``. Either ``Delta`` or ``Delta_polar`` must
      be given, but not both at the same time, since one is completely
      determined by another via :meth:`polar
      <sage.geometry.lattice_polytope.LatticePolytopeClass.polar>` method.

    - ``coordinate_points`` -- list of integers or string. A list will be
      interpreted as indices of (boundary) points of ``Delta_polar`` which
      should be used as rays of the underlying fan. It must include all
      vertices of ``Delta_polar`` and no repetitions are allowed. A string
      must be one of the following descriptions of points of ``Delta_polar``:

      * "vertices" (default),
      * "all" (will not include the origin),
      * "all but facets" (will not include points in the relative interior of
        facets);

    - ``charts`` -- list of lists of elements from ``coordinate_points``. Each
      of these lists must define a generating cone of a fan subdividing the
      normal fan of ``Delta``. Default ``charts`` correspond to the normal fan
      of ``Delta`` without subdivision. The fan specified by ``charts`` will
      be subdivided to include all of the requested ``coordinate_points``.

    - ``coordinate_names`` -- names of variables for the coordinate ring, see
      :func:`~sage.schemes.toric.variety.normalize_names`
      for acceptable formats. If not given, indexed variable names will be
      created automatically.

    - ``names`` -- an alias of ``coordinate_names`` for internal
      use. You may specify either ``names`` or ``coordinate_names``,
      but not both.

    - ``coordinate_name_indices`` -- list of integers, indices for indexed
      variables. If not given, the index of each variable will coincide with
      the index of the corresponding point of ``Delta_polar``.

    - ``make_simplicial`` -- if ``True``, the underlying fan will be made
      simplicial (default: ``False``)

    - ``base_ring`` -- base field of the CPR-Fano toric variety
      (default: `\\QQ`)

    - ``base_field`` -- alias for ``base_ring``. Takes precedence if
      both are specified.

    - ``check`` -- by default the input data will be checked for correctness
      (e.g. that ``charts`` do form a subdivision of the normal fan of
      ``Delta``). If you know for sure that the input is valid, you may
      significantly decrease construction time using ``check=False`` option.

    OUTPUT: :class:`CPR-Fano toric variety <CPRFanoToricVariety_field>`

    EXAMPLES:

    We start with the product of two projective lines::

        sage: diamond = lattice_polytope.cross_polytope(2)
        sage: diamond.vertices()
        M( 1,  0),        M( 0,  1),
        M(-1,  0),        M( 0, -1)
        in 2-d lattice M
        sage: P1xP1 = CPRFanoToricVariety(Delta_polar=diamond)
        sage: P1xP1
        2-d CPR-Fano toric variety covered by 4 affine patches
        sage: P1xP1.fan()
        Rational polyhedral fan in 2-d lattice M
        sage: P1xP1.fan().rays()
        M( 1,  0),        M( 0,  1),
        M(-1,  0),        M( 0, -1)
        in 2-d lattice M

    "Unfortunately," this variety is smooth to start with and we cannot
    perform any subdivisions of the underlying fan without leaving the
    category of CPR-Fano toric varieties. Our next example starts with a
    square::

        sage: square = diamond.polar()
        sage: square.vertices()
        N( 1,  1),        N( 1, -1),
        N(-1, -1),        N(-1,  1)
        in 2-d lattice N
        sage: square.points()
        N( 1,  1),        N( 1, -1),        N(-1, -1),
        N(-1,  1),        N(-1,  0),        N( 0, -1),
        N( 0,  0),        N( 0,  1),        N( 1,  0)
        in 2-d lattice N

    We will construct several varieties associated to it::

        sage: FTV = CPRFanoToricVariety(Delta_polar=square)
        sage: FTV.fan().rays()
        N( 1,  1),        N( 1, -1),
        N(-1, -1),        N(-1,  1)
        in 2-d lattice N
        sage: FTV.gens()
        (z0, z1, z2, z3)

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,8])
        sage: FTV.fan().rays()
        N( 1,  1),        N( 1, -1),        N(-1, -1),
        N(-1,  1),        N( 1,  0)
        in 2-d lattice N
        sage: FTV.gens()
        (z0, z1, z2, z3, z8)

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[8,0,2,1,3],
        ....:                           coordinate_names=\'x+\')
        sage: FTV.fan().rays()
        N( 1,  0),        N( 1,  1),        N(-1, -1),
        N( 1, -1),        N(-1,  1)
        in 2-d lattice N
        sage: FTV.gens()
        (x8, x0, x2, x1, x3)

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=\'all\',
        ....:                           coordinate_names="x y Z+")
        sage: FTV.fan().rays()
        N( 1,  1),        N( 1, -1),        N(-1, -1),        N(-1,  1),
        N(-1,  0),        N( 0, -1),        N( 0,  1),        N( 1,  0)
        in 2-d lattice N
        sage: FTV.gens()
        (x, y, Z2, Z3, Z4, Z5, Z7, Z8)

    Note that ``Z6`` is "missing". This is due to the fact that the 6-th point
    of ``square`` is the origin, and all automatically created names have the
    same indices as corresponding points of
    :meth:`~CPRFanoToricVariety_field.Delta_polar`. This is usually very
    convenient, especially if you have to work with several partial
    resolutions of the same Fano toric variety. However, you can change it, if
    you want::

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=\'all\',
        ....:                           coordinate_names="x y Z+",
        ....:                           coordinate_name_indices=list(range(8)))
        sage: FTV.gens()
        (x, y, Z2, Z3, Z4, Z5, Z6, Z7)

    Note that you have to provide indices for *all* variables, including those
    that have "completely custom" names. Again, this is usually convenient,
    because you can add or remove "custom" variables without disturbing too
    much "automatic" ones::

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=\'all\',
        ....:                           coordinate_names="x Z+",
        ....:                           coordinate_name_indices=list(range(8)))
        sage: FTV.gens()
        (x, Z1, Z2, Z3, Z4, Z5, Z6, Z7)

    If you prefer to always start from zero, you will have to shift indices
    accordingly::

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=\'all\',
        ....:                           coordinate_names="x Z+",
        ....:                           coordinate_name_indices=[0] + list(range(7)))
        sage: FTV.gens()
        (x, Z0, Z1, Z2, Z3, Z4, Z5, Z6)

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=\'all\',
        ....:                           coordinate_names="x y Z+",
        ....:                           coordinate_name_indices=[0]*2 + list(range(6)))
        sage: FTV.gens()
        (x, y, Z0, Z1, Z2, Z3, Z4, Z5)

    So you always can get any names you want, somewhat complicated default
    behaviour was designed with the hope that in most cases you will have no
    desire to provide different names.

    Now we will use the possibility to specify initial charts::

        sage: charts = [(0,1), (1,2), (2,3), (3,0)]

    (these charts actually form exactly the face fan of our square) ::

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,4],
        ....:                           charts=charts)
        sage: FTV.fan().rays()
        N( 1,  1),        N( 1, -1),        N(-1, -1),
        N(-1,  1),        N(-1,  0)
        in 2-d lattice N
        sage: [cone.ambient_ray_indices() for cone in FTV.fan()]
        [(0, 1), (1, 2), (2, 4), (3, 4), (0, 3)]

    If charts are wrong, it should be detected::

        sage: bad_charts = charts + [(3,0)]
        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,4],
        ....:                           charts=bad_charts)
        Traceback (most recent call last):
        ...
        ValueError: you have provided 5 cones, but only 4 of them are maximal!
        Use discard_faces=True if you indeed need to construct a fan from these cones.

    These charts are technically correct, they just happened to list one of
    them twice, but it is assumed that such a situation will not happen. It is
    especially important when you try to speed up your code::

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,4],
        ....:                           charts=bad_charts,
        ....:                           check=False)
        Traceback (most recent call last):
        ...
        IndexError: list assignment index out of range

    In this case you still get an error message, but it is harder to figure out
    what is going on. It may also happen that "everything will still work" in
    the sense of not crashing, but work with such an invalid variety may lead to
    mathematically wrong results, so use ``check=False`` carefully!

    Here are some other possible mistakes::

        sage: bad_charts = charts + [(0,2)]
        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,4],
        ....:                           charts=bad_charts)
        Traceback (most recent call last):
        ...
        ValueError: (0, 2) does not form a chart of a subdivision of
        the face fan of 2-d reflexive polytope #14 in 2-d lattice N!

        sage: bad_charts = charts[:-1]
        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,4],
        ....:                           charts=bad_charts)
        Traceback (most recent call last):
        ...
        ValueError: given charts do not form a complete fan!

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[1,2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: all 4 vertices of Delta_polar must be used for coordinates!
        Got: [1, 2, 3, 4]

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,0,1,2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: no repetitions are allowed for coordinate points!
        Got: [0, 0, 1, 2, 3, 4]

        sage: FTV = CPRFanoToricVariety(Delta_polar=square,
        ....:                           coordinate_points=[0,1,2,3,6])
        Traceback (most recent call last):
        ...
        ValueError: the origin (point #6) cannot be used for a coordinate!
        Got: [0, 1, 2, 3, 6]

    Here is a shorthand for defining the toric variety and homogeneous
    coordinates in one go::

        sage: P1xP1.<a,b,c,d> = CPRFanoToricVariety(Delta_polar=diamond)
        sage: (a^2+b^2) * (c+d)
        a^2*c + b^2*c + a^2*d + b^2*d
    '''

class CPRFanoToricVariety_field(ToricVariety_field):
    """
    Construct a CPR-Fano toric variety associated to a reflexive polytope.

    .. WARNING::

        This class does not perform any checks of correctness of input and it
        does assume that the internal structure of the given parameters is
        coordinated in a certain way. Use
        :func:`CPRFanoToricVariety` to construct CPR-Fano toric varieties.

    .. NOTE::

        See documentation of the module
        :mod:`~sage.schemes.toric.fano_variety` for the used
        definitions and supported varieties.

    INPUT:

    - ``Delta_polar`` -- reflexive polytope

    - ``fan`` -- rational polyhedral fan subdividing the face fan of
      ``Delta_polar``

    - ``coordinate_points`` -- list of indices of points of ``Delta_polar``
      used for rays of ``fan``

    - ``point_to_ray`` -- dictionary mapping the index of a coordinate point
      to the index of the corresponding ray

    - ``coordinate_names`` -- names of the variables of the coordinate ring in
      the format accepted by
      :func:`~sage.schemes.toric.variety.normalize_names`

    - ``coordinate_name_indices`` -- indices for indexed variables,
      if ``None``, will be equal to ``coordinate_points``

    - ``base_field`` -- base field of the CPR-Fano toric variety

    OUTPUT: :class:`CPR-Fano toric variety <CPRFanoToricVariety_field>`

    TESTS::

        sage: P1xP1 = CPRFanoToricVariety(
        ....:     Delta_polar=lattice_polytope.cross_polytope(2))
        sage: P1xP1
        2-d CPR-Fano toric variety covered by 4 affine patches
    """
    def __init__(self, Delta_polar, fan, coordinate_points, point_to_ray, coordinate_names, coordinate_name_indices, base_field) -> None:
        """
        See :class:`CPRFanoToricVariety_field` for documentation.

        Use ``CPRFanoToricVariety`` to construct CPR-Fano toric varieties.

        TESTS::

            sage: P1xP1 = CPRFanoToricVariety(
            ....:     Delta_polar=lattice_polytope.cross_polytope(2))
            sage: P1xP1
            2-d CPR-Fano toric variety covered by 4 affine patches
        """
    def anticanonical_hypersurface(self, **kwds):
        '''
        Return an anticanonical hypersurface of ``self``.

        .. NOTE::

            The returned hypersurface may be actually a subscheme of
            **another** CPR-Fano toric variety: if the base field of ``self``
            does not include all of the required names for generic monomial
            coefficients, it will be automatically extended.

        Below `\\Delta` is the reflexive polytope corresponding to ``self``,
        i.e. the fan of ``self`` is a refinement of the normal fan of
        `\\Delta`. This function accepts only keyword parameters.

        INPUT:

        - ``monomial_points`` -- list of integers or a string. A list will be
          interpreted as indices of points of `\\Delta` which should be used
          for monomials of this hypersurface. A string must be one of the
          following descriptions of points of `\\Delta`:

          * "vertices",
          * "vertices+origin",
          * "all",
          * "simplified" (default) -- all points of `\\Delta` except for
            the interior points of facets, this choice corresponds to working
            with the "simplified polynomial moduli space" of anticanonical
            hypersurfaces;

        - ``coefficient_names`` -- names for the monomial coefficients, see
          :func:`~sage.schemes.toric.variety.normalize_names`
          for acceptable formats. If not given, indexed coefficient names will
          be created automatically.

        - ``coefficient_name_indices`` -- list of integers, indices for
          indexed coefficients. If not given, the index of each coefficient
          will coincide with the index of the corresponding point of `\\Delta`.

        - ``coefficients`` -- as an alternative to specifying coefficient
          names and/or indices, you can give the coefficients themselves as
          arbitrary expressions and/or strings. Using strings allows you to
          easily add "parameters": the base field of ``self`` will be extended
          to include all necessary names.

        OUTPUT:

        - an :class:`anticanonical hypersurface <AnticanonicalHypersurface>` of
          ``self`` (with the extended base field, if necessary).

        EXAMPLES:

        We realize the projective plane as a Fano toric variety::

            sage: simplex = LatticePolytope([(1,0), (0,1), (-1,-1)])
            sage: P2 = CPRFanoToricVariety(Delta_polar=simplex)

        Its anticanonical "hypersurface" is a one-dimensional Calabi-Yau
        manifold::

            sage: P2.anticanonical_hypersurface(monomial_points=\'all\')
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 3 affine patches defined by:
              a0*z0^3 + a9*z0^2*z1 + a7*z0*z1^2 + a1*z1^3 + a8*z0^2*z2 + a6*z0*z1*z2
              + a4*z1^2*z2 + a5*z0*z2^2 + a3*z1*z2^2 + a2*z2^3

        In many cases it is sufficient to work with the "simplified polynomial
        moduli space" of anticanonical hypersurfaces::

            sage: P2.anticanonical_hypersurface(monomial_points=\'simplified\')
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 3 affine patches defined by:
              a0*z0^3 + a1*z1^3 + a6*z0*z1*z2 + a2*z2^3

        The mirror family to these hypersurfaces lives inside the Fano toric
        variety obtained using ``simplex`` as ``Delta`` instead of
        ``Delta_polar``::

            sage: FTV = CPRFanoToricVariety(Delta=simplex,
            ....:                           coordinate_points=\'all\')
            sage: FTV.anticanonical_hypersurface(monomial_points=\'simplified\')
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 9 affine patches defined by:
              a2*z2^3*z3^2*z4*z5^2*z8 + a1*z1^3*z3*z4^2*z7^2*z9
              + a3*z0*z1*z2*z3*z4*z5*z7*z8*z9 + a0*z0^3*z5*z7*z8^2*z9^2

        Here we have taken the resolved version of the ambient space for the
        mirror family, but in fact we don\'t have to resolve singularities
        corresponding to the interior points of facets - they are singular
        points which do not lie on a generic anticanonical hypersurface::

            sage: FTV = CPRFanoToricVariety(Delta=simplex,
            ....:                           coordinate_points="all but facets")
            sage: FTV.anticanonical_hypersurface(monomial_points=\'simplified\')
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 3 affine patches defined by:
              a0*z0^3 + a1*z1^3 + a3*z0*z1*z2 + a2*z2^3

        This looks very similar to our second anticanonical
        hypersurface of the projective plane, as expected, since all
        one-dimensional Calabi-Yau manifolds are elliptic curves!

        All anticanonical hypersurfaces constructed above were generic with
        automatically generated coefficients. If you want, you can specify your
        own names ::

            sage: FTV.anticanonical_hypersurface(coefficient_names="a b c d")
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 3 affine patches defined by:
              a*z0^3 + b*z1^3 + d*z0*z1*z2 + c*z2^3

        or give concrete coefficients ::

            sage: FTV.anticanonical_hypersurface(coefficients=[1, 2, 3, 4])
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 3 affine patches defined by:
              z0^3 + 2*z1^3 + 4*z0*z1*z2 + 3*z2^3

        or even mix numerical coefficients with some expressions ::

            sage: H = FTV.anticanonical_hypersurface(
            ....:   coefficients=[0, "t", "1/t", "psi/(psi^2 + phi)"])
            sage: H
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 3 affine patches defined by:
              t*z1^3 + psi/(phi + psi^2)*z0*z1*z2 + 1/t*z2^3
            sage: R = H.ambient_space().base_ring()
            sage: R
            Fraction Field of
             Multivariate Polynomial Ring in phi, psi, t over Rational Field
        '''
    def change_ring(self, F):
        """
        Return a CPR-Fano toric variety over field ``F``, otherwise the same
        as ``self``.

        INPUT:

        - ``F`` -- field

        OUTPUT: :class:`CPR-Fano toric variety <CPRFanoToricVariety_field>` over ``F``

        .. NOTE::

            There is no need to have any relation between ``F`` and the base
            field of ``self``. If you do want to have such a relation, use
            :meth:`base_extend` instead.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.base_ring()
            Rational Field
            sage: P1xP1_RR = P1xP1.change_ring(RR)
            sage: P1xP1_RR.base_ring()
            Real Field with 53 bits of precision
            sage: P1xP1_QQ = P1xP1_RR.change_ring(QQ)
            sage: P1xP1_QQ.base_ring()
            Rational Field
            sage: P1xP1_RR.base_extend(QQ)
            Traceback (most recent call last):
            ...
            ValueError: no natural map from the base ring
            (=Real Field with 53 bits of precision) to R (=Rational Field)!
            sage: R = PolynomialRing(QQ, 2, 'a')
            sage: P1xP1.change_ring(R)
            Traceback (most recent call last):
            ...
            TypeError: need a field to construct a Fano toric variety!
            Got Multivariate Polynomial Ring in a0, a1 over Rational Field
        """
    def coordinate_point_to_coordinate(self, point):
        """
        Return the variable of the coordinate ring corresponding to ``point``.

        INPUT:

        - ``point`` -- integer from the list of :meth:`coordinate_points`

        OUTPUT: the corresponding generator of the coordinate ring of ``self``

        EXAMPLES::

            sage: diamond = lattice_polytope.cross_polytope(2)
            sage: FTV = CPRFanoToricVariety(diamond, coordinate_points=[0,1,2,3,8])
            sage: FTV.coordinate_points()
            (0, 1, 2, 3, 8)
            sage: FTV.gens()
            (z0, z1, z2, z3, z8)
            sage: FTV.coordinate_point_to_coordinate(8)
            z8
        """
    def coordinate_points(self):
        """
        Return indices of points of :meth:`Delta_polar` used for coordinates.

        OUTPUT: :class:`tuple` of integers

        EXAMPLES::

            sage: diamond = lattice_polytope.cross_polytope(2)
            sage: square = diamond.polar()
            sage: FTV = CPRFanoToricVariety(Delta_polar=square,
            ....:                           coordinate_points=[0,1,2,3,8])
            sage: FTV.coordinate_points()
            (0, 1, 2, 3, 8)
            sage: FTV.gens()
            (z0, z1, z2, z3, z8)

            sage: FTV = CPRFanoToricVariety(Delta_polar=square,
            ....:                           coordinate_points='all')
            sage: FTV.coordinate_points()
            (0, 1, 2, 3, 4, 5, 7, 8)
            sage: FTV.gens()
            (z0, z1, z2, z3, z4, z5, z7, z8)

        Note that one point is missing, namely ::

            sage: square.origin()
            6
        """
    def Delta(self):
        """
        Return the reflexive polytope associated to ``self``.

        OUTPUT:

        - reflexive :class:`lattice polytope
          <sage.geometry.lattice_polytope.LatticePolytopeClass>`. The
          underlying fan of ``self`` is a coherent subdivision of the
          *normal fan* of this polytope.

        EXAMPLES::

            sage: diamond = lattice_polytope.cross_polytope(2)
            sage: P1xP1 = CPRFanoToricVariety(Delta_polar=diamond)
            sage: P1xP1.Delta()
            2-d reflexive polytope #14 in 2-d lattice N
            sage: P1xP1.Delta() is diamond.polar()
            True
        """
    def Delta_polar(self):
        """
        Return polar of :meth:`Delta`.

        OUTPUT:

        - reflexive :class:`lattice polytope
          <sage.geometry.lattice_polytope.LatticePolytopeClass>`. The
          underlying fan of ``self`` is a coherent subdivision of the
          *face fan* of this polytope.

        EXAMPLES::

            sage: diamond = lattice_polytope.cross_polytope(2)
            sage: P1xP1 = CPRFanoToricVariety(Delta_polar=diamond)
            sage: P1xP1.Delta_polar()
            2-d reflexive polytope #3 in 2-d lattice M
            sage: P1xP1.Delta_polar() is diamond
            True
            sage: P1xP1.Delta_polar() is P1xP1.Delta().polar()
            True
        """
    def nef_complete_intersection(self, nef_partition, **kwds):
        '''
        Return a nef complete intersection in ``self``.

        .. NOTE::

            The returned complete intersection may be actually a subscheme of
            **another** CPR-Fano toric variety: if the base field of ``self``
            does not include all of the required names for monomial
            coefficients, it will be automatically extended.

        Below `\\Delta` is the reflexive polytope corresponding to ``self``,
        i.e. the fan of ``self`` is a refinement of the normal fan of
        `\\Delta`. Other polytopes are described in the documentation of
        :class:`nef-partitions <sage.geometry.lattice_polytope.NefPartition>`
        of :class:`reflexive polytopes
        <sage.geometry.lattice_polytope.LatticePolytopeClass>`.

        Except for the first argument, ``nef_partition``, this method accepts
        only keyword parameters.

        INPUT:

        - ``nef_partition`` -- a `k`-part :class:`nef-partition
          <sage.geometry.lattice_polytope.NefPartition>` of `\\Delta^\\circ`, all
          other parameters (if given) must be lists of length `k`

        - ``monomial_points`` -- the `i`-th element of this list is either a
          list of integers or a string. A list will be interpreted as indices
          of points of `\\Delta_i` which should be used for monomials of the
          `i`-th polynomial of this complete intersection. A string must be one
          of the following descriptions of points of `\\Delta_i`:

          * "vertices",
          * "vertices+origin",
          * "all" (default),

          when using this description, it is also OK to pass a single string as
          ``monomial_points`` instead of repeating it `k` times.

        - ``coefficient_names`` -- the `i`-th element of this list specifies
          names for the monomial coefficients of the `i`-th polynomial, see
          :func:`~sage.schemes.toric.variety.normalize_names`
          for acceptable formats. If not given, indexed coefficient names will
          be created automatically.

        - ``coefficient_name_indices`` -- the `i`-th element of this list
          specifies indices for indexed coefficients of the `i`-th polynomial.
          If not given, the index of each coefficient will coincide with the
          index of the corresponding point of `\\Delta_i`.

        - ``coefficients`` -- as an alternative to specifying coefficient
          names and/or indices, you can give the coefficients themselves as
          arbitrary expressions and/or strings. Using strings allows you to
          easily add "parameters": the base field of ``self`` will be extended
          to include all necessary names.

        OUTPUT:

        - a :class:`nef complete intersection <NefCompleteIntersection>` of
          ``self`` (with the extended base field, if necessary).

        EXAMPLES:

        We construct several complete intersections associated to the same
        nef-partition of the 3-dimensional reflexive polytope #2254::

            sage: p = ReflexivePolytope(3, 2254)
            sage: np = p.nef_partitions()[1]; np
            Nef-partition {2, 3, 4, 7, 8} ⊔ {0, 1, 5, 6}
            sage: X = CPRFanoToricVariety(Delta_polar=p)
            sage: X.nef_complete_intersection(np)
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 10 affine patches defined by:
              a0*z1*z4^2*z5^2*z7^3 + a2*z2*z4*z5*z6*z7^2*z8^2
              + a3*z2*z3*z4*z7*z8 + a1*z0*z2,
              b3*z1*z4*z5^2*z6^2*z7^2*z8^2 + b0*z2*z5*z6^3*z7*z8^4
              + b5*z1*z3*z4*z5*z6*z7*z8 + b2*z2*z3*z6^2*z8^3
              + b1*z1*z3^2*z4 + b4*z0*z1*z5*z6

        Now we include only monomials associated to vertices of `\\Delta_i`::

            sage: X.nef_complete_intersection(np, monomial_points=\'vertices\')
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 10 affine patches defined by:
              a0*z1*z4^2*z5^2*z7^3 + a2*z2*z4*z5*z6*z7^2*z8^2
              + a3*z2*z3*z4*z7*z8 + a1*z0*z2,
              b3*z1*z4*z5^2*z6^2*z7^2*z8^2 + b0*z2*z5*z6^3*z7*z8^4
              + b2*z2*z3*z6^2*z8^3 + b1*z1*z3^2*z4 + b4*z0*z1*z5*z6

        (effectively, we set ``b5=0``). Next we provide coefficients explicitly
        instead of using default generic names::

            sage: X.nef_complete_intersection(np,
            ....:       monomial_points=\'vertices\',
            ....:       coefficients=[("a", "a^2", "a/e", "c_i"), list(range(1,6))])
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 10 affine patches defined by:
              a*z1*z4^2*z5^2*z7^3 + a/e*z2*z4*z5*z6*z7^2*z8^2
              + (c_i)*z2*z3*z4*z7*z8 + (a^2)*z0*z2,
              4*z1*z4*z5^2*z6^2*z7^2*z8^2 + z2*z5*z6^3*z7*z8^4
              + 3*z2*z3*z6^2*z8^3 + 2*z1*z3^2*z4 + 5*z0*z1*z5*z6

        Finally, we take a look at the generic representative of these complete
        intersections in a completely resolved ambient toric variety::

            sage: X = CPRFanoToricVariety(Delta_polar=p,
            ....:                         coordinate_points=\'all\')
            sage: X.nef_complete_intersection(np)
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 22 affine patches defined by:
              a2*z2*z4*z5*z6*z7^2*z8^2*z9^2*z10^2*z11*z12*z13
              + a0*z1*z4^2*z5^2*z7^3*z9*z10^2*z12*z13
              + a3*z2*z3*z4*z7*z8*z9*z10*z11*z12 + a1*z0*z2,
              b0*z2*z5*z6^3*z7*z8^4*z9^3*z10^2*z11^2*z12*z13^2
              + b3*z1*z4*z5^2*z6^2*z7^2*z8^2*z9^2*z10^2*z11*z12*z13^2
              + b2*z2*z3*z6^2*z8^3*z9^2*z10*z11^2*z12*z13
              + b5*z1*z3*z4*z5*z6*z7*z8*z9*z10*z11*z12*z13
              + b1*z1*z3^2*z4*z11*z12 + b4*z0*z1*z5*z6*z13
        '''
    def cartesian_product(self, other, coordinate_names=None, coordinate_indices=None):
        """
        Return the Cartesian product of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a (possibly
          :class:`CPR-Fano <CPRFanoToricVariety_field>`) :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>`

        - ``coordinate_names`` -- names of variables for the coordinate ring,
          see :func:`normalize_names` for acceptable formats. If not given,
          indexed variable names will be created automatically.

        - ``coordinate_indices`` -- list of integers, indices for indexed
          variables. If not given, the index of each variable will coincide
          with the index of the corresponding ray of the fan.

        OUTPUT:

        - a :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>`, which is
          :class:`CPR-Fano <CPRFanoToricVariety_field>` if ``other`` was.

        EXAMPLES::

            sage: P1 = toric_varieties.P1()
            sage: P2 = toric_varieties.P2()
            sage: P1xP2 = P1.cartesian_product(P2); P1xP2
            3-d CPR-Fano toric variety covered by 6 affine patches
            sage: P1xP2.fan().rays()
            N+N( 1,  0,  0),        N+N(-1,  0,  0),        N+N( 0,  1,  0),
            N+N( 0,  0,  1),        N+N( 0, -1, -1)
            in 3-d lattice N+N
            sage: P1xP2.Delta_polar()
            3-d reflexive polytope in 3-d lattice N+N
        """
    def resolve(self, **kwds):
        """
        Construct a toric variety whose fan subdivides the fan of ``self``.

        This function accepts only keyword arguments, none of which are
        mandatory.

        INPUT:

        - ``new_points`` -- list of integers, indices of boundary points of
          :meth:`Delta_polar`, which should be added as rays to the
          subdividing fan

        - all other arguments will be passed to
          :meth:`~sage.schemes.toric.variety.ToricVariety_field.resolve`
          method of (general) toric varieties; see its documentation for
          details

        OUTPUT:

        - :class:`CPR-Fano toric variety <CPRFanoToricVariety_field>` if there
          was no ``new_rays`` argument and :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>` otherwise.

        EXAMPLES::

            sage: diamond = lattice_polytope.cross_polytope(2)
            sage: FTV = CPRFanoToricVariety(Delta=diamond)
            sage: FTV.coordinate_points()
            (0, 1, 2, 3)
            sage: FTV.gens()
            (z0, z1, z2, z3)
            sage: FTV_res = FTV.resolve(new_points=[6,8])
            Traceback (most recent call last):
            ...
            ValueError: the origin (point #6)
            cannot be used for subdivision!
            sage: FTV_res = FTV.resolve(new_points=[8,5]); FTV_res
            2-d CPR-Fano toric variety covered by 6 affine patches
            sage: FTV_res.coordinate_points()
            (0, 1, 2, 3, 8, 5)
            sage: FTV_res.gens()
            (z0, z1, z2, z3, z8, z5)

            sage: TV_res = FTV.resolve(new_rays=[(1,2)]); TV_res
            2-d toric variety covered by 5 affine patches
            sage: TV_res.gens()
            (z0, z1, z2, z3, z4)
        """

class AnticanonicalHypersurface(AlgebraicScheme_subscheme_toric):
    """
    Construct an anticanonical hypersurface of a CPR-Fano toric variety.

    INPUT:

    - ``P_Delta`` -- :class:`CPR-Fano toric variety
      <CPRFanoToricVariety_field>` associated to a reflexive polytope `\\Delta`

    - see :meth:`CPRFanoToricVariety_field.anticanonical_hypersurface` for
      documentation on all other acceptable parameters

    OUTPUT:

    :class:`anticanonical hypersurface <AnticanonicalHypersurface>` of
    ``P_Delta`` (with the extended base field, if necessary).

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: import sage.schemes.toric.fano_variety as ftv
        sage: ftv.AnticanonicalHypersurface(P1xP1)
        Closed subscheme of 2-d CPR-Fano toric variety
         covered by 4 affine patches defined by:
          a0*s^2*x^2 + a3*t^2*x^2 + a6*s*t*x*y + a1*s^2*y^2 + a2*t^2*y^2

    See :meth:`~CPRFanoToricVariety_field.anticanonical_hypersurface()` for a
    more elaborate example.
    """
    def __init__(self, P_Delta, monomial_points=None, coefficient_names=None, coefficient_name_indices=None, coefficients=None) -> None:
        '''
        See :meth:`CPRFanoToricVariety_field.anticanonical_hypersurface` for
        documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: import sage.schemes.toric.fano_variety as ftv
            sage: ftv.AnticanonicalHypersurface(P1xP1)
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 4 affine patches defined by:
              a0*s^2*x^2 + a3*t^2*x^2 + a6*s*t*x*y + a1*s^2*y^2 + a2*t^2*y^2

        Check that finite fields are handled correctly :issue:`14899`::

            sage: F = GF(5^2, "a")                                                      # needs sage.rings.finite_rings
            sage: X = P1xP1.change_ring(F)                                              # needs sage.rings.finite_rings
            sage: X.anticanonical_hypersurface(monomial_points=\'all\',                   # needs sage.rings.finite_rings
            ....:                   coefficients=[1]*X.Delta().npoints())
            Closed subscheme of 2-d CPR-Fano toric variety
             covered by 4 affine patches defined by:
              s^2*x^2 + s*t*x^2 + t^2*x^2 + s^2*x*y + s*t*x*y
              + t^2*x*y + s^2*y^2 + s*t*y^2 + t^2*y^2
        '''

class NefCompleteIntersection(AlgebraicScheme_subscheme_toric):
    """
    Construct a nef complete intersection in a CPR-Fano toric variety.

    INPUT:

    - ``P_Delta`` -- a :class:`CPR-Fano toric variety
      <CPRFanoToricVariety_field>` associated to a reflexive polytope `\\Delta`

    - see :meth:`CPRFanoToricVariety_field.nef_complete_intersection` for
      documentation on all other acceptable parameters

    OUTPUT:

    - a :class:`nef complete intersection <NefCompleteIntersection>` of
      ``P_Delta`` (with the extended base field, if necessary).

    EXAMPLES::

        sage: o = lattice_polytope.cross_polytope(3)
        sage: np = o.nef_partitions()[0]; np
        Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
        sage: X = CPRFanoToricVariety(Delta_polar=o)
        sage: X.nef_complete_intersection(np)
        Closed subscheme of 3-d CPR-Fano toric variety
         covered by 8 affine patches defined by:
          a2*z0^2*z1 + a5*z0*z1*z3 + a1*z1*z3^2 + a3*z0^2*z4 + a4*z0*z3*z4 + a0*z3^2*z4,
          b1*z1*z2^2 + b2*z2^2*z4 + b5*z1*z2*z5 + b4*z2*z4*z5 + b3*z1*z5^2 + b0*z4*z5^2

    See :meth:`CPRFanoToricVariety_field.nef_complete_intersection` for a
    more elaborate example.
    """
    def __init__(self, P_Delta, nef_partition, monomial_points: str = 'all', coefficient_names=None, coefficient_name_indices=None, coefficients=None) -> None:
        """
        See :meth:`CPRFanoToricVariety_field.nef_complete_intersection` for
        documentation.

        TESTS::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = o.nef_partitions()[0]
            sage: np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: X = CPRFanoToricVariety(Delta_polar=o)
            sage: from sage.schemes.toric.fano_variety import *
            sage: NefCompleteIntersection(X, np)
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 8 affine patches defined by:
              a2*z0^2*z1 + a5*z0*z1*z3 + a1*z1*z3^2
              + a3*z0^2*z4 + a4*z0*z3*z4 + a0*z3^2*z4,
              b1*z1*z2^2 + b2*z2^2*z4 + b5*z1*z2*z5
              + b4*z2*z4*z5 + b3*z1*z5^2 + b0*z4*z5^2
        """
    def cohomology_class(self):
        """
        Return the class of ``self`` in the ambient space cohomology ring.

        OUTPUT: a :class:`cohomology class <sage.schemes.generic.toric_variety.CohomologyClass>`

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = o.nef_partitions()[0]; np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: X = CPRFanoToricVariety(Delta_polar=o)
            sage: CI = X.nef_complete_intersection(np); CI
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 8 affine patches defined by:
              a2*z0^2*z1 + a5*z0*z1*z3 + a1*z1*z3^2 + a3*z0^2*z4 + a4*z0*z3*z4 + a0*z3^2*z4,
              b1*z1*z2^2 + b2*z2^2*z4 + b5*z1*z2*z5 + b4*z2*z4*z5 + b3*z1*z5^2 + b0*z4*z5^2
            sage: CI.cohomology_class()                                                 # needs sage.libs.singular
            [2*z3*z4 + 4*z3*z5 + 2*z4*z5]
        """
    def nef_partition(self):
        """
        Return the nef-partition associated to ``self``.

        OUTPUT: a :class:`nef-partition <sage.geometry.lattice_polytope.NefPartition>`

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: np = o.nef_partitions()[0]; np
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: X = CPRFanoToricVariety(Delta_polar=o)
            sage: CI = X.nef_complete_intersection(np); CI
            Closed subscheme of 3-d CPR-Fano toric variety
             covered by 8 affine patches defined by:
              a2*z0^2*z1 + a5*z0*z1*z3 + a1*z1*z3^2 + a3*z0^2*z4 + a4*z0*z3*z4 + a0*z3^2*z4,
              b1*z1*z2^2 + b2*z2^2*z4 + b5*z1*z2*z5 + b4*z2*z4*z5 + b3*z1*z5^2 + b0*z4*z5^2
            sage: CI.nef_partition()
            Nef-partition {0, 1, 3} ⊔ {2, 4, 5}
            sage: CI.nef_partition() is np
            True
        """

def add_variables(field, variables):
    '''
    Extend ``field`` to include all ``variables``.

    INPUT:

    - ``field`` -- a field

    - ``variables`` -- list of strings

    OUTPUT:

    - a fraction field extending the original ``field``, which has all
      ``variables`` among its generators.

    EXAMPLES:

    We start with the rational field and slowly add more variables::

        sage: from sage.schemes.toric.fano_variety import *
        sage: F = add_variables(QQ, []); F      # No extension
        Rational Field
        sage: F = add_variables(QQ, ["a"]); F
        Fraction Field of Univariate Polynomial Ring in a over Rational Field
        sage: F = add_variables(F, ["a"]); F
        Fraction Field of Univariate Polynomial Ring in a over Rational Field
        sage: F = add_variables(F, ["b", "c"]); F
        Fraction Field of Multivariate Polynomial Ring in a, b, c over Rational Field
        sage: F = add_variables(F, ["c", "d", "b", "c", "d"]); F
        Fraction Field of Multivariate Polynomial Ring in a, b, c, d over Rational Field
    '''
