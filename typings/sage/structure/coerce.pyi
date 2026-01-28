r"""
The coercion model

The coercion model manages how elements of one parent get related to elements
of another. For example, the integer 2 can canonically be viewed as an element
of the rational numbers. (The parent of a non-element is its Python type.)

::

    sage: ZZ(2).parent()
    Integer Ring
    sage: QQ(2).parent()
    Rational Field

The most prominent role of the coercion model is to make sense of binary
operations between elements that have distinct parents. It does this by
finding a parent where both elements make sense, and doing the operation
there. For example::

    sage: a = 1/2; a.parent()
    Rational Field
    sage: b = ZZ['x'].gen(); b.parent()
    Univariate Polynomial Ring in x over Integer Ring
    sage: a + b
    x + 1/2
    sage: (a + b).parent()
    Univariate Polynomial Ring in x over Rational Field

If there is a coercion (see below) from one of the parents to the other,
the operation is always performed in the codomain of that coercion. Otherwise
a reasonable attempt to create a new parent with coercion maps from both
original parents is made. The results of these discoveries are cached.
On failure, a :exc:`TypeError` is always raised.

Some arithmetic operations (such as multiplication) can indicate an action
rather than arithmetic in a common parent. For example::

    sage: E = EllipticCurve('37a')                                                      # needs sage.schemes
    sage: P = E(0,0)                                                                    # needs sage.schemes
    sage: 5*P                                                                           # needs sage.schemes
    (1/4 : -5/8 : 1)

where there is action of `\ZZ` on the points of `E` given by the additive
group law. Parents can specify how they act on or are acted upon by other
parents.

There are two kinds of ways to get from one parent to another, coercions and
conversions.

Coercions are canonical (possibly modulo a finite number of
deterministic choices) morphisms, and the set of all coercions between
all parents forms a commuting diagram (modulo possibly rounding
issues). `\ZZ \rightarrow \QQ` is an example of a
coercion. These are invoked implicitly by the coercion model.

Conversions try to construct an element out of their input if at all possible.
Examples include sections of coercions, creating an element from a string or
list, etc. and may fail on some inputs of a given type while succeeding on
others (i.e. they may not be defined on the whole domain). Conversions are
always explicitly invoked, and never used by the coercion model to resolve
binary operations.

For more information on how to specify coercions, conversions, and actions,
see the documentation for :class:`Parent`.
"""

from collections.abc import Callable
from typing import Any, TypeGuard, Union, overload
from typings_sagemath import SupportsSage
from sage.structure.element import Element
from sage.structure.sage_object import SageObject
from sage.structure.parent import Parent
from sage.categories.map import Map
from sage.categories.action import Action
from numpy import number as NumPyNumber
from operator import mul

from sage.categories.morphism import IdentityMorphism as IdentityMorphism
from sage.structure.coerce_exceptions import CoercionException as CoercionException
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal


from typings_sagemath import MpmathType, NumPyType

def is_mpmath_type(t: object) -> TypeGuard[type[MpmathType]]:
    r"""
    Check whether the type ``t`` is a type whose name starts with either
    ``mpmath.`` or ``sage.libs.mpmath.``.

    EXAMPLES::

        sage: # needs mpmath
        sage: from sage.structure.coerce import is_mpmath_type
        sage: is_mpmath_type(int)
        False
        sage: import mpmath
        sage: is_mpmath_type(mpmath.mpc(2))
        False
        sage: is_mpmath_type(type(mpmath.mpc(2)))
        True
        sage: is_mpmath_type(type(mpmath.mpf(2)))
        True
    """

def is_numpy_type(t: object) -> TypeGuard[type[NumPyType]]:
    """
    Return ``True`` if and only if `t` is a type whose name starts
    with ``numpy.``

    EXAMPLES::

        sage: from sage.structure.coerce import is_numpy_type

        sage: # needs numpy
        sage: import numpy
        sage: is_numpy_type(numpy.int16)
        True
        sage: is_numpy_type(numpy.floating)
        True
        sage: is_numpy_type(numpy.ndarray)
        True
        sage: is_numpy_type(numpy.matrix)
        True

        sage: is_numpy_type(int)
        False
        sage: is_numpy_type(Integer)
        False
        sage: is_numpy_type(Sudoku)                                                     # needs sage.combinat
        False
        sage: is_numpy_type(None)
        False

    TESTS:

    This used to crash Sage (:issue:`20715`)::

        sage: is_numpy_type(object)
        False
        sage: 1 + object()
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand parent(s) for +: 'Integer Ring' and
        '<class 'object'>'
    """
def parent_is_integers(P: type | Parent) -> bool:
    """
    Check whether the type or parent represents the ring of integers.

    EXAMPLES::

        sage: from sage.structure.coerce import parent_is_integers
        sage: parent_is_integers(int)
        True
        sage: parent_is_integers(float)
        False
        sage: parent_is_integers(bool)
        True
        sage: parent_is_integers(dict)
        False

        sage: import numpy                                                              # needs numpy
        sage: parent_is_integers(numpy.int16)                                           # needs numpy
        True
        sage: parent_is_integers(numpy.uint64)                                          # needs numpy
        True
        sage: parent_is_integers(float)
        False

        sage: import gmpy2
        sage: parent_is_integers(gmpy2.mpz)
        True
        sage: parent_is_integers(gmpy2.mpq)
        False

    Ensure (:issue:`27893`) is fixed::

        sage: K.<f> = QQ[]
        sage: gmpy2.mpz(2) * f
        2*f
    """
    ...
def parent_is_numerical(P: type | Parent) -> bool:
    r"""
    Test if elements of the parent or type ``P`` can be numerically evaluated
    as complex numbers (in a canonical way).

    EXAMPLES::

        sage: from sage.structure.coerce import parent_is_numerical
        sage: import gmpy2
        sage: [parent_is_numerical(R) for R in [QQ, int, complex, gmpy2.mpc]]           # needs sage.rings.complex_double
        [True, True, True, True]
        sage: [parent_is_numerical(R) for R in [RR, CC]]                                # needs sage.rings.real_mpfr
        [True, True]
        sage: parent_is_numerical(QuadraticField(-1))                                   # needs sage.rings.number_field
        True
        sage: import numpy; parent_is_numerical(numpy.complexfloating)                  # needs numpy
        True
        sage: parent_is_numerical(SR)                                                   # needs sage.symbolic
        False
        sage: [parent_is_numerical(R) for R in [QQ['x'], QQ[['x']], str]]
        [False, False, False]
        sage: [parent_is_numerical(R) for R in [RIF, RBF, CIF, CBF]]                    # needs sage.libs.flint
        [False, False, False, False]
    """
    ...
def parent_is_real_numerical(P: type | Parent) -> bool:
    r"""
    Test if elements of the parent or type ``P`` can be numerically evaluated
    as real numbers (in a canonical way).

    EXAMPLES::

        sage: from sage.structure.coerce import parent_is_real_numerical
        sage: import gmpy2
        sage: [parent_is_real_numerical(R) for R in [RR, QQ, ZZ, RLF, int, float, gmpy2.mpq]]
        [True, True, True, True, True, True, True]
        sage: parent_is_real_numerical(QuadraticField(2))                               # needs sage.rings.number_field
        True
        sage: import numpy; parent_is_real_numerical(numpy.integer)                     # needs numpy
        True
        sage: parent_is_real_numerical(QuadraticField(-1))                              # needs sage.rings.number_field
        False
        sage: [parent_is_real_numerical(R)                                              # needs numpy
        ....:  for R in [CC, complex, gmpy2.mpc, numpy.complexfloating]]
        [False, False, False, False]
        sage: [parent_is_real_numerical(R) for R in [QQ['x'], QQ[['x']], str]]
        [False, False, False]
        sage: parent_is_real_numerical(SR)                                              # needs sage.symbolic
        False
        sage: [parent_is_real_numerical(R) for R in [RIF, RBF, CIF, CBF]]               # needs sage.libs.flint
        [False, False, False, False]
    """
    ...
def py_scalar_parent(py_type: type) -> Parent | None:
    """
    Return the Sage equivalent of the given python type, if one exists.
    If there is no equivalent, return ``None``.

    EXAMPLES::

        sage: from sage.structure.coerce import py_scalar_parent
        sage: py_scalar_parent(int)
        Integer Ring
        sage: py_scalar_parent(float)
        Real Double Field
        sage: py_scalar_parent(complex)                                                 # needs sage.rings.complex_double
        Complex Double Field
        sage: py_scalar_parent(bool)
        Integer Ring
        sage: py_scalar_parent(dict),
        (None,)

        sage: import fractions
        sage: py_scalar_parent(fractions.Fraction)
        Rational Field

        sage: # needs numpy
        sage: import numpy
        sage: py_scalar_parent(numpy.int16)
        Integer Ring
        sage: py_scalar_parent(numpy.int32)
        Integer Ring
        sage: py_scalar_parent(numpy.uint64)
        Integer Ring
        sage: py_scalar_parent(numpy.double)
        Real Double Field

        sage: import gmpy2
        sage: py_scalar_parent(gmpy2.mpz)
        Integer Ring
        sage: py_scalar_parent(gmpy2.mpq)
        Rational Field
        sage: py_scalar_parent(gmpy2.mpfr)
        Real Double Field
        sage: py_scalar_parent(gmpy2.mpc)                                               # needs sage.rings.complex_double
        Complex Double Field
    """
    ...
@overload
def py_scalar_to_element[P: Parent](x: Element[P]) -> Element[P]: ...
@overload
def py_scalar_to_element[T](x: T) -> Element | T:
    """
    Convert ``x`` to a Sage :class:`~sage.structure.element.Element` if possible.

    If ``x`` was already an :class:`~sage.structure.element.Element` or if there is no obvious
    conversion possible, just return ``x`` itself.

    EXAMPLES::

        sage: from sage.structure.coerce import py_scalar_to_element
        sage: x = py_scalar_to_element(42)
        sage: x, parent(x)
        (42, Integer Ring)
        sage: x = py_scalar_to_element(int(42))
        sage: x, parent(x)
        (42, Integer Ring)
        sage: x = py_scalar_to_element(float(42))
        sage: x, parent(x)
        (42.0, Real Double Field)
        sage: x = py_scalar_to_element(complex(42))                                     # needs sage.rings.complex_double
        sage: x, parent(x)                                                              # needs sage.rings.complex_double
        (42.0, Complex Double Field)
        sage: py_scalar_to_element('hello')
        'hello'

        sage: from fractions import Fraction
        sage: f = Fraction(int(2^100), int(3^100))
        sage: py_scalar_to_element(f)
        1267650600228229401496703205376/515377520732011331036461129765621272702107522001

    Note that bools are converted to 0 or 1::

        sage: py_scalar_to_element(False), py_scalar_to_element(True)
        (0, 1)

    Test gmpy2's types::

        sage: import gmpy2
        sage: x = py_scalar_to_element(gmpy2.mpz(42))
        sage: x, parent(x)
        (42, Integer Ring)
        sage: x = py_scalar_to_element(gmpy2.mpq('3/4'))
        sage: x, parent(x)
        (3/4, Rational Field)
        sage: x = py_scalar_to_element(gmpy2.mpfr(42.57))
        sage: x, parent(x)
        (42.57, Real Double Field)
        sage: x = py_scalar_to_element(gmpy2.mpc(int(42), int(42)))                     # needs sage.rings.complex_double
        sage: x, parent(x)                                                              # needs sage.rings.complex_double
        (42.0 + 42.0*I, Complex Double Field)

    Test compatibility with :func:`py_scalar_parent`::

        sage: from sage.structure.coerce import py_scalar_parent
        sage: elt = [True, int(42), float(42), complex(42)]
        sage: for x in elt:                                                             # needs sage.rings.complex_double
        ....:     assert py_scalar_parent(type(x)) == py_scalar_to_element(x).parent()

        sage: import numpy                                                              # needs numpy
        sage: elt = [numpy.int8('-12'),  numpy.uint8('143'),                            # needs numpy
        ....:        numpy.int16('-33'), numpy.uint16('122'),
        ....:        numpy.int32('-19'), numpy.uint32('44'),
        ....:        numpy.int64('-3'),  numpy.uint64('552'),
        ....:        numpy.float16('-1.23'), numpy.float32('-2.22'),
        ....:        numpy.float64('-3.412'), numpy.complex64(1.2+I),
        ....:        numpy.complex128(-2+I)]
        sage: for x in elt:                                                             # needs numpy
        ....:     assert py_scalar_parent(type(x)) == py_scalar_to_element(x).parent()

        sage: elt = [gmpy2.mpz(42), gmpy2.mpq('3/4'),
        ....:        gmpy2.mpfr(42.57), gmpy2.mpc(int(42), int(42))]
        sage: for x in elt:                                                             # needs sage.rings.complex_double
        ....:     assert py_scalar_parent(type(x)) == py_scalar_to_element(x).parent()
    """

type _Numeric = int | float | complex | NumPyNumber
type _Sage = SageObject | SupportsSage

class CoercionModel:
    '''
    See also :mod:`sage.categories.pushout`

    EXAMPLES::

        sage: f = ZZ[\'t\', \'x\'].0 + QQ[\'x\'].0 + CyclotomicField(13).gen(); f             # needs sage.rings.number_field
        t + x + zeta13
        sage: f.parent()                                                                # needs sage.rings.number_field
        Multivariate Polynomial Ring in t, x
         over Cyclotomic Field of order 13 and degree 12
        sage: ZZ[\'x\',\'y\'].0 + ~Frac(QQ[\'y\']).0
        (x*y + 1)/y
        sage: MatrixSpace(ZZ[\'x\'], 2, 2)(2) + ~Frac(QQ[\'x\']).0                          # needs sage.modules
        [(2*x + 1)/x           0]
        [          0 (2*x + 1)/x]
        sage: f = ZZ[\'x,y,z\'].0 + QQ[\'w,x,z,a\'].0; f
        w + x
        sage: f.parent()
        Multivariate Polynomial Ring in w, x, y, z, a over Rational Field
        sage: ZZ[\'x,y,z\'].0 + ZZ[\'w,x,z,a\'].1
        2*x

    TESTS:

    Check that :issue:`8426` is fixed (see also :issue:`18076`)::

        sage: import numpy                                                              # needs numpy
        sage: if int(numpy.version.short_version[0]) > 1:                               # needs numpy
        ....:     __ = numpy.set_printoptions(legacy="1.25")                            # needs numpy

        sage: # needs sage.rings.real_mpfr
        sage: x = polygen(RR)
        sage: numpy.float32(\'1.5\') * x                                                  # needs numpy
        1.50000000000000*x
        sage: x * numpy.float32(\'1.5\')                                                  # needs numpy
        1.50000000000000*x
        sage: p = x**3 + 2*x - 1
        sage: p(float(\'1.2\'))
        3.12800000000000
        sage: p(int(\'2\'))
        11.0000000000000

    This used to fail (see :issue:`18076`)::

        sage: 1/3 + numpy.int8(\'12\')                                                    # needs numpy
        37/3
        sage: -2/3 + numpy.int16(\'-2\')                                                  # needs numpy
        -8/3
        sage: 2/5 + numpy.uint8(\'2\')                                                    # needs numpy
        12/5

    The numpy types do not interact well with the Sage coercion framework. More
    precisely, if a numpy type is the first operand in a binary operation then
    this operation is done in numpy. The result is hence a numpy type::

        sage: numpy.uint8(\'2\') + 3                                                      # needs numpy
        5
        sage: type(_)                                                                   # needs numpy
        <class \'numpy.int32\'>  # 32-bit
        <class \'numpy.int64\'>  # 64-bit

        sage: numpy.int8(\'12\') + 1/3                                                    # needs numpy
        12.333333333333334
        sage: type(_)                                                                   # needs numpy
        <class \'numpy.float64\'>

    AUTHOR:

    - Robert Bradshaw'''
    type _CoercionMap = dict[tuple[SageObject | _Numeric, SageObject | _Numeric], tuple[Map, Map] | None] # TODO
    type _ActionMap = dict[tuple[Any, Any], Action | None] # TODO
    def __init__(self):
        """
                EXAMPLES::

                    sage: from sage.structure.coerce import CoercionModel
                    sage: cm = CoercionModel()
                    sage: x = polygen(ZZ, 'x')
                    sage: K = NumberField(x^2 - 2, 'a')                                         # needs sage.rings.number_field
                    sage: A = cm.get_action(ZZ, K, operator.mul)                                # needs sage.rings.number_field
                    sage: f, g = cm.coercion_maps(QQ, int)
                    sage: f, g = cm.coercion_maps(ZZ, int)
        """
    def analyse(
        self, xp: object, yp: object, op: Callable[..., Any] = mul
    ) -> tuple[list[str | Any], type | SageObject | None]:
        """CoercionModel.analyse(self, xp, yp, op=mul)

        File: /build/sagemath/src/sage/src/sage/structure/coerce.pyx (starting at line 935)

        Emulate the process of doing arithmetic between xp and yp, returning
        a list of steps and the parent that the result will live in.

        The :meth:`explain` method is easier to use, but if one wants access to
        the actual morphism and action objects (rather than their string
        representations), then this is the function to use.

        For programmatic usages, use :meth:`canonical_coercion` and
        :meth:`common_parent` instead.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: GF7 = GF(7)
            sage: steps, res = cm.analyse(GF7, ZZ)
            sage: steps
            ['Coercion on right operand via',
             Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 7,
             'Arithmetic performed after coercions.']
            sage: res
            Finite Field of size 7
            sage: f = steps[1]; type(f)
            <class 'sage.rings.finite_rings.integer_mod.Integer_to_IntegerMod'>
            sage: f(100)
            2"""
    def bin_op(self, x: object, y: object, op: Callable[[Any, Any], Any]) -> Any:
        """
        Execute the operation ``op`` on `x` and `y`.

        It first looks for an action
        corresponding to ``op``, and failing that, it tries to coerce `x` and `y`
        into a common parent and calls ``op`` on them.

        If it cannot make sense of the operation, a :exc:`TypeError` is raised.

        INPUT:

        - ``x`` -- the left operand

        - ``y`` -- the right operand

        - ``op`` -- a python function taking 2 arguments

          .. NOTE::

             ``op`` is often an arithmetic operation, but need not be so.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.bin_op(1/2, 5, operator.mul)
            5/2

        The operator can be any callable::

            sage: R.<x> = ZZ['x']
            sage: cm.bin_op(x^2 - 1, x + 1, gcd)
            x + 1

        Actions are detected and performed::

            sage: M = matrix(ZZ, 2, 2, range(4))                                        # needs sage.modules
            sage: V = vector(ZZ, [5,7])                                                 # needs sage.modules
            sage: cm.bin_op(M, V, operator.mul)                                         # needs sage.modules
            (7, 31)

        TESTS::

            sage: class Foo():
            ....:     def __rmul__(self, left):
            ....:         return 'hello'
            sage: H = Foo()
            sage: print(int(3)*H)
            hello
            sage: print(Integer(3)*H)
            hello
            sage: print(H*3)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: '<class '__main__.Foo'>' and 'Integer Ring'

            sage: class Nonsense():
            ....:     def __init__(self, s):
            ....:         self.s = s
            ....:     def __repr__(self):
            ....:         return self.s
            ....:     def __mul__(self, x):
            ....:         return Nonsense(self.s + chr(x%256))
            ....:     __add__ = __mul__
            ....:     def __rmul__(self, x):
            ....:         return Nonsense(chr(x%256) + self.s)
            ....:     __radd__ = __rmul__
            sage: a = Nonsense('blahblah')
            sage: a*80
            blahblahP
            sage: 80*a
            Pblahblah
            sage: a+80
            blahblahP
            sage: 80+a
            Pblahblah"""
    @overload
    def canonical_coercion[P: Parent | SageObject](
        self, x: Element[P], y: Element[P]
    ) -> tuple[Element[P], Element[P]]: ...
    @overload
    def canonical_coercion(
        self, x: _Numeric, y: _Numeric) -> tuple[_Numeric, _Numeric]: ...
    @overload
    def canonical_coercion[P: Parent | SageObject](
        self, x: _Sage, y: _Numeric) -> tuple[Element[P], Element[P]]: ...
    @overload
    def canonical_coercion[P: Parent | SageObject](
        self, x: _Numeric, y: _Sage) -> tuple[Element[P], Element[P]]: ...
    @overload
    def canonical_coercion[P: Parent | SageObject](
        self, x: _Sage, y: _Sage) -> tuple[Element[P], Element[P]]:
        """
        Given two elements `x` and `y`, with parents `S` and `R` respectively,
        find a common parent `Z` such that there are coercions
        `f: S \\to Z` and `g: R \\to Z` and return `f(x), g(y)`,
        which will have the same parent.

        Raises a type error if no such `Z` can be found.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.canonical_coercion(mod(2, 10), 17)
            (2, 7)

            sage: # needs sage.modules
            sage: x, y = cm.canonical_coercion(1/2, matrix(ZZ, 2, 2, range(4)))
            sage: x
            [1/2   0]
            [  0 1/2]
            sage: y
            [0 1]
            [2 3]
            sage: parent(x) is parent(y)
            True

        There is some support for non-Sage datatypes as well::

            sage: x, y = cm.canonical_coercion(int(5), 10)
            sage: type(x), type(y)
            (<class 'sage.rings.integer.Integer'>, <class 'sage.rings.integer.Integer'>)

            sage: x, y = cm.canonical_coercion(int(5), complex(3))
            sage: type(x), type(y)
            (<class 'complex'>, <class 'complex'>)

            sage: class MyClass:
            ....:     def _sage_(self):
            ....:         return 13
            sage: a, b = cm.canonical_coercion(MyClass(), 1/3)
            sage: a, b
            (13, 1/3)
            sage: type(a)
            <class 'sage.rings.rational.Rational'>

        We also make an exception for 0, even if `\\ZZ` does not map in::

            sage: canonical_coercion(vector([1, 2, 3]), 0)                              # needs sage.modules
            ((1, 2, 3), (0, 0, 0))
            sage: canonical_coercion(GF(5)(0), float(0))
            (0, 0)"""
    def coercion_maps(self, R: SageObject | type, S: SageObject | type
        ) -> tuple[Map|None, Map|None] | None:
        """
        Give two parents `R` and `S`, return a pair of coercion maps
        `f: R \\rightarrow Z` and `g: S \\rightarrow Z` , if such a `Z`
        can be found.

        In the (common) case that `R=Z` or `S=Z` then ``None`` is returned
        for `f` or `g` respectively rather than constructing (and subsequently
        calling) the identity morphism.

        If no suitable `f, g` can be found, a single ``None`` is returned.
        This result is cached.

        .. NOTE::

            By :issue:`14711`, coerce maps should be copied when using them
            outside of the coercion system, because they may become defunct
            by garbage collection.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: f, g = cm.coercion_maps(ZZ, QQ)
            sage: print(copy(f))
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: print(g)
            None

            sage: ZZx = ZZ['x']
            sage: f, g = cm.coercion_maps(ZZx, QQ)
            sage: print(f)
            (map internal to coercion system -- copy before use)
            Ring morphism:
              From: Univariate Polynomial Ring in x over Integer Ring
              To:   Univariate Polynomial Ring in x over Rational Field
            sage: print(g)
            (map internal to coercion system -- copy before use)
            Polynomial base injection morphism:
              From: Rational Field
              To:   Univariate Polynomial Ring in x over Rational Field

            sage: K = GF(7)
            sage: cm.coercion_maps(QQ, K) is None
            True

        Note that to break symmetry, if there is a coercion map in both
        directions, the parent on the left is used::

            sage: # needs sage.modules
            sage: V = QQ^3
            sage: W = V.__class__(QQ, 3)
            sage: V == W
            True
            sage: V is W
            False
            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.coercion_maps(V, W)
            (None,
             (map internal to coercion system -- copy before use)
             Coercion map:
               From: Vector space of dimension 3 over Rational Field
               To:   Vector space of dimension 3 over Rational Field)
            sage: cm.coercion_maps(W, V)
            (None,
             (map internal to coercion system -- copy before use)
             Coercion map:
               From: Vector space of dimension 3 over Rational Field
               To:   Vector space of dimension 3 over Rational Field)
            sage: v = V([1,2,3])
            sage: w = W([1,2,3])
            sage: parent(v + w) is V
            True
            sage: parent(w + v) is W
            True

        TESTS:

        We check that with :issue:`14058`, parents are still eligible for
        garbage collection after being involved in binary operations::

            sage: # needs sage.libs.pari
            sage: import gc
            sage: T = type(GF(2))
            sage: gc.collect()  # random
            852
            sage: N0 = len(list(o for o in gc.get_objects() if type(o) is T))
            sage: L = [ZZ(1) + GF(p)(1) for p in prime_range(2, 50)]
            sage: N1 = len(list(o for o in gc.get_objects() if type(o) is T))
            sage: N1 > N0
            True
            sage: del L
            sage: gc.collect()  # random
            3939
            sage: N2 = len(list(o for o in gc.get_objects() if type(o) is T))
            sage: N2 - N0
            0"""
    def common_parent(self, *args: object) -> type | SageObject | None:
        """
        Compute a common parent for all the inputs.

        It's essentially an `n`-ary canonical coercion except it can
        operate on parents rather than just elements.

        INPUT:

        - ``args`` -- set of elements and/or parents

        OUTPUT:

        A :class:`Parent` into which each input should coerce, or raises a
        :exc:`TypeError` if no such :class:`Parent` can be found.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.common_parent(ZZ, QQ)
            Rational Field
            sage: cm.common_parent(ZZ, QQ, RR)                                          # needs sage.rings.real_mpfr
            Real Field with 53 bits of precision
            sage: ZZT = ZZ[['T']]
            sage: QQT = QQ['T']
            sage: cm.common_parent(ZZT, QQT, RDF)
            Power Series Ring in T over Real Double Field
            sage: cm.common_parent(4r, 5r)
            <class 'int'>
            sage: cm.common_parent(int, float, ZZ)
            <class 'float'>
            sage: real_fields = [RealField(prec) for prec in [10,20..100]]              # needs sage.rings.real_mpfr
            sage: cm.common_parent(*real_fields)                                        # needs sage.rings.real_mpfr
            Real Field with 10 bits of precision

        There are some cases where the ordering does matter, but if a parent
        can be found it is always the same::

            sage: QQxy = QQ['x,y']
            sage: QQyz = QQ['y,z']
            sage: cm.common_parent(QQxy, QQyz) == cm.common_parent(QQyz, QQxy)
            True
            sage: QQzt = QQ['z,t']
            sage: cm.common_parent(QQxy, QQyz, QQzt)
            Multivariate Polynomial Ring in x, y, z, t over Rational Field
            sage: cm.common_parent(QQxy, QQzt, QQyz)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in z, t over Rational Field'"""
    @overload
    def discover_action[_RP: Parent, _SP: Parent](
            self, R: _RP, S: _SP, 
            op: Callable[[Any, Any], Any], 
            r: Element[_RP] | None = None, 
            s: Element[_SP] | None = None
        ) -> Action[_RP, _SP] | None:
        ...
    @overload
    def discover_action[_RP: Parent, _S](
            self, R: _RP, S: type[_S], 
            op: Callable[[Any, Any], Any], 
            r: Element[_RP] | None = None, 
            s: _S | None = None
        ) -> Action[_RP, _S] | None:
        ...
    @overload
    def discover_action[_R, _SP: Parent](
            self, R: type[_R], S: _SP, 
            op: Callable[[Any, Any], Any], 
            r: _R | None = None, 
            s: Element[_SP] | None = None
        ) -> Action[_R, _SP] | None:
        ...
    @overload
    def discover_action[_R, _S](
            self, R: type[_R], S: type[_S], 
            op: Callable[[Any, Any], Any], 
            r: _R | None = None, 
            s: _S | None = None) -> Action[_R, _S] | None:
        """
        INPUT:

        - ``R`` -- the left :class:`Parent` (or type)
        - ``S`` -- the right :class:`Parent` (or type)
        - ``op`` -- the operand, typically an element of the :mod:`operator` module
        - ``r`` -- (optional) element of `R`
        - ``s`` -- (optional) element of `S`

        OUTPUT: an action `A` such that `s` ``op`` `r` is given by `A(s,r)`

        The steps taken are illustrated below.

        EXAMPLES::

            sage: P.<x> = ZZ['x']
            sage: P.get_action(ZZ)
            Right scalar multiplication by Integer Ring on
             Univariate Polynomial Ring in x over Integer Ring
            sage: ZZ.get_action(P) is None
            True
            sage: cm = sage.structure.element.get_coercion_model()

        If `R` or `S` is a :class:`Parent`, ask it for an action by/on `R`::

            sage: cm.discover_action(ZZ, P, operator.mul)
            Left scalar multiplication by Integer Ring on
             Univariate Polynomial Ring in x over Integer Ring

        If `R` or `S` a type, recursively call :meth:`get_action`
        with the Sage versions of `R` and/or `S`::

            sage: cm.discover_action(P, int, operator.mul)
            Right scalar multiplication by Integer Ring on
             Univariate Polynomial Ring in x over Integer Ring
             with precomposition on right by Native morphism:
              From: Set of Python objects of class 'int'
              To:   Integer Ring

        If ``op`` is division, look for action on ``right`` by inverse::

            sage: cm.discover_action(P, ZZ, operator.truediv)
            Right inverse action by Rational Field on
             Univariate Polynomial Ring in x over Integer Ring
            with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Rational Field

        Check that :issue:`17740` is fixed::

            sage: R = GF(5)['x']
            sage: cm.discover_action(R, ZZ, operator.truediv)
            Right inverse action by Finite Field of size 5
             on Univariate Polynomial Ring in x over Finite Field of size 5
            with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Finite Field of size 5
            sage: cm.bin_op(R.gen(), 7, operator.truediv).parent()
            Univariate Polynomial Ring in x over Finite Field of size 5

        Check that :issue:`18221` is fixed::

            sage: # needs sage.combinat sage.modules
            sage: F.<x> = FreeAlgebra(QQ)
            sage: x / 2
            1/2*x
            sage: cm.discover_action(F, ZZ, operator.truediv)
            Right inverse action by Rational Field on
             Free Algebra on 1 generator (x,) over Rational Field
             with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Rational Field"""
    def discover_coercion(
            self, R: SageObject | type, S: SageObject | type
        ) -> tuple[Map|None, Map|None] | None:
        '''
        This actually implements the finding of coercion maps as described in
        the :meth:`coercion_maps` method.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()

        If R is S, then two identity morphisms suffice::

            sage: cm.discover_coercion(SR, SR)                                          # needs sage.symbolic
            (None, None)

        If there is a coercion map either direction, use that::

            sage: cm.discover_coercion(ZZ, QQ)
            ((map internal to coercion system -- copy before use)
            Natural morphism:
              From: Integer Ring
              To:   Rational Field, None)
            sage: cm.discover_coercion(RR, QQ)                                          # needs sage.rings.real_mpfr
            (None, (map internal to coercion system -- copy before use)
             Generic map:
              From: Rational Field
              To:   Real Field with 53 bits of precision)

        Otherwise, try and compute an appropriate cover::

            sage: ZZxy = ZZ[\'x,y\']
            sage: cm.discover_coercion(ZZxy, RDF)
            ((map internal to coercion system -- copy before use)
             Coercion map:
               From: Multivariate Polynomial Ring in x, y over Integer Ring
               To:   Multivariate Polynomial Ring in x, y over Real Double Field,
             (map internal to coercion system -- copy before use)
             Polynomial base injection morphism:
               From: Real Double Field
               To:   Multivariate Polynomial Ring in x, y over Real Double Field)

        Sometimes there is a reasonable "cover," but no canonical coercion::

            sage: sage.categories.pushout.pushout(QQ, QQ^3)                             # needs sage.modules
            Vector space of dimension 3 over Rational Field
            sage: print(cm.discover_coercion(QQ, QQ^3))                                 # needs sage.modules
            None'''
    def division_parent(self, P: Parent) -> SageObject | type:
        """
        Deduces where the result of division in ``P`` lies by
        calculating the inverse of ``P.one()`` or ``P.an_element()``.

        The result is cached.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.division_parent(ZZ)
            Rational Field
            sage: cm.division_parent(QQ)
            Rational Field
            sage: ZZx = ZZ['x']
            sage: cm.division_parent(ZZx)
            Fraction Field of Univariate Polynomial Ring in x over Integer Ring
            sage: K = GF(41)
            sage: cm.division_parent(K)
            Finite Field of size 41
            sage: Zmod100 = Integers(100)
            sage: cm.division_parent(Zmod100)
            Ring of integers modulo 100
            sage: S5 = SymmetricGroup(5)                                                # needs sage.groups
            sage: cm.division_parent(S5)                                                # needs sage.groups
            Symmetric group of order 5! as a permutation group"""
    def exception_stack(self) -> list[str]:
        """
        Return the list of exceptions that were caught in the course of
        executing the last binary operation. Useful for diagnosis when
        user-defined maps or actions raise exceptions that are caught in
        the course of coercion detection.

        If all went well, this should be the empty list. If things aren't
        happening as you expect, this is a good place to check. See also
        :func:`coercion_traceback`.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.record_exceptions()
            sage: 1/2 + 2
            5/2
            sage: cm.exception_stack()
            []
            sage: 1/2 + GF(3)(2)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Rational Field' and 'Finite Field of size 3'

        Now see what the actual problem was::

            sage: import traceback
            sage: cm.exception_stack()
            ['Traceback (most recent call last):...', 'Traceback (most recent call last):...']
            sage: print(cm.exception_stack()[-1])
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Rational Field' and 'Finite Field of size 3'

        This is typically accessed via the :func:`coercion_traceback` function.

        ::

            sage: coercion_traceback()
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Rational Field' and 'Finite Field of size 3'"""
    def explain(
        self, xp: object, yp: object, op: Callable[..., Any] = mul, 
        intverbosity: int = 2
    ) -> type | SageObject | None:
        """
        This function can be used to understand what coercions will happen
        for an arithmetic operation between xp and yp (which may be either
        elements or parents). If the parent of the result can be determined
        then it will be returned.

        For programmatic usages, use :meth:`canonical_coercion` and
        :meth:`common_parent` instead.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()

            sage: cm.explain(ZZ, ZZ)
            Identical parents, arithmetic performed immediately.
            Result lives in Integer Ring
            Integer Ring

            sage: cm.explain(QQ, int)
            Coercion on right operand via
                Native morphism:
                  From: Set of Python objects of class 'int'
                  To:   Rational Field
            Arithmetic performed after coercions.
            Result lives in Rational Field
            Rational Field

            sage: R = ZZ['x']
            sage: cm.explain(R, QQ)
            Action discovered.
                Right scalar multiplication by Rational Field
                 on Univariate Polynomial Ring in x over Integer Ring
            Result lives in Univariate Polynomial Ring in x over Rational Field
            Univariate Polynomial Ring in x over Rational Field

            sage: cm.explain(ZZ['x'], QQ, operator.add)
            Coercion on left operand via
                Ring morphism:
                  From: Univariate Polynomial Ring in x over Integer Ring
                  To:   Univariate Polynomial Ring in x over Rational Field
                  Defn: Induced from base ring by
                        Natural morphism:
                          From: Integer Ring
                          To:   Rational Field
            Coercion on right operand via
                Polynomial base injection morphism:
                  From: Rational Field
                  To:   Univariate Polynomial Ring in x over Rational Field
            Arithmetic performed after coercions.
            Result lives in Univariate Polynomial Ring in x over Rational Field
            Univariate Polynomial Ring in x over Rational Field

        Sometimes with non-sage types there is not enough information to deduce
        what will actually happen::

            sage: R100 = RealField(100)                                                 # needs sage.rings.real_mpfr
            sage: cm.explain(R100, float, operator.add)                                 # needs sage.rings.real_mpfr
            Right operand is numeric, will attempt coercion in both directions.
            Unknown result parent.
            sage: parent(R100(1) + float(1))                                            # needs sage.rings.real_mpfr
            <class 'float'>
            sage: cm.explain(QQ, float, operator.add)
            Right operand is numeric, will attempt coercion in both directions.
            Unknown result parent.
            sage: parent(QQ(1) + float(1))
            <class 'float'>

        Special care is taken to deal with division::

            sage: cm.explain(ZZ, ZZ, operator.truediv)
            Identical parents, arithmetic performed immediately.
            Result lives in Rational Field
            Rational Field

            sage: ZZx = ZZ['x']
            sage: QQx = QQ['x']
            sage: cm.explain(ZZx, QQx, operator.truediv)
            Coercion on left operand via
                Ring morphism:
                  From: Univariate Polynomial Ring in x over Integer Ring
                  To:   Univariate Polynomial Ring in x over Rational Field
                  Defn: Induced from base ring by
                        Natural morphism:
                          From: Integer Ring
                          To:   Rational Field
            Arithmetic performed after coercions.
            Result lives in Fraction Field of Univariate Polynomial Ring in x over Rational Field
            Fraction Field of Univariate Polynomial Ring in x over Rational Field

            sage: cm.explain(int, ZZ, operator.truediv)
            Coercion on left operand via
                Native morphism:
                  From: Set of Python objects of class 'int'
                  To:   Integer Ring
            Arithmetic performed after coercions.
            Result lives in Rational Field
            Rational Field

            sage: cm.explain(ZZx, ZZ, operator.truediv)
            Action discovered.
                Right inverse action by Rational Field
                 on Univariate Polynomial Ring in x over Integer Ring
                with precomposition on right by Natural morphism:
                  From: Integer Ring
                  To:   Rational Field
            Result lives in Univariate Polynomial Ring in x over Rational Field
            Univariate Polynomial Ring in x over Rational Field

        .. NOTE::

           This function is accurate only in so far as :meth:`analyse` is kept
           in sync with the :meth:`bin_op` and
           :meth:`canonical_coercion` which are kept separate for
           maximal efficiency."""
    
    @overload
    def get_action[_RP: Parent, _SP: Parent](
            self, R: _RP, S: _SP, 
            op: Callable[[Any, Any], Any], 
            r: Element[_RP] | None = None, 
            s: Element[_SP] | None = None
        ) -> Action[_RP, _SP] | None:
        ...
    @overload
    def get_action[_RP: Parent, _S](
            self, R: _RP, S: type[_S], 
            op: Callable[[Any, Any], Any], 
            r: Element[_RP] | None = None, 
            s: _S | None = None
        ) -> Action[_RP, _S] | None:
        ...
    @overload
    def get_action[_R, _SP: Parent](
            self, R: type[_R], S: _SP, 
            op: Callable[[Any, Any], Any], 
            r: _R | None = None, 
            s: Element[_SP] | None = None
        ) -> Action[_R, _SP] | None:
        ...
    @overload
    def get_action[_R, _S](
            self, R: type[_R], S: type[_S], 
            op: Callable[[Any, Any], Any], 
            r: _R | None = None, 
            s: _S | None = None) -> Action[_R, _S] | None:
        """
        Get the action of R on S or S on R associated to the operation op.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: ZZx = ZZ['x']
            sage: cm.get_action(ZZx, ZZ, operator.mul)
            Right scalar multiplication by Integer Ring
             on Univariate Polynomial Ring in x over Integer Ring
            sage: cm.get_action(ZZx, QQ, operator.mul)
            Right scalar multiplication by Rational Field
             on Univariate Polynomial Ring in x over Integer Ring
            sage: QQx = QQ['x']
            sage: cm.get_action(QQx, int, operator.mul)
            Right scalar multiplication by Integer Ring
             on Univariate Polynomial Ring in x over Rational Field
            with precomposition on right by Native morphism:
              From: Set of Python objects of class 'int'
              To:   Integer Ring

            sage: A = cm.get_action(QQx, ZZ, operator.truediv); A
            Right inverse action by Rational Field
             on Univariate Polynomial Ring in x over Rational Field
            with precomposition on right by Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: x = QQx.gen()
            sage: A(x+10, 5)
            1/5*x + 2"""
    def get_cache(self) -> tuple[_CoercionMap, _ActionMap]:
        """
        This returns the current cache of coercion maps and actions, primarily
        useful for debugging and introspection.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.canonical_coercion(1, 2/3)
            (1, 2/3)
            sage: maps, actions = cm.get_cache()

        Now let us see what happens when we do a binary operations with
        an integer and a rational::

            sage: left_morphism_ref, right_morphism_ref = maps[ZZ, QQ]

        Note that by :issue:`14058` the coercion model only stores a weak
        reference to the coercion maps in this case::

            sage: left_morphism_ref
            <weakref at ...; to 'sage.rings.rational.Z_to_Q' at ...>

        Moreover, the weakly referenced coercion map uses only a weak
        reference to the codomain::

            sage: left_morphism_ref()
            (map internal to coercion system -- copy before use)
            Natural morphism:
              From: Integer Ring
              To:   Rational Field

        To get an actual valid map, we simply copy the weakly referenced
        coercion map::

            sage: print(copy(left_morphism_ref()))
            Natural morphism:
              From: Integer Ring
              To:   Rational Field
            sage: print(right_morphism_ref)
            None

        We can see that it coerces the left operand from an integer to a
        rational, and doesn't do anything to the right.

        Now for some actions::

            sage: R.<x> = ZZ['x']
            sage: 1/2 * x
            1/2*x
            sage: maps, actions = cm.get_cache()
            sage: act = actions[QQ, R, operator.mul]; act
            Left scalar multiplication by Rational Field
             on Univariate Polynomial Ring in x over Integer Ring
            sage: act.actor()
            Rational Field
            sage: act.domain()
            Univariate Polynomial Ring in x over Integer Ring
            sage: act.codomain()
            Univariate Polynomial Ring in x over Rational Field
            sage: act(1/5, x+10)
            1/5*x + 2"""
    def record_exceptions(self, value: bool = True) -> None:
        '''
        Enables (or disables) recording of the exceptions suppressed during
        arithmetic.

        Each time that record_exceptions is called (either enabling or disabling
        the record), the exception_stack is cleared.

        TESTS::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.record_exceptions()
            sage: cm._test_exception_stack()
            sage: cm.exception_stack()
            [\'Traceback (most recent call last):\\n  File "...coerce.pyx", line ...TypeError: just a test\']
            sage: cm.record_exceptions(False)
            sage: cm._test_exception_stack()
            sage: cm.exception_stack()
            []'''
    def reset_cache(self) -> None:
        """
        Clear the coercion cache.

        This should have no impact on the result of arithmetic operations, as
        the exact same coercions and actions will be re-discovered when needed.

        It may be useful for debugging, and may also free some memory.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: len(cm.get_cache()[0])    # random
            42
            sage: cm.reset_cache()
            sage: cm.get_cache()
            ({}, {})"""
    def richcmp(self, x: object, y: object, op: int) -> bool:
        '''
        Given two arbitrary objects ``x`` and ``y``, coerce them to
        a common parent and compare them using rich comparison operator
        ``op``.

        EXAMPLES::

            sage: from sage.structure.element import get_coercion_model
            sage: from sage.structure.richcmp import op_LT, op_LE, op_EQ, op_NE, op_GT, op_GE
            sage: richcmp = get_coercion_model().richcmp
            sage: richcmp(None, None, op_EQ)
            True
            sage: richcmp(None, 1, op_LT)
            True
            sage: richcmp("hello", None, op_LE)
            False
            sage: richcmp(-1, 1, op_GE)
            False
            sage: richcmp(int(1), float(2), op_GE)
            False

        If there is no coercion, we only support ``==`` and ``!=``::

            sage: x = QQ.one(); y = GF(2).one()
            sage: richcmp(x, y, op_EQ)
            False
            sage: richcmp(x, y, op_NE)
            True
            sage: richcmp(x, y, op_GT)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for >:
            \'Rational Field\' and \'Finite Field of size 2\'

        We support non-Sage types with the usual Python convention::

            sage: class AlwaysEqual():
            ....:     def __eq__(self, other):
            ....:         return True
            sage: x = AlwaysEqual()
            sage: x == 1
            True
            sage: 1 == x
            True'''
    @overload
    def verify_action[_RP: Parent, _SP: Parent](
            self, action: Action[_RP,_SP], R: _RP, S: _SP, 
            op: Callable[[Any, Any], Any], 
            r: Element[_RP] | None = None, 
            s: Element[_SP] | None = None,
            fix: bool = True
        ) -> Action[_RP, _SP] | None:
        ...
    @overload
    def verify_action[_RP: Parent, _S](
            self, action: Action[_RP,_S], R: _RP, S: type[_S], 
            op: Callable[[Any, Any], Any], 
            r: Element[_RP] | None = None, 
            s: _S | None = None,
            fix: bool = True
        ) -> Action[_RP, _S] | None:
        ...
    @overload
    def verify_action[_R, _SP: Parent](
            self, action: Action[_R,_SP], R: type[_R], S: _SP, 
            op: Callable[[Any, Any], Any], 
            r: _R | None = None, 
            s: Element[_SP] | None = None,
            fix: bool = True
        ) -> Action[_R, _SP] | None:
        ...
    @overload
    def verify_action[_R, _S](
            self, action: Action[_R,_S], R: type[_R], S: type[_S], 
            op: Callable[[Any, Any], Any], 
            r: _R | None = None, 
            s: _S | None = None,
            fix: bool = True
        ) -> Action[_R, _S] | None:
        """
        Verify that ``action`` takes an element of R on the left and S
        on the right, raising an error if not.

        This is used for consistency checking in the coercion model.

        EXAMPLES::

            sage: R.<x> = ZZ['x']
            sage: cm = sage.structure.element.get_coercion_model()
            sage: cm.verify_action(R.get_action(QQ), R, QQ, operator.mul)
            Right scalar multiplication by Rational Field
             on Univariate Polynomial Ring in x over Integer Ring
            sage: cm.verify_action(R.get_action(QQ), RDF, R, operator.mul)
            Traceback (most recent call last):
            ...
            RuntimeError: There is a BUG in the coercion model:
                Action found for R <built-in function mul> S does not have the correct domains
                R = Real Double Field
                S = Univariate Polynomial Ring in x over Integer Ring
                (should be Univariate Polynomial Ring in x over Integer Ring, Rational Field)
                action = Right scalar multiplication by Rational Field
                         on Univariate Polynomial Ring in x over Integer Ring
                (<class 'sage.structure.coerce_actions.RightModuleAction'>)"""
    def verify_coercion_maps(
        self, R: SageObject|type, S: SageObject|type, 
        homs: tuple[Map|None, Map| None], fix: bool = False
    ) -> tuple[Map | None, Map | None] | None:
        """
        Make sure this is a valid pair of homomorphisms from `R` and `S` to a common parent.
        This function is used to protect the user against buggy parents.

        EXAMPLES::

            sage: cm = sage.structure.element.get_coercion_model()
            sage: homs = QQ.coerce_map_from(ZZ), None
            sage: cm.verify_coercion_maps(ZZ, QQ, homs) == homs
            True
            sage: homs = QQ.coerce_map_from(ZZ), RR.coerce_map_from(QQ)
            sage: cm.verify_coercion_maps(ZZ, QQ, homs) == homs
            Traceback (most recent call last):
            ...
            RuntimeError: ('BUG in coercion model, codomains must be identical',
            Natural morphism:
              From: Integer Ring
              To:   Rational Field,
            Generic map:
              From: Rational Field
              To:   Real Field with 53 bits of precision)"""
        ...

Coercion_model: CoercionModel
