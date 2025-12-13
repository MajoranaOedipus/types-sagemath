from sage.manifolds.differentiable.scalarfield import DiffScalarField as DiffScalarField
from sage.manifolds.scalarfield_algebra import ScalarFieldAlgebra as ScalarFieldAlgebra
from sage.rings.infinity import infinity as infinity
from sage.symbolic.ring import SymbolicRing as SymbolicRing

class DiffScalarFieldAlgebra(ScalarFieldAlgebra):
    """
    Commutative algebra of differentiable scalar fields on a differentiable
    manifold.

    If `M` is a differentiable manifold of class `C^k` over a topological
    field `K`, the *commutative algebra of scalar fields on* `M` is the set
    `C^k(M)` of all `k`-times continuously differentiable maps `M\\rightarrow K`.
    The set `C^k(M)` is an algebra over `K`, whose ring product is the
    pointwise multiplication of `K`-valued functions, which is clearly
    commutative.

    If `K = \\RR` or `K = \\CC`, the field `K` over which the
    algebra `C^k(M)` is constructed is represented by Sage's Symbolic Ring
    ``SR``, since there is no exact representation of `\\RR` nor `\\CC` in Sage.

    Via its base class
    :class:`~sage.manifolds.scalarfield_algebra.ScalarFieldAlgebra`,
    the class :class:`DiffScalarFieldAlgebra` inherits from
    :class:`~sage.structure.parent.Parent`, with the category set to
    :class:`~sage.categories.commutative_algebras.CommutativeAlgebras`.
    The corresponding *element* class is
    :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`.

    INPUT:

    - ``domain`` -- the differentiable manifold `M` on which the scalar fields
      are defined (must be an instance of class
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`)

    EXAMPLES:

    Algebras of scalar fields on the sphere `S^2` and on some open subset of
    it::

        sage: M = Manifold(2, 'M') # the 2-dimensional sphere S^2
        sage: U = M.open_subset('U') # complement of the North pole
        sage: c_xy.<x,y> = U.chart() # stereographic coordinates from the North pole
        sage: V = M.open_subset('V') # complement of the South pole
        sage: c_uv.<u,v> = V.chart() # stereographic coordinates from the South pole
        sage: M.declare_union(U,V)   # S^2 is the union of U and V
        sage: xy_to_uv = c_xy.transition_map(c_uv, (x/(x^2+y^2), y/(x^2+y^2)),
        ....:                 intersection_name='W', restrictions1= x^2+y^2!=0,
        ....:                 restrictions2= u^2+v^2!=0)
        sage: uv_to_xy = xy_to_uv.inverse()
        sage: CM = M.scalar_field_algebra() ; CM
        Algebra of differentiable scalar fields on the 2-dimensional
         differentiable manifold M
        sage: W = U.intersection(V)  # S^2 minus the two poles
        sage: CW = W.scalar_field_algebra() ; CW
        Algebra of differentiable scalar fields on the Open subset W of the
         2-dimensional differentiable manifold M

    `C^k(M)` and `C^k(W)` belong to the category of commutative
    algebras over `\\RR` (represented here by Sage's Symbolic Ring)::

        sage: CM.category()
        Join of Category of commutative algebras over Symbolic Ring and Category of homsets of topological spaces
        sage: CM.base_ring()
        Symbolic Ring
        sage: CW.category()
        Join of Category of commutative algebras over Symbolic Ring and Category of homsets of topological spaces
        sage: CW.base_ring()
        Symbolic Ring

    The elements of `C^k(M)` are scalar fields on `M`::

        sage: CM.an_element()
        Scalar field on the 2-dimensional differentiable manifold M
        sage: CM.an_element().display()  # this sample element is a constant field
        M → ℝ
        on U: (x, y) ↦ 2
        on V: (u, v) ↦ 2

    Those of `C^k(W)` are scalar fields on `W`::

        sage: CW.an_element()
        Scalar field on the Open subset W of the 2-dimensional differentiable
         manifold M
        sage: CW.an_element().display()  # this sample element is a constant field
        W → ℝ
        (x, y) ↦ 2
        (u, v) ↦ 2

    The zero element::

        sage: CM.zero()
        Scalar field zero on the 2-dimensional differentiable manifold M
        sage: CM.zero().display()
        zero: M → ℝ
        on U: (x, y) ↦ 0
        on V: (u, v) ↦ 0

    ::

        sage: CW.zero()
        Scalar field zero on the Open subset W of the 2-dimensional
         differentiable manifold M
        sage: CW.zero().display()
        zero: W → ℝ
           (x, y) ↦ 0
           (u, v) ↦ 0

    The unit element::

        sage: CM.one()
        Scalar field 1 on the 2-dimensional differentiable manifold M
        sage: CM.one().display()
        1: M → ℝ
        on U: (x, y) ↦ 1
        on V: (u, v) ↦ 1

    ::

        sage: CW.one()
        Scalar field 1 on the Open subset W of the 2-dimensional differentiable
         manifold M
        sage: CW.one().display()
        1: W → ℝ
        (x, y) ↦ 1
        (u, v) ↦ 1

    A generic element can be constructed as for any parent in Sage, namely
    by means of the ``__call__`` operator on the parent (here with the
    dictionary of the coordinate expressions defining the scalar field)::

        sage: f = CM({c_xy: atan(x^2+y^2), c_uv: pi/2 - atan(u^2+v^2)}); f
        Scalar field on the 2-dimensional differentiable manifold M
        sage: f.display()
        M → ℝ
        on U: (x, y) ↦ arctan(x^2 + y^2)
        on V: (u, v) ↦ 1/2*pi - arctan(u^2 + v^2)
        sage: f.parent()
        Algebra of differentiable scalar fields on the 2-dimensional
         differentiable manifold M

    Specific elements can also be constructed in this way::

        sage: CM(0) == CM.zero()
        True
        sage: CM(1) == CM.one()
        True

    Note that the zero scalar field is cached::

        sage: CM(0) is CM.zero()
        True

    Elements can also be constructed by means of the method
    :meth:`~sage.manifolds.manifold.TopologicalManifold.scalar_field` acting on
    the domain (this allows one to set the name of the scalar field at the
    construction)::

        sage: f1 = M.scalar_field({c_xy: atan(x^2+y^2), c_uv: pi/2 - atan(u^2+v^2)},
        ....:                     name='f')
        sage: f1.parent()
        Algebra of differentiable scalar fields on the 2-dimensional
         differentiable manifold M
        sage: f1 == f
        True
        sage: M.scalar_field(0, chart='all') == CM.zero()
        True

    The algebra `C^k(M)` coerces to `C^k(W)` since `W` is an open
    subset of `M`::

        sage: CW.has_coerce_map_from(CM)
        True

    The reverse is of course false::

        sage: CM.has_coerce_map_from(CW)
        False

    The coercion map is nothing but the restriction to `W` of scalar fields
    on `M`::

        sage: fW = CW(f) ; fW
        Scalar field on the Open subset W of the 2-dimensional differentiable
         manifold M
        sage: fW.display()
        W → ℝ
        (x, y) ↦ arctan(x^2 + y^2)
        (u, v) ↦ 1/2*pi - arctan(u^2 + v^2)

    ::

        sage: CW(CM.one()) == CW.one()
        True

    The coercion map allows for the addition of elements of `C^k(W)`
    with elements of `C^k(M)`, the result being an element of
    `C^k(W)`::

        sage: s = fW + f
        sage: s.parent()
        Algebra of differentiable scalar fields on the Open subset W of the
         2-dimensional differentiable manifold M
        sage: s.display()
        W → ℝ
        (x, y) ↦ 2*arctan(x^2 + y^2)
        (u, v) ↦ pi - 2*arctan(u^2 + v^2)

    Another coercion is that from the Symbolic Ring, the parent of all
    symbolic expressions (cf. :class:`~sage.symbolic.ring.SymbolicRing`).
    Since the Symbolic Ring is the base ring for the algebra ``CM``, the
    coercion of a symbolic expression ``s`` is performed by the operation
    ``s*CM.one()``, which invokes the reflected multiplication operator
    :meth:`sage.manifolds.scalarfield.ScalarField._rmul_`. If the symbolic
    expression does not involve any chart coordinate, the outcome is a
    constant scalar field::

        sage: h = CM(pi*sqrt(2)) ; h
        Scalar field on the 2-dimensional differentiable manifold M
        sage: h.display()
        M → ℝ
        on U: (x, y) ↦ sqrt(2)*pi
        on V: (u, v) ↦ sqrt(2)*pi
        sage: a = var('a')
        sage: h = CM(a); h.display()
        M → ℝ
        on U: (x, y) ↦ a
        on V: (u, v) ↦ a

    If the symbolic expression involves some coordinate of one of the
    manifold's charts, the outcome is initialized only on the chart domain::

        sage: h = CM(a+x); h.display()
        M → ℝ
        on U: (x, y) ↦ a + x
        on W: (u, v) ↦ (a*u^2 + a*v^2 + u)/(u^2 + v^2)
        sage: h = CM(a+u); h.display()
        M → ℝ
        on W: (x, y) ↦ (a*x^2 + a*y^2 + x)/(x^2 + y^2)
        on V: (u, v) ↦ a + u

    If the symbolic expression involves coordinates of different charts,
    the scalar field is created as a Python object, but is not initialized,
    in order to avoid any ambiguity::

        sage: h = CM(x+u); h.display()
        M → ℝ

    .. RUBRIC:: TESTS OF THE ALGEBRA LAWS:

    Ring laws::

        sage: h = CM(pi*sqrt(2))
        sage: s = f + h ; s
        Scalar field on the 2-dimensional differentiable manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ sqrt(2)*pi + arctan(x^2 + y^2)
        on V: (u, v) ↦ 1/2*pi*(2*sqrt(2) + 1) - arctan(u^2 + v^2)

    ::

        sage: s = f - h ; s
        Scalar field on the 2-dimensional differentiable manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ -sqrt(2)*pi + arctan(x^2 + y^2)
        on V: (u, v) ↦ -1/2*pi*(2*sqrt(2) - 1) - arctan(u^2 + v^2)

    ::

        sage: s = f*h ; s
        Scalar field on the 2-dimensional differentiable manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ sqrt(2)*pi*arctan(x^2 + y^2)
        on V: (u, v) ↦ 1/2*sqrt(2)*(pi^2 - 2*pi*arctan(u^2 + v^2))

    ::

        sage: s = f/h ; s
        Scalar field on the 2-dimensional differentiable manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ 1/2*sqrt(2)*arctan(x^2 + y^2)/pi
        on V: (u, v) ↦ 1/4*sqrt(2)*(pi - 2*arctan(u^2 + v^2))/pi

    ::

        sage: f*(h+f) == f*h + f*f
        True

    Ring laws with coercion::

        sage: f - fW == CW.zero()
        True
        sage: f/fW == CW.one()
        True
        sage: s = f*fW ; s
        Scalar field on the Open subset W of the 2-dimensional differentiable
         manifold M
        sage: s.display()
        W → ℝ
        (x, y) ↦ arctan(x^2 + y^2)^2
        (u, v) ↦ 1/4*pi^2 - pi*arctan(u^2 + v^2) + arctan(u^2 + v^2)^2
        sage: s/f == fW
        True

    Multiplication by a number::

        sage: s = 2*f ; s
        Scalar field on the 2-dimensional differentiable manifold M
        sage: s.display()
        M → ℝ
        on U: (x, y) ↦ 2*arctan(x^2 + y^2)
        on V: (u, v) ↦ pi - 2*arctan(u^2 + v^2)

    ::

        sage: 0*f == CM.zero()
        True
        sage: 1*f == f
        True
        sage: 2*(f/2) == f
        True
        sage: (f+2*f)/3 == f
        True
        sage: 1/3*(f+2*f) == f
        True

    The Sage test suite for algebras is passed::

        sage: TestSuite(CM).run()

    It is passed also for `C^k(W)`::

        sage: TestSuite(CW).run()
    """
    Element = DiffScalarField
    def __init__(self, domain) -> None:
        """
        Construct an algebra of differentiable scalar fields.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: CM = M.scalar_field_algebra(); CM
            Algebra of differentiable scalar fields on the 2-dimensional
             differentiable manifold M
            sage: type(CM)
            <class 'sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra_with_category'>
            sage: type(CM).__base__
            <class 'sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra'>
            sage: TestSuite(CM).run()
        """
