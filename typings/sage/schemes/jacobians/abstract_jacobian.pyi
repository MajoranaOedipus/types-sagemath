from sage.categories.fields import Fields as Fields
from sage.categories.schemes import Jacobians as Jacobians
from sage.schemes.generic.scheme import Scheme as Scheme
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

def is_Jacobian(J):
    """
    Return ``True`` if `J` is of type ``Jacobian_generic``.

    EXAMPLES::

        sage: from sage.schemes.jacobians.abstract_jacobian import Jacobian, is_Jacobian
        sage: P2.<x, y, z> = ProjectiveSpace(QQ, 2)
        sage: C = Curve(x^3 + y^3 + z^3)
        sage: J = Jacobian(C)
        sage: is_Jacobian(J)
        ...
        DeprecationWarning: Use Jacobian_generic directly
        See https://github.com/sagemath/sage/issues/35467 for details.
        True

    ::

        sage: E = EllipticCurve('37a1')
        sage: is_Jacobian(E)
        False
    """
def Jacobian(C):
    """
    EXAMPLES::

        sage: from sage.schemes.jacobians.abstract_jacobian import Jacobian
        sage: P2.<x, y, z> = ProjectiveSpace(QQ, 2)
        sage: C = Curve(x^3 + y^3 + z^3)
        sage: Jacobian(C)
        Jacobian of Projective Plane Curve over Rational Field defined by x^3 + y^3 + z^3
    """

class Jacobian_generic(Scheme):
    """
    Base class for Jacobians of projective curves.

    The input must be a projective curve over a field.

    EXAMPLES::

        sage: from sage.schemes.jacobians.abstract_jacobian import Jacobian
        sage: P2.<x, y, z> = ProjectiveSpace(QQ, 2)
        sage: C = Curve(x^3 + y^3 + z^3)
        sage: J = Jacobian(C); J
        Jacobian of Projective Plane Curve over Rational Field defined by x^3 + y^3 + z^3
    """
    def __init__(self, C, category=None) -> None:
        '''
        Initialize.

        TESTS::

            sage: from sage.schemes.jacobians.abstract_jacobian import Jacobian_generic
            sage: P2.<x, y, z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x^3 + y^3 + z^3)
            sage: J = Jacobian_generic(C); J
            Jacobian of Projective Plane Curve over Rational Field defined by x^3 + y^3 + z^3
            sage: type(J)
            <class \'sage.schemes.jacobians.abstract_jacobian.Jacobian_generic_with_category\'>

        Note: this is an abstract parent, so we skip element tests::

            sage: TestSuite(J).run(skip =["_test_an_element",             ....:                         "_test_zero",             ....:                         "_test_elements",             ....:                         "_test_elements_eq_reflexive",             ....:                         "_test_elements_eq_symmetric",             ....:                         "_test_elements_eq_transitive",             ....:                         "_test_additive_associativity",             ....:                         "_test_elements_neq",             ....:                         "_test_some_elements"])

        ::

            sage: Jacobian_generic(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: Argument (=Integer Ring) must be a scheme.
            sage: Jacobian_generic(P2)
            Traceback (most recent call last):
            ...
            ValueError: C (=Projective Space of dimension 2 over Rational Field)
            must have dimension 1.

        ::

            sage: P2.<x, y, z> = ProjectiveSpace(Zmod(6), 2)
            sage: C = Curve(x + y + z, P2)
            sage: Jacobian_generic(C)
            Traceback (most recent call last):
            ...
            TypeError: C (=Projective Plane Curve over Ring of integers modulo 6
            defined by x + y + z) must be defined over a field.
        '''
    def __richcmp__(self, J, op):
        """
        Compare the Jacobian ``self`` to `J`.  If `J` is a Jacobian, then
        ``self`` and `J` are equal if and only if their curves are equal.

        EXAMPLES::

            sage: from sage.schemes.jacobians.abstract_jacobian import Jacobian
            sage: P2.<x, y, z> = ProjectiveSpace(QQ, 2)
            sage: J1 = Jacobian(Curve(x^3 + y^3 + z^3))
            sage: J1 == J1
            True
            sage: J1 == P2
            False
            sage: J1 != P2
            True
            sage: J2 = Jacobian(Curve(x + y + z))
            sage: J1 == J2
            False
            sage: J1 != J2
            True
        """
    def curve(self):
        """
        Return the curve of which ``self`` is the Jacobian.

        EXAMPLES::

            sage: from sage.schemes.jacobians.abstract_jacobian import Jacobian
            sage: P2.<x, y, z> = ProjectiveSpace(QQ, 2)
            sage: J = Jacobian(Curve(x^3 + y^3 + z^3))
            sage: J.curve()
            Projective Plane Curve over Rational Field defined by x^3 + y^3 + z^3
        """
    base_curve = curve
    def change_ring(self, R):
        """
        Return the Jacobian over the ring `R`.

        INPUT:

        - ``R`` -- a field; the new base ring

        OUTPUT: the Jacobian over the ring `R`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3 - 10*x + 9)
            sage: Jac = H.jacobian();   Jac
            Jacobian of Hyperelliptic Curve over Rational Field
             defined by y^2 = x^3 - 10*x + 9
            sage: Jac.change_ring(RDF)
            Jacobian of Hyperelliptic Curve over Real Double Field
             defined by y^2 = x^3 - 10.0*x + 9.0
        """
    def base_extend(self, R):
        """
        Return the natural extension of ``self`` over `R`.

        INPUT:

        - ``R`` -- a field; the new base field

        OUTPUT: the Jacobian over the ring `R`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3 - 10*x + 9)
            sage: Jac = H.jacobian();   Jac
            Jacobian of Hyperelliptic Curve over Rational Field
             defined by y^2 = x^3 - 10*x + 9

            sage: # needs sage.rings.number_field
            sage: F.<a> = QQ.extension(x^2 + 1)
            sage: Jac.base_extend(F)
            Jacobian of Hyperelliptic Curve over Number Field in a with defining
             polynomial x^2 + 1 defined by y^2 = x^3 - 10*x + 9
        """
