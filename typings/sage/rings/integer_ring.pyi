r"""
Ring `\ZZ` of Integers

The :class:`IntegerRing_class` represents the ring `\ZZ` of (arbitrary
precision) integers. Each integer is an instance of :class:`Integer`,
which is defined in a Pyrex extension module that wraps GMP integers
(the ``mpz_t`` type in GMP).

::

    sage: Z = IntegerRing(); Z
    Integer Ring
    sage: Z.characteristic()
    0
    sage: Z.is_field()
    False

There is a unique instance of the :class:`integer ring<IntegerRing_class>`.
To create an :class:`Integer`, coerce either a Python int, long, or a string. Various
other types will also coerce to the integers, when it makes sense.

::

    sage: a = Z(1234); a
    1234
    sage: b = Z(5678); b
    5678
    sage: type(a)
    <class 'sage.rings.integer.Integer'>
    sage: a + b
    6912
    sage: Z('94803849083985934859834583945394')
    94803849083985934859834583945394
"""

from typing import Annotated, Any, Literal, Self, TypeGuard, overload
from collections.abc import Callable, Iterable, Iterator
from typings_sagemath import Int
from sage.rings.ring import PrincipalIdealDomain
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_integral_domain
    # TODO: with: Join category of 
    # [Category of unique factorization domains,
    #  Category of algebras with basis over (Dedekind domains and euclidean domains and noetherian rings and infinite enumerated sets and metric spaces),
    #  Category of commutative algebras over (Dedekind domains and euclidean domains and noetherian rings and infinite enumerated sets and metric spaces),
    #  Category of infinite sets]
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.number_field.order import Order
from sage.rings.integer import Integer
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.rational_field import RationalField # TODO: with 
    # [Category of number fields,
    # Category of quotient fields,
    # Category of metric spaces]
from sage.rings.ideal import Ideal_generic
from sage.rings.finite_rings.residue_field import ResidueField_generic
from sage.rings.infinity import PlusInfinity
from sage.rings.padics.padic_base_leaves import pAdicRingCappedRelative # with
    # [Category of complete discrete valuation rings,
    # Category of infinite sets,
    # Category of complete metric spaces]
from sage.rings.padics.padic_valuation import pAdicValuation_int # with Category of homsets of sets

import sage as sage
from sage.categories.dedekind_domains import DedekindDomains as DedekindDomains
from sage.categories.euclidean_domains import EuclideanDomains as EuclideanDomains
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.noetherian_rings import NoetherianRings as NoetherianRings
from sage.misc.misc_c import prod as prod
from sage.rings.number_field.number_field_element_base import NumberFieldElement_base as NumberFieldElement_base
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
import sage.arith.all as arith

type _NotUsed = object

def IntegerRing() -> IntegerRing_class:
    """
Return the integer ring.

EXAMPLES::

    sage: IntegerRing()
    Integer Ring
    sage: ZZ==IntegerRing()
    True

"""

def crt_basis(X: list[Integer], xgcd: _NotUsed = None) -> list[Integer]:
    r"""
    Compute and return a Chinese Remainder Theorem basis for the list ``X``
    of coprime integers.

    INPUT:

    - ``X`` -- list of Integers that are coprime in pairs

    - ``xgcd`` -- an optional parameter which is ignored

    OUTPUT:

    - ``E`` -- list of Integers such that ``E[i] = 1`` (mod ``X[i]``) and
      ``E[i] = 0`` (mod ``X[j]``) for all `j \neq i`

    For this explanation, let ``E[i]`` be denoted by `E_i`.

    The `E_i` have the property that if `A` is a list of objects, e.g.,
    integers, vectors, matrices, etc., where `A_i` is understood modulo
    `X_i`, then a CRT lift of `A` is simply

    .. MATH::

        \sum_i E_i A_i.

    ALGORITHM: To compute `E_i`, compute integers `s` and `t` such that

    .. MATH::

        s X_i + t \prod_{i \neq j} X_j = 1. (\*)

    Then

    .. MATH::

        E_i = t \prod_{i \neq j} X[j].

    Notice that equation
    (\*) implies that `E_i` is congruent to 1 modulo `X_i` and to 0
    modulo the other `X_j` for `j \neq i`.

    COMPLEXITY: We compute ``len(X)`` extended GCD's.

    EXAMPLES::

        sage: X = [11,20,31,51]
        sage: E = crt_basis([11,20,31,51])
        sage: E[0]%X[0], E[1]%X[0], E[2]%X[0], E[3]%X[0]
        (1, 0, 0, 0)
        sage: E[0]%X[1], E[1]%X[1], E[2]%X[1], E[3]%X[1]
        (0, 1, 0, 0)
        sage: E[0]%X[2], E[1]%X[2], E[2]%X[2], E[3]%X[2]
        (0, 0, 1, 0)
        sage: E[0]%X[3], E[1]%X[3], E[2]%X[3], E[3]%X[3]
        (0, 0, 0, 1)
    """
    ...

def is_IntegerRing(x) -> TypeGuard[IntegerRing_class]:
    r"""
    Internal function: return ``True`` iff ``x`` is the ring `\ZZ` of integers.

    TESTS::

        sage: from sage.rings.integer_ring import is_IntegerRing
        sage: is_IntegerRing(ZZ)
        doctest:warning...
        DeprecationWarning: The function is_IntegerRing is deprecated;
        use 'isinstance(..., IntegerRing_class)' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        True
        sage: is_IntegerRing(QQ)
        False
        sage: is_IntegerRing(parent(3))
        True
        sage: is_IntegerRing(parent(1/3))
        False
    """

class IntegerRing_class(PrincipalIdealDomain):
    '''
    The ring of integers.

    In order to introduce the ring `\\ZZ` of integers, we illustrate
    creation, calling a few functions, and working with its elements.

    ::

        sage: Z = IntegerRing(); Z
        Integer Ring
        sage: Z.characteristic()
        0
        sage: Z.is_field()
        False
        sage: Z.category()
        Join of Category of Dedekind domains
            and Category of euclidean domains
            and Category of noetherian rings
            and Category of infinite enumerated sets
            and Category of metric spaces
        sage: Z(2^(2^5) + 1)
        4294967297

    One can give strings to create integers. Strings starting with
    ``0x`` are interpreted as hexadecimal, and strings starting with
    ``0o`` are interpreted as octal::

        sage: parent(\'37\')
        <... \'str\'>
        sage: parent(Z(\'37\'))
        Integer Ring
        sage: Z(\'0x10\')
        16
        sage: Z(\'0x1a\')
        26
        sage: Z(\'0o20\')
        16

    As an inverse to :meth:`~sage.rings.integer.Integer.digits`,
    lists of digits are accepted, provided that you give a base.
    The lists are interpreted in little-endian order, so that
    entry ``i`` of the list is the coefficient of ``base^i``::

        sage: Z([4,1,7], base=100)
        70104
        sage: Z([4,1,7], base=10)
        714
        sage: Z([3, 7], 10)
        73
        sage: Z([3, 7], 9)
        66
        sage: Z([], 10)
        0

    Alphanumeric strings can be used for bases 2..36; letters ``a`` to
    ``z`` represent numbers 10 to 36.  Letter case does not matter.
    ::

        sage: Z("sage", base=32)
        928270
        sage: Z("SAGE", base=32)
        928270
        sage: Z("Sage", base=32)
        928270
        sage: Z([14, 16, 10, 28], base=32)
        928270
        sage: 14 + 16*32 + 10*32^2 + 28*32^3
        928270

    We next illustrate basic arithmetic in `\\ZZ`::

        sage: a = Z(1234); a
        1234
        sage: b = Z(5678); b
        5678
        sage: type(a)
        <class \'sage.rings.integer.Integer\'>
        sage: a + b
        6912
        sage: b + a
        6912
        sage: a * b
        7006652
        sage: b * a
        7006652
        sage: a - b
        -4444
        sage: b - a
        4444

    When we divide two integers using ``/``, the result is automatically
    coerced to the field of rational numbers, even if the result is
    an integer.

    ::

        sage: a / b
        617/2839
        sage: type(a/b)
        <class \'sage.rings.rational.Rational\'>
        sage: a/a
        1
        sage: type(a/a)
        <class \'sage.rings.rational.Rational\'>

    For floor division, use the ``//`` operator instead::

        sage: a // b
        0
        sage: type(a//b)
        <class \'sage.rings.integer.Integer\'>

    Next we illustrate arithmetic with automatic coercion. The types
    that coerce are: str, int, long, Integer.

    ::

        sage: a + 17
        1251
        sage: a * 374
        461516
        sage: 374 * a
        461516
        sage: a/19
        1234/19
        sage: 0 + Z(-64)
        -64

    Integers can be coerced::

        sage: a = Z(-64)
        sage: int(a)
        -64

    We can create integers from several types of objects::

        sage: Z(17/1)
        17
        sage: Z(Mod(19,23))
        19
        sage: Z(2 + 3*5 + O(5^3))                                                       # needs sage.rings.padics
        17

    Arbitrary numeric bases are supported; strings or list of integers
    are used to provide the digits (more details in
    :class:`IntegerRing_class`)::

        sage: Z("sage", base=32)
        928270
        sage: Z([14, 16, 10, 28], base=32)
        928270

    The :meth:`digits<~sage.rings.integer.Integer.digits>` method
    allows you to get the list of digits of an integer in a different
    basis (note that the digits are returned in little-endian order)::

        sage: b = Z([4,1,7], base=100)
        sage: b
        70104
        sage: b.digits(base=71)
        [27, 64, 13]

        sage: Z(15).digits(2)
        [1, 1, 1, 1]
        sage: Z(15).digits(3)
        [0, 2, 1]

    The :meth:`str<~sage.rings.integer.Integer.str>` method returns a
    string of the digits, using letters ``a`` to ``z`` to represent
    digits 10..36::

        sage: Z(928270).str(base=32)
        \'sage\'

    Note that :meth:`str<~sage.rings.integer.Integer.str>` only works
    with bases 2 through 36.

    TESTS::

        sage: TestSuite(ZZ).run()
        sage: list(ZZ)
        Traceback (most recent call last):
        ...
        NotImplementedError: len() of an infinite set

        sage: ZZ.is_finite()
        False
        sage: ZZ.cardinality()
        +Infinity'''
    
    def __init__(self):
        """
                Initialize ``self``.

                TESTS::

                    sage: from sage.rings.integer_ring import IntegerRing_class
                    sage: A = IntegerRing_class()

                We check that ``ZZ`` is an infinite enumerated set
                (see :issue:`16239`)::

                    sage: A in InfiniteEnumeratedSets()
                    True
        """
    def absolute_degree(self) -> Literal[1]:
        """
        Return the absolute degree of the integers, which is 1.

        Here, absolute degree refers to the rank of the ring as a module
        over the integers.

        EXAMPLES::

            sage: ZZ.absolute_degree()
            1"""
    def characteristic(self) -> Annotated[Integer, 0]:
        """
        Return the characteristic of the integers, which is 0.

        EXAMPLES::

            sage: ZZ.characteristic()
            0"""
    def completion(self, p: Int | PlusInfinity, prec: Int, extras: dict[str, Any]={}) -> pAdicRingCappedRelative:
        """
        Return the metric completion of the integers at the prime `p`.

        INPUT:

        - ``p`` -- a prime (or ``infinity``)

        - ``prec`` -- the desired precision

        - ``extras`` -- any further parameters to pass to the method used to
          create the completion

        OUTPUT: the completion of `\\ZZ` at `p`

        EXAMPLES::

            sage: ZZ.completion(infinity, 53)
            Integer Ring
            sage: ZZ.completion(5, 15, {'print_mode': 'bars'})                          # needs sage.rings.padics
            5-adic Ring with capped relative precision 15"""
    def degree(self) -> Literal[1]:
        """
        Return the degree of the integers, which is 1.

        Here, degree refers to the rank of the ring as a module over the
        integers.

        EXAMPLES::

            sage: ZZ.degree()
            1"""
    def extension( # pyright: ignore[reportIncompatibleMethodOverride]
        self, 
        poly: Polynomial | MPolynomial | Iterable[Polynomial | MPolynomial],
        names: str | Iterable[str], 
        embedding = None, 
        **kwds) -> Order:
        """
        Return the order generated by the specified list of polynomials.

        INPUT:

        - ``poly`` -- list of one or more polynomials

        - ``names`` -- a parameter which will be passed to
          :func:`EquationOrder`

        - ``embedding`` -- a parameter which will be passed to
          :func:`EquationOrder`

        OUTPUT:

        - Given a single polynomial as input, return the order generated by a
          root of the polynomial in the field generated by a root of the
          polynomial.

          Given a list of polynomials as input, return the relative order
          generated by a root of the first polynomial in the list, over the
          order generated by the roots of the subsequent polynomials.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: ZZ.extension(x^2 - 5, 'a')                                            # needs sage.rings.number_field
            Order of conductor 2 generated by a in Number Field in a with defining polynomial x^2 - 5
            sage: ZZ.extension([x^2 + 1, x^2 + 2], 'a,b')                               # needs sage.rings.number_field
            Relative Order generated by [-b*a - 1, -3*a + 2*b] in Number Field in a
             with defining polynomial x^2 + 1 over its base field"""
    def fraction_field(self) -> RationalField:
        """
        Return the field of rational numbers - the fraction field of the
        integers.

        EXAMPLES::

            sage: ZZ.fraction_field()
            Rational Field
            sage: ZZ.fraction_field() == QQ
            True"""
    def from_bytes(self, input_bytes: bytes, byteorder: Literal["little", "big"]="big", is_signed: bool =False) -> Integer:
        """
        Return the integer represented by the given array of bytes.

        Internally relies on the python ``int.from_bytes()`` method.

        INPUT:

        - ``input_bytes`` -- a bytes-like object or iterable producing bytes
        - ``byteorder`` -- string (default: ``'big'``); determines the byte order of
          ``input_bytes`` (can only be ``'big'`` or ``'little'``)
        - ``is_signed`` -- boolean (default: ``False``); determines whether to use two's
          compliment to represent the integer

        EXAMPLES::

            sage: ZZ.from_bytes(b'\\x00\\x10', byteorder='big')
            16
            sage: ZZ.from_bytes(b'\\x00\\x10', byteorder='little')
            4096
            sage: ZZ.from_bytes(b'\\xfc\\x00', byteorder='big', is_signed=True)
            -1024
            sage: ZZ.from_bytes(b'\\xfc\\x00', byteorder='big', is_signed=False)
            64512
            sage: ZZ.from_bytes([255, 0, 0], byteorder='big')
            16711680
            sage: type(_)
            <class 'sage.rings.integer.Integer'>"""
    def gen(self, n: Literal[0] = 0) -> Integer: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Return the additive generator of the integers, which is 1.

        INPUT:

        - ``n`` -- (default: 0) in a ring with more than one generator, the
          optional parameter `n` indicates which generator to return; since
          there is only one generator in this case, the only valid value for
          `n` is 0

        EXAMPLES::

            sage: ZZ.gen()
            1
            sage: type(ZZ.gen())
            <class 'sage.rings.integer.Integer'>"""
    def gens(self) -> tuple[Integer]:
        """
        Return the tuple ``(1,)`` containing a single element, the additive
        generator of the integers, which is 1.

        EXAMPLES::

            sage: ZZ.gens(); ZZ.gens()[0]
            (1,)
            1
            sage: type(ZZ.gens()[0])
            <class 'sage.rings.integer.Integer'>"""
    def is_field(self, proof: bool = True) -> Literal[False]:
        """
        Return ``False`` since the integers are not a field.

        EXAMPLES::

            sage: ZZ.is_field()
            False"""
    def krull_dimension(self) -> Literal[1]:
        """
        Return the Krull dimension of the integers, which is 1.

        .. NOTE::

            This should rather be inherited from the category
            of ``DedekindDomains``.

        EXAMPLES::

            sage: ZZ.krull_dimension()
            1"""
    def ngens(self) -> Literal[1]:
        """
        Return the number of additive generators of the ring, which is 1.

        EXAMPLES::

            sage: ZZ.ngens()
            1
            sage: len(ZZ.gens())
            1"""
    def order(self) -> PlusInfinity:
        """
        Return the order (cardinality) of the integers, which is
        ``+Infinity``.

        EXAMPLES::

            sage: ZZ.order()
            +Infinity"""
    def parameter(self) -> Annotated[Integer, 1]:
        """
        Return an integer of degree 1 for the Euclidean property of `\\ZZ`,
        namely 1.

        EXAMPLES::

            sage: ZZ.parameter()
            1"""
    def quotient(self, I: Integer | Ideal_generic, names: _NotUsed = None, **kwds) -> IntegerModRing_generic:
        """
        Return the quotient of `\\ZZ` by the ideal or integer ``I``.

        EXAMPLES::

            sage: ZZ.quo(6*ZZ)
            Ring of integers modulo 6
            sage: ZZ.quo(0*ZZ)
            Integer Ring
            sage: ZZ.quo(3)
            Ring of integers modulo 3
            sage: ZZ.quo(3*QQ)
            Traceback (most recent call last):
            ...
            TypeError: I must be an ideal of ZZ"""
    def random_element(
        self, 
        x: int | None = None, 
        y: Int | None = None, 
        distribution: Literal[
            "uniform", "mpz_rrandomb", "1/n", "gaussian"] | None = None
    ) -> Integer:
        '''
        Return a random integer.

        INPUT:

        - ``x``, ``y`` integers -- bounds for the result

        - ``distribution`` -- string:

          - ``\'uniform\'``
          - ``\'mpz_rrandomb\'``
          - ``\'1/n\'``
          - ``\'gaussian\'``

        OUTPUT: with no input, return a random integer

          If only one integer `x` is given, return an integer
          between 0 and `x-1`.

          If two integers are given, return an integer
          between `x` and `y-1` inclusive.

          If at least one bound is given, the default distribution is the
          uniform distribution; otherwise, it is the distribution described
          below.

          If the distribution ``\'1/n\'`` is specified, the bounds are ignored.

          If the distribution ``\'mpz_rrandomb\'`` is specified, the output is
          in the range from 0 to `2^x - 1`.

          If the distribution ``\'gaussian\'`` is specified, the output is
          sampled from a discrete Gaussian distribution with parameter
          `\\sigma=x` and centered at zero. That is, the integer `v` is returned
          with probability proportional to `\\mathrm{exp}(-v^2/(2\\sigma^2))`.
          See :mod:`sage.stats.distributions.discrete_gaussian_integer` for
          details.  Note that if many samples from the same discrete Gaussian
          distribution are needed, it is faster to construct a
          :class:`sage.stats.distributions.discrete_gaussian_integer.DiscreteGaussianDistributionIntegerSampler`
          object which is then repeatedly queried.

        The default distribution for ``ZZ.random_element()`` is based on
        `X = \\mbox{trunc}(4/(5R))`, where `R` is a random
        variable uniformly distributed between `-1` and `1`. This gives
        `\\mbox{Pr}(X = 0) = 1/5`, and
        `\\mbox{Pr}(X = n) = 2/(5|n|(|n|+1))` for
        `n \\neq 0`. Most of the samples will be small; `-1`, `0`, and `1`
        occur with probability `1/5` each. But we also have a small but
        non-negligible proportion of "outliers";
        `\\mbox{Pr}(|X| \\geq n) = 4/(5n)`, so for instance, we
        expect that `|X| \\geq 1000` on one in 1250 samples.

        We actually use an easy-to-compute truncation of the above
        distribution; the probabilities given above hold fairly well up to
        about `|n| = 10000`, but around `|n| = 30000` some
        values will never be returned at all, and we will never return
        anything greater than `2^{30}`.

        EXAMPLES::

            sage: ZZ.random_element().parent() is ZZ
            True

        The default uniform distribution is integers in `[-2, 2]`::

            sage: from collections import defaultdict
            sage: def add_samples(*args, **kwds):
            ....:     global dic, counter
            ....:     for _ in range(100):
            ....:         counter += 1
            ....:         dic[ZZ.random_element(*args, **kwds)] += 1

            sage: def prob(x):
            ....:     return 1/5
            sage: dic = defaultdict(Integer)
            sage: counter = 0.0
            sage: add_samples(distribution=\'uniform\')
            sage: while any(abs(dic[i]/counter - prob(i)) > 0.01 for i in dic):
            ....:     add_samples(distribution=\'uniform\')

        Here we use the distribution ``\'1/n\'``::

            sage: def prob(n):
            ....:     if n == 0:
            ....:         return 1/5
            ....:     return 2/(5*abs(n)*(abs(n) + 1))
            sage: dic = defaultdict(Integer)
            sage: counter = 0.0
            sage: add_samples(distribution=\'1/n\')
            sage: while any(abs(dic[i]/counter - prob(i)) > 0.01 for i in dic):
            ....:     add_samples(distribution=\'1/n\')

        If a range is given, the default distribution is uniform in that
        range::

            sage: -10 <= ZZ.random_element(-10, 10) < 10
            True
            sage: def prob(x):
            ....:     return 1/20
            sage: dic = defaultdict(Integer)
            sage: counter = 0.0
            sage: add_samples(-10, 10)
            sage: while any(abs(dic[i]/counter - prob(i)) > 0.01 for i in dic):
            ....:     add_samples(-10, 10)

            sage: 0 <= ZZ.random_element(5) < 5
            True
            sage: def prob(x):
            ....:     return 1/5
            sage: dic = defaultdict(Integer)
            sage: counter = 0.0
            sage: add_samples(5)
            sage: while any(abs(dic[i]/counter - prob(i)) > 0.01 for i in dic):
            ....:     add_samples(5)

            sage: while ZZ.random_element(10^50) < 10^49:
            ....:     pass

        Notice that the right endpoint is not included::

            sage: all(ZZ.random_element(-2, 2) < 2 for _ in range(100))
            True

        We return a sample from a discrete Gaussian distribution::

             sage: ZZ.random_element(11.0, distribution=\'gaussian\').parent() is ZZ      # needs sage.modules
             True

        TESTS:

        Check that :issue:`32124` is fixed::

            sage: ZZ.random_element(5, -5, distribution=\'1/n\').parent() is ZZ
            True
            sage: ZZ.random_element(5, -5, distribution=\'gaussian\').parent() is ZZ      # needs sage.modules
            True
            sage: ZZ.random_element(5, -5, distribution=\'mpz_rrandomb\').parent() is ZZ
            True

            sage: ZZ.random_element(-10, -5, distribution=\'mpz_rrandomb\')
            Traceback (most recent call last):
            ...
            TypeError: x must be > 0
            sage: ZZ.random_element(-10, -5, distribution=\'gaussian\')
            Traceback (most recent call last):
            ...
            TypeError: x must be > 0

        Checking error messages::

            sage: ZZ.random_element(-3)
            Traceback (most recent call last):
            ...
            TypeError: x must be > 0
            sage: ZZ.random_element(4, 2)
            Traceback (most recent call last):
            ...
            TypeError: x must be < y'''
    @overload
    def range(self, end: Int) -> list[Integer]: ...
    @overload
    def range(self, start: Int, end: Int, step: Int = 1) -> list[Integer]:
        """
        Optimized range function for Sage integers.

        AUTHORS:

        - Robert Bradshaw (2007-09-20)

        EXAMPLES::

            sage: ZZ.range(10)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: ZZ.range(-5, 5)
            [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
            sage: ZZ.range(0, 50, 5)
            [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
            sage: ZZ.range(0, 50, -5)
            []
            sage: ZZ.range(50, 0, -5)
            [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
            sage: ZZ.range(50, 0, 5)
            []
            sage: ZZ.range(50, -1, -5)
            [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]

        It uses different code if the step doesn't fit in a long::

            sage: ZZ.range(0, 2^83, 2^80)
            [0, 1208925819614629174706176, 2417851639229258349412352,
             3626777458843887524118528, 4835703278458516698824704, 6044629098073145873530880,
             7253554917687775048237056, 8462480737302404222943232]

        Make sure :issue:`8818` is fixed::

            sage: ZZ.range(1r, 10r)
            [1, 2, 3, 4, 5, 6, 7, 8, 9]"""
    def residue_field(self, prime: Integer | Ideal_generic, check: bool = True, names: _NotUsed = None) -> ResidueField_generic:
        """
        Return the residue field of the integers modulo the given prime, i.e.
        `\\ZZ/p\\ZZ`.

        INPUT:

        - ``prime`` -- a prime number

        - ``check`` -- boolean (default: ``True``); whether or not
          to check the primality of prime

        - ``names`` -- ignored (for compatibility with number fields)

        OUTPUT: the residue field at this prime

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: F = ZZ.residue_field(61); F
            Residue field of Integers modulo 61
            sage: pi = F.reduction_map(); pi
            Partially defined reduction map:
              From: Rational Field
              To:   Residue field of Integers modulo 61
            sage: pi(123/234)
            6
            sage: pi(1/61)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot reduce rational 1/61 modulo 61:
            it has negative valuation
            sage: lift = F.lift_map(); lift
            Lifting map:
              From: Residue field of Integers modulo 61
              To:   Integer Ring
            sage: lift(F(12345/67890))
            33
            sage: (12345/67890) % 61
            33

        Construction can be from a prime ideal instead of a prime::

            sage: ZZ.residue_field(ZZ.ideal(97))
            Residue field of Integers modulo 97

        TESTS::

            sage: ZZ.residue_field(ZZ.ideal(96))
            Traceback (most recent call last):
            ...
            TypeError: Principal ideal (96) of Integer Ring is not prime
            sage: ZZ.residue_field(96)
            Traceback (most recent call last):
            ...
            TypeError: 96 is not prime"""
    def valuation(self) -> pAdicValuation_int:
        """
        Return the discrete valuation with uniformizer ``p``.

        EXAMPLES::

            sage: v = ZZ.valuation(3); v                                                # needs sage.rings.padics
            3-adic valuation
            sage: v(3)                                                                  # needs sage.rings.padics
            1

        .. SEEALSO::

            :meth:`Order.valuation() <sage.rings.number_field.order.Order.valuation>`,
            :meth:`RationalField.valuation() <sage.rings.rational_field.RationalField.valuation>`"""
    def zeta(self, n: Literal[1, 2] = 2) -> Integer:
        """
        Return a primitive ``n``-th root of unity in the integers, or raise an
        error if none exists.

        INPUT:

        - ``n`` -- (default: 2) a positive integer

        OUTPUT:

        an ``n``-th root of unity in `\\ZZ`

        EXAMPLES::

            sage: ZZ.zeta()
            -1
            sage: ZZ.zeta(1)
            1
            sage: ZZ.zeta(3)
            Traceback (most recent call last):
            ...
            ValueError: no nth root of unity in integer ring
            sage: ZZ.zeta(0)
            Traceback (most recent call last):
            ...
            ValueError: n must be positive in zeta()"""
    @overload
    def __eq__(self, other: IntegerRing_class) -> Literal[True]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def __eq__(self, other: object) -> Literal[False]: ...
    @overload
    def __ge__(self, other: IntegerRing_class) -> Literal[True]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def __ge__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, x: Int) -> Self: ...
    @overload
    def __getitem__(self, x: NumberFieldElement_base) -> Order: ...
    @overload
    def __getitem__(self, x: str) -> PolynomialRing_integral_domain | MPolynomialRing_base: ...
    @overload
    def __getitem__(self, x):   # CommutativeRing.__getitem__(self, x)
        """
        Return the ring `\\ZZ[...]` obtained by adjoining to the integers one
        or several elements.

        EXAMPLES::

            sage: ZZ['x']
            Univariate Polynomial Ring in x over Integer Ring
            sage: ZZ['x,y']
            Multivariate Polynomial Ring in x, y over Integer Ring

            sage: # needs sage.rings.number_field sage.symbolic
            sage: ZZ[sqrt(2), sqrt(3)]
            Relative Order generated by [-sqrt3*sqrt2 + 3, 6*sqrt2 - 5*sqrt3, 11*sqrt2 - 9*sqrt3]
             in Number Field in sqrt2 with defining polynomial x^2 - 2 over its base field
            sage: R = ZZ[sqrt(5) + 1]; R
            Order of conductor 2 generated by a in Number Field in a
             with defining polynomial x^2 - 2*x - 4 with a = 3.236067977499790?
            sage: R.is_maximal()
            False
            sage: R = ZZ[(1 + sqrt(5))/2]; R
            Maximal Order generated by a in Number Field in a
             with defining polynomial x^2 - x - 1 with a = 1.618033988749895?
            sage: R.is_maximal()
            True"""
    def __gt__(self, other: object) -> Literal[False]: ...
    def __hash__(self) -> Literal[554590422]:
        """
        Return the hash value of ``self``.

        TESTS::

            sage: from sage.rings.integer_ring import IntegerRing_class
            sage: A = IntegerRing_class()
            sage: A.__hash__()
            554590422"""
    def __iter__(self) -> Iterator[Integer]:
        """
        Iterate over all integers: 0 1 -1 2 -2 3 -3 ...

        EXAMPLES::

            sage: for n in ZZ:
            ....:  if n < 3: print(n)
            ....:  else: break
            0
            1
            -1
            2
            -2"""
    @overload
    def __le__(self, other: IntegerRing_class | RationalField) -> Literal[True]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def __le__(self, other: object) -> Literal[False]: ...
    @overload
    def __lt__(self, other: RationalField) -> Literal[True]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def __lt__(self, other: object) -> Literal[False]: ...
    @overload
    def __ne__(self, other: IntegerRing_class) -> Literal[False]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def __ne__(self, other: object) -> Literal[True]: ...
    def __reduce__(self) -> tuple[Callable[[], IntegerRing_class], tuple[()]]:
        """
        For pickling.

        TESTS::

            sage: loads(dumps(ZZ)) is ZZ
            True"""
    def __richcmp__(left, right, op: int) -> bool:  # pyright: ignore[reportSelfClsParameterName]
        """
        Rich comparison of ``left`` and ``right``.

        TESTS::

            sage: from sage.rings.integer_ring import IntegerRing_class
            sage: ZZ == ZZ
            True
            sage: ZZ != QQ
            True
        """
        ...

ZZ: IntegerRing_class