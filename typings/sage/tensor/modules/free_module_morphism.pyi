from sage.categories.morphism import Morphism as Morphism
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer import Integer as Integer
from sage.tensor.modules.free_module_element import FiniteRankFreeModuleElement as FiniteRankFreeModuleElement

class FiniteRankFreeModuleMorphism(Morphism):
    """
    Homomorphism between free modules of finite rank over a commutative ring.

    An instance of this class is a homomorphism

    .. MATH::

        \\phi:\\ M \\longrightarrow N,

    where `M` and `N` are two free modules of finite rank over the same
    commutative ring `R`.

    This is a Sage *element* class, the corresponding *parent* class being
    :class:`~sage.tensor.modules.free_module_homset.FreeModuleHomset`.

    For the special case of endomorphisms (`M=N`), use the subclass
    :class:`FiniteRankFreeModuleEndomorphism`.

    INPUT:

    - ``parent`` -- Hom-set Hom(M,N) to which the homomorphism belongs
    - ``matrix_rep`` -- matrix representation of the homomorphism with
      respect to the bases ``bases``; this entry can actually
      be any material from which a matrix of size rank(N)*rank(M) of
      elements of `R` can be constructed; the *columns* of the matrix give
      the images of the basis of `M` (see the convention in the example below)
    - ``bases`` -- (default: ``None``) pair (basis_M, basis_N) defining the
      matrix representation, basis_M being a basis of module `M` and
      basis_N a basis of module `N` ; if None the pair formed by the
      default bases of each module is assumed.
    - ``name`` -- (default: ``None``) string; name given to the homomorphism
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      homomorphism. If ``None``, ``name`` will be used.

    EXAMPLES:

    A homomorphism between two free modules over `\\ZZ` is constructed
    as an element of the corresponding hom-set, by means of the function
    ``__call__``::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
        sage: e = M.basis('e') ; f = N.basis('f')
        sage: H = Hom(M,N) ; H
        Set of Morphisms from Rank-3 free module M over the Integer Ring
         to Rank-2 free module N over the Integer Ring
         in Category of finite dimensional modules over Integer Ring
        sage: phi = H([[2,-1,3], [1,0,-4]], name='phi', latex_name=r'\\phi') ; phi
        Generic morphism:
          From: Rank-3 free module M over the Integer Ring
          To:   Rank-2 free module N over the Integer Ring

    Since no bases have been specified in the argument list, the provided
    matrix is relative to the default bases of modules M and N, so that
    the above is equivalent to::

        sage: phi = H([[2,-1,3], [1,0,-4]], bases=(e,f), name='phi',
        ....:         latex_name=r'\\phi') ; phi
        Generic morphism:
          From: Rank-3 free module M over the Integer Ring
          To:   Rank-2 free module N over the Integer Ring

    An alternative way to construct a homomorphism is to call the method
    :meth:`~sage.tensor.modules.finite_rank_free_module.FiniteRankFreeModule.hom`
    on the domain::

        sage: phi = M.hom(N, [[2,-1,3], [1,0,-4]], bases=(e,f), name='phi',
        ....:             latex_name=r'\\phi') ; phi
        Generic morphism:
          From: Rank-3 free module M over the Integer Ring
          To:   Rank-2 free module N over the Integer Ring

    The parent of a homomorphism is of course the corresponding hom-set::

        sage: phi.parent() is H
        True
        sage: phi.parent() is Hom(M,N)
        True

    Due to Sage's category scheme, the actual class of the homomorphism ``phi``
    is a derived class of :class:`FiniteRankFreeModuleMorphism`::

        sage: type(phi)
        <class 'sage.tensor.modules.free_module_homset.FreeModuleHomset_with_category_with_equality_by_id.element_class'>
        sage: isinstance(phi, sage.tensor.modules.free_module_morphism.FiniteRankFreeModuleMorphism)
        True

    The domain and codomain of the homomorphism are returned respectively by
    the methods ``domain()`` and ``codomain()``, which are implemented as
    Sage's constant functions::

        sage: phi.domain()
        Rank-3 free module M over the Integer Ring
        sage: phi.codomain()
        Rank-2 free module N over the Integer Ring
        sage: type(phi.domain)
        <... 'sage.misc.constant_function.ConstantFunction'>

    The matrix of the homomorphism with respect to a pair of bases is
    returned by the method :meth:`matrix`::

        sage: phi.matrix(e,f)
        [ 2 -1  3]
        [ 1  0 -4]

    The convention is that the columns of this matrix give the components of
    the images of the elements of basis ``e`` w.r.t basis ``f``::

        sage: phi(e[0]).display()
        phi(e_0) = 2 f_0 + f_1
        sage: phi(e[1]).display()
        phi(e_1) = -f_0
        sage: phi(e[2]).display()
        phi(e_2) = 3 f_0 - 4 f_1

    Test of the module homomorphism laws::

        sage: phi(M.zero()) == N.zero()
        True
        sage: u = M([1,2,3], basis=e, name='u') ; u.display()
        u = e_0 + 2 e_1 + 3 e_2
        sage: v = M([-2,1,4], basis=e, name='v') ; v.display()
        v = -2 e_0 + e_1 + 4 e_2
        sage: phi(u).display()
        phi(u) = 9 f_0 - 11 f_1
        sage: phi(v).display()
        phi(v) = 7 f_0 - 18 f_1
        sage: phi(3*u + v).display()
        34 f_0 - 51 f_1
        sage: phi(3*u + v) == 3*phi(u) + phi(v)
        True
    """
    def __init__(self, parent, matrix_rep, bases=None, name=None, latex_name=None, is_identity: bool = False) -> None:
        """
        TESTS:

        Generic homomorphism::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleMorphism
            sage: phi = FiniteRankFreeModuleMorphism(Hom(M,N), [[1,0,-3], [2,1,4]],
            ....:                                    name='phi', latex_name=r'\\phi')
            sage: phi
            Generic morphism:
              From: Rank-3 free module M over the Integer Ring
              To:   Rank-2 free module N over the Integer Ring
            sage: phi.matrix(e,f)
            [ 1  0 -3]
            [ 2  1  4]
            sage: latex(phi)
            \\phi
        """
    def __eq__(self, other):
        '''
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- a free module morphism (or 0)

        OUTPUT: ``True`` if ``self`` is equal to ``other`` and ``False`` otherwise

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: N = FiniteRankFreeModule(ZZ, 2, name=\'N\')
            sage: e = M.basis(\'e\') ; f = N.basis(\'f\')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]], name=\'phi\',
            ....:             latex_name=r\'\\phi\')
            sage: psi = M.hom(N, [[-1,2,0], [5,1,2]])
            sage: phi.__eq__(psi)
            True
            sage: phi == psi
            True
            sage: phi.__eq__(phi)
            True
            sage: phi.__eq__(+phi)
            True
            sage: psi = M.hom(N, [[1,1,0], [4,1,3]])
            sage: phi.__eq__(psi)
            False
            sage: phi.__eq__(-phi)
            False

        Comparison of homomorphisms defined on different bases::

            sage: a = M.automorphism() ; a[0,2], a[1,0], a[2,1] = 1, -1, -1
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: psi = M.hom(N, [[-2,0,-1], [-1,-2, 5]], bases=(ep,f))
            sage: phi.__eq__(psi)
            True
            sage: phi.matrix(e,f) == psi.matrix(e,f)  # check
            True

        Comparison of homomorphisms having the same matrix but defined on
        different modules::

            sage: N1 = FiniteRankFreeModule(ZZ, 2, name=\'N1\')
            sage: f1 = N1.basis(\'f\')
            sage: phi1 = M.hom(N1, [[-1,2,0], [5,1,2]])
            sage: phi.matrix() == phi1.matrix() # same matrix in the default bases
            True
            sage: phi.__eq__(phi1)
            False

        Comparison to zero::

            sage: phi.__eq__(0)
            False
            sage: phi = M.hom(N, 0)
            sage: phi.__eq__(0)
            True
            sage: phi == 0
            True
            sage: phi.__eq__(Hom(M,N).zero())
            True
        '''
    def __ne__(self, other):
        """
        Inequality operator.

        INPUT:

        - ``other`` -- a free module morphism (or 0)

        OUTPUT:

        - ``True`` if ``self`` is different from ``other`` and ``False``
          otherwise

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]], name='phi',
            ....:             latex_name=r'\\phi')
            sage: psi = M.hom(N, [[-1,2,0], [5,1,2]])
            sage: phi.__ne__(psi)
            False
            sage: psi = M.hom(N, [[1,1,0], [4,1,3]])
            sage: phi.__ne__(psi)
            True
            sage: phi != psi
            True
            sage: phi.__ne__('junk')
            True
            sage: Hom(M,N).zero().__ne__(0)
            False
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if ``self`` is nonzero and ``False`` otherwise.

        This method is called by self.is_zero().

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: phi = M.hom(N, [[2,-1,3], [1,0,-4]])
            sage: bool(phi)
            True
            sage: phi.is_zero() # indirect doctest
            False
            sage: phi = M.hom(N, 0)
            sage: bool(phi)
            False
            sage: phi.is_zero() # indirect doctest
            True
            sage: bool(Hom(M,N).zero())
            False
        """
    def __pos__(self):
        """
        Unary plus operator.

        OUTPUT: an exact copy of ``self``

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]], name='phi',
            ....:             latex_name=r'\\phi')
            sage: s = phi.__pos__() ; s
            Generic morphism:
              From: Rank-3 free module M over the Integer Ring
              To:   Rank-2 free module N over the Integer Ring
            sage: s == +phi
            True
            sage: s == phi
            True
            sage: s is phi
            False
        """
    def __neg__(self):
        """
        Unary minus operator.

        OUTPUT: the homomorphism `-f`, where `f` is ``self``

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]], name='phi',
            ....:             latex_name=r'\\phi')
            sage: s = phi.__neg__() ; s
            Generic morphism:
              From: Rank-3 free module M over the Integer Ring
              To:   Rank-2 free module N over the Integer Ring
            sage: s == -phi
            True
            sage: s.matrix()
            [ 1 -2  0]
            [-5 -1 -2]
            sage: s.matrix() == -phi.matrix()
            True
        """
    def is_injective(self):
        """
        Determine whether ``self`` is injective.

        OUTPUT:

        - ``True`` if ``self`` is an injective homomorphism and ``False``
          otherwise

        EXAMPLES:

        Homomorphisms between two `\\ZZ`-modules::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]])
            sage: phi.matrix(e,f)
            [-1  2  0]
            [ 5  1  2]
            sage: phi.is_injective()
            False

        Indeed, phi has a non trivial kernel::

            sage: phi(4*e[0] + 2*e[1] - 11*e[2]).display()
            0

        An injective homomorphism::

            sage: psi = N.hom(M, [[1,-1], [0,3], [4,-5]])
            sage: psi.matrix(f,e)
            [ 1 -1]
            [ 0  3]
            [ 4 -5]
            sage: psi.is_injective()
            True

        Of course, the identity endomorphism is injective::

            sage: End(M).one().is_injective()
            True
            sage: End(N).one().is_injective()
            True
        """
    def is_surjective(self):
        """
        Determine whether ``self`` is surjective.

        OUTPUT:

        - ``True`` if ``self`` is a surjective homomorphism and ``False``
          otherwise

        EXAMPLES:

        This method has not been implemented yet::

            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: N = FiniteRankFreeModule(ZZ, 2, name='N')
            sage: e = M.basis('e') ; f = N.basis('f')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]])
            sage: phi.is_surjective()
            Traceback (most recent call last):
            ...
            NotImplementedError: FiniteRankFreeModuleMorphism.is_surjective()
             has not been implemented yet

        except for the identity endomorphism (!)::

            sage: End(M).one().is_surjective()
            True
            sage: End(N).one().is_surjective()
            True
        """
    def is_identity(self):
        '''
        Check whether ``self`` is the identity morphism.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 2, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: phi = M.endomorphism([[1,0], [0,1]])
            sage: phi.is_identity()
            True
            sage: (phi+phi).is_identity()
            False
            sage: End(M).zero().is_identity()
            False
            sage: a = M.automorphism() ; a[0,1], a[1,0] = 1, -1
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,0], [0,1]], basis=ep)
            sage: phi.is_identity()
            True

        Example illustrating that the identity can be constructed from a
        matrix that is not the identity one, provided that it is relative to
        different bases::

            sage: phi = M.hom(M, [[0,1], [-1,0]], bases=(ep,e))
            sage: phi.is_identity()
            True

        Of course, if we ask for the matrix in a single basis, it is the
        identity matrix::

            sage: phi.matrix(e)
            [1 0]
            [0 1]
            sage: phi.matrix(ep)
            [1 0]
            [0 1]
        '''
    def matrix(self, basis1=None, basis2=None):
        '''
        Return the matrix of ``self`` w.r.t to a pair of bases.

        If the matrix is not known already, it is computed from the matrix in
        another pair of bases by means of the change-of-basis formula.

        INPUT:

        - ``basis1`` -- (default: ``None``) basis of the domain of ``self``; if
          none is provided, the domain\'s default basis is assumed
        - ``basis2`` -- (default: ``None``) basis of the codomain of ``self``;
          if none is provided, ``basis2`` is set to ``basis1`` if ``self`` is
          an endomorphism, otherwise, ``basis2`` is set to the codomain\'s
          default basis.

        OUTPUT:

        - the matrix representing the homomorphism ``self`` w.r.t
          to bases ``basis1`` and ``basis2``; more precisely, the columns of
          this matrix are formed by the components w.r.t. ``basis2`` of
          the images of the elements of ``basis1``.

        EXAMPLES:

        Matrix of a homomorphism between two `\\ZZ`-modules::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: N = FiniteRankFreeModule(ZZ, 2, name=\'N\')
            sage: e = M.basis(\'e\') ; f = N.basis(\'f\')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]])
            sage: phi.matrix()     # default bases
            [-1  2  0]
            [ 5  1  2]
            sage: phi.matrix(e, f)  # given bases
            [-1  2  0]
            [ 5  1  2]
            sage: type(phi.matrix())                                                    # needs sage.libs.flint
            <class \'sage.matrix.matrix_integer_dense.Matrix_integer_dense\'>

        Matrix in bases different from those in which the homomorphism has
        been defined::

            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: b = N.automorphism(matrix=[[3,5],[4,7]], basis=f)
            sage: fp = f.new_basis(b, \'fp\', latex_symbol="f\'")
            sage: phi.matrix(ep, fp)
            [ 32  -1 -12]
            [-19   1   8]

        Check of the change-of-basis formula::

            sage: phi.matrix(ep, fp) == (b^(-1)).matrix(f) * phi.matrix(e,f) * a.matrix(e)
            True

        Single change of basis::

            sage: phi.matrix(ep, f)
            [ 1  2  4]
            [-5  3  8]
            sage: phi.matrix(ep,f) == phi.matrix(e,f) * a.matrix(e)
            True
            sage: phi.matrix(e, fp)
            [-32   9 -10]
            [ 19  -5   6]
            sage: phi.matrix(e, fp) == (b^(-1)).matrix(f) * phi.matrix(e,f)
            True

        Matrix of an endomorphism::

            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.matrix(ep)
            [1 2 3]
            [4 5 6]
            [7 8 9]
            sage: phi.matrix(ep,ep)  # same as above
            [1 2 3]
            [4 5 6]
            [7 8 9]
            sage: phi.matrix()  # matrix w.r.t to the module\'s default basis
            [  1  -3   1]
            [-18  39 -18]
            [-25  54 -25]
        '''
    def display(self, basis1=None, basis2=None):
        '''
        Display ``self`` as a matrix w.r.t to a pair of bases.

        If the matrix is not known already, it is computed from the matrix in
        another pair of bases by means of the change-of-basis formula.

        INPUT:

        - ``basis1`` -- (default: ``None``) basis of the domain of ``self``; if
          none is provided, the domain\'s default basis is assumed
        - ``basis2`` -- (default: ``None``) basis of the codomain of ``self``;
          if none is provided, ``basis2`` is set to ``basis1`` if ``self`` is
          an endomorphism, otherwise, ``basis2`` is set to the codomain\'s
          default basis.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: N = FiniteRankFreeModule(ZZ, 2, name=\'N\')
            sage: e = M.basis(\'e\'); f = N.basis(\'f\')
            sage: phi = M.hom(N, [[-1,2,0], [5,1,2]])
            sage: phi.display()     # default bases
                e_0 e_1 e_2
            f_0⎛ -1   2   0⎞
            f_1⎝  5   1   2⎠
            sage: phi.display(e, f)  # given bases
                e_0 e_1 e_2
            f_0⎛ -1   2   0⎞
            f_1⎝  5   1   2⎠

        Matrix of an endomorphism::

            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.display(ep)
                 ep_0 ep_1 ep_2
            ep_0⎛   1    2    3⎞
            ep_1⎜   4    5    6⎟
            ep_2⎝   7    8    9⎠
            sage: phi.display(ep, ep)  # same as above
                 ep_0 ep_1 ep_2
            ep_0⎛   1    2    3⎞
            ep_1⎜   4    5    6⎟
            ep_2⎝   7    8    9⎠
            sage: phi.display()  # matrix w.r.t to the module\'s default basis
                e_0 e_1 e_2
            e_0⎛  1  -3   1⎞
            e_1⎜-18  39 -18⎟
            e_2⎝-25  54 -25⎠
        '''

class FiniteRankFreeModuleEndomorphism(FiniteRankFreeModuleMorphism):
    """
    Endomorphism of a free module of finite rank over a commutative ring.

    An instance of this class is an endomorphism

    .. MATH::

        \\phi:\\ M \\longrightarrow M,

    where `M` is a free module of finite rank over a commutative ring `R`.

    This is a Sage *element* class, the corresponding *parent* class being
    :class:`~sage.tensor.modules.free_module_homset.FreeModuleEndset`.

    INPUT:

    - ``parent`` -- Hom-set Hom(M,M) to which the endomorphism belongs
    - ``matrix_rep`` -- matrix representation of the endomorphism with
      respect to the basis ``bases``; this entry can actually
      be any material from which a matrix of size rank(N)*rank(M) of
      elements of `R` can be constructed; the *columns* of the matrix give
      the images of the basis of `M` (see the convention in the example below)
    - ``bases`` -- (default: ``None``) pair ``(basis_domain, basis_codomain)``
      defining the matrix representation, ``basis_domain`` and ``basis_codomain``
      being two bases (typically the same) of the same module `M`; if ``None``,
      the default basis of `M` is used for both.
    - ``name`` -- (default: ``None``) string; name given to the endomorphism
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      endomorphism. If ``None``, ``name`` will be used.
    - ``is_identity`` -- boolean (default: ``False``); determines whether the
      constructed object is the identity endomorphism. If set to ``True``,
      then the entry ``matrix_rep`` is not used.

    EXAMPLES:

    The identity endomorphism::

        sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
        sage: e = M.basis('e')
        sage: Id = End(M).one(); Id
        Identity endomorphism of Rank-3 free module M over the Integer Ring
        sage: Id.parent()
        Set of Morphisms from Rank-3 free module M over the Integer Ring
         to Rank-3 free module M over the Integer Ring
         in Category of finite dimensional modules over Integer Ring
        sage: Id.parent() is End(M)
        True

    The matrix of ``Id`` with respect to the basis ``e`` is of course the identity
    matrix::

        sage: Id.matrix(e)
        [1 0 0]
        [0 1 0]
        [0 0 1]

    The identity acting on a module element::

        sage: v = M([-2,1,4], basis=e, name='v'); v.display()
        v = -2 e_0 + e_1 + 4 e_2
        sage: Id(v) is v
        True
    """
    def __init__(self, parent, matrix_rep, bases=None, name=None, latex_name=None, is_identity: bool = False) -> None:
        """
        TESTS::

            sage: from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleEndomorphism
            sage: M = FiniteRankFreeModule(ZZ, 3, name='M')
            sage: e = M.basis('e')

        Generic endomorphism::

            sage: phi = FiniteRankFreeModuleEndomorphism(End(M),
            ....:                                        [[1,0,-3], [2,1,4], [7,8,9]],
            ....:                                        name='phi', latex_name=r'\\phi')
            sage: phi
            Generic endomorphism of Rank-3 free module M over the Integer Ring

        Identity endomorphism::

            sage: phi = FiniteRankFreeModuleEndomorphism(End(M), 'whatever',
            ....:                                        is_identity=True)
            sage: phi
            Identity endomorphism of Rank-3 free module M over the Integer Ring
            sage: phi.matrix(e)
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: latex(phi)
            \\mathrm{Id}
        """
    @lazy_attribute
    def characteristic_polynomial(self):
        '''
        Return the characteristic polynomial of ``self``.

        :meth:`characteristic_polynomial` and :meth:`charpoly` are the same method.

        INPUT:

        - ``var`` -- string (default: ``\'x\'``); a variable name

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.matrix(e)
            [  1  -3   1]
            [-18  39 -18]
            [-25  54 -25]
            sage: phi.characteristic_polynomial()
            x^3 - 15*x^2 - 18*x
            sage: phi.charpoly()
            x^3 - 15*x^2 - 18*x
            sage: phi.charpoly(\'T\')
            T^3 - 15*T^2 - 18*T
        '''
    charpoly = characteristic_polynomial
    @lazy_attribute
    def det(self):
        '''
        Return the determinant of ``self``.

        OUTPUT:

        - element of the base ring of the modules on which ``self`` is defined,
          equal to the determinant of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.matrix(e)
            [  1  -3   1]
            [-18  39 -18]
            [-25  54 -25]
            sage: phi.det()
            0
            sage: det(phi)
            0
        '''
    determinant = det
    @lazy_attribute
    def fcp(self):
        '''
        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- string (default: ``\'x\'``); a variable name

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.matrix(e)
            [  1  -3   1]
            [-18  39 -18]
            [-25  54 -25]
            sage: phi.fcp()                                                             # needs sage.libs.pari
            x * (x^2 - 15*x - 18)
            sage: phi.fcp(\'T\')                                                          # needs sage.libs.pari
            T * (T^2 - 15*T - 18)
        '''
    @lazy_attribute
    def minimal_polynomial(self):
        '''
        Return the minimal polynomial of ``self``.

        :meth:`minimal_polynomial` and :meth:`minpoly` are the same method.

        INPUT:

        - ``var`` -- string (default: ``\'x\'``); a variable name

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.matrix(e)
            [  1  -3   1]
            [-18  39 -18]
            [-25  54 -25]
            sage: phi.minpoly()                                                         # needs sage.libs.pari
            x^3 - 15*x^2 - 18*x
            sage: phi.minimal_polynomial()                                              # needs sage.libs.pari
            x^3 - 15*x^2 - 18*x
            sage: phi.minimal_polynomial(\'T\')                                           # needs sage.libs.pari
            T^3 - 15*T^2 - 18*T
        '''
    minpoly = minimal_polynomial
    @lazy_attribute
    def trace(self):
        '''
        Return the trace of ``self``.

        OUTPUT:

        - element of the base ring of the modules on which ``self`` is defined,
          equal to the trace of ``self``.

        EXAMPLES::

            sage: M = FiniteRankFreeModule(ZZ, 3, name=\'M\')
            sage: e = M.basis(\'e\')
            sage: a = M.automorphism(matrix=[[-1,0,0],[0,1,2],[0,1,3]], basis=e)
            sage: ep = e.new_basis(a, \'ep\', latex_symbol="e\'")
            sage: phi = M.endomorphism([[1,2,3], [4,5,6], [7,8,9]], basis=ep)
            sage: phi.matrix(e)
            [  1  -3   1]
            [-18  39 -18]
            [-25  54 -25]
            sage: phi.trace()
            15
            sage: id = M.identity_map()
            sage: id.trace()
            3
        '''
