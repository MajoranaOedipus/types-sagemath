from sage.matroids.matroid import Matroid as Matroid

class DualMatroid(Matroid):
    """
    Dual of a matroid.

    For some matroid representations it can be computationally expensive to
    derive an explicit representation of the dual. This class wraps around any
    matroid to provide an abstract dual. It also serves as the default
    implementation of the dual.

    INPUT:

    - ``matroid`` -- matroid

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: M = matroids.catalog.Vamos()
        sage: Md = DualMatroid(M)  # indirect doctest
        sage: Md.rank('abd') == M.corank('abd')
        True
        sage: Md
        Dual of 'Vamos: Matroid of rank 4 on 8 elements with circuit-closures
        {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'}, {'a', 'b', 'g', 'h'},
             {'c', 'd', 'e', 'f'}, {'e', 'f', 'g', 'h'}},
         4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}'
    """
    def __init__(self, matroid) -> None:
        """
        See the class definition for documentation.

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = matroids.catalog.Vamos()
            sage: Md = DualMatroid(M)  # indirect doctest
            sage: Md.rank('abd') == M.corank('abd')
            True
            sage: Md
            Dual of 'Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}'

        TESTS::

            sage: from sage.matroids.dual_matroid import DualMatroid
            sage: DualMatroid([])
            Traceback (most recent call last):
            ...
            TypeError: no matroid provided to take the dual of
        """
    def groundset(self):
        """
        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: M = matroids.catalog.Pappus().dual()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        """
    def dual(self):
        """
        Return the dual of the matroid.

        Let `M` be a matroid with groundset `E`. If `B` is the set of bases
        of `M`, then the set `\\{E - b : b \\in B\\}` is the set of bases of
        another matroid, the *dual* of `M`. Note that the dual of the dual of
        `M` equals `M`, so if this is the :class:`DualMatroid` instance
        wrapping `M` then the returned matroid is `M`.

        OUTPUT: the dual matroid

        EXAMPLES::

            sage: M = matroids.catalog.Pappus().dual()
            sage: N = M.dual()
            sage: N.rank()
            3
            sage: N
            Pappus: Matroid of rank 3 on 9 elements with 9 nonspanning circuits
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

            sage: M = matroids.catalog.Vamos().dual()
            sage: N = matroids.catalog.Vamos().dual()
            sage: O = matroids.catalog.Vamos()
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

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M1 = matroids.catalog.Fano()
            sage: M2 = CircuitClosuresMatroid(M1.dual())
            sage: M3 = CircuitClosuresMatroid(M1).dual()
            sage: M4 = CircuitClosuresMatroid(groundset='abcdefg',
            ....:   circuit_closures={3: ['abcdefg'], 2: ['beg', 'cdb', 'cfg',
            ....:   'ace', 'fed', 'gad', 'fab']}).dual()
            sage: M1.dual() == M2  # indirect doctest
            False
            sage: M2 == M3
            False
            sage: M3 == M4
            True
        """
    def __ne__(self, other):
        """
        Compare two matroids.

        INPUT:

        - ``other`` -- matroid

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M1 = matroids.catalog.Fano()
            sage: M2 = CircuitClosuresMatroid(M1.dual())
            sage: M3 = CircuitClosuresMatroid(M1).dual()
            sage: M4 = CircuitClosuresMatroid(groundset='abcdefg',
            ....:   circuit_closures={3: ['abcdefg'], 2: ['beg', 'cdb', 'cfg',
            ....:                'ace', 'fed', 'gad', 'fab']}).dual()
            sage: M1.dual() != M2  # indirect doctest
            True
            sage: M2 != M3
            True
            sage: M3 != M4
            False
        """
    def __reduce__(self):
        """
        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(M, name)`` where ``M`` is
        the internal matroid, and ``name`` is a custom name.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos().dual()
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: loads(dumps(M))
            Dual of 'Vamos:
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}'
        """
    def relabel(self, mapping):
        """
        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: M = matroids.catalog.K5dual(range(10))
            sage: type(M)
            <class 'sage.matroids.dual_matroid.DualMatroid'>
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: N = M.dual().relabel({0:10})
            sage: sorted(N.groundset())
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sage: N.is_isomorphic(matroids.catalog.K5())
            True

        TESTS::

            sage: M = matroids.catalog.K5dual(range(10))
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
            ....:      5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])
        """
    def is_valid(self, certificate: bool = False):
        """
        Test if ``self`` obeys the matroid axioms.

        For a :class:`DualMatroid`, we check its dual.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: M = matroids.catalog.K5dual()
            sage: type(M)
            <class 'sage.matroids.dual_matroid.DualMatroid'>
            sage: M.is_valid()
            True
            sage: M = Matroid([[0, 1], [2, 3]])
            sage: M.dual().is_valid()
            False
        """
