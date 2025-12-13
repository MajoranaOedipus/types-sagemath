import sage.matroids.matroid
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class CircuitsMatroid(sage.matroids.matroid.Matroid):
    """CircuitsMatroid(M=None, groundset=None, circuits=None, nsc_defined=False)

    File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 38)

    A matroid defined by its circuits.

    INPUT:

    - ``M`` -- matroid (default: ``None``)
    - ``groundset`` -- list (default: ``None``); the groundset of the matroid
    - ``circuits`` -- list (default: ``None``); the collection of circuits of
      the matroid
    - ``nsc_defined`` -- boolean (default: ``False``); whether the matroid was
      defined by its nonspanning circuits

    .. NOTE::

        For a more flexible means of input, use the ``Matroid()`` function."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, M=..., groundset=..., circuits=..., nsc_defined=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 58)

                Initialization of the matroid. See the class docstring for full
                documentation.

                TESTS::

                    sage: from sage.matroids.circuits_matroid import CircuitsMatroid
                    sage: M = CircuitsMatroid(matroids.catalog.Fano())
                    sage: TestSuite(M).run()
        """
    @overload
    def bases_iterator(self) -> Any:
        """CircuitsMatroid.bases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 447)

        Return an iterator over the bases of the matroid.

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: it = M.bases_iterator()
            sage: it.__next__()
            frozenset({0, 1})
            sage: sorted(M.bases_iterator(), key=str)
            [frozenset({0, 1}),
             frozenset({0, 2}),
             frozenset({0, 3}),
             frozenset({1, 2}),
             frozenset({1, 3}),
             frozenset({2, 3})]"""
    @overload
    def bases_iterator(self) -> Any:
        """CircuitsMatroid.bases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 447)

        Return an iterator over the bases of the matroid.

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: it = M.bases_iterator()
            sage: it.__next__()
            frozenset({0, 1})
            sage: sorted(M.bases_iterator(), key=str)
            [frozenset({0, 1}),
             frozenset({0, 2}),
             frozenset({0, 3}),
             frozenset({1, 2}),
             frozenset({1, 3}),
             frozenset({2, 3})]"""
    @overload
    def bases_iterator(self) -> Any:
        """CircuitsMatroid.bases_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 447)

        Return an iterator over the bases of the matroid.

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: it = M.bases_iterator()
            sage: it.__next__()
            frozenset({0, 1})
            sage: sorted(M.bases_iterator(), key=str)
            [frozenset({0, 1}),
             frozenset({0, 2}),
             frozenset({0, 3}),
             frozenset({1, 2}),
             frozenset({1, 3}),
             frozenset({2, 3})]"""
    @overload
    def broken_circuit_complex(self, ordering=..., reduced=...) -> Any:
        """CircuitsMatroid.broken_circuit_complex(self, ordering=None, reduced=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 786)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``); whether to return the
          reduced broken circuit complex (the link at the smallest element)

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: M.broken_circuit_complex()
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5, 4, 3, 2, 1])
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}
            sage: M.broken_circuit_complex([5, 4, 3, 2, 1], reduced=True)
            Simplicial complex with vertex set (1, 2, 3, 4)
             and facets {(1, 3), (1, 4), (2, 3), (2, 4)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(groundset=[0, 1, 2], circuits=[[0]])
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined"""
    @overload
    def broken_circuit_complex(self) -> Any:
        """CircuitsMatroid.broken_circuit_complex(self, ordering=None, reduced=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 786)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``); whether to return the
          reduced broken circuit complex (the link at the smallest element)

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: M.broken_circuit_complex()
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5, 4, 3, 2, 1])
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}
            sage: M.broken_circuit_complex([5, 4, 3, 2, 1], reduced=True)
            Simplicial complex with vertex set (1, 2, 3, 4)
             and facets {(1, 3), (1, 4), (2, 3), (2, 4)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(groundset=[0, 1, 2], circuits=[[0]])
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined"""
    @overload
    def broken_circuit_complex(self) -> Any:
        """CircuitsMatroid.broken_circuit_complex(self, ordering=None, reduced=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 786)

        Return the broken circuit complex of ``self``.

        The broken circuit complex of a matroid with a total ordering `<`
        on the groundset is obtained from the
        :meth:`NBC sets <no_broken_circuits_sets>` under subset inclusion.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``); whether to return the
          reduced broken circuit complex (the link at the smallest element)

        OUTPUT: a simplicial complex of the NBC sets under inclusion

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: M.broken_circuit_complex()
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: M.broken_circuit_complex([5, 4, 3, 2, 1])
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}
            sage: M.broken_circuit_complex([5, 4, 3, 2, 1], reduced=True)
            Simplicial complex with vertex set (1, 2, 3, 4)
             and facets {(1, 3), (1, 4), (2, 3), (2, 4)}

        For a matroid with loops, the broken circuit complex is not defined,
        and the method yields an error::

            sage: M = Matroid(groundset=[0, 1, 2], circuits=[[0]])
            sage: M.broken_circuit_complex()
            Traceback (most recent call last):
            ...
            ValueError: broken circuit complex of matroid with loops is not defined"""
    @overload
    def circuits(self, k=...) -> SetSystem:
        """CircuitsMatroid.circuits(self, k=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 566)

        Return the circuits of the matroid.

        INPUT:

        - ``k`` -- integer (optional); the length of the circuits

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: M.circuits()
            SetSystem of 4 sets over 4 elements
            sage: list(M.circuits(0))
            []
            sage: sorted(M.circuits(3), key=str)
            [frozenset({0, 1, 2}),
             frozenset({0, 1, 3}),
             frozenset({0, 2, 3}),
             frozenset({1, 2, 3})]"""
    @overload
    def circuits(self) -> Any:
        """CircuitsMatroid.circuits(self, k=None) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 566)

        Return the circuits of the matroid.

        INPUT:

        - ``k`` -- integer (optional); the length of the circuits

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: M.circuits()
            SetSystem of 4 sets over 4 elements
            sage: list(M.circuits(0))
            []
            sage: sorted(M.circuits(3), key=str)
            [frozenset({0, 1, 2}),
             frozenset({0, 1, 3}),
             frozenset({0, 2, 3}),
             frozenset({1, 2, 3})]"""
    @overload
    def circuits_iterator(self, k=...) -> Any:
        """CircuitsMatroid.circuits_iterator(self, k=None)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 601)

        Return an iterator over the circuits of the matroid.

        INPUT:

        - ``k`` -- integer (optional); the length of the circuits

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: sum(1 for C in M.circuits_iterator())
            4
            sage: list(M.circuits_iterator(0))
            []
            sage: sorted(M.circuits_iterator(3), key=str)
            [frozenset({0, 1, 2}),
             frozenset({0, 1, 3}),
             frozenset({0, 2, 3}),
             frozenset({1, 2, 3})]"""
    @overload
    def circuits_iterator(self) -> Any:
        """CircuitsMatroid.circuits_iterator(self, k=None)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 601)

        Return an iterator over the circuits of the matroid.

        INPUT:

        - ``k`` -- integer (optional); the length of the circuits

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: sum(1 for C in M.circuits_iterator())
            4
            sage: list(M.circuits_iterator(0))
            []
            sage: sorted(M.circuits_iterator(3), key=str)
            [frozenset({0, 1, 2}),
             frozenset({0, 1, 3}),
             frozenset({0, 2, 3}),
             frozenset({1, 2, 3})]"""
    def dependent_sets(self, longk) -> SetSystem:
        """CircuitsMatroid.dependent_sets(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 521)

        Return the dependent sets of fixed size.

        INPUT:

        - ``k`` -- integer

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.Vamos())
            sage: M.dependent_sets(3)
            SetSystem of 0 sets over 8 elements
            sage: sorted([sorted(X) for X in M.dependent_sets(4)])
            [['a', 'b', 'c', 'd'], ['a', 'b', 'e', 'f'], ['a', 'b', 'g', 'h'],
             ['c', 'd', 'e', 'f'], ['e', 'f', 'g', 'h']]

        TESTS::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: len(M.nonbases())
            0
            sage: M = CircuitsMatroid(matroids.CompleteGraphic(6))
            sage: len(M.nonbases())
            1707"""
    @overload
    def full_rank(self) -> Any:
        """CircuitsMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 124)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.Theta(20)
            sage: M.full_rank()
            20"""
    @overload
    def full_rank(self) -> Any:
        """CircuitsMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 124)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: M = matroids.Theta(20)
            sage: M.full_rank()
            20"""
    def girth(self) -> Any:
        """CircuitsMatroid.girth(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 831)

        Return the girth of the matroid.

        The girth is the size of the smallest circuit. In case the matroid has
        no circuits the girth is `\\infty`.

        EXAMPLES::

            sage: matroids.Theta(10).girth()
            3

        REFERENCES:

        [Oxl2011]_, p. 327."""
    @overload
    def groundset(self) -> frozenset:
        """CircuitsMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 85)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: M = matroids.Theta(2)
            sage: sorted(M.groundset())
            ['x0', 'x1', 'y0', 'y1']"""
    @overload
    def groundset(self) -> Any:
        """CircuitsMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 85)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: set

        EXAMPLES::

            sage: M = matroids.Theta(2)
            sage: sorted(M.groundset())
            ['x0', 'x1', 'y0', 'y1']"""
    def independent_sets(self, longk=...) -> SetSystem:
        """CircuitsMatroid.independent_sets(self, long k=-1) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 474)

        Return the independent sets of the matroid.

        INPUT:

        - ``k`` -- integer (optional); if specified, return the size-`k`
          independent sets of the matroid

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.Pappus())
            sage: M.independent_sets(4)
            SetSystem of 0 sets over 9 elements
            sage: M.independent_sets(3)
            SetSystem of 75 sets over 9 elements
            sage: frozenset({'a', 'c', 'e'}) in _
            True

        TESTS::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.CompleteGraphic(4))
            sage: len(M.bases())
            16

        .. SEEALSO::

            :meth:`M.bases() <sage.matroids.circuits_matroid.bases>`"""
    @overload
    def is_paving(self) -> bool:
        """CircuitsMatroid.is_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 850)

        Return if ``self`` is paving.

        A matroid is paving if each of its circuits has size `r` or `r+1`.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.Vamos())
            sage: M.is_paving()
            True"""
    @overload
    def is_paving(self) -> Any:
        """CircuitsMatroid.is_paving(self) -> bool

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 850)

        Return if ``self`` is paving.

        A matroid is paving if each of its circuits has size `r` or `r+1`.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.Vamos())
            sage: M.is_paving()
            True"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def is_valid(self) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def is_valid(self) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def is_valid(self) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def is_valid(self) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def is_valid(self) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """CircuitsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 869)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its circuits, we check the circuit axioms.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: C = [[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[3, 6], [1, 2, 3], [3, 4, 5], [1, 2, 6], [6, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            True
            sage: C = [[], [1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid()
            False
            sage: C = [[1, 2, 3], [3, 4, 5]]
            sage: M = Matroid(circuits=C)
            sage: M.is_valid(certificate=True)
            (False,
             {'circuit 1': frozenset({...}),
              'circuit 2': frozenset({...}),
              'element': 3,
              'error': 'elimination axiom failed'})"""
    @overload
    def no_broken_circuits_facets(self, ordering=..., reduced=...) -> SetSystem:
        """CircuitsMatroid.no_broken_circuits_facets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 675)

        Return the no broken circuits (NBC) facets of ``self``.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[0, 1, 2]])
            sage: M.no_broken_circuits_facets(ordering=[1, 0, 2])
            SetSystem of 2 sets over 3 elements
            sage: sorted([sorted(X) for X in _])
            [[0, 1], [1, 2]]
            sage: M.no_broken_circuits_facets(ordering=[1, 0, 2], reduced=True)
            SetSystem of 2 sets over 3 elements
            sage: sorted([sorted(X) for X in _])
            [[0], [2]]"""
    @overload
    def no_broken_circuits_facets(self, ordering=...) -> Any:
        """CircuitsMatroid.no_broken_circuits_facets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 675)

        Return the no broken circuits (NBC) facets of ``self``.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[0, 1, 2]])
            sage: M.no_broken_circuits_facets(ordering=[1, 0, 2])
            SetSystem of 2 sets over 3 elements
            sage: sorted([sorted(X) for X in _])
            [[0, 1], [1, 2]]
            sage: M.no_broken_circuits_facets(ordering=[1, 0, 2], reduced=True)
            SetSystem of 2 sets over 3 elements
            sage: sorted([sorted(X) for X in _])
            [[0], [2]]"""
    @overload
    def no_broken_circuits_facets(self, ordering=..., reduced=...) -> Any:
        """CircuitsMatroid.no_broken_circuits_facets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 675)

        Return the no broken circuits (NBC) facets of ``self``.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[0, 1, 2]])
            sage: M.no_broken_circuits_facets(ordering=[1, 0, 2])
            SetSystem of 2 sets over 3 elements
            sage: sorted([sorted(X) for X in _])
            [[0, 1], [1, 2]]
            sage: M.no_broken_circuits_facets(ordering=[1, 0, 2], reduced=True)
            SetSystem of 2 sets over 3 elements
            sage: sorted([sorted(X) for X in _])
            [[0], [2]]"""
    @overload
    def no_broken_circuits_sets(self, ordering=..., reduced=...) -> SetSystem:
        """CircuitsMatroid.no_broken_circuits_sets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 738)

        Return the no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets())
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1, 2, 3], [1, 4, 5], [2, 3, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        TESTS::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: C1 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: from sage.matroids.basis_matroid import BasisMatroid
            sage: M = BasisMatroid(Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]))
            sage: C2 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: C1 == C2
            True"""
    @overload
    def no_broken_circuits_sets(self) -> Any:
        """CircuitsMatroid.no_broken_circuits_sets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 738)

        Return the no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets())
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1, 2, 3], [1, 4, 5], [2, 3, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        TESTS::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: C1 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: from sage.matroids.basis_matroid import BasisMatroid
            sage: M = BasisMatroid(Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]))
            sage: C2 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: C1 == C2
            True"""
    @overload
    def no_broken_circuits_sets(self) -> Any:
        """CircuitsMatroid.no_broken_circuits_sets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 738)

        Return the no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets())
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1, 2, 3], [1, 4, 5], [2, 3, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        TESTS::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: C1 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: from sage.matroids.basis_matroid import BasisMatroid
            sage: M = BasisMatroid(Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]))
            sage: C2 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: C1 == C2
            True"""
    @overload
    def no_broken_circuits_sets(self) -> Any:
        """CircuitsMatroid.no_broken_circuits_sets(self, ordering=None, reduced=False) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 738)

        Return the no broken circuits (NBC) sets of ``self``.

        An NBC set is a subset `A` of the groundset under some total
        ordering `<` such that `A` contains no broken circuit.

        INPUT:

        - ``ordering`` -- list (optional); a total ordering of the groundset
        - ``reduced`` -- boolean (default: ``False``)

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets())
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5)}
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)}

        ::

            sage: M = Matroid(circuits=[[1, 2, 3], [1, 4, 5], [2, 3, 4, 5]])
            sage: SimplicialComplex(M.no_broken_circuits_sets([5, 4, 3, 2, 1]))
            Simplicial complex with vertex set (1, 2, 3, 4, 5)
             and facets {(1, 3, 5), (2, 3, 5), (2, 4, 5), (3, 4, 5)}

        TESTS::

            sage: M = Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]])
            sage: C1 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: from sage.matroids.basis_matroid import BasisMatroid
            sage: M = BasisMatroid(Matroid(circuits=[[1, 2, 3], [3, 4, 5], [1, 2, 4, 5]]))
            sage: C2 = SimplicialComplex(M.no_broken_circuits_sets())
            sage: C1 == C2
            True"""
    @overload
    def nonspanning_circuits(self) -> SetSystem:
        """CircuitsMatroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 632)

        Return the nonspanning circuits of the matroid.

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: M.nonspanning_circuits()
            SetSystem of 0 sets over 4 elements
            sage: M = matroids.Theta(5)
            sage: M.nonspanning_circuits()
            SetSystem of 15 sets over 10 elements"""
    @overload
    def nonspanning_circuits(self) -> Any:
        """CircuitsMatroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 632)

        Return the nonspanning circuits of the matroid.

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: M.nonspanning_circuits()
            SetSystem of 0 sets over 4 elements
            sage: M = matroids.Theta(5)
            sage: M.nonspanning_circuits()
            SetSystem of 15 sets over 10 elements"""
    @overload
    def nonspanning_circuits(self) -> Any:
        """CircuitsMatroid.nonspanning_circuits(self) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 632)

        Return the nonspanning circuits of the matroid.

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: M.nonspanning_circuits()
            SetSystem of 0 sets over 4 elements
            sage: M = matroids.Theta(5)
            sage: M.nonspanning_circuits()
            SetSystem of 15 sets over 10 elements"""
    @overload
    def nonspanning_circuits_iterator(self) -> Any:
        """CircuitsMatroid.nonspanning_circuits_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 658)

        Return an iterator over the nonspanning circuits of the matroid.

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: list(M.nonspanning_circuits_iterator())
            []"""
    @overload
    def nonspanning_circuits_iterator(self) -> Any:
        """CircuitsMatroid.nonspanning_circuits_iterator(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 658)

        Return an iterator over the nonspanning circuits of the matroid.

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.Uniform(2, 4))
            sage: list(M.nonspanning_circuits_iterator())
            []"""
    @overload
    def relabel(self, mapping) -> Any:
        """CircuitsMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 400)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.RelaxedNonFano())
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
            sage: N = M.relabel({'g': 'x', 0: 'z'})  # 'g': 'x' is ignored
            sage: from sage.matroids.utilities import cmp_elements_key
            sage: sorted(N.groundset(), key=cmp_elements_key)
            [1, 2, 3, 4, 5, 6, 'z']
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.RelaxedNonFano())
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """CircuitsMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 400)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.RelaxedNonFano())
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
            sage: N = M.relabel({'g': 'x', 0: 'z'})  # 'g': 'x' is ignored
            sage: from sage.matroids.utilities import cmp_elements_key
            sage: sorted(N.groundset(), key=cmp_elements_key)
            [1, 2, 3, 4, 5, 6, 'z']
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.RelaxedNonFano())
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
        """CircuitsMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 311)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: from sage.matroids.circuits_matroid import CircuitsMatroid
            sage: M = CircuitsMatroid(matroids.catalog.Vamos())
            sage: N = CircuitsMatroid(matroids.catalog.Vamos())
            sage: hash(M) == hash(N)
            True
            sage: O = CircuitsMatroid(matroids.catalog.NonVamos())
            sage: hash(M) == hash(O)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """CircuitsMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/circuits_matroid.pyx (starting at line 373)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(E, C, name)`` where ``E`` is
        the groundset, ``C`` is the list of circuits, and ``name`` is a custom
        name.

        EXAMPLES::

            sage: M = matroids.Theta(5)
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.reset_name()
            sage: loads(dumps(M))
            Matroid of rank 5 on 10 elements with 45 circuits"""
