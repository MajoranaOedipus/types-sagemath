from sage.categories.homset import Homset as Homset
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.tensor.modules.free_module_automorphism import FreeModuleAutomorphism as FreeModuleAutomorphism
from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleEndomorphism as FiniteRankFreeModuleEndomorphism, FiniteRankFreeModuleMorphism as FiniteRankFreeModuleMorphism
from sage.tensor.modules.free_module_tensor import FreeModuleTensor as FreeModuleTensor

class FreeModuleHomset(Homset, metaclass=ClasscallMetaclass):
    '''
    Set of homomorphisms between free modules of finite rank over a
    commutative ring.

    Given two free modules `M` and `N` of respective ranks `m` and `n` over a
    commutative ring `R`, the class :class:`FreeModuleHomset` implements the
    set `\\mathrm{Hom}(M,N)` of homomorphisms `M\\rightarrow N`.
    The set `\\mathrm{Hom}(M,N)` is actually a free module of rank `mn` over
    `R`, but this aspect is not taken into account here.

    This is a Sage *parent* class, whose *element* class is
    :class:`~sage.tensor.modules.free_module_morphism.FiniteRankFreeModuleMorphism`.

    The case `M=N` (endomorphisms) is delegated to the subclass :class:`FreeModuleEndset`.

    INPUT:

    - ``fmodule1`` -- free module `M` (domain of the homomorphisms), as an
      instance of
      :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`
    - ``fmodule2`` -- free module `N` (codomain of the homomorphisms), as an
      instance of
      :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`
    - ``name`` -- (default: ``None``) string; name given to the hom-set; if
      none is provided, Hom(M,N) will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      hom-set; if none is provided, `\\mathrm{Hom}(M,N)` will be used

    EXAMPLES:

    Set of homomorphisms between two free modules over `\\ZZ`::

        sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
        sage: N = FiniteRankFreeModule(ZZ, 2, name=\'N\')
        sage: H = Hom(M,N) ; H
        Set of Morphisms from Rank-3 free module M over the Integer Ring
         to Rank-2 free module N over the Integer Ring
         in Category of finite dimensional modules over Integer Ring
        sage: type(H)
        <class \'sage.tensor.modules.free_module_homset.FreeModuleHomset_with_category_with_equality_by_id\'>
        sage: H.category()
        Category of homsets of modules over Integer Ring

    Hom-sets are cached::

        sage: H is Hom(M,N)
        True

    The LaTeX formatting is::

        sage: latex(H)
        \\mathrm{Hom}\\left(M,N\\right)

    As usual, the construction of an element is performed by the ``__call__``
    method; the argument can be the matrix representing the morphism in the
    default bases of the two modules::

        sage: e = M.basis(\'e\')
        sage: f = N.basis(\'f\')
        sage: phi = H([[-1,2,0], [5,1,2]]) ; phi
        Generic morphism:
          From: Rank-3 free module M over the Integer Ring
          To:   Rank-2 free module N over the Integer Ring
        sage: phi.parent() is H
        True

    An example of construction from a matrix w.r.t. bases that are not the
    default ones::

        sage: ep = M.basis(\'ep\', latex_symbol=r"e\'")
        sage: fp = N.basis(\'fp\', latex_symbol=r"f\'")
        sage: phi2 = H([[3,2,1], [1,2,3]], bases=(ep,fp)) ; phi2
        Generic morphism:
          From: Rank-3 free module M over the Integer Ring
          To:   Rank-2 free module N over the Integer Ring

    The zero element::

        sage: z = H.zero() ; z
        Generic morphism:
          From: Rank-3 free module M over the Integer Ring
          To:   Rank-2 free module N over the Integer Ring
        sage: z.matrix(e,f)
        [0 0 0]
        [0 0 0]

    The test suite for H is passed::

        sage: TestSuite(H).run()
    '''
    Element = FiniteRankFreeModuleMorphism
    @staticmethod
    def __classcall_private__(cls, fmodule1, fmodule2, name=None, latex_name=None):
        """
        Delegate to the subclass :class:`FreeModuleEndset` if ``fmodule1 == fmodule2``.

        TESTS::

            sage: from sage.tensor.modules.free_module_homset import FreeModuleEndset, FreeModuleHomset
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: isinstance(FreeModuleHomset(M, N), FreeModuleEndset)
            False
            sage: isinstance(FreeModuleHomset(M, M), FreeModuleEndset)
            True
        """
    def __init__(self, fmodule1, fmodule2, name, latex_name) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.free_module_homset import FreeModuleHomset
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: FreeModuleHomset(M, N)
            Set of Morphisms from Rank-3 free module M over the Integer Ring
             to Rank-2 free module N over the Integer Ring
             in Category of finite dimensional modules over Integer Ring

            sage: H = FreeModuleHomset(M, N, name='L(M,N)',
            ....:                      latex_name=r'\\mathcal{L}(M,N)')
            sage: latex(H)
            \\mathcal{L}(M,N)
        """
    def __call__(self, *args, **kwds):
        """
        To bypass Homset.__call__, enforcing Parent.__call__ instead.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 2, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 3, name='N')
            sage: H = Hom(M,N)
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: a = H.__call__(0) ; a
            Generic morphism:
              From: Rank-2 free module M over the Integer Ring
              To:   Rank-3 free module N over the Integer Ring
            sage: a.matrix(e,f)
            [0 0]
            [0 0]
            [0 0]
            sage: a == H.zero()
            True
            sage: a == H(0)
            True
            sage: a = H.__call__([[1,2],[3,4],[5,6]], bases=(e,f), name='a') ; a
            Generic morphism:
              From: Rank-2 free module M over the Integer Ring
              To:   Rank-3 free module N over the Integer Ring
            sage: a.matrix(e,f)
            [1 2]
            [3 4]
            [5 6]
            sage: a == H([[1,2],[3,4],[5,6]], bases=(e,f))
            True
        """

class FreeModuleEndset(FreeModuleHomset):
    """
    Ring of endomorphisms of a free module of finite rank over a commutative ring.

    Given a free modules `M` of rank `n` over a commutative ring `R`, the
    class :class:`FreeModuleEndset` implements the ring `\\mathrm{Hom}(M,M)`
    of endomorphisms `M\\rightarrow M`.

    This is a Sage *parent* class, whose *element* class is
    :class:`~sage.tensor.modules.free_module_morphism.FiniteRankFreeModuleMorphism`.

    INPUT:

    - ``fmodule`` -- free module `M` (domain and codomain of the endomorphisms), as an
      instance of
      :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`
    - ``name`` -- (default: ``None``) string; name given to the end-set; if
      none is provided, Hom(M,M) will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      hom-set; if none is provided, `\\mathrm{Hom}(M,M)` will be used

    EXAMPLES:

    The set of homomorphisms `M\\rightarrow M`, i.e. endomorphisms, is
    obtained by the function :func:`End`::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: e = M.basis('e')
        sage: End(M)
        Set of Morphisms from Rank-3 free module M over the Integer Ring
         to Rank-3 free module M over the Integer Ring
         in Category of finite dimensional modules over Integer Ring

    ``End(M)`` is actually identical to ``Hom(M,M)``::

        sage: End(M) is Hom(M,M)
        True

    The unit of the endomorphism ring is the identity map::

        sage: End(M).one()
        Identity endomorphism of Rank-3 free module M over the Integer Ring

    whose matrix in any basis is of course the identity matrix::

        sage: End(M).one().matrix(e)
        [1 0 0]
        [0 1 0]
        [0 0 1]

    There is a canonical identification between endomorphisms of `M` and
    tensors of type `(1,1)` on `M`. Accordingly, coercion maps have been
    implemented between `\\mathrm{End}(M)` and `T^{(1,1)}(M)` (the module of
    all type-`(1,1)` tensors on `M`, see
    :class:`~sage.tensor.modules.tensor_free_module.TensorFreeModule`)::

        sage: T11 = M.tensor_module(1,1) ; T11
        Free module of type-(1,1) tensors on the Rank-3 free module M over
         the Integer Ring
        sage: End(M).has_coerce_map_from(T11)
        True
        sage: T11.has_coerce_map_from(End(M))
        True

    See :class:`~sage.tensor.modules.tensor_free_module.TensorFreeModule` for
    examples of the above coercions.

    There is a coercion `\\mathrm{GL}(M) \\rightarrow \\mathrm{End}(M)`, since
    every automorphism is an endomorphism::

        sage: GL = M.general_linear_group() ; GL
        General linear group of the Rank-3 free module M over the Integer Ring
        sage: End(M).has_coerce_map_from(GL)
        True

    Of course, there is no coercion in the reverse direction, since only
    bijective endomorphisms are automorphisms::

        sage: GL.has_coerce_map_from(End(M))
        False

    The coercion `\\mathrm{GL}(M) \\rightarrow \\mathrm{End}(M)` in action::

        sage: a = GL.an_element() ; a
        Automorphism of the Rank-3 free module M over the Integer Ring
        sage: a.matrix(e)
        [ 1  0  0]
        [ 0 -1  0]
        [ 0  0  1]
        sage: ea = End(M)(a) ; ea
        Generic endomorphism of Rank-3 free module M over the Integer Ring
        sage: ea.matrix(e)
        [ 1  0  0]
        [ 0 -1  0]
        [ 0  0  1]
    """
    Element = FiniteRankFreeModuleEndomorphism
    def __init__(self, fmodule, name, latex_name) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.free_module_homset import FreeModuleHomset
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: FreeModuleHomset(M, N)
            Set of Morphisms from Rank-3 free module M over the Integer Ring
             to Rank-2 free module N over the Integer Ring
             in Category of finite dimensional modules over Integer Ring

            sage: H = FreeModuleHomset(M, N, name='L(M,N)',
            ....:                      latex_name=r'\\mathcal{L}(M,N)')
            sage: latex(H)
            \\mathcal{L}(M,N)
        """
    def one(self):
        """
        Return the identity element of ``self`` considered as a monoid.

        OUTPUT:

        - the identity element of `\\mathrm{End}(M) = \\mathrm{Hom}(M,M)`, as an
          instance of
          :class:`~sage.tensor.modules.free_module_morphism.FiniteRankFreeModuleMorphism`

        EXAMPLES:

        Identity element of the set of endomorphisms of a free module
        over `\\ZZ`::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: H = End(M)
            sage: H.one()
            Identity endomorphism of Rank-3 free module M over the Integer Ring
            sage: H.one().matrix(e)
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: H.one().is_identity()
            True

        NB: mathematically, ``H.one()`` coincides with the identity map of the
        free module `M`. However the latter is considered here as an
        element of `\\mathrm{GL}(M)`, the general linear group of `M`.
        Accordingly, one has to use the coercion map
        `\\mathrm{GL}(M) \\rightarrow \\mathrm{End}(M)`
        to recover ``H.one()`` from ``M.identity_map()``::

            sage: M.identity_map()
            Identity map of the Rank-3 free module M over the Integer Ring
            sage: M.identity_map().parent()
            General linear group of the Rank-3 free module M over the Integer Ring
            sage: H.one().parent()
            Set of Morphisms from Rank-3 free module M over the Integer Ring
             to Rank-3 free module M over the Integer Ring
             in Category of finite dimensional modules over Integer Ring
            sage: H.one() == H(M.identity_map())
            True

        Conversely, one can recover ``M.identity_map()`` from ``H.one()`` by
        means of a conversion `\\mathrm{End}(M)\\rightarrow \\mathrm{GL}(M)`::

            sage: GL = M.general_linear_group()
            sage: M.identity_map() == GL(H.one())
            True
        """
