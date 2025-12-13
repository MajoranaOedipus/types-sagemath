from sage.misc.superseded import deprecation as deprecation
from typing import Any, ClassVar, overload

class CachedWeakValueDictionary(WeakValueDictionary):
    """CachedWeakValueDictionary(data=(), cache=16)

    File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 1118)

    This class extends :class:`WeakValueDictionary` with a strong cache
    to the most recently added values. It is meant to solve the case
    where significant performance losses can occur if a value is deleted
    too early, but where keeping a value alive too long does not hurt
    much. This is typically the case with cached functions.

    EXAMPLES:

    We illustrate the difference between :class:`WeakValueDictionary`
    and :class:`CachedWeakValueDictionary`. An item is removed from a
    :class:`WeakValueDictionary` as soon as there are no references to
    it::

        sage: from sage.misc.weak_dict import WeakValueDictionary
        sage: D = WeakValueDictionary()
        sage: class Test(): pass
        sage: tmp = Test()
        sage: D[0] = tmp
        sage: 0 in D
        True
        sage: del tmp
        sage: 0 in D
        False

    So, if you have a cached function repeatedly creating the same
    temporary object and deleting it (in a helper function called from
    a loop for example), this caching will not help at all. With
    :class:`CachedWeakValueDictionary`, the most recently added values
    are not deleted. After adding enough new values, the item is removed
    anyway::

        sage: from sage.misc.weak_dict import CachedWeakValueDictionary
        sage: D = CachedWeakValueDictionary(cache=4)
        sage: class Test(): pass
        sage: tmp = Test()
        sage: D[0] = tmp
        sage: 0 in D
        True
        sage: del tmp
        sage: 0 in D
        True
        sage: for i in range(5):
        ....:     D[1] = Test()
        ....:     print(0 in D)
        True
        True
        True
        False
        False"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, data=..., cache=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 1181)

                Create a :class:`CachedWeakValueDictionary` with given initial
                data and strong cache size.

                INPUT:

                - ``data`` -- (optional) iterable of key-value pairs

                - ``cache`` -- (default: 16) number of values with strong
                  references

                EXAMPLES::

                    sage: L = [(p, GF(p)) for p in prime_range(10)]                             # needs sage.libs.pari
                    sage: from sage.misc.weak_dict import CachedWeakValueDictionary
                    sage: D = CachedWeakValueDictionary()
                    sage: len(D)
                    0
                    sage: D = CachedWeakValueDictionary(L)                                      # needs sage.libs.pari
                    sage: len(D) == len(L)                                                      # needs sage.libs.pari
                    True

                A :class:`CachedWeakValueDictionary` with a cache size of zero
                works exactly the same as an ordinary
                :class:`WeakValueDictionary`::

                    sage: D = CachedWeakValueDictionary(cache=0)
                    sage: class Test(): pass
                    sage: tmp = Test()
                    sage: D[0] = tmp
                    sage: del tmp
                    sage: 0 in D
                    False
        """
    @overload
    def __init__(self, cache=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 1181)

                Create a :class:`CachedWeakValueDictionary` with given initial
                data and strong cache size.

                INPUT:

                - ``data`` -- (optional) iterable of key-value pairs

                - ``cache`` -- (default: 16) number of values with strong
                  references

                EXAMPLES::

                    sage: L = [(p, GF(p)) for p in prime_range(10)]                             # needs sage.libs.pari
                    sage: from sage.misc.weak_dict import CachedWeakValueDictionary
                    sage: D = CachedWeakValueDictionary()
                    sage: len(D)
                    0
                    sage: D = CachedWeakValueDictionary(L)                                      # needs sage.libs.pari
                    sage: len(D) == len(L)                                                      # needs sage.libs.pari
                    True

                A :class:`CachedWeakValueDictionary` with a cache size of zero
                works exactly the same as an ordinary
                :class:`WeakValueDictionary`::

                    sage: D = CachedWeakValueDictionary(cache=0)
                    sage: class Test(): pass
                    sage: tmp = Test()
                    sage: D[0] = tmp
                    sage: del tmp
                    sage: 0 in D
                    False
        """

class WeakValueDictEraser:
    """WeakValueDictEraser(D)

    File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 142)

    Erases items from a :class:`sage.misc.weak_dict.WeakValueDictionary` when
    a weak reference becomes invalid.

    This is of internal use only. Instances of this class will be passed as a
    callback function when creating a weak reference.

    EXAMPLES::

        sage: from sage.misc.weak_dict import WeakValueDictionary
        sage: v = frozenset([1])
        sage: D = WeakValueDictionary({1 : v})
        sage: len(D)
        1
        sage: del v
        sage: len(D)
        0

    AUTHOR:

     - Nils Bruin (2013-11)"""
    def __init__(self, D) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 167)

                INPUT:

                - ``D`` -- a :class:`sage.misc.weak_dict.WeakValueDictionary`

                EXAMPLES::

                    sage: v = frozenset([1])
                    sage: D = sage.misc.weak_dict.WeakValueDictionary({ 1 : v })
                    sage: len(D)
                    1
                    sage: del v
                    sage: len(D)  # indirect doctest
                    0
        """
    def __call__(self, r) -> Any:
        """WeakValueDictEraser.__call__(self, r)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 185)

        INPUT:

        - ``r`` -- a weak reference with key

        When this is called with a weak reference ``r``, then an entry from the
        dictionary pointed to by ``self.D`` is removed that has ``r`` as a value
        identically, stored under a key with hash ``r.key``. If no such key
        exists, or if the dictionary itself does not exist any more, then nothing
        happens.

        If the dictionary has an iterator active on it then the object is
        queued for removal when all iterators have concluded.

        EXAMPLES::

            sage: v = frozenset([1])
            sage: D = sage.misc.weak_dict.WeakValueDictionary({ 1 : v })
            sage: len(D)
            1
            sage: del v
            sage: len(D)  # indirect doctest
            0"""

class WeakValueDictionary(dict):
    """WeakValueDictionary(data=())

    File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 222)

    IMPLEMENTATION:

    The :class:`WeakValueDictionary` inherits from :class:`dict`. In its
    implementation, it stores weakrefs to the actual values under the keys.
    All access routines are wrapped to transparently place and remove these
    weakrefs.

    NOTE:

    In contrast to :class:`weakref.WeakValueDictionary` in Python's
    :mod:`weakref` module, the callback does not need to assume that the
    dictionary key is a valid Python object when it is called. There is no
    need to compute the hash or compare the dictionary keys. This is why
    the example below would not work with
    :class:`weakref.WeakValueDictionary`, but does work with
    :class:`sage.misc.weak_dict.WeakValueDictionary`.

    EXAMPLES::

        sage: import weakref
        sage: class Vals(): pass
        sage: class Keys:
        ....:     def __init__(self, val):
        ....:         self.val = weakref.ref(val)
        ....:     def __hash__(self):
        ....:         return hash(self.val())
        ....:     def __eq__(self, other):
        ....:         return self.val() == other.val()
        ....:     def __ne__(self, other):
        ....:         return self.val() != other.val()
        sage: ValList = [Vals() for _ in range(10)]
        sage: import sage.misc.weak_dict
        sage: D = sage.misc.weak_dict.WeakValueDictionary()
        sage: for v in ValList:
        ....:     D[Keys(v)] = v
        sage: len(D)
        10
        sage: del ValList
        sage: len(D)
        1
        sage: del v
        sage: len(D)
        0

    TESTS:

    The following reflects the behaviour of the callback on weak dict values,
    as discussed on :issue:`13394`.  ::

        sage: from sage.misc.weak_dict import WeakValueDictionary
        sage: V = [set(range(n)) for n in range(5)]
        sage: D = WeakValueDictionary(enumerate(V))

    The line ``V[k] = None`` triggers execution of the callback functions of
    the dictionary values. However, the actual deletion is postponed till
    after the iteration over the dictionary has finished. Hence, when the
    callbacks are executed, the values which the callback belongs to has
    already been overridden by a new value. Therefore, the callback does not
    delete the item::

        sage: for k in D:    # indirect doctest
        ....:     V[k] = None
        ....:     D[k] = ZZ
        sage: len(D)
        5
        sage: D[1]
        Integer Ring

    The following is a stress test for weak value dictionaries::

        sage: class C():
        ....:     def __init__(self, n):
        ....:         self.n = n
        ....:     def __lt__(self, other):
        ....:         return self.n < other.n
        ....:     def __eq__(self, other):
        ....:         return self.n == other.n
        ....:     def __ne__(self, other):
        ....:         return self.val() != other.val()
        sage: B = 100
        sage: L = [None]*B
        sage: D1 = WeakValueDictionary()
        sage: D2 = WeakValueDictionary()
        sage: for i in range(10000):
        ....:     ki = floor(random()*B)
        ....:     vi = C(floor(random()*B))
        ....:     D1[ki] = vi
        ....:     D2[ki] = vi
        ....:     L[ki]  = vi
        ....:     del vi
        ....:     ko = floor(random()*B)
        ....:     if ko in D1:
        ....:         del D1[ko]
        ....:         L[ko] = None
        ....:     assert D1 == D2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, data=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 332)

                Create a :class:`WeakValueDictionary` with given initial data.

                INPUT:

                - ``data`` -- (optional) iterable of key-value pairs

                EXAMPLES::

                    sage: # needs sage.rings.finite_rings
                    sage: L = [(p, GF(p)) for p in prime_range(10)]
                    sage: import sage.misc.weak_dict
                    sage: D = sage.misc.weak_dict.WeakValueDictionary()
                    sage: len(D)
                    0
                    sage: D = sage.misc.weak_dict.WeakValueDictionary(L)
                    sage: len(D) == len(L)
                    True
        """
    def get(self, k, d=...) -> Any:
        '''WeakValueDictionary.get(self, k, d=None)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 632)

        Return the stored value for a key, or a default value for unknown keys.

        The default value defaults to ``None``.

        EXAMPLES::

            sage: import sage.misc.weak_dict

            sage: # needs sage.libs.pari
            sage: L = [GF(p) for p in prime_range(10^3)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: 100 in D
            True
            sage: 200 in D
            False
            sage: D.get(100, "not found")
            Finite Field of size 547
            sage: D.get(200, "not found")
            \'not found\'
            sage: D.get(200) is None
            True

        TESTS:

        Check that :issue:`15956` has been fixed, i.e., a :exc:`TypeError` is
        raised for unhashable objects::

            sage: # needs sage.libs.pari
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D.get(matrix([]))                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable'''
    @overload
    def items(self) -> Any:
        '''WeakValueDictionary.items(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 937)

        Iterate over the items of this dictionary.

        .. WARNING::

            Iteration is unsafe, if the length of the dictionary changes
            during the iteration! This can also happen by garbage collection.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: class Keys():
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __hash__(self):
            ....:         if self.n % 2:
            ....:             return int(5)
            ....:         return int(3)
            ....:     def __repr__(self):
            ....:         return "[%s]" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [(Keys(n), Vals(n)) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(L)

        We remove one dictionary item directly. Another item is removed by
        means of garbage collection. By consequence, there remain eight
        items in the dictionary::

            sage: del D[Keys(2)]
            sage: del L[5]
            sage: for k,v in sorted(D.items()):
            ....:     print("{} {}".format(k, v))
            [0] <0>
            [1] <1>
            [3] <3>
            [4] <4>
            [6] <6>
            [7] <7>
            [8] <8>
            [9] <9>'''
    @overload
    def items(self) -> Any:
        '''WeakValueDictionary.items(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 937)

        Iterate over the items of this dictionary.

        .. WARNING::

            Iteration is unsafe, if the length of the dictionary changes
            during the iteration! This can also happen by garbage collection.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: class Keys():
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __hash__(self):
            ....:         if self.n % 2:
            ....:             return int(5)
            ....:         return int(3)
            ....:     def __repr__(self):
            ....:         return "[%s]" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [(Keys(n), Vals(n)) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(L)

        We remove one dictionary item directly. Another item is removed by
        means of garbage collection. By consequence, there remain eight
        items in the dictionary::

            sage: del D[Keys(2)]
            sage: del L[5]
            sage: for k,v in sorted(D.items()):
            ....:     print("{} {}".format(k, v))
            [0] <0>
            [1] <1>
            [3] <3>
            [4] <4>
            [6] <6>
            [7] <7>
            [8] <8>
            [9] <9>'''
    def items_list(self) -> Any:
        '''WeakValueDictionary.items_list(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 1007)

        The key-value pairs of this dictionary.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: class Keys():
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __hash__(self):
            ....:         if self.n % 2:
            ....:             return int(5)
            ....:         return int(3)
            ....:     def __repr__(self):
            ....:         return "[%s]" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [(Keys(n), Vals(n)) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(L)

        We remove one dictionary item directly. Another item is removed by
        means of garbage collection. By consequence, there remain eight
        items in the dictionary::

            sage: del D[Keys(2)]
            sage: del L[5]
            sage: sorted(D.items())
            [([0], <0>),
             ([1], <1>),
             ([3], <3>),
             ([4], <4>),
             ([6], <6>),
             ([7], <7>),
             ([8], <8>),
             ([9], <9>)]'''
    @overload
    def iteritems(self) -> Any:
        """WeakValueDictionary.iteritems(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 921)

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: T = list(D.iteritems())
            doctest:warning...:
            DeprecationWarning: use items instead
            See https://github.com/sagemath/sage/issues/34488 for details."""
    @overload
    def iteritems(self) -> Any:
        """WeakValueDictionary.iteritems(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 921)

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: T = list(D.iteritems())
            doctest:warning...:
            DeprecationWarning: use items instead
            See https://github.com/sagemath/sage/issues/34488 for details."""
    @overload
    def itervalues(self) -> Any:
        """WeakValueDictionary.itervalues(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 816)

        Deprecated.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: T = list(D.itervalues())
            doctest:warning...:
            DeprecationWarning: use values instead
            See https://github.com/sagemath/sage/issues/34488 for details."""
    @overload
    def itervalues(self) -> Any:
        """WeakValueDictionary.itervalues(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 816)

        Deprecated.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: T = list(D.itervalues())
            doctest:warning...:
            DeprecationWarning: use values instead
            See https://github.com/sagemath/sage/issues/34488 for details."""
    @overload
    def keys(self) -> Any:
        """WeakValueDictionary.keys(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 795)

        The list of keys.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: del L[4]

        One item got deleted from the list ``L`` and hence the corresponding
        item in the dictionary got deleted as well. Therefore, the
        corresponding key 4 is missing in the list of keys::

            sage: sorted(D.keys())
            [0, 1, 2, 3, 5, 6, 7, 8, 9]"""
    @overload
    def keys(self) -> Any:
        """WeakValueDictionary.keys(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 795)

        The list of keys.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: del L[4]

        One item got deleted from the list ``L`` and hence the corresponding
        item in the dictionary got deleted as well. Therefore, the
        corresponding key 4 is missing in the list of keys::

            sage: sorted(D.keys())
            [0, 1, 2, 3, 5, 6, 7, 8, 9]"""
    def pop(self, k) -> Any:
        """WeakValueDictionary.pop(self, k)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 558)

        Return the value for a given key, and delete it from the dictionary.

        EXAMPLES::

            sage: import sage.misc.weak_dict

            sage: # needs sage.libs.pari
            sage: L = [GF(p) for p in prime_range(10^3)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: 20 in D
            True
            sage: D.pop(20)
            Finite Field of size 73
            sage: 20 in D
            False
            sage: D.pop(20)
            Traceback (most recent call last):
            ...
            KeyError: 20

        TESTS:

        Check that :issue:`15956` has been fixed, i.e., a :exc:`TypeError` is
        raised for unhashable objects::

            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D.pop(matrix([]))                                                     # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable"""
    @overload
    def popitem(self) -> Any:
        """WeakValueDictionary.popitem(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 603)

        Return and delete some item from the dictionary.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[1] = ZZ

        The dictionary only contains a single item, hence, it is clear which
        one will be returned::

            sage: D.popitem()
            (1, Integer Ring)

        Now, the dictionary is empty, and hence the next attempt to pop an
        item will fail with a :exc:`KeyError`::

            sage: D.popitem()
            Traceback (most recent call last):
            ...
            KeyError: 'popitem(): weak value dictionary is empty'"""
    @overload
    def popitem(self) -> Any:
        """WeakValueDictionary.popitem(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 603)

        Return and delete some item from the dictionary.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[1] = ZZ

        The dictionary only contains a single item, hence, it is clear which
        one will be returned::

            sage: D.popitem()
            (1, Integer Ring)

        Now, the dictionary is empty, and hence the next attempt to pop an
        item will fail with a :exc:`KeyError`::

            sage: D.popitem()
            Traceback (most recent call last):
            ...
            KeyError: 'popitem(): weak value dictionary is empty'"""
    @overload
    def popitem(self) -> Any:
        """WeakValueDictionary.popitem(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 603)

        Return and delete some item from the dictionary.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[1] = ZZ

        The dictionary only contains a single item, hence, it is clear which
        one will be returned::

            sage: D.popitem()
            (1, Integer Ring)

        Now, the dictionary is empty, and hence the next attempt to pop an
        item will fail with a :exc:`KeyError`::

            sage: D.popitem()
            Traceback (most recent call last):
            ...
            KeyError: 'popitem(): weak value dictionary is empty'"""
    def setdefault(self, k, default=...) -> Any:
        """WeakValueDictionary.setdefault(self, k, default=None)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 423)

        Return the stored value for a given key; return and store a default
        value if no previous value is stored.

        EXAMPLES::

            sage: import sage.misc.weak_dict

            sage: # needs sage.libs.pari
            sage: L = [(p, GF(p)) for p in prime_range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(L)
            sage: len(D)
            4

        The value for an existing key is returned and not overridden::

            sage: # needs sage.libs.pari
            sage: D.setdefault(5, ZZ)
            Finite Field of size 5
            sage: D[5]
            Finite Field of size 5

        For a non-existing key, the default value is stored and returned::

            sage: # needs sage.libs.pari
            sage: 4 in D
            False
            sage: D.setdefault(4, ZZ)
            Integer Ring
            sage: 4 in D
            True
            sage: D[4]
            Integer Ring
            sage: len(D)
            5

        TESTS:

        Check that :issue:`15956` has been fixed, i.e., a :exc:`TypeError` is
        raised for unhashable objects::

            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D.setdefault(matrix([]), ZZ)                                          # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable"""
    @overload
    def values(self) -> Any:
        '''WeakValueDictionary.values(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 834)

        Iterate over the values of this dictionary.

        .. WARNING::

            Iteration is unsafe, if the length of the dictionary changes
            during the iteration! This can also happen by garbage collection.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [Vals(n) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))

        We delete one item from ``D`` and we delete one item from the list
        ``L``. The latter implies that the corresponding item from ``D`` gets
        deleted as well. Hence, there remain eight values::

            sage: del D[2]
            sage: del L[5]
            sage: for v in sorted(D.values()):
            ....:     print(v)
            <0>
            <1>
            <3>
            <4>
            <6>
            <7>
            <8>
            <9>'''
    @overload
    def values(self) -> Any:
        '''WeakValueDictionary.values(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 834)

        Iterate over the values of this dictionary.

        .. WARNING::

            Iteration is unsafe, if the length of the dictionary changes
            during the iteration! This can also happen by garbage collection.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [Vals(n) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))

        We delete one item from ``D`` and we delete one item from the list
        ``L``. The latter implies that the corresponding item from ``D`` gets
        deleted as well. Hence, there remain eight values::

            sage: del D[2]
            sage: del L[5]
            sage: for v in sorted(D.values()):
            ....:     print(v)
            <0>
            <1>
            <3>
            <4>
            <6>
            <7>
            <8>
            <9>'''
    @overload
    def values_list(self) -> Any:
        '''WeakValueDictionary.values_list(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 889)

        Return the list of values.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [Vals(n) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))

        We delete one item from ``D`` and we delete one item from the list
        ``L``. The latter implies that the corresponding item from ``D`` gets
        deleted as well. Hence, there remain eight values::

            sage: del D[2]
            sage: del L[5]
            sage: sorted(D.values_list())
            [<0>, <1>, <3>, <4>, <6>, <7>, <8>, <9>]'''
    @overload
    def values_list(self) -> Any:
        '''WeakValueDictionary.values_list(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 889)

        Return the list of values.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals:
            ....:     def __init__(self, n):
            ....:         self.n = n
            ....:     def __repr__(self):
            ....:         return "<%s>" % self.n
            ....:     def __lt__(self, other):
            ....:         return self.n < other.n
            ....:     def __eq__(self, other):
            ....:         return self.n == other.n
            ....:     def __ne__(self, other):
            ....:         return self.val() != other.val()
            sage: L = [Vals(n) for n in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))

        We delete one item from ``D`` and we delete one item from the list
        ``L``. The latter implies that the corresponding item from ``D`` gets
        deleted as well. Hence, there remain eight values::

            sage: del D[2]
            sage: del L[5]
            sage: sorted(D.values_list())
            [<0>, <1>, <3>, <4>, <6>, <7>, <8>, <9>]'''
    def __contains__(self, k) -> Any:
        """WeakValueDictionary.__contains__(self, k)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 715)

        Containment in the set of keys.

        TESTS::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: 3 in D     # indirect doctest
            True

        As usual, keys are compared by equality and not by identity::

            sage: int(3) in D
            True

        This is a weak value dictionary. Hence, the existence of the
        dictionary does not prevent the values from garbage collection,
        thereby removing the corresponding key-value pairs::

            sage: del L[3]
            sage: 3 in D
            False

        Check that :issue:`15956` has been fixed, i.e., a :exc:`TypeError` is
        raised for unhashable objects::

            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: matrix([]) in D                                                       # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable"""
    def __copy__(self) -> Any:
        """WeakValueDictionary.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 359)

        Return a copy of this weak dictionary.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[1] = QQ
            sage: D[2] = ZZ
            sage: D[None] = CC                                                          # needs sage.rings.real_mpfr
            sage: E = copy(D)    # indirect doctest
            sage: set(E.items()) == set(D.items())
            True"""
    def __deepcopy__(self, memo) -> Any:
        """WeakValueDictionary.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 376)

        Return a copy of this dictionary using copies of the keys.

        .. NOTE::

            The values of the dictionary are not copied, since we
            cannot copy the external strong references to the values,
            which are decisive for garbage collection.

        EXAMPLES::

            sage: class C(): pass
            sage: V = [C(),C()]
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[C()] = V[0]
            sage: D[C()] = V[1]
            sage: E = deepcopy(D)     # indirect doctest

        The keys are copied (in this silly example, the copies of the keys are
        actually not equal to the original keys)::

            sage: set(E.keys()) == set(D.keys())
            False

        However, the values are not copied::

            sage: set(E.values()) == set(D.values()) == set(V)
            True"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, k) -> Any:
        """WeakValueDictionary.__getitem__(self, k)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 677)

        TESTS::

            sage: import sage.misc.weak_dict
            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[ZZ] = QQ
            sage: D[QQ]
            Traceback (most recent call last):
            ...
            KeyError: Rational Field
            sage: D[ZZ]     # indirect doctest
            Rational Field

        As usual, the dictionary keys are compared by ``==`` and not by
        identity::

            sage: D[10] = ZZ
            sage: D[int(10)]
            Integer Ring

        Check that :issue:`15956` has been fixed, i.e., a :exc:`TypeError` is
        raised for unhashable objects::

            sage: D = sage.misc.weak_dict.WeakValueDictionary()
            sage: D[matrix([])]                                                         # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable"""
    def __iter__(self) -> Any:
        """WeakValueDictionary.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 757)

        Iterate over the keys of this dictionary.

        .. WARNING::

            Iteration is unsafe, if the length of the dictionary changes
            during the iteration! This can also happen by garbage collection.

        EXAMPLES::

            sage: import sage.misc.weak_dict
            sage: class Vals(): pass
            sage: L = [Vals() for _ in range(10)]
            sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
            sage: del L[4]

        One item got deleted from the list ``L`` and hence the corresponding
        item in the dictionary got deleted as well. Therefore, the
        corresponding key 4 is missing in the list of keys::

            sage: sorted(D)
            [0, 1, 2, 3, 5, 6, 7, 8, 9]"""
    def __setitem__(self, index, object) -> None:
        """WeakValueDictionary.__setitem__(self, k, v)

        File: /build/sagemath/src/sage/src/sage/misc/weak_dict.pyx (starting at line 479)

         EXAMPLES::

             sage: import sage.misc.weak_dict
             sage: D = sage.misc.weak_dict.WeakValueDictionary()
             sage: ZZ in D
             False

         One can set new items::

             sage: D[ZZ] = QQ   # indirect doctest
             sage: D[ZZ]
             Rational Field
             sage: len(D)
             1
             sage: ZZ in D
             True

        One can also override existing items::

            sage: D[ZZ] = RLF
            sage: ZZ in D
            True
            sage: D[ZZ]
            Real Lazy Field
            sage: len(D)
            1

         TESTS:

         One may wonder whether it causes problems when garbage collection for
         a previously existing item happens *after* overriding the item. The
         example shows that it is not a problem::

             sage: class Cycle:
             ....:     def __init__(self):
             ....:         self.selfref = self
             sage: L = [Cycle() for _ in range(5)]
             sage: D = sage.misc.weak_dict.WeakValueDictionary(enumerate(L))
             sage: len(D)
             5
             sage: import gc
             sage: gc.disable()
             sage: del L
             sage: len(D)
             5
             sage: D[2] = ZZ
             sage: len(D)
             5
             sage: gc.enable()
             sage: _ = gc.collect()
             sage: len(D)
             1
             sage: list(D.items())
             [(2, Integer Ring)]

         Check that :issue:`15956` has been fixed, i.e., a :exc:`TypeError` is
         raised for unhashable objects::

             sage: D = sage.misc.weak_dict.WeakValueDictionary()
             sage: D[matrix([])] = ZZ                                                    # needs sage.modules
             Traceback (most recent call last):
             ...
             TypeError: mutable matrices are unhashable
 """
