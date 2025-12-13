from .drinfeld_module import DrinfeldModule as DrinfeldModule
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ

class DrinfeldModule_charzero(DrinfeldModule):
    """
    This class implements Drinfeld `\\mathbb{F}_q[T]`-modules defined
    over fields of `\\mathbb{F}_q[T]`-characteristic zero.

    Recall that the `\\mathbb{F}_q[T]`-*characteristic* is defined as the
    kernel of the underlying structure morphism. For general definitions
    and help on Drinfeld modules, see class
    :class:`sage.rings.function_fields.drinfeld_module.drinfeld_module.DrinfeldModule`.

    .. RUBRIC:: Construction:

    The user does not ever need to directly call
    ``DrinfeldModule_charzero`` --- the metaclass ``DrinfeldModule`` is
    responsible for instantiating the right class depending on the
    input::

        sage: A = GF(3)['T']
        sage: K.<T> = Frac(A)
        sage: phi = DrinfeldModule(A, [T, 1])
        sage: phi
        Drinfeld module defined by T |--> t + T

    ::

        sage: isinstance(phi, DrinfeldModule)
        True
        sage: from sage.rings.function_field.drinfeld_modules.charzero_drinfeld_module import DrinfeldModule_charzero
        sage: isinstance(phi, DrinfeldModule_charzero)
        True

    .. RUBRIC:: Logarithm and exponential

    It is possible to calculate the logarithm and the exponential of
    any Drinfeld modules of characteristic zero::

        sage: A = GF(2)['T']
        sage: K.<T> = Frac(A)
        sage: phi = DrinfeldModule(A, [T, 1])
        sage: phi.exponential()
        z + ((1/(T^2+T))*z^2) + ((1/(T^8+T^6+T^5+T^3))*z^4) + O(z^8)
        sage: phi.logarithm()
        z + ((1/(T^2+T))*z^2) + ((1/(T^6+T^5+T^3+T^2))*z^4) + O(z^8)

    .. RUBRIC:: Goss polynomials

    Goss polynomials are a sequence of polynomials related with the
    analytic theory of Drinfeld module. They provide a function field
    analogue of certain classical trigonometric functions::

        sage: A = GF(2)['T']
        sage: K.<T> = Frac(A)
        sage: phi = DrinfeldModule(A, [T, 1])
        sage: phi.goss_polynomial(1)
        X
        sage: phi.goss_polynomial(2)
        X^2
        sage: phi.goss_polynomial(3)
        X^3 + (1/(T^2 + T))*X^2

    .. RUBRIC:: Base fields of `\\mathbb{F}_q[T]`-characteristic zero

    The base fields need not only be fraction fields of polynomials
    ring. In the following example, we construct a Drinfeld module over
    `\\mathbb{F}_q((1/T))`, the completion of the rational function field
    at the place `1/T`::

        sage: A.<T> = GF(2)[]
        sage: L.<s> = LaurentSeriesRing(GF(2))  # s = 1/T
        sage: phi = DrinfeldModule(A, [1/s, s + s^2 + s^5 + O(s^6), 1+1/s])
        sage: phi(T)
        (s^-1 + 1)*t^2 + (s + s^2 + s^5 + O(s^6))*t + s^-1

    One can also construct Drinfeld modules over SageMath's global
    function fields::

        sage: A.<T> = GF(5)[]
        sage: K.<z> = FunctionField(GF(5))  # z = T
        sage: phi = DrinfeldModule(A, [z, 1, z^2])
        sage: phi(T)
        z^2*t^2 + t + z
    """
    def exponential(self, prec=..., name: str = 'z'):
        """
        Return the exponential of this Drinfeld module.

        Note that the exponential is only defined when the
        `\\mathbb{F}_q[T]`-characteristic is zero.

        INPUT:

        - ``prec`` -- an integer or ``Infinity`` (default: ``Infinity``);
          the precision at which the series is returned; if ``Infinity``,
          a lazy power series in returned, else, a classical power series
          is returned.

        - ``name`` -- string (default: ``'z'``); the name of the
          generator of the lazy power series ring

        EXAMPLES::

            sage: A = GF(2)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, 1])
            sage: q = A.base_ring().cardinality()

        When ``prec`` is ``Infinity`` (which is the default),
        the exponential is returned as a lazy power series, meaning
        that any of its coefficients can be computed on demands::

            sage: exp = phi.exponential(); exp
            z + ((1/(T^2+T))*z^2) + ((1/(T^8+T^6+T^5+T^3))*z^4) + O(z^8)
            sage: exp[2^4]
            1/(T^64 + T^56 + T^52 + ... + T^27 + T^23 + T^15)
            sage: exp[2^5]
            1/(T^160 + T^144 + T^136 + ... + T^55 + T^47 + T^31)

        On the contrary, when ``prec`` is a finite number, all the
        required coefficients are computed at once::

            sage: phi.exponential(prec=10)
            z + (1/(T^2 + T))*z^2 + (1/(T^8 + T^6 + T^5 + T^3))*z^4 + (1/(T^24 + T^20 + T^18 + T^17 + T^14 + T^13 + T^11 + T^7))*z^8 + O(z^10)

        Example in higher rank::

            sage: A = GF(5)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, T^2, T + T^2 + T^4, 1])
            sage: exp = phi.exponential(); exp
            z + ((T/(T^4+4))*z^5) + O(z^8)

        The exponential is the compositional inverse of the logarithm
        (see :meth:`logarithm`)::

            sage: log = phi.logarithm(); log
            z + ((4*T/(T^4+4))*z^5) + O(z^8)
            sage: exp.compose(log)
            z + O(z^8)
            sage: log.compose(exp)
            z + O(z^8)

        TESTS::

            sage: A = GF(2)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, 1])
            sage: exp = phi.exponential()
            sage: exp[2] == 1/(T**q - T)  # expected value
            True
            sage: exp[2^2] == 1/((T**(q**2) - T)*(T**q - T)**q)  # expected value
            True
            sage: exp[2^3] == 1/((T**(q**3) - T)*(T**(q**2) - T)**q*(T**q - T)**(q**2))  # expected value
            True

        REFERENCE:

        See section 4.6 of [Gos1998]_ for the definition of the
        exponential.
        """
    def logarithm(self, prec=..., name: str = 'z'):
        """
        Return the logarithm of the given Drinfeld module.

        By definition, the logarithm is the compositional inverse of the
        exponential (see :meth:`exponential`). Note that the logarithm
        is only defined when the `\\mathbb{F}_q[T]`-characteristic is
        zero.

        INPUT:

        - ``prec`` -- an integer or ``Infinity`` (default: ``Infinity``);
          the precision at which the series is returned; if ``Infinity``,
          a lazy power series in returned

        - ``name`` -- string (default: ``'z'``); the name of the
          generator of the lazy power series ring

        EXAMPLES::

            sage: A = GF(2)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, 1])

        When ``prec`` is ``Infinity`` (which is the default),
        the logarithm is returned as a lazy power series, meaning
        that any of its coefficients can be computed on demands::

            sage: log = phi.logarithm(); log
            z + ((1/(T^2+T))*z^2) + ((1/(T^6+T^5+T^3+T^2))*z^4) + O(z^8)
            sage: log[2^4]
            1/(T^30 + T^29 + T^27 + ... + T^7 + T^5 + T^4)
            sage: log[2^5]
            1/(T^62 + T^61 + T^59 + ... + T^8 + T^6 + T^5)

        If ``prec`` is a finite number, all the
        required coefficients are computed at once::

            sage: phi.logarithm(prec=10)
            z + (1/(T^2 + T))*z^2 + (1/(T^6 + T^5 + T^3 + T^2))*z^4 + (1/(T^14 + T^13 + T^11 + T^10 + T^7 + T^6 + T^4 + T^3))*z^8 + O(z^10)

        Example in higher rank::

            sage: A = GF(5)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, T^2, T + T^2 + T^4, 1])
            sage: phi.logarithm()
            z + ((4*T/(T^4+4))*z^5) + O(z^8)

        TESTS::

            sage: A = GF(2)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, 1])
            sage: q = 2
            sage: log[2] == -1/((T**q - T))  # expected value
            True
            sage: log[2**2] == 1/((T**q - T)*(T**(q**2) - T))  # expected value
            True
            sage: log[2**3] == -1/((T**q - T)*(T**(q**2) - T)*(T**(q**3) - T))  # expected value
            True
        """
    def goss_polynomial(self, n, var: str = 'X'):
        """
        Return the `n`-th Goss polynomial of the Drinfeld module.

        Note that Goss polynomials are only defined for Drinfeld modules
        of characteristic zero.

        INPUT:

        - ``n`` -- integer; the index of the Goss polynomial

        - ``var``-- string (default: ``'X'``); the name of polynomial
          variable

        OUTPUT: a univariate polynomial in ``var`` over the base `A`-field

        EXAMPLES::

            sage: A = GF(3)['T']
            sage: K.<T> = Frac(A)
            sage: phi = DrinfeldModule(A, [T, 1])  # Carlitz module
            sage: phi.goss_polynomial(1)
            X
            sage: phi.goss_polynomial(2)
            X^2
            sage: phi.goss_polynomial(4)
            X^4 + (1/(T^3 + 2*T))*X^2
            sage: phi.goss_polynomial(5)
            X^5 + (2/(T^3 + 2*T))*X^3
            sage: phi.goss_polynomial(10)
            X^10 + (1/(T^3 + 2*T))*X^8 + (1/(T^6 + T^4 + T^2))*X^6 + (1/(T^9 + 2*T^3))*X^4 + (1/(T^18 + 2*T^12 + 2*T^10 + T^4))*X^2

        REFERENCE:

        Section 3 of [Gek1988]_ provides an exposition of Goss
        polynomials.
        """

class DrinfeldModule_rational(DrinfeldModule_charzero):
    """
    A class for Drinfeld modules defined over the fraction
    field of the underlying function field.

    TESTS::

        sage: q = 9
        sage: Fq = GF(q)
        sage: A = Fq['T']
        sage: K.<T> = Frac(A)
        sage: C = DrinfeldModule(A, [T, 1]); C
        Drinfeld module defined by T |--> t + T
        sage: type(C)
        <class 'sage.rings.function_field.drinfeld_modules.charzero_drinfeld_module.DrinfeldModule_rational_with_category'>
    """
    def coefficient_in_function_ring(self, n):
        """
        Return the `n`-th coefficient of this Drinfeld module as
        an element of the underlying function ring.

        INPUT:

        - ``n`` -- an integer

        EXAMPLES::

            sage: q = 5
            sage: Fq = GF(q)
            sage: A = Fq['T']
            sage: R = Fq['U']
            sage: K.<U> = Frac(R)
            sage: phi = DrinfeldModule(A, [U, 0, U^2, U^3])
            sage: phi.coefficient_in_function_ring(2)
            T^2

        Compare with the method meth:`coefficient`::

            sage: phi.coefficient(2)
            U^2

        If the required coefficient is not a polynomials,
        an error is raised::

            sage: psi = DrinfeldModule(A, [U, 1/U])
            sage: psi.coefficient_in_function_ring(0)
            T
            sage: psi.coefficient_in_function_ring(1)
            Traceback (most recent call last):
            ...
            ValueError: coefficient is not polynomial
        """
    def coefficients_in_function_ring(self, sparse: bool = True):
        """
        Return the coefficients of this Drinfeld module as elements
        of the underlying function ring.

        INPUT:

        - ``sparse`` -- a boolean (default: ``True``); if ``True``,
          only return the nonzero coefficients; otherwise, return
          all of them.

        EXAMPLES::

            sage: q = 5
            sage: Fq = GF(q)
            sage: A = Fq['T']
            sage: R = Fq['U']
            sage: K.<U> = Frac(R)
            sage: phi = DrinfeldModule(A, [U, 0, U^2, U^3])
            sage: phi.coefficients_in_function_ring()
            [T, T^2, T^3]
            sage: phi.coefficients_in_function_ring(sparse=False)
            [T, 0, T^2, T^3]

        Compare with the method meth:`coefficients`::

            sage: phi.coefficients()
            [U, U^2, U^3]

        If the coefficients are not polynomials, an error is raised::

            sage: psi = DrinfeldModule(A, [U, 1/U])
            sage: psi.coefficients_in_function_ring()
            Traceback (most recent call last):
            ...
            ValueError: coefficients are not polynomials
        """
    def class_polynomial(self):
        """
        Return the class polynomial, that is the Fitting ideal
        of the class module, of this Drinfeld module.

        We refer to [Tae2012]_ for the definition and basic
        properties of the class module.

        EXAMPLES:

        We check that the class module of the Carlitz module
        is trivial::

            sage: q = 5
            sage: Fq = GF(q)
            sage: A = Fq['T']
            sage: K.<T> = Frac(A)
            sage: C = DrinfeldModule(A, [T, 1]); C
            Drinfeld module defined by T |--> t + T
            sage: C.class_polynomial()
            1

        When the coefficients of the Drinfeld module have small
        enough degrees, the class module is always trivial::

            sage: gs = [T] + [A.random_element(degree = q^i)
            ....:             for i in range(1, 5)]
            sage: phi = DrinfeldModule(A, gs)
            sage: phi.class_polynomial()
            1

        Here is an example with a nontrivial class module::

            sage: phi = DrinfeldModule(A, [T, 2*T^14 + 2*T^4])
            sage: phi.class_polynomial()
            T + 3

        TESTS:

        The Drinfeld module must have polynomial coefficients::

            sage: phi = DrinfeldModule(A, [T, 1/T])
            sage: phi.class_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: coefficients are not polynomials
        """
