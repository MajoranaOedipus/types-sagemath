from sage.modular.arithgroup.congroup_sl2z import SL2Z_class as SL2Z_class
from sage.modular.modform.constructor import EisensteinForms as EisensteinForms
from sage.modular.modform.eis_series import eisenstein_series_qexp as eisenstein_series_qexp
from sage.modular.modform.element import GradedModularFormElement as GradedModularFormElement
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp

class QuasiModularFormsElement(ModuleElement):
    """
    A quasimodular forms ring element. Such an element is described by
    SageMath as a polynomial

    .. MATH::

        F = f_0 + f_1 E_2 + f_2 E_2^2 + \\cdots + f_m E_2^m

    where each `f_i` a graded modular form element
    (see :class:`~sage.modular.modform.element.GradedModularFormElement`)

    For an integer `k`, we say that `F` is homogeneous of weight `k` if
    it lies in an homogeneous component of degree `k` of the graded ring
    of quasimodular forms.

    EXAMPLES::

        sage: QM = QuasiModularForms(1)
        sage: QM.gens()
        (1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
        1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
        1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6))
        sage: QM.0 + QM.1
        2 + 216*q + 2088*q^2 + 6624*q^3 + 17352*q^4 + 30096*q^5 + O(q^6)
        sage: QM.0 * QM.1
        1 + 216*q - 3672*q^2 - 62496*q^3 - 322488*q^4 - 1121904*q^5 + O(q^6)
        sage: (QM.0)^2
        1 - 48*q + 432*q^2 + 3264*q^3 + 9456*q^4 + 21600*q^5 + O(q^6)
        sage: QM.0 == QM.1
        False

    Quasimodular forms ring element can be created via a polynomial in `E2` over the ring of modular forms::

        sage: E2 = QM.polygen()
        sage: E2.parent()
        Univariate Polynomial Ring in E2 over Ring of Modular Forms for Modular Group SL(2,Z) over Rational Field
        sage: QM(E2)
        1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
        sage: M = QM.modular_forms_subring()
        sage: QM(M.0 * E2 + M.1 * E2^2)
        2 - 336*q + 4320*q^2 + 398400*q^3 - 3772992*q^4 - 89283168*q^5 + O(q^6)

    One may convert a quasimodular form into a multivariate polynomial in the
    generators of the ring by calling
    :meth:`~sage.modular.quasimodform.element.QuasiModularFormsElement.polynomial`::

        sage: QM = QuasiModularForms(1)
        sage: F = QM.0^2 + QM.1^2 + QM.0*QM.1*QM.2
        sage: F.polynomial()
        E2*E4*E6 + E4^2 + E2^2

    If the group is not the full modular group, the default names of the
    generators are given by ``Ek_i`` and ``Sk_i`` to denote the `i`-th basis
    element of the weight `k` Eisenstein subspace and cuspidal subspace
    respectively (for more details, see the documentation of
    :meth:`~sage.modular.quasimodform.ring.QuasiModularFormsRing.polynomial_ring`) ::

        sage: QM = QuasiModularForms(Gamma1(4))
        sage: F = (QM.0^4)*(QM.1^3) + QM.3
        sage: F.polynomial()
        -512*E2^4*E2_1^3 + E2^4*E3_0^2 + 48*E2^4*E3_1^2 + E3_0
    """
    def __init__(self, parent, polynomial) -> None:
        """
        INPUT:

        - ``parent`` -- a quasimodular forms ring
        - ``polynomial`` -- a polynomial `f_0 + f_1 E_2 + ... + f_n E_2^n` where
          each `f_i` are modular forms ring elements and `E_2` correspond to the
          weight 2 Eisenstein series

        OUTPUT: ``QuasiModularFormsElement``

        TESTS::

            sage: QM = QuasiModularForms(1)
            sage: QM.element_class(QM, 'E2')
            Traceback (most recent call last):
            ...
            TypeError: 'polynomial' argument should be of type 'Polynomial'
            sage: x = polygen(QQ)
            sage: QM.element_class(QM, x^2 + 1)
            Traceback (most recent call last):
            ...
            ValueError: at least one coefficient is not a 'GradedModularFormElement'
        """
    def q_expansion(self, prec: int = 6):
        """
        Return the `q`-expansion of the given quasimodular form up to precision
        ``prec`` (default: 6).

        An alias of this method is ``qexp``.

        EXAMPLES::

            sage: QM = QuasiModularForms()
            sage: E2 = QM.0
            sage: E2.q_expansion()
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: E2.q_expansion(prec=10)
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 - 288*q^6 - 192*q^7 - 360*q^8 - 312*q^9 + O(q^10)
        """
    qexp = q_expansion
    def __neg__(self):
        """
        The negation of ``self``.

        TESTS::

            sage: -QuasiModularForms(1).0
            -1 + 24*q + 72*q^2 + 96*q^3 + 168*q^4 + 144*q^5 + O(q^6)
            sage: QuasiModularForms(1).0 - QuasiModularForms(1).0
            0
            sage: -QuasiModularForms(Gamma1(2)).2
            -1 - 240*q^2 - 2160*q^4 + O(q^6)
        """
    def __bool__(self) -> bool:
        """
        Return whether ``self`` is nonzero.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: bool(QM(0))
            False
            sage: bool(QM(1))
            True
            sage: bool(QM.0)
            True
        """
    def depth(self):
        """
        Return the depth of this quasimodular form.

        Note that the quasimodular form must be homogeneous of weight
        `k`. Recall that the *depth* is the integer `p` such that

        .. MATH::

            f = f_0 + f_1 E_2 + \\cdots + f_p E_2^p,

        where `f_i` is a modular form of weight `k - 2i` and `f_p` is
        nonzero.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: E2, E4, E6 = QM.gens()
            sage: E2.depth()
            1
            sage: F = E4^2 + E6*E2 + E4*E2^2 + E2^4
            sage: F.depth()
            4
            sage: QM(7/11).depth()
            0

        TESTS::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0 + QM.1).depth()
            Traceback (most recent call last):
            ...
            ValueError: the given graded quasiform is not an homogeneous element
        """
    def is_zero(self) -> bool:
        """
        Return whether the given quasimodular form is zero.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.zero().is_zero()
            True
            sage: QM(0).is_zero()
            True
            sage: QM(1/2).is_zero()
            False
            sage: (QM.0).is_zero()
            False
            sage: QM = QuasiModularForms(Gamma0(2))
            sage: QM(0).is_zero()
            True
        """
    def is_one(self) -> bool:
        """
        Return whether the given quasimodular form is 1, i.e. the
        multiplicative identity.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.one().is_one()
            True
            sage: QM(1).is_one()
            True
            sage: (QM.0).is_one()
            False
            sage: QM = QuasiModularForms(Gamma0(2))
            sage: QM(1).is_one()
            True
        """
    def is_graded_modular_form(self) -> bool:
        """
        Return whether the given quasimodular form is a
        graded modular form element
        (see :class:`~sage.modular.modform.element.GradedModularFormElement`).

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0).is_graded_modular_form()
            False
            sage: (QM.1).is_graded_modular_form()
            True
            sage: (QM.1 + QM.0^2).is_graded_modular_form()
            False
            sage: (QM.1^2 + QM.2).is_graded_modular_form()
            True
            sage: QM = QuasiModularForms(Gamma0(6))
            sage: (QM.0).is_graded_modular_form()
            False
            sage: (QM.1 + QM.2 + QM.1 * QM.3).is_graded_modular_form()
            True
            sage: QM.zero().is_graded_modular_form()
            True
            sage: QM = QuasiModularForms(Gamma0(6))
            sage: (QM.0).is_graded_modular_form()
            False
            sage: (QM.0 + QM.1*QM.2 + QM.3).is_graded_modular_form()
            False
            sage: (QM.1*QM.2 + QM.3).is_graded_modular_form()
            True

        .. NOTE::

            A graded modular form in SageMath is not necessarily a modular form
            as it can have mixed weight components. To check for modular forms
            only, see the method :meth:`is_modular_form`.
        """
    def is_modular_form(self) -> bool:
        """
        Return whether the given quasimodular form is a modular form.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0).is_modular_form()
            False
            sage: (QM.1).is_modular_form()
            True
            sage: (QM.1 + QM.2).is_modular_form() # mixed weight components
            False
            sage: QM.zero().is_modular_form()
            True
            sage: QM = QuasiModularForms(Gamma0(4))
            sage: (QM.0).is_modular_form()
            False
            sage: (QM.1).is_modular_form()
            True
        """
    def polynomial(self, names=None):
        """
        Return a multivariate polynomial such that every variable corresponds to
        a generator of the ring, ordered by the method:
        :meth:`~sage.modular.quasimodform.ring.QuasiModularForms.gens`.

        An alias of this method is ``to_polynomial``.

        INPUT:

        - ``names``-- string (default: ``None``); list or tuple of names
          (strings), or a comma separated string. Defines the names for the
          generators of the multivariate polynomial ring. The default names are
          of the form ``ABCk`` where ``k`` is a number corresponding to the
          weight of the form ``ABC``.

        OUTPUT: a multivariate polynomial in the variables ``names``

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0 + QM.1).polynomial()
            E4 + E2
            sage: (1/2 + QM.0 + 2*QM.1^2 + QM.0*QM.2).polynomial()
            E2*E6 + 2*E4^2 + E2 + 1/2

        Check that :issue:`34569` is fixed::

            sage: QM = QuasiModularForms(Gamma1(3))
            sage: QM.ngens()
            5
            sage: (QM.0 + QM.1 + QM.2*QM.1 + QM.3*QM.4).polynomial()
            E3_1*E4_0 + E2_0*E3_0 + E2 + E2_0
        """
    to_polynomial = polynomial
    def weights_list(self):
        """
        Return the list of the weights of all the graded components of the given
        graded quasimodular form.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0).weights_list()
            [2]
            sage: (QM.0 + QM.1 + QM.2).weights_list()
            [2, 4, 6]
            sage: (QM.0 * QM.1 + QM.2).weights_list()
            [6]
            sage: QM(1/2).weights_list()
            [0]
            sage: QM = QuasiModularForms(Gamma1(3))
            sage: (QM.0 + QM.1 + QM.2*QM.1 + QM.3*QM.4).weights_list()
            [2, 5, 7]
        """
    def is_homogeneous(self) -> bool:
        """
        Return whether the graded quasimodular form is a homogeneous element,
        that is, it lives in a unique graded components of the parent of
        ``self``.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: E2, E4, E6 = QM.gens()
            sage: (E2).is_homogeneous()
            True
            sage: (E2 + E4).is_homogeneous()
            False
            sage: (E2 * E4 + E6).is_homogeneous()
            True
            sage: QM(1).is_homogeneous()
            True
            sage: (1 + E2).is_homogeneous()
            False
            sage: F = E6^3 + E4^4*E2 + (E4^2*E6)*E2^2 + (E4^3 + E6^2)*E2^3
            sage: F.is_homogeneous()
            True
        """
    def weight(self):
        """
        Return the weight of the given quasimodular form.

        Note that the given form must be homogeneous. An alias of this method is
        ``degree``.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0).weight()
            2
            sage: (QM.0 * QM.1 + QM.2).weight()
            6
            sage: QM(1/2).weight()
            0
            sage: (QM.0).degree()
            2
            sage: (QM.0 + QM.1).weight()
            Traceback (most recent call last):
            ...
            ValueError: the given graded quasiform is not an homogeneous element
        """
    degree = weight
    def homogeneous_components(self):
        """
        Return a dictionary where the values are the homogeneous components of
        the given graded form and the keys are the weights of those components.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: (QM.0).homogeneous_components()
            {2: 1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)}
            sage: (QM.0 + QM.1 + QM.2).homogeneous_components()
            {2: 1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
             4: 1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
             6: 1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)}
            sage: (1 + QM.0).homogeneous_components()
            {0: 1, 2: 1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)}
            sage: QM5 = QuasiModularForms(Gamma1(3))
            sage: F = QM.1 + QM.1*QM.2 + QM.1*QM.0 + (QM.1 + QM.2^2)*QM.0^3
            sage: F.homogeneous_components()
            {4: 1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
             6: 1 + 216*q - 3672*q^2 - 62496*q^3 - 322488*q^4 - 1121904*q^5 + O(q^6),
             10: 2 - 96*q - 149040*q^2 - 4986240*q^3 - 67535952*q^4 - 538187328*q^5 + O(q^6),
             18: 1 - 1080*q + 294840*q^2 - 902880*q^3 - 452402280*q^4 + 105456816*q^5 + O(q^6)}
            sage: F = QM.zero()
            sage: F.homogeneous_components()
            {0: 0}
            sage: F = QM(42/13)
            sage: F.homogeneous_components()
            {0: 42/13}
        """
    def __getitem__(self, weight):
        """
        Return the homogeneous component of the given quasimodular form ring
        element.

        An alias of this method is ``homogeneous_component``.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: E2, E4, E6 = QM.gens()
            sage: F = E2 + E4*E6 + E2^3*E6
            sage: F[2]
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: F[10]
            1 - 264*q - 135432*q^2 - 5196576*q^3 - 69341448*q^4 - 515625264*q^5 + O(q^6)
            sage: F[12]
            1 - 576*q + 21168*q^2 + 308736*q^3 - 15034608*q^4 - 39208320*q^5 + O(q^6)
            sage: F[4]
            0
            sage: F.homogeneous_component(2)
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)

        TESTS::

            sage: F[x]                                                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            KeyError: 'the weight must be an integer'
            sage: F[-1]
            Traceback (most recent call last):
            ...
            ValueError: the weight must be nonnegative
        """
    homogeneous_component = __getitem__
    def serre_derivative(self):
        """
        Return the Serre derivative of the given quasimodular form.

        If the form is not homogeneous, then this method sums the Serre
        derivative of each homogeneous component.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: E2, E4, E6 = QM.gens()
            sage: DE2 = E2.serre_derivative(); DE2
            -1/6 - 16*q - 216*q^2 - 832*q^3 - 2248*q^4 - 4320*q^5 + O(q^6)
            sage: DE2 == (-E2^2 - E4)/12
            True
            sage: DE4 = E4.serre_derivative(); DE4
            -1/3 + 168*q + 5544*q^2 + 40992*q^3 + 177576*q^4 + 525168*q^5 + O(q^6)
            sage: DE4 == (-1/3) * E6
            True
            sage: DE6 = E6.serre_derivative(); DE6
            -1/2 - 240*q - 30960*q^2 - 525120*q^3 - 3963120*q^4 - 18750240*q^5 + O(q^6)
            sage: DE6 == (-1/2) * E4^2
            True

        The Serre derivative raises the weight of homogeneous elements by 2::

            sage: F = E6 + E4 * E2
            sage: F.weight()
            6
            sage: F.serre_derivative().weight()
            8

        Check that :issue:`34569` is fixed::

            sage: QM = QuasiModularForms(Gamma1(3))
            sage: E2 = QM.weight_2_eisenstein_series()
            sage: E2.serre_derivative()
            -1/6 - 16*q - 216*q^2 - 832*q^3 - 2248*q^4 - 4320*q^5 + O(q^6)
            sage: F = QM.0 + QM.1*QM.2
        """
    def derivative(self):
        """
        Return the derivative `q \\frac{d}{dq}` of the given quasimodular form.

        If the form is not homogeneous, then this method sums the derivative of
        each homogeneous component.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: E2, E4, E6 = QM.gens()
            sage: dE2 = E2.derivative(); dE2
            -24*q - 144*q^2 - 288*q^3 - 672*q^4 - 720*q^5 + O(q^6)
            sage: dE2 == (E2^2 - E4)/12 # Ramanujan identity
            True
            sage: dE4 = E4.derivative(); dE4
            240*q + 4320*q^2 + 20160*q^3 + 70080*q^4 + 151200*q^5 + O(q^6)
            sage: dE4 == (E2 * E4 - E6)/3 # Ramanujan identity
            True
            sage: dE6 = E6.derivative(); dE6
            -504*q - 33264*q^2 - 368928*q^3 - 2130912*q^4 - 7877520*q^5 + O(q^6)
            sage: dE6 == (E2 * E6 - E4^2)/2 # Ramanujan identity
            True

        Note that the derivative of a modular form is not necessarily a modular form::

            sage: dE4.is_modular_form()
            False
            sage: dE4.weight()
            6
        """
    def coefficients(self, X):
        """
        Return the coefficients of `q^n` of the `q`-expansion of this,
        graded quasimodular form for `n` in the list `X`.

        If X is an integer, return coefficients for indices from 1
        to X. This method caches the result.

        EXAMPLES::

            sage: E2, E4 = QuasiModularForms(1).0, QuasiModularForms(1).1
            sage: f = E2^2
            sage: g = E2^3 * E4
            sage: f.coefficients(10)
            [-48, 432, 3264, 9456, 21600, 39744, 66432, 105840, 147984, 220320]
            sage: f.coefficients([0,1])
            [1, -48]
            sage: f.coefficients([0,1,2,3])
            [1, -48, 432, 3264]
            sage: f.coefficients([2,3])
            [432, 3264]
            sage: g.coefficients(10)
            [168,
             -13608,
             210336,
             1805496,
             -22562064,
             -322437024,
             -2063087808,
             -9165872520,
             -32250917496,
             -96383477232]
            sage: g.coefficients([3, 7])
            [210336, -2063087808]
        """
