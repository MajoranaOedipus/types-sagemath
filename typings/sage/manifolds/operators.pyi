def grad(scalar):
    """
    Gradient operator.

    The *gradient* of a scalar field `f` on a pseudo-Riemannian manifold
    `(M,g)` is the vector field `\\mathrm{grad}\\, f` whose components in any
    coordinate frame are

    .. MATH::

        (\\mathrm{grad}\\, f)^i = g^{ij} \\frac{\\partial F}{\\partial x^j}

    where the `x^j`'s are the coordinates with respect to which the
    frame is defined and `F` is the chart function representing `f` in
    these coordinates: `f(p) = F(x^1(p),\\ldots,x^n(p))` for any point `p`
    in the chart domain.
    In other words, the gradient of `f` is the vector field that is the
    `g`-dual of the differential of `f`.

    INPUT:

    - ``scalar`` -- scalar field `f`, as an instance of
      :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`

    OUTPUT:

    - instance of
      :class:`~sage.manifolds.differentiable.vectorfield.VectorField`
      representing `\\mathrm{grad}\\, f`

    EXAMPLES:

    Gradient of a scalar field in the Euclidean plane::

        sage: E.<x,y> = EuclideanSpace()
        sage: f = E.scalar_field(sin(x*y), name='f')
        sage: from sage.manifolds.operators import grad
        sage: grad(f)
        Vector field grad(f) on the Euclidean plane E^2
        sage: grad(f).display()
        grad(f) = y*cos(x*y) e_x + x*cos(x*y) e_y
        sage: grad(f)[:]
        [y*cos(x*y), x*cos(x*y)]

    See the method
    :meth:`~sage.manifolds.differentiable.scalarfield.DiffScalarField.gradient`
    of :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField` for
    more details and examples.
    """
def div(tensor):
    """
    Divergence operator.

    Let `t` be a tensor field of type `(k,0)` with `k\\geq 1` on a
    pseudo-Riemannian manifold `(M, g)`. The *divergence* of `t` is the tensor
    field of type `(k-1,0)` defined by

    .. MATH::

        (\\mathrm{div}\\, t)^{a_1\\ldots a_{k-1}} =
            \\nabla_i t^{a_1\\ldots a_{k-1} i} =
            (\\nabla t)^{a_1\\ldots a_{k-1} i}_{\\phantom{a_1\\ldots a_{k-1} i}\\, i}

    where `\\nabla` is the Levi-Civita connection of `g` (cf.
    :class:`~sage.manifolds.differentiable.levi_civita_connection.LeviCivitaConnection`).

    Note that the divergence is taken on the *last* index of the tensor field.
    This definition is extended to tensor fields of type `(k,l)` with
    `k\\geq 0` and `l\\geq 1`, by raising the last index with the metric `g`:
    `\\mathrm{div}\\, t` is then the tensor field of type `(k,l-1)` defined by

    .. MATH::

        (\\mathrm{div}\\, t)^{a_1\\ldots a_k}_{\\phantom{a_1\\ldots a_k}\\, b_1\\ldots b_{l-1}}
        = \\nabla_i (g^{ij} t^{a_1\\ldots a_k}_{\\phantom{a_1\\ldots a_k}\\, b_1\\ldots b_{l-1} j})
        = (\\nabla t^\\sharp)^{a_1\\ldots a_k i}_{\\phantom{a_1\\ldots a_k i}\\, b_1\\ldots b_{l-1} i}

    where `t^\\sharp` is the tensor field deduced from `t` by raising the
    last index with the metric `g` (see
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.up`).

    INPUT:

    - ``tensor`` -- tensor field `t` on a pseudo-Riemannian manifold `(M,g)`,
      as an instance of
      :class:`~sage.manifolds.differentiable.tensorfield.TensorField` (possibly
      via one of its derived classes, like
      :class:`~sage.manifolds.differentiable.vectorfield.VectorField`)

    OUTPUT:

    - the divergence of ``tensor`` as an instance of either
      :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`
      if `(k,l)=(1,0)` (``tensor`` is a vector field) or `(k,l)=(0,1)`
      (``tensor`` is a 1-form) or of
      :class:`~sage.manifolds.differentiable.tensorfield.TensorField`
      if `k+l\\geq 2`

    EXAMPLES:

    Divergence of a vector field in the Euclidean plane::

        sage: E.<x,y> = EuclideanSpace()
        sage: v = E.vector_field(cos(x*y), sin(x*y), name='v')
        sage: v.display()
        v = cos(x*y) e_x + sin(x*y) e_y
        sage: from sage.manifolds.operators import div
        sage: s = div(v); s
        Scalar field div(v) on the Euclidean plane E^2
        sage: s.display()
        div(v): E^2 → ℝ
           (x, y) ↦ x*cos(x*y) - y*sin(x*y)
        sage: s.expr()
        x*cos(x*y) - y*sin(x*y)

    See the method
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.divergence`
    of :class:`~sage.manifolds.differentiable.tensorfield.TensorField` for
    more details and examples.
    """
def curl(vector):
    """
    Curl operator.

    The *curl* of a vector field `v` on an orientable pseudo-Riemannian
    manifold `(M,g)` of dimension 3 is the vector field defined by

    .. MATH::

        \\mathrm{curl}\\, v = (*(\\mathrm{d} v^\\flat))^\\sharp

    where `v^\\flat` is the 1-form associated to `v` by the metric `g` (see
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.down`),
    `*(\\mathrm{d} v^\\flat)` is the Hodge dual with respect to `g` of the
    2-form `\\mathrm{d} v^\\flat` (exterior derivative of `v^\\flat`) (see
    :meth:`~sage.manifolds.differentiable.diff_form.DiffForm.hodge_dual`)
    and
    `(*(\\mathrm{d} v^\\flat))^\\sharp` is corresponding vector field by
    `g`-duality (see
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.up`).

    An alternative expression of the curl is

    .. MATH::

        (\\mathrm{curl}\\, v)^i = \\epsilon^{ijk} \\nabla_j v_k

    where `\\nabla` is the Levi-Civita connection of `g` (cf.
    :class:`~sage.manifolds.differentiable.levi_civita_connection.LeviCivitaConnection`)
    and `\\epsilon` the volume 3-form (Levi-Civita tensor) of `g` (cf.
    :meth:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric.volume_form`)

    INPUT:

    - ``vector`` -- vector field on an orientable 3-dimensional
      pseudo-Riemannian manifold, as an instance of
      :class:`~sage.manifolds.differentiable.vectorfield.VectorField`

    OUTPUT:

    - instance of
      :class:`~sage.manifolds.differentiable.vectorfield.VectorField`
      representing the curl of ``vector``

    EXAMPLES:

    Curl of a vector field in the Euclidean 3-space::

        sage: E.<x,y,z> = EuclideanSpace()
        sage: v = E.vector_field(sin(y), sin(x), 0, name='v')
        sage: v.display()
        v = sin(y) e_x + sin(x) e_y
        sage: from sage.manifolds.operators import curl
        sage: s = curl(v); s
        Vector field curl(v) on the Euclidean space E^3
        sage: s.display()
        curl(v) = (cos(x) - cos(y)) e_z
        sage: s[:]
        [0, 0, cos(x) - cos(y)]

    See the method
    :meth:`~sage.manifolds.differentiable.vectorfield.VectorField.curl`
    of :class:`~sage.manifolds.differentiable.vectorfield.VectorField` for more
    details and examples.
    """
def laplacian(field):
    """
    Laplace-Beltrami operator.

    The *Laplace-Beltrami operator* on a pseudo-Riemannian manifold `(M,g)`
    is the operator

    .. MATH::

        \\Delta =  \\nabla_i \\nabla^i = g^{ij} \\nabla_i \\nabla_j

    where `\\nabla` is the Levi-Civita connection of the metric `g` (cf.
    :class:`~sage.manifolds.differentiable.levi_civita_connection.LeviCivitaConnection`)
    and `\\nabla^i := g^{ij} \\nabla_j`

    INPUT:

    - ``field`` -- a scalar field `f` (instance of
      :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`) or a
      tensor field `f` (instance of
      :class:`~sage.manifolds.differentiable.tensorfield.TensorField`) on a
      pseudo-Riemannian manifold

    OUTPUT:

    - `\\Delta f`, as an instance of
      :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField` or of
      :class:`~sage.manifolds.differentiable.tensorfield.TensorField`

    EXAMPLES:

    Laplacian of a scalar field on the Euclidean plane::

        sage: E.<x,y> = EuclideanSpace()
        sage: f = E.scalar_field(sin(x*y), name='f')
        sage: from sage.manifolds.operators import laplacian
        sage: Df = laplacian(f); Df
        Scalar field Delta(f) on the Euclidean plane E^2
        sage: Df.display()
        Delta(f): E^2 → ℝ
           (x, y) ↦ -(x^2 + y^2)*sin(x*y)
        sage: Df.expr()
        -(x^2 + y^2)*sin(x*y)

    The Laplacian of a scalar field is the divergence of its gradient::

        sage: from sage.manifolds.operators import div, grad
        sage: Df == div(grad(f))
        True

    See the method
    :meth:`~sage.manifolds.differentiable.scalarfield.DiffScalarField.laplacian`
    of :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField` and
    the method
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.laplacian`
    of :class:`~sage.manifolds.differentiable.tensorfield.TensorField` for
    more details and examples.
    """
def dalembertian(field):
    """
    d'Alembert operator.

    The *d'Alembert operator* or *d'Alembertian* on a Lorentzian manifold
    `(M,g)` is nothing but the Laplace-Beltrami operator:

    .. MATH::

        \\Box =  \\nabla_i \\nabla^i = g^{ij} \\nabla_i \\nabla_j

    where `\\nabla` is the Levi-Civita connection of the metric `g` (cf.
    :class:`~sage.manifolds.differentiable.levi_civita_connection.LeviCivitaConnection`)
    and `\\nabla^i := g^{ij} \\nabla_j`

    INPUT:

    - ``field`` -- a scalar field `f` (instance of
      :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`) or a
      tensor field `f` (instance of
      :class:`~sage.manifolds.differentiable.tensorfield.TensorField`) on a
      pseudo-Riemannian manifold

    OUTPUT:

    - `\\Box f`, as an instance of
      :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField` or of
      :class:`~sage.manifolds.differentiable.tensorfield.TensorField`

    EXAMPLES:

    d'Alembertian of a scalar field in the 2-dimensional Minkowski spacetime::

        sage: M = Manifold(2, 'M', structure='Lorentzian')
        sage: X.<t,x> = M.chart()
        sage: g = M.metric()
        sage: g[0,0], g[1,1] = -1, 1
        sage: f = M.scalar_field((x-t)^3 + (x+t)^2, name='f')
        sage: from sage.manifolds.operators import dalembertian
        sage: Df = dalembertian(f); Df
        Scalar field Box(f) on the 2-dimensional Lorentzian manifold M
        sage: Df.display()
        Box(f): M → ℝ
           (t, x) ↦ 0

    See the method
    :meth:`~sage.manifolds.differentiable.scalarfield.DiffScalarField.dalembertian`
    of :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField` and
    the method
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.dalembertian`
    of :class:`~sage.manifolds.differentiable.tensorfield.TensorField` for
    more details and examples.
    """
