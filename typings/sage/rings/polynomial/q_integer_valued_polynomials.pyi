from sage.arith.misc import binomial as binomial
from sage.categories.algebras import Algebras as Algebras
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent
from sage.categories.rings import Rings as Rings
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.q_analogues import q_binomial as q_binomial, q_int as q_int
from sage.data_structures.blas_dict import linear_combination as linear_combination
from sage.matrix.constructor import matrix as matrix
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.element import parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def q_int_x(n, q=None):
    """
    Return the interpolating polynomial of `q`-integers.

    INPUT:

    - ``n`` -- a positive integer

    - ``q`` -- optional variable

    EXAMPLES::

        sage: from sage.rings.polynomial.q_integer_valued_polynomials import q_int_x
        sage: q_int_x(3)
        q^2*x + q + 1

    TESTS::

        sage: from sage.rings.polynomial.q_integer_valued_polynomials import q_int_x
        sage: q_int_x(3, 1)
        x + 2
    """
def q_binomial_x(m, n, q=None):
    """
    Return a `q`-analogue of ``binomial(m + x, n)``.

    When evaluated at the `q`-integer `[k]_q`, this gives
    the usual `q`-binomial coefficient `[m + k, n]_q`.

    INPUT:

    - ``m`` and ``n`` -- positive integers

    - ``q`` -- optional variable

    EXAMPLES::

        sage: from sage.combinat.q_analogues import q_int
        sage: from sage.rings.polynomial.q_integer_valued_polynomials import q_binomial_x, q_int_x
        sage: q_binomial_x(4,2)(0) == q_binomial(4,2)
        True
        sage: q_binomial_x(3,2)(1) == q_binomial(4,2)
        True
        sage: q_binomial_x(3,1) == q_int_x(4)
        True
        sage: q_binomial_x(2,0).parent()
        Univariate Polynomial Ring in x over Fraction Field of
        Univariate Polynomial Ring in q over Integer Ring

    TESTS::

        sage: from sage.rings.polynomial.q_integer_valued_polynomials import q_binomial_x
        sage: q_binomial_x(4,2,1)
        1/2*x^2 + 7/2*x + 6
    """

class QuantumValuedPolynomialRing(UniqueRepresentation, Parent):
    """
    The quantum-valued polynomial ring over a base ring.

    Quantum-valued polynomial rings are commutative and associative
    algebras, with a basis indexed by nonnegative integers.

    The elements are polynomials in one variable `x` with coefficients in
    the field of rational functions in `q`, such that the value at
    every nonegative `q`-integer is a polynomial in `q`.

    This algebra is endowed with two bases, named ``B`` or ``Binomial``
    and ``S`` or ``Shifted``.

    INPUT:

    - ``R`` -- commutative ring

    - ``q`` -- optional variable

    There are two possible input formats:

    - If the argument ``q`` is not given, then the ring ``R`` is
      taken as a base ring and the ring of Laurent polynomials in `q`
      over ``R`` is built and used.

    - If the argument ``q`` is given, then it should belong to the ring ``R``
      and be invertible in this ring.

    EXAMPLES::

        sage: F = QuantumValuedPolynomialRing(QQ).S(); F
        Quantum-Valued Polynomial Ring over Rational Field
        in the shifted basis

        sage: F.gen()
        S[1]

        sage: S = QuantumValuedPolynomialRing(ZZ); S
        Quantum-Valued Polynomial Ring over Integer Ring
        sage: S.base_ring()
        Univariate Laurent Polynomial Ring in q over Integer Ring

    Quantum-valued polynomial rings commute with their base ring::

        sage: K = QuantumValuedPolynomialRing(QQ).S()
        sage: a = K.gen()
        sage: c = K.monomial(2)

    Quantum-valued polynomial rings are commutative::

        sage: c^3 * a == c * a * c * c
        True

    We can also manipulate elements in the basis and coerce elements from our
    base field::

        sage: F = QuantumValuedPolynomialRing(QQ).S()
        sage: B = F.basis()
        sage: B[2] * B[3]
        (q^-5+q^-4+q^-3)*S[3] - (q^-6+2*q^-5+3*q^-4+3*q^-3+2*q^-2+q^-1)*S[4]
        + (q^-6+q^-5+2*q^-4+2*q^-3+2*q^-2+q^-1+1)*S[5]
        sage: 1 - B[2] * B[2] / 2
        S[0] - (1/2*q^-3)*S[2] + (1/2*q^-4+q^-3+q^-2+1/2*q^-1)*S[3]
        - (1/2*q^-4+1/2*q^-3+q^-2+1/2*q^-1+1/2)*S[4]
    """
    @staticmethod
    def __classcall_private__(cls, R, q=None) -> None:
        """
        Normalize the input.

        EXAMPLES::

            sage: q = LaurentPolynomialRing(QQ, 'q').gen()
            sage: F1 = QuantumValuedPolynomialRing(QQ)
            sage: F2 = QuantumValuedPolynomialRing(q.parent(), q)
            sage: F1 is F2
            True
        """
    def __init__(self, R, q) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: F = QuantumValuedPolynomialRing(QQ); F
            Quantum-Valued Polynomial Ring over Rational Field
            sage: TestSuite(F).run()

            sage: F = QuantumValuedPolynomialRing(QQ, 1); F
            Quantum-Valued Polynomial Ring over Integer Ring
            sage: TestSuite(F).run()

        TESTS::

            sage: QuantumValuedPolynomialRing(24)
            Traceback (most recent call last):
            ...
            TypeError: argument R must be a commutative ring
        """
    def a_realization(self):
        """
        Return a default realization.

        The Shifted realization is chosen.

        EXAMPLES::

            sage: QuantumValuedPolynomialRing(QQ).a_realization()
            Quantum-Valued Polynomial Ring over Rational Field
            in the shifted basis
        """
    class Bases(Category_realization_of_parent):
        def super_categories(self) -> list:
            """
            Return the super-categories of ``self``.

            EXAMPLES::

                sage: A = QuantumValuedPolynomialRing(QQ); A
                Quantum-Valued Polynomial Ring over Rational Field
                sage: C = A.Bases(); C
                Category of bases of Quantum-Valued Polynomial Ring
                over Rational Field
                sage: C.super_categories()
                [Category of realizations of Quantum-Valued Polynomial Ring
                 over Rational Field,
                 Join of Category of algebras with basis
                 over Univariate Laurent Polynomial Ring in q over Rational Field and
                 Category of filtered algebras
                 over Univariate Laurent Polynomial Ring in q over Rational Field and
                 Category of commutative algebras
                 over Univariate Laurent Polynomial Ring in q over Rational Field and
                 Category of realizations of unital magmas]
            """
        class ParentMethods:
            def ground_ring(self):
                """
                Return the ring of coefficients.

                This ring is not supposed to contain the variable `q`.

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(QQ).S()
                    sage: A.ground_ring()
                    Rational Field
                """
            @cached_method
            def one_basis(self):
                """
                Return the number 0, which index the unit of this algebra.

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(QQ).S()
                    sage: A.one_basis()
                    0
                    sage: A.one()
                    S[0]
                """
            def q(self):
                """
                Return the variable `q`.

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(QQ).S()
                    sage: A.q()
                    q
                """
            def degree_on_basis(self, m):
                """
                Return the degree of the basis element indexed by ``m``.

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(QQ).S()
                    sage: A.degree_on_basis(4)
                    4
                """
            def from_polynomial(self, p):
                """
                Convert a polynomial into the ring of quantum-valued polynomials.

                This raises a :exc:`ValueError` if this is not possible.

                INPUT:

                - ``p`` -- a polynomial in ``x`` with coefficients in ``QQ(q)``

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(ZZ).S()
                    sage: S = A.basis()
                    sage: A.from_polynomial((S[1]).polynomial())
                    S[1]
                    sage: A.from_polynomial((S[2]+2*S[3]).polynomial())
                    S[2] + 2*S[3]

                    sage: A = QuantumValuedPolynomialRing(ZZ).B()
                    sage: B = A.basis()
                    sage: A.from_polynomial((B[1]).polynomial())
                    B[1]
                    sage: A.from_polynomial((B[2]+2*B[3]).polynomial())
                    B[2] + 2*B[3]

                TESTS::

                    sage: A = QuantumValuedPolynomialRing(QQ).B()
                    sage: q = polygen(QQ,'q')
                    sage: x = polygen(q.parent(),'x')
                    sage: A.from_polynomial(x**2/(q+1)+1)
                    Traceback (most recent call last):
                    ...
                    ValueError: not a polynomial with integer values : 1/(q + 1) is not a Laurent polynomial
                """
            def gen(self, i: int = 0):
                """
                Return the generator of the algebra.

                The optional argument is ignored.

                EXAMPLES::

                    sage: F = QuantumValuedPolynomialRing(ZZ).S()
                    sage: F.gen()
                    S[1]
                """
            @cached_method
            def algebra_generators(self):
                """
                Return the generators of this algebra.

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(ZZ).S(); A
                    Quantum-Valued Polynomial Ring over Integer Ring
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

                     sage: F = QuantumValuedPolynomialRing(ZZ).S()
                     sage: B = F.gen()
                     sage: f = B**2+4*B+6
                     sage: f(1/3)
                     (q^2 + 18*q + 99)/9

                     sage: F = QuantumValuedPolynomialRing(ZZ).B()
                     sage: B = F.gen()
                     sage: f = F.monomial(2)+4*B+6
                     sage: f(1/3)
                     (66*q^2 + 66*q - 2)/(9*q^2 + 9*q)
                """
            def polynomial(self):
                """
                Convert to a polynomial in `x`.

                EXAMPLES::

                    sage: F = QuantumValuedPolynomialRing(ZZ).S()
                    sage: S = F.gen()
                    sage: (S+1).polynomial()
                    q*x + 2

                    sage: F = QuantumValuedPolynomialRing(ZZ).B()
                    sage: B = F.gen()
                    sage: (B+1).polynomial()
                    x + 1

                TESTS::

                    sage: F.zero().polynomial().parent()
                    Univariate Polynomial Ring in x over Fraction Field
                    of Univariate Polynomial Ring in q over Integer Ring
                """
            def shift(self, j: int = 1):
                """
                Shift all indices by `j`.

                INPUT:

                - `j` -- integer (default 1)

                In the binomial basis, the shift by 1 corresponds to
                a summation operator from `0` to `x`.

                EXAMPLES::

                    sage: F = QuantumValuedPolynomialRing(ZZ).S()
                    sage: B = F.gen()
                    sage: (B+1).shift()
                    S[1] + S[2]
                """
            def sum_of_coefficients(self):
                """
                Return the sum of coefficients.

                In the shifted basis, this is the evaluation at `x=0`.

                EXAMPLES::

                    sage: F = QuantumValuedPolynomialRing(ZZ).S()
                    sage: B = F.basis()
                    sage: (B[2]*B[4]).sum_of_coefficients()
                    1
                """
    class Shifted(CombinatorialFreeModule, BindableClass):
        """
        The quantum-valued polynomial ring in the shifted basis.

        The basis used here is given by `S[i] = \\genfrac{[}{]}{0pt}{}{i+x}{i}_q` for `i \\in \\NN`.

        Assuming `n_1 \\leq n_2`, the product of two monomials `S[n_1] \\cdot S[n_2]`
        is given by the sum

        .. MATH::

            \\sum_{k=0}^{n_1} (-1)^k q^{\\binom{k}{2} - n_1 * n_2} \\genfrac{[}{]}{0pt}{}{n_1}{k}_q \\genfrac{[}{]}{0pt}{}{n_1+n_2-k}{n_1}_q S[n_1 + n_2 - k].
        """
        def __init__(self, A) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: F = QuantumValuedPolynomialRing(QQ).S(); F
                Quantum-Valued Polynomial Ring over Rational Field
                in the shifted basis
                sage: TestSuite(F).run()  # not tested
            """
        def product_on_basis(self, n1, n2):
            """
            Return the product of basis elements ``n1`` and ``n2``.

            INPUT:

            - ``n1``, ``n2`` -- integers

            EXAMPLES::

                sage: A = QuantumValuedPolynomialRing(QQ).S()
                sage: A.product_on_basis(0, 1)
                S[1]
            """
        def from_h_vector(self, hv):
            """
            Convert from some `h`-vector.

            EXAMPLES::

                sage: A = QuantumValuedPolynomialRing(ZZ).S()
                sage: B = A.basis()
                sage: ex = B[2] + B[3]
                sage: A.from_h_vector(ex.h_vector())
                S[2] + S[3]

                sage: q = A.base_ring().gen()
                sage: ex = B[2] + q*B[3]
                sage: A.from_h_vector(ex.h_vector())
                S[2] + q*S[3]
            """
        class Element(CombinatorialFreeModule.Element):
            def umbra(self):
                """
                Return the Bernoulli umbra.

                This is the derivative at `-1` of the shift by one.

                This is related to Carlitz's `q`-Bernoulli numbers.

                .. SEEALSO:: :meth:`derivative_at_minus_one`

                EXAMPLES::

                    sage: F = QuantumValuedPolynomialRing(ZZ).S()
                    sage: B = F.gen()
                    sage: (B+1).umbra()
                    (q + 2)/(q + 1)
                """
            def variable_shift(self, k: int = 1):
                """
                Return the image by the shift on variables.

                The shift is the substitution operator

                .. MATH::

                    x \\mapsto q x + 1.

                INPUT:

                - `k` -- integer (default: 1)

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(ZZ).S()
                    sage: S = A.basis()
                    sage: S[5].variable_shift()
                    S[0] + q*S[1] + q^2*S[2] + q^3*S[3] + q^4*S[4] + q^5*S[5]

                    sage: S[5].variable_shift(-1)
                    -(q^-5)*S[4] + (q^-5)*S[5]

                TESTS::

                    sage: S[5].variable_shift(0)
                    S[5]
                    sage: S[5].variable_shift().variable_shift(-1)
                    S[5]
                    sage: S[5].variable_shift(2).variable_shift(-2)
                    S[5]
                    sage: S[3].variable_shift(-2)
                    (q^-5)*S[1] - (q^-6+q^-5)*S[2] + (q^-6)*S[3]
                """
            def derivative_at_minus_one(self):
                """
                Return the 'derivative' at -1.

                .. SEEALSO:: :meth:`umbra`

                EXAMPLES::

                    sage: F = QuantumValuedPolynomialRing(ZZ).S()
                    sage: B = F.gen()
                    sage: (B+1).derivative_at_minus_one()
                    1
                """
            def h_vector(self):
                """
                Return the numerator of the generating series of values.

                If ``self`` is an Ehrhart polynomial, this is the h-vector.

                .. SEEALSO:: :meth:`h_polynomial`, :meth:`fraction`

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(ZZ).S()
                    sage: ex = A.basis()[4]
                    sage: ex.h_vector()
                    (0, 0, 0, 0, 1)

                    sage: q = polygen(QQ,'q')
                    sage: x = polygen(q.parent(),'x')
                    sage: ex = A.from_polynomial((1+q*x)**3)
                    sage: ex.h_vector()
                    (0, q^3, 2*q + 2*q^2, 1)
                """
            def h_polynomial(self):
                """
                Return the `h`-vector as a polynomial.

                .. SEEALSO:: :meth:`h_vector`, :meth:`fraction`

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(ZZ).S()
                    sage: q = polygen(ZZ,'q')
                    sage: x = polygen(q.parent(),'x')
                    sage: ex = A.from_polynomial((1+q*x)**3)
                    sage: ex.h_polynomial()
                    z^3 + (2*q + 2*q^2)*z^2 + q^3*z
                """
            def fraction(self):
                """
                Return the generating series of values as a fraction.

                .. SEEALSO:: :meth:`h_vector`, :meth:`h_polynomial`

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(QQ).S()
                    sage: ex = A.basis()[4]
                    sage: ex.fraction().factor()
                    (-1) * (t - 1)^-1 * (q*t - 1)^-1 * (q^2*t - 1)^-1 * (q^3*t - 1)^-1 * (q^4*t - 1)^-1

                    sage: q = polygen(QQ,'q')
                    sage: x = polygen(q.parent(), 'x')
                    sage: ex = A.from_polynomial((1+q*x)**3)
                    sage: ex.fraction().factor()
                    (t - 1)^-1 * (q*t - 1)^-1 * (q^2*t - 1)^-1 * (q^3*t - 1)^-1 * (q^3*t^2 + 2*q^2*t + 2*q*t + 1)
                    sage: ex.fraction().numerator()
                    q^3*t^2 + 2*q^2*t + 2*q*t + 1
                """
    S = Shifted
    class Binomial(CombinatorialFreeModule, BindableClass):
        """
        The quantum-valued polynomial ring in the binomial basis.

        The basis used here is given by `B[i] = \\genfrac{[}{]}{0pt}{}{x}{i}_q` for `i \\in \\NN`.

        Assuming `n_1 \\leq n_2`, the product of two monomials `B[n_1] \\cdot B[n_2]`
        is given by the sum

        .. MATH::

            \\sum_{k=0}^{n_1} q^{(k-n_1)(k-n_2)} \\genfrac{[}{]}{0pt}{}{n_1}{k}_q \\genfrac{[}{]}{0pt}{}{n_1+n_2-k}{n_1}_q B[n_1 + n_2 - k].
        """
        def __init__(self, A) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: F = QuantumValuedPolynomialRing(QQ).B(); F
                Quantum-Valued Polynomial Ring over Rational Field
                in the binomial basis
                sage: TestSuite(F).run()  # not tested
            """
        def product_on_basis(self, n1, n2):
            """
            Return the product of basis elements ``n1`` and ``n2``.

            INPUT:

            - ``n1``, ``n2`` -- integers

            The formula is taken from Theorem 3.4 in [HaHo2017]_.

            EXAMPLES::

                sage: A = QuantumValuedPolynomialRing(QQ).B()
                sage: A.product_on_basis(0, 1)
                B[1]
            """
        class Element(CombinatorialFreeModule.Element):
            def variable_shift(self, k: int = 1):
                """
                Return the image by the shift of variables.

                On polynomials, the action for `k=1` is the shift
                on variables `x \\mapsto 1 + qx`.

                This implementation follows formula (5.5) in [HaHo2017]_.

                INPUT:

                - `k` -- nonnegative integer (default: 1)

                EXAMPLES::

                    sage: A = QuantumValuedPolynomialRing(ZZ).B()
                    sage: B = A.basis()
                    sage: B[5].variable_shift()
                    B[4] + q^5*B[5]

                TESTS::

                    sage: B[5].variable_shift(0)
                    B[5]
                """
    B = Binomial
