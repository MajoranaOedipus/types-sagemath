r"""
Enumeration of primitive totally real fields

This module contains functions for enumerating all primitive
totally real number fields of given degree and small discriminant.
Here a number field is called *primitive* if it contains no proper
subfields except `\QQ`.

See also :mod:`sage.rings.number_field.totallyreal_rel`, which handles the non-primitive
case using relative extensions.

ALGORITHM:

We use Hunter's algorithm ([Coh2000]_, Section 9.3) with modifications
due to Takeuchi [Tak1999]_ and the author [Voi2008]_.

We enumerate polynomials `f(x) = x^n + a_{n-1} x^{n-1} + \dots + a_0`.
Hunter's theorem gives bounds on `a_{n-1}` and `a_{n-2}`; then given
`a_{n-1}` and `a_{n-2}`, one can recursively compute bounds on `a_{n-3},
\dots, a_0`, using the fact that the polynomial is totally real by
looking at the zeros of successive derivatives and applying
Rolle's theorem. See [Tak1999]_ for more details.

EXAMPLES:

In this first simple example, we compute the totally real quadratic
fields of discriminant `\le 50`. ::

    sage: enumerate_totallyreal_fields_prim(2,50)
    [[5, x^2 - x - 1],
     [8, x^2 - 2],
     [12, x^2 - 3],
     [13, x^2 - x - 3],
     [17, x^2 - x - 4],
     [21, x^2 - x - 5],
     [24, x^2 - 6],
     [28, x^2 - 7],
     [29, x^2 - x - 7],
     [33, x^2 - x - 8],
     [37, x^2 - x - 9],
     [40, x^2 - 10],
     [41, x^2 - x - 10],
     [44, x^2 - 11]]
    sage: [d for d in range(5,50)
    ....:    if (is_squarefree(d) and d%4 == 1) or (d%4 == 0 and is_squarefree(d/4))]
    [5, 8, 12, 13, 17, 20, 21, 24, 28, 29, 33, 37, 40, 41, 44]

Next, we compute all totally real quintic fields of discriminant `\le 10^5`::

    sage: ls = enumerate_totallyreal_fields_prim(5,10^5) ; ls
    [[14641, x^5 - x^4 - 4*x^3 + 3*x^2 + 3*x - 1],
     [24217, x^5 - 5*x^3 - x^2 + 3*x + 1],
     [36497, x^5 - 2*x^4 - 3*x^3 + 5*x^2 + x - 1],
     [38569, x^5 - 5*x^3 + 4*x - 1],
     [65657, x^5 - x^4 - 5*x^3 + 2*x^2 + 5*x + 1],
     [70601, x^5 - x^4 - 5*x^3 + 2*x^2 + 3*x - 1],
     [81509, x^5 - x^4 - 5*x^3 + 3*x^2 + 5*x - 2],
     [81589, x^5 - 6*x^3 + 8*x - 1],
     [89417, x^5 - 6*x^3 - x^2 + 8*x + 3]]
     sage: len(ls)
     9

We see that there are 9 such fields (up to isomorphism!).

See also [Mar1980]_.

AUTHORS:

- John Voight (2007-09-01): initial version; various optimization tweaks
- John Voight (2007-10-09): added DSage module; added pari functions to avoid
  recomputations; separated DSage component
- Craig Citro and John Voight (2007-11-04): additional doctests and type checking
- Craig Citro and John Voight (2008-02-10): final modifications for submission
"""
import _cython_3_2_1
import cypari2.pari_instance
from sage.categories.category import ZZ as ZZ
from sage.rings.number_field.totallyreal_data import int_has_small_square_divisor as int_has_small_square_divisor
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typings_sagemath import Int

def enumerate_totallyreal_fields_prim(n: Int, B: Int, a = [], verbose=0, return_seqs=False,
                                      phc=False, keep_fields=False, t_2=False,
                                      just_print=False,
                                      return_pari_objects=True):
    r"""
    Enumerate primitive totally real fields of degree
    `n>1` with discriminant `d \leq B`; optionally one can specify the
    first few coefficients, where the sequence `a` corresponds to

    ::

        a[d]*x^n + ... + a[0]*x^(n-d)

    where ``length(a) = d+1``, so in particular always ``a[d] = 1``.

    .. NOTE::

        This is guaranteed to give all primitive such fields, and
        seems in practice to give many imprimitive ones.

    INPUT:

    - ``n`` -- integer; the degree
    - ``B`` -- integer; the discriminant bound
    - ``a`` -- list (default: ``[]``); the coefficient list to begin with
    - ``verbose`` -- (integer or string, default: 0) if ``verbose == 1``
      (or ``2``), then print to the screen (really) verbosely; if verbose is
      a string, then print verbosely to the file specified by verbose.
    - ``return_seqs`` -- boolean (default: ``False``); if ``True``, then return
      the polynomials as sequences (for easier exporting to a file)
    - ``phc`` -- boolean or integer (default: ``False``)
    - ``keep_fields`` -- boolean or integer (default: ``False``); if
      ``keep_fields`` is ``True``, then keep fields up to ``B*log(B)``; if
      ``keep_fields`` is an integer, then keep fields up to that integer.
    - ``t_2`` -- boolean or integer (default: ``False``); if ``t_2 = T``, then
      keep only polynomials with ``t_2 norm >= T``
    - ``just_print`` -- boolean (default: ``False``); if ``just_print`` is not
      ``False``, instead of creating a sorted list of totally real number
      fields, we simply write each totally real field we find to the file
      whose filename is given by ``just_print``. In this case, we don't
      return anything.
    - ``return_pari_objects`` -- boolean (default: ``True``); if
      both ``return_seqs`` and ``return_pari_objects`` are ``False`` then
      it returns the elements as Sage objects. Otherwise it returns PARI
      objects.

    OUTPUT:

    the list of fields with entries ``[d,f]``, where ``d`` is the
    discriminant and ``f`` is a defining polynomial, sorted by
    discriminant.


    AUTHORS:

    - John Voight (2007-09-03)
    - Craig Citro (2008-09-19): moved to Cython for speed improvement

    TESTS::

        sage: len(enumerate_totallyreal_fields_prim(2,10**4))
        3043
        sage: len(enumerate_totallyreal_fields_prim(3,3**8))
        237
        sage: len(enumerate_totallyreal_fields_prim(5,5**7))
        6
        sage: len(enumerate_totallyreal_fields_prim(2,2**15)) # long time
        9957
        sage: len(enumerate_totallyreal_fields_prim(3,3**10)) # long time
        2720
        sage: len(enumerate_totallyreal_fields_prim(5,5**8)) # long time
        103

    Each of the outputs must be elements of Sage if ``return_pari_objects``
    is set to ``False``::

        sage: enumerate_totallyreal_fields_prim(2, 10)
        [[5, x^2 - x - 1], [8, x^2 - 2]]
        sage: type(enumerate_totallyreal_fields_prim(2, 10)[0][1])
        <class 'cypari2.gen.Gen'>
        sage: enumerate_totallyreal_fields_prim(2, 10, return_pari_objects=False)[0][0].parent()
        Integer Ring
        sage: enumerate_totallyreal_fields_prim(2, 10, return_pari_objects=False)[0][1].parent()
        Univariate Polynomial Ring in x over Rational Field
        sage: enumerate_totallyreal_fields_prim(2, 10, return_seqs=True)[1][0][1][0].parent()
        Rational Field
    """
odlyzko_bound_totallyreal: _cython_3_2_1.cython_function_or_method
pari: cypari2.pari_instance.Pari
weed_fields: _cython_3_2_1.cython_function_or_method
