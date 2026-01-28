from __future__ import annotations
from builtins import range as xrange
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['appellf1', 'appellf2', 'appellf3', 'appellf4', 'bihyper', 'defun', 'defun_wrapped', 'hyp0f1', 'hyp1f1', 'hyp1f2', 'hyp2f0', 'hyp2f1', 'hyp2f2', 'hyp2f3', 'hyp3f2', 'hyper', 'hyper2d', 'hypercomb', 'meijerg', 'xrange']
def _check_need_perturb(ctx, terms, prec, discard_known_zeros):
    ...
def _hyp0f1(ctx, b_s, z, **kwargs):
    ...
def _hyp1f0(ctx, a, z):
    ...
def _hyp1f1(ctx, a_s, b_s, z, **kwargs):
    ...
def _hyp1f2(ctx, a_s, b_s, z, **kwargs):
    ...
def _hyp2f0(ctx, a_s, b_s, z, **kwargs):
    ...
def _hyp2f1(ctx, a_s, b_s, z, **kwargs):
    ...
def _hyp2f1_gosper(ctx, a, b, c, z, **kwargs):
    ...
def _hyp2f2(ctx, a_s, b_s, z, **kwargs):
    ...
def _hyp2f3(ctx, a_s, b_s, z, **kwargs):
    ...
def _hyp_borel(ctx, p, q, a_s, b_s, z, **kwargs):
    ...
def _hypq1fq(ctx, p, q, a_s, b_s, z, **kwargs):
    """
    
    Evaluates 3F2, 4F3, 5F4, ...
    """
def appellf1(ctx, a, b1, b2, c, x, y, **kwargs):
    ...
def appellf2(ctx, a, b1, b2, c1, c2, x, y, **kwargs):
    """
    
    Gives the Appell F2 hypergeometric function of two variables
    
    .. math ::
    
        F_2(a,b_1,b_2,c_1,c_2,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
            \\frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c_1)_m (c_2)_n}
            \\frac{x^m y^n}{m! n!}.
    
    The series is generally absolutely convergent for `|x| + |y| < 1`.
    
    **Examples**
    
    Evaluation for real and complex arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf2(1,2,3,4,5,0.25,0.125)
        1.257417193533135344785602
        >>> appellf2(1,-3,-4,2,3,2,3)
        -42.8
        >>> appellf2(0.5,0.25,-0.25,2,3,0.25j,0.25)
        (0.9880539519421899867041719 + 0.01497616165031102661476978j)
        >>> chop(appellf2(1,1+j,1-j,3j,-3j,0.25,0.25))
        1.201311219287411337955192
        >>> appellf2(1,1,1,4,6,0.125,16)
        (-0.09455532250274744282125152 - 0.7647282253046207836769297j)
    
    A transformation formula::
    
        >>> a,b1,b2,c1,c2,x,y = map(mpf, [1,2,0.5,0.25,1.625,-0.125,0.125])
        >>> appellf2(a,b1,b2,c1,c2,x,y)
        0.2299211717841180783309688
        >>> (1-x)**(-a)*appellf2(a,c1-b1,b2,c1,c2,x/(x-1),y/(1-x))
        0.2299211717841180783309688
    
    A system of partial differential equations satisfied by F2::
    
        >>> a,b1,b2,c1,c2,x,y = map(mpf, [1,0.5,0.25,1.125,1.5,0.0625,-0.0625])
        >>> F = lambda x,y: appellf2(a,b1,b2,c1,c2,x,y)
        >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) -
        ...      x*y*diff(F,(x,y),(1,1)) +
        ...      (c1-(a+b1+1)*x)*diff(F,(x,y),(1,0)) -
        ...      b1*y*diff(F,(x,y),(0,1)) -
        ...      a*b1*F(x,y))
        0.0
        >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) -
        ...      x*y*diff(F,(x,y),(1,1)) +
        ...      (c2-(a+b2+1)*y)*diff(F,(x,y),(0,1)) -
        ...      b2*x*diff(F,(x,y),(1,0)) -
        ...      a*b2*F(x,y))
        0.0
    
    **References**
    
    See references for :func:`~mpmath.appellf1`.
    """
def appellf3(ctx, a1, a2, b1, b2, c, x, y, **kwargs):
    """
    
    Gives the Appell F3 hypergeometric function of two variables
    
    .. math ::
    
        F_3(a_1,a_2,b_1,b_2,c,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
            \\frac{(a_1)_m (a_2)_n (b_1)_m (b_2)_n}{(c)_{m+n}}
            \\frac{x^m y^n}{m! n!}.
    
    The series is generally absolutely convergent for `|x| < 1, |y| < 1`.
    
    **Examples**
    
    Evaluation for various parameters and variables::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf3(1,2,3,4,5,0.5,0.25)
        2.221557778107438938158705
        >>> appellf3(1,2,3,4,5,6,0); hyp2f1(1,3,5,6)
        (-0.5189554589089861284537389 - 0.1454441043328607980769742j)
        (-0.5189554589089861284537389 - 0.1454441043328607980769742j)
        >>> appellf3(1,-2,-3,1,1,4,6)
        -17.4
        >>> appellf3(1,2,-3,1,1,4,6)
        (17.7876136773677356641825 + 19.54768762233649126154534j)
        >>> appellf3(1,2,-3,1,1,6,4)
        (85.02054175067929402953645 + 148.4402528821177305173599j)
        >>> chop(appellf3(1+j,2,1-j,2,3,0.25,0.25))
        1.719992169545200286696007
    
    Many transformations and evaluations for special combinations
    of the parameters are possible, e.g.:
    
        >>> a,b,c,x,y = map(mpf, [0.5,0.25,0.125,0.125,-0.125])
        >>> appellf3(a,c-a,b,c-b,c,x,y)
        1.093432340896087107444363
        >>> (1-y)**(a+b-c)*hyp2f1(a,b,c,x+y-x*y)
        1.093432340896087107444363
        >>> x**2*appellf3(1,1,1,1,3,x,-x)
        0.01568646277445385390945083
        >>> polylog(2,x**2)
        0.01568646277445385390945083
        >>> a1,a2,b1,b2,c,x = map(mpf, [0.5,0.25,0.125,0.5,4.25,0.125])
        >>> appellf3(a1,a2,b1,b2,c,x,1)
        1.03947361709111140096947
        >>> gammaprod([c,c-a2-b2],[c-a2,c-b2])*hyp3f2(a1,b1,c-a2-b2,c-a2,c-b2,x)
        1.03947361709111140096947
    
    The Appell F3 function satisfies a pair of partial
    differential equations::
    
        >>> a1,a2,b1,b2,c,x,y = map(mpf, [0.5,0.25,0.125,0.5,0.625,0.0625,-0.0625])
        >>> F = lambda x,y: appellf3(a1,a2,b1,b2,c,x,y)
        >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) +
        ...      y*diff(F,(x,y),(1,1)) +
        ...     (c-(a1+b1+1)*x)*diff(F,(x,y),(1,0)) -
        ...     a1*b1*F(x,y))
        0.0
        >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) +
        ...     x*diff(F,(x,y),(1,1)) +
        ...     (c-(a2+b2+1)*y)*diff(F,(x,y),(0,1)) -
        ...     a2*b2*F(x,y))
        0.0
    
    **References**
    
    See references for :func:`~mpmath.appellf1`.
    """
def appellf4(ctx, a, b, c1, c2, x, y, **kwargs):
    """
    
    Gives the Appell F4 hypergeometric function of two variables
    
    .. math ::
    
        F_4(a,b,c_1,c_2,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
            \\frac{(a)_{m+n} (b)_{m+n}}{(c_1)_m (c_2)_n}
            \\frac{x^m y^n}{m! n!}.
    
    The series is generally absolutely convergent for
    `\\sqrt{|x|} + \\sqrt{|y|} < 1`.
    
    **Examples**
    
    Evaluation for various parameters and arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> appellf4(1,1,2,2,0.25,0.125)
        1.286182069079718313546608
        >>> appellf4(-2,-3,4,5,4,5)
        34.8
        >>> appellf4(5,4,2,3,0.25j,-0.125j)
        (-0.2585967215437846642163352 + 2.436102233553582711818743j)
    
    Reduction to `\\,_2F_1` in a special case::
    
        >>> a,b,c,x,y = map(mpf, [0.5,0.25,0.125,0.125,-0.125])
        >>> appellf4(a,b,c,a+b-c+1,x*(1-y),y*(1-x))
        1.129143488466850868248364
        >>> hyp2f1(a,b,c,x)*hyp2f1(a,b,a+b-c+1,y)
        1.129143488466850868248364
    
    A system of partial differential equations satisfied by F4::
    
        >>> a,b,c1,c2,x,y = map(mpf, [1,0.5,0.25,1.125,0.0625,-0.0625])
        >>> F = lambda x,y: appellf4(a,b,c1,c2,x,y)
        >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) -
        ...      y**2*diff(F,(x,y),(0,2)) -
        ...      2*x*y*diff(F,(x,y),(1,1)) +
        ...      (c1-(a+b+1)*x)*diff(F,(x,y),(1,0)) -
        ...      ((a+b+1)*y)*diff(F,(x,y),(0,1)) -
        ...      a*b*F(x,y))
        0.0
        >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) -
        ...      x**2*diff(F,(x,y),(2,0)) -
        ...      2*x*y*diff(F,(x,y),(1,1)) +
        ...      (c2-(a+b+1)*y)*diff(F,(x,y),(0,1)) -
        ...      ((a+b+1)*x)*diff(F,(x,y),(1,0)) -
        ...      a*b*F(x,y))
        0.0
    
    **References**
    
    See references for :func:`~mpmath.appellf1`.
    """
def bihyper(ctx, a_s, b_s, z, **kwargs):
    """
    
    Evaluates the bilateral hypergeometric series
    
    .. math ::
    
        \\,_AH_B(a_1, \\ldots, a_k; b_1, \\ldots, b_B; z) =
            \\sum_{n=-\\infty}^{\\infty}
            \\frac{(a_1)_n \\ldots (a_A)_n}
                 {(b_1)_n \\ldots (b_B)_n} \\, z^n
    
    where, for direct convergence, `A = B` and `|z| = 1`, although a
    regularized sum exists more generally by considering the
    bilateral series as a sum of two ordinary hypergeometric
    functions. In order for the series to make sense, none of the
    parameters may be integers.
    
    **Examples**
    
    The value of `\\,_2H_2` at `z = 1` is given by Dougall's formula::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a,b,c,d = 0.5, 1.5, 2.25, 3.25
        >>> bihyper([a,b],[c,d],1)
        -14.49118026212345786148847
        >>> gammaprod([c,d,1-a,1-b,c+d-a-b-1],[c-a,d-a,c-b,d-b])
        -14.49118026212345786148847
    
    The regularized function `\\,_1H_0` can be expressed as the
    sum of one `\\,_2F_0` function and one `\\,_1F_1` function::
    
        >>> a = mpf(0.25)
        >>> z = mpf(0.75)
        >>> bihyper([a], [], z)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        >>> hyper([a,1],[],z) + (hyper([1],[1-a],-1/z)-1)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        >>> hyper([a,1],[],z) + hyper([1],[2-a],-1/z)/z/(a-1)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
    
    **References**
    
    1. [Slater]_ (chapter 6: "Bilateral Series", pp. 180-189)
    2. [Wikipedia]_ http://en.wikipedia.org/wiki/Bilateral_hypergeometric_series
    
    """
def hyp0f1(ctx, b, z, **kwargs):
    """
    
    Gives the hypergeometric function `\\,_0F_1`, sometimes known as the
    confluent limit function, defined as
    
    .. math ::
    
        \\,_0F_1(a,z) = \\sum_{k=0}^{\\infty} \\frac{1}{(a)_k} \\frac{z^k}{k!}.
    
    This function satisfies the differential equation `z f''(z) + a f'(z) = f(z)`,
    and is related to the Bessel function of the first kind (see :func:`~mpmath.besselj`).
    
    ``hyp0f1(a,z)`` is equivalent to ``hyper([],[a],z)``; see documentation for
    :func:`~mpmath.hyper` for more information.
    
    **Examples**
    
    Evaluation for arbitrary arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyp0f1(2, 0.25)
        1.130318207984970054415392
        >>> hyp0f1((1,2), 1234567)
        6.27287187546220705604627e+964
        >>> hyp0f1(3+4j, 1000000j)
        (3.905169561300910030267132e+606 + 3.807708544441684513934213e+606j)
    
    Evaluation is supported for arbitrarily large values of `z`,
    using asymptotic expansions::
    
        >>> hyp0f1(1, 10**50)
        2.131705322874965310390701e+8685889638065036553022565
        >>> hyp0f1(1, -10**50)
        1.115945364792025420300208e-13
    
    Verifying the differential equation::
    
        >>> a = 2.5
        >>> f = lambda z: hyp0f1(a,z)
        >>> for z in [0, 10, 3+4j]:
        ...     chop(z*diff(f,z,2) + a*diff(f,z) - f(z))
        ...
        0.0
        0.0
        0.0
    
    """
def hyp1f1(ctx, a, b, z, **kwargs):
    """
    
    Gives the confluent hypergeometric function of the first kind,
    
    .. math ::
    
        \\,_1F_1(a,b,z) = \\sum_{k=0}^{\\infty} \\frac{(a)_k}{(b)_k} \\frac{z^k}{k!},
    
    also known as Kummer's function and sometimes denoted by `M(a,b,z)`. This
    function gives one solution to the confluent (Kummer's) differential equation
    
    .. math ::
    
        z f''(z) + (b-z) f'(z) - af(z) = 0.
    
    A second solution is given by the `U` function; see :func:`~mpmath.hyperu`.
    Solutions are also given in an alternate form by the Whittaker
    functions (:func:`~mpmath.whitm`, :func:`~mpmath.whitw`).
    
    ``hyp1f1(a,b,z)`` is equivalent
    to ``hyper([a],[b],z)``; see documentation for :func:`~mpmath.hyper` for more
    information.
    
    **Examples**
    
    Evaluation for real and complex values of the argument `z`, with
    fixed parameters `a = 2, b = -1/3`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyp1f1(2, (-1,3), 3.25)
        -2815.956856924817275640248
        >>> hyp1f1(2, (-1,3), -3.25)
        -1.145036502407444445553107
        >>> hyp1f1(2, (-1,3), 1000)
        -8.021799872770764149793693e+441
        >>> hyp1f1(2, (-1,3), -1000)
        0.000003131987633006813594535331
        >>> hyp1f1(2, (-1,3), 100+100j)
        (-3.189190365227034385898282e+48 - 1.106169926814270418999315e+49j)
    
    Parameters may be complex::
    
        >>> hyp1f1(2+3j, -1+j, 10j)
        (261.8977905181045142673351 + 160.8930312845682213562172j)
    
    Arbitrarily large values of `z` are supported::
    
        >>> hyp1f1(3, 4, 10**20)
        3.890569218254486878220752e+43429448190325182745
        >>> hyp1f1(3, 4, -10**20)
        6.0e-60
        >>> hyp1f1(3, 4, 10**20*j)
        (-1.935753855797342532571597e-20 - 2.291911213325184901239155e-20j)
    
    Verifying the differential equation::
    
        >>> a, b = 1.5, 2
        >>> f = lambda z: hyp1f1(a,b,z)
        >>> for z in [0, -10, 3, 3+4j]:
        ...     chop(z*diff(f,z,2) + (b-z)*diff(f,z) - a*f(z))
        ...
        0.0
        0.0
        0.0
        0.0
    
    An integral representation::
    
        >>> a, b = 1.5, 3
        >>> z = 1.5
        >>> hyp1f1(a,b,z)
        2.269381460919952778587441
        >>> g = lambda t: exp(z*t)*t**(a-1)*(1-t)**(b-a-1)
        >>> gammaprod([b],[a,b-a])*quad(g, [0,1])
        2.269381460919952778587441
    
    
    """
def hyp1f2(ctx, a1, b1, b2, z, **kwargs):
    """
    
    Gives the hypergeometric function `\\,_1F_2(a_1,a_2;b_1,b_2; z)`.
    The call ``hyp1f2(a1,b1,b2,z)`` is equivalent to
    ``hyper([a1],[b1,b2],z)``.
    
    Evaluation works for complex and arbitrarily large arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a, b, c = 1.5, (-1,3), 2.25
        >>> hyp1f2(a, b, c, 10**20)
        -1.159388148811981535941434e+8685889639
        >>> hyp1f2(a, b, c, -10**20)
        -12.60262607892655945795907
        >>> hyp1f2(a, b, c, 10**20*j)
        (4.237220401382240876065501e+6141851464 - 2.950930337531768015892987e+6141851464j)
        >>> hyp1f2(2+3j, -2j, 0.5j, 10-20j)
        (135881.9905586966432662004 - 86681.95885418079535738828j)
    
    """
def hyp2f0(ctx, a, b, z, **kwargs):
    """
    
    Gives the hypergeometric function `\\,_2F_0`, defined formally by the
    series
    
    .. math ::
    
        \\,_2F_0(a,b;;z) = \\sum_{n=0}^{\\infty} (a)_n (b)_n \\frac{z^n}{n!}.
    
    This series usually does not converge. For small enough `z`, it can be viewed
    as an asymptotic series that may be summed directly with an appropriate
    truncation. When this is not the case, :func:`~mpmath.hyp2f0` gives a regularized sum,
    or equivalently, it uses a representation in terms of the
    hypergeometric U function [1]. The series also converges when either `a` or `b`
    is a nonpositive integer, as it then terminates into a polynomial
    after `-a` or `-b` terms.
    
    **Examples**
    
    Evaluation is supported for arbitrary complex arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyp2f0((2,3), 1.25, -100)
        0.07095851870980052763312791
        >>> hyp2f0((2,3), 1.25, 100)
        (-0.03254379032170590665041131 + 0.07269254613282301012735797j)
        >>> hyp2f0(-0.75, 1-j, 4j)
        (-0.3579987031082732264862155 - 3.052951783922142735255881j)
    
    Even with real arguments, the regularized value of 2F0 is often complex-valued,
    but the imaginary part decreases exponentially as `z \\to 0`. In the following
    example, the first call uses complex evaluation while the second has a small
    enough `z` to evaluate using the direct series and thus the returned value
    is strictly real (this should be taken to indicate that the imaginary
    part is less than ``eps``)::
    
        >>> mp.dps = 15
        >>> hyp2f0(1.5, 0.5, 0.05)
        (1.04166637647907 + 8.34584913683906e-8j)
        >>> hyp2f0(1.5, 0.5, 0.0005)
        1.00037535207621
    
    The imaginary part can be retrieved by increasing the working precision::
    
        >>> mp.dps = 80
        >>> nprint(hyp2f0(1.5, 0.5, 0.009).imag)
        1.23828e-46
    
    In the polynomial case (the series terminating), 2F0 can evaluate exactly::
    
        >>> mp.dps = 15
        >>> hyp2f0(-6,-6,2)
        291793.0
        >>> identify(hyp2f0(-2,1,0.25))
        '(5/8)'
    
    The coefficients of the polynomials can be recovered using Taylor expansion::
    
        >>> nprint(taylor(lambda x: hyp2f0(-3,0.5,x), 0, 10))
        [1.0, -1.5, 2.25, -1.875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        >>> nprint(taylor(lambda x: hyp2f0(-4,0.5,x), 0, 10))
        [1.0, -2.0, 4.5, -7.5, 6.5625, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    
    [1] http://people.math.sfu.ca/~cbm/aands/page_504.htm
    """
def hyp2f1(ctx, a, b, c, z, **kwargs):
    """
    
    Gives the Gauss hypergeometric function `\\,_2F_1` (often simply referred to as
    *the* hypergeometric function), defined for `|z| < 1` as
    
    .. math ::
    
        \\,_2F_1(a,b,c,z) = \\sum_{k=0}^{\\infty}
            \\frac{(a)_k (b)_k}{(c)_k} \\frac{z^k}{k!}.
    
    and for `|z| \\ge 1` by analytic continuation, with a branch cut on `(1, \\infty)`
    when necessary.
    
    Special cases of this function include many of the orthogonal polynomials as
    well as the incomplete beta function and other functions. Properties of the
    Gauss hypergeometric function are documented comprehensively in many references,
    for example Abramowitz & Stegun, section 15.
    
    The implementation supports the analytic continuation as well as evaluation
    close to the unit circle where `|z| \\approx 1`. The syntax ``hyp2f1(a,b,c,z)``
    is equivalent to ``hyper([a,b],[c],z)``.
    
    **Examples**
    
    Evaluation with `z` inside, outside and on the unit circle, for
    fixed parameters::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyp2f1(2, (1,2), 4, 0.75)
        1.303703703703703703703704
        >>> hyp2f1(2, (1,2), 4, -1.75)
        0.7431290566046919177853916
        >>> hyp2f1(2, (1,2), 4, 1.75)
        (1.418075801749271137026239 - 1.114976146679907015775102j)
        >>> hyp2f1(2, (1,2), 4, 1)
        1.6
        >>> hyp2f1(2, (1,2), 4, -1)
        0.8235498012182875315037882
        >>> hyp2f1(2, (1,2), 4, j)
        (0.9144026291433065674259078 + 0.2050415770437884900574923j)
        >>> hyp2f1(2, (1,2), 4, 2+j)
        (0.9274013540258103029011549 + 0.7455257875808100868984496j)
        >>> hyp2f1(2, (1,2), 4, 0.25j)
        (0.9931169055799728251931672 + 0.06154836525312066938147793j)
    
    Evaluation with complex parameter values::
    
        >>> hyp2f1(1+j, 0.75, 10j, 1+5j)
        (0.8834833319713479923389638 + 0.7053886880648105068343509j)
    
    Evaluation with `z = 1`::
    
        >>> hyp2f1(-2.5, 3.5, 1.5, 1)
        0.0
        >>> hyp2f1(-2.5, 3, 4, 1)
        0.06926406926406926406926407
        >>> hyp2f1(2, 3, 4, 1)
        +inf
    
    Evaluation for huge arguments::
    
        >>> hyp2f1((-1,3), 1.75, 4, '1e100')
        (7.883714220959876246415651e+32 + 1.365499358305579597618785e+33j)
        >>> hyp2f1((-1,3), 1.75, 4, '1e1000000')
        (7.883714220959876246415651e+333332 + 1.365499358305579597618785e+333333j)
        >>> hyp2f1((-1,3), 1.75, 4, '1e1000000j')
        (1.365499358305579597618785e+333333 - 7.883714220959876246415651e+333332j)
    
    An integral representation::
    
        >>> a,b,c,z = -0.5, 1, 2.5, 0.25
        >>> g = lambda t: t**(b-1) * (1-t)**(c-b-1) * (1-t*z)**(-a)
        >>> gammaprod([c],[b,c-b]) * quad(g, [0,1])
        0.9480458814362824478852618
        >>> hyp2f1(a,b,c,z)
        0.9480458814362824478852618
    
    Verifying the hypergeometric differential equation::
    
        >>> f = lambda z: hyp2f1(a,b,c,z)
        >>> chop(z*(1-z)*diff(f,z,2) + (c-(a+b+1)*z)*diff(f,z) - a*b*f(z))
        0.0
    
    """
def hyp2f2(ctx, a1, a2, b1, b2, z, **kwargs):
    """
    
    Gives the hypergeometric function `\\,_2F_2(a_1,a_2;b_1,b_2; z)`.
    The call ``hyp2f2(a1,a2,b1,b2,z)`` is equivalent to
    ``hyper([a1,a2],[b1,b2],z)``.
    
    Evaluation works for complex and arbitrarily large arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a, b, c, d = 1.5, (-1,3), 2.25, 4
        >>> hyp2f2(a, b, c, d, 10**20)
        -5.275758229007902299823821e+43429448190325182663
        >>> hyp2f2(a, b, c, d, -10**20)
        2561445.079983207701073448
        >>> hyp2f2(a, b, c, d, 10**20*j)
        (2218276.509664121194836667 - 1280722.539991603850462856j)
        >>> hyp2f2(2+3j, -2j, 0.5j, 4j, 10-20j)
        (80500.68321405666957342788 - 20346.82752982813540993502j)
    
    """
def hyp2f3(ctx, a1, a2, b1, b2, b3, z, **kwargs):
    """
    
    Gives the hypergeometric function `\\,_2F_3(a_1,a_2;b_1,b_2,b_3; z)`.
    The call ``hyp2f3(a1,a2,b1,b2,b3,z)`` is equivalent to
    ``hyper([a1,a2],[b1,b2,b3],z)``.
    
    Evaluation works for arbitrarily large arguments::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a1,a2,b1,b2,b3 = 1.5, (-1,3), 2.25, 4, (1,5)
        >>> hyp2f3(a1,a2,b1,b2,b3,10**20)
        -4.169178177065714963568963e+8685889590
        >>> hyp2f3(a1,a2,b1,b2,b3,-10**20)
        7064472.587757755088178629
        >>> hyp2f3(a1,a2,b1,b2,b3,10**20*j)
        (-5.163368465314934589818543e+6141851415 + 1.783578125755972803440364e+6141851416j)
        >>> hyp2f3(2+3j, -2j, 0.5j, 4j, -1-j, 10-20j)
        (-2280.938956687033150740228 + 13620.97336609573659199632j)
        >>> hyp2f3(2+3j, -2j, 0.5j, 4j, -1-j, 10000000-20000000j)
        (4.849835186175096516193e+3504 - 3.365981529122220091353633e+3504j)
    
    """
def hyp3f2(ctx, a1, a2, a3, b1, b2, z, **kwargs):
    """
    
    Gives the generalized hypergeometric function `\\,_3F_2`, defined for `|z| < 1`
    as
    
    .. math ::
    
        \\,_3F_2(a_1,a_2,a_3,b_1,b_2,z) = \\sum_{k=0}^{\\infty}
            \\frac{(a_1)_k (a_2)_k (a_3)_k}{(b_1)_k (b_2)_k} \\frac{z^k}{k!}.
    
    and for `|z| \\ge 1` by analytic continuation. The analytic structure of this
    function is similar to that of `\\,_2F_1`, generally with a singularity at
    `z = 1` and a branch cut on `(1, \\infty)`.
    
    Evaluation is supported inside, on, and outside
    the circle of convergence `|z| = 1`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> hyp3f2(1,2,3,4,5,0.25)
        1.083533123380934241548707
        >>> hyp3f2(1,2+2j,3,4,5,-10+10j)
        (0.1574651066006004632914361 - 0.03194209021885226400892963j)
        >>> hyp3f2(1,2,3,4,5,-10)
        0.3071141169208772603266489
        >>> hyp3f2(1,2,3,4,5,10)
        (-0.4857045320523947050581423 - 0.5988311440454888436888028j)
        >>> hyp3f2(0.25,1,1,2,1.5,1)
        1.157370995096772047567631
        >>> (8-pi-2*ln2)/3
        1.157370995096772047567631
        >>> hyp3f2(1+j,0.5j,2,1,-2j,-1)
        (1.74518490615029486475959 + 0.1454701525056682297614029j)
        >>> hyp3f2(1+j,0.5j,2,1,-2j,sqrt(j))
        (0.9829816481834277511138055 - 0.4059040020276937085081127j)
        >>> hyp3f2(-3,2,1,-5,4,1)
        1.41
        >>> hyp3f2(-3,2,1,-5,4,2)
        2.12
    
    Evaluation very close to the unit circle::
    
        >>> hyp3f2(1,2,3,4,5,'1.0001')
        (1.564877796743282766872279 - 3.76821518787438186031973e-11j)
        >>> hyp3f2(1,2,3,4,5,'1+0.0001j')
        (1.564747153061671573212831 + 0.0001305757570366084557648482j)
        >>> hyp3f2(1,2,3,4,5,'0.9999')
        1.564616644881686134983664
        >>> hyp3f2(1,2,3,4,5,'-0.9999')
        0.7823896253461678060196207
    
    .. note ::
    
        Evaluation for `|z-1|` small can currently be inaccurate or slow
        for some parameter combinations.
    
    For various parameter combinations, `\\,_3F_2` admits representation in terms
    of hypergeometric functions of lower degree, or in terms of
    simpler functions::
    
        >>> for a, b, z in [(1,2,-1), (2,0.5,1)]:
        ...     hyp2f1(a,b,a+b+0.5,z)**2
        ...     hyp3f2(2*a,a+b,2*b,a+b+0.5,2*a+2*b,z)
        ...
        0.4246104461966439006086308
        0.4246104461966439006086308
        7.111111111111111111111111
        7.111111111111111111111111
    
        >>> z = 2+3j
        >>> hyp3f2(0.5,1,1.5,2,2,z)
        (0.7621440939243342419729144 + 0.4249117735058037649915723j)
        >>> 4*(pi-2*ellipe(z))/(pi*z)
        (0.7621440939243342419729144 + 0.4249117735058037649915723j)
    
    """
def hyper(ctx, a_s, b_s, z, **kwargs):
    """
    
    Evaluates the generalized hypergeometric function
    
    .. math ::
    
        \\,_pF_q(a_1,\\ldots,a_p; b_1,\\ldots,b_q; z) =
        \\sum_{n=0}^\\infty \\frac{(a_1)_n (a_2)_n \\ldots (a_p)_n}
           {(b_1)_n(b_2)_n\\ldots(b_q)_n} \\frac{z^n}{n!}
    
    where `(x)_n` denotes the rising factorial (see :func:`~mpmath.rf`).
    
    The parameters lists ``a_s`` and ``b_s`` may contain integers,
    real numbers, complex numbers, as well as exact fractions given in
    the form of tuples `(p, q)`. :func:`~mpmath.hyper` is optimized to handle
    integers and fractions more efficiently than arbitrary
    floating-point parameters (since rational parameters are by
    far the most common).
    
    **Examples**
    
    Verifying that :func:`~mpmath.hyper` gives the sum in the definition, by
    comparison with :func:`~mpmath.nsum`::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a,b,c,d = 2,3,4,5
        >>> x = 0.25
        >>> hyper([a,b],[c,d],x)
        1.078903941164934876086237
        >>> fn = lambda n: rf(a,n)*rf(b,n)/rf(c,n)/rf(d,n)*x**n/fac(n)
        >>> nsum(fn, [0, inf])
        1.078903941164934876086237
    
    The parameters can be any combination of integers, fractions,
    floats and complex numbers::
    
        >>> a, b, c, d, e = 1, (-1,2), pi, 3+4j, (2,3)
        >>> x = 0.2j
        >>> hyper([a,b],[c,d,e],x)
        (0.9923571616434024810831887 - 0.005753848733883879742993122j)
        >>> b, e = -0.5, mpf(2)/3
        >>> fn = lambda n: rf(a,n)*rf(b,n)/rf(c,n)/rf(d,n)/rf(e,n)*x**n/fac(n)
        >>> nsum(fn, [0, inf])
        (0.9923571616434024810831887 - 0.005753848733883879742993122j)
    
    The `\\,_0F_0` and `\\,_1F_0` series are just elementary functions::
    
        >>> a, z = sqrt(2), +pi
        >>> hyper([],[],z)
        23.14069263277926900572909
        >>> exp(z)
        23.14069263277926900572909
        >>> hyper([a],[],z)
        (-0.09069132879922920160334114 + 0.3283224323946162083579656j)
        >>> (1-z)**(-a)
        (-0.09069132879922920160334114 + 0.3283224323946162083579656j)
    
    If any `a_k` coefficient is a nonpositive integer, the series terminates
    into a finite polynomial::
    
        >>> hyper([1,1,1,-3],[2,5],1)
        0.7904761904761904761904762
        >>> identify(_)
        '(83/105)'
    
    If any `b_k` is a nonpositive integer, the function is undefined (unless the
    series terminates before the division by zero occurs)::
    
        >>> hyper([1,1,1,-3],[-2,5],1)
        Traceback (most recent call last):
          ...
        ZeroDivisionError: pole in hypergeometric series
        >>> hyper([1,1,1,-1],[-2,5],1)
        1.1
    
    Except for polynomial cases, the radius of convergence `R` of the hypergeometric
    series is either `R = \\infty` (if `p \\le q`), `R = 1` (if `p = q+1`), or
    `R = 0` (if `p > q+1`).
    
    The analytic continuations of the functions with `p = q+1`, i.e. `\\,_2F_1`,
    `\\,_3F_2`,  `\\,_4F_3`, etc, are all implemented and therefore these functions
    can be evaluated for `|z| \\ge 1`. The shortcuts :func:`~mpmath.hyp2f1`, :func:`~mpmath.hyp3f2`
    are available to handle the most common cases (see their documentation),
    but functions of higher degree are also supported via :func:`~mpmath.hyper`::
    
        >>> hyper([1,2,3,4], [5,6,7], 1)   # 4F3 at finite-valued branch point
        1.141783505526870731311423
        >>> hyper([4,5,6,7], [1,2,3], 1)   # 4F3 at pole
        +inf
        >>> hyper([1,2,3,4,5], [6,7,8,9], 10)    # 5F4
        (1.543998916527972259717257 - 0.5876309929580408028816365j)
        >>> hyper([1,2,3,4,5,6], [7,8,9,10,11], 1j)   # 6F5
        (0.9996565821853579063502466 + 0.0129721075905630604445669j)
    
    Near `z = 1` with noninteger parameters::
    
        >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','41/8'], 1)
        2.219433352235586121250027
        >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','5/4'], 1)
        +inf
        >>> eps1 = extradps(6)(lambda: 1 - mpf('1e-6'))()
        >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','5/4'], eps1)
        2923978034.412973409330956
    
    Please note that, as currently implemented, evaluation of `\\,_pF_{p-1}`
    with `p \\ge 3` may be slow or inaccurate when `|z-1|` is small,
    for some parameter values.
    
    Evaluation may be aborted if convergence appears to be too slow.
    The optional ``maxterms`` (limiting the number of series terms) and ``maxprec``
    (limiting the internal precision) keyword arguments can be used
    to control evaluation::
    
        >>> hyper([1,2,3], [4,5,6], 10000)              # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
          ...
        NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
        >>> hyper([1,2,3], [4,5,6], 10000, maxterms=10**6)
        7.622806053177969474396918e+4310
    
    Additional options include ``force_series`` (which forces direct use of
    a hypergeometric series even if another evaluation method might work better)
    and ``asymp_tol`` which controls the target tolerance for using
    asymptotic series.
    
    When `p > q+1`, ``hyper`` computes the (iterated) Borel sum of the divergent
    series. For `\\,_2F_0` the Borel sum has an analytic solution and can be
    computed efficiently (see :func:`~mpmath.hyp2f0`). For higher degrees, the functions
    is evaluated first by attempting to sum it directly as an asymptotic
    series (this only works for tiny `|z|`), and then by evaluating the Borel
    regularized sum using numerical integration. Except for
    special parameter combinations, this can be extremely slow.
    
        >>> hyper([1,1], [], 0.5)          # regularization of 2F0
        (1.340965419580146562086448 + 0.8503366631752726568782447j)
        >>> hyper([1,1,1,1], [1], 0.5)     # regularization of 4F1
        (1.108287213689475145830699 + 0.5327107430640678181200491j)
    
    With the following magnitude of argument, the asymptotic series for `\\,_3F_1`
    gives only a few digits. Using Borel summation, ``hyper`` can produce
    a value with full accuracy::
    
        >>> mp.dps = 15
        >>> hyper([2,0.5,4], [5.25], '0.08', force_series=True)             # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
          ...
        NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
        >>> hyper([2,0.5,4], [5.25], '0.08', asymp_tol=1e-4)
        1.0725535790737
        >>> hyper([2,0.5,4], [5.25], '0.08')
        (1.07269542893559 + 5.54668863216891e-5j)
        >>> hyper([2,0.5,4], [5.25], '-0.08', asymp_tol=1e-4)
        0.946344925484879
        >>> hyper([2,0.5,4], [5.25], '-0.08')
        0.946312503737771
        >>> mp.dps = 25
        >>> hyper([2,0.5,4], [5.25], '-0.08')
        0.9463125037377662296700858
    
    Note that with the positive `z` value, there is a complex part in the
    correct result, which falls below the tolerance of the asymptotic series.
    
    By default, a parameter that appears in both ``a_s`` and ``b_s`` will be removed
    unless it is a nonpositive integer. This generally speeds up evaluation
    by producing a hypergeometric function of lower order.
    This optimization can be disabled by passing ``eliminate=False``.
    
        >>> hyper([1,2,3], [4,5,3], 10000)
        1.268943190440206905892212e+4321
        >>> hyper([1,2,3], [4,5,3], 10000, eliminate=False)             # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
          ...
        NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
        >>> hyper([1,2,3], [4,5,3], 10000, eliminate=False, maxterms=10**6)
        1.268943190440206905892212e+4321
    
    If a nonpositive integer `-n` appears in both ``a_s`` and ``b_s``, this parameter
    cannot be unambiguously removed since it creates a term 0 / 0.
    In this case the hypergeometric series is understood to terminate before
    the division by zero occurs. This convention is consistent with Mathematica.
    An alternative convention of eliminating the parameters can be toggled
    with ``eliminate_all=True``:
    
        >>> hyper([2,-1], [-1], 3)
        7.0
        >>> hyper([2,-1], [-1], 3, eliminate_all=True)
        0.25
        >>> hyper([2], [], 3)
        0.25
    
    """
def hyper2d(ctx, a, b, x, y, **kwargs):
    """
    
    Sums the generalized 2D hypergeometric series
    
    .. math ::
    
        \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
            \\frac{P((a),m,n)}{Q((b),m,n)}
            \\frac{x^m y^n} {m! n!}
    
    where `(a) = (a_1,\\ldots,a_r)`, `(b) = (b_1,\\ldots,b_s)` and where
    `P` and `Q` are products of rising factorials such as `(a_j)_n` or
    `(a_j)_{m+n}`. `P` and `Q` are specified in the form of dicts, with
    the `m` and `n` dependence as keys and parameter lists as values.
    The supported rising factorials are given in the following table
    (note that only a few are supported in `Q`):
    
    +------------+-------------------+--------+
    | Key        |  Rising factorial | `Q`    |
    +============+===================+========+
    | ``'m'``    |   `(a_j)_m`       | Yes    |
    +------------+-------------------+--------+
    | ``'n'``    |   `(a_j)_n`       | Yes    |
    +------------+-------------------+--------+
    | ``'m+n'``  |   `(a_j)_{m+n}`   | Yes    |
    +------------+-------------------+--------+
    | ``'m-n'``  |   `(a_j)_{m-n}`   | No     |
    +------------+-------------------+--------+
    | ``'n-m'``  |   `(a_j)_{n-m}`   | No     |
    +------------+-------------------+--------+
    | ``'2m+n'`` |   `(a_j)_{2m+n}`  | No     |
    +------------+-------------------+--------+
    | ``'2m-n'`` |   `(a_j)_{2m-n}`  | No     |
    +------------+-------------------+--------+
    | ``'2n-m'`` |   `(a_j)_{2n-m}`  | No     |
    +------------+-------------------+--------+
    
    For example, the Appell F1 and F4 functions
    
    .. math ::
    
        F_1 = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
              \\frac{(a)_{m+n} (b)_m (c)_n}{(d)_{m+n}}
              \\frac{x^m y^n}{m! n!}
    
        F_4 = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
              \\frac{(a)_{m+n} (b)_{m+n}}{(c)_m (d)_{n}}
              \\frac{x^m y^n}{m! n!}
    
    can be represented respectively as
    
        ``hyper2d({'m+n':[a], 'm':[b], 'n':[c]}, {'m+n':[d]}, x, y)``
    
        ``hyper2d({'m+n':[a,b]}, {'m':[c], 'n':[d]}, x, y)``
    
    More generally, :func:`~mpmath.hyper2d` can evaluate any of the 34 distinct
    convergent second-order (generalized Gaussian) hypergeometric
    series enumerated by Horn, as well as the Kampe de Feriet
    function.
    
    The series is computed by rewriting it so that the inner
    series (i.e. the series containing `n` and `y`) has the form of an
    ordinary generalized hypergeometric series and thereby can be
    evaluated efficiently using :func:`~mpmath.hyper`. If possible,
    manually swapping `x` and `y` and the corresponding parameters
    can sometimes give better results.
    
    **Examples**
    
    Two separable cases: a product of two geometric series, and a
    product of two Gaussian hypergeometric functions::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> x, y = mpf(0.25), mpf(0.5)
        >>> hyper2d({'m':1,'n':1}, {}, x,y)
        2.666666666666666666666667
        >>> 1/(1-x)/(1-y)
        2.666666666666666666666667
        >>> hyper2d({'m':[1,2],'n':[3,4]}, {'m':[5],'n':[6]}, x,y)
        4.164358531238938319669856
        >>> hyp2f1(1,2,5,x)*hyp2f1(3,4,6,y)
        4.164358531238938319669856
    
    Some more series that can be done in closed form::
    
        >>> hyper2d({'m':1,'n':1},{'m+n':1},x,y)
        2.013417124712514809623881
        >>> (exp(x)*x-exp(y)*y)/(x-y)
        2.013417124712514809623881
    
    Six of the 34 Horn functions, G1-G3 and H1-H3::
    
        >>> from mpmath import *
        >>> mp.dps = 10; mp.pretty = True
        >>> x, y = 0.0625, 0.125
        >>> a1,a2,b1,b2,c1,c2,d = 1.1,-1.2,-1.3,-1.4,1.5,-1.6,1.7
        >>> hyper2d({'m+n':a1,'n-m':b1,'m-n':b2},{},x,y)  # G1
        1.139090746
        >>> nsum(lambda m,n: rf(a1,m+n)*rf(b1,n-m)*rf(b2,m-n)*\\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        1.139090746
        >>> hyper2d({'m':a1,'n':a2,'n-m':b1,'m-n':b2},{},x,y)  # G2
        0.9503682696
        >>> nsum(lambda m,n: rf(a1,m)*rf(a2,n)*rf(b1,n-m)*rf(b2,m-n)*\\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        0.9503682696
        >>> hyper2d({'2n-m':a1,'2m-n':a2},{},x,y)  # G3
        1.029372029
        >>> nsum(lambda m,n: rf(a1,2*n-m)*rf(a2,2*m-n)*\\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        1.029372029
        >>> hyper2d({'m-n':a1,'m+n':b1,'n':c1},{'m':d},x,y)  # H1
        -1.605331256
        >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m+n)*rf(c1,n)/rf(d,m)*\\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        -1.605331256
        >>> hyper2d({'m-n':a1,'m':b1,'n':[c1,c2]},{'m':d},x,y)  # H2
        -2.35405404
        >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m)*rf(c1,n)*rf(c2,n)/rf(d,m)*\\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        -2.35405404
        >>> hyper2d({'2m+n':a1,'n':b1},{'m+n':c1},x,y)  # H3
        0.974479074
        >>> nsum(lambda m,n: rf(a1,2*m+n)*rf(b1,n)/rf(c1,m+n)*\\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        0.974479074
    
    **References**
    
    1. [SrivastavaKarlsson]_
    2. [Weisstein]_ http://mathworld.wolfram.com/HornFunction.html
    3. [Weisstein]_ http://mathworld.wolfram.com/AppellHypergeometricFunction.html
    
    """
def hypercomb(ctx, function, params = list(), discard_known_zeros = True, **kwargs):
    """
    
    Computes a weighted combination of hypergeometric functions
    
    .. math ::
    
        \\sum_{r=1}^N \\left[ \\prod_{k=1}^{l_r} {w_{r,k}}^{c_{r,k}}
        \\frac{\\prod_{k=1}^{m_r} \\Gamma(\\alpha_{r,k})}{\\prod_{k=1}^{n_r}
        \\Gamma(\\beta_{r,k})}
        \\,_{p_r}F_{q_r}(a_{r,1},\\ldots,a_{r,p}; b_{r,1},
        \\ldots, b_{r,q}; z_r)\\right].
    
    Typically the parameters are linear combinations of a small set of base
    parameters; :func:`~mpmath.hypercomb` permits computing a correct value in
    the case that some of the `\\alpha`, `\\beta`, `b` turn out to be
    nonpositive integers, or if division by zero occurs for some `w^c`,
    assuming that there are opposing singularities that cancel out.
    The limit is computed by evaluating the function with the base
    parameters perturbed, at a higher working precision.
    
    The first argument should be a function that takes the perturbable
    base parameters ``params`` as input and returns `N` tuples
    ``(w, c, alpha, beta, a, b, z)``, where the coefficients ``w``, ``c``,
    gamma factors ``alpha``, ``beta``, and hypergeometric coefficients
    ``a``, ``b`` each should be lists of numbers, and ``z`` should be a single
    number.
    
    **Examples**
    
    The following evaluates
    
    .. math ::
    
        (a-1) \\frac{\\Gamma(a-3)}{\\Gamma(a-4)} \\,_1F_1(a,a-1,z) = e^z(a-4)(a+z-1)
    
    with `a=1, z=3`. There is a zero factor, two gamma function poles, and
    the 1F1 function is singular; all singularities cancel out to give a finite
    value::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> hypercomb(lambda a: [([a-1],[1],[a-3],[a-4],[a],[a-1],3)], [1])
        -180.769832308689
        >>> -9*exp(3)
        -180.769832308689
    
    """
def meijerg(ctx, a_s, b_s, z, r = 1, series = None, **kwargs):
    """
    
    Evaluates the Meijer G-function, defined as
    
    .. math ::
    
        G^{m,n}_{p,q} \\left( \\left. \\begin{matrix}
             a_1, \\dots, a_n ; a_{n+1} \\dots a_p \\\\
             b_1, \\dots, b_m ; b_{m+1} \\dots b_q
        \\end{matrix}\\; \\right| \\; z ; r \\right) =
        \\frac{1}{2 \\pi i} \\int_L
        \\frac{\\prod_{j=1}^m \\Gamma(b_j+s) \\prod_{j=1}^n\\Gamma(1-a_j-s)}
             {\\prod_{j=n+1}^{p}\\Gamma(a_j+s) \\prod_{j=m+1}^q \\Gamma(1-b_j-s)}
             z^{-s/r} ds
    
    for an appropriate choice of the contour `L` (see references).
    
    There are `p` elements `a_j`.
    The argument *a_s* should be a pair of lists, the first containing the
    `n` elements `a_1, \\ldots, a_n` and the second containing
    the `p-n` elements `a_{n+1}, \\ldots a_p`.
    
    There are `q` elements `b_j`.
    The argument *b_s* should be a pair of lists, the first containing the
    `m` elements `b_1, \\ldots, b_m` and the second containing
    the `q-m` elements `b_{m+1}, \\ldots b_q`.
    
    The implicit tuple `(m, n, p, q)` constitutes the order or degree of the
    Meijer G-function, and is determined by the lengths of the coefficient
    vectors. Confusingly, the indices in this tuple appear in a different order
    from the coefficients, but this notation is standard. The many examples
    given below should hopefully clear up any potential confusion.
    
    **Algorithm**
    
    The Meijer G-function is evaluated as a combination of hypergeometric series.
    There are two versions of the function, which can be selected with
    the optional *series* argument.
    
    *series=1* uses a sum of `m` `\\,_pF_{q-1}` functions of `z`
    
    *series=2* uses a sum of `n` `\\,_qF_{p-1}` functions of `1/z`
    
    The default series is chosen based on the degree and `|z|` in order
    to be consistent with Mathematica's. This definition of the Meijer G-function
    has a discontinuity at `|z| = 1` for some orders, which can
    be avoided by explicitly specifying a series.
    
    Keyword arguments are forwarded to :func:`~mpmath.hypercomb`.
    
    **Examples**
    
    Many standard functions are special cases of the Meijer G-function
    (possibly rescaled and/or with branch cut corrections). We define
    some test parameters::
    
        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a = mpf(0.75)
        >>> b = mpf(1.5)
        >>> z = mpf(2.25)
    
    The exponential function:
    `e^z = G^{1,0}_{0,1} \\left( \\left. \\begin{matrix} - \\\\ 0 \\end{matrix} \\;
    \\right| \\; -z \\right)`
    
        >>> meijerg([[],[]], [[0],[]], -z)
        9.487735836358525720550369
        >>> exp(z)
        9.487735836358525720550369
    
    The natural logarithm:
    `\\log(1+z) = G^{1,2}_{2,2} \\left( \\left. \\begin{matrix} 1, 1 \\\\ 1, 0
    \\end{matrix} \\; \\right| \\; -z \\right)`
    
        >>> meijerg([[1,1],[]], [[1],[0]], z)
        1.178654996341646117219023
        >>> log(1+z)
        1.178654996341646117219023
    
    A rational function:
    `\\frac{z}{z+1} = G^{1,2}_{2,2} \\left( \\left. \\begin{matrix} 1, 1 \\\\ 1, 1
    \\end{matrix} \\; \\right| \\; z \\right)`
    
        >>> meijerg([[1,1],[]], [[1],[1]], z)
        0.6923076923076923076923077
        >>> z/(z+1)
        0.6923076923076923076923077
    
    The sine and cosine functions:
    
    `\\frac{1}{\\sqrt \\pi} \\sin(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left. \\begin{matrix}
    - \\\\ \\frac{1}{2}, 0 \\end{matrix} \\; \\right| \\; z \\right)`
    
    `\\frac{1}{\\sqrt \\pi} \\cos(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left. \\begin{matrix}
    - \\\\ 0, \\frac{1}{2} \\end{matrix} \\; \\right| \\; z \\right)`
    
        >>> meijerg([[],[]], [[0.5],[0]], (z/2)**2)
        0.4389807929218676682296453
        >>> sin(z)/sqrt(pi)
        0.4389807929218676682296453
        >>> meijerg([[],[]], [[0],[0.5]], (z/2)**2)
        -0.3544090145996275423331762
        >>> cos(z)/sqrt(pi)
        -0.3544090145996275423331762
    
    Bessel functions:
    
    `J_a(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left.
    \\begin{matrix} - \\\\ \\frac{a}{2}, -\\frac{a}{2}
    \\end{matrix} \\; \\right| \\; z \\right)`
    
    `Y_a(2 \\sqrt z) = G^{2,0}_{1,3} \\left( \\left.
    \\begin{matrix} \\frac{-a-1}{2} \\\\ \\frac{a}{2}, -\\frac{a}{2}, \\frac{-a-1}{2}
    \\end{matrix} \\; \\right| \\; z \\right)`
    
    `(-z)^{a/2} z^{-a/2} I_a(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left.
    \\begin{matrix} - \\\\ \\frac{a}{2}, -\\frac{a}{2}
    \\end{matrix} \\; \\right| \\; -z \\right)`
    
    `2 K_a(2 \\sqrt z) = G^{2,0}_{0,2} \\left( \\left.
    \\begin{matrix} - \\\\ \\frac{a}{2}, -\\frac{a}{2}
    \\end{matrix} \\; \\right| \\; z \\right)`
    
    As the example with the Bessel *I* function shows, a branch
    factor is required for some arguments when inverting the square root.
    
        >>> meijerg([[],[]], [[a/2],[-a/2]], (z/2)**2)
        0.5059425789597154858527264
        >>> besselj(a,z)
        0.5059425789597154858527264
        >>> meijerg([[],[(-a-1)/2]], [[a/2,-a/2],[(-a-1)/2]], (z/2)**2)
        0.1853868950066556941442559
        >>> bessely(a, z)
        0.1853868950066556941442559
        >>> meijerg([[],[]], [[a/2],[-a/2]], -(z/2)**2)
        (0.8685913322427653875717476 + 2.096964974460199200551738j)
        >>> (-z)**(a/2) / z**(a/2) * besseli(a, z)
        (0.8685913322427653875717476 + 2.096964974460199200551738j)
        >>> 0.5*meijerg([[],[]], [[a/2,-a/2],[]], (z/2)**2)
        0.09334163695597828403796071
        >>> besselk(a,z)
        0.09334163695597828403796071
    
    Error functions:
    
    `\\sqrt{\\pi} z^{2(a-1)} \\mathrm{erfc}(z) = G^{2,0}_{1,2} \\left( \\left.
    \\begin{matrix} a \\\\ a-1, a-\\frac{1}{2}
    \\end{matrix} \\; \\right| \\; z, \\frac{1}{2} \\right)`
    
        >>> meijerg([[],[a]], [[a-1,a-0.5],[]], z, 0.5)
        0.00172839843123091957468712
        >>> sqrt(pi) * z**(2*a-2) * erfc(z)
        0.00172839843123091957468712
    
    A Meijer G-function of higher degree, (1,1,2,3):
    
        >>> meijerg([[a],[b]], [[a],[b,a-1]], z)
        1.55984467443050210115617
        >>> sin((b-a)*pi)/pi*(exp(z)-1)*z**(a-1)
        1.55984467443050210115617
    
    A Meijer G-function of still higher degree, (4,1,2,4), that can
    be expanded as a messy combination of exponential integrals:
    
        >>> meijerg([[a],[2*b-a]], [[b,a,b-0.5,-1-a+2*b],[]], z)
        0.3323667133658557271898061
        >>> chop(4**(a-b+1)*sqrt(pi)*gamma(2*b-2*a)*z**a*\\
        ...     expint(2*b-2*a, -2*sqrt(-z))*expint(2*b-2*a, 2*sqrt(-z)))
        0.3323667133658557271898061
    
    In the following case, different series give different values::
    
        >>> chop(meijerg([[1],[0.25]],[[3],[0.5]],-2))
        -0.06417628097442437076207337
        >>> meijerg([[1],[0.25]],[[3],[0.5]],-2,series=1)
        0.1428699426155117511873047
        >>> chop(meijerg([[1],[0.25]],[[3],[0.5]],-2,series=2))
        -0.06417628097442437076207337
    
    **References**
    
    1. http://en.wikipedia.org/wiki/Meijer_G-function
    
    2. http://mathworld.wolfram.com/MeijerG-Function.html
    
    3. http://functions.wolfram.com/HypergeometricFunctions/MeijerG/
    
    4. http://functions.wolfram.com/HypergeometricFunctions/MeijerG1/
    
    """
_hypercomb_msg: str = '\nhypercomb() failed to converge to the requested %i bits of accuracy\nusing a working precision of %i bits. The function value may be zero or\ninfinite; try passing zeroprec=N or infprec=M to bound finite values between\n2^(-N) and 2^M. Otherwise try a higher maxprec or maxterms.\n'
