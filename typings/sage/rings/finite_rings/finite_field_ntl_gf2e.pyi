from sage.libs.pari import pari as pari
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer

def late_import() -> None:
    """
    Imports various modules after startup.

    EXAMPLES::

       sage: sage.rings.finite_rings.finite_field_ntl_gf2e.late_import()
       sage: sage.rings.finite_rings.finite_field_ntl_gf2e.GF2 is None # indirect doctest
       False
    """

class FiniteField_ntl_gf2e(FiniteField):
    """
    Finite Field of characteristic 2 and order `2^n`.

    INPUT:

    - ``q`` -- `2^n` (must be 2 power)

    - ``names`` -- variable used for poly_repr (default: ``'a'``)

    - ``modulus`` -- a minimal polynomial to use for reduction

    - ``repr`` -- controls the way elements are printed to the user:
                 (default: ``'poly'``)

      - ``'poly'`` -- polynomial representation

    OUTPUT: finite field with characteristic 2 and cardinality `2^n`

    EXAMPLES::

        sage: k.<a> = GF(2^16)
        sage: type(k)
        <class 'sage.rings.finite_rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e_with_category'>
        sage: k.<a> = GF(2^1024)
        sage: k.modulus()
        x^1024 + x^19 + x^6 + x + 1
        sage: set_random_seed(6397)
        sage: k.<a> = GF(2^17, modulus='random')
        sage: k.modulus()
        x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
        sage: k.modulus().is_irreducible()
        True
        sage: k.<a> = GF(2^211, modulus='minimal_weight')
        sage: k.modulus()
        x^211 + x^11 + x^10 + x^8 + 1
        sage: k.<a> = GF(2^211, modulus='conway')
        sage: k.modulus()
        x^211 + x^9 + x^6 + x^5 + x^3 + x + 1
        sage: k.<a> = GF(2^23, modulus='conway')
        sage: a.multiplicative_order() == k.order() - 1
        True
    """
    def __init__(self, q, names: str = 'a', modulus=None, repr: str = 'poly') -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: k.<a> = GF(2^100, modulus='strangeinput')
            Traceback (most recent call last):
            ...
            ValueError: no such algorithm for finding an irreducible polynomial: strangeinput
            sage: k.<a> = GF(2^20) ; type(k)
            <class 'sage.rings.finite_rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e_with_category'>
            sage: loads(dumps(k)) is k
            True
            sage: k1.<a> = GF(2^16)
            sage: k2.<a> = GF(2^17)
            sage: k1 == k2
            False
            sage: k3.<a> = GF(2^16, impl='pari_ffelt')
            sage: k1 == k3
            False

            sage: TestSuite(k).run()

            sage: k.<a> = GF(2^64)
            sage: k._repr_option('element_is_atomic')
            False
            sage: P.<x> = PolynomialRing(k)
            sage: (a+1)*x # indirect doctest
            (a + 1)*x
        """
    def characteristic(self):
        """
        Return the characteristic of ``self`` which is 2.

        EXAMPLES::

            sage: k.<a> = GF(2^16,modulus='random')
            sage: k.characteristic()
            2
        """
    def order(self):
        """
        Return the cardinality of this field.

        EXAMPLES::

            sage: k.<a> = GF(2^64)
            sage: k.order()
            18446744073709551616
        """
    def degree(self):
        """
        If this field has cardinality `2^n` this method returns `n`.

        EXAMPLES::

            sage: k.<a> = GF(2^64)
            sage: k.degree()
            64
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

            sage: k.<a> = GF(2^19)
            sage: k.gen() == a
            True
            sage: a
            a

        TESTS::

            sage: GF(2, impl=\'ntl\').gen()
            1
            sage: GF(2, impl=\'ntl\', modulus=polygen(GF(2)) ).gen()
            0
            sage: GF(2^19, \'a\').gen(1)
            Traceback (most recent call last):
            ...
            IndexError: only one generator
        '''
    def prime_subfield(self):
        """
        Return the prime subfield `\\GF{p}` of ``self`` if ``self`` is
        `\\GF{p^n}`.

        EXAMPLES::

            sage: F.<a> = GF(2^16)
            sage: F.prime_subfield()
            Finite Field of size 2
        """
    def from_integer(self, number):
        """
        Given an integer `n` less than :meth:`cardinality` with base `2`
        representation `a_0 + 2 \\cdot a_1 + \\cdots + 2^k a_k`, returns
        `a_0 + a_1 \\cdot x + \\cdots + a_k x^k`, where `x` is the
        generator of this finite field.

        INPUT:

        - ``number`` -- integer

        EXAMPLES::

            sage: k.<a> = GF(2^48)
            sage: k.from_integer(2^43 + 2^15 + 1)
            a^43 + a^15 + 1
            sage: k.from_integer(33793)
            a^15 + a^10 + 1
            sage: 33793.digits(2) # little endian
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
        """
