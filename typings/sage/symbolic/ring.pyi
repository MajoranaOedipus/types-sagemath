"""
The symbolic ring
"""

from typing import Annotated, Any, Literal, Self, SupportsIndex, SupportsInt, overload
from collections.abc import Callable
from sage.rings.ring import Ring
from sage.rings.integer import Integer
from sage.rings.abc import SymbolicRing as SymbolicRingABC
from sage.symbolic.subring import SymbolicSubringFactory
from sage.categories.morphism import Morphism
from numpy import (
    integer as NumPyInteger, 
    floating as NumPyFloating, 
    complexfloating as NumPyComplexFloating
)

type _NotUsed = object
type _Domain = Literal["real", "complex", "positive", "integer", "noninteger"]

import sage as sage
from sage.symbolic.expression import Expression as Expression
from sage.categories.category import ZZ as ZZ
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

KEYWORDS: set[str]

# It has the category of `CommutativeRings`, but not included in `__mro__`?
class SymbolicRing(SymbolicRingABC):
    """
    Symbolic Ring, parent object for all symbolic expressions."""
    
    symbols: dict
    
    def __init__(self, base_ring: Ring = SR):
        """
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
    def I(self) -> Expression[Self]:
        """
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
    
    type _Zero = Annotated[Integer, Integer(0)]
    def characteristic(self) -> _Zero:
        """
        Return the characteristic of the symbolic ring, which is 0.

        OUTPUT: a Sage integer

        EXAMPLES::

            sage: c = SR.characteristic(); c
            0
            sage: type(c)
            <class 'sage.rings.integer.Integer'>"""
    def cleanup_var(self, symbol: Expression | list[Expression] | tuple[Expression, ...]
        ) -> None:
        """
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
    def is_exact(self) -> Literal[False]:
        """
        Return ``False``, because there are approximate elements in the
        symbolic ring.

        EXAMPLES::

            sage: SR.is_exact()
            False

        Here is an inexact element.

        ::

            sage: SR(1.9393)
            1.93930000000000"""
    def is_field(self, proof: _NotUsed = True) -> Literal[True]:
        """
        Return ``True``, since the symbolic expression ring is (for the most
        part) a field.

        EXAMPLES::

            sage: SR.is_field()
            True"""
    def is_finite(self) -> Literal[False]:
        """
        Return ``False``, since the Symbolic Ring is infinite.

        EXAMPLES::

            sage: SR.is_finite()
            False"""
    def pi(self) -> Expression[Self]:
        """
        EXAMPLES::

            sage: SR.pi() is pi
            True"""
    # TODO: follows sage.symbolic.subring.SymbolicSubring's argument convention
    def subring(self, *args, **kwds) -> SymbolicSubringFactory:
        """
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
    def symbol(
        self, 
        name: str | None = None, 
        latex_name: str | None = None, 
        domain: str | None= None
    ) -> Expression[Self]:
        """
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
            My Symbolic Ring"""
    def temp_var(
        self, n: SupportsIndex | None = None, domain: str | None =None
    ) -> Expression[Self] | TemporaryVariables[Expression[Self]]:
        """
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
    def var[Expr: Expression](self, name: Expr) -> Expr: ...
    @overload
    def var(
        self, 
        name: object, 
        n: SupportsIndex, 
        domain: _Domain  | None = None
    ) -> tuple[Expression[Self]]: ...
    @overload
    def var(
        self, 
        name: object, 
        latex_name: str | None = None, 
        domain: _Domain | None = None
    ) -> Expression[Self] | tuple[Expression[Self]]:
        """
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
            ValueError: cannot specify n for multiple symbol names"""
    
    type _uint = SupportsInt
    def wild(self, n: _uint = 0) -> Expression[SymbolicRing]:
        """
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
    def __contains__(self, x: object) -> bool:
        """
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
    def __reduce__(self) -> tuple[Callable[[], SymbolicRing], tuple[()]]:
        """
        EXAMPLES::

           sage: loads(dumps(SR)) == SR           # indirect doctest
           True"""

SR: SymbolicRing

class NumpyToSRMorphism(Morphism):
    """
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
        -0.4161468365471424"""
    
    def __init__(self, numpy_type: type[NumPyInteger | NumPyFloating | NumPyComplexFloating]):
        """
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

class UnderscoreSageMorphism(Morphism):
    def __init__(self, t: type, R):
        """
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

def the_SymbolicRing() -> SymbolicRing:
    """
    Return the unique symbolic ring object.

    (This is mainly used for unpickling.)

    EXAMPLES::

        sage: sage.symbolic.ring.the_SymbolicRing()
        Symbolic Ring
        sage: sage.symbolic.ring.the_SymbolicRing() is sage.symbolic.ring.the_SymbolicRing()
        True
        sage: sage.symbolic.ring.the_SymbolicRing() is SR
        True
    """

def var(name, **kwds):
    """
    EXAMPLES::

        sage: from sage.symbolic.ring import var
        sage: var("x y z")
        (x, y, z)
        sage: var("x,y,z")
        (x, y, z)
        sage: var("x , y , z")
        (x, y, z)
        sage: var("z")
        z

    TESTS:

    These examples test that variables can only be made from valid
    identifiers.  See :issue:`7496` (and :issue:`9724`) for details::

        sage: var(' ')
        Traceback (most recent call last):
        ...
        ValueError: You need to specify the name of the new variable.
        sage: var('3')
        Traceback (most recent call last):
        ...
        ValueError: The name "3" is not a valid Python identifier.
    """

def isidentifier(x: str) -> bool:
    """
    Return whether ``x`` is a valid identifier.

    INPUT:

    - ``x`` -- string

    OUTPUT: boolean; whether the string ``x`` can be used as a variable name

    This function should return ``False`` for keywords, so we can not
    just use the ``isidentifier`` method of strings,
    because, for example, it returns ``True`` for "def" and for "None".

    EXAMPLES::

        sage: from sage.symbolic.ring import isidentifier
        sage: isidentifier('x')
        True
        sage: isidentifier(' x')   # can't start with space
        False
        sage: isidentifier('ceci_n_est_pas_une_pipe')
        True
        sage: isidentifier('1 + x')
        False
        sage: isidentifier('2good')
        False
        sage: isidentifier('good2')
        True
        sage: isidentifier('lambda s:s+1')
        False
        sage: isidentifier('None')
        False
        sage: isidentifier('lambda')
        False
        sage: isidentifier('def')
        False
    """

class TemporaryVariables[Var: Expression](tuple[Var, ...]):
    """
        Instances of this class can be used with Python `with` to
        automatically clean up after themselves.
    """
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: _NotUsed) -> Literal[False]:
        """
        TESTS::

            sage: symbols_copy = SR.symbols.copy()
            sage: with SR.temp_var(n=2) as temp_vars: pass
            sage: symbols_copy == SR.symbols
            True"""
