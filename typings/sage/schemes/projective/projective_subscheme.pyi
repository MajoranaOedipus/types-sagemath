from sage.arith.misc import binomial as binomial
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme
from sage.schemes.projective.projective_morphism import SchemeMorphism_polynomial_projective_subscheme_field as SchemeMorphism_polynomial_projective_subscheme_field

class AlgebraicScheme_subscheme_projective(AlgebraicScheme_subscheme):
    """
    Construct an algebraic subscheme of projective space.

    .. WARNING::

        You should not create objects of this class directly. The
        preferred method to construct such subschemes is to use
        :meth:`~sage.schemes.projective.projective_space.ProjectiveSpace_field.subscheme`
        method of :class:`projective space
        <sage.schemes.projective.projective_space.ProjectiveSpace_field>`.

    INPUT:

    - ``A`` -- ambient :class:`projective space
      <sage.schemes.projective.projective_space.ProjectiveSpace_field>`

    - ``polynomials`` -- single polynomial, ideal or iterable of
      defining homogeneous polynomials

    EXAMPLES::

        sage: P.<x, y, z> = ProjectiveSpace(2, QQ)
        sage: P.subscheme([x^2 - y*z])
        Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
          x^2 - y*z

    TESTS::

        sage: from sage.schemes.projective.projective_subscheme import AlgebraicScheme_subscheme_projective
        sage: AlgebraicScheme_subscheme_projective(P, [x^2-y*z])
        Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
          x^2 - y*z
    """
    def point(self, v, check: bool = True):
        """
        Create a point on this projective subscheme.

        INPUT:

        - ``v`` -- anything that defines a point

        - ``check`` -- boolean (default: ``True``); whether
          to check the defining data for consistency

        OUTPUT: a point of the subscheme

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P2.subscheme([x - y, y - z])
            sage: X.point([1,1,1])
            (1 : 1 : 1)

        ::

            sage: P2.<x,y> = ProjectiveSpace(QQ, 1)
            sage: X = P2.subscheme([y])
            sage: X.point(infinity)
            (1 : 0)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: X = P.subscheme(x^2 + 2*y^2)
            sage: X.point(infinity)
            Traceback (most recent call last):
            ...
            TypeError: Coordinates [1, 0] do not define a point on Closed subscheme
            of Projective Space of dimension 1 over Rational Field defined by:
              x^2 + 2*y^2
        """
    def dimension(self):
        """
        Return the dimension of the projective algebraic subscheme.

        OUTPUT: integer

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: P2.<x,y,z> = ProjectiveSpace(2, QQ)
            sage: P2.subscheme([]).dimension()
            2
            sage: P2.subscheme([x]).dimension()
            1
            sage: P2.subscheme([x^5]).dimension()
            1
            sage: P2.subscheme([x^2 + y^2 - z^2]).dimension()
            1
            sage: P2.subscheme([x*(x-z), y*(y-z)]).dimension()
            0

        Something less obvious::

            sage: P3.<x,y,z,w,t> = ProjectiveSpace(4, QQ)
            sage: X = P3.subscheme([x^2, x^2*y^2 + z^2*t^2,
            ....:                   z^2 - w^2, 10*x^2 + w^2 - z^2]); X
            Closed subscheme of Projective Space of dimension 4 over Rational Field defined by:
              x^2,
              x^2*y^2 + z^2*t^2,
              z^2 - w^2,
              10*x^2 - z^2 + w^2
            sage: X.dimension()                                                         # needs sage.libs.singular
            1
        """
    def affine_patch(self, i, AA=None):
        """
        Return the `i`-th affine patch of this projective scheme.

        This is the intersection with this `i`-th affine patch of
        its ambient space.

        INPUT:

        - ``i`` -- integer between 0 and dimension of ``self``, inclusive

        - ``AA`` -- (default: ``None``) ambient affine space, this
          is constructed if it is not given

        OUTPUT:

        An affine algebraic scheme with fixed
        :meth:`embedding_morphism` equal to the default
        :meth:`projective_embedding` map`.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: PP = ProjectiveSpace(2, QQ, names='X,Y,Z')
            sage: X,Y,Z = PP.gens()
            sage: C = PP.subscheme(X^3*Y + Y^3*Z + Z^3*X)
            sage: U = C.affine_patch(0); U
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              Y^3*Z + Z^3 + Y
            sage: U.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                    defined by: Y^3*Z + Z^3 + Y
              To:   Closed subscheme of Projective Space of dimension 2 over Rational Field
                    defined by: X^3*Y + Y^3*Z + X*Z^3
              Defn: Defined on coordinates by sending (Y, Z) to (1 : Y : Z)
            sage: U.projective_embedding() is U.embedding_morphism()
            True

        ::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A.subscheme([x - y*z])
            sage: Y = X.projective_embedding(1).codomain()                              # needs sage.libs.singular
            sage: Y.affine_patch(1, A).ambient_space() == A                             # needs sage.libs.singular
            True

        ::

            sage: P.<u,v,w> = ProjectiveSpace(2, ZZ)
            sage: S = P.subscheme([u^2 - v*w])
            sage: A.<x, y> = AffineSpace(2, ZZ)
            sage: S.affine_patch(1, A)                                                  # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Integer Ring defined by:
              x^2 - y
        """
    def neighborhood(self, point):
        """
        Return an affine algebraic subscheme isomorphic to a
        neighborhood of the ``point``.

        INPUT:

        - ``point`` -- a point of the projective subscheme

        OUTPUT:

        An affine algebraic scheme (polynomial equations in affine
        space) ``result`` such that

        * :meth:`embedding_morphism
          <AlgebraicScheme.embedding_morphism>` is an isomorphism to a
          neighborhood of ``point``

        * :meth:`embedding_center <AlgebraicScheme.embedding_center>`
          is mapped to ``point``.

        EXAMPLES::

            sage: P.<x,y,z>= ProjectiveSpace(QQ, 2)
            sage: S = P.subscheme(x + 2*y + 3*z)
            sage: s = S.point([0,-3,2]); s
            (0 : -3/2 : 1)
            sage: patch = S.neighborhood(s); patch
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x + 3*z
            sage: patch.embedding_morphism()
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                    defined by: x + 3*z
              To:   Closed subscheme of Projective Space of dimension 2 over Rational Field
                    defined by: x + 2*y + 3*z
              Defn: Defined on coordinates by sending (x, z) to (x : -3/2 : z + 1)
            sage: patch.embedding_center()
            (0, 0)
            sage: patch.embedding_morphism()([0,0])
            (0 : -3/2 : 1)
            sage: patch.embedding_morphism()(patch.embedding_center())
            (0 : -3/2 : 1)
        """
    def is_smooth(self, point=None) -> bool:
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
            sage: P2.<x,y,z> = ProjectiveSpace(2, QQ)
            sage: cuspidal_curve = P2.subscheme([y^2*z - x^3])
            sage: cuspidal_curve
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              -x^3 + y^2*z
            sage: cuspidal_curve.is_smooth([1,1,1])
            True
            sage: cuspidal_curve.is_smooth([0,0,1])
            False
            sage: cuspidal_curve.is_smooth()
            False
            sage: P2.subscheme([y^2*z - x^3 + z^3 + 1/10*x*y*z]).is_smooth()
            True

        TESTS::

            sage: H = P2.subscheme(x)                                                   # needs sage.libs.singular
            sage: H.is_smooth()  # one of the few cases where the cone over the subvariety is smooth                    # needs sage.libs.singular
            True
        """
    def orbit(self, f, N) -> list:
        """
        Return the orbit of this scheme by ``f``.

        If `N` is an integer it returns `[self,f(self),\\ldots,f^N(self)]`.
        If `N` is a list or tuple `N=[m,k]` it returns `[f^m(self),\\ldots,f^k(self)`].

        INPUT:

        - ``f`` -- a :class:`DynamicalSystem_projective` with ``self`` in ``f.domain()``

        - ``N`` -- nonnegative integer or list or tuple of two nonnegative integers

        OUTPUT: list of projective subschemes

        EXAMPLES::

            sage: # needs sage.libs.singular sage.schemes
            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: f = DynamicalSystem_projective([(x-2*y)^2, (x-2*z)^2,
            ....:                                 (x-2*w)^2, x^2])
            sage: f.orbit(P.subscheme([x]), 5)
            [Closed subscheme of Projective Space of dimension 3 over Rational Field
              defined by: x,
             Closed subscheme of Projective Space of dimension 3 over Rational Field
              defined by: w,
             Closed subscheme of Projective Space of dimension 3 over Rational Field
              defined by: z - w,
             Closed subscheme of Projective Space of dimension 3 over Rational Field
              defined by: y - z,
             Closed subscheme of Projective Space of dimension 3 over Rational Field
              defined by: x - y,
             Closed subscheme of Projective Space of dimension 3 over Rational Field
              defined by: x - w]

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P1.<u,v> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(PS, P1)
            sage: f = H([x^2, y^2])
            sage: X = PS.subscheme([x - y])
            sage: X.orbit(f, 2)
            Traceback (most recent call last):
            ...
            TypeError: map must be a dynamical system for iteration

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])                       # needs sage.schemes
            sage: X = PS.subscheme([x - y])
            sage: X.orbit(f, [-1,2])                                                    # needs sage.schemes
            Traceback (most recent call last):
            ...
            TypeError: orbit bounds must be nonnegative
        """
    def nth_iterate(self, f, n):
        """
        The `n`-th forward image of this scheme by the map ``f``.

        INPUT:

        - ``f`` -- a :class:`DynamicalSystem_projective` with ``self`` in ``f.domain()``

        - ``n`` -- positive integer

        OUTPUT:

        - A subscheme in ``f.codomain()``

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: f = DynamicalSystem_projective([y^2, z^2, x^2, w^2])                  # needs sage.schemes
            sage: f.nth_iterate(P.subscheme([x - w, y - z]), 3)                         # needs sage.libs.singular sage.schemes
            Closed subscheme of Projective Space of dimension 3 over Rational Field
             defined by:
              y - z,
              x - w

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])                       # needs sage.schemes
            sage: X = PS.subscheme([x - y])
            sage: X.nth_iterate(f, -2)                                                  # needs sage.libs.singular sage.schemes
            Traceback (most recent call last):
            ...
            TypeError: must be a forward orbit

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: P2.<u,v,w> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(PS, P2)
            sage: f = H([x^2, y^2, z^2])
            sage: X = PS.subscheme([x - y])
            sage: X.nth_iterate(f, 2)
            Traceback (most recent call last):
            ...
            TypeError: map must be a dynamical system for iteration

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])                       # needs sage.schemes
            sage: X = PS.subscheme([x - y])
            sage: X.nth_iterate(f, 2.5)                                                 # needs sage.schemes
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer
        """
    def preimage(self, f, k: int = 1, check: bool = True):
        """
        The subscheme that maps to this scheme by the map `f^k`.

        In particular, `f^{-k}(V(h_1,\\ldots,h_t)) = V(h_1 \\circ f^k, \\ldots, h_t \\circ f^k)`.
        Map must be a morphism and also must be an endomorphism for `k > 1`.

        INPUT:

        - ``f`` -- a map whose codomain contains this scheme

        - ``k`` -- positive integer

        - ``check`` -- boolean; if ``False`` no input checking is done

        OUTPUT: a subscheme in the domain of ``f``

        EXAMPLES::

            sage: PS.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: H = End(PS)
            sage: f = H([y^2, x^2, z^2])
            sage: X = PS.subscheme([x - y])
            sage: X.preimage(f)                                                         # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Integer Ring
             defined by:
              -x^2 + y^2

        ::

            sage: P.<x,y,z,w,t> = ProjectiveSpace(QQ, 4)
            sage: H = End(P)
            sage: f = H([x^2 - y^2, y^2, z^2, w^2, t^2 + w^2])
            sage: f.rational_preimages(P.subscheme([x - z, t^2, w - t]))                # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 4 over Rational Field
             defined by:
              x^2 - y^2 - z^2,
              w^4 + 2*w^2*t^2 + t^4,
              -t^2

        ::

            sage: P1.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P3.<u,v,w,t> = ProjectiveSpace(QQ, 3)
            sage: H = Hom(P1, P3)
            sage: X = P3.subscheme([u - v, 2*u - w, u + t])
            sage: f = H([x^2, y^2, x^2 + y^2, x*y])
            sage: X.preimage(f)                                                         # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1 over Rational Field
             defined by:
              x^2 - y^2,
              x^2 - y^2,
              x^2 + x*y

        ::

            sage: P1.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P3.<u,v,w,t> = ProjectiveSpace(QQ, 3)
            sage: H = Hom(P3, P1)
            sage: X = P1.subscheme([x - y])
            sage: f = H([u^2, v^2])
            sage: X.preimage(f)                                                         # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: map must be a morphism

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: H = End(PS)
            sage: f = H([x^2, x^2, x^2])
            sage: X = PS.subscheme([x - y])
            sage: X.preimage(f)                                                         # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: map must be a morphism

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: P1.<u,v> = ProjectiveSpace(ZZ, 1)
            sage: Y = P1.subscheme([u^2 - v^2])
            sage: H = End(PS)
            sage: f = H([x^2, y^2, z^2])
            sage: Y.preimage(f)                                                         # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: subscheme must be in ambient space of codomain

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: Y = P.subscheme([x - y])
            sage: H = End(P)
            sage: f = H([x^2, y^2, z^2])
            sage: Y.preimage(f, k=2)                                                    # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field
             defined by:
              x^4 - y^4
        """
    def dual(self):
        """
        Return the projective dual of the given subscheme of projective space.

        INPUT:

        - ``X`` -- a subscheme of projective space. At present, ``X`` is
          required to be an irreducible and reduced hypersurface defined
          over `\\QQ` or a finite field.

        OUTPUT: the dual of ``X`` as a subscheme of the dual projective space

        EXAMPLES:

        The dual of a smooth conic in the plane is also a smooth conic::

            sage: R.<x, y, z> = QQ[]
            sage: P.<x, y, z> = ProjectiveSpace(2, QQ)
            sage: I = R.ideal(x^2 + y^2 + z^2)
            sage: X = P.subscheme(I)
            sage: X.dual()                                                              # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field
             defined by:
              y0^2 + y1^2 + y2^2

        The dual of the twisted cubic curve in projective 3-space is a singular
        quartic surface. In the following example, we compute the dual of this
        surface, which by double duality is equal to the twisted cubic itself.
        The output is the twisted cubic as an intersection of three quadrics::

            sage: R.<x, y, z, w> = QQ[]
            sage: P.<x, y, z, w> = ProjectiveSpace(3, QQ)
            sage: I = R.ideal(y^2*z^2 - 4*x*z^3 - 4*y^3*w + 18*x*y*z*w - 27*x^2*w^2)
            sage: X = P.subscheme(I)
            sage: X.dual()                                                              # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 3 over
             Rational Field defined by:
              y2^2 - y1*y3,
              y1*y2 - y0*y3,
              y1^2 - y0*y2

        The singular locus of the quartic surface in the last example
        is itself supported on a twisted cubic::

            sage: X.Jacobian().radical()                                                # needs sage.libs.singular
            Ideal (z^2 - 3*y*w, y*z - 9*x*w, y^2 - 3*x*z) of Multivariate
            Polynomial Ring in x, y, z, w over Rational Field

        An example over a finite field::

            sage: R = PolynomialRing(GF(61), 'a,b,c')
            sage: P.<a, b, c> = ProjectiveSpace(2, R.base_ring())
            sage: X = P.subscheme(R.ideal(a*a + 2*b*b + 3*c*c))
            sage: X.dual()                                                              # needs sage.libs.singular sage.rings.finite_rings
            Closed subscheme of Projective Space of dimension 2 over
             Finite Field of size 61 defined by:
              y0^2 - 30*y1^2 - 20*y2^2

        TESTS::

            sage: # needs sage.rings.padics
            sage: R = PolynomialRing(Qp(3), 'a,b,c')
            sage: P.<a, b, c> = ProjectiveSpace(2, R.base_ring())
            sage: X = P.subscheme(R.ideal(a*a + 2*b*b + 3*c*c))
            sage: X.dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: base ring must be QQ or a finite field
        """
    def degree(self):
        """
        Return the degree of this projective subscheme.

        If `P(t) = a_{m}t^m + \\ldots + a_{0}` is the Hilbert
        polynomial of this subscheme, then the degree is `a_{m} m!`.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z,w,t,u> = ProjectiveSpace(QQ, 5)
            sage: X = P.subscheme([x^7 + x*y*z*t^4 - u^7])
            sage: X.degree()                                                            # needs sage.libs.singular
            7

            sage: P.<x,y,z,w> = ProjectiveSpace(GF(13), 3)
            sage: X = P.subscheme([y^3 - w^3, x + 7*z])
            sage: X.degree()                                                            # needs sage.libs.singular
            3

            sage: # needs sage.libs.singular sage.schemes
            sage: P.<x,y,z,w,u> = ProjectiveSpace(QQ, 4)
            sage: C = P.curve([x^7 - y*z^3*w^2*u, w*x^2 - y*u^2, z^3 + y^3])
            sage: C.degree()
            63
        """
    def intersection_multiplicity(self, X, P):
        """
        Return the intersection multiplicity of this subscheme and the subscheme ``X`` at the point ``P``.

        This uses the intersection_multiplicity function for affine subschemes on affine patches of this subscheme
        and ``X`` that contain ``P``.

        INPUT:

        - ``X`` -- subscheme in the same ambient space as this subscheme

        - ``P`` -- a point in the intersection of this subscheme with ``X``

        OUTPUT: integer

        EXAMPLES::

            sage: # needs sage.schemes
            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: C = Curve([x^4 - z^2*y^2], P)
            sage: D = Curve([y^4*z - x^5 - x^3*z^2], P)
            sage: Q1 = P([0,1,0])
            sage: C.intersection_multiplicity(D, Q1)                                    # needs sage.libs.singular
            4
            sage: Q2 = P([0,0,1])
            sage: C.intersection_multiplicity(D, Q2)                                    # needs sage.libs.singular
            6

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^4 + 1)
            sage: P.<x,y,z,w> = ProjectiveSpace(K, 3)
            sage: X = P.subscheme([x^2 + y^2 - z*w])
            sage: Y = P.subscheme([y*z - x*w, z - w])
            sage: Q1 = P([b^2,1,0,0])
            sage: X.intersection_multiplicity(Y, Q1)                                    # needs sage.libs.singular
            1
            sage: Q2 = P([1/2*b^3 - 1/2*b, 1/2*b^3 - 1/2*b, 1, 1])
            sage: X.intersection_multiplicity(Y, Q2)                                    # needs sage.libs.singular
            1

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: X = P.subscheme([x^2 - z^2, y^3 - w*x^2])
            sage: Y = P.subscheme([w^2 - 2*x*y + z^2, y^2 - w^2])
            sage: Q = P([1,1,-1,1])
            sage: X.intersection_multiplicity(Y, Q)                                     # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: the intersection of this subscheme and (=Closed subscheme of Affine Space of dimension 3
            over Rational Field defined by: z^2 + w^2 - 2*y, y^2 - w^2)
            must be proper and finite
        """
    def multiplicity(self, P):
        """
        Return the multiplicity of ``P`` on this subscheme.

        This is computed as the multiplicity of the corresponding point on an affine patch of this subscheme
        that contains ``P``. This subscheme must be defined over a field. An error is returned if ``P``
        not a point on this subscheme.

        INPUT:

        - ``P`` -- a point on this subscheme

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z,w,t> = ProjectiveSpace(QQ, 4)
            sage: X = P.subscheme([y^2 - x*t, w^7 - t*w*x^5 - z^7])
            sage: Q1 = P([0,0,1,1,1])
            sage: X.multiplicity(Q1)                                                    # needs sage.libs.singular
            1
            sage: Q2 = P([1,0,0,0,0])
            sage: X.multiplicity(Q2)                                                    # needs sage.libs.singular
            3
            sage: Q3 = P([0,0,0,0,1])
            sage: X.multiplicity(Q3)                                                    # needs sage.libs.singular
            7

        ::

            sage: # needs sage.rings.real_mpfr
            sage: P.<x,y,z,w> = ProjectiveSpace(CC, 3)
            sage: X = P.subscheme([z^5*x^2*w - y^8])
            sage: Q = P([2,0,0,1])
            sage: X.multiplicity(Q)                                                     # needs sage.libs.singular
            5

        ::

            sage: # needs sage.libs.singular sage.schemes
            sage: P.<x,y,z,w> = ProjectiveSpace(GF(29), 3)
            sage: C = Curve([y^17 - x^5*w^4*z^8, x*y - z^2], P)
            sage: Q = P([3,0,0,1])
            sage: C.multiplicity(Q)
            8
        """
    def veronese_embedding(self, d, CS=None, order: str = 'lex'):
        """
        Return the degree ``d`` Veronese embedding of this projective subscheme.

        INPUT:

        - ``d`` -- positive integer

        - ``CS`` -- (default: ``None``) a projective ambient space to embed
          into. If the projective ambient space of this subscheme is of
          dimension `N`, the dimension of ``CS`` must be
          `\\binom{N + d}{d} - 1`. This is constructed if not specified.

        - ``order`` -- string (default: ``'lex'``); a monomial order to use to
          arrange the monomials defining the embedding. The monomials will be
          arranged from greatest to least with respect to this order.

        OUTPUT: a scheme morphism from this subscheme to its image by the
        degree ``d`` Veronese embedding

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: L = P.subscheme([y - x])
            sage: v = L.veronese_embedding(2); v                                        # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Projective Space of dimension 2
                    over Rational Field defined by: -x + y
              To:   Closed subscheme of Projective Space of dimension 5
                    over Rational Field defined by:
                      -x4^2 + x3*x5,
                      x2 - x4,
                      x1 - x3,
                      x0 - x3
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^2 : x*y : x*z : y^2 : y*z : z^2)
            sage: v.codomain().degree()                                                 # needs sage.libs.singular
            2
            sage: C = P.subscheme([y*z - x^2])
            sage: C.veronese_embedding(2).codomain().degree()                           # needs sage.libs.singular
            4

        twisted cubic::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: Q.<u,v,s,t> = ProjectiveSpace(QQ, 3)
            sage: P.subscheme([]).veronese_embedding(3, Q)                              # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Projective Space of dimension 1
                    over Rational Field defined by: (no polynomials)
              To:   Closed subscheme of Projective Space of dimension 3
                    over Rational Field defined by:
                      -s^2 + v*t,
                      -v*s + u*t,
                      -v^2 + u*s
              Defn: Defined on coordinates by sending (x : y) to
                    (x^3 : x^2*y : x*y^2 : y^3)
        """

class AlgebraicScheme_subscheme_projective_field(AlgebraicScheme_subscheme_projective):
    """
    Algebraic subschemes of projective spaces defined over fields.
    """
    def Chow_form(self):
        """
        Return the Chow form associated to this subscheme.

        For a `k`-dimensional subvariety of `\\mathbb{P}^N` of degree `D`.
        The `(N-k-1)`-dimensional projective linear subspaces of `\\mathbb{P}^N`
        meeting `X` form a hypersurface in the Grassmannian `G(N-k-1,N)`.
        The homogeneous form of degree `D` defining this hypersurface in Plucker
        coordinates is called the Chow form of `X`.

        The base ring needs to be a number field, finite field, or `\\QQbar`.

        ALGORITHM:

        For a `k`-dimension subscheme `X` consider the `k+1` linear forms
        `l_i = u_{i0}x_0 + \\cdots + u_{in}x_n`. Let `J` be the ideal in the
        polynomial ring `K[x_i,u_{ij}]` defined by the equations of `X` and the `l_i`.
        Let `J'` be the saturation of `J` with respect to the irrelevant ideal of
        the ambient projective space of `X`. The elimination ideal `I = J' \\cap K[u_{ij}]`
        is a principal ideal, let `R` be its generator. The Chow form is obtained by
        writing `R` as a polynomial in Plucker coordinates (i.e. bracket polynomials).
        [DS1994]_.

        OUTPUT: a homogeneous polynomial

        EXAMPLES::

            sage: P.<x0,x1,x2,x3> = ProjectiveSpace(GF(17), 3)
            sage: X = P.subscheme([x3 + x1, x2 - x0, x2 - x3])
            sage: X.Chow_form()                                                         # needs sage.libs.singular
            t0 - t1 + t2 + t3

        ::

            sage: P.<x0,x1,x2,x3> = ProjectiveSpace(QQ, 3)
            sage: X = P.subscheme([x3^2 - 101*x1^2 - 3*x2*x0])
            sage: X.Chow_form()                                                         # needs sage.libs.singular
            t0^2 - 101*t2^2 - 3*t1*t3

        ::

            sage: # needs sage.libs.singular
            sage: P.<x0,x1,x2,x3> = ProjectiveSpace(QQ, 3)
            sage: X = P.subscheme([x0*x2 - x1^2, x0*x3 - x1*x2, x1*x3 - x2^2])
            sage: Ch = X.Chow_form(); Ch
            t2^3 + 2*t2^2*t3 + t2*t3^2 - 3*t1*t2*t4 - t1*t3*t4 + t0*t4^2 + t1^2*t5
            sage: Y = P.subscheme_from_Chow_form(Ch, 1); Y
            Closed subscheme of Projective Space of dimension 3 over Rational Field
             defined by:
              x2^2*x3 - x1*x3^2,                    -x2^3 + x0*x3^2,
              -x2^2*x3 + x1*x3^2,                   x1*x2*x3 - x0*x3^2,
              3*x1*x2^2 - 3*x0*x2*x3,               -2*x1^2*x3 + 2*x0*x2*x3,
              -3*x1^2*x2 + 3*x0*x1*x3,              x1^3 - x0^2*x3,
              x2^3 - x1*x2*x3,                      -3*x1*x2^2 + 2*x1^2*x3 + x0*x2*x3,
              2*x0*x2^2 - 2*x0*x1*x3,               3*x1^2*x2 - 2*x0*x2^2 - x0*x1*x3,
              -x0*x1*x2 + x0^2*x3,                  -x0*x1^2 + x0^2*x2,
              -x1^3 + x0*x1*x2,                     x0*x1^2 - x0^2*x2
            sage: I = Y.defining_ideal()
            sage: I.saturation(I.ring().ideal(list(I.ring().gens())))[0]
            Ideal (x2^2 - x1*x3, x1*x2 - x0*x3, x1^2 - x0*x2)
             of Multivariate Polynomial Ring in x0, x1, x2, x3 over Rational Field
        """
    def global_height(self, prec=None):
        """
        Return the (projective) global height of the subscheme.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default ``RealField`` precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: NF.<a> = NumberField(x^2 - 5)
            sage: P.<x,y,z> = ProjectiveSpace(NF, 2)
            sage: X = P.subscheme([x^2 + y*z, 2*y*z, 3*x*y])
            sage: X.global_height()                                                     # needs sage.libs.singular
            0.000000000000000

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme([z^2 - 101*y^2 - 3*x*z])
            sage: X.global_height()             # long time                             # needs sage.libs.singular
            4.61512051684126
        """
    def local_height(self, v, prec=None):
        """
        Return the (projective) local height of the subscheme.

        INPUT:

        - ``v`` -- a prime or prime ideal of the base ring

        - ``prec`` -- desired floating point precision (default:
          default ``RealField`` precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: NF.<a> = NumberField(x^2 - 5)
            sage: I = NF.ideal(3)
            sage: P.<x,y,z> = ProjectiveSpace(NF, 2)
            sage: X = P.subscheme([3*x*y - 5*x*z, y^2])
            sage: X.local_height(I)                                                     # needs sage.libs.singular
            0.000000000000000

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme([z^2 - 101*y^2 - 3*x*z])
            sage: X.local_height(2)                                                     # needs sage.libs.singular
            0.000000000000000
        """
    def local_height_arch(self, i, prec=None):
        """
        Return the local height at the ``i``-th infinite place of the subscheme.

        INPUT:

        - ``i`` -- integer

        - ``prec`` -- desired floating point precision (default:
          default ``RealField`` precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: NF.<a> = NumberField(x^2 - 5)
            sage: P.<x,y,z> = ProjectiveSpace(NF, 2)
            sage: X = P.subscheme([x^2 + y*z, 3*x*y])
            sage: X.local_height_arch(1)                                                # needs sage.libs.singular
            0.0000000000000000000000000000000

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme([z^2 - 101*y^2 - 3*x*z])
            sage: X.local_height_arch(1)                                                # needs sage.libs.singular
            4.61512051684126
        """
