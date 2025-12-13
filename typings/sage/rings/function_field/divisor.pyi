from .place import PlaceSet as PlaceSet
from sage.arith.functions import lcm as lcm
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def divisor(field, data):
    """
    Construct a divisor from the data.

    INPUT:

    - ``field`` -- function field

    - ``data`` -- dictionary of place and multiplicity pairs

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); R.<t> = K[]
        sage: F.<y> = K.extension(t^3 - x^2*(x^2 + x + 1)^2)
        sage: from sage.rings.function_field.divisor import divisor
        sage: p, q, r = F.places()
        sage: divisor(F, {p: 1, q: 2, r: 3})
        Place (1/x, 1/x^2*y + 1)
         + 2*Place (x, (1/(x^3 + x^2 + x))*y^2)
         + 3*Place (x + 1, y + 1)
    """
def prime_divisor(field, place, m: int = 1):
    """
    Construct a prime divisor from the place.

    INPUT:

    - ``field`` -- function field

    - ``place`` -- place of the function field

    - ``m`` -- (default: 1) a positive integer; multiplicity at the place

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); R.<t> = K[]
        sage: F.<y> = K.extension(t^3 - x^2*(x^2 + x + 1)^2)
        sage: p = F.places()[0]
        sage: from sage.rings.function_field.divisor import prime_divisor
        sage: d = prime_divisor(F, p)
        sage: 3 * d == prime_divisor(F, p, 3)
        True
    """

class FunctionFieldDivisor(ModuleElement):
    """
    Divisors of function fields.

    INPUT:

    - ``parent`` -- divisor group

    - ``data`` -- dictionary of place and multiplicity pairs

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
        sage: f = x/(y + 1)
        sage: f.divisor()
        Place (1/x, 1/x^4*y^2 + 1/x^2*y + 1)
         + Place (1/x, 1/x^2*y + 1)
         + 3*Place (x, (1/(x^3 + x^2 + x))*y^2)
         - 6*Place (x + 1, y + 1)
    """
    def __init__(self, parent, data) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)
            sage: G = L.divisor_group()
            sage: TestSuite(G).run()
        """
    def __hash__(self):
        """
        Return the hash of the divisor.

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
    def dict(self):
        """
        Return the dictionary representing the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: f = x/(y + 1)
            sage: D = f.divisor()
            sage: D.dict()
            {Place (1/x, 1/x^3*y^2 + 1/x): -1,
             Place (1/x, 1/x^3*y^2 + 1/x^2*y + 1): 1,
             Place (x, y): 3,
             Place (x^3 + x + 1, y + 1): -1}
        """
    def list(self):
        """
        Return the list of place and multiplicity pairs of the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: f = x/(y + 1)
            sage: D = f.divisor()
            sage: D.list()
            [(Place (1/x, 1/x^3*y^2 + 1/x), -1),
             (Place (1/x, 1/x^3*y^2 + 1/x^2*y + 1), 1),
             (Place (x, y), 3),
             (Place (x^3 + x + 1, y + 1), -1)]
        """
    def support(self):
        """
        Return the support of the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: f = x/(y + 1)
            sage: D = f.divisor()
            sage: D.support()
            [Place (1/x, 1/x^3*y^2 + 1/x),
             Place (1/x, 1/x^3*y^2 + 1/x^2*y + 1),
             Place (x, y),
             Place (x^3 + x + 1, y + 1)]
        """
    def multiplicity(self, place):
        """
        Return the multiplicity of the divisor at the place.

        INPUT:

        - ``place`` -- place of a function field

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: p1,p2 = L.places()[:2]
            sage: D = 2*p1 - 3*p2
            sage: D.multiplicity(p1)
            2
            sage: D.multiplicity(p2)
            -3
        """
    valuation = multiplicity
    def is_effective(self):
        """
        Return ``True`` if this divisor has nonnegative multiplicity at all
        places.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: p1, p2 = L.places()[:2]
            sage: D = 2*p1 + 3*p2
            sage: D.is_effective()
            True
            sage: E = D - 4*p2
            sage: E.is_effective()
            False
        """
    def numerator(self):
        """
        Return the numerator part of the divisor.

        The numerator of a divisor is the positive part of the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: p1,p2 = L.places()[:2]
            sage: D = 2*p1 - 3*p2
            sage: D.numerator()
            2*Place (1/x, 1/x^3*y^2 + 1/x)
        """
    def denominator(self):
        """
        Return the denominator part of the divisor.

        The denominator of a divisor is the negative of the negative part of
        the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: p1,p2 = L.places()[:2]
            sage: D = 2*p1 - 3*p2
            sage: D.denominator()
            3*Place (1/x, 1/x^3*y^2 + 1/x^2*y + 1)
        """
    def degree(self):
        """
        Return the degree of the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: p1,p2 = L.places()[:2]
            sage: D = 2*p1 - 3*p2
            sage: D.degree()
            -1
        """
    def dimension(self):
        """
        Return the dimension of the Riemann-Roch space of the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x - 2)
            sage: P1 = I.divisor().support()[0]
            sage: Pinf = F.places_infinite()[0]
            sage: D = 3*Pinf + 2*P1
            sage: D.dimension()
            5
        """
    def basis_function_space(self):
        """
        Return a basis of the Riemann-Roch space of the divisor.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x - 2)
            sage: D = I.divisor()
            sage: D.basis_function_space()
            [x/(x + 3), 1/(x + 3)]
        """
    @cached_method
    def function_space(self):
        """
        Return the vector space of the Riemann-Roch space of the divisor.

        OUTPUT:

        - a vector space, an isomorphism from the vector space
          to the Riemann-Roch space, and its inverse.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2-x^3-1)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x - 2)
            sage: D = I.divisor()
            sage: V, from_V, to_V = D.function_space()
            sage: all(to_V(from_V(e)) == e for e in V)
            True
        """
    def basis_differential_space(self):
        """
        Return a basis of the space of differentials `\\Omega(D)`
        for the divisor `D`.

        EXAMPLES:

        We check the Riemann-Roch theorem::

            sage: K.<x>=FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y>=K.extension(Y^3 + x^3*Y + x)
            sage: d = 3*L.places()[0]
            sage: l = len(d.basis_function_space())
            sage: i = len(d.basis_differential_space())
            sage: l == d.degree() + 1 - L.genus() + i
            True
        """
    def differential_space(self):
        """
        Return the vector space of the differential space `\\Omega(D)` of the divisor `D`.

        OUTPUT:

        - a vector space isomorphic to `\\Omega(D)`

        - an isomorphism from the vector space to the differential space

        - the inverse of the isomorphism

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x - 2)
            sage: P1 = I.divisor().support()[0]
            sage: Pinf = F.places_infinite()[0]
            sage: D = -3*Pinf + P1
            sage: V, from_V, to_V = D.differential_space()
            sage: all(to_V(from_V(e)) == e for e in V)
            True
        """

class DivisorGroup(UniqueRepresentation, Parent):
    """
    Groups of divisors of function fields.

    INPUT:

    - ``field`` -- function field

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
        sage: F.<y> = K.extension(Y^2 - x^3 - 1)
        sage: F.divisor_group()
        Divisor group of Function field in y defined by y^2 + 4*x^3 + 4
    """
    Element = FunctionFieldDivisor
    def __init__(self, field) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 - x^3 - 1)
            sage: G = F.divisor_group()
            sage: TestSuite(G).run()
        """
    def function_field(self):
        """
        Return the function field to which the divisor group is attached.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(5)); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^2 - x^3 - 1)
            sage: G = F.divisor_group()
            sage: G.function_field()
            Function field in y defined by y^2 + 4*x^3 + 4
        """
