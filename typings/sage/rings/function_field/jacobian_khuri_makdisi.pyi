from .divisor import FunctionFieldDivisor as FunctionFieldDivisor
from .jacobian_base import JacobianGroup_base as JacobianGroup_base, JacobianGroup_finite_field_base as JacobianGroup_finite_field_base, JacobianPoint_base as JacobianPoint_base, JacobianPoint_finite_field_base as JacobianPoint_finite_field_base, Jacobian_base as Jacobian_base
from .place import FunctionFieldPlace as FunctionFieldPlace
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.richcmp import op_EQ as op_EQ, richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class JacobianPoint(JacobianPoint_base):
    """
    Points of a Jacobian group.

    INPUT:

    - ``parent`` -- Jacobian group

    - ``w`` -- matrix

    EXAMPLES::

        sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: h = C.function(y/x).divisor_of_poles()
        sage: J = C.jacobian(model='km_large', base_div=h)
        sage: G = J.group()
        sage: pl = C([3,2,1]).place()
        sage: G.point(pl - b)
        Point of Jacobian determined by
        [1 0 0 0 0 0 0 2 3]
        [0 1 0 0 0 0 0 0 3]
        [0 0 1 0 0 0 0 0 1]
        [0 0 0 1 0 0 0 0 5]
        [0 0 0 0 0 1 0 0 5]
        [0 0 0 0 0 0 1 0 4]
    """
    def __init__(self, parent, w) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: pl = C([3,2,1]).place()
            sage: p = G.point(pl - b)
            sage: TestSuite(p).run(skip=['_test_category','_test_pickling'])
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: F = C.function_field()
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: zero = G.zero()
            sage: {zero: 1}
            {Point of Jacobian determined by
             [1 0 0 0 0 0 0 0 0]
             [0 1 0 0 0 0 0 0 0]
             [0 0 1 0 0 0 0 0 0]
             [0 0 0 0 1 0 0 0 0]
             [0 0 0 0 0 1 0 0 0]
             [0 0 0 0 0 0 0 1 0]: 1}
        """
    def multiple(self, n):
        """
        Return the ``n``-th multiple of this point.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p = G.point(pl - b)
            sage: p.multiple(100)
            Point of Jacobian determined by
            [1 0 0 0 0 2 0 1 1]
            [0 1 0 0 0 5 0 1 6]
            [0 0 1 0 0 2 0 6 3]
            [0 0 0 1 0 1 0 0 0]
            [0 0 0 0 1 5 0 1 4]
            [0 0 0 0 0 0 1 1 0]
        """
    def addflip(self, other):
        """
        Return the addflip of this and ``other`` point.

        The addflip of two points is by definition the negative of the sum of
        the points. This operation is faster than addition in Jacobian
        arithmetic by Khuri-Makdisi algorithms.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: b = C([0,1,0]).place()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([3,2,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: p1.addflip(p2)
            Point of Jacobian determined by
            [1 0 0 0 0 0 0 2 6]
            [0 1 0 0 0 0 0 0 3]
            [0 0 1 0 0 0 0 0 4]
            [0 0 0 1 0 0 0 0 3]
            [0 0 0 0 0 1 0 0 5]
            [0 0 0 0 0 0 1 0 2]
            sage: _ == -(p1 + p2)
            True
        """
    def defining_matrix(self):
        """
        Return the matrix whose row span determines the effective divisor
        representing this point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: b = C([0,1,0]).place()
            sage: pl = C([-1,2,1]).place()
            sage: p = G.point(pl - b)
            sage: p.defining_matrix()
            [1 0 0 0 0 0 0 2 5]
            [0 1 0 0 0 0 0 0 3]
            [0 0 1 0 0 0 0 0 2]
            [0 0 0 1 0 0 0 0 6]
            [0 0 0 0 0 1 0 0 5]
            [0 0 0 0 0 0 1 0 1]
        """
    def divisor(self):
        """
        Return the divisor representing this point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: F = C.function_field()
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: b = F.get_place(1)
            sage: p = C([-1,2,1]).place()
            sage: pt = G.point(p - b)
            sage: G.point(pt.divisor()) == pt
            True

        ALGORITHM: Lemma 2.1 of [Khu2004]_.
        """

class JacobianPoint_finite_field(JacobianPoint, JacobianPoint_finite_field_base): ...

class JacobianGroupEmbedding(Map):
    """
    Embeddings between Jacobian groups.

    INPUT:

    - ``base_group`` -- Jacobian group over a base field

    - ``extension_group`` -- Jacobian group over an extension field

    EXAMPLES::

        sage: k = GF(5)
        sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
        sage: C = Curve(x^3 + z^3 - y^2*z, P2)
        sage: h = C.function(y/x).divisor_of_poles()
        sage: J = C.jacobian(model='km_large', base_div=h)
        sage: G1 = J.group()
        sage: K = k.extension(2)
        sage: G2 = J.group(K)
        sage: G2.coerce_map_from(G1)
        Jacobian group embedding map:
          From: Group of rational points of Jacobian
                over Finite Field of size 5 (Khuri-Makdisi large model)
          To:   Group of rational points of Jacobian
                over Finite Field in z2 of size 5^2 (Khuri-Makdisi large model)
    """
    def __init__(self, base_group, extension_group) -> None:
        """
        Initialize.

        TESTS::

            sage: k = GF(5)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G1 = J.group()
            sage: K = k.extension(2)
            sage: G2 = J.group(K)
            sage: map = G2.coerce_map_from(G1)
            sage: TestSuite(map).run(skip=['_test_category', '_test_pickling'])
        """

class JacobianGroup(UniqueRepresentation, JacobianGroup_base):
    """
    Groups of rational points of a Jacobian.

    INPUT:

    - ``parent`` -- a Jacobian

    - ``function_field`` -- a function field

    - ``base_div`` -- an effective divisor of the function field

    EXAMPLES::

        sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: h = C.function(y/x).divisor_of_poles()
        sage: J = C.jacobian(model='km_large', base_div=h)
        sage: J.group()
        Group of rational points of Jacobian
         over Finite Field of size 7 (Khuri-Makdisi large model)
    """
    Element = JacobianPoint
    def __init__(self, parent, function_field, base_div) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
        """
    def point(self, divisor):
        """
        Return the point represented by the divisor.

        INPUT:

        - ``divisor`` -- a divisor of degree zero

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: b = C([0,1,0]).place()
            sage: p = C([-1,2,1]).place()
            sage: G.point(p - b)
            Point of Jacobian determined by
            [1 0 0 0 0 0 0 2 5]
            [0 1 0 0 0 0 0 0 3]
            [0 0 1 0 0 0 0 0 2]
            [0 0 0 1 0 0 0 0 6]
            [0 0 0 0 0 1 0 0 5]
            [0 0 0 0 0 0 1 0 1]
        """
    @cached_method
    def zero(self):
        """
        Return the zero element of this group.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: G.zero()
            Point of Jacobian determined by
            [1 0 0 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0]
            [0 0 0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0 0 0]
            [0 0 0 0 0 0 0 1 0]
        """

class JacobianGroup_finite_field(JacobianGroup, JacobianGroup_finite_field_base):
    """
    Jacobian groups of function fields over finite fields.

    INPUT:

    - ``parent`` -- a Jacobian

    - ``function_field`` -- a function field

    - ``base_div`` -- an effective divisor of the function field

    EXAMPLES::

        sage: k = GF(7)
        sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: h = C.function(y/x).divisor_of_poles()
        sage: J = C.jacobian(model='km_large', base_div=h)
        sage: G1 = J.group()
        sage: K = k.extension(2)
        sage: G2 = J.group(K)
        sage: G2.coerce_map_from(G1)
        Jacobian group embedding map:
          From: Group of rational points of Jacobian
                over Finite Field of size 7 (Khuri-Makdisi large model)
          To:   Group of rational points of Jacobian
                over Finite Field in z2 of size 7^2 (Khuri-Makdisi large model)
    """
    Element = JacobianPoint_finite_field
    def __init__(self, parent, function_field, base_div) -> None:
        """
        Initialize.

        TESTS::

            sage: k = GF(7)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: h = C.function(y/x).divisor_of_poles()
            sage: J = C.jacobian(model='km_large', base_div=h)
            sage: G = J.group()
            sage: TestSuite(G).run(skip=['_test_elements', '_test_pickling'])
        """
    def __iter__(self):
        """
        Return generator of points of this group.

        TESTS::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: b = C([0,0,1]).place()
            sage: J = C.jacobian(model='km_large', base_div=3*b)
            sage: G = J.group()
            sage: len([pt for pt in G])  # long time
            11
        """

class Jacobian(UniqueRepresentation, Jacobian_base):
    """
    Jacobians implemented by Khuri-Makdisi's algorithms.

    EXAMPLES::

        sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: C.jacobian(model='km')
        Jacobian of Projective Plane Curve over Finite Field of size 7
         defined by x^3 - y^2*z - 2*z^3 (Khuri-Makdisi large model)
    """
    def __init__(self, function_field, base_div, model, **kwds) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: J = C.jacobian(model='km_large')
            sage: TestSuite(J).run(skip=['_test_elements', '_test_pickling'])

        ::

            sage: J = C.jacobian(model='km_unknown')
            Traceback (most recent call last):
            ...
            ValueError: unknown model
        """
