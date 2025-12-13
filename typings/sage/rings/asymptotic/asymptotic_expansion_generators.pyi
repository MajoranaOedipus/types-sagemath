from _typeshed import Incomplete
from sage.misc.defaults import series_precision as series_precision
from sage.misc.superseded import experimental as experimental
from sage.structure.sage_object import SageObject as SageObject

class AsymptoticExpansionGenerators(SageObject):
    '''
    A collection of constructors for several common asymptotic expansions.

    A list of all asymptotic expansions in this database is available via tab
    completion. Type "``asymptotic_expansions.``" and then hit tab to see which
    expansions are available.

    The asymptotic expansions currently in this class include:

    - :meth:`~HarmonicNumber`
    - :meth:`~Stirling`
    - :meth:`~log_Stirling`
    - :meth:`~Binomial_kn_over_n`
    - :meth:`~SingularityAnalysis`
    - :meth:`~ImplicitExpansion`
    - :meth:`~ImplicitExpansionPeriodicPart`
    - :meth:`~InverseFunctionAnalysis`
    '''
    @staticmethod
    def Stirling(var, precision=None, skip_constant_factor: bool = False):
        """
        Return Stirling's approximation formula for factorials.

        INPUT:

        - ``var`` -- string for the variable name

        - ``precision`` -- (default: ``None``) integer `\\ge 3`. If ``None``, then
          the default precision of the asymptotic ring is used.

        - ``skip_constant_factor`` -- boolean (default: ``False``); if set,
          then the constant factor `\\sqrt{2\\pi}` is left out.
          As a consequence, the coefficient ring of the output changes
          from ``Symbolic Constants Subring`` (if ``False``) to
          ``Rational Field`` (if ``True``).

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: asymptotic_expansions.Stirling('n', precision=5)
            sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(1/2) +
            1/12*sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(-1/2) +
            1/288*sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(-3/2) +
            O(e^(n*log(n))*(e^n)^(-1)*n^(-5/2))
            sage: _.parent()
            Asymptotic Ring <(e^(n*log(n)))^QQ * (e^n)^QQ * n^QQ * log(n)^QQ>
            over Symbolic Constants Subring

        .. SEEALSO::

            :meth:`log_Stirling`,
            :meth:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticExpansion.factorial`.

        TESTS::

            sage: expansion = asymptotic_expansions.Stirling('n', precision=5)
            sage: n = expansion.parent().gen()
            sage: expansion.compare_with_values(n, lambda x: x.factorial(), [5, 10, 20])  # rel tol 1e-6
            [(5, 0.00675841118?), (10, 0.0067589306?), (20, 0.006744925?)]
            sage: asymptotic_expansions.Stirling('n', precision=5,
            ....:                                skip_constant_factor=True)
            e^(n*log(n))*(e^n)^(-1)*n^(1/2) +
            1/12*e^(n*log(n))*(e^n)^(-1)*n^(-1/2) +
            1/288*e^(n*log(n))*(e^n)^(-1)*n^(-3/2) +
            O(e^(n*log(n))*(e^n)^(-1)*n^(-5/2))
            sage: _.parent()
            Asymptotic Ring <(e^(n*log(n)))^QQ * (e^n)^QQ * n^QQ * log(n)^QQ>
            over Rational Field
            sage: asymptotic_expansions.Stirling('m', precision=4)
            sqrt(2)*sqrt(pi)*e^(m*log(m))*(e^m)^(-1)*m^(1/2) +
            O(e^(m*log(m))*(e^m)^(-1)*m^(-1/2))
            sage: asymptotic_expansions.Stirling('m', precision=3)
            O(e^(m*log(m))*(e^m)^(-1)*m^(1/2))
            sage: asymptotic_expansions.Stirling('m', precision=2)
            Traceback (most recent call last):
            ...
            ValueError: precision must be at least 3

        Check that :issue:`20066` is resolved::

            sage: set_series_precision(5)
            sage: asymptotic_expansions.Stirling('n')
            sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(1/2) +
            ... + O(e^(n*log(n))*(e^n)^(-1)*n^(-5/2))
            sage: set_series_precision(20)  # restore series precision default
        """
    @staticmethod
    def log_Stirling(var, precision=None, skip_constant_summand: bool = False):
        """
        Return the logarithm of Stirling's approximation formula
        for factorials.

        INPUT:

        - ``var`` -- string for the variable name

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        - ``skip_constant_summand`` -- boolean (default: ``False``); if set,
          then the constant summand `\\log(2\\pi)/2` is left out.
          As a consequence, the coefficient ring of the output changes
          from ``Symbolic Constants Subring`` (if ``False``) to
          ``Rational Field`` (if ``True``).

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: asymptotic_expansions.log_Stirling('n', precision=7)
            n*log(n) - n + 1/2*log(n) + 1/2*log(2*pi) + 1/12*n^(-1)
            - 1/360*n^(-3) + 1/1260*n^(-5) + O(n^(-7))

        .. SEEALSO::

            :meth:`Stirling`,
            :meth:`~sage.rings.asymptotic.asymptotic_ring.AsymptoticExpansion.factorial`.

        TESTS::

            sage: expansion = asymptotic_expansions.log_Stirling('n', precision=7)
            sage: n = expansion.parent().gen()
            sage: expansion.compare_with_values(n, lambda x: x.factorial().log(), [5, 10, 20])  # rel tol 1e-6
            [(5, 0.000564287?), (10, 0.0005870?), (20, 0.0006?)]
            sage: asymptotic_expansions.log_Stirling('n')
            n*log(n) - n + 1/2*log(n) + 1/2*log(2*pi) + 1/12*n^(-1)
            - 1/360*n^(-3) + 1/1260*n^(-5) - 1/1680*n^(-7) + 1/1188*n^(-9)
            - 691/360360*n^(-11) + 1/156*n^(-13) - 3617/122400*n^(-15)
            + 43867/244188*n^(-17) - 174611/125400*n^(-19) + 77683/5796*n^(-21)
            - 236364091/1506960*n^(-23) + 657931/300*n^(-25)
            - 3392780147/93960*n^(-27) + 1723168255201/2492028*n^(-29)
            - 7709321041217/505920*n^(-31) + O(n^(-33))
            sage: _.parent()
            Asymptotic Ring <n^ZZ * log(n)^ZZ> over Symbolic Constants Subring

        ::

            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=7, skip_constant_summand=True)
            n*log(n) - n + 1/2*log(n) + 1/12*n^(-1) - 1/360*n^(-3) +
            1/1260*n^(-5) + O(n^(-7))
            sage: _.parent()
            Asymptotic Ring <n^ZZ * log(n)^ZZ> over Rational Field
            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=0)
            O(n*log(n))
            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=1)
            n*log(n) + O(n)
            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=2)
            n*log(n) - n + O(log(n))
            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=3)
            n*log(n) - n + 1/2*log(n) + O(1)
            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=4)
            n*log(n) - n + 1/2*log(n) + 1/2*log(2*pi) + O(n^(-1))
            sage: asymptotic_expansions.log_Stirling(
            ....:     'n', precision=5)
            n*log(n) - n + 1/2*log(n) + 1/2*log(2*pi) + 1/12*n^(-1)
            + O(n^(-3))
            sage: asymptotic_expansions.log_Stirling(
            ....:     'm', precision=7, skip_constant_summand=True)
            m*log(m) - m + 1/2*log(m) + 1/12*m^(-1) - 1/360*m^(-3) +
            1/1260*m^(-5) + O(m^(-7))
        """
    @staticmethod
    def HarmonicNumber(var, precision=None, skip_constant_summand: bool = False):
        """
        Return the asymptotic expansion of a harmonic number.

        INPUT:

        - ``var`` -- string for the variable name

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        - ``skip_constant_summand`` -- boolean (default: ``False``); if set,
          then the constant summand ``euler_gamma`` is left out.
          As a consequence, the coefficient ring of the output changes
          from ``Symbolic Constants Subring`` (if ``False``) to
          ``Rational Field`` (if ``True``).

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: asymptotic_expansions.HarmonicNumber('n', precision=5)
            log(n) + euler_gamma + 1/2*n^(-1) - 1/12*n^(-2) + 1/120*n^(-4) + O(n^(-6))

        TESTS::

            sage: ex = asymptotic_expansions.HarmonicNumber('n', precision=5)
            sage: n = ex.parent().gen()
            sage: ex.compare_with_values(n,                      # rel tol 1e-6
            ....:      lambda x: sum(1/k for k in srange(1, x+1)), [5, 10, 20])
            [(5, 0.0038125360?), (10, 0.00392733?), (20, 0.0039579?)]
            sage: asymptotic_expansions.HarmonicNumber('n')
            log(n) + euler_gamma + 1/2*n^(-1) - 1/12*n^(-2) + 1/120*n^(-4)
            - 1/252*n^(-6) + 1/240*n^(-8) - 1/132*n^(-10)
            + 691/32760*n^(-12) - 1/12*n^(-14) + 3617/8160*n^(-16)
            - 43867/14364*n^(-18) + 174611/6600*n^(-20) - 77683/276*n^(-22)
            + 236364091/65520*n^(-24) - 657931/12*n^(-26)
            + 3392780147/3480*n^(-28) - 1723168255201/85932*n^(-30)
            + 7709321041217/16320*n^(-32)
            - 151628697551/12*n^(-34) + O(n^(-36))
            sage: _.parent()
            Asymptotic Ring <n^ZZ * log(n)^ZZ> over Symbolic Constants Subring

        ::

            sage: asymptotic_expansions.HarmonicNumber(
            ....:     'n', precision=5, skip_constant_summand=True)
            log(n) + 1/2*n^(-1) - 1/12*n^(-2) + 1/120*n^(-4) + O(n^(-6))
            sage: _.parent()
            Asymptotic Ring <n^ZZ * log(n)^ZZ> over Rational Field
            sage: for p in range(5):
            ....:     print(asymptotic_expansions.HarmonicNumber(
            ....:         'n', precision=p))
            O(log(n))
            log(n) + O(1)
            log(n) + euler_gamma + O(n^(-1))
            log(n) + euler_gamma + 1/2*n^(-1) + O(n^(-2))
            log(n) + euler_gamma + 1/2*n^(-1) - 1/12*n^(-2) + O(n^(-4))
            sage: asymptotic_expansions.HarmonicNumber('m', precision=5)
            log(m) + euler_gamma + 1/2*m^(-1) - 1/12*m^(-2) + 1/120*m^(-4) + O(m^(-6))
        """
    @staticmethod
    def Binomial_kn_over_n(var, k, precision=None, skip_constant_factor: bool = False):
        """
        Return the asymptotic expansion of the binomial coefficient
        `kn` choose `n`.

        INPUT:

        - ``var`` -- string for the variable name

        - ``k`` -- a number or symbolic constant

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        - ``skip_constant_factor`` -- boolean (default: ``False``); if set,
          then the constant factor `\\sqrt{k/(2\\pi(k-1))}` is left out.
          As a consequence, the coefficient ring of the output changes
          from ``Symbolic Constants Subring`` (if ``False``) to
          ``Rational Field`` (if ``True``).

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: asymptotic_expansions.Binomial_kn_over_n('n', k=2, precision=3)
            1/sqrt(pi)*4^n*n^(-1/2)
            - 1/8/sqrt(pi)*4^n*n^(-3/2)
            + 1/128/sqrt(pi)*4^n*n^(-5/2)
            + O(4^n*n^(-7/2))
            sage: _.parent()
            Asymptotic Ring <QQ^n * n^QQ> over Symbolic Constants Subring

        ::

            sage: asymptotic_expansions.Binomial_kn_over_n('n', k=3, precision=3)
            1/2*sqrt(3)/sqrt(pi)*(27/4)^n*n^(-1/2)
            - 7/144*sqrt(3)/sqrt(pi)*(27/4)^n*n^(-3/2)
            + 49/20736*sqrt(3)/sqrt(pi)*(27/4)^n*n^(-5/2)
            + O((27/4)^n*n^(-7/2))

        ::

            sage: asymptotic_expansions.Binomial_kn_over_n('n', k=7/5, precision=3)
            1/2*sqrt(7)/sqrt(pi)*(7/10*7^(2/5)*2^(3/5))^n*n^(-1/2)
            - 13/112*sqrt(7)/sqrt(pi)*(7/10*7^(2/5)*2^(3/5))^n*n^(-3/2)
            + 169/12544*sqrt(7)/sqrt(pi)*(7/10*7^(2/5)*2^(3/5))^n*n^(-5/2)
            + O((7/10*7^(2/5)*2^(3/5))^n*n^(-7/2))
            sage: _.parent()
            Asymptotic Ring <(Symbolic Constants Subring)^n * n^QQ>
            over Symbolic Constants Subring

        TESTS::

            sage: expansion = asymptotic_expansions.Binomial_kn_over_n('n', k=7/5, precision=3)
            sage: n = expansion.parent().gen()
            sage: expansion.compare_with_values(n, lambda x: binomial(7/5*x, x), [5, 10, 20])  # rel tol 1e-6
            [(5, -0.0287383845047?), (10, -0.030845971026?), (20, -0.03162833549?)]
            sage: asymptotic_expansions.Binomial_kn_over_n(
            ....:     'n', k=5, precision=3, skip_constant_factor=True)
            (3125/256)^n*n^(-1/2)
            - 7/80*(3125/256)^n*n^(-3/2)
            + 49/12800*(3125/256)^n*n^(-5/2)
            + O((3125/256)^n*n^(-7/2))
            sage: _.parent()
            Asymptotic Ring <QQ^n * n^QQ> over Rational Field
            sage: asymptotic_expansions.Binomial_kn_over_n(
            ....:     'n', k=4, precision=1, skip_constant_factor=True)
            (256/27)^n*n^(-1/2) + O((256/27)^n*n^(-3/2))

        ::

            sage: S = asymptotic_expansions.Stirling('n', precision=5)
            sage: n = S.parent().gen()
            sage: all(  # long time
            ....:     SR(asymptotic_expansions.Binomial_kn_over_n(
            ....:         'n', k=k, precision=3)).canonicalize_radical() ==
            ....:     SR(S.subs(n=k*n) / (S.subs(n=(k-1)*n) * S)).canonicalize_radical()
            ....:     for k in [2, 3, 4])
            True

        Check that :issue:`20066` is resolved::

            sage: set_series_precision(3)
            sage: asymptotic_expansions.Binomial_kn_over_n('n', k=2)
            1/sqrt(pi)*4^n*n^(-1/2) - 1/8/sqrt(pi)*4^n*n^(-3/2) + ... + O(4^n*n^(-7/2))
            sage: set_series_precision(20)  # restore series precision default
        """
    @staticmethod
    def SingularityAnalysis(var, zeta: int = 1, alpha: int = 0, beta: int = 0, delta: int = 0, precision=None, normalized: bool = True):
        """
        Return the asymptotic expansion of the coefficients of
        a power series with specified pole and logarithmic singularity.

        More precisely, this extracts the `n`-th coefficient

        .. MATH::

            [z^n] \\left(\\frac{1}{1-z/\\zeta}\\right)^\\alpha
            \\left(\\frac{1}{z/\\zeta} \\log \\frac{1}{1-z/\\zeta}\\right)^\\beta
            \\left(\\frac{1}{z/\\zeta} \\log
            \\left(\\frac{1}{z/\\zeta} \\log \\frac{1}{1-z/\\zeta}\\right)\\right)^\\delta

        (if ``normalized=True``, the default) or

        .. MATH::

            [z^n] \\left(\\frac{1}{1-z/\\zeta}\\right)^\\alpha
            \\left(\\log \\frac{1}{1-z/\\zeta}\\right)^\\beta
            \\left(\\log
            \\left(\\frac{1}{z/\\zeta} \\log \\frac{1}{1-z/\\zeta}\\right)\\right)^\\delta

        (if ``normalized=False``).

        INPUT:

        - ``var`` -- string for the variable name

        - ``zeta`` -- (default: `1`) the location of the singularity

        - ``alpha`` -- (default: `0`) the pole order of the singularity

        - ``beta`` -- (default: `0`) the order of the logarithmic singularity

        - ``delta`` -- (default: `0`) the order of the log-log singularity;
          not yet implemented for ``delta != 0``

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        - ``normalized`` -- boolean (default: ``True``); see above

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: asymptotic_expansions.SingularityAnalysis('n', alpha=1)
            1
            sage: asymptotic_expansions.SingularityAnalysis('n', alpha=2)
            n + 1
            sage: asymptotic_expansions.SingularityAnalysis('n', alpha=3)
            1/2*n^2 + 3/2*n + 1
            sage: _.parent()
            Asymptotic Ring <n^ZZ> over Rational Field

        ::

            sage: asymptotic_expansions.SingularityAnalysis('n', alpha=-3/2,
            ....:     precision=3)
            3/4/sqrt(pi)*n^(-5/2)
            + 45/32/sqrt(pi)*n^(-7/2)
            + 1155/512/sqrt(pi)*n^(-9/2)
            + O(n^(-11/2))
            sage: asymptotic_expansions.SingularityAnalysis('n', alpha=-1/2,
            ....:     precision=3)
            -1/2/sqrt(pi)*n^(-3/2)
            - 3/16/sqrt(pi)*n^(-5/2)
            - 25/256/sqrt(pi)*n^(-7/2)
            + O(n^(-9/2))
            sage: asymptotic_expansions.SingularityAnalysis('n', alpha=1/2,
            ....:     precision=4)
            1/sqrt(pi)*n^(-1/2)
            - 1/8/sqrt(pi)*n^(-3/2)
            + 1/128/sqrt(pi)*n^(-5/2)
            + 5/1024/sqrt(pi)*n^(-7/2)
            + O(n^(-9/2))
            sage: _.parent()
            Asymptotic Ring <n^QQ> over Symbolic Constants Subring

        ::

            sage: S = SR.subring(rejecting_variables=('n',))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=S.var('a'),
            ....:     precision=4).map_coefficients(lambda c: c.factor())
            1/gamma(a)*n^(a - 1)
            + (1/2*(a - 1)*a/gamma(a))*n^(a - 2)
            + (1/24*(3*a - 1)*(a - 1)*(a - 2)*a/gamma(a))*n^(a - 3)
            + (1/48*(a - 1)^2*(a - 2)*(a - 3)*a^2/gamma(a))*n^(a - 4)
            + O(n^(a - 5))
            sage: _.parent()
            Asymptotic Ring <n^(Symbolic Subring rejecting the variable n)>
            over Symbolic Subring rejecting the variable n

        ::

            sage: ae = asymptotic_expansions.SingularityAnalysis('n',
            ....:          alpha=1/2, beta=1, precision=4); ae
            1/sqrt(pi)*n^(-1/2)*log(n) + ((euler_gamma + 2*log(2))/sqrt(pi))*n^(-1/2)
            - 5/8/sqrt(pi)*n^(-3/2)*log(n) + (1/8*(3*euler_gamma + 6*log(2) - 8)/sqrt(pi)
            - (euler_gamma + 2*log(2) - 2)/sqrt(pi))*n^(-3/2) + O(n^(-5/2)*log(n))
            sage: n = ae.parent().gen()
            sage: ae.subs(n=n-1).map_coefficients(lambda x: x.canonicalize_radical())
            1/sqrt(pi)*n^(-1/2)*log(n)
            + ((euler_gamma + 2*log(2))/sqrt(pi))*n^(-1/2)
            - 1/8/sqrt(pi)*n^(-3/2)*log(n)
            + (-1/8*(euler_gamma + 2*log(2))/sqrt(pi))*n^(-3/2)
            + O(n^(-5/2)*log(n))

        ::

            sage: asymptotic_expansions.SingularityAnalysis('n',
            ....:     alpha=1, beta=1/2, precision=4)
            log(n)^(1/2) + 1/2*euler_gamma*log(n)^(-1/2)
            + (-1/8*euler_gamma^2 + 1/48*pi^2)*log(n)^(-3/2)
            + (1/16*euler_gamma^3 - 1/32*euler_gamma*pi^2 + 1/8*zeta(3))*log(n)^(-5/2)
            + O(log(n)^(-7/2))

        ::

            sage: ae = asymptotic_expansions.SingularityAnalysis('n',
            ....:     alpha=0, beta=2, precision=14)
            sage: n = ae.parent().gen()
            sage: ae.subs(n=n-2)
            2*n^(-1)*log(n) + 2*euler_gamma*n^(-1) - n^(-2) - 1/6*n^(-3) + O(n^(-5))

        ::

            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=-1/2, beta=1, precision=2, normalized=False)
            -1/2/sqrt(pi)*n^(-3/2)*log(n)
            + (-1/2*(euler_gamma + 2*log(2) - 2)/sqrt(pi))*n^(-3/2)
            + O(n^(-5/2)*log(n))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1/2, alpha=0, beta=1, precision=3, normalized=False)
            2^n*n^(-1) + O(2^n*n^(-2))


        ALGORITHM:

        See [FS2009]_.


        TESTS::

            sage: ex = asymptotic_expansions.SingularityAnalysis('n', alpha=-1/2,
            ....:     precision=4)
            sage: n = ex.parent().gen()
            sage: coefficients = ((1-x)^(1/2)).series(
            ....:     x, 21).truncate().coefficients(x, sparse=False)
            sage: ex.compare_with_values(n,    # rel tol 1e-6
            ....:     lambda k: coefficients[k], [5, 10, 20])
            [(5, 0.015778873294?), (10, 0.01498952777?), (20, 0.0146264622?)]
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=3, precision=2)
            1/2*n^2 + 3/2*n + O(1)
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=3, precision=3)
            1/2*n^2 + 3/2*n + 1
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=3, precision=4)
            1/2*n^2 + 3/2*n + 1

        ::

            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=0)
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got O(0)
            The error term O(0) means 0 for sufficiently large n.
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=-1)
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got O(0)
            The error term O(0) means 0 for sufficiently large n.

        ::

            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'm', alpha=-1/2, precision=3)
            -1/2/sqrt(pi)*m^(-3/2)
            - 3/16/sqrt(pi)*m^(-5/2)
            - 25/256/sqrt(pi)*m^(-7/2)
            + O(m^(-9/2))
            sage: _.parent()
            Asymptotic Ring <m^QQ> over Symbolic Constants Subring

        Location of the singularity::

            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=1, zeta=2, precision=3)
            (1/2)^n
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=1, zeta=1/2, precision=3)
            2^n
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=1, zeta=CyclotomicField(3).gen(),
            ....:      precision=3)
            (e^(I*arg(-zeta3 - 1)))^n
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=4, zeta=2, precision=3)
            1/6*(1/2)^n*n^3 + (1/2)^n*n^2 + 11/6*(1/2)^n*n + O((1/2)^n)
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=-1, zeta=2, precision=3)
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got O(0)
            The error term O(0) means 0 for sufficiently large n.
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=1/2, zeta=2, precision=3)
            1/sqrt(pi)*(1/2)^n*n^(-1/2) - 1/8/sqrt(pi)*(1/2)^n*n^(-3/2)
            + 1/128/sqrt(pi)*(1/2)^n*n^(-5/2) + O((1/2)^n*n^(-7/2))

        The following tests correspond to Table VI.5 in [FS2009]_. ::

            sage: A.<n> = AsymptoticRing('n^QQ * log(n)^QQ', QQ)
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=-1/2, beta=1, precision=2,
            ....:     normalized=False) * (- sqrt(pi*n^3))
            1/2*log(n) + 1/2*euler_gamma + log(2) - 1 + O(n^(-1)*log(n))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=0, beta=1, precision=3,
            ....:     normalized=False)
            n^(-1) + O(n^(-2))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=0, beta=2,  precision=14,
            ....:     normalized=False) * n
            2*log(n) + 2*euler_gamma - n^(-1) - 1/6*n^(-2) +  O(n^(-4))
            sage: (asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=1/2, beta=1, precision=4,
            ....:     normalized=False) * sqrt(pi*n)).\\\n            ....:     map_coefficients(lambda x: x.expand())
            log(n) + euler_gamma + 2*log(2) - 1/8*n^(-1)*log(n) +
            (-1/8*euler_gamma - 1/4*log(2))*n^(-1) + O(n^(-2)*log(n))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=1, beta=1, precision=13,
            ....:     normalized=False)
            log(n) + euler_gamma + 1/2*n^(-1) - 1/12*n^(-2) + 1/120*n^(-4)
            + O(n^(-6))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=1, beta=2, precision=4,
            ....:     normalized=False)
            log(n)^2 + 2*euler_gamma*log(n) + euler_gamma^2 - 1/6*pi^2
            + O(n^(-1)*log(n))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=3/2, beta=1, precision=3,
            ....:     normalized=False) * sqrt(pi/n)
            2*log(n) + 2*euler_gamma + 4*log(2) - 4 + 3/4*n^(-1)*log(n)
            + O(n^(-1))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=2, beta=1, precision=5,
            ....:     normalized=False)
            n*log(n) + (euler_gamma - 1)*n + log(n) + euler_gamma + 1/2
            + O(n^(-1))
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, alpha=2, beta=2, precision=4,
            ....:     normalized=False) / n
            log(n)^2 + (2*euler_gamma - 2)*log(n)
            - 2*euler_gamma + euler_gamma^2 - 1/6*pi^2 + 2
            + n^(-1)*log(n)^2 + O(n^(-1)*log(n))

        Be aware that the last result does *not* coincide with [FS2009]_,
        they do have a different error term.

        Checking parameters::

            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, 1, 1/2, precision=0, normalized=False)
            Traceback (most recent call last):
            ...
            ValueError: beta and delta must be integers
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', 1, 1, 1, 1/2, normalized=False)
            Traceback (most recent call last):
            ...
            ValueError: beta and delta must be integers

        ::

            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', alpha=0, beta=0, delta=1, precision=3)
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented for delta!=0

        ::

            sage: from sage.groups.misc_gps.argument_groups import SignGroup
            sage: Signs = SignGroup()
            sage: asymptotic_expansions.SingularityAnalysis(
            ....:     'n', Signs(-1), alpha=2, beta=1, precision=5,
            ....:     normalized=False)
            n*log(n)*(-1)^n + (euler_gamma - 1)*n*(-1)^n + log(n)*(-1)^n
            + (euler_gamma + 1/2)*(-1)^n + O(n^(-1)*(-1)^n)
            sage: _.parent()
            Asymptotic Ring <n^ZZ * log(n)^ZZ * Signs^n> over Symbolic Constants Subring
        """
    @staticmethod
    def ImplicitExpansion(var, phi, tau=None, precision=None):
        """
        Return the singular expansion for a function `y(z)` defined
        implicitly by `y(z) = z \\Phi(y(z))`.

        The function `\\Phi` is assumed to be analytic around `0`. Furthermore,
        `\\Phi` is not allowed to be an affine-linear function and we require
        `\\Phi(0) \\neq 0`.

        Furthermore, it is assumed that there is a unique positive solution `\\tau`
        of `\\Phi(\\tau) - \\tau\\Phi'(\\tau) = 0`.

        All details are given in Chapter VI.7 of [FS2009]_.

        INPUT:

        - ``var`` -- string for the variable name

        - ``phi`` -- the function `\\Phi`; see the extended description for
          assumptions on `\\Phi`

        - ``tau`` -- (default: ``None``) the fundamental constant described
          in the extended description. If ``None``, then `\\tau` is determined
          automatically if possible.

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        OUTPUT: an asymptotic expansion


        .. NOTE::

            In the given case, the radius of convergence of the function of
            interest is known to be `\\rho = \\tau/\\Phi(\\tau)`.  Until :issue:`20050`
            is implemented, the variable in the returned asymptotic expansion
            represents a singular element of the form `(1 - z/\\rho)^{-1}`,
            for the variable `z\\to\\rho`.

        EXAMPLES:

        We can, for example, determine the singular expansion of the well-known
        tree function `T` (which satisfies `T(z) = z \\exp(T(z))`)::

            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=exp, precision=8)
            doctest:warning
            ...
            FutureWarning: This class/method/function is marked as experimental. It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/20050 for details.
            1 - sqrt(2)*Z^(-1/2) + 2/3*Z^(-1) - 11/36*sqrt(2)*Z^(-3/2) +
            43/135*Z^(-2) - 769/4320*sqrt(2)*Z^(-5/2) + 1768/8505*Z^(-3) + O(Z^(-7/2))

        Another classical example in this context is the generating function `B(z)`
        enumerating binary trees with respect to the number of inner nodes. The
        function satisfies `B(z) = z (1 + 2B(z) + B(z)^2)`, which can also be
        solved explicitly, yielding `B(z) = \\frac{1 - \\sqrt{1 - 4z}}{2z} - 1`. We
        compare the expansions from both approaches::

            sage: def B(z):
            ....:     return (1 - sqrt(1 - 4*z))/(2*z) - 1
            sage: A.<Z> = AsymptoticRing('Z^QQ', QQ, default_prec=3)
            sage: B((1-1/Z)/4)
            1 - 2*Z^(-1/2) + 2*Z^(-1) - 2*Z^(-3/2) + 2*Z^(-2)
            - 2*Z^(-5/2) + O(Z^(-3))
            sage: asymptotic_expansions.ImplicitExpansion(Z, phi=lambda u: 1 + 2*u + u^2, precision=7)
            1 - 2*Z^(-1/2) + 2*Z^(-1) - 2*Z^(-3/2) + 2*Z^(-2)
            - 2*Z^(-5/2) + O(Z^(-3))

        Neither `\\tau` nor `\\Phi` have to be known explicitly, they can
        also be passed symbolically::

            sage: tau = var('tau')
            sage: phi = function('phi')
            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=phi, tau=tau, precision=3)  # long time
            tau + (-sqrt(2)*sqrt(-tau*phi(tau)^2/(2*tau*diff(phi(tau), tau)^2
            - tau*phi(tau)*diff(phi(tau), tau, tau)
            - 2*phi(tau)*diff(phi(tau), tau))))*Z^(-1/2) + O(Z^(-1))

        Note that we do not check whether a passed `\\tau` actually
        satisfies the requirements. Only the first of the following
        expansions is correct::

            sage: asymptotic_expansions.ImplicitExpansion('Z',
            ....:     phi=lambda u: 1 + 2*u + u^2, precision=5) # correct expansion
            1 - 2*Z^(-1/2) + 2*Z^(-1) - 2*Z^(-3/2) + O(Z^(-2))
            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=lambda u: 1 + 2*u + u^2, tau=2, precision=5)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: symbolic division by zero
            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=lambda u: 1 + 2*u + u^2, tau=3, precision=5)
            3 - 4*I*sqrt(3)*Z^(-1/2) + 6*I*sqrt(3)*Z^(-3/2) + O(Z^(-2))

        .. SEEALSO::

            :meth:`~AsymptoticExpansionGenerators.ImplicitExpansionPeriodicPart`,
            :meth:`~AsymptoticExpansionGenerators.InverseFunctionAnalysis`.

        TESTS::

            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=lambda u: 1 + 42*u, precision=5)
            Traceback (most recent call last):
            ...
            ValueError: the function phi does not satisfy the requirements
            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=lambda u: 42*u + u^2, precision=5)
            Traceback (most recent call last):
            ...
            ValueError: the function phi does not satisfy the requirements
            sage: asymptotic_expansions.ImplicitExpansion('Z', phi=lambda u: 1 + u^2 + u^42, precision=5)
            Traceback (most recent call last):
            ...
            ValueError: fundamental constant tau could not be determined
        """
    @staticmethod
    def ImplicitExpansionPeriodicPart(var, phi, period, tau=None, precision=None):
        """
        Return the singular expansion for the periodic part of a function `y(z)`
        defined implicitly by `y(z) = z \\Phi(y(z))`.

        The function `\\Phi` is assumed to be analytic around `0`. Furthermore,
        `\\Phi` is not allowed to be an affine-linear function and we require
        `\\Phi(0) \\neq 0`. For an integer `p`, `\\Phi` is called `p`-periodic
        if we have `\\Psi(u^p) = \\Phi(u)` for a power series `\\Psi`
        where `p` is maximal.

        Furthermore, it is assumed that there is a unique positive solution `\\tau`
        of `\\Phi(\\tau) - \\tau\\Phi'(\\tau) = 0`.

        If `\\Phi` is `p`-periodic, then we have `y(z) = z g(z^p)`. This method
        returns the singular expansion of `g(z)`.

        INPUT:

        - ``var`` -- string for the variable name

        - ``phi`` -- the function `\\Phi`; see the extended description for
          assumptions on `\\Phi`

        - ``period`` -- the period of the function `\\Phi`; see the
          extended description for details

        - ``tau`` -- (default: ``None``) the fundamental constant described
          in the extended description. If ``None``, then `\\tau` is determined
          automatically if possible.

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        OUTPUT: an asymptotic expansion


        .. NOTE::

            In the given case, the radius of convergence of the function of
            interest is known to be `\\rho = \\tau/\\Phi(\\tau)`. Until :issue:`20050`
            is implemented, the variable in the returned asymptotic expansion
            represents a singular element of the form `(1 - z/\\rho)^{-1}`,
            for the variable `z\\to\\rho`.

        .. SEEALSO::

            :meth:`~AsymptoticExpansionGenerators.ImplicitExpansion`,
            :meth:`~AsymptoticExpansionGenerators.InverseFunctionAnalysis`.

        EXAMPLES:

        The generating function enumerating binary trees with respect to
        tree size satisfies `B(z) = z (1 + B(z)^2)`. This function can be
        written as `B(z) = z g(z^2)`, and as `B(z)` can be determined
        explicitly we have `g(z) = \\frac{1 - \\sqrt{1 - 4z}}{2z}`. We
        compare the corresponding expansions::

            sage: asymptotic_expansions.ImplicitExpansionPeriodicPart('Z', phi=lambda u: 1 + u^2,
            ....:                                                     period=2, precision=7)
            doctest:warning
            ...
            FutureWarning: This class/method/function is marked as experimental. It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/20050 for details.
            2 - 2*Z^(-1/2) + 2*Z^(-1) - 2*Z^(-3/2) + 2*Z^(-2) - 2*Z^(-5/2) + O(Z^(-3))
            sage: def g(z):
            ....:     return (1 - sqrt(1 - 4*z))/(2*z)
            sage: A.<Z> = AsymptoticRing('Z^QQ', QQ, default_prec=3)
            sage: g((1 - 1/Z)/4)
            2 - 2*Z^(-1/2) + 2*Z^(-1) - 2*Z^(-3/2) + 2*Z^(-2) - 2*Z^(-5/2) + O(Z^(-3))
        """
    @staticmethod
    def InverseFunctionAnalysis(var, phi, tau=None, period: int = 1, precision=None):
        """
        Return the coefficient growth of a function `y(z)` defined implicitly
        by `y(z) = z \\Phi(y(z))`.

        The function `\\Phi` is assumed to be analytic around `0`. Furthermore,
        `\\Phi` is not allowed to be an affine-linear function and we require
        `\\Phi(0) \\neq 0`. For an integer `p`, `\\Phi` is called `p`-periodic
        if we have `\\Psi(u^p) = \\Phi(u)` for a power series `\\Psi`
        where `p` is maximal.

        Furthermore, it is assumed that there is a unique positive solution `\\tau`
        of `\\Phi(\\tau) - \\tau\\Phi'(\\tau) = 0`.

        INPUT:

        - ``var`` -- string for the variable name

        - ``phi`` -- the function `\\Phi`; see the extended description for
          assumptions on `\\Phi`

        - ``tau`` -- (default: ``None``) the fundamental constant described
          in the extended description. If ``None``, then `\\tau` is determined
          automatically if possible.

        - ``period`` -- (default: `1`) the period of the function `\\Phi`. See
          the extended description for details

        - ``precision`` -- (default: ``None``) integer. If ``None``, then
          the default precision of the asymptotic ring is used.

        OUTPUT: an asymptotic expansion


        .. NOTE::

            It is not checked that the passed period actually fits to
            the passed function `\\Phi`.

            The resulting asymptotic expansion is only valid
            for `n \\equiv 1 \\mod p`, where `p` is the period. All other
            coefficients are `0`.

        EXAMPLES:

        There are `C_n` (the `n`-th Catalan number) different binary trees
        of size `2n+1`, and there are no binary trees with an even number of
        nodes. The corresponding generating function satisfies
        `B(z) = z (1 + B(z)^2)`, which allows us to compare the asymptotic
        expansions for the number of binary trees of size `n` obtained via
        `C_n` and obtained via the analysis of `B(z)`::

            sage: assume(SR.an_element() > 0)
            sage: A.<n> = AsymptoticRing('QQ^n * n^QQ', SR)
            sage: binomial_expansion = asymptotic_expansions.Binomial_kn_over_n(n, k=2, precision=3)
            sage: catalan_expansion = binomial_expansion / (n+1)
            sage: catalan_expansion.subs(n=(n-1)/2)
            2*sqrt(1/2)/sqrt(pi)*2^n*n^(-3/2) - 3/2*sqrt(1/2)/sqrt(pi)*2^n*n^(-5/2)
            + 25/16*sqrt(1/2)/sqrt(pi)*2^n*n^(-7/2) + O(2^n*n^(-9/2))
            sage: asymptotic_expansions.InverseFunctionAnalysis(n, phi=lambda u: 1 + u^2, period=2,
            ....:                                               tau=1, precision=8)
            2*sqrt(1/2)/sqrt(pi)*2^n*n^(-3/2) - 3/2*sqrt(1/2)/sqrt(pi)*2^n*n^(-5/2)
            + 25/16*sqrt(1/2)/sqrt(pi)*2^n*n^(-7/2) + O(2^n*n^(-9/2))

        The code in the aperiodic case is more efficient, however. Therefore,
        it is recommended to use combinatorial identities to reduce to the
        aperiodic case. In the example above, this is well-known: we now count
        binary trees with `n` internal nodes. The corresponding generating function
        satisfies `B(z) = z (1 + 2B(z) + B(z)^2)`::

            sage: catalan_expansion
            1/sqrt(pi)*4^n*n^(-3/2) - 9/8/sqrt(pi)*4^n*n^(-5/2)
            + 145/128/sqrt(pi)*4^n*n^(-7/2) + O(4^n*n^(-9/2))
            sage: asymptotic_expansions.InverseFunctionAnalysis(n, phi=lambda u: 1 + 2*u + u^2,
            ....:                                               tau=1, precision=8)
            1/sqrt(pi)*4^n*n^(-3/2) - 9/8/sqrt(pi)*4^n*n^(-5/2)
            + 145/128/sqrt(pi)*4^n*n^(-7/2) + O(4^n*n^(-9/2))

            sage: forget()

        .. SEEALSO::

            :meth:`~AsymptoticExpansionGenerators.ImplicitExpansion`,
            :meth:`~AsymptoticExpansionGenerators.ImplicitExpansionPeriodicPart`.


        TESTS:

        Omitting the precision parameter does not lead to an error (per default,
        the default series precision is a python integer, which led to an error
        in an earlier version of the code)::

            sage: set_series_precision(int(5))
            sage: asymptotic_expansions.InverseFunctionAnalysis('n', phi=lambda u: 1 + 2*u + u^2,
            ....:                                               tau=1)
            1/sqrt(pi)*4^n*n^(-3/2) - 9/8/sqrt(pi)*4^n*n^(-5/2) + O(4^n*n^(-3))
        """

asymptotic_expansions: Incomplete
