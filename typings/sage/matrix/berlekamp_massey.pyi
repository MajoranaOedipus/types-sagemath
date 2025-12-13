def berlekamp_massey(a):
    '''
    Use the Berlekamp-Massey algorithm to find the minimal polynomial
    of a linear recurrence sequence `a`.

    The minimal polynomial of a linear recurrence `\\{a_r\\}` is
    by definition the unique monic polynomial `g`, such that if
    `\\{a_r\\}` satisfies a linear recurrence
    `a_{j+k} + b_{j-1} a_{j-1+k} + \\cdots + b_0 a_k=0`
    (for all `k\\geq 0`), then `g` divides the
    polynomial `x^j + \\sum_{i=0}^{j-1} b_i x^i`.

    INPUT:

    - ``a`` -- list of even length of elements of a field (or domain)

    OUTPUT:

    the minimal polynomial of the sequence, as a polynomial over the
    field in which the entries of `a` live

    .. WARNING::

         The result is only guaranteed to be correct on the full
         sequence if there exists a linear recurrence of length less
         than half the length of `a`.

    EXAMPLES::

        sage: from sage.matrix.berlekamp_massey import berlekamp_massey
        sage: berlekamp_massey([1,2,1,2,1,2])
        x^2 - 1
        sage: berlekamp_massey([GF(7)(1), 19, 1, 19])
        x^2 + 6
        sage: berlekamp_massey([2,2,1,2,1,191,393,132])
        x^4 - 36727/11711*x^3 + 34213/5019*x^2 + 7024942/35133*x - 335813/1673
        sage: berlekamp_massey(prime_range(2, 38))                                      # needs sage.libs.pari
        x^6 - 14/9*x^5 - 7/9*x^4 + 157/54*x^3 - 25/27*x^2 - 73/18*x + 37/9

    TESTS::

        sage: berlekamp_massey("banana")
        Traceback (most recent call last):
        ...
        TypeError: argument must be a list or tuple
        sage: berlekamp_massey([1,2,5])
        Traceback (most recent call last):
        ...
        ValueError: argument must have an even number of terms
    '''
