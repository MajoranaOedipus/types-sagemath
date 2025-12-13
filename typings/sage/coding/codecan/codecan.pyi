import sage.groups.perm_gps.partn_ref2.refinement_generic
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class InnerGroup:
    """File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 106)

        This class implements the stabilizers `G_{\\Pi^{(I)}(x)}` described in
        :mod:`sage.groups.perm_gps.partn_ref2.refinement_generic` with
        `G = (GL(k,q) \\times \\GF{q}^n ) \\rtimes Aut(\\GF{q})`.

        Those stabilizers can be stored as triples:

        - ``rank`` -- integer in `\\{0, \\ldots, k\\}`
        - ``row_partition`` -- a partition of `\\{0, \\ldots, k-1\\}` with
          discrete cells for all integers `i` `\\geq` ``rank``
        - ``frob_pow`` -- integer `s` in `\\{0, \\ldots, r-1\\}` if `q = p^r`

        The group `G_{\\Pi^{(I)}(x)}` contains all elements `(A, \\varphi, \\alpha) \\in G`,
        where

        - `A` is a `2 \\times 2` blockmatrix, whose upper left matrix
          is a `k \\times k` diagonal matrix whose entries `A_{i,i}` are constant
          on the cells of the partition ``row_partition``.
          The lower left matrix is zero.
          And the right part is arbitrary.
        - The support of the columns given by `i \\in I` intersect exactly one
          cell of the partition. The entry `\\varphi_i` is equal to the entries
          of the corresponding diagonal entry of `A`.
        - `\\alpha` is a power of `\\tau^s`, where `\\tau` denotes the
          Frobenius automorphism of the finite field `\\GF{q}` and `s` = ``frob_pow``.

        See [Feu2009]_ for more details.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def column_blocks(self, mat) -> Any:
        """InnerGroup.column_blocks(self, mat)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 435)

        Let ``mat`` be a matrix which is stabilized by ``self`` having no zero
        columns. We know that for each column of ``mat`` there is a uniquely
        defined cell in ``self.row_partition`` having a nontrivial intersection
        with the support of this particular column.

        This function returns a partition (as list of lists) of the columns
        indices according to the partition of the rows given by ``self``.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import InnerGroup
            sage: I = InnerGroup(3)
            sage: mat = Matrix(GF(3), [[0,1,0],[1,0,0], [0,0,1]])
            sage: I.column_blocks(mat)
            [[1], [0], [2]]"""
    @overload
    def column_blocks(self, mat) -> Any:
        """InnerGroup.column_blocks(self, mat)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 435)

        Let ``mat`` be a matrix which is stabilized by ``self`` having no zero
        columns. We know that for each column of ``mat`` there is a uniquely
        defined cell in ``self.row_partition`` having a nontrivial intersection
        with the support of this particular column.

        This function returns a partition (as list of lists) of the columns
        indices according to the partition of the rows given by ``self``.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import InnerGroup
            sage: I = InnerGroup(3)
            sage: mat = Matrix(GF(3), [[0,1,0],[1,0,0], [0,0,1]])
            sage: I.column_blocks(mat)
            [[1], [0], [2]]"""
    @overload
    def get_frob_pow(self) -> int:
        """InnerGroup.get_frob_pow(self) -> int

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 421)

        Return the power of the Frobenius automorphism which generates
        the corresponding component of ``self``.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import InnerGroup
            sage: I = InnerGroup(10)
            sage: I.get_frob_pow()
            1"""
    @overload
    def get_frob_pow(self) -> Any:
        """InnerGroup.get_frob_pow(self) -> int

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 421)

        Return the power of the Frobenius automorphism which generates
        the corresponding component of ``self``.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import InnerGroup
            sage: I = InnerGroup(10)
            sage: I.get_frob_pow()
            1"""

class PartitionRefinementLinearCode(sage.groups.perm_gps.partn_ref2.refinement_generic.PartitionRefinement_generic):
    """PartitionRefinementLinearCode(n, generator_matrix, P=None, algorithm_type='semilinear')

    File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 465)

    See :mod:`sage.coding.codecan.codecan`.

    EXAMPLES::

        sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
        sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
        sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
        sage: cf = P.get_canonical_form(); cf
        [1 0 0 0 0 1 1 1 1 1 1 1 1]
        [0 1 0 1 1 0 0 1 1 2 2 1 2]
        [0 0 1 1 2 1 2 1 2 1 2 0 0]

    ::

        sage: cf.echelon_form() == (P.get_transporter() * mat).echelon_form()
        True

    ::

        sage: P.get_autom_order_permutation() == GL(3, GF(3)).order()/(len(GF(3))-1)
        True
        sage: A = P.get_autom_gens()
        sage: all((a*mat).echelon_form() == mat.echelon_form() for a in A)
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, n, generator_matrix, P=..., algorithm_type=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 509)

                Initialization, we immediately start the algorithm
                (see :mod:`sage.coding.codecan.codecan`)
                to compute the canonical form and automorphism group of the linear code
                generated by ``generator_matrix``.

                INPUT:

                - ``n`` -- integer
                - ``generator_matrix`` -- a `k \\times n` matrix over `\\GF{q}` of full row rank,
                  i.e. `k<n` and without zero columns
                - partition --  (optional) a partition (as list of lists) of the set
                  `\\{0, \\ldots, n-1\\}` which restricts the action of the permutational
                  part of the group to the stabilizer of this partition
                - algorithm_type -- (optional) use one of the following options

                  * "semilinear" --  full group
                  * "linear" -- no field automorphisms, i.e. `G = (GL(k,q) \\times \\GF{q}^n )`
                  * "permutational - no field automorphisms and no column multiplications
                    i.e. `G = GL(k,q)`

                EXAMPLES::

                    sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
                    sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
                    sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)

                ::

                    sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
                    sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
                    sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
        '''
    @overload
    def get_autom_gens(self) -> Any:
        """PartitionRefinementLinearCode.get_autom_gens(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 708)

        Return generators of the automorphism group of the initial matrix.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: A = P.get_autom_gens()
            sage: all((a*mat).echelon_form() == mat.echelon_form() for a in A)
            True"""
    @overload
    def get_autom_gens(self) -> Any:
        """PartitionRefinementLinearCode.get_autom_gens(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 708)

        Return generators of the automorphism group of the initial matrix.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: A = P.get_autom_gens()
            sage: all((a*mat).echelon_form() == mat.echelon_form() for a in A)
            True"""
    @overload
    def get_autom_order_inner_stabilizer(self) -> Any:
        """PartitionRefinementLinearCode.get_autom_order_inner_stabilizer(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 723)

        Return the order of the stabilizer of the initial matrix under
        the action of the inner group `G`.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: P.get_autom_order_inner_stabilizer()
            2
            sage: mat2 = Matrix(GF(4, 'a'), [[1,0,1], [0,1,1]])
            sage: P2 = PartitionRefinementLinearCode(mat2.ncols(), mat2)
            sage: P2.get_autom_order_inner_stabilizer()
            6"""
    @overload
    def get_autom_order_inner_stabilizer(self) -> Any:
        """PartitionRefinementLinearCode.get_autom_order_inner_stabilizer(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 723)

        Return the order of the stabilizer of the initial matrix under
        the action of the inner group `G`.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: P.get_autom_order_inner_stabilizer()
            2
            sage: mat2 = Matrix(GF(4, 'a'), [[1,0,1], [0,1,1]])
            sage: P2 = PartitionRefinementLinearCode(mat2.ncols(), mat2)
            sage: P2.get_autom_order_inner_stabilizer()
            6"""
    @overload
    def get_autom_order_inner_stabilizer(self) -> Any:
        """PartitionRefinementLinearCode.get_autom_order_inner_stabilizer(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 723)

        Return the order of the stabilizer of the initial matrix under
        the action of the inner group `G`.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: P.get_autom_order_inner_stabilizer()
            2
            sage: mat2 = Matrix(GF(4, 'a'), [[1,0,1], [0,1,1]])
            sage: P2 = PartitionRefinementLinearCode(mat2.ncols(), mat2)
            sage: P2.get_autom_order_inner_stabilizer()
            6"""
    @overload
    def get_canonical_form(self) -> Any:
        """PartitionRefinementLinearCode.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 674)

        Return the canonical form for this matrix.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P1 = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: CF1 = P1.get_canonical_form()
            sage: s = SemimonomialTransformationGroup(GF(3), mat.ncols()).an_element()
            sage: P2 = PartitionRefinementLinearCode(mat.ncols(), s*mat)
            sage: CF1 == P2.get_canonical_form()
            True"""
    @overload
    def get_canonical_form(self) -> Any:
        """PartitionRefinementLinearCode.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 674)

        Return the canonical form for this matrix.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P1 = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: CF1 = P1.get_canonical_form()
            sage: s = SemimonomialTransformationGroup(GF(3), mat.ncols()).an_element()
            sage: P2 = PartitionRefinementLinearCode(mat.ncols(), s*mat)
            sage: CF1 == P2.get_canonical_form()
            True"""
    @overload
    def get_canonical_form(self) -> Any:
        """PartitionRefinementLinearCode.get_canonical_form(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 674)

        Return the canonical form for this matrix.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P1 = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: CF1 = P1.get_canonical_form()
            sage: s = SemimonomialTransformationGroup(GF(3), mat.ncols()).an_element()
            sage: P2 = PartitionRefinementLinearCode(mat.ncols(), s*mat)
            sage: CF1 == P2.get_canonical_form()
            True"""
    @overload
    def get_transporter(self) -> Any:
        """PartitionRefinementLinearCode.get_transporter(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 691)

        Return the transporter element, mapping the initial matrix to its
        canonical form.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: CF = P.get_canonical_form()
            sage: t = P.get_transporter()
            sage: (t*mat).echelon_form() == CF.echelon_form()
            True"""
    @overload
    def get_transporter(self) -> Any:
        """PartitionRefinementLinearCode.get_transporter(self)

        File: /build/sagemath/src/sage/src/sage/coding/codecan/codecan.pyx (starting at line 691)

        Return the transporter element, mapping the initial matrix to its
        canonical form.

        EXAMPLES::

            sage: from sage.coding.codecan.codecan import PartitionRefinementLinearCode
            sage: mat = codes.HammingCode(GF(3), 3).dual_code().generator_matrix()
            sage: P = PartitionRefinementLinearCode(mat.ncols(), mat)
            sage: CF = P.get_canonical_form()
            sage: t = P.get_transporter()
            sage: (t*mat).echelon_form() == CF.echelon_form()
            True"""
