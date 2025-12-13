from sage.manifolds.subset import ManifoldSubset as ManifoldSubset

class ImageManifoldSubset(ManifoldSubset):
    """
    Subset of a topological manifold that is a continuous image of a manifold subset.

    INPUT:

    - ``map`` -- continuous map `\\Phi`
    - ``inverse`` -- (default: ``None``) continuous map from
      ``map.codomain()`` to ``map.domain()``, which once restricted to the image
      of `\\Phi` is the inverse of `\\Phi` onto its image if the latter
      exists (NB: no check of this is performed)
    - ``name`` -- (default: computed from the names of the map and the subset)
      string; name (symbol) given to the subset
    - ``latex_name`` -- string (default: ``None``); LaTeX symbol to
      denote the subset; if none is provided, it is set to ``name``
    - ``domain_subset`` -- (default: the domain of ``map``) a subset of the domain of
      ``map``
    """
    def __init__(self, map, inverse=None, name=None, latex_name=None, domain_subset=None) -> None:
        """
        Construct a manifold subset that is the image of a continuous map.

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: N = Manifold(1, 'N', ambient=M, structure='topological')
            sage: CM.<x,y> = M.chart()
            sage: CN.<u> = N.chart(coord_restrictions=lambda u: [u > -1, u < 1])
            sage: Phi = N.continuous_map(M, {(CN,CM): [u, 1 + u^2]}, name='Phi')
            sage: Phi_inv = M.continuous_map(N, {(CM, CN): [x]}, name='Phi_inv')
            sage: Phi_N = Phi.image(inverse=Phi_inv)
            sage: TestSuite(Phi_N).run()
        """
    def __contains__(self, point) -> bool:
        """
        Check whether ``point`` is contained in ``self``.

        TESTS::

            sage: M = Manifold(2, 'M', structure='topological')
            sage: N = Manifold(1, 'N', ambient=M, structure='topological')
            sage: CM.<x,y> = M.chart()
            sage: CN.<u> = N.chart(coord_restrictions=lambda u: [u > -1, u < 1])
            sage: Phi = N.continuous_map(M, {(CN,CM): [u, 1 + u^2]}, name='Phi')
            sage: Phi_inv = M.continuous_map(N, {(CM, CN): [x]}, name='Phi_inv')
            sage: Phi_N = Phi.image(inverse=Phi_inv)
            sage: M((0, 0)) in Phi_N
            False
            sage: M((0, 1)) in Phi_N
            True
        """
