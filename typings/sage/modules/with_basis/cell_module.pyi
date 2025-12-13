from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.data_structures.blas_dict import linear_combination as linear_combination
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.with_basis.subquotient import QuotientModuleWithBasis as QuotientModuleWithBasis
from sage.structure.element import Element as Element

class CellModule(CombinatorialFreeModule):
    """
    A cell module.

    Let `R` be a commutative ring. Let `A` be a cellular `R`-algebra
    with cell datum `(\\Lambda, i, M, C)`. A *cell module* `W(\\lambda)`
    is the `R`-module given by `R\\{C_s \\mid s \\in M(\\lambda)\\}` with
    an action of `a \\in A` given by `a C_s = \\sum_{u \\in M(\\lambda)}
    r_a(u, s) C_u`, where `r_a(u, s)` is the same as those
    given by the cellular condition:

    .. MATH::

        a C^{\\lambda}_{st} = \\sum_{u \\in M(\\lambda)} r_a(u, s)
        C_{ut}^{\\lambda} +
        \\sum_{\\substack{\\mu < \\lambda \\\\ x,y \\in M(\\mu)}} R C^{\\mu}_{xy}.

    INPUT:

    - ``A`` -- a cellular algebra
    - ``mu`` -- an element of the cellular poset of ``A``

    .. SEEALSO::

        :class:`~sage.algebras.cellular_basis.CellularBasis`

    AUTHORS:

    - Travis Scrimshaw (2015-11-5): Initial version

    REFERENCES:

    - [GrLe1996]_
    - [KX1998]_
    - [Mat1999]_
    - :wikipedia:`Cellular_algebra`
    - http://webusers.imj-prg.fr/~bernhard.keller/ictp2006/lecturenotes/xi.pdf
    """
    @staticmethod
    def __classcall_private__(cls, A, mu, **kwds):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W1 = S.cell_module([2,1])
            sage: W2 = S.cell_module([2,1], prefix='W')
            sage: W1 is W2
            True
        """
    def __init__(self, A, mu, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: TestSuite(W).run()
        """
    def cellular_algebra(self):
        """
        Return the cellular algebra of ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: W.cellular_algebra() is S.cellular_basis()
            True
            sage: S.has_coerce_map_from(W.cellular_algebra())
            True
        """
    def bilinear_form(self, x, y):
        """
        Return the bilinear form on ``x`` and ``y``.

        The cell module `W(\\lambda)` has a canonical bilinear form
        `\\Phi_{\\lambda} : W(\\lambda) \\times W(\\lambda) \\to W(\\lambda)`
        given by

        .. MATH::

            C_{ss}^{\\lambda} C_{tt}^{\\lambda} = \\Phi_{\\lambda}(C_s, C_t)
            C_{st}^{\\lambda} +
            \\sum_{\\substack{\\mu < \\lambda \\\\ x,y \\in M(\\mu)}} R C^{\\mu}_{xy}.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: elt = W.an_element(); elt
            2*W[[1, 2], [3]] + 2*W[[1, 3], [2]]
            sage: W.bilinear_form(elt, elt)
            8
        """
    def bilinear_form_matrix(self, ordering=None):
        """
        Return the matrix corresponding to the bilinear form
        of ``self``.

        INPUT:

        - ``ordering`` -- (optional) an ordering of the indices

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: W.bilinear_form_matrix()
            [1 0]
            [0 1]
        """
    @cached_method
    def nonzero_bilinear_form(self):
        """
        Return ``True`` if the bilinear form of ``self`` is nonzero.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: W.nonzero_bilinear_form()
            True

        TESTS::

            sage: C5.<z5> = CyclotomicField(5)
            sage: TL = TemperleyLiebAlgebra(2, z5 + ~z5, C5)
            sage: m = TL.cell_module(0)
            sage: m.nonzero_bilinear_form()
            True
        """
    @cached_method
    def radical_basis(self):
        """
        Return a basis of the radical of ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: W.radical_basis()
            ()
        """
    def radical(self):
        """
        Return the radical of ``self``.

        Let `W(\\lambda)` denote a cell module. The *radical* of `W(\\lambda)`
        is defined as

        .. MATH::

            \\operatorname{rad}(\\lambda) := \\{x \\in W(\\lambda) \\mid
            \\Phi_{\\lambda}(x, y)\\},

        and note that it is a submodule of `W(\\lambda)`.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: R = W.radical(); R
            Radical of Cell module indexed by [2, 1] of Cellular basis of
             Symmetric group algebra of order 3 over Rational Field
            sage: R.basis()
            Finite family {}
        """
    def simple_module(self):
        """
        Return the corresponding simple module of ``self``.

        Let `W(\\lambda)` denote a cell module. The simple module `L(\\lambda)`
        is defined as `W(\\lambda) / \\operatorname{rad}(\\lambda)`,
        where `\\operatorname{rad}(\\lambda)` is the radical of the
        bilinear form `\\Phi_{\\lambda}`.

        .. SEEALSO::

            :meth:`radical`

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: W = S.cell_module([2,1])
            sage: L = W.simple_module(); L
            Simple module indexed by [2, 1] of Cellular basis of
             Symmetric group algebra of order 3 over Rational Field
            sage: L.has_coerce_map_from(W)
            True
        """
    class Element(CombinatorialFreeModule.Element): ...

class SimpleModule(QuotientModuleWithBasis):
    """
    A simple module of a cellular algebra.

    Let `W(\\lambda)` denote a cell module. The simple module `L(\\lambda)`
    is defined as `W(\\lambda) / \\operatorname{rad}(\\lambda)`,
    where `\\operatorname{rad}(\\lambda)` is the radical of the
    bilinear form `\\Phi_{\\lambda}`.
    """
    def __init__(self, submodule) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SymmetricGroupAlgebra(QQ, 3)
            sage: L = S.cell_module([2,1]).simple_module()
            sage: TestSuite(L).run()
        """
    class Element(QuotientModuleWithBasis.Element): ...
