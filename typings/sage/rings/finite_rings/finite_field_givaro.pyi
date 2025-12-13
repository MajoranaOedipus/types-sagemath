from sage.libs.pari import pari as pari
from sage.rings.finite_rings.element_givaro import Cache_givaro as Cache_givaro
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer

class FiniteField_givaro(FiniteField):
    """
    Finite field implemented using Zech logs and the cardinality must be
    less than `2^{16}`. By default, Conway polynomials are used as minimal
    polynomials.

    INPUT:

    - ``q`` -- `p^n` (must be prime power)

    - ``name`` -- (default: ``'a'``) variable used for
      :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.poly_repr()`

    - ``modulus`` -- a minimal polynomial to use for reduction

    - ``repr`` -- (default: ``'poly'``) controls the way elements are printed
      to the user:

      - 'log': repr is
        :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.log_repr()`
      - 'int': repr is
        :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.int_repr()`
      - 'poly': repr is
        :meth:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement.poly_repr()`

    - ``cache`` -- boolean (default: ``False``); if ``True`` a cache of all
      elements of this field is created. Thus, arithmetic does not create new
      elements which speeds calculations up. Also, if many elements are needed
      during a calculation this cache reduces the memory requirement as at most
      :meth:`order` elements are created.

    OUTPUT: Givaro finite field with characteristic `p` and cardinality `p^n`

    EXAMPLES:

    By default, Conway polynomials are used for extension fields::

        sage: k.<a> = GF(2**8)
        sage: -a ^ k.degree()
        a^4 + a^3 + a^2 + 1
        sage: f = k.modulus(); f
        x^8 + x^4 + x^3 + x^2 + 1

    You may enforce a modulus::

        sage: P.<x> = PolynomialRing(GF(2))
        sage: f = x^8 + x^4 + x^3 + x + 1 # Rijndael Polynomial
        sage: k.<a> = GF(2^8, modulus=f)
        sage: k.modulus()
        x^8 + x^4 + x^3 + x + 1
        sage: a^(2^8)
        a

    You may enforce a random modulus::

        sage: k = GF(3**5, 'a', modulus='random')
        sage: k.modulus() # random polynomial
        x^5 + 2*x^4 + 2*x^3 + x^2 + 2

    Three different representations are possible::

        sage: FiniteField(9, 'a', impl='givaro', repr='poly').gen()
        a
        sage: FiniteField(9, 'a', impl='givaro', repr='int').gen()
        3
        sage: FiniteField(9, 'a', impl='givaro', repr='log').gen()
        1

    For prime fields, the default modulus is the polynomial `x - 1`,
    but you can ask for a different modulus::

        sage: GF(1009, impl='givaro').modulus()
        x + 1008
        sage: GF(1009, impl='givaro', modulus='conway').modulus()
        x + 998
    """
    def __init__(self, q, name: str = 'a', modulus=None, repr: str = 'poly', cache: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: k.<a> = GF(2^3)
            sage: j.<b> = GF(3^4)
            sage: k == j
            False

            sage: GF(2^3,'a') == copy(GF(2^3,'a'))
            True
            sage: TestSuite(GF(2^3, 'a')).run()
        """
    def characteristic(self):
        """
        Return the characteristic of this field.

        EXAMPLES::

            sage: p = GF(19^5,'a').characteristic(); p
            19
            sage: type(p)
            <class 'sage.rings.integer.Integer'>
        """
    def order(self):
        """
        Return the cardinality of this field.

        OUTPUT: integer; the number of elements in ``self``

        EXAMPLES::

            sage: n = GF(19^5,'a').order(); n
            2476099
            sage: type(n)
            <class 'sage.rings.integer.Integer'>
        """
    def degree(self):
        """
        If the cardinality of ``self`` is `p^n`, then this returns `n`.

        OUTPUT: integer; the degree

        EXAMPLES::

            sage: GF(3^4,'a').degree()
            4
        """
    def random_element(self, *args, **kwds):
        """
        Return a random element of ``self``.

        EXAMPLES::

            sage: k = GF(23**3, 'a')
            sage: e = k.random_element()
            sage: e.parent() is k
            True
            sage: type(e)
            <class 'sage.rings.finite_rings.element_givaro.FiniteField_givaroElement'>

            sage: P.<x> = PowerSeriesRing(GF(3^3, 'a'))
            sage: P.random_element(5).parent() is P
            True
        """
    def gen(self, n: int = 0):
        '''
        Return a generator of ``self`` over its prime field, which is a
        root of ``self.modulus()``.

        INPUT:

        - ``n`` -- must be 0

        OUTPUT:

        An element `a` of ``self`` such that ``self.modulus()(a) == 0``.

        .. WARNING::

            This generator is not guaranteed to be a generator for the
            multiplicative group.  To obtain the latter, use
            :meth:`~sage.rings.finite_rings.finite_field_base.FiniteFields.multiplicative_generator()`
            or use the ``modulus="primitive"`` option when constructing
            the field.

        EXAMPLES::

            sage: k = GF(3^4, \'b\'); k.gen()
            b
            sage: k.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: only one generator
            sage: F = FiniteField(31, impl=\'givaro\')
            sage: F.gen()
            1
        '''
    def prime_subfield(self):
        """
        Return the prime subfield `\\GF{p}` of ``self`` if ``self`` is `\\GF{p^n}`.

        EXAMPLES::

            sage: GF(3^4, 'b').prime_subfield()
            Finite Field of size 3

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: S.prime_subfield()
            Finite Field of size 5
            sage: type(S.prime_subfield())
            <class 'sage.rings.finite_rings.finite_field_prime_modn.FiniteField_prime_modn_with_category'>
        """
    def log_to_int(self, n):
        """
        Given an integer `n` this method returns ``i`` where ``i``
        satisfies `g^n = i` where `g` is the generator of ``self``; the
        result is interpreted as an integer.

        INPUT:

        - ``n`` -- log representation of a finite field element

        OUTPUT: integer representation of a finite field element

        EXAMPLES::

            sage: k = GF(2**8, 'a')
            sage: k.log_to_int(4)
            16
            sage: k.log_to_int(20)
            180
        """
    def int_to_log(self, n):
        """
        Given an integer `n` this method returns `i` where `i` satisfies
        `g^i = n \\mod p` where `g` is the generator and `p` is the
        characteristic of ``self``.

        INPUT:

        - ``n`` -- integer representation of a finite field element

        OUTPUT: log representation of ``n``

        EXAMPLES::

            sage: k = GF(7**3, 'a')
            sage: k.int_to_log(4)
            228
            sage: k.int_to_log(3)
            57
            sage: k.gen()^57
            3
        """
    def from_integer(self, n):
        """
        Given an integer `n` return a finite field element in ``self``
        which equals `n` under the condition that :meth:`gen()` is set to
        :meth:`characteristic()`.

        EXAMPLES::

            sage: k.<a> = GF(2^8)
            sage: k.from_integer(8)
            a^3
            sage: e = k.from_integer(151); e
            a^7 + a^4 + a^2 + a + 1
            sage: 2^7 + 2^4 + 2^2 + 2 + 1
            151
        """
    def __iter__(self):
        """
        Finite fields may be iterated over.

        EXAMPLES::

            sage: list(GF(2**2, 'a'))
            [0, a, a + 1, 1]
        """
    def a_times_b_plus_c(self, a, b, c):
        """
        Return ``a*b + c``. This is faster than multiplying ``a`` and ``b``
        first and adding ``c`` to the result.

        INPUT:

        - ``a``, ``b``, ``c`` -- :class:`~~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement`

        EXAMPLES::

            sage: k.<a> = GF(2**8)
            sage: k.a_times_b_plus_c(a,a,k(1))
            a^2 + 1
        """
    def a_times_b_minus_c(self, a, b, c):
        """
        Return ``a*b - c``.

        INPUT:

        - ``a``, ``b``, ``c`` -- :class:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement`

        EXAMPLES::

            sage: k.<a> = GF(3**3)
            sage: k.a_times_b_minus_c(a,a,k(1))
            a^2 + 2
        """
    def c_minus_a_times_b(self, a, b, c):
        """
        Return ``c - a*b``.

        INPUT:

        - ``a``, ``b``, ``c`` -- :class:`~sage.rings.finite_rings.element_givaro.FiniteField_givaroElement`

        EXAMPLES::

            sage: k.<a> = GF(3**3)
            sage: k.c_minus_a_times_b(a,a,k(1))
            2*a^2 + 1
        """
    def frobenius_endomorphism(self, n: int = 1):
        """
        INPUT:

        - ``n`` -- integer (default: 1)

        OUTPUT:

        The `n`-th power of the absolute arithmetic Frobenius
        endomorphism on this finite field.

        EXAMPLES::

            sage: k.<t> = GF(3^5)
            sage: Frob = k.frobenius_endomorphism(); Frob
            Frobenius endomorphism t |--> t^3 on Finite Field in t of size 3^5

            sage: a = k.random_element()
            sage: Frob(a) == a^3
            True

        We can specify a power::

            sage: k.frobenius_endomorphism(2)
            Frobenius endomorphism t |--> t^(3^2) on Finite Field in t of size 3^5

        The result is simplified if possible::

            sage: k.frobenius_endomorphism(6)
            Frobenius endomorphism t |--> t^3 on Finite Field in t of size 3^5
            sage: k.frobenius_endomorphism(5)
            Identity endomorphism of Finite Field in t of size 3^5

        Comparisons work::

            sage: k.frobenius_endomorphism(6) == Frob
            True
            sage: from sage.categories.morphism import IdentityMorphism
            sage: k.frobenius_endomorphism(5) == IdentityMorphism(k)
            True

        AUTHOR:

        - Xavier Caruso (2012-06-29)
        """
