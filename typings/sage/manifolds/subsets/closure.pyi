from sage.manifolds.subset import ManifoldSubset as ManifoldSubset

class ManifoldSubsetClosure(ManifoldSubset):
    """
    Topological closure of a manifold subset in the topology of the manifold.

    INPUT:

    - ``subset`` -- a :class:`~sage.manifolds.subset.ManifoldSubset`
    - ``name`` -- (default: computed from the name of the subset)
      string; name (symbol) given to the closure
    - ``latex_name`` -- string (default: ``None``); LaTeX symbol to
      denote the subset. If none is provided, it is set to ``name``.

    EXAMPLES::

        sage: M = Manifold(2, 'R^2', structure='topological')
        sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
        sage: D = M.open_subset('D', coord_def={c_cart: x^2+y^2<1}); D
        Open subset D of the 2-dimensional topological manifold R^2
        sage: cl_D = D.closure()
        sage: cl_D
        Topological closure cl_D of the Open subset D of the 2-dimensional
         topological manifold R^2
        sage: latex(cl_D)
        \\mathop{\\mathrm{cl}}(D)
        sage: type(cl_D)
        <class 'sage.manifolds.subsets.closure.ManifoldSubsetClosure_with_category'>
        sage: cl_D.category()
        Category of subobjects of sets

    The closure of the subset `D` is a subset of every closed superset
    of `D`::

        sage: S = D.superset('S')
        sage: S.declare_closed()
        sage: cl_D.is_subset(S)
        True
    """
    def __init__(self, subset, name=None, latex_name=None) -> None:
        """
        Initialize a :class:`ManifoldSubsetClosure` instance.

        TESTS::

            sage: from sage.manifolds.subsets.closure import ManifoldSubsetClosure
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: D = M.open_subset('D', coord_def={c_cart: x^2+y^2<1}); D
            Open subset D of the 2-dimensional topological manifold R^2
            sage: cl_D = D.closure(); cl_D  # indirect doctest
            Topological closure cl_D of the
             Open subset D of the 2-dimensional topological manifold R^2
            sage: also_cl_D = ManifoldSubsetClosure(D, name='also_cl_D'); also_cl_D
            Topological closure also_cl_D of the
             Open subset D of the 2-dimensional topological manifold R^2
            sage: cl_D is also_cl_D
            False
            sage: cl_D == also_cl_D
            False
        """
    def is_closed(self):
        """
        Return if ``self`` is a closed set.

        This implementation of the method always returns ``True``.

        EXAMPLES::

            sage: from sage.manifolds.subsets.closure import ManifoldSubsetClosure
            sage: M = Manifold(2, 'R^2', structure='topological')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: D = M.open_subset('D', coord_def={c_cart: x^2+y^2<1}); D
            Open subset D of the 2-dimensional topological manifold R^2
            sage: cl_D = D.closure(); cl_D  # indirect doctest
            Topological closure cl_D of the Open subset D of the 2-dimensional topological manifold R^2
            sage: cl_D.is_closed()
            True
        """
