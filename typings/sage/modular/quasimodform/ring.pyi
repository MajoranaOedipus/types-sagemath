from .element import QuasiModularFormsElement as QuasiModularFormsElement
from sage.categories.graded_algebras import GradedAlgebras as GradedAlgebras
from sage.modular.arithgroup.congroup_generic import CongruenceSubgroupBase as CongruenceSubgroupBase
from sage.modular.modform.element import GradedModularFormElement as GradedModularFormElement, ModularFormElement as ModularFormElement
from sage.modular.modform.ring import ModularFormsRing as ModularFormsRing
from sage.modular.modform.space import ModularFormsSpace as ModularFormsSpace
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.power_series_poly import PowerSeries_poly as PowerSeries_poly
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class QuasiModularForms(Parent, UniqueRepresentation):
    """
    The graded ring of quasimodular forms for the full modular group
    `\\SL_2(\\ZZ)`, with coefficients in a ring.

    EXAMPLES::

        sage: QM = QuasiModularForms(1); QM
        Ring of Quasimodular Forms for Modular Group SL(2,Z) over Rational Field
        sage: QM.gens()
        (1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
         1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
         1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6))

    It is possible to access the weight 2 Eisenstein series::

        sage: QM.weight_2_eisenstein_series()
        1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)

    Currently, the only supported base ring is the rational numbers::

        sage: QuasiModularForms(1, GF(5))
        Traceback (most recent call last):
        ...
        NotImplementedError: base ring other than Q are not yet supported for quasimodular forms ring
    """
    Element = QuasiModularFormsElement
    def __init__(self, group: int = 1, base_ring=..., name: str = 'E2') -> None:
        """
        INPUT:

        - ``group`` -- (default: `\\SL_2(\\ZZ)`) a congruence subgroup of
          `\\SL_2(\\ZZ)`, or a positive integer `N` (interpreted as
          `\\Gamma_0(N)`)

        - ``base_ring`` -- a base ring (default: `\\QQ`); should be
          `\\QQ`, `\\ZZ`, or the integers mod `p` for some prime `p`

        - ``name`` -- string (default: ``'E2'``); a variable name corresponding to
          the weight 2 Eisenstein series

        TESTS:

            sage: M = QuasiModularForms(1)
            sage: M.group()
            Modular Group SL(2,Z)
            sage: M.base_ring()
            Rational Field
            sage: QuasiModularForms(Integers(5))
            Traceback (most recent call last):
            ...
            ValueError: Group (=Ring of integers modulo 5) should be a congruence subgroup

        ::

            sage: TestSuite(QuasiModularForms(1)).run()
            sage: TestSuite(QuasiModularForms(Gamma0(3))).run()
            sage: TestSuite(QuasiModularForms(Gamma1(3))).run()
        """
    def group(self):
        """
        Return the congruence subgroup attached to the given quasimodular forms
        ring.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.group()
            Modular Group SL(2,Z)
            sage: QM.group() is SL2Z
            True
            sage: QuasiModularForms(3).group()
            Congruence Subgroup Gamma0(3)
            sage: QuasiModularForms(Gamma1(5)).group()
            Congruence Subgroup Gamma1(5)
        """
    def modular_forms_subring(self):
        """
        Return the subring of modular forms of this ring of quasimodular forms.

        EXAMPLES::

            sage: QuasiModularForms(1).modular_forms_subring()
            Ring of Modular Forms for Modular Group SL(2,Z) over Rational Field
            sage: QuasiModularForms(5).modular_forms_subring()
            Ring of Modular Forms for Congruence Subgroup Gamma0(5) over Rational Field
        """
    def modular_forms_of_weight(self, weight):
        """
        Return the space of modular forms on this group of the given weight.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.modular_forms_of_weight(12)
            Modular Forms space of dimension 2 for Modular Group SL(2,Z) of weight 12 over Rational Field
            sage: QM = QuasiModularForms(Gamma1(3))
            sage: QM.modular_forms_of_weight(4)
            Modular Forms space of dimension 2 for Congruence Subgroup Gamma1(3) of weight 4 over Rational Field
        """
    def quasimodular_forms_of_weight(self, weight) -> None:
        """
        Return the space of quasimodular forms on this group of the given weight.

        INPUT:

        - ``weight`` -- integer

        OUTPUT: a quasimodular forms space of the given weight

        EXAMPLES::

            sage: QuasiModularForms(1).quasimodular_forms_of_weight(4)
            Traceback (most recent call last):
            ...
            NotImplementedError: spaces of quasimodular forms of fixed weight not yet implemented
        """
    def weight_2_eisenstein_series(self):
        """
        Return the weight 2 Eisenstein series.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: E2 = QM.weight_2_eisenstein_series(); E2
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: E2.parent()
            Ring of Quasimodular Forms for Modular Group SL(2,Z) over Rational Field
        """
    def gens(self) -> tuple:
        """
        Return a tuple of generators of the quasimodular forms ring.

        Note that the generators of the modular forms subring are the one given
        by the method :meth:`sage.modular.modform.ring.ModularFormsRing.gen_forms`

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.gens()
            (1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6))
            sage: QM.modular_forms_subring().gen_forms()
            [1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)]
            sage: QM = QuasiModularForms(5)
            sage: QM.gens()
            (1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
            1 + 6*q + 18*q^2 + 24*q^3 + 42*q^4 + 6*q^5 + O(q^6),
            1 + 240*q^5 + O(q^6),
            q + 10*q^3 + 28*q^4 + 35*q^5 + O(q^6))

        An alias of this method is ``generators``::

            sage: QuasiModularForms(1).generators()
            (1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6))
        """
    generators = gens
    def ngens(self):
        """
        Return the number of generators of the given graded quasimodular forms
        ring.

        EXAMPLES::

            sage: QuasiModularForms(1).ngens()
            3
        """
    def gen(self, n):
        """
        Return the `n`-th generator of the quasimodular forms ring.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.0
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: QM.1
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: QM.2
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)
            sage: QM = QuasiModularForms(5)
            sage: QM.0
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: QM.1
            1 + 6*q + 18*q^2 + 24*q^3 + 42*q^4 + 6*q^5 + O(q^6)
            sage: QM.2
            1 + 240*q^5 + O(q^6)
            sage: QM.3
            q + 10*q^3 + 28*q^4 + 35*q^5 + O(q^6)
            sage: QM.4
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
        """
    def zero(self):
        """
        Return the zero element of this ring.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.zero()
            0
            sage: QM.zero().is_zero()
            True
        """
    def one(self):
        """
        Return the one element of this ring.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.one()
            1
            sage: QM.one().is_one()
            True
        """
    def some_elements(self):
        """
        Return a list of generators of ``self``.

        EXAMPLES::

            sage: QuasiModularForms(1).some_elements()
            (1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6),
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6))
        """
    def polygen(self):
        """
        Return the generator of this quasimodular form space as a polynomial
        ring over the modular form subring.

        Note that this generator correspond to the weight-2 Eisenstein series.
        The default name of this generator is ``E2``.

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.polygen()
            E2
            sage: QuasiModularForms(1, name='X').polygen()
            X
            sage: QM.polygen().parent()
            Univariate Polynomial Ring in E2 over Ring of Modular Forms for Modular Group SL(2,Z) over Rational Field
        """
    def polynomial_ring(self, names=None):
        '''
        Return a multivariate polynomial ring of which the quasimodular forms
        ring is a quotient.

        In the case of the full modular group, this ring is `R[E_2, E_4, E_6]`
        where `E_2`, `E_4` and `E_6` have degrees 2, 4 and 6 respectively.

        INPUT:

        - ``names``-- string (default: ``None``); list or tuple of names
          (strings), or a comma separated string. Defines the names for the
          generators of the multivariate polynomial ring. The default names are
          of the following form:

          - ``E2`` denotes the weight 2 Eisenstein series;

          - ``Ek_i`` and ``Sk_i`` denote the `i`-th basis element of the weight
            `k` Eisenstein subspace and cuspidal subspace respectively;

          - If the level is one, the default names are ``E2``, ``E4`` and
            ``E6``;

          - In any other cases, we use the letters ``Fk``, ``Gk``, ``Hk``, ...,
            ``FFk``, ``FGk``, ... to denote any generator of weight `k`.

        OUTPUT: a multivariate polynomial ring in the variables ``names``

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: P = QM.polynomial_ring(); P
            Multivariate Polynomial Ring in E2, E4, E6 over Rational Field
            sage: P.inject_variables()
            Defining E2, E4, E6
            sage: E2.degree()
            2
            sage: E4.degree()
            4
            sage: E6.degree()
            6

        Example when the level is not one::

            sage: QM = QuasiModularForms(Gamma0(29))
            sage: P_29 = QM.polynomial_ring()
            sage: P_29
            Multivariate Polynomial Ring in E2, F2, S2_0, S2_1, E4_0, F4, G4, H4 over Rational Field
            sage: P_29.inject_variables()
            Defining E2, F2, S2_0, S2_1, E4_0, F4, G4, H4
            sage: F2.degree()
            2
            sage: E4_0.degree()
            4

        The name ``Sk_i`` stands for the `i`-th basis element of the cuspidal subspace of weight `k`::

            sage: F2 = QM.from_polynomial(S2_0)
            sage: F2.qexp(10)
            q - q^4 - q^5 - q^6 + 2*q^7 - 2*q^8 - 2*q^9 + O(q^10)
            sage: CuspForms(Gamma0(29), 2).0.qexp(10)
            q - q^4 - q^5 - q^6 + 2*q^7 - 2*q^8 - 2*q^9 + O(q^10)
            sage: F2 == CuspForms(Gamma0(29), 2).0
            True

        The name ``Ek_i`` stands for the `i`-th basis element of the Eisenstein subspace of weight `k`::

            sage: F4 = QM.from_polynomial(E4_0)
            sage: F4.qexp(30)
            1 + 240*q^29 + O(q^30)
            sage: EisensteinForms(Gamma0(29), 4).0.qexp(30)
            1 + 240*q^29 + O(q^30)
            sage: F4 == EisensteinForms(Gamma0(29), 4).0
            True

        One may also choose the name of the variables::

            sage: QM = QuasiModularForms(1)
            sage: QM.polynomial_ring(names="P, Q, R")
            Multivariate Polynomial Ring in P, Q, R over Rational Field
        '''
    def from_polynomial(self, polynomial):
        """
        Convert the given polynomial `P(x,\\ldots, y)` to the graded quasiform
        `P(g_0, \\ldots, g_n)` where the `g_i` are the generators given
        by :meth:`~sage.modular.quasimodform.ring.QuasiModularForms.gens`.

        INPUT:

        - ``polynomial`` -- a multivariate polynomial

        OUTPUT: the graded quasimodular forms `P(g_0, \\ldots, g_n)`

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: P.<x, y, z> = QQ[]
            sage: QM.from_polynomial(x)
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: QM.from_polynomial(x) == QM.0
            True
            sage: QM.from_polynomial(y) == QM.1
            True
            sage: QM.from_polynomial(z) == QM.2
            True
            sage: QM.from_polynomial(x^2 + y + x*z + 1)
            4 - 336*q - 2016*q^2 + 322368*q^3 + 3691392*q^4 + 21797280*q^5 + O(q^6)
            sage: QM = QuasiModularForms(Gamma0(2))
            sage: P = QM.polynomial_ring()
            sage: P.inject_variables()
            Defining E2, E2_0, E4_0
            sage: QM.from_polynomial(E2)
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 - 144*q^5 + O(q^6)
            sage: QM.from_polynomial(E2 + E4_0*E2_0) == QM.0 + QM.2*QM.1
            True

        Naturally, the number of variable must not exceed the number of generators::

            sage: P = PolynomialRing(QQ, 'F', 4)
            sage: P.inject_variables()
            Defining F0, F1, F2, F3
            sage: QM.from_polynomial(F0 + F1 + F2 + F3)
            Traceback (most recent call last):
            ...
            ValueError: the number of variables (4) of the given polynomial cannot exceed the number of generators (3) of the quasimodular forms ring


        TESTS::

            sage: QuasiModularForms(1).from_polynomial('x')
            Traceback (most recent call last):
            ...
            TypeError: the input must be a polynomial
        """
    def basis_of_weight(self, weight):
        """
        Return a basis of elements generating the subspace of the given
        weight.

        INPUT:

        - ``weight`` -- integer; the weight of the subspace

        OUTPUT: list of quasimodular forms of the given weight

        EXAMPLES::

            sage: QM = QuasiModularForms(1)
            sage: QM.basis_of_weight(12)
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6),
             1 + 65520/691*q + 134250480/691*q^2 + 11606736960/691*q^3 + 274945048560/691*q^4 + 3199218815520/691*q^5 + O(q^6),
             1 - 288*q - 129168*q^2 - 1927296*q^3 + 65152656*q^4 + 1535768640*q^5 + O(q^6),
             1 + 432*q + 39312*q^2 - 1711296*q^3 - 14159664*q^4 + 317412000*q^5 + O(q^6),
             1 - 576*q + 21168*q^2 + 308736*q^3 - 15034608*q^4 - 39208320*q^5 + O(q^6),
             1 + 144*q - 17712*q^2 + 524736*q^3 - 2279088*q^4 - 79760160*q^5 + O(q^6),
             1 - 144*q + 8208*q^2 - 225216*q^3 + 2634192*q^4 + 1488672*q^5 + O(q^6)]
            sage: QM = QuasiModularForms(Gamma1(3))
            sage: QM.basis_of_weight(3)
            [1 + 54*q^2 + 72*q^3 + 432*q^5 + O(q^6),
             q + 3*q^2 + 9*q^3 + 13*q^4 + 24*q^5 + O(q^6)]
            sage: QM.basis_of_weight(5)
            [1 - 90*q^2 - 240*q^3 - 3744*q^5 + O(q^6),
             q + 15*q^2 + 81*q^3 + 241*q^4 + 624*q^5 + O(q^6),
             1 - 24*q - 18*q^2 - 1320*q^3 - 5784*q^4 - 10080*q^5 + O(q^6),
             q - 21*q^2 - 135*q^3 - 515*q^4 - 1392*q^5 + O(q^6)]
        """
