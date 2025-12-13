from . import multiplicative as multiplicative
from sage.arith.misc import divisors as divisors
from sage.combinat.integer_lists.invlex import IntegerListsLex as IntegerListsLex
from sage.combinat.partitions import ZS1_iterator as ZS1_iterator
from sage.misc.cachefunc import cached_method as cached_method

class SymmetricFunctionAlgebra_witt(multiplicative.SymmetricFunctionAlgebra_multiplicative):
    """
    The Witt symmetric function basis (or Witt basis, to be short).

    The Witt basis of the ring of symmetric functions is
    denoted by `(x_{\\lambda})` in [HazWitt1]_, section 9.63, and by
    `(q_{\\lambda})` in [DoranIV1996]_. We will denote this basis by
    `(w_{\\lambda})` (which is precisely how it is denoted in
    [GriRei18]_, Exercise 2.9.3(d)). It is a multiplicative basis
    (meaning that `w_{\\emptyset} = 1` and that every partition
    `\\lambda` satisfies
    `w_{\\lambda} = w_{\\lambda_1} w_{\\lambda_2} w_{\\lambda_3} \\cdots`,
    where `w_i` means `w_{(i)}` for every nonnegative integer `i`).

    This basis can be defined in various ways. Probably the most
    well-known one is using the equation

    .. MATH::

        \\prod_{d=1}^{\\infty} (1 - w_d t^d)^{-1} = \\sum_{n=0}^{\\infty} h_n t^n

    where `t` is a formal variable and `h_n` are the complete
    homogeneous symmetric functions, extended to `0` by `h_0 = 1`.
    This equation allows one to uniquely determine the functions
    `w_1, w_2, w_3, \\ldots` by recursion; one consequently extends the
    definition to all `w_{\\lambda}` by requiring multiplicativity.

    A way to rewrite the above equation without power series is:

    .. MATH::

        h_n = \\sum_{\\lambda \\vdash n} w_{\\lambda}

    for all nonnegative integers `n`, where `\\lambda \\vdash n` means
    that `\\lambda` is a partition of `n`.

    A similar equation (which is easily seen to be equivalent to the
    former) is

    .. MATH::

        e_n = \\sum_{\\lambda} (-1)^{n - \\ell(\\lambda)} w_{\\lambda},

    with the sum running only over *strict* partitions `\\lambda` of
    `n` this time. This equation can also be used to recursively
    define the `w_n`. Furthermore, every positive integer `n`
    satisfies

    .. MATH::

        p_n = \\sum_{d\\mid n} d w_d^{n/d},

    and this can be used to define the `w_n` recursively over any
    ring which is torsion-free as a `\\ZZ`-module. While these
    equations all yield easy formulas for classical bases of the
    ring of symmetric functions in terms of the Witt symmetric
    functions, it seems difficult to obtain explicit formulas in
    the other direction.

    The Witt symmetric functions owe their name to the fact that
    the ring of symmetric functions can be viewed as the coordinate
    ring of the group scheme of Witt vectors, and the Witt
    symmetric functions are the functions that send a Witt vector
    to its components (whereas the powersum symmetric functions
    send a Witt vector to its ghost components). Details can be
    found in [HazWitt1]_ or section 3.2 of [BorWi2004]_.

    INPUT:

    - ``Sym`` -- an instance of the ring of the symmetric functions

    REFERENCES:

    .. [HazWitt1] Michiel Hazewinkel. *Witt vectors. Part 1*.
       :arxiv:`0804.3888v1`

    .. [DoranIV1996] William F. Doran IV.
       *A Proof of Reutenauer's `-q_{(n)}` Conjecture*.
       Journal of combinatorial theory, Series A 74, pp. 342-344 (1996),
       article no. 0056. :doi:`10.1006/jcta.1996.0056`

    .. [BorWi2004] James Borger, Ben Wieland.
       *Plethystic algebra*.
       :arxiv:`math/0407227v1`

    .. [GriRei18]_

    EXAMPLES:

    Here are the first few Witt symmetric functions, in various bases::

        sage: Sym = SymmetricFunctions(QQ)
        sage: w = Sym.w()
        sage: e = Sym.e()
        sage: h = Sym.h()
        sage: p = Sym.p()
        sage: s = Sym.s()
        sage: m = Sym.m()

        sage: p(w([1]))
        p[1]
        sage: m(w([1]))
        m[1]
        sage: e(w([1]))
        e[1]
        sage: h(w([1]))
        h[1]
        sage: s(w([1]))
        s[1]

        sage: p(w([2]))
        -1/2*p[1, 1] + 1/2*p[2]
        sage: m(w([2]))
        -m[1, 1]
        sage: e(w([2]))
        -e[2]
        sage: h(w([2]))
        -h[1, 1] + h[2]
        sage: s(w([2]))
        -s[1, 1]

        sage: p(w([3]))
        -1/3*p[1, 1, 1] + 1/3*p[3]
        sage: m(w([3]))
        -2*m[1, 1, 1] - m[2, 1]
        sage: e(w([3]))
        -e[2, 1] + e[3]
        sage: h(w([3]))
        -h[2, 1] + h[3]
        sage: s(w([3]))
        -s[2, 1]

        sage: Sym = SymmetricFunctions(ZZ)
        sage: w = Sym.w()
        sage: e = Sym.e()
        sage: h = Sym.h()
        sage: s = Sym.s()
        sage: m = Sym.m()
        sage: p = Sym.p()
        sage: m(w([4]))
        -9*m[1, 1, 1, 1] - 4*m[2, 1, 1] - 2*m[2, 2] - m[3, 1]
        sage: e(w([4]))
        -e[2, 1, 1] + e[3, 1] - e[4]
        sage: h(w([4]))
        -h[1, 1, 1, 1] + 2*h[2, 1, 1] - h[2, 2] - h[3, 1] + h[4]
        sage: s(w([4]))
        -s[1, 1, 1, 1] - s[2, 1, 1] - s[2, 2] - s[3, 1]

    Some examples of conversions the other way::

        sage: w(h[3])
        w[1, 1, 1] + w[2, 1] + w[3]
        sage: w(e[3])
        -w[2, 1] + w[3]
        sage: w(m[2,1])
        2*w[2, 1] - 3*w[3]
        sage: w(p[3])
        w[1, 1, 1] + 3*w[3]

    Antipodes::

        sage: w([1]).antipode()
        -w[1]
        sage: w([2]).antipode()
        -w[1, 1] - w[2]

    The following holds for all odd `i` and is easily proven by
    induction::

        sage: all(w([i]).antipode() == -w([i]) for i in range(1, 10, 2))
        True

    The Witt basis does not allow for simple expressions for
    comultiplication and antipode in general (this is related to the
    fact that the sum of two Witt vectors isn't easily described in
    terms of the components). Therefore, a number of computations with
    Witt symmetric functions pass through the complete homogeneous
    symmetric functions by default.
    """
    def __init__(self, Sym) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: w = SymmetricFunctions(QQ).w()
            sage: TestSuite(w).run(skip=['_test_associativity', '_test_distributivity', '_test_prod'])
            sage: TestSuite(w).run(elements=[w[1,1]+w[2], w[1]+2*w[1,1]])
        """
    def coproduct(self, elt):
        """
        Return the coproduct of the element ``elt``.

        INPUT:

        - ``elt`` -- a symmetric function written in this basis

        OUTPUT:

        The coproduct acting on ``elt``; the result is an element of the
        tensor squared of the basis ``self``.

        EXAMPLES::

            sage: w = SymmetricFunctions(QQ).w()
            sage: w[2].coproduct()
            w[] # w[2] - w[1] # w[1] + w[2] # w[]
            sage: w.coproduct(w[2])
            w[] # w[2] - w[1] # w[1] + w[2] # w[]
            sage: w[2,1].coproduct()
            w[] # w[2, 1] - w[1] # w[1, 1] + w[1] # w[2] - w[1, 1] # w[1] + w[2] # w[1] + w[2, 1] # w[]
            sage: w.coproduct(w[2,1])
            w[] # w[2, 1] - w[1] # w[1, 1] + w[1] # w[2] - w[1, 1] # w[1] + w[2] # w[1] + w[2, 1] # w[]
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
            \\quad \\mathbf{V}_n(e_r) = (-1)^{r - r/n} e_{r/n},
            \\quad \\mathbf{V}_n(w_r) = w_{r/n},

        (where `h` is the complete homogeneous basis, `p` is the
        powersum basis, `e` is the elementary basis, and `w` is the
        Witt basis). For every nonnegative integer `r` with `n \\nmid r`,
        it satisfes

        .. MATH::

            \\mathbf{V}_n(h_r) = \\mathbf{V}_n(p_r) = \\mathbf{V}_n(e_r)
            = \\mathbf{V}_n(w_r) = 0.

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

        The result of applying the `n`-th Verschiebung operator (on the
        ring of symmetric functions) to ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(ZZ)
            sage: w = Sym.w()
            sage: w[3].verschiebung(2)
            0
            sage: w[4].verschiebung(4)
            w[1]

        TESTS:

        Let us check that this method on the Witt basis gives the
        same result as the implementation in sfa.py on the complete
        homogeneous basis::

            sage: Sym = SymmetricFunctions(QQ)
            sage: w = Sym.w(); h = Sym.h()
            sage: all( w(h(lam)).verschiebung(3) == w(h(lam).verschiebung(3))
            ....:      for lam in Partitions(6) )
            True
            sage: all( h(w(lam)).verschiebung(2) == h(w(lam).verschiebung(2))
            ....:      for lam in Partitions(4) )
            True
        '''
    class Element(multiplicative.SymmetricFunctionAlgebra_multiplicative.Element):
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

            :meth:`omega_involution` is a synonym for the :meth:`omega`
            method.

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: w = Sym.w()
                sage: a = w([4,3,1,1]); a
                w[4, 3, 1, 1]
                sage: a.omega()
                -w[3, 1, 1, 1, 1, 1, 1] - w[3, 2, 1, 1, 1, 1]
                 - w[3, 2, 2, 1, 1] - w[4, 3, 1, 1]

                sage: h = Sym.h()
                sage: all(w(h(w[la]).omega()) == w[la].omega()
                ....:     for n in range(6) for la in Partitions(n))
                True
            """
