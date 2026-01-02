r"""
Piecewise functions

This module implement piecewise functions in a single variable. See
:mod:`sage.sets.real_set` for more information about how to construct
subsets of the real line for the domains.

EXAMPLES::

    sage: f = piecewise([((0,1), x^3), ([-1,0], -x^2)]);  f
    piecewise(x|-->x^3 on (0, 1), x|-->-x^2 on [-1, 0]; x)
    sage: 2*f
    2*piecewise(x|-->x^3 on (0, 1), x|-->-x^2 on [-1, 0]; x)
    sage: f(x=1/2)
    1/8
    sage: plot(f)    # not tested

.. TODO::

    Implement max/min location and values,

AUTHORS:

- David Joyner (2006-04): initial version

- David Joyner (2006-09): added __eq__, extend_by_zero_to, unextend,
  convolution, trapezoid, trapezoid_integral_approximation,
  riemann_sum, riemann_sum_integral_approximation, tangent_line fixed
  bugs in __mul__, __add__

- David Joyner (2007-03): adding Hann filter for FS, added general FS
  filter methods for computing and plotting, added options to plotting
  of FS (eg, specifying rgb values are now allowed). Fixed bug in
  documentation reported by Pablo De Napoli.

- David Joyner (2007-09): bug fixes due to behaviour of
  SymbolicArithmetic

- David Joyner (2008-04): fixed docstring bugs reported by J Morrow; added
  support for Laplace transform of functions with infinite support.

- David Joyner (2008-07): fixed a left multiplication bug reported by
  C. Boncelet (by defining __rmul__ = __mul__).

- Paul Butler (2009-01): added indefinite integration and default_variable

- Volker Braun (2013): Complete rewrite

- Ralf Stephan (2015): Rewrite of convolution() and other calculus
  functions; many doctest adaptations

- Eric Gourgoulhon (2017): Improve documentation and user interface of
  Fourier series

TESTS::

    sage: fast_callable(f, vars=[x])(0.5)
    0.125000000000...
"""
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity, minus_infinity as minus_infinity
from sage.sets.real_set import RealSet as RealSet
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

class PiecewiseFunction(BuiltinFunction):
    def __init__(self) -> None:
        """
        Piecewise function.

        EXAMPLES::

            sage: var('x, y')
            (x, y)
            sage: f = piecewise([((0,1), x^2*y), ([-1,0], -x*y^2)], var=x);  f
            piecewise(x|-->x^2*y on (0, 1), x|-->-x*y^2 on [-1, 0]; x)
            sage: f(1/2)
            1/4*y
            sage: f(-1/2)
            1/2*y^2
        """
    type Domain = Incomplete
    type Func = Incomplete
    def __call__(self, function_piecesL: Sequence[tuple[Domain, Func]],  # pyright: ignore[reportIncompatibleMethodOverride]
                 var = None, **kwds):
        """
        Piecewise functions.

        INPUT:

        - ``function_pieces`` -- list of pairs consisting of a
          domain and a symbolic function

        - ``var=x`` -- a symbolic variable or ``None`` (default); the
          real variable in which the function is piecewise in

        OUTPUT:

        A piecewise-defined function. A :exc:`ValueError` will be raised
        if the domains of the pieces are not pairwise disjoint.

        EXAMPLES::

            sage: my_abs = piecewise([((-1, 0), -x), ([0, 1], x)], var=x);  my_abs
            piecewise(x|-->-x on (-1, 0), x|-->x on [0, 1]; x)
            sage: [ my_abs(i/5) for i in range(-4, 5)]
            [4/5, 3/5, 2/5, 1/5, 0, 1/5, 2/5, 3/5, 4/5]

        TESTS::

            sage: piecewise([([-1, 0], -x), ([0, 1], x)], var=x)
            Traceback (most recent call last):
            ...
            ValueError: domains must be pairwise disjoint

            sage: step = piecewise([((-1, 0), -1), ([0, 0], 0), ((0, 1), 1)], var=x);  step
            piecewise(x|-->-1 on (-1, 0), x|-->0 on {0}, x|-->1 on (0, 1); x)
            sage: step(-1/2), step(0), step(1/2)
            (-1, 0, 1)
        """
    @staticmethod
    def in_operands(ex) -> bool:
        """
        Return whether a symbolic expression contains a piecewise
        function as operand.

        INPUT:

        - ``ex`` -- a symbolic expression

        OUTPUT: boolean

        EXAMPLES::

            sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
            piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
            sage: piecewise.in_operands(f)
            True
            sage: piecewise.in_operands(1+sin(f))
            True
            sage: piecewise.in_operands(1+sin(0*f))
            False
        """
    @staticmethod
    def simplify(ex) -> None:
        """
        Combine piecewise operands into single piecewise function.

        OUTPUT:

        A piecewise function whose operands are not piecewise if
        possible, that is, as long as the piecewise variable is the same.

        EXAMPLES::

            sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))])
            sage: piecewise.simplify(f)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    class EvaluationMethods:
        def __pow__(self, parameters, variable, n):
            """
            Return the `n`-th power of the piecewise function by applying the
            operation to each piece.

            INPUT:

            - ``n`` -- number or symbolic expression

            EXAMPLES::

                sage: f1(x) = -abs(x) + 1; f2(x) = abs(x - 2) - 1
                sage: f = piecewise([[(-1,1), f1], [(1,3), f2]])
                sage: (f^2).integral(definite=True)
                4/3
            """
        def expression_at(self, parameters, variable, point):
            """
            Return the expression defining the piecewise function at
            ``value``.

            INPUT:

            - ``point`` -- a real number

            OUTPUT:

            The symbolic expression defining the function value at the
            given ``point``.

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: f.expression_at(0)
                sin(x)
                sage: f.expression_at(1)
                cos(x)
                sage: f.expression_at(2)
                Traceback (most recent call last):
                ...
                ValueError: point is not in the domain
            """
        which_function = expression_at
        def domains(self, parameters, variable):
            """
            Return the individual domains.

            See also :meth:`~expressions`.

            OUTPUT:

            The collection of domains of the component functions as a
            tuple of :class:`~sage.sets.real_set.RealSet`.

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: f.domains()
                ({0}, (0, 2))
            """
        def domain(self, parameters, variable):
            """
            Return the domain.

            OUTPUT:

            The union of the domains of the individual pieces as a
            :class:`~sage.sets.real_set.RealSet`.

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: f.domain()
                [0, 2)
            """
        def __len__(self, parameters, variable) -> int:
            '''
            Return the number of "pieces".

            OUTPUT: integer

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: len(f)
                2
            '''
        def expressions(self, parameters, variable):
            """
            Return the individual domains.

            See also :meth:`~domains`.

            OUTPUT: the collection of expressions of the component functions

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: f.expressions()
                (sin(x), cos(x))
            """
        def items(self, parameters, variable) -> Generator[Incomplete, Incomplete]:
            """
            Iterate over the pieces of the piecewise function.

            .. NOTE::

                You should probably use :meth:`pieces` instead, which
                offers a nicer interface.

            OUTPUT:

            This method iterates over pieces of the piecewise
            function, each represented by a pair. The first element is
            the support, and the second the function over that
            support.

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))])
                sage: for support, function in f.items():
                ....:     print('support is {0}, function is {1}'.format(support, function))
                support is {0}, function is sin(x)
                support is (0, 2), function is cos(x)
            """
        def __call__(self, parameters, variable, value=None, **kwds):
            """
            Call the piecewise function.

            EXAMPLES::

                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: f(0)
                0
                sage: f(1)
                cos(1)
                sage: f(2)
                Traceback (most recent call last):
                ...
                ValueError: point 2 is not in the domain
            """
        def restriction(self, parameters, variable, restricted_domain):
            """
            Restrict the domain.

            INPUT:

            - ``restricted_domain`` -- a
              :class:`~sage.sets.real_set.RealSet` or something that
              defines one.

            OUTPUT: a new piecewise function obtained by restricting the domain

            EXAMPLES::

                sage: f = piecewise([((-oo, oo), x)]);  f
                piecewise(x|-->x on (-oo, +oo); x)
                sage: f.restriction([[-1,1], [3,3]])
                piecewise(x|-->x on [-1, 1] ∪ {3}; x)
            """
        def extension(self, parameters, variable, extension, extension_domain=None):
            """
            Extend the function.

            INPUT:

            - ``extension`` -- a symbolic expression

            - ``extension_domain`` -- a
              :class:`~sage.sets.real_set.RealSet` or ``None``
              (default). The domain of the extension. By default, the
              entire complement of the current domain.

            EXAMPLES::

                sage: f = piecewise([((-1,1), x)]);  f
                piecewise(x|-->x on (-1, 1); x)
                sage: f(3)
                Traceback (most recent call last):
                ...
                ValueError: point 3 is not in the domain

                sage: g = f.extension(0);  g
                piecewise(x|-->x on (-1, 1), x|-->0 on (-oo, -1] ∪ [1, +oo); x)
                sage: g(3)
                0

                sage: h = f.extension(1, RealSet.unbounded_above_closed(1));  h
                piecewise(x|-->x on (-1, 1), x|-->1 on [1, +oo); x)
                sage: h(3)
                1
            """
        def unextend_zero(self, parameters, variable):
            """
            Remove zero pieces.

            EXAMPLES::

                sage: f = piecewise([((-1,1), x)]);  f
                piecewise(x|-->x on (-1, 1); x)
                sage: g = f.extension(0);  g
                piecewise(x|-->x on (-1, 1), x|-->0 on (-oo, -1] ∪ [1, +oo); x)
                sage: g(3)
                0
                sage: h = g.unextend_zero()
                sage: bool(h == f)
                True
            """
        def pieces(self, parameters, variable):
            '''
            Return the "pieces".

            OUTPUT:

            A tuple of piecewise functions, each having only a single
            expression.

            EXAMPLES::

                sage: p = piecewise([((-1, 0), -x), ([0, 1], x)], var=x)
                sage: p.pieces()
                (piecewise(x|-->-x on (-1, 0); x),
                 piecewise(x|-->x on [0, 1]; x))
            '''
        def end_points(self, parameters, variable) -> list:
            """
            Return a list of all interval endpoints for this function.

            EXAMPLES::

                sage: f1(x) = 1
                sage: f2(x) = 1 - x
                sage: f3(x) = x^2 - 5
                sage: f = piecewise([[(0,1), f1], [(1,2), f2], [(2,3), f3]])
                sage: f.end_points()
                [0, 1, 2, 3]
                sage: f = piecewise([([0,0], sin(x)), ((0,2), cos(x))]);  f
                piecewise(x|-->sin(x) on {0}, x|-->cos(x) on (0, 2); x)
                sage: f.end_points()
                [0, 2]
            """
        def piecewise_add(self, parameters, variable, other):
            """
            Return a new piecewise function with domain the union
            of the original domains and functions summed. Undefined
            intervals in the union domain get function value `0`.

            EXAMPLES::

                sage: f = piecewise([([0,1], 1), ((2,3), x)])
                sage: g = piecewise([((1/2, 2), x)])
                sage: f.piecewise_add(g).unextend_zero()
                piecewise(x|-->1 on (0, 1/2],
                          x|-->x + 1 on (1/2, 1],
                          x|-->x on (1, 2) ∪ (2, 3); x)
            """
        def integral(self, parameters, variable, x=None, a=None, b=None, definite: bool = False, **kwds):
            """
            By default, return the indefinite integral of the function.

            If ``definite=True`` is given, returns the definite integral.

            AUTHOR:

            - Paul Butler

            EXAMPLES::

                sage: f1(x) = 1 - x
                sage: f = piecewise([((0,1), 1), ((1,2), f1)])
                sage: f.integral(definite=True)
                1/2

            ::

                sage: f1(x) = -1
                sage: f2(x) = 2
                sage: f = piecewise([((0,pi/2), f1), ((pi/2,pi), f2)])
                sage: f.integral(definite=True)
                1/2*pi

                sage: f1(x) = 2
                sage: f2(x) = 3 - x
                sage: f = piecewise([[(-2, 0), f1], [(0, 3), f2]])
                sage: f.integral()
                piecewise(x|-->2*x + 4 on (-2, 0),
                          x|-->-1/2*x^2 + 3*x + 4 on (0, 3); x)

                sage: f1(y) = -1
                sage: f2(y) = y + 3
                sage: f3(y) = -y - 1
                sage: f4(y) = y^2 - 1
                sage: f5(y) = 3
                sage: f = piecewise([[[-4,-3], f1], [(-3,-2), f2], [[-2,0], f3],
                ....:                [(0,2), f4], [[2,3], f5]])
                sage: F = f.integral(y); F
                piecewise(y|-->-y - 4 on [-4, -3],
                          y|-->1/2*y^2 + 3*y + 7/2 on (-3, -2),
                          y|-->-1/2*y^2 - y - 1/2 on [-2, 0],
                          y|-->1/3*y^3 - y - 1/2 on (0, 2),
                          y|-->3*y - 35/6 on [2, 3]; y)

            Ensure results are consistent with FTC::

                sage: F(-3) - F(-4)
                -1
                sage: F(-1) - F(-3)
                1
                sage: F(2) - F(0)
                2/3
                sage: f.integral(y, 0, 2)
                2/3
                sage: F(3) - F(-4)
                19/6
                sage: f.integral(y, -4, 3)
                19/6
                sage: f.integral(definite=True)
                19/6

            ::

                sage: f1(y) = (y+3)^2
                sage: f2(y) = y+3
                sage: f3(y) = 3
                sage: f = piecewise([[(-infinity, -3), f1], [(-3, 0), f2],
                ....:                [(0, infinity), f3]])
                sage: f.integral()
                piecewise(y|-->1/3*y^3 + 3*y^2 + 9*y + 9 on (-oo, -3),
                          y|-->1/2*y^2 + 3*y + 9/2 on (-3, 0),
                          y|-->3*y + 9/2 on (0, +oo); y)

            ::

                sage: f1(x) = e^(-abs(x))
                sage: f = piecewise([[(-infinity, infinity), f1]])
                sage: result = f.integral(definite=True)
                ...
                sage: result
                2
                sage: f.integral()
                piecewise(x|-->-integrate(e^(-abs(x)), x, x, +Infinity) on (-oo, +oo); x)

            ::

                sage: f = piecewise([((0, 5), cos(x))])
                sage: f.integral()
                piecewise(x|-->sin(x) on (0, 5); x)

            TESTS:

            Verify that piecewise integrals of zero work (:issue:`10841`)::

                sage: f0(x) = 0
                sage: f = piecewise([[[0,1], f0]])
                sage: f.integral(x,0,1)
                0
                sage: f = piecewise([[[0,1], 0]])
                sage: f.integral(x,0,1)
                0
                sage: f = piecewise([[[0,1], SR(0)]])
                sage: f.integral(x,0,1)
                0

            Check that the algorithm keyword can be used::

                sage: # needs sage.libs.giac
                sage: ex = piecewise([([0, 1], 1), ((1, oo), 1/x**2)])
                sage: integral(ex, x, 0, 100, algorithm='sympy')
                199/100
                sage: integral(ex, x, algorithm='sympy')
                piecewise(x|-->x on [0, 1], x|-->-1/x + 2 on (1, +oo); x)
            """
        def critical_points(self, parameters, variable):
            """
            Return the critical points of this piecewise function.

            EXAMPLES::

                sage: R.<x> = QQ[]
                sage: f1 = x^0
                sage: f2 = 10*x - x^2
                sage: f3 = 3*x^4 - 156*x^3 + 3036*x^2 - 26208*x
                sage: f = piecewise([[(0,3), f1], [(3,10), f2], [(10,20), f3]])
                sage: expected = [5, 12, 13, 14]
                sage: all(abs(e-a) < 0.001 for e,a in zip(expected, f.critical_points()))
                True

            TESTS:

            Use variables other than x (:issue:`13836`)::

                sage: R.<y> = QQ[]
                sage: f1 = y^0
                sage: f2 = 10*y - y^2
                sage: f3 = 3*y^4 - 156*y^3 + 3036*y^2 - 26208*y
                sage: f = piecewise([[(0,3), f1], [(3,10), f2], [(10,20), f3]])
                sage: expected = [5, 12, 13, 14]
                sage: all(abs(e-a) < 0.001 for e,a in zip(expected, f.critical_points()))
                True
            """
        def convolution(self, parameters, variable, other):
            """
            Return the convolution function,
            `f*g(t)=\\int_{-\\infty}^\\infty f(u)g(t-u)du`, for compactly
            supported `f,g`.

            EXAMPLES::

                sage: x = PolynomialRing(QQ, 'x').gen()

            Example 0::

                sage: f = piecewise([[[0,1], 1]])
                sage: g = f.convolution(f); g
                piecewise(x|-->x on (0, 1],
                          x|-->-x + 2 on (1, 2]; x)
                sage: h = f.convolution(g); h
                piecewise(x|-->1/2*x^2 on (0, 1],
                          x|-->-x^2 + 3*x - 3/2 on (1, 2],
                          x|-->1/2*x^2 - 3*x + 9/2 on (2, 3]; x)

            Example 1::

                sage: f = piecewise([[(0,1), 1], [(1,2), 2], [(2,3), 1]])
                sage: g = f.convolution(f)
                sage: h = f.convolution(g); h
                piecewise(x|-->1/2*x^2 on (0, 1],
                          x|-->2*x^2 - 3*x + 3/2 on (1, 3],
                          x|-->-2*x^2 + 21*x - 69/2 on (3, 4],
                          x|-->-5*x^2 + 45*x - 165/2 on (4, 5],
                          x|-->-2*x^2 + 15*x - 15/2 on (5, 6],
                          x|-->2*x^2 - 33*x + 273/2 on (6, 8],
                          x|-->1/2*x^2 - 9*x + 81/2 on (8, 9]; x)

            Example 2::

                sage: f = piecewise([[(-1,1), 1]])
                sage: g = piecewise([[(0,3), x]])
                sage: f.convolution(g)
                piecewise(x|-->1/2*x^2 + x + 1/2 on (-1, 1],
                          x|-->2*x on (1, 2],
                          x|-->-1/2*x^2 + x + 4 on (2, 4]; x)
                sage: g = piecewise([[(0,3), 1], [(3,4), 2]])
                sage: f.convolution(g)
                piecewise(x|-->x + 1 on (-1, 1],
                          x|-->2 on (1, 2],
                          x|-->x on (2, 3],
                          x|-->-x + 6 on (3, 4],
                          x|-->-2*x + 10 on (4, 5]; x)

            Some unbounded but convergent cases now work::

                sage: p = piecewise([[(2,oo),exp(-x)]])
                sage: q = piecewise([[[2,3],x]])
                sage: p.convolution(q)
                piecewise(x|-->(x - 3)*e^(-2) - e^(-x + 2) on (4, 5]; x)
                sage: q.convolution(p)
                piecewise(x|-->(x - 3)*e^(-2) - e^(-x + 2) on (4, 5]; x)

            TESTS:

            Check that the bugs raised in :issue:`12123` are fixed::

                sage: f = piecewise([[(-2, 2), 2]])
                sage: g = piecewise([[(0, 2), 3/4]])
                sage: f.convolution(g)
                piecewise(x|-->3/2*x + 3 on (-2, 0],
                          x|-->3 on (0, 2],
                          x|-->-3/2*x + 6 on (2, 4]; x)
                sage: f = piecewise([[(-1, 1), 1]])
                sage: g = piecewise([[(0, 1), x], [(1, 2), -x + 2]])
                sage: f.convolution(g)
                piecewise(x|-->1/2*x^2 + x + 1/2 on (-1, 0],
                          x|-->-1/2*x^2 + x + 1/2 on (0, 2],
                          x|-->1/2*x^2 - 3*x + 9/2 on (2, 3]; x)
            """
        def trapezoid(self, parameters, variable, N):
            """
            Return the piecewise line function defined by the trapezoid rule
            for numerical integration based on a subdivision of each domain
            interval into N subintervals.

            EXAMPLES::

                sage: f = piecewise([[[0,1], x^2],
                ....:                [RealSet.open_closed(1,2), 5 - x^2]])
                sage: f.trapezoid(2)
                piecewise(x|-->1/2*x on (0, 1/2),
                          x|-->3/2*x - 1/2 on (1/2, 1),
                          x|-->7/2*x - 5/2 on (1, 3/2),
                          x|-->-7/2*x + 8 on (3/2, 2); x)
                sage: f = piecewise([[[-1,1], 1 - x^2]])
                sage: f.trapezoid(4).integral(definite=True)
                5/4
                sage: f = piecewise([[[-1,1], 1/2 + x - x^3]])          ## example 3
                sage: f.trapezoid(6).integral(definite=True)
                1

            TESTS:

            Use variables or rings other than x (:issue:`13836`)::

                sage: R.<y> = QQ[]
                sage: f1 = y^2
                sage: f2 = 5 - y^2
                sage: f = piecewise([[[0,1], f1], [RealSet.open_closed(1,2), f2]])
                sage: f.trapezoid(2)
                piecewise(y|-->1/2*y on (0, 1/2),
                          y|-->3/2*y - 1/2 on (1/2, 1),
                          y|-->7/2*y - 5/2 on (1, 3/2),
                          y|-->-7/2*y + 8 on (3/2, 2); y)
            """
        def laplace(self, parameters, variable, x: str = 'x', s: str = 't'):
            """
            Return the Laplace transform of ``self`` with respect to the variable
            var.

            INPUT:

            - ``x`` -- variable of ``self``

            - ``s`` -- variable of Laplace transform

            We assume that a piecewise function is 0 outside of its domain and
            that the left-most endpoint of the domain is 0.

            EXAMPLES::

                sage: x, s, w = var('x, s, w')
                sage: f = piecewise([[(0,1), 1], [[1,2], 1 - x]])
                sage: f.laplace(x, s)
                -e^(-s)/s + (s + 1)*e^(-2*s)/s^2 + 1/s - e^(-s)/s^2
                sage: f.laplace(x, w)
                -e^(-w)/w + (w + 1)*e^(-2*w)/w^2 + 1/w - e^(-w)/w^2

            ::

                sage: y, t = var('y, t')
                sage: f = piecewise([[[1,2], 1 - y]])
                sage: f.laplace(y, t)
                (t + 1)*e^(-2*t)/t^2 - e^(-t)/t^2

            ::

                sage: s = var('s')
                sage: t = var('t')
                sage: f1(t) = -t
                sage: f2(t) = 2
                sage: f = piecewise([[[0,1], f1], [(1,infinity), f2]])
                sage: f.laplace(t, s)
                (s + 1)*e^(-s)/s^2 + 2*e^(-s)/s - 1/s^2
            """
        def fourier_series_cosine_coefficient(self, parameters, variable, n, L=None):
            """
            Return the `n`-th cosine coefficient of the Fourier series of
            the periodic function `f` extending the piecewise-defined
            function ``self``.

            Given an integer `n\\geq 0`, the `n`-th cosine coefficient of
            the Fourier series of `f` is defined by

            .. MATH::

                a_n = \\frac{1}{L}\\int_{-L}^L
                        f(x)\\cos\\left(\\frac{n\\pi x}{L}\\right) dx,

            where `L` is the half-period of `f`. For `n\\geq 1`, `a_n` is
            the coefficient of `\\cos(n\\pi x/L)` in the Fourier series of
            `f`, while `a_0` is twice the coefficient of the constant
            term `\\cos(0 x)`, i.e. twice the mean value of `f` over one
            period (cf. :meth:`fourier_series_partial_sum`).

            INPUT:

            - ``n`` -- nonnegative integer

            - ``L`` -- (default: ``None``) the half-period of `f`; if none
              is provided, `L` is assumed to be the half-width of the domain
              of ``self``

            OUTPUT: the Fourier coefficient `a_n`, as defined above

            EXAMPLES:

            A triangle wave function of period 2::

                sage: f = piecewise([((0,1), x), ((1,2), 2 - x)])
                sage: f.fourier_series_cosine_coefficient(0)
                1
                sage: f.fourier_series_cosine_coefficient(3)
                -4/9/pi^2

            If the domain of the piecewise-defined function encompasses
            more than one period, the half-period must be passed as the
            second argument; for instance::

                sage: f2 = piecewise([((0,1), x), ((1,2), 2 - x),
                ....:                 ((2,3), x - 2), ((3,4), 2 - (x-2))])
                sage: bool(f2.restriction((0,2)) == f)  # f2 extends f on (0,4)
                True
                sage: f2.fourier_series_cosine_coefficient(3, 1)  # half-period = 1
                -4/9/pi^2

            The default half-period is 2 and one has::

                sage: f2.fourier_series_cosine_coefficient(3)     # half-period = 2
                0

            The Fourier coefficient `-4/(9\\pi^2)` obtained above is actually
            recovered for `n=6`::

                sage: f2.fourier_series_cosine_coefficient(6)
                -4/9/pi^2

            Other examples::

                sage: f(x) = x^2
                sage: f = piecewise([[(-1,1), f]])
                sage: f.fourier_series_cosine_coefficient(2)
                pi^(-2)
                sage: f1(x) = -1
                sage: f2(x) = 2
                sage: f = piecewise([[(-pi, pi/2), f1], [(pi/2, pi), f2]])
                sage: f.fourier_series_cosine_coefficient(5, pi)
                -3/5/pi
            """
        def fourier_series_sine_coefficient(self, parameters, variable, n, L=None):
            """
            Return the `n`-th sine coefficient of the Fourier series of
            the periodic function `f` extending the piecewise-defined
            function ``self``.

            Given an integer `n\\geq 0`, the `n`-th sine coefficient of
            the Fourier series of `f` is defined by

            .. MATH::

                b_n = \\frac{1}{L}\\int_{-L}^L
                        f(x)\\sin\\left(\\frac{n\\pi x}{L}\\right) dx,

            where `L` is the half-period of `f`. The number `b_n` is
            the coefficient of `\\sin(n\\pi x/L)` in the Fourier
            series of `f` (cf. :meth:`fourier_series_partial_sum`).

            INPUT:

            - ``n`` -- nonnegative integer

            - ``L`` -- (default: ``None``) the half-period of `f`; if none
              is provided, `L` is assumed to be the half-width of the domain
              of ``self``

            OUTPUT: the Fourier coefficient `b_n`, as defined above

            EXAMPLES:

            A square wave function of period 2::

                sage: f = piecewise([((-1,0), -1), ((0,1), 1)])
                sage: f.fourier_series_sine_coefficient(1)
                4/pi
                sage: f.fourier_series_sine_coefficient(2)
                0
                sage: f.fourier_series_sine_coefficient(3)
                4/3/pi

            If the domain of the piecewise-defined function encompasses
            more than one period, the half-period must be passed as the
            second argument; for instance::

                sage: f2 = piecewise([((-1,0), -1), ((0,1), 1),
                ....:                 ((1,2), -1), ((2,3), 1)])
                sage: bool(f2.restriction((-1,1)) == f)  # f2 extends f on (-1,3)
                True
                sage: f2.fourier_series_sine_coefficient(1, 1)  # half-period = 1
                4/pi
                sage: f2.fourier_series_sine_coefficient(3, 1)  # half-period = 1
                4/3/pi

            The default half-period is 2 and one has::

                sage: f2.fourier_series_sine_coefficient(1)  # half-period = 2
                0
                sage: f2.fourier_series_sine_coefficient(3)  # half-period = 2
                0

            The Fourier coefficients obtained from ``f`` are actually
            recovered for `n=2` and `n=6` respectively::

                sage: f2.fourier_series_sine_coefficient(2)
                4/pi
                sage: f2.fourier_series_sine_coefficient(6)
                4/3/pi
            """
        def fourier_series_partial_sum(self, parameters, variable, N, L=None):
            """
            Return the partial sum up to a given order of the Fourier series
            of the periodic function `f` extending the piecewise-defined
            function ``self``.

            The Fourier partial sum of order `N` is defined as

            .. MATH::

                S_{N}(x) = \\frac{a_0}{2} + \\sum_{n=1}^{N} \\left[
                      a_n\\cos\\left(\\frac{n\\pi x}{L}\\right)
                    + b_n\\sin\\left(\\frac{n\\pi x}{L}\\right)\\right],

            where `L` is the half-period of `f` and the `a_n`'s and `b_n`'s
            are respectively the cosine coefficients and sine coefficients
            of the Fourier series of `f` (cf.
            :meth:`fourier_series_cosine_coefficient` and
            :meth:`fourier_series_sine_coefficient`).

            INPUT:

            - ``N`` -- positive integer; the order of the partial sum

            - ``L`` -- (default: ``None``) the half-period of `f`; if none
              is provided, `L` is assumed to be the half-width of the domain
              of ``self``

            OUTPUT:

            - the partial sum `S_{N}(x)`, as a symbolic expression

            EXAMPLES:

            A square wave function of period 2::

                sage: f = piecewise([((-1,0), -1), ((0,1), 1)])
                sage: f.fourier_series_partial_sum(5)
                4/5*sin(5*pi*x)/pi + 4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi

            If the domain of the piecewise-defined function encompasses
            more than one period, the half-period must be passed as the
            second argument; for instance::

                sage: f2 = piecewise([((-1,0), -1), ((0,1), 1),
                ....:                 ((1,2), -1), ((2,3), 1)])
                sage: bool(f2.restriction((-1,1)) == f)  # f2 extends f on (-1,3)
                True
                sage: f2.fourier_series_partial_sum(5, 1)  # half-period = 1
                4/5*sin(5*pi*x)/pi + 4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi
                sage: bool(f2.fourier_series_partial_sum(5, 1) ==
                ....:      f.fourier_series_partial_sum(5))
                True

            The default half-period is 2, so that skipping the second
            argument yields a different result::

                sage: f2.fourier_series_partial_sum(5)  # half-period = 2
                4*sin(pi*x)/pi

            An example of partial sum involving both cosine and sine terms::

                sage: f = piecewise([((-1,0), 0), ((0,1/2), 2*x),
                ....:                ((1/2,1), 2*(1-x))])
                sage: f.fourier_series_partial_sum(5)
                -2*cos(2*pi*x)/pi^2 + 4/25*sin(5*pi*x)/pi^2
                 - 4/9*sin(3*pi*x)/pi^2 + 4*sin(pi*x)/pi^2 + 1/4
            """

piecewise: PiecewiseFunction
