from .affine_morphism import SchemeMorphism_polynomial_affine_subscheme_field as SchemeMorphism_polynomial_affine_subscheme_field
from sage.categories.fields import Fields as Fields
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme

class AlgebraicScheme_subscheme_affine(AlgebraicScheme_subscheme):
    """
    An algebraic subscheme of affine space.

    INPUT:

    - ``A`` -- ambient affine space

    - ``polynomials`` -- single polynomial, ideal or iterable of defining
      polynomials

    EXAMPLES::

        sage: A3.<x, y, z> = AffineSpace(QQ, 3)
        sage: A3.subscheme([x^2 - y*z])
        Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
          x^2 - y*z

    TESTS::

        sage: from sage.schemes.affine.affine_subscheme import AlgebraicScheme_subscheme_affine
        sage: AlgebraicScheme_subscheme_affine(A3, [x^2 - y*z])
        Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
          x^2 - y*z
    """
    def __init__(self, A, polynomials, embedding_center=None, embedding_codomain=None, embedding_images=None) -> None:
        """
        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: A.subscheme([y^2 - x*z - x*y])
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              -x*y + y^2 - x*z
        """
    def dimension(self):
        """
        Return the dimension of the affine algebraic subscheme.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: A.<x,y> = AffineSpace(2, QQ)
            sage: A.subscheme([]).dimension()
            2
            sage: A.subscheme([x]).dimension()
            1
            sage: A.subscheme([x^5]).dimension()
            1
            sage: A.subscheme([x^2 + y^2 - 1]).dimension()
            1
            sage: A.subscheme([x*(x-1), y*(y-1)]).dimension()
            0

        Something less obvious::

            sage: A.<x,y,z,w> = AffineSpace(4, QQ)
            sage: X = A.subscheme([x^2, x^2*y^2 + z^2, z^2 - w^2, 10*x^2 + w^2 - z^2])
            sage: X
            Closed subscheme of Affine Space of dimension 4 over Rational Field defined by:
              x^2,
              x^2*y^2 + z^2,
              z^2 - w^2,
              10*x^2 - z^2 + w^2
            sage: X.dimension()                                                         # needs sage.libs.singular
            1
        """
    def projective_embedding(self, i=None, PP=None):
        """
        Return a morphism from this affine scheme into an ambient projective
        space of the same dimension.

        The codomain of this morphism is the projective closure of this affine
        scheme in ``PP``, if given, or otherwise in a new projective space that
        is constructed.

        INPUT:

        - ``i`` -- integer (default: dimension of self = last coordinate);
          determines which projective embedding to compute. The embedding is
          that which has a 1 in the `i`-th coordinate, numbered from 0.

        - ``PP`` -- (default: ``None``) ambient projective space, i.e., ambient
          space of codomain of morphism; this is constructed if it is not given

        EXAMPLES::

            sage: A.<x, y, z> = AffineSpace(3, ZZ)
            sage: S = A.subscheme([x*y - z])
            sage: S.projective_embedding()                                              # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 3 over Integer Ring
                    defined by: x*y - z
              To:   Closed subscheme of Projective Space of dimension 3 over Integer Ring
                    defined by: x0*x1 - x2*x3
              Defn: Defined on coordinates by sending (x, y, z) to (x : y : z : 1)

        ::

            sage: A.<x, y, z> = AffineSpace(3, ZZ)
            sage: P = ProjectiveSpace(3, ZZ, 'u')
            sage: S = A.subscheme([x^2 - y*z])
            sage: S.projective_embedding(1, P)                                          # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 3 over Integer Ring
                    defined by: x^2 - y*z
              To:   Closed subscheme of Projective Space of dimension 3 over Integer Ring
                    defined by: u0^2 - u2*u3
              Defn: Defined on coordinates by sending (x, y, z) to (x : 1 : y : z)

        ::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A.subscheme([y - x^2, z - x^3])
            sage: X.projective_embedding()                                              # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 3 over Rational Field
                    defined by: -x^2 + y, -x^3 + z
              To:   Closed subscheme of Projective Space of dimension 3 over Rational Field
                    defined by: x0^2 - x1*x3, x0*x1 - x2*x3, x1^2 - x0*x2
              Defn: Defined on coordinates by sending (x, y, z) to (x : y : z : 1)

        When taking a closed subscheme of an affine space with a
        projective embedding, the subscheme inherits the embedding::

            sage: A.<u,v> = AffineSpace(2, QQ, default_embedding_index=1)
            sage: X = A.subscheme(u - v)                                                # needs sage.libs.singular
            sage: X.projective_embedding()                                              # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                    defined by: u - v
              To:   Closed subscheme of Projective Space of dimension 2 over Rational Field
                    defined by: x0 - x2
              Defn: Defined on coordinates by sending (u, v) to (u : 1 : v)
            sage: phi = X.projective_embedding()                                        # needs sage.libs.singular
            sage: psi = A.projective_embedding()
            sage: phi(X(2, 2)) == psi(A(X(2, 2)))                                       # needs sage.libs.singular
            True
        """
    def projective_closure(self, i=None, PP=None):
        """
        Return the projective closure of this affine subscheme.

        INPUT:

        - ``i`` -- (default: ``None``) determines the embedding to use to
          compute the projective closure of this affine subscheme. The
          embedding used is the one which has a 1 in the i-th coordinate,
          numbered from 0.

        - ``PP`` -- (default: ``None``) ambient projective space, i.e., ambient
          space of codomain of morphism; this is constructed if it is not given

        OUTPUT: a projective subscheme

        EXAMPLES::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: X = A.subscheme([x^2 - y, x*y - z, y^2 - w,
            ....:                  x*z - w, y*z - x*w, z^2 - y*w])
            sage: X.projective_closure()                                                # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 4 over Rational Field
             defined by:
              x0^2 - x1*x4,
              x0*x1 - x2*x4,
              x1^2 - x3*x4,
              x0*x2 - x3*x4,
              x1*x2 - x0*x3,
              x2^2 - x1*x3

        ::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: P.<a,b,c,d> = ProjectiveSpace(QQ, 3)
            sage: X = A.subscheme([z - x^2 - y^2])
            sage: X.projective_closure(1, P).ambient_space() == P                       # needs sage.libs.singular
            True
        """
    def is_smooth(self, point=None):
        """
        Test whether the algebraic subscheme is smooth.

        INPUT:

        - ``point`` -- a point or ``None`` (default). The point to
          test smoothness at

        OUTPUT:

        boolean; if no point was specified, returns whether the
        algebraic subscheme is smooth everywhere. Otherwise,
        smoothness at the specified point is tested.

        EXAMPLES::

            sage: A2.<x,y> = AffineSpace(2, QQ)
            sage: cuspidal_curve = A2.subscheme([y^2 - x^3])
            sage: cuspidal_curve
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              -x^3 + y^2
            sage: smooth_point = cuspidal_curve.point([1,1])
            sage: smooth_point in cuspidal_curve
            True
            sage: singular_point = cuspidal_curve.point([0,0])
            sage: singular_point in cuspidal_curve
            True
            sage: cuspidal_curve.is_smooth(smooth_point)                                # needs sage.libs.singular
            True
            sage: cuspidal_curve.is_smooth(singular_point)                              # needs sage.libs.singular
            False
            sage: cuspidal_curve.is_smooth()                                            # needs sage.libs.singular
            False
        """
    def intersection_multiplicity(self, X, P):
        """
        Return the intersection multiplicity of this subscheme and the subscheme ``X`` at the point ``P``.

        The intersection of this subscheme with ``X`` must be proper, that is `\\mathrm{codim}(self\\cap
        X) = \\mathrm{codim}(self) + \\mathrm{codim}(X)`, and must also be finite. We use Serre's Tor
        formula to compute the intersection multiplicity. If `I`, `J` are the defining ideals of ``self``, ``X``,
        respectively, then this is `\\sum_{i=0}^{\\infty}(-1)^i\\mathrm{length}(\\mathrm{Tor}_{\\mathcal{O}_{A,p}}^{i}
        (\\mathcal{O}_{A,p}/I,\\mathcal{O}_{A,p}/J))` where `A` is the affine ambient space of these subschemes.

        INPUT:

        - ``X`` -- subscheme in the same ambient space as this subscheme

        - ``P`` -- a point in the intersection of this subscheme with ``X``

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y^2 - x^3 - x^2], A)                                       # needs sage.libs.singular
            sage: D = Curve([y^2 + x^3], A)                                             # needs sage.libs.singular
            sage: Q = A([0,0])
            sage: C.intersection_multiplicity(D, Q)                                     # needs sage.libs.singular
            4

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^6 - 3*a^5 + 5*a^4 - 5*a^3 + 5*a^2 - 3*a + 1)
            sage: A.<x,y,z,w> = AffineSpace(K, 4)
            sage: X = A.subscheme([x*y, y*z + 7, w^3 - x^3])
            sage: Y = A.subscheme([x - z^3 + z + 1])
            sage: Q = A([0,
            ....:        -7*b^5 + 21*b^4 - 28*b^3 + 21*b^2 - 21*b + 14,
            ....:        -b^5 + 2*b^4 - 3*b^3 + 2*b^2 - 2*b,
            ....:        0])
            sage: X.intersection_multiplicity(Y, Q)                                     # needs sage.libs.singular
            3

        ::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A.subscheme([z^2 - 1])
            sage: Y = A.subscheme([z - 1, y - x^2])
            sage: Q = A([1,1,1])
            sage: X.intersection_multiplicity(Y, Q)                                     # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: the intersection of this subscheme and (=Closed subscheme of Affine Space of dimension 3
            over Rational Field defined by: z - 1, -x^2 + y) must be proper and finite

        ::

            sage: A.<x,y,z,w,t> = AffineSpace(QQ, 5)
            sage: X = A.subscheme([x*y, t^2*w, w^3*z])
            sage: Y = A.subscheme([y*w + z])
            sage: Q = A([0,0,0,0,0])
            sage: X.intersection_multiplicity(Y, Q)                                     # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: the intersection of this subscheme and (=Closed subscheme of Affine Space of dimension 5
            over Rational Field defined by: y*w + z) must be proper and finite
        """
    def multiplicity(self, P):
        """
        Return the multiplicity of ``P`` on this subscheme.

        This is computed as the multiplicity of the local ring of this subscheme corresponding to ``P``. This
        subscheme must be defined over a field. An error is raised if ``P`` is not a point on this subscheme.

        INPUT:

        - ``P`` -- a point on this subscheme

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: X = A.subscheme([z*y - x^7, w - 2*z])
            sage: Q1 = A([1,1/3,3,6])
            sage: X.multiplicity(Q1)                                                    # needs sage.libs.singular
            1
            sage: Q2 = A([0,0,0,0])
            sage: X.multiplicity(Q2)                                                    # needs sage.libs.singular
            2

        ::

            sage: A.<x,y,z,w,v> = AffineSpace(GF(23), 5)
            sage: C = A.curve([x^8 - y, y^7 - z, z^3 - 1, w^5 - v^3])                   # needs sage.libs.singular sage.schemes
            sage: Q = A([22,1,1,0,0])
            sage: C.multiplicity(Q)                                                     # needs sage.libs.singular sage.schemes
            3

        ::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(-1)
            sage: A.<x,y,z,w,t> = AffineSpace(K, 5)
            sage: X = A.subscheme([y^7 - x^2*z^5 + z^3*t^8 - x^2*y^4*z - t^8])
            sage: Q1 = A([1,1,0,1,-1])
            sage: X.multiplicity(Q1)                                                    # needs sage.libs.singular
            1
            sage: Q2 = A([0,0,0,-a,0])
            sage: X.multiplicity(Q2)                                                    # needs sage.libs.singular
            7

        Check that :issue:`27479` is fixed::

            sage: A1.<x> = AffineSpace(QQ, 1)
            sage: X = A1.subscheme([x^1789 + x])
            sage: Q = X([0])
            sage: X.multiplicity(Q)                                                     # needs sage.libs.singular
            1
        """

class AlgebraicScheme_subscheme_affine_field(AlgebraicScheme_subscheme_affine):
    """
    Algebraic subschemes of projective spaces defined over fields.
    """
    def tangent_space(self, p):
        """
        Return the tangent space at the point ``p``.

        The points of the tangent space are the tangent vectors at ``p``.

        INPUT:

        - ``p`` -- a rational point

        EXAMPLES::

            sage: A3.<x,y,z> = AffineSpace(3, QQ)
            sage: X = A3.subscheme(z - x*y)
            sage: X.tangent_space(A3.origin())                                          # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Rational Field
             defined by:
              z
            sage: X.tangent_space(X(1,1,1))                                             # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Rational Field
             defined by:
              -x - y + z

        Tangent space at a point may have higher dimension than the dimension
        of the point. ::

            sage: # needs sage.libs.singular
            sage: C = Curve([x + y + z, x^2 - y^2*z^2 + z^3])
            sage: C.singular_points()
            [(0, 0, 0)]
            sage: p = C(0,0,0)
            sage: C.tangent_space(p)
            Closed subscheme of Affine Space of dimension 3 over Rational Field
             defined by:
              x + y + z
            sage: _.dimension()
            2
            sage: q = C(1,0,-1)
            sage: C.tangent_space(q)
            Closed subscheme of Affine Space of dimension 3 over Rational Field
             defined by:
              x + y + z,
              2*x + 3*z
            sage: _.dimension()
            1
        """
