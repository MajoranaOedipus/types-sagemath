import sage.matroids.matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matroids.utilities import setprint_s as setprint_s
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class CircuitClosuresMatroid(sage.matroids.matroid.Matroid):
    """CircuitClosuresMatroid(M=None, groundset=None, circuit_closures=None)

    File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 68)

    A general matroid `M` is characterized by its rank `r(M)` and the set of
    pairs

    `(k, \\{` closure `(C) : C ` circuit of ` M, r(C)=k\\})` for `k=0, .., r(M)-1`

    As each independent set of size `k` is in at most one closure(`C`) of rank
    `k`, and each closure(`C`) of rank `k` contains at least `k + 1`
    independent sets of size `k`, there are at most `\\binom{n}{k}/(k + 1)`
    such closures-of-circuits of rank `k`. Each closure(`C`) takes `O(n)` bits
    to store, giving an upper bound of `O(2^n)` on the space complexity of the
    entire matroid.

    A subset `X` of the groundset is independent if and only if

    `| X \\cap ` closure `(C) | \\leq k` for all circuits `C` of `M` with
    `r(C)=k`.

    So determining whether a set is independent takes time proportional to the
    space complexity of the matroid.

    INPUT:

    - ``M`` -- matroid (default: ``None``)
    - ``groundset`` -- groundset of a matroid (default: ``None``)
    - ``circuit_closures`` -- dictionary (default: ``None``); the collection of
      circuit closures of a matroid presented as a dictionary whose keys are
      ranks, and whose values are sets of circuit closures of the specified rank

    OUTPUT:

    - If the input is a matroid ``M``, return a ``CircuitClosuresMatroid``
      instance representing ``M``.
    - Otherwise, return a ``CircuitClosuresMatroid`` instance based on
      ``groundset`` and ``circuit_closures``.

    .. NOTE::

        For a more flexible means of input, use the ``Matroid()`` function.

    EXAMPLES::

        sage: from sage.matroids.advanced import *
        sage: M = CircuitClosuresMatroid(matroids.catalog.Fano())
        sage: M
        Matroid of rank 3 on 7 elements with circuit-closures
        {2: {{'a', 'b', 'f'}, {'a', 'c', 'e'}, {'a', 'd', 'g'},
             {'b', 'c', 'd'}, {'b', 'e', 'g'}, {'c', 'f', 'g'},
             {'d', 'e', 'f'}}, 3: {{'a', 'b', 'c', 'd', 'e', 'f', 'g'}}}
        sage: M = CircuitClosuresMatroid(groundset='abcdefgh',
        ....:            circuit_closures={3: ['edfg', 'acdg', 'bcfg', 'cefh',
        ....:                 'afgh', 'abce', 'abdf', 'begh', 'bcdh', 'adeh'],
        ....:                              4: ['abcdefgh']})
        sage: M.equals(matroids.catalog.P8())
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, M=..., groundset=..., circuit_closures=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 128)

                Initialization of the matroid. See the class docstring for full
                documentation.

                EXAMPLES::

                    sage: from sage.matroids.advanced import *
                    sage: M = CircuitClosuresMatroid(matroids.catalog.Fano())
                    sage: M
                    Matroid of rank 3 on 7 elements with circuit-closures
                    {2: {{'a', 'b', 'f'}, {'a', 'c', 'e'}, {'a', 'd', 'g'},
                         {'b', 'c', 'd'}, {'b', 'e', 'g'}, {'c', 'f', 'g'},
                         {'d', 'e', 'f'}},
                     3: {{'a', 'b', 'c', 'd', 'e', 'f', 'g'}}}

                    sage: M = CircuitClosuresMatroid(groundset='abcdefgh',
                    ....:        circuit_closures={3: ['edfg', 'acdg', 'bcfg', 'cefh',
                    ....:             'afgh', 'abce', 'abdf', 'begh', 'bcdh', 'adeh'],
                    ....:                          4: ['abcdefgh']})
                    sage: M.equals(matroids.catalog.P8())
                    True

                TESTS::

                    sage: from sage.matroids.advanced import *
                    sage: M = CircuitClosuresMatroid(matroids.catalog.Fano())
                    sage: TestSuite(M).run()
        """
    @overload
    def circuit_closures(self) -> dict:
        """CircuitClosuresMatroid.circuit_closures(self) -> dict

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 319)

        Return the closures of circuits of the matroid.

        A *circuit closure* is a closed set containing a circuit.

        OUTPUT: dictionary containing the circuit closures of the matroid,
        indexed by their ranks

        .. SEEALSO::

            :meth:`Matroid.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`Matroid.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = CircuitClosuresMatroid(matroids.catalog.Fano())
            sage: CC = M.circuit_closures()
            sage: len(CC[2])
            7
            sage: len(CC[3])
            1
            sage: len(CC[1])
            Traceback (most recent call last):
            ...
            KeyError: 1
            sage: [sorted(X) for X in CC[3]]
            [['a', 'b', 'c', 'd', 'e', 'f', 'g']]"""
    @overload
    def circuit_closures(self) -> Any:
        """CircuitClosuresMatroid.circuit_closures(self) -> dict

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 319)

        Return the closures of circuits of the matroid.

        A *circuit closure* is a closed set containing a circuit.

        OUTPUT: dictionary containing the circuit closures of the matroid,
        indexed by their ranks

        .. SEEALSO::

            :meth:`Matroid.circuit() <sage.matroids.matroid.Matroid.circuit>`,
            :meth:`Matroid.closure() <sage.matroids.matroid.Matroid.closure>`

        EXAMPLES::

            sage: from sage.matroids.advanced import *
            sage: M = CircuitClosuresMatroid(matroids.catalog.Fano())
            sage: CC = M.circuit_closures()
            sage: len(CC[2])
            7
            sage: len(CC[3])
            1
            sage: len(CC[1])
            Traceback (most recent call last):
            ...
            KeyError: 1
            sage: [sorted(X) for X in CC[3]]
            [['a', 'b', 'c', 'd', 'e', 'f', 'g']]"""
    @overload
    def full_rank(self) -> Any:
        """CircuitClosuresMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 206)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_rank()
            4
            sage: M.dual().full_rank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """CircuitClosuresMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 206)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_rank()
            4
            sage: M.dual().full_rank()
            4"""
    @overload
    def full_rank(self) -> Any:
        """CircuitClosuresMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 206)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M.full_rank()
            4
            sage: M.dual().full_rank()
            4"""
    @overload
    def groundset(self) -> frozenset:
        """CircuitClosuresMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 167)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: frozenset

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']"""
    @overload
    def groundset(self) -> Any:
        """CircuitClosuresMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 167)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: frozenset

        EXAMPLES::

            sage: M = matroids.catalog.Pappus()
            sage: sorted(M.groundset())
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']"""
    @overload
    def relabel(self, mapping) -> Any:
        """CircuitClosuresMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 511)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.circuit_closures_matroid import CircuitClosuresMatroid
            sage: M = CircuitClosuresMatroid(matroids.catalog.RelaxedNonFano())
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
            sage: N = M.relabel({'g': 'x', 0: 'z'})  # 'g': 'x' is ignored
            sage: from sage.matroids.utilities import cmp_elements_key
            sage: sorted(N.groundset(), key=cmp_elements_key)
            [1, 2, 3, 4, 5, 6, 'z']
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.circuit_closures_matroid import CircuitClosuresMatroid
            sage: M = CircuitClosuresMatroid(matroids.catalog.RelaxedNonFano())
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """CircuitClosuresMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 511)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.circuit_closures_matroid import CircuitClosuresMatroid
            sage: M = CircuitClosuresMatroid(matroids.catalog.RelaxedNonFano())
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
            sage: N = M.relabel({'g': 'x', 0: 'z'})  # 'g': 'x' is ignored
            sage: from sage.matroids.utilities import cmp_elements_key
            sage: sorted(N.groundset(), key=cmp_elements_key)
            [1, 2, 3, 4, 5, 6, 'z']
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.circuit_closures_matroid import CircuitClosuresMatroid
            sage: M = CircuitClosuresMatroid(matroids.catalog.RelaxedNonFano())
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """CircuitClosuresMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 420)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: N = matroids.catalog.Vamos()
            sage: hash(M) == hash(N)
            True
            sage: O = matroids.catalog.NonVamos()
            sage: hash(M) == hash(O)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """CircuitClosuresMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuit_closures_matroid.pyx (starting at line 480)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(E, CC, name)`` where ``E`` is
        the groundset, ``CC`` is the dictionary of circuit closures, and
        ``name`` is a custom name.

        EXAMPLES::

            sage: M = matroids.catalog.Vamos()
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.reset_name()
            sage: loads(dumps(M))
            Matroid of rank 4 on 8 elements with circuit-closures
            {3: {{'a', 'b', 'c', 'd'}, {'a', 'b', 'e', 'f'},
                 {'a', 'b', 'g', 'h'}, {'c', 'd', 'e', 'f'},
                 {'e', 'f', 'g', 'h'}},
             4: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}"""
