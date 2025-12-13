import _cython_3_2_1
import sage.structure.parent
from sage.categories.sets_cat import Sets as Sets
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

Set_PythonType: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict

class Set_PythonType_class(sage.structure.parent.Set_generic):
    """Set_PythonType_class(typ)

    File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 51)

    The set of Python objects of a given class.

    The elements of this set are not instances of
    :class:`~sage.structure.element.Element`; they are instances of
    the given class.

    INPUT:

    - ``typ`` -- a Python (new-style) class

    EXAMPLES::

        sage: from sage.sets.pythonclass import Set_PythonType
        sage: S = Set_PythonType(int); S
        Set of Python objects of class 'int'
        sage: int('1') in S
        True
        sage: Integer('1') in S
        False

        sage: Set_PythonType(2)
        Traceback (most recent call last):
        ...
        TypeError: must be initialized with a class, not 2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, typ) -> Any:
        """File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 79)

                EXAMPLES::

                    sage: from sage.sets.pythonclass import Set_PythonType
                    sage: Set_PythonType(float).category()
                    Category of infinite sets
        """
    @overload
    def cardinality(self) -> Any:
        """Set_PythonType_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 229)

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(bool)
            sage: S.cardinality()
            2
            sage: S = Set_PythonType(int)
            sage: S.cardinality()
            +Infinity"""
    @overload
    def cardinality(self) -> Any:
        """Set_PythonType_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 229)

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(bool)
            sage: S.cardinality()
            2
            sage: S = Set_PythonType(int)
            sage: S.cardinality()
            +Infinity"""
    @overload
    def cardinality(self) -> Any:
        """Set_PythonType_class.cardinality(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 229)

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(bool)
            sage: S.cardinality()
            2
            sage: S = Set_PythonType(int)
            sage: S.cardinality()
            +Infinity"""
    @overload
    def object(self) -> Any:
        """Set_PythonType_class.object(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 219)

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: Set_PythonType(tuple).object()
            <... 'tuple'>"""
    @overload
    def object(self) -> Any:
        """Set_PythonType_class.object(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 219)

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: Set_PythonType(tuple).object()
            <... 'tuple'>"""
    def __call__(self, x) -> Any:
        """Set_PythonType_class.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 120)

        Construct a new instance from ``x``. If ``x`` is already an
        instance of the correct class, directly return ``x`` itself.

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(float)
            sage: S(5)
            5.0
            sage: S(9/3)
            3.0
            sage: S(1/3)
            0.333333333333333...
            sage: a = float(3); S(a) is a
            True"""
    def __contains__(self, x) -> Any:
        """Set_PythonType_class.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 187)

        Only things of the right class (or subclasses thereof) are
        considered to belong to the set.

        EXAMPLES::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(tuple)
            sage: (1,2,3) in S
            True
            sage: () in S
            True
            sage: [1,2] in S
            False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """Set_PythonType_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 142)

        TESTS::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(int)
            sage: hash(S) == -hash(int)
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """Set_PythonType_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/sets/pythonclass.pyx (starting at line 107)

        Pickling support.

        TESTS::

            sage: from sage.sets.pythonclass import Set_PythonType
            sage: S = Set_PythonType(object)
            sage: loads(dumps(S))
            Set of Python objects of class 'object'"""
