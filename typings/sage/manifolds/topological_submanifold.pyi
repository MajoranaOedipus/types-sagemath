from sage.manifolds.continuous_map import ContinuousMap as ContinuousMap
from sage.manifolds.manifold import TopologicalManifold as TopologicalManifold
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.symbolic.assumptions import assume as assume, assumptions as assumptions
from sage.symbolic.expression import Expression as Expression

class TopologicalSubmanifold(TopologicalManifold):
    '''
    Submanifold of a topological manifold.

    Given a topological manifold `M` over a topological field `K`, a
    *topological submanifold of* `M` is defined by a topological manifold `N`
    over the same field `K` of dimension lower than the dimension of `M` and
    a topological embedding `\\phi` from `N` to `M` (i.e. `\\phi` is an
    homeomorphism onto its image).

    In the case where `\\phi` is only a topological immersion (i.e. is only
    locally an embedding), one says that `N` is an *immersed submanifold*.

    The map `\\phi` can also depend on one or multiple parameters.
    As long as `\\phi` remains injective in these parameters, it represents
    a *foliation*. The *dimension* of the foliation is defined as the number of
    parameters.

    INPUT:

    - ``n`` -- positive integer; dimension of the submanifold
    - ``name`` -- string; name (symbol) given to the submanifold
    - ``field`` -- field `K` on which the submanifold is defined; allowed
      values are

      - ``\'real\'`` or an object of type ``RealField`` (e.g., ``RR``) for
        a manifold over `\\RR`
      - ``\'complex\'`` or an object of type ``ComplexField`` (e.g., ``CC``)
        for a manifold over `\\CC`
      - an object in the category of topological fields (see
        :class:`~sage.categories.fields.Fields` and
        :class:`~sage.categories.topological_spaces.TopologicalSpaces`)
        for other types of manifolds

    - ``structure`` -- manifold structure (see
      :class:`~sage.manifolds.structure.TopologicalStructure` or
      :class:`~sage.manifolds.structure.RealTopologicalStructure`)
    - ``ambient`` -- (default: ``None``) codomain `M` of the immersion `\\phi`;
      must be a topological manifold. If ``None``, it is set to ``self``
    - ``base_manifold`` -- (default: ``None``) if not ``None``, must be a
      topological manifold; the created object is then an open subset of
      ``base_manifold``
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the submanifold; if none are provided, it is set to ``name``
    - ``start_index`` -- (default: 0) integer; lower value of the range of
      indices used for "indexed objects" on the submanifold, e.g., coordinates
      in a chart
    - ``category`` -- (default: ``None``) to specify the category; if
      ``None``, ``Manifolds(field)`` is assumed (see the category
      :class:`~sage.categories.manifolds.Manifolds`)
    - ``unique_tag`` -- (default: ``None``) tag used to force the construction
      of a new object when all the other arguments have been used previously
      (without ``unique_tag``, the
      :class:`~sage.structure.unique_representation.UniqueRepresentation`
      behavior inherited from
      :class:`~sage.manifolds.subset.ManifoldSubset` via
      :class:`~sage.manifolds.manifold.TopologicalManifold`
      would return the previously constructed object corresponding to these
      arguments)

    EXAMPLES:

    Let `N` be a 2-dimensional submanifold of a 3-dimensional manifold `M`::

        sage: M = Manifold(3, \'M\', structure=\'topological\')
        sage: N = Manifold(2, \'N\', ambient=M, structure=\'topological\')
        sage: N
        2-dimensional topological submanifold N immersed in the 3-dimensional
         topological manifold M
        sage: CM.<x,y,z> = M.chart()
        sage: CN.<u,v> = N.chart()

    Let us define a 1-dimensional foliation indexed by `t`::

        sage: t = var(\'t\')
        sage: phi = N.continuous_map(M, {(CN,CM): [u, v, t+u^2+v^2]})
        sage: phi.display()
        N → M
           (u, v) ↦ (x, y, z) = (u, v, u^2 + v^2 + t)

    The foliation inverse maps are needed for computing the adapted chart on
    the ambient manifold::

        sage: phi_inv = M.continuous_map(N, {(CM, CN): [x, y]})
        sage: phi_inv.display()
        M → N
           (x, y, z) ↦ (u, v) = (x, y)
        sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
        sage: phi_inv_t.display()
        M → ℝ
        (x, y, z) ↦ -x^2 - y^2 + z

    `\\phi` can then be declared as an embedding `N\\to M`::

        sage: N.set_embedding(phi, inverse=phi_inv, var=t,
        ....:                 t_inverse={t: phi_inv_t})

    The foliation can also be used to find new charts on the ambient manifold
    that are adapted to the foliation, i.e. in which the expression of the
    immersion is trivial. At the same time, the appropriate coordinate changes
    are computed::

        sage: N.adapted_chart()
        [Chart (M, (u_M, v_M, t_M))]
        sage: M.atlas()
        [Chart (M, (x, y, z)), Chart (M, (u_M, v_M, t_M))]
        sage: len(M.coord_changes())
        2

    The foliation parameters are always added as the last coordinates.

    .. SEEALSO::

        :mod:`~sage.manifolds.manifold`
    '''
    def __init__(self, n, name, field, structure, ambient=None, base_manifold=None, latex_name=None, start_index: int = 0, category=None, unique_tag=None) -> None:
        """
        Construct a submanifold of a topological manifold.

        TESTS::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: N
            2-dimensional topological submanifold N immersed in the
             3-dimensional topological manifold M
        """
    def open_subset(self, name, latex_name=None, coord_def={}, supersets=None):
        """
        Create an open subset of the manifold.

        An open subset is a set that is (i) included in the manifold and (ii)
        open with respect to the manifold's topology. It is a topological
        manifold by itself.

        As ``self`` is a submanifold of its ambient manifold,
        the new open subset is also considered a submanifold of that.
        Hence the returned object is an instance of
        :class:`TopologicalSubmanifold`.

        INPUT:

        - ``name`` -- name given to the open subset
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote
          the subset; if none are provided, it is set to ``name``
        - ``coord_def`` -- (default: {}) definition of the subset in
          terms of coordinates; ``coord_def`` must a be dictionary with keys
          charts on the manifold and values the symbolic expressions formed
          by the coordinates to define the subset
        - ``supersets`` -- (default: only ``self``) list of sets that the
          new open subset is a subset of

        OUTPUT: the open subset, as an instance of :class:`TopologicalSubmanifold`

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological'); N
            2-dimensional topological submanifold N immersed in the
             3-dimensional topological manifold M
            sage: S = N.subset('S'); S
            Subset S of the
             2-dimensional topological submanifold N immersed in the
              3-dimensional topological manifold M
            sage: O = N.subset('O', is_open=True); O  # indirect doctest
            Open subset O of the
             2-dimensional topological submanifold N immersed in the
              3-dimensional topological manifold M

            sage: phi = N.continuous_map(M)
            sage: N.set_embedding(phi)
            sage: N
            2-dimensional topological submanifold N embedded in the
             3-dimensional topological manifold M
            sage: S = N.subset('S'); S
            Subset S of the
             2-dimensional topological submanifold N embedded in the
              3-dimensional topological manifold M
            sage: O = N.subset('O', is_open=True); O  # indirect doctest
            Open subset O of the
             2-dimensional topological submanifold N embedded in the
              3-dimensional topological manifold M
        """
    def set_immersion(self, phi, inverse=None, var=None, t_inverse=None) -> None:
        """
        Register the immersion of the immersed submanifold.

        A *topological immersion* is a continuous map that is locally a
        topological embedding (i.e. a homeomorphism onto its image).
        A *differentiable immersion* is a differentiable map whose differential
        is injective at each point.

        If an inverse of the immersion onto its image exists, it can be
        registered at the same time. If the immersion depends on parameters,
        they must also be declared here.

        INPUT:

        - ``phi`` -- continuous map `\\phi` from ``self`` to ``self.ambient()``
        - ``inverse`` -- (default: ``None``) continuous map from
          ``self.ambient()`` to ``self``, which once restricted to the image
          of `\\phi` is the inverse of `\\phi` onto its image if the latter
          exists (NB: no check of this is performed)
        - ``var`` -- (default: ``None``) list of parameters involved in the
          definition of `\\phi` (case of foliation); if `\\phi` depends on a
          single parameter ``t``, one can write ``var=t`` as a shortcut for
          ``var=[t]``
        - ``t_inverse`` -- (default: ``None``) dictionary of scalar fields on
          ``self.ambient()`` providing the values of the parameters involved
          in the definition of `\\phi` (case of foliation), the keys being
          the parameters

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: N
            2-dimensional topological submanifold N immersed in the
             3-dimensional topological manifold M
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var('t')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi.display()
            N → M
               (u, v) ↦ (x, y, z) = (u, v, u^2 + v^2 + t)
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv.display()
            M → N
                (x, y, z) ↦ (u, v) = (x, y)
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: phi_inv_t.display()
            M → ℝ
            (x, y, z) ↦ -x^2 - y^2 + z
            sage: N.set_immersion(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse={t: phi_inv_t})
        """
    def declare_embedding(self) -> None:
        """
        Declare that the immersion provided by :meth:`set_immersion` is in
        fact an embedding.

        A *topological embedding* is a continuous map that is a homeomorphism
        onto its image. A *differentiable embedding* is a topological embedding
        that is also a differentiable immersion.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: N
            2-dimensional topological submanifold N immersed in the
             3-dimensional topological manifold M
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var('t')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: N.set_immersion(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse={t: phi_inv_t})
            sage: N._immersed
            True
            sage: N._embedded
            False
            sage: N.declare_embedding()
            sage: N._immersed
            True
            sage: N._embedded
            True
        """
    def set_embedding(self, phi: ContinuousMap, inverse=None, var=None, t_inverse=None):
        """
        Register the embedding of an embedded submanifold.

        A *topological embedding* is a continuous map that is a homeomorphism
        onto its image. A *differentiable embedding* is a topological embedding
        that is also a differentiable immersion.

        INPUT:

        - ``phi`` -- continuous map `\\phi` from ``self`` to ``self.ambient()``
        - ``inverse`` -- (default: ``None``) continuous map from
          ``self.ambient()`` to ``self``, which once restricted to the image
          of `\\phi` is the inverse of `\\phi` onto its image (NB: no check of
          this is performed)
        - ``var`` -- (default: ``None``) list of parameters involved in the
          definition of `\\phi` (case of foliation); if `\\phi` depends on a
          single parameter ``t``, one can write ``var=t`` as a shortcut for
          ``var=[t]``
        - ``t_inverse`` -- (default: ``None``) dictionary of scalar fields on
          ``self.ambient()`` providing the values of the parameters involved
          in the definition of `\\phi` (case of foliation), the keys being
          the parameters

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: N
            2-dimensional topological submanifold N immersed in the
             3-dimensional topological manifold M
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var('t')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi.display()
            N → M
               (u, v) ↦ (x, y, z) = (u, v, u^2 + v^2 + t)
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv.display()
            M → N
                (x, y, z) ↦ (u, v) = (x, y)
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: phi_inv_t.display()
            M → ℝ
            (x, y, z) ↦ -x^2 - y^2 + z
            sage: N.set_embedding(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse={t: phi_inv_t})

        Now ``N`` appears as an embedded submanifold::

            sage: N
            2-dimensional topological submanifold N embedded in the
             3-dimensional topological manifold M
        """
    def adapted_chart(self, postscript=None, latex_postscript=None):
        '''
        Create charts and changes of charts in the ambient manifold adapted
        to the foliation.

        A manifold `M` of dimension `m` can be foliated by submanifolds `N` of
        dimension `n`. The corresponding embedding needs `m-n` free parameters
        to describe the whole manifold.

        A chart adapted to the foliation is a set of coordinates
        `(x_1,\\ldots,x_n,t_1,\\ldots,t_{m-n})` on `M` such that
        `(x_1,\\ldots,x_n)` are coordinates on `N` and `(t_1,\\ldots,t_{m-n})`
        are the `m-n` free parameters of the foliation.

        Provided that an embedding with free variables is already defined, this
        function constructs such charts and coordinates changes whenever
        it is possible.

        If there are restrictions of the coordinates on the starting chart,
        these restrictions are also propagated.

        INPUT:

        - ``postscript`` -- (default: ``None``) string defining the name of the
          coordinates of the adapted chart. This string will be appended to
          the names of the coordinates `(x_1,\\ldots,x_n)` and of the parameters
          `(t_1,\\ldots,t_{m-n})`. If ``None``, ``"_" + self.ambient()._name``
          is used
        - ``latex_postscript`` -- (default: ``None``) string defining the LaTeX
          name of the coordinates of the adapted chart. This string will be
          appended to the LaTeX names of the coordinates `(x_1,\\ldots,x_n)` and
          of the parameters `(t_1,\\ldots,t_{m-n})`, If ``None``,
          ``"_" + self.ambient()._latex_()`` is used

        OUTPUT: list of adapted charts on `M` created from the charts of ``self``

        EXAMPLES::

            sage: M = Manifold(3, \'M\', structure=\'topological\',
            ....:              latex_name=r"\\mathcal{M}")
            sage: N = Manifold(2, \'N\', ambient=M, structure=\'topological\')
            sage: N
            2-dimensional topological submanifold N immersed in the
             3-dimensional topological manifold M
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var(\'t\')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: N.set_embedding(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse={t:phi_inv_t})
            sage: N.adapted_chart()
            [Chart (M, (u_M, v_M, t_M))]
            sage: latex(_)
            \\left[\\left(\\mathcal{M},({{u}_{\\mathcal{M}}}, {{v}_{\\mathcal{M}}},
             {{t}_{\\mathcal{M}}})\\right)\\right]

        The adapted chart has been added to the atlas of ``M``::

            sage: M.atlas()
            [Chart (M, (x, y, z)), Chart (M, (u_M, v_M, t_M))]
            sage: N.atlas()
            [Chart (N, (u, v))]

        The names of the adapted coordinates can be customized::

            sage: N.adapted_chart(postscript=\'1\', latex_postscript=\'_1\')
            [Chart (M, (u1, v1, t1))]
            sage: latex(_)
            \\left[\\left(\\mathcal{M},({{u}_1}, {{v}_1}, {{t}_1})\\right)\\right]
        '''
    def plot(self, param, u, v, chart1=None, chart2=None, **kwargs):
        """
        Plot an embedding.

        Plot the embedding defined by the foliation and a set of values for the
        free parameters. This function can only plot 2-dimensional surfaces
        embedded in 3-dimensional manifolds. It ultimately calls
        :class:`~sage.plot.plot3d.parametric_surface.ParametricSurface`.

        INPUT:

        - ``param`` -- dictionary of values indexed by the free variables
          appearing in the foliation
        - ``u`` -- iterable of the values taken by the first coordinate of the
          surface to plot
        - ``v`` -- iterable of the values taken by the second coordinate of the
          surface to plot
        - ``chart1`` -- (default: ``None``) chart in which ``u`` and ``v`` are
          considered. By default, the default chart of the submanifold is used
        - ``chart2`` -- (default: ``None``) chart in the codomain of the
          embedding. By default, the default chart of the codomain is used
        - ``**kwargs`` -- other arguments as used in
          :class:`~sage.plot.plot3d.parametric_surface.ParametricSurface`

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient = M, structure='topological')
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var('t')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: N.set_embedding(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse = {t:phi_inv_t})
            sage: N.adapted_chart()
            [Chart (M, (u_M, v_M, t_M))]
            sage: P0 = N.plot({t:0}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
            ....:             CN, CM, opacity=0.3, mesh=True)
            sage: P1 = N.plot({t:1}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
            ....:             CN, CM, opacity=0.3, mesh=True)
            sage: P2 = N.plot({t:2}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
            ....:             CN, CM, opacity=0.3, mesh=True)
            sage: P3 = N.plot({t:3}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
            ....:             CN, CM, opacity=0.3, mesh=True)
            sage: P0 + P1 + P2 + P3
            Graphics3d Object

        .. PLOT::

            M = Manifold(3, 'M', structure='topological')
            N = Manifold(2, 'N', ambient = M, structure='topological')
            CM = M.chart('x y z'); x, y, z = CM[:]
            CN = N.chart('u v'); u, v = CN[:]
            t = var('t')
            phi = N.continuous_map(M, {(CN,CM): [u,v,t+u**2+v**2]})
            phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            phi_inv_t = M.scalar_field({CM: z-x**2-y**2})
            N.set_embedding(phi, inverse=phi_inv, var=t,
                            t_inverse = {t:phi_inv_t})
            N.adapted_chart()
            P0 = N.plot({t:0}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
                        CN, CM, opacity=0.3, mesh=True)
            P1 = N.plot({t:1}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
                        CN, CM, opacity=0.3, mesh=True)
            P2 = N.plot({t:2}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
                        CN, CM, opacity=0.3, mesh=True)
            P3 = N.plot({t:3}, srange(-1, 1, 0.1), srange(-1, 1, 0.1),
                        CN, CM, opacity=0.3, mesh=True)
            sphinx_plot(P0 + P1 + P2 + P3)

        .. SEEALSO::

            :class:`~sage.plot.plot3d.parametric_surface.ParametricSurface`
        """
    def ambient(self) -> TopologicalManifold:
        """
        Return the manifold in which ``self`` is immersed or embedded.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: N.ambient()
            3-dimensional topological manifold M
        """
    def immersion(self) -> ContinuousMap:
        """
        Return the immersion of ``self`` into the ambient manifold.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var('t')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: N.set_immersion(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse={t: phi_inv_t})
            sage: N.immersion()
            Continuous map from the 2-dimensional topological submanifold N
             immersed in the 3-dimensional topological manifold M to the
             3-dimensional topological manifold M
        """
    def embedding(self) -> ContinuousMap:
        """
        Return the embedding of ``self`` into the ambient manifold.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='topological')
            sage: N = Manifold(2, 'N', ambient=M, structure='topological')
            sage: CM.<x,y,z> = M.chart()
            sage: CN.<u,v> = N.chart()
            sage: t = var('t')
            sage: phi = N.continuous_map(M, {(CN,CM): [u,v,t+u^2+v^2]})
            sage: phi_inv = M.continuous_map(N, {(CM,CN): [x,y]})
            sage: phi_inv_t = M.scalar_field({CM: z-x^2-y^2})
            sage: N.set_embedding(phi, inverse=phi_inv, var=t,
            ....:                 t_inverse={t: phi_inv_t})
            sage: N.embedding()
            Continuous map from the 2-dimensional topological submanifold N
             embedded in the 3-dimensional topological manifold M to the
             3-dimensional topological manifold M
        """
    def as_subset(self):
        """
        Return ``self`` as a subset of the ambient manifold.

        ``self`` must be an embedded submanifold.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: N = Manifold(1, 'N', ambient=M, structure='topological')
            sage: CM.<x,y> = M.chart()
            sage: CN.<u> = N.chart(coord_restrictions=lambda u: [u > -1, u < 1])
            sage: phi = N.continuous_map(M, {(CN,CM): [u, u^2]})
            sage: N.set_embedding(phi)
            sage: N
            1-dimensional topological submanifold N
              embedded in the 2-dimensional topological manifold M
            sage: N.as_subset()
            Image of the Continuous map
              from the 1-dimensional topological submanifold N
                embedded in the 2-dimensional topological manifold M
              to the 2-dimensional topological manifold M
        """
