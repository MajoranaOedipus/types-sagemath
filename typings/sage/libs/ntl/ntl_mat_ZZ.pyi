from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from typing import Any, overload

class ntl_mat_ZZ:
    """ntl_mat_ZZ(nrows=0, ncols=0, v=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 70)

    The \\class{mat_ZZ} class implements arithmetic with matrices over `\\Z`."""
    def __init__(self, nrows=..., ncols=..., v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 75)

                The \\class{mat_ZZ} class implements arithmetic with matrices over `\\Z`.

                EXAMPLES::

                    sage: M = ntl.mat_ZZ(3,3) ; M
                    [
                    [0 0 0]
                    [0 0 0]
                    [0 0 0]
                    ]
                    sage: ntl.mat_ZZ(3,3,[1..9])
                    [
                    [1 2 3]
                    [4 5 6]
                    [7 8 9]
                    ]
        """
    def BKZ_FP(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.BKZ_FP(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 466)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.BKZ_FP(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.BKZ_FP(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def BKZ_QP(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.BKZ_QP(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 537)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.BKZ_QP(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.BKZ_QP(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def BKZ_QP1(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.BKZ_QP1(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 608)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.BKZ_QP1(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.BKZ_QP1(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def BKZ_RR(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.BKZ_RR(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 750)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.BKZ_RR(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.BKZ_RR(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def BKZ_XD(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.BKZ_XD(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 679)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.BKZ_XD(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.BKZ_XD(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def G_BKZ_FP(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.G_BKZ_FP(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 821)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.G_BKZ_FP(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.G_BKZ_FP(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def G_BKZ_QP(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.G_BKZ_QP(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 892)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.G_BKZ_QP(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.G_BKZ_QP(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def G_BKZ_QP1(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.G_BKZ_QP1(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 963)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.G_BKZ_QP1(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.G_BKZ_QP1(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def G_BKZ_RR(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.G_BKZ_RR(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1105)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.G_BKZ_RR(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.G_BKZ_RR(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def G_BKZ_XD(self, U=..., delta=..., BlockSize=..., prune=..., verbose=...) -> Any:
        '''ntl_mat_ZZ.G_BKZ_XD(self, U=None, delta=0.99, BlockSize=10, prune=0, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1034)

        All BKZ methods are equivalent to the LLL routines,
        except that Block Korkin-Zolotarev reduction is applied. We
        describe here only the differences in the calling syntax.

        * The optional parameter "BlockSize" specifies the size of the
        blocks in the reduction. High values yield shorter vectors,
        but the running time increases exponentially with BlockSize.
        BlockSize should be between 2 and the number of rows of B.

        * The optional parameter "prune" can be set to any positive
        number to invoke the Volume Heuristic from [Schnorr and
        Horner, Eurocrypt \'95].  This can significantly reduce the
        running time, and hence allow much bigger block size, but the
        quality of the reduction is of course not as good in general.
        Higher values of prune mean better quality, and slower running
        time.  When prune == 0, pruning is disabled.  Recommended
        usage: for BlockSize >= 30, set 10 <= prune <= 15.

        * The QP1 variant uses quad_float precision to compute
        Gram-Schmidt, but uses double precision in the search phase
        of the block reduction algorithm.  This seems adequate for
        most purposes, and is faster than QP, which uses quad_float
        precision uniformly throughout.

        INPUT:

        - ``U`` -- permutation matrix (see LLL, default: ``None``)
        - ``delta`` -- reduction parameter (default: 0.99)
        - ``BlockSize`` -- see above (default: 10)
        - ``prune`` -- see above (default: 0)
        - ``verbose`` -- print verbose output (default: ``False``)

        EXAMPLES::

            sage: A = Matrix(ZZ,5,5,range(25))
            sage: a = A._ntl_()
            sage: a.G_BKZ_XD(); a
            2
            [
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 1 2 3 4]
            [5 3 1 -1 -3]
            ]

            sage: U = ntl.mat_ZZ(2,2) # note that the dimension doesn\'t matter
            sage: r = a.G_BKZ_XD(U=U); U
            [
            [0 1 0 0 0]
            [1 0 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
            ]'''
    def G_LLL_FP(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.G_LLL_FP(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1442)

        Perform the same reduction as self.LLL_FP using the same
        calling conventions but uses the Givens Orthogonalization.

        Givens Orthogonalization.  This is a bit slower, but generally
        much more stable, and is really the preferred
        orthogonalization strategy.  For a nice description of this,
        see Chapter 5 of [G. Golub and C. van Loan, Matrix
        Computations, 3rd edition, Johns Hopkins Univ. Press, 1996]."""
    def G_LLL_QP(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.G_LLL_QP(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1466)

        Perform the same reduction as self.G_LLL_FP using the same
        calling conventions but with quad float precision."""
    def G_LLL_RR(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.G_LLL_RR(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1503)

        Perform the same reduction as self.G_LLL_FP using the same
        calling conventions but with arbitrary precision floating
        point numbers."""
    def G_LLL_XD(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.G_LLL_XD(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1484)

        Perform the same reduction as self.G_LLL_FP using the same
        calling conventions but with extended exponent double
        precision."""
    @overload
    def HNF(self, D=...) -> Any:
        """ntl_mat_ZZ.HNF(self, D=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 384)

        The input matrix A=self is an n x m matrix of rank m (so n >=
        m), and D is a multiple of the determinant of the lattice L
        spanned by the rows of A.  The output W is the Hermite Normal
        Form of A; that is, W is the unique m x m matrix whose rows
        span L, such that

        - W is lower triangular,
        - the diagonal entries are positive,
        - any entry below the diagonal is a nonnegative number
          strictly less than the diagonal entry in its column.

        This is implemented using the algorithm of [P. Domich,
        R. Kannan and L. Trotter, Math. Oper. Research 12:50-59,
        1987].

        TIMINGS:

        NTL is not very good compared to MAGMA, unfortunately::

            sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2
            sage: A = ntl.mat_ZZ(200,200)
            sage: for i in range(a.nrows()):
            ....:     for j in range(a.ncols()):
            ....:         A[i,j] = a[i,j]
            sage: t = cputime(); d = A.determinant()
            sage: cputime(t)          # random
            0.33201999999999998
            sage: t = cputime(); B = A.HNF(d)  # long time (5s on sage.math, 2011)
            sage: cputime(t)          # random
            6.4924050000000006

        In comparison, MAGMA does this much more quickly:
        \\begin{verbatim}
            > A := MatrixAlgebra(IntegerRing(),200)![Random(-2,2) : i in [1..200^2]];
            > time d := Determinant(A);
            Time: 0.140
            > time H := HermiteForm(A);
            Time: 0.290
        \\end{verbatim}

        Also, PARI is also faster than NTL if one uses the flag 1 to
        the mathnf routine.  The above takes 16 seconds in PARI.

        TESTS::

            sage: ntl.mat_ZZ(2,2,[1..4]).HNF()
            [
            [1 0]
            [0 2]
            ]"""
    @overload
    def HNF(self, d) -> Any:
        """ntl_mat_ZZ.HNF(self, D=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 384)

        The input matrix A=self is an n x m matrix of rank m (so n >=
        m), and D is a multiple of the determinant of the lattice L
        spanned by the rows of A.  The output W is the Hermite Normal
        Form of A; that is, W is the unique m x m matrix whose rows
        span L, such that

        - W is lower triangular,
        - the diagonal entries are positive,
        - any entry below the diagonal is a nonnegative number
          strictly less than the diagonal entry in its column.

        This is implemented using the algorithm of [P. Domich,
        R. Kannan and L. Trotter, Math. Oper. Research 12:50-59,
        1987].

        TIMINGS:

        NTL is not very good compared to MAGMA, unfortunately::

            sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2
            sage: A = ntl.mat_ZZ(200,200)
            sage: for i in range(a.nrows()):
            ....:     for j in range(a.ncols()):
            ....:         A[i,j] = a[i,j]
            sage: t = cputime(); d = A.determinant()
            sage: cputime(t)          # random
            0.33201999999999998
            sage: t = cputime(); B = A.HNF(d)  # long time (5s on sage.math, 2011)
            sage: cputime(t)          # random
            6.4924050000000006

        In comparison, MAGMA does this much more quickly:
        \\begin{verbatim}
            > A := MatrixAlgebra(IntegerRing(),200)![Random(-2,2) : i in [1..200^2]];
            > time d := Determinant(A);
            Time: 0.140
            > time H := HermiteForm(A);
            Time: 0.290
        \\end{verbatim}

        Also, PARI is also faster than NTL if one uses the flag 1 to
        the mathnf routine.  The above takes 16 seconds in PARI.

        TESTS::

            sage: ntl.mat_ZZ(2,2,[1..4]).HNF()
            [
            [1 0]
            [0 2]
            ]"""
    def LLL(self, a=..., b=..., return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.LLL(self, a=3, b=4, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1176)

        Perform LLL reduction of ``self`` (puts \\code{self} in an LLL form).

        \\code{self} is an `m x n` matrix, viewed as `m` rows of
        `n`-vectors.  `m` may be less than, equal to, or greater than `n`,
        and the rows need not be linearly independent. ``self`` is
        transformed into an LLL-reduced basis, and the return value is
        the rank r of ``self`` so as det2 (see below).  The first `m-r` rows
        of ``self`` are zero.

        More specifically, elementary row transformations are
        performed on \\code{self} so that the nonzero rows of
        new-\\code{self} form an LLL-reduced basis for the lattice
        spanned by the rows of old-\\code{self}.  The default reduction
        parameter is `\\delta=3/4`, which means that the squared length
        of the first nonzero basis vector is no more than `2^{r-1}`
        times that of the shortest vector in the lattice.

        det2 is calculated as the \\emph{square} of the determinant of
        the lattice---note that sqrt(det2) is in general an integer
        only when r = n.

        If return_U is True, a value U is returned which is the
        transformation matrix, so that U is a unimodular m x m matrix
        with U * old-\\code{self} = new-\\code{self}. Note that the
        first m-r rows of U form a basis (as a lattice) for the kernel
        of old-B.

        The parameters a and b allow an arbitrary reduction parameter
        `\\delta=a/b`, where `1/4 < a/b \\leq 1`, where a and b are positive
        integers.  For a basis reduced with parameter delta, the
        squared length of the first nonzero basis vector is no more
        than `1/(delta-1/4)^{r-1}` times that of the shortest vector in
        the lattice.

        The algorithm employed here is essentially the one in Cohen's
        book: [H. Cohen, A Course in Computational Algebraic Number
        Theory, Springer, 1993]

        INPUT:

        - ``a`` -- parameter a as described above (default: 3)
        - ``b`` -- parameter b as described above (default: 4)
        - ``return_U`` -- return U as described above
        - ``verbose`` -- if ``True`` NTL will produce some verbatim messages on
          what's going on internally (default: ``False``)

        OUTPUT:

        (rank,det2,[U]) where rank,det2, and U are as described
        above and U is an optional return value if return_U is ``True``.

        EXAMPLES::

            sage: M=ntl.mat_ZZ(3,3,[1,2,3,4,5,6,7,8,9])
            sage: M.LLL()
            (2, 54)
            sage: M
            [
            [0 0 0]
            [2 1 0]
            [-1 1 3]
            ]
            sage: M=ntl.mat_ZZ(4,4,[-6,9,-15,-18,4,-6,10,12,10,-16,18,35,-24,36,-46,-82]); M
            [
            [-6 9 -15 -18]
            [4 -6 10 12]
            [10 -16 18 35]
            [-24 36 -46 -82]
            ]
            sage: M.LLL()
            (3, 19140)
            sage: M
            [
            [0 0 0 0]
            [0 -2 0 0]
            [-2 1 -5 -6]
            [0 -1 -7 5]
            ]

        WARNING: This method modifies \\code{self}. So after applying
        this method your matrix will be a vector of vectors."""
    def LLL_FP(self, delta=..., return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.LLL_FP(self, delta=0.75, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1273)

        Perform approximate LLL reduction of \\code{self} (puts
        \\code{self} in an LLL form) subject to the following
        conditions:

        The precision is double.

        The return value is the rank of B.

        Classical Gram-Schmidt Orthogonalization is used:

        This choice uses classical methods for computing the
        Gram-Schmidt orthogonalization.  It is fast but prone to
        stability problems.  This strategy was first proposed by
        Schnorr and Euchner [C. P. Schnorr and M. Euchner,
        Proc. Fundamentals of Computation Theory, LNCS 529, pp. 68-85,
        1991].  The version implemented here is substantially
        different, improving both stability and performance.

        If return_U is True, then also U is returned which is
        the transition matrix: `U * self_{old} = self_{new}`

        The optional argument 'delta' is the reduction parameter, and
        may be set so that 0.50 <= delta < 1.  Setting it close to 1
        yields shorter vectors, and also improves the stability, but
        increases the running time.  Recommended value: delta =
        0.99.

        The optional parameter 'verbose' can be set to see all kinds
        of fun things printed while the routine is executing.  A
        status report is also printed every once in a while.

        INPUT:

        - ``delta`` -- as described above (0.5 <= delta < 1.0) (default: 0.75)
        - ``return_U`` -- return U as described above
        - ``verbose`` -- if ``True`` NTL will produce some verbatim messages on
          what's going on internally (default: ``False``)

        OUTPUT:

        (rank,[U]) where rank and U are as described above and U
        is an optional return value if ``return_U`` is ``True``.

        EXAMPLES::

            sage: M=ntl.mat_ZZ(3,3,[1,2,3,4,5,6,7,8,9])
            sage: M.LLL_FP()
            2
            sage: M
            [
            [0 0 0]
            [2 1 0]
            [-1 1 3]
            ]
            sage: M=ntl.mat_ZZ(4,4,[-6,9,-15,-18,4,-6,10,12,10,-16,18,35,-24,36,-46,-82]); M
            [
            [-6 9 -15 -18]
            [4 -6 10 12]
            [10 -16 18 35]
            [-24 36 -46 -82]
            ]
            sage: M.LLL_FP()
            3
            sage: M
            [
            [0 0 0 0]
            [0 -2 0 0]
            [-2 1 -5 -6]
            [0 -1 -7 5]
            ]

        WARNING: This method modifies \\code{self}. So after applying this
        method your matrix will be a vector of vectors."""
    def LLL_QP(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.LLL_QP(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1362)

        Perform the same reduction as \\code{self.LLL_FP} using the
        same calling conventions but with quad float precision.

        EXAMPLES::

            sage: M=ntl.mat_ZZ(3,3,[1,2,3,4,5,6,7,8,9])
            sage: M.LLL_QP(delta=0.75)
            2"""
    def LLL_RR(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.LLL_RR(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1411)

        Perform the same reduction as \\code{self.LLL_FP} using the
        same calling conventions but with arbitrary precision floating
        point numbers.

        EXAMPLES::

            sage: M=ntl.mat_ZZ(3,3,[1,2,3,4,5,6,7,8,9])
            sage: M.LLL_RR(delta=0.75)
            2"""
    def LLL_XD(self, delta, return_U=..., verbose=...) -> Any:
        """ntl_mat_ZZ.LLL_XD(self, delta, return_U=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 1386)

        Perform the same reduction as \\code{self.LLL_FP} using the
        same calling conventions but with extended exponent double
        precision.

        EXAMPLES::

            sage: M=ntl.mat_ZZ(3,3,[1,2,3,4,5,6,7,8,9])
            sage: M.LLL_XD(delta=0.75)
            2"""
    @overload
    def charpoly(self) -> Any:
        """ntl_mat_ZZ.charpoly(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 445)

        Find the characteristic polynomial of self, and return it
        as an NTL ZZX.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,2,[1,2,3,4])
            sage: M.charpoly()
            [-2 -5 1]
            sage: type(_)
            <class 'sage.libs.ntl.ntl_ZZX.ntl_ZZX'>
            sage: M.determinant()
            -2"""
    @overload
    def charpoly(self) -> Any:
        """ntl_mat_ZZ.charpoly(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 445)

        Find the characteristic polynomial of self, and return it
        as an NTL ZZX.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,2,[1,2,3,4])
            sage: M.charpoly()
            [-2 -5 1]
            sage: type(_)
            <class 'sage.libs.ntl.ntl_ZZX.ntl_ZZX'>
            sage: M.determinant()
            -2"""
    @overload
    def determinant(self, deterministic=...) -> Any:
        """ntl_mat_ZZ.determinant(self, deterministic=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 362)

        Return the determinant of ``self``.

        EXAMPLES::

            sage: ntl.mat_ZZ(8,8,[3..66]).determinant()
            0
            sage: ntl.mat_ZZ(2,5,range(10)).determinant()
            Traceback (most recent call last):
            ...
            TypeError: cannot take determinant of non-square matrix.
            sage: ntl.mat_ZZ(4,4,[next_prime(2**i) for i in range(16)]).determinant()
            -10248
            sage: ntl.mat_ZZ(4,4,[ ZZ.random_element() for _ in range(16) ]).determinant()  # random
            678"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_ZZ.determinant(self, deterministic=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 362)

        Return the determinant of ``self``.

        EXAMPLES::

            sage: ntl.mat_ZZ(8,8,[3..66]).determinant()
            0
            sage: ntl.mat_ZZ(2,5,range(10)).determinant()
            Traceback (most recent call last):
            ...
            TypeError: cannot take determinant of non-square matrix.
            sage: ntl.mat_ZZ(4,4,[next_prime(2**i) for i in range(16)]).determinant()
            -10248
            sage: ntl.mat_ZZ(4,4,[ ZZ.random_element() for _ in range(16) ]).determinant()  # random
            678"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_ZZ.determinant(self, deterministic=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 362)

        Return the determinant of ``self``.

        EXAMPLES::

            sage: ntl.mat_ZZ(8,8,[3..66]).determinant()
            0
            sage: ntl.mat_ZZ(2,5,range(10)).determinant()
            Traceback (most recent call last):
            ...
            TypeError: cannot take determinant of non-square matrix.
            sage: ntl.mat_ZZ(4,4,[next_prime(2**i) for i in range(16)]).determinant()
            -10248
            sage: ntl.mat_ZZ(4,4,[ ZZ.random_element() for _ in range(16) ]).determinant()  # random
            678"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_ZZ.determinant(self, deterministic=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 362)

        Return the determinant of ``self``.

        EXAMPLES::

            sage: ntl.mat_ZZ(8,8,[3..66]).determinant()
            0
            sage: ntl.mat_ZZ(2,5,range(10)).determinant()
            Traceback (most recent call last):
            ...
            TypeError: cannot take determinant of non-square matrix.
            sage: ntl.mat_ZZ(4,4,[next_prime(2**i) for i in range(16)]).determinant()
            -10248
            sage: ntl.mat_ZZ(4,4,[ ZZ.random_element() for _ in range(16) ]).determinant()  # random
            678"""
    @overload
    def determinant(self) -> Any:
        """ntl_mat_ZZ.determinant(self, deterministic=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 362)

        Return the determinant of ``self``.

        EXAMPLES::

            sage: ntl.mat_ZZ(8,8,[3..66]).determinant()
            0
            sage: ntl.mat_ZZ(2,5,range(10)).determinant()
            Traceback (most recent call last):
            ...
            TypeError: cannot take determinant of non-square matrix.
            sage: ntl.mat_ZZ(4,4,[next_prime(2**i) for i in range(16)]).determinant()
            -10248
            sage: ntl.mat_ZZ(4,4,[ ZZ.random_element() for _ in range(16) ]).determinant()  # random
            678"""
    @overload
    def list(self) -> Any:
        """ntl_mat_ZZ.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 341)

        EXAMPLES::

            sage: m = ntl.mat_ZZ(3, 4, range(12)); m
            [
            [0 1 2 3]
            [4 5 6 7]
            [8 9 10 11]
            ]
            sage: m.list()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"""
    @overload
    def list(self) -> Any:
        """ntl_mat_ZZ.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 341)

        EXAMPLES::

            sage: m = ntl.mat_ZZ(3, 4, range(12)); m
            [
            [0 1 2 3]
            [4 5 6 7]
            [8 9 10 11]
            ]
            sage: m.list()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"""
    @overload
    def ncols(self) -> Any:
        """ntl_mat_ZZ.ncols(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 281)

        Return the number of columns in ``self``.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(5,8,range(40))
            sage: M.ncols()
            8"""
    @overload
    def ncols(self) -> Any:
        """ntl_mat_ZZ.ncols(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 281)

        Return the number of columns in ``self``.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(5,8,range(40))
            sage: M.ncols()
            8"""
    @overload
    def nrows(self) -> Any:
        """ntl_mat_ZZ.nrows(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 269)

        Return the number of rows in ``self``.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(5,5,range(25))
            sage: M.nrows()
            5"""
    @overload
    def nrows(self) -> Any:
        """ntl_mat_ZZ.nrows(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 269)

        Return the number of rows in ``self``.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(5,5,range(25))
            sage: M.nrows()
            5"""
    def __add__(self, ntl_mat_ZZself, other) -> Any:
        """ntl_mat_ZZ.__add__(ntl_mat_ZZ self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 187)

        Return ``self + other``.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,2,[8..11]) ; N = ntl.mat_ZZ(2,2,[-1..2])
            sage: M+N
            [
            [7 9]
            [11 13]
            ]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, ij) -> Any:
        """ntl_mat_ZZ.__getitem__(self, ij)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 318)

        EXAMPLES::

            sage: m = ntl.mat_ZZ(3, 2, range(6))
            sage: m[0,0] ## indirect doctest
            0
            sage: m[2,1]
            5
            sage: m[3,2] #  oops, 0 based
            Traceback (most recent call last):
            ...
            IndexError: array index out of range"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, ntl_mat_ZZself, other) -> Any:
        """ntl_mat_ZZ.__mul__(ntl_mat_ZZ self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 141)

        Multiply two matrices.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,2,[8..11]) ; N = ntl.mat_ZZ(2,2,[-1..2])
            sage: M*N
            [
            [1 18]
            [1 22]
            ]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __pow__(self, ntl_mat_ZZself, longe, ignored) -> Any:
        """ntl_mat_ZZ.__pow__(ntl_mat_ZZ self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 237)

        Return ``self`` to the e power.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,2,[8..11])
            sage: M**4
            [
            [56206 62415]
            [69350 77011]
            ]
            sage: M**0
            [
            [1 0]
            [0 1]
            ]
            sage: M**(-1)
            Traceback (most recent call last):
            ...
            ValueError: cannot take negative powers of matrices."""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_mat_ZZ.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 109)

        EXAMPLES::

            sage: m = ntl.mat_ZZ(3, 2, range(6)); m
            [
            [0 1]
            [2 3]
            [4 5]
            ]
            sage: loads(dumps(m))
            [
            [0 1]
            [2 3]
            [4 5]
            ]
            sage: loads(dumps(m)) == m
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __setitem__(self, ij, x) -> Any:
        """ntl_mat_ZZ.__setitem__(self, ij, x)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 293)

        Given a tuple (i, j), return self[i,j].

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,9,[3..20])
            sage: M[1,7] ## indirect doctest
            19"""
    def __sub__(self, ntl_mat_ZZself, other) -> Any:
        """ntl_mat_ZZ.__sub__(ntl_mat_ZZ self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_mat_ZZ.pyx (starting at line 164)

        Return ``self - other``.

        EXAMPLES::

            sage: M = ntl.mat_ZZ(2,2,[8..11]) ; N = ntl.mat_ZZ(2,2,[-1..2])
            sage: M-N
            [
            [9 9]
            [9 9]
            ]"""
