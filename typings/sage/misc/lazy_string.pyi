import _cython_3_2_1
from _typeshed import Incomplete
from typing import Any, ClassVar

is_lazy_string: _cython_3_2_1.cython_function_or_method
lazy_string: _cython_3_2_1.cython_function_or_method

class _LazyString:
    '''_LazyString(f, args, kwargs)

    File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 136)

    Lazy class for strings created by a function call or a format string.

    INPUT:

    - ``f`` -- either a callable or a (format) string
    - ``args`` -- tuple of arguments that are given to ``f``, either by calling
      or by applying it as a format string
    - ``kwargs`` -- dictionary of optional arguments, that are forwarded to ``f``
      if it is a callable

    .. NOTE::

        Evaluation of ``f`` is postponed until it becomes necessary, e.g., for
        comparison. The result of evaluation is not cached. The proxy
        implementation attempts to be as complete as possible, so that the
        lazy objects should mostly work as expected, for example for sorting.

        The function :func:`lazy_string` creates lazy strings in a slightly more
        convenient way, because it is then not needed to provide the arguments as
        tuple and dictionary.

    EXAMPLES::

        sage: from sage.misc.lazy_string import lazy_string, _LazyString
        sage: f = lambda x: "laziness in the " + repr(x)
        sage: s = lazy_string(f, ZZ); s
        l\'laziness in the Integer Ring\'
        sage: lazy_string("laziness in the %s", ZZ)
        l\'laziness in the Integer Ring\'

    Here, we demonstrate that the evaluation is postponed until the value is
    needed, and that the result is not cached. Also, we create a lazy string directly,
    without calling :func:`lazy_string`::

        sage: class C:
        ....:     def __repr__(self):
        ....:         print("determining string representation")
        ....:         return "a test"
        sage: c = C()
        sage: s = _LazyString("this is %s", (c,), {})
        sage: s
        determining string representation
        l\'this is a test\'
        sage: s == \'this is a test\'
        determining string representation
        True'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    value: Incomplete
    def __init__(self, f, args, kwargs) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 185)

                INPUT:

                - ``f`` -- either a callable or a (format) string
                - ``args`` -- tuple of arguments that are given to ``f``, either by calling
                  or by applying it as a format string
                - ``kwargs`` -- dictionary of optional arguments, that are forwarded to ``f``
                  if it is a callable

                EXAMPLES::

                    sage: from sage.misc.lazy_string import lazy_string
                    sage: f = lambda x: "laziness" + repr(x)
                    sage: s = lazy_string(f, 5); s
                    l\'laziness5\'
                    sage: lazy_string("This is %s", ZZ)
                    l\'This is Integer Ring\'
        '''
    def update_lazy_string(self, args, kwds) -> Any:
        '''_LazyString.update_lazy_string(self, args, kwds)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 507)

        Change this lazy string in-place.

        INPUT:

        - ``args`` -- tuple
        - ``kwds`` -- dictionary

        .. NOTE::

            Lazy strings are not hashable, and thus an in-place change is
            allowed.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.misc.lazy_string import lazy_string
            sage: def f(op, A, B):
            ....:     return "unsupported operand parent(s) for %s: \'%s\' and \'%s\'" % (op, A, B)
            sage: R = GF(5)
            sage: S = GF(3)
            sage: D = lazy_string(f, \'+\', R, S); D
            l"unsupported operand parent(s) for +: \'Finite Field of size 5\' and \'Finite Field of size 3\'"
            sage: D.update_lazy_string((\'+\', S, R), {})

        Apparently, the lazy string got changed in-place::

            sage: D                                                                     # needs sage.rings.finite_rings
            l"unsupported operand parent(s) for +: \'Finite Field of size 3\' and \'Finite Field of size 5\'"

        TESTS::

            sage: D.update_lazy_string(None, None)                                      # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: Expected tuple, got NoneType'''
    def __add__(self, other) -> Any:
        '''_LazyString.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 332)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: s + " supreme"
            \'laziness supreme\''''
    def __bool__(self) -> bool:
        """True if self else False"""
    def __contains__(self, key) -> Any:
        '''_LazyString.__contains__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 234)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: \'zi\' in s
            True
            sage: \'ni\' in s
            False'''
    def __copy__(self) -> Any:
        '''_LazyString.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 480)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: copy(s) is s
            True'''
    def __dir__(self) -> Any:
        '''_LazyString.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 262)

        We assume that the underlying value provides the methods of a
        unicode string.

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: "split" in dir(s) # indirect doctest
            True'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __fspath__(self) -> Any:
        '''_LazyString.__fspath__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 313)

        Return the file system representation of ``self``, assuming that
        ``self`` is a path.

        This is for Python 3 compatibility: see :issue:`24046`, and also
        :pep:`519` and
        https://docs.python.org/3/library/os.html#os.fspath

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "/dev/null"
            sage: s = lazy_string(f)
            sage: os.fspath(s)
            \'/dev/null\''''
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, key) -> Any:
        '''_LazyString.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 468)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: s[4]
            \'n\''''
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __iter__(self) -> Any:
        '''_LazyString.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 277)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: "".join(list(s)) # indirect doctest
            \'laziness\''''
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        '''_LazyString.__len__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 289)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: len(s)
            8'''
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, other) -> Any:
        '''_LazyString.__mod__(self, other)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 347)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laz%sss"
            sage: s = lazy_string(f)
            sage: s % "ine"
            \'laziness\'
            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "ine"
            sage: s = lazy_string(f)
            sage: "laz%sss" % s
            \'laziness\''''
    def __mul__(self, other) -> Any:
        '''_LazyString.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 367)

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: s * 2
            \'lazinesslaziness\'
            sage: 2 * s
            \'lazinesslaziness\''''
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        '''_LazyString.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/lazy_string.pyx (starting at line 448)

        Pickling.

        EXAMPLES::

            sage: from sage.misc.lazy_string import lazy_string
            sage: f = lambda: "laziness"
            sage: s = lazy_string(f)
            sage: TestSuite(s).run() # indirect doctest'''
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
