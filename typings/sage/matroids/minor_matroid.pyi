from sage.matroids.matroid import Matroid as Matroid
from sage.matroids.utilities import setprint_s as setprint_s

class MinorMatroid(Matroid):
    """
    Minor of a matroid.

    For some matroid representations, it can be computationally
    expensive to derive an explicit representation of a minor. This
    class wraps around any matroid to provide an abstract minor. It
    also serves as default implementation.

    Return a minor.

    INPUT:

    - ``matroid`` -- matroid
    - ``contractions`` -- an object with Python's ``frozenset`` interface
      containing a subset of ``self.groundset()``.
    - ``deletions`` -- an object with Python's ``frozenset`` interface
      containing a subset of ``self.groundset()``

    OUTPUT:

    A ``MinorMatroid`` instance representing
    ``matroid / contractions \\ deletions``.

    .. WARNING::

        This class does NOT do any checks. Besides the assumptions above, we
        assume the following:

        - ``contractions`` is independent
        - ``deletions`` is coindependent
        - ``contractions`` and ``deletions`` are disjoint.

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: M = matroids.catalog.Vamos()
        sage: N = MinorMatroid(matroid=M, contractions=set(['a']),
        ....:                  deletions=set())
        sage: N._minor(contractions=set(), deletions=set(['b', 'c']))
        M / {'a'} \\ {'b', 'c'}, where M is Vamos:
        Matroid of rank 4 on 8 elements with circuit-closures
        {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'}, {'a', 'b', 'g', 'h'},
             {'c', 'd', 'e', 'f'}, {'e', 'f', 'g', 'h'}},
         4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}
    """
    def __init__(self, matroid, contractions=None, deletions=None) -> None:
        """
        See the class docstring for documentation.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = MinorMatroid(matroids.catalog.Fano(),  # indirect doctest
            ....:                  contractions=set(), deletions=set(['g']))
            sage: M.is_isomorphic(matroids.Wheel(3))
            True
        """
    def groundset(self):
        """
        Return the groundset of the matroid.

        EXAMPLES::

            sage: M = matroids.catalog.Pappus().contract(['c'])
            sage: sorted(M.groundset())
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        """
    def __hash__(self):
        """
        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = MinorMatroid(matroids.catalog.Vamos(),
            ....:                 contractions=set('c'), deletions={'b', 'f'})
            sage: N = MinorMatroid(matroids.catalog.Vamos(),
            ....:                 deletions={'b', 'f'}, contractions=set('c'))
            sage: O = MinorMatroid(matroids.catalog.Vamos(),
            ....:                 contractions={'b', 'f'}, deletions=set('c'))
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

        ``True`` if ``self`` and ``other`` have the same underlying matroid,
        same set of contractions, and same set of deletions; ``False``
        otherwise.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = MinorMatroid(M, set('ab'), set('f'))
            sage: M2 = MinorMatroid(M, set('af'), set('b'))
            sage: M3 = MinorMatroid(M, set('a'), set('f'))._minor(set('b'), set())
            sage: M1 == M2  # indirect doctest
            False
            sage: M1.equals(M2)
            True
            sage: M1 == M3
            True
        """
    def __ne__(self, other):
        """
        Compare two matroids.

        INPUT:

        - ``other`` -- matroid

        OUTPUT:

        ``False`` if ``self`` and ``other`` have the same underlying matroid,
        same set of contractions, and same set of deletions; ``True``
        otherwise.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Fano()
            sage: M1 = MinorMatroid(M, set('ab'), set('f'))
            sage: M2 = MinorMatroid(M, set('af'), set('b'))
            sage: M3 = MinorMatroid(M, set('a'), set('f'))._minor(set('b'), set())
            sage: M1 != M2  # indirect doctest
            True
            sage: M1.equals(M2)
            True
            sage: M1 != M3
            False
        """
    def __reduce__(self):
        """
        Save the matroid for later reloading.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos().minor('abc', 'g')
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: loads(dumps(M))
            M / {'a', 'b', 'c'} \\ {'g'}, where M is Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}
        """
