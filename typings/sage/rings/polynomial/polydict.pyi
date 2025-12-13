import _cython_3_2_1
from sage.misc.latex import latex as latex
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
gen_index: _cython_3_2_1.cython_function_or_method
make_ETuple: _cython_3_2_1.cython_function_or_method
make_PolyDict: _cython_3_2_1.cython_function_or_method
monomial_exponent: _cython_3_2_1.cython_function_or_method

class ETuple:
    """ETuple(data=None, length=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1425)

    Representation of the exponents of a polydict monomial. If
    (0,0,3,0,5) is the exponent tuple of x_2^3*x_4^5 then this class
    only stores {2:3, 4:5} instead of the full tuple. This sparse
    information may be obtained by provided methods.

    The index/value data is all stored in the _data C int array member
    variable.  For the example above, the C array would contain
    2,3,4,5.  The indices are interlaced with the values.

    This data structure is very nice to work with for some functions
    implemented in this class, but tricky for others.  One reason that
    I really like the format is that it requires a single memory
    allocation for all of the values.  A hash table would require more
    allocations and presumably be slower.  I didn't benchmark this
    question (although, there is no question that this is much faster
    than the prior use of python dicts)."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, data=..., length=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1454)

                - ``ETuple()`` -> an empty ETuple
                - ``ETuple(sequence)`` -> ETuple initialized from sequence's items

                If the argument is an ETuple, the return value is the same object.

                EXAMPLES::

                    sage: from sage.rings.polynomial.polydict import ETuple
                    sage: ETuple([1, 1, 0])
                    (1, 1, 0)
                    sage: ETuple({int(1): int(2)}, int(3))
                    (0, 2, 0)
                    sage: ETuple([1, -1, 0])
                    (1, -1, 0)

                TESTS:

                Iterators are not accepted::

                    sage: ETuple(iter([2, 3, 4]))
                    Traceback (most recent call last):
                    ...
                    TypeError: Error in ETuple((), <list... object at ...>, None)
        """
    @overload
    def combine_to_positives(self, ETupleother) -> Any:
        """ETuple.combine_to_positives(self, ETuple other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2671)

        Given a pair of ETuples (self, other), returns a triple of
        ETuples (a, b, c) so that self = a + b, other = a + c and b and c
        have all positive entries.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([-2, 1, -5, 3, 1, 0])
            sage: f = ETuple([1, -3, -3, 4, 0, 2])
            sage: e.combine_to_positives(f)
            ((-2, -3, -5, 3, 0, 0), (0, 4, 0, 0, 1, 0), (3, 0, 2, 1, 0, 2))"""
    @overload
    def combine_to_positives(self, f) -> Any:
        """ETuple.combine_to_positives(self, ETuple other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2671)

        Given a pair of ETuples (self, other), returns a triple of
        ETuples (a, b, c) so that self = a + b, other = a + c and b and c
        have all positive entries.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([-2, 1, -5, 3, 1, 0])
            sage: f = ETuple([1, -3, -3, 4, 0, 2])
            sage: e.combine_to_positives(f)
            ((-2, -3, -5, 3, 0, 0), (0, 4, 0, 0, 1, 0), (3, 0, 2, 1, 0, 2))"""
    @overload
    def common_nonzero_positions(self, ETupleother, boolsort=...) -> Any:
        """ETuple.common_nonzero_positions(self, ETuple other, bool sort=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2590)

        Return an optionally sorted list of nonzero positions either
        in ``self`` or other, i.e. the only positions that need to be
        considered for any vector operation.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 0, 1])
            sage: e.common_nonzero_positions(f)
            {0, 2}
            sage: e.common_nonzero_positions(f, sort=True)
            [0, 2]"""
    @overload
    def common_nonzero_positions(self, f) -> Any:
        """ETuple.common_nonzero_positions(self, ETuple other, bool sort=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2590)

        Return an optionally sorted list of nonzero positions either
        in ``self`` or other, i.e. the only positions that need to be
        considered for any vector operation.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 0, 1])
            sage: e.common_nonzero_positions(f)
            {0, 2}
            sage: e.common_nonzero_positions(f, sort=True)
            [0, 2]"""
    @overload
    def common_nonzero_positions(self, f, sort=...) -> Any:
        """ETuple.common_nonzero_positions(self, ETuple other, bool sort=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2590)

        Return an optionally sorted list of nonzero positions either
        in ``self`` or other, i.e. the only positions that need to be
        considered for any vector operation.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 0, 1])
            sage: e.common_nonzero_positions(f)
            {0, 2}
            sage: e.common_nonzero_positions(f, sort=True)
            [0, 2]"""
    def divide_by_gcd(self, ETupleother) -> ETuple:
        """ETuple.divide_by_gcd(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2401)

        Return ``self / gcd(self, other)``.

        The entries of the result are the maximum of 0 and the
        difference of the corresponding entries of ``self`` and ``other``."""
    def divide_by_var(self, size_tpos) -> ETuple:
        """ETuple.divide_by_var(self, size_t pos) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2444)

        Return division of ``self`` by the variable with index ``pos``.

        If ``self[pos] == 0`` then a :exc:`ArithmeticError` is raised. Otherwise,
        an :class:`~sage.rings.polynomial.polydict.ETuple` is returned that is
        zero in position ``pos`` and coincides with ``self`` in the other
        positions.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 2, 0, 1])
            sage: e.divide_by_var(0)
            (0, 2, 0, 1)
            sage: e.divide_by_var(1)
            (1, 1, 0, 1)
            sage: e.divide_by_var(3)
            (1, 2, 0, 0)
            sage: e.divide_by_var(2)
            Traceback (most recent call last):
            ...
            ArithmeticError: not divisible by this variable"""
    def divides(self, ETupleother) -> bool:
        """ETuple.divides(self, ETuple other) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2491)

        Return whether ``self`` divides ``other``, i.e., no entry of ``self``
        exceeds that of ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 1, 0, 1, 0]).divides(ETuple([2, 2, 2, 2, 2]))
            True
            sage: ETuple([0, 3, 0, 1, 0]).divides(ETuple([2, 2, 2, 2, 2]))
            False
            sage: ETuple([0, 3, 0, 1, 0]).divides(ETuple([0, 3, 2, 2, 2]))
            True
            sage: ETuple([0, 0, 0, 0, 0]).divides(ETuple([2, 2, 2, 2, 2]))
            True

            sage: ETuple({104: 18, 256: 25, 314:78}, length=400r).divides(ETuple({104: 19, 105: 20, 106: 21}, length=400r))
            False
            sage: ETuple({104: 18, 256: 25, 314:78}, length=400r).divides(ETuple({104: 19, 105: 20, 106: 21, 255: 2, 256: 25, 312: 5, 314: 79, 315: 28}, length=400r))
            True"""
    @overload
    def dotprod(self, ETupleother) -> int:
        """ETuple.dotprod(self, ETuple other) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2331)

        Return the dot product of this tuple by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.dotprod(f)
            2
            sage: e = ETuple([1, 1, -1])
            sage: f = ETuple([0, -2, 1])
            sage: e.dotprod(f)
            -3"""
    @overload
    def dotprod(self, f) -> Any:
        """ETuple.dotprod(self, ETuple other) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2331)

        Return the dot product of this tuple by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.dotprod(f)
            2
            sage: e = ETuple([1, 1, -1])
            sage: f = ETuple([0, -2, 1])
            sage: e.dotprod(f)
            -3"""
    @overload
    def dotprod(self, f) -> Any:
        """ETuple.dotprod(self, ETuple other) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2331)

        Return the dot product of this tuple by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.dotprod(f)
            2
            sage: e = ETuple([1, 1, -1])
            sage: f = ETuple([0, -2, 1])
            sage: e.dotprod(f)
            -3"""
    @overload
    def eadd(self, ETupleother) -> ETuple:
        """ETuple.eadd(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2004)

        Return the vector addition of ``self`` with ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.eadd(f)
            (1, 1, 3)

        Verify that :issue:`6428` has been addressed::

            sage: # needs sage.libs.singular
            sage: R.<y, z> = Frac(QQ['x'])[]
            sage: type(y)
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: y^(2^32)
            Traceback (most recent call last):
            ...
            OverflowError: exponent overflow (...)   # 64-bit
            OverflowError: Python int too large to convert to C unsigned long  # 32-bit"""
    @overload
    def eadd(self, f) -> Any:
        """ETuple.eadd(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2004)

        Return the vector addition of ``self`` with ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.eadd(f)
            (1, 1, 3)

        Verify that :issue:`6428` has been addressed::

            sage: # needs sage.libs.singular
            sage: R.<y, z> = Frac(QQ['x'])[]
            sage: type(y)
            <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
            sage: y^(2^32)
            Traceback (most recent call last):
            ...
            OverflowError: exponent overflow (...)   # 64-bit
            OverflowError: Python int too large to convert to C unsigned long  # 32-bit"""
    def eadd_p(self, intother, size_tpos) -> ETuple:
        """ETuple.eadd_p(self, int other, size_t pos) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2054)

        Add ``other`` to ``self`` at position ``pos``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.eadd_p(5, 1)
            (1, 5, 2)
            sage: e = ETuple([0]*7)
            sage: e.eadd_p(5, 4)
            (0, 0, 0, 0, 5, 0, 0)

            sage: ETuple([0,1]).eadd_p(1, 0) == ETuple([1,1])
            True

            sage: e = ETuple([0, 1, 0])
            sage: e.eadd_p(0, 0).nonzero_positions()
            [1]
            sage: e.eadd_p(0, 1).nonzero_positions()
            [1]
            sage: e.eadd_p(0, 2).nonzero_positions()
            [1]

        TESTS:

        Test segmentation faults occurring as described in :issue:`34000`::

            sage: ETuple([0, 1, 1]).eadd_p(1, 0)
            (1, 1, 1)
            sage: ETuple([0, 2, 4, 3]).eadd_p(5, 0)
            (5, 2, 4, 3)
            sage: ETuple([0, 2]).eadd_p(5, 0)
            (5, 2)
            sage: e = ETuple([0, 1, 0])
            sage: e.eadd_p(0, 0).nonzero_positions()
            [1]
            sage: e.eadd_p(0, 1).nonzero_positions()
            [1]
            sage: e.eadd_p(0, 2).nonzero_positions()
            [1]
            sage: e.eadd_p(-1, 1).nonzero_positions()
            []"""
    def eadd_scaled(self, ETupleother, intscalar) -> ETuple:
        """ETuple.eadd_scaled(self, ETuple other, int scalar) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2142)

        Vector addition of ``self`` with ``scalar * other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.eadd_scaled(f, 3)
            (1, 3, 5)"""
    @overload
    def emax(self, ETupleother) -> ETuple:
        """ETuple.emax(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2243)

        Vector of maximum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emax(f)
            (1, 1, 2)
            sage: e = ETuple((1, 2, 3, 4))
            sage: f = ETuple((4, 0, 2, 1))
            sage: f.emax(e)
            (4, 2, 3, 4)
            sage: e = ETuple((1, -2, -2, 4))
            sage: f = ETuple((4, 0, 0, 0))
            sage: f.emax(e)
            (4, 0, 0, 4)
            sage: f.emax(e).nonzero_positions()
            [0, 3]"""
    @overload
    def emax(self, f) -> Any:
        """ETuple.emax(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2243)

        Vector of maximum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emax(f)
            (1, 1, 2)
            sage: e = ETuple((1, 2, 3, 4))
            sage: f = ETuple((4, 0, 2, 1))
            sage: f.emax(e)
            (4, 2, 3, 4)
            sage: e = ETuple((1, -2, -2, 4))
            sage: f = ETuple((4, 0, 0, 0))
            sage: f.emax(e)
            (4, 0, 0, 4)
            sage: f.emax(e).nonzero_positions()
            [0, 3]"""
    @overload
    def emax(self, e) -> Any:
        """ETuple.emax(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2243)

        Vector of maximum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emax(f)
            (1, 1, 2)
            sage: e = ETuple((1, 2, 3, 4))
            sage: f = ETuple((4, 0, 2, 1))
            sage: f.emax(e)
            (4, 2, 3, 4)
            sage: e = ETuple((1, -2, -2, 4))
            sage: f = ETuple((4, 0, 0, 0))
            sage: f.emax(e)
            (4, 0, 0, 4)
            sage: f.emax(e).nonzero_positions()
            [0, 3]"""
    @overload
    def emax(self, e) -> Any:
        """ETuple.emax(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2243)

        Vector of maximum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emax(f)
            (1, 1, 2)
            sage: e = ETuple((1, 2, 3, 4))
            sage: f = ETuple((4, 0, 2, 1))
            sage: f.emax(e)
            (4, 2, 3, 4)
            sage: e = ETuple((1, -2, -2, 4))
            sage: f = ETuple((4, 0, 0, 0))
            sage: f.emax(e)
            (4, 0, 0, 4)
            sage: f.emax(e).nonzero_positions()
            [0, 3]"""
    @overload
    def emax(self, e) -> Any:
        """ETuple.emax(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2243)

        Vector of maximum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emax(f)
            (1, 1, 2)
            sage: e = ETuple((1, 2, 3, 4))
            sage: f = ETuple((4, 0, 2, 1))
            sage: f.emax(e)
            (4, 2, 3, 4)
            sage: e = ETuple((1, -2, -2, 4))
            sage: f = ETuple((4, 0, 0, 0))
            sage: f.emax(e)
            (4, 0, 0, 4)
            sage: f.emax(e).nonzero_positions()
            [0, 3]"""
    @overload
    def emin(self, ETupleother) -> ETuple:
        """ETuple.emin(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2290)

        Vector of minimum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emin(f)
            (0, 0, 1)
            sage: e = ETuple([1, 0, -1])
            sage: f = ETuple([0, -2, 1])
            sage: e.emin(f)
            (0, -2, -1)"""
    @overload
    def emin(self, f) -> Any:
        """ETuple.emin(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2290)

        Vector of minimum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emin(f)
            (0, 0, 1)
            sage: e = ETuple([1, 0, -1])
            sage: f = ETuple([0, -2, 1])
            sage: e.emin(f)
            (0, -2, -1)"""
    @overload
    def emin(self, f) -> Any:
        """ETuple.emin(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2290)

        Vector of minimum of components of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.emin(f)
            (0, 0, 1)
            sage: e = ETuple([1, 0, -1])
            sage: f = ETuple([0, -2, 1])
            sage: e.emin(f)
            (0, -2, -1)"""
    def emul(self, intfactor) -> ETuple:
        """ETuple.emul(self, int factor) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2219)

        Scalar Vector multiplication of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.emul(2)
            (2, 0, 4)"""
    @overload
    def escalar_div(self, intn) -> ETuple:
        """ETuple.escalar_div(self, int n) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2360)

        Divide each exponent by ``n``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 0, 2]).escalar_div(2)
            (0, 0, 1)
            sage: ETuple([0, 3, 12]).escalar_div(3)
            (0, 1, 4)

            sage: ETuple([1, 5, 2]).escalar_div(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError

        TESTS:

        Checking that memory allocation works fine::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: t = ETuple(list(range(2048)))
            sage: for n in range(1, 9):
            ....:     t = t.escalar_div(n)
            sage: assert t.is_constant()"""
    @overload
    def escalar_div(self, n) -> Any:
        """ETuple.escalar_div(self, int n) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2360)

        Divide each exponent by ``n``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 0, 2]).escalar_div(2)
            (0, 0, 1)
            sage: ETuple([0, 3, 12]).escalar_div(3)
            (0, 1, 4)

            sage: ETuple([1, 5, 2]).escalar_div(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError

        TESTS:

        Checking that memory allocation works fine::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: t = ETuple(list(range(2048)))
            sage: for n in range(1, 9):
            ....:     t = t.escalar_div(n)
            sage: assert t.is_constant()"""
    @overload
    def esub(self, ETupleother) -> ETuple:
        """ETuple.esub(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2181)

        Vector subtraction of ``self`` with ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.esub(f)
            (1, -1, 1)"""
    @overload
    def esub(self, f) -> Any:
        """ETuple.esub(self, ETuple other) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2181)

        Vector subtraction of ``self`` with ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: f = ETuple([0, 1, 1])
            sage: e.esub(f)
            (1, -1, 1)"""
    @overload
    def is_constant(self) -> bool:
        """ETuple.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2532)

        Return if all exponents are zero in the tuple.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.is_constant()
            False
            sage: e = ETuple([0, 0])
            sage: e.is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """ETuple.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2532)

        Return if all exponents are zero in the tuple.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.is_constant()
            False
            sage: e = ETuple([0, 0])
            sage: e.is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """ETuple.is_constant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2532)

        Return if all exponents are zero in the tuple.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.is_constant()
            False
            sage: e = ETuple([0, 0])
            sage: e.is_constant()
            True"""
    def is_multiple_of(self, intn) -> bool:
        """ETuple.is_multiple_of(self, int n) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2548)

        Test whether each entry is a multiple of ``n``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple

            sage: ETuple([0, 0]).is_multiple_of(3)
            True
            sage: ETuple([0, 3, 12, 0, 6]).is_multiple_of(3)
            True
            sage: ETuple([0, 0, 2]).is_multiple_of(3)
            False"""
    @overload
    def nonzero_positions(self, boolsort=...) -> list:
        """ETuple.nonzero_positions(self, bool sort=False) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2571)

        Return the positions of nonzero exponents in the tuple.

        INPUT:

        - ``sort`` -- boolean (default: ``False``); if ``True`` a sorted list is
          returned; if ``False`` an unsorted list is returned

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.nonzero_positions()
            [0, 2]"""
    @overload
    def nonzero_positions(self) -> Any:
        """ETuple.nonzero_positions(self, bool sort=False) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2571)

        Return the positions of nonzero exponents in the tuple.

        INPUT:

        - ``sort`` -- boolean (default: ``False``); if ``True`` a sorted list is
          returned; if ``False`` an unsorted list is returned

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2])
            sage: e.nonzero_positions()
            [0, 2]"""
    @overload
    def nonzero_values(self, boolsort=...) -> list:
        """ETuple.nonzero_values(self, bool sort=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2613)

        Return the nonzero values of the tuple.

        INPUT:

        - ``sort`` -- boolean (default: ``True``); if ``True`` the values are
          sorted by their indices. Otherwise the values are returned unsorted.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([2, 0, 1])
            sage: e.nonzero_values()
            [2, 1]
            sage: f = ETuple([0, -1, 1])
            sage: f.nonzero_values(sort=True)
            [-1, 1]"""
    @overload
    def nonzero_values(self) -> Any:
        """ETuple.nonzero_values(self, bool sort=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2613)

        Return the nonzero values of the tuple.

        INPUT:

        - ``sort`` -- boolean (default: ``True``); if ``True`` the values are
          sorted by their indices. Otherwise the values are returned unsorted.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([2, 0, 1])
            sage: e.nonzero_values()
            [2, 1]
            sage: f = ETuple([0, -1, 1])
            sage: f.nonzero_values(sort=True)
            [-1, 1]"""
    @overload
    def nonzero_values(self, sort=...) -> Any:
        """ETuple.nonzero_values(self, bool sort=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2613)

        Return the nonzero values of the tuple.

        INPUT:

        - ``sort`` -- boolean (default: ``True``); if ``True`` the values are
          sorted by their indices. Otherwise the values are returned unsorted.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([2, 0, 1])
            sage: e.nonzero_values()
            [2, 1]
            sage: f = ETuple([0, -1, 1])
            sage: f.nonzero_values(sort=True)
            [-1, 1]"""
    @overload
    def reversed(self) -> ETuple:
        """ETuple.reversed(self) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2635)

        Return the reversed ETuple of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 2, 3])
            sage: e.reversed()
            (3, 2, 1)"""
    @overload
    def reversed(self) -> Any:
        """ETuple.reversed(self) -> ETuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2635)

        Return the reversed ETuple of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 2, 3])
            sage: e.reversed()
            (3, 2, 1)"""
    @overload
    def sparse_iter(self) -> Any:
        """ETuple.sparse_iter(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2655)

        Iterator over the elements of ``self`` where the elements are returned
        as ``(i, e)`` where ``i`` is the position of ``e`` in the tuple.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2, 0, 3])
            sage: list(e.sparse_iter())
            [(0, 1), (2, 2), (4, 3)]"""
    @overload
    def sparse_iter(self) -> Any:
        """ETuple.sparse_iter(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 2655)

        Iterator over the elements of ``self`` where the elements are returned
        as ``(i, e)`` where ``i`` is the position of ``e`` in the tuple.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2, 0, 3])
            sage: list(e.sparse_iter())
            [(0, 1), (2, 2), (4, 3)]"""
    @overload
    def unweighted_degree(self) -> int:
        """ETuple.unweighted_degree(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1878)

        Return the sum of entries.

        EXAMPLES::

             sage: from sage.rings.polynomial.polydict import ETuple
             sage: ETuple([1, 1, 0, 2, 0]).unweighted_degree()
             4
             sage: ETuple([-1, 1]).unweighted_degree()
             0"""
    @overload
    def unweighted_degree(self) -> Any:
        """ETuple.unweighted_degree(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1878)

        Return the sum of entries.

        EXAMPLES::

             sage: from sage.rings.polynomial.polydict import ETuple
             sage: ETuple([1, 1, 0, 2, 0]).unweighted_degree()
             4
             sage: ETuple([-1, 1]).unweighted_degree()
             0"""
    @overload
    def unweighted_degree(self) -> Any:
        """ETuple.unweighted_degree(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1878)

        Return the sum of entries.

        EXAMPLES::

             sage: from sage.rings.polynomial.polydict import ETuple
             sage: ETuple([1, 1, 0, 2, 0]).unweighted_degree()
             4
             sage: ETuple([-1, 1]).unweighted_degree()
             0"""
    def unweighted_quotient_degree(self, ETupleother) -> int:
        """ETuple.unweighted_quotient_degree(self, ETuple other) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1928)

        Return the degree of ``self`` divided by its gcd with ``other``.

        It amounts to counting the nonnegative entries of
        ``self.esub(other)``."""
    def weighted_degree(self, tuplew) -> int:
        """ETuple.weighted_degree(self, tuple w) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1892)

        Return the weighted sum of entries.

        INPUT:

        - ``w`` -- tuple of nonnegative integers

        EXAMPLES::

             sage: from sage.rings.polynomial.polydict import ETuple
             sage: e = ETuple([1, 1, 0, 2, 0])
             sage: e.weighted_degree((1, 2, 3, 4, 5))
             11
             sage: ETuple([-1, 1]).weighted_degree((1, 2))
             1

             sage: ETuple([1, 0]).weighted_degree((1, 2, 3))
             Traceback (most recent call last):
             ...
             ValueError: w must be of the same length as the ETuple"""
    def weighted_quotient_degree(self, ETupleother, tuplew) -> int:
        """ETuple.weighted_quotient_degree(self, ETuple other, tuple w) -> int

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1962)

        Return the weighted degree of ``self`` divided by its gcd with ``other``.

        INPUT:

        - ``other`` -- an :class:`~sage.rings.polynomial.polydict.ETuple`
        - ``w`` -- tuple of nonnegative integers"""
    @overload
    def __add__(self, ETupleself, ETupleother) -> Any:
        """ETuple.__add__(ETuple self, ETuple other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1542)

        ``x.__add__(n) <==> x+n``.

        Concatenate two ETuples.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 1, 0]) + ETuple({int(1): int(2)}, int(3))
            (1, 1, 0, 0, 2, 0)"""
    @overload
    def __add__(self, n) -> Any:
        """ETuple.__add__(ETuple self, ETuple other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1542)

        ``x.__add__(n) <==> x+n``.

        Concatenate two ETuples.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 1, 0]) + ETuple({int(1): int(2)}, int(3))
            (1, 1, 0, 0, 2, 0)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __contains__(self, elem) -> Any:
        """ETuple.__contains__(self, elem)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1691)

        ``x.__contains__(n) <==> n in x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple({int(1): int(2)}, int(3))
            sage: e
            (0, 2, 0)
            sage: 1 in e
            False
            sage: 2 in e
            True"""
    @overload
    def __contains__(self, n) -> Any:
        """ETuple.__contains__(self, elem)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1691)

        ``x.__contains__(n) <==> n in x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple({int(1): int(2)}, int(3))
            sage: e
            (0, 2, 0)
            sage: 1 in e
            False
            sage: 2 in e
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, i) -> Any:
        """ETuple.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1594)

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: m = ETuple([1, 2, 0, 3])
            sage: m[2]
            0
            sage: m[1]
            2
            sage: e = ETuple([1, 2, 3])
            sage: e[1:]
            (2, 3)
            sage: e[:1]
            (1,)"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """ETuple.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1666)

        x.__hash__() <==> hash(x)"""
    @overload
    def __hash__(self) -> Any:
        """ETuple.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1666)

        x.__hash__() <==> hash(x)"""
    @overload
    def __iter__(self) -> Any:
        """ETuple.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1793)

        ``x.__iter__() <==> iter(x)``.

        TESTS::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple((4, 0, 0, 2, 0))
            sage: list(e)
            [4, 0, 0, 2, 0]

        Check that :issue:`28178` is fixed::

            sage: it = iter(e)
            sage: iter(it) is it
            True"""
    @overload
    def __iter__(self) -> Any:
        """ETuple.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1793)

        ``x.__iter__() <==> iter(x)``.

        TESTS::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple((4, 0, 0, 2, 0))
            sage: list(e)
            [4, 0, 0, 2, 0]

        Check that :issue:`28178` is fixed::

            sage: it = iter(e)
            sage: iter(it) is it
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    @overload
    def __len__(self) -> Any:
        """ETuple.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1678)

        ``x.__len__() <==> len(x)``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2, 0, 3])
            sage: len(e)
            5"""
    @overload
    def __len__(self) -> Any:
        """ETuple.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1678)

        ``x.__len__() <==> len(x)``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 0, 2, 0, 3])
            sage: len(e)
            5"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    @overload
    def __mul__(self, ETupleself, factor) -> Any:
        """ETuple.__mul__(ETuple self, factor)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1567)

        ``x.__mul__(n) <==> x*n``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 2, 3])*2
            (1, 2, 3, 1, 2, 3)"""
    @overload
    def __mul__(self, n) -> Any:
        """ETuple.__mul__(ETuple self, factor)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1567)

        ``x.__mul__(n) <==> x*n``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: ETuple([1, 2, 3])*2
            (1, 2, 3, 1, 2, 3)"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ETuple.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1845)

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: e = ETuple([1, 1, 0])
            sage: e == loads(dumps(e))
            True"""
    def __rmul__(self, other):
        """Return value*self."""

class PolyDict:
    """PolyDict(pdict, zero=None, remove_zero=None, force_int_exponents=None, force_etuples=None, bool check=True)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 96)

    Data structure for multivariate polynomials.

    A PolyDict holds a dictionary all of whose keys are :class:`ETuple` and
    whose values are coefficients on which it is implicitely assumed that
    arithmetic operations can be performed.

    No arithmetic operation on :class:`PolyDict` clear zero coefficients as of
    now there is no reliable way of testing it in the most general setting, see
    :issue:`35319`. For removing zero coefficients from a :class:`PolyDict` you
    can use the method :meth:`remove_zeros` which can be parametrized by a zero
    test."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, pdict, zero=..., remove_zero=..., force_int_exponents=..., force_etuples=..., boolcheck=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 110)

                INPUT:

                - ``pdict`` -- dictionary or list, which represents a multi-variable
                  polynomial with the distribute representation (a copy is made)

                - ``zero`` -- deprecated

                - ``remove_zero`` -- deprecated

                - ``force_int_exponents`` -- deprecated

                - ``force_etuples`` -- deprecated

                - ``check`` -- if set to ``False`` then assumes that the exponents are
                  all valid ``ETuple``; in that case the construction is a bit faster

                EXAMPLES::

                    sage: from sage.rings.polynomial.polydict import PolyDict
                    sage: PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
                    PolyDict with representation {(1, 2): 3, (2, 1): 4, (2, 3): 2}

                    sage: PolyDict({(2, 3): 0, (1, 2): 3, (2, 1): 4})
                    PolyDict with representation {(1, 2): 3, (2, 1): 4, (2, 3): 0}

                    sage: PolyDict({(0, 0): RIF(-1,1)})                                         # needs sage.rings.real_interval_field
                    PolyDict with representation {(0, 0): 0.?}

                TESTS::

                    sage: from sage.rings.polynomial.polydict import PolyDict
                    sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
                    sage: len(f)
                    3
                    sage: f = PolyDict({}, zero=3, force_int_exponents=True, force_etuples=True)
                    doctest:warning
                    ...
                    DeprecationWarning: the arguments "zero", "forced_int_exponents"
                    and "forced_etuples" of PolyDict constructor are deprecated
                    See https://github.com/sagemath/sage/issues/34000 for details.
                    sage: f = PolyDict({}, remove_zero=False)
                    doctest:warning
                    ...
                    DeprecationWarning: the argument "remove_zero" of PolyDict
                    constructor is deprecated; call the method remove_zeros
                    See https://github.com/sagemath/sage/issues/34000 for details.
        '''
    @overload
    def apply_map(self, f) -> Any:
        """PolyDict.apply_map(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 262)

        Apply the map ``f`` on the coefficients (inplace).

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(1, 0): 1, (1, 1): -2})
            sage: f.apply_map(lambda x: x^2)
            sage: f
            PolyDict with representation {(1, 0): 1, (1, 1): 4}"""
    @overload
    def apply_map(self, lambdax) -> Any:
        """PolyDict.apply_map(self, f)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 262)

        Apply the map ``f`` on the coefficients (inplace).

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(1, 0): 1, (1, 1): -2})
            sage: f.apply_map(lambda x: x^2)
            sage: f
            PolyDict with representation {(1, 0): 1, (1, 1): 4}"""
    def coefficient(self, mon) -> Any:
        """PolyDict.coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 649)

        Return a polydict that defines a polynomial in 1 less number
        of variables that gives the coefficient of mon in this
        polynomial.

        The coefficient is defined as follows.  If f is this
        polynomial, then the coefficient is the sum T/mon where the
        sum is over terms T in f that are exactly divisible by mon."""
    @overload
    def coefficients(self) -> Any:
        """PolyDict.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 468)

        Return the coefficients of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: sorted(f.coefficients())
            [2, 3, 4]"""
    @overload
    def coefficients(self) -> Any:
        """PolyDict.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 468)

        Return the coefficients of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: sorted(f.coefficients())
            [2, 3, 4]"""
    @overload
    def coerce_coefficients(self, A) -> Any:
        """PolyDict.coerce_coefficients(self, A)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 277)

        Coerce the coefficients in the parent ``A``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 0})
            sage: f
            PolyDict with representation {(2, 3): 0}
            sage: f.coerce_coefficients(QQ)
            doctest:warning
            ...
            DeprecationWarning: coerce_cefficients is deprecated; use apply_map instead
            See https://github.com/sagemath/sage/issues/34000 for details.
            sage: f
            PolyDict with representation {(2, 3): 0}"""
    @overload
    def coerce_coefficients(self, QQ) -> Any:
        """PolyDict.coerce_coefficients(self, A)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 277)

        Coerce the coefficients in the parent ``A``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 0})
            sage: f
            PolyDict with representation {(2, 3): 0}
            sage: f.coerce_coefficients(QQ)
            doctest:warning
            ...
            DeprecationWarning: coerce_cefficients is deprecated; use apply_map instead
            See https://github.com/sagemath/sage/issues/34000 for details.
            sage: f
            PolyDict with representation {(2, 3): 0}"""
    @overload
    def degree(self, PolyDictx=...) -> Any:
        """PolyDict.degree(self, PolyDict x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 533)

        Return the total degree or the maximum degree in the variable ``x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.degree()
            5
            sage: f.degree(PolyDict({(1, 0): 1}))
            2
            sage: f.degree(PolyDict({(0, 1): 1}))
            3"""
    @overload
    def degree(self) -> Any:
        """PolyDict.degree(self, PolyDict x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 533)

        Return the total degree or the maximum degree in the variable ``x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.degree()
            5
            sage: f.degree(PolyDict({(1, 0): 1}))
            2
            sage: f.degree(PolyDict({(0, 1): 1}))
            3"""
    def derivative(self, PolyDictx) -> Any:
        """PolyDict.derivative(self, PolyDict x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1228)

        Return the derivative of ``self`` with respect to ``x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.derivative(PolyDict({(1, 0): 1}))
            PolyDict with representation {(0, 2): 3, (1, 1): 8, (1, 3): 4}
            sage: f.derivative(PolyDict({(0, 1): 1}))
            PolyDict with representation {(1, 1): 6, (2, 0): 4, (2, 2): 6}

            sage: PolyDict({(-1,): 1}).derivative(PolyDict({(1,): 1}))
            PolyDict with representation {(-2,): -1}
            sage: PolyDict({(-2,): 1}).derivative(PolyDict({(1,): 1}))
            PolyDict with representation {(-3,): -2}

            sage: PolyDict({}).derivative(PolyDict({(1, 1): 1}))
            Traceback (most recent call last):
            ...
            ValueError: x must be a generator"""
    def derivative_i(self, size_ti) -> Any:
        """PolyDict.derivative_i(self, size_t i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1213)

        Return the derivative of ``self`` with respect to the ``i``-th variable.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PolyDict({(1, 1): 1}).derivative_i(0)
            PolyDict with representation {(0, 1): 1}"""
    @overload
    def dict(self) -> Any:
        """PolyDict.dict(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 455)

        Return a copy of the dict that defines ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.dict()
            {(1, 2): 3, (2, 1): 4, (2, 3): 2}"""
    @overload
    def dict(self) -> Any:
        """PolyDict.dict(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 455)

        Return a copy of the dict that defines ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.dict()
            {(1, 2): 3, (2, 1): 4, (2, 3): 2}"""
    @overload
    def exponents(self) -> Any:
        """PolyDict.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 481)

        Return the exponents of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: sorted(f.exponents())
            [(1, 2), (2, 1), (2, 3)]"""
    @overload
    def exponents(self) -> Any:
        """PolyDict.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 481)

        Return the exponents of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: sorted(f.exponents())
            [(1, 2), (2, 1), (2, 3)]"""
    def get(self, ETuplee, default=...) -> Any:
        """PolyDict.get(self, ETuple e, default=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 511)

        Return the coefficient of the ETuple ``e`` if present and ``default`` otherwise.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict, ETuple
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.get(ETuple([1,2]))
            3
            sage: f.get(ETuple([1,1]), 'hello')
            'hello'"""
    def homogenize(self, size_tvar) -> Any:
        """PolyDict.homogenize(self, size_t var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 729)

        Return the homogeneization of ``self`` by increasing the degree of the
        variable ``var``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(0, 0): 1, (2, 1): 3, (1, 1): 5})
            sage: f.homogenize(0)
            PolyDict with representation {(2, 1): 8, (3, 0): 1}
            sage: f.homogenize(1)
            PolyDict with representation {(0, 3): 1, (1, 2): 5, (2, 1): 3}

            sage: PolyDict({(0, 1): 1, (1, 1): -1}).homogenize(0)
            PolyDict with representation {(1, 1): 0}"""
    def integral(self, PolyDictx) -> Any:
        """PolyDict.integral(self, PolyDict x)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1275)

        Return the integral of ``self`` with respect to ``x``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.integral(PolyDict({(1, 0): 1}))
            PolyDict with representation {(2, 2): 3/2, (3, 1): 4/3, (3, 3): 2/3}
            sage: f.integral(PolyDict({(0, 1): 1}))
            PolyDict with representation {(1, 3): 1, (2, 2): 2, (2, 4): 1/2}

            sage: PolyDict({(-1,): 1}).integral(PolyDict({(1,): 1}))
            Traceback (most recent call last):
            ...
            ArithmeticError: integral of monomial with exponent -1
            sage: PolyDict({(-2,): 1}).integral(PolyDict({(1,): 1}))
            PolyDict with representation {(-1,): -1}
            sage: PolyDict({}).integral(PolyDict({(1, 1): 1}))
            Traceback (most recent call last):
            ...
            ValueError: x must be a generator"""
    def integral_i(self, size_ti) -> Any:
        """PolyDict.integral_i(self, size_t i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1256)

        Return the derivative of ``self`` with respect to the ``i``-th variable.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PolyDict({(1, 1): 1}).integral_i(0)
            PolyDict with representation {(2, 1): 1/2}"""
    @overload
    def is_constant(self) -> Any:
        """PolyDict.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 706)

        Return whether this polynomial is constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.is_constant()
            False
            sage: g = PolyDict({(0, 0): 2})
            sage: g.is_constant()
            True
            sage: h = PolyDict({})
            sage: h.is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """PolyDict.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 706)

        Return whether this polynomial is constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.is_constant()
            False
            sage: g = PolyDict({(0, 0): 2})
            sage: g.is_constant()
            True
            sage: h = PolyDict({})
            sage: h.is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """PolyDict.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 706)

        Return whether this polynomial is constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.is_constant()
            False
            sage: g = PolyDict({(0, 0): 2})
            sage: g.is_constant()
            True
            sage: h = PolyDict({})
            sage: h.is_constant()
            True"""
    @overload
    def is_constant(self) -> Any:
        """PolyDict.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 706)

        Return whether this polynomial is constant.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.is_constant()
            False
            sage: g = PolyDict({(0, 0): 2})
            sage: g.is_constant()
            True
            sage: h = PolyDict({})
            sage: h.is_constant()
            True"""
    @overload
    def is_homogeneous(self, tuplew=...) -> Any:
        """PolyDict.is_homogeneous(self, tuple w=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 675)

        Return whether this polynomial is homogeneous.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PolyDict({}).is_homogeneous()
            True
            sage: PolyDict({(1, 2): 1, (0, 3): -2}).is_homogeneous()
            True
            sage: PolyDict({(1, 0): 1, (1, 2): 3}).is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """PolyDict.is_homogeneous(self, tuple w=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 675)

        Return whether this polynomial is homogeneous.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PolyDict({}).is_homogeneous()
            True
            sage: PolyDict({(1, 2): 1, (0, 3): -2}).is_homogeneous()
            True
            sage: PolyDict({(1, 0): 1, (1, 2): 3}).is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """PolyDict.is_homogeneous(self, tuple w=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 675)

        Return whether this polynomial is homogeneous.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PolyDict({}).is_homogeneous()
            True
            sage: PolyDict({(1, 2): 1, (0, 3): -2}).is_homogeneous()
            True
            sage: PolyDict({(1, 0): 1, (1, 2): 3}).is_homogeneous()
            False"""
    @overload
    def is_homogeneous(self) -> Any:
        """PolyDict.is_homogeneous(self, tuple w=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 675)

        Return whether this polynomial is homogeneous.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PolyDict({}).is_homogeneous()
            True
            sage: PolyDict({(1, 2): 1, (0, 3): -2}).is_homogeneous()
            True
            sage: PolyDict({(1, 0): 1, (1, 2): 3}).is_homogeneous()
            False"""
    def latex(self, vars, atomic_exponents=..., atomic_coefficients=..., sortkey=...) -> Any:
        """PolyDict.latex(self, vars, atomic_exponents=True, atomic_coefficients=True, sortkey=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 761)

        Return a nice polynomial latex representation of this PolyDict, where
        the vars are substituted in.

        INPUT:

        - ``vars`` -- list
        - ``atomic_exponents`` -- boolean (default: ``True``)
        - ``atomic_coefficients`` -- boolean (default: ``True``)

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.latex(['a', 'WW'])
            '2 a^{2} WW^{3} + 4 a^{2} WW + 3 a WW^{2}'

        TESTS:

        We check that the issue on :issue:`9478` is resolved::

            sage: R2.<a> = QQ[]
            sage: R3.<xi, x> = R2[]
            sage: print(latex(xi*x))
            \\xi x

        TESTS:

        Check that :issue:`29604` is fixed::

            sage: PolyDict({(1, 0): GF(2)(1)}).latex(['x', 'y'])
            'x'"""
    def lcmt(self, greater_etuple) -> Any:
        """PolyDict.lcmt(self, greater_etuple)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1304)

        Provides functionality of lc, lm, and lt by calling the tuple
        compare function on the provided term order T.

        INPUT:

        - ``greater_etuple`` -- a term order"""
    @overload
    def list(self) -> Any:
        """PolyDict.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 442)

        Return a list that defines ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: sorted(f.list())
            [[2, [2, 3]], [3, [1, 2]], [4, [2, 1]]]"""
    @overload
    def list(self) -> Any:
        """PolyDict.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 442)

        Return a list that defines ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: sorted(f.list())
            [[2, [2, 3]], [3, [1, 2]], [4, [2, 1]]]"""
    def max_exp(self) -> Any:
        """PolyDict.max_exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1356)

        Return an ETuple containing the maximum exponents appearing.  If
        there are no terms at all in the PolyDict, it returns None.

        The nvars parameter is necessary because a PolyDict doesn't know it
        from the data it has (and an empty PolyDict offers no clues).

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.max_exp()
            (2, 3)
            sage: PolyDict({}).max_exp() # returns None"""
    def min_exp(self) -> Any:
        """PolyDict.min_exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1330)

        Return an ETuple containing the minimum exponents appearing.  If
        there are no terms at all in the PolyDict, it returns None.

        The nvars parameter is necessary because a PolyDict doesn't know it
        from the data it has (and an empty PolyDict offers no clues).

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.min_exp()
            (1, 1)
            sage: PolyDict({}).min_exp() # returns None"""
    def monomial_coefficient(self, mon) -> Any:
        """PolyDict.monomial_coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 583)

        Return the coefficient of the monomial ``mon``.

        INPUT:

        - ``mon`` -- a PolyDict with a single key

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2,3):2, (1,2):3, (2,1):4})
            sage: f.monomial_coefficient(PolyDict({(2,1):1}).dict())
            doctest:warning
            ...
            DeprecationWarning: PolyDict.monomial_coefficient is deprecated; use PolyDict.get instead
            See https://github.com/sagemath/sage/issues/34000 for details.
            4"""
    def poly_repr(self, vars, atomic_exponents=..., atomic_coefficients=..., sortkey=...) -> Any:
        """PolyDict.poly_repr(self, vars, atomic_exponents=True, atomic_coefficients=True, sortkey=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 856)

        Return a nice polynomial string representation of this PolyDict, where
        the vars are substituted in.

        INPUT:

        - ``vars`` -- list
        - ``atomic_exponents`` -- boolean (default: ``True``)
        - ``atomic_coefficients`` -- boolean (default: ``True``)

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2,3):2, (1,2):3, (2,1):4})
            sage: f.poly_repr(['a', 'WW'])
            '2*a^2*WW^3 + 4*a^2*WW + 3*a*WW^2'

        We check to make sure that when we are in characteristic two, we
        don't put negative signs on the generators. ::

            sage: Integers(2)['x, y'].gens()
            (x, y)

        We make sure that intervals are correctly represented. ::

            sage: f = PolyDict({(2, 3): RIF(1/2,3/2), (1, 2): RIF(-1,1)})               # needs sage.rings.real_interval_field
            sage: f.poly_repr(['x', 'y'])                                               # needs sage.rings.real_interval_field
            '1.?*x^2*y^3 + 0.?*x*y^2'

        TESTS:

        Check that :issue:`29604` is fixed::

            sage: PolyDict({(1, 0): GF(4)(1)}).poly_repr(['x', 'y'])                    # needs sage.rings.finite_rings
            'x'

            sage: # needs sage.modules
            sage: P.<x,y> = LaurentPolynomialRing(GF(2), 2)
            sage: P.gens()
            (x, y)
            sage: -x - y
            x + y"""
    def polynomial_coefficient(self, degrees) -> Any:
        """PolyDict.polynomial_coefficient(self, degrees)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 609)

        Return a polydict that defines the coefficient in the current
        polynomial viewed as a tower of polynomial extensions.

        INPUT:

        - ``degrees`` -- list of degree restrictions; list elements are ``None``
          if the variable in that position should be unrestricted

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.polynomial_coefficient([2, None])
            PolyDict with representation {(0, 1): 4, (0, 3): 2}
            sage: f = PolyDict({(0, 3): 2, (0, 2): 3, (2, 1): 4})
            sage: f.polynomial_coefficient([0, None])
            PolyDict with representation {(0, 2): 3, (0, 3): 2}"""
    @overload
    def remove_zeros(self, zero_test=...) -> Any:
        """PolyDict.remove_zeros(self, zero_test=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 198)

        Remove the entries with zero coefficients.

        INPUT:

        - ``zero_test`` -- (optional) function that performs test to zero of a coefficient

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3):0})
            sage: f
            PolyDict with representation {(2, 3): 0}
            sage: f.remove_zeros()
            sage: f
            PolyDict with representation {}

        The following example shows how to remove only exact zeros from a ``PolyDict``
        containing univariate power series::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = PolyDict({(1, 1): O(t), (1, 0): R.zero()})
            sage: f.remove_zeros(lambda s: s.is_zero() and s.prec() is Infinity)
            sage: f
            PolyDict with representation {(1, 1): O(t^1)}"""
    @overload
    def remove_zeros(self) -> Any:
        """PolyDict.remove_zeros(self, zero_test=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 198)

        Remove the entries with zero coefficients.

        INPUT:

        - ``zero_test`` -- (optional) function that performs test to zero of a coefficient

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3):0})
            sage: f
            PolyDict with representation {(2, 3): 0}
            sage: f.remove_zeros()
            sage: f
            PolyDict with representation {}

        The following example shows how to remove only exact zeros from a ``PolyDict``
        containing univariate power series::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = PolyDict({(1, 1): O(t), (1, 0): R.zero()})
            sage: f.remove_zeros(lambda s: s.is_zero() and s.prec() is Infinity)
            sage: f
            PolyDict with representation {(1, 1): O(t^1)}"""
    @overload
    def remove_zeros(self, lambdas) -> Any:
        """PolyDict.remove_zeros(self, zero_test=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 198)

        Remove the entries with zero coefficients.

        INPUT:

        - ``zero_test`` -- (optional) function that performs test to zero of a coefficient

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3):0})
            sage: f
            PolyDict with representation {(2, 3): 0}
            sage: f.remove_zeros()
            sage: f
            PolyDict with representation {}

        The following example shows how to remove only exact zeros from a ``PolyDict``
        containing univariate power series::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = PolyDict({(1, 1): O(t), (1, 0): R.zero()})
            sage: f.remove_zeros(lambda s: s.is_zero() and s.prec() is Infinity)
            sage: f
            PolyDict with representation {(1, 1): O(t^1)}"""
    @overload
    def rich_compare(self, PolyDictother, intop, sortkey=...) -> Any:
        '''PolyDict.rich_compare(self, PolyDict other, int op, sortkey=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 365)

        Compare two `PolyDict`s using a specified term ordering ``sortkey``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: from sage.structure.richcmp import op_EQ, op_NE, op_LT
            sage: p1 = PolyDict({(0,): 1})
            sage: p2 = PolyDict({(0,): 2})
            sage: O = TermOrder()
            sage: p1.rich_compare(PolyDict({(0,): 1}), op_EQ, O.sortkey)
            True
            sage: p1.rich_compare(p2, op_EQ, O.sortkey)
            False
            sage: p1.rich_compare(p2, op_NE, O.sortkey)
            True
            sage: p1.rich_compare(p2, op_LT, O.sortkey)
            True

            sage: p3 = PolyDict({(3, 2, 4): 1, (3, 2, 5): 2})
            sage: p4 = PolyDict({(3, 2, 4): 1, (3, 2, 3): 2})
            sage: p3.rich_compare(p4, op_LT, O.sortkey)
            False

        TESTS::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: from sage.structure.richcmp import op_EQ, op_NE, op_LT
            sage: p = PolyDict({})
            sage: ans = p.rich_compare(p, op_EQ)
            doctest:warning
            ...
            DeprecationWarning: the argument "sortkey" will become mandatory in future sage versions
            See https://github.com/sagemath/sage/issues/34000 for details.
            sage: ans
            True'''
    @overload
    def rich_compare(self, p, op_EQ) -> Any:
        '''PolyDict.rich_compare(self, PolyDict other, int op, sortkey=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 365)

        Compare two `PolyDict`s using a specified term ordering ``sortkey``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: from sage.structure.richcmp import op_EQ, op_NE, op_LT
            sage: p1 = PolyDict({(0,): 1})
            sage: p2 = PolyDict({(0,): 2})
            sage: O = TermOrder()
            sage: p1.rich_compare(PolyDict({(0,): 1}), op_EQ, O.sortkey)
            True
            sage: p1.rich_compare(p2, op_EQ, O.sortkey)
            False
            sage: p1.rich_compare(p2, op_NE, O.sortkey)
            True
            sage: p1.rich_compare(p2, op_LT, O.sortkey)
            True

            sage: p3 = PolyDict({(3, 2, 4): 1, (3, 2, 5): 2})
            sage: p4 = PolyDict({(3, 2, 4): 1, (3, 2, 3): 2})
            sage: p3.rich_compare(p4, op_LT, O.sortkey)
            False

        TESTS::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: from sage.structure.richcmp import op_EQ, op_NE, op_LT
            sage: p = PolyDict({})
            sage: ans = p.rich_compare(p, op_EQ)
            doctest:warning
            ...
            DeprecationWarning: the argument "sortkey" will become mandatory in future sage versions
            See https://github.com/sagemath/sage/issues/34000 for details.
            sage: ans
            True'''
    @overload
    def scalar_lmult(self, s) -> Any:
        """PolyDict.scalar_lmult(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1106)

        Return the left scalar multiplication of ``self`` by ``s``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict

            sage: x, y = FreeMonoid(2, 'x, y').gens()  # a strange object to live in a polydict, but non-commutative!   # needs sage.combinat
            sage: f = PolyDict({(2,3):x})                                               # needs sage.combinat
            sage: f.scalar_lmult(y)                                                     # needs sage.combinat
            PolyDict with representation {(2, 3): y*x}

            sage: f = PolyDict({(2,3):2, (1,2):3, (2,1):4})
            sage: f.scalar_lmult(-2)
            PolyDict with representation {(1, 2): -6, (2, 1): -8, (2, 3): -4}
            sage: f.scalar_lmult(RIF(-1,1))                                             # needs sage.rings.real_interval_field
            PolyDict with representation {(1, 2): 0.?e1, (2, 1): 0.?e1, (2, 3): 0.?e1}"""
    @overload
    def scalar_lmult(self, y) -> Any:
        """PolyDict.scalar_lmult(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1106)

        Return the left scalar multiplication of ``self`` by ``s``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict

            sage: x, y = FreeMonoid(2, 'x, y').gens()  # a strange object to live in a polydict, but non-commutative!   # needs sage.combinat
            sage: f = PolyDict({(2,3):x})                                               # needs sage.combinat
            sage: f.scalar_lmult(y)                                                     # needs sage.combinat
            PolyDict with representation {(2, 3): y*x}

            sage: f = PolyDict({(2,3):2, (1,2):3, (2,1):4})
            sage: f.scalar_lmult(-2)
            PolyDict with representation {(1, 2): -6, (2, 1): -8, (2, 3): -4}
            sage: f.scalar_lmult(RIF(-1,1))                                             # needs sage.rings.real_interval_field
            PolyDict with representation {(1, 2): 0.?e1, (2, 1): 0.?e1, (2, 3): 0.?e1}"""
    @overload
    def scalar_rmult(self, s) -> Any:
        """PolyDict.scalar_rmult(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1082)

        Return the right scalar multiplication of ``self`` by ``s``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict

            sage: x, y = FreeMonoid(2, 'x, y').gens()  # a strange object to live in a polydict, but non-commutative!   # needs sage.combinat
            sage: f = PolyDict({(2, 3): x})                                             # needs sage.combinat
            sage: f.scalar_rmult(y)                                                     # needs sage.combinat
            PolyDict with representation {(2, 3): x*y}

            sage: f = PolyDict({(2,3):2, (1, 2): 3, (2, 1): 4})
            sage: f.scalar_rmult(-2)
            PolyDict with representation {(1, 2): -6, (2, 1): -8, (2, 3): -4}
            sage: f.scalar_rmult(RIF(-1,1))                                             # needs sage.rings.real_interval_field
            PolyDict with representation {(1, 2): 0.?e1, (2, 1): 0.?e1, (2, 3): 0.?e1}"""
    @overload
    def scalar_rmult(self, y) -> Any:
        """PolyDict.scalar_rmult(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1082)

        Return the right scalar multiplication of ``self`` by ``s``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict

            sage: x, y = FreeMonoid(2, 'x, y').gens()  # a strange object to live in a polydict, but non-commutative!   # needs sage.combinat
            sage: f = PolyDict({(2, 3): x})                                             # needs sage.combinat
            sage: f.scalar_rmult(y)                                                     # needs sage.combinat
            PolyDict with representation {(2, 3): x*y}

            sage: f = PolyDict({(2,3):2, (1, 2): 3, (2, 1): 4})
            sage: f.scalar_rmult(-2)
            PolyDict with representation {(1, 2): -6, (2, 1): -8, (2, 3): -4}
            sage: f.scalar_rmult(RIF(-1,1))                                             # needs sage.rings.real_interval_field
            PolyDict with representation {(1, 2): 0.?e1, (2, 1): 0.?e1, (2, 3): 0.?e1}"""
    def term_lmult(self, exponent, s) -> Any:
        """PolyDict.term_lmult(self, exponent, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1130)

        Return this element multiplied by ``s`` on the left and with exponents
        shifted by ``exponent``.

        INPUT:

        - ``exponent`` -- a ETuple

        - ``s`` -- a scalar

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple, PolyDict

            sage: x, y = FreeMonoid(2, 'x, y').gens()  # a strange object to live in a polydict, but non-commutative!   # needs sage.combinat
            sage: f = PolyDict({(2, 3): x})                                             # needs sage.combinat
            sage: f.term_lmult(ETuple((1, 2)), y)                                       # needs sage.combinat
            PolyDict with representation {(3, 5): y*x}

            sage: f = PolyDict({(2,3): 2, (1,2): 3, (2,1): 4})
            sage: f.term_lmult(ETuple((1, 2)), -2)
            PolyDict with representation {(2, 4): -6, (3, 3): -8, (3, 5): -4}"""
    def term_rmult(self, exponent, s) -> Any:
        """PolyDict.term_rmult(self, exponent, s)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1159)

        Return this element multiplied by ``s`` on the right and with exponents
        shifted by ``exponent``.

        INPUT:

        - ``exponent`` -- a ETuple

        - ``s`` -- a scalar

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import ETuple, PolyDict

            sage: x, y = FreeMonoid(2, 'x, y').gens()  # a strange object to live in a polydict, but non-commutative!   # needs sage.combinat
            sage: f = PolyDict({(2, 3): x})                                             # needs sage.combinat
            sage: f.term_rmult(ETuple((1, 2)), y)                                       # needs sage.combinat
            PolyDict with representation {(3, 5): x*y}

            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.term_rmult(ETuple((1, 2)), -2)
            PolyDict with representation {(2, 4): -6, (3, 3): -8, (3, 5): -4}"""
    @overload
    def total_degree(self, tuplew=...) -> Any:
        """PolyDict.total_degree(self, tuple w=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 557)

        Return the total degree.

        INPUT:

        - ``w`` -- (optional) a tuple of weights

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.total_degree()
            5
            sage: f.total_degree((3, 1))
            9
            sage: PolyDict({}).degree()
            -1"""
    @overload
    def total_degree(self) -> Any:
        """PolyDict.total_degree(self, tuple w=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 557)

        Return the total degree.

        INPUT:

        - ``w`` -- (optional) a tuple of weights

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f.total_degree()
            5
            sage: f.total_degree((3, 1))
            9
            sage: PolyDict({}).degree()
            -1"""
    def __add__(self, PolyDictself, PolyDictother) -> Any:
        """PolyDict.__add__(PolyDict self, PolyDict other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1005)

        Add two PolyDict's in the same number of variables.

        EXAMPLES:

        We add two polynomials in 2 variables::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: g = PolyDict({(1, 5): -3, (2, 3): -2, (1, 1): 3})
            sage: f + g
            PolyDict with representation {(1, 1): 3, (1, 2): 3, (1, 5): -3, (2, 1): 4, (2, 3): 0}

            sage: K = GF(2)
            sage: f = PolyDict({(1, 1): K(1)})
            sage: f + f
            PolyDict with representation {(1, 1): 0}"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, e) -> Any:
        """PolyDict.__getitem__(self, e)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 494)

        Return a coefficient of the polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: f[1, 2]
            3
            sage: f[(2, 1)]
            4"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """PolyDict.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 299)

        Return the hash.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PD1 = PolyDict({(2, 3): 0, (1, 2): 3, (2, 1): 4})
            sage: PD2 = PolyDict({(2, 3): 0, (1, 2): 3, (2, 1): 4})
            sage: PD3 = PolyDict({(2, 3): 1, (1, 2): 3, (2, 1): 4})
            sage: hash(PD1) == hash(PD2)
            True
            sage: hash(PD1) == hash(PD3)
            False"""
    def __iadd__(self, PolyDictother) -> Any:
        """PolyDict.__iadd__(self, PolyDict other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 966)

        Inplace addition.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: g = PolyDict({(1, 5): -3, (2, 3): -2, (1, 1): 3})
            sage: f += g
            sage: f
            PolyDict with representation {(1, 1): 3, (1, 2): 3, (1, 5): -3, (2, 1): 4, (2, 3): 0}"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """PolyDict.__len__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 329)

        Return the number of terms of this polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: PD1 = PolyDict({(2, 3): 0, (1, 2): 3, (2, 1): 4})
            sage: len(PD1)
            3"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, PolyDictself, PolyDictright) -> Any:
        """PolyDict.__mul__(PolyDict self, PolyDict right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1036)

        Multiply two PolyDict's in the same number of variables.

        The algorithm do not test whether a product of coefficients is zero
        or whether a final coefficient is zero because there is no reliable way
        to do so in general (eg power series ring or `p`-adic rings).

        EXAMPLES:

        Multiplication of polynomials in 2 variables with rational coefficients::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: g = PolyDict({(1, 5): -3, (2, 3): -2, (1, 1): 3})
            sage: f * g
            PolyDict with representation {(2, 3): 9, (2, 7): -9, (3, 2): 12, (3, 4): 6, (3, 5): -6, (3, 6): -12, (3, 8): -6, (4, 4): -8, (4, 6): -4}

        Multiplication of polynomials in 2 variables with power series coefficients::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: f = PolyDict({(1, 0): 1 + O(t), (0, 1): 1 + O(t^2)})
            sage: g = PolyDict({(1, 0): 1, (0, 1): -1})
            sage: f * g
            PolyDict with representation {(0, 2): -1 + O(t^2), (1, 1): O(t^1), (2, 0): 1 + O(t)}
            sage: f = PolyDict({(1, 0): O(t), (0, 1): O(t)})
            sage: g = PolyDict({(1, 0): 1, (0, 1): O(t)})
            sage: f * g
            PolyDict with representation {(0, 2): O(t^2), (1, 1): O(t^1), (2, 0): O(t^1)}"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """PolyDict.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 992)

        TESTS::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: -PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            PolyDict with representation {(1, 2): -3, (2, 1): -4, (2, 3): -2}"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """PolyDict.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1318)


        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2, 3): 2, (1, 2): 3, (2, 1): 4})
            sage: loads(dumps(f)) == f
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rsub__(self, other):
        """Return value-self."""
    def __sub__(self, PolyDictself, PolyDictother) -> Any:
        """PolyDict.__sub__(PolyDict self, PolyDict other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polydict.pyx (starting at line 1188)

        Subtract two PolyDict's.

        EXAMPLES::

            sage: from sage.rings.polynomial.polydict import PolyDict
            sage: f = PolyDict({(2,3):2, (1,2):3, (2,1):4})
            sage: g = PolyDict({(2,3):2, (1,1):-10})
            sage: f - g
            PolyDict with representation {(1, 1): 10, (1, 2): 3, (2, 1): 4, (2, 3): 0}
            sage: g - f
            PolyDict with representation {(1, 1): -10, (1, 2): -3, (2, 1): -4, (2, 3): 0}
            sage: f - f
            PolyDict with representation {(1, 2): 0, (2, 1): 0, (2, 3): 0}"""
