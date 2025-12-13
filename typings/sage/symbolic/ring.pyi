import _cython_3_2_1
import sage as sage
import sage.categories.morphism
import sage.rings.abc
from sage.symbolic.expression import Expression as Expression
from sage.categories.category import ZZ as ZZ
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

KEYWORDS: set
is_SymbolicVariable: _cython_3_2_1.cython_function_or_method
isidentifier: _cython_3_2_1.cython_function_or_method
the_SymbolicRing: _cython_3_2_1.cython_function_or_method
var: _cython_3_2_1.cython_function_or_method

class NumpyToSRMorphism(sage.categories.morphism.Morphism):
    '''NumpyToSRMorphism(numpy_type)

    File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1151)

    A morphism from numpy types to the symbolic ring.

    TESTS:

    We check that :issue:`8949` and :issue:`9769` are fixed (see also :issue:`18076`)::

        sage: import numpy                                                              # needs numpy
        sage: if int(numpy.version.short_version[0]) > 1:                               # needs numpy
        ....:     _ = numpy.set_printoptions(legacy="1.25")                                 # needs numpy
        sage: f(x) = x^2
        sage: f(numpy.int8(\'2\'))                                                        # needs numpy
        4
        sage: f(numpy.int32(\'3\'))                                                       # needs numpy
        9

    Note that the answer is a Sage integer and not a numpy type::

        sage: a = f(numpy.int8(\'2\')).pyobject()                                         # needs numpy
        sage: type(a)                                                                   # needs numpy
        <class \'sage.rings.integer.Integer\'>

    This behavior also applies to standard functions::

        sage: cos(int(\'2\'))
        cos(2)
        sage: numpy.cos(int(\'2\'))                                                       # needs numpy
        -0.4161468365471424'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, numpy_type) -> Any:
        """File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1183)

                A Morphism which constructs Expressions from NumPy floats and
                complexes by converting them to elements of either RDF or CDF.

                INPUT:

                - ``numpy_type`` -- a numpy number type

                EXAMPLES::

                    sage: # needs numpy
                    sage: import numpy
                    sage: from sage.symbolic.ring import NumpyToSRMorphism
                    sage: f = NumpyToSRMorphism(numpy.float64)
                    sage: f(numpy.float64('2.0'))
                    2.0
                    sage: _.parent()
                    Symbolic Ring

                    sage: NumpyToSRMorphism(str)                                                # needs numpy
                    Traceback (most recent call last):
                    ...
                    TypeError: <... 'str'> is not a numpy number type
        """

class SymbolicRing(sage.rings.abc.SymbolicRing):
    """SymbolicRing(base_ring=None)

    File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 69)

    Symbolic Ring, parent object for all symbolic expressions."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    symbols: symbols
    def __init__(self, base_ring=...):
        """File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 73)

                Initialize the Symbolic Ring.

                This is a commutative ring of symbolic expressions and functions.

                EXAMPLES::

                    sage: SR
                    Symbolic Ring

                TESTS::

                    sage: isinstance(SR, sage.symbolic.ring.SymbolicRing)
                    True
                    sage: TestSuite(SR).run(skip=['_test_divides'])
        """
    def I(self) -> Expression:
        """SymbolicRing.I(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 590)

        The imaginary unit, viewed as an element of the symbolic ring.

        EXAMPLES::

            sage: SR.I()^2
            -1
            sage: SR.I().parent()
            Symbolic Ring

        TESTS:

        Test that :issue:`32404` is fixed::

            sage: SR0 = SR.subring(no_variables=True)
            sage: SR0.I().parent()
            Symbolic Constants Subring"""
    
    @overload
    def characteristic(self) -> Any:
        """SymbolicRing.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 511)

        Return the characteristic of the symbolic ring, which is 0.

        OUTPUT: a Sage integer

        EXAMPLES::

            sage: c = SR.characteristic(); c
            0
            sage: type(c)
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def characteristic(self) -> Any:
        """SymbolicRing.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 511)

        Return the characteristic of the symbolic ring, which is 0.

        OUTPUT: a Sage integer

        EXAMPLES::

            sage: c = SR.characteristic(); c
            0
            sage: type(c)
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def cleanup_var(self, symbol) -> Any:
        """SymbolicRing.cleanup_var(self, symbol)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 717)

        Cleans up a variable, removing assumptions about the
        variable and allowing for it to be garbage collected

        INPUT:

        - ``symbol`` -- a variable or a list of variables

        TESTS:

            sage: from sage.symbolic.assumptions import assumptions
            sage: symbols_copy = SR.symbols.copy()
            sage: assumptions_copy = assumptions().copy()
            sage: x = SR.temp_var(domain='real')
            sage: SR.cleanup_var(x)
            sage: symbols_copy == SR.symbols
            True
            sage: assumptions_copy == assumptions()
            True"""
    @overload
    def cleanup_var(self, x) -> Any:
        """SymbolicRing.cleanup_var(self, symbol)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 717)

        Cleans up a variable, removing assumptions about the
        variable and allowing for it to be garbage collected

        INPUT:

        - ``symbol`` -- a variable or a list of variables

        TESTS:

            sage: from sage.symbolic.assumptions import assumptions
            sage: symbols_copy = SR.symbols.copy()
            sage: assumptions_copy = assumptions().copy()
            sage: x = SR.temp_var(domain='real')
            sage: SR.cleanup_var(x)
            sage: symbols_copy == SR.symbols
            True
            sage: assumptions_copy == assumptions()
            True"""
    @overload
    def is_exact(self) -> bool:
        """SymbolicRing.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 561)

        Return ``False``, because there are approximate elements in the
        symbolic ring.

        EXAMPLES::

            sage: SR.is_exact()
            False

        Here is an inexact element.

        ::

            sage: SR(1.9393)
            1.93930000000000"""
    @overload
    def is_exact(self) -> Any:
        """SymbolicRing.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 561)

        Return ``False``, because there are approximate elements in the
        symbolic ring.

        EXAMPLES::

            sage: SR.is_exact()
            False

        Here is an inexact element.

        ::

            sage: SR(1.9393)
            1.93930000000000"""
    @overload
    def is_field(self, proof=...) -> Any:
        """SymbolicRing.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 538)

        Return ``True``, since the symbolic expression ring is (for the most
        part) a field.

        EXAMPLES::

            sage: SR.is_field()
            True"""
    @overload
    def is_field(self) -> Any:
        """SymbolicRing.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 538)

        Return ``True``, since the symbolic expression ring is (for the most
        part) a field.

        EXAMPLES::

            sage: SR.is_field()
            True"""
    @overload
    def is_finite(self) -> Any:
        """SymbolicRing.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 550)

        Return ``False``, since the Symbolic Ring is infinite.

        EXAMPLES::

            sage: SR.is_finite()
            False"""
    @overload
    def is_finite(self) -> Any:
        """SymbolicRing.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 550)

        Return ``False``, since the Symbolic Ring is infinite.

        EXAMPLES::

            sage: SR.is_finite()
            False"""
    @overload
    def pi(self) -> Any:
        """SymbolicRing.pi(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 580)

        EXAMPLES::

            sage: SR.pi() is pi
            True"""
    @overload
    def pi(self) -> Any:
        """SymbolicRing.pi(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 580)

        EXAMPLES::

            sage: SR.pi() is pi
            True"""
    @overload
    def subring(self, *args, **kwds) -> Any:
        """SymbolicRing.subring(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1044)

        Create a subring of this symbolic ring.

        INPUT:

        Choose one of the following keywords to create a subring.

        - ``accepting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in only these variables is created.

        - ``rejecting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in variables distinct to these variables is
          created.

        - ``no_variables`` -- boolean (default: ``False``); if set,
          then a symbolic subring of constant expressions (i.e.,
          expressions without a variable) is created.

        OUTPUT: a ring

        EXAMPLES:

        Let us create a couple of symbolic variables first::

            sage: V = var('a, b, r, s, x, y')

        Now we create a symbolic subring only accepting expressions in
        the variables `a` and `b`::

            sage: A = SR.subring(accepting_variables=(a, b)); A
            Symbolic Subring accepting the variables a, b

        An element is
        ::

            sage: A.an_element()
            a

        From our variables in `V` the following are valid in `A`::

            sage: tuple(v for v in V if v in A)
            (a, b)

        Next, we create a symbolic subring rejecting expressions with
        given variables::

            sage: R = SR.subring(rejecting_variables=(r, s)); R
            Symbolic Subring rejecting the variables r, s

        An element is
        ::

            sage: R.an_element()
            some_variable

        From our variables in `V` the following are valid in `R`::

            sage: tuple(v for v in V if v in R)
            (a, b, x, y)

        We have a third kind of subring, namely the subring of
        symbolic constants::

            sage: C = SR.subring(no_variables=True); C
            Symbolic Constants Subring

        Note that this subring can be considered as a special accepting
        subring; one without any variables.

        An element is
        ::

            sage: C.an_element()
            I*pi*e

        None of our variables in `V` is valid in `C`::

            sage: tuple(v for v in V if v in C)
            ()

        .. SEEALSO::

            :doc:`subring`"""
    @overload
    def subring(self, accepting_variables=...) -> Any:
        """SymbolicRing.subring(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1044)

        Create a subring of this symbolic ring.

        INPUT:

        Choose one of the following keywords to create a subring.

        - ``accepting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in only these variables is created.

        - ``rejecting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in variables distinct to these variables is
          created.

        - ``no_variables`` -- boolean (default: ``False``); if set,
          then a symbolic subring of constant expressions (i.e.,
          expressions without a variable) is created.

        OUTPUT: a ring

        EXAMPLES:

        Let us create a couple of symbolic variables first::

            sage: V = var('a, b, r, s, x, y')

        Now we create a symbolic subring only accepting expressions in
        the variables `a` and `b`::

            sage: A = SR.subring(accepting_variables=(a, b)); A
            Symbolic Subring accepting the variables a, b

        An element is
        ::

            sage: A.an_element()
            a

        From our variables in `V` the following are valid in `A`::

            sage: tuple(v for v in V if v in A)
            (a, b)

        Next, we create a symbolic subring rejecting expressions with
        given variables::

            sage: R = SR.subring(rejecting_variables=(r, s)); R
            Symbolic Subring rejecting the variables r, s

        An element is
        ::

            sage: R.an_element()
            some_variable

        From our variables in `V` the following are valid in `R`::

            sage: tuple(v for v in V if v in R)
            (a, b, x, y)

        We have a third kind of subring, namely the subring of
        symbolic constants::

            sage: C = SR.subring(no_variables=True); C
            Symbolic Constants Subring

        Note that this subring can be considered as a special accepting
        subring; one without any variables.

        An element is
        ::

            sage: C.an_element()
            I*pi*e

        None of our variables in `V` is valid in `C`::

            sage: tuple(v for v in V if v in C)
            ()

        .. SEEALSO::

            :doc:`subring`"""
    @overload
    def subring(self, rejecting_variables=...) -> Any:
        """SymbolicRing.subring(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1044)

        Create a subring of this symbolic ring.

        INPUT:

        Choose one of the following keywords to create a subring.

        - ``accepting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in only these variables is created.

        - ``rejecting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in variables distinct to these variables is
          created.

        - ``no_variables`` -- boolean (default: ``False``); if set,
          then a symbolic subring of constant expressions (i.e.,
          expressions without a variable) is created.

        OUTPUT: a ring

        EXAMPLES:

        Let us create a couple of symbolic variables first::

            sage: V = var('a, b, r, s, x, y')

        Now we create a symbolic subring only accepting expressions in
        the variables `a` and `b`::

            sage: A = SR.subring(accepting_variables=(a, b)); A
            Symbolic Subring accepting the variables a, b

        An element is
        ::

            sage: A.an_element()
            a

        From our variables in `V` the following are valid in `A`::

            sage: tuple(v for v in V if v in A)
            (a, b)

        Next, we create a symbolic subring rejecting expressions with
        given variables::

            sage: R = SR.subring(rejecting_variables=(r, s)); R
            Symbolic Subring rejecting the variables r, s

        An element is
        ::

            sage: R.an_element()
            some_variable

        From our variables in `V` the following are valid in `R`::

            sage: tuple(v for v in V if v in R)
            (a, b, x, y)

        We have a third kind of subring, namely the subring of
        symbolic constants::

            sage: C = SR.subring(no_variables=True); C
            Symbolic Constants Subring

        Note that this subring can be considered as a special accepting
        subring; one without any variables.

        An element is
        ::

            sage: C.an_element()
            I*pi*e

        None of our variables in `V` is valid in `C`::

            sage: tuple(v for v in V if v in C)
            ()

        .. SEEALSO::

            :doc:`subring`"""
    @overload
    def subring(self, no_variables=...) -> Any:
        """SymbolicRing.subring(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1044)

        Create a subring of this symbolic ring.

        INPUT:

        Choose one of the following keywords to create a subring.

        - ``accepting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in only these variables is created.

        - ``rejecting_variables`` -- (default: ``None``) a tuple or other
          iterable of variables. If specified, then a symbolic subring of
          expressions in variables distinct to these variables is
          created.

        - ``no_variables`` -- boolean (default: ``False``); if set,
          then a symbolic subring of constant expressions (i.e.,
          expressions without a variable) is created.

        OUTPUT: a ring

        EXAMPLES:

        Let us create a couple of symbolic variables first::

            sage: V = var('a, b, r, s, x, y')

        Now we create a symbolic subring only accepting expressions in
        the variables `a` and `b`::

            sage: A = SR.subring(accepting_variables=(a, b)); A
            Symbolic Subring accepting the variables a, b

        An element is
        ::

            sage: A.an_element()
            a

        From our variables in `V` the following are valid in `A`::

            sage: tuple(v for v in V if v in A)
            (a, b)

        Next, we create a symbolic subring rejecting expressions with
        given variables::

            sage: R = SR.subring(rejecting_variables=(r, s)); R
            Symbolic Subring rejecting the variables r, s

        An element is
        ::

            sage: R.an_element()
            some_variable

        From our variables in `V` the following are valid in `R`::

            sage: tuple(v for v in V if v in R)
            (a, b, x, y)

        We have a third kind of subring, namely the subring of
        symbolic constants::

            sage: C = SR.subring(no_variables=True); C
            Symbolic Constants Subring

        Note that this subring can be considered as a special accepting
        subring; one without any variables.

        An element is
        ::

            sage: C.an_element()
            I*pi*e

        None of our variables in `V` is valid in `C`::

            sage: tuple(v for v in V if v in C)
            ()

        .. SEEALSO::

            :doc:`subring`"""
    @overload
    def symbol(self, name=..., latex_name=..., domain=...) -> Any:
        '''SymbolicRing.symbol(self, name=None, latex_name=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 612)

        EXAMPLES::

            sage: t0 = SR.symbol("t0")
            sage: t0.conjugate()
            conjugate(t0)

            sage: t1 = SR.symbol("t1", domain=\'real\')
            sage: t1.conjugate()
            t1

            sage: t0.abs()
            abs(t0)

            sage: t0_2 = SR.symbol("t0", domain=\'positive\')
            sage: t0_2.abs()
            t0
            sage: bool(t0_2 == t0)
            True
            sage: t0.conjugate()
            t0

            sage: SR.symbol() # temporary variable
            symbol...

        We propagate the domain to the assumptions database::

            sage: n = var(\'n\', domain=\'integer\')
            sage: solve([n^2 == 3],n)
            []

        TESTS:

        Test that the parent is set correctly (inheritance)::

            sage: from sage.symbolic.ring import SymbolicRing
            sage: class MySymbolicRing(SymbolicRing):
            ....:     def _repr_(self):
            ....:         return \'My Symbolic Ring\'
            sage: MySR = MySymbolicRing()
            sage: MySR.symbol(\'x\').parent()
            My Symbolic Ring
            sage: MySR.var(\'x\').parent()  # indirect doctest
            My Symbolic Ring
            sage: MySR.var(\'blub\').parent()  # indirect doctest
            My Symbolic Ring
            sage: MySR.an_element().parent()
            My Symbolic Ring'''
    @overload
    def symbol(self) -> Any:
        '''SymbolicRing.symbol(self, name=None, latex_name=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 612)

        EXAMPLES::

            sage: t0 = SR.symbol("t0")
            sage: t0.conjugate()
            conjugate(t0)

            sage: t1 = SR.symbol("t1", domain=\'real\')
            sage: t1.conjugate()
            t1

            sage: t0.abs()
            abs(t0)

            sage: t0_2 = SR.symbol("t0", domain=\'positive\')
            sage: t0_2.abs()
            t0
            sage: bool(t0_2 == t0)
            True
            sage: t0.conjugate()
            t0

            sage: SR.symbol() # temporary variable
            symbol...

        We propagate the domain to the assumptions database::

            sage: n = var(\'n\', domain=\'integer\')
            sage: solve([n^2 == 3],n)
            []

        TESTS:

        Test that the parent is set correctly (inheritance)::

            sage: from sage.symbolic.ring import SymbolicRing
            sage: class MySymbolicRing(SymbolicRing):
            ....:     def _repr_(self):
            ....:         return \'My Symbolic Ring\'
            sage: MySR = MySymbolicRing()
            sage: MySR.symbol(\'x\').parent()
            My Symbolic Ring
            sage: MySR.var(\'x\').parent()  # indirect doctest
            My Symbolic Ring
            sage: MySR.var(\'blub\').parent()  # indirect doctest
            My Symbolic Ring
            sage: MySR.an_element().parent()
            My Symbolic Ring'''
    @overload
    def temp_var(self, n=..., domain=...) -> Any:
        """SymbolicRing.temp_var(self, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 664)

        Return one or multiple new unique symbolic variables as an element
        of the symbolic ring. Use this instead of SR.var() if there is a
        possibility of name clashes occuring. Call SR.cleanup_var() once
        the variables are no longer needed or use a `with SR.temp_var()
        as ...` construct.

        INPUT:

        - ``n`` -- (optional) positive integer; number of symbolic variables

        - ``domain`` -- (optional) specify the domain of the variable(s);

        EXAMPLES:

        Simple definition of a functional derivative::

            sage: def functional_derivative(expr, f, x):
            ....:     with SR.temp_var() as a:
            ....:         return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a)

        Contrast this to a similar implementation using SR.var(),
        which gives a wrong result in our example::

            sage: def functional_derivative(expr, f, x):
            ....:     a = SR.var('a')
            ....:     return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a) + 1

        TESTS:

            sage: x = SR.temp_var()
            sage: y = SR.temp_var()
            sage: bool(x == x)
            True
            sage: bool(x == y)
            False
            sage: bool(x.parent()(x._maxima_()) == x)
            True"""
    @overload
    def temp_var(self) -> Any:
        """SymbolicRing.temp_var(self, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 664)

        Return one or multiple new unique symbolic variables as an element
        of the symbolic ring. Use this instead of SR.var() if there is a
        possibility of name clashes occuring. Call SR.cleanup_var() once
        the variables are no longer needed or use a `with SR.temp_var()
        as ...` construct.

        INPUT:

        - ``n`` -- (optional) positive integer; number of symbolic variables

        - ``domain`` -- (optional) specify the domain of the variable(s);

        EXAMPLES:

        Simple definition of a functional derivative::

            sage: def functional_derivative(expr, f, x):
            ....:     with SR.temp_var() as a:
            ....:         return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a)

        Contrast this to a similar implementation using SR.var(),
        which gives a wrong result in our example::

            sage: def functional_derivative(expr, f, x):
            ....:     a = SR.var('a')
            ....:     return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a) + 1

        TESTS:

            sage: x = SR.temp_var()
            sage: y = SR.temp_var()
            sage: bool(x == x)
            True
            sage: bool(x == y)
            False
            sage: bool(x.parent()(x._maxima_()) == x)
            True"""
    @overload
    def temp_var(self) -> Any:
        """SymbolicRing.temp_var(self, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 664)

        Return one or multiple new unique symbolic variables as an element
        of the symbolic ring. Use this instead of SR.var() if there is a
        possibility of name clashes occuring. Call SR.cleanup_var() once
        the variables are no longer needed or use a `with SR.temp_var()
        as ...` construct.

        INPUT:

        - ``n`` -- (optional) positive integer; number of symbolic variables

        - ``domain`` -- (optional) specify the domain of the variable(s);

        EXAMPLES:

        Simple definition of a functional derivative::

            sage: def functional_derivative(expr, f, x):
            ....:     with SR.temp_var() as a:
            ....:         return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a)

        Contrast this to a similar implementation using SR.var(),
        which gives a wrong result in our example::

            sage: def functional_derivative(expr, f, x):
            ....:     a = SR.var('a')
            ....:     return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a) + 1

        TESTS:

            sage: x = SR.temp_var()
            sage: y = SR.temp_var()
            sage: bool(x == x)
            True
            sage: bool(x == y)
            False
            sage: bool(x.parent()(x._maxima_()) == x)
            True"""
    @overload
    def temp_var(self) -> Any:
        """SymbolicRing.temp_var(self, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 664)

        Return one or multiple new unique symbolic variables as an element
        of the symbolic ring. Use this instead of SR.var() if there is a
        possibility of name clashes occuring. Call SR.cleanup_var() once
        the variables are no longer needed or use a `with SR.temp_var()
        as ...` construct.

        INPUT:

        - ``n`` -- (optional) positive integer; number of symbolic variables

        - ``domain`` -- (optional) specify the domain of the variable(s);

        EXAMPLES:

        Simple definition of a functional derivative::

            sage: def functional_derivative(expr, f, x):
            ....:     with SR.temp_var() as a:
            ....:         return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a)

        Contrast this to a similar implementation using SR.var(),
        which gives a wrong result in our example::

            sage: def functional_derivative(expr, f, x):
            ....:     a = SR.var('a')
            ....:     return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a) + 1

        TESTS:

            sage: x = SR.temp_var()
            sage: y = SR.temp_var()
            sage: bool(x == x)
            True
            sage: bool(x == y)
            False
            sage: bool(x.parent()(x._maxima_()) == x)
            True"""
    @overload
    def temp_var(self) -> Any:
        """SymbolicRing.temp_var(self, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 664)

        Return one or multiple new unique symbolic variables as an element
        of the symbolic ring. Use this instead of SR.var() if there is a
        possibility of name clashes occuring. Call SR.cleanup_var() once
        the variables are no longer needed or use a `with SR.temp_var()
        as ...` construct.

        INPUT:

        - ``n`` -- (optional) positive integer; number of symbolic variables

        - ``domain`` -- (optional) specify the domain of the variable(s);

        EXAMPLES:

        Simple definition of a functional derivative::

            sage: def functional_derivative(expr, f, x):
            ....:     with SR.temp_var() as a:
            ....:         return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a)

        Contrast this to a similar implementation using SR.var(),
        which gives a wrong result in our example::

            sage: def functional_derivative(expr, f, x):
            ....:     a = SR.var('a')
            ....:     return expr.subs({f(x):a}).diff(a).subs({a:f(x)})
            sage: f = function('f')
            sage: a = var('a')
            sage: functional_derivative(f(a)^2+a,f,a)
            2*f(a) + 1

        TESTS:

            sage: x = SR.temp_var()
            sage: y = SR.temp_var()
            sage: bool(x == x)
            True
            sage: bool(x == y)
            False
            sage: bool(x.parent()(x._maxima_()) == x)
            True"""
    @overload
    def var(self, name, latex_name=..., n=..., domain=...) -> Any:
        '''SymbolicRing.var(self, name, latex_name=None, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 752)

        Return a symbolic variable as an element of the symbolic ring.

        INPUT:

        - ``name`` -- string or list of strings with the name(s) of the symbolic variable(s)

        - ``latex_name`` -- (optional) string used when printing in latex mode, if not specified use ``\'name\'``

        - ``n`` -- (optional) positive integer; number of symbolic variables, indexed from `0` to `n-1`

        - ``domain`` -- (optional) specify the domain of the variable(s); it is None
          by default, and possible options are (non-exhaustive list, see note below):
          ``\'real\'``, ``\'complex\'``, ``\'positive\'``, ``\'integer\'`` and ``\'noninteger\'``

        OUTPUT: symbolic expression or tuple of symbolic expressions

        .. SEEALSO::

            This function does not inject the variable(s) into the global namespace.
            For that purpose see :meth:`var()<sage.calculus.var.var>`.

        .. NOTE::

            For a comprehensive list of acceptable features type ``\'maxima(\'features\')\'``,
            and see also the documentation of :ref:`sage.symbolic.assumptions`.

        EXAMPLES:

        Create a variable `zz`::

            sage: zz = SR.var(\'zz\'); zz
            zz

        The return type is a symbolic expression::

            sage: type(zz)
            <class \'sage.symbolic.expression.Expression\'>

        We can specify the domain as well::

            sage: zz = SR.var(\'zz\', domain=\'real\')
            sage: zz.is_real()
            True

        The real domain is also set with the integer domain::

            sage: SR.var(\'x\', domain=\'integer\').is_real()
            True

        The ``name`` argument does not have to match the left-hand side variable::

            sage: t = SR.var(\'theta2\'); t
            theta2

        Automatic indexing is available as well::

            sage: x = SR.var(\'x\', 4)
            sage: x[0], x[3]
            (x0, x3)
            sage: sum(x)
            x0 + x1 + x2 + x3

        TESTS::

            sage: var(\' x y  z    \')
            (x, y, z)
            sage: var(\' x  ,  y ,  z    \')
            (x, y, z)
            sage: var(\' \')
            Traceback (most recent call last):
            ...
            ValueError: You need to specify the name of the new variable.

            var([\'x\', \'y \', \' z \'])
            (x, y, z)
            var([\'x,y\'])
            Traceback (most recent call last):
            ...
            ValueError: The name "x,y" is not a valid Python identifier.

        Check that :issue:`17206` is fixed::

            sage: var1 = var(\'var1\', latex_name=r\'\\sigma^2_1\'); latex(var1)
            {\\sigma^2_1}

        The number of variables should be an integer greater or equal than 1::

            sage: SR.var(\'K\', -273)
            Traceback (most recent call last):
            ...
            ValueError: the number of variables should be a positive integer

        The argument ``n`` can only handle a single variable::

            sage: SR.var(\'x y\', 4)
            Traceback (most recent call last):
            ...
            ValueError: cannot specify n for multiple symbol names

        Check that :issue:`28353` is fixed: Constructions that suggest multiple
        variables but actually only give one variable name return a 1-tuple::

            sage: SR.var([\'x\'])
            (x,)
            sage: SR.var(\'x,\')
            (x,)
            sage: SR.var([\'x\'], n=4)
            Traceback (most recent call last):
            ...
            ValueError: cannot specify n for multiple symbol names'''
    @overload
    def var(self) -> Any:
        '''SymbolicRing.var(self, name, latex_name=None, n=None, domain=None)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 752)

        Return a symbolic variable as an element of the symbolic ring.

        INPUT:

        - ``name`` -- string or list of strings with the name(s) of the symbolic variable(s)

        - ``latex_name`` -- (optional) string used when printing in latex mode, if not specified use ``\'name\'``

        - ``n`` -- (optional) positive integer; number of symbolic variables, indexed from `0` to `n-1`

        - ``domain`` -- (optional) specify the domain of the variable(s); it is None
          by default, and possible options are (non-exhaustive list, see note below):
          ``\'real\'``, ``\'complex\'``, ``\'positive\'``, ``\'integer\'`` and ``\'noninteger\'``

        OUTPUT: symbolic expression or tuple of symbolic expressions

        .. SEEALSO::

            This function does not inject the variable(s) into the global namespace.
            For that purpose see :meth:`var()<sage.calculus.var.var>`.

        .. NOTE::

            For a comprehensive list of acceptable features type ``\'maxima(\'features\')\'``,
            and see also the documentation of :ref:`sage.symbolic.assumptions`.

        EXAMPLES:

        Create a variable `zz`::

            sage: zz = SR.var(\'zz\'); zz
            zz

        The return type is a symbolic expression::

            sage: type(zz)
            <class \'sage.symbolic.expression.Expression\'>

        We can specify the domain as well::

            sage: zz = SR.var(\'zz\', domain=\'real\')
            sage: zz.is_real()
            True

        The real domain is also set with the integer domain::

            sage: SR.var(\'x\', domain=\'integer\').is_real()
            True

        The ``name`` argument does not have to match the left-hand side variable::

            sage: t = SR.var(\'theta2\'); t
            theta2

        Automatic indexing is available as well::

            sage: x = SR.var(\'x\', 4)
            sage: x[0], x[3]
            (x0, x3)
            sage: sum(x)
            x0 + x1 + x2 + x3

        TESTS::

            sage: var(\' x y  z    \')
            (x, y, z)
            sage: var(\' x  ,  y ,  z    \')
            (x, y, z)
            sage: var(\' \')
            Traceback (most recent call last):
            ...
            ValueError: You need to specify the name of the new variable.

            var([\'x\', \'y \', \' z \'])
            (x, y, z)
            var([\'x,y\'])
            Traceback (most recent call last):
            ...
            ValueError: The name "x,y" is not a valid Python identifier.

        Check that :issue:`17206` is fixed::

            sage: var1 = var(\'var1\', latex_name=r\'\\sigma^2_1\'); latex(var1)
            {\\sigma^2_1}

        The number of variables should be an integer greater or equal than 1::

            sage: SR.var(\'K\', -273)
            Traceback (most recent call last):
            ...
            ValueError: the number of variables should be a positive integer

        The argument ``n`` can only handle a single variable::

            sage: SR.var(\'x y\', 4)
            Traceback (most recent call last):
            ...
            ValueError: cannot specify n for multiple symbol names

        Check that :issue:`28353` is fixed: Constructions that suggest multiple
        variables but actually only give one variable name return a 1-tuple::

            sage: SR.var([\'x\'])
            (x,)
            sage: SR.var(\'x,\')
            (x,)
            sage: SR.var([\'x\'], n=4)
            Traceback (most recent call last):
            ...
            ValueError: cannot specify n for multiple symbol names'''
    def wild(self, unsignedintn=...) -> Any:
        """SymbolicRing.wild(self, unsigned int n=0)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 442)

        Return the n-th wild-card for pattern matching and substitution.

        INPUT:

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

        TESTS:

        Check that :issue:`15047` is fixed::

            sage: latex(SR.wild(0))
            \\$0

        Check that :issue:`21455` is fixed::

            sage: coth(SR.wild(0))
            coth($0)"""
    def __contains__(self, x) -> Any:
        """SymbolicRing.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 479)

        ``True`` if there is an element of the symbolic ring that is equal to x
        under ``==``.

        EXAMPLES:

        The symbolic variable x is in the symbolic ring.::

            sage: x.parent()
            Symbolic Ring
            sage: x in SR
            True

        2 is also in the symbolic ring since it is equal to something in
        SR, even though 2's parent is not SR.

        ::

            sage: 2 in SR
            True
            sage: parent(2)
            Integer Ring
            sage: 1/3 in SR
            True"""
    def __reduce__(self) -> Any:
        """SymbolicRing.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 96)

        EXAMPLES::

           sage: loads(dumps(SR)) == SR           # indirect doctest
           True"""

class TemporaryVariables(tuple):
    """File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1377)

        Instances of this class can be used with Python `with` to
        automatically clean up after themselves.
    """
    def __enter__(self) -> Any:
        """TemporaryVariables.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1382)"""
    def __exit__(self, *args) -> Any:
        """TemporaryVariables.__exit__(self, *args)

        File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1385)

        TESTS::

            sage: symbols_copy = SR.symbols.copy()
            sage: with SR.temp_var(n=2) as temp_vars: pass
            sage: symbols_copy == SR.symbols
            True"""

class UnderscoreSageMorphism(sage.categories.morphism.Morphism):
    """UnderscoreSageMorphism(t, R)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, t, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/symbolic/ring.pyx (starting at line 1247)

                A Morphism which constructs Expressions from an arbitrary Python
                object by calling the :meth:`_sage_` method on the object.

                EXAMPLES::

                    sage: # needs sympy
                    sage: import sympy
                    sage: from sage.symbolic.ring import UnderscoreSageMorphism
                    sage: b = sympy.var('b')
                    sage: f = UnderscoreSageMorphism(type(b), SR)
                    sage: f(b)
                    b
                    sage: _.parent()
                    Symbolic Ring
        """

SR = SymbolicRing()