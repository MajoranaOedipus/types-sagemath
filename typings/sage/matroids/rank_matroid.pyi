from sage.matroids.matroid import Matroid as Matroid

class RankMatroid(Matroid):
    """
    Matroid specified by its rank function.

    INPUT:

    - ``groundset`` -- the groundset of a matroid
    - ``rank_function`` -- a function mapping subsets of ``groundset`` to
      nonnegative integers

    OUTPUT: a matroid on ``groundset`` whose rank function equals ``rank_function``

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: def f(X):
        ....:     return min(len(X), 3)
        sage: M = RankMatroid(groundset=range(6), rank_function=f)
        sage: M.is_valid()
        True
        sage: M.is_isomorphic(matroids.Uniform(3, 6))
        True
    """
    def __init__(self, groundset, rank_function) -> None:
        """
        Initialize the rank matroid.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = RankMatroid(range(6),
            ....:                 rank_function=matroids.Uniform(3, 6).rank)
            sage: M
            Matroid of rank 3 on 6 elements
        """
    def groundset(self):
        """
        Return the groundset of ``self``.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = RankMatroid(range(6),
            ....:                 rank_function=matroids.Uniform(3, 6).rank)
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5]
        """
    def __hash__(self):
        """
        Return a string invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = Matroid(groundset=range(10),
            ....:             rank_function=lambda X: min(len(X), 4))
            sage: N = Matroid(groundset=range(10),
            ....:             rank_function=lambda X: min(len(X), 4))
            sage: O = Matroid(groundset=range(10),
            ....:             rank_function=lambda X: min(len(X), 3))
            sage: hash(M) == hash(N)
            True
            sage: hash(M) == hash(O)
            False
        """
    def __eq__(self, other):
        """
        Compare two matroids.

        INPUT:

        - ``other`` -- matroid

        OUTPUT:

        ``True`` if ``self`` and ``other have the same groundset and the same
        rank function; ``False`` otherwise.

        .. NOTE::

            Note that rank functions ``f`` and ``g`` are normally deemed equal
            only if ``f is g``. It would be too time-consuming to check all
            their values.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: def f(X):
            ....:     return min(len(X), 3)
            sage: def g(X):
            ....:     return min(len(X), 3)
            sage: M1 = RankMatroid(groundset=range(6), rank_function=f)
            sage: M2 = RankMatroid(groundset=range(6), rank_function=g)
            sage: M3 = RankMatroid(groundset=range(7), rank_function=f)
            sage: M4 = RankMatroid(groundset=range(6), rank_function=f)
            sage: M1 == M2  # indirect doctest
            False
            sage: M1 == M3
            False
            sage: M1 == M4
            True
        """
    def __ne__(self, other):
        """
        Compare two matroids.

        INPUT:

        - ``other`` -- matroid

        OUTPUT:

        ``False`` if ``self`` and ``other have the same groundset and the
        same rank function; ``True`` otherwise.

        .. NOTE::

            Rank functions ``f`` and ``g`` are normally deemed equal only if
            ``f is g``. It would be too time-consuming to check all their
            values.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: def f(X):
            ....:     return min(len(X), 3)
            sage: def g(X):
            ....:     return min(len(X), 3)
            sage: M1 = RankMatroid(groundset=range(6), rank_function=f)
            sage: M2 = RankMatroid(groundset=range(6), rank_function=g)
            sage: M3 = RankMatroid(groundset=range(7), rank_function=f)
            sage: M4 = RankMatroid(groundset=range(6), rank_function=f)
            sage: M1 != M2  # indirect doctest
            True
            sage: M1 != M3
            True
            sage: M1 != M4
            False
        """
    def __reduce__(self) -> None:
        """
        Save the matroid for later reloading.

        .. NOTE::

            Unfortunately, functions cannot be pickled reliably, so this class
            doesn't have load/save support

        EXAMPLES::

            sage: M = Matroid(groundset=range(10),
            ....:             rank_function=lambda X: min(len(X), 4))
            sage: M == loads(dumps(M))  # indirect doctest
            Traceback (most recent call last):
            ...
            TypeError: unfortunately, functions cannot be saved reliably, so
            this class doesn't have load/save support. Convert to another
            class, such as BasisMatroid, instead.
        """
