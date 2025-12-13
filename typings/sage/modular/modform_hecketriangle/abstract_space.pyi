from .abstract_ring import FormsRing_abstract as FormsRing_abstract
from .element import FormsElement as FormsElement
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import FreeModuleElement as FreeModuleElement, vector as vector
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing_generic as PowerSeriesRing_generic
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import parent as parent

class FormsSpace_abstract(FormsRing_abstract):
    """
    Abstract (Hecke) forms space.

    This should never be called directly. Instead one should
    instantiate one of the derived classes of this class.
    """
    Element = FormsElement
    def __init__(self, group, base_ring, k, ep, n) -> None:
        """
        Abstract (Hecke) forms space.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``k`` -- the weight (default: `0`)

        - ``ep`` -- the epsilon (default: ``None``); if ``None``, then `k(n-2)`
          has to be divisible by `2` and ``ep=(-1)^(k*(n-2)/2)`` is used

        - ``base_ring`` -- the base_ring (default: `\\Z`)

        OUTPUT: the corresponding abstract (Hecke) forms space

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=5, base_ring=ZZ, k=6, ep=-1)
            sage: MF
            ModularForms(n=5, k=6, ep=-1) over Integer Ring
            sage: MF.group()
            Hecke triangle group for n = 5
            sage: MF.base_ring()
            Integer Ring
            sage: MF.weight()
            6
            sage: MF.ep()
            -1
            sage: MF.has_reduce_hom()
            True
            sage: MF.is_homogeneous()
            True
        """
    @cached_method
    def one(self):
        """
        Return the one element from the corresponding space of constant forms.

        .. NOTE:: The one element does not lie in ``self`` in general.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: MF = CuspForms(k=12)
            sage: MF.Delta()^0 == MF.one()
            True
            sage: (MF.Delta()^0).parent()
            ModularForms(n=3, k=0, ep=1) over Integer Ring
        """
    def is_ambient(self) -> bool:
        """
        Return whether ``self`` is an ambient space.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=12)
            sage: MF.is_ambient()
            True
            sage: MF.subspace([MF.gen(0)]).is_ambient()
            False
        """
    def ambient_space(self):
        """
        Return the ambient space of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=12)
            sage: MF.ambient_space()
            ModularForms(n=3, k=12, ep=1) over Integer Ring
            sage: MF.ambient_space() == MF
            True
            sage: subspace = MF.subspace([MF.gen(0)])
            sage: subspace
            Subspace of dimension 1 of ModularForms(n=3, k=12, ep=1) over Integer Ring
            sage: subspace.ambient_space() == MF
            True
        """
    def module(self):
        """
        Return the module associated to ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=12)
            sage: MF.module()
            Vector space of dimension 2 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: subspace = MF.subspace([MF.gen(0)])
            sage: subspace.module()
            Vector space of degree 2 and dimension 1 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            Basis matrix:
            [1 0]
        """
    def ambient_module(self):
        """
        Return the module associated to the ambient space of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=12)
            sage: MF.ambient_module()
            Vector space of dimension 2 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: MF.ambient_module() == MF.module()
            True
            sage: subspace = MF.subspace([MF.gen(0)])
            sage: subspace.ambient_module() == MF.module()
            True
        """
    def subspace(self, basis):
        """
        Return the subspace of ``self`` generated by ``basis``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=24)
            sage: MF.dimension()
            3
            sage: subspace = MF.subspace([MF.gen(0), MF.gen(1)])
            sage: subspace
            Subspace of dimension 2 of ModularForms(n=3, k=24, ep=1) over Integer Ring
        """
    def change_ring(self, new_base_ring):
        """
        Return the same space as ``self`` but over a new base ring ``new_base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CuspForms(n=5, k=24).change_ring(CC)
            CuspForms(n=5, k=24, ep=1) over Complex Field with 53 bits of precision
        """
    def construction(self):
        """
        Return a functor that constructs ``self`` (used by the coercion machinery).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms
            sage: QuasiModularForms(n=4, k=2, ep=1, base_ring=CC).construction()
            (QuasiModularFormsFunctor(n=4, k=2, ep=1),
             BaseFacade(Complex Field with 53 bits of precision))

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF=ModularForms(k=12)
            sage: MF.subspace([MF.gen(1)]).construction()
            (FormsSubSpaceFunctor with 1 generator for the ModularFormsFunctor(n=3, k=12, ep=1), BaseFacade(Integer Ring))
        """
    @cached_method
    def weight(self):
        """
        Return the weight of (elements of) ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms
            sage: QuasiModularForms(n=16, k=16/7, ep=-1).weight()
            16/7
        """
    @cached_method
    def ep(self):
        """
        Return the multiplier of (elements of) ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms
            sage: QuasiModularForms(n=16, k=16/7, ep=-1).ep()
            -1
        """
    @cached_method
    def contains_coeff_ring(self):
        """
        Return whether ``self`` contains its coefficient ring.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms
            sage: QuasiModularForms(k=0, ep=1, n=8).contains_coeff_ring()
            True
            sage: QuasiModularForms(k=0, ep=-1, n=8).contains_coeff_ring()
            False
        """
    def element_from_coordinates(self, vec):
        """
        If ``self`` has an associated free module, then return the element of ``self``
        corresponding to the given coordinate vector ``vec``. Otherwise raise an exception.

        INPUT:

        - ``vec`` -- a coordinate vector with respect to ``self.gens()``

        OUTPUT: an element of ``self`` corresponding to the coordinate vector ``vec``

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=24)
            sage: MF.dimension()
            3
            sage: el = MF.element_from_coordinates([1,1,1])
            sage: el
            1 + q + q^2 + 52611612*q^3 + 39019413208*q^4 + O(q^5)
            sage: el == MF.gen(0) + MF.gen(1) + MF.gen(2)
            True
            sage: el.parent() == MF
            True

            sage: subspace = MF.subspace([MF.gen(0), MF.gen(1)])
            sage: el = subspace.element_from_coordinates([1,1])
            sage: el
            1 + q + 52611660*q^3 + 39019412128*q^4 + O(q^5)
            sage: el == subspace.gen(0) + subspace.gen(1)
            True
            sage: el.parent() == subspace
            True
        """
    def element_from_ambient_coordinates(self, vec):
        """
        If ``self`` has an associated free module, then return the element of ``self``
        corresponding to the given ``vec``. Otherwise raise an exception.

        INPUT:

        - ``vec`` -- an element of ``self.module()`` or ``self.ambient_module()``

        OUTPUT: an element of ``self`` corresponding to ``vec``

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=24)
            sage: MF.dimension()
            3
            sage: el = MF.element_from_ambient_coordinates([1,1,1])
            sage: el == MF.element_from_coordinates([1,1,1])
            True
            sage: el.parent() == MF
            True

            sage: subspace = MF.subspace([MF.gen(0), MF.gen(1)])
            sage: el = subspace.element_from_ambient_coordinates([1,1,0])
            sage: el
            1 + q + 52611660*q^3 + 39019412128*q^4 + O(q^5)
            sage: el.parent() == subspace
            True
        """
    def homogeneous_part(self, k, ep):
        """
        Since ``self`` already is a homogeneous component return ``self``
        unless the degree differs in which case a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiMeromorphicModularForms
            sage: MF = QuasiMeromorphicModularForms(n=6, k=4)
            sage: MF == MF.homogeneous_part(4,1)
            True
            sage: MF.homogeneous_part(5,1)
            Traceback (most recent call last):
            ...
            ValueError: QuasiMeromorphicModularForms(n=6, k=4, ep=1) over Integer Ring already is homogeneous with degree (4, 1) != (5, 1)!
        """
    def weight_parameters(self):
        """
        Check whether ``self`` has a valid weight and multiplier.

        If not then an exception is raised. Otherwise the two weight
        parameters corresponding to the weight and multiplier of ``self``
        are returned.

        The weight parameters are e.g. used to calculate dimensions
        or precisions of Fourier expansion.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import MeromorphicModularForms
            sage: MF = MeromorphicModularForms(n=18, k=-7, ep=-1)
            sage: MF.weight_parameters()
            (-3, 17)
            sage: (MF._l1, MF._l2) == MF.weight_parameters()
            True
            sage: (k, ep) = (MF.weight(), MF.ep())
            sage: n = MF.hecke_n()
            sage: k == 4*(n*MF._l1 + MF._l2)/(n-2) + (1-ep)*n/(n-2)
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=5, k=12, ep=1)
            sage: MF.weight_parameters()
            (1, 4)
            sage: (MF._l1, MF._l2) == MF.weight_parameters()
            True
            sage: (k, ep) = (MF.weight(), MF.ep())
            sage: n = MF.hecke_n()
            sage: k == 4*(n*MF._l1 + MF._l2)/(n-2) + (1-ep)*n/(n-2)
            True
            sage: MF.dimension() == MF._l1 + 1
            True

            sage: MF = ModularForms(n=infinity, k=8, ep=1)
            sage: MF.weight_parameters()
            (2, 0)
            sage: MF.dimension() == MF._l1 + 1
            True
        """
    def aut_factor(self, gamma, t):
        """
        The automorphy factor of ``self``.

        INPUT:

        - ``gamma`` -- an element of the group of ``self``

        - ``t`` -- an element of the upper half plane

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=8, k=4, ep=1)
            sage: full_factor = lambda mat, t: (mat[1][0]*t+mat[1][1])**4
            sage: T = MF.group().T()
            sage: S = MF.group().S()
            sage: i = AlgebraicField()(i)
            sage: z = 1 + i/2

            sage: MF.aut_factor(S, z)
            3/2*I - 7/16
            sage: MF.aut_factor(-T^(-2), z)
            1
            sage: MF.aut_factor(MF.group().V(6), z)
            173.2640595631...? + 343.8133289126...?*I
            sage: MF.aut_factor(S, z) == full_factor(S, z)
            True
            sage: MF.aut_factor(T, z) == full_factor(T, z)
            True
            sage: MF.aut_factor(MF.group().V(6), z) == full_factor(MF.group().V(6), z)
            True

            sage: MF = ModularForms(n=7, k=14/5, ep=-1)
            sage: T = MF.group().T()
            sage: S = MF.group().S()

            sage: MF.aut_factor(S, z)
            1.3655215324256...? + 0.056805991182877...?*I
            sage: MF.aut_factor(-T^(-2), z)
            1
            sage: MF.aut_factor(S, z) == MF.ep() * (z/i)^MF.weight()
            True
            sage: MF.aut_factor(MF.group().V(6), z)
            13.23058830577...? + 15.71786610686...?*I
        """
    @cached_method
    def F_simple(self, order_1=...):
        """
        Return a (the most) simple normalized element of ``self``
        corresponding to the weight parameters ``l1=self._l1`` and
        ``l2=self._l2``. If the element does not lie in ``self`` the
        type of its parent is extended accordingly.

        The main part of the element is given by the ``(l1 - order_1)``-th power
        of ``f_inf``, up to a small holomorphic correction factor.

        INPUT:

        - ``order_1`` -- an integer (default: 0) denoting the desired order at
          ``-1`` in the case ``n = infinity``. If ``n != infinity`` the
          parameter is ignored.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: MF = WeakModularForms(n=18, k=-7, ep=-1)
            sage: MF.disp_prec(1)
            sage: MF.F_simple()
            q^-3 + 16/(81*d)*q^-2 - 4775/(104976*d^2)*q^-1 - 14300/(531441*d^3) + O(q)
            sage: MF.F_simple() == MF.f_inf()^MF._l1 * MF.f_rho()^MF._l2 * MF.f_i()
            True

            sage: from sage.modular.modform_hecketriangle.space import CuspForms, ModularForms
            sage: MF = CuspForms(n=5, k=2, ep=-1)
            sage: MF._l1
            -1
            sage: MF.F_simple().parent()
            WeakModularForms(n=5, k=2, ep=-1) over Integer Ring

            sage: MF = ModularForms(n=infinity, k=8, ep=1)
            sage: MF.F_simple().reduced_parent()
            ModularForms(n=+Infinity, k=8, ep=1) over Integer Ring
            sage: MF.F_simple()
            q^2 - 16*q^3 + 120*q^4 + O(q^5)
            sage: MF.F_simple(order_1=2)
            1 + 32*q + 480*q^2 + 4480*q^3 + 29152*q^4 + O(q^5)
        """
    def Faber_pol(self, m, order_1=..., fix_d: bool = False, d_num_prec=None):
        """
        Return the ``m``-th Faber polynomial of ``self``.

        Namely a polynomial ``P(q)`` such that ``P(J_inv)*F_simple(order_1)``
        has a Fourier expansion of the form ``q^m + O(q^(order_inf + 1))``.
        where ``order_inf = self._l1 - order_1`` and ``d^(order_inf - m)*P(q)``
        is a monic polynomial of degree ``order_inf - m``.

        If ``n=infinity`` a non-trivial order of ``-1`` can be specified through the
        parameter ``order_1`` (default: 0). Otherwise it is ignored.

        The Faber polynomials are e.g. used to construct a basis of weakly holomorphic
        forms and to recover such forms from their initial Fourier coefficients.

        INPUT:

        - ``m`` -- an integer ``m <= order_inf = self._l1 - order_1``

        - ``order_1`` -- the order at ``-1`` of F_simple (default: 0);
          this parameter is ignored if ``n != infinity``

        - ``fix_d`` -- if ``False`` (default) a formal parameter is used for
          ``d``. If ``True`` then the numerical value of ``d`` is used (resp.
          an exact value if the group is arithmetic). Otherwise the given
          value is used for ``d``.

        - ``d_num_prec`` -- the precision to be used if a numerical value for
          ``d`` is substituted (default: ``None``), otherwise the default
          numerical precision of ``self.parent()`` is used

        OUTPUT: the corresponding Faber polynomial ``P(q)``

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: MF = WeakModularForms(n=5, k=62/3, ep=-1)
            sage: MF.weight_parameters()
            (2, 3)

            sage: MF.Faber_pol(2)
            1
            sage: MF.Faber_pol(1)
            1/d*q - 19/(100*d)
            sage: MF.Faber_pol(0)
            1/d^2*q^2 - 117/(200*d^2)*q + 9113/(320000*d^2)
            sage: MF.Faber_pol(-2)
            1/d^4*q^4 - 11/(8*d^4)*q^3 + 41013/(80000*d^4)*q^2 - 2251291/(48000000*d^4)*q + 1974089431/(4915200000000*d^4)
            sage: (MF.Faber_pol(2)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2)
            q^2 - 41/(200*d)*q^3 + O(q^4)
            sage: (MF.Faber_pol(1)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1)
            q + O(q^3)
            sage: (MF.Faber_pol(0)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1)
            1 + O(q^3)
            sage: (MF.Faber_pol(-2)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1)
            q^-2 + O(q^3)

            sage: MF.Faber_pol(2, fix_d=1)
            1
            sage: MF.Faber_pol(1, fix_d=1)
            q - 19/100
            sage: MF.Faber_pol(-2, fix_d=1)
            q^4 - 11/8*q^3 + 41013/80000*q^2 - 2251291/48000000*q + 1974089431/4915200000000
            sage: (MF.Faber_pol(2, fix_d=1)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=1)
            q^2 - 41/200*q^3 + O(q^4)
            sage: (MF.Faber_pol(-2)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1, fix_d=1)
            q^-2 + O(q^3)

            sage: MF = WeakModularForms(n=4, k=-2, ep=1)
            sage: MF.weight_parameters()
            (-1, 3)

            sage: MF.Faber_pol(-1)
            1
            sage: MF.Faber_pol(-2, fix_d=True)
            256*q - 184
            sage: MF.Faber_pol(-3, fix_d=True)
            65536*q^2 - 73728*q + 14364
            sage: (MF.Faber_pol(-1, fix_d=True)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=True)
            q^-1 + 80 + O(q)
            sage: (MF.Faber_pol(-2, fix_d=True)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=True)
            q^-2 + 400 + O(q)
            sage: (MF.Faber_pol(-3)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=True)
            q^-3 + 2240 + O(q)

            sage: MF = WeakModularForms(n=infinity, k=14, ep=-1)
            sage: MF.Faber_pol(3)
            1
            sage: MF.Faber_pol(2)
            1/d*q + 3/(8*d)
            sage: MF.Faber_pol(1)
            1/d^2*q^2 + 75/(1024*d^2)
            sage: MF.Faber_pol(0)
            1/d^3*q^3 - 3/(8*d^3)*q^2 + 3/(512*d^3)*q + 41/(4096*d^3)
            sage: MF.Faber_pol(-1)
            1/d^4*q^4 - 3/(4*d^4)*q^3 + 81/(1024*d^4)*q^2 + 9075/(8388608*d^4)
            sage: (MF.Faber_pol(-1)(MF.J_inv())*MF.F_simple()).q_expansion(prec=MF._l1 + 1)
            q^-1 + O(q^4)

            sage: MF.Faber_pol(3, order_1=-1)
            1/d*q + 3/(4*d)
            sage: MF.Faber_pol(1, order_1=2)
            1
            sage: MF.Faber_pol(0, order_1=2)
            1/d*q - 3/(8*d)
            sage: MF.Faber_pol(-1, order_1=2)
            1/d^2*q^2 - 3/(4*d^2)*q + 81/(1024*d^2)
            sage: (MF.Faber_pol(-1, order_1=2)(MF.J_inv())*MF.F_simple(order_1=2)).q_expansion(prec=MF._l1 + 1)
            q^-1 - 9075/(8388608*d^4)*q^3 + O(q^4)
        """
    def faber_pol(self, m, order_1=..., fix_d: bool = False, d_num_prec=None):
        """
        If ``n=infinity`` a non-trivial order of ``-1`` can be specified through the
        parameter ``order_1`` (default: 0). Otherwise it is ignored.
        Return the `m`-th Faber polynomial of ``self``
        with a different normalization based on ``j_inv``
        instead of ``J_inv``.

        Namely a polynomial ``p(q)`` such that ``p(j_inv)*F_simple()``
        has a Fourier expansion of the form ``q^m + O(q^(order_inf + 1))``.
        where ``order_inf = self._l1 - order_1`` and ``p(q)`` is a
        monic polynomial of degree ``order_inf - m``.

        If ``n=infinity`` a non-trivial order of ``-1`` can be specified through the
        parameter ``order_1`` (default: 0). Otherwise it is ignored.

        The relation to ``Faber_pol`` is: ``faber_pol(q) = Faber_pol(d*q)``.

        INPUT:

        - ``m`` -- integer; ``m <= self._l1 - order_1``

        - ``order_1`` -- the order at ``-1`` of ``F_simple`` (default: 0);
          this parameter is ignored if ``n != infinity``

        - ``fix_d`` -- if ``False`` (default) a formal parameter is used for
          ``d``. If ``True`` then the numerical value of ``d`` is used (resp.
          an exact value if the group is arithmetic). Otherwise the given value
          is used for ``d``.

        - ``d_num_prec`` -- the precision to be used if a numerical value for
          ``d`` is substituted (default: ``None``), otherwise the default
          numerical precision of ``self.parent()`` is used

        OUTPUT: the corresponding Faber polynomial ``p(q)``

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: MF = WeakModularForms(n=5, k=62/3, ep=-1)
            sage: MF.weight_parameters()
            (2, 3)

            sage: MF.faber_pol(2)
            1
            sage: MF.faber_pol(1)
            q - 19/(100*d)
            sage: MF.faber_pol(0)
            q^2 - 117/(200*d)*q + 9113/(320000*d^2)
            sage: MF.faber_pol(-2)
            q^4 - 11/(8*d)*q^3 + 41013/(80000*d^2)*q^2 - 2251291/(48000000*d^3)*q + 1974089431/(4915200000000*d^4)
            sage: (MF.faber_pol(2)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2)
            q^2 - 41/(200*d)*q^3 + O(q^4)
            sage: (MF.faber_pol(1)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1)
            q + O(q^3)
            sage: (MF.faber_pol(0)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1)
            1 + O(q^3)
            sage: (MF.faber_pol(-2)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+1)
            q^-2 + O(q^3)

            sage: MF = WeakModularForms(n=4, k=-2, ep=1)
            sage: MF.weight_parameters()
            (-1, 3)

            sage: MF.faber_pol(-1)
            1
            sage: MF.faber_pol(-2, fix_d=True)
            q - 184
            sage: MF.faber_pol(-3, fix_d=True)
            q^2 - 288*q + 14364
            sage: (MF.faber_pol(-1, fix_d=True)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=True)
            q^-1 + 80 + O(q)
            sage: (MF.faber_pol(-2, fix_d=True)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=True)
            q^-2 + 400 + O(q)
            sage: (MF.faber_pol(-3)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1+2, fix_d=True)
            q^-3 + 2240 + O(q)

            sage: MF = WeakModularForms(n=infinity, k=14, ep=-1)
            sage: MF.faber_pol(3)
            1
            sage: MF.faber_pol(2)
            q + 3/(8*d)
            sage: MF.faber_pol(1)
            q^2 + 75/(1024*d^2)
            sage: MF.faber_pol(0)
            q^3 - 3/(8*d)*q^2 + 3/(512*d^2)*q + 41/(4096*d^3)
            sage: MF.faber_pol(-1)
            q^4 - 3/(4*d)*q^3 + 81/(1024*d^2)*q^2 + 9075/(8388608*d^4)
            sage: (MF.faber_pol(-1)(MF.j_inv())*MF.F_simple()).q_expansion(prec=MF._l1 + 1)
            q^-1 + O(q^4)

            sage: MF.faber_pol(3, order_1=-1)
            q + 3/(4*d)
            sage: MF.faber_pol(1, order_1=2)
            1
            sage: MF.faber_pol(0, order_1=2)
            q - 3/(8*d)
            sage: MF.faber_pol(-1, order_1=2)
            q^2 - 3/(4*d)*q + 81/(1024*d^2)
            sage: (MF.faber_pol(-1, order_1=2)(MF.j_inv())*MF.F_simple(order_1=2)).q_expansion(prec=MF._l1 + 1)
            q^-1 - 9075/(8388608*d^4)*q^3 + O(q^4)
        """
    def F_basis_pol(self, m, order_1=...):
        """
        Return a polynomial corresponding to the basis element of
        the corresponding space of weakly holomorphic forms of
        the same degree as ``self``. The basis element is determined
        by the property that the Fourier expansion is of the form
        ``q^m + O(q^(order_inf + 1))``, where ``order_inf = self._l1 - order_1``.

        If ``n=infinity`` a non-trivial order of ``-1`` can be specified through
        the parameter ``order_1`` (default: 0). Otherwise it is ignored.

        INPUT:

        - ``m`` -- integer; ``m <= self._l1``

        - ``order_1`` -- the order at ``-1`` of ``F_simple`` (default: 0);
          this parameter is ignored if ``n != infinity``

        OUTPUT:

        A polynomial in ``x,y,z,d``, corresponding to ``f_rho, f_i, E2``
        and the (possibly) transcendental parameter ``d``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: MF = WeakModularForms(n=5, k=62/3, ep=-1)
            sage: MF.weight_parameters()
            (2, 3)

            sage: MF.F_basis_pol(2)
            x^13*y*d^2 - 2*x^8*y^3*d^2 + x^3*y^5*d^2
            sage: MF.F_basis_pol(1) * 100
            81*x^13*y*d - 62*x^8*y^3*d - 19*x^3*y^5*d
            sage: MF.F_basis_pol(0)
            (141913*x^13*y + 168974*x^8*y^3 + 9113*x^3*y^5)/320000

            sage: MF(MF.F_basis_pol(2)).q_expansion(prec=MF._l1+2)
            q^2 - 41/(200*d)*q^3 + O(q^4)
            sage: MF(MF.F_basis_pol(1)).q_expansion(prec=MF._l1+1)
            q + O(q^3)
            sage: MF(MF.F_basis_pol(0)).q_expansion(prec=MF._l1+1)
            1 + O(q^3)
            sage: MF(MF.F_basis_pol(-2)).q_expansion(prec=MF._l1+1)
            q^-2 + O(q^3)
            sage: MF(MF.F_basis_pol(-2)).parent()
            WeakModularForms(n=5, k=62/3, ep=-1) over Integer Ring

            sage: MF = WeakModularForms(n=4, k=-2, ep=1)
            sage: MF.weight_parameters()
            (-1, 3)

            sage: MF.F_basis_pol(-1)
            x^3/(x^4*d - y^2*d)
            sage: MF.F_basis_pol(-2)
            (9*x^7 + 23*x^3*y^2)/(32*x^8*d^2 - 64*x^4*y^2*d^2 + 32*y^4*d^2)

            sage: MF(MF.F_basis_pol(-1)).q_expansion(prec=MF._l1+2)
            q^-1 + 5/(16*d) + O(q)
            sage: MF(MF.F_basis_pol(-2)).q_expansion(prec=MF._l1+2)
            q^-2 + 25/(4096*d^2) + O(q)

            sage: MF = WeakModularForms(n=infinity, k=14, ep=-1)
            sage: MF.F_basis_pol(3)
            -y^7*d^3 + 3*x*y^5*d^3 - 3*x^2*y^3*d^3 + x^3*y*d^3
            sage: MF.F_basis_pol(2)
            (3*y^7*d^2 - 17*x*y^5*d^2 + 25*x^2*y^3*d^2 - 11*x^3*y*d^2)/(-8)
            sage: MF.F_basis_pol(1)
            (-75*y^7*d + 225*x*y^5*d - 1249*x^2*y^3*d + 1099*x^3*y*d)/1024
            sage: MF.F_basis_pol(0)
            (41*y^7 - 147*x*y^5 - 1365*x^2*y^3 - 2625*x^3*y)/(-4096)
            sage: MF.F_basis_pol(-1)
            (-9075*y^9 + 36300*x*y^7 - 718002*x^2*y^5 - 4928052*x^3*y^3 - 2769779*x^4*y)/(8388608*y^2*d - 8388608*x*d)

            sage: MF.F_basis_pol(3, order_1=-1)
            (-3*y^9*d^3 + 16*x*y^7*d^3 - 30*x^2*y^5*d^3 + 24*x^3*y^3*d^3 - 7*x^4*y*d^3)/(-4*x)
            sage: MF.F_basis_pol(1, order_1=2)
            -x^2*y^3*d + x^3*y*d
            sage: MF.F_basis_pol(0, order_1=2)
            (-3*x^2*y^3 - 5*x^3*y)/(-8)
            sage: MF.F_basis_pol(-1, order_1=2)
            (-81*x^2*y^5 - 606*x^3*y^3 - 337*x^4*y)/(1024*y^2*d - 1024*x*d)
        """
    def F_basis(self, m, order_1=...):
        """
        Return a weakly holomorphic element of ``self``
        (extended if necessarily) determined by the property that
        the Fourier expansion is of the form is of the form
        ``q^m + O(q^(order_inf + 1))``, where ``order_inf = self._l1 - order_1``.

        In particular for all ``m <= order_inf`` these elements form
        a basis of the space of weakly holomorphic modular forms
        of the corresponding degree in case ``n!=infinity``.

        If ``n=infinity`` a non-trivial order of ``-1`` can be specified through
        the parameter ``order_1`` (default: 0). Otherwise it is ignored.

        INPUT:

        - ``m`` -- integer; ``m <= self._l1``

        - ``order_1`` -- the order at ``-1`` of ``F_simple`` (default: 0);
          this parameter is ignored if ``n != infinity``

        OUTPUT:

        The corresponding element in (possibly an extension of) ``self``.
        Note that the order at ``-1`` of the resulting element may be
        bigger than ``order_1`` (rare).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, CuspForms
            sage: MF = WeakModularForms(n=5, k=62/3, ep=-1)
            sage: MF.disp_prec(MF._l1+2)
            sage: MF.weight_parameters()
            (2, 3)

            sage: MF.F_basis(2)
            q^2 - 41/(200*d)*q^3 + O(q^4)
            sage: MF.F_basis(1)
            q - 13071/(640000*d^2)*q^3 + O(q^4)
            sage: MF.F_basis(0)
            1 - 277043/(192000000*d^3)*q^3 + O(q^4)
            sage: MF.F_basis(-2)
            q^-2 - 162727620113/(40960000000000000*d^5)*q^3 + O(q^4)
            sage: MF.F_basis(-2).parent() == MF
            True

            sage: MF = CuspForms(n=4, k=-2, ep=1)
            sage: MF.weight_parameters()
            (-1, 3)

            sage: MF.F_basis(-1).parent()
            WeakModularForms(n=4, k=-2, ep=1) over Integer Ring
            sage: MF.F_basis(-1).parent().disp_prec(MF._l1+2)
            sage: MF.F_basis(-1)
            q^-1 + 80 + O(q)
            sage: MF.F_basis(-2)
            q^-2 + 400 + O(q)

            sage: MF = WeakModularForms(n=infinity, k=14, ep=-1)
            sage: MF.F_basis(3)
            q^3 - 48*q^4 + O(q^5)
            sage: MF.F_basis(2)
            q^2 - 1152*q^4 + O(q^5)
            sage: MF.F_basis(1)
            q - 18496*q^4 + O(q^5)
            sage: MF.F_basis(0)
            1 - 224280*q^4 + O(q^5)
            sage: MF.F_basis(-1)
            q^-1 - 2198304*q^4 + O(q^5)

            sage: MF.F_basis(3, order_1=-1)
            q^3 + O(q^5)
            sage: MF.F_basis(1, order_1=2)
            q - 300*q^3 - 4096*q^4 + O(q^5)
            sage: MF.F_basis(0, order_1=2)
            1 - 24*q^2 - 2048*q^3 - 98328*q^4 + O(q^5)
            sage: MF.F_basis(-1, order_1=2)
            q^-1 - 18150*q^3 - 1327104*q^4 + O(q^5)
        """
    def quasi_part_gens(self, r=None, min_exp: int = 0, max_exp=..., order_1=...) -> tuple:
        """
        Return a basis in ``self`` of the subspace of (quasi) weakly
        holomorphic forms which satisfy the specified properties on
        the quasi parts and the initial Fourier coefficient.

        INPUT:

        - ``r`` -- an integer or ``None`` (default), indicating the desired
          power of ``E2``; if ``r`` is ``None`` then all possible powers
          (``r``) are chosen

        - ``min_exp`` -- integer (default: 0); a lower bound for the first
          non-trivial Fourier coefficient of the generators

        - ``max_exp`` -- integer or ``infinity`` (default) giving an upper
          bound for the first non-trivial Fourier coefficient of the
          generators.  If ``max_exp==infinity`` then no upper bound is assumed.

        - ``order_1`` -- a lower bound for the order at ``-1`` of all quasi
          parts of the basis elements (default: 0). If ``n!=infinity`` this
          parameter is ignored.

        OUTPUT:

        A basis in ``self`` of the subspace of forms which are modular
        after dividing by ``E2^r`` and which have a Fourier expansion
        of the form ``q^m + O(q^(m+1))`` with ``min_exp <= m <=
        max_exp`` for each quasi part (and at least the specified
        order at ``-1`` in case ``n=infinity``). Note that linear
        combinations of forms/quasi parts maybe have a higher order at
        infinity than ``max_exp``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiWeakModularForms
            sage: QF = QuasiWeakModularForms(n=8, k=10/3, ep=-1)
            sage: QF.default_prec(1)
            sage: QF.quasi_part_gens(min_exp=-1)
            (q^-1 + O(q), 1 + O(q), q^-1 - 9/(128*d) + O(q),
             1 + O(q), q^-1 - 19/(64*d) + O(q), q^-1 + 1/(64*d) + O(q))

            sage: QF.quasi_part_gens(min_exp=-1, max_exp=-1)
            (q^-1 + O(q), q^-1 - 9/(128*d) + O(q),
             q^-1 - 19/(64*d) + O(q), q^-1 + 1/(64*d) + O(q))
            sage: QF.quasi_part_gens(min_exp=-2, r=1)
            (q^-2 - 9/(128*d)*q^-1 - 261/(131072*d^2) + O(q),
             q^-1 - 9/(128*d) + O(q), 1 + O(q))

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=36)
            sage: MF.quasi_part_gens(min_exp=2)
            (q^2 + 194184*q^4 + O(q^5), q^3 - 72*q^4 + O(q^5))

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms
            sage: MF = QuasiModularForms(n=5, k=6, ep=-1)
            sage: MF.default_prec(2)
            sage: MF.dimension()
            3
            sage: MF.quasi_part_gens(r=0)
            (1 - 37/(200*d)*q + O(q^2),)
            sage: MF.quasi_part_gens(r=0)[0] == MF.E6()
            True
            sage: MF.quasi_part_gens(r=1)
            (1 + 33/(200*d)*q + O(q^2),)
            sage: MF.quasi_part_gens(r=1)[0] == MF.E2()*MF.E4()
            True
            sage: MF.quasi_part_gens(r=2)
            ()
            sage: MF.quasi_part_gens(r=3)
            (1 - 27/(200*d)*q + O(q^2),)
            sage: MF.quasi_part_gens(r=3)[0] == MF.E2()^3
            True

            sage: from sage.modular.modform_hecketriangle.space import QuasiCuspForms, CuspForms
            sage: MF = QuasiCuspForms(n=5, k=18, ep=-1)
            sage: MF.default_prec(4)
            sage: MF.dimension()
            8
            sage: MF.quasi_part_gens(r=0)
            (q - 34743/(640000*d^2)*q^3 + O(q^4), q^2 - 69/(200*d)*q^3 + O(q^4))
            sage: MF.quasi_part_gens(r=1)
            (q - 9/(200*d)*q^2 + 37633/(640000*d^2)*q^3 + O(q^4),
             q^2 + 1/(200*d)*q^3 + O(q^4))
            sage: MF.quasi_part_gens(r=2)
            (q - 1/(4*d)*q^2 - 24903/(640000*d^2)*q^3 + O(q^4),)
            sage: MF.quasi_part_gens(r=3)
            (q + 1/(10*d)*q^2 - 7263/(640000*d^2)*q^3 + O(q^4),)
            sage: MF.quasi_part_gens(r=4)
            (q - 11/(20*d)*q^2 + 53577/(640000*d^2)*q^3 + O(q^4),)
            sage: MF.quasi_part_gens(r=5)
            (q - 1/(5*d)*q^2 + 4017/(640000*d^2)*q^3 + O(q^4),)

            sage: MF.quasi_part_gens(r=1)[0] == MF.E2() * CuspForms(n=5, k=16, ep=1).gen(0)
            True
            sage: MF.quasi_part_gens(r=1)[1] == MF.E2() * CuspForms(n=5, k=16, ep=1).gen(1)
            True
            sage: MF.quasi_part_gens(r=3)[0] == MF.E2()^3 * MF.Delta()
            True

            sage: MF = QuasiCuspForms(n=infinity, k=18, ep=-1)
            sage: MF.quasi_part_gens(r=1, min_exp=-2) == MF.quasi_part_gens(r=1, min_exp=1)
            True
            sage: MF.quasi_part_gens(r=1)
            (q - 8*q^2 - 8*q^3 + 5952*q^4 + O(q^5),
             q^2 - 8*q^3 + 208*q^4 + O(q^5),
             q^3 - 16*q^4 + O(q^5))

            sage: MF = QuasiWeakModularForms(n=infinity, k=4, ep=1)
            sage: MF.quasi_part_gens(r=2, min_exp=2, order_1=-2)[0] == MF.E2()^2 * MF.E4()^(-2) * MF.f_inf()^2
            True
            sage: [v.order_at(-1) for v in MF.quasi_part_gens(r=0, min_exp=2, order_1=-2)]
            [-2, -2]
        """
    def quasi_part_dimension(self, r=None, min_exp: int = 0, max_exp=..., order_1=...):
        """
        Return the dimension of the subspace of ``self`` generated by
        ``self.quasi_part_gens(r, min_exp, max_exp, order_1)``.

        See :meth:`quasi_part_gens` for more details.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms, QuasiCuspForms, QuasiWeakModularForms
            sage: MF = QuasiModularForms(n=5, k=6, ep=-1)
            sage: [v.as_ring_element() for v in MF.gens()]
            [f_rho^2*f_i, f_rho^3*E2, E2^3]
            sage: MF.dimension()
            3
            sage: MF.quasi_part_dimension(r=0)
            1
            sage: MF.quasi_part_dimension(r=1)
            1
            sage: MF.quasi_part_dimension(r=2)
            0
            sage: MF.quasi_part_dimension(r=3)
            1

            sage: MF = QuasiCuspForms(n=5, k=18, ep=-1)
            sage: MF.dimension()
            8
            sage: MF.quasi_part_dimension(r=0)
            2
            sage: MF.quasi_part_dimension(r=1)
            2
            sage: MF.quasi_part_dimension(r=2)
            1
            sage: MF.quasi_part_dimension(r=3)
            1
            sage: MF.quasi_part_dimension(r=4)
            1
            sage: MF.quasi_part_dimension(r=5)
            1
            sage: MF.quasi_part_dimension(min_exp=2, max_exp=2)
            2

            sage: MF = QuasiCuspForms(n=infinity, k=18, ep=-1)
            sage: MF.quasi_part_dimension(r=1, min_exp=-2)
            3
            sage: MF.quasi_part_dimension()
            12
            sage: MF.quasi_part_dimension(order_1=3)
            2

            sage: MF = QuasiWeakModularForms(n=infinity, k=4, ep=1)
            sage: MF.quasi_part_dimension(min_exp=2, order_1=-2)
            4
            sage: [v.order_at(-1) for v in MF.quasi_part_gens(r=0, min_exp=2, order_1=-2)]
            [-2, -2]
        """
    def construct_form(self, laurent_series, order_1=..., check: bool = True, rationalize: bool = False):
        '''
        Try to construct an element of ``self`` with the given Fourier
        expansion. The assumption is made that the specified Fourier
        expansion corresponds to a weakly holomorphic modular form.

        If the precision is too low to determine the
        element an exception is raised.

        INPUT:

        - ``laurent_series`` -- a Laurent or Power series

        - ``order_1`` -- a lower bound for the order at ``-1`` of the form
          (default: 0). If ``n!=infinity`` this parameter is ignored.

        - ``check`` -- if ``True`` (default) then the series expansion of the
          constructed form is compared against the given series

        - ``rationalize`` -- if ``True`` (default: ``False``) then the series
          is "rationalized" beforehand. Note that in non-exact or
          non-arithmetic cases this is experimental and extremely unreliable!

        OUTPUT:

        If possible: An element of ``self`` with the same initial
        Fourier expansion as ``laurent_series``.

        Note: For modular spaces it is also possible to call
        ``self(laurent_series)`` instead.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: Delta = CuspForms(k=12).Delta()
            sage: qexp = Delta.q_expansion(prec=2)
            sage: qexp.parent()
            Power Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: qexp
            q + O(q^2)
            sage: CuspForms(k=12).construct_form(qexp) == Delta
            True

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: J_inv = WeakModularForms(n=7).J_inv()
            sage: qexp2 = J_inv.q_expansion(prec=1)
            sage: qexp2.parent()
            Laurent Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: qexp2
            d*q^-1 + 151/392 + O(q)
            sage: WeakModularForms(n=7).construct_form(qexp2) == J_inv
            True

            sage: MF = WeakModularForms(n=5, k=62/3, ep=-1)
            sage: MF.default_prec(MF._l1+1)
            sage: d = MF.get_d()
            sage: MF.weight_parameters()
            (2, 3)
            sage: el2 = d*MF.F_basis(2) + 2*MF.F_basis(1) + MF.F_basis(-2)
            sage: qexp2 = el2.q_expansion()
            sage: qexp2.parent()
            Laurent Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: qexp2
            q^-2 + 2*q + d*q^2 + O(q^3)
            sage: WeakModularForms(n=5, k=62/3, ep=-1).construct_form(qexp2) == el2
            True

            sage: MF = WeakModularForms(n=infinity, k=-2, ep=-1)
            sage: el3 = MF.f_i()/MF.f_inf() + MF.f_i()*MF.f_inf()/MF.E4()^2
            sage: MF.quasi_part_dimension(min_exp=-1, order_1=-2)
            3
            sage: prec = MF._l1 + 3
            sage: qexp3 = el3.q_expansion(prec)
            sage: qexp3
            q^-1 - 1/(4*d) + ((1024*d^2 - 33)/(1024*d^2))*q + O(q^2)
            sage: MF.construct_form(qexp3, order_1=-2) == el3
            True
            sage: MF.construct_form(el3.q_expansion(prec + 1), order_1=-3) == el3
            True

            sage: WF = WeakModularForms(n=14)
            sage: qexp = WF.J_inv().q_expansion_fixed_d(d_num_prec=1000)
            sage: qexp.parent()
            Laurent Series Ring in q over Real Field with 1000 bits of precision
            sage: WF.construct_form(qexp, rationalize=True) == WF.J_inv()
            doctest:...: UserWarning: Using an experimental rationalization of coefficients, please check the result for correctness!
            True
        '''
    def required_laurent_prec(self, min_exp: int = 0, order_1=...):
        """
        Return an upper bound for the required precision for Laurent series to
        uniquely determine a corresponding (quasi) form in ``self`` with the given
        lower bound ``min_exp`` for the order at infinity (for each quasi part).

        .. NOTE::

            For ``n=infinity`` only the holomorphic case (``min_exp >= 0``)
            is supported (in particular a nonnegative order at ``-1`` is assumed).

        INPUT:

        - ``min_exp`` -- integer (default: 0); namely the lower bound for the
          order at infinity resp. the exponent of the Laurent series

        - ``order_1`` -- a lower bound for the order at ``-1`` for all quasi
          parts (default: 0). If ``n!=infinity`` this parameter is ignored.

        OUTPUT:

        An integer, namely an upper bound for the number of required
        Laurent coefficients.  The bound should be precise or at least
        pretty sharp.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiWeakModularForms, ModularForms, QuasiModularForms
            sage: QF = QuasiWeakModularForms(n=8, k=10/3, ep=-1)
            sage: QF.required_laurent_prec(min_exp=-1)
            5

            sage: MF = ModularForms(k=36)
            sage: MF.required_laurent_prec(min_exp=2)
            4

            sage: QuasiModularForms(k=2).required_laurent_prec()
            1

            sage: QuasiWeakModularForms(n=infinity, k=2, ep=-1).required_laurent_prec(order_1=-1)
            6
        """
    def construct_quasi_form(self, laurent_series, order_1=..., check: bool = True, rationalize: bool = False):
        '''
        Try to construct an element of ``self`` with the given Fourier
        expansion. The assumption is made that the specified Fourier
        expansion corresponds to a weakly holomorphic quasi modular form.

        If the precision is too low to determine the
        element an exception is raised.

        INPUT:

        - ``laurent_series`` -- a Laurent or Power series

        - ``order_1`` -- a lower bound for the order at ``-1`` for all quasi
          parts of the form (default: 0). If ``n!=infinity`` this parameter is
          ignored.

        - ``check`` -- if ``True`` (default) then the series expansion of the
          constructed form is compared against the given (rationalized) series.

        - ``rationalize`` -- if ``True`` (default: ``False``) then the series
          is "rationalized" beforehand. Note that in non-exact or
          non-arithmetic cases this is experimental and extremely unreliable!

        OUTPUT:

        If possible: An element of ``self`` with the same initial
        Fourier expansion as ``laurent_series``.

        Note: For non modular spaces it is also possible to call
        ``self(laurent_series)`` instead. Also note that this function works
        much faster if a corresponding (cached) ``q_basis`` is available.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiWeakModularForms, ModularForms, QuasiModularForms, QuasiCuspForms
            sage: QF = QuasiWeakModularForms(n=8, k=10/3, ep=-1)
            sage: el = QF.quasi_part_gens(min_exp=-1)[4]
            sage: prec = QF.required_laurent_prec(min_exp=-1)
            sage: prec
            5
            sage: qexp = el.q_expansion(prec=prec)
            sage: qexp
            q^-1 - 19/(64*d) - 7497/(262144*d^2)*q + 15889/(8388608*d^3)*q^2 + 543834047/(1649267441664*d^4)*q^3 + 711869853/(43980465111040*d^5)*q^4 + O(q^5)
            sage: qexp.parent()
            Laurent Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: constructed_el = QF.construct_quasi_form(qexp)
            sage: constructed_el.parent()
            QuasiWeakModularForms(n=8, k=10/3, ep=-1) over Integer Ring
            sage: el == constructed_el
            True

        If a q_basis is available the construction uses a different algorithm which we also check::

            sage: basis = QF.q_basis(min_exp=-1)
            sage: QF(qexp) == constructed_el
            True

            sage: MF = ModularForms(k=36)
            sage: el2 = MF.quasi_part_gens(min_exp=2)[1]
            sage: prec = MF.required_laurent_prec(min_exp=2)
            sage: prec
            4
            sage: qexp2 = el2.q_expansion(prec=prec + 1)
            sage: qexp2
            q^3 - 1/(24*d)*q^4 + O(q^5)
            sage: qexp2.parent()
            Power Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: constructed_el2 = MF.construct_quasi_form(qexp2)
            sage: constructed_el2.parent()
            ModularForms(n=3, k=36, ep=1) over Integer Ring
            sage: el2 == constructed_el2
            True

            sage: QF = QuasiModularForms(k=2)
            sage: q = QF.get_q()
            sage: qexp3 = 1 + O(q)
            sage: QF(qexp3)
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 + O(q^5)
            sage: QF(qexp3) == QF.E2()
            True

            sage: QF = QuasiWeakModularForms(n=infinity, k=2, ep=-1)
            sage: el4 = QF.f_i() + QF.f_i()^3/QF.E4()
            sage: prec = QF.required_laurent_prec(order_1=-1)
            sage: qexp4 = el4.q_expansion(prec=prec)
            sage: qexp4
            2 - 7/(4*d)*q + 195/(256*d^2)*q^2 - 903/(4096*d^3)*q^3 + 41987/(1048576*d^4)*q^4 - 181269/(33554432*d^5)*q^5 + O(q^6)
            sage: QF.construct_quasi_form(qexp4, check=False) == el4
            False
            sage: QF.construct_quasi_form(qexp4, order_1=-1) == el4
            True

            sage: QF = QuasiCuspForms(n=8, k=22/3, ep=-1)
            sage: el = QF(QF.f_inf()*QF.E2())
            sage: qexp = el.q_expansion_fixed_d(d_num_prec=1000)
            sage: qexp.parent()
            Power Series Ring in q over Real Field with 1000 bits of precision
            sage: QF.construct_quasi_form(qexp, rationalize=True) == el
            True
        '''
    @cached_method
    def q_basis(self, m=None, min_exp: int = 0, order_1=...):
        """
        Try to return a (basis) element of ``self`` with a Laurent series of the form
        ``q^m + O(q^N)``, where ``N=self.required_laurent_prec(min_exp)``.

        If ``m==None`` the whole basis (with varying ``m``'s) is returned if it exists.

        INPUT:

        - ``m`` -- integer, indicating the desired initial Laurent exponent
          of the element. If ``m==None`` (default) then the whole basis is
          returned.

        - ``min_exp`` -- integer (default: 0); the minimal Laurent exponent
          (for each quasi part) of the subspace of ``self`` which should be
          considered

        - ``order_1`` -- a lower bound for the order at ``-1`` of all quasi
          parts of the subspace (default: 0). If ``n!=infinity`` this parameter
          is ignored.

        OUTPUT:

        The corresponding basis (if ``m==None``) resp. the corresponding basis vector (if ``m!=None``).
        If the basis resp. element doesn't exist an exception is raised.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiWeakModularForms, ModularForms, QuasiModularForms
            sage: QF = QuasiWeakModularForms(n=8, k=10/3, ep=-1)
            sage: QF.default_prec(QF.required_laurent_prec(min_exp=-1))
            sage: q_basis = QF.q_basis(min_exp=-1)
            sage: q_basis
            [q^-1 + O(q^5), 1 + O(q^5), q + O(q^5), q^2 + O(q^5), q^3 + O(q^5), q^4 + O(q^5)]
            sage: QF.q_basis(m=-1, min_exp=-1)
            q^-1 + O(q^5)

            sage: MF = ModularForms(k=36)
            sage: MF.q_basis() == list(MF.gens())
            True

            sage: QF = QuasiModularForms(k=6)
            sage: QF.required_laurent_prec()
            3
            sage: QF.q_basis()
            [1 - 20160*q^3 - 158760*q^4 + O(q^5), q - 60*q^3 - 248*q^4 + O(q^5), q^2 + 8*q^3 + 30*q^4 + O(q^5)]

            sage: QF = QuasiWeakModularForms(n=infinity, k=-2, ep=-1)
            sage: QF.q_basis(order_1=-1)
            [1 - 168*q^2 + 2304*q^3 - 19320*q^4 + O(q^5),
             q - 18*q^2 + 180*q^3 - 1316*q^4 + O(q^5)]
        """
    def rationalize_series(self, laurent_series, coeff_bound: float = 1e-10, denom_factor=...):
        """
        Try to return a Laurent series with coefficients in ``self.coeff_ring()``
        that matches the given Laurent series.

        We give our best but there is absolutely no guarantee that it will work!

        INPUT:

        - ``laurent_series`` -- a Laurent series. If the Laurent coefficients
          already coerce into ``self.coeff_ring()`` with a formal parameter
          then the Laurent series is returned as is.

          Otherwise it is assumed that the series is normalized in the sense
          that the first non-trivial coefficient is a power of ``d`` (e.g.
          ``1``).

        - ``coeff_bound`` -- either ``None`` resp. ``0`` or a positive real
          number (default: ``1e-10``). If specified ``coeff_bound`` gives a
          lower bound for the size of the initial Laurent coefficients. If a
          coefficient is smaller it is assumed to be zero.

          For calculations with very small coefficients (less than ``1e-10``)
          ``coeff_bound`` should be set to something even smaller or just ``0``.

          Non-exact calculations often produce nonzero coefficients which are
          supposed to be zero. In those cases this parameter helps a lot.

        - ``denom_factor`` -- integer (default: 1) whose factor might occur in
          the denominator of the given Laurent coefficients (in addition to
          naturally occurring factors).

        OUTPUT:

        A Laurent series over ``self.coeff_ring()`` corresponding to the given
        Laurent series.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, ModularForms, QuasiCuspForms
            sage: WF = WeakModularForms(n=14)
            sage: qexp = WF.J_inv().q_expansion_fixed_d(d_num_prec=1000)
            sage: qexp.parent()
            Laurent Series Ring in q over Real Field with 1000 bits of precision
            sage: qexp_int = WF.rationalize_series(qexp)
            sage: qexp_int.add_bigoh(3)
            d*q^-1 + 37/98 + 2587/(38416*d)*q + 899/(117649*d^2)*q^2 + O(q^3)
            sage: qexp_int == WF.J_inv().q_expansion()
            True
            sage: WF.rationalize_series(qexp_int) == qexp_int
            True
            sage: WF(qexp_int) == WF.J_inv()
            True

            sage: WF.rationalize_series(qexp.parent()(1))
            1
            sage: WF.rationalize_series(qexp_int.parent()(1)).parent()
            Laurent Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring

            sage: MF = ModularForms(n=infinity, k=4)
            sage: qexp = MF.E4().q_expansion_fixed_d()
            sage: qexp.parent()
            Power Series Ring in q over Rational Field
            sage: qexp_int = MF.rationalize_series(qexp)
            sage: qexp_int.parent()
            Power Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: qexp_int == MF.E4().q_expansion()
            True
            sage: MF.rationalize_series(qexp_int) == qexp_int
            True
            sage: MF(qexp_int) == MF.E4()
            True

            sage: QF = QuasiCuspForms(n=8, k=22/3, ep=-1)
            sage: el = QF(QF.f_inf()*QF.E2())
            sage: qexp = el.q_expansion_fixed_d(d_num_prec=1000)
            sage: qexp.parent()
            Power Series Ring in q over Real Field with 1000 bits of precision
            sage: qexp_int = QF.rationalize_series(qexp)
            sage: qexp_int.parent()
            Power Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: qexp_int == el.q_expansion()
            True
            sage: QF.rationalize_series(qexp_int) == qexp_int
            True
            sage: QF(qexp_int) == el
            True
        """
    @cached_method
    def dimension(self):
        """
        Return the dimension of ``self``.

        .. NOTE::

            This method should be overloaded by subclasses.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import QuasiMeromorphicModularForms
            sage: QuasiMeromorphicModularForms(k=2, ep=-1).dimension()
            +Infinity
        """
    def rank(self):
        """
        Return the rank of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=4, k=24, ep=-1)
            sage: MF.rank()
            3
            sage: MF.subspace([MF.gen(0), MF.gen(2)]).rank()
            2
        """
    def degree(self):
        """
        Return the degree of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=4, k=24, ep=-1)
            sage: MF.degree()
            3
            sage: MF.subspace([MF.gen(0), MF.gen(2)]).degree() # defined in subspace.py
            3
        """
    def coordinate_vector(self, v) -> None:
        """
        This method should be overloaded by subclasses.

        Return the coordinate vector of the element ``v``
        with respect to ``self.gens()``.

        NOTE:

        Elements use this method (from their parent)
        to calculate their coordinates.

        INPUT:

        - ``v`` -- an element of ``self``

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=4, k=24, ep=-1)
            sage: MF.coordinate_vector(MF.gen(0)).parent() # defined in space.py
            Vector space of dimension 3 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: MF.coordinate_vector(MF.gen(0))          # defined in space.py
            (1, 0, 0)
            sage: subspace = MF.subspace([MF.gen(0), MF.gen(2)])
            sage: subspace.coordinate_vector(subspace.gen(0)).parent()  # defined in subspace.py
            Vector space of dimension 2 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: subspace.coordinate_vector(subspace.gen(0))           # defined in subspace.py
            (1, 0)
        """
    @cached_method
    def ambient_coordinate_vector(self, v):
        """
        Return the coordinate vector of the element ``v``
        in ``self.module()`` with respect to the basis
        from ``self.ambient_space``.

        NOTE:

        Elements use this method (from their parent)
        to calculate their coordinates.

        INPUT:

        - ``v`` -- an element of ``self``

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(n=4, k=24, ep=-1)
            sage: MF.ambient_coordinate_vector(MF.gen(0)).parent()
            Vector space of dimension 3 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: MF.ambient_coordinate_vector(MF.gen(0))
            (1, 0, 0)
            sage: subspace = MF.subspace([MF.gen(0), MF.gen(2)])
            sage: subspace.ambient_coordinate_vector(subspace.gen(0)).parent()
            Vector space of degree 3 and dimension 2 over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            Basis matrix:
            [1 0 0]
            [0 0 1]
            sage: subspace.ambient_coordinate_vector(subspace.gen(0))
            (1, 0, 0)
        """
    def gens(self) -> tuple:
        """
        This method should be overloaded by subclasses.

        Return a basis of ``self`` as a tuple.

        Note that the coordinate vector of elements of ``self``
        are with respect to this basis.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ModularForms(k=12).gens() # defined in space.py
            (1 + 196560*q^2 + 16773120*q^3 + 398034000*q^4 + O(q^5),
             q - 24*q^2 + 252*q^3 - 1472*q^4 + O(q^5))
        """
    def gen(self, k: int = 0):
        """
        Return the ``k``-th basis element of ``self``
        if possible (default: ``k=0``).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ModularForms(k=12).gen(1).parent()
            ModularForms(n=3, k=12, ep=1) over Integer Ring
            sage: ModularForms(k=12).gen(1)
            q - 24*q^2 + 252*q^3 - 1472*q^4 + O(q^5)
        """
