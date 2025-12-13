from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.schemes.projective.projective_subscheme import AlgebraicScheme_subscheme_projective as AlgebraicScheme_subscheme_projective

class AlgebraicScheme_subscheme_product_projective(AlgebraicScheme_subscheme_projective):
    """
    Construct an algebraic subscheme of a product of projective spaces.

    .. WARNING::

        You should not create objects of this class directly. The
        preferred method to construct such subschemes is to use
        :meth:`~sage.schemes.product_projective.subscheme`
        method of :class:`Product of Projective Spaces
        <sage.schemes.product_projective.space.ProductProjectiveSpaces_ring>`.

    INPUT:

    - ``A`` -- ambient :class:`Product of Projective Spaces
      <sage.schemes.product_projective.space.ProductProjectiveSpaces_ring>`

    - ``polynomials`` -- single polynomial, ideal or iterable of
      defining multi-homogeneous polynomials

    EXAMPLES::

        sage: P.<x, y, u, v> = ProductProjectiveSpaces([1, 1], QQ)
        sage: P.subscheme([u*x^2 - v*y*x])
        Closed subscheme of Product of projective spaces P^1 x P^1 over Rational Field
         defined by:
          x^2*u - x*y*v

    TESTS::

        sage: from sage.schemes.product_projective.subscheme \\\n        ....: import AlgebraicScheme_subscheme_product_projective
        sage: AlgebraicScheme_subscheme_product_projective(P, [u*x^2 - v*y*x])
        Closed subscheme of Product of projective spaces P^1 x P^1
         over Rational Field defined by:
          x^2*u - x*y*v
    """
    @cached_method
    def segre_embedding(self, PP=None):
        """
        Return the Segre embedding of this subscheme into the appropriate projective
        space.

        INPUT:

        - ``PP`` -- (default: ``None``) ambient image projective space;
          this is constructed if it is not given

        OUTPUT: hom from this subscheme to the appropriate subscheme of projective space

        EXAMPLES::

            sage: X.<x,y,z,w,u,v> = ProductProjectiveSpaces([2, 2], QQ)
            sage: P = ProjectiveSpace(QQ, 8, 't')
            sage: L = (-w - v)*x + (-w*y - u*z)
            sage: Q = ((-u*w - v^2)*x^2 + ((-w^2 - u*w + (-u*v - u^2))*y + (-w^2 - u*v)*z)*x
            ....:      + ((-w^2 - u*w - u^2)*y^2 + (-u*w - v^2)*z*y + (-w^2 + (-v - u)*w)*z^2))
            sage: W = X.subscheme([L,Q])
            sage: phi = W.segre_embedding(P)                                            # needs sage.libs.singular
            sage: phi.codomain().ambient_space() == P                                   # needs sage.libs.singular
            True

        ::

            sage: PP.<x,y,u,v,s,t> = ProductProjectiveSpaces([1, 1, 1], CC)             # needs sage.rings.real_mpfr
            sage: PP.subscheme([]).segre_embedding()                                    # needs sage.libs.singular sage.rings.real_mpfr
            Scheme morphism:
              From: Closed subscheme of Product of projective spaces P^1 x P^1 x P^1
                    over Complex Field with 53 bits of precision defined by:
                      (no polynomials)
              To:   Closed subscheme of Projective Space of dimension 7
                    over Complex Field with 53 bits of precision defined by:
                      -u5*u6 + u4*u7,       -u3*u6 + u2*u7,       -u3*u4 + u2*u5,
                      -u3*u5 + u1*u7,       -u3*u4 + u1*u6,       -u3*u4 + u0*u7,
                      -u2*u4 + u0*u6,       -u1*u4 + u0*u5,       -u1*u2 + u0*u3
              Defn: Defined by sending (x : y , u : v , s : t) to
                    (x*u*s : x*u*t : x*v*s : x*v*t : y*u*s : y*u*t : y*v*s : y*v*t).

        ::

            sage: PP.<x,y,z,u,v,s,t> = ProductProjectiveSpaces([2, 1, 1], ZZ)
            sage: PP.subscheme([x^3, u - v, s^2 - t^2]).segre_embedding()               # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Product of projective spaces P^2 x P^1 x P^1
                    over Integer Ring defined by:
                      x^3,                  u - v,                s^2 - t^2
              To:   Closed subscheme of Projective Space of dimension 11
                    over Integer Ring defined by:
                      u10^2 - u11^2,        u9 - u11,             u8 - u10,
                      -u7*u10 + u6*u11,     u6*u10 - u7*u11,      u6^2 - u7^2,
                      u5 - u7,              u4 - u6,              u3^3,
                      -u3*u10 + u2*u11,     u2*u10 - u3*u11,      -u3*u6 + u2*u7,
                      u2*u6 - u3*u7,        u2*u3^2,              u2^2 - u3^2,
                      u1 - u3,              u0 - u2
              Defn: Defined by sending (x : y : z , u : v , s : t) to
                    (x*u*s : x*u*t : x*v*s : x*v*t : y*u*s : y*u*t : y*v*s : y*v*t
                     : z*u*s : z*u*t : z*v*s : z*v*t).
        """
    def dimension(self):
        """
        Return the dimension of the algebraic subscheme.

        OUTPUT: integer

        EXAMPLES::

            sage: X.<x,y,z,w,u,v> = ProductProjectiveSpaces([2, 2], QQ)
            sage: L = (-w - v)*x + (-w*y - u*z)
            sage: Q = ((-u*w - v^2)*x^2 + ((-w^2 - u*w + (-u*v - u^2))*y + (-w^2 - u*v)*z)*x
            ....:      + ((-w^2 - u*w - u^2)*y^2 + (-u*w - v^2)*z*y + (-w^2 + (-v - u)*w)*z^2))
            sage: W = X.subscheme([L, Q])
            sage: W.dimension()                                                         # needs sage.libs.singular
            2

        ::

            sage: PP.<x,y,z,u,v,s,t> = ProductProjectiveSpaces([2, 1, 1], QQ)
            sage: X = PP.subscheme([x^3, x^5 + y^5, z^6, x*u - v*y, s^2 - t^2])
            sage: X.dimension()                                                         # needs sage.libs.singular
            -1

        ::

            sage: PP = ProductProjectiveSpaces([2, 1, 3], CC, 't')                      # needs sage.rings.real_mpfr
            sage: PP.subscheme([]).dimension()                                          # needs sage.libs.singular sage.rings.real_mpfr
            6

        ::

            sage: PP = ProductProjectiveSpaces([1, 3, 1], ZZ, 't')
            sage: PP.subscheme([]).dimension()                                          # needs sage.libs.singular
            5

        ::

            sage: PP.<x,y,u,v,s,t> = ProductProjectiveSpaces([1,1,1], CC)               # needs sage.rings.real_mpfr
            sage: X = PP.subscheme([x^2 - y^2, u - v, s^2 - t^2])                       # needs sage.libs.singular sage.rings.real_mpfr
            sage: X.dimension()                                                         # needs sage.libs.singular sage.rings.real_mpfr
            0
        """
    def is_smooth(self, point=None) -> None:
        """
        Test whether the algebraic subscheme is smooth.

        EXAMPLES::

            sage: X.<x,y,z,w,u,v> = ProductProjectiveSpaces([2, 2],QQ)
            sage: L = (-w - v)*x + (-w*y - u*z)
            sage: Q = ((-u*w - v^2)*x^2 + ((-w^2 - u*w + (-u*v - u^2))*y + (-w^2 - u*v)*z)*x
            ....:      + ((-w^2 - u*w - u^2)*y^2 + (-u*w - v^2)*z*y + (-w^2 + (-v - u)*w)*z^2))
            sage: W = X.subscheme([L, Q])
            sage: W.is_smooth()
            Traceback (most recent call last):
            ...
            NotImplementedError: Not Implemented
        """
    def affine_patch(self, I, return_embedding: bool = False):
        """
        Return the `I`-th affine patch of this projective scheme
        where `I` is a multi-index.

        INPUT:

        - ``I`` -- list or tuple of positive integers

        - ``return_embedding`` -- boolean; if ``True`` the projective embedding
          is also returned

        OUTPUT:

        - An affine algebraic scheme

        - An embedding into a product of projective space (optional)

        EXAMPLES::

            sage: PP.<x,y,z,w,u,v> = ProductProjectiveSpaces([3, 1],QQ)
            sage: W = PP.subscheme([y^2*z - x^3, z^2 - w^2, u^3 - v^3])
            sage: W.affine_patch([0, 1], True)
            (Closed subscheme of Affine Space of dimension 4 over Rational Field defined by:
              x0^2*x1 - 1,
              x1^2 - x2^2,
              x3^3 - 1,
             Scheme morphism:
              From: Closed subscheme of Affine Space of dimension 4
                    over Rational Field defined by: x0^2*x1 - 1, x1^2 - x2^2, x3^3 - 1
              To:   Closed subscheme of Product of projective spaces P^3 x P^1
                    over Rational Field defined by: -x^3 + y^2*z, z^2 - w^2, u^3 - v^3
              Defn: Defined on coordinates by sending (x0, x1, x2, x3) to
                    (1 : x0 : x1 : x2 , x3 : 1))
        """
    def intersection_multiplicity(self, X, P):
        """
        Return the intersection multiplicity of this subscheme and the
        subscheme ``X`` at the point ``P``.

        This uses the intersection_multiplicity function for affine subschemes
        on affine patches of this subscheme and ``X`` that contain ``P``.

        INPUT:

        - ``X`` -- subscheme in the same ambient space as this subscheme

        - ``P`` -- a point in the intersection of this subscheme with ``X``

        OUTPUT: integer

        EXAMPLES:

        Multiplicity of a fixed point of the map `z^2 + \\frac{1}{4}`::

            sage: PP.<x,y,u,v> = ProductProjectiveSpaces(QQ, [1, 1])
            sage: G = PP.subscheme([(x^2 + 1/4*y^2)*v - y^2*u])
            sage: D = PP.subscheme([x*v - y*u])
            sage: sorted(G.intersection(D).rational_points())                           # needs sage.libs.singular
            [(1/2 : 1 , 1/2 : 1), (1 : 0 , 1 : 0)]
            sage: Q = PP([1/2,1,1/2,1])
            sage: G.intersection_multiplicity(D, Q)                                     # needs sage.libs.singular
            2

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: PP.<x,y,z,u,v,w> = ProductProjectiveSpaces(F, [2, 2])
            sage: X = PP.subscheme([z^5 + 3*x*y^4 + 8*y^5, u^2 - v^2])
            sage: Y = PP.subscheme([x^6 + z^6, w*z - v*y])
            sage: Q = PP([a,a+1,1,a,a,1])
            sage: X.intersection_multiplicity(Y, Q)                                     # needs sage.libs.singular
            16

        ::

            sage: PP.<x,y,z,u,v,w> = ProductProjectiveSpaces(QQ, [2, 2])
            sage: X = PP.subscheme([x^2*u^3 + y*z*u*v^2, x - y])
            sage: Y = PP.subscheme([u^3 - w^3, x*v - y*w, z^3*w^2 - y^3*u*v])
            sage: Q = PP([0,0,1,0,1,0])
            sage: X.intersection_multiplicity(Y, Q)                                     # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: the intersection of this subscheme and (=Closed subscheme of Affine Space of dimension 4
            over Rational Field defined by: x2^3 - x3^3, -x1*x3 + x0, -x1^3*x2 + x3^2) must be proper and finite
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

            sage: PP.<x,y,z,w> = ProductProjectiveSpaces(QQ, [1, 1])
            sage: X = PP.subscheme([x^4*z^3 - y^4*w^3])
            sage: Q1 = PP([1,1,1,1])
            sage: X.multiplicity(Q1)                                                    # needs sage.libs.singular
            1
            sage: Q2 = PP([0,1,1,0])
            sage: X.multiplicity(Q2)                                                    # needs sage.libs.singular
            3

        ::

            sage: PP.<x,y,z,w,u> = ProductProjectiveSpaces(GF(11), [1,2])
            sage: X = PP.subscheme([x^7*u - y^7*z, u^6*x^2 - w^3*z^3*x*y - w^6*y^2])
            sage: Q1 = PP([1,0,10,1,0])
            sage: X.multiplicity(Q1)                                                    # needs sage.libs.singular sage.rings.finite_rings
            1
            sage: Q2 = PP([1,0,1,0,0])
            sage: X.multiplicity(Q2)                                                    # needs sage.libs.singular sage.rings.finite_rings
            4
        """
