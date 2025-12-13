import _cython_3_2_1
import sage.misc.cachefunc
import sage.structure.element
import sage.structure.parent
from sage.misc.cachefunc import cached_function as cached_function
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

LinearConstraintsParent: sage.misc.cachefunc.CachedFunction
LinearFunctionsParent: sage.misc.cachefunc.CachedFunction
__pyx_capi__: dict
is_LinearConstraint: _cython_3_2_1.cython_function_or_method
is_LinearFunction: _cython_3_2_1.cython_function_or_method

class LinearConstraint(LinearFunctionOrConstraint):
    """LinearConstraint(parent, terms, equality=False)

    File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1359)

    A class to represent formal Linear Constraints.

    A Linear Constraint being an inequality between
    two linear functions, this class lets the user
    write ``LinearFunction1 <= LinearFunction2``
    to define the corresponding constraint, which
    can potentially involve several layers of such
    inequalities (``A <= B <= C``), or even equalities
    like ``A == B == C``.

    Trivial constraints (meaning that they have only one term and no
    relation) are also allowed. They are required for the coercion
    system to work.

    .. warning::

        This class has no reason to be instantiated by the user, and
        is meant to be used by instances of
        :class:`MixedIntegerLinearProgram`.

    INPUT:

    - ``parent`` -- the parent; a :class:`LinearConstraintsParent_class`

    - ``terms`` -- list/tuple/iterable of two or more linear
      functions (or things that can be converted into linear
      functions)

    - ``equality`` -- boolean (default: ``False``); whether the terms
      are the entries of a chained less-or-equal (``<=``) inequality
      or a chained equality

    EXAMPLES::

        sage: p = MixedIntegerLinearProgram()
        sage: b = p.new_variable()
        sage: b[2]+2*b[3] <= b[8]-5
        x_0 + 2*x_1 <= -5 + x_2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, terms, equality=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1401)

                Constructor for ``LinearConstraint``.

                INPUT:

                See :class:`LinearConstraint`.

                EXAMPLES::

                    sage: p = MixedIntegerLinearProgram()
                    sage: b = p.new_variable()
                    sage: b[2]+2*b[3] <= b[8]-5
                    x_0 + 2*x_1 <= -5 + x_2
        """
    def equals(self, left, LinearConstraintright) -> Any:
        """LinearConstraint.equals(left, LinearConstraint right)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1422)

        Compare ``left`` and ``right``.

        OUTPUT:

        boolean; whether all terms of ``left`` and ``right`` are
        equal. Note that this is stronger than mathematical
        equivalence of the relations.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: (x[1] + 1 >= 2).equals(3/3 + 1*x[1] + 0*x[2] >= 8/4)
            True
            sage: (x[1] + 1 >= 2).equals(x[1] + 1-1 >= 1-1)
            False"""
    @overload
    def equations(self) -> Any:
        """LinearConstraint.equations(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1535)

        Iterate over the unchained(!) equations.

        OUTPUT:

        An iterator over pairs ``(lhs, rhs)`` such that the individual
        equations are ``lhs == rhs``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: eqns = 1 == b[0] == b[2] == 3 == b[3];  eqns
            1 == x_0 == x_1 == 3 == x_2
            sage: for lhs, rhs in eqns.equations():
            ....:     print(str(lhs) + ' == ' + str(rhs))
            1 == x_0
            x_0 == x_1
            x_1 == 3
            3 == x_2"""
    @overload
    def equations(self) -> Any:
        """LinearConstraint.equations(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1535)

        Iterate over the unchained(!) equations.

        OUTPUT:

        An iterator over pairs ``(lhs, rhs)`` such that the individual
        equations are ``lhs == rhs``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: eqns = 1 == b[0] == b[2] == 3 == b[3];  eqns
            1 == x_0 == x_1 == 3 == x_2
            sage: for lhs, rhs in eqns.equations():
            ....:     print(str(lhs) + ' == ' + str(rhs))
            1 == x_0
            x_0 == x_1
            x_1 == 3
            3 == x_2"""
    @overload
    def inequalities(self) -> Any:
        """LinearConstraint.inequalities(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1570)

        Iterate over the unchained(!) inequalities.

        OUTPUT:

        An iterator over pairs ``(lhs, rhs)`` such that the individual
        equations are ``lhs <= rhs``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: ieq = 1 <= b[0] <= b[2] <= 3 <= b[3]; ieq
            1 <= x_0 <= x_1 <= 3 <= x_2

            sage: for lhs, rhs in ieq.inequalities():
            ....:     print(str(lhs) + ' <= ' + str(rhs))
            1 <= x_0
            x_0 <= x_1
            x_1 <= 3
            3 <= x_2"""
    @overload
    def inequalities(self) -> Any:
        """LinearConstraint.inequalities(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1570)

        Iterate over the unchained(!) inequalities.

        OUTPUT:

        An iterator over pairs ``(lhs, rhs)`` such that the individual
        equations are ``lhs <= rhs``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: ieq = 1 <= b[0] <= b[2] <= 3 <= b[3]; ieq
            1 <= x_0 <= x_1 <= 3 <= x_2

            sage: for lhs, rhs in ieq.inequalities():
            ....:     print(str(lhs) + ' <= ' + str(rhs))
            1 <= x_0
            x_0 <= x_1
            x_1 <= 3
            3 <= x_2"""
    @overload
    def is_equation(self) -> Any:
        """LinearConstraint.is_equation(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1453)

        Whether the constraint is a chained equation.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: (b[0] == b[1]).is_equation()
            True
            sage: (b[0] <= b[1]).is_equation()
            False"""
    @overload
    def is_equation(self) -> Any:
        """LinearConstraint.is_equation(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1453)

        Whether the constraint is a chained equation.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: (b[0] == b[1]).is_equation()
            True
            sage: (b[0] <= b[1]).is_equation()
            False"""
    @overload
    def is_equation(self) -> Any:
        """LinearConstraint.is_equation(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1453)

        Whether the constraint is a chained equation.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: (b[0] == b[1]).is_equation()
            True
            sage: (b[0] <= b[1]).is_equation()
            False"""
    @overload
    def is_less_or_equal(self) -> Any:
        """LinearConstraint.is_less_or_equal(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1470)

        Whether the constraint is a chained less-or_equal inequality.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: (b[0] == b[1]).is_less_or_equal()
            False
            sage: (b[0] <= b[1]).is_less_or_equal()
            True"""
    @overload
    def is_less_or_equal(self) -> Any:
        """LinearConstraint.is_less_or_equal(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1470)

        Whether the constraint is a chained less-or_equal inequality.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: (b[0] == b[1]).is_less_or_equal()
            False
            sage: (b[0] <= b[1]).is_less_or_equal()
            True"""
    @overload
    def is_less_or_equal(self) -> Any:
        """LinearConstraint.is_less_or_equal(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1470)

        Whether the constraint is a chained less-or_equal inequality.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: (b[0] == b[1]).is_less_or_equal()
            False
            sage: (b[0] <= b[1]).is_less_or_equal()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """LinearConstraint.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1487)

        Test whether the constraint is trivial.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: LC = p.linear_constraints_parent()
            sage: ieq = LC(1,2);  ieq
            1 <= 2
            sage: ieq.is_trivial()
            False

            sage: ieq = LC(1);  ieq
            trivial constraint starting with 1
            sage: ieq.is_trivial()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """LinearConstraint.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1487)

        Test whether the constraint is trivial.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: LC = p.linear_constraints_parent()
            sage: ieq = LC(1,2);  ieq
            1 <= 2
            sage: ieq.is_trivial()
            False

            sage: ieq = LC(1);  ieq
            trivial constraint starting with 1
            sage: ieq.is_trivial()
            True"""
    @overload
    def is_trivial(self) -> Any:
        """LinearConstraint.is_trivial(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1487)

        Test whether the constraint is trivial.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: LC = p.linear_constraints_parent()
            sage: ieq = LC(1,2);  ieq
            1 <= 2
            sage: ieq.is_trivial()
            False

            sage: ieq = LC(1);  ieq
            trivial constraint starting with 1
            sage: ieq.is_trivial()
            True"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __iter__(self) -> Any:
        """LinearConstraint.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1507)

        Iterate over the terms of the chained (in)-equality.

        OUTPUT:

        A generator yielding the individual terms of the constraint in
        left-to-right order.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: b = p.new_variable()
            sage: ieq = 1 <= b[0] <= b[2] <= 3 <= b[3];  ieq
            1 <= x_0 <= x_1 <= 3 <= x_2
            sage: list(ieq)
            [1, x_0, x_1, 3, x_2]
            sage: for term in ieq:
            ....:     print(term)
            1
            x_0
            x_1
            3
            x_2"""

class LinearConstraintsParent_class(sage.structure.parent.Parent):
    """LinearConstraintsParent_class(linear_functions_parent)

    File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1172)

    Parent for :class:`LinearConstraint`.

    .. warning::

        This class has no reason to be instantiated by the user, and
        is meant to be used by instances of
        :class:`MixedIntegerLinearProgram`. Also, use the
        :func:`LinearConstraintsParent` factory function.

    INPUT/OUTPUT: see :func:`LinearFunctionsParent`

    EXAMPLES::

        sage: p = MixedIntegerLinearProgram()
        sage: LC = p.linear_constraints_parent();  LC
        Linear constraints over Real Double Field
        sage: from sage.numerical.linear_functions import LinearConstraintsParent
        sage: LinearConstraintsParent(p.linear_functions_parent()) is LC
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, linear_functions_parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1214)

                The Python constructor.

                INPUT/OUTPUT: see :func:`LinearFunctionsParent`

                TESTS::

                    sage: from sage.numerical.linear_functions import LinearFunctionsParent
                    sage: LF = LinearFunctionsParent(RDF)
                    sage: from sage.numerical.linear_functions import LinearConstraintsParent
                    sage: LinearConstraintsParent(LF)
                    Linear constraints over Real Double Field
                    sage: LinearConstraintsParent(None)
                    Traceback (most recent call last):
                    ...
                    TypeError: Cannot convert NoneType to sage.numerical.linear_functions.LinearFunctionsParent_class
        """
    @overload
    def linear_functions_parent(self) -> Any:
        """LinearConstraintsParent_class.linear_functions_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1234)

        Return the parent for the linear functions.

        EXAMPLES::

            sage: LC = MixedIntegerLinearProgram().linear_constraints_parent()
            sage: LC.linear_functions_parent()
            Linear functions over Real Double Field"""
    @overload
    def linear_functions_parent(self) -> Any:
        """LinearConstraintsParent_class.linear_functions_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1234)

        Return the parent for the linear functions.

        EXAMPLES::

            sage: LC = MixedIntegerLinearProgram().linear_constraints_parent()
            sage: LC.linear_functions_parent()
            Linear functions over Real Double Field"""

class LinearFunction(LinearFunctionOrConstraint):
    """LinearFunction(parent, f)

    File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 746)

    An elementary algebra to represent symbolic linear functions.

    .. warning::

        You should never instantiate :class:`LinearFunction`
        manually. Use the element constructor in the parent
        instead.

    EXAMPLES:

    For example, do this::

        sage: p = MixedIntegerLinearProgram()
        sage: parent = p.linear_functions_parent()
        sage: parent({0 : 1, 3 : -8})
        x_0 - 8*x_3

    instead of this::

        sage: from sage.numerical.linear_functions import LinearFunction
        sage: LinearFunction(p.linear_functions_parent(), {0 : 1, 3 : -8})
        x_0 - 8*x_3"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 772)

                Constructor taking a dictionary or a numerical value as its argument.

                A linear function is represented as a dictionary. The
                values are the coefficient of the variable represented
                by the keys ( which are integers ). The key ``-1``
                corresponds to the constant term.

                EXAMPLES:

                With a dictionary::

                    sage: p = MixedIntegerLinearProgram()
                    sage: LF = p.linear_functions_parent()
                    sage: LF({0 : 1, 3 : -8})
                    x_0 - 8*x_3

                Using the constructor with a numerical value::

                    sage: p = MixedIntegerLinearProgram()
                    sage: LF = p.linear_functions_parent()
                    sage: LF(25)
                    25
        """
    def coefficient(self, x) -> Any:
        """LinearFunction.coefficient(self, x)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 848)

        Return one of the coefficients.

        INPUT:

        - ``x`` -- a linear variable or an integer; if an integer `i`
          is passed, then `x_i` is used as linear variable

        OUTPUT:

        A base ring element. The coefficient of ``x`` in the linear
        function. Pass ``-1`` for the constant term.

        EXAMPLES::

            sage: mip.<b> = MixedIntegerLinearProgram()
            sage: lf = -8 * b[3] + b[0] - 5;  lf
            -5 - 8*x_0 + x_1
            sage: lf.coefficient(b[3])
            -8.0
            sage: lf.coefficient(0)      # x_0 is b[3]
            -8.0
            sage: lf.coefficient(4)
            0.0
            sage: lf.coefficient(-1)
            -5.0

        TESTS::

            sage: lf.coefficient(b[3] + b[4])
            Traceback (most recent call last):
            ...
            ValueError: x is a sum, must be a single variable
            sage: lf.coefficient(2*b[3])
            Traceback (most recent call last):
            ...
            ValueError: x must have a unit coefficient
            sage: mip.<q> = MixedIntegerLinearProgram(solver='ppl')
            sage: lf.coefficient(q[0])
            Traceback (most recent call last):
            ...
            ValueError: x is from a different linear functions module"""
    @overload
    def dict(self) -> Any:
        """LinearFunction.dict(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 827)

        Return the dictionary corresponding to the Linear Function.

        OUTPUT:

        The linear function is represented as a dictionary. The value
        are the coefficient of the variable represented by the keys (
        which are integers ). The key ``-1`` corresponds to the
        constant term.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: LF = p.linear_functions_parent()
            sage: lf = LF({0 : 1, 3 : -8})
            sage: lf.dict()
            {0: 1.0, 3: -8.0}"""
    @overload
    def dict(self) -> Any:
        """LinearFunction.dict(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 827)

        Return the dictionary corresponding to the Linear Function.

        OUTPUT:

        The linear function is represented as a dictionary. The value
        are the coefficient of the variable represented by the keys (
        which are integers ). The key ``-1`` corresponds to the
        constant term.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: LF = p.linear_functions_parent()
            sage: lf = LF({0 : 1, 3 : -8})
            sage: lf.dict()
            {0: 1.0, 3: -8.0}"""
    def equals(self, left, LinearFunctionright) -> Any:
        """LinearFunction.equals(left, LinearFunction right)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1150)

        Logically compare ``left`` and ``right``.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: (x[1] + 1).equals(3/3 + 1*x[1] + 0*x[2])
            True"""
    @overload
    def is_zero(self) -> Any:
        """LinearFunction.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1132)

        Test whether ``self`` is zero.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: (x[1] - x[1] + 0*x[2]).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """LinearFunction.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 1132)

        Test whether ``self`` is zero.

        OUTPUT: boolean

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: (x[1] - x[1] + 0*x[2]).is_zero()
            True"""
    @overload
    def iteritems(self) -> Any:
        """LinearFunction.iteritems(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 804)

        Iterate over the index, coefficient pairs.

        OUTPUT:

        An iterator over the ``(key, coefficient)`` pairs. The keys
        are integers indexing the variables. The key ``-1``
        corresponds to the constant term.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver = 'ppl')
            sage: x = p.new_variable()
            sage: f = 0.5 + 3/2*x[1] + 0.6*x[3]
            sage: for id, coeff in sorted(f.iteritems()):
            ....:     print('id = {}   coeff = {}'.format(id, coeff))
            id = -1   coeff = 1/2
            id = 0   coeff = 3/2
            id = 1   coeff = 3/5"""
    @overload
    def iteritems(self) -> Any:
        """LinearFunction.iteritems(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 804)

        Iterate over the index, coefficient pairs.

        OUTPUT:

        An iterator over the ``(key, coefficient)`` pairs. The keys
        are integers indexing the variables. The key ``-1``
        corresponds to the constant term.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver = 'ppl')
            sage: x = p.new_variable()
            sage: f = 0.5 + 3/2*x[1] + 0.6*x[3]
            sage: for id, coeff in sorted(f.iteritems()):
            ....:     print('id = {}   coeff = {}'.format(id, coeff))
            id = -1   coeff = 1/2
            id = 0   coeff = 3/2
            id = 1   coeff = 3/5"""

class LinearFunctionOrConstraint(sage.structure.element.ModuleElement):
    """File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 247)

        Base class for :class:`LinearFunction` and :class:`LinearConstraint`.

        This class exists solely to implement chaining of inequalities
        in constraints.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """LinearFunctionOrConstraint.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 487)

        Return a hash from the ``id()``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: LF = p.linear_functions_parent()
            sage: f = LF({2 : 5, 3 : 2})
            sage: hash(f)  # indirect doctest; random
            103987752

        Since we hash by ``id()``, linear functions and constraints are
        only considered equal for sets and dicts if they are the same
        object::

            sage: f = LF.0
            sage: set([f, f])
            {x_0}
            sage: set([f, f+0])
            {x_0, x_0}
            sage: len(set([f, f+1]))
            2
            sage: d = {}
            sage: d[f] = 123
            sage: d[f+0] = 456
            sage: list(d)
            [x_0, x_0]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class LinearFunctionsParent_class(sage.structure.parent.Parent):
    """LinearFunctionsParent_class(base_ring)

    File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 525)

    The parent for all linear functions over a fixed base ring.

    .. warning::

        You should use :func:`LinearFunctionsParent` to construct
        instances of this class.

    INPUT/OUTPUT: see :func:`LinearFunctionsParent`

    EXAMPLES::

        sage: from sage.numerical.linear_functions import LinearFunctionsParent_class
        sage: LinearFunctionsParent_class
        <class 'sage.numerical.linear_functions.LinearFunctionsParent_class'>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base_ring) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 557)

                The Python constructor.

                TESTS::

                    sage: from sage.numerical.linear_functions import LinearFunctionsParent
                    sage: LinearFunctionsParent(RDF)
                    Linear functions over Real Double Field
        """
    def gen(self, i) -> Any:
        """LinearFunctionsParent_class.gen(self, i)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 640)

        Return the linear variable `x_i`.

        INPUT:

        - ``i`` -- nonnegative integer

        OUTPUT: the linear function `x_i`

        EXAMPLES::

            sage: LF = MixedIntegerLinearProgram().linear_functions_parent()
            sage: LF.gen(23)
            x_23"""
    @overload
    def set_multiplication_symbol(self, symbol=...) -> Any:
        """LinearFunctionsParent_class.set_multiplication_symbol(self, symbol='*')

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 570)

        Set the multiplication symbol when pretty-printing linear functions.

        INPUT:

        - ``symbol`` -- string (default: ``'*'``); the multiplication
          symbol to be used

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: f = -1-2*x[0]-3*x[1]
            sage: LF = f.parent()
            sage: LF._get_multiplication_symbol()
            '*'
            sage: f
            -1 - 2*x_0 - 3*x_1
            sage: LF.set_multiplication_symbol(' ')
            sage: f
            -1 - 2 x_0 - 3 x_1
            sage: LF.set_multiplication_symbol()
            sage: f
            -1 - 2*x_0 - 3*x_1"""
    @overload
    def set_multiplication_symbol(self) -> Any:
        """LinearFunctionsParent_class.set_multiplication_symbol(self, symbol='*')

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 570)

        Set the multiplication symbol when pretty-printing linear functions.

        INPUT:

        - ``symbol`` -- string (default: ``'*'``); the multiplication
          symbol to be used

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: f = -1-2*x[0]-3*x[1]
            sage: LF = f.parent()
            sage: LF._get_multiplication_symbol()
            '*'
            sage: f
            -1 - 2*x_0 - 3*x_1
            sage: LF.set_multiplication_symbol(' ')
            sage: f
            -1 - 2 x_0 - 3 x_1
            sage: LF.set_multiplication_symbol()
            sage: f
            -1 - 2*x_0 - 3*x_1"""
    def tensor(self, free_module) -> Any:
        """LinearFunctionsParent_class.tensor(self, free_module)

        File: /build/sagemath/src/sage/src/sage/numerical/linear_functions.pyx (starting at line 612)

        Return the tensor product with ``free_module``.

        INPUT:

        - ``free_module`` -- vector space or matrix space over the
          same base ring

        OUTPUT:

        Instance of
        :class:`sage.numerical.linear_tensor.LinearTensorParent_class`.

        EXAMPLES::

            sage: LF = MixedIntegerLinearProgram().linear_functions_parent()
            sage: LF.tensor(RDF^3)
            Tensor product of Vector space of dimension 3 over Real Double Field
            and Linear functions over Real Double Field
            sage: LF.tensor(QQ^2)
            Traceback (most recent call last):
            ...
            ValueError: base rings must match"""
