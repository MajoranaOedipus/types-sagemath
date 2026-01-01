r"""
The Elliptic Curve Factorization Method

The elliptic curve factorization method (ECM) is the fastest way to
factor a **known composite** integer if one of the factors is
relatively small (up to approximately 80 bits / 25 decimal digits). To
factor an arbitrary integer it must be combined with a primality
test. The :meth:`ECM.factor` method is an example for how to combine
ECM with a primality test to compute the prime factorization of integers.

Sage includes GMP-ECM, which is a highly optimized implementation of
Lenstra's elliptic curve factorization method.  See
https://gitlab.inria.fr/zimmerma/ecm for more about GMP-ECM.

AUTHORS:

These people wrote GMP-ECM:
Pierrick Gaudry, Jim Fougeron,
Laurent Fousse, Alexander Kruppa,
Dave Newman, Paul Zimmermann

BUGS:

Output from ecm is non-deterministic. Doctests should set the random
seed, but currently there is no facility to do so.

TESTS:

Check that the issues from :issue:`27199` are fixed::

    sage: n = 16262093986406371
    sage: ecm = ECM()
    sage: ecm.factor(n, B1=10)
    [1009, 1009, 1733, 3023, 3049]

    sage: n = 1308301 * (10^499 + 153)
    sage: ECM(B1=600).one_curve(n, c=1, sigma=10)
    [1308301, 100...00153]
"""
from sage.env import SAGE_ECMBIN as SAGE_ECMBIN
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

class ECM(SageObject):
    def __init__(self, B1: int = 10, B2=None, **kwds) -> None:
        '''
        Create an interface to the GMP-ECM elliptic curve method
        factorization program.

        See https://gitlab.inria.fr/zimmerma/ecm

        INPUT:

        - ``B1`` -- integer; Stage 1 bound

        - ``B2`` -- integer; Stage 2 bound (or interval B2min-B2max)

        In addition the following keyword arguments can be used:

        - ``x0`` -- integer `x`; use `x` as initial point

        - ``sigma`` -- integer `s`; use s as curve generator [ecm]

        - ``A`` -- integer `a`; use a as curve parameter [ecm]

        - ``k`` -- integer `n`; perform `>= n` steps in stage 2

        - ``power`` -- integer `n`; use `x^n` for Brent-Suyama\'s
          extension

        - ``dickson`` -- integer `n`; use `n`-th Dickson\'s polynomial
          for Brent-Suyama\'s extension

        - ``c`` -- integer `n`; perform `n` runs for each input

        - ``pm1`` -- boolean; perform P-1 instead of ECM

        - ``pp1`` -- boolean; perform P+1 instead of ECM

        - ``q`` -- boolean; quiet mode

        - ``v`` -- boolean; verbose mode

        - ``timestamp`` -- boolean; print a time stamp with each number

        - ``mpzmod`` -- boolean; use GMP\'s mpz_mod for mod reduction

        - ``modmuln`` -- boolean; use Montgomery\'s MODMULN for mod reduction

        - ``redc`` -- boolean; use Montgomery\'s REDC for mod reduction

        - ``nobase2`` -- boolean; disable special base-2 code

        - ``base2`` -- integer `n`; force base 2 mode with 2^n+1 (n>0)
          or 2^n-1 (n<0)

        - ``save`` -- string filename; save residues at end of stage 1
          to file

        - ``savea`` -- string filename; Like -save, appends to
          existing files

        - ``resume`` -- string filename; resume residues from file,
          reads from stdin if file is "-"

        - ``primetest`` -- boolean; perform a primality test on input

        - ``treefile`` -- string; store product tree of F in files f.0
          f.1 ...

        - ``i`` -- integer; increment B1 by this constant on each run

        - ``I`` -- integer `f`; auto-calculated increment for B1
          multiplied by `f` scale factor

        - ``inp`` -- string; use file as input (instead of redirecting
          stdin)

        - ``b`` -- boolean; use breadth-first mode of file processing

        - ``d`` -- boolean; use depth-first mode of file processing
          (default)

        - ``one`` -- boolean; stop processing a candidate if a factor
          is found (looping mode )

        - ``n`` -- boolean; run ecm in \'nice\' mode (below normal
          priority)

        - ``nn`` -- boolean; run ecm in \'very nice\' mode (idle
          priority)

        - ``t`` -- integer `n`; trial divide candidates before P-1,
          P+1 or ECM up to `n`

        - ``ve`` -- integer `n`; verbosely show short (`< n`
          character) expressions on each loop

        - ``B2scale`` -- integer; multiplies the default B2 value

        - ``go`` -- integer; preload with group order val, which can
          be a simple expression, or can use N as a placeholder for
          the number being factored

        - ``prp`` -- string; use shell command cmd to do large
          primality tests

        - ``prplen`` -- integer; only candidates longer than this
          number of digits are \'large\'

        - ``prpval`` -- integer; value>=0 which indicates the prp
          command foundnumber to be PRP

        - ``prptmp`` -- file; outputs n value to temp file prior to
          running (NB. gets deleted)

        - ``prplog`` -- file; otherwise get PRP results from this file
          (NB. gets deleted)

        - ``prpyes`` -- string; literal string found in prplog file
          when number is PRP

        - ``prpno`` -- string; literal string found in prplog file
          when number is composite
        '''
    def __call__(self, n):
        """
        Call syntax.

        INPUT:

        - ``n`` -- integer

        OUTPUT: string; the ECM output

        EXAMPLES::

            sage: print(ecm(3))    # random output
            GMP-ECM 6.4.4 [configured with MPIR 2.6.0, --enable-asm-redc] [ECM]
            Input number is 3 (1 digits)
            ********** Factor found in step 1: 3
            Found input number N
        """
    def interact(self) -> None:
        """
        Interactively interact with the ECM program.

        EXAMPLES::

            sage: ecm.interact()    # not tested
        """
    def recommended_B1(self, factor_digits):
        """
        Return recommended ``B1`` setting.

        INPUT:

        - ``factor_digits`` -- integer; number of digits

        OUTPUT:

        Integer. Recommended settings from
        http://www.mersennewiki.org/index.php/Elliptic_Curve_Method

        EXAMPLES::

            sage: ecm.recommended_B1(33)
            1000000
        """
    def one_curve(self, n, factor_digits=None, B1: int = 2000, algorithm: str = 'ECM', **kwds):
        '''
        Run one single ECM (or P-1/P+1) curve on input n.

        Note that trying a single curve is not particularly useful by
        itself. One typically needs to run over thousands of trial
        curves to factor `n`.

        INPUT:

        - ``n`` -- positive integer

        - ``factor_digits`` -- integer; decimal digits estimate of the
          wanted factor

        - ``B1`` -- integer; Stage 1 bound (default: 2000)

        - ``algorithm`` -- either "ECM" (default); "P-1" or "P+1"

        OUTPUT:

        A list ``[p, q]`` where p and q are integers and n = p * q.
        If no factor was found, then p = 1 and q = n.

        .. WARNING::

            Neither p nor q in the output is guaranteed to be prime.

        EXAMPLES::

            sage: f = ECM()
            sage: n = 508021860739623467191080372196682785441177798407961
            sage: f.one_curve(n, B1=10000, sigma=11)
            [1, 508021860739623467191080372196682785441177798407961]
            sage: f.one_curve(n, B1=10000, sigma=1022170541)
            [79792266297612017, 6366805760909027985741435139224233]
            sage: n = 432132887883903108009802143314445113500016816977037257
            sage: f.one_curve(n, B1=500000, algorithm=\'P-1\')
            [67872792749091946529, 6366805760909027985741435139224233]
            sage: n = 2088352670731726262548647919416588631875815083
            sage: f.one_curve(n, B1=2000, algorithm=\'P+1\', x0=5)
            [328006342451, 6366805760909027985741435139224233]
        '''
    def find_factor(self, n, factor_digits=None, B1: int = 2000, **kwds):
        """
        Return a factor of n.

        See also :meth:`factor` if you want a prime factorization of
        `n`.

        INPUT:

        - ``n`` -- positive integer

        - ``factor_digits`` -- integer or ``None`` (default); decimal
          digits estimate of the wanted factor

        - ``B1`` -- integer; Stage 1 bound (default: 2000). This is
          used as bound if ``factor_digits`` is not specified

        - ``kwds`` -- optional keyword parameters

        OUTPUT:

        List of integers whose product is n. For certain lengths of
        the factor, this is the best algorithm to find a
        factor.

        .. NOTE::

            ECM is not a good primality test. Not finding a
            factorization is only weak evidence for `n` being
            prime. You should run a **good** primality test before
            calling this function.

        EXAMPLES::

            sage: f = ECM()
            sage: n = 508021860739623467191080372196682785441177798407961
            sage: f.find_factor(n)
            [79792266297612017, 6366805760909027985741435139224233]

        Note that the input number cannot have more than 4095 digits::

            sage: f = 2^2^14+1
            sage: ecm.find_factor(f)
            Traceback (most recent call last):
            ...
            ValueError: n must have at most 4095 digits
        """
    def factor(self, n, factor_digits=None, B1: int = 2000, proof: bool = False, **kwds):
        """
        Return a probable prime factorization of `n`.

        Combines GMP-ECM with a primality test, see
        :meth:`~sage.rings.integer.Integer.is_prime`. The primality
        test is provable or probabilistic depending on the `proof`
        flag.

        Moreover, for small `n` PARI is used directly.

        .. WARNING::

            There is no mathematical guarantee that the factors
            returned are actually prime if ``proof=False``
            (default). It is extremely likely, though. Currently,
            there are no known examples where this fails.

        INPUT:

        - ``n`` -- positive integer

        - ``factor_digits`` -- integer or ``None`` (default); optional
          guess at how many digits are in the smallest factor

        - ``B1`` -- initial lower bound, defaults to 2000 (15 digit
          factors); used if ``factor_digits`` is not specified

        - ``proof`` -- boolean (default: ``False``); whether to prove
          that the factors are prime

        - ``kwds`` -- keyword arguments to pass to ecm-gmp; see help
          for :class:`ECM` for more details

        OUTPUT: list of integers whose product is `n`

        .. NOTE::

            Trial division should typically be performed, but this is
            not implemented (yet) in this method.

            If you suspect that n is the product of two
            similarly-sized primes, other methods (such as a quadratic
            sieve -- use the qsieve command) will usually be faster.

            The best known algorithm for factoring in the case where
            all factors are large is the general number field
            sieve. This is not implemented in Sage; You probably want
            to use a cluster for problems of this size.

        EXAMPLES::

            sage: ecm.factor(602400691612422154516282778947806249229526581)
            [45949729863572179, 13109994191499930367061460439]
            sage: ecm.factor((2^197 + 1)/3)  # long time
            [197002597249, 1348959352853811313, 251951573867253012259144010843]
            sage: ecm.factor(179427217^13) == [179427217] * 13
            True
        """
    def get_last_params(self):
        """
        Return the parameters (including the curve) of the last ecm run.

        In the case that the number was factored successfully, this
        will return the parameters that yielded the factorization.

        OUTPUT:

        A dictionary containing the parameters for the most recent
        factorization.

        EXAMPLES::

            sage: ecm.factor((2^197 + 1)/3)             # long time
            [197002597249, 1348959352853811313, 251951573867253012259144010843]
            sage: ecm.get_last_params()                 # random output
            {'poly': 'x^1', 'sigma': '1785694449', 'B1': '8885', 'B2': '1002846'}
        """
    def time(self, n, factor_digits, verbose: bool = False) -> None:
        """
        Print a runtime estimate.

        BUGS:

        This method should really return something and not just print
        stuff on the screen.

        INPUT:

        - ``n`` -- positive integer

        - ``factor_digits`` -- the (estimated) number of digits of the
          smallest factor

        OUTPUT:

        An approximation for the amount of time it will take to find a
        factor of size factor_digits in a single process on the
        current computer.  This estimate is provided by GMP-ECM's
        verbose option on a single run of a curve.

        EXAMPLES::

            sage: n = next_prime(11^23)*next_prime(11^37)
            sage: ecm.time(n, 35)                  # random output
            Expected curves: 910, Expected time: 23.95m

            sage: ecm.time(n, 30, verbose=True)     # random output
            GMP-ECM 6.4.4 [configured with MPIR 2.6.0, --enable-asm-redc] [ECM]
            Running on localhost.localdomain
            Input number is 304481639541418099574459496544854621998616257489887231115912293 (63 digits)
            Using MODMULN [mulredc:0, sqrredc:0]
            Using B1=250000, B2=128992510, polynomial Dickson(3), sigma=3244548117
            dF=2048, k=3, d=19110, d2=11, i0=3
            Expected number of curves to find a factor of n digits:
            35  40  45  50  55  60  65  70  75  80
            4911  70940  1226976  2.5e+07  5.8e+08  1.6e+10  2.7e+13  4e+18  5.4e+23  Inf
            Step 1 took 230ms
            Using 10 small primes for NTT
            Estimated memory usage: 4040K
            Initializing tables of differences for F took 0ms
            Computing roots of F took 9ms
            Building F from its roots took 16ms
            Computing 1/F took 9ms
            Initializing table of differences for G took 0ms
            Computing roots of G took 8ms
            Building G from its roots took 16ms
            Computing roots of G took 7ms
            Building G from its roots took 16ms
            Computing G * H took 6ms
            Reducing  G * H mod F took 5ms
            Computing roots of G took 7ms
            Building G from its roots took 17ms
            Computing G * H took 5ms
            Reducing  G * H mod F took 5ms
            Computing polyeval(F,G) took 34ms
            Computing product of all F(g_i) took 0ms
            Step 2 took 164ms
            Expected time to find a factor of n digits:
            35  40  45  50  55  60  65  70  75  80
            32.25m  7.76h  5.60d  114.21d  7.27y  196.42y  337811y  5e+10y  7e+15y  Inf
            <BLANKLINE>
            Expected curves: 4911, Expected time: 32.25m
        """

ecm: ECM
TEST_ECM_OUTPUT_1: str
TEST_ECM_OUTPUT_2: str
TEST_ECM_OUTPUT_3: str
TEST_ECM_OUTPUT_4: str
