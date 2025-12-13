from sage.manifolds.differentiable.degenerate import DegenerateManifold as DegenerateManifold, TangentTensor as TangentTensor
from sage.manifolds.differentiable.differentiable_submanifold import DifferentiableSubmanifold as DifferentiableSubmanifold
from sage.manifolds.differentiable.metric import DegenerateMetric as DegenerateMetric
from sage.manifolds.differentiable.pseudo_riemannian import PseudoRiemannianManifold as PseudoRiemannianManifold
from sage.manifolds.differentiable.vectorfield_module import VectorFieldModule as VectorFieldModule
from sage.matrix.constructor import matrix as matrix
from sage.rings.infinity import infinity as infinity
from sage.symbolic.expression import Expression as Expression

class DegenerateSubmanifold(DegenerateManifold, DifferentiableSubmanifold):
    '''
    Degenerate submanifolds.

    An *embedded (resp. immersed) degenerate submanifold of a proper
    pseudo-Riemannian manifold* `(M,g)` is an embedded (resp. immersed)
    submanifold `H` of `M` as a differentiable manifold such that pull
    back of the metric tensor `g` via the embedding (resp. immersion)
    endows `H` with the structure of a degenerate manifold.

    INPUT:

    - ``n`` -- positive integer; dimension of the manifold
    - ``name`` -- string; name (symbol) given to the manifold
    - ``ambient`` -- (default: ``None``) pseudo-Riemannian manifold `M` in
      which the submanifold is embedded (or immersed). If ``None``, it is set
      to ``self``
    - ``metric_name`` -- (default: ``None``) string; name (symbol) given to the
      metric; if ``None``, ``\'g\'`` is used
    - ``signature`` -- (default: ``None``) signature `S` of the metric as a
      tuple: `S = (n_+, n_-, n_0)`, where `n_+` (resp. `n_-`, resp. `n_0`) is the
      number of positive terms (resp. negative terms, resp. zero tems) in any
      diagonal writing of the metric components; if ``signature`` is not
      provided, `S` is set to `(ndim-1, 0, 1)`, being `ndim` the manifold\'s dimension
    - ``base_manifold`` -- (default: ``None``) if not ``None``, must be a
      topological manifold; the created object is then an open subset of
      ``base_manifold``
    - ``diff_degree`` -- (default: ``infinity``) degree of differentiability
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the manifold; if none are provided, it is set to ``name``
    - ``metric_latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the metric; if none is provided, it is set to ``metric_name``
    - ``start_index`` -- (default: 0) integer; lower value of the range of
      indices used for "indexed objects" on the manifold, e.g., coordinates
      in a chart
      - ``category`` -- (default: ``None``) to specify the category; if
      ``None``, ``Manifolds(field)`` is assumed (see the category
      :class:`~sage.categories.manifolds.Manifolds`)
    - ``unique_tag`` -- (default: ``None``) tag used to force the construction
      of a new object when all the other arguments have been used previously
      (without ``unique_tag``, the
      :class:`~sage.structure.unique_representation.UniqueRepresentation`
      behavior inherited from
      :class:`~sage.manifolds.subset.ManifoldSubset`
      would return the previously constructed object corresponding to these
      arguments)

    .. SEEALSO::

        :mod:`~sage.manifolds.manifold` and
        :mod:`~sage.manifolds.differentiable.differentiable_submanifold`
    '''
    def __init__(self, n, name, ambient=None, metric_name=None, signature=None, base_manifold=None, diff_degree=..., latex_name=None, metric_latex_name=None, start_index: int = 0, category=None, unique_tag=None) -> None:
        """
        Construct a degenerate submanifold.

        EXAMPLES:

        A `2`-dimensional degenerate submanifold of a Lorentzian manifold::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: S = Manifold(2, 'S', ambient=M, structure='degenerate_metric')
            sage: S
            2-dimensional degenerate submanifold S embedded in 4-dimensional
            differentiable manifold M
        """
    def ambient_metric(self):
        """
        Return the metric of the ambient manifold. The submanifold has to be
        embedded

        OUTPUT: the metric of the ambient manifold

        EXAMPLES:

        The lightcone of the 3D Minkowski space::

            sage: M = Manifold(3, 'M', structure='Lorentzian')
            sage: X.<t,x,y> = M.chart()
            sage: S = Manifold(2, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [sqrt(u^2+v^2), u, v]},
            ....:           name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x, y]}, name='Phi_inv',
            ....:               latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: S.ambient_metric()
            Lorentzian metric g on the 3-dimensional Lorentzian manifold M
        """
    def default_screen(self):
        """
        Return the default screen distribution.

        OUTPUT:

        - an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi)  # long time
            sage: S.default_screen()              # long time
            screen distribution Sc along the degenerate hypersurface S embedded
            in 4-dimensional differentiable manifold M mapped into the 4-dimensional
            Lorentzian manifold M
        """
    def list_of_screens(self):
        """
        Return the default screen distribution.

        OUTPUT:

        - an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:                  name='Phi', latex_name=r'\\Phi')
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:                      latex_name=r'\\Phi^{-1}')
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi)  # long time
            sage: S.list_of_screens()             # long time
            {'Sc': screen distribution Sc along the degenerate hypersurface S
            embedded in 4-dimensional differentiable manifold M mapped into the
            4-dimensional Lorentzian manifold M}
        """
    def set_transverse(self, rigging=None, normal=None) -> None:
        """
        For setting a transversal distribution of the degenerate submanifold.

        According to the type of the submanifold among the 4 possible types,
        one must enter a list of normal transversal vector fields and/or a
        list of transversal and not normal vector fields spanning a transverse
        distribution.

        INPUT:

        - ``rigging`` -- list or tuple (default: ``None``); list of vector fields
          of the ambient manifold or chart function; of the ambient manifold in
          the latter case, the corresponding gradient vector field with respect to
          the ambient metric is calculated; the vectors must be linearly independent,
          transversal to the submanifold but not normal
        - ``normal`` -- list or tuple (default: ``None``); list of vector fields
          of the ambient manifold or chart function; of the ambient manifold in
          the latter case, the corresponding gradient vector field with respect to
          the ambient metric is calculated; the vectors must be linearly independent,
          transversal and normal to the submanifold

        EXAMPLES:

        The lightcone of the 3-dimensional Minkowski space `\\RR^3_1`::

            sage: M = Manifold(3, 'M', structure='Lorentzian')
            sage: X.<t,x,y> = M.chart()
            sage: S = Manifold(2, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [sqrt(u^2+v^2), u, v]},
            ....:                   name='Phi', latex_name=r'\\Phi')
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x, y]}, name='Phi_inv',
            ....:                           latex_name=r'\\Phi^{-1}')
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2] = -1,1,1
            sage: S.set_transverse(rigging=t)
        """
    def screen(self, name, screen, rad, latex_name=None):
        """
        For setting a screen distribution and vector fields of the radical distribution
        that will be used for computations

        INPUT:

        - ``name`` -- string (default: ``None``); name given to the screen
        - ``latex_name`` -- string (default: ``None``); LaTeX symbol to denote
          the screen; if ``None``, the LaTeX symbol is set to ``name``
        - ``screen`` -- list or tuple  of vector fields
          of the ambient manifold or chart function; of the ambient manifold in
          the latter case, the corresponding gradient vector field with respect to
          the ambient metric is calculated; the vectors must be linearly independent,
          tangent to the submanifold but not normal
        - ``rad`` -- -- list or tuple  of vector fields
          of the ambient manifold or chart function; of the ambient manifold in
          the latter case, the corresponding gradient vector field with respect to
          the ambient metric is calculated; the vectors must be linearly independent,
          tangent and normal to the submanifold

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi); Sc  # long time
            screen distribution Sc along the degenerate hypersurface S embedded
            in 4-dimensional differentiable manifold M mapped into the 4-dimensional
            Lorentzian manifold M
        """
    def induced_metric(self) -> DegenerateMetric:
        """
        Return the pullback of the ambient metric.

        OUTPUT:

        - induced metric, as an instance of
          :class:`~sage.manifolds.differentiable.metric.DegenerateMetric`

        EXAMPLES:

        Section of the lightcone of the Minkowski space with a hyperplane
        passing through the origin::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(2, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [sqrt(u^2+v^2), u, v, 0]},
            ....:             name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x, y]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: h = S.induced_metric(); h  # long time
            degenerate metric gamma on the 2-dimensional degenerate
            submanifold S embedded in 4-dimensional differentiable manifold M
        """
    def first_fundamental_form(self):
        """
        Return the restriction of the ambient metric on vector field
        along the submanifold and tangent to it. It is difference from
        induced metric who gives the pullback of the ambient metric
        on the submanifold.

        OUTPUT:

        - the first fundamental form, as an instance of
          :class:`~sage.manifolds.differentiable.degenerate.TangentTensor`

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: h = S.first_fundamental_form()   # long time
        """
    def adapted_frame(self, screen=None):
        """
        Return a frame
        `(e_1,\\ldots,e_p, \\xi_1,\\ldots, \\xi_r, v_1,\\ldots, v_q, N_1, \\ldots, N_n)`
        of the ambient manifold along the submanifold, being `e_i` vector fields
        spanning the giving screen distribution, `\\xi_i` vector fields spanning
        radical distribution, `v_i` normal transversal vector fields, `N_i`
        rigging vector fields corresponding to the giving screen.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          if ``None`` default screen is used.

        OUTPUT: a frame on the ambient manifold along the submanifold

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: T = S.adapted_frame(); T         # long time
            Vector frame (S, (vv_0,vv_1,vv_2,vv_3)) with values on the 4-dimensional
            Lorentzian manifold M
        """
    def second_fundamental_form(self, screen=None):
        """

        This method is implemented only for null hypersurfaces. The method
        returns a tensor `B` of type `(0,2)` instance of
        :class:`~sage.manifolds.differentiable.degenerate.TangentTensor`
        such that for two vector fields `U, V` on the ambient manifold along
        the null hypersurface, one has:

        .. MATH::

            \\nabla_UV=D(U,V)+B(U,V)N

        being `\\nabla` the ambient connection, `D` the induced connection
        and `N` the chosen rigging.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          If ``None``, the default screen is used

        OUTPUT:

        - an instance of
          :class:`~sage.manifolds.differentiable.degenerate.TangentTensor`

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);   # long time
            sage: B = S.second_fundamental_form();  # long time
            sage: B.display()                       # long time
            B = 0
        """
    extrinsic_curvature = second_fundamental_form
    def projection(self, tensor, screen=None):
        """

        For a given tensor `T` of type `(r, 1)` on the ambient manifold, this
        method returns the tensor `T'` of type `(r,1)` such that for `r`
        vector fields `v_1,\\ldots,v_r`, `T'(v_1,\\ldots,v_r)` is the projection
        of  `T(v_1,\\ldots,v_r)` on ``self`` along the bundle spanned by the
        transversal vector fields provided by :meth:`set_transverse`.

        INPUT:

        - ``tensor`` -- a tensor of type `(r,1)` on the ambient manifold

        OUTPUT:

        - a tensor of type `(r,1)` on the ambient manifold along ``self``

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: U1 = S.projection(U)             # long time
        """
    def screen_projection(self, tensor, screen=None):
        """
        For a given tensor `T` of type `(r, 1)` on the ambient manifold, this
        method returns the tensor `T'` of type `(r,1)` such that for `r`
        vector fields `v_1,\\ldots,v_r`, `T'(v_1,\\ldots,v_r)` is the projection
        of  `T(v_1,\\ldots,v_r)` on the bundle spanned by ``screen`` along the
        bundle spanned by the transversal plus the radical vector fields provided.

        INPUT:

        - ``tensor`` -- a tensor of type `(r,1)` on the ambient manifold

        OUTPUT:

        - a tensor of type `(r,1)` on the ambient manifold

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: U1 = S.screen_projection(U);     # long time
        """
    def weingarten_map(self, screen=None):
        """

        This method is implemented only for hypersurfaces.
        *Weigarten map* is the `1`-form `W` defined for a vector field
        `U` tangent to ``self`` by

        .. MATH::

            W(U)=\\nabla_U\\xi

        being `\\nabla` the Levi-Civita connection of the ambient manifold
        and `\\xi` the chosen vector field spanning the radical distribution.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          If ``None`` the default screen is used.

        OUTPUT:

        - tensor of type `(1,1)` instance of
          :class:`~sage.manifolds.differentiable.degenerate.TangentTensor`

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: v = M.vector_field(); v[1] = 1
            sage: S.set_transverse(rigging=v)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: W = S.weingarten_map();          # long time
            sage: W.display()                      # long time
            nabla_g(xi)|X(S) = 0
        """
    def shape_operator(self, screen=None):
        """

        This method is implemented only for hypersurfaces.
        *shape operator* is the projection of the Weingarten map
        on the screen distribution along the radical distribution.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          If ``None`` the default screen is used.

        OUTPUT:

        - tensor of type `(1,1)` instance of
          :class:`~sage.manifolds.differentiable.degenerate.TangentTensor`

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: v = M.vector_field(); v[1] = 1
            sage: S.set_transverse(rigging=v)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: SO = S.shape_operator();         # long time
            sage: SO.display()                     # long time
            A^* = 0
        """
    def gauss_curvature(self, screen=None):
        """
        Gauss curvature is the product of all eigenfunctions of the shape operator.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          If ``None`` the default screen is used.

        OUTPUT: a scalar function on ``self``

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: K = S.gauss_curvature();         # long time
            sage: K.display()                      # long time
            S → ℝ
            (u, v, w) ↦ 0
        """
    def principal_directions(self, screen=None):
        """

        Principal directions are eigenvectors of the shape operator. This
        method is implemented only for hypersurfaces.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          If ``None`` default screen is used.

        OUTPUT:

        - list of pairs (vector field, scalar field) representing the
          principal directions and the associated principal curvatures

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi); T = S.adapted_frame()  # long time
            sage: PD = S.principal_directions()                          # long time
            sage: PD[2][0].display(T)                                    # long time
            e_2 = xi
        """
    def mean_curvature(self, screen=None):
        """

        Mean curvature is the sum of principal curvatures. This
        method is implemented only for hypersurfaces.

        INPUT:

        - ``screen`` -- (default: ``None``) an instance of
          :class:`~sage.manifolds.differentiable.degenerate_submanifold.Screen`.
          If ``None`` the default screen is used.

        OUTPUT: the mean curvature, as a scalar field on the submanifold

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: S.set_transverse(rigging=x)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: m = S.mean_curvature(); m        # long time
            Scalar field on the degenerate hypersurface S embedded in 4-dimensional
            differentiable manifold M
            sage: m.display()                      # long time
            S → ℝ
            (u, v, w) ↦ 0
        """
    def is_tangent(self, v):
        """
        Determine whether a vector field on the ambient manifold along ``self``
        is tangent to ``self`` or not.

        INPUT:

        - ``v`` -- field on the ambient manifold along ``self``

        OUTPUT:

        - ``True`` if ``v`` is everywhere tangent to ``self`` or ``False`` if
          not

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: v = M.vector_field(); v[1] = 1
            sage: S.set_transverse(rigging=v)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);  # long time
            sage: S.is_tangent(xi.along(Phi))      # long time
            True
            sage: S.is_tangent(v.along(Phi))       # long time
            False
        """

class Screen(VectorFieldModule):
    '''
    Let `H` be a lightlike submanifold embedded in a pseudo-Riemannian
    manifold `(M,g)` with `\\Phi` the embedding map. A screen distribution
    is a complementary `S(TH)` of the radical distribution `Rad(TM)=TH\\cap
    TH^\\perp` in `TH`. One then has

    .. MATH::

        TH=S(TH)\\oplus_{orth}Rad(TH)

    INPUT:

    - ``submanifold`` -- a lightlike submanifold, as an instance of
      :class:`DegenerateSubmanifold`
    - ``name`` -- name given to the screen distribution
    - ``screen`` -- vector fields of the ambient manifold which
      span the screen distribution
    - ``rad`` -- vector fields of the ambient manifold which
      span the radical distribution
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
      screen distribution; if ``None``, it is formed from ``name``

    EXAMPLES:

    The horizon of the Schwarzschild black hole::

        sage: M = Manifold(4, \'M\', structure=\'Lorentzian\')
        sage: X_M.<t, r, th, ph> = \\\n        ....: M.chart(r"t r:(0,oo) th:(0,pi):\\theta ph:(0,2*pi):\\phi")
        sage: var(\'m\'); assume(m>0)
        m
        sage: g = M.metric()
        sage: g[0,0], g[0,1], g[1,1], g[2,2], g[3,3] = \\\n        ....: -1+2*m/r, 2*m/r, 1+2*m/r, r^2, r^2*sin(th)^2
        sage: H = Manifold(3, \'H\', ambient=M, structure=\'degenerate_metric\')
        sage: X_H.<ht,hth,hph> = \\\n        ....: H.chart(r"ht:(-oo,oo):t hth:(0,pi):\\theta hph:(0,2*pi):\\phi")
        sage: Phi = H.diff_map(M, {(X_H, X_M): [ht, 2*m,hth, hph]}, \\\n        ....: name=\'Phi\', latex_name=r\'\\Phi\')
        sage: Phi_inv = M.diff_map(H, {(X_M, X_H): [t,th, ph]}, \\\n        ....: name=\'Phi_inv\', latex_name=r\'\\Phi^{-1}\')
        sage: H.set_immersion(Phi, inverse=Phi_inv); H.declare_embedding()
        sage: xi = M.vector_field(-1, 0, 0, 0)
        sage: v = M.vector_field(r, -r, 0, 0)
        sage: e1 = M.vector_field(0, 0, 1, 0)
        sage: e2 = M.vector_field(0, 0, 0, 1)

    A screen distribution for the Schwarzschild black hole horizon::

        sage: H.set_transverse(rigging=v)
        sage: S = H.screen(\'S\', [e1, e2], (xi)); S  # long time
        screen distribution S along the degenerate hypersurface H embedded
        in 4-dimensional differentiable manifold M mapped into the
        4-dimensional Lorentzian manifold M

    The corresponding normal tangent null vector field and null
    transversal vector field::

        sage: xi = S.normal_tangent_vector(); xi.display()  # long time
        xi = -∂/∂t
        sage: N = S.rigging(); N.display()  # long time
        N = ∂/∂t - ∂/∂r

    Those vector fields are normalized by `g(\\xi,N)=1`::

        sage: g.along(Phi)(xi, N).display()  # long time
        g(xi,N): H → ℝ
        (ht, hth, hph) ↦ 1

    '''
    def __init__(self, submanifold, name, screen, rad, latex_name=None) -> None:
        """

        TESTS::

            sage: M = Manifold(3, 'M', structure='Lorentzian')
            sage: X.<t,x,y> = M.chart()
            sage: S = Manifold(2, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [sqrt(u^2+v^2), u, v]},
            ....:                  name='Phi', latex_name=r'\\Phi')
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x, y]}, name='Phi_inv',
            ....:                      latex_name=r'\\Phi^{-1}')
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2] = -1,1,1
            sage: S.set_transverse(rigging=t)
            sage: xi = M.vector_field(); xi[0] = sqrt(x^2+y^2); xi[1] = x; xi[2] = y
            sage: U = M.vector_field(); U[1] = -y; U[2] = x
            sage: Sc = S.screen('Sc', U, xi);
        """
    def __getitem__(self, i):
        """
        Access vector fields spanning the screen distribution.

        INPUT:

        - ``i`` -- index of the coordinate; if the slice ``[:]``, then all
          the coordinates are returned

        OUTPUT:

        - a vector field on the ambient manifold that belong to
          the screen distribution

        TESTS::

            sage: M = Manifold(3, 'M', structure='Lorentzian')
            sage: X.<t,x,y> = M.chart()
            sage: S = Manifold(2, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [sqrt(u^2+v^2), u, v]},
            ....:                  name='Phi', latex_name=r'\\Phi')
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x, y]}, name='Phi_inv',
            ....:                      latex_name=r'\\Phi^{-1}')
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2] = -1,1,1
            sage: S.set_transverse(rigging=t)
            sage: xi = M.vector_field(); xi[0] = sqrt(x^2+y^2); xi[1] = x; xi[2] = y
            sage: U = M.vector_field(); U[1] = -y; U[2] = x
            sage: Sc = S.screen('Sc', U, xi);
            sage: Sc.__getitem__(0)
            Vector field along the degenerate hypersurface S embedded in
            3-dimensional differentiable manifold M with values on the 3-dimensional
            Lorentzian manifold M
        """
    def normal_tangent_vector(self):
        """
        Return either a list ``Rad`` of vector fields spanning the radical
        distribution or (in case of a hypersurface) a normal tangent null
        vector field spanning the radical distribution.

        OUTPUT:

        - either a list of vector fields or a single vector field in
          case of a hypersurface

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:                  name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:                      latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: v = M.vector_field(); v[1] = 1
            sage: S.set_transverse(rigging=v)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);                  # long time
            sage: Rad = Sc.normal_tangent_vector(); Rad.display()  # long time
            xi = ∂/∂t + ∂/∂x
        """
    def rigging(self):
        """
        Return either a list ``Rad`` of vector fields spanning the
        complementary of the normal distribution `TH^\\perp` in the
        transverse bundle or (when `H` is a null hypersurface) the
        null transversal vector field defined in [DB1996]_.

        OUTPUT:

        - either a list made by vector fields or a vector field in
          case of hypersurface

        EXAMPLES:

        A degenerate hyperplane the 4-dimensional Minkowski space `\\RR^4_1`::

            sage: M = Manifold(4, 'M', structure='Lorentzian')
            sage: X.<t,x,y,z> = M.chart()
            sage: S = Manifold(3, 'S', ambient=M, structure='degenerate_metric')
            sage: X_S.<u,v,w> = S.chart()
            sage: Phi = S.diff_map(M, {(X_S, X): [u, u, v, w]},
            ....:         name='Phi', latex_name=r'\\Phi');
            sage: Phi_inv = M.diff_map(S, {(X, X_S): [x,y, z]}, name='Phi_inv',
            ....:           latex_name=r'\\Phi^{-1}');
            sage: S.set_immersion(Phi, inverse=Phi_inv); S.declare_embedding()
            sage: g = M.metric()
            sage: g[0,0], g[1,1], g[2,2], g[3,3] = -1,1,1,1
            sage: v = M.vector_field(); v[1] = 1
            sage: S.set_transverse(rigging=v)
            sage: xi = M.vector_field(); xi[0] = 1; xi[1] = 1
            sage: U = M.vector_field(); U[2] = 1; V = M.vector_field(); V[3] = 1
            sage: Sc = S.screen('Sc', (U,V), xi);    # long time
            sage: rig = Sc.rigging(); rig.display()  # long time
            N = -1/2 ∂/∂t + 1/2 ∂/∂x
        """
