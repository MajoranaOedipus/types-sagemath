import sage.rings.finite_rings.integer_mod_ring as integer_mod_ring
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField_generic
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic as IntegerModRing_generic
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class FiniteField_prime_modn(FiniteField_generic, integer_mod_ring.IntegerModRing_generic):
    """
    Finite field of order `p` where `p` is prime.

    EXAMPLES::

        sage: FiniteField(3)
        Finite Field of size 3

        sage: FiniteField(next_prime(1000))                                             # needs sage.rings.finite_rings
        Finite Field of size 1009
    """
    def __init__(self, p, check: bool = True, modulus=None) -> None:
        """
        Return a new finite field of order `p` where `p` is prime.

        INPUT:

        - ``p`` -- integer at least 2

        - ``check`` -- boolean (default: ``True``); if ``False``, do not
          check ``p`` for primality

        EXAMPLES::

            sage: F = FiniteField(3); F
            Finite Field of size 3
        """
    def __reduce__(self):
        """
        For pickling.

        EXAMPLES::

            sage: k = FiniteField(5); type(k)
            <class 'sage.rings.finite_rings.finite_field_prime_modn.FiniteField_prime_modn_with_category'>
            sage: k is loads(dumps(k))
            True
        """
    def construction(self):
        """
        Return the construction of this finite field (for use by
        ``sage.categories.pushout``).

        EXAMPLES::

            sage: GF(3).construction()
            (QuotientFunctor, Integer Ring)
        """
    def characteristic(self):
        """
        Return the characteristic of \\code{self}.

        EXAMPLES::

            sage: k = GF(7)
            sage: k.characteristic()
            7
        """
    def is_prime_field(self):
        """
        Return ``True`` since this is a prime field.

        EXAMPLES::

            sage: k.<a> = GF(3)
            sage: k.is_prime_field()
            True

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(3^2)
            sage: k.is_prime_field()
            False
        """
    def polynomial(self, name=None):
        """
        Return the polynomial ``name``.

        EXAMPLES::

            sage: k.<a> = GF(3)
            sage: k.polynomial()
            x
        """
    def order(self):
        """
        Return the order of this finite field.

        EXAMPLES::

            sage: k = GF(5)
            sage: k.order()
            5
        """
    def gen(self, n: int = 0):
        '''
        Return a generator of ``self`` over its prime field, which is a
        root of ``self.modulus()``.

        Unless a custom modulus was given when constructing this prime
        field, this returns `1`.

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

            sage: k = GF(13)
            sage: k.gen()
            1

            sage: # needs sage.rings.finite_rings
            sage: k = GF(1009, modulus=\'primitive\')
            sage: k.gen()  # this gives a primitive element
            11
            sage: k.gen(1)
            Traceback (most recent call last):
            ...
            IndexError: only one generator
        '''
    def gens(self) -> tuple:
        '''
        Return a tuple containing the generator of ``self``.

        .. WARNING::

            The generator is not guaranteed to be a generator for the
            multiplicative group.  To obtain the latter, use
            :meth:`~sage.rings.finite_rings.finite_field_base.FiniteFields.multiplicative_generator()`
            or use the ``modulus="primitive"`` option when constructing
            the field.

        EXAMPLES::

            sage: k = GF(1009, modulus=\'primitive\')
            sage: k.gens()
            (11,)

            sage: k = GF(1009)
            sage: k.gens()
            (1,)
        '''
    def __iter__(self):
        """
        Return an iterator over ``self``.

        EXAMPLES::

            sage: list(GF(7))
            [0, 1, 2, 3, 4, 5, 6]

        We can even start iterating over something that would be too big
        to actually enumerate::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(next_prime(2^256))
            sage: all = iter(K)
            sage: next(all)
            0
            sage: next(all)
            1
            sage: next(all)
            2
        """
    def degree(self):
        """
        Return the degree of ``self`` over its prime field.

        This always returns 1.

        EXAMPLES::

            sage: FiniteField(3).degree()
            1
        """
