from _typeshed import Incomplete
from sage.misc.cachefunc import cached_function as cached_function
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing, ZZ as ZZ
from sage.rings.number_field.number_field_element_base import NumberFieldElement_base as NumberFieldElement_base
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

@cached_function
def hilbert_class_polynomial(D, algorithm=None):
    '''
    Return the Hilbert class polynomial for discriminant `D`.

    INPUT:

    - ``D`` -- negative integer congruent to 0 or 1 modulo 4

    - ``algorithm`` -- string (default: ``None``)

    OUTPUT:

    (integer polynomial) The Hilbert class polynomial for the
    discriminant `D`.

    ALGORITHM:

    - If ``algorithm`` = "arb" (default): Use FLINT\'s implementation inherited
      from Arb which uses complex interval arithmetic.

    - If ``algorithm`` = "sage": Use complex approximations to the roots.

    - If ``algorithm`` = "magma": Call the appropriate Magma function (if available).

    AUTHORS:

    - Sage implementation originally by Eduardo Ocampo Alvarez and
      AndreyTimofeev

    - Sage implementation corrected by John Cremona (using corrected precision bounds from Andreas Enge)

    - Magma implementation by David Kohel

    EXAMPLES::

        sage: # needs sage.libs.flint
        sage: hilbert_class_polynomial(-4)
        x - 1728
        sage: hilbert_class_polynomial(-7)
        x + 3375
        sage: hilbert_class_polynomial(-23)
        x^3 + 3491750*x^2 - 5151296875*x + 12771880859375
        sage: hilbert_class_polynomial(-37*4)
        x^2 - 39660183801072000*x - 7898242515936467904000000
        sage: hilbert_class_polynomial(-37*4, algorithm=\'magma\') # optional - magma
        x^2 - 39660183801072000*x - 7898242515936467904000000
        sage: hilbert_class_polynomial(-163)
        x + 262537412640768000
        sage: hilbert_class_polynomial(-163, algorithm=\'sage\')
        x + 262537412640768000
        sage: hilbert_class_polynomial(-163, algorithm=\'magma\') # optional - magma
        x + 262537412640768000

    TESTS::

        sage: all(hilbert_class_polynomial(d, algorithm=\'arb\') ==
        ....:      hilbert_class_polynomial(d, algorithm=\'sage\')
        ....:        for d in range(-1,-100,-1) if d % 4 in [0, 1])
        True
    '''
def is_HCP(f, check_monic_irreducible: bool = True):
    """
    Determine whether a polynomial is a Hilbert Class Polynomial.

    INPUT:

    - ``f`` -- a polynomial in `\\ZZ[X]`
    - ``check_monic_irreducible`` -- boolean (default: ``True``); if ``True``,
      check that ``f`` is a monic, irreducible, integer polynomial

    OUTPUT:

    (integer) -- either `D` if ``f`` is the Hilbert Class Polynomial
    `H_D` for discriminant `D`, or `0` if not an HCP.

    ALGORITHM:

    Cremona and Sutherland: Algorithm 2 of [CreSuth2023]_.

    EXAMPLES:

    Even for large degrees this is fast.  We test the largest
    discriminant of class number 100, for which the HCP has coefficients
    with thousands of digits::

        sage: from sage.schemes.elliptic_curves.cm import is_HCP
        sage: D = -1856563
        sage: D.class_number()                                                          # needs sage.libs.pari
        100

        sage: # needs sage.libs.flint
        sage: H = hilbert_class_polynomial(D)
        sage: H.degree()
        100
        sage: max(H).ndigits()
        2774
        sage: is_HCP(H)
        -1856563

    Testing polynomials which are not HCPs is faster::

        sage: is_HCP(H+1)                                                               # needs sage.libs.flint
        0


    TESTS::

        sage: # needs sage.libs.flint
        sage: from sage.schemes.elliptic_curves.cm import is_HCP
        sage: all(is_HCP(hilbert_class_polynomial(D)) == D
        ....:     for D in srange(-4,-100,-1) if D.is_discriminant())
        True
        sage: all(not is_HCP(hilbert_class_polynomial(D) + 1)
        ....:     for D in srange(-4,-100,-1) if D.is_discriminant())
        True

    Ensure that :issue:`37471` is fixed::

        sage: from sage.schemes.elliptic_curves.cm import is_HCP
        sage: set_random_seed(297388353221545796156853787333338705098)
        sage: is_HCP(hilbert_class_polynomial(-55))
        -55
    """
def OrderClassNumber(D0, h0, f):
    """
    Return the class number h(f**2 * D0), given h(D0)=h0.

    INPUT:

    - ``D0`` -- integer; a negative fundamental discriminant
    - ``h0`` -- integer; the class number of the (maximal) imaginary quadratic order of discriminant ``D0``
    - ``f`` -- positive integer

    OUTPUT:

    (integer) the class number of the imaginary quadratic order of discriminant ``D0*f**2``

    ALGORITHM:

    We use the formula for the class number of the order `\\mathcal{O}_{D}` in terms of the class number of the
     maximal order  `\\mathcal{O}_{D_0}`; see [Cox1989]_ Theorem 7.24:

    .. MATH::

        h(D) = \\frac{h(D_0)f}{[\\mathcal{O}_{D_0}^\\times:\\mathcal{O}_{D}^\\times]}\\prod_{p\\,|\\,f}\\left(1-\\left(\\frac{D_0}{p}\\right)\\frac{1}{p}\\right)

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: from sage.schemes.elliptic_curves.cm import OrderClassNumber
        sage: D0 = -4
        sage: h = D0.class_number()
        sage: [OrderClassNumber(D0,h,f) for f in srange(1,20)]
        [1, 1, 2, 2, 2, 4, 4, 4, 6, 4, 6, 8, 6, 8, 8, 8, 8, 12, 10]
        sage: all([OrderClassNumber(D0,h,f) == (D0*f**2).class_number() for f in srange(1,20)])
        True
    """
@cached_function
def cm_j_invariants(K, proof=None):
    """
    Return a list of all CM `j`-invariants in the field `K`.

    INPUT:

    - ``K`` -- a number field
    - ``proof`` -- (default: proof.number_field())

    OUTPUT:

    (list) -- A list of CM `j`-invariants in the field `K`.

    EXAMPLES::

        sage: cm_j_invariants(QQ)
        [-262537412640768000, -147197952000, -884736000, -12288000, -884736,
         -32768, -3375, 0, 1728, 8000, 54000, 287496, 16581375]

    Over imaginary quadratic fields there are no more than over `QQ`::

        sage: cm_j_invariants(QuadraticField(-1, 'i'))                                  # needs sage.rings.number_field
        [-262537412640768000, -147197952000, -884736000, -12288000, -884736,
         -32768, -3375, 0, 1728, 8000, 54000, 287496, 16581375]

    Over real quadratic fields there may be more, for example::

        sage: len(cm_j_invariants(QuadraticField(5, 'a')))                              # needs sage.rings.number_field
        31

    Over number fields K of many higher degrees this also works::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 2)
        sage: cm_j_invariants(K)
        [-262537412640768000, -147197952000, -884736000, -884736, -32768,
         8000, -3375, 16581375, 1728, 287496, 0, 54000, -12288000,
         31710790944000*a^2 + 39953093016000*a + 50337742902000]
        sage: K.<a> = NumberField(x^4 - 2)
        sage: len(cm_j_invariants(K))
        23
    """
@cached_function
def cm_j_invariants_and_orders(K, proof=None):
    """
    Return a list of all CM `j`-invariants in the field `K`, together with the associated orders.

    INPUT:

    - ``K`` -- a number field
    - ``proof`` -- (default: proof.number_field())

    OUTPUT:

    A list of 3-tuples `(D,f,j)` where `j` is a CM `j`-invariant in `K` with
    quadratic fundamental discriminant `D` and conductor `f`.

    EXAMPLES::

        sage: cm_j_invariants_and_orders(QQ)
        [(-3, 3, -12288000), (-3, 2, 54000), (-3, 1, 0), (-4, 2, 287496), (-4, 1, 1728),
         (-7, 2, 16581375), (-7, 1, -3375), (-8, 1, 8000), (-11, 1, -32768),
         (-19, 1, -884736), (-43, 1, -884736000), (-67, 1, -147197952000),
         (-163, 1, -262537412640768000)]

    Over an imaginary quadratic field there are no more than over `QQ`::

        sage: cm_j_invariants_and_orders(QuadraticField(-1, 'i'))                       # needs sage.rings.number_field
        [(-163, 1, -262537412640768000), (-67, 1, -147197952000),
         (-43, 1, -884736000), (-19, 1, -884736), (-11, 1, -32768),
         (-8, 1, 8000), (-7, 1, -3375), (-7, 2, 16581375), (-4, 1, 1728),
         (-4, 2, 287496), (-3, 1, 0), (-3, 2, 54000), (-3, 3, -12288000)]

    Over real quadratic fields there may be more::

        sage: v = cm_j_invariants_and_orders(QuadraticField(5,'a')); len(v)             # needs sage.rings.number_field
        31
        sage: [(D, f) for D, f, j in v if j not in QQ]                                  # needs sage.rings.number_field
        [(-235, 1), (-235, 1), (-115, 1), (-115, 1), (-40, 1), (-40, 1),
         (-35, 1), (-35, 1), (-20, 1), (-20, 1), (-15, 1), (-15, 1), (-15, 2),
         (-15, 2), (-4, 5), (-4, 5), (-3, 5), (-3, 5)]

    Over number fields K of many higher degrees this also works::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 2)                                              # needs sage.rings.number_field
        sage: cm_j_invariants_and_orders(K)                                             # needs sage.rings.number_field
        [(-163, 1, -262537412640768000), (-67, 1, -147197952000),
         (-43, 1, -884736000), (-19, 1, -884736), (-11, 1, -32768),
         (-8, 1, 8000), (-7, 1, -3375), (-7, 2, 16581375), (-4, 1, 1728),
         (-4, 2, 287496), (-3, 1, 0), (-3, 2, 54000), (-3, 3, -12288000),
         (-3, 6, 31710790944000*a^2 + 39953093016000*a + 50337742902000)]
    """
@cached_function
def cm_orders(h, proof=None):
    """
    Return a list of all pairs `(D,f)` where there is a CM order of
    discriminant `D f^2` with class number h, with `D` a fundamental
    discriminant.

    INPUT:

    - ``h`` -- positive integer
    - ``proof`` -- (default: proof.number_field())

    OUTPUT: list of 2-tuples `(D,f)` sorted lexicographically by `(|D|, f)`

    EXAMPLES::

        sage: cm_orders(0)
        []
        sage: v = cm_orders(1); v
        [(-3, 1), (-3, 2), (-3, 3), (-4, 1), (-4, 2), (-7, 1), (-7, 2), (-8, 1),
         (-11, 1), (-19, 1), (-43, 1), (-67, 1), (-163, 1)]
        sage: type(v[0][0]), type(v[0][1])
        (<... 'sage.rings.integer.Integer'>, <... 'sage.rings.integer.Integer'>)
        sage: # needs sage.libs.pari
        sage: v = cm_orders(2); v
         [(-3, 4), (-3, 5), (-3, 7), (-4, 3), (-4, 4), (-4, 5), (-7, 4), (-8, 2),
          (-8, 3), (-11, 3), (-15, 1), (-15, 2), (-20, 1), (-24, 1), (-35, 1),
          (-40, 1), (-51, 1), (-52, 1), (-88, 1), (-91, 1), (-115, 1), (-123, 1),
          (-148, 1), (-187, 1), (-232, 1), (-235, 1), (-267, 1), (-403, 1), (-427, 1)]
        sage: len(v)
        29
        sage: set([hilbert_class_polynomial(D*f^2).degree() for D,f in v])
        {2}

    Any degree up to 100 is implemented, but may be slow::

        sage: # needs sage.libs.pari
        sage: cm_orders(3)
        [(-3, 6), (-3, 9), (-11, 2), (-19, 2), (-23, 1), (-23, 2), (-31, 1), (-31, 2),
         (-43, 2), (-59, 1), (-67, 2), (-83, 1), (-107, 1), (-139, 1), (-163, 2),
         (-211, 1), (-283, 1), (-307, 1), (-331, 1), (-379, 1), (-499, 1), (-547, 1),
         (-643, 1), (-883, 1), (-907, 1)]
        sage: len(cm_orders(4))
        84
    """

watkins_table: Incomplete
klaise_table: Incomplete

def largest_fundamental_disc_with_class_number(h):
    """
    Return largest absolute value of any fundamental negative discriminant with
    class number `h`, and the number of fundamental negative discriminants with
    that class number.  This is known (unconditionally) for `h` up to 100,
    by work of Mark Watkins ([Watkins2004]_).

    .. NOTE::

        The class number of a fundamental negative discriminant `D` is
        the same as the class number of the imaginary quadratic field
        `\\QQ(\\sqrt{D})`, so this function gives the number of such
        fields of each class number `h\\le100`.  It is easy to extend
        this to larger class number conditional on the GRH, but much
        harder to obtain unconditional results.

    INPUT:

    - ``h`` -- integer

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.cm import largest_fundamental_disc_with_class_number
        sage: largest_fundamental_disc_with_class_number(0)
        (0, 0)
        sage: largest_fundamental_disc_with_class_number(1)
        (163, 9)
        sage: largest_fundamental_disc_with_class_number(2)
        (427, 18)
        sage: largest_fundamental_disc_with_class_number(10)
        (13843, 87)
        sage: largest_fundamental_disc_with_class_number(100)
        (1856563, 1736)
        sage: largest_fundamental_disc_with_class_number(101)
        Traceback (most recent call last):
        ...
        NotImplementedError: largest fundamental discriminant not available for class number 101
    """
def largest_disc_with_class_number(h):
    """
    Return largest absolute value of any negative discriminant with
    class number `h`, and the number of fundamental negative
    discriminants with that class number.  This is known
    (unconditionally) for `h` up to 100, by work of Mark Watkins
    [Watkins2004]_ for fundamental discriminants, extended to all
    discriminants of class number `h\\le100` by Klaise [Klaise2012]_.

    .. NOTE::

        The class number of a negative discriminant `D` is
        the same as the class number of the unique imaginary quadratic order
        of discriminant `D`, so this function gives the number of such
        orders of each class number `h\\le100`.  It is easy to extend
        this to larger class number conditional on the GRH, but much
        harder to obyain unconditional results.

    INPUT:

    - ``h`` -- integer

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.cm import largest_disc_with_class_number
        sage: largest_disc_with_class_number(0)
        (0, 0)
        sage: largest_disc_with_class_number(1)
        (163, 13)
        sage: largest_disc_with_class_number(2)
        (427, 29)
        sage: largest_disc_with_class_number(10)
        (13843, 123)
        sage: largest_disc_with_class_number(100)
        (1856563, 2311)
        sage: largest_disc_with_class_number(101)
        Traceback (most recent call last):
        ...
        NotImplementedError: largest discriminant not available for class number 101

    For most `h\\le100`, the largest fundamental discriminant with
    class number `h` is also the largest discriminant, but this is not
    the case for some `h`::

        sage: from sage.schemes.elliptic_curves.cm import largest_disc_with_class_number, largest_fundamental_disc_with_class_number
        sage: [h for h in range(1,101) if largest_disc_with_class_number(h)[0] != largest_fundamental_disc_with_class_number(h)[0]]
        [6, 8, 12, 16, 20, 30, 40, 42, 52, 70]
        sage: largest_fundamental_disc_with_class_number(6)
        (3763, 51)
        sage: largest_disc_with_class_number(6)
        (4075, 101)
    """

hDf_dict: Incomplete

def discriminants_with_bounded_class_number(hmax, B=None, proof=None):
    """Return a dictionary with keys class numbers `h\\le hmax` and values the
    list of all pairs `(D_0, f)`, with `D_0<0` a fundamental discriminant such
    that `D=D_0f^2` has class number `h`.  If the optional bound `B` is given,
    return only those pairs with `|D| \\le B`.

    INPUT:

    - ``hmax`` -- integer
    - ``B`` -- integer or ``None``; if ``None`` returns all pairs
    - ``proof`` -- this code calls the PARI function :pari:`qfbclassno`, so it
      could give wrong answers when ``proof``==``False`` (though only for
      discriminants greater than `2\\cdot10^{10}`).  The default is
      the current value of ``proof.number_field()``.

    OUTPUT: dictionary

    .. NOTE::

       In case `B` is not given, then ``hmax`` must be at most 100; we
       use the tables from [Watkins2004]_ and [Klaise2012]_ to compute
       a `B` that captures all `h` up to `hmax`.

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: from sage.schemes.elliptic_curves.cm import discriminants_with_bounded_class_number
        sage: v = discriminants_with_bounded_class_number(3)
        sage: sorted(v)
        [1, 2, 3]
        sage: v[1]
        [(-3, 1), (-3, 2), (-3, 3), (-4, 1), (-4, 2), (-7, 1), (-7, 2), (-8, 1),
         (-11, 1), (-19, 1), (-43, 1), (-67, 1), (-163, 1)]
        sage: v[2]
        [(-3, 4), (-3, 5), (-3, 7), (-4, 3), (-4, 4), (-4, 5), (-7, 4), (-8, 2),
         (-8, 3), (-11, 3), (-15, 1), (-15, 2), (-20, 1), (-24, 1), (-35, 1), (-40, 1),
         (-51, 1), (-52, 1), (-88, 1), (-91, 1), (-115, 1), (-123, 1), (-148, 1),
         (-187, 1), (-232, 1), (-235, 1), (-267, 1), (-403, 1), (-427, 1)]
        sage: v[3]
        [(-3, 6), (-3, 9), (-11, 2), (-19, 2), (-23, 1), (-23, 2), (-31, 1), (-31, 2),
         (-43, 2), (-59, 1), (-67, 2), (-83, 1), (-107, 1), (-139, 1), (-163, 2),
         (-211, 1), (-283, 1), (-307, 1), (-331, 1), (-379, 1), (-499, 1), (-547, 1),
         (-643, 1), (-883, 1), (-907, 1)]
        sage: v = discriminants_with_bounded_class_number(8, proof=False)
        sage: sorted(len(v[h]) for h in v)
        [13, 25, 29, 29, 38, 84, 101, 208]

    Find all class numbers for discriminant up to 50::

        sage: sage.schemes.elliptic_curves.cm.discriminants_with_bounded_class_number(hmax=5, B=50)
        {1: [(-3, 1), (-3, 2), (-3, 3), (-4, 1), (-4, 2), (-7, 1), (-7, 2), (-8, 1), (-11, 1), (-19, 1), (-43, 1)], 2: [(-3, 4), (-4, 3), (-8, 2), (-15, 1), (-20, 1), (-24, 1), (-35, 1), (-40, 1)], 3: [(-11, 2), (-23, 1), (-31, 1)], 4: [(-39, 1)], 5: [(-47, 1)]}
    """
@cached_function
def is_cm_j_invariant(j, algorithm: str = 'CremonaSutherland', method=None):
    """Return whether or not this is a CM `j`-invariant, and the CM discriminant if it is.

    INPUT:

    - ``j`` -- an element of a number field `K`

    - ``algorithm`` -- string (default: ``'CremonaSutherland'``); the algorithm
      used, either ``'CremonaSutherland'`` (the default, very much faster
      for all but very small degrees), ``'exhaustive'`` or ``'reduction'``

    - ``method`` -- string; deprecated name for ``algorithm``

    OUTPUT:

    A pair (bool, (d,f)) which is either (False, None) if `j` is not a
    CM j-invariant or (True, (d,f)) if `j` is the `j`-invariant of the
    imaginary quadratic order of discriminant `D=df^2` where `d` is
    the associated fundamental discriminant and `f` the index.

    ALGORITHM:

    The default algorithm used is to test whether the minimal
    polynomial of ``j`` is a Hilbert CLass Polynomail, using
    :func:`is_HCP` which implements Algorithm 2 of [CreSuth2023]_ by
    Cremona and Sutherland.

    Two older algorithms are available, both of which are much slower
    except for very small degrees.

    Method 'exhaustive' makes use of the complete and unconditionsl classification of
    all orders of class number up to 100, and hence will raise an
    error if `j` is an algebraic integer of degree greater than
    this.

    Method 'reduction' constructs an elliptic curve over the number
    field `\\QQ(j)` and computes its traces of Frobenius at several
    primes of degree 1.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.cm import is_cm_j_invariant
        sage: is_cm_j_invariant(0)
        (True, (-3, 1))
        sage: is_cm_j_invariant(8000)
        (True, (-8, 1))

        sage: # needs sage.rings.number_field
        sage: K.<a> = QuadraticField(5)
        sage: is_cm_j_invariant(282880*a + 632000)
        (True, (-20, 1))
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 2)
        sage: is_cm_j_invariant(31710790944000*a^2 + 39953093016000*a + 50337742902000)
        (True, (-3, 6))

    An example of large degree.  This is only possible using the default algorithm::

        sage: from sage.schemes.elliptic_curves.cm import is_cm_j_invariant
        sage: D = -1856563
        sage: H = hilbert_class_polynomial(D)                                           # needs sage.libs.flint
        sage: H.degree()                                                                # needs sage.libs.flint
        100
        sage: K.<j> = NumberField(H)                                                    # needs sage.libs.flint sage.rings.number_field
        sage: is_cm_j_invariant(j)                                                      # needs sage.libs.flint sage.rings.number_field
        (True, (-1856563, 1))

    TESTS::

        sage: from sage.schemes.elliptic_curves.cm import is_cm_j_invariant
        sage: all(is_cm_j_invariant(j) == (True, (d,f)) for d,f,j in cm_j_invariants_and_orders(QQ))
        True
    """
