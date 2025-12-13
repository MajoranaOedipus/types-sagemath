from .fund_domain import M2Z as M2Z
from .manin_map import ManinMap as ManinMap
from .sigma0 import Sigma0 as Sigma0
from _typeshed import Incomplete
from sage.arith.misc import gcd as gcd, kronecker as kronecker, next_prime as next_prime
from sage.categories.action import Action as Action
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE

minusproj: Incomplete

class PSModSymAction(Action):
    def __init__(self, actor, MSspace) -> None:
        """
        Create the action.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: g = phi._map._codomain._act._Sigma0(matrix(ZZ,2,2,[1,2,3,4]))
            sage: phi * g # indirect doctest
            Modular symbol of level 11 with values in Sym^0 Q^2
        """

class PSModularSymbolElement(ModuleElement):
    def __init__(self, map_data, parent, construct: bool = False) -> None:
        """
        Initialize a modular symbol.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: phi = E.pollack_stevens_modular_symbol()
        """
    def dict(self):
        """
        Return dictionary on the modular symbol ``self``, where keys are
        generators and values are the corresponding values of ``self`` on
        generators.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: Set([x.moment(0) for x in phi.dict().values()]) == Set([-1/5, 1, 0])
            True
        """
    def weight(self):
        """
        Return the weight of this Pollack-Stevens modular symbol.

        This is `k-2`, where `k` is the usual notion of weight for modular
        forms!

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.weight()
            0
        """
    def values(self):
        """
        Return the values of the symbol ``self`` on our chosen generators.

        The generators are listed in ``self.dict()``.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: sorted(phi.dict())
            [
            [-1 -1]  [ 0 -1]  [1 0]
            [ 3  2], [ 1  3], [0 1]
            ]
            sage: sorted(phi.values()) == sorted(phi.dict().values())
            True
        """
    def plus_part(self):
        """
        Return the plus part of ``self`` -- i.e.
        ``self + self | [1,0,0,-1]``.

        Note that we haven't divided by 2.  Is this a problem?

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: (phi.plus_part()+phi.minus_part()) == 2 * phi
            True
        """
    def minus_part(self):
        """
        Return the minus part of self -- i.e. self - self | [1,0,0,-1]

        Note that we haven't divided by 2.  Is this a problem?

        OUTPUT:

        - self -- self | [1,0,0,-1]

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: (phi.plus_part()+phi.minus_part()) == phi * 2
            True
        """
    def hecke(self, ell, algorithm: str = 'prep'):
        """
        Return ``self`` | `T_{\\ell}` by making use of the precomputations in
        ``self.prep_hecke()``.

        INPUT:

        - ``ell`` -- a prime

        - ``algorithm`` -- string, either 'prep' (default) or
          'naive'

        OUTPUT:

        - The image of this element under the Hecke operator
          `T_{\\ell}`

        ALGORITHMS:

        - If ``algorithm == 'prep'``, precomputes a list of matrices
          that only depend on the level, then uses them to speed up
          the action.

        - If ``algorithm == 'naive'``, just acts by the matrices
          defining the Hecke operator.  That is, it computes
          sum_a self | [1,a,0,ell] + self | [ell,0,0,1],
          the last term occurring only if the level is prime to ell.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: phi.hecke(2) == phi * E.ap(2)
            True
            sage: phi.hecke(3) == phi * E.ap(3)
            True
            sage: phi.hecke(5) == phi * E.ap(5)
            True
            sage: phi.hecke(101) == phi * E.ap(101)
            True

            sage: all(phi.hecke(p, algorithm='naive') == phi * E.ap(p) for p in [2,3,5,101]) # long time
            True
        """
    def valuation(self, p=None):
        """
        Return the valuation of ``self`` at `p`.

        Here the valuation is the minimum of the valuations of the
        values of ``self``.

        INPUT:

        - ``p`` -- prime

        OUTPUT: the valuation of ``self`` at `p`

        EXAMPLES::

           sage: E = EllipticCurve('11a')
           sage: phi = E.pollack_stevens_modular_symbol()
           sage: phi.values()
           [-1/5, 1, 0]
           sage: phi.valuation(2)
           0
           sage: phi.valuation(3)
           0
           sage: phi.valuation(5)
           -1
           sage: phi.valuation(7)
           0
           sage: phi.valuation()
           Traceback (most recent call last):
           ...
           ValueError: you must specify a prime

           sage: phi2 = phi.lift(11, M=2)
           sage: phi2.valuation()
           0
           sage: phi2.valuation(3)
           Traceback (most recent call last):
           ...
           ValueError: inconsistent prime
           sage: phi2.valuation(11)
           0
        """
    def diagonal_valuation(self, p):
        """
        Return the minimum of the diagonal valuation on the values of ``self``.

        INPUT:

        - ``p`` -- a positive integral prime

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: phi.diagonal_valuation(2)
            0
            sage: phi.diagonal_valuation(3)
            0
            sage: phi.diagonal_valuation(5)
            -1
            sage: phi.diagonal_valuation(7)
            0
        """
    @cached_method
    def is_Tq_eigensymbol(self, q, p=None, M=None):
        """
        Determine if ``self`` is an eigenvector for `T_q` modulo `p^M`.

        INPUT:

        - ``q`` -- prime of the Hecke operator

        - ``p`` -- prime we are working modulo

        - ``M`` -- degree of accuracy of approximation

        OUTPUT: boolean

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: phi_ord = phi.p_stabilize(p = 3, ap = E.ap(3), M = 10, ordinary = True)
            sage: phi_ord.is_Tq_eigensymbol(2,3,10)
            True
            sage: phi_ord.is_Tq_eigensymbol(2,3,100)
            False
            sage: phi_ord.is_Tq_eigensymbol(2,3,1000)
            False
            sage: phi_ord.is_Tq_eigensymbol(3,3,10)
            True
            sage: phi_ord.is_Tq_eigensymbol(3,3,100)
            False
        """
    @cached_method
    def Tq_eigenvalue(self, q, p=None, M=None, check: bool = True):
        """
        Eigenvalue of `T_q` modulo `p^M`.

        INPUT:

        - ``q`` -- prime of the Hecke operator

        - ``p`` -- prime we are working modulo (default: ``None``)

        - ``M`` -- degree of accuracy of approximation (default: ``None``)

        - ``check`` -- check that ``self`` is an eigensymbol

        OUTPUT:

        - Constant `c` such that `self|T_q - c * self` has valuation greater than
          or equal to `M` (if it exists), otherwise raises ValueError

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.values()
            [-1/5, 1, 0]
            sage: phi_ord = phi.p_stabilize(p = 3, ap = E.ap(3), M = 10, ordinary = True)
            sage: phi_ord.Tq_eigenvalue(2,3,10) + 2
            O(3^10)

            sage: phi_ord.Tq_eigenvalue(3,3,10)
            2 + 3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 3^8 + 2*3^9 + O(3^10)
            sage: phi_ord.Tq_eigenvalue(3,3,100)
            Traceback (most recent call last):
            ...
            ValueError: result not determined to high enough precision
        """
    def is_ordinary(self, p=None, P=None) -> bool:
        """
        Return ``True`` if the `p`-th eigenvalue is a `p`-adic unit.

        INPUT:

        - ``p`` -- a positive integral prime, or ``None`` (default: ``None``)
        - ``P`` -- a prime of the base ring above `p`, or ``None``.
          This is ignored unless the base ring is a number field

        OUTPUT: boolean

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phi.is_ordinary(2)
            False
            sage: E.ap(2)
            -2
            sage: phi.is_ordinary(3)
            True
            sage: E.ap(3)
            -1
            sage: phip = phi.p_stabilize(3,20)
            sage: phip.is_ordinary()
            True

        A number field example. Here there are multiple primes above `p`, and
        `\\phi` is ordinary at one but not the other.::

            sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
            sage: f = Newforms(32, 8, names='a')[1]
            sage: phi = ps_modsym_from_simple_modsym_space(f.modular_symbols(1))
            sage: (p1, _), (p2, _) = phi.base_ring().ideal(3).factor()
            sage: phi.is_ordinary(p1) != phi.is_ordinary(p2)
            True
            sage: phi.is_ordinary(3)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal
        """
    def evaluate_twisted(self, a, chi):
        """
        Return `\\Phi_{\\chi}(\\{a/p\\}-\\{\\infty\\})` where `\\Phi` is ``self`` and
        `\\chi` is a quadratic character

        INPUT:

        - ``a`` -- integer in the range range(p)
        - ``chi`` -- the modulus of a quadratic character

        OUTPUT:

        The distribution `\\Phi_{\\chi}(\\{a/p\\}-\\{\\infty\\})`.

        EXAMPLES::

            sage: E = EllipticCurve('17a1')
            sage: L = E.padic_lseries(5, implementation='pollackstevens', precision=4) #long time
            sage: D = L.quadratic_twist()          # long time
            sage: L.symbol().evaluate_twisted(1,D) # long time
            (1 + 5 + 3*5^2 + 5^3 + O(5^4), 5^2 + O(5^3), 1 + O(5^2), 2 + O(5))

            sage: E = EllipticCurve('40a4')
            sage: L = E.padic_lseries(7, implementation='pollackstevens', precision=4) #long time
            sage: D = L.quadratic_twist()          # long time
            sage: L.symbol().evaluate_twisted(1,D) # long time
            (4 + 6*7 + 3*7^2 + O(7^4), 6*7 + 6*7^2 + O(7^3), 6 + O(7^2), 1 + O(7))

        TESTS:

        Check for :issue:`32878`::

            sage: E = EllipticCurve('11a1')
            sage: L = E.padic_lseries(3, implementation='pollackstevens', precision=4)
            sage: D = 5
            sage: L.symbol().evaluate_twisted(1, D)
            (2 + 3 + 2*3^2 + O(3^4), 2 + 3 + O(3^3), 2 + 3 + O(3^2), 2 + O(3))
        """

class PSModularSymbolElement_symk(PSModularSymbolElement):
    def p_stabilize(self, p=None, M: int = 20, alpha=None, ap=None, new_base_ring=None, ordinary: bool = True, check: bool = True):
        """
        Return the `p`-stabilization of ``self`` to level `N p` on which `U_p`
        acts by `\\alpha`.

        Note that since `\\alpha` is `p`-adic, the resulting symbol
        is just an approximation to the true `p`-stabilization
        (depending on how well `\\alpha` is approximated).

        INPUT:

        - ``p`` -- prime not dividing the level of self

        - ``M`` -- (default: 20) precision of `\\QQ_p`

        - ``alpha`` -- `U_p` eigenvalue

        - ``ap`` -- Hecke eigenvalue

        - ``new_base_ring`` -- change of base ring

        - ``ordinary`` -- boolean (default: ``True``); whether to return the
          ordinary (at ``p``) eigensymbol

        - ``check`` -- boolean (default: ``True``); whether to perform extra
          sanity checks

        OUTPUT:

        A modular symbol with the same Hecke eigenvalues as
        ``self`` away from `p` and eigenvalue `\\alpha` at `p`.
        The eigenvalue `\\alpha` depends on the parameter ``ordinary``.

        If ``ordinary`` == True: the unique modular symbol of level
        `N p` with the same Hecke eigenvalues as ``self`` away from
        `p` and unit eigenvalue at `p`; else  the unique modular
        symbol of level `N p` with the same Hecke eigenvalues as
        ``self`` away from `p` and non-unit eigenvalue at `p`.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: p = 5
            sage: prec = 4
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: phis = phi.p_stabilize(p,M = prec)
            sage: phis
            Modular symbol of level 55 with values in Sym^0 Q_5^2
            sage: phis.hecke(7) == phis*E.ap(7)
            True
            sage: phis.hecke(5) == phis*E.ap(5)
            False
            sage: phis.hecke(3) == phis*E.ap(3)
            True
            sage: phis.Tq_eigenvalue(5)
            1 + 4*5 + 3*5^2 + 2*5^3 + O(5^4)
            sage: phis.Tq_eigenvalue(5,M = 3)
            1 + 4*5 + 3*5^2 + O(5^3)

            sage: phis = phi.p_stabilize(p,M = prec,ordinary=False)
            sage: phis.Tq_eigenvalue(5)
            5 + 5^2 + 2*5^3 + O(5^5)

        A complicated example (with nontrivial character)::

            sage: chi = DirichletGroup(24)([-1, -1, -1])
            sage: f = Newforms(chi,names='a')[0]
            sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
            sage: phi = ps_modsym_from_simple_modsym_space(f.modular_symbols(1))
            sage: phi11, h11 = phi.completions(11,20)[0]
            sage: phi11s = phi11.p_stabilize()
            sage: phi11s.is_Tq_eigensymbol(11) # long time
            True
        """
    def completions(self, p, M):
        """
        If `K` is the base_ring of self, this function takes all maps
        `K\\to \\QQ_p` and applies them to ``self`` return a list of
        (modular symbol,map: `K\\to \\QQ_p`) as map varies over all such maps.

        .. NOTE::

            This only returns all completions when `p` splits completely in `K`

        INPUT:

        - ``p`` -- prime

        - ``M`` -- precision

        OUTPUT:

        - A list of tuples (modular symbol,map: `K\\to \\QQ_p`) as map varies over all such maps

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
            sage: D = ModularSymbols(67,2,1).cuspidal_submodule().new_subspace().decomposition()[1]
            sage: f = ps_modsym_from_simple_modsym_space(D)
            sage: S = f.completions(41,10); S
            [(Modular symbol of level 67 with values in Sym^0 Q_41^2, Ring morphism:
              From: Number Field in alpha with defining polynomial x^2 + 3*x + 1
              To:   41-adic Field with capped relative precision 10
              Defn: alpha |--> 5 + 22*41 + 19*41^2 + 10*41^3 + 28*41^4 + 22*41^5 + 9*41^6 + 25*41^7 + 40*41^8 + 8*41^9 + O(41^10)), (Modular symbol of level 67 with values in Sym^0 Q_41^2, Ring morphism:
              From: Number Field in alpha with defining polynomial x^2 + 3*x + 1
              To:   41-adic Field with capped relative precision 10
              Defn: alpha |--> 33 + 18*41 + 21*41^2 + 30*41^3 + 12*41^4 + 18*41^5 + 31*41^6 + 15*41^7 + 32*41^9 + O(41^10))]
            sage: TestSuite(S[0][0]).run(skip=['_test_category'])
        """
    def lift(self, p=None, M=None, alpha=None, new_base_ring=None, algorithm=None, eigensymbol: bool = False, check: bool = True):
        """
        Return a (`p`-adic) overconvergent modular symbol with
        `M` moments which lifts ``self`` up to an Eisenstein error.

        Here the Eisenstein error is a symbol whose system of Hecke
        eigenvalues equals `\\ell+1` for `T_\\ell` when `\\ell`
        does not divide `Np` and 1 for `U_q` when `q` divides `Np`.

        INPUT:

        - ``p`` -- prime

        - ``M`` -- integer equal to the number of moments

        - ``alpha`` -- `U_p` eigenvalue

        - ``new_base_ring`` -- change of base ring

        - ``algorithm`` -- ``'stevens'`` or ``'greenberg'`` (default:
          ``'stevens'``)

        - ``eigensymbol`` -- if ``True``, lifts to Hecke eigensymbol (self must
          be a `p`-ordinary eigensymbol)

        (Note: ``eigensymbol = True`` does *not* just indicate to the code that
        ``self`` is an eigensymbol; it solves a wholly different problem, lifting
        an eigensymbol to an eigensymbol.)

        OUTPUT:

        An overconvergent modular symbol whose specialization equals self, up
        to some Eisenstein error if ``eigensymbol`` is False. If ``eigensymbol
        = True`` then the output will be an overconvergent Hecke eigensymbol
        (and it will lift the input exactly, the Eisenstein error disappears).

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: f = E.pollack_stevens_modular_symbol()
            sage: g = f.lift(11,4,algorithm='stevens',eigensymbol=True)
            sage: g.is_Tq_eigensymbol(2)
            True
            sage: g.Tq_eigenvalue(3)
            10 + 10*11 + 10*11^2 + 10*11^3 + O(11^4)
            sage: g.Tq_eigenvalue(11)
            1 + O(11^4)

        We check that lifting and then specializing gives back the original symbol::

            sage: g.specialize() == f
            True

        Another example, which showed precision loss in an earlier version of the code::

            sage: E = EllipticCurve('37a')
            sage: p = 5
            sage: prec = 4
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: Phi = phi.p_stabilize_and_lift(p,prec, algorithm='stevens', eigensymbol=True) # long time
            sage: Phi.Tq_eigenvalue(5,M = 4) # long time
            3 + 2*5 + 4*5^2 + 2*5^3 + O(5^4)

        Another example::

            sage: from sage.modular.pollack_stevens.padic_lseries import pAdicLseries
            sage: E = EllipticCurve('37a')
            sage: p = 5
            sage: prec = 6
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: Phi = phi.p_stabilize_and_lift(p=p,M=prec,alpha=None,algorithm='stevens',eigensymbol=True) #long time
            sage: L = pAdicLseries(Phi)          # long time
            sage: L.symbol() is Phi              # long time
            True

        Examples using Greenberg's algorithm::

            sage: E = EllipticCurve('11a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: Phi = phi.lift(11,8,algorithm='greenberg',eigensymbol=True)
            sage: Phi2 = phi.lift(11,8,algorithm='stevens',eigensymbol=True)
            sage: Phi == Phi2
            True

        An example in higher weight::

            sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
            sage: f = ps_modsym_from_simple_modsym_space(Newforms(7, 4)[0].modular_symbols(1))
            sage: fs = f.p_stabilize(5)
            sage: FsG = fs.lift(M=6, eigensymbol=True,algorithm='greenberg') # long time
            sage: FsG.values()[0]                                            # long time
            5^-1 * (2*5 + 5^2 + 3*5^3 + 4*5^4 + O(5^7), O(5^6), 2*5^2 + 3*5^3 + O(5^5), O(5^4), 5^2 + O(5^3), O(5^2))
            sage: FsS = fs.lift(M=6, eigensymbol=True,algorithm='stevens')   # long time
            sage: FsS == FsG                                                 # long time
            True
        """
    def p_stabilize_and_lift(self, p, M, alpha=None, ap=None, new_base_ring=None, ordinary: bool = True, algorithm: str = 'greenberg', eigensymbol: bool = False, check: bool = True):
        """
        `p`-stabilize and lift ``self``.

        INPUT:

        - ``p`` -- prime, not dividing the level of self

        - ``M`` -- precision

        - ``alpha`` -- (default: ``None``) the `U_p` eigenvalue, if known

        - ``ap`` -- (default: ``None``) the Hecke eigenvalue at p (before
          stabilizing), if known

        - ``new_base_ring`` -- (default: ``None``) if specified, force the
          resulting eigensymbol to take values in the given ring

        - ``ordinary`` -- boolean (default: ``True``); whether to return the
          ordinary (at ``p``) eigensymbol

        - ``algorithm`` -- string (default: ``'greenberg'``); either
          ``'greenberg'`` or ``'stevens'``, specifying whether to use
          the lifting algorithm of M.Greenberg or that of Pollack--Stevens.
          The latter one solves the difference equation, which is not needed.
          The option to use Pollack--Stevens' algorithm here is just for
          historical reasons.

        - ``eigensymbol`` -- boolean (default: ``False``); if ``True``, return
          an overconvergent eigensymbol. Otherwise just perform a naive lift

        - ``check`` -- boolean (default: ``True``); whether to perform extra
          sanity checks

        OUTPUT: `p`-stabilized and lifted version of ``self``

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: f = E.pollack_stevens_modular_symbol()
            sage: g = f.p_stabilize_and_lift(3,10)  # long time
            sage: g.Tq_eigenvalue(5)                # long time
            1 + O(3^10)
            sage: g.Tq_eigenvalue(7)                # long time
            1 + 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^5 + 2*3^6 + 2*3^7 + 2*3^8 + 2*3^9 + O(3^10)
            sage: g.Tq_eigenvalue(3)                # long time
            2 + 3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 3^8 + 2*3^9 + O(3^10)
        """

class PSModularSymbolElement_dist(PSModularSymbolElement):
    def reduce_precision(self, M):
        """
        Only hold on to `M` moments of each value of ``self``.

        EXAMPLES::

            sage: D = OverconvergentDistributions(0, 5, 10)
            sage: M = PollackStevensModularSymbols(Gamma0(5), coefficients=D)
            sage: f = M(1)
            sage: f.reduce_precision(1)
            Modular symbol of level 5 with values in Space of 5-adic distributions with k=0 action and precision cap 10
        """
    def precision_relative(self):
        """
        Return the number of moments of each value of ``self``.

        EXAMPLES::

            sage: D = OverconvergentDistributions(0, 5, 10)
            sage: M = PollackStevensModularSymbols(Gamma0(5), coefficients=D)
            sage: f = M(1)
            sage: f.precision_relative()
            1
        """
    def specialize(self, new_base_ring=None):
        """
        Return the underlying classical symbol of weight `k`.

        Namely, this applies the canonical map `D_k \\to Sym^k` to all
        values of ``self``.

        EXAMPLES::

            sage: D = OverconvergentDistributions(0, 5, 10);  M = PollackStevensModularSymbols(Gamma0(5), coefficients=D); M
            Space of overconvergent modular symbols for Congruence Subgroup Gamma0(5) with sign 0
            and values in Space of 5-adic distributions with k=0 action and precision cap 10
            sage: f = M(1)
            sage: f.specialize()
            Modular symbol of level 5 with values in Sym^0 Z_5^2
            sage: f.specialize().values()
            [1 + O(5), 1 + O(5), 1 + O(5)]
            sage: f.values()
            [1 + O(5), 1 + O(5), 1 + O(5)]
            sage: f.specialize().parent()
            Space of modular symbols for Congruence Subgroup Gamma0(5) with sign 0 and values in Sym^0 Z_5^2
            sage: f.specialize().parent().coefficient_module()
            Sym^0 Z_5^2
            sage: f.specialize().parent().coefficient_module().is_symk()
            True
            sage: f.specialize(Qp(5,20))
            Modular symbol of level 5 with values in Sym^0 Q_5^2
        """
    def padic_lseries(self, *args, **kwds):
        """
        Return the `p`-adic `L`-series of this modular symbol.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: L = phi.lift(37, M=6, eigensymbol=True).padic_lseries(); L  # long time
            37-adic L-series of Modular symbol of level 37 with values in Space of 37-adic distributions with k=0 action and precision cap 7
            sage: L.series(2) # long time
            O(37^6) + (4 + 37 + 36*37^2 + 19*37^3 + 21*37^4 + O(37^5))*T + O(T^2)
        """
