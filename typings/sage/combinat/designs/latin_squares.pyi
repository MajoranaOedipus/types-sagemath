from sage.arith.misc import is_prime_power as is_prime_power
from sage.categories.sets_cat import EmptySetError as EmptySetError
from sage.misc.unknown import Unknown as Unknown
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer

def are_mutually_orthogonal_latin_squares(l, verbose: bool = False):
    """
    Check whether the list of matrices in ``l`` form mutually orthogonal latin
    squares.

    INPUT:

    - ``verbose`` -- if ``True`` then print why the list of matrices provided are
      not mutually orthogonal latin squares

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import are_mutually_orthogonal_latin_squares
        sage: m1 = matrix([[0,1,2],[2,0,1],[1,2,0]])
        sage: m2 = matrix([[0,1,2],[1,2,0],[2,0,1]])
        sage: m3 = matrix([[0,1,2],[2,0,1],[1,2,0]])
        sage: are_mutually_orthogonal_latin_squares([m1,m2])
        True
        sage: are_mutually_orthogonal_latin_squares([m1,m3])
        False
        sage: are_mutually_orthogonal_latin_squares([m2,m3])
        True
        sage: are_mutually_orthogonal_latin_squares([m1,m2,m3], verbose=True)
        Squares 0 and 2 are not orthogonal
        False

        sage: m = designs.mutually_orthogonal_latin_squares(7,8)                        # needs sage.schemes
        sage: are_mutually_orthogonal_latin_squares(m)                                  # needs sage.schemes
        True

    TESTS:

    Not a latin square::

        sage: m1 = matrix([[0,1,0],[2,0,1],[1,2,0]])
        sage: m2 = matrix([[0,1,2],[1,2,0],[2,0,1]])
        sage: are_mutually_orthogonal_latin_squares([m1,m2], verbose=True)
        Matrix 0 is not row latin
        False
        sage: m1 = matrix([[0,1,2],[1,0,2],[1,2,0]])
        sage: are_mutually_orthogonal_latin_squares([m1,m2], verbose=True)
        Matrix 0 is not column latin
        False
        sage: m1 = matrix([[0,0,0],[1,1,1],[2,2,2]])
        sage: m2 = matrix([[0,1,2],[0,1,2],[0,1,2]])
        sage: are_mutually_orthogonal_latin_squares([m1,m2])
        False
    """
def mutually_orthogonal_latin_squares(k, n, partitions: bool = False, check: bool = True):
    """
    Return `k` Mutually Orthogonal `n\\times n` Latin Squares (MOLS).

    For more information on Mutually Orthogonal Latin Squares, see
    :mod:`~sage.combinat.designs.latin_squares`.

    INPUT:

    - ``k`` -- integer; number of MOLS. If ``k`` is ``None`` it is set to the largest
      value available

    - ``n`` -- integer; size of the latin square

    - ``partitions`` -- boolean; a Latin Square can be seen as 3 partitions of
      the `n^2` cells of the array into `n` sets of size `n`, respectively:

      * The partition of rows
      * The partition of columns
      * The partition of number (cells numbered with 0, cells numbered with 1,
        ...)

      These partitions have the additional property that any two sets from
      different partitions intersect on exactly one element.

      When ``partitions`` is set to ``True``, this function returns a list of `k+2`
      partitions satisfying this intersection property instead of the `k+2` MOLS
      (though the data is exactly the same in both cases).

    - ``check`` -- boolean (default: ``True``); whether to check that output is
      correct before returning it. As this is expected to be useless, you may
      want to disable it whenever you want speed.

    EXAMPLES::

        sage: designs.mutually_orthogonal_latin_squares(4,5)                            # needs sage.schemes
        [
        [0 1 2 3 4]  [0 1 2 3 4]  [0 1 2 3 4]  [0 1 2 3 4]
        [1 2 3 4 0]  [2 3 4 0 1]  [3 4 0 1 2]  [4 0 1 2 3]
        [2 3 4 0 1]  [4 0 1 2 3]  [1 2 3 4 0]  [3 4 0 1 2]
        [3 4 0 1 2]  [1 2 3 4 0]  [4 0 1 2 3]  [2 3 4 0 1]
        [4 0 1 2 3], [3 4 0 1 2], [2 3 4 0 1], [1 2 3 4 0]
        ]

        sage: designs.mutually_orthogonal_latin_squares(3,7)                            # needs sage.schemes
        [
        [0 1 2 3 4 5 6]  [0 1 2 3 4 5 6]  [0 1 2 3 4 5 6]
        [1 2 3 4 5 6 0]  [2 3 4 5 6 0 1]  [3 4 5 6 0 1 2]
        [2 3 4 5 6 0 1]  [4 5 6 0 1 2 3]  [6 0 1 2 3 4 5]
        [3 4 5 6 0 1 2]  [6 0 1 2 3 4 5]  [2 3 4 5 6 0 1]
        [4 5 6 0 1 2 3]  [1 2 3 4 5 6 0]  [5 6 0 1 2 3 4]
        [5 6 0 1 2 3 4]  [3 4 5 6 0 1 2]  [1 2 3 4 5 6 0]
        [6 0 1 2 3 4 5], [5 6 0 1 2 3 4], [4 5 6 0 1 2 3]
        ]

        sage: designs.mutually_orthogonal_latin_squares(2,5,partitions=True)            # needs sage.schemes
        [[[0, 1, 2, 3, 4],
          [5, 6, 7, 8, 9],
          [10, 11, 12, 13, 14],
          [15, 16, 17, 18, 19],
          [20, 21, 22, 23, 24]],
         [[0, 5, 10, 15, 20],
          [1, 6, 11, 16, 21],
          [2, 7, 12, 17, 22],
          [3, 8, 13, 18, 23],
          [4, 9, 14, 19, 24]],
         [[0, 9, 13, 17, 21],
          [1, 5, 14, 18, 22],
          [2, 6, 10, 19, 23],
          [3, 7, 11, 15, 24],
          [4, 8, 12, 16, 20]],
         [[0, 8, 11, 19, 22],
          [1, 9, 12, 15, 23],
          [2, 5, 13, 16, 24],
          [3, 6, 14, 17, 20],
          [4, 7, 10, 18, 21]]]

    What is the maximum number of MOLS of size 8 that Sage knows how to build?::

        sage: designs.orthogonal_arrays.largest_available_k(8)-2                        # needs sage.schemes
        7

    If you only want to know if Sage is able to build a given set of
    MOLS, query the ``orthogonal_arrays.*`` functions::

        sage: designs.orthogonal_arrays.is_available(5+2, 5) # 5 MOLS of order 5
        False
        sage: designs.orthogonal_arrays.is_available(4+2,6)  # 4 MOLS of order 6        # needs sage.schemes
        False

    Sage, however, is not able to prove that the second MOLS do not exist::

        sage: designs.orthogonal_arrays.exists(4+2,6)  # 4 MOLS of order 6              # needs sage.schemes
        Unknown

    If you ask for such a MOLS then you will respectively get an informative
    :exc:`EmptySetError` or :exc:`NotImplementedError`::

        sage: designs.mutually_orthogonal_latin_squares(5, 5)
        Traceback (most recent call last):
        ...
        EmptySetError: there exist at most n-1 MOLS of size n if n>=2
        sage: designs.mutually_orthogonal_latin_squares(4,6)                            # needs sage.schemes
        Traceback (most recent call last):
        ...
        NotImplementedError: I don't know how to build 4 MOLS of order 6

    TESTS:

    The special case `n=1`::

        sage: designs.mutually_orthogonal_latin_squares(3, 1)
        [[0], [0], [0]]

    Wrong input for `k`::

        sage: designs.mutually_orthogonal_latin_squares(None, 1)
        Traceback (most recent call last):
        ...
        TypeError: k must be a positive integer

        sage: designs.mutually_orthogonal_latin_squares(-1, 1)
        Traceback (most recent call last):
        ...
        ValueError: k must be positive

        sage: designs.mutually_orthogonal_latin_squares(2,10)
        [
        [1 8 9 0 2 4 6 3 5 7]  [1 7 6 5 0 9 8 2 3 4]
        [7 2 8 9 0 3 5 4 6 1]  [8 2 1 7 6 0 9 3 4 5]
        [6 1 3 8 9 0 4 5 7 2]  [9 8 3 2 1 7 0 4 5 6]
        [5 7 2 4 8 9 0 6 1 3]  [0 9 8 4 3 2 1 5 6 7]
        [0 6 1 3 5 8 9 7 2 4]  [2 0 9 8 5 4 3 6 7 1]
        [9 0 7 2 4 6 8 1 3 5]  [4 3 0 9 8 6 5 7 1 2]
        [8 9 0 1 3 5 7 2 4 6]  [6 5 4 0 9 8 7 1 2 3]
        [2 3 4 5 6 7 1 8 9 0]  [3 4 5 6 7 1 2 8 0 9]
        [3 4 5 6 7 1 2 0 8 9]  [5 6 7 1 2 3 4 0 9 8]
        [4 5 6 7 1 2 3 9 0 8], [7 1 2 3 4 5 6 9 8 0]
        ]

    Verify the construction from [KD2015]_::

        sage: designs.mutually_orthogonal_latin_squares(2, 9)
        [
        [0 1 2 3 4 5 6 7 8]  [0 1 2 3 4 5 6 7 8]
        [2 3 6 4 1 8 0 5 7]  [3 8 4 7 5 2 1 0 6]
        [3 8 4 7 5 2 1 0 6]  [4 7 1 5 8 6 3 2 0]
        [4 7 1 5 8 6 3 2 0]  [5 0 8 2 6 1 7 4 3]
        [5 0 8 2 6 1 7 4 3]  [6 4 0 1 3 7 2 8 5]
        [6 4 0 1 3 7 2 8 5]  [7 6 5 0 2 4 8 3 1]
        [7 6 5 0 2 4 8 3 1]  [8 2 7 6 0 3 5 1 4]
        [8 2 7 6 0 3 5 1 4]  [1 5 3 8 7 0 4 6 2]
        [1 5 3 8 7 0 4 6 2], [2 3 6 4 1 8 0 5 7]
        ]
    """
def latin_square_product(M, N, *others):
    """
    Return the product of two (or more) latin squares.

    Given two Latin Squares `M,N` of respective sizes `m,n`, the direct product
    `M\\times N` of size `mn` is defined by `(M\\times
    N)((i_1,i_2),(j_1,j_2))=(M(i_1,j_1),N(i_2,j_2))` where `i_1,j_1\\in [m],
    i_2,j_2\\in [n]`

    Each pair of values `(i,j)\\in [m]\\times [n]` is then relabeled to `in+j`.

    This is Lemma 6.25 of [Stinson2004]_.

    INPUT:

    - ``M``, ``N``, ``*others`` -- an arbitrary number of latin squares
      (greater than or equal to 2)

    EXAMPLES::

        sage: from sage.combinat.designs.latin_squares import latin_square_product
        sage: m=designs.mutually_orthogonal_latin_squares(3,4)[0]                       # needs sage.schemes
        sage: latin_square_product(m,m,m)                                               # needs sage.schemes
        64 x 64 sparse matrix over Integer Ring (use the '.str()' method to see the entries)
    """
def MOLS_table(start, stop=None, compare: bool = False, width=None) -> None:
    """
    Print the MOLS table that Sage can produce.

    INPUT:

    - ``start``, ``stop`` -- integers; print the table of MOLS for value of
      `n` such that ``start<=n<stop``. If only one integer is given as input,
      it is interpreted as the value of ``stop`` with ``start=0`` (same
      behaviour as ``range``).

    - ``compare`` -- boolean; if sets to ``True`` the MOLS displays
      with `+` and `-` entries its difference with the table from the
      Handbook of Combinatorial Designs (2ed).

    - ``width`` -- integer; the width of each column of the table. By default,
      it is computed from range of values determined by the parameters ``start``
      and ``stop``.

    EXAMPLES::

        sage: # needs sage.schemes
        sage: from sage.combinat.designs.latin_squares import MOLS_table
        sage: MOLS_table(100)
               0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
            ________________________________________________________________________________
          0| +oo +oo   1   2   3   4   1   6   7   8   2  10   5  12   4   4  15  16   5  18
         20|   4   5   3  22   7  24   4  26   5  28   4  30  31   5   4   5   8  36   4   5
         40|   7  40   5  42   5   6   4  46   8  48   6   5   5  52   5   6   7   7   5  58
         60|   5  60   5   6  63   7   5  66   5   6   6  70   7  72   5   7   6   6   6  78
         80|   9  80   8  82   6   6   6   6   7  88   6   7   6   6   6   6   7  96   6   8
        sage: MOLS_table(100, width=4)
                 0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19
             ____________________________________________________________________________________________________
           0|  +oo  +oo    1    2    3    4    1    6    7    8    2   10    5   12    4    4   15   16    5   18
          20|    4    5    3   22    7   24    4   26    5   28    4   30   31    5    4    5    8   36    4    5
          40|    7   40    5   42    5    6    4   46    8   48    6    5    5   52    5    6    7    7    5   58
          60|    5   60    5    6   63    7    5   66    5    6    6   70    7   72    5    7    6    6    6   78
          80|    9   80    8   82    6    6    6    6    7   88    6    7    6    6    6    6    7   96    6    8
        sage: MOLS_table(100, compare=True)
               0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
            ________________________________________________________________________________
          0|                                                           +               +
         20|
         40|
         60|
         80|
        sage: MOLS_table(50, 100, compare=True)
               0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
            ________________________________________________________________________________
         40|
         60|
         80|
    """
