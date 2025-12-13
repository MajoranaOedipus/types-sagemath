from sage.misc.abstract_method import abstract_method as abstract_method
from sage.structure.parent import Parent as Parent

class ReflexiveModule_abstract(Parent):
    """
    Abstract base class for reflexive modules.

    An `R`-module `M` is *reflexive* if the natural map from `M` to its double
    dual `M^{**}` is an isomorphism.

    In the category of `R`-modules, the dual module `M^*` is
    the `R`-module of linear functionals `\\phi:\\ M \\longrightarrow R`.
    However, we do not make the assumption that the dual module
    (obtained by :meth:`dual`) is in the category :class:`Homsets`.

    We identify the double dual `M^{**}` with `M`.

    Tensor products of reflexive modules are reflexive. We identify all
    tensor products of `k` copies of `M` and `l` copies of `M^*` and
    denote it by `T^{(k,l)}(M)`. The :meth:`tensor_type` of such a tensor
    product is the pair `(k, l)`, and `M` is called its :meth:`base_module`.

    There are three abstract subclasses:

    - :class:`ReflexiveModule_base` is the base class for implementations
      of base modules `M`.

    - :class:`ReflexiveModule_dual` is the base class for implementations
      of duals `M^*`.

    - :class:`ReflexiveModule_tensor` is the base class for implementations
      of tensor modules `T^{(k,l)}(M)`.

    TESTS::

        sage: from sage.tensor.modules.reflexive_module import (
        ....:     ReflexiveModule_abstract, ReflexiveModule_base,
        ....:     ReflexiveModule_dual, ReflexiveModule_tensor)
        sage: M = FiniteRankFreeModule(ZZ, 3)
        sage: isinstance(M, ReflexiveModule_abstract)
        True
        sage: isinstance(M, ReflexiveModule_base)
        True
        sage: isinstance(M.dual(), ReflexiveModule_abstract)
        True
        sage: isinstance(M.dual(), ReflexiveModule_dual)
        True
        sage: isinstance(M.tensor_module(1, 1), ReflexiveModule_abstract)
        True
        sage: isinstance(M.tensor_module(1, 1), ReflexiveModule_tensor)
        True
    """
    def tensor_type(self) -> None:
        """
        Return the tensor type of ``self``.

        OUTPUT:

        - pair `(k,l)` such that ``self`` is the module tensor product
          `T^{(k,l)}(M)`, where `M` is the :meth:`base_module` of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3)
            sage: T = M.tensor_module(1, 2)
            sage: T.tensor_type()
            (1, 2)
        """
    @abstract_method
    def base_module(self) -> None:
        """
        Return the module on which ``self`` is constructed.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3)
            sage: M.base_module() is M
            True
            sage: M.dual().base_module() is M
            True
            sage: M.tensor_module(1, 2).base_module() is M
            True
        """
    def dual(self):
        """
        Return the dual module.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3)
            sage: M.dual()
            Dual of the Rank-3 free module over the Integer Ring
            sage: M.dual().dual()
            Rank-3 free module over the Integer Ring
            sage: M.tensor_module(1, 2)
            Free module of type-(1,2) tensors on the Rank-3 free module over the Integer Ring
            sage: M.tensor_module(1, 2).dual()
            Free module of type-(2,1) tensors on the Rank-3 free module over the Integer Ring
        """
    def tensor(self, *args, **kwds):
        """
        Return the tensor product of ``self`` and ``others``.

        This method is invoked when :class:`~sage.categories.tensor.TensorProductFunctor`
        is applied to parents.

        It just delegates to :meth:`tensor_product`.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(QQ, 2); M
            2-dimensional vector space over the Rational Field
            sage: M20 = M.tensor_module(2, 0); M20
            Free module of type-(2,0) tensors on the 2-dimensional vector space over the Rational Field
            sage: tensor([M20, M20])
            Free module of type-(4,0) tensors on the 2-dimensional vector space over the Rational Field
        """
    def tensor_power(self, n):
        """
        Return the ``n``-fold tensor product of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(QQ, 2)
            sage: M.tensor_power(3)
            Free module of type-(3,0) tensors on the 2-dimensional vector space over the Rational Field
            sage: M.tensor_module(1,2).tensor_power(3)
            Free module of type-(3,6) tensors on the 2-dimensional vector space over the Rational Field
        """
    def tensor_product(self, *others):
        """
        Return the tensor product of ``self`` and ``others``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(QQ, 2)
            sage: M.tensor_product(M)
            Free module of type-(2,0) tensors on the 2-dimensional vector space over the Rational Field
            sage: M.tensor_product(M.dual())
            Free module of type-(1,1) tensors on the 2-dimensional vector space over the Rational Field
            sage: M.dual().tensor_product(M, M.dual())
            Free module of type-(1,2) tensors on the 2-dimensional vector space over the Rational Field
            sage: M.tensor_product(M.tensor_module(1,2))
            Free module of type-(2,2) tensors on the 2-dimensional vector space over the Rational Field
            sage: M.tensor_module(1,2).tensor_product(M)
            Free module of type-(2,2) tensors on the 2-dimensional vector space over the Rational Field
            sage: M.tensor_module(1,1).tensor_product(M.tensor_module(1,2))
            Free module of type-(2,3) tensors on the 2-dimensional vector space over the Rational Field

            sage: Sym2M = M.tensor_module(2, 0, sym=range(2)); Sym2M
            Free module of fully symmetric type-(2,0) tensors on the 2-dimensional vector space over the Rational Field
            sage: Sym01x23M = Sym2M.tensor_product(Sym2M); Sym01x23M
            Free module of type-(4,0) tensors on the 2-dimensional vector space over the Rational Field,
             with symmetry on the index positions (0, 1), with symmetry on the index positions (2, 3)
            sage: Sym01x23M._index_maps
            ((0, 1), (2, 3))

            sage: N = M.tensor_module(3, 3, sym=[1, 2], antisym=[3, 4]); N
            Free module of type-(3,3) tensors on the 2-dimensional vector space over the Rational Field,
             with symmetry on the index positions (1, 2),
             with antisymmetry on the index positions (3, 4)
            sage: NxN = N.tensor_product(N); NxN
            Free module of type-(6,6) tensors on the 2-dimensional vector space over the Rational Field,
             with symmetry on the index positions (1, 2), with symmetry on the index positions (4, 5),
             with antisymmetry on the index positions (6, 7), with antisymmetry on the index positions (9, 10)
            sage: NxN._index_maps
            ((0, 1, 2, 6, 7, 8), (3, 4, 5, 9, 10, 11))
        """

class ReflexiveModule_base(ReflexiveModule_abstract):
    """
    Abstract base class for reflexive modules that are base modules.

    TESTS::

        sage: from sage.tensor.modules.reflexive_module import ReflexiveModule_base
        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: isinstance(M, ReflexiveModule_base)
        True
    """
    def base_module(self):
        """
        Return the free module on which ``self`` is constructed, namely ``self`` itself.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: M.base_module() is M
            True

            sage: M = Manifold(2, 'M')                                                  # needs sage.symbolic
            sage: XM = M.vector_field_module()                                          # needs sage.symbolic
            sage: XM.base_module() is XM                                                # needs sage.symbolic
            True
        """
    def tensor_type(self):
        """
        Return the tensor type of ``self``, the pair `(1, 0)`.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3)
            sage: M.tensor_type()
            (1, 0)

            sage: M = Manifold(2, 'M')                                                  # needs sage.symbolic
            sage: XM = M.vector_field_module()                                          # needs sage.symbolic
            sage: XM.tensor_type()                                                      # needs sage.symbolic
            (1, 0)
        """
    def dual(self):
        """
        Return the dual module.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: M.dual()
            Dual of the Rank-3 free module M over the Integer Ring
        """
    @abstract_method
    def tensor_module(self, k, l, **kwds) -> None:
        """
        Return the module of all tensors of type `(k, l)` defined on ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3)
            sage: M.tensor_module(1, 2)
            Free module of type-(1,2) tensors on the Rank-3 free module over the Integer Ring
        """

class ReflexiveModule_dual(ReflexiveModule_abstract):
    """
    Abstract base class for reflexive modules that are the duals of base modules.

    TESTS::

        sage: from sage.tensor.modules.reflexive_module import ReflexiveModule_dual
        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: isinstance(M.dual(), ReflexiveModule_dual)
        True
    """
    def tensor_type(self):
        """
        Return the tensor type of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: M.dual().tensor_type()
            (0, 1)
        """
    def construction(self) -> None:
        """
        Return the functorial construction of ``self``.

        This implementation just returns ``None``, as no functorial construction is implemented.

        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: A = M.dual()
            sage: A.construction() is None
            True
        """

class ReflexiveModule_tensor(ReflexiveModule_abstract):
    """
    Abstract base class for reflexive modules that are tensor products of base modules.

    TESTS::

        sage: from sage.tensor.modules.reflexive_module import ReflexiveModule_tensor
        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: isinstance(M.tensor_module(1, 1), ReflexiveModule_tensor)
        True
    """
    def tensor_factors(self):
        """
        Return the tensor factors of this tensor module.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T = M.tensor_module(2, 3)
            sage: T.tensor_factors()
            [Rank-3 free module M over the Integer Ring,
             Rank-3 free module M over the Integer Ring,
             Dual of the Rank-3 free module M over the Integer Ring,
             Dual of the Rank-3 free module M over the Integer Ring,
             Dual of the Rank-3 free module M over the Integer Ring]
        """
