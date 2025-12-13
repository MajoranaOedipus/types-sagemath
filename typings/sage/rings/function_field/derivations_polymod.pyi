from .derivations import FunctionFieldDerivation as FunctionFieldDerivation
from sage.arith.misc import binomial as binomial
from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.categories.sets_cat import Sets as Sets
from sage.rings.derivation import RingDerivationWithoutTwist as RingDerivationWithoutTwist

class FunctionFieldDerivation_separable(FunctionFieldDerivation):
    """
    Derivations of separable extensions.

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ)
        sage: R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x)
        sage: L.derivation()
        d/dx
    """
    def __init__(self, parent, d) -> None:
        """
        Initialize a derivation.

        INPUT:

        - ``parent`` -- the parent of this derivation

        - ``d`` -- a variable name or a derivation over
          the base field (or something capable to create
          such a derivation)

        EXAMPLES::

            sage: K.<x> = FunctionField(QQ)
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: d = L.derivation()
            sage: TestSuite(d).run()

            sage: L.derivation(y)  # d/dy
            2*y*d/dx

            sage: dK = K.derivation([x]); dK
            x*d/dx
            sage: L.derivation(dK)
            x*d/dx
        """

class FunctionFieldDerivation_inseparable(FunctionFieldDerivation):
    def __init__(self, parent, u=None) -> None:
        """
        Initialize this derivation.

        INPUT:

        - ``parent`` -- the parent of this derivation

        - ``u`` -- a parameter describing the derivation

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x)
            sage: d = L.derivation()

        This also works for iterated non-monic extensions::

            sage: K.<x> = FunctionField(GF(2))
            sage: R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - 1/x)
            sage: R.<z> = L[]
            sage: M.<z> = L.extension(z^2*y - x^3)
            sage: M.derivation()
            d/dz

        We can also create a multiple of the canonical derivation::

            sage: M.derivation([x])
            x*d/dz
        """

class FunctionFieldHigherDerivation(Map):
    """
    Base class of higher derivations on function fields.

    INPUT:

    - ``field`` -- function field on which the derivation operates

    EXAMPLES::

        sage: F.<x> = FunctionField(GF(2))
        sage: F.higher_derivation()
        Higher derivation map:
          From: Rational function field in x over Finite Field of size 2
          To:   Rational function field in x over Finite Field of size 2
    """
    def __init__(self, field) -> None:
        """
        Initialize.

        TESTS::

            sage: F.<x> = FunctionField(GF(4))                                                      # needs sage.rings.finite_rings
            sage: h = F.higher_derivation()                                                         # needs sage.rings.finite_rings
            sage: TestSuite(h).run(skip='_test_category')                                           # needs sage.rings.finite_rings
        """
    def __eq__(self, other) -> bool:
        """
        Test if ``self`` equals ``other``.

        TESTS::

            sage: F.<x> = FunctionField(GF(2))
            sage: h = F.higher_derivation()
            sage: loads(dumps(h)) == h
            True
        """

class RationalFunctionFieldHigherDerivation_global(FunctionFieldHigherDerivation):
    """
    Higher derivations of rational function fields over finite fields.

    INPUT:

    - ``field`` -- function field on which the derivation operates

    EXAMPLES::

        sage: F.<x> = FunctionField(GF(2))
        sage: h = F.higher_derivation()
        sage: h
        Higher derivation map:
          From: Rational function field in x over Finite Field of size 2
          To:   Rational function field in x over Finite Field of size 2
        sage: h(x^2, 2)
        1
    """
    def __init__(self, field) -> None:
        """
        Initialize.

        TESTS::

            sage: F.<x> = FunctionField(GF(2))
            sage: h = F.higher_derivation()
            sage: TestSuite(h).run(skip='_test_category')
        """

class FunctionFieldHigherDerivation_global(FunctionFieldHigherDerivation):
    """
    Higher derivations of global function fields.

    INPUT:

    - ``field`` -- function field on which the derivation operates

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
        sage: h = L.higher_derivation()
        sage: h
        Higher derivation map:
          From: Function field in y defined by y^3 + x^3*y + x
          To:   Function field in y defined by y^3 + x^3*y + x
        sage: h(y^2, 2)
        ((x^7 + 1)/x^2)*y^2 + x^3*y
    """
    def __init__(self, field) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
            sage: h = L.higher_derivation()
            sage: TestSuite(h).run(skip=['_test_category'])
        """

class FunctionFieldHigherDerivation_char_zero(FunctionFieldHigherDerivation):
    """
    Higher derivations of function fields of characteristic zero.

    INPUT:

    - ``field`` -- function field on which the derivation operates

    EXAMPLES::

        sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
        sage: h = L.higher_derivation()
        sage: h
        Higher derivation map:
          From: Function field in y defined by y^3 + x^3*y + x
          To:   Function field in y defined by y^3 + x^3*y + x
        sage: h(y,1) == -(3*x^2*y+1)/(3*y^2+x^3)
        True
        sage: h(y^2,1) == -2*y*(3*x^2*y+1)/(3*y^2+x^3)
        True
        sage: e = L.random_element()
        sage: h(h(e,1),1) == 2*h(e,2)
        True
        sage: h(h(h(e,1),1),1) == 3*2*h(e,3)
        True
    """
    def __init__(self, field) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
            sage: h = L.higher_derivation()
            sage: TestSuite(h).run(skip=['_test_category'])
        """
