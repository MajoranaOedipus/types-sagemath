from collections.abc import Iterator
from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.categories.algebras import Algebras as Algebras
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation

def is_HeckeAlgebra(x) -> bool:
    """
    Return ``True`` if x is of type HeckeAlgebra.

    EXAMPLES::

        sage: from sage.modular.hecke.algebra import is_HeckeAlgebra
        sage: is_HeckeAlgebra(CuspForms(1, 12).anemic_hecke_algebra())
        doctest:warning...
        DeprecationWarning: the function is_HeckeAlgebra is deprecated;
        use 'isinstance(..., HeckeAlgebra_base)' instead
        See https://github.com/sagemath/sage/issues/37895 for details.
        True
        sage: is_HeckeAlgebra(ZZ)
        False
    """

class HeckeAlgebra_base(CachedRepresentation, Parent):
    """
    Base class for algebras of Hecke operators on a fixed Hecke module.

    INPUT:

    - ``M`` -- a Hecke module

    EXAMPLES::

        sage: CuspForms(1, 12).hecke_algebra() # indirect doctest
        Full Hecke algebra acting on Cuspidal subspace of dimension 1 of Modular Forms space of dimension 2 for Modular Group SL(2,Z) of weight 12 over Rational Field
    """
    @staticmethod
    def __classcall__(cls, M):
        """
        We need to work around a problem originally discovered by David
        Loeffler on 2009-04-13: The problem is that if one creates two
        subspaces of a Hecke module which are equal as subspaces but have
        different bases, then the caching machinery needs to distinguish
        between them. So we need to add ``basis_matrix`` to the cache key even
        though it is not looked at by the constructor.

        TESTS:

        We test that coercion is OK between the Hecke algebras associated to two submodules which are equal but have different bases::

            sage: M = CuspForms(Gamma0(57))
            sage: f1,f2,f3 = M.newforms()
            sage: N1 = M.submodule(M.free_module().submodule_with_basis([f1.element().element(), f2.element().element()]))
            sage: N2 = M.submodule(M.free_module().submodule_with_basis([f1.element().element(), (f1.element() + f2.element()).element()]))
            sage: N1.hecke_operator(5).matrix_form()
            Hecke operator on Modular Forms subspace of dimension 2 of ... defined by:
            [-3  0]
            [ 0  1]
            sage: N2.hecke_operator(5).matrix_form()
            Hecke operator on Modular Forms subspace of dimension 2 of ... defined by:
            [-3  0]
            [-4  1]
            sage: N1.hecke_algebra()(N2.hecke_operator(5)).matrix_form()
            Hecke operator on Modular Forms subspace of dimension 2 of ... defined by:
            [-3  0]
            [ 0  1]
            sage: N1.hecke_algebra()(N2.hecke_operator(5).matrix_form())
            Hecke operator on Modular Forms subspace of dimension 2 of ... defined by:
            [-3  0]
            [ 0  1]
        """
    def __init__(self, M) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: from sage.modular.hecke.algebra import HeckeAlgebra_base
            sage: type(HeckeAlgebra_base(CuspForms(1, 12)))
            <class 'sage.modular.hecke.algebra.HeckeAlgebra_base_with_category'>
        """
    def gen(self, n):
        """
        Return the `n`-th Hecke operator.

        EXAMPLES::

            sage: T = ModularSymbols(11).hecke_algebra()
            sage: T.gen(2)
            Hecke operator T_2 on Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
        """
    def ngens(self):
        """
        The size of the set of generators returned by gens(), which is clearly
        infinity.

        (This is not necessarily a minimal set of generators.)

        EXAMPLES::

            sage: CuspForms(1, 12).anemic_hecke_algebra().ngens()
            +Infinity
        """
    def one(self):
        """
        Return the unit of the Hecke algebra.

        EXAMPLES::

            sage: M = ModularSymbols(11,2,1)
            sage: H = M.hecke_algebra()
            sage: H.one()
            Hecke operator on Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field defined by:
            [1 0]
            [0 1]
        """
    def is_noetherian(self) -> bool:
        """
        Return ``True`` if this Hecke algebra is Noetherian as a ring.

        This is true if and only if the base ring is Noetherian.

        EXAMPLES::

            sage: CuspForms(1, 12).anemic_hecke_algebra().is_noetherian()
            True
        """
    @cached_method
    def matrix_space(self):
        """
        Return the underlying matrix space of this module.

        EXAMPLES::

            sage: CuspForms(3, 24, base_ring=Qp(5)).anemic_hecke_algebra().matrix_space()
            Full MatrixSpace of 7 by 7 dense matrices over 5-adic Field with capped relative precision 20
        """
    def level(self):
        """
        Return the level of this Hecke algebra, which is (by definition) the
        level of the Hecke module on which it acts.

        EXAMPLES::

            sage: ModularSymbols(37).hecke_algebra().level()
            37
        """
    def module(self):
        """
        The Hecke module on which this algebra is acting.

        EXAMPLES::

            sage: T = ModularSymbols(1,12).hecke_algebra()
            sage: T.module()
            Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
        """
    def rank(self) -> None:
        """
        The rank of this Hecke algebra as a module over its base
        ring. Not implemented at present.

        EXAMPLES::

            sage: ModularSymbols(Gamma1(3), 3).hecke_algebra().rank()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    @cached_method
    def basis(self):
        """
        Return a basis for this Hecke algebra as a free module over
        its base ring.

        EXAMPLES::

            sage: ModularSymbols(Gamma1(3), 3).hecke_algebra().basis()
            (Hecke operator on Modular Symbols space of dimension 2 for Gamma_1(3) of weight 3 with sign 0 over Rational Field defined by:
            [1 0]
            [0 1],
            Hecke operator on Modular Symbols space of dimension 2 for Gamma_1(3) of weight 3 with sign 0 over Rational Field defined by:
            [0 0]
            [0 2])

            sage: M = ModularSymbols(Gamma0(22), sign=1)
            sage: H = M.hecke_algebra()
            sage: B = H.basis()
            sage: len(B)
            5
            sage: all(b in H for b in B)
            True
            sage: [B[0, 0] for B in M.anemic_hecke_algebra().basis()]
            Traceback (most recent call last):
            ...
            NotImplementedError: basis not implemented for anemic Hecke algebra
        """
    @cached_method
    def discriminant(self):
        """
        Return the discriminant of this Hecke algebra.

        This is the
        determinant of the matrix `{\\rm Tr}(x_i x_j)` where `x_1,
        \\dots,x_d` is a basis for self, and `{\\rm Tr}(x)` signifies
        the trace (in the sense of linear algebra) of left
        multiplication by `x` on the algebra (*not* the trace of the
        operator `x` acting on the underlying Hecke module!). For
        further discussion and conjectures see Calegari + Stein,
        *Conjectures about discriminants of Hecke algebras of prime
        level*, Springer LNCS 3076.

        EXAMPLES::

            sage: BrandtModule(3, 4).hecke_algebra().discriminant()
            1
            sage: ModularSymbols(65, sign=1).cuspidal_submodule().hecke_algebra().discriminant()
            6144
            sage: ModularSymbols(1,4,sign=1).cuspidal_submodule().hecke_algebra().discriminant()
            1
            sage: H = CuspForms(1, 24).hecke_algebra()
            sage: H.discriminant()
            83041344
        """
    def gens(self) -> Iterator:
        """
        Return a generator over all Hecke operator `T_n`
        for `n = 1, 2, 3, \\ldots`.

        This is infinite.

        EXAMPLES::

            sage: T = ModularSymbols(1,12).hecke_algebra()
            sage: g = T.gens()
            sage: next(g)
            Hecke operator T_1 on Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
            sage: next(g)
            Hecke operator T_2 on Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
        """
    def hecke_operator(self, n):
        """
        Return the `n`-th Hecke operator `T_n`.

        EXAMPLES::

            sage: T = ModularSymbols(1,12).hecke_algebra()
            sage: T.hecke_operator(2)
            Hecke operator T_2 on Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
        """
    def hecke_matrix(self, n, *args, **kwds):
        """
        Return the matrix of the `n`-th Hecke operator `T_n`.

        EXAMPLES::

            sage: T = ModularSymbols(1,12).hecke_algebra()
            sage: T.hecke_matrix(2)
            [ -24    0    0]
            [   0  -24    0]
            [4860    0 2049]
        """
    def diamond_bracket_matrix(self, d):
        """
        Return the matrix of the diamond bracket operator `\\langle d \\rangle`.

        EXAMPLES::

            sage: T = ModularSymbols(Gamma1(7), 4).hecke_algebra()
            sage: d3 = T.diamond_bracket_matrix(3)
            sage: x = d3.charpoly().variables()[0]
            sage: d3.charpoly() == (x^3-1)^4
            True
        """
    def diamond_bracket_operator(self, d):
        """
        Return the diamond bracket operator `\\langle d \\rangle`.

        EXAMPLES::

            sage: T = ModularSymbols(Gamma1(7), 4).hecke_algebra()
            sage: T.diamond_bracket_operator(3)
            Diamond bracket operator <3> on Modular Symbols space of dimension 12 for Gamma_1(7) of weight 4 with sign 0 over Rational Field
        """

class HeckeAlgebra_full(HeckeAlgebra_base):
    """
    A full Hecke algebra (including the operators `T_n` where `n` is not
    assumed to be coprime to the level).
    """
    def __richcmp__(self, other, op) -> bool:
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: A = ModularForms(37).hecke_algebra()
            sage: A == QQ
            False
            sage: A == ModularForms(37).anemic_hecke_algebra()
            False
            sage: A == A
            True
        """
    def is_anemic(self) -> bool:
        """
        Return ``False``, since this the full Hecke algebra.

        EXAMPLES::

            sage: H = CuspForms(3, 12).hecke_algebra()
            sage: H.is_anemic()
            False
        """
    def anemic_subalgebra(self):
        """
        The subalgebra of ``self`` generated by the Hecke operators of
        index coprime to the level.

        EXAMPLES::

            sage: H = CuspForms(3, 12).hecke_algebra()
            sage: H.anemic_subalgebra()
            Anemic Hecke algebra acting on Cuspidal subspace of dimension 3 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(3) of weight 12 over Rational Field
        """
HeckeAlgebra = HeckeAlgebra_full

class HeckeAlgebra_anemic(HeckeAlgebra_base):
    """
    An anemic Hecke algebra, generated by Hecke operators with index coprime to the level.
    """
    def __richcmp__(self, other, op) -> bool:
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: A = ModularForms(23).anemic_hecke_algebra()
            sage: A == QQ
            False
            sage: A == ModularForms(23).hecke_algebra()
            False
            sage: A == A
            True
        """
    def hecke_operator(self, n):
        """
        Return the `n`-th Hecke operator, for `n` any
        positive integer coprime to the level.

        EXAMPLES::

            sage: T = ModularSymbols(Gamma1(5),3).anemic_hecke_algebra()
            sage: T.hecke_operator(2)
            Hecke operator T_2 on Modular Symbols space of dimension 4 for Gamma_1(5) of weight 3 with sign 0 over Rational Field
            sage: T.hecke_operator(5)
            Traceback (most recent call last):
            ...
            IndexError: Hecke operator T_5 not defined in the anemic Hecke algebra
        """
    def is_anemic(self) -> bool:
        """
        Return ``True``, since this is the anemic Hecke algebra.

        EXAMPLES::

            sage: H = CuspForms(3, 12).anemic_hecke_algebra()
            sage: H.is_anemic()
            True
        """
    def gens(self) -> Iterator:
        """
        Return a generator over all Hecke operator `T_n` for
        `n = 1, 2, 3, \\ldots`, with `n` coprime to the
        level. This is an infinite sequence.

        EXAMPLES::

            sage: T = ModularSymbols(12,2).anemic_hecke_algebra()
            sage: g = T.gens()
            sage: next(g)
            Hecke operator T_1 on Modular Symbols space of dimension 5 for Gamma_0(12) of weight 2 with sign 0 over Rational Field
            sage: next(g)
            Hecke operator T_5 on Modular Symbols space of dimension 5 for Gamma_0(12) of weight 2 with sign 0 over Rational Field
        """
AnemicHeckeAlgebra = HeckeAlgebra_anemic
