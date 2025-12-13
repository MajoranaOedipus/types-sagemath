import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matrix.constructor import Matrix as Matrix
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

__pyx_capi__: dict
random_tests: _cython_3_2_1.cython_function_or_method

class MatrixStruct:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def automorphism_group(self) -> Any:
        """MatrixStruct.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 172)

        Return a list of generators of the automorphism group, along with its
        order and a base for which the list of generators is a strong generating
        set.

        For more examples, see self.run().

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
            sage: M.automorphism_group()
            ([[0, 2, 1]], 2, [1])"""
    @overload
    def automorphism_group(self) -> Any:
        """MatrixStruct.automorphism_group(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 172)

        Return a list of generators of the automorphism group, along with its
        order and a base for which the list of generators is a strong generating
        set.

        For more examples, see self.run().

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
            sage: M.automorphism_group()
            ([[0, 2, 1]], 2, [1])"""
    @overload
    def canonical_relabeling(self) -> Any:
        """MatrixStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 201)

        Return a canonical relabeling (in list permutation format).

        For more examples, see self.run().

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
            sage: M.canonical_relabeling()
            [0, 1, 2]"""
    @overload
    def canonical_relabeling(self) -> Any:
        """MatrixStruct.canonical_relabeling(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 201)

        Return a canonical relabeling (in list permutation format).

        For more examples, see self.run().

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
            sage: M.canonical_relabeling()
            [0, 1, 2]"""
    @overload
    def display(self) -> Any:
        """MatrixStruct.display(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 93)

        Display the matrix, and associated data.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
            sage: M = MatrixStruct(Matrix(GF(5), [[0,1,1,4,4],[0,4,4,1,1]]))
            sage: M.display()
            [0 1 1 4 4]
            [0 4 4 1 1]
            <BLANKLINE>
            01100
            00011
            1
            <BLANKLINE>
            00011
            01100
            4"""
    @overload
    def display(self) -> Any:
        """MatrixStruct.display(self)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 93)

        Display the matrix, and associated data.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
            sage: M = MatrixStruct(Matrix(GF(5), [[0,1,1,4,4],[0,4,4,1,1]]))
            sage: M.display()
            [0 1 1 4 4]
            [0 4 4 1 1]
            <BLANKLINE>
            01100
            00011
            1
            <BLANKLINE>
            00011
            01100
            4"""
    @overload
    def is_isomorphic(self, MatrixStructother) -> Any:
        """MatrixStruct.is_isomorphic(self, MatrixStruct other)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 220)

        Calculate whether ``self`` is isomorphic to ``other``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
            sage: M = MatrixStruct(Matrix(GF(11), [[1,2,3,0,0,0],[0,0,0,1,2,3]]))
            sage: N = MatrixStruct(Matrix(GF(11), [[0,1,0,2,0,3],[1,0,2,0,3,0]]))
            sage: M.is_isomorphic(N)
            [0, 2, 4, 1, 3, 5]"""
    @overload
    def is_isomorphic(self, N) -> Any:
        """MatrixStruct.is_isomorphic(self, MatrixStruct other)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 220)

        Calculate whether ``self`` is isomorphic to ``other``.

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
            sage: M = MatrixStruct(Matrix(GF(11), [[1,2,3,0,0,0],[0,0,0,1,2,3]]))
            sage: N = MatrixStruct(Matrix(GF(11), [[0,1,0,2,0,3],[1,0,2,0,3,0]]))
            sage: M.is_isomorphic(N)
            [0, 2, 4, 1, 3, 5]"""
    @overload
    def run(self, partition=...) -> Any:
        """MatrixStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 125)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns;
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
            sage: M.run()
            sage: M.automorphism_group()
            ([[0, 2, 1]], 2, [1])
            sage: M.canonical_relabeling()
            [0, 1, 2]

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]))
            sage: M.automorphism_group()[1] == 6
            True

            sage: M = MatrixStruct(matrix(GF(3),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]))
            sage: M.automorphism_group()[1] == factorial(14)
            True"""
    @overload
    def run(self) -> Any:
        """MatrixStruct.run(self, partition=None)

        File: /build/sagemath/src/sage/src/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx (starting at line 125)

        Perform the canonical labeling and automorphism group computation,
        storing results to ``self``.

        INPUT:

        - ``partition`` -- an optional list of lists partition of the columns;
          default is the unit partition

        EXAMPLES::

            sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
            sage: M.run()
            sage: M.automorphism_group()
            ([[0, 2, 1]], 2, [1])
            sage: M.canonical_relabeling()
            [0, 1, 2]

            sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]))
            sage: M.automorphism_group()[1] == 6
            True

            sage: M = MatrixStruct(matrix(GF(3),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]))
            sage: M.automorphism_group()[1] == factorial(14)
            True"""
