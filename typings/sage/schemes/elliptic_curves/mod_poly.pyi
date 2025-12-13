from sage.databases.db_modular_polynomials import ClassicalModularPolynomialDatabase as ClassicalModularPolynomialDatabase
from sage.libs.pari import pari as pari
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import parent as parent

def classical_modular_polynomial(l, j=None):
    '''
    Return the classical modular polynomial `\\Phi_\\ell`, either as a
    "generic" bivariate polynomial over `\\ZZ`, or as an "instantiated"
    modular polynomial where one variable has been replaced by the
    given `j`-invariant.

    Generic polynomials are cached up to a certain size of `\\ell`,
    which significantly accelerates subsequent invocations with the
    same `\\ell`. The default bound is `\\ell \\leq 100`, which can be
    adjusted using ``classical_modular_polynomial.set_cache_bound()``
    with a different value. Beware that modular polynomials are very
    big objects and the amount of memory consumed by the cache will
    grow rapidly when the bound is set to a large value.

    INPUT:

    - ``l`` -- positive integer
    - ``j`` -- either ``None`` or a ring element:

      * if ``None`` is given, the original modular polynomial
        is returned as an element of `\\ZZ[X,Y]`
      * if a ring element `j \\in R` is given, the evaluation
        `\\Phi_\\ell(j,Y)` is returned as an element of the
        univariate polynomial ring `R[Y]`

    ALGORITHMS:

    - The Kohel database
      :class:`~sage.databases.db_modular_polynomials.ClassicalModularPolynomialDatabase`
    - :pari:`polmodular`

    EXAMPLES::

        sage: classical_modular_polynomial(2)
        -X^2*Y^2 + X^3 + 1488*X^2*Y + 1488*X*Y^2 + Y^3 - 162000*X^2 + 40773375*X*Y - 162000*Y^2 + 8748000000*X + 8748000000*Y - 157464000000000
        sage: j = Mod(1728, 419)
        sage: classical_modular_polynomial(3, j)
        Y^4 + 230*Y^3 + 84*Y^2 + 118*Y + 329

    Increasing the cache size can be useful for repeated invocations::

        sage: %timeit classical_modular_polynomial(101)                              # not tested
        6.11 s ± 1.21 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
        sage: %timeit classical_modular_polynomial(101, GF(65537).random_element())  # not tested
        5.43 s ± 2.71 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

        sage: classical_modular_polynomial.set_cache_bound(150)                      # not tested
        sage: %timeit classical_modular_polynomial(101)                              # not tested
        The slowest run took 10.35 times longer than the fastest. This could mean that an intermediate result is being cached.
        1.84 µs ± 1.84 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
        sage: %timeit classical_modular_polynomial(101, GF(65537).random_element())  # not tested
        59.8 ms ± 29.4 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    TESTS::

        sage: q = random_prime(50)^randrange(1,4)
        sage: j = GF(q).random_element()
        sage: l = random_prime(50)
        sage: Y = polygen(parent(j), \'Y\')
        sage: classical_modular_polynomial(l, j) == classical_modular_polynomial(l)(j, Y)
        True
        sage: p = 2^216 * 3^137 - 1
        sage: F.<i> = GF((p,2), modulus=[1,0,1])
        sage: l = random_prime(50)
        sage: j = F.random_element()
        sage: Y = polygen(parent(j), \'Y\')
        sage: classical_modular_polynomial(l, j) == classical_modular_polynomial(l)(j, Y)
        True
        sage: E = EllipticCurve(F, [0, 6, 0, 1, 0])
        sage: j = E.j_invariant()
        sage: l = random_prime(50)
        sage: classical_modular_polynomial(l, j) == classical_modular_polynomial(l)(j, Y)
        True
        sage: R.<Y> = QQ[\'Y\']
        sage: j = QQ(1/2)
        sage: l = random_prime(50)
        sage: classical_modular_polynomial(l, j) == classical_modular_polynomial(l)(j, Y)
        True
    '''
