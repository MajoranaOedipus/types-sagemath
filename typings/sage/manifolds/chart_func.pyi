from sage.categories.commutative_algebras import CommutativeAlgebras as CommutativeAlgebras
from sage.manifolds.utilities import ExpressionNice as ExpressionNice
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import AlgebraElement as AlgebraElement, ModuleElementWithMutability as ModuleElementWithMutability
from sage.structure.mutability import Mutability as Mutability
from sage.structure.parent import Parent as Parent
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.symbolic.ring import SR as SR
from typing import Self

class ChartFunction(AlgebraElement, ModuleElementWithMutability):
    '''
    Function of coordinates of a given chart.

    If `(U, \\varphi)` is a chart on a topological manifold `M` of
    dimension `n` over a topological field `K`,  a *chart function*
    associated to `(U, \\varphi)` is a map

    .. MATH::

        \\begin{array}{llcl}
        f:& V \\subset K^n & \\longrightarrow & K \\\\\n          & (x^1, \\ldots, x^n) & \\longmapsto & f(x^1, \\ldots, x^n),
        \\end{array}

    where `V` is the codomain of `\\varphi`. In other words, `f` is a
    `K`-valued function of the coordinates associated to the chart
    `(U, \\varphi)`.

    The chart function `f` can be represented by expressions pertaining to
    different calculus methods; the currently implemented ones are

    - ``SR`` (Sage\'s Symbolic Ring)
    - ``SymPy``

    See :meth:`~sage.manifolds.chart_func.ChartFunction.expr` for details.

    INPUT:

    - ``parent`` -- the algebra of chart functions on the chart
      `(U, \\varphi)`

    - ``expression`` -- (default: ``None``) a symbolic expression representing
      `f(x^1, \\ldots, x^n)`, where `(x^1, \\ldots, x^n)` are the
      coordinates of the chart `(U, \\varphi)`

    - ``calc_method`` -- string (default: ``None``); the calculus method with
      respect to which the internal expression of ``self`` must be initialized
      from ``expression``. One of

      - ``\'SR\'``: Sage\'s default symbolic engine (Symbolic Ring)
      - ``\'sympy\'``: SymPy
      - ``None``: the chart current calculus method is assumed

    - ``expansion_symbol`` -- (default: ``None``) symbolic variable (the "small
      parameter") with respect to which the coordinate expression is expanded
      in power series (around the zero value of this variable)

    - ``order`` -- integer (default: ``None``); the order of the expansion
      if ``expansion_symbol`` is not ``None``; the *order* is defined as the
      degree of the polynomial representing the truncated power series in
      ``expansion_symbol``

      .. WARNING::

         The value of ``order`` is `n-1`, where `n` is the order of the
         big `O` in the power series expansion

    EXAMPLES:

    A symbolic chart function on a 2-dimensional manifold::

        sage: M = Manifold(2, \'M\', structure=\'topological\')
        sage: X.<x,y> = M.chart()
        sage: f = X.function(x^2+3*y+1)
        sage: type(f)
        <class \'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class\'>
        sage: f.display()
        (x, y) ↦ x^2 + 3*y + 1
        sage: f(x,y)
        x^2 + 3*y + 1

    The symbolic expression is returned when asking for the direct display of
    the function::

        sage: f
        x^2 + 3*y + 1
        sage: latex(f)
        x^{2} + 3 \\, y + 1

    A similar output is obtained by means of the method :meth:`expr`::

        sage: f.expr()
        x^2 + 3*y + 1

    The expression returned by :meth:`expr` is by default a Sage symbolic
    expression::

        sage: type(f.expr())
        <class \'sage.symbolic.expression.Expression\'>

    A SymPy expression can also be asked for::

        sage: f.expr(\'sympy\')
        x**2 + 3*y + 1
        sage: type(f.expr(\'sympy\'))
        <class \'sympy.core.add.Add\'>

    The value of the function at specified coordinates is obtained by means
    of the standard parentheses notation::

        sage: f(2,-1)
        2
        sage: var(\'a b\')
        (a, b)
        sage: f(a,b)
        a^2 + 3*b + 1

    An unspecified chart function::

        sage: g = X.function(function(\'G\')(x, y))
        sage: g
        G(x, y)
        sage: g.display()
        (x, y) ↦ G(x, y)
        sage: g.expr()
        G(x, y)
        sage: g(2,3)
        G(2, 3)

    Coordinate functions can be compared to other values::

        sage: f = X.function(x^2+3*y+1)
        sage: f == 2
        False
        sage: f == x^2 + 3*y + 1
        True
        sage: g = X.function(x*y)
        sage: f == g
        False
        sage: h = X.function(x^2+3*y+1)
        sage: f == h
        True

    A coercion by means of the restriction is implemented::

        sage: D = M.open_subset(\'D\')
        sage: X_D = X.restrict(D, x^2+y^2<1)  # open disk
        sage: c = X_D.function(x^2)
        sage: c + f
        2*x^2 + 3*y + 1

    Expansion to a given order with respect to a small parameter::

        sage: t = var(\'t\')  # the small parameter
        sage: f = X.function(cos(t)*x*y, expansion_symbol=t, order=2)

    The expansion is triggered by the call to :meth:`simplify`::

        sage: f
        x*y*cos(t)
        sage: f.simplify()
        -1/2*t^2*x*y + x*y

    .. RUBRIC:: Differences between ``ChartFunction`` and callable
      symbolic expressions

    Callable symbolic expressions are defined directly from symbolic
    expressions of the coordinates::

        sage: f0(x,y) = x^2 + 3*y + 1
        sage: type(f0)
        <class \'sage.symbolic.expression.Expression\'>
        sage: f0
        (x, y) |--> x^2 + 3*y + 1
        sage: f0(x,y)
        x^2 + 3*y + 1

    To get an output similar to that of ``f0`` for a chart function, we must
    use the method :meth:`display`::

        sage: f = X.function(x^2+3*y+1)
        sage: f
        x^2 + 3*y + 1
        sage: f.display()
        (x, y) ↦ x^2 + 3*y + 1
        sage: f(x,y)
        x^2 + 3*y + 1

    More importantly, instances of :class:`ChartFunction` differ from
    callable symbolic expression by the automatic simplifications in all
    operations. For instance, adding the two callable symbolic expressions::

        sage: f0(x,y,z) = cos(x)^2 ; g0(x,y,z) = sin(x)^2

    results in::

        sage: f0 + g0
        (x, y, z) |--> cos(x)^2 + sin(x)^2

    To get `1`, one has to call
    :meth:`~sage.symbolic.expression.Expression.simplify_trig`::

        sage: (f0 + g0).simplify_trig()
        (x, y, z) |--> 1

    On the contrary, the sum of the corresponding :class:`ChartFunction`
    instances is automatically simplified (see
    :func:`~sage.manifolds.utilities.simplify_chain_real` and
    :func:`~sage.manifolds.utilities.simplify_chain_generic` for details)::

        sage: f = X.function(cos(x)^2) ; g = X.function(sin(x)^2)
        sage: f + g
        1

    Another difference regards the display of partial derivatives:
    for callable symbolic functions, it involves ``diff``::

        sage: g = function(\'g\')(x, y)
        sage: f0(x,y) = diff(g, x) + diff(g, y)
        sage: f0
        (x, y) |--> diff(g(x, y), x) + diff(g(x, y), y)

    while for chart functions, the display is more "textbook" like::

        sage: f = X.function(diff(g, x) + diff(g, y))
        sage: f
        d(g)/dx + d(g)/dy

    The difference is even more dramatic on LaTeX outputs::

        sage: latex(f0)
        \\left( x, y \\right) \\ {\\mapsto} \\ \\frac{\\partial}{\\partial x}g\\left(x, y\\right) + \\frac{\\partial}{\\partial y}g\\left(x, y\\right)
        sage: latex(f)
        \\frac{\\partial\\,g}{\\partial x} + \\frac{\\partial\\,g}{\\partial y}

    Note that this regards only the display of coordinate functions:
    internally, the ``diff`` notation is still used, as we can check by asking
    for the symbolic expression stored in ``f``::

        sage: f.expr()
        diff(g(x, y), x) + diff(g(x, y), y)

    One can switch to Pynac notation by changing the options::

        sage: Manifold.options.textbook_output=False
        sage: latex(f)
        \\frac{\\partial}{\\partial x}g\\left(x, y\\right) + \\frac{\\partial}{\\partial y}g\\left(x, y\\right)
        sage: Manifold.options._reset()
        sage: latex(f)
        \\frac{\\partial\\,g}{\\partial x} + \\frac{\\partial\\,g}{\\partial y}

    Another difference between :class:`ChartFunction` and
    callable symbolic expression is the possibility to switch off the display
    of the arguments of unspecified functions. Consider for instance::

        sage: f = X.function(function(\'u\')(x, y) * function(\'v\')(x, y))
        sage: f
        u(x, y)*v(x, y)
        sage: f0(x,y) = function(\'u\')(x, y) * function(\'v\')(x, y)
        sage: f0
        (x, y) |--> u(x, y)*v(x, y)

    If there is a clear understanding that `u` and `v` are functions of
    `(x,y)`, the explicit mention of the latter can be cumbersome in lengthy
    tensor expressions. We can switch it off by::

        sage: Manifold.options.omit_function_arguments=True
        sage: f
        u*v

    Note that neither the callable symbolic expression ``f0`` nor the internal
    expression of ``f`` is affected by the above command::

        sage: f0
        (x, y) |--> u(x, y)*v(x, y)
        sage: f.expr()
        u(x, y)*v(x, y)

    We revert to the default behavior by::

        sage: Manifold.options._reset()
        sage: f
        u(x, y)*v(x, y)

    .. automethod:: __call__
    '''
    def __init__(self, parent, expression=None, calc_method=None, expansion_symbol=None, order=None) -> None:
        """
        Initialize ``self``.

        TESTS:

        Chart function on a real manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^3+y); f
            x^3 + y
            sage: type(f)
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
            sage: TestSuite(f).run()

        Using SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f = X.function(x^3+y)
            sage: f
            x**3 + y
            sage: TestSuite(f).run()

        Chart function on a complex manifold::

            sage: N = Manifold(2, 'N', structure='topological', field='complex')
            sage: Y.<z,w> = N.chart()
            sage: g = Y.function(i*z + 2*w); g
            2*w + I*z
            sage: TestSuite(g).run()
        """
    def chart(self):
        """
        Return the chart with respect to which ``self`` is defined.

        OUTPUT: a :class:`~sage.manifolds.chart.Chart`

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(1+x+y^2)
            sage: f.chart()
            Chart (M, (x, y))
            sage: f.chart() is X
            True
        """
    def scalar_field(self, name=None, latex_name=None):
        """
        Construct the scalar field that has ``self`` as coordinate expression.

        The domain of the scalar field is the open subset covered by the
        chart on which ``self`` is defined.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the scalar field

        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          scalar field; if ``None``, the LaTeX symbol is set to ``name``

        OUTPUT: a :class:`~sage.manifolds.scalarfield.ScalarField`

        EXAMPLES:

        Construction of a scalar field on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: fc = c_xy.function(x+2*y^3)
            sage: f = fc.scalar_field() ; f
            Scalar field on the 2-dimensional topological manifold M
            sage: f.display()
            M → ℝ
            (x, y) ↦ 2*y^3 + x
            sage: f.coord_function(c_xy) is fc
            True
        """
    def expr(self, method=None):
        '''
        Return the symbolic expression of ``self`` in terms of the chart
        coordinates, as an object of a specified calculus method.

        INPUT:

        - ``method`` -- string (default: ``None``); the calculus method which
          the returned expression belongs to. One of

          - ``\'SR\'``: Sage\'s default symbolic engine (Symbolic Ring)
          - ``\'sympy\'``: SymPy
          - ``None``: the chart current calculus method is assumed

        OUTPUT:

        - a :class:`Sage symbolic expression <sage.symbolic.expression.Expression>`
          if ``method`` is ``\'SR\'``
        - a SymPy object if ``method`` is ``\'sympy\'``

        EXAMPLES:

        Chart function on a 2-dimensional manifold::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^2+y)
            sage: f.expr()
            x^2 + y
            sage: type(f.expr())
            <class \'sage.symbolic.expression.Expression\'>

        Asking for the SymPy expression::

            sage: f.expr(\'sympy\')
            x**2 + y
            sage: type(f.expr(\'sympy\'))
            <class \'sympy.core.add.Add\'>

        The default corresponds to the current calculus method, here the one
        based on the Symbolic Ring ``SR``::

            sage: f.expr() is f.expr(\'SR\')
            True

        If we change the current calculus method on chart ``X``, we change the
        default::

            sage: X.calculus_method().set(\'sympy\')
            sage: f.expr()
            x**2 + y
            sage: f.expr() is f.expr(\'sympy\')
            True
            sage: X.calculus_method().set(\'SR\')  # revert back to SR

        Internally, the expressions corresponding to various calculus methods
        are stored in the dictionary ``_express``::

            sage: for method in sorted(f._express):
            ....:     print("\'{}\': {}".format(method, f._express[method]))
            ....:
            \'SR\': x^2 + y
            \'sympy\': x**2 + y

        The method :meth:`expr` is useful for accessing to all the
        symbolic expression functionalities in Sage; for instance::

            sage: var(\'a\')
            a
            sage: f = X.function(a*x*y); f.display()
            (x, y) ↦ a*x*y
            sage: f.expr()
            a*x*y
            sage: f.expr().subs(a=2)
            2*x*y

        Note that for substituting the value of a coordinate, the function
        call can be used as well::

            sage: f(x,3)
            3*a*x
            sage: bool( f(x,3) == f.expr().subs(y=3) )
            True
        '''
    def set_expr(self, calc_method, expression) -> None:
        """
        Add an expression in a particular calculus method  ``self``.
        Some control is done to verify the consistency between the
        different representations of the same expression.

        INPUT:

        - ``calc_method`` -- calculus method

        - ``expression`` -- symbolic expression

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(1+x^2)
            sage: f._repr_()
            'x^2 + 1'
            sage: f.set_expr('sympy','x**2+1')
            sage: f  # indirect doctest
            x^2 + 1

            sage: g = X.function(1+x^3)
            sage: g._repr_()
            'x^3 + 1'
            sage: g.set_expr('sympy','x**2+y')
            Traceback (most recent call last):
            ...
            ValueError: Expressions are not equal
        """
    def display(self):
        """
        Display ``self`` in arrow notation.
        For display the standard ``SR`` representation is used.

        The output is either text-formatted (console mode) or
        LaTeX-formatted (notebook mode).

        EXAMPLES:

        Coordinate function on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(cos(x*y/2))
            sage: f.display()
            (x, y) ↦ cos(1/2*x*y)
            sage: latex(f.display())
            \\left(x, y\\right) \\mapsto \\cos\\left(\\frac{1}{2} \\, x y\\right)

        A shortcut is ``disp()``::

            sage: f.disp()
            (x, y) ↦ cos(1/2*x*y)

        Display of the zero function::

            sage: X.zero_function().display()
            (x, y) ↦ 0
        """
    disp = display
    def __call__(self, *coords, **options):
        """
        Compute the value of the function at specified coordinates.

        INPUT:

        - ``*coords`` -- list of coordinates `(x^1, \\ldots, x^n)`,
          where the function `f` is to be evaluated
        - ``**options`` -- allows to pass ``simplify=False`` to disable the
          call of the simplification chain on the result

        OUTPUT:

        - the value `f(x^1, \\ldots, x^n)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(sin(x*y))
            sage: f.__call__(-2, 3)
            -sin(6)
            sage: f(-2, 3)
            -sin(6)
            sage: var('a b')
            (a, b)
            sage: f.__call__(a, b)
            sin(a*b)
            sage: f(a,b)
            sin(a*b)
            sage: f.__call__(pi, 1)
            0
            sage: f.__call__(pi, 1/2)
            1

        With SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f(-2,3)
            -sin(6)
            sage: type(f(-2,3))
            <class 'sympy.core.mul.Mul'>
            sage: f(a,b)
            sin(a*b)
            sage: type(f(a,b))
            sin
            sage: type(f(pi,1))
            <class 'sympy.core.numbers.Zero'>
            sage: f(pi, 1/2)
            1
            sage: type(f(pi, 1/2))
            <class 'sympy.core.numbers.One'>
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if ``self`` is nonzero and ``False`` otherwise.

        This method is called by :meth:`~sage.structure.element.Element.is_zero()`.

        EXAMPLES:

        Coordinate functions associated to a 2-dimensional chart::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^2+3*y+1)
            sage: bool(f)
            True
            sage: f.is_zero()
            False
            sage: f == 0
            False
            sage: g = X.function(0)
            sage: bool(g)
            False
            sage: g.is_zero()
            True
            sage: X.calculus_method().set('sympy')
            sage: g.is_zero()
            True
            sage: g == 0
            True
            sage: X.zero_function().is_zero()
            True
            sage: X.zero_function() == 0
            True
        """
    def is_trivial_zero(self):
        """
        Check if ``self`` is trivially equal to zero without any
        simplification.

        This method is supposed to be fast as compared with
        ``self.is_zero()`` or ``self == 0`` and is intended to be
        used in library code where trying to obtain a mathematically
        correct result by applying potentially expensive rewrite rules
        is not desirable.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(0)
            sage: f.is_trivial_zero()
            True
            sage: f = X.function(float(0.0))
            sage: f.is_trivial_zero()
            True
            sage: f = X.function(x-x)
            sage: f.is_trivial_zero()
            True
            sage: X.zero_function().is_trivial_zero()
            True

        No simplification is attempted, so that ``False`` is returned for
        non-trivial cases::

            sage: f = X.function(cos(x)^2 + sin(x)^2 - 1)
            sage: f.is_trivial_zero()
            False

        On the contrary, the method
        :meth:`~sage.structure.element.Element.is_zero` and the direct
        comparison to zero involve some simplification algorithms and
        return ``True``::

            sage: f.is_zero()
            True
            sage: f == 0
            True
        """
    def is_trivial_one(self):
        """
        Check if ``self`` is trivially equal to one without any
        simplification.

        This method is supposed to be fast as compared with
        ``self == 1`` and is intended to be used in library code where
        trying to obtain a mathematically correct result by applying
        potentially expensive rewrite rules is not desirable.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(1)
            sage: f.is_trivial_one()
            True
            sage: f = X.function(float(1.0))
            sage: f.is_trivial_one()
            True
            sage: f = X.function(x-x+1)
            sage: f.is_trivial_one()
            True
            sage: X.one_function().is_trivial_one()
            True

        No simplification is attempted, so that ``False`` is returned for
        non-trivial cases::

            sage: f = X.function(cos(x)^2 + sin(x)^2)
            sage: f.is_trivial_one()
            False

        On the contrary, the method
        :meth:`~sage.structure.element.Element.is_zero` and the direct
        comparison to one involve some simplification algorithms and
        return ``True``::

            sage: (f - 1).is_zero()
            True
            sage: f == 1
            True
        """
    def is_unit(self):
        """
        Return ``True`` iff ``self`` is not trivially zero since most chart
        functions are invertible and an actual computation would take too much
        time.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^2+3*y+1)
            sage: f.is_unit()
            True
            sage: zero = X.function(0)
            sage: zero.is_unit()
            False
        """
    def copy(self):
        """
        Return an exact copy of the object.

        OUTPUT: a :class:`ChartFunctionSymb`

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x+y^2)
            sage: g = f.copy(); g
            y^2 + x

        By construction, ``g`` is identical to ``f``::

            sage: type(g) == type(f)
            True
            sage: g == f
            True

        but it is not the same object::

            sage: g is f
            False
        """
    def derivative(self, coord):
        """
        Partial derivative with respect to a coordinate.

        INPUT:

        - ``coord`` -- either the coordinate `x^i` with respect
          to which the derivative of the chart function `f` is to be
          taken, or the index `i` labelling this coordinate (with the
          index convention defined on the chart domain via the parameter
          ``start_index``)

        OUTPUT:

        - a :class:`ChartFunction` representing the partial
          derivative `\\frac{\\partial f}{\\partial x^i}`

        EXAMPLES:

        Partial derivatives of a 2-dimensional chart function::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart(calc_method='SR')
            sage: f = X.function(x^2+3*y+1); f
            x^2 + 3*y + 1
            sage: f.derivative(x)
            2*x
            sage: f.derivative(y)
            3

        An alias is ``diff``::

            sage: f.diff(x)
            2*x

        Each partial derivative is itself a chart function::

            sage: type(f.diff(x))
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>

        The same result is returned by the function ``diff``::

            sage: diff(f, x)
            2*x

        An index can be used instead of the coordinate symbol::

            sage: f.diff(0)
            2*x
            sage: diff(f, 1)
            3

        The index range depends on the convention used on the chart's domain::

            sage: M = Manifold(2, 'M', structure='topological', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^2+3*y+1)
            sage: f.diff(0)
            Traceback (most recent call last):
            ...
            ValueError: coordinate index out of range
            sage: f.diff(1)
            2*x
            sage: f.diff(2)
            3

        The same test with SymPy::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart(calc_method='sympy')
            sage: f = X.function(x^2+3*y+1); f
            x**2 + 3*y + 1
            sage: f.diff(x)
            2*x
            sage: f.diff(y)
            3
        """
    diff = derivative
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- a :class:`ChartFunction` or a value

        OUTPUT: ``True`` if ``self`` is equal to ``other``,  or ``False`` otherwise

        TESTS:

        Coordinate functions associated to a 2-dimensional chart::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x+y^2)
            sage: g = X.function(x+y^2)
            sage: f == g
            True
            sage: f = X.function(x+y^2)
            sage: g = X.function(x+y**2,'sympy')
            sage: f._express; g._express
            {'SR': y^2 + x}
            {'sympy': x + y**2}
            sage: f == g
            True
            sage: f == 1
            False
            sage: h = X.function(1)
            sage: h == 1
            True
            sage: h == f
            False
            sage: h == 0
            False
            sage: X.function(0) == 0
            True
            sage: X.zero_function() == 0
            True
        """
    def __ne__(self, other):
        """
        Inequality operator.

        INPUT:

        - ``other`` -- a :class:`ChartFunction`

        OUTPUT:

        - ``True`` if ``self`` is different from ``other``, ``False``
          otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x-y)
            sage: f != X.function(x*y)
            True
            sage: f != X.function(x)
            True
            sage: f != X.function(x-y)
            False
        """
    def __neg__(self):
        """
        Unary minus operator.

        OUTPUT: the opposite of ``self``

        TESTS:

        Coordinate functions associated to a 2-dimensional chart::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart(calc_method='sympy')
            sage: f = X.function(x+y^2)
            sage: g = -f; g
            -x - y**2
            sage: type(g)
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
            sage: -g == f
            True
        """
    def __invert__(self):
        """
        Inverse operator.

        If `f` denotes the current chart function and `K` the topological
        field over which the manifold is defined, the *inverse* of `f` is the
        chart function `1/f`, where `1` of the multiplicative identity
        of `K`.

        OUTPUT: the inverse of ``self``

        TESTS:

        Coordinate functions associated to a 2-dimensional chart::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(1+x^2+y^2)
            sage: g = f.__invert__(); g
            1/(x^2 + y^2 + 1)
            sage: type(g)
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
            sage: g == ~f
            True
            sage: g.__invert__() == f
            True

        The same test with SymPy::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart(calc_method='sympy')
            sage: f = X.function(1+x^2+y^2)
            sage: g = f.__invert__(); g
            1/(x**2 + y**2 + 1)
            sage: type(g)
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
            sage: g == ~f
            True
            sage: g.__invert__() == f
            True
        """
    def exp(self):
        """
        Exponential of ``self``.

        OUTPUT:

        - chart function `\\exp(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x+y)
            sage: f.exp()
            e^(x + y)
            sage: exp(f) # equivalent to f.exp()
            e^(x + y)
            sage: exp(f).display()
            (x, y) ↦ e^(x + y)
            sage: exp(X.zero_function())
            1

        The same test with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f = X.function(x+y)
            sage: f.exp()
            exp(x + y)
            sage: exp(f) # equivalent to f.exp()
            exp(x + y)
            sage: exp(f).display()
            (x, y) ↦ exp(x + y)
            sage: exp(X.zero_function())
            1
        """
    def log(self, base=None):
        """
        Logarithm of ``self``.

        INPUT:

        - ``base`` -- (default: ``None``) base of the logarithm; if ``None``,
          the natural logarithm (i.e. logarithm to base `e`) is returned

        OUTPUT:

        - chart function `\\log_a(f)`, where `f` is the current chart
          function and `a` is the base

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x+y)
            sage: f.log()
            log(x + y)
            sage: log(f) # equivalent to f.log()
            log(x + y)
            sage: log(f).display()
            (x, y) ↦ log(x + y)
            sage: f.log(2)
            log(x + y)/log(2)
            sage: log(f, 2)
            log(x + y)/log(2)

        The same test with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f = X.function(x+y)
            sage: f.log()
            log(x + y)
            sage: log(f) # equivalent to f.log()
            log(x + y)
            sage: log(f).display()
            (x, y) ↦ log(x + y)
            sage: f.log(2)
            log(x + y)/log(2)
            sage: log(f, 2)
            log(x + y)/log(2)
        """
    def __pow__(self, exponent):
        """
        Power of ``self``.

        INPUT:

        - ``exponent`` -- the exponent

        OUTPUT:

        - chart function `f^a`, where `f` is the current chart
          function and `a` is the exponent

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x+y)
            sage: f.__pow__(3)
            x^3 + 3*x^2*y + 3*x*y^2 + y^3
            sage: f^3  # equivalent to f.__pow__(3)
            x^3 + 3*x^2*y + 3*x*y^2 + y^3
            sage: f.__pow__(3).display()
            (x, y) ↦ x^3 + 3*x^2*y + 3*x*y^2 + y^3
            sage: pow(f,3).display()
            (x, y) ↦ x^3 + 3*x^2*y + 3*x*y^2 + y^3
            sage: (f^3).display()
            (x, y) ↦ x^3 + 3*x^2*y + 3*x*y^2 + y^3
            sage: pow(X.zero_function(), 3).display()
            (x, y) ↦ 0

        The same test with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f = X.function(x+y)
            sage: f.__pow__(3)
            x**3 + 3*x**2*y + 3*x*y**2 + y**3
            sage: f^3  # equivalent to f.__pow__(3)
            x**3 + 3*x**2*y + 3*x*y**2 + y**3
            sage: f.__pow__(3).display()
            (x, y) ↦ x**3 + 3*x**2*y + 3*x*y**2 + y**3
            sage: pow(f,3).display()
            (x, y) ↦ x**3 + 3*x**2*y + 3*x*y**2 + y**3
            sage: (f^3).display()
            (x, y) ↦ x**3 + 3*x**2*y + 3*x*y**2 + y**3
            sage: pow(X.zero_function(), 3).display()
            (x, y) ↦ 0
        """
    def sqrt(self):
        """
        Square root of ``self``.

        OUTPUT:

        - chart function `\\sqrt{f}`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x+y)
            sage: f.sqrt()
            sqrt(x + y)
            sage: sqrt(f)  # equivalent to f.sqrt()
            sqrt(x + y)
            sage: sqrt(f).display()
            (x, y) ↦ sqrt(x + y)
            sage: sqrt(X.zero_function()).display()
            (x, y) ↦ 0
        """
    def cos(self):
        """
        Cosine of ``self``.

        OUTPUT:

        - chart function `\\cos(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.cos()
            cos(x*y)
            sage: cos(f)  # equivalent to f.cos()
            cos(x*y)
            sage: cos(f).display()
            (x, y) ↦ cos(x*y)
            sage: cos(X.zero_function()).display()
            (x, y) ↦ 1

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.cos()
            cos(x*y)
            sage: cos(f)  # equivalent to f.cos()
            cos(x*y)
        """
    def sin(self):
        """
        Sine of ``self``.

        OUTPUT:

        - chart function `\\sin(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.sin()
            sin(x*y)
            sage: sin(f)  # equivalent to f.sin()
            sin(x*y)
            sage: sin(f).display()
            (x, y) ↦ sin(x*y)
            sage: sin(X.zero_function()) == X.zero_function()
            True
            sage: f = X.function(2-cos(x)^2+y)
            sage: g = X.function(-sin(x)^2+y)
            sage: (f+g).simplify()
            2*y + 1

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f = X.function(x*y)
            sage: f.sin()
            sin(x*y)
            sage: sin(f)  # equivalent to f.sin()
            sin(x*y)
        """
    def tan(self):
        """
        Tangent of ``self``.

        OUTPUT:

        - chart function `\\tan(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.tan()
            sin(x*y)/cos(x*y)
            sage: tan(f)  # equivalent to f.tan()
            sin(x*y)/cos(x*y)
            sage: tan(f).display()
            (x, y) ↦ sin(x*y)/cos(x*y)
            sage: tan(X.zero_function()) == X.zero_function()
            True

        The same test with SymPy::

            sage: M.set_calculus_method('sympy')
            sage: g = X.function(x*y)
            sage: g.tan()
            tan(x*y)
            sage: tan(g)  # equivalent to g.tan()
            tan(x*y)
            sage: tan(g).display()
            (x, y) ↦ tan(x*y)
        """
    def arccos(self):
        """
        Arc cosine of ``self``.

        OUTPUT:

        - chart function `\\arccos(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.arccos()
            arccos(x*y)
            sage: arccos(f)  # equivalent to f.arccos()
            arccos(x*y)
            sage: acos(f)  # equivalent to f.arccos()
            arccos(x*y)
            sage: arccos(f).display()
            (x, y) ↦ arccos(x*y)
            sage: arccos(X.zero_function()).display()
            (x, y) ↦ 1/2*pi

        The same test with SymPy::

            sage: M.set_calculus_method('sympy')
            sage: f = X.function(x*y)
            sage: f.arccos()
            acos(x*y)
            sage: arccos(f)  # equivalent to f.arccos()
            acos(x*y)
            sage: acos(f)  # equivalent to f.arccos()
            acos(x*y)
            sage: arccos(f).display()
            (x, y) ↦ acos(x*y)
        """
    def arcsin(self):
        """
        Arc sine of ``self``.

        OUTPUT:

        - chart function `\\arcsin(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.arcsin()
            arcsin(x*y)
            sage: arcsin(f)  # equivalent to f.arcsin()
            arcsin(x*y)
            sage: asin(f)  # equivalent to f.arcsin()
            arcsin(x*y)
            sage: arcsin(f).display()
            (x, y) ↦ arcsin(x*y)
            sage: arcsin(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.arcsin()
            asin(x*y)
            sage: arcsin(f)  # equivalent to f.arcsin()
            asin(x*y)
            sage: asin(f)  # equivalent to f.arcsin()
            asin(x*y)
        """
    def arctan(self):
        """
        Arc tangent of ``self``.

        OUTPUT:

        - chart function `\\arctan(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.arctan()
            arctan(x*y)
            sage: arctan(f)  # equivalent to f.arctan()
            arctan(x*y)
            sage: atan(f)  # equivalent to f.arctan()
            arctan(x*y)
            sage: arctan(f).display()
            (x, y) ↦ arctan(x*y)
            sage: arctan(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.arctan()
            atan(x*y)
            sage: arctan(f)  # equivalent to f.arctan()
            atan(x*y)
            sage: atan(f)  # equivalent to f.arctan()
            atan(x*y)
        """
    def cosh(self):
        """
        Hyperbolic cosine of ``self``.

        OUTPUT:

        - chart function `\\cosh(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.cosh()
            cosh(x*y)
            sage: cosh(f)  # equivalent to f.cosh()
            cosh(x*y)
            sage: cosh(f).display()
            (x, y) ↦ cosh(x*y)
            sage: cosh(X.zero_function()).display()
            (x, y) ↦ 1

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.cosh()
            cosh(x*y)
            sage: cosh(f)  # equivalent to f.cosh()
            cosh(x*y)
        """
    def sinh(self):
        """
        Hyperbolic sine of ``self``.

        OUTPUT:

        - chart function `\\sinh(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.sinh()
            sinh(x*y)
            sage: sinh(f)  # equivalent to f.sinh()
            sinh(x*y)
            sage: sinh(f).display()
            (x, y) ↦ sinh(x*y)
            sage: sinh(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.sinh()
            sinh(x*y)
            sage: sinh(f)  # equivalent to f.sinh()
            sinh(x*y)
        """
    def tanh(self):
        """
        Hyperbolic tangent of ``self``.

        OUTPUT:

        - chart function `\\tanh(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.tanh()
            sinh(x*y)/cosh(x*y)
            sage: tanh(f)  # equivalent to f.tanh()
            sinh(x*y)/cosh(x*y)
            sage: tanh(f).display()
            (x, y) ↦ sinh(x*y)/cosh(x*y)
            sage: tanh(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.tanh()
            tanh(x*y)
            sage: tanh(f)  # equivalent to f.tanh()
            tanh(x*y)
        """
    def arccosh(self):
        """
        Inverse hyperbolic cosine of ``self``.

        OUTPUT:

        - chart function `\\mathrm{arccosh}(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.arccosh()
            arccosh(x*y)
            sage: arccosh(f)  # equivalent to f.arccosh()
            arccosh(x*y)
            sage: acosh(f)  # equivalent to f.arccosh()
            arccosh(x*y)
            sage: arccosh(f).display()
            (x, y) ↦ arccosh(x*y)
            sage: arccosh(X.function(1)) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.arccosh()
            acosh(x*y)
            sage: arccosh(f)  # equivalent to f.arccosh()
            acosh(x*y)
            sage: acosh(f)  # equivalent to f.arccosh()
            acosh(x*y)
        """
    def arcsinh(self):
        """
        Inverse hyperbolic sine of ``self``.

        OUTPUT:

        - chart function `\\mathrm{arcsinh}(f)`, where `f` is the current
          chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.arcsinh()
            arcsinh(x*y)
            sage: arcsinh(f)  # equivalent to f.arcsinh()
            arcsinh(x*y)
            sage: asinh(f)  # equivalent to f.arcsinh()
            arcsinh(x*y)
            sage: arcsinh(f).display()
            (x, y) ↦ arcsinh(x*y)
            sage: arcsinh(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.arcsinh()
            asinh(x*y)
            sage: arcsinh(f)  # equivalent to f.arcsinh()
            asinh(x*y)
            sage: asinh(f)  # equivalent to f.arcsinh()
            asinh(x*y)
        """
    def arctanh(self):
        """
        Inverse hyperbolic tangent of ``self``.

        OUTPUT:

        - chart function `\\mathrm{arctanh}(f)`, where `f` is the
          current chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.arctanh()
            arctanh(x*y)
            sage: arctanh(f)  # equivalent to f.arctanh()
            arctanh(x*y)
            sage: atanh(f)  # equivalent to f.arctanh()
            arctanh(x*y)
            sage: arctanh(f).display()
            (x, y) ↦ arctanh(x*y)
            sage: arctanh(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.arctanh()
            atanh(x*y)
            sage: arctanh(f)  # equivalent to f.arctanh()
            atanh(x*y)
            sage: atanh(f)  # equivalent to f.arctanh()
            atanh(x*y)
        """
    def __abs__(self):
        """
        Absolute value of ``self``.

        OUTPUT:

        - chart function `\\mathrm{abs}(f)`, where `f` is the
          current chart function

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x*y)
            sage: f.abs()
            abs(x)*abs(y)
            sage: abs(f)  # equivalent to f.abs()
            abs(x)*abs(y)
            sage: abs(f).display()
            (x, y) ↦ abs(x)*abs(y)
            sage: abs(X.zero_function()) == X.zero_function()
            True

        The same tests with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: f.abs()
            Abs(x*y)
            sage: abs(f)  # equivalent to f.abs()
            Abs(x*y)
        """
    def simplify(self) -> Self:
        """
        Simplify the coordinate expression of ``self``.

        For details about the employed chain of simplifications for the ``SR``
        calculus method, see
        :func:`~sage.manifolds.utilities.simplify_chain_real` for chart
        functions on real manifolds and
        :func:`~sage.manifolds.utilities.simplify_chain_generic` for the
        generic case.

        If ``self`` has been defined with the small parameter
        ``expansion_symbol`` and some truncation order, the coordinate
        expression of ``self`` will be expanded in power series of that
        parameter and truncated to the given order.

        OUTPUT: ``self`` with its coordinate expression simplified

        EXAMPLES:

        Simplification of a chart function on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(cos(x)^2 + sin(x)^2 + sqrt(x^2))
            sage: f.display()
            (x, y) ↦ cos(x)^2 + sin(x)^2 + abs(x)
            sage: f.simplify()
            abs(x) + 1

        The method ``simplify()`` has changed the expression of ``f``::

            sage: f.display()
            (x, y) ↦ abs(x) + 1

        Another example::

            sage: f = X.function((x^2-1)/(x+1)); f
            (x^2 - 1)/(x + 1)
            sage: f.simplify()
            x - 1

        Examples taking into account the declared range of a coordinate::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart('x:(1,+oo) y')
            sage: f = X.function(sqrt(x^2-2*x+1)); f
            sqrt(x^2 - 2*x + 1)
            sage: f.simplify()
            x - 1

        ::

            sage: forget()  # to clear the previous assumption on x
            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart('x:(-oo,0) y')
            sage: f = X.function(sqrt(x^2-2*x+1)); f
            sqrt(x^2 - 2*x + 1)
            sage: f.simplify()
            -x + 1

        The same tests with SymPy::

            sage: forget()  # to clear the previous assumption on x
            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart(calc_method='sympy')
            sage: f = X.function(cos(x)^2 + sin(x)^2 + sqrt(x^2)); f
            sin(x)**2 + cos(x)**2 + Abs(x)
            sage: f.simplify()
            Abs(x) + 1

        ::

            sage: f = X.function((x^2-1)/(x+1)); f
            (x**2 - 1)/(x + 1)
            sage: f.simplify()
            x - 1

        ::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart('x:(1,+oo) y', calc_method='sympy')
            sage: f = X.function(sqrt(x^2-2*x+1)); f
            sqrt(x**2 - 2*x + 1)
            sage: f.simplify()
            x - 1

        ::

            sage: forget()  # to clear the previous assumption on x
            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart('x:(-oo,0) y', calc_method='sympy')
            sage: f = X.function(sqrt(x^2-2*x+1)); f
            sqrt(x**2 - 2*x + 1)
            sage: f.simplify()
            1 - x

        Power series expansion with respect to a small parameter `t` (at
        the moment, this is implemented only for the ``SR`` calculus backend,
        hence the first line below)::

            sage: X.calculus_method().set('SR')
            sage: t = var('t')
            sage: f = X.function(exp(t*x), expansion_symbol=t, order=3)

        At this stage, `f` is not expanded in power series::

            sage: f
            e^(t*x)

        Invoking ``simplify()`` triggers the expansion to the given order::

            sage: f.simplify()
            1/6*t^3*x^3 + 1/2*t^2*x^2 + t*x + 1
            sage: f.display()
            (x, y) ↦ 1/6*t^3*x^3 + 1/2*t^2*x^2 + t*x + 1
        """
    def factor(self) -> Self:
        """
        Factorize the coordinate expression of ``self``.

        OUTPUT: ``self`` with its expression factorized

        EXAMPLES:

        Factorization of a 2-dimensional chart function::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^2 + 2*x*y + y^2)
            sage: f.display()
            (x, y) ↦ x^2 + 2*x*y + y^2
            sage: f.factor()
            (x + y)^2

        The method ``factor()`` has changed the expression of ``f``::

            sage: f.display()
            (x, y) ↦ (x + y)^2

        The same test with SymPy ::

            sage: X.calculus_method().set('sympy')
            sage: g = X.function(x^2 + 2*x*y + y^2)
            sage: g.display()
            (x, y) ↦ x**2 + 2*x*y + y**2
            sage: g.factor()
            (x + y)**2
        """
    def expand(self) -> Self:
        """
        Expand the coordinate expression of ``self``.

        OUTPUT: ``self`` with its expression expanded

        EXAMPLES:

        Expanding a 2-dimensional chart function::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function((x - y)^2)
            sage: f.display()
            (x, y) ↦ (x - y)^2
            sage: f.expand()
            x^2 - 2*x*y + y^2

        The method ``expand()`` has changed the expression of ``f``::

            sage: f.display()
            (x, y) ↦ x^2 - 2*x*y + y^2

        The same test with SymPy ::

            sage: X.calculus_method().set('sympy')
            sage: g = X.function((x - y)^2)
            sage: g.expand()
            x**2 - 2*x*y + y**2
        """
    def collect(self, s) -> Self:
        """
        Collect the coefficients of `s` in the expression of ``self``
        into a group.

        INPUT:

        - ``s`` -- the symbol whose coefficients will be collected

        OUTPUT:

        - ``self`` with the coefficients of ``s`` grouped in
          its expression

        EXAMPLES:

        Action on a 2-dimensional chart function::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x^2*y + x*y + (x*y)^2)
            sage: f.display()
            (x, y) ↦ x^2*y^2 + x^2*y + x*y
            sage: f.collect(y)
            x^2*y^2 + (x^2 + x)*y

        The method ``collect()`` has changed the expression of ``f``::

            sage: f.display()
            (x, y) ↦ x^2*y^2 + (x^2 + x)*y

        The same test with SymPy ::

            sage: X.calculus_method().set('sympy')
            sage: f = X.function(x^2*y + x*y + (x*y)^2)
            sage: f.display()
            (x, y) ↦ x**2*y**2 + x**2*y + x*y
            sage: f.collect(y)
            x**2*y**2 + y*(x**2 + x)
        """
    def collect_common_factors(self) -> Self:
        """
        Collect common factors in the expression of ``self``.

        This method does not perform a full factorization but only looks
        for factors which are already explicitly present.

        OUTPUT:

        - ``self`` with the common factors collected in
          its expression

        EXAMPLES:

        Action on a 2-dimensional chart function::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.function(x/(x^2*y + x*y))
            sage: f.display()
            (x, y) ↦ x/(x^2*y + x*y)
            sage: f.collect_common_factors()
            1/((x + 1)*y)

        The method ``collect_common_factors()`` has changed the expression
        of ``f``::

            sage: f.display()
            (x, y) ↦ 1/((x + 1)*y)

        The same test with SymPy::

            sage: X.calculus_method().set('sympy')
            sage: g = X.function(x/(x^2*y + x*y))
            sage: g.display()
            (x, y) ↦ x/(x**2*y + x*y)
            sage: g.collect_common_factors()
            1/(y*(x + 1))
        """

class ChartFunctionRing(Parent, UniqueRepresentation):
    """
    Ring of all chart functions on a chart.

    INPUT:

    - ``chart`` -- a coordinate chart, as an instance of class
      :class:`~sage.manifolds.chart.Chart`

    EXAMPLES:

    The ring of all chart functions w.r.t. to a chart::

        sage: M = Manifold(2, 'M', structure='topological')
        sage: X.<x,y> = M.chart()
        sage: FR = X.function_ring(); FR
        Ring of chart functions on Chart (M, (x, y))
        sage: type(FR)
        <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category'>
        sage: FR.category()
        Category of commutative algebras over Symbolic Ring

    Coercions by means of restrictions are implemented::

        sage: FR_X = X.function_ring()
        sage: D = M.open_subset('D')
        sage: X_D = X.restrict(D, x^2+y^2<1)  # open disk
        sage: FR_X_D = X_D.function_ring()
        sage: FR_X_D.has_coerce_map_from(FR_X)
        True

    But only if the charts are compatible::

        sage: Y.<t,z> = D.chart()
        sage: FR_Y = Y.function_ring()
        sage: FR_Y.has_coerce_map_from(FR_X)
        False
    """
    Element = ChartFunction
    def __init__(self, chart) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: FR = X.function_ring()
            sage: TestSuite(FR).run()
        """
    def is_integral_domain(self, proof: bool = True):
        """
        Return ``False`` as ``self`` is not an integral domain.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: FR = X.function_ring()
            sage: FR.is_integral_domain()
            False
            sage: FR.is_field()
            False
        """
    @cached_method
    def zero(self):
        """
        Return the constant function `0` in ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: FR = X.function_ring()
            sage: FR.zero()
            0

            sage: M = Manifold(2, 'M', structure='topological', field=Qp(5))
            sage: X.<x,y> = M.chart()
            sage: X.function_ring().zero()
            0
        """
    @cached_method
    def one(self):
        """
        Return the constant function `1` in ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: FR = X.function_ring()
            sage: FR.one()
            1

            sage: M = Manifold(2, 'M', structure='topological', field=Qp(5))
            sage: X.<x,y> = M.chart()
            sage: X.function_ring().one()
            1 + O(5^20)
        """
    is_field = is_integral_domain

class MultiCoordFunction(SageObject, Mutability):
    """
    Coordinate function to some Cartesian power of the base field.

    If `n` and `m` are two positive integers and `(U, \\varphi)` is a chart on
    a topological manifold `M` of dimension `n` over a topological field `K`,
    a *multi-coordinate function* associated to `(U, \\varphi)` is a map

    .. MATH::

        \\begin{array}{llcl}
        f:& V \\subset K^n & \\longrightarrow & K^m \\\\\n          & (x^1, \\ldots, x^n) & \\longmapsto & (f_1(x^1, \\ldots, x^n),
            \\ldots, f_m(x^1, \\ldots, x^n)),
        \\end{array}

    where `V` is the codomain of `\\varphi`. In other words, `f` is a
    `K^m`-valued function of the coordinates associated to the chart
    `(U, \\varphi)`. Each component `f_i` (`1 \\leq i \\leq m`) is a coordinate
    function and is therefore stored as a
    :class:`~sage.manifolds.chart_func.ChartFunction`.

    INPUT:

    - ``chart`` -- the chart `(U, \\varphi)`
    - ``expressions`` -- list (or tuple) of length `m` of elements to
      construct the coordinate functions `f_i` (`1 \\leq i \\leq m`); for
      symbolic coordinate functions, this must be symbolic expressions
      involving the chart coordinates, while for numerical coordinate
      functions, this must be data file names

    EXAMPLES:

    A function `f: V \\subset \\RR^2 \\longrightarrow \\RR^3`::

        sage: forget()  # to clear the previous assumption on x
        sage: M = Manifold(2, 'M', structure='topological')
        sage: X.<x,y> = M.chart()
        sage: f = X.multifunction(x-y, x*y, cos(x)*exp(y)); f
        Coordinate functions (x - y, x*y, cos(x)*e^y) on the Chart (M, (x, y))
        sage: type(f)
        <class 'sage.manifolds.chart_func.MultiCoordFunction'>
        sage: f(x,y)
        (x - y, x*y, cos(x)*e^y)
        sage: latex(f)
        \\left(x - y, x y, \\cos\\left(x\\right) e^{y}\\right)

    Each real-valued function `f_i` (`1 \\leq i \\leq m`) composing `f` can
    be accessed via the square-bracket operator, by providing `i-1` as an
    argument::

        sage: f[0]
        x - y
        sage: f[1]
        x*y
        sage: f[2]
        cos(x)*e^y

    We can give a more verbose explanation of each function::

        sage: f[0].display()
        (x, y) ↦ x - y

    Each ``f[i-1]`` is an instance of
    :class:`~sage.manifolds.chart_func.ChartFunction`::

        sage: isinstance(f[0], sage.manifolds.chart_func.ChartFunction)
        True

    A class :class:`MultiCoordFunction` can represent a
    real-valued function (case `m = 1`), although one should
    rather employ the class :class:`~sage.manifolds.chart_func.ChartFunction`
    for this purpose::

        sage: g = X.multifunction(x*y^2)
        sage: g(x,y)
        (x*y^2,)

    Evaluating the functions at specified coordinates::

        sage: f(1,2)
        (-1, 2, cos(1)*e^2)
        sage: var('a b')
        (a, b)
        sage: f(a,b)
        (a - b, a*b, cos(a)*e^b)
        sage: g(1,2)
        (4,)
    """
    def __init__(self, chart, expressions) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: X.<x,y,z> = M.chart()
            sage: f = X.multifunction(x+y+z, x*y*z); f
            Coordinate functions (x + y + z, x*y*z) on the Chart (M, (x, y, z))
            sage: type(f)
            <class 'sage.manifolds.chart_func.MultiCoordFunction'>
            sage: TestSuite(f).run()
        """
    def expr(self, method=None):
        """
        Return a tuple of data, the item no. `i` being sufficient to
        reconstruct the coordinate function no. `i`.

        In other words, if ``f`` is a multi-coordinate function, then
        ``f.chart().multifunction(*(f.expr()))`` results in a
        multi-coordinate function identical to ``f``.

        INPUT:

        - ``method`` -- string (default: ``None``); the calculus method which
          the returned expressions belong to. One of

          - ``'SR'``: Sage's default symbolic engine (Symbolic Ring)
          - ``'sympy'``: SymPy
          - ``None``: the chart current calculus method is assumed

        OUTPUT:

        - a tuple of the symbolic expressions of the chart functions
          composing ``self``

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, cos(x)*exp(y))
            sage: f.expr()
            (x - y, x*y, cos(x)*e^y)
            sage: type(f.expr()[0])
            <class 'sage.symbolic.expression.Expression'>

        A SymPy output::

            sage: f.expr('sympy')
            (x - y, x*y, exp(y)*cos(x))
            sage: type(f.expr('sympy')[0])
            <class 'sympy.core.add.Add'>

        One shall always have::

            sage: f.chart().multifunction(*(f.expr())) == f
            True
        """
    def chart(self):
        """
        Return the chart with respect to which ``self`` is defined.

        OUTPUT: a :class:`~sage.manifolds.chart.Chart`

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, cos(x)*exp(y))
            sage: f.chart()
            Chart (M, (x, y))
            sage: f.chart() is X
            True
        """
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- a :class:`MultiCoordFunction`

        OUTPUT: ``True`` if ``self`` is equal to ``other``, ``False`` otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, cos(x*y))
            sage: f == X.multifunction(x-y, x*y)
            False
            sage: f == X.multifunction(x-y, x*y, 2)
            False
            sage: f == X.multifunction(x-y, x*y, cos(y*x))
            True
            sage: Y.<u,v> = M.chart()
            sage: f == Y.multifunction(u-v, u*v, cos(u*v))
            False
        """
    def __ne__(self, other):
        """
        Inequality operator.

        INPUT:

        - ``other`` -- a :class:`MultiCoordFunction`

        OUTPUT:

        - ``True`` if ``self`` is different from ``other``, ``False``
          otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, cos(x*y))
            sage: f != X.multifunction(x-y, x*y)
            True
            sage: f != X.multifunction(x, y, 2)
            True
            sage: f != X.multifunction(x-y, x*y, cos(x*y))
            False
        """
    def __getitem__(self, index):
        """
        Return a specified function of the set represented by ``self``.

        INPUT:

        - ``index`` -- index `i` of the function (`0 \\leq i \\leq m-1`)

        OUTPUT:

        -- a :class:`ChartFunction` representing the function

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, cos(x*y))
            sage: f.__getitem__(0)
            x - y
            sage: f.__getitem__(1)
            x*y
            sage: f.__getitem__(2)
            cos(x*y)
            sage: f[0], f[1], f[2]
            (x - y, x*y, cos(x*y))
        """
    def __call__(self, *coords, **options):
        """
        Compute the values of the functions at specified coordinates.

        INPUT:

        - ``*coords`` -- list of coordinates where the functions are
          to be evaluated
        - ``**options`` -- allows to pass some options, e.g.,
          ``simplify=False`` to disable simplification for symbolic
          coordinate functions

        OUTPUT: tuple containing the values of the `m` functions

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, cos(x*y))
            sage: f.__call__(2,3)
            (-1, 6, cos(6))
            sage: f(2,3)
            (-1, 6, cos(6))
            sage: f.__call__(x,y)
            (x - y, x*y, cos(x*y))
        """
    @cached_method
    def jacobian(self):
        """
        Return the Jacobian matrix of the system of coordinate functions.

        ``jacobian()`` is a 2-dimensional array of size `m \\times n`,
        where `m` is the number of functions and `n` the number of
        coordinates, the generic element being
        `J_{ij} = \\frac{\\partial f_i}{\\partial x^j}` with `1 \\leq i \\leq m`
        (row index) and `1 \\leq j \\leq n` (column index).

        OUTPUT:

        - Jacobian matrix as a 2-dimensional array ``J`` of
          coordinate functions with ``J[i-1][j-1]`` being
          `J_{ij} = \\frac{\\partial f_i}{\\partial x^j}`
          for `1 \\leq i \\leq m` and `1 \\leq j \\leq n`

        EXAMPLES:

        Jacobian of a set of 3 functions of 2 coordinates::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, y^3*cos(x))
            sage: f.jacobian()
            [           1           -1]
            [           y            x]
            [ -y^3*sin(x) 3*y^2*cos(x)]

        Each element of the result is a
        :class:`chart function <ChartFunction>`::

            sage: type(f.jacobian()[2,0])
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
            sage: f.jacobian()[2,0].display()
            (x, y) ↦ -y^3*sin(x)

        Test of the computation::

            sage: [[f.jacobian()[i,j] == f[i].diff(j) for j in range(2)] for i in range(3)]
            [[True, True], [True, True], [True, True]]

        Test with ``start_index = 1``::

            sage: M = Manifold(2, 'M', structure='topological', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y, y^3*cos(x))
            sage: f.jacobian()
            [           1           -1]
            [           y            x]
            [ -y^3*sin(x) 3*y^2*cos(x)]
            sage: [[f.jacobian()[i,j] == f[i].diff(j+1) for j in range(2)]  # note the j+1
            ....:                                         for i in range(3)]
            [[True, True], [True, True], [True, True]]
        """
    @cached_method
    def jacobian_det(self):
        """
        Return the Jacobian determinant of the system of functions.

        The number `m` of coordinate functions must equal the number `n`
        of coordinates.

        OUTPUT: a :class:`ChartFunction` representing the determinant

        EXAMPLES:

        Jacobian determinant of a set of 2 functions of 2 coordinates::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = X.multifunction(x-y, x*y)
            sage: f.jacobian_det()
            x + y

        The output of :meth:`jacobian_det` is an instance of
        :class:`ChartFunction` and can therefore be called on specific
        values of the coordinates, e.g. `(x,y) = (1,2)`::

            sage: type(f.jacobian_det())
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
            sage: f.jacobian_det().display()
            (x, y) ↦ x + y
            sage: f.jacobian_det()(1,2)
            3

        The result is cached::

            sage: f.jacobian_det() is f.jacobian_det()
            True

        We verify the determinant of the Jacobian::

            sage: f.jacobian_det() == det(matrix([[f[i].diff(j).expr() for j in range(2)]
            ....:                                 for i in range(2)]))
            True

        An example using SymPy::

            sage: M.set_calculus_method('sympy')
            sage: g = X.multifunction(x*y^3, e^x)
            sage: g.jacobian_det()
            -3*x*y**2*exp(x)
            sage: type(g.jacobian_det().expr())
            <class 'sympy.core.mul.Mul'>

        Jacobian determinant of a set of 3 functions of 3 coordinates::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: X.<x,y,z> = M.chart()
            sage: f = X.multifunction(x*y+z^2, z^2*x+y^2*z, (x*y*z)^3)
            sage: f.jacobian_det().display()
            (x, y, z) ↦ 6*x^3*y^5*z^3 - 3*x^4*y^3*z^4 - 12*x^2*y^4*z^5 + 6*x^3*y^2*z^6

        We verify the determinant of the Jacobian::

            sage: f.jacobian_det() == det(matrix([[f[i].diff(j).expr() for j in range(3)]
            ....:                                 for i in range(3)]))
            True
        """
    def set_immutable(self) -> None:
        """
        Set ``self`` and all chart functions of ``self`` immutable.

        EXAMPLES:

        Declare a coordinate function immutable::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: X.<x,y,z> = M.chart()
            sage: f = X.multifunction(x+y+z, x*y*z)
            sage: f.is_immutable()
            False
            sage: f.set_immutable()
            sage: f.is_immutable()
            True

        The chart functions are now immutable, too::

            sage: f[0].parent()
            Ring of chart functions on Chart (M, (x, y, z))
            sage: f[0].is_immutable()
            True
        """
