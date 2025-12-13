from sage.misc.misc_c import prod as prod
from sage.modules.free_module import span as span
from sage.rings.cc import CC as CC
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class Lseries(SageObject):
    """
    Base class for `L`-series attached to modular abelian varieties.

    This is a common base class for complex and `p`-adic `L`-series
    of modular abelian varieties.
    """
    def __init__(self, abvar) -> None:
        """
        Called when creating an `L`-series.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        EXAMPLES::

            sage: J0(11).lseries()
            Complex L-series attached to Abelian variety J0(11) of dimension 1
            sage: J0(11).padic_lseries(7)
            7-adic L-series attached to Abelian variety J0(11) of dimension 1
        """
    def abelian_variety(self):
        """
        Return the abelian variety that this `L`-series is attached to.

        OUTPUT: a modular abelian variety

        EXAMPLES::

            sage: J0(11).padic_lseries(7).abelian_variety()
            Abelian variety J0(11) of dimension 1
        """

class Lseries_complex(Lseries):
    """
    A complex `L`-series attached to a modular abelian variety.

    EXAMPLES::

        sage: A = J0(37)
        sage: A.lseries()
        Complex L-series attached to Abelian variety J0(37) of dimension 2
    """
    def __call__(self, s, prec: int = 53):
        """
        Evaluate this complex `L`-series at `s`.

        INPUT:

        - ``s`` -- complex number

        - ``prec`` -- integer (default: 53); the number of bits of precision
          used in computing the lseries of the newforms

        OUTPUT: a complex number L(A, s)

        EXAMPLES::

            sage: L = J0(23).lseries()
            sage: L(1)                                                                  # needs sage.symbolic
            0.248431866590600
            sage: L(1, prec=100)                                                        # needs sage.symbolic
            0.24843186659059968120725033931

            sage: L = J0(389)[0].lseries()
            sage: L(1)                          # abstol 1e-10          # long time (2s), needs sage.symbolic
            -1.33139759782370e-19
            sage: L(1, prec=100)                # abstol 1e-20          # long time (2s), needs sage.symbolic
            6.0129758648142797032650287762e-39
            sage: L.rational_part()
            0

            sage: L = J1(23)[0].lseries()
            sage: L(1)                                                                  # needs sage.symbolic
            0.248431866590600

            sage: J = J0(11) * J1(11)
            sage: J.lseries()(1)                                                        # needs sage.symbolic
            0.0644356903227915

            sage: L = JH(17,[2]).lseries()
            sage: L(1)                                                                  # needs sage.symbolic
            0.386769938387780
        """
    def __eq__(self, other):
        """
        Compare this complex `L`-series to another one.

        INPUT:

        - ``other`` -- object

        OUTPUT: boolean

        EXAMPLES::

            sage: L = J0(37)[0].lseries()
            sage: M = J0(37)[1].lseries()
            sage: L == M
            False
            sage: L == L
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        INPUT:

        - ``other`` -- object

        OUTPUT: boolean

        EXAMPLES::

            sage: L = J0(37)[0].lseries()
            sage: M = J0(37)[1].lseries()
            sage: L != M
            True
            sage: L != L
            False
        """
    def vanishes_at_1(self):
        """
        Return ``True`` if `L(1)=0` and return ``False`` otherwise.

        OUTPUT: boolean

        EXAMPLES:

        Numerically, the `L`-series for `J_0(389)` appears to vanish
        at 1.  This is confirmed by this algebraic computation::

            sage: L = J0(389)[0].lseries(); L
            Complex L-series attached to Simple abelian subvariety 389a(1,389) of dimension 1 of J0(389)
            sage: L(1) # long time (2s) abstol 1e-10
            -1.33139759782370e-19
            sage: L.vanishes_at_1()
            True

        Numerically, one might guess that the `L`-series for `J_1(23)`
        and `J_1(31)` vanish at 1.  This algebraic computation shows
        otherwise::

            sage: L = J1(23).lseries(); L
            Complex L-series attached to Abelian variety J1(23) of dimension 12
            sage: L(1)  # long time (about 3 s)
            0.0001295198...
            sage: L.vanishes_at_1()
            False
            sage: abs(L(1, prec=100)- 0.00012951986142702571478817757148) < 1e-32  # long time (about 3 s)
            True

            sage: L = J1(31).lseries(); L
            Complex L-series attached to Abelian variety J1(31) of dimension 26
            sage: abs(L(1) - 3.45014267547611e-7) < 1e-15  # long time (about 8 s)
            True
            sage: L.vanishes_at_1()  # long time (about 6 s)
            False
        """
    def rational_part(self):
        """
        Return the rational part of this `L`-function at the central critical
        value 1.

        OUTPUT: a rational number

        EXAMPLES::

            sage: A, B = J0(43).decomposition()
            sage: A.lseries().rational_part()
            0
            sage: B.lseries().rational_part()
            2/7
        """
    lratio = rational_part

class Lseries_padic(Lseries):
    """
    A `p`-adic `L`-series attached to a modular abelian variety.
    """
    def __init__(self, abvar, p) -> None:
        """
        Create a `p`-adic `L`-series.

        EXAMPLES::

            sage: J0(37)[0].padic_lseries(389)
            389-adic L-series attached to Simple abelian subvariety 37a(1,37) of dimension 1 of J0(37)
        """
    def __eq__(self, other):
        """
        Compare this `p`-adic `L`-series to another one.

        First the abelian varieties are compared; if they are the same,
        then the primes are compared.

        INPUT:

        - ``other`` -- object

        OUTPUT: boolean

        EXAMPLES::

            sage: L = J0(37)[0].padic_lseries(5)
            sage: M = J0(37)[1].padic_lseries(5)
            sage: K = J0(37)[0].padic_lseries(3)
            sage: L == K
            False
            sage: L == M
            False
            sage: L == L
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        INPUT:

        - ``other`` -- object

        OUTPUT: boolean

        EXAMPLES::

            sage: L = J0(37)[0].padic_lseries(5)
            sage: M = J0(37)[1].padic_lseries(5)
            sage: K = J0(37)[0].padic_lseries(3)
            sage: L != K
            True
            sage: L != M
            True
            sage: L != L
            False
        """
    def prime(self):
        """
        Return the prime `p` of this `p`-adic `L`-series.

        EXAMPLES::

            sage: J0(11).padic_lseries(7).prime()
            7
        """
    def power_series(self, n: int = 2, prec: int = 5) -> None:
        """
        Return the `n`-th approximation to this `p`-adic `L`-series as
        a power series in `T`.

        Each coefficient is a `p`-adic number
        whose precision is provably correct.

        NOTE: This is not yet implemented.

        EXAMPLES::

            sage: L = J0(37)[0].padic_lseries(5)
            sage: L.power_series()
            Traceback (most recent call last):
            ...
            NotImplementedError
            sage: L.power_series(3,7)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
