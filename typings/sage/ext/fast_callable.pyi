import _cython_3_2_1
import sage as sage
from sage.categories.category import ZZ as ZZ
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

fast_callable: _cython_3_2_1.cython_function_or_method
function_name: _cython_3_2_1.cython_function_or_method
generate_code: _cython_3_2_1.cython_function_or_method
get_builtin_functions: _cython_3_2_1.cython_function_or_method
nan: float
op_list: _cython_3_2_1.cython_function_or_method

class CompilerInstrSpec:
    """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2385)

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
    def __init__(self, n_inputs, n_outputs, parameters) -> Any:
        """CompilerInstrSpec.__init__(self, n_inputs, n_outputs, parameters)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2411)

        Initialize a :class:`CompilerInstrSpec`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import CompilerInstrSpec
            sage: CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])
            CompilerInstrSpec(0, 1, ['py_constants', 'n_inputs'])"""

class Expression:
    """Expression(etb)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 862)

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
    def __init__(self, etb) -> Any:
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
    @overload
    def abs(self) -> Any:
        """Expression.abs(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1118)

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
    @overload
    def abs(self, x) -> Any:
        """Expression.abs(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1118)

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
    @overload
    def abs(self, v_0) -> Any:
        """Expression.abs(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1118)

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
    @overload
    def abs(self) -> Any:
        """Expression.abs(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1118)

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
    @overload
    def abs(self, v_0) -> Any:
        """Expression.abs(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1118)

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
    @overload
    def abs(self, v_0) -> Any:
        """Expression.abs(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1118)

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
    @overload
    def __abs__(self) -> Any:
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
    @overload
    def __abs__(self) -> Any:
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
    def __add__(self, s, o) -> Any:
        """Expression.__add__(s, o)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 923)

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
    def __floordiv__(self, s, o) -> Any:
        """Expression.__floordiv__(s, o)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1015)

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
    @overload
    def __invert__(self) -> Any:
        """Expression.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1137)

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
    @overload
    def __invert__(self) -> Any:
        """Expression.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1137)

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
    def __mul__(self, s, o) -> Any:
        """Expression.__mul__(s, o)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 969)

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
    @overload
    def __neg__(self) -> Any:
        """Expression.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1082)

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
    def __neg__(self) -> Any:
        """Expression.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1082)

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
    def __pow__(self, s, o, dummy) -> Any:
        """Expression.__pow__(s, o, dummy)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1038)

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
    def __radd__(self, other):
        """Return value+self."""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __sub__(self, s, o) -> Any:
        """Expression.__sub__(s, o)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 946)

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
    def __truediv__(self, s, o) -> Any:
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

class ExpressionCall(Expression):
    """ExpressionCall(etb, fn, args)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1295)

    An Expression that represents a function call.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb.call(sin, x))                                                    # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionCall'>"""
    def __init__(self, etb, fn, args) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1309)

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
    @overload
    def arguments(self) -> Any:
        """ExpressionCall.arguments(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1347)

        Return the arguments from this :class:`ExpressionCall`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.call(sin, x).arguments()                                          # needs sage.symbolic
            [v_0]"""
    @overload
    def arguments(self) -> Any:
        """ExpressionCall.arguments(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1347)

        Return the arguments from this :class:`ExpressionCall`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.call(sin, x).arguments()                                          # needs sage.symbolic
            [v_0]"""
    @overload
    def function(self) -> Any:
        """ExpressionCall.function(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1334)

        Return the function from this :class:`ExpressionCall`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.call(sin, x).function()                                           # needs sage.symbolic
            sin"""
    @overload
    def function(self) -> Any:
        """ExpressionCall.function(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1334)

        Return the function from this :class:`ExpressionCall`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.call(sin, x).function()                                           # needs sage.symbolic
            sin"""

class ExpressionChoice(Expression):
    """ExpressionChoice(etb, cond, iftrue, iffalse)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1476)

    A conditional expression.

    (It's possible to create choice nodes, but they don't work yet.)

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: etb.choice(etb.call(operator.eq, x, 0), 0, 1/x)                           # needs sage.symbolic
        (0 if {eq}(v_0, 0) else div(1, v_0))"""
    def __init__(self, etb, cond, iftrue, iffalse) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1494)

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
    @overload
    def condition(self) -> Any:
        """ExpressionChoice.condition(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1522)

        Return the condition of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).condition()                                      # needs sage.symbolic
            v_0"""
    @overload
    def condition(self) -> Any:
        """ExpressionChoice.condition(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1522)

        Return the condition of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).condition()                                      # needs sage.symbolic
            v_0"""
    @overload
    def if_false(self) -> Any:
        """ExpressionChoice.if_false(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1550)

        Return the false branch of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).if_false()                                       # needs sage.symbolic
            0"""
    @overload
    def if_false(self) -> Any:
        """ExpressionChoice.if_false(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1550)

        Return the false branch of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).if_false()                                       # needs sage.symbolic
            0"""
    @overload
    def if_true(self) -> Any:
        """ExpressionChoice.if_true(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1536)

        Return the true branch of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).if_true()                                        # needs sage.symbolic
            inv(v_0)"""
    @overload
    def if_true(self) -> Any:
        """ExpressionChoice.if_true(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1536)

        Return the true branch of an :class:`ExpressionChoice`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: x = etb(x)                                                            # needs sage.symbolic
            sage: etb.choice(x, ~x, 0).if_true()                                        # needs sage.symbolic
            inv(v_0)"""

class ExpressionConstant(Expression):
    """ExpressionConstant(etb, c)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1155)

    An Expression that represents an arbitrary constant.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb(3))                                                              # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionConstant'>"""
    def __init__(self, etb, c) -> Any:
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
    @overload
    def value(self) -> Any:
        """ExpressionConstant.value(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1192)

        Return the constant value of an :class:`ExpressionConstant`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb(3).value()                                                        # needs sage.symbolic
            3"""
    @overload
    def value(self) -> Any:
        """ExpressionConstant.value(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1192)

        Return the constant value of an :class:`ExpressionConstant`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb(3).value()                                                        # needs sage.symbolic
            3"""

class ExpressionIPow(Expression):
    """ExpressionIPow(etb, base, exponent)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1386)

    A power Expression with an integer exponent.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb.var('x')^17)                                                     # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionIPow'>"""
    def __init__(self, etb, base, exponent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1400)

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
    @overload
    def base(self) -> Any:
        """ExpressionIPow.base(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1425)

        Return the base from this :class:`ExpressionIPow`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: (etb(33)^42).base()                                                   # needs sage.symbolic
            33"""
    @overload
    def base(self) -> Any:
        """ExpressionIPow.base(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1425)

        Return the base from this :class:`ExpressionIPow`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: (etb(33)^42).base()                                                   # needs sage.symbolic
            33"""
    @overload
    def exponent(self) -> Any:
        """ExpressionIPow.exponent(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1438)

        Return the exponent from this :class:`ExpressionIPow`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: (etb(x)^(-1)).exponent()                                              # needs sage.symbolic
            -1"""
    @overload
    def exponent(self) -> Any:
        """ExpressionIPow.exponent(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1438)

        Return the exponent from this :class:`ExpressionIPow`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: (etb(x)^(-1)).exponent()                                              # needs sage.symbolic
            -1"""

class ExpressionTreeBuilder:
    """ExpressionTreeBuilder(vars, domain=None)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 611)

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
    def __init__(self, vars, domain=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 631)

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
    @overload
    def call(self, fn, *args) -> Any:
        """ExpressionTreeBuilder.call(self, fn, *args)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 791)

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
    @overload
    def call(self, cos, x) -> Any:
        """ExpressionTreeBuilder.call(self, fn, *args)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 791)

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
    def choice(self, cond, iftrue, iffalse) -> Any:
        """ExpressionTreeBuilder.choice(self, cond, iftrue, iffalse)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 824)

        Construct a choice node (a conditional expression), given the
        condition, and the values for the true and false cases.

        (It's possible to create choice nodes, but they don't work yet.)

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb.choice(etb.call(operator.eq, x, 0), 0, 1/x)                       # needs sage.symbolic
            (0 if {eq}(v_0, 0) else div(1, v_0))"""
    @overload
    def constant(self, c) -> Any:
        """ExpressionTreeBuilder.constant(self, c)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 720)

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
    @overload
    def constant(self, pi) -> Any:
        """ExpressionTreeBuilder.constant(self, c)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 720)

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
    @overload
    def constant(self, pi) -> Any:
        """ExpressionTreeBuilder.constant(self, c)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 720)

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
    @overload
    def var(self, v) -> Any:
        """ExpressionTreeBuilder.var(self, v)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 739)

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
    @overload
    def var(self, some_really_long_name) -> Any:
        """ExpressionTreeBuilder.var(self, v)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 739)

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
    @overload
    def var(self, x) -> Any:
        """ExpressionTreeBuilder.var(self, v)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 739)

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
    def __call__(self, x) -> Any:
        """ExpressionTreeBuilder.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 667)

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

class ExpressionVariable(Expression):
    """ExpressionVariable(etb, int n)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1225)

    An Expression that represents a variable.

    EXAMPLES::

        sage: from sage.ext.fast_callable import ExpressionTreeBuilder
        sage: etb = ExpressionTreeBuilder(vars=(x,))                                    # needs sage.symbolic
        sage: type(etb.var(x))                                                          # needs sage.symbolic
        <class 'sage.ext.fast_callable.ExpressionVariable'>"""
    def __init__(self, etb, intn) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1238)

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
    @overload
    def variable_index(self) -> Any:
        """ExpressionVariable.variable_index(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1259)

        Return the variable index of an :class:`ExpressionVariable`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb(x).variable_index()                                               # needs sage.symbolic
            0"""
    @overload
    def variable_index(self) -> Any:
        """ExpressionVariable.variable_index(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1259)

        Return the variable index of an :class:`ExpressionVariable`.

        EXAMPLES::

            sage: from sage.ext.fast_callable import ExpressionTreeBuilder
            sage: etb = ExpressionTreeBuilder(vars=(x,))                                # needs sage.symbolic
            sage: etb(x).variable_index()                                               # needs sage.symbolic
            0"""

class FastCallableFloatWrapper:
    '''File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2588)

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
    def __init__(self, ff, imag_tol) -> Any:
        """FastCallableFloatWrapper.__init__(self, ff, imag_tol)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2659)

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
    def __call__(self, *args) -> Any:
        """FastCallableFloatWrapper.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2701)

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

class InstructionStream:
    """InstructionStream(metadata, n_args, domain=None)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2034)

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
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, metadata, n_args, domain=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2065)

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
    def current_op_list(self) -> Any:
        """InstructionStream.current_op_list(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2276)

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
    @overload
    def get_current(self) -> Any:
        """InstructionStream.get_current(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2298)

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
    @overload
    def get_current(self) -> Any:
        """InstructionStream.get_current(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2298)

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
    @overload
    def get_current(self) -> Any:
        """InstructionStream.get_current(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2298)

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
    @overload
    def get_metadata(self) -> Any:
        """InstructionStream.get_metadata(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2257)

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
    @overload
    def get_metadata(self) -> Any:
        """InstructionStream.get_metadata(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2257)

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
    def instr(self, opname, *args) -> Any:
        """InstructionStream.instr(self, opname, *args)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2177)

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
    def load_arg(self, n) -> Any:
        """InstructionStream.load_arg(self, n)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2138)

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
    def load_const(self, c) -> Any:
        """InstructionStream.load_const(self, c)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2112)

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

class IntegerPowerFunction:
    """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1640)

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
    def __init__(self, n) -> Any:
        """IntegerPowerFunction.__init__(self, n)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1670)

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
    def __call__(self, x) -> Any:
        """IntegerPowerFunction.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 1709)

        Call this :class:`IntegerPowerFunction`, to compute a power of its argument.

        EXAMPLES::

            sage: from sage.ext.fast_callable import IntegerPowerFunction
            sage: square = IntegerPowerFunction(2)
            sage: square.__call__(5)
            25
            sage: square(5)
            25"""

class InterpreterMetadata:
    """InterpreterMetadata(by_opname, by_opcode, ipow_range)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2342)

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
    by_opcode: by_opcode
    by_opname: by_opname
    ipow_range: ipow_range
    def __init__(self, by_opname, by_opcode, ipow_range) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2363)

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

class Wrapper:
    """Wrapper(args, metadata)

    File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2494)

    The parent class for all :func:`fast_callable` wrappers.

    Implements shared behavior (currently only debugging)."""
    def __init__(self, args, metadata) -> Any:
        """File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2501)

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
    @overload
    def get_orig_args(self) -> Any:
        """Wrapper.get_orig_args(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2535)

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
    @overload
    def get_orig_args(self) -> Any:
        """Wrapper.get_orig_args(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2535)

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
    @overload
    def op_list(self) -> Any:
        """Wrapper.op_list(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2553)

        Return the list of instructions in this wrapper.

        EXAMPLES::

            sage: fast_callable(cos(x) * x, vars=[x], domain=RDF).op_list()             # needs sage.symbolic
            [('load_arg', 0), ('load_arg', 0), 'cos', 'mul', 'return']"""
    @overload
    def op_list(self) -> Any:
        """Wrapper.op_list(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2553)

        Return the list of instructions in this wrapper.

        EXAMPLES::

            sage: fast_callable(cos(x) * x, vars=[x], domain=RDF).op_list()             # needs sage.symbolic
            [('load_arg', 0), ('load_arg', 0), 'cos', 'mul', 'return']"""
    @overload
    def python_calls(self) -> Any:
        """Wrapper.python_calls(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2564)

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
    @overload
    def python_calls(self) -> Any:
        """Wrapper.python_calls(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2564)

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
    @overload
    def python_calls(self) -> Any:
        """Wrapper.python_calls(self)

        File: /build/sagemath/src/sage/src/sage/ext/fast_callable.pyx (starting at line 2564)

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
