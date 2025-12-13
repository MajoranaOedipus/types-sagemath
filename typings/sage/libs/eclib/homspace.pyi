from sage.categories.category import ZZ as ZZ
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from typing import Any, overload

class ModularSymbols:
    """ModularSymbols(long level, int sign=0, bool cuspidal=False, int verbose=0)

    File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 16)

    Class of Cremona Modular Symbols of given level and sign (and weight 2).

    EXAMPLES::

        sage: M = CremonaModularSymbols(225)
        sage: type(M)
        <class 'sage.libs.eclib.homspace.ModularSymbols'>"""
    def __init__(self, longlevel, intsign=..., boolcuspidal=..., intverbose=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 26)

                Called when creating a space of Cremona modular symbols.

                INPUT:

                - ``level`` -- integer; the level: at least 2
                - ``sign`` -- integer (default: 0); the sign: 0, +1 or -1
                - ``cuspidal`` -- boolean (default: ``False``); ``True`` for cuspidal homology
                - ``verbose`` -- integer (default: 0); verbosity level

                EXAMPLES::

                    sage: CremonaModularSymbols(123, sign=1, cuspidal=True)
                    Cremona Cuspidal Modular Symbols space of dimension 13 for Gamma_0(123) of weight 2 with sign 1
                    sage: CremonaModularSymbols(123, sign=-1, cuspidal=True)
                    Cremona Cuspidal Modular Symbols space of dimension 13 for Gamma_0(123) of weight 2 with sign -1
                    sage: CremonaModularSymbols(123, sign=0, cuspidal=True)
                    Cremona Cuspidal Modular Symbols space of dimension 26 for Gamma_0(123) of weight 2 with sign 0
                    sage: CremonaModularSymbols(123, sign=0, cuspidal=False)
                    Cremona Modular Symbols space of dimension 29 for Gamma_0(123) of weight 2 with sign 0
        """
    @overload
    def dimension(self) -> Any:
        """ModularSymbols.dimension(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 92)

        Return the dimension of this modular symbols space.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1234, sign=1)
            sage: M.dimension()
            156"""
    @overload
    def dimension(self) -> Any:
        """ModularSymbols.dimension(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 92)

        Return the dimension of this modular symbols space.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1234, sign=1)
            sage: M.dimension()
            156"""
    def hecke_matrix(self, longp, dual=..., verbose=...) -> Any:
        """ModularSymbols.hecke_matrix(self, long p, dual=False, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 156)

        Return the matrix of the ``p``-th Hecke operator acting on
        this space of modular symbols.

        The result of this command is not cached.

        INPUT:

        - ``p`` -- a prime number

        - ``dual`` -- boolean (default: ``False``); whether to compute the
          Hecke operator acting on the dual space, i.e., the transpose of the
          Hecke operator

        - ``verbose`` -- boolean (default: ``False``); print verbose output

        OUTPUT:

        (matrix) If ``p`` divides the level, the matrix of the
        Atkin-Lehner involution `W_p` at ``p``; otherwise the matrix of the
        Hecke operator `T_p`,

        EXAMPLES::

            sage: M = CremonaModularSymbols(37)
            sage: t = M.hecke_matrix(2); t
            5 x 5 Cremona matrix over Rational Field
            sage: print(t.str())
            [ 3  0  0  0  0]
            [-1 -1  1  1  0]
            [ 0  0 -1  0  1]
            [-1  1  0 -1 -1]
            [ 0  0  1  0 -1]
            sage: t.charpoly().factor()
            (x - 3) * x^2 * (x + 2)^2
            sage: print(M.hecke_matrix(2, dual=True).str())
            [ 3 -1  0 -1  0]
            [ 0 -1  0  1  0]
            [ 0  1 -1  0  1]
            [ 0  1  0 -1  0]
            [ 0  0  1 -1 -1]
            sage: w = M.hecke_matrix(37); w
            5 x 5 Cremona matrix over Rational Field
            sage: w.charpoly().factor()
            (x - 1)^2 * (x + 1)^3
            sage: sw = w.sage_matrix_over_ZZ()
            sage: st = t.sage_matrix_over_ZZ()
            sage: sw^2 == sw.parent()(1)
            True
            sage: st*sw == sw*st
            True"""
    @overload
    def is_cuspidal(self) -> Any:
        """ModularSymbols.is_cuspidal(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 143)

        Return whether or not this space is cuspidal.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122); M.is_cuspidal()
            0
            sage: M = CremonaModularSymbols(1122, cuspidal=True); M.is_cuspidal()
            1"""
    @overload
    def is_cuspidal(self) -> Any:
        """ModularSymbols.is_cuspidal(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 143)

        Return whether or not this space is cuspidal.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122); M.is_cuspidal()
            0
            sage: M = CremonaModularSymbols(1122, cuspidal=True); M.is_cuspidal()
            1"""
    @overload
    def is_cuspidal(self) -> Any:
        """ModularSymbols.is_cuspidal(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 143)

        Return whether or not this space is cuspidal.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122); M.is_cuspidal()
            0
            sage: M = CremonaModularSymbols(1122, cuspidal=True); M.is_cuspidal()
            1"""
    @overload
    def level(self) -> Any:
        """ModularSymbols.level(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 79)

        Return the level of this modular symbols space.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1234, sign=1)
            sage: M.level()
            1234"""
    @overload
    def level(self) -> Any:
        """ModularSymbols.level(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 79)

        Return the level of this modular symbols space.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1234, sign=1)
            sage: M.level()
            1234"""
    def number_of_cusps(self) -> Any:
        """ModularSymbols.number_of_cusps(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 107)

        Return the number of cusps for `\\Gamma_0(N)`, where `N` is the
        level.

        EXAMPLES::

            sage: M = CremonaModularSymbols(225)
            sage: M.number_of_cusps()
            24"""
    @overload
    def sign(self) -> Any:
        """ModularSymbols.sign(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 121)

        Return the sign of this Cremona modular symbols space.  The sign is either 0, +1 or -1.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122, sign=1); M
            Cremona Modular Symbols space of dimension 224 for Gamma_0(1122) of weight 2 with sign 1
            sage: M.sign()
            1
            sage: M = CremonaModularSymbols(1122); M
            Cremona Modular Symbols space of dimension 433 for Gamma_0(1122) of weight 2 with sign 0
            sage: M.sign()
            0
            sage: M = CremonaModularSymbols(1122, sign=-1); M
            Cremona Modular Symbols space of dimension 209 for Gamma_0(1122) of weight 2 with sign -1
            sage: M.sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """ModularSymbols.sign(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 121)

        Return the sign of this Cremona modular symbols space.  The sign is either 0, +1 or -1.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122, sign=1); M
            Cremona Modular Symbols space of dimension 224 for Gamma_0(1122) of weight 2 with sign 1
            sage: M.sign()
            1
            sage: M = CremonaModularSymbols(1122); M
            Cremona Modular Symbols space of dimension 433 for Gamma_0(1122) of weight 2 with sign 0
            sage: M.sign()
            0
            sage: M = CremonaModularSymbols(1122, sign=-1); M
            Cremona Modular Symbols space of dimension 209 for Gamma_0(1122) of weight 2 with sign -1
            sage: M.sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """ModularSymbols.sign(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 121)

        Return the sign of this Cremona modular symbols space.  The sign is either 0, +1 or -1.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122, sign=1); M
            Cremona Modular Symbols space of dimension 224 for Gamma_0(1122) of weight 2 with sign 1
            sage: M.sign()
            1
            sage: M = CremonaModularSymbols(1122); M
            Cremona Modular Symbols space of dimension 433 for Gamma_0(1122) of weight 2 with sign 0
            sage: M.sign()
            0
            sage: M = CremonaModularSymbols(1122, sign=-1); M
            Cremona Modular Symbols space of dimension 209 for Gamma_0(1122) of weight 2 with sign -1
            sage: M.sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """ModularSymbols.sign(self)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 121)

        Return the sign of this Cremona modular symbols space.  The sign is either 0, +1 or -1.

        EXAMPLES::

            sage: M = CremonaModularSymbols(1122, sign=1); M
            Cremona Modular Symbols space of dimension 224 for Gamma_0(1122) of weight 2 with sign 1
            sage: M.sign()
            1
            sage: M = CremonaModularSymbols(1122); M
            Cremona Modular Symbols space of dimension 433 for Gamma_0(1122) of weight 2 with sign 0
            sage: M.sign()
            0
            sage: M = CremonaModularSymbols(1122, sign=-1); M
            Cremona Modular Symbols space of dimension 209 for Gamma_0(1122) of weight 2 with sign -1
            sage: M.sign()
            -1"""
    def sparse_hecke_matrix(self, longp, dual=..., verbose=..., base_ring=...) -> Any:
        """ModularSymbols.sparse_hecke_matrix(self, long p, dual=False, verbose=False, base_ring=ZZ)

        File: /build/sagemath/src/sage/src/sage/libs/eclib/homspace.pyx (starting at line 214)

        Return the matrix of the ``p``-th Hecke operator acting on
        this space of modular symbols as a sparse Sage matrix over
        ``base_ring``. This is more memory-efficient than creating a
        Cremona matrix and then applying sage_matrix_over_ZZ with sparse=True.

        The result of this command is not cached.

        INPUT:

        - ``p`` -- a prime number

        - ``dual`` -- boolean (default: ``False``); whether to compute the
          Hecke operator acting on the dual space, i.e., the transpose of the Hecke
          operator

        - ``verbose`` -- boolean (default: ``False``); print verbose output

        OUTPUT:

        (matrix) If ``p`` divides the level, the matrix of the
        Atkin-Lehner involution `W_p` at ``p``; otherwise the matrix of the
        Hecke operator `T_p`,

        EXAMPLES::

            sage: M = CremonaModularSymbols(37)
            sage: t = M.sparse_hecke_matrix(2); type(t)
            <class 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>
            sage: print(t)
            [ 3  0  0  0  0]
            [-1 -1  1  1  0]
            [ 0  0 -1  0  1]
            [-1  1  0 -1 -1]
            [ 0  0  1  0 -1]
            sage: M = CremonaModularSymbols(5001)
            sage: T = M.sparse_hecke_matrix(2)
            sage: U = M.hecke_matrix(2).sage_matrix_over_ZZ(sparse=True)
            sage: print(T == U)
            True
            sage: T = M.sparse_hecke_matrix(2, dual=True)
            sage: print(T == U.transpose())
            True
            sage: T = M.sparse_hecke_matrix(2, base_ring=GF(7))
            sage: print(T == U.change_ring(GF(7)))
            True

        This concerns an issue reported on :issue:`21303`::

            sage: C = CremonaModularSymbols(45, cuspidal=True,sign=-1)
            sage: T2a = C.hecke_matrix(2).sage_matrix_over_ZZ()
            sage: T2b = C.sparse_hecke_matrix(2)
            sage: print(T2a == T2b)
            True"""
