from .analytic_type import AnalyticType as AnalyticType
from .constructor import FormsRing as FormsRing, FormsSpace as FormsSpace
from .graded_ring_element import FormsRingElement as FormsRingElement
from .series_constructor import MFSeriesConstructor as MFSeriesConstructor
from _typeshed import Incomplete
from sage.algebras.free_algebra import FreeAlgebra as FreeAlgebra
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent

class FormsRing_abstract(Parent):
    """
    Abstract (Hecke) forms ring.

    This should never be called directly. Instead one should
    instantiate one of the derived classes of this class.
    """
    Element = FormsRingElement
    AT: Incomplete
    def __init__(self, group, base_ring, red_hom, n) -> None:
        """
        Abstract (Hecke) forms ring.

        INPUT:

        - ``group`` -- the Hecke triangle group (default: ``HeckeTriangleGroup(3)``)

        - ``base_ring`` -- the base_ring (default: `\\Z`)

        - ``red_hom`` -- if ``True`` then results of binary operations are
          considered homogeneous whenever it makes sense (default: ``False``).
          This is mainly used by the (Hecke) forms.

        OUTPUT: the corresponding abstract (Hecke) forms ring

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: MR = ModularFormsRing(n=5, base_ring=ZZ, red_hom=True)
            sage: MR
            ModularFormsRing(n=5) over Integer Ring
            sage: MR.group()
            Hecke triangle group for n = 5
            sage: MR.base_ring()
            Integer Ring
            sage: MR.has_reduce_hom()
            True
            sage: MR.is_homogeneous()
            False
        """
    def default_prec(self, prec=None):
        """
        Set the default precision ``prec`` for the Fourier expansion.
        If ``prec=None`` (default) then the current default precision is
        returned instead.

        INPUT:

        - ``prec`` -- integer

        .. NOTE::

            This is also used as the default precision for the Fourier
            expansion when evaluating forms.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MR = ModularFormsRing()
            sage: MR.default_prec(3)
            sage: MR.default_prec()
            3
            sage: MR.Delta().q_expansion_fixed_d()
            q - 24*q^2 + O(q^3)
            sage: MF = ModularForms(k=4)
            sage: MF.default_prec(2)
            sage: MF.E4()
            1 + 240*q + O(q^2)
            sage: MF.default_prec()
            2
        """
    def disp_prec(self, prec=None):
        '''
        Set the maximal display precision to ``prec``.
        If ``prec="max"`` the precision is set to the default precision.
        If ``prec=None`` (default) then the current display precision is returned instead.

        NOTE:

        This is used for displaying/representing (elements of)
        ``self`` as Fourier expansions.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=4)
            sage: MF.default_prec(5)
            sage: MF.disp_prec(3)
            sage: MF.disp_prec()
            3
            sage: MF.E4()
            1 + 240*q + 2160*q^2 + O(q^3)
            sage: MF.disp_prec("max")
            sage: MF.E4()
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + O(q^5)
        '''
    def default_num_prec(self, prec=None):
        """
        Set the default numerical precision to ``prec`` (default: ``53``).
        If ``prec=None`` (default) the current default numerical
        precision is returned instead.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: MF = ModularForms(k=6)
            sage: MF.default_prec(20)
            sage: MF.default_num_prec(10)
            sage: MF.default_num_prec()
            10
            sage: E6 = MF.E6()
            sage: E6(i + 10^(-1000))
            0.002... - 6.7...e-1000*I
            sage: MF.default_num_prec(100)
            sage: E6(i + 10^(-1000))
            3.9946838...e-1999 - 6.6578064...e-1000*I

            sage: MF = ModularForms(n=5, k=4/3)
            sage: f_rho = MF.f_rho()
            sage: f_rho.q_expansion(prec=2)[1]
            7/(100*d)
            sage: MF.default_num_prec(15)
            sage: f_rho.q_expansion_fixed_d(prec=2)[1]
            9.9...
            sage: MF.default_num_prec(100)
            sage: f_rho.q_expansion_fixed_d(prec=2)[1]
            9.92593243510795915276017782...
        """
    def change_ring(self, new_base_ring):
        """
        Return the same space as ``self`` but over a new base ring ``new_base_ring``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().change_ring(CC)
            ModularFormsRing(n=3) over Complex Field with 53 bits of precision
        """
    def graded_ring(self):
        """
        Return the graded ring containing ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing, CuspFormsRing
            sage: from sage.modular.modform_hecketriangle.space import CuspForms

            sage: MR = ModularFormsRing(n=5)
            sage: MR.graded_ring() == MR
            True

            sage: CF=CuspForms(k=12)
            sage: CF.graded_ring() == CuspFormsRing()
            False
            sage: CF.graded_ring() == CuspFormsRing(red_hom=True)
            True

            sage: CF.subspace([CF.Delta()]).graded_ring() == CuspFormsRing(red_hom=True)
            True
        """
    def extend_type(self, analytic_type=None, ring: bool = False):
        '''
        Return a new space which contains (elements of) ``self`` with the analytic type
        of ``self`` extended by ``analytic_type``, possibly extended to a graded ring
        in case ``ring`` is ``True``.

        INPUT:

        - ``analytic_type`` -- an ``AnalyticType`` or something which
          coerces into it (default: ``None``)

        - ``ring`` -- whether to extend to a graded ring (default: ``False``)

        OUTPUT: the new extended space

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: from sage.modular.modform_hecketriangle.space import CuspForms

            sage: MR = ModularFormsRing(n=5)
            sage: MR.extend_type(["quasi", "weak"])
            QuasiWeakModularFormsRing(n=5) over Integer Ring

            sage: CF=CuspForms(k=12)
            sage: CF.extend_type("holo")
            ModularForms(n=3, k=12, ep=1) over Integer Ring
            sage: CF.extend_type("quasi", ring=True)
            QuasiCuspFormsRing(n=3) over Integer Ring

            sage: CF.subspace([CF.Delta()]).extend_type()
            CuspForms(n=3, k=12, ep=1) over Integer Ring
        '''
    def reduce_type(self, analytic_type=None, degree=None):
        '''
        Return a new space with analytic properties shared by both ``self`` and ``analytic_type``,
        possibly reduced to its space of homogeneous elements of the given ``degree`` (if ``degree`` is set).
        Elements of the new space are contained in ``self``.

        INPUT:

        - ``analytic_type`` -- an ``AnalyticType`` or something which coerces
          into it (default: ``None``)

        - ``degree`` -- ``None`` (default) or the degree of the homogeneous
          component to which ``self`` should be reduced

        OUTPUT: the new reduced space

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiModularFormsRing
            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms

            sage: MR = QuasiModularFormsRing()
            sage: MR.reduce_type(["quasi", "cusp"])
            QuasiCuspFormsRing(n=3) over Integer Ring

            sage: MR.reduce_type("cusp", degree=(12,1))
            CuspForms(n=3, k=12, ep=1) over Integer Ring

            sage: MF=QuasiModularForms(k=6)
            sage: MF.reduce_type("holo")
            ModularForms(n=3, k=6, ep=-1) over Integer Ring

            sage: MF.reduce_type([])
            ZeroForms(n=3, k=6, ep=-1) over Integer Ring
        '''
    @cached_method
    def contains_coeff_ring(self):
        """
        Return whether ``self`` contains its coefficient ring.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import CuspFormsRing, ModularFormsRing
            sage: CuspFormsRing(n=4).contains_coeff_ring()
            False
            sage: ModularFormsRing(n=5).contains_coeff_ring()
            True
        """
    def construction(self):
        """
        Return a functor that constructs ``self`` (used by the coercion machinery).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().construction()
            (ModularFormsRingFunctor(n=3), BaseFacade(Integer Ring))
        """
    @cached_method
    def group(self):
        """
        Return the (Hecke triangle) group of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: MR = ModularFormsRing(n=7)
            sage: MR.group()
            Hecke triangle group for n = 7

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CF = CuspForms(n=7, k=4/5)
            sage: CF.group()
            Hecke triangle group for n = 7
        """
    @cached_method
    def hecke_n(self):
        """
        Return the parameter ``n`` of the
        (Hecke triangle) group of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: MR = ModularFormsRing(n=7)
            sage: MR.hecke_n()
            7

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CF = CuspForms(n=7, k=4/5)
            sage: CF.hecke_n()
            7
        """
    @cached_method
    def base_ring(self):
        """
        Return base ring of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().base_ring()
            Integer Ring

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CuspForms(k=12, base_ring=AA).base_ring()
            Algebraic Real Field
        """
    @cached_method
    def coeff_ring(self):
        """
        Return coefficient ring of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().coeff_ring()
            Fraction Field of Univariate Polynomial Ring in d over Integer Ring

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CuspForms(k=12, base_ring=AA).coeff_ring()
            Fraction Field of Univariate Polynomial Ring in d over Algebraic Real Field
        """
    @cached_method
    def pol_ring(self):
        """
        Return the underlying polynomial ring used
        by ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().pol_ring()
            Multivariate Polynomial Ring in x, y, z, d over Integer Ring

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CuspForms(k=12, base_ring=AA).pol_ring()
            Multivariate Polynomial Ring in x, y, z, d over Algebraic Real Field
        """
    @cached_method
    def rat_field(self):
        """
        Return the underlying rational field used by
        ``self`` to construct/represent elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().rat_field()
            Fraction Field of Multivariate Polynomial Ring in x, y, z, d over Integer Ring

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CuspForms(k=12, base_ring=AA).rat_field()
            Fraction Field of Multivariate Polynomial Ring in x, y, z, d over Algebraic Real Field
        """
    def get_d(self, fix_d: bool = False, d_num_prec=None):
        """
        Return the parameter ``d`` of ``self`` either as a formal
        parameter or as a numerical approximation with the specified
        precision (resp. an exact value in the arithmetic cases).

        For an (exact) symbolic expression also see
        ``HeckeTriangleGroup().dvalue()``.

        INPUT:

        - ``fix_d`` -- if ``False`` (default) a formal parameter is
          used for ``d``. If ``True`` then the numerical value of ``d`` is used
          (or an exact value if the group is arithmetic). Otherwise, the given
          value is used for ``d``.

        - ``d_num_prec`` -- integer (default: ``None``); the numerical
          precision of ``d``. By default, the default numerical precision of
          ``self.parent()`` is used.

        OUTPUT:

        The corresponding formal, numerical or exact parameter ``d`` of ``self``,
        depending on the arguments and whether ``self.group()`` is arithmetic.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing(n=8).get_d()
            d
            sage: ModularFormsRing(n=8).get_d().parent()
            Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: ModularFormsRing(n=infinity).get_d(fix_d = True)
            1/64
            sage: ModularFormsRing(n=infinity).get_d(fix_d = True).parent()
            Rational Field
            sage: ModularFormsRing(n=5).default_num_prec(40)
            sage: ModularFormsRing(n=5).get_d(fix_d = True)
            0.0070522341...
            sage: ModularFormsRing(n=5).get_d(fix_d = True).parent()
            Real Field with 40 bits of precision
            sage: ModularFormsRing(n=5).get_d(fix_d = True, d_num_prec=100).parent()
            Real Field with 100 bits of precision
            sage: ModularFormsRing(n=5).get_d(fix_d=1).parent()
            Integer Ring
        """
    def get_q(self, prec=None, fix_d: bool = False, d_num_prec=None):
        """
        Return the generator of the power series of the Fourier expansion of ``self``.

        INPUT:

        - ``prec`` -- an integer or ``None`` (default), namely the desired
          default precision of the space of power series. If nothing is
          specified the default precision of ``self`` is used.

        - ``fix_d`` -- if ``False`` (default) a formal parameter is used for
          ``d``. If ``True`` then the numerical value of ``d`` is used (resp.
          an exact value if the group is arithmetic). Otherwise the given value
          is used for ``d``.

        - ``d_num_prec`` -- the precision to be used if a numerical value for
          ``d`` is substituted (default: ``None``), otherwise the default
          numerical precision of ``self.parent()`` is used

        OUTPUT:

        The generator of the ``PowerSeriesRing`` of corresponding to the given
        parameters. The base ring of the power series ring is given by the corresponding
        parent of ``self.get_d()`` with the same arguments.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing(n=8).default_prec(5)
            sage: ModularFormsRing(n=8).get_q().parent()
            Power Series Ring in q over Fraction Field of Univariate Polynomial Ring in d over Integer Ring
            sage: ModularFormsRing(n=8).get_q().parent().default_prec()
            5
            sage: ModularFormsRing(n=infinity).get_q(prec=12, fix_d = True).parent()
            Power Series Ring in q over Rational Field
            sage: ModularFormsRing(n=infinity).get_q(prec=12, fix_d = True).parent().default_prec()
            12
            sage: ModularFormsRing(n=5).default_num_prec(40)
            sage: ModularFormsRing(n=5).get_q(fix_d = True).parent()
            Power Series Ring in q over Real Field with 40 bits of precision
            sage: ModularFormsRing(n=5).get_q(fix_d = True, d_num_prec=100).parent()
            Power Series Ring in q over Real Field with 100 bits of precision
            sage: ModularFormsRing(n=5).get_q(fix_d=1).parent()
            Power Series Ring in q over Rational Field
        """
    @cached_method
    def diff_alg(self):
        """
        Return the algebra of differential operators
        (over QQ) which is used on rational functions
        representing elements of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().diff_alg()
            Noncommutative Multivariate Polynomial Ring in X, Y, Z, dX, dY, dZ over Rational Field, nc-relations: {dX*X: X*dX + 1, dY*Y: Y*dY + 1, dZ*Z: Z*dZ + 1}

            sage: from sage.modular.modform_hecketriangle.space import CuspForms
            sage: CuspForms(k=12, base_ring=AA).diff_alg()
            Noncommutative Multivariate Polynomial Ring in X, Y, Z, dX, dY, dZ over Rational Field, nc-relations: {dX*X: X*dX + 1, dY*Y: Y*dY + 1, dZ*Z: Z*dZ + 1}
        """
    @cached_method
    def has_reduce_hom(self) -> bool:
        """
        Return whether the method ``reduce`` should reduce
        homogeneous elements to the corresponding space of homogeneous elements.

        This is mainly used by binary operations on homogeneous
        spaces which temporarily produce an element of ``self``
        but want to consider it as a homogeneous element
        (also see ``reduce``).

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().has_reduce_hom()
            False
            sage: ModularFormsRing(red_hom=True).has_reduce_hom()
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ModularForms(k=6).has_reduce_hom()
            True
            sage: ModularForms(k=6).graded_ring().has_reduce_hom()
            True
        """
    def is_homogeneous(self) -> bool:
        """
        Return whether ``self`` is homogeneous component.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().is_homogeneous()
            False

            sage: from sage.modular.modform_hecketriangle.space import ModularForms
            sage: ModularForms(k=6).is_homogeneous()
            True
        """
    def is_modular(self) -> bool:
        """
        Return whether ``self`` only contains modular elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiWeakModularFormsRing, CuspFormsRing
            sage: QuasiWeakModularFormsRing().is_modular()
            False
            sage: CuspFormsRing(n=7).is_modular()
            True

            sage: from sage.modular.modform_hecketriangle.space import QuasiWeakModularForms, CuspForms
            sage: QuasiWeakModularForms(k=10).is_modular()
            False
            sage: CuspForms(n=7, k=12, base_ring=AA).is_modular()
            True
        """
    def is_weakly_holomorphic(self) -> bool:
        """
        Return whether ``self`` only contains weakly
        holomorphic modular elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, QuasiWeakModularFormsRing, CuspFormsRing
            sage: QuasiMeromorphicModularFormsRing().is_weakly_holomorphic()
            False
            sage: QuasiWeakModularFormsRing().is_weakly_holomorphic()
            True

            sage: from sage.modular.modform_hecketriangle.space import MeromorphicModularForms, CuspForms
            sage: MeromorphicModularForms(k=10).is_weakly_holomorphic()
            False
            sage: CuspForms(n=7, k=12, base_ring=AA).is_weakly_holomorphic()
            True
        """
    def is_holomorphic(self) -> bool:
        """
        Return whether ``self`` only contains holomorphic
        modular elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiWeakModularFormsRing, QuasiModularFormsRing
            sage: QuasiWeakModularFormsRing().is_holomorphic()
            False
            sage: QuasiModularFormsRing().is_holomorphic()
            True

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, CuspForms
            sage: WeakModularForms(k=10).is_holomorphic()
            False
            sage: CuspForms(n=7, k=12, base_ring=AA).is_holomorphic()
            True
        """
    def is_cuspidal(self) -> bool:
        """
        Return whether ``self`` only contains cuspidal elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiModularFormsRing, QuasiCuspFormsRing
            sage: QuasiModularFormsRing().is_cuspidal()
            False
            sage: QuasiCuspFormsRing().is_cuspidal()
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms, QuasiCuspForms
            sage: ModularForms(k=12).is_cuspidal()
            False
            sage: QuasiCuspForms(k=12).is_cuspidal()
            True
        """
    def is_zerospace(self) -> bool:
        """
        Return whether ``self`` is the (`0`-dimensional) zero space.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing
            sage: ModularFormsRing().is_zerospace()
            False

            sage: from sage.modular.modform_hecketriangle.space import ModularForms, CuspForms
            sage: ModularForms(k=12).is_zerospace()
            False
            sage: CuspForms(k=12).reduce_type([]).is_zerospace()
            True
        """
    def analytic_type(self):
        """
        Return the analytic type of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, QuasiWeakModularFormsRing
            sage: QuasiMeromorphicModularFormsRing().analytic_type()
            quasi meromorphic modular
            sage: QuasiWeakModularFormsRing().analytic_type()
            quasi weakly holomorphic modular

            sage: from sage.modular.modform_hecketriangle.space import MeromorphicModularForms, CuspForms
            sage: MeromorphicModularForms(k=10).analytic_type()
            meromorphic modular
            sage: CuspForms(n=7, k=12, base_ring=AA).analytic_type()
            cuspidal
        """
    def homogeneous_part(self, k, ep):
        """
        Return the homogeneous component of degree (``k``, ``e``) of ``self``.

        INPUT:

        - ``k`` -- integer

        - ``ep`` -- `+1` or `-1`

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, QuasiWeakModularFormsRing
            sage: QuasiMeromorphicModularFormsRing(n=7).homogeneous_part(k=2, ep=-1)
            QuasiMeromorphicModularForms(n=7, k=2, ep=-1) over Integer Ring
        """
    @cached_method
    def J_inv(self):
        """
        Return the J-invariant (Hauptmodul) of the group of ``self``.
        It is normalized such that ``J_inv(infinity) = infinity``,
        it has real Fourier coefficients starting with ``d > 0`` and ``J_inv(i) = 1``

        It lies in a (weak) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, WeakModularFormsRing, CuspFormsRing
            sage: MR = WeakModularFormsRing(n=7)
            sage: J_inv = MR.J_inv()
            sage: J_inv in MR
            True
            sage: CuspFormsRing(n=7).J_inv() == J_inv
            True
            sage: J_inv
            f_rho^7/(f_rho^7 - f_i^2)
            sage: QuasiMeromorphicModularFormsRing(n=7).J_inv() == QuasiMeromorphicModularFormsRing(n=7)(J_inv)
            True

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, CuspForms
            sage: MF = WeakModularForms(n=5, k=0)
            sage: J_inv = MF.J_inv()
            sage: J_inv in MF
            True
            sage: WeakModularFormsRing(n=5, red_hom=True).J_inv() == J_inv
            True
            sage: CuspForms(n=5, k=12).J_inv() == J_inv
            True
            sage: MF.disp_prec(3)
            sage: J_inv
            d*q^-1 + 79/200 + 42877/(640000*d)*q + 12957/(2000000*d^2)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = WeakModularForms(n=5)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: WeakModularForms(n=5).J_inv().q_expansion(prec=5) == MFC(group=5, prec=7).J_inv_ZZ()(q/d).add_bigoh(5)
            True
            sage: WeakModularForms(n=infinity).J_inv().q_expansion(prec=5) == MFC(group=infinity, prec=7).J_inv_ZZ()(q/d).add_bigoh(5)
            True
            sage: WeakModularForms(n=5).J_inv().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).J_inv_ZZ().add_bigoh(5)
            True
            sage: WeakModularForms(n=infinity).J_inv().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).J_inv_ZZ().add_bigoh(5)
            True

            sage: WeakModularForms(n=infinity).J_inv()
            1/64*q^-1 + 3/8 + 69/16*q + 32*q^2 + 5601/32*q^3 + 768*q^4 + O(q^5)

            sage: WeakModularForms().J_inv()
            1/1728*q^-1 + 31/72 + 1823/16*q + 335840/27*q^2 + 16005555/32*q^3 + 11716352*q^4 + O(q^5)
        """
    @cached_method
    def j_inv(self):
        """
        Return the j-invariant (Hauptmodul) of the group of ``self``.
        It is normalized such that ``j_inv(infinity) = infinity``,
        and such that it has real Fourier coefficients starting with ``1``.

        It lies in a (weak) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, WeakModularFormsRing, CuspFormsRing
            sage: MR = WeakModularFormsRing(n=7)
            sage: j_inv = MR.j_inv()
            sage: j_inv in MR
            True
            sage: CuspFormsRing(n=7).j_inv() == j_inv
            True
            sage: j_inv
            f_rho^7/(f_rho^7*d - f_i^2*d)
            sage: QuasiMeromorphicModularFormsRing(n=7).j_inv() == QuasiMeromorphicModularFormsRing(n=7)(j_inv)
            True

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, CuspForms
            sage: MF = WeakModularForms(n=5, k=0)
            sage: j_inv = MF.j_inv()
            sage: j_inv in MF
            True
            sage: WeakModularFormsRing(n=5, red_hom=True).j_inv() == j_inv
            True
            sage: CuspForms(n=5, k=12).j_inv() == j_inv
            True
            sage: MF.disp_prec(3)
            sage: j_inv
            q^-1 + 79/(200*d) + 42877/(640000*d^2)*q + 12957/(2000000*d^3)*q^2 + O(q^3)

            sage: WeakModularForms(n=infinity).j_inv()
            q^-1 + 24 + 276*q + 2048*q^2 + 11202*q^3 + 49152*q^4 + O(q^5)

            sage: WeakModularForms().j_inv()
            q^-1 + 744 + 196884*q + 21493760*q^2 + 864299970*q^3 + 20245856256*q^4 + O(q^5)
        """
    @cached_method
    def f_rho(self):
        """
        Return a normalized modular form ``f_rho`` with exactly one simple
        zero at ``rho`` (up to the group action).

        It lies in a (holomorphic) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        The polynomial variable ``x`` exactly corresponds to ``f_rho``.

        NOTE:

        If ``n=infinity`` the situation is different, there we have:
        ``f_rho=1`` (since that's the limit as ``n`` goes to infinity)
        and the polynomial variable ``x`` no longer refers to ``f_rho``.
        Instead it refers to ``E4`` which has exactly one simple zero
        at the cusp ``-1``. Also note that ``E4`` is the limit of
        ``f_rho^(n-2)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, ModularFormsRing, CuspFormsRing
            sage: MR = ModularFormsRing(n=7)
            sage: f_rho = MR.f_rho()
            sage: f_rho in MR
            True
            sage: CuspFormsRing(n=7).f_rho() == f_rho
            True
            sage: f_rho
            f_rho
            sage: QuasiMeromorphicModularFormsRing(n=7).f_rho() == QuasiMeromorphicModularFormsRing(n=7)(f_rho)
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms, CuspForms
            sage: MF = ModularForms(n=5, k=4/3)
            sage: f_rho = MF.f_rho()
            sage: f_rho in MF
            True
            sage: ModularFormsRing(n=5, red_hom=True).f_rho() == f_rho
            True
            sage: CuspForms(n=5, k=12).f_rho() == f_rho
            True
            sage: MF.disp_prec(3)
            sage: f_rho
            1 + 7/(100*d)*q + 21/(160000*d^2)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = ModularForms(n=5)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: ModularForms(n=5).f_rho().q_expansion(prec=5) == MFC(group=5, prec=7).f_rho_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=infinity).f_rho().q_expansion(prec=5) == MFC(group=infinity, prec=7).f_rho_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=5).f_rho().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).f_rho_ZZ().add_bigoh(5)
            True
            sage: ModularForms(n=infinity).f_rho().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).f_rho_ZZ().add_bigoh(5)
            True

            sage: ModularForms(n=infinity, k=0).f_rho() == ModularForms(n=infinity, k=0)(1)
            True

            sage: ModularForms(k=4).f_rho() == ModularForms(k=4).E4()
            True
            sage: ModularForms(k=4).f_rho()
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + O(q^5)
        """
    @cached_method
    def f_i(self):
        """
        Return a normalized modular form ``f_i`` with exactly one simple
        zero at ``i`` (up to the group action).

        It lies in a (holomorphic) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        The polynomial variable ``y`` exactly corresponds to ``f_i``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, ModularFormsRing, CuspFormsRing
            sage: MR = ModularFormsRing(n=7)
            sage: f_i = MR.f_i()
            sage: f_i in MR
            True
            sage: CuspFormsRing(n=7).f_i() == f_i
            True
            sage: f_i
            f_i
            sage: QuasiMeromorphicModularFormsRing(n=7).f_i() == QuasiMeromorphicModularFormsRing(n=7)(f_i)
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms, CuspForms
            sage: MF = ModularForms(n=5, k=10/3)
            sage: f_i = MF.f_i()
            sage: f_i in MF
            True
            sage: ModularFormsRing(n=5, red_hom=True).f_i() == f_i
            True
            sage: CuspForms(n=5, k=12).f_i() == f_i
            True
            sage: MF.disp_prec(3)
            sage: f_i
            1 - 13/(40*d)*q - 351/(64000*d^2)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = ModularForms(n=5)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: ModularForms(n=5).f_i().q_expansion(prec=5) == MFC(group=5, prec=7).f_i_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=infinity).f_i().q_expansion(prec=5) == MFC(group=infinity, prec=7).f_i_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=5).f_i().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).f_i_ZZ().add_bigoh(5)
            True
            sage: ModularForms(n=infinity).f_i().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).f_i_ZZ().add_bigoh(5)
            True

            sage: ModularForms(n=infinity, k=2).f_i()
            1 - 24*q + 24*q^2 - 96*q^3 + 24*q^4 + O(q^5)

            sage: ModularForms(k=6).f_i() == ModularForms(k=4).E6()
            True
            sage: ModularForms(k=6).f_i()
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 + O(q^5)
        """
    @cached_method
    def f_inf(self):
        """
        Return a normalized (according to its first nontrivial Fourier
        coefficient) cusp form ``f_inf`` with exactly one simple zero
        at ``infinity`` (up to the group action).

        It lies in a (cuspidal) extension of the graded ring of
        ``self``. In case ``has_reduce_hom`` is ``True`` it is given
        as an element of the corresponding space of homogeneous elements.

        NOTE:

        If ``n=infinity`` then ``f_inf`` is no longer a cusp form
        since it doesn't vanish at the cusp ``-1``. The first
        non-trivial cusp form is given by ``E4*f_inf``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, CuspFormsRing
            sage: MR = CuspFormsRing(n=7)
            sage: f_inf = MR.f_inf()
            sage: f_inf in MR
            True
            sage: f_inf
            f_rho^7*d - f_i^2*d
            sage: QuasiMeromorphicModularFormsRing(n=7).f_inf() == QuasiMeromorphicModularFormsRing(n=7)(f_inf)
            True

            sage: from sage.modular.modform_hecketriangle.space import CuspForms, ModularForms
            sage: MF = CuspForms(n=5, k=20/3)
            sage: f_inf = MF.f_inf()
            sage: f_inf in MF
            True
            sage: CuspFormsRing(n=5, red_hom=True).f_inf() == f_inf
            True
            sage: CuspForms(n=5, k=0).f_inf() == f_inf
            True
            sage: MF.disp_prec(3)
            sage: f_inf
            q - 9/(200*d)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = ModularForms(n=5)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: ModularForms(n=5).f_inf().q_expansion(prec=5) == (d*MFC(group=5, prec=7).f_inf_ZZ()(q/d)).add_bigoh(5)
            True
            sage: ModularForms(n=infinity).f_inf().q_expansion(prec=5) == (d*MFC(group=infinity, prec=7).f_inf_ZZ()(q/d)).add_bigoh(5)
            True
            sage: ModularForms(n=5).f_inf().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).f_inf_ZZ().add_bigoh(5)
            True
            sage: ModularForms(n=infinity).f_inf().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).f_inf_ZZ().add_bigoh(5)
            True

            sage: ModularForms(n=infinity, k=4).f_inf().reduced_parent()
            ModularForms(n=+Infinity, k=4, ep=1) over Integer Ring
            sage: ModularForms(n=infinity, k=4).f_inf()
            q - 8*q^2 + 28*q^3 - 64*q^4 + O(q^5)

            sage: CuspForms(k=12).f_inf() == CuspForms(k=12).Delta()
            True
            sage: CuspForms(k=12).f_inf()
            q - 24*q^2 + 252*q^3 - 1472*q^4 + O(q^5)
        """
    @cached_method
    def G_inv(self):
        """
        If `2` divides `n`: Return the G-invariant of the group of ``self``.

        The G-invariant is analogous to the J-invariant but has multiplier `-1`.
        I.e. ``G_inv(-1/t) = -G_inv(t)``. It is a holomorphic square root
        of ``J_inv*(J_inv-1)`` with real Fourier coefficients.

        If `2` does not divide `n` the function does not exist and an
        exception is raised.

        The G-invariant lies in a (weak) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        NOTE:

        If ``n=infinity`` then ``G_inv`` is holomorphic everywhere except
        at the cusp ``-1`` where it isn't even meromorphic. Consequently
        this function raises an exception for ``n=infinity``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, WeakModularFormsRing, CuspFormsRing
            sage: MR = WeakModularFormsRing(n=8)
            sage: G_inv = MR.G_inv()
            sage: G_inv in MR
            True
            sage: CuspFormsRing(n=8).G_inv() == G_inv
            True
            sage: G_inv
            f_rho^4*f_i*d/(f_rho^8 - f_i^2)
            sage: QuasiMeromorphicModularFormsRing(n=8).G_inv() == QuasiMeromorphicModularFormsRing(n=8)(G_inv)
            True

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, CuspForms
            sage: MF = WeakModularForms(n=8, k=0, ep=-1)
            sage: G_inv = MF.G_inv()
            sage: G_inv in MF
            True
            sage: WeakModularFormsRing(n=8, red_hom=True).G_inv() == G_inv
            True
            sage: CuspForms(n=8, k=12, ep=1).G_inv() == G_inv
            True
            sage: MF.disp_prec(3)
            sage: G_inv
            d^2*q^-1 - 15*d/128 - 15139/262144*q - 11575/(1572864*d)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = WeakModularForms(n=8)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: WeakModularForms(n=8).G_inv().q_expansion(prec=5) == (d*MFC(group=8, prec=7).G_inv_ZZ()(q/d)).add_bigoh(5)
            True
            sage: WeakModularForms(n=8).G_inv().q_expansion(fix_d=1, prec=5) == MFC(group=8, prec=7).G_inv_ZZ().add_bigoh(5)
            True

            sage: WeakModularForms(n=4, k=0, ep=-1).G_inv()
            1/65536*q^-1 - 3/8192 - 955/16384*q - 49/32*q^2 - 608799/32768*q^3 - 659/4*q^4 + O(q^5)

            As explained above, the G-invariant exists only for even `n`::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: MF = WeakModularForms(n=9)
            sage: MF.G_inv()
            Traceback (most recent call last):
            ...
            ArithmeticError: G_inv doesn't exist for odd n(=9).
        """
    @cached_method
    def g_inv(self):
        """
        If `2` divides `n`: Return the g-invariant of the group of ``self``.

        The g-invariant is analogous to the j-invariant but has
        multiplier ``-1``.  I.e. ``g_inv(-1/t) = -g_inv(t)``. It is a
        (normalized) holomorphic square root of ``J_inv*(J_inv-1)``,
        normalized such that its first nontrivial Fourier coefficient
        is ``1``.

        If `2` does not divide ``n`` the function does not exist and
        an exception is raised.

        The g-invariant lies in a (weak) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        NOTE:

        If ``n=infinity`` then ``g_inv`` is holomorphic everywhere except
        at the cusp ``-1`` where it isn't even meromorphic. Consequently
        this function raises an exception for ``n=infinity``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, WeakModularFormsRing, CuspFormsRing
            sage: MR = WeakModularFormsRing(n=8)
            sage: g_inv = MR.g_inv()
            sage: g_inv in MR
            True
            sage: CuspFormsRing(n=8).g_inv() == g_inv
            True
            sage: g_inv
            f_rho^4*f_i/(f_rho^8*d - f_i^2*d)
            sage: QuasiMeromorphicModularFormsRing(n=8).g_inv() == QuasiMeromorphicModularFormsRing(n=8)(g_inv)
            True

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms, CuspForms
            sage: MF = WeakModularForms(n=8, k=0, ep=-1)
            sage: g_inv = MF.g_inv()
            sage: g_inv in MF
            True
            sage: WeakModularFormsRing(n=8, red_hom=True).g_inv() == g_inv
            True
            sage: CuspForms(n=8, k=12, ep=1).g_inv() == g_inv
            True
            sage: MF.disp_prec(3)
            sage: g_inv
            q^-1 - 15/(128*d) - 15139/(262144*d^2)*q - 11575/(1572864*d^3)*q^2 + O(q^3)

            sage: WeakModularForms(n=4, k=0, ep=-1).g_inv()
            q^-1 - 24 - 3820*q - 100352*q^2 - 1217598*q^3 - 10797056*q^4 + O(q^5)

            As explained above, the g-invariant exists only for even `n`::

            sage: from sage.modular.modform_hecketriangle.space import WeakModularForms
            sage: MF = WeakModularForms(n=9)
            sage: MF.g_inv()
            Traceback (most recent call last):
            ...
            ArithmeticError: g_inv doesn't exist for odd n(=9).
        """
    @cached_method
    def E4(self):
        """
        Return the normalized Eisenstein series of weight `4`.

        It lies in a (holomorphic) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        It is equal to ``f_rho^(n-2)``.

        NOTE:

        If ``n=infinity`` the situation is different, there we have:
        ``f_rho=1`` (since that's the limit as ``n`` goes to infinity)
        and the polynomial variable ``x`` refers to ``E4`` instead of
        ``f_rho``. In that case ``E4`` has exactly one simple zero
        at the cusp ``-1``. Also note that ``E4`` is the limit of ``f_rho^n``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, ModularFormsRing, CuspFormsRing
            sage: MR = ModularFormsRing(n=7)
            sage: E4 = MR.E4()
            sage: E4 in MR
            True
            sage: CuspFormsRing(n=7).E4() == E4
            True
            sage: E4
            f_rho^5
            sage: QuasiMeromorphicModularFormsRing(n=7).E4() == QuasiMeromorphicModularFormsRing(n=7)(E4)
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms, CuspForms
            sage: MF = ModularForms(n=5, k=4)
            sage: E4 = MF.E4()
            sage: E4 in MF
            True
            sage: ModularFormsRing(n=5, red_hom=True).E4() == E4
            True
            sage: CuspForms(n=5, k=12).E4() == E4
            True
            sage: MF.disp_prec(3)
            sage: E4
            1 + 21/(100*d)*q + 483/(32000*d^2)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = ModularForms(n=5)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: ModularForms(n=5, k=4).E4().q_expansion(prec=5) == MFC(group=5, prec=7).E4_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=infinity, k=4).E4().q_expansion(prec=5) == MFC(group=infinity, prec=7).E4_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=5, k=4).E4().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).E4_ZZ().add_bigoh(5)
            True
            sage: ModularForms(n=infinity, k=4).E4().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).E4_ZZ().add_bigoh(5)
            True

            sage: ModularForms(n=infinity, k=4).E4()
            1 + 16*q + 112*q^2 + 448*q^3 + 1136*q^4 + O(q^5)

            sage: ModularForms(k=4).f_rho() == ModularForms(k=4).E4()
            True
            sage: ModularForms(k=4).E4()
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + O(q^5)
        """
    @cached_method
    def E6(self):
        """
        Return the normalized Eisenstein series of weight `6`.

        It lies in a (holomorphic) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        It is equal to ``f_rho^(n-3) * f_i``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, ModularFormsRing, CuspFormsRing
            sage: MR = ModularFormsRing(n=7)
            sage: E6 = MR.E6()
            sage: E6 in MR
            True
            sage: CuspFormsRing(n=7).E6() == E6
            True
            sage: E6
            f_rho^4*f_i
            sage: QuasiMeromorphicModularFormsRing(n=7).E6() == QuasiMeromorphicModularFormsRing(n=7)(E6)
            True

            sage: from sage.modular.modform_hecketriangle.space import ModularForms, CuspForms
            sage: MF = ModularForms(n=5, k=6)
            sage: E6 = MF.E6()
            sage: E6 in MF
            True
            sage: ModularFormsRing(n=5, red_hom=True).E6() == E6
            True
            sage: CuspForms(n=5, k=12).E6() == E6
            True
            sage: MF.disp_prec(3)
            sage: E6
            1 - 37/(200*d)*q - 14663/(320000*d^2)*q^2 + O(q^3)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = ModularForms(n=5, k=6)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: ModularForms(n=5, k=6).E6().q_expansion(prec=5) == MFC(group=5, prec=7).E6_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=infinity, k=6).E6().q_expansion(prec=5) == MFC(group=infinity, prec=7).E6_ZZ()(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=5, k=6).E6().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).E6_ZZ().add_bigoh(5)
            True
            sage: ModularForms(n=infinity, k=6).E6().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).E6_ZZ().add_bigoh(5)
            True

            sage: ModularForms(n=infinity, k=6).E6()
            1 - 8*q - 248*q^2 - 1952*q^3 - 8440*q^4 + O(q^5)

            sage: ModularForms(k=6).f_i() == ModularForms(k=6).E6()
            True
            sage: ModularForms(k=6).E6()
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 + O(q^5)
        """
    @cached_method
    def Delta(self):
        """
        Return an analog of the Delta-function.

        It lies in the graded ring of ``self``. In case
        ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        It is a cusp form of weight `12` and is equal to ``d*(E4^3 -
        E6^2)`` or (in terms of the generators) ``d*x^(2*n-6)*(x^n -
        y^2)``.

        Note that ``Delta`` is also a cusp form for ``n=infinity``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, CuspFormsRing
            sage: MR = CuspFormsRing(n=7)
            sage: Delta = MR.Delta()
            sage: Delta in MR
            True
            sage: Delta
            f_rho^15*d - f_rho^8*f_i^2*d
            sage: QuasiMeromorphicModularFormsRing(n=7).Delta() == QuasiMeromorphicModularFormsRing(n=7)(Delta)
            True

            sage: from sage.modular.modform_hecketriangle.space import CuspForms, ModularForms
            sage: MF = CuspForms(n=5, k=12)
            sage: Delta = MF.Delta()
            sage: Delta in MF
            True
            sage: CuspFormsRing(n=5, red_hom=True).Delta() == Delta
            True
            sage: CuspForms(n=5, k=0).Delta() == Delta
            True
            sage: MF.disp_prec(3)
            sage: Delta
            q + 47/(200*d)*q^2 + O(q^3)

            sage: d = ModularForms(n=5).get_d()
            sage: Delta == (d*(ModularForms(n=5).E4()^3-ModularForms(n=5).E6()^2))
            True

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = CuspForms(n=5, k=12)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: CuspForms(n=5, k=12).Delta().q_expansion(prec=5) == (d*MFC(group=5, prec=7).Delta_ZZ()(q/d)).add_bigoh(5)
            True
            sage: CuspForms(n=infinity, k=12).Delta().q_expansion(prec=5) == (d*MFC(group=infinity, prec=7).Delta_ZZ()(q/d)).add_bigoh(5)
            True
            sage: CuspForms(n=5, k=12).Delta().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).Delta_ZZ().add_bigoh(5)
            True
            sage: CuspForms(n=infinity, k=12).Delta().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).Delta_ZZ().add_bigoh(5)
            True

            sage: CuspForms(n=infinity, k=12).Delta()
            q + 24*q^2 + 252*q^3 + 1472*q^4 + O(q^5)

            sage: CuspForms(k=12).f_inf() == CuspForms(k=12).Delta()
            True
            sage: CuspForms(k=12).Delta()
            q - 24*q^2 + 252*q^3 - 1472*q^4 + O(q^5)
        """
    @cached_method
    def E2(self):
        """
        Return the normalized quasi holomorphic Eisenstein series of weight `2`.

        It lies in a (quasi holomorphic) extension of the graded ring of ``self``.
        In case ``has_reduce_hom`` is ``True`` it is given as an element of
        the corresponding space of homogeneous elements.

        It is in particular also a generator of the graded ring of
        ``self`` and  the polynomial variable ``z`` exactly corresponds to ``E2``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import QuasiMeromorphicModularFormsRing, QuasiModularFormsRing, CuspFormsRing
            sage: MR = QuasiModularFormsRing(n=7)
            sage: E2 = MR.E2()
            sage: E2 in MR
            True
            sage: CuspFormsRing(n=7).E2() == E2
            True
            sage: E2
            E2
            sage: QuasiMeromorphicModularFormsRing(n=7).E2() == QuasiMeromorphicModularFormsRing(n=7)(E2)
            True

            sage: from sage.modular.modform_hecketriangle.space import QuasiModularForms, CuspForms
            sage: MF = QuasiModularForms(n=5, k=2)
            sage: E2 = MF.E2()
            sage: E2 in MF
            True
            sage: QuasiModularFormsRing(n=5, red_hom=True).E2() == E2
            True
            sage: CuspForms(n=5, k=12, ep=1).E2() == E2
            True
            sage: MF.disp_prec(3)
            sage: E2
            1 - 9/(200*d)*q - 369/(320000*d^2)*q^2 + O(q^3)

            sage: f_inf = MF.f_inf()
            sage: E2 == f_inf.derivative() / f_inf
            True

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: MF = QuasiModularForms(n=5, k=2)
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: QuasiModularForms(n=5, k=2).E2().q_expansion(prec=5) == MFC(group=5, prec=7).E2_ZZ()(q/d).add_bigoh(5)
            True
            sage: QuasiModularForms(n=infinity, k=2).E2().q_expansion(prec=5) == MFC(group=infinity, prec=7).E2_ZZ()(q/d).add_bigoh(5)
            True
            sage: QuasiModularForms(n=5, k=2).E2().q_expansion(fix_d=1, prec=5) == MFC(group=5, prec=7).E2_ZZ().add_bigoh(5)
            True
            sage: QuasiModularForms(n=infinity, k=2).E2().q_expansion(fix_d=1, prec=5) == MFC(group=infinity, prec=7).E2_ZZ().add_bigoh(5)
            True

            sage: QuasiModularForms(n=infinity, k=2).E2()
            1 - 8*q - 8*q^2 - 32*q^3 - 40*q^4 + O(q^5)

            sage: QuasiModularForms(k=2).E2()
            1 - 24*q - 72*q^2 - 96*q^3 - 168*q^4 + O(q^5)
        """
    @cached_method
    def EisensteinSeries(self, k=None):
        """
        Return the normalized Eisenstein series of weight ``k``.

        Only arithmetic groups or trivial weights (with corresponding
        one dimensional spaces) are supported.

        INPUT:

        - ``k`` -- a nonnegative even integer, namely the weight.
          If ``k`` is ``None`` (default) then the weight of ``self`` is chosen if
          ``self`` is homogeneous and the weight is possible, otherwise ``k``
          is set to `0`.

        OUTPUT:

        A modular form element lying in a (holomorphic) extension of
        the graded ring of ``self``. In case ``has_reduce_hom`` is
        ``True`` it is given as an element of the corresponding
        space of homogeneous elements.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.graded_ring import ModularFormsRing, CuspFormsRing
            sage: MR = ModularFormsRing()
            sage: MR.EisensteinSeries() == MR.one()
            True
            sage: E8 = MR.EisensteinSeries(k=8)
            sage: E8 in MR
            True
            sage: E8
            f_rho^2

            sage: from sage.modular.modform_hecketriangle.space import CuspForms, ModularForms
            sage: MF = ModularForms(n=4, k=12)
            sage: E12 = MF.EisensteinSeries()
            sage: E12 in MF
            True
            sage: CuspFormsRing(n=4, red_hom=True).EisensteinSeries(k=12).parent()
            ModularForms(n=4, k=12, ep=1) over Integer Ring
            sage: MF.disp_prec(4)
            sage: E12
            1 + 1008/691*q + 2129904/691*q^2 + 178565184/691*q^3 + O(q^4)

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor as MFC
            sage: d = MF.get_d()
            sage: q = MF.get_q()
            sage: ModularForms(n=3, k=2).EisensteinSeries().q_expansion(prec=5) == MFC(group=3, prec=7).EisensteinSeries_ZZ(k=2)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=3, k=4).EisensteinSeries().q_expansion(prec=5) == MFC(group=3, prec=7).EisensteinSeries_ZZ(k=4)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=3, k=6).EisensteinSeries().q_expansion(prec=5) == MFC(group=3, prec=7).EisensteinSeries_ZZ(k=6)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=3, k=8).EisensteinSeries().q_expansion(prec=5) == MFC(group=3, prec=7).EisensteinSeries_ZZ(k=8)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=4, k=2).EisensteinSeries().q_expansion(prec=5) == MFC(group=4, prec=7).EisensteinSeries_ZZ(k=2)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=4, k=4).EisensteinSeries().q_expansion(prec=5) == MFC(group=4, prec=7).EisensteinSeries_ZZ(k=4)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=4, k=6).EisensteinSeries().q_expansion(prec=5) == MFC(group=4, prec=7).EisensteinSeries_ZZ(k=6)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=4, k=8).EisensteinSeries().q_expansion(prec=5) == MFC(group=4, prec=7).EisensteinSeries_ZZ(k=8)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=6, k=2, ep=-1).EisensteinSeries().q_expansion(prec=5) == MFC(group=6, prec=7).EisensteinSeries_ZZ(k=2)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=6, k=4).EisensteinSeries().q_expansion(prec=5) == MFC(group=6, prec=7).EisensteinSeries_ZZ(k=4)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=6, k=6, ep=-1).EisensteinSeries().q_expansion(prec=5) == MFC(group=6, prec=7).EisensteinSeries_ZZ(k=6)(q/d).add_bigoh(5)
            True
            sage: ModularForms(n=6, k=8).EisensteinSeries().q_expansion(prec=5) == MFC(group=6, prec=7).EisensteinSeries_ZZ(k=8)(q/d).add_bigoh(5)
            True

            sage: ModularForms(n=3, k=12).EisensteinSeries()
            1 + 65520/691*q + 134250480/691*q^2 + 11606736960/691*q^3 + 274945048560/691*q^4 + O(q^5)
            sage: ModularForms(n=4, k=12).EisensteinSeries()
            1 + 1008/691*q + 2129904/691*q^2 + 178565184/691*q^3 + O(q^4)
            sage: ModularForms(n=6, k=12).EisensteinSeries()
            1 + 6552/50443*q + 13425048/50443*q^2 + 1165450104/50443*q^3 + 27494504856/50443*q^4 + O(q^5)
            sage: ModularForms(n=3, k=20).EisensteinSeries()
            1 + 13200/174611*q + 6920614800/174611*q^2 + 15341851377600/174611*q^3 + 3628395292275600/174611*q^4 + O(q^5)
            sage: ModularForms(n=4).EisensteinSeries(k=8)
            1 + 480/17*q + 69600/17*q^2 + 1050240/17*q^3 + 8916960/17*q^4 + O(q^5)
            sage: ModularForms(n=6).EisensteinSeries(k=20)
            1 + 264/206215591*q + 138412296/206215591*q^2 + 306852616488/206215591*q^3 + 72567905845512/206215591*q^4 + O(q^5)
        """
