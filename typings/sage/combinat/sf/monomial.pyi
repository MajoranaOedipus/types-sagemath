from . import classical as classical
from sage.arith.misc import binomial as binomial, factorial as factorial, multinomial as multinomial
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer

class SymmetricFunctionAlgebra_monomial(classical.SymmetricFunctionAlgebra_classical):
    def __init__(self, Sym) -> None:
        """
        A class for methods related to monomial symmetric functions.

        INPUT:

        - ``self`` -- a monomial symmetric function basis
        - ``Sym`` -- an instance of the ring of the symmetric functions

        TESTS::

            sage: m = SymmetricFunctions(QQ).m()
            sage: m == loads(dumps(m))
            True
            sage: TestSuite(m).run(skip=['_test_associativity', '_test_distributivity', '_test_prod'])
            sage: TestSuite(m).run(elements = [m[1,1]+m[2], m[1]+2*m[1,1]])
        """
    def product(self, left, right):
        """
        Return the product of ``left`` and ``right``.

        - ``left``, ``right`` -- symmetric functions written in the
          monomial basis ``self``

        OUTPUT:

        - the product of ``left`` and ``right``, expanded in the
          monomial basis, as a dictionary whose keys are partitions and
          whose values are the coefficients of these partitions (more
          precisely, their respective monomial symmetric functions) in the
          product.

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).m()
            sage: a = m([2,1])
            sage: a^2
            4*m[2, 2, 1, 1] + 6*m[2, 2, 2] + 2*m[3, 2, 1] + 2*m[3, 3] + 2*m[4, 1, 1] + m[4, 2]

        ::

            sage: QQx.<x> = QQ['x']
            sage: m = SymmetricFunctions(QQx).m()
            sage: a = m([2,1])+x
            sage: 2*a # indirect doctest
            2*x*m[] + 2*m[2, 1]
            sage: a^2
            x^2*m[] + 2*x*m[2, 1] + 4*m[2, 2, 1, 1] + 6*m[2, 2, 2] + 2*m[3, 2, 1] + 2*m[3, 3] + 2*m[4, 1, 1] + m[4, 2]
        """
    def from_polynomial(self, f, check: bool = True):
        """
        Return the symmetric function in the monomial basis corresponding
        to the polynomial ``f``.

        INPUT:

        - ``self`` -- a monomial symmetric function basis
        - ``f`` -- a polynomial in finitely many variables over the
          same base ring as ``self``; it is assumed that this
          polynomial is symmetric
        - ``check`` -- boolean (default: ``True``); checks whether
          the polynomial is indeed symmetric

        OUTPUT:

        - This function converts a symmetric polynomial `f` in a
          polynomial ring in finitely many variables to a symmetric
          function in the monomial basis of the ring of symmetric
          functions over the same base ring.

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).m()
            sage: P = PolynomialRing(QQ, 'x', 3)
            sage: x = P.gens()
            sage: f = x[0] + x[1] + x[2]
            sage: m.from_polynomial(f)
            m[1]
            sage: f = x[0]**2+x[1]**2+x[2]**2
            sage: m.from_polynomial(f)
            m[2]
            sage: f = x[0]^2+x[1]
            sage: m.from_polynomial(f)
            Traceback (most recent call last):
            ...
            ValueError: x0^2 + x1 is not a symmetric polynomial
            sage: f = (m[2,1]+m[1,1]).expand(3)
            sage: m.from_polynomial(f)
            m[1, 1] + m[2, 1]
            sage: f = (2*m[2,1]+m[1,1]+3*m[3]).expand(3)
            sage: m.from_polynomial(f)
            m[1, 1] + 2*m[2, 1] + 3*m[3]

        """
    def from_polynomial_exp(self, p):
        """
        Conversion from polynomial in exponential notation.

        INPUT:

        - ``self`` -- a monomial symmetric function basis
        - ``p`` -- a polynomial over the same base ring as ``self``

        OUTPUT:

        - This returns a symmetric function by mapping each monomial of
          `p` with exponents ``exp`` into `m_\\lambda` where `\\lambda` is
          the partition with exponential notation ``exp``.

        EXAMPLES::

            sage: m = SymmetricFunctions(QQ).m()
            sage: P = PolynomialRing(QQ,'x',5)
            sage: x = P.gens()

        The exponential notation of the partition `(5,5,5,3,1,1)` is::

            sage: Partition([5,5,5,3,1,1]).to_exp()
            [2, 0, 1, 0, 3]

        Therefore, the monomial::

            sage: f = x[0]^2 * x[2] * x[4]^3

        is mapped to::

            sage: m.from_polynomial_exp(f)
            m[5, 5, 5, 3, 1, 1]

        Furthermore, this function is linear::

            sage: f = 3 * x[3] + 2 * x[0]^2 * x[2] * x[4]^3
            sage: m.from_polynomial_exp(f)
            3*m[4] + 2*m[5, 5, 5, 3, 1, 1]

        .. SEEALSO::

            :func:`Partition`, :meth:`Partition.to_exp`
        """
    def antipode_by_coercion(self, element):
        """
        The antipode of ``element`` via coercion to and from the power-sum
        basis or the Schur basis (depending on whether the power sums really
        form a basis over the given ground ring).

        INPUT:

        - ``element`` -- element in a basis of the ring of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: m = Sym.monomial()
            sage: m[3,2].antipode()
            m[3, 2] + 2*m[5]
            sage: m.antipode_by_coercion(m[3,2])
            m[3, 2] + 2*m[5]

            sage: Sym = SymmetricFunctions(ZZ)
            sage: m = Sym.monomial()
            sage: m[3,2].antipode()
            m[3, 2] + 2*m[5]
            sage: m.antipode_by_coercion(m[3,2])
            m[3, 2] + 2*m[5]

        .. TODO::

            Is there a not too difficult way to get the power-sum computations
            to work over any ring, not just one with coercion from `\\QQ`?
        """
    class Element(classical.SymmetricFunctionAlgebra_classical.Element):
        def expand(self, n, alphabet: str = 'x'):
            """
            Expand the symmetric function ``self`` as a symmetric polynomial
            in ``n`` variables.

            INPUT:

            - ``n`` -- nonnegative integer

            - ``alphabet`` -- (default: ``'x'``) a variable for the expansion

            OUTPUT:

            A monomial expansion of ``self`` in the `n` variables
            labelled by ``alphabet``.

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).m()
                sage: m([2,1]).expand(3)
                x0^2*x1 + x0*x1^2 + x0^2*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2
                sage: m([1,1,1]).expand(2)
                0
                sage: m([2,1]).expand(3,alphabet='z')
                z0^2*z1 + z0*z1^2 + z0^2*z2 + z1^2*z2 + z0*z2^2 + z1*z2^2
                sage: m([2,1]).expand(3,alphabet='x,y,z')
                x^2*y + x*y^2 + x^2*z + y^2*z + x*z^2 + y*z^2
                sage: m([1]).expand(0)
                0
                sage: (3*m([])).expand(0)
                3
            """
        def principal_specialization(self, n=..., q=None):
            '''
            Return the principal specialization of a symmetric function.

            The *principal specialization* of order `n` at `q`
            is the ring homomorphism `ps_{n,q}` from the ring of
            symmetric functions to another commutative ring `R`
            given by `x_i \\mapsto q^{i-1}` for `i \\in \\{1,\\dots,n\\}`
            and `x_i \\mapsto 0` for `i > n`.
            Here, `q` is a given element of `R`, and we assume that
            the variables of our symmetric functions are
            `x_1, x_2, x_3, \\ldots`.
            (To be more precise, `ps_{n,q}` is a `K`-algebra
            homomorphism, where `K` is the base ring.)
            See Section 7.8 of [EnumComb2]_.

            The *stable principal specialization* at `q` is the ring
            homomorphism `ps_q` from the ring of symmetric functions
            to another commutative ring `R` given by
            `x_i \\mapsto q^{i-1}` for all `i`.
            This is well-defined only if the resulting infinite sums
            converge; thus, in particular, setting `q = 1` in the
            stable principal specialization is an invalid operation.

            INPUT:

            - ``n`` -- (default: ``infinity``) a nonnegative integer or
              ``infinity``, specifying whether to compute the principal
              specialization of order ``n`` or the stable principal
              specialization.

            - ``q`` -- (default: ``None``) the value to use for `q`; the
              default is to create a ring of polynomials in ``q``
              (or a field of rational functions in ``q``) over the
              given coefficient ring.

            For ``q=1`` and finite ``n`` we use the formula from
            Proposition 7.8.3 of [EnumComb2]_:

            .. MATH::

                ps_{n,1}(m_\\lambda) = \\binom{n}{\\ell(\\lambda)}
                                      \\binom{\\ell(\\lambda)}{m_1(\\lambda), m_2(\\lambda),\\dots},

            where `\\ell(\\lambda)` denotes the length of `\\lambda`.

            In all other cases, we convert to complete homogeneous
            symmetric functions.

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).m()
                sage: x = m[3,1]
                sage: x.principal_specialization(3)
                q^7 + q^6 + q^5 + q^3 + q^2 + q

                sage: x = 5*m[2] + 3*m[1] + 1
                sage: x.principal_specialization(3, q=var("q"))                         # needs sage.symbolic
                -10*(q^3 - 1)*q/(q - 1) + 5*(q^3 - 1)^2/(q - 1)^2 + 3*(q^3 - 1)/(q - 1) + 1

            TESTS::

                sage: m.zero().principal_specialization(3)
                0
            '''
        def exponential_specialization(self, t=None, q: int = 1):
            '''
            Return the exponential specialization of a
            symmetric function (when `q = 1`), or the
            `q`-exponential specialization (when `q \\neq 1`).

            The *exponential specialization* `ex` at `t` is a
            `K`-algebra homomorphism from the `K`-algebra of
            symmetric functions to another `K`-algebra `R`.
            It is defined whenever the base ring `K` is a
            `\\QQ`-algebra and `t` is an element of `R`.
            The easiest way to define it is by specifying its
            values on the powersum symmetric functions to be
            `p_1 = t` and `p_n = 0` for `n > 1`.
            Equivalently, on the homogeneous functions it is
            given by `ex(h_n) = t^n / n!`; see Proposition 7.8.4 of
            [EnumComb2]_.

            By analogy, the `q`-exponential specialization is a
            `K`-algebra homomorphism from the `K`-algebra of
            symmetric functions to another `K`-algebra `R` that
            depends on two elements `t` and `q` of `R` for which
            the elements `1 - q^i` for all positive integers `i`
            are invertible.
            It can be defined by specifying its values on the
            complete homogeneous symmetric functions to be

            .. MATH::

                ex_q(h_n) = t^n / [n]_q!,

            where `[n]_q!` is the `q`-factorial.  Equivalently, for
            `q \\neq 1` and a homogeneous symmetric function `f` of
            degree `n`, we have

            .. MATH::

                ex_q(f) = (1-q)^n t^n ps_q(f),

            where `ps_q(f)` is the stable principal specialization of `f`
            (see :meth:`principal_specialization`).
            (See (7.29) in [EnumComb2]_.)

            The limit of `ex_q` as `q \\to 1` is `ex`.

            INPUT:

            - ``t`` -- (default: ``None``) the value to use for `t`;
              the default is to create a ring of polynomials in ``t``

            - ``q`` -- (default: `1`) the value to use for `q`;  if
              ``q`` is ``None``, then a ring (or fraction field) of
              polynomials in ``q`` is created

            EXAMPLES::

                sage: m = SymmetricFunctions(QQ).m()
                sage: (m[3]+m[2,1]+m[1,1,1]).exponential_specialization()
                1/6*t^3

                sage: x = 5*m[1,1,1] + 3*m[2,1] + 1
                sage: x.exponential_specialization()
                5/6*t^3 + 1

            We also support the `q`-exponential_specialization::

                sage: factor(m[3].exponential_specialization(q=var("q"), t=var("t")))   # needs sage.symbolic
                (q - 1)^2*t^3/(q^2 + q + 1)

            TESTS::

                sage: m.zero().exponential_specialization()
                0
            '''
