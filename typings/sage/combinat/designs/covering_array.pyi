from .orthogonal_arrays import OA_relabel as OA_relabel, OA_standard_label as OA_standard_label

CA_relabel = OA_relabel
CA_standard_label = OA_standard_label

def truncate_columns(array, k):
    """
    Return a covering array with `k` columns, obtained by removing excess
    columns from a larger covering array.

    INPUT:

    - ``array`` -- the array to be truncated.

    - ``k`` -- the number of columns desired. Must be less than the
      number of columns in ``array``.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.covering_array import truncate_columns
        sage: from sage.combinat.designs.database import ca_11_2_5_3
        sage: C = ca_11_2_5_3()
        sage: D = truncate_columns(C,7)
        Traceback (most recent call last):
        ...
        ValueError: array only has 5 columns
        sage: E = truncate_columns(C,4)
        sage: is_covering_array(E,parameters=True)
        (True, (11, 2, 4, 3))

    """
def Kleitman_Spencer_Katona(N):
    """
    Return a `CA(N; 2, k, 2)` where `k = \\binom {N-1}{\\lceil N/2 \\rceil}`.

    INPUT:

    - ``N`` -- the number of rows in the array, must be an integer greater
      than 3 since any smaller would not produce enough columns for a
      strength 2 array.

    This construction is referenced in [Colb2004]_ from [KS1973]_ and [Kat1973]_

    **Construction**

    Take all distinct binary `N`-tuples of weight `N/2` that have a 0
    in the first position and place them as columns in an array.

    EXAMPLES::

        sage: from sage.combinat.designs.covering_array import Kleitman_Spencer_Katona
        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: C = Kleitman_Spencer_Katona(2)
        Traceback (most recent call last):
        ...
        ValueError: N must be greater than 3
        sage: C = Kleitman_Spencer_Katona(5)
        sage: is_covering_array(C,parameters=True)
        (True, (5, 2, 4, 2))

    """
def column_Kleitman_Spencer_Katona(k):
    """
    Return a covering array with `k` columns using the Kleitman-Spencer-Katona
    method.

    See :func:`~sage.combinat.designs.covering_array.Kleitman_Spencer_Katona`

    INPUT:

    - ``k`` -- the number of columns in the array, must be an integer
      greater than 3 since any smaller is a trivial array for strength 2.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.covering_array import column_Kleitman_Spencer_Katona
        sage: C = column_Kleitman_Spencer_Katona(20)
        sage: is_covering_array(C,parameters=True)
        (True, (8, 2, 20, 2))
        sage: column_Kleitman_Spencer_Katona(25000)
        Traceback (most recent call last):
        ...
        NotImplementedError: not implemented for k > 24310

    """
def database_check(number_columns, strength, levels):
    """
    Check if the database can be used to build a CA with the given parameters.
    If so return the CA, if not return False.

    INPUT:

    - ``strength`` (integer) -- the parameter `t` of the covering array,
      such that in any selection of `t` columns of the array, every
      `t`-tuple appears at least once.

    - ``levels`` (integer) -- the parameter `v` which is the number of
      unique symbols that appear in the covering array.

    - ``number_columns`` (integer) -- the number of columns desired for
      the covering array.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.covering_array import database_check
        sage: C = database_check(6, 2, 3)
        sage: is_covering_array(C, parameters=True)
        (True, (12, 2, 6, 3))
        sage: database_check(6, 3, 3)
        False

    """
def covering_array(strength, number_columns, levels):
    """
    Build a `CA(N; t, k, v)` using direct constructions, where `N` is the
    smallest size known.

    INPUT:

    - ``strength`` (integer) -- the parameter `t` of the covering array,
      such that in any selection of `t` columns of the array, every
      `t`-tuple appears at least once.

    - ``levels`` (integer) -- the parameter `v` which is the number of
      unique symbols that appear in the covering array.

    - ``number_columns`` (integer) -- the number of columns desired for
      the covering array.

    EXAMPLES::

        sage: from sage.combinat.designs.designs_pyx import is_covering_array
        sage: from sage.combinat.designs.covering_array import covering_array
        sage: C1 = covering_array(2, 7, 3)
        sage: is_covering_array(C1,parameters=True)
        (True, (12, 2, 7, 3))
        sage: C2 = covering_array(2, 11, 2)
        sage: is_covering_array(C2,parameters=True)
        (True, (7, 2, 11, 2))
        sage: C3 = covering_array(2, 8, 7)
        sage: is_covering_array(C3,parameters=True)
        (True, (49, 2, 8, 7))
        sage: C4 = covering_array(2, 50, 7)
        No direct construction known and/or implemented for a CA(N; 2, 50, 7)

    """
