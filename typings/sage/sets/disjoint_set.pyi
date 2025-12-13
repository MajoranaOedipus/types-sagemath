import _cython_3_2_1
import sage.structure.sage_object
from sage.combinat.set_partition import SetPartition as SetPartition
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

DisjointSet: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict

class DisjointSet_class(sage.structure.sage_object.SageObject):
    """File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 157)

        Common class and methods for :class:`DisjointSet_of_integers` and
        :class:`DisjointSet_of_hashables`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def cardinality(self) -> Any:
        """DisjointSet_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 300)

        Return the number of elements in ``self``, *not* the number of subsets.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5
            sage: d = DisjointSet(range(5))
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5"""
    @overload
    def cardinality(self) -> Any:
        """DisjointSet_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 300)

        Return the number of elements in ``self``, *not* the number of subsets.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5
            sage: d = DisjointSet(range(5))
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5"""
    @overload
    def cardinality(self) -> Any:
        """DisjointSet_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 300)

        Return the number of elements in ``self``, *not* the number of subsets.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5
            sage: d = DisjointSet(range(5))
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5"""
    @overload
    def cardinality(self) -> Any:
        """DisjointSet_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 300)

        Return the number of elements in ``self``, *not* the number of subsets.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5
            sage: d = DisjointSet(range(5))
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5"""
    @overload
    def cardinality(self) -> Any:
        """DisjointSet_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 300)

        Return the number of elements in ``self``, *not* the number of subsets.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5
            sage: d = DisjointSet(range(5))
            sage: d.cardinality()
            5
            sage: d.union(2, 4)
            sage: d.cardinality()
            5"""
    @overload
    def number_of_subsets(self) -> Any:
        """DisjointSet_class.number_of_subsets(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 321)

        Return the number of subsets in ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4
            sage: d = DisjointSet(range(5))
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4"""
    @overload
    def number_of_subsets(self) -> Any:
        """DisjointSet_class.number_of_subsets(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 321)

        Return the number of subsets in ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4
            sage: d = DisjointSet(range(5))
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4"""
    @overload
    def number_of_subsets(self) -> Any:
        """DisjointSet_class.number_of_subsets(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 321)

        Return the number of subsets in ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4
            sage: d = DisjointSet(range(5))
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4"""
    @overload
    def number_of_subsets(self) -> Any:
        """DisjointSet_class.number_of_subsets(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 321)

        Return the number of subsets in ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4
            sage: d = DisjointSet(range(5))
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4"""
    @overload
    def number_of_subsets(self) -> Any:
        """DisjointSet_class.number_of_subsets(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 321)

        Return the number of subsets in ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4
            sage: d = DisjointSet(range(5))
            sage: d.number_of_subsets()
            5
            sage: d.union(2, 4)
            sage: d.number_of_subsets()
            4"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __iter__(self) -> Any:
        """DisjointSet_class.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 195)

        Iterate over elements of the set.

        EXAMPLES::

            sage: d = DisjointSet(4)
            sage: d.union(2, 0)
            sage: sorted(d)
            [[0, 2], [1], [3]]
            sage: d = DisjointSet('abc')
            sage: sorted(d)
            [['a'], ['b'], ['c']]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    @overload
    def __reduce__(self) -> Any:
        """DisjointSet_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 277)

        Return a tuple of three elements:

        - The function :func:`DisjointSet`
        - Arguments for the function :func:`DisjointSet`
        - The actual state of ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>, (5,), [0, 1, 2, 3, 4])

        ::

            sage: d.union(2, 4)
            sage: d.union(1, 3)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>, (5,), [0, 1, 2, 1, 2])"""
    @overload
    def __reduce__(self) -> Any:
        """DisjointSet_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 277)

        Return a tuple of three elements:

        - The function :func:`DisjointSet`
        - Arguments for the function :func:`DisjointSet`
        - The actual state of ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>, (5,), [0, 1, 2, 3, 4])

        ::

            sage: d.union(2, 4)
            sage: d.union(1, 3)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>, (5,), [0, 1, 2, 1, 2])"""
    @overload
    def __reduce__(self) -> Any:
        """DisjointSet_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 277)

        Return a tuple of three elements:

        - The function :func:`DisjointSet`
        - Arguments for the function :func:`DisjointSet`
        - The actual state of ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>, (5,), [0, 1, 2, 3, 4])

        ::

            sage: d.union(2, 4)
            sage: d.union(1, 3)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>, (5,), [0, 1, 2, 1, 2])"""

class DisjointSet_of_hashables(DisjointSet_class):
    """DisjointSet_of_hashables(iterable)

    File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 665)

    Disjoint set of hashables.

    EXAMPLES::

        sage: d = DisjointSet('abcde')
        sage: d
        {{'a'}, {'b'}, {'c'}, {'d'}, {'e'}}
        sage: d.union('a', 'c')
        sage: d
        {{'a', 'c'}, {'b'}, {'d'}, {'e'}}
        sage: d.find('a')
        'a'

    TESTS::

        sage: a = DisjointSet('abcdef')
        sage: a == loads(dumps(a))
        True

    ::

        sage: a.union('a', 'c')
        sage: a == loads(dumps(a))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, iterable) -> Any:
        """File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 692)

                Construct the trivial disjoint set where each element is in its own set.

                INPUT:

                - ``iterable`` -- iterable of hashable objects

                EXAMPLES::

                    sage: DisjointSet('abcde')
                    {{'a'}, {'b'}, {'c'}, {'d'}, {'e'}}
                    sage: DisjointSet(range(6))
                    {{0}, {1}, {2}, {3}, {4}, {5}}
                    sage: DisjointSet(['yi', 45, 'cheval'])
                    {{'cheval'}, {'yi'}, {45}}
                    sage: DisjointSet(set([0, 1, 2, 3, 4]))
                    {{0}, {1}, {2}, {3}, {4}}
        """
    @overload
    def element_to_root_dict(self) -> Any:
        """DisjointSet_of_hashables.element_to_root_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 939)

        Return the dictionary where the keys are the elements of ``self`` and
        the values are their representative inside a list.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: e = d.element_to_root_dict()
            sage: sorted(e.items())
            [(0, 0), (1, 4), (2, 2), (3, 2), (4, 4)]
            sage: WordMorphism(e)                                                       # needs sage.combinat
            WordMorphism: 0->0, 1->4, 2->2, 3->2, 4->4"""
    @overload
    def element_to_root_dict(self) -> Any:
        """DisjointSet_of_hashables.element_to_root_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 939)

        Return the dictionary where the keys are the elements of ``self`` and
        the values are their representative inside a list.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: e = d.element_to_root_dict()
            sage: sorted(e.items())
            [(0, 0), (1, 4), (2, 2), (3, 2), (4, 4)]
            sage: WordMorphism(e)                                                       # needs sage.combinat
            WordMorphism: 0->0, 1->4, 2->2, 3->2, 4->4"""
    @overload
    def find(self, e) -> Any:
        """DisjointSet_of_hashables.find(self, e)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 805)

        Return the representative of the set that ``e`` currently belongs to.

        INPUT:

        - ``e`` -- element in ``self``

        EXAMPLES::

            sage: e = DisjointSet(range(5))
            sage: e.union(4, 2)
            sage: e
            {{0}, {1}, {2, 4}, {3}}
            sage: e.find(2)
            4
            sage: e.find(4)
            4
            sage: e.union(1,3)
            sage: e
            {{0}, {1, 3}, {2, 4}}
            sage: e.find(1)
            1
            sage: e.find(3)
            1
            sage: e.union(3, 2)
            sage: e
            {{0}, {1, 2, 3, 4}}
            sage: [e.find(i) for i in range(5)]
            [0, 1, 1, 1, 1]
            sage: e.find(5)
            Traceback (most recent call last):
            ...
            KeyError: 5"""
    @overload
    def find(self, i) -> Any:
        """DisjointSet_of_hashables.find(self, e)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 805)

        Return the representative of the set that ``e`` currently belongs to.

        INPUT:

        - ``e`` -- element in ``self``

        EXAMPLES::

            sage: e = DisjointSet(range(5))
            sage: e.union(4, 2)
            sage: e
            {{0}, {1}, {2, 4}, {3}}
            sage: e.find(2)
            4
            sage: e.find(4)
            4
            sage: e.union(1,3)
            sage: e
            {{0}, {1, 3}, {2, 4}}
            sage: e.find(1)
            1
            sage: e.find(3)
            1
            sage: e.union(3, 2)
            sage: e
            {{0}, {1, 2, 3, 4}}
            sage: [e.find(i) for i in range(5)]
            [0, 1, 1, 1, 1]
            sage: e.find(5)
            Traceback (most recent call last):
            ...
            KeyError: 5"""
    @overload
    def make_set(self, new_elt=...) -> Any:
        """DisjointSet_of_hashables.make_set(self, new_elt=None)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 880)

        Add a new element into a new set containing only the new element.

        According to :wikipedia:`Disjoint-set_data_structure#Making_new_sets`
        the ``make_set`` operation adds a new element into a new set containing
        only the new element. The new set is added at the end of ``self``.

        INPUT:

        - ``new_elt`` -- (optional) element to add. If `None`, then an integer
          is added.

        EXAMPLES::

            sage: e = DisjointSet('abcde')
            sage: e.union('d', 'c')
            sage: e.union('c', 'e')
            sage: e.make_set('f')
            sage: e
            {{'a'}, {'b'}, {'c', 'd', 'e'}, {'f'}}
            sage: e.union('f', 'b')
            sage: e
            {{'a'}, {'b', 'f'}, {'c', 'd', 'e'}}
            sage: e.make_set('e'); e
            {{'a'}, {'b', 'f'}, {'c', 'd', 'e'}}
            sage: e.make_set(); e
            {{'a'}, {'b', 'f'}, {'c', 'd', 'e'}, {6}}"""
    @overload
    def make_set(self) -> Any:
        """DisjointSet_of_hashables.make_set(self, new_elt=None)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 880)

        Add a new element into a new set containing only the new element.

        According to :wikipedia:`Disjoint-set_data_structure#Making_new_sets`
        the ``make_set`` operation adds a new element into a new set containing
        only the new element. The new set is added at the end of ``self``.

        INPUT:

        - ``new_elt`` -- (optional) element to add. If `None`, then an integer
          is added.

        EXAMPLES::

            sage: e = DisjointSet('abcde')
            sage: e.union('d', 'c')
            sage: e.union('c', 'e')
            sage: e.make_set('f')
            sage: e
            {{'a'}, {'b'}, {'c', 'd', 'e'}, {'f'}}
            sage: e.union('f', 'b')
            sage: e
            {{'a'}, {'b', 'f'}, {'c', 'd', 'e'}}
            sage: e.make_set('e'); e
            {{'a'}, {'b', 'f'}, {'c', 'd', 'e'}}
            sage: e.make_set(); e
            {{'a'}, {'b', 'f'}, {'c', 'd', 'e'}, {6}}"""
    @overload
    def root_to_elements_dict(self) -> Any:
        """DisjointSet_of_hashables.root_to_elements_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 917)

        Return the dictionary where the keys are the roots of ``self`` and the
        values are the elements in the same set.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: e = d.root_to_elements_dict()
            sage: sorted(e.items())
            [(0, [0]), (2, [2, 3]), (4, [1, 4])]"""
    @overload
    def root_to_elements_dict(self) -> Any:
        """DisjointSet_of_hashables.root_to_elements_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 917)

        Return the dictionary where the keys are the roots of ``self`` and the
        values are the elements in the same set.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: e = d.root_to_elements_dict()
            sage: sorted(e.items())
            [(0, [0]), (2, [2, 3]), (4, [1, 4])]"""
    @overload
    def to_digraph(self) -> Any:
        """DisjointSet_of_hashables.to_digraph(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 960)

        Return the current digraph of ``self`` where `(a, b)` is an oriented
        edge if `b` is the parent of `a`.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: d.union(3, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: g = d.to_digraph()
            sage: g                                                                     # needs sage.graphs
            Looped digraph on 5 vertices
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, None), (1, 2, None), (2, 2, None), (3, 2, None), (4, 2, None)]

        The result depends on the ordering of the union::

            sage: d = DisjointSet(range(5))
            sage: d.union(1, 2)
            sage: d.union(1, 3)
            sage: d.union(1, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: d.to_digraph().edges(sort=True)                                       # needs sage.graphs
            [(0, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (4, 1, None)]"""
    @overload
    def to_digraph(self) -> Any:
        """DisjointSet_of_hashables.to_digraph(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 960)

        Return the current digraph of ``self`` where `(a, b)` is an oriented
        edge if `b` is the parent of `a`.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: d.union(3, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: g = d.to_digraph()
            sage: g                                                                     # needs sage.graphs
            Looped digraph on 5 vertices
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, None), (1, 2, None), (2, 2, None), (3, 2, None), (4, 2, None)]

        The result depends on the ordering of the union::

            sage: d = DisjointSet(range(5))
            sage: d.union(1, 2)
            sage: d.union(1, 3)
            sage: d.union(1, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: d.to_digraph().edges(sort=True)                                       # needs sage.graphs
            [(0, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (4, 1, None)]"""
    @overload
    def to_digraph(self) -> Any:
        """DisjointSet_of_hashables.to_digraph(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 960)

        Return the current digraph of ``self`` where `(a, b)` is an oriented
        edge if `b` is the parent of `a`.

        EXAMPLES::

            sage: d = DisjointSet(range(5))
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: d.union(3, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: g = d.to_digraph()
            sage: g                                                                     # needs sage.graphs
            Looped digraph on 5 vertices
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, None), (1, 2, None), (2, 2, None), (3, 2, None), (4, 2, None)]

        The result depends on the ordering of the union::

            sage: d = DisjointSet(range(5))
            sage: d.union(1, 2)
            sage: d.union(1, 3)
            sage: d.union(1, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: d.to_digraph().edges(sort=True)                                       # needs sage.graphs
            [(0, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (4, 1, None)]"""
    def union(self, e, f) -> void:
        """DisjointSet_of_hashables.union(self, e, f) -> void

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 844)

        Combine the set of ``e`` and the set of ``f`` into one.

        All elements in those two sets will share the same representative
        that can be retrieved using
        :meth:`~sage.sets.disjoint_set.DisjointSet_of_hashables.find`.

        INPUT:

        - ``e`` -- element in ``self``
        - ``f`` -- element in ``self``

        EXAMPLES::

            sage: e = DisjointSet('abcde')
            sage: e
            {{'a'}, {'b'}, {'c'}, {'d'}, {'e'}}
            sage: e.union('a', 'b')
            sage: e
            {{'a', 'b'}, {'c'}, {'d'}, {'e'}}
            sage: e.union('c', 'e')
            sage: e
            {{'a', 'b'}, {'c', 'e'}, {'d'}}
            sage: e.union('b', 'e')
            sage: e
            {{'a', 'b', 'c', 'e'}, {'d'}}
            sage: e.union('a', 2**10)
            Traceback (most recent call last):
            ...
            KeyError: 1024"""
    def __reduce__(self):
        """DisjointSet_of_hashables.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 719)

        Return a tuple of three elements:

        - The function :func:`DisjointSet`
        - Arguments for the function :func:`DisjointSet`
        - The actual state of ``self``.

        EXAMPLES::

            sage: DisjointSet(range(5))
            {{0}, {1}, {2}, {3}, {4}}
            sage: d = _
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>,
             ([0, 1, 2, 3, 4],),
             [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

         ::

            sage: d.union(2, 4)
            sage: d.union(1, 3)
            sage: d.__reduce__()
            (<cyfunction DisjointSet at ...>,
             ([0, 1, 2, 3, 4],),
             [(0, 0), (1, 1), (2, 2), (3, 1), (4, 2)])"""

class DisjointSet_of_integers(DisjointSet_class):
    """DisjointSet_of_integers(n)

    File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 342)

    Disjoint set of integers from ``0`` to ``n-1``.

    EXAMPLES::

        sage: d = DisjointSet(5)
        sage: d
        {{0}, {1}, {2}, {3}, {4}}
        sage: d.union(2, 4)
        sage: d.union(0, 2)
        sage: d
        {{0, 2, 4}, {1}, {3}}
        sage: d.find(2)
        2

    TESTS::

        sage: a = DisjointSet(5)
        sage: a == loads(dumps(a))
        True

    ::

        sage: a.union(3, 4)
        sage: a == loads(dumps(a))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, n) -> Any:
        """File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 370)

                Construct the ``DisjointSet`` where each element (integers from ``0``
                to ``n-1``) is in its own set.

                INPUT:

                - ``n`` -- nonnegative integer

                EXAMPLES::

                    sage: DisjointSet(6)
                    {{0}, {1}, {2}, {3}, {4}, {5}}
                    sage: DisjointSet(1)
                    {{0}}
                    sage: DisjointSet(0)
                    {}
        """
    @overload
    def element_to_root_dict(self) -> Any:
        """DisjointSet_of_integers.element_to_root_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 610)

        Return the dictionary where the keys are the elements of ``self`` and
        the values are their representative inside a list.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: e = d.element_to_root_dict()
            sage: e
            {0: 0, 1: 4, 2: 2, 3: 2, 4: 4}
            sage: WordMorphism(e)                                                       # needs sage.combinat
            WordMorphism: 0->0, 1->4, 2->2, 3->2, 4->4"""
    @overload
    def element_to_root_dict(self) -> Any:
        """DisjointSet_of_integers.element_to_root_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 610)

        Return the dictionary where the keys are the elements of ``self`` and
        the values are their representative inside a list.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: e = d.element_to_root_dict()
            sage: e
            {0: 0, 1: 4, 2: 2, 3: 2, 4: 4}
            sage: WordMorphism(e)                                                       # needs sage.combinat
            WordMorphism: 0->0, 1->4, 2->2, 3->2, 4->4"""
    @overload
    def find(self, inti) -> int:
        """DisjointSet_of_integers.find(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 465)

        Return the representative of the set that ``i`` currently belongs to.

        INPUT:

        - ``i`` -- element in ``self``

        EXAMPLES::

            sage: e = DisjointSet(5)
            sage: e.union(4, 2)
            sage: e
            {{0}, {1}, {2, 4}, {3}}
            sage: e.find(2)
            4
            sage: e.find(4)
            4
            sage: e.union(1, 3)
            sage: e
            {{0}, {1, 3}, {2, 4}}
            sage: e.find(1)
            1
            sage: e.find(3)
            1
            sage: e.union(3, 2)
            sage: e
            {{0}, {1, 2, 3, 4}}
            sage: [e.find(i) for i in range(5)]
            [0, 1, 1, 1, 1]
            sage: e.find(2**10)
            Traceback (most recent call last):
            ...
            ValueError: i must be between 0 and 4 (1024 given)

        .. NOTE::

            This method performs input checks. To avoid them you may directly
            use :meth:`~sage.groups.perm_gps.partn_ref.data_structures.OP_find`."""
    @overload
    def find(self, i) -> Any:
        """DisjointSet_of_integers.find(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 465)

        Return the representative of the set that ``i`` currently belongs to.

        INPUT:

        - ``i`` -- element in ``self``

        EXAMPLES::

            sage: e = DisjointSet(5)
            sage: e.union(4, 2)
            sage: e
            {{0}, {1}, {2, 4}, {3}}
            sage: e.find(2)
            4
            sage: e.find(4)
            4
            sage: e.union(1, 3)
            sage: e
            {{0}, {1, 3}, {2, 4}}
            sage: e.find(1)
            1
            sage: e.find(3)
            1
            sage: e.union(3, 2)
            sage: e
            {{0}, {1, 2, 3, 4}}
            sage: [e.find(i) for i in range(5)]
            [0, 1, 1, 1, 1]
            sage: e.find(2**10)
            Traceback (most recent call last):
            ...
            ValueError: i must be between 0 and 4 (1024 given)

        .. NOTE::

            This method performs input checks. To avoid them you may directly
            use :meth:`~sage.groups.perm_gps.partn_ref.data_structures.OP_find`."""
    @overload
    def make_set(self) -> Any:
        """DisjointSet_of_integers.make_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 554)

        Add a new element into a new set containing only the new element.

        According to :wikipedia:`Disjoint-set_data_structure#Making_new_sets` the
        ``make_set`` operation adds a new element into a new set containing only
        the new element. The new set is added at the end of ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(1, 2)
            sage: d.union(0, 1)
            sage: d.make_set()
            sage: d
            {{0, 1, 2}, {3}, {4}, {5}}
            sage: d.find(1)
            1

        TESTS::

            sage: d = DisjointSet(0)
            sage: d.make_set()
            sage: d
            {{0}}"""
    @overload
    def make_set(self) -> Any:
        """DisjointSet_of_integers.make_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 554)

        Add a new element into a new set containing only the new element.

        According to :wikipedia:`Disjoint-set_data_structure#Making_new_sets` the
        ``make_set`` operation adds a new element into a new set containing only
        the new element. The new set is added at the end of ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(1, 2)
            sage: d.union(0, 1)
            sage: d.make_set()
            sage: d
            {{0, 1, 2}, {3}, {4}, {5}}
            sage: d.find(1)
            1

        TESTS::

            sage: d = DisjointSet(0)
            sage: d.make_set()
            sage: d
            {{0}}"""
    @overload
    def make_set(self) -> Any:
        """DisjointSet_of_integers.make_set(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 554)

        Add a new element into a new set containing only the new element.

        According to :wikipedia:`Disjoint-set_data_structure#Making_new_sets` the
        ``make_set`` operation adds a new element into a new set containing only
        the new element. The new set is added at the end of ``self``.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(1, 2)
            sage: d.union(0, 1)
            sage: d.make_set()
            sage: d
            {{0, 1, 2}, {3}, {4}, {5}}
            sage: d.find(1)
            1

        TESTS::

            sage: d = DisjointSet(0)
            sage: d.make_set()
            sage: d
            {{0}}"""
    @overload
    def root_to_elements_dict(self) -> Any:
        """DisjointSet_of_integers.root_to_elements_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 582)

        Return the dictionary where the keys are the roots of ``self`` and the
        values are the elements in the same set as the root.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4])]
            sage: d.union(2, 3)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2, 3]), (4, [4])]
            sage: d.union(3, 0)
            sage: sorted(d.root_to_elements_dict().items())
            [(1, [1]), (2, [0, 2, 3]), (4, [4])]
            sage: d
            {{0, 2, 3}, {1}, {4}}"""
    @overload
    def root_to_elements_dict(self) -> Any:
        """DisjointSet_of_integers.root_to_elements_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 582)

        Return the dictionary where the keys are the roots of ``self`` and the
        values are the elements in the same set as the root.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4])]
            sage: d.union(2, 3)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2, 3]), (4, [4])]
            sage: d.union(3, 0)
            sage: sorted(d.root_to_elements_dict().items())
            [(1, [1]), (2, [0, 2, 3]), (4, [4])]
            sage: d
            {{0, 2, 3}, {1}, {4}}"""
    @overload
    def root_to_elements_dict(self) -> Any:
        """DisjointSet_of_integers.root_to_elements_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 582)

        Return the dictionary where the keys are the roots of ``self`` and the
        values are the elements in the same set as the root.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4])]
            sage: d.union(2, 3)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2, 3]), (4, [4])]
            sage: d.union(3, 0)
            sage: sorted(d.root_to_elements_dict().items())
            [(1, [1]), (2, [0, 2, 3]), (4, [4])]
            sage: d
            {{0, 2, 3}, {1}, {4}}"""
    @overload
    def root_to_elements_dict(self) -> Any:
        """DisjointSet_of_integers.root_to_elements_dict(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 582)

        Return the dictionary where the keys are the roots of ``self`` and the
        values are the elements in the same set as the root.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2]), (3, [3]), (4, [4])]
            sage: d.union(2, 3)
            sage: sorted(d.root_to_elements_dict().items())
            [(0, [0]), (1, [1]), (2, [2, 3]), (4, [4])]
            sage: d.union(3, 0)
            sage: sorted(d.root_to_elements_dict().items())
            [(1, [1]), (2, [0, 2, 3]), (4, [4])]
            sage: d
            {{0, 2, 3}, {1}, {4}}"""
    @overload
    def to_digraph(self) -> Any:
        """DisjointSet_of_integers.to_digraph(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 632)

        Return the current digraph of ``self`` where `(a, b)` is an oriented
        edge if `b` is the parent of `a`.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: d.union(3, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: g = d.to_digraph(); g                                                 # needs sage.graphs
            Looped digraph on 5 vertices
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, None), (1, 2, None), (2, 2, None), (3, 2, None), (4, 2, None)]

        The result depends on the ordering of the union::

            sage: d = DisjointSet(5)
            sage: d.union(1, 2)
            sage: d.union(1, 3)
            sage: d.union(1, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: d.to_digraph().edges(sort=True)                                       # needs sage.graphs
            [(0, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (4, 1, None)]"""
    @overload
    def to_digraph(self) -> Any:
        """DisjointSet_of_integers.to_digraph(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 632)

        Return the current digraph of ``self`` where `(a, b)` is an oriented
        edge if `b` is the parent of `a`.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: d.union(3, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: g = d.to_digraph(); g                                                 # needs sage.graphs
            Looped digraph on 5 vertices
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, None), (1, 2, None), (2, 2, None), (3, 2, None), (4, 2, None)]

        The result depends on the ordering of the union::

            sage: d = DisjointSet(5)
            sage: d.union(1, 2)
            sage: d.union(1, 3)
            sage: d.union(1, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: d.to_digraph().edges(sort=True)                                       # needs sage.graphs
            [(0, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (4, 1, None)]"""
    @overload
    def to_digraph(self) -> Any:
        """DisjointSet_of_integers.to_digraph(self)

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 632)

        Return the current digraph of ``self`` where `(a, b)` is an oriented
        edge if `b` is the parent of `a`.

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d.union(2, 3)
            sage: d.union(4, 1)
            sage: d.union(3, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: g = d.to_digraph(); g                                                 # needs sage.graphs
            Looped digraph on 5 vertices
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 0, None), (1, 2, None), (2, 2, None), (3, 2, None), (4, 2, None)]

        The result depends on the ordering of the union::

            sage: d = DisjointSet(5)
            sage: d.union(1, 2)
            sage: d.union(1, 3)
            sage: d.union(1, 4)
            sage: d
            {{0}, {1, 2, 3, 4}}
            sage: d.to_digraph().edges(sort=True)                                       # needs sage.graphs
            [(0, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (4, 1, None)]"""
    def union(self, inti, intj) -> void:
        """DisjointSet_of_integers.union(self, int i, int j) -> void

        File: /build/sagemath/src/sage/src/sage/sets/disjoint_set.pyx (starting at line 510)

        Combine the set of ``i`` and the set of ``j`` into one.

        All elements in those two sets will share the same representative
        that can be retrieved using
        :meth:`~sage.sets.disjoint_set.DisjointSet_of_integers.find`.

        INPUT:

        - ``i`` -- element in ``self``
        - ``j`` -- element in ``self``

        EXAMPLES::

            sage: d = DisjointSet(5)
            sage: d
            {{0}, {1}, {2}, {3}, {4}}
            sage: d.union(0, 1)
            sage: d
            {{0, 1}, {2}, {3}, {4}}
            sage: d.union(2, 4)
            sage: d
            {{0, 1}, {2, 4}, {3}}
            sage: d.union(1, 4)
            sage: d
            {{0, 1, 2, 4}, {3}}
            sage: d.union(1, 5)
            Traceback (most recent call last):
            ...
            ValueError: j must be between 0 and 4 (5 given)

        .. NOTE::

            This method performs input checks. To avoid them you may directly
            use :meth:`~sage.groups.perm_gps.partn_ref.data_structures.OP_join`."""
