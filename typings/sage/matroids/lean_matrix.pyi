import _cython_3_2_1
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matrix.constructor import matrix as matrix
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict
generic_identity: _cython_3_2_1.cython_function_or_method

class BinaryMatrix(LeanMatrix):
    """BinaryMatrix(long m, long n, M=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 938)

    Binary matrix class. Entries are stored bit-packed into integers.

    INPUT:

    - ``m`` -- number of rows
    - ``n`` -- number of columns
    - ``M`` -- (default: ``None``) ``Matrix`` or ``BinaryMatrix`` instance.
      Assumption: dimensions of ``M`` are at most ``m`` by ``n``.
    - ``ring`` -- (default: ``None``) ignored

    EXAMPLES::

        sage: from sage.matroids.lean_matrix import *
        sage: A = BinaryMatrix(2, 2, Matrix(GF(7), [[0, 0], [0, 0]]))
        sage: B = BinaryMatrix(2, 2, ring=GF(5))
        sage: C = BinaryMatrix(2, 2)
        sage: A == B and A == C
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longm, longn, M=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 983)

                See the class docstring for full specification.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import *
                    sage: A = BinaryMatrix(2, 2, Matrix(GF(4, 'x'), [[0, 0], [0, 0]]))  # indirect doctest
                    sage: A.nrows()
                    2
        """
    @overload
    def base_ring(self) -> Any:
        """BinaryMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1131)

        Return `GF(2)`.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = BinaryMatrix(4, 4)
            sage: A.base_ring()
            Finite Field of size 2"""
    @overload
    def base_ring(self) -> Any:
        """BinaryMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1131)

        Return `GF(2)`.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = BinaryMatrix(4, 4)
            sage: A.base_ring()
            Finite Field of size 2"""
    @overload
    def characteristic(self) -> Any:
        """BinaryMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1145)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = BinaryMatrix(3, 4)
            sage: A.characteristic()
            2"""
    @overload
    def characteristic(self) -> Any:
        """BinaryMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1145)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = BinaryMatrix(3, 4)
            sage: A.characteristic()
            2"""
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
    def __neg__(self) -> Any:
        """BinaryMatrix.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1460)

        Negate the matrix.

        In characteristic 2, this does nothing.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = BinaryMatrix(2, 2, Matrix(GF(2), [[1, 0], [0, 1]]))
            sage: B = -A  # indirect doctest
            sage: B == A
            True"""
    def __reduce__(self) -> Any:
        """BinaryMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1516)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = BinaryMatrix(2, 5)
            sage: A == loads(dumps(A))  # indirect doctest
            True
            sage: C = BinaryMatrix(2, 2, Matrix(GF(2), [[1, 1], [0, 1]]))
            sage: C == loads(dumps(C))
            True"""

class GenericMatrix(LeanMatrix):
    """GenericMatrix(long nrows, long ncols, M=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 644)

    Matrix over arbitrary Sage ring.

    INPUT:

    - ``nrows`` -- number of rows
    - ``ncols`` -- number of columns
    - ``M`` -- (default: ``None``) a ``Matrix`` or ``GenericMatrix`` of
      dimensions at most ``m*n``
    - ``ring`` -- (default: ``None``) a Sage ring

    .. NOTE::

        This class is intended for internal use by the LinearMatroid class
        only. Hence it does not derive from ``SageObject``. If ``A`` is a
        LeanMatrix instance, and you need access from other parts of Sage,
        use ``Matrix(A)`` instead.

        If the constructor is fed a GenericMatrix instance, the ``ring``
        argument is ignored. Otherwise, the matrix entries
        will be converted to the appropriate ring.

    EXAMPLES::

        sage: M = Matroid(ring=GF(5), matrix=[[1, 0, 1, 1, 1], [0, 1, 1, 2, 3]])  # indirect doctest
        sage: M.is_isomorphic(matroids.Uniform(2, 5))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longnrows, longncols, M=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 674)

                See the class docstring for full information.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import *
                    sage: A = GenericMatrix(2, 2, Matrix(GF(3), [[0, 0], [0, 0]]))  # indirect doctest
                    sage: B = GenericMatrix(2, 2, ring=GF(3))
                    sage: A == B
                    True
        """
    @overload
    def base_ring(self) -> Any:
        """GenericMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 788)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import GenericMatrix
            sage: A = GenericMatrix(3, 4, ring=GF(5))
            sage: A.base_ring()
            Finite Field of size 5"""
    @overload
    def base_ring(self) -> Any:
        """GenericMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 788)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import GenericMatrix
            sage: A = GenericMatrix(3, 4, ring=GF(5))
            sage: A.base_ring()
            Finite Field of size 5"""
    @overload
    def characteristic(self) -> Any:
        """GenericMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 801)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import GenericMatrix
            sage: A = GenericMatrix(3, 4, ring=GF(5))
            sage: A.characteristic()
            5"""
    @overload
    def characteristic(self) -> Any:
        """GenericMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 801)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import GenericMatrix
            sage: A = GenericMatrix(3, 4, ring=GF(5))
            sage: A.characteristic()
            5"""
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
        """GenericMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 914)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = GenericMatrix(2, 5, ring=QQ)
            sage: A == loads(dumps(A))  # indirect doctest
            True
            sage: C = GenericMatrix(2, 2, Matrix(GF(3), [[1, 1], [0, 1]]))
            sage: C == loads(dumps(C))
            True"""

class LeanMatrix:
    """LeanMatrix(long m, long n, M=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 48)

    Lean matrices

    Sage's matrix classes are powerful, versatile, and often very fast. However, their performance with regard to pivoting
    (pretty much the only task performed on them within the context of matroids) leaves something to be desired. The LeanMatrix
    classes provide the LinearMatroid classes with a custom, light-weight data structure to store and manipulate matrices.

    This is the abstract base class. Most methods are not implemented; this is only to fix the interface.

    .. NOTE::

        This class is intended for internal use by the LinearMatroid class only. Hence it does not derive from ``SageObject``.
        If ``A`` is a LeanMatrix instance, and you need access from other parts of Sage, use ``Matrix(A)`` instead.

    EXAMPLES::

        sage: M = Matroid(ring=GF(5), matrix=[[1, 0, 1, 1, 1], [0, 1, 1, 2, 3]])  # indirect doctest
        sage: M.is_isomorphic(matroids.Uniform(2, 5))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longm, longn, M=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 69)

                Initialize a lean matrix; see class documentation for more info.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import LeanMatrix
                    sage: A = LeanMatrix(3, 4)
                    sage: A.ncols()
                    4
        """
    @overload
    def base_ring(self) -> Any:
        """LeanMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 200)

        Return the base ring.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import LeanMatrix
            sage: A = LeanMatrix(3, 4)
            sage: A.base_ring()
            Traceback (most recent call last):
            ...
            NotImplementedError: subclasses need to implement this"""
    @overload
    def base_ring(self) -> Any:
        """LeanMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 200)

        Return the base ring.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import LeanMatrix
            sage: A = LeanMatrix(3, 4)
            sage: A.base_ring()
            Traceback (most recent call last):
            ...
            NotImplementedError: subclasses need to implement this"""
    @overload
    def characteristic(self) -> Any:
        """LeanMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 215)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import GenericMatrix
            sage: A = GenericMatrix(3, 4, ring=GF(5))
            sage: A.characteristic()
            5"""
    @overload
    def characteristic(self) -> Any:
        """LeanMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 215)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import GenericMatrix
            sage: A = GenericMatrix(3, 4, ring=GF(5))
            sage: A.characteristic()
            5"""
    @overload
    def ncols(self) -> long:
        """LeanMatrix.ncols(self) -> long

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 174)

        Return the number of columns.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import LeanMatrix
            sage: A = LeanMatrix(3, 4)
            sage: A.ncols()
            4"""
    @overload
    def ncols(self) -> Any:
        """LeanMatrix.ncols(self) -> long

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 174)

        Return the number of columns.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import LeanMatrix
            sage: A = LeanMatrix(3, 4)
            sage: A.ncols()
            4"""
    @overload
    def nrows(self) -> long:
        """LeanMatrix.nrows(self) -> long

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 187)

        Return the number of rows.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import LeanMatrix
            sage: A = LeanMatrix(3, 4)
            sage: A.nrows()
            3"""
    @overload
    def nrows(self) -> Any:
        """LeanMatrix.nrows(self) -> long

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 187)

        Return the number of rows.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import LeanMatrix
            sage: A = LeanMatrix(3, 4)
            sage: A.nrows()
            3"""
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
    def __mul__(self, left, right) -> Any:
        """LeanMatrix.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 378)

        Multiply two matrices, or multiply a matrix with a constant from the
        base ring.

        Only works if both matrices are of the same type, or if the constant
        is the first operand and can be coerced into the base ring.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = GenericMatrix(2, 2, Matrix(GF(2), [[1, 0], [1, 1]]))
            sage: B = GenericMatrix(3, 2, Matrix(GF(2), [[1, 0], [1, 0], [1, 0]]))
            sage: B * A
            LeanMatrix instance with 3 rows and 2 columns over Finite Field of size 2"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """LeanMatrix.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 411)

        Return a matrix ``B`` such that ``self + B`` is the all-zero matrix.

        Note that the `` + `` operator is currently not supported.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = GenericMatrix(2, 2, Matrix(GF(3), [[1, 0], [0, 1]]))
            sage: C = -A
            sage: -C == A
            True"""
    def __reduce__(self) -> Any:
        """LeanMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 479)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = LeanMatrix(2, 5)
            sage: A == loads(dumps(A))  # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedError: subclasses need to implement this"""
    def __rmul__(self, other):
        """Return value*self."""

class PlusMinusOneMatrix(LeanMatrix):
    """PlusMinusOneMatrix(long nrows, long ncols, M=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2728)

    Matrix with nonzero entries of `\\pm 1`.

    INPUT:

    - ``nrows`` -- number of rows
    - ``ncols`` -- number of columns
    - ``M`` -- (default: ``None``) a ``Matrix`` or ``GenericMatrix`` of
      dimensions at most ``m*n``

    .. NOTE::

        This class is intended for internal use by the
        :class:`~sage.matroids.linear_matroid.LinearMatroid` class
        only. Hence it does not derive from ``SageObject``.
        If ``A`` is a :class:`~sage.matroids.lean_matrix.LeanMatrix`
        instance, and you need access from other parts of Sage,
        use ``Matrix(A)`` instead.

        This class is mainly intended for use with the
        :class:`~sage.matroids.linear_matroid.RegularMatroid` class,
        so entries are assumed to be `\\pm 1` or `0`. No overflow checking
        takes place!

    EXAMPLES::

        sage: M = Matroid(graphs.CompleteGraph(4).incidence_matrix(oriented=True),  # indirect doctest
        ....:             regular=True)
        sage: M.is_isomorphic(matroids.Wheel(3))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longnrows, longncols, M=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2776)

                See the class docstring for full information.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import *
                    sage: A = PlusMinusOneMatrix(2, 2, Matrix(GF(3), [[0, 0], [0, 0]]))  # indirect doctest
                    sage: B = PlusMinusOneMatrix(2, 2)
                    sage: A == B
                    True
        """
    @overload
    def base_ring(self) -> Any:
        """PlusMinusOneMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2914)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import PlusMinusOneMatrix
            sage: A = PlusMinusOneMatrix(3, 4)
            sage: A.base_ring()
            Integer Ring"""
    @overload
    def base_ring(self) -> Any:
        """PlusMinusOneMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2914)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import PlusMinusOneMatrix
            sage: A = PlusMinusOneMatrix(3, 4)
            sage: A.base_ring()
            Integer Ring"""
    @overload
    def characteristic(self) -> Any:
        """PlusMinusOneMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2927)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import PlusMinusOneMatrix
            sage: A = PlusMinusOneMatrix(3, 4)
            sage: A.characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """PlusMinusOneMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2927)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import PlusMinusOneMatrix
            sage: A = PlusMinusOneMatrix(3, 4)
            sage: A.characteristic()
            0"""
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
        """PlusMinusOneMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3147)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = PlusMinusOneMatrix(2, 5)
            sage: A == loads(dumps(A))  # indirect doctest
            True
            sage: C = PlusMinusOneMatrix(2, 2, Matrix(GF(3), [[1, 1], [0, 1]]))
            sage: C == loads(dumps(C))
            True"""

class QuaternaryMatrix(LeanMatrix):
    """QuaternaryMatrix(long m, long n, M=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2104)

    Matrices over GF(4).

    INPUT:

    - ``m`` -- number of rows
    - ``n`` -- number of columns
    - ``M`` -- (default: ``None``) ``QuaternaryMatrix`` or ``LeanMatrix`` or
      (Sage) ``Matrix`` instance. If not given, new matrix will be filled with
      zeroes. Assumption: ``M`` has dimensions at most ``m`` times ``n``.
    - ``ring`` -- (default: ``None``) a copy of GF(4); useful for specifying
      generator name

    EXAMPLES::

        sage: from sage.matroids.lean_matrix import *
        sage: A = QuaternaryMatrix(2, 2, Matrix(GF(4, 'x'), [[0, 0], [0, 0]]))
        sage: B = QuaternaryMatrix(2, 2, GenericMatrix(2, 2, ring=GF(4, 'x')))
        sage: C = QuaternaryMatrix(2, 2, ring=GF(4, 'x'))
        sage: A == B and A == C
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longm, longn, M=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2158)

                See the class docstring for full specification.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import *
                    sage: A = QuaternaryMatrix(2, 2, Matrix(GF(4, 'x'), [[0, 0], [0, 0]]))  # indirect doctest
                    sage: A.nrows()
                    2
        """
    @overload
    def base_ring(self) -> Any:
        """QuaternaryMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2383)

        Return copy of `GF(4)` with appropriate generator.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = QuaternaryMatrix(2, 2, ring=GF(4, 'f'))
            sage: A.base_ring()
            Finite Field in f of size 2^2"""
    @overload
    def base_ring(self) -> Any:
        """QuaternaryMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2383)

        Return copy of `GF(4)` with appropriate generator.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = QuaternaryMatrix(2, 2, ring=GF(4, 'f'))
            sage: A.base_ring()
            Finite Field in f of size 2^2"""
    @overload
    def characteristic(self) -> Any:
        """QuaternaryMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2396)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = QuaternaryMatrix(200, 5000, ring=GF(4, 'x'))
            sage: A.characteristic()
            2"""
    @overload
    def characteristic(self) -> Any:
        """QuaternaryMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2396)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = QuaternaryMatrix(200, 5000, ring=GF(4, 'x'))
            sage: A.characteristic()
            2"""
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
    def __neg__(self) -> Any:
        """QuaternaryMatrix.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2616)

        Negate the matrix.

        In characteristic 2, this does nothing.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = QuaternaryMatrix(2, 2, Matrix(GF(4, 'x'), [[1, 0], [0, 1]]))
            sage: B = -A  # indirect doctest
            sage: B == A
            True"""
    def __reduce__(self) -> Any:
        """QuaternaryMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2676)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = QuaternaryMatrix(2, 5, ring=GF(4, 'x'))
            sage: A == loads(dumps(A))  # indirect doctest
            True
            sage: C = QuaternaryMatrix(2, 2, Matrix(GF(4, 'x'), [[1, 1], [0, 1]]))
            sage: C == loads(dumps(C))
            True"""

class RationalMatrix(LeanMatrix):
    """RationalMatrix(long nrows, long ncols, M=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3172)

    Matrix over the rationals.

    INPUT:

    - ``nrows`` -- number of rows
    - ``ncols`` -- number of columns
    - ``M`` -- (default: ``None``) a ``Matrix`` or ``GenericMatrix`` of
      dimensions at most ``m * n``

    EXAMPLES::

        sage: M = Matroid(graphs.CompleteGraph(4).incidence_matrix(oriented=True))  # indirect doctest
        sage: M.is_isomorphic(matroids.Wheel(3))
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longnrows, longncols, M=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3210)

                See the class docstring for full information.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import RationalMatrix, PlusMinusOneMatrix
                    sage: A = RationalMatrix(2, 2, Matrix(GF(3), [[0, 0], [0, 0]]))
                    sage: B = RationalMatrix(2, 2)
                    sage: A == B
                    True

                    sage: IM = PlusMinusOneMatrix(2, 2, Matrix([[-1, 0], [0, 1]]))
                    sage: A = RationalMatrix(2, 2, IM)
                    sage: B = RationalMatrix(2, 2, Matrix(QQ, [[-1, 0], [0, 1]]))
                    sage: A == B
                    True
        """
    @overload
    def base_ring(self) -> Any:
        """RationalMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3378)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import RationalMatrix
            sage: A = RationalMatrix(3, 4)
            sage: A.base_ring()
            Rational Field"""
    @overload
    def base_ring(self) -> Any:
        """RationalMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3378)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import RationalMatrix
            sage: A = RationalMatrix(3, 4)
            sage: A.base_ring()
            Rational Field"""
    @overload
    def characteristic(self) -> Any:
        """RationalMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3391)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import RationalMatrix
            sage: A = RationalMatrix(3, 4)
            sage: A.characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """RationalMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3391)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import RationalMatrix
            sage: A = RationalMatrix(3, 4)
            sage: A.characteristic()
            0"""
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
        """RationalMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 3640)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import RationalMatrix
            sage: A = RationalMatrix(2, 5)
            sage: A == loads(dumps(A))  # indirect doctest
            True
            sage: C = RationalMatrix(2, 2, matrix(QQ, [[1, 1/3], [0, -1]]))
            sage: C == loads(dumps(C))
            True"""

class TernaryMatrix(LeanMatrix):
    """TernaryMatrix(long m, long n, M=None, ring=None)

    File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1547)

    Ternary matrix class. Entries are stored bit-packed into integers.

    INPUT:

    - ``m`` -- number of rows
    - ``n`` -- number of columns
    - ``M`` -- (default: ``None``) ``Matrix`` or ``TernaryMatrix`` instance.
      Assumption: dimensions of ``M`` are at most ``m`` by ``n``.
    - ``ring`` -- (default: ``None``) ignored

    EXAMPLES::

        sage: from sage.matroids.lean_matrix import *
        sage: A = TernaryMatrix(2, 2, Matrix(GF(7), [[0, 0], [0, 0]]))
        sage: B = TernaryMatrix(2, 2, ring=GF(5))
        sage: C = TernaryMatrix(2, 2)
        sage: A == B and A == C
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longm, longn, M=..., ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1606)

                See the class docstring for full specification.

                EXAMPLES::

                    sage: from sage.matroids.lean_matrix import *
                    sage: A = TernaryMatrix(2, 2, Matrix(GF(4, 'x'), [[0, 0], [0, 0]]))  # indirect doctest
                    sage: A.nrows()
                    2
        """
    @overload
    def base_ring(self) -> Any:
        """TernaryMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1782)

        Return GF(3).

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = TernaryMatrix(3, 3)
            sage: A.base_ring()
            Finite Field of size 3"""
    @overload
    def base_ring(self) -> Any:
        """TernaryMatrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1782)

        Return GF(3).

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = TernaryMatrix(3, 3)
            sage: A.base_ring()
            Finite Field of size 3"""
    @overload
    def characteristic(self) -> Any:
        """TernaryMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1796)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = TernaryMatrix(3, 4)
            sage: A.characteristic()
            3"""
    @overload
    def characteristic(self) -> Any:
        """TernaryMatrix.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 1796)

        Return the characteristic of ``self.base_ring()``.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = TernaryMatrix(3, 4)
            sage: A.characteristic()
            3"""
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
        """TernaryMatrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matroids/lean_matrix.pyx (starting at line 2074)

        Save the object.

        EXAMPLES::

            sage: from sage.matroids.lean_matrix import *
            sage: A = TernaryMatrix(2, 5)
            sage: A == loads(dumps(A))  # indirect doctest
            True
            sage: C = TernaryMatrix(2, 2, Matrix(GF(3), [[1, 1], [0, 1]]))
            sage: C == loads(dumps(C))
            True"""
