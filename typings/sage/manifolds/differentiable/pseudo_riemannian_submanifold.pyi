from sage.functions.other import factorial as factorial
from sage.manifolds.differentiable.degenerate import DegenerateManifold as DegenerateManifold
from sage.manifolds.differentiable.differentiable_submanifold import DifferentiableSubmanifold as DifferentiableSubmanifold
from sage.manifolds.differentiable.pseudo_riemannian import PseudoRiemannianManifold as PseudoRiemannianManifold
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.symbolic.ring import SR as SR

class PseudoRiemannianSubmanifold(PseudoRiemannianManifold, DifferentiableSubmanifold):
    '''
    Pseudo-Riemannian submanifold.

    An *embedded (resp. immersed) submanifold of a pseudo-Riemannian manifold*
    `(M,g)` is an embedded (resp. immersed) submanifold `N` of `M` as a
    differentiable manifold such that pull back of the metric tensor `g` via
    the embedding (resp. immersion) endows `N` with the structure of a
    pseudo-Riemannian manifold.

    INPUT:

    - ``n`` -- positive integer; dimension of the submanifold
    - ``name`` -- string; name (symbol) given to the submanifold
    - ``ambient`` -- (default: ``None``) pseudo-Riemannian manifold `M` in
      which the submanifold is embedded (or immersed). If ``None``, it is set
      to ``self``
    - ``metric_name`` -- (default: ``None``) string; name (symbol) given to the
      metric; if ``None``, ``\'gamma\'`` is used
    - ``signature`` -- (default: ``None``) signature `S` of the metric as a
      single integer: `S = n_+ - n_-`, where `n_+` (resp. `n_-`) is the
      number of positive terms (resp. number of negative terms) in any
      diagonal writing of the metric components; if ``signature`` is not
      provided, `S` is set to the submanifold\'s dimension (Riemannian
      signature)
    - ``base_manifold`` -- (default: ``None``) if not ``None``, must be a
      differentiable manifold; the created object is then an open subset of
      ``base_manifold``
    - ``diff_degree`` -- (default: ``infinity``) degree of differentiability
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the submanifold; if none is provided, it is set to ``name``
    - ``metric_latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the metric; if none is provided, it is set to ``metric_name`` if
      the latter is not ``None`` and to ``r\'\\gamma\'`` otherwise
    - ``start_index`` -- (default: 0) integer; lower value of the range of
      indices used for "indexed objects" on the submanifold, e.g. coordinates
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

    Let `N` be a 2-dimensional submanifold of a 3-dimensional Riemannian
    manifold `M`::

        sage: M = Manifold(3, \'M\', structure =\'Riemannian\')
        sage: N = Manifold(2, \'N\', ambient=M, structure=\'Riemannian\')
        sage: N
        2-dimensional Riemannian submanifold N immersed in the 3-dimensional
         Riemannian manifold M
        sage: CM.<x,y,z> = M.chart()
        sage: CN.<u,v> = N.chart()

    Let us define a 1-dimension foliation indexed by `t`. The inverse map is
    needed in order to compute the adapted chart in the ambient manifold::

        sage: t = var(\'t\')
        sage: phi = N.diff_map(M, {(CN,CM):[u, v, t+u^2+v^2]}); phi
        Differentiable map from the 2-dimensional Riemannian submanifold N
         immersed in the 3-dimensional Riemannian manifold M to the
         3-dimensional Riemannian manifold M
        sage: phi_inv = M.diff_map(N,{(CM, CN): [x,y]})
        sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})

    `\\phi` can then be declared as an embedding `N\\to M`::

        sage: N.set_embedding(phi, inverse=phi_inv, var=t,
        ....:                 t_inverse={t: phi_inv_t})

    The foliation can also be used to find new charts on the ambient manifold
    that are adapted to the foliation, ie in which the expression of the
    immersion is trivial. At the same time, the appropriate coordinate changes
    are computed::

        sage: N.adapted_chart()
        [Chart (M, (u_M, v_M, t_M))]
        sage: len(M.coord_changes())
        2

    .. SEEALSO::

        :mod:`~sage.manifolds.manifold` and
        :mod:`~sage.manifolds.differentiable.differentiable_submanifold`
    '''
    def __init__(self, n, name, ambient=None, metric_name=None, signature=None, base_manifold=None, diff_degree=..., latex_name=None, metric_latex_name=None, start_index: int = 0, category=None, unique_tag=None) -> None:
        '''
        Construct a pseudo-Riemannian submanifold.

        TESTS::

            sage: M = Manifold(3, \'M\', structure=\'Lorentzian\')
            sage: N = Manifold(2, \'N\', ambient=M, structure=\'Riemannian\')
            sage: N
            2-dimensional Riemannian submanifold N immersed in the
             3-dimensional Lorentzian manifold M
            sage: phi = N.diff_map(M)
            sage: N.set_embedding(phi)
            sage: N
            2-dimensional Riemannian submanifold N embedded in the
             3-dimensional Lorentzian manifold M
            sage: S = Manifold(2, \'S\', latex_name=r"\\Sigma", ambient=M,
            ....:              structure=\'Riemannian\', start_index=1)
            sage: latex(S)
            \\Sigma
            sage: S.start_index()
            1

        ::

            sage: M = Manifold(5, \'M\', structure=\'pseudo-Riemannian\',
            ....:              signature=1)
            sage: N = Manifold(4, \'N\', ambient=M,
            ....:              structure=\'pseudo-Riemannian\', signature=0)
            sage: N
            4-dimensional pseudo-Riemannian submanifold N immersed in the
             5-dimensional pseudo-Riemannian manifold M
        '''
    def open_subset(self, name, latex_name=None, coord_def={}, supersets=None):
        """
        Create an open subset of ``self``.

        An open subset is a set that is (i) included in the manifold and (ii)
        open with respect to the manifold's topology. It is a differentiable
        manifold by itself. Moreover, equipped with the restriction of the
        manifold metric to itself, it is a pseudo-Riemannian manifold.

        As ``self`` is a submanifold of its ambient manifold,
        the new open subset is also considered a submanifold of that.
        Hence the returned object is an instance of
        :class:`PseudoRiemannianSubmanifold`.

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

        - instance of :class:`PseudoRiemannianSubmanifold` representing the
          created open subset

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='Riemannian')
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian'); N
            2-dimensional Riemannian submanifold N immersed in the
             3-dimensional Riemannian manifold M
            sage: S = N.subset('S'); S
            Subset S of the
             2-dimensional Riemannian submanifold N immersed in the
              3-dimensional Riemannian manifold M
            sage: O = N.subset('O', is_open=True); O  # indirect doctest
            Open subset O of the
             2-dimensional Riemannian submanifold N immersed in the
              3-dimensional Riemannian manifold M

            sage: phi = N.diff_map(M)
            sage: N.set_embedding(phi)
            sage: N
            2-dimensional Riemannian submanifold N embedded in the
             3-dimensional Riemannian manifold M
            sage: S = N.subset('S'); S
            Subset S of the
             2-dimensional Riemannian submanifold N embedded in the
              3-dimensional Riemannian manifold M
            sage: O = N.subset('O', is_open=True); O  # indirect doctest
            Open subset O of the
             2-dimensional Riemannian submanifold N embedded in the
              3-dimensional Riemannian manifold M
        """
    def ambient_metric(self):
        """
        Return the metric of the ambient manifold.

        OUTPUT: the metric of the ambient manifold

        EXAMPLES::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: N.ambient_metric()
            Riemannian metric g on the Euclidean space E^3
            sage: N.ambient_metric().display()
            g = dx⊗dx + dy⊗dy + dz⊗dz
            sage: N.ambient_metric() is M.metric()
            True
        """
    def first_fundamental_form(self):
        """
        Return the first fundamental form of the submanifold.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - the first fundamental form, as an instance of
          :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`

        EXAMPLES:

        A sphere embedded in Euclidean space::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real')
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: N.set_embedding(phi)
            sage: N.first_fundamental_form()  # long time
            Riemannian metric gamma on the 2-dimensional Riemannian
             submanifold N embedded in the Euclidean space E^3
            sage: N.first_fundamental_form()[:]  # long time
            [          r^2             0]
            [            0 r^2*sin(th)^2]

        An alias is ``induced_metric``::

            sage: N.induced_metric()[:]  # long time
            [          r^2             0]
            [            0 r^2*sin(th)^2]

        By default, the first fundamental form is named ``gamma``, but this
        can be customized by means of the argument ``metric_name`` when
        declaring the submanifold::

            sage: P = Manifold(1, 'P', ambient=M, structure='Riemannian',
            ....:              metric_name='g')
            sage: CP.<t> = P.chart()
            sage: F = P.diff_map(M, [t, 2*t, 3*t])
            sage: P.set_embedding(F)
            sage: P.induced_metric()
            Riemannian metric g on the 1-dimensional Riemannian submanifold P
             embedded in the Euclidean space E^3
            sage: P.induced_metric().display()
            g = 14 dt⊗dt
        """
    induced_metric = first_fundamental_form
    def metric(self, name=None, signature=None, latex_name=None, dest_map=None):
        """
        Return the induced metric (first fundamental form) or define a new
        metric tensor on the submanifold.

        A new (uninitialized) metric is returned only if the argument ``name``
        is provided and differs from the metric name declared at the
        construction of the submanifold; otherwise, the first fundamental
        form is returned.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the metric; if ``name``
          is ``None`` or equals the metric name declared when constructing
          the submanifold, the first fundamental form is returned (see
          :meth:`first_fundamental_form`)
        - ``signature`` -- (default: ``None``; ignored if ``name`` is ``None``)
          signature `S` of the metric as a single integer: `S = n_+ - n_-`,
          where `n_+` (resp. `n_-`) is the number of positive terms (resp.
          number of negative terms) in any diagonal writing of the metric
          components; if ``signature`` is not provided, `S` is set to the
          submanifold's dimension (Riemannian signature)
        - ``latex_name`` -- (default: ``None``; ignored if ``name`` is ``None``)
          LaTeX symbol to denote the metric; if ``None``, it is formed from
          ``name``
        - ``dest_map`` -- (default: ``None``; ignored if ``name`` is ``None``)
          instance of
          class :class:`~sage.manifolds.differentiable.diff_map.DiffMap`
          representing the destination map `\\Phi:\\ U \\rightarrow M`, where `U`
          is the current submanifold; if ``None``, the identity map is assumed
          (case of a metric tensor field *on* `U`)

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`

        EXAMPLES:

        Induced metric on a straight line of the Euclidean plane::

            sage: M.<x,y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: CN.<t> = N.chart()
            sage: F = N.diff_map(M, [t, 2*t])
            sage: N.set_embedding(F)
            sage: N.metric()
            Riemannian metric gamma on the 1-dimensional Riemannian
             submanifold N embedded in the Euclidean plane E^2
            sage: N.metric().display()
            gamma = 5 dt⊗dt

        Setting the argument ``name`` to that declared while constructing
        the submanifold (default: ``'gamma'``) yields the same result::

            sage: N.metric(name='gamma') is N.metric()
            True

        while using a different name allows one to define a new metric on the
        submanifold::

            sage: h = N.metric(name='h'); h
            Riemannian metric h on the 1-dimensional Riemannian submanifold N
             embedded in the Euclidean plane E^2
            sage: h[0, 0] = 1  # initialization
            sage: h.display()
            h = dt⊗dt
        """
    @cached_method
    def difft(self):
        """
        Return the differential of the scalar field on the ambient manifold
        representing the first parameter of the foliation associated to
        ``self``.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT: 1-form field on the ambient manifold

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real')
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: N.difft()
            1-form dr on the Euclidean space E^3
            sage: N.difft().display()
            dr = x/sqrt(x^2 + y^2 + z^2) dx + y/sqrt(x^2 + y^2 + z^2) dy +
             z/sqrt(x^2 + y^2 + z^2) dz
        """
    @cached_method
    def gradt(self):
        """
        Return the gradient of the scalar field on the ambient manifold
        representing the first parameter of the foliation associated to
        ``self``.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT: vector field on the ambient manifold

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real')
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: N.gradt()
            Vector field grad(r) on the Euclidean space E^3
            sage: N.gradt().display()
            grad(r) = x/sqrt(x^2 + y^2 + z^2) e_x + y/sqrt(x^2 + y^2 + z^2) e_y
             + z/sqrt(x^2 + y^2 + z^2) e_z
        """
    @cached_method
    def normal(self):
        '''
        Return a normal unit vector to the submanifold.

        If a foliation is defined, it is used to compute the gradient of the
        foliation parameter and then the normal vector. If not, the normal
        vector is computed using the following formula:

        .. MATH::

            n = \\vec{*}(\\mathrm{d}x_0\\wedge\\mathrm{d}x_1\\wedge\\cdots
            \\wedge\\mathrm{d}x_{n-1})

        where the star stands for the Hodge dual operator and the wedge for the
        exterior product.

        This formula does not always define a proper vector field when
        multiple charts overlap, because of the arbitrariness of the direction
        of the normal vector. To avoid this problem, the method ``normal()``
        considers the graph defined by the atlas of the submanifold and the
        changes of coordinates, and only calculate the normal vector once by
        connected component. The expression is then propagate by restriction,
        continuation, or change of coordinates using a breadth-first
        exploration of the graph.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - vector field on the ambient manifold (case of a foliation) or along
          the submanifold with values in the ambient manifold (case of a
          single submanifold)

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, \'N\', ambient=M, structure=\'Riemannian\')
            sage: C.<th,ph> = N.chart(r\'th:(0,pi):\\theta ph:(-pi,pi):\\phi\')
            sage: r = var(\'r\', domain=\'real\') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()
            sage: N.normal()  # long time
            Vector field n on the Euclidean space E^3
            sage: N.normal().display()  # long time
            n = x/sqrt(x^2 + y^2 + z^2) e_x + y/sqrt(x^2 + y^2 + z^2) e_y
             + z/sqrt(x^2 + y^2 + z^2) e_z

        Or in spherical coordinates::

            sage: N.normal().display(T[0].frame(),T[0])  # long time
            n = ∂/∂r_E3

        Let us now consider a sphere of constant radius, i.e. not assumed to be
        part of a foliation, in stereographic coordinates::

            sage: M.<X,Y,Z> = EuclideanSpace()
            sage: N = Manifold(2, \'N\', ambient=M, structure=\'Riemannian\')
            sage: U = N.open_subset(\'U\')
            sage: V = N.open_subset(\'V\')
            sage: N.declare_union(U, V)
            sage: stereoN.<x,y> = U.chart()
            sage: stereoS.<xp,yp> = V.chart("xp:x\' yp:y\'")
            sage: stereoN_to_S = stereoN.transition_map(stereoS,
            ....:                                 (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                                 intersection_name=\'W\',
            ....:                                 restrictions1= x^2+y^2!=0,
            ....:                                 restrictions2= xp^2+yp^2!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: W = U.intersection(V)
            sage: stereoN_W = stereoN.restrict(W)
            sage: stereoS_W = stereoS.restrict(W)
            sage: A = W.open_subset(\'A\', coord_def={stereoN_W: (y!=0, x<0),
            ....:                                   stereoS_W: (yp!=0, xp<0)})
            sage: spher.<the,phi> = A.chart(r\'the:(0,pi):\\theta phi:(0,2*pi):\\phi\')
            sage: stereoN_A = stereoN_W.restrict(A)
            sage: spher_to_stereoN = spher.transition_map(stereoN_A,
            ....:                              (sin(the)*cos(phi)/(1-cos(the)),
            ....:                               sin(the)*sin(phi)/(1-cos(the))))
            sage: spher_to_stereoN.set_inverse(2*atan(1/sqrt(x^2+y^2)),
            ....:                              atan2(-y,-x)+pi)
            Check of the inverse coordinate transformation:
              the == 2*arctan(sqrt(-cos(the) + 1)/sqrt(cos(the) + 1))  **failed**
              phi == pi + arctan2(sin(phi)*sin(the)/(cos(the) - 1),
                                  cos(phi)*sin(the)/(cos(the) - 1))  **failed**
              x == x  *passed*
              y == y  *passed*
            NB: a failed report can reflect a mere lack of simplification.
            sage: stereoN_to_S_A = stereoN_to_S.restrict(A)
            sage: spher_to_stereoS = stereoN_to_S_A * spher_to_stereoN
            sage: stereoS_to_N_A = stereoN_to_S.inverse().restrict(A)
            sage: stereoS_to_spher = spher_to_stereoN.inverse() * stereoS_to_N_A
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(stereoN, E): [2*x/(1+x^2+y^2),
            ....:                                    2*y/(1+x^2+y^2),
            ....:                                    (x^2+y^2-1)/(1+x^2+y^2)],
            ....:                   (stereoS, E): [2*xp/(1+xp^2+yp^2),
            ....:                                  2*yp/(1+xp^2+yp^2),
            ....:                                 (1-xp^2-yp^2)/(1+xp^2+yp^2)]},
            ....:                  name=\'Phi\', latex_name=r\'\\Phi\')
            sage: N.set_embedding(phi)

        The method ``normal()`` now returns a tensor field along ``N``::

            sage: n = N.normal()  # long time
            sage: n  # long time
            Vector field n along the 2-dimensional Riemannian submanifold N
             embedded in the Euclidean space E^3 with values on the Euclidean
             space E^3

        Let us check that the choice of orientation is coherent on the two top
        frames::

            sage: n.restrict(V).display(format_spec=spher)  # long time
            n = -cos(phi)*sin(the) e_X - sin(phi)*sin(the) e_Y - cos(the) e_Z
            sage: n.restrict(U).display(format_spec=spher)  # long time
            n = -cos(phi)*sin(the) e_X - sin(phi)*sin(the) e_Y - cos(the) e_Z
        '''
    def ambient_first_fundamental_form(self):
        """
        Return the first fundamental form of the submanifold as a tensor of the
        ambient manifold.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - (0,2) tensor field on the ambient manifold describing the induced
          metric before projection on the submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.ambient_first_fundamental_form()
            Tensor field gamma of type (0,2) along the 1-dimensional Riemannian
             submanifold N embedded in the Euclidean plane E^2 with values on
             the Euclidean plane E^2
            sage: N.ambient_first_fundamental_form()[:]
            [ x^2/(x^2 + 4) -2*x/(x^2 + 4)]
            [-2*x/(x^2 + 4)    4/(x^2 + 4)]

        An alias is ``ambient_induced_metric``::

            sage: N.ambient_induced_metric()[:]
            [ x^2/(x^2 + 4) -2*x/(x^2 + 4)]
            [-2*x/(x^2 + 4)    4/(x^2 + 4)]
        """
    ambient_induced_metric = ambient_first_fundamental_form
    @cached_method
    def lapse(self):
        """
        Return the lapse function of the foliation.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT: the lapse function, as a scalar field on the ambient manifold

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()
            sage: N.lapse()
            Scalar field N on the Euclidean space E^3
            sage: N.lapse().display()
            N: E^3 → ℝ
               (x, y, z) ↦ 1
               (th_E3, ph_E3, r_E3) ↦ 1
        """
    @cached_method
    def shift(self):
        """
        Return the shift vector associated with the first adapted chart of the
        foliation.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT: shift vector field on the ambient manifold

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()
            sage: N.shift()  # long time
            Vector field beta on the Euclidean space E^3
            sage: N.shift().display()  # long time
            beta = 0
        """
    def ambient_second_fundamental_form(self):
        """
        Return the second fundamental form of the submanifold as a tensor field
        on the ambient manifold.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - (0,2) tensor field on the ambient manifold equal to the second
          fundamental form once orthogonally projected onto the submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.ambient_second_fundamental_form()  # long time
            Field of symmetric bilinear forms K along the 1-dimensional
             Riemannian submanifold N embedded in the Euclidean plane E^2 with
             values on the Euclidean plane E^2
            sage: N.ambient_second_fundamental_form()[:] # long time
            [-x^2/(x^2 + 4)  2*x/(x^2 + 4)]
            [ 2*x/(x^2 + 4)   -4/(x^2 + 4)]

        An alias is ``ambient_extrinsic_curvature``::

            sage: N.ambient_extrinsic_curvature()[:]  # long time
            [-x^2/(x^2 + 4)  2*x/(x^2 + 4)]
            [ 2*x/(x^2 + 4)   -4/(x^2 + 4)]
        """
    ambient_extrinsic_curvature = ambient_second_fundamental_form
    def second_fundamental_form(self):
        """
        Return the second fundamental form of the submanifold.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - the second fundamental form, as a symmetric tensor field of type
          (0,2) on the submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.second_fundamental_form()  # long time
            Field of symmetric bilinear forms K on the 1-dimensional Riemannian
             submanifold N embedded in the Euclidean plane E^2
            sage: N.second_fundamental_form().display()  # long time
            K = -4/(x^4 + 8*x^2 + 16) dx⊗dx

        An alias is ``extrinsic_curvature``::

            sage: N.extrinsic_curvature().display()  # long time
            K = -4/(x^4 + 8*x^2 + 16) dx⊗dx

        An example with a non-Euclidean ambient metric::

            sage: M = Manifold(2, 'M', structure='Riemannian')
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian',
            ....:              start_index=1)
            sage: CM.<x,y> = M.chart()
            sage: CN.<u> = N.chart()
            sage: g = M.metric()
            sage: g[0, 0], g[1, 1] = 1, 1/(1 + y^2)^2
            sage: phi = N.diff_map(M, (u, u))
            sage: N.set_embedding(phi)
            sage: N.second_fundamental_form()
            Field of symmetric bilinear forms K on the 1-dimensional Riemannian
             submanifold N embedded in the 2-dimensional Riemannian manifold M
            sage: N.second_fundamental_form().display()
            K = 2*sqrt(u^4 + 2*u^2 + 2)*u/(u^6 + 3*u^4 + 4*u^2 + 2) du⊗du
        """
    extrinsic_curvature = second_fundamental_form
    @cached_method
    def projector(self):
        """
        Return the orthogonal projector onto the submanifold.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - the orthogonal projector onto the submanifold, as tensor field of
          type (1,1) on the ambient manifold

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()

        The orthogonal projector onto ``N`` is a type-(1,1) tensor field on
        ``M``::

            sage: N.projector()  # long time
            Tensor field gamma of type (1,1) on the Euclidean space E^3

        Check that the orthogonal projector applied to the normal vector is
        zero::

            sage: N.projector().contract(N.normal()).display()  # long time
            0
        """
    def project(self, tensor):
        """
        Return the orthogonal projection of a tensor field onto the submanifold.

        INPUT:

        - ``tensor`` -- any tensor field to be projected onto the submanifold.
          If no foliation is provided, must be a tensor field along the
          submanifold.

        OUTPUT:

        - orthogonal projection of ``tensor`` onto the submanifold, as a
          tensor field of the *ambient* manifold

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()

        Let us perform the projection of the ambient metric and check that it
        is equal to the first fundamental form::

            sage: pg = N.project(M.metric()); pg  # long time
            Tensor field of type (0,2) on the Euclidean space E^3
            sage: pg == N.ambient_first_fundamental_form()  # long time
            True

        Note that the output of ``project()`` is not cached.
        """
    def mixed_projection(self, tensor, indices: int = 0):
        """
        Return de n+1 decomposition of a tensor on the submanifold and the
        normal vector.

        The n+1 decomposition of a tensor of rank `k` can be obtained by
        contracting each index either with the normal vector or the projection
        operator of the submanifold (see
        :meth:`~sage.manifolds.differentiable.pseudo_riemannian_submanifold.PseudoRiemannianSubmanifold.projector`).

        INPUT:

        - ``tensor`` -- any tensor field, eventually along the submanifold if
          no foliation is provided
        - ``indices`` -- (default: ``0``) list of integers containing the
          indices on which the projection is made on the normal vector.
          By default, all projections are made on the submanifold. If
          an integer `n` is provided, the `n` first contractions are made with
          the normal vector, all the other ones with the orthogonal projection
          operator.

        OUTPUT: tensor field of rank `k`-``len(indices)``

        EXAMPLES:

        Foliation of the Euclidean 3-space by 2-spheres parametrized by their
        radii::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()

        If ``indices`` is not specified, the mixed projection of the ambient
        metric coincides with the first fundamental form::

            sage: g = M.metric()
            sage: gpp = N.mixed_projection(g); gpp  # long time
            Tensor field of type (0,2) on the Euclidean space E^3
            sage: gpp == N.ambient_first_fundamental_form()  # long time
            True

        The other non-redundant projections are::

            sage: gnp = N.mixed_projection(g, [0]); gnp  # long time
            1-form on the Euclidean space E^3

        and::

            sage: gnn = N.mixed_projection(g, [0,1]); gnn
            Scalar field on the Euclidean space E^3

        which is constant and equal to 1 (the norm of the unit normal vector)::

            sage: gnn.display()
            E^3 → ℝ
            (x, y, z) ↦ 1
            (th_E3, ph_E3, r_E3) ↦ 1
        """
    @cached_method
    def gauss_curvature(self):
        """
        Return the Gauss curvature of the submanifold.

        The *Gauss curvature* is the product or the principal curvatures, or
        equivalently the determinant of the projection operator.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT: the Gauss curvature as a scalar field on the submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.gauss_curvature()  # long time
            Scalar field on the 1-dimensional Riemannian submanifold N embedded
             in the Euclidean plane E^2
            sage: N.gauss_curvature().display()  # long time
            N → ℝ
            on U: x ↦ -1
            on V: y ↦ -1
        """
    @cached_method
    def principal_directions(self, chart):
        """
        Return the principal directions of the submanifold.

        The *principal directions* are the eigenvectors of the projection
        operator. The result is formatted as a list of pairs
        (eigenvector, eigenvalue).

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        INPUT:

        - ``chart`` -- chart in which the principal directions are to be
          computed

        OUTPUT:

        - list of pairs (vector field, scalar field) representing the
          principal directions and the associated principal curvatures

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.principal_directions(stereoN)  # long time
            [(Vector field e_0 on the 1-dimensional Riemannian submanifold N
              embedded in the Euclidean plane E^2, -1)]
            sage: N.principal_directions(stereoN)[0][0].display()  # long time
            e_0 = ∂/∂x
        """
    @cached_method
    def principal_curvatures(self, chart):
        """
        Return the principal curvatures of the submanifold.

        The *principal curvatures* are the eigenvalues of the projection
        operator. The resulting scalar fields are named ``k_i`` with the
        index ``i`` ranging from 0 to the submanifold dimension minus one.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        INPUT:

        - ``chart`` -- chart in which the principal curvatures are to be
          computed

        OUTPUT:

        - the principal curvatures, as a list of scalar fields on the
          submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.principal_curvatures(stereoN)  # long time
            [Scalar field k_0 on the 1-dimensional Riemannian submanifold N
             embedded in the Euclidean plane E^2]
            sage: N.principal_curvatures(stereoN)[0].display()  # long time
            k_0: N → ℝ
            on U: x ↦ -1
            on W: y ↦ -1
        """
    @cached_method
    def mean_curvature(self):
        """
        Return the mean curvature of the submanifold.

        The *mean curvature* is the arithmetic mean of the principal curvatures,
        or equivalently the trace of the projection operator.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT: the mean curvature, as a scalar field on the submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.mean_curvature()  # long time
            Scalar field on the 1-dimensional Riemannian submanifold N
             embedded in the Euclidean plane E^2
            sage: N.mean_curvature().display()  # long time
            N → ℝ
            on U: x ↦ -1
            on V: y ↦ -1
        """
    @cached_method
    def shape_operator(self):
        """
        Return the shape operator of the submanifold.

        The shape operator is equal to the second fundamental form with one of
        the indices upped.

        The result is cached, so calling this method multiple times always
        returns the same result at no additional cost.

        OUTPUT:

        - the shape operator, as a tensor field of type (1,1) on the
          submanifold

        EXAMPLES:

        A unit circle embedded in the Euclidean plane::

            sage: M.<X,Y> = EuclideanSpace()
            sage: N = Manifold(1, 'N', ambient=M, structure='Riemannian')
            sage: U = N.open_subset('U')
            sage: V = N.open_subset('V')
            sage: N.declare_union(U,V)
            sage: stereoN.<x> = U.chart()
            sage: stereoS.<y> = V.chart()
            sage: stereoN_to_S = stereoN.transition_map(stereoS, (4/x),
            ....:                   intersection_name='W',
            ....:                   restrictions1=x!=0, restrictions2=y!=0)
            sage: stereoS_to_N = stereoN_to_S.inverse()
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M,
            ....:         {(stereoN, E): [1/sqrt(1+x^2/4), x/2/sqrt(1+x^2/4)],
            ....:          (stereoS, E): [1/sqrt(1+4/y^2), 2/y/sqrt(1+4/y^2)]})
            sage: N.set_embedding(phi)
            sage: N.shape_operator()  # long time
            Tensor field of type (1,1) on the 1-dimensional Riemannian
             submanifold N embedded in the Euclidean plane E^2
            sage: N.shape_operator().display()  # long time
            -∂/∂x⊗dx
        """
    def clear_cache(self) -> None:
        """
        Reset all the cached functions and the derived quantities.

        Use this function if you modified the immersion (or embedding) of the
        submanifold. Note that when calling a calculus function after clearing,
        new Python objects will be created.

        EXAMPLES::

            sage: M.<x,y,z> = EuclideanSpace()
            sage: N = Manifold(2, 'N', ambient=M, structure='Riemannian')
            sage: C.<th,ph> = N.chart(r'th:(0,pi):\\theta ph:(-pi,pi):\\phi')
            sage: r = var('r', domain='real') # foliation parameter
            sage: assume(r>0)
            sage: E = M.cartesian_coordinates()
            sage: phi = N.diff_map(M, {(C,E): [r*sin(th)*cos(ph),
            ....:                              r*sin(th)*sin(ph),
            ....:                              r*cos(th)]})
            sage: phi_inv = M.diff_map(N, {(E,C): [arccos(z/r), atan2(y,x)]})
            sage: phi_inv_r = M.scalar_field({E: sqrt(x^2+y^2+z^2)})
            sage: N.set_embedding(phi, inverse=phi_inv, var=r,
            ....:                 t_inverse={r: phi_inv_r})
            sage: T = N.adapted_chart()
            sage: n = N.normal()
            sage: n is N.normal()
            True
            sage: N.clear_cache()
            sage: n is N.normal()
            False
            sage: n == N.normal()
            True
        """
