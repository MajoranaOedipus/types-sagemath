from .ideal import FunctionFieldIdeal as FunctionFieldIdeal, IdealMonoid as IdealMonoid
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation, UniqueRepresentation as UniqueRepresentation

class FunctionFieldOrder_base(CachedRepresentation, Parent):
    """
    Base class for orders in function fields.

    INPUT:

    - ``field`` -- function field

    EXAMPLES::

        sage: F = FunctionField(QQ,'y')
        sage: F.maximal_order()
        Maximal order of Rational function field in y over Rational Field
    """
    def __init__(self, field, ideal_class=..., category=None) -> None:
        """
        Initialize.

        TESTS::

            sage: F = FunctionField(QQ,'y')
            sage: O = F.maximal_order()
            sage: TestSuite(O).run(skip='_test_gcd_vs_xgcd')
        """
    def is_field(self, proof: bool = True):
        """
        Return ``False`` since orders are never fields.

        EXAMPLES::

            sage: FunctionField(QQ,'y').maximal_order().is_field()
            False
        """
    def is_noetherian(self):
        """
        Return ``True`` since orders in function fields are Noetherian.

        EXAMPLES::

            sage: FunctionField(QQ,'y').maximal_order().is_noetherian()
            True
        """
    def function_field(self):
        """
        Return the function field to which the order belongs.

        EXAMPLES::

            sage: FunctionField(QQ,'y').maximal_order().function_field()
            Rational function field in y over Rational Field
        """
    fraction_field = function_field
    def is_subring(self, other):
        """
        Return ``True`` if the order is a subring of the other order.

        INPUT:

        - ``other`` -- order of the function field or the field itself

        EXAMPLES::

            sage: F = FunctionField(QQ,'y')
            sage: O = F.maximal_order()
            sage: O.is_subring(F)
            True
        """
    def ideal_monoid(self):
        """
        Return the monoid of ideals of the order.

        EXAMPLES::

            sage: FunctionField(QQ,'y').maximal_order().ideal_monoid()
            Monoid of ideals of Maximal order of Rational function field in y over Rational Field
        """

class FunctionFieldOrder(FunctionFieldOrder_base):
    """
    Base class for orders in function fields.
    """
class FunctionFieldOrderInfinite(FunctionFieldOrder_base):
    """
    Base class for infinite orders in function fields.
    """
class FunctionFieldMaximalOrder(UniqueRepresentation, FunctionFieldOrder):
    """
    Base class of maximal orders of function fields.
    """
class FunctionFieldMaximalOrderInfinite(FunctionFieldMaximalOrder, FunctionFieldOrderInfinite):
    """
    Base class of maximal infinite orders of function fields.
    """
