import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

aut_gp_and_can_lab_python: _cython_3_2_1.cython_function_or_method
double_coset_python: _cython_3_2_1.cython_function_or_method

class PythonObjectWrapper:
    """File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 337)

        Instances of this class wrap a Python object and the refinement functions.
    """
    def __init__(self, obj, acae_fn, rari_fn, cs_fn, intdegree) -> Any:
        """PythonObjectWrapper.__init__(self, obj, acae_fn, rari_fn, cs_fn, int degree)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 341)

        Initialize a PythonObjectWrapper.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonObjectWrapper
            sage: def acae(a, b):
            ....:  return 0
            sage: def rari(a, b, c):
            ....:  return 0
            sage: def cs(a, b, c, d, e):
            ....:  return 0
            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonObjectWrapper
            sage: P = PythonObjectWrapper(None, acae, rari, cs, 7) # implicit doctest
            sage: P.obj
            sage: P.degree
            7
            sage: P.acae_fn
            <function acae at ...>
            sage: P.rari_fn
            <function rari at ...>
            sage: P.cs_fn
            <function cs at ...>"""

class PythonPartitionStack:
    """PythonPartitionStack(int n)

    File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 42)

    Instances of this class wrap a (Cython) PartitionStack."""
    def __init__(self, intn) -> Any:
        """File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 47)

                Initialize a PartitionStack.

                EXAMPLES::

                    sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
                    sage: P = PythonPartitionStack(7) # implicit doctest
        """
    @overload
    def clear(self) -> Any:
        """PythonPartitionStack.clear(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 167)

        Set the current partition to the first shallower one, i.e. forget about
        boundaries between cells that are new to the current level.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth(1)
            1
            sage: P.set_level(2,1)
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2|3 4 5 6)
            sage: P.clear()
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2 3 4 5 6)"""
    @overload
    def clear(self) -> Any:
        """PythonPartitionStack.clear(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 167)

        Set the current partition to the first shallower one, i.e. forget about
        boundaries between cells that are new to the current level.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth(1)
            1
            sage: P.set_level(2,1)
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2|3 4 5 6)
            sage: P.clear()
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2 3 4 5 6)"""
    @overload
    def degree(self, new=...) -> Any:
        """PythonPartitionStack.degree(self, new=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 294)

        Return the degree of the partition stack, setting it to
        new if new is not None.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.degree()
            7"""
    @overload
    def degree(self) -> Any:
        """PythonPartitionStack.degree(self, new=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 294)

        Return the degree of the partition stack, setting it to
        new if new is not None.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.degree()
            7"""
    @overload
    def depth(self, new=...) -> Any:
        """PythonPartitionStack.depth(self, new=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 278)

        Return the depth of the deepest partition in the stack, setting it to
        new if new is not None.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth()
            0"""
    @overload
    def depth(self) -> Any:
        """PythonPartitionStack.depth(self, new=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 278)

        Return the depth of the deepest partition in the stack, setting it to
        new if new is not None.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth()
            0"""
    @overload
    def display(self) -> Any:
        """PythonPartitionStack.display(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 83)

        Print a representation of the stack.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth(1)
            1
            sage: P.set_level(2,1)
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2|3 4 5 6)"""
    @overload
    def display(self) -> Any:
        """PythonPartitionStack.display(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 83)

        Print a representation of the stack.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth(1)
            1
            sage: P.set_level(2,1)
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2|3 4 5 6)"""
    @overload
    def entries(self) -> Any:
        """PythonPartitionStack.entries(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 189)

        Return the entries array as a Python list of ints.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.entries()
            [0, 1, 2, 3, 4, 5, 6]
            sage: P.levels()
            [7, 7, 7, 7, 7, 7, -1]"""
    @overload
    def entries(self) -> Any:
        """PythonPartitionStack.entries(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 189)

        Return the entries array as a Python list of ints.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.entries()
            [0, 1, 2, 3, 4, 5, 6]
            sage: P.levels()
            [7, 7, 7, 7, 7, 7, -1]"""
    def get_entry(self, inti) -> Any:
        """PythonPartitionStack.get_entry(self, int i)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 220)

        Get the `i`-th entry of the entries array.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.get_entry(0)
            0"""
    def get_level(self, inti) -> Any:
        """PythonPartitionStack.get_level(self, int i)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 265)

        Get the `i`-th entry of the levels array.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.get_level(0)
            7"""
    @overload
    def is_discrete(self) -> Any:
        """PythonPartitionStack.is_discrete(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 100)

        Return whether the deepest partition consists only of singleton cells.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.is_discrete()
            False
            sage: [P.set_level(i,0) for i in range(7)]
            [None, None, None, None, None, None, None]
            sage: P.is_discrete()
            True"""
    @overload
    def is_discrete(self) -> Any:
        """PythonPartitionStack.is_discrete(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 100)

        Return whether the deepest partition consists only of singleton cells.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.is_discrete()
            False
            sage: [P.set_level(i,0) for i in range(7)]
            [None, None, None, None, None, None, None]
            sage: P.is_discrete()
            True"""
    @overload
    def is_discrete(self) -> Any:
        """PythonPartitionStack.is_discrete(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 100)

        Return whether the deepest partition consists only of singleton cells.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.is_discrete()
            False
            sage: [P.set_level(i,0) for i in range(7)]
            [None, None, None, None, None, None, None]
            sage: P.is_discrete()
            True"""
    @overload
    def levels(self) -> Any:
        """PythonPartitionStack.levels(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 233)

        Return the levels array as a Python list of ints.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.entries()
            [0, 1, 2, 3, 4, 5, 6]
            sage: P.levels()
            [7, 7, 7, 7, 7, 7, -1]"""
    @overload
    def levels(self) -> Any:
        """PythonPartitionStack.levels(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 233)

        Return the levels array as a Python list of ints.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.entries()
            [0, 1, 2, 3, 4, 5, 6]
            sage: P.levels()
            [7, 7, 7, 7, 7, 7, -1]"""
    def move_min_to_front(self, intstart, intend) -> Any:
        """PythonPartitionStack.move_min_to_front(self, int start, int end)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 130)

        Make sure that the first element of the segment of entries i with
        start <= i <= end is minimal.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.set_entry(1,0)
            sage: P.set_entry(0,1)
            sage: P.display()
            (1 0 2 3 4 5 6)
            sage: P.move_min_to_front(0,1)
            sage: P.display()
            (0 1 2 3 4 5 6)"""
    @overload
    def num_cells(self) -> Any:
        """PythonPartitionStack.num_cells(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 117)

        Return the number of cells in the deepest partition.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.num_cells()
            1"""
    @overload
    def num_cells(self) -> Any:
        """PythonPartitionStack.num_cells(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 117)

        Return the number of cells in the deepest partition.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.num_cells()
            1"""
    def partition(self, intk) -> Any:
        """PythonPartitionStack.partition(self, int k)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 310)

        Return the partition at level k, as a Python list of lists.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth(1)
            1
            sage: P.set_level(2,1)
            sage: P.partition(0)
            [[0, 1, 2, 3, 4, 5, 6]]
            sage: P.partition(1)
            [[0, 1, 2], [3, 4, 5, 6]]"""
    def set_entry(self, inti, intentry) -> Any:
        """PythonPartitionStack.set_entry(self, int i, int entry)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 205)

        Set the `i`-th entry of the entries array to entry.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.set_entry(1,0)
            sage: P.set_entry(0,1)
            sage: P.display()
            (1 0 2 3 4 5 6)"""
    def set_level(self, inti, intlevel) -> Any:
        """PythonPartitionStack.set_level(self, int i, int level)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 248)

        Set the `i`-th entry of the levels array to entry.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: P.depth(1)
            1
            sage: P.set_level(2,1)
            sage: P.display()
            (0 1 2 3 4 5 6)
            (0 1 2|3 4 5 6)"""
    def __copy__(self) -> Any:
        """PythonPartitionStack.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_python.pyx (starting at line 149)


        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_python import PythonPartitionStack
            sage: P = PythonPartitionStack(7)
            sage: Q = copy(P)
            sage: P.display()
            (0 1 2 3 4 5 6)
            sage: Q.display()
            (0 1 2 3 4 5 6)"""
