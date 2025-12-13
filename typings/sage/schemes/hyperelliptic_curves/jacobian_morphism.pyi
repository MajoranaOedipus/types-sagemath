from sage.misc.latex import latex as latex
from sage.schemes.generic.morphism import SchemeMorphism as SchemeMorphism
from sage.structure.element import AdditiveGroupElement as AdditiveGroupElement
from sage.structure.richcmp import op_NE as op_NE, richcmp as richcmp

def cantor_reduction_simple(a, b, f, genus):
    """
    Return the unique reduced divisor linearly equivalent to
    `(a, b)` on the curve `y^2 = f(x).`

    See the docstring of
    :mod:`sage.schemes.hyperelliptic_curves.jacobian_morphism` for
    information about divisors, linear equivalence, and reduction.

    EXAMPLES::

        sage: x = QQ['x'].gen()
        sage: f = x^5 - x
        sage: H = HyperellipticCurve(f); H
        Hyperelliptic Curve over Rational Field defined by y^2 = x^5 - x
        sage: J = H.jacobian()(QQ); J
        Set of rational points of Jacobian of Hyperelliptic Curve over Rational Field
         defined by y^2 = x^5 - x

    The following point is 2-torsion::

        sage: P = J(H.lift_x(-1)); P
        (x + 1, y)
        sage: 2 * P # indirect doctest
        (1)
    """
def cantor_reduction(a, b, f, h, genus):
    """
    Return the unique reduced divisor linearly equivalent to
    `(a, b)` on the curve `y^2 + y h(x) = f(x)`.

    See the docstring of
    :mod:`sage.schemes.hyperelliptic_curves.jacobian_morphism` for
    information about divisors, linear equivalence, and reduction.

    EXAMPLES::

        sage: x = QQ['x'].gen()
        sage: f = x^5 - x
        sage: H = HyperellipticCurve(f, x); H
        Hyperelliptic Curve over Rational Field defined by y^2 + x*y = x^5 - x
        sage: J = H.jacobian()(QQ); J
        Set of rational points of Jacobian of Hyperelliptic Curve over
         Rational Field defined by y^2 + x*y = x^5 - x

    The following point is 2-torsion::

        sage: Q = J(H.lift_x(0)); Q
        (x, y)
        sage: 2*Q # indirect doctest
        (1)

    The next point is not 2-torsion::

        sage: P = J(H.lift_x(-1)); P
        (x + 1, y)
        sage: 2 * J(H.lift_x(-1)) # indirect doctest
        (x^2 + 2*x + 1, y + 4*x + 4)
        sage: 3 * J(H.lift_x(-1)) # indirect doctest
        (x^2 - 487*x - 324, y + 10755*x + 7146)
    """
def cantor_composition_simple(D1, D2, f, genus):
    """
    Given `D_1` and `D_2` two reduced Mumford
    divisors on the Jacobian of the curve `y^2 = f(x)`,
    computes a representative `D_1 + D_2`.

    .. warning::

       The representative computed is NOT reduced! Use
       :func:`cantor_reduction_simple` to reduce it.

    EXAMPLES::

        sage: x = QQ['x'].gen()
        sage: f = x^5 + x
        sage: H = HyperellipticCurve(f); H
        Hyperelliptic Curve over Rational Field defined by y^2 = x^5 + x

    ::

        sage: F.<a> = NumberField(x^2 - 2, 'a')                                         # needs sage.rings.number_field
        sage: J = H.jacobian()(F); J                                                    # needs sage.rings.number_field
        Set of rational points of Jacobian of Hyperelliptic Curve over
         Number Field in a with defining polynomial x^2 - 2 defined by y^2 = x^5 + x

    ::

        sage: # needs sage.rings.number_field
        sage: P = J(H.lift_x(F(1))); P
        (x - 1, y + a)
        sage: Q = J(H.lift_x(F(0))); Q
        (x, y)
        sage: 2*P + 2*Q # indirect doctest
        (x^2 - 2*x + 1, y + 3/2*a*x - 1/2*a)
        sage: 2*(P + Q) # indirect doctest
        (x^2 - 2*x + 1, y + 3/2*a*x - 1/2*a)
        sage: 3*P # indirect doctest
        (x^2 - 25/32*x + 49/32, y + 45/256*a*x + 315/256*a)
    """
def cantor_composition(D1, D2, f, h, genus):
    """
    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: F.<a> = GF(7^2, 'a')
        sage: x = F['x'].gen()
        sage: f = x^7 + x^2 + a
        sage: H = HyperellipticCurve(f, 2*x); H
        Hyperelliptic Curve over Finite Field in a of size 7^2
         defined by y^2 + 2*x*y = x^7 + x^2 + a
        sage: J = H.jacobian()(F); J
        Set of rational points of Jacobian of Hyperelliptic Curve over
         Finite Field in a of size 7^2 defined by y^2 + 2*x*y = x^7 + x^2 + a

    ::

        sage: Q = J(H.lift_x(F(1))); Q                                                  # needs sage.rings.finite_rings
        (x + 6, y + 5*a)
        sage: 10*Q  # indirect doctest                                                  # needs sage.rings.finite_rings
        (x^3 + (3*a + 1)*x^2 + (2*a + 5)*x + a + 5, y + (3*a + 2)*x^2 + (6*a + 1)*x + a + 4)
        sage: 7*8297*Q                                                                  # needs sage.rings.finite_rings
        (1)

    ::

        sage: Q = J(H.lift_x(F(a+1))); Q                                                # needs sage.rings.finite_rings
        (x + 6*a + 6, y + 2)
        sage: 7*8297*Q  # indirect doctest                                              # needs sage.rings.finite_rings
        (1)

        A test over a prime field:

        sage: # needs sage.rings.finite_rings
        sage: F = GF(next_prime(10^30))
        sage: x = F['x'].gen()
        sage: f = x^7 + x^2 + 1
        sage: H = HyperellipticCurve(f, 2*x); H
        Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057
         defined by y^2 + 2*x*y = x^7 + x^2 + 1
        sage: J = H.jacobian()(F); J
        Set of rational points of Jacobian of Hyperelliptic Curve
         over Finite Field of size 1000000000000000000000000000057
         defined by y^2 + 2*x*y = x^7 + x^2 + 1
        sage: Q = J(H.lift_x(F(1))); Q
        (x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)
        sage: 10*Q  # indirect doctest
        (x^3 + 150296037169838934997145567227*x^2
             + 377701248971234560956743242408*x + 509456150352486043408603286615,
         y + 514451014495791237681619598519*x^2
           + 875375621665039398768235387900*x + 861429240012590886251910326876)
        sage: 7*8297*Q
        (x^3 + 35410976139548567549919839063*x^2
             + 26230404235226464545886889960*x + 681571430588959705539385624700,
         y + 999722365017286747841221441793*x^2
           + 262703715994522725686603955650*x + 626219823403254233972118260890)
    """

class JacobianMorphism_divisor_class_field(AdditiveGroupElement, SchemeMorphism):
    """
    An element of a Jacobian defined over a field, i.e. in
    `J(K) = \\mathrm{Pic}^0_K(C)`.
    """
    def __init__(self, parent, polys, check: bool = True) -> None:
        """
        Create a new Jacobian element in Mumford representation.

        INPUT:

        - ``parent`` -- the parent Homset
        - ``polys`` -- Mumford's `u` and `v` polynomials
        - ``check`` -- boolean (default: ``True``); if ``True``, ensure that
          polynomials define a divisor on the appropriate curve and are reduced

        .. warning::

           Not for external use! Use ``J(K)([u, v])`` instead.

        EXAMPLES::

            sage: x = GF(37)['x'].gen()
            sage: H = HyperellipticCurve(x^5 + 12*x^4 + 13*x^3 + 15*x^2 + 33*x)
            sage: J = H.jacobian()(GF(37));  J
            Set of rational points of Jacobian of Hyperelliptic Curve over
             Finite Field of size 37 defined by
            y^2 = x^5 + 12*x^4 + 13*x^3 + 15*x^2 + 33*x

        ::

            sage: P1 = J(H.lift_x(2)); P1  # indirect doctest
            (x + 35, y + 26)
            sage: P1.parent()
            Set of rational points of Jacobian of Hyperelliptic Curve over
             Finite Field of size 37 defined by
            y^2 = x^5 + 12*x^4 + 13*x^3 + 15*x^2 + 33*x
            sage: type(P1)
            <class 'sage.schemes.hyperelliptic_curves.jacobian_morphism.JacobianMorphism_divisor_class_field'>
        """
    def scheme(self):
        """
        Return the scheme this morphism maps to; or, where this divisor lives.

        .. WARNING::

            Although a pointset is defined over a specific field, the
            scheme returned may be over a different (usually smaller)
            field.  The example below demonstrates this: the pointset
            is determined over a number field of absolute degree 2 but
            the scheme returned is defined over the rationals.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = QQ['x'].gen()
            sage: f = x^5 + x
            sage: H = HyperellipticCurve(f)
            sage: F.<a> = NumberField(x^2 - 2, 'a')
            sage: J = H.jacobian()(F); J
            Set of rational points of Jacobian of Hyperelliptic Curve
             over Number Field in a with defining polynomial x^2 - 2
             defined by y^2 = x^5 + x
            sage: P = J(H.lift_x(F(1)))
            sage: P.scheme()
            Jacobian of Hyperelliptic Curve over Rational Field defined by y^2 = x^5 + x
        """
    def point_of_jacobian_of_curve(self):
        """
        Return the point in the Jacobian of the curve.

        The Jacobian is the one attached to the projective curve
        corresponding to this hyperelliptic curve.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(11))
            sage: f = x^6 + x + 1
            sage: H = HyperellipticCurve(f)
            sage: J = H.jacobian()
            sage: D = J(H.lift_x(1))
            sage: D  # divisor in Mumford representation
            (x + 10, y + 6)
            sage: jacobian_order = sum(H.frobenius_polynomial())
            sage: jacobian_order
            234
            sage: p = D.point_of_jacobian_of_curve(); p
            [Place (1/x0, 1/x0^3*x1 + 1)
             + Place (x0 + 10, x1 + 6)]
            sage: p  # Jacobian point represented by an effective divisor
            [Place (1/x0, 1/x0^3*x1 + 1)
             + Place (x0 + 10, x1 + 6)]
            sage: p.order()
            39
            sage: 234*p == 0
            True
            sage: G = p.parent()
            sage: G
            Group of rational points of Jacobian over Finite Field of size 11 (Hess model)
            sage: J = G.parent()
            sage: J
            Jacobian of Projective Plane Curve over Finite Field of size 11
             defined by x0^6 + x0^5*x1 + x1^6 - x0^4*x2^2 (Hess model)
            sage: C = J.curve()
            sage: C
            Projective Plane Curve over Finite Field of size 11
             defined by x0^6 + x0^5*x1 + x1^6 - x0^4*x2^2
            sage: C.affine_patch(0) == H.affine_patch(2)
            True
        """
    def __list__(self):
        """
        Return a list `(a(x), b(x))` of the polynomials giving the
        Mumford representation of ``self``.

        TESTS::

            sage: x = QQ['x'].gen()
            sage: f = x^5 + x
            sage: H = HyperellipticCurve(f)
            sage: F.<a> = NumberField(x^2 - 2, 'a')                                     # needs sage.rings.number_field
            sage: J = H.jacobian()(F); J                                                # needs sage.rings.number_field
            Set of rational points of Jacobian of Hyperelliptic Curve
             over Number Field in a with defining polynomial x^2 - 2
             defined by y^2 = x^5 + x

        ::

            sage: P = J(H.lift_x(F(1)))                                                 # needs sage.rings.number_field
            sage: list(P)  # indirect doctest                                           # needs sage.rings.number_field
            [x - 1, -a]
        """
    def __tuple__(self):
        """
        Return a tuple `(a(x), b(x))` of the polynomials giving the
        Mumford representation of ``self``.

        TESTS::

            sage: x = QQ['x'].gen()
            sage: f = x^5 + x
            sage: H = HyperellipticCurve(f)
            sage: F.<a> = NumberField(x^2 - 2, 'a')                                     # needs sage.rings.number_field
            sage: J = H.jacobian()(F); J                                                # needs sage.rings.number_field
            Set of rational points of Jacobian of Hyperelliptic Curve
             over Number Field in a with defining polynomial x^2 - 2
             defined by y^2 = x^5 + x

        ::

            sage: P = J(H.lift_x(F(1)))                                                 # needs sage.rings.number_field
            sage: tuple(P)  # indirect doctest                                          # needs sage.rings.number_field
            (x - 1, -a)
        """
    def __getitem__(self, n):
        """
        Return the `n`-th item of the pair `(a(x), b(x))`
        of polynomials giving the Mumford representation of ``self``.

        TESTS::

            sage: x = QQ['x'].gen()
            sage: f = x^5 + x
            sage: H = HyperellipticCurve(f)
            sage: F.<a> = NumberField(x^2 - 2, 'a')                                     # needs sage.rings.number_field
            sage: J = H.jacobian()(F); J                                                # needs sage.rings.number_field
            Set of rational points of Jacobian of Hyperelliptic Curve
             over Number Field in a with defining polynomial x^2 - 2
             defined by y^2 = x^5 + x

        ::

            sage: # needs sage.rings.number_field
            sage: P = J(H.lift_x(F(1)))
            sage: P[0] # indirect doctest
            x - 1
            sage: P[1] # indirect doctest
            -a
            sage: P[-1] # indirect doctest
            -a
            sage: P[:1] # indirect doctest
            [x - 1]
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if this divisor is not the additive identity element.

        EXAMPLES::

            sage: x = GF(37)['x'].gen()
            sage: H = HyperellipticCurve(x^5 + 12*x^4 + 13*x^3 + 15*x^2 + 33*x)
            sage: J = H.jacobian()(GF(37))

        ::

            sage: P1 = J(H.lift_x(2)); P1
            (x + 35, y + 26)
            sage: P1 == 0  # indirect doctest
            False
            sage: P1 - P1 == 0  # indirect doctest
            True
        """
    def __neg__(self):
        """
        Return the additive inverse of this divisor.

        EXAMPLES::

            sage: x = GF(37)['x'].gen()
            sage: H = HyperellipticCurve(x^5 + 12*x^4 + 13*x^3 + 15*x^2 + 33*x)
            sage: J = H.jacobian()(GF(37))
            sage: P1 = J(H.lift_x(2)); P1
            (x + 35, y + 26)
            sage: - P1  # indirect doctest
            (x + 35, y + 11)
            sage: P1 + (-P1)  # indirect doctest
            (1)

        ::

            sage: H2 = HyperellipticCurve(x^5 + 12*x^4 + 13*x^3 + 15*x^2 + 33*x, x)
            sage: J2 = H2.jacobian()(GF(37))
            sage: P2 = J2(H2.lift_x(2)); P2
            (x + 35, y + 24)
            sage: - P2  # indirect doctest
            (x + 35, y + 15)
            sage: P2 + (-P2)  # indirect doctest
            (1)

        TESTS:

        The following was fixed in :issue:`14264`::

            sage: # needs sage.rings.number_field
            sage: P.<x> = QQ[]
            sage: f = x^5 - x + 1; h = x
            sage: C = HyperellipticCurve(f, h, 'u,v')
            sage: J = C.jacobian()
            sage: K.<t> = NumberField(x^2 - 2)
            sage: R.<x> = K[]
            sage: Q = J(K)([x^2 - t, R(1)])
            sage: Q
            (u^2 - t, v - 1)
            sage: -Q
            (u^2 - t, v + u + 1)
            sage: Q + (-Q)  # indirect doctest
            (1)
        """
