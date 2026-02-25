from _typeshed import Incomplete
from typing import Any, Literal, overload
from sage.arith.misc import algebraic_dependency as algebraic_dependency
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.parser import LookupNameMaker as LookupNameMaker, Parser as Parser
from sage.rings.cc import CC as CC
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RealDoubleElement as RealDoubleElement
from sage.rings.real_mpfr import RR as RR, create_RealNumber as create_RealNumber
from sage.structure.element import Expression as Expression
from sage.symbolic.function import Function as Function
from sage.symbolic.function_factory import function_factory as function_factory
from sage.symbolic.integration.integral import definite_integral as definite_integral, indefinite_integral as indefinite_integral
from sage.symbolic.ring import SR as SR, SymbolicRing, var as var
from sage.symbolic.symbols import symbol_table as symbol_table
import sage.interfaces.maxima_lib

from typings_sagemath import CoercibleToExpression, FloatingSage
maxima = sage.interfaces.maxima_lib

@overload
def symbolic_sum(
    expression: CoercibleToExpression, v: str | Expression[SymbolicRing], 
    a, b,  
    algorithm: Literal["maxima", "maple", "mathematica", "giac", "sympy"] = "maxima"
) -> Expression[SymbolicRing] | Integer | FloatingSage | Any: ...
@overload
def symbolic_sum(
    expression: CoercibleToExpression, v: str | Expression[SymbolicRing], 
    a, b, 
    algorithm: Literal["maxima", "maple", "mathematica", "giac", "sympy"], 
    hold: Literal[True]
) -> Expression[SymbolicRing]: ...
@overload
def symbolic_sum(
    expression: CoercibleToExpression, v: str | Expression[SymbolicRing], 
    a, b, 
    algorithm: Literal["maxima", "maple", "mathematica", "giac", "sympy"] = "maxima", 
    *, hold: Literal[True]
) -> Expression[SymbolicRing]:
    """
    Return the symbolic sum `\\sum_{v = a}^b expression` with respect
    to the variable `v` with endpoints `a` and `b`.

    INPUT:

    - ``expression`` -- a symbolic expression

    - ``v`` -- a variable or variable name

    - ``a`` -- lower endpoint of the sum

    - ``b`` -- upper endpoint of the sum

    - ``algorithm`` -- (default: ``'maxima'``)  one of

      - ``'maxima'`` -- use Maxima (the default)

      - ``'maple'`` -- (optional) use Maple

      - ``'mathematica'`` -- (optional) use Mathematica

      - ``'giac'`` -- (optional) use Giac

      - ``'sympy'`` -- use SymPy

    - ``hold`` -- boolean (default: ``False``); if ``True``, don't evaluate

    EXAMPLES::

        sage: k, n = var('k,n')
        sage: from sage.calculus.calculus import symbolic_sum
        sage: symbolic_sum(k, k, 1, n).factor()
        1/2*(n + 1)*n

    ::

        sage: symbolic_sum(1/k^4, k, 1, oo)
        1/90*pi^4

    ::

        sage: symbolic_sum(1/k^5, k, 1, oo)
        zeta(5)

    A well known binomial identity::

        sage: symbolic_sum(binomial(n,k), k, 0, n)
        2^n

    And some truncations thereof::

        sage: assume(n>1)
        sage: symbolic_sum(binomial(n,k), k, 1, n)
        2^n - 1
        sage: symbolic_sum(binomial(n,k), k, 2, n)
        2^n - n - 1
        sage: symbolic_sum(binomial(n,k), k, 0, n-1)
        2^n - 1
        sage: symbolic_sum(binomial(n,k), k, 1, n-1)
        2^n - 2

    The binomial theorem::

        sage: x, y = var('x, y')
        sage: symbolic_sum(binomial(n,k) * x^k * y^(n-k), k, 0, n)
        (x + y)^n

    ::

        sage: symbolic_sum(k * binomial(n, k), k, 1, n)
        2^(n - 1)*n

    ::

        sage: symbolic_sum((-1)^k*binomial(n,k), k, 0, n)
        0

    ::

        sage: symbolic_sum(2^(-k)/(k*(k+1)), k, 1, oo)
        -log(2) + 1

    Summing a hypergeometric term::

        sage: symbolic_sum(binomial(n, k) * factorial(k) / factorial(n+1+k), k, 0, n)
        1/2*sqrt(pi)/factorial(n + 1/2)

    We check a well known identity::

        sage: bool(symbolic_sum(k^3, k, 1, n) == symbolic_sum(k, k, 1, n)^2)
        True

    A geometric sum::

        sage: a, q = var('a, q')
        sage: symbolic_sum(a*q^k, k, 0, n)
        (a*q^(n + 1) - a)/(q - 1)

    For the geometric series, we will have to assume
    the right values for the sum to converge::

        sage: assume(abs(q) < 1)
        sage: symbolic_sum(a*q^k, k, 0, oo)
        -a/(q - 1)

    A divergent geometric series.  Don't forget
    to forget your assumptions::

        sage: forget()
        sage: assume(q > 1)
        sage: symbolic_sum(a*q^k, k, 0, oo)
        Traceback (most recent call last):
        ...
        ValueError: Sum is divergent.
        sage: forget()
        sage: assumptions()  # check the assumptions were really forgotten
        []

    A summation performed by Mathematica::

        sage: symbolic_sum(1/(1+k^2), k, -oo, oo, algorithm='mathematica')     # optional - mathematica
        pi*coth(pi)

    An example of this summation with Giac::

        sage: # needs giac
        sage: symbolic_sum(1/(1+k^2), k, -oo, oo, algorithm='giac').factor()
        pi*(e^(2*pi) + 1)/((e^pi + 1)*(e^pi - 1))

    The same summation is solved by SymPy::

        sage: symbolic_sum(1/(1+k^2), k, -oo, oo, algorithm='sympy')
        pi/tanh(pi)

    SymPy and Maxima 5.39.0 can do the following (see
    :issue:`22005`)::

        sage: sum(1/((2*n+1)^2-4)^2, n, 0, Infinity, algorithm='sympy')
        1/64*pi^2
        sage: sum(1/((2*n+1)^2-4)^2, n, 0, Infinity)
        1/64*pi^2

    Use Maple as a backend for summation::

        sage: symbolic_sum(binomial(n,k)*x^k, k, 0, n, algorithm='maple')      # optional - maple
        (x + 1)^n

    If you don't want to evaluate immediately give the ``hold`` keyword::

        sage: s = sum(n, n, 1, k, hold=True); s
        sum(n, n, 1, k)
        sage: s.unhold()
        1/2*k^2 + 1/2*k
        sage: s.subs(k == 10)
        sum(n, n, 1, 10)
        sage: s.subs(k == 10).unhold()
        55
        sage: s.subs(k == 10).n()
        55.0000000000000

    TESTS:

    :issue:`10564` is fixed::

        sage: sum (n^3 * x^n, n, 0, infinity)
        (x^3 + 4*x^2 + x)/(x^4 - 4*x^3 + 6*x^2 - 4*x + 1)

    .. NOTE::

       Sage can currently only understand a subset of the output of Maxima,
       Maple and Mathematica, so even if the chosen backend can perform
       the summation the result might not be convertible into a Sage
       expression.
    """
def nintegral(ex, x, a, b, desired_relative_error: str = '1e-8', maximum_num_subintervals: int = 200):
    """
    Return a floating point machine precision numerical approximation
    to the integral of ``self`` from `a` to
    `b`, computed using floating point arithmetic via maxima.

    INPUT:

    - ``x`` -- variable to integrate with respect to

    - ``a`` -- lower endpoint of integration

    - ``b`` -- upper endpoint of integration

    - ``desired_relative_error`` -- (default: ``1e-8``) the
      desired relative error

    - ``maximum_num_subintervals`` -- (default: 200)
      maximal number of subintervals

    OUTPUT: float; approximation to the integral

    - float: estimated absolute error of the
      approximation

    - the number of integrand evaluations

    - an error code:

      - ``0`` -- no problems were encountered

      - ``1`` -- too many subintervals were done

      - ``2`` -- excessive roundoff error

      - ``3`` -- extremely bad integrand behavior

      - ``4`` -- failed to converge

      - ``5`` -- integral is probably divergent or slowly
        convergent

      - ``6`` -- the input is invalid; this includes the case of
        ``desired_relative_error`` being too small to be achieved

    ALIAS: :func:`nintegrate` is the same as :func:`nintegral`

    REMARK: There is also a function
    :func:`numerical_integral` that implements numerical
    integration using the GSL C library. It is potentially much faster
    and applies to arbitrary user defined functions.

    Also, there are limits to the precision to which Maxima can compute
    the integral due to limitations in quadpack.
    In the following example, remark that the last value of the returned
    tuple is ``6``, indicating that the input was invalid, in this case
    because of a too high desired precision.

    ::

        sage: f = x
        sage: f.nintegral(x, 0, 1, 1e-14)
        (0.0, 0.0, 0, 6)

    EXAMPLES::

        sage: f(x) = exp(-sqrt(x))
        sage: f.nintegral(x, 0, 1)
        (0.5284822353142306, 4.163...e-11, 231, 0)

    We can also use the :func:`numerical_integral` function,
    which calls the GSL C library.

    ::

        sage: numerical_integral(f, 0, 1)
        (0.528482232253147, 6.83928460...e-07)

    Note that in exotic cases where floating point evaluation of the
    expression leads to the wrong value, then the output can be
    completely wrong::

        sage: f = exp(pi*sqrt(163)) - 262537412640768744

    Despite appearance, `f` is really very close to 0, but one
    gets a nonzero value since the definition of
    ``float(f)`` is that it makes all constants inside the
    expression floats, then evaluates each function and each arithmetic
    operation using float arithmetic::

        sage: float(f)
        -480.0

    Computing to higher precision we see the truth::

        sage: f.n(200)
        -7.4992740280181431112064614366622348652078895136533593355718e-13
        sage: f.n(300)
        -7.49927402801814311120646143662663009137292462589621789352095066181709095575681963967103004e-13

    Now numerically integrating, we see why the answer is wrong::

        sage: f.nintegrate(x,0,1)
        (-480.000000000000..., 5.32907051820075...e-12, 21, 0)

    It is just because every floating point evaluation of `f` returns `-480.0`
    in floating point.

    Important note: using PARI/GP one can compute numerical integrals
    to high precision::

        sage: gp.eval('intnum(x=17,42,exp(-x^2)*log(x))')
        '2.5657285005610514829176211363206621657 E-127'
        sage: old_prec = gp.set_real_precision(50)
        sage: gp.eval('intnum(x=17,42,exp(-x^2)*log(x))')
        '2.5657285005610514829173563961304957417746108003917 E-127'
        sage: gp.set_real_precision(old_prec)
        57

    Note that the input function above is a string in PARI syntax.
    """
nintegrate = nintegral

@overload
def symbolic_prod(
    expression: CoercibleToExpression, v: str | Expression[SymbolicRing],
    a, b, algorithm: Literal["maxima", "mathematica", "giac", "sympy"] = "maxima"
) -> Expression[SymbolicRing] | Integer | FloatingSage | Any: ...
@overload
def symbolic_prod(
    expression: CoercibleToExpression, v: str | Expression[SymbolicRing],
    a, b, algorithm: Literal["maxima", "mathematica", "giac", "sympy"],
    hold: Literal[True]
) -> Expression[SymbolicRing]: ...
@overload
def symbolic_prod(
    expression: CoercibleToExpression, v: str | Expression[SymbolicRing],
    a, b, algorithm: Literal["maxima", "mathematica", "giac", "sympy"] = "maxima",
    *, hold: Literal[True]
) -> Expression[SymbolicRing]:
    """
    Return the symbolic product `\\prod_{v = a}^b expression` with respect
    to the variable `v` with endpoints `a` and `b`.

    INPUT:

    - ``expression`` -- a symbolic expression

    - ``v`` -- a variable or variable name

    - ``a`` -- lower endpoint of the product

    - ``b`` -- upper endpoint of the prduct

    - ``algorithm`` -- (default: ``'maxima'``)  one of

      - ``'maxima'`` -- use Maxima (the default)

      - ``'giac'`` -- use Giac (optional)

      - ``'sympy'`` -- use SymPy

      - ``'mathematica'`` -- (optional) use Mathematica

    - ``hold`` -- boolean (default: ``False``); if ``True``, don't evaluate

    EXAMPLES::

        sage: i, k, n = var('i,k,n')
        sage: from sage.calculus.calculus import symbolic_product
        sage: symbolic_product(k, k, 1, n)
        factorial(n)
        sage: symbolic_product(x + i*(i+1)/2, i, 1, 4)
        x^4 + 20*x^3 + 127*x^2 + 288*x + 180
        sage: symbolic_product(i^2, i, 1, 7)
        25401600
        sage: f = function('f')
        sage: symbolic_product(f(i), i, 1, 7)
        f(7)*f(6)*f(5)*f(4)*f(3)*f(2)*f(1)
        sage: symbolic_product(f(i), i, 1, n)
        product(f(i), i, 1, n)
        sage: assume(k>0)
        sage: symbolic_product(integrate (x^k, x, 0, 1), k, 1, n)
        1/factorial(n + 1)
        sage: symbolic_product(f(i), i, 1, n).log().log_expand()
        sum(log(f(i)), i, 1, n)

    TESTS:

    Verify that :issue:`30520` is fixed::

        sage: symbolic_product(-x^2,x,1,n)
        (-1)^n*factorial(n)^2
    """
def minpoly(ex, var: str = 'x', algorithm=None, bits=None, degree=None, epsilon: int = 0):
    """
    Return the minimal polynomial of ``self``, if possible.

    INPUT:

    - ``var`` -- polynomial variable name (default: ``'x'``)

    - ``algorithm`` -- ``'algebraic'`` or ``'numerical'`` (default
      both, but with numerical first)

    - ``bits`` -- the number of bits to use in numerical
      approx

    - ``degree`` -- the expected algebraic degree

    - ``epsilon`` -- return without error as long as
      f(self) epsilon, in the case that the result cannot be proven

      All of the above parameters are optional, with epsilon=0, ``bits`` and
      ``degree`` tested up to 1000 and 24 by default respectively. The
      numerical algorithm will be faster if bits and/or degree are given
      explicitly. The algebraic algorithm ignores the last three
      parameters.

    OUTPUT: the minimal polynomial of ``self``. If the numerical algorithm
    is used, then it is proved symbolically when ``epsilon=0`` (default).

    If the minimal polynomial could not be found, two distinct kinds of
    errors are raised. If no reasonable candidate was found with the
    given ``bits``/``degree`` parameters, a :exc:`ValueError` will be
    raised. If a reasonable candidate was found but (perhaps due to
    limits in the underlying symbolic package) was unable to be proved
    correct, a :exc:`NotImplementedError` will be raised.

    ALGORITHM: Two distinct algorithms are used, depending on the
    algorithm parameter. By default, the numerical algorithm is
    attempted first, then the algebraic one.

    Algebraic: Attempt to evaluate this expression in ``QQbar``, using
    cyclotomic fields to resolve exponential and trig functions at
    rational multiples of `\\pi`, field extensions to handle roots and
    rational exponents, and computing compositums to represent the full
    expression as an element of a number field where the minimal
    polynomial can be computed exactly. The ``bits``, ``degree``, and ``epsilon``
    parameters are ignored.

    Numerical: Computes a numerical approximation of
    ``self`` and use PARI's :pari:`algdep` to get a candidate
    minpoly `f`. If `f(\\mathtt{self})`,
    evaluated to a higher precision, is close enough to 0 then evaluate
    `f(\\mathtt{self})` symbolically, attempting to prove
    vanishing. If this fails, and ``epsilon`` is nonzero,
    return `f` if and only if
    `f(\\mathtt{self}) < \\mathtt{epsilon}`.
    Otherwise raise a :exc:`ValueError` (if no suitable
    candidate was found) or a :exc:`NotImplementedError` (if a
    likely candidate was found but could not be proved correct).

    EXAMPLES: First some simple examples::

        sage: sqrt(2).minpoly()
        x^2 - 2
        sage: minpoly(2^(1/3))
        x^3 - 2
        sage: minpoly(sqrt(2) + sqrt(-1))
        x^4 - 2*x^2 + 9
        sage: minpoly(sqrt(2)-3^(1/3))
        x^6 - 6*x^4 + 6*x^3 + 12*x^2 + 36*x + 1


    Works with trig and exponential functions too.

    ::

        sage: sin(pi/3).minpoly()
        x^2 - 3/4
        sage: sin(pi/7).minpoly()
        x^6 - 7/4*x^4 + 7/8*x^2 - 7/64
        sage: minpoly(exp(I*pi/17))
        x^16 - x^15 + x^14 - x^13 + x^12 - x^11 + x^10 - x^9 + x^8
         - x^7 + x^6 - x^5 + x^4 - x^3 + x^2 - x + 1

    Here we verify it gives the same result as the abstract number
    field.

    ::

        sage: (sqrt(2) + sqrt(3) + sqrt(6)).minpoly()
        x^4 - 22*x^2 - 48*x - 23
        sage: K.<a,b> = NumberField([x^2-2, x^2-3])
        sage: (a+b+a*b).absolute_minpoly()
        x^4 - 22*x^2 - 48*x - 23

    The :func:`minpoly` function is used implicitly when creating
    number fields::

        sage: x = var('x')
        sage: eqn =  x^3 + sqrt(2)*x + 5 == 0
        sage: a = solve(eqn, x)[0].rhs()
        sage: QQ[a]
        Number Field in a with defining polynomial x^6 + 10*x^3 - 2*x^2 + 25
         with a = 0.7185272465828846? - 1.721353471724806?*I

    Here we solve a cubic and then recover it from its complicated
    radical expansion.

    ::

        sage: f = x^3 - x + 1
        sage: a = f.solve(x)[0].rhs(); a
        -1/2*(1/18*sqrt(23)*sqrt(3) - 1/2)^(1/3)*(I*sqrt(3) + 1)
         - 1/6*(-I*sqrt(3) + 1)/(1/18*sqrt(23)*sqrt(3) - 1/2)^(1/3)
        sage: a.minpoly()
        x^3 - x + 1

    Note that simplification may be necessary to see that the minimal
    polynomial is correct.

    ::

        sage: a = sqrt(2)+sqrt(3)+sqrt(5)
        sage: f = a.minpoly(); f
        x^8 - 40*x^6 + 352*x^4 - 960*x^2 + 576
        sage: f(a)
        (sqrt(5) + sqrt(3) + sqrt(2))^8 - 40*(sqrt(5) + sqrt(3) + sqrt(2))^6
         + 352*(sqrt(5) + sqrt(3) + sqrt(2))^4 - 960*(sqrt(5) + sqrt(3) + sqrt(2))^2
         + 576
        sage: f(a).expand()
        0

    ::

        sage: a = sin(pi/7)
        sage: f = a.minpoly(algorithm='numerical'); f
        x^6 - 7/4*x^4 + 7/8*x^2 - 7/64
        sage: f(a).horner(a).numerical_approx(100)
        0.00000000000000000000000000000

    The degree must be high enough (default tops out at 24).

    ::

        sage: a = sqrt(3) + sqrt(2)
        sage: a.minpoly(algorithm='numerical', bits=100, degree=3)
        Traceback (most recent call last):
        ...
        ValueError: Could not find minimal polynomial (100 bits, degree 3).
        sage: a.minpoly(algorithm='numerical', bits=100, degree=10)
        x^4 - 10*x^2 + 1

    ::

        sage: cos(pi/33).minpoly(algorithm='algebraic')
        x^10 + 1/2*x^9 - 5/2*x^8 - 5/4*x^7 + 17/8*x^6 + 17/16*x^5
         - 43/64*x^4 - 43/128*x^3 + 3/64*x^2 + 3/128*x + 1/1024
        sage: cos(pi/33).minpoly(algorithm='numerical')
        x^10 + 1/2*x^9 - 5/2*x^8 - 5/4*x^7 + 17/8*x^6 + 17/16*x^5
         - 43/64*x^4 - 43/128*x^3 + 3/64*x^2 + 3/128*x + 1/1024

    Sometimes it fails, as it must given that some numbers aren't algebraic::

        sage: sin(1).minpoly(algorithm='numerical')
        Traceback (most recent call last):
        ...
        ValueError: Could not find minimal polynomial (1000 bits, degree 24).

    .. NOTE::

       Of course, failure to produce a minimal polynomial does not
       necessarily indicate that this number is transcendental.
    """
def limit(ex, *args, dir=None, taylor: bool = False, algorithm: str = 'maxima', **kwargs):
    '''
    Return the limit as the variable `v` approaches `a`
    from the given direction.

    SYNTAX:

    There are two ways of invoking limit. One can write
    ``limit(expr, x=a, <keywords>)`` or ``limit(expr, x, a, <keywords>)``.
    In the first option, ``x`` must be a valid Python identifier. Its
    string representation is used to create the corresponding symbolic
    variable with respect to which to take the limit. In the second
    option, ``x`` can simply be a symbolic variable. For symbolic
    variables that do not have a string representation that is a valid
    Python identifier (for instance, if ``x`` is an indexed symbolic
    variable), the second option is required.

    INPUT:

    - ``ex`` -- the expression whose limit is computed. Must be convertible
      to a symbolic expression.
    - ``v`` -- The variable for the limit. Required for the
      ``limit(expr, v, a)`` syntax. Must be convertible to a symbolic
      variable.
    - ``a`` -- The value the variable approaches. Required for the
      ``limit(expr, v, a)`` syntax. Must be convertible to a symbolic
      expression.
    - ``dir`` -- (default: ``None``) direction for the limit:
      ``\'plus\'`` (or ``\'+\'`` or ``\'right\'`` or ``\'above\'``) for a limit from above,
      ``\'minus\'`` (or ``\'-\'`` or ``\'left\'`` or ``\'below\'``) for a limit from below.
      Omitted (``None``) implies a two-sided limit.
    - ``taylor`` -- (default: ``False``) if ``True``, use Taylor
      series via Maxima (may handle more cases but potentially less stable).
      Setting this automatically uses the ``\'maxima_taylor\'`` algorithm.
    - ``algorithm`` -- (default: ``\'maxima\'``) the backend algorithm to use.
      Options include ``\'maxima\'``, ``\'maxima_taylor\'``, ``\'sympy\'``,
      ``\'giac\'``, ``\'fricas\'``, ``\'mathematica_free\'``.
    - ``**kwargs`` -- (optional) single named parameter. Required for the
      ``limit(expr, v=a)`` syntax to specify variable and limit point.

    .. NOTE::

        The output may also use ``und`` (undefined), ``ind``
        (indefinite but bounded), and ``infinity`` (complex
        infinity).

    EXAMPLES::

        sage: x = var(\'x\')
        sage: f = (1 + 1/x)^x
        sage: limit(f, x=oo)
        e
        sage: limit(f, x, oo)
        e
        sage: f.limit(x=5)
        7776/3125
        sage: f.limit(x, 5)
        7776/3125

    The positional ``limit(expr, v, a)`` syntax is particularly useful
    when the limit variable ``v`` is an indexed variable or another
    expression that cannot be used as a keyword argument
    (fixes :issue:`38761`)::

        sage: y = var(\'y\', n=3)
        sage: g = sum(y); g
        y0 + y1 + y2
        sage: limit(g, y[1], 1)
        y0 + y2 + 1
        sage: g.limit(y[0], 5)
        y1 + y2 + 5
        sage: limit(y[0]^2 + y[1], y[0], y[2]) # Limit as y0 -> y2
        y2^2 + y1

    Directional limits work with both syntaxes::

        sage: limit(1/x, x, 0, dir=\'+\')
        +Infinity
        sage: limit(1/x, x=0, dir=\'-\')
        -Infinity
        sage: limit(exp(-1/x), x, 0, dir=\'left\')
        +Infinity

    Using different algorithms::

        sage: limit(sin(x)/x, x, 0, algorithm=\'sympy\')
        1
        sage: limit(sin(x)/x, x, 0, algorithm=\'giac\') # needs sage.libs.giac
        1
        sage: limit(x^x, x, 0, dir=\'+\', algorithm=\'fricas\') # optional - fricas
        1

    Using Taylor series (can sometimes handle more complex limits)::

        sage: limit((cos(x)-1)/x^2, x, 0, taylor=True)
        -1/2

    Error handling for incorrect syntax::

        sage: limit(sin(x)/x, x=0, y=1) # Too many keyword args
        Traceback (most recent call last):
        ...
        ValueError: multiple keyword arguments specified
        sage: limit(sin(x)/x, x, 0, y=1) # Mixed positional (v,a) and keyword variable
        Traceback (most recent call last):
        ...
        ValueError: cannot mix positional specification of limit variable and point with keyword variable arguments
        sage: limit(sin(x)/x, x) # Not enough positional args
        Traceback (most recent call last):
        ...
        ValueError: three positional arguments (expr, v, a) or one positional and one keyword argument (expr, v=a) required
        sage: limit(sin(x)/x) # No variable specified
        Traceback (most recent call last):
        ...
        ValueError: invalid limit specification
        sage: limit(sin(x)/x, x, 0, x=0) # Mixing both syntaxes
        Traceback (most recent call last):
        ...
        ValueError: cannot mix positional specification of limit variable and point with keyword variable arguments

    Domain to real, a regression in 5.46.0, see https://sf.net/p/maxima/bugs/4138 ::

        sage: maxima_calculus.eval("domain:real")
        ...
        sage: f = (1 + 1/x)^x
        sage: f.limit(x=1.2).n()
        2.06961575467...
        sage: maxima_calculus.eval("domain:complex");
        ...

    Otherwise, it works ::

        sage: f.limit(x=I, taylor=True)
        (-I + 1)^I
        sage: f(x=1.2)
        2.0696157546720...
        sage: f(x=I)
        (-I + 1)^I
        sage: CDF(f(x=I))
        2.0628722350809046 + 0.7450070621797239*I
        sage: CDF(f.limit(x=I))
        2.0628722350809046 + 0.7450070621797239*I

    Notice that Maxima may ask for more information::

        sage: var(\'a\')
        a
        sage: limit(x^a,x=0)
        Traceback (most recent call last):
        ...
        ValueError: Computation failed since Maxima requested additional
        constraints; using the \'assume\' command before evaluation
        *may* help (example of legal syntax is \'assume(a>0)\', see
        `assume?` for more details)
        Is a positive, negative or zero?

    With this example, Maxima is looking for a LOT of information::

        sage: assume(a>0)
        sage: limit(x^a,x=0)  # random - maxima 5.46.0 does not need extra assumption
        Traceback (most recent call last):
        ...
        ValueError: Computation failed since Maxima requested additional
        constraints; using the \'assume\' command before evaluation *may* help
        (example of legal syntax is \'assume(a>0)\', see `assume?` for
         more details)
        Is a an integer?
        sage: assume(a,\'integer\')
        sage: limit(x^a, x=0)  # random - maxima 5.46.0 does not need extra assumption
        Traceback (most recent call last):
        ...
        ValueError: Computation failed since Maxima requested additional
        constraints; using the \'assume\' command before evaluation *may* help
        (example of legal syntax is \'assume(a>0)\', see `assume?` for
         more details)
        Is a an even number?
        sage: assume(a, \'even\')
        sage: limit(x^a, x=0)
        0
        sage: forget()

    More examples::

        sage: limit(x*log(x), x=0, dir=\'+\')
        0
        sage: lim((x+1)^(1/x), x=0)
        e
        sage: lim(e^x/x, x=oo)
        +Infinity
        sage: lim(e^x/x, x=-oo)
        0
        sage: lim(-e^x/x, x=oo)
        -Infinity
        sage: lim((cos(x))/(x^2), x=0)
        +Infinity
        sage: lim(sqrt(x^2+1) - x, x=oo)
        0
        sage: lim(x^2/(sec(x)-1), x=0)
        2
        sage: lim(cos(x)/(cos(x)-1), x=0)
        -Infinity
        sage: lim(x*sin(1/x), x=0)
        0
        sage: limit(e^(-1/x), x=0, dir=\'right\')
        0
        sage: limit(e^(-1/x), x=0, dir=\'left\')
        +Infinity

    ::

        sage: f = log(log(x)) / log(x)
        sage: forget(); assume(x < -2); lim(f, x=0, taylor=True)
        0
        sage: forget()

    Here ind means "indefinite but bounded"::

        sage: lim(sin(1/x), x = 0)
        ind

    We can use other packages than maxima, namely "sympy", "giac", "fricas".

    With the standard package Giac::

        sage: # needs sage.libs.giac
        sage: (exp(-x)/(2+sin(x))).limit(x=oo, algorithm=\'giac\')
        0
        sage: limit(e^(-1/x), x=0, dir=\'right\', algorithm=\'giac\')
        0
        sage: limit(e^(-1/x), x=0, dir=\'left\', algorithm=\'giac\')
        +Infinity
        sage: (x / (x+2^x+cos(x))).limit(x=-infinity, algorithm=\'giac\')
        1

    With the optional package FriCAS::

        sage: (x / (x+2^x+cos(x))).limit(x=-infinity, algorithm=\'fricas\')       # optional - fricas
        1
        sage: limit(e^(-1/x), x=0, dir=\'right\', algorithm=\'fricas\')             # optional - fricas
        0
        sage: limit(e^(-1/x), x=0, dir=\'left\', algorithm=\'fricas\')              # optional - fricas
        +Infinity

    One can also call Mathematica\'s online interface::

        sage: limit(pi+log(x)/x,x=oo, algorithm=\'mathematica_free\') # optional - internet
        pi

    TESTS::

        sage: lim(x^2, x=2, dir=\'nugget\')
        Traceback (most recent call last):
        ...
        ValueError: dir must be one of None, \'plus\', \'+\', \'above\', \'right\', \'minus\', \'-\', \'below\', \'left\'

        sage: x.limit(x=3, algorithm=\'nugget\')
        Traceback (most recent call last):
        ...
        ValueError: Unknown algorithm: nugget

    We check that :issue:`3718` is fixed, so that
    Maxima gives correct limits for the floor function::

        sage: limit(floor(x), x=0, dir=\'-\')
        -1
        sage: limit(floor(x), x=0, dir=\'+\')
        0
        sage: limit(floor(x), x=0)
        ...nd

    Maxima gives the right answer here, too, showing
    that :issue:`4142` is fixed::

        sage: f = sqrt(1 - x^2)
        sage: g = diff(f, x); g
        -x/sqrt(-x^2 + 1)
        sage: limit(g, x=1, dir=\'-\')
        -Infinity

    ::

        sage: limit(1/x, x=0)
        Infinity
        sage: limit(1/x, x=0, dir=\'+\')
        +Infinity
        sage: limit(1/x, x=0, dir=\'-\')
        -Infinity

    Check that :issue:`8942` is fixed::

        sage: f(x) = (cos(pi/4 - x) - tan(x)) / (1 - sin(pi/4 + x))
        sage: limit(f(x), x=pi/4, dir=\'minus\')
        +Infinity
        sage: limit(f(x), x=pi/4, dir=\'plus\')
        -Infinity
        sage: limit(f(x), x=pi/4)
        Infinity

    Check that :issue:`12708` is fixed::

        sage: limit(tanh(x), x=0)
        0

    Check that :issue:`15386` is fixed::

        sage: n = var(\'n\')
        sage: assume(n>0)
        sage: sequence = -(3*n^2 + 1)*(-1)^n / sqrt(n^5 + 8*n^3 + 8)
        sage: limit(sequence, n=infinity)
        0
        sage: forget() # Clean up assumption

    Check if :issue:`23048` is fixed::

        sage: (1/(x-3)).limit(x=3, dir=\'below\')
        -Infinity

    From :issue:`14677`::

        sage: f = (x^x - sin(x)^sin(x)) / (x^3*log(x))
        sage: limit(f, x=0, algorithm=\'fricas\')                                 # optional - fricas
        und

        sage: limit(f, x=0, dir=\'right\', algorithm=\'fricas\')                    # optional - fricas
        1/6

    From :issue:`26497`::

        sage: mu, y, sigma = var("mu, y, sigma")
        sage: f = 1/2*sqrt(2)*e^(-1/2*(mu - log(y))^2/sigma^2)/(sqrt(pi)*sigma*y)
        sage: limit(f, y=0, algorithm=\'fricas\')                                 # optional - fricas
        0

    From :issue:`26060`::

        sage: limit(x / (x + 2^x + cos(x)), x=-infinity)
        1

    # Added specific tests for argument parsing logic to ensure coverage
    sage: limit(x+1, x=1)
    2
    sage: limit(x+1, x, 1)
    2
    sage: limit(x+1, \'x\', 1)
    2
    sage: limit(x+1, v=x, a=1) # using v=, a= keywords triggers multiple keyword error
    Traceback (most recent call last):
    ...
    ValueError: multiple keyword arguments specified
    sage: limit(x+1, v=x, a=1, algorithm=\'sympy\') # as above
    Traceback (most recent call last):
    ...
    ValueError: multiple keyword arguments specified
    sage: limit(x+1, x=1, algorithm=\'sympy\')
    2
    sage: limit(x+1, x, 1, algorithm=\'sympy\')
    2

    # Test that var() is not called unnecessarily on symbolic input v
    sage: y = var(\'y\', n=3)
    sage: limit(sum(y), y[1], 1) # Should work directly
    y0 + y2 + 1

    # Test conversion of v if not symbolic
    sage: limit(x**2, \'x\', 3)
    9
    sage: y = var(\'y\')
    sage: limit(x**2 + y, "y", x) # Need y=var(\'y\') defined for this test
    x^2 + x

    # Test conversion of a if not symbolic
    sage: limit(x**2, x, "3")
    9

    # Test using a constant number as variable \'v\' fails
    sage: limit(x**2 + 5, 5, 10)
    Traceback (most recent call last):
    ...
    TypeError: limit variable must be a variable, not a constant
    '''
lim = limit

def mma_free_limit(expression, v, a, dir=None):
    """
    Limit using Mathematica's online interface.

    INPUT:

    - ``expression`` -- symbolic expression
    - ``v`` -- variable
    - ``a`` -- value where the variable goes to
    - ``dir`` -- ``'+'``, ``'-'`` or ``None`` (default: ``None``)

    EXAMPLES::

        sage: from sage.calculus.calculus import mma_free_limit
        sage: mma_free_limit(sin(x)/x, x, a=0) # optional - internet
        1

    Another simple limit::

        sage: mma_free_limit(e^(-x), x, a=oo) # optional - internet
        0
    """
def laplace(ex, t, s, algorithm: str = 'maxima'):
    '''
    Return the Laplace transform with respect to the variable `t` and
    transform parameter `s`, if possible.

    If this function cannot find a solution, a formal function is returned.
    The function that is returned may be viewed as a function of `s`.

    DEFINITION:

    The Laplace transform of a function `f(t)`, defined for all real numbers
    `t \\geq 0`, is the function `F(s)` defined by

    .. MATH::

                      F(s) = \\int_{0}^{\\infty} e^{-st} f(t) dt.

    INPUT:

    - ``ex`` -- a symbolic expression

    - ``t`` -- independent variable

    - ``s`` -- transform parameter

    - ``algorithm`` -- (default: ``\'maxima\'``)  one of

      - ``\'maxima\'`` -- use Maxima (the default)

      - ``\'sympy\'`` -- use SymPy

      - ``\'giac\'`` -- use Giac (optional)

    .. NOTE::

        The ``\'sympy\'`` algorithm returns the tuple (`F`, `a`, ``cond``)
        where `F` is the Laplace transform of `f(t)`,
        `Re(s)>a` is the half-plane of convergence, and ``cond`` are
        auxiliary convergence conditions.

    .. SEEALSO::

        :func:`inverse_laplace`

    EXAMPLES:

    We compute a few Laplace transforms::

        sage: var(\'x, s, z, t, t0\')
        (x, s, z, t, t0)
        sage: sin(x).laplace(x, s)
        1/(s^2 + 1)
        sage: (z + exp(x)).laplace(x, s)
        z/s + 1/(s - 1)
        sage: log(t/t0).laplace(t, s)
        -(euler_gamma + log(s) + log(t0))/s

    We do a formal calculation::

        sage: f = function(\'f\')(x)
        sage: g = f.diff(x); g
        diff(f(x), x)
        sage: g.laplace(x, s)
        s*laplace(f(x), x, s) - f(0)

    A BATTLE BETWEEN the X-women and the Y-men (by David
    Joyner): Solve

    .. MATH::

                   x\' = -16y, x(0)=270,  y\' = -x + 1, y(0) = 90.

    This models a fight between two sides, the "X-women" and the
    "Y-men", where the X-women have 270 initially and the Y-men have
    90, but the Y-men are better at fighting, because of the higher
    factor of "-16" vs "-1", and also get an occasional reinforcement,
    because of the "+1" term.

    ::

        sage: var(\'t\')
        t
        sage: t = var(\'t\')
        sage: x = function(\'x\')(t)
        sage: y = function(\'y\')(t)
        sage: de1 = x.diff(t) + 16*y
        sage: de2 = y.diff(t) + x - 1
        sage: de1.laplace(t, s)
        s*laplace(x(t), t, s) + 16*laplace(y(t), t, s) - x(0)
        sage: de2.laplace(t, s)
        s*laplace(y(t), t, s) - 1/s + laplace(x(t), t, s) - y(0)

    Next we form the augmented matrix of the above system::

        sage: A = matrix([[s, 16, 270], [1, s, 90+1/s]])
        sage: E = A.echelon_form()
        sage: xt = E[0,2].inverse_laplace(s,t)
        sage: yt = E[1,2].inverse_laplace(s,t)
        sage: xt
        -91/2*e^(4*t) + 629/2*e^(-4*t) + 1
        sage: yt
        91/8*e^(4*t) + 629/8*e^(-4*t)
        sage: p1 = plot(xt, 0, 1/2, rgbcolor=(1,0,0))                                   # needs sage.plot
        sage: p2 = plot(yt, 0, 1/2, rgbcolor=(0,1,0))                                   # needs sage.plot
        sage: import tempfile
        sage: with tempfile.NamedTemporaryFile(suffix=\'.png\') as f:                     # needs sage.plot
        ....:     (p1 + p2).save(f.name)

    Another example::

        sage: var(\'a,s,t\')
        (a, s, t)
        sage: f = exp (2*t + a) * sin(t) * t; f
        t*e^(a + 2*t)*sin(t)
        sage: L = laplace(f, t, s); L
        2*(s - 2)*e^a/(s^2 - 4*s + 5)^2
        sage: inverse_laplace(L, s, t)
        t*e^(a + 2*t)*sin(t)

    The Laplace transform of the exponential function::

        sage: laplace(exp(x), x, s)
        1/(s - 1)

    Dirac\'s delta distribution is handled (the output of SymPy is
    related to a choice that has to be made when defining Laplace
    transforms of distributions)::

        sage: laplace(dirac_delta(t), t, s)
        1
        sage: F, a, cond = laplace(dirac_delta(t), t, s, algorithm=\'sympy\')
        sage: a, cond  # random - sympy <1.10 gives (-oo, True)
        (0, True)
        sage: F        # random - sympy <1.9 includes undefined heaviside(0) in answer
        1
        sage: laplace(dirac_delta(t), t, s, algorithm=\'giac\')  # needs giac
        1

    Heaviside step function can be handled with different interfaces.
    Try with Maxima::

        sage: laplace(heaviside(t-1), t, s)
        e^(-s)/s

    Try with giac, if it is installed::

        sage: # needs giac
        sage: laplace(heaviside(t-1), t, s, algorithm=\'giac\')
        e^(-s)/s

    Try with SymPy::

        sage: laplace(heaviside(t-1), t, s, algorithm=\'sympy\')
        (e^(-s)/s, 0, True)

    TESTS:

    Testing Giac::

        sage: # needs giac
        sage: var(\'t, s\')
        (t, s)
        sage: laplace(5*cos(3*t-2)*heaviside(t-2), t, s, algorithm=\'giac\')
        5*(s*cos(4)*e^(-2*s) - 3*e^(-2*s)*sin(4))/(s^2 + 9)

    Check unevaluated expression from Giac (it is locale-dependent, see
    :issue:`22833`)::

        sage: # needs giac
        sage: n = SR.var(\'n\')
        sage: laplace(t^n, t, s, algorithm=\'giac\')
        laplace(t^n, t, s)

    Testing SymPy::

        sage: n = SR.var(\'n\')
        sage: F, a, cond = laplace(t^n, t, s, algorithm=\'sympy\')
        sage: a, cond
        (0, re(n) > -1)
        sage: F.simplify()
        s^(-n - 1)*gamma(n + 1)


    Testing Maxima::
        sage: n = SR.var(\'n\')
        sage: assume(n > -1)
        sage: laplace(t^n, t, s, algorithm=\'maxima\')
        s^(-n - 1)*gamma(n + 1)

    Check that :issue:`24212` is fixed::

        sage: F, a, cond = laplace(cos(t^2), t, s, algorithm=\'sympy\')
        sage: a, cond
        (0, True)
        sage: F._sympy_().simplify()
        sqrt(pi)*(sqrt(2)*sin(s**2/4)*fresnelc(sqrt(2)*s/(2*sqrt(pi))) -
        sqrt(2)*cos(s**2/4)*fresnels(sqrt(2)*s/(2*sqrt(pi))) + cos(s**2/4 + pi/4))/2

    Testing result from SymPy that Sage doesn\'t know how to handle::

        sage: laplace(cos(-1/t), t, s, algorithm=\'sympy\')
        Traceback (most recent call last):
        ...
        AttributeError: Unable to convert SymPy result (=meijerg(((), ()), ((-1/2, 0, 1/2), (0,)), ...)/4) into Sage
    '''
def inverse_laplace(ex, s, t, algorithm: str = 'maxima'):
    """
    Return the inverse Laplace transform with respect to the variable `t` and
    transform parameter `s`, if possible.

    If this function cannot find a solution, a formal function is returned.
    The function that is returned may be viewed as a function of `t`.

    DEFINITION:

    The inverse Laplace transform of a function `F(s)` is the function
    `f(t)`, defined by

    .. MATH::

                      f(t) = \\frac{1}{2\\pi i} \\int_{\\gamma-i\\infty}^{\\gamma + i\\infty} e^{st} F(s) ds,

    where `\\gamma` is chosen so that the contour path of
    integration is in the region of convergence of `F(s)`.

    INPUT:

    - ``ex`` -- a symbolic expression

    - ``s`` -- transform parameter

    - ``t`` -- independent variable

    - ``algorithm`` -- (default: ``'maxima'``)  one of

      - ``'maxima'`` -- use Maxima (the default)

      - ``'sympy'`` -- use SymPy

      - ``'giac'`` -- use Giac (optional)

    .. SEEALSO::

        :func:`laplace`

    EXAMPLES::

        sage: var('w, m')
        (w, m)
        sage: f = (1/(w^2+10)).inverse_laplace(w, m); f
        1/10*sqrt(10)*sin(sqrt(10)*m)
        sage: laplace(f, m, w)
        1/(w^2 + 10)

        sage: f(t) = t*cos(t)
        sage: s = var('s')
        sage: L = laplace(f, t, s); L
        t |--> 2*s^2/(s^2 + 1)^2 - 1/(s^2 + 1)
        sage: inverse_laplace(L, s, t)
        t |--> t*cos(t)
        sage: inverse_laplace(1/(s^3+1), s, t)
        1/3*(sqrt(3)*sin(1/2*sqrt(3)*t) - cos(1/2*sqrt(3)*t))*e^(1/2*t) + 1/3*e^(-t)

    No explicit inverse Laplace transform, so one is returned formally a
    function ``ilt``::

        sage: inverse_laplace(cos(s), s, t)
        ilt(cos(s), s, t)

    Transform an expression involving a time-shift, via SymPy::

        sage: inverse_laplace(1/s^2*exp(-s), s, t, algorithm='sympy').simplify()
        (t - 1)*heaviside(t - 1)

    The same instance with Giac::

        sage: # needs giac
        sage: inverse_laplace(1/s^2*exp(-s), s, t, algorithm='giac')
        (t - 1)*heaviside(t - 1)

    Transform a rational expression::

        sage: # needs giac
        sage: inverse_laplace((2*s^2*exp(-2*s) - exp(-s))/(s^3+1), s, t,
        ....:                 algorithm='giac')
        -1/3*(sqrt(3)*e^(1/2*t - 1/2)*sin(1/2*sqrt(3)*(t - 1))
         - cos(1/2*sqrt(3)*(t - 1))*e^(1/2*t - 1/2) + e^(-t + 1))*heaviside(t - 1)
         + 2/3*(2*cos(1/2*sqrt(3)*(t - 2))*e^(1/2*t - 1) + e^(-t + 2))*heaviside(t - 2)

        sage: inverse_laplace(1/(s - 1), s, x)
        e^x

    The inverse Laplace transform of a constant is a delta
    distribution::

        sage: inverse_laplace(1, s, t)
        dirac_delta(t)
        sage: inverse_laplace(1, s, t, algorithm='sympy')
        dirac_delta(t)
        sage: inverse_laplace(1, s, t, algorithm='giac')  # needs giac
        dirac_delta(t)

    TESTS:

    Testing unevaluated expression from Maxima::

        sage: var('t, s')
        (t, s)
        sage: inverse_laplace(exp(-s)/s, s, t)
        ilt(e^(-s)/s, s, t)

    Testing Giac::

        sage: # needs giac
        sage: inverse_laplace(exp(-s)/s, s, t, algorithm='giac')
        heaviside(t - 1)

    Testing SymPy::

        sage: inverse_laplace(exp(-s)/s, s, t, algorithm='sympy')
        heaviside(t - 1)

    Testing unevaluated expression from Giac::

        sage: # needs giac
        sage: n = SR.var('n')
        sage: inverse_laplace(1/s^n, s, t, algorithm='giac')
        ilt(1/(s^n), t, s)

    Try with Maxima::

        sage: n = SR.var('n')
        sage: inverse_laplace(1/s^n, s, t, algorithm='maxima')
        ilt(1/(s^n), s, t)

    Try with SymPy::

        sage: inverse_laplace(1/s^n, s, t, algorithm='sympy')
        t^(n - 1)*heaviside(t)/gamma(n)

    Testing unevaluated expression from SymPy::

        sage: inverse_laplace(cos(s), s, t, algorithm='sympy')
        ilt(cos(s), t, s)

    Testing the same with Giac::

        sage: # needs giac
        sage: inverse_laplace(cos(s), s, t, algorithm='giac')
        ilt(cos(s), t, s)
    """
def at(ex, *args, **kwds):
    """
    Parses ``at`` formulations from other systems, such as Maxima.
    Replaces evaluation 'at' a point with substitution method of
    a symbolic expression.

    EXAMPLES:

    We do not import ``at`` at the top level, but we can use it
    as a synonym for substitution if we import it::

        sage: g = x^3 - 3
        sage: from sage.calculus.calculus import at
        sage: at(g, x=1)
        -2
        sage: g.subs(x=1)
        -2

    We find a formal Taylor expansion::

        sage: h,x = var('h,x')
        sage: u = function('u')
        sage: u(x + h)
        u(h + x)
        sage: diff(u(x+h), x)
        D[0](u)(h + x)
        sage: taylor(u(x+h), h, 0, 4)
        1/24*h^4*diff(u(x), x, x, x, x) + 1/6*h^3*diff(u(x), x, x, x)
         + 1/2*h^2*diff(u(x), x, x) + h*diff(u(x), x) + u(x)

    We compute a Laplace transform::

        sage: var('s,t')
        (s, t)
        sage: f = function('f')(t)
        sage: f.diff(t, 2)
        diff(f(t), t, t)
        sage: f.diff(t,2).laplace(t,s)
        s^2*laplace(f(t), t, s) - s*f(0) - D[0](f)(0)

    We can also accept a non-keyword list of expression substitutions,
    like Maxima does (:issue:`12796`)::

        sage: from sage.calculus.calculus import at
        sage: f = function('f')
        sage: at(f(x), [x == 1])
        f(1)

    TESTS:

    Our one non-keyword argument must be a list::

        sage: from sage.calculus.calculus import at
        sage: f = function('f')
        sage: at(f(x), x == 1)
        Traceback (most recent call last):
        ...
        TypeError: at can take at most one argument, which must be a list

    We should convert our first argument to a symbolic expression::

        sage: from sage.calculus.calculus import at
        sage: at(int(1), x=1)
        1
    """
def dummy_diff(*args):
    """
    This function is called when 'diff' appears in a Maxima string.

    EXAMPLES::

        sage: from sage.calculus.calculus import dummy_diff
        sage: x,y = var('x,y')
        sage: dummy_diff(sin(x*y), x, SR(2), y, SR(1))
        -x*y^2*cos(x*y) - 2*y*sin(x*y)

    Here the function is used implicitly::

        sage: a = var('a')
        sage: f = function('cr')(a)
        sage: g = f.diff(a); g
        diff(cr(a), a)
    """
def dummy_integrate(*args):
    """
    This function is called to create formal wrappers of integrals that
    Maxima can't compute:

    EXAMPLES::

        sage: from sage.calculus.calculus import dummy_integrate
        sage: f = function('f')
        sage: dummy_integrate(f(x), x)
        integrate(f(x), x)
        sage: a,b = var('a,b')
        sage: dummy_integrate(f(x), x, a, b)
        integrate(f(x), x, a, b)
    """
def dummy_laplace(*args):
    """
    This function is called to create formal wrappers of laplace transforms
    that Maxima can't compute:

    EXAMPLES::

        sage: from sage.calculus.calculus import dummy_laplace
        sage: s,t = var('s,t')
        sage: f = function('f')
        sage: dummy_laplace(f(t), t, s)
        laplace(f(t), t, s)
    """
def dummy_inverse_laplace(*args):
    """
    This function is called to create formal wrappers of inverse Laplace
    transforms that Maxima can't compute:

    EXAMPLES::

        sage: from sage.calculus.calculus import dummy_inverse_laplace
        sage: s,t = var('s,t')
        sage: F = function('F')
        sage: dummy_inverse_laplace(F(s), s, t)
        ilt(F(s), s, t)
    """
def dummy_pochhammer(*args):
    """
    This function is called to create formal wrappers of Pochhammer symbols.

    EXAMPLES::

        sage: from sage.calculus.calculus import dummy_pochhammer
        sage: s,t = var('s,t')
        sage: dummy_pochhammer(s, t)
        gamma(s + t)/gamma(s)
    """

symtable: Incomplete
maxima_qp: Incomplete
maxima_var: Incomplete
sci_not: Incomplete
polylog_ex: Incomplete
maxima_polygamma: Incomplete
maxima_hyper: Incomplete

def symbolic_expression_from_maxima_string(x, equals_sub: bool = False, maxima=...):
    '''
    Given a string representation of a Maxima expression, parse it and
    return the corresponding Sage symbolic expression.

    INPUT:

    - ``x`` -- string

    - ``equals_sub`` -- boolean (default: ``False``); if ``True``, replace
      \'=\' by \'==\' in self

    - ``maxima`` -- (default: the calculus package\'s copy of
      Maxima) the Maxima interpreter to use

    EXAMPLES::

        sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
        sage: sefms(\'x^%e + %e^%pi + %i + sin(0)\')
        x^e + e^pi + I
        sage: f = function(\'f\')(x)
        sage: sefms(\'?%at(f(x),x=2)#1\')
        f(2) != 1
        sage: a = sage.calculus.calculus.maxima("x#0"); a
        x # 0
        sage: a.sage()
        x != 0

    TESTS:

    :issue:`8459` fixed::

        sage: maxima(\'3*li[2](u)+8*li[33](exp(u))\').sage()
        3*dilog(u) + 8*polylog(33, e^u)

    Check if :issue:`8345` is fixed::

        sage: assume(x,\'complex\')
        sage: t = x.conjugate()
        sage: latex(t)
        \\overline{x}
        sage: latex(t._maxima_()._sage_())
        \\overline{x}

    Check that we can understand maxima\'s not-equals (:issue:`8969`)::

        sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
        sage: sefms("x!=3") == (factorial(x) == 3)
        True
        sage: sefms("x # 3") == SR(x != 3)
        True
        sage: solve([x != 5], x) in [[[x - 5 != 0]], [[x < 5], [5 < x]]]
        True
        sage: solve([2*x==3, x != 5], x)
        [[x == (3/2)...

    Make sure that we don\'t accidentally pick up variables in the maxima namespace (:issue:`8734`)::

        sage: sage.calculus.calculus.maxima(\'my_new_var : 2\')
        2
        sage: var(\'my_new_var\').full_simplify()
        my_new_var

    ODE solution constants are treated differently (:issue:`16007`)::

        sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
        sage: sefms(\'%k1*x + %k2*y + %c\')
        _K1*x + _K2*y + _C

    Check that some hypothetical variables don\'t end up as special constants (:issue:`6882`)::

        sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
        sage: sefms(\'%i\')^2
        -1
        sage: ln(sefms(\'%e\'))
        1
        sage: sefms(\'i\')^2
        _i^2
        sage: sefms(\'I\')^2
        _I^2
        sage: sefms(\'ln(e)\')
        ln(_e)
        sage: sefms(\'%inf\')
        +Infinity
    '''
def mapped_opts(v):
    """
    Used internally when creating a string of options to pass to
    Maxima.

    INPUT:

    - ``v`` -- an object

    OUTPUT: string

    The main use of this is to turn Python bools into lower case
    strings.

    EXAMPLES::

        sage: sage.calculus.calculus.mapped_opts(True)
        'true'
        sage: sage.calculus.calculus.mapped_opts(False)
        'false'
        sage: sage.calculus.calculus.mapped_opts('bar')
        'bar'
    """
def maxima_options(**kwds):
    """
    Used internally to create a string of options to pass to Maxima.

    EXAMPLES::

        sage: sage.calculus.calculus.maxima_options(an_option=True, another=False, foo='bar')
        'an_option=true,another=false,foo=bar'
    """

syms_cur: Incomplete
syms_default: Incomplete
parser_make_var: Incomplete
parser_make_function: Incomplete
SR_parser: Incomplete

def symbolic_expression_from_string(s, syms=None, accept_sequence: bool = False, *, parser=None):
    """
    Given a string, (attempt to) parse it and return the
    corresponding Sage symbolic expression.  Normally used
    to return Maxima output to the user.

    INPUT:

    - ``s`` -- string

    - ``syms`` -- (default: ``{}``) dictionary of
      strings to be regarded as symbols or functions;
      keys are pairs (string, number of arguments)

    - ``accept_sequence`` -- boolean (default: ``False``); controls whether
      to allow a (possibly nested) set of lists and tuples
      as input

    - ``parser`` -- (default: ``SR_parser``) parser for internal use

    EXAMPLES::

        sage: from sage.calculus.calculus import symbolic_expression_from_string
        sage: y = var('y')
        sage: symbolic_expression_from_string('[sin(0)*x^2,3*spam+e^pi]',
        ....:                                 syms={('spam',0): y}, accept_sequence=True)
        [0, 3*y + e^pi]

    TESTS:

    Check that the precision is preserved (:issue:`28814`)::

        sage: symbolic_expression_from_string(str(RealField(100)(1/3)))
        0.3333333333333333333333333333
        sage: symbolic_expression_from_string(str(RealField(100)(10^-500/3)))
        3.333333333333333333333333333e-501

    The Giac interface uses a different parser (:issue:`30133`)::

        sage: # needs giac
        sage: from sage.calculus.calculus import SR_parser_giac
        sage: symbolic_expression_from_string(repr(giac(SR.var('e'))), parser=SR_parser_giac)
        e
    """

parser_make_Mvar: Incomplete
SRM_parser: Incomplete
SR_parser_giac: Incomplete
