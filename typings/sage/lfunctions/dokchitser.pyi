from _typeshed import Incomplete
from sage.env import SAGE_EXTCODE as SAGE_EXTCODE
from sage.misc.verbose import verbose as verbose
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class Dokchitser(SageObject):
    """
    Dokchitser's `L`-functions Calculator.

    PARI code can be found on
    `Dokchitser's homepage <https://people.maths.bris.ac.uk/~matyd/computel>`_.

    Create a Dokchitser `L`-series with

    Dokchitser(conductor, gammaV, weight, eps, poles, residues, init,
    prec)

    where

    - ``conductor`` -- integer; the conductor

    - ``gammaV`` -- list of Gamma-factor parameters, e.g. [0] for
      Riemann zeta, [0,1] for ell.curves, (see examples)

    - ``weight`` -- positive real number, usually an integer e.g. 1 for
      Riemann zeta, 2 for `H^1` of curves/`\\QQ`

    - ``eps`` -- complex number; sign in functional equation

    - ``poles`` -- (default: ``[]``) list of points where `L^*(s)` has
      (simple) poles; only poles with `Re(s)>weight/2` should be
      included

    - ``residues`` -- vector of residues of `L^*(s)` in those poles or
      set ``residues='automatic'`` (default)

    - ``prec`` -- integer (default: 53); number of *bits* of precision

    RIEMANN ZETA FUNCTION:

    We compute with the Riemann Zeta function. ::

        sage: L = Dokchitser(conductor=1, gammaV=[0], weight=1, eps=1, poles=[1], residues=[-1], init='1')
        sage: L
        Dokchitser L-series of conductor 1 and weight 1
        sage: L(1)
        Traceback (most recent call last):
        ...
        ArithmeticError
        sage: L(2)
        1.64493406684823
        sage: L(2, 1.1)
        1.64493406684823
        sage: L.derivative(2)
        -0.937548254315844
        sage: h = RR('0.0000000000001')
        sage: (zeta(2+h) - zeta(2.))/h
        -0.937028232783632
        sage: L.taylor_series(2, k=5)
        1.64493406684823 - 0.937548254315844*z + 0.994640117149451*z^2 - 1.00002430047384*z^3 + 1.00006193307...*z^4 + O(z^5)

    RANK 1 ELLIPTIC CURVE:

    We compute with the `L`-series of a rank `1` curve. ::

        sage: E = EllipticCurve('37a')
        sage: L = E.lseries().dokchitser(algorithm='gp'); L
        Dokchitser L-function associated to Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        sage: L(1)
        0.000000000000000
        sage: L.derivative(1)
        0.305999773834052
        sage: L.derivative(1,2)
        0.373095594536324
        sage: L.num_coeffs()
        48
        sage: L.taylor_series(1,4)
        0.000000000000000 + 0.305999773834052*z + 0.186547797268162*z^2 - 0.136791463097188*z^3 + O(z^4)
        sage: L.check_functional_equation()  # abs tol 1e-19
        6.04442711160669e-18

    RANK 2 ELLIPTIC CURVE:

    We compute the leading coefficient and Taylor expansion of the
    `L`-series of a rank `2` elliptic curve. ::

        sage: E = EllipticCurve('389a')
        sage: L = E.lseries().dokchitser(algorithm='gp')
        sage: L.num_coeffs()
        156
        sage: L.derivative(1,E.rank())
        1.51863300057685
        sage: L.taylor_series(1,4)
        -1.27685190980159e-23 + (7.23588070754027e-24)*z + 0.759316500288427*z^2 - 0.430302337583362*z^3 + O(z^4)  # 32-bit
        -2.72911738151096e-23 + (1.54658247036311e-23)*z + 0.759316500288427*z^2 - 0.430302337583362*z^3 + O(z^4)  # 64-bit

    NUMBER FIELD:

    We compute with the Dedekind zeta function of a number field. ::

        sage: x = var('x')
        sage: K = NumberField(x**4 - x**2 - 1,'a')
        sage: L = K.zeta_function(algorithm='gp')
        sage: L.conductor
        400
        sage: L.num_coeffs()
        264
        sage: L(2)
        1.10398438736918
        sage: L.taylor_series(2,3)
        1.10398438736918 - 0.215822638498759*z + 0.279836437522536*z^2 + O(z^3)

    RAMANUJAN DELTA L-FUNCTION:

    The coefficients are given by Ramanujan's tau function::

        sage: L = Dokchitser(conductor=1, gammaV=[0,1], weight=12, eps=1)
        sage: pari_precode = 'tau(n)=(5*sigma(n,3)+7*sigma(n,5))*n/12 - 35*sum(k=1,n-1,(6*k-4*(n-k))*sigma(k,3)*sigma(n-k,5))'
        sage: L.init_coeffs('tau(k)', pari_precode=pari_precode)

    We redefine the default bound on the coefficients: Deligne's
    estimate on tau(n) is better than the default
    coefgrow(n)= `(4n)^{11/2}` (by a factor 1024), so
    re-defining coefgrow() improves efficiency (slightly faster). ::

        sage: L.num_coeffs()
        12
        sage: L.set_coeff_growth('2*n^(11/2)')
        sage: L.num_coeffs()
        11

    Now we're ready to evaluate, etc. ::

        sage: L(1)
        0.0374412812685155
        sage: L(1, 1.1)
        0.0374412812685155
        sage: L.taylor_series(1,3)
        0.0374412812685155 + 0.0709221123619322*z + 0.0380744761270520*z^2 + O(z^3)
    """
    def __new__(cls, *args, **kwargs): ...
    conductor: Incomplete
    gammaV: Incomplete
    weight: Incomplete
    eps: Incomplete
    poles: Incomplete
    residues: Incomplete
    prec: Incomplete
    def __init__(self, conductor, gammaV, weight, eps, poles=None, residues: str = 'automatic', prec: int = 53, init=None) -> None:
        """
        Initialization of Dokchitser calculator EXAMPLES::

            sage: L = Dokchitser(conductor=1, gammaV=[0], weight=1, eps=1, poles=[1], residues=[-1], init='1')
            sage: L.num_coeffs()
            4
        """
    def __reduce__(self): ...
    def __del__(self) -> None: ...
    def gp(self):
        """
        Return the gp interpreter that is used to implement this Dokchitser
        `L`-function.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: L = E.lseries().dokchitser(algorithm='gp')
            sage: L(2)
            0.546048036215014
            sage: L.gp()
            PARI/GP interpreter
        """
    def num_coeffs(self, T: int = 1):
        """
        Return number of coefficients `a_n` that are needed in
        order to perform most relevant `L`-function computations to
        the desired precision.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: L = E.lseries().dokchitser(algorithm='gp')
            sage: L.num_coeffs()
            26
            sage: E = EllipticCurve('5077a')
            sage: L = E.lseries().dokchitser(algorithm='gp')
            sage: L.num_coeffs()
            568
            sage: L = Dokchitser(conductor=1, gammaV=[0], weight=1, eps=1, poles=[1], residues=[-1], init='1')
            sage: L.num_coeffs()
            4

        Verify that ``num_coeffs`` works with non-real spectral
        parameters, e.g. for the `L`-function of the level 10 Maass form
        with eigenvalue 2.7341055592527126::

            sage: ev = 2.7341055592527126
            sage: L = Dokchitser(conductor=10, gammaV=[ev*i, -ev*i],weight=2,eps=1)
            sage: L.num_coeffs()
            26
        """
    def init_coeffs(self, v, cutoff: int = 1, w=None, pari_precode: str = '', max_imaginary_part: int = 0, max_asymp_coeffs: int = 40):
        '''
        Set the coefficients `a_n` of the `L`-series.

        If `L(s)` is not equal to its dual, pass the coefficients of
        the dual as the second optional argument.

        INPUT:

        - ``v`` -- list of complex numbers or string (pari function of k)

        - ``cutoff`` -- real number (default: 1)

        - ``w`` -- list of complex numbers or string (pari function of k)

        - ``pari_precode`` -- some code to execute in pari
          before calling initLdata

        - ``max_imaginary_part`` -- (default: 0) redefine if
          you want to compute L(s) for s having large imaginary part

        - ``max_asymp_coeffs`` -- (default: 40) at most this
          many terms are generated in asymptotic series for phi(t) and G(s,t)

        EXAMPLES::

            sage: L = Dokchitser(conductor=1, gammaV=[0,1], weight=12, eps=1)
            sage: pari_precode = \'tau(n)=(5*sigma(n,3)+7*sigma(n,5))*n/12 - 35*sum(k=1,n-1,(6*k-4*(n-k))*sigma(k,3)*sigma(n-k,5))\'
            sage: L.init_coeffs(\'tau(k)\', pari_precode=pari_precode)

        Evaluate the resulting `L`-function at a point, and compare with
        the answer that one gets "by definition" (of `L`-function
        attached to a modular form)::

            sage: L(14)
            0.998583063162746
            sage: a = delta_qexp(1000)
            sage: sum(a[n]/float(n)^14 for n in reversed(range(1,1000)))
            0.9985830631627461

        Illustrate that one can give a list of complex numbers for v
        (see :issue:`10937`)::

            sage: L2 = Dokchitser(conductor=1, gammaV=[0,1], weight=12, eps=1)
            sage: L2.init_coeffs(list(delta_qexp(1000))[1:])
            sage: L2(14)
            0.998583063162746

        TESTS:

        Verify that setting the `w` parameter does not raise an error
        (see :issue:`10937`).  Note that the meaning of `w` does not seem to
        be documented anywhere in Dokchitser\'s package yet, so there is
        no claim that the example below is meaningful! ::

            sage: L2 = Dokchitser(conductor=1, gammaV=[0,1], weight=12, eps=1)
            sage: L2.init_coeffs(list(delta_qexp(1000))[1:], w=[1..1000])
        '''
    def __call__(self, s, c=None):
        """
        INPUT:

        - ``s`` -- complex number

        - ``c`` -- internal parameter, call with `c>1` to get the same value
          with a different cutoff point (`c` close to `1`); should return the
          same answer, good to check if everything works with right precision

        .. NOTE::

           Evaluation of the function takes a long time, so each
           evaluation is cached. Call ``self._clear_value_cache()`` to
           clear the evaluation cache.

        EXAMPLES::

            sage: E = EllipticCurve('5077a')
            sage: L = E.lseries().dokchitser(100, algorithm='gp')
            sage: L(1)
            0.00000000000000000000000000000
            sage: L(1+I)
            -1.3085436607849493358323930438 + 0.81298000036784359634835412129*I
            sage: L(1+I, 1.2)
            -1.3085436607849493358323930438 + 0.81298000036784359634835412129*I

        TESTS::

            sage: L(1+I, 0)
            Traceback (most recent call last):
            ...
            RuntimeError
        """
    def derivative(self, s, k: int = 1):
        """
        Return the `k`-th derivative of the `L`-series at `s`.

        .. WARNING::

           If `k` is greater than the order of vanishing of
           `L` at `s` you may get nonsense.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: L = E.lseries().dokchitser(algorithm='gp')
            sage: L.derivative(1,E.rank())
            1.51863300057685
        """
    def taylor_series(self, a: int = 0, k: int = 6, var: str = 'z'):
        '''
        Return the first `k` terms of the Taylor series expansion
        of the `L`-series about `a`.

        This is returned as a series in ``var``, where you
        should view ``var`` as equal to `s-a`. Thus
        this function returns the formal power series whose coefficients
        are `L^{(n)}(a)/n!`.

        INPUT:

        - ``a`` -- complex number (default: 0); point about which to expand

        - ``k`` -- integer (default: 6); series is `O(\\texttt{var}^k)`

        - ``var`` -- string (default: ``\'z\'``); variable of power series

        EXAMPLES::

            sage: L = Dokchitser(conductor=1, gammaV=[0], weight=1, eps=1, poles=[1], residues=[-1], init=\'1\')
            sage: L.taylor_series(2, 3)
            1.64493406684823 - 0.937548254315844*z + 0.994640117149451*z^2 + O(z^3)
            sage: E = EllipticCurve(\'37a\')
            sage: L = E.lseries().dokchitser(algorithm=\'gp\')
            sage: L.taylor_series(1)
            0.000000000000000 + 0.305999773834052*z + 0.186547797268162*z^2 - 0.136791463097188*z^3 + 0.0161066468496401*z^4 + 0.0185955175398802*z^5 + O(z^6)

        We compute a Taylor series where each coefficient is to high
        precision. ::

            sage: E = EllipticCurve(\'389a\')
            sage: L = E.lseries().dokchitser(200, algorithm=\'gp\')
            sage: L.taylor_series(1,3)
            ...e-82 + (...e-82)*z + 0.75931650028842677023019260789472201907809751649492435158581*z^2 + O(z^3)

        Check that :issue:`25402` is fixed::

            sage: L = EllipticCurve("24a1").modular_form().lseries()
            sage: L.taylor_series(-1, 3)
            0.000000000000000 - 0.702565506265199*z + 0.638929001045535*z^2 + O(z^3)

        Check that :issue:`25965` is fixed::

            sage: L2 = EllipticCurve("37a1").modular_form().lseries(); L2
            L-series associated to the cusp form q - 2*q^2 - 3*q^3 + 2*q^4 - 2*q^5 + O(q^6)
            sage: L2.taylor_series(0,4)
            0.000000000000000 - 0.357620466127498*z + 0.273373112603865*z^2 + 0.303362857047671*z^3 + O(z^4)
            sage: L2.taylor_series(0,1)
            O(z^1)
            sage: L2(0)
            0.000000000000000
        '''
    def check_functional_equation(self, T: float = 1.2):
        '''
        Verifies how well numerically the functional equation is satisfied,
        and also determines the residues if ``self.poles !=
        []`` and residues=\'automatic\'.

        More specifically: for `T>1` (default: 1.2),
        ``self.check_functional_equation(T)`` should ideally
        return 0 (to the current precision).

        - if what this function returns does not look like 0 at all,
          probably the functional equation is wrong (i.e. some of the
          parameters gammaV, conductor etc., or the coefficients are wrong),

        - if checkfeq(T) is to be used, more coefficients have to be
          generated (approximately T times more), e.g. call cflength(1.3),
          initLdata("a(k)",1.3), checkfeq(1.3)

        - T=1 always (!) returns 0, so T has to be away from 1

        - default value `T=1.2` seems to give a reasonable
          balance

        - if you don\'t have to verify the functional equation or the
          L-values, call num_coeffs(1) and initLdata("a(k)",1), you need
          slightly less coefficients.

        EXAMPLES::

            sage: L = Dokchitser(conductor=1, gammaV=[0], weight=1, eps=1, poles=[1], residues=[-1], init=\'1\')
            sage: L.check_functional_equation()  # abs tol 1e-19
            -2.71050543121376e-20

        If we choose the sign in functional equation for the
        `\\zeta` function incorrectly, the functional equation
        doesn\'t check out. ::

            sage: L = Dokchitser(conductor=1, gammaV=[0], weight=1, eps=-11, poles=[1], residues=[-1], init=\'1\')
            sage: L.check_functional_equation()
            -9.73967861488124
        '''
    def set_coeff_growth(self, coefgrow) -> None:
        """
        You might have to redefine the coefficient growth function if the
        `a_n` of the `L`-series are not given by the
        following PARI function::

                        coefgrow(n) = if(length(Lpoles),
                                          1.5*n^(vecmax(real(Lpoles))-1),
                                          sqrt(4*n)^(weight-1));


        INPUT:

        - ``coefgrow`` -- string that evaluates to a PARI function of n that
          defines a coefgrow function

        EXAMPLES::

            sage: L = Dokchitser(conductor=1, gammaV=[0,1], weight=12, eps=1)
            sage: pari_precode = 'tau(n)=(5*sigma(n,3)+7*sigma(n,5))*n/12 - 35*sum(k=1,n-1,(6*k-4*(n-k))*sigma(k,3)*sigma(n-k,5))'
            sage: L.init_coeffs('tau(k)', pari_precode=pari_precode)
            sage: L.set_coeff_growth('2*n^(11/2)')
            sage: L(1)
            0.0374412812685155
        """

def reduce_load_dokchitser(D): ...
