from typing import Any, ClassVar, overload

class MonoDict:
    '''MonoDict(data=None, weak_values=False, *)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 252)

     This is a hashtable specifically designed for (read) speed in
     the coercion model.

     It differs from a python WeakKeyDictionary in the following important ways:

        - Comparison is done using the \'is\' rather than \'==\' operator.
        - Only weak references to the keys are stored if at all possible.
          Keys that do not allow for weak references are stored with a normal
          refcounted reference.
        - The callback of the weak references is safe against recursion, see below.

     There are special cdef set/get methods for faster access.
     It is bare-bones in the sense that not all dictionary methods are
     implemented.

     IMPLEMENTATION:

     It is implemented as a hash table with open addressing, similar to python\'s
     dict.

     INPUT:

     - ``data`` -- (optional) iterable defining initial data, as dict or
       iterable of (key, value) pairs

     - ``weak_values`` -- boolean (default: ``False``); if it is
       ``True``, weak references to the values in this dictionary will be used,
       when possible

     EXAMPLES::

         sage: from sage.structure.coerce_dict import MonoDict
         sage: L = MonoDict()
         sage: a = \'a\'; b = \'ab\'; c = \'-15\'
         sage: L[a] = 1
         sage: L[b] = 2
         sage: L[c] = 3

     The key is expected to be a unique object. Hence, the item stored for ``c``
     cannot be obtained by providing another equal string::

         sage: L[a]
         1
         sage: L[b]
         2
         sage: L[c]
         3
         sage: L[\'-15\']
         Traceback (most recent call last):
         ...
         KeyError: \'-15\'

     Not all features of Python dictionaries are available, but iteration over
     the dictionary items is possible::

         sage: sorted(L.items())
         [(\'-15\', 3), (\'a\', 1), (\'ab\', 2)]
         sage: del L[c]
         sage: sorted(L.items())
         [(\'a\', 1), (\'ab\', 2)]
         sage: len(L)
         2
         sage: for i in range(1000):
         ....:     L[i] = i
         sage: len(L)
         1002
         sage: L[\'a\']
         1
         sage: L[\'c\']
         Traceback (most recent call last):
         ...
         KeyError: \'c\'

     TESTS:

     Here, we demonstrate the use of weak values::

         sage: M = MonoDict()
         sage: MW = MonoDict(weak_values=True)
         sage: class Foo: pass
         sage: a = Foo()
         sage: b = Foo()
         sage: k = 1
         sage: M[k] = a
         sage: MW[k] = b
         sage: M[k] is a
         True
         sage: MW[k] is b
         True
         sage: k in M
         True
         sage: k in MW
         True

     While ``M`` uses a strong reference to ``a``, ``MW`` uses a *weak*
     reference to ``b``, and after deleting ``b``, the corresponding item of
     ``MW`` will be removed during the next garbage collection::

         sage: import gc
         sage: del a,b
         sage: _ = gc.collect()
         sage: k in M
         True
         sage: k in MW
         False
         sage: len(MW)
         0
         sage: len(M)
         1

    Note that ``MW`` also accepts values that do not allow for weak references::

         sage: MW[k] = int(5)
         sage: MW[k]
         5

     The following demonstrates that :class:`MonoDict` is safer than
     :class:`~weakref.WeakKeyDictionary` against recursions created by nested
     callbacks; compare :issue:`15069` (the mechanism used now is different, though)::

         sage: M = MonoDict()
         sage: class A: pass
         sage: a = A()
         sage: prev = a
         sage: for i in range(1000):
         ....:     newA = A()
         ....:     M[prev] = newA
         ....:     prev = newA
         sage: len(M)
         1000
         sage: del a
         sage: len(M)
         0

     The corresponding example with a Python :class:`weakref.WeakKeyDictionary`
     would result in a too deep recursion during deletion of the dictionary
     items::

         sage: import weakref
         sage: M = weakref.WeakKeyDictionary()
         sage: a = A()
         sage: prev = a
         sage: for i in range(1000):
         ....:     newA = A()
         ....:     M[prev] = newA
         ....:     prev = newA
         sage: len(M)
         1000

     Check that also in the presence of circular references, :class:`MonoDict`
     gets properly collected::

         sage: import gc
         sage: def count_type(T):
         ....:     return len([c for c in gc.get_objects() if isinstance(c,T)])
         sage: gc.freeze()  # so that gc.collect() only deals with our trash
         sage: N = count_type(MonoDict)
         sage: for i in range(100):
         ....:     V = [MonoDict({"id":j+100*i}) for j in range(100)]
         ....:     n = len(V)
         ....:     for i in range(n): V[i][V[(i+1)%n]] = (i+1)%n
         ....:     del V
         ....:     _ = gc.collect()
         ....:     assert count_type(MonoDict) == N
         sage: count_type(MonoDict) == N
         True
         sage: gc.unfreeze()

     AUTHORS:

     - Simon King (2012-01)
     - Nils Bruin (2012-08)
     - Simon King (2013-02)
     - Nils Bruin (2013-11)
 '''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 540)

                Create a special dict using singletons for keys.

                EXAMPLES::

                    sage: from sage.structure.coerce_dict import MonoDict
                    sage: L = MonoDict()
                    sage: a = 'a'
                    sage: L[a] = 1
                    sage: L[a]
                    1
                    sage: L = MonoDict({a: 1})
                    sage: L[a]
                    1
                    sage: L = MonoDict([(a, 1)])
                    sage: L[a]
                    1
        """
    @overload
    def copy(self) -> Any:
        """MonoDict.copy(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 810)

        Return a copy of this :class:`MonoDict` as Python dict.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: L[1] = 42
            sage: L.copy()
            {1: 42}"""
    @overload
    def copy(self) -> Any:
        """MonoDict.copy(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 810)

        Return a copy of this :class:`MonoDict` as Python dict.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: L[1] = 42
            sage: L.copy()
            {1: 42}"""
    @overload
    def items(self) -> Any:
        """MonoDict.items(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 769)

        Iterate over the ``(key, value)`` pairs of this :class:`MonoDict`.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: L[1] = None
            sage: L[2] = True
            sage: L.items()
            <...generator object at ...>
            sage: sorted(L.items())
            [(1, None), (2, True)]"""
    @overload
    def items(self) -> Any:
        """MonoDict.items(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 769)

        Iterate over the ``(key, value)`` pairs of this :class:`MonoDict`.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: L[1] = None
            sage: L[2] = True
            sage: L.items()
            <...generator object at ...>
            sage: sorted(L.items())
            [(1, None), (2, True)]"""
    @overload
    def items(self) -> Any:
        """MonoDict.items(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 769)

        Iterate over the ``(key, value)`` pairs of this :class:`MonoDict`.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: L[1] = None
            sage: L[2] = True
            sage: L.items()
            <...generator object at ...>
            sage: sorted(L.items())
            [(1, None), (2, True)]"""
    def __contains__(self, k) -> Any:
        """MonoDict.__contains__(self, k)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 589)

        Test if the dictionary contains a given key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: a = 'a'; b = 'ab'; c = 15
            sage: L[a] = 1
            sage: L[b] = 2
            sage: L[c] = 3
            sage: c in L         # indirect doctest
            True

        The keys are compared by identity, not by equality. Hence, we have::

            sage: c == 15
            True
            sage: 15 in L
            False"""
    def __delitem__(self, k) -> Any:
        """MonoDict.__delitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 735)

        Delete the value corresponding to a key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: a = 15
            sage: L[a] = -1
            sage: len(L)
            1

        Note that the keys are unique, hence using a key that is equal but not
        identical to a results in an error::

            sage: del L[15]
            Traceback (most recent call last):
            ...
            KeyError: 15
            sage: a in L
            True
            sage: del L[a]
            sage: len(L)
            0
            sage: a in L
            False"""
    def __getitem__(self, k) -> Any:
        """MonoDict.__getitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 619)

        Get the value corresponding to a key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: a = 'a'; b = 'b'; c = 15
            sage: L[a] = 1
            sage: L[b] = 2
            sage: L[c] = 3
            sage: L[c]                  # indirect doctest
            3

        Note that the keys are supposed to be unique::

            sage: c == 15
            True
            sage: c is 15
            False
            sage: L[15]
            Traceback (most recent call last):
            ...
            KeyError: 15"""
    def __len__(self) -> Any:
        """MonoDict.__len__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 572)

        The number of items in ``self``.
        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: a = 'a'; b = 'b'; c = 'c'
            sage: L[a] = 1
            sage: L[a] = -1 # re-assign
            sage: L[b] = 1
            sage: L[c] = None
            sage: len(L)
            3"""
    def __reduce__(self) -> Any:
        """MonoDict.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 824)

        Note that we don't expect equality as this class concerns itself with
        object identity rather than object equality.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: L[1] = True
            sage: loads(dumps(L)) == L
            False
            sage: list(loads(dumps(L)).items())
            [(1, True)]"""
    def __setitem__(self, k, value) -> Any:
        """MonoDict.__setitem__(self, k, value)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 665)

        Set the value corresponding to a key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import MonoDict
            sage: L = MonoDict()
            sage: a = 'a'
            sage: L[a] = -1   # indirect doctest
            sage: L[a]
            -1
            sage: L[a] = 1
            sage: L[a]
            1
            sage: len(L)
            1"""

class MonoDictEraser:
    """MonoDictEraser(D)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 173)

    Erase items from a :class:`MonoDict` when a weak reference becomes
    invalid.

    This is of internal use only. Instances of this class will be passed as a
    callback function when creating a weak reference.

    EXAMPLES::

        sage: from sage.structure.coerce_dict import MonoDict
        sage: class A: pass
        sage: a = A()
        sage: M = MonoDict()
        sage: M[a] = 1
        sage: len(M)
        1
        sage: del a
        sage: import gc
        sage: n = gc.collect()
        sage: len(M)    # indirect doctest
        0

    AUTHOR:

    - Simon King (2012-01)
    - Nils Bruin (2013-11)"""
    def __init__(self, D) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 203)

                INPUT:

                - ``D`` -- a :class:`MonoDict`

                EXAMPLES::

                    sage: k = set([1])
                    sage: D = sage.structure.coerce_dict.MonoDict([(k,1)])
                    sage: len(D)
                    1
                    sage: del k
                    sage: len(D) # indirect doctest
                    0
        """
    def __call__(self, r) -> Any:
        """MonoDictEraser.__call__(self, r)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 221)

        INPUT:

        - ``r`` -- a weak reference with key

        For internal use only.

        EXAMPLES::

            sage: k = set([1])
            sage: D = sage.structure.coerce_dict.MonoDict([(k,1)])
            sage: len(D)
            1
            sage: del k
            sage: len(D) # indirect doctest
            0"""

class ObjectWrapper:
    """File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 104)

        A simple fast wrapper around a Python object. This is like a
        1-element tuple except that it does not keep a reference to the
        wrapped object.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class TripleDict:
    """TripleDict(data=None, weak_values=False, *)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 983)

    This is a hashtable specifically designed for (read) speed in
    the coercion model.

    It differs from a python dict in the following important ways:

       - All keys must be sequence of exactly three elements. All sequence
         types (tuple, list, etc.) map to the same item.

       - Any of the three key components that support weak-refs are stored
         via a weakref. If any of these components gets garbage collected
         then the entire entry is removed. In that sense, this structure
         behaves like a nested :class:`~weakref.WeakKeyDictionary`.

       - Comparison is done using the 'is' rather than '==' operator.

    There are special cdef set/get methods for faster access.
    It is bare-bones in the sense that not all dictionary methods are
    implemented.

    INPUT:

    - ``data`` -- (optional) iterable defining initial data, as dict or
      iterable of (key, value) pairs

    - ``weak_values`` -- boolean (default: ``False``); if it is
      ``True``, weak references to the values in this dictionary will be used,
      when possible

    IMPLEMENTATION:

    It is implemented as a hash table with open addressing, similar to python's
    dict.

    EXAMPLES::

        sage: from sage.structure.coerce_dict import TripleDict
        sage: L = TripleDict()
        sage: a = 'a'; b = 'b'; c = 'c'
        sage: L[a,b,c] = 1
        sage: L[a,b,c]
        1
        sage: L[c,b,a] = -1
        sage: sorted(L.items())
        [(('a', 'b', 'c'), 1), (('c', 'b', 'a'), -1)]
        sage: del L[a,b,c]
        sage: list(L.items())
        [(('c', 'b', 'a'), -1)]
        sage: len(L)
        1
        sage: for i in range(1000):
        ....:     L[i,i,i] = i
        sage: len(L)
        1001
        sage: L = TripleDict(L)
        sage: L[c,b,a]
        -1
        sage: L[a,b,c]
        Traceback (most recent call last):
        ...
        KeyError: ('a', 'b', 'c')
        sage: L[a]
        Traceback (most recent call last):
        ...
        KeyError: 'a'
        sage: L[a] = 1
        Traceback (most recent call last):
        ...
        KeyError: 'a'

    TESTS:

    Here, we demonstrate the use of weak values::

        sage: class Foo: pass
        sage: T = TripleDict()
        sage: TW = TripleDict(weak_values=True)
        sage: a = Foo()
        sage: b = Foo()
        sage: k = 1
        sage: T[a,k,k]=1
        sage: T[k,a,k]=2
        sage: T[k,k,a]=3
        sage: T[k,k,k]=a
        sage: TW[b,k,k]=1
        sage: TW[k,b,k]=2
        sage: TW[k,k,b]=3
        sage: TW[k,k,k]=b
        sage: len(T)
        4
        sage: len(TW)
        4
        sage: (k,k,k) in T
        True
        sage: (k,k,k) in TW
        True
        sage: T[k,k,k] is a
        True
        sage: TW[k,k,k] is b
        True

    Now, ``T`` holds a strong reference to ``a``, namely in ``T[k,k,k]``. Hence,
    when we delete ``a``, *all* items of ``T`` survive::

        sage: import gc
        sage: del a
        sage: _ = gc.collect()
        sage: len(T)
        4

    Only when we remove the strong reference, the items become collectable::

        sage: del T[k,k,k]
        sage: _ = gc.collect()
        sage: len(T)
        0

    The situation is different for ``TW``, since it only holds *weak*
    references to ``a``. Therefore, all items become collectable after
    deleting ``a``::

        sage: del b
        sage: _ = gc.collect()
        sage: len(TW)
        0

    AUTHORS:

    - Robert Bradshaw, 2007-08

    - Simon King, 2012-01

    - Nils Bruin, 2012-08

    - Simon King, 2013-02

    - Nils Bruin, 2013-11"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None:
        '''File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1205)

                Create a special dict using triples for keys.

                EXAMPLES::

                    sage: from sage.structure.coerce_dict import TripleDict
                    sage: L = TripleDict()
                    sage: a = \'a\'; b = \'b\'; c = \'c\'
                    sage: L[a,b,c] = 1
                    sage: L[a,b,c]
                    1
                    sage: key = ("x", "y", "z")
                    sage: L = TripleDict([(key, 42)])
                    sage: L[key]
                    42
                    sage: L = TripleDict({key: 42})
                    sage: L[key]
                    42
        '''
    @overload
    def copy(self) -> Any:
        """TripleDict.copy(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1485)

        Return a copy of this :class:`TripleDict` as Python dict.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: L[1,2,3] = 42
            sage: L.copy()
            {(1, 2, 3): 42}"""
    @overload
    def copy(self) -> Any:
        """TripleDict.copy(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1485)

        Return a copy of this :class:`TripleDict` as Python dict.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: L[1,2,3] = 42
            sage: L.copy()
            {(1, 2, 3): 42}"""
    @overload
    def items(self) -> Any:
        """TripleDict.items(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1440)

        Iterate over the ``(key, value)`` pairs of this :class:`TripleDict`.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: L[1,2,3] = None
            sage: L.items()
            <...generator object at ...>
            sage: list(L.items())
            [((1, 2, 3), None)]"""
    @overload
    def items(self) -> Any:
        """TripleDict.items(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1440)

        Iterate over the ``(key, value)`` pairs of this :class:`TripleDict`.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: L[1,2,3] = None
            sage: L.items()
            <...generator object at ...>
            sage: list(L.items())
            [((1, 2, 3), None)]"""
    @overload
    def items(self) -> Any:
        """TripleDict.items(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1440)

        Iterate over the ``(key, value)`` pairs of this :class:`TripleDict`.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: L[1,2,3] = None
            sage: L.items()
            <...generator object at ...>
            sage: list(L.items())
            [((1, 2, 3), None)]"""
    def __contains__(self, k) -> Any:
        """TripleDict.__contains__(self, k)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1256)

        Test if the dictionary contains a given key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: a = 'a'; b = 'ab'; c = 15
            sage: L[a,b,c] = 123
            sage: (a,b,c) in L         # indirect doctest
            True

        The keys are compared by identity, not by equality. Hence, we have::

            sage: c == 15
            True
            sage: (a, b, 15) in L
            False

        TESTS::

            sage: a in L
            Traceback (most recent call last):
            ...
            KeyError: 'a'
            sage: (a, b) in L
            Traceback (most recent call last):
            ...
            KeyError: ('a', 'ab')"""
    def __delitem__(self, k) -> Any:
        """TripleDict.__delitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1412)

        Delete the value corresponding to a key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: a = 'a'; b = 'b'; c = 'c'
            sage: L[a,b,c] = -1
            sage: (a,b,c) in L
            True
            sage: del L[a,b,c]
            sage: len(L)
            0
            sage: (a,b,c) in L
            False"""
    def __getitem__(self, k) -> Any:
        """TripleDict.__getitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1299)

        Get the value corresponding to a key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: a = 'a'; b = 'b'; c = 'c'
            sage: L[a,b,c] = 1
            sage: L[a,b,c]
            1"""
    def __len__(self) -> Any:
        """TripleDict.__len__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1238)

        The number of items in ``self``.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: a = 'a'; b = 'b'; c = 'c'
            sage: L[a,b,c] = 1
            sage: L[a,b,c] = -1 # re-assign
            sage: L[a,c,b] = 1
            sage: L[a,a,None] = None
            sage: len(L)
            3"""
    def __reduce__(self) -> Any:
        """TripleDict.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1499)

        Note that we don't expect equality as this class concerns itself with
        object identity rather than object equality.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: L[1,2,3] = True
            sage: loads(dumps(L)) == L
            False
            sage: list(loads(dumps(L)).items())
            [((1, 2, 3), True)]"""
    def __setitem__(self, k, value) -> Any:
        """TripleDict.__setitem__(self, k, value)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 1329)

        Set the value corresponding to a key.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: L = TripleDict()
            sage: a = 'a'; b = 'b'; c = 'c'
            sage: L[a,b,c] = -1
            sage: L[a,b,c]
            -1"""

class TripleDictEraser:
    """TripleDictEraser(D)

    File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 890)

    Erases items from a :class:`TripleDict` when a weak reference becomes
    invalid.

    This is of internal use only. Instances of this class will be passed as a
    callback function when creating a weak reference.

    EXAMPLES::

        sage: from sage.structure.coerce_dict import TripleDict
        sage: class A: pass
        sage: a = A()
        sage: T = TripleDict()
        sage: T[a,ZZ,None] = 1
        sage: T[ZZ,a,1] = 2
        sage: T[a,a,ZZ] = 3
        sage: len(T)
        3
        sage: del a
        sage: import gc
        sage: n = gc.collect()
        sage: len(T) # indirect doctest
        0

    AUTHOR:

    - Simon King (2012-01)
    - Nils Bruin (2013-11)"""
    def __init__(self, D) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 922)

                INPUT:

                - ``D`` -- a :class:`TripleDict`. For internal use only.

                EXAMPLES::

                    sage: D = sage.structure.coerce_dict.TripleDict()
                    sage: k = set([1])
                    sage: D[k,1,1] = 1
                    sage: len(D)
                    1
                    sage: del k
                    sage: len(D) # indirect doctest
                    0
        """
    def __call__(self, r) -> Any:
        """TripleDictEraser.__call__(self, r)

        File: /build/sagemath/src/sage/src/sage/structure/coerce_dict.pyx (starting at line 941)

        INPUT:

        - ``r`` -- a weak reference with key

        For internal use only.

        EXAMPLES::

            sage: from sage.structure.coerce_dict import TripleDict
            sage: class A: pass
            sage: a = A()
            sage: T = TripleDict()
            sage: T[a,ZZ,None] = 1
            sage: T[ZZ,a,1] = 2
            sage: T[a,a,ZZ] = 3
            sage: len(T)
            3
            sage: del a
            sage: import gc
            sage: n = gc.collect()
            sage: len(T)    # indirect doctest
            0"""
