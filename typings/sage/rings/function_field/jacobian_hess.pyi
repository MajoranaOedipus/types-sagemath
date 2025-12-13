from .divisor import FunctionFieldDivisor as FunctionFieldDivisor
from .jacobian_base import JacobianGroup_base as JacobianGroup_base, JacobianGroup_finite_field_base as JacobianGroup_finite_field_base, JacobianPoint_base as JacobianPoint_base, JacobianPoint_finite_field_base as JacobianPoint_finite_field_base, Jacobian_base as Jacobian_base
from .place import FunctionFieldPlace as FunctionFieldPlace
from sage.arith.functions import lcm as lcm
from sage.arith.misc import integer_ceil as integer_ceil
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.structure.richcmp import op_EQ as op_EQ, richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class JacobianPoint(JacobianPoint_base):
    """
    Points of Jacobians represented by a pair of ideals.

    If a point of Jacobian is determined by `D`, then the divisor `D` is
    represented by a pair of ideals in the finite maximal order and the
    infinite maximal order of the function field.

    For efficiency reasons, the actual ideals stored are the inverted ideals
    of the ideals representing the divisor `D`.

    INPUT:

    - ``parent`` -- Jacobian group

    - ``dS`` -- an ideal of the finite maximal order of a function field

    - ``ds`` -- an ideal of infinite maximal order of a function field

    EXAMPLES::

        sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: G = C.jacobian(model='hess', base_div=b).group()
        sage: pl = C([1,8,1]).place()
        sage: p = G.point(pl - b)
        sage: dS, ds = p._data
        sage: -(dS.divisor() + ds.divisor()) == pl
        True
    """
    def __init__(self, parent, dS, ds) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: G = C.jacobian(model='hess', base_div=b).group()
            sage: pl = C([1,8,1]).place()
            sage: p = G.point(pl - b)
            sage: TestSuite(p).run(skip=['_test_category','_test_pickling'])
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: f = x/(y + 1)
            sage: d = f.divisor()
            sage: {d: 1}
            {Place (1/x, 1/x^4*y^2 + 1/x^2*y + 1)
              + Place (1/x, 1/x^2*y + 1)
              + 3*Place (x, (1/(x^3 + x^2 + x))*y^2)
              - 6*Place (x + 1, y + 1): 1}
        """
    def multiple(self, n):
        """
        Return the ``n``-th multiple of this point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: G = C.jacobian(model='hess', base_div=b).group()
            sage: pl = C([-1,2,1]).place()
            sage: p = G.point(pl - b)
            sage: p.multiple(100)
            [Place (1/y, 1/y*z + 8)]
        """
    def addflip(self, other):
        """
        Return the addflip of this and ``other`` point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: G = C.jacobian(model='hess', base_div=b).group()
            sage: pl1 = C([-1,2,1]).place()
            sage: pl2 = C([2,19,1]).place()
            sage: p1 = G.point(pl1 - b)
            sage: p2 = G.point(pl2 - b)
            sage: p1.addflip(p2)
            [Place (y + 8, z + 27)]
            sage: _ == -(p1 + p2)
            True
        """
    def defining_divisor(self):
        """
        Return the effective divisor that defines this point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: G = C.jacobian(model='hess', base_div=b).group()
            sage: pl = C([-1,2,1]).place()
            sage: p = G.point(pl - b)
            sage: p.defining_divisor() == pl
            True
        """
    def order(self, bound=None):
        """
        Return the order of this point.

        ALGORITHM: Shanks' Baby Step Giant Step

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: G = C.jacobian(model='hess', base_div=b).group()
            sage: p = C([-1,2,1]).place()
            sage: pt = G.point(p - b)
            sage: pt.order()
            30
        """
    def divisor(self):
        """
        Return the divisor representing this point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(29), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: G = C.jacobian(model='hess', base_div=b).group()
            sage: pl = C([-1,2,1]).place()
            sage: p = G.point(pl - b)
            sage: G.point(p.divisor()) == p
            True
        """

class JacobianPoint_finite_field(JacobianPoint, JacobianPoint_finite_field_base):
    """
    Points of Jacobians over finite fields
    """

class JacobianGroupEmbedding(Map):
    """
    Embeddings between Jacobian groups.

    INPUT:

    - ``base_group`` -- Jacobian group over a base field

    - ``extension_group`` -- Jacobian group over an extension field

    EXAMPLES::

        sage: k = GF(17)
        sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: J = C.jacobian(model='hess', base_div=b)
        sage: G1 = J.group()
        sage: K = k.extension(3)
        sage: G3 = J.group(K)
        sage: G3.coerce_map_from(G1)
        Jacobian group embedding map:
          From: Group of rational points of Jacobian
           over Finite Field of size 17 (Hess model)
          To:   Group of rational points of Jacobian
           over Finite Field in z3 of size 17^3 (Hess model)
    """
    def __init__(self, base_group, extension_group) -> None:
        """
        Initialize.

        TESTS::

            sage: k = GF(17)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G1 = J.group()
            sage: K = k.extension(3)
            sage: G3 = J.group(K)
            sage: map = G3.coerce_map_from(G1)
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

        sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: J = C.jacobian(model='hess', base_div=b)
        sage: J.group()
        Group of rational points of Jacobian
         over Finite Field of size 17 (Hess model)
    """
    Element = JacobianPoint
    def __init__(self, parent, function_field, base_div) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G = J.group()
            sage: TestSuite(G).run(skip=['_test_elements', '_test_pickling'])
        """
    def point(self, divisor):
        """
        Return the point represented by the divisor of degree zero.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G = J.group()
            sage: p = C([-1,2,1]).place()
            sage: G.point(p - b)
            [Place (y + 2, z + 1)]
        """
    @cached_method
    def zero(self):
        """
        Return the zero element of this group.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G = J.group()
            sage: G.zero()
            [Place (1/y, 1/y*z)]
        """

class JacobianGroup_finite_field(JacobianGroup, JacobianGroup_finite_field_base):
    """
    Jacobian groups of function fields over finite fields.

    INPUT:

    - ``parent`` -- a Jacobian

    - ``function_field`` -- a function field

    - ``base_div`` -- an effective divisor of the function field

    EXAMPLES::

        sage: k = GF(17)
        sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: J = C.jacobian(model='hess', base_div=b)
        sage: G1 = J.group()
        sage: K = k.extension(3)
        sage: G3 = J.group(K)
        sage: G3.coerce_map_from(G1)
        Jacobian group embedding map:
          From: Group of rational points of Jacobian
           over Finite Field of size 17 (Hess model)
          To:   Group of rational points of Jacobian
           over Finite Field in z3 of size 17^3 (Hess model)
    """
    Element = JacobianPoint_finite_field
    def __init__(self, parent, function_field, base_div) -> None:
        """
        Initialize.

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: G = J.group()
            sage: TestSuite(G).run(skip=['_test_elements','_test_pickling'])
        """
    def __iter__(self):
        """
        Return generator of points of this group.

        TESTS::

            sage: k = GF(7)
            sage: A.<x,y> = AffineSpace(k,2)
            sage: C = Curve(y^2 + x^3 + 2*x + 1).projective_closure()
            sage: J = C.jacobian(model='hess')
            sage: G = J.group()
            sage: len([pt for pt in G])
            11
        """

class Jacobian(Jacobian_base, UniqueRepresentation):
    """
    Jacobians of function fields.

    EXAMPLES::

        sage: k = GF(17)
        sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
        sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
        sage: b = C([0,1,0]).place()
        sage: C.jacobian(model='hess', base_div=b)
        Jacobian of Projective Plane Curve over Finite Field of size 17
         defined by x^3 - y^2*z + 5*z^3 (Hess model)
    """
    def __init__(self, function_field, base_div, **kwds) -> None:
        """
        Initialize.

        TESTS::

            sage: k = GF(17)
            sage: P2.<x,y,z> = ProjectiveSpace(k, 2)
            sage: C = Curve(x^3 + 5*z^3 - y^2*z, P2)
            sage: b = C([0,1,0]).place()
            sage: J = C.jacobian(model='hess', base_div=b)
            sage: TestSuite(J).run(skip=['_test_elements','_test_pickling'])
        """
