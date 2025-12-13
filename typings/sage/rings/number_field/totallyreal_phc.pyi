def coefficients_to_power_sums(n, m, a):
    """
    Take the list ``a``, representing a list of initial coefficients of
    a (monic) polynomial of degree `n`, and return the power sums
    of the roots of `f` up to `(m-1)`-th powers.

    INPUT:

    - ``n`` -- integer; the degree
    - ``a`` -- list of integers; the coefficients

    OUTPUT: list of integers

    .. NOTE::

        This uses Newton's relations, which are classical.

    EXAMPLES::

        sage: from sage.rings.number_field.totallyreal_phc import coefficients_to_power_sums
        sage: coefficients_to_power_sums(3,2,[1,5,7])
        [3, -7, 39]
        sage: coefficients_to_power_sums(5,4,[1,5,7,9,8])
        [5, -8, 46, -317, 2158]
    """
