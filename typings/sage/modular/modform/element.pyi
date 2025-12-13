import sage.modular.hecke.element as element
from . import defaults as defaults
from sage.arith.functions import lcm as lcm
from sage.arith.misc import crt as crt, divisors as divisors, factor as factor, moebius as moebius, sigma as sigma
from sage.arith.srange import xsrange as xsrange
from sage.matrix.constructor import Matrix as Matrix, matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.verbose import verbose as verbose
from sage.modular.dirichlet import DirichletGroup as DirichletGroup
from sage.modular.modsym.modsym import ModularSymbols as ModularSymbols
from sage.modular.modsym.p1list import lift_to_sl2z as lift_to_sl2z
from sage.modular.modsym.space import ModularSymbolsSpace as ModularSymbolsSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.morphism import RingHomomorphism as RingHomomorphism
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.element import Element as Element, ModuleElement as ModuleElement, coercion_model as coercion_model
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp

def is_ModularFormElement(x):
    """
    Return ``True`` if x is a modular form.

    EXAMPLES::

        sage: from sage.modular.modform.element import is_ModularFormElement
        sage: is_ModularFormElement(5)
        doctest:warning...
        DeprecationWarning: The function is_ModularFormElement is deprecated;
        use 'isinstance(..., ModularFormElement)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        False
        sage: is_ModularFormElement(ModularForms(11).0)
        True
    """
def delta_lseries(prec: int = 53, max_imaginary_part: int = 0, max_asymp_coeffs: int = 40, algorithm=None):
    """
    Return the `L`-series of the modular form `\\Delta`.

    If algorithm is ``'gp'``, this returns an interface to Tim
    Dokchitser's program for computing with the `L`-series of the
    modular form `\\Delta`.

    If algorithm is ``'pari'``, this returns instead an interface to Pari's
    own general implementation of `L`-functions.

    INPUT:

    - ``prec`` -- integer (bits precision)

    - ``max_imaginary_part`` -- real number

    - ``max_asymp_coeffs`` -- integer

    - ``algorithm`` -- string; ``'gp'`` (default), ``'pari'``

    OUTPUT:

    The `L`-series of `\\Delta`.

    EXAMPLES::

        sage: L = delta_lseries()
        sage: L(1)
        0.0374412812685155

        sage: L = delta_lseries(algorithm='pari')
        sage: L(1)
        0.0374412812685155
    """

class ModularForm_abstract(ModuleElement):
    """
    Constructor for generic class of a modular form. This
    should never be called directly; instead one should
    instantiate one of the derived classes of this
    class.
    """
    def group(self):
        """
        Return the group for which ``self`` is a modular form.

        EXAMPLES::

            sage: ModularForms(Gamma1(11), 2).gen(0).group()
            Congruence Subgroup Gamma1(11)
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: (ModularForms(Gamma1(9),2).6).weight()
            2
        """
    def level(self):
        """
        Return the level of ``self``.

        EXAMPLES::

            sage: ModularForms(25,4).0.level()
            25
        """
    def is_homogeneous(self) -> bool:
        """
        Return ``True``.

        For compatibility with elements of a graded modular forms ring.

        An alias of this method is ``is_modular_form``.

        .. SEEALSO::

            :meth:`sage.modular.modform.element.GradedModularFormElement.is_homogeneous`

        EXAMPLES::

            sage: ModularForms(1,12).0.is_homogeneous()
            True
        """
    is_modular_form = is_homogeneous
    def __call__(self, x, prec=None):
        """
        Evaluate the `q`-expansion of this modular form at x.

        EXAMPLES::

            sage: f = ModularForms(DirichletGroup(17).0^2,2).2

            sage: q = f.q_expansion().parent().gen()
            sage: f(q^2 + O(q^7))
            q^2 + (-zeta8^2 + 2)*q^4 + (zeta8 + 3)*q^6 + O(q^7)

            sage: f(0)
            0

        Evaluate numerically::

            sage: f = ModularForms(1, 12).0
            sage: f(0.3)  # rel tol 1e-12
            2.34524576548591e-6
            sage: f = EisensteinForms(1, 4).0
            sage: f(0.9)  # rel tol 1e-12
            1.26475942209241e7

        TESTS::

            sage: f = ModularForms(96, 2).0
            sage: f(0.3)  # rel tol 1e-12
            0.299999997396191
            sage: f(0.0+0.0*I)
            0

        For simplicity, ``float`` or ``complex`` input are converted to ``CC``, except for
        input ``0`` where exact result is returned::

            sage: result = f(0.3r); result  # rel tol 1e-12
            0.299999997396191
            sage: result.parent()
            Complex Field with 53 bits of precision
            sage: result = f(0.3r + 0.3jr); result  # rel tol 1e-12
            0.299999359878484 + 0.299999359878484*I
            sage: result.parent()
            Complex Field with 53 bits of precision

        Symbolic numerical values use precision of ``CC`` by default::

            sage: f(sqrt(1/2))  # rel tol 1e-12
            0.700041406692037
            sage: f(sqrt(1/2)*QQbar.zeta(8))  # rel tol 1e-12
            0.496956554651376 + 0.496956554651376*I

        Higher precision::

            sage: f(ComplexField(128)(0.3))  # rel tol 1e-36
            0.29999999739619131029285166058750164058
            sage: f(ComplexField(128)(1+2*I)/3)  # rel tol 1e-36
            0.32165384572356882556790532669389900691 + 0.67061244638367586302820790711257777390*I

        Confirm numerical evaluation matches the q-expansion::

            sage: f = EisensteinForms(1, 4).0
            sage: f(0.3)  # rel tol 1e-12
            741.741819297986
            sage: f.qexp(50).polynomial()(0.3)  # rel tol 1e-12
            741.741819297986

        With a nontrivial character::

            sage: M = ModularForms(DirichletGroup(17).0^2, 2)
            sage: M.0(0.5)  # rel tol 1e-12
            0.166916655031616 + 0.0111529051752428*I
            sage: M.0.qexp(60).polynomial()(0.5)  # rel tol 1e-12
            0.166916655031616 + 0.0111529051752428*I

        Higher precision::

            sage: f(ComplexField(128)(1+2*I)/3)  # rel tol 1e-36
            429.19994832206294278688085399056359632 - 786.15736284188243351153830824852974995*I
            sage: f.qexp(400).polynomial()(ComplexField(128)(1+2*I)/3)  # rel tol 1e-36
            429.19994832206294278688085399056359631 - 786.15736284188243351153830824852974999*I

        Check ``SR`` does not make the result lose precision::

            sage: f(ComplexField(128)(1+2*I)/3 + x - x)  # rel tol 1e-36
            429.19994832206294278688085399056359632 - 786.15736284188243351153830824852974995*I
        """
    def eval_at_tau(self, tau):
        """
        Evaluate this modular form at the half-period ratio `\\tau`.
        This is related to `q` by `q = e^{2\\pi i \\tau}`.

        EXAMPLES::

            sage: f = ModularForms(1, 12).0
            sage: f.eval_at_tau(0.3 * I)  # rel tol 1e-12
            0.00150904633897550

        TESTS:

        Symbolic numerical values use precision of ``CC`` by default::

            sage: f.eval_at_tau(sqrt(1/5)*I)  # rel tol 1e-12
            0.0123633234207127
            sage: f.eval_at_tau(sqrt(1/2)*QQbar.zeta(8))  # rel tol 1e-12
            -0.114263670441098

        For simplicity, ``complex`` input are converted to ``CC``::

            sage: result = f.eval_at_tau(0.3jr); result  # rel tol 1e-12
            0.00150904633897550
            sage: result.parent()
            Complex Field with 53 bits of precision

        Check ``SR`` does not make the result lose precision::

            sage: f = EisensteinForms(1, 4).0
            sage: f.eval_at_tau(ComplexField(128)(1+2*I)/3 + x - x)  # rel tol 1e-36
            -1.0451570582202060056197878314286036966 + 2.7225112098519803098203933583286590274*I
        """
    @cached_method
    def valuation(self):
        """
        Return the valuation of ``self`` (i.e. as an element of the power
        series ring in q).

        EXAMPLES::

            sage: ModularForms(11,2).0.valuation()
            1
            sage: ModularForms(11,2).1.valuation()
            0
            sage: ModularForms(25,6).1.valuation()
            2
            sage: ModularForms(25,6).6.valuation()
            7
        """
    def qexp(self, prec=None):
        """
        Same as ``self.q_expansion(prec)``.

        .. SEEALSO:: :meth:`q_expansion`

        EXAMPLES::

            sage: CuspForms(1,12).0.qexp()
            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
        """
    def __eq__(self, other):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: f = ModularForms(6,4).0
            sage: g = ModularForms(23,2).0
            sage: f == g  # indirect doctest
            False
            sage: f == f
            True
            sage: f == loads(dumps(f))
            True
        """
    def __ne__(self, other):
        """
        Return ``True`` if ``self != other``.

        EXAMPLES::

            sage: f = Newforms(Gamma1(30), 2, names='a')[1]
            sage: g = ModularForms(23, 2).0
            sage: f != g
            True
            sage: f != f
            False

        TESTS:

        The following used to fail (see :issue:`18068`)::

            sage: f != loads(dumps(f))
            False
        """
    def coefficients(self, X):
        """
        Return the coefficients `a_n` of the `q`-expansion of this modular form.

        This function caches the results of the compute function.

        INPUT:

        - ``X`` -- an iterator or an integer. If ``X`` is an iterator, a list
          containing all `a_{X_i}` is returned. If ``X`` is an integer, it must
          be positive, in which case the coefficients `a_1` to `a_X` are
          returned in a list.

        TESTS::

            sage: e = DirichletGroup(11).gen()
            sage: f = EisensteinForms(e, 3).eisenstein_series()[0]
            sage: f.coefficients([0,1])
            [15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,
             1]
            sage: f.coefficients([0,1,2,3])
            [15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,
             1,
             4*zeta10 + 1,
             -9*zeta10^3 + 1]
            sage: f.coefficients([2,3])
            [4*zeta10 + 1,
             -9*zeta10^3 + 1]

        Running this twice once revealed a bug, so we test it::

            sage: f.coefficients([0,1,2,3])
            [15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,
             1,
             4*zeta10 + 1,
             -9*zeta10^3 + 1]
        """
    def __getitem__(self, n):
        """
        Return the `q^n` coefficient of the `q`-expansion of ``self`` or
        returns a list containing the `q^i` coefficients of self
        where `i` is in slice `n`.

        EXAMPLES::

            sage: f = ModularForms(DirichletGroup(17).0^2,2).2
            sage: f.__getitem__(10)
            zeta8^3 - 5*zeta8^2 - 2*zeta8 + 10
            sage: f[30]
            -2*zeta8^3 - 17*zeta8^2 + 4*zeta8 + 29
            sage: f[10:15]
            [zeta8^3 - 5*zeta8^2 - 2*zeta8 + 10,
            -zeta8^3 + 11,
            -2*zeta8^3 - 6*zeta8^2 + 3*zeta8 + 9,
            12,
            2*zeta8^3 - 7*zeta8^2 + zeta8 + 14]
        """
    def coefficient(self, n):
        """
        Return the `n`-th coefficient of the `q`-expansion of ``self``.

        INPUT:

        - ``n`` -- nonnegative integer

        EXAMPLES::

            sage: f = ModularForms(1, 12).0; f
            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
            sage: f.coefficient(0)
            0
            sage: f.coefficient(1)
            1
            sage: f.coefficient(2)
            -24
            sage: f.coefficient(3)
            252
            sage: f.coefficient(4)
            -1472
        """
    def padded_list(self, n):
        """
        Return a list of length n whose entries are the first n
        coefficients of the `q`-expansion of ``self``.

        EXAMPLES::

            sage: CuspForms(1,12).0.padded_list(20)
            [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643,
             -115920, 534612, -370944, -577738, 401856, 1217160, 987136,
             -6905934, 2727432, 10661420]
        """
    def character(self, compute: bool = True):
        """
        Return the character of ``self``. If ``compute=False``, then this will
        return None unless the form was explicitly created as an element of a
        space of forms with character, skipping the (potentially expensive)
        computation of the matrices of the diamond operators.

        EXAMPLES::

            sage: ModularForms(DirichletGroup(17).0^2,2).2.character()
            Dirichlet character modulo 17 of conductor 17 mapping 3 |--> zeta8

            sage: CuspForms(Gamma1(7), 3).gen(0).character()
            Dirichlet character modulo 7 of conductor 7 mapping 3 |--> -1
            sage: CuspForms(Gamma1(7), 3).gen(0).character(compute = False) is None
            True
            sage: M = CuspForms(Gamma1(7), 5).gen(0).character()
            Traceback (most recent call last):
            ...
            ValueError: Form is not an eigenvector for <3>
        """
    def __bool__(self) -> bool:
        """
        Return ``True`` if ``self`` is nonzero, and ``False`` if not.

        EXAMPLES::

            sage: bool(ModularForms(25,6).6)
            True
        """
    def prec(self):
        """
        Return the precision to which self.q_expansion() is
        currently known. Note that this may be 0.

        EXAMPLES::

            sage: M = ModularForms(2,14)
            sage: f = M.0
            sage: f.prec()
            0

            sage: M.prec(20)
            20
            sage: f.prec()
            0
            sage: x = f.q_expansion() ; f.prec()
            20
        """
    def q_expansion(self, prec=None):
        """
        The `q`-expansion of the modular form to precision `O(q^\\text{prec})`.
        This function takes one argument, which is the integer prec.

        EXAMPLES:

        We compute the cusp form `\\Delta`::

            sage: delta = CuspForms(1,12).0
            sage: delta.q_expansion()
            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)

        We compute the `q`-expansion of one of the cusp forms of level 23::

            sage: f = CuspForms(23,2).0
            sage: f.q_expansion()
            q - q^3 - q^4 + O(q^6)
            sage: f.q_expansion(10)
            q - q^3 - q^4 - 2*q^6 + 2*q^7 - q^8 + 2*q^9 + O(q^10)
            sage: f.q_expansion(2)
            q + O(q^2)
            sage: f.q_expansion(1)
            O(q^1)
            sage: f.q_expansion(0)
            O(q^0)
            sage: f.q_expansion(-1)
            Traceback (most recent call last):
            ...
            ValueError: prec (= -1) must be nonnegative
        """
    def serre_derivative(self):
        """
        Return the Serre derivative of the given modular form.

        If ``self`` is of weight `k`, then the returned modular form will be of
        weight `k+2`.

        EXAMPLES::

            sage: E4 = ModularForms(1, 4).0
            sage: E6 = ModularForms(1, 6).0
            sage: DE4 = E4.serre_derivative(); DE4
            -1/3 + 168*q + 5544*q^2 + 40992*q^3 + 177576*q^4 + 525168*q^5 + O(q^6)
            sage: DE6 = E6.serre_derivative(); DE6
            -1/2 - 240*q - 30960*q^2 - 525120*q^3 - 3963120*q^4 - 18750240*q^5 + O(q^6)
            sage: Del = ModularForms(1, 12).0 # Modular discriminant
            sage: Del.serre_derivative()
            0
            sage: f = ModularForms(DirichletGroup(5).0, 1).0
            sage: Df = f.serre_derivative(); Df
            -1/12 + (-11/12*zeta4 + 19/4)*q + (11/6*zeta4 + 59/3)*q^2 + (-41/3*zeta4 + 239/6)*q^3 + (31/4*zeta4 + 839/12)*q^4 + (-251/12*zeta4 + 459/4)*q^5 + O(q^6)

        The Serre derivative raises the weight of a modular form by `2`::

            sage: DE4.weight()
            6
            sage: DE6.weight()
            8
            sage: Df.weight()
            3

        The Ramanujan identities are verified (see :wikipedia:`Eisenstein_series#Ramanujan_identities`)::

            sage: DE4 == (-1/3) * E6
            True
            sage: DE6 == (-1/2) * E4 * E4
            True
        """
    def atkin_lehner_eigenvalue(self, d=None, embedding=None) -> None:
        """
        Return the eigenvalue of the Atkin-Lehner operator `W_d`
        acting on ``self``.

        INPUT:

        - ``d`` -- positive integer exactly dividing the level `N`
          of ``self``, i.e. `d` divides `N` and is coprime to `N/d`
          (default: `d = N`)

        - ``embedding`` -- (optional) embedding of the base ring of
          ``self`` into another ring

        OUTPUT:

        The Atkin-Lehner eigenvalue of `W_d` on ``self``.  This is
        returned as an element of the codomain of ``embedding`` if
        specified, and in (a suitable extension of) the base field of
        ``self`` otherwise.

        If ``self`` is not an eigenform for `W_d`, a :exc:`ValueError` is
        raised.

        .. SEEALSO::

            :meth:`sage.modular.hecke.module.HeckeModule_free_module.atkin_lehner_operator`
            (especially for the conventions used to define the operator `W_d`).

        EXAMPLES::

            sage: CuspForms(1, 12).0.atkin_lehner_eigenvalue()
            1
            sage: CuspForms(2, 8).0.atkin_lehner_eigenvalue()
            Traceback (most recent call last):
            ...
            NotImplementedError: don't know how to compute Atkin-Lehner matrix acting on this space (try using a newform constructor instead)
        """
    def period(self, M, prec: int = 53):
        """
        Return the period of ``self`` with respect to `M`.

        INPUT:

        - ``self`` -- a cusp form `f` of weight 2 for `Gamma_0(N)`

        - ``M`` -- an element of `\\Gamma_0(N)`

        - ``prec`` -- (default: 53) the working precision in bits.  If
          `f` is a normalised eigenform, then the output is correct to
          approximately this number of bits.

        OUTPUT:

        A numerical approximation of the period `P_f(M)`.  This period
        is defined by the following integral over the complex upper
        half-plane, for any `\\alpha` in `\\Bold{P}^1(\\QQ)`:

        .. MATH::

            P_f(M) = 2 \\pi i \\int_\\alpha^{M(\\alpha)} f(z) dz.

        This is independent of the choice of `\\alpha`.

        EXAMPLES::

            sage: C = Newforms(11, 2)[0]
            sage: m = C.group()(matrix([[-4, -3], [11, 8]]))
            sage: C.period(m)
            -0.634604652139776 - 1.45881661693850*I

            sage: f = Newforms(15, 2)[0]
            sage: g = Gamma0(15)(matrix([[-4, -3], [15, 11]]))
            sage: f.period(g)  # abs tol 1e-15
            2.17298044293747e-16 - 1.59624222213178*I

        If `E` is an elliptic curve over `\\QQ` and `f` is the newform
        associated to `E`, then the periods of `f` are in the period
        lattice of `E` up to an integer multiple::

            sage: E = EllipticCurve('11a3')
            sage: f = E.newform()
            sage: g = Gamma0(11)([3, 1, 11, 4])
            sage: f.period(g)
            0.634604652139777 + 1.45881661693850*I
            sage: omega1, omega2 = E.period_lattice().basis()
            sage: -2/5*omega1 + omega2
            0.634604652139777 + 1.45881661693850*I

        The integer multiple is 5 in this case, which is explained by
        the fact that there is a 5-isogeny between the elliptic curves
        `J_0(5)` and `E`.

        The elliptic curve `E` has a pair of modular symbols attached
        to it, which can be computed using the method
        :meth:`sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.modular_symbol`.
        These can be used to express the periods of `f` as exact
        linear combinations of the real and the imaginary period of `E`::

            sage: s = E.modular_symbol(sign=+1)
            sage: t = E.modular_symbol(sign=-1, implementation='sage')
            sage: s(3/11), t(3/11)
            (1/10, 1/2)
            sage: s(3/11)*omega1 + t(3/11)*2*omega2.imag()*I
            0.634604652139777 + 1.45881661693850*I

        ALGORITHM:

        We use the series expression from [Cre1997]_, Chapter II,
        Proposition 2.10.3.  The algorithm sums the first `T` terms of
        this series, where `T` is chosen in such a way that the result
        would approximate `P_f(M)` with an absolute error of at most
        `2^{-\\text{prec}}` if all computations were done exactly.

        Since the actual precision is finite, the output is currently
        *not* guaranteed to be correct to ``prec`` bits of precision.

        TESTS::

            sage: C = Newforms(11, 2)[0]
            sage: g = Gamma0(15)(matrix([[-4, -3], [15, 11]]))
            sage: C.period(g)
            Traceback (most recent call last):
            ...
            TypeError: matrix [-4 -3]
                              [15 11]
            is not an element of Congruence Subgroup Gamma0(11)

            sage: f = Newforms(Gamma0(15), 4)[0]
            sage: f.period(g)
            Traceback (most recent call last):
            ...
            ValueError: period pairing only defined for cusp forms of weight 2

            sage: S = Newforms(Gamma1(17), 2, names='a')
            sage: f = S[1]
            sage: g = Gamma1(17)([18, 1, 17, 1])
            sage: f.period(g)
            Traceback (most recent call last):
            ...
            NotImplementedError: period pairing only implemented for cusp forms of trivial character

            sage: E = ModularForms(Gamma0(4), 2).eisenstein_series()[0]
            sage: gamma = Gamma0(4)([1, 0, 4, 1])
            sage: E.period(gamma)
            Traceback (most recent call last):
            ...
            NotImplementedError: don't know how to compute Atkin-Lehner matrix acting on this space (try using a newform constructor instead)

            sage: E = EllipticCurve('19a1')
            sage: M = Gamma0(19)([10, 1, 19, 2])
            sage: E.newform().period(M)  # abs tol 1e-14
            -1.35975973348831 + 1.09365931898146e-16*I
        """
    def lseries(self, embedding: int = 0, prec: int = 53, max_imaginary_part: int = 0, max_asymp_coeffs: int = 40):
        """
        Return the `L`-series of the weight k cusp form
        `f` on `\\Gamma_0(N)`.

        This actually returns an interface to Tim Dokchitser's program for
        computing with the `L`-series of the cusp form.

        INPUT:

        - ``embedding`` -- either an embedding of the coefficient field of self
          into `\\CC`, or an integer `i` between 0 and D-1 where D is the degree
          of the coefficient field (meaning to pick the `i`-th embedding).
          (default: 0)

        - ``prec`` -- integer (default: 53); bits precision

        - ``max_imaginary_part`` -- real number (default: 0)

        - ``max_asymp_coeffs`` -- integer (default: 40)

        For more information on the significance of the last three arguments,
        see :mod:`~sage.lfunctions.dokchitser`.

        .. NOTE::

            If an explicit embedding is given, but this embedding is specified
            to smaller precision than ``prec``, it will be automatically
            refined to precision ``prec``.

        OUTPUT:

        The `L`-series of the cusp form, as a
        :class:`sage.lfunctions.dokchitser.Dokchitser` object.

        EXAMPLES::

            sage: f = CuspForms(2,8).newforms()[0]
            sage: L = f.lseries()
            sage: L
            L-series associated to the cusp form q - 8*q^2 + 12*q^3 + 64*q^4 - 210*q^5 + O(q^6)
            sage: L(1)
            0.0884317737041015
            sage: L(0.5)
            0.0296568512531983

        As a consistency check, we verify that the functional equation holds::

            sage: abs(L.check_functional_equation()) < 1.0e-20
            True

        For non-rational newforms we can specify an embedding of the coefficient field::

            sage: f = Newforms(43, names='a')[1]
            sage: K = f.hecke_eigenvalue_field()
            sage: phi1, phi2 = K.embeddings(CC)
            sage: L = f.lseries(embedding=phi1)
            sage: L
            L-series associated to the cusp form q + a1*q^2 - a1*q^3 + (-a1 + 2)*q^5 + O(q^6), a1=-1.41421356237310
            sage: L(1)
            0.620539857407845
            sage: L = f.lseries(embedding=1)
            sage: L(1)
            0.921328017272472

        An example with a non-real coefficient field (`\\QQ(\\zeta_3)`
        in this case)::

            sage: f = Newforms(Gamma1(13), 2, names='a')[0]
            sage: f.lseries(embedding=0)(1)
            0.298115272465799 - 0.0402203326076734*I
            sage: f.lseries(embedding=1)(1)
            0.298115272465799 + 0.0402203326076732*I

        We compute with the `L`-series of the Eisenstein series `E_4`::

            sage: f = ModularForms(1,4).0
            sage: L = f.lseries()
            sage: L(1)
            -0.0304484570583933
            sage: L = eisenstein_series_lseries(4)
            sage: L(1)
            -0.0304484570583933

        Consistency check with delta_lseries (which computes coefficients in pari)::

            sage: delta = CuspForms(1,12).0
            sage: L = delta.lseries()
            sage: L(1)
            0.0374412812685155
            sage: L = delta_lseries()
            sage: L(1)
            0.0374412812685155

        We check that :issue:`5262` is fixed::

            sage: E = EllipticCurve('37b2')
            sage: h = Newforms(37)[1]
            sage: Lh = h.lseries()
            sage: LE = E.lseries()
            sage: Lh(1), LE(1)
            (0.725681061936153, 0.725681061936153)
            sage: CuspForms(1, 30).0.lseries().eps
            -1.00000000000000

        We check that :issue:`25369` is fixed::

            sage: f5 = Newforms(Gamma1(4), 5, names='a')[0]; f5
            q - 4*q^2 + 16*q^4 - 14*q^5 + O(q^6)
            sage: L5 = f5.lseries()
            sage: abs(L5.check_functional_equation()) < 1e-15
            True
            sage: abs(L5(4) - (gamma(1/4)^8/(3840*pi^2)).n()) < 1e-15
            True

        We can change the precision (in bits)::

            sage: f = Newforms(389, names='a')[0]
            sage: L = f.lseries(prec=30)
            sage: abs(L(1)) < 2^-30
            True
            sage: L = f.lseries(prec=53)
            sage: abs(L(1)) < 2^-53
            True
            sage: L = f.lseries(prec=100)
            sage: abs(L(1)) < 2^-100
            True

            sage: f = Newforms(27, names='a')[0]
            sage: L = f.lseries()
            sage: L(1)
            0.588879583428483
        """
    def symsquare_lseries(self, chi=None, embedding: int = 0, prec: int = 53):
        """
        Compute the symmetric square `L`-series of this modular form, twisted by
        the character `\\chi`.

        INPUT:

        - ``chi`` -- Dirichlet character to twist by, or ``None`` (default:
          ``None``), interpreted as the trivial character)
        - ``embedding`` -- embedding of the coefficient field into `\\RR` or
          `\\CC`, or an integer `i` (in which case take the `i`-th embedding)
        - ``prec`` -- the desired precision in bits (default: 53)

        OUTPUT: the symmetric square `L`-series of the cusp form, as a
        :class:`sage.lfunctions.dokchitser.Dokchitser` object.

        EXAMPLES::

            sage: CuspForms(1, 12).0.symsquare_lseries()(22)
            0.999645711124771

        An example twisted by a nontrivial character::

            sage: psi = DirichletGroup(7).0^2
            sage: L = CuspForms(1, 16).0.symsquare_lseries(psi)
            sage: L(22)
            0.998407750967420 - 0.00295712911510708*I

        An example with coefficients not in `\\QQ`::

            sage: F = Newforms(1, 24, names='a')[0]
            sage: K = F.hecke_eigenvalue_field()
            sage: phi = K.embeddings(RR)[0]
            sage: L = F.symsquare_lseries(embedding=phi)
            sage: L(5)
            verbose -1 (...: dokchitser.py, __call__) Warning: Loss of 8 decimal digits due to cancellation
            -3.57698266793901e19

        TESTS::

            sage: CuspForms(1,16).0.symsquare_lseries(prec=200).check_functional_equation().abs() < 1.0e-80
            True
            sage: CuspForms(1, 12).0.symsquare_lseries(prec=1000)(22) # long time (20s)
            0.999645711124771397835729622033153189549796658647254961493709341358991830134499267117001769570658192128781135161587571716303826382489492569725002840546129937149159065273765309218543427544527498868033604310899372849565046516553245752253255585377793879866297612679545029546953895098375829822346290125161

        Check that :issue:`23247` is fixed::

            sage: F = Newforms(1,12)[0]
            sage: chi = DirichletGroup(7).0
            sage: abs(F.symsquare_lseries(chi).check_functional_equation()) < 1e-5  # long time
            True

        AUTHORS:

        - Martin Raum (2011) -- original code posted to sage-nt
        - David Loeffler (2015) -- added support for twists, integrated into
          Sage library
        """
    def petersson_norm(self, embedding: int = 0, prec: int = 53):
        '''
        Compute the Petersson scalar product of f with itself:

        .. MATH::

            \\langle f, f \\rangle = \\int_{\\Gamma_0(N) \\backslash \\mathbb{H}} |f(x + iy)|^2 y^k\\, \\mathrm{d}x\\, \\mathrm{d}y.

        Only implemented for N = 1 at present. It is assumed that `f` has real
        coefficients. The norm is computed as a special value of the symmetric
        square `L`-function, using the identity

        .. MATH::

            \\langle f, f \\rangle = \\frac{(k-1)! L(\\mathrm{Sym}^2 f, k)}{2^{2k-1} \\pi^{k+1}}

        INPUT:

        - ``embedding`` -- embedding of the coefficient field into `\\RR` or
          `\\CC`, or an integer `i` (interpreted as the `i`-th embedding)
          (default: 0)
        - ``prec`` -- integer (default: 53); precision in bits

        EXAMPLES::

            sage: CuspForms(1, 16).0.petersson_norm()
            verbose -1 (...: dokchitser.py, __call__) Warning: Loss of 2 decimal digits due to cancellation
            2.16906134759063e-6

        The Petersson norm depends on a choice of embedding::

            sage: set_verbose(-2, "dokchitser.py") # disable precision-loss warnings
            sage: F = Newforms(1, 24, names=\'a\')[0]
            sage: F.petersson_norm(embedding=0)
            0.000107836545077234
            sage: F.petersson_norm(embedding=1)
            0.000128992800758160

        TESTS:

        Verify that the Petersson norm is a quadratic form::

            sage: F, G = CuspForms(1, 24).basis()
            sage: X = lambda u: u.petersson_norm(prec=100)
            sage: (X(F + G) + X(F - G) - 2*X(F) - 2*X(G)).abs() < 1e-25
            True
        '''
    @cached_method
    def has_cm(self) -> bool:
        """
        Return whether the modular form ``self`` has complex multiplication.

        OUTPUT: boolean

        .. SEEALSO::

            - :meth:`cm_discriminant` (to return the CM field)
            - :meth:`sage.schemes.elliptic_curves.ell_rational_field.has_cm`

        EXAMPLES::

            sage: G = DirichletGroup(21); eps = G.0 * G.1
            sage: Newforms(eps, 2)[0].has_cm()
            True

        This example illustrates what happens when
        candidate_characters(self) is the empty list. ::

            sage: M = ModularForms(Gamma0(1), 12)
            sage: C = M.cuspidal_submodule()
            sage: Delta = C.gens()[0]
            sage: Delta.has_cm()
            False

        We now compare the function has_cm between elliptic curves and
        their associated modular forms. ::

            sage: E = EllipticCurve([-1, 0])
            sage: f = E.modular_form()
            sage: f.has_cm()
            True
            sage: E.has_cm() == f.has_cm()
            True

        Here is a non-cm example coming from elliptic curves. ::

            sage: E = EllipticCurve('11a')
            sage: f = E.modular_form()
            sage: f.has_cm()
            False
            sage: E.has_cm() == f.has_cm()
            True
        """
    def cm_discriminant(self):
        """
        Return the discriminant of the CM field associated to this form. An
        error will be raised if the form isn't of CM type.

        EXAMPLES::

            sage: Newforms(49, 2)[0].cm_discriminant()
            -7
            sage: CuspForms(1, 12).gen(0).cm_discriminant()
            Traceback (most recent call last):
            ...
            ValueError: Not a CM form
        """

class Newform(ModularForm_abstract):
    def __init__(self, parent, component, names, check: bool = True) -> None:
        """
        Initialize a Newform object.

        INPUT:

        - ``parent`` -- an ambient cuspidal space of modular forms for
          which ``self`` is a newform

        - ``component`` -- a simple component of a cuspidal modular
          symbols space of any sign corresponding to this newform

        - ``check`` -- if check is ``True``, check that parent and
          component have the same weight, level, and character, that
          component has sign 1 and is simple, and that the types are
          correct on all inputs.

        EXAMPLES::

            sage: sage.modular.modform.element.Newform(CuspForms(11,2), ModularSymbols(11,2,sign=1).cuspidal_subspace(), 'a')
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)

            sage: f = Newforms(DirichletGroup(5).0, 7,names='a')[0]; f[2].trace(f.base_ring().base_field())
            -5*zeta4 - 5
        """
    def __eq__(self, other):
        """
        Return ``True`` if ``self`` equals ``other``, and ``False`` otherwise.

        EXAMPLES::

            sage: f1, f2 = Newforms(17,4,names='a')
            sage: f1.__eq__(f1)
            True
            sage: f1.__eq__(f2)
            False

        We test comparison of equal newforms with different parents
        (see :issue:`18478`)::

            sage: f = Newforms(Gamma1(11), 2)[0]; f
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
            sage: g = Newforms(Gamma0(11), 2)[0]; g
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
            sage: f == g
            True

            sage: f = Newforms(DirichletGroup(4)[1], 5)[0]; f
            q - 4*q^2 + 16*q^4 - 14*q^5 + O(q^6)
            sage: g = Newforms(Gamma1(4), 5)[0]; g
            q - 4*q^2 + 16*q^4 - 14*q^5 + O(q^6)
            sage: f == g
            True
        """
    @cached_method
    def abelian_variety(self):
        """
        Return the abelian variety associated to ``self``.

        EXAMPLES::

            sage: Newforms(14,2)[0]
            q - q^2 - 2*q^3 + q^4 + O(q^6)
            sage: Newforms(14,2)[0].abelian_variety()
            Newform abelian subvariety 14a of dimension 1 of J0(14)
            sage: Newforms(1, 12)[0].abelian_variety()
            Traceback (most recent call last):
            ...
            TypeError: f must have weight 2
        """
    def hecke_eigenvalue_field(self):
        """
        Return the field generated over the rationals by the
        coefficients of this newform.

        EXAMPLES::

            sage: ls = Newforms(35, 2, names='a') ; ls
            [q + q^3 - 2*q^4 - q^5 + O(q^6),
            q + a1*q^2 + (-a1 - 1)*q^3 + (-a1 + 2)*q^4 + q^5 + O(q^6)]
            sage: ls[0].hecke_eigenvalue_field()
            Rational Field
            sage: ls[1].hecke_eigenvalue_field()
            Number Field in a1 with defining polynomial x^2 + x - 4
        """
    def coefficient(self, n):
        """
        Return the coefficient of `q^n` in the power series of ``self``.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT: the coefficient of `q^n` in the power series of ``self``

        EXAMPLES::

            sage: f = Newforms(11)[0]; f
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
            sage: f.coefficient(100)
            -8

            sage: g = Newforms(23, names='a')[0]; g
            q + a0*q^2 + (-2*a0 - 1)*q^3 + (-a0 - 1)*q^4 + 2*a0*q^5 + O(q^6)
            sage: g.coefficient(3)
            -2*a0 - 1
        """
    def element(self):
        """
        Find an element of the ambient space of modular forms which
        represents this newform.

        .. NOTE::

           This can be quite expensive. Also, the polynomial defining
           the field of Hecke eigenvalues should be considered random,
           since it is generated by a random sum of Hecke
           operators. (The field itself is not random, of course.)

        EXAMPLES::

            sage: ls = Newforms(38,4,names='a')
            sage: ls[0]
            q - 2*q^2 - 2*q^3 + 4*q^4 - 9*q^5 + O(q^6)
            sage: ls # random
            [q - 2*q^2 - 2*q^3 + 4*q^4 - 9*q^5 + O(q^6),
            q - 2*q^2 + (-a1 - 2)*q^3 + 4*q^4 + (2*a1 + 10)*q^5 + O(q^6),
            q + 2*q^2 + (1/2*a2 - 1)*q^3 + 4*q^4 + (-3/2*a2 + 12)*q^5 + O(q^6)]
            sage: type(ls[0])
            <class 'sage.modular.modform.element.Newform'>
            sage: ls[2][3].minpoly()
            x^2 - 9*x + 2
            sage: ls2 = [ x.element() for x in ls ]
            sage: ls2 # random
            [q - 2*q^2 - 2*q^3 + 4*q^4 - 9*q^5 + O(q^6),
            q - 2*q^2 + (-a1 - 2)*q^3 + 4*q^4 + (2*a1 + 10)*q^5 + O(q^6),
            q + 2*q^2 + (1/2*a2 - 1)*q^3 + 4*q^4 + (-3/2*a2 + 12)*q^5 + O(q^6)]
            sage: type(ls2[0])
            <class 'sage.modular.modform.cuspidal_submodule.CuspidalSubmodule_g0_Q_with_category.element_class'>
            sage: ls2[2][3].minpoly()
            x^2 - 9*x + 2
        """
    def is_cuspidal(self) -> bool:
        """
        Return ``True``.

        For compatibility with elements of modular forms spaces.

        EXAMPLES::

            sage: Newforms(11, 2)[0].is_cuspidal()
            True
        """
    def modular_symbols(self, sign: int = 0):
        """
        Return the subspace with the specified sign of the space of
        modular symbols corresponding to this newform.

        EXAMPLES::

            sage: f = Newforms(18,4)[0]
            sage: f.modular_symbols()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 18 for Gamma_0(18) of weight 4 with sign 0 over Rational Field
            sage: f.modular_symbols(1)
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 11 for Gamma_0(18) of weight 4 with sign 1 over Rational Field
        """
    @cached_method
    def modsym_eigenspace(self, sign: int = 0):
        '''
        Return a submodule of dimension 1 or 2 of the ambient space of
        the sign 0 modular symbols space associated to ``self``,
        base-extended to the Hecke eigenvalue field, which is an
        eigenspace for the Hecke operators with the same eigenvalues
        as this newform, *and* is an eigenspace for the star
        involution of the appropriate sign if the sign is not 0.

        EXAMPLES::

            sage: N = Newform("37a")
            sage: N.modular_symbols(0)
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field
            sage: M = N.modular_symbols(0)
            sage: V = N.modsym_eigenspace(1); V
            Vector space of degree 5 and dimension 1 over Rational Field
            Basis matrix:
            [ 0  1 -1  1  0]
            sage: V.0 in M.free_module()
            True
            sage: V = N.modsym_eigenspace(-1); V
            Vector space of degree 5 and dimension 1 over Rational Field
            Basis matrix:
            [   0    0    0    1 -1/2]
            sage: V.0 in M.free_module()
            True
        '''
    def number(self):
        """
        Return the index of this space in the list of simple, new,
        cuspidal subspaces of the full space of modular symbols for
        this weight and level.

        EXAMPLES::

            sage: Newforms(43, 2, names='a')[1].number()
            1
        """
    def __bool__(self) -> bool:
        """
        Return ``True``, as newforms are never zero.

        EXAMPLES::

            sage: bool(Newforms(14,2)[0])
            True
        """
    def character(self):
        """
        The nebentypus character of this newform (as a Dirichlet character with
        values in the field of Hecke eigenvalues of the form).

        EXAMPLES::

            sage: Newforms(Gamma1(7), 4,names='a')[1].character()
            Dirichlet character modulo 7 of conductor 7 mapping 3 |--> 1/2*a1
            sage: chi = DirichletGroup(3).0; Newforms(chi, 7)[0].character() == chi
            True
        """
    def atkin_lehner_action(self, d=None, normalization: str = 'analytic', embedding=None):
        """
        Return the result of the Atkin-Lehner operator `W_d` on this form `f`,
        in the form of a constant `\\lambda_d(f)` and a normalized newform `f'`
        such that

        .. math::

            f \\mid W_d = \\lambda_d(f) f'.

        See :meth:`atkin_lehner_eigenvalue` for further details.

        EXAMPLES::

            sage: f = Newforms(DirichletGroup(30).1^2, 2, names='a')[0]
            sage: emb = f.base_ring().complex_embeddings()[0]
            sage: for d in divisors(30):
            ....:     print(f.atkin_lehner_action(d, embedding=emb))
            (1.00000000000000, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (-1.00000000000000*I, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (1.00000000000000*I, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (-0.894427190999916 + 0.447213595499958*I, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))
            (1.00000000000000, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (-0.447213595499958 - 0.894427190999916*I, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))
            (0.447213595499958 + 0.894427190999916*I, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))
            (-0.894427190999916 + 0.447213595499958*I, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))

        The above computation can also be done exactly::

            sage: K.<z> = CyclotomicField(20)
            sage: f = Newforms(DirichletGroup(30).1^2, 2, names='a')[0]
            sage: emb = f.base_ring().embeddings(CyclotomicField(20, 'z'))[0]
            sage: for d in divisors(30):
            ....:     print(f.atkin_lehner_action(d, embedding=emb))
            (1, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (z^5, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (-z^5, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (-2/5*z^7 + 4/5*z^6 + 1/5*z^5 - 4/5*z^4 - 2/5*z^3 - 2/5, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))
            (1, q + a0*q^2 - a0*q^3 - q^4 + (a0 - 2)*q^5 + O(q^6))
            (4/5*z^7 + 2/5*z^6 - 2/5*z^5 - 2/5*z^4 + 4/5*z^3 - 1/5, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))
            (-4/5*z^7 - 2/5*z^6 + 2/5*z^5 + 2/5*z^4 - 4/5*z^3 + 1/5, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))
            (-2/5*z^7 + 4/5*z^6 + 1/5*z^5 - 4/5*z^4 - 2/5*z^3 - 2/5, q - a0*q^2 + a0*q^3 - q^4 + (-a0 - 2)*q^5 + O(q^6))

        We can compute the eigenvalue of `W_{p^e}` in certain cases
        where the `p`-th coefficient of `f` is zero::

            sage: f = Newforms(169, names='a')[0]; f
            q + a0*q^2 + 2*q^3 + q^4 - a0*q^5 + O(q^6)
            sage: f[13]
            0
            sage: f.atkin_lehner_eigenvalue(169)
            -1

        An example showing the non-multiplicativity of the pseudo-eigenvalues::

            sage: chi = DirichletGroup(18).0^4
            sage: f = Newforms(chi, 2)[0]
            sage: w2, _ = f.atkin_lehner_action(2); w2
            zeta6
            sage: w9, _ = f.atkin_lehner_action(9); w9
            -zeta18^4
            sage: w18,_ = f.atkin_lehner_action(18); w18
            -zeta18
            sage: w18 == w2 * w9 * chi( crt(2, 9, 9, 2) )
            True

        TESTS::

            sage: K.<a> = QuadraticField(1129)
            sage: f = Newforms(Gamma0(20), 8, base_ring=K)[2]; f
            q + (2*a - 10)*q^3 + 125*q^5 + O(q^6)
            sage: f.atkin_lehner_action(2)
            (-1, q + (2*a - 10)*q^3 + 125*q^5 + O(q^6))

            sage: f = Newforms(Gamma1(11), 2)[0]
            sage: f.atkin_lehner_action(2)
            Traceback (most recent call last):
            ...
            ValueError: d (= 2) does not divide the level (= 11)
        """
    def atkin_lehner_eigenvalue(self, d=None, normalization: str = 'analytic', embedding=None):
        """
        Return the pseudo-eigenvalue of the Atkin-Lehner operator `W_d`
        acting on this form `f`.

        INPUT:

        - ``d`` -- positive integer exactly dividing the level `N` of `f`,
          i.e., `d` divides `N` and is coprime to `N/d`; the default is `d = N`

          If `d` does not divide `N` exactly, then it will be replaced with a
          multiple `D` of `d` such that `D` exactly divides `N` and `D` has the
          same prime factors as `d`. An error will be raised if `d` does not
          divide `N`.

        - ``normalization`` -- either ``'analytic'`` (the default) or
          ``'arithmetic'``; see below

        - ``embedding`` -- (optional) embedding of the coefficient field of `f`
          into another ring; ignored if ``'normalization='arithmetic'``

        OUTPUT:

        The Atkin-Lehner pseudo-eigenvalue of `W_d` on `f`, as an element of
        the coefficient field of `f`, or the codomain of ``embedding`` if
        specified.

        As defined in [AL1978]_, the pseudo-eigenvalue is the constant
        `\\lambda_d(f)` such that

        ..math::

            f \\mid W_d = \\lambda_d(f) f'

        where `f'` is some normalised newform (not necessarily equal to `f`).

        If ``normalisation='analytic'`` (the default), this routine will
        compute `\\lambda_d`, using the conventions of [AL1978]_ for the weight
        `k` action, which imply that `\\lambda_d` has complex absolute value 1.
        However, with these conventions `\\lambda_d` is not in the Hecke
        eigenvalue field of `f` in general, so it is often necessary to specify
        an embedding of the eigenvalue field into a larger ring (which needs to
        contain roots of unity of sufficiently large order, and a square root
        of `d` if `k` is odd).

        If ``normalisation='arithmetic'`` we compute instead the quotient

        ..math::

            d^{k/2-1} \\lambda_d(f) \\varepsilon_{N/d}(d / d_0) / G(\\varepsilon_d),

        where `G(\\varepsilon_d)` is the Gauss sum of the `d`-primary part of
        the nebentype of `f` (more precisely, of its associated primitive
        character), and `d_0` its conductor. This ratio is always in the Hecke
        eigenvalue field of `f` (and can be computed using only arithmetic in
        this field), so specifying an embedding is not needed, although we
        still allow it for consistency.

        (Note that if `k = 2` and `\\varepsilon` is trivial, both
        normalisations coincide.)

        .. SEEALSO::

            - :meth:`sage.modular.hecke.module.atkin_lehner_operator`
              (especially for the conventions used to define the operator
              `W_d`)

            - :meth:`atkin_lehner_action`, which returns both the
              pseudo-eigenvalue and the newform `f'`.

        EXAMPLES::

            sage: [x.atkin_lehner_eigenvalue() for x in ModularForms(53).newforms('a')]
            [1, -1]

            sage: f = Newforms(Gamma1(15), 3, names='a')[2]; f
            q + a2*q^2 + (-a2 - 2)*q^3 - q^4 - a2*q^5 + O(q^6)
            sage: f.atkin_lehner_eigenvalue(5)
            Traceback (most recent call last):
            ...
            ValueError: Unable to compute square root. Try specifying an embedding into a larger ring
            sage: L = f.hecke_eigenvalue_field(); x = polygen(QQ); M.<sqrt5> = L.extension(x^2 - 5)
            sage: f.atkin_lehner_eigenvalue(5, embedding=M.coerce_map_from(L))
            1/5*a2*sqrt5
            sage: f.atkin_lehner_eigenvalue(5, normalization='arithmetic')
            a2

            sage: Newforms(DirichletGroup(5).0^2, 6, names='a')[0].atkin_lehner_eigenvalue()
            Traceback (most recent call last):
            ...
            ValueError: Unable to compute Gauss sum. Try specifying an embedding into a larger ring

        TESTS:

        Check that the bug reported at :issue:`18061` is fixed::

            sage: K.<i> = CyclotomicField(4)
            sage: f = Newforms(DirichletGroup(30, QQ).1, 2, K)[0]
            sage: f.atkin_lehner_eigenvalue(embedding=K.embeddings(QQbar)[1])
            -0.8944271909999159? - 0.4472135954999580?*I

        Check that :issue:`24086` is fixed::

            sage: f = Newforms(24, 4)[0]
            sage: f.atkin_lehner_eigenvalue(8)
            -1
            sage: f.atkin_lehner_eigenvalue(3)
            -1

        A case where the eigenvalue isn't in the coefficient field of `f`::

            sage: chi = DirichletGroup(7, QQ).0
            sage: f = Newforms(chi, 3)[0]
            sage: f.atkin_lehner_eigenvalue()
            Traceback (most recent call last):
            ...
            ValueError: Unable to compute square root. Try specifying an embedding into a larger ring
            sage: emb = f.hecke_eigenvalue_field().embeddings(QQbar)[0]
            sage: f.atkin_lehner_eigenvalue(embedding=emb)
            0.?e-18 - 1.000000000000000?*I

        A case where the embeddings really matter::

            sage: chi2 = chi.extend(63)
            sage: g = Newforms(chi2, 3, names='a')[2]
            sage: g.atkin_lehner_eigenvalue(7)
            Traceback (most recent call last):
            ...
            ValueError: Unable to compute Gauss sum. Try specifying an embedding into a larger ring
            sage: g.atkin_lehner_eigenvalue(7, embedding=g.hecke_eigenvalue_field().embeddings(QQbar)[0])
            0.?e-18 + 1.000000000000000?*I
        """
    def twist(self, chi, level=None, check: bool = True):
        """
        Return the twist of the newform ``self`` by the Dirichlet
        character ``chi``.

        If ``self`` is a newform `f` with character `\\epsilon` and
        `q`-expansion

        .. MATH::

            f(q) = \\sum_{n=1}^\\infty a_n q^n,

        then the twist by `\\chi` is the unique newform `f\\otimes\\chi`
        with character `\\epsilon\\chi^2` and `q`-expansion

        .. MATH::

            (f\\otimes\\chi)(q) = \\sum_{n=1}^\\infty b_n q^n

        satisfying `b_n = \\chi(n) a_n` for all but finitely many `n`.

        INPUT:

        - ``chi`` -- a Dirichlet character. Note that Sage must be able to
          determine a common base field into which both the Hecke eigenvalue
          field of self, and the field of values of ``chi``, can be embedded.

        - ``level`` -- (optional) the level `N` of the twisted form. If `N` is
          not given, the algorithm tries to compute `N` using [AL1978]_,
          Theorem 3.1; if this is not possible, it returns an error. If `N` is
          given but incorrect, i.e. the twisted form does not have level `N`,
          then this function will attempt to detect this and return an error,
          but it may sometimes return an incorrect answer (a newform of level
          `N` whose first few coefficients agree with those of `f \\otimes
          \\chi`).

        - ``check`` -- (optional) boolean; if ``True`` (default), ensure that
          the space of modular symbols that is computed is genuinely simple and
          new. This makes it less likely, but not impossible, that a wrong
          result is returned if an incorrect ``level`` is specified.

        OUTPUT:

        The form `f\\otimes\\chi` as an element of the set of newforms
        for `\\Gamma_1(N)` with character `\\epsilon\\chi^2`.

        EXAMPLES::

            sage: G = DirichletGroup(3, base_ring=QQ)
            sage: Delta = Newforms(SL2Z, 12)[0]; Delta
            q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
            sage: Delta.twist(G[0]) == Delta
            True
            sage: Delta.twist(G[1])  # long time (about 5 s)
            q + 24*q^2 - 1472*q^4 - 4830*q^5 + O(q^6)

            sage: M = CuspForms(Gamma1(13), 2)
            sage: f = M.newforms('a')[0]; f
            q + a0*q^2 + (-2*a0 - 4)*q^3 + (-a0 - 1)*q^4 + (2*a0 + 3)*q^5 + O(q^6)
            sage: f.twist(G[1])
            q - a0*q^2 + (-a0 - 1)*q^4 + (-2*a0 - 3)*q^5 + O(q^6)

            sage: f = Newforms(Gamma1(30), 2, names='a')[1]; f
            q + a1*q^2 - a1*q^3 - q^4 + (a1 - 2)*q^5 + O(q^6)
            sage: f.twist(f.character())
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot calculate 5-primary part of the level of the twist of q + a1*q^2 - a1*q^3 - q^4 + (a1 - 2)*q^5 + O(q^6) by Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -1
            sage: f.twist(f.character(), level=30)
            q - a1*q^2 + a1*q^3 - q^4 + (-a1 - 2)*q^5 + O(q^6)

        TESTS:

        We test that feeding inappropriate values of the ``level`` parameter is handled gracefully::

            sage: chi = DirichletGroup(1)[0]
            sage: Delta.twist(chi, level=3)
            Traceback (most recent call last):
            ...
            ValueError: twist of q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6) by Dirichlet character modulo 1 of conductor 1 is not a newform of level 3

        Twisting and twisting back works::

            sage: f = Newforms(11)[0]
            sage: chi = DirichletGroup(5).0
            sage: f.twist(chi).twist(~chi, level=11) == f
            True

        AUTHORS:

        - Peter Bruin (April 2015)
        """
    def minimal_twist(self, p=None):
        """
        Compute a pair `(g, chi)` such that `g = f \\otimes \\chi`, where `f` is
        this newform and `\\chi` is a Dirichlet character, such that `g` has
        level as small as possible. If the optional argument `p` is given,
        consider only twists by Dirichlet characters of `p`-power conductor.

        EXAMPLES::

            sage: f = Newforms(121, 2)[3]
            sage: g, chi = f.minimal_twist()
            sage: g
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
            sage: chi
            Dirichlet character modulo 11 of conductor 11 mapping 2 |--> -1
            sage: f.twist(chi, level=11) == g
            True

            sage: # long time
            sage: f = Newforms(575, 2, names='a')[4]
            sage: g, chi = f.minimal_twist(5)
            sage: g
            q + a*q^2 - a*q^3 - 2*q^4 + (1/2*a + 2)*q^5 + O(q^6)
            sage: chi
            Dirichlet character modulo 5 of conductor 5 mapping 2 |--> 1/2*a
            sage: f.twist(chi, level=g.level()) == g
            True
        """
    def local_component(self, p, twist_factor=None):
        '''
        Calculate the local component at the prime `p` of the automorphic
        representation attached to this newform. For more information, see the
        documentation of the :func:`LocalComponent` function.

        EXAMPLES::

            sage: f = Newform("49a")
            sage: f.local_component(7)
            Smooth representation of GL_2(Q_7) with conductor 7^2
        '''

class ModularFormElement(ModularForm_abstract, element.HeckeModuleElement):
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        An element of a space of modular forms.

        INPUT:

        - ``parent`` -- :class:`ModularFormsSpace` (an ambient space of modular
          forms)

        - ``x`` -- a vector on the basis for parent

        - ``check`` -- if check is ``True``, check the types of the
          inputs

        OUTPUT: ``ModularFormElement`` -- a modular form

        EXAMPLES::

            sage: M = ModularForms(Gamma0(11),2)
            sage: f = M.0
            sage: f.parent()
            Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Rational Field
        """
    def __mul__(self, other):
        """
        Calculate the product ``self * other``.

        This tries to determine the
        characters of ``self`` and ``other``, in order to avoid having to compute a
        (potentially very large) Gamma1 space. Note that this might lead to
        a modular form that is defined with respect to a larger subgroup than
        the factors are.

        An example with character::

            sage: f = ModularForms(DirichletGroup(3).0, 3).0
            sage: f * f
            1 + 108*q^2 + 144*q^3 + 2916*q^4 + 8640*q^5 + O(q^6)
            sage: (f*f).parent()
            Modular Forms space of dimension 3 for Congruence Subgroup Gamma0(3) of weight 6 over Rational Field
            sage: (f*f*f).parent()
            Modular Forms space of dimension 4, character [-1] and weight 9 over Rational Field

        An example where the character is computed on-the-fly::

            sage: f = ModularForms(Gamma1(3), 5).0
            sage: f*f
            1 - 180*q^2 - 480*q^3 + 8100*q^4 + 35712*q^5 + O(q^6)
            sage: (f*f).parent()
            Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(3) of weight 10 over Rational Field

            sage: f = ModularForms(Gamma1(3), 7).0
            sage: f*f
            q^2 - 54*q^4 + 128*q^5 + O(q^6)
            sage: (f*f).parent()
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(3) of weight 14 over Rational Field

        An example with no character::

            sage: f = ModularForms(Gamma1(5), 2).0
            sage: f*f
            1 + 120*q^3 - 240*q^4 + 480*q^5 + O(q^6)
            sage: (f*f).parent()
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma1(5) of weight 4 over Rational Field

        TESTS:

        This shows that the issue at :issue:`7548` is fixed::

            sage: M = CuspForms(Gamma0(5*3^2), 2)
            sage: f = M.basis()[0]
            sage: 2*f
            2*q - 2*q^4 + O(q^6)
            sage: f*2
            2*q - 2*q^4 + O(q^6)
        """
    def atkin_lehner_eigenvalue(self, d=None, embedding=None):
        """
        Return the result of the Atkin-Lehner operator `W_d` on
        ``self``.

        INPUT:

        - ``d`` -- positive integer exactly dividing the level `N` of
          ``self``, i.e. `d` divides `N` and is coprime to `N/d`. (default: `d
          = N`)

        - ``embedding`` -- ignored (but accepted for compatibility with
          :meth:`Newform.atkin_lehner_eigenvalue`)

        OUTPUT:

        The Atkin-Lehner eigenvalue of `W_d` on ``self``. If ``self`` is not an
        eigenform for `W_d`, a :exc:`ValueError` is raised.

        .. SEEALSO::

            For the conventions used to define the operator `W_d`, see
            :meth:`sage.modular.hecke.module.HeckeModule_free_module.atkin_lehner_operator`.

        EXAMPLES::

            sage: CuspForms(1, 30).0.atkin_lehner_eigenvalue()
            1
            sage: CuspForms(2, 8).0.atkin_lehner_eigenvalue()
            Traceback (most recent call last):
            ...
            NotImplementedError: don't know how to compute Atkin-Lehner matrix acting on this space (try using a newform constructor instead)
        """
    def twist(self, chi, level=None):
        """
        Return the twist of the modular form ``self`` by the Dirichlet
        character ``chi``.

        If ``self`` is a modular form `f` with character `\\epsilon`
        and `q`-expansion

        .. MATH::

            f(q) = \\sum_{n=0}^\\infty a_n q^n,

        then the twist by `\\chi` is a modular form `f_\\chi` with
        character `\\epsilon\\chi^2` and `q`-expansion

        .. MATH::

            f_\\chi(q) = \\sum_{n=0}^\\infty \\chi(n) a_n q^n.

        INPUT:

        - ``chi`` -- a Dirichlet character

        - ``level`` -- (optional) the level `N` of the twisted form.
          By default, the algorithm chooses some not necessarily
          minimal value for `N` using [AL1978]_, Proposition 3.1,
          (See also [Kob1993]_, Proposition III.3.17, for a simpler
          but slightly weaker bound.)

        OUTPUT:

        The form `f_\\chi` as an element of the space of modular forms
        for `\\Gamma_1(N)` with character `\\epsilon\\chi^2`.

        EXAMPLES::

            sage: f = CuspForms(11, 2).0
            sage: f.parent()
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Rational Field
            sage: f.q_expansion(6)
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
            sage: eps = DirichletGroup(3).0
            sage: eps.parent()
            Group of Dirichlet characters modulo 3 with values in Cyclotomic Field of order 2 and degree 1
            sage: f_eps = f.twist(eps)
            sage: f_eps.parent()
            Cuspidal subspace of dimension 9 of Modular Forms space of dimension 16 for Congruence Subgroup Gamma0(99) of weight 2 over Cyclotomic Field of order 2 and degree 1
            sage: f_eps.q_expansion(6)
            q + 2*q^2 + 2*q^4 - q^5 + O(q^6)

        Modular forms without character are supported::

            sage: M = ModularForms(Gamma1(5), 2)
            sage: f = M.gen(0); f
            1 + 60*q^3 - 120*q^4 + 240*q^5 + O(q^6)
            sage: chi = DirichletGroup(2)[0]
            sage: f.twist(chi)
            60*q^3 + 240*q^5 + O(q^6)

        The base field of the twisted form is extended if necessary::

            sage: E4 = ModularForms(1, 4).gen(0)
            sage: E4.parent()
            Modular Forms space of dimension 1 for Modular Group SL(2,Z) of weight 4 over Rational Field
            sage: chi = DirichletGroup(5)[1]
            sage: chi.base_ring()
            Cyclotomic Field of order 4 and degree 2
            sage: E4_chi = E4.twist(chi)
            sage: E4_chi.parent()
            Modular Forms space of dimension 10, character [-1] and weight 4 over Cyclotomic Field of order 4 and degree 2

        REFERENCES:

        - [AL1978]_

        - [Kob1993]_

        AUTHORS:

        - \\L. J. P. Kilford (2009-08-28)

        - Peter Bruin (2015-03-30)
        """

class ModularFormElement_elliptic_curve(Newform):
    """
    A modular form attached to an elliptic curve over `\\QQ`.
    """
    def __init__(self, parent, E) -> None:
        """
        Modular form attached to an elliptic curve as an element
        of a space of modular forms.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: f = E.modular_form()
            sage: f
            q - 2*q^2 - 2*q^3 + 2*q^4 - 3*q^5 + O(q^6)
            sage: f.q_expansion(10)
            q - 2*q^2 - 2*q^3 + 2*q^4 - 3*q^5 + 4*q^6 - 5*q^7 + q^9 + O(q^10)
            sage: f.parent()
            Modular Forms space of dimension 33 for Congruence Subgroup Gamma0(389) of weight 2 over Rational Field

            sage: E = EllipticCurve('37a')
            sage: f = E.modular_form() ; f
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + O(q^6)
            sage: f == loads(dumps(f))
            True
        """
    def elliptic_curve(self):
        """
        Return elliptic curve associated to ``self``.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: f = E.modular_form()
            sage: f.elliptic_curve()
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: f.elliptic_curve() is E
            True
        """
    def atkin_lehner_eigenvalue(self, d=None, embedding=None):
        """
        Return the result of the Atkin-Lehner operator `W_d` on
        ``self``.

        INPUT:

        - ``d`` -- positive integer exactly dividing the level `N` of
          ``self``, i.e. `d` divides `N` and is coprime to `N/d`. (Defaults to
          `d = N` if not given.)

        - ``embedding`` -- ignored (but accepted for compatibility with
          :meth:`Newform.atkin_lehner_action`)

        OUTPUT:

        The Atkin-Lehner eigenvalue of `W_d` on ``self``. This is either `1` or
        `-1`.

        EXAMPLES::

            sage: EllipticCurve('57a1').newform().atkin_lehner_eigenvalue()
            1
            sage: EllipticCurve('57b1').newform().atkin_lehner_eigenvalue()
            -1
            sage: EllipticCurve('57b1').newform().atkin_lehner_eigenvalue(19)
            1
        """

class EisensteinSeries(ModularFormElement):
    """
    An Eisenstein series.

    EXAMPLES::

        sage: E = EisensteinForms(1,12)
        sage: E.eisenstein_series()
        [691/65520 + q + 2049*q^2 + 177148*q^3 + 4196353*q^4 + 48828126*q^5 + O(q^6)]
        sage: E = EisensteinForms(11,2)
        sage: E.eisenstein_series()
        [5/12 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + O(q^6)]
        sage: E = EisensteinForms(Gamma1(7),2)
        sage: E.set_precision(4)
        sage: E.eisenstein_series()
        [1/4 + q + 3*q^2 + 4*q^3 + O(q^4),
         1/7*zeta6 - 3/7 + q + (-2*zeta6 + 1)*q^2 + (3*zeta6 - 2)*q^3 + O(q^4),
         q + (-zeta6 + 2)*q^2 + (zeta6 + 2)*q^3 + O(q^4),
         -1/7*zeta6 - 2/7 + q + (2*zeta6 - 1)*q^2 + (-3*zeta6 + 1)*q^3 + O(q^4),
         q + (zeta6 + 1)*q^2 + (-zeta6 + 3)*q^3 + O(q^4)]
    """
    def __init__(self, parent, vector, t, chi, psi) -> None:
        """
        An Eisenstein series.

        EXAMPLES::

            sage: E = EisensteinForms(1,12)  # indirect doctest
            sage: E.eisenstein_series()
            [691/65520 + q + 2049*q^2 + 177148*q^3 + 4196353*q^4 + 48828126*q^5 + O(q^6)]
            sage: E = EisensteinForms(11,2)
            sage: E.eisenstein_series()
            [5/12 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + O(q^6)]
            sage: E = EisensteinForms(Gamma1(7),2)
            sage: E.set_precision(4)
            sage: E.eisenstein_series()
            [1/4 + q + 3*q^2 + 4*q^3 + O(q^4),
             1/7*zeta6 - 3/7 + q + (-2*zeta6 + 1)*q^2 + (3*zeta6 - 2)*q^3 + O(q^4),
             q + (-zeta6 + 2)*q^2 + (zeta6 + 2)*q^3 + O(q^4),
             -1/7*zeta6 - 2/7 + q + (2*zeta6 - 1)*q^2 + (-3*zeta6 + 1)*q^3 + O(q^4),
             q + (zeta6 + 1)*q^2 + (-zeta6 + 3)*q^3 + O(q^4)]
        """
    def chi(self):
        """
        Return the parameter chi associated to ``self``.

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].chi()
            Dirichlet character modulo 17 of conductor 17 mapping 3 |--> zeta16
        """
    def psi(self):
        """
        Return the parameter psi associated to ``self``.

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].psi()
             Dirichlet character modulo 17 of conductor 1 mapping 3 |--> 1
        """
    def t(self):
        """
        Return the parameter t associated to ``self``.

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].t()
            1
        """
    def parameters(self):
        """
        Return chi, psi, and t, which are the defining parameters of ``self``.

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].parameters()
            (Dirichlet character modulo 17 of conductor 17 mapping 3 |--> zeta16, Dirichlet character modulo 17 of conductor 1 mapping 3 |--> 1, 1)
        """
    def L(self):
        """
        Return the conductor of self.chi().

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].L()
            17
        """
    def M(self):
        """
        Return the conductor of self.psi().

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].M()
            1
        """
    @cached_method
    def character(self):
        """
        Return the character associated to ``self``.

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].character()
            Dirichlet character modulo 17 of conductor 17 mapping 3 |--> zeta16

            sage: chi = DirichletGroup(7)[4]
            sage: E = EisensteinForms(chi).eisenstein_series() ; E
            [-1/7*zeta6 - 2/7 + q + (2*zeta6 - 1)*q^2 + (-3*zeta6 + 1)*q^3 + (-2*zeta6 - 1)*q^4 + (5*zeta6 - 4)*q^5 + O(q^6),
             q + (zeta6 + 1)*q^2 + (-zeta6 + 3)*q^3 + (zeta6 + 2)*q^4 + (zeta6 + 4)*q^5 + O(q^6)]
            sage: E[0].character() == chi
            True
            sage: E[1].character() == chi
            True

        TESTS::

            sage: [ [ f.character() == chi for f in EisensteinForms(chi).eisenstein_series() ] for chi in DirichletGroup(17) ]
            [[True], [], [True, True], [], [True, True], [], [True, True], [], [True, True], [], [True, True], [], [True, True], [], [True, True], []]

            sage: [ [ f.character() == chi for f in EisensteinForms(chi).eisenstein_series() ] for chi in DirichletGroup(16) ]
            [[True, True, True, True, True], [], [True, True], [], [True, True, True, True], [], [True, True], []]
        """
    def new_level(self):
        """
        Return level at which ``self`` is new.

        EXAMPLES::

            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].level()
            17
            sage: EisensteinForms(DirichletGroup(17).0,99).eisenstein_series()[1].new_level()
            17
            sage: [ [x.level(), x.new_level()] for x in EisensteinForms(DirichletGroup(60).0^2,2).eisenstein_series() ]
            [[60, 2], [60, 3], [60, 2], [60, 5], [60, 2], [60, 2], [60, 2], [60, 3], [60, 2], [60, 2], [60, 2]]
        """

class GradedModularFormElement(ModuleElement):
    """
    The element class for ``ModularFormsRing``. A ``GradedModularFormElement`` is basically a
    formal sum of modular forms of different weight: `f_1 + f_2 + ... + f_n`. Note that a
    ``GradedModularFormElement`` is not necessarily a modular form (as it can have mixed weight
    components).

    A ``GradedModularFormElement`` should not be constructed directly via this class. Instead,
    one should use the element constructor of the parent class (``ModularFormsRing``).

    EXAMPLES::

        sage: M = ModularFormsRing(1)
        sage: D = CuspForms(1, 12).0
        sage: M(D).parent()
        Ring of Modular Forms for Modular Group SL(2,Z) over Rational Field

    A graded modular form can be initiated via a dictionary or a list::

        sage: E4 = ModularForms(1, 4).0
        sage: M({4:E4, 12:D})  # dictionary
        1 + 241*q + 2136*q^2 + 6972*q^3 + 16048*q^4 + 35070*q^5 + O(q^6)
        sage: M([E4, D])  # list
        1 + 241*q + 2136*q^2 + 6972*q^3 + 16048*q^4 + 35070*q^5 + O(q^6)

    Also, when adding two modular forms of different weights, a graded modular form element will be created::

        sage: (E4 + D).parent()
        Ring of Modular Forms for Modular Group SL(2,Z) over Rational Field
        sage: M([E4, D]) == E4 + D
        True

    Graded modular forms elements for congruence subgroups are also supported::

        sage: M = ModularFormsRing(Gamma0(3))
        sage: f = ModularForms(Gamma0(3), 4).0
        sage: g = ModularForms(Gamma0(3), 2).0
        sage: M([f, g])
        2 + 12*q + 36*q^2 + 252*q^3 + 84*q^4 + 72*q^5 + O(q^6)
        sage: M({4:f, 2:g})
        2 + 12*q + 36*q^2 + 252*q^3 + 84*q^4 + 72*q^5 + O(q^6)
    """
    def __init__(self, parent, forms_datum) -> None:
        """
        INPUT:

        - ``parent`` -- an object of the class ``ModularFormsRing``
        - ``forms_datum`` -- dictionary ``{k_1:f_1, k_2:f_2, ..., k_n:f_n}``
          or a list ``[f_1, f_2,..., f_n]`` where `f_i` is a modular form of
          weight `k_i`

        OUTPUT: a ``GradedModularFormElement`` corresponding to `f_1 + f_2 + ... + f_n`

        TESTS::

            sage: M = ModularFormsRing(1)
            sage: E4 = ModularForms(1,4).0
            sage: M({6:E4})
            Traceback (most recent call last):
            ...
            ValueError: at least one key (6) of the defining dictionary does not correspond to the weight of its value (1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)). Real weight: 4
            sage: M({4:'f'})
            Traceback (most recent call last):
            ...
            ValueError: at least one value (f) of the defining dictionary is not a `ModularFormElement`
            sage: M({4.:E4})
            Traceback (most recent call last):
            ...
            ValueError: at least one key (4.00000000000000) of the defining dictionary is not an integer
            sage: M({0:E4})
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Modular Forms space of dimension 1 for Modular Group SL(2,Z) of weight 4 over Rational Field to Rational Field
            sage: M([E4, x])                                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Symbolic Ring to Rational Field
            sage: M([E4, ModularForms(3, 6).0])
            Traceback (most recent call last):
            ...
            ValueError: the group and/or the base ring of at least one modular form (q - 6*q^2 + 9*q^3 + 4*q^4 + 6*q^5 + O(q^6)) is not consistent with the base space
            sage: M({4:E4, 6:ModularForms(3, 6).0})
            Traceback (most recent call last):
            ...
            ValueError: the group and/or the base ring of at least one modular form (q - 6*q^2 + 9*q^3 + 4*q^4 + 6*q^5 + O(q^6)) is not consistent with the base space
            sage: M = ModularFormsRing(Gamma0(2))
            sage: E4 = ModularForms(1, 4).0
            sage: M(E4)[4].parent()
            Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(2) of weight 4 over Rational Field
            sage: M = ModularFormsRing(Gamma1(3), base_ring=GF(7))
            sage: E6 = ModularForms(1, 6, base_ring=GF(7)).0
            sage: M(E6)[6].parent()
            Modular Forms space of dimension 3 for Congruence Subgroup Gamma1(3) of weight 6 over Finite Field of size 7
        """
    def __bool__(self) -> bool:
        '''
        Return "True" if ``self`` is nonzero and "False" otherwise.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: bool(M(0))
            False
            sage: bool(M(1))
            True
            sage: bool(M(ModularForms(1,6).0))
            True
        '''
    def is_zero(self) -> bool:
        '''
        Return "True" if the graded form is 0 and "False" otherwise.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: M(0).is_zero()
            True
            sage: M(1/2).is_zero()
            False
            sage: E6 = M.1
            sage: M(E6).is_zero()
            False
        '''
    def is_one(self) -> bool:
        '''
        Return "True" if the graded form is 1 and "False" otherwise.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: M(1).is_one()
            True
            sage: M(2).is_one()
            False
            sage: E6 = M.0
            sage: E6.is_one()
            False
        '''
    def group(self):
        """
        Return the group for which ``self`` is a modular form.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: E4 = M.0
            sage: E4.group()
            Modular Group SL(2,Z)
            sage: M5 = ModularFormsRing(Gamma1(5))
            sage: f = M5(ModularForms(Gamma1(5)).0);
            sage: f.group()
            Congruence Subgroup Gamma1(5)
        """
    def q_expansion(self, prec=None):
        """
        Return the `q`-expansion of the graded modular form up to precision
        ``prec`` (default: 6).

        An alias of this method is ``qexp``.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: zer = M(0); zer.q_expansion()
            0
            sage: M(5/7).q_expansion()
            5/7
            sage: E4 = M.0; E4
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: E6 = M.1; E6
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)
            sage: F = E4 + E6; F
            2 - 264*q - 14472*q^2 - 116256*q^3 - 515208*q^4 - 1545264*q^5 + O(q^6)
            sage: F.q_expansion()
            2 - 264*q - 14472*q^2 - 116256*q^3 - 515208*q^4 - 1545264*q^5 + O(q^6)
            sage: F.q_expansion(10)
            2 - 264*q - 14472*q^2 - 116256*q^3 - 515208*q^4 - 1545264*q^5 - 3997728*q^6 - 8388672*q^7 - 16907400*q^8 - 29701992*q^9 + O(q^10)
        """
    qexp = q_expansion
    def coefficients(self, X):
        """
        Return the coefficients `a_n` of the `q`-expansion of this modular form.

        INPUT:

        - ``X`` -- an iterable or an integer. If ``X`` is iterable, a list
          containing all `a_{X_i}` is returned. If ``X`` is an integer, it must
          be positive, in which case the coefficients `a_1` to `a_X` are
          returned in a list.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: E4 = M.0; E6 = M.1
            sage: F = E4 + E6
            sage: F.coefficients([0,1,3,6])
            [2, -264, -116256, -3997728]
            sage: F.coefficients(10)
            [-264, -14472, -116256, -515208, -1545264, -3997728, -8388672, -16907400, -29701992, -51719472]
            sage: assert _ == F.coefficients(range(1, 11)) == list(F.qexp(11))[1:]

        ::

            sage: F = ModularFormsRing(13).0
            sage: (F^3).coefficients(range(10, 20))
            [22812, 36552, 57680, 85686, 126744, 177408, 249246, 332172, 448926, 575736]
        """
    def __getitem__(self, weight):
        """
        Return the homogeneous component of the given graded modular form.

        INPUT:

        - ``weight`` -- integer corresponding to the weight of the
          homogeneous component of the given graded modular form

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: f4 = ModularForms(1, 4).0; f6 = ModularForms(1, 6).0; f8 = ModularForms(1, 8).0
            sage: F = M(f4) + M(f6) + M(f8)
            sage: F[4] # indirect doctest
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: F[6] # indirect doctest
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)
            sage: F[8] # indirect doctest
            1 + 480*q + 61920*q^2 + 1050240*q^3 + 7926240*q^4 + 37500480*q^5 + O(q^6)
            sage: F[10] # indirect doctest
            0
            sage: F.homogeneous_component(4)
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)

        TESTS::

            sage: M = ModularFormsRing(1)
            sage: f = M.0
            sage: f['a']
            Traceback (most recent call last):
            ...
            KeyError: 'the weight must be an integer'
            sage: f[-1]
            Traceback (most recent call last):
            ...
            ValueError: the weight must be nonnegative
        """
    homogeneous_component = __getitem__
    def __call__(self, x, prec=None):
        """
        Evaluate the `q`-expansion of this graded modular form at x.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: f4 = ModularForms(1, 4).0; f6 = ModularForms(1, 6).0; f8 = ModularForms(1, 8).0
            sage: F = M(f4) + M(f6) + M(f8); F # indirect doctest
            3 + 216*q + 47448*q^2 + 933984*q^3 + 7411032*q^4 + 35955216*q^5 + O(q^6)
            sage: q = F.q_expansion().parent().gen()
            sage: F(q^2) # indirect doctest
            3 + 216*q^2 + 47448*q^4 + 933984*q^6 + 7411032*q^8 + 35955216*q^10 + O(q^12)
            sage: G = M(113/19)
            sage: G(q) # indirect doctest
            113/19
        """
    def __neg__(self):
        """
        The negation of ``self``.

        TESTS::

            sage: M = ModularFormsRing(1)
            sage: F4 = M(ModularForms(1, 4).0); F6 = M(ModularForms(1, 6).0);
            sage: -F4 # indirect doctest
            -1 - 240*q - 2160*q^2 - 6720*q^3 - 17520*q^4 - 30240*q^5 + O(q^6)
            sage: F4 - F6 # indirect doctest
            744*q + 18792*q^2 + 129696*q^3 + 550248*q^4 + 1605744*q^5 + O(q^6)
        """
    def weight(self):
        """
        Return the weight of the given form if it is homogeneous (i.e. a modular form).

        EXAMPLES::

            sage: D = ModularForms(1,12).0; M = ModularFormsRing(1)
            sage: M(D).weight()
            12
            sage: M.zero().weight()
            0
            sage: e4 = ModularForms(1,4).0
            sage: (M(D)+e4).weight()
            Traceback (most recent call last):
            ...
            ValueError: the given graded form is not homogeneous (not a modular form)
        """
    def weights_list(self):
        """
        Return the list of the weights of all the homogeneous components of the
        given graded modular form.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: f4 = ModularForms(1, 4).0; f6 = ModularForms(1, 6).0; f8 = ModularForms(1, 8).0
            sage: F4 = M(f4); F6 = M(f6); F8 = M(f8)
            sage: F = F4 + F6 + F8
            sage: F.weights_list()
            [4, 6, 8]
            sage: M(0).weights_list()
            [0]
        """
    def is_homogeneous(self) -> bool:
        """
        Return ``True`` if the graded modular form is homogeneous, i.e. if it
        is a modular forms of a certain weight.

        An alias of this method is ``is_modular_form``

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: E4 = M.0; E6 = M.1;
            sage: E4.is_homogeneous()
            True
            sage: F = E4 + E6 # Not a modular form
            sage: F.is_homogeneous()
            False
        """
    is_modular_form = is_homogeneous
    def to_polynomial(self, names: str = 'x', gens=None):
        """
        Return a polynomial `P(x_0,..., x_n)` such that `P(g_0,..., g_n)` is equal to ``self``
        where `g_0, ..., g_n` is a list of generators of the parent.

        INPUT:

        - ``names`` -- list or tuple of names (strings), or a comma separated
          string; corresponds to the names of the variables
        - ``gens`` -- (default: ``None``) a list of generator of the parent of
          ``self``. If set to ``None``, the list returned by
          :meth:`~sage.modular.modform.find_generator.ModularFormsRing.gen_forms`
          is used instead

        OUTPUT: a polynomial in the variables ``names``

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: (M.0 + M.1).to_polynomial()
            x1 + x0
            sage: (M.0^10 + M.0 * M.1).to_polynomial()
            x0^10 + x0*x1

        This method is not necessarily the inverse of
        :meth:`~sage.modular.modform.ring.ModularFormsRing.from_polynomial` since there may be some
        relations between the generators of the modular forms ring::

            sage: M = ModularFormsRing(Gamma0(6))
            sage: P.<x0,x1,x2> = M.polynomial_ring()
            sage: M.from_polynomial(x1^2).to_polynomial()
            x0*x2 + 2*x1*x2 + 11*x2^2
        """
    def serre_derivative(self):
        """
        Return the Serre derivative of the given graded modular form.

        If ``self`` is a modular form of weight `k`, then the returned modular
        form will be of weight `k + 2`. If the form is not homogeneous, then
        this method sums the Serre derivative of each homogeneous component.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: E4 = M.0
            sage: E6 = M.1
            sage: DE4 = E4.serre_derivative(); DE4
            -1/3 + 168*q + 5544*q^2 + 40992*q^3 + 177576*q^4 + 525168*q^5 + O(q^6)
            sage: DE4 == (-1/3) * E6
            True
            sage: DE6 = E6.serre_derivative(); DE6
            -1/2 - 240*q - 30960*q^2 - 525120*q^3 - 3963120*q^4 - 18750240*q^5 + O(q^6)
            sage: DE6 == (-1/2) * E4^2
            True
            sage: f = E4 + E6
            sage: Df = f.serre_derivative(); Df
            -5/6 - 72*q - 25416*q^2 - 484128*q^3 - 3785544*q^4 - 18225072*q^5 + O(q^6)
            sage: Df == (-1/3) * E6 + (-1/2) * E4^2
            True
            sage: M(1/2).serre_derivative()
            0
        """
    def derivative(self, name: str = 'E2'):
        """
        Return the derivative `q \\frac{d}{dq}` of the given graded form.

        Note that this method returns an element of a new parent, that is a
        quasimodular form. If the form is not homogeneous, then this method sums
        the derivative of each homogeneous component.

        INPUT:

        - ``name``-- string (default: ``'E2'``); the name of the weight 2
          Eisenstein series generating the graded algebra of quasimodular forms
          over the ring of modular forms

        OUTPUT: a :class:`sage.modular.quasimodform.element.QuasiModularFormsElement`

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: E4 = M.0; E6 = M.1
            sage: dE4 = E4.derivative(); dE4
            240*q + 4320*q^2 + 20160*q^3 + 70080*q^4 + 151200*q^5 + O(q^6)
            sage: dE4.parent()
            Ring of Quasimodular Forms for Modular Group SL(2,Z) over Rational Field
            sage: dE4.is_modular_form()
            False
        """
