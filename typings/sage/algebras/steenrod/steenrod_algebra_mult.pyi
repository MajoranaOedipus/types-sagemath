from sage.misc.cachefunc import cached_function as cached_function

def milnor_multiplication(r, s):
    """
    Product of Milnor basis elements r and s at the prime 2.

    INPUT:

    - ``r`` -- tuple of nonnegative integers
    - ``s`` -- tuple of nonnegative integers

    OUTPUT:

    Dictionary of terms of the form (tuple: coeff), where
    'tuple' is a tuple of nonnegative integers and 'coeff' is 1.

    This computes Milnor matrices for the product of `\\text{Sq}(r)`
    and `\\text{Sq}(s)`, computes their multinomial coefficients, and
    for each matrix whose coefficient is 1, add `\\text{Sq}(t)` to the
    output, where `t` is the tuple formed by the diagonals sums from
    the matrix.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import milnor_multiplication
        sage: milnor_multiplication((2,), (1,)) == {(0, 1): 1, (3,): 1}
        True
        sage: sorted(milnor_multiplication((4,), (2,1)).items())
        [((0, 3), 1), ((2, 0, 1), 1), ((6, 1), 1)]
        sage: sorted(milnor_multiplication((2,4), (0,1)).items())
        [((2, 0, 0, 1), 1), ((2, 5), 1)]

    These examples correspond to the following product computations:

    .. MATH::

        \\text{Sq}(2) \\text{Sq}(1) = \\text{Sq}(0,1) + \\text{Sq}(3)

        \\text{Sq}(4) \\text{Sq}(2,1) = \\text{Sq}(6,1) + \\text{Sq}(0,3) + \\text{Sq}(2,0,1)

        \\text{Sq}(2,4) \\text{Sq}(0,1) = \\text{Sq}(2, 5) + \\text{Sq}(2, 0, 0, 1)

    This uses the same algorithm Monks does in his Maple package: see
    http://mathweb.scranton.edu/monks/software/Steenrod/steen.html.
    """
def multinomial(list):
    """
    Multinomial coefficient of list, mod 2.

    INPUT:

    - ``list`` -- list of integers

    OUTPUT: none if the multinomial coefficient is 0, or sum of list if it is 1

    Given the input `[n_1, n_2, n_3, ...]`, this computes the
    multinomial coefficient `(n_1 + n_2 + n_3 + ...)! / (n_1! n_2!
    n_3! ...)`, mod 2.  The method is roughly this: expand each
    `n_i` in binary.  If there is a 1 in the same digit for any `n_i`
    and `n_j` with `i\\neq j`, then the coefficient is 0; otherwise, it
    is 1.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import multinomial
        sage: multinomial([1,2,4])
        7
        sage: multinomial([1,2,5])
        sage: multinomial([1,2,12,192,256])
        463

    This function does not compute any factorials, so the following are
    actually reasonable to do::

        sage: multinomial([1,65536])
        65537
        sage: multinomial([4,65535])
        sage: multinomial([32768,65536])
        98304
    """
def milnor_multiplication_odd(m1, m2, p):
    """
    Product of Milnor basis elements defined by m1 and m2 at the odd prime p.

    INPUT:

    - ``m1`` -- pair of tuples (e,r), where e is an increasing tuple of
      nonnegative integers and r is a tuple of nonnegative integers
    - ``m2`` -- pair of tuples (f,s), same format as m1
    - ``p`` -- odd prime number

    OUTPUT:

    Dictionary of terms of the form (tuple: coeff), where 'tuple' is
    a pair of tuples, as for r and s, and 'coeff' is an integer mod p.

    This computes the product of the Milnor basis elements
    `Q_{e_1} Q_{e_2} ... P(r_1, r_2, ...)` and
    `Q_{f_1} Q_{f_2} ... P(s_1, s_2, ...)`.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import milnor_multiplication_odd
        sage: sorted(milnor_multiplication_odd(((0,2),(5,)), ((1,),(1,)), 5).items())
        [(((0, 1, 2), (0, 1)), 4), (((0, 1, 2), (6,)), 4)]
        sage: milnor_multiplication_odd(((0,2,4),()), ((1,3),()), 7)
        {((0, 1, 2, 3, 4), ()): 6}
        sage: milnor_multiplication_odd(((0,2,4),()), ((1,5),()), 7)
        {((0, 1, 2, 4, 5), ()): 1}
        sage: sorted(milnor_multiplication_odd(((),(6,)), ((),(2,)), 3).items())
        [(((), (0, 2)), 1), (((), (4, 1)), 1), (((), (8,)), 1)]

    These examples correspond to the following product computations:

    .. MATH::

        p=5: \\quad Q_0 Q_2 \\mathcal{P}(5) Q_1 \\mathcal{P}(1) = 4 Q_0 Q_1 Q_2 \\mathcal{P}(0,1) + 4 Q_0 Q_1 Q_2 \\mathcal{P}(6)

        p=7: \\quad (Q_0 Q_2 Q_4) (Q_1 Q_3) = 6 Q_0 Q_1 Q_2 Q_3 Q_4

        p=7: \\quad (Q_0 Q_2 Q_4) (Q_1 Q_5) = Q_0 Q_1 Q_2 Q_3 Q_5

        p=3: \\quad \\mathcal{P}(6) \\mathcal{P}(2) = \\mathcal{P}(0,2) + \\mathcal{P}(4,1) + \\mathcal{P}(8)

    The following used to fail until the trailing zeroes were
    eliminated in p_mono::

        sage: A = SteenrodAlgebra(3)
        sage: a = A.P(0,3); b = A.P(12); c = A.Q(1,2)
        sage: (a+b)*c == a*c + b*c
        True

    Test that the bug reported in :issue:`7212` has been fixed::

        sage: A.P(36,6)*A.P(27,9,81)
        2 P(13,21,83) + P(14,24,82) + P(17,20,83) + P(25,18,83) + P(26,21,82) + P(36,15,80,1) + P(49,12,83) + 2 P(50,15,82) + 2 P(53,11,83) + 2 P(63,15,81)

    Associativity once failed because of a sign error::

        sage: a,b,c = A.Q_exp(0,1), A.P(3), A.Q_exp(1,1)
        sage: (a*b)*c == a*(b*c)
        True

    This uses the same algorithm Monks does in his Maple package to
    iterate through the possible matrices: see
    http://mathweb.scranton.edu/monks/software/Steenrod/steen.html.
    """
def multinomial_odd(list, p):
    """
    Multinomial coefficient of list, mod p.

    INPUT:

    - ``list`` -- list of integers
    - ``p`` -- a prime number

    OUTPUT: associated multinomial coefficient, mod p

    Given the input `[n_1, n_2, n_3, ...]`, this computes the
    multinomial coefficient `(n_1 + n_2 + n_3 + ...)! / (n_1! n_2!
    n_3! ...)`, mod `p`.  The method is this: expand each `n_i` in
    base `p`: `n_i = \\sum_j p^j n_{ij}`.  Do the same for the sum of
    the `n_i`'s, which we call `m`: `m = \\sum_j p^j m_j`.  Then the
    multinomial coefficient is congruent, mod `p`, to the product of
    the multinomial coefficients `m_j! / (n_{1j}! n_{2j}! ...)`.

    Furthermore, any multinomial coefficient `m! / (n_1! n_2! ...)`
    can be computed as a product of binomial coefficients: it equals

    .. MATH::

       \\binom{n_1}{n_1} \\binom{n_1 + n_2}{n_2} \\binom{n_1 + n_2 + n_3}{n_3} ...

    This is convenient because Sage's binomial function returns
    integers, not rational numbers (as would be produced just by
    dividing factorials).

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import multinomial_odd
        sage: multinomial_odd([1,2,4], 2)
        1
        sage: multinomial_odd([1,2,4], 7)
        0
        sage: multinomial_odd([1,2,4], 11)
        6
        sage: multinomial_odd([1,2,4], 101)
        4
        sage: multinomial_odd([1,2,4], 107)
        105
    """
def binomial_mod2(n, k):
    """
    The binomial coefficient `\\binom{n}{k}`, computed mod 2.

    INPUT:

    - `n`, `k` -- integers

    OUTPUT: `n` choose `k`, mod 2

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import binomial_mod2
        sage: binomial_mod2(4,2)
        0
        sage: binomial_mod2(5,4)
        1
        sage: binomial_mod2(3 * 32768, 32768)
        1
        sage: binomial_mod2(4 * 32768, 32768)
        0
    """
def binomial_modp(n, k, p):
    """
    The binomial coefficient `\\binom{n}{k}`, computed mod `p`.

    INPUT:

    - `n`, `k` -- integers
    - ``p`` -- prime number

    OUTPUT: `n` choose `k`, mod `p`

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import binomial_modp
        sage: binomial_modp(5,2,3)
        1
        sage: binomial_modp(6,2,11)  # 6 choose 2 = 15
        4
    """
@cached_function
def adem(a, b, c: int = 0, p: int = 2, generic=None):
    """
    The mod `p` Adem relations.

    INPUT:

    - `a`, `b`, `c` -- nonnegative integers (optional); corresponding
      to either `P^a P^b` or (if `c` present) to `P^a \\beta^b P^c`
    - ``p`` -- positive prime number (default: 2)
    - ``generic`` -- whether to use the generic Steenrod algebra, (default: depends on prime)

    OUTPUT:

    a dictionary representing the mod `p` Adem relations
    applied to `P^a P^b` or (if `c` present) to `P^a \\beta^b P^c`.

    The mod `p` Adem relations for the mod `p` Steenrod algebra are as
    follows: if `p=2`, then if `a < 2b`,

    .. MATH::

       \\text{Sq}^a \\text{Sq}^b = \\sum_{j=0}^{a/2} \\binom{b-j-1}{a-2j} \\text{Sq}^{a+b-j} \\text{Sq}^j

    If `p` is odd, then if `a < pb`,

    .. MATH::

       P^a P^b = \\sum_{j=0}^{a/p} (-1)^{a+j} \\binom{(b-j)(p-1)-1}{a-pj} P^{a+b-j} P^j

    Also for `p` odd, if `a \\leq pb`,

    .. MATH::

       P^a \\beta P^b = \\sum_{j=0}^{a/p} (-1)^{a+j} \\binom{(b-j)(p-1)}{a-pj} \\beta P^{a+b-j} P^j
           + \\sum_{j=0}^{a/p} (-1)^{a+j-1} \\binom{(b-j)(p-1)-1}{a-pj-1} P^{a+b-j} \\beta P^j

    EXAMPLES:

    If two arguments (`a` and `b`) are given, then computations are
    done mod 2.  If `a \\geq 2b`, then the dictionary {(a,b): 1} is
    returned.  Otherwise, the right side of the mod 2 Adem relation
    for `\\text{Sq}^a \\text{Sq}^b` is returned.  For example, since
    `\\text{Sq}^2 \\text{Sq}^2 = \\text{Sq}^3 \\text{Sq}^1`, we have::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import adem
        sage: adem(2,2) # indirect doctest
        {(3, 1): 1}
        sage: adem(4,2)
        {(4, 2): 1}
        sage: adem(4,4) == {(6, 2): 1, (7, 1): 1}
        True

    If `p` is given and is odd, then with two inputs `a` and `b`, the
    Adem relation for `P^a P^b` is computed.  With three inputs `a`,
    `b`, `c`, the Adem relation for `P^a \\beta^b P^c` is computed.
    In either case, the keys in the output are all tuples of odd length,
    with ``(i_1, i_2, ..., i_m)`` representing

    .. MATH::

        \\beta^{i_1} P^{i_2} \\beta^{i_3} P^{i_4} ... \\beta^{i_m}

    For instance::

        sage: adem(3,1, p=3)
        {(0, 3, 0, 1, 0): 1}
        sage: adem(3,0,1, p=3)
        {(0, 3, 0, 1, 0): 1}
        sage: adem(1,0,1, p=7)
        {(0, 2, 0): 2}
        sage: adem(1,1,1, p=5) == {(0, 2, 1): 1, (1, 2, 0): 1}
        True
        sage: adem(1,1,2, p=5) == {(0, 3, 1): 1, (1, 3, 0): 2}
        True
    """
@cached_function
def make_mono_admissible(mono, p: int = 2, generic=None):
    """
    Given a tuple ``mono``, view it as a product of Steenrod
    operations, and return a dictionary giving data equivalent to
    writing that product as a linear combination of admissible
    monomials.

    When `p=2`, the sequence (and hence the corresponding monomial)
    `(i_1, i_2, ...)` is admissible if `i_j \\geq 2 i_{j+1}` for all
    `j`.

    When `p` is odd, the sequence `(e_1, i_1, e_2, i_2, ...)` is
    admissible if `i_j \\geq e_{j+1} + p i_{j+1}` for all `j`.

    INPUT:

    - ``mono`` -- tuple of nonnegative integers
    - ``p`` -- prime number (default: 2)
    - ``generic`` -- whether to use the generic Steenrod algebra (default: depends on prime)

    OUTPUT:

    Dictionary of terms of the form (tuple: coeff), where
    'tuple' is an admissible tuple of nonnegative integers and
    'coeff' is its coefficient.  This corresponds to a linear
    combination of admissible monomials.  When `p` is odd, each tuple
    must have an odd length: it should be of the form `(e_1, i_1, e_2,
    i_2, ..., e_k)` where each `e_j` is either 0 or 1 and each `i_j`
    is a positive integer: this corresponds to the admissible monomial

    .. MATH::

       \\beta^{e_1} \\mathcal{P}^{i_2} \\beta^{e_2} \\mathcal{P}^{i_2} ...
       \\mathcal{P}^{i_k} \\beta^{e_k}

    ALGORITHM:

    Given `(i_1, i_2, i_3, ...)`, apply the Adem relations to the first
    pair (or triple when `p` is odd) where the sequence is inadmissible,
    and then apply this function recursively to each of the resulting
    tuples `(i_1, ..., i_{j-1}, NEW, i_{j+2}, ...)`, keeping track of
    the coefficients.

    EXAMPLES::

        sage: from sage.algebras.steenrod.steenrod_algebra_mult import make_mono_admissible
        sage: make_mono_admissible((12,)) # already admissible, indirect doctest
        {(12,): 1}
        sage: make_mono_admissible((2,1)) # already admissible
        {(2, 1): 1}
        sage: make_mono_admissible((2,2))
        {(3, 1): 1}
        sage: make_mono_admissible((2, 2, 2))
        {(5, 1): 1}
        sage: make_mono_admissible((0, 2, 0, 1, 0), p=7)
        {(0, 3, 0): 3}

    Test the fix from :issue:`13796`::

        sage: SteenrodAlgebra(p=2, basis='adem').Q(2) * (Sq(6) * Sq(2)) # indirect doctest
        Sq^10 Sq^4 Sq^1 + Sq^10 Sq^5 + Sq^12 Sq^3 + Sq^13 Sq^2
    """
