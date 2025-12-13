from . import classical as classical
from sage.arith.misc import factorial as factorial
from sage.combinat.tableau import StandardTableaux as StandardTableaux
from sage.data_structures.blas_dict import convert_remove_zeroes as convert_remove_zeroes
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

class SymmetricFunctionAlgebra_schur(classical.SymmetricFunctionAlgebra_classical):
    def __init__(self, Sym) -> None:
        """
        A class for methods related to the Schur symmetric function basis.

        INPUT:

        - ``self`` -- a Schur symmetric function basis
        - ``Sym`` -- an instance of the ring of the symmetric functions

        TESTS::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s == loads(dumps(s))
            True
            sage: TestSuite(s).run(skip=['_test_associativity', '_test_distributivity', '_test_prod'])
            sage: TestSuite(s).run(elements = [s[1,1]+s[2], s[1]+2*s[1,1]])
        """
    def product_on_basis(self, left, right):
        """
        Return the product of ``left`` and ``right``.

        INPUT:

        - ``self`` -- a Schur symmetric function basis
        - ``left``, ``right`` -- partitions

        OUTPUT: an element of the Schur basis, the product of ``left`` and ``right``

        TESTS::

            sage: s = SymmetricFunctions(QQ).s()
            sage: a = s([2,1]) + 1; a
            s[] + s[2, 1]
            sage: a^2   # indirect doctest
            s[] + 2*s[2, 1] + s[2, 2, 1, 1] + s[2, 2, 2] + s[3, 1, 1, 1]
             + 2*s[3, 2, 1] + s[3, 3] + s[4, 1, 1] + s[4, 2]

        Examples failing with three different messages in symmetrica::

            sage: s[123,1]*s[1,1]
            s[123, 1, 1, 1] + s[123, 2, 1] + s[124, 1, 1] + s[124, 2]
            sage: s[123]*s[2,1]
            s[123, 2, 1] + s[124, 1, 1] + s[124, 2] + s[125, 1]
            sage: s[125]*s[3]
            s[125, 3] + s[126, 2] + s[127, 1] + s[128]

        ::

            sage: QQx.<x> = QQ[]
            sage: s = SymmetricFunctions(QQx).s()
            sage: a = x^2*s([2,1]) + 2*x; a
            2*x*s[] + x^2*s[2, 1]
            sage: a^2
            4*x^2*s[] + 4*x^3*s[2, 1] + x^4*s[2, 2, 1, 1] + x^4*s[2, 2, 2]
             + x^4*s[3, 1, 1, 1] + 2*x^4*s[3, 2, 1] + x^4*s[3, 3]
             + x^4*s[4, 1, 1] + x^4*s[4, 2]

        ::

            sage: 0*s([2,1])
            0

        Example over a field with positive characteristic::

            sage: s[2,1]^2
            s[2, 2, 1, 1] + s[2, 2, 2] + s[3, 1, 1, 1] + 2*s[3, 2, 1]
             + s[3, 3] + s[4, 1, 1] + s[4, 2]
            sage: s = SymmetricFunctions(GF(2)).s()
            sage: s[2,1]^2
            s[2, 2, 1, 1] + s[2, 2, 2] + s[3, 1, 1, 1] + s[3, 3] + s[4, 1, 1] + s[4, 2]
        """
    def coproduct_on_basis(self, mu):
        """
        Return the coproduct of ``self(mu)``.

        Here ``self`` is the basis of Schur functions in the ring of symmetric functions.

        INPUT:

        - ``self`` -- a Schur symmetric function basis
        - ``mu`` -- a partition

        OUTPUT:

        - the image of the ``mu``-th Schur function under the comultiplication of
          the Hopf algebra of symmetric functions; this is an element of the
          tensor square of the Schur basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: s = Sym.schur()
            sage: s.coproduct_on_basis([2])
            s[] # s[2] + s[1] # s[1] + s[2] # s[]

        TESTS::

            sage: s = SymmetricFunctions(QQ['t']).s()
            sage: s[2].coproduct() / 2
            1/2*s[] # s[2] + 1/2*s[1] # s[1] + 1/2*s[2] # s[]
        """
    class Element(classical.SymmetricFunctionAlgebra_classical.Element):
        def __pow__(self, n):
            """
            Return the naive powering of an instance of ``self``.

            INPUT:

            - ``self`` -- an element of the Schur symmetric function basis
            - ``n`` -- nonnegative integer

            OUTPUT: the `n`-th power of an instance of ``self`` in the Schur basis

            See ``Monoids.Element.__pow__`` and ``Monoids.Element._pow_naive``.

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ['x']).s()
                sage: len(s([2,1])^8) # long time (~ 4 s)
                1485
                sage: len(s([2,1])^9) # long time (~10 s)
                2876

            Binary exponentiation does not seem to bring any speedup for
            Schur functions. This most likely is because of the
            explosion of the number of terms.

            #    sage: s = SymmetricFunctions(QQ).s(); y = s([1])
            #    sage: n = 24
            #    sage: %timeit y**n    # using binary exponentiation
            #    10 loops, best of 3: 1.22 s per loop
            #    sage: %timeit prod(y for i in range(n))
            #    10 loops, best of 3: 1.06 s per loop

            With polynomial coefficients, this is actually much *slower*
            (although this should be profiled further; there seems to
            be an unreasonable number of polynomial multiplication involved,
            besides the fact that 1 * QQ['x'].one() currently involves a
            polynomial multiplication)

            #    sage: sage: s = SymmetricFunctions(QQ['x']).s()
            #    sage: y = s([2,1])
            #    sage: %timeit y**7
            #    10 loops, best of 3: 18.9 s per loop
            #    sage: %timeit y*y*y*y*y*y*y
            #    10 loops, best of 3: 1.73 s per loop

            Todo: do the same for the other non multiplicative bases?
            """
        def omega(self):
            """
            Return the image of ``self`` under the omega automorphism.

            The *omega automorphism* is defined to be the unique algebra
            endomorphism `\\omega` of the ring of symmetric functions that
            satisfies `\\omega(e_k) = h_k` for all positive integers `k`
            (where `e_k` stands for the `k`-th elementary symmetric
            function, and `h_k` stands for the `k`-th complete homogeneous
            symmetric function). It furthermore is a Hopf algebra
            endomorphism and an involution, and it is also known as the
            *omega involution*. It sends the power-sum symmetric function
            `p_k` to `(-1)^{k-1} p_k` for every positive integer `k`.

            The images of some bases under the omega automorphism are given by

            .. MATH::

                \\omega(e_{\\lambda}) = h_{\\lambda}, \\qquad
                \\omega(h_{\\lambda}) = e_{\\lambda}, \\qquad
                \\omega(p_{\\lambda}) = (-1)^{|\\lambda| - \\ell(\\lambda)}
                p_{\\lambda}, \\qquad
                \\omega(s_{\\lambda}) = s_{\\lambda^{\\prime}},

            where `\\lambda` is any partition, where `\\ell(\\lambda)` denotes
            the length (:meth:`~sage.combinat.partition.Partition.length`)
            of the partition `\\lambda`, where `\\lambda^{\\prime}` denotes the
            conjugate partition
            (:meth:`~sage.combinat.partition.Partition.conjugate`) of
            `\\lambda`, and where the usual notations for bases are used
            (`e` = elementary, `h` = complete homogeneous, `p` = powersum,
            `s` = Schur).

            :meth:`omega_involution()` is a synonym for the :meth:`omega()`
            method.

            OUTPUT: the image of ``self`` under the omega automorphism

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: s([2,1]).omega()
                s[2, 1]
                sage: s([2,1,1]).omega()
                s[3, 1]
            """
        omega_involution = omega
        def scalar(self, x, zee=None):
            """
            Return the standard scalar product between ``self`` and `x`.

            Note that the Schur functions are self-dual with respect to this
            scalar product. They are also lower-triangularly related to the
            monomial symmetric functions with respect to this scalar product.

            INPUT:

            - ``x`` -- element of the ring of symmetric functions over the
              same base ring as ``self``

            - ``zee`` -- an optional function on partitions giving
              the value for the scalar product between the power-sum
              symmetric function `p_{\\mu}` and itself
              (the default value is the standard
              :meth:`~sage.combinat.sf.sfa.zee` function)

            OUTPUT: the scalar product between ``self`` and ``x``

            EXAMPLES::

                sage: s = SymmetricFunctions(ZZ).s()
                sage: a = s([2,1])
                sage: b = s([1,1,1])
                sage: c = 2*s([1,1,1])
                sage: d = a + b
                sage: a.scalar(a)
                1
                sage: b.scalar(b)
                1
                sage: b.scalar(a)
                0
                sage: b.scalar(c)
                2
                sage: c.scalar(c)
                4
                sage: d.scalar(a)
                1
                sage: d.scalar(b)
                1
                sage: d.scalar(c)
                2

            ::

                sage: m = SymmetricFunctions(ZZ).monomial()
                sage: p4 = Partitions(4)
                sage: l = [ [s(p).scalar(m(q)) for q in p4] for p in p4]
                sage: matrix(l)
                [ 1  0  0  0  0]
                [-1  1  0  0  0]
                [ 0 -1  1  0  0]
                [ 1 -1 -1  1  0]
                [-1  2  1 -3  1]
            """
        def verschiebung(self, n):
            '''
            Return the image of the symmetric function ``self`` under the
            `n`-th Verschiebung operator.

            The `n`-th Verschiebung operator `\\mathbf{V}_n` is defined to be
            the unique algebra endomorphism `V` of the ring of symmetric
            functions that satisfies `V(h_r) = h_{r/n}` for every positive
            integer `r` divisible by `n`, and satisfies `V(h_r) = 0` for
            every positive integer `r` not divisible by `n`. This operator
            `\\mathbf{V}_n` is a Hopf algebra endomorphism. For every
            nonnegative integer `r` with `n \\mid r`, it satisfies

            .. MATH::

                \\mathbf{V}_n(h_r) = h_{r/n},
                \\quad \\mathbf{V}_n(p_r) = n p_{r/n},
                \\quad \\mathbf{V}_n(e_r) = (-1)^{r - r/n} e_{r/n}

            (where `h` is the complete homogeneous basis, `p` is the
            powersum basis, and `e` is the elementary basis). For every
            nonnegative integer `r` with `n \\nmid r`, it satisfes

            .. MATH::

                \\mathbf{V}_n(h_r) = \\mathbf{V}_n(p_r) = \\mathbf{V}_n(e_r) = 0.

            The `n`-th Verschiebung operator is also called the `n`-th
            Verschiebung endomorphism. Its name derives from the Verschiebung
            (German for "shift") endomorphism of the Witt vectors.

            The `n`-th Verschiebung operator is adjoint to the `n`-th
            Frobenius operator (see :meth:`frobenius` for its definition)
            with respect to the Hall scalar product (:meth:`scalar`).

            The action of the `n`-th Verschiebung operator on the Schur basis
            can also be computed explicitly. The following (probably clumsier
            than necessary) description can be obtained by solving exercise
            7.61 in Stanley\'s [STA]_.

            Let `\\lambda` be a partition. Let `n` be a positive integer. If
            the `n`-core of `\\lambda` is nonempty, then
            `\\mathbf{V}_n(s_\\lambda) = 0`. Otherwise, the following method
            computes `\\mathbf{V}_n(s_\\lambda)`: Write the partition `\\lambda`
            in the form `(\\lambda_1, \\lambda_2, \\ldots, \\lambda_{ns})` for some
            nonnegative integer `s`. (If `n` does not divide the length of
            `\\lambda`, then this is achieved by adding trailing zeroes to
            `\\lambda`.) Set `\\beta_i = \\lambda_i + ns - i` for every
            `s \\in \\{ 1, 2, \\ldots, ns \\}`. Then,
            `(\\beta_1, \\beta_2, \\ldots, \\beta_{ns})` is a strictly decreasing
            sequence of nonnegative integers. Stably sort the list
            `(1, 2, \\ldots, ns)` in order of (weakly) increasing remainder of
            `-1 - \\beta_i` modulo `n`. Let `\\xi` be the sign of the
            permutation that is used for this sorting. Let `\\psi` be the sign
            of the permutation that is used to stably sort the list
            `(1, 2, \\ldots, ns)` in order of (weakly) increasing remainder of
            `i - 1` modulo `n`. (Notice that `\\psi = (-1)^{n(n-1)s(s-1)/4}`.)
            Then, `\\mathbf{V}_n(s_\\lambda) = \\xi \\psi \\prod_{i = 0}^{n - 1}
            s_{\\lambda^{(i)}}`, where
            `(\\lambda^{(0)}, \\lambda^{(1)}, \\ldots, \\lambda^{(n - 1)})`
            is the `n`-quotient of `\\lambda`.

            INPUT:

            - ``n`` -- positive integer

            OUTPUT:

            The result of applying the `n`-th Verschiebung operator (on the ring of
            symmetric functions) to ``self``.

            EXAMPLES::

                sage: Sym = SymmetricFunctions(ZZ)
                sage: s = Sym.s()
                sage: s[5].verschiebung(2)
                0
                sage: s[6].verschiebung(6)
                s[1]
                sage: s[6,3].verschiebung(3)
                s[2, 1] + s[3]
                sage: s[6,3,1].verschiebung(2)
                -s[3, 2]
                sage: s[3,2,1].verschiebung(1)
                s[3, 2, 1]
                sage: s([]).verschiebung(1)
                s[]
                sage: s([]).verschiebung(4)
                s[]

            TESTS:

            Let us check that this method on the powersum basis gives the
            same result as the implementation in sfa.py on the monomial
            basis::

                sage: Sym = SymmetricFunctions(QQ)
                sage: s = Sym.s(); h = Sym.h()
                sage: all( h(s(lam)).verschiebung(3) == h(s(lam).verschiebung(3))
                ....:      for lam in Partitions(6) )
                True
                sage: all( s(h(lam)).verschiebung(2) == s(h(lam).verschiebung(2))
                ....:      for lam in Partitions(4) )
                True
                sage: all( s(h(lam)).verschiebung(5) == s(h(lam).verschiebung(5))
                ....:      for lam in Partitions(10) )
                True
                sage: all( s(h(lam)).verschiebung(2) == s(h(lam).verschiebung(2))
                ....:      for lam in Partitions(8) )
                True
                sage: all( s(h(lam)).verschiebung(3) == s(h(lam).verschiebung(3))
                ....:      for lam in Partitions(12) )
                True
                sage: all( s(h(lam)).verschiebung(3) == s(h(lam).verschiebung(3))
                ....:      for lam in Partitions(9) )
                True
            '''
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

                sage: s = SymmetricFunctions(QQ).s()
                sage: a = s([2,1])
                sage: a.expand(2)
                x0^2*x1 + x0*x1^2
                sage: a.expand(3)
                x0^2*x1 + x0*x1^2 + x0^2*x2 + 2*x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2
                sage: a.expand(4)
                x0^2*x1 + x0*x1^2 + x0^2*x2 + 2*x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2 + x0^2*x3 + 2*x0*x1*x3 + x1^2*x3 + 2*x0*x2*x3 + 2*x1*x2*x3 + x2^2*x3 + x0*x3^2 + x1*x3^2 + x2*x3^2
                sage: a.expand(2, alphabet='y')
                y0^2*y1 + y0*y1^2
                sage: a.expand(2, alphabet=['a','b'])
                a^2*b + a*b^2
                sage: s([1,1,1,1]).expand(3)
                0
                sage: (s([]) + 2*s([1])).expand(3)
                2*x0 + 2*x1 + 2*x2 + 1
                sage: s([1]).expand(0)
                0
                sage: (3*s([])).expand(0)
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

            For `q=1` we use the formula from Corollary 7.21.4 of [EnumComb2]_:

            .. MATH::

                ps_{n,1}(s_\\lambda) = \\prod_{u\\in\\lambda} (n+c(u)) / h(u),

            where `h(u)` is the hook length of a cell `u` in `\\lambda`,
            and where `c(u)` is the content of a cell `u` in `\\lambda`.

            For `n=infinity` we use the formula from Corollary 7.21.3 of [EnumComb2]_

            .. MATH::

                ps_q(s_\\lambda) = q^{\\sum_i (i-1)\\lambda_i} / \\prod_{u\\in\\lambda} (1-q^{h(u)}).

            Otherwise, we use the formula from Theorem 7.21.2 of [EnumComb2]_,

            .. MATH::

                ps_{n,q}(s_\\lambda) = q^{\\sum_i (i-1)\\lambda_i}
                                      \\prod_{u\\in\\lambda} (1-q^{n+c(u)})/(1-q^{h(u)}).

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: x = s[2]
                sage: x.principal_specialization(3)
                q^4 + q^3 + 2*q^2 + q + 1

                sage: x = 3*s[2,2] + 2*s[1] + 1
                sage: x.principal_specialization(3, q=var("q"))                         # needs sage.symbolic
                3*(q^4 - 1)*(q^3 - 1)*q^2/((q^2 - 1)*(q - 1)) + 2*(q^3 - 1)/(q - 1) + 1

                sage: x.principal_specialization(q=var("q"))                            # needs sage.symbolic
                -2/(q - 1) + 3*q^2/((q^3 - 1)*(q^2 - 1)^2*(q - 1)) + 1

            TESTS::

                sage: s.zero().principal_specialization(3)
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

            - ``q`` -- (default: `1`) the value to use for `q`.  If
              ``q`` is ``None``, then a ring (or fraction field) of
              polynomials in ``q`` is created.

            We use the formula in the proof of Corollary 7.21.6 of
            [EnumComb2]_

            .. MATH::

                ex_{q}(s_\\lambda) = t^{|\\lambda|} q^{\\sum_i (i-1)\\lambda_i}
                                      / \\prod_{u\\in\\lambda} (1 + q + q^2 + \\dots + q^{h(u)-1})

            where `h(u)` is the hook length of a cell `u` in `\\lambda`.

            As a limit case, we obtain a formula for `q=1`

            .. MATH::

                ex_{1}(s_\\lambda) = f^\\lambda t^{|\\lambda|} / |\\lambda|!

            where `f^\\lambda` is the number of standard Young
            tableaux of shape `\\lambda`.

            EXAMPLES::

                sage: s = SymmetricFunctions(QQ).s()
                sage: x = s[5,3]
                sage: x.exponential_specialization()
                1/1440*t^8

                sage: x = 5*s[1,1,1] + 3*s[2,1] + 1
                sage: x.exponential_specialization()
                11/6*t^3 + 1

            We also support the `q`-exponential_specialization::

                sage: factor(s[3].exponential_specialization(q=var("q"), t=var("t")))   # needs sage.symbolic
                t^3/((q^2 + q + 1)*(q + 1))

            TESTS::

                sage: s.zero().exponential_specialization()
                0
            '''
