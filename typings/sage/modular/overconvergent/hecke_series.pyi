from sage.arith.misc import valuation as valuation
from sage.functions.other import ceil as ceil, floor as floor
from sage.matrix.constructor import matrix as matrix, random_matrix as random_matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.functional import charpoly as charpoly, dimension as dimension, transpose as transpose
from sage.misc.timing import cputime as cputime
from sage.misc.verbose import verbose as verbose
from sage.modular.dims import dimension_modular_forms as dimension_modular_forms
from sage.modular.modform.all import ModularForms as ModularForms, ModularFormsRing as ModularFormsRing, delta_qexp as delta_qexp, eisenstein_series_qexp as eisenstein_series_qexp
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

def compute_G(p, F):
    """
    Given a power series `F \\in R[[q]]^\\times`, for some ring `R`, and an
    integer `p`, compute the quotient

    .. MATH::

        \\frac{F(q)}{F(q^p)}.

    Used by :func:`level1_UpGj` and by :func:`higher_level_UpGj`, with `F` equal
    to the Eisenstein series `E_{p-1}`.

    INPUT:

    - ``p`` -- integer
    - ``F`` -- power series (with invertible constant term)

    OUTPUT:

    the power series `F(q) / F(q^p)`, to the same precision as `F`

    EXAMPLES::

        sage: E = sage.modular.overconvergent.hecke_series.eisenstein_series_qexp(2, 12, Zmod(9),normalization='constant')
        sage: sage.modular.overconvergent.hecke_series.compute_G(3, E)
        1 + 3*q + 3*q^4 + 6*q^7 + O(q^12)
    """
def low_weight_bases(N, p, m, NN, weightbound):
    """
    Return a list of integral bases of modular forms of level `N` and (even)
    weight at most ``weightbound``, as `q`-expansions modulo `(p^m,q^{NN})`.

    These forms are obtained by reduction mod `p^m` from an integral basis in
    Hermite normal form (so they are not necessarily in reduced row echelon
    form mod `p^m`, but they are not far off).

    INPUT:

    - ``N`` -- positive integer (level)
    - ``p`` -- prime
    - ``m``, ``NN`` -- positive integers
    - ``weightbound`` -- (even) positive integer

    OUTPUT: list of lists of `q`-expansions modulo `(p^m,q^{NN})`

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import low_weight_bases
        sage: low_weight_bases(2, 5, 3, 5, 6)
        [[1 + 24*q + 24*q^2 + 96*q^3 + 24*q^4 + O(q^5)],
        [1 + 115*q^2 + 35*q^4 + O(q^5), q + 8*q^2 + 28*q^3 + 64*q^4 + O(q^5)],
        [1 + 121*q^2 + 118*q^4 + O(q^5), q + 32*q^2 + 119*q^3 + 24*q^4 + O(q^5)]]
    """
def random_low_weight_bases(N, p, m, NN, weightbound):
    """
    Return list of random integral bases of modular forms of level `N` and
    (even) weight at most weightbound with coefficients reduced modulo
    `(p^m,q^{NN})`.

    INPUT:

    - ``N`` -- positive integer (level)
    - ``p`` -- prime
    - ``m``, ``NN`` -- positive integers
    - ``weightbound`` -- (even) positive integer

    OUTPUT: list of lists of `q`-expansions modulo `(p^m,q^{NN})`

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import random_low_weight_bases
        sage: S = random_low_weight_bases(3, 7, 2, 5, 6); S # random
        [[4 + 48*q + 46*q^2 + 48*q^3 + 42*q^4 + O(q^5)],
        [3 + 5*q + 45*q^2 + 22*q^3 + 22*q^4 + O(q^5),
        1 + 3*q + 27*q^2 + 27*q^3 + 23*q^4 + O(q^5)],
        [2*q + 4*q^2 + 16*q^3 + 48*q^4 + O(q^5),
        2 + 6*q + q^2 + 3*q^3 + 43*q^4 + O(q^5),
        1 + 2*q + 6*q^2 + 14*q^3 + 4*q^4 + O(q^5)]]
        sage: S[0][0].parent()
        Power Series Ring in q over Ring of integers modulo 49
        sage: S[0][0].prec()
        5
    """
def low_weight_generators(N, p, m, NN):
    """
    Return a list of lists of modular forms, and an even natural number.

    The first output is a list of lists of modular forms reduced modulo
    `(p^m,q^{NN})` which generate the `(\\ZZ / p^m \\ZZ)`-algebra of mod `p^m`
    modular forms of weight at most 8, and the second output is the largest
    weight among the forms in the generating set.

    We (Alan Lauder and David Loeffler, the author and reviewer of this patch)
    conjecture that forms of weight at most 8 are always sufficient to generate
    the algebra of mod `p^m` modular forms of all weights. (We believe 6 to be
    sufficient, and we can prove that 4 is sufficient when there are no
    elliptic points, but using weights up to 8 acts as a consistency check.)

    INPUT:

    - ``N`` -- positive integer (level)
    - ``p`` -- prime
    - ``m``, ``NN`` -- positive integers

    OUTPUT: a tuple consisting of:

    - a list of lists of `q`-expansions modulo `(p^m,q^{NN})`,
    - an even natural number (twice the length of the list).

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import low_weight_generators
        sage: low_weight_generators(3, 7, 3, 10)
        ([[1 + 12*q + 36*q^2 + 12*q^3 + 84*q^4 + 72*q^5 + 36*q^6 + 96*q^7 + 180*q^8 + 12*q^9 + O(q^10)],
        [1 + 240*q^3 + 102*q^6 + 203*q^9 + O(q^10)],
        [1 + 182*q^3 + 175*q^6 + 161*q^9 + O(q^10)]], 6)
        sage: low_weight_generators(11, 5, 3, 10)
        ([[1 + 12*q^2 + 12*q^3 + 12*q^4 + 12*q^5 + 24*q^6 + 24*q^7 + 36*q^8 + 36*q^9 + O(q^10),
        q + 123*q^2 + 124*q^3 + 2*q^4 + q^5 + 2*q^6 + 123*q^7 + 123*q^9 + O(q^10)],
        [q + 116*q^4 + 115*q^5 + 102*q^6 + 121*q^7 + 96*q^8 + 106*q^9 + O(q^10)]], 4)
    """
def random_solution(B, K):
    """
    Return a random solution in nonnegative integers to the equation `a_1 + 2
    a_2 + 3 a_3 + ... + B a_B = K`, using a greedy algorithm.

    Note that this is *much* faster than using
    ``WeightedIntegerVectors.random_element()``.

    INPUT:

    - ``B``, ``K`` -- nonnegative integers

    OUTPUT: list

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import random_solution
        sage: s = random_solution(5, 10)
        sage: sum(s[i] * (i + 1) for i in range(5))
        10
        sage: S = set()
        sage: while len(S) != 30:
        ....:     s = random_solution(5, 10)
        ....:     assert sum(s[i] * (i + 1) for i in range(5)) == 10
        ....:     S.add(tuple(s))
    """
def ech_form(A, p):
    """
    Return echelon form of matrix ``A`` over the ring of integers modulo
    `p^m`, for some prime `p` and `m \\ge 1`.

    .. TODO::

        This should be moved to :mod:`sage.matrix.matrix_modn_dense` at some
        point.

    INPUT:

    - ``A`` -- matrix over ``Zmod(p^m)`` for some m
    - ``p`` -- prime p

    OUTPUT: matrix over ``Zmod(p^m)``

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import ech_form
        sage: A = MatrixSpace(Zmod(5 ** 3), 3)([1, 2, 3, 4, 5, 6, 7, 8, 9])
        sage: ech_form(A, 5)
        [1 2 3]
        [0 1 2]
        [0 0 0]
    """
def random_new_basis_modp(N, p, k, LWBModp, TotalBasisModp, elldash, bound):
    """
    Return a list of lists of lists ``[j, a]`` encoding a choice of basis for
    the `i`-th complementary space `W_i`, as explained in the documentation for the
    function :func:`complementary_spaces_modp`.

    INPUT:

    - ``N`` -- positive integer at least 2 and not divisible by `p` (level)
    - ``p`` -- prime at least 5
    - ``k`` -- nonnegative integer
    - ``LWBModp`` -- list of list of `q`-expansions modulo `(p,q^\\text{elldash})`
    - ``TotalBasisModp`` -- matrix over `\\mathrm{GF}(p)`
    - ``elldash`` -- positive integer
    - ``bound`` -- positive even integer (twice the length of the list ``LWBModp``)

    OUTPUT: list of lists of lists ``[j, a]``

    .. NOTE::

        As well as having a non-trivial return value, this function also
        modifies the input matrix ``TotalBasisModp``.

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import random_low_weight_bases, complementary_spaces_modp
        sage: LWB = random_low_weight_bases(2, 5, 2, 4, 6)
        sage: LWBModp = [ [f.change_ring(GF(5)) for f in x] for x in LWB]
        sage: complementary_spaces_modp(2, 5, 2, 3, 4, LWBModp, 4) # random, indirect doctest
        [[[[0, 0]]], [[[0, 0], [1, 1]]], [[[0, 0], [1, 0], [1, 1]]], [[[0, 0], [1, 0], [1, 1], [1, 1]]]]
    """
def complementary_spaces_modp(N, p, k0, n, elldash, LWBModp, bound):
    """
    Return a list of lists of lists of lists ``[j, a]``. The pairs ``[j, a]``
    encode the choice of the `a`-th element in the `j`-th list of the input
    ``LWBModp``, i.e., the `a`-th element in a particular basis modulo
    `(p,q^\\text{elldash})` for the space of modular forms of level
    `\\Gamma_0(N)` and weight `2(j+1)`. The list ``[[j_1, a_1], ...,[j_r, a_r]]``
    then encodes the product of the r modular forms associated to each
    ``[j_i, a_i]``; this has weight `k + (p-1)i` for some `0 \\le i \\le n`; here
    the `i` is such that this *list of lists* occurs in the `i`-th list of the
    output. The `i`-th list of the output thus encodes a choice of basis for the
    complementary space `W_i` which occurs in Step 2 of Algorithm 2 in [Lau2011]_.
    The idea is that one searches for this space `W_i` first modulo
    `(p,q^\\text{elldash})` and then, having found the correct products of
    generating forms, one can reconstruct these spaces modulo
    `(p^\\text{mdash},q^\\text{elldashp})` using the output of this function.
    (This idea is based upon a suggestion of John Voight.)

    INPUT:

    - ``N`` -- positive integer at least 2 and not divisible by `p` (level)
    - ``p`` -- prime at least 5
    - ``k0`` -- integer in range 0 to `p-1`
    - ``n``, ``elldash`` -- positive integers
    - ``LWBModp`` -- list of lists of `q`-expansions over `GF(p)`
    - ``bound`` -- positive even integer (twice the length of the list ``LWBModp``)

    OUTPUT: list of list of list of lists

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import random_low_weight_bases, complementary_spaces_modp
        sage: LWB = random_low_weight_bases(2, 5, 2, 4, 6)
        sage: LWBModp = [[f.change_ring(Zmod(5)) for f in x] for x in LWB]
        sage: complementary_spaces_modp(2, 5, 0, 3, 4, LWBModp, 6) # random, indirect doctest
        [[[]], [[[0, 0], [0, 0]]], [[[0, 0], [2, 1]]], [[[0, 0], [0, 0], [0, 0], [2, 1]]]]
    """
def complementary_spaces(N, p, k0, n, mdash, elldashp, elldash, modformsring, bound):
    """
    Return a list ``Ws``, each element in which is a list ``Wi`` of
    `q`-expansions modulo `(p^\\text{mdash},q^\\text{elldashp})`. The list ``Wi`` is
    a basis for a choice of complementary space in level `\\Gamma_0(N)` and
    weight `k` to the image of weight `k - (p-1)` forms under multiplication by
    the Eisenstein series `E_{p-1}`.

    The lists ``Wi`` play the same role as `W_i` in Step 2 of Algorithm 2 in
    [Lau2011]_. (The parameters ``k0, n, mdash, elldash, elldashp = elldash * p`` are
    defined as in Step 1 of that algorithm when this function is used in
    :func:`hecke_series`.) However, the complementary spaces are computed in a
    different manner, combining a suggestion of David Loeffler with one of John
    Voight. That is, one builds these spaces recursively using random products
    of forms in low weight, first searching for suitable products modulo
    `(p,q^\\text{elldash})`, and then later reconstructing only the required
    products to the full precision modulo `(p^\\text{mdash},q^\\text{elldashp})`. The
    forms in low weight are chosen from either bases of all forms up to weight
    ``bound`` or from a (tentative) generating set for the ring of all modular
    forms, according to whether ``modformsring`` is ``False`` or ``True``.

    INPUT:

    - ``N`` -- positive integer at least 2 and not divisible by p (level)
    - ``p`` -- prime at least 5
    - ``k0`` -- integer in range 0 to `p - 1`
    - ``n``, ``mdash``, ``elldashp``, ``elldash`` -- positive integers
    - ``modformsring`` -- boolean
    - ``bound`` -- positive (even) integer (ignored if ``modformsring`` is True)

    OUTPUT:

    - list of lists of `q`-expansions modulo
      `(p^\\text{mdash},q^\\text{elldashp})`.

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import complementary_spaces
        sage: complementary_spaces(2, 5, 0, 3, 2, 5, 4, True, 6) # random
        [[1],
        [1 + 23*q + 24*q^2 + 19*q^3 + 7*q^4 + O(q^5)],
        [1 + 21*q + 2*q^2 + 17*q^3 + 14*q^4 + O(q^5)],
        [1 + 19*q + 9*q^2 + 11*q^3 + 9*q^4 + O(q^5)]]
        sage: complementary_spaces(2, 5, 0, 3, 2, 5, 4, False, 6) # random
        [[1],
        [3 + 4*q + 2*q^2 + 12*q^3 + 11*q^4 + O(q^5)],
        [2 + 2*q + 14*q^2 + 19*q^3 + 18*q^4 + O(q^5)],
        [6 + 8*q + 10*q^2 + 23*q^3 + 4*q^4 + O(q^5)]]
    """
def higher_level_katz_exp(p, N, k0, m, mdash, elldash, elldashp, modformsring, bound):
    """
    Return a matrix `e` of size ``ell x elldashp`` over the integers modulo
    `p^\\text{mdash}`, and the Eisenstein series `E_{p-1} = 1 + .\\dots \\bmod
    (p^\\text{mdash},q^\\text{elldashp})`. The matrix `e` contains the coefficients
    of the elements `e_{i,s}` in the Katz expansions basis in Step 3 of
    Algorithm 2 in [Lau2011]_ when one takes as input to that algorithm
    `p, N, m` and `k` and define ``k0``, ``mdash``, ``n``, ``elldash``,
    ``elldashp = ell * dashp`` as in Step 1.

    INPUT:

    - ``p`` -- prime at least 5
    - ``N`` -- positive integer at least 2 and not divisible by `p` (level)
    - ``k0`` -- integer in range 0 to `p-1`
    - ``m``, ``mdash, ``elldash``, ``elldashp`` -- positive integers
    - ``modformsring`` -- boolean
    - ``bound`` -- positive (even) integer

    OUTPUT: matrix and `q`-expansion

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import higher_level_katz_exp
        sage: e, Ep1 = higher_level_katz_exp(5, 2, 0, 1, 2, 4, 20, True, 6)
        sage: e
        [ 1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
        [ 0  1 18 23 19  6  9  9 17  7  3 17 12  8 22  8 11 19  1  5]
        [ 0  0  1 11 20 16  0  8  4  0 18 15 24  6 15 23  5 18  7 15]
        [ 0  0  0  1  4 16 23 13  6  5 23  5  2 16  4 18 10 23  5 15]
        sage: Ep1
        1 + 15*q + 10*q^2 + 20*q^3 + 20*q^4 + 15*q^5 + 5*q^6 + 10*q^7 +
        5*q^9 + 10*q^10 + 5*q^11 + 10*q^12 + 20*q^13 + 15*q^14 + 20*q^15 + 15*q^16 +
        10*q^17 + 20*q^18 + O(q^20)
    """
def compute_elldash(p, N, k0, n):
    '''
    Return the "Sturm bound" for the space of modular forms of level
    `\\Gamma_0(N)` and weight `k_0 + n(p-1)`.

    .. SEEALSO::

        :meth:`~sage.modular.modform.space.ModularFormsSpace.sturm_bound`

    INPUT:

    - ``p`` -- prime
    - ``N`` -- positive integer (level)
    - ``k0``, ``n`` -- nonnegative integers not both zero

    OUTPUT: positive integer

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import compute_elldash
        sage: compute_elldash(11, 5, 4, 10)
        53
    '''
def hecke_series_degree_bound(p, N, k, m):
    """
    Return the ``Wan bound`` on the degree of the characteristic series of the
    Atkin operator on `p`-adic overconvergent modular forms of level
    `\\Gamma_0(N)` and weight `k` when reduced modulo `p^m`.

    This bound depends only upon `p, k \\pmod{p-1}`, and `N`. It uses Lemma 3.1 in
    [Wan1998]_.

    INPUT:

    - ``p`` -- prime at least 5
    - ``N`` -- positive integer not divisible by `p`
    - ``k`` -- even integer
    - ``m`` -- positive integer

    OUTPUT: nonnegative integer

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import hecke_series_degree_bound
        sage: hecke_series_degree_bound(13,11,100,5)
        39
    """
def higher_level_UpGj(p, N, klist, m, modformsring, bound, extra_data: bool = False):
    """
    Return a list ``[A_k]`` of square matrices over ``IntegerRing(p^m)``
    parameterised by the weights `k` in ``klist``.

    The matrix `A_k` is the finite square matrix which occurs on input
    `p, k, N` and `m` in Step 6 of Algorithm 2 in [Lau2011]_.

    Notational change from paper: In Step 1 following Wan we defined
    `j` by `k = k_0 + j(p-1)` with `0 \\le k_0 < p-1`. Here we replace `j` by
    ``kdiv`` so that we may use `j` as a column index for matrices.)

    INPUT:

    - ``p`` -- prime at least 5
    - ``N`` -- integer at least 2 and not divisible by `p` (level)
    - ``klist`` -- list of integers all congruent modulo `(p-1)` (the weights)
    - ``m`` -- positive integer
    - ``modformsring`` -- boolean
    - ``bound`` -- (even) positive integer
    - ``extra_data`` -- boolean (default: ``False``)

    OUTPUT:

    - list of square matrices. If ``extra_data`` is ``True``, return also
      extra intermediate data, namely the matrix `E` in [Lau2011]_ and
      the integers ``elldash`` and ``mdash``.

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import higher_level_UpGj
        sage: A = Matrix([
        ....:     [1,  0,  0,  0,  0,  0],
        ....:     [0,  1,  0,  0,  0,  0],
        ....:     [0,  7,  0,  0,  0,  0],
        ....:     [0,  5, 10, 20,  0,  0],
        ....:     [0,  7, 20,  0, 20,  0],
        ....:     [0,  1, 24,  0, 20,  0]])
        sage: B = Matrix([
        ....:     [1,  0,  0,  0,  0,  0],
        ....:     [0,  1,  0,  0,  0,  0],
        ....:     [0,  7,  0,  0,  0,  0],
        ....:     [0, 19,  0, 20,  0,  0],
        ....:     [0,  7, 20,  0, 20,  0],
        ....:     [0,  1, 24,  0, 20,  0]])
        sage: C = higher_level_UpGj(5, 3, [4], 2, True, 6)
        sage: len(C)
        1
        sage: C[0] in (A, B)
        True
        sage: len(higher_level_UpGj(5, 3, [4], 2, True, 6, extra_data=True))
        4
    """
def compute_Wi(k, p, h, hj, E4, E6):
    """
    This function computes a list `W_i` of `q`-expansions, together with an
    auxiliary quantity `h^j` (see below) which is to be used on the next
    call of this function. (The precision is that of input `q`-expansions.)

    The list `W_i` is a certain subset of a basis of the modular forms of
    weight `k` and level 1. Suppose `(a, b)` is the pair of nonnegative
    integers with `4a + 6b = k` and `a` minimal among such pairs. Then this
    space has a basis given by

    .. MATH::

        \\{ \\Delta^j E_6^{b - 2j} E_4^a : 0 \\le j < d\\}

    where `d` is the dimension.

    What this function returns is the subset of the above basis corresponding
    to `e \\le j < d` where `e` is the dimension of the space of modular forms
    of weight `k - (p-1)`. This set is a basis for the complement of the image
    of the weight `k - (p-1)` forms under multiplication by `E_{p-1}`.

    This function is used repeatedly in the construction of the Katz expansion
    basis. Hence considerable care is taken to reuse steps in the computation
    wherever possible: we keep track of powers of the form `h = \\Delta /
    E_6^2`.

    INPUT:

    - ``k`` -- nonnegative integer
    - ``p`` -- prime at least 5
    - ``h`` -- `q`-expansion of `h` (to some finite precision)
    - ``hj`` -- `q`-expansion of `h^j` where `j` is the dimension of the space of
      modular forms of level 1 and weight `k - (p-1)` (to same finite
      precision)
    - ``E4`` -- `q`-expansion of `E_4` (to same finite precision)
    - ``E6`` -- `q`-expansion of `E_6` (to same finite precision)

    The Eisenstein series `q`-expansions should be normalized to have constant
    term 1.

    OUTPUT:

    - list of `q`-expansions (to same finite precision), and `q`-expansion.

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import compute_Wi
        sage: p = 17
        sage: prec = 10
        sage: k = 24
        sage: S = Zmod(17^3)
        sage: E4 = eisenstein_series_qexp(4, prec, K=S, normalization='constant')
        sage: E6 = eisenstein_series_qexp(6, prec, K=S, normalization='constant')
        sage: h = delta_qexp(prec, K=S) / E6^2
        sage: from sage.modular.dims import dimension_modular_forms
        sage: j = dimension_modular_forms(1, k - (p - 1))
        sage: hj = h ** j
        sage: c = compute_Wi(k, p, h, hj, E4, E6); c
        ([q + 3881*q^2 + 4459*q^3 + 4665*q^4 + 2966*q^5 + 1902*q^6 + 1350*q^7 + 3836*q^8 + 1752*q^9 + O(q^10), q^2 + 4865*q^3 + 1080*q^4 + 4612*q^5 + 1343*q^6 + 1689*q^7 + 3876*q^8 + 1381*q^9 + O(q^10)], q^3 + 2952*q^4 + 1278*q^5 + 3225*q^6 + 1286*q^7 + 589*q^8 + 122*q^9 + O(q^10))
        sage: c == ([delta_qexp(10) * E6^2, delta_qexp(10)^2], h**3)
        True
    """
def katz_expansions(k0, p, ellp, mdash, n):
    """
    Return a list `e` of `q`-expansions, and the Eisenstein series `E_{p-1} = 1 +
    \\dots`, all modulo `(p^\\text{mdash},q^\\text{ellp})`. The list `e` contains
    the elements `e_{i,s}` in the Katz expansions basis in Step 3 of Algorithm
    1 in [Lau2011]_ when one takes as input to that algorithm `p,m` and `k` and define
    ``k0``, ``mdash``, ``n``, ``ellp = ell * p`` as in Step 1.

    INPUT:

    - ``k0`` -- integer in range 0 to `p - 1`
    - ``p`` -- prime at least 5
    - ``ellp``, ``mdash``, ``n`` -- positive integers

    OUTPUT:

    - list of `q`-expansions and the Eisenstein series `E_{p-1}` modulo
      `(p^\\text{mdash},q^\\text{ellp})`.

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import katz_expansions
        sage: katz_expansions(0, 5, 10, 3, 4)
        ([1 + O(q^10), q + 6*q^2 + 27*q^3 + 98*q^4 + 65*q^5 + 37*q^6 + 81*q^7 + 85*q^8 + 62*q^9 + O(q^10)],
        1 + 115*q + 35*q^2 + 95*q^3 + 20*q^4 + 115*q^5 + 105*q^6 + 60*q^7 + 25*q^8 + 55*q^9 + O(q^10))
    """
def level1_UpGj(p, klist, m, extra_data: bool = False):
    """
    Return a list `[A_k]` of square matrices over ``IntegerRing(p^m)``
    parameterised by the weights `k` in ``klist``.

    The matrix `A_k` is the finite square matrix which occurs on input
    `p, k` and `m` in Step 6 of Algorithm 1 in [Lau2011]_.

    Notational change from paper: In Step 1 following Wan we defined
    `j` by `k = k_0 + j(p-1)` with `0 \\le k_0 < p-1`. Here we replace `j` by
    ``kdiv`` so that we may use `j` as a column index for matrices.

    INPUT:

    - ``p`` -- prime at least 5
    - ``klist`` -- list of integers congruent modulo `(p-1)` (the weights)
    - ``m`` -- positive integer
    - ``extra_data`` -- boolean (default: ``False``)

    OUTPUT:

    - list of square matrices. If ``extra_data`` is ``True``, return also
      extra intermediate data, namely the matrix `E` in [Lau2011]_ and
      the integers ``elldash`` and ``mdash``.

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import level1_UpGj
        sage: level1_UpGj(7, [100], 5)
        [
        [    1   980  4802     0     0]
        [    0 13727 14406     0     0]
        [    0 13440  7203     0     0]
        [    0  1995  4802     0     0]
        [    0  9212 14406     0     0]
        ]
        sage: len(level1_UpGj(7, [100], 5, extra_data=True))
        4
    """
def is_valid_weight_list(klist, p) -> None:
    """
    This function checks that ``klist`` is a nonempty list of integers all of
    which are congruent modulo `(p-1)`. Otherwise, it will raise a
    :exc:`ValueError`.

    INPUT:

    - ``klist`` -- list of integers
    - ``p`` -- prime

    EXAMPLES::

        sage: from sage.modular.overconvergent.hecke_series import is_valid_weight_list
        sage: is_valid_weight_list([10, 20, 30],11)
        sage: is_valid_weight_list([-3, 1], 5)
        sage: is_valid_weight_list([], 3)
        Traceback (most recent call last):
        ...
        ValueError: List of weights must be non-empty
        sage: is_valid_weight_list([-3, 2], 5)
        Traceback (most recent call last):
        ...
        ValueError: List of weights must be all congruent modulo p-1 = 4, but given list contains -3 and 2 which are not congruent
    """
def hecke_series(p, N, klist, m, modformsring: bool = False, weightbound: int = 6):
    """
    Return the characteristic series modulo `p^m` of the Atkin operator `U_p`
    acting upon the space of `p`-adic overconvergent modular forms of level
    `\\Gamma_0(N)` and weight ``klist``.

    The input ``klist`` may also be a list of weights congruent modulo `(p-1)`,
    in which case the output is the corresponding list of characteristic series
    for each `k` in ``klist``; this is faster than performing the computation
    separately for each `k`, since intermediate steps in the computation may be
    reused.

    If ``modformsring`` is ``True``, then for `N > 1` the algorithm computes at one
    step ``ModularFormsRing(N).generators()``. This will often be faster but
    the algorithm will default to ``modformsring=False`` if the generators
    found are not `p`-adically integral. Note that ``modformsring`` is ignored
    for `N = 1` and the ring structure of modular forms is *always* used in
    this case.

    When ``modformsring`` is ``False`` and `N > 1`, ``weightbound`` is a bound set on
    the weight of generators for a certain subspace of modular forms. The
    algorithm will often be faster if ``weightbound=4``, but it may fail to
    terminate for certain exceptional small values of `N`, when this bound is
    too small.

    The algorithm is based upon that described in [Lau2011]_.

    INPUT:

    - ``p`` -- a prime greater than or equal to 5
    - ``N`` -- positive integer not divisible by `p`
    - ``klist`` -- either a list of integers congruent modulo `(p-1)`, or a single integer
    - ``m`` -- positive integer
    - ``modformsring`` -- boolean (default: ``False``); ignored if `N = 1`
    - ``weightbound`` -- a positive even integer (default: 6). Ignored
      if `N = 1` or ``modformsring`` is ``True``

    OUTPUT: either a list of polynomials or a single polynomial over the integers modulo `p^m`

    EXAMPLES::

        sage: hecke_series(5, 7, 10000, 5, modformsring=True) # long time (3.4s)
        250*x^6 + 1825*x^5 + 2500*x^4 + 2184*x^3 + 1458*x^2 + 1157*x + 1
        sage: hecke_series(7, 3, 10000, 3, weightbound=4)
        196*x^4 + 294*x^3 + 197*x^2 + 341*x + 1
        sage: hecke_series(19, 1, [10000, 10018], 5)
        [1694173*x^4 + 2442526*x^3 + 1367943*x^2 + 1923654*x + 1,
        130321*x^4 + 958816*x^3 + 2278233*x^2 + 1584827*x + 1]

    Check that silly weights are handled correctly::

        sage: hecke_series(5, 7, [2, 3], 5)
        Traceback (most recent call last):
        ...
        ValueError: List of weights must be all congruent modulo p-1 = 4, but given list contains 2 and 3 which are not congruent
        sage: hecke_series(5, 7, [3], 5)
        [1]
        sage: hecke_series(5, 7, 3, 5)
        1
    """
