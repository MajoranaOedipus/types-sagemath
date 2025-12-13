from sage.rings.infinity import infinity as infinity

python_min = min
python_max = max

def gauss_sum(a, p, f, prec: int = 20, factored: bool = False, algorithm: str = 'pari', parent=None):
    """
    Return the Gauss sum `g_q(a)` as a `p`-adic number.

    The Gauss sum `g_q(a)` is defined by

    .. MATH::

        g_q(a)= \\sum_{u\\in F_q^*} \\omega(u)^{-a} \\zeta_q^u,

    where `q = p^f`, `\\omega` is the Teichmüller character and
    `\\zeta_q` is some arbitrary choice of primitive `q`-th root of
    unity. The computation is adapted from the main theorem in Alain
    Robert's paper *The Gross-Koblitz formula revisited*,
    Rend. Sem. Mat. Univ. Padova 105 (2001), 157--170.

    Let `p` be a prime, `f` a positive integer, `q=p^f`, and `\\pi` be
    the unique root of `f(x) = x^{p-1}+p` congruent to `\\zeta_p - 1` modulo
    `(\\zeta_p - 1)^2`. Let `0\\leq a < q-1`. Then the
    Gross-Koblitz formula gives us the value of the Gauss sum `g_q(a)`
    as a product of `p`-adic Gamma functions as follows:

    .. MATH::

        g_q(a) = -\\pi^s \\prod_{0\\leq i < f} \\Gamma_p(a^{(i)}/(q-1)),

    where `s` is the sum of the digits of `a` in base `p` and the
    `a^{(i)}` have `p`-adic expansions obtained from cyclic
    permutations of that of `a`.

    INPUT:

    - ``a`` -- integer

    - ``p`` -- prime

    - ``f`` -- positive integer

    - ``prec`` -- positive integer (default: 20)

    - ``factored`` -- boolean (default: ``False``)

    - ``algorithm`` -- flag passed to `p`-adic Gamma function (default: ``'pari'``)

    OUTPUT:

    If ``factored`` is ``False``, returns a `p`-adic number in an Eisenstein extension of `\\QQ_p`.
    This number has the form `pi^e * z` where `pi` is as above, `e` is some nonnegative
    integer, and `z` is an element of `\\ZZ_p`; if ``factored`` is ``True``, the pair `(e,z)`
    is returned instead, and the Eisenstein extension is not formed.

    .. NOTE::

        This is based on GP code written by Adriana Salerno.

    EXAMPLES:

    In this example, we verify that `g_3(0) = -1`::

        sage: from sage.rings.padics.misc import gauss_sum
        sage: -gauss_sum(0, 3, 1)                                                       # needs sage.libs.ntl sage.rings.padics
        1 + O(pi^40)

    Next, we verify that `g_5(a) g_5(-a) = 5 (-1)^a`::

        sage: from sage.rings.padics.misc import gauss_sum
        sage: gauss_sum(2,5,1)^2 - 5                                                    # needs sage.libs.ntl
        O(pi^84)
        sage: gauss_sum(1,5,1)*gauss_sum(3,5,1) + 5                                     # needs sage.libs.ntl
        O(pi^84)

    Finally, we compute a non-trivial value::

        sage: from sage.rings.padics.misc import gauss_sum
        sage: gauss_sum(2,13,2)                                                         # needs sage.libs.ntl
        6*pi^2 + 7*pi^14 + 11*pi^26 + 3*pi^62 + 6*pi^74 + 3*pi^86 + 5*pi^98 +
        pi^110 + 7*pi^134 + 9*pi^146 + 4*pi^158 + 6*pi^170 + 4*pi^194 +
        pi^206 + 6*pi^218 + 9*pi^230 + O(pi^242)
        sage: gauss_sum(2,13,2, prec=5, factored=True)                                  # needs sage.rings.padics
        (2, 6 + 6*13 + 10*13^2 + O(13^5))

    .. SEEALSO::

        - :func:`sage.arith.misc.gauss_sum` for general finite fields
        - :meth:`sage.modular.dirichlet.DirichletCharacter.gauss_sum`
          for prime finite fields
        - :meth:`sage.modular.dirichlet.DirichletCharacter.gauss_sum_numerical`
          for prime finite fields
    """
def min(*L):
    """
    Return the minimum of the inputs, where the minimum of the empty
    list is `\\infty`.

    EXAMPLES::

        sage: from sage.rings.padics.misc import min
        sage: min()
        +Infinity
        sage: min(2,3)
        2
    """
def max(*L):
    """
    Return the maximum of the inputs, where the maximum of the empty
    list is `-\\infty`.

    EXAMPLES::

        sage: from sage.rings.padics.misc import max
        sage: max()
        -Infinity
        sage: max(2,3)
        3
    """
def precprint(prec_type, prec_cap, p):
    """
    String describing the precision mode on a `p`-adic ring or field.

    EXAMPLES::

        sage: from sage.rings.padics.misc import precprint
        sage: precprint('capped-rel', 12, 2)
        'with capped relative precision 12'
        sage: precprint('capped-abs', 11, 3)
        'with capped absolute precision 11'
        sage: precprint('floating-point', 1234, 5)
        'with floating precision 1234'
        sage: precprint('fixed-mod', 1, 17)
        'of fixed modulus 17^1'
    """
def trim_zeros(L):
    """
    Strip trailing zeros/empty lists from a list.

    EXAMPLES::

        sage: from sage.rings.padics.misc import trim_zeros
        sage: trim_zeros([1,0,1,0])
        [1, 0, 1]
        sage: trim_zeros([[1],[],[2],[],[]])
        [[1], [], [2]]
        sage: trim_zeros([[],[]])
        []
        sage: trim_zeros([])
        []

    Zeros are also trimmed from nested lists (one deep)::

        sage: trim_zeros([[1,0]])
        [[1]]
        sage: trim_zeros([[0],[1]])
        [[], [1]]
    """
