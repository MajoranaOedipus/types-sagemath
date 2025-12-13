import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import Matrix as Matrix, have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

__pyx_capi__: dict
random_tests: _cython_3_2_1.cython_function_or_method

class BinaryCodeStruct:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class LinearBinaryCodeStruct(BinaryCodeStruct):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def automorphism_group(self) -> Any:
        """LinearBinaryCodeStruct.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 254)

        Return a list of generators of the automorphism group, along with its
        order and a base for which the list of generators is a strong generating
        set.

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[1,1,1,1]]))
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])"""
    @overload
    def automorphism_group(self) -> Any:
        """LinearBinaryCodeStruct.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 254)

        Return a list of generators of the automorphism group, along with its
        order and a base for which the list of generators is a strong generating
        set.

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[1,1,1,1]]))
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])"""
    @overload
    def canonical_relabeling(self) -> Any:
        """LinearBinaryCodeStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 281)

        Return a canonical relabeling (in list permutation format).

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2), [[1,1,0]]))
            sage: B.automorphism_group()
            ([[1, 0, 2]], 2, [0])
            sage: B.canonical_relabeling()
            [1, 2, 0]
            sage: B = LinearBinaryCodeStruct(matrix(GF(2), [[1,0,1]]))
            sage: B.automorphism_group()
            ([[2, 1, 0]], 2, [0])
            sage: B.canonical_relabeling()
            [1, 0, 2]"""
    @overload
    def canonical_relabeling(self) -> Any:
        """LinearBinaryCodeStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 281)

        Return a canonical relabeling (in list permutation format).

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2), [[1,1,0]]))
            sage: B.automorphism_group()
            ([[1, 0, 2]], 2, [0])
            sage: B.canonical_relabeling()
            [1, 2, 0]
            sage: B = LinearBinaryCodeStruct(matrix(GF(2), [[1,0,1]]))
            sage: B.automorphism_group()
            ([[2, 1, 0]], 2, [0])
            sage: B.canonical_relabeling()
            [1, 0, 2]"""
    @overload
    def canonical_relabeling(self) -> Any:
        """LinearBinaryCodeStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 281)

        Return a canonical relabeling (in list permutation format).

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2), [[1,1,0]]))
            sage: B.automorphism_group()
            ([[1, 0, 2]], 2, [0])
            sage: B.canonical_relabeling()
            [1, 2, 0]
            sage: B = LinearBinaryCodeStruct(matrix(GF(2), [[1,0,1]]))
            sage: B.automorphism_group()
            ([[2, 1, 0]], 2, [0])
            sage: B.canonical_relabeling()
            [1, 0, 2]"""
    @overload
    def is_isomorphic(self, LinearBinaryCodeStructother) -> Any:
        """LinearBinaryCodeStruct.is_isomorphic(self, LinearBinaryCodeStruct other)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 305)

        Calculate whether ``self`` is isomorphic to ``other``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,1,0,0],[0,0,1,1,1,1]]))
            sage: C = LinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,1],[1,1,0,1,1,0]]))
            sage: B.is_isomorphic(C)
            [0, 1, 2, 5, 3, 4]"""
    @overload
    def is_isomorphic(self, C) -> Any:
        """LinearBinaryCodeStruct.is_isomorphic(self, LinearBinaryCodeStruct other)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 305)

        Calculate whether ``self`` is isomorphic to ``other``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,1,0,0],[0,0,1,1,1,1]]))
            sage: C = LinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,1],[1,1,0,1,1,0]]))
            sage: B.is_isomorphic(C)
            [0, 1, 2, 5, 3, 4]"""
    @overload
    def run(self, partition=...) -> Any:
        """LinearBinaryCodeStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 113)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns;
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[1,0,1],[0,1,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 2, 1], [1, 0, 2]], 6, [0, 1])
            sage: B.canonical_relabeling()
            [0, 1, 2]

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[1,1,1,1]]))
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])
            sage: B.canonical_relabeling()
            [0, 1, 2, 3]

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]))
            sage: B.automorphism_group()[1] == factorial(14)
            True

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],            ....: [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],            ....: [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],            ....: [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],            ....: [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            322560

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],            ....: [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0],            ....: [0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1],            ....: [0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            2304

            sage: M = Matrix(GF(2),[            ....: [1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0],            ....: [0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0],            ....: [0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0],            ....: [0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0],            ....: [0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0],            ....: [0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0],            ....: [0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0],            ....: [0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            136

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
            ....: [0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1],
            ....: [0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1],
            ....: [0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1],
            ....: [0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,0]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            2160

            sage: M = Matrix(GF(2),[            ....: [0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1],            ....: [1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0],            ....: [0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0],            ....: [1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1],            ....: [1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0],            ....: [1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0],            ....: [0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0],            ....: [0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1],            ....: [0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1],            ....: [1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1],            ....: [0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            887040

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
            ....: [1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,0],
            ....: [1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0],
            ....: [1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            294912

            sage: M = Matrix(GF(2), [            ....: [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],
            ....: [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0],
            ....: [0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0],
            ....: [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
            ....: [0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1],
            ....: [0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            442368

            sage: M = Matrix(GF(2), [            ....: [1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],            ....: [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            17868913969917295853568000000"""
    @overload
    def run(self) -> Any:
        """LinearBinaryCodeStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 113)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns;
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import LinearBinaryCodeStruct

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[1,0,1],[0,1,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 2, 1], [1, 0, 2]], 6, [0, 1])
            sage: B.canonical_relabeling()
            [0, 1, 2]

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[1,1,1,1]]))
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])
            sage: B.canonical_relabeling()
            [0, 1, 2, 3]

            sage: B = LinearBinaryCodeStruct(matrix(GF(2),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]))
            sage: B.automorphism_group()[1] == factorial(14)
            True

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],            ....: [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],            ....: [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],            ....: [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],            ....: [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            322560

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],            ....: [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0],            ....: [0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1],            ....: [0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            2304

            sage: M = Matrix(GF(2),[            ....: [1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0],            ....: [0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0],            ....: [0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0],            ....: [0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0],            ....: [0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0],            ....: [0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0],            ....: [0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0],            ....: [0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            136

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
            ....: [0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1],
            ....: [0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1],
            ....: [0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1],
            ....: [0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,0]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            2160

            sage: M = Matrix(GF(2),[            ....: [0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1],            ....: [1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0],            ....: [0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0],            ....: [1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1],            ....: [1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0],            ....: [1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0],            ....: [0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0],            ....: [0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1],            ....: [0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1],            ....: [1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1],            ....: [0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            887040

            sage: M = Matrix(GF(2),[            ....: [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
            ....: [1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,0],
            ....: [1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0],
            ....: [1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            294912

            sage: M = Matrix(GF(2), [            ....: [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
            ....: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],
            ....: [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0],
            ....: [0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0],
            ....: [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
            ....: [0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1],
            ....: [0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            442368

            sage: M = Matrix(GF(2), [            ....: [1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],            ....: [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1]])
            sage: B = LinearBinaryCodeStruct(M)
            sage: B.automorphism_group()[1]
            17868913969917295853568000000"""

class NonlinearBinaryCodeStruct(BinaryCodeStruct):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def automorphism_group(self) -> Any:
        """NonlinearBinaryCodeStruct.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 529)

        Return a list of generators of the automorphism group, along with its
        order and a base for which the list of generators is a strong generating
        set.

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2, 4, 5],
              [0, 2, 1, 3, 4, 5],
              [1, 0, 2, 3, 4, 5],
              [0, 1, 2, 3, 5, 4]],
             48,
             [4, 0, 1, 2])"""
    @overload
    def automorphism_group(self) -> Any:
        """NonlinearBinaryCodeStruct.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 529)

        Return a list of generators of the automorphism group, along with its
        order and a base for which the list of generators is a strong generating
        set.

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2, 4, 5],
              [0, 2, 1, 3, 4, 5],
              [1, 0, 2, 3, 4, 5],
              [0, 1, 2, 3, 5, 4]],
             48,
             [4, 0, 1, 2])"""
    @overload
    def canonical_relabeling(self) -> Any:
        """NonlinearBinaryCodeStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 562)

        Return a canonical relabeling (in list permutation format).

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.canonical_relabeling()
            [2, 3, 4, 5, 0, 1]"""
    @overload
    def canonical_relabeling(self) -> Any:
        """NonlinearBinaryCodeStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 562)

        Return a canonical relabeling (in list permutation format).

        EXAMPLES: (For more examples, see self.run())::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.canonical_relabeling()
            [2, 3, 4, 5, 0, 1]"""
    @overload
    def is_isomorphic(self, NonlinearBinaryCodeStructother) -> Any:
        """NonlinearBinaryCodeStruct.is_isomorphic(self, NonlinearBinaryCodeStruct other)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 580)

        Calculate whether ``self`` is isomorphic to ``other``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,1,0,0],[0,0,1,1,1,1]]))
            sage: C = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,0,0,1,1],[1,1,1,1,0,0]]))
            sage: B.is_isomorphic(C)
            [2, 3, 0, 1, 4, 5]"""
    @overload
    def is_isomorphic(self, C) -> Any:
        """NonlinearBinaryCodeStruct.is_isomorphic(self, NonlinearBinaryCodeStruct other)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 580)

        Calculate whether ``self`` is isomorphic to ``other``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,1,0,0],[0,0,1,1,1,1]]))
            sage: C = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,0,0,1,1],[1,1,1,1,0,0]]))
            sage: B.is_isomorphic(C)
            [2, 3, 0, 1, 4, 5]"""
    @overload
    def run(self, partition=...) -> Any:
        """NonlinearBinaryCodeStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 475)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,0,0,0],[0,0,1,0]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[2, 1, 0, 3], [0, 3, 2, 1]], 4, [1, 0])
            sage: B.canonical_relabeling()
            [2, 0, 3, 1]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])
            sage: B.canonical_relabeling()
            [0, 1, 2, 3]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2, 4, 5],
              [0, 2, 1, 3, 4, 5],
              [1, 0, 2, 3, 4, 5],
              [0, 1, 2, 3, 5, 4]],
             48,
             [4, 0, 1, 2])
            sage: B.canonical_relabeling()
            [2, 3, 4, 5, 0, 1]"""
    @overload
    def run(self) -> Any:
        """NonlinearBinaryCodeStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 475)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,0,0,0],[0,0,1,0]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[2, 1, 0, 3], [0, 3, 2, 1]], 4, [1, 0])
            sage: B.canonical_relabeling()
            [2, 0, 3, 1]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])
            sage: B.canonical_relabeling()
            [0, 1, 2, 3]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2, 4, 5],
              [0, 2, 1, 3, 4, 5],
              [1, 0, 2, 3, 4, 5],
              [0, 1, 2, 3, 5, 4]],
             48,
             [4, 0, 1, 2])
            sage: B.canonical_relabeling()
            [2, 3, 4, 5, 0, 1]"""
    @overload
    def run(self) -> Any:
        """NonlinearBinaryCodeStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 475)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,0,0,0],[0,0,1,0]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[2, 1, 0, 3], [0, 3, 2, 1]], 4, [1, 0])
            sage: B.canonical_relabeling()
            [2, 0, 3, 1]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])
            sage: B.canonical_relabeling()
            [0, 1, 2, 3]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2, 4, 5],
              [0, 2, 1, 3, 4, 5],
              [1, 0, 2, 3, 4, 5],
              [0, 1, 2, 3, 5, 4]],
             48,
             [4, 0, 1, 2])
            sage: B.canonical_relabeling()
            [2, 3, 4, 5, 0, 1]"""
    @overload
    def run(self) -> Any:
        """NonlinearBinaryCodeStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_binary.pyx (starting at line 475)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,0,0,0],[0,0,1,0]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[2, 1, 0, 3], [0, 3, 2, 1]], 4, [1, 0])
            sage: B.canonical_relabeling()
            [2, 0, 3, 1]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2], [0, 2, 1, 3], [1, 0, 2, 3]], 24, [0, 1, 2])
            sage: B.canonical_relabeling()
            [0, 1, 2, 3]

            sage: B = NonlinearBinaryCodeStruct(Matrix(GF(2), [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,1,1,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]))
            sage: B.run()
            sage: B.automorphism_group()
            ([[0, 1, 3, 2, 4, 5],
              [0, 2, 1, 3, 4, 5],
              [1, 0, 2, 3, 4, 5],
              [0, 1, 2, 3, 5, 4]],
             48,
             [4, 0, 1, 2])
            sage: B.canonical_relabeling()
            [2, 3, 4, 5, 0, 1]"""
