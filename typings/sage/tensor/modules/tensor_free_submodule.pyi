from .comp import CompFullyAntiSym as CompFullyAntiSym, CompFullySym as CompFullySym, CompWithSym as CompWithSym
from .finite_rank_free_module import FiniteRankFreeModule_abstract as FiniteRankFreeModule_abstract
from .tensor_free_module import TensorFreeModule as TensorFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.sets.disjoint_set import DisjointSet as DisjointSet
from sage.typeset.unicode_characters import unicode_otimes as unicode_otimes

class TensorFreeSubmodule_sym(TensorFreeModule):
    """
    Class for free submodules of tensor products of free modules
    that are defined by some monoterm symmetries.

    EXAMPLES::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: e = M.basis('e')
        sage: T60M = M.tensor_module(6, 0); T60M
        Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring
        sage: T60M._name
        'T^(6, 0)(M)'
        sage: latex(T60M)
        T^{(6, 0)}\\left(M\\right)
        sage: T40Sym45M = M.tensor_module(6, 0, sym=((4, 5))); T40Sym45M
        Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring,
         with symmetry on the index positions (4, 5)
        sage: T40Sym45M._name
        'T^{0,1,2,3}(M)⊗Sym^{4,5}(M)'
        sage: latex(T40Sym45M)
        T^{\\{0,1,2,3\\}}(M) \\otimes \\mathrm{Sym}^{\\{4,5\\}}(M)
        sage: Sym0123x45M = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5))); Sym0123x45M
        Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring,
         with symmetry on the index positions (0, 1, 2, 3),
         with symmetry on the index positions (4, 5)
        sage: Sym0123x45M._name
        'Sym^{0,1,2,3}(M)⊗Sym^{4,5}(M)'
        sage: latex(Sym0123x45M)
        \\mathrm{Sym}^{\\{0,1,2,3\\}}(M) \\otimes \\mathrm{Sym}^{\\{4,5\\}}(M)
        sage: Sym012x345M = M.tensor_module(6, 0, sym=((0, 1, 2), (3, 4, 5))); Sym012x345M
        Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring,
         with symmetry on the index positions (0, 1, 2),
         with symmetry on the index positions (3, 4, 5)
        sage: Sym012x345M._name
        'Sym^{0,1,2}(M)⊗Sym^{3,4,5}(M)'
        sage: latex(Sym012x345M)
        \\mathrm{Sym}^{\\{0,1,2\\}}(M) \\otimes \\mathrm{Sym}^{\\{3,4,5\\}}(M)
        sage: Sym012345M = M.tensor_module(6, 0, sym=((0, 1, 2, 3, 4, 5))); Sym012345M
        Free module of fully symmetric type-(6,0) tensors
         on the Rank-3 free module M over the Integer Ring
        sage: Sym012345M._name
        'Sym^6(M)'
        sage: latex(Sym012345M)
        \\mathrm{Sym}^6(M)

    Canonical injections from submodules are coercions::

        sage: Sym0123x45M.has_coerce_map_from(Sym012345M)
        True
        sage: T60M.has_coerce_map_from(Sym0123x45M)
        True
        sage: t = e[0] * e[0] * e[0] * e[0] * e[0] * e[0]
        sage: t.parent()
        Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring
        sage: Sym012345M(t) is t
        False

    TESTS::

        sage: T = M.tensor_module(4, 4, sym=((0, 1)), antisym=((4, 5))); T
        Free module of type-(4,4) tensors on the Rank-3 free module M over the Integer Ring,
         with symmetry on the index positions (0, 1),
         with antisymmetry on the index positions (4, 5)
        sage: T._name
        'T^{2,3}(M)⊗T^{6,7}(M*)⊗Sym^{0,1}(M)⊗ASym^{4,5}(M*)'
        sage: latex(T)
        T^{\\{2,3\\}}(M) \\otimes T^{\\{6,7\\}}(M^*) \\otimes \\mathrm{Sym}^{\\{0,1\\}}(M) \\otimes \\mathrm{ASym}^{\\{4,5\\}}(M^*)
    """
    def __init__(self, fmodule, tensor_type, name=None, latex_name=None, sym=None, antisym=None, *, category=None, ambient=None) -> None:
        """
        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: Sym0123x45M = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: TestSuite(Sym0123x45M).run()
        """
    def construction(self) -> None:
        """
        Return the functorial construction of ``self``.

        This implementation just returns ``None``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: Sym2M = M.tensor_module(2, 0, sym=range(2)); Sym2M
            Free module of fully symmetric type-(2,0) tensors on the Rank-3 free module M over the Integer Ring
            sage: Sym2M.construction() is None
            True
        """
    def is_submodule(self, other):
        """
        Return ``True`` if ``self`` is a submodule of ``other``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T60M = M.tensor_module(6, 0)
            sage: Sym0123x45M = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: Sym012x345M = M.tensor_module(6, 0, sym=((0, 1, 2), (3, 4, 5)))
            sage: Sym012345M  = M.tensor_module(6, 0, sym=((0, 1, 2, 3, 4, 5)))
            sage: Sym012345M.is_submodule(Sym012345M)
            True
            sage: Sym012345M.is_submodule(Sym0123x45M)
            True
            sage: Sym0123x45M.is_submodule(Sym012345M)
            False
            sage: Sym012x345M.is_submodule(Sym0123x45M)
            False
            sage: all(S.is_submodule(T60M) for S in (Sym0123x45M, Sym012x345M, Sym012345M))
            True
        """
    @lazy_attribute
    def lift(self):
        """
        The lift (embedding) map from ``self`` to the ambient space.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: Sym0123x45M = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: Sym0123x45M.lift
            Generic morphism:
              From: Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring,
                     with symmetry on the index positions (0, 1, 2, 3),
                     with symmetry on the index positions (4, 5)
              To:   Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring
        """
    @lazy_attribute
    def reduce(self):
        """
        The reduce map.

        This map reduces elements of the ambient space modulo this
        submodule.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(QQ, 3, name='M')
            sage: e = M.basis('e')
            sage: X = M.tensor_module(6, 0)
            sage: Y = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: Y.reduce
            Generic endomorphism of
             Free module of type-(6,0) tensors on the 3-dimensional vector space M over the Rational Field
            sage: t = e[0]*e[0]*e[0]*e[0]*e[1]*e[2]; t.disp()
            e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2 = e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2
            sage: r = Y.reduce(t); r
            Type-(6,0) tensor on the 3-dimensional vector space M over the Rational Field
            sage: r.disp()
            1/2 e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2 - 1/2 e_0⊗e_0⊗e_0⊗e_0⊗e_2⊗e_1
            sage: r.parent()._name
            'T^(6, 0)(M)'

        If the base ring is not a field, this may fail::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: X = M.tensor_module(6, 0)
            sage: Y = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: Y.reduce
            Generic endomorphism of
             Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring
            sage: t = e[0]*e[0]*e[0]*e[0]*e[1]*e[2]; t.disp()
            e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2 = e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2
            sage: Y.reduce(t)
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: X = M.tensor_module(6, 0)
            sage: Y = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: all(Y.reduce(u.lift()) == 0 for u in Y.basis('e'))
            True
        """
    @lazy_attribute
    def retract(self):
        """
        The retract map from the ambient space.

        This is a partial map, which gives an error for elements not in the subspace.

        Calling this map on elements of the ambient space is the same as calling the
        element constructor of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: X = M.tensor_module(6, 0)
            sage: Y = M.tensor_module(6, 0, sym=((0, 1, 2, 3), (4, 5)))
            sage: e_Y = Y.basis('e')
            sage: Y.retract
            Generic morphism:
              From: Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring
              To:   Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring,
                     with symmetry on the index positions (0, 1, 2, 3),
                     with symmetry on the index positions (4, 5)

            sage: t = e[0]*e[0]*e[0]*e[0]*e[1]*e[2]; t.disp()
            e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2 = e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2
            sage: Y.retract(t)
            Traceback (most recent call last):
            ...
            ValueError: this tensor does not have the symmetries of
             Free module of type-(6,0) tensors on the Rank-3 free module M over the Integer Ring,
              with symmetry on the index positions (0, 1, 2, 3),
              with symmetry on the index positions (4, 5)
            sage: t = e[0]*e[0]*e[0]*e[0]*e[1]*e[2] + e[0]*e[0]*e[0]*e[0]*e[2]*e[1]
            sage: y = Y.retract(t); y
            Type-(6,0) tensor on the Rank-3 free module M over the Integer Ring
            sage: y.disp()
            e_0⊗e_0⊗e_0⊗e_0⊗e_1⊗e_2 + e_0⊗e_0⊗e_0⊗e_0⊗e_2⊗e_1
            sage: y.parent()._name
            'Sym^{0,1,2,3}(M)⊗Sym^{4,5}(M)'

        TESTS::

            sage: all(Y.retract(u.lift()) == u for u in e_Y)
            True
        """
