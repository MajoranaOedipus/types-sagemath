from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing

def q_int(n, q=None):
    '''
    Return the `q`-analog of the nonnegative integer `n`.

    The `q`-analog of the nonnegative integer `n` is given by

    .. MATH::

        [n]_q = \\frac{q^n - q^{-n}}{q - q^{-1}}
        = q^{n-1} + q^{n-3} + \\cdots + q^{-n+3} + q^{-n+1}.

    INPUT:

    - ``n`` -- the nonnegative integer `n` defined above
    - ``q`` -- (default: `q \\in \\ZZ[q, q^{-1}]`) the parameter `q`
      (should be invertible)

    If ``q`` is unspecified, then it defaults to using the generator `q`
    for a Laurent polynomial ring over the integers.

    .. NOTE::

        This is not the "usual" `q`-analog of `n` (or `q`-integer) but
        a variant useful for quantum groups. For the version used in
        combinatorics, see :mod:`sage.combinat.q_analogues`.

    EXAMPLES::

        sage: from sage.algebras.quantum_groups.q_numbers import q_int
        sage: q_int(2)
        q^-1 + q
        sage: q_int(3)
        q^-2 + 1 + q^2
        sage: q_int(5)
        q^-4 + q^-2 + 1 + q^2 + q^4
        sage: q_int(5, 1)
        5

    TESTS::

        sage: from sage.algebras.quantum_groups.q_numbers import q_int
        sage: q_int(1)
        1
        sage: q_int(0)
        0
    '''
def q_factorial(n, q=None):
    '''
    Return the `q`-analog of the factorial `n!`.

    The `q`-factorial is defined by:

    .. MATH::

        [n]_q! = [n]_q \\cdot [n-1]_q \\cdots [2]_q \\cdot [1]_q,

    where `[n]_q` denotes the `q`-integer defined in
    :func:`sage.algebras.quantum_groups.q_numbers.q_int()`.

    INPUT:

    - ``n`` -- the nonnegative integer `n` defined above
    - ``q`` -- (default: `q \\in \\ZZ[q, q^{-1}]`) the parameter `q`
      (should be invertible)

    If ``q`` is unspecified, then it defaults to using the generator `q`
    for a Laurent polynomial ring over the integers.

    .. NOTE::

        This is not the "usual" `q`-factorial but a variant
        useful for quantum groups. For the version used in
        combinatorics, see :mod:`sage.combinat.q_analogues`.

    EXAMPLES::

        sage: from sage.algebras.quantum_groups.q_numbers import q_factorial
        sage: q_factorial(3)
        q^-3 + 2*q^-1 + 2*q + q^3
        sage: p = LaurentPolynomialRing(QQ, \'q\').gen()
        sage: q_factorial(3, p)
        q^-3 + 2*q^-1 + 2*q + q^3
        sage: p = ZZ[\'p\'].gen()
        sage: q_factorial(3, p)
        (p^6 + 2*p^4 + 2*p^2 + 1)/p^3

    The `q`-analog of `n!` is only defined for `n` a nonnegative
    integer (:issue:`11411`)::

        sage: q_factorial(-2)
        Traceback (most recent call last):
        ...
        ValueError: argument (-2) must be a nonnegative integer
    '''
def q_binomial(n, k, q=None):
    '''
    Return the `q`-binomial coefficient.

    Let `[n]_q!` denote the `q`-factorial of `n` given by
    :meth:`sage.algebras.quantum_groups.q_numbers.q_factorial()`.
    The `q`-binomial coefficient is defined by

    .. MATH::

        \\begin{bmatrix} n \\\\ k \\end{bmatrix}_q
        = \\frac{[n]_q!}{[n-k]_q! \\cdot [k]_q!}.

    INPUT:

    - ``n``, ``k`` -- the nonnegative integers `n` and `k` defined above
    - ``q`` -- (default: `q \\in \\ZZ[q, q^{-1}]`) the parameter `q`
      (should be invertible)

    If ``q`` is unspecified, then it is taken to be the generator `q` for
    a Laurent polynomial ring over the integers.

    .. NOTE::

        This is not the "usual" `q`-binomial but a variant
        useful for quantum groups. For the version used in
        combinatorics, see :mod:`sage.combinat.q_analogues`.

    .. WARNING::

        This method uses division by `q`-factorials.
        If `[k]_q!` or `[n-k]_q!` are zero-divisors, or
        division is not implemented in the ring containing `q`,
        then it will not work.

    EXAMPLES::

        sage: from sage.algebras.quantum_groups.q_numbers import q_binomial
        sage: q_binomial(2, 1)
        q^-1 + q
        sage: q_binomial(2, 0)
        1
        sage: q_binomial(4, 1)
        q^-3 + q^-1 + q + q^3
        sage: q_binomial(4, 3)
        q^-3 + q^-1 + q + q^3

    TESTS::

        sage: from sage.algebras.quantum_groups.q_numbers import q_binomial
        sage: all(q_binomial(n, k, 1) == binomial(n, k)
        ....:     for n in range(6) for k in range(n+1))
        True
        sage: q_binomial(-2, 1)
        Traceback (most recent call last):
        ...
        ValueError: n must be nonnegative
    '''
