from sage.tensor.modules.free_module_element import FiniteRankFreeModuleElement as FiniteRankFreeModuleElement

class VectorBundleFiberElement(FiniteRankFreeModuleElement):
    """
    Vector in a fiber of a vector bundle at the given point.

    INPUT:

    - ``parent`` -- :class:`~sage.manifolds.vector_bundle_fiber.VectorBundleFiber`;
      the fiber to which the vector belongs
    - ``name`` -- (default: ``None``) string; symbol given to the vector
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
      the vector; if ``None``, ``name`` will be used

    EXAMPLES:

    A vector `v` in a fiber of a rank 2 vector bundle::

        sage: M = Manifold(2, 'M', structure='top')
        sage: X.<x,y> = M.chart()
        sage: p = M((1,-1), name='p')
        sage: E = M.vector_bundle(2, 'E')
        sage: e = E.local_frame('e')
        sage: Ep = E.fiber(p)
        sage: v = Ep((-2,1), name='v'); v
        Vector v in the fiber of E at Point p on the 2-dimensional topological
         manifold M
        sage: v.display()
        v = -2 e_0 + e_1
        sage: v.parent()
        Fiber of E at Point p on the 2-dimensional topological manifold M
        sage: v in Ep
        True

    .. SEEALSO::

        :class:`~sage.tensor.modules.free_module_element.FiniteRankFreeModuleElement`
        for more documentation.
    """
    def __init__(self, parent, name=None, latex_name=None) -> None:
        """
        Construct a vector in the given fiber of a given vector bundle.

        TESTS::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: p = M((1,-1), name='p')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: Ep = E.fiber(p)
            sage: v = Ep.element_class(Ep, name='v') ; v
            Vector v in the fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: v[:] = 5, -3/2
            sage: TestSuite(v).run()
        """
