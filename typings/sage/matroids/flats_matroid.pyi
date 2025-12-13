import sage.matroids.matroid
from sage.combinat.posets.lattices import FiniteLatticePoset as FiniteLatticePoset, LatticePoset as LatticePoset
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class FlatsMatroid(sage.matroids.matroid.Matroid):
    """FlatsMatroid(M=None, groundset=None, flats=None)

    File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 40)

    INPUT:

    - ``M`` -- matroid (default: ``None``)
    - ``groundset`` -- list (default: ``None``); the groundset of the matroid
    - ``flats`` -- (default: ``None``) the dictionary of the lists of flats
      (indexed by their rank), or the list of all flats, or the lattice of
      flats of the matroid

    .. NOTE::

        For a more flexible means of input, use the ``Matroid()`` function."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, M=..., groundset=..., flats=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 57)

                Initialization of the matroid. See the class docstring for full
                documentation.

                TESTS::

                    sage: from sage.matroids.flats_matroid import FlatsMatroid
                    sage: M = FlatsMatroid(matroids.catalog.Fano())
                    sage: TestSuite(M).run()
        """
    def flats(self, longk) -> SetSystem:
        """FlatsMatroid.flats(self, long k) -> SetSystem

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 413)

        Return the flats of the matroid of specified rank.

        INPUT:

        - ``k`` -- integer

        OUTPUT: :class:`SetSystem`

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.Uniform(3, 4))
            sage: sorted(M.flats(2), key=str)
            [frozenset({0, 1}),
             frozenset({0, 2}),
             frozenset({0, 3}),
             frozenset({1, 2}),
             frozenset({1, 3}),
             frozenset({2, 3})]"""
    def flats_iterator(self, k) -> Any:
        """FlatsMatroid.flats_iterator(self, k)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 439)

        Return an iterator over the flats of the matroid of specified rank.

        INPUT:

        - ``k`` -- integer

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.Uniform(3, 4))
            sage: sorted([list(F) for F in M.flats_iterator(2)])
            [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]"""
    @overload
    def full_rank(self) -> Any:
        """FlatsMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 161)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.Theta(6))
            sage: M.full_rank()
            6"""
    @overload
    def full_rank(self) -> Any:
        """FlatsMatroid.full_rank(self)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 161)

        Return the rank of the matroid.

        The *rank* of the matroid is the size of the largest independent
        subset of the groundset.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.Theta(6))
            sage: M.full_rank()
            6"""
    @overload
    def groundset(self) -> frozenset:
        """FlatsMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 107)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: :class:`frozenset`

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.Theta(2))
            sage: sorted(M.groundset())
            ['x0', 'x1', 'y0', 'y1']"""
    @overload
    def groundset(self) -> Any:
        """FlatsMatroid.groundset(self) -> frozenset

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 107)

        Return the groundset of the matroid.

        The groundset is the set of elements that comprise the matroid.

        OUTPUT: :class:`frozenset`

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.Theta(2))
            sage: sorted(M.groundset())
            ['x0', 'x1', 'y0', 'y1']"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def is_valid(self, certificate=...) -> Any:
        """FlatsMatroid.is_valid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 543)

        Test if ``self`` obeys the matroid axioms.

        For a matroid defined by its flats, we check the flats axioms.

        If the lattice of flats has already been computed, we instead perform
        the equivalent check of whether it forms a geometric lattice.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``)

        OUTPUT: boolean, or (boolean, dictionary)

        EXAMPLES::

            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0, 1]]}).is_valid()
            True
            sage: Matroid(flats={0: [''], 1: ['a', 'b'], 2: ['ab']}).is_valid()
            True
            sage: M = Matroid(flats={0: [[]], 1: [[0], [1]]})  # missing groundset
            sage: M.is_valid()
            False
            sage: M = Matroid(flats=[[0, 1], [0, 2], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'the intersection of two flats must be a flat',
              'flat 1': frozenset({0, 1}),
              'flat 2': frozenset({0, 2})})
            sage: M = Matroid(flats=[[], [0, 1], [2], [0], [1], [0, 1, 2]])
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({2})})
            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: FlatsMatroid(matroids.catalog.NonVamos()).is_valid()
            True
            sage: Matroid(flats=[[], [0], [1], [0, 1]]).is_valid()
            True
            sage: Matroid(flats=['', 'a', 'b', 'ab']).is_valid()
            True

        If we compute the lattice of flats, the method checks whether the
        lattice of flats is geometric::

            sage: M = Matroid(flats=['',  # missing an extension of flat ['5'] by '6'
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: _ = M.lattice_of_flats()
            sage: M.is_valid(certificate=True)
            (False, {'error': 'the lattice of flats is not geometric'})
            sage: Matroid(matroids.catalog.Fano().lattice_of_flats()).is_valid()
            True

        Some invalid lists of flats are recognized when attempting to construct
        the lattice of flats::

            sage: M = Matroid(flats=[[], [0], [1]])  # missing groundset
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a join-semilattice: no top element
            sage: M = Matroid(flats=[[0], [1], [0, 1]])  # missing an intersection
            sage: M.lattice_of_flats()
            Traceback (most recent call last):
            ...
            ValueError: not a meet-semilattice: no bottom element

        TESTS::

            sage: Matroid(flats={0: [], 1: [[0], [1]], 2: [[0, 1]]}).is_valid(certificate=True)  # missing an intersection
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 1,
              'poset rank': 0})
            sage: Matroid(flats={0: [[]], 2: [[0], [1]], 3: [[0, 1]]}).is_valid(certificate=True)  # invalid ranks
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: Matroid(flats={0: [[]], 1: [[0], [1]], 2: [[0], [0, 1]]}).is_valid(certificate=True)  # duplicates
            (False, {'error': 'flats dictionary has repeated flats'})
            sage: Matroid(flats={0: [[]], 1: [[0], [1], [0, 1]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({0, 1}),
              'given rank': 1,
              'poset rank': 2})
            sage: Matroid(flats={0: [[]], 1: [[0, 1], [2]], 2: [[0], [1], [0, 1, 2]]}).is_valid(certificate=True)
            (False,
             {'error': 'flat of incorrect rank',
              'flat': frozenset({1}),
              'given rank': 2,
              'poset rank': 1})
            sage: M = Matroid(flats={0: [''],  # missing an extension of flat ['5'] by '6'
            ....:                    1: ['0','1','2','3','4','5','6','7','8','9','a','b','c'],
            ....:                    2: ['45','46','47','4c','57','5c','67','6c','7c',
            ....:                        '048','149','24a','34b','059','15a','25b','358',
            ....:                        '06a','16b','268','369','07b','178','279','37a',
            ....:                        '0123c','89abc'],
            ....:                    3: ['0123456789abc']})
            sage: M.is_valid(certificate=True)
            (False,
             {'error': 'a single element extension of a k-flat must be a subset of exactly one (k + 1)-flat',
              'flat': frozenset({'...'})})
            sage: M = Matroid(flats=[[], [0], [1], [0], [0, 1]])  # duplicates are ignored
            sage: M.lattice_of_flats()
            Finite lattice containing 4 elements
            sage: M.is_valid(certificate=True)
            (True, {})
            sage: M = Matroid(flats=['',
            ....:                    '0','1','2','3','4','5','6','7','8','9','a','b','c',
            ....:                    '45','46','47','4c','56','57','5c','67','6c','7c',
            ....:                    '048','149','24a','34b','059','15a','25b','358',
            ....:                    '06a','16b','268','369','07b','178','279','37a',
            ....:                    '0123c','89abc',
            ....:                    '0123456789abc'])
            sage: M.is_valid(certificate=True)
            (True, {})"""
    @overload
    def lattice_of_flats(self) -> Any:
        """FlatsMatroid.lattice_of_flats(self)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 458)

        Return the lattice of flats of the matroid.

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.Fano())
            sage: M.lattice_of_flats()
            Finite lattice containing 16 elements"""
    @overload
    def lattice_of_flats(self) -> Any:
        """FlatsMatroid.lattice_of_flats(self)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 458)

        Return the lattice of flats of the matroid.

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.Fano())
            sage: M.lattice_of_flats()
            Finite lattice containing 16 elements"""
    @overload
    def relabel(self, mapping) -> Any:
        """FlatsMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 365)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.RelaxedNonFano())
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
            sage: N = M.relabel({'g': 'x', 0: 'z'})  # 'g': 'x' is ignored
            sage: from sage.matroids.utilities import cmp_elements_key
            sage: sorted(N.groundset(), key=cmp_elements_key)
            [1, 2, 3, 4, 5, 6, 'z']
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.RelaxedNonFano())
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    @overload
    def relabel(self, f) -> Any:
        """FlatsMatroid.relabel(self, mapping)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 365)

        Return an isomorphic matroid with relabeled groundset.

        The output is obtained by relabeling each element `e` by
        ``mapping[e]``, where ``mapping`` is a given injective map. If
        ``mapping[e]`` is not defined, then the identity map is assumed.

        INPUT:

        - ``mapping`` -- a Python object such that ``mapping[e]`` is the new
          label of `e`

        OUTPUT: matroid

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.RelaxedNonFano())
            sage: sorted(M.groundset())
            [0, 1, 2, 3, 4, 5, 6]
            sage: N = M.relabel({'g': 'x', 0: 'z'})  # 'g': 'x' is ignored
            sage: from sage.matroids.utilities import cmp_elements_key
            sage: sorted(N.groundset(), key=cmp_elements_key)
            [1, 2, 3, 4, 5, 6, 'z']
            sage: M.is_isomorphic(N)
            True

        TESTS::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.RelaxedNonFano())
            sage: f = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g'}
            sage: N = M.relabel(f)
            sage: for S in powerset(M.groundset()):
            ....:     assert M.rank(S) == N.rank([f[x] for x in S])"""
    def whitney_numbers(self) -> list:
        """FlatsMatroid.whitney_numbers(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 473)

        Return the Whitney numbers of the first kind of the matroid.

        The Whitney numbers of the first kind -- here encoded as a vector
        `(w_0=1, \\ldots, w_r)` -- are numbers of alternating sign, where `w_i`
        is the value of the coefficient of the `(r-i)`-th degree term of the
        matroid's characteristic polynomial. Moreover, `|w_i|` is the number of
        `(i-1)`-dimensional faces of the broken circuit complex of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.BetsyRoss())
            sage: M.whitney_numbers()
            [1, -11, 35, -25]

        TESTS::

            sage: M = Matroid(flats=[[0], [0, 1]])
            sage: M.whitney_numbers()
            []"""
    @overload
    def whitney_numbers2(self) -> list:
        """FlatsMatroid.whitney_numbers2(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 512)

        Return the Whitney numbers of the second kind of the matroid.

        The Whitney numbers of the second kind are here encoded as a vector
        `(W_0, ..., W_r)`, where `W_i` is the number of flats of rank `i`, and
        `r` is the rank of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.XY13())
            sage: M.whitney_numbers2()
            [1, 13, 78, 250, 394, 191, 1]

        TESTS::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: for M in matroids.AllMatroids(4):  # optional - matroid_database
            ....:     assert M.whitney_numbers2() == FlatsMatroid(M).whitney_numbers2()"""
    @overload
    def whitney_numbers2(self) -> Any:
        """FlatsMatroid.whitney_numbers2(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 512)

        Return the Whitney numbers of the second kind of the matroid.

        The Whitney numbers of the second kind are here encoded as a vector
        `(W_0, ..., W_r)`, where `W_i` is the number of flats of rank `i`, and
        `r` is the rank of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.XY13())
            sage: M.whitney_numbers2()
            [1, 13, 78, 250, 394, 191, 1]

        TESTS::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: for M in matroids.AllMatroids(4):  # optional - matroid_database
            ....:     assert M.whitney_numbers2() == FlatsMatroid(M).whitney_numbers2()"""
    @overload
    def whitney_numbers2(self) -> Any:
        """FlatsMatroid.whitney_numbers2(self) -> list

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 512)

        Return the Whitney numbers of the second kind of the matroid.

        The Whitney numbers of the second kind are here encoded as a vector
        `(W_0, ..., W_r)`, where `W_i` is the number of flats of rank `i`, and
        `r` is the rank of the matroid.

        OUTPUT: list of integers

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.XY13())
            sage: M.whitney_numbers2()
            [1, 13, 78, 250, 394, 191, 1]

        TESTS::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: for M in matroids.AllMatroids(4):  # optional - matroid_database
            ....:     assert M.whitney_numbers2() == FlatsMatroid(M).whitney_numbers2()"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """FlatsMatroid.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 275)

        Return an invariant of the matroid.

        This function is called when matroids are added to a set. It is very
        desirable to override it so it can distinguish matroids on the same
        groundset, which is a very typical use case!

        .. WARNING::

            This method is linked to ``__richcmp__`` (in Cython) and ``__cmp__``
            or ``__eq__``/``__ne__`` (in Python). If you override one, you
            should (and, in Cython, \\emph{must}) override the other!

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.Vamos())
            sage: N = FlatsMatroid(matroids.catalog.Vamos())
            sage: hash(M) == hash(N)
            True
            sage: O = FlatsMatroid(matroids.catalog.NonVamos())
            sage: hash(M) == hash(O)
            False"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """FlatsMatroid.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/flats_matroid.pyx (starting at line 337)

        Save the matroid for later reloading.

        OUTPUT:

        A tuple ``(unpickle, (version, data))``, where ``unpickle`` is the
        name of a function that, when called with ``(version, data)``,
        produces a matroid isomorphic to ``self``. ``version`` is an integer
        (currently 0) and ``data`` is a tuple ``(E, F, name)`` where ``E`` is
        the groundset, ``F`` is the dictionary of flats, and ``name`` is a
        custom name.

        EXAMPLES::

            sage: from sage.matroids.flats_matroid import FlatsMatroid
            sage: M = FlatsMatroid(matroids.catalog.Vamos())
            sage: M == loads(dumps(M))  # indirect doctest
            True
            sage: M.reset_name()
            sage: loads(dumps(M))
            Matroid of rank 4 on 8 elements with 79 flats"""
