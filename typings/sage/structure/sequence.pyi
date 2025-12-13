from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.structure.sage_object import SageObject as SageObject

def Sequence(x, universe=None, check: bool = True, immutable: bool = False, cr: bool = False, cr_str=None, use_sage_types: bool = False):
    '''
    A mutable list of elements with a common guaranteed universe,
    which can be set immutable.

    A universe is either an object that supports coercion (e.g., a
    parent), or a category.

    INPUT:

    - ``x`` -- list or tuple instance

    - ``universe`` -- (default: ``None``) the universe of elements; if ``None``
      determined using canonical coercions and the entire list of elements.
      If list is empty, is category ``Objects()`` of all objects.

    - ``check`` -- boolean (default: ``True``); whether to coerce the elements of x
      into the universe

    - ``immutable`` -- boolean (default: ``True``); whether or not this sequence is
      immutable

    - ``cr`` -- boolean (default: ``False``); if ``True``, then print a carriage return
      after each comma when calling ``repr()`` on this sequence (see note below)

    - ``cr_str`` -- boolean (default: same as ``cr``); if ``True``, then print a carriage return
      after each comma when calling ``str()`` on this sequence (see note below)

    - ``use_sage_types`` -- boolean (default: ``False``); if ``True``, coerce the
      built-in Python numerical types int, float, complex to the corresponding
      Sage types (this makes functions like ``vector()`` more flexible)

    OUTPUT: a sequence

    EXAMPLES::

        sage: v = Sequence(range(10))
        sage: v.universe()
        <class \'int\'>
        sage: v
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    We can request that the built-in Python numerical types be coerced
    to Sage objects::

        sage: v = Sequence(range(10), use_sage_types=True)
        sage: v.universe()
        Integer Ring
        sage: v
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    You can also use seq for "Sequence", which is identical to using
    Sequence::

        sage: v = seq([1,2,1/1]); v
        [1, 2, 1]
        sage: v.universe()
        Rational Field

    Note that assignment coerces if possible,::

        sage: v = Sequence(range(10), ZZ)
        sage: a = QQ(5)
        sage: v[3] = a
        sage: parent(v[3])
        Integer Ring
        sage: parent(a)
        Rational Field
        sage: v[3] = 2/3
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer

    Sequences can be used absolutely anywhere lists or tuples can be used::

        sage: isinstance(v, list)
        True

    Sequence can be immutable, so entries can\'t be changed::

        sage: v = Sequence([1,2,3], immutable=True)
        sage: v.is_immutable()
        True
        sage: v[0] = 5
        Traceback (most recent call last):
        ...
        ValueError: object is immutable; please change a copy instead.

    Only immutable sequences are hashable (unlike Python lists),
    though the hashing is potentially slow, since it first involves
    conversion of the sequence to a tuple, and returning the hash of
    that.::

        sage: v = Sequence(range(10), ZZ, immutable=True)
        sage: hash(v) == hash(tuple(range(10)))
        True


    If you really know what you are doing, you can circumvent the type
    checking (for an efficiency gain)::

        sage: list.__setitem__(v, int(1), 2/3)        # bad circumvention
        sage: v
        [0, 2/3, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: list.__setitem__(v, int(1), int(2))     # not so bad circumvention

    You can make a sequence with a new universe from an old sequence.::

        sage: w = Sequence(v, QQ)
        sage: w
        [0, 2, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: w.universe()
        Rational Field
        sage: w[1] = 2/3
        sage: w
        [0, 2/3, 2, 3, 4, 5, 6, 7, 8, 9]

    The default universe for any sequence, if no compatible parent structure
    can be found, is the universe of all Sage objects.

    This example illustrates how every element of a list is taken into account
    when constructing a sequence.::

        sage: v = Sequence([1, 7, 6, GF(5)(3)]); v
        [1, 2, 1, 3]
        sage: v.universe()
        Finite Field of size 5

    .. NOTE::

        ``cr`` and ``cr_str`` is not recommended (because IPython\'s pretty printer is used);
        nevertheless it is kept for backwards compatibility.

        By default ``Sequence`` are printed using IPython\'s pretty printer,
        so ``cr`` and ``cr_str`` are not taken into account at all::

            sage: Sequence([1, 2, 3], cr=False)
            [1, 2, 3]
            sage: Sequence([1, 2, 3], cr=True)
            [1, 2, 3]

        Nevertheless, before the pretty printer exists, ``repr()`` is used.
        Now ``cr`` and ``cr_str`` still affects the behavior of ``repr()`` and ``str()``::

            sage: repr(Sequence([1, 2, 3], cr=False))
            \'[1, 2, 3]\'
            sage: repr(Sequence([1, 2, 3], cr=True))
            \'[\\n1,\\n2,\\n3\\n]\'

        In any case, this behavior should probably not be relied upon.

    TESTS::

        sage: Sequence(["a"], universe=ZZ)
        Traceback (most recent call last):
        ...
        TypeError: unable to convert a to an element of Integer Ring

    Here are some tests for ``cr`` and ``cr_str``, even though they shouldn\'t be used.
    ``cr_str`` can be weird in this case, but we keep the current implementation
    (the feature is not recommended anyway so it doesn\'t make much difference)::

        sage: str(Sequence([1, 2, 3], cr=True, cr_str=True))
        \'[\\n1,\\n2,\\n3\\n]\'
        sage: str(Sequence([1, 2, 3], cr=True, cr_str=False))
        \'[\\n1,\\n2,\\n3\\n]\'

    In the opposite case, ``cr_str`` works fine::

        sage: str(Sequence([1, 2, 3], cr=False, cr_str=False))
        \'[1, 2, 3]\'
        sage: str(Sequence([1, 2, 3], cr=False, cr_str=True))
        \'[\\n1,\\n2,\\n3\\n]\'
        sage: repr(Sequence([1, 2, 3], cr=False, cr_str=False))
        \'[1, 2, 3]\'
        sage: repr(Sequence([1, 2, 3], cr=False, cr_str=True))
        \'[1, 2, 3]\'
    '''

class Sequence_generic(SageObject, list):
    '''
    A mutable list of elements with a common guaranteed universe,
    which can be set immutable.

    A universe is either an object that supports coercion (e.g., a parent),
    or a category.

    INPUT:

    - ``x`` -- list or tuple instance

    - ``universe`` -- (default: ``None``) the universe of elements; if ``None``
      determined using canonical coercions and the entire list of elements.
      If list is empty, is category ``Objects()`` of all objects.

    - ``check`` -- boolean (default: ``True``); whether to coerce the elements of x
      into the universe

    - ``immutable`` -- boolean (default: ``True``); whether or not this sequence is
      immutable

    - ``cr``, ``cr_str`` -- see :func:`Sequence`

    - ``use_sage_types`` -- boolean (default: ``False``); if ``True``, coerce the
      built-in Python numerical types int, float, complex to the corresponding
      Sage types (this makes functions like ``vector()`` more flexible)

    OUTPUT: a sequence

    EXAMPLES::

        sage: v = Sequence(range(10))
        sage: v.universe()
        <class \'int\'>
        sage: v
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    We can request that the built-in Python numerical types be coerced
    to Sage objects::

        sage: v = Sequence(range(10), use_sage_types=True)
        sage: v.universe()
        Integer Ring
        sage: v
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    You can also use seq for "Sequence", which is identical to using Sequence::

        sage: v = seq([1,2,1/1]); v
        [1, 2, 1]
        sage: v.universe()
        Rational Field

    Note that assignment coerces if possible,

    ::

        sage: v = Sequence(range(10), ZZ)
        sage: a = QQ(5)
        sage: v[3] = a
        sage: parent(v[3])
        Integer Ring
        sage: parent(a)
        Rational Field
        sage: v[3] = 2/3
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer

    Sequences can be used absolutely anywhere lists or tuples can be used::

        sage: isinstance(v, list)
        True

    Sequence can be immutable, so entries can\'t be changed::

        sage: v = Sequence([1,2,3], immutable=True)
        sage: v.is_immutable()
        True
        sage: v[0] = 5
        Traceback (most recent call last):
        ...
        ValueError: object is immutable; please change a copy instead.

    Only immutable sequences are hashable (unlike Python lists),
    though the hashing is potentially slow, since it first involves
    conversion of the sequence to a tuple, and returning the hash of
    that.

    ::

        sage: v = Sequence(range(10), ZZ, immutable=True)
        sage: hash(v) == hash(tuple(range(10)))
        True


    If you really know what you are doing, you can circumvent the type
    checking (for an efficiency gain)::

        sage: list.__setitem__(v, int(1), 2/3)        # bad circumvention
        sage: v
        [0, 2/3, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: list.__setitem__(v, int(1), int(2))     # not so bad circumvention

    You can make a sequence with a new universe from an old sequence.

    ::

        sage: w = Sequence(v, QQ)
        sage: w
        [0, 2, 2, 3, 4, 5, 6, 7, 8, 9]
        sage: w.universe()
        Rational Field
        sage: w[1] = 2/3
        sage: w
        [0, 2/3, 2, 3, 4, 5, 6, 7, 8, 9]

    The default universe for any sequence, if no compatible parent structure
    can be found, is the universe of all Sage objects.

    This example illustrates how every element of a list is taken into account
    when constructing a sequence.

    ::

        sage: v = Sequence([1, 7, 6, GF(5)(3)]); v
        [1, 2, 1, 3]
        sage: v.universe()
        Finite Field of size 5
    '''
    def __init__(self, x, universe=None, check: bool = True, immutable: bool = False, cr: bool = False, cr_str=None, use_sage_types: bool = False) -> None:
        """
        Create a sequence.

        EXAMPLES::

            sage: Sequence([1..5])
            [1, 2, 3, 4, 5]
            sage: a = Sequence([1..3], universe=QQ, check=False, immutable=True, cr=True, cr_str=False, use_sage_types=True)
            sage: a
            [1, 2, 3]
            sage: a = Sequence([1..5], universe=QQ, check=False, immutable=True, cr_str=True, use_sage_types=True)
            sage: a
            [1, 2, 3, 4, 5]
            sage: a._Sequence_generic__cr_str
            True
            sage: a.__str__()
            '[\\n1,\\n2,\\n3,\\n4,\\n5\\n]'
        """
    def reverse(self) -> None:
        """
        Reverse the elements of self, in place.

        EXAMPLES::

            sage: B = Sequence([1,2,3])
            sage: B.reverse(); B
            [3, 2, 1]
        """
    def __setitem__(self, n, value) -> None:
        """
        EXAMPLES::

            sage: a = Sequence([1..5])
            sage: a[2] = 19
            sage: a
            [1, 2, 19, 4, 5]
            sage: a[2] = 'hello'
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'hello' to an integer
            sage: a[2] = '5'
            sage: a
            [1, 2, 5, 4, 5]
            sage: v = Sequence([1,2,3,4], immutable=True)
            sage: v[1:3] = [5,7]
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: v = Sequence([1,2,3,4])
            sage: v[1:3] = [5, 3/1]
            sage: v
            [1, 5, 3, 4]
            sage: type(v[2])
            <class 'sage.rings.integer.Integer'>
        """
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: v = Sequence([1,2,3,4], immutable=True)
            sage: w = v[2:]
            sage: w
            [3, 4]
            sage: type(w)
            <class 'sage.structure.sequence.Sequence_generic'>
            sage: w[0] = 5; w
            [5, 4]
            sage: v
            [1, 2, 3, 4]
        """
    def __getslice__(self, i, j): ...
    def __setslice__(self, i, j, value): ...
    def append(self, x) -> None:
        """
        EXAMPLES::

            sage: v = Sequence([1,2,3,4], immutable=True)
            sage: v.append(34)
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: v = Sequence([1/3,2,3,4])
            sage: v.append(4)
            sage: type(v[4])
            <class 'sage.rings.rational.Rational'>
        """
    def extend(self, iterable) -> None:
        """
        Extend list by appending elements from the iterable.

        EXAMPLES::

            sage: B = Sequence([1,2,3])
            sage: B.extend(range(4))
            sage: B
            [1, 2, 3, 0, 1, 2, 3]
        """
    def insert(self, index, object) -> None:
        """
        Insert object before index.

        EXAMPLES::

            sage: B = Sequence([1,2,3])
            sage: B.insert(10, 5)
            sage: B
            [1, 2, 3, 5]
        """
    def pop(self, index: int = -1):
        """
        Remove and return item at index ``index`` (default: last).

        EXAMPLES::

            sage: B = Sequence([1,2,3])
            sage: B.pop(1)
            2
            sage: B
            [1, 3]
        """
    def remove(self, value) -> None:
        """
        Remove first occurrence of ``value``.

        EXAMPLES::

            sage: B = Sequence([1,2,3])
            sage: B.remove(2)
            sage: B
            [1, 3]
        """
    def sort(self, key=None, reverse: bool = False) -> None:
        """
        Sort this list *IN PLACE*.

        INPUT:

        - ``key`` -- see Python ``list sort``

        - ``reverse`` -- see Python ``list sort``

        EXAMPLES::

            sage: B = Sequence([3,2,1/5])
            sage: B.sort()
            sage: B
            [1/5, 2, 3]
            sage: B.sort(reverse=True); B
            [3, 2, 1/5]
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: a = Sequence([1..5])
            sage: a.__hash__()
            Traceback (most recent call last):
            ...
            ValueError: mutable sequences are unhashable
            sage: a[0] = 10
            sage: a.set_immutable()
            sage: a.__hash__() == hash(a) == hash(tuple(a))
            True
        """
    def universe(self):
        """
        Return the universe of the sequence.

        EXAMPLES::

            sage: Sequence([1, 2/3, -2/5]).universe()
            Rational Field
            sage: Sequence([1, 2/3, '-2/5']).universe()
            Category of objects
        """
    def set_immutable(self) -> None:
        """
        Make this object immutable, so it can never again be changed.

        EXAMPLES::

            sage: v = Sequence([1, 2, 3, 4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.set_immutable()
            sage: v[3] = 7
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
        """
    def is_immutable(self):
        """
        Return ``True`` if this object is immutable (can not be changed)
        and ``False`` if it is not.

        To make this object immutable use :meth:`set_immutable`.

        EXAMPLES::

            sage: v = Sequence([1, 2, 3, 4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_immutable()
            False
            sage: v.set_immutable()
            sage: v.is_immutable()
            True
        """
    def is_mutable(self):
        """
        EXAMPLES::

            sage: a = Sequence([1, 2/3, -2/5])
            sage: a.is_mutable()
            True
            sage: a[0] = 100
            sage: type(a[0])
            <class 'sage.rings.rational.Rational'>
            sage: a.set_immutable()
            sage: a[0] = 50
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead.
            sage: a.is_mutable()
            False
        """
    def __reduce__(self):
        """
        Implement pickling for sequences.

        TESTS::

            sage: v = Sequence([1..5])
            sage: w = loads(dumps(v))
            sage: v == w
            True
            sage: w.is_mutable()
            True
            sage: v.set_immutable()
            sage: w = loads(dumps(v))
            sage: w.is_mutable()
            False
        """
    def __copy__(self):
        """
        Return a copy of this sequence.

        EXAMPLES::

            sage: s = seq(range(10))
            sage: t = copy(s)
            sage: t == s
            True
            sage: t.is_immutable() == s.is_immutable()
            True
            sage: t.is_mutable() == s.is_mutable()
            True
        """
    def __getattr__(self, name):
        """
        Strictly for unpickling old 'Sequences'.

        INPUT:

        - ``name`` -- some string

        TESTS::

            sage: S = Sequence([])
            sage: del S._Sequence_generic__universe
            sage: S.universe()
            Traceback (most recent call last):
            ...
            AttributeError: 'Sequence_generic' object has no attribute '_Sequence_generic__universe'...
            sage: S._Sequence__universe = 'foobar'
            sage: S.universe()
            'foobar'

        We test that :issue:`13998` is fixed::

            sage: S = Sequence([])
            sage: S.set_immutable()
            sage: del S._Sequence_generic__hash
            sage: hash(S)
            Traceback (most recent call last):
            ...
            AttributeError: 'Sequence_generic' object has no attribute '_Sequence_generic__hash'...
            sage: S._Sequence__hash = int(34)
            sage: hash(S)
            34
        """
seq = Sequence
