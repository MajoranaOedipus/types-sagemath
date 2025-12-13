from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import AbstractFamily as AbstractFamily
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Basis_abstract(UniqueRepresentation, AbstractFamily):
    """
    Abstract base class for (dual) bases of free modules.

    A basis is an :class:`~sage.sets.family.AbstractFamily`, hence like
    :class:`collections.abc.Mapping` subclasses such as :class:`dict`, it is
    an associative :class:`Container`, providing methods :meth:`keys`,
    :meth:`values`, and :meth:`items`. Thus, ``e[i]`` returns the element
    of the basis ``e`` indexed by the key ``i``. However, in contrast to
    :class:`Mapping` subclasses, not the :meth:`keys` but the
    :meth:`values` are considered the elements.

    EXAMPLES::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M', start_index=1)
        sage: e = M.basis('e'); e
        Basis (e_1,e_2,e_3) on the Rank-3 free module M over the Integer Ring
        sage: list(e)
        [Element e_1 of the Rank-3 free module M over the Integer Ring,
        Element e_2 of the Rank-3 free module M over the Integer Ring,
        Element e_3 of the Rank-3 free module M over the Integer Ring]
        sage: e.category()
        Category of facade finite enumerated sets
        sage: list(e.keys())
        [1, 2, 3]
        sage: list(e.values())
        [Element e_1 of the Rank-3 free module M over the Integer Ring,
        Element e_2 of the Rank-3 free module M over the Integer Ring,
        Element e_3 of the Rank-3 free module M over the Integer Ring]
        sage: list(e.items())
        [(1, Element e_1 of the Rank-3 free module M over the Integer Ring),
        (2, Element e_2 of the Rank-3 free module M over the Integer Ring),
        (3, Element e_3 of the Rank-3 free module M over the Integer Ring)]
    """
    def __init__(self, fmodule, symbol, latex_symbol, indices, latex_indices) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: e._fmodule is M
            True
        """
    def keys(self):
        """
        Return the keys (indices) of the family.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: list(e.keys())
            [0, 1, 2]
        """
    def values(self):
        """
        Return the basis elements of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: list(e.values())
            [Element e_0 of the Rank-3 free module M over the Integer Ring,
             Element e_1 of the Rank-3 free module M over the Integer Ring,
             Element e_2 of the Rank-3 free module M over the Integer Ring]
        """
    def __iter__(self):
        """
        Return an iterator for the basis elements of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: list(e)
            [Element e_0 of the Rank-3 free module M over the Integer Ring,
             Element e_1 of the Rank-3 free module M over the Integer Ring,
             Element e_2 of the Rank-3 free module M over the Integer Ring]
            sage: ed = e.dual_basis()
            sage: list(ed)
            [Linear form e^0 on the Rank-3 free module M over the Integer Ring,
             Linear form e^1 on the Rank-3 free module M over the Integer Ring,
             Linear form e^2 on the Rank-3 free module M over the Integer Ring]

        An example with indices starting at 1 instead of 0::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M1',
            ....:                          start_index=1)
            sage: e = M.basis('e')
            sage: list(e)
            [Element e_1 of the Rank-3 free module M1 over the Integer Ring,
             Element e_2 of the Rank-3 free module M1 over the Integer Ring,
             Element e_3 of the Rank-3 free module M1 over the Integer Ring]
        """
    def __len__(self) -> int:
        '''
        Return the basis length, i.e. the rank of the free module.

        .. NOTE::

            the method ``__len__()`` is required for the basis to act as a
            "frame" in the class :class:`~sage.tensor.modules.comp.Components`.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: e.__len__()
            3
            sage: len(e)
            3
        '''
    def cardinality(self):
        """
        Return the basis length, i.e. the rank of the free module.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: e.cardinality()
            3
        """
    def __getitem__(self, index):
        """
        Return the basis element corresponding to a given index.

        INPUT:

        - ``index`` -- the index of the basis element

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: e.__getitem__(0)
            Element e_0 of the Rank-3 free module M over the Integer Ring
            sage: e.__getitem__(1)
            Element e_1 of the Rank-3 free module M over the Integer Ring
            sage: e.__getitem__(2)
            Element e_2 of the Rank-3 free module M over the Integer Ring
            sage: e[1] is e.__getitem__(1)
            True
            sage: e[1].parent() is M
            True
            sage: e[:]
            (Element e_0 of the Rank-3 free module M over the Integer Ring,
             Element e_1 of the Rank-3 free module M over the Integer Ring,
             Element e_2 of the Rank-3 free module M over the Integer Ring)
            sage: f = e.dual_basis()
            sage: f[0]
            Linear form e^0 on the Rank-3 free module M over the Integer Ring

        Examples with ``start_index=1``::

            sage: M1 = FiniteRankFreeModule(ZZ, 3, name='M', start_index=1)
            sage: e1 = M1.basis('e')
            sage: e1.__getitem__(1)
            Element e_1 of the Rank-3 free module M over the Integer Ring
            sage: e1.__getitem__(2)
            Element e_2 of the Rank-3 free module M over the Integer Ring
            sage: e1.__getitem__(3)
            Element e_3 of the Rank-3 free module M over the Integer Ring
        """
    def free_module(self):
        """
        Return the free module of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(QQ, 2, name='M', start_index=1)
            sage: e = M.basis('e')
            sage: e.free_module() is M
            True
        """
    def set_name(self, symbol, latex_symbol=None, indices=None, latex_indices=None, index_position: str = 'down') -> None:
        """
        Set (or change) the text name and LaTeX name of ``self``.

        INPUT:

        - ``symbol`` -- either a string, to be used as a common base for the
          symbols of the elements of ``self``, or a list of strings,
          representing the individual symbols of the elements of ``self``
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the elements of ``self``,
          or a list of strings, representing the individual LaTeX symbols of
          the elements of ``self``; if ``None``, ``symbol`` is used in place
          of ``latex_symbol``
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices labelling
          the elements of ``self``; if ``None``, the indices will be generated
          as integers within the range declared on the free module on which
          ``self`` is defined
        - ``latex_indices`` -- (default: ``None``) list of strings representing
          the indices for the LaTeX symbols of the elements of ``self``; if
          ``None``, ``indices`` is used instead
        - ``index_position`` -- (default: ``'down'``) determines the position
          of the indices labelling the individual elements of ``self``; can be
          either ``'down'`` or ``'up'``

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e'); e
            Basis (e_0,e_1,e_2) on the Rank-3 free module M over the Integer Ring
            sage: e.set_name('f'); e
            Basis (f_0,f_1,f_2) on the Rank-3 free module M over the Integer Ring
            sage: e.set_name(['a', 'b', 'c']); e
            Basis (a,b,c) on the Rank-3 free module M over the Integer Ring
            sage: e.set_name('e', indices=['x', 'y', 'z']); e
            Basis (e_x,e_y,e_z) on the Rank-3 free module M over the Integer Ring
            sage: e.set_name('e', index_position='up'); e
            Basis (e^0,e^1,e^2) on the Rank-3 free module M over the Integer Ring
            sage: latex(e)
            \\left(e^{0},e^{1},e^{2}\\right)
            sage: e.set_name('e', latex_symbol=r'\\epsilon'); e
            Basis (e_0,e_1,e_2) on the Rank-3 free module M over the Integer Ring
            sage: latex(e)
            \\left(\\epsilon_{0},\\epsilon_{1},\\epsilon_{2}\\right)
            sage: e.set_name('e', latex_symbol=[r'\\alpha', r'\\beta', r'\\gamma'])
            sage: latex(e)
            \\left(\\alpha,\\beta,\\gamma\\right)
            sage: e.set_name('e', latex_symbol='E',
            ....:            latex_indices=[r'\\alpha', r'\\beta', r'\\gamma'])
            sage: latex(e)
            \\left(E_{\\alpha},E_{\\beta},E_{\\gamma}\\right)
            sage: e.set_name('e') # back to the default
        """

class FreeModuleCoBasis(Basis_abstract):
    """
    Dual basis of a free module over a commutative ring.

    INPUT:

    - ``basis`` -- basis of a free module `M` of which ``self`` is the dual
      (must be an instance of :class:`FreeModuleBasis`)
    - ``symbol`` -- either a string, to be used as a common base for the
      symbols of the elements of the cobasis, or a tuple of strings,
      representing the individual symbols of the elements of the cobasis
    - ``latex_symbol`` -- (default: ``None``) either a string, to be used
      as a common base for the LaTeX symbols of the elements of the cobasis,
      or a tuple of strings, representing the individual LaTeX symbols of
      the elements of the cobasis; if ``None``, ``symbol`` is used in place
      of ``latex_symbol``
    - ``indices`` -- (default: ``None``; used only if ``symbol`` is a single
      string) tuple of strings representing the indices labelling
      the elements of the cobasis; if ``None``, the indices will be generated
      as integers within the range declared on the free module on which the
      cobasis is defined
    - ``latex_indices`` -- (default: ``None``) tuple of strings representing
      the indices for the LaTeX symbols of the elements of the cobasis; if
      ``None``, ``indices`` is used instead

    EXAMPLES:

    Dual basis on a rank-3 free module::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M', start_index=1)
        sage: e = M.basis('e') ; e
        Basis (e_1,e_2,e_3) on the Rank-3 free module M over the Integer Ring
        sage: from sage.tensor.modules.free_module_basis import FreeModuleCoBasis
        sage: f = FreeModuleCoBasis(e, 'f') ; f
        Dual basis (f^1,f^2,f^3) on the Rank-3 free module M over the Integer Ring

    Instead of importing ``FreeModuleCoBasis`` in the global name space, it is
    recommended to use the method
    :meth:`~sage.tensor.modules.free_module_basis.FreeModuleBasis.dual_basis`
    of the basis ``e``::

        sage: f = e.dual_basis() ; f
        Dual basis (e^1,e^2,e^3) on the Rank-3 free module M over the Integer Ring

    Let us check that the elements of ``f`` are in the dual of ``M``::

        sage: f[1]
        Linear form e^1 on the Rank-3 free module M over the Integer Ring
        sage: f[1] in M.dual()
        True

    and that ``f`` is indeed the dual of ``e``::

        sage: f[1](e[1]), f[1](e[2]), f[1](e[3])
        (1, 0, 0)
        sage: f[2](e[1]), f[2](e[2]), f[2](e[3])
        (0, 1, 0)
        sage: f[3](e[1]), f[3](e[2]), f[3](e[3])
        (0, 0, 1)

    TESTS::

        sage: TestSuite(f).run()
    """
    def __init__(self, basis, symbol, latex_symbol=None, indices=None, latex_indices=None) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.free_module_basis import FreeModuleCoBasis
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: f = FreeModuleCoBasis(e, 'f')
            sage: TestSuite(f).run()
        """

class FreeModuleBasis(Basis_abstract):
    """
    Basis of a free module over a commutative ring `R`.

    INPUT:

    - ``fmodule`` -- free module `M` (as an instance of
      :class:`FiniteRankFreeModule`)
    - ``symbol`` -- either a string, to be used as a common base for the
      symbols of the elements of the basis, or a tuple of strings,
      representing the individual symbols of the elements of the basis
    - ``latex_symbol`` -- (default: ``None``) either a string, to be used
      as a common base for the LaTeX symbols of the elements of the basis,
      or a tuple of strings, representing the individual LaTeX symbols of
      the elements of the basis; if ``None``, ``symbol`` is used in place
      of ``latex_symbol``
    - ``indices`` -- (default: ``None``; used only if ``symbol`` is a single
      string) tuple of strings representing the indices labelling
      the elements of the basis; if ``None``, the indices will be generated
      as integers within the range declared on ``fmodule``
    - ``latex_indices`` -- (default: ``None``) tuple of strings representing
      the indices for the LaTeX symbols of the elements of the basis; if
      ``None``, ``indices`` is used instead
    - ``symbol_dual`` -- (default: ``None``) same as ``symbol`` but for the
      dual basis; if ``None``, ``symbol`` must be a string and is used
      for the common base of the symbols of the elements of the dual basis
    - ``latex_symbol_dual`` -- (default: ``None``) same as ``latex_symbol``
      but for the dual basis

    EXAMPLES:

    A basis on a rank-3 free module over `\\ZZ`::

        sage: M0 = FiniteRankFreeModule(ZZ, 3, name='M_0')
        sage: from sage.tensor.modules.free_module_basis import FreeModuleBasis
        sage: e = FreeModuleBasis(M0, 'e') ; e
        Basis (e_0,e_1,e_2) on the Rank-3 free module M_0 over the Integer Ring

    Instead of importing ``FreeModuleBasis`` in the global name space, it is
    recommended to use the module's method
    :meth:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.basis`::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: e = M.basis('e') ; e
        Basis (e_0,e_1,e_2) on the Rank-3 free module M over the Integer Ring

    The individual elements constituting the basis are accessed via the
    square bracket operator::

        sage: e[0]
        Element e_0 of the Rank-3 free module M over the Integer Ring
        sage: e[0] in M
        True

    The slice operator ``:`` can be used to access to more than one element::

        sage: e[0:2]
        (Element e_0 of the Rank-3 free module M over the Integer Ring,
         Element e_1 of the Rank-3 free module M over the Integer Ring)
        sage: e[:]
        (Element e_0 of the Rank-3 free module M over the Integer Ring,
         Element e_1 of the Rank-3 free module M over the Integer Ring,
         Element e_2 of the Rank-3 free module M over the Integer Ring)

    The LaTeX symbol can be set explicitly::

        sage: latex(e)
        \\left(e_{0},e_{1},e_{2}\\right)
        sage: eps = M.basis('eps', latex_symbol=r'\\epsilon') ; eps
        Basis (eps_0,eps_1,eps_2) on the Rank-3 free module M over the Integer
         Ring
        sage: latex(eps)
        \\left(\\epsilon_{0},\\epsilon_{1},\\epsilon_{2}\\right)

    The individual elements of the basis are labelled according the
    parameter ``start_index`` provided at the free module construction::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M', start_index=1)
        sage: e = M.basis('e') ; e
        Basis (e_1,e_2,e_3) on the Rank-3 free module M over the Integer Ring
        sage: e[1]
        Element e_1 of the Rank-3 free module M over the Integer Ring

    It is also possible to fully customize the labels, via the argument
    ``indices``::

        sage: f = M.basis('f', indices=('x', 'y', 'z')); f
        Basis (f_x,f_y,f_z) on the Rank-3 free module M over the Integer Ring
        sage: f[1]
        Element f_x of the Rank-3 free module M over the Integer Ring

    The symbol of each element of the basis can also be freely chosen, by
    providing a tuple of symbols as the first argument of ``basis``; it is then
    mandatory to specify some symbols for the dual basis as well::

        sage: g = M.basis(('a', 'b', 'c'), symbol_dual=('A', 'B', 'C')); g
        Basis (a,b,c) on the Rank-3 free module M over the Integer Ring
        sage: g[1]
        Element a of the Rank-3 free module M over the Integer Ring
        sage: g.dual_basis()[1]
        Linear form A on the Rank-3 free module M over the Integer Ring

    TESTS::

        sage: TestSuite(e).run()
        sage: TestSuite(f).run()
        sage: TestSuite(g).run()
    """
    @staticmethod
    def __classcall_private__(cls, fmodule, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: from sage.tensor.modules.free_module_basis import FreeModuleBasis
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = FreeModuleBasis(M, 'e', latex_symbol='e')
            sage: e is FreeModuleBasis(M, 'e')
            True
        """
    def __init__(self, fmodule, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: FiniteRankFreeModule._clear_cache_() # for doctests only
            sage: from sage.tensor.modules.free_module_basis import FreeModuleBasis
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = FreeModuleBasis(M, 'e', latex_symbol=r'\\epsilon')
            sage: TestSuite(e).run()
        """
    def module(self):
        """
        Return the free module on which the basis is defined.

        OUTPUT:

        - instance of
          :class:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule`
          representing the free module of which ``self`` is a basis

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')
            sage: e.module()
            Rank-3 free module M over the Integer Ring
            sage: e.module() is M
            True
        """
    def dual_basis(self):
        """
        Return the basis dual to ``self``.

        OUTPUT:

        - instance of :class:`FreeModuleCoBasis` representing the dual of
          ``self``

        EXAMPLES:

        Dual basis on a rank-3 free module::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M', start_index=1)
            sage: e = M.basis('e') ; e
            Basis (e_1,e_2,e_3) on the Rank-3 free module M over the Integer Ring
            sage: f = e.dual_basis() ; f
            Dual basis (e^1,e^2,e^3) on the Rank-3 free module M over the Integer Ring

        Let us check that the elements of f are elements of the dual of M::

            sage: f[1] in M.dual()
            True
            sage: f[1]
            Linear form e^1 on the Rank-3 free module M over the Integer Ring

        and that f is indeed the dual of e::

            sage: f[1](e[1]), f[1](e[2]), f[1](e[3])
            (1, 0, 0)
            sage: f[2](e[1]), f[2](e[2]), f[2](e[3])
            (0, 1, 0)
            sage: f[3](e[1]), f[3](e[2]), f[3](e[3])
            (0, 0, 1)
        """
    def new_basis(self, change_of_basis, symbol, latex_symbol=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Define a new module basis from ``self``.

        The new basis is defined by means of a module automorphism.

        INPUT:

        - ``change_of_basis`` -- instance of
          :class:`~sage.tensor.modules.free_module_automorphism.FreeModuleAutomorphism`
          describing the automorphism `P` that relates the current basis
          `(e_i)` (described by ``self``) to the new basis `(n_i)` according
          to `n_i = P(e_i)`
        - ``symbol`` -- either a string, to be used as a common base for the
          symbols of the elements of the basis, or a tuple of strings,
          representing the individual symbols of the elements of the basis
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the elements of the basis,
          or a tuple of strings, representing the individual LaTeX symbols of
          the elements of the basis; if ``None``, ``symbol`` is used in place
          of ``latex_symbol``
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices labelling
          the elements of the basis; if ``None``, the indices will be generated
          as integers within the range declared on the free module on which
          ``self`` is defined
        - ``latex_indices`` -- (default: ``None``) tuple of strings
          representing the indices for the LaTeX symbols of the elements of the
          basis; if ``None``, ``indices`` is used instead
        - ``symbol_dual`` -- (default: ``None``) same as ``symbol`` but for the
          dual basis; if ``None``, ``symbol`` must be a string and is used
          for the common base of the symbols of the elements of the dual basis
        - ``latex_symbol_dual`` -- (default: ``None``) same as ``latex_symbol``
          but for the dual basis

        OUTPUT:

        - the new basis `(n_i)`, as an instance of :class:`FreeModuleBasis`

        EXAMPLES:

        Change of basis on a vector space of dimension 2::

            sage: M = FiniteRankFreeModule(QQ, 2, name='M', start_index=1)
            sage: e = M.basis('e')
            sage: a = M.automorphism()
            sage: a[:] = [[1, 2], [-1, 3]]
            sage: f = e.new_basis(a, 'f') ; f
            Basis (f_1,f_2) on the 2-dimensional vector space M over the
             Rational Field
            sage: f[1].display()
            f_1 = e_1 - e_2
            sage: f[2].display()
            f_2 = 2 e_1 + 3 e_2
            sage: e[1].display(f)
            e_1 = 3/5 f_1 + 1/5 f_2
            sage: e[2].display(f)
            e_2 = -2/5 f_1 + 1/5 f_2

        Use of some keyword arguments::

            sage: b = e.new_basis(a, 'b', indices=('x', 'y'),
            ....:                 symbol_dual=('A', 'B'))
            sage: b
            Basis (b_x,b_y) on the 2-dimensional vector space M over the
             Rational Field
            sage: b.dual_basis()
            Dual basis (A,B) on the 2-dimensional vector space M over the
             Rational Field
        """
