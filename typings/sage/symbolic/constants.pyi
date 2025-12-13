from _typeshed import Incomplete
from sage.symbolic.expression import Expression as Expression, E as E, PynacConstant as PynacConstant
from sage.rings.infinity import infinity as infinity, minus_infinity as minus_infinity, unsigned_infinity as unsigned_infinity
from sage.structure.richcmp import op_EQ as op_EQ, op_GE as op_GE, op_LE as op_LE, richcmp_method as richcmp_method
from sage.symbolic.expression import E as E, init_pynac_I as init_pynac_I, register_symbol as register_symbol

constants_table: Incomplete
constants_name_table: Incomplete
I: Incomplete

def unpickle_Constant(class_name, name, conversions, latex, mathml, domain):
    """
    EXAMPLES::

        sage: from sage.symbolic.constants import unpickle_Constant
        sage: a = unpickle_Constant('Constant', 'a', {}, 'aa', '', 'positive')
        sage: a.domain()
        'positive'
        sage: latex(a)
        aa

    Note that if the name already appears in the
    ``constants_name_table``, then that will be returned instead of
    constructing a new object::

        sage: pi = unpickle_Constant('Pi', 'pi', None, None, None, None)
        sage: pi._maxima_init_()
        '%pi'
    """

class Constant:
    _pynac: PynacConstant

    def __init__(self, name, conversions=None, latex=None, mathml: str = '', domain: str = 'complex') -> None:
        """
        EXAMPLES::

            sage: from sage.symbolic.constants import Constant
            sage: p = Constant('p')
            sage: loads(dumps(p))
            p
        """
    def __richcmp__(self, other, op):
        """
        EXAMPLES::

            sage: from sage.symbolic.constants import Constant
            sage: p = Constant('p')
            sage: s = Constant('s')
            sage: p == p
            True
            sage: p == s
            False
            sage: p != s
            True
        """
    def __reduce__(self):
        """
        Add support for pickling constants.

        EXAMPLES::

            sage: from sage.symbolic.constants import Constant
            sage: p = Constant('p')
            sage: p.__reduce__()
            (<function unpickle_Constant at 0x...>,
             ('Constant', 'p', {}, 'p', '', 'complex'))
            sage: loads(dumps(p))
            p

            sage: pi.pyobject().__reduce__()
            (<function unpickle_Constant at 0x...>,
             ('Pi',
              'pi',
              ...,
              '\\pi',
              '<mi>&pi;</mi>',
              'positive'))
            sage: loads(dumps(pi.pyobject()))
            pi
        """
    def domain(self) -> str:
        """
        Return the domain of this constant.  This is either positive,
        real, or complex, and is used by Pynac to make inferences
        about expressions containing this constant.

        EXAMPLES::

            sage: p = pi.pyobject(); p
            pi
            sage: type(_)
            <class 'sage.symbolic.constants.Pi'>
            sage: p.domain()
            'positive'
        """
    def expression(self) -> Expression:
        """
        Return an expression for this constant.

        EXAMPLES::

            sage: a = pi.pyobject()
            sage: pi2 = a.expression()
            sage: pi2
            pi
            sage: pi2 + 2
            pi + 2
            sage: pi - pi2
            0
        """
    def name(self) -> str:
        """
        Return the name of this constant.

        EXAMPLES::

            sage: from sage.symbolic.constants import Constant
            sage: c = Constant('c')
            sage: c.name()
            'c'
        """

class Pi(Constant):
    def __init__(self, name: str = 'pi') -> None:
        """
        TESTS::

            sage: pi._latex_()
            '\\\\pi'
            sage: latex(pi)
            \\pi
            sage: mathml(pi)
            <mi>&pi;</mi>
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(pi)
            3.141592653589793
        """

pi = Pi().expression()
e = E()

class NotANumber(Constant):
    """
    Not a Number
    """
    def __init__(self, name: str = 'NaN') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(NaN))
            NaN
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(NaN)
            nan
        """

NaN = NotANumber().expression()

class GoldenRatio(Constant):
    """
    The number (1+sqrt(5))/2.

    EXAMPLES::

        sage: gr = golden_ratio
        sage: RR(gr)
        1.61803398874989
        sage: R = RealField(200)
        sage: R(gr)
        1.6180339887498948482045868343656381177203091798057628621354
        sage: grm = maxima(golden_ratio);grm
        (sqrt(5)+1)/2
        sage: grm + grm
        sqrt(5)+1
        sage: float(grm + grm)
        3.23606797749979
    """
    def __init__(self, name: str = 'golden_ratio') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(golden_ratio))
            golden_ratio
        """
    def minpoly(self, bits=None, degree=None, epsilon: int = 0):
        """
        EXAMPLES::

            sage: golden_ratio.minpoly()
            x^2 - x - 1
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(golden_ratio)
            1.618033988749895
            sage: golden_ratio.__float__()
            1.618033988749895
        """

golden_ratio = GoldenRatio().expression()

class Log2(Constant):
    """
    The natural logarithm of the real number 2.

    EXAMPLES::

        sage: log2
        log2
        sage: float(log2)
        0.6931471805599453
        sage: RR(log2)
        0.693147180559945
        sage: R = RealField(200); R
        Real Field with 200 bits of precision
        sage: R(log2)
        0.69314718055994530941723212145817656807550013436025525412068
        sage: l = (1-log2)/(1+log2); l
        -(log2 - 1)/(log2 + 1)
        sage: R(l)
        0.18123221829928249948761381864650311423330609774776013488056
        sage: maxima(log2)
        log(2)
        sage: maxima(log2).float()
        0.6931471805599453
        sage: gp(log2)
        0.69314718055994530941723212145817656807
        sage: RealField(150)(2).log()
        0.69314718055994530941723212145817656807550013
        sage: giac(log2)  # optional - giac
        ln(2)
    """
    def __init__(self, name: str = 'log2') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(log2))
            log2
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(log2)
            0.6931471805599453
            sage: log2.__float__()
            0.6931471805599453
        """

log2 = Log2().expression()

class EulerGamma(Constant):
    """
    The limiting difference between the harmonic series and the natural
    logarithm.

    EXAMPLES::

        sage: R = RealField()
        sage: R(euler_gamma)
        0.577215664901533
        sage: R = RealField(200); R
        Real Field with 200 bits of precision
        sage: R(euler_gamma)
        0.57721566490153286060651209008240243104215933593992359880577
        sage: eg = euler_gamma + euler_gamma; eg
        2*euler_gamma
        sage: R(eg)
        1.1544313298030657212130241801648048620843186718798471976115
    """
    def __init__(self, name: str = 'euler_gamma') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(euler_gamma))
            euler_gamma
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(euler_gamma)
            0.5772156649015329
        """

euler_gamma = EulerGamma().expression()

class Catalan(Constant):
    """
    A number appearing in combinatorics defined as the Dirichlet beta
    function evaluated at the number 2.

    EXAMPLES::

        sage: catalan^2 + mertens
        mertens + catalan^2
    """
    def __init__(self, name: str = 'catalan') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(catalan))
            catalan
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(catalan)
            0.915965594177219
        """

catalan = Catalan().expression()

class Khinchin(Constant):
    """
    The geometric mean of the continued fraction expansion of any
    (almost any) real number.

    EXAMPLES::

        sage: float(khinchin)
        2.6854520010653062
        sage: khinchin.n(digits=60)
        2.68545200106530644530971483548179569382038229399446295305115
        sage: m = mathematica(khinchin); m             # optional - mathematica
        Khinchin
        sage: m.N(200)                                 # optional - mathematica
        2.685452001065306445309714835481795693820382293...32852204481940961807
    """
    def __init__(self, name: str = 'khinchin') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(khinchin))
            khinchin
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(khinchin)
            2.6854520010653062
        """

khinchin = Khinchin().expression()

class TwinPrime(Constant):
    """
    The Twin Primes constant is defined as
    `\\prod 1 - 1/(p-1)^2` for primes `p > 2`.

    EXAMPLES::

        sage: float(twinprime)
        0.6601618158468696
        sage: twinprime.n(digits=60)
        0.660161815846869573927812110014555778432623360284733413319448
    """
    def __init__(self, name: str = 'twinprime') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(twinprime))
            twinprime
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(twinprime)
            0.6601618158468696
        """

twinprime = TwinPrime().expression()

class Mertens(Constant):
    """
    The Mertens constant is related to the Twin Primes constant and
    appears in Mertens' second theorem.

    EXAMPLES::

        sage: float(mertens)
        0.26149721284764277
        sage: mertens.n(digits=60)
        0.261497212847642783755426838608695859051566648261199206192064
    """
    def __init__(self, name: str = 'mertens') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(mertens))
            mertens
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(mertens)
            0.26149721284764277
        """

mertens = Mertens().expression()

class Glaisher(Constant):
    """
    The Glaisher-Kinkelin constant `A = \\exp(\\frac{1}{12}-\\zeta'(-1))`.

    EXAMPLES::

        sage: float(glaisher)
        1.2824271291006226
        sage: glaisher.n(digits=60)
        1.28242712910062263687534256886979172776768892732500119206374
        sage: a = glaisher + 2
        sage: a
        glaisher + 2
        sage: parent(a)
        Symbolic Ring
    """
    def __init__(self, name: str = 'glaisher') -> None:
        """
        EXAMPLES::

            sage: loads(dumps(glaisher))
            glaisher
        """
    def __float__(self) -> float:
        """
        EXAMPLES::

            sage: float(glaisher)
            1.2824271291006226
        """

glaisher = Glaisher().expression()
