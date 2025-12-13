from sage.arith.misc import factorial as factorial
from sage.combinat.composition import Composition as Composition, Compositions as Compositions
from sage.combinat.composition_tableau import CompositionTableaux as CompositionTableaux
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ

def coeff_pi(J, I):
    """
    Return the coefficient `\\pi_{J,I}` as defined in [NCSF]_.

    INPUT:

    - ``J`` -- a composition
    - ``I`` -- a composition refining ``J``

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import coeff_pi
        sage: coeff_pi(Composition([1,1,1]), Composition([2,1]))
        2
        sage: coeff_pi(Composition([2,1]), Composition([3]))
        6
    """
def coeff_lp(J, I):
    """
    Return the coefficient `lp_{J,I}` as defined in [NCSF]_.

    INPUT:

    - ``J`` -- a composition
    - ``I`` -- a composition refining ``J``

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import coeff_lp
        sage: coeff_lp(Composition([1,1,1]), Composition([2,1]))
        1
        sage: coeff_lp(Composition([2,1]), Composition([3]))
        1
    """
def coeff_ell(J, I):
    """
    Return the coefficient `\\ell_{J,I}` as defined in [NCSF]_.

    INPUT:

    - ``J`` -- a composition
    - ``I`` -- a composition refining ``J``

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import coeff_ell
        sage: coeff_ell(Composition([1,1,1]), Composition([2,1]))
        2
        sage: coeff_ell(Composition([2,1]), Composition([3]))
        2
    """
def coeff_sp(J, I):
    """
    Return the coefficient `sp_{J,I}` as defined in [NCSF]_.

    INPUT:

    - ``J`` -- a composition
    - ``I`` -- a composition refining ``J``

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import coeff_sp
        sage: coeff_sp(Composition([1,1,1]), Composition([2,1]))
        2
        sage: coeff_sp(Composition([2,1]), Composition([3]))
        4
    """
def coeff_dab(I, J):
    """
    Return the number of standard composition tableaux of shape `I` with
    descent composition `J`.

    INPUT:

    - ``I``, ``J`` -- compositions

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import coeff_dab
        sage: coeff_dab(Composition([2,1]),Composition([2,1]))
        1
        sage: coeff_dab(Composition([1,1,2]),Composition([1,2,1]))
        0
    """
def compositions_order(n):
    """
    Return the compositions of `n` ordered as defined in [QSCHUR]_.

    Let `S(\\gamma)` return the composition `\\gamma` after sorting. For
    compositions `\\alpha` and `\\beta`, we order `\\alpha \\rhd \\beta` if

    1) `S(\\alpha) > S(\\beta)` lexicographically, or
    2) `S(\\alpha) = S(\\beta)` and `\\alpha > \\beta` lexicographically.

    INPUT:

    - ``n`` -- positive integer

    OUTPUT: list of the compositions of `n` sorted into decreasing order
    by `\\rhd`

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import compositions_order
        sage: compositions_order(3)
        [[3], [2, 1], [1, 2], [1, 1, 1]]
        sage: compositions_order(4)
        [[4], [3, 1], [1, 3], [2, 2], [2, 1, 1], [1, 2, 1], [1, 1, 2], [1, 1, 1, 1]]
    """
def m_to_s_stat(R, I, K):
    """
    Return the coefficient of the complete non-commutative symmetric
    function `S^K` in the expansion of the monomial non-commutative
    symmetric function `M^I` with respect to the complete basis
    over the ring `R`. This is the coefficient in formula (36) of
    Tevlin's paper [Tev2007]_.

    INPUT:

    - ``R`` -- a ring; supposed to be a `\\QQ`-algebra
    - ``I``, ``K`` -- compositions

    OUTPUT:

    - The coefficient of `S^K` in the expansion of `M^I` in the
      complete basis of the non-commutative symmetric functions
      over ``R``.

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import m_to_s_stat
        sage: m_to_s_stat(QQ, Composition([2,1]), Composition([1,1,1]))
        -1
        sage: m_to_s_stat(QQ, Composition([3]), Composition([1,2]))
        -2
        sage: m_to_s_stat(QQ, Composition([2,1,2]), Composition([2,1,2]))
        8/3
    """
@cached_function
def number_of_fCT(content_comp, shape_comp):
    """
    Return the number of Immaculate tableaux of shape
    ``shape_comp`` and content ``content_comp``.

    See [BBSSZ2012]_, Definition 3.9, for the notion of an
    immaculate tableau.

    INPUT:

    - ``content_comp``, ``shape_comp`` -- compositions

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import number_of_fCT
        sage: number_of_fCT(Composition([3,1]), Composition([1,3]))
        0
        sage: number_of_fCT(Composition([1,2,1]), Composition([1,3]))
        1
        sage: number_of_fCT(Composition([1,1,3,1]), Composition([2,1,3]))
        2
    """
@cached_function
def number_of_SSRCT(content_comp, shape_comp):
    """
    The number of semi-standard reverse composition tableaux.

    The dual quasisymmetric-Schur functions satisfy a left Pieri rule
    where `S_n dQS_\\gamma` is a sum over dual quasisymmetric-Schur
    functions indexed by compositions which contain the composition
    `\\gamma`.  The definition of an SSRCT comes from this rule.  The
    number of SSRCT of content `\\beta` and shape `\\alpha` is equal to
    the number of SSRCT of content `(\\beta_2, \\ldots, \\beta_\\ell)`
    and shape `\\gamma` where `dQS_\\alpha` appears in the expansion of
    `S_{\\beta_1} dQS_\\gamma`.

    In sage the recording tableau for these objects are called
    :class:`~sage.combinat.composition_tableau.CompositionTableaux`.

    INPUT:

    - ``content_comp``, ``shape_comp`` -- compositions

    OUTPUT: integer

    EXAMPLES::

        sage: from sage.combinat.ncsf_qsym.combinatorics import number_of_SSRCT
        sage: number_of_SSRCT(Composition([3,1]), Composition([1,3]))
        0
        sage: number_of_SSRCT(Composition([1,2,1]), Composition([1,3]))
        1
        sage: number_of_SSRCT(Composition([1,1,2,2]), Composition([3,3]))
        2
        sage: all(CompositionTableaux(be).cardinality()
        ....:     == sum(number_of_SSRCT(al,be)*binomial(4,len(al))
        ....:            for al in Compositions(4))
        ....:     for be in Compositions(4))
        True
    """
