import _cython_3_2_1
from sage.misc.decorators import sage_wraps as sage_wraps
from typing import Any, ClassVar, overload

require_immutable: _cython_3_2_1.cython_function_or_method
require_mutable: _cython_3_2_1.cython_function_or_method

class Mutability:
    """Mutability(is_immutable=False)

    File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 18)

    Class to mix in mutability feature.

    EXAMPLES::

        sage: class A(SageObject, Mutability):
        ....:     def __init__(self, val):
        ....:         self._val = val
        ....:     def change(self, val):
        ....:         self._require_mutable()
        ....:         self._val = val
        ....:     def __hash__(self):
        ....:         self._require_immutable()
        ....:         return hash(self._val)
        sage: a = A(4)
        sage: a._val
        4
        sage: a.change(6); a._val
        6
        sage: hash(a)
        Traceback (most recent call last):
        ...
        ValueError: object is mutable; please make it immutable first
        sage: a.set_immutable()
        sage: a.change(4)
        Traceback (most recent call last):
        ...
        ValueError: object is immutable; please change a copy instead
        sage: hash(a)
        6"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, val) -> Any:
        """File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 51)

                TESTS::

                    sage: class A(SageObject, Mutability):
                    ....:     def __init__(self, val):
                    ....:         self._val = val
                    ....:     def change(self, val):
                    ....:         self._require_mutable()
                    ....:         self._val = val
                    ....:     def __hash__(self):
                    ....:         self._require_immutable()
                    ....:         return hash(self._val)
                    sage: a = A(4)
                    sage: TestSuite(a).run(skip ='_test_pickling')
        """
    @overload
    def is_immutable(self) -> bool:
        """Mutability.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 136)

        Return ``True`` if this object is immutable (cannot be changed)
        and ``False`` if it is not.

        To make this object immutable use self.set_immutable().

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_immutable()
            False
            sage: v.set_immutable()
            sage: v.is_immutable()
            True"""
    @overload
    def is_immutable(self) -> Any:
        """Mutability.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 136)

        Return ``True`` if this object is immutable (cannot be changed)
        and ``False`` if it is not.

        To make this object immutable use self.set_immutable().

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_immutable()
            False
            sage: v.set_immutable()
            sage: v.is_immutable()
            True"""
    @overload
    def is_immutable(self) -> Any:
        """Mutability.is_immutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 136)

        Return ``True`` if this object is immutable (cannot be changed)
        and ``False`` if it is not.

        To make this object immutable use self.set_immutable().

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_immutable()
            False
            sage: v.set_immutable()
            sage: v.is_immutable()
            True"""
    @overload
    def is_mutable(self) -> bool:
        """Mutability.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 157)

        Return ``True`` if this object is mutable (can be changed)
        and ``False`` if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_mutable()
            True
            sage: v.set_immutable()
            sage: v.is_mutable()
            False"""
    @overload
    def is_mutable(self) -> Any:
        """Mutability.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 157)

        Return ``True`` if this object is mutable (can be changed)
        and ``False`` if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_mutable()
            True
            sage: v.set_immutable()
            sage: v.is_mutable()
            False"""
    @overload
    def is_mutable(self) -> Any:
        """Mutability.is_mutable(self) -> bool

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 157)

        Return ``True`` if this object is mutable (can be changed)
        and ``False`` if it is not.

        To make this object immutable use ``self.set_immutable()``.

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.is_mutable()
            True
            sage: v.set_immutable()
            sage: v.is_mutable()
            False"""
    @overload
    def set_immutable(self) -> Any:
        """Mutability.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 118)

        Make this object immutable, so it can never again be changed.

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.set_immutable()
            sage: v[3] = 7
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead."""
    @overload
    def set_immutable(self) -> Any:
        """Mutability.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/structure/mutability.pyx (starting at line 118)

        Make this object immutable, so it can never again be changed.

        EXAMPLES::

            sage: v = Sequence([1,2,3,4/5])
            sage: v[0] = 5
            sage: v
            [5, 2, 3, 4/5]
            sage: v.set_immutable()
            sage: v[3] = 7
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead."""
