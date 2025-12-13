from sage.arith.misc import binomial as binomial, factorial as factorial
from sage.categories.algebras import Algebras as Algebras
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.data_structures.blas_dict import linear_combination as linear_combination
from sage.matrix.constructor import matrix as matrix
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IntegerValuedPolynomialRing(UniqueRepresentation, Parent):
    """
    The integer-valued polynomial ring over a base ring `R`.

    Integer-valued polynomial rings are commutative and associative
    algebras, with a basis indexed by nonnegative integers.

    There are two natural bases, made of the sequence
    `\\binom{x}{n}` for `n \\geq 0` (the *binomial basis*) and of
    the other sequence `\\binom{x+n}{n}` for `n \\geq 0` (the *shifted basis*).

    These two bases are available as follows::

        sage: B = IntegerValuedPolynomialRing(QQ).Binomial()
        sage: S = IntegerValuedPolynomialRing(QQ).Shifted()

    or by using the shortcuts::

        sage: B = IntegerValuedPolynomialRing(QQ).B()
        sage: S = IntegerValuedPolynomialRing(QQ).S()

    There is a conversion formula between the two bases:

    .. MATH::

        \\binom{x}{i} = \\sum_{k=0}^{i} (-1)^{i-k} \\binom{i}{k} \\binom{x+k}{k}

    with inverse:

    .. MATH::

        \\binom{x+i}{i} = \\sum_{k=0}^{i} \\binom{i}{k} \\binom{x}{k}.

    REFERENCES:

    - :wikipedia:`Integer-valued polynomial`

    TESTS::

        sage: IntegerValuedPolynomialRing(24)
        Traceback (most recent call last):
        ...
        TypeError: argument R must be a commutative ring
    """
    def __init__(self, R) -> None:
        """
        TESTS::

            sage: IV = IntegerValuedPolynomialRing(ZZ)
            sage: TestSuite(IV).run()
        """
    def a_realization(self):
        """
        Return a default realization.

        The Binomial realization is chosen.

        EXAMPLES::

            sage: IntegerValuedPolynomialRing(QQ).a_realization()
            Integer-Valued Polynomial Ring over Rational Field
            in the binomial basis
        """
    class Bases(Category_realization_of_parent):
        def super_categories(self) -> list:
            """
            Return the super-categories of ``self``.

            EXAMPLES::

                sage: A = IntegerValuedPolynomialRing(QQ); A
                Integer-Valued Polynomial Ring over Rational Field
                sage: C = A.Bases(); C
                Category of bases of Integer-Valued Polynomial Ring
                over Rational Field
                sage: C.super_categories()
                [Category of realizations of Integer-Valued Polynomial Ring
                 over Rational Field,
                 Join of Category of algebras with basis over Rational Field and
                 Category of filtered algebras over Rational Field and
                 Category of commutative algebras over Rational Field and
                 Category of realizations of unital magmas]
            """
        class ParentMethods:
            @cached_method
            def one_basis(self):
                """
                Return the number 0, which index the unit of this algebra.

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(QQ).S()
                    sage: A.one_basis()
                    0
                    sage: A.one()
                    S[0]
                """
            def degree_on_basis(self, m):
                """
                Return the degree of the basis element indexed by ``m``.

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(QQ).S()
                    sage: A.degree_on_basis(4)
                    4
                """
            def from_polynomial(self, p):
                """
                Convert a polynomial into the ring of integer-valued polynomials.

                This raises a :exc:`ValueError` if this is not possible.

                INPUT:

                - ``p`` -- a polynomial in one variable

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(ZZ).S()
                    sage: S = A.basis()
                    sage: S[5].polynomial()
                    1/120*x^5 + 1/8*x^4 + 17/24*x^3 + 15/8*x^2 + 137/60*x + 1
                    sage: A.from_polynomial(_)
                    S[5]
                    sage: x = polygen(QQ, 'x')
                    sage: A.from_polynomial(x)
                    -S[0] + S[1]

                    sage: A = IntegerValuedPolynomialRing(ZZ).B()
                    sage: B = A.basis()
                    sage: B[5].polynomial()
                    1/120*x^5 - 1/12*x^4 + 7/24*x^3 - 5/12*x^2 + 1/5*x
                    sage: A.from_polynomial(_)
                    B[5]
                    sage: x = polygen(QQ, 'x')
                    sage: A.from_polynomial(x)
                    B[1]

                TESTS::

                    sage: x = polygen(QQ,'x')
                    sage: A.from_polynomial(x+1/3)
                    Traceback (most recent call last):
                    ...
                    ValueError: not a polynomial with integer values: 1/3

                    sage: t = polygen(ZZ,'t')
                    sage: B = IntegerValuedPolynomialRing(QQ).B()
                    sage: B.from_polynomial(t+1)
                    B[0] + B[1]
                """
            def gen(self, i: int = 0):
                """
                Return the generator of this algebra.

                The optional argument is ignored.

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).B()
                    sage: F.gen()
                    B[1]
                """
            @cached_method
            def algebra_generators(self):
                """
                Return the generators of this algebra.

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(ZZ).S(); A
                    Integer-Valued Polynomial Ring over Integer Ring
                    in the shifted basis
                    sage: A.algebra_generators()
                    Family (S[1],)
                """
            gens = algebra_generators
        class ElementMethods:
            def __call__(self, v):
                """
                Return the evaluation at some value ``v``.

                EXAMPLES::

                     sage: F = IntegerValuedPolynomialRing(ZZ).S()
                     sage: B = F.gen()
                     sage: f = B**2+4*B+6
                     sage: f(1/3)
                     118/9

                     sage: F = IntegerValuedPolynomialRing(ZZ).B()
                     sage: B = F.gen()
                     sage: f = B**2+4*B+6
                     sage: f(1/3)
                     67/9
                """
            def polynomial(self):
                """
                Convert to a polynomial in `x`.

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).S()
                    sage: B = F.gen()
                    sage: (B+1).polynomial()
                    x + 2

                    sage: F = IntegerValuedPolynomialRing(ZZ).B()
                    sage: B = F.gen()
                    sage: (B+1).polynomial()
                    x + 1

                TESTS::

                    sage: F.zero().polynomial().parent()
                    Univariate Polynomial Ring in x over Rational Field
                """
            def shift(self, j: int = 1):
                """
                Shift all indices by `j`.

                INPUT:

                - ``j`` -- integer (default: 1)

                In the binomial basis, the shift by 1 corresponds to
                a summation operator from `0` to `x`.

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).B()
                    sage: B = F.gen()
                    sage: (B+1).shift()
                    B[1] + B[2]
                    sage: (B+1).shift(3)
                    B[3] + B[4]
                """
            def sum_of_coefficients(self):
                """
                Return the sum of coefficients.

                In the shifted basis, this is the evaluation at `x=0`.

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).S()
                    sage: B = F.basis()
                    sage: (B[2]*B[4]).sum_of_coefficients()
                    1

                TESTS::

                    sage: (0*B[2]).sum_of_coefficients().parent()
                    Integer Ring
                """
            def content(self):
                """
                Return the content of ``self``.

                This is the gcd of the coefficients.

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).S()
                    sage: B = F.basis()
                    sage: (3*B[4]+6*B[7]).content()
                    3

                TESTS::

                    sage: (0*B[2]).content()
                    0
                """
    class Shifted(CombinatorialFreeModule, BindableClass):
        """
        The integer-valued polynomial ring in the shifted basis.

        The basis used here is given by `S[i] = \\binom{i+x}{i}` for `i \\in \\NN`.

        Assuming `n_1 \\leq n_2`, the product of two monomials `S[n_1] \\cdot S[n_2]`
        is given by the sum

        .. MATH::

            \\sum_{k=0}^{n_1} (-1)^k \\binom{n_1}{k}\\binom{n_1+n_2-k}{n_1} S[n_1 + n_2 - k].

        EXAMPLES::

            sage: F = IntegerValuedPolynomialRing(QQ).S(); F
            Integer-Valued Polynomial Ring over Rational Field
            in the shifted basis

            sage: F.gen()
            S[1]

            sage: S = IntegerValuedPolynomialRing(ZZ).S(); S
            Integer-Valued Polynomial Ring over Integer Ring
            in the shifted basis
            sage: S.base_ring()
            Integer Ring

            sage: G = IntegerValuedPolynomialRing(S).S(); G
            Integer-Valued Polynomial Ring over Integer-Valued Polynomial
            Ring over Integer Ring in the shifted basis in the shifted basis
            sage: G.base_ring()
            Integer-Valued Polynomial Ring over Integer Ring
            in the shifted basis

        Integer-valued polynomial rings commute with their base ring::

            sage: K = IntegerValuedPolynomialRing(QQ).S()
            sage: a = K.gen()
            sage: K.is_commutative()
            True
            sage: L = IntegerValuedPolynomialRing(K).S()
            sage: c = L.gen()
            sage: L.is_commutative()
            True
            sage: s = a * c^3; s
            S[1]*S[1] + (-6*S[1])*S[2] + 6*S[1]*S[3]
            sage: parent(s)
            Integer-Valued Polynomial Ring over Integer-Valued Polynomial
            Ring over Rational Field in the shifted basis in the shifted basis

        Integer-valued polynomial rings are commutative::

            sage: c^3 * a == c * a * c * c
            True

        We can also manipulate elements in the basis and
        coerce elements from our base field::

            sage: F = IntegerValuedPolynomialRing(QQ).S()
            sage: S = F.basis()
            sage: S[2] * S[3]
            3*S[3] - 12*S[4] + 10*S[5]
            sage: 1 - S[2] * S[2] / 2
            S[0] - 1/2*S[2] + 3*S[3] - 3*S[4]
        """
        def __init__(self, A) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: F = IntegerValuedPolynomialRing(QQ).S(); F
                Integer-Valued Polynomial Ring over Rational Field
                in the shifted basis
                sage: TestSuite(F).run()
            """
        def product_on_basis(self, n1, n2):
            """
            Return the product of basis elements ``n1`` and ``n2``.

            INPUT:

            - ``n1``, ``n2`` -- integers

            EXAMPLES::

                sage: A = IntegerValuedPolynomialRing(QQ).S()
                sage: A.product_on_basis(0, 1)
                S[1]
                sage: A.product_on_basis(1, 2)
                -2*S[2] + 3*S[3]
            """
        def from_h_vector(self, h):
            """
            Convert from some `h`-vector.

            INPUT:

            - ``h`` -- tuple or vector

            .. SEEALSO:: :meth:`Element.h_vector`

            EXAMPLES::

                sage: A = IntegerValuedPolynomialRing(ZZ).S()
                sage: S = A.basis()
                sage: ex = S[2]+S[4]
                sage: A.from_h_vector(ex.h_vector())
                S[2] + S[4]
            """
        class Element(CombinatorialFreeModule.Element):
            def umbra(self):
                """
                Return the Bernoulli umbra.

                This is the derivative at `-1` of the shift by one.

                This is related to Bernoulli numbers.

                .. SEEALSO:: :meth:`derivative_at_minus_one`

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).S()
                    sage: B = F.gen()
                    sage: (B+1).umbra()
                    3/2

                TESTS::

                    sage: [(B**n).umbra() for n in range(1, 11)]
                    [1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66]
                """
            def delta(self):
                """
                Return the image by the difference operator `\\Delta`.

                The operator `\\Delta` is defined on polynomials by

                .. MATH::

                    f \\mapsto f(x+1)-f(x).

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).S()
                    sage: S = F.basis()
                    sage: S[5].delta()
                    S[0] + S[1] + S[2] + S[3] + S[4]
                """
            def variable_shift(self, k: int = 1):
                """
                Return the image by the shift of variables.

                On polynomials, the action is the shift
                on variables `x \\mapsto x + k`.

                INPUT:

                - ``k`` -- integer (default: 1)

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(ZZ).S()
                    sage: S = A.basis()
                    sage: S[5].variable_shift()
                    S[0] + S[1] + S[2] + S[3] + S[4] + S[5]

                    sage: S[5].variable_shift(-1)
                    -S[4] + S[5]

                TESTS::

                    sage: S[5].variable_shift(0)
                    S[5]
                    sage: S[5].variable_shift().variable_shift(-1)
                    S[5]
                    sage: S[5].variable_shift(2).variable_shift(-2)
                    S[5]
                """
            def derivative_at_minus_one(self):
                """
                Return the derivative at `-1`.

                This is sometimes useful when `-1` is a root.

                .. SEEALSO:: :meth:`umbra`

                EXAMPLES::

                    sage: F = IntegerValuedPolynomialRing(ZZ).S()
                    sage: B = F.gen()
                    sage: (B+1).derivative_at_minus_one()
                    1
                """
            def h_vector(self):
                """
                Return the numerator of the generating series of values.

                If ``self`` is an Ehrhart polynomial, this is the `h`-vector.

                .. SEEALSO:: :meth:`h_polynomial`, :meth:`fraction`

                EXAMPLES::

                    sage: x = polygen(QQ,'x')
                    sage: A = IntegerValuedPolynomialRing(ZZ).S()
                    sage: ex = A.from_polynomial((1+x)**3)
                    sage: ex.h_vector()
                    (0, 1, 4, 1)
                """
            def h_polynomial(self):
                """
                Return the `h`-vector as a polynomial.

                .. SEEALSO:: :meth:`h_vector`, :meth:`fraction`

                EXAMPLES::

                    sage: x = polygen(QQ,'x')
                    sage: A = IntegerValuedPolynomialRing(ZZ).S()
                    sage: ex = A.from_polynomial((1+x)**3)
                    sage: ex.h_polynomial()
                    z^2 + 4*z + 1
                """
            def fraction(self):
                """
                Return the generating series of values as a fraction.

                In the case of Ehrhart polynomials, this is known as
                the Ehrhart series.

                .. SEEALSO:: :meth:`h_vector`, :meth:`h_polynomial`

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(ZZ).S()
                    sage: ex = A.monomial(4)
                    sage: f = ex.fraction();f
                    1/(-t^5 + 5*t^4 - 10*t^3 + 10*t^2 - 5*t + 1)

                    sage: F = LazyPowerSeriesRing(QQ, 't')
                    sage: F(f)
                    1 + 5*t + 15*t^2 + 35*t^3 + 70*t^4 + 126*t^5 + 210*t^6 + O(t^7)

                    sage: poly = ex.polynomial()
                    sage: [poly(i) for i in range(6)]
                    [1, 5, 15, 35, 70, 126]

                    sage: y = polygen(QQ, 'y')
                    sage: penta = A.from_polynomial(7/2*y^2 + 7/2*y + 1)
                    sage: penta.fraction()
                    (t^2 + 5*t + 1)/(-t^3 + 3*t^2 - 3*t + 1)

                TESTS::

                    sage: A.zero().fraction()
                    0
                    sage: A.zero().fraction().parent()
                    Fraction Field of Univariate Polynomial Ring in t over Integer Ring
                """
    S = Shifted
    class Binomial(CombinatorialFreeModule, BindableClass):
        """
        The integer-valued polynomial ring in the binomial basis.

        The basis used here is given by `B[i] = \\binom{x}{i}` for `i \\in \\NN`.

        Assuming `n_1 \\leq n_2`, the product of two monomials `B[n_1] \\cdot B[n_2]`
        is given by the sum

        .. MATH::

            \\sum_{k=0}^{n_1} \\binom{n_1}{k}\\binom{n_1+n_2-k}{n_1} B[n_1 + n_2 - k].

        The product of two monomials is therefore a positive linear combination
        of monomials.

        EXAMPLES::

            sage: F = IntegerValuedPolynomialRing(QQ).B(); F
            Integer-Valued Polynomial Ring over Rational Field
            in the binomial basis

            sage: F.gen()
            B[1]

            sage: S = IntegerValuedPolynomialRing(ZZ).B(); S
            Integer-Valued Polynomial Ring over Integer Ring
            in the binomial basis
            sage: S.base_ring()
            Integer Ring

            sage: G = IntegerValuedPolynomialRing(S).B(); G
            Integer-Valued Polynomial Ring over Integer-Valued Polynomial Ring
            over Integer Ring in the binomial basis in the binomial basis
            sage: G.base_ring()
            Integer-Valued Polynomial Ring over Integer Ring
            in the binomial basis

        Integer-valued polynomial rings commute with their base ring::

            sage: K = IntegerValuedPolynomialRing(QQ).B()
            sage: a = K.gen()
            sage: K.is_commutative()
            True
            sage: L = IntegerValuedPolynomialRing(K).B()
            sage: c = L.gen()
            sage: L.is_commutative()
            True
            sage: s = a * c^3; s
            B[1]*B[1] + 6*B[1]*B[2] + 6*B[1]*B[3]
            sage: parent(s)
            Integer-Valued Polynomial Ring over Integer-Valued Polynomial
            Ring over Rational Field in the binomial basis in the binomial basis

        Integer-valued polynomial rings are commutative::

            sage: c^3 * a == c * a * c * c
            True

        We can also manipulate elements in the basis::

            sage: F = IntegerValuedPolynomialRing(QQ).B()
            sage: B = F.basis()
            sage: B[2] * B[3]
            3*B[3] + 12*B[4] + 10*B[5]
            sage: 1 - B[2] * B[2] / 2
            B[0] - 1/2*B[2] - 3*B[3] - 3*B[4]

        and coerce elements from our base field::

            sage: F(4/3)
            4/3*B[0]
        """
        def __init__(self, A) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: F = IntegerValuedPolynomialRing(QQ).B(); F
                Integer-Valued Polynomial Ring over Rational Field
                in the binomial basis
                sage: TestSuite(F).run()
            """
        def product_on_basis(self, n1, n2):
            """
            Return the product of basis elements ``n1`` and ``n2``.

            INPUT:

            - ``n1``, ``n2`` -- integers

            EXAMPLES::

                sage: A = IntegerValuedPolynomialRing(QQ).B()
                sage: A.product_on_basis(0, 1)
                B[1]
                sage: A.product_on_basis(1, 2)
                2*B[2] + 3*B[3]
            """
        class Element(CombinatorialFreeModule.Element):
            def variable_shift(self, k: int = 1):
                """
                Return the image by the shift of variables.

                On polynomials, the action is the shift
                on variables `x \\mapsto x + k`.

                INPUT:

                - ``k`` -- integer (default: 1)

                EXAMPLES::

                    sage: A = IntegerValuedPolynomialRing(ZZ).B()
                    sage: B = A.basis()
                    sage: B[5].variable_shift()
                    B[4] + B[5]
                    sage: B[5].variable_shift(-1)
                    -B[0] + B[1] - B[2] + B[3] - B[4] + B[5]

                TESTS::

                    sage: B[5].variable_shift(0)
                    B[5]
                    sage: B[5].variable_shift().variable_shift(-1)
                    B[5]
                """
    B = Binomial
