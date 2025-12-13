from sage.misc.cachefunc import cached_function as cached_function

def MacMahonOmega(var, expression, denominator=None, op=..., Factorization_sort: bool = False, Factorization_simplify: bool = True):
    """
    Return `\\Omega_{\\mathrm{op}}` of ``expression`` with respect to ``var``.

    To be more precise, calculate

    .. MATH::

        \\Omega_{\\mathrm{op}} \\frac{n}{d_1 \\dots d_n}

    for the numerator `n` and the factors `d_1`, ..., `d_n` of
    the denominator, all of which are Laurent polynomials in ``var``
    and return a (partial) factorization of the result.

    INPUT:

    - ``var`` -- a variable or a representation string of a variable

    - ``expression`` -- a
      :class:`~sage.structure.factorization.Factorization`
      of Laurent polynomials or, if ``denominator`` is specified,
      a Laurent polynomial interpreted as the numerator of the
      expression

    - ``denominator`` -- a Laurent polynomial or a
      :class:`~sage.structure.factorization.Factorization` (consisting
      of Laurent polynomial factors) or a tuple/list of factors (Laurent
      polynomials)

    - ``op`` -- (default: ``operator.ge``) an operator

      At the moment only ``operator.ge`` is implemented.

    - ``Factorization_sort`` (default: ``False``) and
      ``Factorization_simplify`` (default: ``True``) -- are passed on to
      :class:`sage.structure.factorization.Factorization` when creating
      the result

    OUTPUT:

    A (partial) :class:`~sage.structure.factorization.Factorization`
    of the result whose factors are Laurent polynomials

    .. NOTE::

        The numerator of the result may not be factored.

    REFERENCES:

    - [Mac1915]_

    - [APR2001]_

    EXAMPLES::

        sage: L.<mu, x, y, z, w> = LaurentPolynomialRing(ZZ)

        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y/mu])
        1 * (-x + 1)^-1 * (-x*y + 1)^-1

        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y/mu, 1 - z/mu])
        1 * (-x + 1)^-1 * (-x*y + 1)^-1 * (-x*z + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y*mu, 1 - z/mu])
        (-x*y*z + 1) * (-x + 1)^-1 * (-y + 1)^-1 * (-x*z + 1)^-1 * (-y*z + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y/mu^2])
        1 * (-x + 1)^-1 * (-x^2*y + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu^2, 1 - y/mu])
        (x*y + 1) * (-x + 1)^-1 * (-x*y^2 + 1)^-1

        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y*mu, 1 - z/mu^2])
        (-x^2*y*z - x*y^2*z + x*y*z + 1) *
        (-x + 1)^-1 * (-y + 1)^-1 * (-x^2*z + 1)^-1 * (-y^2*z + 1)^-1

        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y/mu^3])
        1 * (-x + 1)^-1 * (-x^3*y + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y/mu^4])
        1 * (-x + 1)^-1 * (-x^4*y + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu^3, 1 - y/mu])
        (x*y^2 + x*y + 1) * (-x + 1)^-1 * (-x*y^3 + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu^4, 1 - y/mu])
        (x*y^3 + x*y^2 + x*y + 1) * (-x + 1)^-1 * (-x*y^4 + 1)^-1

        sage: MacMahonOmega(mu, 1, [1 - x*mu^2, 1 - y/mu, 1 - z/mu])
        (x*y*z + x*y + x*z + 1) *
        (-x + 1)^-1 * (-x*y^2 + 1)^-1 * (-x*z^2 + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu^2, 1 - y*mu, 1 - z/mu])
        (-x*y*z^2 - x*y*z + x*z + 1) *
        (-x + 1)^-1 * (-y + 1)^-1 * (-x*z^2 + 1)^-1 * (-y*z + 1)^-1

        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y*mu, 1 - z*mu, 1 - w/mu])
        (x*y*z*w^2 + x*y*z*w - x*y*w - x*z*w - y*z*w + 1) *
        (-x + 1)^-1 * (-y + 1)^-1 * (-z + 1)^-1 *
        (-x*w + 1)^-1 * (-y*w + 1)^-1 * (-z*w + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - y*mu, 1 - z/mu, 1 - w/mu])
        (x^2*y*z*w + x*y^2*z*w - x*y*z*w - x*y*z - x*y*w + 1) *
        (-x + 1)^-1 * (-y + 1)^-1 *
        (-x*z + 1)^-1 * (-x*w + 1)^-1 * (-y*z + 1)^-1 * (-y*w + 1)^-1

        sage: MacMahonOmega(mu, mu^-2, [1 - x*mu, 1 - y/mu])
        x^2 * (-x + 1)^-1 * (-x*y + 1)^-1
        sage: MacMahonOmega(mu, mu^-1, [1 - x*mu, 1 - y/mu])
        x * (-x + 1)^-1 * (-x*y + 1)^-1
        sage: MacMahonOmega(mu, mu, [1 - x*mu, 1 - y/mu])
        (-x*y + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1
        sage: MacMahonOmega(mu, mu^2, [1 - x*mu, 1 - y/mu])
        (-x*y^2 - x*y + y^2 + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1

    We demonstrate the different allowed input variants::

        sage: MacMahonOmega(mu,
        ....:     Factorization([(mu, 2), (1 - x*mu, -1), (1 - y/mu, -1)]))
        (-x*y^2 - x*y + y^2 + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1

        sage: MacMahonOmega(mu, mu^2,
        ....:     Factorization([(1 - x*mu, 1), (1 - y/mu, 1)]))
        (-x*y^2 - x*y + y^2 + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1

        sage: MacMahonOmega(mu, mu^2, [1 - x*mu, 1 - y/mu])
        (-x*y^2 - x*y + y^2 + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1

        sage: MacMahonOmega(mu, mu^2, (1 - x*mu)*(1 - y/mu))  # not tested because not fully implemented
        (-x*y^2 - x*y + y^2 + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1

        sage: MacMahonOmega(mu, mu^2 / ((1 - x*mu)*(1 - y/mu)))  # not tested because not fully implemented
        (-x*y^2 - x*y + y^2 + y + 1) * (-x + 1)^-1 * (-x*y + 1)^-1

    TESTS::

        sage: MacMahonOmega(mu, 1, [1 - x*mu])
        1 * (-x + 1)^-1
        sage: MacMahonOmega(mu, 1, [1 - x/mu])
        1
        sage: MacMahonOmega(mu, 0, [1 - x*mu])
        0
        sage: MacMahonOmega(mu, L(1), [])
        1
        sage: MacMahonOmega(mu, L(0), [])
        0
        sage: MacMahonOmega(mu, 2, [])
        2
        sage: MacMahonOmega(mu, 2*mu, [])
        2
        sage: MacMahonOmega(mu, 2/mu, [])
        0

    ::

        sage: MacMahonOmega(mu, Factorization([(1/mu, 1), (1 - x*mu, -1),
        ....:                                  (1 - y/mu, -2)], unit=2))
        2*x * (-x + 1)^-1 * (-x*y + 1)^-2
        sage: MacMahonOmega(mu, Factorization([(mu, -1), (1 - x*mu, -1),
        ....:                                  (1 - y/mu, -2)], unit=2))
        2*x * (-x + 1)^-1 * (-x*y + 1)^-2
        sage: MacMahonOmega(mu, Factorization([(mu, -1), (1 - x, -1)]))
        0
        sage: MacMahonOmega(mu, Factorization([(2, -1)]))
        1 * 2^-1

    ::

        sage: MacMahonOmega(mu, 1, [1 - x*mu, 1 - z, 1 - y/mu])
        1 * (-z + 1)^-1 * (-x + 1)^-1 * (-x*y + 1)^-1

    ::

        sage: MacMahonOmega(mu, 1, [1 - x*mu], op=operator.lt)
        Traceback (most recent call last):
        ...
        NotImplementedError: only Omega_ge is implemented

        sage: MacMahonOmega(mu, 1, Factorization([(1 - x*mu, -1)]))
        Traceback (most recent call last):
        ...
        ValueError: factorization (-mu*x + 1)^-1 of the denominator
        contains negative exponents

        sage: MacMahonOmega(2*mu, 1, [1 - x*mu])
        Traceback (most recent call last):
        ...
        ValueError: 2*mu is not a variable

        sage: MacMahonOmega(mu, 1, Factorization([(0, 2)]))
        Traceback (most recent call last):
        ...
        ZeroDivisionError: denominator contains a factor 0

        sage: MacMahonOmega(mu, 1, [2 - x*mu])
        Traceback (most recent call last):
        ...
        NotImplementedError: factor 2 - x*mu is not normalized

        sage: MacMahonOmega(mu, 1, [1 - x*mu - mu^2])
        Traceback (most recent call last):
        ...
        NotImplementedError: cannot handle factor 1 - x*mu - mu^2

    ::

        sage: L.<mu, x, y, z, w> = LaurentPolynomialRing(QQ)
        sage: MacMahonOmega(mu, 1/mu,
        ....:     Factorization([(1 - x*mu, 1), (1 - y/mu, 2)], unit=2))
        1/2*x * (-x + 1)^-1 * (-x*y + 1)^-2
    """
@cached_function
def Omega_ge(a, exponents):
    """
    Return `\\Omega_{\\ge}` of the expression specified by the input.

    To be more precise, calculate

    .. MATH::

        \\Omega_{\\ge} \\frac{\\mu^a}{
        (1 - z_0 \\mu^{e_0}) \\dots (1 - z_{n-1} \\mu^{e_{n-1}})}

    and return its numerator and a factorization of its denominator.
    Note that `z_0`, ..., `z_{n-1}` only appear in the output, but not in the
    input.

    INPUT:

    - ``a`` -- integer

    - ``exponents`` -- tuple of integers

    OUTPUT:

    A pair representing a quotient as follows: Its first component is the
    numerator as a Laurent polynomial, its second component a factorization
    of the denominator as a tuple of Laurent polynomials, where each
    Laurent polynomial `z` represents a factor `1 - z`.

    The parents of these Laurent polynomials is always a
    Laurent polynomial ring in `z_0`, ..., `z_{n-1}` over `\\ZZ`, where
    `n` is the length of ``exponents``.

    EXAMPLES::

        sage: from sage.rings.polynomial.omega import Omega_ge
        sage: Omega_ge(0, (1, -2))
        (1, (z0, z0^2*z1))
        sage: Omega_ge(0, (1, -3))
        (1, (z0, z0^3*z1))
        sage: Omega_ge(0, (1, -4))
        (1, (z0, z0^4*z1))

        sage: Omega_ge(0, (2, -1))
        (z0*z1 + 1, (z0, z0*z1^2))
        sage: Omega_ge(0, (3, -1))
        (z0*z1^2 + z0*z1 + 1, (z0, z0*z1^3))
        sage: Omega_ge(0, (4, -1))
        (z0*z1^3 + z0*z1^2 + z0*z1 + 1, (z0, z0*z1^4))

        sage: Omega_ge(0, (1, 1, -2))
        (-z0^2*z1*z2 - z0*z1^2*z2 + z0*z1*z2 + 1, (z0, z1, z0^2*z2, z1^2*z2))
        sage: Omega_ge(0, (2, -1, -1))
        (z0*z1*z2 + z0*z1 + z0*z2 + 1, (z0, z0*z1^2, z0*z2^2))
        sage: Omega_ge(0, (2, 1, -1))
        (-z0*z1*z2^2 - z0*z1*z2 + z0*z2 + 1, (z0, z1, z0*z2^2, z1*z2))

    ::

        sage: Omega_ge(0, (2, -2))
        (-z0*z1 + 1, (z0, z0*z1, z0*z1))
        sage: Omega_ge(0, (2, -3))
        (z0^2*z1 + 1, (z0, z0^3*z1^2))
        sage: Omega_ge(0, (3, 1, -3))
        (-z0^3*z1^3*z2^3 + 2*z0^2*z1^3*z2^2 - z0*z1^3*z2
         + z0^2*z2^2 - 2*z0*z2 + 1,
         (z0, z1, z0*z2, z0*z2, z0*z2, z1^3*z2))

    ::

        sage: Omega_ge(0, (3, 6, -1))
        (-z0*z1*z2^8 - z0*z1*z2^7 - z0*z1*z2^6 - z0*z1*z2^5 - z0*z1*z2^4 +
         z1*z2^5 - z0*z1*z2^3 + z1*z2^4 - z0*z1*z2^2 + z1*z2^3 -
         z0*z1*z2 + z0*z2^2 + z1*z2^2 + z0*z2 + z1*z2 + 1,
         (z0, z1, z0*z2^3, z1*z2^6))

    TESTS::

        sage: Omega_ge(0, (2, 2, 1, 1, 1, -1, -1))[0].number_of_terms()  # long time
        1695
        sage: Omega_ge(0, (2, 2, 1, 1, 1, 1, 1, -1, -1))[0].number_of_terms()  # not tested (too long, 1 min)
        27837

    ::

        sage: Omega_ge(1, (2,))
        (1, (z0,))
    """
def partition(items, predicate=...):
    """
    Split ``items`` into two parts by the given ``predicate``.

    INPUT:

    - ``item`` -- an iterator

    - ``predicate`` -- a function

    OUTPUT:

    A pair of iterators; the first contains the elements not satisfying
    the ``predicate``, the second the elements satisfying the ``predicate``.

    ALGORITHM:

    Source of the code:
    `http://nedbatchelder.com/blog/201306/filter_a_list_into_two_parts.html
    <http://nedbatchelder.com/blog/201306/filter_a_list_into_two_parts.html>`_

    EXAMPLES::

        sage: from sage.rings.polynomial.omega import partition
        sage: E, O = partition(srange(10), is_odd)
        sage: tuple(E), tuple(O)
        ((0, 2, 4, 6, 8), (1, 3, 5, 7, 9))
    """
def homogeneous_symmetric_function(j, x):
    """
    Return a complete homogeneous symmetric polynomial
    (:wikipedia:`Complete_homogeneous_symmetric_polynomial`).

    INPUT:

    - ``j`` -- the degree as a nonnegative integer

    - ``x`` -- an iterable of variables

    OUTPUT: a polynomial of the common parent of all entries of ``x``

    EXAMPLES::

        sage: from sage.rings.polynomial.omega import homogeneous_symmetric_function
        sage: P = PolynomialRing(ZZ, 'X', 3)
        sage: homogeneous_symmetric_function(0, P.gens())
        1
        sage: homogeneous_symmetric_function(1, P.gens())
        X0 + X1 + X2
        sage: homogeneous_symmetric_function(2, P.gens())
        X0^2 + X0*X1 + X1^2 + X0*X2 + X1*X2 + X2^2
        sage: homogeneous_symmetric_function(3, P.gens())
        X0^3 + X0^2*X1 + X0*X1^2 + X1^3 + X0^2*X2 +
        X0*X1*X2 + X1^2*X2 + X0*X2^2 + X1*X2^2 + X2^3
    """
