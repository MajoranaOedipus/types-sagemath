from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RR as RR, RealNumber as RealNumber
from sage.schemes.projective.projective_point import SchemeMorphism_point_projective_field as SchemeMorphism_point_projective_field
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.structure.element import Element as Element, Expression as Expression

class Berkovich_Element(Element):
    """
    The parent class for any element of a Berkovich space.
    """

class Berkovich_Element_Cp(Berkovich_Element):
    """
    The abstract parent class for any element of Berkovich space over `\\CC_p`.

    This class should never be instantiated, instead use :class:`Berkovich_Element_Cp_Affine`
    or :class:`Berkovich_Element_Cp_Projective`.

    EXAMPLES::

        sage: B = Berkovich_Cp_Affine(3)
        sage: B(2)
        Type I point centered at 2 + O(3^20)

    ::

        sage: B(0, 1)
        Type II point centered at 0 of radius 3^0
    """
    def __init__(self, parent, center, radius=None, power=None, prec: int = 20, space_type=None, error_check: bool = True) -> None:
        """
        Initialization function.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(5)
            sage: B(4)
            Type I point centered at 4 + O(5^20)
        """
    def center_function(self):
        """
        Return the function defining the centers of disks in the approximation.

        Not defined unless this point is a type IV point created by using
        a univariate function to compute centers.

        OUTPUT: a univariate function

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(5)
            sage: L.<t> = PolynomialRing(Qp(5))
            sage: T = FractionField(L)
            sage: f = T(1/t)
            sage: R.<x> = RR[]
            sage: Y = FractionField(R)
            sage: g = (40*pi)/x                                                         # needs sage.symbolic
            sage: Q1 = B(f, g)                                                          # needs sage.symbolic
            sage: Q1.center_function()                                                  # needs sage.symbolic
            (1 + O(5^20))/((1 + O(5^20))*t)
        """
    def radius_function(self):
        """
        Return the function defining the radii of disks in the approximation.

        Not defined unless this point is a type IV point created by using
        a univariate function to compute radii.

        OUTPUT: a univariate function

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(5)
            sage: L.<t> = PolynomialRing(Qp(5))
            sage: T = FractionField(L)
            sage: f = T(1/t)
            sage: R.<x> = RR[]
            sage: Y = FractionField(R)
            sage: g = (40*pi)/x                                                         # needs sage.symbolic
            sage: Q1 = B(f, g)                                                          # needs sage.symbolic
            sage: Q1.radius_function()                                                  # needs sage.symbolic
            40.0000000000000*pi/x
        """
    def precision(self):
        """
        Return the precision of a type IV point.

        This integer is the number of disks used in the approximation of the type IV point.
        Not defined for type I, II, or III points.

        OUTPUT: integer

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(Qp(3))
            sage: d = B([2, 2, 2], [1.761, 1.123, 1.112])
            sage: d.precision()
            3

        TESTS::

            sage: d.precision == d.prec
            True
        """
    prec = precision
    def ideal(self):
        """
        The ideal which defines an embedding of the ``base_ring`` into `\\CC_p`.

        If this Berkovich space is backed by a `p`-adic field, then an embedding is
        already specified, and this returns ``None``.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(QQ, 3)
            sage: B(0).ideal()
            3

            ::

            sage: B = Berkovich_Cp_Projective(3)
            sage: B(0).ideal()
        """
    def power(self):
        """
        The power of ``p`` such that `p^\\text{power} = \\text{radius}`.

        For type II points, always in `\\QQ`. For type III points,
        a real number. Not defined for type I or IV points.

        OUTPUT:

        - A rational for type II points.
        - A real number for type III points.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1, 9)
            sage: Q1.power()
            2

        ::

            sage: Q2 = B(1, 4)
            sage: Q2.power()
            1.26185950714291
        """
    def radius(self):
        """
        Radius of the corresponding disk (or sequence of disks) in `\\CC_p`.

        OUTPUT:

        - A nonnegative real number for type I, II, or III points.
        - A list of nonnegative real numbers for type IV points.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1, 2/5)
            sage: Q1.radius()
            0.400000000000000

        ::

            sage: d = B([2, 2, 2], [1.761, 1.123, 1.112])
            sage: d.radius()
            [1.76100000000000, 1.12300000000000, 1.11200000000000]
        """
    def diameter(self, basepoint=...):
        """
        Generalized diameter function on Berkovich space.

        If the basepoint is infinity, the diameter is equal to
        the limit of the radii of the corresponding disks in `\\CC_p`.

        If the basepoint is not infinity, the diameter
        is the Hsia kernel of this point with itself at
        basepoint ``basepoint``.

        INPUT:

        - ``basepoint`` -- (default: ``Infinity``) a point of the
          same Berkovich space as this point

        OUTPUT: a real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(3)
            sage: Q1.diameter()
            0

        ::

            sage: Q2 = B(1/2, 9)
            sage: Q2.diameter()
            9.00000000000000

        The diameter of a type IV point is the limit of the radii::

            sage: R.<x> = PolynomialRing(Qp(3))
            sage: f = R(2)
            sage: S.<y> = PolynomialRing(RR)
            sage: S = FractionField(S)
            sage: g = (y+1)/y
            sage: B(f,g).diameter()
            1.0

        ::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1/81, 1)
            sage: Q2 = B(1/3)
            sage: Q1.diameter(Q2)
            0.00137174211248285

        ::

            sage: Q2.diameter(Q2)
            +infinity
        """
    def path_distance_metric(self, other):
        """
        Return the path distance metric distance between this point and ``other``.

        Also referred to as the hyperbolic metric, or the big metric.

        On the set of type II, III and IV points, the path distance metric
        is a metric. Following Baker and Rumely, we extend
        the path distance metric to type I points `x`, `y` by `\\rho(x,x) = 0` and `\\rho(x,y) =
        \\infty`. See [BR2010]_.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT: a finite or infinite real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1/4, 4)
            sage: Q2 = B(1/4, 6)
            sage: Q1.path_distance_metric(Q2)
            0.369070246428542

        ::

            sage: Q3 = B(1)
            sage: Q3.path_distance_metric(Q1)
            +infinity

        ::

            sage: Q3.path_distance_metric(Q3)
            0
        """
    big_metric = path_distance_metric
    hyperbolic_metric = path_distance_metric
    def Hsia_kernel(self, other, basepoint):
        """
        The Hsia kernel of this point and ``other``,
        with basepoint ``basepoint``.

        The Hsia kernel with arbitrary basepoint
        is a generalization of the Hsia kernel at infinity.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point
        - ``basepoint`` -- a point of the same Berkovich space as this point

        OUTPUT: a finite or infinite real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(2, 9)
            sage: Q2 = B(1/27, 1/27)
            sage: Q3 = B(1, 1/3)
            sage: Q1.Hsia_kernel(Q2, Q3)
            0.111111111111111

        ::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(2, 9)
            sage: Q2 = B(1/2)
            sage: Q3 = B(1/2)
            sage: Q1.Hsia_kernel(Q2, Q3)
            +infinity
        """
    def small_metric(self, other):
        """
        Return the small metric distance between this point and ``other``.

        The small metric is an extension of twice
        the spherical distance on `P^1(\\CC_p)`.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT: a real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1/4, 4)
            sage: Q2 = B(1/4, 6)
            sage: Q1.small_metric(Q2)
            0.0833333333333333

        ::

            sage: B = Berkovich_Cp_Projective(QQ, 5)
            sage: Q1 = B(0, 1)
            sage: Q2 = B(99)
            sage: Q1.small_metric(Q2)
            1.00000000000000

        ::

            sage: Q3 = B(1/4, 4)
            sage: Q3.small_metric(Q2)
            1.75000000000000

        ::

            sage: Q2.small_metric(Q3)
            1.75000000000000
        """
    def potential_kernel(self, other, basepoint):
        """
        The potential kernel of this point with ``other``,
        with basepoint ``basepoint``.

        The potential kernel is the hyperbolic distance
        between ``basepoint`` and the join of this point
        with ``other`` relative to ``basepoint``.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point
        - ``basepoint`` -- a point of the same Berkovich space as this point

        OUTPUT: a finite or infinite real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(27, 1)
            sage: Q2 = B(1/3, 2)
            sage: Q3 = B(1/9, 1/2)
            sage: Q3.potential_kernel(Q1, Q2)
            0.369070246428543

        ::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(27, 1)
            sage: Q2 = B(1/3, 2)
            sage: Q3 = B(1/9, 1/2)
            sage: Q3.potential_kernel(Q1, Q2)
            0.369070246428543
        """
    def spherical_kernel(self, other):
        """
        The spherical kernel of this point with ``other``.

        The spherical kernel is one possible extension of the spherical
        distance on `P^1(\\CC_p)` to the projective Berkovich line.
        See [BR2010]_ for details.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT: a real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(2, 2)
            sage: Q2 = B(1/9, 1)
            sage: Q1.spherical_kernel(Q2)
            0.500000000000000

        ::

            sage: Q3 = B(2)
            sage: Q3.spherical_kernel(Q3)
            0
        """
    def Hsia_kernel_infinity(self, other):
        """
        Return the Hsia kernel at infinity of this point with ``other``.

        The Hsia kernel at infinity is the natural extension of the
        absolute value on `\\CC_p` to Berkovich space.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT: a real number

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(Qp(3))
            sage: Q1 = B(1/4, 4)
            sage: Q2 = B(1/4, 6)
            sage: Q1.Hsia_kernel_infinity(Q2)
            6.00000000000000

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.ideal(-1/2*a^2 + a - 3)
            sage: B = Berkovich_Cp_Projective(A, ideal)
            sage: Q1 = B(4)
            sage: Q2 = B(0, 1.5)
            sage: Q1.Hsia_kernel_infinity(Q2)
            1.50000000000000
        """
    def center(self):
        """
        Return the center of the corresponding disk (or sequence of disks)
        in `\\CC_p`.

        OUTPUT: an element of the ``base`` of the parent Berkovich space

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: B(3, 1).center()
            3 + O(3^21)

        ::

            sage: C = Berkovich_Cp_Projective(3)
            sage: C(3, 1).center()
            (3 + O(3^21) : 1 + O(3^20))

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.ideal(-1/2*a^2 + a - 3)
            sage: B = Berkovich_Cp_Projective(A, ideal)
            sage: B(a^2 + 4).center()
            (a^2 + 4 : 1)
        """
    def type_of_point(self):
        """
        Return the type of this point of Berkovich space over `\\CC_p`.

        OUTPUT: integer between 1 and 4 inclusive

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: B(1).type_of_point()
            1

        ::

            sage: B(0, 1).type_of_point()
            2
        """
    def prime(self):
        """
        The residue characteristic of the parent.

        OUTPUT: a prime integer

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: B(1).prime()
            3
        """
    def __ne__(self, other):
        """
        Non-equality operator.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(3, 3**(1/2))
            sage: Q2 = B(3, RR(3**(1/2)))
            sage: Q1 != Q2
            False
        """

class Berkovich_Element_Cp_Affine(Berkovich_Element_Cp):
    """
    Element class of the Berkovich affine line over `\\CC_p`.

    Elements are categorized into four types, represented by specific data:

    - Type I points are represented by a center in the ``base`` of the parent Berkovich space,
      which is `\\QQ_p`, a finite extension of `\\QQ_p`, or a number field.

    - Type II points are represented by a center in the ``base`` of the parent Berkovich space,
      and a rational power of `p`.

    - Type III points are represented by a center in the ``base`` of the parent Berkovich space,
      and a radius, a real number in `[0,\\infty)`.

    - Type IV points are represented by a finite list of centers in the ``base`` of the parent
      Berkovich space and a finite list of radii in `[0,\\infty)`. Type IV points can be created
      from univariate functions, allowing for arbitrary precision.

    INPUT:

    - ``center`` -- for type I, II, and III points, the center of the
      corresponding disk in `\\CC_p`. If the parent Berkovich space was created using a number field
      `K`, then ``center`` must be an element of `K`. Otherwise, ``center`` must be an element of a
      `p`-adic field. For type IV points, can be a list of centers used to approximate the point or a
      univariate function that computes the centers (computation starts at 1).

    - ``radius`` -- (optional) For type I, II, and III points, the radius of the
      corresponding disk in ``Cp``. Must coerce into the real numbers. For type IV points,
      can be a list of radii used to approximate the point or a univariate function that
      computes the radii (computation starts at 1).

    - ``power`` -- (optional) Rational number. Used for constructing type II points; specifies
      the power of ``p`` such that `p^\\text{power}` = radius

    - ``prec`` -- (default: 20) the number of disks to be used to approximate a type IV point

    - ``error_check`` -- boolean (default: ``True``); if error checking should be run on input. If
      input is correctly formatted, can be set to ``False`` for better performance.
      WARNING: with error check set to ``False``, any error in the input will lead to
      incorrect results.

    EXAMPLES:

    Type I points can be created by specifying the corresponding point of ``Cp``::

        sage: B = Berkovich_Cp_Affine(Qp(3))
        sage: B(4)
        Type I point centered at 1 + 3 + O(3^20)

    The center of a point can be an element of a finite extension of ``Qp``::

        sage: A.<t> = Qq(27)
        sage: B(1 + t)
        Type I point centered at (t + 1) + O(3^20)

    Type II and III points can be created by specifying a center and a radius::

        sage: B(2, 3**(1/2))                                                            # needs sage.symbolic
        Type II point centered at 2 + O(3^20) of radius 3^1/2

    ::

        sage: B(2, 1.6)
        Type III point centered at 2 + O(3^20) of radius 1.60000000000000

    Some type II points may be mistaken for type III points::

        sage: B(3, 3**0.5)                      # not tested
        Type III point centered at 3 + O(3^21) of radius 1.73205080756888

    To avoid these errors, specify the power instead of the radius::

        sage: B(3, power=RR(1/100000))
        Type II point centered at 3 + O(3^21) of radius 3^1/100000

    Type IV points can be constructed in a number of ways, the first being
    from a list of centers and radii used to approximate the point::

        sage: B([Qp(3)(2), Qp(3)(2), Qp(3)(2)], [1.761, 1.123, 1.112])
        Type IV point of precision 3, approximated by disks centered at
        [2 + O(3^20), 2 + O(3^20)] ... with radii [1.76100000000000, 1.12300000000000] ...

    Type IV points can be constructed from univariate functions, with arbitrary precision::

        sage: A.<t> = Qq(27)
        sage: R.<x> = PolynomialRing(A)
        sage: f = (1 + t)^2*x
        sage: S.<y> = PolynomialRing(RR)
        sage: S = FractionField(S)
        sage: g = (y + 1)/y
        sage: d = B(f, g, prec=100); d
        Type IV point of precision 100 with centers given by
        ((t^2 + 2*t + 1) + O(3^20))*x and radii given by (y + 1.00000000000000)/y

    For increased performance, ``error_check`` can be set to ``False``. WARNING: with error check set
    to ``False``, any error in the input will lead to incorrect results::

        sage: B(f, g, prec=100, error_check=False)
        Type IV point of precision 100 with centers given by
        ((t^2 + 2*t + 1) + O(3^20))*x and radii given by (y + 1.00000000000000)/y

    When creating a Berkovich space backed by a number field, points can be created similarly::

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: A.<a> = NumberField(x^3 + 20)
        sage: ideal = A.prime_above(3)
        sage: B = Berkovich_Cp_Projective(A, ideal)
        sage: Q1 = B(a); Q1
        Type I point centered at (a : 1)

    ::

        sage: B(a + 1, 3)                                                               # needs sage.rings.number_field
        Type II point centered at (a + 1 : 1) of radius 3^1

    TESTS::

        sage: A = Berkovich_Cp_Affine(3)
        sage: Q1 = A(3, 1); Q1
        Type II point centered at 3 + O(3^21) of radius 3^0
        sage: Q2 = A(2.5, 1); Q2
        Type II point centered at 1 + 2*3 + 3^2 + 3^3 + 3^4 + 3^5 + 3^6 + 3^7 +
        3^8 + 3^9 + 3^10 + 3^11 + 3^12 + 3^13 + 3^14 + 3^15 + 3^16 + 3^17 +
        3^18 + 3^19 + O(3^20) of radius 3^0
        sage: Q5 = A(3, 0); Q5
        Type I point centered at 3 + O(3^21)
        sage: A(Zp(3)(2), 2).center().parent() == A(Qp(3)(2), 2).center().parent()
        True
        sage: Q1 == Q2
        True
        sage: Q1 == Q5
        False
        sage: Q3 = A(Qp(3)(3), power=0, error_check=False); Q3
        Type II point centered at 3 + O(3^21) of radius 3^0
        sage: Q4 = A(3, 3**0); Q4
        Type II point centered at 3 + O(3^21) of radius 3^0
        sage: Q5 = A(3, power=1/2); Q5
        Type II point centered at 3 + O(3^21) of radius 3^1/2
        sage: Q6 = A(3, RR(3**(1/2))); Q6                                               # needs sage.symbolic
        Type III point centered at 3 + O(3^21) of radius 1.73205080756888
        sage: Q5 == Q6                                                                  # needs sage.symbolic
        True

        sage: k = Qp(5)
        sage: R.<x> = k[]
        sage: l.<w> = k.extension(x^2 - 5)
        sage: B = Berkovich_Cp_Affine(5)
        sage: B(w, power=1)
        Type II point centered at w + O(w^41) of radius 5^1

        sage: TestSuite(Q5).run()
    """
    def __init__(self, parent, center, radius=None, power=None, prec: int = 20, error_check: bool = True) -> None:
        """
        Initialization function.

        EXAMPLES::

            sage: A = Berkovich_Cp_Affine(17)
            sage: A(5, 1)
            Type II point centered at 5 + O(17^20) of radius 17^0
        """
    def as_projective_point(self):
        """
        Return the corresponding point of projective Berkovich space.

        We identify affine Berkovich space with the subset `P^1_{\\text{Berk}}(C_p) - \\{(1 : 0)\\}`.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(5)
            sage: B(5).as_projective_point()
            Type I point centered at (5 + O(5^21) : 1 + O(5^20))

        ::

            sage: B(0, 1).as_projective_point()
            Type II point centered at (0 : 1 + O(5^20)) of radius 5^0

        ::

            sage: L.<t> = PolynomialRing(Qp(5))
            sage: T = FractionField(L)
            sage: f = T(1/t)
            sage: R.<x> = RR[]
            sage: Y = FractionField(R)
            sage: g = (40*pi)/x                                                         # needs sage.symbolic
            sage: Q2 = B(f, g)                                                          # needs sage.symbolic
            sage: Q2.as_projective_point()                                              # needs sage.symbolic
            Type IV point of precision 20 with centers given by (1 + O(5^20))/((1 + O(5^20))*t)
            and radii given by 40.0000000000000*pi/x
        """
    def __eq__(self, other):
        """
        Equality operator.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(1, RR(3**(1/2)))                                               # needs sage.symbolic
            sage: Q2 = B(1, 3**(1/2))                                                   # needs sage.symbolic
            sage: Q1 == Q2                                                              # needs sage.symbolic
            True

        ::

            sage: Q3 = B(1)
            sage: Q4 = B(4)
            sage: Q3 == Q4
            False

        ::

            sage: Q5 = B(1, 4)
            sage: Q1 == Q5                                                              # needs sage.symbolic
            False

        ::

            sage: Q1 == Q3                                                              # needs sage.symbolic
            False
        """
    def __hash__(self):
        """
        Return the hash of this point.

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1, RR(3**(1/2)))                                               # needs sage.symbolic
            sage: Q2 = B(1, 3**(1/2))                                                   # needs sage.symbolic
            sage: hash(Q1) == hash(Q2)                                                  # needs sage.symbolic
            True

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.ideal(-1/2*a^2 + a - 3)
            sage: B = Berkovich_Cp_Projective(A, ideal)
            sage: Q1 = B(a^2 + 1, 2)
            sage: Q2 = B(0, 2)
            sage: hash(Q1) == hash(Q2)
            True
        """
    def lt(self, other):
        """
        Return ``True`` if this point is strictly less than ``other`` in the standard partial order.

        Roughly, the partial order corresponds to containment of
        the corresponding disks in ``Cp``.

        For example, let x and y be points of type II or III.
        If x has center `c_1` and radius `r_1` and y has center
        `c_2` and radius `r_2`, `x < y` if and only if `D(c_1,r_1)`
        is a subset of `D(c_2,r_2)` in `\\CC_p`.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT:

        - ``True`` -- if this point is less than ``other`` in the standard partial order
        - ``False`` -- otherwise

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(5, 0.5)
            sage: Q2 = B(5, 1)
            sage: Q1.lt(Q2)
            True

        ::

            sage: Q3 = B(1)
            sage: Q1.lt(Q3)
            False

        TESTS::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(5)
            sage: Q1.lt(Q1)
            False

        ::

            sage: Q2 = B([4, 1/3], [5, 1])
            sage: Q1.lt(Q2)
            False

        ::

            sage: Q4 = B(0, 1)
            sage: Q1.lt(Q4)
            True

        ::

            sage: Q2.lt(Q4)
            False
        """
    def gt(self, other):
        """
        Return ``True`` if this point is strictly greater than ``other`` in the standard partial order.

        Roughly, the partial order corresponds to containment of
        the corresponding disks in `\\CC_p`.

        For example, let x and y be points of type II or III.
        If x has center `c_1` and radius `r_1` and y has center
        `c_2` and radius `r_2`, `x < y` if and only if `D(c_1,r_1)`
        is a subset of `D(c_2,r_2)` in `\\CC_p`.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT:

        - ``True`` -- if this point is greater than ``other`` in the standard partial order
        - ``False`` -- otherwise

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(QQ, 3)
            sage: Q1 = B(5, 3)
            sage: Q2 = B(5, 1)
            sage: Q1.gt(Q2)
            True

        ::

            sage: Q3 = B(1/27)
            sage: Q1.gt(Q3)
            False

        TESTS::

            sage: B = Berkovich_Cp_Affine(QQ, 3)
            sage: Q1 = B(5)
            sage: Q1.gt(Q1)
            False

        ::

            sage: Q2 = B(0, 1)
            sage: Q1.gt(Q2)
            False

        ::

            sage: Q3 = B([0, 3], [5, 1])
            sage: Q2.gt(Q3)
            True
        """
    def join(self, other, basepoint=...):
        """
        Compute the join of this point and ``other`` with respect to ``basepoint``.

        The join is first point that lies on the intersection
        of the path from this point to ``basepoint`` and the path from ``other`` to
        ``basepoint``.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point
        - ``basepoint`` -- (default: ``Infinity``) a point of the same
          Berkovich space as this point or ``Infinity``

        OUTPUT: a point of the same Berkovich space

        EXAMPLES::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(2, 1)
            sage: Q2 = B(2, 2)
            sage: Q1.join(Q2)
            Type III point centered at 2 + O(3^20) of radius 2.00000000000000

        ::

            sage: Q3 = B(5)
            sage: Q3.join(Q1)
            Type II point centered at 2 + 3 + O(3^20) of radius 3^0

        ::

            sage: Q3.join(Q1, basepoint=Q2)
            Type II point centered at 2 + O(3^20) of radius 3^0

        TESTS::

            sage: Q4 = B(1/3**8 + 2, 1)
            sage: Q2.join(Q4, basepoint=Q1)
            Type III point centered at 2 + O(3^20) of radius 2.00000000000000

        ::

            sage: Q5 = B(2, 1/9)
            sage: Q6 = B(1, 1/27)
            sage: Q4.join(Q5, basepoint=Q6)
            Type II point centered at 1 + O(3^20) of radius 3^0

        ::

            sage: Q7 = B(1/27, 1/27)
            sage: Q1.join(Q7, Q2)
            Type III point centered at 2 + O(3^20) of radius 2.00000000000000
        """
    def involution_map(self):
        """
        Return the image of this point under the involution map.

        The involution map is the extension of the map ``z |-> 1/z``
        on `\\CC_p` to Berkovich space.

        For affine Berkovich space, not defined for the type I
        point centered at 0.

        If zero is contained in every disk approximating a type IV point,
        then the image under the involution map is not defined. To avoid
        this error, increase precision.

        OUTPUT: a point of the same Berkovich space

        EXAMPLES:

        The involution map is 1/z on type I points::

            sage: B = Berkovich_Cp_Affine(3)
            sage: Q1 = B(1/2)
            sage: Q1.involution_map()
            Type I point centered at 2 + O(3^20)

        ::

            sage: Q2 = B(0, 1/3)
            sage: Q2.involution_map()
            Type II point centered at 0 of radius 3^1

        ::

            sage: Q3 = B(1/3, 1/3)
            sage: Q3.involution_map()
            Type II point centered at 3 + O(3^21) of radius 3^-3

        TESTS::

            sage: B = Berkovich_Cp_Affine(3)
            sage: B(0).involution_map()
            Traceback (most recent call last):
            ...
            ValueError: involution map not defined on affine type I point centered at 0

        ::

            sage: B(1/81, 1.5).involution_map()
            Type III point centered at 3^4 + O(3^24) of radius 0.000228623685413809

        ::

            sage: B([1, 2], [3, 1]).involution_map()
            Traceback (most recent call last):
            ...
            ValueError: precision of type IV is not high enough to define image

        ::

            sage: B([1/81, 10/81], [10, 9]).involution_map()
            Type IV point of precision 2, approximated by disks centered at [3^4 + O(3^24),
            3^4 + 2*3^6 + 2*3^7 + 2*3^10 + 2*3^11 + 2*3^14 + 2*3^15 + 2*3^18 + 2*3^19 + 2*3^22
            + 2*3^23 + O(3^24)] ... with radii [0.00152415790275873, 0.00137174211248285] ...
        """
    def contained_in_interval(self, start, end):
        """
        Check if this point is an element of the interval [``start``, ``end``].

        INPUT:

        - ``start`` -- a point of the same Berkovich space as this point
        - ``end`` -- a point of the same Berkovich space as this point

        OUTPUT:

        - ``True`` if this point is an element of [``start``, ``end``].
        - ``False`` otherwise.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective((3))
            sage: Q1 = B(2, 1)
            sage: Q2 = B(2, 4)
            sage: Q3 = B(1/3)
            sage: Q2.contained_in_interval(Q1, Q3.join(Q1))
            False

        ::

            sage: Q4 = B(1/81, 1)
            sage: Q2.contained_in_interval(Q1, Q4.join(Q1))
            True
        """

class Berkovich_Element_Cp_Projective(Berkovich_Element_Cp):
    """
    Element class of the Berkovich projective line over `\\CC_p`.

    Elements are categorized into four types, represented by specific data:

    - Type I points are represented by a center in the ``base`` of the parent Berkovich space,
      which is projective space of dimension 1 over either `\\QQ_p`, a finite extension of `\\QQ_p`,
      or a number field.

    - Type II points are represented by a center in the ``base`` of the parent Berkovich space,
      and a rational power of `p`.

    - Type III points are represented by a center in the ``base`` of the parent Berkovich space,
      and by a radius, a real number, in `[0,\\infty)`.

    - Type IV points are represented by a finite list of centers in the ``base`` of the parent
      Berkovich space and a finite list of radii in `[0,\\infty)`.

    The projective Berkovich line is viewed as the one-point compactification of
    the affine Berkovich line. The projective Berkovich line therefore contains
    every point of the affine Berkovich line, along with a type I point centered
    at infinity.

    INPUT:

    - ``center`` -- for type I, II, and III points, the center of the
      corresponding disk in `P^1(\\CC_p)`. If the parent Berkovich space was created using a number field
      `K`, then ``center`` can be an element of `P^1(K)`. Otherwise, ``center``
      must be an element of a projective space of dimension 1 over a `p`-adic field.
      For type IV points, can be a list of centers used to approximate the point or a
      univariate function that computes the centers (computation starts at 1).

    - ``radius`` -- (optional) For type I, II, and III points, the radius of the
      corresponding disk in `\\CC_p`. Must coerce into the real numbers. For type IV points,
      can be a list of radii used to approximate the point or a univariate function that
      computes the radii (computation starts at 1).

    - ``power`` -- (optional) Rational number. Used for constructing type II points; specifies
      the power of ``p`` such that `p^\\text{power}` = radius

    - ``prec`` -- (default: 20) the number of disks to be used to approximate a type IV point

    - ``error_check`` -- boolean (default: ``True``); if error checking should be run on input. If
      input is correctly formatted, can be set to ``False`` for better performance.
      WARNING: with error check set to ``False``, any error in the input will lead to
      incorrect results.

    EXAMPLES:

    Type I points can be created by specifying the corresponding point of `P^1(\\CC_p)`::

        sage: S = ProjectiveSpace(Qp(5), 1)
        sage: P = Berkovich_Cp_Projective(S); P
        Projective Berkovich line over Cp(5) of precision 20

    ::

        sage: a = S(0, 1)
        sage: Q1 = P(a); Q1
        Type I point centered at (0 : 1 + O(5^20))

    ::

        sage: Q2 = P((1,0)); Q2
        Type I point centered at (1 + O(5^20) : 0)

    Type II and III points can be created by specifying a center and a radius::

        sage: Q3 = P((0,5), 5**(3/2)); Q3                                               # needs sage.symbolic
        Type II point centered at (0 : 1 + O(5^20)) of radius 5^3/2

    ::

        sage: Q4 = P(0, 3**(3/2)); Q4                                                   # needs sage.symbolic
        Type III point centered at (0 : 1 + O(5^20)) of radius 5.19615242270663

    Type IV points can be created from lists of centers and radii::

        sage: b = S((3,2))  # create centers
        sage: c = S((4,3))
        sage: d = S((2,3))
        sage: L = [b, c, d]
        sage: R = [1.761, 1.123, 1.112]
        sage: Q5 = P(L, R); Q5
        Type IV point of precision 3, approximated by disks centered at
        [(4 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 2*5^8 + 2*5^9 + 2*5^10 +
         2*5^11 + 2*5^12 + 2*5^13 + 2*5^14 + 2*5^15 + 2*5^16 + 2*5^17 + 2*5^18 + 2*5^19 + O(5^20) :
         1 + O(5^20)), (3 + 3*5 + 5^2 + 3*5^3 + 5^4 + 3*5^5 + 5^6 + 3*5^7 + 5^8 + 3*5^9 +
         5^10 + 3*5^11 + 5^12 + 3*5^13 + 5^14 + 3*5^15 + 5^16 + 3*5^17 + 5^18 + 3*5^19 + O(5^20) :
         1 + O(5^20))] ... with radii [1.76100000000000, 1.12300000000000] ...

    Type IV points can also be created from univariate functions. Since the centers of
    the sequence of disks can not be the point at infinity in `P^1(\\CC_p)`, only functions
    into `\\CC_p` are supported::

        sage: L.<t> = PolynomialRing(Qp(5))
        sage: T = FractionField(L)
        sage: f = T(1/t)
        sage: R.<x> = RR[]
        sage: Y = FractionField(R)
        sage: g = (40*pi)/x                                                             # needs sage.symbolic
        sage: Q6 = P(f, g); Q6                                                          # needs sage.symbolic
        Type IV point of precision 20 with centers given by (1 + O(5^20))/((1 + O(5^20))*t)
         and radii given by 40.0000000000000*pi/x

    TESTS::

        sage: P((1,0), 3)
        Traceback (most recent call last):
        ...
        ValueError: type II and III points can not be centered at infinity

        sage: B = Berkovich_Cp_Projective(3)
        sage: Q1 = B(3)
        sage: TestSuite(Q1).run()
    """
    def __init__(self, parent, center, radius=None, power=None, prec: int = 20, error_check: bool = True) -> None:
        """
        Initialization function.

        EXAMPLES::

            sage: S = ProjectiveSpace(Qp(7), 1)
            sage: P = Berkovich_Cp_Projective(S)
            sage: P(0,1)
            Type II point centered at (0 : 1 + O(7^20)) of radius 7^0
        """
    def as_affine_point(self):
        """
        Return the corresponding affine point after dehomogenizing at infinity.

        OUTPUT: a point of affine Berkovich space

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(5)
            sage: B(5).as_affine_point()
            Type I point centered at 5 + O(5^21)

        ::

            sage: Q = B(0, 1).as_affine_point(); Q
            Type II point centered at 0 of radius 5^0
            sage: Q.parent()
            Affine Berkovich line over Cp(5) of precision 20

        ::

            sage: L.<t> = PolynomialRing(Qp(5))
            sage: T = FractionField(L)
            sage: f = T(1/t)
            sage: R.<x> = RR[]
            sage: Y = FractionField(R)
            sage: g = (40*pi)/x                                                         # needs sage.symbolic
            sage: Q2 = B(f, g)                                                          # needs sage.symbolic
            sage: Q2.as_affine_point()                                                  # needs sage.symbolic
            Type IV point of precision 20 with centers given by (1 + O(5^20))/((1 + O(5^20))*t)
            and radii given by 40.0000000000000*pi/x
        """
    def __eq__(self, other):
        """
        Equality operator.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B([2, 2], RR(3**(1/2)))                                          # needs sage.symbolic
            sage: Q2 = B([1, 1], 3**(1/2))                                              # needs sage.symbolic
            sage: Q1 == Q2                                                              # needs sage.symbolic
            True

        ::

            sage: Q3 = B(1)
            sage: Q4 = B(4)
            sage: Q3 == Q4
            False

        ::

            sage: Q5 = B(1, 4)
            sage: Q1 == Q5                                                              # needs sage.symbolic
            False

        ::

            sage: Q1 == Q3                                                              # needs sage.symbolic
            False
        """
    def __hash__(self):
        """
        Return the hash of this point.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: P = ProjectiveSpace(B.base_ring(), 1)
            sage: Q1 = B(P.point([2, 2], False), RR(3**(1/2)))                          # needs sage.symbolic
            sage: Q2 = B([1, 1], 3**(1/2))                                              # needs sage.symbolic
            sage: hash(Q1) == hash(Q2)                                                  # needs sage.symbolic
            True

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.ideal(-1/2*a^2 + a - 3)
            sage: B = Berkovich_Cp_Projective(A, ideal)
            sage: Q1 = B(a^2 + 1, 2)
            sage: Q2 = B(0, 2)
            sage: hash(Q1) == hash(Q2)
            True
        """
    def lt(self, other):
        """
        Return ``True`` if this point is strictly less than ``other`` in the standard partial order.

        Roughly, the partial order corresponds to containment of
        the corresponding disks in `\\CC_p`.

        For example, let x and y be points of type II or III.
        If x has center `c_1` and radius `r_1` and y has center
        `c_2` and radius `r_2`, `x < y` if and only if `D(c_1,r_1)`
        is a subset of `D(c_2,r_2)` in `\\CC_p`.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT:

        - ``True`` -- if this point is less than ``other`` in the standard partial order
        - ``False`` -- otherwise

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(5, 0.5)
            sage: Q2 = B(5, 1)
            sage: Q1.lt(Q2)
            True

        ::

            sage: Q3 = B(1)
            sage: Q1.lt(Q3)
            False

        TESTS::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(5)
            sage: Q1.lt(Q1)
            False

        ::

            sage: Q2 = B([4, 1/3], [5, 1])
            sage: Q1.lt(Q2)
            False

        ::

            sage: Q3 = B((1,0))
            sage: Q4 = B(0, 1)
            sage: Q3.lt(Q4)
            False

        ::

            sage: Q4.lt(Q3)
            True

        ::

            sage: Q1.lt(Q4)
            True

        ::

            sage: Q2.lt(Q4)
            False
        """
    def gt(self, other):
        """
        Return ``True`` if this point is strictly greater than ``other`` in the standard partial order.

        Roughly, the partial order corresponds to containment of
        the corresponding disks in `\\CC_p`.

        For example, let x and y be points of type II or III.
        If x has center `c_1` and radius `r_1` and y has center
        `c_2` and radius `r_2`, `x < y` if and only if `D(c_1, r_1)`
        is a subset of `D(c_2, r_2)` in `\\CC_p`.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point

        OUTPUT:

        - ``True`` -- if this point is greater than ``other`` in the standard partial order
        - ``False`` -- otherwise

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(QQ, 3)
            sage: Q1 = B(5, 3)
            sage: Q2 = B(5, 1)
            sage: Q1.gt(Q2)
            True

        ::

            sage: Q3 = B(1/27)
            sage: Q1.gt(Q3)
            False

        TESTS::

            sage: B = Berkovich_Cp_Projective(QQ, 3)
            sage: Q1 = B(5)
            sage: Q1.gt(Q1)
            False

        ::

            sage: Q2 = B(0, 1)
            sage: Q1.gt(Q2)
            False

        ::

            sage: Q3 = B([0, 3], [5, 1])
            sage: Q2.gt(Q3)
            True

        ::

            sage: Q4 = B((1,0))
            sage: Q4.gt(Q2)
            True

        ::

            sage: Q1.gt(Q4)
            False
        """
    def join(self, other, basepoint=...):
        """
        Compute the join of this point and ``other``, with respect to ``basepoint``.

        The join is first point that lies on the intersection
        of the path from this point to ``basepoint`` and the path from ``other`` to
        ``basepoint``.

        INPUT:

        - ``other`` -- a point of the same Berkovich space as this point
        - ``basepoint`` -- (default: ``Infinity``) a point of the same
          Berkovich space as this point, or ``Infinity``

        OUTPUT: a point of the same Berkovich space

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(2, 1)
            sage: Q2 = B(2, 2)
            sage: Q1.join(Q2)
            Type III point centered at (2 + O(3^20) : 1 + O(3^20)) of radius 2.00000000000000

        ::

            sage: Q3 = B(5)
            sage: Q3.join(Q1)
            Type II point centered at (2 + 3 + O(3^20) : 1 + O(3^20)) of radius 3^0

        ::

            sage: Q3.join(Q1, basepoint=Q2)
            Type II point centered at (2 + O(3^20) : 1 + O(3^20)) of radius 3^0

        TESTS::

            sage: Q4 = B(1/3**8 + 2, 1)
            sage: Q2.join(Q4, basepoint=Q1)
            Type III point centered at (2 + O(3^20) : 1 + O(3^20)) of radius 2.00000000000000
            sage: Q5 = B(2, 1/9)
            sage: Q6 = B(1, 1/27)
            sage: Q4.join(Q5, basepoint=Q6)
            Type II point centered at (1 + O(3^20) : 1 + O(3^20)) of radius 3^0
            sage: Q7 = B(1/27, 1/27)
            sage: Q1.join(Q7, Q2)
            Type III point centered at (2 + O(3^20) : 1 + O(3^20)) of radius 2.00000000000000
            sage: Q1.join(Q2, Q7)
            Type III point centered at (2 + O(3^20) : 1 + O(3^20)) of radius 2.00000000000000
            sage: Q8 = B(0, power=1/3)
            sage: Q9 = B(0, power=1/2)
            sage: Q8.join(Q9)
            Type II point centered at (0 : 1 + O(3^20)) of radius 3^1/2

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: A.<a> = NumberField(x^3 + 20)
            sage: ideal = A.prime_above(3)
            sage: C = Berkovich_Cp_Projective(A, ideal)
            sage: Q10 = C(a, 1/9)
            sage: Q10.join(Q9)
            Traceback (most recent call last):
            ...
            ValueError: other must be a point of the same projective Berkovich line
            sage: Q11 = C(0, 1/3)
            sage: Q11.join(Q10)
            Type II point centered at (0 : 1) of radius 3^0
        """
    def involution_map(self):
        """
        Return the image of this point under the involution map.

        The involution map is the extension of the map ``z |-> 1/z``
        on `P^1(\\CC_p)` to Berkovich space.

        If zero is contained in every disk approximating a type IV point,
        then the image under the involution map is not defined. To avoid
        this error, increase precision.

        OUTPUT: a point of the same Berkovich space

        EXAMPLES:

        The involution map is 1/z on type I points::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(1/2)
            sage: Q1.involution_map()
            Type I point centered at (2 + O(3^20) : 1 + O(3^20))

        ::

            sage: Q2 = B(0, 1/3)
            sage: Q2.involution_map()
            Type II point centered at (0 : 1 + O(3^20)) of radius 3^1

        ::

            sage: Q3 = B(1/3, 1/3)
            sage: Q3.involution_map()
            Type II point centered at (3 + O(3^21) : 1 + O(3^20)) of radius 3^-3

        TESTS::

            sage: B = Berkovich_Cp_Projective(3)
            sage: B((1,0)).involution_map()
            Type I point centered at (0 : 1 + O(3^20))

        ::

            sage: B(0).involution_map()
            Type I point centered at (1 + O(3^20) : 0)

        ::

            sage: B(1/81, 1.5).involution_map()
            Type III point centered at (3^4 + O(3^24) : 1 + O(3^20)) of radius 0.000228623685413809

        ::

            sage: B([1, 2], [3, 1]).involution_map()
            Traceback (most recent call last):
            ...
            ValueError: precision of type IV is not high enough to define image

        ::

            sage: B([1/81, 10/81], [10, 9]).involution_map()
            Type IV point of precision 2, approximated by disks centered at
            [(3^4 + O(3^24) : 1 + O(3^20)), (3^4 + 2*3^6 + 2*3^7 + 2*3^10 + 2*3^11 +
            2*3^14 + 2*3^15 + 2*3^18 + 2*3^19 + 2*3^22 + 2*3^23 + O(3^24) : 1 + O(3^20))]
            ... with radii [0.00152415790275873, 0.00137174211248285] ...
        """
    def contained_in_interval(self, start, end):
        """
        Check if this point is an element of the interval [``start``, ``end``].

        INPUT:

        - ``start`` -- a point of the same Berkovich space as this point
        - ``end`` -- a point of the same Berkovich space as this point

        OUTPUT:

        - ``True`` if this point is an element of [``start``, ``end``].
        - ``False`` otherwise.

        EXAMPLES::

            sage: B = Berkovich_Cp_Projective(3)
            sage: Q1 = B(2, 1)
            sage: Q2 = B(2, 4)
            sage: Q3 = B(1/3)
            sage: Q2.contained_in_interval(Q1, Q3.join(Q1))
            False

        ::

            sage: Q4 = B(1/81, 1)
            sage: Q2.contained_in_interval(Q1, Q4.join(Q1))
            True

        TESTS::

            sage: B = Berkovich_Cp_Projective(3)
            sage: infty = B((1, 0))
            sage: zero = B(0)
            sage: gauss = B(0, 1)
            sage: infty.contained_in_interval(zero, gauss)
            False

        ::

            sage: Q1 = B(1, 3)
            sage: infty.contained_in_interval(gauss, Q1)
            False

        ::

            sage: zero.contained_in_interval(infty, gauss)
            False

        ::

            sage: gauss.contained_in_interval(zero, infty)
            True

        ::

            sage: Q2 = B(81, 1/3)
            sage: gauss.contained_in_interval(infty, Q2)
            True
        """
