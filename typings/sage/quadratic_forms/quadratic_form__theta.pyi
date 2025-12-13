from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing

def theta_series(self, Max: int = 10, var_str: str = 'q', safe_flag: bool = True):
    """
    Compute the theta series as a power series in the variable given
    in ``var_str`` (which defaults to ``'q'``), up to the specified precision
    `O(q^{Max})`.

    This uses the PARI/GP function :pari:`qfrep`, wrapped by the
    theta_by_pari() method. This caches the result for future
    computations.

    The ``safe_flag`` allows us to select whether we want a copy of the
    output, or the original output.  It is only meaningful when a
    vector is returned, otherwise a copy is automatically made in
    creating the power series.  By default ``safe_flag`` = ``True``, so we
    return a copy of the cached information.  If this is set to ``False``,
    then the routine is much faster but the return values are
    vulnerable to being corrupted by the user.

    .. TODO::

        Allow the option ``Max='mod_form'`` to give enough coefficients
        to ensure we determine the theta series as a modular form.  This
        is related to the Sturm bound, but we will need to be careful about
        this (particularly for half-integral weights!).

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Q.theta_series()                                                          # needs sage.libs.pari
        1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 6*q^7 + 8*q^8 + 14*q^9 + O(q^10)

        sage: Q.theta_series(25)                                                        # needs sage.libs.pari
        1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 6*q^7 + 8*q^8 + 14*q^9 + 4*q^10
        + 12*q^11 + 18*q^12 + 12*q^13 + 12*q^14 + 8*q^15 + 34*q^16 + 12*q^17 + 8*q^18
        + 32*q^19 + 10*q^20 + 28*q^21 + 16*q^23 + 44*q^24 + O(q^25)
    """
def theta_by_pari(self, Max, var_str: str = 'q', safe_flag: bool = True):
    """
    Use PARI/GP to compute the theta function as a power series (or
    vector) up to the precision `O(q^{Max})`.  This also caches the result
    for future computations.

    If ``var_str`` = ``''``, then we return a vector `v` where ``v[i]`` counts the
    number of vectors of length `i`.

    The ``safe_flag`` allows us to select whether we want a copy of the
    output, or the original output.  It is only meaningful when a
    vector is returned, otherwise a copy is automatically made in
    creating the power series.  By default ``safe_flag=True``, so we
    return a copy of the cached information.  If this is set to ``False``,
    then the routine is much faster but the return values are
    vulnerable to being corrupted by the user.

    INPUT:

    - ``Max`` -- integer `\\geq 0`
    - ``var_str`` -- string

    OUTPUT: a power series or a vector

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Prec = 100
        sage: compute = Q.theta_by_pari(Prec, '')                                       # needs sage.libs.pari
        sage: exact = [1] + [8 * sum([d  for d in divisors(i)  if d % 4 != 0])          # needs sage.libs.pari
        ....:                for i in range(1, Prec)]
        sage: compute == exact                                                          # needs sage.libs.pari
        True
    """
def theta_by_cholesky(self, q_prec):
    '''
    Uses the real Cholesky decomposition to compute (the `q`-expansion of) the
    theta function of the quadratic form as a power series in `q` with terms
    correct up to the power `q^{\\text{q\\_prec}}`. (So its error is `O(q^
    {\\text{q\\_prec} + 1})`.)

    REFERENCE:

    Cohen\'s "A Course in Computational Algebraic Number Theory" book, p 102.

    EXAMPLES:

    Check the sum of 4 squares form against Jacobi\'s formula::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: Theta = Q.theta_by_cholesky(10)
        sage: Theta
        1 + 8*q + 24*q^2 + 32*q^3 + 24*q^4 + 48*q^5 + 96*q^6
         + 64*q^7 + 24*q^8 + 104*q^9 + 144*q^10
        sage: Expected = [1] + [8*sum(d for d in divisors(n) if d%4)
        ....:                   for n in range(1, 11)]
        sage: Expected
        [1, 8, 24, 32, 24, 48, 96, 64, 24, 104, 144]
        sage: Theta.list() == Expected
        True

    Check the form `x^2 + 3y^2 + 5z^2 + 7w^2` represents everything except 2 and 22.::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,3,5,7])
        sage: Theta = Q.theta_by_cholesky(50)
        sage: Theta_list = Theta.list()
        sage: [m  for m in range(len(Theta_list))  if Theta_list[m] == 0]
        [2, 22]
    '''
def theta_series_degree_2(Q, prec) -> dict:
    """
    Compute the theta series of degree 2 for the quadratic form `Q`.

    INPUT:

    - ``prec`` -- integer

    OUTPUT: dictionary, where:

    - keys are `{\\rm GL}_2(\\ZZ)`-reduced binary quadratic forms (given as triples of
      coefficients)
    - values are coefficients

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: Q2 = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1])
        sage: S = Q2.theta_series_degree_2(10)
        sage: S[(0,0,2)]
        24
        sage: S[(1,0,1)]
        144
        sage: S[(1,1,1)]
        192

    AUTHORS:

    - Gonzalo Tornaria (2010-03-23)

    REFERENCE:

    - Raum, Ryan, Skoruppa, Tornaria, 'On Formal Siegel Modular Forms'
      (preprint)
    """
