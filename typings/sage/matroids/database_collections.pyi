from _typeshed import Incomplete
from collections.abc import Generator

def AllMatroids(n, r=None, type: str = 'all') -> Generator[Incomplete]:
    """
    Iterate over all matroids of certain number of elements (and, optionally,
    of specific rank and type).

    INPUT:

    - ``n`` -- integer; the number of elements of the matroids
    - ``r`` -- integer (optional); the rank of the matroids (`0 \\le r \\le n`)
    - ``type`` -- string (default: ``'all'``); the type of the matroids. Must
      be one of the following:

      * ``'all'`` -- all matroids; available: (n=0-9), (n=0-12, r=0-2),
        (n=0-11, r=3)
      * ``'unorientable'`` -- all unorientable matroids; the rank `r` must be
        specified; available: (n=7-11, r=3), (n=7-9, r=4)
      * any other type for which there exists an ``is_type`` method;
        availability same as for ``'all'``

    EXAMPLES::

        sage: for M in matroids.AllMatroids(2):                                         # optional - matroid_database
        ....:     M
        all_n02_r00_#0: Matroid of rank 0 on 2 elements with 1 bases
        all_n02_r01_#0: Matroid of rank 1 on 2 elements with 2 bases
        all_n02_r01_#1: Matroid of rank 1 on 2 elements with 1 bases
        all_n02_r02_#0: Matroid of rank 2 on 2 elements with 1 bases

    ::

        sage: for M in matroids.AllMatroids(5, 3, 'simple'):                            # optional - matroid_database
        ....:     M
        simple_n05_r03_#0: Matroid of rank 3 on 5 elements with 10 bases
        simple_n05_r03_#1: Matroid of rank 3 on 5 elements with 9 bases
        simple_n05_r03_#2: Matroid of rank 3 on 5 elements with 8 bases
        simple_n05_r03_#3: Matroid of rank 3 on 5 elements with 6 bases

    ::

        sage: # optional - matroid_database
        sage: for M in matroids.AllMatroids(4, type='paving'):
        ....:     M
        paving_n04_r00_#0: Matroid of rank 0 on 4 elements with 1 bases
        paving_n04_r01_#0: Matroid of rank 1 on 4 elements with 4 bases
        paving_n04_r01_#1: Matroid of rank 1 on 4 elements with 3 bases
        paving_n04_r01_#2: Matroid of rank 1 on 4 elements with 2 bases
        paving_n04_r01_#3: Matroid of rank 1 on 4 elements with 1 bases
        paving_n04_r02_#0: Matroid of rank 2 on 4 elements with 6 bases
        paving_n04_r02_#1: Matroid of rank 2 on 4 elements with 5 bases
        paving_n04_r02_#2: Matroid of rank 2 on 4 elements with 4 bases
        paving_n04_r02_#3: Matroid of rank 2 on 4 elements with 3 bases
        paving_n04_r03_#0: Matroid of rank 3 on 4 elements with 4 bases
        paving_n04_r03_#1: Matroid of rank 3 on 4 elements with 3 bases
        paving_n04_r04_#0: Matroid of rank 4 on 4 elements with 1 bases

    ::

        sage: # optional - matroid_database
        sage: for M in matroids.AllMatroids(10, 4):
        ....:     M
        Traceback (most recent call last):
        ...
        ValueError: (n=10, r=4, type='all') is not available in the database
        sage: for M in matroids.AllMatroids(12, 3, 'unorientable'):
        ....:     M
        Traceback (most recent call last):
        ...
        ValueError: (n=12, r=3, type='unorientable') is not available in the database
        sage: for M in matroids.AllMatroids(8, type='unorientable'):
        ....:     M
        Traceback (most recent call last):
        ...
        ValueError: The rank needs to be specified for type 'unorientable'
        sage: for M in matroids.AllMatroids(6, type='nice'):
        ....:     M
        Traceback (most recent call last):
        ...
        AttributeError: The type 'nice' is not available. There needs to be an 'is_nice()'
        attribute for the type to be supported.

    REFERENCES:

    The underlying database was retrieved from Yoshitake Matsumoto's Database
    of Matroids; see [Mat2012]_.

    TESTS::

        sage: # optional - matroid_database
        sage: all_n = [1, 2, 4, 8, 17, 38, 98, 306, 1724, 383172]
        sage: for i in range(0, 8 + 1):
        ....:     assert len(list(matroids.AllMatroids(i))) == all_n[i]
        ....:     for M in matroids.AllMatroids(i):
        ....:         assert M.is_valid()
        sage: all = [
        ....:     [     1,     1,      1,    1,    1,    1,    1,    1,     1,      1,     1,      1,    1],
        ....:     [  None,     1,      2,    3,    4,    5,    6,    7,     8,      9,    10,     11,   12],
        ....:     [  None,  None,      1,    3,    7,   13,   23,   37,    58,     87,   128,    183,  259],
        ....:     [  None,  None,   None,    1,    4,   13,   38,  108,   325,   1275, 10037, 298491, None],
        ....:     [  None,  None,   None, None,    1,    5,   23,  108,   940, 190214,  None,   None, None],
        ....:     [  None,  None,   None, None, None,    1,    6,   37,   325, 190214,  None,   None, None],
        ....:     [  None,  None,   None, None, None, None,    1,    7,    58,   1275,  None,   None, None],
        ....:     [  None,  None,   None, None, None, None, None,    1,     8,     87, 10037,   None, None],
        ....:     [  None,  None,   None, None, None, None, None, None,     1,      9,   128, 298491, None],
        ....:     [  None,  None,   None, None, None, None, None, None,  None,      1,    10,    183, None],
        ....:     [  None,  None,   None, None, None, None, None, None,  None,   None,     1,     11,  259],
        ....:     [  None,  None,   None, None, None, None, None, None,  None,   None,  None,      1,   12],
        ....:     [  None,  None,   None, None, None, None, None, None,  None,   None,  None,   None,    1]
        ....: ]
        sage: for r in range(0, 12 + 1):  # long time
        ....:     for n in range(r, 12 + 1):
        ....:         if all[r][n] and all[r][n] < 1000:
        ....:             assert len(list(matroids.AllMatroids(n, r))) == all[r][n]
        ....:             for M in matroids.AllMatroids(n, r):
        ....:                 assert M.is_valid()
        sage: simple = [
        ....:     [    1,  None,   None, None, None, None, None, None,  None,  None,  None,   None, None],
        ....:     [ None,     1,   None, None, None, None, None, None,  None,  None,  None,   None, None],
        ....:     [ None,  None,      1,    1,    1,    1,    1,    1,     1,     1,     1,      1,    1],
        ....:     [ None,  None,   None,    1,    2,    4,    9,   23,    68,   383,  5249, 232928, None],
        ....:     [ None,  None,   None, None,    1,    3,   11,   49,   617, 185981, None,   None, None]
        ....: ]
        sage: for r in range(0, 4 + 1):  # long time
        ....:     for n in range(r, 12 + 1):
        ....:         if simple[r][n] and simple[r][n] < 1000:
        ....:             assert len(list(matroids.AllMatroids(n, r, 'simple'))) == simple[r][n]
        ....:             for M in matroids.AllMatroids(n, r, 'simple'):
        ....:                 assert M.is_valid() and M.is_simple()
        sage: unorientable = [
        ....:     [1,  3,    18,  201, 9413],
        ....:     [1, 34, 12284, None, None]
        ....: ]
        sage: for r in range(0, 1 + 1):  # long time
        ....:     for n in range(0, 4 + 1):
        ....:         if unorientable[r][n] and unorientable[r][n] < 1000:
        ....:             assert len(list(matroids.AllMatroids(n+7, r+3, 'unorientable'))) == unorientable[r][n]
        ....:             for M in matroids.AllMatroids(n+7, r+3, 'unorientable'):
        ....:                 assert M.is_valid()
    """
def OxleyMatroids() -> Generator[Incomplete]:
    """
    Iterate over Oxley's matroid collection.

    EXAMPLES::

        sage: OM = list(matroids.OxleyMatroids()); len(OM)
        44
        sage: import random
        sage: M = random.choice(OM)
        sage: M.is_valid()
        True

    .. SEEALSO::

        :mod:`Matroid catalog <sage.matroids.matroids_catalog>`, under
        ``Oxley's matroid collection``.

    REFERENCES:

    These matroids are the nonparametrized matroids that appear in the Appendix
    ``Some Interesting Matroids`` in [Oxl2011]_ (p. 639-64).
    """
def BrettellMatroids() -> Generator[Incomplete]:
    """
    Iterate over Brettell's matroid collection.

    EXAMPLES::

        sage: BM = list(matroids.BrettellMatroids()); len(BM)
        68
        sage: import random
        sage: M = random.choice(BM)
        sage: M.is_valid()
        True

    .. SEEALSO::

        :mod:`Matroid catalog <sage.matroids.matroids_catalog>`, under
        ``Brettell's matroid collection``.
    """
def VariousMatroids() -> Generator[Incomplete]:
    """
    Iterate over various other named matroids.

    EXAMPLES::

        sage: VM = list(matroids.VariousMatroids()); len(VM)
        16
        sage: import random
        sage: M = random.choice(VM)
        sage: M.is_valid()
        True

    .. SEEALSO::

        :mod:`Matroid catalog <sage.matroids.matroids_catalog>`, under
        ``Collection of various matroids``.
    """
