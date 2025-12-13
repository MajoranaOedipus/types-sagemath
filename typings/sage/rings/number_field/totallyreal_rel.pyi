from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial, divisors as divisors
from sage.libs.pari import pari as pari
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing, ZZ as ZZ
from sage.rings.number_field.number_field import NumberField as NumberField
from sage.rings.number_field.totallyreal import enumerate_totallyreal_fields_prim as enumerate_totallyreal_fields_prim, odlyzko_bound_totallyreal as odlyzko_bound_totallyreal, weed_fields as weed_fields
from sage.rings.number_field.totallyreal_data import ZZx as ZZx, hermite_constant as hermite_constant, int_has_small_square_divisor as int_has_small_square_divisor, lagrange_degree_3 as lagrange_degree_3
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

def integral_elements_in_box(K, C):
    """
    Return all integral elements of the totally real field `K` whose
    embeddings lie *numerically* within the bounds specified by the
    list ``C``.  The output is architecture dependent, and one may want
    to expand the bounds that define ``C`` by some epsilon.

    INPUT:

    - ``K`` -- a totally real number field
    - ``C`` -- list ``[[lower, upper], ...]`` of lower and upper bounds,
      for each embedding

    EXAMPLES::

        sage: x = polygen(QQ)
        sage: K.<alpha> = NumberField(x^2 - 2)
        sage: eps = 10e-6
        sage: C = [[0-eps, 5+eps], [0-eps, 10+eps]]
        sage: ls = sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, C)
        sage: sorted(a.trace() for a in ls)
        [0, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 10, 10, 10, 10, 12, 12, 14]
        sage: len(ls)
        19

        sage: v = sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, C)
        sage: sorted(v)
        [0, -alpha + 2, 1, -alpha + 3, 2, 3, alpha + 2, 4, alpha + 3, 5, alpha + 4,
         2*alpha + 3, alpha + 5, 2*alpha + 4, alpha + 6, 2*alpha + 5, 2*alpha + 6,
         3*alpha + 5, 2*alpha + 7]

    A cubic field::

        sage: x = polygen(QQ)
        sage: K.<a> = NumberField(x^3 - 16*x +16)
        sage: eps = 10e-6
        sage: C = [[0-eps,5+eps]]*3
        sage: v = sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, C)

    Note that the output is platform dependent (sometimes a 5 is listed
    below, and sometimes it isn't)::

        sage: sorted(v)
        [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4,...-1/4*a^2 - 1/2*a + 5,
         1/2*a + 3, -1/4*a^2 + 5]
    """

eps_global: Incomplete

class tr_data_rel:
    """
    This class encodes the data used in the enumeration of totally real
    fields for relative extensions.

    We do not give a complete description here.  For more information,
    see the attached functions; all of these are used internally by the
    functions in totallyreal_rel.py, so see that file for examples and
    further documentation.
    """
    m: Incomplete
    d: Incomplete
    n: Incomplete
    B: Incomplete
    gamma: Incomplete
    F: Incomplete
    Z_F: Incomplete
    Foo: Incomplete
    dF: Incomplete
    Fx: Incomplete
    beta: Incomplete
    gnk: Incomplete
    trace_elts: Incomplete
    a: Incomplete
    amaxvals: Incomplete
    k: Incomplete
    b_lower: Incomplete
    b_upper: Incomplete
    def __init__(self, F, m, B, a=None) -> None:
        """
        Initialization routine (constructor).

        INPUT:

        - ``F`` -- number field; the base field
        - ``m`` -- integer; the relative degree
        - ``B`` -- integer; the discriminant bound
        - ``a`` -- list (default: ``[]``); the coefficient list to begin with,
          corresponding to ``a[len(a)]*x^n + ... + a[0]x^(n-len(a))``

        OUTPUT:

        the data initialized to begin enumeration of totally real fields
        with base field `F`, degree `n`, discriminant bounded by `B`, and starting
        with coefficients `a`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<t> = NumberField(x^2 - 2)
            sage: T = sage.rings.number_field.totallyreal_rel.tr_data_rel(F, 2, 2000)
        """
    def incr(self, f_out, verbose: bool = False, haltk: int = 0) -> None:
        """
        'Increment' the totally real data to the next
        value which satisfies the bounds essentially given by Rolle's
        theorem, and return the next polynomial in the sequence
        ``f_out``.

        The default or usual case just increments the constant
        coefficient; then inductively, if this is outside of the
        bounds we increment the next higher coefficient, and so on.

        If there are no more coefficients to be had, returns the zero
        polynomial.

        INPUT:

        - ``f_out`` -- integer sequence; to be written with the coefficients of
          the next polynomial
        - ``verbose`` -- boolean or nonnegative integer (default: ``False``);
          print verbosely computational details. It prints extra information if
          ``verbose`` is set to ``2`` or more.
        - ``haltk`` -- integer; the level at which to halt the inductive
          coefficient bounds

        OUTPUT: the successor polynomial as a coefficient list
        """

def enumerate_totallyreal_fields_rel(F, m, B, a=[], verbose: int = 0, return_seqs: bool = False, return_pari_objects: bool = True):
    """
    This function enumerates (primitive) totally real field extensions of
    degree `m>1` of the totally real field F with discriminant `d \\leq B`;
    optionally one can specify the first few coefficients, where the sequence ``a``
    corresponds to a polynomial by

    ::

        a[k]*x^m + ... + a[0]*x^(m-k)

    if ``length(a) = k+1``, so in particular always ``a[k] = 1``.

    .. NOTE::

        This is guaranteed to give all primitive such fields, and
        seems in practice to give many imprimitive ones.

    INPUT:

    - ``F`` -- number field; the base field
    - ``m`` -- integer; the degree
    - ``B`` -- integer; the discriminant bound
    - ``a`` -- list (default: ``[]``); the coefficient list to begin with
    - ``verbose`` -- boolean or nonnegative integer or string (default: 0);
      give a verbose description of the computations being performed. If
      ``verbose`` is set to ``2`` or more then it outputs some extra
      information. If ``verbose`` is a string then it outputs to a file
      specified by ``verbose``.
    - ``return_seqs`` -- boolean (default: ``False``); if ``True``, then return
      the polynomials as sequences (for easier exporting to a file). This
      also returns a list of four numbers, as explained in the OUTPUT
      section below.
    - ``return_pari_objects`` -- boolean (default: ``True``); if both
      ``return_seqs`` and ``return_pari_objects`` are ``False`` then it returns
      the elements as Sage objects; otherwise it returns PARI objects.

    OUTPUT:

    - the list of fields with entries ``[d,fabs,f]``, where ``d`` is the
      discriminant, ``fabs`` is an absolute defining polynomial, and ``f``
      is a defining polynomial relative to `F`, sorted by discriminant.

    - if ``return_seqs`` is ``True``, then the first field of the list is
      a list containing the count of four items as explained below

      - the first entry gives the number of polynomials tested
      - the second entry gives the number of polynomials with its
        discriminant having a large enough square divisor
      - the third entry is the number of irreducible polynomials
      - the fourth entry is the number of irreducible polynomials with
        discriminant at most `B`

    EXAMPLES::

        sage: ZZx.<x> = ZZ[]
        sage: F.<t> = NumberField(x^2 - 2)
        sage: enumerate_totallyreal_fields_rel(F, 1, 2000)
        [[1, [-2, 0, 1], xF - 1]]
        sage: enumerate_totallyreal_fields_rel(F, 2, 2000)
        [[1600, x^4 - 6*x^2 + 4, xF^2 + xF - 1]]
        sage: enumerate_totallyreal_fields_rel(F, 2, 2000, return_seqs=True)
        [[9, 6, 5, 0], [[1600, [4, 0, -6, 0, 1], [-1, 1, 1]]]]

    TESTS:

    Each of the outputs must be elements of Sage if ``return_pari_objects``
    is set to ``False``::

        sage: type(enumerate_totallyreal_fields_rel(F, 2, 2000)[0][1])
        <class 'cypari2.gen.Gen'>
        sage: enumerate_totallyreal_fields_rel(F, 2, 2000, return_pari_objects=False)[0][0].parent()
        Integer Ring
        sage: enumerate_totallyreal_fields_rel(F, 2, 2000, return_pari_objects=False)[0][1].parent()
        Univariate Polynomial Ring in x over Rational Field
        sage: enumerate_totallyreal_fields_rel(F, 2, 2000, return_pari_objects=False)[0][2].parent()
        Univariate Polynomial Ring in xF over Number Field in t with defining polynomial x^2 - 2
        sage: enumerate_totallyreal_fields_rel(F, 2, 2000, return_seqs=True)[1][0][1][0].parent()
        Rational Field

    AUTHORS:

    - John Voight (2007-11-01)
    """
def enumerate_totallyreal_fields_all(n, B, verbose: int = 0, return_seqs: bool = False, return_pari_objects: bool = True):
    """
    Enumerate *all* totally real fields of degree ``n`` with discriminant
    at most ``B``, primitive or otherwise.

    INPUT:

    - ``n`` -- integer; the degree
    - ``B`` -- integer; the discriminant bound
    - ``verbose`` -- boolean or nonnegative integer or string (default: 0);
      give a verbose description of the computations being performed. If
      ``verbose`` is set to ``2`` or more, it outputs some extra information.
      If ``verbose`` is a string, it outputs to a file specified by ``verbose``.
    - ``return_seqs`` -- boolean (default: ``False``); if ``True``, then return
      the polynomials as sequences (for easier exporting to a file). This
      also returns a list of four numbers, as explained in the OUTPUT
      section below.
    - ``return_pari_objects`` -- boolean (default: ``True``); if both
      ``return_seqs`` and ``return_pari_objects`` are ``False`` then it
      returns the elements as Sage objects; otherwise it returns PARI objects.

    EXAMPLES::

        sage: enumerate_totallyreal_fields_all(4, 2000)
        [[725, x^4 - x^3 - 3*x^2 + x + 1],
        [1125, x^4 - x^3 - 4*x^2 + 4*x + 1],
        [1600, x^4 - 6*x^2 + 4],
        [1957, x^4 - 4*x^2 - x + 1],
        [2000, x^4 - 5*x^2 + 5]]
        sage: enumerate_totallyreal_fields_all(1, 10)
        [[1, x - 1]]

    TESTS:

    Each of the outputs must be elements of Sage if ``return_pari_objects``
    is set to ``False``::

        sage: enumerate_totallyreal_fields_all(2, 10)
        [[5, x^2 - x - 1], [8, x^2 - 2]]
        sage: type(enumerate_totallyreal_fields_all(2, 10)[0][1])
        <class 'cypari2.gen.Gen'>
        sage: enumerate_totallyreal_fields_all(2, 10, return_pari_objects=False)[0][1].parent()
        Univariate Polynomial Ring in x over Rational Field

    In practice most of these will be found by
    :func:`~sage.rings.number_field.totallyreal.enumerate_totallyreal_fields_prim`,
    which is guaranteed to return all primitive fields but often returns
    many non-primitive ones as well. For instance, only one of the five
    fields in the example above is primitive, but
    :func:`~sage.rings.number_field.totallyreal.enumerate_totallyreal_fields_prim`
    finds four out of the five (the exception being `x^4 - 6x^2 + 4`).

    The following was fixed in :issue:`13101`::

        sage: enumerate_totallyreal_fields_all(8, 10^6)  # long time (about 2 s)
        []
    """
