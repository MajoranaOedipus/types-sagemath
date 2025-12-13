from _typeshed import Incomplete
from sage.misc.verbose import get_verbose as get_verbose
from sage.structure.sequence import Sequence as Sequence

LCM: Incomplete
LM: Incomplete
LT: Incomplete

def spol(f, g):
    """
    Compute the S-polynomial of f and g.

    INPUT:

    - ``f``, ``g`` -- polynomials

    OUTPUT: the S-polynomial of f and g

    EXAMPLES::

        sage: R.<x,y,z> = PolynomialRing(QQ)
        sage: from sage.rings.polynomial.toy_buchberger import spol
        sage: spol(x^2 - z - 1, z^2 - y - 1)
        x^2*y - z^3 + x^2 - z^2
    """
def buchberger(F):
    """
    Compute a Groebner basis using the original version of Buchberger's
    algorithm as presented in [BW1993]_, page 214.

    INPUT:

    - ``F`` -- an ideal in a multivariate polynomial ring

    OUTPUT: a Groebner basis for F

    .. NOTE::

       The verbosity of this function may be controlled with a
       ``set_verbose()`` call. Any value >=1 will result in this
       function printing intermediate bases.

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_buchberger import buchberger
        sage: R.<x,y,z> = PolynomialRing(QQ)
        sage: I = R.ideal([x^2 - z - 1, z^2 - y - 1, x*y^2 - x - 1])
        sage: set_verbose(0)
        sage: gb = buchberger(I)                                                        # needs sage.libs.singular
        sage: gb.is_groebner()                                                          # needs sage.libs.singular
        True
        sage: gb.ideal() == I                                                           # needs sage.libs.singular
        True
    """
def buchberger_improved(F):
    """
    Compute a Groebner basis using an improved version of Buchberger's
    algorithm as presented in [BW1993]_, page 232.

    This variant uses the Gebauer-Moeller Installation to apply
    Buchberger's first and second criterion to avoid useless pairs.

    INPUT:

    - ``F`` -- an ideal in a multivariate polynomial ring

    OUTPUT: a Groebner basis for F

    .. NOTE::

       The verbosity of this function may be controlled with a
       ``set_verbose()`` call. Any value ``>=1`` will result in this
       function printing intermediate Groebner bases.

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_buchberger import buchberger_improved
        sage: R.<x,y,z> = PolynomialRing(QQ)
        sage: set_verbose(0)
        sage: sorted(buchberger_improved(R.ideal([x^4 - y - z, x*y*z - 1])))            # needs sage.libs.singular
        [x*y*z - 1, x^3 - y^2*z - y*z^2, y^3*z^2 + y^2*z^3 - x^2]
    """
def update(G, B, h):
    """
    Update ``G`` using the set of critical pairs ``B`` and the
    polynomial ``h`` as presented in [BW1993]_, page 230. For this,
    Buchberger's first and second criterion are tested.

    This function implements the Gebauer-Moeller Installation.

    INPUT:

    - ``G`` -- an intermediate Groebner basis

    - ``B`` -- set of critical pairs

    - ``h`` -- a polynomial

    OUTPUT: a tuple of

    - an intermediate Groebner basis

    - a set of critical pairs

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_buchberger import update
        sage: R.<x,y,z> = PolynomialRing(QQ)
        sage: set_verbose(0)
        sage: update(set(), set(), x*y*z)
        ({x*y*z}, set())
        sage: G, B = update(set(), set(), x*y*z - 1)
        sage: G, B = update(G, B, x*y^2 - 1)
        sage: G, B
        ({x*y*z - 1, x*y^2 - 1}, {(x*y^2 - 1, x*y*z - 1)})
    """
def select(P):
    """
    Select a polynomial using the normal selection strategy.

    INPUT:

    - ``P`` -- list of critical pairs

    OUTPUT: an element of P

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_buchberger import select
        sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
        sage: ps = [x^3 - z - 1, z^3 - y - 1, x^5 - y - 2]
        sage: pairs = [[ps[i], ps[j]] for i in range(3) for j in range(i + 1, 3)]
        sage: select(pairs)
        [x^3 - z - 1, -y + z^3 - 1]
    """
def inter_reduction(Q):
    """
    Compute inter-reduced polynomials from a set of polynomials.

    INPUT:

    - ``Q`` -- set of polynomials

    OUTPUT:

    if ``Q`` is the set `f_1, ..., f_n`, this method returns `g_1,
    ..., g_s` such that:

    - `(f_1,...,f_n) = (g_1,...,g_s)`
    - `LM(g_i) \\neq LM(g_j)` for all `i \\neq j`
    - `LM(g_i)` does not divide `m` for all monomials `m` of
      `\\{g_1,...,g_{i-1}, g_{i+1},...,g_s\\}`
    - `LC(g_i) = 1` for all `i`.

    EXAMPLES::

        sage: from sage.rings.polynomial.toy_buchberger import inter_reduction
        sage: inter_reduction(set())
        set()

    ::

        sage: P.<x,y> = QQ[]
        sage: reduced = inter_reduction(set([x^2 - 5*y^2, x^3]))                        # needs sage.libs.singular
        sage: reduced == set([x*y^2, x^2 - 5*y^2])                                      # needs sage.libs.singular
        True
        sage: reduced == inter_reduction(set([2*(x^2 - 5*y^2), x^3]))                   # needs sage.libs.singular
        True
    """
