from sage.manifolds.chart import Chart as Chart
from sage.manifolds.chart_func import ChartFunction as ChartFunction
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import CommutativeAlgebraElement as CommutativeAlgebraElement, ModuleElementWithMutability as ModuleElementWithMutability
from sage.symbolic.expression import Expression as Expression
from sage.tensor.modules.format_utilities import FormattedExpansion as FormattedExpansion

class ScalarField(CommutativeAlgebraElement, ModuleElementWithMutability):
    """
    Scalar field on a topological manifold.

    Given a topological manifold `M` over a topological field `K` (in most
    applications, `K = \\RR` or `K = \\CC`), a *scalar field on* `M` is a
    continuous map

    .. MATH::

        f: M \\longrightarrow K.

    A scalar field on `M` is an element of the commutative algebra
    `C^0(M)` (see
    :class:`~sage.manifolds.scalarfield_algebra.ScalarFieldAlgebra`).

    INPUT:

    - ``parent`` -- the algebra of scalar fields containing the scalar field
      (must be an instance of class
      :class:`~sage.manifolds.scalarfield_algebra.ScalarFieldAlgebra`)

    - ``coord_expression`` -- (default: ``None``) coordinate expression(s) of
      the scalar field; this can be either

      * a dictionary of coordinate expressions in various charts on
        the domain, with the charts as keys;
      * a single coordinate expression; if the argument ``chart`` is
        ``'all'``, this expression is set to all the charts defined
        on the open set; otherwise, the expression is set in the
        specific chart provided by the argument ``chart``

    - ``chart`` -- (default: ``None``) chart defining the coordinates used
      in ``coord_expression`` when the latter is a single coordinate
      expression; if none is provided (default), the default chart of the
      open set is assumed. If ``chart=='all'``, ``coord_expression`` is
      assumed to be independent of the chart (constant scalar field).

    - ``name`` -- (default: ``None``) string; name (symbol) given to the
      scalar field

    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      scalar field; if none is provided, the LaTeX symbol is set to ``name``

    If ``coord_expression`` is ``None`` or incomplete, coordinate
    expressions can be added after the creation of the object, by means of
    the methods :meth:`add_expr`, :meth:`add_expr_by_continuation` and
    :meth:`set_expr`.

    EXAMPLES:

    A scalar field on the 2-sphere::

        sage: M = Manifold(2, 'M', structure='topological') # the 2-dimensional sphere S^2
        sage: U = M.open_subset('U') # complement of the North pole
        sage: c_xy.<x,y> = U.chart() # stereographic coordinates from the North pole
        sage: V = M.open_subset('V') # complement of the South pole
        sage: c_uv.<u,v> = V.chart() # stereographic coordinates from the South pole
        sage: M.declare_union(U,V)   # S^2 is the union of U and V
        sage: xy_to_uv = c_xy.transition_map(c_uv, (x/(x^2+y^2), y/(x^2+y^2)),
        ....:                                intersection_name='W',
        ....:                                restrictions1= x^2+y^2!=0,
        ....:                                restrictions2= u^2+v^2!=0)
        sage: uv_to_xy = xy_to_uv.inverse()
        sage: f = M.scalar_field({c_xy: 1/(1+x^2+y^2), c_uv: (u^2+v^2)/(1+u^2+v^2)},
        ....:                    name='f') ; f
        Scalar field f on the 2-dimensional topological manifold M
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x^2 + y^2 + 1)
        on V: (u, v) ↦ (u^2 + v^2)/(u^2 + v^2 + 1)

    For scalar fields defined by a single coordinate expression, the latter
    can be passed instead of the dictionary over the charts::

        sage: g = U.scalar_field(x*y, chart=c_xy, name='g') ; g
        Scalar field g on the Open subset U of the 2-dimensional topological
         manifold M

    The above is indeed equivalent to::

        sage: g = U.scalar_field({c_xy: x*y}, name='g') ; g
        Scalar field g on the Open subset U of the 2-dimensional topological
         manifold M

    Since ``c_xy`` is the default chart of ``U``, the argument ``chart`` can
    be skipped::

        sage: g = U.scalar_field(x*y, name='g') ; g
        Scalar field g on the Open subset U of the 2-dimensional topological
         manifold M

    The scalar field `g` is defined on `U` and has an expression in terms of
    the coordinates `(u,v)` on `W=U\\cap V`::

        sage: g.display()
        g: U → ℝ
           (x, y) ↦ x*y
        on W: (u, v) ↦ u*v/(u^4 + 2*u^2*v^2 + v^4)

    Scalar fields on `M` can also be declared with a single chart::

        sage: f = M.scalar_field(1/(1+x^2+y^2), chart=c_xy, name='f') ; f
        Scalar field f on the 2-dimensional topological manifold M

    Their definition must then be completed by providing the expressions on
    other charts, via the method :meth:`add_expr`, to get a global cover of
    the manifold::

        sage: f.add_expr((u^2+v^2)/(1+u^2+v^2), chart=c_uv)
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x^2 + y^2 + 1)
        on V: (u, v) ↦ (u^2 + v^2)/(u^2 + v^2 + 1)

    We can even first declare the scalar field without any coordinate
    expression and provide them subsequently::

        sage: f = M.scalar_field(name='f')
        sage: f.add_expr(1/(1+x^2+y^2), chart=c_xy)
        sage: f.add_expr((u^2+v^2)/(1+u^2+v^2), chart=c_uv)
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x^2 + y^2 + 1)
        on V: (u, v) ↦ (u^2 + v^2)/(u^2 + v^2 + 1)

    We may also use the method :meth:`add_expr_by_continuation` to complete
    the coordinate definition using the analytic continuation from domains in
    which charts overlap::

        sage: f = M.scalar_field(1/(1+x^2+y^2), chart=c_xy, name='f') ; f
        Scalar field f on the 2-dimensional topological manifold M
        sage: f.add_expr_by_continuation(c_uv, U.intersection(V))
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x^2 + y^2 + 1)
        on V: (u, v) ↦ (u^2 + v^2)/(u^2 + v^2 + 1)

    A scalar field can also be defined by some unspecified function of the
    coordinates::

        sage: h = U.scalar_field(function('H')(x, y), name='h') ; h
        Scalar field h on the Open subset U of the 2-dimensional topological
         manifold M
        sage: h.display()
        h: U → ℝ
           (x, y) ↦ H(x, y)
        on W: (u, v) ↦ H(u/(u^2 + v^2), v/(u^2 + v^2))

    We may use the argument ``latex_name`` to specify the LaTeX symbol denoting
    the scalar field if the latter is different from ``name``::

        sage: latex(f)
        f
        sage: f = M.scalar_field({c_xy: 1/(1+x^2+y^2), c_uv: (u^2+v^2)/(1+u^2+v^2)},
        ....:                    name='f', latex_name=r'\\mathcal{F}')
        sage: latex(f)
        \\mathcal{F}

    The coordinate expression in a given chart is obtained via the method
    :meth:`expr`, which returns a symbolic expression::

        sage: f.expr(c_uv)
        (u^2 + v^2)/(u^2 + v^2 + 1)
        sage: type(f.expr(c_uv))
        <class 'sage.symbolic.expression.Expression'>

    The method :meth:`coord_function` returns instead a function of the
    chart coordinates, i.e. an instance of
    :class:`~sage.manifolds.chart_func.ChartFunction`::

        sage: f.coord_function(c_uv)
        (u^2 + v^2)/(u^2 + v^2 + 1)
        sage: type(f.coord_function(c_uv))
        <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
        sage: f.coord_function(c_uv).display()
        (u, v) ↦ (u^2 + v^2)/(u^2 + v^2 + 1)

    The value returned by the method :meth:`expr` is actually the coordinate
    expression of the chart function::

        sage: f.expr(c_uv) is f.coord_function(c_uv).expr()
        True

    A constant scalar field is declared by setting the argument ``chart`` to
    ``'all'``::

        sage: c = M.scalar_field(2, chart='all', name='c') ; c
        Scalar field c on the 2-dimensional topological manifold M
        sage: c.display()
        c: M → ℝ
        on U: (x, y) ↦ 2
        on V: (u, v) ↦ 2

    A shortcut is to use the method
    :meth:`~sage.manifolds.manifold.TopologicalManifold.constant_scalar_field`::

        sage: c == M.constant_scalar_field(2)
        True

    The constant value can be some unspecified parameter::

        sage: var('a')
        a
        sage: c = M.constant_scalar_field(a, name='c') ; c
        Scalar field c on the 2-dimensional topological manifold M
        sage: c.display()
        c: M → ℝ
        on U: (x, y) ↦ a
        on V: (u, v) ↦ a

    A special case of constant field is the zero scalar field::

        sage: zer = M.constant_scalar_field(0) ; zer
        Scalar field zero on the 2-dimensional topological manifold M
        sage: zer.display()
        zero: M → ℝ
        on U: (x, y) ↦ 0
        on V: (u, v) ↦ 0

    It can be obtained directly by means of the function
    :meth:`~sage.manifolds.manifold.TopologicalManifold.zero_scalar_field`::

        sage: zer is M.zero_scalar_field()
        True

    A third way is to get it as the zero element of the algebra `C^0(M)`
    of scalar fields on `M` (see below)::

        sage: zer is M.scalar_field_algebra().zero()
        True

    The constant scalar fields zero and one are immutable, and therefore
    their expressions cannot be changed::

        sage: zer.is_immutable()
        True
        sage: zer.set_expr(x)
        Traceback (most recent call last):
        ...
        ValueError: the expressions of an immutable element cannot be
         changed
        sage: one = M.one_scalar_field()
        sage: one.is_immutable()
        True
        sage: one.set_expr(x)
        Traceback (most recent call last):
        ...
        ValueError: the expressions of an immutable element cannot be
         changed

    Other scalar fields can be declared immutable, too::

        sage: c.is_immutable()
        False
        sage: c.set_immutable()
        sage: c.is_immutable()
        True
        sage: c.set_expr(y^2)
        Traceback (most recent call last):
        ...
        ValueError: the expressions of an immutable element cannot be
         changed
        sage: c.set_name('b')
        Traceback (most recent call last):
        ...
        ValueError: the name of an immutable element cannot be changed

    Immutable elements are hashable and can therefore be used as keys for
    dictionaries::

        sage: {c: 1}[c]
        1

    By definition, a scalar field acts on the manifold's points, sending
    them to elements of the manifold's base field (real numbers in the
    present case)::

        sage: N = M.point((0,0), chart=c_uv) # the North pole
        sage: S = M.point((0,0), chart=c_xy) # the South pole
        sage: E = M.point((1,0), chart=c_xy) # a point at the equator
        sage: f(N)
        0
        sage: f(S)
        1
        sage: f(E)
        1/2
        sage: h(E)
        H(1, 0)
        sage: c(E)
        a
        sage: zer(E)
        0

    A scalar field can be compared to another scalar field::

        sage: f == g
        False

    ...to a symbolic expression::

        sage: f == x*y
        False
        sage: g == x*y
        True
        sage: c == a
        True

    ...to a number::

        sage: f == 2
        False
        sage: zer == 0
        True

    ...to anything else::

        sage: f == M
        False

    Standard mathematical functions are implemented::

        sage: sqrt(f)
        Scalar field sqrt(f) on the 2-dimensional topological manifold M
        sage: sqrt(f).display()
        sqrt(f): M → ℝ
        on U: (x, y) ↦ 1/sqrt(x^2 + y^2 + 1)
        on V: (u, v) ↦ sqrt(u^2 + v^2)/sqrt(u^2 + v^2 + 1)

    ::

        sage: tan(f)
        Scalar field tan(f) on the 2-dimensional topological manifold M
        sage: tan(f).display()
        tan(f): M → ℝ
        on U: (x, y) ↦ sin(1/(x^2 + y^2 + 1))/cos(1/(x^2 + y^2 + 1))
        on V: (u, v) ↦ sin((u^2 + v^2)/(u^2 + v^2 + 1))/cos((u^2 + v^2)/(u^2 + v^2 + 1))

    .. RUBRIC:: Arithmetics of scalar fields

    Scalar fields on `M` (resp. `U`) belong to the algebra `C^0(M)`
    (resp. `C^0(U)`)::

        sage: f.parent()
        Algebra of scalar fields on the 2-dimensional topological manifold M
        sage: f.parent() is M.scalar_field_algebra()
        True
        sage: g.parent()
        Algebra of scalar fields on the Open subset U of the 2-dimensional
         topological manifold M
        sage: g.parent() is U.scalar_field_algebra()
        True

    Consequently, scalar fields can be added::

        sage: s = f + c ; s
        Scalar field f+c on the 2-dimensional topological manifold M
        sage: s.display()
        f+c: M → ℝ
        on U: (x, y) ↦ (a*x^2 + a*y^2 + a + 1)/(x^2 + y^2 + 1)
        on V: (u, v) ↦ ((a + 1)*u^2 + (a + 1)*v^2 + a)/(u^2 + v^2 + 1)

    and subtracted::

        sage: s = f - c ; s
        Scalar field f-c on the 2-dimensional topological manifold M
        sage: s.display()
        f-c: M → ℝ
        on U: (x, y) ↦ -(a*x^2 + a*y^2 + a - 1)/(x^2 + y^2 + 1)
        on V: (u, v) ↦ -((a - 1)*u^2 + (a - 1)*v^2 + a)/(u^2 + v^2 + 1)

    Some tests::

        sage: f + zer == f
        True
        sage: f - f == zer
        True
        sage: f + (-f) == zer
        True
        sage: (f+c)-f == c
        True
        sage: (f-c)+c == f
        True

    We may add a number (interpreted as a constant scalar field) to a scalar
    field::

        sage: s = f + 1 ; s
        Scalar field f+1 on the 2-dimensional topological manifold M
        sage: s.display()
        f+1: M → ℝ
        on U: (x, y) ↦ (x^2 + y^2 + 2)/(x^2 + y^2 + 1)
        on V: (u, v) ↦ (2*u^2 + 2*v^2 + 1)/(u^2 + v^2 + 1)
        sage: (f+1)-1 == f
        True

    The number can represented by a symbolic variable::

        sage: s = a + f ; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s == c + f
        True

    However if the symbolic variable is a chart coordinate, the addition
    is performed only on the chart domain::

        sage: s = f + x; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ (x^3 + x*y^2 + x + 1)/(x^2 + y^2 + 1)
        on W: (u, v) ↦ (u^4 + v^4 + u^3 + (2*u^2 + u)*v^2 + u)/(u^4 + v^4 + (2*u^2 + 1)*v^2 + u^2)
        sage: s = f + u; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on W: (x, y) ↦ (x^3 + (x + 1)*y^2 + x^2 + x)/(x^4 + y^4 + (2*x^2 + 1)*y^2 + x^2)
        on V: (u, v) ↦ (u^3 + (u + 1)*v^2 + u^2 + u)/(u^2 + v^2 + 1)

    The addition of two scalar fields with different domains is possible if
    the domain of one of them is a subset of the domain of the other; the
    domain of the result is then this subset::

        sage: f.domain()
        2-dimensional topological manifold M
        sage: g.domain()
        Open subset U of the 2-dimensional topological manifold M
        sage: s = f + g ; s
        Scalar field f+g on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.domain()
        Open subset U of the 2-dimensional topological manifold M
        sage: s.display()
        f+g: U → ℝ
           (x, y) ↦ (x*y^3 + (x^3 + x)*y + 1)/(x^2 + y^2 + 1)
        on W: (u, v) ↦ (u^6 + 3*u^4*v^2 + 3*u^2*v^4 + v^6 + u*v^3
         + (u^3 + u)*v)/(u^6 + v^6 + (3*u^2 + 1)*v^4 + u^4 + (3*u^4 + 2*u^2)*v^2)

    The operation actually performed is `f|_U + g`::

        sage: s == f.restrict(U) + g
        True

    In Sage framework, the addition of `f` and `g` is permitted because
    there is a *coercion* of the parent of `f`, namely `C^0(M)`, to
    the parent of `g`, namely `C^0(U)` (see
    :class:`~sage.manifolds.scalarfield_algebra.ScalarFieldAlgebra`)::

        sage: CM = M.scalar_field_algebra()
        sage: CU = U.scalar_field_algebra()
        sage: CU.has_coerce_map_from(CM)
        True

    The coercion map is nothing but the restriction to domain `U`::

        sage: CU.coerce(f) == f.restrict(U)
        True

    Since the algebra `C^0(M)` is a vector space over `\\RR`, scalar fields
    can be multiplied by a number, either an explicit one::

        sage: s = 2*f ; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ 2/(x^2 + y^2 + 1)
        on V: (u, v) ↦ 2*(u^2 + v^2)/(u^2 + v^2 + 1)

    or a symbolic one::

        sage: s = a*f ; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ a/(x^2 + y^2 + 1)
        on V: (u, v) ↦ (u^2 + v^2)*a/(u^2 + v^2 + 1)

    However, if the symbolic variable is a chart coordinate, the
    multiplication is performed only in the corresponding chart::

        sage: s = x*f; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ x/(x^2 + y^2 + 1)
        on W: (u, v) ↦ u/(u^2 + v^2 + 1)
        sage: s = u*f; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on W: (x, y) ↦ x/(x^4 + y^4 + (2*x^2 + 1)*y^2 + x^2)
        on V: (u, v) ↦ (u^2 + v^2)*u/(u^2 + v^2 + 1)

    Some tests::

        sage: 0*f == 0
        True
        sage: 0*f == zer
        True
        sage: 1*f == f
        True
        sage: (-2)*f == - f - f
        True

    The ring multiplication of the algebras `C^0(M)` and `C^0(U)`
    is the pointwise multiplication of functions::

        sage: s = f*f ; s
        Scalar field f*f on the 2-dimensional topological manifold M
        sage: s.display()
        f*f: M → ℝ
        on U: (x, y) ↦ 1/(x^4 + y^4 + 2*(x^2 + 1)*y^2 + 2*x^2 + 1)
        on V: (u, v) ↦ (u^4 + 2*u^2*v^2 + v^4)/(u^4 + v^4 + 2*(u^2 + 1)*v^2
         + 2*u^2 + 1)
        sage: s = g*h ; s
        Scalar field g*h on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        g*h: U → ℝ
           (x, y) ↦ x*y*H(x, y)
        on W: (u, v) ↦ u*v*H(u/(u^2 + v^2), v/(u^2 + v^2))/(u^4 + 2*u^2*v^2 + v^4)

    Thanks to the coercion `C^0(M) \\to C^0(U)` mentioned above,
    it is possible to multiply a scalar field defined on `M` by a
    scalar field defined on `U`, the result being a scalar field
    defined on `U`::

        sage: f.domain(), g.domain()
        (2-dimensional topological manifold M,
         Open subset U of the 2-dimensional topological manifold M)
        sage: s = f*g ; s
        Scalar field f*g on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        f*g: U → ℝ
           (x, y) ↦ x*y/(x^2 + y^2 + 1)
        on W: (u, v) ↦ u*v/(u^4 + v^4 + (2*u^2 + 1)*v^2 + u^2)
        sage: s == f.restrict(U)*g
        True

    Scalar fields can be divided (pointwise division)::

        sage: s = f/c ; s
        Scalar field f/c on the 2-dimensional topological manifold M
        sage: s.display()
        f/c: M → ℝ
        on U: (x, y) ↦ 1/(a*x^2 + a*y^2 + a)
        on V: (u, v) ↦ (u^2 + v^2)/(a*u^2 + a*v^2 + a)
        sage: s = g/h ; s
        Scalar field g/h on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        g/h: U → ℝ
           (x, y) ↦ x*y/H(x, y)
        on W: (u, v) ↦ u*v/((u^4 + 2*u^2*v^2 + v^4)*H(u/(u^2 + v^2), v/(u^2 + v^2)))
        sage: s = f/g ; s
        Scalar field f/g on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        f/g: U → ℝ
           (x, y) ↦ 1/(x*y^3 + (x^3 + x)*y)
        on W: (u, v) ↦ (u^6 + 3*u^4*v^2 + 3*u^2*v^4 + v^6)/(u*v^3 + (u^3 + u)*v)
        sage: s == f.restrict(U)/g
        True

    For scalar fields defined on a single chart domain, we may perform some
    arithmetics with symbolic expressions involving the chart coordinates::

        sage: s = g + x^2 - y ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ x^2 + (x - 1)*y
        on W: (u, v) ↦ -(v^3 - u^2 + (u^2 - u)*v)/(u^4 + 2*u^2*v^2 + v^4)

    ::

        sage: s = g*x ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ x^2*y
        on W: (u, v) ↦ u^2*v/(u^6 + 3*u^4*v^2 + 3*u^2*v^4 + v^6)

    ::

        sage: s = g/x ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ y
        on W: (u, v) ↦ v/(u^2 + v^2)
        sage: s = x/g ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ 1/y
        on W: (u, v) ↦ (u^2 + v^2)/v


    .. RUBRIC:: Examples with SymPy as the symbolic engine

    From now on, we ask that all symbolic calculus on manifold `M` are
    performed by SymPy::

        sage: M.set_calculus_method('sympy')

    We define `f` as above::

        sage: f = M.scalar_field({c_xy: 1/(1+x^2+y^2), c_uv: (u^2+v^2)/(1+u^2+v^2)},
        ....:                    name='f') ; f
        Scalar field f on the 2-dimensional topological manifold M
        sage: f.display()  # notice the SymPy display of exponents
        f: M → ℝ
        on U: (x, y) ↦ 1/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (u**2 + v**2)/(u**2 + v**2 + 1)
        sage: type(f.coord_function(c_xy).expr())
        <class 'sympy.core.power.Pow'>

    The scalar field `g` defined on `U`::

        sage: g = U.scalar_field({c_xy: x*y}, name='g')
        sage: g.display() # again notice the SymPy display of exponents
        g: U → ℝ
           (x, y) ↦ x*y
        on W: (u, v) ↦ u*v/(u**4 + 2*u**2*v**2 + v**4)

    Definition on a single chart and subsequent completion::

        sage: f = M.scalar_field(1/(1+x^2+y^2), chart=c_xy, name='f')
        sage: f.add_expr((u^2+v^2)/(1+u^2+v^2), chart=c_uv)
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (u**2 + v**2)/(u**2 + v**2 + 1)

    Definition without any coordinate expression and subsequent completion::

        sage: f = M.scalar_field(name='f')
        sage: f.add_expr(1/(1+x^2+y^2), chart=c_xy)
        sage: f.add_expr((u^2+v^2)/(1+u^2+v^2), chart=c_uv)
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (u**2 + v**2)/(u**2 + v**2 + 1)

    Use of :meth:`add_expr_by_continuation`::

        sage: f = M.scalar_field(1/(1+x^2+y^2), chart=c_xy, name='f')
        sage: f.add_expr_by_continuation(c_uv, U.intersection(V))
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ 1/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (u**2 + v**2)/(u**2 + v**2 + 1)

    A scalar field defined by some unspecified function of the
    coordinates::

        sage: h = U.scalar_field(function('H')(x, y), name='h') ; h
        Scalar field h on the Open subset U of the 2-dimensional topological
         manifold M
        sage: h.display()
        h: U → ℝ
           (x, y) ↦ H(x, y)
        on W: (u, v) ↦ H(u/(u**2 + v**2), v/(u**2 + v**2))

    The coordinate expression in a given chart is obtained via the method
    :meth:`expr`, which in the present context, returns a SymPy object::

        sage: f.expr(c_uv)
        (u**2 + v**2)/(u**2 + v**2 + 1)
        sage: type(f.expr(c_uv))
        <class 'sympy.core.mul.Mul'>

    The method :meth:`coord_function` returns instead a function of the
    chart coordinates, i.e. an instance of
    :class:`~sage.manifolds.chart_func.ChartFunction`::

        sage: f.coord_function(c_uv)
        (u**2 + v**2)/(u**2 + v**2 + 1)
        sage: type(f.coord_function(c_uv))
        <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>
        sage: f.coord_function(c_uv).display()
        (u, v) ↦ (u**2 + v**2)/(u**2 + v**2 + 1)

    The value returned by the method :meth:`expr` is actually the coordinate
    expression of the chart function::

        sage: f.expr(c_uv) is f.coord_function(c_uv).expr()
        True

    We may ask for the ``SR`` representation of the coordinate function::

        sage: f.coord_function(c_uv).expr('SR')
        (u^2 + v^2)/(u^2 + v^2 + 1)

    A constant scalar field with SymPy representation::

        sage: c = M.constant_scalar_field(2, name='c')
        sage: c.display()
        c: M → ℝ
        on U: (x, y) ↦ 2
        on V: (u, v) ↦ 2
        sage: type(c.expr(c_xy))
        <class 'sympy.core.numbers.Integer'>

    The constant value can be some unspecified parameter::

        sage: var('a')
        a
        sage: c = M.constant_scalar_field(a, name='c')
        sage: c.display()
        c: M → ℝ
        on U: (x, y) ↦ a
        on V: (u, v) ↦ a
        sage: type(c.expr(c_xy))
        <class 'sympy.core.symbol.Symbol'>

    The zero scalar field::

        sage: zer = M.constant_scalar_field(0) ; zer
        Scalar field zero on the 2-dimensional topological manifold M
        sage: zer.display()
        zero: M → ℝ
        on U: (x, y) ↦ 0
        on V: (u, v) ↦ 0
        sage: type(zer.expr(c_xy))
        <class 'sympy.core.numbers.Zero'>
        sage: zer is M.zero_scalar_field()
        True

    Action of scalar fields on manifold's points::

        sage: N = M.point((0,0), chart=c_uv) # the North pole
        sage: S = M.point((0,0), chart=c_xy) # the South pole
        sage: E = M.point((1,0), chart=c_xy) # a point at the equator
        sage: f(N)
        0
        sage: f(S)
        1
        sage: f(E)
        1/2
        sage: h(E)
        H(1, 0)
        sage: c(E)
        a
        sage: zer(E)
        0

    A scalar field can be compared to another scalar field::

        sage: f == g
        False

    ...to a symbolic expression::

        sage: f == x*y
        False
        sage: g == x*y
        True
        sage: c == a
        True

    ...to a number::

        sage: f == 2
        False
        sage: zer == 0
        True

    ...to anything else::

        sage: f == M
        False

    Standard mathematical functions are implemented::

        sage: sqrt(f)
        Scalar field sqrt(f) on the 2-dimensional topological manifold M
        sage: sqrt(f).display()
        sqrt(f): M → ℝ
        on U: (x, y) ↦ 1/sqrt(x**2 + y**2 + 1)
        on V: (u, v) ↦ sqrt(u**2 + v**2)/sqrt(u**2 + v**2 + 1)

    ::

        sage: tan(f)
        Scalar field tan(f) on the 2-dimensional topological manifold M
        sage: tan(f).display()
        tan(f): M → ℝ
        on U: (x, y) ↦ tan(1/(x**2 + y**2 + 1))
        on V: (u, v) ↦ tan((u**2 + v**2)/(u**2 + v**2 + 1))

    .. RUBRIC:: Arithmetics of scalar fields with SymPy

    Scalar fields on `M` (resp. `U`) belong to the algebra `C^0(M)`
    (resp. `C^0(U)`)::

        sage: f.parent()
        Algebra of scalar fields on the 2-dimensional topological manifold M
        sage: f.parent() is M.scalar_field_algebra()
        True
        sage: g.parent()
        Algebra of scalar fields on the Open subset U of the 2-dimensional
         topological manifold M
        sage: g.parent() is U.scalar_field_algebra()
        True

    Consequently, scalar fields can be added::

        sage: s = f + c ; s
        Scalar field f+c on the 2-dimensional topological manifold M
        sage: s.display()
        f+c: M → ℝ
        on U: (x, y) ↦ (a*x**2 + a*y**2 + a + 1)/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (a*u**2 + a*v**2 + a + u**2 + v**2)/(u**2 + v**2 + 1)

    and subtracted::

        sage: s = f - c ; s
        Scalar field f-c on the 2-dimensional topological manifold M
        sage: s.display()
        f-c: M → ℝ
        on U: (x, y) ↦ (-a*x**2 - a*y**2 - a + 1)/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (-a*u**2 - a*v**2 - a + u**2 + v**2)/(u**2 + v**2 + 1)

    Some tests::

        sage: f + zer == f
        True
        sage: f - f == zer
        True
        sage: f + (-f) == zer
        True
        sage: (f+c)-f == c
        True
        sage: (f-c)+c == f
        True

    We may add a number (interpreted as a constant scalar field) to a scalar
    field::

        sage: s = f + 1 ; s
        Scalar field f+1 on the 2-dimensional topological manifold M
        sage: s.display()
        f+1: M → ℝ
        on U: (x, y) ↦ (x**2 + y**2 + 2)/(x**2 + y**2 + 1)
        on V: (u, v) ↦ (2*u**2 + 2*v**2 + 1)/(u**2 + v**2 + 1)
        sage: (f+1)-1 == f
        True

    The number can represented by a symbolic variable::

        sage: s = a + f ; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s == c + f
        True

    However if the symbolic variable is a chart coordinate, the addition
    is performed only on the chart domain::

        sage: s = f + x; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ (x**3 + x*y**2 + x + 1)/(x**2 + y**2 + 1)
        on W: (u, v) ↦ (u**4 + u**3 + 2*u**2*v**2 + u*v**2 + u + v**4)/(u**4 + 2*u**2*v**2 + u**2 + v**4 + v**2)
        sage: s = f + u; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on W: (x, y) ↦ (x**3 + x**2 + x*y**2 + x + y**2)/(x**4 + 2*x**2*y**2 + x**2 + y**4 + y**2)
        on V: (u, v) ↦ (u**3 + u**2 + u*v**2 + u + v**2)/(u**2 + v**2 + 1)

    The addition of two scalar fields with different domains is possible if
    the domain of one of them is a subset of the domain of the other; the
    domain of the result is then this subset::

        sage: f.domain()
        2-dimensional topological manifold M
        sage: g.domain()
        Open subset U of the 2-dimensional topological manifold M
        sage: s = f + g ; s
        Scalar field f+g on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.domain()
        Open subset U of the 2-dimensional topological manifold M
        sage: s.display()
        f+g: U → ℝ
           (x, y) ↦ (x**3*y + x*y**3 + x*y + 1)/(x**2 + y**2 + 1)
        on W: (u, v) ↦ (u**6 + 3*u**4*v**2 + u**3*v + 3*u**2*v**4 + u*v**3 + u*v + v**6)/(u**6 + 3*u**4*v**2 + u**4 + 3*u**2*v**4 + 2*u**2*v**2 + v**6 + v**4)

    The operation actually performed is `f|_U + g`::

        sage: s == f.restrict(U) + g
        True

    Since the algebra `C^0(M)` is a vector space over `\\RR`, scalar fields
    can be multiplied by a number, either an explicit one::

        sage: s = 2*f ; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ 2/(x**2 + y**2 + 1)
        on V: (u, v) ↦ 2*(u**2 + v**2)/(u**2 + v**2 + 1)

    or a symbolic one::

        sage: s = a*f ; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ a/(x**2 + y**2 + 1)
        on V: (u, v) ↦ a*(u**2 + v**2)/(u**2 + v**2 + 1)

    However, if the symbolic variable is a chart coordinate, the
    multiplication is performed only in the corresponding chart::

        sage: s = x*f; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ x/(x**2 + y**2 + 1)
        on W: (u, v) ↦ u/(u**2 + v**2 + 1)
        sage: s = u*f; s
        Scalar field on the 2-dimensional topological manifold M
        sage: s.display()
        M → ℝ
        on W: (x, y) ↦ x/(x**4 + 2*x**2*y**2 + x**2 + y**4 + y**2)
        on V: (u, v) ↦ u*(u**2 + v**2)/(u**2 + v**2 + 1)

    Some tests::

        sage: 0*f == 0
        True
        sage: 0*f == zer
        True
        sage: 1*f == f
        True
        sage: (-2)*f == - f - f
        True

    The ring multiplication of the algebras `C^0(M)` and `C^0(U)`
    is the pointwise multiplication of functions::

        sage: s = f*f ; s
        Scalar field f*f on the 2-dimensional topological manifold M
        sage: s.display()
        f*f: M → ℝ
        on U: (x, y) ↦ 1/(x**4 + 2*x**2*y**2 + 2*x**2 + y**4 + 2*y**2 + 1)
        on V: (u, v) ↦ (u**4 + 2*u**2*v**2 + v**4)/(u**4 + 2*u**2*v**2 + 2*u**2 + v**4 + 2*v**2 + 1)

        sage: s = g*h ; s
        Scalar field g*h on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        g*h: U → ℝ
           (x, y) ↦ x*y*H(x, y)
        on W: (u, v) ↦ u*v*H(u/(u**2 + v**2), v/(u**2 + v**2))/(u**4 + 2*u**2*v**2 + v**4)

    Thanks to the coercion `C^0(M) \\to C^0(U)` mentioned above,
    it is possible to multiply a scalar field defined on `M` by a
    scalar field defined on `U`, the result being a scalar field
    defined on `U`::

        sage: f.domain(), g.domain()
        (2-dimensional topological manifold M,
         Open subset U of the 2-dimensional topological manifold M)
        sage: s = f*g ; s
        Scalar field f*g on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        f*g: U → ℝ
           (x, y) ↦ x*y/(x**2 + y**2 + 1)
        on W: (u, v) ↦ u*v/(u**4 + 2*u**2*v**2 + u**2 + v**4 + v**2)

        sage: s == f.restrict(U)*g
        True

    Scalar fields can be divided (pointwise division)::

        sage: s = f/c ; s
        Scalar field f/c on the 2-dimensional topological manifold M
        sage: s.display()
        f/c: M → ℝ
        on U: (x, y) ↦ 1/(a*(x**2 + y**2 + 1))
        on V: (u, v) ↦ (u**2 + v**2)/(a*(u**2 + v**2 + 1))
        sage: s = g/h ; s
        Scalar field g/h on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        g/h: U → ℝ
           (x, y) ↦ x*y/H(x, y)
        on W: (u, v) ↦ u*v/((u**4 + 2*u**2*v**2 + v**4)*H(u/(u**2 + v**2), v/(u**2 + v**2)))

        sage: s = f/g ; s
        Scalar field f/g on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        f/g: U → ℝ
           (x, y) ↦ 1/(x*y*(x**2 + y**2 + 1))
        on W: (u, v) ↦ (u**6 + 3*u**4*v**2 + 3*u**2*v**4 + v**6)/(u*v*(u**2 + v**2 + 1))
        sage: s == f.restrict(U)/g
        True

    For scalar fields defined on a single chart domain, we may perform some
    arithmetics with symbolic expressions involving the chart coordinates::

        sage: s = g + x^2 - y ; s
        Scalar field on the Open subset U of the 2-dimensional topological manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ x**2 + x*y - y
        on W: (u, v) ↦ (-u**2*v + u**2 + u*v - v**3)/(u**4 + 2*u**2*v**2 + v**4)


    ::

        sage: s = g*x ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ x**2*y
        on W: (u, v) ↦ u**2*v/(u**6 + 3*u**4*v**2 + 3*u**2*v**4 + v**6)

    ::

        sage: s = g/x ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ y
        on W: (u, v) ↦ v/(u**2 + v**2)
        sage: s = x/g ; s
        Scalar field on the Open subset U of the 2-dimensional topological
         manifold M
        sage: s.display()
        U → ℝ
        (x, y) ↦ 1/y
        on W: (u, v) ↦ u**2/v + v

    The test suite is passed::

        sage: TestSuite(f).run()
        sage: TestSuite(zer).run()
    """
    def __init__(self, parent, coord_expression=None, chart=None, name=None, latex_name=None) -> None:
        """
        Construct a scalar field.

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name='f') ; f
            Scalar field f on the 2-dimensional topological manifold M
            sage: from sage.manifolds.scalarfield import ScalarField
            sage: isinstance(f, ScalarField)
            True
            sage: f.parent()
            Algebra of scalar fields on the 2-dimensional topological
             manifold M
            sage: TestSuite(f).run()
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if ``self`` is nonzero and ``False`` otherwise.

        This method is called by :meth:`~sage.structure.element.Element.is_zero()`.

        EXAMPLES:

        Tests on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x*y)
            sage: f.is_zero()
            False
            sage: f.set_expr(0)
            sage: f.is_zero()
            True
            sage: g = M.scalar_field(0)
            sage: g.is_zero()
            True
            sage: M.zero_scalar_field().is_zero()
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
            sage: f = M.scalar_field({X: 0})
            sage: f.is_trivial_zero()
            True
            sage: f = M.scalar_field(0)
            sage: f.is_trivial_zero()
            True
            sage: M.zero_scalar_field().is_trivial_zero()
            True
            sage: f = M.scalar_field({X: x+y})
            sage: f.is_trivial_zero()
            False

        Scalar field defined by means of two charts::

            sage: U1 = M.open_subset('U1'); X1.<x1,y1> = U1.chart()
            sage: U2 = M.open_subset('U2'); X2.<x2,y2> = U2.chart()
            sage: f = M.scalar_field({X1: 0, X2: 0})
            sage: f.is_trivial_zero()
            True
            sage: f = M.scalar_field({X1: 0, X2: 1})
            sage: f.is_trivial_zero()
            False

        No simplification is attempted, so that ``False`` is returned for
        non-trivial cases::

            sage: f = M.scalar_field({X: cos(x)^2 + sin(x)^2 - 1})
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
            sage: f = M.scalar_field({X: 1})
            sage: f.is_trivial_one()
            True
            sage: f = M.scalar_field(1)
            sage: f.is_trivial_one()
            True
            sage: M.one_scalar_field().is_trivial_one()
            True
            sage: f = M.scalar_field({X: x+y})
            sage: f.is_trivial_one()
            False

        Scalar field defined by means of two charts::

            sage: U1 = M.open_subset('U1'); X1.<x1,y1> = U1.chart()
            sage: U2 = M.open_subset('U2'); X2.<x2,y2> = U2.chart()
            sage: f = M.scalar_field({X1: 1, X2: 1})
            sage: f.is_trivial_one()
            True
            sage: f = M.scalar_field({X1: 0, X2: 1})
            sage: f.is_trivial_one()
            False

        No simplification is attempted, so that ``False`` is returned for
        non-trivial cases::

            sage: f = M.scalar_field({X: cos(x)^2 + sin(x)^2})
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
        Return ``True`` iff ``self`` is not trivially zero in at least one of
        the given expressions since most scalar fields are invertible and a
        complete computation would take too much time.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: one = M.scalar_field_algebra().one()
            sage: one.is_unit()
            True
            sage: zero = M.scalar_field_algebra().zero()
            sage: zero.is_unit()
            False
        """
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- a scalar field (or something else)

        OUTPUT: ``True`` if ``self`` is equal to ``other``, ``False`` otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y})
            sage: f == 1
            False
            sage: f == M.zero_scalar_field()
            False
            sage: g = M.scalar_field({X: x+y})
            sage: f == g
            True
            sage: h = M.scalar_field({X: 1})
            sage: h == M.one_scalar_field()
            True
            sage: h == 1
            True
        """
    def __ne__(self, other):
        """
        Non-equality operator.

        INPUT:

        - ``other`` -- a scalar field

        OUTPUT: ``True`` if ``self`` differs from ``other``, ``False`` otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y})
            sage: f != 1
            True
            sage: f != M.zero_scalar_field()
            True
            sage: g = M.scalar_field({X: x+y})
            sage: f != g
            False
        """
    def set_name(self, name=None, latex_name=None) -> None:
        """
        Set (or change) the text name and LaTeX name of the scalar field.

        INPUT:

        - ``name`` -- (string; default: ``None``) name given to the scalar
          field
        - ``latex_name`` -- (string; default: ``None``) LaTeX symbol to denote
          the scalar field; if ``None`` while ``name`` is provided, the LaTeX
          symbol is set to ``name``

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y})
            sage: f = M.scalar_field({X: x+y}); f
            Scalar field on the 2-dimensional topological manifold M
            sage: f.set_name('f'); f
            Scalar field f on the 2-dimensional topological manifold M
            sage: latex(f)
            f
            sage: f.set_name('f', latex_name=r'\\Phi'); f
            Scalar field f on the 2-dimensional topological manifold M
            sage: latex(f)
            \\Phi
        """
    def domain(self):
        """
        Return the open subset on which the scalar field is defined.

        OUTPUT:

        - instance of class
          :class:`~sage.manifolds.manifold.TopologicalManifold`
          representing the manifold's open subset on which the
          scalar field is defined

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x+2*y)
            sage: f.domain()
            2-dimensional topological manifold M
            sage: U = M.open_subset('U', coord_def={c_xy: x<0})
            sage: g = f.restrict(U)
            sage: g.domain()
            Open subset U of the 2-dimensional topological manifold M
        """
    def codomain(self):
        """
        Return the codomain of the scalar field.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x+2*y)
            sage: f.codomain()
            Real Field with 53 bits of precision
        """
    def copy(self, name=None, latex_name=None):
        """
        Return an exact copy of the scalar field.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the copy
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          copy; if none is provided, the LaTeX symbol is set to ``name``

        EXAMPLES:

        Copy on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x*y^2)
            sage: g = f.copy()
            sage: type(g)
            <class 'sage.manifolds.scalarfield_algebra.ScalarFieldAlgebra_with_category.element_class'>
            sage: g.expr()
            x*y^2
            sage: g == f
            True
            sage: g is f
            False
        """
    def copy_from(self, other) -> None:
        """
        Make ``self`` a copy of ``other``.

        INPUT:

        - ``other`` -- other scalar field, in the same module as ``self``

        .. NOTE::

            While the derived quantities are not copied, the name is kept.

        .. WARNING::

            All previous defined expressions and restrictions will be deleted!

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x*y^2, name='f')
            sage: f.display()
            f: M → ℝ
               (x, y) ↦ x*y^2
            sage: g = M.scalar_field(name='g')
            sage: g.copy_from(f)
            sage: g.display()
            g: M → ℝ
               (x, y) ↦ x*y^2
            sage: f == g
            True

        While the original scalar field is modified, the copy is not::

            sage: f.set_expr(x-y)
            sage: f.display()
            f: M → ℝ
               (x, y) ↦ x - y
            sage: g.display()
            g: M → ℝ
               (x, y) ↦ x*y^2
            sage: f == g
            False
        """
    def coord_function(self, chart=None, from_chart=None):
        """
        Return the function of the coordinates representing the scalar field
        in a given chart.

        INPUT:

        - ``chart`` -- (default: ``None``) chart with respect to which the
          coordinate expression is to be returned; if ``None``, the
          default chart of the scalar field's domain will be used
        - ``from_chart`` -- (default: ``None``) chart from which the
          required expression is computed if it is not known already in the
          chart ``chart``; if ``None``, a chart is picked in the known
          expressions

        OUTPUT:

        - instance of :class:`~sage.manifolds.chart_func.ChartFunction`
          representing the coordinate function of the scalar field in the
          given chart

        EXAMPLES:

        Coordinate function on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x*y^2)
            sage: f.coord_function()
            x*y^2
            sage: f.coord_function(c_xy)  # equivalent form (since c_xy is the default chart)
            x*y^2
            sage: type(f.coord_function())
            <class 'sage.manifolds.chart_func.ChartFunctionRing_with_category.element_class'>

        Expression via a change of coordinates::

            sage: c_uv.<u,v> = M.chart()
            sage: c_uv.transition_map(c_xy, [u+v, u-v])
            Change of coordinates from Chart (M, (u, v)) to Chart (M, (x, y))
            sage: f._express # at this stage, f is expressed only in terms of (x,y) coordinates
            {Chart (M, (x, y)): x*y^2}
            sage: f.coord_function(c_uv) # forces the computation of the expression of f in terms of (u,v) coordinates
            u^3 - u^2*v - u*v^2 + v^3
            sage: f.coord_function(c_uv) == (u+v)*(u-v)^2  # check
            True
            sage: f._express  # random (dict. output); f has now 2 coordinate expressions:
            {Chart (M, (x, y)): x*y^2, Chart (M, (u, v)): u^3 - u^2*v - u*v^2 + v^3}

        Usage in a physical context (simple Lorentz transformation - boost in
        ``x`` direction, with relative velocity ``v`` between ``o1``
        and ``o2`` frames)::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: o1.<t,x> = M.chart()
            sage: o2.<T,X> = M.chart()
            sage: f = M.scalar_field(x^2 - t^2)
            sage: f.coord_function(o1)
            -t^2 + x^2
            sage: v = var('v'); gam = 1/sqrt(1-v^2)
            sage: o2.transition_map(o1, [gam*(T - v*X), gam*(X - v*T)])
            Change of coordinates from Chart (M, (T, X)) to Chart (M, (t, x))
            sage: f.coord_function(o2)
            -T^2 + X^2
        """
    def expr(self, chart=None, from_chart=None):
        """
        Return the coordinate expression of the scalar field in a given
        chart.

        INPUT:

        - ``chart`` -- (default: ``None``) chart with respect to which the
          coordinate expression is required; if ``None``, the default
          chart of the scalar field's domain will be used
        - ``from_chart`` -- (default: ``None``) chart from which the
          required expression is computed if it is not known already in the
          chart ``chart``; if ``None``, a chart is picked in ``self._express``

        OUTPUT:

        - the coordinate expression of the scalar field in the given chart,
          either as a Sage's symbolic expression or as a SymPy object,
          depending on the symbolic calculus method used on the chart

        EXAMPLES:

        Expression of a scalar field on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x*y^2)
            sage: f.expr()
            x*y^2
            sage: f.expr(c_xy)  # equivalent form (since c_xy is the default chart)
            x*y^2

        Expression via a change of coordinates::

            sage: c_uv.<u,v> = M.chart()
            sage: c_uv.transition_map(c_xy, [u+v, u-v])
            Change of coordinates from Chart (M, (u, v)) to Chart (M, (x, y))
            sage: f._express # at this stage, f is expressed only in terms of (x,y) coordinates
            {Chart (M, (x, y)): x*y^2}
            sage: f.expr(c_uv) # forces the computation of the expression of f in terms of (u,v) coordinates
            u^3 - u^2*v - u*v^2 + v^3
            sage: bool( f.expr(c_uv) == (u+v)*(u-v)^2 ) # check
            True
            sage: f._express  # random (dict. output); f has now 2 coordinate expressions:
            {Chart (M, (x, y)): x*y^2, Chart (M, (u, v)): u^3 - u^2*v - u*v^2 + v^3}

        Note that the object returned by ``expr()`` depends on the symbolic
        backend used for coordinate computations::

            sage: type(f.expr())
            <class 'sage.symbolic.expression.Expression'>
            sage: M.set_calculus_method('sympy')
            sage: type(f.expr())
            <class 'sympy.core.mul.Mul'>
            sage: f.expr()  # note the SymPy exponent notation
            x*y**2
        """
    def set_expr(self, coord_expression, chart=None) -> None:
        """
        Set the coordinate expression of the scalar field.

        The expressions with respect to other charts are deleted, in order to
        avoid any inconsistency. To keep them, use :meth:`add_expr` instead.

        INPUT:

        - ``coord_expression`` -- coordinate expression of the scalar field
        - ``chart`` -- (default: ``None``) chart in which ``coord_expression``
          is defined; if ``None``, the default chart of the scalar field's
          domain is assumed

        EXAMPLES:

        Setting scalar field expressions on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x^2 + 2*x*y +1)
            sage: f._express
            {Chart (M, (x, y)): x^2 + 2*x*y + 1}
            sage: f.set_expr(3*y)
            sage: f._express  # the (x,y) expression has been changed:
            {Chart (M, (x, y)): 3*y}
            sage: c_uv.<u,v> = M.chart()
            sage: f.set_expr(cos(u)-sin(v), c_uv)
            sage: f._express # the (x,y) expression has been lost:
            {Chart (M, (u, v)): cos(u) - sin(v)}
            sage: f.set_expr(3*y)
            sage: f._express # the (u,v) expression has been lost:
            {Chart (M, (x, y)): 3*y}

        Since zero and one are special elements, their expressions cannot be
        changed::

            sage: z = M.zero_scalar_field()
            sage: z.set_expr(3*y)
            Traceback (most recent call last):
            ...
            ValueError: the expressions of an immutable element cannot be
             changed
            sage: one = M.one_scalar_field()
            sage: one.set_expr(3*y)
            Traceback (most recent call last):
            ...
            ValueError: the expressions of an immutable element cannot be
             changed
        """
    def add_expr(self, coord_expression, chart=None) -> None:
        """
        Add some coordinate expression to the scalar field.

        The previous expressions with respect to other charts are kept. To
        clear them, use :meth:`set_expr` instead.

        INPUT:

        - ``coord_expression`` -- coordinate expression of the scalar field
        - ``chart`` -- (default: ``None``) chart in which ``coord_expression``
          is defined; if ``None``, the default chart of the scalar field's
          domain is assumed

        .. WARNING::

            If the scalar field has already expressions in other charts, it
            is the user's responsibility to make sure that the expression
            to be added is consistent with them.

        EXAMPLES:

        Adding scalar field expressions on a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(x^2 + 2*x*y +1)
            sage: f._express
            {Chart (M, (x, y)): x^2 + 2*x*y + 1}
            sage: f.add_expr(3*y)
            sage: f._express  # the (x,y) expression has been changed:
            {Chart (M, (x, y)): 3*y}
            sage: c_uv.<u,v> = M.chart()
            sage: f.add_expr(cos(u)-sin(v), c_uv)
            sage: f._express # random (dict. output); f has now 2 expressions:
            {Chart (M, (x, y)): 3*y, Chart (M, (u, v)): cos(u) - sin(v)}

        Since zero and one are special elements, their expressions cannot be
        changed::

            sage: z = M.zero_scalar_field()
            sage: z.add_expr(cos(u)-sin(v), c_uv)
            Traceback (most recent call last):
            ...
            ValueError: the expressions of an immutable element cannot be
             changed
            sage: one = M.one_scalar_field()
            sage: one.add_expr(cos(u)-sin(v), c_uv)
            Traceback (most recent call last):
            ...
            ValueError: the expressions of an immutable element cannot be
             changed
        """
    def add_expr_by_continuation(self, chart, subdomain) -> None:
        """
        Set coordinate expression in a chart by continuation of the
        coordinate expression in a subchart.

        The continuation is performed by demanding that the coordinate
        expression is identical to that in the restriction of the chart to
        a given subdomain.

        INPUT:

        - ``chart`` -- coordinate chart `(U,(x^i))` in which the expression of
          the scalar field is to set
        - ``subdomain`` -- open subset `V\\subset U` in which the expression
          in terms of the restriction of the coordinate chart `(U,(x^i))` to
          `V` is already known or can be evaluated by a change of coordinates.

        EXAMPLES:

        Scalar field on the sphere `S^2`::

            sage: M = Manifold(2, 'S^2', structure='topological')
            sage: U = M.open_subset('U') ; V = M.open_subset('V') # the complement of resp. N pole and S pole
            sage: M.declare_union(U,V)   # S^2 is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart() # stereographic coordinates
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                intersection_name='W', restrictions1= x^2+y^2!=0,
            ....:                restrictions2= u^2+v^2!=0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W =  U.intersection(V)  # S^2 minus the two poles
            sage: f = M.scalar_field(atan(x^2+y^2), chart=c_xy, name='f')

        The scalar field has been defined only on the domain covered by the
        chart ``c_xy``, i.e. `U`::

            sage: f.display()
            f: S^2 → ℝ
            on U: (x, y) ↦ arctan(x^2 + y^2)
            on W: (u, v) ↦ arctan(1/(u^2 + v^2))

        We note that on `W = U \\cap V`, the expression of `f` in terms of
        coordinates `(u,v)` can be deduced from that in the coordinates
        `(x,y)` thanks to the transition map between the two charts::

            sage: f.display(c_uv.restrict(W))
            f: S^2 → ℝ
            on W: (u, v) ↦ arctan(1/(u^2 + v^2))

        We use this fact to extend the definition of `f` to the open
        subset `V`, covered by the chart ``c_uv``::

            sage: f.add_expr_by_continuation(c_uv, W)

        Then, `f` is known on the whole sphere::

            sage: f.display()
            f: S^2 → ℝ
            on U: (x, y) ↦ arctan(x^2 + y^2)
            on V: (u, v) ↦ arctan(1/(u^2 + v^2))
        """
    def set_restriction(self, rst) -> None:
        """
        Define a restriction of ``self`` to some subdomain.

        INPUT:

        - ``rst`` -- :class:`ScalarField` defined on a subdomain of
          the domain of ``self``

        EXAMPLES::

            sage: M = Manifold(2, 'M') # the 2-dimensional sphere S^2
            sage: U = M.open_subset('U') # complement of the North pole
            sage: c_xy.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: V = M.open_subset('V') # complement of the South pole
            sage: c_uv.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: M.declare_union(U,V)   # S^2 is the union of U and V
            sage: f = M.scalar_field(name='f')
            sage: g = U.scalar_field(x^2+y)
            sage: f.set_restriction(g)
            sage: f.display()
            f: M → ℝ
            on U: (x, y) ↦ x^2 + y
            sage: f.restrict(U) == g
            True
        """
    def display(self, chart: Chart | None = None) -> FormattedExpansion:
        """
        Display the expression of the scalar field in a given chart.

        Without any argument, this function displays all known, distinct
        expressions.

        INPUT:

        - ``chart`` -- (default: ``None``) chart with respect to which
          the coordinate expression is to be displayed; if ``None``, the
          display is performed in all the greatest charts in which the
          coordinate expression is known

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        EXAMPLES:

        Various displays::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: c_xy.<x,y> = M.chart()
            sage: f = M.scalar_field(sqrt(x+1), name='f')
            sage: f.display()
            f: M → ℝ
               (x, y) ↦ sqrt(x + 1)
            sage: latex(f.display())
            \\begin{array}{llcl} f:& M & \\longrightarrow & \\mathbb{R} \\\\ & \\left(x, y\\right) & \\longmapsto & \\sqrt{x + 1} \\end{array}
            sage: g = M.scalar_field(function('G')(x, y), name='g')
            sage: g.display()
            g: M → ℝ
               (x, y) ↦ G(x, y)
            sage: latex(g.display())
            \\begin{array}{llcl} g:& M & \\longrightarrow & \\mathbb{R} \\\\ & \\left(x, y\\right) & \\longmapsto & G\\left(x, y\\right) \\end{array}

        A shortcut of ``display()`` is ``disp()``::

            sage: f.disp()
            f: M → ℝ
               (x, y) ↦ sqrt(x + 1)

        In case the scalar field is piecewise-defined, the ``display()``
        command still outputs all expressions. Each expression displayed
        corresponds to the chart on the greatest domain where this particular
        expression is known::

            sage: U = M.open_subset('U')
            sage: f.set_expr(y^2, c_xy.restrict(U))
            sage: f.display()
            f: M → ℝ
            on U: (x, y) ↦ y^2
            sage: latex(f.display())
            \\begin{array}{llcl} f:& M & \\longrightarrow & \\mathbb{R} \\\\ \\text{on}\\ U : & \\left(x, y\\right) & \\longmapsto & y^{2} \\end{array}
        """
    disp = display
    def restrict(self, subdomain):
        """
        Restriction of the scalar field to an open subset of its domain of
        definition.

        INPUT:

        - ``subdomain`` -- an open subset of the scalar field's domain

        OUTPUT:

        - instance of :class:`ScalarField` representing the restriction of
          the scalar field to ``subdomain``

        EXAMPLES:

        Restriction of a scalar field defined on `\\RR^2` to the
        unit open disc::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()  # Cartesian coordinates
            sage: U = M.open_subset('U', coord_def={X: x^2+y^2 < 1}) # U unit open disc
            sage: f = M.scalar_field(cos(x*y), name='f')
            sage: f_U = f.restrict(U) ; f_U
            Scalar field f on the Open subset U of the 2-dimensional
             topological manifold M
            sage: f_U.display()
            f: U → ℝ
               (x, y) ↦ cos(x*y)
            sage: f.parent()
            Algebra of scalar fields on the 2-dimensional topological
             manifold M
            sage: f_U.parent()
            Algebra of scalar fields on the Open subset U of the 2-dimensional
             topological manifold M

        The restriction to the whole domain is the identity::

            sage: f.restrict(M) is f
            True
            sage: f_U.restrict(U) is f_U
            True

        Restriction of the zero scalar field::

            sage: M.zero_scalar_field().restrict(U)
            Scalar field zero on the Open subset U of the 2-dimensional
             topological manifold M
            sage: M.zero_scalar_field().restrict(U) is U.zero_scalar_field()
            True
        """
    def common_charts(self, other):
        """
        Find common charts for the expressions of the scalar field and
        ``other``.

        INPUT:

        - ``other`` -- a scalar field

        OUTPUT:

        - list of common charts; if no common chart is found, ``None`` is
          returned (instead of an empty list)

        EXAMPLES:

        Search for common charts on a 2-dimensional manifold with 2
        overlapping domains::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: U = M.open_subset('U')
            sage: c_xy.<x,y> = U.chart()
            sage: V = M.open_subset('V')
            sage: c_uv.<u,v> = V.chart()
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: f = U.scalar_field(x^2)
            sage: g = M.scalar_field(x+y)
            sage: f.common_charts(g)
            [Chart (U, (x, y))]
            sage: g.add_expr(u, c_uv)
            sage: f._express
            {Chart (U, (x, y)): x^2}
            sage: g._express  # random (dictionary output)
            {Chart (U, (x, y)): x + y, Chart (V, (u, v)): u}
            sage: f.common_charts(g)
            [Chart (U, (x, y))]

        Common charts found as subcharts: the subcharts are introduced via
        a transition map between charts c_xy and c_uv on the intersecting
        subdomain `W = U\\cap V`::

            sage: trans = c_xy.transition_map(c_uv, (x+y, x-y), 'W', x<0, u+v<0)
            sage: M.atlas()
            [Chart (U, (x, y)), Chart (V, (u, v)), Chart (W, (x, y)),
             Chart (W, (u, v))]
            sage: c_xy_W = M.atlas()[2]
            sage: c_uv_W = M.atlas()[3]
            sage: trans.inverse()
            Change of coordinates from Chart (W, (u, v)) to Chart (W, (x, y))
            sage: f.common_charts(g)
            [Chart (U, (x, y))]
            sage: f.expr(c_xy_W)
            x^2
            sage: f._express  # random (dictionary output)
            {Chart (U, (x, y)): x^2, Chart (W, (x, y)): x^2}
            sage: g._express  # random (dictionary output)
            {Chart (U, (x, y)): x + y, Chart (V, (u, v)): u}
            sage: g.common_charts(f)  # c_xy_W is not returned because it is subchart of 'xy'
            [Chart (U, (x, y))]
            sage: f.expr(c_uv_W)
            1/4*u^2 + 1/2*u*v + 1/4*v^2
            sage: f._express  # random (dictionary output)
            {Chart (U, (x, y)): x^2, Chart (W, (x, y)): x^2,
             Chart (W, (u, v)): 1/4*u^2 + 1/2*u*v + 1/4*v^2}
            sage: g._express  # random (dictionary output)
            {Chart (U, (x, y)): x + y, Chart (V, (u, v)): u}
            sage: f.common_charts(g)
            [Chart (U, (x, y)), Chart (W, (u, v))]
            sage: # the expressions have been updated on the subcharts
            sage: g._express #  random (dictionary output)
            {Chart (U, (x, y)): x + y, Chart (V, (u, v)): u,
             Chart (W, (u, v)): u}

        Common charts found by computing some coordinate changes::

            sage: W = U.intersection(V)
            sage: f = W.scalar_field(x^2, c_xy_W)
            sage: g = W.scalar_field(u+1, c_uv_W)
            sage: f._express
            {Chart (W, (x, y)): x^2}
            sage: g._express
            {Chart (W, (u, v)): u + 1}
            sage: f.common_charts(g)
            [Chart (W, (x, y)), Chart (W, (u, v))]
            sage: f._express # random (dictionary output)
            {Chart (W, (u, v)): 1/4*u^2 + 1/2*u*v + 1/4*v^2,
             Chart (W, (x, y)): x^2}
            sage: g._express # random (dictionary output)
            {Chart (W, (u, v)): u + 1, Chart (W, (x, y)): x + y + 1}

        TESTS:

        Check that :issue:`28072` has been fixed::

            sage: c_ab.<a,b> = W.chart()
            sage: xy_to_ab = c_xy_W.transition_map(c_ab, (3*y, x-y))
            sage: h = W.scalar_field(a+b, chart=c_ab)
            sage: f.common_charts(h)
            [Chart (W, (x, y))]
            sage: h.expr(c_xy_W)
            x + 2*y
        """
    def __call__(self, p, chart=None):
        """
        Compute the value of the scalar field at a given point.

        INPUT:

        - ``p`` -- point in the scalar field's domain
        - ``chart`` -- (default: ``None``) chart in which the coordinates
          of ``p`` are to be considered; if ``None``, a chart in which
          both ``p``'s coordinates and the expression of the scalar field
          are known is searched, starting from the default chart
          of ``self._domain``

        OUTPUT: value at ``p``

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name='f')
            sage: p = M((2,-5), name='p'); p
            Point p on the 2-dimensional topological manifold M
            sage: f.__call__(p)
            -3
            sage: f(p)
            -3
            sage: M.zero_scalar_field()(p)
            0
            sage: M.one_scalar_field()(p)
            1

        Example with a change of chart::

            sage: Y.<u,v> = M.chart()
            sage: X_to_Y = X.transition_map(Y, [x+y, x-y])
            sage: Y_to_X = X_to_Y.inverse()
            sage: g = M.scalar_field({Y: u*v}, name='g')
            sage: g(p)
            -21
            sage: p.coord(Y)
            (-3, 7)
        """
    def preimage(self, codomain_subset, name=None, latex_name=None):
        """
        Return the preimage of ``codomain_subset``.

        An alias is :meth:`pullback`.

        INPUT:

        - ``codomain_subset`` -- an instance of
          :class:`~sage.sets.real_set.RealSet`
        - ``name`` -- string; name (symbol) given to the subset
        - ``latex_name`` -- string (default: ``None``); LaTeX symbol to
          denote the subset; if none are provided, it is set to ``name``

        OUTPUT:

        - either a :class:`~sage.manifolds.manifold.TopologicalManifold` or
          a :class:`~sage.manifolds.subsets.pullback.ManifoldSubsetPullback`

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name='f')
            sage: L = f.pullback(RealSet.point(1)); latex(L)
            f^{-1}(\\{1\\})
            sage: M((-1, 1)) in L
            False
            sage: M((0, 1)) in L
            True

            sage: M.zero_scalar_field().preimage(RealSet.point(0)) is M
            True
        """
    pullback = preimage
    def __pos__(self):
        """
        Unary plus operator.

        OUTPUT: an exact copy of the scalar field

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name='f')
            sage: g = f.__pos__(); g
            Scalar field +f on the 2-dimensional topological manifold M
            sage: g == f
            True
        """
    def __neg__(self):
        """
        Unary minus operator.

        OUTPUT: the negative of the scalar field

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name='f')
            sage: g = f.__neg__(); g
            Scalar field -f on the 2-dimensional topological manifold M
            sage: g.display()
            -f: M → ℝ
               (x, y) ↦ -x - y
            sage: g.__neg__() == f
            True
        """
    def exp(self):
        '''
        Exponential of the scalar field.

        OUTPUT: the scalar field `\\exp f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = exp(f) ; g
            Scalar field exp(f) on the 2-dimensional topological manifold M
            sage: g.display()
            exp(f): M → ℝ
               (x, y) ↦ e^(x + y)
            sage: latex(g)
            \\exp\\left(\\Phi\\right)

        Automatic simplifications occur::

            sage: f = M.scalar_field({X: 2*ln(1+x^2)}, name=\'f\')
            sage: exp(f).display()
            exp(f): M → ℝ
               (x, y) ↦ x^4 + 2*x^2 + 1

        The inverse function is :meth:`log`::

            sage: log(exp(f)) == f
            True

        Some tests::

            sage: exp(M.zero_scalar_field()) == M.constant_scalar_field(1)
            True
            sage: exp(M.constant_scalar_field(1)) == M.constant_scalar_field(e)
            True
        '''
    def log(self):
        '''
        Natural logarithm of the scalar field.

        OUTPUT: the scalar field `\\ln f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = log(f) ; g
            Scalar field ln(f) on the 2-dimensional topological manifold M
            sage: g.display()
            ln(f): M → ℝ
               (x, y) ↦ log(x + y)
            sage: latex(g)
            \\ln\\left(\\Phi\\right)

        The inverse function is :meth:`exp`::

            sage: exp(log(f)) == f
            True
        '''
    def __pow__(self, exponent):
        """
        The scalar field to a given power.

        INPUT:

        - ``exponent`` -- the exponent

        OUTPUT:

        - the scalar field `f^a`, where `f` is the current scalar field and
          `a` the exponent

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x+y}, name='f', latex_name=r'\\Phi')
            sage: g = f.__pow__(pi) ; g
            Scalar field f^pi on the 2-dimensional topological manifold M
            sage: latex(g)
            {\\Phi}^{ \\pi }
            sage: g.display()
            f^pi: M → ℝ
               (x, y) ↦ (x + y)^pi

        The global function ``pow`` can be used::

            sage: pow(f, pi) == f.__pow__(pi)
            True

        as well as the exponent notation::

            sage: f^pi == f.__pow__(pi)
            True

        Some checks::

            sage: pow(f, 2) == f*f
            True
            sage: pow(pow(f, 1/2), 2) == f
            True
        """
    def sqrt(self):
        '''
        Square root of the scalar field.

        OUTPUT: the scalar field `\\sqrt f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: 1+x^2+y^2}, name=\'f\',
            ....:                    latex_name=r"\\Phi")
            sage: g = sqrt(f) ; g
            Scalar field sqrt(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\sqrt{\\Phi}
            sage: g.display()
            sqrt(f): M → ℝ
               (x, y) ↦ sqrt(x^2 + y^2 + 1)

        Some tests::

            sage: g^2 == f
            True
            sage: sqrt(M.zero_scalar_field()) == M.zero_scalar_field()
            True
        '''
    def cos(self):
        '''
        Cosine of the scalar field.

        OUTPUT: the scalar field `\\cos f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = cos(f) ; g
            Scalar field cos(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\cos\\left(\\Phi\\right)
            sage: g.display()
            cos(f): M → ℝ
               (x, y) ↦ cos(x*y)

        Some tests::

            sage: cos(M.zero_scalar_field()) == M.constant_scalar_field(1)
            True
            sage: cos(M.constant_scalar_field(pi/2)) == M.zero_scalar_field()
            True
        '''
    def sin(self):
        '''
        Sine of the scalar field.

        OUTPUT: the scalar field `\\sin f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = sin(f) ; g
            Scalar field sin(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\sin\\left(\\Phi\\right)
            sage: g.display()
            sin(f): M → ℝ
               (x, y) ↦ sin(x*y)

        Some tests::

            sage: sin(M.zero_scalar_field()) == M.zero_scalar_field()
            True
            sage: sin(M.constant_scalar_field(pi/2)) == M.constant_scalar_field(1)
            True
        '''
    def tan(self):
        '''
        Tangent of the scalar field.

        OUTPUT: the scalar field `\\tan f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = tan(f) ; g
            Scalar field tan(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\tan\\left(\\Phi\\right)
            sage: g.display()
            tan(f): M → ℝ
               (x, y) ↦ sin(x*y)/cos(x*y)

        Some tests::

            sage: tan(f) == sin(f) / cos(f)
            True
            sage: tan(M.zero_scalar_field()) == M.zero_scalar_field()
            True
            sage: tan(M.constant_scalar_field(pi/4)) == M.constant_scalar_field(1)
            True
        '''
    def arccos(self):
        '''
        Arc cosine of the scalar field.

        OUTPUT: the scalar field `\\arccos f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = arccos(f) ; g
            Scalar field arccos(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\arccos\\left(\\Phi\\right)
            sage: g.display()
            arccos(f): M → ℝ
               (x, y) ↦ arccos(x*y)

        The notation ``acos`` can be used as well::

            sage: acos(f)
            Scalar field arccos(f) on the 2-dimensional topological manifold M
            sage: acos(f) == g
            True

        Some tests::

            sage: cos(g) == f
            True
            sage: arccos(M.constant_scalar_field(1)) == M.zero_scalar_field()
            True
            sage: arccos(M.zero_scalar_field()) == M.constant_scalar_field(pi/2)
            True
        '''
    def arcsin(self):
        '''
        Arc sine of the scalar field.

        OUTPUT: the scalar field `\\arcsin f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = arcsin(f) ; g
            Scalar field arcsin(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\arcsin\\left(\\Phi\\right)
            sage: g.display()
            arcsin(f): M → ℝ
               (x, y) ↦ arcsin(x*y)

        The notation ``asin`` can be used as well::

            sage: asin(f)
            Scalar field arcsin(f) on the 2-dimensional topological manifold M
            sage: asin(f) == g
            True

        Some tests::

            sage: sin(g) == f
            True
            sage: arcsin(M.zero_scalar_field()) == M.zero_scalar_field()
            True
            sage: arcsin(M.constant_scalar_field(1)) == M.constant_scalar_field(pi/2)
            True
        '''
    def arctan(self):
        '''
        Arc tangent of the scalar field.

        OUTPUT: the scalar field `\\arctan f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = arctan(f) ; g
            Scalar field arctan(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\arctan\\left(\\Phi\\right)
            sage: g.display()
            arctan(f): M → ℝ
               (x, y) ↦ arctan(x*y)

        The notation ``atan`` can be used as well::

            sage: atan(f)
            Scalar field arctan(f) on the 2-dimensional topological manifold M
            sage: atan(f) == g
            True

        Some tests::

            sage: tan(g) == f
            True
            sage: arctan(M.zero_scalar_field()) == M.zero_scalar_field()
            True
            sage: arctan(M.constant_scalar_field(1)) == M.constant_scalar_field(pi/4)
            True
        '''
    def cosh(self):
        '''
        Hyperbolic cosine of the scalar field.

        OUTPUT: the scalar field `\\cosh f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = cosh(f) ; g
            Scalar field cosh(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\cosh\\left(\\Phi\\right)
            sage: g.display()
            cosh(f): M → ℝ
               (x, y) ↦ cosh(x*y)

        Some test::

            sage: cosh(M.zero_scalar_field()) == M.constant_scalar_field(1)
            True
        '''
    def sinh(self):
        '''
        Hyperbolic sine of the scalar field.

        OUTPUT: the scalar field `\\sinh f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = sinh(f) ; g
            Scalar field sinh(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\sinh\\left(\\Phi\\right)
            sage: g.display()
            sinh(f): M → ℝ
               (x, y) ↦ sinh(x*y)

        Some test::

            sage: sinh(M.zero_scalar_field()) == M.zero_scalar_field()
            True
        '''
    def tanh(self):
        '''
        Hyperbolic tangent of the scalar field.

        OUTPUT: the scalar field `\\tanh f`, where `f` is the current scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = tanh(f) ; g
            Scalar field tanh(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\tanh\\left(\\Phi\\right)
            sage: g.display()
            tanh(f): M → ℝ
               (x, y) ↦ sinh(x*y)/cosh(x*y)

        Some tests::

            sage: tanh(f) == sinh(f) / cosh(f)
            True
            sage: tanh(M.zero_scalar_field()) == M.zero_scalar_field()
            True
        '''
    def arccosh(self):
        '''
        Inverse hyperbolic cosine of the scalar field.

        OUTPUT:

        - the scalar field `\\mathrm{arccosh}\\, f`, where `f` is the current
          scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = arccosh(f) ; g
            Scalar field arccosh(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\,\\mathrm{arccosh}\\left(\\Phi\\right)
            sage: g.display()
            arccosh(f): M → ℝ
               (x, y) ↦ arccosh(x*y)

        The notation ``acosh`` can be used as well::

            sage: acosh(f)
            Scalar field arccosh(f) on the 2-dimensional topological manifold M
            sage: acosh(f) == g
            True

        Some tests::

            sage: cosh(g) == f
            True
            sage: arccosh(M.constant_scalar_field(1)) == M.zero_scalar_field()
            True
        '''
    def arcsinh(self):
        '''
        Inverse hyperbolic sine of the scalar field.

        OUTPUT:

        - the scalar field `\\mathrm{arcsinh}\\, f`, where `f` is the current
          scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = arcsinh(f) ; g
            Scalar field arcsinh(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\,\\mathrm{arcsinh}\\left(\\Phi\\right)
            sage: g.display()
            arcsinh(f): M → ℝ
               (x, y) ↦ arcsinh(x*y)

        The notation ``asinh`` can be used as well::

            sage: asinh(f)
            Scalar field arcsinh(f) on the 2-dimensional topological manifold M
            sage: asinh(f) == g
            True

        Some tests::

            sage: sinh(g) == f
            True
            sage: arcsinh(M.zero_scalar_field()) == M.zero_scalar_field()
            True
        '''
    def arctanh(self):
        '''
        Inverse hyperbolic tangent of the scalar field.

        OUTPUT:

        - the scalar field `\\mathrm{arctanh}\\, f`, where `f` is the current
          scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = arctanh(f) ; g
            Scalar field arctanh(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\,\\mathrm{arctanh}\\left(\\Phi\\right)
            sage: g.display()
            arctanh(f): M → ℝ
               (x, y) ↦ arctanh(x*y)

        The notation ``atanh`` can be used as well::

            sage: atanh(f)
            Scalar field arctanh(f) on the 2-dimensional topological manifold M
            sage: atanh(f) == g
            True

        Some tests::

            sage: tanh(g) == f
            True
            sage: arctanh(M.zero_scalar_field()) == M.zero_scalar_field()
            True
            sage: arctanh(M.constant_scalar_field(1/2)) == M.constant_scalar_field(log(3)/2)
            True
        '''
    def __abs__(self):
        '''
        Absolute value of the scalar field.

        OUTPUT:

        - the scalar field `\\mathrm{Abs}\\, f`, where `f` is the current
          scalar field

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field({X: x*y}, name=\'f\', latex_name=r"\\Phi")
            sage: g = abs(f) ; g
            Scalar field abs(f) on the 2-dimensional topological manifold M
            sage: latex(g)
            \\,\\mathrm{abs}\\left(\\Phi\\right)
            sage: g.display()
            abs(f): M → ℝ
               (x, y) ↦ abs(x)*abs(y)
        '''
    def set_calc_order(self, symbol, order, truncate: bool = False) -> None:
        '''
        Trigger a power series expansion with respect to a small parameter in
        computations involving the scalar field.

        This property is propagated by usual operations. The internal
        representation must be ``SR`` for this to take effect.

        If the small parameter is `\\epsilon` and `f` is ``self``, the
        power series expansion to order `n` is

        .. MATH::

            f = f_0 + \\epsilon f_1 + \\epsilon^2 f_2 + \\cdots + \\epsilon^n f_n
                + O(\\epsilon^{n+1}),

        where `f_0, f_1, \\ldots, f_n` are `n+1` scalar fields that do not
        depend upon `\\epsilon`.

        INPUT:

        - ``symbol`` -- symbolic variable (the "small parameter" `\\epsilon`)
          with respect to which the coordinate expressions of ``self`` in
          various charts are expanded in power series (around the zero value of
          this variable)
        - ``order`` -- integer; the order `n` of the expansion, defined as the
          degree of the polynomial representing the truncated power series in
          ``symbol``

          .. WARNING::

             The order of the big `O` in the power series expansion is `n+1`,
             where `n` is ``order``.

        - ``truncate`` -- boolean (default: ``False``); determines whether the
          coordinate expressions of ``self`` are replaced by their expansions
          to the given order

        EXAMPLES::

            sage: M = Manifold(2, \'M\', structure=\'topological\')
            sage: X.<x,y> = M.chart()
            sage: t = var(\'t\')  # the small parameter
            sage: f = M.scalar_field(exp(-t*x))
            sage: f.expr()
            e^(-t*x)
            sage: f.set_calc_order(t, 2, truncate=True)
            sage: f.expr()
            1/2*t^2*x^2 - t*x + 1
        '''
    def set_immutable(self) -> None:
        """
        Set ``self`` and all restrictions of ``self`` immutable.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: U = M.open_subset('U', coord_def={X: x^2+y^2<1})  # disk
            sage: V = M.open_subset('U', coord_def={X: x>0})  # half plane
            sage: f = M.scalar_field(x^2, name='f')
            sage: fU = f.restrict(U)
            sage: f.set_immutable()
            sage: fU.is_immutable()
            True
            sage: f.restrict(V).is_immutable()
            True
        """
    @cached_method
    def __hash__(self):
        """
        Hash function.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: f = M.scalar_field(x^2, name='f')
            sage: f.set_immutable()
            sage: g = M.scalar_field(x^2, name='g')
            sage: g.set_immutable()

        Check whether equality implies equality of hash::

            sage: f == g
            True
            sage: hash(f) == hash(g)
            True

        Let us check that ``f`` can be used as a dictionary key::

            sage: {f: 1}[f]
            1
        """
