import _cython_3_2_1
import sage.structure.sage_object
from sage.misc.fpickle import pickle_function as pickle_function, unpickle_function as unpickle_function
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.symbolic.expression import call_registered_function as call_registered_function, find_registered_function as find_registered_function, get_sfunction_from_hash as get_sfunction_from_hash, get_sfunction_from_serial as get_sfunction_from_serial, register_or_update_function as register_or_update_function
from sage.symbolic.symbols import register_symbol as register_symbol
from typing import Any, ClassVar, overload

pickle_wrapper: _cython_3_2_1.cython_function_or_method
sfunctions_funcs: list
symbol_table: dict
unpickle_wrapper: _cython_3_2_1.cython_function_or_method

class BuiltinFunction(Function):
    """BuiltinFunction(name, nargs=1, latex_name=None, conversions=None, evalf_params_first=True, alt_name=None, preserved_arg=None)

    File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 875)

    This is the base class for symbolic functions defined in Sage.

    If a function is provided by the Sage library, we don't need to pickle
    the custom methods, since we can just initialize the same library function
    again. This allows us to use Cython for custom methods.

    We assume that each subclass of this class will define one symbolic
    function. Make sure you use subclasses and not just call the initializer
    of this class."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, nargs=..., latex_name=..., conversions=..., evalf_params_first=..., alt_name=..., preserved_arg=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 887)

                TESTS::

                    sage: from sage.functions.trig import Function_cot
                    sage: c = Function_cot()  # indirect doctest
                    sage: c(pi/2)                                                               # needs sage.symbolic
                    0
        """
    def __call__(self, *args, boolcoerce=..., boolhold=..., booldont_call_method_on_arg=...) -> Any:
        '''BuiltinFunction.__call__(self, *args, bool coerce=True, bool hold=False, bool dont_call_method_on_arg=False)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 944)

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
            \'foo\''''
    @overload
    def __reduce__(self) -> Any:
        """BuiltinFunction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 1161)

        EXAMPLES::

            sage: cot.__reduce__()
            (<class 'sage.functions.trig.Function_cot'>, ())

            sage: f = loads(dumps(cot)) #indirect doctest
            sage: f(pi/2)                                                               # needs sage.symbolic
            0"""
    @overload
    def __reduce__(self) -> Any:
        """BuiltinFunction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 1161)

        EXAMPLES::

            sage: cot.__reduce__()
            (<class 'sage.functions.trig.Function_cot'>, ())

            sage: f = loads(dumps(cot)) #indirect doctest
            sage: f(pi/2)                                                               # needs sage.symbolic
            0"""

class Function(sage.structure.sage_object.SageObject):
    """Function(name, nargs, latex_name=None, conversions=None, evalf_params_first=True, alt_name=None)

    File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 170)

    Base class for symbolic functions defined through Pynac in Sage.

    This is an abstract base class, with generic code for the interfaces
    and a :meth:`__call__` method. Subclasses should implement the
    :meth:`_is_registered` and :meth:`_register_function` methods.

    This class is not intended for direct use, instead use one of the
    subclasses :class:`BuiltinFunction` or :class:`SymbolicFunction`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, nargs, latex_name=..., conversions=..., evalf_params_first=..., alt_name=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 181)

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
        '''
    @overload
    def default_variable(self) -> Any:
        """Function.default_variable(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 603)

        Return a default variable.

        EXAMPLES::

            sage: sin.default_variable()                                                # needs sage.symbolic
            x"""
    @overload
    def default_variable(self) -> Any:
        """Function.default_variable(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 603)

        Return a default variable.

        EXAMPLES::

            sage: sin.default_variable()                                                # needs sage.symbolic
            x"""
    @overload
    def name(self) -> Any:
        '''Function.name(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 561)

        Return the name of this function.

        EXAMPLES::

            sage: foo = function("foo", nargs=2)                                        # needs sage.symbolic
            sage: foo.name()                                                            # needs sage.symbolic
            \'foo\''''
    @overload
    def name(self) -> Any:
        '''Function.name(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 561)

        Return the name of this function.

        EXAMPLES::

            sage: foo = function("foo", nargs=2)                                        # needs sage.symbolic
            sage: foo.name()                                                            # needs sage.symbolic
            \'foo\''''
    @overload
    def number_of_arguments(self) -> Any:
        '''Function.number_of_arguments(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 573)

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
            TypeError: Symbolic function foo takes exactly 2 arguments (1 given)'''
    @overload
    def number_of_arguments(self) -> Any:
        '''Function.number_of_arguments(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 573)

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
            TypeError: Symbolic function foo takes exactly 2 arguments (1 given)'''
    @overload
    def variables(self) -> Any:
        """Function.variables(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 592)

        Return the variables (of which there are none) present in this function.

        EXAMPLES::

            sage: sin.variables()
            ()"""
    @overload
    def variables(self, ofwhichtherearenone) -> Any:
        """Function.variables(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 592)

        Return the variables (of which there are none) present in this function.

        EXAMPLES::

            sage: sin.variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """Function.variables(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 592)

        Return the variables (of which there are none) present in this function.

        EXAMPLES::

            sage: sin.variables()
            ()"""
    def __call__(self, *args, boolcoerce=..., boolhold=...) -> Any:
        '''Function.__call__(self, *args, bool coerce=True, bool hold=False)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 411)

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
            array([ 2., -3.])'''
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """Function.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 351)

        EXAMPLES::

            sage: f = function('f', nargs=1, conjugate_func=lambda self, x: 2r*x)       # needs sage.symbolic
            sage: f.__hash__()    # random                                              # needs sage.symbolic
            -2224334885124003860
            sage: hash(f(2))      # random                                              # needs sage.symbolic
            4168614485"""
    @overload
    def __hash__(self) -> Any:
        """Function.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 351)

        EXAMPLES::

            sage: f = function('f', nargs=1, conjugate_func=lambda self, x: 2r*x)       # needs sage.symbolic
            sage: f.__hash__()    # random                                              # needs sage.symbolic
            -2224334885124003860
            sage: hash(f(2))      # random                                              # needs sage.symbolic
            4168614485"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class GinacFunction(BuiltinFunction):
    """GinacFunction(name, nargs=1, latex_name=None, conversions=None, ginac_name=None, evalf_params_first=True, preserved_arg=None, alt_name=None)

    File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 824)

    This class provides a wrapper around symbolic functions already defined in
    Pynac/GiNaC.

    GiNaC provides custom methods for these functions defined at the C++ level.
    It is still possible to define new custom functionality or override those
    already defined.

    There is also no need to register these functions."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, nargs=..., latex_name=..., conversions=..., ginac_name=..., evalf_params_first=..., preserved_arg=..., alt_name=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 835)

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

class SymbolicFunction(Function):
    """SymbolicFunction(name, nargs=0, latex_name=None, conversions=None, evalf_params_first=True)

    File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 1195)

    This is the basis for user defined symbolic functions. We try to pickle or
    hash the custom methods, so subclasses must be defined in Python not Cython."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 1200)

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
    def __hash__(self) -> Any:
        '''SymbolicFunction.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/function.pyx (starting at line 1256)

        TESTS::

            sage: foo = function("foo", nargs=2)                                        # needs sage.symbolic
            sage: hash(foo)      # random output                                        # needs sage.symbolic
            -6859868030555295348

            sage: def ev(self, x): return 2*x
            sage: foo = function("foo", nargs=2, eval_func=ev)                          # needs sage.symbolic
            sage: hash(foo)      # random output                                        # needs sage.symbolic
            -6859868030555295348'''
