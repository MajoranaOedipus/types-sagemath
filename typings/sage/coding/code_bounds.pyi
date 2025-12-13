from .delsarte_bounds import delsarte_bound_additive_hamming_space as delsarte_bound_additive_hamming_space, delsarte_bound_hamming_space as delsarte_bound_hamming_space
from sage.arith.misc import binomial as binomial, is_prime_power as is_prime_power
from sage.features.gap import GapPackage as GapPackage
from sage.misc.functional import log as log, sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF

def codesize_upper_bound(n, d, q, algorithm=None):
    '''
    Return an upper bound on the number of codewords in a (possibly non-linear)
    code.

    This function computes the minimum value of the upper bounds of Singleton,
    Hamming, Plotkin, and Elias.

    If ``algorithm="gap"``, then this returns the best known upper
    bound `A(n,d)=A_q(n,d)` for the size of a code of length `n`,
    minimum distance `d` over a field of size `q`. The function first
    checks for trivial cases (like `d=1` or `n=d`), and if the value
    is in the built-in table. Then it calculates the minimum value
    of the upper bound using the algorithms of Singleton, Hamming,
    Johnson, Plotkin and Elias. If the code is binary,
    `A(n, 2\\ell-1) = A(n+1,2\\ell)`, so the function
    takes the minimum of the values obtained from all algorithms for the
    parameters `(n, 2\\ell-1)` and `(n+1, 2\\ell)`. This
    wraps GUAVA\'s (i.e. GAP\'s package Guava) ``UpperBound(n, d, q)``.

    If ``algorithm="LP"``, then this returns the Delsarte (a.k.a. Linear
    Programming) upper bound.

    EXAMPLES::

        sage: codes.bounds.codesize_upper_bound(10, 3, 2)
        93
        sage: codes.bounds.codesize_upper_bound(24, 8, 2, algorithm=\'LP\')               # needs sage.numerical.mip
        4096
        sage: codes.bounds.codesize_upper_bound(10, 3, 2, algorithm=\'gap\')              # optional - gap_package_guava
        85
        sage: codes.bounds.codesize_upper_bound(11, 3, 4, algorithm=None)               # needs sage.symbolic
        123361
        sage: codes.bounds.codesize_upper_bound(11, 3, 4, algorithm=\'gap\')              # optional - gap_package_guava
        123361
        sage: codes.bounds.codesize_upper_bound(11, 3, 4, algorithm=\'LP\')               # needs sage.numerical.mip
        109226

    TESTS:

    Make sure :issue:`22961` is fixed::

        sage: codes.bounds.codesize_upper_bound(19, 10, 2)
        20
        sage: codes.bounds.codesize_upper_bound(19, 10, 2, algorithm=\'gap\')            # optional - gap_package_guava
        20

    Meaningless parameters are rejected::

        sage: codes.bounds.codesize_upper_bound(10, -20, 6)
        Traceback (most recent call last):
        ...
        ValueError: The length or minimum distance does not make sense
    '''
def dimension_upper_bound(n, d, q, algorithm=None):
    """
    Return an upper bound for the dimension of a linear code.

    Return an upper bound `B(n,d) = B_q(n,d)` for the
    dimension of a linear code of length `n`, minimum distance `d` over a
    field of size `q`.

    Parameter ``algorithm`` has the same meaning as in
    :func:`codesize_upper_bound`

    EXAMPLES::

        sage: codes.bounds.dimension_upper_bound(10,3,2)                                # needs sage.libs.pari sage.symbolic
        6
        sage: codes.bounds.dimension_upper_bound(30,15,4)                               # needs sage.libs.pari sage.symbolic
        13
        sage: codes.bounds.dimension_upper_bound(30,15,4,algorithm='LP')                # needs sage.libs.pari sage.numerical.mip
        12

    TESTS:

    Meaningless code parameters are rejected::

        sage: codes.bounds.dimension_upper_bound(13,3,6)                                # needs sage.libs.pari
        Traceback (most recent call last):
        ...
        ValueError: The alphabet size does not make sense for a code over a field
    """
def volume_hamming(n, q, r):
    """
    Return the number of elements in a Hamming ball.

    Return the number of elements in a Hamming ball of radius `r` in
    `\\GF{q}^n`.

    EXAMPLES::

        sage: codes.bounds.volume_hamming(10,2,3)
        176
    """
def gilbert_lower_bound(n, q, d):
    """
    Return the Gilbert-Varshamov lower bound.

    Return the Gilbert-Varshamov lower bound for number of elements in a largest code of
    minimum distance d in `\\GF{q}^n`. See :wikipedia:`Gilbert-Varshamov_bound`

    EXAMPLES::

        sage: codes.bounds.gilbert_lower_bound(10,2,3)
        128/7
    """
def plotkin_upper_bound(n, q, d, algorithm=None):
    '''
    Return the Plotkin upper bound.

    Return the Plotkin upper bound for the number of elements in a largest
    code of minimum distance `d` in `\\GF{q}^n`.
    More precisely this is a generalization of Plotkin\'s result for `q=2`
    to bigger `q` due to Berlekamp.

    The ``algorithm="gap"`` option wraps Guava\'s ``UpperBoundPlotkin``.

    EXAMPLES::

        sage: codes.bounds.plotkin_upper_bound(10,2,3)
        192
        sage: codes.bounds.plotkin_upper_bound(10,2,3,algorithm=\'gap\')  # optional - gap_package_guava
        192
    '''
def griesmer_upper_bound(n, q, d, algorithm=None):
    '''
    Return the Griesmer upper bound.

    Return the Griesmer upper bound for the number of elements in a
    largest linear code of minimum distance `d` in `\\GF{q}^n`, cf. [HP2003]_.
    If the method is "gap", it wraps GAP\'s ``UpperBoundGriesmer``.

    The bound states:

    .. MATH::

        `n\\geq \\sum_{i=0}^{k-1} \\lceil d/q^i \\rceil.`

    EXAMPLES:

    The bound is reached for the ternary Golay codes::

        sage: codes.bounds.griesmer_upper_bound(12,3,6)                                 # needs sage.libs.pari
        729
        sage: codes.bounds.griesmer_upper_bound(11,3,5)                                 # needs sage.libs.pari
        729

    ::

        sage: codes.bounds.griesmer_upper_bound(10,2,3)                                 # needs sage.libs.pari
        128
        sage: codes.bounds.griesmer_upper_bound(10,2,3,algorithm=\'gap\')                 # optional - gap_package_guava, needs sage.libs.pari
        128

    TESTS::

        sage: codes.bounds.griesmer_upper_bound(11,3,6)                                 # needs sage.libs.pari
        243
        sage: codes.bounds.griesmer_upper_bound(11,3,6)                                 # needs sage.libs.pari
        243
    '''
def elias_upper_bound(n, q, d, algorithm=None):
    '''
    Return the Elias upper bound.

    Return the Elias upper bound for number of elements in the largest
    code of minimum distance `d` in `\\GF{q}^n`, cf. [HP2003]_.
    If ``algorithm="gap"``, it wraps GAP\'s ``UpperBoundElias``.

    EXAMPLES::

        sage: codes.bounds.elias_upper_bound(10,2,3)
        232
        sage: codes.bounds.elias_upper_bound(10,2,3,algorithm=\'gap\')  # optional - gap_package_guava
        232
    '''
def hamming_upper_bound(n, q, d):
    """
    Return the Hamming upper bound.

    Return the Hamming upper bound for number of elements in the
    largest code of length `n` and minimum distance `d` over alphabet
    of size `q`.

    The Hamming bound (also known as the sphere packing bound) returns
    an upper bound on the size of a code of length `n`, minimum distance
    `d`, over an alphabet of size `q`. The Hamming bound is obtained by
    dividing the contents of the entire Hamming space
    `q^n` by the contents of a ball with radius
    `floor((d-1)/2)`. As all these balls are disjoint, they can never
    contain more than the whole vector space.


    .. MATH::

         M \\leq \\frac{q^n}{V(n,e)},


    where `M` is the maximum number of codewords and `V(n,e)` is
    equal to the contents of a ball of radius `e`. This bound is useful
    for small values of `d`. Codes for which equality holds are called
    perfect. See e.g. [HP2003]_.

    EXAMPLES::

        sage: codes.bounds.hamming_upper_bound(10,2,3)
        93
    """
def singleton_upper_bound(n, q, d):
    """
    Return the Singleton upper bound.

    Return the Singleton upper bound for number of elements in a
    largest code of minimum distance `d` in `\\GF{q}^n`.

    This bound is based on the shortening of codes. By shortening an
    `(n, M, d)` code `d-1` times, an `(n-d+1,M,1)` code
    results, with `M \\leq q^n-d+1`. Thus


    .. MATH::

         M \\leq q^{n-d+1}.


    Codes that meet this bound are called maximum distance separable
    (MDS).

    EXAMPLES::

        sage: codes.bounds.singleton_upper_bound(10,2,3)
        256
    """
def gv_info_rate(n, delta, q):
    """
    The Gilbert-Varshamov lower bound for information rate.

    The Gilbert-Varshamov lower bound for information rate of a `q`-ary code of
    length `n` and minimum distance `n\\delta`.

    EXAMPLES::

        sage: RDF(codes.bounds.gv_info_rate(100,1/4,3))  # abs tol 1e-15                # needs sage.libs.pari sage.symbolic
        0.36704992608261894
    """
def entropy(x, q: int = 2):
    """
    Compute the entropy at `x` on the `q`-ary symmetric channel.

    INPUT:

    - ``x`` -- real number in the interval `[0, 1]`

    - ``q`` -- (default: 2) integer greater than 1; this is the base of the
      logarithm

    EXAMPLES::

        sage: codes.bounds.entropy(0, 2)
        0
        sage: codes.bounds.entropy(1/5,4).factor()                                      # needs sage.symbolic
        1/10*(log(3) - 4*log(4/5) - log(1/5))/log(2)
        sage: codes.bounds.entropy(1, 3)                                                # needs sage.symbolic
        log(2)/log(3)

    Check that values not within the limits are properly handled::

        sage: codes.bounds.entropy(1.1, 2)
        Traceback (most recent call last):
        ...
        ValueError: The entropy function is defined only for x in the interval [0, 1]
        sage: codes.bounds.entropy(1, 1)
        Traceback (most recent call last):
        ...
        ValueError: The value q must be an integer greater than 1
    """
def entropy_inverse(x, q: int = 2):
    """
    Find the inverse of the `q`-ary entropy function at the point ``x``.

    INPUT:

    - ``x`` -- real number in the interval `[0, 1]`

    - ``q`` -- (default: 2) integer greater than 1; this is the base of the
      logarithm

    OUTPUT:

    Real number in the interval `[0, 1-1/q]`. The function has multiple
    values if we include the entire interval `[0, 1]`; hence only the
    values in the above interval is returned.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.coding.code_bounds import entropy_inverse
        sage: entropy_inverse(0.1)                                                      # needs scipy
        0.012986862055...
        sage: entropy_inverse(1)
        1/2
        sage: entropy_inverse(0, 3)
        0
        sage: entropy_inverse(1, 3)
        2/3
    """
def gv_bound_asymp(delta, q):
    """
    The asymptotic Gilbert-Varshamov bound for the information rate, R.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: RDF(codes.bounds.gv_bound_asymp(1/4,2))                                   # needs sage.libs.pari
        0.18872187554086...
        sage: f = lambda x: codes.bounds.gv_bound_asymp(x,2)
        sage: plot(f,0,1)                                                               # needs sage.libs.pari sage.plot
        Graphics object consisting of 1 graphics primitive
    """
def hamming_bound_asymp(delta, q):
    """
    The asymptotic Hamming bound for the information rate.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: RDF(codes.bounds.hamming_bound_asymp(1/4,2))                              # needs sage.libs.pari
        0.456435556800...
        sage: f = lambda x: codes.bounds.hamming_bound_asymp(x,2)
        sage: plot(f,0,1)                                                               # needs sage.libs.pari sage.plot
        Graphics object consisting of 1 graphics primitive
    """
def singleton_bound_asymp(delta, q):
    """
    The asymptotic Singleton bound for the information rate.

    EXAMPLES::

        sage: codes.bounds.singleton_bound_asymp(1/4,2)
        3/4
        sage: f = lambda x: codes.bounds.singleton_bound_asymp(x,2)
        sage: plot(f,0,1)                                                               # needs sage.plot
        Graphics object consisting of 1 graphics primitive
    """
def plotkin_bound_asymp(delta, q):
    """
    The asymptotic Plotkin bound for the information rate.

    This only makes sense when `0 < \\delta < 1-1/q`.

    EXAMPLES::

        sage: codes.bounds.plotkin_bound_asymp(1/4,2)
        1/2
    """
def elias_bound_asymp(delta, q):
    """
    The asymptotic Elias bound for the information rate.

    This only makes sense when `0 < \\delta < 1-1/q`.

    EXAMPLES::

        sage: codes.bounds.elias_bound_asymp(1/4,2)                                     # needs sage.symbolic
        0.39912396330...
    """
def mrrw1_bound_asymp(delta, q):
    """
    The first asymptotic McEliese-Rumsey-Rodemich-Welsh bound.

    This only makes sense when `0 < \\delta < 1-1/q`.

    EXAMPLES::

        sage: codes.bounds.mrrw1_bound_asymp(1/4,2)   # abs tol 4e-16                   # needs sage.symbolic
        0.3545789026652697
    """
