from _typeshed import Incomplete
from collections.abc import Generator
from sage.env import SAGE_SHARE as SAGE_SHARE

class SteinWatkinsIsogenyClass:
    conductor: Incomplete
    def __init__(self, conductor) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

class SteinWatkinsAllData:
    """
    Class for iterating through one of the Stein-Watkins database files
    for all conductors.
    """
    num: Incomplete
    def __init__(self, num) -> None: ...
    def __iter__(self):
        """
        EXAMPLES::

            sage: d = SteinWatkinsAllData(0)
            sage: d = d[10:20]                         # optional - database_stein_watkins; long time
            sage: for C in d:                          # optional - database_stein_watkins; long time
            ....:     print(C)
            Stein-Watkins isogeny class of conductor 11
            Stein-Watkins isogeny class of conductor 14
            Stein-Watkins isogeny class of conductor 15
            Stein-Watkins isogeny class of conductor 17
            Stein-Watkins isogeny class of conductor 19
            Stein-Watkins isogeny class of conductor 20
        """
    def __next__(self): ...
    next = __next__
    def __getitem__(self, N):
        """
        Return the curves of conductor N in this table. (Very slow!)
        Return all data about curves between the given levels in this
        database file.

        EXAMPLES::

            sage: d = SteinWatkinsAllData(0)
            sage: d[15:18]                             # optional - database_stein_watkins; long time
            [Stein-Watkins isogeny class of conductor 15, Stein-Watkins isogeny
             class of conductor 17]
        """
    def iter_levels(self) -> Generator[Incomplete]:
        """
        Iterate through the curve classes, but grouped into lists by
        level.

        EXAMPLES::

            sage: d = SteinWatkinsAllData(1)
            sage: E = d.iter_levels()
            sage: next(E)                             # optional - database_stein_watkins
            [Stein-Watkins isogeny class of conductor 100002]
            sage: next(E)                             # optional - database_stein_watkins
            [Stein-Watkins isogeny class of conductor 100005,
            Stein-Watkins isogeny class of conductor 100005]
            sage: next(E)                             # optional - database_stein_watkins
            [Stein-Watkins isogeny class of conductor 100007]
        """

class SteinWatkinsPrimeData(SteinWatkinsAllData):
    num: Incomplete
    def __init__(self, num) -> None: ...

def ecdb_num_curves(max_level: int = 200000):
    """
    Return a list whose `N`-th entry, for ``0 <= N <= max_level``, is the
    number of elliptic curves of conductor `N` in the database.

    EXAMPLES::

        sage: sage.databases.stein_watkins.ecdb_num_curves(100) # optional - database_stein_watkins
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 6, 8, 0, 4, 0, 3, 4, 6, 0, 0,
         6, 0, 5, 4, 0, 0, 8, 0, 4, 4, 4, 3, 4, 4, 5, 4, 4, 0, 6, 1, 2, 8, 2, 0,
         6, 4, 8, 2, 2, 1, 6, 4, 6, 7, 3, 0, 0, 1, 4, 6, 4, 2, 12, 1, 0, 2, 4, 0,
         6, 2, 0, 12, 1, 6, 4, 1, 8, 0, 2, 1, 6, 2, 0, 0, 1, 3, 16, 4, 3, 0, 2,
         0, 8, 0, 6, 11, 4]
    """
