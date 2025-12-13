from sage.categories.fields import Fields as Fields
from sage.geometry.cone import Cone as Cone
from sage.geometry.fan import Fan as Fan
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.rings.quotient_ring_element import QuotientRingElement as QuotientRingElement
from sage.rings.rational_field import QQ as QQ
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace
from sage.schemes.generic.ambient_space import AmbientSpace as AmbientSpace
from sage.schemes.toric.homset import SchemeHomset_points_toric_field as SchemeHomset_points_toric_field
from sage.structure.category_object import certify_names as certify_names
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

DEFAULT_PREFIX: str

def is_ToricVariety(x):
    """
    Check if ``x`` is a toric variety.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    - ``True`` if ``x`` is a :class:`toric variety <ToricVariety_field>` and
      ``False`` otherwise.

    .. NOTE::

        While projective spaces are toric varieties mathematically, they are
        not toric varieties in Sage due to efficiency considerations, so this
        function will return ``False``.

    EXAMPLES::

        sage: from sage.schemes.toric.variety import is_ToricVariety
        sage: is_ToricVariety(1)
        doctest:warning...
        DeprecationWarning: The function is_ToricVariety is deprecated; use 'isinstance(..., ToricVariety_field)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        False
        sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
        sage: P = ToricVariety(fan)
        sage: P
        2-d toric variety covered by 4 affine patches
        sage: is_ToricVariety(P)
        True
        sage: is_ToricVariety(ProjectiveSpace(2))
        False
    """
def ToricVariety(fan, coordinate_names=None, names=None, coordinate_indices=None, base_ring=..., base_field=None):
    '''
    Construct a toric variety.

    INPUT:

    - ``fan`` -- :class:`rational polyhedral fan
      <sage.geometry.fan.RationalPolyhedralFan>`

    - ``coordinate_names`` -- names of variables for the coordinate ring, see
      :func:`normalize_names` for acceptable formats. If not given, indexed
      variable names will be created automatically.

    - ``names`` -- an alias of ``coordinate_names`` for internal
      use. You may specify either ``names`` or ``coordinate_names``,
      but not both.

    - ``coordinate_indices`` -- list of integers, indices for indexed
      variables. If not given, the index of each variable will coincide with
      the index of the corresponding ray of the fan.

    - ``base_ring`` -- base ring of the toric variety (default:
      `\\QQ`); must be a field

    - ``base_field`` -- alias for ``base_ring``; takes precedence if
      both are specified

    OUTPUT: a :class:`toric variety <ToricVariety_field>`

    EXAMPLES:

    We will create the product of two projective lines::

        sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
        sage: fan.rays()
        M( 1,  0),    M( 0,  1),
        M(-1,  0),    M( 0, -1)
        in 2-d lattice M
        sage: P1xP1 = ToricVariety(fan)
        sage: P1xP1.gens()
        (z0, z1, z2, z3)

    Let\'s create some points::

        sage: P1xP1(1,1,1,1)
        [1 : 1 : 1 : 1]
        sage: P1xP1(0,1,1,1)
        [0 : 1 : 1 : 1]
        sage: P1xP1(0,1,0,1)
        Traceback (most recent call last):
        ...
        TypeError: coordinates (0, 1, 0, 1) are in the exceptional set

    We cannot set to zero both coordinates of the same projective line!

    Let\'s change the names of the variables. We have to re-create our toric
    variety::

        sage: P1xP1 = ToricVariety(fan, "x s y t")
        sage: P1xP1.gens()
        (x, s, y, t)

    Now `(x, y)` correspond to one line and `(s, t)` to the other one. ::

        sage: P1xP1.inject_variables()
        Defining x, s, y, t
        sage: P1xP1.subscheme(x*s - y*t)
        Closed subscheme of 2-d toric variety covered by 4 affine patches defined by:
          x*s - y*t

    Here is a shorthand for defining the toric variety and homogeneous
    coordinates in one go::

        sage: P1xP1.<a,b,c,d> = ToricVariety(fan)
        sage: (a^2+b^2) * (c+d)
        a^2*c + b^2*c + a^2*d + b^2*d
    '''
def AffineToricVariety(cone, *args, **kwds):
    """
    Construct an affine toric variety.

    INPUT:

    - ``cone`` -- :class:`strictly convex rational polyhedral cone
      <sage.geometry.cone.ConvexRationalPolyhedralCone>`

    This cone will be used to construct a :class:`rational polyhedral fan
    <sage.geometry.fan.RationalPolyhedralFan>`, which will be passed to
    :func:`ToricVariety` with the rest of positional and keyword arguments.

    OUTPUT: a :class:`toric variety <ToricVariety_field>`

    .. NOTE::

        The generating rays of the fan of this variety are guaranteed to be
        listed in the same order as the rays of the original cone.

    EXAMPLES:

    We will create the affine plane as an affine toric variety::

        sage: quadrant = Cone([(1,0), (0,1)])
        sage: A2 = AffineToricVariety(quadrant)
        sage: origin = A2(0,0)
        sage: origin
        [0 : 0]
        sage: parent(origin)
        Set of rational points of 2-d affine toric variety

    Only affine toric varieties have points whose (homogeneous) coordinates
    are all zero.
    """

class ToricVariety_field(AmbientSpace):
    """
    Construct a toric variety associated to a rational polyhedral fan.

    .. WARNING::

        This class does not perform any checks of correctness of input. Use
        :func:`ToricVariety` and :func:`AffineToricVariety` to construct toric
        varieties.

    INPUT:

    - ``fan`` -- :class:`rational polyhedral fan
      <sage.geometry.fan.RationalPolyhedralFan>`

    - ``coordinate_names`` -- names of variables, see :func:`normalize_names`
      for acceptable formats. If ``None``, indexed variable names will be
      created automatically.

    - ``coordinate_indices`` -- list of integers, indices for indexed
      variables. If ``None``, the index of each variable will coincide with
      the index of the corresponding ray of the fan.

    - ``base_field`` -- base field of the toric variety

    OUTPUT: a :class:`toric variety <ToricVariety_field>`

    TESTS::

        sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
        sage: P1xP1 = ToricVariety(fan)
    """
    def __init__(self, fan, coordinate_names, coordinate_indices, base_field) -> None:
        """
        See :class:`ToricVariety_field` for documentation.

        TESTS::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan)
        """
    def __eq__(self, right):
        '''
        Check equality of ``self`` and ``right``.

        INPUT:

        - ``right`` -- anything

        OUTPUT: boolean

        ``True`` if and only if ``right`` is of the same type as ``self``,
        their fans are the same, names of variables are the same and
        stored in the same order, and base fields are the same.

        TESTS::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan)
            sage: P1xP1a = ToricVariety(fan, "x s y t")
            sage: P1xP1b = ToricVariety(fan)

            sage: P1xP1 == P1xP1a
            False
            sage: P1xP1a == P1xP1
            False
            sage: P1xP1 == P1xP1b
            True
            sage: P1xP1 is P1xP1b
            False
        '''
    def __ne__(self, other):
        '''
        Check not-equality of ``self`` and ``other``.

        INPUT:

        - ``other`` -- anything

        OUTPUT: boolean

        ``True`` if and only if ``other`` is of the same type as ``self``,
        their fans are the same, names of variables are the same and
        stored in the same order, and base fields are the same.

        TESTS::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan)
            sage: P1xP1a = ToricVariety(fan, "x s y t")
            sage: P1xP1b = ToricVariety(fan)

            sage: P1xP1 != P1xP1a
            True
            sage: P1xP1a != P1xP1
            True
            sage: P1xP1 != P1xP1b
            False
        '''
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan)
            sage: h1 = hash(P1xP1)
            sage: h2 = hash(P1xP1)
            sage: h3 = hash(toric_varieties.P(2))
            sage: h1 == h2 and h1 != h3
            True
        """
    def affine_patch(self, i):
        '''
        Return the ``i``-th affine patch of ``self``.

        INPUT:

        - ``i`` -- integer; index of a generating cone of the fan of ``self``

        OUTPUT:

        - affine :class:`toric variety <ToricVariety_field>` corresponding to
          the ``i``-th generating cone of the fan of ``self``.

        The result is cached, so the ``i``-th patch is always the same object
        in memory.

        See also :meth:`affine_algebraic_patch`, which expresses the
        patches as subvarieties of affine space instead.

        EXAMPLES::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan, "x s y t")
            sage: patch0 = P1xP1.affine_patch(0)
            sage: patch0
            2-d affine toric variety
            sage: patch0.embedding_morphism()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [y : t] to [1 : 1 : y : t]
            sage: patch1 = P1xP1.affine_patch(1)
            sage: patch1.embedding_morphism()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [s : y] to [1 : s : y : 1]
            sage: patch1 is P1xP1.affine_patch(1)
            True
        '''
    def change_ring(self, F):
        """
        Return a toric variety over ``F`` and otherwise the same as ``self``.

        INPUT:

        - ``F`` -- field

        OUTPUT: :class:`toric variety <ToricVariety_field>` over ``F``

        .. NOTE::

            There is no need to have any relation between ``F`` and the base
            field of ``self``. If you do want to have such a relation, use
            :meth:`base_extend` instead.

        EXAMPLES::

            sage: P1xA1 = toric_varieties.P1xA1()
            sage: P1xA1.base_ring()
            Rational Field
            sage: P1xA1_RR = P1xA1.change_ring(RR)
            sage: P1xA1_RR.base_ring()
            Real Field with 53 bits of precision
            sage: P1xA1_QQ = P1xA1_RR.change_ring(QQ)
            sage: P1xA1_QQ.base_ring()
            Rational Field
            sage: P1xA1_RR.base_extend(QQ)
            Traceback (most recent call last):
            ...
            ValueError: no natural map from the base ring
            (=Real Field with 53 bits of precision) to R (=Rational Field)!
            sage: R = PolynomialRing(QQ, 2, 'a')
            sage: P1xA1.change_ring(R)
            Traceback (most recent call last):
            ...
            TypeError: need a field to construct a toric variety;
            got Multivariate Polynomial Ring in a0, a1 over Rational Field
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring of ``self``.

        For toric varieties this is the homogeneous coordinate ring (a.k.a.
        Cox's ring and total ring).

        OUTPUT: a polynomial ring

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.coordinate_ring()
            Multivariate Polynomial Ring in s, t, x, y over Rational Field

        TESTS::

            sage: R = toric_varieties.A1().coordinate_ring();  R
            Multivariate Polynomial Ring in z over Rational Field
            sage: type(R)                                                               # needs sage.libs.singular
            <... 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>
        """
    def embedding_morphism(self):
        '''
        Return the default embedding morphism of ``self``.

        Such a morphism is always defined for an affine patch of a toric
        variety (which is also a toric varieties itself).

        OUTPUT:

        - :class:`scheme morphism
          <sage.schemes.generic.morphism.SchemeMorphism_polynomial_toric_variety>`
          if the default embedding morphism was defined for ``self``,
          otherwise a :exc:`ValueError` exception is raised.

        EXAMPLES::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan, "x s y t")
            sage: P1xP1.embedding_morphism()
            Traceback (most recent call last):
            ...
            ValueError: no default embedding was defined for this toric variety
            sage: patch = P1xP1.affine_patch(0)
            sage: patch
            2-d affine toric variety
            sage: patch.embedding_morphism()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [y : t] to [1 : 1 : y : t]
        '''
    def fan(self, dim=None, codim=None):
        """
        Return the underlying fan of ``self`` or its cones.

        INPUT:

        - ``dim`` -- dimension of the requested cones

        - ``codim`` -- codimension of the requested cones

        OUTPUT:

        - :class:`rational polyhedral fan
          <sage.geometry.fan.RationalPolyhedralFan>` if no parameters were
          given, :class:`tuple` of :class:`cones
          <sage.geometry.cone.ConvexRationalPolyhedralCone>` otherwise.

        EXAMPLES::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan)
            sage: P1xP1.fan()
            Rational polyhedral fan in 2-d lattice M
            sage: P1xP1.fan() is fan
            True
            sage: P1xP1.fan(1)[0]
            1-d cone of Rational polyhedral fan in 2-d lattice M
        """
    def inject_coefficients(self, scope=None, verbose: bool = True) -> None:
        '''
        Inject generators of the base field of ``self`` into ``scope``.

        This function is useful if the base field is the field of rational
        functions.

        INPUT:

        - ``scope`` -- namespace (default: global, not just the scope from
          which this function was called)

        - ``verbose`` -- if ``True`` (default), names of injected generators
          will be printed

        OUTPUT: none

        EXAMPLES::

            sage: fan = FaceFan(lattice_polytope.cross_polytope(2))
            sage: F = QQ["a, b"].fraction_field()
            sage: P1xP1 = ToricVariety(fan, base_field=F)
            sage: P1xP1.inject_coefficients()
            Defining a, b

        We check that we can use names ``a`` and ``b``, :issue:`10498` is fixed::

            sage: a + b
            a + b
            sage: a + b in P1xP1.coordinate_ring()
            True
        '''
    @cached_method
    def dimension_singularities(self):
        """
        Return the dimension of the singular set.

        OUTPUT:

        Integer. The dimension of the singular set of the toric
        variety. Often the singular set is a reducible subvariety, and
        this method will return the dimension of the
        largest-dimensional component.

        This returns `-1` if the toric variety is smooth.

        EXAMPLES::

            sage: toric_varieties.P4_11169().dimension_singularities()
            1
            sage: toric_varieties.Conifold().dimension_singularities()
            0
            sage: toric_varieties.P2().dimension_singularities()
            -1
        """
    def is_homogeneous(self, polynomial):
        """
        Check if ``polynomial`` is homogeneous.

        The coordinate ring of a toric variety is multigraded by relations
        between generating rays of the underlying fan.

        INPUT:

        - ``polynomial`` -- polynomial in the coordinate ring of ``self`` or
          its quotient

        OUTPUT: ``True`` if ``polynomial`` is homogeneous and ``False`` otherwise

        EXAMPLES:

        We will use the product of two projective lines with coordinates
        `(x, y)` for one and `(s, t)` for the other::

            sage: P1xP1.<x,y,s,t> = toric_varieties.P1xP1()
            sage: P1xP1.is_homogeneous(x - y)
            True
            sage: P1xP1.is_homogeneous(x*s + y*t)
            True
            sage: P1xP1.is_homogeneous(x - t)
            False
            sage: P1xP1.is_homogeneous(1)
            True

        Note that by homogeneous, we mean well-defined with respect to
        the homogeneous rescalings of ``self``. So a polynomial that you would
        usually not call homogeneous can be homogeneous if there are
        no homogeneous rescalings, for example::

            sage: A1.<z> = toric_varieties.A1()
            sage: A1.is_homogeneous(z^3 + z^7)
            True

        Finally, the degree group is really the Chow group
        `A_{d-1}(X)` and can contain torsion. For example, take
        `\\CC^2/\\ZZ_2`. Here, the Chow group is `A_{d-1}(\\CC^2/\\ZZ_2) =
        \\ZZ_2` and distinguishes even-degree homogeneous polynomials
        from odd-degree homogeneous polynomials::

            sage: A2_Z2.<x,y> = toric_varieties.A2_Z2()
            sage: A2_Z2.is_homogeneous(x + y + x^3 + y^5 + x^3*y^4)
            True
            sage: A2_Z2.is_homogeneous(x^2 + x*y + y^4 + (x*y)^5 + x^4*y^4)
            True
            sage: A2_Z2.is_homogeneous(x + y^2)
            False
        """
    def is_isomorphic(self, another):
        """
        Check if ``self`` is isomorphic to ``another``.

        INPUT:

        - ``another`` -- :class:`toric variety <ToricVariety_field>`

        OUTPUT:

        - ``True`` if ``self`` and ``another`` are isomorphic,
          ``False`` otherwise.

        EXAMPLES::

            sage: TV1 = toric_varieties.P1xA1()
            sage: TV2 = toric_varieties.P1xP1()

        Only the most trivial case is implemented so far::

            sage: TV1.is_isomorphic(TV1)
            True
            sage: TV1.is_isomorphic(TV2)
            Traceback (most recent call last):
            ...
            NotImplementedError: isomorphism check is not yet implemented
        """
    def is_affine(self):
        """
        Check if ``self`` is an affine toric variety.

        An affine toric variety is a toric variety whose fan is the
        face lattice of a single cone. See also
        :func:`AffineToricVariety`.

        OUTPUT: boolean

        EXAMPLES::

            sage: toric_varieties.A2().is_affine()
            True
            sage: toric_varieties.P1xA1().is_affine()
            False
        """
    def is_complete(self):
        """
        Check if ``self`` is complete.

        OUTPUT: ``True`` if ``self`` is complete and ``False`` otherwise

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.is_complete()
            True
            sage: P1xP1.affine_patch(0).is_complete()
            False
        """
    def is_orbifold(self):
        """
        Check if ``self`` has only quotient singularities.

        A toric variety with at most orbifold singularities (in this
        sense) is often called a simplicial toric variety. In this
        package, we generally try to avoid this term since it mixes up
        differential geometry and cone terminology.

        OUTPUT:

        - ``True`` if ``self`` has at most quotient singularities by
          finite groups, ``False`` otherwise.

        EXAMPLES::

            sage: fan1 = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan1)
            sage: P1xP1.is_orbifold()
            True
            sage: fan2 = NormalFan(lattice_polytope.cross_polytope(3))
            sage: TV = ToricVariety(fan2)
            sage: TV.is_orbifold()
            False
        """
    def is_smooth(self):
        """
        Check if ``self`` is smooth.

        OUTPUT: ``True`` if ``self`` is smooth and ``False`` otherwise

        EXAMPLES::

            sage: fan1 = FaceFan(lattice_polytope.cross_polytope(2))
            sage: P1xP1 = ToricVariety(fan1)
            sage: P1xP1.is_smooth()
            True
            sage: fan2 = NormalFan(lattice_polytope.cross_polytope(2))
            sage: TV = ToricVariety(fan2)
            sage: TV.is_smooth()
            False
        """
    @cached_method
    def Kaehler_cone(self):
        """
        Return the closure of the Kähler cone of ``self``.

        OUTPUT: :class:`cone <sage.geometry.cone.ConvexRationalPolyhedralCone>`

        .. NOTE::

            This cone sits in the rational divisor class group of ``self`` and
            the choice of coordinates agrees with
            :meth:`rational_class_group`.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: Kc = P1xP1.Kaehler_cone()
            sage: Kc
            2-d cone in 2-d lattice
            sage: Kc.rays()
            Divisor class [0, 1],
            Divisor class [1, 0]
            in Basis lattice of The toric rational divisor class group
            of a 2-d CPR-Fano toric variety covered by 4 affine patches
            sage: [ divisor_class.lift() for divisor_class in Kc.rays() ]
            [V(y), V(t)]
            sage: Kc.lattice()
            Basis lattice of The toric rational divisor class group of a
            2-d CPR-Fano toric variety covered by 4 affine patches
        """
    @cached_method
    def Mori_cone(self):
        """
        Return the Mori cone of ``self``.

        OUTPUT: :class:`cone <sage.geometry.cone.ConvexRationalPolyhedralCone>`

        .. NOTE::

            * The Mori cone is dual to the Kähler cone.

            * We think of the Mori cone as living inside the row span of the
              Gale transform matrix (computed by
              ``self.fan().Gale_transform()``).

            * The points in the Mori cone are the effective curves in the
              variety.

            * The ``i``-th entry in each Mori vector is the intersection
              number of the curve corresponding to the generator of the
              ``i``-th ray of the fan with the corresponding divisor class.
              The very last entry is associated to the origin of the fan
              lattice.

            * The Mori vectors are also known as the gauged linear sigma model
              charge vectors.

        EXAMPLES::

            sage: P4_11169 = toric_varieties.P4_11169_resolved()
            sage: P4_11169.Mori_cone()
            2-d cone in 7-d lattice
            sage: P4_11169.Mori_cone().rays()
            (3, 2, 0, 0, 0,  1, -6),
            (0, 0, 1, 1, 1, -3,  0)
            in Ambient free module of rank 7 over the principal ideal domain Integer Ring
        """
    def plot(self, **options):
        """
        Plot ``self``, i.e. the corresponding fan.

        INPUT:

        - any options for toric plots (see :func:`toric_plotter.options
          <sage.geometry.toric_plotter.options>`), none are mandatory.

        OUTPUT: a plot

        .. NOTE::

            The difference between ``X.plot()`` and ``X.fan().plot()`` is that
            in the first case default ray labels correspond to variables of
            ``X``.

        EXAMPLES::

            sage: X = toric_varieties.Cube_deformation(4)
            sage: X.plot()                                                              # needs sage.plot
            Graphics3d Object
        """
    def rational_class_group(self):
        """
        Return the rational divisor class group of ``self``.

        Let `X` be a toric variety.

        The **Weil divisor class group** `\\mathop{Cl}(X)` is a finitely
        generated abelian group and can contain torsion. Its rank equals the
        number of rays in the fan of `X` minus the dimension of `X`.

        The **rational divisor class group** is
        `\\mathop{Cl}(X) \\otimes_\\ZZ \\QQ` and never includes torsion. If `X` is
        *smooth*, this equals the **Picard group** of `X`, whose elements are
        the isomorphism classes of line bundles on `X`. The group law (which
        we write as addition) is the tensor product of the line bundles. The
        Picard group of a toric variety is always torsion-free.

        OUTPUT: :class:`rational divisor class group
        <sage.schemes.toric.divisor.ToricRationalDivisorClassGroup>`.

        .. NOTE::

            * Coordinates correspond to the rows of
              ``self.fan().gale_transform()``.

            * :meth:`Kaehler_cone` yields a cone in this group.

        EXAMPLES::

            sage: P1xA1 = toric_varieties.P1xA1()
            sage: P1xA1.rational_class_group()
            The toric rational divisor class group
            of a 2-d toric variety covered by 2 affine patches
        """
    def Chow_group(self, base_ring=...):
        """
        Return the toric Chow group.

        INPUT:

        - ``base_ring`` -- either ``ZZ`` (default) or ``QQ``; the
          coefficient ring of the Chow group

        OUTPUT: a :class:`sage.schemes.toric.chow_group.ChowGroup_class`

        EXAMPLES::

            sage: A = toric_varieties.P2().Chow_group(); A
            Chow group of 2-d CPR-Fano toric variety covered by 3 affine patches
            sage: A.gens()
            (( 0 | 0 | 1 ), ( 0 | 1 | 0 ), ( 1 | 0 | 0 ))
        """
    def cartesian_product(self, other, coordinate_names=None, coordinate_indices=None):
        """
        Return the Cartesian product of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a :class:`toric variety <ToricVariety_field>`

        - ``coordinate_names`` -- names of variables for the coordinate ring,
          see :func:`normalize_names` for acceptable formats. If not given,
          indexed variable names will be created automatically.

        - ``coordinate_indices`` -- list of integers, indices for indexed
          variables. If not given, the index of each variable will coincide
          with the index of the corresponding ray of the fan.

        OUTPUT: a :class:`toric variety <ToricVariety_field>`

        EXAMPLES::

            sage: P1 = ToricVariety(Fan([Cone([(1,)]), Cone([(-1,)])]))
            sage: P1xP1 = P1.cartesian_product(P1); P1xP1
            2-d toric variety covered by 4 affine patches
            sage: P1xP1.fan().rays()
            N+N(-1,  0),      N+N( 1,  0),
            N+N( 0, -1),      N+N( 0,  1)
            in 2-d lattice N+N
        """
    def resolve(self, **kwds):
        '''
        Construct a toric variety whose fan subdivides the fan of ``self``.

        The name of this function reflects the fact that usually such
        subdivisions are done for resolving singularities of the original
        variety.

        INPUT:

        This function accepts only keyword arguments, none of which are
        mandatory.

        - ``coordinate_names`` -- names for coordinates of the new variety. If
          not given, will be constructed from the coordinate names of ``self``
          and necessary indexed ones. See :func:`normalize_names` for the
          description of acceptable formats.

        - ``coordinate_indices`` -- coordinate indices which should be used
          for indexed variables of the new variety

        - all other arguments will be passed to
          :meth:`~sage.geometry.fan.RationalPolyhedralFan.subdivide` method of
          the underlying :class:`rational polyhedral fan
          <sage.geometry.fan.RationalPolyhedralFan>`, see its documentation
          for the available options.

        OUTPUT: a :class:`toric variety <ToricVariety_field>`

        EXAMPLES:

        First we will "manually" resolve a simple orbifold singularity::

            sage: cone = Cone([(1,1), (-1,1)])
            sage: fan = Fan([cone])
            sage: TV = ToricVariety(fan)
            sage: TV.is_smooth()
            False
            sage: TV_res = TV.resolve(new_rays=[(0,1)])
            sage: TV_res.is_smooth()
            True
            sage: TV_res.fan().rays()
            N( 1, 1),
            N(-1, 1),
            N( 0, 1)
            in 2-d lattice N
            sage: [cone.ambient_ray_indices() for cone in TV_res.fan()]
            [(0, 2), (1, 2)]

        Now let\'s "automatically" partially resolve a more complicated fan::

            sage: fan = NormalFan(lattice_polytope.cross_polytope(3))
            sage: TV = ToricVariety(fan)
            sage: TV.is_smooth()
            False
            sage: TV.is_orbifold()
            False
            sage: TV.fan().nrays()
            8
            sage: TV.fan().ngenerating_cones()
            6
            sage: TV_res = TV.resolve(make_simplicial=True)
            sage: TV_res.is_smooth()
            False
            sage: TV_res.is_orbifold()
            True
            sage: TV_res.fan().nrays()
            8
            sage: TV_res.fan().ngenerating_cones()
            12
            sage: TV.gens()
            (z0, z1, z2, z3, z4, z5, z6, z7)
            sage: TV_res.gens()
            (z0, z1, z2, z3, z4, z5, z6, z7)
            sage: TV_res = TV.resolve(coordinate_names=\'x+\',
            ....:                     make_simplicial=True)
            sage: TV_res.gens()
            (x0, x1, x2, x3, x4, x5, x6, x7)
        '''
    def resolve_to_orbifold(self, **kwds):
        """
        Construct an orbifold whose fan subdivides the fan of ``self``.

        It is a synonym for :meth:`resolve` with ``make_simplicial=True``
        option.

        INPUT:

        - this function accepts only keyword arguments. See :meth:`resolve`
          for documentation.

        OUTPUT: a :class:`toric variety <ToricVariety_field>`

        EXAMPLES::

            sage: fan = NormalFan(lattice_polytope.cross_polytope(3))
            sage: TV = ToricVariety(fan)
            sage: TV.is_orbifold()
            False
            sage: TV.fan().nrays()
            8
            sage: TV.fan().ngenerating_cones()
            6
            sage: TV_res = TV.resolve_to_orbifold()
            sage: TV_res.is_orbifold()
            True
            sage: TV_res.fan().nrays()
            8
            sage: TV_res.fan().ngenerating_cones()
            12
        """
    def subscheme(self, polynomials):
        """
        Return the subscheme of ``self`` defined by ``polynomials``.

        INPUT:

        - ``polynomials`` -- list of polynomials in the coordinate ring of
          ``self``

        OUTPUT: a :class:`subscheme of a toric variety
        <sage.schemes.toric.toric_subscheme.AlgebraicScheme_subscheme_toric>`.

        EXAMPLES:

        We will construct a subscheme of the product of two projective lines
        with coordinates `(x, y)` for one and `(s, t)` for the other::

            sage: P1xP1.<x,y,s,t> = toric_varieties.P1xP1()
            sage: X = P1xP1.subscheme([x*s + y*t, x^3 + y^3])
            sage: X
            Closed subscheme of 2-d CPR-Fano toric variety
            covered by 4 affine patches defined by:
              x*s + y*t,
              x^3 + y^3
            sage: X.defining_polynomials()
            (x*s + y*t, x^3 + y^3)
            sage: X.defining_ideal()
            Ideal (x*s + y*t, x^3 + y^3) of
             Multivariate Polynomial Ring in x, y, s, t over Rational Field
            sage: X.base_ring()
            Rational Field
            sage: X.base_scheme()
            Spectrum of Rational Field
            sage: X.structure_morphism()
            Scheme morphism:
              From: Closed subscheme of 2-d CPR-Fano toric variety
                    covered by 4 affine patches defined by: x*s + y*t, x^3 + y^3
              To:   Spectrum of Rational Field
              Defn: Structure map
        """
    def Stanley_Reisner_ideal(self):
        """
        Return the Stanley-Reisner ideal.

        OUTPUT:

        - The Stanley-Reisner ideal in the polynomial ring over
          `\\QQ` generated by the homogeneous coordinates.

        EXAMPLES::

            sage: fan = Fan([[0,1,3], [3,4], [2,0], [1,2,4]],
            ....:           [(-3, -2, 1), (0, 0, 1), (3, -2, 1), (-1, -1, 1), (1, -1, 1)])
            sage: X = ToricVariety(fan, coordinate_names='A B C D E', base_field=GF(5))
            sage: SR = X.Stanley_Reisner_ideal(); SR
            Ideal (A*E, C*D, A*B*C, B*D*E) of
             Multivariate Polynomial Ring in A, B, C, D, E over Rational Field
        """
    def linear_equivalence_ideal(self):
        """
        Return the ideal generated by linear relations.

        OUTPUT:

        - The ideal generated by the linear relations of the rays in
          the polynomial ring over `\\QQ` generated by the homogeneous
          coordinates.

        EXAMPLES::

            sage: fan = Fan([[0,1,3], [3,4], [2,0], [1,2,4]],
            ....:           [(-3, -2, 1), (0, 0, 1), (3, -2, 1), (-1, -1, 1), (1, -1, 1)])
            sage: X = ToricVariety(fan, coordinate_names='A B C D E', base_field=GF(5))
            sage: lin = X.linear_equivalence_ideal(); lin
            Ideal (-3*A + 3*C - D + E, -2*A - 2*C - D - E, A + B + C + D + E) of
             Multivariate Polynomial Ring in A, B, C, D, E over Rational Field
        """
    @cached_method
    def cohomology_ring(self):
        """
        Return the cohomology ring of the toric variety.

        OUTPUT:

        - If the toric variety is over `\\CC` and has at most finite
          orbifold singularities: `H^\\bullet(X,\\QQ)` as a polynomial
          quotient ring.

        - Other cases are not handled yet.

        .. NOTE::

            - Toric varieties over any field of characteristic 0 are
              treated as if they were varieties over `\\CC`.

            - The integral cohomology of smooth toric varieties is
              torsion-free, so in this case there is no loss of
              information when going to rational coefficients.

            - ``self.cohomology_ring().gen(i)`` is the divisor class corresponding to
              the ``i``-th ray of the fan.

        EXAMPLES::

            sage: X = toric_varieties.dP6()
            sage: X.cohomology_ring()
            Rational cohomology ring of a 2-d CPR-Fano toric variety covered by 6 affine patches
            sage: X.cohomology_ring().defining_ideal()
            Ideal (-u - y + z + w, x - y - v + w, x*y, x*v, x*z, u*v, u*z, u*w, y*z, y*w, v*w)
             of Multivariate Polynomial Ring in x, u, y, v, z, w over Rational Field
            sage: X.cohomology_ring().defining_ideal().ring()
            Multivariate Polynomial Ring in x, u, y, v, z, w over Rational Field
            sage: X.variable_names()
            ('x', 'u', 'y', 'v', 'z', 'w')
            sage: X.cohomology_ring().gens()                                            # needs sage.libs.singular
            ([y + v - w], [-y + z + w], [y], [v], [z], [w])

        TESTS:

        The cohomology ring is a circular reference that is
        potentially troublesome on unpickling, see :issue:`15050`
        and :issue:`15149` ::

            sage: # needs sage.libs.singular
            sage: variety = toric_varieties.P(1)
            sage: a = [variety.cohomology_ring(), variety.cohomology_basis(), variety.volume_class()]
            sage: b = [variety.Todd_class(), variety.Chern_class(), variety.Chern_character(), variety.Kaehler_cone(), variety.Mori_cone()]
            sage: loads(dumps(variety)) == variety
            True
        """
    @cached_method
    def cohomology_basis(self, d=None):
        """
        Return a basis for the cohomology of the toric variety.

        INPUT:

        - ``d`` -- (optional) integer

        OUTPUT:

        - Without the optional argument, a list whose `d`-th entry is a
          basis for `H^{2d}(X,\\QQ)`

        - If the argument is an integer ``d``, returns basis for
          `H^{2d}(X,\\QQ)`

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: X = toric_varieties.dP8()
            sage: X.cohomology_basis()
            (([1],), ([z], [y]), ([y*z],))
            sage: X.cohomology_basis(1)
            ([z], [y])
            sage: X.cohomology_basis(dimension(X))[0] == X.volume_class()
            True
        """
    @cached_method
    def volume_class(self):
        """
        Return the cohomology class of the volume form on the toric
        variety.

        Note that we are using cohomology with compact supports. If
        the variety is non-compact this is dual to homology without
        any support condition. In particular, for non-compact
        varieties the volume form `\\mathrm{dVol}=\\wedge_i(dx_i \\wedge
        dy_i)` does not define a (nonzero) cohomology class.

        OUTPUT:

        A :class:`CohomologyClass`. If it exists, it is the class of
        the (properly normalized) volume form, that is, it is the
        Poincaré dual of a single point. If it does not exist, a
        :exc:`ValueError` is raised.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.volume_class()                                                     # needs sage.libs.singular
            [z^2]

            sage: A2_Z2 = toric_varieties.A2_Z2()
            sage: A2_Z2.volume_class()                                                  # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: volume class does not exist

        If none of the maximal cones is smooth things get more
        tricky. In this case no torus-fixed point is smooth. If we
        want to count an ordinary point as `1`, then a `G`-orbifold
        point needs to count as `\\frac{1}{|G|}`. For example, take
        `\\mathbb{P}^1\\times\\mathbb{P}^1` with inhomogeneous
        coordinates `(t,y)`. Take the quotient by the action
        `(t,y)\\mapsto (-t,-y)`. The `\\ZZ_2`-invariant Weil divisors
        `\\{t=0\\}` and `\\{y=0\\}` intersect in a `\\ZZ_2`-fixed point, so
        they ought to have intersection number `\\frac{1}{2}`. This
        means that the cohomology class `[t] \\cap [y]` should be
        `\\frac{1}{2}` times the volume class. Note that this is
        different from the volume normalization chosen in
        [KS]_::

            sage: P1xP1_Z2 = toric_varieties.P1xP1_Z2()
            sage: Dt = P1xP1_Z2.divisor(1);  Dt
            V(t)
            sage: Dy = P1xP1_Z2.divisor(3);  Dy
            V(y)
            sage: P1xP1_Z2.volume_class()                                               # needs sage.libs.singular
            [2*t*y]

            sage: HH = P1xP1_Z2.cohomology_ring()
            sage: HH(Dt) * HH(Dy) == 1/2 * P1xP1_Z2.volume_class()                      # needs sage.libs.singular
            True

        The fractional coefficients are also necessary to match the
        normalization in the rational Chow group for simplicial toric
        varieties::

            sage: A = P1xP1_Z2.Chow_group(QQ)
            sage: A(Dt).intersection_with_divisor(Dy).count_points()
            1/2
        """
    def integrate(self, cohomology_class):
        """
        Integrate a cohomology class over the toric variety.

        INPUT:

        - ``cohomology_class`` -- a cohomology class given as a
          polynomial in ``self.cohomology_ring()``

        OUTPUT:

        The integral of the cohomology class over the variety. The
        volume normalization is given by :meth:`volume_class`, that
        is, ``self.integrate(self.volume_class())`` is always one (if
        the volume class exists).

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: dP6 = toric_varieties.dP6()
            sage: HH = dP6.cohomology_ring()
            sage: D = [ HH(c) for c in dP6.fan(dim=1) ]
            sage: matrix([ [ D[i]*D[j] for i in range(0,6) ] for j in range(0,6) ])
            [ [w^2] [-w^2]    [0]    [0]    [0] [-w^2]]
            [[-w^2]  [w^2] [-w^2]    [0]    [0]    [0]]
            [   [0] [-w^2]  [w^2] [-w^2]    [0]    [0]]
            [   [0]    [0] [-w^2]  [w^2] [-w^2]    [0]]
            [   [0]    [0]    [0] [-w^2]  [w^2] [-w^2]]
            [[-w^2]    [0]    [0]    [0] [-w^2]  [w^2]]
            sage: matrix([ [ dP6.integrate(D[i]*D[j]) for i in range(0,6) ] for j in range(0,6) ])
            [-1  1  0  0  0  1]
            [ 1 -1  1  0  0  0]
            [ 0  1 -1  1  0  0]
            [ 0  0  1 -1  1  0]
            [ 0  0  0  1 -1  1]
            [ 1  0  0  0  1 -1]

        If the toric variety is an orbifold, the intersection numbers
        are usually fractional::

            sage: # needs sage.libs.singular
            sage: P2_123 = toric_varieties.P2_123()
            sage: HH = P2_123.cohomology_ring()
            sage: D = [ HH(c) for c in P2_123.fan(dim=1) ]
            sage: matrix([ [ P2_123.integrate(D[i]*D[j]) for i in range(0,3) ] for j in range(0,3) ])
            [2/3   1 1/3]
            [  1 3/2 1/2]
            [1/3 1/2 1/6]
            sage: A = P2_123.Chow_group(QQ)
            sage: matrix([ [ A(P2_123.divisor(i))
            ....:            .intersection_with_divisor(P2_123.divisor(j))
            ....:            .count_points() for i in range(0,3) ] for j in range(0,3) ])
            [2/3   1 1/3]
            [  1 3/2 1/2]
            [1/3 1/2 1/6]
        """
    @property
    def sheaves(self):
        """
        Return the factory object for sheaves on the toric variety.

        See :class:`sage.schemes.toric.sheaf.constructor.SheafLibrary`
        for details.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: dP6.sheaves
            Sheaf constructor on 2-d CPR-Fano toric variety covered by 6 affine patches
            sage: dP6.sheaves.trivial_bundle()
            Rank 1 bundle on 2-d CPR-Fano toric variety covered by 6 affine patches.
        """
    @cached_method
    def Chern_class(self, deg=None):
        """
        Return Chern classes of the (tangent bundle of the) toric variety.

        INPUT:

        - ``deg`` -- integer (optional); the degree of the Chern class

        OUTPUT: if the degree is specified, the ``deg``-th Chern class

        - If no degree is specified, the total Chern class.

        REFERENCES:

        - :wikipedia:`Chern_class`

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: X = toric_varieties.dP6()
            sage: X.Chern_class()
            [-6*w^2 + y + 2*v + 2*z + w + 1]
            sage: X.c()
            [-6*w^2 + y + 2*v + 2*z + w + 1]
            sage: X.c(1)
            [y + 2*v + 2*z + w]
            sage: X.c(2)
            [-6*w^2]
            sage: X.integrate( X.c(2) )
            6
            sage: X.integrate( X.c(2) ) == X.Euler_number()
            True
        """
    @cached_method
    def Chern_character(self, deg=None):
        """
        Return the Chern character (of the tangent bundle) of the toric
        variety.

        INPUT:

        - ``deg`` -- integer (optional); the degree of the Chern
          character

        OUTPUT:

        - If the degree is specified, the degree-``deg`` part of the
          Chern character.

        - If no degree is specified, the total Chern character.

        REFERENCES:

        - :wikipedia:`Chern_character#The_Chern_character`

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: dP6 = toric_varieties.dP6()
            sage: dP6.Chern_character()
            [3*w^2 + y + 2*v + 2*z + w + 2]
            sage: dP6.ch()
            [3*w^2 + y + 2*v + 2*z + w + 2]
            sage: dP6.ch(1) == dP6.c(1)
            True
        """
    @cached_method
    def Todd_class(self, deg=None):
        """
        Return the Todd class (of the tangent bundle) of the toric variety.

        INPUT:

        - ``deg`` -- integer (optional); the desired degree part

        OUTPUT:

        - If the degree is specified, the degree-``deg`` part of the
          Todd class.

        - If no degree is specified, the total Todd class.

        REFERENCES:

        - :wikipedia:`Todd_class`

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: dP6 = toric_varieties.dP6()
            sage: dP6.Todd_class()
            [-w^2 + 1/2*y + v + z + 1/2*w + 1]
            sage: dP6.Td()
            [-w^2 + 1/2*y + v + z + 1/2*w + 1]
            sage: dP6.integrate( dP6.Td() )
            1
        """
    c = Chern_class
    ch = Chern_character
    Td = Todd_class
    def Euler_number(self):
        """
        Return the topological Euler number of the toric variety.

        Sometimes, this is also called the Euler
        characteristic. :meth:`chi` is a synonym for
        :meth:`Euler_number`.

        REFERENCES:

        - :wikipedia:`Euler_characteristic`

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.Euler_number()
            4
            sage: P1xP1.chi()
            4
        """
    chi = Euler_number
    def K(self):
        """
        Return the canonical divisor of the toric variety.

        EXAMPLES:

        Lets test that the del Pezzo surface `dP_6` has degree 6, as its name implies::

            sage: dP6 = toric_varieties.dP6()
            sage: HH = dP6.cohomology_ring()
            sage: dP6.K()
            -V(x) - V(u) - V(y) - V(v) - V(z) - V(w)
            sage: dP6.integrate( HH(dP6.K())^2 )                                        # needs sage.libs.singular
            6
        """
    def divisor(self, arg, base_ring=None, check: bool = True, reduce: bool = True):
        """
        Return a divisor.

        INPUT:

        The arguments are the same as in
        :func:`sage.schemes.toric.divisor.ToricDivisor`, with the
        exception of defining a divisor with a single integer: this method
        considers it to be the index of a ray of the :meth:`fan` of ``self``.

        OUTPUT: a :class:`sage.schemes.toric.divisor.ToricDivisor_generic`

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: dP6.coordinate_ring()
            Multivariate Polynomial Ring in x, u, y, v, z, w over Rational Field
            sage: dP6.divisor(list(range(6)))
            V(u) + 2*V(y) + 3*V(v) + 4*V(z) + 5*V(w)
            sage: dP6.inject_variables()
            Defining x, u, y, v, z, w
            sage: dP6.divisor(x*u^3)
            V(x) + 3*V(u)

        You can also construct divisors based on ray indices::

            sage: dP6.divisor(0)
            V(x)
            sage: for i in range(dP6.fan().nrays()):
            ....:     print('{} : generated by ray {}'.format(dP6.divisor(i),
            ....:           dP6.fan().ray(i)))
            V(x) : generated by ray N(0, 1)
            V(u) : generated by ray N(-1, 0)
            V(y) : generated by ray N(-1, -1)
            V(v) : generated by ray N(0, -1)
            V(z) : generated by ray N(1, 0)
            V(w) : generated by ray N(1, 1)

        TESTS:

        We check that the issue :issue:`12812` is resolved::

            sage: sum(dP6.divisor(i) for i in range(3))
            V(x) + V(u) + V(y)
        """
    def divisor_group(self, base_ring=...):
        """
        Return the group of Weil divisors.

        INPUT:

        - ``base_ring`` -- the coefficient ring, usually ``ZZ``
          (default) or ``QQ``

        OUTPUT:

        The (free abelian) group of Cartier divisors, that is, formal
        linear combinations of polynomial equations over the
        coefficient ring ``base_ring``.

        These need not be toric (=defined by monomials), but allow
        general polynomials. The output will be an instance of
        :class:`sage.schemes.generic.divisor_group.DivisorGroup_generic`.

        .. WARNING::

            You almost certainly want the group of toric divisors, see
            :meth:`toric_divisor_group`. The toric divisor group is
            generated by the rays of the fan. The general divisor
            group has no toric functionality implemented.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: Div = dP6.divisor_group(); Div
            Group of ZZ-Divisors on 2-d CPR-Fano toric variety covered by 6 affine patches
            sage: Div(x)                                                                # needs sage.symbolic
            V(x)
        """
    def toric_divisor_group(self, base_ring=...):
        """
        Return the group of toric (T-Weil) divisors.

        INPUT:

        - ``base_ring`` -- the coefficient ring, usually ``ZZ``
          (default) or ``QQ``

        OUTPUT:

        The free Abelian agroup of toric Weil divisors, that is,
        formal ``base_ring``-linear combinations of codimension-one
        toric subvarieties. The output will be an instance of
        :class:`sage.schemes.toric.divisor.ToricDivisorGroup`.

        The `i`-th generator of the divisor group is the divisor where
        the `i`-th homogeneous coordinate vanishes, `\\{z_i=0\\}`.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: TDiv = dP6.toric_divisor_group(); TDiv
            Group of toric ZZ-Weil divisors on 2-d CPR-Fano toric variety
            covered by 6 affine patches
            sage: TDiv == dP6.toric_divisor_group()
            True
            sage: TDiv.gens()
            (V(x), V(u), V(y), V(v), V(z), V(w))
            sage: dP6.coordinate_ring()
            Multivariate Polynomial Ring in x, u, y, v, z, w over Rational Field
        """
    def Spec(self, cone=None, names=None):
        """
        Return the spectrum associated to the dual cone.

        Let `\\sigma \\in N_\\RR` be a cone and `\\sigma^\\vee \\cap M` the
        associated semigroup of lattice points in the dual cone. Then

        .. MATH::

            S = \\CC[\\sigma^\\vee \\cap M]

        is a `\\CC`-algebra. It is spanned over `\\CC` by the points of
        `\\sigma \\cap N`, addition is formal linear combination of
        lattice points, and multiplication of lattice points is the
        semigroup law (that is, addition of lattice points). The
        `\\CC`-algebra `S` then defines a scheme `\\mathop{Spec}(S)`.

        For example, if `\\sigma=\\{(x,y)|x\\geq 0,y\\geq 0\\}` is the
        first quadrant then `S` is the polynomial ring in two
        variables. The associated scheme is `\\mathop{Spec}(S) =
        \\CC^2`.

        The same construction works over any base field, this
        introduction only used `\\CC` for simplicity.

        INPUT:

        - ``cone`` -- a :class:`Cone
          <sage.geometry.cone.ConvexRationalPolyhedralCone>`. Can be
          omitted for an affine toric variety, in which case the
          (unique) generating cone is used.

        - ``names`` -- (optional). Names of variables for the
          semigroup ring, see :func:`normalize_names` for acceptable
          formats. If not given, indexed variable names will be
          created automatically.

        OUTPUT: the spectrum of the semigroup ring `\\CC[\\sigma^\\vee \\cap M]`

        EXAMPLES::

            sage: quadrant = Cone([(1,0), (0,1)])
            sage: AffineToricVariety(quadrant).Spec()
            Spectrum of Multivariate Polynomial Ring in z0, z1 over Rational Field

        A more interesting example::

            sage: A2Z2 = Cone([(0,1), (2,1)])
            sage: AffineToricVariety(A2Z2).Spec(names='u,v,t')                          # needs fpylll sage.libs.singular
            Spectrum of Quotient of Multivariate Polynomial Ring
            in u, v, t over Rational Field by the ideal (-u*v + t^2)
        """
    def affine_algebraic_patch(self, cone=None, names=None):
        """
        Return the patch corresponding to ``cone`` as an affine
        algebraic subvariety.

        INPUT:

        - ``cone`` -- a :class:`Cone
          <sage.geometry.cone.ConvexRationalPolyhedralCone>` `\\sigma`
          of the fan. It can be omitted for an affine toric variety,
          in which case the single generating cone is used.

        OUTPUT:

        A :class:`affine algebraic subscheme
        <sage.schemes.affine.affine_subscheme.AlgebraicScheme_subscheme_affine>`
        corresponding to the patch `\\mathop{Spec}(\\sigma^\\vee \\cap M)`
        associated to the cone `\\sigma`.

        See also :meth:`affine_patch`, which expresses the patches as
        subvarieties of affine toric varieties instead.

        EXAMPLES::

            sage: cone = Cone([(0,1), (2,1)])
            sage: A2Z2 = AffineToricVariety(cone)
            sage: A2Z2.affine_algebraic_patch()                                         # needs fpylll sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              -z0*z1 + z2^2
            sage: A2Z2.affine_algebraic_patch(Cone([(0,1)]), names='x, y, t')           # needs fpylll sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              1
        """
    def orbit_closure(self, cone):
        """
        Return the orbit closure of ``cone``.

        The cones `\\sigma` of a fan `\\Sigma` are in one-to-one correspondence
        with the torus orbits `O(\\sigma)` of the corresponding toric variety
        `X_\\Sigma`. Each orbit is isomorphic to a lower dimensional torus (of
        dimension equal to the codimension of `\\sigma`). Just like the toric
        variety `X_\\Sigma` itself, these orbits are (partially) compactified by
        lower-dimensional orbits. In particular, one can define the closure
        `V(\\sigma)` of the torus orbit `O(\\sigma)` in the ambient toric
        variety `X_\\Sigma`, which is again a toric variety.

        See Proposition 3.2.7 of [CLS2011]_ for more details.

        INPUT:

        - ``cone`` -- a :class:`cone
          <sage.geometry.cone.ConvexRationalPolyhedralCone>` of the fan

        OUTPUT:

        - a torus orbit closure associated to ``cone`` as a
          :class:`toric variety <ToricVariety_field>`.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: H = P1xP1.fan(1)[0]
            sage: V = P1xP1.orbit_closure(H);  V
            1-d toric variety covered by 2 affine patches
            sage: V.embedding_morphism()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined by embedding the torus closure associated to the 1-d
                    cone of Rational polyhedral fan in 2-d lattice N.
            sage: V.embedding_morphism().as_polynomial_map()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to [0 : 1 : z1 : z0]

        TESTS::

            sage: A2 = toric_varieties.A2()
            sage: A2.orbit_closure(A2.fan(2)[0])
            0-d affine toric variety
        """
    def count_points(self):
        """
        Return the number of points of ``self``.

        This is an alias for ``point_set().cardinality()``, see
        :meth:`~sage.schemes.toric.homset.SchemeHomset_points_toric_field.cardinality`
        for details.

        EXAMPLES::

            sage: o = lattice_polytope.cross_polytope(3)
            sage: V = ToricVariety(FaceFan(o))
            sage: V2 = V.change_ring(GF(2))
            sage: V2.point_set().cardinality()
            27
            sage: V2.count_points()
            27
        """
    @cached_method
    def Demazure_roots(self):
        """
        Return the Demazure roots.

        OUTPUT: the roots as points of the `M`-lattice

        REFERENCES:

        - [De1970]_
        - [Baz2011]_

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.Demazure_roots()
            (M(-1, 0), M(-1, 1), M(0, -1), M(0, 1), M(1, -1), M(1, 0))

        Here are the remaining three examples listed in [Baz2011]_, Example 2.1 and 2.3::

            sage: s = 3
            sage: cones = [(0,1), (1,2), (2,3), (3,0)]
            sage: Hs = ToricVariety(Fan(rays=[(1,0), (0,-1), (-1,s), (0,1)], cones=cones))
            sage: Hs.Demazure_roots()
            (M(-1, 0), M(1, 0), M(0, 1), M(1, 1), M(2, 1), M(3, 1))

            sage: P11s = ToricVariety(Fan(rays=[(1,0), (0,-1), (-1,s)],
            ....:                         cones=[(0,1), (1,2), (2,0)]))
            sage: P11s.Demazure_roots()
            (M(-1, 0), M(1, 0), M(0, 1), M(1, 1), M(2, 1), M(3, 1))
            sage: P11s.Demazure_roots() == Hs.Demazure_roots()
            True

            sage: Bs = ToricVariety(Fan(rays=[(s,1), (s,-1), (-s,-1), (-s,1)], cones=cones))
            sage: Bs.Demazure_roots()
            ()

        TESTS::

            sage: toric_varieties.A1().Demazure_roots()
            Traceback (most recent call last):
            ...
            NotImplementedError: Demazure_roots is only implemented for complete toric varieties
        """
    def Aut_dimension(self):
        """
        Return the dimension of the automorphism group.

        There are three kinds of symmetries of toric varieties:

          * Toric automorphisms (rescaling of homogeneous coordinates)

          * Demazure roots. These are translations `x_i \\to x_i +
            \\epsilon x^m` of a homogeneous coordinate `x_i` by a
            monomial `x^m` of the same homogeneous degree.

          * Symmetries of the fan. These yield discrete subgroups.

        OUTPUT:

        An integer. The dimension of the automorphism group. Equals
        the dimension of the `M`-lattice plus the number of Demazure
        roots.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.Aut_dimension()
            8

        TESTS::

            sage: toric_varieties.A1().Aut_dimension()
            Traceback (most recent call last):
            ...
            NotImplementedError: Aut_dimension is only implemented for complete toric varieties
        """

def normalize_names(names=None, ngens=None, prefix=None, indices=None, return_prefix: bool = False):
    '''
    Return a list of names in the standard form.

    INPUT:

    All input parameters are optional.

    - ``names`` -- names given either as a single string (with individual
      names separated by commas or spaces) or a list of strings with each
      string specifying a name. If the last name ends with the plus sign,
      "+", this name will be used as ``prefix`` (even if ``prefix`` was
      given explicitly).

    - ``ngens`` -- number of names to be returned

    - ``prefix`` -- prefix for the indexed names given as a string

    - ``indices`` -- list of integers (default: ``range(ngens)``) used as
      indices for names with ``prefix``. If given, must be of length
      ``ngens``.

    - ``return_prefix`` -- if ``True``, the last element of the returned list
      will contain the prefix determined from ``names`` or given as the
      parameter ``prefix``. This is useful if you may need more names in the
      future.

    OUTPUT: list of names given as strings

    These names are constructed in the following way:

    #. If necessary, split ``names`` into separate names.
    #. If the last name ends with "+", put it into ``prefix``.
    #. If ``ngens`` was given, add to the names obtained so far as many
       indexed names as necessary to get this number. If the ``k``-th name of
       the *total* list of names is indexed, it is
       ``prefix + str(indices[k])``. If there were already more names than
       ``ngens``, discard "extra" ones.
    #. Check if constructed names are valid. See :func:`certify_names` for
       details.
    #. If the option ``return_prefix=True`` was given, add ``prefix`` to the
       end of the list.

    EXAMPLES:

    As promised, all parameters are optional::

        sage: from sage.schemes.toric.variety import normalize_names
        sage: normalize_names()
        []

    One of the most common uses is probably this one::

        sage: normalize_names("x+", 4)
        [\'x0\', \'x1\', \'x2\', \'x3\']

    Now suppose that you want to enumerate your variables starting with one
    instead of zero::

        sage: normalize_names("x+", 4, indices=list(range(1,5)))
        [\'x1\', \'x2\', \'x3\', \'x4\']

    You may actually have an arbitrary enumeration scheme::

        sage: normalize_names("x+", 4, indices=[1, 10, 100, 1000])
        [\'x1\', \'x10\', \'x100\', \'x1000\']

    Now let\'s add some "explicit" names::

        sage: normalize_names("x y z t+", 4)
        [\'x\', \'y\', \'z\', \'t3\']

    Note that the "automatic" name is ``t3`` instead of ``t0``. This may seem
    weird, but the reason for this behaviour is that the fourth name in this
    list will be the same no matter how many explicit names were given::

        sage: normalize_names("x y t+", 4)
        [\'x\', \'y\', \'t2\', \'t3\']

    This is especially useful if you get ``names`` from a user but want to
    specify all default names::

        sage: normalize_names("x, y", 4, prefix=\'t\')
        [\'x\', \'y\', \'t2\', \'t3\']

    In this format, the user can easily override your choice for automatic
    names::

        sage: normalize_names("x y s+", 4, prefix=\'t\')
        [\'x\', \'y\', \'s2\', \'s3\']

    Let\'s now use all parameters at once::

        sage: normalize_names("x, y, s+", 4, prefix=\'t\',
        ....:     indices=list(range(1,5)), return_prefix=True)
        [\'x\', \'y\', \'s3\', \'s4\', \'s\']

    Note that you still need to give indices for all names, even if some of
    the first ones will be "wasted" because of the explicit names. The reason
    is the same as before - this ensures consistency of automatically
    generated names, no matter how many explicit names were given.

    The prefix is discarded if ``ngens`` was not given::

        sage: normalize_names("alpha, beta, gamma, zeta+")
        [\'alpha\', \'beta\', \'gamma\']

    Finally, let\'s take a look at some possible mistakes::

        sage: normalize_names("123")
        Traceback (most recent call last):
        ...
        ValueError: variable name \'123\' does not start with a letter

    A more subtle one::

        sage: normalize_names("x1", 4, prefix=\'x\')
        Traceback (most recent call last):
        ...
        ValueError: variable name \'x1\' appears more than once
    '''

class CohomologyRing(QuotientRing_generic, UniqueRepresentation):
    '''
    The (even) cohomology ring of a toric variety.

    Irregardles of the variety\'s base ring, we always work with the
    variety over `\\CC` and its topology.

    The cohomology is always the singular cohomology with
    `\\QQ`-coefficients. Note, however, that the cohomology of smooth
    toric varieties is torsion-free, so there is no loss of
    information in that case.

    Currently, the toric variety must not be "too singular".  See
    :meth:`ToricVariety_field.cohomology_ring` for a detailed
    description of which toric varieties are admissible. For such
    varieties the odd-dimensional cohomology groups vanish.

    .. WARNING::

        You should not create instances of this class manually. Use
        :meth:`ToricVariety_field.cohomology_ring` to generate the
        cohomology ring.

    INPUT:

    - ``variety`` -- a toric variety. Currently, the toric variety
      must be at least an orbifold. See
      :meth:`ToricVariety_field.cohomology_ring` for a detailed
      description of which toric varieties are admissible.

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: P2.cohomology_ring()
        Rational cohomology ring of a 2-d CPR-Fano toric variety covered by 3 affine patches

    This is equivalent to::

        sage: from sage.schemes.toric.variety import CohomologyRing
        sage: CohomologyRing(P2)
        Rational cohomology ring of a 2-d CPR-Fano toric variety covered by 3 affine patches
    '''
    def __init__(self, variety) -> None:
        """
        See :class:`CohomologyRing` for documentation.

        TESTS::

            sage: P2 = toric_varieties.P2()
            sage: P2.cohomology_ring()
            Rational cohomology ring of a 2-d CPR-Fano toric variety covered by 3 affine patches

        ::

            sage: cone1 = Cone([(1,0)]);  cone2 = Cone([(1,0)])
            sage: cone1 is cone2
            False
            sage: fan1 = Fan([cone1]);  fan2 = Fan([cone2])
            sage: fan1 is fan2
            False
            sage: X1 = ToricVariety(fan1);  X2 = ToricVariety(fan2)
            sage: X1 is X2
            False
            sage: X1.cohomology_ring() is X2.cohomology_ring()   # see https://github.com/sagemath/sage/issues/10325
            True
            sage: TDiv = X1.toric_divisor_group()
            sage: X1.toric_divisor_group() is TDiv
            True
            sage: X2.toric_divisor_group() is TDiv
            True
            sage: TDiv.scheme() is X1   # as you expect
            True
            sage: TDiv.scheme() is X2   # perhaps less obvious, but toric_divisor_group is unique!
            False
            sage: TDiv.scheme() == X2   # isomorphic, but not necessarily identical
            True
            sage: TDiv.scheme().cohomology_ring() is X2.cohomology_ring()  # this is where it gets tricky
            True
            sage: TDiv.gen(0).Chern_character() * X2.cohomology_ring().one()            # needs sage.libs.singular
            [1]
        """
    def __call__(self, x, coerce: bool = True):
        """
        Turn ``x`` into a ``CohomologyClass``.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2 = toric_varieties.P2()
            sage: H = P2.cohomology_ring()
            sage: H(1)
            [1]
            sage: type( H(1) )
            <class 'sage.schemes.toric.variety.CohomologyClass'>
        """
    def gens(self) -> tuple:
        """
        Return the generators of the cohomology ring.

        OUTPUT:

        A tuple of generators, one for each toric divisor of the toric
        variety ``X``. The order is the same as the ordering of the
        rays of the fan ``X.fan().rays()``, which is also the same as
        the ordering of the one-cones in ``X.fan(1)``

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.cohomology_ring().gens()                                           # needs sage.libs.singular
            ([z], [z], [z])
        """
    def gen(self, i):
        """
        Return a generator of the cohomology ring.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        The ``i``-th generator of the cohomology ring. If we denote
        the toric variety by ``X``, then this generator is
        associated to the ray ``X.fan().ray(i)``, which spans the
        one-cone ``X.fan(1)[i]``

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.cohomology_ring().gen(2)                                           # needs sage.libs.singular
            [z]
        """

def is_CohomologyClass(x):
    """
    Check whether ``x`` is a cohomology class of a toric variety.

    INPUT:

    - ``x`` -- anything

    OUTPUT:

    ``True`` or ``False`` depending on whether ``x`` is an instance of
    :class:`CohomologyClass`

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: HH = P2.cohomology_ring()
        sage: from sage.schemes.toric.variety import is_CohomologyClass
        sage: is_CohomologyClass( HH.one() )                                            # needs sage.libs.singular
        doctest:warning...
        DeprecationWarning: The function is_CohomologyClass is deprecated;
        use 'isinstance(..., CohomologyClass)' instead.
        See https://github.com/sagemath/sage/issues/38277 for details.
        True
        sage: is_CohomologyClass( HH(P2.fan(1)[0]) )                                    # needs sage.libs.singular
        True
        sage: is_CohomologyClass('z')
        False
    """

class CohomologyClass(QuotientRingElement):
    """
    An element of the :class:`CohomologyRing`.

    .. WARNING::

        You should not create instances of this class manually. The
        generators of the cohomology ring as well as the cohomology
        classes associated to cones of the fan can be obtained from
        :meth:`ToricVariety_field.cohomology_ring`.

    EXAMPLES::

        sage: # needs sage.libs.singular
        sage: P2 = toric_varieties.P2()
        sage: P2.cohomology_ring().gen(0)
        [z]
        sage: HH = P2.cohomology_ring()
        sage: HH.gen(0)
        [z]
        sage: cone = P2.fan(1)[0];  HH(cone)
        [z]
    """
    def __init__(self, cohomology_ring, representative) -> None:
        """
        Construct the cohomology class.

        INPUT:

        - ``cohomology_ring`` -- :class:`CohomologyRing`

        - ``representative`` -- a polynomial in the generators of the cohomology ring

        OUTPUT: an instance of :class:`CohomologyClass`

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: H = P2.cohomology_ring()
            sage: from sage.schemes.toric.variety import CohomologyClass
            sage: CohomologyClass(H, H.defining_ideal().ring().zero() )                 # needs sage.libs.singular
            [0]
        """
    def deg(self):
        """
        The degree of the cohomology class.

        OUTPUT:

        An integer `d` such that the cohomology class is in degree
        `2d`. If the cohomology class is of mixed degree, the highest
        degree is returned.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P2.cohomology_ring().gen(0).deg()                                     # needs sage.libs.singular
            1
            sage: P2.cohomology_ring().zero().deg()                                     # needs sage.libs.singular
            -1
        """
    def part_of_degree(self, d):
        """
        Project the (mixed-degree) cohomology class to the given degree.

        .. MATH::

            \\mathop{pr}\\nolimits_d:~ H^\\bullet(X_\\Delta,\\QQ) \\to H^{2d}(X_\\Delta,\\QQ)

        INPUT:

        - An integer ``d``

        OUTPUT: the degree-``2d`` part of the cohomology class

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P1xP1 = toric_varieties.P1xP1()
            sage: t = P1xP1.cohomology_ring().gen(0)
            sage: y = P1xP1.cohomology_ring().gen(2)
            sage: 3*t + 4*t^2*y + y + t*y + t + 1
            [t*y + 4*t + y + 1]
            sage: (3*t + 4*t^2*y + y + t*y + t + 1).part_of_degree(1)
            [4*t + y]
        """
    def exp(self):
        """
        Exponentiate ``self``.

        .. NOTE::

            The exponential `\\exp(x)` of a rational number `x` is
            usually not rational. Therefore, the cohomology class must
            not have a constant (degree zero) part. The coefficients
            in the Taylor series of `\\exp` are rational, so any
            cohomology class without constant term can be
            exponentiated.

        OUTPUT:

        The cohomology class `\\exp(` ``self`` `)` if the constant part
        vanishes, otherwise a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2 = toric_varieties.P2()
            sage: H_class = P2.cohomology_ring().gen(0)
            sage: H_class
            [z]
            sage: H_class.exp()
            [1/2*z^2 + z + 1]
        """
