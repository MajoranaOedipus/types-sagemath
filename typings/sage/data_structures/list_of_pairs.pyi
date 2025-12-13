from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

class ListOfPairs:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, size_tindex) -> Any:
        """ListOfPairs.__getitem__(self, size_t index)

        File: /build/sagemath/src/sage/src/sage/data_structures/list_of_pairs.pyx (starting at line 55)

        Get item of specified index.

        EXAMPLES::

            sage: from sage.data_structures.list_of_pairs import ListOfPairs
            sage: l = ListOfPairs()
            sage: l[0] = [1, 5]
            sage: l[0]
            (1, 5)
            sage: l[1]
            Traceback (most recent call last):
            ...
            IndexError
            sage: l[-1]
            Traceback (most recent call last):
            ...
            OverflowError: can't convert negative value to size_t"""
    def __setitem__(self, size_tindex, value) -> Any:
        """ListOfPairs.__setitem__(self, size_t index, value)

        File: /build/sagemath/src/sage/src/sage/data_structures/list_of_pairs.pyx (starting at line 78)

        Set item of specified index.

        Allows increasing the size of the list by at most 1.

        EXAMPLES::

            sage: from sage.data_structures.list_of_pairs import ListOfPairs
            sage: l = ListOfPairs()
            sage: l[0] = (2, 1)
            sage: l[1] = (1, 2)
            sage: l[0]
            (2, 1)
            sage: l[1]
            (1, 2)
            sage: l[10] = (5, 3)
            Traceback (most recent call last):
            ...
            IndexError
            sage: l[2] = 2
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable"""
