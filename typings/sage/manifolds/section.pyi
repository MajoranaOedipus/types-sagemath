from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import ModuleElementWithMutability as ModuleElementWithMutability
from sage.tensor.modules.free_module_element import FiniteRankFreeModuleElement as FiniteRankFreeModuleElement
from sage.tensor.modules.tensor_with_indices import TensorWithIndices as TensorWithIndices

class Section(ModuleElementWithMutability):
    """
    Section in a vector bundle.

    An instance of this class is a section in a vector bundle `E \\to M` of class
    `C^k`, where `E|_U` is not manifestly trivial. More precisely, a
    *(local) section* on a subset `U \\in M` is a map of class `C^k`

    .. MATH::

        s: U \\longrightarrow E

    such that

    .. MATH::

        \\forall p \\in U,\\ s(p) \\in E_p

    where `E_p` denotes the vector bundle fiber of `E` over the point `p \\in U`.

    If `E|_U` is trivial, the class
    :class:`~sage.manifolds.section.TrivialSection` should be used instead.

    This is a Sage *element* class, the corresponding *parent* class being
    :class:`~sage.manifolds.section_module.SectionModule`.

    INPUT:

    - ``section_module`` -- module `C^k(U;E)` of sections on `E` over `U`
      (cf. :class:`~sage.manifolds.section_module.SectionModule`)
    - ``name`` -- (default: ``None``) name given to the section
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the section;
      if none is provided, the LaTeX symbol is set to ``name``

    EXAMPLES:

    A section on a non-trivial rank 2 vector bundle over a non-trivial
    2-manifold::

        sage: M = Manifold(2, 'M', structure='top')
        sage: U = M.open_subset('U') ; V = M.open_subset('V')
        sage: M.declare_union(U,V)   # M is the union of U and V
        sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
        sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
        ....:                    intersection_name='W', restrictions1= x>0,
        ....:                    restrictions2= u+v>0)
        sage: uv_to_xy = xy_to_uv.inverse()
        sage: W = U.intersection(V)
        sage: E = M.vector_bundle(2, 'E') # define the vector bundle
        sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
        sage: phi_V = E.trivialization('phi_V', domain=V)
        sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]]) # transition map between trivializations
        sage: fU = phi_U.frame(); fV = phi_V.frame() # define induced frames
        sage: s = E.section(name='s'); s
        Section s on the 2-dimensional topological manifold M with values in the
         real vector bundle E of rank 2

    The parent of `s` is not a free module, since `E` is not trivial::

        sage: isinstance(s.parent(), FiniteRankFreeModule)
        False

    To fully define `s`, we have to specify its components in some local
    frames defined on the trivial parts of `E`. The components consist of
    scalar fields defined on the corresponding domain. Let us start with
    `E|_U`::

        sage: s[fU,:] = [x^2, 1-y]
        sage: s.display(fU)
        s = x^2 (phi_U^*e_1) + (-y + 1) (phi_U^*e_2)

    To set the components of `s` on `V` consistently, we copy the expressions
    of the components in the common subset `W`::

        sage: fUW = fU.restrict(W); fVW = fV.restrict(W)
        sage: c_uvW = c_uv.restrict(W)
        sage: s[fV,0] = s[fVW,0,c_uvW].expr()  # long time
        sage: s[fV,1] = s[fVW,1,c_uvW].expr()  # long time

    Actually, the operation above can be performed in a single line by means
    of the method :meth:`add_comp_by_continuation`::

        sage: s.add_comp_by_continuation(fV, W, chart=c_uv)

    At this stage, `s` is fully defined, having components in frames ``fU``
    and ``fV`` and the union of the domains of ``fU`` and ``fV`` being the
    whole manifold::

        sage: s.display(fV)
        s = (-1/4*u^2 + 1/4*v^2 + 1/2*u + 1/2*v) (phi_V^*e_1)
            + (1/8*u^3 + 3/8*u^2*v + 3/8*u*v^2 + 1/8*v^3) (phi_V^*e_2)

    Sections can be pointwisely added::

        sage: t = E.section([x,y], frame=fU, name='t'); t
        Section t on the 2-dimensional topological manifold M with values in the
         real vector bundle E of rank 2
        sage: t.add_comp_by_continuation(fV, W, chart=c_uv)
        sage: t.display(fV)
        t = (1/4*u^2 - 1/4*v^2) (phi_V^*e_1) + (1/4*u^2 + 1/2*u*v + 1/4*v^2) (phi_V^*e_2)
        sage: a = s + t; a
        Section s+t on the 2-dimensional topological manifold M with values
         in the real vector bundle E of rank 2
        sage: a.display(fU)
        s+t = (x^2 + x) (phi_U^*e_1) + (phi_U^*e_2)
        sage: a.display(fV)
        s+t = (1/2*u + 1/2*v) (phi_V^*e_1) + (1/8*u^3 + 1/8*(3*u + 2)*v^2
              + 1/8*v^3 + 1/4*u^2 + 1/8*(3*u^2 + 4*u)*v) (phi_V^*e_2)

    and multiplied by scalar fields::

        sage: f = M.scalar_field(y^2-x^2, name='f')
        sage: f.add_expr_by_continuation(c_uv, W)
        sage: f.display()
        f: M → ℝ
        on U: (x, y) ↦ -x^2 + y^2
        on V: (u, v) ↦ -u*v
        sage: b = f*s; b
        Section f*s on the 2-dimensional topological manifold M with values
         in the real vector bundle E of rank 2
        sage: b.display(fU)
        f*s = (-x^4 + x^2*y^2) (phi_U^*e_1) + (x^2*y - y^3 - x^2 + y^2) (phi_U^*e_2)
        sage: b.display(fV)
        f*s = (-1/4*u*v^3 - 1/2*u*v^2 + 1/4*(u^3 - 2*u^2)*v) (phi_V^*e_1)
              + (-1/8*u^4*v - 3/8*u^3*v^2 - 3/8*u^2*v^3 - 1/8*u*v^4) (phi_V^*e_2)

    The domain on which the section should be defined, can be stated via the
    ``domain`` option in :meth:`~sage.manifolds.vector_bundle.TopologicalVectorBundle.section`::

        sage: cU = E.section([1,x], domain=U, name='c'); cU
        Section c on the Open subset U of the 2-dimensional topological manifold
         M with values in the real vector bundle E of rank 2
        sage: cU.display()
        c = (phi_U^*e_1) + x (phi_U^*e_2)

    Since `E|_U` is trivial, ``cU`` now belongs to the free module::

        sage: isinstance(cU.parent(), FiniteRankFreeModule)
        True

    Omitting the ``domain`` option, the section is defined on the whole base
    space::

        sage: c = E.section(name='c'); c
        Section c on the 2-dimensional topological manifold M with values in the
         real vector bundle E of rank 2

    Via :meth:`set_restriction`, ``cU`` can be defined as the restriction of
    ``c`` to `U`::

        sage: c.set_restriction(cU)
        sage: c.display(fU)
        c = (phi_U^*e_1) + x (phi_U^*e_2)
        sage: c.restrict(U) == cU
        True

    Notice that the zero section is immutable, and therefore its components
    cannot be changed::

        sage: zer = E.section_module().zero()
        sage: zer.is_immutable()
        True
        sage: zer.set_comp()
        Traceback (most recent call last):
        ...
        ValueError: the components of an immutable element cannot be
         changed

    Other sections can be declared immutable, too::

        sage: c.is_immutable()
        False
        sage: c.set_immutable()
        sage: c.is_immutable()
        True
        sage: c.set_comp()
        Traceback (most recent call last):
        ...
        ValueError: the components of an immutable element cannot be
         changed
        sage: c.set_name('b')
        Traceback (most recent call last):
        ...
        ValueError: the name of an immutable element cannot be changed
    """
    def __init__(self, section_module, name=None, latex_name=None) -> None:
        """
        Construct a local section.

        TESTS::

            sage: M = Manifold(1, 'S^1', structure='top', start_index=1)
            sage: U = M.open_subset('U')  # the complement of one point
            sage: c_t.<t> =  U.chart('t:(0,2*pi)') # the standard angle coordinate
            sage: V = M.open_subset('V') # the complement of the point t=pi
            sage: M.declare_union(U,V)   # S^1 is the union of U and V
            sage: c_u.<u> = V.chart('u:(0,2*pi)') # the angle t-pi
            sage: t_to_u = c_t.transition_map(c_u, (t-pi,), intersection_name='W',
            ....:                     restrictions1 = t!=pi, restrictions2 = u!=pi)
            sage: u_to_t = t_to_u.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(1, 'E')
            sage: phi_U = E.trivialization('phi_U', domain=U)
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[-1]])
            sage: C0 = E.section_module()
            sage: s = E.section([t], frame=phi_U.frame(), name='s')
            sage: s.add_comp_by_continuation(phi_V.frame(), W)
            sage: s in C0
            True
            sage: TestSuite(s).run()
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if ``self`` is nonzero and ``False`` otherwise.

        This method is called by :meth:`is_zero`.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: X.<x,y,z> = M.chart()
            sage: U = M.open_subset('U'); V = M.open_subset('V')
            sage: M.declare_union(U,V)
            sage: XU = X.restrict(U); XV = X.restrict(V)
            sage: XUV = X.restrict(U.intersection(V))
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e', domain=U)
            sage: f = E.local_frame('f', domain=V)
            sage: s = E.section(name='s')
            sage: su = E.section(name='s', domain=U)
            sage: sv = E.section(name='s', domain=V)
            sage: su[0] = 0
            sage: sv[0] = 0
            sage: s.set_restriction(su); s.set_restriction(sv)
            sage: bool(s)
            False
            sage: s.is_zero()  # indirect doctest
            True
            sage: sv[0] = 1
            sage: s.set_restriction(sv)
            sage: bool(s)
            True
            sage: s.is_zero()  # indirect doctest
            False
        """
    def set_name(self, name=None, latex_name=None) -> None:
        """
        Set (or change) the text name and LaTeX name of ``self``.

        INPUT:

        - ``name`` -- string (default: ``None``); name given to the section
        - ``latex_name`` -- string (default: ``None``); LaTeX symbol to denote
          the section; if ``None`` while ``name`` is provided, the LaTeX
          symbol is set to ``name``

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: s = E.section(); s
            Section on the 3-dimensional topological manifold M with values in
             the real vector bundle E of rank 2
            sage: s.set_name(name='s')
            sage: s
            Section s on the 3-dimensional topological manifold M with values in
             the real vector bundle E of rank 2
            sage: latex(s)
            s
            sage: s.set_name(latex_name=r'\\sigma')
            sage: latex(s)
            \\sigma
            sage: s.set_name(name='a')
            sage: s
            Section a on the 3-dimensional topological manifold M with values in
             the real vector bundle E of rank 2
            sage: latex(s)
            a
        """
    def domain(self):
        """
        Return the manifold on which ``self`` is defined.

        OUTPUT:

        - instance of class
          :class:`~sage.manifolds.manifold.TopologicalManifold`

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0_U = E.section_module(domain=U, force_free=True)
            sage: z = C0_U.zero()
            sage: z.domain()
            Open subset U of the 3-dimensional topological manifold M
        """
    def base_module(self):
        """
        Return the section module on which ``self`` acts as a section.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.section_module.SectionModule`

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: s = E.section(domain=U)
            sage: s.base_module()
            Module C^0(U;E) of sections on the Open subset U of the
             3-dimensional topological manifold M with values in the real vector
             bundle E of rank 2
        """
    def set_restriction(self, rst) -> None:
        """
        Define a restriction of ``self`` to some subdomain.

        INPUT:

        - ``rst`` -- :class:`Section` defined on a subdomain of the domain of
          ``self``

        EXAMPLES::

            sage: S2 = Manifold(2, 'S^2', structure='top')
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS,
            ....:                                   (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                                   intersection_name='W',
            ....:                                   restrictions1= x^2+y^2!=0,
            ....:                                   restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E')
            sage: phi_U = E.trivialization('phi_U', domain=U)
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: s = E.section(name='s')
            sage: sU = E.section(domain=U, name='s')
            sage: sU[:] = x+y, x
            sage: s.set_restriction(sU)
            sage: s.display(phi_U.frame())
            s = (x + y) (phi_U^*e_1) + x (phi_U^*e_2)
            sage: s.restrict(U) == sU
            True
        """
    def restrict(self, subdomain):
        """
        Return the restriction of ``self`` to some subdomain.

        If the restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` --
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
          open subset `U` of the section domain `S`

        OUTPUT: :class:`Section` representing the restriction

        EXAMPLES:

        Restrictions of a section on a rank 2 vector bundle over the 2-sphere::

            sage: S2 = Manifold(2, 'S^2', structure='top', start_index=1)
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS,
            ....:                                   (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                                   intersection_name='W',
            ....:                                   restrictions1= x^2+y^2!=0,
            ....:                                   restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[y,0]])
            sage: fN = phi_U.frame(); fS = phi_V.frame() # get induced frames
            sage: fN_W = fN.restrict(W); fS_W = fS.restrict(W) # restrict them
            sage: stereoN_W = stereoN.restrict(W) # restrict charts, too
            sage: stereoS_W = stereoS.restrict(W)
            sage: s = E.section({fN: [1, 0]}, name='s')
            sage: s.display(fN)
            s = (phi_U^*e_1)
            sage: sU = s.restrict(U) ; sU
            Section s on the Open subset U of the 2-dimensional topological
             manifold S^2 with values in the real vector bundle E of rank 2
            sage: sU.display() # fN is the default frame on U
            s = (phi_U^*e_1)
            sage: sU == fN[1]
            True
            sage: sW = s.restrict(W) ; sW
            Section s on the Open subset W of the 2-dimensional topological
             manifold S^2 with values in the real vector bundle E of rank 2
            sage: sW.display(fN_W)
            s = (phi_U^*e_1)
            sage: sW.display(fS_W, stereoN_W)
            s = y (phi_V^*e_2)
            sage: sW.display(fS_W, stereoS_W)
            s = v/(u^2 + v^2) (phi_V^*e_2)
            sage: sW == fN_W[1]
            True

        At this stage, defining the restriction of ``s`` to the open
        subset ``V`` fully specifies ``s``::

            sage: s.restrict(V)[1] = sW[fS_W, 1, stereoS_W].expr()  # note that fS is the default frame on V
            sage: s.restrict(V)[2] = sW[fS_W, 2, stereoS_W].expr()
            sage: s.display(fS, stereoS)
            s = v/(u^2 + v^2) (phi_V^*e_2)
            sage: s.restrict(U).display()
            s = (phi_U^*e_1)
            sage: s.restrict(V).display()
            s = v/(u^2 + v^2) (phi_V^*e_2)

        The restriction of the section to its own domain is of course itself::

            sage: s.restrict(S2) is s
            True
            sage: sU.restrict(U) is sU
            True
        """
    def set_comp(self, basis=None):
        """
        Return the components of ``self`` in a given local frame for assignment.

        The components with respect to other frames having the same domain
        as the provided local frame are deleted, in order to avoid any
        inconsistency. To keep them, use the method :meth:`add_comp` instead.

        INPUT:

        - ``basis`` -- (default: ``None``) local frame in which the
          components are defined; if none is provided, the components are
          assumed to refer to the section domain's default frame

        OUTPUT:

        - components in the given frame, as a
          :class:`~sage.tensor.modules.comp.Components`; if such
          components did not exist previously, they are created

        EXAMPLES::

            sage: S2 = Manifold(2, 'S^2', structure='top', start_index=1)
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS,
            ....:                                   (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                                   intersection_name='W',
            ....:                                   restrictions1= x^2+y^2!=0,
            ....:                                   restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[y,0]])
            sage: fN = phi_U.frame(); fS = phi_V.frame() # get induced frames
            sage: s = E.section(name='s')
            sage: s.set_comp(fS)
            1-index components w.r.t. Trivialization frame (E|_V, ((phi_V^*e_1),(phi_V^*e_2)))
            sage: s.set_comp(fS)[1] = u+v
            sage: s.display(fS)
            s = (u + v) (phi_V^*e_1)

        Setting the components in a new frame (``e``)::

            sage: e = E.local_frame('e', domain=V)
            sage: s.set_comp(e)
            1-index components w.r.t. Local frame (E|_V, (e_1,e_2))
            sage: s.set_comp(e)[1] = u*v
            sage: s.display(e)
            s = u*v e_1

        Since the frames ``e`` and ``fS`` are defined on the same domain, the
        components w.r.t. ``fS`` have been erased::

            sage: s.display(phi_V.frame())
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components in
             the Trivialization frame (E|_V, ((phi_V^*e_1),(phi_V^*e_2)))
        """
    def add_comp(self, basis=None):
        """
        Return the components of ``self`` in a given local frame for assignment.

        The components with respect to other frames having the same domain
        as the provided local frame are kept. To delete them, use the
        method :meth:`set_comp` instead.

        INPUT:

        - ``basis`` -- (default: ``None``) local frame in which the
          components are defined; if ``None``, the components are assumed
          to refer to the section domain's default frame

        OUTPUT:

        - components in the given frame, as a
          :class:`~sage.tensor.modules.comp.Components`; if such
          components did not exist previously, they are created

        EXAMPLES::

            sage: S2 = Manifold(2, 'S^2', structure='top', start_index=1)
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS, (x/(x^2+y^2), y/(x^2+y^2)),
            ....:               intersection_name='W', restrictions1= x^2+y^2!=0,
            ....:               restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,1],[1,0]])
            sage: fN = phi_U.frame(); fS = phi_V.frame() # get induced frames
            sage: s = E.section(name='s')
            sage: s.add_comp(fS)
            1-index components w.r.t. Trivialization frame (E|_V, ((phi_V^*e_1),(phi_V^*e_2)))
            sage: s.add_comp(fS)[1] = u+v
            sage: s.display(fS)
            s = (u + v) (phi_V^*e_1)

        Setting the components in a new frame::

            sage: e = E.local_frame('e', domain=V)
            sage: s.add_comp(e)
            1-index components w.r.t. Local frame (E|_V, (e_1,e_2))
            sage: s.add_comp(e)[1] = u*v
            sage: s.display(e)
            s = u*v e_1

        The components with respect to ``fS`` are kept::

            sage: s.display(fS)
            s = (u + v) (phi_V^*e_1)
        """
    def add_comp_by_continuation(self, frame, subdomain, chart=None) -> None:
        """
        Set components with respect to a local frame by continuation of the
        coordinate expression of the components in a subframe.

        The continuation is performed by demanding that the components have
        the same coordinate expression as those on the restriction of the
        frame to a given subdomain.

        INPUT:

        - ``frame`` -- local frame `e` in which the components are to be set
        - ``subdomain`` -- open subset of `e`'s domain in which the
          components are known or can be evaluated from other components
        - ``chart`` -- (default: ``None``) coordinate chart on `e`'s domain in
          which the extension of the expression of the components is to be
          performed; if ``None``, the default's chart of `e`'s domain is
          assumed

        EXAMPLES:

        Components of a vector field on the sphere `S^2`::

            sage: S2 = Manifold(2, 'S^2', structure='top', start_index=1)
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS,
            ....:                                   (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                                   intersection_name='W',
            ....:                                   restrictions1= x^2+y^2!=0,
            ....:                                   restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,1],[1,0]])
            sage: fN = phi_U.frame(); fS = phi_V.frame() # get induced frames
            sage: a = E.section({fN: [x, 2+y]}, name='a')

        At this stage, the section has been defined only on the open subset
        ``U`` (through its components in the frame ``fN``)::

            sage: a.display(fN)
            a = x (phi_U^*e_1) + (y + 2) (phi_U^*e_2)

        The components with respect to the restriction of ``fS`` to the common
        subdomain ``W``, in terms of the ``(u,v)`` coordinates, are obtained
        by a change-of-frame formula on ``W``::

            sage: a.display(fS.restrict(W), stereoS.restrict(W))
            a = (2*u^2 + 2*v^2 + v)/(u^2 + v^2) (phi_V^*e_1) + u/(u^2 + v^2)
             (phi_V^*e_2)

        The continuation consists in extending the definition of the vector
        field to the whole open subset ``V`` by demanding that the components
        in the frame eV have the same coordinate expression as the above one::

            sage: a.add_comp_by_continuation(fS, W, chart=stereoS)

        We have then::

            sage: a.display(fS)
            a = (2*u^2 + 2*v^2 + v)/(u^2 + v^2) (phi_V^*e_1) + u/(u^2 + v^2)
             (phi_V^*e_2)

        and `a` is defined on the entire manifold `S^2`.
        """
    def add_expr_from_subdomain(self, frame, subdomain) -> None:
        """
        Add an expression to an existing component from a subdomain.

        INPUT:

        - ``frame`` -- local frame `e` in which the components are to be set
        - ``subdomain`` -- open subset of `e`'s domain in which the
          components have additional expressions

        EXAMPLES:

        We are going to consider a section on the trivial rank 2 vector bundle
        over the 2-sphere::

            sage: S2 = Manifold(2, 'S^2', structure='top', start_index=1)
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS,
            ....:              (x/(x^2+y^2), y/(x^2+y^2)),
            ....:              intersection_name='W', restrictions1= x^2+y^2!=0,
            ....:              restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E') # define vector bundle
            sage: e = E.local_frame('e') # frame to trivialize E
            sage: eU = e.restrict(U); eV = e.restrict(V); eW = e.restrict(W) # this step is essential since U, V and W must be trivial

        To define a section ``s`` on `S^2`, we first set the components on
        ``U``::

            sage: s = E.section(name='s')
            sage: sU = s.restrict(U)
            sage: sU[:] = [x, y]

        But because ``E`` is trivial, these components can be extended with
        respect to the global frame ``e`` onto `S^2`::

            sage: s.add_comp_by_continuation(e, U)

        One can see that ``s`` is not yet fully defined: the components
        (scalar fields) do not have values on the whole manifold::

            sage: sorted(s._components.values())[0]._comp[(1,)].display()
            S^2 → ℝ
            on U: (x, y) ↦ x
            on W: (u, v) ↦ u/(u^2 + v^2)

        To fix that, we extend the components from ``W`` to ``V`` first, using
        :meth:`add_comp_by_continuation`::

            sage: s.add_comp_by_continuation(eV, W, stereoS)

        Then, the expression on the subdomain ``V`` is added to the
        components on `S^2` already known by::

            sage: s.add_expr_from_subdomain(e, V)

        The definition of ``s`` is now complete::

            sage: sorted(s._components.values())[0]._comp[(2,)].display()
            S^2 → ℝ
            on U: (x, y) ↦ y
            on V: (u, v) ↦ v/(u^2 + v^2)
        """
    def comp(self, basis=None, from_basis=None):
        """
        Return the components in a given local frame.

        If the components are not known already, they are computed by the
        change-of-basis formula from components in another local frame.

        INPUT:

        - ``basis`` -- (default: ``None``) local frame in which the components
          are required; if none is provided, the components are assumed to
          refer to the section module's default frame on the corresponding
          domain
        - ``from_basis`` -- (default: ``None``) local frame from which the
          required components are computed, via the change-of-basis
          formula, if they are not known already in the basis ``basis``

        OUTPUT:

        - components in the local frame ``basis``, as a
          :class:`~sage.tensor.modules.comp.Components`

        EXAMPLES:

        Components of a section defined on a rank 2 vector bundle over two
        open subsets::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x, y> = M.chart()
            sage: U = M.open_subset('U'); V = M.open_subset('V')
            sage: M.declare_union(U, V)
            sage: XU = X.restrict(U); XV = X.restrict(V)
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e', domain=U); e
            Local frame (E|_U, (e_0,e_1))
            sage: f = E.local_frame('f', domain=V); f
            Local frame (E|_V, (f_0,f_1))
            sage: s = E.section(name='s')
            sage: s[e,:] = - x + y^3, 2+x
            sage: s[f,0] = x^2
            sage: s[f,1] = x+y
            sage: s.comp(e)
            1-index components w.r.t. Local frame (E|_U, (e_0,e_1))
            sage: s.comp(e)[:]
            [y^3 - x, x + 2]
            sage: s.comp(f)
            1-index components w.r.t. Local frame (E|_V, (f_0,f_1))
            sage: s.comp(f)[:]
            [x^2, x + y]

        Since ``e`` is the default frame of ``E|_U``, the argument ``e`` can
        be omitted after restricting::

            sage: e is E.section_module(domain=U).default_frame()
            True
            sage: s.restrict(U).comp() is s.comp(e)
            True
        """
    def display(self, frame=None, chart=None):
        """
        Display the section in terms of its expansion with respect to a given
        local frame.

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        INPUT:

        - ``frame`` -- (default: ``None``) local frame with respect to
          which the section is expanded; if ``frame`` is ``None`` and ``chart``
          is not ``None``, the default frame in the corresponding section module
          is assumed
        - ``chart`` -- (default: ``None``) chart with respect to which the
          components of the section in the selected frame are expressed;
          if ``None``, the default chart of the local frame domain is assumed

        EXAMPLES:

        Display of section on a rank 2 vector bundle over the 2-sphere::

            sage: S2 = Manifold(2, 'S^2', structure='top', start_index=1)
            sage: U = S2.open_subset('U') ; V = S2.open_subset('V') # complement of the North and South pole, respectively
            sage: S2.declare_union(U,V)
            sage: stereoN.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: stereoS.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: xy_to_uv = stereoN.transition_map(stereoS,
            ....:                                   (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                                   intersection_name='W',
            ....:                                   restrictions1= x^2+y^2!=0,
            ....:                                   restrictions2= u^2+v^2!=0)
            sage: W = U.intersection(V)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: E = S2.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,1],[1,0]])
            sage: fN = phi_U.frame(); fS = phi_V.frame() # get induced frames
            sage: s = E.section(name='s')
            sage: s[fN,:] = [x, y]
            sage: s.add_comp_by_continuation(fS, W, stereoS)
            sage: s.display(fN)
            s = x (phi_U^*e_1) + y (phi_U^*e_2)
            sage: s.display(fS)
            s = v/(u^2 + v^2) (phi_V^*e_1) + u/(u^2 + v^2) (phi_V^*e_2)

        Since ``fN`` is the default frame on ``E|_U``, the argument ``fN`` can
        be omitted after restricting::

            sage: fN is E.section_module(domain=U).default_frame()
            True
            sage: s.restrict(U).display()
            s = x (phi_U^*e_1) + y (phi_U^*e_2)

        Similarly, since ``fS`` is ``V``'s default frame, the argument ``fS``
        can be omitted when considering the restriction of ``s`` to ``V``::

            sage: s.restrict(V).display()
            s = v/(u^2 + v^2) (phi_V^*e_1) + u/(u^2 + v^2) (phi_V^*e_2)

        The second argument comes into play whenever the frame's domain is
        covered by two distinct charts. Since ``stereoN.restrict(W)`` is the
        default chart on ``W``, the second argument can be omitted for the
        expression in this chart::

            sage: s.display(fS.restrict(W))
            s = y (phi_V^*e_1) + x (phi_V^*e_2)

        To get the expression in the other chart, the second argument must be
        used::

            sage: s.display(fN.restrict(W), stereoS.restrict(W))
            s = u/(u^2 + v^2) (phi_U^*e_1) + v/(u^2 + v^2) (phi_U^*e_2)

        One can ask for the display with respect to a frame in which ``s`` has
        not been initialized yet (this will automatically trigger the use of
        the change-of-frame formula for tensors)::

            sage: a = E.section_module(domain=U).automorphism()
            sage: a[:] = [[1+x^2,0],[0,1+y^2]]
            sage: e = fN.new_frame(a, 'e')
            sage: [e[i].display() for i in S2.irange()]
            [e_1 = (x^2 + 1) (phi_U^*e_1), e_2 = (y^2 + 1) (phi_U^*e_2)]
            sage: s.display(e)
            s = x/(x^2 + 1) e_1 + y/(y^2 + 1) e_2

        A shortcut of ``display()`` is ``disp()``::

            sage: s.disp(fS)
            s = v/(u^2 + v^2) (phi_V^*e_1) + u/(u^2 + v^2) (phi_V^*e_2)
        """
    disp = display
    def display_comp(self, frame=None, chart=None, only_nonzero: bool = True):
        """
        Display the section components with respect to a given frame,
        one per line.

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        INPUT:

        - ``frame`` -- (default: ``None``) local frame with respect to which
          the section components are defined; if ``None``, then the default
          frame on the section module is used
        - ``chart`` -- (default: ``None``) chart specifying the coordinate
          expression of the components; if ``None``, the default chart of the
          section domain is used
        - ``only_nonzero`` -- boolean (default: ``True``); if ``True``, only
          nonzero components are displayed

        EXAMPLES:

        Display of the components of a section defined on two open subsets::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: c_xy.<x, y> = U.chart()
            sage: V = M.open_subset('V')
            sage: c_uv.<u, v> = V.chart()
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e', domain=U)
            sage: f = E.local_frame('f', domain=V)
            sage: s = E.section(name='s')
            sage: s[e,0] = - x + y^3
            sage: s[e,1] = 2+x
            sage: s[f,1] = - u*v
            sage: s.display_comp(e)
            s^0 = y^3 - x
            s^1 = x + 2
            sage: s.display_comp(f)
            s^1 = -u*v

        See documentation of
        :meth:`sage.manifolds.section.TrivialSection.display_comp`
        for more options.
        """
    def at(self, point):
        """
        Value of ``self`` at a point of its domain.

        If the current section is

        .. MATH::

            s:\\ U  \\longrightarrow E ,

        then for any point `p \\in U`, `s(p)` is a vector in the fiber `E_p` of
        `E` at `p`.

        INPUT:

        - ``point`` -- :class:`~sage.manifolds.point.ManifoldPoint`;
          point `p` in the domain of the section `U`

        OUTPUT:

        - :class:`~sage.manifolds.vector_bundle_fiber_element.VectorBundleFiberElement`
          representing the vector `s(p)` in the fiber `E_p` of `E` at `p`.

        EXAMPLES:

        Vector on a rank 2 vector bundle fiber over a non-parallelizable
        2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: transf = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: inv = transf.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame() # get induced frames
            sage: s = E.section({fU: [1+y, x]}, name='s')
            sage: s.add_comp_by_continuation(fV, W, chart=c_uv)
            sage: s.display(fU)
            s = (y + 1) (phi_U^*e_1) + x (phi_U^*e_2)
            sage: s.display(fV)
            s = (1/4*u^2 + 1/2*u*v + 1/4*v^2) (phi_V^*e_1) + (1/4*u^2 - 1/4*v^2
             + 1/2*u + 1/2*v) (phi_V^*e_2)
            sage: p = M.point((2,3), chart=c_xy, name='p')
            sage: sp = s.at(p) ; sp
            Vector s in the fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: sp.parent()
            Fiber of E at Point p on the 2-dimensional topological manifold M
            sage: sp.display(fU.at(p))
            s = 4 (phi_U^*e_1) + 2 (phi_U^*e_2)
            sage: sp.display(fV.at(p))
            s = 4 (phi_V^*e_1) + 8 (phi_V^*e_2)
            sage: p.coord(c_uv) # to check the above expression
            (5, -1)
        """
    def __getitem__(self, args):
        """
        Return a component with respect to some frame.

        INPUT:

        - ``args`` -- list of indices defining the component; if ``[:]`` is
          provided, all the components are returned

        The frame can be passed as the first item of ``args``. If not, the
        default frame of the corresponding section module is assumed.

        TESTS::

            sage: M = Manifold(3, 'M', structure='top') # the 2-dimensional sphere S^3
            sage: U = M.open_subset('U') # complement of the North pole
            sage: c_xyz.<x,y,z> = U.chart() # stereographic coordinates from the North pole
            sage: V = M.open_subset('V') # complement of the South pole
            sage: c_uvt.<u,v,t> = V.chart() # stereographic coordinates from the South pole
            sage: M.declare_union(U,V)   # S^3 is the union of U and V
            sage: E = M.vector_bundle(3, 'E')
            sage: e = E.local_frame('e')
            sage: s = E.section(name='s')
            sage: s[e, :] = [x+y, -2*z, 3*y^2]
            sage: s.__getitem__(1)
            -2*z
            sage: s.__getitem__(2)
            3*y^2
            sage: s.__getitem__((e,1))
            -2*z
            sage: s.__getitem__((e, 1, c_xyz))
            -2*z
            sage: s.__getitem__(slice(None))
            [x + y, -2*z, 3*y^2]
            sage: s.__getitem__((e,slice(None)))
            [x + y, -2*z, 3*y^2]
            sage: s.__getitem__((e,[slice(None)]))
            [Scalar field on the 3-dimensional topological manifold M,
             Scalar field on the 3-dimensional topological manifold M,
             Scalar field on the 3-dimensional topological manifold M]
        """
    def __setitem__(self, args, value) -> None:
        """
        Set a component with respect to some local frame.

        INPUT:

        - ``args`` -- list of indices; if ``[:]`` is provided, all the
          components are set; the frame can be passed as the first item
          of ``args``; if not, the default frame of the corresponding section
          module is assumed
        - ``value`` -- the value to be set or a list of values if
          ``args = [:]``

        TESTS::

            sage: M = Manifold(3, 'M', structure='top') # the 3-dimensional sphere S^3
            sage: U = M.open_subset('U') # complement of the North pole
            sage: c_xyz.<x,y,z> = U.chart() # stereographic coordinates from the North pole
            sage: V = M.open_subset('V') # complement of the South pole
            sage: c_uvt.<u,v,t> = V.chart() # stereographic coordinates from the South pole
            sage: M.declare_union(U,V)   # S^3 is the union of U and V
            sage: E = M.vector_bundle(3, 'E')
            sage: e = E.local_frame('e')
            sage: s = E.section(name='s')
            sage: s.__setitem__((e, 0), x+y^2)
            sage: s.display(e)
            s = (y^2 + x) e_0
            sage: s.__setitem__(0, x+y^2)  # same as above since e is the default frame on E
            sage: s.display()
            s = (y^2 + x) e_0
            sage: s.__setitem__(slice(None), [x+y, 3*y^2, x*y])
            sage: s.display()
            s = (x + y) e_0 + 3*y^2 e_1 + x*y e_2
        """
    def copy_from(self, other) -> None:
        """
        Make ``self`` a copy of ``other``.

        INPUT:

        - ``other`` -- other section, in the same module as ``self``

        .. NOTE::

            While the derived quantities are not copied, the name is kept.

        .. WARNING::

            All previous defined components and restrictions will be deleted!

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame()
            sage: s = E.section(name='s')
            sage: s[fU,:] = [2, 1-y]
            sage: s.add_comp_by_continuation(fV, U.intersection(V), c_uv)
            sage: t = E.section(name='t')
            sage: t.copy_from(s)
            sage: t.display(fU)
            t = 2 (phi_U^*e_1) + (-y + 1) (phi_U^*e_2)
            sage: s == t
            True

        If the original section is modified, the copy is not::

            sage: s[fU,0] = -1
            sage: s.display(fU)
            s = -(phi_U^*e_1) + (-y + 1) (phi_U^*e_2)
            sage: t.display(fU)
            t = 2 (phi_U^*e_1) + (-y + 1) (phi_U^*e_2)
            sage: s == t
            False
        """
    def copy(self, name=None, latex_name=None):
        """
        Return an exact copy of ``self``.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the copy
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          copy; if none is provided, the LaTeX symbol is set to ``name``

        .. NOTE::

            The name and the derived quantities are not copied.

        EXAMPLES:

        Copy of a section on a rank 2 vector bundle over a 2-dimensional
        manifold::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame()
            sage: s = E.section(name='s')
            sage: s[fU,:] = [2, 1-y]
            sage: s.add_comp_by_continuation(fV, U.intersection(V), c_uv)
            sage: t = s.copy(); t
            Section on the 2-dimensional topological manifold M with values in
             the real vector bundle E of rank 2
            sage: t.display(fU)
            2 (phi_U^*e_1) + (-y + 1) (phi_U^*e_2)
            sage: t == s
            True

        If the original section is modified, the copy is not::

            sage: s[fU,0] = -1
            sage: s.display(fU)
            s = -(phi_U^*e_1) + (-y + 1) (phi_U^*e_2)
            sage: t.display(fU)
            2 (phi_U^*e_1) + (-y + 1) (phi_U^*e_2)
            sage: t == s
            False
        """
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- a section or 0

        OUTPUT: ``True`` if ``self`` is equal to ``other`` and ``False`` otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame()
            sage: s = E.section(name='s')
            sage: s[fU,:] = [x+y, 0]
            sage: s.add_comp_by_continuation(fV, U.intersection(V), c_uv)
            sage: s == s
            True
            sage: s == s.copy()
            True
            sage: t = E.section(name='t')
            sage: t.set_restriction(s.restrict(U))
            sage: s == t  # False since t has not been defined on V
            False
            sage: t.set_restriction(s.restrict(V))
            sage: s == t  # True now
            True
            sage: t[fU, 0] = -1
            sage: s == t  # False since a has been reset on U (domain of fU)
            False
            sage: s.parent().zero() == 0
            True
        """
    def __ne__(self, other):
        """
        Inequality operator.

        INPUT:

        - ``other`` -- section or 0

        OUTPUT:

        - ``True`` if ``self`` is different from ``other`` and ``False``
          otherwise

        TESTS::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame()
            sage: s = E.section(name='s')
            sage: s[fU,:] = [x+y, 0]
            sage: s.add_comp_by_continuation(fV, U.intersection(V), c_uv)
            sage: s != s
            False
            sage: s != s.copy()
            False
            sage: s != 0
            True
        """
    def __pos__(self):
        """
        Unary plus operator.

        OUTPUT: an exact copy of ``self``

        TESTS::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame()
            sage: s = E.section(name='s')
            sage: s[fU,:] = [x, 1]
            sage: s.add_comp_by_continuation(fV, U.intersection(V), c_uv)
            sage: t = s.__pos__(); t
            Section +s on the 2-dimensional topological manifold M with values
             in the real vector bundle E of rank 2
            sage: t.display(fU)
            +s = x (phi_U^*e_1) + (phi_U^*e_2)
        """
    def __neg__(self):
        """
        Unary minus operator.

        OUTPUT: the tensor field `-T`, where `T` is ``self``

        TESTS::

            sage: M = Manifold(2, 'M', structure='top')
            sage: U = M.open_subset('U') ; V = M.open_subset('V')
            sage: M.declare_union(U,V)   # M is the union of U and V
            sage: c_xy.<x,y> = U.chart() ; c_uv.<u,v> = V.chart()
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x+y, x-y),
            ....:                    intersection_name='W', restrictions1= x>0,
            ....:                    restrictions2= u+v>0)
            sage: uv_to_xy = xy_to_uv.inverse()
            sage: W = U.intersection(V)
            sage: E = M.vector_bundle(2, 'E') # define vector bundle
            sage: phi_U = E.trivialization('phi_U', domain=U) # define trivializations
            sage: phi_V = E.trivialization('phi_V', domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[0,x],[x,0]])
            sage: fU = phi_U.frame(); fV = phi_V.frame()
            sage: s = E.section(name='s')
            sage: s[fU,:] = [x, 1]
            sage: s.add_comp_by_continuation(fV, U.intersection(V), c_uv)
            sage: s.display(fU)
            s = x (phi_U^*e_1) + (phi_U^*e_2)
            sage: s.display(fV)
            s = (1/2*u + 1/2*v) (phi_V^*e_1) + (1/4*u^2 + 1/2*u*v + 1/4*v^2) (phi_V^*e_2)
            sage: t = s.__neg__(); t
            Section -s on the 2-dimensional topological manifold M with values
             in the real vector bundle E of rank 2
            sage: t.display(fU)
            -s = -x (phi_U^*e_1) - (phi_U^*e_2)
            sage: t.display(fV)
            -s = (-1/2*u - 1/2*v) (phi_V^*e_1) + (-1/4*u^2 - 1/2*u*v - 1/4*v^2) (phi_V^*e_2)
            sage: s == -t  # indirect doctest
            True
        """
    def set_immutable(self) -> None:
        """
        Set ``self`` and all restrictions of ``self`` immutable.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: U = M.open_subset('U', coord_def={X: x^2+y^2<1})
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: s = E.section([1+y,x], name='s')
            sage: sU = s.restrict(U)
            sage: s.set_immutable()
            sage: s.is_immutable()
            True
            sage: sU.is_immutable()
            True
        """

class TrivialSection(FiniteRankFreeModuleElement, Section):
    """
    Section in a trivial vector bundle.

    An instance of this class is a section in a vector bundle `E \\to M` of class
    `C^k`, where `E|_U` is manifestly trivial. More precisely, a *(local)
    section* on a subset `U \\in M` is a map of class `C^k`

    .. MATH::

        s: U \\longrightarrow E

    such that

    .. MATH::

        \\forall p \\in U,\\ s(p) \\in E_p

    where `E_p` denotes the vector bundle fiber of `E` over the point `p \\in U`.
    `E` being trivial means `E` being homeomorphic to `E \\times F`, for `F` is
    the typical fiber of `E`, namely the underlying topological vector space. By
    this means, `s` can be seen as a map of class `C^k(U;E)`

    .. MATH::

        s: U \\longrightarrow F ,

    so that the set of all sections `C^k(U;E)` becomes a *free* module over the
    algebra of scalar fields on `U`.

    .. NOTE::

        If `E|_U` is not manifestly trivial, the class
        :class:`~sage.manifolds.section.Section` should be used instead.

    This is a Sage *element* class, the corresponding *parent* class being
    :class:`~sage.manifolds.section_module.SectionFreeModule`.

    INPUT:

    - ``section_module`` -- free module `C^k(U;E)` of sections on `E` over `U`
      (cf. :class:`~sage.manifolds.section_module.SectionFreeModule`)
    - ``name`` -- (default: ``None``) name given to the section
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the section;
      if none is provided, the LaTeX symbol is set to ``name``

    EXAMPLES:

    A section on a trivial rank 3 vector bundle over the 3-sphere::

        sage: M = Manifold(3, 'S^3', structure='top')
        sage: U = M.open_subset('U') ; V = M.open_subset('V') # complement of the North and South pole, respectively
        sage: M.declare_union(U,V)
        sage: stereoN.<x,y,z> = U.chart() # stereographic coordinates from the North pole
        sage: stereoS.<u,v,t> = V.chart() # stereographic coordinates from the South pole
        sage: xyz_to_uvt = stereoN.transition_map(stereoS,
        ....:           (x/(x^2+y^2+z^2), y/(x^2+y^2+z^2), z/(x^2+y^2+z^2)),
        ....:           intersection_name='W',
        ....:           restrictions1= x^2+y^2+z^2!=0,
        ....:           restrictions2= u^2+v^2+t^2!=0)
        sage: W = U.intersection(V)
        sage: uvt_to_xyz = xyz_to_uvt.inverse()
        sage: E = M.vector_bundle(3, 'E')
        sage: e = E.local_frame('e') # Trivializes E
        sage: s = E.section(name='s'); s
        Section s on the 3-dimensional topological manifold S^3 with values in
         the real vector bundle E of rank 3
        sage: s[e,:] = z^2, x-y, 1-x
        sage: s.display()
        s = z^2 e_0 + (x - y) e_1 + (-x + 1) e_2

    Since `E` is trivial, `s` is now element of a free section module::

        sage: s.parent()
        Free module C^0(S^3;E) of sections on the 3-dimensional topological
         manifold S^3 with values in the real vector bundle E of rank 3
        sage: isinstance(s.parent(), FiniteRankFreeModule)
        True
    """
    def __init__(self, section_module, name=None, latex_name=None) -> None:
        """
        Construct a section on a trivial vector bundle.

        TESTS:

        Construction via ``parent.element_class``, and not via a direct call
        to ``TrivialSection``, to fit with the category framework::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: C0 = E.section_module()
            sage: s = C0.element_class(C0, name='s'); s
            Section s on the 2-dimensional topological manifold M with values in
             the real vector bundle E of rank 2
            sage: s[:] = [1+x^2, x*y]
            sage: s.display()
            s = (x^2 + 1) e_0 + x*y e_1
            sage: s.parent()
            Free module C^0(M;E) of sections on the 2-dimensional topological
             manifold M with values in the real vector bundle E of rank 2
            sage: TestSuite(s).run()
        """
    def set_comp(self, basis=None):
        """
        Return the components of the section in a given local frame for
        assignment.

        The components with respect to other frames on the same domain are
        deleted, in order to avoid any inconsistency. To keep them, use the
        method :meth:`add_comp` instead.

        INPUT:

        - ``basis`` -- (default: ``None``) local frame in which the
          components are defined; if none is provided, the components are
          assumed to refer to the section module's default frame

        OUTPUT:

        - components in the given frame, as an instance of the
          class :class:`~sage.tensor.modules.comp.Components`; if such
          components did not exist previously, they are created

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # makes E trivial
            sage: s = E.section(name='s')
            sage: s.set_comp(e)
            1-index components w.r.t. Local frame (E|_M, (e_0,e_1))
            sage: s.set_comp(e)[0] = 2
            sage: s.display(e)
            s = 2 e_0

        Setting components in a new frame (``f``)::

            sage: f = E.local_frame('f')
            sage: s.set_comp(f)
            1-index components w.r.t. Local frame (E|_M, (f_0,f_1))
            sage: s.set_comp(f)[0] = x
            sage: s.display(f)
            s = x f_0

        The components with respect to the frame ``e`` have be erased::

            sage: s.display(e)
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components
             in the Local frame (E|_M, (e_0,e_1))

        Setting components in a frame defined on a subdomain deletes
        previously defined components as well::

            sage: U = M.open_subset('U', coord_def={X: x>0})
            sage: g = E.local_frame('g', domain=U)
            sage: s.set_comp(g)
            1-index components w.r.t. Local frame (E|_U, (g_0,g_1))
            sage: s.set_comp(g)[0] = 1+y
            sage: s.display(g)
            s = (y + 1) g_0
            sage: s.display(f)
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components
             in the Local frame (E|_M, (f_0,f_1))
        """
    def add_comp(self, basis=None):
        """
        Return the components of the section in a given local frame for
        assignment.

        The components with respect to other frames on the same domain are
        kept. To delete them, use the method :meth:`set_comp` instead.

        INPUT:

        - ``basis`` -- (default: ``None``) local frame in which the
          components are defined; if none is provided, the components are
          assumed to refer to the section module's default frame

        OUTPUT:

        - components in the given frame, as an instance of the
          class :class:`~sage.tensor.modules.comp.Components`; if such
          components did not exist previously, they are created

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # makes E trivial
            sage: s = E.section(name='s')
            sage: s.add_comp(e)
            1-index components w.r.t. Local frame (E|_M, (e_0,e_1))
            sage: s.add_comp(e)[0] = 2
            sage: s.display(e)
            s = 2 e_0

        Adding components with respect to a new frame (``f``)::

            sage: f = E.local_frame('f')
            sage: s.add_comp(f)
            1-index components w.r.t. Local frame (E|_M, (f_0,f_1))
            sage: s.add_comp(f)[0] = x
            sage: s.display(f)
            s = x f_0

        The components with respect to the frame ``e`` are kept::

            sage: s.display(e)
            s = 2 e_0

        Adding components in a frame defined on a subdomain::

            sage: U = M.open_subset('U', coord_def={X: x>0})
            sage: g = E.local_frame('g', domain=U)
            sage: s.add_comp(g)
            1-index components w.r.t. Local frame (E|_U, (g_0,g_1))
            sage: s.add_comp(g)[0] = 1+y
            sage: s.display(g)
            s = (y + 1) g_0

        The components previously defined are kept::

            sage: s.display(e)
            s = 2 e_0
            sage: s.display(f)
            s = x f_0
        """
    def comp(self, basis=None, from_basis=None):
        """
        Return the components in a given local frame.

        If the components are not known already, they are computed by the
        tensor change-of-basis formula from components in another local frame.

        INPUT:

        - ``basis`` -- (default: ``None``) local frame in which the components
          are required; if none is provided, the components are assumed to
          refer to the section module's default frame
        - ``from_basis`` -- (default: ``None``) local frame from which the
          required components are computed, via the tensor change-of-basis
          formula, if they are not known already in the basis ``basis``

        OUTPUT:

        - components in the local frame ``basis``, as an instance of the
          class :class:`~sage.tensor.modules.comp.Components`

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # makes E trivial
            sage: s = E.section(name='s')
            sage: s[1] = x*y
            sage: s.comp(e)
            1-index components w.r.t. Local frame (E|_M, (e_1,e_2))
            sage: s.comp()  # the default frame is e
            1-index components w.r.t. Local frame (E|_M, (e_1,e_2))
            sage: s.comp()[:]
            [x*y, 0]
            sage: f = E.local_frame('f')
            sage: s[f, 1] = x-3
            sage: s.comp(f)
            1-index components w.r.t. Local frame (E|_M, (f_1,f_2))
            sage: s.comp(f)[:]
            [x - 3, 0]
        """
    def restrict(self, subdomain):
        """
        Return the restriction of ``self`` to some subdomain.

        If the restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` --
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
          open subset `U` of the section module domain `S`

        OUTPUT: instance of :class:`TrivialSection` representing the restriction

        EXAMPLES:

        Restriction of a section defined over `\\RR^2` to a disk::

            sage: M = Manifold(2, 'R^2')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # makes E trivial
            sage: s = E.section(x+y, -1+x^2, name='s')
            sage: D = M.open_subset('D') # the unit open disc
            sage: e_D = e.restrict(D)
            sage: c_cart_D = c_cart.restrict(D, x^2+y^2<1)
            sage: s_D = s.restrict(D) ; s_D
            Section s on the Open subset D of the 2-dimensional differentiable
             manifold R^2 with values in the real vector bundle E of rank 2
            sage: s_D.display(e_D)
            s = (x + y) e_0 + (x^2 - 1) e_1

        The symbolic expressions of the components with respect to
        Cartesian coordinates are equal::

            sage: bool( s_D[1].expr() == s[1].expr() )
            True

        but neither the chart functions representing the components (they are
        defined on different charts)::

            sage: s_D[1] == s[1]
            False

        nor the scalar fields representing the components (they are
        defined on different open subsets)::

            sage: s_D[[1]] == s[[1]]
            False

        The restriction of the section to its own domain is of course itself::

            sage: s.restrict(M) is s
            True
        """
    def display_comp(self, frame=None, chart=None, only_nonzero: bool = False):
        """
        Display the section components with respect to a given frame, one per
        line.

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        INPUT:

        - ``frame`` -- (default: ``None``) local frame with respect to which
          the section components are defined; if ``None``, then the default
          basis of the section module on which the section is defined is used
        - ``chart`` -- (default: ``None``) chart specifying the coordinate
          expression of the components; if ``None``, the default chart of the
          section module domain is used
        - ``only_nonzero`` -- boolean (default: ``False``); if ``True``, only
          nonzero components are displayed

        EXAMPLES:

        Display of the components of a section on a rank 4 vector bundle over
        a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(3, 'E')
            sage: e = E.local_frame('e') # makes E trivial
            sage: s = E.section(name='s')
            sage: s[0], s[2] = x+y, x*y
            sage: s.display_comp()
            s^0 = x + y
            s^1 = 0
            s^2 = x*y

        By default, the vanishing components are displayed, too;
        to see only non-vanishing components, the argument ``only_nonzero`` must
        be set to ``True``::

            sage: s.display_comp(only_nonzero=True)
            s^0 = x + y
            s^2 = x*y

        Display in a frame different from the default one::

            sage: a = E.section_module().automorphism()
            sage: a[:] = [[1+y^2, 0, 0], [0, 2+x^2, 0], [0, 0, 1]]
            sage: f = e.new_frame(a, 'f')
            sage: s.display_comp(frame=f)
            s^0 = (x + y)/(y^2 + 1)
            s^1 = 0
            s^2 = x*y

        Display with respect to a chart different from the default one::

            sage: Y.<u,v> = M.chart()
            sage: X_to_Y = X.transition_map(Y, [x+y, x-y])
            sage: Y_to_X = X_to_Y.inverse()
            sage: s.display_comp(chart=Y)
            s^0 = u
            s^1 = 0
            s^2 = 1/4*u^2 - 1/4*v^2

        Display of the components with respect to a specific frame, expressed
        in terms of a specific chart::

            sage: s.display_comp(frame=f, chart=Y)
            s^0 = 4*u/(u^2 - 2*u*v + v^2 + 4)
            s^1 = 0
            s^2 = 1/4*u^2 - 1/4*v^2
        """
    def at(self, point):
        """
        Value of ``self`` at a point of its domain.

        If the current section is

        .. MATH::

            s:\\ U  \\longrightarrow E ,

        then for any point `p\\in U`, `s(p)` is
        a vector in the fiber `E_p` of `E` at the point `p \\in U`.

        INPUT:

        - ``point`` -- :class:`~sage.manifolds.point.ManifoldPoint`
          point `p` in the domain of the section `U`

        OUTPUT:

        - :class:`~sage.tensor.modules.free_module_tensor.FreeModuleTensor`
          representing the vector `s(p)` in the vector space `E_p`

        EXAMPLES:

        Vector in a tangent space of a 2-dimensional manifold::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: p = M.point((-2,3), name='p')
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # makes E trivial
            sage: s = E.section(y, x^2, name='s')
            sage: s.display()
            s = y e_0 + x^2 e_1
            sage: sp = s.at(p) ; sp
            Vector s in the fiber of E at Point p on the 2-dimensional
             topological manifold M
            sage: sp.parent()
            Fiber of E at Point p on the 2-dimensional topological manifold M
            sage: sp.display()
            s = 3 e_0 + 4 e_1
        """
