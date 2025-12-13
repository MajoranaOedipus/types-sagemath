from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule as FiniteRankFreeModule
from sage.tensor.modules.free_module_basis import FreeModuleBasis as FreeModuleBasis, FreeModuleCoBasis as FreeModuleCoBasis

class LocalCoFrame(FreeModuleCoBasis):
    """
    Local coframe on a vector bundle.

    A *local coframe* on a vector bundle `E \\to M` of class `C^k` is a
    local section `e^*: U \\to E^n` of class `C^k` on some subset `U` of the base
    space `M`, such that `e^*(p)` is a basis of the fiber `E^*_p` of the dual
    bundle for any `p \\in U`.

    INPUT:

    - ``frame`` -- the local frame dual to the coframe
    - ``symbol`` -- either a string, to be used as a common base for the
      symbols of the linear forms constituting the coframe, or a tuple of
      strings, representing the individual symbols of the linear forms
    - ``latex_symbol`` -- (default: ``None``) either a string, to be used
      as a common base for the LaTeX symbols of the linear forms constituting
      the coframe, or a tuple of strings, representing the individual LaTeX
      symbols of the linear forms; if ``None``, ``symbol`` is used in place of
      ``latex_symbol``
    - ``indices`` -- (default: ``None``; used only if ``symbol`` is a single
      string) tuple of strings representing the indices labelling the linear
      forms  of the coframe; if ``None``, the indices will be generated as
      integers within the range declared on the coframe's domain
    - ``latex_indices`` -- (default: ``None``) tuple of strings representing
      the indices for the LaTeX symbols of the linear forms of the coframe; if
      ``None``, ``indices`` is used instead

    EXAMPLES:

    Local coframe on a topological vector bundle of rank 3::

        sage: M = Manifold(3, 'M', structure='top', start_index=1)
        sage: X.<x,y,z> = M.chart()
        sage: E = M.vector_bundle(3, 'E')
        sage: e = E.local_frame('e')
        sage: from sage.manifolds.local_frame import LocalCoFrame
        sage: f = LocalCoFrame(e, 'f'); f
        Local coframe (E|_M, (f^1,f^2,f^3))

    The local coframe can also be obtained by using the method
    :meth:`~sage.tensor.modules.free_module_basis.FreeModuleBasis.dual_basis` or
    :meth:`~sage.manifolds.local_frame.LocalFrame.coframe`::

        sage: e_dual = e.dual_basis(); e_dual
        Local coframe (E|_M, (e^1,e^2,e^3))
        sage: e_dual is e.coframe()
        True
        sage: e_dual is f
        False
        sage: e_dual[:] == f[:]
        True
        sage: f[1].display(e)
        f^1 = e^1

    The consisted linear forms can be obtained via the operator ``[]``::

        sage: f[1], f[2], f[3]
        (Linear form f^1 on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3,
         Linear form f^2 on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3,
         Linear form f^3 on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3)

    Checking that `f` is the dual of `e`::

        sage: f[1](e[1]).expr(), f[1](e[2]).expr(), f[1](e[3]).expr()
        (1, 0, 0)
        sage: f[2](e[1]).expr(), f[2](e[2]).expr(), f[2](e[3]).expr()
        (0, 1, 0)
        sage: f[3](e[1]).expr(), f[3](e[2]).expr(), f[3](e[3]).expr()
        (0, 0, 1)
    """
    def __init__(self, frame, symbol, latex_symbol=None, indices=None, latex_indices=None) -> None:
        """
        Construct a local coframe, dual to a given local frame.

        TESTS::

            sage: M = Manifold(3, 'M')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: from sage.manifolds.local_frame import LocalCoFrame
            sage: f = LocalCoFrame(e, 'f'); f
            Local coframe (E|_M, (f^0,f^1))
            sage: TestSuite(f).run()
        """
    def at(self, point):
        """
        Return the value of ``self`` at a given point on the base space, this
        value being a basis of the dual vector bundle at this point.

        INPUT:

        - ``point`` -- :class:`~sage.manifolds.point.ManifoldPoint`;
          point `p` in the domain `U` of the coframe (denoted `f` hereafter)

        OUTPUT:

        - :class:`~sage.tensor.modules.free_module_basis.FreeModuleCoBasis`
          representing the basis `f(p)` of the vector space `E^*_p`,
          dual to the vector bundle fiber `E_p`

        EXAMPLES:

        Cobasis of a vector bundle fiber::

            sage: M = Manifold(2, 'M', structure='top', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: e_dual = e.coframe(); e_dual
            Local coframe (E|_M, (e^1,e^2))
            sage: p = M.point((-1,2), name='p')
            sage: e_dual_p = e_dual.at(p) ; e_dual_p
            Dual basis (e^1,e^2) on the Fiber of E at Point p on the
            2-dimensional topological manifold M
            sage: type(e_dual_p)
            <class 'sage.tensor.modules.free_module_basis.FreeModuleCoBasis_with_category'>
            sage: e_dual_p[1]
            Linear form e^1 on the Fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: e_dual_p[2]
            Linear form e^2 on the Fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: e_dual_p is e.at(p).dual_basis()
            True
        """
    def set_name(self, symbol, latex_symbol=None, indices=None, latex_indices=None, index_position: str = 'up', include_domain: bool = True) -> None:
        """
        Set (or change) the text name and LaTeX name of ``self``.

        INPUT:

        - ``symbol`` -- either a string, to be used as a common base for the
          symbols of the linear forms constituting the coframe, or a list/tuple
          of strings, representing the individual symbols of the linear forms
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the linear forms
          constituting the coframe, or a list/tuple of strings, representing the
          individual LaTeX symbols of the linear forms; if ``None``, ``symbol``
          is used in place of ``latex_symbol``
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices labelling
          the linear forms of the coframe; if ``None``, the indices will be
          generated as integers within the range declared on ``self``
        - ``latex_indices`` -- (default: ``None``) tuple of strings
          representing the indices for the LaTeX symbols of the linear forms;
          if ``None``, ``indices`` is used instead
        - ``index_position`` -- (default: ``'up'``) determines the position
          of the indices labelling the linear forms of the coframe; can be
          either ``'down'`` or ``'up'``
        - ``include_domain`` -- boolean (default: ``True``); determining whether
          the name of the domain is included in the beginning of the coframe
          name

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e').coframe(); e
            Local coframe (E|_M, (e^0,e^1))
            sage: e.set_name('f'); e
            Local coframe (E|_M, (f^0,f^1))
            sage: e.set_name('e', latex_symbol=r'\\epsilon')
            sage: latex(e)
            \\left(E|_{M}, \\left(\\epsilon^{0},\\epsilon^{1}\\right)\\right)
            sage: e.set_name('e', include_domain=False); e
            Local coframe (e^0,e^1)
            sage: e.set_name(['a', 'b'], latex_symbol=[r'\\alpha', r'\\beta']); e
            Local coframe (E|_M, (a,b))
            sage: latex(e)
            \\left(E|_{M}, \\left(\\alpha,\\beta\\right)\\right)
            sage: e.set_name('e', indices=['x','y'],
            ....:            latex_indices=[r'\\xi', r'\\zeta']); e
            Local coframe (E|_M, (e^x,e^y))
            sage: latex(e)
            \\left(E|_{M}, \\left(e^{\\xi},e^{\\zeta}\\right)\\right)
        """

class LocalFrame(FreeModuleBasis):
    """
    Local frame on a vector bundle.

    A *local frame* on a vector bundle `E \\to M` of class `C^k` is a local
    section `(e_1,\\dots,e_n):U \\to E^n` of class `C^k` defined on some subset `U`
    of the base space `M`, such that `e(p)` is a basis of the fiber `E_p` for
    any `p \\in U`.

    For each instantiation of a local frame, a local coframe is automatically
    created, as an instance of the class :class:`LocalCoFrame`. It is returned
    by the method :meth:`coframe`.

    INPUT:

    - ``section_module`` -- free module of local sections over `U` in the given
      vector bundle `E \\to M`
    - ``symbol`` -- either a string, to be used as a common base for the
      symbols of the local sections constituting the local frame, or a tuple
      of strings, representing the individual symbols of the local sections
    - ``latex_symbol`` -- (default: ``None``) either a string, to be used
      as a common base for the LaTeX symbols of the local sections constituting
      the local frame, or a tuple of strings, representing the individual
      LaTeX symbols of the local sections; if ``None``, ``symbol`` is used in
      place of ``latex_symbol``
    - ``indices`` -- (default: ``None``; used only if ``symbol`` is a single
      string) tuple of strings representing the indices labelling the local
      sections of the frame; if ``None``, the indices will be generated as
      integers within the range declared on the local frame's domain
    - ``latex_indices`` -- (default: ``None``) tuple of strings representing
      the indices for the LaTeX symbols of the  local sections; if
      ``None``, ``indices`` is used instead
    - ``symbol_dual`` -- (default: ``None``) same as ``symbol`` but for the
      dual coframe; if ``None``, ``symbol`` must be a string and is used
      for the common base of the symbols of the elements of the dual coframe
    - ``latex_symbol_dual`` -- (default: ``None``) same as ``latex_symbol``
      but for the dual coframe

    EXAMPLES:

    Defining a local frame on a 3-dimensional vector bundle over a 3-dimensional
    manifold::

        sage: M = Manifold(3, 'M', start_index=1, structure='top')
        sage: E = M.vector_bundle(3, 'E')
        sage: e = E.local_frame('e'); e
        Local frame (E|_M, (e_1,e_2,e_3))
        sage: latex(e)
        \\left(E|_{M}, \\left(e_{1},e_{2},e_{3}\\right)\\right)

    The individual elements of the vector frame are accessed via square
    brackets, with the possibility to invoke the slice operator '``:``' to
    get more than a single element::

        sage: e[2]
        Section e_2 on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3
        sage: e[1:3]
        (Section e_1 on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3,
         Section e_2 on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3)
        sage: e[:]
        (Section e_1 on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3,
         Section e_2 on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3,
         Section e_3 on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3)

    The LaTeX symbol can be specified::

        sage: eps = E.local_frame('eps', latex_symbol=r'\\epsilon')
        sage: latex(eps)
        \\left(E|_{M}, \\left(\\epsilon_{1},\\epsilon_{2},\\epsilon_{3}\\right)\\right)

    By default, the elements of the local frame are labelled by integers
    within the range specified at the manifold declaration. It is however
    possible to fully customize the labels, via the argument ``indices``::

        sage: u = E.local_frame('u', indices=('x', 'y', 'z')) ; u
        Local frame (E|_M, (u_x,u_y,u_z))
        sage: u[1]
        Section u_x on the 3-dimensional topological manifold M with values in
         the real vector bundle E of rank 3
        sage: u.coframe()
        Local coframe (E|_M, (u^x,u^y,u^z))

    The LaTeX format of the indices can be adjusted::

        sage: v = E.local_frame('v', indices=('a', 'b', 'c'),
        ....:                    latex_indices=(r'\\alpha', r'\\beta', r'\\gamma'))
        sage: v
        Local frame (E|_M, (v_a,v_b,v_c))
        sage: latex(v)
        \\left(E|_{M}, \\left(v_{\\alpha},v_{\\beta},v_{\\gamma}\\right)\\right)
        sage: latex(v.coframe())
        \\left(E|_{M}, \\left(v^{\\alpha},v^{\\beta},v^{\\gamma}\\right)\\right)

    The symbol of each element of the local frame can also be freely chosen,
    by providing a tuple of symbols as the first argument of ``local_frame``;
    it is then mandatory to specify as well some symbols for the dual coframe::

        sage: h = E.local_frame(('a', 'b', 'c'), symbol_dual=('A', 'B', 'C')); h
        Local frame (E|_M, (a,b,c))
        sage: h[1]
        Section a on the 3-dimensional topological manifold M with values in the
         real vector bundle E of rank 3
        sage: h.coframe()
        Local coframe (E|_M, (A,B,C))
        sage: h.coframe()[1]
        Linear form A on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3

    Local frames are bases of free modules formed by local sections::

        sage: N = Manifold(2, 'N', structure='top', start_index=1)
        sage: X.<x,y> = N.chart()
        sage: U = N.open_subset('U')
        sage: F = N.vector_bundle(2, 'F')
        sage: f = F.local_frame('f', domain=U)
        sage: f.module()
        Free module C^0(U;F) of sections on the Open subset U of the
         2-dimensional topological manifold N with values in the real vector
         bundle F of rank 2
        sage: f.module().base_ring()
        Algebra of scalar fields on the Open subset U of the 2-dimensional
         topological manifold N
        sage: f.module() is F.section_module(domain=f.domain())
        True
        sage: f in F.section_module(domain=U).bases()
        True

    The value of the local frame at a given point is a basis of the
    corresponding fiber::

        sage: X_U = X.restrict(U) # We need coordinates on the subset
        sage: p = N((0,1), name='p') ; p
        Point p on the 2-dimensional topological manifold N
        sage: f.at(p)
        Basis (f_1,f_2) on the Fiber of F at Point p on the 2-dimensional
         topological manifold N
    """
    @staticmethod
    def __classcall_private__(cls, section_module, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Transform input lists into tuples for the unique representation of
        LocalFrame.

        TESTS::

            sage: M = Manifold(3, 'M')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module(force_free=True)
            sage: from sage.manifolds.local_frame import LocalFrame
            sage: e = LocalFrame(C0, ['a', 'b'], symbol_dual=['A', 'B']); e
            Local frame (E|_M, (a,b))
            sage: e.dual_basis()
            Local coframe (E|_M, (A,B))
            sage: e is LocalFrame(C0, ('a', 'b'), symbol_dual=('A', 'B'))
            True
        """
    def __init__(self, section_module, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None) -> None:
        """
        Construct a local frame on a vector bundle.

        TESTS:

            sage: M = Manifold(3, 'M')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module(force_free=True)
            sage: from sage.manifolds.local_frame import LocalFrame
            sage: e = LocalFrame(C0, 'e', latex_symbol=r'\\epsilon'); e
            Local frame (E|_M, (e_0,e_1))
            sage: TestSuite(e).run()
        """
    def domain(self):
        """
        Return the domain on which ``self`` is defined.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e', domain=U); e
            Local frame (E|_U, (e_0,e_1))
            sage: e.domain()
            Open subset U of the 3-dimensional topological manifold M
        """
    def base_space(self):
        """
        Return the base space on which the overlying vector bundle is defined.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e', domain=U)
            sage: e.base_space()
            3-dimensional topological manifold M
        """
    def vector_bundle(self):
        """
        Return the vector bundle on which ``self`` is defined.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e', domain=U)
            sage: e.vector_bundle()
            Topological real vector bundle E -> M of rank 2 over the base space
            3-dimensional topological manifold M
            sage: e.vector_bundle() is E
            True
        """
    def coframe(self):
        """
        Return the coframe of ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e'); e
            Local frame (E|_M, (e_0,e_1))
            sage: e.coframe()
            Local coframe (E|_M, (e^0,e^1))
        """
    def new_frame(self, change_of_frame, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Define a new local frame from ``self``.

        The new local frame is defined from vector bundle automorphisms; its
        module is the same as that of the current frame.

        INPUT:

        - ``change_of_frame`` --
          :class:`~sage.tensor.modules.free_module_automorphism.FreeModuleAutomorphism`;
          vector bundle automorphisms `P` that relates
          the current frame `(e_i)` to the new frame `(f_i)` according
          to `f_i = P(e_i)`
        - ``symbol`` -- either a string, to be used as a common base for the
          symbols of the sections constituting the local frame, or a
          list/tuple of strings, representing the individual symbols of the
          sections
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the sections
          constituting the local frame, or a list/tuple of strings,
          representing the individual LaTeX symbols of the sections;
          if ``None``, ``symbol`` is used in place of ``latex_symbol``
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices labelling
          the sections of the frame; if ``None``, the indices will be
          generated as integers within the range declared on ``self``
        - ``latex_indices`` -- (default: ``None``) tuple of strings
          representing the indices for the LaTeX symbols of the sections;
          if ``None``, ``indices`` is used instead
        - ``symbol_dual`` -- (default: ``None``) same as ``symbol`` but for the
          dual coframe; if ``None``, ``symbol`` must be a string and is used
          for the common base of the symbols of the elements of the dual
          coframe
        - ``latex_symbol_dual`` -- (default: ``None``) same as ``latex_symbol``
          but for the dual coframe

        OUTPUT:

        - the new frame `(f_i)`, as an instance of :class:`LocalFrame`

        EXAMPLES:

        Orthogonal transformation of a frame on the 2-dimensional trivial vector
        bundle over the Euclidean plane::

            sage: M = Manifold(2, 'R^2', structure='top', start_index=1)
            sage: c_cart.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e'); e
            Local frame (E|_R^2, (e_1,e_2))
            sage: orth = E.section_module().automorphism()
            sage: orth[:] = [[sqrt(3)/2, -1/2], [1/2, sqrt(3)/2]]
            sage: f = e.new_frame(orth, 'f')
            sage: f[1][:]
            [1/2*sqrt(3), 1/2]
            sage: f[2][:]
            [-1/2, 1/2*sqrt(3)]
            sage: a =  E.change_of_frame(e,f)
            sage: a[:]
            [1/2*sqrt(3)        -1/2]
            [        1/2 1/2*sqrt(3)]
            sage: a == orth
            True
            sage: a is orth
            False
            sage: a._components # random (dictionary output)
            {Local frame (E|_D_0, (e_1,e_2)): 2-indices components w.r.t.
             Local frame (E|_D_0, (e_1,e_2)),
             Local frame (E|_D_0, (f_1,f_2)): 2-indices components w.r.t.
             Local frame (E|_D_0, (f_1,f_2))}
            sage: a.comp(f)[:]
            [1/2*sqrt(3)        -1/2]
             [        1/2 1/2*sqrt(3)]
            sage: a1 = E.change_of_frame(f,e)
            sage: a1[:]
            [1/2*sqrt(3)         1/2]
            [       -1/2 1/2*sqrt(3)]
            sage: a1 == orth.inverse()
            True
            sage: a1 is orth.inverse()
            False
            sage: e[1].comp(f)[:]
            [1/2*sqrt(3), -1/2]
            sage: e[2].comp(f)[:]
            [1/2, 1/2*sqrt(3)]
        """
    def restrict(self, subdomain):
        """
        Return the restriction of ``self`` to some open subset of its domain.

        If the restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` -- open subset `V` of the current frame domain `U`

        OUTPUT: the restriction of the current frame to `V` as a :class:`LocalFrame`

        EXAMPLES:

        Restriction of a frame defined on `\\RR^2` to the unit disk::

            sage: M = Manifold(2, 'R^2', structure='top', start_index=1)
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e'); e
            Local frame (E|_R^2, (e_1,e_2))
            sage: a = E.section_module().automorphism()
            sage: a[:] = [[1-y^2,0], [1+x^2, 2]]
            sage: f = e.new_frame(a, 'f'); f
            Local frame (E|_R^2, (f_1,f_2))
            sage: U = M.open_subset('U', coord_def={c_cart: x^2+y^2<1})
            sage: e_U = e.restrict(U); e_U
            Local frame (E|_U, (e_1,e_2))
            sage: f_U = f.restrict(U) ; f_U
            Local frame (E|_U, (f_1,f_2))

        The vectors of the restriction have the same symbols as those of the
        original frame::

            sage: f_U[1].display()
            f_1 = (-y^2 + 1) e_1 + (x^2 + 1) e_2
            sage: f_U[2].display()
            f_2 = 2 e_2

        Actually, the components are the restrictions of the original frame
        vectors::

            sage: f_U[1] is f[1].restrict(U)
            True
            sage: f_U[2] is f[2].restrict(U)
            True
        """
    def at(self, point):
        """
        Return the value of ``self`` at a given point, this value being
        a basis of the vector bundle fiber at the point.

        INPUT:

        - ``point`` -- :class:`~sage.manifolds.point.ManifoldPoint`; point
          `p` in the domain `U` of the local frame (denoted `e` hereafter)

        OUTPUT:

        - :class:`~sage.tensor.modules.free_module_basis.FreeModuleBasis`
          representing the basis `e(p)` of the vector bundle fiber
          `E_p`

        EXAMPLES:

        Basis of a fiber of a trivial vector bundle::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e'); e
            Local frame (E|_M, (e_0,e_1))
            sage: p = M.point((-1,2), name='p')
            sage: ep = e.at(p) ; ep
            Basis (e_0,e_1) on the Fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: type(ep)
            <class 'sage.tensor.modules.free_module_basis.FreeModuleBasis_with_category'>
            sage: ep[0]
            Vector e_0 in the fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: ep[1]
            Vector e_1 in the fiber of E at Point p on the 2-dimensional
             topological manifold M

        Note that the symbols used to denote the vectors are same as those
        for the vector fields of the frame. At this stage, ``ep`` is the unique
        basis on fiber at ``p``::

            sage: Ep = E.fiber(p)
            sage: Ep.bases()
            [Basis (e_0,e_1) on the Fiber of E at Point p on the 2-dimensional
             topological manifold M]

        Let us consider another local frame::

            sage: aut = E.section_module().automorphism()
            sage: aut[:] = [[1+y^2, 0], [0, 2]]
            sage: f = e.new_frame(aut, 'f') ; f
            Local frame (E|_M, (f_0,f_1))
            sage: fp = f.at(p) ; fp
            Basis (f_0,f_1) on the Fiber of E at Point p on the 2-dimensional
             topological manifold M

        There are now two bases on the fiber::

            sage: Ep.bases()
            [Basis (e_0,e_1) on the Fiber of E at Point p on the 2-dimensional
             topological manifold M,
             Basis (f_0,f_1) on the Fiber of E at Point p on the 2-dimensional
             topological manifold M]

        Moreover, the changes of bases in the tangent space have been
        computed from the known relation between the frames ``e`` and
        ``f`` (via the automorphism ``aut`` defined above)::

            sage: Ep.change_of_basis(ep, fp)
            Automorphism of the Fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: Ep.change_of_basis(ep, fp).display()
            5 e_0⊗e^0 + 2 e_1⊗e^1
            sage: Ep.change_of_basis(fp, ep)
            Automorphism of the Fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: Ep.change_of_basis(fp, ep).display()
            1/5 e_0⊗e^0 + 1/2 e_1⊗e^1

        The dual bases::

            sage: e.coframe()
            Local coframe (E|_M, (e^0,e^1))
            sage: ep.dual_basis()
            Dual basis (e^0,e^1) on the Fiber of E at Point p on the
             2-dimensional topological manifold M
            sage: ep.dual_basis() is e.coframe().at(p)
            True
            sage: f.coframe()
            Local coframe (E|_M, (f^0,f^1))
            sage: fp.dual_basis()
            Dual basis (f^0,f^1) on the Fiber of E at Point p on the
             2-dimensional topological manifold M
            sage: fp.dual_basis() is f.coframe().at(p)
            True
        """
    def set_name(self, symbol, latex_symbol=None, indices=None, latex_indices=None, index_position: str = 'down', include_domain: bool = True) -> None:
        """
        Set (or change) the text name and LaTeX name of ``self``.

        INPUT:

        - ``symbol`` -- either a string, to be used as a common base for the
          symbols of the local sections constituting the local frame, or a
          list/tuple of strings, representing the individual symbols of the
          local sections
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the local sections
          constituting the local frame, or a list/tuple of strings,
          representing the individual LaTeX symbols of the local sections;
          if ``None``, ``symbol`` is used in place of ``latex_symbol``
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices labelling
          the local sections of the frame; if ``None``, the indices will be
          generated as integers within the range declared on ``self``
        - ``latex_indices`` -- (default: ``None``) tuple of strings
          representing the indices for the LaTeX symbols of the local sections;
          if ``None``, ``indices`` is used instead
        - ``index_position`` -- (default: ``'down'``) determines the position
          of the indices labelling the local sections of the frame; can be
          either ``'down'`` or ``'up'``
        - ``include_domain`` -- boolean (default: ``True``); determining whether
          the name of the domain is included in the beginning of the vector
          frame name

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e'); e
            Local frame (E|_M, (e_0,e_1))
            sage: e.set_name('f'); e
            Local frame (E|_M, (f_0,f_1))
            sage: e.set_name('e', include_domain=False); e
            Local frame (e_0,e_1)
            sage: e.set_name(['a', 'b']); e
            Local frame (E|_M, (a,b))
            sage: e.set_name('e', indices=['x', 'y']); e
            Local frame (E|_M, (e_x,e_y))
            sage: e.set_name('e', latex_symbol=r'\\epsilon')
            sage: latex(e)
            \\left(E|_{M}, \\left(\\epsilon_{0},\\epsilon_{1}\\right)\\right)
            sage: e.set_name('e', latex_symbol=[r'\\alpha', r'\\beta'])
            sage: latex(e)
            \\left(E|_{M}, \\left(\\alpha,\\beta\\right)\\right)
            sage: e.set_name('e', latex_symbol='E',
            ....:            latex_indices=[r'\\alpha', r'\\beta'])
            sage: latex(e)
            \\left(E|_{M}, \\left(E_{\\alpha},E_{\\beta}\\right)\\right)
        """

class TrivializationCoFrame(LocalCoFrame):
    """
    Trivialization coframe on a vector bundle.

    A *trivialization coframe* is the coframe of the trivialization frame
    induced by a trivialization (see: :class:`~sage.manifolds.local_frame.TrivializationFrame`).

    More precisely, a *trivialization frame* on a vector bundle `E \\to M` of
    class `C^k` and rank `n` over the topological field `K` and over a
    topological manifold `M` is a local coframe induced by a local
    trivialization `\\varphi:E|_U \\to U \\times K^n` of the domain `U \\in M`.
    Namely, the local dual sections

    .. MATH::

        \\varphi^*e^i := \\varphi(\\;\\cdot\\;, e^i)

    on `U` induce a local frame `(\\varphi^*e^1, \\dots, \\varphi^*e^n)`, where
    `(e^1, \\dots, e^n)` is the dual of the standard basis of `K^n`.

    INPUT:

    - ``triv_frame`` -- trivialization frame dual to the trivialization coframe
    - ``symbol`` -- either a string, to be used as a common base for the
      symbols of the dual sections constituting the coframe, or a tuple of
      strings, representing the individual symbols of the dual sections
    - ``latex_symbol`` -- (default: ``None``) either a string, to be used
      as a common base for the LaTeX symbols of the dual sections constituting
      the coframe, or a tuple of strings, representing the individual LaTeX
      symbols of the dual sections; if ``None``, ``symbol`` is used in place of
      ``latex_symbol``
    - ``indices`` -- (default: ``None``; used only if ``symbol`` is a single
      string) tuple of strings representing the indices labelling the dual
      sections of the coframe; if ``None``, the indices will be generated as
      integers within the range declared on the local frame's domain
    - ``latex_indices`` -- (default: ``None``) tuple of strings representing
      the indices for the LaTeX symbols of the dual sections of the coframe; if
      ``None``, ``indices`` is used instead

    EXAMPLES:

    Trivialization coframe on a trivial vector bundle of rank 3::

        sage: M = Manifold(3, 'M', start_index=1, structure='top')
        sage: X.<x,y,z> = M.chart()
        sage: E = M.vector_bundle(3, 'E')
        sage: phi = E.trivialization('phi'); phi
        Trivialization (phi, E|_M)
        sage: E.frames()
        [Trivialization frame (E|_M, ((phi^*e_1),(phi^*e_2),(phi^*e_3)))]
        sage: E.coframes()
        [Trivialization coframe (E|_M, ((phi^*e^1),(phi^*e^2),(phi^*e^3)))]
        sage: f = E.coframes()[0] ; f
        Trivialization coframe (E|_M, ((phi^*e^1),(phi^*e^2),(phi^*e^3)))

    The linear forms composing the coframe are obtained via the operator
    ``[]``::

        sage: f[1]
        Linear form (phi^*e^1) on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3
        sage: f[2]
        Linear form (phi^*e^2) on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3
        sage: f[3]
        Linear form (phi^*e^3) on the Free module C^0(M;E) of sections on the
         3-dimensional topological manifold M with values in the real vector
         bundle E of rank 3
        sage: f[1][:]
        [1, 0, 0]
        sage: f[2][:]
        [0, 1, 0]
        sage: f[3][:]
        [0, 0, 1]

    The coframe is the dual of the trivialization frame::

        sage: e = phi.frame() ; e
        Trivialization frame (E|_M, ((phi^*e_1),(phi^*e_2),(phi^*e_3)))
        sage: f[1](e[1]).expr(), f[1](e[2]).expr(), f[1](e[3]).expr()
        (1, 0, 0)
        sage: f[2](e[1]).expr(), f[2](e[2]).expr(), f[2](e[3]).expr()
        (0, 1, 0)
        sage: f[3](e[1]).expr(), f[3](e[2]).expr(), f[3](e[3]).expr()
        (0, 0, 1)
    """
    def __init__(self, triv_frame, symbol, latex_symbol=None, indices=None, latex_indices=None) -> None:
        """
        Construct a local coframe from a local trivialization.

        TESTS::

            sage: M = Manifold(2, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: phi = E.trivialization('phi')
            sage: from sage.manifolds.local_frame import TrivializationCoFrame
            sage: f = TrivializationCoFrame(phi.frame(), 'omega'); f
            Trivialization coframe (E|_M, (omega^0,omega^1))
            sage: TestSuite(f).run()
        """

class TrivializationFrame(LocalFrame):
    """
    Trivialization frame on a topological vector bundle.

    A *trivialization frame* on a topological vector bundle `E \\to M` of rank
    `n` over the topological field `K` and over a topological manifold `M` is a
    local frame induced by a local trivialization `\\varphi:E|_U \\to U \\times K^n`
    of the domain `U \\in M`. More precisely, the local sections

    .. MATH::

        \\varphi^*e_i := \\varphi(\\;\\cdot\\;, e_i)

    on `U` induce a local frame `(\\varphi^*e_1, \\dots, \\varphi^*e_n)`, where
    `(e_1, \\dots, e_n)` is the standard basis of `K^n`.

    INPUT:

    - ``trivialization`` -- the trivialization defined on the vector bundle

    EXAMPLES::

        sage: M = Manifold(3, 'M')
        sage: U = M.open_subset('U')
        sage: E = M.vector_bundle(2, 'E')
        sage: phi_U = E.trivialization('phi_U', domain=U)
        sage: phi_U.frame()
        Trivialization frame (E|_U, ((phi_U^*e_1),(phi_U^*e_2)))
        sage: latex(phi_U.frame())
        \\left(E|_{U}, \\left(\\left(phi_U^* e_{ 1 }\\right),\\left(phi_U^* e_{ 2 }\\right)\\right)\\right)
    """
    def __init__(self, trivialization) -> None:
        """
        Construct a trivialization frame.

        TESTS::

            sage: M = Manifold(3, 'M')
            sage: E = M.vector_bundle(2, 'E')
            sage: phi = E.trivialization('phi')
            sage: e = phi.frame()
            sage: TestSuite(e).run()
        """
    def trivialization(self):
        """
        Return the underlying trivialization of ``self``.

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: phi_U = E.trivialization('phi_U', domain=U)
            sage: e = phi_U.frame()
            sage: e.trivialization()
            Trivialization (phi_U, E|_U)
            sage: e.trivialization() is phi_U
            True
        """
