from _typeshed import Incomplete
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import column_matrix as column_matrix, identity_matrix as identity_matrix, random_matrix as random_matrix
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.html import HtmlFragment as HtmlFragment
from sage.misc.latex import LatexExpr as LatexExpr, latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc import get_main_globals as get_main_globals
from sage.misc.prandom import randint as randint, random as random
from sage.modules.free_module_element import random_vector as random_vector
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.structure.all import SageObject as SageObject

generate_real_LaTeX: bool

@cached_function
def variable(R, v):
    '''
    Interpret ``v`` as a variable of ``R``.

    INPUT:

    - ``R`` -- a polynomial ring

    - ``v`` -- a variable of ``R`` or convertible into ``R``, a string
      with the name of a variable of ``R`` or an index of a variable in ``R``

    OUTPUT: a variable of ``R``

    EXAMPLES::

        sage: from sage.numerical.interactive_simplex_method \\\n        ....:     import variable
        sage: R = PolynomialRing(QQ, "x3, y5, x5, y")
        sage: R.inject_variables()
        Defining x3, y5, x5, y
        sage: variable(R, "x3")
        x3
        sage: variable(R, x3)
        x3
        sage: variable(R, 3)
        x3
        sage: variable(R, 0)
        Traceback (most recent call last):
        ...
        ValueError: there is no variable with the given index
        sage: variable(R, 5)
        Traceback (most recent call last):
        ...
        ValueError: the given index is ambiguous
        sage: variable(R, 2 * x3)
        Traceback (most recent call last):
        ...
        ValueError: cannot interpret given data as a variable
        sage: variable(R, "z")
        Traceback (most recent call last):
        ...
        ValueError: cannot interpret given data as a variable
    '''

available_styles: Incomplete
current_style: str

def default_variable_name(variable):
    '''
    Return default variable name for the current :func:`style`.

    INPUT:

    - ``variable`` -- string describing requested name

    OUTPUT: string with the requested name for current style

    EXAMPLES::

        sage: sage.numerical.interactive_simplex_method.default_variable_name("primal slack")
        \'x\'
        sage: sage.numerical.interactive_simplex_method.style(\'Vanderbei\')
        \'Vanderbei\'
        sage: sage.numerical.interactive_simplex_method.default_variable_name("primal slack")
        \'w\'
        sage: sage.numerical.interactive_simplex_method.style(\'UAlberta\')
        \'UAlberta\'
    '''
def style(new_style=None):
    """
    Set or get the current style of problems and dictionaries.

    INPUT:

    - ``new_style`` -- string or ``None`` (default)

    OUTPUT:

    - a string with current style (same as ``new_style`` if it was given)

    If the input is not recognized as a valid style, a :exc:`ValueError` exception
    is raised.

    Currently supported styles are:

    - 'UAlberta' (default):  Follows the style used in the Math 373 course
      on Mathematical Programming and Optimization at the University of
      Alberta, Edmonton, Canada; based on Chvatal's book.

      - Objective functions of dictionaries are printed at the bottom.

      Variable names default to

      - `z` for primal objective

      - `z` for dual objective

      - `w` for auxiliary objective

      - `x_1, x_2, \\dots, x_n` for primal decision variables

      - `x_{n+1}, x_{n+2}, \\dots, x_{n+m}` for primal slack variables

      - `y_1, y_2, \\dots, y_m` for dual decision variables

      - `y_{m+1}, y_{m+2}, \\dots, y_{m+n}` for dual slack variables

    - 'Vanderbei':  Follows the style of Robert Vanderbei's textbook,
      Linear Programming -- Foundations and Extensions.

      - Objective functions of dictionaries are printed at the top.

      Variable names default to

      - `zeta` for primal objective

      - `xi` for dual objective

      - `xi` for auxiliary objective

      - `x_1, x_2, \\dots, x_n` for primal decision variables

      - `w_1, w_2, \\dots, w_m` for primal slack variables

      - `y_1, y_2, \\dots, y_m` for dual decision variables

      - `z_1, z_2, \\dots, z_n` for dual slack variables

    EXAMPLES::

        sage: sage.numerical.interactive_simplex_method.style()
        'UAlberta'
        sage: sage.numerical.interactive_simplex_method.style('Vanderbei')
        'Vanderbei'
        sage: sage.numerical.interactive_simplex_method.style('Doesntexist')
        Traceback (most recent call last):
        ...
        ValueError: Style must be one of: UAlberta, Vanderbei
        sage: sage.numerical.interactive_simplex_method.style('UAlberta')
        'UAlberta'
    """

class InteractiveLPProblem(SageObject):
    '''
    Construct an LP (Linear Programming) problem.

    .. NOTE::

        This class is for **educational purposes only**: if you want to solve
        Linear Programs efficiently, use :class:`MixedIntegerLinearProgram`
        instead.

    This class supports LP problems with "variables on the left" constraints.

    INPUT:

    - ``A`` -- a matrix of constraint coefficients

    - ``b`` -- a vector of constraint constant terms

    - ``c`` -- a vector of objective coefficients

    - ``x`` -- (default: ``\'x\'``) a vector of decision variables or a
      string giving the base name

    - ``constraint_type`` -- (default: ``\'<=\'``) a string specifying constraint
      type(s): either ``\'<=\'``, ``\'>=\'``, ``\'==\'``, or a list of them

    - ``variable_type`` -- (default: ``""``) a string specifying variable
      type(s): either ``\'>=\'``, ``\'<=\'``, ``""`` (the empty string), or a
      list of them, corresponding, respectively, to nonnegative,
      nonpositive, and free variables

    - ``problem_type`` -- (default: ``\'max\'``) a string specifying the
      problem type: ``\'max\'``, ``\'min\'``, ``\'-max\'``, or ``\'-min\'``

    - ``base_ring`` -- (default: the fraction field of a common ring for all
      input coefficients) a field to which all input coefficients will be
      converted

    - ``is_primal`` -- boolean (default: ``True``); whether this problem is primal or
      dual: each problem is of course dual to its own dual, this flag is mostly
      for internal use and affects default variable names only

    - ``objective_constant_term`` -- (default: 0) a constant term of the
      objective

    EXAMPLES:

    We will construct the following problem:

    .. MATH::

        \\begin{array}{l}
        \\begin{array}{lcrcrcl}
         \\max \\mspace{-6mu}&\\mspace{-6mu}  \\mspace{-6mu}&\\mspace{-6mu} 10 C \\mspace{-6mu}&\\mspace{-6mu} + \\mspace{-6mu}&\\mspace{-6mu} 5 B \\mspace{-6mu} \\\\\n         \\mspace{-6mu}&\\mspace{-6mu}  \\mspace{-6mu}&\\mspace{-6mu} C \\mspace{-6mu}&\\mspace{-6mu} + \\mspace{-6mu}&\\mspace{-6mu} B \\mspace{-6mu}&\\mspace{-6mu} \\leq \\mspace{-6mu}&\\mspace{-6mu} 1000 \\\\\n         \\mspace{-6mu}&\\mspace{-6mu}  \\mspace{-6mu}&\\mspace{-6mu} 3 C \\mspace{-6mu}&\\mspace{-6mu} + \\mspace{-6mu}&\\mspace{-6mu} B \\mspace{-6mu}&\\mspace{-6mu} \\leq \\mspace{-6mu}&\\mspace{-6mu} 1500 \\\\\n        \\end{array} \\\\\n        C, B \\geq 0
        \\end{array}

    ::

        sage: A = ([1, 1], [3, 1])
        sage: b = (1000, 1500)
        sage: c = (10, 5)
        sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')

    Same problem, but more explicitly::

        sage: P = InteractiveLPProblem(A, b, c, ["C", "B"],
        ....:     constraint_type=\'<=\', variable_type=\'>=\')

    Even more explicitly::

        sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], problem_type=\'max\',
        ....:     constraint_type=["<=", "<="], variable_type=[">=", ">="])

    Using the last form you should be able to represent any LP problem, as long
    as all like terms are collected and in constraints variables and constants
    are on different sides.
    '''
    def __init__(self, A, b, c, x: str = 'x', constraint_type: str = '<=', variable_type: str = '', problem_type: str = 'max', base_ring=None, is_primal: bool = True, objective_constant_term: int = 0) -> None:
        '''
        See :class:`InteractiveLPProblem` for documentation.

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: TestSuite(P).run()
        '''
    def __eq__(self, other):
        '''
        Check if two LP problems are equal.

        INPUT:

        - ``other`` -- anything

        OUTPUT:

        - ``True`` if ``other`` is an :class:`InteractiveLPProblem` with all details the
          same as ``self``, ``False`` otherwise.

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P2 = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P == P2
            True
            sage: P3 = InteractiveLPProblem(A, c, b, ["C", "B"], variable_type=\'>=\')
            sage: P == P3
            False
        '''
    def Abcx(self):
        '''
        Return `A`, `b`, `c`, and `x` of ``self`` as a tuple.

        OUTPUT: a tuple

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.Abcx()
            (
            [1 1]
            [3 1], (1000, 1500), (10, 5), (C, B)
            )
        '''
    def add_constraint(self, coefficients, constant_term, constraint_type: str = '<='):
        '''
        Return a new LP problem by adding a constraint to``self``.

        INPUT:

        - ``coefficients`` -- coefficients of the new constraint

        - ``constant_term`` -- a constant term of the new constraint

        - ``constraint_type`` -- (default: ``\'<=\'``) a string indicating
          the constraint type of the new constraint

        OUTPUT: an :class:`LP problem <InteractiveLPProblem>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c)
            sage: P1 = P.add_constraint(([2, 4]), 2000, "<=")
            sage: P1.Abcx()
            (
            [1 1]
            [3 1]
            [2 4], (1000, 1500, 2000), (10, 5), (x1, x2)
            )
            sage: P1.constraint_types()
            (\'<=\', \'<=\', \'<=\')
            sage: P.Abcx()
            (
            [1 1]
            [3 1], (1000, 1500), (10, 5), (x1, x2)
            )
            sage: P.constraint_types()
            (\'<=\', \'<=\')
            sage: P2 = P.add_constraint(([2, 4, 6]), 2000, "<=")
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3
            sage: P3 = P.add_constraint(([2, 4]), 2000, "<")
            Traceback (most recent call last):
            ...
            ValueError: unknown constraint type
        '''
    def base_ring(self):
        '''
        Return the base ring of ``self``.

        .. NOTE::

            The base ring of LP problems is always a field.

        OUTPUT: a ring

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.base_ring()
            Rational Field

            sage: c = (10, 5.)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.base_ring()
            Real Field with 53 bits of precision
        '''
    def constant_terms(self):
        '''
        Return constant terms of constraints of ``self``, i.e. `b`.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.constant_terms()
            (1000, 1500)
            sage: P.b()
            (1000, 1500)
        '''
    def constraint_coefficients(self):
        '''
        Return coefficients of constraints of ``self``, i.e. `A`.

        OUTPUT: a matrix

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.constraint_coefficients()
            [1 1]
            [3 1]
            sage: P.A()
            [1 1]
            [3 1]
        '''
    def constraint_types(self):
        '''
        Return a tuple listing the constraint types of all rows.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\', constraint_type=["<=", "=="])
            sage: P.constraint_types()
            (\'<=\', \'==\')
        '''
    def decision_variables(self):
        '''
        Return decision variables of ``self``, i.e. `x`.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.decision_variables()
            (C, B)
            sage: P.x()
            (C, B)
        '''
    def dual(self, y=None):
        '''
        Construct the dual LP problem for ``self``.

        INPUT:

        - ``y`` -- (default: depends on :func:`style`)
          a vector of dual decision variables or a string giving the base name

        OUTPUT: an :class:`InteractiveLPProblem`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: DP = P.dual()
            sage: DP.b() == P.c()
            True
            sage: DP.dual(["C", "B"]) == P
            True

        TESTS::

            sage: DP.standard_form().objective_name()
            -z
            sage: sage.numerical.interactive_simplex_method.style("Vanderbei")
            \'Vanderbei\'
            sage: P.dual().standard_form().objective_name()
            -xi
            sage: sage.numerical.interactive_simplex_method.style("UAlberta")
            \'UAlberta\'
            sage: P.dual().standard_form().objective_name()
            -z
        '''
    @cached_method
    def feasible_set(self):
        '''
        Return the feasible set of ``self``.

        OUTPUT: a :mod:`Polyhedron <sage.geometry.polyhedron.constructor>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.feasible_set()
            A 2-dimensional polyhedron in QQ^2
            defined as the convex hull of 4 vertices
        '''
    def is_bounded(self):
        '''
        Check if ``self`` is bounded.

        OUTPUT: ``True`` if ``self`` is bounded, ``False`` otherwise

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.is_bounded()
            True

        Note that infeasible problems are always bounded::

            sage: b = (-1000, 1500)
            sage: P = InteractiveLPProblem(A, b, c, variable_type=\'>=\')
            sage: P.is_feasible()
            False
            sage: P.is_bounded()
            True
        '''
    def is_feasible(self, *x):
        """
        Check if ``self`` or given solution is feasible.

        INPUT:

        - (optional) anything that can be interpreted as a valid solution for
          this problem, i.e. a sequence of values for all decision variables

        OUTPUT:

        - ``True`` is this problem or given solution is feasible, ``False``
          otherwise

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, variable_type='>=')
            sage: P.is_feasible()
            True
            sage: P.is_feasible(100, 200)
            True
            sage: P.is_feasible(1000, 200)
            False
            sage: P.is_feasible([1000, 200])
            False
            sage: P.is_feasible(1000)
            Traceback (most recent call last):
            ...
            TypeError: given input is not a solution for this problem
        """
    def is_negative(self):
        '''
        Return ``True`` when the problem is of type ``\'-max\'`` or ``\'-min\'``.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.is_negative()
            False
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\', problem_type=\'-min\')
            sage: P.is_negative()
            True
        '''
    def is_primal(self):
        '''
        Check if we consider this problem to be primal or dual.

        This distinction affects only some automatically chosen variable names.

        OUTPUT: boolean

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.is_primal()
            True
            sage: P.dual().is_primal()
            False
        '''
    def is_optimal(self, *x):
        """
        Check if given solution is feasible.

        INPUT:

        - anything that can be interpreted as a valid solution for
          this problem, i.e. a sequence of values for all decision variables

        OUTPUT: ``True`` if the given solution is optimal, ``False`` otherwise

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (15, 5)
            sage: P = InteractiveLPProblem(A, b, c, variable_type='>=')
            sage: P.is_optimal(100, 200)
            False
            sage: P.is_optimal(500, 0)
            True
            sage: P.is_optimal(499, 3)
            True
            sage: P.is_optimal(501, -3)
            False
        """
    def n_constraints(self):
        '''
        Return the number of constraints of ``self``, i.e. `m`.

        OUTPUT: integer

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.n_constraints()
            2
            sage: P.m()
            2
        '''
    def n_variables(self):
        '''
        Return the number of decision variables of ``self``, i.e. `n`.

        OUTPUT: integer

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.n_variables()
            2
            sage: P.n()
            2
        '''
    def objective_coefficients(self):
        '''
        Return coefficients of the objective of ``self``, i.e. `c`.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.objective_coefficients()
            (10, 5)
            sage: P.c()
            (10, 5)
        '''
    def objective_constant_term(self):
        '''
        Return the constant term of the objective.

        OUTPUT: a number

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.objective_constant_term()
            0
            sage: P.optimal_value()
            6250
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"],
            ....:       variable_type=\'>=\', objective_constant_term=-1250)
            sage: P.objective_constant_term()
            -1250
            sage: P.optimal_value()
            5000
        '''
    def objective_value(self, *x):
        """
        Return the value of the objective on the given solution.

        INPUT:

        - anything that can be interpreted as a valid solution for
          this problem, i.e. a sequence of values for all decision variables

        OUTPUT:

        - the value of the objective on the given solution taking into account
          :meth:`objective_constant_term` and :meth:`is_negative`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, variable_type='>=')
            sage: P.objective_value(100, 200)
            2000
        """
    def optimal_solution(self):
        '''
        Return **an** optimal solution of ``self``.

        OUTPUT: a vector or ``None`` if there are no optimal solutions

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.optimal_solution()
            (250, 750)
        '''
    def optimal_value(self):
        '''
        Return the optimal value for ``self``.

        OUTPUT:

        - a number if the problem is bounded, `\\pm \\infty` if it is unbounded,
          or ``None`` if it is infeasible

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.optimal_value()
            6250
        '''
    def plot(self, *args, **kwds):
        '''
        Return a plot for solving ``self`` graphically.

        INPUT:

        - ``xmin``, ``xmax``, ``ymin``, ``ymax`` -- bounds for the axes, if
          not given, an attempt will be made to pick reasonable values

        - ``alpha`` -- (default: 0.2) determines how opaque are shadows

        OUTPUT: a plot

        This only works for problems with two decision variables. On the plot
        the black arrow indicates the direction of growth of the objective. The
        lines perpendicular to it are level curves of the objective. If there
        are optimal solutions, the arrow originates in one of them and the
        corresponding level curve is solid: all points of the feasible set
        on it are optimal solutions. Otherwise the arrow is placed in the
        center. If the problem is infeasible or the objective is zero, a plot
        of the feasible set only is returned.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: p = P.plot()                                                          # needs sage.plot
            sage: p.show()                                                              # needs sage.plot

        In this case the plot works better with the following axes ranges::

            sage: p = P.plot(0, 1000, 0, 1500)                                          # needs sage.plot
            sage: p.show()                                                              # needs sage.plot

        TESTS:

        We check that zero objective can be dealt with::

            sage: InteractiveLPProblem(A, b, (0, 0), ["C", "B"], variable_type=\'>=\').plot()         # needs sage.plot
            Graphics object consisting of 8 graphics primitives
        '''
    def plot_feasible_set(self, xmin=None, xmax=None, ymin=None, ymax=None, alpha: float = 0.2):
        '''
        Return a plot of the feasible set of ``self``.

        INPUT:

        - ``xmin``, ``xmax``, ``ymin``, ``ymax`` -- bounds for the axes, if
          not given, an attempt will be made to pick reasonable values

        - ``alpha`` -- (default: 0.2) determines how opaque are shadows

        OUTPUT: a plot

        This only works for a problem with two decision variables. The plot
        shows boundaries of constraints with a shadow on one side for
        inequalities. If the :meth:`feasible_set` is not empty and at least
        part of it is in the given boundaries, it will be shaded gray and `F`
        will be placed in its middle.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: p = P.plot_feasible_set()                                             # needs sage.plot
            sage: p.show()                                                              # needs sage.plot

        In this case the plot works better with the following axes ranges::

            sage: p = P.plot_feasible_set(0, 1000, 0, 1500)                             # needs sage.plot
            sage: p.show()                                                              # needs sage.plot
        '''
    def problem_type(self):
        '''
        Return the problem type.

        Needs to be used together with ``is_negative``.

        OUTPUT: string, one of ``\'max\'``, ``\'min\'``

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\')
            sage: P.problem_type()
            \'max\'
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=\'>=\', problem_type=\'-min\')
            sage: P.problem_type()
            \'min\'
        '''
    def standard_form(self, transformation: bool = False, **kwds):
        '''
        Construct the LP problem in standard form equivalent to ``self``.

        INPUT:

        - ``transformation`` -- boolean (default: ``False``); if ``True``, a map
          converting solutions of the problem in standard form to the original
          one will be returned as well

        - you can pass (as keywords only) ``slack_variables``,
          ``auxiliary_variable``,``objective_name`` to the constructor of
          :class:`InteractiveLPProblemStandardForm`

        OUTPUT:

        - an :class:`InteractiveLPProblemStandardForm` by itself or a tuple
          with variable transformation as the second component

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, variable_type=\'>=\')
            sage: DP = P.dual()
            sage: DPSF = DP.standard_form()
            sage: DPSF.b()
            (-10, -5)
            sage: DPSF.slack_variables()
            (y3, y4)
            sage: DPSF = DP.standard_form(slack_variables=["L", "F"])
            sage: DPSF.slack_variables()
            (L, F)
            sage: DPSF, f = DP.standard_form(True)
            sage: f
            Vector space morphism represented by the matrix:
            [1 0]
            [0 1]
            Domain: Vector space of dimension 2 over Rational Field
            Codomain: Vector space of dimension 2 over Rational Field

        A more complicated transformation map::

            sage: P = InteractiveLPProblem(A, b, c, variable_type=["<=", ""],
            ....:                          objective_constant_term=42)
            sage: PSF, f = P.standard_form(True)
            sage: f
            Vector space morphism represented by the matrix:
            [-1  0]
            [ 0  1]
            [ 0 -1]
            Domain: Vector space of dimension 3 over Rational Field
            Codomain: Vector space of dimension 2 over Rational Field
            sage: PSF.optimal_solution()
            (0, 1000, 0)
            sage: P.optimal_solution()
            (0, 1000)
            sage: P.is_optimal(PSF.optimal_solution())
            Traceback (most recent call last):
            ...
            TypeError: given input is not a solution for this problem
            sage: P.is_optimal(f(PSF.optimal_solution()))
            True
            sage: PSF.optimal_value()
            5042
            sage: P.optimal_value()
            5042

        TESTS:

        Above also works for the equivalent minimization problem::

            sage: c = (-10, -5)
            sage: P = InteractiveLPProblem(A, b, c, variable_type=["<=", ""],
            ....:                          objective_constant_term=-42,
            ....:                          problem_type=\'min\')
            sage: PSF, f = P.standard_form(True)
            sage: PSF.optimal_solution()
            (0, 1000, 0)
            sage: P.optimal_solution()
            (0, 1000)
            sage: PSF.optimal_value()
            -5042
            sage: P.optimal_value()
            -5042
        '''
    def variable_types(self):
        '''
        Return a tuple listing the variable types of all decision variables.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblem(A, b, c, ["C", "B"], variable_type=[">=", ""])
            sage: P.variable_types()
            (\'>=\', \'\')
        '''
    A = constraint_coefficients
    b = constant_terms
    c = objective_coefficients
    x = decision_variables
    m = n_constraints
    n = n_variables

class InteractiveLPProblemStandardForm(InteractiveLPProblem):
    """
    Construct an LP (Linear Programming) problem in standard form.

    .. NOTE::

        This class is for **educational purposes only**: if you want to solve
        Linear Programs efficiently, use :class:`MixedIntegerLinearProgram`
        instead.

    The used standard form is:

    .. MATH::

        \\begin{array}{l}
        \\pm \\max cx \\\\\n        Ax \\leq b \\\\\n        x \\geq 0
        \\end{array}

    INPUT:

    - ``A`` -- a matrix of constraint coefficients

    - ``b`` -- a vector of constraint constant terms

    - ``c`` -- a vector of objective coefficients

    - ``x`` -- (default: ``'x'``) a vector of decision variables or a string
      the base name giving

    - ``problem_type`` -- (default: ``'max'``) a string specifying the
      problem type: either ``'max'`` or ``'-max'``

    - ``slack_variables`` -- (default: depends on :func:`style`)
      a vector of slack variables or a string giving the base name

    - ``auxiliary_variable`` -- (default: same as ``x`` parameter with adjoined
      ``'0'`` if it was given as a string, otherwise ``'x0'``) the auxiliary
      name, expected to be the same as the first decision variable for
      auxiliary problems

    - ``base_ring`` -- (default: the fraction field of a common ring for all
      input coefficients) a field to which all input coefficients will be
      converted

    - ``is_primal`` -- boolean (default: ``True``); whether this problem is primal or
      dual: each problem is of course dual to its own dual, this flag is mostly
      for internal use and affects default variable names only

    - ``objective_name`` -- string or symbolic expression for the
      objective used in dictionaries (default: depends on :func:`style`)

    - ``objective_constant_term`` -- (default: 0) a constant term of the
      objective

    EXAMPLES::

        sage: A = ([1, 1], [3, 1])
        sage: b = (1000, 1500)
        sage: c = (10, 5)
        sage: P = InteractiveLPProblemStandardForm(A, b, c)

    Unlike :class:`InteractiveLPProblem`, this class does not allow you to adjust types of
    constraints (they are always ``'<='``) and variables (they are always
    ``'>='``), and the problem type may only be ``'max'`` or ``'-max'``.
    You may give custom names to slack and auxiliary variables, but in
    most cases defaults should work::

        sage: P.decision_variables()
        (x1, x2)
        sage: P.slack_variables()
        (x3, x4)
    """
    def __init__(self, A, b, c, x: str = 'x', problem_type: str = 'max', slack_variables=None, auxiliary_variable=None, base_ring=None, is_primal: bool = True, objective_name=None, objective_constant_term: int = 0) -> None:
        """
        See :class:`InteractiveLPProblemStandardForm` for documentation.

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: TestSuite(P).run()
        """
    @staticmethod
    def random_element(m, n, bound: int = 5, special_probability: float = 0.2, **kwds):
        """
        Construct a random ``InteractiveLPProblemStandardForm``.

        INPUT:

        - ``m`` -- the number of constraints/basic variables

        - ``n`` -- the number of decision/non-basic variables

        - ``bound`` -- (default: 5) a bound on coefficients

        - ``special_probability`` -- (default: 0.2) probability of
          constructing a problem whose initial dictionary is allowed
          to be primal infeasible or dual feasible

        All other keyword arguments are passed to the constructor.

        EXAMPLES::

            sage: InteractiveLPProblemStandardForm.random_element(3, 4)
            LP problem (use 'view(...)' or '%display typeset' for details)
        """
    def add_constraint(self, coefficients, constant_term, slack_variable=None):
        """
        Return a new LP problem by adding a constraint to``self``.

        INPUT:

        - ``coefficients`` -- coefficients of the new constraint

        - ``constant_term`` -- a constant term of the new constraint

        - ``slack_variable`` -- (default: depends on :func:`style`)
          a string giving the name of the slack variable of the new constraint

        OUTPUT: an :class:`LP problem in standard form <InteractiveLPProblemStandardForm>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.Abcx()
            (
            [1 1]
            [3 1], (1000, 1500), (10, 5), (x1, x2)
            )
            sage: P.slack_variables()
            (x3, x4)
            sage: P1 = P.add_constraint(([2, 4]), 2000)
            sage: P1.Abcx()
            (
            [1 1]
            [3 1]
            [2 4], (1000, 1500, 2000), (10, 5), (x1, x2)
            )
            sage: P1.slack_variables()
            (x3, x4, x5)
            sage: P2 = P.add_constraint(([2, 4]), 2000, slack_variable='c')
            sage: P2.slack_variables()
            (x3, x4, c)
            sage: P3 = P.add_constraint(([2, 4, 6]), 2000)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3
        """
    def auxiliary_problem(self, objective_name=None):
        """
        Construct the auxiliary problem for ``self``.

        INPUT:

        - ``objective_name`` -- string or symbolic expression for the
          objective used in dictionaries (default: depends on :func:`style`)

        OUTPUT: an :class:`LP problem in standard form <InteractiveLPProblemStandardForm>`

        The auxiliary problem with the auxiliary variable `x_0` is

        .. MATH::

            \\begin{array}{l}
            \\max - x_0 \\\\\n            - x_0 + A_i x \\leq b_i \\text{ for all } i \\\\\n            x \\geq 0
            \\end{array}\\ .

        Such problems are used when the :meth:`initial_dictionary` is
        infeasible.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: AP = P.auxiliary_problem()
        """
    def auxiliary_variable(self):
        """
        Return the auxiliary variable of ``self``.

        Note that the auxiliary variable may or may not be among
        :meth:`~InteractiveLPProblem.decision_variables`.

        OUTPUT: a variable of the :meth:`coordinate_ring` of ``self``

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.auxiliary_variable()
            x0
            sage: P.decision_variables()
            (x1, x2)
            sage: AP = P.auxiliary_problem()
            sage: AP.auxiliary_variable()
            x0
            sage: AP.decision_variables()
            (x0, x1, x2)
        """
    def coordinate_ring(self):
        '''
        Return the coordinate ring of ``self``.

        OUTPUT:

        - a polynomial ring over the :meth:`~InteractiveLPProblem.base_ring` of ``self`` in
          the :meth:`auxiliary_variable`, :meth:`~InteractiveLPProblem.decision_variables`,
          and :meth:`slack_variables` with "neglex" order

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.coordinate_ring()
            Multivariate Polynomial Ring in x0, x1, x2, x3, x4, x5
            over Rational Field
            sage: P.base_ring()
            Rational Field
            sage: P.auxiliary_variable()
            x0
            sage: P.decision_variables()
            (x1, x2)
            sage: P.slack_variables()
            (x3, x4, x5)
        '''
    def dictionary(self, *x_B):
        '''
        Construct a dictionary for ``self`` with given basic variables.

        INPUT:

        - basic variables for the dictionary to be constructed

        OUTPUT: a :class:`dictionary <LPDictionary>`

        .. NOTE::

            This is a synonym for ``self.revised_dictionary(x_B).dictionary()``,
            but basic variables are mandatory.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.dictionary("x1", "x2")
            sage: D.basic_variables()
            (x1, x2)
        '''
    def feasible_dictionary(self, auxiliary_dictionary):
        """
        Construct a feasible dictionary for ``self``.

        INPUT:

        - ``auxiliary_dictionary`` -- an optimal dictionary for the
          :meth:`auxiliary_problem` of ``self`` with the optimal value `0` and
          a non-basic auxiliary variable

        OUTPUT: a feasible :class:`dictionary <LPDictionary>` for ``self``

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: AP = P.auxiliary_problem()
            sage: D = AP.initial_dictionary()
            sage: D.enter(0)
            sage: D.leave(5)
            sage: D.update()
            sage: D.enter(1)
            sage: D.leave(0)
            sage: D.update()
            sage: D.is_optimal()
            True
            sage: D.objective_value()
            0
            sage: D.basic_solution()
            (0, 400, 0)
            sage: D = P.feasible_dictionary(D)
            sage: D.is_optimal()
            False
            sage: D.is_feasible()
            True
            sage: D.objective_value()
            4000
            sage: D.basic_solution()
            (400, 0)
        """
    def final_dictionary(self):
        """
        Return the final dictionary of the simplex method applied to ``self``.

        See :meth:`run_simplex_method` for the description of possibilities.

        OUTPUT: a :class:`dictionary <LPDictionary>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.final_dictionary()
            sage: D.is_optimal()
            True

        TESTS::

            sage: P.final_dictionary() is P.final_dictionary()
            False
        """
    def final_revised_dictionary(self):
        """
        Return the final dictionary of the revised simplex method applied
        to ``self``.

        See :meth:`run_revised_simplex_method` for the description of
        possibilities.

        OUTPUT: a :class:`revised dictionary <LPRevisedDictionary>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.final_revised_dictionary()
            sage: D.is_optimal()
            True

        TESTS::

            sage: P.final_revised_dictionary() is P.final_revised_dictionary()
            False
        """
    def initial_dictionary(self):
        '''
        Construct the initial dictionary of ``self``.

        The initial dictionary "defines" :meth:`slack_variables` in terms
        of the :meth:`~InteractiveLPProblem.decision_variables`, i.e. it has slack
        variables as basic ones.

        OUTPUT: a :class:`dictionary <LPDictionary>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
        '''
    def inject_variables(self, scope=None, verbose: bool = True) -> None:
        """
        Inject variables of ``self`` into ``scope``.

        INPUT:

        - ``scope`` -- namespace (default: global)

        - ``verbose`` -- if ``True`` (default), names of injected variables
          will be printed

        OUTPUT: none

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: 3*x1 + x2
            x2 + 3*x1
        """
    def objective_name(self):
        '''
        Return the objective name used in dictionaries for this problem.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.objective_name()
            z
            sage: sage.numerical.interactive_simplex_method.style("Vanderbei")
            \'Vanderbei\'
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.objective_name()
            zeta
            sage: sage.numerical.interactive_simplex_method.style("UAlberta")
            \'UAlberta\'
            sage: P = InteractiveLPProblemStandardForm(A, b, c, objective_name=\'custom\')
            sage: P.objective_name()
            custom
        '''
    def revised_dictionary(self, *x_B):
        '''
        Construct a revised dictionary for ``self``.

        INPUT:

        - basic variables for the dictionary to be constructed; if not given,
          :meth:`slack_variables` will be used, perhaps with the
          :meth:`auxiliary_variable` to give a feasible dictionary

        OUTPUT: a :class:`revised dictionary <LPRevisedDictionary>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary("x1", "x2")
            sage: D.basic_variables()
            (x1, x2)

        If basic variables are not given the initial dictionary is
        constructed::

            sage: P.revised_dictionary().basic_variables()
            (x3, x4)
            sage: P.initial_dictionary().basic_variables()
            (x3, x4)

        Unless it is infeasible, in which case a feasible dictionary for the
        auxiliary problem is constructed::

            sage: A = ([1, 1], [3, 1], [-1,-1])
            sage: b = (1000, 1500, -400)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.initial_dictionary().is_feasible()
            False
            sage: P.revised_dictionary().basic_variables()
            (x3, x4, x0)
        '''
    def run_revised_simplex_method(self):
        """
        Apply the revised simplex method and return all steps.

        OUTPUT:

        - :class:`~sage.misc.html.HtmlFragment` with HTML/`\\LaTeX` code of
          all encountered dictionaries

        .. NOTE::

            You can access the :meth:`final_revised_dictionary`, which can be
            one of the following:

            - an optimal dictionary with the :meth:`auxiliary_variable` among
              :meth:`~LPRevisedDictionary.basic_variables` and a nonzero
              optimal value indicating
              that ``self`` is infeasible;

            - a non-optimal dictionary that has marked entering
              variable for which there is no choice of the leaving variable,
              indicating that ``self`` is unbounded;

            - an optimal dictionary.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.run_revised_simplex_method()
            \\begin{equation*}
            ...
            \\end{equation*}
            Entering: $x_{1}$. Leaving: $x_{0}$.
            \\begin{equation*}
            ...
            \\end{equation*}
            Entering: $x_{5}$. Leaving: $x_{4}$.
            \\begin{equation*}
            ...
            \\end{equation*}
            Entering: $x_{2}$. Leaving: $x_{3}$.
            \\begin{equation*}
            ...
            \\end{equation*}
            The optimal value: $6250$. An optimal solution: $\\left(250,\\,750\\right)$.
        """
    def run_simplex_method(self):
        """
        Apply the simplex method and return all steps and intermediate states.

        OUTPUT:

        - :class:`~sage.misc.html.HtmlFragment` with HTML/`\\LaTeX` code of
          all encountered dictionaries

        .. NOTE::

            You can access the :meth:`final_dictionary`, which can be one
            of the following:

            - an optimal dictionary for the :meth:`auxiliary_problem` with a
              nonzero optimal value indicating that ``self`` is infeasible;

            - a non-optimal dictionary for ``self`` that has marked entering
              variable for which there is no choice of the leaving variable,
              indicating that ``self`` is unbounded;

            - an optimal dictionary for ``self``.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.run_simplex_method()
            \\begin{equation*}
            ...
            \\end{equation*}
            The initial dictionary is infeasible, solving auxiliary problem.
            ...
            Entering: $x_{0}$. Leaving: $x_{5}$.
            ...
            Entering: $x_{1}$. Leaving: $x_{0}$.
            ...
            Back to the original problem.
            ...
            Entering: $x_{5}$. Leaving: $x_{4}$.
            ...
            Entering: $x_{2}$. Leaving: $x_{3}$.
            ...
            The optimal value: $6250$. An optimal solution: $\\left(250,\\,750\\right)$.
        """
    def slack_variables(self):
        '''
        Return slack variables of ``self``.

        Slack variables are differences between the constant terms and
        left hand sides of the constraints.

        If you want to give custom names to slack variables, you have to do so
        during construction of the problem.

        OUTPUT: a tuple

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: P.slack_variables()
            (x3, x4)
            sage: P = InteractiveLPProblemStandardForm(A, b, c, ["C", "B"],
            ....:     slack_variables=["L", "F"])
            sage: P.slack_variables()
            (L, F)
        '''

class LPAbstractDictionary(SageObject):
    """
    Abstract base class for dictionaries for LP problems.

    Instantiating this class directly is meaningless, see :class:`LPDictionary`
    and :class:`LPRevisedDictionary` for useful extensions.
    """
    def __init__(self) -> None:
        """
        Initialize internal fields for entering and leaving variables.

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()    # indirect doctest
        """
    @abstract_method
    def add_row(self, nonbasic_coefficients, constant, basic_variable=None) -> None:
        '''
        Return a dictionary with an additional row based on a given dictionary.

        INPUT:

        - ``nonbasic_coefficients`` -- list of the coefficients for the
          new row (with which nonbasic variables are subtracted in the relation
          for the new basic variable)

        - ``constant`` -- the constant term for the new row

        - ``basic_variable`` -- (default: depends on :func:`style`)
          a string giving the name of the basic variable of the new row

        OUTPUT: a new dictionary of the same class

        EXAMPLES::

            sage: A = ([-1, 1, 7], [8, 2, 13], [34, 17, 12])
            sage: b = (2, 17, 6)
            sage: c = (55/10, 21/10, 14/30)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.dictionary("x1", "x2", "x4")
            sage: D1 = D.add_row([7, 11, 19], 42, basic_variable=\'c\')
            sage: D1.row_coefficients("c")
            (7, 11, 19)
        '''
    def base_ring(self):
        """
        Return the base ring of ``self``, i.e. the ring of coefficients.

        OUTPUT: a ring

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.base_ring()
            Rational Field
            sage: D = P.revised_dictionary()
            sage: D.base_ring()
            Rational Field
        """
    @abstract_method
    def basic_variables(self) -> None:
        """
        Return the basic variables of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.basic_variables()
            (x3, x4)
        """
    def basic_solution(self, include_slack_variables: bool = False):
        """
        Return the basic solution of ``self``.

        The basic solution associated to a dictionary is obtained by setting to
        zero all :meth:`~LPDictionary.nonbasic_variables`, in which case
        :meth:`~LPDictionary.basic_variables` have to be equal to
        :meth:`~LPDictionary.constant_terms` in equations.
        It may refer to values of :meth:`~InteractiveLPProblem.decision_variables` only or
        include :meth:`~InteractiveLPProblemStandardForm.slack_variables` as well.

        INPUT:

        - ``include_slack_variables`` -- boolean (default: ``False``); if ``True``,
          values of slack variables will be appended at the end

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.basic_solution()
            (0, 0)
            sage: D.basic_solution(True)
            (0, 0, 1000, 1500)
            sage: D = P.revised_dictionary()
            sage: D.basic_solution()
            (0, 0)
            sage: D.basic_solution(True)
            (0, 0, 1000, 1500)
        """
    @abstract_method
    def column_coefficients(self, v) -> None:
        """
        Return the coefficients of a nonbasic variable.

        INPUT:

        - ``v`` -- a nonbasic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a variable

        OUTPUT: a vector of coefficients of a nonbasic variable

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.column_coefficients(1)
            (1, 3)
        """
    @abstract_method
    def constant_terms(self) -> None:
        """
        Return the constant terms of relations of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.constant_terms()
            (1000, 1500)
        """
    def coordinate_ring(self):
        """
        Return the coordinate ring of ``self``.

        OUTPUT:

        - a polynomial ring in
          :meth:`~InteractiveLPProblemStandardForm.auxiliary_variable`,
          :meth:`~InteractiveLPProblem.decision_variables`, and
          :meth:`~InteractiveLPProblemStandardForm.slack_variables` of ``self`` over the
          :meth:`base_ring`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.coordinate_ring()
            Multivariate Polynomial Ring in x0, x1, x2, x3, x4
            over Rational Field
            sage: D = P.revised_dictionary()
            sage: D.coordinate_ring()
            Multivariate Polynomial Ring in x0, x1, x2, x3, x4
            over Rational Field
        """
    def dual_ratios(self):
        """
        Return ratios used to determine the entering variable based on leaving.

        OUTPUT:

        - A list of pairs `(r_j, x_j)` where `x_j` is a non-basic variable and
          `r_j = c_j / a_{ij}` is the ratio of the objective coefficient `c_j`
          to the coefficient `a_{ij}` of `x_j` in the relation for the leaving
          variable `x_i`:

          .. MATH::

              x_i = b_i - \\cdots - a_{ij} x_j - \\cdots.

          The order of pairs matches the order of
          :meth:`~LPDictionary.nonbasic_variables`,
          but only `x_j` with negative `a_{ij}` are considered.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.dictionary(2, 3, 5)
            sage: D.leave(3)
            sage: D.dual_ratios()
            [(5/2, x1), (5, x4)]
            sage: D = P.revised_dictionary(2, 3, 5)
            sage: D.leave(3)
            sage: D.dual_ratios()
            [(5/2, x1), (5, x4)]
        """
    def enter(self, v) -> None:
        '''
        Set ``v`` as the entering variable of ``self``.

        INPUT:

        - ``v`` -- a non-basic variable of ``self``, can be given as a string,
          an actual variable, or an integer interpreted as the index of a
          variable. It is also possible to enter ``None`` to reset choice.

        OUTPUT:

        - none, but the selected variable will be used as entering by methods
          that require an entering variable and the corresponding column
          will be typeset in green

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.enter("x1")

        We can also use indices of variables::

            sage: D.enter(1)

        Or variable names without quotes after injecting them::

            sage: P.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: D.enter(x1)

        The same works for revised dictionaries as well::

            sage: D = P.revised_dictionary()
            sage: D.enter(x1)
        '''
    def entering(self):
        """
        Return the currently chosen entering variable.

        OUTPUT: a variable if the entering one was chosen, otherwise ``None``

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.entering() is None
            True
            sage: D.enter(1)
            sage: D.entering()
            x1
        """
    def entering_coefficients(self):
        """
        Return coefficients of the entering variable.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.enter(1)
            sage: D.entering_coefficients()
            (1, 3)
        """
    def is_dual_feasible(self):
        """
        Check if ``self`` is dual feasible.

        OUTPUT:

        - ``True`` if all :meth:`~LPDictionary.objective_coefficients` are
          nonpositive, ``False`` otherwise

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.is_dual_feasible()
            False
            sage: D = P.revised_dictionary()
            sage: D.is_dual_feasible()
            False
        """
    def is_feasible(self):
        """
        Check if ``self`` is feasible.

        OUTPUT:

        - ``True`` if all :meth:`~LPDictionary.constant_terms` are
          nonnegative, ``False`` otherwise

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.is_feasible()
            True
            sage: D = P.revised_dictionary()
            sage: D.is_feasible()
            True
        """
    def is_optimal(self):
        """
        Check if ``self`` is optimal.

        OUTPUT:

        - ``True`` if ``self`` :meth:`is_feasible` and :meth:`is_dual_feasible`
          (i.e. all :meth:`~LPDictionary.constant_terms` are nonnegative and
          all :meth:`~LPDictionary.objective_coefficients` are nonpositive),
          ``False`` otherwise.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.is_optimal()
            False
            sage: D = P.revised_dictionary()
            sage: D.is_optimal()
            False
            sage: D = P.revised_dictionary(1, 2)
            sage: D.is_optimal()
            True
        """
    def leave(self, v) -> None:
        '''
        Set ``v`` as the leaving variable of ``self``.

        INPUT:

        - ``v`` -- a basic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a
          variable. It is also possible to leave ``None`` to reset choice.

        OUTPUT:

        - none, but the selected variable will be used as leaving by methods
          that require a leaving variable and the corresponding row will be
          typeset in red

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.leave("x4")

        We can also use indices of variables::

            sage: D.leave(4)

        Or variable names without quotes after injecting them::

            sage: P.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: D.leave(x4)

        The same works for revised dictionaries as well::

            sage: D = P.revised_dictionary()
            sage: D.leave(x4)
        '''
    def leaving(self):
        """
        Return the currently chosen leaving variable.

        OUTPUT: a variable if the leaving one was chosen, otherwise ``None``

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.leaving() is None
            True
            sage: D.leave(4)
            sage: D.leaving()
            x4
        """
    def leaving_coefficients(self):
        """
        Return coefficients of the leaving variable.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.dictionary(2, 3)
            sage: D.leave(3)
            sage: D.leaving_coefficients()
            (-2, -1)

        The same works for revised dictionaries as well::

            sage: D = P.revised_dictionary(2, 3)
            sage: D.leave(3)
            sage: D.leaving_coefficients()
            (-2, -1)
        """
    @abstract_method
    def nonbasic_variables(self) -> None:
        """
        Return non-basic variables of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.nonbasic_variables()
            (x1, x2)
        """
    @abstract_method
    def objective_coefficients(self) -> None:
        """
        Return coefficients of the objective of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_coefficients()
            (10, 5)
        """
    @abstract_method
    def objective_name(self) -> None:
        """
        Return the objective name of ``self``.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_name()
            z
        """
    @abstract_method
    def objective_value(self) -> None:
        """
        Return the value of the objective at the
        :meth:`~LPAbstractDictionary.basic_solution` of ``self``.

        OUTPUT: a number

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_value()
            0
        """
    def possible_dual_simplex_method_steps(self):
        """
        Return possible dual simplex method steps for ``self``.

        OUTPUT:

        - A list of pairs ``(leaving, entering)``, where ``leaving`` is a
          basic variable that may :meth:`leave` and ``entering`` is a list of
          non-basic variables that may :meth:`enter` when ``leaving`` leaves.
          Note that ``entering`` may be empty, indicating that the problem is
          infeasible (since the dual one is unbounded).

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.dictionary(2, 3)
            sage: D.possible_dual_simplex_method_steps()
            [(x3, [x1])]
            sage: D = P.revised_dictionary(2, 3)
            sage: D.possible_dual_simplex_method_steps()
            [(x3, [x1])]
        """
    def possible_entering(self):
        """
        Return possible entering variables for ``self``.

        OUTPUT:

        - a list of non-basic variables of ``self`` that can :meth:`enter` on
          the next step of the (dual) simplex method

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.possible_entering()
            [x1, x2]
            sage: D = P.revised_dictionary()
            sage: D.possible_entering()
            [x1, x2]
        """
    def possible_leaving(self):
        """
        Return possible leaving variables for ``self``.

        OUTPUT:

        - a list of basic variables of ``self`` that can :meth:`leave` on
          the next step of the (dual) simplex method

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.enter(1)
            sage: D.possible_leaving()
            [x4]
            sage: D = P.revised_dictionary()
            sage: D.enter(1)
            sage: D.possible_leaving()
            [x4]
        """
    def possible_simplex_method_steps(self):
        """
        Return possible simplex method steps for ``self``.

        OUTPUT:

        - A list of pairs ``(entering, leaving)``, where ``entering`` is a
          non-basic variable that may :meth:`enter` and ``leaving`` is a list
          of basic variables that may :meth:`leave` when ``entering`` enters.
          Note that ``leaving`` may be empty, indicating that the problem is
          unbounded.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.possible_simplex_method_steps()
            [(x1, [x4]), (x2, [x3])]
            sage: D = P.revised_dictionary()
            sage: D.possible_simplex_method_steps()
            [(x1, [x4]), (x2, [x3])]
        """
    def ratios(self):
        """
        Return ratios used to determine the leaving variable based on entering.

        OUTPUT:

        - A list of pairs `(r_i, x_i)` where `x_i` is a basic variable and
          `r_i = b_i / a_{ik}` is the ratio of the constant term `b_i` to the
          coefficient `a_{ik}` of the entering variable `x_k` in the relation
          for `x_i`:

          .. MATH::

              x_i = b_i - \\cdots - a_{ik} x_k - \\cdots.

          The order of pairs matches the order of
          :meth:`~LPDictionary.basic_variables`,
          but only `x_i` with positive `a_{ik}` are considered.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.enter(1)
            sage: D.ratios()
            [(1000, x3), (500, x4)]
            sage: D = P.revised_dictionary()
            sage: D.enter(1)
            sage: D.ratios()
            [(1000, x3), (500, x4)]
        """
    @abstract_method
    def row_coefficients(self, v) -> None:
        '''
        Return the coefficients of the basic variable ``v``.

        These are the coefficients with which nonbasic variables are subtracted
        in the relation for ``v``.

        INPUT:

        - ``v`` -- a basic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a variable

        OUTPUT: a vector of coefficients of a basic variable

        EXAMPLES::

            sage: A = ([-1, 1], [8, 2])
            sage: b = (2, 17)
            sage: c = (55/10, 21/10)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.final_dictionary()
            sage: D.row_coefficients("x1")
            (1/10, -1/5)

        We can also use indices of variables::

            sage: D.row_coefficients(1)
            (1/10, -1/5)

        Or use variable names without quotes after injecting them::

            sage: P.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: D.row_coefficients(x1)
            (1/10, -1/5)
        '''
    def run_dual_simplex_method(self):
        """
        Apply the dual simplex method and return all steps/intermediate states.

        If either entering or leaving variables were already set, they will be
        used.

        OUTPUT:

        - :class:`~sage.misc.html.HtmlFragment` with HTML/`\\LaTeX` code of
          all encountered dictionaries

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.run_dual_simplex_method()
            Traceback (most recent call last):
            ...
            ValueError: leaving variables can be determined for feasible
            dictionaries with a set entering variable or for dual feasible
            dictionaries

        Let's start with a dual feasible dictionary then::

            sage: D = P.dictionary(2, 3, 5)
            sage: D.is_dual_feasible()
            True
            sage: D.is_optimal()
            False
            sage: D.run_dual_simplex_method()
            \\begin{equation*}
            ...
            \\end{equation*}
            Leaving: $x_{3}$. Entering: $x_{1}$.
            \\begin{equation*}
            ...
            \\end{equation*}
            sage: D.is_optimal()
            True

        This method detects infeasible problems::

            sage: A = ([1, 0],)
            sage: b = (-1,)
            sage: c = (0, -1)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.run_dual_simplex_method()
            \\begin{equation*}
            ...
            \\end{equation*}
            The problem is infeasible because of $x_{3}$ constraint.
        """
    def run_simplex_method(self):
        """
        Apply the simplex method and return all steps and intermediate states.

        If either entering or leaving variables were already set, they will be
        used.

        OUTPUT:

        - :class:`~sage.misc.html.HtmlFragment` with HTML/`\\LaTeX` code of
          all encountered dictionaries

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.run_simplex_method()
            Traceback (most recent call last):
            ...
            ValueError: entering variables can be determined for feasible
            dictionaries or for dual feasible dictionaries with a set leaving
            variable

        Let's start with a feasible dictionary then::

            sage: D = P.dictionary(1, 3, 4)
            sage: D.is_feasible()
            True
            sage: D.is_optimal()
            False
            sage: D.run_simplex_method()
            \\begin{equation*}
            ...
            \\end{equation*}
            Entering: $x_{5}$. Leaving: $x_{4}$.
            \\begin{equation*}
            ...
            \\end{equation*}
            Entering: $x_{2}$. Leaving: $x_{3}$.
            \\begin{equation*}
            ...
            \\end{equation*}
            sage: D.is_optimal()
            True

        This method detects unbounded problems::

            sage: A = ([1, 0],)
            sage: b = (1,)
            sage: c = (0, 1)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.run_simplex_method()
            \\begin{equation*}
            ...
            \\end{equation*}
            The problem is unbounded in $x_{2}$ direction.
        """
    @abstract_method
    def update(self) -> None:
        '''
        Update ``self`` using previously set entering and leaving variables.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_value()
            0
            sage: D.enter("x1")
            sage: D.leave("x4")
            sage: D.update()
            sage: D.objective_value()
            5000
        '''

class LPDictionary(LPAbstractDictionary):
    '''
    Construct a dictionary for an LP problem.

    A dictionary consists of the following data:

    .. MATH::

        \\begin{array}{|l|}
        \\hline
        x_B = b - A x_N\\\\\n        \\hline
        z = z^* + c x_N\\\\\n        \\hline
        \\end{array}

    INPUT:

    - ``A`` -- a matrix of relation coefficients

    - ``b`` -- a vector of relation constant terms

    - ``c`` -- a vector of objective coefficients

    - ``objective_value`` -- current value of the objective `z^*`

    - ``basic_variables`` -- list of basic variables `x_B`

    - ``nonbasic_variables`` -- list of non-basic variables `x_N`

    - ``objective_name`` -- a "name" for the objective `z`

    OUTPUT: a :class:`dictionary for an LP problem <LPDictionary>`

    .. NOTE::

        This constructor does not check correctness of input, as it is
        intended to be used internally by :class:`InteractiveLPProblemStandardForm`.

    EXAMPLES:

    The intended way to use this class is indirect::

        sage: A = ([1, 1], [3, 1])
        sage: b = (1000, 1500)
        sage: c = (10, 5)
        sage: P = InteractiveLPProblemStandardForm(A, b, c)
        sage: D = P.initial_dictionary()
        sage: D
        LP problem dictionary (use ...)

    But if you want you can create a dictionary without starting with an LP
    problem, here is construction of the same dictionary as above::

        sage: A = matrix(QQ, ([1, 1], [3, 1]))
        sage: b = vector(QQ, (1000, 1500))
        sage: c = vector(QQ, (10, 5))
        sage: R = PolynomialRing(QQ, "x1, x2, x3, x4", order=\'neglex\')
        sage: from sage.numerical.interactive_simplex_method \\\n        ....:     import LPDictionary
        sage: D2 = LPDictionary(A, b, c, 0, R.gens()[2:], R.gens()[:2], "z")
        sage: D2 == D
        True
    '''
    def __init__(self, A, b, c, objective_value, basic_variables, nonbasic_variables, objective_name) -> None:
        '''
        See :class:`LPDictionary` for documentation.

        TESTS::

            sage: A = matrix(QQ, ([1, 1], [3, 1]))
            sage: b = vector(QQ, (1000, 1500))
            sage: c = vector(QQ, (10, 5))
            sage: R = PolynomialRing(QQ, "x1, x2, x3, x4", order=\'neglex\')
            sage: from sage.numerical.interactive_simplex_method \\\n            ....:     import LPDictionary
            sage: D = LPDictionary(A, b, c, 0, R.gens()[2:], R.gens()[:2], "z")
            sage: TestSuite(D).run()
        '''
    def __copy__(self):
        """
        TESTS:

        Test that copies do not share state with the original::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D_2 = copy(D)
            sage: D is D_2
            False
            sage: D.enter('x1')
            sage: D.leave('x3')
            sage: D.update()
            sage: D_2 == D
            False
        """
    @staticmethod
    def random_element(m, n, bound: int = 5, special_probability: float = 0.2):
        """
        Construct a random dictionary.

        INPUT:

        - ``m`` -- the number of constraints/basic variables

        - ``n`` -- the number of decision/non-basic variables

        - ``bound`` -- (default: 5) a bound on dictionary entries

        - ``special_probability`` -- (default: 0.2) probability of constructing a
          potentially infeasible or potentially optimal dictionary

        OUTPUT: an :class:`LP problem dictionary <LPDictionary>`

        EXAMPLES::

            sage: from sage.numerical.interactive_simplex_method \\\n            ....:     import random_dictionary
            sage: random_dictionary(3, 4)  # indirect doctest
            LP problem dictionary (use 'view(...)' or '%display typeset' for details)
        """
    def __eq__(self, other):
        '''
        Check if two LP problem dictionaries are equal.

        INPUT:

        - ``other`` -- anything

        OUTPUT:

        - ``True`` if ``other`` is an :class:`LPDictionary` with all
          details the same as ``self``, ``False`` otherwise.

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()

            sage: A = matrix(QQ, ([1, 1], [3, 1]))
            sage: b = vector(QQ, (1000, 1500))
            sage: c = vector(QQ, (10, 5))
            sage: R = PolynomialRing(QQ, "x1, x2, x3, x4", order=\'neglex\')
            sage: from sage.numerical.interactive_simplex_method \\\n            ....:     import LPDictionary
            sage: D2 = LPDictionary(A, b, c, 0, R.gens()[2:], R.gens()[:2], "z")
            sage: D2 == D
            True

            sage: D3 = LPDictionary(A, b, c, 0, R.gens()[2:], R.gens()[:2], "w")
            sage: D2 == D3
            False
        '''
    def add_row(self, nonbasic_coefficients, constant, basic_variable=None):
        '''
        Return a dictionary with an additional row based on a given dictionary.

        INPUT:

        - ``nonbasic_coefficients`` -- list of the coefficients for the
          new row (with which nonbasic variables are subtracted in the relation
          for the new basic variable)

        - ``constant`` -- the constant term for the new row

        - ``basic_variable`` -- (default: depends on :func:`style`)
          a string giving the name of the basic variable of the new row

        OUTPUT: a :class:`dictionary <LPDictionary>`

        EXAMPLES::

            sage: A = ([-1, 1, 7], [8, 2, 13], [34, 17, 12])
            sage: b = (2, 17, 6)
            sage: c = (55/10, 21/10, 14/30)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.dictionary("x1", "x2", "x4")
            sage: D1 = D.add_row([7, 11, 19], 42, basic_variable=\'c\')
            sage: D1.row_coefficients("c")
            (7, 11, 19)
            sage: D1.constant_terms()[-1]
            42
            sage: D1.basic_variables()[-1]
            c
        '''
    def basic_variables(self):
        """
        Return the basic variables of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.basic_variables()
            (x3, x4)
        """
    def column_coefficients(self, v):
        """
        Return coefficients of a nonbasic variable.

        INPUT:

        - ``v`` -- a nonbasic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a variable

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.column_coefficients(1)
            (1, 3)
        """
    def constant_terms(self):
        """
        Return the constant terms of relations of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.constant_terms()
            (1000, 1500)
        """
    def nonbasic_variables(self):
        """
        Return non-basic variables of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.nonbasic_variables()
            (x1, x2)
        """
    def objective_coefficients(self):
        """
        Return coefficients of the objective of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_coefficients()
            (10, 5)
        """
    def objective_name(self):
        """
        Return the objective name of ``self``.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_name()
            z
        """
    def objective_value(self):
        """
        Return the value of the objective at the
        :meth:`~LPAbstractDictionary.basic_solution` of ``self``.

        OUTPUT: a number

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_value()
            0
        """
    def row_coefficients(self, v):
        '''
        Return the coefficients of the basic variable ``v``.

        These are the coefficients with which nonbasic variables are subtracted
        in the relation for ``v``.

        INPUT:

        - ``v`` -- a basic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a variable

        OUTPUT: a vector of coefficients of a basic variable

        EXAMPLES::

            sage: A = ([-1, 1], [8, 2])
            sage: b = (2, 17)
            sage: c = (55/10, 21/10)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.final_dictionary()
            sage: D.row_coefficients("x1")
            (1/10, -1/5)

        We can also use indices of variables::

            sage: D.row_coefficients(1)
            (1/10, -1/5)

        Or use variable names without quotes after injecting them::

            sage: P.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: D.row_coefficients(x1)
            (1/10, -1/5)
        '''
    def update(self) -> None:
        '''
        Update ``self`` using previously set entering and leaving variables.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.initial_dictionary()
            sage: D.objective_value()
            0
            sage: D.enter("x1")
            sage: D.leave("x4")
            sage: D.update()
            sage: D.objective_value()
            5000
        '''

random_dictionary: Incomplete

class LPRevisedDictionary(LPAbstractDictionary):
    '''
    Construct a revised dictionary for an LP problem.

    INPUT:

    - ``problem`` -- an :class:`LP problem in standard form
      <InteractiveLPProblemStandardForm>`

    - ``basic_variables`` -- list of basic variables or their indices

    OUTPUT: a :class:`revised dictionary for an LP problem <LPRevisedDictionary>`

    A revised dictionary encodes the same relations as a
    :class:`regular dictionary <LPDictionary>`, but stores only what is
    "necessary to efficiently compute data for the simplex method".

    Let the original problem be

    .. MATH::

        \\begin{array}{l}
        \\pm \\max cx \\\\\n        Ax \\leq b \\\\\n        x \\geq 0
        \\end{array}

    Let `\\bar{x}` be the vector of :meth:`~InteractiveLPProblem.decision_variables` `x`
    followed by the :meth:`~InteractiveLPProblemStandardForm.slack_variables`.
    Let `\\bar{c}` be the vector of :meth:`~InteractiveLPProblem.objective_coefficients` `c`
    followed by zeroes for all slack variables.
    Let `\\bar{A} = (A | I)` be the matrix of
    :meth:`~InteractiveLPProblem.constraint_coefficients` `A` augmented by the identity
    matrix as columns corresponding to the slack variables. Then the problem
    above can be written as

    .. MATH::

        \\begin{array}{l}
        \\pm \\max \\bar{c} \\bar{x} \\\\\n        \\bar{A} \\bar{x} = b \\\\\n        \\bar{x} \\geq 0
        \\end{array}

    and any dictionary is a system of equations equivalent to
    `\\bar{A} \\bar{x} = b`, but resolved for :meth:`basic_variables` `x_B` in
    terms of :meth:`nonbasic_variables` `x_N` together with the expression for
    the objective in terms of `x_N`. Let :meth:`c_B` and :meth:`c_N` be vectors
    "splitting `\\bar{c}` into basic and non-basic parts". Let :meth:`B` and
    :meth:`A_N` be the splitting of `\\bar{A}`. Then the corresponding dictionary
    is

    .. MATH::

        \\begin{array}{|l|}
        \\hline
        x_B = B^{-1} b - B^{-1} A_N x_N\\\\\n        \\hline
        z = y b + \\left(c_N - y^T A_N\\right) x_N\\\\\n        \\hline
        \\end{array}

    where `y = c_B^T B^{-1}`. To proceed with the simplex method, it is not
    necessary to compute all entries of this dictionary. On the other hand, any
    entry is easy to compute, if you know `B^{-1}`, so we keep track of it
    through the update steps.

    EXAMPLES::

        sage: A = ([1, 1], [3, 1])
        sage: b = (1000, 1500)
        sage: c = (10, 5)
        sage: P = InteractiveLPProblemStandardForm(A, b, c)
        sage: from sage.numerical.interactive_simplex_method \\\n        ....:     import LPRevisedDictionary
        sage: D = LPRevisedDictionary(P, [1, 2])
        sage: D.basic_variables()
        (x1, x2)
        sage: D
        LP problem dictionary (use ...)

    The same dictionary can be constructed through the problem::

        sage: P.revised_dictionary(1, 2) == D
        True

    When this dictionary is typeset, you will see two tables like these ones:

    .. MATH::

        \\renewcommand{\\arraystretch}{1.500000}
        \\begin{array}{l}
        \\begin{array}{l|r|rr||r||r}
        x_B & c_B &  & \\mspace{-16mu} B^{-1} & y & B^{-1} b \\\\\n        \\hline
        x_{1} & 10 & -\\frac{1}{2} & \\frac{1}{2} & \\frac{5}{2} & 250 \\\\\n        x_{2} & 5 & \\frac{3}{2} & -\\frac{1}{2} & \\frac{5}{2} & 750 \\\\\n        \\end{array}\\\\\n        \\\\\n        \\begin{array}{r|rr}
        x_N & x_{3} & x_{4} \\\\\n        \\hline
        c_N^T & 0 & 0 \\\\\n        \\hline
        y^T A_N & \\frac{5}{2} & \\frac{5}{2} \\\\\n        \\hline
        c_N^T - y^T A_N & -\\frac{5}{2} & -\\frac{5}{2} \\\\\n        \\end{array}
        \\end{array}

    More details will be shown if entering and leaving variables are set, but in
    any case the top table shows `B^{-1}` and a few extra columns, while the
    bottom one shows several rows: these are related to columns and rows of
    dictionary entries.
    '''
    def __init__(self, problem, basic_variables) -> None:
        """
        See :class:`LPRevisedDictionary` for documentation.

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: from sage.numerical.interactive_simplex_method \\\n            ....:     import LPRevisedDictionary
            sage: D = LPRevisedDictionary(P, [1, 2])
            sage: TestSuite(D).run()
        """
    def __eq__(self, other):
        """
        Check if two revised LP problem dictionaries are equal.

        INPUT:

        - ``other`` -- anything

        OUTPUT:

        - ``True`` if ``other`` is an :class:`LPRevisedDictionary` for the same
          :class:`InteractiveLPProblemStandardForm` with the same :meth:`basic_variables`,
          ``False`` otherwise

        TESTS::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: from sage.numerical.interactive_simplex_method \\\n            ....:     import LPRevisedDictionary
            sage: D1 = LPRevisedDictionary(P, [1, 2])
            sage: D2 = LPRevisedDictionary(P, [1, 2])
            sage: D1 is D2
            False
            sage: D1 == D2
            True
            sage: D3 = LPRevisedDictionary(P, [2, 0])
            sage: D1 == D3
            False
        """
    def A(self, v):
        '''
        Return the column of constraint coefficients corresponding to ``v``.

        INPUT:

        - ``v`` -- a variable, its name, or its index

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.A(1)
            (1, 3)
            sage: D.A(0)
            (-1, -1)
            sage: D.A("x3")
            (1, 0)
        '''
    def A_N(self):
        """
        Return the `A_N` matrix, constraint coefficients of
        non-basic variables.

        OUTPUT: a matrix

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.A_N()
            [1 1]
            [3 1]
        """
    def B(self):
        """
        Return the `B` matrix, i.e. constraint coefficients of
        basic variables.

        OUTPUT: a matrix

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary(1, 2)
            sage: D.B()
            [1 1]
            [3 1]
        """
    def B_inverse(self):
        """
        Return the inverse of the :meth:`B` matrix.

        This inverse matrix is stored and computed during dictionary update in
        a more efficient way than generic inversion.

        OUTPUT: a matrix

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary(1, 2)
            sage: D.B_inverse()
            [-1/2  1/2]
            [ 3/2 -1/2]
        """
    def E(self):
        """
        Return the eta matrix between ``self`` and the next dictionary.

        OUTPUT: a matrix

        If `B_{\\mathrm{old}}` is the current matrix `B` and `B_{\\mathrm{new}}`
        is the `B` matrix of the next dictionary (after the update step), then
        `B_{\\mathrm{new}} = B_{\\mathrm{old}} E`.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.enter(1)
            sage: D.leave(4)
            sage: D.E()
            [1 1]
            [0 3]
        """
    def E_inverse(self):
        """
        Return the inverse of the matrix :meth:`E`.

        This inverse matrix is computed in a more efficient way than generic
        inversion.

        OUTPUT: a matrix

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.enter(1)
            sage: D.leave(4)
            sage: D.E_inverse()
            [   1 -1/3]
            [   0  1/3]
        """
    def add_row(self, nonbasic_coefficients, constant, basic_variable=None):
        '''
        Return a dictionary with an additional row based on a given dictionary.

        The implementation of this method for revised dictionaries
        adds a new inequality constraint to the problem, in which the given
        ``basic_variable`` becomes the slack variable.  The resulting dictionary
        (with ``basic_variable`` added to the basis) will have the given
        ``nonbasic_coefficients`` and ``constant`` as a new row.

        INPUT:

        - ``nonbasic_coefficients`` -- list of the coefficients for the
          new row (with which nonbasic variables are subtracted in the relation
          for the new basic variable)

        - ``constant`` -- the constant term for the new row

        - ``basic_variable`` -- (default: depends on :func:`style`)
          a string giving the name of the basic variable of the new row

        OUTPUT: a :class:`revised dictionary <LPRevisedDictionary>`

        EXAMPLES::

            sage: A = ([-1, 1111, 3, 17], [8, 222, 7, 6],
            ....: [3, 7, 17, 5], [9, 5, 7, 3])
            sage: b = (2, 17, 11, 27)
            sage: c = (5/133, 1/10, 1/18, 47/3)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.final_revised_dictionary()
            sage: D1 = D.add_row([7, 11, 13, 9], 42)
            sage: D1.row_coefficients("x9")
            (7, 11, 13, 9)
            sage: D1.constant_terms()[-1]
            42
            sage: D1.basic_variables()[-1]
            x9

            sage: A = ([-9, 7, 48, 31, 23], [5, 2, 9, 13, 98],
            ....: [14, 15, 97, 49, 1], [9, 5, 7, 3, 17],
            ....: [119, 7, 121, 5, 111])
            sage: b = (33, 27, 1, 272, 61)
            sage: c = (51/133, 1/100, 149/18, 47/37, 13/17)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary("x1", "x2", "x3", "x4", "x5")
            sage: D2 = D.add_row([5 ,7, 11, 13, 9], 99, basic_variable=\'c\')
            sage: D2.row_coefficients("c")
            (5, 7, 11, 13, 9)
            sage: D2.constant_terms()[-1]
            99
            sage: D2.basic_variables()[-1]
            c

            sage: D = P.revised_dictionary(0, 1, 2, 3, 4)
            sage: D.add_row([1, 2, 3, 4, 5, 6], 0)
            Traceback (most recent call last):
            ...
            ValueError: the sum of coefficients of nonbasic slack variables has
            to be equal to -1 when inserting a row into a dictionary for the
            auxiliary problem
            sage: D3 = D.add_row([1, 2, 3, 4, 5, -15], 0)
            sage: D3.row_coefficients(11)
            (1, 2, 3, 4, 5, -15)
        '''
    def basic_indices(self):
        """
        Return the basic indices of ``self``.

        .. NOTE::

            Basic indices are indices of :meth:`basic_variables` in the list of
            generators of the :meth:`~InteractiveLPProblemStandardForm.coordinate_ring` of
            the :meth:`problem` of ``self``, they may not coincide with the
            indices of variables which are parts of their names. (They will for
            the default indexed names.)

        OUTPUT: list

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.basic_indices()
            [3, 4]
        """
    def basic_variables(self):
        """
        Return the basic variables of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.basic_variables()
            (x3, x4)
        """
    def c_B(self):
        """
        Return the `c_B` vector, objective coefficients of basic variables.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary(1, 2)
            sage: D.c_B()
            (10, 5)
        """
    def c_N(self):
        """
        Return the `c_N` vector, objective coefficients of non-basic variables.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.c_N()
            (10, 5)
        """
    def column_coefficients(self, v):
        """
        Return the coefficients of a nonbasic variable.

        INPUT:

        - ``v`` -- a nonbasic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a variable

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.column_coefficients(1)
            (1, 3)
        """
    def constant_terms(self):
        """
        Return constant terms in the relations of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.constant_terms()
            (1000, 1500)
        """
    def dictionary(self):
        """
        Return a regular LP dictionary matching ``self``.

        OUTPUT: an :class:`LP dictionary <LPDictionary>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1], [-1, -1])
            sage: b = (1000, 1500, -400)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.dictionary()
            LP problem dictionary (use ...)
        """
    def nonbasic_indices(self):
        """
        Return the non-basic indices of ``self``.

        .. NOTE::

            Non-basic indices are indices of :meth:`nonbasic_variables` in the
            list of generators of the
            :meth:`~InteractiveLPProblemStandardForm.coordinate_ring` of the
            :meth:`problem` of ``self``, they may not coincide with the indices
            of variables which are parts of their names. (They will for the
            default indexed names.)

        OUTPUT: list

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.nonbasic_indices()
            [1, 2]
        """
    def nonbasic_variables(self):
        """
        Return non-basic variables of ``self``.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.nonbasic_variables()
            (x1, x2)
        """
    def objective_coefficients(self):
        """
        Return coefficients of the objective of ``self``.

        OUTPUT: a vector

        These are coefficients of non-basic variables when basic variables are
        eliminated.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.objective_coefficients()
            (10, 5)
        """
    def objective_name(self):
        """
        Return the objective name of ``self``.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.objective_name()
            z
        """
    def objective_value(self):
        """
        Return the value of the objective at the basic solution of ``self``.

        OUTPUT: a number

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.objective_value()
            0
        """
    def problem(self):
        """
        Return the original problem.

        OUTPUT: an :class:`LP problem in standard form <InteractiveLPProblemStandardForm>`

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.problem() is P
            True
        """
    def row_coefficients(self, v):
        '''
        Return the coefficients of the basic variable ``v``.

        These are the coefficients with which nonbasic variables are subtracted
        in the relation for ``v``.

        INPUT:

        - ``v`` -- a basic variable of ``self``, can be given as a string, an
          actual variable, or an integer interpreted as the index of a variable

        OUTPUT: a vector of coefficients of a basic variable

        EXAMPLES::

            sage: A = ([-1, 1], [8, 2])
            sage: b = (2, 17)
            sage: c = (55/10, 21/10)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.row_coefficients("x3")
            (-1, 1)

        We can also use indices of variables::

            sage: D.row_coefficients(3)
            (-1, 1)

        Or variable names without quotes after injecting them::

            sage: P.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: D.row_coefficients(x3)
            (-1, 1)
        '''
    def update(self) -> None:
        '''
        Update ``self`` using previously set entering and leaving variables.

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.objective_value()
            0
            sage: D.enter("x1")
            sage: D.leave("x4")
            sage: D.update()
            sage: D.objective_value()
            5000
        '''
    def y(self):
        """
        Return the `y` vector, the product of :meth:`c_B` and
        :meth:`B_inverse`.

        OUTPUT: a vector

        EXAMPLES::

            sage: A = ([1, 1], [3, 1])
            sage: b = (1000, 1500)
            sage: c = (10, 5)
            sage: P = InteractiveLPProblemStandardForm(A, b, c)
            sage: D = P.revised_dictionary()
            sage: D.y()
            (0, 0)
        """
    x_B = basic_variables
    x_N = nonbasic_variables
