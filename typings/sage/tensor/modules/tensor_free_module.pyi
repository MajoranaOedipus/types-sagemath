from .tensor_free_submodule_basis import TensorFreeSubmoduleBasis_sym as TensorFreeSubmoduleBasis_sym
from sage.categories.modules import Modules as Modules
from sage.misc.cachefunc import cached_method as cached_method
from sage.tensor.modules.alternating_contr_tensor import AlternatingContrTensor as AlternatingContrTensor
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule_abstract as FiniteRankFreeModule_abstract
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm as FreeModuleAltForm
from sage.tensor.modules.free_module_automorphism import FreeModuleAutomorphism as FreeModuleAutomorphism
from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleMorphism as FiniteRankFreeModuleMorphism
from sage.tensor.modules.free_module_tensor import FreeModuleTensor as FreeModuleTensor
from sage.tensor.modules.reflexive_module import ReflexiveModule_tensor as ReflexiveModule_tensor

class TensorFreeModule(ReflexiveModule_tensor, FiniteRankFreeModule_abstract):
    """
    Class for the free modules over a commutative ring `R` that are
    tensor products of a given free module `M` over `R` with itself and its
    dual `M^*`:

    .. MATH::

        T^{(k,l)}(M) = \\underbrace{M\\otimes\\cdots\\otimes M}_{k\\ \\; \\mbox{times}}
        \\otimes \\underbrace{M^*\\otimes\\cdots\\otimes M^*}_{l\\ \\; \\mbox{times}}

    As recalled above, `T^{(k,l)}(M)` can be canonically identified with the
    set of tensors of type `(k,l)` on `M`.

    This is a Sage *parent* class, whose *element* class is
    :class:`~sage.tensor.modules.free_module_tensor.FreeModuleTensor`.

    INPUT:

    - ``fmodule`` -- free module `M` of finite rank over a commutative ring
      `R`, as an instance of
      :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`
    - ``tensor_type`` -- pair ``(k, l)`` with ``k`` being the contravariant
      rank and ``l`` the covariant rank
    - ``name`` -- (default: ``None``) string; name given to the tensor module
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      tensor module; if none is provided, it is set to ``name``

    EXAMPLES:

    Set of tensors of type `(1,2)` on a free `\\ZZ`-module of rank 3::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: e = M.basis('e')
        sage: from sage.tensor.modules.tensor_free_module import TensorFreeModule
        sage: T = TensorFreeModule(M, (1,2)) ; T
        Free module of type-(1,2) tensors on the
         Rank-3 free module M over the Integer Ring

    Instead of importing TensorFreeModule in the global name space, it is
    recommended to use the module's method
    :meth:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.tensor_module`::

        sage: T = M.tensor_module(1,2) ; T
        Free module of type-(1,2) tensors on the
         Rank-3 free module M over the Integer Ring
        sage: latex(T)
        T^{(1, 2)}\\left(M\\right)

    The module ``M`` itself is considered as the set of tensors of
    type `(1,0)`::

        sage: M is M.tensor_module(1,0)
        True

    ``T`` is a module (actually a free module) over `\\ZZ`::

        sage: T.category()
        Category of tensor products of finite dimensional modules over Integer Ring
        sage: T in Modules(ZZ)
        True
        sage: T.rank()
        27
        sage: T.base_ring()
        Integer Ring
        sage: T.base_module()
        Rank-3 free module M over the Integer Ring

    ``T`` is a *parent* object, whose elements are instances of
    :class:`~sage.tensor.modules.free_module_tensor.FreeModuleTensor`::

        sage: t = T.an_element() ; t
        Type-(1,2) tensor on the Rank-3 free module M over the Integer Ring
        sage: from sage.tensor.modules.free_module_tensor import FreeModuleTensor
        sage: isinstance(t, FreeModuleTensor)
        True
        sage: t in T
        True
        sage: T.is_parent_of(t)
        True

    Elements can be constructed from ``T``. In particular, 0 yields
    the zero element of ``T``::

        sage: T(0)
        Type-(1,2) tensor zero on the Rank-3 free module M over the Integer Ring
        sage: T(0) is T.zero()
        True

    while nonzero elements are constructed by providing their components in
    a given basis::

        sage: e
        Basis (e_0,e_1,e_2) on the Rank-3 free module M over the Integer Ring
        sage: comp = [[[i-j+k for k in range(3)] for j in range(3)] for i in range(3)]
        sage: t = T(comp, basis=e, name='t') ; t
        Type-(1,2) tensor t on the Rank-3 free module M over the Integer Ring
        sage: t.comp(e)[:]
        [[[0, 1, 2], [-1, 0, 1], [-2, -1, 0]],
         [[1, 2, 3], [0, 1, 2], [-1, 0, 1]],
         [[2, 3, 4], [1, 2, 3], [0, 1, 2]]]
        sage: t.display(e)
        t = e_0⊗e^0⊗e^1 + 2 e_0⊗e^0⊗e^2 - e_0⊗e^1⊗e^0 + e_0⊗e^1⊗e^2
         - 2 e_0⊗e^2⊗e^0 - e_0⊗e^2⊗e^1 + e_1⊗e^0⊗e^0 + 2 e_1⊗e^0⊗e^1
         + 3 e_1⊗e^0⊗e^2 + e_1⊗e^1⊗e^1 + 2 e_1⊗e^1⊗e^2 - e_1⊗e^2⊗e^0
         + e_1⊗e^2⊗e^2 + 2 e_2⊗e^0⊗e^0 + 3 e_2⊗e^0⊗e^1 + 4 e_2⊗e^0⊗e^2
         + e_2⊗e^1⊗e^0 + 2 e_2⊗e^1⊗e^1 + 3 e_2⊗e^1⊗e^2 + e_2⊗e^2⊗e^1
         + 2 e_2⊗e^2⊗e^2

    An alternative is to construct the tensor from an empty list of components
    and to set the nonzero components afterwards::

        sage: t = T([], name='t')
        sage: t.set_comp(e)[0,1,1] = -3
        sage: t.set_comp(e)[2,0,1] = 4
        sage: t.display(e)
        t = -3 e_0⊗e^1⊗e^1 + 4 e_2⊗e^0⊗e^1

    See the documentation of
    :class:`~sage.tensor.modules.free_module_tensor.FreeModuleTensor`
    for the full list of arguments that can be provided to the __call__
    operator. For instance, to construct a tensor symmetric with respect to the
    last two indices::

        sage: t = T([], name='t', sym=(1,2))
        sage: t.set_comp(e)[0,1,1] = -3
        sage: t.set_comp(e)[2,0,1] = 4
        sage: t.display(e)  # notice that t^2_{10} has be set equal to t^2_{01} by symmetry
        t = -3 e_0⊗e^1⊗e^1 + 4 e_2⊗e^0⊗e^1 + 4 e_2⊗e^1⊗e^0

    The tensor modules over a given module `M` are unique::

        sage: T is M.tensor_module(1,2)
        True

    There is a coercion map from `\\Lambda^p(M^*)`, the set of alternating
    forms of degree `p`, to `T^{(0,p)}(M)`::

        sage: L2 = M.dual_exterior_power(2) ; L2
        2nd exterior power of the dual of the Rank-3 free module M over the
         Integer Ring
        sage: T02 = M.tensor_module(0,2) ; T02
        Free module of type-(0,2) tensors on the Rank-3 free module M over the
         Integer Ring
        sage: T02.has_coerce_map_from(L2)
        True

    Of course, for `p\\geq 2`, there is no coercion in the reverse direction,
    since not every tensor of type `(0,p)` is alternating::

        sage: L2.has_coerce_map_from(T02)
        False

    The coercion map `\\Lambda^2(M^*)\\rightarrow T^{(0,2)}(M)` in action::

        sage: a = M.alternating_form(2, name='a') ; a
        Alternating form a of degree 2 on the Rank-3 free module M over the
         Integer Ring
        sage: a[0,1], a[1,2] = 4, -3
        sage: a.display(e)
        a = 4 e^0∧e^1 - 3 e^1∧e^2
        sage: a.parent() is L2
        True
        sage: ta = T02(a) ; ta
        Type-(0,2) tensor a on the Rank-3 free module M over the Integer Ring
        sage: ta.display(e)
        a = 4 e^0⊗e^1 - 4 e^1⊗e^0 - 3 e^1⊗e^2 + 3 e^2⊗e^1
        sage: ta.symmetries() # the antisymmetry is of course preserved
        no symmetry;  antisymmetry: (0, 1)

    For the degree `p=1`, we have the identity `\\Lambda^1(M^*) = T^{(0,1)}(M) = M^*`::

        sage: M.dual_exterior_power(1) is M.tensor_module(0,1)
        True
        sage: M.tensor_module(0,1) is M.dual()
        True

    There is a canonical identification between tensors of type `(1,1)` and
    endomorphisms of module `M`. Accordingly, coercion maps have been
    implemented between `T^{(1,1)}(M)` and `\\mathrm{End}(M)` (the module of
    all endomorphisms of `M`, see
    :class:`~sage.tensor.modules.free_module_homset.FreeModuleHomset`)::

        sage: T11 = M.tensor_module(1,1) ; T11
        Free module of type-(1,1) tensors on the Rank-3 free module M over the
         Integer Ring
        sage: End(M)
        Set of Morphisms from Rank-3 free module M over the Integer Ring
         to Rank-3 free module M over the Integer Ring
         in Category of finite dimensional modules over Integer Ring
        sage: T11.has_coerce_map_from(End(M))
        True
        sage: End(M).has_coerce_map_from(T11)
        True

    The coercion map `\\mathrm{End}(M)\\rightarrow T^{(1,1)}(M)` in action::

        sage: phi = End(M).an_element() ; phi
        Generic endomorphism of Rank-3 free module M over the Integer Ring
        sage: phi.matrix(e)
        [1 1 1]
        [1 1 1]
        [1 1 1]
        sage: tphi = T11(phi) ; tphi # image of phi by the coercion map
        Type-(1,1) tensor on the Rank-3 free module M over the Integer Ring
        sage: tphi[:]
        [1 1 1]
        [1 1 1]
        [1 1 1]
        sage: t = M.tensor((1,1))
        sage: t[0,0], t[1,1], t[2,2] = -1,-2,-3
        sage: t[:]
        [-1  0  0]
        [ 0 -2  0]
        [ 0  0 -3]
        sage: s = t + phi ; s  # phi is coerced to a type-(1,1) tensor prior to the addition
        Type-(1,1) tensor on the Rank-3 free module M over the Integer Ring
        sage: s[:]
        [ 0  1  1]
        [ 1 -1  1]
        [ 1  1 -2]

    The coercion map `T^{(1,1)}(M) \\rightarrow \\mathrm{End}(M)` in action::

        sage: phi1 = End(M)(tphi) ; phi1
        Generic endomorphism of Rank-3 free module M over the Integer Ring
        sage: phi1 == phi
        True
        sage: s = phi + t ; s  # t is coerced to an endomorphism prior to the addition
        Generic endomorphism of Rank-3 free module M over the Integer Ring
        sage: s.matrix(e)
        [ 0  1  1]
        [ 1 -1  1]
        [ 1  1 -2]

    There is a coercion `\\mathrm{GL}(M)\\rightarrow T^{(1,1)}(M)`, i.e. from
    automorphisms of `M` to type-`(1,1)` tensors on `M`::

        sage: GL = M.general_linear_group() ; GL
        General linear group of the Rank-3 free module M over the Integer Ring
        sage: T11.has_coerce_map_from(GL)
        True

    The coercion map `\\mathrm{GL}(M)\\rightarrow T^{(1,1)}(M)` in action::

        sage: a = GL.an_element() ; a
        Automorphism of the Rank-3 free module M over the Integer Ring
        sage: a.matrix(e)
        [ 1  0  0]
        [ 0 -1  0]
        [ 0  0  1]
        sage: ta = T11(a) ; ta
        Type-(1,1) tensor on the Rank-3 free module M over the Integer Ring
        sage: ta.display(e)
        e_0⊗e^0 - e_1⊗e^1 + e_2⊗e^2
        sage: a.display(e)
        e_0⊗e^0 - e_1⊗e^1 + e_2⊗e^2

    Of course, there is no coercion in the reverse direction, since not
    every type-`(1,1)` tensor is invertible::

        sage: GL.has_coerce_map_from(T11)
        False
    """
    Element = FreeModuleTensor
    def __init__(self, fmodule, tensor_type, name=None, latex_name=None, category=None) -> None:
        """
        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T = M.tensor_module(2, 3)
            sage: TestSuite(T).run()
        """
    @cached_method
    def zero(self):
        """
        Return the zero of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: T11 = M.tensor_module(1,1)
            sage: T11.zero()
            Type-(1,1) tensor zero on the Rank-3 free module M over the Integer
             Ring

        The zero element is cached::

            sage: T11.zero() is T11(0)
            True
        """
    def base_module(self):
        """
        Return the free module on which ``self`` is constructed.

        OUTPUT:

        - instance of :class:`FiniteRankFreeModule` representing the free
          module on which the tensor module is defined.

        EXAMPLES:

        Base module of a type-`(1,2)` tensor module::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T = M.tensor_module(1,2)
            sage: T.base_module()
            Rank-3 free module M over the Integer Ring
            sage: T.base_module() is M
            True
        """
    def tensor_type(self):
        """
        Return the tensor type of ``self``.

        OUTPUT:

        - pair `(k,l)` such that ``self`` is the module tensor product
          `T^{(k,l)}(M)`

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3)
            sage: T = M.tensor_module(1,2)
            sage: T.tensor_type()
            (1, 2)
        """
    @cached_method
    def basis(self, symbol, latex_symbol=None, from_family=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Return the standard basis of ``self`` corresponding to a basis of the base module.

        INPUT:

        - ``symbol``, ``indices`` -- passed to the base module's method
          :meth:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.basis`
          to select a basis of the :meth:`base_module` of ``self``,
          or to create it.

        - other parameters -- passed to
          :meth:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.basis`; when
          the basis does not exist yet, it will be created using these parameters.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T = M.tensor_module(1,1)
            sage: e_T = T.basis('e'); e_T
            Standard basis on the
             Free module of type-(1,1) tensors on the Rank-3 free module M over the Integer Ring
             induced by Basis (e_0,e_1,e_2) on the Rank-3 free module M over the Integer Ring
            sage: for a in e_T: a.display()
            e_0⊗e^0
            e_0⊗e^1
            e_0⊗e^2
            e_1⊗e^0
            e_1⊗e^1
            e_1⊗e^2
            e_2⊗e^0
            e_2⊗e^1
            e_2⊗e^2

            sage: Sym2M = M.tensor_module(2, 0, sym=range(2))
            sage: e_Sym2M = Sym2M.basis('e'); e_Sym2M
            Standard basis on the
             Free module of fully symmetric type-(2,0) tensors on the Rank-3 free module M over the Integer Ring
             induced by Basis (e_0,e_1,e_2) on the Rank-3 free module M over the Integer Ring
            sage: for a in e_Sym2M: a.display()
            e_0⊗e_0
            e_0⊗e_1 + e_1⊗e_0
            e_0⊗e_2 + e_2⊗e_0
            e_1⊗e_1
            e_1⊗e_2 + e_2⊗e_1
            e_2⊗e_2

            sage: M = FiniteRankFreeModule(ZZ, 2)
            sage: e = M.basis('e')
            sage: f = M.basis('f', from_family=(-e[1], e[0]))
            sage: for b in f: b.display()
            f_0 = -e_1
            f_1 = e_0
            sage: S = M.tensor_module(2, 0, sym=(0,1))
            sage: fS = S.basis('f')
            sage: for b in fS: b.display()
            e_1⊗e_1
            -e_0⊗e_1 - e_1⊗e_0
            e_0⊗e_0
            sage: for b in fS: b.display(f)
            f_0⊗f_0
            f_0⊗f_1 + f_1⊗f_0
            f_1⊗f_1
        """
