from numbers import Complex, Number
import _cython_3_2_1
import sage as sage
import sage.categories.morphism
import sage.rings.integer_ring as integer_ring
import sage.structure.element
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

GCD_list: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict
free_integer_pool: _cython_3_2_1.cython_function_or_method
initialized: bool
is_Integer: _cython_3_2_1.cython_function_or_method
make_integer: _cython_3_2_1.cython_function_or_method
n_factor_to_list: None
new_gen_from_integer: None
objtogen: None
pari_divisors_small: None
pari_is_prime: None
pari_is_prime_power: None
set_integer_from_gen: None

class Integer(sage.structure.element.EuclideanDomainElement, Number):
    '''Integer(x=None, base=0)

    File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 404)

    The :class:`Integer` class represents arbitrary precision
    integers. It derives from the :class:`Element` class, so
    integers can be used as ring elements anywhere in Sage.

    The constructor of :class:`Integer` interprets strings that begin with ``0o`` as octal numbers,
    strings that begin with ``0x`` as hexadecimal numbers and strings
    that begin with ``0b`` as binary numbers.

    The class :class:`Integer` is implemented in Cython, as a wrapper of the
    GMP ``mpz_t`` integer type.

    EXAMPLES::

        sage: Integer(123)
        123
        sage: Integer("123")
        123

    Sage Integers support :pep:`3127` literals::

        sage: Integer(\'0x12\')
        18
        sage: Integer(\'-0o12\')
        -10
        sage: Integer(\'+0b101010\')
        42

    Conversion from PARI::

        sage: Integer(pari(\'-10380104371593008048799446356441519384\'))                  # needs sage.libs.pari
        -10380104371593008048799446356441519384
        sage: Integer(pari(\'Pol([-3])\'))                                                # needs sage.libs.pari
        -3

    Conversion from gmpy2::

        sage: from gmpy2 import mpz
        sage: Integer(mpz(3))
        3

    .. automethod:: __pow__'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    __array_interface__: Incomplete
    def __init__(self, x=..., base=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 454)

                EXAMPLES::

                    sage: a = int(-901824309821093821093812093810928309183091832091)
                    sage: b = ZZ(a); b
                    -901824309821093821093812093810928309183091832091
                    sage: ZZ(b)
                    -901824309821093821093812093810928309183091832091
                    sage: ZZ(\'-901824309821093821093812093810928309183091832091\')
                    -901824309821093821093812093810928309183091832091
                    sage: ZZ(int(-93820984323))
                    -93820984323
                    sage: ZZ(ZZ(-901824309821093821093812093810928309183091832091))
                    -901824309821093821093812093810928309183091832091
                    sage: ZZ(QQ(-901824309821093821093812093810928309183091832091))
                    -901824309821093821093812093810928309183091832091
                    sage: ZZ(RR(2.0)^80)
                    1208925819614629174706176
                    sage: ZZ(QQbar(sqrt(28-10*sqrt(3)) + sqrt(3)))                              # needs sage.rings.number_field sage.symbolic
                    5
                    sage: ZZ(AA(32).nth_root(5))                                                # needs sage.rings.number_field
                    2
                    sage: ZZ(pari(\'Mod(-3,7)\'))                                                 # needs sage.libs.pari
                    4
                    sage: ZZ(\'sage\')
                    Traceback (most recent call last):
                    ...
                    TypeError: unable to convert \'sage\' to an integer
                    sage: Integer(\'zz\',36).str(36)
                    \'zz\'
                    sage: ZZ(\'0x3b\').str(16)
                    \'3b\'
                    sage: ZZ( ZZ(5).digits(3) , 3)
                    5
                    sage: import numpy                                                          # needs numpy
                    sage: ZZ(numpy.int64(7^7))                                                  # needs numpy
                    823543
                    sage: ZZ(numpy.ubyte(-7))                                                   # needs numpy
                    249
                    sage: ZZ(True)
                    1
                    sage: ZZ(False)
                    0
                    sage: ZZ(1==0)
                    0
                    sage: ZZ(\'+10\')
                    10
                    sage: from gmpy2 import mpz
                    sage: ZZ(mpz(42))
                    42

                ::

                    sage: k = GF(2)
                    sage: ZZ((k(0),k(1)), 2)
                    2

                ::

                    sage: ZZ(float(2.0))
                    2
                    sage: ZZ(float(1.0/0.0))
                    Traceback (most recent call last):
                    ...
                    OverflowError: cannot convert float infinity to integer
                    sage: ZZ(float(0.0/0.0))
                    Traceback (most recent call last):
                    ...
                    ValueError: cannot convert float NaN to integer

                ::

                    sage: class MyInt(int):
                    ....:     pass
                    sage: class MyFloat(float):
                    ....:     pass
                    sage: ZZ(MyInt(3))
                    3
                    sage: ZZ(MyFloat(5))
                    5

                ::

                    sage: Integer(\'0\')
                    0
                    sage: Integer(\'0X2AEEF\')
                    175855

                Test conversion from PARI (:issue:`11685`)::

                    sage: # needs sage.libs.pari
                    sage: ZZ(pari(-3))
                    -3
                    sage: ZZ(pari("-3.0"))
                    -3
                    sage: ZZ(pari("-3.5"))
                    Traceback (most recent call last):
                    ...
                    TypeError: Attempt to coerce non-integral real number to an Integer
                    sage: ZZ(pari("1e100"))
                    Traceback (most recent call last):
                    ...
                    PariError: precision too low in truncr (precision loss in truncation)
                    sage: ZZ(pari("10^50"))
                    100000000000000000000000000000000000000000000000000
                    sage: ZZ(pari("Pol(3)"))
                    3
                    sage: ZZ(GF(3^20,\'t\')(1))                                                   # needs sage.rings.finite_rings
                    1
                    sage: ZZ(pari(GF(3^20,\'t\')(1)))                                             # needs sage.rings.finite_rings
                    1
                    sage: x = polygen(QQ)
                    sage: K.<a> = NumberField(x^2 + 3)                                          # needs sage.rings.number_field
                    sage: ZZ(a^2)                                                               # needs sage.rings.number_field
                    -3
                    sage: ZZ(pari(a)^2)                                                         # needs sage.rings.number_field
                    -3
                    sage: ZZ(pari("Mod(x, x^3+x+1)"))   # Note error message refers to lifted element
                    Traceback (most recent call last):
                    ...
                    TypeError: Unable to coerce PARI x to an Integer

                Test coercion of `p`-adic with negative valuation::

                    sage: ZZ(pari(Qp(11)(11^-7)))                                               # needs sage.libs.pari sage.rings.padics
                    Traceback (most recent call last):
                    ...
                    TypeError: cannot convert p-adic with negative valuation to an integer

                Test converting a list with a very large base::

                    sage: a = ZZ(randint(0, 2^128 - 1))
                    sage: L = a.digits(2^64)
                    sage: a == sum([x * 2^(64*i) for i,x in enumerate(L)])
                    True
                    sage: a == ZZ(L, base=2^64)
                    True

                Test comparisons with numpy types (see :issue:`13386` and :issue:`18076`)::

                    sage: # needs numpy
                    sage: import numpy
                    sage: if int(numpy.version.short_version[0]) > 1:
                    ....:     _ = numpy.set_printoptions(legacy="1.25")
                    sage: numpy.int8(\'12\') == 12
                    True
                    sage: 12 == numpy.int8(\'12\')
                    True

                    sage: float(\'15\') == 15
                    True
                    sage: 15 == float(\'15\')
                    True

                Test underscores as digit separators (PEP 515,
                https://www.python.org/dev/peps/pep-0515/)::

                    sage: Integer(\'1_3\')
                    13
                    sage: Integer(b\'1_3\')
                    13
        '''
    @overload
    def additive_order(self) -> Any:
        """Integer.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6105)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: ZZ(0).additive_order()
            1
            sage: ZZ(1).additive_order()
            +Infinity"""
    @overload
    def additive_order(self) -> Any:
        """Integer.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6105)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: ZZ(0).additive_order()
            1
            sage: ZZ(1).additive_order()
            +Infinity"""
    @overload
    def additive_order(self) -> Any:
        """Integer.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6105)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: ZZ(0).additive_order()
            1
            sage: ZZ(1).additive_order()
            +Infinity"""
    @overload
    def as_integer_ratio(self) -> Any:
        """Integer.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4528)

        Return the pair ``(self.numerator(), self.denominator())``,
        which is ``(self, 1)``.

        EXAMPLES::

            sage: x = -12
            sage: x.as_integer_ratio()
            (-12, 1)"""
    @overload
    def as_integer_ratio(self) -> Any:
        """Integer.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4528)

        Return the pair ``(self.numerator(), self.denominator())``,
        which is ``(self, 1)``.

        EXAMPLES::

            sage: x = -12
            sage: x.as_integer_ratio()
            (-12, 1)"""
    @overload
    def balanced_digits(self, base=..., positive_shift=...) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def balanced_digits(self) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def balanced_digits(self, positive_shift=...) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def balanced_digits(self, base) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def balanced_digits(self, base) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def balanced_digits(self, base) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def balanced_digits(self, base, positive_shift=...) -> Any:
        """Integer.balanced_digits(self, base=10, positive_shift=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1609)

        Return the list of balanced digits for ``self`` in the given base.

        The balanced base ``b`` uses ``b`` digits centered around zero. Thus
        if ``b`` is odd, there is only one possibility, namely digits
        between ``-b//2`` and ``b//2`` (both included). For instance in base 9,
        one uses digits from -4 to 4. If ``b`` is even, one has to choose
        between digits from ``-b//2`` to ``b//2 - 1`` or ``-b//2 + 1`` to ``b//2``
        (base 10 for instance: either `-5` to `4` or `-4` to `5`), and this is
        defined by the value of ``positive_shift``.

        INPUT:

        - ``base`` -- integer (default: 10); when ``base`` is 2, only the
          nonnegative or the nonpositive integers can be represented by
          ``balanced_digits``. Thus we say base must be greater than 2.

        - ``positive_shift`` -- boolean (default: ``True``); for even bases, the
          representation uses digits from ``-b//2 + 1`` to ``b//2`` if set to
          ``True``, and from ``-b//2`` to ``b//2 - 1`` otherwise. This has no
          effect for odd bases.

        EXAMPLES::

            sage: 8.balanced_digits(3)
            [-1, 0, 1]
            sage: (-15).balanced_digits(5)
            [0, 2, -1]
            sage: 17.balanced_digits(6)
            [-1, 3]
            sage: 17.balanced_digits(6, positive_shift=False)
            [-1, -3, 1]
            sage: (-46).balanced_digits()
            [4, 5, -1]
            sage: (-46).balanced_digits(positive_shift=False)
            [4, -5]
            sage: (-23).balanced_digits(12)
            [1, -2]
            sage: (-23).balanced_digits(12, positive_shift=False)
            [1, -2]
            sage: 0.balanced_digits(7)
            []
            sage: 14.balanced_digits(5.8)
            Traceback (most recent call last):
            ...
            ValueError: base must be an integer
            sage: 14.balanced_digits(2)
            Traceback (most recent call last):
            ...
            ValueError: base must be > 2

        TESTS::

            sage: base = 5; n = 39
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 12; n = -52
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True
            sage: base = 8; n = 37
            sage: l = n.balanced_digits(base, positive_shift=False)
            sage: sum(l[i]*base^i for i in range(len(l))) == n
            True

        .. SEEALSO::

            :func:`digits <digits>`"""
    @overload
    def binary(self) -> Any:
        """Integer.binary(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1248)

        Return the binary digits of ``self`` as a string.

        EXAMPLES::

            sage: print(Integer(15).binary())
            1111
            sage: print(Integer(16).binary())
            10000
            sage: print(Integer(16938402384092843092843098243).binary())
            1101101011101100011110001110010010100111010001101010001111111000101000000000101111000010000011"""
    @overload
    def binary(self) -> Any:
        """Integer.binary(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1248)

        Return the binary digits of ``self`` as a string.

        EXAMPLES::

            sage: print(Integer(15).binary())
            1111
            sage: print(Integer(16).binary())
            10000
            sage: print(Integer(16938402384092843092843098243).binary())
            1101101011101100011110001110010010100111010001101010001111111000101000000000101111000010000011"""
    @overload
    def binary(self) -> Any:
        """Integer.binary(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1248)

        Return the binary digits of ``self`` as a string.

        EXAMPLES::

            sage: print(Integer(15).binary())
            1111
            sage: print(Integer(16).binary())
            10000
            sage: print(Integer(16938402384092843092843098243).binary())
            1101101011101100011110001110010010100111010001101010001111111000101000000000101111000010000011"""
    @overload
    def binary(self) -> Any:
        """Integer.binary(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1248)

        Return the binary digits of ``self`` as a string.

        EXAMPLES::

            sage: print(Integer(15).binary())
            1111
            sage: print(Integer(16).binary())
            10000
            sage: print(Integer(16938402384092843092843098243).binary())
            1101101011101100011110001110010010100111010001101010001111111000101000000000101111000010000011"""
    def binomial(self, m, algorithm=...) -> Any:
        '''Integer.binomial(self, m, algorithm=\'gmp\')

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7094)

        Return the binomial coefficient "``self`` choose ``m``".

        INPUT:

        - ``m`` -- integer

        - ``algorithm`` -- ``\'gmp\'`` (default), ``\'mpir\'`` (an alias for
          ``gmp``), or ``\'pari\'``; ``\'gmp\'`` is faster for small ``m``,
          and ``\'pari\'`` tends to be faster for large ``m``

        OUTPUT: integer

        EXAMPLES::

            sage: 10.binomial(2)
            45
            sage: 10.binomial(2, algorithm=\'pari\')                                      # needs sage.libs.pari
            45
            sage: 10.binomial(-2)
            0
            sage: (-2).binomial(3)
            -4
            sage: (-3).binomial(0)
            1

        The argument ``m`` or (``self - m``) must fit into an ``unsigned long``::

            sage: (2**256).binomial(2**256)
            1
            sage: (2**256).binomial(2**256 - 1)
            115792089237316195423570985008687907853269984665640564039457584007913129639936
            sage: (2**256).binomial(2**128)
            Traceback (most recent call last):
            ...
            OverflowError: m must fit in an unsigned long

        TESTS::

            sage: 0.binomial(0)
            1
            sage: 0.binomial(1)
            0
            sage: 0.binomial(-1)
            0
            sage: 13.binomial(2r)
            78

        Check that it can be interrupted (:issue:`17852`)::

            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.5): (2^100).binomial(2^22, algorithm=\'mpir\')

        For PARI, we try 10 interrupts with increasing intervals to
        check for reliable interrupting, see :issue:`18919`::

            sage: from cysignals import AlarmInterrupt
            sage: for i in [1..10]:             # long time (5s)                        # needs sage.libs.pari
            ....:     with ensure_interruptible_after(i/11):
            ....:         (2^100).binomial(2^22, algorithm=\'pari\')
            doctest:...: RuntimeWarning: cypari2 leaked ... bytes on the PARI stack...'''
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bit_length(self) -> Any:
        """Integer.bit_length(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1294)

        Return the number of bits required to represent this integer.

        Identical to :meth:`int.bit_length`.

        EXAMPLES::

            sage: 500.bit_length()
            9
            sage: 5.bit_length()
            3
            sage: 0.bit_length() == len(0.bits()) == 0.ndigits(base=2)
            True
            sage: 12345.bit_length() == len(12345.binary())
            True
            sage: 1023.bit_length()
            10
            sage: 1024.bit_length()
            11

        TESTS::

            sage: {ZZ(n).bit_length() == int(n).bit_length() for n in range(-9999, 9999)}
            {True}
            sage: n = randrange(-2^99, 2^99)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^999, 2^999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True
            sage: n = randrange(-2^9999, 2^9999)
            sage: ZZ(n).bit_length() == int(n).bit_length()
            True"""
    @overload
    def bits(self) -> Any:
        '''Integer.bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1263)

        Return the bits in ``self`` as a list, least significant first. The
        result satisfies the identity

        ::

            x == sum(b*2^e for e, b in enumerate(x.bits()))

        Negative numbers will have negative "bits". (So, strictly
        speaking, the entries of the returned list are not really
        members of `\\ZZ/2\\ZZ`.)

        This method just calls :func:`digits` with ``base=2``.

        .. SEEALSO::

            - :meth:`bit_length`, a faster way to compute ``len(x.bits())``
            - :meth:`binary`, which returns a string in perhaps more familiar notation

        EXAMPLES::

            sage: 500.bits()
            [0, 0, 1, 0, 1, 1, 1, 1, 1]
            sage: 11.bits()
            [1, 1, 0, 1]
            sage: (-99).bits()
            [-1, -1, 0, 0, 0, -1, -1]'''
    @overload
    def bits(self) -> Any:
        '''Integer.bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1263)

        Return the bits in ``self`` as a list, least significant first. The
        result satisfies the identity

        ::

            x == sum(b*2^e for e, b in enumerate(x.bits()))

        Negative numbers will have negative "bits". (So, strictly
        speaking, the entries of the returned list are not really
        members of `\\ZZ/2\\ZZ`.)

        This method just calls :func:`digits` with ``base=2``.

        .. SEEALSO::

            - :meth:`bit_length`, a faster way to compute ``len(x.bits())``
            - :meth:`binary`, which returns a string in perhaps more familiar notation

        EXAMPLES::

            sage: 500.bits()
            [0, 0, 1, 0, 1, 1, 1, 1, 1]
            sage: 11.bits()
            [1, 1, 0, 1]
            sage: (-99).bits()
            [-1, -1, 0, 0, 0, -1, -1]'''
    @overload
    def canonical_associate(self) -> Any:
        """Integer.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7227)

        Return a canonical associate.

        EXAMPLES::

            sage: (-2).canonical_associate()
            (2, -1)
            sage: (0).canonical_associate()
            (0, 1)
            sage: a = -17
            sage: b, u = a.canonical_associate()
            sage: b*u == a
            True"""
    @overload
    def canonical_associate(self) -> Any:
        """Integer.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7227)

        Return a canonical associate.

        EXAMPLES::

            sage: (-2).canonical_associate()
            (2, -1)
            sage: (0).canonical_associate()
            (0, 1)
            sage: a = -17
            sage: b, u = a.canonical_associate()
            sage: b*u == a
            True"""
    @overload
    def canonical_associate(self) -> Any:
        """Integer.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7227)

        Return a canonical associate.

        EXAMPLES::

            sage: (-2).canonical_associate()
            (2, -1)
            sage: (0).canonical_associate()
            (0, 1)
            sage: a = -17
            sage: b, u = a.canonical_associate()
            sage: b*u == a
            True"""
    @overload
    def canonical_associate(self) -> Any:
        """Integer.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7227)

        Return a canonical associate.

        EXAMPLES::

            sage: (-2).canonical_associate()
            (2, -1)
            sage: (0).canonical_associate()
            (0, 1)
            sage: a = -17
            sage: b, u = a.canonical_associate()
            sage: b*u == a
            True"""
    @overload
    def ceil(self) -> Any:
        """Integer.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4704)

        Return the ceiling of ``self``, which is ``self`` since ``self`` is an
        integer.

        EXAMPLES::

            sage: n = 6
            sage: n.ceil()
            6"""
    @overload
    def ceil(self) -> Any:
        """Integer.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4704)

        Return the ceiling of ``self``, which is ``self`` since ``self`` is an
        integer.

        EXAMPLES::

            sage: n = 6
            sage: n.ceil()
            6"""
    def class_number(self, proof=...) -> Any:
        """Integer.class_number(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5699)

        Return the class number of the quadratic order with this discriminant.

        INPUT:

        - ``self`` -- integer congruent to `0` or `1` mod `4` which is
          not a square

        - ``proof`` -- boolean (default: ``True``); if ``False``, then
          for negative discriminants a faster algorithm is used by
          the PARI library which is known to give incorrect results
          when the class group has many cyclic factors.  However, the
          results are correct for discriminants `D` with `|D|\\le 2\\cdot10^{10}`.

        OUTPUT:

        (integer) the class number of the quadratic order with this
        discriminant.

        .. NOTE::

           For positive `D`, this is not always equal to the number of classes of
           primitive binary quadratic forms of discriminant `D`, which
           is equal to the narrow class number. The two notions are
           the same when `D<0`, or `D>0` and the fundamental unit of
           the order has negative norm; otherwise the number of
           classes of forms is twice this class number.

        EXAMPLES::

            sage: (-163).class_number()                                                 # needs sage.libs.pari
            1
            sage: (-104).class_number()                                                 # needs sage.libs.pari
            6
            sage: [((4*n + 1), (4*n + 1).class_number()) for n in [21..29]]             # needs sage.libs.pari
            [(85, 2),
            (89, 1),
            (93, 1),
            (97, 1),
            (101, 1),
            (105, 2),
            (109, 1),
            (113, 1),
            (117, 1)]

        TESTS:

        The integer must not be a square, or an error is raised::

           sage: 100.class_number()
           Traceback (most recent call last):
           ...
           ValueError: class_number not defined for square integers


        The integer must be 0 or 1 mod 4, or an error is raised::

           sage: 10.class_number()
           Traceback (most recent call last):
           ...
           ValueError: class_number only defined for integers congruent to 0 or 1 modulo 4
           sage: 3.class_number()
           Traceback (most recent call last):
           ...
           ValueError: class_number only defined for integers congruent to 0 or 1 modulo 4"""
    @overload
    def conjugate(self) -> Any:
        """Integer.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7081)

        Return the complex conjugate of this integer, which is the
        integer itself.

        EXAMPLES::

            sage: n = 205
            sage: n.conjugate()
            205"""
    @overload
    def conjugate(self) -> Any:
        """Integer.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7081)

        Return the complex conjugate of this integer, which is the
        integer itself.

        EXAMPLES::

            sage: n = 205
            sage: n.conjugate()
            205"""
    @overload
    def coprime_integers(self, m) -> Any:
        """Integer.coprime_integers(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4106)

        Return the nonnegative integers `< m` that are coprime to
        this integer.

        EXAMPLES::

            sage: n = 8
            sage: n.coprime_integers(8)
            [1, 3, 5, 7]
            sage: n.coprime_integers(11)
            [1, 3, 5, 7, 9]
            sage: n = 5; n.coprime_integers(10)
            [1, 2, 3, 4, 6, 7, 8, 9]
            sage: n.coprime_integers(5)
            [1, 2, 3, 4]
            sage: n = 99; n.coprime_integers(99)
            [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 46, 47, 49, 50, 52, 53, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 79, 80, 82, 83, 85, 86, 89, 91, 92, 94, 95, 97, 98]

        TESTS::

            sage: 0.coprime_integers(10^100)
            [1]
            sage: 1.coprime_integers(10^100)
            Traceback (most recent call last):
            ...
            OverflowError: bound is too large
            sage: for n in srange(-6, 7):
            ....:     for m in range(-1, 10):
            ....:         assert n.coprime_integers(m) == [k for k in srange(0, m) if gcd(k, n) == 1]

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples

        - David Roe (2017-10-02): Use sieving

        - Jeroen Demeyer (2018-06-25): allow returning zero (only relevant for 1.coprime_integers(n))

        ALGORITHM:

        Create an integer with `m` bits and set bits at every multiple
        of a prime `p` that divides this integer and is less than `m`.
        Then return a list of integers corresponding to the unset bits."""
    @overload
    def coprime_integers(self, m) -> Any:
        """Integer.coprime_integers(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4106)

        Return the nonnegative integers `< m` that are coprime to
        this integer.

        EXAMPLES::

            sage: n = 8
            sage: n.coprime_integers(8)
            [1, 3, 5, 7]
            sage: n.coprime_integers(11)
            [1, 3, 5, 7, 9]
            sage: n = 5; n.coprime_integers(10)
            [1, 2, 3, 4, 6, 7, 8, 9]
            sage: n.coprime_integers(5)
            [1, 2, 3, 4]
            sage: n = 99; n.coprime_integers(99)
            [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 46, 47, 49, 50, 52, 53, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 79, 80, 82, 83, 85, 86, 89, 91, 92, 94, 95, 97, 98]

        TESTS::

            sage: 0.coprime_integers(10^100)
            [1]
            sage: 1.coprime_integers(10^100)
            Traceback (most recent call last):
            ...
            OverflowError: bound is too large
            sage: for n in srange(-6, 7):
            ....:     for m in range(-1, 10):
            ....:         assert n.coprime_integers(m) == [k for k in srange(0, m) if gcd(k, n) == 1]

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples

        - David Roe (2017-10-02): Use sieving

        - Jeroen Demeyer (2018-06-25): allow returning zero (only relevant for 1.coprime_integers(n))

        ALGORITHM:

        Create an integer with `m` bits and set bits at every multiple
        of a prime `p` that divides this integer and is less than `m`.
        Then return a list of integers corresponding to the unset bits."""
    @overload
    def coprime_integers(self, n) -> Any:
        """Integer.coprime_integers(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4106)

        Return the nonnegative integers `< m` that are coprime to
        this integer.

        EXAMPLES::

            sage: n = 8
            sage: n.coprime_integers(8)
            [1, 3, 5, 7]
            sage: n.coprime_integers(11)
            [1, 3, 5, 7, 9]
            sage: n = 5; n.coprime_integers(10)
            [1, 2, 3, 4, 6, 7, 8, 9]
            sage: n.coprime_integers(5)
            [1, 2, 3, 4]
            sage: n = 99; n.coprime_integers(99)
            [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 46, 47, 49, 50, 52, 53, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 79, 80, 82, 83, 85, 86, 89, 91, 92, 94, 95, 97, 98]

        TESTS::

            sage: 0.coprime_integers(10^100)
            [1]
            sage: 1.coprime_integers(10^100)
            Traceback (most recent call last):
            ...
            OverflowError: bound is too large
            sage: for n in srange(-6, 7):
            ....:     for m in range(-1, 10):
            ....:         assert n.coprime_integers(m) == [k for k in srange(0, m) if gcd(k, n) == 1]

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples

        - David Roe (2017-10-02): Use sieving

        - Jeroen Demeyer (2018-06-25): allow returning zero (only relevant for 1.coprime_integers(n))

        ALGORITHM:

        Create an integer with `m` bits and set bits at every multiple
        of a prime `p` that divides this integer and is less than `m`.
        Then return a list of integers corresponding to the unset bits."""
    def crt(self, y, m, n) -> Any:
        """Integer.crt(self, y, m, n)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6987)

        Return the unique integer between `0` and `\\lcm(m,n)` that is congruent
        to the integer modulo `m` and to `y` modulo `n`.

        EXAMPLES::

            sage: n = 17
            sage: m = n.crt(5, 23, 11); m
            247
            sage: m%23
            17
            sage: m%11
            5

        ``crt`` also works for some non-coprime moduli::

            sage: 6.crt(0,10,4)
            16
            sage: 6.crt(0,10,10)
            Traceback (most recent call last):
            ...
            ValueError: no solution to crt problem since gcd(10,10) does not
            divide 6 - 0"""
    @overload
    def denominator(self) -> Any:
        """Integer.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4494)

        Return the denominator of this integer, which of course is
        always 1.

        EXAMPLES::

            sage: x = 5
            sage: x.denominator()
            1
            sage: x = 0
            sage: x.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """Integer.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4494)

        Return the denominator of this integer, which of course is
        always 1.

        EXAMPLES::

            sage: x = 5
            sage: x.denominator()
            1
            sage: x = 0
            sage: x.denominator()
            1"""
    @overload
    def denominator(self) -> Any:
        """Integer.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4494)

        Return the denominator of this integer, which of course is
        always 1.

        EXAMPLES::

            sage: x = 5
            sage: x.denominator()
            1
            sage: x = 0
            sage: x.denominator()
            1"""
    @overload
    def digits(self, base=..., digits=..., padto=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=..., digits=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=..., padto=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=..., padto=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=..., padto=..., digits=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def digits(self, base=...) -> Any:
        '''Integer.digits(self, base=10, digits=None, padto=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1368)

        Return a list of digits for ``self`` in the given base in little
        endian order.

        The returned value is unspecified if ``self`` is a negative number
        and the digits are given.

        INPUT:

        - ``base`` -- integer (default: 10)

        - ``digits`` -- (optional) indexable object as source for
          the digits

        - ``padto`` -- the minimal length of the returned list, sufficient
          number of zeros are added to make the list minimum that length
          (default: 0)

        As a shorthand for ``digits(2)``, you can use :meth:`.bits`.

        Also see :meth:`ndigits`.

        EXAMPLES::

            sage: 17.digits()
            [7, 1]
            sage: 5.digits(base=2, digits=["zero","one"])
            [\'one\', \'zero\', \'one\']
            sage: 5.digits(3)
            [2, 1]
            sage: 0.digits(base=10)  # 0 has 0 digits
            []
            sage: 0.digits(base=2)  # 0 has 0 digits
            []
            sage: 10.digits(16,\'0123456789abcdef\')
            [\'a\']
            sage: 0.digits(16,\'0123456789abcdef\')
            []
            sage: 0.digits(16,\'0123456789abcdef\',padto=1)
            [\'0\']
            sage: 123.digits(base=10,padto=5)
            [3, 2, 1, 0, 0]
            sage: 123.digits(base=2,padto=3)       # padto is the minimal length
            [1, 1, 0, 1, 1, 1, 1]
            sage: 123.digits(base=2,padto=10,digits=(1,-1))
            [-1, -1, 1, -1, -1, -1, -1, 1, 1, 1]
            sage: a=9939082340; a.digits(10)
            [0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
            sage: a.digits(512)
            [100, 302, 26, 74]
            sage: (-12).digits(10)
            [-2, -1]
            sage: (-12).digits(2)
            [0, 0, -1, -1]

        We can sum the digits of an integer in any base::

            sage: sum(14.digits())
            5
            sage: 14.digits(base=2), sum(14.digits(base=2))
            ([0, 1, 1, 1], 3)
            sage: sum(13408967.digits())
            38
            sage: 13408967.digits(base=7), sum(13408967.digits(base=7))
            ([5, 2, 1, 5, 5, 6, 1, 2, 2], 29)
            sage: 13408967.digits(base=1111), sum(13408967.digits(base=1111))
            ([308, 959, 10], 1277)

        We support large bases.

        ::

            sage: n=2^6000
            sage: n.digits(2^3000)
            [0, 0, 1]

        ::

            sage: base=3; n=25
            sage: l=n.digits(base)
            sage: # the next relationship should hold for all n,base
            sage: sum(base^i*l[i] for i in range(len(l)))==n
            True
            sage: base=3; n=-30; l=n.digits(base); sum(base^i*l[i] for i in range(len(l)))==n
            True

        The inverse of this method -- constructing an integer from a
        list of digits and a base -- can be done using the above method
        or by simply using :class:`ZZ()
        <sage.rings.integer_ring.IntegerRing_class>` with a base::

            sage: x = 123; ZZ(x.digits(), 10)
            123
            sage: x == ZZ(x.digits(6), 6)
            True
            sage: x == ZZ(x.digits(25), 25)
            True

        Using :func:`sum` and :func:`enumerate` to do the same thing is
        slightly faster in many cases (and
        :func:`~sage.misc.misc_c.balanced_sum` may be faster yet). Of
        course it gives the same result::

            sage: base = 4
            sage: sum(digit * base^i for i, digit in enumerate(x.digits(base))) == ZZ(x.digits(base), base)
            True

        Note: In some cases it is faster to give a digits collection. This
        would be particularly true for computing the digits of a series of
        small numbers. In these cases, the code is careful to allocate as
        few python objects as reasonably possible.

        ::

            sage: digits = list(range(15))
            sage: l = [ZZ(i).digits(15,digits) for i in range(100)]
            sage: l[16]
            [1, 1]

        This function is comparable to :func:`str` for speed.

        ::

            sage: n=3^100000
            sage: n.digits(base=10)[-1]  # slightly slower than str                     # needs sage.rings.real_interval_field
            1
            sage: n=10^10000
            sage: n.digits(base=10)[-1]  # slightly faster than str                     # needs sage.rings.real_interval_field
            1

        AUTHORS:

        - Joel B. Mohler (2008-03-02):  significantly rewrote this entire function'''
    @overload
    def divide_knowing_divisible_by(self, right) -> Any:
        """Integer.divide_knowing_divisible_by(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4425)

        Return the integer ``self`` / ``right`` when ``self`` is divisible by ``right``.

        If ``self`` is not divisible by right, the return value is undefined,
        and may not even be close to ``self`` / ``right`` for multi-word integers.

        EXAMPLES::

            sage: a = 8; b = 4
            sage: a.divide_knowing_divisible_by(b)
            2
            sage: (100000).divide_knowing_divisible_by(25)
            4000
            sage: (100000).divide_knowing_divisible_by(26) # close (random)
            3846

        However, often it's way off.

        ::

            sage: a = 2^70; a
            1180591620717411303424
            sage: a // 11  # floor divide
            107326510974310118493
            sage: a.divide_knowing_divisible_by(11) # way off and possibly random
            43215361478743422388970455040"""
    @overload
    def divide_knowing_divisible_by(self, b) -> Any:
        """Integer.divide_knowing_divisible_by(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4425)

        Return the integer ``self`` / ``right`` when ``self`` is divisible by ``right``.

        If ``self`` is not divisible by right, the return value is undefined,
        and may not even be close to ``self`` / ``right`` for multi-word integers.

        EXAMPLES::

            sage: a = 8; b = 4
            sage: a.divide_knowing_divisible_by(b)
            2
            sage: (100000).divide_knowing_divisible_by(25)
            4000
            sage: (100000).divide_knowing_divisible_by(26) # close (random)
            3846

        However, often it's way off.

        ::

            sage: a = 2^70; a
            1180591620717411303424
            sage: a // 11  # floor divide
            107326510974310118493
            sage: a.divide_knowing_divisible_by(11) # way off and possibly random
            43215361478743422388970455040"""
    def divides(self, n) -> Any:
        """Integer.divides(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4201)

        Return ``True`` if ``self`` divides ``n``.

        EXAMPLES::

            sage: Z = IntegerRing()
            sage: Z(5).divides(Z(10))
            True
            sage: Z(0).divides(Z(5))
            False
            sage: Z(10).divides(Z(5))
            False"""
    @overload
    def divisors(self, method=...) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def divisors(self, method=...) -> Any:
        """Integer.divisors(self, method=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3030)

        Return the list of all positive integer divisors of this integer,
        sorted in increasing order.

        EXAMPLES:

        ::

            sage: (-3).divisors()
            [1, 3]
            sage: 6.divisors()
            [1, 2, 3, 6]
            sage: 28.divisors()
            [1, 2, 4, 7, 14, 28]
            sage: (2^5).divisors()
            [1, 2, 4, 8, 16, 32]
            sage: 100.divisors()
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            sage: 1.divisors()
            [1]
            sage: 0.divisors()
            Traceback (most recent call last):
            ...
            ValueError: n must be nonzero
            sage: (2^3 * 3^2 * 17).divisors()
            [1, 2, 3, 4, 6, 8, 9, 12, 17, 18, 24, 34, 36, 51, 68, 72,
            102, 136, 153, 204, 306, 408, 612, 1224]
            sage: a = odd_part(factorial(31))
            sage: v = a.divisors()                                                      # needs sage.libs.pari
            sage: len(v)                                                                # needs sage.libs.pari
            172800
            sage: prod(e + 1 for p, e in factor(a))                                     # needs sage.libs.pari
            172800
            sage: all(t.divides(a) for t in v)                                          # needs sage.libs.pari
            True

        ::

            sage: n = 2^551 - 1
            sage: L = n.divisors()                                                      # needs sage.libs.pari
            sage: len(L)                                                                # needs sage.libs.pari
            256
            sage: L[-1] == n                                                            # needs sage.libs.pari
            True

        TESTS:

        Overflow::

            sage: prod(primes_first_n(64)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large
            sage: prod(primes_first_n(58)).divisors()                                   # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            OverflowError: value too large                                 # 32-bit
            MemoryError: failed to allocate 288230376151711744 * 24 bytes  # 64-bit

        Check for memory leaks and ability to interrupt
        (the ``divisors`` call below allocates about 800 MB every time,
        so a memory leak will not go unnoticed)::

            sage: n = prod(primes_first_n(25))                                          # needs sage.libs.pari
            sage: for i in range(20):           # long time                             # needs sage.libs.pari
            ....:     try:
            ....:         alarm(RDF.random_element(1e-3, 0.5))
            ....:         _ = n.divisors()
            ....:         cancel_alarm()  # we never get here
            ....:     except AlarmInterrupt:
            ....:         pass

        Test a strange method::

            sage: 100.divisors(method='hey')
            Traceback (most recent call last):
            ...
            ValueError: method must be 'pari' or 'sage'


        .. NOTE::

           If one first computes all the divisors and then sorts it,
           the sorting step can easily dominate the runtime. Note,
           however, that (nonnegative) multiplication on the left
           preserves relative order. One can leverage this fact to
           keep the list in order as one computes it using a process
           similar to that of the merge sort algorithm."""
    @overload
    def euclidean_degree(self) -> Any:
        """Integer.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3302)

        Return the degree of this element as an element of a Euclidean domain.

        If this is an element in the ring of integers, this is simply its
        absolute value.

        EXAMPLES::

            sage: ZZ(1).euclidean_degree()
            1"""
    @overload
    def euclidean_degree(self) -> Any:
        """Integer.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3302)

        Return the degree of this element as an element of a Euclidean domain.

        If this is an element in the ring of integers, this is simply its
        absolute value.

        EXAMPLES::

            sage: ZZ(1).euclidean_degree()
            1"""
    def exact_log(self, m) -> Any:
        """Integer.exact_log(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2625)

        Return the largest integer `k` such that `m^k \\leq \\text{self}`,
        i.e., the floor of `\\log_m(\\text{self})`.

        This is guaranteed to return the correct answer even when the usual
        log function doesn't have sufficient precision.

        INPUT:

        - ``m`` -- integer `\\geq 2`

        AUTHORS:

        - David Harvey (2006-09-15)
        - Joel B. Mohler (2009-04-08) -- rewrote this to handle small cases
          and/or easy cases up to 100x faster..

        EXAMPLES::

            sage: Integer(125).exact_log(5)
            3
            sage: Integer(124).exact_log(5)
            2
            sage: Integer(126).exact_log(5)
            3
            sage: Integer(3).exact_log(5)
            0
            sage: Integer(1).exact_log(5)
            0
            sage: Integer(178^1700).exact_log(178)
            1700
            sage: Integer(178^1700-1).exact_log(178)
            1699
            sage: Integer(178^1700+1).exact_log(178)
            1700
            sage: # we need to exercise the large base code path too
            sage: Integer(1780^1700-1).exact_log(1780)                                  # needs sage.rings.real_interval_field
            1699

            sage: # The following are very very fast.
            sage: # Note that for base m a perfect power of 2, we get the exact log by counting bits.
            sage: n = 2983579823750185701375109835; m = 32
            sage: n.exact_log(m)
            18
            sage: # The next is a favorite of mine.  The log2 approximate is exact and immediately provable.
            sage: n = 90153710570912709517902579010793251709257901270941709247901209742124
            sage: m = 213509721309572
            sage: n.exact_log(m)
            4

        ::

            sage: # needs sage.rings.real_mpfr
            sage: x = 3^100000
            sage: RR(log(RR(x), 3))
            100000.000000000
            sage: RR(log(RR(x + 100000), 3))
            100000.000000000

        ::

            sage: # needs sage.rings.real_mpfr
            sage: x.exact_log(3)
            100000
            sage: (x + 1).exact_log(3)
            100000
            sage: (x - 1).exact_log(3)
            99999

        ::

            sage: # needs sage.rings.real_mpfr
            sage: x.exact_log(2.5)
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer"""
    @overload
    def exp(self, prec=...) -> Any:
        """Integer.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2906)

        Return the exponential function of ``self`` as a real number.

        This function is provided only so that Sage integers may be treated
        in the same manner as real numbers when convenient.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(8).exp()                                                      # needs sage.symbolic
            e^8
            sage: Integer(8).exp(prec=100)                                              # needs sage.symbolic
            2980.9579870417282747435920995
            sage: exp(Integer(8))                                                       # needs sage.symbolic
            e^8

        For even fairly large numbers, this may not be useful.

        ::

            sage: y = Integer(145^145)
            sage: y.exp()                                                               # needs sage.symbolic
            e^25024207011349079210459585279553675697932183658421565260323592409432707306554163224876110094014450895759296242775250476115682350821522931225499163750010280453185147546962559031653355159703678703793369785727108337766011928747055351280379806937944746847277089168867282654496776717056860661614337004721164703369140625
            sage: y.exp(prec=53)  # default RealField precision                         # needs sage.symbolic
            +infinity"""
    @overload
    def exp(self) -> Any:
        """Integer.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2906)

        Return the exponential function of ``self`` as a real number.

        This function is provided only so that Sage integers may be treated
        in the same manner as real numbers when convenient.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(8).exp()                                                      # needs sage.symbolic
            e^8
            sage: Integer(8).exp(prec=100)                                              # needs sage.symbolic
            2980.9579870417282747435920995
            sage: exp(Integer(8))                                                       # needs sage.symbolic
            e^8

        For even fairly large numbers, this may not be useful.

        ::

            sage: y = Integer(145^145)
            sage: y.exp()                                                               # needs sage.symbolic
            e^25024207011349079210459585279553675697932183658421565260323592409432707306554163224876110094014450895759296242775250476115682350821522931225499163750010280453185147546962559031653355159703678703793369785727108337766011928747055351280379806937944746847277089168867282654496776717056860661614337004721164703369140625
            sage: y.exp(prec=53)  # default RealField precision                         # needs sage.symbolic
            +infinity"""
    @overload
    def exp(self, prec=...) -> Any:
        """Integer.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2906)

        Return the exponential function of ``self`` as a real number.

        This function is provided only so that Sage integers may be treated
        in the same manner as real numbers when convenient.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(8).exp()                                                      # needs sage.symbolic
            e^8
            sage: Integer(8).exp(prec=100)                                              # needs sage.symbolic
            2980.9579870417282747435920995
            sage: exp(Integer(8))                                                       # needs sage.symbolic
            e^8

        For even fairly large numbers, this may not be useful.

        ::

            sage: y = Integer(145^145)
            sage: y.exp()                                                               # needs sage.symbolic
            e^25024207011349079210459585279553675697932183658421565260323592409432707306554163224876110094014450895759296242775250476115682350821522931225499163750010280453185147546962559031653355159703678703793369785727108337766011928747055351280379806937944746847277089168867282654496776717056860661614337004721164703369140625
            sage: y.exp(prec=53)  # default RealField precision                         # needs sage.symbolic
            +infinity"""
    @overload
    def exp(self) -> Any:
        """Integer.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2906)

        Return the exponential function of ``self`` as a real number.

        This function is provided only so that Sage integers may be treated
        in the same manner as real numbers when convenient.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(8).exp()                                                      # needs sage.symbolic
            e^8
            sage: Integer(8).exp(prec=100)                                              # needs sage.symbolic
            2980.9579870417282747435920995
            sage: exp(Integer(8))                                                       # needs sage.symbolic
            e^8

        For even fairly large numbers, this may not be useful.

        ::

            sage: y = Integer(145^145)
            sage: y.exp()                                                               # needs sage.symbolic
            e^25024207011349079210459585279553675697932183658421565260323592409432707306554163224876110094014450895759296242775250476115682350821522931225499163750010280453185147546962559031653355159703678703793369785727108337766011928747055351280379806937944746847277089168867282654496776717056860661614337004721164703369140625
            sage: y.exp(prec=53)  # default RealField precision                         # needs sage.symbolic
            +infinity"""
    @overload
    def exp(self, prec=...) -> Any:
        """Integer.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2906)

        Return the exponential function of ``self`` as a real number.

        This function is provided only so that Sage integers may be treated
        in the same manner as real numbers when convenient.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(8).exp()                                                      # needs sage.symbolic
            e^8
            sage: Integer(8).exp(prec=100)                                              # needs sage.symbolic
            2980.9579870417282747435920995
            sage: exp(Integer(8))                                                       # needs sage.symbolic
            e^8

        For even fairly large numbers, this may not be useful.

        ::

            sage: y = Integer(145^145)
            sage: y.exp()                                                               # needs sage.symbolic
            e^25024207011349079210459585279553675697932183658421565260323592409432707306554163224876110094014450895759296242775250476115682350821522931225499163750010280453185147546962559031653355159703678703793369785727108337766011928747055351280379806937944746847277089168867282654496776717056860661614337004721164703369140625
            sage: y.exp(prec=53)  # default RealField precision                         # needs sage.symbolic
            +infinity"""
    def factor(self, algorithm=..., proof=..., limit=..., int_=..., verbose=...) -> Any:
        """Integer.factor(self, algorithm='pari', proof=None, limit=None, int_=False, verbose=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3879)

        Return the prime factorization of this integer as a
        formal Factorization object.

        INPUT:

        - ``algorithm`` -- string; one of

          - ``'pari'`` -- (default) use the PARI library

          - ``'flint'`` -- use the FLINT library

          - ``'kash'`` -- use the KASH computer algebra system (requires
            kash)

          - ``'magma'`` -- use the MAGMA computer algebra system (requires
            an installation of MAGMA)

          - ``'qsieve'`` -- use Bill Hart's quadratic sieve code;
            WARNING: this may not work as expected, see qsieve? for
            more information

          - ``'ecm'`` -- use ECM-GMP, an implementation of Hendrik
            Lenstra's elliptic curve method

        - ``proof`` -- boolean (default: ``True``); whether or not to prove
          primality of each factor (only applicable for ``'pari'`` and ``'ecm'``)

        - ``limit`` -- integer or ``None`` (default: ``None``); if limit is
          given it must fit in a ``signed int``, and the factorization is done
          using trial division and primes up to limit

        OUTPUT: a Factorization object containing the prime factors and
        their multiplicities

        EXAMPLES::

            sage: n = 2^100 - 1; n.factor()                                             # needs sage.libs.pari
            3 * 5^3 * 11 * 31 * 41 * 101 * 251 * 601 * 1801 * 4051 * 8101 * 268501

        This factorization can be converted into a list of pairs `(p,
        e)`, where `p` is prime and `e` is a positive integer.  Each
        pair can also be accessed directly by its index (ordered by
        increasing size of the prime)::

            sage: f = 60.factor()
            sage: list(f)
            [(2, 2), (3, 1), (5, 1)]
            sage: f[2]
            (5, 1)

        Similarly, the factorization can be converted to a dictionary
        so the exponent can be extracted for each prime::

            sage: f = (3^6).factor()
            sage: dict(f)
            {3: 6}
            sage: dict(f)[3]
            6

        We use ``proof=False``, which doesn't prove correctness of the primes
        that appear in the factorization::

            sage: n = 920384092842390423848290348203948092384082349082
            sage: n.factor(proof=False)                                                 # needs sage.libs.pari
            2 * 11 * 1531 * 4402903 * 10023679 * 619162955472170540533894518173
            sage: n.factor(proof=True)                                                  # needs sage.libs.pari
            2 * 11 * 1531 * 4402903 * 10023679 * 619162955472170540533894518173

        We factor using trial division only::

            sage: n.factor(limit=1000)
            2 * 11 * 41835640583745019265831379463815822381094652231

        An example where FLINT is used::

            sage: n = 82862385732327628428164127822
            sage: n.factor(algorithm='flint')                                           # needs sage.libs.flint
            2 * 3 * 11 * 13 * 41 * 73 * 22650083 * 1424602265462161

        We factor using a quadratic sieve algorithm::

            sage: # needs sage.libs.pari
            sage: p = next_prime(10^20)
            sage: q = next_prime(10^21)
            sage: n = p * q
            sage: n.factor(algorithm='qsieve')                                          # needs sage.libs.flint
            doctest:... RuntimeWarning: the factorization returned
            by qsieve may be incomplete (the factors may not be prime)
            or even wrong; see qsieve? for details
            100000000000000000039 * 1000000000000000000117

        We factor using the elliptic curve method::

            sage: # needs sage.libs.pari
            sage: p = next_prime(10^15)
            sage: q = next_prime(10^21)
            sage: n = p * q
            sage: n.factor(algorithm='ecm')
            1000000000000037 * 1000000000000000000117

        TESTS::

            sage: n = 42
            sage: n.factor(algorithm='foobar')
            Traceback (most recent call last):
            ...
            ValueError: Algorithm is not known"""
    def factorial(self) -> Any:
        '''Integer.factorial(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4541)

        Return the factorial `n! = 1 \\cdot 2 \\cdot 3 \\cdots n`.

        If the input does not fit in an ``unsigned long int``, an :exc:`OverflowError`
        is raised.

        EXAMPLES::

            sage: for n in srange(7):
            ....:     print("{} {}".format(n, n.factorial()))
            0 1
            1 1
            2 2
            3 6
            4 24
            5 120
            6 720

        Large integers raise an :exc:`OverflowError`::

            sage: (2**64).factorial()
            Traceback (most recent call last):
            ...
            OverflowError: argument too large for factorial

        And negative ones a :exc:`ValueError`::

            sage: (-1).factorial()
            Traceback (most recent call last):
            ...
            ValueError: factorial only defined for nonnegative integers'''
    @overload
    def floor(self) -> Any:
        """Integer.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4691)

        Return the floor of ``self``, which is just ``self`` since ``self`` is an
        integer.

        EXAMPLES::

            sage: n = 6
            sage: n.floor()
            6"""
    @overload
    def floor(self) -> Any:
        """Integer.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4691)

        Return the floor of ``self``, which is just ``self`` since ``self`` is an
        integer.

        EXAMPLES::

            sage: n = 6
            sage: n.floor()
            6"""
    def gamma(self) -> Any:
        """Integer.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4669)

        The gamma function on integers is the factorial function (shifted by
        one) on positive integers, and `\\pm \\infty` on nonpositive integers.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: gamma(5)
            24
            sage: gamma(0)
            Infinity
            sage: gamma(-1)
            Infinity
            sage: gamma(-2^150)
            Infinity"""
    def global_height(self, prec=...) -> Any:
        """Integer.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4916)

        Return the absolute logarithmic height of this rational integer.

        INPUT:

        - ``prec`` -- integer; desired floating point precision (default:
          default RealField precision)

        OUTPUT:

        (real) The absolute logarithmic height of this rational integer.

        ALGORITHM:

        The height of the integer `n` is `\\log |n|`.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: ZZ(5).global_height()
            1.60943791243410
            sage: ZZ(-2).global_height(prec=100)
            0.69314718055994530941723212146
            sage: exp(_)
            2.0000000000000000000000000000"""
    @overload
    def hex(self) -> Any:
        """Integer.hex(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1184)

        Return the hexadecimal digits of ``self`` in lower case.

        .. NOTE::

           '0x' is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(15).hex())
            f
            sage: print(Integer(16).hex())
            10
            sage: print(Integer(16938402384092843092843098243).hex())
            36bb1e3929d1a8fe2802f083"""
    @overload
    def hex(self) -> Any:
        """Integer.hex(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1184)

        Return the hexadecimal digits of ``self`` in lower case.

        .. NOTE::

           '0x' is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(15).hex())
            f
            sage: print(Integer(16).hex())
            10
            sage: print(Integer(16938402384092843092843098243).hex())
            36bb1e3929d1a8fe2802f083"""
    @overload
    def hex(self) -> Any:
        """Integer.hex(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1184)

        Return the hexadecimal digits of ``self`` in lower case.

        .. NOTE::

           '0x' is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(15).hex())
            f
            sage: print(Integer(16).hex())
            10
            sage: print(Integer(16938402384092843092843098243).hex())
            36bb1e3929d1a8fe2802f083"""
    @overload
    def hex(self) -> Any:
        """Integer.hex(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1184)

        Return the hexadecimal digits of ``self`` in lower case.

        .. NOTE::

           '0x' is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(15).hex())
            f
            sage: print(Integer(16).hex())
            10
            sage: print(Integer(16938402384092843092843098243).hex())
            36bb1e3929d1a8fe2802f083"""
    @overload
    def imag(self) -> Any:
        """Integer.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4756)

        Return the imaginary part of ``self``, which is zero.

        EXAMPLES::

            sage: Integer(9).imag()
            0"""
    @overload
    def imag(self) -> Any:
        """Integer.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4756)

        Return the imaginary part of ``self``, which is zero.

        EXAMPLES::

            sage: Integer(9).imag()
            0"""
    def inverse_mod(self, n) -> Any:
        """Integer.inverse_mod(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6925)

        Return the inverse of ``self`` modulo `n`, if this inverse exists.

        Otherwise, raise a :exc:`ZeroDivisionError` exception.

        INPUT:

        - ``self`` -- integer

        - ``n`` -- integer or ideal of integer ring

        OUTPUT:

        - ``x`` -- integer such that x * ``self`` = 1 (mod m), or
          raises :exc:`ZeroDivisionError`

        IMPLEMENTATION:

        Call the ``mpz_invert`` GMP library function.

        EXAMPLES::

            sage: a = Integer(189)
            sage: a.inverse_mod(10000)
            4709
            sage: a.inverse_mod(-10000)
            4709
            sage: a.inverse_mod(1890)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(189, 1890) does not exist
            sage: a = Integer(19)**100000  # long time
            sage: c = a.inverse_mod(a*a)   # long time
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(..., ...) does not exist

        We check that :issue:`10625` is fixed::

            sage: ZZ(2).inverse_mod(ZZ.ideal(3))
            2

        We check that :issue:`9955` is fixed::

            sage: Rational(3) % Rational(-1)
            0"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Integer.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6900)

        Return inverse of ``self`` if ``self`` is a unit in the integers, i.e.,
        ``self`` is `-1` or `1`. Otherwise, raise a :exc:`ZeroDivisionError`.

        EXAMPLES::

            sage: (1).inverse_of_unit()
            1
            sage: (-1).inverse_of_unit()
            -1
            sage: 5.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist
            sage: 0.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Integer.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6900)

        Return inverse of ``self`` if ``self`` is a unit in the integers, i.e.,
        ``self`` is `-1` or `1`. Otherwise, raise a :exc:`ZeroDivisionError`.

        EXAMPLES::

            sage: (1).inverse_of_unit()
            1
            sage: (-1).inverse_of_unit()
            -1
            sage: 5.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist
            sage: 0.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Integer.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6900)

        Return inverse of ``self`` if ``self`` is a unit in the integers, i.e.,
        ``self`` is `-1` or `1`. Otherwise, raise a :exc:`ZeroDivisionError`.

        EXAMPLES::

            sage: (1).inverse_of_unit()
            1
            sage: (-1).inverse_of_unit()
            -1
            sage: 5.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist
            sage: 0.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Integer.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6900)

        Return inverse of ``self`` if ``self`` is a unit in the integers, i.e.,
        ``self`` is `-1` or `1`. Otherwise, raise a :exc:`ZeroDivisionError`.

        EXAMPLES::

            sage: (1).inverse_of_unit()
            1
            sage: (-1).inverse_of_unit()
            -1
            sage: 5.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist
            sage: 0.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Integer.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6900)

        Return inverse of ``self`` if ``self`` is a unit in the integers, i.e.,
        ``self`` is `-1` or `1`. Otherwise, raise a :exc:`ZeroDivisionError`.

        EXAMPLES::

            sage: (1).inverse_of_unit()
            1
            sage: (-1).inverse_of_unit()
            -1
            sage: 5.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist
            sage: 0.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: inverse does not exist"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_discriminant(self) -> Any:
        """Integer.is_discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6159)

        Return ``True`` if this integer is a discriminant.

        .. NOTE::

            A discriminant is an integer congruent to 0 or 1 modulo 4.

        EXAMPLES::

            sage: (-1).is_discriminant()
            False
            sage: (-4).is_discriminant()
            True
            sage: 100.is_discriminant()
            True
            sage: 101.is_discriminant()
            True

        TESTS::

            sage: 0.is_discriminant()
            True
            sage: 1.is_discriminant()
            True
            sage: len([D for D in srange(-100,100) if D.is_discriminant()])
            100"""
    @overload
    def is_fundamental_discriminant(self) -> bool:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_fundamental_discriminant(self) -> Any:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_fundamental_discriminant(self) -> Any:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_fundamental_discriminant(self) -> Any:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_fundamental_discriminant(self) -> Any:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_fundamental_discriminant(self) -> Any:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_fundamental_discriminant(self) -> Any:
        """Integer.is_fundamental_discriminant(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6189)

        Return ``True`` if this integer is a fundamental discriminant.

        .. NOTE::

            A fundamental discriminant is a discriminant, not 0 or 1
            and not a square multiple of a smaller discriminant.

        EXAMPLES::

            sage: (-4).is_fundamental_discriminant()                                    # needs sage.libs.pari
            True
            sage: (-12).is_fundamental_discriminant()
            False
            sage: 101.is_fundamental_discriminant()                                     # needs sage.libs.pari
            True

        TESTS::

            sage: 0.is_fundamental_discriminant()
            False
            sage: 1.is_fundamental_discriminant()
            False
            sage: len([D for D in srange(-100,100)                                      # needs sage.libs.pari
            ....:      if D.is_fundamental_discriminant()])
            61"""
    @overload
    def is_integer(self) -> Any:
        """Integer.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4816)

        Return ``True`` as they are integers.

        EXAMPLES::

            sage: sqrt(4).is_integer()
            True"""
    @overload
    def is_integer(self) -> Any:
        """Integer.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4816)

        Return ``True`` as they are integers.

        EXAMPLES::

            sage: sqrt(4).is_integer()
            True"""
    @overload
    def is_integral(self) -> Any:
        """Integer.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4793)

        Return ``True`` since integers are integral, i.e.,
        satisfy a monic polynomial with integer coefficients.

        EXAMPLES::

            sage: Integer(3).is_integral()
            True"""
    @overload
    def is_integral(self) -> Any:
        """Integer.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4793)

        Return ``True`` since integers are integral, i.e.,
        satisfy a monic polynomial with integer coefficients.

        EXAMPLES::

            sage: Integer(3).is_integral()
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Integer.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5448)

        Return ``True`` if ``self`` is irreducible, i.e. +/-
        prime

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_irreducible()                                                    # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_irreducible()
            False
            sage: z = 7
            sage: z.is_irreducible()
            True
            sage: z = -7
            sage: z.is_irreducible()
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Integer.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5448)

        Return ``True`` if ``self`` is irreducible, i.e. +/-
        prime

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_irreducible()                                                    # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_irreducible()
            False
            sage: z = 7
            sage: z.is_irreducible()
            True
            sage: z = -7
            sage: z.is_irreducible()
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Integer.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5448)

        Return ``True`` if ``self`` is irreducible, i.e. +/-
        prime

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_irreducible()                                                    # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_irreducible()
            False
            sage: z = 7
            sage: z.is_irreducible()
            True
            sage: z = -7
            sage: z.is_irreducible()
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Integer.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5448)

        Return ``True`` if ``self`` is irreducible, i.e. +/-
        prime

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_irreducible()                                                    # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_irreducible()
            False
            sage: z = 7
            sage: z.is_irreducible()
            True
            sage: z = -7
            sage: z.is_irreducible()
            True"""
    @overload
    def is_irreducible(self) -> Any:
        """Integer.is_irreducible(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5448)

        Return ``True`` if ``self`` is irreducible, i.e. +/-
        prime

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_irreducible()                                                    # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_irreducible()
            False
            sage: z = 7
            sage: z.is_irreducible()
            True
            sage: z = -7
            sage: z.is_irreducible()
            True"""
    @overload
    def is_norm(self, K, element=..., proof=...) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, QQ) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, QQ, element=...) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, K) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, K) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, K, element=...) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, K, element=...) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_norm(self, K, element=...) -> Any:
        """Integer.is_norm(self, K, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5590)

        See ``QQ(self).is_norm()``.

        EXAMPLES::

            sage: n = 7
            sage: n.is_norm(QQ)
            True
            sage: n.is_norm(QQ, element=True)
            (True, 7)

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: n = 4
            sage: n.is_norm(K)
            True
            sage: 5.is_norm(K)
            False
            sage: n.is_norm(K, element=True)
            (True, -4*beta + 6)
            sage: n.is_norm(K, element=True)[1].norm()
            4
            sage: n = 5
            sage: n.is_norm(K, element=True)
            (False, None)"""
    @overload
    def is_one(self) -> Any:
        """Integer.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4767)

        Return ``True`` if the integer is `1`, otherwise ``False``.

        EXAMPLES::

            sage: Integer(1).is_one()
            True
            sage: Integer(0).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Integer.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4767)

        Return ``True`` if the integer is `1`, otherwise ``False``.

        EXAMPLES::

            sage: Integer(1).is_one()
            True
            sage: Integer(0).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Integer.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4767)

        Return ``True`` if the integer is `1`, otherwise ``False``.

        EXAMPLES::

            sage: Integer(1).is_one()
            True
            sage: Integer(0).is_one()
            False"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Integer.is_perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5534)

        Return ``True`` if ``self`` is a perfect power, ie if there exist integers
        `a` and `b`, `b > 1` with ``self`` `= a^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_power_of`: If you know the base already, this method is
              the fastest option.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(-27).is_perfect_power()
            True
            sage: Integer(12).is_perfect_power()
            False

            sage: z = 8
            sage: z.is_perfect_power()
            True
            sage: 144.is_perfect_power()
            True
            sage: 10.is_perfect_power()
            False
            sage: (-8).is_perfect_power()
            True
            sage: (-4).is_perfect_power()
            False

        TESTS:

        This is a test to make sure we work around a bug in GMP, see
        :issue:`4612`.

        ::

            sage: [ -a for a in srange(100) if not (-a^3).is_perfect_power() ]
            []"""
    def is_power_of(self, n) -> Any:
        """Integer.is_power_of(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5072)

        Return ``True`` if there is an integer `b` with
        `\\mathtt{self} = n^b`.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which this
              integer is a perfect power.
            - :meth:`is_perfect_power`: If you don't know the base but just
              want to know if this integer is a perfect power, use this
              function.
            - :meth:`is_prime_power`: Checks whether the base is prime.

        EXAMPLES::

            sage: Integer(64).is_power_of(4)
            True
            sage: Integer(64).is_power_of(16)
            False

        TESTS::

            sage: Integer(-64).is_power_of(-4)
            True
            sage: Integer(-32).is_power_of(-2)
            True
            sage: Integer(1).is_power_of(1)
            True
            sage: Integer(-1).is_power_of(-1)
            True
            sage: Integer(0).is_power_of(1)
            False
            sage: Integer(0).is_power_of(0)
            True
            sage: Integer(1).is_power_of(0)
            True
            sage: Integer(1).is_power_of(8)
            True
            sage: Integer(-8).is_power_of(2)
            False
            sage: Integer(-81).is_power_of(-3)
            False

        .. NOTE::

           For large integers ``self``, :meth:`is_power_of` is faster than
           :meth:`is_perfect_power`. The following examples give some indication of
           how much faster.

        ::

            sage: b = lcm(range(1,10000))
            sage: b.exact_log(2)
            14446
            sage: t = cputime()
            sage: for a in range(2, 1000): k = b.is_perfect_power()
            sage: cputime(t)      # random
            0.53203299999999976
            sage: t = cputime()
            sage: for a in range(2, 1000): k = b.is_power_of(2)
            sage: cputime(t)      # random
            0.0
            sage: t = cputime()
            sage: for a in range(2, 1000): k = b.is_power_of(3)
            sage: cputime(t)      # random
            0.032002000000000308

        ::

            sage: b = lcm(range(1, 1000))
            sage: b.exact_log(2)
            1437
            sage: t = cputime()
            sage: for a in range(2, 10000):  # note: changed range from the example above
            ....:     k = b.is_perfect_power()
            sage: cputime(t)      # random
            0.17201100000000036
            sage: t = cputime(); TWO = int(2)
            sage: for a in range(2, 10000): k = b.is_power_of(TWO)
            sage: cputime(t)      # random
            0.0040000000000000036
            sage: t = cputime()
            sage: for a in range(2, 10000): k = b.is_power_of(3)
            sage: cputime(t)      # random
            0.040003000000000011
            sage: t = cputime()
            sage: for a in range(2, 10000): k = b.is_power_of(a)
            sage: cputime(t)      # random
            0.02800199999999986"""
    @overload
    def is_prime(self, proof=...) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self, proof=...) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self, proof=...) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    @overload
    def is_prime(self) -> Any:
        '''Integer.is_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5323)

        Test whether ``self`` is prime.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a
          strong pseudo-primality test (see :meth:`is_pseudoprime`).
          If ``True``, use a provable primality test.  If unset, use the
          :mod:`default arithmetic proof flag <sage.structure.proof.proof>`.

        .. NOTE::

           Integer primes are by definition *positive*! This is
           different than Magma, but the same as in PARI. See also the
           :meth:`is_irreducible()` method.

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_prime()                                                          # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_prime()
            False
            sage: z = 7
            sage: z.is_prime()
            True
            sage: z = -7
            sage: z.is_prime()
            False
            sage: z.is_irreducible()
            True

        ::

            sage: z = 10^80 + 129
            sage: z.is_prime(proof=False)                                               # needs sage.libs.pari
            True
            sage: z.is_prime(proof=True)                                                # needs sage.libs.pari
            True

        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows::

            sage: proof.arithmetic()
            True
            sage: n = 10^100 + 267
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            5 loops, best of 3: 163 ms per loop
            sage: proof.arithmetic(False)
            sage: proof.arithmetic()
            False
            sage: timeit("n.is_prime()")        # not tested                            # needs sage.libs.pari
            1000 loops, best of 3: 573 us per loop

        ALGORITHM:

        Calls the PARI function :pari:`isprime`.

        TESTS:

        We compare the output of this method to a straightforward sieve::

            sage: size = 10000
            sage: tab = [0,0] + [1] * (size-2)
            sage: for i in range(size):
            ....:     if tab[i]:
            ....:         for j in range(2*i, size, i):
            ....:             tab[j] = 0
            sage: all(ZZ(i).is_prime() == b for i,b in enumerate(tab))                  # needs sage.libs.pari
            True'''
    def is_prime_power(self, proof=..., boolget_data=...) -> Any:
        """Integer.is_prime_power(self, *, proof=None, bool get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5167)

        Return ``True`` if this integer is a prime power, and ``False`` otherwise.

        A prime power is a prime number raised to a positive power. Hence `1` is
        not a prime power.

        For a method that uses a pseudoprimality test instead see
        :meth:`is_pseudoprime_power`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default). If ``False``, use a strong
          pseudo-primality test (see :meth:`is_pseudoprime`).  If ``True``, use
          a provable primality test. If unset, use the default arithmetic proof
          flag.

        - ``get_data`` -- (default: ``False``), if ``True`` return a pair
          ``(p,k)`` such that this integer equals ``p^k`` with ``p`` a prime
          and ``k`` a positive integer or the pair ``(self,0)`` otherwise.

        .. SEEALSO::

            - :meth:`perfect_power`: Finds the minimal base for which integer
              is a perfect power.
            - :meth:`is_perfect_power`: Doesn't test whether the base is prime.
            - :meth:`is_power_of`: If you know the base already this method is
              the fastest option.
            - :meth:`is_pseudoprime_power`: If the entry is very large.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 17.is_prime_power()
            True
            sage: 10.is_prime_power()
            False
            sage: 64.is_prime_power()
            True
            sage: (3^10000).is_prime_power()
            True
            sage: (10000).is_prime_power()
            False
            sage: (-3).is_prime_power()
            False
            sage: 0.is_prime_power()
            False
            sage: 1.is_prime_power()
            False
            sage: p = next_prime(10^20); p
            100000000000000000039
            sage: p.is_prime_power()
            True
            sage: (p^97).is_prime_power()
            True
            sage: (p + 1).is_prime_power()
            False

        With the ``get_data`` keyword set to ``True``::

            sage: # needs sage.libs.pari
            sage: (3^100).is_prime_power(get_data=True)
            (3, 100)
            sage: 12.is_prime_power(get_data=True)
            (12, 0)
            sage: (p^97).is_prime_power(get_data=True)
            (100000000000000000039, 97)
            sage: q = p.next_prime(); q
            100000000000000000129
            sage: (p*q).is_prime_power(get_data=True)
            (10000000000000000016800000000000000005031, 0)

        The method works for large entries when ``proof=False``::

            sage: proof.arithmetic(False)
            sage: ((10^500 + 961)^4).is_prime_power()                                   # needs sage.libs.pari
            True
            sage: proof.arithmetic(True)

        We check that :issue:`4777` is fixed::

            sage: n = 150607571^14
            sage: n.is_prime_power()                                                    # needs sage.libs.pari
            True

        TESTS::

            sage: 2.is_prime_power(get_data=True)
            (2, 1)
            sage: 4.is_prime_power(get_data=True)
            (2, 2)
            sage: 512.is_prime_power(get_data=True)
            (2, 9)"""
    def is_pseudoprime(self) -> Any:
        """Integer.is_pseudoprime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5471)

        Test whether ``self`` is a pseudoprime.

        This uses PARI's Baillie-PSW probabilistic primality
        test. Currently, there are no known pseudoprimes for
        Baillie-PSW that are not actually prime. However, it is
        conjectured that there are infinitely many.

        See :wikipedia:`Baillie-PSW_primality_test`

        EXAMPLES::

            sage: z = 2^31 - 1
            sage: z.is_pseudoprime()                                                    # needs sage.libs.pari
            True
            sage: z = 2^31
            sage: z.is_pseudoprime()                                                    # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self, get_data=...) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self, get_data=...) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_pseudoprime_power(self) -> Any:
        """Integer.is_pseudoprime_power(self, get_data=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5493)

        Test if this number is a power of a pseudoprime number.

        For large numbers, this method might be faster than
        :meth:`is_prime_power`.

        INPUT:

        - ``get_data`` -- (default: ``False``) if ``True`` return a pair `(p,k)`
          such that this number equals `p^k` with `p` a pseudoprime and `k` a
          positive integer or the pair ``(self,0)`` otherwise

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = 10^200 + 357
            sage: x.is_pseudoprime()
            True
            sage: (x^12).is_pseudoprime_power()
            True
            sage: (x^12).is_pseudoprime_power(get_data=True)
            (1000...000357, 12)
            sage: (997^100).is_pseudoprime_power()
            True
            sage: (998^100).is_pseudoprime_power()
            False
            sage: ((10^1000 + 453)^2).is_pseudoprime_power()
            True

        TESTS::

            sage: 0.is_pseudoprime_power()
            False
            sage: (-1).is_pseudoprime_power()
            False
            sage: 1.is_pseudoprime_power()                                              # needs sage.libs.pari
            False"""
    @overload
    def is_rational(self) -> Any:
        """Integer.is_rational(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4805)

        Return ``True`` as an integer is a rational number.

        EXAMPLES::

            sage: 5.is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """Integer.is_rational(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4805)

        Return ``True`` as an integer is a rational number.

        EXAMPLES::

            sage: 5.is_rational()
            True"""
    @overload
    def is_square(self) -> Any:
        """Integer.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4843)

        Return ``True`` if ``self`` is a perfect square.

        EXAMPLES::

            sage: Integer(4).is_square()
            True
            sage: Integer(41).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Integer.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4843)

        Return ``True`` if ``self`` is a perfect square.

        EXAMPLES::

            sage: Integer(4).is_square()
            True
            sage: Integer(41).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Integer.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4843)

        Return ``True`` if ``self`` is a perfect square.

        EXAMPLES::

            sage: Integer(4).is_square()
            True
            sage: Integer(41).is_square()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """Integer.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6143)

        Return ``True`` if this integer is not divisible by the square of any
        prime and ``False`` otherwise.

        EXAMPLES::

            sage: 100.is_squarefree()                                                   # needs sage.libs.pari
            False
            sage: 102.is_squarefree()                                                   # needs sage.libs.pari
            True
            sage: 0.is_squarefree()                                                     # needs sage.libs.pari
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """Integer.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6143)

        Return ``True`` if this integer is not divisible by the square of any
        prime and ``False`` otherwise.

        EXAMPLES::

            sage: 100.is_squarefree()                                                   # needs sage.libs.pari
            False
            sage: 102.is_squarefree()                                                   # needs sage.libs.pari
            True
            sage: 0.is_squarefree()                                                     # needs sage.libs.pari
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """Integer.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6143)

        Return ``True`` if this integer is not divisible by the square of any
        prime and ``False`` otherwise.

        EXAMPLES::

            sage: 100.is_squarefree()                                                   # needs sage.libs.pari
            False
            sage: 102.is_squarefree()                                                   # needs sage.libs.pari
            True
            sage: 0.is_squarefree()                                                     # needs sage.libs.pari
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """Integer.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6143)

        Return ``True`` if this integer is not divisible by the square of any
        prime and ``False`` otherwise.

        EXAMPLES::

            sage: 100.is_squarefree()                                                   # needs sage.libs.pari
            False
            sage: 102.is_squarefree()                                                   # needs sage.libs.pari
            True
            sage: 0.is_squarefree()                                                     # needs sage.libs.pari
            False"""
    @overload
    def is_unit(self) -> Any:
        '''Integer.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4827)

        Return ``True`` if this integer is a unit, i.e., `1` or `-1`.

        EXAMPLES::

            sage: for n in srange(-2,3):
            ....:     print("{} {}".format(n, n.is_unit()))
            -2 False
            -1 True
            0 False
            1 True
            2 False'''
    @overload
    def is_unit(self) -> Any:
        '''Integer.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4827)

        Return ``True`` if this integer is a unit, i.e., `1` or `-1`.

        EXAMPLES::

            sage: for n in srange(-2,3):
            ....:     print("{} {}".format(n, n.is_unit()))
            -2 False
            -1 True
            0 False
            1 True
            2 False'''
    @overload
    def isqrt(self) -> Any:
        """Integer.isqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6395)

        Return the integer floor of the square root of ``self``, or raises an
        :exc:`ValueError` if ``self`` is negative.

        EXAMPLES::

            sage: a = Integer(5)
            sage: a.isqrt()
            2

        ::

            sage: Integer(-102).isqrt()
            Traceback (most recent call last):
            ...
            ValueError: square root of negative integer not defined"""
    @overload
    def isqrt(self) -> Any:
        """Integer.isqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6395)

        Return the integer floor of the square root of ``self``, or raises an
        :exc:`ValueError` if ``self`` is negative.

        EXAMPLES::

            sage: a = Integer(5)
            sage: a.isqrt()
            2

        ::

            sage: Integer(-102).isqrt()
            Traceback (most recent call last):
            ...
            ValueError: square root of negative integer not defined"""
    @overload
    def isqrt(self) -> Any:
        """Integer.isqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6395)

        Return the integer floor of the square root of ``self``, or raises an
        :exc:`ValueError` if ``self`` is negative.

        EXAMPLES::

            sage: a = Integer(5)
            sage: a.isqrt()
            2

        ::

            sage: Integer(-102).isqrt()
            Traceback (most recent call last):
            ...
            ValueError: square root of negative integer not defined"""
    def jacobi(self, b) -> Any:
        """Integer.jacobi(self, b)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5635)

        Calculate the Jacobi symbol `\\left(\\frac{\\text{self}}{b}\\right)`.

        EXAMPLES::

            sage: z = -1
            sage: z.jacobi(17)
            1
            sage: z.jacobi(19)
            -1
            sage: z.jacobi(17*19)
            -1
            sage: (2).jacobi(17)
            1
            sage: (3).jacobi(19)
            -1
            sage: (6).jacobi(17*19)
            -1
            sage: (6).jacobi(33)
            0
            sage: a = 3; b = 7
            sage: a.jacobi(b) == -b.jacobi(a)
            True"""
    def kronecker(self, b) -> Any:
        """Integer.kronecker(self, b)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5672)

        Calculate the Kronecker symbol `\\left(\\frac{\\text{self}}{b}\\right)`
        with the Kronecker extension `(\\text{self}/2)=(2/\\text{self})` when ``self`` is odd,
        or `(\\text{self}/2)=0` when ``self`` is even.

        EXAMPLES::

            sage: z = 5
            sage: z.kronecker(41)
            1
            sage: z.kronecker(43)
            -1
            sage: z.kronecker(8)
            -1
            sage: z.kronecker(15)
            0
            sage: a = 2; b = 5
            sage: a.kronecker(b) == b.kronecker(a)
            True"""
    @overload
    def list(self) -> Any:
        """Integer.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 971)

        Return a list with this integer in it, to be compatible with the
        method for number fields.

        EXAMPLES::

            sage: m = 5
            sage: m.list()
            [5]"""
    @overload
    def list(self) -> Any:
        """Integer.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 971)

        Return a list with this integer in it, to be compatible with the
        method for number fields.

        EXAMPLES::

            sage: m = 5
            sage: m.list()
            [5]"""
    @overload
    def log(self, m=..., prec=...) -> Any:
        """Integer.log(self, m=None, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2775)

        Return symbolic log by default, unless the logarithm is exact (for
        an integer argument). When ``prec`` is given, the :class:`RealField`
        approximation to that bit precision is used.

        This function is provided primarily so that Sage integers may be
        treated in the same manner as real numbers when convenient. Direct
        use of :meth:`exact_log` is probably best for arithmetic log computation.

        INPUT:

        - ``m`` -- (default: natural) log base e

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(124).log(5)                                                   # needs sage.symbolic
            log(124)/log(5)
            sage: Integer(124).log(5, 100)                                              # needs sage.rings.real_mpfr
            2.9950093311241087454822446806
            sage: Integer(125).log(5)
            3
            sage: Integer(125).log(5, prec=53)                                          # needs sage.rings.real_mpfr
            3.00000000000000
            sage: log(Integer(125))                                                     # needs sage.symbolic
            3*log(5)

        For extremely large numbers, this works::

            sage: x = 3^100000
            sage: log(x, 3)                                                             # needs sage.rings.real_interval_field
            100000

        Also ``log(x)``, giving a symbolic output,
        works in a reasonable amount of time for this ``x``::

            sage: x = 3^100000
            sage: log(x)                                                                # needs sage.symbolic
            log(1334971414230...5522000001)

        But approximations are probably more useful in this
        case, and work to as high a precision as we desire::

            sage: x.log(3, 53)  # default precision for RealField                       # needs sage.rings.real_mpfr
            100000.000000000
            sage: (x + 1).log(3, 53)                                                    # needs sage.rings.real_mpfr
            100000.000000000
            sage: (x + 1).log(3, 1000)                                                  # needs sage.rings.real_mpfr
            100000.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

        We can use non-integer bases, with default e::

            sage: x.log(2.5, prec=53)                                                   # needs sage.rings.real_mpfr
            119897.784671579

        We also get logarithms of negative integers, via the
        symbolic ring, using the branch from `-\\pi` to `\\pi`::

            sage: log(-1)                                                               # needs sage.symbolic
            I*pi

        The logarithm of zero is done likewise::

            sage: log(0)                                                                # needs sage.symbolic
            -Infinity

        Some rational bases yield integer logarithms (:issue:`21517`)::

            sage: ZZ(8).log(1/2)
            -3

        Check that Python ints are accepted (:issue:`21518`)::

            sage: ZZ(8).log(int(2))
            3

        Check that negative bases yield complex logarithms (:issue:`39959`)::

            sage: 8.log(-2)
            3*log(2)/(I*pi + log(2))
            sage: (-10).log(prec=53)
            2.30258509299405 + 3.14159265358979*I

        Check that zero base  yield complex logarithms (:issue:`39959`)::

            sage: 8.log(0)
            0

        TESTS::

            sage: (-2).log(3)                                                           # needs sage.symbolic
            (I*pi + log(2))/log(3)"""
    @overload
    def log(self, x) -> Any:
        """Integer.log(self, m=None, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2775)

        Return symbolic log by default, unless the logarithm is exact (for
        an integer argument). When ``prec`` is given, the :class:`RealField`
        approximation to that bit precision is used.

        This function is provided primarily so that Sage integers may be
        treated in the same manner as real numbers when convenient. Direct
        use of :meth:`exact_log` is probably best for arithmetic log computation.

        INPUT:

        - ``m`` -- (default: natural) log base e

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(124).log(5)                                                   # needs sage.symbolic
            log(124)/log(5)
            sage: Integer(124).log(5, 100)                                              # needs sage.rings.real_mpfr
            2.9950093311241087454822446806
            sage: Integer(125).log(5)
            3
            sage: Integer(125).log(5, prec=53)                                          # needs sage.rings.real_mpfr
            3.00000000000000
            sage: log(Integer(125))                                                     # needs sage.symbolic
            3*log(5)

        For extremely large numbers, this works::

            sage: x = 3^100000
            sage: log(x, 3)                                                             # needs sage.rings.real_interval_field
            100000

        Also ``log(x)``, giving a symbolic output,
        works in a reasonable amount of time for this ``x``::

            sage: x = 3^100000
            sage: log(x)                                                                # needs sage.symbolic
            log(1334971414230...5522000001)

        But approximations are probably more useful in this
        case, and work to as high a precision as we desire::

            sage: x.log(3, 53)  # default precision for RealField                       # needs sage.rings.real_mpfr
            100000.000000000
            sage: (x + 1).log(3, 53)                                                    # needs sage.rings.real_mpfr
            100000.000000000
            sage: (x + 1).log(3, 1000)                                                  # needs sage.rings.real_mpfr
            100000.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

        We can use non-integer bases, with default e::

            sage: x.log(2.5, prec=53)                                                   # needs sage.rings.real_mpfr
            119897.784671579

        We also get logarithms of negative integers, via the
        symbolic ring, using the branch from `-\\pi` to `\\pi`::

            sage: log(-1)                                                               # needs sage.symbolic
            I*pi

        The logarithm of zero is done likewise::

            sage: log(0)                                                                # needs sage.symbolic
            -Infinity

        Some rational bases yield integer logarithms (:issue:`21517`)::

            sage: ZZ(8).log(1/2)
            -3

        Check that Python ints are accepted (:issue:`21518`)::

            sage: ZZ(8).log(int(2))
            3

        Check that negative bases yield complex logarithms (:issue:`39959`)::

            sage: 8.log(-2)
            3*log(2)/(I*pi + log(2))
            sage: (-10).log(prec=53)
            2.30258509299405 + 3.14159265358979*I

        Check that zero base  yield complex logarithms (:issue:`39959`)::

            sage: 8.log(0)
            0

        TESTS::

            sage: (-2).log(3)                                                           # needs sage.symbolic
            (I*pi + log(2))/log(3)"""
    @overload
    def log(self, x) -> Any:
        """Integer.log(self, m=None, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2775)

        Return symbolic log by default, unless the logarithm is exact (for
        an integer argument). When ``prec`` is given, the :class:`RealField`
        approximation to that bit precision is used.

        This function is provided primarily so that Sage integers may be
        treated in the same manner as real numbers when convenient. Direct
        use of :meth:`exact_log` is probably best for arithmetic log computation.

        INPUT:

        - ``m`` -- (default: natural) log base e

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          symbolic, else to given bits of precision as in :class:`RealField`

        EXAMPLES::

            sage: Integer(124).log(5)                                                   # needs sage.symbolic
            log(124)/log(5)
            sage: Integer(124).log(5, 100)                                              # needs sage.rings.real_mpfr
            2.9950093311241087454822446806
            sage: Integer(125).log(5)
            3
            sage: Integer(125).log(5, prec=53)                                          # needs sage.rings.real_mpfr
            3.00000000000000
            sage: log(Integer(125))                                                     # needs sage.symbolic
            3*log(5)

        For extremely large numbers, this works::

            sage: x = 3^100000
            sage: log(x, 3)                                                             # needs sage.rings.real_interval_field
            100000

        Also ``log(x)``, giving a symbolic output,
        works in a reasonable amount of time for this ``x``::

            sage: x = 3^100000
            sage: log(x)                                                                # needs sage.symbolic
            log(1334971414230...5522000001)

        But approximations are probably more useful in this
        case, and work to as high a precision as we desire::

            sage: x.log(3, 53)  # default precision for RealField                       # needs sage.rings.real_mpfr
            100000.000000000
            sage: (x + 1).log(3, 53)                                                    # needs sage.rings.real_mpfr
            100000.000000000
            sage: (x + 1).log(3, 1000)                                                  # needs sage.rings.real_mpfr
            100000.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

        We can use non-integer bases, with default e::

            sage: x.log(2.5, prec=53)                                                   # needs sage.rings.real_mpfr
            119897.784671579

        We also get logarithms of negative integers, via the
        symbolic ring, using the branch from `-\\pi` to `\\pi`::

            sage: log(-1)                                                               # needs sage.symbolic
            I*pi

        The logarithm of zero is done likewise::

            sage: log(0)                                                                # needs sage.symbolic
            -Infinity

        Some rational bases yield integer logarithms (:issue:`21517`)::

            sage: ZZ(8).log(1/2)
            -3

        Check that Python ints are accepted (:issue:`21518`)::

            sage: ZZ(8).log(int(2))
            3

        Check that negative bases yield complex logarithms (:issue:`39959`)::

            sage: 8.log(-2)
            3*log(2)/(I*pi + log(2))
            sage: (-10).log(prec=53)
            2.30258509299405 + 3.14159265358979*I

        Check that zero base  yield complex logarithms (:issue:`39959`)::

            sage: 8.log(0)
            0

        TESTS::

            sage: (-2).log(3)                                                           # needs sage.symbolic
            (I*pi + log(2))/log(3)"""
    def multifactorial(self, longk) -> Any:
        """Integer.multifactorial(self, long k)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4588)

        Compute the `k`-th factorial `n!^{(k)}` of ``self``.

        The multifactorial number `n!^{(k)}` is defined for nonnegative
        integers `n` as follows. For `k=1` this is the standard factorial,
        and for `k` greater than `1` it is the product of every `k`-th
        terms down from `n` to `1`. The recursive definition is used to
        extend this function to the negative integers `n`.

        This function uses direct call to GMP if `k` and `n` are nonnegative
        and uses simple transformation for other cases.

        EXAMPLES::

            sage: 5.multifactorial(1)
            120
            sage: 5.multifactorial(2)
            15
            sage: 5.multifactorial(3)
            10

            sage: 23.multifactorial(2)
            316234143225
            sage: prod([1..23, step=2])
            316234143225

            sage: (-29).multifactorial(7)
            1/2640
            sage: (-3).multifactorial(5)
            1/2
            sage: (-9).multifactorial(3)
            Traceback (most recent call last):
            ...
            ValueError: multifactorial undefined

        When entries are too large an :exc:`OverflowError` is raised::

            sage: (2**64).multifactorial(2)
            Traceback (most recent call last):
            ...
            OverflowError: argument too large for multifactorial"""
    @overload
    def multiplicative_order(self) -> Any:
        """Integer.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6121)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: ZZ(1).multiplicative_order()
            1
            sage: ZZ(-1).multiplicative_order()
            2
            sage: ZZ(0).multiplicative_order()
            +Infinity
            sage: ZZ(2).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Integer.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6121)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: ZZ(1).multiplicative_order()
            1
            sage: ZZ(-1).multiplicative_order()
            2
            sage: ZZ(0).multiplicative_order()
            +Infinity
            sage: ZZ(2).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Integer.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6121)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: ZZ(1).multiplicative_order()
            1
            sage: ZZ(-1).multiplicative_order()
            2
            sage: ZZ(0).multiplicative_order()
            +Infinity
            sage: ZZ(2).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Integer.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6121)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: ZZ(1).multiplicative_order()
            1
            sage: ZZ(-1).multiplicative_order()
            2
            sage: ZZ(0).multiplicative_order()
            +Infinity
            sage: ZZ(2).multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Integer.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6121)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: ZZ(1).multiplicative_order()
            1
            sage: ZZ(-1).multiplicative_order()
            2
            sage: ZZ(0).multiplicative_order()
            +Infinity
            sage: ZZ(2).multiplicative_order()
            +Infinity"""
    @overload
    def nbits(self) -> Any:
        """Integer.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1335)

        Alias for :meth:`bit_length`.

        TESTS::

            sage: {ZZ(n).nbits() == ZZ(n).bit_length() for n in range(-9999, 9999)}
            {True}"""
    @overload
    def nbits(self) -> Any:
        """Integer.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1335)

        Alias for :meth:`bit_length`.

        TESTS::

            sage: {ZZ(n).nbits() == ZZ(n).bit_length() for n in range(-9999, 9999)}
            {True}"""
    @overload
    def ndigits(self, base=...) -> Any:
        """Integer.ndigits(self, base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1717)

        Return the number of digits of ``self`` expressed in the given base.

        INPUT:

        - ``base`` -- integer (default: 10)

        EXAMPLES::

            sage: n = 52
            sage: n.ndigits()
            2
            sage: n = -10003
            sage: n.ndigits()
            5
            sage: n = 15
            sage: n.ndigits(2)
            4
            sage: n = 1000**1000000+1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000001
            sage: n = 1000**1000000-1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000000
            sage: n = 10**10000000-10**9999990
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            10000000"""
    @overload
    def ndigits(self) -> Any:
        """Integer.ndigits(self, base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1717)

        Return the number of digits of ``self`` expressed in the given base.

        INPUT:

        - ``base`` -- integer (default: 10)

        EXAMPLES::

            sage: n = 52
            sage: n.ndigits()
            2
            sage: n = -10003
            sage: n.ndigits()
            5
            sage: n = 15
            sage: n.ndigits(2)
            4
            sage: n = 1000**1000000+1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000001
            sage: n = 1000**1000000-1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000000
            sage: n = 10**10000000-10**9999990
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            10000000"""
    @overload
    def ndigits(self) -> Any:
        """Integer.ndigits(self, base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1717)

        Return the number of digits of ``self`` expressed in the given base.

        INPUT:

        - ``base`` -- integer (default: 10)

        EXAMPLES::

            sage: n = 52
            sage: n.ndigits()
            2
            sage: n = -10003
            sage: n.ndigits()
            5
            sage: n = 15
            sage: n.ndigits(2)
            4
            sage: n = 1000**1000000+1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000001
            sage: n = 1000**1000000-1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000000
            sage: n = 10**10000000-10**9999990
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            10000000"""
    @overload
    def ndigits(self) -> Any:
        """Integer.ndigits(self, base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1717)

        Return the number of digits of ``self`` expressed in the given base.

        INPUT:

        - ``base`` -- integer (default: 10)

        EXAMPLES::

            sage: n = 52
            sage: n.ndigits()
            2
            sage: n = -10003
            sage: n.ndigits()
            5
            sage: n = 15
            sage: n.ndigits(2)
            4
            sage: n = 1000**1000000+1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000001
            sage: n = 1000**1000000-1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000000
            sage: n = 10**10000000-10**9999990
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            10000000"""
    @overload
    def ndigits(self) -> Any:
        """Integer.ndigits(self, base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1717)

        Return the number of digits of ``self`` expressed in the given base.

        INPUT:

        - ``base`` -- integer (default: 10)

        EXAMPLES::

            sage: n = 52
            sage: n.ndigits()
            2
            sage: n = -10003
            sage: n.ndigits()
            5
            sage: n = 15
            sage: n.ndigits(2)
            4
            sage: n = 1000**1000000+1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000001
            sage: n = 1000**1000000-1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000000
            sage: n = 10**10000000-10**9999990
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            10000000"""
    @overload
    def ndigits(self) -> Any:
        """Integer.ndigits(self, base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1717)

        Return the number of digits of ``self`` expressed in the given base.

        INPUT:

        - ``base`` -- integer (default: 10)

        EXAMPLES::

            sage: n = 52
            sage: n.ndigits()
            2
            sage: n = -10003
            sage: n.ndigits()
            5
            sage: n = 15
            sage: n.ndigits(2)
            4
            sage: n = 1000**1000000+1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000001
            sage: n = 1000**1000000-1
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            3000000
            sage: n = 10**10000000-10**9999990
            sage: n.ndigits()                                                           # needs sage.rings.real_interval_field
            10000000"""
    @overload
    def next_prime(self, proof=...) -> Any:
        """Integer.next_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5880)

        Return the next prime after ``self``.

        This method calls the PARI function :pari:`nextprime`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          ``proof.arithmetic`` or :mod:`sage.structure.proof`); note that the
          global Sage default is ``proof=True``

        EXAMPLES::

            sage: 100.next_prime()                                                      # needs sage.libs.pari
            101
            sage: (10^50).next_prime()                                                  # needs sage.libs.pari
            100000000000000000000000000000000000000000000000151

        Use ``proof=False``, which is way faster since it does not need
        a primality proof::

            sage: b = (2^1024).next_prime(proof=False)                                  # needs sage.libs.pari
            sage: b - 2^1024                                                            # needs sage.libs.pari
            643

        ::

            sage: Integer(0).next_prime()                                               # needs sage.libs.pari
            2
            sage: Integer(1001).next_prime()                                            # needs sage.libs.pari
            1009"""
    @overload
    def next_prime(self) -> Any:
        """Integer.next_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5880)

        Return the next prime after ``self``.

        This method calls the PARI function :pari:`nextprime`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          ``proof.arithmetic`` or :mod:`sage.structure.proof`); note that the
          global Sage default is ``proof=True``

        EXAMPLES::

            sage: 100.next_prime()                                                      # needs sage.libs.pari
            101
            sage: (10^50).next_prime()                                                  # needs sage.libs.pari
            100000000000000000000000000000000000000000000000151

        Use ``proof=False``, which is way faster since it does not need
        a primality proof::

            sage: b = (2^1024).next_prime(proof=False)                                  # needs sage.libs.pari
            sage: b - 2^1024                                                            # needs sage.libs.pari
            643

        ::

            sage: Integer(0).next_prime()                                               # needs sage.libs.pari
            2
            sage: Integer(1001).next_prime()                                            # needs sage.libs.pari
            1009"""
    @overload
    def next_prime(self) -> Any:
        """Integer.next_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5880)

        Return the next prime after ``self``.

        This method calls the PARI function :pari:`nextprime`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          ``proof.arithmetic`` or :mod:`sage.structure.proof`); note that the
          global Sage default is ``proof=True``

        EXAMPLES::

            sage: 100.next_prime()                                                      # needs sage.libs.pari
            101
            sage: (10^50).next_prime()                                                  # needs sage.libs.pari
            100000000000000000000000000000000000000000000000151

        Use ``proof=False``, which is way faster since it does not need
        a primality proof::

            sage: b = (2^1024).next_prime(proof=False)                                  # needs sage.libs.pari
            sage: b - 2^1024                                                            # needs sage.libs.pari
            643

        ::

            sage: Integer(0).next_prime()                                               # needs sage.libs.pari
            2
            sage: Integer(1001).next_prime()                                            # needs sage.libs.pari
            1009"""
    @overload
    def next_prime(self, proof=...) -> Any:
        """Integer.next_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5880)

        Return the next prime after ``self``.

        This method calls the PARI function :pari:`nextprime`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          ``proof.arithmetic`` or :mod:`sage.structure.proof`); note that the
          global Sage default is ``proof=True``

        EXAMPLES::

            sage: 100.next_prime()                                                      # needs sage.libs.pari
            101
            sage: (10^50).next_prime()                                                  # needs sage.libs.pari
            100000000000000000000000000000000000000000000000151

        Use ``proof=False``, which is way faster since it does not need
        a primality proof::

            sage: b = (2^1024).next_prime(proof=False)                                  # needs sage.libs.pari
            sage: b - 2^1024                                                            # needs sage.libs.pari
            643

        ::

            sage: Integer(0).next_prime()                                               # needs sage.libs.pari
            2
            sage: Integer(1001).next_prime()                                            # needs sage.libs.pari
            1009"""
    @overload
    def next_prime(self) -> Any:
        """Integer.next_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5880)

        Return the next prime after ``self``.

        This method calls the PARI function :pari:`nextprime`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          ``proof.arithmetic`` or :mod:`sage.structure.proof`); note that the
          global Sage default is ``proof=True``

        EXAMPLES::

            sage: 100.next_prime()                                                      # needs sage.libs.pari
            101
            sage: (10^50).next_prime()                                                  # needs sage.libs.pari
            100000000000000000000000000000000000000000000000151

        Use ``proof=False``, which is way faster since it does not need
        a primality proof::

            sage: b = (2^1024).next_prime(proof=False)                                  # needs sage.libs.pari
            sage: b - 2^1024                                                            # needs sage.libs.pari
            643

        ::

            sage: Integer(0).next_prime()                                               # needs sage.libs.pari
            2
            sage: Integer(1001).next_prime()                                            # needs sage.libs.pari
            1009"""
    @overload
    def next_prime(self) -> Any:
        """Integer.next_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5880)

        Return the next prime after ``self``.

        This method calls the PARI function :pari:`nextprime`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          ``proof.arithmetic`` or :mod:`sage.structure.proof`); note that the
          global Sage default is ``proof=True``

        EXAMPLES::

            sage: 100.next_prime()                                                      # needs sage.libs.pari
            101
            sage: (10^50).next_prime()                                                  # needs sage.libs.pari
            100000000000000000000000000000000000000000000000151

        Use ``proof=False``, which is way faster since it does not need
        a primality proof::

            sage: b = (2^1024).next_prime(proof=False)                                  # needs sage.libs.pari
            sage: b - 2^1024                                                            # needs sage.libs.pari
            643

        ::

            sage: Integer(0).next_prime()                                               # needs sage.libs.pari
            2
            sage: Integer(1001).next_prime()                                            # needs sage.libs.pari
            1009"""
    @overload
    def next_prime_power(self, proof=...) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_prime_power(self) -> Any:
        '''Integer.next_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5967)

        Return the next prime power after ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the next power of 2 and goes through
        the odd numbers calling :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`previous_prime_power`
            - :meth:`is_prime_power`
            - :meth:`next_prime`
            - :meth:`previous_prime`

        EXAMPLES::

            sage: (-1).next_prime_power()
            2
            sage: 2.next_prime_power()
            3
            sage: 103.next_prime_power()                                                # needs sage.libs.pari
            107
            sage: 107.next_prime_power()
            109
            sage: 2044.next_prime_power()                                               # needs sage.libs.pari
            2048

        TESTS::

            sage: [(2**k - 1).next_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).next_prime_power() for k in range(10)]                        # needs sage.libs.pari
            [2, 3, 5, 9, 17, 37, 67, 131, 257, 521]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(2**256).next_prime_power()
            ....:     m = n.next_prime_power().previous_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    @overload
    def next_probable_prime(self) -> Any:
        """Integer.next_probable_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5858)

        Return the next probable prime after ``self``, as determined by PARI.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (-37).next_probable_prime()
            2
            sage: (100).next_probable_prime()
            101
            sage: (2^512).next_probable_prime()
            13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
            sage: 0.next_probable_prime()
            2
            sage: 126.next_probable_prime()
            127
            sage: 144168.next_probable_prime()
            144169"""
    def nth_root(self, intn, booltruncate_mode=...) -> Any:
        """Integer.nth_root(self, int n, bool truncate_mode=0)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2339)

        Return the (possibly truncated) ``n``-th root of ``self``.

        INPUT:

        - ``n`` -- integer `\\geq 1` (must fit in the C ``int`` type)

        - ``truncate_mode`` -- boolean, whether to allow truncation if
          ``self`` is not an ``n``-th power

        OUTPUT:

        If ``truncate_mode`` is 0 (default), then returns the exact n'th root
        if ``self`` is an n'th power, or raises a :exc:`ValueError`
        if it is not.

        If ``truncate_mode`` is 1, then if either ``n`` is odd or ``self`` is
        positive, returns a pair ``(root, exact_flag)`` where ``root`` is the
        truncated ``n``-th root (rounded towards zero) and ``exact_flag`` is a
        boolean indicating whether the root extraction was exact;
        otherwise raises a :exc:`ValueError`.

        AUTHORS:

        - David Harvey (2006-09-15)
        - Interface changed by John Cremona (2009-04-04)

        EXAMPLES::

            sage: Integer(125).nth_root(3)
            5
            sage: Integer(124).nth_root(3)
            Traceback (most recent call last):
            ...
            ValueError: 124 is not a 3rd power
            sage: Integer(124).nth_root(3, truncate_mode=1)
            (4, False)
            sage: Integer(125).nth_root(3, truncate_mode=1)
            (5, True)
            sage: Integer(126).nth_root(3, truncate_mode=1)
            (5, False)

        ::

            sage: Integer(-125).nth_root(3)
            -5
            sage: Integer(-125).nth_root(3,truncate_mode=1)
            (-5, True)
            sage: Integer(-124).nth_root(3,truncate_mode=1)
            (-4, False)
            sage: Integer(-126).nth_root(3,truncate_mode=1)
            (-5, False)

        ::

            sage: Integer(125).nth_root(2, True)
            (11, False)
            sage: Integer(125).nth_root(3, True)
            (5, True)

        ::

            sage: Integer(125).nth_root(-5)
            Traceback (most recent call last):
            ...
            ValueError: n (=-5) must be positive

        ::

            sage: Integer(-25).nth_root(2)
            Traceback (most recent call last):
            ...
            ValueError: cannot take even root of negative number

        ::

            sage: a=9
            sage: a.nth_root(3)
            Traceback (most recent call last):
            ...
            ValueError: 9 is not a 3rd power

            sage: a.nth_root(22)
            Traceback (most recent call last):
            ...
            ValueError: 9 is not a 22nd power

            sage: ZZ(2^20).nth_root(21)
            Traceback (most recent call last):
            ...
            ValueError: 1048576 is not a 21st power

            sage: ZZ(2^20).nth_root(21, truncate_mode=1)
            (1, False)"""
    @overload
    def numerator(self) -> Any:
        """Integer.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4510)

        Return the numerator of this integer.

        EXAMPLES::

            sage: x = 5
            sage: x.numerator()
            5

        ::

            sage: x = 0
            sage: x.numerator()
            0"""
    @overload
    def numerator(self) -> Any:
        """Integer.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4510)

        Return the numerator of this integer.

        EXAMPLES::

            sage: x = 5
            sage: x.numerator()
            5

        ::

            sage: x = 0
            sage: x.numerator()
            0"""
    @overload
    def numerator(self) -> Any:
        """Integer.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4510)

        Return the numerator of this integer.

        EXAMPLES::

            sage: x = 5
            sage: x.numerator()
            5

        ::

            sage: x = 0
            sage: x.numerator()
            0"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    @overload
    def oct(self) -> Any:
        """Integer.oct(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1208)

        Return the digits of ``self`` in base 8.

        .. NOTE::

           '0' (or '0o') is *not* prepended to the result like is done by the
           corresponding Python function on ``int``. This is for
           efficiency sake--adding and stripping the string wastes
           time; since this function is used for conversions from
           integers to other C-library structures, it is important
           that it be fast.

        EXAMPLES::

            sage: print(Integer(800).oct())
            1440
            sage: print(Integer(8).oct())
            10
            sage: print(Integer(-50).oct())
            -62
            sage: print(Integer(-899).oct())
            -1603
            sage: print(Integer(16938402384092843092843098243).oct())
            15535436162247215217705000570203

        Behavior of Sage integers vs. Python integers::

            sage: Integer(10).oct()
            '12'
            sage: oct(int(10))
            '0o12'

            sage: Integer(-23).oct()
            '-27'
            sage: oct(int(-23))
            '-0o27'"""
    def odd_part(self) -> Any:
        """Integer.odd_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4367)

        The odd part of the integer `n`. This is `n / 2^v`,
        where `v = \\mathrm{valuation}(n,2)`.

        IMPLEMENTATION:

        Currently returns 0 when ``self`` is 0.  This behaviour is fairly arbitrary,
        and in Sage 4.6 this special case was not handled at all, eventually
        propagating a :exc:`TypeError`.  The caller should not rely on the behaviour
        in case ``self`` is 0.

        EXAMPLES::

            sage: odd_part(5)
            5
            sage: odd_part(4)
            1
            sage: odd_part(factorial(31))
            122529844256906551386796875"""
    def ord(self, *args, **kwargs):
        """Integer.valuation(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4275)

        Return the `p`-adic valuation of ``self``.

        INPUT:

        - ``p`` -- integer at least 2

        EXAMPLES::

            sage: n = 60
            sage: n.valuation(2)
            2
            sage: n.valuation(3)
            1
            sage: n.valuation(7)
            0
            sage: n.valuation(1)
            Traceback (most recent call last):
            ...
            ValueError: You can only compute the valuation with respect to a integer larger than 1.

        We do not require that ``p`` is a prime::

            sage: (2^11).valuation(4)
            5"""
    @overload
    def ordinal_str(self) -> Any:
        """Integer.ordinal_str(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1136)

        Return a string representation of the ordinal associated to ``self``.

        EXAMPLES::

            sage: [ZZ(n).ordinal_str() for n in range(25)]
            ['0th',
            '1st',
            '2nd',
            '3rd',
            '4th',
            ...
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            ...
            '20th',
            '21st',
            '22nd',
            '23rd',
            '24th']

            sage: ZZ(1001).ordinal_str()
            '1001st'

            sage: ZZ(113).ordinal_str()
            '113th'
            sage: ZZ(112).ordinal_str()
            '112th'
            sage: ZZ(111).ordinal_str()
            '111th'"""
    @overload
    def ordinal_str(self) -> Any:
        """Integer.ordinal_str(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1136)

        Return a string representation of the ordinal associated to ``self``.

        EXAMPLES::

            sage: [ZZ(n).ordinal_str() for n in range(25)]
            ['0th',
            '1st',
            '2nd',
            '3rd',
            '4th',
            ...
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            ...
            '20th',
            '21st',
            '22nd',
            '23rd',
            '24th']

            sage: ZZ(1001).ordinal_str()
            '1001st'

            sage: ZZ(113).ordinal_str()
            '113th'
            sage: ZZ(112).ordinal_str()
            '112th'
            sage: ZZ(111).ordinal_str()
            '111th'"""
    @overload
    def ordinal_str(self) -> Any:
        """Integer.ordinal_str(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1136)

        Return a string representation of the ordinal associated to ``self``.

        EXAMPLES::

            sage: [ZZ(n).ordinal_str() for n in range(25)]
            ['0th',
            '1st',
            '2nd',
            '3rd',
            '4th',
            ...
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            ...
            '20th',
            '21st',
            '22nd',
            '23rd',
            '24th']

            sage: ZZ(1001).ordinal_str()
            '1001st'

            sage: ZZ(113).ordinal_str()
            '113th'
            sage: ZZ(112).ordinal_str()
            '112th'
            sage: ZZ(111).ordinal_str()
            '111th'"""
    @overload
    def ordinal_str(self) -> Any:
        """Integer.ordinal_str(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1136)

        Return a string representation of the ordinal associated to ``self``.

        EXAMPLES::

            sage: [ZZ(n).ordinal_str() for n in range(25)]
            ['0th',
            '1st',
            '2nd',
            '3rd',
            '4th',
            ...
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            ...
            '20th',
            '21st',
            '22nd',
            '23rd',
            '24th']

            sage: ZZ(1001).ordinal_str()
            '1001st'

            sage: ZZ(113).ordinal_str()
            '113th'
            sage: ZZ(112).ordinal_str()
            '112th'
            sage: ZZ(111).ordinal_str()
            '111th'"""
    @overload
    def ordinal_str(self) -> Any:
        """Integer.ordinal_str(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1136)

        Return a string representation of the ordinal associated to ``self``.

        EXAMPLES::

            sage: [ZZ(n).ordinal_str() for n in range(25)]
            ['0th',
            '1st',
            '2nd',
            '3rd',
            '4th',
            ...
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            ...
            '20th',
            '21st',
            '22nd',
            '23rd',
            '24th']

            sage: ZZ(1001).ordinal_str()
            '1001st'

            sage: ZZ(113).ordinal_str()
            '113th'
            sage: ZZ(112).ordinal_str()
            '112th'
            sage: ZZ(111).ordinal_str()
            '111th'"""
    @overload
    def ordinal_str(self) -> Any:
        """Integer.ordinal_str(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1136)

        Return a string representation of the ordinal associated to ``self``.

        EXAMPLES::

            sage: [ZZ(n).ordinal_str() for n in range(25)]
            ['0th',
            '1st',
            '2nd',
            '3rd',
            '4th',
            ...
            '10th',
            '11th',
            '12th',
            '13th',
            '14th',
            ...
            '20th',
            '21st',
            '22nd',
            '23rd',
            '24th']

            sage: ZZ(1001).ordinal_str()
            '1001st'

            sage: ZZ(113).ordinal_str()
            '113th'
            sage: ZZ(112).ordinal_str()
            '112th'
            sage: ZZ(111).ordinal_str()
            '111th'"""
    def p_primary_part(self, p) -> Any:
        """Integer.p_primary_part(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4307)

        Return the ``p``-primary part of ``self``.

        INPUT:

        - ``p`` -- prime integer

        OUTPUT: largest power of ``p`` dividing ``self``

        EXAMPLES::

            sage: n = 40
            sage: n.p_primary_part(2)
            8
            sage: n.p_primary_part(5)
            5
            sage: n.p_primary_part(7)
            1
            sage: n.p_primary_part(6)
            Traceback (most recent call last):
            ...
            ValueError: 6 is not a prime number"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def perfect_power(self) -> Any:
        """Integer.perfect_power(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4856)

        Return ``(a, b)``, where this integer is `a^b` and `b` is maximal.

        If called on `-1`, `0` or `1`, `b` will be `1`, since there is no
        maximal value of `b`.

        .. SEEALSO::

            - :meth:`is_perfect_power`: testing whether an integer is a perfect
              power is usually faster than finding `a` and `b`.
            - :meth:`is_prime_power`: checks whether the base is prime.
            - :meth:`is_power_of`: if you know the base already, this method is
              the fastest option.

        EXAMPLES::

            sage: 144.perfect_power()                                                   # needs sage.libs.pari
            (12, 2)
            sage: 1.perfect_power()
            (1, 1)
            sage: 0.perfect_power()
            (0, 1)
            sage: (-1).perfect_power()
            (-1, 1)
            sage: (-8).perfect_power()                                                  # needs sage.libs.pari
            (-2, 3)
            sage: (-4).perfect_power()
            (-4, 1)
            sage: (101^29).perfect_power()                                              # needs sage.libs.pari
            (101, 29)
            sage: (-243).perfect_power()                                                # needs sage.libs.pari
            (-3, 5)
            sage: (-64).perfect_power()                                                 # needs sage.libs.pari
            (-4, 3)

        TESTS::

            sage: 4.perfect_power()
            (2, 2)
            sage: 256.perfect_power()
            (2, 8)"""
    @overload
    def popcount(self) -> Any:
        """Integer.popcount(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7060)

        Return the number of 1 bits in the binary representation.
        If ``self`` < 0, we return Infinity.

        EXAMPLES::

            sage: n = 123
            sage: n.str(2)
            '1111011'
            sage: n.popcount()
            6

            sage: n = -17
            sage: n.popcount()
            +Infinity"""
    @overload
    def popcount(self) -> Any:
        """Integer.popcount(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7060)

        Return the number of 1 bits in the binary representation.
        If ``self`` < 0, we return Infinity.

        EXAMPLES::

            sage: n = 123
            sage: n.str(2)
            '1111011'
            sage: n.popcount()
            6

            sage: n = -17
            sage: n.popcount()
            +Infinity"""
    @overload
    def popcount(self) -> Any:
        """Integer.popcount(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7060)

        Return the number of 1 bits in the binary representation.
        If ``self`` < 0, we return Infinity.

        EXAMPLES::

            sage: n = 123
            sage: n.str(2)
            '1111011'
            sage: n.popcount()
            6

            sage: n = -17
            sage: n.popcount()
            +Infinity"""
    def powermod(self, exp, mod) -> Any:
        """Integer.powermod(self, exp, mod)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3516)

        Compute ``self**exp`` modulo ``mod``.

        EXAMPLES::

            sage: z = 2
            sage: z.powermod(31,31)
            2
            sage: z.powermod(0,31)
            1
            sage: z.powermod(-31,31) == 2^-31 % 31
            True

        As expected, the following is invalid::

            sage: z.powermod(31,0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: cannot raise to a power modulo 0"""
    @overload
    def previous_prime(self, proof=...) -> Any:
        """Integer.previous_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5919)

        Return the previous prime before ``self``.

        This method calls the PARI function :pari:`precprime`.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        .. SEEALSO::

            - :meth:`next_prime`

        EXAMPLES::

            sage: 10.previous_prime()                                                   # needs sage.libs.pari
            7
            sage: 7.previous_prime()                                                    # needs sage.libs.pari
            5
            sage: 14376485.previous_prime()                                             # needs sage.libs.pari
            14376463

            sage: 2.previous_prime()
            Traceback (most recent call last):
            ...
            ValueError: no prime less than 2

        An example using ``proof=False``, which is way faster since it does not
        need a primality proof::

            sage: b = (2^1024).previous_prime(proof=False)                              # needs sage.libs.pari
            sage: 2^1024 - b                                                            # needs sage.libs.pari
            105"""
    @overload
    def previous_prime(self) -> Any:
        """Integer.previous_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5919)

        Return the previous prime before ``self``.

        This method calls the PARI function :pari:`precprime`.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        .. SEEALSO::

            - :meth:`next_prime`

        EXAMPLES::

            sage: 10.previous_prime()                                                   # needs sage.libs.pari
            7
            sage: 7.previous_prime()                                                    # needs sage.libs.pari
            5
            sage: 14376485.previous_prime()                                             # needs sage.libs.pari
            14376463

            sage: 2.previous_prime()
            Traceback (most recent call last):
            ...
            ValueError: no prime less than 2

        An example using ``proof=False``, which is way faster since it does not
        need a primality proof::

            sage: b = (2^1024).previous_prime(proof=False)                              # needs sage.libs.pari
            sage: 2^1024 - b                                                            # needs sage.libs.pari
            105"""
    @overload
    def previous_prime(self) -> Any:
        """Integer.previous_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5919)

        Return the previous prime before ``self``.

        This method calls the PARI function :pari:`precprime`.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        .. SEEALSO::

            - :meth:`next_prime`

        EXAMPLES::

            sage: 10.previous_prime()                                                   # needs sage.libs.pari
            7
            sage: 7.previous_prime()                                                    # needs sage.libs.pari
            5
            sage: 14376485.previous_prime()                                             # needs sage.libs.pari
            14376463

            sage: 2.previous_prime()
            Traceback (most recent call last):
            ...
            ValueError: no prime less than 2

        An example using ``proof=False``, which is way faster since it does not
        need a primality proof::

            sage: b = (2^1024).previous_prime(proof=False)                              # needs sage.libs.pari
            sage: 2^1024 - b                                                            # needs sage.libs.pari
            105"""
    @overload
    def previous_prime(self) -> Any:
        """Integer.previous_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5919)

        Return the previous prime before ``self``.

        This method calls the PARI function :pari:`precprime`.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        .. SEEALSO::

            - :meth:`next_prime`

        EXAMPLES::

            sage: 10.previous_prime()                                                   # needs sage.libs.pari
            7
            sage: 7.previous_prime()                                                    # needs sage.libs.pari
            5
            sage: 14376485.previous_prime()                                             # needs sage.libs.pari
            14376463

            sage: 2.previous_prime()
            Traceback (most recent call last):
            ...
            ValueError: no prime less than 2

        An example using ``proof=False``, which is way faster since it does not
        need a primality proof::

            sage: b = (2^1024).previous_prime(proof=False)                              # needs sage.libs.pari
            sage: 2^1024 - b                                                            # needs sage.libs.pari
            105"""
    @overload
    def previous_prime(self) -> Any:
        """Integer.previous_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5919)

        Return the previous prime before ``self``.

        This method calls the PARI function :pari:`precprime`.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        .. SEEALSO::

            - :meth:`next_prime`

        EXAMPLES::

            sage: 10.previous_prime()                                                   # needs sage.libs.pari
            7
            sage: 7.previous_prime()                                                    # needs sage.libs.pari
            5
            sage: 14376485.previous_prime()                                             # needs sage.libs.pari
            14376463

            sage: 2.previous_prime()
            Traceback (most recent call last):
            ...
            ValueError: no prime less than 2

        An example using ``proof=False``, which is way faster since it does not
        need a primality proof::

            sage: b = (2^1024).previous_prime(proof=False)                              # needs sage.libs.pari
            sage: 2^1024 - b                                                            # needs sage.libs.pari
            105"""
    @overload
    def previous_prime(self, proof=...) -> Any:
        """Integer.previous_prime(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5919)

        Return the previous prime before ``self``.

        This method calls the PARI function :pari:`precprime`.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        .. SEEALSO::

            - :meth:`next_prime`

        EXAMPLES::

            sage: 10.previous_prime()                                                   # needs sage.libs.pari
            7
            sage: 7.previous_prime()                                                    # needs sage.libs.pari
            5
            sage: 14376485.previous_prime()                                             # needs sage.libs.pari
            14376463

            sage: 2.previous_prime()
            Traceback (most recent call last):
            ...
            ValueError: no prime less than 2

        An example using ``proof=False``, which is way faster since it does not
        need a primality proof::

            sage: b = (2^1024).previous_prime(proof=False)                              # needs sage.libs.pari
            sage: 2^1024 - b                                                            # needs sage.libs.pari
            105"""
    @overload
    def previous_prime_power(self, proof=...) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def previous_prime_power(self) -> Any:
        '''Integer.previous_prime_power(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6033)

        Return the previous prime power before ``self``.

        INPUT:

        - ``proof`` -- if ``True`` ensure that the returned value is the next
          prime power and if set to ``False`` uses probabilistic methods
          (i.e. the result is not guaranteed). By default it uses global
          configuration variables to determine which alternative to use (see
          :mod:`proof.arithmetic` or :mod:`sage.structure.proof`).

        ALGORITHM:

        The algorithm is naive. It computes the previous power of 2 and goes
        through the odd numbers calling the method :meth:`is_prime_power`.

        .. SEEALSO::

            - :meth:`next_prime_power`
            - :meth:`is_prime_power`
            - :meth:`previous_prime`
            - :meth:`next_prime`

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: 3.previous_prime_power()
            2
            sage: 103.previous_prime_power()
            101
            sage: 107.previous_prime_power()
            103
            sage: 2044.previous_prime_power()
            2039

            sage: 2.previous_prime_power()
            Traceback (most recent call last):
            ...
            ValueError: no prime power less than 2

        TESTS::

            sage: [(2**k + 1).previous_prime_power() for k in range(1,10)]
            [2, 4, 8, 16, 32, 64, 128, 256, 512]
            sage: [(2**k).previous_prime_power() for k in range(2, 10)]                 # needs sage.libs.pari
            [3, 7, 13, 31, 61, 127, 251, 509]

            sage: for _ in range(10):                                                   # needs sage.libs.pari
            ....:     n = ZZ.random_element(3,2**256).previous_prime_power()
            ....:     m = n.previous_prime_power().next_prime_power()
            ....:     assert m == n, "problem with n = {}".format(n)'''
    @overload
    def prime_divisors(self, *args, **kwds) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self, limit=...) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    @overload
    def prime_divisors(self, limit=...) -> Any:
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    def prime_factors(self, *args, **kwargs):
        """Integer.prime_divisors(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2985)

        Return the prime divisors of this integer, sorted in increasing order.

        If this integer is negative, we do *not* include `-1` among
        its prime divisors, since `-1` is not a prime number.

        INPUT:

        - ``limit`` -- (integer, optional keyword argument)
          Return only prime divisors up to this bound, and the factorization
          is done by checking primes up to ``limit`` using trial division.

        Any additional arguments are passed on to the :meth:`factor` method.

        EXAMPLES::

            sage: a = 1; a.prime_divisors()
            []
            sage: a = 100; a.prime_divisors()
            [2, 5]
            sage: a = -100; a.prime_divisors()
            [2, 5]
            sage: a = 2004; a.prime_divisors()
            [2, 3, 167]

        Setting the optional ``limit`` argument works as expected::

            sage: a = 10^100 + 1
            sage: a.prime_divisors()                                                    # needs sage.libs.pari
            [73, 137, 401, 1201, 1601, 1676321, 5964848081,
             129694419029057750551385771184564274499075700947656757821537291527196801]
            sage: a.prime_divisors(limit=10^3)
            [73, 137, 401]
            sage: a.prime_divisors(limit=10^7)
            [73, 137, 401, 1201, 1601, 1676321]"""
    def prime_to_m_part(self, m) -> Any:
        """Integer.prime_to_m_part(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2943)

        Return the prime-to-`m` part of ``self``, i.e., the largest divisor of
        ``self`` that is coprime to `m`.

        INPUT:

        - ``m`` -- integer

        OUTPUT: integer

        EXAMPLES::

            sage: 43434.prime_to_m_part(20)
            21717
            sage: 2048.prime_to_m_part(2)
            1
            sage: 2048.prime_to_m_part(3)
            2048

            sage: 0.prime_to_m_part(2)
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be nonzero"""
    @overload
    def quo_rem(self, other) -> Any:
        """Integer.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3424)

        Return the quotient and the remainder of ``self`` divided by ``other``.
        Note that the remainder returned is always either zero or of the
        same sign as ``other``.

        INPUT:

        - ``other`` -- the divisor

        OUTPUT:

        - ``q`` -- the quotient of ``self/other``

        - ``r`` -- the remainder of ``self/other``

        EXAMPLES::

            sage: z = Integer(231)
            sage: z.quo_rem(2)
            (115, 1)
            sage: z.quo_rem(-2)
            (-116, -1)
            sage: z.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Integer division by zero

            sage: a = ZZ.random_element(10**50)
            sage: b = ZZ.random_element(10**15)
            sage: q, r = a.quo_rem(b)
            sage: q*b + r == a
            True

            sage: 3.quo_rem(ZZ['x'].0)
            (0, 3)

        TESTS:

        The divisor can be rational as well, although the remainder
        will always be zero (:issue:`7965`)::

            sage: 5.quo_rem(QQ(2))
            (5/2, 0)
            sage: 5.quo_rem(2/3)
            (15/2, 0)

        Check that :issue:`29009` is fixed:

            sage: divmod(1, sys.maxsize+1r)  # should not raise OverflowError: Python int too large to convert to C long
            (0, 1)

            sage: # needs mpmath
            sage: import mpmath
            sage: mpmath.mp.prec = 1000
            sage: root = mpmath.findroot(lambda x: x^2 - 3, 2)
            sage: len(str(root))
            301"""
    @overload
    def quo_rem(self, b) -> Any:
        """Integer.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3424)

        Return the quotient and the remainder of ``self`` divided by ``other``.
        Note that the remainder returned is always either zero or of the
        same sign as ``other``.

        INPUT:

        - ``other`` -- the divisor

        OUTPUT:

        - ``q`` -- the quotient of ``self/other``

        - ``r`` -- the remainder of ``self/other``

        EXAMPLES::

            sage: z = Integer(231)
            sage: z.quo_rem(2)
            (115, 1)
            sage: z.quo_rem(-2)
            (-116, -1)
            sage: z.quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Integer division by zero

            sage: a = ZZ.random_element(10**50)
            sage: b = ZZ.random_element(10**15)
            sage: q, r = a.quo_rem(b)
            sage: q*b + r == a
            True

            sage: 3.quo_rem(ZZ['x'].0)
            (0, 3)

        TESTS:

        The divisor can be rational as well, although the remainder
        will always be zero (:issue:`7965`)::

            sage: 5.quo_rem(QQ(2))
            (5/2, 0)
            sage: 5.quo_rem(2/3)
            (15/2, 0)

        Check that :issue:`29009` is fixed:

            sage: divmod(1, sys.maxsize+1r)  # should not raise OverflowError: Python int too large to convert to C long
            (0, 1)

            sage: # needs mpmath
            sage: import mpmath
            sage: mpmath.mp.prec = 1000
            sage: root = mpmath.findroot(lambda x: x^2 - 3, 2)
            sage: len(str(root))
            301"""
    def rational_reconstruction(self, Integerm) -> Any:
        """Integer.rational_reconstruction(self, Integer m)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3551)

        Return the rational reconstruction of this integer modulo `m`, i.e.,
        the unique (if it exists) rational number that reduces to ``self``
        modulo m and whose numerator and denominator is bounded by
        `\\sqrt{m/2}`.

        INPUT:

        - ``self`` -- integer

        - ``m`` -- integer

        OUTPUT: a :class:`Rational`

        EXAMPLES::

            sage: (3/7)%100
            29
            sage: (29).rational_reconstruction(100)
            3/7

        TESTS:

        Check that :issue:`9345` is fixed::

            sage: 0.rational_reconstruction(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational reconstruction with zero modulus
            sage: ZZ.random_element(-10^6, 10^6).rational_reconstruction(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational reconstruction with zero modulus"""
    @overload
    def real(self) -> Any:
        """Integer.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4745)

        Return the real part of ``self``, which is ``self``.

        EXAMPLES::

            sage: Integer(-4).real()
            -4"""
    @overload
    def real(self) -> Any:
        """Integer.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4745)

        Return the real part of ``self``, which is ``self``.

        EXAMPLES::

            sage: Integer(-4).real()
            -4"""
    @overload
    def round(self, mode=...) -> Any:
        """Integer.round(self, mode='away')

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4730)

        Return the nearest integer to ``self``, which is ``self`` since
        ``self`` is an integer.

        EXAMPLES:

        This example addresses :issue:`23502`::

            sage: n = 6
            sage: n.round()
            6"""
    @overload
    def round(self) -> Any:
        """Integer.round(self, mode='away')

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4730)

        Return the nearest integer to ``self``, which is ``self`` since
        ``self`` is an integer.

        EXAMPLES:

        This example addresses :issue:`23502`::

            sage: n = 6
            sage: n.round()
            6"""
    @overload
    def sign(self) -> Any:
        """Integer.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3319)

        Return the sign of this integer, which is `-1`, `0`, or `1`
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: 500.sign()
            1
            sage: 0.sign()
            0
            sage: (-10^43).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """Integer.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3319)

        Return the sign of this integer, which is `-1`, `0`, or `1`
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: 500.sign()
            1
            sage: 0.sign()
            0
            sage: (-10^43).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """Integer.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3319)

        Return the sign of this integer, which is `-1`, `0`, or `1`
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: 500.sign()
            1
            sage: 0.sign()
            0
            sage: (-10^43).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """Integer.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3319)

        Return the sign of this integer, which is `-1`, `0`, or `1`
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: 500.sign()
            1
            sage: 0.sign()
            0
            sage: (-10^43).sign()
            -1"""
    @overload
    def sqrt(self, prec=..., extend=..., all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, prec=..., all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """Integer.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6424)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, return an exact
          square root; otherwise return a numerical square root, to the
          given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: Integer(144).sqrt()
            12
            sage: sqrt(Integer(144))
            12
            sage: Integer(102).sqrt()                                                   # needs sage.symbolic
            sqrt(102)

        ::

            sage: n = 2
            sage: n.sqrt(all=True)                                                      # needs sage.symbolic
            [sqrt(2), -sqrt(2)]
            sage: n.sqrt(prec=10)                                                       # needs sage.rings.real_mpfr
            1.4
            sage: n.sqrt(prec=100)                                                      # needs sage.rings.real_mpfr
            1.4142135623730950488016887242
            sage: n.sqrt(prec=100, all=True)                                            # needs sage.rings.real_mpfr
            [1.4142135623730950488016887242, -1.4142135623730950488016887242]
            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of 2 is not an integer
            sage: (-1).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ArithmeticError: square root of -1 is not an integer
            sage: Integer(144).sqrt(all=True)
            [12, -12]
            sage: Integer(0).sqrt(all=True)
            [0]

        TESTS::

            sage: type(5.sqrt())                                                        # needs sage.symbolic
            <class 'sage.symbolic.expression.Expression'>
            sage: type(5.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: type((-5).sqrt(prec=53))                                              # needs sage.rings.real_mpfr
            <class 'sage.rings.complex_mpfr.ComplexNumber'>
            sage: type(0.sqrt(prec=53))                                                 # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>

        Check that :issue:`9466` and :issue:`26509` are fixed::

            sage: 3.sqrt(extend=False, all=True)
            []
            sage: (-1).sqrt(extend=False, all=True)
            []"""
    def sqrtrem(self) -> Any:
        """Integer.sqrtrem(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6366)

        Return `(s, r)` where `s` is the integer square root of ``self`` and
        `r` is the remainder such that `\\text{self} = s^2 + r`.
        Raises :exc:`ValueError` if ``self`` is negative.

        EXAMPLES::

            sage: 25.sqrtrem()
            (5, 0)
            sage: 27.sqrtrem()
            (5, 2)
            sage: 0.sqrtrem()
            (0, 0)

        ::

            sage: Integer(-102).sqrtrem()
            Traceback (most recent call last):
            ...
            ValueError: square root of negative integer not defined"""
    @overload
    def squarefree_part(self, longbound=...) -> Any:
        """Integer.squarefree_part(self, long bound=-1)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5777)

        Return the square free part of `x` (=``self``), i.e., the unique integer
        `z` that `x = z y^2`, with `y^2` a perfect square and `z` square-free.

        Use ``self.radical()`` for the product of the primes that divide ``self``.

        If ``self`` is 0, just returns 0.

        EXAMPLES::

            sage: squarefree_part(100)
            1
            sage: squarefree_part(12)
            3
            sage: squarefree_part(17*37*37)
            17
            sage: squarefree_part(-17*32)
            -34
            sage: squarefree_part(1)
            1
            sage: squarefree_part(-1)
            -1
            sage: squarefree_part(-2)
            -2
            sage: squarefree_part(-4)
            -1

        ::

            sage: a = 8 * 5^6 * 101^2
            sage: a.squarefree_part(bound=2).factor()
            2 * 5^6 * 101^2
            sage: a.squarefree_part(bound=5).factor()
            2 * 101^2
            sage: a.squarefree_part(bound=1000)
            2
            sage: a.squarefree_part(bound=2**14)
            2
            sage: a = 7^3 * next_prime(2^100)^2 * next_prime(2^200)                     # needs sage.libs.pari
            sage: a / a.squarefree_part(bound=1000)                                     # needs sage.libs.pari
            49"""
    @overload
    def squarefree_part(self, bound=...) -> Any:
        """Integer.squarefree_part(self, long bound=-1)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5777)

        Return the square free part of `x` (=``self``), i.e., the unique integer
        `z` that `x = z y^2`, with `y^2` a perfect square and `z` square-free.

        Use ``self.radical()`` for the product of the primes that divide ``self``.

        If ``self`` is 0, just returns 0.

        EXAMPLES::

            sage: squarefree_part(100)
            1
            sage: squarefree_part(12)
            3
            sage: squarefree_part(17*37*37)
            17
            sage: squarefree_part(-17*32)
            -34
            sage: squarefree_part(1)
            1
            sage: squarefree_part(-1)
            -1
            sage: squarefree_part(-2)
            -2
            sage: squarefree_part(-4)
            -1

        ::

            sage: a = 8 * 5^6 * 101^2
            sage: a.squarefree_part(bound=2).factor()
            2 * 5^6 * 101^2
            sage: a.squarefree_part(bound=5).factor()
            2 * 101^2
            sage: a.squarefree_part(bound=1000)
            2
            sage: a.squarefree_part(bound=2**14)
            2
            sage: a = 7^3 * next_prime(2^100)^2 * next_prime(2^200)                     # needs sage.libs.pari
            sage: a / a.squarefree_part(bound=1000)                                     # needs sage.libs.pari
            49"""
    @overload
    def squarefree_part(self, bound=...) -> Any:
        """Integer.squarefree_part(self, long bound=-1)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5777)

        Return the square free part of `x` (=``self``), i.e., the unique integer
        `z` that `x = z y^2`, with `y^2` a perfect square and `z` square-free.

        Use ``self.radical()`` for the product of the primes that divide ``self``.

        If ``self`` is 0, just returns 0.

        EXAMPLES::

            sage: squarefree_part(100)
            1
            sage: squarefree_part(12)
            3
            sage: squarefree_part(17*37*37)
            17
            sage: squarefree_part(-17*32)
            -34
            sage: squarefree_part(1)
            1
            sage: squarefree_part(-1)
            -1
            sage: squarefree_part(-2)
            -2
            sage: squarefree_part(-4)
            -1

        ::

            sage: a = 8 * 5^6 * 101^2
            sage: a.squarefree_part(bound=2).factor()
            2 * 5^6 * 101^2
            sage: a.squarefree_part(bound=5).factor()
            2 * 101^2
            sage: a.squarefree_part(bound=1000)
            2
            sage: a.squarefree_part(bound=2**14)
            2
            sage: a = 7^3 * next_prime(2^100)^2 * next_prime(2^200)                     # needs sage.libs.pari
            sage: a / a.squarefree_part(bound=1000)                                     # needs sage.libs.pari
            49"""
    @overload
    def squarefree_part(self, bound=...) -> Any:
        """Integer.squarefree_part(self, long bound=-1)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5777)

        Return the square free part of `x` (=``self``), i.e., the unique integer
        `z` that `x = z y^2`, with `y^2` a perfect square and `z` square-free.

        Use ``self.radical()`` for the product of the primes that divide ``self``.

        If ``self`` is 0, just returns 0.

        EXAMPLES::

            sage: squarefree_part(100)
            1
            sage: squarefree_part(12)
            3
            sage: squarefree_part(17*37*37)
            17
            sage: squarefree_part(-17*32)
            -34
            sage: squarefree_part(1)
            1
            sage: squarefree_part(-1)
            -1
            sage: squarefree_part(-2)
            -2
            sage: squarefree_part(-4)
            -1

        ::

            sage: a = 8 * 5^6 * 101^2
            sage: a.squarefree_part(bound=2).factor()
            2 * 5^6 * 101^2
            sage: a.squarefree_part(bound=5).factor()
            2 * 101^2
            sage: a.squarefree_part(bound=1000)
            2
            sage: a.squarefree_part(bound=2**14)
            2
            sage: a = 7^3 * next_prime(2^100)^2 * next_prime(2^200)                     # needs sage.libs.pari
            sage: a / a.squarefree_part(bound=1000)                                     # needs sage.libs.pari
            49"""
    @overload
    def squarefree_part(self, bound=...) -> Any:
        """Integer.squarefree_part(self, long bound=-1)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5777)

        Return the square free part of `x` (=``self``), i.e., the unique integer
        `z` that `x = z y^2`, with `y^2` a perfect square and `z` square-free.

        Use ``self.radical()`` for the product of the primes that divide ``self``.

        If ``self`` is 0, just returns 0.

        EXAMPLES::

            sage: squarefree_part(100)
            1
            sage: squarefree_part(12)
            3
            sage: squarefree_part(17*37*37)
            17
            sage: squarefree_part(-17*32)
            -34
            sage: squarefree_part(1)
            1
            sage: squarefree_part(-1)
            -1
            sage: squarefree_part(-2)
            -2
            sage: squarefree_part(-4)
            -1

        ::

            sage: a = 8 * 5^6 * 101^2
            sage: a.squarefree_part(bound=2).factor()
            2 * 5^6 * 101^2
            sage: a.squarefree_part(bound=5).factor()
            2 * 101^2
            sage: a.squarefree_part(bound=1000)
            2
            sage: a.squarefree_part(bound=2**14)
            2
            sage: a = 7^3 * next_prime(2^100)^2 * next_prime(2^200)                     # needs sage.libs.pari
            sage: a / a.squarefree_part(bound=1000)                                     # needs sage.libs.pari
            49"""
    @overload
    def squarefree_part(self, bound=...) -> Any:
        """Integer.squarefree_part(self, long bound=-1)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 5777)

        Return the square free part of `x` (=``self``), i.e., the unique integer
        `z` that `x = z y^2`, with `y^2` a perfect square and `z` square-free.

        Use ``self.radical()`` for the product of the primes that divide ``self``.

        If ``self`` is 0, just returns 0.

        EXAMPLES::

            sage: squarefree_part(100)
            1
            sage: squarefree_part(12)
            3
            sage: squarefree_part(17*37*37)
            17
            sage: squarefree_part(-17*32)
            -34
            sage: squarefree_part(1)
            1
            sage: squarefree_part(-1)
            -1
            sage: squarefree_part(-2)
            -2
            sage: squarefree_part(-4)
            -1

        ::

            sage: a = 8 * 5^6 * 101^2
            sage: a.squarefree_part(bound=2).factor()
            2 * 5^6 * 101^2
            sage: a.squarefree_part(bound=5).factor()
            2 * 101^2
            sage: a.squarefree_part(bound=1000)
            2
            sage: a.squarefree_part(bound=2**14)
            2
            sage: a = 7^3 * next_prime(2^100)^2 * next_prime(2^200)                     # needs sage.libs.pari
            sage: a / a.squarefree_part(bound=1000)                                     # needs sage.libs.pari
            49"""
    @overload
    def str(self, intbase=...) -> Any:
        """Integer.str(self, int base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1075)

        Return the string representation of ``self`` in the
        given base.

        EXAMPLES::

            sage: Integer(2^10).str(2)
            '10000000000'
            sage: Integer(2^10).str(17)
            '394'

        ::

            sage: two = Integer(2)
            sage: two.str(1)
            Traceback (most recent call last):
            ...
            ValueError: base (=1) must be between 2 and 36

        ::

            sage: two.str(37)
            Traceback (most recent call last):
            ...
            ValueError: base (=37) must be between 2 and 36

        ::

            sage: big = 10^5000000
            sage: s = big.str()       # long time (2s on sage.math, 2014)
            sage: len(s)              # long time (depends on above defn of s)
            5000001
            sage: s[:10]              # long time (depends on above defn of s)
            '1000000000'"""
    @overload
    def str(self) -> Any:
        """Integer.str(self, int base=10)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1075)

        Return the string representation of ``self`` in the
        given base.

        EXAMPLES::

            sage: Integer(2^10).str(2)
            '10000000000'
            sage: Integer(2^10).str(17)
            '394'

        ::

            sage: two = Integer(2)
            sage: two.str(1)
            Traceback (most recent call last):
            ...
            ValueError: base (=1) must be between 2 and 36

        ::

            sage: two.str(37)
            Traceback (most recent call last):
            ...
            ValueError: base (=37) must be between 2 and 36

        ::

            sage: big = 10^5000000
            sage: s = big.str()       # long time (2s on sage.math, 2014)
            sage: len(s)              # long time (depends on above defn of s)
            5000001
            sage: s[:10]              # long time (depends on above defn of s)
            '1000000000'"""
    @overload
    def support(self) -> Any:
        """Integer.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4079)

        Return a sorted list of the primes dividing this integer.

        OUTPUT: the sorted list of primes appearing in the factorization of
        this rational with positive exponent

        EXAMPLES::

            sage: factorial(10).support()
            [2, 3, 5, 7]
            sage: (-999).support()
            [3, 37]

        Trying to find the support of 0 raises an :exc:`ArithmeticError`::

            sage: 0.support()
            Traceback (most recent call last):
            ...
            ArithmeticError: support of 0 not defined"""
    @overload
    def support(self) -> Any:
        """Integer.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4079)

        Return a sorted list of the primes dividing this integer.

        OUTPUT: the sorted list of primes appearing in the factorization of
        this rational with positive exponent

        EXAMPLES::

            sage: factorial(10).support()
            [2, 3, 5, 7]
            sage: (-999).support()
            [3, 37]

        Trying to find the support of 0 raises an :exc:`ArithmeticError`::

            sage: 0.support()
            Traceback (most recent call last):
            ...
            ArithmeticError: support of 0 not defined"""
    @overload
    def support(self) -> Any:
        """Integer.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4079)

        Return a sorted list of the primes dividing this integer.

        OUTPUT: the sorted list of primes appearing in the factorization of
        this rational with positive exponent

        EXAMPLES::

            sage: factorial(10).support()
            [2, 3, 5, 7]
            sage: (-999).support()
            [3, 37]

        Trying to find the support of 0 raises an :exc:`ArithmeticError`::

            sage: 0.support()
            Traceback (most recent call last):
            ...
            ArithmeticError: support of 0 not defined"""
    @overload
    def support(self) -> Any:
        """Integer.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4079)

        Return a sorted list of the primes dividing this integer.

        OUTPUT: the sorted list of primes appearing in the factorization of
        this rational with positive exponent

        EXAMPLES::

            sage: factorial(10).support()
            [2, 3, 5, 7]
            sage: (-999).support()
            [3, 37]

        Trying to find the support of 0 raises an :exc:`ArithmeticError`::

            sage: 0.support()
            Traceback (most recent call last):
            ...
            ArithmeticError: support of 0 not defined"""
    def test_bit(self, longindex) -> Any:
        """Integer.test_bit(self, long index)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7025)

        Return the bit at ``index``.

        If the index is negative, returns 0.

        Although internally a sign-magnitude representation is used
        for integers, this method pretends to use a two's complement
        representation.  This is illustrated with a negative integer
        below.

        EXAMPLES::

            sage: w = 6
            sage: w.str(2)
            '110'
            sage: w.test_bit(2)
            1
            sage: w.test_bit(-1)
            0
            sage: x = -20
            sage: x.str(2)
            '-10100'
            sage: x.test_bit(4)
            0
            sage: x.test_bit(5)
            1
            sage: x.test_bit(6)
            1"""
    @overload
    def to_bytes(self, length=..., byteorder=..., is_signed=...) -> Any:
        """Integer.to_bytes(self, length=1, byteorder='big', is_signed=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7192)

        Return an array of bytes representing an integer.

        Internally relies on the python ``int.to_bytes()`` method.

        INPUT:

        - ``length`` -- positive integer (default: 1); integer represented
          in ``length`` bytes
        - ``byteorder`` -- string (default: ``'big'``); determines the byte
          order of the output (can only be ``'big'`` or ``'little'``)
        - ``is_signed`` -- boolean (default: ``False``); determines whether to use two's
          compliment to represent the integer

        .. TODO::

            It should be possible to convert straight from the gmp type in cython.
            This could be significantly faster, but I am unsure of the fastest and cleanest
            way to do this.

        EXAMPLES::

            sage: (1024).to_bytes(2, byteorder='big')
            b'\\x04\\x00'
            sage: (1024).to_bytes(10, byteorder='big')
            b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x04\\x00'
            sage: (-1024).to_bytes(10, byteorder='big', is_signed=True)
            b'\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xfc\\x00'
            sage: x = 1000
            sage: x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
            b'\\xe8\\x03'"""
    @overload
    def to_bytes(self) -> Any:
        """Integer.to_bytes(self, length=1, byteorder='big', is_signed=False)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7192)

        Return an array of bytes representing an integer.

        Internally relies on the python ``int.to_bytes()`` method.

        INPUT:

        - ``length`` -- positive integer (default: 1); integer represented
          in ``length`` bytes
        - ``byteorder`` -- string (default: ``'big'``); determines the byte
          order of the output (can only be ``'big'`` or ``'little'``)
        - ``is_signed`` -- boolean (default: ``False``); determines whether to use two's
          compliment to represent the integer

        .. TODO::

            It should be possible to convert straight from the gmp type in cython.
            This could be significantly faster, but I am unsure of the fastest and cleanest
            way to do this.

        EXAMPLES::

            sage: (1024).to_bytes(2, byteorder='big')
            b'\\x04\\x00'
            sage: (1024).to_bytes(10, byteorder='big')
            b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x04\\x00'
            sage: (-1024).to_bytes(10, byteorder='big', is_signed=True)
            b'\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xfc\\x00'
            sage: x = 1000
            sage: x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
            b'\\xe8\\x03'"""
    @overload
    def trailing_zero_bits(self) -> Any:
        """Integer.trailing_zero_bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1346)

        Return the number of trailing zero bits in ``self``, i.e.
        the exponent of the largest power of 2 dividing ``self``.

        EXAMPLES::

            sage: 11.trailing_zero_bits()
            0
            sage: (-11).trailing_zero_bits()
            0
            sage: (11<<5).trailing_zero_bits()
            5
            sage: (-11<<5).trailing_zero_bits()
            5
            sage: 0.trailing_zero_bits()
            0"""
    @overload
    def trailing_zero_bits(self) -> Any:
        """Integer.trailing_zero_bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1346)

        Return the number of trailing zero bits in ``self``, i.e.
        the exponent of the largest power of 2 dividing ``self``.

        EXAMPLES::

            sage: 11.trailing_zero_bits()
            0
            sage: (-11).trailing_zero_bits()
            0
            sage: (11<<5).trailing_zero_bits()
            5
            sage: (-11<<5).trailing_zero_bits()
            5
            sage: 0.trailing_zero_bits()
            0"""
    @overload
    def trailing_zero_bits(self) -> Any:
        """Integer.trailing_zero_bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1346)

        Return the number of trailing zero bits in ``self``, i.e.
        the exponent of the largest power of 2 dividing ``self``.

        EXAMPLES::

            sage: 11.trailing_zero_bits()
            0
            sage: (-11).trailing_zero_bits()
            0
            sage: (11<<5).trailing_zero_bits()
            5
            sage: (-11<<5).trailing_zero_bits()
            5
            sage: 0.trailing_zero_bits()
            0"""
    @overload
    def trailing_zero_bits(self) -> Any:
        """Integer.trailing_zero_bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1346)

        Return the number of trailing zero bits in ``self``, i.e.
        the exponent of the largest power of 2 dividing ``self``.

        EXAMPLES::

            sage: 11.trailing_zero_bits()
            0
            sage: (-11).trailing_zero_bits()
            0
            sage: (11<<5).trailing_zero_bits()
            5
            sage: (-11<<5).trailing_zero_bits()
            5
            sage: 0.trailing_zero_bits()
            0"""
    @overload
    def trailing_zero_bits(self) -> Any:
        """Integer.trailing_zero_bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1346)

        Return the number of trailing zero bits in ``self``, i.e.
        the exponent of the largest power of 2 dividing ``self``.

        EXAMPLES::

            sage: 11.trailing_zero_bits()
            0
            sage: (-11).trailing_zero_bits()
            0
            sage: (11<<5).trailing_zero_bits()
            5
            sage: (-11<<5).trailing_zero_bits()
            5
            sage: 0.trailing_zero_bits()
            0"""
    @overload
    def trailing_zero_bits(self) -> Any:
        """Integer.trailing_zero_bits(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1346)

        Return the number of trailing zero bits in ``self``, i.e.
        the exponent of the largest power of 2 dividing ``self``.

        EXAMPLES::

            sage: 11.trailing_zero_bits()
            0
            sage: (-11).trailing_zero_bits()
            0
            sage: (11<<5).trailing_zero_bits()
            5
            sage: (-11<<5).trailing_zero_bits()
            5
            sage: 0.trailing_zero_bits()
            0"""
    @overload
    def trial_division(self, longbound=..., longstart=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self, bound=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self, bound=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self, bound=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self, bound=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self, bound=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trial_division(self, start=...) -> Any:
        """Integer.trial_division(self, long bound=LONG_MAX, long start=2)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3718)

        Return smallest prime divisor of ``self`` up to bound, beginning
        checking at ``start``, or ``abs(self)`` if no such divisor is found.

        INPUT:

        - ``bound`` -- positive integer that fits in a C ``signed long``
        - ``start`` -- positive integer that fits in a C ``signed long``

        OUTPUT: a positive integer

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^6)*next_prime(10^7); n.trial_division()
            1000003
            sage: (-n).trial_division()
            1000003
            sage: n.trial_division(bound=100)
            10000049000057
            sage: n.trial_division(bound=-10)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: n.trial_division(bound=0)
            Traceback (most recent call last):
            ...
            ValueError: bound must be positive
            sage: ZZ(0).trial_division()
            Traceback (most recent call last):
            ...
            ValueError: self must be nonzero

            sage: # needs sage.libs.pari
            sage: n = next_prime(10^5) * next_prime(10^40); n.trial_division()
            100003
            sage: n.trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division(bound=10^4)
            1000030000000000000000000000000000000012100363
            sage: (-n).trial_division()
            100003
            sage: n = 2 * next_prime(10^40); n.trial_division()
            2
            sage: n = 3 * next_prime(10^40); n.trial_division()
            3
            sage: n = 5 * next_prime(10^40); n.trial_division()
            5
            sage: n = 2 * next_prime(10^4); n.trial_division()
            2
            sage: n = 3 * next_prime(10^4); n.trial_division()
            3
            sage: n = 5 * next_prime(10^4); n.trial_division()
            5

        You can specify a starting point::

            sage: n = 3*5*101*103
            sage: n.trial_division(start=50)
            101"""
    @overload
    def trunc(self) -> Any:
        """Integer.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4717)

        Round this number to the nearest integer, which is ``self`` since
        ``self`` is an integer.

        EXAMPLES::

            sage: n = 6
            sage: n.trunc()
            6"""
    @overload
    def trunc(self) -> Any:
        """Integer.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4717)

        Round this number to the nearest integer, which is ``self`` since
        ``self`` is an integer.

        EXAMPLES::

            sage: n = 6
            sage: n.trunc()
            6"""
    def val_unit(self, p) -> Any:
        """Integer.val_unit(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4336)

        Return a pair: the `p`-adic valuation of ``self``, and th`p`-adicic unit
        of ``self``.

        INPUT:

        - ``p`` -- integer at least 2

        OUTPUT:

        - ``v_p(self)`` -- the `p`-adic valuation of ``self``

        - ``u_p(self)`` -- ``self`` / `p^{v_p(\\mathrm{self})}`

        EXAMPLES::

            sage: n = 60
            sage: n.val_unit(2)
            (2, 15)
            sage: n.val_unit(3)
            (1, 20)
            sage: n.val_unit(7)
            (0, 60)
            sage: (2^11).val_unit(4)
            (5, 2)
            sage: 0.val_unit(2)
            (+Infinity, 1)"""
    def valuation(self, p) -> Any:
        """Integer.valuation(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 4275)

        Return the `p`-adic valuation of ``self``.

        INPUT:

        - ``p`` -- integer at least 2

        EXAMPLES::

            sage: n = 60
            sage: n.valuation(2)
            2
            sage: n.valuation(3)
            1
            sage: n.valuation(7)
            0
            sage: n.valuation(1)
            Traceback (most recent call last):
            ...
            ValueError: You can only compute the valuation with respect to a integer larger than 1.

        We do not require that ``p`` is a prime::

            sage: (2^11).valuation(4)
            5"""
    def xgcd(self, Integern) -> Any:
        """Integer.xgcd(self, Integer n)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6526)

        Return the extended gcd of this element and ``n``.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        A triple ``(g, s, t)`` such that ``g`` is the nonnegative gcd of
        ``self`` and ``n``, and ``s`` and ``t`` are cofactors satisfying the
        Bezout identity

        .. MATH::

            g = s \\cdot \\mathrm{self} + t \\cdot n.

        .. NOTE::

            There is no guarantee that the cofactors will be minimal. If you
            need the cofactors to be minimal use :meth:`_xgcd`. Also, using
            :meth:`_xgcd` directly might be faster in some cases, see
            :issue:`13628`.

        EXAMPLES::

            sage: 6.xgcd(4)
            (2, 1, -1)"""
    def __abs__(self) -> Any:
        """Integer.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3286)

        Compute ``|self|``.

        EXAMPLES::

            sage: z = -1
            sage: abs(z)
            1
            sage: abs(z) == abs(1)
            True"""
    def __add__(self, left, right) -> Any:
        """Integer.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1763)

        TESTS::

            sage: 1 + 2
            3
            sage: sum(Integer(i) for i in [1..100])
            5050
            sage: 1 + 2/3
            5/3
            sage: 1 + (-2/3)
            1/3"""
    @overload
    def __and__(self, x, y) -> Any:
        """Integer.__and__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6839)

        Return the bitwise and two integers.

        EXAMPLES::

            sage: n = Integer(6);  m = Integer(2)
            sage: n & m
            2
            sage: n.__and__(m)
            2"""
    @overload
    def __and__(self, m) -> Any:
        """Integer.__and__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6839)

        Return the bitwise and two integers.

        EXAMPLES::

            sage: n = Integer(6);  m = Integer(2)
            sage: n & m
            2
            sage: n.__and__(m)
            2"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Integer.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 947)

        EXAMPLES::

            sage: n = 2
            sage: copy(n)
            2
            sage: copy(n) is n
            True"""
    def __deepcopy__(self, memo) -> Any:
        """Integer.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 960)

        EXAMPLES::

            sage: n = 2
            sage: deepcopy(n) is n
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    @overload
    def __float__(self) -> Any:
        """Integer.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3620)

        Return double precision floating point representation of this
        integer.

        EXAMPLES::

            sage: n = Integer(17); float(n)
            17.0
            sage: n = Integer(902834098234908209348209834092834098); float(n)
            9.028340982349083e+35
            sage: n = Integer(-57); float(n)
            -57.0
            sage: n.__float__()
            -57.0
            sage: type(n.__float__())
            <... 'float'>"""
    @overload
    def __float__(self) -> Any:
        """Integer.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3620)

        Return double precision floating point representation of this
        integer.

        EXAMPLES::

            sage: n = Integer(17); float(n)
            17.0
            sage: n = Integer(902834098234908209348209834092834098); float(n)
            9.028340982349083e+35
            sage: n = Integer(-57); float(n)
            -57.0
            sage: n.__float__()
            -57.0
            sage: type(n.__float__())
            <... 'float'>"""
    @overload
    def __float__(self) -> Any:
        """Integer.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3620)

        Return double precision floating point representation of this
        integer.

        EXAMPLES::

            sage: n = Integer(17); float(n)
            17.0
            sage: n = Integer(902834098234908209348209834092834098); float(n)
            9.028340982349083e+35
            sage: n = Integer(-57); float(n)
            -57.0
            sage: n.__float__()
            -57.0
            sage: type(n.__float__())
            <... 'float'>"""
    def __format__(self, *args, **kwargs) -> Any:
        '''Integer.__format__(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1124)

        Return a string representation using Python\'s Format protocol.
        Valid format descriptions are exactly those for Python integers.

        EXAMPLES::

            sage: "{0:#x}; {0:#b}; {0:+05d}".format(ZZ(17))
            \'0x11; 0b10001; +0017\''''
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """Integer.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3655)

        Return the hash of this integer.

        This agrees with the Python hash of the corresponding Python int or
        long.

        EXAMPLES::

            sage: n = -920384; n.__hash__()
            -920384
            sage: hash(int(n))
            -920384
            sage: n = -920390823904823094890238490238484
            sage: n.__hash__()    # random
            -43547310504077801
            sage: n.__hash__() == hash(int(n))
            True

        TESTS::

            sage: hash(-1), hash(0), hash(1)
            (-2, 0, 1)
            sage: n = 2^31 + 2^63 + 2^95 + 2^127 + 2^128*(2^32-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True
            sage: n = 2^63 + 2^127 + 2^191 + 2^255 + 2^256*(2^64-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True

        These tests come from :issue:`4957`::

            sage: n = 2^31 + 2^13
            sage: hash(n)             # random
            2147491840
            sage: hash(n) == hash(int(n))
            True
            sage: n = 2^63 + 2^13
            sage: hash(n)             # random
            8196
            sage: hash(n) == hash(int(n))
            True"""
    @overload
    def __hash__(self) -> Any:
        """Integer.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3655)

        Return the hash of this integer.

        This agrees with the Python hash of the corresponding Python int or
        long.

        EXAMPLES::

            sage: n = -920384; n.__hash__()
            -920384
            sage: hash(int(n))
            -920384
            sage: n = -920390823904823094890238490238484
            sage: n.__hash__()    # random
            -43547310504077801
            sage: n.__hash__() == hash(int(n))
            True

        TESTS::

            sage: hash(-1), hash(0), hash(1)
            (-2, 0, 1)
            sage: n = 2^31 + 2^63 + 2^95 + 2^127 + 2^128*(2^32-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True
            sage: n = 2^63 + 2^127 + 2^191 + 2^255 + 2^256*(2^64-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True

        These tests come from :issue:`4957`::

            sage: n = 2^31 + 2^13
            sage: hash(n)             # random
            2147491840
            sage: hash(n) == hash(int(n))
            True
            sage: n = 2^63 + 2^13
            sage: hash(n)             # random
            8196
            sage: hash(n) == hash(int(n))
            True"""
    @overload
    def __hash__(self) -> Any:
        """Integer.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3655)

        Return the hash of this integer.

        This agrees with the Python hash of the corresponding Python int or
        long.

        EXAMPLES::

            sage: n = -920384; n.__hash__()
            -920384
            sage: hash(int(n))
            -920384
            sage: n = -920390823904823094890238490238484
            sage: n.__hash__()    # random
            -43547310504077801
            sage: n.__hash__() == hash(int(n))
            True

        TESTS::

            sage: hash(-1), hash(0), hash(1)
            (-2, 0, 1)
            sage: n = 2^31 + 2^63 + 2^95 + 2^127 + 2^128*(2^32-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True
            sage: n = 2^63 + 2^127 + 2^191 + 2^255 + 2^256*(2^64-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True

        These tests come from :issue:`4957`::

            sage: n = 2^31 + 2^13
            sage: hash(n)             # random
            2147491840
            sage: hash(n) == hash(int(n))
            True
            sage: n = 2^63 + 2^13
            sage: hash(n)             # random
            8196
            sage: hash(n) == hash(int(n))
            True"""
    @overload
    def __hash__(self) -> Any:
        """Integer.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3655)

        Return the hash of this integer.

        This agrees with the Python hash of the corresponding Python int or
        long.

        EXAMPLES::

            sage: n = -920384; n.__hash__()
            -920384
            sage: hash(int(n))
            -920384
            sage: n = -920390823904823094890238490238484
            sage: n.__hash__()    # random
            -43547310504077801
            sage: n.__hash__() == hash(int(n))
            True

        TESTS::

            sage: hash(-1), hash(0), hash(1)
            (-2, 0, 1)
            sage: n = 2^31 + 2^63 + 2^95 + 2^127 + 2^128*(2^32-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True
            sage: n = 2^63 + 2^127 + 2^191 + 2^255 + 2^256*(2^64-2)
            sage: hash(n) == hash(int(n))
            True
            sage: hash(n-1) == hash(int(n-1))
            True
            sage: hash(-n) == hash(int(-n))
            True
            sage: hash(1-n) == hash(int(1-n))
            True

        These tests come from :issue:`4957`::

            sage: n = 2^31 + 2^13
            sage: hash(n)             # random
            2147491840
            sage: hash(n) == hash(int(n))
            True
            sage: n = 2^63 + 2^13
            sage: hash(n)             # random
            8196
            sage: hash(n) == hash(int(n))
            True"""
    def __index__(self) -> Any:
        """Integer.__index__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 748)

        Needed so integers can be used as list indices.

        EXAMPLES::

            sage: v = [1,2,3,4,5]
            sage: v[Integer(3)]
            4
            sage: v[Integer(2):Integer(4)]
            [3, 4]

        See :issue:`20750`::

            sage: import re
            sage: p = re.compile('(a)b')
            sage: m = p.match('ab')
            sage: m.group(Integer(0))
            'ab'
            sage: m.group(Integer(1))
            'a'"""
    @overload
    def __int__(self) -> Any:
        """Integer.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3595)

        Return the Python int corresponding to this Sage integer.

        EXAMPLES::

            sage: n = 920938
            sage: int(n)
            920938
            sage: int(-n)
            -920938
            sage: type(n.__int__())
            <... 'int'>
            sage: n = 99028390823409823904823098490238409823490820938
            sage: int(n)
            99028390823409823904823098490238409823490820938
            sage: int(-n)
            -99028390823409823904823098490238409823490820938
            sage: type(n.__int__())
            <class 'int'>
            sage: int(-1), int(0), int(1)
            (-1, 0, 1)"""
    @overload
    def __int__(self) -> Any:
        """Integer.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3595)

        Return the Python int corresponding to this Sage integer.

        EXAMPLES::

            sage: n = 920938
            sage: int(n)
            920938
            sage: int(-n)
            -920938
            sage: type(n.__int__())
            <... 'int'>
            sage: n = 99028390823409823904823098490238409823490820938
            sage: int(n)
            99028390823409823904823098490238409823490820938
            sage: int(-n)
            -99028390823409823904823098490238409823490820938
            sage: type(n.__int__())
            <class 'int'>
            sage: int(-1), int(0), int(1)
            (-1, 0, 1)"""
    @overload
    def __int__(self) -> Any:
        """Integer.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3595)

        Return the Python int corresponding to this Sage integer.

        EXAMPLES::

            sage: n = 920938
            sage: int(n)
            920938
            sage: int(-n)
            -920938
            sage: type(n.__int__())
            <... 'int'>
            sage: n = 99028390823409823904823098490238409823490820938
            sage: int(n)
            99028390823409823904823098490238409823490820938
            sage: int(-n)
            -99028390823409823904823098490238409823490820938
            sage: type(n.__int__())
            <class 'int'>
            sage: int(-1), int(0), int(1)
            (-1, 0, 1)"""
    @overload
    def __invert__(self) -> Any:
        """Integer.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6874)

        Return the multiplicative inverse of ``self``, as a rational number.

        EXAMPLES::

            sage: n = 10
            sage: 1/n
            1/10
            sage: n.__invert__()
            1/10
            sage: n = -3
            sage: ~n
            -1/3"""
    @overload
    def __invert__(self) -> Any:
        """Integer.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6874)

        Return the multiplicative inverse of ``self``, as a rational number.

        EXAMPLES::

            sage: n = 10
            sage: 1/n
            1/10
            sage: n.__invert__()
            1/10
            sage: n = -3
            sage: ~n
            -1/3"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lshift__(self, x, y) -> Any:
        """Integer.__lshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6771)

        Shift x to the left by y bits.

        EXAMPLES::

            sage: 32 << 2
            128
            sage: 32 << int(2)
            128
            sage: int(32) << 2
            128
            sage: 1 << 2.5                                                              # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            TypeError: unsupported operands for <<: 1, 2.5000...

            sage: 32 << (4/2)
            128

        A negative shift to the left is treated as a right shift::

            sage: 128 << -2
            32
            sage: 128 << (-2^100)
            0"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, x, y) -> Any:
        """Integer.__mod__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3338)

        Return x modulo y.

        EXAMPLES::

            sage: z = 43
            sage: z % 2
            1
            sage: z % 0
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Integer modulo by zero
            sage: -5 % 7
            2
            sage: -5 % -7
            -5
            sage: 5 % -7
            -2
            sage: 5 % int(-7)
            -2
            sage: int(5) % -7
            -2
            sage: int(5) % int(-7)
            -2

        TESTS::

            sage: signs = [(11,5), (11,-5), (-11,5), (-11,-5)]
            sage: control = [int(a) % int(b) for a, b in signs]
            sage: [a % b for a,b in signs] == control
            True
            sage: [a % int(b) for a,b in signs] == control
            True
            sage: [int(a) % b for a,b in signs] == control
            True

        This example caused trouble in :issue:`6083`::

            sage: a = next_prime(2**31)                                                 # needs sage.libs.pari
            sage: b = Integers(a)(100)                                                  # needs sage.libs.pari
            sage: a % b                                                                 # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ArithmeticError: reduction modulo 100 not defined"""
    @overload
    def __mpz__(self) -> Any:
        '''Integer.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1053)

        Return a gmpy2 integer.

        EXAMPLES::

            sage: a = 5
            sage: a.__mpz__()
            mpz(5)
            sage: from gmpy2 import mpz
            sage: mpz(a)
            mpz(5)

        TESTS::

            sage: a.__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpz__(self) -> Any:
        '''Integer.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1053)

        Return a gmpy2 integer.

        EXAMPLES::

            sage: a = 5
            sage: a.__mpz__()
            mpz(5)
            sage: from gmpy2 import mpz
            sage: mpz(a)
            mpz(5)

        TESTS::

            sage: a.__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpz__(self) -> Any:
        '''Integer.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1053)

        Return a gmpy2 integer.

        EXAMPLES::

            sage: a = 5
            sage: a.__mpz__()
            mpz(5)
            sage: from gmpy2 import mpz
            sage: mpz(a)
            mpz(5)

        TESTS::

            sage: a.__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    def __mul__(self, left, right) -> Any:
        """Integer.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1958)

        TESTS::

            sage: 3 * 2
            6
            sage: 5 * QQ((2,3))
            10/3
            sage: 3 * (-5/6)
            -5/2
            sage: (-2) * (-5/4)
            5/2"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """Integer.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1898)

        TESTS::

            sage: a = Integer(3)
            sage: -a
            -3
            sage: a = Integer(3^100); a
            515377520732011331036461129765621272702107522001
            sage: -a
            -515377520732011331036461129765621272702107522001"""
    @overload
    def __or__(self, x, y) -> Any:
        """Integer.__or__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6860)

        Return the bitwise or of the integers x and y.

        EXAMPLES::

            sage: n = 8; m = 4
            sage: n.__or__(m)
            12"""
    @overload
    def __or__(self, m) -> Any:
        """Integer.__or__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6860)

        Return the bitwise or of the integers x and y.

        EXAMPLES::

            sage: n = 8; m = 4
            sage: n.__or__(m)
            12"""
    @overload
    def __pari__(self) -> Any:
        """Integer.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6227)

        Return the PARI version of this integer.

        EXAMPLES::

            sage: n = 9390823
            sage: m = n.__pari__(); m                                                   # needs sage.libs.pari
            9390823
            sage: type(m)                                                               # needs sage.libs.pari
            <class 'cypari2.gen.Gen'>

        TESTS::

            sage: n = 10^10000000
            sage: m = n.__pari__()  # crash from trac 875                               # needs sage.libs.pari
            sage: m % 1234567                                                           # needs sage.libs.pari
            1041334"""
    @overload
    def __pari__(self) -> Any:
        """Integer.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6227)

        Return the PARI version of this integer.

        EXAMPLES::

            sage: n = 9390823
            sage: m = n.__pari__(); m                                                   # needs sage.libs.pari
            9390823
            sage: type(m)                                                               # needs sage.libs.pari
            <class 'cypari2.gen.Gen'>

        TESTS::

            sage: n = 10^10000000
            sage: m = n.__pari__()  # crash from trac 875                               # needs sage.libs.pari
            sage: m % 1234567                                                           # needs sage.libs.pari
            1041334"""
    @overload
    def __pari__(self) -> Any:
        """Integer.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6227)

        Return the PARI version of this integer.

        EXAMPLES::

            sage: n = 9390823
            sage: m = n.__pari__(); m                                                   # needs sage.libs.pari
            9390823
            sage: type(m)                                                               # needs sage.libs.pari
            <class 'cypari2.gen.Gen'>

        TESTS::

            sage: n = 10^10000000
            sage: m = n.__pari__()  # crash from trac 875                               # needs sage.libs.pari
            sage: m % 1234567                                                           # needs sage.libs.pari
            1041334"""
    @overload
    def __pos__(self) -> Any:
        """Integer.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3276)

        EXAMPLES::

            sage: z=43434
            sage: z.__pos__()
            43434"""
    @overload
    def __pos__(self) -> Any:
        """Integer.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 3276)

        EXAMPLES::

            sage: z=43434
            sage: z.__pos__()
            43434"""
    def __pow__(self, left, right, modulus) -> Any:
        """Integer.__pow__(left, right, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2123)

        Return ``(left ^ right) % modulus``.

        EXAMPLES::

            sage: 2^-6
            1/64
            sage: 2^6
            64
            sage: 2^0
            1
            sage: 2^-0
            1
            sage: (-1)^(1/3)                                                            # needs sage.symbolic
            (-1)^(1/3)

        For consistency with Python and MPFR, 0^0 is defined to be 1 in
        Sage::

            sage: 0^0
            1

        See also `<http://www.faqs.org/faqs/sci-math-faq/0to0/>`_ and
        `<https://math.stackexchange.com/questions/11150/zero-to-the-zero-power-is-00-1>`_.

        The base need not be a Sage integer. If it is a Python type, the
        result is a Python type too::

            sage: r = int(2) ^ 10; r; type(r)
            1024
            <... 'int'>
            sage: r = int(3) ^ -3; r; type(r)
            0.037037037037037035
            <... 'float'>
            sage: r = float(2.5) ^ 10; r; type(r)
            9536.7431640625
            <... 'float'>

        We raise 2 to various interesting exponents::

            sage: 2^x                # symbolic x                                       # needs sage.symbolic
            2^x
            sage: 2^1.5              # real number                                      # needs sage.rings.real_mpfr
            2.82842712474619
            sage: 2^float(1.5)       # python float  abs tol 3e-16
            2.8284271247461903
            sage: 2^I                # complex number                                   # needs sage.symbolic
            2^I
            sage: r = 2 ^ int(-3); r; type(r)
            1/8
            <class 'sage.rings.rational.Rational'>
            sage: f = 2^(sin(x)-cos(x)); f                                              # needs sage.symbolic
            2^(-cos(x) + sin(x))
            sage: f(x=3)                                                                # needs sage.symbolic
            2^(-cos(3) + sin(3))

        A symbolic sum::

            sage: # needs sage.symbolic
            sage: x, y, z = var('x,y,z')
            sage: 2^(x + y + z)
            2^(x + y + z)
            sage: 2^(1/2)
            sqrt(2)
            sage: 2^(-1/2)
            1/2*sqrt(2)

        TESTS::

            sage: R.<t> = QQ[]
            sage: 2^t
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Univariate Polynomial
            Ring in t over Rational Field to Rational Field

        Test for :issue:`34143`::

            sage: pow(5,7,13).parent()
            Integer Ring"""
    def __radd__(self, other):
        """Return value+self."""
    def __rand__(self, other):
        """Return value&self."""
    @overload
    def __reduce__(self) -> Any:
        """Integer.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 725)

        This is used when pickling integers.

        EXAMPLES::

            sage: n = 5
            sage: t = n.__reduce__(); t
            (<cyfunction make_integer at ...>, ('5',))
            sage: t[0](*t[1])
            5
            sage: loads(dumps(n)) == n
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Integer.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 725)

        This is used when pickling integers.

        EXAMPLES::

            sage: n = 5
            sage: t = n.__reduce__(); t
            (<cyfunction make_integer at ...>, ('5',))
            sage: t[0](*t[1])
            5
            sage: loads(dumps(n)) == n
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __ror__(self, other):
        """Return value|self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, x, y) -> Any:
        """Integer.__rshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 6804)

        Shift x to the right by y bits.

        EXAMPLES::

            sage: 32 >> 2
            8
            sage: 32 >> int(2)
            8
            sage: int(32) >> 2
            8
            sage: 1 >> 2.5                                                              # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            TypeError: unsupported operands for >>: 1, 2.5000...
            sage: 10^5 >> 10^100
            0

        A negative shift to the right is treated as a left shift::

            sage: 8 >> -2
            32"""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __rxor__(self, other):
        """Return value^self."""
    def __sub__(self, left, right) -> Any:
        """Integer.__sub__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 1846)

        TESTS::

            sage: 1 - 2
            -1
            sage: 1 - 2/3
            1/3
            sage: 1 - (-2/3)
            5/3
            sage: (-1) - (-5/4)
            1/4"""
    def __truediv__(self, left, right) -> Any:
        """Integer.__truediv__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 2009)

        TESTS::

            sage: 3 / 2
            3/2
            sage: 5 / QQ((10,3))
            3/2
            sage: 3 / (-5/6)
            -18/5
            sage: (-2) / (-5/4)
            8/5
            sage: 3 / polygen(ZZ)
            3/x

            sage: 3 / 0
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
            sage: 3 / QQ.zero()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
            sage: 3 / QQbar.zero()                                                      # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero in algebraic field"""
    @overload
    def __xor__(self, x, y) -> Any:
        """Integer.__xor__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 793)

        Compute the exclusive or of x and y.

        EXAMPLES::

            sage: n = ZZ(2); m = ZZ(3)
            sage: n.__xor__(m)
            1"""
    @overload
    def __xor__(self, m) -> Any:
        """Integer.__xor__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 793)

        Compute the exclusive or of x and y.

        EXAMPLES::

            sage: n = ZZ(2); m = ZZ(3)
            sage: n.__xor__(m)
            1"""

class IntegerWrapper(Integer):
    '''IntegerWrapper(parent=None, x=None, unsigned int base=0)

    File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 355)

    Rationale for the :class:`IntegerWrapper` class:

    With :class:`Integer` objects, the allocation/deallocation function slots are
    hijacked with custom functions that stick already allocated
    :class:`Integer` objects (with initialized ``parent`` and ``mpz_t`` fields)
    into a pool on "deallocation" and then pull them out whenever a
    new one is needed. Because :class:`Integers` objects are so common, this is
    actually a significant savings. However, this does cause issues
    with subclassing a Python class directly from :class:`Integer` (but
    that\'s ok for a Cython class).

    As a workaround, one can instead derive a class from the
    intermediate class :class:`IntegerWrapper`, which sets statically its
    alloc/dealloc methods to the *original* :class:`Integer` alloc/dealloc
    methods, before they are swapped manually for the custom ones.

    The constructor of :class:`IntegerWrapper` further allows for
    specifying an alternative parent to :class:`IntegerRing`.'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent=..., x=..., unsignedintbase=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 377)

                We illustrate how to create integers with parents different
                from :class:`IntegerRing`::

                    sage: from sage.rings.integer import IntegerWrapper

                    sage: n = IntegerWrapper(Primes(), 3) # indirect doctest
                    sage: n
                    3
                    sage: n.parent()
                    Set of all prime numbers: 2, 3, 5, 7, ...

                Pickling seems to work now (as of :issue:`10314`)::

                    sage: nn = loads(dumps(n))
                    sage: nn
                    3
                    sage: nn.parent()
                    Integer Ring

                    sage: TestSuite(n).run()
        """

class int_to_Z(sage.categories.morphism.Morphism):
    """int_to_Z()

    File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7470)

    EXAMPLES::

        sage: f = ZZ.coerce_map_from(int)
        sage: f
        Native morphism:
          From: Set of Python objects of class 'int'
          To:   Integer Ring
        sage: f(1rL)
        1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/integer.pyx (starting at line 7482)"""
