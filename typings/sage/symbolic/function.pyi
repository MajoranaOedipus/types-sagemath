r"""
Classes for symbolic functions

.. _symbolic-function-classes:

To enable their usage as part of symbolic expressions, symbolic function
classes are derived from one of the subclasses of :class:`Function`:

 * :class:`BuiltinFunction`: the code of these functions is written in Python;
   many :ref:`special functions<special-functions>` are of this type
 * :class:`GinacFunction`: the code of these functions is written in C++ and
   part of the Pynac support library; most elementary functions are of this type
 * :class:`SymbolicFunction`: symbolic functions defined on the Sage command
   line are of this type

Sage uses ``BuiltinFunction`` and ``GinacFunction`` for its symbolic builtin
functions. Users can define any other additional ``SymbolicFunction`` through
the ``function()`` factory, see :doc:`function_factory`

Several parameters are supported by the superclass' ``__init__()`` method.
Examples follow below.

 * ``nargs``: the number of arguments
 * ``name``: the string that is printed on the CLI; the name of the member
   functions that are attempted for evaluation of Sage element arguments; also
   the name of the Pynac function that is associated with a ``GinacFunction``
 * ``alt_name``: the second name of the member functions that are attempted for
   evaluation of Sage element arguments
 * ``latex_name``: what is printed when ``latex(f(...))`` is called
 * ``conversions``: a dict containing the function's name in other CAS
 * ``evalf_params_first``: if ``False``, when floating-point evaluating the
   expression do not evaluate function arguments before calling the
   ``_evalf_()`` member of the function
 * ``preserved_arg``: if nonzero, the index (starting with ``1``) of the
   function argument that determines the return type. Note that, e.g,
   ``atan2()`` uses both arguments to determine return type, through a
   different mechanism

Function classes can define the following Python member functions:

 * ``_eval_(*args)``: the only mandatory member function, evaluating the
   argument and returning the result; if ``None`` is returned the expression
   stays unevaluated
 * ``_eval_numpy_(*args)``: evaluation of ``f(args)`` with arguments of numpy
   type
 * ``_evalf_(*args, **kwds)``: called when the expression is floating-point
   evaluated; may receive a ``parent`` keyword specifying the expected parent
   of the result. If not defined an attempt is made to convert the result of
   ``_eval_()``.
 * ``_conjugate_(*args)``, ``_real_part_(*args)``, ``_imag_part_(*args)``:
   return conjugate, real part, imaginary part of the expression ``f(args)``
 * ``_derivative_(*args, index)``: return derivative with respect to the
   parameter indexed by ``index`` (starting with 0) of ``f(args)``
 * ``_tderivative_()``: same as ``_derivative_()`` but don't apply chain rule;
   only one of the two functions may be defined
 * ``_power_(*args, expo)``: return ``f(args)^expo``
 * ``_series_(*args, **kwds)``: return the power series at ``at`` up to
   ``order`` with respect to ``var`` of ``f(args)``; these three values are
   received in ``kwds``. If not defined the series is attempted to be computed
   by differentiation.
 * ``print(*args)``: return what should be printed on the CLI with ``f(args)``
 * ``print_latex(*args)``: return what should be output with ``latex(f(args))``

The following examples are intended for Sage developers. Users can define
functions interactively through the ``function()`` factory, see
:doc:`function_factory`.

EXAMPLES:

The simplest example is a function returning nothing, it practically behaves
like a symbol. Setting ``nargs=0`` allows any number of arguments::

    sage: from sage.symbolic.function import BuiltinFunction
    sage: class Test1(BuiltinFunction):
    ....:     def __init__(self):
    ....:         BuiltinFunction.__init__(self, 'test', nargs=0)
    ....:     def _eval_(self, *args):
    ....:         pass
    sage: f = Test1()
    sage: f()                                                                           # needs sage.symbolic
    test()
    sage: f(1,2,3)*f(1,2,3)                                                             # needs sage.symbolic
    test(1, 2, 3)^2

In the following the ``sin`` function of ``CBF(0)`` is called because with
floating point arguments the ``CBF`` element's ``my_sin()`` member function
is attempted, and after that ``sin()`` which succeeds::

    sage: class Test2(BuiltinFunction):
    ....:     def __init__(self):
    ....:         BuiltinFunction.__init__(self, 'my_sin', alt_name='sin',
    ....:                                  latex_name=r'\SIN', nargs=1)
    ....:     def _eval_(self, x):
    ....:         return 5
    ....:     def _evalf_(self, x, **kwds):
    ....:         return 3.5
    sage: f = Test2()
    sage: f(0)
    5
    sage: f(0, hold=True)                                                               # needs sage.symbolic
    my_sin(0)
    sage: f(0, hold=True).n()                                                           # needs sage.rings.real_mpfr
    3.50000000000000
    sage: f(CBF(0))                                                                     # needs sage.libs.flint
    0

    sage: latex(f(0, hold=True))                                                        # needs sage.symbolic
    \SIN\left(0\right)
    sage: f(1,2)
    Traceback (most recent call last):
    ...
    TypeError: Symbolic function my_sin takes exactly 1 arguments (2 given)
"""
from types import FunctionType
from typing import Any, Literal, Self, SupportsInt, overload
from typings_sagemath import SupportsKeysAndGetItem, Supports__code__
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SymbolicRing
from sage.rings.integer import Integer

from sage.misc.fpickle import pickle_function as pickle_function, unpickle_function as unpickle_function
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.symbolic.expression import call_registered_function as call_registered_function, find_registered_function as find_registered_function, get_sfunction_from_hash as get_sfunction_from_hash, get_sfunction_from_serial as get_sfunction_from_serial, register_or_update_function as register_or_update_function
from sage.symbolic.symbols import register_symbol as register_symbol

type _int = SupportsInt
type _Nargs = int | Integer # SupportsInt and can do arithmatics with int

sfunctions_funcs: list[
    Literal[
        "eval",
        "evalf",
        "conjugate",
        "real_part",
        "imag_part",
        "derivative",
        "power",
        "series",
        "print",
        "print_latex",
        "tderivative",
    ]
]
symbol_table: dict

class Function(SageObject):
    """
    Base class for symbolic functions defined through Pynac in Sage.

    This is an abstract base class, with generic code for the interfaces
    and a :meth:`__call__` method. Subclasses should implement the
    :meth:`_is_registered` and :meth:`_register_function` methods.

    This class is not intended for direct use, instead use one of the
    subclasses :class:`BuiltinFunction` or :class:`SymbolicFunction`."""

    def __init__(
        self, 
        name: str, 
        nargs: _Nargs, 
        latex_name: str | None = None, 
        conversions: SupportsKeysAndGetItem[str, str] | None = None, 
        evalf_params_first: bool | None = None, 
        alt_name: str | None = None
    ):
        """
                This is an abstract base class. It\'s not possible to test it directly.

                EXAMPLES::

                    sage: f = function(\'f\', nargs=1,  # indirect doctest                        # needs sage.symbolic
                    ....:              conjugate_func=lambda self, x: 2r*x)
                    sage: f(2)                                                                  # needs sage.symbolic
                    f(2)
                    sage: f(2).conjugate()                                                      # needs sage.symbolic
                    4

                TESTS::

                    # eval_func raises exception
                    sage: def ef(self, x): raise RuntimeError("foo")
                    sage: bar = function("bar", nargs=1, eval_func=ef)                          # needs sage.symbolic
                    sage: bar(x)                                                                # needs sage.symbolic
                    Traceback (most recent call last):
                    ...
                    RuntimeError: foo

                    # eval_func returns non coercible
                    sage: def ef(self, x): return ZZ
                    sage: bar = function("bar", nargs=1, eval_func=ef)                          # needs sage.symbolic
                    sage: bar(x)                                                                # needs sage.symbolic
                    Traceback (most recent call last):
                    ...
                    TypeError: function did not return a symbolic expression
                    or an element that can be coerced into a symbolic expression

                    # eval_func is not callable
                    sage: bar = function("bar", nargs=1, eval_func=5)                           # needs sage.symbolic
                    Traceback (most recent call last):
                    ...
                    ValueError: eval_func parameter must be callable
        """
    def default_variable(self) -> Expression[SymbolicRing]:
        """
        Return a default variable.

        EXAMPLES::

            sage: sin.default_variable()                                                # needs sage.symbolic
            x"""
    def name(self) -> str:
        """
        Return the name of this function.

        EXAMPLES::

            sage: foo = function("foo", nargs=2)                                        # needs sage.symbolic
            sage: foo.name()                                                            # needs sage.symbolic
            \'foo\'"""
    def number_of_arguments(self) -> _Nargs:
        """
        Return the number of arguments that this function takes.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: foo = function("foo", nargs=2)
            sage: foo.number_of_arguments()
            2
            sage: foo(x, x)
            foo(x, x)
            sage: foo(x)
            Traceback (most recent call last):
            ...
            TypeError: Symbolic function foo takes exactly 2 arguments (1 given)"""
    def variables(self) -> tuple[()]:
        """
        Return the variables (of which there are none) present in this function.

        EXAMPLES::

            sage: sin.variables()
            ()"""
    @overload
    def __call__(
        self, *args: Expression, coerce: Literal[False] = ..., hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(self, *args, coerce: bool = True, hold: bool = False) -> Any:
        """
        Evaluates this function at the given arguments.

        We coerce the arguments into symbolic expressions if ``coerce=True``, then
        call the Pynac evaluation method, which in turn passes the arguments to
        a custom automatic evaluation method if ``_eval_()`` is defined.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: foo = function("foo", nargs=2)
            sage: x,y,z = var("x y z")
            sage: foo(x, y)
            foo(x, y)
            sage: foo(y)
            Traceback (most recent call last):
            ...
            TypeError: Symbolic function foo takes exactly 2 arguments (1 given)
            sage: bar = function("bar")
            sage: bar(x)
            bar(x)
            sage: bar(x, y)
            bar(x, y)

        The `hold` argument prevents automatic evaluation of the function::

            sage: exp(log(x))                                                           # needs sage.symbolic
            x
            sage: exp(log(x), hold=True)                                                # needs sage.symbolic
            e^log(x)

        We can also handle numpy types::

            sage: import numpy                                                          # needs numpy
            sage: sin(numpy.arange(5))                                                  # needs numpy
            array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ])

        Symbolic functions evaluate non-exact input numerically, and return
        symbolic expressions on exact input, or if any input is symbolic::

            sage: arctan(1)                                                             # needs sage.symbolic
            1/4*pi
            sage: arctan(float(1))                                                      # needs sage.rings.complex_double
            0.7853981633974483
            sage: type(lambert_w(SR(0)))                                                # needs sage.symbolic
            <class \'sage.symbolic.expression.Expression\'>

        Precision of the result depends on the precision of the input::

            sage: arctan(RR(1))                                                         # needs sage.rings.real_mpfr
            0.785398163397448
            sage: arctan(RealField(100)(1))                                             # needs sage.rings.real_mpfr
            0.78539816339744830961566084582

        Return types for non-exact input depends on the input type::

            sage: type(exp(float(0)))
            <... \'float\'>
            sage: exp(RR(0)).parent()
            Real Field with 53 bits of precision


        TESTS:

        Test coercion::

            sage: bar(ZZ)                                                               # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: cannot coerce arguments: ...
            sage: exp(QQbar(I))                                                         # needs sage.rings.number_field sage.symbolic
            e^I

        For functions with single argument, if coercion fails we try to call
        a method with the name of the function on the object::

            sage: M = matrix(SR, 2, 2, [x, 0, 0, I*pi])                                 # needs sage.modules sage.symbolic
            sage: exp(M)                                                                # needs sage.modules sage.symbolic
            [e^x   0]
            [  0  -1]

        Make sure we can pass mpmath arguments (:issue:`13608`)::

            sage: import mpmath                                                         # needs mpmath
            sage: with mpmath.workprec(128): sin(mpmath.mpc(\'0.5\', \'1.2\'))              # needs mpmath
            mpc(real=\'0.86807452059118713192871150787046523179886\',
                imag=\'1.3246769633571289324095313649562791720086\')

        Check that :issue:`10133` is fixed::

            sage: # needs sage.symbolic
            sage: out = sin(0)
            sage: out, parent(out)
            (0, Integer Ring)
            sage: out = sin(int(0))
            sage: (out, parent(out))
            (0, <... \'int\'>)
            sage: out = arctan2(int(0), float(1))
            sage: (out, parent(out))
            (0, <... \'int\'>)
            sage: out = arctan2(int(0), RR(1))
            sage: (out, parent(out))
            (0, Integer Ring)

        Check that ``real_part`` and ``imag_part`` still works after :issue:`21216`::

            sage: # needs numpy sage.symbolic
            sage: import numpy
            sage: a = numpy.array([1+2*I, -2-3*I], dtype=complex)
            sage: real_part(a)
            array([ 1., -2.])
            sage: imag_part(a)
            array([ 2., -3.])"""
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __ge__(self, other: Function) -> bool: ...
    def __gt__(self, other: Function) -> bool: ...
    def __le__(self, other: Function) -> bool: ...
    def __lt__(self, other: Function) -> bool: ...

    def __hash__(self) -> int:
        """
        EXAMPLES::

            sage: f = function('f', nargs=1, conjugate_func=lambda self, x: 2r*x)       # needs sage.symbolic
            sage: f.__hash__()    # random                                              # needs sage.symbolic
            -2224334885124003860
            sage: hash(f(2))      # random                                              # needs sage.symbolic
            4168614485"""
    def __repr__(self) -> str:
        """
        EXAMPLES::

            sage: foo = function("foo", nargs=2); foo                                   # needs sage.symbolic
            foo
        """

class GinacFunction(BuiltinFunction):
    """
    This class provides a wrapper around symbolic functions already defined in
    Pynac/GiNaC.

    GiNaC provides custom methods for these functions defined at the C++ level.
    It is still possible to define new custom functionality or override those
    already defined.

    There is also no need to register these functions."""

    def __init__(
        self,
        name: str,
        nargs: _Nargs = 1,
        latex_name: str | None = None,
        conversions: SupportsKeysAndGetItem[str, str] | None = None,
        ginac_name: str | None = None,
        evalf_params_first: bool | None = None,
        preserved_arg: _Nargs | None = None,
        alt_name: str | None = None,
    ):
        """
                TESTS::

                    sage: from sage.functions.trig import Function_sin
                    sage: s = Function_sin()  # indirect doctest
                    sage: s(0)                                                                  # needs sage.symbolic
                    0
                    sage: s(pi)                                                                 # needs sage.symbolic
                    0
                    sage: s(pi/2)                                                               # needs sage.symbolic
                    1
        """

class BuiltinFunction(Function):
    """
    This is the base class for symbolic functions defined in Sage.

    If a function is provided by the Sage library, we don't need to pickle
    the custom methods, since we can just initialize the same library function
    again. This allows us to use Cython for custom methods.

    We assume that each subclass of this class will define one symbolic
    function. Make sure you use subclasses and not just call the initializer
    of this class."""

    def __init__(
        self,
        name: str,
        nargs: _Nargs = 1,
        latex_name: str | None = None,
        conversions: SupportsKeysAndGetItem[str, str] | None = None,
        ginac_name: str | None = None,
        evalf_params_first: bool | None = None,
        alt_name: str | None = None,
        preserved_arg: _Nargs | None = None,
    ):
        """
                TESTS::

                    sage: from sage.functions.trig import Function_cot
                    sage: c = Function_cot()  # indirect doctest
                    sage: c(pi/2)                                                               # needs sage.symbolic
                    0
        """
    def __call__(
        self,
        *args,
        coerce: bool = True,
        hold: bool = False,
        dont_call_method_on_arg: bool = False,
    ) -> Any:
        """
        Evaluate this function on the given arguments and return the result.

        EXAMPLES::

            sage: exp(5)                                                                # needs sage.symbolic
            e^5
            sage: gamma(15)
            87178291200

        Python float, Python complex, mpmath mpf and mpc as well as numpy inputs
        are sent to the relevant ``math``, ``cmath``, ``mpmath`` or ``numpy``
        function::

            sage: cos(1.r)
            0.5403023058681398
            sage: assert type(_) is float
            sage: gamma(4.r)
            6.0
            sage: assert type(_) is float

            sage: cos(1jr)  # abstol 1e-15
            (1.5430806348152437-0j)
            sage: assert type(_) is complex

            sage: # needs mpmath
            sage: import mpmath
            sage: cos(mpmath.mpf(\'1.321412\'))
            mpf(\'0.24680737898640387\')
            sage: cos(mpmath.mpc(1,1))
            mpc(real=\'0.83373002513114902\', imag=\'-0.98889770576286506\')

            sage: import numpy                                                          # needs numpy
            sage: if int(numpy.version.short_version[0]) > 1:                           # needs numpy
            ....:     __ = numpy.set_printoptions(legacy="1.25")                        # needs numpy

            sage: sin(numpy.int32(0))                                                   # needs numpy
            0.0
            sage: type(_)                                                               # needs numpy
            <class \'numpy.float64\'>

        TESTS::

            sage: from sage.symbolic.function import BuiltinFunction
            sage: class A:
            ....:     def foo(self):
            ....:         return \'foo\'
            sage: foo = BuiltinFunction(name=\'foo\')
            sage: foo(A())
            \'foo\'
            sage: bar = BuiltinFunction(name=\'bar\', alt_name=\'foo\')
            sage: bar(A())
            \'foo\'"""
    def __reduce__(self) -> tuple[type[Self], tuple[()]]:
        """
        EXAMPLES::

            sage: cot.__reduce__()
            (<class 'sage.functions.trig.Function_cot'>, ())

            sage: f = loads(dumps(cot)) #indirect doctest
            sage: f(pi/2)                                                               # needs sage.symbolic
            0"""

class SymbolicFunction(Function):
    """
    This is the basis for user defined symbolic functions. We try to pickle or
    hash the custom methods, so subclasses must be defined in Python not Cython."""
    
    def __init__(
        self,
        name: str,
        nargs: _Nargs = 0,
        latex_name: str | None = None,
        conversions: SupportsKeysAndGetItem[str, str] | None = None,
        evalf_params_first: bool | None = True,
    ):
        """
                EXAMPLES::

                    sage: from sage.symbolic.function import SymbolicFunction
                    sage: class my_function(SymbolicFunction):
                    ....:     def __init__(self):
                    ....:         SymbolicFunction.__init__(self, 'foo', nargs=2)
                    ....:     def _evalf_(self, x, y, parent=None, algorithm=None):
                    ....:         return x*y*2r
                    ....:     def _conjugate_(self, x, y):
                    ....:         return x
                    sage: foo = my_function()
                    sage: foo
                    foo
                    sage: foo(2, 3)                                                             # needs sage.symbolic
                    foo(2, 3)
                    sage: foo(2, 3).n()                                                         # needs sage.rings.real_mpfr
                    12.0000000000000
                    sage: foo(2, 3).conjugate()                                                 # needs sage.symbolic
                    2
        """
    def __hash__(self) -> int:
        """
        TESTS::

            sage: foo = function("foo", nargs=2)                                        # needs sage.symbolic
            sage: hash(foo)      # random output                                        # needs sage.symbolic
            -6859868030555295348

            sage: def ev(self, x): return 2*x
            sage: foo = function("foo", nargs=2, eval_func=ev)                          # needs sage.symbolic
            sage: hash(foo)      # random output                                        # needs sage.symbolic
            -6859868030555295348"""

@overload
def pickle_wrapper(f: Supports__code__) -> bytes: ...
@overload
def pickle_wrapper(f: None) -> None:
    """
    Return a pickled version of the function ``f``.

    If ``f`` is ``None``, just return ``None``.

    This is a wrapper around :func:`pickle_function`.

    EXAMPLES::

        sage: from sage.symbolic.function import pickle_wrapper
        sage: def f(x): return x*x
        sage: isinstance(pickle_wrapper(f), bytes)
        True
        sage: pickle_wrapper(None) is None
        True
    """

@overload
def unpickle_wrapper(p: bytes) -> FunctionType: ...
@overload
def unpickle_wrapper(p: None) -> None:
    """
    Return a unpickled version of the function defined by ``p``.

    If ``p`` is ``None``, just return ``None``.

    This is a wrapper around :func:`unpickle_function`.

    EXAMPLES::

        sage: from sage.symbolic.function import pickle_wrapper, unpickle_wrapper
        sage: def f(x): return x*x
        sage: s = pickle_wrapper(f)
        sage: g = unpickle_wrapper(s)
        sage: g(2)
        4
        sage: unpickle_wrapper(None) is None
        True
    """

from sage.symbolic.expression import (
    call_registered_function, find_registered_function,
    register_or_update_function, get_sfunction_from_hash, 
    get_sfunction_from_serial
)