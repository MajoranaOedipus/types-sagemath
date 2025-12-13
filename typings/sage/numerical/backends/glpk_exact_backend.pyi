import sage.numerical.backends.glpk_backend
from typing import Any, ClassVar, overload

class GLPKExactBackend(sage.numerical.backends.glpk_backend.GLPKBackend):
    """File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 17)

        MIP Backend that runs the GLPK solver in exact rational simplex mode.

        The only access to data is via double-precision floats, which
        means that rationals in the input data may be rounded before
        the exact solver sees them. Thus, it is unreasonable to expect
        that arbitrary LPs with rational coefficients are solved exactly.
        Once the LP has been read into the backend, it reconstructs
        rationals from doubles and does solve exactly over the rationals,
        but results are returned as as doubles.

        There is no support for integer variables.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def add_variable(self, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., name=...) -> int:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self, lower_bound=...) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self, continuous=...) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self, name=..., obj=...) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self, integer=...) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    @overload
    def add_variable(self, binary=...) -> Any:
        '''GLPKExactBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 43)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name=\'x\',obj=1.0)
            4
            sage: p.objective_coefficient(4)
            1.0

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            ValueError: GLPK/exact only supports continuous variables'''
    def add_variables(self, intnumber, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., names=...) -> int:
        '''GLPKExactBackend.add_variables(self, int number, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, names=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 109)

        Add ``number`` variables.

        This amounts to adding new columns to the matrix. By default,
        the variables are both nonnegative and real.

        In this backend, variables are always continuous (real).
        If integer variables are requested via the parameters
        ``binary`` and ``integer``, an error will be raised.

        INPUT:

        - ``n`` -- the number of new variables (must be > 0)

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is binary (default: ``True``)

        - ``integer`` -- ``True`` if the variable is binary (default: ``False``)

        - ``obj`` -- coefficient of all variables in the objective function (default: 0.0)

        - ``names`` -- list of names (default: ``None``)

        OUTPUT: the index of the variable created last

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.ncols()
            0
            sage: p.add_variables(5)
            4
            sage: p.ncols()
            5
            sage: p.add_variables(2, lower_bound=-2.0, obj=42.0, names=[\'a\',\'b\'])
            6'''
    def set_variable_type(self, intvariable, intvtype) -> Any:
        '''GLPKExactBackend.set_variable_type(self, int variable, int vtype)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_exact_backend.pyx (starting at line 158)

        Set the type of a variable.

        In this backend, variables are always continuous (real).
        If integer or binary variables are requested via the parameter
        ``vtype``, an error will be raised.

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``vtype`` -- integer:

            *  1  Integer
            *  0  Binary
            * -1 Real

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK/exact")
            sage: p.add_variables(5)
            4
            sage: p.set_variable_type(3, -1)
            sage: p.set_variable_type(3, -2)
            Traceback (most recent call last):
            ...
            ValueError: ...'''
