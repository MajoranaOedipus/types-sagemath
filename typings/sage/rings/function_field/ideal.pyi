from _typeshed import Incomplete
from sage.categories.monoids import Monoids as Monoids
from sage.combinat.subset import powerset as powerset
from sage.misc.latex import latex as latex
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.structure.element import Element as Element
from sage.structure.factorization import Factorization as Factorization
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FunctionFieldIdeal(Element):
    """
    Base class of fractional ideals of function fields.

    INPUT:

    - ``ring`` -- ring of the ideal

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(7))
        sage: O = K.equation_order()
        sage: O.ideal(x^3 + 1)
        Ideal (x^3 + 1) of Maximal order of Rational function field in x over Finite Field of size 7
    """
    def __init__(self, ring) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(7))
            sage: O = K.equation_order()
            sage: I = O.ideal(x^3 + 1)
            sage: TestSuite(I).run()
        """
    def gens_reduced(self):
        """
        Return reduced generators.

        For now, this method just looks at the generators and sees if any
        can be removed without changing the ideal.  It prefers principal
        representations (a single generator) over all others, and otherwise
        picks the generator set with the shortest print representation.

        This method is provided so that ideals in function fields have
        the method :meth:`gens_reduced()`, just like ideals of number
        fields. Sage linear algebra machinery sometimes requires this.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(7))
            sage: O = K.equation_order()
            sage: I = O.ideal(x, x^2, x^2 + x)
            sage: I.gens_reduced()
            (x,)
        """
    def ring(self):
        """
        Return the ring to which this ideal belongs.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(7))
            sage: O = K.equation_order()
            sage: I = O.ideal(x, x^2, x^2 + x)
            sage: I.ring()
            Maximal order of Rational function field in x over Finite Field of size 7
        """
    def base_ring(self):
        """
        Return the base ring of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(x^2 + 1)
            sage: I.base_ring()
            Order in Function field in y defined by y^2 - x^3 - 1
        """
    def place(self):
        """
        Return the place associated with this prime ideal.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^2 + x + 1)
            sage: I.place()
            Traceback (most recent call last):
            ...
            TypeError: not a prime ideal
            sage: I = O.ideal(x^3 + x + 1)
            sage: I.place()
            Place (x^3 + x + 1)

            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x + 1)/(x^3 + 1))
            sage: p = I.factor()[0][0]
            sage: p.place()
            Place (1/x)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 - x^2*(x^2+x+1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.place() for f,_ in I.factor()]
            [Place (x, (1/(x^3 + x^2 + x))*y^2),
             Place (x^2 + x + 1, (1/(x^3 + x^2 + x))*y^2)]

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: [f.place() for f,_ in I.factor()]
            [Place (x, x*y), Place (x + 1, x*y)]

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: K.<x> = FunctionField(GF(3^2)); R.<t> = PolynomialRing(K)
            sage: F.<y> = K.extension(t^3 + t^2 - x^4)
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(1/x)
            sage: I.factor()
            (Ideal (1/x^3*y^2) of Maximal infinite order of Function field
            in y defined by y^3 + y^2 + 2*x^4)^3
            sage: J = I.factor()[0][0]
            sage: J.is_prime()
            True
            sage: J.place()
            Place (1/x, 1/x^3*y^2)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(1/x)
            sage: I.factor()
            (Ideal (1/x*y) of Maximal infinite order of Function field in y
            defined by y^2 + y + (x^2 + 1)/x)^2
            sage: J = I.factor()[0][0]
            sage: J.is_prime()
            True
            sage: J.place()
            Place (1/x, 1/x*y)
        """
    def factor(self):
        """
        Return the factorization of this ideal.

        Subclass of this class should define :meth:`_factor` method that
        returns a list of prime ideal and multiplicity pairs.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x^3*(x + 1)^2)
            sage: I.factor()
            (Ideal (x) of Maximal order of Rational function field in x
            over Finite Field in z2 of size 2^2)^3 *
            (Ideal (x + 1) of Maximal order of Rational function field in x
            over Finite Field in z2 of size 2^2)^2

            sage: # needs sage.rings.finite_rings
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x + 1)/(x^3 + 1))
            sage: I.factor()
            (Ideal (1/x) of Maximal infinite order of Rational function field in x
            over Finite Field in z2 of size 2^2)^2

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<T> = PolynomialRing(K)
            sage: F.<y> = K.extension(T^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: I == I.factor().prod()
            True

            sage: # needs sage.rings.function_field
            sage: Oinf = F.maximal_order_infinite()
            sage: f= 1/x
            sage: I = Oinf.ideal(f)
            sage: I.factor()
            (Ideal ((1/(x^4 + x^3 + x^2))*y^2 + 1/x^2*y + 1) of Maximal infinite order
            of Function field in y defined by y^3 + x^6 + x^4 + x^2) *
            (Ideal ((1/(x^4 + x^3 + x^2))*y^2 + 1) of Maximal infinite order
            of Function field in y defined by y^3 + x^6 + x^4 + x^2)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: F.<y> = K.extension(Y^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: I == I.factor().prod()
            True

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: I == I.factor().prod()
            True
        """
    def divisor(self):
        """
        Return the divisor corresponding to the ideal.

        EXAMPLES::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x*(x + 1)^2/(x^2 + x + 1))
            sage: I.divisor()
            Place (x) + 2*Place (x + 1) - Place (x + z2) - Place (x + z2 + 1)

            sage: # needs sage.modules sage.rings.finite_rings
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x + 1)/(x^3 + 1))
            sage: I.divisor()
            2*Place (1/x)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<T> = PolynomialRing(K)
            sage: F.<y> = K.extension(T^3 - x^2*(x^2 + x + 1)^2)
            sage: O = F.maximal_order()
            sage: I = O.ideal(y)
            sage: I.divisor()
            2*Place (x, (1/(x^3 + x^2 + x))*y^2)
             + 2*Place (x^2 + x + 1, (1/(x^3 + x^2 + x))*y^2)

            sage: # needs sage.rings.function_field
            sage: Oinf = F.maximal_order_infinite()
            sage: I = Oinf.ideal(y)
            sage: I.divisor()
            -2*Place (1/x, 1/x^4*y^2 + 1/x^2*y + 1)
             - 2*Place (1/x, 1/x^2*y + 1)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: I.divisor()
            - Place (x, x*y)
             + 2*Place (x + 1, x*y)

            sage: # needs sage.rings.function_field
            sage: Oinf = L.maximal_order_infinite()
            sage: I = Oinf.ideal(y)
            sage: I.divisor()
            - Place (1/x, 1/x*y)
        """
    def divisor_of_zeros(self):
        """
        Return the divisor of zeros corresponding to the ideal.

        EXAMPLES::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x*(x + 1)^2/(x^2 + x + 1))
            sage: I.divisor_of_zeros()
            Place (x) + 2*Place (x + 1)

            sage: # needs sage.modules
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x + 1)/(x^3 + 1))
            sage: I.divisor_of_zeros()
            2*Place (1/x)

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: I.divisor_of_zeros()
            2*Place (x + 1, x*y)
        """
    def divisor_of_poles(self):
        """
        Return the divisor of poles corresponding to the ideal.

        EXAMPLES::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4))
            sage: O = K.maximal_order()
            sage: I = O.ideal(x*(x + 1)^2/(x^2 + x + 1))
            sage: I.divisor_of_poles()
            Place (x + z2) + Place (x + z2 + 1)

            sage: # needs sage.modules
            sage: K.<x> = FunctionField(GF(2))
            sage: Oinf = K.maximal_order_infinite()
            sage: I = Oinf.ideal((x + 1)/(x^3 + 1))
            sage: I.divisor_of_poles()
            0

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: O = L.maximal_order()
            sage: I = O.ideal(y)
            sage: I.divisor_of_poles()
            Place (x, x*y)
        """

class FunctionFieldIdeal_module(FunctionFieldIdeal, Ideal_generic):
    """
    A fractional ideal specified by a finitely generated module over
    the integers of the base field.

    INPUT:

    - ``ring`` -- an order in a function field

    - ``module`` -- a module of the order

    EXAMPLES:

    An ideal in an extension of a rational function field::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x^3 - 1)
        sage: O = L.equation_order()
        sage: I = O.ideal(y)
        sage: I
        Ideal (x^3 + 1, -y) of Order in Function field in y defined by y^2 - x^3 - 1
        sage: I^2
        Ideal (x^3 + 1, (-x^3 - 1)*y) of Order in Function field in y defined by y^2 - x^3 - 1
    """
    def __init__(self, ring, module) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(y)
            sage: TestSuite(I).run()
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is in this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(y); I
            Ideal (x^3 + 1, -y) of Order in Function field in y defined by y^2 - x^3 - 1
            sage: y in I
            True
            sage: y/x in I
            False
            sage: y^2 - 2 in I
            False
        """
    def __hash__(self):
        """
        Return the hash of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(y)
            sage: d = {I: 1}  # indirect doctest
        """
    def module(self):
        """
        Return the module over the maximal order of the base field that
        underlies this ideal.

        The formation of the module is compatible with the vector
        space corresponding to the function field.

        OUTPUT: a module over the maximal order of the base field of the ideal

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order();  O
            Order in Function field in y defined by y^2 - x^3 - 1
            sage: I = O.ideal(x^2 + 1)
            sage: I.gens()
            (x^2 + 1, (x^2 + 1)*y)
            sage: I.module()
            Free module of degree 2 and rank 2 over Maximal order of Rational function field in x over Rational Field
            Echelon basis matrix:
            [x^2 + 1       0]
            [      0 x^2 + 1]
            sage: V, from_V, to_V = L.vector_space(); V
            Vector space of dimension 2 over Rational function field in x over Rational Field
            sage: I.module().is_submodule(V)
            True
        """
    def gens(self) -> tuple:
        """
        Return a set of generators of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(x^2 + 1)
            sage: I.gens()
            (x^2 + 1, (x^2 + 1)*y)
        """
    def gen(self, i):
        """
        Return the ``i``-th generator in the current basis of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(x^2 + 1)
            sage: I.gen(1)
            (x^2 + 1)*y
        """
    def ngens(self):
        """
        Return the number of generators in the basis.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(x^2 + 1)
            sage: I.ngens()
            2
        """
    def intersection(self, other):
        """
        Return the intersection of this ideal and ``other``.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(y^3); J = O.ideal(y^2)
            sage: Z = I.intersection(J); Z
            Ideal (x^6 + 2*x^3 + 1, (-x^3 - 1)*y) of Order in Function field in y defined by y^2 - x^3 - 1
            sage: y^2 in Z
            False
            sage: y^3 in Z
            True
        """
    def __invert__(self):
        """
        Return the inverse of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(y)
            sage: ~I
            Ideal (-1, (1/(x^3 + 1))*y) of Order in Function field in y defined by y^2 - x^3 - 1
            sage: I^-1
            Ideal (-1, (1/(x^3 + 1))*y) of Order in Function field in y defined by y^2 - x^3 - 1
            sage: ~I * I
            Ideal (1) of Order in Function field in y defined by y^2 - x^3 - 1
        """

class FunctionFieldIdealInfinite(FunctionFieldIdeal):
    """
    Base class of ideals of maximal infinite orders
    """

class FunctionFieldIdealInfinite_module(FunctionFieldIdealInfinite, Ideal_generic):
    """
    A fractional ideal specified by a finitely generated module over
    the integers of the base field.

    INPUT:

    - ``ring`` -- order in a function field

    - ``module`` -- module

    EXAMPLES::

        sage: # needs sage.rings.function_field
        sage: K.<x> = FunctionField(QQ); R.<y> = K[]
        sage: L.<y> = K.extension(y^2 - x^3 - 1)
        sage: O = L.equation_order()
        sage: O.ideal(y)
        Ideal (x^3 + 1, -y) of Order in Function field in y defined by y^2 - x^3 - 1
    """
    def __init__(self, ring, module) -> None:
        """
        Initialize.

        TESTS::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(QQ); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal(y)
            sage: TestSuite(I).run()
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is in this ideal.

        INPUT:

        - ``x`` -- element of the function field

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal_with_gens_over_base([1, y]);  I
            Ideal (1) of Order in Function field in y defined by y^2 + 6*x^3 + 6
            sage: y in I
            True
            sage: y/x in I
            False
            sage: y^2 - 2 in I
            True
        """
    def __hash__(self):
        """
        Return the hash of this ideal.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal_with_gens_over_base([1, y])
            sage: d = {I: 2}  # indirect doctest
        """
    def __eq__(self, other):
        """
        Test equality of this ideal with the ``other`` ideal.

        INPUT:

        - ``other`` -- ideal

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(7)); R.<y> = K[]
            sage: L.<y> = K.extension(y^2 - x^3 - 1)
            sage: O = L.equation_order()
            sage: I = O.ideal_with_gens_over_base([1, y])
            sage: I == I + I  # indirect doctest
            True
        """
    def module(self):
        """
        Return the module over the maximal order of the base field that
        underlies this ideal.

        The formation of the module is compatible with the vector
        space corresponding to the function field.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(7))
            sage: O = K.maximal_order(); O
            Maximal order of Rational function field in x over Finite Field of size 7
            sage: K.polynomial_ring()
            Univariate Polynomial Ring in x over
             Rational function field in x over Finite Field of size 7
            sage: I = O.ideal([x^2 + 1, x*(x^2+1)])
            sage: I.gens()
            (x^2 + 1,)
            sage: I.module()                                                            # needs sage.modules
            Free module of degree 1 and rank 1 over
             Maximal order of Rational function field in x over Finite Field of size 7
            Echelon basis matrix:
            [x^2 + 1]
            sage: V, from_V, to_V = K.vector_space(); V                                 # needs sage.modules
            Vector space of dimension 1 over
             Rational function field in x over Finite Field of size 7
            sage: I.module().is_submodule(V)                                            # needs sage.modules
            True
        """

class IdealMonoid(UniqueRepresentation, Parent):
    """
    The monoid of ideals in orders of function fields.

    INPUT:

    - ``R`` -- order

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2))
        sage: O = K.maximal_order()
        sage: M = O.ideal_monoid(); M
        Monoid of ideals of Maximal order of Rational function field in x over Finite Field of size 2
    """
    Element: Incomplete
    def __init__(self, R) -> None:
        """
        Initialize the ideal monoid.

        TESTS::

            sage: K.<x> = FunctionField(GF(2))
            sage: O = K.maximal_order()
            sage: M = O.ideal_monoid()
            sage: TestSuite(M).run()
        """
    def ring(self):
        """
        Return the ring of which this is the ideal monoid.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2))
            sage: O = K.maximal_order()
            sage: M = O.ideal_monoid(); M.ring() is O
            True
        """
