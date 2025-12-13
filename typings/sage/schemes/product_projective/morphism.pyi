from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.generic.morphism import SchemeMorphism_polynomial as SchemeMorphism_polynomial

class ProductProjectiveSpaces_morphism_ring(SchemeMorphism_polynomial):
    """
    The class of morphisms on products of projective spaces.

    The components are projective space morphisms.

    EXAMPLES::

        sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
        sage: H = T.Hom(T)
        sage: H([x^2, y^2, z^2, w^2, u^2])
        Scheme endomorphism of Product of projective spaces P^2 x P^1 over Rational Field
          Defn: Defined by sending (x : y : z , w : u) to (x^2 : y^2 : z^2 , w^2 : u^2).
    """
    def __init__(self, parent, polys, check: bool = True) -> None:
        """
        The Python constructor.

        INPUT:

        - ``parent`` -- Hom-set

        - ``polys`` -- anything that defines a point in the class

        - ``check`` -- boolean; whether or not to perform input checks
          (default: ``True``)

        EXAMPLES::

            sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: H = T.Hom(T)
            sage: H([x^2*u, y^2*w, z^2*u, w^2, u^2])
            Scheme endomorphism of Product of projective spaces P^2 x P^1 over Rational Field
              Defn: Defined by sending (x : y : z , w : u) to
                    (x^2*u : y^2*w : z^2*u , w^2 : u^2).

        ::

            sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: H = T.Hom(T)
            sage: H([x^2*u, y^2*w, z^2*u, w^2, u*z])
            Traceback (most recent call last):
            ...
            TypeError: polys (=[x^2*u, y^2*w, z^2*u, w^2, z*u]) must be
            multi-homogeneous of the same degrees (by component)

        ::

            sage: R.<s,t> = PolynomialRing(QQ)
            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], QQ)
            sage: P.<u,v,w,s,t,r> = ProductProjectiveSpaces([3, 1], QQ)
            sage: H = Hom(Z,P)
            sage: f = H([a^2, b^2, a^2, a*b, a*x, b*z]); f
            Scheme morphism:
              From: Product of projective spaces P^1 x P^2 over Rational Field
              To:   Product of projective spaces P^3 x P^1 over Rational Field
              Defn: Defined by sending (a : b , x : y : z) to
                    (a^2 : b^2 : a^2 : a*b , a*x : b*z).

        ::

            sage: Z.<a,b,c,x,y,z> = ProductProjectiveSpaces([1, 3], QQ)
            sage: P.<u,v,w,s,t,r> = ProductProjectiveSpaces([2, 2], QQ)
            sage: H = Hom(Z,P)
            sage: f = H([a^2, b^2, c^2, x^2, y^2, z^2])
            Traceback (most recent call last):
            ...
            TypeError: polys (=[a^2, b^2, c^2, x^2, y^2, z^2]) must be
            multi-homogeneous of the same degrees (by component)
        """
    def __getitem__(self, i):
        """
        Return the ``i``-th coordinate polynomial.

        INPUT:

        - ``i`` -- integer

        OUTPUT:

        The (multi)-homogeneous polynomial that is the ``i``-th coordinate.

        EXAMPLES::

            sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: H = T.Hom(T)
            sage: F = H([x^2*u, y^2*w, z^2*u, w^2, u^2])
            sage: F[2]
            z^2*u
        """
    def __call__(self, P, check: bool = True):
        """
        Make morphisms of products of projective spaces callable.

        INPUT:

        - ``P`` -- a point in the domain

        - ``check`` -- boolean (default: ``True``); whether or not to perform
          the input checks on the image point

        OUTPUT: the image point in the codomain

        EXAMPLES::

            sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: H = T.Hom(T)
            sage: F = H([x^2*u, y^2*w, z^2*u, w^2, u^2])
            sage: F(T([2, 1, 3, 0, 1]))
            (4/9 : 0 : 1 , 0 : 1)

        ::

            sage: PP.<x,y,z,u,v,w> = ProductProjectiveSpaces(QQ, [1, 1, 1])
            sage: HP = End(PP)
            sage: f = HP([v*x^2,w*y^2,z^2,u^2,v^2,w^2])
            sage: Q = PP([0,1,1,1,1,1])
            sage: f(Q)
            (0 : 1 , 1 : 1 , 1 : 1)

        ::

            sage: PP.<t0,t1,t2,t3,t4> = ProductProjectiveSpaces([2, 1], ZZ)
            sage: Q = PP([1,1,1,2,1])
            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], ZZ)
            sage: H = End(Z)
            sage: f = H([a^3, b^3 + a*b^2, x^2, y^2 - z^2, z*y])
            sage: f(Q)
            Traceback (most recent call last):
            ...
            TypeError: (1 : 1 : 1 , 2 : 1) fails to convert into the map's domain
            Product of projective spaces P^1 x P^2 over Integer Ring, but a
            `pushforward` method is not properly implemented
            sage: f([1,1,1,2,1])
            (1 : 2 , 1 : 3 : 2)

        ::

            sage: PP.<x,y,u,v> = ProductProjectiveSpaces(ZZ, [1, 1])
            sage: HP = End(PP)
            sage: g = HP([x^2, y^2, u^2, v^2])
            sage: g([0, 0, 0, 0], check=False)
            (0 : 0 , 0 : 0)
        """
    def __eq__(self, right):
        """
        Test the equality of two product projective morphisms.

        INPUT:

        - ``right`` -- a map on product of projective space

        OUTPUT:

        boolean; ``True`` if ``self`` and ``right`` define the same product
        projective map. ``False`` otherwise.

        EXAMPLES::

            sage: P1.<x1,x2,x3,x4> = ProductProjectiveSpaces([1, 1], QQ)
            sage: P2.<y1,y2,y3,y4> = ProductProjectiveSpaces([1, 1], CC)                # needs sage.rings.real_mpfr
            sage: H1 = End(P1)
            sage: H2 = End(P2)                                                          # needs sage.rings.real_mpfr
            sage: f = H1([x1*x2, x2^2, x3*x4, x4^2])
            sage: g = H2([y1*y2, y2^2, y3*y4, y4^2])                                    # needs sage.rings.real_mpfr
            sage: f == g                                                                # needs sage.rings.real_mpfr
            False

        ::

            sage: P.<x,y,u,v> = ProductProjectiveSpaces([1, 1], QQ)
            sage: H = Hom(P, P)
            sage: f = H([x^2, y^2, u^2, v^2])
            sage: g = H([x^2, x*y, u*v, u^2])
            sage: f == g
            False

        ::

            sage: PP.<x,y,z,a,b> = ProductProjectiveSpaces([2,1], ZZ)
            sage: H = End(PP)
            sage: f = H([x^2*y*z, x*y^2*z, x*y*z^2, a^2, b^2])
            sage: g = H([x, y, z, a^3, a*b^2])
            sage: f == g
            True
        """
    def __ne__(self, right):
        """
        Test the inequality of two prduct projective morphisms.

        INPUT:

        - ``right`` -- a map on product of projective space

        OUTPUT:

        boolean; ``True`` if ``self`` and ``right`` define different product
        projective maps. ``False`` otherwise.

        EXAMPLES::

            sage: PP.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], ZZ)
            sage: E = End(PP)
            sage: f = E([a^3, a*b^2, x*y, y*z, z*x])
            sage: g = E([a*b, a^2, x^2, y^2, z^2])
            sage: f != g
            True
            sage: f != f
            False
        """
    def is_morphism(self):
        """
        Return ``True`` if this mapping is a morphism of products of projective spaces.

        For each component space of the codomain of this mapping we consider the subscheme of
        the domain of this map generated by the corresponding coordinates of the map.
        This map is a morphism if and only if each of these subschemes has no points.

        OUTPUT: boolean

        EXAMPLES::

            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], ZZ)
            sage: H = End(Z)
            sage: f = H([a^2, b^2, x*z - y*z, x^2 - y^2, z^2])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            False

        ::

            sage: P.<x,y,z,u,v,w> = ProductProjectiveSpaces([2, 2], QQ)
            sage: H = End(P)
            sage: f = H([u, v, w, u^2, v^2, w^2])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            True

        ::

            sage: P.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: Q.<a,b,c,d,e> = ProductProjectiveSpaces([1, 2], QQ)
            sage: H = Hom(P, Q)
            sage: f = H([x^2, y^2, u^3, w^3, u^3])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            False
        """
    def as_dynamical_system(self):
        """
        Return this endomorphism as a :class:`~sage.dynamics.arithmetic_dynamics.product_projective_ds.DynamicalSystem_product_projective`.

        OUTPUT: :class:`~sage.dynamics.arithmetic_dynamics.product_projective_ds.DynamicalSystem_product_projective`

        EXAMPLES::

            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], ZZ)
            sage: H = End(Z)
            sage: f = H([a^3, b^3, x^2, y^2, z^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.product_projective_ds.DynamicalSystem_product_projective'>
        """
    def global_height(self, prec=None):
        """
        Return the maximum of the absolute logarithmic heights of the coefficients
        in any of the coordinate functions of this map.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        .. TODO::

            Add functionality for `\\QQbar`, implement function to convert
            the map defined over `\\QQbar` to map over a number field.

        EXAMPLES::

            sage: P1xP1.<x,y,u,v> = ProductProjectiveSpaces([1, 1], ZZ)
            sage: H = End(P1xP1)
            sage: f = H([x^2*u, 3*y^2*v, 5*x*v^2, y*u^2])
            sage: f.global_height()                                                     # needs sage.rings.real_mpfr
            1.60943791243410

        ::

            sage: # needs sage.rings.number_field
            sage: u = QQ['u'].0
            sage: R = NumberField(u^2 - 2, 'v')
            sage: PP.<x,y,a,b> = ProductProjectiveSpaces([1, 1], R)
            sage: H = End(PP)
            sage: O = R.maximal_order()
            sage: g = H([3*O(u)*x^2, 13*x*y, 7*a*y, 5*b*x + O(u)*a*y])
            sage: g.global_height()                                                     # needs sage.rings.real_mpfr
            2.56494935746154
        """
    def local_height(self, v, prec=None):
        """
        Return the maximum of the local height of the coefficients in any
        of the coordinate functions of this map.

        INPUT:

        - ``v`` -- a prime or prime ideal of the base ring

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: H = T.Hom(T)
            sage: f = H([4*x^2 + 3/100*y^2, 8/210*x*y, 1/10000*z^2, 20*w^2, 1/384*u*w])
            sage: f.local_height(2)                                                     # needs sage.rings.real_mpfr
            4.85203026391962

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(z^2 - 5)
            sage: P.<x,y,a,b> = ProductProjectiveSpaces([1, 1], K)
            sage: H = Hom(P, P)
            sage: f = H([2*x^2 + w/3*y^2, 1/w*y^2, a^2, 6*b^2 + 1/9*a*b])
            sage: f.local_height(K.ideal(3))                                            # needs sage.rings.real_mpfr
            2.19722457733622
        """
