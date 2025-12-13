from . import multiplicative as multiplicative
from sage.misc.cachefunc import cached_method as cached_method

class SymmetricFunctionAlgebra_AbreuNigro(multiplicative.SymmetricFunctionAlgebra_multiplicative):
    """
    The Abreu-Nigro (symmetric function) basis.

    The Abreu-Nigro basis `\\{\\rho_{\\lambda}(x; q)\\}_{\\lambda}` is the
    multiplicative basis defined by

    .. MATH::

        [n]_q h_n(x) = \\sum_{i=1}^n h_{n-i}(x) \\rho_i(x; q),
        \\qquad\\qquad
        \\rho_{\\lambda}(x; q) = \\rho_{\\lambda_1}(x; q) \\rho_{\\lambda_2}(x; q)
        \\cdots \\rho_{\\lambda_{\\ell}}(x; q).

    Here `[n]_q = 1 + q + \\cdots + q^{n-1}` is a `q`-integer.
    An alternative definition is given by
    `\\rho_n = q^{n-1} P_n(x; q^{-1})`, where `P_n(x; q)` is the
    Hall-Littlewood `P` function for the one-row partition `n`.

    INPUT:

    - ``Sym`` -- the ring of the symmetric functions
    - ``q`` -- the parameter `q`

    REFERENCES:

    - [AN2021]_
    - [AN2021II]_
    - [AN2023]_

    EXAMPLES:

    We verify the change of basis formula for the first few `n`::

        sage: q = ZZ['q'].fraction_field().gen()
        sage: Sym = SymmetricFunctions(q.parent())
        sage: an = Sym.abreu_nigro(q)
        sage: h = Sym.h()
        sage: from sage.combinat.q_analogues import q_int, q_factorial
        sage: all(q_int(n, q) * h[n] == sum(h[n-i] * an[i] for i in range(1,n+1))
        ....:     for n in range(1, 5))
        True

        sage: P = Sym.hall_littlewood(q).P()
        sage: all(h(P[n]).map_coefficients(lambda c: q^(n-1) * c(q=~q)) == h(an[n])
        ....:     for n in range(1, 6))
        True

    Next, we give the expansion in a few other bases::

        sage: p = Sym.p()
        sage: s = Sym.s()
        sage: m = Sym.m()
        sage: e = Sym.e()

        sage: p(an([1]))
        p[1]
        sage: m(an([1]))
        m[1]
        sage: e(an([1]))
        e[1]
        sage: h(an([1]))
        h[1]
        sage: s(an([1]))
        s[1]

        sage: p(an([2]))
        ((q-1)/2)*p[1, 1] + ((q+1)/2)*p[2]
        sage: m(an([2]))
        (q-1)*m[1, 1] + q*m[2]
        sage: e(an([2]))
        q*e[1, 1] + (-q-1)*e[2]
        sage: h(an([2]))
        -h[1, 1] + (q+1)*h[2]
        sage: s(an([2]))
        -s[1, 1] + q*s[2]

        sage: p(an([3]))
        ((q^2-2*q+1)/6)*p[1, 1, 1] + ((q^2-1)/2)*p[2, 1] + ((q^2+q+1)/3)*p[3]
        sage: m(an([3]))
        (q^2-2*q+1)*m[1, 1, 1] + (q^2-q)*m[2, 1] + q^2*m[3]
        sage: e(an([3]))
        q^2*e[1, 1, 1] + (-2*q^2-q)*e[2, 1] + (q^2+q+1)*e[3]
        sage: h(an([3]))
        h[1, 1, 1] + (-q-2)*h[2, 1] + (q^2+q+1)*h[3]
        sage: s(an([3]))
        s[1, 1, 1] - q*s[2, 1] + q^2*s[3]

    Some examples of conversions the other way::

        sage: q_int(3, q) * an(h[3])
        (1/(q+1))*an[1, 1, 1] + ((q+2)/(q+1))*an[2, 1] + an[3]
        sage: q_int(3, q) * an(e[3])
        (q^3/(q+1))*an[1, 1, 1] + ((-2*q^2-q)/(q+1))*an[2, 1] + an[3]
        sage: q_int(3, q) * an(m[2,1])
        ((-2*q^3+q^2+q)/(q+1))*an[1, 1, 1] + ((5*q^2+2*q-1)/(q+1))*an[2, 1] - 3*an[3]
        sage: q_int(3, q) * an(p[3])
        (q^2-2*q+1)*an[1, 1, 1] + (-3*q+3)*an[2, 1] + 3*an[3]

    We verify the determinant formulas of [AN2021II]_ Proposition 2.1, but
    correcting a parity issue with (3)::

        sage: def h_det(n):
        ....:     ret = matrix.zero(an, n)
        ....:     for i in range(n):
        ....:         if i != 0:
        ....:             ret[i,i-1] = -q_int(i)
        ....:         for j in range(i, n):
        ....:             ret[i,j] = an[j-i+1]
        ....:     return ret.det()
        sage: all(q_factorial(n, q) * h[n] == h(h_det(n)) for n in range(6))
        True
        sage: all(q_factorial(n, q) * an(h[n]) == h_det(n) for n in range(6))
        True

        sage: def rho_det(n):
        ....:     ret = matrix.zero(h, n)
        ....:     for i in range(n):
        ....:         if i == 0:
        ....:             for j in range(n):
        ....:                 ret[0,j] = q_int(j+1, q) * h[j+1]
        ....:         else:
        ....:             for j in range(i-1, n):
        ....:                 ret[i,j] = h[j-i+1]
        ....:     return ret.det()
        sage: all((-1)^(n+1) * an[n] == an(rho_det(n)) for n in range(1, 6))
        True
        sage: all((-1)^(n+1) * h(an[n]) == rho_det(n) for n in range(1, 6))
        True

    Antipodes::

        sage: an([1]).antipode()
        -an[1]
        sage: an([2]).antipode()
        (q-1)*an[1, 1] - an[2]
        sage: an([3]).antipode()
        (-q^2+2*q-1)*an[1, 1, 1] + (2*q-2)*an[2, 1] - an[3]

    For single row partitions, the antipode is given by the formula
    `S(\\rho_n(x; q)) = -P_n(x; q)`, where `P_n`
    is the Hall-Littlewood P-function::

        sage: P = Sym.hall_littlewood(q).P()
        sage: all(P(an[n].antipode()) == -P[n] for n in range(1, 6))
        True
    """
    @staticmethod
    def __classcall_private__(cls, Sym, q: str = 'q'):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: Sym = SymmetricFunctions(q.parent())
            sage: Sym.abreu_nigro(q) is Sym.abreu_nigro('q')
            True
        """
    def __init__(self, Sym, q) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: Sym = SymmetricFunctions(q.parent())
            sage: an = Sym.abreu_nigro(q)
            sage: TestSuite(an).run(skip=['_test_associativity', '_test_distributivity', '_test_prod'])
            sage: TestSuite(an).run(elements=[an[1,1]+an[2], an[1]+2*an[1,1]])
            sage: latex(an[2,1])
            \\rho_{2,1}
        """
    def coproduct_on_generators(self, n):
        """
        Return the coproduct on the ``n``-th generator of ``self``.

        For any `n \\geq 1`, we have

        .. MATH::

            \\Delta(\\rho_n) = \\rho_0 \\otimes \\rho_n
            + (q-1) \\sum_{k=1}^{n-1} \\rho_k \\otimes \\rho_{n-k}
            + \\rho_n \\otimes \\rho_0.

        INPUT:

        - ``n`` -- a nonnegative integer

        OUTPUT:

        an element of the tensor squared of the basis ``self``

        EXAMPLES::

            sage: q = ZZ['q'].fraction_field().gen()
            sage: Sym = SymmetricFunctions(q.parent())
            sage: h = Sym.h()
            sage: an = Sym.abreu_nigro(q)
            sage: an.coproduct_on_generators(2)
            an[] # an[2] + (q-1)*an[1] # an[1] + an[2] # an[]
            sage: an[2].coproduct()
            an[] # an[2] + (q-1)*an[1] # an[1] + an[2] # an[]
            sage: an.coproduct(an[2])
            an[] # an[2] + (q-1)*an[1] # an[1] + an[2] # an[]
            sage: an.tensor_square()(h(an[5]).coproduct()) == an[5].coproduct()
            True
            sage: an[2,1].coproduct()
            an[] # an[2, 1] + (q-1)*an[1] # an[1, 1] + an[1] # an[2]
             + (q-1)*an[1, 1] # an[1] + an[2] # an[1] + an[2, 1] # an[]
            sage: an.tensor_square()(h(an[2,1]).coproduct())
            an[] # an[2, 1] + (q-1)*an[1] # an[1, 1] + an[1] # an[2]
             + (q-1)*an[1, 1] # an[1] + an[2] # an[1] + an[2, 1] # an[]
        """
