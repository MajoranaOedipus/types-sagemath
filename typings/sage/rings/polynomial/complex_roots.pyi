from sage.arith.misc import sort_complex_numbers_for_display as sort_complex_numbers_for_display
from sage.rings.complex_interval_field import ComplexIntervalField as ComplexIntervalField
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.polynomial.refine_root import refine_root as refine_root
from sage.rings.qqbar import AA as AA, QQbar as QQbar

def interval_roots(p, rts, prec):
    """
    We are given a squarefree polynomial p, a list of estimated roots,
    and a precision.

    We attempt to verify that the estimated roots are in fact distinct
    roots of the polynomial, using interval arithmetic of precision ``prec``.
    If we succeed, we return a list of intervals bounding the roots; if we
    fail, we return ``None``.

    EXAMPLES::

        sage: x = polygen(ZZ)
        sage: p = x^3 - 1
        sage: rts = [CC.zeta(3)^i for i in range(0, 3)]
        sage: from sage.rings.polynomial.complex_roots import interval_roots
        sage: interval_roots(p, rts, 53)
        [1, -0.500000000000000? + 0.866025403784439?*I,
            -0.500000000000000? - 0.866025403784439?*I]
        sage: interval_roots(p, rts, 200)
        [1, -0.500000000000000000000000000000000000000000000000000000000000?
              + 0.866025403784438646763723170752936183471402626905190314027904?*I,
            -0.500000000000000000000000000000000000000000000000000000000000?
              - 0.866025403784438646763723170752936183471402626905190314027904?*I]
    """
def intervals_disjoint(intvs):
    """
    Given a list of complex intervals, check whether they are pairwise
    disjoint.

    EXAMPLES::

        sage: from sage.rings.polynomial.complex_roots import intervals_disjoint
        sage: a = CIF(RIF(0, 3), 0)
        sage: b = CIF(0, RIF(1, 3))
        sage: c = CIF(RIF(1, 2), RIF(1, 2))
        sage: d = CIF(RIF(2, 3), RIF(2, 3))
        sage: intervals_disjoint([a,b,c,d])
        False
        sage: d2 = CIF(RIF(2, 3), RIF(2.001, 3))
        sage: intervals_disjoint([a,b,c,d2])
        True
    """
def complex_roots(p, skip_squarefree: bool = False, retval: str = 'interval', min_prec: int = 0):
    """
    Compute the complex roots of a given polynomial with exact
    coefficients (integer, rational, Gaussian rational, and algebraic
    coefficients are supported).  Returns a list of pairs of a root
    and its multiplicity.

    Roots are returned as a ComplexIntervalFieldElement; each interval
    includes exactly one root, and the intervals are disjoint.

    By default, the algorithm will do a squarefree decomposition
    to get squarefree polynomials.  The skip_squarefree parameter
    lets you skip this step.  (If this step is skipped, and the polynomial
    has a repeated root, then the algorithm will loop forever!)

    You can specify retval='interval' (the default) to get roots as
    complex intervals.  The other options are retval='algebraic' to
    get elements of QQbar, or retval='algebraic_real' to get only
    the real roots, and to get them as elements of AA.

    EXAMPLES::

        sage: from sage.rings.polynomial.complex_roots import complex_roots
        sage: x = polygen(ZZ)
        sage: complex_roots(x^5 - x - 1)
        [(1.167303978261419?, 1),
         (-0.764884433600585? - 0.352471546031727?*I, 1),
         (-0.764884433600585? + 0.352471546031727?*I, 1),
         (0.181232444469876? - 1.083954101317711?*I, 1),
         (0.181232444469876? + 1.083954101317711?*I, 1)]
        sage: v = complex_roots(x^2 + 27*x + 181)

    Unfortunately due to numerical noise there can be a small imaginary part to each
    root depending on CPU, compiler, etc, and that affects the printing order. So we
    verify the real part of each root and check that the imaginary part is small in
    both cases::

        sage: v  # random
        [(-14.61803398874990?..., 1), (-12.3819660112501...? + 0.?e-27*I, 1)]
        sage: sorted((v[0][0].real(),v[1][0].real()))
        [-14.61803398874989?, -12.3819660112501...?]
        sage: v[0][0].imag().upper() < 1e25
        True
        sage: v[1][0].imag().upper() < 1e25
        True

        sage: K.<im> = QuadraticField(-1)
        sage: eps = 1/2^100
        sage: x = polygen(K)
        sage: p = (x-1)*(x-1-eps)*(x-1+eps)*(x-1-eps*im)*(x-1+eps*im)

    This polynomial actually has all-real coefficients, and is very, very
    close to (x-1)^5::

        sage: [RR(QQ(a)) for a in list(p - (x-1)^5)]
        [3.87259191484932e-121, -3.87259191484932e-121]
        sage: rts = complex_roots(p)
        sage: [ComplexIntervalField(10)(rt[0] - 1) for rt in rts]
        [-7.8887?e-31, 0, 7.8887?e-31, -7.8887?e-31*I, 7.8887?e-31*I]

    We can get roots either as intervals, or as elements of QQbar or AA.

    ::

        sage: p = (x^2 + x - 1)
        sage: p = p * p(x*im)
        sage: p
        -x^4 + (im - 1)*x^3 + im*x^2 + (-im - 1)*x + 1

    Two of the roots have a zero real component; two have a zero
    imaginary component.  These zero components will be found slightly
    inaccurately, and the exact values returned are very sensitive to
    the (non-portable) results of NumPy.  So we post-process the roots
    for printing, to get predictable doctest results.

    ::

        sage: def tiny(x):
        ....:     return x.contains_zero() and x.absolute_diameter() <  1e-14
        sage: def smash(x):
        ....:     x = CIF(x[0]) # discard multiplicity
        ....:     if tiny(x.imag()): return x.real()
        ....:     if tiny(x.real()): return CIF(0, x.imag())
        sage: rts = complex_roots(p); type(rts[0][0]), sorted(map(smash, rts))
        (<class 'sage.rings.complex_interval.ComplexIntervalFieldElement'>,
         [-1.618033988749895?, -0.618033988749895?*I,
          1.618033988749895?*I, 0.618033988749895?])
        sage: rts = complex_roots(p, retval='algebraic'); type(rts[0][0]), sorted(map(smash, rts))
        (<class 'sage.rings.qqbar.AlgebraicNumber'>,
         [-1.618033988749895?, -0.618033988749895?*I,
          1.618033988749895?*I, 0.618033988749895?])
        sage: rts = complex_roots(p, retval='algebraic_real'); type(rts[0][0]), rts
        (<class 'sage.rings.qqbar.AlgebraicReal'>,
         [(-1.618033988749895?, 1), (0.618033988749895?, 1)])

    TESTS:

    Verify that :issue:`12026` is fixed::

        sage: f = matrix(QQ, 8, lambda i, j: 1/(i + j + 1)).charpoly()
        sage: from sage.rings.polynomial.complex_roots import complex_roots
        sage: len(complex_roots(f))
        8
    """
