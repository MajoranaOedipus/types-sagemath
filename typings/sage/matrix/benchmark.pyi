from sage.matrix.constructor import Matrix as Matrix, random_matrix as random_matrix
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.timing import cputime as cputime
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

verbose: bool
timeout: int

def report(F, title, systems=['sage', 'magma'], **kwds) -> None:
    '''
    Run benchmarks with default arguments for each function in the list F.

    INPUT:

    - ``F`` -- list of callables used for benchmarking
    - ``title`` -- string describing this report
    - ``systems`` -- list of systems (supported entries are \'sage\' and \'magma\')
    - ``**kwds`` -- keyword arguments passed to all functions in ``F``

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: print("starting"); import sys; sys.stdout.flush(); b.report([b.det_ZZ], \'Test\', systems=[\'sage\'])
        starting...
        ======================================================================
                  Test
        ======================================================================
        ...
        ======================================================================
    '''
def report_ZZ(**kwds) -> None:
    '''
    Reports all the benchmarks for integer matrices and few
    rational matrices.

    INPUT:

    - ``**kwds`` -- passed through to :func:`report`

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: print("starting"); import sys; sys.stdout.flush(); b.report_ZZ(systems=[\'sage\'])  # long time (15s on sage.math, 2012)
        starting...
        ======================================================================
        Dense benchmarks over ZZ
        ======================================================================
        ...
        ======================================================================
    '''
def nullspace_ZZ(n: int = 200, min: int = 0, max=..., system: str = 'sage'):
    """
    Nullspace over ZZ:
    Given a n+1 x n matrix over ZZ with random entries
    between min and max, compute the nullspace.

    INPUT:

    - ``n`` -- matrix dimension (default: ``200``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``2**32``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.nullspace_ZZ(200)
        sage: tm = b.nullspace_ZZ(200, system='magma')  # optional - magma
    """
def charpoly_ZZ(n: int = 100, min: int = 0, max: int = 9, system: str = 'sage'):
    """
    Characteristic polynomial over ZZ:
    Given a n x n matrix over ZZ with random entries between min and
    max, compute the charpoly.

    INPUT:

    - ``n`` -- matrix dimension (default: ``100``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.charpoly_ZZ(100)
        sage: tm = b.charpoly_ZZ(100, system='magma')  # optional - magma
    """
def rank_ZZ(n: int = 700, min: int = 0, max: int = 9, system: str = 'sage'):
    """
    Rank over ZZ:
    Given a n x (n+10) matrix over ZZ with random entries
    between min and max, compute the rank.

    INPUT:

    - ``n`` -- matrix dimension (default: ``700``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.rank_ZZ(300)
        sage: tm = b.rank_ZZ(300, system='magma')  # optional - magma
    """
def rank2_ZZ(n: int = 400, min: int = 0, max=..., system: str = 'sage'):
    """
    Rank 2 over ZZ:
    Given a (n + 10) x n matrix over ZZ with random entries
    between min and max, compute the rank.

    INPUT:

    - ``n`` -- matrix dimension (default: ``400``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``2**64``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.rank2_ZZ(300)
        sage: tm = b.rank2_ZZ(300, system='magma')  # optional - magma
    """
def smithform_ZZ(n: int = 128, min: int = 0, max: int = 9, system: str = 'sage'):
    """
    Smith Form over ZZ:
    Given a n x n matrix over ZZ with random entries
    between min and max, compute the Smith normal form.

    INPUT:

    - ``n`` -- matrix dimension (default: ``128``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.smithform_ZZ(100)
        sage: tm = b.smithform_ZZ(100, system='magma')  # optional - magma
    """
def matrix_multiply_ZZ(n: int = 300, min: int = -9, max: int = 9, system: str = 'sage', times: int = 1):
    """
    Matrix multiplication over ZZ
    Given an n x n matrix A over ZZ with random entries
    between min and max, inclusive, compute A * (A+1).

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``min`` -- minimal value for entries of matrix (default: ``-9``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``1``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.matrix_multiply_ZZ(200)
        sage: tm = b.matrix_multiply_ZZ(200, system='magma')  # optional - magma
    """
def matrix_add_ZZ(n: int = 200, min: int = -9, max: int = 9, system: str = 'sage', times: int = 50):
    """
    Matrix addition over ZZ
    Given an n x n matrix A and B over ZZ with random entries between
    ``min`` and ``max``, inclusive, compute A + B ``times`` times.

    INPUT:

    - ``n`` -- matrix dimension (default: ``200``)
    - ``min`` -- minimal value for entries of matrix (default: ``-9``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``50``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.matrix_add_ZZ(200)
        sage: tm = b.matrix_add_ZZ(200, system='magma')  # optional - magma
    """
def matrix_add_ZZ_2(n: int = 200, bits: int = 16, system: str = 'sage', times: int = 50):
    """
    Matrix addition over ZZ.
    Given an n x n matrix A and B over ZZ with random ``bits``-bit
    entries, compute A + B.

    INPUT:

    - ``n`` -- matrix dimension (default: ``200``)
    - ``bits`` -- bitsize of entries
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``50``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.matrix_add_ZZ_2(200)
        sage: tm = b.matrix_add_ZZ_2(200, system='magma')  # optional - magma
    """
def det_ZZ(n: int = 200, min: int = 1, max: int = 100, system: str = 'sage'):
    """
    Dense integer determinant over ZZ.
    Given an n x n matrix A over ZZ with random entries
    between min and max, inclusive, compute det(A).

    INPUT:

    - ``n`` -- matrix dimension (default: ``200``)
    - ``min`` -- minimal value for entries of matrix (default: ``1``)
    - ``max`` -- maximal value for entries of matrix (default: ``100``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.det_ZZ(200)
        sage: tm = b.det_ZZ(200, system='magma')  # optional - magma
    """
def det_QQ(n: int = 300, num_bound: int = 10, den_bound: int = 10, system: str = 'sage'):
    """
    Dense rational determinant over QQ.
    Given an n x n matrix A over QQ with random entries
    with numerator bound and denominator bound, compute det(A).

    INPUT:

    - ``n`` -- matrix dimension (default: ``200``)
    - ``num_bound`` -- numerator bound, inclusive (default: ``10``)
    - ``den_bound`` -- denominator bound, inclusive (default: ``10``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.det_QQ(200)
        sage: ts = b.det_QQ(10, num_bound=100000, den_bound=10000)
        sage: tm = b.det_QQ(200, system='magma')  # optional - magma
    """
def vecmat_ZZ(n: int = 300, min: int = -9, max: int = 9, system: str = 'sage', times: int = 200):
    """
    Vector matrix multiplication over ZZ.

    Given an n x n  matrix A over ZZ with random entries
    between min and max, inclusive, and v the first row of A,
    compute the product v * A.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``min`` -- minimal value for entries of matrix (default: ``-9``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)
    - ``times`` -- number of runs (default: ``200``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.vecmat_ZZ(300)  # long time
        sage: tm = b.vecmat_ZZ(300, system='magma')  # optional - magma
    """
def report_GF(p: int = 16411, **kwds) -> None:
    '''
    Run all the reports for finite field matrix operations, for
    prime p=16411.

    INPUT:

    - ``p`` -- ignored
    - ``**kwds`` -- passed through to :func:`report`

    .. NOTE::

        right now, even though p is an input, it is being ignored!  If
        you need to check the performance for other primes, you can
        call individual benchmark functions.

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: print("starting"); import sys; sys.stdout.flush(); b.report_GF(systems=[\'sage\'])
        starting...
        ======================================================================
        Dense benchmarks over GF with prime 16411
        ======================================================================
        ...
        ======================================================================
    '''
def nullspace_GF(n: int = 300, p: int = 16411, system: str = 'sage'):
    """
    Given a n+1 x n  matrix over GF(p) with random
    entries, compute the nullspace.

    INPUT:

    - ``n`` -- matrix dimension (default: 300)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.nullspace_GF(300)
        sage: tm = b.nullspace_GF(300, system='magma')  # optional - magma
    """
def charpoly_GF(n: int = 100, p: int = 16411, system: str = 'sage'):
    """
    Given a n x n matrix over GF with random entries, compute the
    charpoly.

    INPUT:

    - ``n`` -- matrix dimension (default: 100)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.charpoly_GF(100)
        sage: tm = b.charpoly_GF(100, system='magma')  # optional - magma
    """
def matrix_add_GF(n: int = 1000, p: int = 16411, system: str = 'sage', times: int = 100):
    """
    Given two n x n matrix over GF(p) with random entries, add them.

    INPUT:

    - ``n`` -- matrix dimension (default: 300)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``100``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.matrix_add_GF(500, p=19)
        sage: tm = b.matrix_add_GF(500, p=19, system='magma')  # optional - magma
    """
def matrix_multiply_GF(n: int = 100, p: int = 16411, system: str = 'sage', times: int = 3):
    """
    Given an n x n matrix A over GF(p) with random entries, compute
    A * (A+1).

    INPUT:

    - ``n`` -- matrix dimension (default: 100)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``3``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.matrix_multiply_GF(100, p=19)
        sage: tm = b.matrix_multiply_GF(100, p=19, system='magma')  # optional - magma
    """
def rank_GF(n: int = 500, p: int = 16411, system: str = 'sage'):
    """
    Rank over GF(p):
    Given a n x (n+10) matrix over GF(p) with random entries, compute the rank.

    INPUT:

    - ``n`` -- matrix dimension (default: 300)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.rank_GF(1000)
        sage: tm = b.rank_GF(1000, system='magma')  # optional - magma
    """
def rank2_GF(n: int = 500, p: int = 16411, system: str = 'sage'):
    """
    Rank over GF(p): Given a (n + 10) x n matrix over GF(p) with
    random entries, compute the rank.

    INPUT:

    - ``n`` -- matrix dimension (default: 300)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.rank2_GF(500)
        sage: tm = b.rank2_GF(500, system='magma')  # optional - magma
    """
def det_GF(n: int = 400, p: int = 16411, system: str = 'sage'):
    """
    Dense determinant over GF(p).
    Given an n x n matrix A over GF with random entries compute
    det(A).

    INPUT:

    - ``n`` -- matrix dimension (default: 300)
    - ``p`` -- prime number (default: ``16411``)
    - ``system`` -- either 'magma' or 'sage' (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.det_GF(1000)
        sage: tm = b.det_GF(1000, system='magma')  # optional - magma
    """
def hilbert_matrix(n):
    """
    Return the Hilbert matrix of size n over rationals.

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: b.hilbert_matrix(3)
        [  1 1/2 1/3]
        [1/2 1/3 1/4]
        [1/3 1/4 1/5]
    """
def echelon_QQ(n: int = 100, min: int = 0, max: int = 9, system: str = 'sage'):
    """
    Given a n x (2*n) matrix over QQ with random integer entries
    between min and max, compute the reduced row echelon form.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``min`` -- minimal value for entries of matrix (default: ``-9``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.echelon_QQ(100)
        sage: tm = b.echelon_QQ(100, system='magma')  # optional - magma
    """
def inverse_QQ(n: int = 100, min: int = 0, max: int = 9, system: str = 'sage'):
    """
    Given a n x n matrix over QQ with random integer entries
    between min and max, compute the reduced row echelon form.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``min`` -- minimal value for entries of matrix (default: ``-9``)
    - ``max`` -- maximal value for entries of matrix (default: ``9``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.inverse_QQ(100)
        sage: tm = b.inverse_QQ(100, system='magma')  # optional - magma
    """
def matrix_multiply_QQ(n: int = 100, bnd: int = 2, system: str = 'sage', times: int = 1):
    """
    Given an n x n matrix A over QQ with random entries
    whose numerators and denominators are bounded by bnd,
    compute A * (A+1).

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``bnd`` -- numerator and denominator bound (default: ``bnd``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``1``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.matrix_multiply_QQ(100)
        sage: tm = b.matrix_multiply_QQ(100, system='magma')  # optional - magma
    """
def det_hilbert_QQ(n: int = 80, system: str = 'sage'):
    """
    Run the benchmark for calculating the determinant of the hilbert
    matrix over rationals of dimension n.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.det_hilbert_QQ(50)
        sage: tm = b.det_hilbert_QQ(50, system='magma')  # optional - magma
    """
def invert_hilbert_QQ(n: int = 40, system: str = 'sage'):
    """
    Run the benchmark for calculating the inverse of the hilbert
    matrix over rationals of dimension n.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.invert_hilbert_QQ(30)
        sage: tm = b.invert_hilbert_QQ(30, system='magma')  # optional - magma
    """
def MatrixVector_QQ(n: int = 1000, h: int = 100, system: str = 'sage', times: int = 1):
    """
    Compute product of square ``n`` matrix by random vector with num and
    denom bounded by ``h`` the given number of ``times``.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``h`` -- numerator and denominator bound (default: ``bnd``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)
    - ``times`` -- number of experiments (default: ``1``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.MatrixVector_QQ(500)
        sage: tm = b.MatrixVector_QQ(500, system='magma')  # optional - magma
    """
def nullspace_RR(n: int = 300, min: int = 0, max: int = 10, system: str = 'sage'):
    """
    Nullspace over RR:
    Given a n+1 x n matrix over RR with random entries
    between min and max, compute the nullspace.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``10``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.nullspace_RR(100)
        sage: tm = b.nullspace_RR(100, system='magma')  # optional - magma
    """
def nullspace_RDF(n: int = 300, min: int = 0, max: int = 10, system: str = 'sage'):
    """
    Nullspace over RDF:
    Given a n+1 x n  matrix over RDF with random entries
    between min and max, compute the nullspace.

    INPUT:

    - ``n`` -- matrix dimension (default: ``300``)
    - ``min`` -- minimal value for entries of matrix (default: ``0``)
    - ``max`` -- maximal value for entries of matrix (default: ``10``)
    - ``system`` -- either ``'sage'`` or ``'magma'`` (default: ``'sage'``)

    EXAMPLES::

        sage: import sage.matrix.benchmark as b
        sage: ts = b.nullspace_RDF(100)  # long time
        sage: tm = b.nullspace_RDF(100, system='magma')  # optional - magma
    """
