r"""
Ring `\ZZ/n\ZZ` of integers modulo `n`

EXAMPLES::

    sage: R = Integers(97)
    sage: a = R(5)
    sage: a**100000000000000000000000000000000000000000000000000000000000000
    61

This example illustrates the relation between
`\ZZ/p\ZZ` and `\GF{p}`. In
particular, there is a canonical map to `\GF{p}`, but not in
the other direction.

::

    sage: r = Integers(7)
    sage: s = GF(7)
    sage: r.has_coerce_map_from(s)
    False
    sage: s.has_coerce_map_from(r)
    True
    sage: s(1) + r(1)
    2
    sage: parent(s(1) + r(1))
    Finite Field of size 7
    sage: parent(r(1) + s(1))
    Finite Field of size 7

We list the elements of `\ZZ/3\ZZ`::

    sage: R = Integers(3)
    sage: list(R)
    [0, 1, 2]

AUTHORS:

- William Stein (initial code)

- David Joyner (2005-12-22): most examples

- Robert Bradshaw (2006-08-24): convert to SageX (Cython)

- William Stein (2007-04-29): square_roots_of_one

- Simon King (2011-04-21): allow to prescribe a category

- Simon King (2013-09): Only allow to prescribe the category of fields

- Kyle Hofmann (2024-02): New implementation of root-finding
"""
import sage.rings.abc
import sage.rings.quotient_ring as quotient_ring
from _typeshed import Incomplete
from sage.arith.misc import CRT_basis as CRT_basis, factor as factor, primitive_root as primitive_root
from sage.categories.category import JoinCategory as JoinCategory
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.noetherian_rings import NoetherianRings as NoetherianRings
from sage.interfaces.abc import GapElement as GapElement
from sage.libs.pari import pari as pari
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.mrange import cartesian_product_iterator as cartesian_product_iterator
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings import integer_mod as integer_mod
from sage.rings.ring import Field as Field
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

class PariError(Exception): ...

class IntegerModFactory(UniqueFactory):
    """
    Return the quotient ring `\\ZZ / n\\ZZ`.

    INPUT:

    - ``order`` -- integer (default: 0); positive or negative
    - ``is_field`` -- boolean (default: ``False``); assert that the order is
      prime and hence the quotient ring belongs to the category of fields
    - ``category`` -- (optional) the category that the quotient ring belongs to

    .. NOTE::

        The optional argument ``is_field`` is not part of the cache key.
        Hence, this factory will create precisely one instance of `\\ZZ /
        n\\ZZ`.  However, if ``is_field`` is true, then a previously created
        instance of the quotient ring will be updated to be in the category of
        fields.

        **Use with care!** Erroneously putting `\\ZZ / n\\ZZ` into the category
        of fields may have consequences that can compromise a whole Sage
        session, so that a restart will be needed.

    EXAMPLES::

        sage: IntegerModRing(15)
        Ring of integers modulo 15
        sage: IntegerModRing(7)
        Ring of integers modulo 7
        sage: IntegerModRing(-100)
        Ring of integers modulo 100

    Note that you can also use ``Integers``, which is a
    synonym for ``IntegerModRing``.

    ::

        sage: Integers(18)
        Ring of integers modulo 18
        sage: Integers() is Integers(0) is ZZ
        True

    .. NOTE::

        Testing whether a quotient ring `\\ZZ / n\\ZZ` is a field can of
        course be very costly. By default, it is not tested whether `n`
        is prime or not, in contrast to
        :func:`~sage.rings.finite_rings.finite_field_constructor.GF`. If the user
        is sure that the modulus is prime and wants to avoid a primality
        test, (s)he can provide ``category=Fields()`` when constructing
        the quotient ring, and then the result will behave like a field.
        If the category is not provided during initialisation, and it is
        found out later that the ring is in fact a field, then the category
        will be changed at runtime, having the same effect as providing
        ``Fields()`` during initialisation.

    EXAMPLES::

        sage: R = IntegerModRing(5)
        sage: R.category()
        Join of Category of finite commutative rings
            and Category of subquotients of monoids
            and Category of quotients of semigroups
            and Category of finite enumerated sets
        sage: R in Fields()
        True
        sage: R.category()
        Join of Category of finite enumerated fields
            and Category of subquotients of monoids
            and Category of quotients of semigroups
        sage: S = IntegerModRing(5, is_field=True)
        sage: S is R
        True

    .. WARNING::

        If the optional argument ``is_field`` was used by mistake, there is
        currently no way to revert its impact, even though
        :meth:`IntegerModRing_generic.is_field` with the optional argument
        ``proof=True`` would return the correct answer.  So, prescribe
        ``is_field=True`` only if you know what your are doing!

    EXAMPLES::

        sage: R = IntegerModRing(33, is_field=True)
        sage: R in Fields()
        True
        sage: R.is_field()
        True

    If the optional argument `proof=True` is provided, primality is tested and
    the mistaken category assignment is reported::

        sage: R.is_field(proof=True)
        Traceback (most recent call last):
        ...
        ValueError: THIS SAGE SESSION MIGHT BE SERIOUSLY COMPROMISED!
        The order 33 is not prime, but this ring has been put
        into the category of fields. This may already have consequences
        in other parts of Sage. Either it was a mistake of the user,
        or a probabilistic primality test has failed.
        In the latter case, please inform the developers.

    However, the mistaken assignment is not automatically corrected::

        sage: R in Fields()
        True

    To avoid side-effects of this test on other tests, we clear the cache of
    the ring factory::

        sage: IntegerModRing._cache.clear()
    """
    def get_object(self, version, key, extra_args): ...
    def create_key_and_extra_args(self, order: int = 0, is_field: bool = False, category=None):
        """
        An integer mod ring is specified uniquely by its order.

        EXAMPLES::

            sage: Zmod.create_key_and_extra_args(7)
            (7, {})
            sage: Zmod.create_key_and_extra_args(7, True)
            (7, {'category': Category of fields})
        """
    def create_object(self, version, order, **kwds):
        """
        EXAMPLES::

            sage: R = Integers(10)
            sage: TestSuite(R).run() # indirect doctest
        """

Zmod: IntegerModFactory

Integers: IntegerModFactory

IntegerModRing: IntegerModFactory
default_category: Incomplete
ZZ: Incomplete

class IntegerModRing_generic(quotient_ring.QuotientRing_generic, sage.rings.abc.IntegerModRing):
    """
    The ring of integers modulo `N`.

    INPUT:

    - ``order`` -- integer

    - ``category`` -- a subcategory of ``CommutativeRings()`` (the default)

    OUTPUT: the ring of integers modulo `N`

    EXAMPLES:

    First we compute with integers modulo `29`.

    ::

        sage: FF = IntegerModRing(29)
        sage: FF
        Ring of integers modulo 29
        sage: FF.category()
        Join of Category of finite commutative rings
            and Category of subquotients of monoids
            and Category of quotients of semigroups
            and Category of finite enumerated sets
        sage: FF.is_field()
        True
        sage: FF.characteristic()
        29
        sage: FF.order()
        29

        sage: # needs sage.groups
        sage: gens = FF.unit_gens()
        sage: a = gens[0]
        sage: a
        2
        sage: a.is_square()
        False
        sage: def pow(i): return a**i
        sage: [pow(i) for i in range(16)]
        [1, 2, 4, 8, 16, 3, 6, 12, 24, 19, 9, 18, 7, 14, 28, 27]
        sage: TestSuite(FF).run()

    We have seen above that an integer mod ring is, by default, not
    initialised as an object in the category of fields. However, one
    can force it to be. Moreover, testing containment in the category
    of fields my re-initialise the category of the integer mod ring::

        sage: F19 = IntegerModRing(19, is_field=True)
        sage: F19.category().is_subcategory(Fields())
        True
        sage: F23 = IntegerModRing(23)
        sage: F23.category().is_subcategory(Fields())
        False
        sage: F23 in Fields()
        True
        sage: F23.category().is_subcategory(Fields())
        True
        sage: TestSuite(F19).run()
        sage: TestSuite(F23).run()

    By :issue:`15229`, there is a unique instance of the
    integral quotient ring of a given order. Using the
    :func:`IntegerModRing` factory twice, and using
    ``is_field=True`` the second time, will update the
    category of the unique instance::

        sage: F31a = IntegerModRing(31)
        sage: F31a.category().is_subcategory(Fields())
        False
        sage: F31b = IntegerModRing(31, is_field=True)
        sage: F31a is F31b
        True
        sage: F31a.category().is_subcategory(Fields())
        True

    Next we compute with the integers modulo `16`.

    ::

        sage: Z16 = IntegerModRing(16)
        sage: Z16.category()
        Join of Category of finite commutative rings
            and Category of subquotients of monoids
            and Category of quotients of semigroups
            and Category of finite enumerated sets
        sage: Z16.is_field()
        False
        sage: Z16.order()
        16
        sage: Z16.characteristic()
        16

        sage: # needs sage.groups
        sage: gens = Z16.unit_gens()
        sage: gens
        (15, 5)
        sage: a = gens[0]
        sage: b = gens[1]
        sage: def powa(i): return a**i
        sage: def powb(i): return b**i
        sage: gp_exp = FF.unit_group_exponent()
        sage: gp_exp
        28
        sage: [powa(i) for i in range(15)]
        [1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1]
        sage: [powb(i) for i in range(15)]
        [1, 5, 9, 13, 1, 5, 9, 13, 1, 5, 9, 13, 1, 5, 9]
        sage: a.multiplicative_order()
        2
        sage: b.multiplicative_order()
        4

        sage: TestSuite(Z16).run()

    Saving and loading::

        sage: R = Integers(100000)
        sage: TestSuite(R).run()  # long time (17s on sage.math, 2011)

    Testing ideals and quotients::

        sage: Z10 = Integers(10)
        sage: I = Z10.principal_ideal(0)
        sage: Z10.quotient(I) == Z10
        True
        sage: I = Z10.principal_ideal(2)
        sage: Z10.quotient(I) == Z10
        False
        sage: I.is_prime()
        True

    ::

        sage: R = IntegerModRing(97)
        sage: a = R(5)
        sage: a**(10^62)
        61
    """
    def __init__(self, order, cache=None, category=None) -> None:
        """
        Create with the command ``IntegerModRing(order)``.

        TESTS::

            sage: FF = IntegerModRing(29)
            sage: TestSuite(FF).run()
            sage: F19 = IntegerModRing(19, is_field=True)
            sage: TestSuite(F19).run()
            sage: F23 = IntegerModRing(23)
            sage: F23 in Fields()
            True
            sage: TestSuite(F23).run()
            sage: Z16 = IntegerModRing(16)
            sage: TestSuite(Z16).run()
            sage: R = Integers(100000)
            sage: TestSuite(R).run()  # long time (17s on sage.math, 2011)

            sage: R = IntegerModRing(18)
            sage: R.is_finite()
            True

        TESTS::

            sage: Integers(8).is_noetherian()
            True
        """
    def krull_dimension(self):
        """
        Return the Krull dimension of ``self``.

        EXAMPLES::

            sage: Integers(18).krull_dimension()
            0
        """
    def extension(self, poly, name=None, names=None, **kwds):
        """
        Return an algebraic extension of ``self``. See
        :meth:`sage.rings.ring.CommutativeRing.extension()` for more
        information.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: Integers(8).extension(t^2 - 3)
            Univariate Quotient Polynomial Ring in t
             over Ring of integers modulo 8 with modulus t^2 + 5
        """
    @cached_method
    def is_prime_field(self) -> bool:
        """
        Return ``True`` if the order is prime.

        EXAMPLES::

            sage: Zmod(7).is_prime_field()
            True
            sage: Zmod(8).is_prime_field()
            False
        """
    def list_of_elements_of_multiplicative_group(self) -> list:
        """
        Return a list of all invertible elements, as python ints.

        EXAMPLES::

            sage: R = Zmod(12)
            sage: L = R.list_of_elements_of_multiplicative_group(); L
            [1, 5, 7, 11]
            sage: type(L[0])
            <... 'int'>
            sage: Zmod(1).list_of_elements_of_multiplicative_group()
            [0]
        """
    @cached_method
    def multiplicative_subgroups(self):
        """
        Return generators for each subgroup of `(\\ZZ/N\\ZZ)^*`.

        EXAMPLES::

            sage: # optional - gap_package_polycyclic, needs sage.groups
            sage: Integers(5).multiplicative_subgroups()
            ((2,), (4,), ())
            sage: Integers(15).multiplicative_subgroups()
            ((11, 7), (11, 4), (2,), (11,), (14,), (7,), (4,), ())
            sage: Integers(2).multiplicative_subgroups()
            ((),)
            sage: len(Integers(341).multiplicative_subgroups())
            80

        TESTS::

            sage: IntegerModRing(1).multiplicative_subgroups()                          # needs sage.groups
            ((),)
            sage: IntegerModRing(2).multiplicative_subgroups()                          # needs sage.groups
            ((),)
            sage: IntegerModRing(3).multiplicative_subgroups()  # optional - gap_package_polycyclic, needs sage.groups
            ((2,), ())
        """
    def is_integral_domain(self, proof=None):
        """
        Return ``True`` if and only if the order of ``self`` is prime.

        EXAMPLES::

            sage: Integers(389).is_integral_domain()
            True
            sage: Integers(389^2).is_integral_domain()                                  # needs sage.libs.pari
            False

        TESTS:

        Check that :issue:`17453` is fixed::

            sage: R = Zmod(5)
            sage: R in IntegralDomains()
            True
        """
    def is_unique_factorization_domain(self, proof=None):
        """
        Return ``True`` if and only if the order of ``self`` is prime.

        EXAMPLES::

            sage: Integers(389).is_unique_factorization_domain()
            True
            sage: Integers(389^2).is_unique_factorization_domain()                      # needs sage.libs.pari
            False
        """
    @cached_method
    def is_field(self, proof=None):
        """
        Return ``True`` precisely if the order is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, then test
          whether the category of the quotient is a subcategory of
          ``Fields()``, or do a probabilistic primality test. If ``None``, then
          test the category and then do a primality test according to the
          global arithmetic proof settings. If ``True``, do a deterministic
          primality test.

        If it is found (perhaps probabilistically) that the ring is a field,
        then the category of the ring is refined to include the category
        of fields. This may change the Python class of the ring!

        EXAMPLES::

            sage: R = IntegerModRing(18)
            sage: R.is_field()
            False
            sage: FF = IntegerModRing(17)
            sage: FF.is_field()
            True

        By :issue:`15229`, the category of the ring is refined,
        if it is found that the ring is in fact a field::

            sage: R = IntegerModRing(127)
            sage: R.category()
            Join of Category of finite commutative rings
                and Category of subquotients of monoids
                and Category of quotients of semigroups
                and Category of finite enumerated sets
            sage: R.is_field()
            True
            sage: R.category()
            Join of Category of finite enumerated fields
                and Category of subquotients of monoids
                and Category of quotients of semigroups

        It is possible to mistakenly put `\\ZZ/n\\ZZ` into the category of fields.
        In this case, :meth:`is_field` will return ``True`` without performing a
        primality check. However, if the optional argument ``proof=True`` is
        provided, primality is tested and the mistake is uncovered in a warning
        message::

            sage: R = IntegerModRing(21, is_field=True)
            sage: R.is_field()
            True
            sage: R.is_field(proof=True)
            Traceback (most recent call last):
            ...
            ValueError: THIS SAGE SESSION MIGHT BE SERIOUSLY COMPROMISED!
            The order 21 is not prime, but this ring has been put
            into the category of fields. This may already have consequences
            in other parts of Sage. Either it was a mistake of the user,
            or a probabilistic primality test has failed.
            In the latter case, please inform the developers.

        To avoid side-effects of this test on other tests, we clear the cache
        of the ring factory::

            sage: IntegerModRing._cache.clear()
        """
    @cached_method
    def field(self):
        """
        If this ring is a field, return the corresponding field as a finite
        field, which may have extra functionality and structure. Otherwise,
        raise a :exc:`ValueError`.

        EXAMPLES::

            sage: R = Integers(7); R
            Ring of integers modulo 7
            sage: R.field()
            Finite Field of size 7
            sage: R = Integers(9)
            sage: R.field()
            Traceback (most recent call last):
            ...
            ValueError: self must be a field
        """
    @cached_method
    def multiplicative_group_is_cyclic(self):
        """
        Return ``True`` if the multiplicative group of this field is cyclic.
        This is the case exactly when the order is less than 8, a power
        of an odd prime, or twice a power of an odd prime.

        EXAMPLES::

            sage: R = Integers(7); R
            Ring of integers modulo 7
            sage: R.multiplicative_group_is_cyclic()
            True
            sage: R = Integers(9)
            sage: R.multiplicative_group_is_cyclic()                                    # needs sage.libs.pari
            True
            sage: Integers(8).multiplicative_group_is_cyclic()
            False
            sage: Integers(4).multiplicative_group_is_cyclic()
            True
            sage: Integers(25*3).multiplicative_group_is_cyclic()                       # needs sage.libs.pari
            False

        We test that :issue:`5250` is fixed::

            sage: Integers(162).multiplicative_group_is_cyclic()                        # needs sage.libs.pari
            True
        """
    @cached_method
    def multiplicative_generator(self):
        """
        Return a generator for the multiplicative group of this ring,
        assuming the multiplicative group is cyclic.

        Use the unit_gens function to obtain generators even in the
        non-cyclic case.

        EXAMPLES::

            sage: # needs sage.groups sage.libs.pari
            sage: R = Integers(7); R
            Ring of integers modulo 7
            sage: R.multiplicative_generator()
            3
            sage: R = Integers(9)
            sage: R.multiplicative_generator()
            2
            sage: Integers(8).multiplicative_generator()
            Traceback (most recent call last):
            ...
            ValueError: multiplicative group of this ring is not cyclic
            sage: Integers(4).multiplicative_generator()
            3
            sage: Integers(25*3).multiplicative_generator()
            Traceback (most recent call last):
            ...
            ValueError: multiplicative group of this ring is not cyclic
            sage: Integers(25*3).unit_gens()
            (26, 52)
            sage: Integers(162).unit_gens()
            (83,)
        """
    def quadratic_nonresidue(self):
        """
        Return a quadratic non-residue in ``self``.

        EXAMPLES::

            sage: R = Integers(17)
            sage: R.quadratic_nonresidue()                                              # needs sage.libs.pari
            3
            sage: R(3).is_square()
            False
        """
    def square_roots_of_one(self):
        """
        Return all square roots of 1 in self, i.e., all solutions to
        `x^2 - 1 = 0`.

        OUTPUT: the square roots of 1 in ``self`` as a tuple

        EXAMPLES::

            sage: R = Integers(2^10)
            sage: [x for x in R if x^2 == 1]
            [1, 511, 513, 1023]
            sage: R.square_roots_of_one()
            (1, 511, 513, 1023)

        ::

            sage: # needs sage.libs.pari
            sage: v = Integers(9*5).square_roots_of_one(); v
            (1, 19, 26, 44)
            sage: [x^2 for x in v]
            [1, 1, 1, 1]
            sage: v = Integers(9*5*8).square_roots_of_one(); v
            (1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359)
            sage: [x^2 for x in v]
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        """
    @cached_method
    def factored_order(self):
        """
        EXAMPLES::

            sage: R = IntegerModRing(18)
            sage: FF = IntegerModRing(17)
            sage: R.factored_order()
            2 * 3^2
            sage: FF.factored_order()
            17
        """
    def factored_unit_order(self):
        """
        Return a list of :class:`Factorization` objects, each the factorization
        of the order of the units in a `\\ZZ / p^n \\ZZ` component of this group
        (using the Chinese Remainder Theorem).

        EXAMPLES::

            sage: R = Integers(8*9*25*17*29)
            sage: R.factored_unit_order()
            [2^2, 2 * 3, 2^2 * 5, 2^4, 2^2 * 7]
        """
    def characteristic(self):
        """
        EXAMPLES::

            sage: R = IntegerModRing(18)
            sage: FF = IntegerModRing(17)
            sage: FF.characteristic()
            17
            sage: R.characteristic()
            18
        """
    def modulus(self):
        """
        Return the polynomial `x - 1` over this ring.

        .. NOTE::

           This function exists for consistency with the finite-field
           modulus function.

        EXAMPLES::

            sage: R = IntegerModRing(18)
            sage: R.modulus()
            x + 17
            sage: R = IntegerModRing(17)
            sage: R.modulus()
            x + 16
        """
    def order(self):
        """
        Return the order of this ring.

        EXAMPLES::

            sage: Zmod(87).order()
            87
        """
    def cardinality(self):
        """
        Return the cardinality of this ring.

        EXAMPLES::

            sage: Zmod(87).cardinality()
            87
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: R = IntegerModRing(3)
            sage: for i in R:
            ....:     print(i)
            0
            1
            2
            sage: L = [i for i in R]
            sage: L[0].parent()
            Ring of integers modulo 3
        """
    def __richcmp__(self, other, op):
        """
        EXAMPLES::

            sage: Z11 = IntegerModRing(11); Z11
            Ring of integers modulo 11
            sage: Z12 = IntegerModRing(12); Z12
            Ring of integers modulo 12
            sage: Z13 = IntegerModRing(13); Z13
            Ring of integers modulo 13
            sage: Z11 == Z11, Z11 == Z12, Z11 == Z13
            (True, False, False)
            sage: F = GF(11); F
            Finite Field of size 11
            sage: Z11 == F
            False

        In :issue:`15229`, the following was implemented::

            sage: R1 = IntegerModRing(5)
            sage: R2 = IntegerModRing(5, is_field=True)
            sage: R1 is R2    # used to return False
            True
            sage: R2 == GF(5)
            False
        """
    def unit_gens(self, **kwds):
        """
        Return generators for the unit group `(\\ZZ/N\\ZZ)^*`.

        We compute the list of generators using a deterministic algorithm, so
        the generators list will always be the same. For each odd prime divisor
        of `N` there will be exactly one corresponding generator; if `N` is
        even there will be 0, 1 or 2 generators according to whether 2 divides
        `N` to order 1, 2 or `\\geq 3`.

        OUTPUT: a tuple containing the units of ``self``

        EXAMPLES::

            sage: R = IntegerModRing(18)
            sage: R.unit_gens()                                                         # needs sage.groups
            (11,)
            sage: R = IntegerModRing(17)
            sage: R.unit_gens()                                                         # needs sage.groups
            (3,)
            sage: IntegerModRing(next_prime(10^30)).unit_gens()                         # needs sage.groups
            (5,)

        The choice of generators is affected by the optional keyword
        ``algorithm``; this can be ``'sage'`` (default) or ``'pari'``.
        See :meth:`unit_group` for details. ::

            sage: A = Zmod(55)
            sage: A.unit_gens(algorithm='sage')                                         # needs sage.groups
            (12, 46)
            sage: A.unit_gens(algorithm='pari')                                         # needs sage.groups sage.libs.pari
            (2, 21)

        TESTS::

            sage: IntegerModRing(2).unit_gens()                                         # needs sage.groups
            ()
            sage: IntegerModRing(4).unit_gens()                                         # needs sage.groups
            (3,)
            sage: IntegerModRing(8).unit_gens()                                         # needs sage.groups
            (7, 5)
        """
    def unit_group_exponent(self):
        """
        EXAMPLES::

            sage: R = IntegerModRing(17)
            sage: R.unit_group_exponent()                                               # needs sage.groups
            16
            sage: R = IntegerModRing(18)
            sage: R.unit_group_exponent()                                               # needs sage.groups
            6
        """
    def unit_group_order(self):
        """
        Return the order of the unit group of this residue class ring.

        EXAMPLES::

            sage: R = Integers(500)
            sage: R.unit_group_order()                                                  # needs sage.groups
            200
        """
    @cached_method
    def unit_group(self, algorithm: str = 'sage'):
        """
        Return the unit group of ``self``.

        INPUT:

        - ``self`` -- the ring `\\ZZ/n\\ZZ` for a positive integer `n`

        - ``algorithm`` -- either ``'sage'`` (default) or ``'pari'``

        OUTPUT:

        The unit group of ``self``.  This is a finite Abelian group
        equipped with a distinguished set of generators, which is
        computed using a deterministic algorithm depending on the
        ``algorithm`` parameter.

        - If ``algorithm == 'sage'``, the generators correspond to the
          prime factors `p \\mid n` (one generator for each odd `p`;
          the number of generators for `p = 2` is 0, 1 or 2 depending
          on the order to which 2 divides `n`).

        - If ``algorithm == 'pari'``, the generators are chosen such
          that their orders form a decreasing sequence with respect to
          divisibility.

        EXAMPLES:

        The output of the algorithms ``'sage'`` and ``'pari'`` can
        differ in various ways.  In the following example, the same
        cyclic factors are computed, but in a different order::

            sage: # needs sage.groups
            sage: A = Zmod(15)
            sage: G = A.unit_group(); G
            Multiplicative Abelian group isomorphic to C2 x C4
            sage: G.gens_values()
            (11, 7)
            sage: H = A.unit_group(algorithm='pari'); H                                 # needs sage.libs.pari
            Multiplicative Abelian group isomorphic to C4 x C2
            sage: H.gens_values()                                                       # needs sage.libs.pari
            (7, 11)

        Here are two examples where the cyclic factors are isomorphic,
        but are ordered differently and have different generators::

            sage: # needs sage.groups
            sage: A = Zmod(40)
            sage: G = A.unit_group(); G
            Multiplicative Abelian group isomorphic to C2 x C2 x C4
            sage: G.gens_values()
            (31, 21, 17)
            sage: H = A.unit_group(algorithm='pari'); H                                 # needs sage.libs.pari
            Multiplicative Abelian group isomorphic to C4 x C2 x C2
            sage: H.gens_values()                                                       # needs sage.libs.pari
            (17, 31, 21)

            sage: # needs sage.groups
            sage: A = Zmod(192)
            sage: G = A.unit_group(); G
            Multiplicative Abelian group isomorphic to C2 x C16 x C2
            sage: G.gens_values()
            (127, 133, 65)
            sage: H = A.unit_group(algorithm='pari'); H                                 # needs sage.libs.pari
            Multiplicative Abelian group isomorphic to C16 x C2 x C2
            sage: H.gens_values()                                                       # needs sage.libs.pari
            (133, 127, 65)

        In the following examples, the cyclic factors are not even
        isomorphic::

            sage: A = Zmod(319)
            sage: A.unit_group()                                                        # needs sage.groups
            Multiplicative Abelian group isomorphic to C10 x C28
            sage: A.unit_group(algorithm='pari')                                        # needs sage.groups sage.libs.pari
            Multiplicative Abelian group isomorphic to C140 x C2

            sage: A = Zmod(30.factorial())
            sage: A.unit_group()                                                        # needs sage.groups
            Multiplicative Abelian group isomorphic to
             C2 x C16777216 x C3188646 x C62500 x C2058 x C110 x C156 x C16 x C18 x C22 x C28
            sage: A.unit_group(algorithm='pari')                                        # needs sage.groups sage.libs.pari
            Multiplicative Abelian group isomorphic to
             C20499647385305088000000 x C55440 x C12 x C12 x C4 x C2 x C2 x C2 x C2 x C2 x C2

        TESTS:

        We test the cases where the unit group is trivial::

            sage: # needs sage.groups
            sage: A = Zmod(1)
            sage: A.unit_group()
            Trivial Abelian group
            sage: A.unit_group(algorithm='pari')                                        # needs sage.libs.pari
            Trivial Abelian group
            sage: A = Zmod(2)
            sage: A.unit_group()
            Trivial Abelian group
            sage: A.unit_group(algorithm='pari')                                        # needs sage.libs.pari
            Trivial Abelian group

            sage: Zmod(3).unit_group(algorithm='bogus')                                 # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm 'bogus' for computing the unit group
        """
    def random_element(self, bound=None):
        """
        Return a random element of this ring.

        INPUT:

        - ``bound`` -- positive integer or ``None`` (the default); if given,
          return  the coercion of an integer in the interval
          ``[-bound, bound]`` into this ring

        EXAMPLES::

            sage: R = IntegerModRing(18)
            sage: R.random_element().parent() is R
            True
            sage: found = [False]*18
            sage: while not all(found):
            ....:     found[R.random_element()] = True

        We test the ``bound`` option::

            sage: R.random_element(2) in [R(-2), R(-1), R(0), R(1), R(2)]
            True
        """
    def degree(self):
        """
        Return 1.

        EXAMPLES::

            sage: R = Integers(12345678900)
            sage: R.degree()
            1
        """

def crt(v):
    """
    INPUT:

    - ``v`` -- (list) a lift of elements of ``rings.IntegerMod(n)``, for
      various coprime moduli ``n``

    EXAMPLES::

        sage: from sage.rings.finite_rings.integer_mod_ring import crt
        sage: crt([mod(3, 8), mod(1,19), mod(7, 15)])
        1027
    """
