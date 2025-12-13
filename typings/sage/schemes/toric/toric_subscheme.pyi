from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme

class AlgebraicScheme_subscheme_toric(AlgebraicScheme_subscheme):
    """
    Construct an algebraic subscheme of a toric variety.

    .. WARNING::

        You should not create objects of this class directly. The
        preferred method to construct such subschemes is to use
        :meth:`~ToricVariety_field.subscheme` method of :class:`toric
        varieties <sage.schemes.toric.variety.ToricVariety_field>`.

    INPUT:

    - ``toric_variety`` -- ambient :class:`toric variety
      <ToricVariety_field>`

    - ``polynomials`` -- single polynomial, list, or ideal of defining
      polynomials in the coordinate ring of ``toric_variety``

    OUTPUT: an :class:`algebraic subscheme of a toric variety
    <AlgebraicScheme_subscheme_toric>`.

    TESTS::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1xP1.inject_variables()
        Defining s, t, x, y
        sage: import sage.schemes.toric.toric_subscheme as SCM
        sage: X = SCM.AlgebraicScheme_subscheme_toric(
        ....:       P1xP1, [x*s + y*t, x^3 + y^3])
        sage: X
        Closed subscheme of 2-d CPR-Fano toric variety
        covered by 4 affine patches defined by:
          s*x + t*y,
          x^3 + y^3

    A better way to construct the same scheme as above::

        sage: P1xP1.subscheme([x*s + y*t, x^3 + y^3])
        Closed subscheme of 2-d CPR-Fano toric variety
        covered by 4 affine patches defined by:
          s*x + t*y,
          x^3 + y^3
    """
    def __init__(self, toric_variety, polynomials) -> None:
        """
        See :class:`AlgebraicScheme_subscheme_toric` for documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.inject_variables()
            Defining s, t, x, y
            sage: import sage.schemes.toric.toric_subscheme as SCM
            sage: X = SCM.AlgebraicScheme_subscheme_toric(
            ....:       P1xP1, [x*s + y*t, x^3 + y^3])
            sage: X
            Closed subscheme of 2-d CPR-Fano toric variety
            covered by 4 affine patches defined by:
              s*x + t*y,
              x^3 + y^3
        """
    def fan(self):
        """
        Return the fan of the ambient space.

        OUTPUT: a fan

        EXAMPLES::

            sage: P2.<x,y,z> = toric_varieties.P(2)
            sage: E = P2.subscheme([x^2 + y^2 + z^2])
            sage: E.fan()
            Rational polyhedral fan in 2-d lattice N
        """
    def affine_patch(self, i):
        """
        Return the ``i``-th affine patch of ``self`` as an affine
        toric algebraic scheme.

        INPUT:

        - ``i`` -- integer; index of a generating cone of the fan of the
          ambient space of ``self``

        OUTPUT:

        - subscheme of an affine :class:`toric variety
          <sage.schemes.toric.variety.ToricVariety_field>`
          corresponding to the pull-back of ``self`` by the embedding
          morphism of the ``i``-th :meth:`affine patch of the ambient
          space
          <sage.schemes.toric.variety.ToricVariety_field.affine_patch>`
          of ``self``.

        The result is cached, so the ``i``-th patch is always the same object
        in memory.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: patch1 = P1xP1.affine_patch(1)
            sage: patch1.embedding_morphism()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [t : x] to [1 : t : x : 1]
            sage: P1xP1.inject_variables()
            Defining s, t, x, y
            sage: P1 = P1xP1.subscheme(x - y)
            sage: subpatch = P1.affine_patch(1)
            sage: subpatch
            Closed subscheme of 2-d affine toric variety defined by:
              x - 1
        """
    def affine_algebraic_patch(self, cone=None, names=None):
        '''
        Return the affine patch corresponding to ``cone`` as an affine
        algebraic scheme.

        INPUT:

        - ``cone`` -- a :class:`Cone
          <sage.geometry.cone.ConvexRationalPolyhedralCone>` `\\sigma`
          of the fan. It can be omitted for an affine toric variety,
          in which case the single generating cone is used.

        OUTPUT:

        An :class:`affine algebraic subscheme
        <sage.schemes.affine.affine_subscheme.AlgebraicScheme_subscheme_affine>`
        corresponding to the patch `\\mathop{Spec}(\\sigma^\\vee \\cap M)`
        associated to the cone `\\sigma`.

        See also :meth:`affine_patch`, which expresses the patches as
        subvarieties of affine toric varieties instead.

        REFERENCES:

        ..

            David A. Cox, "The Homogeneous Coordinate Ring of a Toric
            Variety", Lemma 2.2.
            :arxiv:`alg-geom/9210008v2`

        EXAMPLES::

            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: cone = P2.fan().generating_cone(0)
            sage: V = P2.subscheme(x^3 + y^3 + z^3)
            sage: V.affine_algebraic_patch(cone)
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              z0^3 + z1^3 + 1

            sage: # needs fpylll sage.libs.singular
            sage: cone = Cone([(0,1), (2,1)])
            sage: A2Z2.<x,y> = AffineToricVariety(cone)
            sage: A2Z2.affine_algebraic_patch()
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              -z0*z1 + z2^2
            sage: V = A2Z2.subscheme(x^2 + y^2 - 1)
            sage: patch = V.affine_algebraic_patch();  patch
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              -z0*z1 + z2^2,
              z0 + z1 - 1
            sage: nbhd_patch = V.neighborhood([1,0]).affine_algebraic_patch();  nbhd_patch
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              -z0*z1 + z2^2,
              z0 + z1 - 1
            sage: nbhd_patch.embedding_center()
            (0, 1, 0)

        Here we got two defining equations. The first one describes
        the singularity of the ambient space and the second is the
        pull-back of `x^2+y^2-1` ::

            sage: lp = LatticePolytope([(1,0,0), (1,1,0), (1,1,1), (1,0,1), (-2,-1,-1)],
            ....:                      lattice=ToricLattice(3))
            sage: X.<x,y,u,v,t> = CPRFanoToricVariety(Delta_polar=lp)
            sage: Y = X.subscheme(x*v + y*u + t)
            sage: cone = Cone([(1,0,0), (1,1,0), (1,1,1), (1,0,1)])
            sage: Y.affine_algebraic_patch(cone)
            Closed subscheme of Affine Space of dimension 4 over Rational Field defined by:
              z0*z2 - z1*z3,
              z1 + z3 + 1
        '''
    def neighborhood(self, point):
        """
        Return a toric algebraic scheme isomorphic to neighborhood of
        the ``point``.

        INPUT:

        - ``point`` -- a point of the toric algebraic scheme

        OUTPUT:

        An affine toric algebraic scheme (polynomial equations in an
        affine toric variety) with fixed
        :meth:`~AlgebraicScheme.embedding_morphism` and
        :meth:`~AlgebraicScheme.embedding_center`.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P.<x,y,z> = toric_varieties.P2()
            sage: S = P.subscheme(x + 2*y + 3*z)
            sage: s = S.point([0,-3,2]); s
            [0 : -3 : 2]
            sage: patch = S.neighborhood(s); patch
            Closed subscheme of 2-d affine toric variety defined by:
              x + 2*y + 6
            sage: patch.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of 2-d affine toric variety defined by: x + 2*y + 6
              To:   Closed subscheme of 2-d CPR-Fano toric variety
                    covered by 3 affine patches defined by: x + 2*y + 3*z
              Defn: Defined on coordinates by sending [x : y] to [-2*y - 6 : y : 2]
            sage: patch.embedding_center()
            [0 : -3]
            sage: patch.embedding_morphism()(patch.embedding_center())
            [0 : -3 : 2]

        A more complicated example::

            sage: # needs sage.libs.singular
            sage: dP6.<x0,x1,x2,x3,x4,x5> = toric_varieties.dP6()
            sage: twoP1 = dP6.subscheme(x0*x3)
            sage: patch = twoP1.neighborhood([0,1,2, 3,4,5]); patch
            Closed subscheme of 2-d affine toric variety defined by:
              3*x0
            sage: patch.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of 2-d affine toric variety defined by: 3*x0
              To:   Closed subscheme of 2-d CPR-Fano toric variety
                    covered by 6 affine patches defined by: x0*x3
              Defn: Defined on coordinates by sending [x0 : x1] to [0 : x1 : 2 : 3 : 4 : 5]
            sage: patch.embedding_center()
            [0 : 1]
            sage: patch.embedding_morphism()(patch.embedding_center())
            [0 : 1 : 2 : 3 : 4 : 5]
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        OUTPUT: integer; if ``self`` is empty, `-1` is returned

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.inject_variables()
            Defining s, t, x, y
            sage: P1 = P1xP1.subscheme(s - t)
            sage: P1.dimension()
            1
            sage: P1xP1.subscheme([s - t, (s-t)^2]).dimension()
            1
            sage: P1xP1.subscheme([s, t]).dimension()
            -1
        """
    def is_smooth(self, point=None):
        """
        Test whether the algebraic subscheme is smooth.

        INPUT:

        - ``point`` -- a point or ``None`` (default); the point to
          test smoothness at

        OUTPUT:

        boolean; if no point was specified, returns whether the
        algebraic subscheme is smooth everywhere. Otherwise,
        smoothness at the specified point is tested.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: cuspidal_curve = P2.subscheme([y^2*z - x^3])
            sage: cuspidal_curve
            Closed subscheme of 2-d CPR-Fano toric variety covered by 3 affine patches defined by:
              -x^3 + y^2*z
            sage: cuspidal_curve.is_smooth([1,1,1])
            True
            sage: cuspidal_curve.is_smooth([0,0,1])
            False
            sage: cuspidal_curve.is_smooth()
            False

        Any sufficiently generic cubic hypersurface is smooth::

            sage: P2.subscheme([y^2*z-x^3+z^3+1/10*x*y*z]).is_smooth()                  # needs sage.libs.singular
            True

        A more complicated example::

            sage: # needs sage.libs.singular
            sage: dP6.<x0,x1,x2,x3,x4,x5> = toric_varieties.dP6()
            sage: disjointP1s = dP6.subscheme(x0*x3)
            sage: disjointP1s.is_smooth()
            True
            sage: intersectingP1s = dP6.subscheme(x0*x1)
            sage: intersectingP1s.is_smooth()
            False

        A smooth hypersurface in a compact singular toric variety::

            sage: # needs sage.libs.singular
            sage: lp = LatticePolytope([(1,0,0), (1,1,0), (1,1,1), (1,0,1), (-2,-1,-1)],
            ....:                      lattice=ToricLattice(3))
            sage: X.<x,y,u,v,t> = CPRFanoToricVariety(Delta_polar=lp)
            sage: Y = X.subscheme(x*v + y*u + t)
            sage: cone = Cone([(1,0,0), (1,1,0), (1,1,1), (1,0,1)])
            sage: Y.is_smooth()
            True
        """
    def is_nondegenerate(self):
        """
        Check if ``self`` is nondegenerate.

        OUTPUT:

        Whether the variety is nondegenerate, that is, the intersection
        with every open torus orbit is smooth and transversal.

        EXAMPLES::

            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: P2.subscheme([x^3 + y^3 + z^3]).is_nondegenerate()
            True
            sage: P2.subscheme([x*y*z]).is_nondegenerate()
            False
            sage: X = P2.subscheme([(x-y)^2*(x+y) + x*y*z + z^3])
            sage: X.is_smooth()
            True
            sage: X.is_nondegenerate()
            False

        A K3 surface in `\\mathbf{P}^1 \\times \\mathbf{P}^1 \\times \\mathbf{P}^1`::

            sage: diamond = lattice_polytope.cross_polytope(3)
            sage: fan = FaceFan(diamond)
            sage: P1xP1xP1 = ToricVariety(fan)
            sage: z0, z1, z2, z3, z4, z5 = P1xP1xP1.gens()
            sage: t = 5
            sage: F = z0^2*z1^2*z2^2 + z1^2*z2^2*z3^2 + z0^2*z2^2*z4^2\\\n            ....: + z2^2*z3^2*z4^2 + t*z0*z1*z2*z3*z4*z5 + z0^2*z1^2*z5^2\\\n            ....: + z1^2*z3^2*z5^2 + z0^2*z4^2*z5^2 + z3^2*z4^2*z5^2
            sage: X = P1xP1xP1.subscheme([F])
            sage: X.is_smooth()
            True
            sage: X.is_nondegenerate()
            False

        Taking a random change of variables breaks the symmetry, but
        makes the surface nondegenerate::

            sage: F1 = F.subs(z0=1*z0 + 1*z3, z3=1*z0 + 2*z3,
            ....:             z1=-2*z1 + -1*z4, z4=1*z1 + 2*z4,
            ....:             z2=-3*z2 + -1*z5, z5=-3*z2 + 2*z5)
            sage: Y = P1xP1xP1.subscheme([F1])
            sage: Y.is_smooth()
            True
            sage: Y.is_nondegenerate()
            True

        This example is from Hamm, :arxiv:`1106.1826v1`. It addresses
        an issue raised at :issue:`15239`::

            sage: X = toric_varieties.WP([1,4,2,3], names='z0 z1 z2 z3')
            sage: X.inject_variables()
            Defining z0, z1, z2, z3
            sage: g0 = z1^3 + z2^6 + z3^4
            sage: g = g0 - 2*z3^2*z0^6 + z2*z0^10 + z0^12
            sage: Y = X.subscheme([g])
            sage: Y.is_nondegenerate()
            False

        It handles nonzero characteristic::

            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: f = x^5 + 2*x*y^4 + y^5 - 2*y^3*z^2 + x*z^4 - 2*z^5
            sage: P2.change_ring(GF(5)).subscheme([f]).is_nondegenerate()
            True
            sage: P2.change_ring(GF(7)).subscheme([f]).is_nondegenerate()
            False

        TESTS:

        Some corner cases discussed at :issue:`15239`::

            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: P2.subscheme([]).is_nondegenerate()
            False
            sage: P2.subscheme([x]).is_nondegenerate()
            False
        """
    def is_schon(self):
        """
        Check if ``self`` is schon (nondegenerate).

        See :meth:`is_nondegenerate` for further documentation.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: X = P2.subscheme([(x-y)^2*(x+y) + x*y*z + z^3])
            sage: X.is_smooth()
            True
            sage: X.is_schon()
            False
        """

class AlgebraicScheme_subscheme_affine_toric(AlgebraicScheme_subscheme_toric):
    """
    Construct an algebraic subscheme of an affine toric variety.

    .. WARNING::

        You should not create objects of this class directly. The preferred
        method to construct such subschemes is to use
        :meth:`~ToricVariety_field.subscheme` method of
        :class:`toric varieties <ToricVariety_field>`.

    INPUT:

    - ``toric_variety`` -- ambient :class:`affine toric variety
      <ToricVariety_field>`

    - ``polynomials`` -- single polynomial, list, or ideal of defining
      polynomials in the coordinate ring of ``toric_variety``

    OUTPUT:

    A :class:`algebraic subscheme of an affine toric variety
    <AlgebraicScheme_subscheme_affine_toric>`.

    TESTS::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1xP1.inject_variables()
        Defining s, t, x, y
        sage: import sage.schemes.toric.toric_subscheme as SCM
        sage: X = SCM.AlgebraicScheme_subscheme_toric(
        ....:       P1xP1, [x*s + y*t, x^3 + y^3])
        sage: X
        Closed subscheme of 2-d CPR-Fano toric variety
        covered by 4 affine patches defined by:
          s*x + t*y,
          x^3 + y^3

    A better way to construct the same scheme as above::

        sage: P1xP1.subscheme([x*s + y*t, x^3 + y^3])
        Closed subscheme of 2-d CPR-Fano toric variety
        covered by 4 affine patches defined by:
          s*x + t*y,
          x^3 + y^3
    """
    def __init__(self, toric_variety, polynomials) -> None:
        """
        See :class:`AlgebraicScheme_subscheme_toric` for documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1xP1.inject_variables()
            Defining s, t, x, y
            sage: import sage.schemes.toric.toric_subscheme as SCM
            sage: X = SCM.AlgebraicScheme_subscheme_toric(
            ....:       P1xP1, [x*s + y*t, x^3 + y^3])
            sage: X
            Closed subscheme of 2-d CPR-Fano toric variety
            covered by 4 affine patches defined by:
              s*x + t*y,
              x^3 + y^3
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P1xP1.<s0,s1,t0,t1> = toric_varieties.P1xP1()
            sage: P1 = P1xP1.subscheme(s0 - s1)
            sage: P1.dimension()
            1

        A more complicated example where the ambient toric variety is
        not smooth::

            sage: # needs sage.libs.singular
            sage: X.<x,y> = toric_varieties.A2_Z2()
            sage: X.is_smooth()
            False
            sage: Y = X.subscheme([x*y, x^2]); Y
            Closed subscheme of 2-d affine toric variety defined by:
              x*y,
              x^2
            sage: Y.dimension()
            1
        """
    def is_smooth(self, point=None):
        """
        Test whether the algebraic subscheme is smooth.

        INPUT:

        - ``point`` -- a point or ``None`` (default); the point to
          test smoothness at

        OUTPUT:

        boolean; if no point was specified, returns whether the
        algebraic subscheme is smooth everywhere. Otherwise,
        smoothness at the specified point is tested.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: A2.<x,y> = toric_varieties.A2()
            sage: cuspidal_curve = A2.subscheme([y^2 - x^3])
            sage: cuspidal_curve
            Closed subscheme of 2-d affine toric variety defined by:
              -x^3 + y^2
            sage: cuspidal_curve.is_smooth([1,1])
            True
            sage: cuspidal_curve.is_smooth([0,0])
            False
            sage: cuspidal_curve.is_smooth()
            False
            sage: circle = A2.subscheme(x^2 + y^2 - 1)
            sage: circle.is_smooth([1,0])
            True
            sage: circle.is_smooth()
            True

        A more complicated example where the ambient toric variety is
        not smooth::

            sage: # needs sage.libs.singular
            sage: X.<x,y> = toric_varieties.A2_Z2()    # 2-d affine space mod Z/2
            sage: X.is_smooth()
            False
            sage: Y = X.subscheme([x*y, x^2])   # (twice the x=0 curve) mod Z/2
            sage: Y
            Closed subscheme of 2-d affine toric variety defined by:
              x*y,
              x^2
            sage: Y.dimension()   # Y is a Weil divisor but not Cartier
            1
            sage: Y.is_smooth()
            True
            sage: Y.is_smooth([0,0])
            True
        """
