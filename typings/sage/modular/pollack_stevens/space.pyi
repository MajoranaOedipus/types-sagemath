r"""
Pollack-Stevens' modular symbols spaces

This module contains a class for spaces of modular symbols that use Glenn
Stevens' conventions, as explained in [PS2011]_.

There are two main differences between the modular symbols in this directory
and the ones in :mod:`sage.modular.modsym`:

- There is a shift in the weight: weight `k=0` here corresponds to weight `k=2`
  there.

- There is a duality: these modular symbols are functions from
  `\textrm{Div}^0(P^1(\QQ))` (cohomological objects), the others are formal linear
  combinations of `\textrm{Div}^0(P^1(\QQ))` (homological objects).

EXAMPLES:

First we create the space of modular symbols of weight 0 (`k=2`) and level 11::

    sage: M = PollackStevensModularSymbols(Gamma0(11), 0); M
    Space of modular symbols for Congruence Subgroup Gamma0(11) with sign 0 and values in Sym^0 Q^2

One can also create a space of overconvergent modular symbols, by specifying a prime and a precision::

    sage: M = PollackStevensModularSymbols(Gamma0(11), p = 5, prec_cap = 10, weight = 0); M
    Space of overconvergent modular symbols for Congruence Subgroup Gamma0(11) with sign 0 and values in Space of 5-adic distributions with k=0 action and precision cap 10

Currently not much functionality is available on the whole space, and these
spaces are mainly used as parents for the modular symbols. These can be constructed from the corresponding
classical modular symbols (or even elliptic curves) as follows::

    sage: A = ModularSymbols(13, sign=1, weight=4).decomposition()[0]
    sage: A.is_cuspidal()
    True
    sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
    sage: f = ps_modsym_from_simple_modsym_space(A); f
    Modular symbol of level 13 with values in Sym^2 Q^2
    sage: f.values()
    [(-13, 0, -1),
     (247/2, 13/2, -6),
     (39/2, 117/2, 42),
     (-39/2, 39, 111/2),
     (-247/2, -117, -209/2)]
    sage: f.parent()
    Space of modular symbols for Congruence Subgroup Gamma0(13) with sign 1 and values in Sym^2 Q^2

::

    sage: E = EllipticCurve('37a1')
    sage: phi = E.pollack_stevens_modular_symbol(); phi
    Modular symbol of level 37 with values in Sym^0 Q^2
    sage: phi.values()
    [0, 1, 0, 0, 0, -1, 1, 0, 0]
    sage: phi.parent()
    Space of modular symbols for Congruence Subgroup Gamma0(37) with sign 0 and values in Sym^0 Q^2
"""
from .distributions import OverconvergentDistributions as OverconvergentDistributions, Symk as Symk
from .fund_domain import ManinRelations as ManinRelations
from .manin_map import ManinMap as ManinMap
from .modsym import PSModSymAction as PSModSymAction, PSModularSymbolElement as PSModularSymbolElement, PSModularSymbolElement_dist as PSModularSymbolElement_dist, PSModularSymbolElement_symk as PSModularSymbolElement_symk
from .sigma0 import Sigma0 as Sigma0, Sigma0Element as Sigma0Element
from sage.modular.arithgroup.arithgroup_element import ArithmeticSubgroupElement as ArithmeticSubgroupElement
from sage.modular.dirichlet import DirichletCharacter as DirichletCharacter
from sage.modules.module import Module as Module
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.factory import UniqueFactory as UniqueFactory

class PollackStevensModularSymbols_factory(UniqueFactory):
    '''
    Create a space of Pollack-Stevens modular symbols.

    INPUT:

    - ``group`` -- integer or congruence subgroup

    - ``weight`` -- integer `\\ge 0`, or ``None``

    - ``sign`` -- integer; -1, 0, 1

    - ``base_ring`` -- ring or ``None``

    - ``p`` -- prime or ``None``

    - ``prec_cap`` -- positive integer or ``None``

    - ``coefficients`` -- the coefficient module (a special type of module,
      typically distributions), or ``None``

    If an explicit coefficient module is given, then the arguments ``weight``,
    ``base_ring``, ``prec_cap``, and ``p`` are redundant and must be ``None``.
    They are only relevant if ``coefficients`` is ``None``, in which case the
    coefficient module is inferred from the other data.

    .. NOTE::

        We emphasize that in the Pollack-Stevens notation, the
        ``weight`` is the usual weight minus 2, so a classical weight
        2 modular form corresponds to a modular symbol of "weight 0".

    EXAMPLES::

        sage: M = PollackStevensModularSymbols(Gamma0(7), weight=0, prec_cap = None); M
        Space of modular symbols for Congruence Subgroup Gamma0(7) with sign 0 and values in Sym^0 Q^2

    An example with an explicit coefficient module::

        sage: D = OverconvergentDistributions(3, 7, prec_cap=10)
        sage: M = PollackStevensModularSymbols(Gamma0(7), coefficients=D); M
        Space of overconvergent modular symbols for Congruence Subgroup Gamma0(7) with sign 0 and values in Space of 7-adic distributions with k=3 action and precision cap 10

    TESTS::

        sage: TestSuite(PollackStevensModularSymbols).run()
    '''
    def create_key(self, group, weight=None, sign: int = 0, base_ring=None, p=None, prec_cap=None, coefficients=None):
        """
        Sanitize input.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3, 7, prec_cap=10)
            sage: M = PollackStevensModularSymbols(Gamma0(7), coefficients=D) # indirect doctest
        """
    def create_object(self, version, key):
        """
        Create a space of modular symbols from ``key``.

        INPUT:

        - ``version`` -- the version of the object to create

        - ``key`` -- tuple of parameters, as created by :meth:`create_key`

        EXAMPLES::

            sage: D = OverconvergentDistributions(5, 7, 15)
            sage: M = PollackStevensModularSymbols(Gamma0(7), coefficients=D) # indirect doctest
            sage: M2 = PollackStevensModularSymbols(Gamma0(7), coefficients=D) # indirect doctest
            sage: M is M2
            True
        """

PollackStevensModularSymbols: PollackStevensModularSymbols_factory

class PollackStevensModularSymbolspace(Module):
    """
    A class for spaces of modular symbols that use Glenn Stevens' conventions.
    This class should not be instantiated directly by the user: this is handled
    by the factory object :class:`PollackStevensModularSymbols_factory`.

    INPUT:

    - ``group`` -- congruence subgroup

    - ``coefficients`` -- a coefficient module

    - ``sign`` -- (default: 0) 0, -1, or 1

    EXAMPLES::

        sage: D = OverconvergentDistributions(2, 11)
        sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D); M.sign()
        0
        sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D, sign=-1); M.sign()
        -1
        sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D, sign=1); M.sign()
        1
    """
    Element: Incomplete
    def __init__(self, group, coefficients, sign: int = 0) -> None:
        """
        INPUT:

        See :class:`PollackStevensModularSymbolspace`

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11)
            sage: M = PollackStevensModularSymbols(Gamma0(11), coefficients=D)
            sage: type(M)
            <class 'sage.modular.pollack_stevens.space.PollackStevensModularSymbolspace_with_category'>
            sage: TestSuite(M).run()
        """
    def source(self):
        """
        Return the domain of the modular symbols in this space.

        OUTPUT: a :class:`sage.modular.pollack_stevens.fund_domain.PollackStevensModularDomain`

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11)
            sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D)
            sage: M.source()
            Manin Relations of level 2
        """
    def coefficient_module(self):
        """
        Return the coefficient module of this space.

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11)
            sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D)
            sage: M.coefficient_module()
            Space of 11-adic distributions with k=2 action and precision cap 20
            sage: M.coefficient_module() is D
            True
        """
    def group(self):
        """
        Return the congruence subgroup of this space.

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 5)
            sage: G = Gamma0(23)
            sage: M = PollackStevensModularSymbols(G, coefficients=D)
            sage: M.group()
            Congruence Subgroup Gamma0(23)
            sage: D = Symk(4)
            sage: G = Gamma1(11)
            sage: M = PollackStevensModularSymbols(G, coefficients=D)
            sage: M.group()
            Congruence Subgroup Gamma1(11)
        """
    def sign(self):
        """
        Return the sign of this space.

        EXAMPLES::

            sage: D = OverconvergentDistributions(3, 17)
            sage: M = PollackStevensModularSymbols(Gamma(5), coefficients=D)
            sage: M.sign()
            0
            sage: D = Symk(4)
            sage: M = PollackStevensModularSymbols(Gamma1(8), coefficients=D, sign=-1)
            sage: M.sign()
            -1
        """
    def ngens(self):
        """
        Return the number of generators defining this space.

        EXAMPLES::

            sage: D = OverconvergentDistributions(4, 29)
            sage: M = PollackStevensModularSymbols(Gamma1(12), coefficients=D)
            sage: M.ngens()
            5
            sage: D = Symk(2)
            sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D)
            sage: M.ngens()
            2
        """
    def ncoset_reps(self):
        """
        Return the number of coset representatives defining the domain of the
        modular symbols in this space.

        OUTPUT:

        The number of coset representatives stored in the manin relations.
        (Just the size of `P^1(\\ZZ/N\\ZZ)`)

        EXAMPLES::

            sage: D = Symk(2)
            sage: M = PollackStevensModularSymbols(Gamma0(2), coefficients=D)
            sage: M.ncoset_reps()
            3
        """
    def level(self):
        """
        Return the level `N`, where this space is of level `\\Gamma_0(N)`.

        EXAMPLES::

            sage: D = OverconvergentDistributions(7, 11)
            sage: M = PollackStevensModularSymbols(Gamma1(14), coefficients=D)
            sage: M.level()
            14
        """
    def precision_cap(self):
        """
        Return the number of moments of each element of this space.

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 5)
            sage: M = PollackStevensModularSymbols(Gamma1(13), coefficients=D)
            sage: M.precision_cap()
            20
            sage: D = OverconvergentDistributions(3, 7, prec_cap=10)
            sage: M = PollackStevensModularSymbols(Gamma0(7), coefficients=D)
            sage: M.precision_cap()
            10
        """
    def weight(self):
        '''
        Return the weight of this space.

        .. WARNING::

            We emphasize that in the Pollack-Stevens notation, this is
            the usual weight minus 2, so a classical weight 2 modular
            form corresponds to a modular symbol of "weight 0".

        EXAMPLES::

            sage: D = Symk(5)
            sage: M = PollackStevensModularSymbols(Gamma1(7), coefficients=D)
            sage: M.weight()
            5
        '''
    def prime(self):
        """
        Return the prime of this space.

        EXAMPLES::

            sage: D = OverconvergentDistributions(2, 11)
            sage: M = PollackStevensModularSymbols(Gamma(2), coefficients=D)
            sage: M.prime()
            11
        """
    def change_ring(self, new_base_ring):
        """
        Change the base ring of this space to ``new_base_ring``.

        INPUT:

        - ``new_base_ring`` -- a ring

        OUTPUT: a space of modular symbols over the specified base

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.distributions import Symk
            sage: D = Symk(4)
            sage: M = PollackStevensModularSymbols(Gamma(6), coefficients=D); M
            Space of modular symbols for Congruence Subgroup Gamma(6) with sign 0 and values in Sym^4 Q^2
            sage: M.change_ring(Qp(5,8))
            Space of modular symbols for Congruence Subgroup Gamma(6) with sign 0 and values in Sym^4 Q_5^2
        """
    def random_element(self, M=None):
        """
        Return a random overconvergent modular symbol in this space with `M` moments.

        INPUT:

        - ``M`` -- positive integer

        OUTPUT: an element of the modular symbol space with `M` moments

        Returns a random element in this space by randomly choosing
        values of distributions on all but one divisor, and solves the
        difference equation to determine the value on the last
        divisor. ::

            sage: D = OverconvergentDistributions(2, 11)
            sage: M = PollackStevensModularSymbols(Gamma0(11), coefficients=D)
            sage: M.random_element(10)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

def cusps_from_mat(g):
    """
    Return the cusps associated to an element of a congruence subgroup.

    INPUT:

    - ``g`` -- an element of a congruence subgroup or a matrix

    OUTPUT: a tuple of cusps associated to ``g``

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.space import cusps_from_mat
        sage: g = SL2Z.one()
        sage: cusps_from_mat(g)
        (+Infinity, 0)

    You can also just give the matrix of ``g``::

        sage: type(g)
        <class 'sage.modular.arithgroup.arithgroup_element.ArithmeticSubgroupElement'>
        sage: cusps_from_mat(g.matrix())
        (+Infinity, 0)

    Another example::

        sage: from sage.modular.pollack_stevens.space import cusps_from_mat
        sage: g = GammaH(3, [2]).generators()[1].matrix(); g
        [-1  1]
        [-3  2]
        sage: cusps_from_mat(g)
        (1/3, 1/2)
    """
def ps_modsym_from_elliptic_curve(E, sign: int = 0, implementation: str = 'eclib'):
    """
    Return the overconvergent modular symbol associated to
    an elliptic curve defined over the rationals.

    INPUT:

    - ``E`` -- an elliptic curve defined over the rationals

    - ``sign`` -- the sign (default: 0). If nonzero, returns either
      the plus (if ``sign`` == 1) or the minus (if ``sign`` == -1) modular
      symbol. The default of 0 returns the sum of the plus and minus symbols.

    - ``implementation`` -- either ``'eclib'`` (default) or ``'sage'``. This
      determines which implementation of the underlying classical
      modular symbols is used.

    OUTPUT: the overconvergent modular symbol associated to ``E``

    EXAMPLES::

        sage: E = EllipticCurve('113a1')
        sage: symb = E.pollack_stevens_modular_symbol() # indirect doctest
        sage: symb
        Modular symbol of level 113 with values in Sym^0 Q^2
        sage: symb.values()
        [-1/2, 1, -1, 0, 0, 1, 1, -1, 0, -1, 0, 0, 0, 1, -1, 0, 0, 0, 1, 0, 0]

        sage: E = EllipticCurve([0,1])
        sage: symb = E.pollack_stevens_modular_symbol()
        sage: symb.values()
        [-1/6, 1/3, 1/2, 1/6, -1/6, 1/3, -1/3, -1/2, -1/6, 1/6, 0, -1/6, -1/6]
    """
def ps_modsym_from_simple_modsym_space(A, name: str = 'alpha'):
    """
    Return some choice -- only well defined up a nonzero scalar (!) -- of an
    overconvergent modular symbol that corresponds to ``A``.

    INPUT:

    - ``A`` -- nonzero simple Hecke equivariant new space of modular symbols,
      which need not be cuspidal

    OUTPUT:

    A choice of corresponding overconvergent modular symbols; when dim(A)>1,
    we make an arbitrary choice of defining polynomial for the codomain field.

    EXAMPLES:

    The level 11 example::

        sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
        sage: A = ModularSymbols(11, sign=1, weight=2).decomposition()[0]
        sage: A.is_cuspidal()
        True
        sage: f = ps_modsym_from_simple_modsym_space(A); f
        Modular symbol of level 11 with values in Sym^0 Q^2
        sage: f.values()
        [1, -5/2, -5/2]
        sage: f.weight()         # this is A.weight()-2  !!!!!!
        0

    And the -1 sign for the level 11 example::

        sage: A = ModularSymbols(11, sign=-1, weight=2).decomposition()[0]
        sage: f = ps_modsym_from_simple_modsym_space(A); f.values()
        [0, 1, -1]

    A does not have to be cuspidal; it can be Eisenstein::

        sage: A = ModularSymbols(11, sign=1, weight=2).decomposition()[1]
        sage: A.is_cuspidal()
        False
        sage: f = ps_modsym_from_simple_modsym_space(A); f
        Modular symbol of level 11 with values in Sym^0 Q^2
        sage: f.values()
        [1, 0, 0]

    We create the simplest weight 2 example in which ``A`` has dimension
    bigger than 1::

        sage: A = ModularSymbols(23, sign=1, weight=2).decomposition()[0]
        sage: f = ps_modsym_from_simple_modsym_space(A); f.values()
        [1, 0, 0, 0, 0]
        sage: A = ModularSymbols(23, sign=-1, weight=2).decomposition()[0]
        sage: f = ps_modsym_from_simple_modsym_space(A); f.values()
        [0, 1, -alpha, alpha, -1]
        sage: f.base_ring()
        Number Field in alpha with defining polynomial x^2 + x - 1

    We create the +1 modular symbol attached to the weight 12 modular form ``Delta``::

        sage: A = ModularSymbols(1, sign=+1, weight=12).decomposition()[0]
        sage: f = ps_modsym_from_simple_modsym_space(A); f
        Modular symbol of level 1 with values in Sym^10 Q^2
        sage: f.values()
        [(-1620/691, 0, 1, 0, -9/14, 0, 9/14, 0, -1, 0, 1620/691), (1620/691, 1620/691, 929/691, -453/691, -29145/9674, -42965/9674, -2526/691, -453/691, 1620/691, 1620/691, 0), (0, -1620/691, -1620/691, 453/691, 2526/691, 42965/9674, 29145/9674, 453/691, -929/691, -1620/691, -1620/691)]

    And, the -1 modular symbol attached to ``Delta``::

        sage: A = ModularSymbols(1, sign=-1, weight=12).decomposition()[0]
        sage: f = ps_modsym_from_simple_modsym_space(A); f
        Modular symbol of level 1 with values in Sym^10 Q^2
        sage: f.values()
        [(0, 1, 0, -25/48, 0, 5/12, 0, -25/48, 0, 1, 0), (0, -1, -2, -119/48, -23/12, -5/24, 23/12, 3, 2, 0, 0), (0, 0, 2, 3, 23/12, -5/24, -23/12, -119/48, -2, -1, 0)]

    A consistency check with :meth:`sage.modular.pollack_stevens.space.ps_modsym_from_simple_modsym_space`::

        sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
        sage: E = EllipticCurve('11a')
        sage: f_E = E.pollack_stevens_modular_symbol(); f_E.values()
        [-1/5, 1, 0]
        sage: A = ModularSymbols(11, sign=1, weight=2).decomposition()[0]
        sage: f_plus = ps_modsym_from_simple_modsym_space(A); f_plus.values()
        [1, -5/2, -5/2]
        sage: A = ModularSymbols(11, sign=-1, weight=2).decomposition()[0]
        sage: f_minus = ps_modsym_from_simple_modsym_space(A); f_minus.values()
        [0, 1, -1]

    We find that a linear combination of the plus and minus parts equals the
    Pollack-Stevens symbol attached to ``E``. This illustrates how
    ``ps_modsym_from_simple_modsym_space`` is only well-defined up to a nonzero
    scalar::

        sage: (-1/5)*vector(QQ, f_plus.values()) + (1/2)*vector(QQ, f_minus.values())
        (-1/5, 1, 0)
        sage: vector(QQ, f_E.values())
        (-1/5, 1, 0)

    The next few examples all illustrate the ways in which exceptions are
    raised if A does not satisfy various constraints.

    First, ``A`` must be new::

        sage: A = ModularSymbols(33,sign=1).cuspidal_subspace().old_subspace()
        sage: ps_modsym_from_simple_modsym_space(A)
        Traceback (most recent call last):
        ...
        ValueError: A must be new

    ``A`` must be simple::

        sage: A = ModularSymbols(43,sign=1).cuspidal_subspace()
        sage: ps_modsym_from_simple_modsym_space(A)
        Traceback (most recent call last):
        ...
        ValueError: A must be simple

    ``A`` must have sign -1 or +1 in order to be simple::

        sage: A = ModularSymbols(11).cuspidal_subspace()
        sage: ps_modsym_from_simple_modsym_space(A)
        Traceback (most recent call last):
        ...
        ValueError: A must have sign +1 or -1 (otherwise it is not simple)

    The dimension must be positive::

        sage: A = ModularSymbols(10).cuspidal_subspace(); A
        Modular Symbols subspace of dimension 0 of Modular Symbols space of dimension 3 for Gamma_0(10) of weight 2 with sign 0 over Rational Field
        sage: ps_modsym_from_simple_modsym_space(A)
        Traceback (most recent call last):
        ...
        ValueError: A must have positive dimension

    We check that forms of nontrivial character are getting handled correctly::

        sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
        sage: f = Newforms(Gamma1(13), names='a')[0]
        sage: phi = ps_modsym_from_simple_modsym_space(f.modular_symbols(1))
        sage: phi.hecke(7)
        Modular symbol of level 13 with values in Sym^0 (Number Field in alpha with defining polynomial x^2 + 3*x + 3)^2 twisted by Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -alpha - 1
        sage: phi.hecke(7).values()
        [0, 0, 0, 0, 0]
    """
