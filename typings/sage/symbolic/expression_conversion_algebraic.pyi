from _typeshed import Incomplete
from operator import eq as eq, ge as ge, gt as gt, le as le, lt as lt, ne as ne, neg as neg, truediv as truediv
from sage.functions.all import exp as exp
from sage.symbolic.expression_conversions import Converter as Converter
from sage.symbolic.operators import add_vararg as add_vararg, mul_vararg as mul_vararg
from sage.symbolic.ring import SR as SR

class AlgebraicConverter(Converter):
    field: Incomplete
    reciprocal_trig_functions: Incomplete
    def __init__(self, field) -> None:
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import AlgebraicConverter
            sage: a = AlgebraicConverter(QQbar)
            sage: a.field
            Algebraic Field
            sage: a.reciprocal_trig_functions['cot']
            tan
        """
    def pyobject(self, ex, obj):
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import AlgebraicConverter
            sage: a = AlgebraicConverter(QQbar)
            sage: f = SR(2)
            sage: a.pyobject(f, f.pyobject())
            2
            sage: _.parent()
            Algebraic Field
        """
    def arithmetic(self, ex, operator):
        """
        Convert a symbolic expression to an algebraic number.

        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import AlgebraicConverter
            sage: f = 2^(1/2)
            sage: a = AlgebraicConverter(QQbar)
            sage: a.arithmetic(f, f.operator())
            1.414213562373095?

        TESTS::

            sage: f = pi^6
            sage: a = AlgebraicConverter(QQbar)
            sage: a.arithmetic(f, f.operator())
            Traceback (most recent call last):
            ...
            TypeError: unable to convert pi^6 to Algebraic Field

        Test that :issue:`14602` is fixed::

            sage: K = QuadraticField(3)
            sage: K(sqrt(3)).parent() is K
            True
            sage: sqrt(K(3)).parent() is K
            True
            sage: (K(3)^(1/2)).parent()
            Symbolic Ring
            sage: bool(K.gen() == K(3)^(1/2) == sqrt(K(3)) == K(sqrt(3)) == sqrt(3))
            True
            sage: L = QuadraticField(3, embedding=-AA(3).sqrt())
            sage: bool(L.gen() == -sqrt(3))
            True
        """
    def composition(self, ex, operator):
        '''
        Coerce to an algebraic number.

        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import AlgebraicConverter
            sage: a = AlgebraicConverter(QQbar)
            sage: a.composition(exp(I*pi/3, hold=True), exp)
            0.500000000000000? + 0.866025403784439?*I
            sage: a.composition(sin(pi/7), sin)
            0.4338837391175581? + 0.?e-18*I

            sage: x = SR.var(\'x\')
            sage: a.composition(complex_root_of(x^3 - x^2 - x - 1, 0), complex_root_of)
            1.839286755214161?
            sage: a.composition(complex_root_of(x^5 - 1, 3), complex_root_of)
            0.3090169943749474? - 0.9510565162951536?*I
            sage: a.composition(complex_root_of(x^2 + 1, 0), complex_root_of)
            1.?e-683 - 0.9999999999999999?*I
            sage: a.composition(complex_root_of(x^2 + 1, 1), complex_root_of)
            1.?e-683 + 0.9999999999999999?*I

        TESTS::

            sage: QQbar(zeta(7))
            Traceback (most recent call last):
            ...
            TypeError: unable to convert zeta(7) to Algebraic Field

        Test :issue:`22571`::

            sage: a.composition(exp(0, hold=True), exp)
            1
            sage: a.composition(exp(1, hold=True), exp)
            Traceback (most recent call last):
            ...
            ValueError: unable to represent as an algebraic number
            sage: a.composition(exp(pi*I*RR(1), hold=True), exp)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert e^(1.00000000000000*I*pi) to Algebraic Field
            sage: a.composition(exp(pi*CC.gen(), hold=True), exp)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert e^(1.00000000000000*I*pi) to Algebraic Field
            sage: bool(sin(pi*RR("0.7000000000000002")) > 0)
            True

        Check that :issue:`24440` is fixed::

            sage: QQbar(tanh(pi + 0.1))
            Traceback (most recent call last):
            ...
            ValueError: unable to represent as an algebraic number
            sage: QQbar(sin(I*pi/7))
            Traceback (most recent call last):
            ...
            ValueError: unable to represent as an algebraic number
            sage: QQbar(sin(I*pi/7, hold=True))
            Traceback (most recent call last):
            ...
            ValueError: unable to represent as an algebraic number
        '''

def algebraic(ex, field):
    """
    Return the symbolic expression ``ex`` as a element of the algebraic
    field ``field``.

    EXAMPLES::

        sage: a = SR(5/6)
        sage: AA(a)
        5/6
        sage: type(AA(a))
        <class 'sage.rings.qqbar.AlgebraicReal'>
        sage: QQbar(a)
        5/6
        sage: type(QQbar(a))
        <class 'sage.rings.qqbar.AlgebraicNumber'>
        sage: QQbar(i)
        I
        sage: AA(golden_ratio)
        1.618033988749895?
        sage: QQbar(golden_ratio)
        1.618033988749895?
        sage: QQbar(sin(pi/3))
        0.866025403784439?

        sage: QQbar(sqrt(2) + sqrt(8))
        4.242640687119285?
        sage: AA(sqrt(2) ^ 4) == 4
        True
        sage: AA(-golden_ratio)
        -1.618033988749895?
        sage: QQbar((2*SR(I))^(1/2))
        1 + 1*I
        sage: QQbar(e^(pi*I/3))
        0.50000000000000000? + 0.866025403784439?*I

        sage: AA(x*sin(0))
        0
        sage: QQbar(x*sin(0))
        0
    """
