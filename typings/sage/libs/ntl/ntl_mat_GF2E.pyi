from sage.libs.ntl.ntl_GF2EContext import ntl_GF2EContext as ntl_GF2EContext
from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class ntl_mat_GF2E:
    """ntl_mat_GF2E(modulus=None, nrows=0, ncols=0, v=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 48)

    The \\class{mat_GF2E} class implements arithmetic with matrices over `GF(2**x)`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, modulus=..., nrows=..., ncols=..., v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 52)

                Construct a matrix over ntl.GF2E.

                INPUT:

                - ``modulus`` -- GF2E context
                - ``nrows`` -- number of rows
                - ``ncols`` -- number of columns
                - ``v`` -- either a list or a matrix over GF(2^x)

                EXAMPLES::

                    sage: k.<a> = GF(2^4)
                    sage: ctx = ntl.GF2EContext(k)
                    sage: ntl.GF2XHexOutput(1)
                    sage: ntl.mat_GF2E(ctx, 5,5, [0..24])
                    [[0x0 0x1 0x2 0x3 0x4]
                    [0x5 0x6 0x7 0x8 0x9]
                    [0xa 0xb 0xc 0xd 0xe]
                    [0xf 0x3 0x2 0x1 0x0]
                    [0x7 0x6 0x5 0x4 0xb]
                    ]
                    sage: ntl.mat_GF2E(ctx, 5,5)
                    [[0x0 0x0 0x0 0x0 0x0]
                    [0x0 0x0 0x0 0x0 0x0]
                    [0x0 0x0 0x0 0x0 0x0]
                    [0x0 0x0 0x0 0x0 0x0]
                    [0x0 0x0 0x0 0x0 0x0]
                    ]
                    sage: A = matrix(k, 5, 5, [k.from_integer(i % 2^4) for i in range(25)])
                    sage: ntl.mat_GF2E(ctx, A)
                    [[0x0 0x1 0x2 0x3 0x4]
                    [0x5 0x6 0x7 0x8 0x9]
                    [0xa 0xb 0xc 0xd 0xe]
                    [0xf 0x0 0x1 0x2 0x3]
                    [0x4 0x5 0x6 0x7 0x8]
                    ]
        """
    def IsDiag(self, longn, ntl_GF2Ed) -> Any:
        """ntl_mat_GF2E.IsDiag(self, long n, ntl_GF2E d)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 605)

        Test if X is an  n x n diagonal matrix with d on diagonal.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 3,3,[[0,1],0,0, 0,[0,1],0, 0,0,[0,1]])
            sage: m.IsDiag(2, ntl.GF2E([0,1],ctx))
            False
            sage: m.IsDiag(3, ntl.GF2E([0,1],ctx))
            True"""
    def IsIdent(self, n=...) -> Any:
        """ntl_mat_GF2E.IsIdent(self, n=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 588)

        Test if `A` is the `n \\times n` identity matrix.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ~m
            sage: o = n*m
            sage: o.IsIdent()
            True"""
    @overload
    def IsZero(self) -> Any:
        """ntl_mat_GF2E.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 494)

        Return ``True`` if ``self`` is zero, and ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ntl.mat_GF2E(ctx, 5,5)
            sage: m.IsZero()
            False
            sage: n.IsZero()
            True"""
    @overload
    def IsZero(self) -> Any:
        """ntl_mat_GF2E.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 494)

        Return ``True`` if ``self`` is zero, and ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ntl.mat_GF2E(ctx, 5,5)
            sage: m.IsZero()
            False
            sage: n.IsZero()
            True"""
    @overload
    def IsZero(self) -> Any:
        """ntl_mat_GF2E.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 494)

        Return ``True`` if ``self`` is zero, and ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ntl.mat_GF2E(ctx, 5,5)
            sage: m.IsZero()
            False
            sage: n.IsZero()
            True"""
    @overload
    def NumCols(self) -> Any:
        """ntl_mat_GF2E.NumCols(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 349)

        Return the number of columns in ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24]) ; m.NumCols()
            5"""
    @overload
    def NumCols(self) -> Any:
        """ntl_mat_GF2E.NumCols(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 349)

        Return the number of columns in ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24]) ; m.NumCols()
            5"""
    @overload
    def NumRows(self) -> Any:
        """ntl_mat_GF2E.NumRows(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 337)

        Return the number of rows in ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24]) ; m.NumRows()
            5"""
    @overload
    def NumRows(self) -> Any:
        """ntl_mat_GF2E.NumRows(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 337)

        Return the number of rows in ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24]) ; m.NumRows()
            5"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_GF2E.determinant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 430)

        Return the determinant.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: ntl.GF2XHexOutput(0)
            sage: ntl.mat_GF2E(ctx, 5,5,[0..24]).determinant()
            [0 1 0 1 1 1 1]
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).determinant()
            [0 1 1 0 0 1]"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_GF2E.determinant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 430)

        Return the determinant.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: ntl.GF2XHexOutput(0)
            sage: ntl.mat_GF2E(ctx, 5,5,[0..24]).determinant()
            [0 1 0 1 1 1 1]
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).determinant()
            [0 1 1 0 0 1]"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_GF2E.determinant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 430)

        Return the determinant.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: ntl.GF2XHexOutput(0)
            sage: ntl.mat_GF2E(ctx, 5,5,[0..24]).determinant()
            [0 1 0 1 1 1 1]
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).determinant()
            [0 1 1 0 0 1]"""
    @overload
    def gauss(self, ncols=...) -> Any:
        """ntl_mat_GF2E.gauss(self, ncols=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 449)

        Perform unitary row operations so as to bring this matrix
        into row echelon form.

        If the optional argument ``ncols`` is supplied, stops when
        first ``ncols`` columns are in echelon form.  The return value
        is the rank (or the rank of the first ``ncols`` columns).

        INPUT:

        - ``ncols`` -- number of columns to process (default: all)

        EXAMPLES::

            sage: m = ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).gauss()
            5
            sage: ntl.mat_GF2E(ctx, 5,5).gauss()
            0
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).gauss(3)
            3"""
    @overload
    def gauss(self) -> Any:
        """ntl_mat_GF2E.gauss(self, ncols=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 449)

        Perform unitary row operations so as to bring this matrix
        into row echelon form.

        If the optional argument ``ncols`` is supplied, stops when
        first ``ncols`` columns are in echelon form.  The return value
        is the rank (or the rank of the first ``ncols`` columns).

        INPUT:

        - ``ncols`` -- number of columns to process (default: all)

        EXAMPLES::

            sage: m = ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).gauss()
            5
            sage: ntl.mat_GF2E(ctx, 5,5).gauss()
            0
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).gauss(3)
            3"""
    @overload
    def gauss(self) -> Any:
        """ntl_mat_GF2E.gauss(self, ncols=-1)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 449)

        Perform unitary row operations so as to bring this matrix
        into row echelon form.

        If the optional argument ``ncols`` is supplied, stops when
        first ``ncols`` columns are in echelon form.  The return value
        is the rank (or the rank of the first ``ncols`` columns).

        INPUT:

        - ``ncols`` -- number of columns to process (default: all)

        EXAMPLES::

            sage: m = ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).gauss()
            5
            sage: ntl.mat_GF2E(ctx, 5,5).gauss()
            0
            sage: ntl.mat_GF2E(ctx, 5,5,[3..27]).gauss(3)
            3"""
    def image(self) -> Any:
        """ntl_mat_GF2E.image(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 620)

        The rows of X are computed as basis of A's row space.  X is
        row echelon form.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 3,3,[0..24])
            sage: ntl.GF2XHexOutput(1)
            sage: m.image()
            [[0x3 0x4 0x5]
            [0x0 0x1 0x2]
            [0x0 0x0 0xc1]
            ]"""
    @overload
    def kernel(self) -> Any:
        """ntl_mat_GF2E.kernel(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 642)

        Compute a basis for the kernel of the map ``x -> x*A``, where
        ``x`` is a row vector.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 3,3,[0..24])
            sage: ntl.GF2XHexOutput(1)
            sage: m.kernel()
            []"""
    @overload
    def kernel(self) -> Any:
        """ntl_mat_GF2E.kernel(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 642)

        Compute a basis for the kernel of the map ``x -> x*A``, where
        ``x`` is a row vector.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 3,3,[0..24])
            sage: ntl.GF2XHexOutput(1)
            sage: m.kernel()
            []"""
    @overload
    def list(self) -> Any:
        """ntl_mat_GF2E.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 476)

        Return a list of the entries in this matrix.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 2,2,[ntl.GF2E_random(ctx) for x in range(2*2)])
            sage: ntl.GF2XHexOutput(0)
            sage: l = m.list(); l  # random
            [[1 1 0 0 1 0 1 1], [1 1 1 0 1 1 1], [0 1 1 1 1 0 0 1], [0 1 0 1 1 1]]
            sage: len(l) == 4
            True
            sage: all(a.modulus_context() is ctx for a in l)
            True"""
    @overload
    def list(self) -> Any:
        """ntl_mat_GF2E.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 476)

        Return a list of the entries in this matrix.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 2,2,[ntl.GF2E_random(ctx) for x in range(2*2)])
            sage: ntl.GF2XHexOutput(0)
            sage: l = m.list(); l  # random
            [[1 1 0 0 1 0 1 1], [1 1 1 0 1 1 1], [0 1 1 1 1 0 0 1], [0 1 0 1 1 1]]
            sage: len(l) == 4
            True
            sage: all(a.modulus_context() is ctx for a in l)
            True"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_mat_GF2E.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 155)

        Return the structure that holds the underlying NTL GF2E modulus.

        EXAMPLES::

            sage: ntl.GF2XHexOutput(0)
            sage: ctx = ntl.GF2EContext( ntl.GF2X([1,1,0,1,1,0,0,0,1]) )
            sage: a = ntl.GF2E(ntl.ZZ_pX([1,1,3],2), ctx)
            sage: A= ntl.mat_GF2E(ctx, 1, 1, [a])
            sage: cty = A.modulus_context(); cty
            NTL modulus [1 1 0 1 1 0 0 0 1]
            sage: ctx == cty
            True"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_mat_GF2E.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 155)

        Return the structure that holds the underlying NTL GF2E modulus.

        EXAMPLES::

            sage: ntl.GF2XHexOutput(0)
            sage: ctx = ntl.GF2EContext( ntl.GF2X([1,1,0,1,1,0,0,0,1]) )
            sage: a = ntl.GF2E(ntl.ZZ_pX([1,1,3],2), ctx)
            sage: A= ntl.mat_GF2E(ctx, 1, 1, [a])
            sage: cty = A.modulus_context(); cty
            NTL modulus [1 1 0 1 1 0 0 0 1]
            sage: ctx == cty
            True"""
    @overload
    def randomize(self, density=..., nonzero=...) -> Any:
        """ntl_mat_GF2E.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 661)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        EXAMPLES::

            sage: k.<a> = GF(2^4)
            sage: ctx = ntl.GF2EContext(k)
            sage: ntl.GF2XHexOutput(1)
            sage: A = ntl.mat_GF2E(ctx, 100, 100)
            sage: expected_non_zeros = 100 * 100 * (1 - 1.0/2^4)
            sage: observed = lambda : len([e for e in A.list() if e!=0])
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A.randomize()
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time

            sage: A = ntl.mat_GF2E(ctx, 100,100)
            sage: A.randomize(nonzero=True)
            sage: len([e for e in A.list() if e!=0])
            10000

            sage: expected_non_zeros = 1000
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A = ntl.mat_GF2E(ctx, 100,100)
            ....:         A.randomize(nonzero=True, density=0.1)
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time"""
    @overload
    def randomize(self) -> Any:
        """ntl_mat_GF2E.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 661)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        EXAMPLES::

            sage: k.<a> = GF(2^4)
            sage: ctx = ntl.GF2EContext(k)
            sage: ntl.GF2XHexOutput(1)
            sage: A = ntl.mat_GF2E(ctx, 100, 100)
            sage: expected_non_zeros = 100 * 100 * (1 - 1.0/2^4)
            sage: observed = lambda : len([e for e in A.list() if e!=0])
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A.randomize()
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time

            sage: A = ntl.mat_GF2E(ctx, 100,100)
            sage: A.randomize(nonzero=True)
            sage: len([e for e in A.list() if e!=0])
            10000

            sage: expected_non_zeros = 1000
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A = ntl.mat_GF2E(ctx, 100,100)
            ....:         A.randomize(nonzero=True, density=0.1)
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time"""
    @overload
    def randomize(self, nonzero=...) -> Any:
        """ntl_mat_GF2E.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 661)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        EXAMPLES::

            sage: k.<a> = GF(2^4)
            sage: ctx = ntl.GF2EContext(k)
            sage: ntl.GF2XHexOutput(1)
            sage: A = ntl.mat_GF2E(ctx, 100, 100)
            sage: expected_non_zeros = 100 * 100 * (1 - 1.0/2^4)
            sage: observed = lambda : len([e for e in A.list() if e!=0])
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A.randomize()
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time

            sage: A = ntl.mat_GF2E(ctx, 100,100)
            sage: A.randomize(nonzero=True)
            sage: len([e for e in A.list() if e!=0])
            10000

            sage: expected_non_zeros = 1000
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A = ntl.mat_GF2E(ctx, 100,100)
            ....:         A.randomize(nonzero=True, density=0.1)
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time"""
    @overload
    def randomize(self, nonzero=..., density=...) -> Any:
        """ntl_mat_GF2E.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 661)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        EXAMPLES::

            sage: k.<a> = GF(2^4)
            sage: ctx = ntl.GF2EContext(k)
            sage: ntl.GF2XHexOutput(1)
            sage: A = ntl.mat_GF2E(ctx, 100, 100)
            sage: expected_non_zeros = 100 * 100 * (1 - 1.0/2^4)
            sage: observed = lambda : len([e for e in A.list() if e!=0])
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A.randomize()
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time

            sage: A = ntl.mat_GF2E(ctx, 100,100)
            sage: A.randomize(nonzero=True)
            sage: len([e for e in A.list() if e!=0])
            10000

            sage: expected_non_zeros = 1000
            sage: n = 0; s = 0
            sage: def add_samples():
            ....:     global n, s, A
            ....:     for i in range(10):
            ....:         A = ntl.mat_GF2E(ctx, 100,100)
            ....:         A.randomize(nonzero=True, density=0.1)
            ....:         n += 1
            ....:         s += observed() - expected_non_zeros

            sage: add_samples()
            sage: while abs(s*1.0/n) > 10: add_samples()
            sage: while abs(s*1.0/n) > 5: add_samples()  # long time"""
    @overload
    def transpose(self) -> Any:
        """ntl_mat_GF2E.transpose(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 549)

        Return the transposed matrix of ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = m.transpose()
            sage: n == m
            False
            sage: n.transpose() == m
            True"""
    @overload
    def transpose(self) -> Any:
        """ntl_mat_GF2E.transpose(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 549)

        Return the transposed matrix of ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = m.transpose()
            sage: n == m
            False
            sage: n.transpose() == m
            True"""
    @overload
    def transpose(self) -> Any:
        """ntl_mat_GF2E.transpose(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 549)

        Return the transposed matrix of ``self``.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = m.transpose()
            sage: n == m
            False
            sage: n.transpose() == m
            True"""
    def __add__(self, ntl_mat_GF2Eself, other) -> Any:
        """ntl_mat_GF2E.__add__(ntl_mat_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 253)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ntl.mat_GF2E(ctx, 5,5,[3..27])
            sage: m+n   # indirect doctest
            [[[1 1] [1 0 1] [1 1 1] [1 0 1] [1 1]]
            [[1 0 1 1] [1 1 1 1] [1 0 1 1] [1 1] [1 0 1]]
            [[1 1 1] [1 0 1] [1 1] [1 0 1 1 1] [1 1 1 1 1]]
            [[1 0 1 1 1] [1 1] [1 0 1] [1 1 1] [1 0 1]]
            [[1 1] [1 0 1 1] [1 1 1 1] [1 0 1 1] [1 1]]
            ]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, ij) -> Any:
        """ntl_mat_GF2E.__getitem__(self, ij)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 399)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: m[0,1]
            [1]
            sage: m[0,0] = 0
            sage: m[0,0]
            []"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __invert__(self) -> Any:
        """ntl_mat_GF2E.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 569)

        Return `X = A^{-1}`; an error is raised if A is singular.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ~m
            sage: o = n*m
            sage: o.IsIdent()
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_mat_GF2Eself, other) -> Any:
        """ntl_mat_GF2E.__mul__(ntl_mat_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 201)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: ntl.GF2XHexOutput(1)
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ntl.mat_GF2E(ctx, 5,5,[3..27])
            sage: m*n  # indirect doctest
            [[0x87 0x04 0xc4 0xc7 0x87]
            [0x32 0x84 0x17 0x63 0x73]
            [0xa1 0x46 0x25 0xcd 0x2f]
            [0x1 0xcf 0xfb 0xd6 0x62]
            [0xcf 0x02 0x06 0xfd 0x79]
            ]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_mat_GF2E.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 278)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: -m == m  # indirect doctest
            True"""
    def __pow__(self, ntl_mat_GF2Eself, longe, ignored) -> Any:
        """ntl_mat_GF2E.__pow__(ntl_mat_GF2E self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 293)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: m**2 == m*m  # indirect doctest
            True"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_mat_GF2E.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 172)

        EXAMPLES::

            sage: k.<a> = GF(2^4)
            sage: ctx = ntl.GF2EContext(k)
            sage: A = ntl.mat_GF2E(ctx, 5,5, [0..24])
            sage: A == loads(dumps(A))
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __setitem__(self, ij, x) -> Any:
        """ntl_mat_GF2E.__setitem__(self, ij, x)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 361)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: ntl.GF2XHexOutput(0)
            sage: m[0,0]
            []
            sage: m[0,0] = 1
            sage: m[0,0]
            [1]"""
    def __sub__(self, ntl_mat_GF2Eself, other) -> Any:
        """ntl_mat_GF2E.__sub__(ntl_mat_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_GF2E.pyx (starting at line 227)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext([1,1,0,1,1,0,0,0,1])
            sage: m = ntl.mat_GF2E(ctx, 5,5,[0..24])
            sage: n = ntl.mat_GF2E(ctx, 5,5,[3..27])
            sage: ntl.GF2XHexOutput(0)
            sage: m-n  # indirect doctest
            [[[1 1] [1 0 1] [1 1 1] [1 0 1] [1 1]]
            [[1 0 1 1] [1 1 1 1] [1 0 1 1] [1 1] [1 0 1]]
            [[1 1 1] [1 0 1] [1 1] [1 0 1 1 1] [1 1 1 1 1]]
            [[1 0 1 1 1] [1 1] [1 0 1] [1 1 1] [1 0 1]]
            [[1 1] [1 0 1 1] [1 1 1 1] [1 0 1 1] [1 1]]
            ]"""
