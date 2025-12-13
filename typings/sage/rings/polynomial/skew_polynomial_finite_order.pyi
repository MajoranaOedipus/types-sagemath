import sage.rings.polynomial.skew_polynomial_element
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class SkewPolynomial_finite_order_dense(sage.rings.polynomial.skew_polynomial_element.SkewPolynomial_generic_dense):
    """SkewPolynomial_finite_order_dense(parent, x=None, int check=1, int construct=0, **kwds)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., intcheck=..., intconstruct=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 29)

                This method constructs a generic dense skew polynomial over a field equipped
                with an automorphism of finite order.

                INPUT:

                - ``parent`` -- parent of ``self``

                - ``x`` -- list of coefficients from which ``self`` can be constructed

                - ``check`` -- flag variable to normalize the polynomial

                - ``construct`` -- boolean (default: ``False``)

                TESTS::

                    sage: R.<t> = GF(5^3)
                    sage: Frob = R.frobenius_endomorphism()
                    sage: S.<x> = R['x', Frob]; S
                    Ore Polynomial Ring in x over Finite Field in t of size 5^3 twisted by t |--> t^5

                We create a skew polynomial from a list::

                    sage: S([t,1])
                    x + t

                from another skew polynomial::

                    sage: S(x^2 + t)
                    x^2 + t

                from a constant::

                    sage: x = S(t^2 + 1); x
                    t^2 + 1
                    sage: x.parent() is S
                    True
        """
    @overload
    def bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 437)

        Return a bound of this skew polynomial (i.e. a multiple
        of this skew polynomial lying in the center).

        .. NOTE::

            Since `b` is central, it divides a skew polynomial
            on the left iff it divides it on the right

        ALGORITHM:

        #. Sage first checks whether self is itself in the
           center. It if is, it returns ``self``

        #. If an optimal bound was previously computed and
           cached, Sage returns it

        #. Otherwise, Sage returns the reduced norm of ``self``

        As a consequence, the output of this function may depend
        on previous computations (an example is given below).

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.bound(); b
            z^2 + z + 4

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^6 + x^3 + 4

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True

        Actually, `b` is the reduced norm of `a`::

            sage: b == a.reduced_norm()
            True

        Now, we compute the optimal bound of `a` and see that
        it affects the behaviour of ``bound()``::

            sage: a.optimal_bound()
            z + 3
            sage: a.bound()
            z + 3

        TESTS:

        We check that when the input skew polynomial lies in
        the center, the output is the skew polynomial itself::

            sage: a = Z.random_element(degree=4)
            sage: b = S(a).bound()
            sage: a == b
            True"""
    @overload
    def bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 437)

        Return a bound of this skew polynomial (i.e. a multiple
        of this skew polynomial lying in the center).

        .. NOTE::

            Since `b` is central, it divides a skew polynomial
            on the left iff it divides it on the right

        ALGORITHM:

        #. Sage first checks whether self is itself in the
           center. It if is, it returns ``self``

        #. If an optimal bound was previously computed and
           cached, Sage returns it

        #. Otherwise, Sage returns the reduced norm of ``self``

        As a consequence, the output of this function may depend
        on previous computations (an example is given below).

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.bound(); b
            z^2 + z + 4

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^6 + x^3 + 4

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True

        Actually, `b` is the reduced norm of `a`::

            sage: b == a.reduced_norm()
            True

        Now, we compute the optimal bound of `a` and see that
        it affects the behaviour of ``bound()``::

            sage: a.optimal_bound()
            z + 3
            sage: a.bound()
            z + 3

        TESTS:

        We check that when the input skew polynomial lies in
        the center, the output is the skew polynomial itself::

            sage: a = Z.random_element(degree=4)
            sage: b = S(a).bound()
            sage: a == b
            True"""
    @overload
    def bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 437)

        Return a bound of this skew polynomial (i.e. a multiple
        of this skew polynomial lying in the center).

        .. NOTE::

            Since `b` is central, it divides a skew polynomial
            on the left iff it divides it on the right

        ALGORITHM:

        #. Sage first checks whether self is itself in the
           center. It if is, it returns ``self``

        #. If an optimal bound was previously computed and
           cached, Sage returns it

        #. Otherwise, Sage returns the reduced norm of ``self``

        As a consequence, the output of this function may depend
        on previous computations (an example is given below).

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.bound(); b
            z^2 + z + 4

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^6 + x^3 + 4

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True

        Actually, `b` is the reduced norm of `a`::

            sage: b == a.reduced_norm()
            True

        Now, we compute the optimal bound of `a` and see that
        it affects the behaviour of ``bound()``::

            sage: a.optimal_bound()
            z + 3
            sage: a.bound()
            z + 3

        TESTS:

        We check that when the input skew polynomial lies in
        the center, the output is the skew polynomial itself::

            sage: a = Z.random_element(degree=4)
            sage: b = S(a).bound()
            sage: a == b
            True"""
    @overload
    def bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 437)

        Return a bound of this skew polynomial (i.e. a multiple
        of this skew polynomial lying in the center).

        .. NOTE::

            Since `b` is central, it divides a skew polynomial
            on the left iff it divides it on the right

        ALGORITHM:

        #. Sage first checks whether self is itself in the
           center. It if is, it returns ``self``

        #. If an optimal bound was previously computed and
           cached, Sage returns it

        #. Otherwise, Sage returns the reduced norm of ``self``

        As a consequence, the output of this function may depend
        on previous computations (an example is given below).

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.bound(); b
            z^2 + z + 4

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^6 + x^3 + 4

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True

        Actually, `b` is the reduced norm of `a`::

            sage: b == a.reduced_norm()
            True

        Now, we compute the optimal bound of `a` and see that
        it affects the behaviour of ``bound()``::

            sage: a.optimal_bound()
            z + 3
            sage: a.bound()
            z + 3

        TESTS:

        We check that when the input skew polynomial lies in
        the center, the output is the skew polynomial itself::

            sage: a = Z.random_element(degree=4)
            sage: b = S(a).bound()
            sage: a == b
            True"""
    @overload
    def bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 437)

        Return a bound of this skew polynomial (i.e. a multiple
        of this skew polynomial lying in the center).

        .. NOTE::

            Since `b` is central, it divides a skew polynomial
            on the left iff it divides it on the right

        ALGORITHM:

        #. Sage first checks whether self is itself in the
           center. It if is, it returns ``self``

        #. If an optimal bound was previously computed and
           cached, Sage returns it

        #. Otherwise, Sage returns the reduced norm of ``self``

        As a consequence, the output of this function may depend
        on previous computations (an example is given below).

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.bound(); b
            z^2 + z + 4

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^6 + x^3 + 4

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True

        Actually, `b` is the reduced norm of `a`::

            sage: b == a.reduced_norm()
            True

        Now, we compute the optimal bound of `a` and see that
        it affects the behaviour of ``bound()``::

            sage: a.optimal_bound()
            z + 3
            sage: a.bound()
            z + 3

        TESTS:

        We check that when the input skew polynomial lies in
        the center, the output is the skew polynomial itself::

            sage: a = Z.random_element(degree=4)
            sage: b = S(a).bound()
            sage: a == b
            True"""
    @overload
    def is_central(self) -> bool:
        """SkewPolynomial_finite_order_dense.is_central(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 413)

        Return ``True`` if this skew polynomial lies in the center.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]

            sage: x.is_central()
            False
            sage: (t*x^3).is_central()
            False
            sage: (x^6 + x^3).is_central()
            True"""
    @overload
    def is_central(self) -> Any:
        """SkewPolynomial_finite_order_dense.is_central(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 413)

        Return ``True`` if this skew polynomial lies in the center.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]

            sage: x.is_central()
            False
            sage: (t*x^3).is_central()
            False
            sage: (x^6 + x^3).is_central()
            True"""
    @overload
    def is_central(self) -> Any:
        """SkewPolynomial_finite_order_dense.is_central(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 413)

        Return ``True`` if this skew polynomial lies in the center.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]

            sage: x.is_central()
            False
            sage: (t*x^3).is_central()
            False
            sage: (x^6 + x^3).is_central()
            True"""
    @overload
    def is_central(self) -> Any:
        """SkewPolynomial_finite_order_dense.is_central(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 413)

        Return ``True`` if this skew polynomial lies in the center.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]

            sage: x.is_central()
            False
            sage: (t*x^3).is_central()
            False
            sage: (x^6 + x^3).is_central()
            True"""
    @overload
    def optimal_bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.optimal_bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 518)

        Return the optimal bound of this skew polynomial (i.e.
        the monic multiple of this skew polynomial of minimal
        degree lying in the center).

        .. NOTE::

            The result is cached.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.optimal_bound(); b
            z + 3

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^3 + 3

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True"""
    @overload
    def optimal_bound(self) -> Any:
        """SkewPolynomial_finite_order_dense.optimal_bound(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 518)

        Return the optimal bound of this skew polynomial (i.e.
        the monic multiple of this skew polynomial of minimal
        degree lying in the center).

        .. NOTE::

            The result is cached.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: Z = S.center(); Z
            Univariate Polynomial Ring in z over Finite Field of size 5

            sage: a = x^2 + (4*t + 2)*x + 4*t^2 + 3
            sage: b = a.optimal_bound(); b
            z + 3

        We observe that the bound is explicitly given as an element of the
        center (which is a univariate polynomial ring in the variable `z`).
        We can use conversion to send it in the skew polynomial ring::

            sage: S(b)
            x^3 + 3

        We check that `b` is divisible by `a`::

            sage: S(b).is_right_divisible_by(a)
            True
            sage: S(b).is_left_divisible_by(a)
            True"""
    @overload
    def reduced_charpoly(self, var=...) -> Any:
        """SkewPolynomial_finite_order_dense.reduced_charpoly(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 336)

        Return the reduced characteristic polynomial of this
        skew polynomial.

        INPUT:

        - ``var`` -- string, a pair of strings or ``None``
          (default: ``None``); the variable names used for the
          characteristic polynomial and the center

        .. NOTE::

            The result is cached.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<u> = k['u', Frob]
            sage: a = u^3 + (2*t^2 + 3)*u^2 + (4*t^2 + t + 4)*u + 2*t^2 + 2
            sage: chi = a.reduced_charpoly()
            sage: chi
            x^3 + (2*z + 1)*x^2 + (3*z^2 + 4*z)*x + 4*z^3 + z^2 + 1

        The reduced characteristic polynomial has coefficients in the center
        of `S`, which is itself a univariate polynomial ring in the variable
        `z = u^3` over `\\GF{5}`. Hence it appears as a bivariate polynomial::

            sage: chi.parent()
            Univariate Polynomial Ring in x over Univariate Polynomial Ring in z over Finite Field of size 5

        The constant coefficient of the reduced characteristic polynomial is
        the reduced norm, up to a sign::

            sage: chi[0] == -a.reduced_norm()
            True

        Its coefficient of degree `\\deg(a) - 1` is the opposite of the reduced
        trace::

            sage: chi[2] == -a.reduced_trace()
            True

        By default, the name of the variable of the reduced characteristic
        polynomial is ``x`` and the name of central variable is usually ``z``
        (see :meth:`~sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        The user can speciify different names if desired::

            sage: a.reduced_charpoly(var='T')  # variable name for the characteristic polynomial
            T^3 + (2*z + 1)*T^2 + (3*z^2 + 4*z)*T + 4*z^3 + z^2 + 1

            sage: a.reduced_charpoly(var=('T', 'c'))
            T^3 + (2*c + 1)*T^2 + (3*c^2 + 4*c)*T + 4*c^3 + c^2 + 1

        .. SEEALSO::

            :meth:`reduced_trace`, :meth:`reduced_norm`"""
    @overload
    def reduced_charpoly(self) -> Any:
        """SkewPolynomial_finite_order_dense.reduced_charpoly(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 336)

        Return the reduced characteristic polynomial of this
        skew polynomial.

        INPUT:

        - ``var`` -- string, a pair of strings or ``None``
          (default: ``None``); the variable names used for the
          characteristic polynomial and the center

        .. NOTE::

            The result is cached.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<u> = k['u', Frob]
            sage: a = u^3 + (2*t^2 + 3)*u^2 + (4*t^2 + t + 4)*u + 2*t^2 + 2
            sage: chi = a.reduced_charpoly()
            sage: chi
            x^3 + (2*z + 1)*x^2 + (3*z^2 + 4*z)*x + 4*z^3 + z^2 + 1

        The reduced characteristic polynomial has coefficients in the center
        of `S`, which is itself a univariate polynomial ring in the variable
        `z = u^3` over `\\GF{5}`. Hence it appears as a bivariate polynomial::

            sage: chi.parent()
            Univariate Polynomial Ring in x over Univariate Polynomial Ring in z over Finite Field of size 5

        The constant coefficient of the reduced characteristic polynomial is
        the reduced norm, up to a sign::

            sage: chi[0] == -a.reduced_norm()
            True

        Its coefficient of degree `\\deg(a) - 1` is the opposite of the reduced
        trace::

            sage: chi[2] == -a.reduced_trace()
            True

        By default, the name of the variable of the reduced characteristic
        polynomial is ``x`` and the name of central variable is usually ``z``
        (see :meth:`~sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        The user can speciify different names if desired::

            sage: a.reduced_charpoly(var='T')  # variable name for the characteristic polynomial
            T^3 + (2*z + 1)*T^2 + (3*z^2 + 4*z)*T + 4*z^3 + z^2 + 1

            sage: a.reduced_charpoly(var=('T', 'c'))
            T^3 + (2*c + 1)*T^2 + (3*c^2 + 4*c)*T + 4*c^3 + c^2 + 1

        .. SEEALSO::

            :meth:`reduced_trace`, :meth:`reduced_norm`"""
    @overload
    def reduced_norm(self, var=...) -> Any:
        """SkewPolynomial_finite_order_dense.reduced_norm(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 224)

        Return the reduced norm of this skew polynomial.

        INPUT:

        - ``var`` -- string or ``False`` or ``None`` (default: ``None``);
          the variable name. If ``False``, return the list of coefficients.

        .. NOTE::

            The result is cached.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: a = x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: N = a.reduced_norm(); N
            z^3 + 4*z^2 + 4

        The reduced norm lies in the center of `S`, which is a univariate
        polynomial ring in the variable `z = x^3` over `\\GF{5}`::

            sage: N.parent()
            Univariate Polynomial Ring in z over Finite Field of size 5
            sage: N.parent() is S.center()
            True

        We can use explicit conversion to view ``N`` as a skew polynomial::

            sage: S(N)
            x^9 + 4*x^6 + 4

        By default, the name of the central variable is usually ``z`` (see
        :meth:`~sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        However, the user can specify a different variable name if desired::

            sage: a.reduced_norm(var='u')
            u^3 + 4*u^2 + 4

        When passing in ``var=False``, a tuple of coefficients (instead of
        an actual polynomial) is returned::

            sage: a.reduced_norm(var=False)
            (4, 0, 4, 1)

        TESTS:

        We check that `N` is a multiple of `a`::

            sage: S(N).is_right_divisible_by(a)
            True
            sage: S(N).is_left_divisible_by(a)
            True

        We check that the reduced norm is a multiplicative map::

            sage: a = S.random_element(degree=5)
            sage: b = S.random_element(degree=7)
            sage: a.reduced_norm() * b.reduced_norm() == (a*b).reduced_norm()
            True

        We check that the reduced norm is correctly computed for a
        constant polynomial::

            sage: c = k.random_element()
            sage: S(c).reduced_norm() == c.norm()
            True

        ALGORITHM:

        If `r` (= the order of the twist map) is small compared
        to `d` (= the degree of this skew polynomial), the reduced
        norm is computed as the determinant of the multiplication
        by `P` (= this skew polynomial) acting on `K[X,\\sigma]`
        (= the underlying skew ring) viewed as a free module of
        rank `r` over `K[X^r]`.

        Otherwise, the reduced norm is computed as the characteristic
        polynomial of the left multiplication by `X` on the quotient
        `K[X,\\sigma] / K[X,\\sigma] P` (which is a `K`-vector space
        of dimension `d`).

        .. SEEALSO::

            :meth:`reduced_trace`, :meth:`reduced_charpoly`"""
    @overload
    def reduced_norm(self) -> Any:
        """SkewPolynomial_finite_order_dense.reduced_norm(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 224)

        Return the reduced norm of this skew polynomial.

        INPUT:

        - ``var`` -- string or ``False`` or ``None`` (default: ``None``);
          the variable name. If ``False``, return the list of coefficients.

        .. NOTE::

            The result is cached.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: a = x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: N = a.reduced_norm(); N
            z^3 + 4*z^2 + 4

        The reduced norm lies in the center of `S`, which is a univariate
        polynomial ring in the variable `z = x^3` over `\\GF{5}`::

            sage: N.parent()
            Univariate Polynomial Ring in z over Finite Field of size 5
            sage: N.parent() is S.center()
            True

        We can use explicit conversion to view ``N`` as a skew polynomial::

            sage: S(N)
            x^9 + 4*x^6 + 4

        By default, the name of the central variable is usually ``z`` (see
        :meth:`~sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        However, the user can specify a different variable name if desired::

            sage: a.reduced_norm(var='u')
            u^3 + 4*u^2 + 4

        When passing in ``var=False``, a tuple of coefficients (instead of
        an actual polynomial) is returned::

            sage: a.reduced_norm(var=False)
            (4, 0, 4, 1)

        TESTS:

        We check that `N` is a multiple of `a`::

            sage: S(N).is_right_divisible_by(a)
            True
            sage: S(N).is_left_divisible_by(a)
            True

        We check that the reduced norm is a multiplicative map::

            sage: a = S.random_element(degree=5)
            sage: b = S.random_element(degree=7)
            sage: a.reduced_norm() * b.reduced_norm() == (a*b).reduced_norm()
            True

        We check that the reduced norm is correctly computed for a
        constant polynomial::

            sage: c = k.random_element()
            sage: S(c).reduced_norm() == c.norm()
            True

        ALGORITHM:

        If `r` (= the order of the twist map) is small compared
        to `d` (= the degree of this skew polynomial), the reduced
        norm is computed as the determinant of the multiplication
        by `P` (= this skew polynomial) acting on `K[X,\\sigma]`
        (= the underlying skew ring) viewed as a free module of
        rank `r` over `K[X^r]`.

        Otherwise, the reduced norm is computed as the characteristic
        polynomial of the left multiplication by `X` on the quotient
        `K[X,\\sigma] / K[X,\\sigma] P` (which is a `K`-vector space
        of dimension `d`).

        .. SEEALSO::

            :meth:`reduced_trace`, :meth:`reduced_charpoly`"""
    @overload
    def reduced_trace(self, var=...) -> Any:
        """SkewPolynomial_finite_order_dense.reduced_trace(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 153)

        Return the reduced trace of this skew polynomial.

        INPUT:

        - ``var`` -- string or ``False`` or ``None`` (default: ``None``);
          the variable name. If ``False``, return the list of coefficients.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: a = x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: tr = a.reduced_trace(); tr
            3*z + 4

        The reduced trace lies in the center of `S`, which is a univariate
        polynomial ring in the variable `z = x^3` over `\\GF{5}`::

            sage: tr.parent()
            Univariate Polynomial Ring in z over Finite Field of size 5
            sage: tr.parent() is S.center()
            True

        We can use explicit conversion to view ``tr`` as a skew polynomial::

            sage: S(tr)
            3*x^3 + 4

        By default, the name of the central variable is usually ``z`` (see
        :meth:`~sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        However, the user can specify a different variable name if desired::

            sage: a.reduced_trace(var='u')
            3*u + 4

        When passing in ``var=False``, a tuple of coefficients (instead of
        an actual polynomial) is returned::

            sage: a.reduced_trace(var=False)
            (4, 3)

        TESTS:

        We check that the reduced trace is additive::

            sage: a = S.random_element(degree=5)
            sage: b = S.random_element(degree=7)
            sage: a.reduced_trace() + b.reduced_trace() == (a+b).reduced_trace()
            True

        .. SEEALSO::

            :meth:`reduced_norm`, :meth:`reduced_charpoly`"""
    @overload
    def reduced_trace(self) -> Any:
        """SkewPolynomial_finite_order_dense.reduced_trace(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/skew_polynomial_finite_order.pyx (starting at line 153)

        Return the reduced trace of this skew polynomial.

        INPUT:

        - ``var`` -- string or ``False`` or ``None`` (default: ``None``);
          the variable name. If ``False``, return the list of coefficients.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: a = x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: tr = a.reduced_trace(); tr
            3*z + 4

        The reduced trace lies in the center of `S`, which is a univariate
        polynomial ring in the variable `z = x^3` over `\\GF{5}`::

            sage: tr.parent()
            Univariate Polynomial Ring in z over Finite Field of size 5
            sage: tr.parent() is S.center()
            True

        We can use explicit conversion to view ``tr`` as a skew polynomial::

            sage: S(tr)
            3*x^3 + 4

        By default, the name of the central variable is usually ``z`` (see
        :meth:`~sage.rings.polynomial.skew_polynomial_ring.SkewPolynomialRing_finite_order.center`
        for more details about this).
        However, the user can specify a different variable name if desired::

            sage: a.reduced_trace(var='u')
            3*u + 4

        When passing in ``var=False``, a tuple of coefficients (instead of
        an actual polynomial) is returned::

            sage: a.reduced_trace(var=False)
            (4, 3)

        TESTS:

        We check that the reduced trace is additive::

            sage: a = S.random_element(degree=5)
            sage: b = S.random_element(degree=7)
            sage: a.reduced_trace() + b.reduced_trace() == (a+b).reduced_trace()
            True

        .. SEEALSO::

            :meth:`reduced_norm`, :meth:`reduced_charpoly`"""
