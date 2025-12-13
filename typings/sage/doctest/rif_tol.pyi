from sage.doctest.marked_output import MarkedOutput as MarkedOutput
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField, RealIntervalFieldElement as RealIntervalFieldElement

def RIFtol(*args) -> RealIntervalFieldElement:
    '''
    Create an element of the real interval field used for doctest tolerances.

    It allows large numbers like 1e1000, it parses strings with spaces
    like ``RIF(" - 1 ")`` out of the box and it carries a lot of
    precision. The latter is useful for testing libraries using
    arbitrary precision but not guaranteed rounding such as PARI. We use
    1044 bits of precision, which should be good to deal with tolerances
    on numbers computed with 1024 bits of precision.

    The interval approach also means that we do not need to worry about
    rounding errors and it is also very natural to see a number with
    tolerance as an interval.

    EXAMPLES::

        sage: from sage.doctest.parsing import RIFtol
        sage: RIFtol(-1, 1)
        0.?
        sage: RIFtol(" - 1 ")
        -1
        sage: RIFtol("1e1000")
        1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000?e1000
    '''
def add_tolerance(wantval, want: MarkedOutput):
    """
    Enlarge the real interval element ``wantval`` according to
    the tolerance options in ``want``.

    INPUT:

    - ``wantval`` -- a real interval element
    - ``want`` -- a :class:`MarkedOutput` describing the tolerance

    OUTPUT: an interval element containing ``wantval``

    EXAMPLES::

        sage: from sage.doctest.parsing import MarkedOutput, SageOutputChecker
        sage: from sage.doctest.rif_tol import add_tolerance
        sage: want_tol = MarkedOutput().update(tol=0.0001)
        sage: want_abs = MarkedOutput().update(abs_tol=0.0001)
        sage: want_rel = MarkedOutput().update(rel_tol=0.0001)
        sage: add_tolerance(RIF(pi.n(64)), want_tol).endpoints()                 # needs sage.symbolic
        (3.14127849432443, 3.14190681285516)
        sage: add_tolerance(RIF(pi.n(64)), want_abs).endpoints()                 # needs sage.symbolic
        (3.14149265358979, 3.14169265358980)
        sage: add_tolerance(RIF(pi.n(64)), want_rel).endpoints()                 # needs sage.symbolic
        (3.14127849432443, 3.14190681285516)
        sage: add_tolerance(RIF(1e1000), want_tol)
        1.000?e1000
        sage: add_tolerance(RIF(1e1000), want_abs)
        1.000000000000000?e1000
        sage: add_tolerance(RIF(1e1000), want_rel)
        1.000?e1000
        sage: add_tolerance(0, want_tol)
        0.000?
        sage: add_tolerance(0, want_abs)
        0.000?
        sage: add_tolerance(0, want_rel)
        0
    """
