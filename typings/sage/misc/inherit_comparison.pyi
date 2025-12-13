import sage.misc.classcall_metaclass
from typing import Any

class InheritComparisonClasscallMetaclass(sage.misc.classcall_metaclass.ClasscallMetaclass, InheritComparisonMetaclass):
    '''File: /build/sagemath/src/sage/src/sage/misc/inherit_comparison.pyx (starting at line 95)

        Combine :class:`ClasscallMetaclass` with
        :class:`InheritComparisonMetaclass`.

        TESTS::

            sage: from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as M
            sage: M.__new__(M, "myclass", (object,), {})
            <class \'__main__.myclass\'>
    '''

class InheritComparisonMetaclass(type):
    '''InheritComparisonMetaclass(*args)

    File: /build/sagemath/src/sage/src/sage/misc/inherit_comparison.pyx (starting at line 46)

    If the type does not define ``__richcmp__`` nor ``__cmp__``,
    inherit both these methods from the base class. The difference with
    plain extension types is that comparison is inherited even if
    ``__hash__`` is defined.

    EXAMPLES::

        sage: # needs sage.misc.cython
        sage: cython(
        ....: \'\'\'
        ....: cimport cython
        ....:
        ....: from sage.misc.inherit_comparison cimport InheritComparisonMetaclass
        ....:
        ....: cdef class Base():
        ....:     def __richcmp__(left, right, int op):
        ....:         print("Calling Base.__richcmp__")
        ....:         return left is right
        ....:
        ....: cdef class Derived(Base):
        ....:     def __hash__(self):
        ....:         return 1
        ....:
        ....: cdef class DerivedWithRichcmp(Base):
        ....:     @cython.always_allow_keywords(False)
        ....:     def __getmetaclass__(_):
        ....:         from sage.misc.inherit_comparison import InheritComparisonMetaclass
        ....:         return InheritComparisonMetaclass
        ....:     def __hash__(self):
        ....:         return 1
        ....: \'\'\')
        sage: a = Derived()
        sage: a == a
        True
        sage: b = DerivedWithRichcmp()
        sage: b == b
        Calling Base.__richcmp__
        True'''
    def __init__(self, *args) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/inherit_comparison.pyx (starting at line 87)"""
