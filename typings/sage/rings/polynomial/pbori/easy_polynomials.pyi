from sage.rings.polynomial.pbori.interpolate import nf_lex_points as nf_lex_points, variety_lex_leading_terms as variety_lex_leading_terms
from sage.rings.polynomial.pbori.pbori import easy_linear_factors as easy_linear_factors

def easy_linear_polynomials(p):
    """
    Get linear polynomials implied by given polynomial.

    EXAMPLES::

        sage: from sage.rings.polynomial.pbori.frontend import x
        sage: from sage.rings.polynomial.pbori.easy_polynomials import easy_linear_polynomials
        sage: easy_linear_polynomials(x(1)*x(2) + 1)
        [x(1) + 1, x(2) + 1]
        sage: easy_linear_polynomials(x(1)*x(2) + 0)
        []
        sage: easy_linear_polynomials(x(0)*x(1) + x(0)*x(2) + 1)
        [x(0) + 1, x(1) + x(2) + 1]
    """
def easy_linear_polynomials_via_interpolation(p):
    """
    Get linear polynomials implied by given polynomial using interpolation of the variety.

    TESTS::

        sage: from sage.rings.polynomial.pbori.frontend import x
        sage: from sage.rings.polynomial.pbori.easy_polynomials import easy_linear_polynomials_via_interpolation
        sage: easy_linear_polynomials_via_interpolation(x(1)*x(2) + 1)
        [x(1) + 1, x(2) + 1]
        sage: easy_linear_polynomials_via_interpolation(x(1)*x(2) + 0)
        []
        sage: easy_linear_polynomials_via_interpolation(x(0)*x(1) + x(0)*x(2) + 1)
        [x(0) + 1, x(1) + x(2) + 1]
    """
