from .hecke_triangle_groups import HeckeTriangleGroup as HeckeTriangleGroup
from sage.arith.misc import bernoulli as bernoulli, rising_factorial as rising_factorial, sigma as sigma
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.big_oh import O as O
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class MFSeriesConstructor(SageObject, UniqueRepresentation):
    """
    Constructor for the Fourier expansion of some
    (specific, basic) modular forms.

    The constructor is used by forms elements in case
    their Fourier expansion is needed or requested.
    """
    @staticmethod
    def __classcall__(cls, group=..., prec=...):
        """
        Return a (cached) instance with canonical parameters.

        .. NOTE::

            For each choice of group and precision the constructor is
            cached (only) once. Further calculations with different
            base rings and possibly numerical parameters are based on
            the same cached instance.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor() == MFSeriesConstructor(3, 10)
            True
            sage: MFSeriesConstructor(group=4).hecke_n()
            4
            sage: MFSeriesConstructor(group=5, prec=12).prec()
            12
        """
    def __init__(self, group, prec) -> None:
        """
        Constructor for the Fourier expansion of some
        (specific, basic) modular forms.

        INPUT:

        - ``group`` -- a Hecke triangle group (default: HeckeTriangleGroup(3))

        - ``prec`` -- integer (default: 10), the default precision used in
          calculations in the LaurentSeriesRing or PowerSeriesRing

        OUTPUT: the constructor for Fourier expansion with the specified settings

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFC = MFSeriesConstructor()
            sage: MFC
            Power series constructor for Hecke modular forms for n=3 with (basic series) precision 10
            sage: MFC.group()
            Hecke triangle group for n = 3
            sage: MFC.prec()
            10
            sage: MFC._series_ring
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=4)
            Power series constructor for Hecke modular forms for n=4 with (basic series) precision 10
            sage: MFSeriesConstructor(group=5, prec=12)
            Power series constructor for Hecke modular forms for n=5 with (basic series) precision 12
            sage: MFSeriesConstructor(group=infinity)
            Power series constructor for Hecke modular forms for n=+Infinity with (basic series) precision 10
        """
    def group(self):
        """
        Return the (Hecke triangle) group of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(group=4).group()
            Hecke triangle group for n = 4
        """
    def hecke_n(self):
        """
        Return the parameter ``n`` of the (Hecke triangle) group of ``self``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(group=4).hecke_n()
            4
        """
    def prec(self):
        """
        Return the used default precision for the PowerSeriesRing or LaurentSeriesRing.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(group=5).prec()
            10
            sage: MFSeriesConstructor(group=5, prec=20).prec()
            20
        """
    @cached_method
    def J_inv_ZZ(self):
        """
        Return the rational Fourier expansion of ``J_inv``,
        where the parameter ``d`` is replaced by ``1``.

        This is the main function used to determine all Fourier expansions!

        .. NOTE::

            The Fourier expansion of ``J_inv`` for ``d!=1``
            is given by ``J_inv_ZZ(q/d)``.

        .. TODO::

            The functions that are used in this implementation are
            products of hypergeometric series with other, elementary,
            functions.  Implement them and clean up this representation.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).J_inv_ZZ()
            q^-1 + 31/72 + 1823/27648*q + O(q^2)
            sage: MFSeriesConstructor(group=5, prec=3).J_inv_ZZ()
            q^-1 + 79/200 + 42877/640000*q + O(q^2)
            sage: MFSeriesConstructor(group=5, prec=3).J_inv_ZZ().parent()
            Laurent Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).J_inv_ZZ()
            q^-1 + 3/8 + 69/1024*q + O(q^2)
        """
    @cached_method
    def f_rho_ZZ(self):
        """
        Return the rational Fourier expansion of ``f_rho``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``f_rho`` for ``d!=1``
            is given by ``f_rho_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).f_rho_ZZ()
            1 + 5/36*q + 5/6912*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).f_rho_ZZ()
            1 + 7/100*q + 21/160000*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).f_rho_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).f_rho_ZZ()
            1
        """
    @cached_method
    def f_i_ZZ(self):
        """
        Return the rational Fourier expansion of ``f_i``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``f_i`` for ``d!=1``
            is given by ``f_i_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).f_i_ZZ()
            1 - 7/24*q - 77/13824*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).f_i_ZZ()
            1 - 13/40*q - 351/64000*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).f_i_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).f_i_ZZ()
            1 - 3/8*q + 3/512*q^2 + O(q^3)
        """
    @cached_method
    def f_inf_ZZ(self):
        """
        Return the rational Fourier expansion of ``f_inf``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``f_inf`` for ``d!=1``
            is given by ``d*f_inf_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).f_inf_ZZ()
            q - 1/72*q^2 + 7/82944*q^3 + O(q^4)
            sage: MFSeriesConstructor(group=5, prec=3).f_inf_ZZ()
            q - 9/200*q^2 + 279/640000*q^3 + O(q^4)
            sage: MFSeriesConstructor(group=5, prec=3).f_inf_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).f_inf_ZZ()
            q - 1/8*q^2 + 7/1024*q^3 + O(q^4)
        """
    @cached_method
    def G_inv_ZZ(self):
        """
        Return the rational Fourier expansion of ``G_inv``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``G_inv`` for ``d!=1``
            is given by ``d*G_inv_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(group=4, prec=3).G_inv_ZZ()
            q^-1 - 3/32 - 955/16384*q + O(q^2)
            sage: MFSeriesConstructor(group=8, prec=3).G_inv_ZZ()
            q^-1 - 15/128 - 15139/262144*q + O(q^2)
            sage: MFSeriesConstructor(group=8, prec=3).G_inv_ZZ().parent()
            Laurent Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).G_inv_ZZ()
            q^-1 - 1/8 - 59/1024*q + O(q^2)
        """
    @cached_method
    def E4_ZZ(self):
        """
        Return the rational Fourier expansion of ``E_4``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``E4`` for ``d!=1``
            is given by ``E4_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).E4_ZZ()
            1 + 5/36*q + 5/6912*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).E4_ZZ()
            1 + 21/100*q + 483/32000*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).E4_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).E4_ZZ()
            1 + 1/4*q + 7/256*q^2 + O(q^3)
        """
    @cached_method
    def E6_ZZ(self):
        """
        Return the rational Fourier expansion of ``E_6``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``E6`` for ``d!=1``
            is given by ``E6_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).E6_ZZ()
            1 - 7/24*q - 77/13824*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).E6_ZZ()
            1 - 37/200*q - 14663/320000*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).E6_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).E6_ZZ()
            1 - 1/8*q - 31/512*q^2 + O(q^3)
        """
    @cached_method
    def Delta_ZZ(self):
        """
        Return the rational Fourier expansion of ``Delta``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``Delta`` for ``d!=1``
            is given by ``d*Delta_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).Delta_ZZ()
            q - 1/72*q^2 + 7/82944*q^3 + O(q^4)
            sage: MFSeriesConstructor(group=5, prec=3).Delta_ZZ()
            q + 47/200*q^2 + 11367/640000*q^3 + O(q^4)
            sage: MFSeriesConstructor(group=5, prec=3).Delta_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).Delta_ZZ()
            q + 3/8*q^2 + 63/1024*q^3 + O(q^4)
        """
    @cached_method
    def E2_ZZ(self):
        """
        Return the rational Fourier expansion of ``E2``,
        where the parameter ``d`` is replaced by ``1``.

        .. NOTE::

            The Fourier expansion of ``E2`` for ``d!=1``
            is given by ``E2_ZZ(q/d)``.

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFSeriesConstructor(prec=3).E2_ZZ()
            1 - 1/72*q - 1/41472*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).E2_ZZ()
            1 - 9/200*q - 369/320000*q^2 + O(q^3)
            sage: MFSeriesConstructor(group=5, prec=3).E2_ZZ().parent()
            Power Series Ring in q over Rational Field

            sage: MFSeriesConstructor(group=infinity, prec=3).E2_ZZ()
            1 - 1/8*q - 1/512*q^2 + O(q^3)
        """
    @cached_method
    def EisensteinSeries_ZZ(self, k):
        """
        Return the rational Fourier expansion of the normalized Eisenstein series
        of weight ``k``, where the parameter ``d`` is replaced by ``1``.

        Only arithmetic groups with ``n < infinity`` are supported!

        .. NOTE::

            THe Fourier expansion of the series is given by ``EisensteinSeries_ZZ(q/d)``.

        INPUT:

        - ``k`` -- a nonnegative even integer, namely the weight

        EXAMPLES::

            sage: from sage.modular.modform_hecketriangle.series_constructor import MFSeriesConstructor
            sage: MFC = MFSeriesConstructor(prec=6)
            sage: MFC.EisensteinSeries_ZZ(k=0)
            1
            sage: MFC.EisensteinSeries_ZZ(k=2)
            1 - 1/72*q - 1/41472*q^2 - 1/53747712*q^3 - 7/371504185344*q^4 - 1/106993205379072*q^5 + O(q^6)
            sage: MFC.EisensteinSeries_ZZ(k=6)
            1 - 7/24*q - 77/13824*q^2 - 427/17915904*q^3 - 7399/123834728448*q^4 - 3647/35664401793024*q^5 + O(q^6)
            sage: MFC.EisensteinSeries_ZZ(k=12)
            1 + 455/8292*q + 310765/4776192*q^2 + 20150585/6189944832*q^3 + 1909340615/42784898678784*q^4 + 3702799555/12322050819489792*q^5 + O(q^6)
            sage: MFC.EisensteinSeries_ZZ(k=12).parent()
            Power Series Ring in q over Rational Field

            sage: MFC = MFSeriesConstructor(group=4, prec=5)
            sage: MFC.EisensteinSeries_ZZ(k=2)
            1 - 1/32*q - 5/8192*q^2 - 1/524288*q^3 - 13/536870912*q^4 + O(q^5)
            sage: MFC.EisensteinSeries_ZZ(k=4)
            1 + 3/16*q + 39/4096*q^2 + 21/262144*q^3 + 327/268435456*q^4 + O(q^5)
            sage: MFC.EisensteinSeries_ZZ(k=6)
            1 - 7/32*q - 287/8192*q^2 - 427/524288*q^3 - 9247/536870912*q^4 + O(q^5)
            sage: MFC.EisensteinSeries_ZZ(k=12)
            1 + 63/11056*q + 133119/2830336*q^2 + 2790081/181141504*q^3 + 272631807/185488900096*q^4 + O(q^5)

            sage: MFC = MFSeriesConstructor(group=6, prec=5)
            sage: MFC.EisensteinSeries_ZZ(k=2)
            1 - 1/18*q - 1/648*q^2 - 7/209952*q^3 - 7/22674816*q^4 + O(q^5)
            sage: MFC.EisensteinSeries_ZZ(k=4)
            1 + 2/9*q + 1/54*q^2 + 37/52488*q^3 + 73/5668704*q^4 + O(q^5)
            sage: MFC.EisensteinSeries_ZZ(k=6)
            1 - 1/6*q - 11/216*q^2 - 271/69984*q^3 - 1057/7558272*q^4 + O(q^5)
            sage: MFC.EisensteinSeries_ZZ(k=12)
            1 + 182/151329*q + 62153/2723922*q^2 + 16186807/882550728*q^3 + 381868123/95315478624*q^4 + O(q^5)
        """
