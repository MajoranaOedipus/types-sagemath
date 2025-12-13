from sage.arith.misc import bernoulli as bernoulli, factorial as factorial, fundamental_discriminant as fundamental_discriminant
from sage.misc.functional import denominator as denominator
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

def gamma__exact(n):
    """
    Evaluates the exact value of the `\\Gamma` function at an integer or
    half-integer argument.

    EXAMPLES::

        sage: gamma__exact(4)
        6
        sage: gamma__exact(3)
        2
        sage: gamma__exact(2)
        1
        sage: gamma__exact(1)
        1

        sage: # needs sage.symbolic
        sage: gamma__exact(1/2)
        sqrt(pi)
        sage: gamma__exact(3/2)
        1/2*sqrt(pi)
        sage: gamma__exact(5/2)
        3/4*sqrt(pi)
        sage: gamma__exact(7/2)
        15/8*sqrt(pi)

        sage: # needs sage.symbolic
        sage: gamma__exact(-1/2)
        -2*sqrt(pi)
        sage: gamma__exact(-3/2)
        4/3*sqrt(pi)
        sage: gamma__exact(-5/2)
        -8/15*sqrt(pi)
        sage: gamma__exact(-7/2)
        16/105*sqrt(pi)

    TESTS::

        sage: gamma__exact(1/3)
        Traceback (most recent call last):
        ...
        TypeError: you must give an integer or half-integer argument
    """
def zeta__exact(n):
    '''
    Return the exact value of the Riemann Zeta function.

    The argument must be a critical value, namely either positive even
    or negative odd.

    See for example [Iwa1972]_, p13, Special value of `\\zeta(2k)`

    EXAMPLES:

    Let us test the accuracy for negative special values::

        sage: RR = RealField(100)
        sage: for i in range(1,10):                                                     # needs sage.symbolic
        ....:     print("zeta({}): {}".format(1 - 2*i,
        ....:                                 RR(zeta__exact(1-2*i)) - zeta(RR(1-2*i))))
        zeta(-1): 0.00000000000000000000000000000
        zeta(-3): 0.00000000000000000000000000000
        zeta(-5): 0.00000000000000000000000000000
        zeta(-7): 0.00000000000000000000000000000
        zeta(-9): 0.00000000000000000000000000000
        zeta(-11): 0.00000000000000000000000000000
        zeta(-13): 0.00000000000000000000000000000
        zeta(-15): 0.00000000000000000000000000000
        zeta(-17): 0.00000000000000000000000000000

    Let us test the accuracy for positive special values::

        sage: all(abs(RR(zeta__exact(2*i)) - zeta(RR(2*i))) < 10**(-28)                 # needs sage.symbolic
        ....:     for i in range(1,10))
        True

    TESTS::

        sage: zeta__exact(4)                                                            # needs sage.symbolic
        1/90*pi^4
        sage: zeta__exact(-3)
        1/120
        sage: zeta__exact(0)
        -1/2
        sage: zeta__exact(5)
        Traceback (most recent call last):
        ...
        TypeError: n must be a critical value (i.e. even > 0 or odd < 0)

    REFERENCES:

    - [Iwa1972]_
    - [IR1990]_
    - [Was1997]_
    '''
def QuadraticBernoulliNumber(k, d):
    """
    Compute `k`-th Bernoulli number for the primitive
    quadratic character associated to `\\chi(x) = \\left(\\frac{d}{x}\\right)`.

    EXAMPLES:

    Let us create a list of some odd negative fundamental discriminants::

        sage: test_set = [d for d in srange(-163, -3, 4)                                # needs sage.libs.pari
        ....:             if d.is_fundamental_discriminant()]

    In general, we have `B_{1, \\chi_d} = -2 h/w` for odd negative fundamental
    discriminants::

        sage: all(QuadraticBernoulliNumber(1, d)                                        # needs sage.libs.pari
        ....:       == -len(BinaryQF_reduced_representatives(d))
        ....:     for d in test_set)
        True

    REFERENCES:

    - [Iwa1972]_, pp 7-16.
    """
def quadratic_L_function__exact(n, d):
    """
    Return the exact value of a quadratic twist of the Riemann Zeta function
    by `\\chi_d(x) = \\left(\\frac{d}{x}\\right)`.

    The input `n` must be a critical value.

    EXAMPLES::

        sage: quadratic_L_function__exact(1, -4)                                        # needs sage.libs.pari sage.symbolic
        1/4*pi
        sage: quadratic_L_function__exact(-4, -4)                                       # needs sage.libs.pari
        5/2
        sage: quadratic_L_function__exact(2, 1)                                         # needs sage.libs.pari sage.symbolic
        1/6*pi^2

    TESTS::

        sage: quadratic_L_function__exact(2, -4)                                        # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        TypeError: n must be a critical value (i.e. odd > 0 or even <= 0)

    REFERENCES:

    - [Iwa1972]_, pp 16-17, Special values of `L(1-n, \\chi)` and `L(n, \\chi)`
    - [IR1990]_
    - [Was1997]_
    """
def quadratic_L_function__numerical(n, d, num_terms: int = 1000):
    '''
    Evaluate the Dirichlet `L`-function (for quadratic character) numerically
    (in a very naive way).

    EXAMPLES:

    First, let us test several values for a given character::

        sage: RR = RealField(100)
        sage: for i in range(5):                                                        # needs sage.symbolic
        ....:     print("L({}, (-4/.)): {}".format(1+2*i,
        ....:             RR(quadratic_L_function__exact(1+2*i, -4))
        ....:                - quadratic_L_function__numerical(RR(1+2*i), -4, 10000)))
        L(1, (-4/.)): 0.000049999999500000024999996962707
        L(3, (-4/.)): 4.99999970000003...e-13
        L(5, (-4/.)): 4.99999922759382...e-21
        L(7, (-4/.)): ...e-29
        L(9, (-4/.)): ...e-29

    This procedure fails for negative special values, as the Dirichlet
    series does not converge here::

        sage: quadratic_L_function__numerical(-3, -4, 10000)
        Traceback (most recent call last):
        ...
        ValueError: the Dirichlet series does not converge here

    Test for several characters that the result agrees with the exact
    value, to a given accuracy ::

        sage: for d in range(-20,0):            # long time (2s on sage.math 2014), needs sage.symbolic
        ....:     if abs(RR(quadratic_L_function__numerical(1, d, 10000)
        ....:                - quadratic_L_function__exact(1, d))) > 0.001:
        ....:         print("We have a problem at d = {}: exact = {}, numerical = {}".format(d,
        ....:                   RR(quadratic_L_function__exact(1, d)),
        ....:                   RR(quadratic_L_function__numerical(1, d))))
    '''
