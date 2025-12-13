import sage.rings.polynomial.skew_polynomial_finite_order
from sage.arith.misc import factorial as factorial
from sage.categories.category import ZZ as ZZ
from sage.combinat.q_analogues import q_jordan as q_jordan
from sage.matrix.matrix2 import NotFullRankError as NotFullRankError
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.mrange import xmrange_iter as xmrange_iter
from sage.misc.prandom import sample as sample
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from typing import Any, ClassVar, overload

class SkewPolynomial_finite_field_dense(sage.rings.polynomial.skew_polynomial_finite_order.SkewPolynomial_finite_order_dense):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def count_factorizations(self) -> Any:
        """SkewPolynomial_finite_field_dense.count_factorizations(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 987)

        Return the number of factorizations (as a product of a
        unit and a product of irreducible monic factors) of this
        skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + (4*t + 3)*x^3 + t^2*x^2 + (4*t^2 + 3*t)*x + 3*t
            sage: a.count_factorizations()
            216

        We illustrate that an irreducible polynomial in the center have
        in general a lot of distinct factorizations in the skew polynomial
        ring::

            sage: Z.<x3> = S.center()
            sage: N = x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3
            sage: N.is_irreducible()
            True
            sage: S(N).count_factorizations()
            30537115626"""
    @overload
    def count_factorizations(self) -> Any:
        """SkewPolynomial_finite_field_dense.count_factorizations(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 987)

        Return the number of factorizations (as a product of a
        unit and a product of irreducible monic factors) of this
        skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + (4*t + 3)*x^3 + t^2*x^2 + (4*t^2 + 3*t)*x + 3*t
            sage: a.count_factorizations()
            216

        We illustrate that an irreducible polynomial in the center have
        in general a lot of distinct factorizations in the skew polynomial
        ring::

            sage: Z.<x3> = S.center()
            sage: N = x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3
            sage: N.is_irreducible()
            True
            sage: S(N).count_factorizations()
            30537115626"""
    @overload
    def count_factorizations(self) -> Any:
        """SkewPolynomial_finite_field_dense.count_factorizations(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 987)

        Return the number of factorizations (as a product of a
        unit and a product of irreducible monic factors) of this
        skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + (4*t + 3)*x^3 + t^2*x^2 + (4*t^2 + 3*t)*x + 3*t
            sage: a.count_factorizations()
            216

        We illustrate that an irreducible polynomial in the center have
        in general a lot of distinct factorizations in the skew polynomial
        ring::

            sage: Z.<x3> = S.center()
            sage: N = x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3
            sage: N.is_irreducible()
            True
            sage: S(N).count_factorizations()
            30537115626"""
    @overload
    def count_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.count_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 683)

        Return the number of irreducible monic divisors of
        this skew polynomial.

        .. NOTE::

            One can prove that there are always as many left
            irreducible monic divisors as right irreducible
            monic divisors.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

        We illustrate that a skew polynomial may have a number of irreducible
        divisors greater than its degree::

            sage: a = x^4 + (4*t + 3)*x^3 + t^2*x^2 + (4*t^2 + 3*t)*x + 3*t
            sage: a.count_irreducible_divisors()
            12

        We illustrate that an irreducible polynomial in the center have
        in general a lot of irreducible divisors in the skew polynomial
        ring::

            sage: Z.<x3> = S.center()
            sage: N = x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3; N
            x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3
            sage: N.is_irreducible()
            True
            sage: S(N).count_irreducible_divisors()
            9768751"""
    @overload
    def count_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.count_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 683)

        Return the number of irreducible monic divisors of
        this skew polynomial.

        .. NOTE::

            One can prove that there are always as many left
            irreducible monic divisors as right irreducible
            monic divisors.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

        We illustrate that a skew polynomial may have a number of irreducible
        divisors greater than its degree::

            sage: a = x^4 + (4*t + 3)*x^3 + t^2*x^2 + (4*t^2 + 3*t)*x + 3*t
            sage: a.count_irreducible_divisors()
            12

        We illustrate that an irreducible polynomial in the center have
        in general a lot of irreducible divisors in the skew polynomial
        ring::

            sage: Z.<x3> = S.center()
            sage: N = x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3; N
            x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3
            sage: N.is_irreducible()
            True
            sage: S(N).count_irreducible_divisors()
            9768751"""
    @overload
    def count_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.count_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 683)

        Return the number of irreducible monic divisors of
        this skew polynomial.

        .. NOTE::

            One can prove that there are always as many left
            irreducible monic divisors as right irreducible
            monic divisors.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

        We illustrate that a skew polynomial may have a number of irreducible
        divisors greater than its degree::

            sage: a = x^4 + (4*t + 3)*x^3 + t^2*x^2 + (4*t^2 + 3*t)*x + 3*t
            sage: a.count_irreducible_divisors()
            12

        We illustrate that an irreducible polynomial in the center have
        in general a lot of irreducible divisors in the skew polynomial
        ring::

            sage: Z.<x3> = S.center()
            sage: N = x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3; N
            x3^5 + 4*x3^4 + 4*x3^2 + 4*x3 + 3
            sage: N.is_irreducible()
            True
            sage: S(N).count_irreducible_divisors()
            9768751"""
    @overload
    def factor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factor(self) -> Any:
        """SkewPolynomial_finite_field_dense.factor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 920)

        Return a factorization of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)
            sage: F.value() == a
            True

        The result of the factorization is cached. Hence, if we try
        again to factor `a`, we will get the same answer::

            sage: a.factor()  # random
            (x + t^2 + 4) * (x + t + 3) * (x + t)

        However, the algorithm is probabilistic. Hence if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^3 + (t^2 + 4*t + 2)*x^2 + (3*t + 3)*x + t^2 + 1
            sage: F = a.factor(); F   # random
            (x + t^2 + t + 2) * (x + 2*t^2 + t + 4) * (x + t)
            sage: F.value() == a
            True

        There is a priori no guarantee on the distribution of the
        factorizations we get. Passing in the keyword ``uniform=True``
        ensures the output is uniformly distributed among all
        factorizations::

            sage: a.factor(uniform=True)   # random
            (x + t^2 + 4) * (x + t) * (x + t + 3)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2) * (x + t^2 + t + 1) * (x + t^2 + t + 2)
            sage: a.factor(uniform=True)   # random
            (x + 2*t^2 + 3*t) * (x + 4*t + 2) * (x + 2*t + 2)

        By convention, the zero skew polynomial has no factorization::

            sage: S(0).factor()
            Traceback (most recent call last):
            ...
            ValueError: factorization of 0 not defined"""
    @overload
    def factorizations(self) -> Any:
        '''SkewPolynomial_finite_field_dense.factorizations(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 1032)

        Return an iterator over all factorizations (as a product
        of a unit and a product of irreducible monic factors) of
        this skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k[\'x\',Frob]
            sage: a = x^3 + (t^2 + 1)*x^2 + (2*t + 3)*x + t^2 + t + 2
            sage: iter = a.factorizations(); iter
            <...generator object at 0x...>
            sage: next(iter)   # random
            (x + 3*t^2 + 4*t) * (x + 2*t^2) * (x + 4*t^2 + 4*t + 2)
            sage: next(iter)   # random
            (x + 3*t^2 + 4*t) * (x + 3*t^2 + 2*t + 2) * (x + 4*t^2 + t + 2)

        We can use this function to build the list of factorizations
        of `a`::

            sage: factorizations = [ F for F in a.factorizations() ]

        We do some checks::

            sage: len(factorizations) == a.count_factorizations()
            True
            sage: len(factorizations) == Set(factorizations).cardinality()  # check no duplicates
            True
            sage: for F in factorizations:
            ....:     assert F.value() == a, "factorization has a different value"
            ....:     for d,_ in F:
            ....:         assert d.is_irreducible(), "a factor is not irreducible"

        Note that the algorithm used in this method is probabilistic.
        As a consequence, if we call it two times with the same input,
        we can get different orderings::

            sage: factorizations2 = [ F for F in a.factorizations() ]
            sage: factorizations == factorizations2  # random
            False
            sage: sorted(factorizations) == sorted(factorizations2)
            True'''
    @overload
    def factorizations(self) -> Any:
        '''SkewPolynomial_finite_field_dense.factorizations(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 1032)

        Return an iterator over all factorizations (as a product
        of a unit and a product of irreducible monic factors) of
        this skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k[\'x\',Frob]
            sage: a = x^3 + (t^2 + 1)*x^2 + (2*t + 3)*x + t^2 + t + 2
            sage: iter = a.factorizations(); iter
            <...generator object at 0x...>
            sage: next(iter)   # random
            (x + 3*t^2 + 4*t) * (x + 2*t^2) * (x + 4*t^2 + 4*t + 2)
            sage: next(iter)   # random
            (x + 3*t^2 + 4*t) * (x + 3*t^2 + 2*t + 2) * (x + 4*t^2 + t + 2)

        We can use this function to build the list of factorizations
        of `a`::

            sage: factorizations = [ F for F in a.factorizations() ]

        We do some checks::

            sage: len(factorizations) == a.count_factorizations()
            True
            sage: len(factorizations) == Set(factorizations).cardinality()  # check no duplicates
            True
            sage: for F in factorizations:
            ....:     assert F.value() == a, "factorization has a different value"
            ....:     for d,_ in F:
            ....:         assert d.is_irreducible(), "a factor is not irreducible"

        Note that the algorithm used in this method is probabilistic.
        As a consequence, if we call it two times with the same input,
        we can get different orderings::

            sage: factorizations2 = [ F for F in a.factorizations() ]
            sage: factorizations == factorizations2  # random
            False
            sage: sorted(factorizations) == sorted(factorizations2)
            True'''
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def is_irreducible(self) -> Any:
        """SkewPolynomial_finite_field_dense.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 56)

        Return ``True`` if this skew polynomial is irreducible.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]

            sage: a = x^2 + t*x + 1
            sage: a.is_irreducible()
            False
            sage: a.factor()
            (x + 4*t^2 + 4*t + 1) * (x + 3*t + 2)

            sage: a = x^2 + t*x + t + 1
            sage: a.is_irreducible()
            True
            sage: a.factor()
            x^2 + t*x + t + 1

        Skew polynomials of degree `1` are of course irreducible::

            sage: a = x + t
            sage: a.is_irreducible()
            True

        A random irreducible skew polynomial is irreducible::

            sage: a = S.random_irreducible(degree=4,monic=True); a   # random
            x^4 + (t + 1)*x^3 + (3*t^2 + 2*t + 3)*x^2 + 3*t*x + 3*t
            sage: a.is_irreducible()
            True

        By convention, constant skew polynomials are not irreducible::

            sage: S(1).is_irreducible()
            False
            sage: S(0).is_irreducible()
            False"""
    @overload
    def left_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 543)

        Return a left irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: dl = a.left_irreducible_divisor(); dl  # random
            x^3 + (t^2 + t + 2)*x^2 + (t + 2)*x + 3*t^2 + t + 4
            sage: a.is_left_divisible_by(dl)
            True

        The algorithm is probabilistic. Hence, if we ask again for
        a left irreducible divisor of `a`, we may get a different
        answer::

            sage: a.left_irreducible_divisor()  # random
            x^3 + (4*t + 3)*x^2 + (2*t^2 + 3*t + 4)*x + 4*t^2 + 2*t

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + t + 3)*x + 2*t^2 + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (2*t^2 + 4*t + 4)*x + 2*t + 3
            sage: a.left_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + t + 2)*x^2 + (3*t^2 + t)*x + 2*t + 1

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).left_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def left_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 650)

        Return an iterator over all irreducible monic left divisors
        of this skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + 2*t*x^3 + 3*t^2*x^2 + (t^2 + t + 1)*x + 4*t + 3
            sage: iter = a.left_irreducible_divisors(); iter
            <...generator object at 0x...>
            sage: next(iter)  # random
            x + 3*t + 3
            sage: next(iter)  # random
            x + 4*t + 2

        We can use this function to build the list of all monic
        irreducible divisors of `a`::

            sage: leftdiv = [ d for d in a.left_irreducible_divisors() ]

        Note that the algorithm is probabilistic. As a consequence, if we
        build again the list of left monic irreducible divisors of `a`, we
        may get a different ordering::

            sage: leftdiv2 = [ d for d in a.left_irreducible_divisors() ]
            sage: Set(leftdiv) == Set(leftdiv2)
            True"""
    @overload
    def left_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.left_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 650)

        Return an iterator over all irreducible monic left divisors
        of this skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + 2*t*x^3 + 3*t^2*x^2 + (t^2 + t + 1)*x + 4*t + 3
            sage: iter = a.left_irreducible_divisors(); iter
            <...generator object at 0x...>
            sage: next(iter)  # random
            x + 3*t + 3
            sage: next(iter)  # random
            x + 4*t + 2

        We can use this function to build the list of all monic
        irreducible divisors of `a`::

            sage: leftdiv = [ d for d in a.left_irreducible_divisors() ]

        Note that the algorithm is probabilistic. As a consequence, if we
        build again the list of left monic irreducible divisors of `a`, we
        may get a different ordering::

            sage: leftdiv2 = [ d for d in a.left_irreducible_divisors() ]
            sage: Set(leftdiv) == Set(leftdiv2)
            True"""
    @overload
    def right_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self, uniform=...) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisor(self) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisor(self, uniform=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 468)

        Return a right irreducible divisor of this skew polynomial.

        INPUT:

        - ``uniform`` -- boolean (default: ``False``); whether the
          output irreducible divisor should be uniformly distributed
          among all possibilities

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3

            sage: dr = a.right_irreducible_divisor(); dr  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1
            sage: a.is_right_divisible_by(dr)
            True

        Right divisors are cached. Hence, if we ask again for a
        right divisor, we will get the same answer::

            sage: a.right_irreducible_divisor()  # random
            x^3 + (2*t^2 + t + 4)*x^2 + (4*t + 1)*x + 4*t^2 + t + 1

        However the algorithm is probabilistic. Hence, if we first
        reinitialize `a`, we may get a different answer::

            sage: a = x^6 + 3*t*x^5 + (3*t + 1)*x^3 + (4*t^2 + 3*t + 4)*x^2 + (t^2 + 2)*x + 4*t^2 + 3*t + 3
            sage: a.right_irreducible_divisor()  # random
            x^3 + (t^2 + 3*t + 4)*x^2 + (t + 2)*x + 4*t^2 + t + 1

        We can also generate uniformly distributed irreducible monic
        divisors as follows::

            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (4*t + 2)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 2
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + (t^2 + 2)*x^2 + (3*t^2 + 1)*x + 4*t^2 + 2*t
            sage: a.right_irreducible_divisor(uniform=True)  # random
            x^3 + x^2 + (4*t^2 + 2*t + 4)*x + t^2 + 3

        By convention, the zero skew polynomial has no irreducible
        divisor::

            sage: S(0).right_irreducible_divisor()
            Traceback (most recent call last):
            ...
            ValueError: 0 has no irreducible divisor"""
    @overload
    def right_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 615)

        Return an iterator over all irreducible monic right divisors
        of this skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + 2*t*x^3 + 3*t^2*x^2 + (t^2 + t + 1)*x + 4*t + 3
            sage: iter = a.right_irreducible_divisors(); iter
            <...generator object at 0x...>
            sage: next(iter)   # random
            x + 2*t^2 + 4*t + 4
            sage: next(iter)   # random
            x + 3*t^2 + 4*t + 1

        We can use this function to build the list of all monic
        irreducible divisors of `a`::

            sage: rightdiv = [ d for d in a.right_irreducible_divisors() ]

        Note that the algorithm is probabilistic. As a consequence, if we
        build again the list of right monic irreducible divisors of `a`, we
        may get a different ordering::

            sage: rightdiv2 = [ d for d in a.right_irreducible_divisors() ]
            sage: rightdiv == rightdiv2
            False
            sage: Set(rightdiv) == Set(rightdiv2)
            True"""
    @overload
    def right_irreducible_divisors(self) -> Any:
        """SkewPolynomial_finite_field_dense.right_irreducible_divisors(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 615)

        Return an iterator over all irreducible monic right divisors
        of this skew polynomial.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^4 + 2*t*x^3 + 3*t^2*x^2 + (t^2 + t + 1)*x + 4*t + 3
            sage: iter = a.right_irreducible_divisors(); iter
            <...generator object at 0x...>
            sage: next(iter)   # random
            x + 2*t^2 + 4*t + 4
            sage: next(iter)   # random
            x + 3*t^2 + 4*t + 1

        We can use this function to build the list of all monic
        irreducible divisors of `a`::

            sage: rightdiv = [ d for d in a.right_irreducible_divisors() ]

        Note that the algorithm is probabilistic. As a consequence, if we
        build again the list of right monic irreducible divisors of `a`, we
        may get a different ordering::

            sage: rightdiv2 = [ d for d in a.right_irreducible_divisors() ]
            sage: rightdiv == rightdiv2
            False
            sage: Set(rightdiv) == Set(rightdiv2)
            True"""
    def type(self, N) -> Any:
        """SkewPolynomial_finite_field_dense.type(self, N)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_field.pyx (starting at line 103)

        Return the `N`-type of this skew polynomial (see definition below).

        INPUT:

        - ``N`` -- an irreducible polynomial in the
          center of the underlying skew polynomial ring

        .. NOTE::

            The result is cached.

        DEFINITION:

        The `N`-type of a skew polynomial `a` is the Partition
        `(t_0, t_1, t_2, \\ldots)` defined by

        .. MATH::

            t_0 + \\cdots + t_i = \\frac{\\deg gcd(a,N^i)}{\\deg N},

        where `\\deg N` is the degree of `N` considered as an
        element in the center.

        This notion has an important mathematical interest because
        it corresponds to the Jordan type of the `N`-typical part
        of the associated Galois representation.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: Z = S.center(); x3 = Z.gen()

            sage: a = x^4 + x^3 + (4*t^2 + 4)*x^2 + (t^2 + 2)*x + 4*t^2
            sage: N = x3^2 + x3 + 1
            sage: a.type(N)
            [1]
            sage: N = x3 + 1
            sage: a.type(N)
            [2]

            sage: a = x^3 + (3*t^2 + 1)*x^2 + (3*t^2 + t + 1)*x + t + 1
            sage: N = x3 + 1
            sage: a.type(N)
            [2, 1]

        If `N` does not divide the reduced map of `a`, the type
        is empty::

            sage: N = x3 + 2
            sage: a.type(N)
            []

        If `a = N`, the type is just `[r]` where `r` is the order
        of the twisting morphism ``Frob``::

            sage: N = x3^2 + x3 + 1
            sage: S(N).type(N)
            [3]

        `N` must be irreducible::

            sage: N = (x3 + 1) * (x3 + 2)
            sage: a.type(N)
            Traceback (most recent call last):
            ...
            ValueError: N is not irreducible"""
