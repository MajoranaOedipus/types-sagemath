import _cython_3_2_1
import sage.structure.parent
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.call import AttrCallObject as AttrCallObject
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from typing import Any, ClassVar, overload

def Family(indices, function=None, hidden_keys=[], hidden_function=None, lazy=False, name=None) -> AbstractFamily:
    r"""Family(indices, function=None, hidden_keys=[], hidden_function=None, lazy=False, name=None)

File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 58)

A Family is an associative container which models a family
`(f_i)_{i \in I}`. Then, ``f[i]`` returns the element of the family
indexed by `i`. Whenever available, set and combinatorial class
operations (counting, iteration, listing) on the family are induced
from those of the index set.

There are several available implementations (classes) for different
usages; Family serves as a factory, and will create instances of
the appropriate classes depending on its arguments.

INPUT:

- ``indices`` -- the indices for the family
- ``function`` -- (optional) the function `f` applied to all visible
  indices; the default is the identity function
- ``hidden_keys`` -- (optional) a list of hidden indices that can be
  accessed through ``my_family[i]``
- ``hidden_function`` -- (optional) a function for the hidden indices
- ``lazy`` -- boolean (default: ``False``); whether the family is lazily
  created or not; if the indices are infinite, then this is automatically
  made ``True``
- ``name`` -- (optional) the name of the function; only used when the
  family is lazily created via a function

EXAMPLES:

In its simplest form, a list `l = [l_0, l_1, \ldots, l_{\ell}]` or a
tuple by itself is considered as the family `(l_i)_{i \in I}` where
`I` is the set `\{0, \ldots, \ell\}` where `\ell` is ``len(l) - 1``.
So ``Family(l)`` returns the corresponding family::

    sage: f = Family([1,2,3])
    sage: f
    Family (1, 2, 3)
    sage: f = Family((1,2,3))
    sage: f
    Family (1, 2, 3)

Instead of a list you can as well pass any iterable object::

    sage: f = Family(2*i+1 for i in [1,2,3])
    sage: f
    Family (3, 5, 7)

A family can also be constructed from a dictionary ``t``. The resulting
family is very close to ``t``, except that the elements of the family
are the values of ``t``. Here, we define the family
`(f_i)_{i \in \{3,4,7\}}` with `f_3 = a`, `f_4 = b`, and `f_7 = d`::

    sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
    sage: f
    Finite family {3: 'a', 4: 'b', 7: 'd'}
    sage: f[7]
    'd'
    sage: len(f)
    3
    sage: list(f)
    ['a', 'b', 'd']
    sage: [ x for x in f ]
    ['a', 'b', 'd']
    sage: f.keys()
    [3, 4, 7]
    sage: 'b' in f
    True
    sage: 'e' in f
    False

A family can also be constructed by its index set `I` and
a function `f`, as in `(f(i))_{i \in I}`::

    sage: f = Family([3,4,7], lambda i: 2*i)
    sage: f
    Finite family {3: 6, 4: 8, 7: 14}
    sage: f.keys()
    [3, 4, 7]
    sage: f[7]
    14
    sage: list(f)
    [6, 8, 14]
    sage: [x for x in f]
    [6, 8, 14]
    sage: len(f)
    3

By default, all images are computed right away, and stored in an internal
dictionary::

    sage: f = Family((3,4,7), lambda i: 2*i)
    sage: f
    Finite family {3: 6, 4: 8, 7: 14}

Note that this requires all the elements of the list to be
hashable. One can ask instead for the images `f(i)` to be computed
lazily, when needed::

    sage: f = Family([3,4,7], lambda i: 2*i, lazy=True)
    sage: f
    Lazy family (<lambda>(i))_{i in [3, 4, 7]}
    sage: f[7]
    14
    sage: list(f)
    [6, 8, 14]
    sage: [x for x in f]
    [6, 8, 14]

This allows in particular for modeling infinite families::

    sage: f = Family(ZZ, lambda i: 2*i, lazy=True)
    sage: f
    Lazy family (<lambda>(i))_{i in Integer Ring}
    sage: f.keys()
    Integer Ring
    sage: f[1]
    2
    sage: f[-5]
    -10
    sage: i = iter(f)
    sage: next(i), next(i), next(i), next(i), next(i)
    (0, 2, -2, 4, -4)

Note that the ``lazy`` keyword parameter is only needed to force
laziness. Usually it is automatically set to a correct default value (ie:
``False`` for finite data structures and ``True`` for enumerated sets::

    sage: f == Family(ZZ, lambda i: 2*i)
    True

Beware that for those kind of families len(f) is not supposed to
work. As a replacement, use the .cardinality() method::

   sage: f = Family(Permutations(3), attrcall("to_lehmer_code"))
   sage: list(f)
   [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0], [2, 0, 0], [2, 1, 0]]
   sage: f.cardinality()
   6

Caveat: Only certain families with lazy behavior can be pickled. In
particular, only functions that work with Sage's pickle_function
and unpickle_function (in sage.misc.fpickle) will correctly
unpickle. The following two work::

   sage: f = Family(Permutations(3), lambda p: p.to_lehmer_code()); f
   Lazy family (<lambda>(i))_{i in Standard permutations of 3}
   sage: f == loads(dumps(f))
   True

   sage: f = Family(Permutations(3), attrcall("to_lehmer_code")); f
   Lazy family (i.to_lehmer_code())_{i in Standard permutations of 3}
   sage: f == loads(dumps(f))
   True

But this one does not::

   sage: def plus_n(n): return lambda x: x+n
   sage: f = Family([1,2,3], plus_n(3), lazy=True); f
   Lazy family (<lambda>(i))_{i in [1, 2, 3]}
   sage: f == loads(dumps(f))
   Traceback (most recent call last):
   ...
   ValueError: Cannot pickle code objects from closures

Finally, it can occasionally be useful to add some hidden elements
in a family, which are accessible as ``f[i]``, but do not appear in the
keys or the container operations::

    sage: f = Family([3,4,7], lambda i: 2*i, hidden_keys=[2])
    sage: f
    Finite family {3: 6, 4: 8, 7: 14}
    sage: f.keys()
    [3, 4, 7]
    sage: f.hidden_keys()
    [2]
    sage: f[7]
    14
    sage: f[2]
    4
    sage: list(f)
    [6, 8, 14]
    sage: [x for x in f]
    [6, 8, 14]
    sage: len(f)
    3

The following example illustrates when the function is actually
called::

    sage: def compute_value(i):
    ....:     print('computing 2*'+str(i))
    ....:     return 2*i
    sage: f = Family([3,4,7], compute_value, hidden_keys=[2])
    computing 2*3
    computing 2*4
    computing 2*7
    sage: f
    Finite family {3: 6, 4: 8, 7: 14}
    sage: f.keys()
    [3, 4, 7]
    sage: f.hidden_keys()
    [2]
    sage: f[7]
    14
    sage: f[2]
    computing 2*2
    4
    sage: f[2]
    4
    sage: list(f)
    [6, 8, 14]
    sage: [x for x in f]
    [6, 8, 14]
    sage: len(f)
    3

Here is a close variant where the function for the hidden keys is
different from that for the other keys::

    sage: f = Family([3,4,7], lambda i: 2*i, hidden_keys=[2], hidden_function = lambda i: 3*i)
    sage: f
    Finite family {3: 6, 4: 8, 7: 14}
    sage: f.keys()
    [3, 4, 7]
    sage: f.hidden_keys()
    [2]
    sage: f[7]
    14
    sage: f[2]
    6
    sage: list(f)
    [6, 8, 14]
    sage: [x for x in f]
    [6, 8, 14]
    sage: len(f)
    3

Family accept finite and infinite EnumeratedSets as input::

    sage: f = Family(FiniteEnumeratedSet([1,2,3]))
    sage: f
    Family (1, 2, 3)
    sage: f = Family(NonNegativeIntegers())
    sage: f
    Family (Non negative integers)

::

    sage: f = Family(FiniteEnumeratedSet([3,4,7]), lambda i: 2*i)
    sage: f
    Finite family {3: 6, 4: 8, 7: 14}
    sage: f.keys()
    {3, 4, 7}
    sage: f[7]
    14
    sage: list(f)
    [6, 8, 14]
    sage: [x for x in f]
    [6, 8, 14]
    sage: len(f)
    3

TESTS::

    sage: f = Family({1:'a', 2:'b', 3:'c'})
    sage: f
    Finite family {1: 'a', 2: 'b', 3: 'c'}
    sage: f[2]
    'b'
    sage: loads(dumps(f)) == f
    True

::

    sage: f = Family({1:'a', 2:'b', 3:'c'}, lazy=True)
    Traceback (most recent call last):
    ...
    ValueError: lazy keyword only makes sense together with function keyword

::

    sage: f = Family(list(range(1,27)), lambda i: chr(i+96))
    sage: f
    Finite family {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
    8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
    16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
    24: 'x', 25: 'y', 26: 'z'}
    sage: f[2]
    'b'

The factory ``Family`` is supposed to be idempotent. We test this feature here::

    sage: from sage.sets.family import FiniteFamily, LazyFamily, TrivialFamily
    sage: f = FiniteFamily({3: 'a', 4: 'b', 7: 'd'})
    sage: g = Family(f)
    sage: f == g
    True

    sage: f = Family([3,4,7], lambda i: 2*i, hidden_keys=[2])
    sage: g = Family(f)
    sage: f == g
    True

    sage: f = LazyFamily([3,4,7], lambda i: 2*i)
    sage: g = Family(f)
    sage: f == g
    True

    sage: f = TrivialFamily([3,4,7])
    sage: g = Family(f)
    sage: f == g
    True

A family should keep the order of the keys::

    sage: f = Family(["c", "a", "b"], lambda i: 2*i)
    sage: list(f)
    ['cc', 'aa', 'bb']

Even with hidden keys (see :issue:`22955`)::

    sage: f = Family(["c", "a", "b"], lambda i: 2*i,
    ....:           hidden_keys=[5], hidden_function=lambda i: i%2)
    sage: list(f)
    ['cc', 'aa', 'bb']

Only the hidden function is applied to the hidden keys::

    sage: f[5]
    1
"""

class AbstractFamily(sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 425)

        The abstract class for family.

        Any family belongs to a class which inherits from :class:`AbstractFamily`.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def hidden_keys(self) -> Any:
        """AbstractFamily.hidden_keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 431)

        Return the hidden keys of the family, if any.

        EXAMPLES::

            sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
            sage: f.hidden_keys()
            []"""
    @overload
    def hidden_keys(self) -> Any:
        """AbstractFamily.hidden_keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 431)

        Return the hidden keys of the family, if any.

        EXAMPLES::

            sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
            sage: f.hidden_keys()
            []"""
    @overload
    def inverse_family(self) -> Any:
        """AbstractFamily.inverse_family(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 520)

        Return the inverse family, with keys and values exchanged. This
        presumes that there are no duplicate values in ``self``.

        This default implementation is not lazy and therefore will
        only work with not too big finite families. It is also cached
        for the same reason::

            sage: Family({3: 'a', 4: 'b', 7: 'd'}).inverse_family()
            Finite family {'a': 3, 'b': 4, 'd': 7}

            sage: Family((3,4,7)).inverse_family()
            Finite family {3: 0, 4: 1, 7: 2}"""
    @overload
    def inverse_family(self) -> Any:
        """AbstractFamily.inverse_family(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 520)

        Return the inverse family, with keys and values exchanged. This
        presumes that there are no duplicate values in ``self``.

        This default implementation is not lazy and therefore will
        only work with not too big finite families. It is also cached
        for the same reason::

            sage: Family({3: 'a', 4: 'b', 7: 'd'}).inverse_family()
            Finite family {'a': 3, 'b': 4, 'd': 7}

            sage: Family((3,4,7)).inverse_family()
            Finite family {3: 0, 4: 1, 7: 2}"""
    @overload
    def inverse_family(self) -> Any:
        """AbstractFamily.inverse_family(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 520)

        Return the inverse family, with keys and values exchanged. This
        presumes that there are no duplicate values in ``self``.

        This default implementation is not lazy and therefore will
        only work with not too big finite families. It is also cached
        for the same reason::

            sage: Family({3: 'a', 4: 'b', 7: 'd'}).inverse_family()
            Finite family {'a': 3, 'b': 4, 'd': 7}

            sage: Family((3,4,7)).inverse_family()
            Finite family {3: 0, 4: 1, 7: 2}"""
    @overload
    def items(self) -> Any:
        """AbstractFamily.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 467)

        Return an iterator for key-value pairs.

        A key can only appear once, but if the function is not injective, values may
        appear multiple times.

        EXAMPLES::

            sage: f = Family([-2, -1, 0, 1, 2], abs)
            sage: list(f.items())
            [(-2, 2), (-1, 1), (0, 0), (1, 1), (2, 2)]"""
    @overload
    def items(self) -> Any:
        """AbstractFamily.items(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 467)

        Return an iterator for key-value pairs.

        A key can only appear once, but if the function is not injective, values may
        appear multiple times.

        EXAMPLES::

            sage: f = Family([-2, -1, 0, 1, 2], abs)
            sage: list(f.items())
            [(-2, 2), (-1, 1), (0, 0), (1, 1), (2, 2)]"""
    @overload
    def keys(self) -> Any:
        """AbstractFamily.keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 443)

        Return the keys of the family.

        EXAMPLES::

            sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
            sage: sorted(f.keys())
            [3, 4, 7]"""
    @overload
    def keys(self) -> Any:
        """AbstractFamily.keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 443)

        Return the keys of the family.

        EXAMPLES::

            sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
            sage: sorted(f.keys())
            [3, 4, 7]"""
    def map(self, f, name=...) -> Any:
        """AbstractFamily.map(self, f, name=None)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 503)

        Return the family `( f(\\mathtt{self}[i]) )_{i \\in I}`, where
        `I` is the index set of ``self``.

        EXAMPLES::

            sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
            sage: g = f.map(lambda x: x+'1')
            sage: list(g)
            ['a1', 'b1', 'd1']"""
    @overload
    def values(self) -> Any:
        '''AbstractFamily.values(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 455)

        Return the elements (values) of this family.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x + x)
            sage: sorted(f.values())
            [\'aa\', \'bb\', \'cc\']'''
    @overload
    def values(self) -> Any:
        '''AbstractFamily.values(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 455)

        Return the elements (values) of this family.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x + x)
            sage: sorted(f.values())
            [\'aa\', \'bb\', \'cc\']'''
    def zip(self, f, other, name=...) -> Any:
        """AbstractFamily.zip(self, f, other, name=None)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 482)

        Given two families with same index set `I` (and same hidden
        keys if relevant), returns the family
        `( f(self[i], other[i]) )_{i \\in I}`

        .. TODO:: generalize to any number of families and merge with map?

        EXAMPLES::

            sage: f = Family({3: 'a', 4: 'b', 7: 'd'})
            sage: g = Family({3: '1', 4: '2', 7: '3'})
            sage: h = f.zip(lambda x,y: x+y, g)
            sage: list(h)
            ['a1', 'b2', 'd3']"""

class EnumeratedFamily(LazyFamily):
    """File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1414)

        :class:`EnumeratedFamily` turns an enumerated set ``c`` into a family
        indexed by the set `\\{0,\\dots, |c|-1\\}` (or ``NN`` if `|c|` is
        countably infinite).

        Instances should be created via the :func:`Family` factory. See its
        documentation for examples and tests.
    """
    def __init__(self, enumset) -> Any:
        """EnumeratedFamily.__init__(self, enumset)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1423)

        EXAMPLES::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(3))
            sage: TestSuite(f).run()

            sage: f = Family(NonNegativeIntegers())
            sage: TestSuite(f).run()

        TESTS:

        Check that category and keys are set correctly (:issue:`28274`)::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(4))
            sage: f.category()
            Category of finite enumerated sets
            sage: list(f.keys()) == list(range(f.cardinality()))
            True
            sage: Family(Permutations()).keys()
            Non negative integers
            sage: type(Family(NN))
            <class 'sage.sets.family.EnumeratedFamily_with_category'>"""
    @overload
    def cardinality(self) -> Any:
        """EnumeratedFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1493)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(3))
            sage: f.cardinality()
            6

            sage: f = Family(NonNegativeIntegers())
            sage: f.cardinality()
            +Infinity"""
    @overload
    def cardinality(self) -> Any:
        """EnumeratedFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1493)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(3))
            sage: f.cardinality()
            6

            sage: f = Family(NonNegativeIntegers())
            sage: f.cardinality()
            +Infinity"""
    @overload
    def cardinality(self) -> Any:
        """EnumeratedFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1493)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(3))
            sage: f.cardinality()
            6

            sage: f = Family(NonNegativeIntegers())
            sage: f.cardinality()
            +Infinity"""
    def __contains__(self, x) -> Any:
        """EnumeratedFamily.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1483)

        EXAMPLES::

            sage: f = Family(Permutations(3))
            sage: [2,1,3] in f
            True"""
    def __eq__(self, other) -> Any:
        """EnumeratedFamily.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1456)

        EXAMPLES::

            sage: f = Family(Permutations(3))
            sage: g = Family(Permutations(3))
            sage: f == g
            True"""
    def __getitem__(self, i) -> Any:
        """EnumeratedFamily.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1521)

        EXAMPLES::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(3))
            sage: f[1]
            [1, 3, 2]"""
    def __iter__(self) -> Any:
        """EnumeratedFamily.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1510)

        EXAMPLES::

            sage: from sage.sets.family import EnumeratedFamily
            sage: f = EnumeratedFamily(Permutations(3))
            sage: [i for i in f]
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]"""

class FiniteFamily(AbstractFamily):
    '''FiniteFamily(dictionary, keys=None)

    File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 539)

    A :class:`FiniteFamily` is an associative container which models a finite
    family `(f_i)_{i \\in I}`. Its elements `f_i` are therefore its
    values. Instances should be created via the :func:`Family` factory. See its
    documentation for examples and tests.

    EXAMPLES:

    We define the family `(f_i)_{i \\in \\{3,4,7\\}}` with `f_3=a`,
    `f_4=b`, and `f_7=d`::

        sage: from sage.sets.family import FiniteFamily
        sage: f = FiniteFamily({3: \'a\', 4: \'b\', 7: \'d\'})

    Individual elements are accessible as in a usual dictionary::

        sage: f[7]
        \'d\'

    And the other usual dictionary operations are also available::

        sage: len(f)
        3
        sage: f.keys()
        [3, 4, 7]

    However f behaves as a container for the `f_i`\'s::

        sage: list(f)
        [\'a\', \'b\', \'d\']
        sage: [ x for x in f ]
        [\'a\', \'b\', \'d\']

    The order of the elements can be specified using the ``keys`` optional argument::

        sage: f = FiniteFamily({"a": "aa", "b": "bb", "c" : "cc" }, keys = ["c", "a", "b"])
        sage: list(f)
        [\'cc\', \'aa\', \'bb\']'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, dictionary, keys=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 580)

                TESTS::

                    sage: from sage.sets.family import FiniteFamily
                    sage: f = FiniteFamily({3: \'a\', 4: \'b\', 7: \'d\'})
                    sage: TestSuite(f).run()

                Check for bug :issue:`5538`::

                    sage: d = {1:"a", 3:"b", 4:"c"}
                    sage: f = Family(d)
                    sage: d[2] = \'DD\'
                    sage: f
                    Finite family {1: \'a\', 3: \'b\', 4: \'c\'}
            '''
    @overload
    def cardinality(self) -> Any:
        """FiniteFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 766)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import FiniteFamily
            sage: f = FiniteFamily({3: 'a', 4: 'b', 7: 'd'})
            sage: f.cardinality()
            3"""
    @overload
    def cardinality(self) -> Any:
        """FiniteFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 766)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import FiniteFamily
            sage: f = FiniteFamily({3: 'a', 4: 'b', 7: 'd'})
            sage: f.cardinality()
            3"""
    def has_key(self, k) -> bool:
        '''FiniteFamily.has_key(self, k) -> bool

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 677)

        Return whether ``k`` is a key of ``self``.

        EXAMPLES::

            sage: Family({"a":1, "b":2, "c":3}).has_key("a")
            True
            sage: Family({"a":1, "b":2, "c":3}).has_key("d")
            False'''
    @overload
    def keys(self) -> Any:
        '''FiniteFamily.keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 649)

        Return the index set of this family.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x+x)
            sage: f.keys()
            [\'c\', \'a\', \'b\']'''
    @overload
    def keys(self) -> Any:
        '''FiniteFamily.keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 649)

        Return the index set of this family.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x+x)
            sage: f.keys()
            [\'c\', \'a\', \'b\']'''
    @overload
    def values(self) -> Any:
        '''FiniteFamily.values(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 662)

        Return the elements of this family.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x+x)
            sage: f.values()
            [\'cc\', \'aa\', \'bb\']'''
    @overload
    def values(self) -> Any:
        '''FiniteFamily.values(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 662)

        Return the elements of this family.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x+x)
            sage: f.values()
            [\'cc\', \'aa\', \'bb\']'''
    def __bool__(self) -> bool:
        """True if self else False"""
    def __contains__(self, x) -> Any:
        """FiniteFamily.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 740)

        EXAMPLES::

            sage: from sage.sets.family import FiniteFamily
            sage: f = FiniteFamily({3: 'a'})
            sage: 'a' in f
            True
            sage: 'b' in f
            False"""
    def __eq__(self, other) -> bool:
        """FiniteFamily.__eq__(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 690)

        EXAMPLES::

            sage: f = Family({1:'a', 2:'b', 3:'c'})
            sage: g = Family({1:'a', 2:'b', 3:'c'})
            sage: f == g
            True

        TESTS::

            sage: from sage.sets.family import FiniteFamily

            sage: f1 = FiniteFamily({1:'a', 2:'b', 3:'c'}, keys = [1,2,3])
            sage: g1 = FiniteFamily({1:'a', 2:'b', 3:'c'}, keys = [1,2,3])
            sage: h1 = FiniteFamily({1:'a', 2:'b', 3:'c'}, keys = [2,1,3])

            sage: f1 == g1
            True
            sage: f1 == h1
            False
            sage: f1 == f
            False"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, i) -> Any:
        """FiniteFamily.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 791)

        Note that we can't just do self.__getitem__ =
        dictionary.__getitem__ in the __init__ method since Python
        queries the object's type/class for the special methods rather than
        querying the object itself.

        EXAMPLES::

            sage: from sage.sets.family import FiniteFamily
            sage: f = FiniteFamily({3: 'a', 4: 'b', 7: 'd'})
            sage: f[3]
            'a'"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        '''FiniteFamily.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 601)

        Return a hash value for ``self``.

        EXAMPLES::

            sage: f = Family(["c", "a", "b"], lambda x: x+x)
            sage: hash(f) == hash(f)
            True
            sage: f2 = Family(["a", "c", "b"], lambda x: x+x)
            sage: hash(f) == hash(f2)
            True
            sage: g = Family(["b", "c", "a"], lambda x: x+x+x)
            sage: hash(f) == hash(g)
            False

        ::

            sage: f = Family({1:[1,2]})
            sage: hash(f) == hash(f)
            True'''
    def __iter__(self) -> Any:
        """FiniteFamily.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 779)

        EXAMPLES::

            sage: from sage.sets.family import FiniteFamily
            sage: f = FiniteFamily({3: 'a'})
            sage: i = iter(f)
            sage: next(i)
            'a'"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """FiniteFamily.__len__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 753)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import FiniteFamily
            sage: f = FiniteFamily({3: 'a', 4: 'b', 7: 'd'})
            sage: len(f)
            3"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class FiniteFamilyWithHiddenKeys(FiniteFamily):
    """File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 832)

        A close variant of :class:`FiniteFamily` where the family contains some
        hidden keys whose corresponding values are computed lazily (and
        remembered). Instances should be created via the :func:`Family` factory.
        See its documentation for examples and tests.

        Caveat: Only instances of this class whose functions are compatible
        with :mod:`sage.misc.fpickle` can be pickled.
    """
    def __init__(self, dictionary, hidden_keys, hidden_function, keys=...) -> Any:
        """FiniteFamilyWithHiddenKeys.__init__(self, dictionary, hidden_keys, hidden_function, keys=None)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 842)

        EXAMPLES::

            sage: f = Family([3,4,7], lambda i: 2*i, hidden_keys=[2])
            sage: TestSuite(f).run()"""
    def hidden_keys(self) -> Any:
        """FiniteFamilyWithHiddenKeys.hidden_keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 884)

        Return ``self``'s hidden keys.

        EXAMPLES::

            sage: f = Family([3,4,7], lambda i: 2*i, hidden_keys=[2])
            sage: f.hidden_keys()
            [2]"""
    def __getitem__(self, i) -> Any:
        """FiniteFamilyWithHiddenKeys.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 858)

        EXAMPLES::

            sage: f = Family([3,4,7], lambda i: 2*i, hidden_keys=[2])
            sage: f[3]
            6
            sage: f[2]
            4
            sage: f[5]
            Traceback (most recent call last):
            ...
            KeyError"""

class LazyFamily(AbstractFamily):
    """File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 940)

        A LazyFamily(I, f) is an associative container which models the
        (possibly infinite) family `(f(i))_{i \\in I}`.

        Instances should be created via the :func:`Family` factory. See its
        documentation for examples and tests.
    """
    def __init__(self, set, function, name=...) -> Any:
        """LazyFamily.__init__(self, set, function, name=None)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 948)

        TESTS::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i); f
            Lazy family (<lambda>(i))_{i in [3, 4, 7]}
            sage: TestSuite(f).run()

        Check for :issue:`5538`::

            sage: l = [3,4,7]
            sage: f = LazyFamily(l, lambda i: 2*i)
            sage: l[1] = 18
            sage: f
            Lazy family (<lambda>(i))_{i in [3, 4, 7]}"""
    @overload
    def cardinality(self) -> Any:
        """LazyFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1109)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f.cardinality()
            3
            sage: l = LazyFamily(NonNegativeIntegers(), lambda i: 2*i)
            sage: l.cardinality()
            +Infinity

        TESTS:

        Check that :issue:`15195` is fixed::

            sage: C = cartesian_product([PositiveIntegers(), [1,2,3]])
            sage: C.cardinality()
            +Infinity
            sage: F = Family(C, lambda x: x)
            sage: F.cardinality()
            +Infinity
    """
    @overload
    def cardinality(self) -> Any:
        """LazyFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1109)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f.cardinality()
            3
            sage: l = LazyFamily(NonNegativeIntegers(), lambda i: 2*i)
            sage: l.cardinality()
            +Infinity

        TESTS:

        Check that :issue:`15195` is fixed::

            sage: C = cartesian_product([PositiveIntegers(), [1,2,3]])
            sage: C.cardinality()
            +Infinity
            sage: F = Family(C, lambda x: x)
            sage: F.cardinality()
            +Infinity
    """
    @overload
    def cardinality(self) -> Any:
        """LazyFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1109)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f.cardinality()
            3
            sage: l = LazyFamily(NonNegativeIntegers(), lambda i: 2*i)
            sage: l.cardinality()
            +Infinity

        TESTS:

        Check that :issue:`15195` is fixed::

            sage: C = cartesian_product([PositiveIntegers(), [1,2,3]])
            sage: C.cardinality()
            +Infinity
            sage: F = Family(C, lambda x: x)
            sage: F.cardinality()
            +Infinity
    """
    @overload
    def cardinality(self) -> Any:
        """LazyFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1109)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f.cardinality()
            3
            sage: l = LazyFamily(NonNegativeIntegers(), lambda i: 2*i)
            sage: l.cardinality()
            +Infinity

        TESTS:

        Check that :issue:`15195` is fixed::

            sage: C = cartesian_product([PositiveIntegers(), [1,2,3]])
            sage: C.cardinality()
            +Infinity
            sage: F = Family(C, lambda x: x)
            sage: F.cardinality()
            +Infinity
    """
    @overload
    def cardinality(self) -> Any:
        """LazyFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1109)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f.cardinality()
            3
            sage: l = LazyFamily(NonNegativeIntegers(), lambda i: 2*i)
            sage: l.cardinality()
            +Infinity

        TESTS:

        Check that :issue:`15195` is fixed::

            sage: C = cartesian_product([PositiveIntegers(), [1,2,3]])
            sage: C.cardinality()
            +Infinity
            sage: F = Family(C, lambda x: x)
            sage: F.cardinality()
            +Infinity
    """
    def keys(self) -> Any:
        """LazyFamily.keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1096)

        Return ``self``'s keys.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f.keys()
            [3, 4, 7]"""
    def __bool__(self) -> Any:
        """LazyFamily.__bool__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 986)

        Return if ``self`` is empty or not.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: bool(f)
            True
            sage: g = LazyFamily([], lambda i: 2*i)
            sage: bool(g)
            False
            sage: h = Family(ZZ, lambda x: x+x)
            sage: bool(h)
            True"""
    def __contains__(self, x) -> Any:
        """LazyFamily.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1151)

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: 3 in f, 14 in f
            (False, True)

        By default this expands the lazy family, which is only done for
        families known to be finite::

            sage: 5 in LazyFamily(NonNegativeIntegers(), lambda i: 2*i)
            Traceback (most recent call last):
            ...
            ValueError: family must be finite to check containment"""
    def __eq__(self, other) -> Any:
        """LazyFamily.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1038)

        WARNING: Since there is no way to compare function, we only compare
        their name.

        TESTS::

            sage: from sage.sets.family import LazyFamily
            sage: fun = lambda i: 2*i
            sage: f = LazyFamily([3,4,7], fun)
            sage: g = LazyFamily([3,4,7], fun)
            sage: f == g
            True"""
    def __getitem__(self, i) -> Any:
        """LazyFamily.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1172)

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: f[3]
            6

        TESTS::

            sage: f[5]
            10"""
    def __hash__(self) -> Any:
        """LazyFamily.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1005)

        Return a hash value for ``self``.

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: hash(f) == hash(f)
            True
            sage: g = LazyFamily(ZZ, lambda i: 2*i)
            sage: hash(g) == hash(g)
            True
            sage: h = LazyFamily(ZZ, lambda i: 2*i, name='foo')
            sage: hash(h) == hash(h)
            True

        ::

            sage: class X():
            ....:     def __call__(self, x):
            ....:         return x
            ....:     __hash__ = None
            sage: f = Family([1,2,3], X())
            sage: hash(f) == hash(f)
            True"""
    def __iter__(self) -> Any:
        """LazyFamily.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1139)

        EXAMPLES::

            sage: from sage.sets.family import LazyFamily
            sage: f = LazyFamily([3,4,7], lambda i: 2*i)
            sage: [i for i in f]
            [6, 8, 14]"""

class TrivialFamily(AbstractFamily):
    """File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1239)

        :class:`TrivialFamily` turns a list/tuple `c` into a family indexed by the
        set `\\{0, \\dots, |c|-1\\}`.

        Instances should be created via the :func:`Family` factory. See its
        documentation for examples and tests.
    """
    def __init__(self, enumeration) -> Any:
        """TrivialFamily.__init__(self, enumeration)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1247)

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily((3,4,7)); f
            Family (3, 4, 7)
            sage: f = TrivialFamily([3,4,7]); f
            Family (3, 4, 7)
            sage: TestSuite(f).run()"""
    @overload
    def cardinality(self) -> Any:
        """TrivialFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1325)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily([3,4,7])
            sage: f.cardinality()
            3"""
    @overload
    def cardinality(self) -> Any:
        """TrivialFamily.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1325)

        Return the number of elements in ``self``.

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily([3,4,7])
            sage: f.cardinality()
            3"""
    def keys(self) -> Any:
        """TrivialFamily.keys(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1312)

        Return ``self``'s keys.

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily([3,4,7])
            sage: f.keys()
            [0, 1, 2]"""
    def map(self, f, name=...) -> Any:
        """TrivialFamily.map(self, f, name=None)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1396)

        Return the family `( f(\\mathtt{self}[i]) )_{i \\in I}`,
        where `I` is the index set of ``self``.

        The result is again a :class:`TrivialFamily`.

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily(['a', 'b', 'd'])
            sage: g = f.map(lambda x: x + '1'); g
            Family ('a1', 'b1', 'd1')"""
    def __bool__(self) -> Any:
        """TrivialFamily.__bool__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1261)

        Return if ``self`` is empty or not.

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily((3,4,7))
            sage: bool(f)
            True
            sage: g = Family([])
            sage: bool(g)
            False"""
    def __contains__(self, x) -> Any:
        """TrivialFamily.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1349)

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily([3,4,7])
            sage: 3 in f
            True
            sage: 5 in f
            False"""
    def __eq__(self, other) -> Any:
        """TrivialFamily.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1277)

        TESTS::

            sage: f = Family((3,4,7))
            sage: g = Family([3,4,7])
            sage: f == g
            True"""
    def __getitem__(self, i) -> Any:
        """TrivialFamily.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1362)

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily([3,4,7])
            sage: f[1]
            4"""
    def __hash__(self) -> Any:
        """TrivialFamily.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1289)

        Return a hash value for ``self``.

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily((3,4,7))
            sage: hash(f) == hash(f)
            True"""
    def __iter__(self) -> Any:
        """TrivialFamily.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/sets/family.pyx (starting at line 1338)

        EXAMPLES::

            sage: from sage.sets.family import TrivialFamily
            sage: f = TrivialFamily([3,4,7])
            sage: [i for i in f]
            [3, 4, 7]"""
