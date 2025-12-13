from sage.matrix.constructor import matrix as matrix

def dhsw_snf(mat, verbose: bool = False):
    '''
    Preprocess a matrix using the "Elimination algorithm" described by
    Dumas et al. [DHSW2003]_, and then call ``elementary_divisors`` on the
    resulting (smaller) matrix.

    .. NOTE::

        \'snf\' stands for \'Smith Normal Form\'.

    INPUT:

    - ``mat`` -- integer matrix, either sparse or dense

    (They use the transpose of the matrix considered here, so they use
    rows instead of columns.)

    ALGORITHM:

    Go through ``mat`` one column at a time.  For each
    column, add multiples of previous columns to it until either

    - it\'s zero, in which case it should be deleted.
    - its first nonzero entry is 1 or -1, in which case it should be kept.
    - its first nonzero entry is something else, in which case it is
      deferred until the second pass.

    Then do a second pass on the deferred columns.

    At this point, the columns with 1 or -1 in the first entry
    contribute to the rank of the matrix, and these can be counted and
    then deleted (after using the 1 or -1 entry to clear out its row).
    Suppose that there were `N` of these.

    The resulting matrix should be much smaller; we then feed it
    to Sage\'s ``elementary_divisors`` function, and prepend `N` 1s to
    account for the rows deleted in the previous step.

    EXAMPLES::

        sage: from sage.homology.matrix_utils import dhsw_snf
        sage: mat = matrix(ZZ, 3, 4, range(12))
        sage: dhsw_snf(mat)
        [1, 4, 0]
        sage: mat = random_matrix(ZZ, 20, 20, x=-1, y=2)
        sage: mat.elementary_divisors() == dhsw_snf(mat)
        True
    '''
