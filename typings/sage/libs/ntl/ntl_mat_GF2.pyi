from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class ntl_mat_GF2:
    """ntl_mat_GF2(nrows=0, ncols=0, v=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 48)

    The \\class{mat_GF2} class implements arithmetic with matrices over `F_2`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, nrows=..., ncols=..., v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 52)

                Construct a matrix over ntl.GF2.

                INPUT:

                - ``nrows`` -- number of rows
                - ``ncols`` -- number of columns
                - ``v`` -- either a list or a matrix over GF(2^x)

                EXAMPLES::

                    sage: A = ntl.mat_GF2(4,4); A
                    [[0 0 0 0]
                    [0 0 0 0]
                    [0 0 0 0]
                    [0 0 0 0]
                    ]

                    sage: A = random_matrix(GF(2),4,4); A  # random
                    [0 1 0 1]
                    [0 1 1 1]
                    [0 0 0 1]
                    [0 1 1 0]

                    sage: B = ntl.mat_GF2(A); B  # random
                    [[0 1 0 1]
                    [0 1 1 1]
                    [0 0 0 1]
                    [0 1 1 0]
                    ]

                    sage: B = ntl.mat_GF2(4, 4, A.list())
                    sage: B == A
                    True
        """
    def IsDiag(self, longn, ntl_GF2d) -> Any:
        """ntl_mat_GF2.IsDiag(self, long n, ntl_GF2 d)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 543)

        Test if X is an  n x n diagonal matrix with d on diagonal.

        EXAMPLES::

            sage: A = ntl.mat_GF2(4,4)
            sage: A[0,0] = 1
            sage: A[1,1] = 1
            sage: A[2,2] = 1
            sage: A.IsDiag(3, ntl.GF2(1))
            False
            sage: A[3,3] = 1
            sage: A.IsDiag(4, ntl.GF2(1))
            True"""
    @overload
    def IsIdent(self, n=...) -> Any:
        """ntl_mat_GF2.IsIdent(self, n=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 523)

        Test if this matrix is the n x n identity matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(4,4)
            sage: A[0,0] = 1
            sage: A[1,1] = 1
            sage: A[2,2] = 1
            sage: A.IsIdent()
            False
            sage: A[3,3] = 1
            sage: A.IsIdent()
            True"""
    @overload
    def IsIdent(self) -> Any:
        """ntl_mat_GF2.IsIdent(self, n=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 523)

        Test if this matrix is the n x n identity matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(4,4)
            sage: A[0,0] = 1
            sage: A[1,1] = 1
            sage: A[2,2] = 1
            sage: A.IsIdent()
            False
            sage: A[3,3] = 1
            sage: A.IsIdent()
            True"""
    @overload
    def IsIdent(self) -> Any:
        """ntl_mat_GF2.IsIdent(self, n=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 523)

        Test if this matrix is the n x n identity matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(4,4)
            sage: A[0,0] = 1
            sage: A[1,1] = 1
            sage: A[2,2] = 1
            sage: A.IsIdent()
            False
            sage: A[3,3] = 1
            sage: A.IsIdent()
            True"""
    def IsZero(self) -> Any:
        """ntl_mat_GF2.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 441)

        Return \\code{True} if this matrix contains only zeroes, and \\code{False} otherwise.

        EXAMPLES::

            sage: A = random_matrix(GF(2), 10, 10)
            sage: Abar = ntl.mat_GF2(A)
            sage: Abar.IsZero()
            False
            sage: Abar = ntl.mat_GF2(10,10)
            sage: Abar.IsZero()
            True"""
    @overload
    def NumCols(self) -> Any:
        """ntl_mat_GF2.NumCols(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 285)

        Return the number of columns of this matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(10,10)
            sage: A.NumCols()
            10"""
    @overload
    def NumCols(self) -> Any:
        """ntl_mat_GF2.NumCols(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 285)

        Return the number of columns of this matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(10,10)
            sage: A.NumCols()
            10"""
    @overload
    def NumRows(self) -> Any:
        """ntl_mat_GF2.NumRows(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 273)

        Return the number of rows of this matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(10,10)
            sage: A.NumRows()
            10"""
    @overload
    def NumRows(self) -> Any:
        """ntl_mat_GF2.NumRows(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 273)

        Return the number of rows of this matrix.

        EXAMPLES::

            sage: A = ntl.mat_GF2(10,10)
            sage: A.NumRows()
            10"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_GF2.determinant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 361)

        Return the determinant.

        EXAMPLES::

            sage: A = ntl.mat_GF2(3,3,range(9))
            sage: A.determinant()
            0
            sage: A = ntl.mat_GF2(3,3,[1,0,0, 0,1,0, 0,0,1])
            sage: A.determinant()
            1"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_GF2.determinant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 361)

        Return the determinant.

        EXAMPLES::

            sage: A = ntl.mat_GF2(3,3,range(9))
            sage: A.determinant()
            0
            sage: A = ntl.mat_GF2(3,3,[1,0,0, 0,1,0, 0,0,1])
            sage: A.determinant()
            1"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_GF2.determinant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 361)

        Return the determinant.

        EXAMPLES::

            sage: A = ntl.mat_GF2(3,3,range(9))
            sage: A.determinant()
            0
            sage: A = ntl.mat_GF2(3,3,[1,0,0, 0,1,0, 0,0,1])
            sage: A.determinant()
            1"""
    @overload
    def gauss(self, ncols=...) -> Any:
        """ntl_mat_GF2.gauss(self, ncols=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 380)

        Perform unitary row operations so as to bring this matrix
        into row echelon form (not reduced!).

        If the optional argument ``ncols`` is supplied, stops when
        first ``ncols`` columns are in echelon form.  The return value is
        the rank (or the rank of the first ``ncols`` columns).

        INPUT:

        - ``ncols`` -- number of columns to process (default: all)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 10, 10)
            sage: Abar = ntl.mat_GF2(A)
            sage: A.rank() == Abar.gauss()
            True
            sage: Abar  # random
            [[1 1 1 1 0 1 0 1 1 0]
            [0 1 1 1 0 1 1 0 0 1]
            [0 0 1 1 1 1 0 0 0 0]
            [0 0 0 1 0 0 1 1 1 1]
            [0 0 0 0 1 1 0 1 0 0]
            [0 0 0 0 0 1 1 1 0 1]
            [0 0 0 0 0 0 0 1 0 1]
            [0 0 0 0 0 0 0 0 0 1]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            ]

        ``Abar`` is in row echelon form now::

            sage: first_nonzero_indices = [Abar._sage_().row(i).nonzero_positions()[0] for i in range(A.rank())]
            sage: all(first_nonzero_indices[i] < first_nonzero_indices[i+1] for i in range(A.rank()-1))
            True

        ``Abar`` is not reduced::

            sage: all(Abar._sage_().row(i).nonzero_positions() == [] for i in range(A.rank(), Abar.NumRows()))
            True"""
    @overload
    def gauss(self) -> Any:
        """ntl_mat_GF2.gauss(self, ncols=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 380)

        Perform unitary row operations so as to bring this matrix
        into row echelon form (not reduced!).

        If the optional argument ``ncols`` is supplied, stops when
        first ``ncols`` columns are in echelon form.  The return value is
        the rank (or the rank of the first ``ncols`` columns).

        INPUT:

        - ``ncols`` -- number of columns to process (default: all)

        EXAMPLES::

            sage: A = random_matrix(GF(2), 10, 10)
            sage: Abar = ntl.mat_GF2(A)
            sage: A.rank() == Abar.gauss()
            True
            sage: Abar  # random
            [[1 1 1 1 0 1 0 1 1 0]
            [0 1 1 1 0 1 1 0 0 1]
            [0 0 1 1 1 1 0 0 0 0]
            [0 0 0 1 0 0 1 1 1 1]
            [0 0 0 0 1 1 0 1 0 0]
            [0 0 0 0 0 1 1 1 0 1]
            [0 0 0 0 0 0 0 1 0 1]
            [0 0 0 0 0 0 0 0 0 1]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            ]

        ``Abar`` is in row echelon form now::

            sage: first_nonzero_indices = [Abar._sage_().row(i).nonzero_positions()[0] for i in range(A.rank())]
            sage: all(first_nonzero_indices[i] < first_nonzero_indices[i+1] for i in range(A.rank()-1))
            True

        ``Abar`` is not reduced::

            sage: all(Abar._sage_().row(i).nonzero_positions() == [] for i in range(A.rank(), Abar.NumRows()))
            True"""
    def image(self) -> Any:
        """ntl_mat_GF2.image(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 561)

        If A is this matrix and X the matrix returned by this function
        then, the rows of X are computed as basis of A's row space.
        X is in row echelon form.

        EXAMPLES::

            sage: A = random_matrix(GF(2),10,10)
            sage: Abar = ntl.mat_GF2(A)
            sage: A_image = A.image().matrix()
            sage: Abar_image =  Abar.image()._sage_()
            sage: A_image.row_space() == Abar_image.row_space()
            True

        X is in row echelon form::

            sage: first_nonzero_indices = [row.nonzero_positions()[0] for row in Abar_image.rows()]
            sage: all(first_nonzero_indices[i] < first_nonzero_indices[i+1] for i in range(Abar_image.nrows() - 1))
            True"""
    @overload
    def kernel(self) -> Any:
        """ntl_mat_GF2.kernel(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 588)

        Compute a basis for the kernel of the map x -> x*A. where x
        is a row vector.

        EXAMPLES::

            sage: A = random_matrix(GF(2),10,10)
            sage: Abar = ntl.mat_GF2(A)
            sage: K_abar = Abar.kernel(); K_abar  # random
            [[0 0 0 1 1 0 1 0 1 0]
            [1 1 1 0 1 1 0 1 0 0]
            ]
            sage: (K_abar*Abar).IsZero()
            True
            sage: K_a = A.kernel().matrix()
            sage: K_a.row_space() == K_abar._sage_().row_space()
            True"""
    @overload
    def kernel(self) -> Any:
        """ntl_mat_GF2.kernel(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 588)

        Compute a basis for the kernel of the map x -> x*A. where x
        is a row vector.

        EXAMPLES::

            sage: A = random_matrix(GF(2),10,10)
            sage: Abar = ntl.mat_GF2(A)
            sage: K_abar = Abar.kernel(); K_abar  # random
            [[0 0 0 1 1 0 1 0 1 0]
            [1 1 1 0 1 1 0 1 0 0]
            ]
            sage: (K_abar*Abar).IsZero()
            True
            sage: K_a = A.kernel().matrix()
            sage: K_a.row_space() == K_abar._sage_().row_space()
            True"""
    @overload
    def kernel(self) -> Any:
        """ntl_mat_GF2.kernel(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 588)

        Compute a basis for the kernel of the map x -> x*A. where x
        is a row vector.

        EXAMPLES::

            sage: A = random_matrix(GF(2),10,10)
            sage: Abar = ntl.mat_GF2(A)
            sage: K_abar = Abar.kernel(); K_abar  # random
            [[0 0 0 1 1 0 1 0 1 0]
            [1 1 1 0 1 1 0 1 0 0]
            ]
            sage: (K_abar*Abar).IsZero()
            True
            sage: K_a = A.kernel().matrix()
            sage: K_a.row_space() == K_abar._sage_().row_space()
            True"""
    @overload
    def list(self) -> Any:
        """ntl_mat_GF2.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 427)

        Return a list of the entries in this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(2), 4, 4)
            sage: Abar = ntl.mat_GF2(A)
            sage: A.list() == Abar.list()
            True"""
    @overload
    def list(self) -> Any:
        """ntl_mat_GF2.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 427)

        Return a list of the entries in this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(2), 4, 4)
            sage: Abar = ntl.mat_GF2(A)
            sage: A.list() == Abar.list()
            True"""
    @overload
    def transpose(self) -> Any:
        """ntl_mat_GF2.transpose(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 483)

        Return the transposed matrix of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(2), 10, 10)
            sage: Abar = ntl.mat_GF2(A)
            sage: Abar_t = Abar.transpose()
            sage: A_t = A.transpose()
            sage: A_t == Abar_t._sage_()
            True"""
    @overload
    def transpose(self) -> Any:
        """ntl_mat_GF2.transpose(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 483)

        Return the transposed matrix of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(2), 10, 10)
            sage: Abar = ntl.mat_GF2(A)
            sage: Abar_t = Abar.transpose()
            sage: A_t = A.transpose()
            sage: A_t == Abar_t._sage_()
            True"""
    @overload
    def transpose(self) -> Any:
        """ntl_mat_GF2.transpose(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 483)

        Return the transposed matrix of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(2), 10, 10)
            sage: Abar = ntl.mat_GF2(A)
            sage: Abar_t = Abar.transpose()
            sage: A_t = A.transpose()
            sage: A_t == Abar_t._sage_()
            True"""
    def __add__(self, ntl_mat_GF2self, other) -> Any:
        """ntl_mat_GF2.__add__(ntl_mat_GF2 self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 192)

        EXAMPLES::

            sage: A = random_matrix(GF(2),4,4)
            sage: B = random_matrix(GF(2),4,4)
            sage: c = ntl.mat_GF2(A) + ntl.mat_GF2(B)
            sage: c._sage_() == A + B
            True"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, ij) -> Any:
        """ntl_mat_GF2.__getitem__(self, ij)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 332)

        EXAMPLES::

            sage: A = ntl.mat_GF2(3,3,range(9))
            sage: A[0,0]
            0
            sage: A[1,2]
            1"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __invert__(self) -> Any:
        """ntl_mat_GF2.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 502)

        Return `X = A^{-1}`; an error is raised if A is singular.

        EXAMPLES::

            sage: l = [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0,             ....:      0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0,             ....:      1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0,             ....:      0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
            sage: A = ntl.mat_GF2(8,8,l)
            sage: E = ~A*A
            sage: E.IsIdent()
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_mat_GF2self, other) -> Any:
        """ntl_mat_GF2.__mul__(ntl_mat_GF2 self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 156)

        EXAMPLES::

            sage: A = random_matrix(GF(2),4,4)
            sage: B = random_matrix(GF(2),4,4)
            sage: c = ntl.mat_GF2(A)*ntl.mat_GF2(B)
            sage: c._sage_() == A*B
            True"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_mat_GF2.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 210)

        EXAMPLES::

            sage: A = random_matrix(GF(2),4,4)
            sage: (-ntl.mat_GF2(A))._sage_() == -A
            True"""
    def __pow__(self, ntl_mat_GF2self, longe, ignored) -> Any:
        """ntl_mat_GF2.__pow__(ntl_mat_GF2 self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 224)

        EXAMPLES::

            sage: A = random_matrix(GF(2),4,4)
            sage: Abar = ntl.mat_GF2(A)
            sage: (Abar^0)._sage_() == A^0
            True
            sage: (Abar^1)._sage_() == A^1
            True
            sage: (Abar^2)._sage_() == A^2
            True
            sage: (Abar^3)._sage_() == A^3
            True"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_mat_GF2.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 132)

        EXAMPLES::

            sage: A = random_matrix(GF(2),4,4)
            sage: B = ntl.mat_GF2(A)
            sage: loads(dumps(B)) == B # indirect doctest
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __setitem__(self, ij, x) -> Any:
        """ntl_mat_GF2.__setitem__(self, ij, x)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 297)

        EXAMPLES::

            sage: A = ntl.mat_GF2(5,5)
            sage: A[0,0] = 1
            sage: A[0,2] = 1
            sage: A
            [[1 0 1 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            ]"""
    def __sub__(self, ntl_mat_GF2self, other) -> Any:
        """ntl_mat_GF2.__sub__(ntl_mat_GF2 self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2.pyx (starting at line 174)

        EXAMPLES::

            sage: A = random_matrix(GF(2),4,4)
            sage: B = random_matrix(GF(2),4,4)
            sage: c = ntl.mat_GF2(A) - ntl.mat_GF2(B)
            sage: c._sage_() == A - B
            True"""
