from _typeshed import Incomplete
from operator import add as add, mul as mul, neg as neg, pow as pow, truediv as truediv
from sage.structure.element import Expression as Expression
from sage.symbolic.expression_conversions import Converter as Converter
from sage.symbolic.operators import arithmetic_operators as arithmetic_operators

class SympyConverter(Converter):
    """
    Convert any expression to SymPy.

    EXAMPLES::

        sage: import sympy
        sage: var('x,y')
        (x, y)
        sage: f = exp(x^2) - arcsin(pi+x)/y
        sage: f._sympy_()
        exp(x**2) - asin(x + pi)/y
        sage: _._sage_()
        -arcsin(pi + x)/y + e^(x^2)

        sage: sympy.sympify(x) # indirect doctest
        x

    TESTS:

    Make sure we can convert I (:issue:`6424`)::

        sage: bool(I._sympy_() == I)
        True
        sage: (x+I)._sympy_()
        x + I
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()  # indirect doctest
            sage: TestSuite(s).run(skip='_test_pickling')
        """
    def __call__(self, ex=None):
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()
            sage: f(x, y) = x^2 + y^2; f
            (x, y) |--> x^2 + y^2
            sage: s(f)
            Lambda((x, y), x**2 + y**2)
        """
    def pyobject(self, ex, obj):
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()
            sage: f = SR(2)
            sage: s.pyobject(f, f.pyobject())
            2
            sage: type(_)
            <class 'sympy.core.numbers.Integer'>
        """
    def arithmetic(self, ex, operator):
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()
            sage: f = x + 2
            sage: s.arithmetic(f, f.operator())
            x + 2
        """
    def symbol(self, ex):
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()
            sage: s.symbol(x)
            x
            sage: type(_)
            <class 'sympy.core.symbol.Symbol'>
        """
    def relation(self, ex, op):
        """
        EXAMPLES::

            sage: import operator
            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()
            sage: s.relation(x == 3, operator.eq)
            Eq(x, 3)
            sage: s.relation(pi < 3, operator.lt)
            pi < 3
            sage: s.relation(x != pi, operator.ne)
            Ne(x, pi)
            sage: s.relation(x > 0, operator.gt)
            x > 0
        """
    def composition(self, ex, operator):
        """
        EXAMPLES::

            sage: from sage.symbolic.expression_conversions import SympyConverter
            sage: s = SympyConverter()
            sage: f = sin(2)
            sage: s.composition(f, f.operator())
            sin(2)
            sage: type(_)
            sin
            sage: f = arcsin(2)
            sage: s.composition(f, f.operator())
            asin(2)
        """
    def tuple(self, ex):
        """
        Conversion of tuples.

        EXAMPLES::

            sage: t = SR._force_pyobject((3, 4, e^x))
            sage: t._sympy_()
            (3, 4, e^x)
            sage: t = SR._force_pyobject((cos(x),))
            sage: t._sympy_()
            (cos(x),)

        TESTS::

            sage: from sage.symbolic.expression_conversions import sympy_converter
            sage: F = hypergeometric([1/3,2/3],[1,1],x)
            sage: F._sympy_()
            hyper((1/3, 2/3), (1, 1), x)

            sage: F = hypergeometric([1/3,2/3],[1],x)
            sage: F._sympy_()
            hyper((1/3, 2/3), (1,), x)

            sage: var('a,b,c,d')
            (a, b, c, d)
            sage: hypergeometric((a,b,),(c,),d)._sympy_()
            hyper((a, b), (c,), d)
        """
    def derivative(self, ex, operator):
        """
        Convert the derivative of ``self`` in sympy.

        INPUT:

        - ``ex`` -- a symbolic expression

        - ``operator`` -- operator

        TESTS::

            sage: var('x','y')
            (x, y)

            sage: f_sage = function('f_sage')(x, y)
            sage: f_sympy = f_sage._sympy_()

            sage: df_sage = f_sage.diff(x, 2, y, 1); df_sage
            diff(f_sage(x, y), x, x, y)
            sage: df_sympy = df_sage._sympy_(); df_sympy
            Derivative(f_sage(x, y), (x, 2), y)
            sage: df_sympy == f_sympy.diff(x, 2, y, 1)
            True

        Check that :issue:`28964` is fixed::

            sage: f = function('f')
            sage: _ = var('x,t')
            sage: diff(f(x, t), x)._sympy_(), diff(f(x, t), t)._sympy_()
            (Derivative(f(x, t), x), Derivative(f(x, t), t))

        Check differentiating by variables with multiple occurrences
        (:issue:`28964`)::

            sage: f = function('f')
            sage: _ = var('x1,x2,x3,x,t')
            sage: f(x, x, t).diff(x)._sympy_()._sage_()
            D[0](f)(x, x, t) + D[1](f)(x, x, t)

            sage: g = f(x1, x2, x3, t).diff(x1, 2, x2).subs(x1==x, x2==x, x3==x); g
            D[0, 0, 1](f)(x, x, x, t)
            sage: g._sympy_()
            Subs(Derivative(f(_xi_1, _xi_2, x, t), (_xi_1, 2), _xi_2),
                 (_xi_1, _xi_2), (x, x))
            sage: assert g._sympy_()._sage_() == g

        Check that the use of dummy variables does not cause a collision::

            sage: f = function('f')
            sage: _ = var('x1,x2,x,xi_1')
            sage: g = f(x1, x2, xi_1).diff(x1).subs(x1==x, x2==x); g
            D[0](f)(x, x, xi_1)
            sage: assert g._sympy_()._sage_() == g
        """

sympy_converter: Incomplete
