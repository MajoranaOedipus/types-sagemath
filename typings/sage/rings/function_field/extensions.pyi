from .constructor import FunctionField as FunctionField
from sage.rings.ring_extension import RingExtension_generic as RingExtension_generic

class FunctionFieldExtension(RingExtension_generic):
    """
    Abstract base class of function field extensions.
    """

class ConstantFieldExtension(FunctionFieldExtension):
    """
    Constant field extension.

    INPUT:

    - ``F`` -- a function field whose constant field is `k`

    - ``k_ext`` -- an extension of `k`
    """
    def __init__(self, F, k_ext) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); R.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: E = F.extension_constant_field(GF(2^3))
            sage: TestSuite(E).run(skip=['_test_elements', '_test_pickling'])
        """
    def top(self):
        """
        Return the top function field of this extension.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); R.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: E = F.extension_constant_field(GF(2^3))
            sage: E.top()
            Function field in y defined by y^3 + x^6 + x^4 + x^2
        """
    def defining_morphism(self):
        """
        Return the defining morphism of this extension.

        This is the morphism from the base to the top.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); R.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: E = F.extension_constant_field(GF(2^3))
            sage: E.defining_morphism()
            Function Field morphism:
              From: Function field in y defined by y^3 + x^6 + x^4 + x^2
              To:   Function field in y defined by y^3 + x^6 + x^4 + x^2
              Defn: y |--> y
                    x |--> x
                    1 |--> 1
        """
    def conorm_place(self, p):
        """
        Return the conorm of the place `p` in this extension.

        INPUT:

        - ``p`` -- place of the base function field

        OUTPUT: divisor of the top function field

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); R.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: E = F.extension_constant_field(GF(2^3))
            sage: p = F.get_place(3)
            sage: d = E.conorm_place(p)
            sage: [pl.degree() for pl in d.support()]
            [1, 1, 1]
            sage: p = F.get_place(2)
            sage: d = E.conorm_place(p)
            sage: [pl.degree() for pl in d.support()]
            [2]
        """
    def conorm_divisor(self, d):
        """
        Return the conorm of the divisor ``d`` in this extension.

        INPUT:

        - ``d`` -- divisor of the base function field

        OUTPUT: a divisor of the top function field

        EXAMPLES::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); R.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: E = F.extension_constant_field(GF(2^3))
            sage: p1 = F.get_place(3)
            sage: p2 = F.get_place(2)
            sage: c = E.conorm_divisor(2*p1 + 3*p2)
            sage: c1 = E.conorm_place(p1)
            sage: c2 = E.conorm_place(p2)
            sage: c == 2*c1 + 3*c2
            True
        """
