"""
Symbolic Expressions

RELATIONAL EXPRESSIONS:

We create a relational expression::

    sage: x = var('x')
    sage: eqn = (x-1)^2 <= x^2 - 2*x + 3
    sage: eqn.subs(x == 5)
    16 <= 18

Notice that squaring the relation squares both sides.

::

    sage: eqn^2
    (x - 1)^4 <= (x^2 - 2*x + 3)^2
    sage: eqn.expand()
    x^2 - 2*x + 1 <= x^2 - 2*x + 3

This can transform a true relation into a false one::

    sage: eqn = SR(-5) < SR(-3); eqn
    -5 < -3
    sage: bool(eqn)
    True
    sage: eqn^2
    25 < 9
    sage: bool(eqn^2)
    False

We can do arithmetic with relations::

    sage: e = x+1 <= x-2
    sage: e + 2
    x + 3 <= x
    sage: e - 1
    x <= x - 3
    sage: e*(-1)
    -x - 1 <= -x + 2
    sage: (-2)*e
    -2*x - 2 <= -2*x + 4
    sage: e*5
    5*x + 5 <= 5*x - 10
    sage: e/5
    1/5*x + 1/5 <= 1/5*x - 2/5
    sage: 5/e
    5/(x + 1) <= 5/(x - 2)
    sage: e/(-2)
    -1/2*x - 1/2 <= -1/2*x + 1
    sage: -2/e
    -2/(x + 1) <= -2/(x - 2)

We can even add together two relations, as long as the operators are
the same::

    sage: (x^3 + x <= x - 17)  + (-x <= x - 10)
    x^3 <= 2*x - 27

Here they are not::

    sage: (x^3 + x <= x - 17)  + (-x >= x - 10)
    Traceback (most recent call last):
    ...
    TypeError: incompatible relations


ARBITRARY SAGE ELEMENTS:

You can work symbolically with any Sage data type.  This can lead to
nonsense if the data type is strange, e.g., an element of a finite
field (at present).

We mix Singular variables with symbolic variables::

    sage: R.<u,v> = QQ[]
    sage: var('a,b,c')
    (a, b, c)
    sage: expand((u + v + a + b + c)^2)
    a^2 + 2*a*b + b^2 + 2*a*c + 2*b*c + c^2 + 2*a*u + 2*b*u + 2*c*u + u^2 + 2*a*v + 2*b*v + 2*c*v + 2*u*v + v^2

TESTS:

Test Jacobian on Pynac expressions. (:issue:`5546`) ::

    sage: var('x,y')
    (x, y)
    sage: f = x + y
    sage: jacobian(f, [x,y])
    [1 1]

Test if matrices work (:issue:`5546`) ::

    sage: var('x,y,z')
    (x, y, z)
    sage: M = matrix(2,2,[x,y,z,x])
    sage: v = vector([x,y])
    sage: M * v
    (x^2 + y^2, x*y + x*z)
    sage: v*M
    (x^2 + y*z, 2*x*y)

Test if comparison bugs from :issue:`6256` are fixed::

    sage: t = exp(sqrt(x)); u = 1/t
    sage: t*u
    1
    sage: t + u
    e^(-sqrt(x)) + e^sqrt(x)
    sage: t
    e^sqrt(x)

Test if :issue:`9947` is fixed::

    sage: r = real_part(1+2*(sqrt(2)+1)*(sqrt(2)-1)); r
    2*(sqrt(2) + 1)*(sqrt(2) - 1) + 1
    sage: r.expand()
    3
    sage: a = (sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5)
    sage: a.real_part()
    4*sqrt(3)/(sqrt(3) + 5)
    sage: a.imag_part()
    2*sqrt(10)/(sqrt(3) + 5)

Check the fix for :issue:`25251` and :issue:`25252`::

    sage: e1 = sqrt(2)*I - sqrt(2) - 2
    sage: e2 = sqrt(2)
    sage: e1 * e2
    sqrt(2)*((I - 1)*sqrt(2) - 2)
    sage: (1 + exp(I*pi/4)) * exp(I*pi/4)
    -(1/4*I + 1/4)*sqrt(2)*(-(I + 1)*sqrt(2) - 2)

Test if :issue:`24883` is fixed::

    sage: a = exp(I*pi/4) + 1
    sage: b = 1 - exp(I*pi/4)
    sage: a*b
    1/4*((I + 1)*sqrt(2) - 2)*(-(I + 1)*sqrt(2) - 2)

Test that :issue:`20784` is fixed (equations should stay unevaluated)::

    sage: limit(1/x, x=0) == unsigned_infinity
    Infinity == Infinity
    sage: SR(unsigned_infinity) == unsigned_infinity
    Infinity == Infinity

Many tests about comparison.

Use :func:`sage.symbolic.expression.mixed_order` instead of
the operators ``<=``, ``<``, etc. to compare symbolic expressions when
you do not want to get a formal inequality::

    sage: from sage.symbolic.expression import mixed_order

    sage: a = sqrt(3)
    sage: b = x^2+1
    sage: mixed_order(a, b)   # indirect doctest
    -1

    sage: x,y = var('x,y')
    sage: x < y
    x < y
    sage: mixed_order(x, y)
    1

    sage: mixed_order(SR(0.5), SR(0.7))
    -1
    sage: SR(0.5) < SR(0.7)
    0.500000000000000 < 0.700000000000000
    sage: mixed_order(SR(0.5), 0.7)
    -1

    sage: mixed_order(sin(SR(2)), sin(SR(1)))
    1
    sage: float(sin(SR(2)))
    0.9092974268256817
    sage: float(sin(SR(1)))
    0.8414709848078965

Check that :issue:`9880` is fixed::

    sage: b = [var('b_%s'%i) for i in range(4)]
    sage: precomp = (2^b_2 + 2)*(2^b_1 + 2^(-b_1) + 2^b_1*2^b_0 - \
    ....:       2^b_1*2^(-b_0) - 2^(-b_1)*2^b_0 - 2^(-b_1)*2^(-b_0) + \
    ....:       2^b_0 + 2^(-b_0) - 9) + (2^b_1 + 2^(-b_1) + \
    ....:       2^b_1*2^b_0 - 2^b_1*2^(-b_0) - 2^(-b_1)*2^b_0 - \
    ....:        2^(-b_1)*2^(-b_0) + 2^b_0 + 2^(-b_0) - 9)/2^b_2
    sage: repl_dict = {b_0: b_0, b_3: b_1, b_2: b_3, b_1: b_2}
    sage: P = precomp.substitute(repl_dict)
    sage: P.expand()
    2^b_0*2^b_2*2^b_3 + 2*2^b_0*2^b_2 + 2^b_0*2^b_3 + 2^b_2*2^b_3 +
    2*2^b_0 + 2*2^b_2 - 9*2^b_3 + 2^b_0*2^b_2/2^b_3 -
    2^b_0*2^b_3/2^b_2 - 2^b_2*2^b_3/2^b_0 - 2*2^b_0/2^b_2 -
    2*2^b_2/2^b_0 + 2^b_0/2^b_3 + 2^b_2/2^b_3 + 2^b_3/2^b_0 +
    2^b_3/2^b_2 + 2/2^b_0 + 2/2^b_2 - 2^b_0/(2^b_2*2^b_3) -
    2^b_2/(2^b_0*2^b_3) - 9/2^b_3 - 2^b_3/(2^b_0*2^b_2) -
    2/(2^b_0*2^b_2) + 1/(2^b_0*2^b_3) + 1/(2^b_2*2^b_3) -
    1/(2^b_0*2^b_2*2^b_3) - 18

    sage: _0,b_1,b_2=var('b_0,b_1,b_2')
    sage: f = 1/27*b_2^2/(2^b_2)^2 + 1/27*b_1^2/(2^b_1)^2 + \
    ....: 1/27*b_0^2/(2^b_0)^2 + 1/27*b_2/(2^b_2)^2 - 2/81/(2^b_2)^2 + \
    ....: 1/27*b_1/(2^b_1)^2 + 8/243/(2^b_2)^2 - 1/81*b_0/(2^b_0)^2 - \
    ....: 1/27*b_1^2/((2^b_2)^2*(2^b_1)^2) - \
    ....: 1/27*b_0^2/((2^b_2)^2*(2^b_0)^2) - 20/243/(2^b_1)^2 + 1/9/2^b_0 \
    ....: + 4/81*b_0/(2^b_0)^2 - 8/243/(2^b_2)^2 - 2/9/(2^b_2*2^b_1) - \
    ....: 2/9/(2^b_2*2^b_0) + 8/243/(2^b_1)^2 - 1/9/2^b_0 + \
    ....: 2/9/(2^b_2*2^b_1) + 2/9/(2^b_2*2^b_0) - \
    ....: 2/27*b_1*b_2/((2^b_2)^2*(2^b_1)^2) - \
    ....: 1/27*b_2^2/((2^b_2)^2*(2^b_1)^2) - \
    ....: 2/27*b_0*b_2/((2^b_2)^2*(2^b_0)^2) - \
    ....: 1/27*b_2^2/((2^b_2)^2*(2^b_0)^2) + 2/81/(2^b_1)^2 - \
    ....: 1/27*b_0^2/((2^b_1)^2*(2^b_0)^2) - \
    ....: 2/27*b_0*b_1/((2^b_1)^2*(2^b_0)^2) - \
    ....: 1/27*b_1^2/((2^b_1)^2*(2^b_0)^2) - 2/81/(2^b_0)^2 + \
    ....: 5/27*b_1/((2^b_2)^2*(2^b_1)^2) + 5/27*b_2/((2^b_2)^2*(2^b_1)^2) \
    ....: + 5/27*b_0/((2^b_2)^2*(2^b_0)^2) + \
    ....: 5/27*b_2/((2^b_2)^2*(2^b_0)^2) + 5/27*b_0/((2^b_1)^2*(2^b_0)^2) \
    ....: + 5/27*b_1/((2^b_1)^2*(2^b_0)^2) - 4/81/((2^b_2)^2*(2^b_1)^2) + \
    ....: 1/27*b_0^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + \
    ....: 2/27*b_0*b_1/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + \
    ....: 2/27*b_0*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + \
    ....: 1/27*b_1^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + \
    ....: 2/27*b_1*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + \
    ....: 1/27*b_2^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - \
    ....: 4/81/((2^b_2)^2*(2^b_0)^2) - 4/81/((2^b_1)^2*(2^b_0)^2) - \
    ....: 11/27*b_0/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - \
    ....: 11/27*b_1/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - \
    ....: 11/27*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + \
    ....: 64/81/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 35/81
    sage: f.nops()
    38

    sage: x,y,z = var('x y z')
    sage: print((-x+z)*(3*x-3*z))
    -3*(x - z)^2

    sage: t = var('t')
    sage: (x-t)^3
    -(t - x)^3
    sage: (-t+x)^3
    -(t - x)^3
    sage: (-x+t)^3
    (t - x)^3

This example is from :issue:`10833`::

    sage: R.<x,c> = PolynomialRing(QQ,2)
    sage: phi(x) = x^2 + c
    sage: def iterkate(n):
    ....:     pol = x
    ....:     for i in range(1,n):
    ....:         pol = phi(pol)
    ....:     return pol
    ....:
    sage: g = expand(iterkate(7))
    sage: g.nops()
    480

Check if :issue:`10849` is fixed::

    sage: t = I.parent()(-1/2)
    sage: t > 0
    False
    sage: t = I*x-1/2; t
    I*x - 1/2
    sage: t.subs(x=I*x).subs(x=0).is_positive()
    False

Check if :issue:`16397` is fixed:

    sage: mixed_order(1, sqrt(2))
    -1
    sage: mixed_order(SR(1), sqrt(2))
    -1
    sage: mixed_order(log(8), 3*log(2))
    0
    sage: bool(RLF(1) < RLF(sqrt(2)))
    True
    sage: RealSet((0, pi),[pi, pi],(pi,4))
    (0, 4)
    sage: RealSet((0, pi),[0, pi],(pi,4))
    [0, 4)
    sage: RealSet((0, pi),[0, 3.5],(pi,4))
    [0, 4)

More sanity tests::

    sage: bool(pi < pi)
    False
    sage: bool(e < e)
    False
    sage: bool(sqrt(2) < sqrt(2))
    False
    sage: bool(pi < SR.zero())
    False
"""

from typing import Annotated, Any, Literal, Protocol, Self, SupportsInt, overload
from collections.abc import Callable, Iterable, Sequence
from typings_sagemath import (
    ConvertibleToExpression, 
    ConvertibleToInteger,
    ConvertibleToRealNumber,
    ConvertibleToComplexNumber, 
    CoercibleToExpression, 
    SupportsExp,
    SupportsGamma,
)
from sage.structure.sage_object import SageObject
from sage.structure.parent import Parent
from sage.rings.abc import SymbolicRing as SymbolicRingABC
from sage.symbolic.ring import SymbolicRing
from sage.symbolic.operators import FDerivativeOperator
from sage.symbolic.function import SymbolicFunction
from sage.symbolic.maxima_wrapper import MaximaWrapper
from sage.rings.integer import Integer
from sage.rings.real_mpfr import RealNumber
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.ring import Ring
from sage.rings.fraction_field_element import FractionFieldElement
from sage.rings.power_series_ring_element import PowerSeries

from sage.rings.power_series_poly import PowerSeries_poly

type _uint = SupportsInt
type _NotUsed = object
type _Domain = Literal["real", "complex", "positive", "integer", "noninteger"]
class _VarArgOp(Protocol):
    def __call__(self, *args): ...
type _Operator = ( # c.f. the implementation of `Expression.operator`
    _VarArgOp | Callable[[Any, Any], Any] | Callable[[Any], Any]
    | FDerivativeOperator | SymbolicFunction | type[tuple] 
)

import sage as sage
import sage.libs.mpmath.utils as mpmath_utils
import sage.structure.element
import sage.structure.sage_object
from _typeshed import Incomplete
from sage.arith.functions import lcm as lcm
from sage.arith.misc import bernoulli as bernoulli, factorial as factorial, gcd as gcd, is_prime as is_prime
from sage.arith.numerical_approx import digits_to_bits as digits_to_bits
from sage.categories.category import RR as RR, ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.decorators import sage_wraps as sage_wraps
from sage.misc.derivative import multi_derivative as multi_derivative
from sage.misc.latex import latex_variable_name as latex_variable_name
from sage.misc.persist import dumps as dumps, loads as loads
from sage.rings.complex_mpfr import CC as CC
from sage.rings.infinity import AnInfinity as AnInfinity, PlusInfinity, infinity as infinity, minus_infinity as minus_infinity, unsigned_infinity as unsigned_infinity
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.dynamic_class import dynamic_class as dynamic_class
from sage.structure.element import Matrix, Vector, have_same_parent as have_same_parent, parent as parent
from sage.symbolic.complexity_measures import string_length as string_length
from sage.symbolic.symbols import register_symbol as register_symbol

def unpack_operands(ex: Expression) -> tuple[Expression[SymbolicRing], ...]:
    """
    EXAMPLES::

        sage: from sage.symbolic.expression import unpack_operands
        sage: t = SR._force_pyobject((1, 2, x, x+1, x+2))
        sage: unpack_operands(t)
        (1, 2, x, x + 1, x + 2)
        sage: type(unpack_operands(t))
        <... 'tuple'>
        sage: list(map(type, unpack_operands(t)))
        [<class 'sage.rings.integer.Integer'>, <class 'sage.rings.integer.Integer'>, <class 'sage.symbolic.expression.Expression'>, <class 'sage.symbolic.expression.Expression'>, <class 'sage.symbolic.expression.Expression'>]
        sage: u = SR._force_pyobject((t, x^2))
        sage: unpack_operands(u)
        ((1, 2, x, x + 1, x + 2), x^2)
        sage: type(unpack_operands(u)[0])
        <... 'tuple'>
    """
# TODO: this causes SIGSEGV if improper expression passed
def paramset_from_Expression(e: Expression) -> list:
    """
    EXAMPLES::

        sage: from sage.symbolic.expression import paramset_from_Expression
        sage: f = function('f')
        sage: paramset_from_Expression(f(x).diff(x))
        [0]
    """
def get_ginac_serial() -> int:
    """
    Number of C++ level functions defined by GiNaC. (Defined mainly for testing.)

    EXAMPLES::

        sage: sage.symbolic.expression.get_ginac_serial() >= 35
        True
    """
def get_fn_serial() -> int:
    """
    Return the overall size of the Pynac function registry which
    corresponds to the last serial value plus one.

    EXAMPLES::

        sage: from sage.symbolic.expression import get_fn_serial, get_sfunction_from_serial
        sage: get_fn_serial() > 125
        True
        sage: print(get_sfunction_from_serial(get_fn_serial()))
        None
        sage: get_sfunction_from_serial(get_fn_serial() - 1) is not None
        True
    """
def py_print_function_pystring(
    id: SupportsInt, args: Iterable[object], fname_paren: bool = False) -> str:
    """
    Return a string with the representation of the symbolic function specified
    by the given id applied to args.

    INPUT:

    - ``id`` -- serial number of the corresponding symbolic function
    - ``params`` -- set of parameter numbers with respect to which to take the
      derivative
    - ``args`` -- arguments of the function

    EXAMPLES::

        sage: from sage.symbolic.expression import py_print_function_pystring, get_ginac_serial, get_fn_serial, get_sfunction_from_serial
        sage: var('x,y,z')
        (x, y, z)
        sage: foo = function('foo', nargs=2)
        sage: for i in range(get_ginac_serial(), get_fn_serial()):
        ....:   if get_sfunction_from_serial(i) == foo: break

        sage: get_sfunction_from_serial(i) == foo
        True
        sage: py_print_function_pystring(i, (x,y))
        'foo(x, y)'
        sage: py_print_function_pystring(i, (x,y), True)
        '(foo)(x, y)'
        sage: def my_print(self, *args): return "my args are: " + ', '.join(map(repr, args))
        sage: foo = function('foo', nargs=2, print_func=my_print)
        sage: for i in range(get_ginac_serial(), get_fn_serial()):
        ....:   if get_sfunction_from_serial(i) == foo: break

        sage: get_sfunction_from_serial(i) == foo
        True
        sage: py_print_function_pystring(i, (x,y))
        'my args are: x, y'
    """
def py_latex_function_pystring(
    id: SupportsInt, args: Iterable[object], fname_paren: bool = False) -> str:
    r"""
    Return a string with the latex representation of the symbolic function
    specified by the given id applied to args.

    See documentation of py_print_function_pystring for more information.

    EXAMPLES::

        sage: from sage.symbolic.expression import py_latex_function_pystring, get_ginac_serial, get_fn_serial, get_sfunction_from_serial
        sage: var('x,y,z')
        (x, y, z)
        sage: foo = function('foo', nargs=2)
        sage: for i in range(get_ginac_serial(), get_fn_serial()):
        ....:   if get_sfunction_from_serial(i) == foo: break

        sage: get_sfunction_from_serial(i) == foo
        True
        sage: py_latex_function_pystring(i, (x,y^z))
        '{\\rm foo}\\left(x, y^{z}\\right)'
        sage: py_latex_function_pystring(i, (x,y^z), True)
        '\\left({\\rm foo}\\right)\\left(x, y^{z}\\right)'
        sage: py_latex_function_pystring(i, (int(0),x))
        '{\\rm foo}\\left(0, x\\right)'

    Test latex_name::

        sage: foo = function('foo', nargs=2, latex_name=r'\mathrm{bar}')
        sage: for i in range(get_ginac_serial(), get_fn_serial()):
        ....:   if get_sfunction_from_serial(i) == foo: break

        sage: get_sfunction_from_serial(i) == foo
        True
        sage: py_latex_function_pystring(i, (x,y^z))
        '\\mathrm{bar}\\left(x, y^{z}\\right)'

    Test custom func::

        sage: def my_print(self, *args): return "my args are: " + ', '.join(map(repr, args))
        sage: foo = function('foo', nargs=2, print_latex_func=my_print)
        sage: for i in range(get_ginac_serial(), get_fn_serial()):
        ....:   if get_sfunction_from_serial(i) == foo: break

        sage: get_sfunction_from_serial(i) == foo
        True
        sage: py_latex_function_pystring(i, (x,y^z))
        'my args are: x, y^z'
    """
def tolerant_is_symbol(a: object) -> bool:
    """
    Utility function to test if something is a symbol.

    Returns False for arguments that do not have an is_symbol attribute.
    Returns the result of calling the is_symbol method otherwise.

    EXAMPLES::

        sage: from sage.symbolic.expression import tolerant_is_symbol
        sage: tolerant_is_symbol(var("x"))
        True
        sage: tolerant_is_symbol(None)
        False
        sage: None.is_symbol()
        Traceback (most recent call last):
        ...
        AttributeError: 'NoneType' object has no attribute 'is_symbol'...
    """
def test_binomial(n: SupportsInt, k: SupportsInt) -> Integer:
    """
    The Binomial coefficients.  It computes the binomial coefficients.  For
    integer n and k and positive n this is the number of ways of choosing k
    objects from n distinct objects.  If n is negative, the formula
    binomial(n,k) == (-1)^k*binomial(k-n-1,k) is used to compute the result.

    INPUT:

    - ``n``, ``k`` -- integers, with ``k >= 0``

    OUTPUT: integer

    EXAMPLES::

        sage: import sage.symbolic.expression
        sage: sage.symbolic.expression.test_binomial(5,2)
        10
        sage: sage.symbolic.expression.test_binomial(-5,3)
        -35
        sage: -sage.symbolic.expression.test_binomial(3-(-5)-1, 3)
        -35
    """
@overload
def py_factorial_py(x: ConvertibleToInteger) -> Integer | float: ...
@overload
def py_factorial_py(x: float) -> float: ... # pyright: ignore[reportOverlappingOverload]
@overload
def py_factorial_py[T: ConvertibleToRealNumber](x: SupportsGamma[T]) -> RealNumber: ...
@overload
def py_factorial_py[T: ConvertibleToComplexNumber](
    x: SupportsGamma[T] | T
) -> ComplexNumber | PlusInfinity:
    """
    This function is a python wrapper around py_factorial(). This wrapper
    is needed when we override the eval() method for GiNaC's factorial
    function in sage.functions.other.Function_factorial.

    TESTS::

        sage: from sage.symbolic.expression import py_factorial_py
        sage: py_factorial_py(3)
        6
    """
def doublefactorial(n: ConvertibleToInteger) -> Integer:
    """
    The double factorial combinatorial function:

        n!! == n * (n-2) * (n-4) * ... * ({1|2}) with 0!! == (-1)!! == 1.

    INPUT:

    - ``n`` -- integer ``>= 1``

    EXAMPLES::

        sage: from sage.symbolic.expression import doublefactorial
        sage: doublefactorial(-1)
        1
        sage: doublefactorial(0)
        1
        sage: doublefactorial(1)
        1
        sage: doublefactorial(5)
        15
        sage: doublefactorial(20)
        3715891200
        sage: prod( [20,18,..,2] )
        3715891200
    """
def init_pynac_I() -> Expression[SymbolicRing]:
    """
    Initialize the numeric ``I`` object in pynac. We use the generator of ``QQ(i)``.

    EXAMPLES::

        sage: from sage.symbolic.constants import I as symbolic_I
        sage: symbolic_I
        I
        sage: symbolic_I^2
        -1

    Note that conversions to real fields will give :exc:`TypeError`::

        sage: float(symbolic_I)
        Traceback (most recent call last):
        ...
        TypeError: unable to simplify to float approximation
        sage: gp(symbolic_I)
        I
        sage: RR(symbolic_I)
        Traceback (most recent call last):
        ...
        TypeError: unable to convert '1.00000000000000*I' to a real number

    We can convert to complex fields::

        sage: C = ComplexField(200); C
        Complex Field with 200 bits of precision
        sage: C(symbolic_I)
        1.0000000000000000000000000000000000000000000000000000000000*I
        sage: symbolic_I._complex_mpfr_field_(ComplexField(53))
        1.00000000000000*I

        sage: symbolic_I._complex_double_(CDF)
        1.0*I
        sage: CDF(symbolic_I)
        1.0*I

        sage: z = symbolic_I + symbolic_I; z
        2*I
        sage: C(z)
        2.0000000000000000000000000000000000000000000000000000000000*I
        sage: 1e8*symbolic_I
        1.00000000000000e8*I

        sage: complex(symbolic_I)
        1j

        sage: QQbar(symbolic_I)
        I

        sage: abs(symbolic_I)
        1

        sage: symbolic_I.minpoly()
        x^2 + 1
        sage: maxima(2*symbolic_I)
        2*%i

    TESTS::

        sage: repr(symbolic_I)
        'I'
        sage: latex(symbolic_I)
        i

        sage: I = sage.symbolic.expression.init_pynac_I()
        sage: type(I)
        <class 'sage.symbolic.expression.Expression'>
        sage: type(I.pyobject())
        <class 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_gaussian'>

    Check that :issue:`10064` is fixed::

        sage: y = symbolic_I*symbolic_I*x / x  # so y is the expression -1
        sage: y.is_positive()
        False
        sage: z = -x / x
        sage: z.is_positive()
        False
        sage: bool(z == y)
        True

    Check that :issue:`31869` is fixed::

        sage: x * ((3*I + 4)*x - 5)
        ((3*I + 4)*x - 5)*x
    """
def init_function_table() -> None:
    """
    Initialize the function pointer table in Pynac.  This must be
    called before Pynac is used; otherwise, there will be segfaults.
    """

class Expression[P: SymbolicRingABC](sage.structure.element.Expression[P]):
    def __init__(self, SR: P, x: Any = 0):
        """
                Nearly all expressions are created by calling new_Expression_from_*,
                but we need to make sure this at least does not leave self._gobj
                uninitialized and segfault.

                TESTS::

                    sage: sage.symbolic.expression.Expression(SR)
                    0
                    sage: sage.symbolic.expression.Expression(SR, 5)
                    5

                We test subclassing ``Expression``::

                    sage: from sage.symbolic.expression import Expression
                    sage: class exp_sub(Expression): pass
                    sage: f = function('f')
                    sage: t = f(x)
                    sage: u = exp_sub(SR, t)
                    sage: u.operator()
                    f
        """
    def Order(self, hold: bool = False) -> Expression[P]:
        """
        Return the order of the expression, as in big oh notation.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: n = var('n')
            sage: t = (17*n^3).Order(); t
            Order(n^3)
            sage: t.derivative(n)
            Order(n^2)

        To prevent automatic evaluation use the ``hold`` argument::

            sage: (17*n^3).Order(hold=True)
            Order(17*n^3)"""
    def WZ_certificate(self, n: Expression, k: CoercibleToExpression) -> Expression[P]:
        """
        Return the Wilf-Zeilberger certificate for this hypergeometric
        summand in ``n``, ``k``.

        To prove the identity `\\sum_k F(n,k)=\\textrm{const}` it suffices
        to show that `F(n+1,k)-F(n,k)=G(n,k+1)-G(n,k),` with `G=RF` and
        `R` the WZ certificate.

        EXAMPLES:

        To show that `\\sum_k \\binom{n}{k} = 2^n` do::

            sage: _ = var('k n')
            sage: F(n,k) = binomial(n,k) / 2^n
            sage: c = F(n,k).WZ_certificate(n,k); c
            1/2*k/(k - n - 1)
            sage: G(n,k) = c * F(n,k); G
            (n, k) |--> 1/2*k*binomial(n, k)/(2^n*(k - n - 1))
            sage: (F(n+1,k) - F(n,k) - G(n,k+1) + G(n,k)).simplify_full()
            0"""
    def abs(self, hold: bool = False) -> Expression[P]:
        """
        Return the absolute value of this expression.

        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: (x+y).abs()
            abs(x + y)

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(-5).abs(hold=True)
            abs(-5)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(-5).abs(hold=True); a.unhold()
            5

        TESTS:

        From :issue:`7557`::

            sage: var('y', domain='real')
            y
            sage: abs(exp(1.1*y*I)).simplify()
            1
            sage: var('y', domain='complex') # reset the domain for other tests
            y"""
    def add(self, *args: CoercibleToExpression, hold: bool = False) -> Expression[P]:
        """
        Return the sum of the current expression and the given arguments.

        To prevent automatic evaluation use the ``hold`` argument.

        EXAMPLES::

            sage: x.add(x)
            2*x
            sage: x.add(x, hold=True)
            x + x
            sage: x.add(x, (2+x), hold=True)
            (x + 2) + x + x
            sage: x.add(x, (2+x), x, hold=True)
            (x + 2) + x + x + x
            sage: x.add(x, (2+x), x, 2*x, hold=True)
            (x + 2) + 2*x + x + x + x

        To then evaluate again, we use :meth:`unhold`::

            sage: a = x.add(x, hold=True); a.unhold()
            2*x"""
    def add_to_both_sides(self, x) -> Expression:
        """
        Return a relation obtained by adding ``x`` to both sides of
        this relation.

        EXAMPLES::

            sage: var('x y z')
            (x, y, z)
            sage: eqn = x^2 + y^2 + z^2 <= 1
            sage: eqn.add_to_both_sides(-z^2)
            x^2 + y^2 <= -z^2 + 1
            sage: eqn.add_to_both_sides(I)
            x^2 + y^2 + z^2 + I <= (I + 1)"""
    def arccos(self, hold: bool = False) -> Expression[P]:
        """
        Return the arc cosine of ``self``.

        EXAMPLES::

            sage: x.arccos()
            arccos(x)
            sage: SR(1).arccos()
            0
            sage: SR(1/2).arccos()
            1/3*pi
            sage: SR(0.4).arccos()
            1.15927948072741
            sage: plot(lambda x: SR(x).arccos(), -1,1)                                  # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(1).arccos(hold=True)
            arccos(1)

        This also works using functional notation::

            sage: arccos(1, hold=True)
            arccos(1)
            sage: arccos(1)
            0

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(1).arccos(hold=True); a.unhold()
            0

        TESTS::

            sage: SR(oo).arccos()
            Traceback (most recent call last):
            ...
            RuntimeError: arccos_eval(): arccos(infinity) encountered
            sage: SR(-oo).arccos()
            Traceback (most recent call last):
            ...
            RuntimeError: arccos_eval(): arccos(infinity) encountered
            sage: SR(unsigned_infinity).arccos()
            Infinity"""
    def arccosh(self, hold: bool = False) -> Expression[P]:
        """
        Return the inverse hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: x.arccosh()
            arccosh(x)
            sage: SR(0).arccosh()
            1/2*I*pi
            sage: SR(1/2).arccosh()
            arccosh(1/2)
            sage: SR(CDF(1/2)).arccosh() #  rel tol 1e-15
            1.0471975511965976*I
            sage: z = maxima('acosh(0.5)')
            sage: z.real(), z.imag()  # abs tol 1e-15
            (0.0, 1.047197551196598)

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(-1).arccosh()
            I*pi
            sage: SR(-1).arccosh(hold=True)
            arccosh(-1)

        This also works using functional notation::

            sage: arccosh(-1,hold=True)
            arccosh(-1)
            sage: arccosh(-1)
            I*pi

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(-1).arccosh(hold=True); a.unhold()
            I*pi

        TESTS::

            sage: SR(oo).arccosh()
            +Infinity
            sage: SR(-oo).arccosh()
            +Infinity
            sage: SR(unsigned_infinity).arccosh()
            +Infinity"""
    def arcsin(self, hold: bool = False) -> Expression[P]:
        """
        Return the arcsin of x, i.e., the number y between -pi and pi
        such that sin(y) == x.

        EXAMPLES::

            sage: x.arcsin()
            arcsin(x)
            sage: SR(0.5).arcsin()
            1/6*pi
            sage: SR(0.999).arcsin()
            1.52607123962616
            sage: SR(1/3).arcsin()
            arcsin(1/3)
            sage: SR(-1/3).arcsin()
            -arcsin(1/3)

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(0).arcsin()
            0
            sage: SR(0).arcsin(hold=True)
            arcsin(0)

        This also works using functional notation::

            sage: arcsin(0,hold=True)
            arcsin(0)
            sage: arcsin(0)
            0

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(0).arcsin(hold=True); a.unhold()
            0

        TESTS::

            sage: SR(oo).arcsin()
            Traceback (most recent call last):
            ...
            RuntimeError: arcsin_eval(): arcsin(infinity) encountered
            sage: SR(-oo).arcsin()
            Traceback (most recent call last):
            ...
            RuntimeError: arcsin_eval(): arcsin(infinity) encountered
            sage: SR(unsigned_infinity).arcsin()
            Infinity"""
    def arcsinh(self, hold: bool = False) -> Expression[P]:
        """
        Return the inverse hyperbolic sine of ``self``.

        EXAMPLES::

            sage: x.arcsinh()
            arcsinh(x)
            sage: SR(0).arcsinh()
            0
            sage: SR(1).arcsinh()
            arcsinh(1)
            sage: SR(1.0).arcsinh()
            0.881373587019543
            sage: maxima('asinh(2.0)')
            1.4436354751788...

        Sage automatically applies certain identities::

            sage: SR(3/2).arcsinh().cosh()
            1/2*sqrt(13)

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(-2).arcsinh()
            -arcsinh(2)
            sage: SR(-2).arcsinh(hold=True)
            arcsinh(-2)

        This also works using functional notation::

            sage: arcsinh(-2,hold=True)
            arcsinh(-2)
            sage: arcsinh(-2)
            -arcsinh(2)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(-2).arcsinh(hold=True); a.unhold()
            -arcsinh(2)

        TESTS::

            sage: SR(oo).arcsinh()
            +Infinity
            sage: SR(-oo).arcsinh()
            -Infinity
            sage: SR(unsigned_infinity).arcsinh()
            Infinity"""
    def arctan(self, hold: bool = False) -> Expression[P]:
        """
        Return the arc tangent of ``self``.

        EXAMPLES::

            sage: x = var('x')
            sage: x.arctan()
            arctan(x)
            sage: SR(1).arctan()
            1/4*pi
            sage: SR(1/2).arctan()
            arctan(1/2)
            sage: SR(0.5).arctan()
            0.463647609000806
            sage: plot(lambda x: SR(x).arctan(), -20,20)                                # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(1).arctan(hold=True)
            arctan(1)

        This also works using functional notation::

            sage: arctan(1, hold=True)
            arctan(1)
            sage: arctan(1)
            1/4*pi

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(1).arctan(hold=True); a.unhold()
            1/4*pi

        TESTS::

            sage: SR(oo).arctan()
            1/2*pi
            sage: SR(-oo).arctan()
            -1/2*pi
            sage: SR(unsigned_infinity).arctan()
            Traceback (most recent call last):
            ...
            RuntimeError: arctan_eval(): arctan(unsigned_infinity) encountered"""
    def arctan2(self, x: CoercibleToExpression, hold: bool = False) -> Expression[P]:
        """
        Return the inverse of the 2-variable tan function on ``self`` and ``x``.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: x.arctan2(y)
            arctan2(x, y)
            sage: SR(1/2).arctan2(1/2)
            1/4*pi
            sage: maxima.eval('atan2(1/2,1/2)')
            '%pi/4'

            sage: SR(-0.7).arctan2(SR(-0.6))
            -2.27942259892257

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(1/2).arctan2(1/2, hold=True)
            arctan2(1/2, 1/2)

        This also works using functional notation::

            sage: arctan2(1,2,hold=True)
            arctan2(1, 2)
            sage: arctan2(1,2)
            arctan(1/2)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(1/2).arctan2(1/2, hold=True); a.unhold()
            1/4*pi

        TESTS:

        We compare a bunch of different evaluation points between
        Sage and Maxima::

            sage: float(SR(0.7).arctan2(0.6))
            0.8621700546672264
            sage: maxima('atan2(0.7,0.6)')
            0.862170054667226...
            sage: float(SR(0.7).arctan2(-0.6))
            2.279422598922567
            sage: maxima('atan2(0.7,-0.6)')
            2.279422598922567
            sage: float(SR(-0.7).arctan2(0.6))
            -0.8621700546672264
            sage: maxima('atan2(-0.7,0.6)')
            -0.862170054667226...
            sage: float(SR(-0.7).arctan2(-0.6))
            -2.279422598922567
            sage: maxima('atan2(-0.7,-0.6)')
            -2.279422598922567
            sage: float(SR(0).arctan2(-0.6))
            3.141592653589793
            sage: maxima('atan2(0,-0.6)')
            3.141592653589793
            sage: float(SR(0).arctan2(0.6))
            0.0
            sage: maxima('atan2(0,0.6)')
            0.0
            sage: SR(0).arctan2(0) # see github issue #21614
            NaN
            sage: SR(I).arctan2(1)
            arctan2(I, 1)
            sage: SR(CDF(0,1)).arctan2(1)
            Traceback (most recent call last):
            ...
            ValueError: power::eval(): division by zero
            sage: SR(1).arctan2(CDF(0,1))
            Traceback (most recent call last):
            ...
            ValueError: power::eval(): division by zero

            sage: arctan2(0,oo)
            0
            sage: SR(oo).arctan2(oo)
            1/4*pi
            sage: SR(oo).arctan2(0)
            1/2*pi
            sage: SR(-oo).arctan2(0)
            -1/2*pi
            sage: SR(-oo).arctan2(-2)
            pi
            sage: SR(unsigned_infinity).arctan2(2)
            Traceback (most recent call last):
            ...
            RuntimeError: arctan2_eval(): arctan2(x, unsigned_infinity) encountered
            sage: SR(2).arctan2(oo)
            1/2*pi
            sage: SR(2).arctan2(-oo)
            -1/2*pi
            sage: SR(2).arctan2(SR(unsigned_infinity))
            Traceback (most recent call last):
            ...
            RuntimeError: arctan2_eval(): arctan2(unsigned_infinity, x) encountered"""
    def arctanh(self, hold: bool = False) -> Expression[P]:
        """
        Return the inverse hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: x.arctanh()
            arctanh(x)
            sage: SR(0).arctanh()
            0
            sage: SR(1/2).arctanh()
            1/2*log(3)
            sage: SR(0.5).arctanh()
            0.549306144334055
            sage: SR(0.5).arctanh().tanh()
            0.500000000000000
            sage: maxima('atanh(0.5)')  # abs tol 2e-16
            0.5493061443340548

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(-1/2).arctanh()
            -1/2*log(3)
            sage: SR(-1/2).arctanh(hold=True)
            arctanh(-1/2)

        This also works using functional notation::

            sage: arctanh(-1/2,hold=True)
            arctanh(-1/2)
            sage: arctanh(-1/2)
            -1/2*log(3)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(-1/2).arctanh(hold=True); a.unhold()
            -1/2*log(3)

        TESTS::

            sage: SR(1).arctanh()
            +Infinity
            sage: SR(-1).arctanh()
            -Infinity

            sage: SR(oo).arctanh()
            -1/2*I*pi
            sage: SR(-oo).arctanh()
            1/2*I*pi
            sage: SR(unsigned_infinity).arctanh()
            Traceback (most recent call last):
            ...
            RuntimeError: arctanh_eval(): arctanh(unsigned_infinity) encountered"""
    def arguments(self) -> tuple[Expression[SymbolicRing]]: # or the parent's arguments?
        """
        EXAMPLES::

            sage: x,y = var('x,y')
            sage: f = x + y
            sage: f.arguments()
            (x, y)

            sage: g = f.function(x)
            sage: g.arguments()
            (x,)"""
    args = arguments
    def assume(self) -> None:
        """
        Assume that this equation holds. This is relevant for symbolic
        integration, among other things.

        EXAMPLES: We call the assume method to assume that `x>2`::

            sage: (x > 2).assume()

        ``bool`` returns ``True`` below if the inequality is *definitely* known
        to be true.

        ::

            sage: bool(x > 0)
            True
            sage: bool(x < 0)
            False

        This may or may not be True, so ``bool`` returns False::

            sage: bool(x > 3)
            False

        If you make inconsistent or meaningless assumptions,
        Sage will let you know::

            sage: forget()
            sage: assume(x<0)
            sage: assume(x>0)
            Traceback (most recent call last):
            ...
            ValueError: Assumption is inconsistent
            sage: assumptions()
            [x < 0]
            sage: forget()

        TESTS::

            sage: v,c = var('v,c')
            sage: assume(c != 0)
            sage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)
            -75/8*sqrt(c^2)*arcsin(sqrt(c^2)*v/c^2) + 83/8*v/sqrt(-v^2/c^2 + 1) - 17/8*v^3/(c^2*sqrt(-v^2/c^2 + 1)) - 1/4*v^5/(c^4*sqrt(-v^2/c^2 + 1))
            sage: forget()"""
    def binomial(self, k: CoercibleToExpression, hold: bool = False) -> Expression[P]:
        """
        Return binomial coefficient "self choose k".

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: var(\'x, y\')
            (x, y)
            sage: SR(5).binomial(SR(3))
            10
            sage: x.binomial(SR(3))
            1/6*(x - 1)*(x - 2)*x
            sage: x.binomial(y)
            binomial(x, y)

        To prevent automatic evaluation use the ``hold`` argument::

            sage: x.binomial(3, hold=True)
            binomial(x, 3)
            sage: SR(5).binomial(3, hold=True)
            binomial(5, 3)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(5).binomial(3, hold=True); a.unhold()
            10

        The ``hold`` parameter is also supported in functional notation::

            sage: binomial(5,3, hold=True)
            binomial(5, 3)

        TESTS:

        Check if we handle zero correctly (:issue:`8561`)::

            sage: x.binomial(0)
            1
            sage: SR(0).binomial(0)
            1"""
    def canonicalize_radical(self) -> Expression[P]:
        """
        Choose a canonical branch of the given expression.

        The square root, cube root, natural log, etc. functions are
        multi-valued. The ``canonicalize_radical()`` method will
        choose *one* of these values based on a heuristic.

        For example, ``sqrt(x^2)`` has two values: ``x``, and
        ``-x``. The ``canonicalize_radical()`` function will choose
        *one* of them, consistently, based on the behavior of the
        expression as ``x`` tends to positive infinity. The solution
        chosen is the one which exhibits this same behavior. Since
        ``sqrt(x^2)`` approaches positive infinity as ``x`` does, the
        solution chosen is ``x`` (which also tends to positive
        infinity).

        .. WARNING::

            As shown in the examples below, a canonical form is not always
            returned, i.e., two mathematically identical expressions might
            be converted to different expressions.

            Assumptions are not taken into account during the
            transformation. This may result in a branch choice
            inconsistent with your assumptions.

        ALGORITHM:

        This uses the Maxima ``radcan()`` command. From the Maxima
        documentation:

        .. pull-quote::

            Simplifies an expression, which can contain logs,
            exponentials, and radicals, by converting it into a form
            which is canonical over a large class of expressions and a
            given ordering of variables; that is, all functionally
            equivalent forms are mapped into a unique form. For a
            somewhat larger class of expressions, radcan produces a
            regular form. Two equivalent expressions in this class do
            not necessarily have the same appearance, but their
            difference can be simplified by radcan to zero.

            For some expressions radcan is quite time consuming. This
            is the cost of exploring certain relationships among the
            components of the expression for simplifications based on
            factoring and partial fraction expansions of exponents.

        EXAMPLES:

        ``canonicalize_radical()`` can perform some of the same
        manipulations as :meth:`log_expand`::

            sage: y = SR.symbol(\'y\')
            sage: f = log(x*y)
            sage: f.log_expand()
            log(x) + log(y)
            sage: f.canonicalize_radical()
            log(x) + log(y)

        And also handles some exponential functions::

            sage: f = (e^x-1)/(1+e^(x/2))
            sage: f.canonicalize_radical()
            e^(1/2*x) - 1

        It can also be used to change the base of a logarithm when the
        arguments to ``log()`` are positive real numbers::

            sage: f = log(8)/log(2)
            sage: f.canonicalize_radical()
            3

        ::

            sage: a = SR.symbol(\'a\')
            sage: f = (log(x+x^2)-log(x))^a/log(1+x)^(a/2)
            sage: f.canonicalize_radical()
            log(x + 1)^(1/2*a)

        The simplest example of counter-intuitive behavior is what
        happens when we take the square root of a square::

            sage: sqrt(x^2).canonicalize_radical()
            x

        If you don\'t want this kind of "simplification," don\'t use
        ``canonicalize_radical()``.

        This behavior can also be triggered when the expression under
        the radical is not given explicitly as a square::

            sage: sqrt(x^2 - 2*x + 1).canonicalize_radical()
            x - 1

        Another place where this can become confusing is with
        logarithms of complex numbers. Suppose ``x`` is complex with
        ``x == r*e^(I*t)`` (``r`` real). Then ``log(x)`` is
        ``log(r) + I*(t + 2*k*pi)`` for some integer ``k``.

        Calling ``canonicalize_radical()`` will choose a branch,
        eliminating the solutions for all choices of ``k`` but
        one. Simplified by hand, the expression below is
        ``(1/2)*log(2) + I*pi*k`` for integer ``k``. However,
        ``canonicalize_radical()`` will take each log expression, and
        choose one particular solution, dropping the other. When the
        results are subtracted, we\'re left with no imaginary part::

            sage: f = (1/2)*log(2*x) + (1/2)*log(1/x)
            sage: f.canonicalize_radical()
            1/2*log(2)

        Naturally the result is wrong for some choices of ``x``::

            sage: f(x = -1)
            I*pi + 1/2*log(2)

        The example below shows two expressions e1 and e2 which are
        "simplified" to different expressions, while their difference
        is "simplified" to zero; thus ``canonicalize_radical()`` does
        not return a canonical form::

            sage: e1 = 1/(sqrt(5)+sqrt(2))
            sage: e2 = (sqrt(5)-sqrt(2))/3
            sage: e1.canonicalize_radical()
            1/(sqrt(5) + sqrt(2))
            sage: e2.canonicalize_radical()
            1/3*sqrt(5) - 1/3*sqrt(2)
            sage: (e1-e2).canonicalize_radical()
            0

        The issue reported in :issue:`3520` is a case where
        ``canonicalize_radical()`` causes a numerical integral to be
        calculated incorrectly::

            sage: f1 = sqrt(25 - x) * sqrt( 1 + 1/(4*(25-x)) )
            sage: f2 = f1.canonicalize_radical()
            sage: numerical_integral(f1.real(), 0, 1)[0] # abs tol 1e-10
            4.974852579915647
            sage: numerical_integral(f2.real(), 0, 1)[0] # abs tol 1e-10
            -4.974852579915647

        TESTS:

        This tests that :issue:`11668` has been fixed (by :issue:`12780`)::

            sage: a,b = var(\'a b\', domain=\'real\')
            sage: A = abs((a+I*b))^2
            sage: imag(A)
            0
            sage: A.canonicalize_radical() # not implemented
            a^2 + b^2
            sage: imag(A.canonicalize_radical())
            0"""
    def coefficient(
        self, s: CoercibleToExpression, n: CoercibleToExpression = 1
    ) -> Expression[P]:
        """
        Return the coefficients of this symbolic expression as a polynomial in x.

        INPUT:

        - ``x`` -- (optional) variable

        OUTPUT: depending on the value of ``sparse``,

        - A list of pairs ``(expr, n)``, where ``expr`` is a symbolic
          expression and ``n`` is a power (``sparse=True``, default)

        - A list of expressions where the ``n``-th element is the coefficient of
          ``x^n`` when ``self`` is seen as polynomial in ``x`` (``sparse=False``).

        EXAMPLES::

            sage: var(\'x, y, a\')
            (x, y, a)
            sage: p = x^3 - (x-3)*(x^2+x) + 1
            sage: p.coefficients()
            [[1, 0], [3, 1], [2, 2]]
            sage: p.coefficients(sparse=False)
            [1, 3, 2]
            sage: p = x - x^3 + 5/7*x^5
            sage: p.coefficients()
            [[1, 1], [-1, 3], [5/7, 5]]
            sage: p.coefficients(sparse=False)
            [0, 1, 0, -1, 0, 5/7]
            sage: p = expand((x-a*sqrt(2))^2 + x + 1); p
            -2*sqrt(2)*a*x + 2*a^2 + x^2 + x + 1
            sage: p.coefficients(a)
            [[x^2 + x + 1, 0], [-2*sqrt(2)*x, 1], [2, 2]]
            sage: p.coefficients(a, sparse=False)
            [x^2 + x + 1, -2*sqrt(2)*x, 2]
            sage: p.coefficients(x)
            [[2*a^2 + 1, 0], [-2*sqrt(2)*a + 1, 1], [1, 2]]
            sage: p.coefficients(x, sparse=False)
            [2*a^2 + 1, -2*sqrt(2)*a + 1, 1]

        TESTS:

        The behaviour is undefined with noninteger or negative exponents::

            sage: p = (17/3*a)*x^(3/2) + x*y + 1/x + 2*x^x + 5*x^y
            sage: rset = set([(1, -1), (y, 1), (17/3*a, 3/2), (2, x), (5, y)])
            sage: all((pair[0],pair[1]) in rset for pair in p.coefficients(x))
            True
            sage: p.coefficients(x, sparse=False)
            Traceback (most recent call last):
            ...
            ValueError: cannot return dense coefficient list with noninteger exponents

        Series coefficients are now handled correctly (:issue:`17399`)::


            sage: s = (1/(1-x)).series(x,6); s
            1 + 1*x + 1*x^2 + 1*x^3 + 1*x^4 + 1*x^5 + Order(x^6)
            sage: s.coefficients()
            [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
            sage: s.coefficients(x, sparse=False)
            [1, 1, 1, 1, 1, 1]
            sage: x,y = var("x,y")
            sage: s = (1/(1-y*x-x)).series(x,3); s
            1 + (y + 1)*x + ((y + 1)^2)*x^2 + Order(x^3)
            sage: s.coefficients(x, sparse=False)
            [1, y + 1, (y + 1)^2]

        We can find coefficients of symbolic functions, :issue:`12255`::

            sage: g = function(\'g\')(var(\'t\'))
            sage: f = 3*g + g**2 + t
            sage: f.coefficients(g)
            [[t, 0], [3, 1], [1, 2]]

        Handle bound variable strictly as part of a constant::

            sage: (sin(1+x)*sin(1+x^2)).coefficients(x)
            [[sin(x^2 + 1)*sin(x + 1), 0]]
            sage: (sin(1+x)*sin(1+x^2)*x).coefficients(x)
            [[sin(x^2 + 1)*sin(x + 1), 1]]

        Check that :issue:`23545` is fixed::

            sage: (x^2/(1+x)).coefficients()
            [[x^2/(x + 1), 0]]
            sage: (1+x+exp(x^2/(1+x))).coefficients()
            [[e^(x^2/(x + 1)) + 1, 0], [1, 1]]
            sage: (1/x).coefficients()
            [[1, -1]]
            sage: ((1+x)^pi).coefficients()
            [[(x + 1)^pi, 0]]"""
    @overload
    def coefficients( # pyright: ignore[reportOverlappingOverload]
        self, x: CoercibleToExpression | None = None, sparse: Literal[False] = ...
    ) -> list[Expression[P]]: ...
    @overload
    def coefficients(
        self, x: CoercibleToExpression | None = None, sparse: Literal[True] = True
    ) -> list[tuple[Expression[P], Expression[P]]]:
        r"""
        Return the coefficients of this symbolic expression as a polynomial in x.

        INPUT:

        - ``x`` -- (optional) variable

        OUTPUT: depending on the value of ``sparse``,

        - A list of pairs ``(expr, n)``, where ``expr`` is a symbolic
          expression and ``n`` is a power (``sparse=True``, default)

        - A list of expressions where the ``n``-th element is the coefficient of
          ``x^n`` when ``self`` is seen as polynomial in ``x`` (``sparse=False``).

        EXAMPLES::

            sage: var('x, y, a')
            (x, y, a)
            sage: p = x^3 - (x-3)*(x^2+x) + 1
            sage: p.coefficients()
            [[1, 0], [3, 1], [2, 2]]
            sage: p.coefficients(sparse=False)
            [1, 3, 2]
            sage: p = x - x^3 + 5/7*x^5
            sage: p.coefficients()
            [[1, 1], [-1, 3], [5/7, 5]]
            sage: p.coefficients(sparse=False)
            [0, 1, 0, -1, 0, 5/7]
            sage: p = expand((x-a*sqrt(2))^2 + x + 1); p
            -2*sqrt(2)*a*x + 2*a^2 + x^2 + x + 1
            sage: p.coefficients(a)
            [[x^2 + x + 1, 0], [-2*sqrt(2)*x, 1], [2, 2]]
            sage: p.coefficients(a, sparse=False)
            [x^2 + x + 1, -2*sqrt(2)*x, 2]
            sage: p.coefficients(x)
            [[2*a^2 + 1, 0], [-2*sqrt(2)*a + 1, 1], [1, 2]]
            sage: p.coefficients(x, sparse=False)
            [2*a^2 + 1, -2*sqrt(2)*a + 1, 1]

        TESTS:

        The behaviour is undefined with noninteger or negative exponents::

            sage: p = (17/3*a)*x^(3/2) + x*y + 1/x + 2*x^x + 5*x^y
            sage: rset = set([(1, -1), (y, 1), (17/3*a, 3/2), (2, x), (5, y)])
            sage: all((pair[0],pair[1]) in rset for pair in p.coefficients(x))
            True
            sage: p.coefficients(x, sparse=False)
            Traceback (most recent call last):
            ...
            ValueError: cannot return dense coefficient list with noninteger exponents

        Series coefficients are now handled correctly (:issue:`17399`)::


            sage: s = (1/(1-x)).series(x,6); s
            1 + 1*x + 1*x^2 + 1*x^3 + 1*x^4 + 1*x^5 + Order(x^6)
            sage: s.coefficients()
            [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
            sage: s.coefficients(x, sparse=False)
            [1, 1, 1, 1, 1, 1]
            sage: x,y = var("x,y")
            sage: s = (1/(1-y*x-x)).series(x,3); s
            1 + (y + 1)*x + ((y + 1)^2)*x^2 + Order(x^3)
            sage: s.coefficients(x, sparse=False)
            [1, y + 1, (y + 1)^2]

        We can find coefficients of symbolic functions, :issue:`12255`::

            sage: g = function('g')(var('t'))
            sage: f = 3*g + g**2 + t
            sage: f.coefficients(g)
            [[t, 0], [3, 1], [1, 2]]

        Handle bound variable strictly as part of a constant::

            sage: (sin(1+x)*sin(1+x^2)).coefficients(x)
            [[sin(x^2 + 1)*sin(x + 1), 0]]
            sage: (sin(1+x)*sin(1+x^2)*x).coefficients(x)
            [[sin(x^2 + 1)*sin(x + 1), 1]]

        Check that :issue:`23545` is fixed::

            sage: (x^2/(1+x)).coefficients()
            [[x^2/(x + 1), 0]]
            sage: (1+x+exp(x^2/(1+x))).coefficients()
            [[e^(x^2/(x + 1)) + 1, 0], [1, 1]]
            sage: (1/x).coefficients()
            [[1, -1]]
            sage: ((1+x)^pi).coefficients()
            [[(x + 1)^pi, 0]]
        """
    def collect(self, s: CoercibleToExpression) -> Expression[P]:
        """
        Collect the coefficients of ``s`` into a group.

        INPUT:

        - ``s`` -- the symbol whose coefficients will be collected

        OUTPUT:

        A new expression, equivalent to the original one, with the
        coefficients of ``s`` grouped.

        .. NOTE::

            The expression is not expanded or factored before the
            grouping takes place. For best results, call :meth:`expand`
            on the expression before :meth:`collect`.

        EXAMPLES:

        In the first term of `f`, `x` has a coefficient of `4y`. In
        the second term, `x` has a coefficient of `z`. Therefore, if
        we collect those coefficients, `x` will have a coefficient of
        `4y+z`::

            sage: x,y,z = var('x,y,z')
            sage: f = 4*x*y + x*z + 20*y^2 + 21*y*z + 4*z^2 + x^2*y^2*z^2
            sage: f.collect(x)
            x^2*y^2*z^2 + x*(4*y + z) + 20*y^2 + 21*y*z + 4*z^2

        Here we do the same thing for `y` and `z`; however, note that
        we do not factor the `y^{2}` and `z^{2}` terms before
        collecting coefficients::

            sage: f.collect(y)
            (x^2*z^2 + 20)*y^2 + (4*x + 21*z)*y + x*z + 4*z^2
            sage: f.collect(z)
            (x^2*y^2 + 4)*z^2 + 4*x*y + 20*y^2 + (x + 21*y)*z

        The terms are collected, whether the expression
        is expanded or not::

            sage: f = (x + y)*(x - z)
            sage: f.collect(x)
            x^2 + x*(y - z) - y*z
            sage: f.expand().collect(x)
            x^2 + x*(y - z) - y*z

        TESTS:

        The output should be equivalent to the input::

            sage: polynomials = QQ['x']
            sage: f = SR(polynomials.random_element())
            sage: g = f.collect(x)
            sage: bool(f == g)
            True

        If ``s`` is not present in the given expression, the
        expression should not be modified. The variable `z` will not
        be present in `f` below since `f` is a random polynomial of
        maximum degree 10 in `x` and `y`::

            sage: z = var('z')
            sage: polynomials = QQ['x,y']
            sage: f = SR(polynomials.random_element(10))
            sage: g = f.collect(z)
            sage: bool(str(f) == str(g))
            True

        Check if :issue:`9046` is fixed::

            sage: var('a b x y z')
            (a, b, x, y, z)
            sage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x
            sage: p.collect(x)
            -a*x^3 + (2*b*y + z + 1)*x^2 + 2*y^3 + y^2*z - (a*y^2 - a)*x + y^2"""
    def collect_common_factors(self) -> Expression[P]:
        """
        This function does not perform a full factorization but only
        looks for factors which are already explicitly present.

        Polynomials can often be brought into a more compact form by
        collecting common factors from the terms of sums. This is
        accomplished by this function.

        EXAMPLES::

            sage: var('x')
            x
            sage: (x/(x^2 + x)).collect_common_factors()
            1/(x + 1)

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: (a*x+a*y).collect_common_factors()
            a*(x + y)
            sage: (a*x^2+2*a*x*y+a*y^2).collect_common_factors()
            (x^2 + 2*x*y + y^2)*a
            sage: (a*(b*(a+c)*x+b*((a+c)*x+(a+c)*y)*y)).collect_common_factors()
            ((x + y)*y + x)*(a + c)*a*b"""
    def combine(self, deep: bool = False) -> Expression[P]:
        """
        Return a simplified version of this symbolic expression
        by combining all toplevel terms with the same denominator into
        a single term.

        Please use the keyword ``deep=True`` to apply the process
        recursively.

        EXAMPLES::

            sage: var('x, y, a, b, c')
            (x, y, a, b, c)
            sage: f = x*(x-1)/(x^2 - 7) + y^2/(x^2-7) + 1/(x+1) + b/a + c/a; f
            (x - 1)*x/(x^2 - 7) + y^2/(x^2 - 7) + b/a + c/a + 1/(x + 1)
            sage: f.combine()
            ((x - 1)*x + y^2)/(x^2 - 7) + (b + c)/a + 1/(x + 1)
            sage: (1/x + 1/x^2 + (x+1)/x).combine()
            (x + 2)/x + 1/x^2
            sage: ex = 1/x + ((x + 1)/x - 1/x)/x^2 + (x+1)/x; ex
            (x + 1)/x + 1/x + ((x + 1)/x - 1/x)/x^2
            sage: ex.combine()
            (x + 2)/x + ((x + 1)/x - 1/x)/x^2
            sage: ex.combine(deep=True)
            (x + 2)/x + 1/x^2
            sage: (1+sin((x + 1)/x - 1/x)).combine(deep=True)
            sin(1) + 1"""
    # TODO: returns vector([self]).compositional_inverse(allow_multivalued_inverse, **kwargs)[0]
    def compositional_inverse(self, allow_multivalued_inverse: bool = True, **kwargs):
        """
        Find the compositional inverse of this symbolic function.

        INPUT:

        - ``allow_multivalued_inverse`` -- (default: ``True``); see example below
        - ``**kwargs`` -- additional keyword arguments passed to :func:`sage.symbolic.relation.solve`.

        .. SEEALSO::

            :meth:`sage.modules.free_module_element.FreeModuleElement.compositional_inverse`.

        EXAMPLES::

            sage: f(x) = x+1
            sage: f.compositional_inverse()
            x |--> x - 1
            sage: var("y")
            y
            sage: f(x) = x+y
            sage: f.compositional_inverse()
            x |--> x - y
            sage: f(x) = x^2
            sage: f.compositional_inverse()
            x |--> -sqrt(x)

        When ``allow_multivalued_inverse=False``, there is some additional checking::

            sage: f(x) = x^2
            sage: f.compositional_inverse(allow_multivalued_inverse=False)
            Traceback (most recent call last):
            ...
            ValueError: inverse is multivalued, pass allow_multivalued_inverse=True to bypass

        Nonetheless, the checking is not always foolproof (``x |--> log(x) + 2*pi*I`` is another possibility)::

            sage: f(x) = exp(x)
            sage: f.compositional_inverse(allow_multivalued_inverse=False)
            x |--> log(x)

        Sometimes passing ``kwargs`` is useful, for example ``algorithm`` can be used
        when the default solver fails::

            sage: f(x) = (2/3)^x
            sage: f.compositional_inverse()
            Traceback (most recent call last):
            ...
            KeyError: x
            sage: f.compositional_inverse(algorithm="giac")                             # needs sage.libs.giac
            x |--> -log(x)/(log(3) - log(2))

        TESTS::

            sage: f(x) = x+exp(x)
            sage: f.compositional_inverse()
            Traceback (most recent call last):
            ...
            ValueError: cannot find an inverse
            sage: f(x) = 0
            sage: f.compositional_inverse()
            Traceback (most recent call last):
            ...
            ValueError: cannot find an inverse
            sage: f(x, y) = (x, x)
            sage: f.compositional_inverse()
            Traceback (most recent call last):
            ...
            ValueError: cannot find an inverse
            sage: (x+1).compositional_inverse()
            Traceback (most recent call last):
            ...
            ValueError: base ring must be a symbolic expression ring
        """
        ...
    def conjugate(self, hold: bool = False) -> Expression[P]:
        """
        Return the complex conjugate of this symbolic expression.

        EXAMPLES::

            sage: a = 1 + 2*I
            sage: a.conjugate()
            -2*I + 1
            sage: a = sqrt(2) + 3^(1/3)*I; a
            sqrt(2) + I*3^(1/3)
            sage: a.conjugate()
            sqrt(2) - I*3^(1/3)

            sage: SR(CDF.0).conjugate()
            -1.0*I
            sage: x.conjugate()
            conjugate(x)
            sage: SR(RDF(1.5)).conjugate()
            1.5
            sage: SR(float(1.5)).conjugate()
            1.5
            sage: SR(I).conjugate()
            -I
            sage: ( 1+I  + (2-3*I)*x).conjugate()
            (3*I + 2)*conjugate(x) - I + 1

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(I).conjugate(hold=True)
            conjugate(I)

        This also works in functional notation::

            sage: conjugate(I)
            -I
            sage: conjugate(I,hold=True)
            conjugate(I)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(I).conjugate(hold=True); a.unhold()
            -I"""
    def content(self, s: CoercibleToExpression) ->  Expression[P]:
        """
        Return the content of this expression when considered as a
        polynomial in ``s``.

        See also :meth:`unit`, :meth:`primitive_part`, and
        :meth:`unit_content_primitive`.

        INPUT:

        - ``s`` -- a symbolic expression

        OUTPUT:

        The content part of a polynomial as a symbolic expression. It
        is defined as the gcd of the coefficients.

        .. warning::

            The expression is considered to be a univariate polynomial
            in ``s``. The output is different from the ``content()``
            method provided by multivariate polynomial rings in Sage.

        EXAMPLES::

            sage: (2*x+4).content(x)
            2
            sage: (2*x+1).content(x)
            1
            sage: (2*x+1/2).content(x)
            1/2
            sage: var('y')
            y
            sage: (2*x + 4*sin(y)).content(sin(y))
            2"""
    def contradicts(self, soln) -> Any:
        """
        Return ``True`` if this relation is violated by the given variable assignment(s).

        EXAMPLES::

            sage: (x<3).contradicts(x==0)
            False
            sage: (x<3).contradicts(x==3)
            True
            sage: (x<=3).contradicts(x==3)
            False
            sage: y = var('y')
            sage: (x<y).contradicts(x==30)
            False
            sage: (x<y).contradicts({x: 30, y: 20})
            True"""
    def convert(self, target: Expression | None = None) -> Expression:
        """
        Call the convert function in the units package. For symbolic
        variables that are not units, this function just returns the
        variable.

        INPUT:

        - ``self`` -- the symbolic expression converting from
        - ``target`` -- (default: ``None``) the symbolic expression
          converting to

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: units.length.foot.convert()
            381/1250*meter
            sage: units.mass.kilogram.convert(units.mass.pound)
            100000000/45359237*pound

        We do not get anything new by converting an ordinary symbolic variable::

            sage: a = var('a')
            sage: a - a.convert()
            0

        Raises :exc:`ValueError` if ``self`` and ``target`` are not convertible::

            sage: units.mass.kilogram.convert(units.length.foot)
            Traceback (most recent call last):
            ...
            ValueError: Incompatible units
            sage: (units.length.meter^2).convert(units.length.foot)
            Traceback (most recent call last):
            ...
            ValueError: Incompatible units

        Recognizes derived unit relationships to base units and other
        derived units::

            sage: (units.length.foot/units.time.second^2).convert(units.acceleration.galileo)
            762/25*galileo
            sage: (units.mass.kilogram*units.length.meter/units.time.second^2).convert(units.force.newton)
            newton
            sage: (units.length.foot^3).convert(units.area.acre*units.length.inch)
            1/3630*(acre*inch)
            sage: (units.charge.coulomb).convert(units.current.ampere*units.time.second)
            (ampere*second)
            sage: (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)
            1290320000000/8896443230521*pounds_per_square_inch

        For decimal answers multiply by 1.0::

            sage: (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)*1.0
            0.145037737730209*pounds_per_square_inch

        Converting temperatures works as well::

            sage: s = 68*units.temperature.fahrenheit
            sage: s.convert(units.temperature.celsius)
            20*celsius
            sage: s.convert()
            293.150000000000*kelvin

        Trying to multiply temperatures by another unit then converting
        raises a ValueError::

            sage: wrong = 50*units.temperature.celsius*units.length.foot
            sage: wrong.convert()
            Traceback (most recent call last):
            ...
            ValueError: cannot convert"""
    def cos(self, hold: bool = False) -> Expression[P]:
        """
        Return the cosine of ``self``.

        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: cos(x^2 + y^2)
            cos(x^2 + y^2)
            sage: cos(sage.symbolic.constants.pi)
            -1
            sage: cos(SR(1))
            cos(1)
            sage: cos(SR(RealField(150)(1)))
            0.54030230586813971740093660744297660373231042

        In order to get a numeric approximation use .n()::

            sage: SR(RR(1)).cos().n()
            0.540302305868140
            sage: SR(float(1)).cos().n()
            0.540302305868140

        To prevent automatic evaluation use the ``hold`` argument::

            sage: pi.cos()
            -1
            sage: pi.cos(hold=True)
            cos(pi)

        This also works using functional notation::

            sage: cos(pi,hold=True)
            cos(pi)
            sage: cos(pi)
            -1

        To then evaluate again, we use :meth:`unhold`::

            sage: a = pi.cos(hold=True); a.unhold()
            -1

        TESTS::

            sage: SR(oo).cos()
            Traceback (most recent call last):
            ...
            RuntimeError: cos_eval(): cos(infinity) encountered
            sage: SR(-oo).cos()
            Traceback (most recent call last):
            ...
            RuntimeError: cos_eval(): cos(infinity) encountered
            sage: SR(unsigned_infinity).cos()
            Traceback (most recent call last):
            ...
            RuntimeError: cos_eval(): cos(infinity) encountered"""
    def cosh(self, hold: bool = False) -> Expression[P]:
        """
        Return cosh of ``self``.

        We have `\\cosh(x) = (e^{x} + e^{-x})/2`.

        EXAMPLES::

            sage: x.cosh()
            cosh(x)
            sage: SR(1).cosh()
            cosh(1)
            sage: SR(0).cosh()
            1
            sage: SR(1.0).cosh()
            1.54308063481524
            sage: maxima('cosh(1.0)')
            1.54308063481524...
            sage: SR(1.00000000000000000000000000).cosh()
            1.5430806348152437784779056
            sage: SR(RIF(1)).cosh()
            1.543080634815244?

        To prevent automatic evaluation use the ``hold`` argument::

            sage: arcsinh(x).cosh()
            sqrt(x^2 + 1)
            sage: arcsinh(x).cosh(hold=True)
            cosh(arcsinh(x))

        This also works using functional notation::

            sage: cosh(arcsinh(x),hold=True)
            cosh(arcsinh(x))
            sage: cosh(arcsinh(x))
            sqrt(x^2 + 1)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = arcsinh(x).cosh(hold=True); a.unhold()
            sqrt(x^2 + 1)

        TESTS::

            sage: SR(oo).cosh()
            +Infinity
            sage: SR(-oo).cosh()
            +Infinity
            sage: SR(unsigned_infinity).cosh()
            Traceback (most recent call last):
            ...
            RuntimeError: cosh_eval(): cosh(unsigned_infinity) encountered"""
    def csgn(self, hold: bool = False) -> Expression[P]:
        """
        Return the sign of ``self``, which is -1 if ``self < 0``, 0 if
        ``self == 0``, and 1 if ``self > 0``, or unevaluated when ``self`` is a
        nonconstant symbolic expression.

        If ``self`` is not real, return the complex half-plane (left or right)
        in which the number lies.  If ``self`` is pure imaginary, return the sign
        of the imaginary part of ``self``.

        EXAMPLES::

            sage: x = var('x')
            sage: SR(-2).csgn()
            -1
            sage: SR(0.0).csgn()
            0
            sage: SR(10).csgn()
            1
            sage: x.csgn()
            csgn(x)
            sage: SR(CDF.0).csgn()
            1
            sage: SR(I).csgn()
            1
            sage: SR(-I).csgn()
            -1
            sage: SR(1+I).csgn()
            1
            sage: SR(1-I).csgn()
            1
            sage: SR(-1+I).csgn()
            -1
            sage: SR(-1-I).csgn()
            -1

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(I).csgn(hold=True)
            csgn(I)"""
    def decl_assume(self, decl: str) -> None:
        """
        TESTS::

            sage: from sage.symbolic.assumptions import GenericDeclaration
            sage: decl = GenericDeclaration(x, 'real')
            sage: x.is_real()
            False
            sage: x.decl_assume(decl._assumption)
            sage: x.is_real()
            True"""
    def decl_forget(self, decl: str) -> None:
        """
        TESTS::

            sage: from sage.symbolic.assumptions import GenericDeclaration
            sage: decl = GenericDeclaration(x, 'integer')
            sage: x.is_integer()
            False
            sage: x.decl_assume(decl._assumption)
            sage: x.is_integer()
            True
            sage: x.decl_forget(decl._assumption)
            sage: x.is_integer()
            False"""
    def default_variable(self) -> Expression[P]:
        """
        Return the default variable, which is by definition the first
        variable in ``self``, or `x` if there are no variables in ``self``.
        The result is cached.

        EXAMPLES::

            sage: sqrt(2).default_variable()
            x
            sage: x, theta, a = var('x, theta, a')
            sage: f = x^2 + theta^3 - a^x
            sage: f.default_variable()
            a

        Note that this is the first *variable*, not the first *argument*::

            sage: f(theta, a, x) = a + theta^3
            sage: f.default_variable()
            a
            sage: f.variables()
            (a, theta)
            sage: f.arguments()
            (theta, a, x)"""
    def degree(self, s: CoercibleToExpression) ->  Expression[P]:
        """
        Return the exponent of the highest power of ``s`` in ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: var('x,y,a')
            (x, y, a)
            sage: f = 100 + a*x + x^3*sin(x*y) + x*y + x/y^10 + 2*sin(x*y)/x; f
            x^3*sin(x*y) + a*x + x*y + 2*sin(x*y)/x + x/y^10 + 100
            sage: f.degree(x)
            3
            sage: f.degree(y)
            1
            sage: f.degree(sin(x*y))
            1
            sage: (x^-3+y).degree(x)
            0
            sage: (1/x+1/x**2).degree(x)
            -1"""
    def demoivre(self) -> Any:
        """
        Return this symbolic expression with complex exponentials
        (optionally all exponentials) replaced by (at least partially)
        trigonometric/hyperbolic expressions.

        EXAMPLES::

            sage: x, a, b = SR.var("x, a, b")
            sage: exp(a + I*b).demoivre()
            (cos(b) + I*sin(b))*e^a
            sage: exp(I*x).demoivre()
            cos(x) + I*sin(x)
            sage: exp(x).demoivre()
            e^x
            sage: exp(x).demoivre(force=True)
            cosh(x) + sinh(x)

        TESTS:

        Check that de Moivre transformation correctly commutes
        with differentiation::

            sage: x = SR.var("x")
            sage: f = function("f")
            sage: bool(f(exp(I*x)).diff(x).demoivre() ==
            ....:      f(exp(I*x)).demoivre().diff(x))
            True"""
    def denominator(self, normalize: bool = True) -> Expression[P]:
        """
        Return the denominator of this symbolic expression.

        INPUT:

        - ``normalize`` -- boolean (default: ``True``)

        If ``normalize`` is ``True``, the expression is first normalized to
        have it as a fraction before getting the denominator.

        If ``normalize`` is ``False``, the expression is kept and if it is not
        a quotient, then this will just return 1.

        .. SEEALSO::

            :meth:`normalize`, :meth:`numerator`,
            :meth:`numerator_denominator`, :meth:`combine`

        EXAMPLES::

            sage: x, y, z, theta = var('x, y, z, theta')
            sage: f = (sqrt(x) + sqrt(y) + sqrt(z))/(x^10 - y^10 - sqrt(theta))
            sage: f.numerator()
            sqrt(x) + sqrt(y) + sqrt(z)
            sage: f.denominator()
            x^10 - y^10 - sqrt(theta)

            sage: f.numerator(normalize=False)
            (sqrt(x) + sqrt(y) + sqrt(z))
            sage: f.denominator(normalize=False)
            x^10 - y^10 - sqrt(theta)

            sage: y = var('y')
            sage: g = x + y/(x + 2); g
            x + y/(x + 2)
            sage: g.numerator(normalize=False)
            x + y/(x + 2)
            sage: g.denominator(normalize=False)
            1

        TESTS::

            sage: ((x+y)^2/(x-y)^3*x^3).denominator(normalize=False)
            (x - y)^3
            sage: ((x+y)^2*x^3).denominator(normalize=False)
            1
            sage: (y/x^3).denominator(normalize=False)
            x^3
            sage: t = y/x^3/(x+y)^(1/2); t
            y/(sqrt(x + y)*x^3)
            sage: t.denominator(normalize=False)
            sqrt(x + y)*x^3
            sage: (1/x^3).denominator(normalize=False)
            x^3
            sage: (x^3).denominator(normalize=False)
            1
            sage: (y*x^sin(x)).denominator(normalize=False)
            Traceback (most recent call last):
            ...
            TypeError: self is not a rational expression"""
    # args should be symbol or something that can be converted to symbols, or int/Intger
    # SR(1) is not allowed.
    def derivative(self, *args: CoercibleToExpression | int | Integer) -> Expression[P]:
        """
        Return the derivative of this expressions with respect to the
        variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global
        :meth:`~sage.calculus.functional.derivative` function for more
        details.

        .. SEEALSO::

            This is implemented in the ``_derivative`` method (see the
            source code).

        EXAMPLES::

            sage: var("x y")
            (x, y)
            sage: t = (x^2+y)^2
            sage: t.derivative(x)
            4*(x^2 + y)*x
            sage: t.derivative(x, 2)
            12*x^2 + 4*y
            sage: t.derivative(x, 2, y)
            4
            sage: t.derivative(y)
            2*x^2 + 2*y

        If the function depends on only one variable, you may omit the
        variable. Giving just a number (for the order of the derivative)
        also works::

            sage: f(x) = x^3 + sin(x)
            sage: f.derivative()
            x |--> 3*x^2 + cos(x)
            sage: f.derivative(2)
            x |--> 6*x - sin(x)

        Some expressions can\'t be cleanly differentiated by the
        chain rule::

            sage: _ = var(\'x\', domain=\'real\')
            sage: _ = var(\'w z\')
            sage: (x^z).conjugate().diff(x)
            conjugate(x^(z - 1))*conjugate(z)
            sage: (w^z).conjugate().diff(w)
            w^(z - 1)*z*D[0](conjugate)(w^z)
            sage: atanh(x).real_part().diff(x)
            -1/(x^2 - 1)
            sage: atanh(x).imag_part().diff(x)
            0
            sage: atanh(w).real_part().diff(w)
            -D[0](real_part)(arctanh(w))/(w^2 - 1)
            sage: atanh(w).imag_part().diff(w)
            -D[0](imag_part)(arctanh(w))/(w^2 - 1)
            sage: abs(log(x)).diff(x)
            1/2*(conjugate(log(x))/x + log(x)/x)/abs(log(x))
            sage: abs(log(z)).diff(z)
            1/2*(conjugate(log(z))/z + log(z)/conjugate(z))/abs(log(z))
            sage: forget()

            sage: t = sin(x+y^2)*tan(x*y)
            sage: t.derivative(x)
            (tan(x*y)^2 + 1)*y*sin(y^2 + x) + cos(y^2 + x)*tan(x*y)
            sage: t.derivative(y)
            (tan(x*y)^2 + 1)*x*sin(y^2 + x) + 2*y*cos(y^2 + x)*tan(x*y)

        ::

            sage: h = sin(x)/cos(x)
            sage: derivative(h,x,x,x)
            8*sin(x)^2/cos(x)^2 + 6*sin(x)^4/cos(x)^4 + 2
            sage: derivative(h,x,3)
            8*sin(x)^2/cos(x)^2 + 6*sin(x)^4/cos(x)^4 + 2

        ::

            sage: var(\'x, y\')
            (x, y)
            sage: u = (sin(x) + cos(y))*(cos(x) - sin(y))
            sage: derivative(u,x,y)
            -cos(x)*cos(y) + sin(x)*sin(y)
            sage: f = ((x^2+1)/(x^2-1))^(1/4)
            sage: g = derivative(f, x); g # this is a complex expression
            -1/2*((x^2 + 1)*x/(x^2 - 1)^2 - x/(x^2 - 1))/((x^2 + 1)/(x^2 - 1))^(3/4)
            sage: g.factor()
            -x/((x + 1)^2*(x - 1)^2*((x^2 + 1)/(x^2 - 1))^(3/4))

        ::

            sage: y = var(\'y\')
            sage: f = y^(sin(x))
            sage: derivative(f, x)
            y^sin(x)*cos(x)*log(y)

        ::

            sage: g(x) = sqrt(5-2*x)
            sage: g_3 = derivative(g, x, 3); g_3(2)
            -3

        ::

            sage: f = x*e^(-x)
            sage: derivative(f, 100)
            x*e^(-x) - 100*e^(-x)

        ::

            sage: g = 1/(sqrt((x^2-1)*(x+5)^6))
            sage: derivative(g, x)
            -((x + 5)^6*x + 3*(x^2 - 1)*(x + 5)^5)/((x^2 - 1)*(x + 5)^6)^(3/2)

        TESTS::

            sage: t.derivative()
            Traceback (most recent call last):
            ...
            ValueError: No differentiation variable specified."""
    diff = derivative
    differentiate = derivative
    # returns unchanged when P is not SR??
    def distribute(self, recursive: bool = True) -> Expression[P]:
        """
        Distribute some indexed operators over similar operators in
        order to allow further groupings or simplifications.

        Implemented cases (so far):

        - Symbolic sum of a sum ==> sum of symbolic sums

        - Integral (definite or not) of a sum ==> sum of integrals.

        - Symbolic product of a product ==> product of symbolic products.

        INPUT:

        - ``recursive`` -- (default: ``True``) the distribution proceeds
          along the subtrees of the expression

        TESTS:

            sage: var("j,k,p,q", domain=\'integer\')
            (j, k, p, q)
            sage: X,Y,Z,f,g = function("X,Y,Z,f,g")
            sage: var("x,a,b")
            (x, a, b)
            sage: sum(X(j)+Y(j),j,1,p)
            sum(X(j) + Y(j), j, 1, p)
            sage: sum(X(j)+Y(j),j,1,p).distribute()
            sum(X(j), j, 1, p) + sum(Y(j), j, 1, p)
            sage: integrate(f(x)+g(x),x)
            integrate(f(x) + g(x), x)
            sage: integrate(f(x)+g(x),x).distribute()
            integrate(f(x), x) + integrate(g(x), x)
            sage: result = integrate(f(x)+g(x),x,a,b)
            ...
            sage: result
            integrate(f(x) + g(x), x, a, b)
            sage: result = integrate(f(x)+g(x),x,a,b).distribute()
            ...
            sage: result
            integrate(f(x), x, a, b) + integrate(g(x), x, a, b)
            sage: sum(X(j)+sum(Y(k)+Z(k),k,1,q),j,1,p)
            sum(X(j) + sum(Y(k) + Z(k), k, 1, q), j, 1, p)
            sage: sum(X(j)+sum(Y(k)+Z(k),k,1,q),j,1,p).distribute()
            sum(sum(Y(k), k, 1, q) + sum(Z(k), k, 1, q), j, 1, p) + sum(X(j), j, 1, p)
            sage: sum(X(j)+sum(Y(k)+Z(k),k,1,q),j,1,p).distribute(recursive=False)
            sum(X(j), j, 1, p) + sum(sum(Y(k) + Z(k), k, 1, q), j, 1, p)
            sage: maxima("product(X(j)*Y(j),j,1,p)").sage()
            product(X(j)*Y(j), j, 1, p)
            sage: maxima("product(X(j)*Y(j),j,1,p)").sage().distribute()
            product(X(j), j, 1, p)*product(Y(j), j, 1, p)


        AUTHORS:

        - Emmanuel Charpentier, Ralf Stephan (05-2017)"""
    def divide_both_sides(self, theta, checksign: _NotUsed = None) -> Expression:
        """
        Return a relation obtained by dividing both sides of this
        relation by ``x``.

        .. NOTE::

           The ``checksign`` keyword argument is currently ignored and
           is included for backward compatibility reasons only.

        EXAMPLES::

            sage: theta = var('theta')
            sage: eqn =   (x^3 + theta < sin(x*theta))
            sage: eqn.divide_both_sides(theta, checksign=False)
            (x^3 + theta)/theta < sin(theta*x)/theta
            sage: eqn.divide_both_sides(theta)
            (x^3 + theta)/theta < sin(theta*x)/theta
            sage: eqn/theta
            (x^3 + theta)/theta < sin(theta*x)/theta"""
    def exp(self, hold: bool = False) -> Expression[P]:
        """
        Return exponential function of ``self``, i.e., `e` to the
        power of ``self``.

        EXAMPLES::

            sage: x.exp()
            e^x
            sage: SR(0).exp()
            1
            sage: SR(1/2).exp()
            e^(1/2)
            sage: SR(0.5).exp()
            1.64872127070013
            sage: math.exp(0.5)
            1.6487212707001282

            sage: SR(0.5).exp().log()
            0.500000000000000
            sage: (pi*I).exp()
            -1

        To prevent automatic evaluation use the ``hold`` argument::

            sage: (pi*I).exp(hold=True)
            e^(I*pi)

        This also works using functional notation::

            sage: exp(I*pi,hold=True)
            e^(I*pi)
            sage: exp(I*pi)
            -1

        To then evaluate again, we use :meth:`unhold`::

            sage: a = (pi*I).exp(hold=True); a.unhold()
            -1

        TESTS:

        Test if :issue:`6377` is fixed::

            sage: SR(oo).exp()
            +Infinity
            sage: SR(-oo).exp()
            0
            sage: SR(unsigned_infinity).exp()
            Traceback (most recent call last):
            ...
            RuntimeError: exp_eval(): exp^(unsigned_infinity) encountered"""
    def expand(self, side: Literal["left", "right"] | None = None) -> Expression[P]:
        """
        Expand this symbolic expression. Products of sums and exponentiated
        sums are multiplied out, numerators of rational expressions which
        are sums are split into their respective terms, and multiplications
        are distributed over addition at all levels.

        EXAMPLES:

        We expand the expression `(x-y)^5` using both
        method and functional notation.

        ::

            sage: x,y = var(\'x,y\')
            sage: a = (x-y)^5
            sage: a.expand()
            x^5 - 5*x^4*y + 10*x^3*y^2 - 10*x^2*y^3 + 5*x*y^4 - y^5
            sage: expand(a)
            x^5 - 5*x^4*y + 10*x^3*y^2 - 10*x^2*y^3 + 5*x*y^4 - y^5

        We expand some other expressions::

            sage: expand((x-1)^3/(y-1))
            x^3/(y - 1) - 3*x^2/(y - 1) + 3*x/(y - 1) - 1/(y - 1)
            sage: expand((x+sin((x+y)^2))^2)
            x^2 + 2*x*sin(x^2 + 2*x*y + y^2) + sin(x^2 + 2*x*y + y^2)^2

        Observe that :meth:`expand` also expands function arguments::

            sage: f(x) = function(\'f\')(x)
            sage: fx = f(x*(x+1)); fx
            f((x + 1)*x)
            sage: fx.expand()
            f(x^2 + x)

        We can expand individual sides of a relation::

            sage: a = (16*x-13)^2 == (3*x+5)^2/2
            sage: a.expand()
            256*x^2 - 416*x + 169 == 9/2*x^2 + 15*x + 25/2
            sage: a.expand(\'left\')
            256*x^2 - 416*x + 169 == 1/2*(3*x + 5)^2
            sage: a.expand(\'right\')
            (16*x - 13)^2 == 9/2*x^2 + 15*x + 25/2

        TESTS::

            sage: var(\'x,y\')
            (x, y)
            sage: ((x + (2/3)*y)^3).expand()
            x^3 + 2*x^2*y + 4/3*x*y^2 + 8/27*y^3
            sage: expand( (x*sin(x) - cos(y)/x)^2 )
            x^2*sin(x)^2 - 2*cos(y)*sin(x) + cos(y)^2/x^2
            sage: f = (x-y)*(x+y); f
            (x + y)*(x - y)
            sage: f.expand()
            x^2 - y^2

            sage: a,b,c = var(\'a,b,c\')
            sage: x,y = var(\'x,y\', domain=\'real\')
            sage: p,q = var(\'p,q\', domain=\'positive\')
            sage: (c/2*(5*(3*a*b*x*y*p*q)^2)^(7/2*c)).expand()
            1/2*45^(7/2*c)*(a^2*b^2*x^2*y^2)^(7/2*c)*c*p^(7*c)*q^(7*c)
            sage: ((-(-a*x*p)^3*(b*y*p)^3)^(c/2)).expand()
            (a^3*b^3*x^3*y^3)^(1/2*c)*p^(3*c)
            sage: x,y,p,q = var(\'x,y,p,q\', domain=\'complex\')

        Check that :issue:`18568` is fixed::

            sage: ((x+sqrt(2)*x)^2).expand()
            2*sqrt(2)*x^2 + 3*x^2

        Check that :issue:`21360` is fixed::

            sage: ((x^(x/2) + 1)^2).expand()
            2*x^(1/2*x) + x^x + 1
            sage: ((x^(1/2*x))^2).expand()
            x^x
            sage: ((x^(2*x))^2).expand()
            x^(4*x)

        Check that exactness is preserved::

            sage: ((x+1.001)^2).expand()
            x^2 + 2.00200000000000*x + 1.00200100000000
            sage: ((x+1.001)^3).expand()
            x^3 + 3.00300000000000*x^2 + 3.00600300000000*x + 1.00300300100000

        Check that :issue:`21302` is fixed::

            sage: ((x+1)^-2).expand()
            1/(x^2 + 2*x + 1)
            sage: (((x-1)/(x+1))^2).expand()
            x^2/(x^2 + 2*x + 1) - 2*x/(x^2 + 2*x + 1) + 1/(x^2 + 2*x + 1)

        Check that :issue:`30688` is fixed::

            sage: assume(x < 0)
            sage: sqrt(-x).expand()
            sqrt(-x)
            sage: ((-x)^(3/4)).expand()
            (-x)^(3/4)
            sage: forget()

        Check that :issue:`31077` and :issue:`31585` are fixed (also see :issue:`31679`)::

            sage: a,b,c,d = var("a b c d")
            sage: ((a + b + c)^30 * (3*b + d - 5/d)^3).expand().subs(a=0,b=2,c=-1)
            d^3 + 18*d^2 + 93*d - 465/d + 450/d^2 - 125/d^3 + 36

        Check that :issue:`31411` is fixed::

            sage: q, j = var("q, j")
            sage: A = q^(2/3) + q^(2/5)
            sage: B = product(1 - q^j, j, 1, 31) * q^(1/24)
            sage: bool((A * B).expand() == (A * B.expand()).expand())
            True"""
    expand_rational = expand
    rational_expand = expand
    # the implementation used maxima's sage method, which will returns Expression
    # with parent SR?
    def expand_log(
        self, 
        algorithm: Literal["nothing", "powers", "products", "all"] = "products",
    ) -> Expression[SymbolicRing]:
        """
        Simplify symbolic expression, which can contain logs.

        Expands logarithms of powers, logarithms of products and
        logarithms of quotients.  The option ``algorithm`` specifies
        which expression types should be expanded.

        INPUT:

        - ``self`` -- expression to be simplified

        - ``algorithm`` -- (default: ``\'products\'``) governs which
          expression is expanded. Possible values are

          - ``\'nothing\'`` (no expansion),

          - ``\'powers\'`` (log(a^r) is expanded),

          - ``\'products\'`` (like \'powers\' and also log(a*b) are expanded),

          - ``\'all\'`` (all possible expansion).

          See also examples below.

        DETAILS: This uses the Maxima simplifier and sets
        ``logexpand`` option for this simplifier. From the Maxima
        documentation: "Logexpand:true causes log(a^b) to become
        b*log(a). If it is set to all, log(a*b) will also simplify to
        log(a)+log(b). If it is set to super, then log(a/b) will also
        simplify to log(a)-log(b) for rational numbers a/b,
        a#1. (log(1/b), for integer b, always simplifies.) If it is
        set to false, all of these simplifications will be turned
        off. "

        ALIAS: :meth:`log_expand` and :meth:`expand_log` are the same

        EXAMPLES:

        By default powers and products (and quotients) are expanded,
        but not quotients of integers::

            sage: (log(3/4*x^pi)).log_expand()
            pi*log(x) + log(3/4)

        To expand also log(3/4) use ``algorithm=\'all\'``::

            sage: (log(3/4*x^pi)).log_expand(\'all\')
            pi*log(x) + log(3) - 2*log(2)

        To expand only the power use ``algorithm=\'powers\'``.::

            sage: (log(x^6)).log_expand(\'powers\')
            6*log(x)

        The expression ``log((3*x)^6)`` is not expanded with
        ``algorithm=\'powers\'``, since it is converted into product
        first::

            sage: (log((3*x)^6)).log_expand(\'powers\')
            log(729*x^6)

        This shows that the option ``algorithm`` from the previous call
        has no influence to future calls (we changed some default
        Maxima flag, and have to ensure that this flag has been
        restored)::

            sage: (log(3/4*x^pi)).log_expand()
            pi*log(x) + log(3/4)

            sage: (log(3/4*x^pi)).log_expand(\'all\')
            pi*log(x) + log(3) - 2*log(2)

            sage: (log(3/4*x^pi)).log_expand()
            pi*log(x) + log(3/4)

        TESTS:

        Most of these log expansions only make sense over the
        reals. So, we should set the Maxima ``domain`` variable to
        \'real\' before we call out to Maxima. When we return, however, we
        should set the ``domain`` back to what it was, rather than
        assuming that it was \'complex\'. See :issue:`12780`::

            sage: from sage.calculus.calculus import maxima
            sage: maxima(\'domain: real;\')
            real
            sage: x.expand_log()
            x
            sage: maxima(\'domain;\')
            real
            sage: maxima(\'domain: complex;\')
            complex

        AUTHORS:

        - Robert Marik (11-2009)"""
    log_expand = expand_log
    def expand_sum(self) -> Expression[P]:
        """
        For every symbolic sum in the given expression, try to expand it,
        symbolically or numerically.

        While symbolic sum expressions with constant limits are evaluated
        immediately on the command line, unevaluated sums of this kind can
        result from, e.g., substitution of limit variables.

        INPUT:

        - ``self`` -- symbolic expression

        EXAMPLES::

            sage: (k,n) = var('k,n')
            sage: ex = sum(abs(-k*k+n),k,1,n)(n=8); ex
            sum(abs(-k^2 + 8), k, 1, 8)
            sage: ex.expand_sum()
            162
            sage: f(x,k) = sum((2/n)*(sin(n*x)*(-1)^(n+1)), n, 1, k)
            sage: f(x,2)
            -2*sum((-1)^n*sin(n*x)/n, n, 1, 2)
            sage: f(x,2).expand_sum()
            -sin(2*x) + 2*sin(x)

        We can use this to do floating-point approximation as well::

            sage: (k,n) = var('k,n')
            sage: f(n)=sum(sqrt(abs(-k*k+n)),k,1,n)
            sage: f(n=8)
            sum(sqrt(abs(-k^2 + 8)), k, 1, 8)
            sage: f(8).expand_sum()
            sqrt(41) + sqrt(17) + 2*sqrt(14) + 3*sqrt(7) + 2*sqrt(2) + 3
            sage: f(8).expand_sum().n()
            31.7752256945384

        See :issue:`9424` for making the following no longer raise
        an error::

            sage: f(8).n()
            31.7752256945384"""
    def expand_trig(
        self, 
        full: bool = False, 
        half_angles: bool = False, 
        plus: bool = True, 
        times: bool =True
    ) -> Expression[P]:
        """
        Expand trigonometric and hyperbolic functions of sums of angles
        and of multiple angles occurring in ``self``.

        For best results, ``self`` should already be expanded.

        INPUT:

        - ``full`` -- boolean (default: ``False``); to enhance user control
          of simplification, this function expands only one level at a time
          by default, expanding sums of angles or multiple angles. To obtain
          full expansion into sines and cosines immediately, set the optional
          parameter full to ``True``.

        - ``half_angles`` -- boolean (default: ``False``); if ``True``, causes
          half-angles to be simplified away

        - ``plus`` -- boolean (default: ``True``); controls the sum rule.
          Expansion of sums (e.g. `\\sin(x + y)`) will take place only if
          ``plus`` is ``True``.

        - ``times`` -- boolean (default: ``True``); controls the product
          rule, expansion of products (e.g. `\\sin(2 x)`) will take place only
          if ``times`` is ``True``.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: sin(5*x).expand_trig()
            5*cos(x)^4*sin(x) - 10*cos(x)^2*sin(x)^3 + sin(x)^5
            sage: cos(2*x + var('y')).expand_trig()
            cos(2*x)*cos(y) - sin(2*x)*sin(y)

        We illustrate various options to this function::

            sage: f = sin(sin(3*cos(2*x))*x)
            sage: f.expand_trig()
            sin((3*cos(cos(2*x))^2*sin(cos(2*x)) - sin(cos(2*x))^3)*x)
            sage: f.expand_trig(full=True)
            sin((3*(cos(cos(x)^2)*cos(sin(x)^2)
                  + sin(cos(x)^2)*sin(sin(x)^2))^2*(cos(sin(x)^2)*sin(cos(x)^2)
                                                     - cos(cos(x)^2)*sin(sin(x)^2))
                  - (cos(sin(x)^2)*sin(cos(x)^2) - cos(cos(x)^2)*sin(sin(x)^2))^3)*x)
            sage: sin(2*x).expand_trig(times=False)
            sin(2*x)
            sage: sin(2*x).expand_trig(times=True)
            2*cos(x)*sin(x)
            sage: sin(2 + x).expand_trig(plus=False)
            sin(x + 2)
            sage: sin(2 + x).expand_trig(plus=True)
            cos(x)*sin(2) + cos(2)*sin(x)
            sage: sin(x/2).expand_trig(half_angles=False)
            sin(1/2*x)
            sage: sin(x/2).expand_trig(half_angles=True)
            (-1)^floor(1/2*x/pi)*sqrt(-1/2*cos(x) + 1/2)

        If the expression contains terms which are factored, we expand first::

            sage: (x, k1, k2) = var('x, k1, k2')
            sage: cos((k1-k2)*x).expand().expand_trig()
            cos(k1*x)*cos(k2*x) + sin(k1*x)*sin(k2*x)

        ALIAS:

        :meth:`trig_expand` and :meth:`expand_trig` are the same"""
    trig_expand = expand_trig
    def exponentialize(self) -> Expression[P]:  # TODO: returns from Exponentialize(self)()
        """
        Return this symbolic expression with all circular and hyperbolic
        functions replaced by their respective exponential
        expressions.

        EXAMPLES::

            sage: x = SR.var("x")
            sage: sin(x).exponentialize()
            -1/2*I*e^(I*x) + 1/2*I*e^(-I*x)
            sage: sec(x).exponentialize()
            2/(e^(I*x) + e^(-I*x))
            sage: tan(x).exponentialize()
            (-I*e^(I*x) + I*e^(-I*x))/(e^(I*x) + e^(-I*x))
            sage: sinh(x).exponentialize()
            -1/2*e^(-x) + 1/2*e^x
            sage: sech(x).exponentialize()
            2/(e^(-x) + e^x)
            sage: tanh(x).exponentialize()
            -(e^(-x) - e^x)/(e^(-x) + e^x)

        TESTS:

        Check that ``u(x).exponentialize().demoivre(force=True)``
        is identity::

            sage: x = SR.var("x")
            sage: all([bool(u(x).exponentialize().demoivre(force=True) == u(x))
            ....:      for u in (sin, cos, tan, csc, sec, cot,
            ....:                sinh, cosh, tanh, csch, sech, coth)])
            True

        Check that differentiation and exponentialization commute::

            sage: x = SR.var("x")
            sage: all([bool(u(x).diff(x).exponentialize() ==
            ....:           u(x).exponentialize().diff(x))
            ....:      for u in (sin, cos, tan, csc, sec, cot,
            ....:                sinh, cosh, tanh, csch, sech, coth)])
            True"""
    @overload
    def factor(self) -> Expression[SymbolicRing]: ...
    @overload
    def factor(self, dontfactor: list[object] = []) -> Expression:
        """
        Factor the expression, containing any number of variables or functions, into
        factors irreducible over the integers.

        INPUT:

        - ``self`` -- a symbolic expression

        - ``dontfactor`` -- list (default: ``[]``); a list of
          variables with respect to which factoring is not to occur.
          Factoring also will not take place with respect to any variables
          which are less important (using the variable ordering assumed for
          CRE form) than those on the 'dontfactor' list.

        EXAMPLES::

            sage: x,y,z = var('x, y, z')
            sage: (x^3-y^3).factor()
            (x^2 + x*y + y^2)*(x - y)
            sage: factor(-8*y - 4*x + z^2*(2*y + x))
            (x + 2*y)*(z + 2)*(z - 2)
            sage: f = -1 - 2*x - x^2 + y^2 + 2*x*y^2 + x^2*y^2
            sage: F = factor(f/(36*(1 + 2*y + y^2)), dontfactor=[x]); F
            1/36*(x^2 + 2*x + 1)*(y - 1)/(y + 1)

        If you are factoring a polynomial with rational coefficients (and
        dontfactor is empty) the factorization is done using Singular
        instead of Maxima, so the following is very fast instead of
        dreadfully slow::

            sage: var('x,y')
            (x, y)
            sage: (x^99 + y^99).factor()
            (x^60 + x^57*y^3 - x^51*y^9 - x^48*y^12 + x^42*y^18 + x^39*y^21 -
            x^33*y^27 - x^30*y^30 - x^27*y^33 + x^21*y^39 + x^18*y^42 -
            x^12*y^48 - x^9*y^51 + x^3*y^57 + y^60)*(x^20 + x^19*y -
            x^17*y^3 - x^16*y^4 + x^14*y^6 + x^13*y^7 - x^11*y^9 -
            x^10*y^10 - x^9*y^11 + x^7*y^13 + x^6*y^14 - x^4*y^16 -
            x^3*y^17 + x*y^19 + y^20)*(x^10 - x^9*y + x^8*y^2 - x^7*y^3 +
            x^6*y^4 - x^5*y^5 + x^4*y^6 - x^3*y^7 + x^2*y^8 - x*y^9 +
            y^10)*(x^6 - x^3*y^3 + y^6)*(x^2 - x*y + y^2)*(x + y)

        TESTS:

        Check that :issue:`21529` is fixed::

            sage: f(x) = function('f')(x)
            sage: (f(x).diff(x)^2-1).factor()
            (diff(f(x), x) + 1)*(diff(f(x), x) - 1)

        Check that :issue:`27304` is fixed::

            sage: factor(2*exp(x) + exp(-x))
            (2*e^(2*x) + 1)*e^(-x)
            sage: factor(x*exp(-x) + exp(-x))
            (x + 1)*e^(-x)
            sage: factor(x + sqrt(x))
            x + sqrt(x)
            sage: factor((x + sqrt(x))/(x - sqrt(x)))
            (x + sqrt(x))/(x - sqrt(x))

        Check that :issue:`33640` is fixed::

            sage: ((x + 1)^2 - 2*x - 1).factor()
            x^2"""
    def factor_list(self, dontfactor: list[object]= []) -> list[tuple[Expression, Expression|int]]:
        """
        Return a list of the factors of self, as computed by the
        factor command.

        INPUT:

        - ``self`` -- a symbolic expression

        - ``dontfactor`` -- see docs for :meth:`factor`

        .. NOTE::

           If you already have a factored expression and just want to
           get at the individual factors, use the ``_factor_list`` method
           instead.

        EXAMPLES::

            sage: var('x, y, z')
            (x, y, z)
            sage: f = x^3-y^3
            sage: f.factor()
            (x^2 + x*y + y^2)*(x - y)

        Notice that the -1 factor is separated out::

            sage: f.factor_list()
            [(x^2 + x*y + y^2, 1), (x - y, 1)]

        We factor a fairly straightforward expression::

            sage: factor(-8*y - 4*x + z^2*(2*y + x)).factor_list()
            [(x + 2*y, 1), (z + 2, 1), (z - 2, 1)]

        A more complicated example::

            sage: var('x, u, v')
            (x, u, v)
            sage: f = expand((2*u*v^2-v^2-4*u^3)^2 * (-u)^3 * (x-sin(x))^3)
            sage: f.factor()
            -(4*u^3 - 2*u*v^2 + v^2)^2*u^3*(x - sin(x))^3
            sage: g = f.factor_list(); g
            [(4*u^3 - 2*u*v^2 + v^2, 2), (u, 3), (x - sin(x), 3), (-1, 1)]

        This function also works for quotients::

            sage: f = -1 - 2*x - x^2 + y^2 + 2*x*y^2 + x^2*y^2
            sage: g = f/(36*(1 + 2*y + y^2)); g
            1/36*(x^2*y^2 + 2*x*y^2 - x^2 + y^2 - 2*x - 1)/(y^2 + 2*y + 1)
            sage: g.factor(dontfactor=[x])
            1/36*(x^2 + 2*x + 1)*(y - 1)/(y + 1)
            sage: g.factor_list(dontfactor=[x])
            [(x^2 + 2*x + 1, 1), (y + 1, -1), (y - 1, 1), (1/36, 1)]

        This example also illustrates that the exponents do not have to be
        integers::

            sage: f = x^(2*sin(x)) * (x-1)^(sqrt(2)*x); f
            (x - 1)^(sqrt(2)*x)*x^(2*sin(x))
            sage: f.factor_list()
            [(x - 1, sqrt(2)*x), (x, 2*sin(x))]"""
    def factorial(self, hold: bool = False) -> Expression[P]:
        """
        Return the factorial of ``self``.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: SR(5).factorial()
            120
            sage: x.factorial()
            factorial(x)
            sage: (x^2+y^3).factorial()
            factorial(y^3 + x^2)

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(5).factorial(hold=True)
            factorial(5)

        This also works using functional notation::

            sage: factorial(5,hold=True)
            factorial(5)
            sage: factorial(5)
            120

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(5).factorial(hold=True); a.unhold()
            120"""
    def find(self, pattern: CoercibleToExpression) -> list[Expression[P]]:
        """
        Find all occurrences of the given pattern in this expression.

        Note that once a subexpression matches the pattern, the search does
        not extend to subexpressions of it.

        EXAMPLES::

            sage: var('x,y,z,a,b')
            (x, y, z, a, b)
            sage: w0 = SR.wild(0); w1 = SR.wild(1)

            sage: (sin(x)*sin(y)).find(sin(w0))
            [sin(y), sin(x)]

            sage: ((sin(x)+sin(y))*(a+b)).expand().find(sin(w0))
            [sin(y), sin(x)]

            sage: (1+x+x^2+x^3).find(x)
            [x]
            sage: (1+x+x^2+x^3).find(x^w0)
            [x^2, x^3]

            sage: (1+x+x^2+x^3).find(y)
            []

            # subexpressions of a match are not listed
            sage: ((x^y)^z).find(w0^w1)
            [(x^y)^z]"""
    def find_local_maximum(self, a, b, var=..., tol=..., maxfun=..., imaginary_tolerance=...) -> Any:
        """
        Numerically find a local maximum of the expression ``self``
        on the interval [a,b] (or [b,a]) along with the point at which the
        maximum is attained.

        See the documentation for
        :func:`find_local_minimum` for more details.

        EXAMPLES::

            sage: f = x*cos(x)
            sage: f.find_local_maximum(0,5)                                             # needs scipy
            (0.5610963381910451, 0.8603335890...)
            sage: f.find_local_maximum(0,5, tol=0.1, maxfun=10)                         # needs scipy
            (0.561090323458081..., 0.857926501456...)"""
    def find_local_minimum(self, a, b, var=..., tol=..., maxfun=..., imaginary_tolerance=...) -> Any:
        """
        Numerically find a local minimum of the expression ``self``
        on the interval [a,b] (or [b,a]) and the point at which it attains
        that minimum. Note that ``self`` must be a function of
        (at most) one variable.

        INPUT:

        - ``a`` -- real number; left endpoint of interval on which to minimize

        - ``b`` -- real number; right endpoint of interval on which to minimize

        - ``var`` -- variable (default: first variable in ``self``); the
          variable in ``self`` to maximize over

        - ``tol`` -- positive real (default: 1.48e-08); the convergence
          tolerance

        - ``maxfun`` -- natural number (default: 500); maximum function
          evaluations

        - ``imaginary_tolerance`` -- (default: ``1e-8``) if an imaginary
          number arises (due, for example, to numerical issues), this
          tolerance specifies how large it has to be in magnitude before
          we raise an error. In other words, imaginary parts smaller than
          this are ignored when we are expecting a real answer.

        OUTPUT:

        A tuple ``(minval, x)``, where

        - ``minval`` -- float; the minimum value that ``self`` takes on in
          the interval ``[a,b]``

        - ``x`` -- float; the point at which ``self`` takes on the minimum
          value

        EXAMPLES::

            sage: # needs scipy
            sage: f = x*cos(x)
            sage: f.find_local_minimum(1, 5)
            (-3.288371395590..., 3.4256184695...)
            sage: f.find_local_minimum(1, 5, tol=1e-3)
            (-3.288371361890..., 3.4257507903...)
            sage: f.find_local_minimum(1, 5, tol=1e-2, maxfun=10)
            (-3.288370845983..., 3.4250840220...)
            sage: show(f.plot(0, 20))                                                   # needs sage.plot
            sage: f.find_local_minimum(1, 15)
            (-9.477294259479..., 9.5293344109...)

        TESTS:

        Ensure that complex expressions do not cause a problem if they
        appear only as intermediate results as in :issue:`24536`::

            sage: x = SR.symbol('x', domain='real')
            sage: f = (x + I).abs()
            sage: f.find_local_minimum(-1,1)  # abs tol 1e-7                            # needs scipy
            (1.0, 1.6937685757340167e-08)

        ALGORITHM:

        Uses :func:`sage.numerical.optimize.find_local_minimum`.

        AUTHORS:

        - William Stein (2007-12-07)"""
    # TODO: this use sage.numerical.optimize.fint_root
    def find_root(
        self, 
        a, 
        b, 
        var: _NotUsed = None, 
        xtol = 10e-13, 
        rtol = 2.0**-50, 
        maxiter = 100, 
        full_output = False, 
        imaginary_tolerance = 1e-8
    ) -> Any:
        """
        Numerically find a root of ``self`` on the closed interval [a,b] (or
        [b,a]) if possible, where ``self`` is a function in one variable.
        Note: this function only works in fixed (machine) precision, it is not
        possible to get arbitrary precision approximations with it.

        INPUT:

        - ``a``, ``b`` -- endpoints of the interval

        - ``var`` -- (optional) variable

        - ``xtol, rtol`` -- the routine converges when a root is known to lie
          within ``xtol`` of the value return. Should be nonnegative. The
          routine modifies this to take into account the relative precision of
          doubles.

        - ``maxiter`` -- integer; if convergence is not achieved in maxiter
          iterations, an error is raised. Must be nonnegative.

        - ``full_output`` -- boolean (default: ``False``); if ``True``,
          also return object that contains information about convergence

        - ``imaginary_tolerance`` -- (default: ``1e-8``) if an imaginary
          number arises (due, for example, to numerical issues), this
          tolerance specifies how large it has to be in magnitude before
          we raise an error. In other words, imaginary parts smaller than
          this are ignored when we are expecting a real answer.

        EXAMPLES:

        Note that in this example both f(-2) and f(3) are positive,
        yet we still find a root in that interval::

            sage: # needs scipy
            sage: f = x^2 - 1
            sage: f.find_root(-2, 3)
            1.0
            sage: f.find_root(-2, 3, x)
            1.0
            sage: z, result = f.find_root(-2, 3, full_output=True)
            sage: result.converged
            True
            sage: result.flag
            'converged'
            sage: result.function_calls
            11
            sage: result.iterations
            10
            sage: result.root
            1.0

        More examples::

            sage: (sin(x) + exp(x)).find_root(-10, 10)                                  # needs scipy
            -0.588532743981862...
            sage: sin(x).find_root(-1,1)                                                # needs scipy
            0.0

        This example was fixed along with :issue:`4942` -
        there was an error in the example
        pi is a root for tan(x), but an asymptote to 1/tan(x)
        added an example to show handling of both cases::

            sage: (tan(x)).find_root(3,3.5)                                             # needs scipy
            3.1415926535...
            sage: (1/tan(x)).find_root(3, 3.5)                                          # needs scipy
            Traceback (most recent call last):
            ...
            NotImplementedError: Brent's method failed to find a zero for f on the interval

        An example with a square root::

            sage: f = 1 + x + sqrt(x+2); f.find_root(-2,10)                             # needs scipy
            -1.618033988749895

        Some examples that Ted Kosan came up with::

            sage: t = var('t')
            sage: v = 0.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))
            sage: v.find_root(0, 0.002)                                                 # needs scipy
            0.001540327067911417...

        With this expression, we can see there is a
        zero very close to the origin::

            sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t)) - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))^2
            sage: show(plot(a, 0, .002), xmin=0, xmax=.002)                             # needs sage.plot

        It is easy to approximate with ``find_root``::

            sage: a.find_root(0,0.002)                                                  # needs scipy
            0.0004110514049349...

        Using solve takes more effort, and even then gives
        only a solution with free (integer) variables::

            sage: a.solve(t)
            []
            sage: b = a.canonicalize_radical(); b
            (46080.0*e^(1800*t) - 576000.0*e^(900*t) + 737280.0)*e^(-2400*t)
            sage: b.solve(t)
            []
            sage: b.solve(t, to_poly_solve=True)
            [t == 1/450*I*pi*z... + 1/900*log(-3/4*sqrt(41) + 25/4),
             t == 1/450*I*pi*z... + 1/900*log(3/4*sqrt(41) + 25/4)]
            sage: n(1/900*log(-3/4*sqrt(41) + 25/4))
            0.000411051404934985

        We illustrate that root finding is only implemented in one
        dimension::

            sage: x, y = var('x,y')
            sage: (x-y).find_root(-2,2)
            Traceback (most recent call last):
            ...
            NotImplementedError: root finding currently only implemented in 1 dimension.

        TESTS:

        Test the special case that failed for the first attempt to fix
        :issue:`3980`::

            sage: t = var('t')
            sage: find_root(1/t - x,0,2)
            Traceback (most recent call last):
            ...
            NotImplementedError: root finding currently only implemented
            in 1 dimension.

        Ensure that complex expressions do not cause a problem if they
        appear only as intermediate results as in :issue:`24536`::

            sage: x = SR.symbol('x', domain='real')
            sage: f = (sqrt(x) - I).abs()
            sage: f.find_root(-2, 2, rtol=1e-6)  # abs tol 1e-6                         # needs scipy
            -1.0000000049668551"""
    def forget(self) -> None:
        """
        Forget the given constraint.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: forget()
            sage: assume(x>0, y < 2)
            sage: assumptions()
            [x > 0, y < 2]
            sage: forget(y < 2)
            sage: assumptions()
            [x > 0]

        TESTS:

        Check if :issue:`7507` is fixed::

            sage: forget()
            sage: n = var('n')
            sage: foo = sin((-1)*n*pi)
            sage: foo.simplify()
            -sin(pi*n)
            sage: assume(n, 'odd')
            sage: assumptions()
            [n is odd]
            sage: foo.simplify()
            0
            sage: forget(n, 'odd')
            sage: assumptions()
            []
            sage: foo.simplify()
            -sin(pi*n)"""
    def fraction(self, base_ring: Ring) -> FractionFieldElement[P]:
        """
        Return this expression as element of the algebraic fraction
        field over the base ring given.

        EXAMPLES::

            sage: fr = (1/x).fraction(ZZ); fr
            1/x
            sage: parent(fr)
            Fraction Field of Univariate Polynomial Ring in x over Integer Ring
            sage: parent(((pi+sqrt(2)/x).fraction(SR)))
            Fraction Field of Univariate Polynomial Ring in x over Symbolic Ring
            sage: parent(((pi+sqrt(2))/x).fraction(SR))
            Fraction Field of Univariate Polynomial Ring in x over Symbolic Ring
            sage: y = var('y')
            sage: fr = ((3*x^5 - 5*y^5)^7/(x*y)).fraction(GF(7)); fr
            (3*x^35 + 2*y^35)/(x*y)
            sage: parent(fr)
            Fraction Field of Multivariate Polynomial Ring in x, y over Finite Field of size 7

        TESTS:

        Check that :issue:`17736` is fixed::

            sage: a,b,c = var('a,b,c')
            sage: fr = (1/a).fraction(QQ); fr
            1/a
            sage: parent(fr)
            Fraction Field of Univariate Polynomial Ring in a over Rational Field
            sage: parent((b/(a+sin(c))).fraction(SR))
            Fraction Field of Multivariate Polynomial Ring in a, b over Symbolic Ring"""    
    def free_variables(self) -> tuple[Expression[SymbolicRing]]:
        """
        Return sorted tuple of unbound variables that occur in this
        expression.

        EXAMPLES::

            sage: (x,y,z) = var('x,y,z')
            sage: (x+y).free_variables()
            (x, y)
            sage: (2*x).free_variables()
            (x,)
            sage: (x^y).free_variables()
            (x, y)
            sage: sin(x+y^z).free_variables()
            (x, y, z)
            sage: _ = function('f')
            sage: e = limit( f(x,y), x=0 ); e
            limit(f(x, y), x, 0)
            sage: e.free_variables()
            (y,)"""
    def function(self, *args: Expression) -> Expression:
        """
        Return a callable symbolic expression with the given variables.

        EXAMPLES:

        We will use several symbolic variables in the examples below::

            sage: var('x, y, z, t, a, w, n')
            (x, y, z, t, a, w, n)

        ::

            sage: u = sin(x) + x*cos(y)
            sage: g = u.function(x,y)
            sage: g(x,y)
            x*cos(y) + sin(x)
            sage: g(t,z)
            t*cos(z) + sin(t)
            sage: g(x^2, x^y)
            x^2*cos(x^y) + sin(x^2)

        ::

            sage: f = (x^2 + sin(a*w)).function(a,x,w); f
            (a, x, w) |--> x^2 + sin(a*w)
            sage: f(1,2,3)
            sin(3) + 4

        Using the :meth:`function` method we can obtain the above function
        `f`, but viewed as a function of different variables::

            sage: h = f.function(w,a); h
            (w, a) |--> x^2 + sin(a*w)

        This notation also works::

            sage: h(w,a) = f
            sage: h
            (w, a) |--> x^2 + sin(a*w)

        You can even make a symbolic expression `f` into a function
        by writing ``f(x,y) = f``::

            sage: f = x^n + y^n; f
            x^n + y^n
            sage: f(x,y) = f
            sage: f
            (x, y) |--> x^n + y^n
            sage: f(2,3)
            3^n + 2^n"""
    def gamma(self, *, hold: bool = False) -> Expression[P]:
        """
        Return the Gamma function evaluated at ``self``.

        EXAMPLES::

            sage: x = var('x')
            sage: x.gamma()
            gamma(x)
            sage: SR(2).gamma()
            1
            sage: SR(10).gamma()
            362880
            sage: SR(10.0r).gamma()  # For ARM: rel tol 2e-15
            362880.0
            sage: SR(CDF(1,1)).gamma()
            0.49801566811835607 - 0.15494982830181067*I

        ::

            sage: gp('gamma(1+I)')
            0.49801566811835604271369111746219809195 - 0.15494982830181068512495513048388660520*I

        We plot the familiar plot of this log-convex function::

            sage: plot(gamma(x), -6, 4).show(ymin=-3, ymax=3)                           # needs sage.plot

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(1/2).gamma()
            sqrt(pi)
            sage: SR(1/2).gamma(hold=True)
            gamma(1/2)

        This also works using functional notation::

            sage: gamma(1/2, hold=True)
            gamma(1/2)
            sage: gamma(1/2)
            sqrt(pi)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(1/2).gamma(hold=True); a.unhold()
            sqrt(pi)

        TESTS:

        Check that no confusion with the incomplete gamma function is
        possible::

            sage: x, y = SR.var('x,y')
            sage: x.gamma(y)
            Traceback (most recent call last):
            ...
            TypeError: ...gamma() takes exactly 0 positional arguments (1 given)"""
    def gamma_normalize(self) -> Expression[P]:
        """
        Return the expression with any gamma functions that have
        a common base converted to that base.

        Additionally the expression is normalized so any fractions
        can be simplified through cancellation.

        EXAMPLES::

            sage: m,n = var('m n', domain='integer')
            sage: (gamma(n+2)/gamma(n)).gamma_normalize()
            (n + 1)*n
            sage: (gamma(n+2)*gamma(n)).gamma_normalize()
            (n + 1)*n*gamma(n)^2
            sage: (gamma(n+2)*gamma(m-1)/gamma(n)/gamma(m+1)).gamma_normalize()
            (n + 1)*n/((m - 1)*m)

        Check that :issue:`22826` is fixed::

            sage: _ = var('n')
            sage: (n-1).gcd(n+1)
            1
            sage: ex = (n-1)^2*gamma(2*n+5)/gamma(n+3) + gamma(2*n+3)/gamma(n+1)
            sage: ex.gamma_normalize()
            (4*n^3 - 2*n^2 - 7*n + 7)*gamma(2*n + 3)/((n + 1)*gamma(n + 1))"""
    def gcd(self, b: CoercibleToExpression) -> Expression[P]:
        """
        Return the symbolic gcd of ``self`` and ``b``.

        Note that the polynomial GCD is unique up to the multiplication
        by an invertible constant. The following examples make sure all
        results are caught.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: SR(10).gcd(SR(15))
            5
            sage: (x^3 - 1).gcd(x-1) / (x-1) in QQ
            True
            sage: (x^3 - 1).gcd(x^2+x+1) / (x^2+x+1) in QQ
            True
            sage: (x^3 - x^2*pi + x^2 - pi^2).gcd(x-pi) / (x-pi) in QQ
            True
            sage: gcd(sin(x)^2 + sin(x), sin(x)^2 - 1) / (sin(x) + 1) in QQ
            True
            sage: gcd(x^3 - y^3, x-y) / (x-y) in QQ
            True
            sage: gcd(x^100-y^100, x^10-y^10) / (x^10-y^10) in QQ
            True
            sage: r = gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )
            sage: r / (x^5 - 17*y + 2/3) in QQ
            True

        Embedded Sage objects of all kinds get basic support. Note that
        full algebraic GCD is not implemented yet::

            sage: gcd(I - I*x, x^2 - 1)
            x - 1
            sage: gcd(I + I*x, x^2 - 1)
            x + 1
            sage: alg = SR(QQbar(sqrt(2) + I*sqrt(3)))
            sage: gcd(alg + alg*x, x^2 - 1)  # known bug (Issue #28489)
            x + 1
            sage: gcd(alg - alg*x, x^2 - 1)  # known bug (Issue #28489)
            x - 1
            sage: sqrt2 = SR(QQbar(sqrt(2)))
            sage: gcd(sqrt2 + x, x^2 - 2)    # known bug
            1

        TESTS:

        Check if :issue:`10284` is fixed::

            sage: u = var('u')
            sage: v = var('v')
            sage: w = var('w')
            sage: x = var('x')
            sage: y = var('y')
            sage: z = var('z')
            sage: e = 792*z^8*w^4*x^3*y^4*u^7 + 24*z^4*w^4*x^2*y^3*u^4 + \\\n            ....:   264*z^8*w^3*x^2*y^7*u^5 + 198*z^4*w^5*x^5*y*u^6  + 110*z^2*w^3*x^5*y^4*u^6 \\\n            ....:   - 120*z^8*w*x^4*u^6 - 480*z^5*w*x^4*y^6*u^8 - 720*z^7*x^3*y^3*u^7 + \\\n            ....:   165*z^4*w^2*x^4*y*u^5 + 450*z^8*w^6*x^2*y*u^8 + 40*z^2*w^3*x^3*y^3*u^6 - \\\n            ....:   288*z^7*w^2*x^3*y^6*u^6  + 250*z^6*w^4*x^2*y^4*u^8 + \\\n            ....:   576*z^7*w^7*x^2*y^4*u^8  - 80*z^6*w^2*x^5*y^3*u^7 - 144*z^8*w^4*x^5*u^7 + \\\n            ....:   120*z^4*w*x^2*y^6*u^6 + 320*z^5*w^5*x^2*y^7*u^8 + 192*z^7*w^6*x*y^7*u^6 - \\\n            ....:   12*z^4*w^3*x^3*y^5*u^6  - 36*z^4*w^4*x^4*y^2*u^8 + 72*z^4*w^5*x^3*u^6  - \\\n            ....:   20*z^2*w^2*x^4*y^5*u^8 + 660*z^8*w*x^2*y^4*u^6 + 66*z^4*w^4*x^4*y^4*u^4 + \\\n            ....:   440*z^6*w^2*x^3*y^7*u^7  - 30*z^4*w*x^3*y^2*u^7 - 48*z^8*w^3*x^4*y^3*u^5 + \\\n            ....:   72*z^6*w^2*x*y^6*u^4 - 864*z^7*w^3*x^4*y^3*u^8 + 480*z^7*w^4*x*y^4*u^7 + \\\n            ....:   60*z^4*w^2*x^2*u^5 + 375*z^8*w^3*x*y*u^7 + 150*z^8*w^5*x*y^4*u^6 + \\\n            ....:   180*z^6*x*y^3*u^5 + 216*z^6*w^3*x^2*y^3*u^6;
            sage: d = e.diff(x)
            sage: gcd(d,e) / (u^4*z^2) in QQ
            True

        Check that :issue:`23793` is fixed::

            sage: gcd(I + I*x, x^2 - 1)
            x + 1

        Check that arguments are expanded before GCD (:issue:`23845`)::

            sage: P = (x+1)^2 + 1
            sage: gcd(P, P.expand())
            x^2 + 2*x + 2"""
    @overload
    def gosper_sum(self, var: CoercibleToExpression, /) -> Expression[P]: ...
    @overload
    def gosper_sum(
        self, 
        n:  CoercibleToExpression, 
        l1: CoercibleToExpression, 
        l2: CoercibleToExpression, /
    ) -> Expression[P]:
        """
        Return the summation of this hypergeometric expression using
        Gosper's algorithm.

        INPUT:

        - a symbolic expression that may contain rational functions,
          powers, factorials, gamma function terms, binomial
          coefficients, and Pochhammer symbols that are rational-linear
          in their arguments

        - the main variable and, optionally, summation limits

        EXAMPLES::

            sage: a,b,k,m,n = var('a b k m n')
            sage: SR(1).gosper_sum(n)
            n
            sage: SR(1).gosper_sum(n,5,8)
            4
            sage: n.gosper_sum(n)
            1/2*(n - 1)*n
            sage: n.gosper_sum(n,0,5)
            15
            sage: n.gosper_sum(n,0,m)
            1/2*(m + 1)*m
            sage: n.gosper_sum(n,a,b)
            -1/2*(a + b)*(a - b - 1)

        ::

            sage: (factorial(m + n)/factorial(n)).gosper_sum(n)
            n*factorial(m + n)/((m + 1)*factorial(n))
            sage: (binomial(m + n, n)).gosper_sum(n)
            n*binomial(m + n, n)/(m + 1)
            sage: (binomial(m + n, n)).gosper_sum(n, 0, a)
            (a + m + 1)*binomial(a + m, a)/(m + 1)
            sage: (binomial(m + n, n)).gosper_sum(n, 0, 5)
            1/120*(m + 6)*(m + 5)*(m + 4)*(m + 3)*(m + 2)
            sage: (rising_factorial(a,n)/rising_factorial(b,n)).gosper_sum(n)
            (b + n - 1)*gamma(a + n)*gamma(b)/((a - b + 1)*gamma(a)*gamma(b + n))
            sage: factorial(n).gosper_term(n)
            Traceback (most recent call last):
            ...
            ValueError: expression not Gosper-summable"""
    def gosper_term(self, n: CoercibleToExpression) -> Expression[P]:
        """
        Return Gosper's hypergeometric term for ``self``.

        Suppose ``f``=``self`` is a hypergeometric term such that:

        .. math::

            s_n = \\sum_{k=0}^{n-1} f_k

        and `f_k` doesn't depend on `n`. Return a hypergeometric
        term `g_n` such that `g_{n+1} - g_n = f_n`.

        EXAMPLES::

            sage: _ = var('n')
            sage: SR(1).gosper_term(n)
            n
            sage: n.gosper_term(n)
            1/2*(n^2 - n)/n
            sage: (n*factorial(n)).gosper_term(n)
            1/n
            sage: factorial(n).gosper_term(n)
            Traceback (most recent call last):
            ...
            ValueError: expression not Gosper-summable"""
    def gradient(
        self, variables: Sequence[CoercibleToExpression] | None = None
    ) -> Vector:
        """
        Compute the gradient of a symbolic function.

        This function returns a vector whose components are the derivatives
        of the original function with respect to the arguments of the
        original function. Alternatively, you can specify the variables as
        a list.

        EXAMPLES::

            sage: x,y = var('x y')
            sage: f = x^2+y^2
            sage: f.gradient()
            (2*x, 2*y)
            sage: g(x,y) = x^2+y^2
            sage: g.gradient()
            (x, y) |--> (2*x, 2*y)
            sage: n = var('n')
            sage: f(x,y) = x^n+y^n
            sage: f.gradient()
            (x, y) |--> (n*x^(n - 1), n*y^(n - 1))
            sage: f.gradient([y,x])
            (x, y) |--> (n*y^(n - 1), n*x^(n - 1))

        .. SEEALSO::

            :meth:`~sage.manifolds.differentiable.scalarfield.DiffScalarField.gradient`
            of scalar fields on Euclidean spaces (and more generally
            pseudo-Riemannian manifolds), in particular for computing the
            gradient in curvilinear coordinates."""
    def half_angle(self) -> Expression:
        """
        Replace all occurrences of trigonometric (or hyperbolic)
        functions by rational fractions of the (hyperbolic) tangent
        of half the original argument.

        This can help highlight the algebraic structure of an expression,
        which can be useful e.g. for integration.

        This method has no direct relation with the ``half_angles``
        argument of the :meth:`trig_expand` method.

        EXAMPLES::

            sage: x, t = var("x, t")
            sage: cos(x).half_angle().subs(tan(x/2) == t)
            -(t^2 - 1)/(t^2 + 1)

        Note that this structure highlighting works better after expansion::

            sage: x, t = var("x, t")
            sage: a = (cos(3*x)/(4-cos(x)))
            sage: b = a.trig_expand()
            sage: a.half_angle().subs(tan(x/2) == t).simplify_full()
            (2*(t^2 + 1)*cos(3/2*x)^2 - t^2 - 1)/(5*t^2 + 3)
            sage: b.half_angle().subs(tan(x/2) == t).simplify_full()
            -(t^6 - 15*t^4 + 15*t^2 - 1)/(5*t^6 + 13*t^4 + 11*t^2 + 3)

        TESTS::

            sage: all((u(x) == u(x).half_angle()).subs(x == 2*x).trig_simplify()
            ....:     for u in (sin, cos, tan, csc, sec, cot,
            ....:               sinh, cosh, tanh, csch, sech, coth))
            True"""
    def has(self, pattern: CoercibleToExpression) -> bool:
        """
        EXAMPLES::

            sage: var(\'x,y,a\'); w0 = SR.wild(); w1 = SR.wild()
            (x, y, a)
            sage: (x*sin(x + y + 2*a)).has(y)
            True

        Here "x+y" is not a subexpression of "x+y+2*a" (which has the
        subexpressions "x", "y" and "2*a")::

            sage: (x*sin(x + y + 2*a)).has(x+y)
            False
            sage: (x*sin(x + y + 2*a)).has(x + y + w0)
            True

        The following fails because "2*(x+y)" automatically gets converted to
        "2*x+2*y" of which "x+y" is not a subexpression::

            sage: (x*sin(2*(x+y) + 2*a)).has(x+y)
            False

        Although x^1==x and x^0==1, neither "x" nor "1" are actually of the
        form "x^something"::

            sage: (x+1).has(x^w0)
            False

        Here is another possible pitfall, where the first expression
        matches because the term "-x" has the form "(-1)*x" in GiNaC. To check
        whether a polynomial contains a linear term you should use the
        coeff() function instead.

        ::

            sage: (4*x^2 - x + 3).has(w0*x)
            True
            sage: (4*x^2 + x + 3).has(w0*x)
            False
            sage: (4*x^2 + x + 3).has(x)
            True
            sage: (4*x^2 - x + 3).coefficient(x,1)
            -1
            sage: (4*x^2 + x + 3).coefficient(x,1)
            1"""
    def has_wild(self) -> bool:
        """
        Return ``True`` if this expression contains a wildcard.

        EXAMPLES::

            sage: (1 + x^2).has_wild()
            False
            sage: (SR.wild(0) + x^2).has_wild()
            True
            sage: SR.wild(0).has_wild()
            True"""
    def hessian(self) -> Matrix:
        """
        Compute the hessian of a function. This returns a matrix components
        are the 2nd partial derivatives of the original function.

        EXAMPLES::

            sage: x,y = var('x y')
            sage: f = x^2+y^2
            sage: f.hessian()
            [2 0]
            [0 2]
            sage: g(x,y) = x^2+y^2
            sage: g.hessian()
            [(x, y) |--> 2 (x, y) |--> 0]
            [(x, y) |--> 0 (x, y) |--> 2]"""
    def horner(self, x: CoercibleToExpression) -> Expression[P]:
        """
        Rewrite this expression as a polynomial in Horner form in ``x``.

        EXAMPLES::

            sage: add((i+1)*x^i for i in range(5)).horner(x)
            (((5*x + 4)*x + 3)*x + 2)*x + 1

            sage: x, y, z = SR.var('x,y,z')
            sage: (x^5 + y*cos(x) + z^3 + (x + y)^2 + y^x).horner(x)
            z^3 + ((x^3 + 1)*x + 2*y)*x + y^2 + y*cos(x) + y^x

            sage: expr = sin(5*x).expand_trig(); expr
            5*cos(x)^4*sin(x) - 10*cos(x)^2*sin(x)^3 + sin(x)^5
            sage: expr.horner(sin(x))
            (5*cos(x)^4 - (10*cos(x)^2 - sin(x)^2)*sin(x)^2)*sin(x)
            sage: expr.horner(cos(x))
            sin(x)^5 + 5*(cos(x)^2*sin(x) - 2*sin(x)^3)*cos(x)^2

        TESTS::

            sage: SR(0).horner(x), SR(1).horner(x), x.horner(x)
            (0, 1, x)
            sage: (x^(1/3)).horner(x)
            Traceback (most recent call last):
            ...
            ValueError: cannot return dense coefficient list with noninteger exponents"""
    def imag_part(self) -> Expression[P]:
        """
        Return the imaginary part of this symbolic expression.

        EXAMPLES::

            sage: sqrt(-2).imag_part()
            sqrt(2)

        We simplify `\\ln(\\exp(z))` to `z`.  This should only
        be for `-\\pi<{\\rm Im}(z)<=\\pi`, but Maxima does not
        have a symbolic imaginary part function, so we cannot
        use ``assume`` to assume that first::

            sage: z = var('z')
            sage: f = log(exp(z))
            sage: f
            log(e^z)
            sage: f.simplify()
            z
            sage: forget()

        A more symbolic example::

            sage: var('a, b')
            (a, b)
            sage: f = log(a + b*I)
            sage: f.imag_part()
            arctan2(imag_part(a) + real_part(b), -imag_part(b) + real_part(a))

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(I).imag_part()
            1
            sage: SR(I).imag_part(hold=True)
            imag_part(I)

        This also works using functional notation::

            sage: imag_part(I, hold=True)
            imag_part(I)
            sage: imag_part(SR(I))
            1

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(I).imag_part(hold=True); a.unhold()
            1

        TESTS::

            sage: x = var('x')
            sage: x.imag_part()
            imag_part(x)
            sage: SR(2+3*I).imag_part()
            3
            sage: SR(CC(2,3)).imag_part()
            3.00000000000000
            sage: SR(CDF(2,3)).imag_part()
            3.0"""
    imag = imag_part
    def implicit_derivative(
        self, 
        Y: CoercibleToExpression,
        X: CoercibleToExpression, 
        n: int | Integer = 1
    ) -> Any:
        """
        Return the `n`-th derivative of `Y` with respect to `X` given
        implicitly by this expression.

        INPUT:

        - ``Y`` -- the dependent variable of the implicit expression

        - ``X`` -- the independent variable with respect to which the
          derivative is taken

        - ``n`` -- (default: 1) the order of the derivative

        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: f = cos(x)*sin(y)
            sage: f.implicit_derivative(y, x)
            sin(x)*sin(y)/(cos(x)*cos(y))
            sage: g = x*y^2
            sage: g.implicit_derivative(y, x, 3)
            -1/4*(y + 2*y/x)/x^2 + 1/4*(2*y^2/x - y^2/x^2)/(x*y) - 3/4*y/x^3

        It is an error to not include an independent variable term
        in the expression::

            sage: (cos(x)*sin(x)).implicit_derivative(y, x)
            Traceback (most recent call last):
            ...
            ValueError: Expression cos(x)*sin(x) contains no y terms


        TESTS:

        Check that the symbols registry is not polluted::

            sage: var('x,y')
            (x, y)
            sage: psr = copy(SR.symbols)
            sage: (x^6*y^5).implicit_derivative(y, x, 3)
            -792/125*y/x^3 + 12/25*(15*x^4*y^5 + 28*x^3*y^5)/(x^6*y^4) - 36/125*(20*x^5*y^4 + 43*x^4*y^4)/(x^7*y^3)
            sage: psr == SR.symbols
            True"""
    # TODO: this uses sage.symbolic.integration.integral.integral
    def integral(
        self, 
        v = None, 
        a = None, 
        b = None, 
        algorithm = None, 
        hold: bool = False
    ) -> Any:
        """
        Compute the integral of ``self``.

        Please see :func:`sage.symbolic.integration.integral.integrate` for more details.

        EXAMPLES::

            sage: sin(x).integral(x,0,3)
            -cos(3) + 1
            sage: sin(x).integral(x)
            -cos(x)

        TESTS:

        We check that :issue:`12438` is resolved::

            sage: f(x) = x; f
            x |--> x
            sage: integral(f, x)
            x |--> 1/2*x^2
            sage: integral(f, x, 0, 1)
            1/2

            sage: f(x, y) = x + y
            sage: f
            (x, y) |--> x + y
            sage: integral(f, y, 0, 1)
            x |--> x + 1/2
            sage: integral(f, x, 0, 1)
            y |--> y + 1/2
            sage: _(3)
            7/2
            sage: var("z")
            z
            sage: integral(f, z, 0, 2)
            (x, y) |--> 2*x + 2*y
            sage: integral(f, z)
            (x, y) |--> (x + y)*z

        We check that :issue:`13097` is resolved (sage doesn\'t
        crash). If giac is available, you may even get a usable
        answer::

            sage: f = ln(1+4/5*sin(x))
            sage: integrate(f, x, -3.1415, 3.1415)  # random
            integrate(log(4/5*sin(x) + 1), x, -3.14150000000000,
            3.14150000000000)
            sage: # needs sage.libs.giac
            sage: integrate(f, x, -3.1415, 3.1415)  # tol 10e-6
            -1.40205228301000"""
    integrate = integral
    # TODO: this uses sage.calculus.calculus.inverse_laplace
    def inverse_laplace(self, t, s) -> Any:
        """
        Return inverse Laplace transform of ``self``.

        See :obj:`sage.calculus.calculus.inverse_laplace`

        EXAMPLES::

            sage: var('w, m')
            (w, m)
            sage: f = (1/(w^2+10)).inverse_laplace(w, m); f
            1/10*sqrt(10)*sin(sqrt(10)*m)"""
    def is_algebraic(self) -> bool:
        """
        Return ``True`` if this expression is known to be algebraic.

        EXAMPLES::

            sage: sqrt(2).is_algebraic()
            True
            sage: (5*sqrt(2)).is_algebraic()
            True
            sage: (sqrt(2) + 2^(1/3) - 1).is_algebraic()
            True
            sage: (I*golden_ratio + sqrt(2)).is_algebraic()
            True
            sage: (sqrt(2) + pi).is_algebraic()
            False
            sage: SR(QQ(2/3)).is_algebraic()
            True
            sage: SR(1.2).is_algebraic()
            False

            sage: complex_root_of(x^3 - x^2 - x - 1, 0).is_algebraic()
            True"""
    def is_callable(self) -> bool:
        """
        Return ``True`` if ``self`` is a callable symbolic expression.

        EXAMPLES::

            sage: var('a x y z')
            (a, x, y, z)
            sage: f(x, y) = a + 2*x + 3*y + z
            sage: f.is_callable()
            True
            sage: (a+2*x).is_callable()
            False"""
    def is_constant(self) -> bool:
        """
        Return whether this symbolic expression is a constant.

        A symbolic expression is constant if it does not contain
        any variables.

        EXAMPLES::

            sage: pi.is_constant()
            True
            sage: SR(1).is_constant()
            True
            sage: SR(2).is_constant()
            True
            sage: log(2).is_constant()
            True
            sage: SR(I).is_constant()
            True
            sage: x.is_constant()
            False

        TESTS::

            sage: P.<p> = ZZ[]
            sage: SR(42).is_constant() == P(2).is_constant()
            True"""
    def is_exact(self) -> bool:
        """
        Return ``True`` if this expression only contains exact numerical coefficients.

        EXAMPLES::

            sage: x, y = var('x, y')
            sage: (x+y-1).is_exact()
            True
            sage: (x+y-1.9).is_exact()
            False
            sage: x.is_exact()
            True
            sage: pi.is_exact()
            True
            sage: (sqrt(x-y) - 2*x + 1).is_exact()
            True
            sage: ((x-y)^0.5 - 2*x + 1).is_exact()
            False

        TESTS::

            sage: (sin(x*cos(2*x*pi)) - 10*y^3 - 1/(x+4)).is_exact()
            True
            sage: (sin(x*cos(2.0*x*pi)) - 10*y^3 - 1/(x+4)).is_exact()
            False
            sage: SR(42).is_exact()
            True
            sage: SR(42.01).is_exact()
            False
            sage: SR(I).is_exact()
            True
            sage: (x-I).is_exact()
            True
            sage: (x-CC(0,1)).is_exact()
            False"""
    def is_infinity(self) -> bool:
        """
        Return ``True`` if ``self`` is an infinite expression.

        EXAMPLES::

            sage: SR(oo).is_infinity()
            True
            sage: x.is_infinity()
            False"""
    def is_integer(self) -> bool:
        """
        Return ``True`` if this expression is known to be an integer.

        EXAMPLES::

            sage: SR(5).is_integer()
            True

        TESTS:

        Check that integer variables are recognized (:issue:`18921`)::

            sage: _ = var('n', domain='integer')
            sage: n.is_integer()
            True

        Assumption of integer has the same effect as setting the domain::

            sage: forget()
            sage: assume(x, 'integer')
            sage: x.is_integer()
            True
            sage: forget()"""
    def is_negative(self) -> bool:
        """
        Return ``True`` if this expression is known to be negative.

        EXAMPLES::

            sage: SR(-5).is_negative()
            True

        Check if we can correctly deduce negativity of mul objects::

            sage: t0 = SR.symbol("t0", domain=\'positive\')
            sage: t0.is_negative()
            False
            sage: (-t0).is_negative()
            True
            sage: (-pi).is_negative()
            True

        Assumptions on symbols are handled correctly::

            sage: y = var(\'y\')
            sage: assume(y < 0)
            sage: y.is_positive()
            False
            sage: y.is_negative()
            True
            sage: forget()"""
    def is_negative_infinity(self) -> bool:
        """
        Return ``True`` if ``self`` is a negative infinite expression.

        EXAMPLES::

            sage: SR(oo).is_negative_infinity()
            False
            sage: SR(-oo).is_negative_infinity()
            True
            sage: x.is_negative_infinity()
            False"""
    def is_numeric(self) -> bool:
        """
        A Pynac numeric is an object you can do arithmetic with
        that is not a symbolic variable, function, or constant.
        Return ``True`` if this expression only consists of a numeric object.

        EXAMPLES::

            sage: SR(1).is_numeric()
            True
            sage: x.is_numeric()
            False
            sage: pi.is_numeric()
            False
            sage: sin(x).is_numeric()
            False"""
    def is_polynomial(self, var: CoercibleToExpression) -> bool:
        """
        Return ``True`` if ``self`` is a polynomial in the given variable.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: t = x^2 + y; t
            x^2 + y
            sage: t.is_polynomial(x)
            True
            sage: t.is_polynomial(y)
            True
            sage: t.is_polynomial(z)
            True

            sage: t = sin(x) + y; t
            y + sin(x)
            sage: t.is_polynomial(x)
            False
            sage: t.is_polynomial(y)
            True
            sage: t.is_polynomial(sin(x))
            True

        TESTS:

        Check if we can handle derivatives. :issue:`6523`::

            sage: f(x) = function('f')(x)
            sage: f(x).diff(x).is_zero()
            False

        Check if :issue:`11352` is fixed::

            sage: el = -1/2*(2*x^2 - sqrt(2*x - 1)*sqrt(2*x + 1) - 1)
            sage: el.is_polynomial(x)
            False

        Check that negative exponents are handled (:issue:`15304`)::

            sage: y = var('y')
            sage: (y/x).is_polynomial(x)
            False"""
    def is_positive(self) -> bool:
        """
        Return ``True`` if this expression is known to be positive.

        EXAMPLES::

            sage: t0 = SR.symbol("t0", domain=\'positive\')
            sage: t0.is_positive()
            True
            sage: t0.is_negative()
            False
            sage: t0.is_real()
            True
            sage: t1 = SR.symbol("t1", domain=\'positive\')
            sage: (t0*t1).is_positive()
            True
            sage: (t0 + t1).is_positive()
            True
            sage: (t0*x).is_positive()
            False

        ::

            sage: forget()
            sage: assume(x>0)
            sage: x.is_positive()
            True
            sage: cosh(x).is_positive()
            True
            sage: f = function(\'f\')(x)
            sage: assume(f>0)
            sage: f.is_positive()
            True
            sage: forget()

        TESTS:

        Check if :issue:`18630` is fixed::

            sage: (log(1/2)).is_negative()
            True
            sage: e.is_positive()
            True
            sage: (e+1).is_positive()
            True
            sage: (2*e).is_positive()
            True
            sage: (e^3).is_positive()
            True

        ::

            sage: cosh(x).is_positive()
            False
            sage: cosh(real(x)).is_positive()
            True
            sage: (cosh(real(x))^2).is_positive()
            True
            sage: ((real(x))^2).is_positive()
            False
            sage: gamma(x^2).is_positive()
            False
            sage: gamma(x^2+1).is_positive()
            False
            sage: gamma(cosh(real(x))).is_positive()
            True
            sage: (real(x)^2).is_positive()
            False
            sage: (real(x)^2+1).is_positive()
            True
            sage: (abs(x)^2+1).is_positive()
            True
            sage: gamma(real(x)^2+1).is_positive()
            True
            sage: cos(I + 1).is_positive()
            False
            sage: sin(2 - I).is_positive()
            False

        ::

            sage: (log(1/3) * log(1/2)).is_positive()
            True
            sage: log((2**500+1)/2**500).is_positive()
            True
            sage: log(2*500/(2**500-1)).is_negative()
            True
            sage: ((-pi^(1/5))^2).is_positive()
            True
            sage: (pi^2).is_positive()
            True
            sage: ((-pi)^2).is_positive()
            True"""
    def is_positive_infinity(self) -> bool:
        """
        Return ``True`` if ``self`` is a positive infinite expression.

        EXAMPLES::

            sage: SR(oo).is_positive_infinity()
            True
            sage: SR(-oo).is_positive_infinity()
            False
            sage: x.is_infinity()
            False"""
    def is_rational_expression(self) -> bool:
        """
        Return ``True`` if this expression if a rational expression, i.e.,
        a quotient of polynomials.

        EXAMPLES::

            sage: var('x y z')
            (x, y, z)
            sage: ((x + y + z)/(1 + x^2)).is_rational_expression()
            True
            sage: ((1 + x + y)^10).is_rational_expression()
            True
            sage: ((1/x + z)^5 - 1).is_rational_expression()
            True
            sage: (1/(x + y)).is_rational_expression()
            True
            sage: (exp(x) + 1).is_rational_expression()
            False
            sage: (sin(x*y) + z^3).is_rational_expression()
            False
            sage: (exp(x) + exp(-x)).is_rational_expression()
            False"""
    def is_real(self) -> bool:
        """
        Return ``True`` if this expression is known to be a real number.

        EXAMPLES::

            sage: t0 = SR.symbol("t0", domain=\'real\')
            sage: t0.is_real()
            True
            sage: t0.is_positive()
            False
            sage: t1 = SR.symbol("t1", domain=\'positive\')
            sage: (t0+t1).is_real()
            True
            sage: (t0+x).is_real()
            False
            sage: (t0*t1).is_real()
            True
            sage: t2 = SR.symbol("t2", domain=\'positive\')
            sage: (t1**t2).is_real()
            True
            sage: (t0*x).is_real()
            False
            sage: (t0^t1).is_real()
            False
            sage: (t1^t2).is_real()
            True
            sage: gamma(pi).is_real()
            True
            sage: cosh(-3).is_real()
            True
            sage: cos(exp(-3) + log(2)).is_real()
            True
            sage: gamma(t1).is_real()
            True
            sage: (x^pi).is_real()
            False
            sage: (cos(exp(t0) + log(t1))^8).is_real()
            True
            sage: cos(I + 1).is_real()
            False
            sage: sin(2 - I).is_real()
            False
            sage: (2^t0).is_real()
            True

        The following is real, but we cannot deduce that.::

            sage: (x*x.conjugate()).is_real()
            False

        Assumption of real has the same effect as setting the domain::

            sage: forget()
            sage: assume(x, \'real\')
            sage: x.is_real()
            True
            sage: cosh(x).is_real()
            True
            sage: forget()

        The real domain is also set with the integer domain::

            sage: SR.var(\'x\', domain=\'integer\').is_real()
            True

        TESTS:

        Check that :issue:`23093` is fixed::

            sage: sqrt(-2).is_real()
            False"""
    def is_relational(self) -> bool:
        """
        Return ``True`` if ``self`` is a relational expression.

        EXAMPLES::

            sage: x = var('x')
            sage: eqn = (x-1)^2 == x^2 - 2*x + 3
            sage: eqn.is_relational()
            True
            sage: sin(x).is_relational()
            False"""
    def is_square(self) -> bool:
        """
        Return ``True`` if ``self`` is the square of another symbolic expression.

        This is ``True`` for all constant, non-relational expressions
        (containing no variables or comparison), and not implemented
        otherwise.

        EXAMPLES::

            sage: SR(4).is_square()
            True
            sage: SR(5).is_square()
            True
            sage: pi.is_square()
            True
            sage: x.is_square()
            Traceback (most recent call last):
            ...
            NotImplementedError: is_square() not implemented for non-constant
            or relational elements of Symbolic Ring
            sage: r = SR(4) == SR(5)
            sage: r.is_square()
            Traceback (most recent call last):
            ...
            NotImplementedError: is_square() not implemented for non-constant
            or relational elements of Symbolic Ring"""
    def is_symbol(self) -> bool:
        """
        Return ``True`` if this symbolic expression consists of only a symbol, i.e.,
        a symbolic variable.

        EXAMPLES::

            sage: x.is_symbol()
            True
            sage: var('y')
            y
            sage: y.is_symbol()
            True
            sage: (x*y).is_symbol()
            False
            sage: pi.is_symbol()
            False

        ::

            sage: ((x*y)/y).is_symbol()
            True
            sage: (x^y).is_symbol()
            False"""
    def is_terminating_series(self) -> bool:
        """
        Return ``True`` if ``self`` is a series without order term.

        A series is terminating if it can be represented exactly,
        without requiring an order term. You can explicitly
        request terminating series by setting the order to
        positive infinity.

        OUTPUT: boolean; whether ``self`` was constructed by :meth:`series`
        and has no order term

        EXAMPLES::

            sage: (x^5+x^2+1).series(x, +oo)
            1 + 1*x^2 + 1*x^5
            sage: (x^5+x^2+1).series(x,+oo).is_terminating_series()
            True
            sage: SR(5).is_terminating_series()
            False
            sage: var('x')
            x
            sage: x.is_terminating_series()
            False
            sage: exp(x).series(x,10).is_terminating_series()
            False"""
    def is_trivial_zero(self) -> bool:
        """
        Check if this expression is trivially equal to zero without any
        simplification.

        This method is intended to be used in library code where trying to
        obtain a mathematically correct result by applying potentially
        expensive rewrite rules is not desirable.

        EXAMPLES::

            sage: SR(0).is_trivial_zero()
            True
            sage: SR(0.0).is_trivial_zero()
            True
            sage: SR(float(0.0)).is_trivial_zero()
            True

            sage: (SR(1)/2^1000).is_trivial_zero()
            False
            sage: SR(1./2^10000).is_trivial_zero()
            False

        The :meth:`~sage.structure.element.Element.is_zero` method
        is more capable::

            sage: t = pi + (pi - 1)*pi - pi^2
            sage: t.is_trivial_zero()
            False
            sage: t.is_zero()
            True
            sage: t = pi + x*pi + (pi - 1 - x)*pi - pi^2
            sage: t.is_zero()
            True
            sage: u = sin(x)^2 + cos(x)^2 - 1
            sage: u.is_trivial_zero()
            False
            sage: u.is_zero()
            True"""
    def is_trivially_equal(self, other: ConvertibleToExpression) -> bool:
        """
        Check if this expression is trivially equal to the argument
        expression, without any simplification.

        Note that the expressions may still be subject to immediate
        evaluation.

        This method is intended to be used in library code where trying to
        obtain a mathematically correct result by applying potentially
        expensive rewrite rules is not desirable.

        EXAMPLES::

            sage: (x^2).is_trivially_equal(x^2)
            True
            sage: ((x+1)^2 - 2*x - 1).is_trivially_equal(x^2)
            False
            sage: (x*(x+1)).is_trivially_equal((x+1)*x)
            True
            sage: (x^2 + x).is_trivially_equal((x+1)*x)
            False
            sage: ((x+1)*(x+1)).is_trivially_equal((x+1)^2)
            True
            sage: (x^2 + 2*x + 1).is_trivially_equal((x+1)^2)
            False
            sage: (x^-1).is_trivially_equal(1/x)
            True
            sage: (x/x^2).is_trivially_equal(1/x)
            True
            sage: ((x^2+x) / (x+1)).is_trivially_equal(1/x)
            False

        TESTS:

        Make sure Python objects work as argument too::

            sage: x = SR(1/2)
            sage: x.is_trivially_equal(QQbar(1/2))
            True"""
    def is_unit(self) -> bool:
        """
        Return ``True`` if this expression is a unit of the symbolic ring.

        Note that a proof may be attempted to get the result. To avoid
        this use ``(ex-1).is_trivial_zero()``.

        EXAMPLES::

            sage: SR(1).is_unit()
            True
            sage: SR(-1).is_unit()
            True
            sage: SR(0).is_unit()
            False"""
    def iterator(self) -> ExpressionIterator[P]:
        """
        Return an iterator over the operands of this expression.

        EXAMPLES::

            sage: x,y,z = var('x,y,z')
            sage: list((x+y+z).iterator())
            [x, y, z]
            sage: list((x*y*z).iterator())
            [x, y, z]
            sage: list((x^y*z*(x+y)).iterator())
            [x + y, x^y, z]

        Note that symbols, constants and numeric objects do not have operands,
        so the iterator function raises an error in these cases::

            sage: x.iterator()
            Traceback (most recent call last):
            ...
            ValueError: expressions containing only a numeric coefficient,
            constant or symbol have no operands
            sage: pi.iterator()
            Traceback (most recent call last):
            ...
            ValueError: expressions containing only a numeric coefficient,
            constant or symbol have no operands
            sage: SR(5).iterator()
            Traceback (most recent call last):
            ...
            ValueError: expressions containing only a numeric coefficient,
            constant or symbol have no operands"""
    # TODO: this uses sage.calculus.calculus.laplace
    def laplace(self, t, s) -> Any:
        """
        Return Laplace transform of ``self``.

        See :obj:`sage.calculus.calculus.laplace`

        EXAMPLES::

            sage: var('x,s,z')
            (x, s, z)
            sage: (z + exp(x)).laplace(x, s)
            z/s + 1/(s - 1)"""
    @overload
    def laurent_polynomial(self, base_ring: Ring = ...) -> LaurentPolynomial: ...
    @overload
    def laurent_polynomial(
        self, base_ring: None = None, ring: Ring = ...) -> LaurentPolynomial:
        """
        Return this symbolic expression as a Laurent polynomial
        over the given base ring, if possible.

        INPUT:

        - ``base_ring`` -- (optional) the base ring for the polynomial

        - ``ring`` -- (optional) the parent for the polynomial

        You can specify either the base ring (``base_ring``) you want
        the output Laurent polynomial to be over, or you can specify the full
        laurent polynomial ring (``ring``) you want the output laurent
        polynomial to be an element of.

        EXAMPLES::

            sage: f = x^2 -2/3/x + 1
            sage: f.laurent_polynomial(QQ)
            -2/3*x^-1 + 1 + x^2
            sage: f.laurent_polynomial(GF(19))
            12*x^-1 + 1 + x^2"""
    def lcm(self, b: CoercibleToExpression) -> Expression[P]:
        """
        Return the lcm of ``self`` and ``b``.

        The lcm is computed from the gcd of ``self`` and ``b`` implicitly from
        the relation ``self * b = gcd(self, b) * lcm(self, b)``.

        .. NOTE::

            In agreement with the convention in use for integers, if
            ``self * b == 0``, then ``gcd(self, b) == max(self, b)`` and
            ``lcm(self, b) == 0``.

        .. NOTE::

            Since the polynomial lcm is computed from the gcd, and the
            polynomial gcd is unique up to a constant factor (which can
            be negative), the polynomial lcm is unique up to a factor of -1.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: SR(10).lcm(SR(15))
            30
            sage: (x^3 - 1).lcm(x-1)
            x^3 - 1
            sage: (x^3 - 1).lcm(x^2+x+1)
            x^3 - 1
            sage: (x^3 - sage.symbolic.constants.pi).lcm(x-sage.symbolic.constants.pi)
            (pi - x^3)*(pi - x)
            sage: lcm(x^3 - y^3, x-y) / (x^3 - y^3) in [1,-1]
            True
            sage: lcm(x^100-y^100, x^10-y^10) / (x^100 - y^100) in [1,-1]
            True
            sage: a = expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) )
            sage: b = expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3) )
            sage: gcd(a,b) * lcm(a,b) / (a * b) in [1,-1]
            True

        The result is not automatically simplified::

            sage: ex = lcm(sin(x)^2 - 1, sin(x)^2 + sin(x)); ex
            (sin(x)^2 + sin(x))*(sin(x)^2 - 1)/(sin(x) + 1)
            sage: ex.simplify_full()
            sin(x)^3 - sin(x)

        TESTS:

        Verify that x * y = gcd(x,y) * lcm(x,y)::

            sage: x, y = var('x,y')
            sage: LRs = [(SR(10), SR(15)), (x^3-1, x-1), (x^3-y^3, x-y), (x^3-1, x^2+x+1), (SR(0), x-y)]
            sage: all((L.gcd(R) * L.lcm(R)) == L*R for L, R in LRs)
            True

        Make sure that the convention for what to do with the 0 is being respected::

            sage: gcd(x, SR(0)), lcm(x, SR(0))
            (x, 0)
            sage: gcd(SR(0), SR(0)), lcm(SR(0), SR(0))
            (0, 0)"""
    def leading_coefficient(self, s: CoercibleToExpression) -> Expression[P]:
        """
        Return the leading coefficient of ``s`` in ``self``.

        EXAMPLES::

            sage: var('x,y,a')
            (x, y, a)
            sage: f = 100 + a*x + x^3*sin(x*y) + x*y + x/y + 2*sin(x*y)/x; f
            x^3*sin(x*y) + a*x + x*y + x/y + 2*sin(x*y)/x + 100
            sage: f.leading_coefficient(x)
            sin(x*y)
            sage: f.leading_coefficient(y)
            x
            sage: f.leading_coefficient(sin(x*y))
            x^3 + 2/x"""
    leading_coeff = leading_coefficient
    def left_hand_side(self) -> Expression[P]:
        """
        If ``self`` is a relational expression, return the left hand side
        of the relation.  Otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: x = var('x')
            sage: eqn = (x-1)^2 == x^2 - 2*x + 3
            sage: eqn.left_hand_side()
            (x - 1)^2
            sage: eqn.lhs()
            (x - 1)^2
            sage: eqn.left()
            (x - 1)^2"""
    lhs = left_hand_side
    left = left_hand_side
    # this uses sage.calculus.calculus.limit
    def limit(
        self, 
        *args, 
        dir= None, 
        taylor: bool = False, 
        algorithm: str = 'maxima', 
        **kwargs
    ):
        """
        Return a symbolic limit.

        See :obj:`sage.calculus.calculus.limit`

        EXAMPLES::

            sage: (sin(x)/x).limit(x=0)
            1"""
    def list(self, x: CoercibleToExpression | None = None) -> list[Expression[P]]:
        """
        Return the coefficients of this symbolic expression as a polynomial in x.

        INPUT:

        - ``x`` -- (optional) variable

        OUTPUT:

        A list of expressions where the ``n``-th element is the coefficient of
        ``x^n`` when ``self`` is seen as polynomial in ``x``.

        EXAMPLES::

            sage: var('x, y, a')
            (x, y, a)
            sage: (x^5).list()
            [0, 0, 0, 0, 0, 1]
            sage: p = x - x^3 + 5/7*x^5
            sage: p.list()
            [0, 1, 0, -1, 0, 5/7]
            sage: p = expand((x-a*sqrt(2))^2 + x + 1); p
            -2*sqrt(2)*a*x + 2*a^2 + x^2 + x + 1
            sage: p.list(a)
            [x^2 + x + 1, -2*sqrt(2)*x, 2]
            sage: s = (1/(1-x)).series(x,6); s
            1 + 1*x + 1*x^2 + 1*x^3 + 1*x^4 + 1*x^5 + Order(x^6)
            sage: s.list()
            [1, 1, 1, 1, 1, 1]"""
    def log(self, b: CoercibleToExpression | None = None, hold: bool = False) -> Expression[P]:
        """
        Return the logarithm of ``self``.

        EXAMPLES::

            sage: x, y = var('x, y')
            sage: x.log()
            log(x)
            sage: (x^y + y^x).log()
            log(x^y + y^x)
            sage: SR(0).log()
            -Infinity
            sage: SR(-1).log()
            I*pi
            sage: SR(1).log()
            0
            sage: SR(1/2).log()
            log(1/2)
            sage: SR(0.5).log()
            -0.693147180559945
            sage: SR(0.5).log().exp()
            0.500000000000000
            sage: math.log(0.5)
            -0.6931471805599453
            sage: plot(lambda x: SR(x).log(), 0.1,10)                                   # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        To prevent automatic evaluation use the ``hold`` argument::

            sage: I.log()
            1/2*I*pi
            sage: I.log(hold=True)
            log(I)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = I.log(hold=True); a.unhold()
            1/2*I*pi

        The ``hold`` parameter also works in functional notation::

            sage: log(-1, hold=True)
            log(-1)
            sage: log(-1)
            I*pi

        TESTS::

            sage: SR(oo).log()
            +Infinity
            sage: SR(-oo).log()
            +Infinity
            sage: SR(unsigned_infinity).log()
            +Infinity"""
    def log_gamma(self, hold: bool = False) -> Expression[P]:
        """
        Return the log gamma function evaluated at ``self``.
        This is the logarithm of gamma of ``self``, where
        gamma is a complex function such that `gamma(n)`
        equals `factorial(n-1)`.

        EXAMPLES::

            sage: x = var('x')
            sage: x.log_gamma()
            log_gamma(x)
            sage: SR(2).log_gamma()
            0
            sage: SR(5).log_gamma()
            log(24)
            sage: a = SR(5).log_gamma(); a.n()
            3.17805383034795
            sage: SR(5-1).factorial().log()
            log(24)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(-1)
            sage: plot(lambda x: SR(x).log_gamma(), -7,8, plot_points=1000).show()      # needs sage.plot
            sage: math.exp(0.5)
            1.6487212707001282
            sage: plot(lambda x: (SR(x).exp() - SR(-x).exp())/2 - SR(x).sinh(), -1, 1)  # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(5).log_gamma(hold=True)
            log_gamma(5)

        To evaluate again, currently we must use numerical evaluation
        via :meth:`n`::

            sage: a = SR(5).log_gamma(hold=True); a.n()
            3.17805383034795"""
    def low_degree(self, s: CoercibleToExpression) ->  Expression[P]:
        """
        Return the exponent of the lowest power of ``s`` in ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: var('x,y,a')
            (x, y, a)
            sage: f = 100 + a*x + x^3*sin(x*y) + x*y + x/y^10 + 2*sin(x*y)/x; f
            x^3*sin(x*y) + a*x + x*y + 2*sin(x*y)/x + x/y^10 + 100
            sage: f.low_degree(x)
            -1
            sage: f.low_degree(y)
            -10
            sage: f.low_degree(sin(x*y))
            0
            sage: (x^3+y).low_degree(x)
            0
            sage: (x+x**2).low_degree(x)
            1"""
    def match(self, pattern: CoercibleToExpression) -> dict[Expression[P], Expression[P]]:
        """
        Check if ``self`` matches the given pattern.

        INPUT:

        - ``pattern`` -- a symbolic expression, possibly containing wildcards
          to match for

        OUTPUT:

        ``None`` if there is no match, or a dictionary mapping the
        wildcards to the matching values if a match was found. Note
        that the dictionary is empty if there were no wildcards in the
        given pattern.

        See also http://www.ginac.de/tutorial/Pattern-matching-and-advanced-substitutions.html

        EXAMPLES::

            sage: var('x,y,z,a,b,c,d,f,g')
            (x, y, z, a, b, c, d, f, g)
            sage: w0 = SR.wild(0); w1 = SR.wild(1); w2 = SR.wild(2)
            sage: ((x+y)^a).match((x+y)^a)  # no wildcards, so empty dict
            {}
            sage: print(((x+y)^a).match((x+y)^b))
            None
            sage: t = ((x+y)^a).match(w0^w1)
            sage: t[w0], t[w1]
            (x + y, a)
            sage: print(((x+y)^a).match(w0^w0))
            None
            sage: ((x+y)^(x+y)).match(w0^w0)
            {$0: x + y}
            sage: t = ((a+b)*(a+c)).match((a+w0)*(a+w1))
            sage: set([t[w0], t[w1]]) == set([b, c])
            True
            sage: ((a+b)*(a+c)).match((w0+b)*(w0+c))
            {$0: a}
            sage: t = ((a+b)*(a+c)).match((w0+w1)*(w0+w2))
            sage: t[w0]
            a
            sage: set([t[w1], t[w2]]) == set([b, c])
            True
            sage: t = ((a+b)*(a+c)).match((w0+w1)*(w1+w2))
            sage: t[w1]
            a
            sage: set([t[w0], t[w2]]) == set([b, c])
            True
            sage: t = (a*(x+y)+a*z+b).match(a*w0+w1)
            sage: s = set([t[w0], t[w1]])
            sage: s == set([x+y, a*z+b]) or s == set([z, a*(x+y)+b])
            True
            sage: print((a+b+c+d+f+g).match(c))
            None
            sage: (a+b+c+d+f+g).has(c)
            True
            sage: (a+b+c+d+f+g).match(c+w0)
            {$0: a + b + d + f + g}
            sage: (a+b+c+d+f+g).match(c+g+w0)
            {$0: a + b + d + f}
            sage: (a+b).match(a+b+w0) # known bug
            {$0: 0}
            sage: print((a*b^2).match(a^w0*b^w1))
            None
            sage: (a*b^2).match(a*b^w1)
            {$1: 2}
            sage: (x*x.arctan2(x^2)).match(w0*w0.arctan2(w0^2))
            {$0: x}

        Beware that behind-the-scenes simplification can lead to
        surprising results in matching::

            sage: print((x+x).match(w0+w1))
            None
            sage: t = x+x; t
            2*x
            sage: t.operator()
            <function mul_vararg ...>

        Since asking to match w0+w1 looks for an addition operator,
        there is no match."""
    def maxima_methods(self) -> MaximaWrapper:
        """
        Provide easy access to maxima methods, converting the result to a
        Sage expression automatically.

        EXAMPLES::

            sage: t = log(sqrt(2) - 1) + log(sqrt(2) + 1); t
            log(sqrt(2) + 1) + log(sqrt(2) - 1)
            sage: res = t.maxima_methods().logcontract(); res
            log((sqrt(2) + 1)*(sqrt(2) - 1))
            sage: type(res)
            <class 'sage.symbolic.expression.Expression'>"""
    # TODO this uses self.pyobject().minpoly or sage.calculus.calculus.minpoly
    def minpoly(
        self,  
        var: str = 'x', 
        algorithm = None, 
        bits = None, 
        degree = None, 
        epsilon: int = 0
    ) -> Any:
        """
        Return the minimal polynomial of this symbolic expression.

        EXAMPLES::

            sage: golden_ratio.minpoly()
            x^2 - x - 1"""
    def mul(self, *args: CoercibleToExpression, hold: bool = False) -> Expression[P]:
        """
        Return the product of the current expression and the given arguments.

        To prevent automatic evaluation use the ``hold`` argument.

        EXAMPLES::

            sage: x.mul(x)
            x^2
            sage: x.mul(x, hold=True)
            x*x
            sage: x.mul(x, (2+x), hold=True)
            (x + 2)*x*x
            sage: x.mul(x, (2+x), x, hold=True)
            (x + 2)*x*x*x
            sage: x.mul(x, (2+x), x, 2*x, hold=True)
            (2*x)*(x + 2)*x*x*x

        To then evaluate again, we use :meth:`unhold`::

            sage: a = x.mul(x, hold=True); a.unhold()
            x^2"""
    def multiply_both_sides(self, x, checksign: _NotUsed = None) -> Expression:
        """
        Return a relation obtained by multiplying both sides of this
        relation by ``x``.

        .. NOTE::

           The *checksign* keyword argument is currently ignored and
           is included for backward compatibility reasons only.

        EXAMPLES::

            sage: var('x,y'); f = x + 3 < y - 2
            (x, y)
            sage: f.multiply_both_sides(7)
            7*x + 21 < 7*y - 14
            sage: f.multiply_both_sides(-1/2)
            -1/2*x - 3/2 < -1/2*y + 1
            sage: f*(-2/3)
            -2/3*x - 2 < -2/3*y + 4/3
            sage: f*(-pi)
            -pi*(x + 3) < -pi*(y - 2)

        Since the direction of the inequality never changes when doing
        arithmetic with equations, you can multiply or divide the
        equation by a quantity with unknown sign::

            sage: f*(1+I)
            (I + 1)*x + 3*I + 3 < (I + 1)*y - 2*I - 2
            sage: f = sqrt(2) + x == y^3
            sage: f.multiply_both_sides(I)
            I*x + I*sqrt(2) == I*y^3
            sage: f.multiply_both_sides(-1)
            -x - sqrt(2) == -y^3

        Note that the direction of the following inequalities is
        not reversed::

            sage: (x^3 + 1 > 2*sqrt(3)) * (-1)
            -x^3 - 1 > -2*sqrt(3)
            sage: (x^3 + 1 >= 2*sqrt(3)) * (-1)
            -x^3 - 1 >= -2*sqrt(3)
            sage: (x^3 + 1 <= 2*sqrt(3)) * (-1)
            -x^3 - 1 <= -2*sqrt(3)"""
    def negation(self) -> Expression[P]:
        """
        Return the negated version of ``self``.

        This is the relation that is ``False`` iff ``self`` is ``True``.

        EXAMPLES::

            sage: (x < 5).negation()
            x >= 5
            sage: (x == sin(3)).negation()
            x != sin(3)
            sage: (2*x >= sqrt(2)).negation()
            2*x < sqrt(2)"""
    # TODO: this uses sage.calculus.calculus.nintegral
    def nintegral(
        self, 
        x,
        a,
        b,
        desired_relative_error: str = '1e-8',
        maximum_num_subintervals: int = 200
    ) -> Any:
        """
        Compute the numerical integral of ``self``.

        Please see :obj:`sage.calculus.calculus.nintegral` for more details.

        EXAMPLES::

            sage: sin(x).nintegral(x,0,3)
            (1.989992496600..., 2.209335488557...e-14, 21, 0)"""
        from sage.calculus.calculus import nintegral
    nintegrate = nintegral
    def norm(self) -> Expression[P]:
        """
        Return the complex norm of this symbolic expression, i.e.,
        the expression times its complex conjugate. If `c = a + bi` is a
        complex number, then the norm of `c` is defined as the product of
        `c` and its complex conjugate

        .. MATH::

            \\text{norm}(c)
            =
            \\text{norm}(a + bi)
            =
            c \\cdot \\overline{c}
            =
            a^2 + b^2.

        The norm of a complex number is different from its absolute value.
        The absolute value of a complex number is defined to be the square
        root of its norm. A typical use of the complex norm is in the
        integral domain `\\ZZ[i]` of Gaussian integers, where the norm of
        each Gaussian integer `c = a + bi` is defined as its complex norm.

        .. SEEALSO::

            :func:`sage.misc.functional.norm`

        EXAMPLES::

            sage: a = 1 + 2*I
            sage: a.norm()
            5
            sage: a = sqrt(2) + 3^(1/3)*I; a
            sqrt(2) + I*3^(1/3)
            sage: a.norm()
            3^(2/3) + 2
            sage: CDF(a).norm()
            4.080083823051...
            sage: CDF(a.norm())
            4.080083823051904"""
    def normalize(self) -> Expression[P]:
        """
        Return this expression normalized as a fraction.

        .. SEEALSO::

            :meth:`numerator`, :meth:`denominator`,
            :meth:`numerator_denominator`, :meth:`combine`

        EXAMPLES::

            sage: var('x, y, a, b, c')
            (x, y, a, b, c)
            sage: g = x + y/(x + 2)
            sage: g.normalize()
            (x^2 + 2*x + y)/(x + 2)

            sage: f = x*(x-1)/(x^2 - 7) + y^2/(x^2-7) + 1/(x+1) + b/a + c/a
            sage: f.normalize()
            (a*x^3 + b*x^3 + c*x^3 + a*x*y^2 + a*x^2 + b*x^2 + c*x^2 +
                    a*y^2 - a*x - 7*b*x - 7*c*x - 7*a - 7*b - 7*c)/((x^2 -
                        7)*a*(x + 1))

        TESTS:

        Check that :issue:`19775` is fixed::

            sage: a,b,c,d,e,y = var('a,b,c,d,e,y')
            sage: ((x - 2*y)^4/(x^2 - 4*y^2)^2).normalize()
            (x - 2*y)^2/(x + 2*y)^2
            sage: f = ((x - 2*y)^4/(x^2 - 4*y^2)^2 + 1)*(y + a)*(2*y + x) / (4*y^2 + x^2)
            sage: f.normalize()
            2*(a + y)/(x + 2*y)
            sage: (c/a - b*c^2/(a^2*(b*c/a-d)) + c*d/(a*(b*c/a-d))).normalize()
            0
            sage: (e + c/a - b*c^2/(a^2*(b*c/a-d)) + c*d/(a*(b*c/a-d))).normalize()
            e

        Check that :issue:`23861` is fixed::

            sage: (x^(2*pi) + x^(-2*pi) - 2).normalize()
            (x^(4*pi) - 2*x^(2*pi) + 1)/x^(2*pi)
            sage: (e^2 + e^(-2) - 2).normalize()
            (e^4 - 2*e^2 + 1)/e^2
            sage: (e^(2*pi) - e^(-2*pi)).normalize()
            (e^(4*pi) - 1)/e^(2*pi)

        ALGORITHM: Uses GiNaC."""
    def number_of_arguments(self) -> int:
        """
        EXAMPLES::

            sage: x,y = var('x,y')
            sage: f = x + y
            sage: f.number_of_arguments()
            2

            sage: g = f.function(x)
            sage: g.number_of_arguments()
            1

        ::

            sage: x,y,z = var('x,y,z')
            sage: (x+y).number_of_arguments()
            2
            sage: (x+1).number_of_arguments()
            1
            sage: (sin(x)+1).number_of_arguments()
            1
            sage: (sin(z)+x+y).number_of_arguments()
            3
            sage: (sin(x+y)).number_of_arguments()
            2"""
    def number_of_operands(self) -> int:
        """
        Return the number of operands of this expression.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: a.number_of_operands()
            0
            sage: (a^2 + b^2 + (x+y)^2).number_of_operands()
            3
            sage: (a^2).number_of_operands()
            2
            sage: (a*b^2*c).number_of_operands()
            3"""
    nops = number_of_operands
    def numerator(self, normalize: bool = True) -> Expression[P]:
        """
        Return the numerator of this symbolic expression.

        INPUT:

        - ``normalize`` -- boolean (default: ``True``)

        If ``normalize`` is ``True``, the expression is first normalized to
        have it as a fraction before getting the numerator.

        If ``normalize`` is ``False``, the expression is kept and if it is not
        a quotient, then this will return the expression itself.

        .. SEEALSO::

            :meth:`normalize`, :meth:`denominator`,
            :meth:`numerator_denominator`, :meth:`combine`

        EXAMPLES::

            sage: a, x, y = var('a,x,y')
            sage: f = x*(x-a)/((x^2 - y)*(x-a)); f
            x/(x^2 - y)
            sage: f.numerator()
            x
            sage: f.denominator()
            x^2 - y
            sage: f.numerator(normalize=False)
            x
            sage: f.denominator(normalize=False)
            x^2 - y

            sage: y = var('y')
            sage: g = x + y/(x + 2); g
            x + y/(x + 2)
            sage: g.numerator()
            x^2 + 2*x + y
            sage: g.denominator()
            x + 2
            sage: g.numerator(normalize=False)
            x + y/(x + 2)
            sage: g.denominator(normalize=False)
            1

        TESTS::

            sage: ((x+y)^2/(x-y)^3*x^3).numerator(normalize=False)
            (x + y)^2*x^3
            sage: ((x+y)^2*x^3).numerator(normalize=False)
            (x + y)^2*x^3
            sage: (y/x^3).numerator(normalize=False)
            y
            sage: t = y/x^3/(x+y)^(1/2); t
            y/(sqrt(x + y)*x^3)
            sage: t.numerator(normalize=False)
            y
            sage: (1/x^3).numerator(normalize=False)
            1
            sage: (x^3).numerator(normalize=False)
            x^3
            sage: (y*x^sin(x)).numerator(normalize=False)
            Traceback (most recent call last):
            ...
            TypeError: self is not a rational expression
            sage: n = var('n'); assume(n,'integer'); assume(n>0); (e^(2*n)/(e^(2*n) - 1)).numerator()
            e^(2*n)"""
    def numerator_denominator(self, normalize: bool = True) -> tuple[Expression[P], Expression[P]]:
        """
        Return the numerator and the denominator of this symbolic expression.

        INPUT:

        - ``normalize`` -- boolean (default: ``True``)

        If ``normalize`` is ``True``, the expression is first normalized to
        have it as a fraction before getting the numerator and denominator.

        If ``normalize`` is ``False``, the expression is kept and if it is not
        a quotient, then this will return the expression itself together with
        1.

        .. SEEALSO::

            :meth:`normalize`, :meth:`numerator`, :meth:`denominator`,
            :meth:`combine`

        EXAMPLES::

            sage: x, y, a = var("x y a")
            sage: ((x+y)^2/(x-y)^3*x^3).numerator_denominator()
            ((x + y)^2*x^3, (x - y)^3)

            sage: ((x+y)^2/(x-y)^3*x^3).numerator_denominator(False)
            ((x + y)^2*x^3, (x - y)^3)

            sage: g = x + y/(x + 2)
            sage: g.numerator_denominator()
            (x^2 + 2*x + y, x + 2)
            sage: g.numerator_denominator(normalize=False)
            (x + y/(x + 2), 1)

            sage: g = x^2*(x + 2)
            sage: g.numerator_denominator()
            ((x + 2)*x^2, 1)
            sage: g.numerator_denominator(normalize=False)
            ((x + 2)*x^2, 1)

        TESTS::

            sage: ((x+y)^2/(x-y)^3*x^3).numerator_denominator(normalize=False)
            ((x + y)^2*x^3, (x - y)^3)
            sage: ((x+y)^2*x^3).numerator_denominator(normalize=False)
            ((x + y)^2*x^3, 1)
            sage: (y/x^3).numerator_denominator(normalize=False)
            (y, x^3)
            sage: t = y/x^3/(x+y)^(1/2); t
            y/(sqrt(x + y)*x^3)
            sage: t.numerator_denominator(normalize=False)
            (y, sqrt(x + y)*x^3)
            sage: (1/x^3).numerator_denominator(normalize=False)
            (1, x^3)
            sage: (x^3).numerator_denominator(normalize=False)
            (x^3, 1)
            sage: (y*x^sin(x)).numerator_denominator(normalize=False)
            Traceback (most recent call last):
            ...
            TypeError: self is not a rational expression"""
    @overload
    def numerical_approx(
        self, *, digits=None, algorithm=None
    ) -> RealNumber | ComplexNumber: ...
    @overload
    def numerical_approx(
        self, prec: SupportsInt = 53, *, algorithm=None
    ) -> RealNumber | ComplexNumber:
        """
        Return a numerical approximation of ``self`` with ``prec`` bits
        (or decimal ``digits``) of precision.

        No guarantee is made about the accuracy of the result.

        INPUT:

        - ``prec`` -- precision in bits

        - ``digits`` -- precision in decimal digits (only used if
          ``prec`` is not given)

        - ``algorithm`` -- which algorithm to use to compute this
          approximation

        If neither ``prec`` nor ``digits`` is given, the default
        precision is 53 bits (roughly 16 digits).

        EXAMPLES::

            sage: sin(x).subs(x=5).n()
            -0.958924274663138
            sage: sin(x).subs(x=5).n(100)
            -0.95892427466313846889315440616
            sage: sin(x).subs(x=5).n(digits=50)
            -0.95892427466313846889315440615599397335246154396460
            sage: zeta(x).subs(x=2).numerical_approx(digits=50)
            1.6449340668482264364724151666460251892189499012068

            sage: cos(3).numerical_approx(200)
            -0.98999249660044545727157279473126130239367909661558832881409
            sage: numerical_approx(cos(3),200)
            -0.98999249660044545727157279473126130239367909661558832881409
            sage: numerical_approx(cos(3), digits=10)
            -0.9899924966
            sage: (i + 1).numerical_approx(32)
            1.00000000 + 1.00000000*I
            sage: (pi + e + sqrt(2)).numerical_approx(100)
            7.2740880444219335226246195788

        TESTS:

        We test the evaluation of different infinities available in Pynac::

            sage: t = x - oo; t
            -Infinity
            sage: t.n()
            -infinity
            sage: t = x + oo; t
            +Infinity
            sage: t.n()
            +infinity
            sage: t = x - unsigned_infinity; t
            Infinity
            sage: t.n()
            Traceback (most recent call last):
            ...
            ValueError: can only convert signed infinity to RR

        Some expressions cannot be evaluated numerically::

            sage: n(sin(x))
            Traceback (most recent call last):
            ...
            TypeError: cannot evaluate symbolic expression numerically
            sage: a = var('a')
            sage: (x^2 + 2*x + 2).subs(x=a).n()
            Traceback (most recent call last):
            ...
            TypeError: cannot evaluate symbolic expression numerically

        Make sure we've rounded up log(10,2) enough to guarantee
        sufficient precision (:issue:`10164`)::

            sage: ks = 4*10**5, 10**6
            sage: all(len(str(e.n(digits=k)))-1 >= k for k in ks)
            True

        Symbolic sums with definite endpoints are expanded (:issue:`9424`)::

            sage: (k,n) = var('k,n')
            sage: f(n) = sum(abs(-k*k+n),k,1,n)
            sage: ex = f(n=8); ex
            sum(abs(-k^2 + 8), k, 1, 8)
            sage: ex.n()
            162.000000000000
            sage: (ex+1).n()
            163.000000000000

        Check if :issue:`24418` is fixed::

            sage: numerical_approx(2^(450232897/4888643760))
            1.06591892580915"""
    @property
    def op(self) -> OperandsWrapper:
        """
        Provide access to the operands of an expression through a property.

        EXAMPLES::

            sage: t = 1+x+x^2
            sage: t.op
            Operands of x^2 + x + 1
            sage: x.op
            Traceback (most recent call last):
            ...
            TypeError: expressions containing only a numeric coefficient,
            constant or symbol have no operands
            sage: t.op[0]
            x^2

        Indexing directly with ``t[1]`` causes problems with numpy types.

            sage: t[1]
            Traceback (most recent call last):
            ...
            TypeError: 'sage.symbolic.expression.Expression' object ...
        """
    def operands(self) -> list[Expression[SymbolicRing]]:
        """
        Return a list containing the operands of this expression.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: (a^2 + b^2 + (x+y)^2).operands()
            [a^2, b^2, (x + y)^2]
            sage: (a^2).operands()
            [a, 2]
            sage: (a*b^2*c).operands()
            [a, b^2, c]"""
    def operator(self) -> _Operator:
        """
        Return the topmost operator in this expression.

        EXAMPLES::

            sage: x,y,z = var('x,y,z')
            sage: (x+y).operator()
            <function add_vararg ...>
            sage: (x^y).operator()
            <built-in function pow>
            sage: (x^y * z).operator()
            <function mul_vararg ...>
            sage: (x < y).operator()
            <built-in function lt>

            sage: abs(x).operator()
            abs
            sage: r = gamma(x).operator(); type(r)
            <class 'sage.functions.gamma.Function_gamma'>

            sage: psi = function('psi', nargs=1)
            sage: psi(x).operator()
            psi

            sage: r = psi(x).operator()
            sage: r == psi
            True

            sage: f = function('f', nargs=1, conjugate_func=lambda self, x: 2*x)
            sage: nf = f(x).operator()
            sage: nf(x).conjugate()
            2*x

            sage: f = function('f')
            sage: a = f(x).diff(x); a
            diff(f(x), x)
            sage: a.operator()
            D[0](f)

        TESTS::

            sage: (x <= y).operator()
            <built-in function le>
            sage: (x == y).operator()
            <built-in function eq>
            sage: (x != y).operator()
            <built-in function ne>
            sage: (x > y).operator()
            <built-in function gt>
            sage: (x >= y).operator()
            <built-in function ge>
            sage: SR._force_pyobject( (x, x + 1, x + 2) ).operator()
            <... 'tuple'>
            sage: exp(x).series(x,3).operator()
            <function add_vararg ...>"""
    def partial_fraction(self, var: str | None = None) -> Expression[P]:
        """
        Return the partial fraction expansion of ``self`` with
        respect to the given variable.

        INPUT:

        - ``var`` -- variable name or string (default: first variable)

        OUTPUT: a symbolic expression

        .. SEEALSO:: :meth:`partial_fraction_decomposition`

        EXAMPLES::

            sage: f = x^2/(x+1)^3
            sage: f.partial_fraction()
            1/(x + 1) - 2/(x + 1)^2 + 1/(x + 1)^3

        Notice that the first variable in the expression is used by
        default::

            sage: y = var('y')
            sage: f = y^2/(y+1)^3
            sage: f.partial_fraction()
            1/(y + 1) - 2/(y + 1)^2 + 1/(y + 1)^3

            sage: f = y^2/(y+1)^3 + x/(x-1)^3
            sage: f.partial_fraction()
            y^2/(y^3 + 3*y^2 + 3*y + 1) + 1/(x - 1)^2 + 1/(x - 1)^3

        You can explicitly specify which variable is used::

            sage: f.partial_fraction(y)
            x/(x^3 - 3*x^2 + 3*x - 1) + 1/(y + 1) - 2/(y + 1)^2 + 1/(y + 1)^3"""
    def partial_fraction_decomposition(self, var: str | None = None) -> list[Expression[P]]:
        """
        Return the partial fraction decomposition of ``self`` with
        respect to the given variable.

        INPUT:

        - ``var`` -- variable name or string (default: first variable)

        OUTPUT: list of symbolic expressions

        .. SEEALSO:: :meth:`partial_fraction`

        EXAMPLES::

            sage: f = x^2/(x+1)^3
            sage: f.partial_fraction_decomposition()
            [1/(x + 1), -2/(x + 1)^2, (x + 1)^(-3)]
            sage: (4+f).partial_fraction_decomposition()
            [1/(x + 1), -2/(x + 1)^2, (x + 1)^(-3), 4]

        Notice that the first variable in the expression is used by
        default::

            sage: y = var('y')
            sage: f = y^2/(y+1)^3
            sage: f.partial_fraction_decomposition()
            [1/(y + 1), -2/(y + 1)^2, (y + 1)^(-3)]

            sage: f = y^2/(y+1)^3 + x/(x-1)^3
            sage: f.partial_fraction_decomposition()
            [y^2/(y^3 + 3*y^2 + 3*y + 1), (x - 1)^(-2), (x - 1)^(-3)]

        You can explicitly specify which variable is used::

            sage: f.partial_fraction_decomposition(y)
            [1/(y + 1), -2/(y + 1)^2, (y + 1)^(-3), x/(x^3 - 3*x^2 + 3*x - 1)]"""
    def plot(self, *args, **kwds) -> Any:
        """
        Plot a symbolic expression. All arguments are passed onto the standard :func:`plot` command.

        EXAMPLES:

        This displays a straight line::

            sage: sin(2).plot((x,0,3))                                                  # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        This draws a red oscillatory curve::

            sage: sin(x^2).plot((x,0,2*pi), rgbcolor=(1,0,0))                           # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Another plot using the variable theta::

            sage: var(\'theta\')
            theta
            sage: (cos(theta) - erf(theta)).plot((theta,-2*pi,2*pi))                    # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        A very thick green plot with a frame::

            sage: sin(x).plot((x, -4*pi, 4*pi),                                         # needs sage.plot
            ....:             thickness=20, rgbcolor=(0,0.7,0)).show(frame=True)

        You can embed 2d plots in 3d space as follows::

            sage: plot(sin(x^2), (x, -pi, pi), thickness=2).plot3d(z=1)         # long time, needs sage.plot
            Graphics3d Object

        A more complicated family::

            sage: G = sum(plot(sin(n*x), (x, -2*pi, 2*pi)).plot3d(z=n)                  # needs sage.plot
            ....:         for n in [0,0.1,..1])
            sage: G.show(frame_aspect_ratio=[1,1,1/2])  # long time (5s on sage.math, 2012), needs sage.plot

        A plot involving the floor function::

            sage: plot(1.0 - x * floor(1/x), (x,0.00001,1.0))                           # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        Sage used to allow symbolic functions with "no arguments";
        this no longer works::

            sage: plot(2*sin, -4, 4)                                                    # needs sage.plot
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            \'Integer Ring\' and \'<class \'sage.functions.trig.Function_sin\'>\'

        You should evaluate the function first::

            sage: plot(2*sin(x), -4, 4)                                                 # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        TESTS::

            sage: f(x) = x*(1 - x)
            sage: plot(f, 0, 1)                                                         # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    def poly(self, x: CoercibleToExpression | None = None) ->  Expression[SymbolicRing]:
        """
        Express this symbolic expression as a polynomial in *x*. If
        this is not a polynomial in *x*, then some coefficients may be
        functions of *x*.

        .. warning::

           This is different from :meth:`polynomial` which returns
           a Sage polynomial over a given base ring.

        EXAMPLES::

            sage: var('a, x')
            (a, x)
            sage: p = expand((x-a*sqrt(2))^2 + x + 1); p
            -2*sqrt(2)*a*x + 2*a^2 + x^2 + x + 1
            sage: p.poly(a)
            -2*sqrt(2)*a*x + 2*a^2 + x^2 + x + 1
            sage: bool(p.poly(a) == (x-a*sqrt(2))^2 + x + 1)
            True
            sage: p.poly(x)
            2*a^2 - (2*sqrt(2)*a - 1)*x + x^2 + 1"""
    @overload
    def polynomial(self, base_ring: Ring = ...) -> CommutativePolynomial: ...
    @overload
    def polynomial(self, base_ring: None = None, ring: Ring = ...) -> CommutativePolynomial:
        """
        Return this symbolic expression as an algebraic polynomial
        over the given base ring, if possible.

        The point of this function is that it converts purely symbolic
        polynomials into optimised algebraic polynomials over a given
        base ring.

        You can specify either the base ring (``base_ring``) you want
        the output polynomial to be over, or you can specify the full
        polynomial ring (``ring``) you want the output polynomial to
        be an element of.

        INPUT:

        - ``base_ring`` -- (optional) the base ring for the polynomial

        - ``ring`` -- (optional) the parent for the polynomial

        .. warning::

           This is different from :meth:`poly` which is used to rewrite
           ``self`` as a polynomial in terms of one of the variables.

        EXAMPLES::

            sage: f = x^2 -2/3*x + 1
            sage: f.polynomial(QQ)
            x^2 - 2/3*x + 1
            sage: f.polynomial(GF(19))
            x^2 + 12*x + 1

        Polynomials can be useful for getting the coefficients of an
        expression::

            sage: g = 6*x^2 - 5
            sage: g.coefficients()
            [[-5, 0], [6, 2]]
            sage: g.polynomial(QQ).list()
            [-5, 0, 6]
            sage: g.polynomial(QQ).monomial_coefficients()
            {0: -5, 2: 6}

        ::

            sage: f = x^2*e + x + pi/e
            sage: f.polynomial(RDF)  # abs tol 5e-16
            2.718281828459045*x^2 + x + 1.1557273497909217
            sage: g = f.polynomial(RR); g
            2.71828182845905*x^2 + x + 1.15572734979092
            sage: g.parent()
            Univariate Polynomial Ring in x over Real Field with 53 bits of precision
            sage: f.polynomial(RealField(100))
            2.7182818284590452353602874714*x^2 + x + 1.1557273497909217179100931833
            sage: f.polynomial(CDF)  # abs tol 5e-16
            2.718281828459045*x^2 + x + 1.1557273497909217
            sage: f.polynomial(CC)
            2.71828182845905*x^2 + x + 1.15572734979092

        We coerce a multivariate polynomial with complex symbolic
        coefficients::

            sage: x, y, n = var(\'x, y, n\')
            sage: f = pi^3*x - y^2*e - I; f
            pi^3*x - y^2*e - I
            sage: f.polynomial(CDF)  # abs tol 1e-15
            (-2.718281828459045)*y^2 + 31.006276680299816*x - 1.0*I
            sage: f.polynomial(CC)
            (-2.71828182845905)*y^2 + 31.0062766802998*x - 1.00000000000000*I
            sage: f.polynomial(ComplexField(70))
            (-2.7182818284590452354)*y^2 + 31.006276680299820175*x - 1.0000000000000000000*I

        Another polynomial::

            sage: f = sum((e*I)^n*x^n for n in range(5)); f
            x^4*e^4 - I*x^3*e^3 - x^2*e^2 + I*x*e + 1
            sage: f.polynomial(CDF)   # abs tol 5e-16
            54.598150033144236*x^4 - 20.085536923187668*I*x^3 - 7.38905609893065*x^2
             + 2.718281828459045*I*x + 1.0
            sage: f.polynomial(CC)
            54.5981500331442*x^4 - 20.0855369231877*I*x^3 - 7.38905609893065*x^2
             + 2.71828182845905*I*x + 1.00000000000000

        A multivariate polynomial over a finite field::

            sage: f = (3*x^5 - 5*y^5)^7; f
            (3*x^5 - 5*y^5)^7
            sage: g = f.polynomial(GF(7)); g
            3*x^35 + 2*y^35
            sage: parent(g)
            Multivariate Polynomial Ring in x, y over Finite Field of size 7

        We check to make sure constants are converted appropriately::

            sage: (pi*x).polynomial(SR)
            pi*x

        Using the ``ring`` parameter, you can also create polynomials
        rings over the symbolic ring where only certain variables are
        considered generators of the polynomial ring and the others
        are considered "constants"::

            sage: a, x, y = var(\'a,x,y\')
            sage: f = a*x^10*y+3*x
            sage: B = f.polynomial(ring=SR[\'x,y\'])
            sage: B.coefficients()
            [a, 3]"""
    def power(self, exp: CoercibleToExpression, hold: bool = False) -> Expression[P]:
        """
        Return the current expression to the power ``exp``.

        To prevent automatic evaluation use the ``hold`` argument.

        EXAMPLES::

            sage: (x^2).power(2)
            x^4
            sage: (x^2).power(2, hold=True)
            (x^2)^2

        To then evaluate again, we use :meth:`unhold`::

            sage: a = (x^2).power(2, hold=True); a.unhold()
            x^4"""
    def power_series(self, base_ring: Ring) -> PowerSeries:
        """
        Return algebraic power series associated to this symbolic
        expression, which must be a polynomial in one variable, with
        coefficients coercible to the base ring.

        The power series is truncated one more than the degree.

        EXAMPLES::

            sage: theta = var('theta')
            sage: f = theta^3 + (1/3)*theta - 17/3
            sage: g = f.power_series(QQ); g
            -17/3 + 1/3*theta + theta^3 + O(theta^4)
            sage: g^3
            -4913/27 + 289/9*theta - 17/9*theta^2 + 2602/27*theta^3 + O(theta^4)
            sage: g.parent()
            Power Series Ring in theta over Rational Field"""
    def primitive_part(self, s: CoercibleToExpression) ->  Expression[P]:
        """
        Return the primitive polynomial of this expression when
        considered as a polynomial in ``s``.

        See also :meth:`unit`, :meth:`content`, and
        :meth:`unit_content_primitive`.

        INPUT:

        - ``s`` -- a symbolic expression

        OUTPUT:

        The primitive polynomial as a symbolic expression. It is
        defined as the quotient by the :meth:`unit` and
        :meth:`content` parts (with respect to the variable ``s``).

        EXAMPLES::

            sage: (2*x+4).primitive_part(x)
            x + 2
            sage: (2*x+1).primitive_part(x)
            2*x + 1
            sage: (2*x+1/2).primitive_part(x)
            4*x + 1
            sage: var('y')
            y
            sage: (2*x + 4*sin(y)).primitive_part(sin(y))
            x + 2*sin(y)"""
    # TODO: this uses sage.calculus.calculus.symbolic_product
    def prod(self, *args, **kwds) -> Any:
        """
        Return the symbolic product `\\prod_{v = a}^b` ``self``.

        This is the product respect to the variable `v` with endpoints `a` and `b`.

        INPUT:

        - ``expression`` -- a symbolic expression

        - ``v`` -- a variable or variable name

        - ``a`` -- lower endpoint of the product

        - ``b`` -- upper endpoint of the product

        - ``algorithm`` -- (default: ``'maxima'``)  one of

          - ``'maxima'`` -- use Maxima (the default)
          - ``'giac'`` -- (optional) use Giac
          - ``'sympy'`` -- use SymPy

        - ``hold`` -- boolean (default: ``False``); if ``True``, don't evaluate

        TESTS:

            sage: i, k, n = var('i,k,n')
            sage: k.prod(k, 1, n)
            factorial(n)
            sage: (x + i*(i+1)/2).prod(i,1,4)
            x^4 + 20*x^3 + 127*x^2 + 288*x + 180
            sage: (i^2).prod(i,1,7)
            25401600
            sage: f = function('f')
            sage: f(i).prod(i,1,7)
            f(7)*f(6)*f(5)*f(4)*f(3)*f(2)*f(1)
            sage: f(i).prod(i,1,n)
            product(f(i), i, 1, n)
            sage: assume(k>0)
            sage: (x^k).integrate(x,0,1).prod(k,1,n)
            1/factorial(n + 1)
            sage: f(i).prod(i,1,n).log().log_expand()
            sum(log(f(i)), i, 1, n)"""
    def pyobject(self) -> object:
        """
        Get the underlying Python object.

        OUTPUT:

        The Python object corresponding to this expression, assuming
        this expression is a single numerical value or an infinity
        representable in Python. Otherwise, a :exc:`TypeError` is raised.

        EXAMPLES::

            sage: var('x')
            x
            sage: b = -17.3
            sage: a = SR(b)
            sage: a.pyobject()
            -17.3000000000000
            sage: a.pyobject() is b
            True

        Integers and Rationals are converted internally though, so you
        won't get back the same object::

            sage: b = -17/3
            sage: a = SR(b)
            sage: a.pyobject()
            -17/3
            sage: a.pyobject() is b
            False

        TESTS::

            sage: SR(oo).pyobject()
            +Infinity
            sage: SR(-oo).pyobject()
            -Infinity
            sage: SR(unsigned_infinity).pyobject()
            Infinity
            sage: SR(I*oo).pyobject()
            Traceback (most recent call last):
            ...
            TypeError: Python infinity cannot have complex phase."""
    def real_part(self) -> Expression[P]:
        """
        Return the real part of this symbolic expression.

        EXAMPLES::

            sage: x = var('x')
            sage: x.real_part()
            real_part(x)
            sage: SR(2+3*I).real_part()
            2
            sage: SR(CDF(2,3)).real_part()
            2.0
            sage: SR(CC(2,3)).real_part()
            2.00000000000000

            sage: f = log(x)
            sage: f.real_part()
            log(abs(x))

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(2).real_part()
            2
            sage: SR(2).real_part(hold=True)
            real_part(2)

        This also works using functional notation::

            sage: real_part(I,hold=True)
            real_part(I)
            sage: real_part(I)
            0

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(2).real_part(hold=True); a.unhold()
            2

        TESTS:

        Check that :issue:`12807` is fixed::

            sage: (6*exp(i*pi/3)-6*exp(i*2*pi/3)).real_part()
            6

        Check that :issue:`28357` is fixed::

            sage: m = var('m')
            sage: assume(m, 'integer')
            sage: (I^m).real_part()
            cos(1/2*pi*m)
            sage: (I^m).imag_part()
            sin(1/2*pi*m)
            sage: forget()

        Check that :issue:`29400` is fixed::

            sage: cot(1 + i).imag().n() - (1/tan(1 + i)).imag().n()  # abs tol 10^-12
            0.00000000000000"""
    real = real_part
    def rectform(self) -> Expression:
        """
        Convert this symbolic expression to rectangular form; that
        is, the form `a + bi` where `a` and `b` are real numbers and
        `i` is the imaginary unit.

        .. NOTE::

           The name \\"rectangular\\" comes from the fact that, in the
           complex plane, `a` and `bi` are perpendicular.

        INPUT:

        - ``self`` -- the expression to convert

        OUTPUT:

        A new expression, equivalent to the original, but expressed in
        the form `a + bi`.

        ALGORITHM:

        We call Maxima\'s ``rectform()`` and return the result unmodified.

        EXAMPLES:

        The exponential form of `\\sin(x)`::

            sage: f = (e^(I*x) - e^(-I*x)) / (2*I)
            sage: f.rectform()
            sin(x)

        And `\\cos(x)`::

            sage: f = (e^(I*x) + e^(-I*x)) / 2
            sage: f.rectform()
            cos(x)

        In some cases, this will simplify the given expression. For
        example, here, `e^{ik\\pi}`, `\\sin(k\\pi)=0` should cancel
        leaving only `\\cos(k\\pi)` which can then be simplified::

            sage: k = var(\'k\')
            sage: assume(k, \'integer\')
            sage: f = e^(I*pi*k)
            sage: f.rectform()
            (-1)^k

        However, in general, the resulting expression may be more
        complicated than the original::

            sage: f = e^(I*x)
            sage: f.rectform()
            cos(x) + I*sin(x)

        TESTS:

        If the expression is already in rectangular form, it should be
        left alone::

            sage: a,b = var(\'a,b\')
            sage: assume((a, \'real\'), (b, \'real\'))
            sage: f = a + b*I
            sage: f.rectform()
            a + I*b
            sage: forget()

        We can check with specific real numbers::

            sage: a = RR.random_element()
            sage: b = RR.random_element()
            sage: f = SR(a + b*I)
            sage: abs(f.rectform() - (a + b*I))  # abs tol 1e-16
            0.0

        If we decompose a complex number into its real and imaginary
        parts, they should correspond to the real and imaginary terms
        of the rectangular form::

            sage: z = CC.random_element()
            sage: a = z.real_part()
            sage: b = z.imag_part()
            sage: abs(SR(z).rectform() - (a + b*I))  # abs tol 1e-16
            0.0"""
    def reduce_trig(self, var: object | None = None) -> Expression[P]:
        """
        Combine products and powers of trigonometric and hyperbolic
        sin's and cos's of x into those of multiples of x. It also
        tries to eliminate these functions when they occur in
        denominators.

        INPUT:

        - ``self`` -- a symbolic expression

        - ``var`` -- (default: ``None``) the variable which is used for
          these transformations. If not specified, all variables are
          used.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: y = var('y')
            sage: f = sin(x)*cos(x)^3+sin(y)^2
            sage: f.reduce_trig()
            -1/2*cos(2*y) + 1/8*sin(4*x) + 1/4*sin(2*x) + 1/2

        To reduce only the expressions involving x we use optional parameter::

            sage: f.reduce_trig(x)
            sin(y)^2 + 1/8*sin(4*x) + 1/4*sin(2*x)

        ALIAS: :meth:`trig_reduce` and :meth:`reduce_trig` are the same"""
    trig_reduce = reduce_trig
    def residue(self, symbol: Expression) -> Any:   # TODO: returns a coefficient of SymbolicSeries
        """
        Calculate the residue of ``self`` with respect to ``symbol``.

        INPUT:

        - ``symbol`` -- a symbolic variable or symbolic equality such
          as ``x == 5``. If an equality is given, the expansion is
          around the value on the right hand side of the equality,
          otherwise at ``0``.

        OUTPUT: the residue of ``self``

        Say, ``symbol`` is ``x == a``, then this function calculates
        the residue of ``self`` at `x=a`, i.e., the coefficient of
        `1/(x-a)` of the series expansion of ``self`` around `a`.

        EXAMPLES::

            sage: (1/x).residue(x == 0)
            1
            sage: (1/x).residue(x == oo)
            -1
            sage: (1/x^2).residue(x == 0)
            0
            sage: (1/sin(x)).residue(x == 0)
            1
            sage: var('q, n, z')
            (q, n, z)
            sage: (-z^(-n-1)/(1-z/q)^2).residue(z == q).simplify_full()
            (n + 1)/q^n
            sage: var('s')
            s
            sage: zeta(s).residue(s == 1)
            1

        We can also compute the residue at more general places,
        given that the pole is recognized::

            sage: k = var('k', domain='integer')
            sage: (gamma(1+x)/(1 - exp(-x))).residue(x==2*I*pi*k)
            gamma(2*I*pi*k + 1)
            sage: csc(x).residue(x==2*pi*k)
            1

        TESTS::

            sage: (exp(x)/sin(x)^4).residue(x == 0)
            5/6

        Check that :issue:`18372` is resolved::

            sage: (1/(x^2 - x - 1)).residue(x == 1/2*sqrt(5) + 1/2)
            1/5*sqrt(5)

        Check that :issue:`20084` is fixed::

            sage: (1/(1 - 2^-x)).residue(x == 2*pi*I/log(2))
            1/log(2)"""
    def resultant(
        self, other: CoercibleToExpression, var: CoercibleToExpression
    ) -> Expression[P]:
        """
        Compute the resultant of this polynomial expression and the first
        argument with respect to the variable given as the second
        argument.

        EXAMPLES::

            sage: _ = var('a b n k u x y')
            sage: x.resultant(y, x)
            y
            sage: (x+y).resultant(x-y, x)
            -2*y
            sage: r = (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)
            sage: r.coefficient(a^4)
            b^4*y^2 - 4*b^3*y^3 + 6*b^2*y^4 - 4*b*y^5 + y^6
            sage: x.resultant(sin(x), x)
            Traceback (most recent call last):
            ...
            RuntimeError: resultant(): arguments must be polynomials"""
    def right_hand_side(self) -> Expression[P]:
        """
        If ``self`` is a relational expression, return the right hand side
        of the relation.  Otherwise, raise a :exc:`ValueError`.

        EXAMPLES::

            sage: x = var('x')
            sage: eqn = (x-1)^2 <= x^2 - 2*x + 3
            sage: eqn.right_hand_side()
            x^2 - 2*x + 3
            sage: eqn.rhs()
            x^2 - 2*x + 3
            sage: eqn.right()
            x^2 - 2*x + 3"""
    rhs = right_hand_side
    right = right_hand_side
    # TODO: the return type shall be checking every ring's root algorithm 
    #       when ring is not None ; when ring is None, this use self.solve()
    @overload
    def roots(
        self, 
        x: None = None, 
        explicit_solutions: bool = True, 
        multiplicities: Literal[True] = True, 
        ring: Ring | None = None
    ) -> Any: ...
    @overload
    def roots(
        self, 
        x: None = None, 
        explicit_solutions: bool = True, 
        multiplicities: Literal[False] = ..., 
        ring: Ring | None = None
    ) -> Any:
        """
        Return roots of ``self`` that can be found exactly,
        possibly with multiplicities.  Not all roots are guaranteed to
        be found.

        .. warning::

           This is *not* a numerical solver - use :meth:`find_root` to
           solve for ``self == 0`` numerically on an interval.

        INPUT:

        - ``x`` -- variable to view the function in terms of
          (use default variable if not given)

        - ``explicit_solutions`` -- boolean (default: ``True``); require that
          roots be explicit rather than implicit

        - ``multiplicities`` -- boolean (default: ``True``); when ``True``, return
          multiplicities

        - ``ring`` -- a ring (default: ``None``); if not ``None``, convert
          ``self`` to a polynomial over ``ring`` and find roots over ``ring``

        OUTPUT:

        A list of pairs ``(root, multiplicity)`` or list of roots.

        If there are infinitely many roots, e.g., a function like
        `\\sin(x)`, only one is returned.

        EXAMPLES::

            sage: var('x, a')
            (x, a)

        A simple example::

            sage: ((x^2-1)^2).roots()
            [(-1, 2), (1, 2)]
            sage: ((x^2-1)^2).roots(multiplicities=False)
            [-1, 1]

        A complicated example::

            sage: f = expand((x^2 - 1)^3*(x^2 + 1)*(x-a)); f
            -a*x^8 + x^9 + 2*a*x^6 - 2*x^7 - 2*a*x^2 + 2*x^3 + a - x

        The default variable is `a`, since it is the first in
        alphabetical order::

            sage: f.roots()
            [(x, 1)]

        As a polynomial in `a`, `x` is indeed a root::

            sage: f.poly(a)
            x^9 - 2*x^7 + 2*x^3 - (x^8 - 2*x^6 + 2*x^2 - 1)*a - x
            sage: f(a=x)
            0

        The roots in terms of `x` are what we expect::

            sage: f.roots(x)
            [(a, 1), (-I, 1), (I, 1), (1, 3), (-1, 3)]

        Only one root of `\\sin(x) = 0` is given::

            sage: f = sin(x)
            sage: f.roots(x)
            [(0, 1)]

        .. NOTE::

            It is possible to solve a greater variety of equations
            using :func:`solve` and the keyword ``to_poly_solve``,
            but only at the price of possibly encountering
            approximate solutions.  See documentation for :meth:`solve`
            for more details.

        We derive the roots of a general quadratic polynomial::

            sage: var('a,b,c,x')
            (a, b, c, x)
            sage: (a*x^2 + b*x + c).roots(x)
            [(-1/2*(b + sqrt(b^2 - 4*a*c))/a, 1), (-1/2*(b - sqrt(b^2 - 4*a*c))/a, 1)]

        By default, all the roots are required to be explicit rather than
        implicit. To get implicit roots, pass ``explicit_solutions=False``
        to ``.roots()`` ::

            sage: var('x')
            x
            sage: f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)
            sage: f.roots()
            Traceback (most recent call last):
            ...
            RuntimeError: no explicit roots found
            sage: f.roots(explicit_solutions=False)
            [((2^(8/9) + x^(8/9) - 2^(1/9) - x^(1/9))/(2^(8/9) - 2^(1/9)), 1)]

        Another example, but involving a degree 5 poly whose roots do not
        get computed explicitly::

            sage: f = x^5 + x^3 + 17*x + 1
            sage: f.roots()
            Traceback (most recent call last):
            ...
            RuntimeError: no explicit roots found
            sage: f.roots(explicit_solutions=False)
            [(x^5 + x^3 + 17*x + 1, 1)]
            sage: f.roots(explicit_solutions=False, multiplicities=False)
            [x^5 + x^3 + 17*x + 1]

        Now let us find some roots over different rings::

            sage: f.roots(ring=CC)
            [(-0.0588115223184..., 1),
             (-1.331099917875... - 1.52241655183732*I, 1),
             (-1.331099917875... + 1.52241655183732*I, 1),
             (1.36050567903502 - 1.51880872209965*I, 1),
             (1.36050567903502 + 1.51880872209965*I, 1)]
            sage: (2.5*f).roots(ring=RR)
            [(-0.058811522318449..., 1)]
            sage: f.roots(ring=CC, multiplicities=False)
            [-0.05881152231844...,
             -1.331099917875... - 1.52241655183732*I,
             -1.331099917875... + 1.52241655183732*I,
             1.36050567903502 - 1.51880872209965*I,
             1.36050567903502 + 1.51880872209965*I]
            sage: f.roots(ring=QQ)
            []
            sage: f.roots(ring=QQbar, multiplicities=False)
            [-0.05881152231844944?,
             -1.331099917875796? - 1.522416551837318?*I,
             -1.331099917875796? + 1.522416551837318?*I,
             1.360505679035020? - 1.518808722099650?*I,
             1.360505679035020? + 1.518808722099650?*I]

        Root finding over finite fields::

            sage: f.roots(ring=GF(7^2, 'a'))                                            # needs sage.rings.finite_rings
            [(3, 1), (4*a + 6, 2), (3*a + 3, 2)]

        TESTS::

            sage: (sqrt(3) * f).roots(ring=QQ)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert sqrt(3) to a rational

        Check if :issue:`9538` is fixed::

            sage: var('f6,f5,f4,x')
            (f6, f5, f4, x)
            sage: e = 15*f6*x^2 + 5*f5*x + f4
            sage: res = e.roots(x); res
            [(-1/30*(5*f5 + sqrt(25*f5^2 - 60*f4*f6))/f6, 1),
             (-1/30*(5*f5 - sqrt(25*f5^2 - 60*f4*f6))/f6, 1)]
            sage: e.subs(x=res[0][0]).is_zero()
            True"""
    def round(self) -> Integer:
        """
        Round this expression to the nearest integer.

        EXAMPLES::

            sage: u = sqrt(43203735824841025516773866131535024)
            sage: u.round()
            207855083711803945
            sage: t = sqrt(Integer('1'*1000)).round(); print(str(t)[-10:])
            3333333333
            sage: (-sqrt(110)).round()
            -10
            sage: (-sqrt(115)).round()
            -11
            sage: (sqrt(-3)).round()
            Traceback (most recent call last):
            ...
            ValueError: could not convert sqrt(-3) to a real number"""
    def series(
        self, 
        symbol: CoercibleToExpression, 
        order: SupportsInt | PlusInfinity | None = None, 
        algorithm: Literal["ginac", "maxima"] = "ginac"
    ) -> SymbolicSeries[P]:
        """
        Return the power series expansion of ``self`` in terms of the
        given variable to the given order.

        INPUT:

        - ``symbol`` -- a symbolic variable or symbolic equality
          such as ``x == 5``; if an equality is given, the
          expansion is around the value on the right hand side
          of the equality
        - ``order`` -- integer; if nothing given, it is set
          to the global default (``20``), which can be changed
          using :func:`set_series_precision`
        - ``algorithm`` -- string (default: ``\'ginac\'``); one of the following:

          * ``\'ginac\'``
          * ``\'maxima\'``

        OUTPUT: a power series

        To truncate the power series and obtain a normal expression, use the
        :meth:`truncate` command.

        EXAMPLES:

        We expand a polynomial in `x` about 0, about `1`, and also truncate
        it back to a polynomial::

            sage: var(\'x,y\')
            (x, y)
            sage: f = (x^3 - sin(y)*x^2 - 5*x + 3); f
            x^3 - x^2*sin(y) - 5*x + 3
            sage: g = f.series(x, 4); g
            3 + (-5)*x + (-sin(y))*x^2 + 1*x^3 + Order(x^4)
            sage: g.truncate()
            x^3 - x^2*sin(y) - 5*x + 3
            sage: g = f.series(x==1, 4); g
            (-sin(y) - 1) + (-2*sin(y) - 2)*(x - 1) + (-sin(y) + 3)*(x - 1)^2
            + 1*(x - 1)^3 + Order((x - 1)^4)
            sage: h = g.truncate(); h
            (x - 1)^3 - (x - 1)^2*(sin(y) - 3) - 2*(x - 1)*(sin(y) + 1) - sin(y) - 1
            sage: h.expand()
            x^3 - x^2*sin(y) - 5*x + 3

        We computer another series expansion of an analytic function::

            sage: f = sin(x)/x^2
            sage: f.series(x,7)
            1*x^(-1) + (-1/6)*x + 1/120*x^3 + (-1/5040)*x^5 + Order(x^7)
            sage: f.series(x)
            1*x^(-1) + (-1/6)*x + ... + Order(x^20)
            sage: f.series(x==1,3)
            (sin(1)) + (cos(1) - 2*sin(1))*(x - 1) + (-2*cos(1) + 5/2*sin(1))*(x - 1)^2
            + Order((x - 1)^3)
            sage: f.series(x==1,3).truncate().expand()
            -2*x^2*cos(1) + 5/2*x^2*sin(1) + 5*x*cos(1) - 7*x*sin(1) - 3*cos(1) + 11/2*sin(1)

        Expressions formed by combining series can be expanded
        by applying series again::

            sage: (1/(1-x)).series(x, 3)+(1/(1+x)).series(x,3)
            (1 + 1*x + 1*x^2 + Order(x^3)) + (1 + (-1)*x + 1*x^2 + Order(x^3))
            sage: _.series(x,3)
            2 + 2*x^2 + Order(x^3)
            sage: (1/(1-x)).series(x, 3)*(1/(1+x)).series(x,3)
            (1 + 1*x + 1*x^2 + Order(x^3))*(1 + (-1)*x + 1*x^2 + Order(x^3))
            sage: _.series(x,3)
            1 + 1*x^2 + Order(x^3)

        Following the GiNaC tutorial, we use John Machin\'s amazing
        formula `\\pi = 16 \\tan^{-1}(1/5) - 4 \\tan^{-1}(1/239)` to compute
        digits of `\\pi`. We expand the arc tangent around 0 and insert
        the fractions 1/5 and 1/239.

        ::

            sage: x = var(\'x\')
            sage: f = atan(x).series(x, 10); f
            1*x + (-1/3)*x^3 + 1/5*x^5 + (-1/7)*x^7 + 1/9*x^9 + Order(x^10)
            sage: float(16*f.subs(x==1/5) - 4*f.subs(x==1/239))
            3.1415926824043994

        TESTS:

        Check if :issue:`8943` is fixed::

            sage: ((1+arctan(x))**(1/x)).series(x==0, 3)
            (e) + (-1/2*e)*x + (1/8*e)*x^2 + Order(x^3)

        Order may be negative::

            sage: f = sin(x)^(-2); f.series(x, -1)
            1*x^(-2) + Order(1/x)

        Check if changing global series precision does it right::

            sage: set_series_precision(3)
            sage: (1/(1-2*x)).series(x)
            1 + 2*x + 4*x^2 + Order(x^3)
            sage: set_series_precision(20)

        Check that :issue:`31645` is fixed::

            sage: (x^(-1) + 1).series(x,1)
            1*x^(-1) + 1 + Order(x)

        Check that :issue:`32115` is fixed::

            sage: exp(log(1+x)*(1/x)).series(x)
            (e) + (-1/2*e)*x + (11/24*e)*x^2 + (-7/16*e)*x^3 + (2447/5760*e)*x^4 + ...

        Check that :issue:`32640` is fixed::

            sage: ((1 - x)^-x).series(x, 8)
            1 + 1*x^2 + 1/2*x^3 + 5/6*x^4 + 3/4*x^5 + 33/40*x^6 + 5/6*x^7 + Order(x^8)

        Try different algorithms::

            sage: ((1 - x)^-x).series(x, 8, algorithm="maxima")
            1 + 1*x^2 + 1/2*x^3 + 5/6*x^4 + 3/4*x^5 + 33/40*x^6 + 5/6*x^7 + Order(x^8)
            sage: ((1 - x)^-x).series(x, 8, algorithm="ginac")
            1 + 1*x^2 + 1/2*x^3 + 5/6*x^4 + 3/4*x^5 + 33/40*x^6 + 5/6*x^7 + Order(x^8)"""
    def show(self) -> Any:
        """
        Pretty-print this symbolic expression.

        This typesets it nicely and prints it immediately.

        OUTPUT:

        This method does not return anything. Like ``print``, output
        is sent directly to the screen.

        Note that the output depends on the display preferences. For details,
        see :func:`~sage.repl.rich_output.pretty_print.pretty_print`.

        EXAMPLES::

            sage: (x^2 + 1).show()
            x^2 + 1

        TESTS::

            sage: dm = get_display_manager()
            sage: dm.preferences.text = 'ascii_art'

        EXAMPLES::

            sage: %display ascii_art  # not tested
            sage: (x^2 + 1).show()
             2
            x  + 1

        TESTS:

        After the previous example, we need to reset the text display
        preferences::

            sage: dm.preferences.text = None"""
    # TODO: examine when will simplify returns non-expressions
    # notable examble SR(1).simplify("sympy") or with "fricas", result is Integer
    @overload
    def simplify(self, algorithm: Literal["sympy", "fricas"]) -> SageObject: ...
    @overload
    def simplify(self, algorithm: Literal["giac"]) -> Expression: ...
    @overload
    def simplify(self, algorithm: Literal["maxima"] = "maxima") -> Expression[P]:
        """
        Return a simplified version of this symbolic expression.

        INPUT:

        - ``algorithm`` -- one of :

            - ``maxima`` : (default) sends the expression to
              ``maxima`` and converts it back to Sage

            - ``sympy`` : converts the expression to ``sympy``,
              simplifies it (passing any optional keyword(s)), and
              converts the result to Sage

            - ``giac`` : converts the expression to ``giac``,
              simplifies it, and converts the result to Sage

            - ``fricas`` : converts the expression to ``fricas``,
              simplifies it, and converts the result to Sage

        .. SEEALSO::

           :meth:`simplify_full`, :meth:`simplify_trig`,
           :meth:`simplify_rational`, :meth:`simplify_rectform`
           :meth:`simplify_factorial`, :meth:`simplify_log`,
           :meth:`simplify_real`, :meth:`simplify_hypergeometric`,
           :meth:`canonicalize_radical`

        EXAMPLES::

            sage: a = var(\'a\'); f = x*sin(2)/(x^a); f
            x*sin(2)/x^a
            sage: f.simplify()
            x^(-a + 1)*sin(2)

        Some simplifications are quite algorithm-specific::

            sage: x, t = var("x, t")
            sage: ex = cos(t).exponentialize()
            sage: ex = ex.subs((sin(t).exponentialize()==x).solve(t)[0])
            sage: ex
            1/2*I*x + 1/2*I*sqrt(x^2 - 1) + 1/2/(I*x + I*sqrt(x^2 - 1))
            sage: ex.simplify()
            1/2*I*x + 1/2*I*sqrt(x^2 - 1) + 1/(2*I*x + 2*I*sqrt(x^2 - 1))
            sage: ex.simplify(algorithm=\'sympy\')
            I*(x^2 + sqrt(x^2 - 1)*x - 1)/(x + sqrt(x^2 - 1))
            sage: ex.simplify(algorithm=\'giac\')  # needs giac
            I*sqrt(x^2 - 1)
            sage: ex.simplify(algorithm=\'fricas\')  # optional - fricas
            (I*x^2 + I*sqrt(x^2 - 1)*x - I)/(x + sqrt(x^2 - 1))

        TESTS:

        Check that :issue:`14637` is fixed::

            sage: assume(x > 0, x < pi/2)
            sage: acos(cos(x)).simplify()
            x
            sage: forget()

        Check that simplifying with sympy works correctly::

            sage: expr = (-1/5*(2*sqrt(6)*(sqrt(5) - 5) + 11*sqrt(5) - 11)/(2*sqrt(6)*sqrt(5) - 11))
            sage: expr.simplify(algorithm=\'sympy\')
            1/5*sqrt(5) - 1/5"""
    def simplify_factorial(self) -> Expression[P]:
        """
        Simplify by combining expressions with factorials, and by
        expanding binomials into factorials.

        ALIAS: factorial_simplify and simplify_factorial are the same

        EXAMPLES:

        Some examples are relatively clear::

            sage: var('n,k')
            (n, k)
            sage: f = factorial(n+1)/factorial(n); f
            factorial(n + 1)/factorial(n)
            sage: f.simplify_factorial()
            n + 1

        ::

            sage: f = factorial(n)*(n+1); f
            (n + 1)*factorial(n)
            sage: simplify(f)
            (n + 1)*factorial(n)
            sage: f.simplify_factorial()
            factorial(n + 1)

        ::

            sage: f = binomial(n, k)*factorial(k)*factorial(n-k); f
            binomial(n, k)*factorial(k)*factorial(-k + n)
            sage: f.simplify_factorial()
            factorial(n)

        A more complicated example, which needs further processing::

            sage: f = factorial(x)/factorial(x-2)/2 + factorial(x+1)/factorial(x)/2; f
            1/2*factorial(x + 1)/factorial(x) + 1/2*factorial(x)/factorial(x - 2)
            sage: g = f.simplify_factorial(); g
            1/2*(x - 1)*x + 1/2*x + 1/2
            sage: g.simplify_rational()
            1/2*x^2 + 1/2


        TESTS:

        Check that the problem with applying ``full_simplify()`` to gamma
        functions (:issue:`9240`) has been fixed::

            sage: gamma(1/3)
            gamma(1/3)
            sage: gamma(1/3).full_simplify()
            gamma(1/3)
            sage: gamma(4/3)
            gamma(4/3)
            sage: gamma(4/3).full_simplify()
            1/3*gamma(1/3)"""
    factorial_simplify = simplify_factorial
    def simplify_full(self) -> Expression[P]:
        """
        Apply :meth:`simplify_factorial`, :meth:`simplify_rectform`,
        :meth:`simplify_trig`, :meth:`simplify_rational`, and
        then :meth:`expand_sum` to ``self`` (in that order).

        ALIAS: ``simplify_full`` and ``full_simplify`` are the same.

        EXAMPLES::

            sage: f = sin(x)^2 + cos(x)^2
            sage: f.simplify_full()
            1

        ::

            sage: f = sin(x/(x^2 + x))
            sage: f.simplify_full()
            sin(1/(x + 1))

        ::

            sage: var('n,k')
            (n, k)
            sage: f = binomial(n,k)*factorial(k)*factorial(n-k)
            sage: f.simplify_full()
            factorial(n)

        TESTS:

        There are two square roots of `(x + 1)^2`, so this should
        not be simplified to `x + 1`, see :issue:`12737`::

            sage: f = sqrt((x + 1)^2)
            sage: f.simplify_full()
            sqrt(x^2 + 2*x + 1)

        The imaginary part of an expression should not change under
        simplification; :issue:`11934`::

            sage: f = sqrt(-8*(4*sqrt(2) - 7)*x^4 + 16*(3*sqrt(2) - 5)*x^3)
            sage: original = f.imag_part()
            sage: simplified = f.full_simplify().imag_part()
            sage: original - simplified
            0

        The invalid simplification from :issue:`12322` should not occur
        after :issue:`12737`::

            sage: t = var('t')
            sage: assume(t, 'complex')
            sage: assumptions()
            [t is complex]
            sage: f = (1/2)*log(2*t) + (1/2)*log(1/t)
            sage: f.simplify_full()
            1/2*log(2*t) - 1/2*log(t)
            sage: forget()

        Complex logs are not contracted, :issue:`17556`::

            sage: x,y = SR.var('x,y')
            sage: assume(y, 'complex')
            sage: f = log(x*y) - (log(x) + log(y))
            sage: f.simplify_full()
            log(x*y) - log(x) - log(y)
            sage: forget()

        The simplifications from :meth:`simplify_rectform` are
        performed, :issue:`17556`::

            sage: f = ( e^(I*x) - e^(-I*x) ) / ( I*e^(I*x) + I*e^(-I*x) )
            sage: f.simplify_full()
            sin(x)/cos(x)

        Check that :issue:`20846` is fixed::

            sage: ((1/6*pi^2).series(x)).simplify_full()
            1/6*pi^2"""
    full_simplify = simplify_full
    def simplify_hypergeometric(
        self, algorithm: Literal["maxima", "sage"] = "maxima") -> Expression[P]:
        """
        Simplify an expression containing hypergeometric or confluent
        hypergeometric functions.

        INPUT:

        - ``algorithm`` -- (default: ``'maxima'``) the algorithm to use for
          for simplification. Implemented are ``'maxima'``, which uses Maxima's
          ``hgfred`` function, and ``'sage'``, which uses an algorithm
          implemented in the hypergeometric module

        ALIAS: :meth:`hypergeometric_simplify` and
        :meth:`simplify_hypergeometric` are the same

        EXAMPLES::

            sage: hypergeometric((5, 4), (4, 1, 2, 3),
            ....:                x).simplify_hypergeometric()
            1/144*x^2*hypergeometric((), (3, 4), x) +...
            1/3*x*hypergeometric((), (2, 3), x) + hypergeometric((), (1, 2), x)
            sage: (2*hypergeometric((), (), x)).simplify_hypergeometric()
            2*e^x
            sage: (nest(lambda y: hypergeometric([y], [1], x), 3, 1)  # not tested, unstable
            ....:  .simplify_hypergeometric())
            laguerre(-laguerre(-e^x, x), x)
            sage: (nest(lambda y: hypergeometric([y], [1], x), 3, 1)  # not tested, unstable
            ....:  .simplify_hypergeometric(algorithm='sage'))
            hypergeometric((hypergeometric((e^x,), (1,), x),), (1,), x)
            sage: hypergeometric_M(1, 3, x).simplify_hypergeometric()
            -2*((x + 1)*e^(-x) - 1)*e^x/x^2
            sage: (2 * hypergeometric_U(1, 3, x)).simplify_hypergeometric()
            2*(x + 1)/x^2"""
    hypergeometric_simplify = simplify_hypergeometric
    def simplify_log(
        self, algorithm: Literal["one", "ratios", "constants", "all"] | None = None
    ) -> Expression[P]:
        """
        Simplify a (real) symbolic expression that contains logarithms.

        The given expression is scanned recursively, transforming
        subexpressions of the form `a \\log(b) + c \\log(d)` into
        `\\log(b^{a} d^{c})` before simplifying within the ``log()``.

        The user can specify conditions that `a` and `c` must satisfy
        before this transformation will be performed using the optional
        parameter ``algorithm``.

        .. WARNING::

            This is only safe to call if every variable in the given
            expression is assumed to be real. The simplification it performs
            is in general not valid over the complex numbers. For example::

                sage: x,y = SR.var('x,y')
                sage: f = log(x*y) - (log(x) + log(y))
                sage: f(x=-1, y=i)
                -2*I*pi
                sage: f.simplify_log()
                0

        INPUT:

        - ``self`` -- expression to be simplified

        - ``algorithm`` -- (default: ``None``) governs the condition
          on `a` and `c` which must be satisfied to contract expression
          `a \\log(b) + c \\log(d)`. Values are

          - ``None`` (use Maxima default, integers),

          - ``'one'`` (1 and -1),

          - ``'ratios'`` (rational numbers),

          - ``'constants'`` (constants),

          - ``'all'`` (all expressions).

        ALGORITHM:

        This uses the Maxima ``logcontract()`` command.

        ALIAS:

        :meth:`log_simplify` and :meth:`simplify_log` are the same.

        EXAMPLES::

            sage: x,y,t = var('x y t')

        Only two first terms are contracted in the following example;
        the logarithm with coefficient `\\frac{1}{2}` is not contracted::

            sage: f = log(x)+2*log(y)+1/2*log(t)
            sage: f.simplify_log()
            log(x*y^2) + 1/2*log(t)

        To contract all terms in the previous example, we use the
        ``'ratios'`` ``algorithm``::

            sage: f.simplify_log(algorithm='ratios')
            log(sqrt(t)*x*y^2)

        To contract terms with no coefficient (more precisely, with
        coefficients `1` and `-1`), we use the ``'one'``
        ``algorithm``::

            sage: f = log(x)+2*log(y)-log(t)
            sage: f.simplify_log('one')
            2*log(y) + log(x/t)

        ::

            sage: f = log(x)+log(y)-1/3*log((x+1))
            sage: f.simplify_log()
            log(x*y) - 1/3*log(x + 1)

            sage: f.simplify_log('ratios')
            log(x*y/(x + 1)^(1/3))

        `\\pi` is an irrational number; to contract logarithms in the
        following example we have to set ``algorithm`` to ``'constants'``
        or ``'all'``::

            sage: f = log(x)+log(y)-pi*log((x+1))
            sage: f.simplify_log('constants')
            log(x*y/(x + 1)^pi)

        ``x*log(9)`` is contracted only if ``algorithm`` is ``'all'``::

            sage: (x*log(9)).simplify_log()
            2*x*log(3)
            sage: (x*log(9)).simplify_log('all')
            log(3^(2*x))

        TESTS:

        Ensure that the option ``algorithm`` from one call has no
        influence upon future calls (a Maxima flag was set, and we have
        to ensure that its value has been restored)::

            sage: f = log(x)+2*log(y)+1/2*log(t)
            sage: f.simplify_log('one')
            1/2*log(t) + log(x) + 2*log(y)

            sage: f.simplify_log('ratios')
            log(sqrt(t)*x*y^2)

            sage: f.simplify_log()
            log(x*y^2) + 1/2*log(t)

        This shows that the issue at :issue:`7334` is fixed. Maxima
        intentionally keeps the expression inside the log factored::

            sage: log_expr = (log(sqrt(2)-1)+log(sqrt(2)+1))
            sage: log_expr.simplify_log('all')
            log((sqrt(2) + 1)*(sqrt(2) - 1))
            sage: _.simplify_rational()
            0

        We should use the current simplification domain rather than
        set it to 'real' explicitly (:issue:`12780`)::

            sage: f = sqrt(x^2)
            sage: f.simplify_log()
            sqrt(x^2)
            sage: from sage.calculus.calculus import maxima
            sage: maxima('domain: real;')
            real
            sage: f.simplify_log()
            abs(x)
            sage: maxima('domain: complex;')
            complex

        AUTHORS:

        - Robert Marik (11-2009)"""
    log_simplify = simplify_log
    def simplify_rational(
        self, 
        algorithm: Literal["simple", "full", "noexpand"] = "full", 
        map: bool = False
    ) -> Expression[P]:
        """
        Simplify rational expressions.

        INPUT:

        - ``self`` -- symbolic expression

        - ``algorithm`` -- (default: ``'full'``) string which switches the
          algorithm for simplifications. Possible values are

          - ``'simple'`` (simplify rational functions into quotient of two
            polynomials)

          - ``'full'`` (apply repeatedly, if necessary)

          - ``'noexpand'`` (convert to common denominator and add)

        - ``map`` -- boolean (default: ``False``); if ``True``, the result is
          an expression whose leading operator is the same as that of the
          expression ``self`` but whose subparts are the results of
          applying simplification rules to the corresponding subparts
          of the expressions.

        ALIAS: :meth:`rational_simplify` and :meth:`simplify_rational`
        are the same

        DETAILS: We call Maxima functions ratsimp, fullratsimp and
        xthru. If each part of the expression has to be simplified
        separately, we use Maxima function map.

        EXAMPLES::

            sage: f = sin(x/(x^2 + x))
            sage: f
            sin(x/(x^2 + x))
            sage: f.simplify_rational()
            sin(1/(x + 1))

        ::

            sage: f = ((x - 1)^(3/2) - (x + 1)*sqrt(x - 1))/sqrt((x - 1)*(x + 1)); f
            -((x + 1)*sqrt(x - 1) - (x - 1)^(3/2))/sqrt((x + 1)*(x - 1))
            sage: f.simplify_rational()
            -2*sqrt(x - 1)/sqrt(x^2 - 1)

        With ``map=True`` each term in a sum is simplified separately
        and thus the results are shorter for functions which are
        combination of rational and nonrational functions. In the
        following example, we use this option if we want not to
        combine logarithm and the rational function into one
        fraction::

            sage: f = (x^2-1)/(x+1)-ln(x)/(x+2)
            sage: f.simplify_rational()
            (x^2 + x - log(x) - 2)/(x + 2)
            sage: f.simplify_rational(map=True)
            x - log(x)/(x + 2) - 1

        Here is an example from the Maxima documentation of where
        ``algorithm='simple'`` produces an (possibly useful) intermediate
        step::

            sage: y = var('y')
            sage: g = (x^(y/2) + 1)^2*(x^(y/2) - 1)^2/(x^y - 1)
            sage: g.simplify_rational(algorithm='simple')
            (x^(2*y) - 2*x^y + 1)/(x^y - 1)
            sage: g.simplify_rational()
            x^y - 1

        With option ``algorithm='noexpand'`` we only convert to common
        denominators and add. No expansion of products is performed::

            sage: f = 1/(x+1)+x/(x+2)^2
            sage: f.simplify_rational()
            (2*x^2 + 5*x + 4)/(x^3 + 5*x^2 + 8*x + 4)
            sage: f.simplify_rational(algorithm='noexpand')
            ((x + 2)^2 + (x + 1)*x)/((x + 2)^2*(x + 1))"""
    rational_simplify = simplify_rational
    def simplify_real(self) -> Expression[P]:
        """
        Simplify the given expression over the real numbers. This allows
        the simplification of `\\sqrt{x^{2}}` into `\\left|x\\right|` and
        the contraction of `\\log(x) + \\log(y)` into `\\log(xy)`.

        INPUT:

        - ``self`` -- the expression to convert

        OUTPUT:

        A new expression, equivalent to the original one under the
        assumption that the variables involved are real.

        EXAMPLES::

            sage: f = sqrt(x^2)
            sage: f.simplify_real()
            abs(x)

        ::

            sage: y = SR.var('y')
            sage: f = log(x) + 2*log(y)
            sage: f.simplify_real()
            log(x*y^2)

        TESTS:

        We set the Maxima ``domain`` variable to 'real' before we call
        out to Maxima. When we return, however, we should set the
        ``domain`` back to what it was, rather than assuming that it
        was 'complex'::

            sage: from sage.calculus.calculus import maxima
            sage: maxima('domain: real;')
            real
            sage: x.simplify_real()
            x
            sage: maxima('domain;')
            real
            sage: maxima('domain: complex;')
            complex

        We forget the assumptions that our variables are real after
        simplification; make sure we don't forget an assumption that
        existed before we were called::

            sage: assume(x, 'real')
            sage: x.simplify_real()
            x
            sage: assumptions()
            [x is real]
            sage: forget()

        We also want to be sure that we don't forget assumptions on
        other variables::

            sage: x,y,z = SR.var('x,y,z')
            sage: assume(y, 'integer')
            sage: assume(z, 'antisymmetric')
            sage: x.simplify_real()
            x
            sage: assumptions()
            [y is integer, z is antisymmetric]
            sage: forget()

        No new assumptions should exist after the call::

            sage: assumptions()
            []
            sage: x.simplify_real()
            x
            sage: assumptions()
            []"""
    def simplify_rectform(self, complexity_measure=string_length) -> Expression:
        """
        Attempt to simplify this expression by expressing it in the
        form `a + bi` where both `a` and `b` are real. This
        transformation is generally not a simplification, so we use
        the given ``complexity_measure`` to discard
        non-simplifications.

        INPUT:

        - ``self`` -- the expression to simplify

        - ``complexity_measure`` -- (default:
          ``sage.symbolic.complexity_measures.string_length``) a
          function taking a symbolic expression as an argument and
          returning a measure of that expressions complexity. If
          ``None`` is supplied, the simplification will be performed
          regardless of the result.

        OUTPUT:

        If the transformation produces a simpler expression (according
        to ``complexity_measure``) then that simpler expression is
        returned. Otherwise, the original expression is returned.

        ALGORITHM:

        We first call :meth:`rectform()` on the given
        expression. Then, the supplied complexity measure is used to
        determine whether or not the result is simpler than the
        original expression.

        EXAMPLES:

        The exponential form of `\\tan(x)`::

            sage: f = ( e^(I*x) - e^(-I*x) ) / ( I*e^(I*x) + I*e^(-I*x) )
            sage: f.simplify_rectform()
            sin(x)/cos(x)

        This should not be expanded with Euler's formula since the
        resulting expression is longer when considered as a string,
        and the default ``complexity_measure`` uses string length to
        determine which expression is simpler::

            sage: f = e^(I*x)
            sage: f.simplify_rectform()
            e^(I*x)

        However, if we pass ``None`` as our complexity measure, it
        is::

            sage: f = e^(I*x)
            sage: f.simplify_rectform(complexity_measure = None)
            cos(x) + I*sin(x)

        TESTS:

        When given ``None``, we should always call :meth:`rectform()`
        and return the result::

            sage: polynomials = QQ['x']
            sage: f = SR(polynomials.random_element())
            sage: g = f.simplify_rectform(complexity_measure = None)
            sage: bool(g == f.rectform())
            True"""
    def simplify_trig(self, expand: bool = True) -> Expression[P]:
        """
        Optionally expand and then employ identities such as
        `\\sin(x)^2 + \\cos(x)^2 = 1`, `\\cosh(x)^2 - \\sinh(x)^2 = 1`,
        `\\sin(x)\\csc(x) = 1`, or `\\tanh(x)=\\sinh(x)/\\cosh(x)`
        to simplify expressions containing tan, sec, etc., to sin,
        cos, sinh, cosh.

        INPUT:

        - ``self`` -- symbolic expression

        - ``expand`` -- boolean (default: ``True``); if ``True``, expands
          trigonometric and hyperbolic functions of sums of angles and of
          multiple angles occurring in ``self`` first. For best results,
          ``self`` should be expanded. See also :meth:`expand_trig` to
          get more controls on this expansion.

        ALIAS: :meth:`trig_simplify` and :meth:`simplify_trig` are the same

        EXAMPLES::

            sage: f = sin(x)^2 + cos(x)^2; f
            cos(x)^2 + sin(x)^2
            sage: f.simplify()
            cos(x)^2 + sin(x)^2
            sage: f.simplify_trig()
            1
            sage: h = sin(x)*csc(x)
            sage: h.simplify_trig()
            1
            sage: k = tanh(x)*cosh(2*x)
            sage: k.simplify_trig()
            (2*sinh(x)^3 + sinh(x))/cosh(x)

        In some cases we do not want to expand::

            sage: f = tan(3*x)
            sage: f.simplify_trig()
            -(4*cos(x)^2 - 1)*sin(x)/(4*cos(x)*sin(x)^2 - cos(x))
            sage: f.simplify_trig(False)
            sin(3*x)/cos(3*x)"""
    trig_simplify = simplify_trig
    def sin(self, hold: bool = False) -> Expression[P]:
        """
        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: sin(x^2 + y^2)
            sin(x^2 + y^2)
            sage: sin(sage.symbolic.constants.pi)
            0
            sage: sin(SR(1))
            sin(1)
            sage: sin(SR(RealField(150)(1)))
            0.84147098480789650665250232163029899962256306

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(0).sin()
            0
            sage: SR(0).sin(hold=True)
            sin(0)

        This also works using functional notation::

            sage: sin(0,hold=True)
            sin(0)
            sage: sin(0)
            0

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(0).sin(hold=True); a.unhold()
            0

        TESTS::

            sage: SR(oo).sin()
            Traceback (most recent call last):
            ...
            RuntimeError: sin_eval(): sin(infinity) encountered
            sage: SR(-oo).sin()
            Traceback (most recent call last):
            ...
            RuntimeError: sin_eval(): sin(infinity) encountered
            sage: SR(unsigned_infinity).sin()
            Traceback (most recent call last):
            ...
            RuntimeError: sin_eval(): sin(infinity) encountered"""
    def sinh(self, hold: bool = False) -> Expression[P]:
        """
        Return sinh of ``self``.

        We have `\\sinh(x) = (e^{x} - e^{-x})/2`.

        EXAMPLES::

            sage: x.sinh()
            sinh(x)
            sage: SR(1).sinh()
            sinh(1)
            sage: SR(0).sinh()
            0
            sage: SR(1.0).sinh()
            1.17520119364380
            sage: maxima('sinh(1.0)')
            1.17520119364380...

            sinh(1.0000000000000000000000000)
            sage: SR(1).sinh().n(90)
            1.1752011936438014568823819
            sage: SR(RIF(1)).sinh()
            1.175201193643802?

        To prevent automatic evaluation use the ``hold`` argument::

            sage: arccosh(x).sinh()
            sqrt(x + 1)*sqrt(x - 1)
            sage: arccosh(x).sinh(hold=True)
            sinh(arccosh(x))

        This also works using functional notation::

            sage: sinh(arccosh(x),hold=True)
            sinh(arccosh(x))
            sage: sinh(arccosh(x))
            sqrt(x + 1)*sqrt(x - 1)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = arccosh(x).sinh(hold=True); a.simplify()
            sqrt(x + 1)*sqrt(x - 1)

        TESTS::

            sage: SR(oo).sinh()
            +Infinity
            sage: SR(-oo).sinh()
            -Infinity
            sage: SR(unsigned_infinity).sinh()
            Traceback (most recent call last):
            ...
            RuntimeError: sinh_eval(): sinh(unsigned_infinity) encountered"""
    # TODO: this uses solve() in symbolic.relation
    @overload
    def solve(
        self, 
        x, 
        multiplicities: bool =False, 
        solution_dict: Literal[True] = ..., 
        explicit_solutions: bool =False, 
        to_poly_solve: bool | str = False, 
        algorithm: str | None = None, 
        domain: str | None = None
    ) -> Any: ...
    @overload
    def solve(
        self, 
        x, 
        multiplicities: bool =False, 
        solution_dict: Literal[False] = False, 
        explicit_solutions: bool = False, 
        to_poly_solve: bool | str = False, 
        algorithm: str | None = None, 
        domain: str | None = None
    ) -> Any:
        """
        Analytically solve the equation ``self == 0`` or a univariate
        inequality for the variable `x`.

        .. warning::

           This is not a numerical solver -- use :meth:`find_root` to solve
           for ``self == 0`` numerically on an interval.

        INPUT:

        - ``x`` -- variable(s) to solve for

        - ``multiplicities`` -- boolean (default: ``False``); if ``True``,
          return corresponding multiplicities.  This keyword is
          incompatible with ``to_poly_solve=True`` and does not make
          any sense when solving an inequality.

        - ``solution_dict`` -- boolean (default: ``False``); if ``True`` or nonzero,
          return a list of dictionaries containing solutions. Not used
          when solving an inequality.

        - ``explicit_solutions`` -- boolean (default: ``False``); require that
          all roots be explicit rather than implicit. Not used
          when solving an inequality.

        - ``to_poly_solve`` -- boolean (default: ``False``) or string; use
          Maxima's ``to_poly_solver`` package to search for more possible
          solutions, but possibly encounter approximate solutions.
          This keyword is incompatible with ``multiplicities=True``
          and is not used when solving an inequality. Setting ``to_poly_solve``
          to ``'force'`` omits Maxima's solve command (useful when
          some solutions of trigonometric equations are lost).

        EXAMPLES::

            sage: z = var('z')
            sage: (z^5 - 1).solve(z)
            [z == 1/4*sqrt(5) + 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4,
             z == -1/4*sqrt(5) + 1/4*I*sqrt(-2*sqrt(5) + 10) - 1/4,
             z == -1/4*sqrt(5) - 1/4*I*sqrt(-2*sqrt(5) + 10) - 1/4,
             z == 1/4*sqrt(5) - 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4,
             z == 1]

            sage: solve((z^3-1)^3, z, multiplicities=True)
            ([z == 1/2*I*sqrt(3) - 1/2, z == -1/2*I*sqrt(3) - 1/2, z == 1], [3, 3, 3])

        TESTS:

        Check that :issue:`20755` is indeed fixed::

            sage: w = x^4 - (1+3*i)*x^3 - (2-4*i)*x^2 + (6-2*i)*x - 4 - 4*i
            sage: w.solve(x,multiplicities=True)
            ([x == -1/2*sqrt(2*I) + 3/2*I - 1/2,
              x == 1/2*sqrt(2*I) + 3/2*I - 1/2,
              x == (-I + 1), x == (I + 1)],
             [1, 1, 1, 1])

        See :func:`sage.symbolic.relation.solve` or the output of ``solve?``
        for extensive documentation."""
    @overload
    def solve_diophantine( # pyright: ignore[reportOverlappingOverload]
        self, 
        x: Expression[P] | tuple[Expression[P], ...] | list[Expression[P]] | None = None, 
        solution_dict: Literal[True] = ...
    ) -> list[dict[Expression[SymbolicRing], Expression[SymbolicRing]]]: ...
    @overload
    def solve_diophantine(
        self, 
        x: Expression[P] | tuple[Expression[P], ...] | list[Expression[P]] | None = None, 
        solution_dict: Literal[False] = False
    ) -> list[Expression[SymbolicRing]] | list[tuple[Expression[SymbolicRing], ...]]:
        """
        Solve a polynomial equation in the integers (a so called Diophantine).

        If the argument is just a polynomial expression, equate to zero.
        If ``solution_dict=True``, return a list of dictionaries instead of
        a list of tuples.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: solve_diophantine(3*x == 4)                                           # needs sympy
            []
            sage: solve_diophantine(x^2 - 9)                                            # needs sympy
            [-3, 3]
            sage: sorted(solve_diophantine(x^2 + y^2 == 25))                            # needs sympy
            [(-5, 0), (-4, -3), (-4, 3), (-3, -4), (-3, 4), (0, -5)...

        The function is used when ``solve()`` is called with all variables
        assumed integer::

            sage: assume(x, 'integer')
            sage: assume(y, 'integer')
            sage: sorted(solve(x*y == 1, (x,y)))                                        # needs sympy
            [(-1, -1), (1, 1)]

        You can also pick specific variables, and get the solution as
        a dictionary::

            sage: # needs sympy
            sage: solve_diophantine(x*y == 10, x)
            [-10, -5, -2, -1, 1, 2, 5, 10]
            sage: sorted(solve_diophantine(x*y - y == 10, (x,y)))
            [(-9, -1), (-4, -2), (-1, -5), (0, -10), (2, 10), (3, 5), (6, 2), (11, 1)]
            sage: res = solve_diophantine(x*y - y == 10, solution_dict=True)
            sage: sol = [{y: -5, x: -1}, {y: -10, x: 0}, {y: -1, x: -9}, {y: -2, x: -4},
            ....:        {y: 10, x: 2}, {y: 1, x: 11}, {y: 2, x: 6}, {y: 5, x: 3}]
            sage: all(solution in res
            ....:     for solution in sol) and bool(len(res) == len(sol))
            True

        If the solution is parametrized the parameter(s) are not defined,
        but you can substitute them with specific integer values::

            sage: # needs sympy
            sage: x,y,z = var('x,y,z')
            sage: sol = solve_diophantine(x^2-y == 0); sol
            (t, t^2)
            sage: [(sol[0].subs(t=t),sol[1].subs(t=t)) for t in range(-3,4)]
            [(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)]
            sage: sol = solve_diophantine(x^2 + y^2 == z^2); sol
            (2*p*q, p^2 - q^2, p^2 + q^2)
            sage: [(sol[0].subs(p=p,q=q), sol[1].subs(p=p,q=q), sol[2].subs(p=p,q=q))
            ....:  for p in range(1,4) for q in range(1,4)]
            [(2, 0, 2), (4, -3, 5), (6, -8, 10), (4, 3, 5), (8, 0, 8),
             (12, -5, 13), (6, 8, 10), (12, 5, 13), (18, 0, 18)]

        Solve Brahmagupta-Pell equations::

            sage: sol = sorted(solve_diophantine(x^2 - 2*y^2 == 1), key=str); sol       # needs sympy
            [(-sqrt(2)*(2*sqrt(2) + 3)^t + sqrt(2)*(-2*sqrt(2) + 3)^t
               - 3/2*(2*sqrt(2) + 3)^t - 3/2*(-2*sqrt(2) + 3)^t,...
            sage: [(sol[1][0].subs(t=t).simplify_full(),                                # needs sympy
            ....:   sol[1][1].subs(t=t).simplify_full()) for t in range(-1,5)]
            [(1, 0), (3, -2), (17, -12), (99, -70), (577, -408), (3363, -2378)]

        TESTS::

            sage: solve_diophantine(x^2 - y, x, y)                                      # needs sympy
            Traceback (most recent call last):
            ...
            AttributeError: please use a tuple or list for several variables.

        .. SEEALSO::

            http://docs.sympy.org/latest/modules/solvers/diophantine.html"""
    def sqrt(self, hold: bool = False) -> Expression[P]:
        """
        Return the square root of this expression.

        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: SR(2).sqrt()
            sqrt(2)
            sage: (x^2+y^2).sqrt()
            sqrt(x^2 + y^2)
            sage: (x^2).sqrt()
            sqrt(x^2)

        Immediate simplifications are applied::

            sage: sqrt(x^2)
            sqrt(x^2)
            sage: x = SR.symbol('x', domain='real')
            sage: sqrt(x^2)
            abs(x)
            sage: forget()
            sage: assume(x<0)
            sage: sqrt(x^2)
            -x
            sage: sqrt(x^4)
            x^2
            sage: forget()
            sage: x = SR.symbol('x', domain='real')
            sage: sqrt(x^4)
            x^2
            sage: sqrt(sin(x)^2)
            abs(sin(x))
            sage: sqrt((x+1)^2)
            abs(x + 1)
            sage: forget()
            sage: assume(x<0)
            sage: sqrt((x-1)^2)
            -x + 1
            sage: forget()

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(4).sqrt()
            2
            sage: SR(4).sqrt(hold=True)
            sqrt(4)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(4).sqrt(hold=True); a.unhold()
            2

        To use this parameter in functional notation, you must coerce to
        the symbolic ring::

            sage: sqrt(SR(4),hold=True)
            sqrt(4)
            sage: sqrt(4,hold=True)
            Traceback (most recent call last):
            ...
            TypeError: ..._do_sqrt() got an unexpected keyword argument 'hold'"""
    def step(self, hold: bool = False) -> Expression[P]:
        """
        Return the value of the unit step function, which is 0 for
        negative x, 1 for 0, and 1 for positive x.

        .. SEEALSO::

            :class:`sage.functions.generalized.FunctionUnitStep`

        EXAMPLES::

            sage: x = var('x')
            sage: SR(1.5).step()
            1
            sage: SR(0).step()
            1
            sage: SR(-1/2).step()
            0
            sage: SR(float(-1)).step()
            0

        Using the ``hold`` parameter it is possible to prevent automatic
        evaluation::

            sage: SR(2).step()
            1
            sage: SR(2).step(hold=True)
            unit_step(2)"""
    type _SubsRep = (
        Expression 
            | dict[CoercibleToExpression, CoercibleToExpression]
            | list[_SubsRep] | tuple[_SubsRep]
    )
    @overload
    def subs(
        self, _none: None, /, *args: _SubsRep, **kwds: CoercibleToExpression
    ) -> Expression[P]: ...
    @overload
    def subs( # pyright: ignore[reportIncompatibleMethodOverride]
        self, *args: _SubsRep, **kwds: CoercibleToExpression
    ) -> Expression[P]:
        """
        Substitute the given subexpressions in this expression.

        EXAMPLES::

            sage: var(\'x,y,z,a,b,c,d,f,g\')
            (x, y, z, a, b, c, d, f, g)
            sage: w0 = SR.wild(0); w1 = SR.wild(1)
            sage: t = a^2 + b^2 + (x+y)^3

        Substitute with keyword arguments (works only with symbols)::

            sage: t.subs(a=c)
            (x + y)^3 + b^2 + c^2
            sage: t.subs(b=19, x=z)
            (y + z)^3 + a^2 + 361

        Substitute with a dictionary argument::

            sage: t.subs({a^2: c})
            (x + y)^3 + b^2 + c

            sage: t.subs({w0^2: w0^3})
            a^3 + b^3 + (x + y)^3

        Substitute with one or more relational expressions::

            sage: t.subs(w0^2 == w0^3)
            a^3 + b^3 + (x + y)^3

            sage: t.subs(w0 == w0^2)
            a^8 + b^8 + (x^2 + y^2)^6

            sage: t.subs(a == b, b == c)
            (x + y)^3 + b^2 + c^2

        Any number of arguments is accepted::

            sage: t.subs(a=b, b=c)
            (x + y)^3 + b^2 + c^2

            sage: t.subs({a:b}, b=c)
            (x + y)^3 + b^2 + c^2

            sage: t.subs([x == 3, y == 2], a == 2, {b:3})
            138

        It can even accept lists of lists::

            sage: eqn1 = (a*x + b*y == 0)
            sage: eqn2 = (1 + y == 0)
            sage: soln = solve([eqn1, eqn2], [x, y])
            sage: soln
            [[x == b/a, y == -1]]
            sage: f = x + y
            sage: f.subs(soln)
            b/a - 1

        Duplicate assignments will throw an error::

            sage: t.subs({a:b}, a=c)
            Traceback (most recent call last):
            ...
            ValueError: duplicate substitution for a, got values b and c

            sage: t.subs([x == 1], a = 1, b = 2, x = 2)
            Traceback (most recent call last):
            ...
            ValueError: duplicate substitution for x, got values 1 and 2

        All substitutions are performed at the same time::

             sage: t.subs({a:b, b:c})
             (x + y)^3 + b^2 + c^2

        Substitutions are done term by term, in other words Sage is not
        able to identify partial sums in a substitution (see :issue:`18396`)::

            sage: f = x + x^2 + x^4
            sage: f.subs(x = y)
            y^4 + y^2 + y
            sage: f.subs(x^2 == y)             # one term is fine
            x^4 + x + y
            sage: f.subs(x + x^2 == y)         # partial sum does not work
            x^4 + x^2 + x
            sage: f.subs(x + x^2 + x^4 == y)   # whole sum is fine
            y

        Note that it is the very same behavior as in Maxima::

            sage: E = \'x^4 + x^2 + x\'
            sage: subs = [(\'x\',\'y\'), (\'x^2\',\'y\'), (\'x^2+x\',\'y\'), (\'x^4+x^2+x\',\'y\')]

            sage: cmd = \'{}, {}={}\'
            sage: for s1,s2 in subs:
            ....:     maxima.eval(cmd.format(E, s1, s2))
            \'y^4+y^2+y\'
            \'y+x^4+x\'
            \'x^4+x^2+x\'
            \'y\'

        Or as in Maple::

            sage: cmd = \'subs({}={}, {})\'              # optional - maple
            sage: for s1,s2 in subs:                   # optional - maple
            ....:     maple.eval(cmd.format(s1,s2, E))
            \'y^4+y^2+y\'
            \'x^4+x+y\'
            \'x^4+x^2+x\'
            \'y\'

        But Mathematica does something different on the third example::

            sage: cmd = \'{} /. {} -> {}\'                    # optional - mathematica
            sage: for s1,s2 in subs:                        # optional - mathematica
            ....:     mathematica.eval(cmd.format(E,s1,s2))
                 2    4
            y + y  + y
                 4
            x + x  + y
             4
            x  + y
            y

        The same, with formatting more suitable for cut and paste::

            sage: for s1,s2 in subs:                        # optional - mathematica
            ....:     mathematica(cmd.format(E,s1,s2))
            y + y^2 + y^4
            x + x^4 + y
            x^4 + y
            y

        .. WARNING::

            Unexpected results may occur if the left-hand side of some substitution
            is not just a single variable (or is a "wildcard" variable). For example,
            the result of ``cos(cos(cos(x))).subs({cos(x) : x})`` is ``x``, because
            the substitution is applied repeatedly. Such repeated substitutions (and
            pattern-matching code that may be somewhat unpredictable) are disabled
            only in the basic case where the left-hand side of every substitution is
            a variable. In particular, although the result of
            ``(x^2).subs({x : sqrt(x)})`` is ``x``, the result of
            ``(x^2).subs({x : sqrt(x), y^2 : y})`` is ``sqrt(x)``, because repeated
            substitution is enabled by the presence of the expression ``y^2`` in the
            left-hand side of one of the substitutions, even though that particular
            substitution does not get applied.

        TESTS:

        No arguments return the same expression::

            sage: t = a^2 + b^2 + (x+y)^3
            sage: t.subs()
            (x + y)^3 + a^2 + b^2

        Similarly for a empty dictionary, empty tuples and empty lists::

            sage: t.subs({}, (), [], ())
            (x + y)^3 + a^2 + b^2

        Invalid argument returns error::

            sage: t.subs(5)
            Traceback (most recent call last):
            ...
            TypeError: not able to determine a substitution from 5

        Substitutions with infinity::

            sage: (x/y).subs(y=oo)
            0
            sage: (x/y).subs(x=oo)
            Traceback (most recent call last):
            ...
            RuntimeError: indeterminate expression: infinity * f(x) encountered.
            sage: (x*y).subs(x=oo)
            Traceback (most recent call last):
            ...
            RuntimeError: indeterminate expression: infinity * f(x) encountered.
            sage: (x^y).subs(x=oo)
            Traceback (most recent call last):
            ...
            ValueError: power::eval(): pow(Infinity, f(x)) is not defined.
            sage: (x^y).subs(y=oo)
            Traceback (most recent call last):
            ...
            ValueError: power::eval(): pow(f(x), infinity) is not defined.
            sage: (x+y).subs(x=oo)
            +Infinity
            sage: (x-y).subs(y=oo)
            -Infinity
            sage: gamma(x).subs(x=-1)
            Infinity
            sage: 1/gamma(x).subs(x=-1)
            0

        Verify that this operation does not modify the passed
        dictionary (:issue:`6622`)::

            sage: var(\'v t\')
            (v, t)
            sage: f = v*t
            sage: D = {v: 2}
            sage: f(D, t=3)
            6
            sage: D
            {v: 2}

        Check if :issue:`9891` is fixed::

            sage: exp(x).subs(x=log(x))
            x

        Check if :issue:`13587` is fixed::

            sage: t = tan(x)^2 - tan(x)
            sage: t.subs(x=pi/2)
            Infinity
            sage: u = gamma(x) - gamma(x-1)
            sage: u.subs(x=-1)
            Infinity

        More checks for ``subs``::

            sage: var(\'x,y,z\'); f = x^3 + y^2 + z
            (x, y, z)
            sage: f.subs(x^3 == y^2, z == 1)
            2*y^2 + 1
            sage: f.subs({x^3:y^2, z:1})
            2*y^2 + 1
            sage: f = x^2 + x^4
            sage: f.subs(x^2 == x)
            x^4 + x
            sage: f = cos(x^2) + sin(x^2)
            sage: f.subs(x^2 == x)
            cos(x) + sin(x)
            sage: f(x,y,t) = cos(x) + sin(y) + x^2 + y^2 + t
            sage: f.subs(y^2 == t)
            (x, y, t) |--> x^2 + 2*t + cos(x) + sin(y)
            sage: f.subs(x^2 + y^2 == t)
            (x, y, t) |--> x^2 + y^2 + t + cos(x) + sin(y)

        Check that inverses in sums are recognized::

            sage: (1 + 1/x).subs({x: 1/x})
            x + 1
            sage: (x + 1/x^2).subs({x: 1/x})
            x^2 + 1/x
            sage: (sqrt(x) + 1/sqrt(x)).subs({x: 1/x})
            sqrt(x) + 1/sqrt(x)

        Check that :issue:`30378` is fixed::

            sage: (x^2).subs({x: sqrt(x)})
            x
            sage: f(x) = x^2
            sage: f(sqrt(x))
            x
            sage: a = var("a")
            sage: f = function("f")
            sage: integrate(f(x), x, 0, a).subs(a=cos(a))
            integrate(f(x), x, 0, cos(a))

        Check that :issue:`31554` is fixed::

            sage: a,b,c,d,x,y = var("a b c d x y")
            sage: with hold:
            ....:     print((2*x^0*a + b*y^1).subs({x:c, y:c*d}))
            b*c*d + 2*a

        Check that :issue:`31530` is fixed::

            sage: a, b = var("a b")
            sage: (a + b*x).series(x, 2).subs(a=a, b=b)
            (a) + (b)*x + Order(x^2)

        Check that :issue:`31585` is fixed::

            sage: m = -2^31
            sage: (-x).subs(x=m)
            2147483648
            sage: abs(x).subs(x=m)
            2147483648
            sage: (2*x).subs(x=m)
            -4294967296
            sage: (m*x + 1)*x
            -(2147483648*x - 1)*x
            sage: m = -2^63
            sage: (-x).subs(x=m)
            9223372036854775808
            sage: abs(x).subs(x=m)
            9223372036854775808
            sage: (2*x).subs(x=m)
            -18446744073709551616
            sage: (m*x + 1)*x
            -(9223372036854775808*x - 1)*x"""
    def substitute_function(
        self, *args: _SubsRep, **kargs: Expression) -> Expression[P]:
        """
        Substitute the given functions by their replacements in this expression.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: foo = function('foo'); bar = function('bar')
            sage: f = foo(x) + 1/foo(pi*y)

        Substitute with a dictionary::

            sage: f.substitute_function({foo: bar})
            1/bar(pi*y) + bar(x)
            sage: f.substitute_function({foo(x): bar(x)})
            1/bar(pi*y) + bar(x)

        If the function expression to be substituted includes its arguments, the right hand side can be an arbitrary symbolic expression::

            sage: f.substitute_function({foo(x): x^2})
            x^2 + 1/(pi^2*y^2)

        Substitute with keyword arguments (works only if no function arguments are given)::

            sage: f.substitute_function(foo=bar)
            1/bar(pi*y) + bar(x)

        Substitute with a relational expression::

            sage: f.substitute_function(foo(x)==bar(x))
            1/bar(pi*y) + bar(x)
            sage: f.substitute_function(foo(x)==bar(x+1))
            1/bar(pi*y + 1) + bar(x + 1)

        All substitutions are performed at the same time::

            sage: g = foo(x) + 1/bar(pi*y)
            sage: g.substitute_function({foo: bar, bar: foo})
            1/foo(pi*y) + bar(x)

        Any number of arguments is accepted::

            sage: g.substitute_function({foo: bar}, bar(x) == x^2)
            1/(pi^2*y^2) + bar(x)

        As well as lists of substitutions::

            sage: g.substitute_function([foo(x) == 1, bar(x) == x])
            1/(pi*y) + 1

        Alternative syntax::

            sage: g.substitute_function(foo, bar)
            1/bar(pi*y) + bar(x)

        Duplicate assignments will throw an error::

            sage: g.substitute_function({foo:bar}, foo(x) == x^2)
            Traceback (most recent call last):
            ...
            ValueError: duplicate substitution for foo, got values bar and x |--> x^2

            sage: g.substitute_function([foo(x) == x^2], foo = bar)
            Traceback (most recent call last):
            ...
            ValueError: duplicate substitution for foo, got values x |--> x^2 and bar

        TESTS:

        Make sure :issue:`17849` is fixed::

            sage: ex = sin(x) + atan2(0,0,hold=True)
            sage: ex.substitute_function(sin,cos)
            arctan2(0, 0) + cos(x)
            sage: ex = sin(x) + hypergeometric([1, 1], [2], -1)
            sage: ex.substitute_function(sin,cos)
            cos(x) + hypergeometric((1, 1), (2,), -1)"""
    def substitution_delayed(
        self, 
        pattern: CoercibleToExpression, 
        replacement: Callable[[Expression[P]], CoercibleToExpression | None]
    ) -> Any:
        """
        Replace all occurrences of pattern by the result of replacement.

        In contrast to :meth:`subs`, the pattern may contains wildcards
        and the replacement can depend on the particular term matched by the
        pattern.

        INPUT:

        - ``pattern`` -- an :class:`Expression`, usually containing wildcards

        - ``replacement`` -- a function; its argument is a dictionary
          mapping the wildcard occurring in ``pattern`` to the actual
          values.  If it returns ``None``, this occurrence of ``pattern`` is
          not replaced. Otherwise, it is replaced by the output of
          ``replacement``.

        OUTPUT: an :class:`Expression`

        EXAMPLES::

            sage: var('x y')
            (x, y)
            sage: w0 = SR.wild(0)
            sage: sqrt(1 + 2*x + x^2).substitution_delayed(
            ....:     sqrt(w0), lambda d: sqrt(factor(d[w0]))
            ....: )
            sqrt((x + 1)^2)
            sage: def r(d):
            ....:    if x not in d[w0].variables():
            ....:        return cos(d[w0])
            sage: (sin(x^2 + x) + sin(y^2 + y)).substitution_delayed(sin(w0), r)
            cos(y^2 + y) + sin(x^2 + x)

        .. SEEALSO::

            :meth:`match`"""
    def subtract_from_both_sides(self, x) -> Expression:
        """
        Return a relation obtained by subtracting ``x`` from both sides
        of this relation.

        EXAMPLES::

            sage: eqn = x*sin(x)*sqrt(3) + sqrt(2) > cos(sin(x))
            sage: eqn.subtract_from_both_sides(sqrt(2))
            sqrt(3)*x*sin(x) > -sqrt(2) + cos(sin(x))
            sage: eqn.subtract_from_both_sides(cos(sin(x)))
            sqrt(3)*x*sin(x) + sqrt(2) - cos(sin(x)) > 0"""
    # TODO: this uses sage.calculus.calculus.symbolic_sum
    def sum(self, *args, **kwds) -> Any:
        """
        Return the symbolic sum `\\sum_{v = a}^b` ``self``.

        with respect to the variable `v` with endpoints
        `a` and `b`.

        INPUT:

        - ``v`` -- a variable or variable name

        - ``a`` -- lower endpoint of the sum

        - ``b`` -- upper endpoint of the sum

        - ``algorithm`` -- (default: ``'maxima'``)  one of

          - ``'maxima'`` -- use Maxima (the default)
          - ``'maple'`` -- (optional) use Maple
          - ``'mathematica'`` -- (optional) use Mathematica
          - ``'giac'`` -- (optional) use Giac
          - ``'sympy'`` -- use SymPy

        EXAMPLES::

            sage: k, n = var('k,n')
            sage: k.sum(k, 1, n).factor()
            1/2*(n + 1)*n

        ::

            sage: (1/k^4).sum(k, 1, oo)
            1/90*pi^4

        ::

            sage: (1/k^5).sum(k, 1, oo)
            zeta(5)

        A well known binomial identity::

            sage: assume(n>=0)
            sage: binomial(n,k).sum(k, 0, n)
            2^n

        And some truncations thereof::

            sage: binomial(n,k).sum(k,1,n)
            2^n - 1
            sage: binomial(n,k).sum(k,2,n)
            2^n - n - 1
            sage: binomial(n,k).sum(k,0,n-1)
            2^n - 1
            sage: binomial(n,k).sum(k,1,n-1)
            2^n - 2

        The binomial theorem::

            sage: x, y = var('x, y')
            sage: (binomial(n,k) * x^k * y^(n-k)).sum(k, 0, n)
            (x + y)^n

        ::

            sage: (k * binomial(n, k)).sum(k, 1, n)
            2^(n - 1)*n

        ::

            sage: ((-1)^k*binomial(n,k)).sum(k, 0, n)
            0

        ::

            sage: (2^(-k)/(k*(k+1))).sum(k, 1, oo)
            -log(2) + 1

        Summing a hypergeometric term::

            sage: (binomial(n, k) * factorial(k) / factorial(n+1+k)).sum(k, 0, n)
            1/2*sqrt(pi)/factorial(n + 1/2)

        We check a well known identity::

            sage: bool((k^3).sum(k, 1, n) == k.sum(k, 1, n)^2)
            True

        A geometric sum::

            sage: a, q = var('a, q')
            sage: (a*q^k).sum(k, 0, n)
            (a*q^(n + 1) - a)/(q - 1)

        The geometric series::

            sage: assume(abs(q) < 1)
            sage: (a*q^k).sum(k, 0, oo)
            -a/(q - 1)

        A divergent geometric series.  Do not forget
        to `forget` your assumptions::

            sage: forget()
            sage: assume(q > 1)
            sage: (a*q^k).sum(k, 0, oo)
            Traceback (most recent call last):
            ...
            ValueError: Sum is divergent.

        This summation only Mathematica can perform::

            sage: (1/(1+k^2)).sum(k, -oo, oo, algorithm = 'mathematica')     # optional - mathematica
            pi*coth(pi)

        Use Giac to perform this summation::

            sage: # needs giac
            sage: (sum(1/(1+k^2), k, -oo, oo, algorithm = 'giac')).factor()
            pi*(e^(2*pi) + 1)/((e^pi + 1)*(e^pi - 1))

        Use Maple as a backend for summation::

            sage: (binomial(n,k)*x^k).sum(k, 0, n, algorithm = 'maple')      # optional - maple
            (x + 1)^n

        .. NOTE::

           #. Sage can currently only understand a subset of the output of Maxima, Maple and
              Mathematica, so even if the chosen backend can perform the summation the
              result might not be convertible into a usable Sage expression.

        TESTS:

        Check that the sum in :issue:`10682` is done right::

            sage: sum(binomial(n,k)*k^2, k, 2, n)
            1/4*(n^2 + n)*2^n - n

        This sum used to give a wrong result (:issue:`9635`) but
        now gives correct results with all relevant assumptions::

            sage: (n,k,j)=var('n,k,j')
            sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
            -(-1)^j*sum((-1)^k*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
            sage: assume(j>-1)
            sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
            1
            sage: forget()
            sage: assume(n>=j)
            sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
            -(-1)^j*sum((-1)^k*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
            sage: forget()
            sage: assume(j==-1)
            sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
            1
            sage: forget()
            sage: assume(j<-1)
            sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
            -(-1)^j*sum((-1)^k*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
            sage: forget()

        Check that :issue:`16176` is fixed::

            sage: n = var('n')
            sage: sum(log(1-1/n^2),n,2,oo)
            -log(2)

        Check that :issue:`21801` is fixed::

            sage: n = SR.var('n')
            sage: sum(1/((n+1)*(2*n-1)), n, 0, oo)
            2/3*log(2) - 2/3
            sage: _.n()
            -0.204568546293370
            sage: f(n) = (-1)^(n+1)/(3*n+6*(-1)^n)
            sage: sum(f(2*n)+f(2*n+1), n, 0, oo)
            1/3*log(2) - 1/3"""
    def tan(self, hold: bool = False) -> Expression[P]:
        """
        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: tan(x^2 + y^2)
            tan(x^2 + y^2)
            sage: tan(sage.symbolic.constants.pi/2)
            Infinity
            sage: tan(SR(1))
            tan(1)
            sage: tan(SR(RealField(150)(1)))
            1.5574077246549022305069748074583601730872508

        To prevent automatic evaluation use the ``hold`` argument::

            sage: (pi/12).tan()
            -sqrt(3) + 2
            sage: (pi/12).tan(hold=True)
            tan(1/12*pi)

        This also works using functional notation::

            sage: tan(pi/12,hold=True)
            tan(1/12*pi)
            sage: tan(pi/12)
            -sqrt(3) + 2

        To then evaluate again, we use :meth:`unhold`::

            sage: a = (pi/12).tan(hold=True); a.unhold()
            -sqrt(3) + 2

        TESTS::

            sage: SR(oo).tan()
            Traceback (most recent call last):
            ...
            RuntimeError: tan_eval(): tan(infinity) encountered
            sage: SR(-oo).tan()
            Traceback (most recent call last):
            ...
            RuntimeError: tan_eval(): tan(infinity) encountered
            sage: SR(unsigned_infinity).tan()
            Traceback (most recent call last):
            ...
            RuntimeError: tan_eval(): tan(infinity) encountered"""
    def tanh(self, hold: bool = False) -> Expression[P]:
        """
        Return tanh of ``self``.

        We have `\\tanh(x) = \\sinh(x) / \\cosh(x)`.

        EXAMPLES::

            sage: x.tanh()
            tanh(x)
            sage: SR(1).tanh()
            tanh(1)
            sage: SR(0).tanh()
            0
            sage: SR(1.0).tanh()
            0.761594155955765
            sage: maxima('tanh(1.0)')
            0.7615941559557649
            sage: plot(lambda x: SR(x).tanh(), -1, 1)                                   # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        To prevent automatic evaluation use the ``hold`` argument::

            sage: arcsinh(x).tanh()
            x/sqrt(x^2 + 1)
            sage: arcsinh(x).tanh(hold=True)
            tanh(arcsinh(x))

        This also works using functional notation::

            sage: tanh(arcsinh(x), hold=True)
            tanh(arcsinh(x))
            sage: tanh(arcsinh(x))
            x/sqrt(x^2 + 1)

        To then evaluate again, we use :meth:`unhold`::

            sage: a = arcsinh(x).tanh(hold=True); a.unhold()
            x/sqrt(x^2 + 1)

        TESTS::

            sage: SR(oo).tanh()
            1
            sage: SR(-oo).tanh()
            -1
            sage: SR(unsigned_infinity).tanh()
            Traceback (most recent call last):
            ...
            RuntimeError: tanh_eval(): tanh(unsigned_infinity) encountered"""
    @overload
    def taylor(
        self, 
        x: Expression, 
        a: ConvertibleToExpression, 
        n: ConvertibleToInteger, /) -> Expression[P]: ...
    @overload
    def taylor(
        self, 
        *args: tuple[ConvertibleToExpression, Any], 
        n: ConvertibleToInteger) -> Expression[P]:
        """
        Expand this symbolic expression in a truncated Taylor or
        Laurent series in the variable `v` around the point `a`,
        containing terms through `(x - a)^n`. Functions in more
        variables is also supported.

        INPUT:

        - ``*args`` -- the following notation is supported

           - ``x``, ``a``, ``n`` -- variable, point, degree

           - ``(x, a)``, ``(y, b)``, ``n`` -- variables with points, degree of polynomial

        .. SEEALSO::

            :meth:`series`

        EXAMPLES::

            sage: var('a, x, z')
            (a, x, z)
            sage: taylor(a*log(z), z, 2, 3)
            1/24*a*(z - 2)^3 - 1/8*a*(z - 2)^2 + 1/2*a*(z - 2) + a*log(2)

        ::

            sage: taylor(sqrt(sin(x) + a*x + 1), x, 0, 3)
            1/48*(3*a^3 + 9*a^2 + 9*a - 1)*x^3 - 1/8*(a^2 + 2*a + 1)*x^2 + 1/2*(a + 1)*x + 1

        ::

            sage: taylor(sqrt(x + 1), x, 0, 5)
            7/256*x^5 - 5/128*x^4 + 1/16*x^3 - 1/8*x^2 + 1/2*x + 1

        ::

            sage: taylor(1/log(x + 1), x, 0, 3)
            -19/720*x^3 + 1/24*x^2 - 1/12*x + 1/x + 1/2

        ::

            sage: taylor(cos(x) - sec(x), x, 0, 5)
            -1/6*x^4 - x^2

        ::

            sage: taylor((cos(x) - sec(x))^3, x, 0, 9)
            -1/2*x^8 - x^6

        ::

            sage: taylor(1/(cos(x) - sec(x))^3, x, 0, 5)
            -15377/7983360*x^4 - 6767/604800*x^2 + 11/120/x^2 + 1/2/x^4 - 1/x^6 - 347/15120

        TESTS:

        Check that issue :issue:`7472` is fixed (Taylor polynomial in
        more variables)::

            sage: x,y = var('x y'); taylor(x*y^3,(x,1),(y,1),4)
            (x - 1)*(y - 1)^3 + 3*(x - 1)*(y - 1)^2 + (y - 1)^3 + 3*(x - 1)*(y - 1) + 3*(y - 1)^2 + x + 3*y - 3
            sage: expand(_)
            x*y^3"""
    def test_relation(
        self, 
        ntests: SupportsInt = 20, 
        domain: Parent | None = None, 
        proof: bool = True
    ) -> Any:
        """
        Test this relation at several random values, attempting to find
        a contradiction. If this relation has no variables, it will also
        test this relation after casting into the domain.

        Because the interval fields never return false positives, we can be
        assured that if ``True`` or ``False`` is returned (and proof is
        ``False``) then the answer is correct.

        INPUT:

        - ``ntests`` -- (default: 20) the number of iterations to run
        - ``domain`` -- (optional) the domain from which to draw the random
          values defaults to ``CIF`` for equality testing and ``RIF`` for
          order testing
        - ``proof`` -- (default: ``True``) if ``False`` and the domain is an
          interval field, regard overlapping (potentially equal) intervals as
          equal, and return ``True`` if all tests succeeded.

        OUTPUT: boolean or ``NotImplemented``, meaning

        - ``True`` -- this relation holds in the domain and has no variables

        - ``False`` -- a contradiction was found

        - ``NotImplemented`` -- no contradiction found

        EXAMPLES::

            sage: (3 < pi).test_relation()
            True
            sage: (0 >= pi).test_relation()
            False
            sage: (exp(pi) - pi).n()
            19.9990999791895
            sage: (exp(pi) - pi == 20).test_relation()
            False
            sage: (sin(x)^2 + cos(x)^2 == 1).test_relation()
            NotImplemented
            sage: (sin(x)^2 + cos(x)^2 == 1).test_relation(proof=False)
            True
            sage: (x == 1).test_relation()
            False
            sage: var('x,y')
            (x, y)
            sage: (x < y).test_relation()
            False

        TESTS::

            sage: all_relations = [op for name, op in sorted(operator.__dict__.items()) if len(name) == 2]
            sage: all_relations
            [<built-in function eq>, <built-in function ge>, <built-in function gt>, <built-in function le>, <built-in function lt>, <built-in function ne>]
            sage: [op(3, pi).test_relation() for op in all_relations]
            [False, False, False, True, True, True]
            sage: [op(pi, pi).test_relation() for op in all_relations]
            [True, True, False, True, False, False]

            sage: s = 'some_very_long_variable_name_which_will_definitely_collide_if_we_use_a_reasonable_length_bound_for_a_hash_that_respects_lexicographic_order'
            sage: t1, t2 = var(','.join([s+'1',s+'2']))
            sage: (t1 == t2).test_relation()
            False
            sage: (cot(-x) == -cot(x)).test_relation()
            NotImplemented

        Check that :issue:`18896` is fixed::

            sage: m = 540579833922455191419978421211010409605356811833049025*sqrt(1/2)
            sage: m1 = 382247666339265723780973363167714496025733124557617743
            sage: (m == m1).test_relation(domain=QQbar)
            False
            sage: (m == m1).test_relation()
            False

        Try the examples from :issue:`31424` and :issue:`31665`::

            sage: k = 26
            sage: bool(2/(2*pi)^(2*k) <= abs(bernoulli(2*k)/factorial(2*k)))
            True
            sage: t = (log(17179815199/17179869184) +
            ....: 727717503781781876485802752874818120860129694543334299450155913077668355 /
            ....: 231584178474632390847141970017375815706539969331281128078915168015826259279872)
            sage: v = -53985/17179869184
            sage: bool(abs(t) < 1.213*2^-56*v^4)
            True"""
    def to_gamma(self) -> Expression[P]:
        """
        Convert factorial, binomial, and Pochhammer symbol
        expressions to their gamma function equivalents.

        EXAMPLES::

            sage: m,n = var('m n', domain='integer')
            sage: factorial(n).to_gamma()
            gamma(n + 1)
            sage: binomial(m,n).to_gamma()
            gamma(m + 1)/(gamma(m - n + 1)*gamma(n + 1))"""
    def trailing_coefficient(
        self, s: CoercibleToExpression | None = None) -> Expression[P]:
        """
        Return the trailing coefficient of s in ``self``, i.e., the coefficient
        of the smallest power of s in ``self``.

        EXAMPLES::

            sage: var('x,y,a')
            (x, y, a)
            sage: f = 100 + a*x + x^3*sin(x*y) + x*y + x/y + 2*sin(x*y)/x; f
            x^3*sin(x*y) + a*x + x*y + x/y + 2*sin(x*y)/x + 100
            sage: f.trailing_coefficient(x)
            2*sin(x*y)
            sage: f.trailing_coefficient(y)
            x
            sage: f.trailing_coefficient(sin(x*y))
            a*x + x*y + x/y + 100"""
    trailing_coeff = trailing_coefficient
    def truncate(self) -> Self: # ?
        """
        Given a power series or expression, return the corresponding
        expression without the big oh.

        INPUT:

        - ``self`` -- a series as output by the :meth:`series` command

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: f = sin(x)/x^2
            sage: f.truncate()
            sin(x)/x^2
            sage: f.series(x,7)
            1*x^(-1) + (-1/6)*x + 1/120*x^3 + (-1/5040)*x^5 + Order(x^7)
            sage: f.series(x,7).truncate()
            -1/5040*x^5 + 1/120*x^3 - 1/6*x + 1/x
            sage: f.series(x==1,3).truncate().expand()
            -2*x^2*cos(1) + 5/2*x^2*sin(1) + 5*x*cos(1) - 7*x*sin(1) - 3*cos(1) + 11/2*sin(1)"""
    def unhold(self, exclude: Iterable[Callable] | None = None) -> Expression[P]:
        """
        Evaluates any held operations (with the ``hold`` keyword) in the
        expression

        INPUT:

        - ``self`` -- an expression with held operations
        - ``exclude`` -- (default: ``None``) a list of operators to exclude from
          evaluation. Excluding arithmetic operators does not yet work (see
          :issue:`10169`).

        OUTPUT:

        A new expression with held operations, except those in ``exclude``,
        evaluated

        EXAMPLES::

            sage: a = exp(I * pi, hold=True)
            sage: a
            e^(I*pi)
            sage: a.unhold()
            -1
            sage: b = x.add(x, hold=True)
            sage: b
            x + x
            sage: b.unhold()
            2*x
            sage: (a + b).unhold()
            2*x - 1
            sage: c = (x.mul(x, hold=True)).add(x.mul(x, hold=True), hold=True)
            sage: c
            x*x + x*x
            sage: c.unhold()
            2*x^2
            sage: sin(tan(0, hold=True), hold=True).unhold()
            0
            sage: sin(tan(0, hold=True), hold=True).unhold(exclude=[sin])
            sin(0)
            sage: (e^sgn(0, hold=True)).unhold()
            1
            sage: (e^sgn(0, hold=True)).unhold(exclude=[exp])
            e^0
            sage: log(3).unhold()
            log(3)"""
    def unit(self, s: CoercibleToExpression) ->  Expression[P]:
        """
        Return the unit of this expression when considered as a
        polynomial in ``s``.

        See also :meth:`content`, :meth:`primitive_part`, and
        :meth:`unit_content_primitive`.

        INPUT:

        - ``s`` -- a symbolic expression

        OUTPUT:

        The unit part of a polynomial as a symbolic expression. It is
        defined as the sign of the leading coefficient.

        EXAMPLES::

            sage: (2*x+4).unit(x)
            1
            sage: (-2*x+1).unit(x)
            -1
            sage: (2*x+1/2).unit(x)
            1
            sage: var('y')
            y
            sage: (2*x - 4*sin(y)).unit(sin(y))
            -1"""
    def unit_content_primitive(self, s: CoercibleToExpression) ->  Expression[P]:
        """
        Return the factorization into unit, content, and primitive part.

        INPUT:

        - ``s`` -- a symbolic expression, usually a symbolic
          variable. The whole symbolic expression ``self`` will be
          considered as a univariate polynomial in ``s``.

        OUTPUT:

        A triple (unit, content, primitive polynomial)` containing the
        :meth:`unit <unit>`, :meth:`content <content>`, and
        :meth:`primitive polynomial <primitive_part>`. Their product equals
        ``self``.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: ex = 9*x^3*y+3*y
            sage: ex.unit_content_primitive(x)
            (1, 3*y, 3*x^3 + 1)
            sage: ex.unit_content_primitive(y)
            (1, 9*x^3 + 3, y)"""
    def variables(self) -> tuple[Expression[SymbolicRing]]:
        """
        Return sorted tuple of variables that occur in this expression.

        EXAMPLES::

            sage: (x,y,z) = var('x,y,z')
            sage: (x+y).variables()
            (x, y)
            sage: (2*x).variables()
            (x,)
            sage: (x^y).variables()
            (x, y)
            sage: sin(x+y^z).variables()
            (x, y, z)"""
    def zeta(self, hold: bool = False) -> Expression[P]:
        """
        EXAMPLES::

            sage: x, y = var('x, y')
            sage: (x/y).zeta()
            zeta(x/y)
            sage: SR(2).zeta()
            1/6*pi^2
            sage: SR(3).zeta()
            zeta(3)
            sage: SR(CDF(0,1)).zeta()  # abs tol 1e-16                                  # needs sage.libs.pari
            0.003300223685324103 - 0.4181554491413217*I
            sage: CDF(0,1).zeta()  # abs tol 1e-16                                      # needs sage.libs.pari
            0.003300223685324103 - 0.4181554491413217*I
            sage: plot(lambda x: SR(x).zeta(), -10,10).show(ymin=-3, ymax=3)            # needs sage.plot

        To prevent automatic evaluation use the ``hold`` argument::

            sage: SR(2).zeta(hold=True)
            zeta(2)

        This also works using functional notation::

            sage: zeta(2, hold=True)
            zeta(2)
            sage: zeta(2)
            1/6*pi^2

        To then evaluate again, we use :meth:`unhold`::

            sage: a = SR(2).zeta(hold=True); a.unhold()
            1/6*pi^2

        TESTS::

            sage: t = SR(1).zeta(); t
            Infinity"""
    def __abs__(self) -> Expression[P]:
        """
        Return the absolute value of this expression.

        EXAMPLES::

            sage: var('x, y')
            (x, y)

        The absolute value of a symbolic expression::

            sage: abs(x^2+y^2)
            abs(x^2 + y^2)

        The absolute value of a number in the symbolic ring::

            sage: abs(SR(-5))
            5
            sage: type(abs(SR(-5)))
            <class 'sage.symbolic.expression.Expression'>

        Because this overrides a Python builtin function, we do not
        currently support a ``hold`` parameter to prevent automatic
        evaluation::

            sage: abs(SR(-5),hold=True)
            Traceback (most recent call last):
            ...
            TypeError: ...abs() takes no keyword arguments

        But this is possible using the method :meth:`abs`::

            sage: SR(-5).abs(hold=True)
            abs(-5)

        TESTS:

        Check if :issue:`11155` is fixed::

            sage: abs(pi+i)
            abs(pi + I)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __call__(self, **kwds: CoercibleToExpression) -> Expression[P]: ...
    @overload
    def __call__(
        self, 
        d: dict[CoercibleToExpression, CoercibleToExpression], 
        /, **kwds: CoercibleToExpression) -> Expression[P]:
        """
        Call the :meth:`subs` on this expression.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: (x+y)(x=z^2, y=x^y)
            z^2 + x^y"""
    def __complex__(self) -> complex:
        """
        EXAMPLES::

            sage: complex(I)
            1j
            sage: complex(erf(3*I))
            1629.9946226015657j"""
    def __copy__(self) -> Expression[P]:
        """
        TESTS::

            sage: copy(x)
            x"""
    def __enter__(self) -> Self:
        """
        Method used by temporary variables with Python `with` to
        automatically clean up after themselves."""
    def __exit__(self, *args: _NotUsed) -> Literal[False]:
        """
        Method used by temporary variables with Python `with` to
        automatically clean up after themselves.

        TESTS::

            sage: symbols_copy = SR.symbols.copy()
            sage: with SR.temp_var() as t: pass
            sage: symbols_copy == SR.symbols
            True"""
    def __float__(self) -> float:
        """
        Return float conversion of ``self``, assuming ``self`` is constant.

        Otherwise, raise a :exc:`TypeError`.

        OUTPUT: a ``float``. Double precision evaluation of ``self``

        EXAMPLES::

            sage: float(SR(12))
            12.0
            sage: float(SR(2/3))
            0.6666666666666666
            sage: float(sqrt(SR(2)))
            1.4142135623730951
            sage: float(SR(RIF(2)))
            2.0
            sage: float(x^2 + 1)
            Traceback (most recent call last):
            ...
            TypeError: unable to simplify to float approximation

        TESTS::

            sage: float(sqrt(2)/sqrt(abs(-(I - 1)*sqrt(2) - I - 1)))
            0.9036020036..."""
    def __getstate__(self) -> tuple[Literal[0], list[str], str]:
        """
        Return a tuple describing the state of this expression for pickling.

        This should return all information that will be required to unpickle
        the object. The functionality for unpickling is implemented in
        __setstate__().

        In order to pickle Expression objects, we return a tuple containing

         * 0  - as pickle version number
                in case we decide to change the pickle format in the feature
         * names of symbols of this expression
         * a string representation of ``self`` stored in a Pynac archive.

        TESTS::

            sage: var('x,y,z')
            (x, y, z)
            sage: t = 2*x*y^z+3
            sage: s = dumps(t)

            sage: t.__getstate__()
            (0,
             ['x', 'y', 'z'],
             ...)
        """
    def __hash__(self) -> int:
        """
        Return hash of this expression.

        EXAMPLES:

        The hash of an object in Python or its coerced version into
        the symbolic ring is usually the same::

            sage: hash(SR(3.1)) == hash(3.1)
            True
            sage: hash(SR(19.23)) == hash(19.23)
            True
            sage: hash(SR(3/1))
            3
            sage: hash(SR(19/23)) == hash(19/23)
            True
            sage: hash(SR(2^32)) == hash(2^32)
            True
            sage: hash(SR(2^64-1)) == hash(2^64-1)
            True
            sage: hash(SR(1e100)) == hash(1e100)
            True

        The hash for symbolic expressions are unfortunately random. Here we
        only test that the hash() function returns without error, and that
        the return type is correct::

            sage: x, y = var("x y")
            sage: t = hash(x); type(t)
            <... \'int\'>
            sage: t = hash(x^y); type(t)
            <... \'int\'>
            sage: type(hash(x+y))
            <... \'int\'>
            sage: d = {x+y: 5}
            sage: d
            {x + y: 5}

        In this example hashing is important otherwise the answer is
        wrong::

            sage: set([x-x, -x+x])
            {0}

        Test if exceptions during hashing are handled properly::

            sage: t = SR(matrix(2,2,range(4)))
            sage: hash(t)
            Traceback (most recent call last):
            ...
            RuntimeError: Python object not hashable

        TESTS:

        Test if hashes for fderivatives with different parameters collide.
        :issue:`6243`::

            sage: f = function(\'f\'); t = f(x,y)
            sage: u = t.derivative(x); v = t.derivative(y)
            sage: hash(u) == hash(v)
            False
            sage: d = {u: 3, v: 5}; sorted(d.values())
            [3, 5]

        More checks for fderivative hashes :issue:`6851` ::

            sage: hash(f(x).derivative(x)) == hash(f(x).derivative(x,2))
            False
            sage: d = dict( (f(x).derivative(x, i), i) for i in range(1,6) )
            sage: len(d.keys())
            5

        We create a function with 10 arguments and test if there are
        hash collisions between any of its derivatives of order at
        most 7. :issue:`7508` ::

            sage: num_vars = 10; max_order=7
            sage: X = var(\' \'.join(\'x\' + str(i) for i in range(num_vars)))
            sage: f = function(\'f\')(*X)
            sage: hashes = set()
            sage: for length in range(1,max_order+1):  # long time (4s on sage.math, 2012)
            ....:     for s in UnorderedTuples(X, length):
            ....:         deriv = f.diff(*s)
            ....:         h = hash(deriv)
            ....:         if h in hashes:
            ....:             print("deriv: %s, hash:%s" % (deriv, h))
            ....:         else:
            ....:             hashes.add(n)

        Check whether `oo` keeps its hash in `SR` (:issue:`19928`)::

            sage: hash(oo) == hash(SR(oo))
            True
            sage: hash(oo) == hash((-x).subs(x=-oo))
            True
            sage: hash(-oo) == hash(SR(-oo))
            True
            sage: hash(-oo) == hash((-x).subs(x=oo))
            True
            sage: hash(unsigned_infinity) == hash(SR(unsigned_infinity))
            True

        Check a corner case for rational numbers (:issue:`28219`)::

            sage: hash(-1/3) == hash(SR(-1/3))
            True"""
    def __index__(self) -> int:
        """
        EXAMPLES::

            sage: a = list(range(10))
            sage: a[:SR(5)]
            [0, 1, 2, 3, 4]"""
    def __int__(self) -> int:
        """
        EXAMPLES::

            sage: int(log(8)/log(2))
            3
            sage: int(-log(8)/log(2))
            -3
            sage: int(sin(2)*100)
            90
            sage: int(-sin(2)*100)
            -90
            sage: int(SR(3^64)) == 3^64
            True
            sage: int(SR(10^100)) == 10^100
            True
            sage: int(SR(10^100-10^-100)) == 10^100 - 1
            True
            sage: int(sqrt(-3))
            Traceback (most recent call last):
            ...
            ValueError: cannot convert sqrt(-3) to int"""
    def __invert__(self) -> Self:
        """
        Return the inverse of this symbolic expression.

        EXAMPLES::

            sage: ~x
            1/x
            sage: ~SR(3)
            1/3
            sage: v1=var('v1'); a = (2*erf(2*v1*arcsech(1/2))/v1); ~a
            1/2*v1/erf(2*v1*arcsech(1/2))"""
    def __setstate__( # pyright: ignore[reportIncompatibleMethodOverride]
        self, state: tuple[Literal[0], list[str], str]
    ) -> None:
        """
        Initialize the state of the object from data saved in a pickle.

        During unpickling __init__ methods of classes are not called, the saved
        data is passed to the class via this function instead.

        TESTS::

            sage: var('x,y,z')
            (x, y, z)
            sage: t = 2*x*y^z+3
            sage: u = loads(dumps(t)) # indirect doctest
            sage: u
            2*x*y^z + 3
            sage: bool(t == u)
            True
            sage: u.subs(x=z)
            2*y^z*z + 3

            sage: loads(dumps(x.parent()(2)))
            2
        """

@overload
def solve_diophantine( # pyright: ignore[reportOverlappingOverload]
    f: ConvertibleToExpression, 
    x: (
        Expression[SymbolicRing] 
        | tuple[Expression[SymbolicRing], ...] 
        | list[Expression[SymbolicRing]] 
        | None ) = None, 
    solution_dict: Literal[True] = ...
) -> list[dict[Expression[SymbolicRing], Expression[SymbolicRing]]]: ...
@overload
def solve_diophantine(
    f: ConvertibleToExpression, 
    x: (
        Expression[SymbolicRing] 
        | tuple[Expression[SymbolicRing], ...] 
        | list[Expression[SymbolicRing]] 
        | None ) = None, 
    solution_dict: Literal[False] = False
) -> list[Expression[SymbolicRing]] | list[tuple[Expression[SymbolicRing], ...]]:
    """
    Solve a Diophantine equation.

    The argument, if not given as symbolic equation, is set equal to zero.
    It can be given in any form that can be converted to symbolic. Please
    see :meth:`Expression.solve_diophantine` for a detailed
    synopsis.

    EXAMPLES::

        sage: R.<a,b> = PolynomialRing(ZZ); R
        Multivariate Polynomial Ring in a, b over Integer Ring
        sage: solve_diophantine(a^2 - 3*b^2 + 1)
        []
        sage: sorted(solve_diophantine(a^2 - 3*b^2 + 2), key=str)
        [(-1/2*sqrt(3)*(sqrt(3) + 2)^t + 1/2*sqrt(3)*(-sqrt(3) + 2)^t - 1/2*(sqrt(3) + 2)^t - 1/2*(-sqrt(3) + 2)^t,
          -1/6*sqrt(3)*(sqrt(3) + 2)^t + 1/6*sqrt(3)*(-sqrt(3) + 2)^t - 1/2*(sqrt(3) + 2)^t - 1/2*(-sqrt(3) + 2)^t),
          (1/2*sqrt(3)*(sqrt(3) + 2)^t - 1/2*sqrt(3)*(-sqrt(3) + 2)^t + 1/2*(sqrt(3) + 2)^t + 1/2*(-sqrt(3) + 2)^t,
           1/6*sqrt(3)*(sqrt(3) + 2)^t - 1/6*sqrt(3)*(-sqrt(3) + 2)^t + 1/2*(sqrt(3) + 2)^t + 1/2*(-sqrt(3) + 2)^t)]
    """

class ExpressionIterator[P: SymbolicRingABC]:
    def __iter__(self) -> Self:
        """
        Return this iterator object itself.

        EXAMPLES::

            sage: x,y,z = var('x,y,z')
            sage: i = (x+y).iterator()
            sage: iter(i) is i
            True"""
    def __next__(self) -> Expression[P]:
        """
        Return the next component of the expression.

        EXAMPLES::

            sage: x,y,z = var('x,y,z')
            sage: i = (x+y).iterator()
            sage: next(i)
            x"""

def new_Expression[P: SymbolicRingABC](parent: P, x: ConvertibleToExpression) -> Expression[P]:
    r"""
    Convert ``x`` into the symbolic expression ring ``parent``.

    This is the element constructor.

    EXAMPLES::

        sage: a = SR(-3/4); a
        -3/4
        sage: type(a)
        <class 'sage.symbolic.expression.Expression'>
        sage: a.parent()
        Symbolic Ring
        sage: K.<a> = QuadraticField(-3)                                                # needs sage.rings.number_field
        sage: a + sin(x)                                                                # needs sage.rings.number_field
        I*sqrt(3) + sin(x)
        sage: x = var('x'); y0,y1 = PolynomialRing(ZZ,2,'y').gens()
        sage: x+y0/y1
        x + y0/y1
        sage: x.subs(x=y0/y1)
        y0/y1
        sage: x + int(1)
        x + 1
    """
def new_Expression_from_pyobject[P: SymbolicRingABC](
    parent: P, x: object, force: bool = True, recursive: bool = True) -> Expression[P]:
    r"""
    Wrap the given Python object in a symbolic expression even if it
    cannot be coerced to the Symbolic Ring.

    INPUT:

    - ``parent`` -- a symbolic ring

    - ``x`` -- a Python object

    - ``force`` -- boolean (default: ``True``); if ``True``, the Python object
      is taken as is without attempting coercion or list traversal

    - ``recursive`` -- boolean (default: ``True``); disables recursive
      traversal of lists

    EXAMPLES::

        sage: t = SR._force_pyobject(QQ); t   # indirect doctest
        Rational Field
        sage: type(t)
        <class 'sage.symbolic.expression.Expression'>

        sage: from sage.symbolic.expression import new_Expression_from_pyobject
        sage: t = new_Expression_from_pyobject(SR, 17); t
        17
        sage: type(t)
        <class 'sage.symbolic.expression.Expression'>

        sage: t2 = new_Expression_from_pyobject(SR, t, False); t2
        17
        sage: t2 is t
        True

        sage: tt = new_Expression_from_pyobject(SR, t, True); tt
        17
        sage: tt is t
        False
    """
def new_Expression_wild[P: SymbolicRingABC](parent: P, n: _uint = 0) -> Expression[P]:
    r"""
    Return the n-th wild-card for pattern matching and substitution.

    INPUT:

    - ``parent`` -- a symbolic ring

    - ``n`` -- nonnegative integer

    OUTPUT: n-th wildcard expression

    EXAMPLES::

        sage: x,y = var('x,y')
        sage: w0 = SR.wild(0); w1 = SR.wild(1)
        sage: pattern = sin(x)*w0*w1^2; pattern
        $1^2*$0*sin(x)
        sage: f = atan(sin(x)*3*x^2); f
        arctan(3*x^2*sin(x))
        sage: f.has(pattern)
        True
        sage: f.subs(pattern == x^2)
        arctan(x^2)
    """
def new_Expression_symbol[P: SymbolicRingABC](
    parent: P, 
    name: str | None = None, 
    latex_name: str | None = None, 
    domain: str | None = None
) -> Expression[P]:
    r"""
    Look up or create a symbol.

    EXAMPLES::

        sage: t0 = SR.symbol("t0")
        sage: t0.conjugate()
        conjugate(t0)

        sage: t1 = SR.symbol("t1", domain='real')
        sage: t1.conjugate()
        t1

        sage: t0.abs()
        abs(t0)

        sage: t0_2 = SR.symbol("t0", domain='positive')
        sage: t0_2.abs()
        t0
        sage: bool(t0_2 == t0)
        True
        sage: t0.conjugate()
        t0

        sage: SR.symbol() # temporary variable
        symbol...
    """

class hold_class:
    """
        Instances of this class can be used with Python `with`.

        EXAMPLES::

            sage: with hold:
            ....:     tan(1/12*pi)
            ....:
            tan(1/12*pi)
            sage: tan(1/12*pi)
            -sqrt(3) + 2
            sage: with hold:
            ....:     2^5
            ....:
            32
            sage: with hold:
            ....:     SR(2)^5
            ....:
            2^5
            sage: with hold:
            ....:     t=tan(1/12*pi)
            ....:
            sage: t
            tan(1/12*pi)
            sage: t.unhold()
            -sqrt(3) + 2
    """

    def start(self) -> None:
        """
        Start a hold context.

        EXAMPLES::

            sage: hold.start()
            sage: SR(2)^5
            2^5
            sage: hold.stop()
            sage: SR(2)^5
            32"""
    def stop(self) -> None:
        """
        Stop any hold context.

        EXAMPLES::

            sage: hold.start()
            sage: SR(2)^5
            2^5
            sage: hold.stop()
            sage: SR(2)^5
            32"""
    def __enter__(self) -> None:
        """
        EXAMPLES::

            sage: hold.__enter__()
            sage: SR(2)^5
            2^5
            sage: hold.__exit__()
            sage: SR(2)^5
            32
        """
    def __exit__(self, *args: _NotUsed) -> None:
        """
        EXAMPLES::

            sage: hold.__enter__()
            sage: SR(2)^5
            2^5
            sage: hold.__exit__()
            sage: SR(2)^5
            32"""

hold: hold_class

def print_order(lhs: ConvertibleToExpression, rhs: ConvertibleToExpression) -> Literal[-1, 0, 1]:
    """
    Comparison in the print order

    INPUT:

    - ``lhs``, ``rhs`` -- two symbolic expressions or something that
      can be converted to one

    OUTPUT:

    Either `-1`, `0`, or `+1` indicating the comparison. An exception
    is raised if the arguments cannot be converted into the symbolic
    ring.

    EXAMPLES::

        sage: from sage.symbolic.expression import print_order
        sage: print_order(1, oo)
        1
        sage: print_order(e, oo)
        -1
        sage: print_order(pi, oo)
        1
        sage: print_order(1, sqrt(2))
        1

    Check that :issue:`12967` is fixed::

        sage: print_order(SR(oo), sqrt(2))
        1
    """
def print_sorted[T: ConvertibleToExpression](expressions: Iterable[T]) -> list[T]:
    """
    Sort a list in print order.

    INPUT:

    - ``expressions`` -- list/tuple/iterable of symbolic
      expressions, or something that can be converted to one

    OUTPUT: the list sorted by :meth:`print_order`

    EXAMPLES::

        sage: from sage.symbolic.expression import print_sorted
        sage: print_sorted([SR(1), SR(e), SR(pi), sqrt(2)])
        [e, sqrt(2), pi, 1]
    """
def math_sorted[T: ConvertibleToExpression](expressions: Iterable[T]) -> list[T]:
    """
    Sort a list of symbolic numbers in the "Mathematics" order.

    INPUT:

    - ``expressions`` -- list/tuple/iterable of symbolic
      expressions, or something that can be converted to one

    OUTPUT:

    The list sorted by ascending (real) value. If an entry does not
    define a real value (or plus/minus infinity), or if the comparison
    is not known, a :exc:`ValueError` is raised.

    EXAMPLES::

        sage: from sage.symbolic.expression import math_sorted
        sage: math_sorted([SR(1), SR(e), SR(pi), sqrt(2)])
        [1, sqrt(2), e, pi]
    """
def mixed_order(lhs: ConvertibleToExpression, rhs: ConvertibleToExpression) -> Literal[-1, 0, 1]:
    """
    Comparison in the mixed order

    INPUT:

    - ``lhs``, ``rhs`` -- two symbolic expressions or something that
      can be converted to one

    OUTPUT:

    Either `-1`, `0`, or `+1` indicating the comparison. An exception
    is raised if the arguments cannot be converted into the symbolic
    ring.

    EXAMPLES::

        sage: from sage.symbolic.expression import mixed_order
        sage: mixed_order(1, oo)
        -1
        sage: mixed_order(e, oo)
        -1
        sage: mixed_order(pi, oo)
        -1
        sage: mixed_order(1, sqrt(2))
        -1
        sage: mixed_order(x + x^2, x*(x+1))
        -1

    Check that :issue:`12967` is fixed::

        sage: mixed_order(SR(oo), sqrt(2))
        1

    Ensure that :issue:`32185` is fixed::

        sage: mixed_order(pi, 0)
        1
        sage: mixed_order(golden_ratio, 0)
        1
        sage: mixed_order(log2, 0)
        1
    """
def mixed_sorted[T: ConvertibleToExpression](expressions: Iterable[T]) -> list[T]:
    """
    Sort a list of symbolic numbers in the "Mixed" order.

    INPUT:

    - ``expressions`` -- list/tuple/iterable of symbolic
      expressions, or something that can be converted to one

    OUTPUT:

    In the list the numeric values are sorted by ascending (real) value,
    and the expressions with variables according to print order.
    If an entry does not
    define a real value (or plus/minus infinity), or if the comparison
    is not known, a :exc:`ValueError` is raised.

    EXAMPLES::

        sage: from sage.symbolic.expression import mixed_sorted
        sage: mixed_sorted([SR(1), SR(e), SR(pi), sqrt(2), x, sqrt(x), sin(1/x)])
        [1, sqrt(2), e, pi, sin(1/x), sqrt(x), x]
    """

class E(Expression):
    """E()"""
    
    def __init__(self):
        """
                Dummy class to represent base of the natural logarithm.

                The base of the natural logarithm ``e`` is not a constant in GiNaC/Sage.
                It is represented by ``exp(1)``.

                This class provides a dummy object that behaves well under addition,
                multiplication, etc. and on exponentiation calls the function ``exp``.

                EXAMPLES:

                The constant defined at the top level is just ``exp(1)``::

                    sage: e.operator()
                    exp
                    sage: e.operands()
                    [1]

                Arithmetic works::

                    sage: e + 2
                    e + 2
                    sage: 2 + e
                    e + 2
                    sage: 2*e
                    2*e
                    sage: e*2
                    2*e
                    sage: x*e
                    x*e
                    sage: var('a,b')
                    (a, b)
                    sage: t = e^(a+b); t
                    e^(a + b)
                    sage: t.operands()
                    [a + b]

                Numeric evaluation, conversion to other systems, and pickling works
                as expected. Note that these are properties of the :func:`exp` function,
                not this class::

                    sage: RR(e)
                    2.71828182845905
                    sage: R = RealField(200); R
                    Real Field with 200 bits of precision
                    sage: R(e)
                    2.7182818284590452353602874713526624977572470936999595749670
                    sage: em = 1 + e^(1-e); em
                    e^(-e + 1) + 1
                    sage: R(em)
                    1.1793740787340171819619895873183164984596816017589156131574
                    sage: maxima(e).float()
                    2.718281828459045
                    sage: t = mathematica(e)               # optional - mathematica
                    sage: t                                # optional - mathematica
                    E
                    sage: float(t)                         # optional - mathematica
                    2.718281828459045...

                    sage: loads(dumps(e))
                    e

                    sage: float(e)
                    2.718281828459045...
                    sage: e.__float__()
                    2.718281828459045...
                    sage: e._mpfr_(RealField(100))
                    2.7182818284590452353602874714
                    sage: e._real_double_(RDF)   # abs tol 5e-16
                    2.718281828459045
                    sage: import sympy                                                          # needs sympy
                    sage: sympy.E == e  # indirect doctest                                      # needs sympy
                    True

                TESTS::

                    sage: t = e^a; t
                    e^a
                    sage: t^b
                    (e^a)^b
                    sage: SR(1).exp()
                    e

                Testing that it works with matrices (see :issue:`4735`)::

                    sage: m = matrix(QQ, 2, 2, [1,0,0,1])
                    sage: e^m
                    [e 0]
                    [0 e]
        """
    @overload
    def __pow__(left, right: ConvertibleToExpression, dummy: _NotUsed) -> Expression[SymbolicRing]: ...
    @overload
    def __pow__[T](left, right: SupportsExp[T], dummy: _NotUsed) -> T: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Call the `exp` function when taking powers of `e`.

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: t = e^a; t
            e^a
            sage: t.operator()
            exp
            sage: t.operands()
            [a]

        This applies to the unit argument as well::

            sage: u = SR(1).exp()^a; u
            e^a
            sage: u.operator()
            exp
            sage: u.operands()
            [a]

        It also works with matrices (see :issue:`4735`)::

            sage: m = matrix(QQ, 2, 2, [1,0,0,1])
            sage: e^m
            [e 0]
            [0 e]
            sage: A = matrix(RDF, [[1,2],[3,4]])
            sage: e^A  # rel tol 5e-14
            [51.968956198705044  74.73656456700327]
            [112.10484685050491 164.07380304920997]"""
    def __rpow__(self, other) -> Expression[SymbolicRing]: ...

def normalize_index_for_doctests(arg: SupportsInt, nops: SupportsInt) -> int:
    """
    Wrapper function to test ``normalize_index``.

    TESTS::

        sage: from sage.symbolic.expression import normalize_index_for_doctests
        sage: normalize_index_for_doctests(-1, 4)
        3
    """

class OperandsWrapper(SageObject):
    """
        Operands wrapper for symbolic expressions.

        EXAMPLES::

            sage: x,y,z = var('x,y,z')
            sage: e = x + x*y + z^y + 3*y*z; e
            x*y + 3*y*z + x + z^y
            sage: e.op[1]
            3*y*z
            sage: e.op[1,1]
            z
            sage: e.op[-1]
            z^y
            sage: e.op[1:]
            [3*y*z, x, z^y]
            sage: e.op[:2]
            [x*y, 3*y*z]
            sage: e.op[-2:]
            [x, z^y]
            sage: e.op[:-2]
            [x*y, 3*y*z]
            sage: e.op[-5]
            Traceback (most recent call last):
            ...
            IndexError: operand index out of range, got -5, expect between -4 and 3
            sage: e.op[5]
            Traceback (most recent call last):
            ...
            IndexError: operand index out of range, got 5, expect between -4 and 3
            sage: e.op[1,1,0]
            Traceback (most recent call last):
            ...
            TypeError: expressions containing only a numeric coefficient, constant or symbol have no operands
            sage: e.op[:1.5]
            Traceback (most recent call last):
            ...
            TypeError: slice indices must be integers or None or have an __index__ method
            sage: e.op[:2:1.5]
            Traceback (most recent call last):
            ...
            ValueError: step value must be an integer
    """
    
    def __getitem__(
        self, arg: slice | list[SupportsInt] | tuple[SupportsInt, ...] | SupportsInt
    ) -> Expression:
        """
        TESTS::

           sage: t = 1+x+x^2
           sage: t.op[1:]
           [x, 1]"""
    def __reduce__(self) -> tuple[Callable[[Expression], Callable], Expression]:
        """
        TESTS::

            sage: (x^2).op.__reduce__()
            (<cyfunction restore_op_wrapper at ...>, (x^2,))
            sage: loads(dumps((x^2).op))
            Operands of x^2"""

def restore_op_wrapper(expr: Expression) -> Callable:
    """
    TESTS::

        sage: from sage.symbolic.expression import restore_op_wrapper
        sage: restore_op_wrapper(x^2)
        Operands of x^2
    """

class PynacConstant:
    def expression(self) -> Expression[SymbolicRing]:
        """
        Return this constant as an Expression.

        EXAMPLES::

            sage: from sage.symbolic.expression import PynacConstant
            sage: f = PynacConstant('foo', 'foo', 'real')
            sage: f + 2
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +: '<class 'sage.symbolic.expression.PynacConstant'>' and 'Integer Ring'

            sage: foo = f.expression(); foo
            foo
            sage: foo + 2
            foo + 2"""
    def name(self) -> str:
        """
        Return the name of this constant.

        EXAMPLES::

            sage: from sage.symbolic.expression import PynacConstant
            sage: f = PynacConstant('foo', 'foo', 'real')
            sage: f.name()
            'foo'"""
    def serial(self) -> int:
        """
        Return the underlying Pynac serial for this constant.

        EXAMPLES::

            sage: from sage.symbolic.expression import PynacConstant
            sage: f = PynacConstant('foo', 'foo', 'real')
            sage: f.serial()  #random
            15"""

def call_registered_function[P: SymbolicRingABC](
    serial: SupportsInt,
    nargs: SupportsInt,
    args: list,
    hold: bool,
    allow_numeric_result: bool,
    result_parent: P
) -> Expression[P]:
    r"""
    Call a function registered with Pynac (GiNaC).

    INPUT:

    - ``serial`` -- serial number of the function

    - ``nargs`` -- declared number of args (0 is variadic)

    - ``args`` -- list of arguments to pass to the function;
      each must be an :class:`Expression`

    - ``hold`` -- whether to leave the call unevaluated

    - ``allow_numeric_result`` -- if ``True``, keep numeric results numeric;
      if ``False``, make all results symbolic expressions

    - ``result_parent`` -- an instance of :class:`SymbolicRing`

    EXAMPLES::

        sage: from sage.symbolic.expression import find_registered_function, call_registered_function
        sage: s_arctan = find_registered_function('arctan', 1)
        sage: call_registered_function(s_arctan, 1, [SR(1)], False, True, SR)
        1/4*pi
        sage: call_registered_function(s_arctan, 1, [SR(1)], True, True, SR)
        arctan(1)
        sage: call_registered_function(s_arctan, 1, [SR(0)], False, True, SR)
        0
        sage: call_registered_function(s_arctan, 1, [SR(0)], False, True, SR).parent()
        Integer Ring
        sage: call_registered_function(s_arctan, 1, [SR(0)], False, False, SR).parent()
        Symbolic Ring
    """
def find_registered_function(name, nargs: SupportsInt) -> int:
    r"""
    Look up a function registered with Pynac (GiNaC).

    Raise a :exc:`ValueError` if the function is not registered.

    OUTPUT: serial number of the function, for use in :func:`call_registered_function`

    EXAMPLES::

        sage: from sage.symbolic.expression import find_registered_function
        sage: find_registered_function('arctan', 1)  # random
        19
        sage: find_registered_function('archenemy', 1)
        Traceback (most recent call last):
        ...
        ValueError: cannot find GiNaC function with name archenemy and 1 arguments
    """
def register_or_update_function(
    self: Callable, name: str, latex_name: str, nargs: SupportsInt,
    evalf_params_first, update: bool) -> int:
    r"""
    Register the function ``self`` with Pynac (GiNaC).

    OUTPUT: serial number of the function, for use in :func:`call_registered_function`

    EXAMPLES::

        sage: from sage.symbolic.function import BuiltinFunction
        sage: class Archosaurian(BuiltinFunction):
        ....:     def __init__(self):
        ....:         BuiltinFunction.__init__(self, 'archsaur', nargs=1)
        ....:     def _eval_(self, x):
        ....:         return x * exp(x)
        sage: archsaur = Archosaurian()  # indirect doctest
        sage: archsaur(2)
        2*e^2
    """
def get_sfunction_from_serial(serial: SupportsInt) -> SymbolicFunction | None:
    """
    Return an already created :class:`SymbolicFunction` given the serial.

    These are stored in the dictionary ``sfunction_serial_dict``.

    EXAMPLES::

        sage: from sage.symbolic.expression import get_sfunction_from_serial
        sage: get_sfunction_from_serial(65) #random
        f
    """
def get_sfunction_from_hash(myhash: SupportsInt) -> SymbolicFunction | None:
    """
    Return an already created :class:`SymbolicFunction` given the hash.

    EXAMPLES::

        sage: from sage.symbolic.expression import get_sfunction_from_hash
        sage: get_sfunction_from_hash(1)  # random
    """

class SymbolicSeries[P: SymbolicRingABC](Expression[P]):
    def __init__(self, SR: P):
        """
                Trivial constructor.

                EXAMPLES::

                    sage: loads(dumps((x+x^3).series(x,2)))
                    1*x + Order(x^2)
        """
    type _ZZZero = Annotated[Integer, Integer(0)]
    @overload
    def coefficients( # pyright: ignore[reportOverlappingOverload]
        self, x: CoercibleToExpression | None = None, sparse: Literal[False] = ...
    ) -> list[Expression[P] | _ZZZero]: ...
    @overload
    def coefficients( # pyright: ignore[reportIncompatibleMethodOverride]
        self, x: CoercibleToExpression | None = None, sparse: Literal[True] = True
    ) -> list[tuple[Expression[P], Expression[P]]]:
        """
        Return the coefficients of this symbolic series as a list of pairs.

        INPUT:

        - ``x`` -- (optional) variable

        - ``sparse`` -- boolean (default: ``True``); if ``False`` return a list
          with as much entries as the order of the series

        OUTPUT: depending on the value of ``sparse``,

        - A list of pairs ``(expr, n)``, where ``expr`` is a symbolic
          expression and ``n`` is a power (``sparse=True``, default)

        - A list of expressions where the ``n``-th element is the coefficient of
          ``x^n`` when ``self`` is seen as polynomial in ``x`` (``sparse=False``).

        EXAMPLES::

            sage: s = (1/(1-x)).series(x,6); s
            1 + 1*x + 1*x^2 + 1*x^3 + 1*x^4 + 1*x^5 + Order(x^6)
            sage: s.coefficients()
            [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
            sage: s.coefficients(x, sparse=False)
            [1, 1, 1, 1, 1, 1]
            sage: x,y = var("x,y")
            sage: s = (1/(1-y*x-x)).series(x,3); s
            1 + (y + 1)*x + ((y + 1)^2)*x^2 + Order(x^3)
            sage: s.coefficients(x, sparse=False)
            [1, y + 1, (y + 1)^2]"""
    def default_variable(self) -> Expression[P]:
        """
        Return the expansion variable of this symbolic series.

        EXAMPLES::

            sage: s = (1/(1-x)).series(x,3); s
            1 + 1*x + 1*x^2 + Order(x^3)
            sage: s.default_variable()
            x"""
    def is_terminating_series(self) -> bool:
        """
        Return ``True`` if the series is without order term.

        A series is terminating if it can be represented exactly,
        without requiring an order term. You can explicitly
        request terminating series by setting the order to
        positive infinity.

        OUTPUT: boolean; ``True`` if the series has no order term

        EXAMPLES::

            sage: (x^5+x^2+1).series(x, +oo)
            1 + 1*x^2 + 1*x^5
            sage: (x^5+x^2+1).series(x,+oo).is_terminating_series()
            True
            sage: SR(5).is_terminating_series()
            False
            sage: exp(x).series(x,10).is_terminating_series()
            False"""
    def power_series(self, base_ring: Ring) -> PowerSeries_poly:
        """
        Return the algebraic power series associated to this symbolic series.

        The coefficients must be coercible to the base ring.

        EXAMPLES::

            sage: ex = (gamma(1-x)).series(x,3); ex
            1 + euler_gamma*x + (1/2*euler_gamma^2 + 1/12*pi^2)*x^2 + Order(x^3)
            sage: g = ex.power_series(SR); g
            1 + euler_gamma*x + (1/2*euler_gamma^2 + 1/12*pi^2)*x^2 + O(x^3)
            sage: g.parent()
            Power Series Ring in x over Symbolic Ring"""
    def truncate(self) -> Expression[P]:
        """
        Given a power series or expression, return the corresponding
        expression without the big oh.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: f = sin(x)/x^2
            sage: f.truncate()
            sin(x)/x^2
            sage: f.series(x,7)
            1*x^(-1) + (-1/6)*x + 1/120*x^3 + (-1/5040)*x^5 + Order(x^7)
            sage: f.series(x,7).truncate()
            -1/5040*x^5 + 1/120*x^3 - 1/6*x + 1/x
            sage: f.series(x==1,3).truncate().expand()
            -2*x^2*cos(1) + 5/2*x^2*sin(1) + 5*x*cos(1) - 7*x*sin(1) - 3*cos(1) + 11/2*sin(1)"""

class SubstitutionMap(SageObject):
    type _unsigned = SupportsInt
    def apply_to[P: SymbolicRingABC](
        self, expr: Expression[P], options: _unsigned) -> Expression[P]:
        """
        Apply the substitution to a symbolic expression.

        EXAMPLES::

            sage: from sage.symbolic.expression import make_map
            sage: subs = make_map({x:x+1})
            sage: subs.apply_to(x^2, 0)
            (x + 1)^2"""

def make_map(subs_dict: dict) -> SubstitutionMap:
    """
    Construct a new substitution map.

    OUTPUT: a new :class:`SubstitutionMap` for doctesting

    EXAMPLES::

        sage: from sage.symbolic.expression import make_map
        sage: make_map({x:x+1})
        SubsMap
    """
