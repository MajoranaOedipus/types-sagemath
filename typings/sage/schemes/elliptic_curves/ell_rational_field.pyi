from . import BSD as BSD, constructor as constructor, ell_modular_symbols as ell_modular_symbols, ell_point as ell_point, ell_tate_curve as ell_tate_curve, ell_torsion as ell_torsion, heegner as heegner, mod5family as mod5family, padics as padics
from .ell_generic import EllipticCurve_generic as EllipticCurve_generic
from .ell_number_field import EllipticCurve_number_field as EllipticCurve_number_field
from .modular_parametrization import ModularParameterization as ModularParameterization
from _typeshed import Incomplete
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modular.modsym.modsym import ModularSymbols as ModularSymbols
from sage.modular.pollack_stevens.space import ps_modsym_from_elliptic_curve as ps_modsym_from_elliptic_curve
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing, ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ, RationalField as RationalField
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField
from sage.rings.real_mpfr import RR as RR, RealField as RealField
from sage.structure.coerce import py_scalar_to_element as py_scalar_to_element
from sage.structure.element import Element as Element, RingElement as RingElement

Q: Incomplete
C: Incomplete
R: Incomplete
Z: Incomplete
CMJ: Incomplete

class EllipticCurve_rational_field(EllipticCurve_number_field):
    """
    Elliptic curve over the Rational Field.

    INPUT:

    - ``ainvs`` -- list or tuple `[a_1, a_2, a_3, a_4, a_6]` of
      Weierstrass coefficients

    .. NOTE::

        This class should not be called directly; use
        :class:`sage.constructor.EllipticCurve` to construct
        elliptic curves.

    EXAMPLES:

    Construction from Weierstrass coefficients (`a`-invariants), long form::

        sage: E = EllipticCurve([1,2,3,4,5]); E
        Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field

    Construction from Weierstrass coefficients (`a`-invariants),
    short form (sets `a_1 = a_2 = a_3 = 0`)::

        sage: EllipticCurve([4,5]).ainvs()
        (0, 0, 0, 4, 5)

    Constructor from a Cremona label::

        sage: EllipticCurve('389a1')
        Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field

    Constructor from an LMFDB label::

        sage: EllipticCurve('462.f3')
        Elliptic Curve defined by y^2 + x*y = x^3 - 363*x + 1305 over Rational Field
    """
    db_extra: Incomplete
    def __init__(self, ainvs, **kwds) -> None:
        """
        Constructor for the EllipticCurve_rational_field class.

        TESTS:

        Passing unexpected keyword arguments will raise an error::

            sage: EllipticCurve.create_object(0, (QQ, (1, 2, 0, 1, 2)), base=QQ)
            Traceback (most recent call last):
            ...
            TypeError: unexpected keyword arguments: {'base': Rational Field}

        When constructing a curve from the large database using a
        label, we must be careful that the copied generators have the
        right curve (see :issue:`10999`: the following used not to work when
        the large database was installed)::

            sage: E = EllipticCurve('389a1')
            sage: [P.curve() is E for P in E.gens()]
            [True, True]
        """
    def lmfdb_page(self) -> None:
        """
        Open the LMFDB web page of the elliptic curve in a browser.

        See http://www.lmfdb.org

        EXAMPLES::

            sage: E = EllipticCurve('5077a1')
            sage: E.lmfdb_page()  # optional -- webbrowser
        """
    def is_p_integral(self, p):
        """
        Return ``True`` if this elliptic curve has `p`-integral
        coefficients.

        INPUT:

        - ``p`` -- prime integer

        EXAMPLES::

            sage: E = EllipticCurve(QQ,[1,1]); E
            Elliptic Curve defined by y^2 = x^3 + x + 1 over Rational Field
            sage: E.is_p_integral(2)
            True
            sage: E2=E.change_weierstrass_model(2,0,0,0); E2
            Elliptic Curve defined by y^2 = x^3 + 1/16*x + 1/64 over Rational Field
            sage: E2.is_p_integral(2)
            False
            sage: E2.is_p_integral(3)
            True
        """
    def is_integral(self):
        """
        Return ``True`` if this elliptic curve has integral coefficients (in
        Z).

        EXAMPLES::

            sage: E = EllipticCurve(QQ,[1,1]); E
            Elliptic Curve defined by y^2 = x^3 + x + 1 over Rational Field
            sage: E.is_integral()
            True
            sage: E2=E.change_weierstrass_model(2,0,0,0); E2
            Elliptic Curve defined by y^2 = x^3 + 1/16*x + 1/64 over Rational Field
            sage: E2.is_integral()
            False
        """
    def mwrank(self, options: str = ''):
        """
        Run Cremona's mwrank program on this elliptic curve and return the
        result as a string.

        INPUT:

        - ``options`` -- string; run-time options passed when starting mwrank.
          The format is as follows (see below for examples of usage):

          - ``-v n``    (verbosity level)       sets verbosity to n (default=1)
          - ``-o``      (PARI/GP style output flag)  turns ON extra PARI/GP short output (default is OFF)
          - ``-p n``    (precision)       sets precision to `n` decimals (default=15)
          - ``-b n``    (quartic bound)   bound on quartic point search (default=10)
          - ``-x n``    (n_aux)           number of aux primes used for sieving (default=6)
          - ``-l``      (generator list flag)            turns ON listing of points (default ON unless v=0)
          - ``-s``      (selmer_only flag)     if set, computes Selmer rank only (default: not set)
          - ``-d``      (skip_2nd_descent flag)        if set, skips the second descent for curves with 2-torsion (default: not set)
          - ``-S n``    (sat_bd)          upper bound on saturation primes (default=100, -1 for automatic)

        OUTPUT: string; output of mwrank on this curve

        .. NOTE::

            The output is a raw string and completely illegible using
            automatic display, so it is recommended to use print for
            legible output.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.mwrank() # random
            ...
            sage: print(E.mwrank())
            Curve [0,0,1,-1,0] :        Basic pair: I=48, J=-432
            disc=255744
            ...
            Generator 1 is [0:-1:1]; height 0.05111...

            Regulator = 0.05111...

            The rank and full Mordell-Weil basis have been determined unconditionally.
            ...

        Options to mwrank can be passed::

            sage: E = EllipticCurve([0,0,0,877,0])

        Run mwrank with ``'verbose'`` flag set to 0 but list generators if
        found::

            sage: print(E.mwrank('-v0 -l'))
            Curve [0,0,0,877,0] :   0 <= rank <= 1
            Regulator = 1

        Run mwrank again, this time with a higher bound for point searching
        on homogeneous spaces::

            sage: print(E.mwrank('-v0 -l -b11'))
            Curve [0,0,0,877,0] :   Rank = 1
            Generator 1 is [29604565304828237474403861024284371796799791624792913256602210:-256256267988926809388776834045513089648669153204356603464786949:490078023219787588959802933995928925096061616470779979261000]; height 95.98037...
            Regulator = 95.98037...
        """
    def conductor(self, algorithm: str = 'pari'):
        """
        Return the conductor of the elliptic curve.

        INPUT:

        - ``algorithm`` -- string (default: ``'pari'``)

          - ``'pari'`` -- use the PARI C-library :pari:`ellglobalred`
            implementation of Tate's algorithm

          - ``'mwrank'`` -- use Cremona's mwrank implementation
            of Tate's algorithm; can be faster if the curve has integer
            coefficients (TODO: limited to small conductor until mwrank gets
            integer factorization)

          - ``'gp'`` -- use the GP interpreter

          - ``'generic'`` -- use the general number field implementation

          - ``'all'`` -- use all four implementations, verify
            that the results are the same (or raise an error), and
            output the common value

        EXAMPLES::

            sage: E = EllipticCurve([1, -1, 1, -29372, -1932937])
            sage: E.conductor(algorithm='pari')
            3006
            sage: E.conductor(algorithm='mwrank')
            3006
            sage: E.conductor(algorithm='gp')
            3006
            sage: E.conductor(algorithm='generic')
            3006
            sage: E.conductor(algorithm='all')
            3006

        .. NOTE::

            The conductor computed using each algorithm is cached
            separately. Thus calling ``E.conductor('pari')``, then
            ``E.conductor('mwrank')`` and getting the same result
            checks that both systems compute the same answer.

        TESTS::

            sage: E.conductor(algorithm='bogus')
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'bogus' is not known
        """
    def pari_curve(self):
        """
        Return the PARI curve corresponding to this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])
            sage: e = E.pari_curve()
            sage: type(e)
            <... 'cypari2.gen.Gen'>
            sage: e.type()
            't_VEC'
            sage: e.ellan(10)
            [1, -2, -3, 2, -2, 6, -1, 0, 6, 4]

        ::

            sage: E = EllipticCurve(RationalField(), ['1/3', '2/3'])
            sage: e = E.pari_curve()
            sage: e[:5]
            [0, 0, 0, 1/3, 2/3]

        When doing certain computations, PARI caches the results::

            sage: E = EllipticCurve('37a1')
            sage: _ = E.__dict__.pop('_pari_curve', None)  # clear cached data
            sage: Epari = E.pari_curve()
            sage: Epari
            [0, 0, 1, -1, 0, 0, -2, 1, -1, 48, -216, 37, 110592/37, Vecsmall([1]), [Vecsmall([64, 1])], [0, 0, 0, 0, 0, 0, 0, 0]]
            sage: Epari.omega()
            [2.99345864623196, -2.45138938198679*I]
            sage: Epari
            [0, 0, 1, -1, 0, 0, -2, 1, -1, 48, -216, 37, 110592/37, Vecsmall([1]), [Vecsmall([64, 1])], [[2.99345864623196, -2.45138938198679*I], 0, [0.837565435283323, 0.269594436405445, -1.10715987168877, 1.37675430809421, 1.94472530697209, 0.567970998877878]~, 0, 0, 0, 0, 0]]

        This shows that the bug uncovered by :issue:`4715` is fixed::

            sage: Ep = EllipticCurve('903b3').pari_curve()

        This still works, even when the curve coefficients are large
        (see :issue:`13163`)::

            sage: E = EllipticCurve([4382696457564794691603442338788106497, 28, 3992, 16777216, 298])
            sage: E.pari_curve()
            [4382696457564794691603442338788106497, 28, 3992, 16777216, 298, ...]
            sage: E.minimal_model()
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 7686423934083797390675981169229171907674183588326184511391146727143672423167091484392497987721106542488224058921302964259990799229848935835464702*x + 8202280443553761483773108648734271851215988504820214784899752662100459663011709992446860978259617135893103951840830254045837355547141096270521198994389833928471736723050112419004202643591202131091441454709193394358885 over Rational Field
        """
    def pari_mincurve(self):
        """
        Return the PARI curve corresponding to a minimal model for this
        elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve(RationalField(), ['1/3', '2/3'])
            sage: e = E.pari_mincurve()
            sage: e[:5]
            [0, 0, 0, 27, 486]
            sage: E.conductor()
            47232
            sage: e.ellglobalred()
            [47232, [1, 0, 0, 0], 2, [2, 7; 3, 2; 41, 1], [[7, 2, 0, 1], [2, -3, 0, 2], [1, 5, 0, 1]]]
        """
    @cached_method
    def database_attributes(self):
        """
        Return a dictionary containing information about ``self`` in
        the elliptic curve database.

        If there is no elliptic curve isomorphic to ``self`` in the
        database, a :exc:`LookupError` is raised.

        EXAMPLES::

            sage: E = EllipticCurve((0, 0, 1, -1, 0))
            sage: data = E.database_attributes()
            sage: data['conductor']
            37
            sage: data['cremona_label']
            '37a1'
            sage: data['rank']
            1
            sage: data['torsion_order']
            1

            sage: E = EllipticCurve((8, 13, 21, 34, 55))
            sage: E.database_attributes()
            Traceback (most recent call last):
            ...
            LookupError: Cremona database does not contain entry for Elliptic Curve
            defined by y^2 + 8*x*y + 21*y = x^3 + 13*x^2 + 34*x + 55 over Rational Field
        """
    def database_curve(self):
        """
        Return the curve in the elliptic curve database isomorphic to this
        curve, if possible. Otherwise raise a :exc:`LookupError` exception.

        Since :issue:`11474`, this returns exactly the same curve as
        :meth:`minimal_model`; the only difference is the additional
        work of checking whether the curve is in the database.

        EXAMPLES::

            sage: E = EllipticCurve([0,1,2,3,4])
            sage: E.database_curve()
            Elliptic Curve defined by y^2  = x^3 + x^2 + 3*x + 5 over Rational Field

        .. NOTE::

            The model of the curve in the database can be different
            from the Weierstrass model for this curve, e.g., database
            models are always minimal.
        """
    def Np(self, p):
        """
        The number of points on `E` modulo `p`.

        INPUT:

        - ``p`` -- integer; a prime, not necessarily of good reduction

        OUTPUT:

        integer; the number of points on the reduction of `E` modulo `p`
        (including the singular point when `p` is a prime of bad reduction).

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.Np(2)
            5
            sage: E.Np(3)
            5
            sage: E.conductor()
            11
            sage: E.Np(11)
            11

        This even works when the prime is large::

            sage: E = EllipticCurve('37a')
            sage: E.Np(next_prime(10^30))
            1000000000000001426441464441649
        """
    def mwrank_curve(self, verbose: bool = False):
        """
        Construct an mwrank_EllipticCurve from this elliptic curve.

        The resulting mwrank_EllipticCurve has available methods from John
        Cremona's eclib library.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: EE = E.mwrank_curve()
            sage: EE
            y^2 + y = x^3 - x^2 - 10 x - 20
            sage: type(EE)
            <class 'sage.libs.eclib.interface.mwrank_EllipticCurve'>
            sage: EE.isogeny_class()
            ([[0, -1, 1, -10, -20], [0, -1, 1, -7820, -263580], [0, -1, 1, 0, 0]],
             [[0, 5, 5], [5, 0, 0], [5, 0, 0]])
        """
    def two_descent(self, verbose: bool = True, selmer_only: bool = False, first_limit: int = 20, second_limit: int = 8, n_aux: int = -1, second_descent: int = 1):
        """
        Compute 2-descent data for this curve.

        INPUT:

        - ``verbose`` -- boolean (default: ``True``); print what mwrank is
          doing. If ``False``, **no output** is printed.

        - ``selmer_only`` -- boolean (default: ``False``); selmer_only switch

        - ``first_limit`` -- integer (default: 20); naive height bound on
          first point search on quartic homogeneous spaces (before
          testing local solubility; very simple search with no
          overheads).

        - ``second_limit`` -- integer (default: 8); logarithmic height bound on
          second point search on quartic homogeneous spaces (after
          testing local solubility; sieve-assisted search)

        - ``n_aux`` -- integer (default: -1); if positive, the number of
          auxiliary primes used in sieve-assisted search for quartics.
          If -1 (the default) use a default value (set in the eclib
          code in ``src/qrank/mrank1.cc`` in DEFAULT_NAUX: currently 8).
          Only relevant for curves with no 2-torsion, where full
          2-descent is carried out.  Worth increasing for curves
          expected to be of rank > 6 to one or two more than the
          expected rank.

        - ``second_descent`` -- boolean (default: ``True``); flag specifying
          whether or not a second descent will be carried out.  Only relevant
          for curves with 2-torsion.  Recommended left as the default except for
          experts interested in details of Selmer groups.

        OUTPUT:

        Return ``True`` if the descent succeeded, i.e. if the lower bound and
        the upper bound for the rank are the same. In this case, generators and
        the rank are cached. A return value of ``False`` indicates that either
        rational points were not found, or that Sha[2] is nontrivial and mwrank
        was unable to determine this for sure.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.two_descent(verbose=False)
            True
        """
    def aplist(self, n, python_ints: bool = False):
        """
        The Fourier coefficients `a_p` of the modular form
        attached to this elliptic curve, for all primes `p\\leq n`.

        INPUT:

        - ``n`` -- integer

        - ``python_ints`` -- boolean (default: ``False``); if ``True``
          return a list of Python ints instead of Sage integers

        OUTPUT: list of integers

        EXAMPLES::

            sage: e = EllipticCurve('37a')
            sage: e.aplist(1)
            []
            sage: e.aplist(2)
            [-2]
            sage: e.aplist(10)
            [-2, -3, -2, -1]
            sage: v = e.aplist(13); v
            [-2, -3, -2, -1, -5, -2]
            sage: type(v[0])
            <... 'sage.rings.integer.Integer'>
            sage: type(e.aplist(13, python_ints=True)[0])
            <... 'int'>
        """
    def anlist(self, n, python_ints: bool = False):
        """
        The Fourier coefficients up to and including `a_n` of the
        modular form attached to this elliptic curve. The `i`-th element of
        the return list is ``a[i]``.

        INPUT:

        - ``n`` -- integer

        - ``python_ints`` -- boolean (default: ``False``); if ``True``
          return a list of Python ints instead of Sage integers

        OUTPUT: list of integers

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.anlist(3)
            [0, 1, -2, -1]

        ::

            sage: E = EllipticCurve([0,1])
            sage: E.anlist(20)
            [0, 1, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 8, 0]
        """
    def q_expansion(self, prec):
        """
        Return the `q`-expansion to precision ``prec`` of the newform
        attached to this elliptic curve.

        INPUT:

        - ``prec`` -- integer

        OUTPUT: a power series (in the variable 'q')

        .. NOTE::

            If you want the output to be a modular form and not just a
            `q`-expansion, use :meth:`.modular_form`.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.q_expansion(20)
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + 6*q^6 - q^7 + 6*q^9 + 4*q^10
             - 5*q^11 - 6*q^12 - 2*q^13 + 2*q^14 + 6*q^15 - 4*q^16 - 12*q^18 + O(q^20)
        """
    def modular_form(self):
        """
        Return the cuspidal modular form associated to this elliptic
        curve.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: f = E.modular_form()
            sage: f
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + O(q^6)

        If you need to see more terms in the `q`-expansion::

            sage: f.q_expansion(20)
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + 6*q^6 - q^7 + 6*q^9 + 4*q^10
             - 5*q^11 - 6*q^12 - 2*q^13 + 2*q^14 + 6*q^15 - 4*q^16 - 12*q^18 + O(q^20)

        .. NOTE::

            If you just want the `q`-expansion, use
            :meth:`.q_expansion`.
        """
    def modular_symbol_space(self, sign: int = 1, base_ring=..., bound=None):
        """
        Return the space of cuspidal modular symbols associated to this
        elliptic curve, with given sign and base ring.

        INPUT:

        - ``sign`` -- 0, -1, or 1
        - ``base_ring`` -- a ring

        EXAMPLES::

            sage: f = EllipticCurve('37b')
            sage: f.modular_symbol_space()
            Modular Symbols subspace of dimension 1 of Modular Symbols space
             of dimension 3 for Gamma_0(37) of weight 2 with sign 1 over Rational Field
            sage: f.modular_symbol_space(-1)
            Modular Symbols subspace of dimension 1 of Modular Symbols space
             of dimension 2 for Gamma_0(37) of weight 2 with sign -1 over Rational Field
            sage: f.modular_symbol_space(0, bound=3)
            Modular Symbols subspace of dimension 2 of Modular Symbols space
             of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field

        .. NOTE::

            If you just want the `q`-expansion, use
            :meth:`.q_expansion`.
        """
    def abelian_variety(self):
        """
        Return ``self`` as a modular abelian variety.

        OUTPUT: a modular abelian variety

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: E.abelian_variety()
            Abelian variety J0(11) of dimension 1

            sage: E = EllipticCurve('33a')
            sage: E.abelian_variety()
            Abelian subvariety of dimension 1 of J0(33)
        """
    def modular_symbol(self, sign: int = +1, normalize=None, implementation: str = 'eclib', nap: int = 0):
        """
        Return the modular symbol map associated to this elliptic curve
        with given sign.

        INPUT:

        - ``sign`` -- +1 (default) or -1

        - ``normalize`` -- (default: ``None``) either ``'L_ratio'``,
          ``'period'``, or ``'none'``; ignored unless ``implementation`` is
          ``'sage'``. For ``'L_ratio'``, the modular symbol tries to normalize
          correctly as explained below by comparing it to ``L_ratio`` for the
          curve and some small twists.  The normalization ``'period'`` uses the
          ``integral_period_map`` for modular symbols which is known to be
          equal to the desired normalization, up to the sign and a possible
          power of 2. With normalization ``'none'``, the modular symbol is
          almost certainly not correctly normalized, i.e. all values will be
          a fixed scalar multiple of what they should be.

        - ``implementation`` -- either ``'eclib'`` (default), ``'sage'`` or
          ``'num'``. Here, ``'eclib'`` uses Cremona's ``C++`` implementation
          in the ``eclib`` library, ``'sage'`` uses an implementation
          within Sage which is often quite a bit slower, and ``'num'``
          uses Wuthrich's implementation of numerical modular symbols.

        - ``nap`` -- integer (default: 0); ignored unless implementation is
          ``'eclib'``.  The number of ap of E to use in determining the
          normalisation of the modular symbols.  If 0 (the default),
          then the value of ``100*E.conductor().isqrt()`` is used.  Using
          too small a value can lead to incorrect normalisation.

        DEFINITION:

        The modular symbol map sends any rational number `r` to the
        rational number whichis the ratio of the real or imaginary
        part (depending on the sign) of the integral of `2 \\pi i
        f(z) dz` from `\\infty` to `r`, where `f` is the newform
        attached to `E`, to the real or imaginary period of `E`.

        More precisely: If the sign is +1, then the value returned
        is the quotient of the real part of this integral by the
        least positive period `\\Omega_E^{+}` of `E`. In particular
        for `r=0`, the value is equal to `L(E,1)/\\Omega_E^{+}`
        (unlike in ``L_ratio`` of ``lseries()``, where the value is
        also divided by the number of connected components of
        `E(\\RR)`). In particular the modular symbol depends on `E`
        and not only the isogeny class of `E`.  For sign `-1`, it
        is the quotient of the imaginary part of the integral
        divided by the purely imaginary period of `E` with smallest
        positive imaginary part. Note however there is an issue
        about these normalizations, hence the optional argument
        ``normalize`` explained below

        ALGORITHM:

        For the implementations ``'sage'`` and ``'eclib'``, the used
        algorithm starts by finding the space of modular symbols
        within the full space of all modular symbols of that
        level. This initial step will take a very long time if the
        conductor is large (e.g. minutes for five digit
        conductors). Once the space is determined, each evaluation
        is very fast (logarithmic in the denominator of `r`).

        The implementation ``'num'`` uses a different algorithm.  It
        uses numerical integration along paths in the upper half
        plane. The bounds are rigorously proved so that the outcome
        is known to be correct. The initial step costs no time,
        instead each evaluation will take more time than in the
        above. More information in the documentation of the class
        ``ModularSymbolNumerical``.

        .. SEEALSO::

            :meth:`modular_symbol_numerical`

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: M = E.modular_symbol(); M
            Modular symbol with sign 1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: M(1/2)
            0
            sage: M(1/5)
            1

        ::

            sage: E = EllipticCurve('121b1')
            sage: M = E.modular_symbol(implementation='sage')
            Warning : Could not normalize the modular symbols, maybe all further results
            will be multiplied by -1 and a power of 2
            sage: M(1/7)
            -1/2

        With the numerical version, rather high conductors can
        be computed::

            sage: E = EllipticCurve([999,997])
            sage: E.conductor()
            16059400956
            sage: m = E.modular_symbol(implementation='num')
            sage: m(0) # long time
            16

        Different curves in an isogeny class have modular symbols
        which differ by a nonzero rational factor::

            sage: E1 = EllipticCurve('11a1')
            sage: M1 = E1.modular_symbol()
            sage: M1(0)
            1/5
            sage: E2 = EllipticCurve('11a2')
            sage: M2 = E2.modular_symbol()
            sage: M2(0)
            1
            sage: E3 = EllipticCurve('11a3')
            sage: M3 = E3.modular_symbol()
            sage: M3(0)
            1/25
            sage: all(5*M1(r)==M2(r)==25*M3(r) for r in QQ.range_by_height(10))
            True

        With the default implementation using ``eclib``, the symbols
        are correctly normalized automatically.  With the ``Sage``
        implementation we can choose to normalize using the L-ratio,
        unless that is 0 (for curves of positive rank) or using
        periods.  Here is an example where the symbol is already
        normalized::

            sage: E = EllipticCurve('11a2')
            sage: E.modular_symbol(implementation = 'eclib')(0)
            1
            sage: E.modular_symbol(implementation = 'sage', normalize='L_ratio')(0)
            1
            sage: E.modular_symbol(implementation = 'sage', normalize='none')(0)
            1
            sage: E.modular_symbol(implementation = 'sage', normalize='period')(0)
            1

        Here is an example where both normalization methods work,
        while the non-normalized symbol is incorrect::

            sage: E = EllipticCurve('11a3')
            sage: E.modular_symbol(implementation = 'eclib')(0)
            1/25
            sage: E.modular_symbol(implementation = 'sage', normalize='none')(0)
            1
            sage: E.modular_symbol(implementation = 'sage', normalize='L_ratio')(0)
            1/25
            sage: E.modular_symbol(implementation = 'sage', normalize='period')(0)
            1/25

        Since :issue:`10256`, the interface for negative modular symbols in eclib is available::

            sage: E = EllipticCurve('11a1')
            sage: Mplus = E.modular_symbol(+1); Mplus
            Modular symbol with sign 1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: [Mplus(1/i) for i in [1..11]]
            [1/5, -4/5, -3/10, 7/10, 6/5, 6/5, 7/10, -3/10, -4/5, 1/5, 0]
            sage: Mminus = E.modular_symbol(-1); Mminus
            Modular symbol with sign -1 over Rational Field attached to
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: [Mminus(1/i) for i in [1..11]]
            [0, 0, 1/2, 1/2, 0, 0, -1/2, -1/2, 0, 0, 0]

        With older version of eclib, in the default 'eclib'
        implementation, if ``nap`` is too small, the normalization may
        be computed incorrectly (see :issue:`31317`).  This was fixed
        in eclib version v20210310, since now eclib increase ``nap``
        automatically. The following used to give incorrect results.
        See :issue:`31443`::

            sage: E = EllipticCurve('1590g1')
            sage: m = E.modular_symbol(nap=300)     # long time
            sage: [m(a/5) for a in [1..4]]          # long time
            [13/2, -13/2, -13/2, 13/2]

        These values are correct, as verified by the numerical
        implementation::

            sage: m = E.modular_symbol(implementation='num')
            sage: [m(a/5) for a in [1..4]]
            [13/2, -13/2, -13/2, 13/2]
        """
    def modular_symbol_numerical(self, sign: int = 1, prec: int = 20):
        """
        Return the modular symbol as a numerical function.

        Just as in :meth:`modular_symbol` this returns a function
        that maps any rational `r` to a real number that should be
        equal to the rational number with an error smaller than the
        given binary precision. In practice the precision is
        often much higher. See the examples below.
        The normalisation is the same.

        INPUT:

        - ``sign`` -- either +1 (default) or -1

        - ``prec`` -- integer (default: 20)

        OUTPUT: a real number

        ALGORITHM:

        This method does not compute spaces of modular symbols,
        so it is suitable for curves of larger conductor than
        can be handled by :meth:`modular_symbol`.
        It is essentially the same implementation as
        ``modular_symbol`` with implementation set to 'num'.
        However the precision is not automatically chosen to
        be certain that the output is equal to the rational
        number it approximates.

        For large conductors one should set the ``prec`` very small.

        EXAMPLES::

            sage: E = EllipticCurve('19a1')
            sage: f = E.modular_symbol_numerical(1)
            sage: g = E.modular_symbol(1)
            sage: f(0), g(0)  # abs tol 1e-11
            (0.333333333333333, 1/3)

            sage: E = EllipticCurve('5077a1')
            sage: f = E.modular_symbol_numerical(-1, prec=2)
            sage: f(0)        # abs tol 1e-11
            0.000000000000000
            sage: f(1/7)      # abs tol 1e-11
            0.999844176260303

            sage: E = EllipticCurve([123,456])
            sage: E.conductor()
            104461920
            sage: f = E.modular_symbol_numerical(prec=2)
            sage: f(0)        # abs tol 1e-11
            2.00001004772210
        """
    def pollack_stevens_modular_symbol(self, sign: int = 0, implementation: str = 'eclib'):
        """
        Create the modular symbol attached to the elliptic curve,
        suitable for overconvergent calculations.

        INPUT:

        - ``sign`` -- +1 or -1 or 0 (default), in which case this it
          is the sum of the two

        - ``implementation`` -- either 'eclib' (default) or 'sage'.
          This determines classical modular symbols which implementation
          of the underlying classical  modular symbols is used

        EXAMPLES::

            sage: E = EllipticCurve('113a1')
            sage: symb = E.pollack_stevens_modular_symbol()
            sage: symb
            Modular symbol of level 113 with values in Sym^0 Q^2
            sage: symb.values()
            [-1/2, 1, -1, 0, 0, 1, 1, -1, 0, -1, 0, 0, 0, 1, -1, 0, 0, 0, 1, 0, 0]

            sage: E = EllipticCurve([0,1])
            sage: symb = E.pollack_stevens_modular_symbol(+1)
            sage: symb.values()
            [-1/6, 1/12, 0, 1/6, 1/12, 1/3, -1/12, 0, -1/6, -1/12, -1/4, -1/6, 1/12]
        """
    padic_lseries: Incomplete
    def newform(self):
        """
        Same as ``self.modular_form()``.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.newform()
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + O(q^6)
            sage: E.newform() == E.modular_form()
            True
        """
    def q_eigenform(self, prec):
        """
        Synonym for ``self.q_expansion(prec)``.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.q_eigenform(10)
            q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + 6*q^6 - q^7 + 6*q^9 + O(q^10)
            sage: E.q_eigenform(10) == E.q_expansion(10)
            True
        """
    def analytic_rank(self, algorithm: str = 'pari', leading_coefficient: bool = False):
        """
        Return an integer that is *probably* the analytic rank of this
        elliptic curve.

        INPUT:

        - ``algorithm`` -- string (default: ``'pari'``):

          - ``'pari'`` -- use the PARI library function
          - ``'sympow'`` -- use Watkins's program sympow
          - ``'rubinstein'`` -- use Rubinstein's `L`-function C++ program lcalc
          - ``'magma'`` -- use MAGMA
          - ``'zero_sum'`` -- use the rank bounding zero sum method implemented
            in :meth:`analytic_rank_upper_bound`
          - ``'all'`` -- compute with PARI, sympow and lcalc, check that
            the answers agree, and return the common answer

        - ``leading_coefficient`` -- boolean (default: ``False``); if set to
          ``True``, return a tuple ``(rank, lead)`` where ``lead`` is the value
          of the first nonzero derivative of the `L`-function of the elliptic
          curve. Only implemented for ``algorithm='pari'``.

        .. NOTE::

            If the curve is loaded from the large Cremona database,
            then the modular degree is taken from the database.

        Of the first three algorithms above, probably Rubinstein's is the
        most efficient (in some limited testing done). The zero sum method
        is often *much* faster, but can return a value which is strictly
        larger than the analytic rank. For curves with conductor <=10^9
        using default parameters, testing indicates that for 99.75% of
        curves the returned rank bound is the true rank.

        .. NOTE::

            If you use ``set_verbose(1)``, extra information about the
            computation will be printed when ``algorithm='zero_sum'``.

        .. NOTE::

            It is an open problem to *prove* that *any* particular
            elliptic curve has analytic rank `\\geq 4`.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: E.analytic_rank(algorithm='pari')
            2
            sage: E.analytic_rank(algorithm='rubinstein')
            2
            sage: E.analytic_rank(algorithm='sympow')
            2
            sage: E.analytic_rank(algorithm='magma')    # optional - magma
            2
            sage: E.analytic_rank(algorithm='zero_sum')
            2
            sage: E.analytic_rank(algorithm='all')
            2

        With the optional parameter leading_coefficient set to ``True``,
        a tuple of both the analytic rank and the leading term of the
        `L`-series at `s = 1` is returned. This only works for
        ``algorithm=='pari'``::

            sage: EllipticCurve([0,-1,1,-10,-20]).analytic_rank(leading_coefficient=True)
            (0, 0.25384186085591068...)
            sage: EllipticCurve([0,0,1,-1,0]).analytic_rank(leading_coefficient=True)
            (1, 0.30599977383405230...)
            sage: EllipticCurve([0,1,1,-2,0]).analytic_rank(leading_coefficient=True)
            (2, 1.518633000576853...)
            sage: EllipticCurve([0,0,1,-7,6]).analytic_rank(leading_coefficient=True)
            (3, 10.39109940071580...)
            sage: EllipticCurve([0,0,1,-7,36]).analytic_rank(leading_coefficient=True)
            (4, 196.170903794579...)

        TESTS:

        When the input is horrendous, some of the algorithms just bomb
        out with a :exc:`RuntimeError`::

            sage: EllipticCurve([1234567,89101112]).analytic_rank(algorithm='rubinstein')
            Traceback (most recent call last):
            ...
            RuntimeError: unable to compute analytic rank using rubinstein algorithm (unable to convert ' 6.19283... and is too large' to an integer)
            sage: EllipticCurve([1234567,89101112]).analytic_rank(algorithm='sympow')  # long time
            Traceback (most recent call last):
            ...
            RuntimeError: failed to compute analytic rank
        """
    def analytic_rank_upper_bound(self, max_Delta=None, adaptive: bool = True, N=None, root_number: str = 'compute', bad_primes=None, ncpus=None):
        '''
        Return an upper bound for the analytic rank of ``self``, conditional on
        the Generalized Riemann Hypothesis, via computing
        the zero sum `\\sum_{\\gamma} f(\\Delta\\gamma),` where `\\gamma`
        ranges over the imaginary parts of the zeros of `L(E,s)`
        along the critical strip, `f(x) = (\\sin(\\pi x)/(\\pi x))^2`,
        and `\\Delta` is the tightness parameter whose maximum value is specified
        by ``max_Delta``. This computation can be run on curves with very large
        conductor (so long as the conductor is known or quickly computable)
        when `\\Delta` is not too large (see below).
        Uses Bober\'s rank bounding method as described in [Bob2013]_.

        INPUT:

        - ``max_Delta`` -- (default: ``None``) if not ``None``, a positive real
          value specifying the maximum Delta value used in the zero sum; larger
          values of Delta yield better bounds - but runtime is exponential in
          Delta. If left as ``None``, Delta is set
          to `\\min\\{\\frac{1}{\\pi}(\\log(N+1000)/2-\\log(2\\pi)-\\eta), 2.5\\}`,
          where `N` is the conductor of the curve attached to ``self``, and `\\eta`
          is the Euler-Mascheroni constant `= 0.5772...`; the crossover
          point is at conductor around `8.3 \\cdot 10^8`. For the former value,
          empirical results show that for about 99.7% of all curves the returned
          value is the actual analytic rank.

        - ``adaptive`` -- boolean (default: ``True``):

          - ``True`` -- the computation is first run with small and then
            successively larger `\\Delta` values up to max_Delta. If at any
            point the computed bound is 0 (or 1 when root_number is -1
            or True), the computation halts and that value is returned;
            otherwise the minimum of the computed bounds is returned.
          - ``False`` -- the computation is run a single time with `\\Delta`
            equal to ``max_Delta``, and the resulting bound returned

        - ``N`` -- (default: ``None``) if not ``None``, a positive integer equal
          to the conductor of ``self``. This is passable so that rank estimation
          can be done for curves whose (large) conductor has been precomputed.

        - ``root_number`` -- (default: ``\'compute\'``) string or integer:

          - ``\'compute\'`` -- the root number of ``self`` is computed and used to
            (possibly) lower the analytic rank estimate by 1.
          - ``\'ignore\'`` -- the above step is omitted
          - ``1`` -- this value is assumed to be the root number of
            ``self``. This is passable so that rank estimation can be done for
            curves whose root number has been precomputed.
          - ``-1`` -- this value is assumed to be the root number of
            ``self``. This is passable so that rank estimation can be done for
            curves whose root number has been precomputed.

        - ``bad_primes`` -- (default: ``None``) if not ``None``, a list of the primes
          of bad reduction for the curve attached to ``self``. This is passable
          so that rank estimation can be done for curves of large conductor
          whose bad primes have been precomputed.

        - ``ncpus`` -- (default: ``None``) if not ``None``, a positive integer
          defining the maximum number of CPUs to be used for the computation.
          If left as None, the maximum available number of CPUs will be used.
          Note: Due to parallelization overhead, multiple processors will
          only be used for Delta values `\\ge 1.75`.

        .. NOTE::

            Output will be incorrect if the incorrect conductor or root number
            is specified.

        .. WARNING::

            Zero sum computation time is exponential in the tightness
            parameter `\\Delta`, roughly doubling for every increase of 0.1
            thereof. Using `\\Delta=1` (and adaptive=False) will yield a runtime
            of a few milliseconds; `\\Delta=2` takes a few seconds, and `\\Delta=3`
            may take upwards of an hour. Increase beyond this at your own risk!

        OUTPUT:

        A nonnegative integer greater than or equal to the analytic rank of
        ``self``.

        .. NOTE::

            If you use set_verbose(1), extra information about the computation
            will be printed.

        .. SEEALSO::

            :func:`LFunctionZeroSum`
            :meth:`.root_number`
            :func:`~sage.misc.verbose.set_verbose`

        EXAMPLES:

        For most elliptic curves with small conductor the central zero(s)
        of `L_E(s)` are fairly isolated, so small values of `\\Delta`
        will yield tight rank estimates.

        ::

            sage: E = EllipticCurve("11a")
            sage: E.rank()
            0
            sage: E.analytic_rank_upper_bound(max_Delta=1, adaptive=False)
            0
            sage: E = EllipticCurve([-39,123])
            sage: E.rank()
            1
            sage: E.analytic_rank_upper_bound(max_Delta=1, adaptive=True)
            1

        This is especially true for elliptic curves with large rank.

        ::

            sage: for r in range(9):
            ....:     E = elliptic_curves.rank(r)[0]
            ....:     print((r, E.analytic_rank_upper_bound(max_Delta=1,
            ....:                                           adaptive=False,
            ....:                                           root_number=\'ignore\')))
            (0, 0)
            (1, 1)
            (2, 2)
            (3, 3)
            (4, 4)
            (5, 5)
            (6, 6)
            (7, 7)
            (8, 8)

        However, some curves have `L`-functions with low-lying zeroes, and for these
        larger values of `\\Delta` must be used to get tight estimates.

        ::

            sage: E = EllipticCurve("974b1")
            sage: r = E.rank(); r
            0
            sage: E.analytic_rank_upper_bound(max_Delta=1, root_number=\'ignore\')
            1
            sage: E.analytic_rank_upper_bound(max_Delta=1.3, root_number=\'ignore\')
            0

        Knowing the root number of `E` allows us to use smaller Delta values
        to get tight bounds, thus speeding up runtime considerably.

        ::

            sage: E.analytic_rank_upper_bound(max_Delta=0.6, root_number=\'compute\')
            0

        There are a small number of curves which have pathologically low-lying
        zeroes. For these curves, this method will produce a bound that is
        strictly larger than the analytic rank, unless very large values of
        Delta are used. The following curve ("256944c1" in the Cremona tables)
        is a rank 0 curve with a zero at 0.0256...; the smallest Delta value
        for which the zero sum is strictly less than 2 is ~2.815.

        ::

            sage: E = EllipticCurve([0, -1, 0, -7460362000712, -7842981500851012704])
            sage: N, r = E.conductor(), E.analytic_rank(); N, r
            (256944, 0)
            sage: E.analytic_rank_upper_bound(max_Delta=1, adaptive=False)
            2
            sage: E.analytic_rank_upper_bound(max_Delta=2, adaptive=False)
            2

        This method is can be called on curves with large conductor.

        ::

            sage: E = EllipticCurve([-2934,19238])
            sage: E.analytic_rank_upper_bound()
            1

        And it can bound rank on curves with *very* large conductor, so long as
        you know beforehand/can easily compute the conductor and primes of bad
        reduction less than `e^{2\\pi\\Delta}`. The example below is of the rank
        28 curve discovered by Elkies that is the elliptic curve of (currently)
        largest known rank.

        ::

            sage: a4 = -20067762415575526585033208209338542750930230312178956502
            sage: a6 = 34481611795030556467032985690390720374855944359319180361266008296291939448732243429
            sage: E = EllipticCurve([1, -1, 1, a4, a6])
            sage: bad_primes = [2, 3, 5, 7, 11, 13, 17, 19, 48463]
            sage: N = 3455601108357547341532253864901605231198511505793733138900595189472144724781456635380154149870961231592352897621963802238155192936274322687070
            sage: E.analytic_rank_upper_bound(max_Delta=2.37, adaptive=False,  # long time
            ....:                             N=N, root_number=1,
            ....:                             bad_primes=bad_primes, ncpus=2)
            32
        '''
    def simon_two_descent(self, verbose: int = 0, lim1: int = 5, lim3: int = 50, limtriv: int = 3, maxprob: int = 20, limbigprime: int = 30, known_points=None):
        '''
        Return lower and upper bounds on the rank of the Mordell-Weil
        group `E(\\QQ)` and a list of points of infinite order.

        .. WARNING::

            This function is deprecated as the functionality of
            Simon\'s script for elliptic curves over the rationals
            has been ported over to pari.
            Use :meth:`.rank` with the keyword ``algorithm=\'pari\'`` instead.

        INPUT:

        - ``verbose`` -- 0, 1, 2, or 3 (default: 0), the verbosity level

        - ``lim1`` -- (default: 5) limit on trivial points on quartics

        - ``lim3`` -- (default: 50) limit on points on ELS quartics

        - ``limtriv`` -- (default: 3) limit on trivial points on `E`

        - ``maxprob`` -- (default: 20)

        - ``limbigprime`` -- (default: 30) to distinguish between small
          and large prime numbers. Use probabilistic tests for large
          primes. If 0, don\'t any probabilistic tests.

        - ``known_points`` -- (default: ``None``) list of known points on
          the curve

        OUTPUT: a triple ``(lower, upper, list)`` consisting of

        - ``lower`` -- integer; lower bound on the rank

        - ``upper`` -- integer; upper bound on the rank

        - ``list`` -- list of points of infinite order in `E(\\QQ)`

        The integer ``upper`` is in fact an upper bound on the
        dimension of the 2-Selmer group, hence on the dimension of
        `E(\\QQ)/2E(\\QQ)`.  It is equal to the dimension of the
        2-Selmer group except possibly if `E(\\QQ)[2]` has dimension 1.
        In that case, ``upper`` may exceed the dimension of the
        2-Selmer group by an even number, due to the fact that the
        algorithm does not perform a second descent.

        To obtain a list of generators, use E.gens().

        IMPLEMENTATION:

        Uses Denis Simon\'s PARI/GP scripts from
        http://www.math.unicaen.fr/~simon/

        EXAMPLES:

        We compute the ranks of the curves of lowest known conductor up to
        rank `8`. Amazingly, each of these computations finishes
        almost instantly!

        ::

            sage: E = EllipticCurve(\'11a1\')
            sage: E.simon_two_descent()
            doctest:warning
            ...
            DeprecationWarning: Use E.rank(algorithm="pari") instead, as this script has been ported over to pari.
            See https://github.com/sagemath/sage/issues/35621 for details.
            doctest:warning
            ...
            DeprecationWarning: please use the 2-descent algorithm over QQ inside pari
            See https://github.com/sagemath/sage/issues/38461 for details.
            (0, 0, [])
            sage: E = EllipticCurve(\'37a1\')
            sage: E.simon_two_descent()
            (1, 1, [(0 : 0 : 1)])
            sage: E = EllipticCurve(\'389a1\')
            sage: E._known_points = []  # clear cached points
            sage: E.simon_two_descent()
            (2, 2, [(-3/4 : 7/8 : 1), (5/4 : 5/8 : 1)])
            sage: E = EllipticCurve(\'5077a1\')
            sage: E.simon_two_descent()
            (3, 3, [(1 : 0 : 1), (2 : 0 : 1), (0 : 2 : 1)])

        In this example Simon\'s program does not find any points, though it
        does correctly compute the rank of the 2-Selmer group.

        ::

            sage: E = EllipticCurve([1, -1, 0, -751055859, -7922219731979])
            sage: E.simon_two_descent()
            (1, 1, [])

        The rest of these entries were taken from Tom Womack\'s page
        http://tom.womack.net/maths/conductors.htm

        ::

            sage: E = EllipticCurve([1, -1, 0, -79, 289])
            sage: E.simon_two_descent()
            (4, 4, [(6 : -1 : 1), (4 : 3 : 1), (5 : -2 : 1), (8 : 7 : 1)])
            sage: E = EllipticCurve([0, 0, 1, -79, 342])
            sage: E.simon_two_descent()  # long time (9s on sage.math, 2011)
            (5, 5, [(5 : 8 : 1), (10 : 23 : 1), (3 : 11 : 1), (-3 : 23 : 1), (0 : 18 : 1)])
            sage: E = EllipticCurve([1, 1, 0, -2582, 48720])
            sage: r, s, G = E.simon_two_descent(); r,s
            (6, 6)
            sage: E = EllipticCurve([0, 0, 0, -10012, 346900])
            sage: r, s, G = E.simon_two_descent(); r,s  # long time
            (7, 7)
            sage: E = EllipticCurve([0, 0, 1, -23737, 960366])
            sage: r, s, G = E.simon_two_descent(); r,s  # long time
            (8, 8)

        Example from :issue:`10832`::

            sage: E = EllipticCurve([1,0,0,-6664,86543])
            sage: E.simon_two_descent()
            (2, 3, [(-1/4 : 2377/8 : 1), (323/4 : 1891/8 : 1)])
            sage: E.rank()
            2
            sage: E.gens()
            [(-1/4 : 2377/8 : 1), (323/4 : 1891/8 : 1)]

        Example where the lower bound is known to be 1
        despite that the algorithm has not found any
        points of infinite order ::

            sage: E = EllipticCurve([1, 1, 0, -23611790086, 1396491910863060])
            sage: E.simon_two_descent()
            (1, 2, [])
            sage: E.rank()
            1
            sage: E.gens()     # uses mwrank
            [(4311692542083/48594841 : -13035144436525227/338754636611 : 1)]

        Example for :issue:`5153`::

            sage: E = EllipticCurve([3,0])
            sage: E.simon_two_descent()
            (1, 2, [(1 : 2 : 1)])

        The upper bound on the 2-Selmer rank returned by this method
        need not be sharp.  In following example, the upper bound
        equals the actual 2-Selmer rank plus 2 (see :issue:`10735`)::

            sage: E = EllipticCurve(\'438e1\')
            sage: E.simon_two_descent()
            (0, 3, [])
            sage: E.selmer_rank()  # uses mwrank
            1
        '''
    two_descent_simon = simon_two_descent
    def three_selmer_rank(self, algorithm: str = 'UseSUnits'):
        """
        Return the 3-selmer rank of this elliptic curve, computed using
        Magma.

        INPUT:

        - ``algorithm`` -- 'Heuristic' (which is usually much
          faster in large examples), 'FindCubeRoots', or 'UseSUnits'
          (default)

        OUTPUT: nonnegative integer

        EXAMPLES: A rank 0 curve::

            sage: EllipticCurve('11a').three_selmer_rank()       # optional - magma
            0

        A rank 0 curve with rational 3-isogeny but no 3-torsion

        ::

            sage: EllipticCurve('14a3').three_selmer_rank()      # optional - magma
            0

        A rank 0 curve with rational 3-torsion::

            sage: EllipticCurve('14a1').three_selmer_rank()      # optional - magma
            1

        A rank 1 curve with rational 3-isogeny::

            sage: EllipticCurve('91b').three_selmer_rank()       # optional - magma
            2

        A rank 0 curve with nontrivial 3-Sha. The Heuristic option makes
        this about twice as fast as without it.

        ::

            sage: EllipticCurve('681b').three_selmer_rank(algorithm='Heuristic')   # long time (10 seconds); optional - magma
            2
        """
    def rank(self, use_database: bool = True, verbose: bool = False, only_use_mwrank: bool = True, algorithm: str = 'mwrank_lib', proof=None, pari_effort: int = 0):
        """
        Return the rank of this elliptic curve, assuming no conjectures.

        If we fail to provably compute the rank, raises a RuntimeError
        exception.

        INPUT:

        - ``use_database`` -- boolean (default: ``True``); if
          ``True``, try to look up the rank in the Cremona database

        - ``verbose`` -- boolean (default: ``False``); if specified changes
          the verbosity of mwrank computations

        - ``algorithm`` -- (default: ``'mwrank_lib'``) one of:

          - ``'mwrank_shell'`` -- call mwrank shell command

          - ``'mwrank_lib'`` -- call mwrank c library

          - ``'pari'`` -- call ellrank in pari

        - ``only_use_mwrank`` -- boolean (default: ``True``); if ``False`` try
          using analytic rank methods first

        - ``proof`` -- boolean (default: ``None``, see
          ``proof.elliptic_curve`` or ``sage.structure.proof``); note that
          results obtained from databases are considered ``proof=True``

        - ``pari_effort`` -- (default: 0) parameter used in when
          the algorithm ``pari`` is chosen. It measure of the effort
          done to find rational points. Values up to 10 can be chosen;
          the running times increase roughly like the cube of the
          effort value.

        OUTPUT: the rank of the elliptic curve as :class:`Integer`

        IMPLEMENTATION: uses `L`-functions, mwrank, pari, and databases

        EXAMPLES::

            sage: EllipticCurve('11a').rank()
            0
            sage: EllipticCurve('37a').rank()
            1
            sage: EllipticCurve('389a').rank()
            2
            sage: EllipticCurve('5077a').rank()
            3
            sage: EllipticCurve([1, -1, 0, -79, 289]).rank()   # This will use the default proof behavior of True
            4
            sage: EllipticCurve([0, 0, 1, -79, 342]).rank(proof=False)
            5
            sage: EllipticCurve([0, 0, 1, -79, 342]).rank(algorithm='pari')
            5

        Examples with denominators in defining equations::

            sage: E = EllipticCurve([0, 0, 0, 0, -675/4])
            sage: E.rank()
            0
            sage: E = EllipticCurve([0, 0, 1/2, 0, -1/5])
            sage: E.rank()
            1
            sage: E.minimal_model().rank()
            1

        A large example where mwrank doesn't determine the result with certainty, but pari does::

            sage: EllipticCurve([1,0,0,0,37455]).rank(proof=False)
            0
            sage: EllipticCurve([1,0,0,0,37455]).rank(proof=True)
            Traceback (most recent call last):
            ...
            RuntimeError: rank not provably correct (lower bound: 0)
            sage: EllipticCurve([1,0,0,0,37455]).rank(algorithm='pari')
            0

        TESTS::

            sage: EllipticCurve([1,10000]).rank(algorithm='garbage')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm 'garbage'

        An example to check if the points are saturated::

            sage: E = EllipticCurve([0,0, 1, -7, 6])
            sage: E.gens(use_database=False, algorithm='pari') # random
            [(2 : 0 : 1), (-1 : 3 : 1), (11 : 35 : 1)]
            sage: E.saturation(_)[1]
            1

        Since :issue:`23962`, the default is to use the Cremona
        database. We also check that the result is cached correctly::

            sage: E = EllipticCurve([-517, -4528])  # 1888b1
            sage: E.rank(use_database=False)
            Traceback (most recent call last):
            ...
            RuntimeError: rank not provably correct (lower bound: 0)
            sage: E._EllipticCurve_rational_field__rank
            (0, False)
            sage: E.rank()
            0
            sage: E._EllipticCurve_rational_field__rank
            (0, True)

        This example has Sha = Z/4 x Z/4 and the rank cannot be
        determined using pari only::

            sage: E =EllipticCurve([-113^2,0])
            sage: E.rank(use_database=False, verbose=False, algorithm='pari')
            Traceback (most recent call last):
            ...
            RuntimeError: rank not provably correct (lower bound: 0, upper bound:2). Hint: increase pari_effort.
        """
    def gens(self, proof=None, **kwds):
        """
        Return generators for the Mordell-Weil group `E(Q)` *modulo* torsion.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``), see
          ``proof.elliptic_curve`` or ``sage.structure.proof``

        - ``verbose`` -- (default: ``None``) if specified changes the
          verbosity of mwrank computations

        - ``rank1_search`` -- (default: 10), if the curve has analytic
          rank 1, try to find a generator by a direct search up to
          this logarithmic height.  If this fails, the usual mwrank
          procedure is called.

        - ``algorithm`` -- one of the following:

          - ``'mwrank_lib'`` -- default; call mwrank C library

          - ``'mwrank_shell'`` -- call mwrank shell command

          - ``'pari'`` -- use ellrank in pari

        - ``only_use_mwrank`` -- boolean (default: ``True``); if ``False``, first
          attempts to use more naive, natively implemented methods

        - ``use_database`` -- boolean (default: ``True``); if ``True``, attempts to
          find curve and gens in the (optional) database

        - ``descent_second_limit`` -- (default: 12); logarithmic height bound on
          second point search on quartic homogeneous spaces (after
          testing local solubility; sieve-assisted search). Used in 2-descent.
          See also ``second_limit``
          in :meth:`~sage.libs.eclib.interface.mwrank_EllipticCurve.two_descent`

        - ``sat_bound`` -- (default: 1000) bound on primes used in
          saturation.  If the computed bound on the index of the
          points found by two-descent in the Mordell-Weil group is
          greater than this, a warning message will be displayed.

        - ``pari_effort`` -- (default: 0) parameter used in when
          the algorithm ``pari`` is chosen. It measure of the effort
          done to find rational points. Values up to 10 can be chosen,
          the running times increase roughly like the cube of the
          effort value.

        OUTPUT:

        - ``generators`` -- list of generators for the Mordell-Weil
          group modulo torsion

        .. NOTE::

            If you call this with ``proof=False``, then you can use the
            :meth:`~gens_certain` method to find out afterwards
            whether the generators were proved.

        IMPLEMENTATION: Uses Cremona's mwrank C++ library or ellrank in pari.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: E.gens()                 # random output
            [(-1 : 1 : 1), (0 : 0 : 1)]
            sage: E.gens(algorithm='pari')    # random output
            [(5/4 : 5/8 : 1), (0 : 0 : 1)]
            sage: E = EllipticCurve([0,2429469980725060,0,275130703388172136833647756388,0])
            sage: len(E.gens(algorithm='pari'))  # not tested (takes too long)
            14

        A non-integral example::

            sage: E = EllipticCurve([-3/8,-2/3])
            sage: E.gens() # random (up to sign)
            [(10/9 : 29/54 : 1)]

        A non-minimal example::

            sage: E = EllipticCurve('389a1')
            sage: E1 = E.change_weierstrass_model([1/20,0,0,0]); E1
            Elliptic Curve defined by y^2 + 8000*y = x^3 + 400*x^2 - 320000*x
             over Rational Field
            sage: E1.gens() # random (if database not used)
            [(-400 : 8000 : 1), (0 : -8000 : 1)]
            sage: E1.gens(algorithm='pari')   # random
            [(-400 : 8000 : 1), (0 : -8000 : 1)]

        TESTS::

            sage: E = EllipticCurve('389a')
            sage: len(E.gens())
            2
            sage: E.saturation(E.gens())[1]
            1
            sage: len(E.gens(algorithm='pari'))
            2
            sage: E.saturation(E.gens(algorithm='pari'))[1]
            1
            sage: E = EllipticCurve([-3/8,-2/3])
            sage: P = E.lift_x(10/9)
            sage: set(E.gens()) <= set([P,-P])
            True

        Check that :issue:`38813` has been fixed::

            sage: # long time
            sage: E = EllipticCurve([-127^2,0])
            sage: l = E.gens(use_database=False, algorithm='pari', pari_effort=4); l   # random
            [(611429153205013185025/9492121848205441 : 15118836457596902442737698070880/924793900700594415341761 : 1)]
            sage: a = E(611429153205013185025/9492121848205441, 15118836457596902442737698070880/924793900700594415341761)
            sage: assert len(l) == 1 and ((l[0] - a).is_finite_order() or (l[0] + a).is_finite_order())
        """
    def gens_certain(self):
        """
        Return ``True`` if the generators have been proven correct.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.gens()                   # random (up to sign)
            [(0 : -1 : 1)]
            sage: E.gens_certain()
            True

        TESTS::

            sage: E = EllipticCurve('37a1')
            sage: P = E([0,-1])
            sage: set(E.gens()) <= set([P,-P])
            True

            sage: E = EllipticCurve([2, 4, 6, 8, 10])
            sage: E.gens_certain()
            Traceback (most recent call last):
            ...
            RuntimeError: no generators have been computed yet
        """
    def ngens(self, proof=None):
        """
        Return the number of generators of this elliptic curve.

        .. NOTE::

            See :meth:`gens` for further documentation. The function
            :meth:`ngens` calls :meth:`gens` if not already done, but
            only with default parameters.  Better results may be
            obtained by calling :meth:`mwrank` with carefully chosen
            parameters.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.ngens()
            1

            sage: E = EllipticCurve([0,0,0,877,0])
            sage: E.ngens()
            1

            sage: print(E.mwrank('-v0 -b12 -l'))
            Curve [0,0,0,877,0] :   Rank = 1
            Generator 1 is [29604565304828237474403861024284371796799791624792913256602210:-256256267988926809388776834045513089648669153204356603464786949:490078023219787588959802933995928925096061616470779979261000]; height 95.98037...
            Regulator = 95.980...
        """
    def regulator(self, proof=None, precision: int = 53, **kwds):
        """
        Return the regulator of this curve, which must be defined over `\\QQ`.

        INPUT:

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          proof.[tab] or sage.structure.proof). Note that results from
          databases are considered ``proof = True``.

        - ``precision`` -- integer (default: 53); the precision in bits of
          the result

        - ``**kwds`` -- passed to :meth:`gens()` method

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])
            sage: E.regulator()
            0.0511114082399688
            sage: EllipticCurve('11a').regulator()
            1.00000000000000
            sage: EllipticCurve('37a').regulator()
            0.0511114082399688
            sage: EllipticCurve('389a').regulator()
            0.152460177943144
            sage: EllipticCurve('5077a').regulator()
            0.41714355875838...
            sage: EllipticCurve([1, -1, 0, -79, 289]).regulator()
            1.50434488827528
            sage: EllipticCurve([0, 0, 1, -79, 342]).regulator(proof=False)  # long time (6s on sage.math, 2011)
            14.790527570131...
        """
    def saturation(self, points, verbose: bool = False, max_prime: int = -1, min_prime: int = 2):
        """
        Given a list of rational points on `E`, compute the saturation in
        `E(Q)` of the subgroup they generate.

        INPUT:

        - ``points`` -- list of points on `E`

        - ``verbose`` -- boolean (default: ``False``); if ``True``, give
          verbose output

        - ``max_prime`` -- integer (default: `-1`); if `-1`, an
          upper bound is computed for the primes at which the subgroup
          may not be saturated, and saturation is performed for all
          primes up to this bound; otherwise, the bound used is the
          minimum of ``max_prime`` and the computed bound

        - ``min_prime`` -- integer (default: `2`); only do `p`-saturation
          at primes `p` greater than or equal to this

        .. NOTE::

            To saturate at a single prime `p`, set ``max_prime`` and
            ``min_prime`` both to `p`.  One situation where this is
            useful is after mapping saturated points from another
            elliptic curve by a `p`-isogeny, since the images may not
            be `p`-saturated but will be saturated at all other primes.

        OUTPUT:

        - ``saturation`` -- list; points that form a basis for
          the saturation

        - ``index`` -- integer; the index of the group generated
          by points in their saturation

        - ``regulator`` -- real with default precision; regulator of saturated
          points

        ALGORITHM:

        Uses Cremona's ``eclib`` package, which computes a
        bound on the saturation index.  To `p`-saturate, or prove
        `p`-saturation, we consider the reductions of the points
        modulo primes `q` of good reduction such that `E(\\GF{q})` has
        order divisible by `p`.

        .. NOTE::

            In versions of ``eclib`` up to ``v20190909``, division of
            points in ``eclib`` was done using floating point methods,
            without automatic handling of precision, so that
            `p`-saturation sometimes failed unless
            ``mwrank_set_precision()`` was called in advance with a
            suitably high bit precision.  Since version ``v20210310``
            of ``eclib``, division is done using exact methods based on
            division polynomials, and `p`-saturation cannot fail in
            this way.

        .. NOTE::

            The computed index of saturation may be large, in which
            case saturation may take a long time.  For example, the
            rank 4 curve ``EllipticCurve([0,1,1,-9872,374262])`` has a
            saturation index bound of 11816 and takes around 40 seconds
            to prove saturation.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: P=E(0,0)
            sage: Q=5*P; Q
            (1/4 : -5/8 : 1)
            sage: E.saturation([Q])
            ([(0 : 0 : 1)], 5, 0.0511114082399688)

        TESTS:

        See :issue:`10590`.  With ``eclib`` versions up to
        ``v20190909``, this example would loop forever at default
        precision.  Since version ``v20210310`` it runs fine::

            sage: E = EllipticCurve([1, 0, 1, -977842, -372252745])
            sage: P = E([-192128125858676194585718821667542660822323528626273/336995568430319276695106602174283479617040716649, 70208213492933395764907328787228427430477177498927549075405076353624188436/195630373799784831667835900062564586429333568841391304129067339731164107, 1])
            sage: P.height()
            113.302910926080
            sage: E.saturation([P])
            ([(-192128125858676194585718821667542660822323528626273/336995568430319276695106602174283479617040716649 : 70208213492933395764907328787228427430477177498927549075405076353624188436/195630373799784831667835900062564586429333568841391304129067339731164107 : 1)], 1, 113.302910926080)
            sage: (Q,), ind, reg = E.saturation([2*P])
            sage: 2*Q == 2*P
            True
            sage: ind
            2
            sage: reg
            113.302910926080

        See :issue:`10840`.  This used to cause eclib to crash since the
        curve is non-minimal at 2::

            sage: E = EllipticCurve([0,0,0,-13711473216,0])
            sage: P = E([-19992,16313472])
            sage: Q = E([-24108,-17791704])
            sage: R = E([-97104,-20391840])
            sage: S = E([-113288,-9969344])
            sage: E.saturation([P,Q,R,S])
            ([(-19992 : 16313472 : 1), (-24108 : -17791704 : 1), (-97104 : -20391840 : 1), (-113288 : -9969344 : 1)], 1, 172.792031341679)

        See :issue:`34029`.  With eclib versions prior to 20220621 this failed to saturate::

            sage: E = EllipticCurve([0, 0, 0, -17607, -889490])
            sage: Q = E([-82,54])
            sage: E.saturation([2*Q], max_prime=10)
            ([(-82 : 54 : 1)], 2, 2.36570863272098)
        """
    def CPS_height_bound(self):
        '''
        Return the Cremona-Prickett-Siksek height bound. This is a
        floating point number B such that if P is a rational point on
        the curve, then `h(P) \\le \\hat{h}(P) + B`, where `h(P)` is
        the naive logarithmic height of `P` and `\\hat{h}(P)` is the
        canonical height.

        .. SEEALSO::

            :meth:`silverman_height_bound` for a bound that also works for
            points over number fields.

        EXAMPLES::

            sage: E = EllipticCurve("11a")
            sage: E.CPS_height_bound()
            2.8774743273580445
            sage: E = EllipticCurve("5077a")
            sage: E.CPS_height_bound()
            0.0
            sage: E = EllipticCurve([1,2,3,4,1])
            sage: E.CPS_height_bound()
            Traceback (most recent call last):
            ...
            RuntimeError: curve must be minimal.
            sage: F = E.quadratic_twist(-19)
            sage: F
            Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 + 1376*x - 130 over Rational Field
            sage: F.CPS_height_bound()
            0.6555158376972852

        IMPLEMENTATION:

        Call the corresponding mwrank C++ library function.  Note that
        the formula in the [CPS2006]_ paper is given for number fields.  It is
        only the implementation in Sage that restricts to the rational
        field.
        '''
    def silverman_height_bound(self, algorithm: str = 'default'):
        """
        Return the Silverman height bound.

        This is a positive real (floating point) number B such that
        for all points `P` on the curve over any number field,
        `|h(P) - \\hat{h}(P)| \\leq B`, where `h(P)` is the naive
        logarithmic height of `P` and `\\hat{h}(P)` is the canonical height.

        INPUT:

        - ``algorithm`` -- one of the following:

          * ``'default'`` (default) - compute using a Python
            implementation in Sage

          * ``'mwrank'`` -- use a C++ implementation in the mwrank
            library

        .. NOTE::

            - The CPS_height_bound is often better (i.e. smaller) than
              the Silverman bound, but it only applies for points over
              the base field, whereas the Silverman bound works over
              all number fields.

            - The Silverman bound is also fairly straightforward to
              compute over number fields, but isn't implemented here.

            - Silverman's paper is 'The Difference Between the Weil
              Height and the Canonical Height on Elliptic Curves',
              Math. Comp., Volume 55, Number 192, pages 723-743.  We
              use a correction by Bremner with 0.973 replaced by 0.961,
              as explained in the source code to mwrank (htconst.cc).

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.silverman_height_bound()
            4.825400758180918
            sage: E.silverman_height_bound(algorithm='mwrank')
            4.825400758180918
            sage: E.CPS_height_bound()
            0.16397076103046915
        """
    def point_search(self, height_limit, verbose: bool = False, rank_bound=None):
        """
        Search for points on a curve up to an input bound on the naive
        logarithmic height.

        INPUT:

        - ``height_limit`` -- float; bound on naive height

        - ``verbose`` -- boolean (default: ``False``);
          if ``True``, report on the saturation process
          otherwise just return the result

        - ``rank_bound`` -- boolean (optional);
          if provided, stop saturating once we find this many
          independent nontorsion points

        OUTPUT: points (list) - list of independent points which generate
        the subgroup of the Mordell-Weil group generated by the points
        found and then saturated.

        .. WARNING::

            height_limit is logarithmic, so increasing by 1 will cause
            the running time to increase by a factor of approximately
            4.5 (=exp(1.5)).

        IMPLEMENTATION: Uses Michael Stoll's ratpoints module in PARI/GP.

        EXAMPLES::

            sage: E = EllipticCurve('389a1')
            sage: E.point_search(1, verbose=False)
            [(-1 : 1 : 1), (0 : 0 : 1)]

        Increasing the height_limit takes longer, but finds no more
        points::

            sage: E.point_search(10, verbose=False)  # long time
            [(-1 : 1 : 1), (0 : 0 : 1)]

        In fact this curve has rank 2 so no more than 2 points will ever be
        output, but we are not using this fact.

        ::

            sage: E.saturation(_)
            ([(-1 : 1 : 1), (0 : 0 : 1)], 1, 0.152460177943144)

        What this shows is that if the rank is 2 then the points listed do
        generate the Mordell-Weil group (mod torsion). Finally,

        ::

            sage: E.rank()
            2

        If we only need one independent generator::

            sage: E.point_search(5, verbose=False, rank_bound=1)
            [(-2 : 0 : 1)]
        """
    def selmer_rank(self, algorithm: str = 'pari'):
        """
        Return the rank of the 2-Selmer group of the curve.

        INPUT:

        - ``algorithm`` -- either ``'pari'`` (default) or ``'mwrank'``

        EXAMPLES:
        This example has rank 1, Sha[2] of order 4 and
        a single rational 2-torsion point::

            sage: E = EllipticCurve([1, 1, 1, 508, -2551])
            sage: E.selmer_rank()
            4
            sage: E.selmer_rank(algorithm='mwrank')
            4

        The following is the curve 960d1, which has rank 0, but
        Sha of order 4::

            sage: E = EllipticCurve([0, -1, 0, -900, -10098])
            sage: E.selmer_rank()
            3
            sage: E.selmer_rank(algorithm='mwrank')
            3

        This curve has rank 1, and 4 elements in Sha[2].
        Yet the order of Sha is 16, so that group is the product
        of two cyclic groups of order 4::

            sage: E = EllipticCurve([1, 0, 0, -150752, -22541610])
            sage: E.selmer_rank()
            4

        Instead in this last example of rank 0, Sha is a product of four cyclic groups of order 2::

            sage: E = EllipticCurve([1, 0, 0, -49280, -4214808])
            sage: E.selmer_rank()
            5
            sage: E.rank()
            0
        """
    def rank_bound(self, algorithm: str = 'pari'):
        '''
        Return the upper bound on the rank of the curve,
        computed using a 2-descent.

        INPUT:

        - ``algorithm`` -- either ``\'pari\'`` (default) or ``\'mwrank\'``

        In many cases, this is the actual rank of the
        curve.

        EXAMPLES::

            sage: E = EllipticCurve("389a1")
            sage: E.rank_bound()
            2

        The following is the curve 571a1, which has
        rank 0, but Sha of order 4, yet pari, using the Cassels
        pairing is able to show that the rank is 0.
        The 2-descent in mwrank only determines a weaker upper bound::

            sage: E = EllipticCurve([0, -1, 1, -929, -10595])
            sage: E.rank_bound()
            0
            sage: E.rank_bound(algorithm=\'mwrank\')
            2

        In the following last example, both algorithm only determine a rank bound larger than the actual rank::

            sage: E = EllipticCurve([1, 1, 1, -896670, -327184905])
            sage: E.rank_bound()
            2
            sage: E.rank_bound(algorithm=\'mwrank\')
            2
            sage: E.rank(only_use_mwrank=False) # uses L-function
            0
        '''
    def an(self, n):
        """
        The ``n``-th Fourier coefficient of the modular form corresponding to
        this elliptic curve, where ``n`` is a positive integer.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: [E.an(n) for n in range(20) if n>0]
            [1, -2, -3, 2, -2, 6, -1, 0, 6, 4, -5, -6, -2, 2, 6, -4, 0, -12, 0]
        """
    def ap(self, p):
        """
        The ``p``-th Fourier coefficient of the modular form corresponding to
        this elliptic curve, where ``p`` is prime.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: [E.ap(p) for p in prime_range(50)]
            [-2, -3, -2, -1, -5, -2, 0, 0, 2, 6, -4, -1, -9, 2, -9]
        """
    def minimal_model(self):
        """
        Return the unique minimal Weierstrass equation for this elliptic
        curve.

        This is the model with minimal discriminant and
        `a_1,a_2,a_3 \\in \\{0,\\pm 1\\}`.

        EXAMPLES::

            sage: E = EllipticCurve([10,100,1000,10000,1000000])
            sage: E.minimal_model()
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + x + 1 over Rational Field
        """
    def is_minimal(self):
        """
        Return ``True`` iff this elliptic curve is a reduced minimal model.

        The unique minimal Weierstrass equation for this elliptic curve.
        This is the model with minimal discriminant and
        `a_1,a_2,a_3 \\in \\{0,\\pm 1\\}`.

        .. TODO::

            This is not very efficient since it just computes the
            minimal model and compares. A better implementation using the
            Kraus conditions would be preferable.

        EXAMPLES::

            sage: E = EllipticCurve([10,100,1000,10000,1000000])
            sage: E.is_minimal()
            False
            sage: E = E.minimal_model()
            sage: E.is_minimal()
            True
        """
    def is_p_minimal(self, p):
        """
        Test if curve is `p`-minimal at a given prime `p`.

        INPUT:

        - ``p`` -- a prime

        OUTPUT:

        - ``True`` -- if curve is `p`-minimal
        - ``False`` -- if curve is not `p`-minimal

        EXAMPLES::

            sage: E = EllipticCurve('441a2')
            sage: E.is_p_minimal(7)
            True

        ::

            sage: E = EllipticCurve([0,0,0,0,(2*5*11)**10])
            sage: [E.is_p_minimal(p) for p in prime_range(2,24)]
            [False, True, False, True, False, True, True, True, True]
        """
    def kodaira_type(self, p):
        """
        Local Kodaira type of the elliptic curve at ``p``.

        INPUT:

        - ``p`` -- an integral prime

        OUTPUT:

        - the Kodaira type of this elliptic curve at ``p``,
          as a :class:`KodairaSymbol`

        EXAMPLES::

            sage: E = EllipticCurve('124a')
            sage: E.kodaira_type(2)
            IV
        """
    kodaira_symbol = kodaira_type
    def kodaira_type_old(self, p):
        """
        Local Kodaira type of the elliptic curve at ``p``.

        INPUT:

        - ``p`` -- an integral prime

        OUTPUT:

        - the Kodaira type of this elliptic curve at ``p``,
          as a :class:`KodairaSymbol`

        EXAMPLES::

            sage: E = EllipticCurve('124a')
            sage: E.kodaira_type_old(2)
            IV
        """
    def tamagawa_number(self, p):
        """
        The Tamagawa number of the elliptic curve at ``p``.

        This is the order of the component group
        `E(\\QQ_p)/E^0(\\QQ_p)`.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: E.tamagawa_number(11)
            5
            sage: E = EllipticCurve('37b')
            sage: E.tamagawa_number(37)
            3
        """
    def tamagawa_number_old(self, p):
        """
        The Tamagawa number of the elliptic curve at ``p``.

        This is the order of the component group
        `E(\\QQ_p)/E^0(\\QQ_p)`.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: E.tamagawa_number_old(11)
            5
            sage: E = EllipticCurve('37b')
            sage: E.tamagawa_number_old(37)
            3
        """
    def tamagawa_exponent(self, p):
        """
        The Tamagawa index of the elliptic curve at ``p``.

        This is the index of the component group
        `E(\\QQ_p)/E^0(\\QQ_p)`. It equals the
        Tamagawa number (as the component group is cyclic) except for types
        `I_m^*` (`m` even) when the group can be
        `C_2 \\times C_2`.

        EXAMPLES::

            sage: E = EllipticCurve('816a1')
            sage: E.tamagawa_number(2)
            4
            sage: E.tamagawa_exponent(2)
            2
            sage: E.kodaira_symbol(2)
            I2*

        ::

            sage: E = EllipticCurve('200c4')
            sage: E.kodaira_symbol(5)
            I4*
            sage: E.tamagawa_number(5)
            4
            sage: E.tamagawa_exponent(5)
            2

        See :issue:`4715`::

            sage: E = EllipticCurve('117a3')
            sage: E.tamagawa_exponent(13)
            4
        """
    def tamagawa_product(self):
        """
        Return the product of the Tamagawa numbers.

        EXAMPLES::

            sage: E = EllipticCurve('54a')
            sage: E.tamagawa_product ()
            3
        """
    def real_components(self) -> int:
        """
        Return the number of real components.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: E.real_components ()
            2
            sage: E = EllipticCurve('37b')
            sage: E.real_components ()
            2
            sage: E = EllipticCurve('11a')
            sage: E.real_components ()
            1
        """
    def has_good_reduction_outside_S(self, S=None) -> bool:
        """
        Test if this elliptic curve has good reduction outside ``S``.

        INPUT:

        - ``S`` -- list of primes (default: ``[]``)

        .. NOTE::

            Primality of elements of ``S`` is not checked, and the output
            is undefined if ``S`` is not a list or contains non-primes.

            This only tests the given model, so should only be applied to
            minimal models.

        EXAMPLES::

            sage: EllipticCurve('11a1').has_good_reduction_outside_S([11])
            True
            sage: EllipticCurve('11a1').has_good_reduction_outside_S([2])
            False
            sage: EllipticCurve('2310a1').has_good_reduction_outside_S([2,3,5,7])
            False
            sage: EllipticCurve('2310a1').has_good_reduction_outside_S([2,3,5,7,11])
            True
        """
    def period_lattice(self, embedding=None):
        """
        Return the period lattice of the elliptic curve with respect to
        the differential `dx/(2y + a_1x + a_3)`.

        INPUT:

        - ``embedding`` -- ignored (for compatibility with the
          period_lattice function for elliptic_curve_number_field)

        OUTPUT:

        (period lattice) The :class:`~sage.schemes.elliptic_curves.period_lattice.PeriodLattice_ell`
        object associated to this elliptic curve (with respect to the natural embedding of
        `\\QQ` into `\\RR`).

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: E.period_lattice()
            Period lattice associated to
             Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        """
    def elliptic_exponential(self, z, embedding=None):
        """
        Compute the elliptic exponential of a complex number with
        respect to the elliptic curve.

        INPUT:

        - ``z`` -- a complex number

        - ``embedding`` -- ignored (for compatibility with the
          period_lattice function for elliptic_curve_number_field)

        OUTPUT:

        The image of `z` modulo `L` under the Weierstrass parametrization
        `\\CC/L \\to E(\\CC)`.

        .. NOTE::

            The precision is that of the input ``z``, or the default
            precision of 53 bits if ``z`` is exact.

        EXAMPLES::

            sage: E = EllipticCurve([1,1,1,-8,6])
            sage: P = E([1,-2])
            sage: z = P.elliptic_logarithm() # default precision is 100 here
            sage: E.elliptic_exponential(z)
            (1.0000000000000000000000000000 : -2.0000000000000000000000000000 : 1.0000000000000000000000000000)
            sage: z = E([1,-2]).elliptic_logarithm(precision=201)
            sage: E.elliptic_exponential(z)
            (1.00000000000000000000000000000000000000000000000000000000000 : -2.00000000000000000000000000000000000000000000000000000000000 : 1.00000000000000000000000000000000000000000000000000000000000)

        ::

            sage: E = EllipticCurve('389a')
            sage: Q = E([3,5])
            sage: E.elliptic_exponential(Q.elliptic_logarithm())
            (3.0000000000000000000000000000 : 5.0000000000000000000000000000 : 1.0000000000000000000000000000)
            sage: P = E([-1,1])
            sage: P.elliptic_logarithm()
            0.47934825019021931612953301006 + 0.98586885077582410221120384908*I
            sage: E.elliptic_exponential(P.elliptic_logarithm())
            (-1.0000000000000000000000000000 : 1.0000000000000000000000000000 : 1.0000000000000000000000000000)

        Some torsion examples::

            sage: w1,w2 = E.period_lattice().basis()
            sage: E.two_division_polynomial().roots(CC,multiplicities=False)
            [-2.0403022002854..., 0.13540924022175..., 0.90489296006371...]
            sage: [E.elliptic_exponential((a*w1+b*w2)/2)[0] for a,b in [(0,1),(1,1),(1,0)]]
            [-2.0403022002854..., 0.13540924022175..., 0.90489296006371...]

            sage: E.division_polynomial(3).roots(CC,multiplicities=False)
            [-2.88288879135...,
             1.39292799513...,
             0.078313731444316... - 0.492840991709...*I,
             0.078313731444316... + 0.492840991709...*I]
            sage: [E.elliptic_exponential((a*w1+b*w2)/3)[0] for a,b in [(0,1),(1,0),(1,1),(2,1)]]
            [-2.8828887913533..., 1.39292799513138,
             0.0783137314443... - 0.492840991709...*I,
             0.0783137314443... + 0.492840991709...*I]

        Observe that this is a group homomorphism (modulo rounding error)::

            sage: z = CC.random_element()
            sage: v = 2 * E.elliptic_exponential(z)
            sage: w = E.elliptic_exponential(2 * z)
            sage: def err(a, b):
            ....:     err = abs(a - b)
            ....:     if a + b:
            ....:         err = min(err, err / abs(a + b))
            ....:     return err
            sage: err(v[0], w[0]) + err(v[1], w[1])  # abs tol 1e-13
            0.0
        """
    def lseries(self):
        """
        Return the `L`-series of this elliptic curve.

        Further documentation is available for the functions which apply to
        the `L`-series.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.lseries()
            Complex L-series of the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        """
    def lseries_gross_zagier(self, A):
        """
        Return the Gross-Zagier `L`-series attached to ``self``
        and an ideal class `A`.

        INPUT:

        - ``A`` -- an ideal class in an imaginary quadratic number field `K`

        This `L`-series `L(E,A,s)` is defined as the product of a shifted `L`-function of the
        quadratic character associated to `K` and the Dirichlet series whose `n`-th
        coefficient is the product of the `n`-th factor of the `L`-series of `E` and
        the number of integral ideal in `A` of norm `n`. For any character `\\chi`
        on the class group of `K`, one gets `L_K(E,\\chi,s) = \\sum_{A} \\chi(A) L(E,A,s)`
        where `A` runs through the class group of `K`.

        For the exact definition see section IV of [GZ1986]_.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: K.<a> = QuadraticField(-40)
            sage: A = K.class_group().gen(0); A
            Fractional ideal class (2, 1/2*a)
            sage: L = E.lseries_gross_zagier(A)  ; L
            Gross Zagier L-series attached to
             Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
             with ideal class Fractional ideal class (2, 1/2*a)
            sage: L(1)
            0.000000000000000
            sage: L.taylor_series(1, 5)
            0.000000000000000 - 5.51899839494458*z + 13.6297841350649*z^2 - 16.2292417817675*z^3 + 7.94788823722712*z^4 + O(z^5)

        These should be equal::

            sage: L(2) + E.lseries_gross_zagier(A^2)(2)
            0.502803417587467
            sage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)
            0.502803417587467
        """
    def Lambda(self, s, prec):
        """
        Return the value of the Lambda-series of the elliptic curve `E` at
        ``s``, where ``s`` can be any complex number.

        IMPLEMENTATION:

        Fairly *slow* computation using the definitions implemented in Python.

        Uses ``prec`` terms of the power series.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: E.Lambda(1.4 + 0.5*I, 50)
            -0.354172680517... + 0.874518681720...*I
        """
    def is_local_integral_model(self, *p):
        """
        Test if ``self`` is integral at the prime `p`, or at all the
        primes if `p` is a list or tuple of primes.

        EXAMPLES::

            sage: E = EllipticCurve([1/2, 1/5, 1/5, 1/5, 1/5])
            sage: [E.is_local_integral_model(p) for p in (2,3,5)]
            [False, True, False]
            sage: E.is_local_integral_model(2,3,5)
            False
            sage: Eint2=E.local_integral_model(2)
            sage: Eint2.is_local_integral_model(2)
            True
        """
    def local_integral_model(self, p):
        """
        Return a model of ``self`` which is integral at the prime `p`.

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])
            sage: E.local_integral_model(2)
            Elliptic Curve defined by y^2 + 1/27*y = x^3 - 7/81*x + 2/243 over Rational Field
            sage: E.local_integral_model(3)
            Elliptic Curve defined by y^2 + 1/8*y = x^3 - 7/16*x + 3/32 over Rational Field
            sage: E.local_integral_model(2).local_integral_model(3) == EllipticCurve('5077a1')
            True
        """
    def is_global_integral_model(self):
        """
        Return ``True`` iff ``self`` is integral at all primes.

        EXAMPLES::

            sage: E = EllipticCurve([1/2, 1/5, 1/5, 1/5, 1/5])
            sage: E.is_global_integral_model()
            False
            sage: Emin=E.global_integral_model()
            sage: Emin.is_global_integral_model()
            True
        """
    def global_integral_model(self):
        """
        Return a model of ``self`` which is integral at all primes.

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])
            sage: F = E.global_integral_model(); F
            Elliptic Curve defined by y^2 + y = x^3 - 7*x + 6 over Rational Field
            sage: F == EllipticCurve('5077a1')
            True
        """
    integral_model = global_integral_model
    def integral_short_weierstrass_model(self):
        """
        Return a model of the form `y^2 = x^3 + ax + b` for this
        curve with `a,b\\in\\ZZ`.

        EXAMPLES::

            sage: E = EllipticCurve('17a1')
            sage: E.integral_short_weierstrass_model()
            Elliptic Curve defined by y^2  = x^3 - 11*x - 890 over Rational Field
        """
    def modular_degree(self, algorithm: str = 'sympow', M: int = 1):
        '''
        Return the modular degree at level `MN` of this elliptic curve. The case
        `M==1` corresponds to the classical definition of modular degree.

        When `M>1`, the function returns the degree of the map from `X_0(MN) \\to A`, where
        A is the abelian variety generated by embeddings of `E` into `J_0(MN)`.

        The result is cached. Subsequent calls, even with a different
        algorithm, just returned the cached result. The algorithm argument is ignored
        when `M>1`.

        INPUT:

        - ``algorithm`` -- string; one of

          * ``\'sympow\'`` -- (default) use Mark Watkin\'s (newer) C
            program sympow

          * ``\'magma\'`` -- requires that MAGMA be installed (also
            implemented by Mark Watkins)

        - ``M`` -- nonnegative integer; the modular degree at level `MN`
          is returned (see above)

        .. NOTE::

            On 64-bit computers ec does not work, so Sage uses sympow
            even if ec is selected on a 64-bit computer.

        The correctness of this function when called with algorithm "sympow"
        is subject to the following three hypothesis:

        - Manin\'s conjecture: the Manin constant is 1

        - Steven\'s conjecture: the `X_1(N)`-optimal quotient is
          the curve with minimal Faltings height. (This is proved in most
          cases.)

        - The modular degree fits in a machine double, so it better be
          less than about 50-some bits. (If you use sympow this constraint
          does not apply.)

        Moreover for all algorithms, computing a certain value of an
        `L`-function \'uses a heuristic method that discerns when
        the real-number approximation to the modular degree is within
        epsilon [=0.01 for algorithm=\'sympow\'] of the same integer for 3
        consecutive trials (which occur maybe every 25000 coefficients or
        so). Probably it could just round at some point. For rigour, you
        would need to bound the tail by assuming (essentially) that all the
        `a_n` are as large as possible, but in practice they
        exhibit significant (square root) cancellation. One difficulty is
        that it doesn\'t do the sum in 1-2-3-4 order; it uses
        1-2-4-8--3-6-12-24-9-18- (Euler product style) instead, and so you
        have to guess ahead of time at what point to curtail this
        expansion.\' (Quote from an email of Mark Watkins.)

        .. NOTE::

            If the curve is loaded from the large Cremona database,
            then the modular degree is taken from the database.

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: E.modular_degree()
            1
            sage: E = EllipticCurve(\'5077a\')
            sage: E.modular_degree()
            1984
            sage: factor(1984)
            2^6 * 31

        ::

            sage: EllipticCurve([0, 0, 1, -7, 6]).modular_degree()
            1984
            sage: EllipticCurve([0, 0, 1, -7, 6]).modular_degree(algorithm=\'sympow\')
            1984
            sage: EllipticCurve([0, 0, 1, -7, 6]).modular_degree(algorithm=\'magma\')  # optional - magma
            1984

        We compute the modular degree of the curve with rank 4 having
        smallest (known) conductor::

            sage: E = EllipticCurve([1, -1, 0, -79, 289])
            sage: factor(E.conductor())  # conductor is 234446
            2 * 117223
            sage: factor(E.modular_degree())
            2^7 * 2617

        Higher level cases::

            sage: E = EllipticCurve(\'11a\')
            sage: for M in range(1,11): print(E.modular_degree(M=M)) # long time (20s on 2009 MBP)
            1
            1
            3
            2
            7
            45
            12
            16
            54
            245
        '''
    def modular_parametrization(self):
        """
        Return the modular parametrization of this elliptic curve, which is
        a map from `X_0(N)` to self, where `N` is the conductor of ``self``.

        EXAMPLES::

            sage: E = EllipticCurve('15a')
            sage: phi = E.modular_parametrization(); phi
            Modular parameterization
             from the upper half plane
               to Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 10*x - 10
                  over Rational Field
            sage: z = 0.1 + 0.2j
            sage: phi(z)
            (8.20822465478531 - 13.1562816054682*I : -8.79855099049364 + 69.4006129342200*I : 1.00000000000000)

        This map is actually a map on `X_0(N)`, so equivalent representatives
        in the upper half plane map to the same point::

            sage: phi((-7*z-1)/(15*z+2))
            (8.20822465478524 - 13.1562816054681*I : -8.79855099049... + 69.4006129342...*I : 1.00000000000000)

        We can also get a series expansion of this modular parameterization::

            sage: E = EllipticCurve('389a1')
            sage: X, Y = E.modular_parametrization().power_series()
            sage: X
            q^-2 + 2*q^-1 + 4 + 7*q + 13*q^2 + 18*q^3 + 31*q^4 + 49*q^5 + 74*q^6 + 111*q^7 + 173*q^8 + 251*q^9 + 379*q^10 + 560*q^11 + 824*q^12 + 1199*q^13 + 1773*q^14 + 2548*q^15 + 3722*q^16 + 5374*q^17 + O(q^18)
            sage: Y
            -q^-3 - 3*q^-2 - 8*q^-1 - 17 - 33*q - 61*q^2 - 110*q^3 - 186*q^4 - 320*q^5 - 528*q^6 - 861*q^7 - 1383*q^8 - 2218*q^9 - 3472*q^10 - 5451*q^11 - 8447*q^12 - 13020*q^13 - 19923*q^14 - 30403*q^15 - 46003*q^16 + O(q^17)

        The following should give 0, but only approximately::

            sage: q = X.parent().gen()
            sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0
            True
        """
    def congruence_number(self, M: int = 1):
        """
        The case `M==1` corresponds to the classical definition of congruence number:
        Let `X` be the subspace of `S_2(\\Gamma_0(N))` spanned by the newform
        associated with this elliptic curve, and `Y` be orthogonal complement
        of `X` under the Petersson inner product. Let `S_X` and `S_Y` be the
        intersections of `X` and `Y` with `S_2(\\Gamma_0(N), \\ZZ)`. The congruence
        number is defined to be `[S_X \\oplus S_Y : S_2(\\Gamma_0(N),\\ZZ)]`.
        It measures congruences between `f` and elements of `S_2(\\Gamma_0(N),\\ZZ)`
        orthogonal to `f`.

        The congruence number for higher levels, when M>1, is defined as above, but
        instead considers `X` to be the subspace of `S_2(\\Gamma_0(MN))` spanned by
        embeddings into `S_2(\\Gamma_0(MN))` of the newform associated with this
        elliptic curve; this subspace has dimension `\\sigma_0(M)`, i.e. the number
        of divisors of `M`. Let `Y` be the orthogonal complement in `S_2(\\Gamma_0(MN))`
        of `X` under the Petersson inner product, and `S_X` and `S_Y` the intersections
        of `X` and `Y` with `S_2(\\Gamma_0(MN), \\ZZ)` respectively. Then the congruence
        number at level `MN` is `[S_X \\oplus S_Y : S_2(\\Gamma_0(MN),\\ZZ)]`.

        INPUT:

        - ``M`` -- nonnegative integer; congruence number is computed
          at level `MN`, where `N` is the conductor of ``self``

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: E.congruence_number()
            2
            sage: E.congruence_number()
            2
            sage: E = EllipticCurve('54b')
            sage: E.congruence_number()
            6
            sage: E.modular_degree()
            2
            sage: E = EllipticCurve('242a1')
            sage: E.modular_degree()
            16
            sage: E.congruence_number()  # long time (4s on sage.math, 2011)
            176

        Higher level cases::

            sage: E = EllipticCurve('11a')
            sage: for M in range(1,11): print(E.congruence_number(M)) # long time (20s on 2009 MBP)
            1
            1
            3
            2
            7
            45
            12
            4
            18
            245

        It is a theorem of Ribet that the congruence number (at level `N`) is equal
        to the modular degree in the case of square free conductor. It is a conjecture
        of Agashe, Ribet, and Stein that `ord_p(c_f/m_f) \\le ord_p(N)/2`.

        TESTS::

            sage: E = EllipticCurve('11a')
            sage: E.congruence_number()
            1
        """
    def cremona_label(self, space: bool = False):
        """
        Return the Cremona label associated to (the minimal model) of this
        curve, if it is known. If not, raise a :exc:`LookupError` exception.

        EXAMPLES::

            sage: E = EllipticCurve('389a1')
            sage: E.cremona_label()
            '389a1'

        The default database only contains conductors up to 10000, so any
        curve with conductor greater than that will cause an error to be
        raised. The optional package ``database_cremona_ellcurve``
        contains many more curves.

        ::

            sage: E = EllipticCurve([1, -1, 0, -79, 289])
            sage: E.conductor()
            234446
            sage: E.cremona_label()  # optional - database_cremona_ellcurve
            '234446a1'
            sage: E = EllipticCurve((0, 0, 1, -79, 342))
            sage: E.conductor()
            19047851
            sage: E.cremona_label()
            Traceback (most recent call last):
            ...
            LookupError: Cremona database does not contain entry for
            Elliptic Curve defined by y^2 + y = x^3 - 79*x + 342 over Rational Field
        """
    label = cremona_label
    def reduction(self, p):
        """
        Return the reduction of the elliptic curve at a prime of good
        reduction.

        .. NOTE::

            The actual reduction is done in ``self.change_ring(GF(p))``;
            the reduction is performed after changing to a model which
            is minimal at p.

        INPUT:

        - ``p`` -- a (positive) prime number

        OUTPUT: an elliptic curve over the finite field `\\GF{p}`

        EXAMPLES::

            sage: E = EllipticCurve('389a1')
            sage: E.reduction(2)
            Elliptic Curve defined by y^2 + y = x^3 + x^2 over Finite Field of size 2
            sage: E.reduction(3)
            Elliptic Curve defined by y^2 + y = x^3 + x^2 + x over Finite Field of size 3
            sage: E.reduction(5)
            Elliptic Curve defined by y^2 + y = x^3 + x^2 + 3*x over Finite Field of size 5
            sage: E.reduction(38)
            Traceback (most recent call last):
            ...
            AttributeError: p must be prime.
            sage: E.reduction(389)
            Traceback (most recent call last):
            ...
            AttributeError: The curve must have good reduction at p.
            sage: E = EllipticCurve([5^4, 5^6])
            sage: E.reduction(5)
            Elliptic Curve defined by y^2 = x^3 + x + 1 over Finite Field of size 5
        """
    def torsion_order(self):
        """
        Return the order of the torsion subgroup.

        EXAMPLES::

            sage: e = EllipticCurve('11a')
            sage: e.torsion_order()
            5
            sage: type(e.torsion_order())
            <... 'sage.rings.integer.Integer'>
            sage: e = EllipticCurve([1,2,3,4,5])
            sage: e.torsion_order()
            1
            sage: type(e.torsion_order())
            <... 'sage.rings.integer.Integer'>
        """
    def torsion_subgroup(self):
        """
        Return the torsion subgroup of this elliptic curve.

        OUTPUT: the EllipticCurveTorsionSubgroup instance associated to
        this elliptic curve.

        .. NOTE::

            To see the torsion points as a list, use :meth:`.torsion_points`.

        EXAMPLES::

            sage: EllipticCurve('11a').torsion_subgroup()
            Torsion Subgroup isomorphic to Z/5 associated to the
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: EllipticCurve('37b').torsion_subgroup()
            Torsion Subgroup isomorphic to Z/3 associated to the
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 23*x - 50 over Rational Field

        ::

            sage: e = EllipticCurve([-1386747,368636886]); e
            Elliptic Curve defined by y^2 = x^3 - 1386747*x + 368636886 over Rational Field
            sage: G = e.torsion_subgroup(); G
            Torsion Subgroup isomorphic to Z/8 + Z/2 associated to the
             Elliptic Curve defined by y^2 = x^3 - 1386747*x + 368636886 over
             Rational Field
            sage: G.0*3 + G.1
            (1227 : 22680 : 1)
            sage: G.1
            (282 : 0 : 1)
            sage: list(G)
            [(0 : 1 : 0), (147 : -12960 : 1), (2307 : -97200 : 1), (-933 : -29160 : 1),
             (1011 : 0 : 1), (-933 : 29160 : 1), (2307 : 97200 : 1), (147 : 12960 : 1),
             (-1293 : 0 : 1), (1227 : 22680 : 1), (-285 : 27216 : 1), (8787 : 816480 : 1),
             (282 : 0 : 1), (8787 : -816480 : 1), (-285 : -27216 : 1), (1227 : -22680 : 1)]
        """
    def torsion_points(self):
        """
        Return the torsion points of this elliptic curve as a sorted list.

        OUTPUT: list of all the torsion points on this elliptic curve

        EXAMPLES::

            sage: EllipticCurve('11a').torsion_points()
            [(0 : 1 : 0), (5 : -6 : 1), (5 : 5 : 1), (16 : -61 : 1), (16 : 60 : 1)]
            sage: EllipticCurve('37b').torsion_points()
            [(0 : 1 : 0), (8 : -19 : 1), (8 : 18 : 1)]

        Some curves with large torsion groups::

            sage: E = EllipticCurve([-1386747, 368636886])
            sage: T = E.torsion_subgroup(); T
            Torsion Subgroup isomorphic to Z/8 + Z/2 associated to the
             Elliptic Curve defined by y^2 = x^3 - 1386747*x + 368636886 over
             Rational Field
            sage: E.torsion_points()
            [(0 : 1 : 0),
             (-1293 : 0 : 1),
             (-933 : -29160 : 1),
             (-933 : 29160 : 1),
             (-285 : -27216 : 1),
             (-285 : 27216 : 1),
             (147 : -12960 : 1),
             (147 : 12960 : 1),
             (282 : 0 : 1),
             (1011 : 0 : 1),
             (1227 : -22680 : 1),
             (1227 : 22680 : 1),
             (2307 : -97200 : 1),
             (2307 : 97200 : 1),
             (8787 : -816480 : 1),
             (8787 : 816480 : 1)]
            sage: EllipticCurve('210b5').torsion_points()
            [(0 : 1 : 0),
             (-41/4 : 37/8 : 1),
             (-5 : -103 : 1),
             (-5 : 107 : 1),
             (10 : -208 : 1),
             (10 : 197 : 1),
             (37 : -397 : 1),
             (37 : 359 : 1),
             (100 : -1153 : 1),
             (100 : 1052 : 1),
             (415 : -8713 : 1),
             (415 : 8297 : 1)]
            sage: EllipticCurve('210e2').torsion_points()
            [(0 : 1 : 0),
             (-36 : 18 : 1),
             (-26 : -122 : 1),
             (-26 : 148 : 1),
             (-8 : -122 : 1),
             (-8 : 130 : 1),
             (4 : -62 : 1),
             (4 : 58 : 1),
             (31/4 : -31/8 : 1),
             (28 : -14 : 1),
             (34 : -122 : 1),
             (34 : 88 : 1),
             (64 : -482 : 1),
             (64 : 418 : 1),
             (244 : -3902 : 1),
             (244 : 3658 : 1)]
        """
    @cached_method
    def root_number(self, p=None):
        """
        Return the root number of this elliptic curve.

        This is 1 if the order of vanishing of the `L`-function `L(E,s)` at 1
        is even, and -1 if it is odd.

        INPUT:

        - ``p`` -- (optional) if given, return the local root number at ``p``

        EXAMPLES::

            sage: EllipticCurve('11a1').root_number()
            1
            sage: EllipticCurve('37a1').root_number()
            -1
            sage: EllipticCurve('389a1').root_number()
            1
            sage: type(EllipticCurve('389a1').root_number())
            <... 'sage.rings.integer.Integer'>

            sage: E = EllipticCurve('100a1')
            sage: E.root_number(2)
            -1
            sage: E.root_number(5)
            1
            sage: E.root_number(7)
            1

        The root number is cached::

            sage: E.root_number(2) is E.root_number(2)
            True
            sage: E.root_number()
            1
        """
    def has_cm(self) -> bool:
        """
        Return whether or not this curve has a CM `j`-invariant.

        OUTPUT:

        ``True`` if the `j`-invariant of this curve is the
        `j`-invariant of an imaginary quadratic order, otherwise
        ``False``.

        .. SEEALSO::

            :meth:`cm_discriminant()` and :meth:`has_rational_cm`

        .. NOTE::

            Even if `E` has CM in this sense (that its `j`-invariant is
            a CM `j`-invariant), since the associated negative
            discriminant `D` is not a square in `\\QQ`, the extra
            endomorphisms will not be defined over `\\QQ`.  See also the
            method :meth:`has_rational_cm` which tests whether `E` has
            extra endomorphisms defined over `\\QQ` or a given extension
            of `\\QQ`.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.has_cm()
            False
            sage: E = EllipticCurve('32a1')
            sage: E.has_cm()
            True
            sage: E.j_invariant()
            1728
        """
    def cm_discriminant(self):
        """
        Return the associated quadratic discriminant if this elliptic
        curve has Complex Multiplication over the algebraic closure.

        A :exc:`ValueError` is raised if the curve does not have CM (see the
        function :meth:`has_cm()`).

        EXAMPLES::

            sage: E = EllipticCurve('32a1')
            sage: E.cm_discriminant()
            -4
            sage: E = EllipticCurve('121b1')
            sage: E.cm_discriminant()
            -11
            sage: E = EllipticCurve('37a1')
            sage: E.cm_discriminant()
            Traceback (most recent call last):
            ...
            ValueError: Elliptic Curve defined by y^2 + y = x^3 - x
            over Rational Field does not have CM
        """
    def has_rational_cm(self, field=None) -> bool:
        """
        Return whether or not this curve has CM defined over `\\QQ`
        or the given field.

        INPUT:

        - ``field`` -- (default: `\\QQ`) a field, which should be an
          extension of `\\QQ`;

        OUTPUT:

        ``True`` if the ring of endomorphisms of this curve over
        the given field is larger than `\\ZZ`; otherwise ``False``.
        If ``field`` is ``None`` the output will always be ``False``.
        See also :meth:`cm_discriminant()` and :meth:`has_cm`.

        .. NOTE::

            If `E` has CM but the discriminant `D` is not a square in
            the given field `K`, which will certainly be the case for
            `K=\\QQ` since `D<0`, then the extra endomorphisms will not
            be defined over `K`, and this function will return
            ``False``.  See also :meth:`has_cm`.  To obtain the CM
            discriminant, use :meth:`cm_discriminant()`.

        EXAMPLES::

            sage: E = EllipticCurve(j=0)
            sage: E.has_cm()
            True
            sage: E.has_rational_cm()
            False
            sage: D = E.cm_discriminant(); D
            -3

        If we extend scalars to a field in which the discriminant is a
        square, the CM becomes rational::

            sage: E.has_rational_cm(QuadraticField(-3))                                 # needs sage.rings.number_field
            True

            sage: E = EllipticCurve(j=8000)
            sage: E.has_cm()
            True
            sage: E.has_rational_cm()
            False
            sage: D = E.cm_discriminant(); D
            -8

        Again, we may extend scalars to a field in which the
        discriminant is a square, where the CM becomes rational::

            sage: E.has_rational_cm(QuadraticField(-2))                                 # needs sage.rings.number_field
            True

        The field need not be a number field provided that it is an
        extension of `\\QQ`::

            sage: E.has_rational_cm(RR)
            False
            sage: E.has_rational_cm(CC)
            True

        An error is raised if a field is given which is not an
        extension of `\\QQ`, i.e., not of characteristic `0`::

            sage: E.has_rational_cm(GF(2))
            Traceback (most recent call last):
            ...
            ValueError: Error in has_rational_cm: Finite Field of size 2
            is not an extension field of QQ
        """
    def quadratic_twist(self, D):
        """
        Return the global minimal model of the quadratic twist of this
        curve by ``D``.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E7 = E.quadratic_twist(7); E7
            Elliptic Curve defined by y^2 = x^3 - 784*x + 5488 over Rational Field
            sage: E7.conductor()
            29008
            sage: E7.quadratic_twist(7) == E
            True
        """
    def minimal_quadratic_twist(self):
        """
        Determine a quadratic twist with minimal conductor. Return a
        global minimal model of the twist and the fundamental
        discriminant of the quadratic field over which they are
        isomorphic.

        .. NOTE::

            If there is more than one curve with minimal conductor, the
            one returned is the one with smallest label (if in the
            database), or the one with minimal `a`-invariant list
            (otherwise).

        .. NOTE::

            For curves with `j`-invariant 0 or 1728 the curve returned
            is the minimal quadratic twist, not necessarily the minimal
            twist (which would have conductor 27 or 32 respectively).

        EXAMPLES::

            sage: E = EllipticCurve('121d1')
            sage: E.minimal_quadratic_twist()
            (Elliptic Curve defined by y^2 + y = x^3 - x^2 over Rational Field, -11)
            sage: Et, D = EllipticCurve('32a1').minimal_quadratic_twist()
            sage: D
            1

            sage: E = EllipticCurve('11a1')
            sage: Et, D = E.quadratic_twist(-24).minimal_quadratic_twist()
            sage: E == Et
            True
            sage: D
            -24

            sage: E = EllipticCurve([0,0,0,0,1000])
            sage: E.minimal_quadratic_twist()
            (Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field, 40)
            sage: E = EllipticCurve([0,0,0,1600,0])
            sage: E.minimal_quadratic_twist()
            (Elliptic Curve defined by y^2 = x^3 + 4*x over Rational Field, 5)

        If the curve has square-free conductor then it is already
        minimal (see :issue:`14060`)::

            sage: E = next(cremona_optimal_curves([2*3*5*7*11]))
            sage: (E, 1) == E.minimal_quadratic_twist()
            True

        An example where the minimal quadratic twist is not the
        minimal twist (which has conductor 27)::

            sage: E = EllipticCurve([0,0,0,0,7])
            sage: E.j_invariant()
            0
            sage: E.minimal_quadratic_twist()[0].conductor()
            5292
        """
    def isogeny_class(self, algorithm: str = 'sage', order=None):
        '''
        Return the `\\QQ`-isogeny class of this elliptic curve.

        INPUT:

        - ``algorithm`` -- string; one of

          - ``\'database\'`` -- use the Cremona database (only works if
            curve is isomorphic to a curve in the database)

          - ``\'sage\'`` (default) -- use the native Sage implementation

        - ``order`` -- ``None``, string, or list of curves (default:
          ``None``); if not ``None`` then the curves in the class are
          reordered after being computed.  Note that if the order is
          ``None`` then the resulting order will depend on the algorithm.

          - If ``order`` is ``\'database\'`` or ``\'sage\'``, then the reordering
            is so that the order of curves matches the order produced
            by that algorithm.

          - If ``order`` is ``\'lmfdb\'`` then the curves are sorted
            lexicographically by a-invariants, in the LMFDB database.

          - If ``order`` is a list of curves, then the curves in the
            class are reordered to be isomorphic with the specified
            list of curves.

        OUTPUT:

        An instance of the class
        :class:`sage.schemes.elliptic_curves.isogeny_class.IsogenyClass_EC_Rational`.
        This object models a list of minimal models (with containment,
        index, etc based on isomorphism classes).  It also has methods
        for computing the isogeny matrix and the list of isogenies
        between curves in this class.

        .. NOTE::

            The curves in the isogeny class will all be standard
            minimal models.

        EXAMPLES::

            sage: isocls = EllipticCurve(\'37b\').isogeny_class(order=\'lmfdb\')
            sage: isocls
            Elliptic curve isogeny class 37b
            sage: isocls.curves
            (Elliptic Curve defined by y^2 + y = x^3 + x^2 - 1873*x - 31833 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 23*x - 50 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 3*x + 1 over Rational Field)
            sage: isocls.matrix()
            [1 3 9]
            [3 1 3]
            [9 3 1]

        ::

            sage: isocls = EllipticCurve(\'37b\').isogeny_class(\'database\', order=\'lmfdb\'); isocls.curves
            (Elliptic Curve defined by y^2 + y = x^3 + x^2 - 1873*x - 31833 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 23*x - 50 over Rational Field,
             Elliptic Curve defined by y^2 + y = x^3 + x^2 - 3*x + 1 over Rational Field)

        This is an example of a curve with a `37`-isogeny::

            sage: E = EllipticCurve([1,1,1,-8,6])
            sage: isocls = E.isogeny_class(); isocls
            Isogeny class of Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 8*x + 6 over Rational Field
            sage: isocls.matrix()
            [ 1 37]
            [37  1]
            sage: print("\\n".join(repr(E) for E in isocls.curves))
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 8*x + 6 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 208083*x - 36621194 over Rational Field

        This curve had numerous `2`-isogenies::

            sage: e = EllipticCurve([1,0,0,-39,90])
            sage: isocls = e.isogeny_class(); isocls.matrix()
            [1 2 4 4 8 8]
            [2 1 2 2 4 4]
            [4 2 1 4 8 8]
            [4 2 4 1 2 2]
            [8 4 8 2 1 4]
            [8 4 8 2 4 1]

        See http://math.harvard.edu/~elkies/nature.html for more
        interesting examples of isogeny structures.

        ::

            sage: E = EllipticCurve(j = -262537412640768000)
            sage: isocls = E.isogeny_class(); isocls.matrix()
            [  1 163]
            [163   1]
            sage: print("\\n".join(repr(C) for C in isocls.curves))
            Elliptic Curve defined by y^2 + y = x^3 - 2174420*x + 1234136692 over Rational Field
            Elliptic Curve defined by y^2 + y = x^3 - 57772164980*x - 5344733777551611 over Rational Field

        The degrees of isogenies are invariant under twists::

            sage: E = EllipticCurve(j = -262537412640768000)
            sage: E1 = E.quadratic_twist(6584935282)
            sage: isocls = E1.isogeny_class(); isocls.matrix()
            [  1 163]
            [163   1]
            sage: E1.conductor()
            18433092966712063653330496

        ::

            sage: E = EllipticCurve(\'14a1\')
            sage: isocls = E.isogeny_class(); isocls.matrix()
            [ 1  2  3  3  6  6]
            [ 2  1  6  6  3  3]
            [ 3  6  1  9  2 18]
            [ 3  6  9  1 18  2]
            [ 6  3  2 18  1  9]
            [ 6  3 18  2  9  1]
            sage: print("\\n".join(repr(C) for C in isocls.curves))
            Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 36*x - 70 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - x over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 171*x - 874 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 11*x + 12 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 2731*x - 55146 over Rational Field
            sage: isocls2 = isocls.reorder(\'lmfdb\'); isocls2.matrix()
            [ 1  2  3  9 18  6]
            [ 2  1  6 18  9  3]
            [ 3  6  1  3  6  2]
            [ 9 18  3  1  2  6]
            [18  9  6  2  1  3]
            [ 6  3  2  6  3  1]
            sage: print("\\n".join(repr(C) for C in isocls2.curves))
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 2731*x - 55146 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 171*x - 874 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 36*x - 70 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 11*x + 12 over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 - x over Rational Field
            Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6 over Rational Field

        ::

            sage: E = EllipticCurve(\'11a1\')
            sage: isocls = E.isogeny_class(); isocls.matrix()
            [ 1  5  5]
            [ 5  1 25]
            [ 5 25  1]
            sage: f = isocls.isogenies()[0][1]; f.kernel_polynomial()
            x^2 + x - 29/5
        '''
    def isogenies_prime_degree(self, l=None):
        """
        Return a list of `\\ell`-isogenies from self, where `\\ell` is a
        prime.

        INPUT:

        - ``l`` -- either ``None`` or a prime or a list of primes

        OUTPUT:

        (list) `\\ell`-isogenies for the given `\\ell` or if `\\ell` is None, all
        `\\ell`-isogenies.

        .. NOTE::

            The codomains of the isogenies returned are standard
            minimal models.  This is because the functions
            :meth:`isogenies_prime_degree_genus_0()` and
            :meth:`isogenies_sporadic_Q()` are implemented that way for
            curves defined over `\\QQ`.

        EXAMPLES::

            sage: E = EllipticCurve([45,32])
            sage: E.isogenies_prime_degree()
            []
            sage: E = EllipticCurve(j = -262537412640768000)
            sage: E.isogenies_prime_degree()
            [Isogeny of degree 163
              from Elliptic Curve defined by y^2 + y = x^3 - 2174420*x + 1234136692 over Rational Field
                to Elliptic Curve defined by y^2 + y = x^3 - 57772164980*x - 5344733777551611 over Rational Field]
            sage: E1 = E.quadratic_twist(6584935282)
            sage: E1.isogenies_prime_degree()
            [Isogeny of degree 163
              from Elliptic Curve defined by y^2 = x^3 - 94285835957031797981376080*x + 352385311612420041387338054224547830898 over Rational Field
                to Elliptic Curve defined by y^2 = x^3 - 2505080375542377840567181069520*x - 1526091631109553256978090116318797845018020806 over Rational Field]

            sage: E = EllipticCurve('14a1')
            sage: E.isogenies_prime_degree(2)
            [Isogeny of degree 2
              from Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6 over Rational Field
                to Elliptic Curve defined by y^2 + x*y + y = x^3 - 36*x - 70 over Rational Field]
            sage: E.isogenies_prime_degree(3)
            [Isogeny of degree 3
              from Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6 over Rational Field
                to Elliptic Curve defined by y^2 + x*y + y = x^3 - x over Rational Field,
             Isogeny of degree 3
              from Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6 over Rational Field
                to Elliptic Curve defined by y^2 + x*y + y = x^3 - 171*x - 874 over Rational Field]
            sage: E.isogenies_prime_degree(5)
            []
            sage: E.isogenies_prime_degree(11)
            []
            sage: E.isogenies_prime_degree(29)
            []
            sage: E.isogenies_prime_degree(4)
            Traceback (most recent call last):
            ...
            ValueError: 4 is not prime.
        """
    def is_isogenous(self, other, proof: bool = True, maxp: int = 200):
        """
        Return whether or not ``self`` is isogenous to other.

        INPUT:

        - ``other`` -- another elliptic curve

        - ``proof`` -- boolean (default: ``True``); if ``False``, the function
          will return ``True`` whenever the two curves have the same
          conductor and are isogenous modulo `p` for `p` up to ``maxp``;
          otherwise this test is followed by a rigorous test (which
          may be more time-consuming)

        - ``maxp`` -- (default: 200) the maximum prime `p` for
          which isogeny modulo `p` will be checked

        OUTPUT:

        boolean; ``True`` if there is an isogeny from curve ``self`` to
        curve ``other``.

        ALGORITHM:

        First the conductors are compared as well as the Traces of
        Frobenius for good primes up to ``maxp``.  If any of these
        tests fail, ``False`` is returned.  If they all pass and
        ``proof`` is ``False`` then ``True`` is returned, otherwise a
        complete set of curves isogenous to ``self`` is computed and
        ``other`` is checked for isomorphism with any of these,

        EXAMPLES::

            sage: E1 = EllipticCurve('14a1')
            sage: E6 = EllipticCurve('14a6')
            sage: E1.is_isogenous(E6)
            True
            sage: E1.is_isogenous(EllipticCurve('11a1'))
            False

        ::

            sage: EllipticCurve('37a1').is_isogenous(EllipticCurve('37b1'))
            False

        ::

            sage: E = EllipticCurve([2, 16])
            sage: EE = EllipticCurve([87, 45])
            sage: E.is_isogenous(EE)
            False
        """
    def isogeny_degree(self, other):
        """
        Return the minimal degree of an isogeny between ``self`` and
        ``other``.

        INPUT:

        - ``other`` -- another elliptic curve

        OUTPUT:

        The minimal degree of an isogeny from ``self`` to
        ``other``, or `0` if the curves are not isogenous.

        EXAMPLES::

            sage: E = EllipticCurve([-1056, 13552])
            sage: E2 = EllipticCurve([-127776, -18037712])
            sage: E.isogeny_degree(E2)
            11

        ::

            sage: E1 = EllipticCurve('14a1')
            sage: E2 = EllipticCurve('14a2')
            sage: E3 = EllipticCurve('14a3')
            sage: E4 = EllipticCurve('14a4')
            sage: E5 = EllipticCurve('14a5')
            sage: E6 = EllipticCurve('14a6')
            sage: E3.isogeny_degree(E1)
            3
            sage: E3.isogeny_degree(E2)
            6
            sage: E3.isogeny_degree(E3)
            1
            sage: E3.isogeny_degree(E4)
            9
            sage: E3.isogeny_degree(E5)
            2
            sage: E3.isogeny_degree(E6)
            18

        ::

            sage: E1 = EllipticCurve('30a1')
            sage: E2 = EllipticCurve('30a2')
            sage: E3 = EllipticCurve('30a3')
            sage: E4 = EllipticCurve('30a4')
            sage: E5 = EllipticCurve('30a5')
            sage: E6 = EllipticCurve('30a6')
            sage: E7 = EllipticCurve('30a7')
            sage: E8 = EllipticCurve('30a8')
            sage: E1.isogeny_degree(E1)
            1
            sage: E1.isogeny_degree(E2)
            2
            sage: E1.isogeny_degree(E3)
            3
            sage: E1.isogeny_degree(E4)
            4
            sage: E1.isogeny_degree(E5)
            4
            sage: E1.isogeny_degree(E6)
            6
            sage: E1.isogeny_degree(E7)
            12
            sage: E1.isogeny_degree(E8)
            12

        ::

            sage: E1 = EllipticCurve('15a1')
            sage: E2 = EllipticCurve('15a2')
            sage: E3 = EllipticCurve('15a3')
            sage: E4 = EllipticCurve('15a4')
            sage: E5 = EllipticCurve('15a5')
            sage: E6 = EllipticCurve('15a6')
            sage: E7 = EllipticCurve('15a7')
            sage: E8 = EllipticCurve('15a8')
            sage: E1.isogeny_degree(E1)
            1
            sage: E7.isogeny_degree(E2)
            8
            sage: E7.isogeny_degree(E3)
            2
            sage: E7.isogeny_degree(E4)
            8
            sage: E7.isogeny_degree(E5)
            16
            sage: E7.isogeny_degree(E6)
            16
            sage: E7.isogeny_degree(E8)
            4

        0 is returned when the curves are not isogenous::

            sage: A = EllipticCurve('37a1')
            sage: B = EllipticCurve('37b1')
            sage: A.isogeny_degree(B)
            0
            sage: A.is_isogenous(B)
            False
        """
    def optimal_curve(self):
        """
        Given an elliptic curve that is in the installed Cremona
        database, return the optimal curve isogenous to it.

        EXAMPLES:

        The following curve is not optimal::

            sage: E = EllipticCurve('11a2'); E
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580 over Rational Field
            sage: E.optimal_curve()
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: E.optimal_curve().cremona_label()
            '11a1'

        Note that 990h is the special case where the optimal curve
        isn't the first in the Cremona labeling::

            sage: E = EllipticCurve('990h4'); E
            Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 + 6112*x - 41533 over Rational Field
            sage: F = E.optimal_curve(); F
            Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 1568*x - 4669 over Rational Field
            sage: F.cremona_label()
            '990h3'
            sage: EllipticCurve('990a1').optimal_curve().cremona_label()   # a isn't h.
            '990a1'

        If the input curve is optimal, this function returns that
        curve (not just a copy of it or a curve isomorphic to it!)::

            sage: E = EllipticCurve('37a1')
            sage: E.optimal_curve() is E
            True

        Also, if this curve is optimal but not given by a minimal
        model, this curve will still be returned, so this function
        need not return a minimal model in general.

        ::

            sage: F = E.short_weierstrass_model(); F
            Elliptic Curve defined by y^2  = x^3 - 16*x + 16 over Rational Field
            sage: F.optimal_curve()
            Elliptic Curve defined by y^2  = x^3 - 16*x + 16 over Rational Field
        """
    def isogeny_graph(self, order=None):
        '''
        Return a graph representing the isogeny class of this elliptic
        curve, where the vertices are isogenous curves over
        `\\QQ` and the edges are prime degree isogenies.

        .. NOTE::

            The vertices are labeled `1` to `n` rather than `0` to `n-1`
            to correspond to LMFDB and Cremona labels.

        EXAMPLES::

            sage: LL = []
            sage: for e in cremona_optimal_curves(range(1, 38)):  # long time
            ....:  G = e.isogeny_graph()
            ....:  already = False
            ....:  for H in LL:
            ....:      if G.is_isomorphic(H):
            ....:          already = True
            ....:          break
            ....:  if not already:
            ....:      LL.append(G)
            sage: graphs_list.show_graphs(LL)  # long time

        ::

            sage: E = EllipticCurve(\'195a\')
            sage: G = E.isogeny_graph()
            sage: for v in G: print("{} {}".format(v, G.get_vertex(v)))
            1 Elliptic Curve defined by y^2 + x*y  = x^3 - 110*x + 435 over Rational Field
            2 Elliptic Curve defined by y^2 + x*y  = x^3 - 115*x + 392 over Rational Field
            3 Elliptic Curve defined by y^2 + x*y  = x^3 + 210*x + 2277 over Rational Field
            4 Elliptic Curve defined by y^2 + x*y  = x^3 - 520*x - 4225 over Rational Field
            5 Elliptic Curve defined by y^2 + x*y  = x^3 + 605*x - 19750 over Rational Field
            6 Elliptic Curve defined by y^2 + x*y  = x^3 - 8125*x - 282568 over Rational Field
            7 Elliptic Curve defined by y^2 + x*y  = x^3 - 7930*x - 296725 over Rational Field
            8 Elliptic Curve defined by y^2 + x*y  = x^3 - 130000*x - 18051943 over Rational Field
            sage: G.plot(edge_labels=True)                                              # needs sage.plot
            Graphics object consisting of 23 graphics primitives
        '''
    def manin_constant(self):
        """
        Return the Manin constant of this elliptic curve.

        If `\\phi: X_0(N) \\to E` is the modular
        parametrization of minimal degree, then the Manin constant `c`
        is defined to be the rational number `c` such that
        `\\phi^*(\\omega_E) = c\\cdot \\omega_f` where `\\omega_E` is a Néron
        differential and `\\omega_f = f(q) dq/q` is the differential on `X_0(N)`
        corresponding to the newform `f` attached to the isogeny class of `E`.

        It is known that the Manin constant is an integer. It is conjectured
        that in each class there is at least one, more precisely the so-called
        strong Weil curve or `X_0(N)`-optimal curve, that has Manin constant `1`.

        OUTPUT: integer

        This function only works if the curve is in the installed
        Cremona database.  Sage includes by default a small database;
        for the full database you have to install an optional package.

        EXAMPLES::

            sage: EllipticCurve('11a1').manin_constant()
            1
            sage: EllipticCurve('11a2').manin_constant()
            1
            sage: EllipticCurve('11a3').manin_constant()
            5

        Check that it works even if the curve is non-minimal::

            sage: EllipticCurve('11a3').change_weierstrass_model([1/35,0,0,0]).manin_constant()
            5

        Rather complicated examples (see :issue:`12080`) ::

            sage: [ EllipticCurve('27a%s'%i).manin_constant() for i in [1,2,3,4]]
            [1, 1, 3, 3]
            sage: [ EllipticCurve('80b%s'%i).manin_constant() for i in [1,2,3,4]]
            [1, 2, 1, 2]
        """
    def galois_representation(self):
        """
        The compatible family of the Galois representation
        attached to this elliptic curve.

        Given an elliptic curve `E` over `\\QQ`
        and a rational prime number `p`, the `p^n`-torsion
        `E[p^n]` points of `E` is a representation of the
        absolute Galois group of `\\QQ`. As `n` varies
        we obtain the Tate module `T_p E` which is a
        a representation of `G_K` on a free `\\ZZ_p`-module
        of rank `2`. As `p` varies the representations
        are compatible.

        EXAMPLES::

            sage: rho = EllipticCurve('11a1').galois_representation()
            sage: rho
            Compatible family of Galois representations associated to the
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: rho.is_irreducible(7)
            True
            sage: rho.is_irreducible(5)
            False
            sage: rho.is_surjective(11)
            True
            sage: rho.non_surjective()
            [5]
            sage: rho = EllipticCurve('37a1').galois_representation()
            sage: rho.non_surjective()
            []
            sage: rho = EllipticCurve('27a1').galois_representation()
            sage: rho.is_irreducible(7)
            True
            sage: rho.non_surjective()   # cm-curve
            [0]
        """
    def is_semistable(self):
        """
        Return ``True`` iff this elliptic curve is semi-stable at all primes.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.is_semistable()
            True
            sage: E = EllipticCurve('90a1')
            sage: E.is_semistable()
            False
        """
    def is_ordinary(self, p, ell=None):
        """
        Return ``True`` precisely when the mod-``p`` representation attached
        to this elliptic curve is ordinary at ``ell``.

        INPUT:

        - ``p`` -- a prime
        - ``ell`` -- a prime (default: ``p``)

        OUTPUT: boolean

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.is_ordinary(37)
            True
            sage: E = EllipticCurve('32a1')
            sage: E.is_ordinary(2)
            False
            sage: [p for p in prime_range(50) if E.is_ordinary(p)]
            [5, 13, 17, 29, 37, 41]
        """
    def is_good(self, p, check: bool = True):
        """
        Return ``True`` if ``p`` is a prime of good reduction for `E`.

        INPUT:

        - ``p`` -- a prime

        OUTPUT: boolean

        EXAMPLES::

            sage: e = EllipticCurve('11a')
            sage: e.is_good(-8)
            Traceback (most recent call last):
            ...
            ValueError: p must be prime
            sage: e.is_good(-8, check=False)
            True
        """
    def is_supersingular(self, p, ell=None):
        """
        Return ``True`` precisely when `p` is a prime of good reduction and the
        mod-`p` representation attached to this elliptic curve is
        supersingular at ell.

        INPUT:

        - ``p`` -- a prime
        - ``ell`` -- a prime (default: ``p``)

        OUTPUT: boolean

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.is_supersingular(37)
            False
            sage: E = EllipticCurve('32a1')
            sage: E.is_supersingular(2)
            False
            sage: E.is_supersingular(7)
            True
            sage: [p for p in prime_range(50) if E.is_supersingular(p)]
            [3, 7, 11, 19, 23, 31, 43, 47]
        """
    def supersingular_primes(self, B):
        """
        Return a list of all supersingular primes for this elliptic curve
        up to and possibly including B.

        EXAMPLES::

            sage: e = EllipticCurve('11a')
            sage: e.aplist(20)
            [-2, -1, 1, -2, 1, 4, -2, 0]
            sage: e.supersingular_primes(1000)
            [2, 19, 29, 199, 569, 809]

        ::

            sage: e = EllipticCurve('27a')
            sage: e.aplist(20)
            [0, 0, 0, -1, 0, 5, 0, -7]
            sage: e.supersingular_primes(97)
            [2, 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89]
            sage: e.ordinary_primes(97)
            [7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97]
            sage: e.supersingular_primes(3)
            [2]
            sage: e.supersingular_primes(2)
            [2]
            sage: e.supersingular_primes(1)
            []
        """
    def ordinary_primes(self, B):
        """
        Return a list of all ordinary primes for this elliptic curve up to
        and possibly including B.

        EXAMPLES::

            sage: e = EllipticCurve('11a')
            sage: e.aplist(20)
            [-2, -1, 1, -2, 1, 4, -2, 0]
            sage: e.ordinary_primes(97)
            [3, 5, 7, 11, 13, 17, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            sage: e = EllipticCurve('49a')
            sage: e.aplist(20)
            [1, 0, 0, 0, 4, 0, 0, 0]
            sage: e.supersingular_primes(97)
            [3, 5, 13, 17, 19, 31, 41, 47, 59, 61, 73, 83, 89, 97]
            sage: e.ordinary_primes(97)
            [2, 11, 23, 29, 37, 43, 53, 67, 71, 79]
            sage: e.ordinary_primes(3)
            [2]
            sage: e.ordinary_primes(2)
            [2]
            sage: e.ordinary_primes(1)
            []
        """
    def eval_modular_form(self, points, order):
        """
        Evaluate the modular form of this elliptic curve at points in `\\CC`.

        INPUT:

        - ``points`` -- list of points in the upper half-plane

        - ``order`` -- nonnegative integer

        The ``order`` parameter is the number of terms used in the summation.

        OUTPUT: list of values for `s` in ``points``

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: E.eval_modular_form([1.5+I,2.0+I,2.5+I],100)
            [-0.0018743978548152085...,
             0.0018604485340371083...,
            -0.0018743978548152085...]

            sage: E.eval_modular_form(2.1+I, 100) # abs tol 1e-16
            [0.00150864362757267079 + 0.00109100341113449845*I]

        TESTS::

            sage: E.eval_modular_form(CDF(2.1+I), 100) # abs tol 1e-16
            [0.00150864362757267079 + 0.00109100341113449845*I]
        """
    def sha(self):
        """
        Return an object of class
        'sage.schemes.elliptic_curves.sha_tate.Sha' attached to this
        elliptic curve.

        This can be used in functions related to bounding the order of Sha
        (The Tate-Shafarevich group of the curve).

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: S = E.sha()
            sage: S
            Tate-Shafarevich group for the Elliptic Curve
             defined by y^2 + y = x^3 - x over Rational Field
            sage: S.bound_kolyvagin()
            ([2], 1)
        """
    heegner_point = heegner.ell_heegner_point
    kolyvagin_point = heegner.kolyvagin_point
    heegner_discriminants = heegner.ell_heegner_discriminants
    heegner_discriminants_list = heegner.ell_heegner_discriminants_list
    satisfies_heegner_hypothesis = heegner.satisfies_heegner_hypothesis
    heegner_point_height = heegner.heegner_point_height
    heegner_index = heegner.heegner_index
    heegner_index_bound = heegner.heegner_index_bound
    heegner_sha_an = heegner.heegner_sha_an
    padic_regulator: Incomplete
    padic_height_pairing_matrix: Incomplete
    padic_height: Incomplete
    padic_height_via_multiply: Incomplete
    padic_sigma: Incomplete
    padic_sigma_truncated: Incomplete
    padic_E2: Incomplete
    matrix_of_frobenius: Incomplete
    def mod5family(self):
        """
        Return the family of all elliptic curves with the same mod-5
        representation as ``self``.

        EXAMPLES::

            sage: E = EllipticCurve('32a1')
            sage: E.mod5family()
            Elliptic Curve defined by y^2 = x^3 + 4*x
             over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def tate_curve(self, p):
        """
        Create the Tate curve over the `p`-adics associated to
        this elliptic curve.

        This Tate curve is a `p`-adic curve with split multiplicative
        reduction of the form `y^2+xy=x^3+s_4 x+s_6` which is
        isomorphic to the given curve over the algebraic closure of
        `\\QQ_p`. Its points over `\\QQ_p`
        are isomorphic to `\\QQ_p^{\\times}/q^{\\ZZ}`
        for a certain parameter `q \\in \\ZZ_p`.

        INPUT:

        - ``p`` -- a prime where the curve has split multiplicative reduction

        EXAMPLES::

            sage: e = EllipticCurve('130a1')
            sage: e.tate_curve(2)
            2-adic Tate curve associated to the Elliptic Curve
             defined by y^2 + x*y + y = x^3 - 33*x + 68 over Rational Field

        The input curve must have multiplicative reduction at the prime.

        ::

            sage: e.tate_curve(3)
            Traceback (most recent call last):
            ...
            ValueError: the elliptic curve must have multiplicative reduction at 3

        We compute with `p=5`::

            sage: T = e.tate_curve(5); T
            5-adic Tate curve associated to the Elliptic Curve
             defined by y^2 + x*y + y = x^3 - 33*x + 68 over Rational Field

        We find the Tate parameter `q`::

            sage: T.parameter(prec=5)
            3*5^3 + 3*5^4 + 2*5^5 + 2*5^6 + 3*5^7 + O(5^8)

        We compute the `\\mathcal{L}`-invariant of the curve::

            sage: T.L_invariant(prec=10)
            5^3 + 4*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 3*5^8 + 5^9 + O(5^10)
        """
    def height(self, precision=None):
        """
        Return the real height of this elliptic curve.

        This is used in :meth:`integral_points()`.

        INPUT:

        - ``precision`` -- desired real precision of the result
          (default real precision if ``None``)

        EXAMPLES::

            sage: E = EllipticCurve('5077a1')
            sage: E.height()
            17.4513334798896
            sage: E.height(100)
            17.451333479889612702508579399
            sage: E = EllipticCurve([0,0,0,0,1])
            sage: E.height()
            1.38629436111989
            sage: E = EllipticCurve([0,0,0,1,0])
            sage: E.height()
            7.45471994936400
        """
    def faltings_height(self, stable: bool = False, prec=None):
        """
        Return the Faltings height (stable or unstable) of this elliptic curve.

        INPUT:

        - ``stable`` -- boolean (default: ``False``); if ``True``, return the
          *stable* Faltings height, otherwise the unstable height

        - ``prec`` -- integer (default: ``None``); bit precision of output; if
          ``None``, use standard precision (53 bits)

        OUTPUT: real; the Faltings height of this elliptic curve

        .. NOTE::

            Different authors normalise the Faltings height
            differently.  We use the formula `-\\frac{1}{2}\\log(A)`,
            where `A` is the area of the fundamental period
            parallelogram; some authors use `-\\frac{1}{2\\pi}\\log(A)`
            instead.

            The unstable Faltings height does depend on the model.  The
            *stable* Faltings height is defined to be

            .. MATH::

                \\frac{1}{12}\\log\\mathrm{denom}(j) - \\frac{1}{12}\\log|\\Delta| -\\frac{1}{2}\\log A,

            This is independent of the model.  For the minimal model of
            a semistable elliptic curve, we have
            `\\mathrm{denom}(j)=|\\Delta|`, and the stable and unstable
            heights agree.

        EXAMPLES::

            sage: E = EllipticCurve('32a1')
            sage: E.faltings_height()
            -0.617385745351564
            sage: E.faltings_height(stable=True)
            -1.31053292591151

        These differ since the curve is not semistable::

            sage: E.is_semistable()
            False

        If the model is changed, the Faltings height changes but the
        stable height does not.  It is reduced by `\\log(u)` where `u`
        is the scale factor::

            sage: E1 = E.change_weierstrass_model([10,0,0,0])
            sage: E1.faltings_height()
            -2.91997083834561
            sage: E1.faltings_height(stable=True)
            -1.31053292591151
            sage: E.faltings_height() - log(10.0)
            -2.91997083834561

        For a semistable curve (that is, one with squarefree
        conductor), the stable and unstable heights are equal.  Here
        we also show that one can specify the (bit) precision of the
        result::

            sage: E = EllipticCurve('210a1')
            sage: E.is_semistable()
            True
            sage: E.faltings_height(prec=100)
            -0.043427311858075396288912139225
            sage: E.faltings_height(stable=True, prec=100)
            -0.043427311858075396288912139225
        """
    def antilogarithm(self, z, max_denominator=None):
        """
        Return the rational point (if any) associated to this complex
        number; the inverse of the elliptic logarithm function.

        INPUT:

        - ``z`` -- a complex number representing an element of
          `\\CC/L` where `L` is the period lattice of the elliptic curve

        - ``max_denominator`` -- integer (optional); parameter controlling
          the attempted conversion of real numbers to rationals.  If
          not given, ``simplest_rational()`` will be used; otherwise,
          ``nearby_rational()`` will be used with this value of
          ``max_denominator``.

        OUTPUT:

        A point on the curve: the rational point which is the image of `z`
        under the Weierstrass parametrization, if it exists and can be
        determined from `z` and the given value of max_denominator (if any);
        otherwise a :exc:`ValueError` exception is raised.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: P = E(-1,1)
            sage: z = P.elliptic_logarithm()
            sage: E.antilogarithm(z)
            (-1 : 1 : 1)
            sage: Q = E(0,-1)
            sage: z = Q.elliptic_logarithm()
            sage: E.antilogarithm(z)
            Traceback (most recent call last):
            ...
            ValueError: approximated point not on the curve
            sage: E.antilogarithm(z, max_denominator=10)
            (0 : -1 : 1)

            sage: E = EllipticCurve('11a1')
            sage: w1,w2 = E.period_lattice().basis()
            sage: [E.antilogarithm(a*w1/5,1) for a in range(5)]
            [(0 : 1 : 0), (16 : -61 : 1), (5 : -6 : 1), (5 : 5 : 1), (16 : 60 : 1)]
        """
    def integral_x_coords_in_interval(self, xmin, xmax):
        '''
        Return the set of integers `x` with `xmin\\le x\\le xmax` which are
        `x`-coordinates of rational points on this curve.

        INPUT:

        - ``xmin``, ``xmax`` -- two integers

        OUTPUT:

        The set of integers `x` with `xmin\\le x\\le xmax` which are
        `x`-coordinates of rational points on the elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1, -7, 6])
            sage: xset = E.integral_x_coords_in_interval(-100,100)
            sage: sorted(xset)
            [-3, -2, -1, 0, 1, 2, 3, 4, 8, 11, 14, 21, 37, 52, 93]
            sage: xset = E.integral_x_coords_in_interval(-100, 0)
            sage: sorted(xset)
            [-3, -2, -1, 0]

        TESTS:

        The bug reported on :issue:`22719` is now fixed::

            sage: E = EllipticCurve("141d1")
            sage: E.integral_points()
            [(0 : -1 : 1), (2 : -2 : 1)]
        '''
    prove_BSD: Incomplete
    def integral_points(self, mw_base: str = 'auto', both_signs: bool = False, verbose: bool = False):
        """
        Compute all integral points (up to sign) on this elliptic curve.

        INPUT:

        - ``mw_base`` -- (default: ``'auto'`` - calls :meth:`.gens`) list
          of EllipticCurvePoint generating the Mordell-Weil group of `E`

        - ``both_signs`` -- boolean (default: ``False``); if
          ``True`` the output contains both `P` and `-P`, otherwise
          only one of each pair

        - ``verbose`` -- boolean (default: ``False``); if ``True``,
          some details of the computation are output

        OUTPUT: a sorted list of all the integral points on `E` (up to sign
        unless ``both_signs`` is ``True``)

        .. NOTE::

            The complexity increases exponentially in the rank of curve
            `E`. The computation time (but not the output!) depends on
            the Mordell-Weil basis. If ``mw_base`` is given but is not a
            basis for the Mordell-Weil group (modulo torsion), integral
            points which are not in the subgroup generated by the given
            points will almost certainly not be listed.

        EXAMPLES: A curve of rank 3 with no torsion points::

            sage: E = EllipticCurve([0,0,1,-7,6])
            sage: P1 = E.point((2,0)); P2 = E.point((-1,3)); P3 = E.point((4,6))
            sage: a = E.integral_points([P1,P2,P3]); a
            [(-3 : -1 : 1), (-2 : -4 : 1), (-1 : -4 : 1), (0 : -3 : 1),
             (1 : -1 : 1), (2 : -1 : 1), (3 : -4 : 1), (4 : -7 : 1),
             (8 : -22 : 1), (11 : -36 : 1), (14 : -52 : 1), (21 : -96 : 1),
             (37 : -225 : 1), (52 : -375 : 1), (93 : -897 : 1),
             (342 : -6325 : 1), (406 : -8181 : 1), (816 : -23310 : 1)]

        ::

            sage: a = E.integral_points([P1,P2,P3], verbose=True)
            Using mw_basis  [(2 : 0 : 1), (3 : -4 : 1), (8 : -22 : 1)]
            e1,e2,e3:  -3.0124303725933... 1.0658205476962... 1.94660982489710
            Minimal and maximal eigenvalues of height pairing matrix: 0.637920814585005,2.31982967525725
            x-coords of points on compact component with  -3 <=x<= 1
            [-3, -2, -1, 0, 1]
            x-coords of points on non-compact component with  2 <=x<= 6
            [2, 3, 4]
            starting search of remaining points using coefficient bound 5 and |x| bound 1.53897183921009e25
            x-coords of extra integral points:
            [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
            Total number of integral points: 18

        It is not necessary to specify ``mw_base``; if it is not provided,
        then the Mordell-Weil basis must be computed, which may take
        much longer.

        ::

            sage: E = EllipticCurve([0,0,1,-7,6])
            sage: a = E.integral_points(both_signs=True); a
            [(-3 : -1 : 1), (-3 : 0 : 1), (-2 : -4 : 1), (-2 : 3 : 1), (-1 : -4 : 1),
             (-1 : 3 : 1), (0 : -3 : 1), (0 : 2 : 1), (1 : -1 : 1), (1 : 0 : 1),
             (2 : -1 : 1), (2 : 0 : 1), (3 : -4 : 1), (3 : 3 : 1), (4 : -7 : 1),
             (4 : 6 : 1), (8 : -22 : 1), (8 : 21 : 1), (11 : -36 : 1), (11 : 35 : 1),
             (14 : -52 : 1), (14 : 51 : 1), (21 : -96 : 1), (21 : 95 : 1),
             (37 : -225 : 1), (37 : 224 : 1), (52 : -375 : 1), (52 : 374 : 1),
             (93 : -897 : 1), (93 : 896 : 1), (342 : -6325 : 1), (342 : 6324 : 1),
             (406 : -8181 : 1), (406 : 8180 : 1), (816 : -23310 : 1), (816 : 23309 : 1)]

        An example with negative discriminant::

            sage: EllipticCurve('900d1').integral_points()
            [(-11 : -27 : 1), (-4 : -34 : 1), (4 : -18 : 1), (16 : -54 : 1)]

        Another example with rank 5 and no torsion points::

            sage: E = EllipticCurve([-879984,319138704])
            sage: P1 = E.point((540,1188)); P2 = E.point((576,1836))
            sage: P3 = E.point((468,3132)); P4 = E.point((612,3132))
            sage: P5 = E.point((432,4428))
            sage: a = E.integral_points([P1,P2,P3,P4,P5]); len(a)  # long time (18s on sage.math, 2011)
            54

        TESTS:

        The bug reported on :issue:`4525` is now fixed::

            sage: EllipticCurve('91b1').integral_points()
            [(-1 : -4 : 1), (1 : -1 : 1), (3 : -5 : 1)]

        ::

            sage: [len(e.integral_points(both_signs=False)) for e in cremona_curves([11..100])]  # long time (15s on sage.math, 2011)
            [2, 0, 2, 3, 2, 1, 3, 0, 2, 4, 2, 4, 3, 0, 0, 1, 2, 1, 2, 0, 2, 1, 0, 1, 3, 3, 1, 1, 4, 2, 3, 2, 0, 0, 5, 3, 2, 2, 1, 1, 1, 0, 1, 3, 0, 1, 0, 1, 1, 3, 6, 1, 2, 2, 2, 0, 0, 2, 3, 1, 2, 2, 1, 1, 0, 3, 2, 1, 0, 1, 0, 1, 3, 3, 1, 1, 5, 1, 0, 1, 1, 0, 1, 2, 0, 2, 0, 1, 1, 3, 1, 2, 2, 4, 4, 2, 1, 0, 0, 5, 1, 0, 1, 2, 0, 2, 2, 0, 0, 0, 1, 0, 3, 1, 5, 1, 2, 4, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2, 0, 0, 1, 0, 1, 1, 4, 1, 0, 1, 1, 0, 4, 2, 0, 1, 1, 2, 3, 1, 1, 1, 1, 6, 2, 1, 1, 0, 2, 0, 6, 2, 0, 4, 2, 2, 0, 0, 1, 2, 0, 2, 1, 0, 3, 1, 2, 1, 4, 6, 3, 2, 1, 0, 2, 2, 0, 0, 5, 4, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 3, 1, 3, 1, 1, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 0, 4, 1, 0, 1, 1, 0, 1, 2, 0, 1, 4, 3, 1, 2, 2, 1, 1, 1, 1, 6, 3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 7, 3, 0, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 2, 6, 0, 0, 6, 2, 2, 3, 3, 5, 5, 1, 0, 6, 1, 0, 3, 1, 1, 2, 3, 1, 2, 1, 1, 0, 1, 0, 1, 0, 5, 5, 2, 2, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]

        The bug reported at :issue:`4897` is now fixed::

            sage: [P[0] for P in EllipticCurve([0,0,0,-468,2592]).integral_points()]
            [-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 168, 186, 381, 1476, 2034, 67246]

        See :issue:`22063`::

            sage: for n in [67,71,74,91]:  # long time
            ....:     assert 4*n^6 + 4*n^2 in [P[0] for P in EllipticCurve([0,0,0,2,n^2]).integral_points()]

        ALGORITHM:

        This function uses the algorithm given in [Coh2007I]_.

        AUTHORS:

        - Michael Mardaus (2008-07)

        - Tobias Nagel (2008-07)

        - John Cremona (2008-07)
        """
    def S_integral_points(self, S, mw_base: str = 'auto', both_signs: bool = False, verbose: bool = False, proof=None):
        '''
        Compute all S-integral points (up to sign) on this elliptic curve.

        INPUT:

        - ``S`` -- list of primes

        - ``mw_base`` -- (default: ``\'auto\'`` - calls :meth:`.gens`) list of
          EllipticCurvePoint generating the Mordell-Weil group of `E`

        - ``both_signs`` -- boolean (default: ``False``); if ``True`` the
          output contains both `P` and `-P`, otherwise only one of each
          pair

        - ``verbose`` -- boolean (default: ``False``); if ``True``, some
          details of the computation are output

        - ``proof`` -- boolean (default: ``True``); if ``True`` ALL
          S-integral points will be returned.  If ``False``, the MW basis
          will be computed with the ``proof=False`` flag, and also the
          time-consuming final call to
          S_integral_x_coords_with_abs_bounded_by(abs_bound) is
          omitted.  Use this only if the computation takes too long,
          but be warned that then it cannot be guaranteed that all
          S-integral points will be found.

        OUTPUT:

        A sorted list of all the S-integral points on E (up to sign
        unless ``both_signs`` is ``True``).

        .. NOTE::

            The complexity increases exponentially in the rank of curve
            E and in the length of S.  The computation time (but not
            the output!) depends on the Mordell-Weil basis.  If mw_base
            is given but is not a basis for the Mordell-Weil group
            (modulo torsion), S-integral points which are not in the
            subgroup generated by the given points will almost
            certainly not be listed.

        EXAMPLES:

        A curve of rank 3 with no torsion points::

            sage: E = EllipticCurve([0,0,1,-7,6])
            sage: P1 = E.point((2,0))
            sage: P2 = E.point((-1,3))
            sage: P3 = E.point((4,6))
            sage: a = E.S_integral_points(S=[2,3], mw_base=[P1,P2,P3], verbose=True); a
            max_S: 3 len_S: 3 len_tors: 1
            lambda 0.485997517468...
            k1,k2,k3,k4 7.65200453902598e234 1.31952866480763 3.54035317966420e9 2.42767548272846e17
            p= 2 : trying with p_prec =  30
            mw_base_p_log_val =  [2, 2, 1]
            min_psi =  2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^11 + 2^12 + 2^13 + 2^16 + 2^17 + 2^19 + 2^20 + 2^21 + 2^23 + 2^24 + 2^28 + O(2^30)
            p= 3 : trying with p_prec =  30
            mw_base_p_log_val =  [1, 2, 1]
            min_psi =  3 + 3^2 + 2*3^3 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^11 + 2*3^12 + 2*3^13 + 3^15 + 2*3^16 + 3^18 + 2*3^19 + 2*3^22 + 2*3^23 + 2*3^24 + 2*3^27 + 3^28 + 3^29 + O(3^30)
            mw_base [(1 : -1 : 1), (2 : 0 : 1), (0 : -3 : 1)]
            mw_base_log [0.667789378224099, 0.552642660712417, 0.818477222895703]
            mp [5, 7]
            mw_base_p_log [[2^2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^14 + 2^15 + 2^18 + 2^19 + 2^24 + 2^29 + O(2^30), 2^2 + 2^3 + 2^5 + 2^6 + 2^9 + 2^11 + 2^12 + 2^14 + 2^15 + 2^16 + 2^18 + 2^20 + 2^22 + 2^23 + 2^26 + 2^27 + 2^29 + O(2^30), 2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^11 + 2^12 + 2^13 + 2^16 + 2^17 + 2^19 + 2^20 + 2^21 + 2^23 + 2^24 + 2^28 + O(2^30)], [2*3^2 + 2*3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 3^12 + 2*3^14 + 3^15 + 3^17 + 2*3^19 + 2*3^23 + 3^25 + 3^28 + O(3^30), 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 2*3^7 + 2*3^8 + 3^10 + 2*3^12 + 3^13 + 2*3^14 + 3^15 + 3^18 + 3^22 + 3^25 + 2*3^26 + 3^27 + 3^28 + O(3^30), 3 + 3^2 + 2*3^3 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^11 + 2*3^12 + 2*3^13 + 3^15 + 2*3^16 + 3^18 + 2*3^19 + 2*3^22 + 2*3^23 + 2*3^24 + 2*3^27 + 3^28 + 3^29 + O(3^30)]]
            k5,k6,k7 0.321154513240... 1.55246328915... 0.161999172489...
            initial bound 2.8057927340...e117
            bound_list [58, 58, 58]
            bound_list [8, 9, 9]
            bound_list [9, 7, 7]
            starting search of points using coefficient bound  9
            x-coords of S-integral points via linear combination of mw_base and torsion:
            [-3, -26/9, -8159/2916, -2759/1024, -151/64, -1343/576, -2, -7/4, -1, -47/256, 0, 1/4, 4/9, 9/16, 58/81, 7/9, 6169/6561, 1, 17/16, 2, 33/16, 172/81, 9/4, 25/9, 3, 31/9, 4, 25/4, 1793/256, 8, 625/64, 11, 14, 21, 37, 52, 6142/81, 93, 4537/36, 342, 406, 816, 207331217/4096]
            starting search of extra S-integer points with absolute value bounded by 3.89321964979420
            x-coords of points with bounded absolute value
            [-3, -2, -1, 0, 1, 2]
            Total number of S-integral points: 43
            [(-3 : -1 : 1),
            (-26/9 : -55/27 : 1),
            (-8159/2916 : -390925/157464 : 1),
            (-2759/1024 : -93587/32768 : 1),
            (-151/64 : -1845/512 : 1),
            (-1343/576 : -50399/13824 : 1),
            (-2 : -4 : 1),
            (-7/4 : -33/8 : 1),
            (-1 : -4 : 1),
            (-47/256 : -13287/4096 : 1),
            (0 : -3 : 1),
            (1/4 : -21/8 : 1),
            (4/9 : -62/27 : 1),
            (9/16 : -133/64 : 1),
            (58/81 : -1288/729 : 1),
            (7/9 : -44/27 : 1),
            (6169/6561 : -641312/531441 : 1),
            (1 : -1 : 1),
            (17/16 : -39/64 : 1),
            (2 : -1 : 1),
            (33/16 : -81/64 : 1),
            (172/81 : -1079/729 : 1),
            (9/4 : -15/8 : 1),
            (25/9 : -91/27 : 1),
            (3 : -4 : 1),
            (31/9 : -143/27 : 1),
            (4 : -7 : 1),
            (25/4 : -119/8 : 1),
            (1793/256 : -73087/4096 : 1),
            (8 : -22 : 1),
            (625/64 : -15351/512 : 1),
            (11 : -36 : 1),
            (14 : -52 : 1),
            (21 : -96 : 1),
            (37 : -225 : 1),
            (52 : -375 : 1),
            (6142/81 : -481429/729 : 1),
            (93 : -897 : 1),
            (4537/36 : -305641/216 : 1),
            (342 : -6325 : 1),
            (406 : -8181 : 1),
            (816 : -23310 : 1),
            (207331217/4096 : -2985362435769/262144 : 1)]

        It is not necessary to specify mw_base; if it is not provided,
        then the Mordell-Weil basis must be computed, which may take
        much longer.

        ::

            sage: a = E.S_integral_points([2,3])
            sage: len(a)
            43

        An example with negative discriminant::

            sage: EllipticCurve(\'900d1\').S_integral_points([17], both_signs=True)
            [(-11 : -27 : 1), (-11 : 27 : 1), (-4 : -34 : 1), (-4 : 34 : 1), (4 : -18 : 1),
             (4 : 18 : 1), (2636/289 : -98786/4913 : 1), (2636/289 : 98786/4913 : 1),
             (16 : -54 : 1), (16 : 54 : 1)]

        Output checked with Magma (corrected in 3 cases)::

            sage: [len(e.S_integral_points([2], both_signs=False)) for e in cremona_curves([11..100])] # long time (17s on sage.math, 2011)
            [2, 0, 2, 3, 3, 1, 3, 1, 3, 5, 3, 5, 4, 1, 1, 2, 2, 2, 3, 1, 2, 1, 0, 1, 3, 3, 1, 1, 5, 3, 4, 2, 1, 1, 5, 3, 2, 2, 1, 1, 1, 0, 1, 3, 0, 1, 0, 1, 1, 3, 7, 1, 3, 3, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 1, 3, 3, 1, 1, 1, 0, 1, 3, 3, 1, 1, 7, 1, 0, 1, 1, 0, 1, 2, 0, 3, 1, 2, 1, 3, 1, 2, 2, 4, 5, 3, 2, 1, 1, 6, 1, 0, 1, 3, 1, 3, 3, 1, 1, 1, 1, 1, 3, 1, 5, 1, 2, 4, 1, 1, 1, 1, 1, 0, 1, 0, 2, 2, 0, 0, 1, 0, 1, 1, 6, 1, 0, 1, 1, 0, 4, 3, 1, 2, 1, 2, 3, 1, 1, 1, 1, 8, 3, 1, 2, 1, 2, 0, 8, 2, 0, 6, 2, 3, 1, 1, 1, 3, 1, 3, 2, 1, 3, 1, 2, 1, 6, 9, 3, 3, 1, 1, 2, 3, 1, 1, 5, 5, 1, 1, 0, 1, 1, 2, 3, 1, 1, 2, 3, 1, 3, 1, 1, 1, 1, 0, 0, 1, 3, 3, 1, 3, 1, 1, 2, 2, 0, 0, 6, 1, 0, 1, 1, 1, 1, 3, 1, 2, 6, 3, 1, 2, 2, 1, 1, 1, 1, 7, 5, 4, 3, 3, 1, 1, 1, 1, 1, 1, 8, 5, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 2, 3, 6, 1, 1, 7, 3, 3, 4, 5, 9, 6, 1, 0, 7, 1, 1, 3, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 7, 8, 2, 3, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]

        An example from [PZGH1999]_::

            sage: E = EllipticCurve([0,0,0,-172,505])
            sage: E.rank(), len(E.S_integral_points([3,5,7]))  # long time (5s on sage.math, 2011)
            (4, 72)

        This is curve "7690e1" which failed until :issue:`4805` was fixed::

            sage: EllipticCurve([1,1,1,-301,-1821]).S_integral_points([13,2])
            [(-13 : -4 : 1), (-9 : -12 : 1), (-7 : 2 : 1), (21 : -52 : 1),
             (23 : -76 : 1), (63 : -516 : 1), (71 : -620 : 1), (87 : -844 : 1),
             (2711 : -142540 : 1), (7323 : -630376 : 1), (17687 : -2361164 : 1)]

        - Some parts of this implementation are partially based on the
          function integral_points()

        AUTHORS:

        - Tobias Nagel (2008-12)

        - Michael Mardaus (2008-12)

        - John Cremona (2008-12)
        '''

def cremona_curves(conductors):
    """
    Return iterator over all known curves (in database) with conductor
    in the list of conductors.

    EXAMPLES::

        sage: [(E.label(), E.rank()) for E in cremona_curves(srange(35,40))]
        [('35a1', 0),
         ('35a2', 0),
         ('35a3', 0),
         ('36a1', 0),
         ('36a2', 0),
         ('36a3', 0),
         ('36a4', 0),
         ('37a1', 1),
         ('37b1', 0),
         ('37b2', 0),
         ('37b3', 0),
         ('38a1', 0),
         ('38a2', 0),
         ('38a3', 0),
         ('38b1', 0),
         ('38b2', 0),
         ('39a1', 0),
         ('39a2', 0),
         ('39a3', 0),
         ('39a4', 0)]
    """
def cremona_optimal_curves(conductors):
    """
    Return iterator over all known optimal curves (in database) with
    conductor in the list of conductors.

    EXAMPLES::

        sage: [(E.label(), E.rank()) for E in cremona_optimal_curves(srange(35,40))]
        [('35a1', 0),
         ('36a1', 0),
         ('37a1', 1),
         ('37b1', 0),
         ('38a1', 0),
         ('38b1', 0),
         ('39a1', 0)]

    There is one case -- 990h3 -- when the optimal curve isn't labeled with a 1::

        sage: [e.cremona_label() for e in cremona_optimal_curves([990])]
        ['990a1', '990b1', '990c1', '990d1', '990e1', '990f1', '990g1',
         '990h3', '990i1', '990j1', '990k1', '990l1']
    """
def integral_points_with_bounded_mw_coeffs(E, mw_base, N, x_bound):
    """
    Return the set of integers `x` which are
    `x`-coordinates of points on the curve `E` which
    are linear combinations of the generators (basis and torsion
    points) with coefficients bounded by `N`.

    INPUT:

    - ``E`` -- an elliptic curve
    - ``mw_base`` -- list of points on `E` (generators)
    - ``N`` -- positive integer (bound on coefficients)
    - ``x_bound`` -- a positive real number (upper bound on size of x-coordinates)

    OUTPUT:

    list of integral points on `E` which are linear combinations of the given
    points with coefficients bounded by `N` in absolute value.

    TESTS:

    We check that some large integral points in a paper of Zagier are found::

        sage: def t(a, b, x): # indirect doctest
        ....:     E = EllipticCurve([0,0,0,a,b])
        ....:     xs = [P[0] for P in E.integral_points()]
        ....:     return x in xs
        sage: all(t(a,b,x) for a,b,x in [(-2,5, 1318), (4,-1, 4321),  # long time
        ....: (0,17, 5234), (11,4, 16833), (-13,37, 60721), (-12,-10, 80327),
        ....: (-7,22, 484961), (-9,28, 764396), (-13,4, 1056517), (-19,-51,
        ....: 2955980), (-24,124, 4435710), (-30,133, 5143326), (-37,60,
        ....: 11975623), (-23,-33, 17454557), (-16,49, 19103002), (27,-62,
        ....: 28844402), (37,18, 64039202), (2,97, 90086608), (49,-64,
        ....: 482042404), (-59,74, 7257247018), (94,689, 30841587841),
        ....: (469,1594, 6327540232326), (1785,0, 275702503440)])
        True
    """
def elliptic_curve_congruence_graph(curves):
    """
    Return the congruence graph for this set of elliptic curves.

    INPUT:

    - ``curves`` -- list of elliptic curves

    OUTPUT:

    The graph with each curve as a vertex (labelled by its Cremona
    label) and an edge from `E` to `F` labelled `p` if and only if `E` is
    congruent to `F` mod `p`.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_rational_field import elliptic_curve_congruence_graph
        sage: curves = list(cremona_optimal_curves([11..30]))
        sage: G = elliptic_curve_congruence_graph(curves)
        sage: G
        Graph on 12 vertices
    """
