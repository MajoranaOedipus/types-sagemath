from _typeshed import Incomplete
from collections.abc import Generator
from sage.tensor.modules.free_module_basis import Basis_abstract as Basis_abstract

class TensorFreeSubmoduleBasis_sym(Basis_abstract):
    """
    Standard basis of a free submodule of a tensor module with prescribed monoterm symmetries.

    EXAMPLES::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: T11 = M.tensor_module(1,1)
        sage: e11 = T11.basis('e')
        sage: for a in e11: a.display()
        e_0⊗e^0
        e_0⊗e^1
        e_0⊗e^2
        e_1⊗e^0
        e_1⊗e^1
        e_1⊗e^2
        e_2⊗e^0
        e_2⊗e^1
        e_2⊗e^2
    """
    def __init__(self, tensor_module, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None) -> None:
        """
        TESTS::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: T11 = M.tensor_module(1,1)
            sage: e_T11 = T11.basis('e')
            sage: TestSuite(e_T11).run()
        """
    def keys(self) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator for the keys (indices) of the family.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T11 = M.tensor_module(1,1)
            sage: e11 = T11.basis('e')
            sage: list(e11.keys())
            [(0, 0), (0, 1), (0, 2),
             (1, 0), (1, 1), (1, 2),
             (2, 0), (2, 1), (2, 2)]
        """
    def values(self) -> Generator[Incomplete]:
        """
        Return an iterator for the elements of the family.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T11 = M.tensor_module(1,1)
            sage: e11 = T11.basis('e')
            sage: [b.disp() for b in e11.values()]
            [e_0⊗e^0, e_0⊗e^1, e_0⊗e^2,
             e_1⊗e^0, e_1⊗e^1, e_1⊗e^2,
             e_2⊗e^0, e_2⊗e^1, e_2⊗e^2]
        """
    def __getitem__(self, index):
        """
        Return the basis element corresponding to a given index.

        INPUT:

        - ``index`` -- the index of the basis element

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: T11 = M.tensor_module(1,1)
            sage: e11 = T11.basis('e')
            sage: e11[1, 2].display()
            e_1⊗e^2

            sage: from sage.tensor.modules.tensor_free_submodule import TensorFreeSubmodule_sym
            sage: Sym2M = TensorFreeSubmodule_sym(M, (2, 0), sym=range(2)); Sym2M
            Free module of fully symmetric type-(2,0) tensors on the Rank-3 free module M over the Integer Ring
            sage: eSym2M = Sym2M.basis('e')
            sage: eSym2M[1, 1].display()
            e_1⊗e_1
            sage: eSym2M[1, 2].display()
            e_1⊗e_2 + e_2⊗e_1
        """
