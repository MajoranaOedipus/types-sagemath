from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, overload

class SymmetricReductionStrategy:
    """SymmetricReductionStrategy(Parent, L=None, tailreduce=False, good_input=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 126)

    A framework for efficient symmetric reduction of InfinitePolynomial, see
    :mod:`~sage.rings.polynomial.infinite_polynomial_element`.

    INPUT:

    - ``Parent`` -- an Infinite Polynomial Ring, see
      :mod:`~sage.rings.polynomial.infinite_polynomial_element`
    - ``L`` -- list (default: the empty list); list of elements of ``Parent``
      with respect to which will be reduced
    - ``good_input`` -- boolean (default: ``None``); if this optional parameter
      is true, it is assumed that each element of ``L`` is symmetrically
      reduced with respect to the previous elements of ``L``

    EXAMPLES::

        sage: X.<y> = InfinitePolynomialRing(QQ)
        sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
        sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]], good_input=True)
        sage: S.reduce(y[3] + 2*y[2]*y[1]^2 + 3*y[2]^2*y[1])
        y_3 + 3*y_2^2*y_1 + 2*y_2*y_1^2
        sage: S.tailreduce(y[3] + 2*y[2]*y[1]^2 + 3*y[2]^2*y[1])                        # needs sage.combinat
        y_3"""
    def __init__(self, Parent, L=..., tailreduce=..., good_input=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 151)

                EXAMPLES::

                    sage: X.<y> = InfinitePolynomialRing(QQ)
                    sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
                    sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]], good_input=True)
                    sage: S == loads(dumps(S))
                    True
        """
    def add_generator(self, p, good_input=...) -> Any:
        """SymmetricReductionStrategy.add_generator(self, p, good_input=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 401)

        Add another polynomial to ``self``.

        INPUT:

        - ``p`` -- an element of the underlying infinite polynomial ring
        - ``good_input`` -- boolean (default: ``None``); if ``True``, it is
          assumed that ``p`` is reduced with respect to ``self``. Otherwise,
          this reduction will be done first (which may cost some time).

        .. NOTE::

            Previously added polynomials may be modified. All input is
            prepared in view of an efficient symmetric reduction.

        EXAMPLES::

            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: S = SymmetricReductionStrategy(X)
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field
            sage: S.add_generator(y[3] + y[1]*(x[3]+x[1]))
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field, modulo
                x_3*y_1 + x_1*y_1 + y_3

        Note that the first added polynomial will be simplified when
        adding a suitable second polynomial::

            sage: S.add_generator(x[2] + x[1])                                          # needs sage.combinat
            sage: S                                                                     # needs sage.combinat
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field, modulo
                y_3,
                x_2 + x_1

        By default, reduction is applied to any newly added
        polynomial. This can be avoided by specifying the optional
        parameter 'good_input'::

            sage: # needs sage.combinat
            sage: S.add_generator(y[2] + y[1]*x[2])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field, modulo
                y_3,
                x_1*y_1 - y_2,
                x_2 + x_1
            sage: S.reduce(x[3] + x[2])
            -2*x_1
            sage: S.add_generator(x[3] + x[2], good_input=True)
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field, modulo
                y_3,
                x_3 + x_2,
                x_1*y_1 - y_2,
                x_2 + x_1

        In the previous example, ``x[3] + x[2]`` is added without
        being reduced to zero."""
    @overload
    def gens(self) -> tuple:
        """SymmetricReductionStrategy.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 257)

        Return the tuple of Infinite Polynomials modulo which ``self`` reduces.

        EXAMPLES::

            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in y over Rational Field, modulo
                y_2*y_1^2,
                y_2^2*y_1
            sage: S.gens()
            (y_2*y_1^2, y_2^2*y_1)"""
    @overload
    def gens(self) -> Any:
        """SymmetricReductionStrategy.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 257)

        Return the tuple of Infinite Polynomials modulo which ``self`` reduces.

        EXAMPLES::

            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in y over Rational Field, modulo
                y_2*y_1^2,
                y_2^2*y_1
            sage: S.gens()
            (y_2*y_1^2, y_2^2*y_1)"""
    def reduce(self, p, notail=..., report=...) -> Any:
        """SymmetricReductionStrategy.reduce(self, p, notail=False, report=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 513)

        Symmetric reduction of an infinite polynomial.

        INPUT:

        - ``p`` -- an element of the underlying infinite polynomial ring
        - ``notail`` -- boolean (default: ``False``); if ``True``, tail reduction
          is avoided (but there is no guarantee that there will be no tail
          reduction at all)
        - ``report`` -- object (default: ``None``); if not ``None``, print
          information on the progress of the computation

        OUTPUT: reduction of ``p`` with respect to ``self``

        .. NOTE::

            If tail reduction shall be forced, use :meth:`tailreduce`.

        EXAMPLES::

            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: S = SymmetricReductionStrategy(X, [y[3]], tailreduce=True)
            sage: S.reduce(y[4]*x[1] + y[1]*x[4])
            x_4*y_1
            sage: S.reduce(y[4]*x[1] + y[1]*x[4], notail=True)
            x_4*y_1 + x_1*y_4

        Last, we demonstrate the ``report`` option::

            sage: S = SymmetricReductionStrategy(X, [x[2] + y[1],
            ....:                                    x[2]*y[3] + x[1]*y[2] + y[4],
            ....:                                    y[3] + y[2]])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field, modulo
                y_3 + y_2,
                x_2 + y_1,
                x_1*y_2 + y_4 - y_3*y_1
            sage: S.reduce(x[3] + x[1]*y[3] + x[1]*y[1], report=True)
            :::>
            x_1*y_1 + y_4 - y_3*y_1 - y_1

        Each ':' indicates that one reduction of the leading monomial
        was performed. Eventually, the '>' indicates that the
        computation is finished."""
    @overload
    def reset(self) -> Any:
        """SymmetricReductionStrategy.reset(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 308)

        Remove all polynomials from ``self``.

        EXAMPLES::

            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in y over Rational Field, modulo
                y_2*y_1^2,
                y_2^2*y_1
            sage: S.reset()
            sage: S
            Symmetric Reduction Strategy in Infinite polynomial ring in y over Rational Field"""
    @overload
    def reset(self) -> Any:
        """SymmetricReductionStrategy.reset(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 308)

        Remove all polynomials from ``self``.

        EXAMPLES::

            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in y over Rational Field, modulo
                y_2*y_1^2,
                y_2^2*y_1
            sage: S.reset()
            sage: S
            Symmetric Reduction Strategy in Infinite polynomial ring in y over Rational Field"""
    def setgens(self, L) -> Any:
        """SymmetricReductionStrategy.setgens(self, L)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 276)

        Define the list of Infinite Polynomials modulo which ``self`` reduces.

        INPUT:

        - ``L`` -- list of elements of the underlying infinite polynomial ring

        .. NOTE::

            It is not tested if ``L`` is a good input. That method simply
            assigns a *copy* of ``L`` to the generators of ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]])
            sage: R = SymmetricReductionStrategy(X)
            sage: R.setgens(S.gens())
            sage: R
            Symmetric Reduction Strategy in
             Infinite polynomial ring in y over Rational Field, modulo
                y_2*y_1^2,
                y_2^2*y_1
            sage: R.gens() is S.gens()
            False
            sage: R.gens() == S.gens()
            True"""
    def tailreduce(self, p, report=...) -> Any:
        """SymmetricReductionStrategy.tailreduce(self, p, report=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 608)

        Symmetric reduction of an infinite polynomial, with forced tail reduction.

        INPUT:

        - ``p`` -- an element of the underlying infinite polynomial ring
        - ``report`` -- object (default: ``None``); if not ``None``, print
          information on the progress of the computation

        OUTPUT:

        Reduction (including the non-leading elements) of ``p`` with respect to ``self``.

        EXAMPLES::

            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: S = SymmetricReductionStrategy(X, [y[3]])
            sage: S.reduce(y[4]*x[1] + y[1]*x[4])
            x_4*y_1 + x_1*y_4
            sage: S.tailreduce(y[4]*x[1] + y[1]*x[4])                                   # needs sage.combinat
            x_4*y_1

        Last, we demonstrate the 'report' option::

            sage: S = SymmetricReductionStrategy(X, [x[2] + y[1],
            ....:                                    x[2]*x[3] + x[1]*y[2] + y[4],
            ....:                                    y[3] + y[2]])
            sage: S
            Symmetric Reduction Strategy in
             Infinite polynomial ring in x, y over Rational Field, modulo
                y_3 + y_2,
                x_2 + y_1,
                x_1*y_2 + y_4 + y_1^2
            sage: S.tailreduce(x[3] + x[1]*y[3] + x[1]*y[1], report=True)               # needs sage.combinat
            T[3]:::>
            T[3]:>
            x_1*y_1 - y_2 + y_1^2 - y_1

        The protocol means the following.
         * 'T[3]' means that we currently do tail reduction for a polynomial
           with three terms.
         * ':::>' means that there were three reductions of leading terms.
         * The tail of the result of the preceding reduction still has three
           terms. One reduction of leading terms was possible, and then the
           final result was obtained."""
    def __call__(self, p) -> Any:
        """SymmetricReductionStrategy.__call__(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 352)

        INPUT:

        A polynomial or an infinite polynomial.

        OUTPUT: a polynomial whose parent ring allows for coercion of any
        generator of ``self``

        EXAMPLES::

            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: X.<x,y> = InfinitePolynomialRing(QQ, implementation='sparse')
            sage: a, b = y[2]^2*y[1], y[1]^2*y[2]
            sage: p = y[3]*x[2]*x[1]
            sage: S = SymmetricReductionStrategy(X, [a,b])
            sage: p._p.parent().has_coerce_map_from(a._p.parent())
            False
            sage: q = S(p)
            sage: q.parent().has_coerce_map_from(a._p.parent())
            True
            sage: S(p) == S(p._p)
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    @overload
    def __getinitargs__(self) -> Any:
        """SymmetricReductionStrategy.__getinitargs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 174)

        Used for pickling.

        EXAMPLES::

            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]], good_input=True)
            sage: S.__getinitargs__()
            (Infinite polynomial ring in y over Rational Field, [], 0, None)"""
    @overload
    def __getinitargs__(self) -> Any:
        """SymmetricReductionStrategy.__getinitargs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/symmetric_reduction.pyx (starting at line 174)

        Used for pickling.

        EXAMPLES::

            sage: X.<y> = InfinitePolynomialRing(QQ)
            sage: from sage.rings.polynomial.symmetric_reduction import SymmetricReductionStrategy
            sage: S = SymmetricReductionStrategy(X, [y[2]^2*y[1],y[1]^2*y[2]], good_input=True)
            sage: S.__getinitargs__()
            (Infinite polynomial ring in y over Rational Field, [], 0, None)"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
