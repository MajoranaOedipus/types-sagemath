from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.list_clone_demo import IncreasingArrays as IncreasingArrays

class IncreasingArraysPy(IncreasingArrays):
    class Element(ClonableArray):
        """
        A small class for testing :class:`ClonableArray`: Increasing Lists.

        TESTS::

            sage: from sage.structure.list_clone_timings import IncreasingArraysPy
            sage: TestSuite(IncreasingArraysPy()([1,2,3])).run()
        """
        def check(self) -> None:
            """
            Check that ``self`` is increasing.

            EXAMPLES::

                sage: from sage.structure.list_clone_timings import IncreasingArraysPy
                sage: IncreasingArraysPy()([1,2,3]) # indirect doctest
                [1, 2, 3]
                sage: IncreasingArraysPy()([3,2,1]) # indirect doctest
                Traceback (most recent call last):
                ...
                ValueError: Lists is not increasing
            """

def add1_internal(bla):
    """
    TESTS::

        sage: from sage.structure.list_clone_timings import *
        sage: add1_internal(IncreasingArrays()([1,4,5]))
        [2, 5, 6]
    """
def add1_immutable(bla):
    """
    TESTS::

        sage: from sage.structure.list_clone_timings import *
        sage: add1_immutable(IncreasingArrays()([1,4,5]))
        [2, 5, 6]
    """
def add1_mutable(bla):
    """
    TESTS::

        sage: from sage.structure.list_clone_timings import *
        sage: add1_mutable(IncreasingArrays()([1,4,5]))
        [2, 5, 6]
    """
def add1_with(bla):
    """
    TESTS::

        sage: from sage.structure.list_clone_timings import *
        sage: add1_with(IncreasingArrays()([1,4,5]))
        [2, 5, 6]
    """
