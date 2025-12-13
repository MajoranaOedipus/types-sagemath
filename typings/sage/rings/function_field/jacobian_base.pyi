from sage.arith.misc import integer_ceil as integer_ceil, integer_floor as integer_floor
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor, pushout as pushout
from sage.categories.schemes import Jacobians as Jacobians
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.parent import Parent as Parent

class JacobianPoint_base(ModuleElement):
    """
    Abstract base class of points of Jacobian groups.
    """

class JacobianPoint_finite_field_base(JacobianPoint_base):
    """
    Points of Jacobians over finite fields.
    """
    def order(self):
        """
        Return the order of this point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: F = C.function_field()
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: b = F.get_place(1)
            sage: pl = C([-1,2,1]).place()
            sage: p = G.point(pl - b)
            sage: p.order()
            15

        ALGORITHM: Shanks' Baby Step Giant Step
        """
    def frobenius(self):
        """
        Return the image of the point acted by the Frobenius automorphism.

        EXAMPLES::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: J = C.jacobian(model='hess')
            sage: G1 = J.group()
            sage: G1.order()
            11
            sage: K = k.extension(3)
            sage: G3 = J.group(K)
            sage: pts1 = G1.get_points(11)
            sage: pts3 = G3.get_points(12)
            sage: pt = next(pt for pt in pts3 if pt not in pts1)
            sage: pt.frobenius() == pt
            False
            sage: pt.frobenius().frobenius().frobenius() == pt
            True
        """

class JacobianGroupFunctor(ConstructionFunctor):
    """
    A construction functor for Jacobian groups.

    EXAMPLES::

        sage: k = GF(7)
        sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: J = C.jacobian(model='hess')
        sage: G = J.group()
        sage: F, obj = G.construction()
        sage: F
        JacobianGroupFunctor
    """
    rank: int
    def __init__(self, base_field, field) -> None:
        """
        Initialize.

        TESTS::

            sage: k = GF(7)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='hess')
            sage: K = k.extension(2)
            sage: G = J.group(K)
            sage: F, obj = G.construction()
            sage: TestSuite(F).run()
        """
    def merge(self, other):
        """
        Return the functor merging ``self`` and ``other``.

        INPUT:

        - ``other`` -- a functor

        EXAMPLES::

            sage: k = GF(7)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='hess')
            sage: K2 = k.extension(2)
            sage: G2 = J.group(K2)
            sage: K3 = k.extension(3)
            sage: G3 = J.group(K3)
            sage: sage.categories.pushout.pushout(G2, G3)  # indirect doctest
            Group of rational points of Jacobian over Finite Field in z6 of size 7^6 (Hess model)
        """

class JacobianGroup_base(Parent):
    """
    Groups of rational points of Jacobians.

    INPUT:

    - ``parent`` -- a Jacobian

    - ``function_field`` -- a function field

    - ``base_div`` -- an effective divisor of the function field

    EXAMPLES::

        sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: J = C.jacobian(model='hess')
        sage: J.group()
        Group of rational points of Jacobian over Finite Field of size 7 (Hess model)
    """
    def __init__(self, parent, function_field, base_div) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='hess')
            sage: G = J.group()
            sage: TestSuite(G).run(skip=['_test_elements', '_test_pickling'])
        """
    def construction(self):
        """
        Return the data for a functorial construction of this Jacobian group.

        EXAMPLES::

            sage: k = GF(7)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='hess')
            sage: K2 = k.extension(2)
            sage: G2 = J.group(K2)
            sage: K3= k.extension(3)
            sage: G3 = J.group(K3)
            sage: p1, p2 = G2.get_points(2)
            sage: q1, q2 = G3.get_points(2)
            sage: (p1 + q1).parent() is (p2 + q2).parent()
            True
        """
    def parent(self):
        """
        Return the Jacobian to which this Jacobian group belongs.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='hess')
            sage: G = J.group()
            sage: G.parent()
            Jacobian of Projective Plane Curve over Finite Field of size 7
             defined by x^3 - y^2*z - 2*z^3 (Hess model)
        """
    def function_field(self):
        """
        Return the function field to which this Jacobian group attached.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='hess')
            sage: G = J.group()
            sage: G.function_field()
            Function field in z defined by z^3 + 4*y^2*z + 3
        """
    def base_divisor(self):
        """
        Return the base divisor that is used to represent points of this group.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G = J.group()
            sage: G.base_divisor()
            Place (1/y, 1/y*z)
            sage: _ == 1*b
            True

        The base divisor is the denominator (negative part) of the divisor of
        degree zero that represents a point. ::

            sage: p = C([-1,2,1]).place()
            sage: G.point(p - b).divisor()
            - Place (1/y, 1/y*z)
             + Place (y + 2, z + 1)
        """

class JacobianGroup_finite_field_base(JacobianGroup_base):
    """
    Jacobian groups of function fields over finite fields.

    EXAMPLES::

        sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: J = C.jacobian(model='hess', base_div=b)
        sage: J.group()
        Group of rational points of Jacobian over Finite Field of size 7 (Hess model)
    """
    def order(self, algorithm: str = 'numeric'):
        """
        Return the order of the Jacobian group.

        INPUT:

        - ``algorithm`` -- ``'numeric'`` (default) or ``'algebraic'``

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G = J.group()
            sage: G.order()
            7
        """
    def get_points(self, n):
        """
        Return `n` points of the Jacobian group.

        If `n` is greater than the order of the group, then returns
        all points of the group.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: J = C.jacobian(model='hess')
            sage: G = J.group()
            sage: pts = G.get_points(G.order())
            sage: len(pts)
            11
        """

class Jacobian_base(Parent):
    """
    Jacobians of function fields.

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
        sage: F.jacobian()
        Jacobian of Function field in y defined by y^2 + y + (x^2 + 1)/x (Hess model)
    """
    def __init__(self, function_field, base_div, **kwds) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: J = F.jacobian()
            sage: TestSuite(J).run()
        """
    def __call__(self, x):
        """
        Return the point of ``self`` constructed from ``x``.

        It is assumed that ``self`` and ``x`` are points of the Jacobians
        attached to the same function field.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: J_hess = F.jacobian(model='hess')
            sage: G = J_hess.group()
            sage: p = G.get_points(3)[2]
            sage: Jkm = F.jacobian(model='km_large')
            sage: q = Jkm(p)
            sage: p.order() == q.order()
            True
            sage: J_hess(q) == p
            True

        If ``x`` is an effective divisor, it is checked that the degree
        is equal to the degree of the base divisor. See :issue:`38623`.

            sage: K.<x> = FunctionField(GF(7))
            sage: _.<t> = K[]
            sage: F.<y> = K.extension(t^2 - x^6 - 3)
            sage: O = F.maximal_order()
            sage: D1 = (O.ideal(x + 1, y + 2) * O.ideal(x + 2, y + 2)).divisor()
            sage: I = O.ideal(x + 3, y+5) * O.ideal(x + 4, y + 5) * O.ideal(x + 5, y + 5)
            sage: D2 = I.divisor()
            sage: J = F.jacobian(model='hess')
            sage: J(D1)
            [Place (x + 1, y + 2) + Place (x + 2, y + 2)]
            sage: J(D2)
            Traceback (most recent call last):
            ...
            ValueError: effective divisor is not of degree 2
            sage: J.base_divisor().degree()
            2
        """
    def curve(self):
        """
        Return the projective curve to which this Jacobian is attached.

        If the Jacobian was constructed from a function field, then returns nothing.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: J = F.jacobian()
            sage: J.curve()
        """
    def base_curve(self):
        """
        Return the base curve or the function field that abstractly defines a curve.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: J = F.jacobian()
            sage: J.base_curve()
            Function field in y defined by y^2 + y + (x^2 + 1)/x
        """
    def facade_for(self):
        """
        Return the system of groups that this Jacobian is a facade for.

        The Jacobian can be seen as a facade for all groups of rational points
        over field extensions of the base constant field of the function field.
        This method returns only the internally constructed system of such
        groups.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: J = F.jacobian()
            sage: J.facade_for()
            [Group of rational points of Jacobian over Finite Field of size 2 (Hess model)]
        """
    def base_divisor(self):
        """
        Return the base divisor used to construct the Jacobian.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: b = F.get_place(1)
            sage: J = F.jacobian(base_div=b)
            sage: J.base_divisor() == b
            True
        """
    def group(self, k_ext=None):
        """
        Return the group of rational points of the Jacobian.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: b = F.get_place(1)
            sage: J = F.jacobian(base_div=b)
            sage: J.group()
            Group of rational points of Jacobian over Finite Field of size 2 (Hess model)
        """
    def set_base_place(self, place) -> None:
        """
        Set ``place`` as the base place.

        INPUT:

        - ``place`` -- a rational place of the function field

        The base place `B` is used to map a rational place `P` of the function
        field to the point of the Jacobian defined by the divisor `P - B`.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: J = F.jacobian()
            sage: B = F.get_place(1)
            sage: J.set_base_place(B)
            sage: Q = F.places()[-1]
            sage: J(Q)
            [Place (x + 1, x*y + 1)]
            sage: J(Q).parent()
            Group of rational points of Jacobian over Finite Field of size 2 (Hess model)
            sage: J(B)
            [Place (x, x*y)]
            sage: J(B).is_zero()
            True
        """
