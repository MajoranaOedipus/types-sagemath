from _typeshed import Incomplete
from sage.categories.modules import Modules as Modules
from sage.manifolds.section import Section as Section, TrivialSection as TrivialSection
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import infinity as infinity
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule as FiniteRankFreeModule

class SectionModule(UniqueRepresentation, Parent):
    """
    Module of sections over a vector bundle `E \\to M` of class `C^k` on a domain
    `U \\in M`.

    The *section module* `C^k(U;E)` is the set of all `C^k`-maps, called
    *sections*, of type

    .. MATH::

        s: U \\longrightarrow E

    such that

    .. MATH::

        \\forall p \\in U,\\ s(p) \\in E_p,

    where `E_p` is the vector bundle fiber of `E` at the point `p`.

    `C^k(U;E)` is a module over `C^k(U)`, the algebra of `C^k` scalar fields on
    `U`.

    INPUT:

    - ``vbundle`` -- vector bundle `E` on which the sections takes its values
    - ``domain`` -- (default: ``None``) subdomain `U` of the base space on which
      the sections are defined

    EXAMPLES:

    Module of sections on the Möbius bundle::

        sage: M = Manifold(1, 'RP^1', structure='top', start_index=1)
        sage: U = M.open_subset('U')  # the complement of one point
        sage: c_u.<u> =  U.chart() # [1:u] in homogeneous coord.
        sage: V = M.open_subset('V') # the complement of the point u=0
        sage: M.declare_union(U,V)   # [v:1] in homogeneous coord.
        sage: c_v.<v> = V.chart()
        sage: u_to_v = c_u.transition_map(c_v, (1/u),
        ....:                             intersection_name='W',
        ....:                             restrictions1 = u!=0,
        ....:                             restrictions2 = v!=0)
        sage: v_to_u = u_to_v.inverse()
        sage: W = U.intersection(V)
        sage: E = M.vector_bundle(1, 'E')
        sage: phi_U = E.trivialization('phi_U', latex_name=r'\\varphi_U',
        ....:                          domain=U)
        sage: phi_V = E.trivialization('phi_V', latex_name=r'\\varphi_V',
        ....:                          domain=V)
        sage: transf = phi_U.transition_map(phi_V, [[u]])
        sage: C0 = E.section_module(); C0
        Module C^0(RP^1;E) of sections on the 1-dimensional topological manifold
         RP^1 with values in the real vector bundle E of rank 1

    `C^0(\\RR P^1;E)` is a module over the algebra `C^0(\\RR P^1)`::

        sage: C0.category()
        Category of modules over Algebra of scalar fields on the 1-dimensional
         topological manifold RP^1
        sage: C0.base_ring() is M.scalar_field_algebra()
        True

    However, `C^0(\\RR P^1;E)` is not a free module::

        sage: isinstance(C0, FiniteRankFreeModule)
        False

    since the Möbius bundle is not trivial::

        sage: E.is_manifestly_trivial()
        False

    The section module over `U`, on the other hand, is a free module since
    `E|_U` admits a trivialization and therefore has a local frame::

        sage: C0_U = E.section_module(domain=U)
        sage: isinstance(C0_U, FiniteRankFreeModule)
        True

    The zero element of the module::

        sage: z = C0.zero() ; z
        Section zero on the 1-dimensional topological manifold RP^1 with values
         in the real vector bundle E of rank 1
        sage: z.display(phi_U.frame())
        zero = 0
        sage: z.display(phi_V.frame())
        zero = 0

    The module `C^0(M;E)` coerces to any module of sections defined
    on a subdomain of `M`, for instance `C^0(U;E)`::

        sage: C0_U.has_coerce_map_from(C0)
        True
        sage: C0_U.coerce_map_from(C0)
        Coercion map:
          From: Module C^0(RP^1;E) of sections on the 1-dimensional topological
           manifold RP^1 with values in the real vector bundle E of rank 1
          To:   Free module C^0(U;E) of sections on the Open subset U of the
           1-dimensional topological manifold RP^1 with values in the real vector
           bundle E of rank 1

    The conversion map is actually the restriction of sections defined
    on `M` to `U`.
    """
    Element = Section
    def __init__(self, vbundle, domain) -> None:
        """
        Construct the module of continuous sections over a vector bundle.

        TESTS::

            sage: M = Manifold(1, 'S^1', latex_name=r'S^1', start_index=1,
            ....:               structure='topological')
            sage: U = M.open_subset('U')
            sage: c_x.<x> = U.chart()
            sage: V = M.open_subset('V')
            sage: c_u.<u> = V.chart()
            sage: M.declare_union(U, V)
            sage: x_to_u = c_x.transition_map(c_u, 1/x, intersection_name='W',
            ....:                   restrictions1= x!=0, restrictions2= u!=0)
            sage: W = U.intersection(V)
            sage: u_to_x = x_to_u.inverse()
            sage: E = M.vector_bundle(1, 'E')
            sage: phi_U = E.trivialization('phi_U', latex_name=r'\\varphi_U',
            ....:                          domain=U)
            sage: phi_V = E.trivialization('phi_V', latex_name=r'\\varphi_V',
            ....:                          domain=V)
            sage: transf = phi_U.transition_map(phi_V, [[-1]])
            sage: C0 = E.section_module(); C0
            Module C^0(S^1;E) of sections on the 1-dimensional topological
             manifold S^1 with values in the real vector bundle E of rank 1
            sage: TestSuite(C0).run()
        """
    def base_space(self):
        """
        Return the base space of the sections in this module.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = U.vector_bundle(2, 'E')
            sage: C0 = E.section_module(); C0
            Module C^0(U;E) of sections on the Open subset U of the
             3-dimensional topological manifold M with values in the real vector
             bundle E of rank 2
            sage: C0.base_space()
            Open subset U of the 3-dimensional topological manifold M
        """
    def domain(self):
        """
        Return the domain of the section module.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0_U = E.section_module(domain=U); C0_U
            Module C^0(U;E) of sections on the Open subset U of the
             3-dimensional topological manifold M with values in the real vector
             bundle E of rank 2
            sage: C0_U.domain()
            Open subset U of the 3-dimensional topological manifold M
        """
    def vector_bundle(self):
        """
        Return the overlying vector bundle on which the section module is
        defined.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module(); C0
            Module C^0(M;E) of sections on the 3-dimensional topological
             manifold M with values in the real vector bundle E of rank 2
            sage: C0.vector_bundle()
            Topological real vector bundle E -> M of rank 2 over the base space
             3-dimensional topological manifold M
            sage: E is C0.vector_bundle()
            True
        """
    @cached_method
    def zero(self):
        """
        Return the zero of ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module()
            sage: z = C0.zero(); z
            Section zero on the 2-dimensional topological manifold M with values
             in the real vector bundle E of rank 2
            sage: z == 0
            True
        """
    def default_frame(self):
        """
        Return the default frame defined on ``self``.

        EXAMPLES:

        Get the default local frame of a non-trivial section module::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: V = M.open_subset('V')
            sage: M.declare_union(U, V)
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module()
            sage: e = E.local_frame('e', domain=U)
            sage: C0.default_frame()
            Local frame (E|_U, (e_0,e_1))

        The local frame is indeed the same, and not a copy::

            sage: e is C0.default_frame()
            True
        """
    def set_default_frame(self, basis) -> None:
        """
        Set the default local frame on ``self``.

        EXAMPLES:

        Set a default frame of a non-trivial section module::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: V = M.open_subset('V')
            sage: M.declare_union(U, V)
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module(); C0
            Module C^0(M;E) of sections on the 3-dimensional topological
             manifold M with values in the real vector bundle E of rank 2
            sage: e = E.local_frame('e', domain=U)
            sage: C0.set_default_frame(e)
            sage: C0.default_frame()
            Local frame (E|_U, (e_0,e_1))

        The local frame is indeed the same, and not a copy::

            sage: e is C0.default_frame()
            True

        Notice, that the local frame is defined on a subset and is not part of
        the section module `C^k(M;E)`::

            sage: C0.default_frame().domain()
            Open subset U of the 3-dimensional topological manifold M
        """

class SectionFreeModule(FiniteRankFreeModule):
    """
    Free module of sections over a vector bundle `E \\to M` of class `C^k` on a
    domain `U \\in M` which admits a trivialization or local frame.

    The *section module* `C^k(U;E)` is the set of all `C^k`-maps, called
    *sections*, of type

    .. MATH::

        s: U \\longrightarrow E

    such that

    .. MATH::

        \\forall p \\in U,\\ s(p) \\in E_p,

    where `E_p` is the vector bundle fiber of `E` at the point `p`.

    Since the domain `U` admits a local frame, the corresponding vector bundle
    `E|_U \\to U` is trivial and `C^k(U;E)` is a free module over `C^k(U)`.

    .. NOTE::

        If `E|_U` is not trivial, the class :class:`SectionModule` should be
        used instead, for `C^k(U;E)` is no longer a free module.

    INPUT:

    - ``vbundle`` -- vector bundle `E` on which the sections takes its values
    - ``domain`` -- (default: ``None``) subdomain `U` of the base space on which
      the sections are defined

    EXAMPLES:

    Module of sections on the 2-rank trivial vector bundle over the Euclidean
    plane `\\RR^2`::

        sage: M = Manifold(2, 'R^2', structure='top')
        sage: c_cart.<x,y> = M.chart()
        sage: E = M.vector_bundle(2, 'E')
        sage: e = E.local_frame('e') # Trivializes the vector bundle
        sage: C0 = E.section_module(); C0
        Free module C^0(R^2;E) of sections on the 2-dimensional topological
         manifold R^2 with values in the real vector bundle E of rank 2
        sage: C0.category()
        Category of finite dimensional modules over Algebra of scalar fields on
         the 2-dimensional topological manifold R^2
        sage: C0.base_ring() is M.scalar_field_algebra()
        True

    The vector bundle admits a global frame and is therefore trivial::

        sage: E.is_manifestly_trivial()
        True

    Since the vector bundle is trivial, its section module of global sections
    is a free module::

        sage: isinstance(C0, FiniteRankFreeModule)
        True

    Some elements are::

        sage: C0.an_element().display()
        2 e_0 + 2 e_1
        sage: C0.zero().display()
        zero = 0
        sage: s = C0([-y,x]); s
        Section on the 2-dimensional topological manifold R^2 with values in the
         real vector bundle E of rank 2
        sage: s.display()
        -y e_0 + x e_1

    The rank of the free module equals the rank of the vector bundle::

        sage: C0.rank()
        2

    The basis is given by the definition above::

        sage: C0.bases()
        [Local frame (E|_R^2, (e_0,e_1))]

    The test suite is passed as well::

        sage: TestSuite(C0).run()
    """
    Element = TrivialSection
    def __init__(self, vbundle, domain) -> None:
        """
        Construct the free module of sections over a trivial part of a vector
        bundle.

        TESTS::

            sage: M = Manifold(3, 'M', structure='top')
            sage: X.<x,y,z> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: from sage.manifolds.section_module import SectionFreeModule
            sage: C0 = SectionFreeModule(E, M); C0
            Free module C^0(M;E) of sections on the 3-dimensional topological
             manifold M with values in the real vector bundle E of rank 2
            sage: C0 is E.section_module(force_free=True)
            True
            sage: TestSuite(C0).run()
        """
    def domain(self):
        """
        Return the domain of the section module.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0_U = E.section_module(domain=U, force_free=True); C0_U
            Free module C^0(U;E) of sections on the Open subset U of the
             3-dimensional topological manifold M with values in the real vector
             bundle E of rank 2
            sage: C0_U.domain()
            Open subset U of the 3-dimensional topological manifold M
        """
    def base_space(self):
        """
        Return the base space of the sections in this module.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: U = M.open_subset('U')
            sage: E = U.vector_bundle(2, 'E')
            sage: C0 = E.section_module(force_free=True); C0
            Free module C^0(U;E) of sections on the Open subset U of the
             3-dimensional topological manifold M with values in the real
             vector bundle E of rank 2
            sage: C0.base_space()
            Open subset U of the 3-dimensional topological manifold M
        """
    def vector_bundle(self):
        """
        Return the overlying vector bundle on which the section module is
        defined.

        EXAMPLES::

            sage: M = Manifold(3, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module(force_free=True); C0
            Free module C^0(M;E) of sections on the 3-dimensional topological
             manifold M with values in the real vector bundle E of rank 2
            sage: C0.vector_bundle()
            Topological real vector bundle E -> M of rank 2 over the base space
             3-dimensional topological manifold M
            sage: E is C0.vector_bundle()
            True
        """
    def basis(self, symbol=None, latex_symbol=None, from_frame=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Define a basis of ``self``.

        A basis of the section module is actually a local frame on the
        differentiable manifold `U` over which the section module is defined.

        If the basis specified by the given symbol already exists, it is
        simply returned.
        If no argument is provided the module's default basis is returned.

        INPUT:

        - ``symbol`` -- (default: ``None``) either a string, to be used as a
          common base for the symbols of the elements of the basis, or a
          tuple of strings, representing the individual symbols of the
          elements of the basis
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the elements of the basis,
          or a tuple of strings, representing the individual LaTeX symbols
          of the elements of the basis; if ``None``, ``symbol`` is used in
          place of ``latex_symbol``
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices
          labelling the elements of the basis; if ``None``, the indices will be
          generated as integers within the range declared on ``self``
        - ``latex_indices`` -- (default: ``None``) tuple of strings
          representing the indices for the LaTeX symbols of the elements of
          the basis; if ``None``, ``indices`` is used instead
        - ``symbol_dual`` -- (default: ``None``) same as ``symbol`` but for the
          dual basis; if ``None``, ``symbol`` must be a string and is used
          for the common base of the symbols of the elements of the dual basis
        - ``latex_symbol_dual`` -- (default: ``None``) same as ``latex_symbol``
          but for the dual basis

        OUTPUT:

        - a :class:`~sage.manifolds.local_frame.LocalFrame` representing a basis
          on ``self``

        EXAMPLES::

            sage: M = Manifold(2, 'M', structure='top')
            sage: E = M.vector_bundle(2, 'E')
            sage: C0 = E.section_module(force_free=True)
            sage: e = C0.basis('e'); e
            Local frame (E|_M, (e_0,e_1))

        See :class:`~sage.manifolds.local_frame.LocalFrame` for more examples
        and documentation.
        """
    set_default_frame: Incomplete
    default_frame: Incomplete
