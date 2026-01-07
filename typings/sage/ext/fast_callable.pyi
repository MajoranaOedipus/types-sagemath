r"""
Fast Expression Evaluation

For many applications such as numerical integration, differential
equation approximation, plotting a 3d surface, optimization problems,
Monte-Carlo simulations, etc., one wishes to pass around and evaluate
a single algebraic expression many, many times at various floating
point values.  Other applications may need to evaluate an expression
many times in interval arithmetic, or in a finite field.  Doing this
via recursive calls over a python representation of the object (even
if Maxima or other outside packages are not involved) is extremely
inefficient.

This module provides a function, :func:`fast_callable`, to
transform such expressions into a form where they can be evaluated
quickly::

    sage: # needs sage.symbolic
    sage: f = sin(x) + 3*x^2
    sage: ff = fast_callable(f, vars=[x])
    sage: ff(3.5)
    36.3992167723104
    sage: ff(RIF(3.5))
    36.39921677231038?

By default, :func:`fast_callable` only removes some interpretive
overhead from the evaluation, but all of the individual arithmetic
operations are done using standard Sage arithmetic.  This is still a
huge win over :mod:`sage.calculus`, which evidently has a lot of overhead.
Compare the cost of evaluating Wilkinson's polynomial (in unexpanded
form) at `x = 30`::

    sage: # needs sage.symbolic
    sage: wilk = prod((x-i) for i in [1 .. 20]); wilk
    (x - 1)*(x - 2)*(x - 3)*(x - 4)*(x - 5)*(x - 6)*(x - 7)*(x - 8)*(x - 9)*(x - 10)*(x - 11)*(x - 12)*(x - 13)*(x - 14)*(x - 15)*(x - 16)*(x - 17)*(x - 18)*(x - 19)*(x - 20)
    sage: timeit('wilk.subs(x=30)')         # random    # long time
    625 loops, best of 3: 1.43 ms per loop
    sage: fc_wilk = fast_callable(wilk, vars=[x])
    sage: timeit('fc_wilk(30)')             # random    # long time
    625 loops, best of 3: 9.72 us per loop

You can specify a particular domain for the evaluation using
``domain=``::

    sage: fc_wilk_zz = fast_callable(wilk, vars=[x], domain=ZZ)                         # needs sage.symbolic

The meaning of ``domain=D`` is that each intermediate and final result
is converted to type ``D``.  For instance, the previous example of
``sin(x) + 3*x^2`` with ``domain=D`` would be equivalent to
``D(D(sin(D(x))) + D(D(3)*D(D(x)^2)))``.  (This example also
demonstrates the one exception to the general rule: if an exponent is an
integral constant, then it is not wrapped with ``D()``.)

At first glance, this seems like a very bad idea if you want to
compute quickly.  And it is a bad idea, for types where we don't
have a special interpreter.  It's not too bad of a slowdown, though.
To mitigate the costs, we check whether the value already has
the correct parent before we call ``D``.

We don't yet have a special interpreter with domain ``ZZ``, so we can see
how that compares to the generic ``fc_wilk`` example above::

    sage: timeit('fc_wilk_zz(30)')          # random    # long time                     # needs sage.symbolic
    625 loops, best of 3: 15.4 us per loop

However, for other types, using ``domain=D`` will get a large speedup,
because we have special-purpose interpreters for those types.  One
example is ``RDF``.  Since with ``domain=RDF`` we know that every single
operation will be floating-point, we can just execute the
floating-point operations directly and skip all the Python object
creations that you would get from actually using ``RDF`` objects::

    sage: fc_wilk_rdf = fast_callable(wilk, vars=[x], domain=RDF)                       # needs sage.symbolic
    sage: timeit('fc_wilk_rdf(30.0)')       # random    # long time                     # needs sage.symbolic
    625 loops, best of 3: 7 us per loop

The domain does not need to be a Sage type; for instance, ``domain=float``
also works.  (We actually use the same fast interpreter for ``domain=float``
and ``domain=RDF``; the only difference is that when ``domain=RDF`` is used,
the return value is an ``RDF`` element, and when ``domain=float`` is used,
the return value is a Python :class:`float`.) ::

    sage: fc_wilk_float = fast_callable(wilk, vars=[x], domain=float)                   # needs sage.symbolic
    sage: timeit('fc_wilk_float(30.0)')     # random    # long time                     # needs sage.symbolic
    625 loops, best of 3: 5.04 us per loop

We also have support for ``RR``::

    sage: fc_wilk_rr = fast_callable(wilk, vars=[x], domain=RR)                         # needs sage.symbolic
    sage: timeit('fc_wilk_rr(30.0)')        # random    # long time                     # needs sage.symbolic
    625 loops, best of 3: 13 us per loop

For ``CC``::

    sage: fc_wilk_cc = fast_callable(wilk, vars=[x], domain=CC)                         # needs sage.symbolic
    sage: timeit('fc_wilk_cc(30.0)')        # random    # long time                     # needs sage.symbolic
    625 loops, best of 3: 23 us per loop

And support for ``CDF``::

    sage: fc_wilk_cdf = fast_callable(wilk, vars=[x], domain=CDF)                       # needs sage.symbolic
    sage: timeit('fc_wilk_cdf(30.0)')       # random    # long time                     # needs sage.symbolic
    625 loops, best of 3: 10.2 us per loop

Currently, :func:`fast_callable` can accept two kinds of objects:
polynomials (univariate and multivariate) and symbolic expressions
(elements of the Symbolic Ring).  For polynomials, you can omit the
``vars`` argument; the variables will default to the ring generators (in
the order used when creating the ring). ::

    sage: K.<x,y,z> = QQ[]
    sage: p = 10*y + 100*z + x
    sage: fp = fast_callable(p)
    sage: fp(1,2,3)
    321

But you can also specify the variable names to override the default
ordering (you can include extra variable names here, too). ::

    sage: fp = fast_callable(p, vars=('x','w','z','y'))

For symbolic expressions, you need to specify the variable names, so
that :func:`fast_callable` knows what order to use. ::

    sage: # needs sage.symbolic
    sage: var('y,z,x')
    (y, z, x)
    sage: f = 10*y + 100*z + x
    sage: ff = fast_callable(f, vars=(x,y,z))
    sage: ff(1,2,3)
    321

You can also specify extra variable names::

    sage: ff = fast_callable(f, vars=('x','w','z','y'))                                 # needs sage.symbolic
    sage: ff(1,2,3,4)                                                                   # needs sage.symbolic
    341

This should be enough for normal use of :func:`fast_callable`; let's
discuss some more advanced topics.

Sometimes it may be useful to create a fast version of an expression
without going through symbolic expressions or polynomials; perhaps
because you want to describe to :func:`fast_callable` an expression
with common subexpressions.

Internally, :func:`fast_callable` works in two stages: it constructs
an expression tree from its argument, and then it builds a
fast evaluator from that expression tree.  You can bypass the first phase
by building your own expression tree and passing that directly to
:func:`fast_callable`, using an :class:`ExpressionTreeBuilder`. ::

    sage: from sage.ext.fast_callable import ExpressionTreeBuilder
    sage: etb = ExpressionTreeBuilder(vars=('x','y','z'))

An :class:`ExpressionTreeBuilder` has three interesting methods:
:meth:`constant`, :meth:`var`, and :meth:`call`.
All of these methods return :class:`ExpressionTree` objects.

The :meth:`var` method takes a string, and returns an expression tree
for the corresponding variable. ::

    sage: x = etb.var('x')
    sage: y = etb.var('y')
    sage: z = etb.var('y')

Expression trees support Python's numeric operators, so you can easily
build expression trees representing arithmetic expressions. ::

    sage: v1 = (x+y)*(y+z) + (y//z)

The :meth:`constant` method takes a Sage value, and returns an
expression tree representing that value. ::

    sage: v2 = etb.constant(3.14159) * x + etb.constant(1729) * y

The :meth:`call` method takes a sage/Python function and zero or more
expression trees, and returns an expression tree representing
the function call. ::

    sage: v3 = etb.call(sin, v1+v2)
    sage: v3                                                                            # needs sage.symbolic
    sin(add(add(mul(add(v_0, v_1), add(v_1, v_1)), floordiv(v_1, v_1)),
            add(mul(3.14159000000000, v_0), mul(1729, v_1))))

Many sage/Python built-in functions are specially handled; for instance,
when evaluating an expression involving :func:`sin` over ``RDF``,
the C math library function :func:`sin` is called.  Arbitrary functions
are allowed, but will be much slower since they will call back to
Python code on every call; for example, the following will work. ::

    sage: def my_sqrt(x): return pow(x, 0.5)
    sage: e = etb.call(my_sqrt, v1); e
    {my_sqrt}(add(mul(add(v_0, v_1), add(v_1, v_1)), floordiv(v_1, v_1)))
    sage: fast_callable(e)(1, 2, 3)
    3.60555127546399

To provide :func:`fast_callable` for your own class (so that
``fast_callable(x)`` works when ``x`` is an instance of your
class), implement a method ``_fast_callable_(self, etb)`` for your class.
This method takes an :class:`ExpressionTreeBuilder`, and returns an
expression tree built up using the methods described above.

EXAMPLES::

    sage: var('x')                                                                      # needs sage.symbolic
    x
    sage: f = fast_callable(sqrt(x^7+1), vars=[x], domain=float)                        # needs sage.symbolic

::

    sage: f(1)                                                                          # needs sage.symbolic
    1.4142135623730951
    sage: f.op_list()                                                                   # needs sage.symbolic
    [('load_arg', 0), ('ipow', 7), ('load_const', 1.0), 'add', 'sqrt', 'return']

To interpret that last line, we load argument 0 (``x`` in this case) onto
the stack, push the constant `7.0` onto the stack, call the :func:`pow`
functionn(which takes 2 arguments from the stack), push the constant `1.0`,
add the top two arguments of the stack, and then call :func:`sqrt`.

Here we take :func:`sin` of the first argument and add it to ``f``::

    sage: from sage.ext.fast_callable import ExpressionTreeBuilder
    sage: etb = ExpressionTreeBuilder('x')
    sage: x = etb.var('x')
    sage: f = etb.call(sqrt, x^7 + 1)
    sage: g = etb.call(sin, x)
    sage: fast_callable(f+g).op_list()
    [('load_arg', 0), ('ipow', 7), ('load_const', 1), 'add',
     ('py_call', <function sqrt at ...>, 1), ('load_arg', 0), ('py_call', sin, 1),
     'add', 'return']


AUTHOR:

- Carl Witty (2009-02): initial version (heavily inspired by
  Robert Bradshaw's fast_eval.pyx)

.. TODO::

    The following bits of text were written for the module docstring.
    They are not true yet, but I hope they will be true someday, at
    which point I will move them into the main text.

    The final interesting method of :class:`ExpressionTreeBuilder` is
    :meth:`choice`.  This produces conditional expressions, like the C
    ``COND ? T : F`` expression or the Python ``T if COND else F``.
    This lets you define piecewise functions using :func:`fast_callable`. ::

        sage: v4 = etb.choice(v3 >= etb.constant(0), v1, v2)  # not tested

    The arguments are ``(COND, T, F)`` (the same order as in C), so the
    above means that if ``v3`` evaluates to a nonnegative number,
    then ``v4`` will evaluate to the result of ``v1``;
    otherwise, ``v4`` will evaluate to the result of ``v2``.

    Let's see an example where we see that :func:`fast_callable` does not
    evaluate common subexpressions more than once.  We'll make a
    :func:`fast_callable` expression that gives the result
    of 16 iterations of the Mandelbrot function. ::

        sage: etb = ExpressionTreeBuilder('c')
        sage: z = etb.constant(0)
        sage: c = etb.var('c')
        sage: for i in range(16):
        ....:     z = z*z + c
        sage: mand = fast_callable(z, domain=CDF)                                       # needs sage.rings.complex_double

    Now ``ff`` does 32 complex arithmetic operations on each call
    (16 additions and 16 multiplications).  However, if ``z*z`` produced
    code that evaluated ``z`` twice, then this would do many
    thousands of arithmetic operations instead.

    Note that the handling for common subexpressions only checks whether
    expression trees are the same Python object; for instance, the following
    code will evaluate ``x+1`` twice::

        sage: etb = ExpressionTreeBuilder('x')
        sage: x = etb.var('x')
        sage: (x+1)*(x+1)
        mul(add(v_0, 1), add(v_0, 1))

    but this code will only evaluate ``x+1`` once::

        sage: v = x+1; v*v
        mul(add(v_0, 1), add(v_0, 1))
"""

from typing import Any, Literal, Self, overload, Protocol, TypedDict
from typings_sagemath import Int, SupportsPowWithExponent, SupportsRPowWithBase, Num
from collections.abc import Callable, Sequence
from sage.symbolic.expression import Expression as SRElement
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base
from sage.structure.element import Element, FieldElement, RingElement
from sage.rings.abc import RealField, ComplexField, RealDoubleField, ComplexDoubleField
from sage.ext.interpreters.wrapper_cdf import Wrapper_cdf
from sage.ext.interpreters.wrapper_rdf import Wrapper_rdf
from sage.ext.interpreters.wrapper_rr import Wrapper_rr
from sage.ext.interpreters.wrapper_cc import Wrapper_cc
from sage.ext.interpreters.wrapper_py import Wrapper_py
from sage.ext.interpreters.wrapper_el import Wrapper_el

import sage as sage
from sage.categories.category import ZZ as ZZ
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

from typings_sagemath.numbers import Real

type _X = Expression | SRElement | Element[PolynomialRing_generic] | Element[MPolynomialRing_base]
type _NotUsed = Any
class _MonadOperator(Protocol):
    def __call__(self): ...
class _BinOperator(Protocol):
    def __call__(self, other, /): ...

type Pair[X] = tuple[X, X] | Sequence[X]

@overload
def fast_callable[_Domain: RealField](
    x: _X, 
    domain: _Domain, 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var: bool = False
) -> Wrapper_rr[RingElement[_Domain]]: ...
@overload
def fast_callable(
    x: _X, 
    domain: type[float], 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var: bool = False
) -> Wrapper_rdf[float]: ...
@overload
def fast_callable[_Domain: RealDoubleField](
    x: _X, 
    domain: _Domain, 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var: bool = False
) -> Wrapper_rdf[FieldElement[_Domain]]: ...
@overload
def fast_callable(
    x: _X, 
    domain: ComplexDoubleField, 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var: bool = False
) -> Wrapper_cdf: ...
@overload
def fast_callable(
    x: _X, 
    domain: ComplexField, 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var: bool = False
) -> Wrapper_cc: ...
@overload
def fast_callable(
    x: _X, 
    domain: None = None, 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var= False
) -> Wrapper_py: ...
@overload
def fast_callable[_DomainElement](
    x: _X, 
    domain: Callable[[Any], _DomainElement], 
    var: Sequence[str |  SRElement] | None = None,
    expect_one_var: bool = False
) -> Wrapper_el[_DomainElement]:
    r"""
    Given an expression ``x``, compile it into a form that can be quickly
    evaluated, given values for the variables in ``x``.

    Currently, ``x`` can be an expression object, an element of ``SR``, or a
    (univariate or multivariate) polynomial; this list will probably
    be extended soon.

    By default, ``x`` is evaluated the same way that a Python function
    would evaluate it -- addition maps to ``PyNumber_Add``, etc.  However,
    you can specify ``domain=D`` where ``D`` is some Sage parent or Python
    type; in this case, all arithmetic is done in that domain.  If we
    have a special-purpose interpreter for that parent (like ``RDF`` or
    :class:`float`), ``domain=...`` will trigger the use of that interpreter.

    If ``vars`` is ``None`` and ``x`` is a polynomial, then we will use the
    generators of ``parent(x)`` as the variables; otherwise, ``vars`` must be
    specified (unless ``x`` is a symbolic expression with only one variable,
    and ``expect_one_var`` is ``True``, in which case we will use that variable).

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: var('x')
        x
        sage: expr = sin(x) + 3*x^2
        sage: f = fast_callable(expr, vars=[x])
        sage: f(2)
        sin(2) + 12
        sage: f(2.0)
        12.9092974268257

    We have special fast interpreters for ``domain=float`` and ``domain=RDF``.
    (Actually it's the same interpreter; only the return type varies.)
    Note that the float interpreter is not actually more accurate than
    the ``RDF`` interpreter; elements of ``RDF`` just don't display all
    their digits. We have special fast interpreter for ``domain=CDF``::

        sage: # needs sage.symbolic
        sage: f_float = fast_callable(expr, vars=[x], domain=float)
        sage: f_float(2)
        12.909297426825681
        sage: f_rdf = fast_callable(expr, vars=[x], domain=RDF)
        sage: f_rdf(2)
        12.909297426825681
        sage: f_cdf = fast_callable(expr, vars=[x], domain=CDF)
        sage: f_cdf(2)
        12.909297426825681
        sage: f_cdf(2+I)
        10.40311925062204 + 11.510943740958707*I
        sage: f = fast_callable(expr, vars=('z','x','y'))
        sage: f(1, 2, 3)
        sin(2) + 12

        sage: K.<x> = QQ[]
        sage: p = -1/4*x^6 + 1/2*x^5 - x^4 - 12*x^3 + 1/2*x^2 - 1/95*x - 1/2
        sage: fp = fast_callable(p, domain=RDF)
        sage: fp.op_list()
        [('load_arg', 0), ('load_const', -0.25), 'mul', ('load_const', 0.5), 'add',
         ('load_arg', 0), 'mul', ('load_const', -1.0), 'add', ('load_arg', 0), 'mul',
         ('load_const', -12.0), 'add', ('load_arg', 0), 'mul', ('load_const', 0.5),
         'add', ('load_arg', 0), 'mul', ('load_const', -0.010526315789473684),
         'add', ('load_arg', 0), 'mul', ('load_const', -0.5), 'add', 'return']
        sage: fp(3.14159)
        -552.4182988917153

        sage: K.<x,y,z> = QQ[]
        sage: p = x*y^2 + 1/3*y^2 - x*z - y*z
        sage: fp = fast_callable(p, domain=RDF)
        sage: fp.op_list()
        [('load_const', 0.0), ('load_const', 1.0), ('load_arg', 0), ('ipow', 1),
         ('load_arg', 1), ('ipow', 2), 'mul', 'mul', 'add',
         ('load_const', 0.3333333333333333), ('load_arg', 1), ('ipow', 2), 'mul', 'add',
         ('load_const', -1.0), ('load_arg', 0), ('ipow', 1), ('load_arg', 2),
         ('ipow', 1), 'mul', 'mul', 'add', ('load_const', -1.0), ('load_arg', 1),
         ('ipow', 1), ('load_arg', 2), ('ipow', 1), 'mul', 'mul', 'add', 'return']
        sage: fp(e, pi, sqrt(2))   # abs tol 3e-14                                      # needs sage.symbolic
        21.831120464939584
        sage: symbolic_result = p(e, pi, sqrt(2)); symbolic_result                      # needs sage.symbolic
        pi^2*e + 1/3*pi^2 - sqrt(2)*pi - sqrt(2)*e
        sage: n(symbolic_result)                                                        # needs sage.symbolic
        21.8311204649396

    ::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=('x','y'), domain=float)
        sage: x = etb.var('x')
        sage: y = etb.var('y')
        sage: expr = etb.call(sin, x^2 + y); expr
        sin(add(ipow(v_0, 2), v_1))
        sage: fc = fast_callable(expr, domain=float)
        sage: fc(5, 7)
        0.5514266812416906

    Check that :func:`fast_callable` also works for symbolic functions with
    evaluation functions::

        sage: # needs sage.symbolic
        sage: def evalf_func(self, x, y, parent):
        ....:     return parent(x*y) if parent is not None else x*y
        sage: x,y = var('x,y')
        sage: f = function('f', evalf_func=evalf_func)
        sage: fc = fast_callable(f(x, y), vars=[x, y])
        sage: fc(3, 4)
        f(3, 4)

    And also when there are complex values involved::

        sage: # needs sage.symbolic
        sage: def evalf_func(self, x, y, parent):
        ....:     return parent(I*x*y) if parent is not None else I*x*y
        sage: g = function('g', evalf_func=evalf_func)
        sage: fc = fast_callable(g(x, y), vars=[x, y])
        sage: fc(3, 4)
        g(3, 4)
        sage: fc2 = fast_callable(g(x, y), domain=complex, vars=[x, y])
        sage: fc2(3, 4)
        12j
        sage: fc3 = fast_callable(g(x, y), domain=float, vars=[x, y])
        sage: fc3(3, 4)
        Traceback (most recent call last):
            ...
        TypeError: unable to simplify to float approximation
    """
def function_name(fn) -> str:
    r"""
    Given a function, return a string giving a name for the function.

    For functions we recognize, we use our standard opcode name for the
    function (so :func:`operator.add` becomes ``'add'``, and
    :func:`sage.functions.trig.sin` becomes ``'sin'``).

    For functions we don't recognize, we try to come up with a name,
    but the name will be wrapped in braces; this is a signal that
    we'll definitely use a slow Python call to call this function.
    (We may use a slow Python call even for functions we do recognize,
    if we're targeting an interpreter without an opcode for the function.)

    Only used when printing Expressions.

    EXAMPLES::

        sage: from sage.ext.fast_callable import function_name
        sage: function_name(operator.pow)
        'pow'
        sage: function_name(cos)                                                        # needs sage.symbolic
        'cos'
        sage: function_name(factorial)
        '{factorial}'
    """
def generate_code(expr: Expression, stream: InstructionStream) -> None:
    r"""
    Generate code from an :class:`Expression` tree; write the result into an
    :class:`InstructionStream`.

    In :func:`fast_callable`, first we create an :class:`Expression`, either directly
    with an :class:`ExpressionTreeBuilder` or with :meth:`_fast_callable_` methods.
    Then we optimize the :class:`Expression` in tree form.  (Unfortunately,
    this step is currently missing -- we do no optimizations.)

    Then we linearize the :class:`Expression` into a sequence of instructions,
    by walking the :class:`Expression` and sending the corresponding stack
    instructions to an :class:`InstructionStream`.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder, generate_code, InstructionStream

        sage: # needs sage.symbolic
        sage: etb = ExpressionTreeBuilder('x')
        sage: x = etb.var('x')
        sage: expr = (x+pi) * (x+1)
        sage: from sage.ext.interpreters.wrapper_py import metadata, Wrapper_py
        sage: instr_stream = InstructionStream(metadata, 1)
        sage: generate_code(expr, instr_stream)
        sage: instr_stream.instr('return')
        sage: v = Wrapper_py(instr_stream.get_current())
        sage: type(v)
        <class '...interpreters.wrapper_py.Wrapper_py'>
        sage: v(7)
        8*pi + 56

    TESTS::

        sage: def my_sin(x): return sin(x)
        sage: def my_norm(x, y): return x*x + y*y
        sage: def my_sqrt(x):
        ....:     if x < 0: raise ValueError("sqrt of negative number")
        ....:     return sqrt(x, extend=False)

        sage: # needs sage.symbolic
        sage: fc = fast_callable(expr, domain=RealField(130))
        sage: fc(0)
        3.1415926535897932384626433832795028842
        sage: fc(1)
        8.2831853071795864769252867665590057684
        sage: fc = fast_callable(expr, domain=RDF)
        sage: fc(0)
        3.141592653589793
        sage: fc(1)
        8.283185307179586
        sage: fc.op_list()
        [('load_arg', 0), ('load_const', pi), 'add', ('load_arg', 0), ('load_const', 1), 'add', 'mul', 'return']
        sage: fc = fast_callable(etb.call(sin, x) + etb.call(sqrt, x), domain=RDF)
        sage: fc(1)
        1.8414709848078965
        sage: fc.op_list()
        [('load_arg', 0), 'sin', ('load_arg', 0), 'sqrt', 'add', 'return']
        sage: fc = fast_callable(etb.call(sin, x) + etb.call(sqrt, x))
        sage: fc(1)
        sin(1) + 1
        sage: fc.op_list()
        [('load_arg', 0), ('py_call', sin, 1), ('load_arg', 0), ('py_call', <function sqrt at ...>, 1), 'add', 'return']
        sage: fc = fast_callable(etb.call(my_sin, x), domain=RDF)
        sage: fc(3)
        0.1411200080598672

        sage: # needs sage.rings.real_mpfr sage.symbolic
        sage: fc = fast_callable(etb.call(my_sin, x), domain=RealField(100))
        sage: fc(3)
        0.14112000805986722210074480281
        sage: fc.op_list()
        [('load_arg', 0), ('py_call', <function my_sin at 0x...>, 1), 'return']

        sage: # needs sage.symbolic
        sage: fc = fast_callable(etb.call(my_sqrt, x), domain=RDF)
        sage: fc(3)
        1.7320508075688772
        sage: parent(fc(3))
        Real Double Field
        sage: fc(-3)
        Traceback (most recent call last):
        ...
        ValueError: sqrt of negative number
        sage: fc = fast_callable(etb.call(my_sqrt, x), domain=RR)
        sage: fc(3)
        1.73205080756888
        sage: fc(-3)
        Traceback (most recent call last):
        ...
        ValueError: sqrt of negative number

        sage: etb2 = ExpressionTreeBuilder(('y','z'))
        sage: y = etb2.var('y')
        sage: z = etb2.var('z')
        sage: fc = fast_callable(etb2.call(sqrt, etb2.call(my_norm, y, z)), domain=RDF)
        sage: fc(3, 4)
        5.0
        sage: fc.op_list()
        [('load_arg', 0), ('load_arg', 1), ('py_call', <function my_norm at 0x...>, 2), 'sqrt', 'return']
        sage: fc.python_calls()
        [<function my_norm at 0x...>]
        sage: fc = fast_callable(etb2.call(sqrt, etb2.call(my_norm, y, z)), domain=RR)  # needs sage.rings.real_mpfr
        sage: fc(3, 4)                                                                  # needs sage.rings.real_mpfr
        5.00000000000000
        sage: fc = fast_callable(etb2.call(my_norm, y, z), domain=ZZ)
        sage: fc(3, 4)
        25
        sage: fc.op_list()
        [('load_arg', 0), ('load_arg', 1), ('py_call', <function my_norm at 0x...>, 2), 'return']

        sage: # needs sage.symbolic
        sage: fc = fast_callable(expr)
        sage: fc(3.0r)
        4.0*pi + 12.0
        sage: fc = fast_callable(x+3, domain=ZZ)
        sage: fc(4)
        7
        sage: fc = fast_callable(x/3, domain=ZZ)
        sage: fc(4)
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer
        sage: fc(6)
        2
        sage: fc = fast_callable(etb.call(sin, x), domain=ZZ)
        sage: fc(0)
        0
        sage: fc(3)
        Traceback (most recent call last):
        ...
        TypeError: unable to convert sin(3) to an integer

    ::

        sage: # needs sage.symbolic
        sage: fc = fast_callable(etb(x)^100)
        sage: fc(pi)
        pi^100
        sage: fc = fast_callable(etb(x)^100, domain=ZZ)
        sage: fc(2)
        1267650600228229401496703205376
        sage: fc = fast_callable(etb(x)^100, domain=RIF)
        sage: fc(RIF(-2))
        1.2676506002282295?e30
        sage: fc = fast_callable(etb(x)^100, domain=RDF)
        sage: fc.op_list()
        [('load_arg', 0), ('ipow', 100), 'return']
        sage: fc(1.1)
        13780.61233982...
        sage: fc = fast_callable(etb(x)^100, domain=RR)                                 # needs sage.rings.real_mpfr
        sage: fc.op_list()                                                              # needs sage.rings.real_mpfr
        [('load_arg', 0), ('ipow', 100), 'return']
        sage: fc(1.1)                                                                   # needs sage.rings.real_mpfr
        13780.6123398224
        sage: fc = fast_callable(etb(x)^(-100), domain=RDF)
        sage: fc.op_list()
        [('load_arg', 0), ('ipow', -100), 'return']
        sage: fc(1.1)
        7.25657159014...e-05
        sage: fc = fast_callable(etb(x)^(-100), domain=RR)                              # needs sage.rings.real_mpfr
        sage: fc(1.1)                                                                   # needs sage.rings.real_mpfr
        0.0000725657159014814
        sage: expo = 2^32
        sage: base = (1.0).nextabove()
        sage: fc = fast_callable(etb(x)^expo, domain=RDF)
        sage: fc.op_list()
        [('load_arg', 0), ('py_call', (^4294967296), 1), 'return']
        sage: fc(base)        # rel tol 1e-15
        1.0000009536747712
        sage: RDF(base)^expo
        1.0000009536747712
        sage: fc = fast_callable(etb(x)^expo, domain=RR)                                # needs sage.rings.real_mpfr
        sage: fc.op_list()                                                              # needs sage.rings.real_mpfr
        [('load_arg', 0), ('py_call', (^4294967296), 1), 'return']
        sage: fc(base)                                                                  # needs sage.rings.real_mpfr
        1.00000095367477
        sage: base^expo
        1.00000095367477

    Make sure we do not overflow the stack with highly nested expressions
    (:issue:`11766`)::

        sage: # needs sage.rings.real_mpfr
        sage: R.<x> = CC[]
        sage: f = R(list(range(100000)))
        sage: ff = fast_callable(f)
        sage: f(0.5)
        2.00000000000000
        sage: ff(0.5)
        2.00000000000000
        sage: f(0.9), ff(0.9)
        (90.0000000000000, 90.0000000000000)
    """
def get_builtin_functions() -> dict[Callable, str]:
    r"""
    Return a dictionary from Sage and Python functions to opcode names.

    The result is cached.

    The dictionary is used in :class:`ExpressionCall`.

    EXAMPLES::

        sage: from sage.ext.fast_callable import get_builtin_functions
        sage: builtins = get_builtin_functions()
        sage: sorted(set(builtins.values()))                                            # needs sage.symbolic
        ['abs', 'acos', 'acosh', 'add', 'asin', 'asinh', 'atan', 'atanh', 'ceil',
         'cos', 'cosh', 'cot', 'csc', 'div', 'exp', 'floor', 'floordiv', 'inv', 'log',
         'mul', 'neg', 'pow', 'sec', 'sin', 'sinh', 'sqrt', 'sub', 'tan', 'tanh']
        sage: builtins[sin]                                                             # needs sage.symbolic
        'sin'
        sage: builtins[ln]
        'log'
    """
nan: float

class ExpressionTreeBuilder[_Domain]:
    """
    A class with helper methods for building Expressions.

    An instance of this class is passed to :meth:`_fast_callable_` methods;
    you can also instantiate it yourself to create your own expressions
    for :func:`fast_callable`, bypassing :meth:`_fast_callable_`.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder('x')
        sage: x = etb.var('x')
        sage: (x+3)*5
        mul(add(v_0, 3), 5)"""
    
    @overload
    def __init__(self: ExpressionTreeBuilder[None], vars: list[object] | tuple[object, ...] | str | object, domain: None = None): ...
    @overload
    def __init__(self, vars: list[object] | tuple[object, ...] | str | object, domain: Callable[[Any], _Domain]):
        """
                Initialize an instance of :class:`ExpressionTreeBuilder`.

                Takes a list or tuple of variable names to use, and also an optional
                ``domain``.  If a ``domain`` is given, then creating an
                :class:`ExpressionConstant` node with the :meth:`__call__`, make, or
                constant methods will convert the value into the given domain.

                Note that this is the only effect of the domain parameter.  It
                is quite possible to use different domains for
                :class:`ExpressionTreeBuilder` and for :func:`fast_callable`; in that case,
                constants will be converted twice (once when building the
                :class:`Expression`, and once when generating code).

                EXAMPLES::

                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder
                    sage: etb = ExpressionTreeBuilder('x')
                    sage: etb(3^50)
                    717897987691852588770249
                    sage: etb = ExpressionTreeBuilder('x', domain=RR)
                    sage: etb(3^50)
                    7.17897987691853e23
        """
    
    type _PowOperator = Callable[[Any, Any], Any]
    @overload
    def call[_B, _E: Int](self, fn: _PowOperator, base: _B, exponent: _E, /) -> ExpressionIPow[_B, _E]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def call[_Fn: _X | object](self, fn: _Fn, *args) -> ExpressionCall[_Fn, tuple[Expression, ...]]:
        """
        Construct a call node, given a function and a list of arguments.

        The arguments will be converted to Expressions using
        :meth:`ExpressionTreeBuilder.__call__`.

        As a special case, notice if the function is :func:`operator.pow` and
        the second argument is integral, and construct an :class:`ExpressionIPow`
        instead.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: etb.call(cos, x)
            cos(v_0)
            sage: etb.call(sin, 1)
            sin(1)
            sage: etb.call(sin, etb(1))
            sin(1)
            sage: etb.call(factorial, x+57)
            {factorial}(add(v_0, 57))
            sage: etb.call(operator.pow, x, 543)
            ipow(v_0, 543)"""
    def choice[_Cond](self, cond: _Cond, iftrue, iffalse) -> ExpressionChoice[_Cond, Expression, Expression]:
        """
        Construct a choice node (a conditional expression), given the
        condition, and the values for the true and false cases.

        (It's possible to create choice nodes, but they don't work yet.)

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.choice(etb.call(operator.eq, x, 0), 0, 1/x)                       # needs sage.symbolic
            (0 if {eq}(v_0, 0) else div(1, v_0))"""
    @overload
    def constant[_C](self: ExpressionTreeBuilder[None], c: _C) -> ExpressionConstant[_C]: ...
    @overload
    def constant(self, c: object) -> ExpressionConstant[_Domain]:
        """
        Turn the argument into an :class:`ExpressionConstant`, converting it to
        our domain if we have one.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder('x')
            sage: etb.constant(pi)                                                      # needs sage.symbolic
            pi
            sage: etb = ExpressionTreeBuilder('x', domain=RealField(200))               # needs sage.rings.real_mpfr
            sage: etb.constant(pi)                                                      # needs sage.rings.real_mpfr sage.symbolic
            3.1415926535897932384626433832795028841971693993751058209749"""
    def var(self, v: str | object) -> ExpressionVariable:
        """
        Turn the argument into an :class:`ExpressionVariable`.  Look it up in
        the list of variables.  (Variables are matched by name.)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: var('a,b,some_really_long_name')
            (a, b, some_really_long_name)
            sage: x = polygen(QQ)
            sage: etb = ExpressionTreeBuilder(vars=('a','b',some_really_long_name, x))
            sage: etb.var(some_really_long_name)
            v_2
            sage: etb.var('some_really_long_name')
            v_2
            sage: etb.var(x)
            v_3
            sage: etb.var('y')
            Traceback (most recent call last):
            ...
            ValueError: Variable 'y' not found..."""
    def __call__(self, x: _X | object) -> Expression:
        """
        Try to convert the given value to an :class:`Expression`.

        If it is already an Expression, just return it.  If it has a
        :meth:`_fast_callable_` method, then call the method with ``self`` as
        an argument.  Otherwise, use ``self.constant()`` to turn it into a constant.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder('x')
            sage: v = etb(3); v, type(v)
            (3, <class 'sage.ext.fast_callable.ExpressionConstant'>)
            sage: v = etb(polygen(QQ)); v, type(v)
            (v_0, <class 'sage.ext.fast_callable.ExpressionVariable'>)
            sage: v is etb(v)
            True"""

class Expression:
    """
    Represent an expression for :func:`fast_callable`.

    Supports the standard Python arithmetic operators; if arithmetic
    is attempted between an Expression and a non-Expression, the
    non-Expression is converted to an expression (using the
    :meth:`__call__` method of the Expression's :class:`ExpressionTreeBuilder`).

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))
        sage: x = etb.var(x)
        sage: etb(x)
        v_0
        sage: etb(3)
        3
        sage: etb.call(sin, x)
        sin(v_0)
        sage: (x+1)/(x-1)
        div(add(v_0, 1), sub(v_0, 1))
        sage: x//5
        floordiv(v_0, 5)
        sage: -abs(~x)
        neg(abs(inv(v_0)))"""
    def __init__(self, etb: ExpressionTreeBuilder):
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 893)

                Initialize an Expression.  Sets the _etb member.

                EXAMPLES::

                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder
                    sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
                    sage: v = etb(3); v  # indirect doctest                                     # needs sage.symbolic
                    3
                    sage: v._get_etb() is etb                                                   # needs sage.symbolic
                    True
        """
    def abs(self) -> ExpressionCall[_MonadOperator, tuple[Self]]:
        """
        Compute the absolute value of an Expression.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: abs(x)
            abs(v_0)
            sage: x.abs()
            abs(v_0)
            sage: x.__abs__()
            abs(v_0)"""
    def __abs__(self) -> ExpressionCall[_MonadOperator, tuple[Self]]:
        """Expression.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1099)

        Compute the absolute value of an Expression.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: abs(x)
            abs(v_0)
            sage: x.abs()
            abs(v_0)
            sage: x.__abs__()
            abs(v_0)"""
    def __add__(self, o) -> ExpressionCall[_BinOperator, tuple[Self]]:
        """
        Compute a sum of two Expressions.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: x+x
            add(v_0, v_0)
            sage: x+1
            add(v_0, 1)
            sage: 1+x
            add(1, v_0)
            sage: x.__add__(1)
            add(v_0, 1)
            sage: x.__radd__(1)
            add(1, v_0)"""
    def __floordiv__(self, o) -> ExpressionCall[_BinOperator, Pair[Expression]]:
        """
        Compute the floordiv (the floor of the quotient) of two Expressions.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: x//x
            floordiv(v_0, v_0)
            sage: x//1
            floordiv(v_0, 1)
            sage: 1//x
            floordiv(1, v_0)
            sage: x.__floordiv__(1)
            floordiv(v_0, 1)
            sage: x.__rfloordiv__(1)
            floordiv(1, v_0)"""
    def __invert__(self) -> ExpressionCall[_MonadOperator, tuple[Self]]:
        """
        Compute the inverse of an Expression.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: ~x
            inv(v_0)
            sage: x.__invert__()
            inv(v_0)"""
    def __mul__(self, o) -> ExpressionCall[_BinOperator, Pair[Expression]]:
        """
        Compute a product of two Expressions.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: x*x
            mul(v_0, v_0)
            sage: x*1
            mul(v_0, 1)
            sage: 1*x
            mul(1, v_0)
            sage: x.__mul__(1)
            mul(v_0, 1)
            sage: x.__rmul__(1)
            mul(1, v_0)"""
    def __neg__(self) -> ExpressionCall[_MonadOperator, tuple[Self]]:
        """
        Compute the negation of an Expression.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: -x
            neg(v_0)
            sage: x.__neg__()
            neg(v_0)"""
    @overload
    def __pow__[_E: Int](self, o: _E, dummy: _NotUsed) -> ExpressionIPow[Expression, _E]: ... # pyright: ignore[reportOverlappingOverload]
    @overload
    def __pow__(self, o, dummy: _NotUsed) -> ExpressionCall[_BinOperator, Pair[Expression]]:
        """
        Compute a power expression from two Expressions.

        If the second Expression is a constant integer, then return
        an :class:`ExpressionIPow` instead of an :class:`ExpressionCall`.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: x^x
            pow(v_0, v_0)
            sage: x^1
            ipow(v_0, 1)
            sage: x.__pow__(1)
            ipow(v_0, 1)
            sage: x.__pow__(1.0)
            pow(v_0, 1.00000000000000)
            sage: x.__rpow__(1)
            pow(1, v_0)"""
    def __radd__(self, other) -> ExpressionCall[_BinOperator, Pair[Expression]]: ...
    def __rfloordiv__(self, other) -> ExpressionCall[_BinOperator, Pair[Expression]]: ...
    def __rmul__(self, other) -> ExpressionCall[_BinOperator, Pair[Expression]]: ...
    def __rpow__(self, other) -> ExpressionCall[_BinOperator, Pair[Expression]]: ...
    def __rsub__(self, other) -> ExpressionCall[_BinOperator, Pair[Expression]]: ...
    def __rtruediv__(self, other) -> ExpressionCall[_BinOperator, Pair[Expression]]: ...
    def __sub__(self, o) -> ExpressionCall[_BinOperator, Pair[Expression]]:
        """
        Compute a difference of two Expressions.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: x-x
            sub(v_0, v_0)
            sage: x-1
            sub(v_0, 1)
            sage: 1-x
            sub(1, v_0)
            sage: x.__sub__(1)
            sub(v_0, 1)
            sage: x.__rsub__(1)
            sub(1, v_0)"""
    def __truediv__(self, o) -> ExpressionCall[_BinOperator, Pair[Expression]]:
        """Expression.__truediv__(s, o)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 992)

        Compute a quotient of two Expressions.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))
            sage: x = etb(x)
            sage: x/x
            div(v_0, v_0)
            sage: x/1
            div(v_0, 1)
            sage: 1/x
            div(1, v_0)
            sage: x.__truediv__(1)
            div(v_0, 1)
            sage: x.__rtruediv__(1)
            div(1, v_0)"""

class ExpressionCall[_Fn, _Args](Expression):
    """
    An Expression that represents a function call.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb.call(sin, x))                                                    # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionCall'>"""
    def __init__(self, etb: ExpressionTreeBuilder, fn: _Fn, args: _Args):
        """
                Initialize an :class:`ExpressionCall`.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder, ExpressionCall
                    sage: etb = ExpressionTreeBuilder(vars=(x,))
                    sage: x = etb(x)
                    sage: etb.call(factorial, x)
                    {factorial}(v_0)
                    sage: v = ExpressionCall(etb, factorial, [x]); v
                    {factorial}(v_0)
                    sage: v._get_etb() is etb
                    True
                    sage: v.function()
                    factorial
                    sage: v.arguments()
                    [v_0]
        """
    def arguments(self) -> _Args:
        """
        Return the arguments from this :class:`ExpressionCall`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.call(sin, x).arguments()                                          # needs sage.symbolic
            [v_0]"""
    def function(self) -> _Fn:
        """
        Return the function from this :class:`ExpressionCall`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.call(sin, x).function()                                           # needs sage.symbolic
            sin"""

class ExpressionChoice[_Cond, _IfTrue, _IfFalse](Expression):
    """
    A conditional expression.

    (It's possible to create choice nodes, but they don't work yet.)

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: etb.choice(etb.call(operator.eq, x, 0), 0, 1/x)                           # needs sage.symbolic
        (0 if {eq}(v_0, 0) else div(1, v_0))"""
    def __init__(self, etb: ExpressionTreeBuilder, cond: _Cond, iftrue: _IfTrue, iffalse: _IfFalse):
        """
                Initialize an :class:`ExpressionChoice`.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder, ExpressionChoice
                    sage: etb = ExpressionTreeBuilder(vars=(x,))
                    sage: x = etb(x)
                    sage: etb.choice(x, ~x, 0)
                    (inv(v_0) if v_0 else 0)
                    sage: v = ExpressionChoice(etb, x, ~x, etb(0)); v
                    (inv(v_0) if v_0 else 0)
                    sage: v._get_etb() is etb
                    True
                    sage: v.condition()
                    v_0
                    sage: v.if_true()
                    inv(v_0)
                    sage: v.if_false()
                    0
        """
    def condition(self) -> _Cond:
        """
        Return the condition of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).condition()                                      # needs sage.symbolic
            v_0"""
    def if_false(self) -> _IfFalse:
        """
        Return the false branch of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).if_false()                                       # needs sage.symbolic
            0"""
    def if_true(self) -> _IfTrue:
        """
        Return the true branch of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).if_true()                                        # needs sage.symbolic
            inv(v_0)"""

class ExpressionConstant[_V](Expression):
    """
    An Expression that represents an arbitrary constant.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb(3))                                                              # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionConstant'>"""
    def __init__(self, etb: ExpressionTreeBuilder, c: _V):
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1169)

                Initialize an :class:`ExpressionConstant`.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder, ExpressionConstant
                    sage: etb = ExpressionTreeBuilder(vars=(x,))
                    sage: etb(3)
                    3
                    sage: v = ExpressionConstant(etb, 3); v
                    3
                    sage: v._get_etb() is etb
                    True
                    sage: v.value()
                    3
                    sage: v.value() == 3
                    True
        """
    def value(self) -> _V:
        """
        Return the constant value of an :class:`ExpressionConstant`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb(3).value()                                                        # needs sage.symbolic
            3"""

class ExpressionIPow[_B, _E: Int](Expression):
    """
    A power Expression with an integer exponent.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb.var('x')^17)                                                     # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionIPow'>"""
    def __init__(self, etb: ExpressionTreeBuilder, base: _B, exponent: _E):
        """
                Initialize an ExpressionIPow.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder, ExpressionIPow
                    sage: etb = ExpressionTreeBuilder(vars=(x,))
                    sage: x = etb(x)
                    sage: x^(-12)
                    ipow(v_0, -12)
                    sage: v = ExpressionIPow(etb, x, 55); v
                    ipow(v_0, 55)
                    sage: v._get_etb() is etb
                    True
                    sage: v.base()
                    v_0
                    sage: v.exponent()
                    55
        """
    def base(self) -> _B:
        """ExpressionIPow.base(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1425)

        Return the base from this :class:`ExpressionIPow`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: (etb(33)^42).base()                                                   # needs sage.symbolic
            33"""
    def exponent(self) -> _E:
        """ExpressionIPow.exponent(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1438)

        Return the exponent from this :class:`ExpressionIPow`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: (etb(x)^(-1)).exponent()                                              # needs sage.symbolic
            -1"""

class ExpressionVariable(Expression):
    """
    An Expression that represents a variable.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb.var(x))                                                          # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionVariable'>"""
    def __init__(self, etb: ExpressionTreeBuilder, n: Int):
        """
                Initialize an ExpressionVariable.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder, ExpressionVariable
                    sage: etb = ExpressionTreeBuilder(vars=(x,))
                    sage: etb(x)
                    v_0
                    sage: v = ExpressionVariable(etb, 0); v
                    v_0
                    sage: v._get_etb() is etb
                    True
                    sage: v.variable_index()
                    0
        """
    def variable_index(self) -> int:
        """ExpressionVariable.variable_index(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1259)

        Return the variable index of an :class:`ExpressionVariable`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb(x).variable_index()                                               # needs sage.symbolic
            0"""

class InstructionStream[_Domain]:
    """
    An :class:`InstructionStream` takes a sequence of instructions (passed in by
    a series of method calls) and computes the data structures needed
    by the interpreter.  This is the stage where we switch from operating
    on :class:`Expression` trees to a linear representation.  If we had a peephole
    optimizer (we don't) it would go here.

    Currently, this class is not very general; it only works for
    interpreters with a fixed set of memory chunks (with fixed names).
    Basically, it only works for stack-based expression interpreters.
    It should be generalized, so that the interpreter metadata includes
    a description of the memory chunks involved and the instruction stream
    can handle any interpreter.

    Once you're done adding instructions, you call :meth:`get_current` to retrieve
    the information needed by the interpreter (as a Python dictionary)."""
    def __init__(self, metadata: InterpreterMetadata, n_args: Int, domain: _Domain | None = None):
        """
                Initialize an :class:`InstructionStream`.

                INPUT:

                - ``metadata`` -- the ``metadata_by_opname`` from a wrapper module

                - ``n_args`` -- the number of arguments accessible by the generated code
                  (this is just passed to the wrapper class)

                - ``domain`` -- the domain of interpretation (this is just passed to the
                  wrapper class)

                EXAMPLES::

                    sage: from sage.ext.interpreters.wrapper_el import metadata
                    sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
                    sage: from sage.ext.fast_callable import InstructionStream
                    sage: instr_stream = InstructionStream(metadata, 1)
                    sage: instr_stream.get_current()
                    {'args': 1,
                     'code': [],
                     'constants': [],
                     'domain': None,
                     'py_constants': [],
                     'stack': 0}
                    sage: md = instr_stream.get_metadata()
                    sage: type(md)
                    <class 'sage.ext.fast_callable.InterpreterMetadata'>
                    sage: md.by_opname['py_call']
                    (CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs']), 3)
                    sage: md.by_opcode[3]
                    ('py_call', CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs']))
        """
    def current_op_list(self) -> _OpList:
        """
        Return the list of instructions that have been added to this
        :class:`InstructionStream` so far.

        It's OK to call this, then add more instructions.

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream
            sage: instr_stream = InstructionStream(metadata, 1)
            sage: instr_stream.instr('load_arg', 0)
            sage: instr_stream.instr('py_call', math.sin, 1)
            sage: instr_stream.instr('abs')
            sage: instr_stream.instr('return')
            sage: instr_stream.current_op_list()
            [('load_arg', 0), ('py_call', <built-in function sin>, 1), 'abs', 'return']"""
    def get_current(self) -> _State[_Domain]:
        """
        Return the current state of the :class:`InstructionStream`, as a dictionary
        suitable for passing to a wrapper class.

        NOTE: The dictionary includes internal data structures of the
        :class:`InstructionStream`; you must not modify it.

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream
            sage: instr_stream = InstructionStream(metadata, 1)
            sage: instr_stream.get_current()
            {'args': 1,
             'code': [],
             'constants': [],
             'domain': None,
             'py_constants': [],
             'stack': 0}
            sage: instr_stream.instr('load_arg', 0)
            sage: instr_stream.instr('py_call', math.sin, 1)
            sage: instr_stream.instr('abs')
            sage: instr_stream.instr('return')
            sage: instr_stream.current_op_list()
            [('load_arg', 0), ('py_call', <built-in function sin>, 1), 'abs', 'return']
            sage: instr_stream.get_current()
            {'args': 1,
             'code': [0, 0, 3, 0, 1, 12, 2],
             'constants': [],
             'domain': None,
             'py_constants': [<built-in function sin>],
             'stack': 1}"""
    def get_metadata(self) -> InterpreterMetadata:
        """
        Return the interpreter metadata being used by the current :class:`InstructionStream`.

        The code generator sometimes uses this to decide which code
        to generate.

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream
            sage: instr_stream = InstructionStream(metadata, 1)
            sage: md = instr_stream.get_metadata()
            sage: type(md)
            <class 'sage.ext.fast_callable.InterpreterMetadata'>"""
    def has_instr(self, opname) -> bool:
        """InstructionStream.has_instr(self, opname) -> bool

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2157)

        Check whether this :class:`InstructionStream` knows how to generate code
        for a given instruction.

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream
            sage: instr_stream = InstructionStream(metadata, 1)
            sage: instr_stream.has_instr('return')
            True
            sage: instr_stream.has_instr('factorial')
            False
            sage: instr_stream.has_instr('abs')
            True"""
    def instr(self, opname: str, *args) -> None:
        """
        Generate code in this :class:`InstructionStream` for the given instruction
        and arguments.

        The opname is used to look up a :class:`CompilerInstrSpec`; the
        :class:`CompilerInstrSpec` describes how to interpret the arguments.
        (This is documented in the class docstring for :class:`CompilerInstrSpec`.)

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream
            sage: instr_stream = InstructionStream(metadata, 1)
            sage: instr_stream.instr('load_arg', 0)
            sage: instr_stream.instr('sin')                                             # needs sage.symbolic
            sage: instr_stream.instr('py_call', math.sin, 1)
            sage: instr_stream.instr('abs')
            sage: instr_stream.instr('factorial')
            Traceback (most recent call last):
            ...
            KeyError: 'factorial'
            sage: instr_stream.instr('return')
            sage: instr_stream.current_op_list()                                        # needs sage.symbolic
            [('load_arg', 0), 'sin', ('py_call', <built-in function sin>, 1), 'abs', 'return']"""
    def load_arg(self, n) -> None:
        """
        Add a ``'load_arg'`` instruction to this :class:`InstructionStream`.

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream
            sage: instr_stream = InstructionStream(metadata, 12)
            sage: instr_stream.load_arg(5)
            sage: instr_stream.current_op_list()
            [('load_arg', 5)]
            sage: instr_stream.load_arg(3)
            sage: instr_stream.current_op_list()
            [('load_arg', 5), ('load_arg', 3)]"""
    def load_const(self, c) -> None:
        """
        Add a ``'load_const'`` instruction to this :class:`InstructionStream`.

        EXAMPLES::

            sage: from sage.ext.interpreters.wrapper_el import metadata
            sage: from sage.ext.interpreters.wrapper_rdf import metadata                # needs sage.modules
            sage: from sage.ext.fast_callable import InstructionStream, op_list
            sage: instr_stream = InstructionStream(metadata, 1)
            sage: instr_stream.load_const(5)
            sage: instr_stream.current_op_list()
            [('load_const', 5)]
            sage: instr_stream.load_const(7)
            sage: instr_stream.load_const(5)
            sage: instr_stream.current_op_list()
            [('load_const', 5), ('load_const', 7), ('load_const', 5)]

        Note that constants are shared: even though we load 5 twice, it
        only appears once in the constant table. ::

            sage: instr_stream.get_current()['constants']
            [5, 7]"""

class IntegerPowerFunction[_N]:
    """
        This class represents the function `x^n` for an arbitrary integral power `n`.

        That is, ``IntegerPowerFunction(2)`` is the squaring function;
        ``IntegerPowerFunction(-1)`` is the reciprocal function.

        EXAMPLES::

            sage: from sage.ext.fast_callable import IntegerPowerFunction
            sage: square = IntegerPowerFunction(2)
            sage: square
            (^2)
            sage: square(pi)                                                                # needs sage.symbolic
            pi^2
            sage: square(I)                                                                 # needs sage.symbolic
            -1
            sage: square(RIF(-1, 1)).str(style='brackets')                                  # needs sage.rings.real_interval_field
            '[0.0000000000000000 .. 1.0000000000000000]'
            sage: IntegerPowerFunction(-1)
            (^(-1))
            sage: IntegerPowerFunction(-1)(22/7)
            7/22
            sage: v = Integers(123456789)(54321)
            sage: v^9876543210
            79745229
            sage: IntegerPowerFunction(9876543210)(v)
            79745229
    """
    def __init__(self, n: _N):
        """
        Initialize an :class:`IntegerPowerFunction`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import IntegerPowerFunction
            sage: cube = IntegerPowerFunction(3)
            sage: cube
            (^3)
            sage: cube(AA(7)^(1/3))                                                     # needs sage.rings.number_field
            7.000000000000000?
            sage: cube.exponent
            3"""
    @overload
    def __call__[_X, _P](self: IntegerPowerFunction[SupportsPowWithExponent[_X, _P]], x: _X) -> _P: ...
    @overload
    def __call__[_P](self, x: SupportsRPowWithBase[_N, _P]) -> _P:
        """
        Call this :class:`IntegerPowerFunction`, to compute a power of its argument.

        EXAMPLES::

            sage: from sage.ext.fast_callable import IntegerPowerFunction
            sage: square = IntegerPowerFunction(2)
            sage: square.__call__(5)
            25
            sage: square(5)
            25"""

class InterpreterMetadata:
    """
    The interpreter metadata for a :func:`fast_callable` interpreter.

    Currently consists of a dictionary mapping instruction names to
    (:class:`CompilerInstrSpec`, opcode) pairs, a list mapping opcodes to
    (instruction name, :class:`CompilerInstrSpec`) pairs, and a range of exponents
    for which the ``'ipow'`` instruction can be used.  This range can be
    ``False`` (if the ``'ipow'`` instruction should never be used), a pair of
    two integers `(a, b)`, if ``'ipow'`` should be used for `a \\le n \\le b`, or
    ``True``, if ``'ipow'`` should always be used.  When ``'ipow'`` cannot be
    used, then we fall back on calling :class:`IntegerPowerFunction`.

    See the class docstring for :class:`CompilerInstrSpec` for more information.

    NOTE: You must not modify the metadata."""
    by_opcode: list[tuple[str, CompilerInstrSpec]]
    by_opname: dict[str, tuple[CompilerInstrSpec, int]]
    ipow_range: bool | tuple[Int, Int]
    def __init__(
        self, 
        by_opname: dict[str, tuple[CompilerInstrSpec, int]], 
        by_opcode: list[tuple[str, CompilerInstrSpec]], 
        ipow_range: bool | tuple[Int, Int]
    ):
        """
                Initialize an InterpreterMetadata object.

                EXAMPLES::

                    sage: from sage.ext.fast_callable import InterpreterMetadata
                    sage: metadata = InterpreterMetadata(by_opname={'opname dict goes here': True},
                    ....:                                by_opcode=['opcode list goes here'],
                    ....:                                ipow_range=(2, 57))
                    sage: metadata.by_opname
                    {'opname dict goes here': True}
                    sage: metadata.by_opcode
                    ['opcode list goes here']
                    sage: metadata.ipow_range
                    (2, 57)
        """

class _State[_Domain](TypedDict):
    args: int
    constants: list
    py_constants: Any
    stack: int
    code: list[int]
    domain: _Domain

type _OpList = list[str | tuple[str, *tuple[Any, ...]]]

def op_list(args: _State, metadata: InterpreterMetadata) -> _OpList:
    r"""
    Given a dictionary with the result of calling :meth:`get_current` on an
    :class:`InstructionStream`, and the corresponding interpreter metadata,
    return a list of the instructions, in a simple somewhat
    human-readable format.

    For debugging only.  (That is, it's probably not a good idea to
    try to programmatically manipulate the result of this function;
    the expected use is just to print the returned list to the
    screen.)

    There's probably no reason to call this directly; if you
    have a wrapper object, call :func:`op_list` on it; if you have an
    :class:`InstructionStream` object, call :meth:`current_op_list` on it.

    EXAMPLES::

        sage: from sage.ext.interpreters.wrapper_el import metadata
        sage: from sage.ext.interpreters.wrapper_rdf import metadata                    # needs sage.modules
        sage: from sage.ext.fast_callable import InstructionStream, op_list
        sage: instr_stream = InstructionStream(metadata, 1)
        sage: instr_stream.instr('load_arg', 0)
        sage: instr_stream.instr('abs')
        sage: instr_stream.instr('return')
        sage: instr_stream.current_op_list()
        [('load_arg', 0), 'abs', 'return']
        sage: op_list(instr_stream.get_current(), metadata)
        [('load_arg', 0), 'abs', 'return']
    """

class CompilerInstrSpec:
    """
        Describe a single instruction to the :func:`fast_callable` code generator.

        An instruction has a number of stack inputs, a number of stack
        outputs, and a parameter list describing extra arguments that
        must be passed to the :meth:`InstructionStream.instr` method (that end up
        as extra words in the code).

        The parameter list is a list of strings.  Each string is one of
        the following:

        - ``'args'`` -- the instruction argument refers to an input argument of the
          wrapper class; it is just appended to the code

        - ``'constants'``, ``'py_constants'`` -- the instruction argument is a value; the
          value is added to the corresponding list (if it's not already there) and
          the index is appended to the code.

        - ``'n_inputs'``, ``'n_outputs'`` -- the instruction actually takes a variable
          number of inputs or outputs (the ``n_inputs`` and ``n_outputs`` attributes of
          this instruction are ignored). The instruction argument specifies the
          number of inputs or outputs (respectively); it is just appended to the
          code.
    """
    def __init__(self, 
        n_inputs: Int, 
        n_outputs: Int, 
        parameters: list[
            Literal["args", "constants", "py_constants", "n_inputs", "n_outputs"]]
    ):
        """
        Initialize a :class:`CompilerInstrSpec`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import CompilerInstrSpec
            sage: CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])
            CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])"""
    def __repr__(self) -> str:
        r"""
        Give a string representation for this :class:`CompilerInstrSpec`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import CompilerInstrSpec
            sage: v = CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])
            sage: v
            CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])
            sage: repr(v)
            "CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])"
            sage: v.__repr__()
            "CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])"
        """

class Wrapper:
    """
    The parent class for all :func:`fast_callable` wrappers.

    Implements shared behavior (currently only debugging)."""
    def __init__(self, args: _State, metadata: InterpreterMetadata):
        """
                Initialize a Wrapper object.

                EXAMPLES::

                    sage: # needs sage.symbolic
                    sage: from sage.ext.fast_callable import ExpressionTreeBuilder, generate_code, InstructionStream
                    sage: etb = ExpressionTreeBuilder('x')
                    sage: x = etb.var('x')
                    sage: expr = (x+pi) * (x+1)
                    sage: from sage.ext.interpreters.wrapper_py import metadata, Wrapper_py
                    sage: instr_stream = InstructionStream(metadata, 1)
                    sage: generate_code(expr, instr_stream)
                    sage: instr_stream.instr('return')
                    sage: v = Wrapper_py(instr_stream.get_current())
                    sage: v.get_orig_args()
                    {'args': 1,
                     'code': [0, 0, 1, 0, 4, 0, 0, 1, 1, 4, 6, 2],
                     'constants': [pi, 1],
                     'domain': None,
                     'py_constants': [],
                     'stack': 3}
                    sage: v.op_list()
                    [('load_arg', 0), ('load_const', pi), 'add', ('load_arg', 0), ('load_const', 1), 'add', 'mul', 'return']
        """
    def get_orig_args(self) -> _State:
        """
        Get the original arguments used when initializing this wrapper.

        (Probably only useful when writing doctests.)

        EXAMPLES::

            sage: fast_callable(sin(x)/x, vars=[x], domain=RDF).get_orig_args()         # needs sage.symbolic
            {'args': 1,
             'code': [0, 0, 16, 0, 0, 8, 2],
             'constants': [],
             'domain': Real Double Field,
             'py_constants': [],
             'stack': 2}"""
    def op_list(self) -> _OpList:
        """
        Return the list of instructions in this wrapper.

        EXAMPLES::

            sage: fast_callable(cos(x) * x, vars=[x], domain=RDF).op_list()             # needs sage.symbolic
            [('load_arg', 0), ('load_arg', 0), 'cos', 'mul', 'return']"""
    def python_calls(self) -> list:
        """
        List the Python functions that are called in this wrapper.

        (Python function calls are slow, so ideally this list would
        be empty.  If it is not empty, then perhaps there is an
        optimization opportunity where a Sage developer could speed
        this up by adding a new instruction to the interpreter.)

        EXAMPLES::

            sage: fast_callable(abs(sin(x)), vars=[x], domain=RDF).python_calls()       # needs sage.symbolic
            []
            sage: fast_callable(abs(sin(factorial(x))), vars=[x]).python_calls()        # needs sage.symbolic
            [factorial, sin]"""

class FastCallableFloatWrapper:
    '''
        A class to alter the return types of the fast-callable functions.

        When applying numerical routines (including plotting) to symbolic
        expressions and functions, we generally first convert them to a
        faster form with :func:`fast_callable`.  That function takes a
        ``domain`` parameter that forces the end (and all intermediate)
        results of evaluation to a specific type.  Though usually always
        want the end result to be of type :class:`float`, correctly choosing
        the ``domain`` presents some problems:

          * :class:`float` is a bad choice because it\'s common for real
            functions to have complex terms in them. Moreover precision
            issues can produce terms like ``1.0 + 1e-12*I`` that are hard
            to avoid if calling ``real()`` on everything is infeasible.

          * :class:`complex` has essentially the same problem as :class:`float`.
            There are several symbolic functions like :func:`min_symbolic`,
            :func:`max_symbolic`, and :func:`floor` that are unable to
            operate on complex numbers.

          * ``None`` leaves the types of the inputs/outputs alone, but due
            to the lack of a specialized interpreter, slows down evaluation
            by an unacceptable amount.

          * ``CDF`` has none of the other issues, because ``CDF`` has its
            own specialized interpreter, a lexicographic ordering (for
            min/max), and supports :func:`floor`. However, most numerical
            functions cannot handle complex numbers, so using ``CDF``
            would require us to wrap every evaluation in a
            ``CDF``-to-:class:`float` conversion routine. That would slow
            things down less than a domain of ``None`` would, but is
            unattractive mainly because of how invasive it would be to
            "fix" the output everywhere.

        Creating a new fast-callable interpreter that has different input
        and output types solves most of the problems with a ``CDF``
        domain, but :func:`fast_callable` and the interpreter classes in
        :mod:`sage.ext.interpreters` are not really written with that in
        mind. The ``domain`` parameter to :func:`fast_callable`, for
        example, is expecting a single Sage ring that corresponds to one
        interpreter. You can make it accept, for example, a string like
        "CDF-to-float", but the hacks required to make that work feel
        wrong.

        Thus we arrive at this solution: a class to wrap the result of
        :func:`fast_callable`. Whenever we need to support intermediate
        complex terms in a numerical routine, we can set ``domain=CDF``
        while creating its fast-callable incarnation, and then wrap the
        result in this class. The :meth:`__call__` method of this class then
        ensures that the ``CDF`` output is converted to a :class:`float` if
        its imaginary part is within an acceptable tolerance.

        EXAMPLES:

        An error is thrown if the answer is complex::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import FastCallableFloatWrapper
            sage: f = sqrt(x)
            sage: ff = fast_callable(f, vars=[x], domain=CDF)
            sage: fff = FastCallableFloatWrapper(ff, imag_tol=1e-8)
            sage: fff(1)
            1.0
            sage: fff(-1)
            Traceback (most recent call last):
            ...
            ValueError: complex fast-callable function result
            1.0*I for arguments (-1,)
    '''
    def __init__(self, ff: Wrapper_cdf, imag_tol: Real):
        """
        Construct a :class:`FastCallableFloatWrapper`.

        INPUT:

          - ``ff`` -- a fast-callable wrapper over ``CDF``; an instance of
            :class:`sage.ext.interpreters.Wrapper_cdf`, usually constructed
            with :func:`fast_callable`.

          - ``imag_tol`` -- float; how big of an imaginary part we're willing
            to ignore before raising an error

        OUTPUT:

        An instance of :class:`FastCallableFloatWrapper` that can be
        called just like ``ff``, but that always returns a :class:`float`
        if no error is raised. A :exc:`ValueError` is raised if the
        imaginary part of the result exceeds ``imag_tol``.

        EXAMPLES:

        The wrapper will ignore an imaginary part smaller in magnitude
        than ``imag_tol``, but not one larger::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import FastCallableFloatWrapper
            sage: f = x
            sage: ff = fast_callable(f, vars=[x], domain=CDF)
            sage: fff = FastCallableFloatWrapper(ff, imag_tol=1e-8)
            sage: fff(I*1e-9)
            0.0
            sage: fff = FastCallableFloatWrapper(ff, imag_tol=1e-12)
            sage: fff(I*1e-9)
            Traceback (most recent call last):
            ...
            ValueError: complex fast-callable function result 1e-09*I for
            arguments (1.00000000000000e-9*I,)"""
    def __call__(self, *args: Num) -> float:
        """
        Evaluate the underlying fast-callable and convert the result to :class:`float`.

        TESTS:

        Evaluation either returns a :class:`float`, or raises a :exc:`ValueError`::

            sage: # needs sage.symbolic
            sage: from sage.ext.fast_callable import FastCallableFloatWrapper
            sage: f = x
            sage: ff = fast_callable(f, vars=[x], domain=CDF)
            sage: fff = FastCallableFloatWrapper(ff, imag_tol=0.1)
            sage: try:
            ....:     result = fff(CDF.random_element())
            ....: except ValueError:
            ....:     result = float(0)
            sage: type(result) is float
            True"""

