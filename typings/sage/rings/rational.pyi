import _cython_3_2_1
import sage as sage
import sage.categories.map
import sage.categories.morphism
import sage.structure.element
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

RealDouble_classes: tuple
RealNumber_classes: tuple
__pyx_capi__: dict
integer_rational_power: _cython_3_2_1.cython_function_or_method
is_Rational: _cython_3_2_1.cython_function_or_method
make_rational: _cython_3_2_1.cython_function_or_method
new_gen_from_rational: None
rational_power_parts: _cython_3_2_1.cython_function_or_method
set_rational_from_gen: None

class Q_to_Z(sage.categories.map.Map):
    """File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4176)

        A morphism from `\\QQ` to `\\ZZ`.

        TESTS::

            sage: type(ZZ.convert_map_from(QQ))
            <class 'sage.rings.rational.Q_to_Z'>
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def section(self) -> Any:
        """Q_to_Z.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4205)

        Return a section of this morphism.

        EXAMPLES::

            sage: sage.rings.rational.Q_to_Z(QQ, ZZ).section()
            Natural morphism:
              From: Integer Ring
              To:   Rational Field"""
    @overload
    def section(self) -> Any:
        """Q_to_Z.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4205)

        Return a section of this morphism.

        EXAMPLES::

            sage: sage.rings.rational.Q_to_Z(QQ, ZZ).section()
            Natural morphism:
              From: Integer Ring
              To:   Rational Field"""

class Rational(sage.structure.element.FieldElement):
    '''Rational(x=None, unsigned int base=0)

    File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 413)

    A rational number.

    Rational numbers are implemented using the GMP C library.

    EXAMPLES::

        sage: a = -2/3
        sage: type(a)
        <class \'sage.rings.rational.Rational\'>
        sage: parent(a)
        Rational Field
        sage: Rational(\'1/0\')
        Traceback (most recent call last):
        ...
        TypeError: unable to convert \'1/0\' to a rational
        sage: Rational(1.5)
        3/2
        sage: Rational(\'9/6\')
        3/2
        sage: Rational((2^99,2^100))
        1/2
        sage: Rational(("2", "10"), 16)
        1/8
        sage: Rational(QQbar(125/8).nth_root(3))                                        # needs sage.rings.number_field
        5/2
        sage: Rational(AA(209735/343 - 17910/49*golden_ratio).nth_root(3)               # needs sage.rings.number_field sage.symbolic
        ....:          + 3*AA(golden_ratio))
        53/7
        sage: QQ(float(1.5))
        3/2
        sage: QQ(RDF(1.2))
        6/5

    Conversion from fractions::

        sage: import fractions
        sage: f = fractions.Fraction(1r, 2r)
        sage: Rational(f)
        1/2

    Conversion from PARI::

        sage: Rational(pari(\'-939082/3992923\'))                                         # needs sage.libs.pari
        -939082/3992923
        sage: Rational(pari(\'Pol([-1/2])\'))  #9595                                      # needs sage.libs.pari
        -1/2

    Conversions from numpy::

        sage: # needs numpy
        sage: import numpy as np
        sage: QQ(np.int8(\'-15\'))
        -15
        sage: QQ(np.int16(\'-32\'))
        -32
        sage: QQ(np.int32(\'-19\'))
        -19
        sage: QQ(np.uint32(\'1412\'))
        1412

        sage: QQ(np.float16(\'12\'))                                                      # needs numpy
        12

    Conversions from gmpy2::

        sage: from gmpy2 import *
        sage: QQ(mpq(\'3/4\'))
        3/4
        sage: QQ(mpz(42))
        42
        sage: Rational(mpq(2/3))
        2/3
        sage: Rational(mpz(5))
        5

    TESTS:

    Check that :issue:`28321` is fixed::

        sage: QQ((2r^100r, 3r^100r))
        1267650600228229401496703205376/515377520732011331036461129765621272702107522001
        sage: QQ((-2r^100r, -3r^100r))
        1267650600228229401496703205376/515377520732011331036461129765621272702107522001'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    __array_interface__: Incomplete
    @overload
    def __init__(self, x=..., unsignedintbase=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 513)

                Create a new rational number.

                INPUT:

                - ``x`` -- object (default: ``None``)

                - ``base`` -- base if ``x`` is a string

                EXAMPLES::

                    sage: a = Rational()
                    sage: a.__init__(7); a
                    7
                    sage: a.__init__('70', base=8); a
                    56
                    sage: a.__init__(pari('2/3')); a                                            # needs sage.libs.pari
                    2/3
                    sage: a.__init__('-h/3ki', 32); a
                    -17/3730
                    sage: from gmpy2 import mpq
                    sage: a.__init__(mpq('3/5')); a
                    3/5

                TESTS:

                Check that :issue:`19835` is fixed::

                    sage: QQ((0r,-1r))
                    0
                    sage: QQ((-1r,-1r))
                    1

                .. NOTE::

                   This is for doctesting purposes only.  Rationals are defined
                   to be immutable.
        """
    @overload
    def __init__(self, AA(209735/343-17910/49*golden_ratio).nth_root(3)# needs sage.rings.number_field sage.symbolic
....) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 513)

                Create a new rational number.

                INPUT:

                - ``x`` -- object (default: ``None``)

                - ``base`` -- base if ``x`` is a string

                EXAMPLES::

                    sage: a = Rational()
                    sage: a.__init__(7); a
                    7
                    sage: a.__init__('70', base=8); a
                    56
                    sage: a.__init__(pari('2/3')); a                                            # needs sage.libs.pari
                    2/3
                    sage: a.__init__('-h/3ki', 32); a
                    -17/3730
                    sage: from gmpy2 import mpq
                    sage: a.__init__(mpq('3/5')); a
                    3/5

                TESTS:

                Check that :issue:`19835` is fixed::

                    sage: QQ((0r,-1r))
                    0
                    sage: QQ((-1r,-1r))
                    1

                .. NOTE::

                   This is for doctesting purposes only.  Rationals are defined
                   to be immutable.
        """
    @overload
    def __init__(self, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 513)

                Create a new rational number.

                INPUT:

                - ``x`` -- object (default: ``None``)

                - ``base`` -- base if ``x`` is a string

                EXAMPLES::

                    sage: a = Rational()
                    sage: a.__init__(7); a
                    7
                    sage: a.__init__('70', base=8); a
                    56
                    sage: a.__init__(pari('2/3')); a                                            # needs sage.libs.pari
                    2/3
                    sage: a.__init__('-h/3ki', 32); a
                    -17/3730
                    sage: from gmpy2 import mpq
                    sage: a.__init__(mpq('3/5')); a
                    3/5

                TESTS:

                Check that :issue:`19835` is fixed::

                    sage: QQ((0r,-1r))
                    0
                    sage: QQ((-1r,-1r))
                    1

                .. NOTE::

                   This is for doctesting purposes only.  Rationals are defined
                   to be immutable.
        """
    @overload
    def absolute_norm(self) -> Any:
        """Rational.absolute_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2890)

        Return the norm from Q to Q of x (which is just x). This was added for
        compatibility with NumberFields.

        EXAMPLES::

            sage: (6/5).absolute_norm()
            6/5

            sage: QQ(7/5).absolute_norm()
            7/5"""
    @overload
    def absolute_norm(self) -> Any:
        """Rational.absolute_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2890)

        Return the norm from Q to Q of x (which is just x). This was added for
        compatibility with NumberFields.

        EXAMPLES::

            sage: (6/5).absolute_norm()
            6/5

            sage: QQ(7/5).absolute_norm()
            7/5"""
    @overload
    def absolute_norm(self) -> Any:
        """Rational.absolute_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2890)

        Return the norm from Q to Q of x (which is just x). This was added for
        compatibility with NumberFields.

        EXAMPLES::

            sage: (6/5).absolute_norm()
            6/5

            sage: QQ(7/5).absolute_norm()
            7/5"""
    @overload
    def additive_order(self) -> Any:
        """Rational.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3524)

        Return the additive order of ``self``.

        OUTPUT: integer or infinity

        EXAMPLES::

            sage: QQ(0).additive_order()
            1
            sage: QQ(1).additive_order()
            +Infinity"""
    @overload
    def additive_order(self) -> Any:
        """Rational.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3524)

        Return the additive order of ``self``.

        OUTPUT: integer or infinity

        EXAMPLES::

            sage: QQ(0).additive_order()
            1
            sage: QQ(1).additive_order()
            +Infinity"""
    @overload
    def additive_order(self) -> Any:
        """Rational.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3524)

        Return the additive order of ``self``.

        OUTPUT: integer or infinity

        EXAMPLES::

            sage: QQ(0).additive_order()
            1
            sage: QQ(1).additive_order()
            +Infinity"""
    @overload
    def as_integer_ratio(self) -> Any:
        """Rational.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3078)

        Return the pair ``(self.numerator(), self.denominator())``.

        EXAMPLES::

            sage: x = -12/29
            sage: x.as_integer_ratio()
            (-12, 29)"""
    @overload
    def as_integer_ratio(self) -> Any:
        """Rational.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3078)

        Return the pair ``(self.numerator(), self.denominator())``.

        EXAMPLES::

            sage: x = -12/29
            sage: x.as_integer_ratio()
            (-12, 29)"""
    @overload
    def ceil(self) -> Any:
        """Rational.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3333)

        Return the ceiling of this rational number.

        OUTPUT: integer

        If this rational number is an integer, this returns this number,
        otherwise it returns the floor of this number +1.

        EXAMPLES::

            sage: n = 5/3; n.ceil()
            2
            sage: n = -17/19; n.ceil()
            0
            sage: n = -7/2; n.ceil()
            -3
            sage: n = 7/2; n.ceil()
            4
            sage: n = 10/2; n.ceil()
            5"""
    @overload
    def ceil(self) -> Any:
        """Rational.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3333)

        Return the ceiling of this rational number.

        OUTPUT: integer

        If this rational number is an integer, this returns this number,
        otherwise it returns the floor of this number +1.

        EXAMPLES::

            sage: n = 5/3; n.ceil()
            2
            sage: n = -17/19; n.ceil()
            0
            sage: n = -7/2; n.ceil()
            -3
            sage: n = 7/2; n.ceil()
            4
            sage: n = 10/2; n.ceil()
            5"""
    @overload
    def ceil(self) -> Any:
        """Rational.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3333)

        Return the ceiling of this rational number.

        OUTPUT: integer

        If this rational number is an integer, this returns this number,
        otherwise it returns the floor of this number +1.

        EXAMPLES::

            sage: n = 5/3; n.ceil()
            2
            sage: n = -17/19; n.ceil()
            0
            sage: n = -7/2; n.ceil()
            -3
            sage: n = 7/2; n.ceil()
            4
            sage: n = 10/2; n.ceil()
            5"""
    @overload
    def ceil(self) -> Any:
        """Rational.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3333)

        Return the ceiling of this rational number.

        OUTPUT: integer

        If this rational number is an integer, this returns this number,
        otherwise it returns the floor of this number +1.

        EXAMPLES::

            sage: n = 5/3; n.ceil()
            2
            sage: n = -17/19; n.ceil()
            0
            sage: n = -7/2; n.ceil()
            -3
            sage: n = 7/2; n.ceil()
            4
            sage: n = 10/2; n.ceil()
            5"""
    @overload
    def ceil(self) -> Any:
        """Rational.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3333)

        Return the ceiling of this rational number.

        OUTPUT: integer

        If this rational number is an integer, this returns this number,
        otherwise it returns the floor of this number +1.

        EXAMPLES::

            sage: n = 5/3; n.ceil()
            2
            sage: n = -17/19; n.ceil()
            0
            sage: n = -7/2; n.ceil()
            -3
            sage: n = 7/2; n.ceil()
            4
            sage: n = 10/2; n.ceil()
            5"""
    @overload
    def ceil(self) -> Any:
        """Rational.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3333)

        Return the ceiling of this rational number.

        OUTPUT: integer

        If this rational number is an integer, this returns this number,
        otherwise it returns the floor of this number +1.

        EXAMPLES::

            sage: n = 5/3; n.ceil()
            2
            sage: n = -17/19; n.ceil()
            0
            sage: n = -7/2; n.ceil()
            -3
            sage: n = 7/2; n.ceil()
            4
            sage: n = 10/2; n.ceil()
            5"""
    def charpoly(self, var=...) -> Any:
        """Rational.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2923)

        Return the characteristic polynomial of this rational number. This
        will always be just ``var - self``; this is really here so that code
        written for number fields won't crash when applied to rational
        numbers.

        INPUT:

        - ``var`` -- string

        OUTPUT: polynomial

        EXAMPLES::

            sage: (1/3).charpoly('x')
             x - 1/3

        The default is ``var='x'``. (:issue:`20967`)::

            sage: a = QQ(2); a.charpoly('x')
            x - 2


        AUTHORS:

        - Craig Citro"""
    @overload
    def conjugate(self) -> Any:
        """Rational.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3779)

        Return the complex conjugate of this rational number, which is
        the number itself.

        EXAMPLES::

            sage: n = 23/11
            sage: n.conjugate()
            23/11"""
    @overload
    def conjugate(self) -> Any:
        """Rational.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3779)

        Return the complex conjugate of this rational number, which is
        the number itself.

        EXAMPLES::

            sage: n = 23/11
            sage: n.conjugate()
            23/11"""
    def content(self, other) -> Any:
        """Rational.content(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1126)

        Return the content of ``self`` and ``other``, i.e., the unique positive
        rational number `c` such that ``self/c`` and ``other/c`` are coprime
        integers.

        ``other`` can be a rational number or a list of rational numbers.

        EXAMPLES::

            sage: a = 2/3
            sage: a.content(2/3)
            2/3
            sage: a.content(1/5)
            1/15
            sage: a.content([2/5, 4/9])
            2/45"""
    @overload
    def continued_fraction(self) -> Any:
        """Rational.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 813)

        Return the continued fraction of that rational.

        EXAMPLES::

            sage: (641/472).continued_fraction()
            [1; 2, 1, 3, 1, 4, 1, 5]

            sage: a = (355/113).continued_fraction(); a
            [3; 7, 16]
            sage: a.n(digits=10)                                                        # needs sage.rings.real_mpfr
            3.141592920
            sage: pi.n(digits=10)                                                       # needs sage.rings.real_mpfr sage.symbolic
            3.141592654

        It's almost pi!"""
    @overload
    def continued_fraction(self) -> Any:
        """Rational.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 813)

        Return the continued fraction of that rational.

        EXAMPLES::

            sage: (641/472).continued_fraction()
            [1; 2, 1, 3, 1, 4, 1, 5]

            sage: a = (355/113).continued_fraction(); a
            [3; 7, 16]
            sage: a.n(digits=10)                                                        # needs sage.rings.real_mpfr
            3.141592920
            sage: pi.n(digits=10)                                                       # needs sage.rings.real_mpfr sage.symbolic
            3.141592654

        It's almost pi!"""
    @overload
    def continued_fraction(self) -> Any:
        """Rational.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 813)

        Return the continued fraction of that rational.

        EXAMPLES::

            sage: (641/472).continued_fraction()
            [1; 2, 1, 3, 1, 4, 1, 5]

            sage: a = (355/113).continued_fraction(); a
            [3; 7, 16]
            sage: a.n(digits=10)                                                        # needs sage.rings.real_mpfr
            3.141592920
            sage: pi.n(digits=10)                                                       # needs sage.rings.real_mpfr sage.symbolic
            3.141592654

        It's almost pi!"""
    @overload
    def continued_fraction_list(self, type=...) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    @overload
    def continued_fraction_list(self) -> Any:
        '''Rational.continued_fraction_list(self, type=\'std\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 716)

        Return the list of partial quotients of this rational number.

        INPUT:

        - ``type`` -- either ``\'std\'`` (the default) for the standard continued
          fractions or ``\'hj\'`` for the Hirzebruch-Jung ones

        EXAMPLES::

            sage: (13/9).continued_fraction_list()
            [1, 2, 4]
            sage: 1 + 1/(2 + 1/4)
            13/9

            sage: (225/157).continued_fraction_list()
            [1, 2, 3, 4,  5]
            sage: 1 + 1/(2 + 1/(3 + 1/(4 + 1/5)))
            225/157

            sage: (fibonacci(20)/fibonacci(19)).continued_fraction_list()               # needs sage.libs.pari
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

            sage: (-1/3).continued_fraction_list()
            [-1, 1, 2]

        Check that the partial quotients of an integer ``n`` is simply ``[n]``::

            sage: QQ(1).continued_fraction_list()
            [1]
            sage: QQ(0).continued_fraction_list()
            [0]
            sage: QQ(-1).continued_fraction_list()
            [-1]

        Hirzebruch-Jung continued fractions::

            sage: (11/19).continued_fraction_list("hj")
            [1, 3, 2, 3, 2]
            sage: 1 - 1/(3 - 1/(2 - 1/(3 - 1/2)))
            11/19

            sage: (225/137).continued_fraction_list("hj")
            [2, 3, 5, 10]
            sage: 2 - 1/(3 - 1/(5 - 1/10))
            225/137

            sage: (-23/19).continued_fraction_list("hj")
            [-1, 5, 4]
            sage: -1 - 1/(5 - 1/4)
            -23/19'''
    def denom(self) -> Any:
        """Rational.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3052)

        Return the denominator of this rational number.
        :meth:`denom` is an alias of :meth:`denominator`.

        EXAMPLES::

            sage: x = -5/11
            sage: x.denominator()
            11

            sage: x = 9/3
            sage: x.denominator()
            1

            sage: x = 5/13
            sage: x.denom()
            13"""
    @overload
    def denominator(self) -> Any:
        """Rational.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3052)

        Return the denominator of this rational number.
        :meth:`denom` is an alias of :meth:`denominator`.

        EXAMPLES::

            sage: x = -5/11
            sage: x.denominator()
            11

            sage: x = 9/3
            sage: x.denominator()
            1

            sage: x = 5/13
            sage: x.denom()
            13"""
    @overload
    def denominator(self) -> Any:
        """Rational.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3052)

        Return the denominator of this rational number.
        :meth:`denom` is an alias of :meth:`denominator`.

        EXAMPLES::

            sage: x = -5/11
            sage: x.denominator()
            11

            sage: x = 9/3
            sage: x.denominator()
            1

            sage: x = 5/13
            sage: x.denom()
            13"""
    @overload
    def denominator(self) -> Any:
        """Rational.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3052)

        Return the denominator of this rational number.
        :meth:`denom` is an alias of :meth:`denominator`.

        EXAMPLES::

            sage: x = -5/11
            sage: x.denominator()
            11

            sage: x = 9/3
            sage: x.denominator()
            1

            sage: x = 5/13
            sage: x.denom()
            13"""
    @overload
    def factor(self) -> Any:
        """Rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3094)

        Return the factorization of this rational number.

        OUTPUT: factorization

        EXAMPLES::

            sage: (-4/17).factor()
            -1 * 2^2 * 17^-1

        Trying to factor 0 gives an arithmetic error::

            sage: (0/1).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined"""
    @overload
    def factor(self) -> Any:
        """Rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3094)

        Return the factorization of this rational number.

        OUTPUT: factorization

        EXAMPLES::

            sage: (-4/17).factor()
            -1 * 2^2 * 17^-1

        Trying to factor 0 gives an arithmetic error::

            sage: (0/1).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined"""
    @overload
    def factor(self) -> Any:
        """Rational.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3094)

        Return the factorization of this rational number.

        OUTPUT: factorization

        EXAMPLES::

            sage: (-4/17).factor()
            -1 * 2^2 * 17^-1

        Trying to factor 0 gives an arithmetic error::

            sage: (0/1).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined"""
    @overload
    def floor(self) -> Any:
        """Rational.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3309)

        Return the floor of this rational number as an integer.

        OUTPUT: integer

        EXAMPLES::

            sage: n = 5/3; n.floor()
            1
            sage: n = -17/19; n.floor()
            -1
            sage: n = -7/2; n.floor()
            -4
            sage: n = 7/2; n.floor()
            3
            sage: n = 10/2; n.floor()
            5"""
    @overload
    def floor(self) -> Any:
        """Rational.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3309)

        Return the floor of this rational number as an integer.

        OUTPUT: integer

        EXAMPLES::

            sage: n = 5/3; n.floor()
            1
            sage: n = -17/19; n.floor()
            -1
            sage: n = -7/2; n.floor()
            -4
            sage: n = 7/2; n.floor()
            3
            sage: n = 10/2; n.floor()
            5"""
    @overload
    def floor(self) -> Any:
        """Rational.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3309)

        Return the floor of this rational number as an integer.

        OUTPUT: integer

        EXAMPLES::

            sage: n = 5/3; n.floor()
            1
            sage: n = -17/19; n.floor()
            -1
            sage: n = -7/2; n.floor()
            -4
            sage: n = 7/2; n.floor()
            3
            sage: n = 10/2; n.floor()
            5"""
    @overload
    def floor(self) -> Any:
        """Rational.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3309)

        Return the floor of this rational number as an integer.

        OUTPUT: integer

        EXAMPLES::

            sage: n = 5/3; n.floor()
            1
            sage: n = -17/19; n.floor()
            -1
            sage: n = -7/2; n.floor()
            -4
            sage: n = 7/2; n.floor()
            3
            sage: n = 10/2; n.floor()
            5"""
    @overload
    def floor(self) -> Any:
        """Rational.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3309)

        Return the floor of this rational number as an integer.

        OUTPUT: integer

        EXAMPLES::

            sage: n = 5/3; n.floor()
            1
            sage: n = -17/19; n.floor()
            -1
            sage: n = -7/2; n.floor()
            -4
            sage: n = 7/2; n.floor()
            3
            sage: n = 10/2; n.floor()
            5"""
    @overload
    def floor(self) -> Any:
        """Rational.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3309)

        Return the floor of this rational number as an integer.

        OUTPUT: integer

        EXAMPLES::

            sage: n = 5/3; n.floor()
            1
            sage: n = -17/19; n.floor()
            -1
            sage: n = -7/2; n.floor()
            -4
            sage: n = 7/2; n.floor()
            3
            sage: n = 10/2; n.floor()
            5"""
    @overload
    def gamma(self, prec=...) -> Any:
        """Rational.gamma(self, *, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3258)

        Return the gamma function evaluated at ``self``. This value is exact
        for integers and half-integers, and returns a symbolic value
        otherwise.  For a numerical approximation, use keyword ``prec``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: gamma(1/2)
            sqrt(pi)
            sage: gamma(7/2)
            15/8*sqrt(pi)
            sage: gamma(-3/2)
            4/3*sqrt(pi)
            sage: gamma(6/1)
            120
            sage: gamma(1/3)
            gamma(1/3)

        This function accepts an optional precision argument::

            sage: (1/3).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            2.6789385347077476336556929410
            sage: (1/2).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            1.7724538509055160272981674833

        TESTS:

        This is not the incomplete gamma function! ::

            sage: (1/2).gamma(5)
            Traceback (most recent call last):
            ...
            TypeError: ...gamma() takes exactly 0 positional arguments (1 given)"""
    @overload
    def gamma(self, prec=...) -> Any:
        """Rational.gamma(self, *, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3258)

        Return the gamma function evaluated at ``self``. This value is exact
        for integers and half-integers, and returns a symbolic value
        otherwise.  For a numerical approximation, use keyword ``prec``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: gamma(1/2)
            sqrt(pi)
            sage: gamma(7/2)
            15/8*sqrt(pi)
            sage: gamma(-3/2)
            4/3*sqrt(pi)
            sage: gamma(6/1)
            120
            sage: gamma(1/3)
            gamma(1/3)

        This function accepts an optional precision argument::

            sage: (1/3).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            2.6789385347077476336556929410
            sage: (1/2).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            1.7724538509055160272981674833

        TESTS:

        This is not the incomplete gamma function! ::

            sage: (1/2).gamma(5)
            Traceback (most recent call last):
            ...
            TypeError: ...gamma() takes exactly 0 positional arguments (1 given)"""
    @overload
    def gamma(self, prec=...) -> Any:
        """Rational.gamma(self, *, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3258)

        Return the gamma function evaluated at ``self``. This value is exact
        for integers and half-integers, and returns a symbolic value
        otherwise.  For a numerical approximation, use keyword ``prec``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: gamma(1/2)
            sqrt(pi)
            sage: gamma(7/2)
            15/8*sqrt(pi)
            sage: gamma(-3/2)
            4/3*sqrt(pi)
            sage: gamma(6/1)
            120
            sage: gamma(1/3)
            gamma(1/3)

        This function accepts an optional precision argument::

            sage: (1/3).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            2.6789385347077476336556929410
            sage: (1/2).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            1.7724538509055160272981674833

        TESTS:

        This is not the incomplete gamma function! ::

            sage: (1/2).gamma(5)
            Traceback (most recent call last):
            ...
            TypeError: ...gamma() takes exactly 0 positional arguments (1 given)"""
    @overload
    def gamma(self) -> Any:
        """Rational.gamma(self, *, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3258)

        Return the gamma function evaluated at ``self``. This value is exact
        for integers and half-integers, and returns a symbolic value
        otherwise.  For a numerical approximation, use keyword ``prec``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: gamma(1/2)
            sqrt(pi)
            sage: gamma(7/2)
            15/8*sqrt(pi)
            sage: gamma(-3/2)
            4/3*sqrt(pi)
            sage: gamma(6/1)
            120
            sage: gamma(1/3)
            gamma(1/3)

        This function accepts an optional precision argument::

            sage: (1/3).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            2.6789385347077476336556929410
            sage: (1/2).gamma(prec=100)                                                 # needs sage.rings.real_mpfr
            1.7724538509055160272981674833

        TESTS:

        This is not the incomplete gamma function! ::

            sage: (1/2).gamma(5)
            Traceback (most recent call last):
            ...
            TypeError: ...gamma() takes exactly 0 positional arguments (1 given)"""
    def global_height(self, prec=...) -> Any:
        """Rational.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1345)

        Return the absolute logarithmic height of this rational number.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this rational number.

        ALGORITHM:

        The height is the sum of the total archimedean and
        non-archimedean components, which is equal to
        `\\max(\\log(n),\\log(d))` where `n,d` are the numerator and
        denominator of the rational number.

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: a = QQ(6/25)
            sage: a.global_height_arch() + a.global_height_non_arch()
            3.21887582486820
            sage: a.global_height()
            3.21887582486820
            sage: (1/a).global_height()
            3.21887582486820
            sage: QQ(0).global_height()
            0.000000000000000
            sage: QQ(1).global_height()
            0.000000000000000"""
    def global_height_arch(self, prec=...) -> Any:
        """Rational.global_height_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1312)

        Return the total archimedean component of the height of this rational
        number.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The total archimedean component of the height of
        this rational number.

        ALGORITHM:

        Since `\\QQ` has only one infinite place this is just the value
        of the local height at that place.  This separate function is
        included for compatibility with number fields.

        EXAMPLES::

            sage: a = QQ(6/25)
            sage: a.global_height_arch()                                                # needs sage.rings.real_mpfr
            0.000000000000000
            sage: (1/a).global_height_arch()                                            # needs sage.rings.real_mpfr
            1.42711635564015
            sage: (1/a).global_height_arch(100)                                         # needs sage.rings.real_mpfr
            1.4271163556401457483890413081"""
    @overload
    def global_height_non_arch(self, prec=...) -> Any:
        """Rational.global_height_non_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1269)

        Return the total non-archimedean component of the height of this
        rational number.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The total non-archimedean component of the height of
        this rational number.

        ALGORITHM:

        This is the sum of the local heights at all primes `p`, which
        may be computed without factorization as the log of the
        denominator.

        EXAMPLES::

            sage: a = QQ(5/6)
            sage: a.support()
            [2, 3, 5]
            sage: a.global_height_non_arch()                                            # needs sage.rings.real_mpfr
            1.79175946922805
            sage: [a.local_height(p) for p in a.support()]                              # needs sage.rings.real_mpfr
            [0.693147180559945, 1.09861228866811, 0.000000000000000]
            sage: sum([a.local_height(p) for p in a.support()])                         # needs sage.rings.real_mpfr
            1.79175946922805"""
    @overload
    def global_height_non_arch(self) -> Any:
        """Rational.global_height_non_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1269)

        Return the total non-archimedean component of the height of this
        rational number.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The total non-archimedean component of the height of
        this rational number.

        ALGORITHM:

        This is the sum of the local heights at all primes `p`, which
        may be computed without factorization as the log of the
        denominator.

        EXAMPLES::

            sage: a = QQ(5/6)
            sage: a.support()
            [2, 3, 5]
            sage: a.global_height_non_arch()                                            # needs sage.rings.real_mpfr
            1.79175946922805
            sage: [a.local_height(p) for p in a.support()]                              # needs sage.rings.real_mpfr
            [0.693147180559945, 1.09861228866811, 0.000000000000000]
            sage: sum([a.local_height(p) for p in a.support()])                         # needs sage.rings.real_mpfr
            1.79175946922805"""
    @overload
    def height(self) -> Any:
        """Rational.height(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3466)

        The max absolute value of the numerator and denominator of ``self``, as
        an :class:`Integer`.

        OUTPUT: integer

        EXAMPLES::

            sage: a = 2/3
            sage: a.height()
            3
            sage: a = 34/3
            sage: a.height()
            34
            sage: a = -97/4
            sage: a.height()
            97

        AUTHORS:

        - Naqi Jaffery (2006-03-05): examples

        .. NOTE::

           For the logarithmic height, use :meth:`global_height()`."""
    @overload
    def height(self) -> Any:
        """Rational.height(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3466)

        The max absolute value of the numerator and denominator of ``self``, as
        an :class:`Integer`.

        OUTPUT: integer

        EXAMPLES::

            sage: a = 2/3
            sage: a.height()
            3
            sage: a = 34/3
            sage: a.height()
            34
            sage: a = -97/4
            sage: a.height()
            97

        AUTHORS:

        - Naqi Jaffery (2006-03-05): examples

        .. NOTE::

           For the logarithmic height, use :meth:`global_height()`."""
    @overload
    def height(self) -> Any:
        """Rational.height(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3466)

        The max absolute value of the numerator and denominator of ``self``, as
        an :class:`Integer`.

        OUTPUT: integer

        EXAMPLES::

            sage: a = 2/3
            sage: a.height()
            3
            sage: a = 34/3
            sage: a.height()
            34
            sage: a = -97/4
            sage: a.height()
            97

        AUTHORS:

        - Naqi Jaffery (2006-03-05): examples

        .. NOTE::

           For the logarithmic height, use :meth:`global_height()`."""
    @overload
    def height(self) -> Any:
        """Rational.height(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3466)

        The max absolute value of the numerator and denominator of ``self``, as
        an :class:`Integer`.

        OUTPUT: integer

        EXAMPLES::

            sage: a = 2/3
            sage: a.height()
            3
            sage: a = 34/3
            sage: a.height()
            34
            sage: a = -97/4
            sage: a.height()
            97

        AUTHORS:

        - Naqi Jaffery (2006-03-05): examples

        .. NOTE::

           For the logarithmic height, use :meth:`global_height()`."""
    @overload
    def imag(self) -> Any:
        """Rational.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3455)

        Return the imaginary part of ``self``, which is zero.

        EXAMPLES::

            sage: (1/239).imag()
            0"""
    @overload
    def imag(self) -> Any:
        """Rational.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3455)

        Return the imaginary part of ``self``, which is zero.

        EXAMPLES::

            sage: (1/239).imag()
            0"""
    @overload
    def is_S_integral(self, S=...) -> Any:
        """Rational.is_S_integral(self, S=[])

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3618)

        Determine if the rational number is ``S``-integral.

        ``x`` is ``S``-integral if ``x.valuation(p)>=0`` for all ``p`` not in
        ``S``, i.e., the denominator of ``x`` is divisible only by the primes
        in ``S``.

        INPUT:

        - ``S`` -- list or tuple of primes

        OUTPUT: boolean

        .. NOTE::

           Primality of the entries in ``S`` is not checked.

        EXAMPLES::

            sage: QQ(1/2).is_S_integral()
            False
            sage: QQ(1/2).is_S_integral([2])
            True
            sage: [a for a in range(1,11) if QQ(101/a).is_S_integral([2,5])]
            [1, 2, 4, 5, 8, 10]"""
    @overload
    def is_S_integral(self) -> Any:
        """Rational.is_S_integral(self, S=[])

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3618)

        Determine if the rational number is ``S``-integral.

        ``x`` is ``S``-integral if ``x.valuation(p)>=0`` for all ``p`` not in
        ``S``, i.e., the denominator of ``x`` is divisible only by the primes
        in ``S``.

        INPUT:

        - ``S`` -- list or tuple of primes

        OUTPUT: boolean

        .. NOTE::

           Primality of the entries in ``S`` is not checked.

        EXAMPLES::

            sage: QQ(1/2).is_S_integral()
            False
            sage: QQ(1/2).is_S_integral([2])
            True
            sage: [a for a in range(1,11) if QQ(101/a).is_S_integral([2,5])]
            [1, 2, 4, 5, 8, 10]"""
    @overload
    def is_S_unit(self, S=...) -> Any:
        """Rational.is_S_unit(self, S=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3649)

        Determine if the rational number is an ``S``-unit.

        ``x`` is an ``S``-unit if ``x.valuation(p)==0`` for all ``p`` not in
        ``S``, i.e., the numerator and denominator of ``x`` are divisible only
        by the primes in `S`.

        INPUT:

        - ``S`` -- list or tuple of primes

        OUTPUT: boolean

        .. NOTE::

           Primality of the entries in ``S`` is not checked.

        EXAMPLES::

            sage: QQ(1/2).is_S_unit()
            False
            sage: QQ(1/2).is_S_unit([2])
            True
            sage: [a for a in range(1,11) if QQ(10/a).is_S_unit([2,5])]
            [1, 2, 4, 5, 8, 10]"""
    @overload
    def is_S_unit(self) -> Any:
        """Rational.is_S_unit(self, S=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3649)

        Determine if the rational number is an ``S``-unit.

        ``x`` is an ``S``-unit if ``x.valuation(p)==0`` for all ``p`` not in
        ``S``, i.e., the numerator and denominator of ``x`` are divisible only
        by the primes in `S`.

        INPUT:

        - ``S`` -- list or tuple of primes

        OUTPUT: boolean

        .. NOTE::

           Primality of the entries in ``S`` is not checked.

        EXAMPLES::

            sage: QQ(1/2).is_S_unit()
            False
            sage: QQ(1/2).is_S_unit([2])
            True
            sage: [a for a in range(1,11) if QQ(10/a).is_S_unit([2,5])]
            [1, 2, 4, 5, 8, 10]"""
    def is_integer(self, *args, **kwargs):
        """Rational.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3588)

        Determine if a rational number is integral (i.e., is in
        `\\ZZ`).

        OUTPUT: boolean

        EXAMPLES::

            sage: QQ(1/2).is_integral()
            False
            sage: QQ(4/4).is_integral()
            True"""
    def is_integral(self) -> Any:
        """Rational.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3588)

        Determine if a rational number is integral (i.e., is in
        `\\ZZ`).

        OUTPUT: boolean

        EXAMPLES::

            sage: QQ(1/2).is_integral()
            False
            sage: QQ(4/4).is_integral()
            True"""
    @overload
    def is_norm(self, L, element=..., proof=...) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    @overload
    def is_norm(self, K) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    @overload
    def is_norm(self, K) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    @overload
    def is_norm(self, K) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    @overload
    def is_norm(self, K, element=...) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    @overload
    def is_norm(self, K, element=...) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    @overload
    def is_norm(self, QQ, element=...) -> Any:
        """Rational.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1410)

        Determine whether ``self`` is the norm of an element of ``L``.

        INPUT:

        - ``L`` -- a number field
        - ``element`` -- boolean (default: ``False``); whether to also output
          an element of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output assumes GRH

        OUTPUT:

        If element is ``False``, then the output is a boolean ``B``, which is
        ``True`` if and only if ``self`` is the norm of an element of ``L``.
        If ``element`` is ``False``, then the output is a pair ``(B, x)``,
        where ``B`` is as above. If ``B`` is ``True``, then ``x`` an element of
        ``L`` such that ``self == x.norm()``. Otherwise, ``x is None``.

        ALGORITHM:

        Uses the PARI function :pari:`bnfisnorm`. See :meth:`_bnfisnorm()`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ, 'x')
            sage: K = NumberField(x^2 - 2, 'beta')
            sage: (1/7).is_norm(K)
            True
            sage: (1/10).is_norm(K)
            False
            sage: 0.is_norm(K)
            True
            sage: (1/7).is_norm(K, element=True)
            (True, 1/7*beta + 3/7)
            sage: (1/10).is_norm(K, element=True)
            (False, None)
            sage: (1/691).is_norm(QQ, element=True)
            (True, 1/691)

        The number field doesn't have to be defined by an
        integral polynomial::

            sage: B, e = (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)          # needs sage.rings.number_field
            sage: B                                                                     # needs sage.rings.number_field
            True
            sage: e.norm()                                                              # needs sage.rings.number_field
            1/5

        A non-Galois number field::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - 2)
            sage: B, e = (3/5).is_norm(K, element=True); B
            True
            sage: e.norm()
            3/5
            sage: 7.is_norm(K)                                                          # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
             for norms from non-Galois number fields
            sage: 7.is_norm(K, proof=False)
            False

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    def is_nth_power(self, intn) -> Any:
        """Rational.is_nth_power(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2119)

        Return ``True`` if ``self`` is an `n`-th power, else ``False``.

        INPUT:

        - ``n`` -- integer (must fit in C ``int`` type)

        .. NOTE::

           Use this function when you need to test if a rational
           number is an `n`-th power, but do not need to know the value
           of its `n`-th root.  If the value is needed, use :meth:`nth_root()`.

        AUTHORS:

        - John Cremona (2009-04-04)

        EXAMPLES::

            sage: QQ(25/4).is_nth_power(2)
            True
            sage: QQ(125/8).is_nth_power(3)
            True
            sage: QQ(-125/8).is_nth_power(3)
            True
            sage: QQ(25/4).is_nth_power(-2)
            True

            sage: QQ(9/2).is_nth_power(2)
            False
            sage: QQ(-25).is_nth_power(2)
            False"""
    @overload
    def is_one(self) -> Any:
        """Rational.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3572)

        Determine if a rational number is one.

        OUTPUT: boolean

        EXAMPLES::

            sage: QQ(1/2).is_one()
            False
            sage: QQ(4/4).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """Rational.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3572)

        Determine if a rational number is one.

        OUTPUT: boolean

        EXAMPLES::

            sage: QQ(1/2).is_one()
            False
            sage: QQ(4/4).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """Rational.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3572)

        Determine if a rational number is one.

        OUTPUT: boolean

        EXAMPLES::

            sage: QQ(1/2).is_one()
            False
            sage: QQ(4/4).is_one()
            True"""
    def is_padic_square(self, p, check=...) -> Any:
        """Rational.is_padic_square(self, p, check=True)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1728)

        Determines whether this rational number is a square in `\\QQ_p` (or in
        `R` when ``p = infinity``).

        INPUT:

        - ``p`` -- a prime number, or ``infinity``

        - ``check`` -- boolean (default: ``True``); check if `p` is prime

        EXAMPLES::

            sage: QQ(2).is_padic_square(7)
            True
            sage: QQ(98).is_padic_square(7)
            True
            sage: QQ(2).is_padic_square(5)
            False

        TESTS::

            sage: QQ(5/7).is_padic_square(int(2))
            False"""
    @overload
    def is_perfect_power(self, expected_value=...) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self, _True) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self, _True) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self, _True) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self, _True) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_perfect_power(self, _True) -> Any:
        """Rational.is_perfect_power(self, expected_value=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1576)

        Return ``True`` if ``self`` is a perfect power.

        INPUT:

        - ``expected_value`` -- boolean; whether or not this rational is
          expected to be a perfect power. This does not affect the correctness
          of the output, only the runtime.

        If ``expected_value`` is ``False`` (default) it will check the
        smallest of the numerator and denominator is a perfect power
        as a first step, which is often faster than checking if the
        quotient is a perfect power.

        EXAMPLES::

            sage: (4/9).is_perfect_power()
            True
            sage: (144/1).is_perfect_power()
            True
            sage: (4/3).is_perfect_power()
            False
            sage: (2/27).is_perfect_power()
            False
            sage: (4/27).is_perfect_power()
            False
            sage: (-1/25).is_perfect_power()
            False
            sage: (-1/27).is_perfect_power()
            True
            sage: (0/1).is_perfect_power()
            True

        The second parameter does not change the result, but may
        change the runtime.

        ::

            sage: (-1/27).is_perfect_power(True)
            True
            sage: (-1/25).is_perfect_power(True)
            False
            sage: (2/27).is_perfect_power(True)
            False
            sage: (144/1).is_perfect_power(True)
            True

        This test makes sure we workaround a bug in GMP (see :issue:`4612`)::

            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power()]
            []
            sage: [-a for a in srange(100) if not QQ(-a^3).is_perfect_power(True)]
            []"""
    @overload
    def is_rational(self) -> Any:
        """Rational.is_rational(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3604)

        Return ``True`` since this is a rational number.

        EXAMPLES::

            sage: (3/4).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """Rational.is_rational(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3604)

        Return ``True`` since this is a rational number.

        EXAMPLES::

            sage: (3/4).is_rational()
            True"""
    @overload
    def is_square(self) -> Any:
        """Rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1387)

        Return whether or not this rational number is a square.

        OUTPUT: boolean

        EXAMPLES::

            sage: x = 9/4
            sage: x.is_square()
            True
            sage: x = (7/53)^100
            sage: x.is_square()
            True
            sage: x = 4/3
            sage: x.is_square()
            False
            sage: x = -1/4
            sage: x.is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1387)

        Return whether or not this rational number is a square.

        OUTPUT: boolean

        EXAMPLES::

            sage: x = 9/4
            sage: x.is_square()
            True
            sage: x = (7/53)^100
            sage: x.is_square()
            True
            sage: x = 4/3
            sage: x.is_square()
            False
            sage: x = -1/4
            sage: x.is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1387)

        Return whether or not this rational number is a square.

        OUTPUT: boolean

        EXAMPLES::

            sage: x = 9/4
            sage: x.is_square()
            True
            sage: x = (7/53)^100
            sage: x.is_square()
            True
            sage: x = 4/3
            sage: x.is_square()
            False
            sage: x = -1/4
            sage: x.is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1387)

        Return whether or not this rational number is a square.

        OUTPUT: boolean

        EXAMPLES::

            sage: x = 9/4
            sage: x.is_square()
            True
            sage: x = (7/53)^100
            sage: x.is_square()
            True
            sage: x = 4/3
            sage: x.is_square()
            False
            sage: x = -1/4
            sage: x.is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Rational.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1387)

        Return whether or not this rational number is a square.

        OUTPUT: boolean

        EXAMPLES::

            sage: x = 9/4
            sage: x.is_square()
            True
            sage: x = (7/53)^100
            sage: x.is_square()
            True
            sage: x = 4/3
            sage: x.is_square()
            False
            sage: x = -1/4
            sage: x.is_square()
            False"""
    @overload
    def list(self) -> Any:
        """Rational.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 701)

        Return a list with the rational element in it, to be compatible
        with the method for number fields.

        OUTPUT: the list ``[self]``

        EXAMPLES::

            sage: m = 5/3
            sage: m.list()
            [5/3]"""
    @overload
    def list(self) -> Any:
        """Rational.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 701)

        Return a list with the rational element in it, to be compatible
        with the method for number fields.

        OUTPUT: the list ``[self]``

        EXAMPLES::

            sage: m = 5/3
            sage: m.list()
            [5/3]"""
    def local_height(self, p, prec=...) -> Any:
        """Rational.local_height(self, p, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1195)

        Return the local height of this rational number at the prime `p`.

        INPUT:

        - ``p`` -- a prime number

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The local height of this rational number at the
        prime `p`.

        EXAMPLES::

            sage: a = QQ(25/6)
            sage: a.local_height(2)                                                     # needs sage.rings.real_mpfr
            0.693147180559945
            sage: a.local_height(3)                                                     # needs sage.rings.real_mpfr
            1.09861228866811
            sage: a.local_height(5)                                                     # needs sage.rings.real_mpfr
            0.000000000000000"""
    def local_height_arch(self, prec=...) -> Any:
        """Rational.local_height_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1233)

        Return the Archimedean local height of this rational number at the
        infinite place.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The local height of this rational number `x` at the
        unique infinite place of `\\QQ`, which is
        `\\max(\\log(|x|),0)`.

        EXAMPLES::

            sage: a = QQ(6/25)
            sage: a.local_height_arch()                                                 # needs sage.rings.real_mpfr
            0.000000000000000
            sage: (1/a).local_height_arch()                                             # needs sage.rings.real_mpfr
            1.42711635564015
            sage: (1/a).local_height_arch(100)                                          # needs sage.rings.real_mpfr
            1.4271163556401457483890413081"""
    def log(self, m=..., prec=...) -> Any:
        """Rational.log(self, m=None, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3142)

        Return the log of ``self``.

        INPUT:

        - ``m`` -- the base (default: natural log base e)

        - ``prec`` -- integer (optional); the precision in bits

        OUTPUT:

        When ``prec`` is not given, the log as an element in symbolic
        ring unless the logarithm is exact. Otherwise the log is a
        :class:`RealField` approximation to ``prec`` bit precision.

        EXAMPLES::

            sage: (124/345).log(5)                                                      # needs sage.symbolic
            log(124/345)/log(5)
            sage: (124/345).log(5, 100)                                                 # needs sage.rings.real_mpfr
            -0.63578895682825611710391773754
            sage: log(QQ(125))                                                          # needs sage.symbolic
            3*log(5)
            sage: log(QQ(125), 5)
            3
            sage: log(QQ(125), 3)                                                       # needs sage.symbolic
            3*log(5)/log(3)
            sage: QQ(8).log(1/2)
            -3
            sage: (1/8).log(1/2)
            3
            sage: (1/2).log(1/8)
            1/3
            sage: (1/2).log(8)
            -1/3
            sage: (16/81).log(8/27)                                                     # needs sage.libs.pari
            4/3
            sage: (8/27).log(16/81)                                                     # needs sage.libs.pari
            3/4
            sage: log(27/8, 16/81)                                                      # needs sage.libs.pari
            -3/4
            sage: log(16/81, 27/8)                                                      # needs sage.libs.pari
            -4/3
            sage: (125/8).log(5/2)                                                      # needs sage.libs.pari
            3
            sage: (125/8).log(5/2, prec=53)                                             # needs sage.rings.real_mpfr
            3.00000000000000

        TESTS::

            sage: (25/2).log(5/2)                                                       # needs sage.symbolic
            log(25/2)/log(5/2)
            sage: (-1/2).log(3)                                                         # needs sage.symbolic
            (I*pi + log(1/2))/log(3)"""
    def minpoly(self, var=...) -> Any:
        """Rational.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2954)

        Return the minimal polynomial of this rational number. This will
        always be just ``x - self``; this is really here so that code written
        for number fields won't crash when applied to rational numbers.

        INPUT:

        - ``var`` -- string

        OUTPUT: polynomial

        EXAMPLES::

            sage: (1/3).minpoly()
            x - 1/3
            sage: (1/3).minpoly('y')
            y - 1/3

        AUTHORS:

        - Craig Citro"""
    def mod_ui(self, unsignedlongn) -> Any:
        """Rational.mod_ui(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2790)

        Return the remainder upon division of ``self`` by the unsigned long
        integer ``n``.

        INPUT:

        - ``n`` -- an unsigned long integer

        OUTPUT: integer

        EXAMPLES::

            sage: (-4/17).mod_ui(3)
            1
            sage: (-4/17).mod_ui(17)
            Traceback (most recent call last):
            ...
            ArithmeticError: The inverse of 0 modulo 17 is not defined."""
    @overload
    def multiplicative_order(self) -> Any:
        """Rational.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3543)

        Return the multiplicative order of ``self``.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: QQ(1).multiplicative_order()
            1
            sage: QQ('1/-1').multiplicative_order()
            2
            sage: QQ(0).multiplicative_order()
            +Infinity
            sage: QQ('2/3').multiplicative_order()
            +Infinity
            sage: QQ('1/2').multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Rational.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3543)

        Return the multiplicative order of ``self``.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: QQ(1).multiplicative_order()
            1
            sage: QQ('1/-1').multiplicative_order()
            2
            sage: QQ(0).multiplicative_order()
            +Infinity
            sage: QQ('2/3').multiplicative_order()
            +Infinity
            sage: QQ('1/2').multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Rational.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3543)

        Return the multiplicative order of ``self``.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: QQ(1).multiplicative_order()
            1
            sage: QQ('1/-1').multiplicative_order()
            2
            sage: QQ(0).multiplicative_order()
            +Infinity
            sage: QQ('2/3').multiplicative_order()
            +Infinity
            sage: QQ('1/2').multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Rational.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3543)

        Return the multiplicative order of ``self``.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: QQ(1).multiplicative_order()
            1
            sage: QQ('1/-1').multiplicative_order()
            2
            sage: QQ(0).multiplicative_order()
            +Infinity
            sage: QQ('2/3').multiplicative_order()
            +Infinity
            sage: QQ('1/2').multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Rational.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3543)

        Return the multiplicative order of ``self``.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: QQ(1).multiplicative_order()
            1
            sage: QQ('1/-1').multiplicative_order()
            2
            sage: QQ(0).multiplicative_order()
            +Infinity
            sage: QQ('2/3').multiplicative_order()
            +Infinity
            sage: QQ('1/2').multiplicative_order()
            +Infinity"""
    @overload
    def multiplicative_order(self) -> Any:
        """Rational.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3543)

        Return the multiplicative order of ``self``.

        OUTPUT: integer or ``infinity``

        EXAMPLES::

            sage: QQ(1).multiplicative_order()
            1
            sage: QQ('1/-1').multiplicative_order()
            2
            sage: QQ(0).multiplicative_order()
            +Infinity
            sage: QQ('2/3').multiplicative_order()
            +Infinity
            sage: QQ('1/2').multiplicative_order()
            +Infinity"""
    def norm(self) -> Any:
        """Rational.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2857)

        Return the norm from `\\QQ` to `\\QQ` of `x` (which is just `x`). This
        was added for compatibility with :class:`NumberField`.

        OUTPUT: ``Rational`` -- reference to ``self``

        EXAMPLES::

            sage: (1/3).norm()
             1/3

        AUTHORS:

        - Craig Citro"""
    def nth_root(self, intn) -> Any:
        """Rational.nth_root(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2051)

        Compute the `n`-th root of ``self``, or raises a
        :exc:`ValueError` if ``self`` is not a perfect `n`-th power.

        INPUT:

        - ``n`` -- integer (must fit in C ``int`` type)

        AUTHORS:

        - David Harvey (2006-09-15)

        EXAMPLES::

            sage: (25/4).nth_root(2)
            5/2
            sage: (125/8).nth_root(3)
            5/2
            sage: (-125/8).nth_root(3)
            -5/2
            sage: (25/4).nth_root(-2)
            2/5

        ::

            sage: (9/2).nth_root(2)
            Traceback (most recent call last):
            ...
            ValueError: not a perfect 2nd power

        ::

            sage: (-25/4).nth_root(2)
            Traceback (most recent call last):
            ...
            ValueError: cannot take even root of negative number"""
    def numer(self) -> Any:
        """Rational.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3002)

        Return the numerator of this rational number.
        :meth:`numer` is an alias of :meth:`numerator`.

        EXAMPLES::

            sage: x = 5/11
            sage: x.numerator()
            5

            sage: x = 9/3
            sage: x.numerator()
            3

            sage: x = -5/11
            sage: x.numer()
            -5"""
    @overload
    def numerator(self) -> Any:
        """Rational.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3002)

        Return the numerator of this rational number.
        :meth:`numer` is an alias of :meth:`numerator`.

        EXAMPLES::

            sage: x = 5/11
            sage: x.numerator()
            5

            sage: x = 9/3
            sage: x.numerator()
            3

            sage: x = -5/11
            sage: x.numer()
            -5"""
    @overload
    def numerator(self) -> Any:
        """Rational.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3002)

        Return the numerator of this rational number.
        :meth:`numer` is an alias of :meth:`numerator`.

        EXAMPLES::

            sage: x = 5/11
            sage: x.numerator()
            5

            sage: x = 9/3
            sage: x.numerator()
            3

            sage: x = -5/11
            sage: x.numer()
            -5"""
    @overload
    def numerator(self) -> Any:
        """Rational.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3002)

        Return the numerator of this rational number.
        :meth:`numer` is an alias of :meth:`numerator`.

        EXAMPLES::

            sage: x = 5/11
            sage: x.numerator()
            5

            sage: x = 9/3
            sage: x.numerator()
            3

            sage: x = -5/11
            sage: x.numer()
            -5"""
    def ord(self) -> Any:
        """Rational.valuation(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1153)

        Return the power of ``p`` in the factorization of ``self``.

        INPUT:

        - ``p`` -- a prime number

        OUTPUT:

        (integer or infinity) ``Infinity`` if ``self`` is zero, otherwise the
        (positive or negative) integer `e` such that ``self`` = `m*p^e`
        with `m` coprime to `p`.

        .. NOTE::

           See also :meth:`val_unit()` which returns the pair `(e,m)`. The
           function :meth:`ord()` is an alias for :meth:`valuation()`.

        EXAMPLES::

            sage: x = -5/9
            sage: x.valuation(5)
            1
            sage: x.ord(5)
            1
            sage: x.valuation(3)
            -2
            sage: x.valuation(2)
            0

        Some edge cases::

            sage: (0/1).valuation(4)
            +Infinity
            sage: (7/16).valuation(4)
            -2"""
    def period(self) -> Any:
        """Rational.period(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2011)

        Return the period of the repeating part of the decimal expansion of
        this rational number.

        ALGORITHM:

        When a rational number `n/d` with `(n,d)=1` is
        expanded, the period begins after `s` terms and has length
        `t`, where `s` and `t` are the smallest numbers satisfying
        `10^s=10^{s+t} \\mod d`. In general if `d=2^a 5^b m` where `m`
        is coprime to 10, then `s=\\max(a,b)` and `t` is the order of
        10 modulo `m`.

        EXAMPLES::

            sage: (1/7).period()                                                        # needs sage.libs.pari
            6
            sage: RR(1/7)                                                               # needs sage.rings.real_mpfr
            0.142857142857143
            sage: (1/8).period()                                                        # needs sage.libs.pari
            1
            sage: RR(1/8)                                                               # needs sage.rings.real_mpfr
            0.125000000000000
            sage: RR(1/6)                                                               # needs sage.rings.real_mpfr
            0.166666666666667
            sage: (1/6).period()                                                        # needs sage.libs.pari
            1
            sage: x = 333/106
            sage: x.period()                                                            # needs sage.libs.pari
            13
            sage: RealField(200)(x)                                                     # needs sage.rings.real_mpfr
            3.1415094339622641509433962264150943396226415094339622641509"""
    @overload
    def prime_to_S_part(self, S=...) -> Any:
        """Rational.prime_to_S_part(self, S=[])

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1846)

        Return ``self`` with all powers of all primes in ``S`` removed.

        INPUT:

        - ``S`` -- list or tuple of primes

        OUTPUT: rational

        .. NOTE::

           Primality of the entries in `S` is not checked.

        EXAMPLES::

            sage: QQ(3/4).prime_to_S_part()
            3/4
            sage: QQ(3/4).prime_to_S_part([2])
            3
            sage: QQ(-3/4).prime_to_S_part([3])
            -1/4
            sage: QQ(700/99).prime_to_S_part([2,3,5])
            7/11
            sage: QQ(-700/99).prime_to_S_part([2,3,5])
            -7/11
            sage: QQ(0).prime_to_S_part([2,3,5])
            0
            sage: QQ(-700/99).prime_to_S_part([])
            -700/99"""
    @overload
    def prime_to_S_part(self) -> Any:
        """Rational.prime_to_S_part(self, S=[])

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1846)

        Return ``self`` with all powers of all primes in ``S`` removed.

        INPUT:

        - ``S`` -- list or tuple of primes

        OUTPUT: rational

        .. NOTE::

           Primality of the entries in `S` is not checked.

        EXAMPLES::

            sage: QQ(3/4).prime_to_S_part()
            3/4
            sage: QQ(3/4).prime_to_S_part([2])
            3
            sage: QQ(-3/4).prime_to_S_part([3])
            -1/4
            sage: QQ(700/99).prime_to_S_part([2,3,5])
            7/11
            sage: QQ(-700/99).prime_to_S_part([2,3,5])
            -7/11
            sage: QQ(0).prime_to_S_part([2,3,5])
            0
            sage: QQ(-700/99).prime_to_S_part([])
            -700/99"""
    @overload
    def real(self) -> Any:
        """Rational.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3444)

        Return the real part of ``self``, which is ``self``.

        EXAMPLES::

            sage: (1/2).real()
            1/2"""
    @overload
    def real(self) -> Any:
        """Rational.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3444)

        Return the real part of ``self``, which is ``self``.

        EXAMPLES::

            sage: (1/2).real()
            1/2"""
    @overload
    def relative_norm(self) -> Any:
        """Rational.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2875)

        Return the norm from Q to Q of x (which is just x). This was added for
        compatibility with NumberFields.

        EXAMPLES::

            sage: (6/5).relative_norm()
            6/5

            sage: QQ(7/5).relative_norm()
            7/5"""
    @overload
    def relative_norm(self) -> Any:
        """Rational.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2875)

        Return the norm from Q to Q of x (which is just x). This was added for
        compatibility with NumberFields.

        EXAMPLES::

            sage: (6/5).relative_norm()
            6/5

            sage: QQ(7/5).relative_norm()
            7/5"""
    @overload
    def relative_norm(self) -> Any:
        """Rational.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2875)

        Return the norm from Q to Q of x (which is just x). This was added for
        compatibility with NumberFields.

        EXAMPLES::

            sage: (6/5).relative_norm()
            6/5

            sage: QQ(7/5).relative_norm()
            7/5"""
    @overload
    def round(self, mode=...) -> Any:
        '''Rational.round(self, mode=\'even\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3380)

        Return the nearest integer to ``self``, rounding to even by default.

        INPUT:

        - ``self`` -- a rational number

        - ``mode`` -- a rounding mode for half integers:

           - ``\'toward\'`` rounds toward zero
           - ``\'away\'`` (default) rounds away from zero
           - ``\'up\'`` rounds up
           - ``\'down\'`` rounds down
           - ``\'even\'`` rounds toward the even integer
           - ``\'odd\'`` rounds toward the odd integer

        OUTPUT: integer

        EXAMPLES::

            sage: (9/2).round()
            4
            sage: n = 4/3; n.round()
            1
            sage: n = -17/4; n.round()
            -4
            sage: n = -5/2; n.round()
            -2
            sage: n.round("away")
            -3
            sage: n.round("up")
            -2
            sage: n.round("down")
            -3
            sage: n.round("even")
            -2
            sage: n.round("odd")
            -3'''
    @overload
    def round(self) -> Any:
        '''Rational.round(self, mode=\'even\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3380)

        Return the nearest integer to ``self``, rounding to even by default.

        INPUT:

        - ``self`` -- a rational number

        - ``mode`` -- a rounding mode for half integers:

           - ``\'toward\'`` rounds toward zero
           - ``\'away\'`` (default) rounds away from zero
           - ``\'up\'`` rounds up
           - ``\'down\'`` rounds down
           - ``\'even\'`` rounds toward the even integer
           - ``\'odd\'`` rounds toward the odd integer

        OUTPUT: integer

        EXAMPLES::

            sage: (9/2).round()
            4
            sage: n = 4/3; n.round()
            1
            sage: n = -17/4; n.round()
            -4
            sage: n = -5/2; n.round()
            -2
            sage: n.round("away")
            -3
            sage: n.round("up")
            -2
            sage: n.round("down")
            -3
            sage: n.round("even")
            -2
            sage: n.round("odd")
            -3'''
    @overload
    def round(self) -> Any:
        '''Rational.round(self, mode=\'even\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3380)

        Return the nearest integer to ``self``, rounding to even by default.

        INPUT:

        - ``self`` -- a rational number

        - ``mode`` -- a rounding mode for half integers:

           - ``\'toward\'`` rounds toward zero
           - ``\'away\'`` (default) rounds away from zero
           - ``\'up\'`` rounds up
           - ``\'down\'`` rounds down
           - ``\'even\'`` rounds toward the even integer
           - ``\'odd\'`` rounds toward the odd integer

        OUTPUT: integer

        EXAMPLES::

            sage: (9/2).round()
            4
            sage: n = 4/3; n.round()
            1
            sage: n = -17/4; n.round()
            -4
            sage: n = -5/2; n.round()
            -2
            sage: n.round("away")
            -3
            sage: n.round("up")
            -2
            sage: n.round("down")
            -3
            sage: n.round("even")
            -2
            sage: n.round("odd")
            -3'''
    @overload
    def round(self) -> Any:
        '''Rational.round(self, mode=\'even\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3380)

        Return the nearest integer to ``self``, rounding to even by default.

        INPUT:

        - ``self`` -- a rational number

        - ``mode`` -- a rounding mode for half integers:

           - ``\'toward\'`` rounds toward zero
           - ``\'away\'`` (default) rounds away from zero
           - ``\'up\'`` rounds up
           - ``\'down\'`` rounds down
           - ``\'even\'`` rounds toward the even integer
           - ``\'odd\'`` rounds toward the odd integer

        OUTPUT: integer

        EXAMPLES::

            sage: (9/2).round()
            4
            sage: n = 4/3; n.round()
            1
            sage: n = -17/4; n.round()
            -4
            sage: n = -5/2; n.round()
            -2
            sage: n.round("away")
            -3
            sage: n.round("up")
            -2
            sage: n.round("down")
            -3
            sage: n.round("even")
            -2
            sage: n.round("odd")
            -3'''
    @overload
    def round(self) -> Any:
        '''Rational.round(self, mode=\'even\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3380)

        Return the nearest integer to ``self``, rounding to even by default.

        INPUT:

        - ``self`` -- a rational number

        - ``mode`` -- a rounding mode for half integers:

           - ``\'toward\'`` rounds toward zero
           - ``\'away\'`` (default) rounds away from zero
           - ``\'up\'`` rounds up
           - ``\'down\'`` rounds down
           - ``\'even\'`` rounds toward the even integer
           - ``\'odd\'`` rounds toward the odd integer

        OUTPUT: integer

        EXAMPLES::

            sage: (9/2).round()
            4
            sage: n = 4/3; n.round()
            1
            sage: n = -17/4; n.round()
            -4
            sage: n = -5/2; n.round()
            -2
            sage: n.round("away")
            -3
            sage: n.round("up")
            -2
            sage: n.round("down")
            -3
            sage: n.round("even")
            -2
            sage: n.round("odd")
            -3'''
    @overload
    def sign(self) -> Any:
        """Rational.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2771)

        Return the sign of this rational number, which is -1, 0, or 1
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: (2/3).sign()
            1
            sage: (0/3).sign()
            0
            sage: (-1/6).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """Rational.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2771)

        Return the sign of this rational number, which is -1, 0, or 1
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: (2/3).sign()
            1
            sage: (0/3).sign()
            0
            sage: (-1/6).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """Rational.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2771)

        Return the sign of this rational number, which is -1, 0, or 1
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: (2/3).sign()
            1
            sage: (0/3).sign()
            0
            sage: (-1/6).sign()
            -1"""
    @overload
    def sign(self) -> Any:
        """Rational.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2771)

        Return the sign of this rational number, which is -1, 0, or 1
        depending on whether this number is negative, zero, or positive
        respectively.

        OUTPUT: integer

        EXAMPLES::

            sage: (2/3).sign()
            1
            sage: (0/3).sign()
            0
            sage: (-1/6).sign()
            -1"""
    @overload
    def sqrt(self, prec=..., extend=..., all=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, x) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, all=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, prec=..., all=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """Rational.sqrt(self, prec=None, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1884)

        The square root function.

        INPUT:

        - ``prec`` -- integer (default: ``None``); if ``None``, returns
          an exact square root; otherwise returns a numerical square root if
          necessary, to the given bits of precision.

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square is not in the base ring. Ignored if
          ``prec`` is not ``None``.

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self`` (a list of length 0, 1, or 2)

        EXAMPLES::

            sage: x = 25/9
            sage: x.sqrt()
            5/3
            sage: sqrt(x)
            5/3
            sage: x = 64/4
            sage: x.sqrt()
            4
            sage: x = 100/1
            sage: x.sqrt()
            10
            sage: x.sqrt(all=True)
            [10, -10]
            sage: x = 81/5
            sage: x.sqrt()                                                              # needs sage.symbolic
            9*sqrt(1/5)
            sage: x = -81/3
            sage: x.sqrt()                                                              # needs sage.symbolic
            3*sqrt(-3)

        ::

            sage: n = 2/3
            sage: n.sqrt()                                                              # needs sage.symbolic
            sqrt(2/3)

            sage: # needs sage.rings.real_mpfr
            sage: n.sqrt(prec=10)
            0.82
            sage: n.sqrt(prec=100)
            0.81649658092772603273242802490
            sage: n.sqrt(prec=100)^2
            0.66666666666666666666666666667
            sage: n.sqrt(prec=53, all=True)
            [0.816496580927726, -0.816496580927726]
            sage: sqrt(-2/3, prec=53)
            0.816496580927726*I
            sage: sqrt(-2/3, prec=53, all=True)
            [0.816496580927726*I, -0.816496580927726*I]

            sage: n.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: square root of 2/3 not a rational number
            sage: n.sqrt(extend=False, all=True)
            []
            sage: sqrt(-2/3, all=True)                                                  # needs sage.symbolic
            [sqrt(-2/3), -sqrt(-2/3)]

        TESTS:

        Ensure that :issue:`37153` is fixed, so that behaviour aligns
        with other rings and fields.
        See :issue:`9466` and :issue:`26509` for context::

            sage: QQ(3).sqrt(extend=False, all=True)
            []
            sage: QQ(-1).sqrt(extend=False, all=True)
            []

        AUTHORS:

        - Naqi Jaffery (2006-03-05): some examples"""
    @overload
    def squarefree_part(self) -> Any:
        """Rational.squarefree_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1709)

        Return the square free part of `x`, i.e., an integer `z` such
        that `x = z y^2`, for a perfect square `y^2`.

        EXAMPLES::

            sage: a = 1/2
            sage: a.squarefree_part()
            2
            sage: b = a/a.squarefree_part()
            sage: b, b.is_square()
            (1/4, True)
            sage: a = 24/5
            sage: a.squarefree_part()
            30"""
    @overload
    def squarefree_part(self) -> Any:
        """Rational.squarefree_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1709)

        Return the square free part of `x`, i.e., an integer `z` such
        that `x = z y^2`, for a perfect square `y^2`.

        EXAMPLES::

            sage: a = 1/2
            sage: a.squarefree_part()
            2
            sage: b = a/a.squarefree_part()
            sage: b, b.is_square()
            (1/4, True)
            sage: a = 24/5
            sage: a.squarefree_part()
            30"""
    @overload
    def squarefree_part(self) -> Any:
        """Rational.squarefree_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1709)

        Return the square free part of `x`, i.e., an integer `z` such
        that `x = z y^2`, for a perfect square `y^2`.

        EXAMPLES::

            sage: a = 1/2
            sage: a.squarefree_part()
            2
            sage: b = a/a.squarefree_part()
            sage: b, b.is_square()
            (1/4, True)
            sage: a = 24/5
            sage: a.squarefree_part()
            30"""
    @overload
    def squarefree_part(self) -> Any:
        """Rational.squarefree_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1709)

        Return the square free part of `x`, i.e., an integer `z` such
        that `x = z y^2`, for a perfect square `y^2`.

        EXAMPLES::

            sage: a = 1/2
            sage: a.squarefree_part()
            2
            sage: b = a/a.squarefree_part()
            sage: b, b.is_square()
            (1/4, True)
            sage: a = 24/5
            sage: a.squarefree_part()
            30"""
    @overload
    def str(self, intbase=...) -> Any:
        """Rational.str(self, int base=10)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2162)

        Return a string representation of ``self`` in the given ``base``.

        INPUT:

        - ``base`` -- integer (default: 10); base must be between 2 and 36

        OUTPUT: string

        EXAMPLES::

            sage: (-4/17).str()
            '-4/17'
            sage: (-4/17).str(2)
            '-100/10001'

        Note that the base must be at most 36.

        ::

            sage: (-4/17).str(40)
            Traceback (most recent call last):
            ...
            ValueError: base (=40) must be between 2 and 36
            sage: (-4/17).str(1)
            Traceback (most recent call last):
            ...
            ValueError: base (=1) must be between 2 and 36"""
    @overload
    def str(self) -> Any:
        """Rational.str(self, int base=10)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2162)

        Return a string representation of ``self`` in the given ``base``.

        INPUT:

        - ``base`` -- integer (default: 10); base must be between 2 and 36

        OUTPUT: string

        EXAMPLES::

            sage: (-4/17).str()
            '-4/17'
            sage: (-4/17).str(2)
            '-100/10001'

        Note that the base must be at most 36.

        ::

            sage: (-4/17).str(40)
            Traceback (most recent call last):
            ...
            ValueError: base (=40) must be between 2 and 36
            sage: (-4/17).str(1)
            Traceback (most recent call last):
            ...
            ValueError: base (=1) must be between 2 and 36"""
    @overload
    def support(self) -> Any:
        """Rational.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3116)

        Return a sorted list of the primes where this rational number has
        nonzero valuation.

        OUTPUT: the set of primes appearing in the factorization of this
        rational with nonzero exponent, as a sorted list.

        EXAMPLES::

            sage: (-4/17).support()
            [2, 17]

        Trying to find the support of 0 gives an arithmetic error::

            sage: (0/1).support()
            Traceback (most recent call last):
            ...
            ArithmeticError: Support of 0 not defined."""
    @overload
    def support(self) -> Any:
        """Rational.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3116)

        Return a sorted list of the primes where this rational number has
        nonzero valuation.

        OUTPUT: the set of primes appearing in the factorization of this
        rational with nonzero exponent, as a sorted list.

        EXAMPLES::

            sage: (-4/17).support()
            [2, 17]

        Trying to find the support of 0 gives an arithmetic error::

            sage: (0/1).support()
            Traceback (most recent call last):
            ...
            ArithmeticError: Support of 0 not defined."""
    @overload
    def support(self) -> Any:
        """Rational.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3116)

        Return a sorted list of the primes where this rational number has
        nonzero valuation.

        OUTPUT: the set of primes appearing in the factorization of this
        rational with nonzero exponent, as a sorted list.

        EXAMPLES::

            sage: (-4/17).support()
            [2, 17]

        Trying to find the support of 0 gives an arithmetic error::

            sage: (0/1).support()
            Traceback (most recent call last):
            ...
            ArithmeticError: Support of 0 not defined."""
    def trace(self) -> Any:
        """Rational.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2905)

        Return the trace from `\\QQ` to `\\QQ` of `x` (which is just `x`). This
        was added for compatibility with :class:`NumberFields`.

        OUTPUT: ``Rational`` -- reference to ``self``

        EXAMPLES::

            sage: (1/3).trace()
             1/3

        AUTHORS:

        - Craig Citro"""
    @overload
    def trunc(self) -> Any:
        """Rational.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3360)

        Round this rational number to the nearest integer toward zero.

        EXAMPLES::

            sage: (5/3).trunc()
            1
            sage: (-5/3).trunc()
            -1
            sage: QQ(42).trunc()
            42
            sage: QQ(-42).trunc()
            -42"""
    @overload
    def trunc(self) -> Any:
        """Rational.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3360)

        Round this rational number to the nearest integer toward zero.

        EXAMPLES::

            sage: (5/3).trunc()
            1
            sage: (-5/3).trunc()
            -1
            sage: QQ(42).trunc()
            42
            sage: QQ(-42).trunc()
            -42"""
    @overload
    def trunc(self) -> Any:
        """Rational.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3360)

        Round this rational number to the nearest integer toward zero.

        EXAMPLES::

            sage: (5/3).trunc()
            1
            sage: (-5/3).trunc()
            -1
            sage: QQ(42).trunc()
            42
            sage: QQ(-42).trunc()
            -42"""
    @overload
    def trunc(self) -> Any:
        """Rational.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3360)

        Round this rational number to the nearest integer toward zero.

        EXAMPLES::

            sage: (5/3).trunc()
            1
            sage: (-5/3).trunc()
            -1
            sage: QQ(42).trunc()
            42
            sage: QQ(-42).trunc()
            -42"""
    @overload
    def trunc(self) -> Any:
        """Rational.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3360)

        Round this rational number to the nearest integer toward zero.

        EXAMPLES::

            sage: (5/3).trunc()
            1
            sage: (-5/3).trunc()
            -1
            sage: QQ(42).trunc()
            42
            sage: QQ(-42).trunc()
            -42"""
    @overload
    def val_unit(self, p) -> Any:
        """Rational.val_unit(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1780)

        Return a pair: the `p`-adic valuation of ``self``, and the `p`-adic
        unit of ``self``, as a :class:`Rational`.

        We do not require the `p` be prime, but it must be at least 2. For
        more documentation see :meth:`Integer.val_unit()`.

        INPUT:

        - ``p`` -- a prime

        OUTPUT:

        - integer; the `p`-adic valuation of this rational

        - ``Rational``; `p`-adic unit part of ``self``

        EXAMPLES::

            sage: (-4/17).val_unit(2)
            (2, -1/17)
            sage: (-4/17).val_unit(17)
            (-1, -4)
            sage: (0/1).val_unit(17)
            (+Infinity, 1)

        AUTHORS:

        - David Roe (2007-04-12)"""
    @overload
    def val_unit(self) -> Any:
        """Rational.val_unit(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1780)

        Return a pair: the `p`-adic valuation of ``self``, and the `p`-adic
        unit of ``self``, as a :class:`Rational`.

        We do not require the `p` be prime, but it must be at least 2. For
        more documentation see :meth:`Integer.val_unit()`.

        INPUT:

        - ``p`` -- a prime

        OUTPUT:

        - integer; the `p`-adic valuation of this rational

        - ``Rational``; `p`-adic unit part of ``self``

        EXAMPLES::

            sage: (-4/17).val_unit(2)
            (2, -1/17)
            sage: (-4/17).val_unit(17)
            (-1, -4)
            sage: (0/1).val_unit(17)
            (+Infinity, 1)

        AUTHORS:

        - David Roe (2007-04-12)"""
    @overload
    def valuation(self, p) -> Any:
        """Rational.valuation(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1153)

        Return the power of ``p`` in the factorization of ``self``.

        INPUT:

        - ``p`` -- a prime number

        OUTPUT:

        (integer or infinity) ``Infinity`` if ``self`` is zero, otherwise the
        (positive or negative) integer `e` such that ``self`` = `m*p^e`
        with `m` coprime to `p`.

        .. NOTE::

           See also :meth:`val_unit()` which returns the pair `(e,m)`. The
           function :meth:`ord()` is an alias for :meth:`valuation()`.

        EXAMPLES::

            sage: x = -5/9
            sage: x.valuation(5)
            1
            sage: x.ord(5)
            1
            sage: x.valuation(3)
            -2
            sage: x.valuation(2)
            0

        Some edge cases::

            sage: (0/1).valuation(4)
            +Infinity
            sage: (7/16).valuation(4)
            -2"""
    @overload
    def valuation(self) -> Any:
        """Rational.valuation(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1153)

        Return the power of ``p`` in the factorization of ``self``.

        INPUT:

        - ``p`` -- a prime number

        OUTPUT:

        (integer or infinity) ``Infinity`` if ``self`` is zero, otherwise the
        (positive or negative) integer `e` such that ``self`` = `m*p^e`
        with `m` coprime to `p`.

        .. NOTE::

           See also :meth:`val_unit()` which returns the pair `(e,m)`. The
           function :meth:`ord()` is an alias for :meth:`valuation()`.

        EXAMPLES::

            sage: x = -5/9
            sage: x.valuation(5)
            1
            sage: x.ord(5)
            1
            sage: x.valuation(3)
            -2
            sage: x.valuation(2)
            0

        Some edge cases::

            sage: (0/1).valuation(4)
            +Infinity
            sage: (7/16).valuation(4)
            -2"""
    @overload
    def __abs__(self) -> Any:
        """Rational.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2753)

        Return the absolute value of this rational number.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__abs__()
            4/17
            sage: abs(-4/17)
            4/17"""
    @overload
    def __abs__(self) -> Any:
        """Rational.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2753)

        Return the absolute value of this rational number.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__abs__()
            4/17
            sage: abs(-4/17)
            4/17"""
    def __add__(self, left, right) -> Any:
        """Rational.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2315)

        Return ``left`` plus ``right``.

        EXAMPLES::

            sage: (2/3) + (1/6)
            5/6
            sage: (1/3) + (1/2)
            5/6
            sage: (1/3) + 2
            7/3"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Rational.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 900)

        EXAMPLES::

            sage: a = -17/37
            sage: copy(a) is a
            True

        Coercion does not make a new copy::

            sage: QQ(a) is a
            True

        Calling the constructor directly makes a new copy::

            sage: Rational(a) is a
            False"""
    def __deepcopy__(self, memo) -> Any:
        """Rational.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 921)

        EXAMPLES::

            sage: a = -17/37
            sage: deepcopy(a) is a
            True"""
    @overload
    def __float__(self) -> Any:
        """Rational.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2210)

        Return floating point approximation to ``self`` as a Python float.

        OUTPUT: float

        EXAMPLES::

            sage: (-4/17).__float__()
            -0.23529411764705882
            sage: float(-4/17)
            -0.23529411764705882
            sage: float(1/3)
            0.3333333333333333
            sage: float(1/10)
            0.1
            sage: n = QQ(902834098234908209348209834092834098); float(n)
            9.028340982349083e+35

        TESTS:

        Test that conversion agrees with `RR`::

            sage: Q = [a/b for a in [-99..99] for b in [1..99]]
            sage: all(RDF(q) == RR(q) for q in Q)
            True

        Test that the conversion has correct rounding on simple rationals::

            sage: for p in [-100..100]:                                                 # needs sage.rings.real_mpfr
            ....:   for q in [1..100]:
            ....:       r = RDF(p/q)
            ....:       assert (RR(r).exact_rational() - p/q) <= r.ulp()/2

        Test larger rationals::

            sage: Q = continued_fraction(pi).convergents()[:100]                        # needs sage.symbolic
            sage: all(RDF(q) == RR(q) for q in Q)
            True

        At some point, the continued fraction and direct conversion
        to ``RDF`` should agree::

            sage: RDFpi = RDF(pi)                                                       # needs sage.symbolic
            sage: all(RDF(q) == RDFpi for q in Q[20:])                                  # needs sage.symbolic
            True"""
    @overload
    def __float__(self) -> Any:
        """Rational.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2210)

        Return floating point approximation to ``self`` as a Python float.

        OUTPUT: float

        EXAMPLES::

            sage: (-4/17).__float__()
            -0.23529411764705882
            sage: float(-4/17)
            -0.23529411764705882
            sage: float(1/3)
            0.3333333333333333
            sage: float(1/10)
            0.1
            sage: n = QQ(902834098234908209348209834092834098); float(n)
            9.028340982349083e+35

        TESTS:

        Test that conversion agrees with `RR`::

            sage: Q = [a/b for a in [-99..99] for b in [1..99]]
            sage: all(RDF(q) == RR(q) for q in Q)
            True

        Test that the conversion has correct rounding on simple rationals::

            sage: for p in [-100..100]:                                                 # needs sage.rings.real_mpfr
            ....:   for q in [1..100]:
            ....:       r = RDF(p/q)
            ....:       assert (RR(r).exact_rational() - p/q) <= r.ulp()/2

        Test larger rationals::

            sage: Q = continued_fraction(pi).convergents()[:100]                        # needs sage.symbolic
            sage: all(RDF(q) == RR(q) for q in Q)
            True

        At some point, the continued fraction and direct conversion
        to ``RDF`` should agree::

            sage: RDFpi = RDF(pi)                                                       # needs sage.symbolic
            sage: all(RDF(q) == RDFpi for q in Q[20:])                                  # needs sage.symbolic
            True"""
    def __getitem__(self, intn) -> Any:
        """Rational.__getitem__(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2286)

        Return ``n``-th element of ``self``, viewed as a list. This is for
        consistency with how number field elements work.

        INPUT:

        - ``n`` -- integer (error if not 0 or -1)

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17)[0]
            -4/17
            sage: (-4/17)[1]
            Traceback (most recent call last):
            ...
            IndexError: index n (=1) out of range; it must be 0
            sage: (-4/17)[-1]   # indexing from the right
            -4/17"""
    @overload
    def __hash__(self) -> Any:
        """Rational.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2259)

        Return hash of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: QQ(42).__hash__()
            42
            sage: QQ(1/42).__hash__()
            1488680910            # 32-bit
            -7658195599476688946  # 64-bit
            sage: n = ZZ.random_element(10^100)
            sage: hash(n) == hash(QQ(n)) or n
            True
            sage: hash(-n) == hash(-QQ(n)) or n
            True
            sage: hash(-4/17)
            -47583156            # 32-bit
            8709371129873690700  # 64-bit"""
    @overload
    def __hash__(self) -> Any:
        """Rational.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2259)

        Return hash of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: QQ(42).__hash__()
            42
            sage: QQ(1/42).__hash__()
            1488680910            # 32-bit
            -7658195599476688946  # 64-bit
            sage: n = ZZ.random_element(10^100)
            sage: hash(n) == hash(QQ(n)) or n
            True
            sage: hash(-n) == hash(-QQ(n)) or n
            True
            sage: hash(-4/17)
            -47583156            # 32-bit
            8709371129873690700  # 64-bit"""
    @overload
    def __hash__(self) -> Any:
        """Rational.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2259)

        Return hash of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: QQ(42).__hash__()
            42
            sage: QQ(1/42).__hash__()
            1488680910            # 32-bit
            -7658195599476688946  # 64-bit
            sage: n = ZZ.random_element(10^100)
            sage: hash(n) == hash(QQ(n)) or n
            True
            sage: hash(-n) == hash(-QQ(n)) or n
            True
            sage: hash(-4/17)
            -47583156            # 32-bit
            8709371129873690700  # 64-bit"""
    def __index__(self) -> Any:
        """Rational.__index__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 567)

        Needed so integers can be used as list indices.

        EXAMPLES::

            sage: v = [1,2,3,4,5]
            sage: v[3/1]
            4
            sage: v[3/2]
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 3/2 to an integer"""
    def __int__(self) -> Any:
        """Rational.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3028)

        Convert this rational to a Python ``int``.

        This truncates ``self`` if ``self`` has a denominator (which is
        consistent with Python's ``int(floats)``).

        EXAMPLES::

            sage: int(7/1)
            7
            sage: int(7/2)
            3"""
    @overload
    def __invert__(self) -> Any:
        """Rational.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2526)

        Return the multiplicative inverse of ``self``.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__invert__()
            -17/4
            sage: ~(-4/17)
            -17/4"""
    @overload
    def __invert__(self) -> Any:
        """Rational.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2526)

        Return the multiplicative inverse of ``self``.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__invert__()
            -17/4
            sage: ~(-4/17)
            -17/4"""
    def __lshift__(self, x, y) -> Any:
        """Rational.__lshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3697)

        Left shift operator ``x << y``.

        INPUT:

        - ``x``, ``y`` -- integer or rational

        OUTPUT: rational

        EXAMPLES::

            sage: (2/3).__lshift__(4/1)
            32/3
            sage: (2/3).__lshift__(4/7)
            Traceback (most recent call last):
            ...
            ValueError: denominator must be 1
            sage: (2).__lshift__(4/1)
            32
            sage: (2/3).__lshift__(4)
            32/3
            sage: (2/3) << (4/1)
            32/3"""
    def __mod__(self, x, y) -> Any:
        """Rational.__mod__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2821)

        Return the remainder of division of ``x`` by ``y``, where ``y`` is
        something that can be coerced to an integer.

        INPUT:

        - ``other`` -- object that coerces to an integer

        OUTPUT: integer

        EXAMPLES::

            sage: (-4/17).__mod__(3/1)
            1

        TESTS:

        Check that :issue:`14870` is fixed::

            sage: int(4) % QQ(3)
            1"""
    @overload
    def __mpq__(self) -> Any:
        """Rational.__mpq__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1028)

        Convert Sage ``Rational`` to gmpy2 ``Rational``.

        EXAMPLES::

            sage: r = 5/3
            sage: r.__mpq__()
            mpq(5,3)
            sage: from gmpy2 import mpq
            sage: mpq(r)
            mpq(5,3)"""
    @overload
    def __mpq__(self) -> Any:
        """Rational.__mpq__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1028)

        Convert Sage ``Rational`` to gmpy2 ``Rational``.

        EXAMPLES::

            sage: r = 5/3
            sage: r.__mpq__()
            mpq(5,3)
            sage: from gmpy2 import mpq
            sage: mpq(r)
            mpq(5,3)"""
    @overload
    def __mpz__(self) -> Any:
        '''Rational.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1002)

        Return a gmpy2 ``mpz`` if this Rational is an integer.

        EXAMPLES::

            sage: q = 6/2
            sage: q.__mpz__()
            mpz(3)
            sage: q = 1/4
            sage: q.__mpz__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 1/4 to an integer

        TESTS::

            sage: QQ().__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpz__(self) -> Any:
        '''Rational.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1002)

        Return a gmpy2 ``mpz`` if this Rational is an integer.

        EXAMPLES::

            sage: q = 6/2
            sage: q.__mpz__()
            mpz(3)
            sage: q = 1/4
            sage: q.__mpz__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 1/4 to an integer

        TESTS::

            sage: QQ().__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpz__(self) -> Any:
        '''Rational.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1002)

        Return a gmpy2 ``mpz`` if this Rational is an integer.

        EXAMPLES::

            sage: q = 6/2
            sage: q.__mpz__()
            mpz(3)
            sage: q = 1/4
            sage: q.__mpz__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 1/4 to an integer

        TESTS::

            sage: QQ().__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpz__(self) -> Any:
        '''Rational.__mpz__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 1002)

        Return a gmpy2 ``mpz`` if this Rational is an integer.

        EXAMPLES::

            sage: q = 6/2
            sage: q.__mpz__()
            mpz(3)
            sage: q = 1/4
            sage: q.__mpz__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 1/4 to an integer

        TESTS::

            sage: QQ().__mpz__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    def __mul__(self, left, right) -> Any:
        """Rational.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2420)

        Return ``left`` times ``right``.

        EXAMPLES::

            sage: (3/14) * 2/3
            1/7
            sage: (3/14) * 10
            15/7
            sage: 3/14 * polygen(QQ)
            3/14*x"""
    @overload
    def __neg__(self) -> Any:
        """Rational.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2719)

        Return the negative of ``self``.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__neg__()
            4/17
            sage: - (-4/17)
            4/17"""
    @overload
    def __neg__(self) -> Any:
        """Rational.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2719)

        Return the negative of ``self``.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__neg__()
            4/17
            sage: - (-4/17)
            4/17"""
    @overload
    def __pari__(self) -> Any:
        """Rational.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3796)

        Return the PARI version of this rational number.

        EXAMPLES::

            sage: n = 9390823/17
            sage: m = n.__pari__(); m                                                   # needs sage.libs.pari
            9390823/17
            sage: type(m)                                                               # needs sage.libs.pari
            <class 'cypari2.gen.Gen'>
            sage: m.type()                                                              # needs sage.libs.pari
            't_FRAC'"""
    @overload
    def __pari__(self) -> Any:
        """Rational.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3796)

        Return the PARI version of this rational number.

        EXAMPLES::

            sage: n = 9390823/17
            sage: m = n.__pari__(); m                                                   # needs sage.libs.pari
            9390823/17
            sage: type(m)                                                               # needs sage.libs.pari
            <class 'cypari2.gen.Gen'>
            sage: m.type()                                                              # needs sage.libs.pari
            't_FRAC'"""
    @overload
    def __pos__(self) -> Any:
        """Rational.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2704)

        Return ``self``.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__pos__()
            -4/17
            sage: +(-4/17)
            -4/17"""
    @overload
    def __pos__(self) -> Any:
        """Rational.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2704)

        Return ``self``.

        OUTPUT: rational

        EXAMPLES::

            sage: (-4/17).__pos__()
            -4/17
            sage: +(-4/17)
            -4/17"""
    def __radd__(self, other):
        """Return value+self."""
    @overload
    def __reduce__(self) -> Any:
        """Rational.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 555)

        Used in pickling rational numbers.

        EXAMPLES::

            sage: a = 3/5
            sage: a.__reduce__()
            (<cyfunction make_rational at ...>, ('3/5',))"""
    @overload
    def __reduce__(self) -> Any:
        """Rational.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 555)

        Used in pickling rational numbers.

        EXAMPLES::

            sage: a = 3/5
            sage: a.__reduce__()
            (<cyfunction make_rational at ...>, ('3/5',))"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __round__(self):
        '''Rational.round(self, mode=\'even\')

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3380)

        Return the nearest integer to ``self``, rounding to even by default.

        INPUT:

        - ``self`` -- a rational number

        - ``mode`` -- a rounding mode for half integers:

           - ``\'toward\'`` rounds toward zero
           - ``\'away\'`` (default) rounds away from zero
           - ``\'up\'`` rounds up
           - ``\'down\'`` rounds down
           - ``\'even\'`` rounds toward the even integer
           - ``\'odd\'`` rounds toward the odd integer

        OUTPUT: integer

        EXAMPLES::

            sage: (9/2).round()
            4
            sage: n = 4/3; n.round()
            1
            sage: n = -17/4; n.round()
            -4
            sage: n = -5/2; n.round()
            -2
            sage: n.round("away")
            -3
            sage: n.round("up")
            -2
            sage: n.round("down")
            -3
            sage: n.round("even")
            -2
            sage: n.round("odd")
            -3'''
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, x, y) -> Any:
        """Rational.__rshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 3745)

        Right shift operator ``x >> y``.

        INPUT:

        - ``x``, ``y`` -- integer or rational

        OUTPUT: rational

        EXAMPLES::

            sage: (2/3).__rshift__(4/1)
            1/24
            sage: (2/3).__rshift__(4/7)
            Traceback (most recent call last):
            ...
            ValueError: denominator must be 1
            sage: (2).__rshift__(4/1)
            0
            sage: (2/1).__rshift__(4)
            1/8
            sage: (2/1) >>(4/1)
            1/8"""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __sub__(self, left, right) -> Any:
        """Rational.__sub__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2356)

        Return ``left`` minus ``right``.

        EXAMPLES::

            sage: 11/3 - 5/4
            29/12

            sage: (2/3) - 2
            -4/3
            sage: (-2/3) - 1
            -5/3
            sage: (2/3) - (-3)
            11/3
            sage: (-2/3) - (-3)
            7/3
            sage: 2/3 - polygen(QQ)
            -x + 2/3"""
    def __truediv__(self, left, right) -> Any:
        """Rational.__truediv__(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 2467)

        Return ``left`` divided by ``right``.

        EXAMPLES::

            sage: QQ((2,3)) / QQ((-5,4))
            -8/15
            sage: QQ((22,3)) / 4
            11/6
            sage: QQ((-2,3)) / (-4)
            1/6
            sage: QQ((2,3)) / QQ.zero()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero"""

class Z_to_Q(sage.categories.morphism.Morphism):
    """Z_to_Q()

    File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4098)

    A morphism from `\\ZZ` to `\\QQ`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4103)

                Create morphism from integers to rationals.

                EXAMPLES::

                    sage: sage.rings.rational.Z_to_Q()
                    Natural morphism:
                      From: Integer Ring
                      To:   Rational Field
        """
    @overload
    def is_surjective(self) -> Any:
        """Z_to_Q.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4165)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: QQ.coerce_map_from(ZZ).is_surjective()
            False"""
    @overload
    def is_surjective(self) -> Any:
        """Z_to_Q.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4165)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: QQ.coerce_map_from(ZZ).is_surjective()
            False"""
    @overload
    def section(self) -> Any:
        """Z_to_Q.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4144)

        Return a section of this morphism.

        EXAMPLES::

            sage: f = QQ.coerce_map_from(ZZ).section(); f
            Generic map:
              From: Rational Field
              To:   Integer Ring

        This map is a morphism in the category of sets with partial
        maps (see :issue:`15618`)::

            sage: f.parent()
            Set of Morphisms from Rational Field to Integer Ring
             in Category of sets with partial maps"""
    @overload
    def section(self) -> Any:
        """Z_to_Q.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4144)

        Return a section of this morphism.

        EXAMPLES::

            sage: f = QQ.coerce_map_from(ZZ).section(); f
            Generic map:
              From: Rational Field
              To:   Integer Ring

        This map is a morphism in the category of sets with partial
        maps (see :issue:`15618`)::

            sage: f.parent()
            Set of Morphisms from Rational Field to Integer Ring
             in Category of sets with partial maps"""

class int_to_Q(sage.categories.morphism.Morphism):
    """int_to_Q()

    File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4219)

    A morphism from Python 3 ``int`` to `\\QQ`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/rational.pyx (starting at line 4223)

                Initialize ``self``.

                EXAMPLES::

                    sage: sage.rings.rational.int_to_Q()
                    Native morphism:
                      From: Set of Python objects of class 'int'
                      To:   Rational Field
        """
