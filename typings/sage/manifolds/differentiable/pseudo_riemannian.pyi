from sage.manifolds.differentiable.manifold import DifferentiableManifold as DifferentiableManifold
from sage.manifolds.structure import LorentzianStructure as LorentzianStructure, PseudoRiemannianStructure as PseudoRiemannianStructure, RiemannianStructure as RiemannianStructure
from sage.rings.infinity import infinity as infinity

class PseudoRiemannianManifold(DifferentiableManifold):
    '''
    PseudoRiemannian manifold.

    A *pseudo-Riemannian manifold* is a pair `(M,g)` where `M` is a real
    differentiable manifold `M` (see
    :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`)
    and `g` is a field of non-degenerate symmetric bilinear forms on `M`, which
    is called the *metric tensor*, or simply the *metric* (see
    :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`).

    Two important subcases are

    - *Riemannian manifold*: the metric `g` is positive definite, i.e. its
      signature is `n = \\dim M`;
    - *Lorentzian manifold*: the metric `g` has signature `n-2` (positive
      convention) or `2-n` (negative convention).

    INPUT:

    - ``n`` -- positive integer; dimension of the manifold
    - ``name`` -- string; name (symbol) given to the manifold
    - ``metric_name`` -- (default: ``None``) string; name (symbol) given to the
      metric; if ``None``, ``\'g\'`` is used
    - ``signature`` -- (default: ``None``) signature `S` of the metric as a
      single integer: `S = n_+ - n_-`, where `n_+` (resp. `n_-`) is the
      number of positive terms (resp. number of negative terms) in any
      diagonal writing of the metric components; if ``signature`` is not
      provided, `S` is set to the manifold\'s dimension (Riemannian
      signature)
    - ``base_manifold`` -- (default: ``None``) if not ``None``, must be a
      differentiable manifold; the created object is then an open subset of
      ``base_manifold``
    - ``diff_degree`` -- (default: ``infinity``) degree `k` of
      differentiability
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the manifold; if none is provided, it is set to ``name``
    - ``metric_latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the metric; if none is provided, it is set to ``metric_name``
    - ``start_index`` -- (default: 0) integer; lower value of the range of
      indices used for "indexed objects" on the manifold, e.g. coordinates
      in a chart
    - ``category`` -- (default: ``None``) to specify the category; if ``None``,
      ``Manifolds(RR).Differentiable()`` (or ``Manifolds(RR).Smooth()``
      if ``diff_degree`` = ``infinity``) is assumed (see the category
      :class:`~sage.categories.manifolds.Manifolds`)
    - ``unique_tag`` -- (default: ``None``) tag used to force the construction
      of a new object when all the other arguments have been used previously
      (without ``unique_tag``, the
      :class:`~sage.structure.unique_representation.UniqueRepresentation`
      behavior inherited from
      :class:`~sage.manifolds.subset.ManifoldSubset`, via
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
      and :class:`~sage.manifolds.manifold.TopologicalManifold`,
      would return the previously constructed object corresponding to these
      arguments).

    EXAMPLES:

    Pseudo-Riemannian manifolds are constructed via the generic function
    :func:`~sage.manifolds.manifold.Manifold`, using the keyword
    ``structure``::

        sage: M = Manifold(4, \'M\', structure=\'pseudo-Riemannian\', signature=0)
        sage: M
        4-dimensional pseudo-Riemannian manifold M
        sage: M.category()
        Category of smooth manifolds over Real Field with 53 bits of precision

    The metric associated with ``M`` is::

        sage: M.metric()
        Pseudo-Riemannian metric g on the 4-dimensional pseudo-Riemannian
         manifold M
        sage: M.metric().signature()
        0
        sage: M.metric().tensor_type()
        (0, 2)

    Its value has to be initialized either by setting its components in various
    vector frames (see the above examples regarding the 2-sphere and Minkowski
    spacetime) or by making it equal to a given field of symmetric bilinear
    forms (see the method
    :meth:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric.set`
    of the metric class). Both methods are also covered in the
    documentation of method :meth:`metric` below.

    The metric object belongs to the class
    :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`::

        sage: isinstance(M.metric(), sage.manifolds.differentiable.metric.
        ....:                        PseudoRiemannianMetric)
        True

    See the documentation of this class for all operations available on
    metrics.

    The default name of the metric is ``g``; it can be customized::

        sage: M = Manifold(4, \'M\', structure=\'pseudo-Riemannian\',
        ....:              metric_name=\'gam\', metric_latex_name=r\'\\gamma\')
        sage: M.metric()
        Riemannian metric gam on the 4-dimensional Riemannian manifold M
        sage: latex(M.metric())
        \\gamma

    A Riemannian manifold is constructed by the proper setting of the keyword
    ``structure``::

        sage: M = Manifold(4, \'M\', structure=\'Riemannian\'); M
        4-dimensional Riemannian manifold M
        sage: M.metric()
        Riemannian metric g on the 4-dimensional Riemannian manifold M
        sage: M.metric().signature()
        4

    Similarly, a Lorentzian manifold is obtained by::

        sage: M = Manifold(4, \'M\', structure=\'Lorentzian\'); M
        4-dimensional Lorentzian manifold M
        sage: M.metric()
        Lorentzian metric g on the 4-dimensional Lorentzian manifold M

    The default Lorentzian signature is taken to be positive::

        sage: M.metric().signature()
        2

    but one can opt for the negative convention via the keyword ``signature``::

        sage: M = Manifold(4, \'M\', structure=\'Lorentzian\', signature=\'negative\')
        sage: M.metric()
        Lorentzian metric g on the 4-dimensional Lorentzian manifold M
        sage: M.metric().signature()
        -2
    '''
    def __init__(self, n, name, metric_name=None, signature=None, base_manifold=None, diff_degree=..., latex_name=None, metric_latex_name=None, start_index: int = 0, category=None, unique_tag=None) -> None:
        """
        Construct a pseudo-Riemannian manifold.

        TESTS::

            sage: M = Manifold(4, 'M', structure='pseudo-Riemannian',
            ....:              signature=0)
            sage: M
            4-dimensional pseudo-Riemannian manifold M
            sage: type(M)
            <class 'sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold_with_category'>
            sage: X.<w,x,y,z> = M.chart()
            sage: M.metric()
            Pseudo-Riemannian metric g on the 4-dimensional pseudo-Riemannian manifold M
            sage: TestSuite(M).run()
        """
    def metric(self, name=None, signature=None, latex_name=None, dest_map=None):
        """
        Return the metric giving the pseudo-Riemannian structure to the
        manifold, or define a new metric tensor on the manifold.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the metric; if
          ``name`` is ``None`` or matches the name of the metric defining the
          pseudo-Riemannian structure of ``self``, the latter metric is
          returned
        - ``signature`` -- (default: ``None``; ignored if ``name`` is ``None``)
          signature `S` of the metric as a single integer: `S = n_+ - n_-`,
          where `n_+` (resp. `n_-`) is the number of positive terms (resp.
          number of negative terms) in any diagonal writing of the metric
          components; if ``signature`` is not provided, `S` is set to the
          manifold's dimension (Riemannian signature)
        - ``latex_name`` -- (default: ``None``; ignored if ``name`` is ``None``)
          LaTeX symbol to denote the metric; if ``None``, it is formed from
          ``name``
        - ``dest_map`` -- (default: ``None``; ignored if ``name`` is ``None``)
          instance of
          class :class:`~sage.manifolds.differentiable.diff_map.DiffMap`
          representing the destination map `\\Phi:\\ U \\rightarrow M`, where `U`
          is the current manifold; if ``None``, the identity map is assumed
          (case of a metric tensor field *on* `U`)

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`

        EXAMPLES:

        Metric of a 3-dimensional Riemannian manifold::

            sage: M = Manifold(3, 'M', structure='Riemannian', start_index=1)
            sage: X.<x,y,z> = M.chart()
            sage: g = M.metric(); g
            Riemannian metric g on the 3-dimensional Riemannian manifold M

        The metric remains to be initialized, for instance by setting its
        components in the coordinate frame associated to the chart ``X``::

            sage: g[1,1], g[2,2], g[3,3] = 1, 1, 1
            sage: g.display()
            g = dx⊗dx + dy⊗dy + dz⊗dz

        Alternatively, the metric can be initialized from a given field of
        nondegenerate symmetric bilinear forms; we may create the former
        object by::

            sage: X.coframe()
            Coordinate coframe (M, (dx,dy,dz))
            sage: dx, dy, dz = X.coframe()[1], X.coframe()[2], X.coframe()[3]
            sage: b = dx*dx + dy*dy + dz*dz
            sage: b
            Field of symmetric bilinear forms dx⊗dx+dy⊗dy+dz⊗dz on the
             3-dimensional Riemannian manifold M

        We then use the metric method
        :meth:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric.set`
        to make ``g`` being equal to ``b`` as a symmetric tensor field of
        type ``(0,2)``::

            sage: g.set(b)
            sage: g.display()
            g = dx⊗dx + dy⊗dy + dz⊗dz

        Another metric can be defined on ``M`` by specifying a metric name
        distinct from that chosen at the creation of the manifold (which
        is ``g`` by default, but can be changed thanks to the keyword
        ``metric_name`` in :func:`~sage.manifolds.manifold.Manifold`)::

            sage: h = M.metric('h'); h
            Riemannian metric h on the 3-dimensional Riemannian manifold M
            sage: h[1,1], h[2,2], h[3,3] = 1+y^2, 1+z^2, 1+x^2
            sage: h.display()
            h = (y^2 + 1) dx⊗dx + (z^2 + 1) dy⊗dy + (x^2 + 1) dz⊗dz

        The metric tensor ``h`` is distinct from the metric entering in the
        definition of the Riemannian manifold ``M``::

            sage: h is M.metric()
            False

        while we have of course::

            sage: g is M.metric()
            True

        Providing the same name as the manifold's default metric returns the
        latter::

            sage: M.metric('g') is M.metric()
            True

        In the present case (``M`` is diffeomorphic to `\\RR^3`), we can even
        create a Lorentzian metric on ``M``::

            sage: h = M.metric('h', signature=1); h
            Lorentzian metric h on the 3-dimensional Riemannian manifold M
        """
    def volume_form(self, contra: int = 0):
        """
        Volume form (Levi-Civita tensor) `\\epsilon` associated with ``self``.

        This assumes that ``self`` is an orientable manifold, with a
        preferred orientation; see
        :meth:`~sage.manifolds.differentiable.manifold.DifferentiableManifold.orientation`
        for details.

        The volume form `\\epsilon` is a `n`-form (`n` being the manifold's
        dimension) such that, for any vector frame `(e_i)` that is orthonormal
        with respect to the metric of the pseudo-Riemannian manifold ``self``,

        .. MATH::

            \\epsilon(e_1,\\ldots,e_n) = \\pm 1

        There are only two such `n`-forms, which are opposite of each other.
        The volume form `\\epsilon` is selected as the one that returns `+1` for
        any right-handed vector frame with respect to the chosen orientation of
        ``self``.

        INPUT:

        - ``contra`` -- (default: 0) number of contravariant indices of the
          returned tensor

        OUTPUT:

        - if ``contra = 0`` (default value): the volume `n`-form `\\epsilon`, as
          an instance of
          :class:`~sage.manifolds.differentiable.diff_form.DiffForm`
        - if ``contra = k``, with `1\\leq k \\leq n`, the tensor field of type
          (k,n-k) formed from `\\epsilon` by raising the first k indices with
          the metric (see method
          :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.up`);
          the output is then an instance of
          :class:`~sage.manifolds.differentiable.tensorfield.TensorField`, with
          the appropriate antisymmetries, or of the subclass
          :class:`~sage.manifolds.differentiable.multivectorfield.MultivectorField`
          if `k=n`

        EXAMPLES:

        Volume form of the Euclidean 3-space::

            sage: M = Manifold(3, 'M', structure='Riemannian', start_index=1)
            sage: X.<x,y,z> = M.chart()
            sage: g = M.metric()
            sage: g[1,1], g[2,2], g[3,3] = 1, 1, 1
            sage: eps = M.volume_form(); eps
            3-form eps_g on the 3-dimensional Riemannian manifold M
            sage: eps.display()
            eps_g = dx∧dy∧dz

        Raising the first index::

            sage: eps1 = M.volume_form(1); eps1
            Tensor field of type (1,2) on the 3-dimensional Riemannian
             manifold M
            sage: eps1.display()
            ∂/∂x⊗dy⊗dz - ∂/∂x⊗dz⊗dy - ∂/∂y⊗dx⊗dz + ∂/∂y⊗dz⊗dx + ∂/∂z⊗dx⊗dy
             - ∂/∂z⊗dy⊗dx
            sage: eps1.symmetries()
            no symmetry; antisymmetry: (1, 2)

        Raising the first and second indices::

            sage: eps2 = M.volume_form(2); eps2
            Tensor field of type (2,1) on the 3-dimensional Riemannian
             manifold M
            sage: eps2.display()
            ∂/∂x⊗∂/∂y⊗dz - ∂/∂x⊗∂/∂z⊗dy - ∂/∂y⊗∂/∂x⊗dz + ∂/∂y⊗∂/∂z⊗dx
             + ∂/∂z⊗∂/∂x⊗dy - ∂/∂z⊗∂/∂y⊗dx
            sage: eps2.symmetries()
            no symmetry; antisymmetry: (0, 1)

        Fully contravariant version::

            sage: eps3 = M.volume_form(3); eps3
            3-vector field on the 3-dimensional Riemannian manifold M
            sage: eps3.display()
            ∂/∂x∧∂/∂y∧∂/∂z
        """
    def open_subset(self, name, latex_name=None, coord_def={}, supersets=None):
        """
        Create an open subset of ``self``.

        An open subset is a set that is (i) included in the manifold and (ii)
        open with respect to the manifold's topology. It is a differentiable
        manifold by itself. Moreover, equipped with the restriction of the
        manifold metric to itself, it is a pseudo-Riemannian manifold. Hence
        the returned object is an instance of
        :class:`PseudoRiemannianManifold`.

        INPUT:

        - ``name`` -- name given to the open subset
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          subset; if none is provided, it is set to ``name``
        - ``coord_def`` -- (default: {}) definition of the subset in
          terms of coordinates; ``coord_def`` must a be dictionary with keys
          charts in the manifold's atlas and values the symbolic expressions
          formed by the coordinates to define the subset.
        - ``supersets`` -- (default: only ``self``) list of sets that the
          new open subset is a subset of

        OUTPUT:

        - instance of :class:`PseudoRiemannianManifold` representing the
          created open subset

        EXAMPLES:

        Open subset of a 2-dimensional Riemannian manifold::

            sage: M = Manifold(2, 'M', structure='Riemannian')
            sage: X.<x,y> = M.chart()
            sage: U = M.open_subset('U', coord_def={X: x>0}); U
            Open subset U of the 2-dimensional Riemannian manifold M
            sage: type(U)
            <class 'sage.manifolds.differentiable.pseudo_riemannian.PseudoRiemannianManifold_with_category'>

        We initialize the metric of ``M``::

            sage: g = M.metric()
            sage: g[0,0], g[1,1] = 1, 1

        Then the metric on ``U`` is determined as the restriction of ``g`` to
        ``U``::

            sage: gU = U.metric(); gU
            Riemannian metric g on the Open subset U of the 2-dimensional Riemannian manifold M
            sage: gU.display()
            g = dx⊗dx + dy⊗dy
            sage: gU is g.restrict(U)
            True

        TESTS:

        Open subset created after the initialization of the metric::

            sage: V = M.open_subset('V', coord_def={X: x<0}); V
            Open subset V of the 2-dimensional Riemannian manifold M
            sage: gV = V.metric()
            sage: gV.display()
            g = dx⊗dx + dy⊗dy
            sage: gV is g.restrict(V)
            True
        """
