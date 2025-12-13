from . import defaults as defaults, eis_series as eis_series, eisenstein_submodule as eisenstein_submodule, space as space, submodule as submodule
from sage.arith.misc import is_prime as is_prime, sigma as sigma
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_class as Gamma1_class
from sage.modular.arithgroup.congroup_generic import CongruenceSubgroupBase as CongruenceSubgroupBase
from sage.modular.dirichlet import TrivialCharacter as TrivialCharacter
from sage.modular.hecke.ambient_module import AmbientHeckeModule as AmbientHeckeModule
from sage.modular.modsym.modsym import ModularSymbols as ModularSymbols
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.rings.integer import Integer as Integer
from sage.structure.sequence import Sequence as Sequence

class ModularFormsAmbient(space.ModularFormsSpace, AmbientHeckeModule):
    """
    An ambient space of modular forms.
    """
    def __init__(self, group, weight, base_ring, character=None, eis_only: bool = False) -> None:
        """
        Create an ambient space of modular forms.

        EXAMPLES::

            sage: m = ModularForms(Gamma1(20),20); m
            Modular Forms space of dimension 238 for Congruence Subgroup Gamma1(20) of weight 20 over Rational Field
            sage: m.is_ambient()
            True
        """
    def change_ring(self, base_ring):
        """
        Change the base ring of this space of modular forms.

        INPUT:

        - ``R`` -- ring

        EXAMPLES::

            sage: M = ModularForms(Gamma0(37),2)
            sage: M.basis()
            [q + q^3 - 2*q^4 + O(q^6),
             q^2 + 2*q^3 - 2*q^4 + q^5 + O(q^6),
             1 + 2/3*q + 2*q^2 + 8/3*q^3 + 14/3*q^4 + 4*q^5 + O(q^6)]

        The basis after changing the base ring is the reduction modulo
        `3` of an integral basis.

        ::

            sage: M3 = M.change_ring(GF(3))
            sage: M3.basis()
            [q + q^3 + q^4 + O(q^6),
             q^2 + 2*q^3 + q^4 + q^5 + O(q^6),
             1 + q^3 + q^4 + 2*q^5 + O(q^6)]
        """
    @cached_method
    def dimension(self):
        """
        Return the dimension of this ambient space of modular forms,
        computed using a dimension formula (so it should be reasonably
        fast).

        EXAMPLES::

            sage: m = ModularForms(Gamma1(20),20)
            sage: m.dimension()
            238
        """
    def hecke_module_of_level(self, N):
        """
        Return the Hecke module of level N corresponding to self, which is the
        domain or codomain of a degeneracy map from ``self``. Here N must be either
        a divisor or a multiple of the level of ``self``.

        EXAMPLES::

            sage: ModularForms(25, 6).hecke_module_of_level(5)
            Modular Forms space of dimension 3 for Congruence Subgroup Gamma0(5) of weight 6 over Rational Field
            sage: ModularForms(Gamma1(4), 3).hecke_module_of_level(8)
            Modular Forms space of dimension 7 for Congruence Subgroup Gamma1(8) of weight 3 over Rational Field
            sage: ModularForms(Gamma1(4), 3).hecke_module_of_level(9)
            Traceback (most recent call last):
            ...
            ValueError: N (=9) must be a divisor or a multiple of the level of self (=4)
        """
    def rank(self):
        """
        This is a synonym for ``self.dimension()``.

        EXAMPLES::

            sage: m = ModularForms(Gamma0(20),4)
            sage: m.rank()
            12
            sage: m.dimension()
            12
        """
    def ambient_space(self):
        """
        Return the ambient space that contains this ambient space. This is,
        of course, just this space again.

        EXAMPLES::

            sage: m = ModularForms(Gamma0(3),30)
            sage: m.ambient_space() is m
            True
        """
    def is_ambient(self) -> bool:
        """
        Return ``True`` if this an ambient space of modular forms.

        This is an ambient space, so this function always returns ``True``.

        EXAMPLES::

            sage: ModularForms(11).is_ambient()
            True
            sage: CuspForms(11).is_ambient()
            False
        """
    def modular_symbols(self, sign: int = 0):
        """
        Return the corresponding space of modular symbols with the given
        sign.

        EXAMPLES::

            sage: S = ModularForms(11,2)
            sage: S.modular_symbols()
            Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: S.modular_symbols(sign=1)
            Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field
            sage: S.modular_symbols(sign=-1)
            Modular Symbols space of dimension 1 for Gamma_0(11) of weight 2 with sign -1 over Rational Field

        ::

            sage: ModularForms(1,12).modular_symbols()
            Modular Symbols space of dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field
        """
    @cached_method
    def module(self):
        """
        Return the underlying free module corresponding to this space
        of modular forms.

        EXAMPLES::

            sage: m = ModularForms(Gamma1(13),10)
            sage: m.free_module()
            Vector space of dimension 69 over Rational Field
            sage: ModularForms(Gamma1(13),4, GF(49,'b')).free_module()
            Vector space of dimension 27 over Finite Field in b of size 7^2
        """
    def free_module(self):
        """
        Return the free module underlying this space of modular forms.

        EXAMPLES::

            sage: ModularForms(37).free_module()
            Vector space of dimension 3 over Rational Field
        """
    def prec(self, new_prec=None):
        """
        Set or get default initial precision for printing modular forms.

        INPUT:

        - ``new_prec`` -- positive integer (default: ``None``)

        OUTPUT: if ``new_prec`` is ``None``, returns the current precision

        EXAMPLES::

            sage: M = ModularForms(1,12, prec=3)
            sage: M.prec()
            3

        ::

            sage: M.basis()
            [q - 24*q^2 + O(q^3), 1 + 65520/691*q + 134250480/691*q^2 + O(q^3)]

        ::

            sage: M.prec(5)
            5
            sage: M.basis()
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + O(q^5),
             1 + 65520/691*q + 134250480/691*q^2 + 11606736960/691*q^3 + 274945048560/691*q^4 + O(q^5)]
        """
    def set_precision(self, n) -> None:
        """
        Set the default precision for displaying elements of this space.

        EXAMPLES::

            sage: m = ModularForms(Gamma1(5),2)
            sage: m.set_precision(10)
            sage: m.basis()
            [1 + 60*q^3 - 120*q^4 + 240*q^5 - 300*q^6 + 300*q^7 - 180*q^9 + O(q^10),
             q + 6*q^3 - 9*q^4 + 27*q^5 - 28*q^6 + 30*q^7 - 11*q^9 + O(q^10),
             q^2 - 4*q^3 + 12*q^4 - 22*q^5 + 30*q^6 - 24*q^7 + 5*q^8 + 18*q^9 + O(q^10)]
            sage: m.set_precision(5)
            sage: m.basis()
            [1 + 60*q^3 - 120*q^4 + O(q^5),
             q + 6*q^3 - 9*q^4 + O(q^5),
             q^2 - 4*q^3 + 12*q^4 + O(q^5)]
        """
    @cached_method
    def cuspidal_submodule(self):
        """
        Return the cuspidal submodule of this ambient module.

        EXAMPLES::

            sage: ModularForms(Gamma1(13)).cuspidal_submodule()
            Cuspidal subspace of dimension 2 of Modular Forms space of dimension 13 for
            Congruence Subgroup Gamma1(13) of weight 2 over Rational Field
        """
    @cached_method
    def eisenstein_submodule(self):
        """
        Return the Eisenstein submodule of this ambient module.

        EXAMPLES::

            sage: m = ModularForms(Gamma1(13),2); m
            Modular Forms space of dimension 13 for Congruence Subgroup Gamma1(13) of weight 2 over Rational Field
            sage: m.eisenstein_submodule()
            Eisenstein subspace of dimension 11 of Modular Forms space of dimension 13 for Congruence Subgroup Gamma1(13) of weight 2 over Rational Field
        """
    def new_submodule(self, p=None):
        """
        Return the new or `p`-new submodule of this ambient
        module.

        INPUT:

        - ``p`` -- (default: ``None``), if specified return only
          the `p`-new submodule

        EXAMPLES::

            sage: m = ModularForms(Gamma0(33),2); m
            Modular Forms space of dimension 6 for Congruence Subgroup Gamma0(33) of weight 2 over Rational Field
            sage: m.new_submodule()
            Modular Forms subspace of dimension 1 of Modular Forms space of dimension 6 for Congruence Subgroup Gamma0(33) of weight 2 over Rational Field

        Another example::

            sage: M = ModularForms(17,4)
            sage: N = M.new_subspace(); N
            Modular Forms subspace of dimension 4 of Modular Forms space of dimension 6 for Congruence Subgroup Gamma0(17) of weight 4 over Rational Field
            sage: N.basis()
            [q + 2*q^5 + O(q^6),
             q^2 - 3/2*q^5 + O(q^6),
             q^3 + O(q^6),
             q^4 - 1/2*q^5 + O(q^6)]

        ::

            sage: ModularForms(12,4).new_submodule()
            Modular Forms subspace of dimension 1 of Modular Forms space of dimension 9 for Congruence Subgroup Gamma0(12) of weight 4 over Rational Field

        Unfortunately (TODO) - `p`-new submodules aren't yet
        implemented::

            sage: m.new_submodule(3)            # not implemented
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: m.new_submodule(11)           # not implemented
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    @cached_method
    def eisenstein_params(self):
        """
        Return parameters that define all Eisenstein series in ``self``.

        OUTPUT: an immutable Sequence

        EXAMPLES::

            sage: m = ModularForms(Gamma0(22), 2)
            sage: v = m.eisenstein_params(); v
            [(Dirichlet character modulo 22 of conductor 1 mapping 13 |--> 1, Dirichlet character modulo 22 of conductor 1 mapping 13 |--> 1, 2), (Dirichlet character modulo 22 of conductor 1 mapping 13 |--> 1, Dirichlet character modulo 22 of conductor 1 mapping 13 |--> 1, 11), (Dirichlet character modulo 22 of conductor 1 mapping 13 |--> 1, Dirichlet character modulo 22 of conductor 1 mapping 13 |--> 1, 22)]
            sage: type(v)
            <class 'sage.structure.sequence.Sequence_generic'>
        """
    def eisenstein_series(self):
        """
        Return all Eisenstein series associated to this space.

        ::

            sage: ModularForms(27,2).eisenstein_series()
            [q^3 + O(q^6),
             q - 3*q^2 + 7*q^4 - 6*q^5 + O(q^6),
             1/12 + q + 3*q^2 + q^3 + 7*q^4 + 6*q^5 + O(q^6),
             1/3 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + O(q^6),
             13/12 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + O(q^6)]

        ::

            sage: ModularForms(Gamma1(5),3).eisenstein_series()
            [-1/5*zeta4 - 2/5 + q + (4*zeta4 + 1)*q^2 + (-9*zeta4 + 1)*q^3 + (4*zeta4 - 15)*q^4 + q^5 + O(q^6),
             q + (zeta4 + 4)*q^2 + (-zeta4 + 9)*q^3 + (4*zeta4 + 15)*q^4 + 25*q^5 + O(q^6),
             1/5*zeta4 - 2/5 + q + (-4*zeta4 + 1)*q^2 + (9*zeta4 + 1)*q^3 + (-4*zeta4 - 15)*q^4 + q^5 + O(q^6),
             q + (-zeta4 + 4)*q^2 + (zeta4 + 9)*q^3 + (-4*zeta4 + 15)*q^4 + 25*q^5 + O(q^6)]

        ::

            sage: eps = DirichletGroup(13).0^2
            sage: ModularForms(eps,2).eisenstein_series()
            [-7/13*zeta6 - 11/13 + q + (2*zeta6 + 1)*q^2 + (-3*zeta6 + 1)*q^3 + (6*zeta6 - 3)*q^4 - 4*q^5 + O(q^6),
             q + (zeta6 + 2)*q^2 + (-zeta6 + 3)*q^3 + (3*zeta6 + 3)*q^4 + 4*q^5 + O(q^6)]
        """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Compute the characteristic polynomial of the Hecke operator `T_n` acting
        on this space. Except in level 1, this is computed via modular symbols,
        and in particular is faster to compute than the matrix itself.

        EXAMPLES::

            sage: ModularForms(17,4).hecke_polynomial(2)
            x^6 - 16*x^5 + 18*x^4 + 608*x^3 - 1371*x^2 - 4968*x + 7776

        Check that this gives the same answer as computing the actual Hecke
        matrix (which is generally slower)::

            sage: ModularForms(17,4).hecke_matrix(2).charpoly()
            x^6 - 16*x^5 + 18*x^4 + 608*x^3 - 1371*x^2 - 4968*x + 7776
        """
