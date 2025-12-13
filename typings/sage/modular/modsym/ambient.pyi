from . import boundary as boundary, element as element, heilbronn as heilbronn, modsym as modsym, modular_symbols as modular_symbols, p1list as p1list, relation_matrix as relation_matrix, subspace as subspace
from .space import ModularSymbolsSpace as ModularSymbolsSpace
from sage.arith.misc import crt as crt, divisors as divisors, is_prime as is_prime, number_of_divisors as number_of_divisors
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.verbose import verbose as verbose
from sage.modular.arithgroup.arithgroup_element import M2Z as M2Z
from sage.modular.cusps import Cusp as Cusp
from sage.modular.dirichlet import DirichletCharacter as DirichletCharacter, TrivialCharacter as TrivialCharacter
from sage.modular.hecke.ambient_module import AmbientHeckeModule as AmbientHeckeModule
from sage.modular.modsym.apply import apply_to_monomial as apply_to_monomial
from sage.modular.modsym.manin_symbol import ManinSymbol as ManinSymbol
from sage.modular.modsym.manin_symbol_list import ManinSymbolList_character as ManinSymbolList_character, ManinSymbolList_gamma0 as ManinSymbolList_gamma0, ManinSymbolList_gamma1 as ManinSymbolList_gamma1, ManinSymbolList_gamma_h as ManinSymbolList_gamma_h
from sage.modules.free_module import FreeModule_generic as FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement as FreeModuleElement
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.rational_field import QQ as QQ
from sage.structure.factorization import Factorization as Factorization
from sage.structure.formal_sum import FormalSum as FormalSum

class ModularSymbolsAmbient(ModularSymbolsSpace, AmbientHeckeModule):
    """
    An ambient space of modular symbols for a congruence subgroup of
    `SL_2(\\ZZ)`.

    This class is an abstract base class, so only derived classes
    should be instantiated.

    INPUT:

    - ``weight`` -- integer
    - ``group`` -- a congruence subgroup
    - ``sign`` -- integer; either -1, 0, or 1
    - ``base_ring`` -- a commutative ring
    - ``custom_init`` -- a function that is called with ``self`` as input
      before any computations are done using self; this could be used
      to set a custom modular symbols presentation

    TESTS::

        sage: ModularSymbols(11,2) == ModularSymbols(11,2)
        True
        sage: ModularSymbols(11,2) == ModularSymbols(11,4)
        False
        sage: ModularSymbols(11,2) != ModularSymbols(11,2)
        False
        sage: ModularSymbols(11,2) != ModularSymbols(11,4)
        True
        sage: hash(ModularSymbols(11,2)) != hash(ModularSymbols(11,4))
        True
    """
    def __init__(self, group, weight, sign, base_ring, character=None, custom_init=None, category=None) -> None:
        """
        Initialize a space of modular symbols.

        INPUT:

        - ``weight`` -- integer

        - ``group`` -- a congruence subgroup

        - ``sign`` -- integer, either -1, 0, or 1

        - ``base_ring`` -- a commutative ring

        EXAMPLES::

            sage: ModularSymbols(2,2)
            Modular Symbols space of dimension 1 for Gamma_0(2) of weight 2 with sign 0 over Rational Field
        """
    def new_submodule(self, p=None):
        """
        Return the new or `p`-new submodule of this modular symbols ambient space.

        INPUT:

        - ``p`` -- (default: ``None``) if not ``None``, return only
          the `p`-new submodule

        OUTPUT: the new or `p`-new submodule of this modular symbols ambient space

        EXAMPLES::

            sage: ModularSymbols(100).new_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 31 for Gamma_0(100) of weight 2 with sign 0 over Rational Field
            sage: ModularSymbols(389).new_submodule()
            Modular Symbols space of dimension 65 for Gamma_0(389) of weight 2 with sign 0 over Rational Field
        """
    def manin_symbols(self) -> None:
        """
        Return the list of Manin symbols for this modular symbols ambient space.

        EXAMPLES::

            sage: ModularSymbols(11,2).manin_symbols()
            Manin Symbol List of weight 2 for Gamma0(11)
        """
    def manin_generators(self):
        """
        Return list of all Manin symbols for this space. These are the
        generators in the presentation of this space by Manin symbols.

        EXAMPLES::

            sage: M = ModularSymbols(2,2)
            sage: M.manin_generators()
            [(0,1), (1,0), (1,1)]

        ::

            sage: M = ModularSymbols(1,6)
            sage: M.manin_generators()
            [[Y^4,(0,0)], [X*Y^3,(0,0)], [X^2*Y^2,(0,0)], [X^3*Y,(0,0)], [X^4,(0,0)]]
        """
    def manin_basis(self):
        """
        Return a list of indices into the list of Manin generators (see
        ``self.manin_generators()``) such that those symbols
        form a basis for the quotient of the `\\QQ`-vector
        space spanned by Manin symbols modulo the relations.

        EXAMPLES::

            sage: M = ModularSymbols(2,2)
            sage: M.manin_basis()
            [1]
            sage: [M.manin_generators()[i] for i in M.manin_basis()]
            [(1,0)]
            sage: M = ModularSymbols(6,2)
            sage: M.manin_basis()
            [1, 10, 11]
            sage: [M.manin_generators()[i] for i in M.manin_basis()]
            [(1,0), (3,1), (3,2)]
        """
    def p1list(self):
        """
        Return a P1list of the level of this modular symbol space.

        EXAMPLES::

            sage: ModularSymbols(11,2).p1list()
            The projective line over the integers modulo 11
        """
    def compute_presentation(self) -> None:
        """
        Compute and cache the presentation of this space.

        EXAMPLES::

            sage: ModularSymbols(11,2).compute_presentation() # no output
        """
    def manin_gens_to_basis(self):
        """
        Return the matrix expressing the manin symbol generators in terms of the basis.

        EXAMPLES::

            sage: ModularSymbols(11,2).manin_gens_to_basis()
            [-1  0  0]
            [ 1  0  0]
            [ 0  0  0]
            [ 0  0  1]
            [ 0 -1  1]
            [ 0 -1  0]
            [ 0  0 -1]
            [ 0  0 -1]
            [ 0  1 -1]
            [ 0  1  0]
            [ 0  0  1]
            [ 0  0  0]
        """
    def change_ring(self, R):
        """
        Change the base ring to R.

        EXAMPLES::

            sage: ModularSymbols(Gamma1(13), 2).change_ring(GF(17))
            Modular Symbols space of dimension 15 for Gamma_1(13) of weight 2 with sign 0 over Finite Field of size 17
            sage: M = ModularSymbols(DirichletGroup(5).0, 7); MM=M.change_ring(CyclotomicField(8)); MM
            Modular Symbols space of dimension 6 and level 5, weight 7, character [zeta8^2], sign 0, over Cyclotomic Field of order 8 and degree 4
            sage: MM.change_ring(CyclotomicField(4)) == M
            True
            sage: M.change_ring(QQ)
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce zeta4 to a rational

        Similarly with :meth:`base_extend`::

            sage: M = ModularSymbols(DirichletGroup(5).0, 7); MM = M.base_extend(CyclotomicField(8)); MM
            Modular Symbols space of dimension 6 and level 5, weight 7, character [zeta8^2], sign 0, over Cyclotomic Field of order 8 and degree 4
            sage: MM.base_extend(CyclotomicField(4))
            Traceback (most recent call last):
            ...
            TypeError: Base extension of self (over 'Cyclotomic Field of order 8 and degree 4') to ring 'Cyclotomic Field of order 4 and degree 2' not defined.
        """
    def manin_symbol(self, x, check: bool = True):
        """
        Construct a Manin Symbol from the given data.

        INPUT:

        - ``x`` -- list; either `[u,v]` or `[i,u,v]`, where `0\\le
          i\\le k-2` where `k` is the weight, and `u`,`v` are integers
          defining a valid element of `\\mathbb{P}^1(N)`, where `N` is
          the level

        OUTPUT:

        (ManinSymbol) the Manin Symbol associated to `[i;(u,v)]`, with
        `i=0` if not supplied, corresponding to the monomial symbol
        `[X^i*Y^{k-2-i}, (u,v)]`.

        EXAMPLES::

            sage: M = ModularSymbols(11,4,1)
            sage: M.manin_symbol([2,5,6])
            -2/3*[X^2,(1,6)] + 5/3*[X^2,(1,9)]
        """
    def modular_symbol(self, x, check: bool = True):
        """
        Create a modular symbol in this space.

        INPUT:

        - ``x`` -- list of either 2 or 3 entries:

            - 2 entries: `[\\alpha, \\beta]` where `\\alpha` and `\\beta`
              are cusps;

            - 3 entries: `[i, \\alpha, \\beta]` where `0\\le i\\le k-2`
              and `\\alpha` and `\\beta` are cusps;

        - ``check`` -- boolean (default: ``True``); flag that determines
          whether the input ``x`` needs processing: use check=False
          for efficiency if the input ``x`` is a list of length 3 whose
          first entry is an Integer, and whose second and third
          entries are Cusps (see examples).

        OUTPUT:

        (Modular Symbol) The modular symbol `Y^{k-2}\\{\\alpha,
        \\beta\\}`. or `X^i Y^{k-2-i}\\{\\alpha,\\beta\\}`.

        EXAMPLES::

            sage: set_modsym_print_mode('modular')
            sage: M = ModularSymbols(11)
            sage: M.modular_symbol([2/11, oo])
            -{-1/9, 0}
            sage: M.1
            {-1/8, 0}
            sage: M.modular_symbol([-1/8, 0])
            {-1/8, 0}
            sage: M.modular_symbol([0, -1/8, 0])
            {-1/8, 0}
            sage: M.modular_symbol([10, -1/8, 0])
            Traceback (most recent call last):
            ...
            ValueError: The first entry of the tuple (=[10, -1/8, 0]) must be an integer between 0 and k-2 (=0).

        ::

            sage: N = ModularSymbols(6,4)
            sage: set_modsym_print_mode('manin')
            sage: N([1,Cusp(-1/4),Cusp(0)])
            17/2*[X^2,(2,3)] - 9/2*[X^2,(2,5)] + 15/2*[X^2,(3,1)] - 15/2*[X^2,(3,2)]
            sage: N([1,Cusp(-1/2),Cusp(0)])
            1/2*[X^2,(2,3)] + 3/2*[X^2,(2,5)] + 3/2*[X^2,(3,1)] - 3/2*[X^2,(3,2)]

        Use check=False for efficiency if the input x is a list of length 3
        whose first entry is an Integer, and whose second and third entries
        are cusps::

            sage: M.modular_symbol([0, Cusp(2/11), Cusp(oo)], check=False)
            -(1,9)

        ::

            sage: set_modsym_print_mode()   # return to default.
        """
    def modular_symbol_sum(self, x, check: bool = True):
        """
        Construct a modular symbol sum.

        INPUT:

        - ``x`` -- list; `[f, \\alpha, \\beta]` where `f =
          \\sum_{i=0}^{k-2} a_i X^i Y^{k-2-i}` is a homogeneous
          polynomial over `\\ZZ` of degree `k` and `\\alpha` and `\\beta`
          are cusps.

        - ``check`` -- boolean (default: ``True``); if ``True`` check the
          validity of the input tuple ``x``

        OUTPUT:

        The sum `\\sum_{i=0}^{k-2} a_i [ i, \\alpha, \\beta ]` as an
        element of this modular symbol space.

        EXAMPLES::

            sage: M = ModularSymbols(11,4)
            sage: R.<X,Y>=QQ[]
            sage: M.modular_symbol_sum([X*Y,Cusp(0),Cusp(Infinity)])
            -3/14*[X^2,(1,6)] + 1/14*[X^2,(1,7)] - 1/14*[X^2,(1,8)] + 1/2*[X^2,(1,9)] - 2/7*[X^2,(1,10)]
        """
    def boundary_map(self):
        """
        Return the boundary map to the corresponding space of boundary modular
        symbols.

        EXAMPLES::

            sage: ModularSymbols(20,2).boundary_map()
            Hecke module morphism boundary map defined by the matrix
            [ 1 -1  0  0  0  0]
            [ 0  1 -1  0  0  0]
            [ 0  1  0 -1  0  0]
            [ 0  0  0 -1  1  0]
            [ 0  1  0 -1  0  0]
            [ 0  0  1 -1  0  0]
            [ 0  1  0  0  0 -1]
            Domain: Modular Symbols space of dimension 7 for Gamma_0(20) of weight ...
            Codomain: Space of Boundary Modular Symbols for Congruence Subgroup Gamma0(20) ...
            sage: type(ModularSymbols(20,2).boundary_map())
            <class 'sage.modular.hecke.morphism.HeckeModuleMorphism_matrix'>
        """
    def cusps(self):
        """
        Return the set of cusps for this modular symbols space.

        EXAMPLES::

            sage: ModularSymbols(20,2).cusps()
            [Infinity, 0, -1/4, 1/5, -1/2, 1/10]
        """
    def boundary_space(self) -> None:
        """
        Return the subspace of boundary modular symbols of this modular symbols ambient space.

        EXAMPLES::

            sage: M = ModularSymbols(20, 2)
            sage: B = M.boundary_space(); B
            Space of Boundary Modular Symbols for Congruence Subgroup Gamma0(20) of weight 2 over Rational Field
            sage: M.cusps()
            [Infinity, 0, -1/4, 1/5, -1/2, 1/10]
            sage: M.dimension()
            7
            sage: B.dimension()
            6
        """
    def cuspidal_submodule(self):
        """
        The cuspidal submodule of this modular symbols ambient space.

        EXAMPLES::

            sage: M = ModularSymbols(12,2,0,GF(5)) ; M
            Modular Symbols space of dimension 5 for Gamma_0(12) of weight 2 with sign 0 over Finite Field of size 5
            sage: M.cuspidal_submodule()
            Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 5 for Gamma_0(12) of weight 2 with sign 0 over Finite Field of size 5
            sage: ModularSymbols(1,24,-1).cuspidal_submodule()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 24 with sign -1 over Rational Field

        The cuspidal submodule of the cuspidal submodule is itself::

            sage: M = ModularSymbols(389)
            sage: S = M.cuspidal_submodule()
            sage: S.cuspidal_submodule() is S
            True
        """
    def rank(self):
        """
        Return the rank of this modular symbols ambient space.

        OUTPUT: integer; the rank of this space of modular symbols

        EXAMPLES::

            sage: M = ModularSymbols(389)
            sage: M.rank()
            65

        ::

            sage: ModularSymbols(11,sign=0).rank()
            3
            sage: ModularSymbols(100,sign=0).rank()
            31
            sage: ModularSymbols(22,sign=1).rank()
            5
            sage: ModularSymbols(1,12).rank()
            3
            sage: ModularSymbols(3,4).rank()
            2
            sage: ModularSymbols(8,6,sign=-1).rank()
            3
        """
    def eisenstein_submodule(self):
        """
        Return the Eisenstein submodule of this space of modular symbols.

        EXAMPLES::

            sage: ModularSymbols(20,2).eisenstein_submodule()
            Modular Symbols subspace of dimension 5 of Modular Symbols space of dimension 7 for Gamma_0(20) of weight 2 with sign 0 over Rational Field
        """
    def element(self, x):
        """
        Create and return an element of ``self`` from a modular symbol, if
        possible.

        INPUT:

        - ``x`` -- an object of one of the following types:
          ModularSymbol, ManinSymbol

        OUTPUT: ModularSymbol - a modular symbol with parent self

        EXAMPLES::

            sage: M = ModularSymbols(11,4,1)
            sage: M.T(3)
            Hecke operator T_3 on Modular Symbols space of dimension 4 for Gamma_0(11) of weight 4 with sign 1 over Rational Field
            sage: M.T(3)(M.0)
            28*[X^2,(0,1)] + 2*[X^2,(1,4)] + 2/3*[X^2,(1,6)] - 8/3*[X^2,(1,9)]
            sage: M.T(3)(M.0).element()
            (28, 2, 2/3, -8/3)
        """
    def dual_star_involution_matrix(self):
        """
        Return the matrix of the dual star involution, which is induced by
        complex conjugation on the linear dual of modular symbols.

        EXAMPLES::

            sage: ModularSymbols(20,2).dual_star_involution_matrix()
            [1 0 0 0 0 0 0]
            [0 1 0 0 0 0 0]
            [0 0 0 0 1 0 0]
            [0 0 0 1 0 0 0]
            [0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0]
            [0 0 0 0 0 0 1]
        """
    def factorization(self):
        """
        Return a list of pairs `(S,e)` where `S` is spaces
        of modular symbols and ``self`` is isomorphic to the direct sum of the
        `S^e` as a module over the *anemic* Hecke algebra adjoin
        the star involution. The cuspidal `S` are all simple, but
        the Eisenstein factors need not be simple.

        EXAMPLES::

            sage: ModularSymbols(Gamma0(22), 2).factorization()
            (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field)^2 *
            (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field)^2 *
            (Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 7 for Gamma_0(22) of weight 2 with sign 0 over Rational Field)

        ::

            sage: ModularSymbols(1,6,0,GF(2)).factorization()
            (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) *
            (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2)

        ::

            sage: ModularSymbols(18,2).factorization()
            (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 for Gamma_0(18) of weight 2 with sign 0 over Rational Field) *
            (Modular Symbols subspace of dimension 5 of Modular Symbols space of dimension 7 for Gamma_0(18) of weight 2 with sign 0 over Rational Field)

        ::

            sage: M = ModularSymbols(DirichletGroup(38,CyclotomicField(3)).0^2,  2, +1); M
            Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2
            sage: M.factorization()                    # long time (about 8 seconds)
            (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
            (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
            (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
            (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)
        """
    factor = factorization
    def is_cuspidal(self) -> bool:
        """
        Return ``True`` if this space is cuspidal, else ``False``.

        EXAMPLES::

            sage: M = ModularSymbols(20,2)
            sage: M.is_cuspidal()
            False
            sage: S = M.cuspidal_subspace()
            sage: S.is_cuspidal()
            True
            sage: S = M.eisenstein_subspace()
            sage: S.is_cuspidal()
            False
        """
    @cached_method
    def is_eisenstein(self) -> bool:
        """
        Return ``True`` if this space is Eisenstein, else ``False``.

        EXAMPLES::

            sage: M = ModularSymbols(20,2)
            sage: M.is_eisenstein()
            False
            sage: S = M.eisenstein_submodule()
            sage: S.is_eisenstein()
            True
            sage: S = M.cuspidal_subspace()
            sage: S.is_eisenstein()
            False
        """
    def manin_symbols_basis(self):
        """
        A list of Manin symbols that form a basis for the ambient space
        ``self``.

        OUTPUT: list of 2-tuples (if the weight is 2) or 3-tuples, which
        represent the Manin symbols basis for ``self``

        EXAMPLES::

            sage: m = ModularSymbols(23)
            sage: m.manin_symbols_basis()
            [(1,0), (1,17), (1,19), (1,20), (1,21)]
            sage: m = ModularSymbols(6, weight=4, sign=-1)
            sage: m.manin_symbols_basis()
            [[X^2,(2,1)]]
        """
    def modular_symbols_of_level(self, G):
        """
        Return a space of modular symbols with the same parameters as
        this space, except the congruence subgroup is changed to `G`.

        INPUT:

        - ``G`` -- either a congruence subgroup or an integer to use
          as the level of such a group.  The given group must either
          contain or be contained in the group defining ``self``.

        TESTS::

            sage: M = ModularSymbols(11)
            sage: M.modular_symbols_of_level(22)
            Modular Symbols space of dimension 7 for Gamma_0(22) of weight 2 with sign 0 over Rational Field
            sage: M.modular_symbols_of_level(Gamma1(22))
            Modular Symbols space of dimension 31 for Gamma_1(22) of weight 2 with sign 0 over Rational Field

            sage: M = ModularSymbols(Gamma1(6))
            sage: M.modular_symbols_of_level(12)
            Modular Symbols space of dimension 9 for Gamma_1(12) of weight 2 with sign 0 over Rational Field
            sage: M.modular_symbols_of_level(Gamma0(3))
            Modular Symbols space of dimension 1 for Gamma_0(3) of weight 2 with sign 0 over Rational Field
            sage: M.modular_symbols_of_level(Gamma0(12))
            Traceback (most recent call last):
            ...
            ValueError: one subgroup must contain the other

            sage: M = ModularSymbols(Gamma1(30),4); M
            Modular Symbols space of dimension 144 for Gamma_1(30) of weight 4 with sign 0 over Rational Field
            sage: M.modular_symbols_of_level(22)
            Traceback (most recent call last):
            ...
            ValueError: one level must divide the other

            sage: M = ModularSymbols(GammaH(15,[7]),6)
            sage: M.modular_symbols_of_level(5)
            Modular Symbols space of dimension 4 for Gamma_0(5) of weight 6 with sign 0 over Rational Field
            sage: M.modular_symbols_of_level(30)
            Modular Symbols space of dimension 60 for Congruence Subgroup Gamma_H(30) with H generated by [7] of weight 6 with sign 0 over Rational Field
            sage: M.modular_symbols_of_level(73)
            Traceback (most recent call last):
            ...
            ValueError: one level must divide the other
        """
    def modular_symbols_of_sign(self, sign):
        """
        Return a space of modular symbols with the same defining
        properties (weight, level, etc.) as this space except with given
        sign.

        INPUT:

        - ``sign`` -- integer; a sign (`+1`, `-1` or `0`)

        OUTPUT:

        (ModularSymbolsAmbient) A space of modular symbols with the
        same defining properties (weight, level, etc.) as this space
        except with given sign.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma0(11),2,sign=0)
            sage: M
            Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: M.modular_symbols_of_sign(-1)
            Modular Symbols space of dimension 1 for Gamma_0(11) of weight 2 with sign -1 over Rational Field
            sage: M = ModularSymbols(Gamma1(11),2,sign=0)
            sage: M.modular_symbols_of_sign(-1)
            Modular Symbols space of dimension 1 for Gamma_1(11) of weight 2 with sign -1 over Rational Field
        """
    def modular_symbols_of_weight(self, k):
        """
        Return a space of modular symbols with the same defining
        properties (weight, sign, etc.) as this space except with weight
        `k`.

        INPUT:

        - ``k`` -- positive integer

        OUTPUT:

        (ModularSymbolsAmbient) A space of modular symbols with the
        same defining properties (level, sign) as this space
        except with given weight.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma1(6),2,sign=0)
            sage: M.modular_symbols_of_weight(3)
            Modular Symbols space of dimension 4 for Gamma_1(6) of weight 3 with sign 0 over Rational Field
        """
    def star_involution(self):
        """
        Return the star involution on this modular symbols space.

        OUTPUT:

        (matrix) The matrix of the star involution on this space,
        which is induced by complex conjugation on modular symbols,
        with respect to the standard basis.

        EXAMPLES::

            sage: ModularSymbols(20,2).star_involution()
            Hecke module morphism Star involution on Modular Symbols space of dimension 7 for Gamma_0(20) of weight 2 with sign 0 over Rational Field defined by the matrix
            [1 0 0 0 0 0 0]
            [0 1 0 0 0 0 0]
            [0 0 0 0 1 0 0]
            [0 0 0 1 0 0 0]
            [0 0 1 0 0 0 0]
            [0 0 0 0 0 1 0]
            [0 0 0 0 0 0 1]
            Domain: Modular Symbols space of dimension 7 for Gamma_0(20) of weight ...
            Codomain: Modular Symbols space of dimension 7 for Gamma_0(20) of weight ...
        """
    def submodule(self, M, dual_free_module=None, check: bool = True):
        """
        Return the submodule with given generators or free module `M`.

        INPUT:

        - ``M`` -- either a submodule of this ambient free module, or
          generators for a submodule

        - ``dual_free_module`` -- boolean (default: ``None``); this may be
          useful to speed up certain calculations; it is the corresponding
          submodule of the ambient dual module;

        - ``check`` -- boolean (default: ``True``); if ``True``, check that `M`
          is a submodule, i.e. is invariant under all Hecke operators

        OUTPUT: a subspace of this modular symbol space

        EXAMPLES::

            sage: M = ModularSymbols(11)
            sage: M.submodule([M.0])
            Traceback (most recent call last):
            ...
            ValueError: The submodule must be invariant under all Hecke operators.
            sage: M.eisenstein_submodule().basis()
            ((1,0) - 1/5*(1,9),)
            sage: M.basis()
            ((1,0), (1,8), (1,9))
            sage: M.submodule([M.0 - 1/5*M.2])
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field

        .. NOTE::

           It would make more sense to only check that `M` is invariant
           under the Hecke operators with index coprime to the level.
           Unfortunately, I do not know a reasonable algorithm for
           determining whether a module is invariant under just the
           anemic Hecke algebra, since I do not know an analogue of
           the Sturm bound for the anemic Hecke algebra. - William
           Stein, 2007-07-27
        """
    def twisted_winding_element(self, i, eps):
        """
        Return the twisted winding element of given degree and character.

        INPUT:

        - ``i`` -- integer; `0\\le i\\le k-2` where `k` is the weight

        - ``eps`` -- character; a Dirichlet character

        OUTPUT:

        (modular symbol) The so-called 'twisted winding element':

        .. MATH::

                \\sum_{a \\in (\\ZZ/m\\ZZ)^\\times} \\varepsilon(a) * [ i, 0, a/m ].

        .. NOTE::

           This will only work if the base ring of the modular symbol
           space contains the character values.

        EXAMPLES::

            sage: eps = DirichletGroup(5)[2]
            sage: K = eps.base_ring()
            sage: M = ModularSymbols(37,2,0,K)
            sage: M.twisted_winding_element(0,eps)
            2*(1,23) - 2*(1,32) + 2*(1,34)
        """
    def integral_structure(self, algorithm: str = 'default'):
        """
        Return the `\\ZZ`-structure of this modular symbols
        space, generated by all integral modular symbols.

        INPUT:

        - ``algorithm`` -- string (default: ``'default'``, choose
          heuristically)

           - ``'pari'`` -- use pari for the HNF computation

           - ``'padic'`` -- use `p`-adic algorithm (only good for
              dense case)


        ALGORITHM: It suffices to consider lattice generated by the free
        generating symbols `X^iY^{k-2-i}.(u,v)` after quotienting
        out by the `S` (and `I`) relations, since the
        quotient by these relations is the same over any ring.

        EXAMPLES: In weight 2 the rational basis is often integral.

        ::

            sage: M = ModularSymbols(11,2)
            sage: M.integral_structure()
            Free module of degree 3 and rank 3 over Integer Ring
            Echelon basis matrix:
            [1 0 0]
            [0 1 0]
            [0 0 1]

        This is rarely the case in higher weight::

            sage: M = ModularSymbols(6,4)
            sage: M.integral_structure()
            Free module of degree 6 and rank 6 over Integer Ring
            Echelon basis matrix:
            [  1   0   0   0   0   0]
            [  0   1   0   0   0   0]
            [  0   0 1/2 1/2 1/2 1/2]
            [  0   0   0   1   0   0]
            [  0   0   0   0   1   0]
            [  0   0   0   0   0   1]

        Here is an example involving `\\Gamma_1(N)`.

        ::

            sage: M = ModularSymbols(Gamma1(5),6)
            sage: M.integral_structure()
            Free module of degree 10 and rank 10 over Integer Ring
            Echelon basis matrix:
            [    1     0     0     0     0     0     0     0     0     0]
            [    0     1     0     0     0     0     0     0     0     0]
            [    0     0  1/96  1/32 23/24     0  1/96     0  7/24 67/96]
            [    0     0     0  1/24 23/24     0     0  1/24   1/4 17/24]
            [    0     0     0     0     1     0     0     0     0     0]
            [    0     0     0     0     0   1/6     0  1/48 23/48   1/3]
            [    0     0     0     0     0     0  1/24  1/24 11/24 11/24]
            [    0     0     0     0     0     0     0  1/16  7/16   1/2]
            [    0     0     0     0     0     0     0     0   1/2   1/2]
            [    0     0     0     0     0     0     0     0     0     1]
        """
    def compact_newform_eigenvalues(self, v, names: str = 'alpha'):
        """
        Return compact systems of eigenvalues for each Galois conjugacy
        class of cuspidal newforms in this ambient space.

        INPUT:

        - ``v`` -- list of positive integers

        OUTPUT:

        List of pairs (E, x), where ``E*x`` is a vector with entries the
        eigenvalues `a_n` for `n \\in v`.

        EXAMPLES::

            sage: M = ModularSymbols(43,2,1)
            sage: X = M.compact_newform_eigenvalues(prime_range(10))
            sage: X[0][0] * X[0][1]
            (-2, -2, -4, 0)
            sage: X[1][0] * X[1][1]
            (alpha1, -alpha1, -alpha1 + 2, alpha1 - 2)

        ::

            sage: M = ModularSymbols(DirichletGroup(24,QQ).1,2,sign=1)
            sage: M.compact_newform_eigenvalues(prime_range(10),'a')
            [(
            [-1/2 -1/2]
            [ 1/2 -1/2]
            [  -1    1]
            [  -2    0], (1, -2*a0 - 1)
            )]
            sage: a = M.compact_newform_eigenvalues([1..10],'a')[0]
            sage: a[0]*a[1]
            (1, a0, a0 + 1, -2*a0 - 2, -2*a0 - 2, -a0 - 2, -2, 2*a0 + 4, -1, 2*a0 + 4)
            sage: M = ModularSymbols(DirichletGroup(13).0^2,2,sign=1)
            sage: M.compact_newform_eigenvalues(prime_range(10),'a')
            [(
            [  -zeta6 - 1]
            [ 2*zeta6 - 2]
            [-2*zeta6 + 1]
            [           0], (1)
            )]
            sage: a = M.compact_newform_eigenvalues([1..10],'a')[0]
            sage: a[0]*a[1]
            (1, -zeta6 - 1, 2*zeta6 - 2, zeta6, -2*zeta6 + 1, -2*zeta6 + 4, 0, 2*zeta6 - 1, -zeta6, 3*zeta6 - 3)
        """
    def __pari__(self) -> None:
        """
        Return a PARI object corresponding to ``self``.

        TESTS::

            sage: ModularSymbols(Gamma1(5), 2).__pari__()
            Traceback (most recent call last):
            ...
            NotImplementedError: PARI modular symbols are only implemented for Gamma0(n)
        """

class ModularSymbolsAmbient_wtk_g0(ModularSymbolsAmbient):
    """
    Modular symbols for `\\Gamma_0(N)` of integer weight
    `k > 2` over the field `F`.

    For weight `2`, it is faster to use ``ModularSymbols_wt2_g0``.

    INPUT:

    - ``N`` -- integer; the level

    - ``k`` -- integer; weight = 2

    - ``sign`` -- integer; either -1, 0, or 1

    - ``F`` -- field

    EXAMPLES::

        sage: ModularSymbols(1,12)
        Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
        sage: ModularSymbols(1,12, sign=1).dimension()
        2
        sage: ModularSymbols(15,4, sign=-1).dimension()
        4
        sage: ModularSymbols(6,6).dimension()
        10
        sage: ModularSymbols(36,4).dimension()
        36
    """
    def __init__(self, N, k, sign, F, custom_init=None, category=None) -> None:
        """
        Initialize a space of modular symbols of weight `k` for
        `\\Gamma_0(N)`, over `\\QQ`.

        For weight `2`, it is faster to use
        ``ModularSymbols_wt2_g0``.

        INPUT:

        - ``N`` -- integer; the level

        - ``k`` -- integer; weight = 2

        - ``sign`` -- integer; either -1, 0, or 1

        - ``F`` -- field

        EXAMPLES::

            sage: ModularSymbols(1,12)
            Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
            sage: ModularSymbols(1,12, sign=1).dimension()
            2
            sage: ModularSymbols(15,4, sign=-1).dimension()
            4
            sage: ModularSymbols(6,6).dimension()
            10
            sage: ModularSymbols(36,4).dimension()
            36
        """
    def boundary_space(self):
        """
        Return the space of boundary modular symbols for this space.

        EXAMPLES::

            sage: M = ModularSymbols(100,2)
            sage: M.boundary_space()
            Space of Boundary Modular Symbols for Congruence Subgroup Gamma0(100) of weight 2 over Rational Field
        """
    def manin_symbols(self):
        """
        Return the Manin symbol list of this modular symbol space.

        EXAMPLES::

            sage: M = ModularSymbols(100,4)
            sage: M.manin_symbols()
            Manin Symbol List of weight 4 for Gamma0(100)
            sage: len(M.manin_symbols())
            540
        """
    @cached_method
    def __pari__(self):
        """
        Return a PARI object corresponding to ``self``.

        EXAMPLES::

            sage: ModularSymbols(Gamma0(1), 2).__pari__()
            [[[[Vecsmall([0, 1])], [0], 1, [Vecsmall([]), Vecsmall([])],
               Vecsmall([1]), Vecsmall([]), Vecsmall([])],
              0, 0, 0, Vecsmall([1]), 0, 0, [[1, 1; [0, 1; -1, 0], 1]],
              [[1, 1; [0, -1; 1, -1], 1; [-1, 1; -1, 0], 1]], 0,
              Vecsmall([0, 0, 1, 1, 2]), [[Vecsmall([1, 0]), Vecsmall([0, 1])]],
              0, 0, 0, [Vecsmall([1, 1]), [Vecsmall([0, 1]), 0], [Vecsmall([1, 0])]]],
             [0, [;], [[;], [;], 1, Vecsmall([])]],
             [[], Vecsmall([2, 0]), Vecsmall([0, 0]), 0, [[;], [;], 1, Vecsmall([])]]]

        .. NOTE::

            Spaces of modular symbols as implemented in PARI are
            canonically dual to those implemented in Sage.  See
            :meth:`ModularSymbolsAmbient._pari_pairing` and
            :meth:`ModularSymbolsAmbient._pari_tensor` for how to use
            this duality.
        """

class ModularSymbolsAmbient_wt2_g0(ModularSymbolsAmbient_wtk_g0):
    """
    Modular symbols for `\\Gamma_0(N)` of integer weight `2` over the field
    `F`.

    INPUT:

    - ``N`` -- integer; the level

    - ``sign`` -- integer; either -1, 0, or 1

    OUTPUT:

    The space of modular symbols of weight `2`, trivial character, level
    `N` and given sign.

    EXAMPLES::

        sage: ModularSymbols(Gamma0(12),2)
        Modular Symbols space of dimension 5 for Gamma_0(12) of weight 2 with sign 0 over Rational Field
    """
    def __init__(self, N, sign, F, custom_init=None, category=None) -> None:
        """
        Initialize a space of modular symbols.

        INPUT:

        - ``N`` -- integer; the level

        - ``sign`` -- integer; either -1, 0, or 1

        OUTPUT:

        The space of modular symbols of weight 2, trivial character,
        level N and given sign.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma0(12),2)
        """
    def boundary_space(self):
        """
        Return the space of boundary modular symbols for this space.

        EXAMPLES::

            sage: M = ModularSymbols(100,2)
            sage: M.boundary_space()
            Space of Boundary Modular Symbols for Congruence Subgroup Gamma0(100) of weight 2 over Rational Field
        """

class ModularSymbolsAmbient_wtk_g1(ModularSymbolsAmbient):
    """
    INPUT:

    - ``level`` -- integer; the level

    - ``weight`` -- integer; the weight = 2

    - ``sign`` -- integer; either -1, 0, or 1

    - ``F`` -- field

    EXAMPLES::

        sage: ModularSymbols(Gamma1(17),2)
        Modular Symbols space of dimension 25 for Gamma_1(17) of weight 2 with sign 0 over Rational Field
        sage: [ModularSymbols(Gamma1(7),k).dimension() for k in [2,3,4,5]]
        [5, 8, 12, 16]

    ::

        sage: ModularSymbols(Gamma1(7),3)
        Modular Symbols space of dimension 8 for Gamma_1(7) of weight 3 with sign 0 over Rational Field
    """
    def __init__(self, level, weight, sign, F, custom_init=None, category=None) -> None:
        """
        Initialize a space of modular symbols for Gamma1(N).

        INPUT:

        - ``level`` -- integer; the level

        - ``weight`` -- integer; the weight = 2

        - ``sign`` -- integer; either -1, 0, or 1

        - ``F`` -- field

        EXAMPLES::

            sage: ModularSymbols(Gamma1(17),2)
            Modular Symbols space of dimension 25 for Gamma_1(17) of weight 2 with sign 0 over Rational Field
            sage: [ModularSymbols(Gamma1(7),k).dimension() for k in [2,3,4,5]]
            [5, 8, 12, 16]

        ::

            sage: M = ModularSymbols(Gamma1(7),3)
        """
    def boundary_space(self):
        """
        Return the space of boundary modular symbols for this space.

        EXAMPLES::

            sage: M = ModularSymbols(100,2)
            sage: M.boundary_space()
            Space of Boundary Modular Symbols for Congruence Subgroup Gamma0(100) of weight 2 over Rational Field
        """
    def manin_symbols(self):
        """
        Return the Manin symbol list of this modular symbol space.

        EXAMPLES::

            sage: M = ModularSymbols(Gamma1(30),4)
            sage: M.manin_symbols()
            Manin Symbol List of weight 4 for Gamma1(30)
            sage: len(M.manin_symbols())
            1728
        """

class ModularSymbolsAmbient_wtk_gamma_h(ModularSymbolsAmbient):
    def __init__(self, group, weight, sign, F, custom_init=None, category=None) -> None:
        """
        Initialize a space of modular symbols for `\\Gamma_H(N)`.

        INPUT:

        - ``group`` -- a congruence subgroup `\\Gamma_H(N)`

        - ``weight`` -- integer; the weight = 2

        - ``sign`` -- integer; either -1, 0, or 1

        - ``F`` -- field

        EXAMPLES::

            sage: ModularSymbols(GammaH(15,[4]),2)
            Modular Symbols space of dimension 9 for Congruence Subgroup Gamma_H(15) with H generated by [4] of weight 2 with sign 0 over Rational Field
        """
    def boundary_space(self):
        """
        Return the space of boundary modular symbols for this space.

        EXAMPLES::

            sage: M = ModularSymbols(GammaH(15,[4]),2)
            sage: M.boundary_space()
            Boundary Modular Symbols space for Congruence Subgroup Gamma_H(15) with H generated by [4] of weight 2 over Rational Field
        """
    def manin_symbols(self):
        """
        Return the Manin symbol list of this modular symbol space.

        EXAMPLES::

            sage: M = ModularSymbols(GammaH(15,[4]),2)
            sage: M.manin_symbols()
            Manin Symbol List of weight 2 for Congruence Subgroup Gamma_H(15) with H generated by [4]
            sage: len(M.manin_symbols())
            96
        """

class ModularSymbolsAmbient_wtk_eps(ModularSymbolsAmbient):
    def __init__(self, eps, weight, sign, base_ring, custom_init=None, category=None) -> None:
        '''
        Space of modular symbols with given weight, character, base ring and
        sign.

        INPUT:

        - ``eps`` -- dirichlet.DirichletCharacter, the
           "Nebentypus" character

        - ``weight`` -- integer; the weight = 2

        - ``sign`` -- integer; either -1, 0, or 1

        - ``base_ring`` -- the base ring; it must be possible to change the ring
          of the character to this base ring (not always canonically)

        EXAMPLES::

            sage: eps = DirichletGroup(4).gen(0)
            sage: eps.order()
            2
            sage: ModularSymbols(eps, 2)
            Modular Symbols space of dimension 0 and level 4, weight 2, character [-1], sign 0, over Rational Field
            sage: ModularSymbols(eps, 3)
            Modular Symbols space of dimension 2 and level 4, weight 3, character [-1], sign 0, over Rational Field

        We next create a space with character of order bigger than 2.

        ::

            sage: eps = DirichletGroup(5).gen(0)
            sage: eps     # has order 4
            Dirichlet character modulo 5 of conductor 5 mapping 2 |--> zeta4
            sage: ModularSymbols(eps, 2).dimension()
            0
            sage: ModularSymbols(eps, 3).dimension()
            2

        Here is another example::

            sage: G.<e> = DirichletGroup(5)
            sage: M = ModularSymbols(e,3)
            sage: loads(M.dumps()) == M
            True
        '''
    def boundary_space(self):
        """
        Return the space of boundary modular symbols for this space.

        EXAMPLES::

            sage: eps = DirichletGroup(5).gen(0)
            sage: M = ModularSymbols(eps, 2)
            sage: M.boundary_space()
            Boundary Modular Symbols space of level 5, weight 2, character [zeta4] and dimension 0 over Cyclotomic Field of order 4 and degree 2
        """
    def manin_symbols(self):
        """
        Return the Manin symbol list of this modular symbol space.

        EXAMPLES::

            sage: eps = DirichletGroup(5).gen(0)
            sage: M = ModularSymbols(eps, 2)
            sage: M.manin_symbols()
            Manin Symbol List of weight 2 for Gamma1(5) with character [zeta4]
            sage: len(M.manin_symbols())
            6
        """
    def modular_symbols_of_level(self, N):
        """
        Return a space of modular symbols with the same parameters as
        this space except with level `N`.

        INPUT:

        - ``N`` -- positive integer

        OUTPUT:

        (Modular Symbol space) A space of modular symbols with the
        same defining properties (weight, sign, etc.) as this space
        except with level `N`.

        EXAMPLES::

            sage: eps = DirichletGroup(5).gen(0)
            sage: M = ModularSymbols(eps, 2); M
            Modular Symbols space of dimension 0 and level 5, weight 2, character [zeta4], sign 0, over Cyclotomic Field of order 4 and degree 2
            sage: M.modular_symbols_of_level(15)
            Modular Symbols space of dimension 0 and level 15, weight 2, character [1, zeta4], sign 0, over Cyclotomic Field of order 4 and degree 2
        """
    def modular_symbols_of_sign(self, sign):
        """
        Return a space of modular symbols with the same defining
        properties (weight, level, etc.) as this space except with given
        sign.

        INPUT:

        - ``sign`` -- integer; a sign (`+1`, `-1` or `0`)

        OUTPUT:

        (ModularSymbolsAmbient) A space of modular symbols with the
        same defining properties (weight, level, etc.) as this space
        except with given sign.

        EXAMPLES::

            sage: eps = DirichletGroup(5).gen(0)
            sage: M = ModularSymbols(eps, 2); M
            Modular Symbols space of dimension 0 and level 5, weight 2, character [zeta4], sign 0, over Cyclotomic Field of order 4 and degree 2
            sage: M.modular_symbols_of_sign(0) == M
            True
            sage: M.modular_symbols_of_sign(+1)
            Modular Symbols space of dimension 0 and level 5, weight 2, character [zeta4], sign 1, over Cyclotomic Field of order 4 and degree 2
            sage: M.modular_symbols_of_sign(-1)
            Modular Symbols space of dimension 0 and level 5, weight 2, character [zeta4], sign -1, over Cyclotomic Field of order 4 and degree 2
        """
    def modular_symbols_of_weight(self, k):
        """
        Return a space of modular symbols with the same defining
        properties (weight, sign, etc.) as this space except with weight
        `k`.

        INPUT:

        - ``k`` -- positive integer

        OUTPUT:

        (ModularSymbolsAmbient) A space of modular symbols with the
        same defining properties (level, sign) as this space
        except with given weight.

        EXAMPLES::

            sage: eps = DirichletGroup(5).gen(0)
            sage: M = ModularSymbols(eps, 2); M
            Modular Symbols space of dimension 0 and level 5, weight 2, character [zeta4], sign 0, over Cyclotomic Field of order 4 and degree 2
            sage: M.modular_symbols_of_weight(3)
            Modular Symbols space of dimension 2 and level 5, weight 3, character [zeta4], sign 0, over Cyclotomic Field of order 4 and degree 2
            sage: M.modular_symbols_of_weight(2) == M
            True
        """
