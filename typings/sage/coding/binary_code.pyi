import _cython_3_2_1
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.timing import cputime as cputime
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

WORD_SIZE: int
__pyx_capi__: dict
test_expand_to_ortho_basis: _cython_3_2_1.cython_function_or_method
test_word_perms: _cython_3_2_1.cython_function_or_method
weight_dist: _cython_3_2_1.cython_function_or_method

class BinaryCode:
    """File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 708)

        Minimal, but optimized, binary code object.

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)     # create from matrix
            sage: C = BinaryCode(B, 60) # create using glue
            sage: D = BinaryCode(C, 240)
            sage: E = BinaryCode(D, 85)
            sage: B
            Binary [4,1] linear code, generator matrix
            [1111]
            sage: C
            Binary [6,2] linear code, generator matrix
            [111100]
            [001111]
            sage: D
            Binary [8,3] linear code, generator matrix
            [11110000]
            [00111100]
            [00001111]
            sage: E
            Binary [8,4] linear code, generator matrix
            [11110000]
            [00111100]
            [00001111]
            [10101010]

            sage: M = Matrix(GF(2), [[1]*32])
            sage: B = BinaryCode(M)
            sage: B
            Binary [32,1] linear code, generator matrix
            [11111111111111111111111111111111]
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    @classmethod
    def __init__(cls, M) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    @classmethod
    def __init__(cls, M) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def apply_permutation(self, labeling) -> Any:
        """BinaryCode.apply_permutation(self, labeling)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1131)

        Apply a column permutation to the code.

        INPUT:

        - ``labeling`` -- list permutation of the columns

        EXAMPLES::

            sage: from sage.coding.binary_code import *
            sage: B = BinaryCode(codes.GolayCode(GF(2)).generator_matrix())
            sage: B
            Binary [24,12] linear code, generator matrix
            [100000000000101011100011]
            [010000000000111110010010]
            [001000000000110100101011]
            [000100000000110001110110]
            [000010000000110011011001]
            [000001000000011001101101]
            [000000100000001100110111]
            [000000010000101101111000]
            [000000001000010110111100]
            [000000000100001011011110]
            [000000000010101110001101]
            [000000000001010111000111]
            sage: B.apply_permutation(list(range(11,-1,-1)) + list(range(12, 24)))
            sage: B
            Binary [24,12] linear code, generator matrix
            [000000000001101011100011]
            [000000000010111110010010]
            [000000000100110100101011]
            [000000001000110001110110]
            [000000010000110011011001]
            [000000100000011001101101]
            [000001000000001100110111]
            [000010000000101101111000]
            [000100000000010110111100]
            [001000000000001011011110]
            [010000000000101110001101]
            [100000000000010111000111]"""
    @overload
    def matrix(self) -> Any:
        """BinaryCode.matrix(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 869)

        Return the generator matrix of the :class:`BinaryCode`, i.e. the code is
        the rowspace of ``B.matrix()``.

        EXAMPLES::

            sage: M = Matrix(GF(2), [[1,1,1,1,0,0], [0,0,1,1,1,1]])
            sage: from sage.coding.binary_code import *
            sage: B = BinaryCode(M)
            sage: B.matrix()
            [1 1 1 1 0 0]
            [0 0 1 1 1 1]"""
    @overload
    def matrix(self) -> Any:
        """BinaryCode.matrix(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 869)

        Return the generator matrix of the :class:`BinaryCode`, i.e. the code is
        the rowspace of ``B.matrix()``.

        EXAMPLES::

            sage: M = Matrix(GF(2), [[1,1,1,1,0,0], [0,0,1,1,1,1]])
            sage: from sage.coding.binary_code import *
            sage: B = BinaryCode(M)
            sage: B.matrix()
            [1 1 1 1 0 0]
            [0 0 1 1 1 1]"""
    @overload
    def matrix(self) -> Any:
        """BinaryCode.matrix(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 869)

        Return the generator matrix of the :class:`BinaryCode`, i.e. the code is
        the rowspace of ``B.matrix()``.

        EXAMPLES::

            sage: M = Matrix(GF(2), [[1,1,1,1,0,0], [0,0,1,1,1,1]])
            sage: from sage.coding.binary_code import *
            sage: B = BinaryCode(M)
            sage: B.matrix()
            [1 1 1 1 0 0]
            [0 0 1 1 1 1]"""
    @overload
    def print_data(self) -> Any:
        '''BinaryCode.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 895)

        Print all data for ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)
            sage: C = BinaryCode(B, 60)
            sage: D = BinaryCode(C, 240)
            sage: E = BinaryCode(D, 85)
            sage: B.print_data() # random - actually "print(P.print_data())"
            ncols: 4
            nrows: 1
            nwords: 2
            radix: 32
            basis:
            1111
            words:
            0000
            1111
            sage: C.print_data() # random - actually "print(P.print_data())"
            ncols: 6
            nrows: 2
            nwords: 4
            radix: 32
            basis:
            111100
            001111
            words:
            000000
            111100
            001111
            110011
            sage: D.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 3
            nwords: 8
            radix: 32
            basis:
            11110000
            00111100
            00001111
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            sage: E.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 4
            nwords: 16
            radix: 32
            basis:
            11110000
            00111100
            00001111
            10101010
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            10101010
            01011010
            10010110
            01100110
            10100101
            01010101
            10011001
            01101001'''
    @overload
    def print_data(self) -> Any:
        '''BinaryCode.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 895)

        Print all data for ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)
            sage: C = BinaryCode(B, 60)
            sage: D = BinaryCode(C, 240)
            sage: E = BinaryCode(D, 85)
            sage: B.print_data() # random - actually "print(P.print_data())"
            ncols: 4
            nrows: 1
            nwords: 2
            radix: 32
            basis:
            1111
            words:
            0000
            1111
            sage: C.print_data() # random - actually "print(P.print_data())"
            ncols: 6
            nrows: 2
            nwords: 4
            radix: 32
            basis:
            111100
            001111
            words:
            000000
            111100
            001111
            110011
            sage: D.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 3
            nwords: 8
            radix: 32
            basis:
            11110000
            00111100
            00001111
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            sage: E.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 4
            nwords: 16
            radix: 32
            basis:
            11110000
            00111100
            00001111
            10101010
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            10101010
            01011010
            10010110
            01100110
            10100101
            01010101
            10011001
            01101001'''
    @overload
    def print_data(self) -> Any:
        '''BinaryCode.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 895)

        Print all data for ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)
            sage: C = BinaryCode(B, 60)
            sage: D = BinaryCode(C, 240)
            sage: E = BinaryCode(D, 85)
            sage: B.print_data() # random - actually "print(P.print_data())"
            ncols: 4
            nrows: 1
            nwords: 2
            radix: 32
            basis:
            1111
            words:
            0000
            1111
            sage: C.print_data() # random - actually "print(P.print_data())"
            ncols: 6
            nrows: 2
            nwords: 4
            radix: 32
            basis:
            111100
            001111
            words:
            000000
            111100
            001111
            110011
            sage: D.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 3
            nwords: 8
            radix: 32
            basis:
            11110000
            00111100
            00001111
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            sage: E.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 4
            nwords: 16
            radix: 32
            basis:
            11110000
            00111100
            00001111
            10101010
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            10101010
            01011010
            10010110
            01100110
            10100101
            01010101
            10011001
            01101001'''
    @overload
    def print_data(self) -> Any:
        '''BinaryCode.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 895)

        Print all data for ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)
            sage: C = BinaryCode(B, 60)
            sage: D = BinaryCode(C, 240)
            sage: E = BinaryCode(D, 85)
            sage: B.print_data() # random - actually "print(P.print_data())"
            ncols: 4
            nrows: 1
            nwords: 2
            radix: 32
            basis:
            1111
            words:
            0000
            1111
            sage: C.print_data() # random - actually "print(P.print_data())"
            ncols: 6
            nrows: 2
            nwords: 4
            radix: 32
            basis:
            111100
            001111
            words:
            000000
            111100
            001111
            110011
            sage: D.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 3
            nwords: 8
            radix: 32
            basis:
            11110000
            00111100
            00001111
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            sage: E.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 4
            nwords: 16
            radix: 32
            basis:
            11110000
            00111100
            00001111
            10101010
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            10101010
            01011010
            10010110
            01100110
            10100101
            01010101
            10011001
            01101001'''
    @overload
    def print_data(self) -> Any:
        '''BinaryCode.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 895)

        Print all data for ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)
            sage: C = BinaryCode(B, 60)
            sage: D = BinaryCode(C, 240)
            sage: E = BinaryCode(D, 85)
            sage: B.print_data() # random - actually "print(P.print_data())"
            ncols: 4
            nrows: 1
            nwords: 2
            radix: 32
            basis:
            1111
            words:
            0000
            1111
            sage: C.print_data() # random - actually "print(P.print_data())"
            ncols: 6
            nrows: 2
            nwords: 4
            radix: 32
            basis:
            111100
            001111
            words:
            000000
            111100
            001111
            110011
            sage: D.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 3
            nwords: 8
            radix: 32
            basis:
            11110000
            00111100
            00001111
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            sage: E.print_data() # random - actually "print(P.print_data())"
            ncols: 8
            nrows: 4
            nwords: 16
            radix: 32
            basis:
            11110000
            00111100
            00001111
            10101010
            words:
            00000000
            11110000
            00111100
            11001100
            00001111
            11111111
            00110011
            11000011
            10101010
            01011010
            10010110
            01100110
            10100101
            01010101
            10011001
            01101001'''
    @overload
    def put_in_std_form(self) -> int:
        """BinaryCode.put_in_std_form(self) -> int

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1207)

        Put the code in binary form, which is defined by an identity matrix on
        the left, augmented by a matrix of data.

        EXAMPLES::

            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1,0,0], [0,0,1,1,1,1]])
            sage: B = BinaryCode(M); B
            Binary [6,2] linear code, generator matrix
            [111100]
            [001111]
            sage: B.put_in_std_form(); B
            0
            Binary [6,2] linear code, generator matrix
            [101011]
            [010111]"""
    @overload
    def put_in_std_form(self) -> Any:
        """BinaryCode.put_in_std_form(self) -> int

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1207)

        Put the code in binary form, which is defined by an identity matrix on
        the left, augmented by a matrix of data.

        EXAMPLES::

            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1,0,0], [0,0,1,1,1,1]])
            sage: B = BinaryCode(M); B
            Binary [6,2] linear code, generator matrix
            [111100]
            [001111]
            sage: B.put_in_std_form(); B
            0
            Binary [6,2] linear code, generator matrix
            [101011]
            [010111]"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """BinaryCode.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 838)

        Method for pickling and unpickling BinaryCodes.

        TESTS::

            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1]])
            sage: B = BinaryCode(M)
            sage: loads(dumps(B)) == B
            True"""

class BinaryCodeClassifier:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def generate_children(self, BinaryCodeB, intn, intd=...) -> Any:
        """BinaryCodeClassifier.generate_children(self, BinaryCode B, int n, int d=2)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 3856)

        Use canonical augmentation to generate children of the code `B`.

        INPUT:

        - ``B`` -- a :class:`BinaryCode`

        - ``n`` -- limit on the degree of the code

        - ``d`` -- test whether new vector has weight divisible by `d`. If
          `d=4`, this ensures that all doubly-even canonically augmented
          children are generated.

        EXAMPLES::

            sage: from sage.coding.binary_code import *
            sage: BC = BinaryCodeClassifier()
            sage: B = BinaryCode(Matrix(GF(2), [[1,1,1,1]]))
            sage: BC.generate_children(B, 6, 4)                                         # needs sage.groups
            [
            [1 1 1 1 0 0]
            [0 1 0 1 1 1]
            ]

        .. NOTE::

            The function ``codes.databases.self_orthogonal_binary_codes`` makes heavy
            use of this function.

        MORE EXAMPLES::

            sage: # needs sage.groups
            sage: soc_iter = codes.databases.self_orthogonal_binary_codes(12, 6, 4)
            sage: L = list(soc_iter)
            sage: for n in range(13):
            ....:   s = 'n=%2d : ' % n
            ....:   for k in range(1,7):
            ....:       s += '%3d ' % len([C for C in L
            ....:                        if C.length() == n and C.dimension() == k])
            ....:   print(s)
            n= 0 :   0   0   0   0   0   0
            n= 1 :   0   0   0   0   0   0
            n= 2 :   0   0   0   0   0   0
            n= 3 :   0   0   0   0   0   0
            n= 4 :   1   0   0   0   0   0
            n= 5 :   0   0   0   0   0   0
            n= 6 :   0   1   0   0   0   0
            n= 7 :   0   0   1   0   0   0
            n= 8 :   1   1   1   1   0   0
            n= 9 :   0   0   0   0   0   0
            n=10 :   0   1   1   1   0   0
            n=11 :   0   0   1   1   0   0
            n=12 :   1   2   3   4   2   0"""
    @overload
    def put_in_canonical_form(self, BinaryCodeB) -> Any:
        """BinaryCodeClassifier.put_in_canonical_form(self, BinaryCode B)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 3808)

        Put the code into canonical form.

        Canonical form is obtained by performing row reduction, permuting the
        pivots to the front so that the generator matrix is of the form: the
        identity matrix augmented to the right by arbitrary data.

        EXAMPLES::

            sage: from sage.coding.binary_code import *
            sage: BC = BinaryCodeClassifier()
            sage: B = BinaryCode(codes.GolayCode(GF(2)).generator_matrix())
            sage: B.apply_permutation(list(range(24,-1,-1)))
            sage: B
            Binary [24,12] linear code, generator matrix
            [011000111010100000000000]
            [001001001111100000000001]
            [011010100101100000000010]
            [001101110001100000000100]
            [010011011001100000001000]
            [010110110011000000010000]
            [011101100110000000100000]
            [000011110110100001000000]
            [000111101101000010000000]
            [001111011010000100000000]
            [010110001110101000000000]
            [011100011101010000000000]
            sage: BC.put_in_canonical_form(B)
            sage: B
            Binary [24,12] linear code, generator matrix
            [100000000000001100111001]
            [010000000000001010001111]
            [001000000000001111010010]
            [000100000000010110101010]
            [000010000000010110010101]
            [000001000000010001101101]
            [000000100000011000110110]
            [000000010000011111001001]
            [000000001000010101110011]
            [000000000100010011011110]
            [000000000010001011110101]
            [000000000001001101101110]"""
    @overload
    def put_in_canonical_form(self, B) -> Any:
        """BinaryCodeClassifier.put_in_canonical_form(self, BinaryCode B)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 3808)

        Put the code into canonical form.

        Canonical form is obtained by performing row reduction, permuting the
        pivots to the front so that the generator matrix is of the form: the
        identity matrix augmented to the right by arbitrary data.

        EXAMPLES::

            sage: from sage.coding.binary_code import *
            sage: BC = BinaryCodeClassifier()
            sage: B = BinaryCode(codes.GolayCode(GF(2)).generator_matrix())
            sage: B.apply_permutation(list(range(24,-1,-1)))
            sage: B
            Binary [24,12] linear code, generator matrix
            [011000111010100000000000]
            [001001001111100000000001]
            [011010100101100000000010]
            [001101110001100000000100]
            [010011011001100000001000]
            [010110110011000000010000]
            [011101100110000000100000]
            [000011110110100001000000]
            [000111101101000010000000]
            [001111011010000100000000]
            [010110001110101000000000]
            [011100011101010000000000]
            sage: BC.put_in_canonical_form(B)
            sage: B
            Binary [24,12] linear code, generator matrix
            [100000000000001100111001]
            [010000000000001010001111]
            [001000000000001111010010]
            [000100000000010110101010]
            [000010000000010110010101]
            [000001000000010001101101]
            [000000100000011000110110]
            [000000010000011111001001]
            [000000001000010101110011]
            [000000000100010011011110]
            [000000000010001011110101]
            [000000000001001101101110]"""

class OrbitPartition:
    """File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1261)

        Structure which keeps track of which vertices are equivalent
        under the part of the automorphism group that has already been
        seen, during search. Essentially a disjoint-set data structure*,
        which also keeps track of the minimum element and size of each
        cell of the partition, and the size of the partition.

        See :wikipedia:`Disjoint-set_data_structure`
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class PartitionStack:
    """File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1549)

        Partition stack structure for traversing the search tree during automorphism
        group computation.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def cmp(self, PartitionStackother, BinaryCodeCG) -> int:
        """PartitionStack.cmp(self, PartitionStack other, BinaryCode CG) -> int

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 2829)

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1,0,0,0,0], [0,0,1,1,1,1,0,0],
            ....:                    [0,0,0,0,1,1,1,1], [1,0,1,0,1,0,1,0]])
            sage: B = BinaryCode(M)
            sage: P = PartitionStack(4, 8)
            sage: P._refine(0, [[0,0],[1,0]], B)
            181
            sage: P._split_vertex(0, 1)
            0
            sage: P._refine(1, [[0,0]], B)
            290
            sage: P._split_vertex(1, 2)
            1
            sage: P._refine(2, [[0,1]], B)
            463
            sage: P._split_vertex(2, 3)
            2
            sage: P._refine(3, [[0,2]], B)
            1500
            sage: P._split_vertex(4, 4)
            4
            sage: P._refine(4, [[0,4]], B)
            1224
            sage: P._is_discrete(4)
            1
            sage: Q = PartitionStack(P)
            sage: Q._clear(4)
            sage: Q._split_vertex(5, 4)
            4
            sage: Q._refine(4, [[0,4]], B)
            1224
            sage: Q._is_discrete(4)
            1
            sage: Q.cmp(P, B)
            0"""
    @overload
    def cmp(self, P, B) -> Any:
        """PartitionStack.cmp(self, PartitionStack other, BinaryCode CG) -> int

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 2829)

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: M = Matrix(GF(2), [[1,1,1,1,0,0,0,0], [0,0,1,1,1,1,0,0],
            ....:                    [0,0,0,0,1,1,1,1], [1,0,1,0,1,0,1,0]])
            sage: B = BinaryCode(M)
            sage: P = PartitionStack(4, 8)
            sage: P._refine(0, [[0,0],[1,0]], B)
            181
            sage: P._split_vertex(0, 1)
            0
            sage: P._refine(1, [[0,0]], B)
            290
            sage: P._split_vertex(1, 2)
            1
            sage: P._refine(2, [[0,1]], B)
            463
            sage: P._split_vertex(2, 3)
            2
            sage: P._refine(3, [[0,2]], B)
            1500
            sage: P._split_vertex(4, 4)
            4
            sage: P._refine(4, [[0,4]], B)
            1224
            sage: P._is_discrete(4)
            1
            sage: Q = PartitionStack(P)
            sage: Q._clear(4)
            sage: Q._split_vertex(5, 4)
            4
            sage: Q._refine(4, [[0,4]], B)
            1224
            sage: Q._is_discrete(4)
            1
            sage: Q.cmp(P, B)
            0"""
    @overload
    def print_basis(self) -> Any:
        """PartitionStack.print_basis(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 2879)

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: P = PartitionStack(4, 8)
            sage: P._dangerous_dont_use_set_ents_lvls(
            ....:     list(range(8)),
            ....:     list(range(7)) + [-1],
            ....:     [4,7,12,11,1,9,3,0,2,5,6,8,10,13,14,15],
            ....:     [0]*16)
            sage: P
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1,2,3,4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2,3,4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3,4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4},{5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4},{5},{6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4},{5},{6},{7})
            sage: P._find_basis()
            sage: P.print_basis()
            basis_locations:
            4
            8
            0
            11"""
    @overload
    def print_basis(self) -> Any:
        """PartitionStack.print_basis(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 2879)

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: P = PartitionStack(4, 8)
            sage: P._dangerous_dont_use_set_ents_lvls(
            ....:     list(range(8)),
            ....:     list(range(7)) + [-1],
            ....:     [4,7,12,11,1,9,3,0,2,5,6,8,10,13,14,15],
            ....:     [0]*16)
            sage: P
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1,2,3,4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2,3,4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3,4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4,5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4},{5,6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4},{5},{6,7})
            ({4},{7},{12},{11},{1},{9},{3},{0},{2},{5},{6},{8},{10},{13},{14},{15})  ({0},{1},{2},{3},{4},{5},{6},{7})
            sage: P._find_basis()
            sage: P.print_basis()
            basis_locations:
            4
            8
            0
            11"""
    @overload
    def print_data(self) -> Any:
        """PartitionStack.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1651)

        Print all data for ``self``.

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: P = PartitionStack(2, 6)
            sage: print(P.print_data())
            nwords:4
            nrows:2
            ncols:6
            radix:32
            wd_ents:
            0
            1
            2
            3
            wd_lvls:
            12
            12
            12
            -1
            col_ents:
            0
            1
            2
            3
            4
            5
            col_lvls:
            12
            12
            12
            12
            12
            -1
            col_degs:
            0
            0
            0
            0
            0
            0
            col_counts:
            0
            0
            0
            0
            col_output:
            0
            0
            0
            0
            0
            0
            wd_degs:
            0
            0
            0
            0
            wd_counts:
            0
            0
            0
            0
            0
            0
            0
            wd_output:
            0
            0
            0
            0"""
    @overload
    def print_data(self) -> Any:
        """PartitionStack.print_data(self)

        File: /build/sagemath/src/sage/src/sage/coding/binary_code.pyx (starting at line 1651)

        Print all data for ``self``.

        EXAMPLES::

            sage: import sage.coding.binary_code
            sage: from sage.coding.binary_code import *
            sage: P = PartitionStack(2, 6)
            sage: print(P.print_data())
            nwords:4
            nrows:2
            ncols:6
            radix:32
            wd_ents:
            0
            1
            2
            3
            wd_lvls:
            12
            12
            12
            -1
            col_ents:
            0
            1
            2
            3
            4
            5
            col_lvls:
            12
            12
            12
            12
            12
            -1
            col_degs:
            0
            0
            0
            0
            0
            0
            col_counts:
            0
            0
            0
            0
            col_output:
            0
            0
            0
            0
            0
            0
            wd_degs:
            0
            0
            0
            0
            wd_counts:
            0
            0
            0
            0
            0
            0
            0
            wd_output:
            0
            0
            0
            0"""
