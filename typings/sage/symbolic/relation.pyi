def check_relation_maxima(relation):
    """
    Return ``True`` if this (in)equality is definitely true. Return ``False``
    if it is false or the algorithm for testing (in)equality is inconclusive.

    EXAMPLES::

        sage: from sage.symbolic.relation import check_relation_maxima
        sage: k = var('k')
        sage: pol = 1/(k-1) - 1/k -1/k/(k-1)
        sage: check_relation_maxima(pol == 0)
        True
        sage: f = sin(x)^2 + cos(x)^2 - 1
        sage: check_relation_maxima(f == 0)
        True
        sage: check_relation_maxima( x == x )
        True
        sage: check_relation_maxima( x != x )
        False
        sage: check_relation_maxima( x > x )
        False
        sage: check_relation_maxima( x^2 > x )
        False
        sage: check_relation_maxima( x + 2 > x )
        True
        sage: check_relation_maxima( x - 2 > x )
        False

    Here are some examples involving assumptions::

        sage: x, y, z = var('x, y, z')
        sage: assume(x>=y,y>=z,z>=x)
        sage: check_relation_maxima(x==z)
        True
        sage: check_relation_maxima(z<x)
        False
        sage: check_relation_maxima(z>y)
        False
        sage: check_relation_maxima(y==z)
        True
        sage: forget()
        sage: assume(x>=1,x<=1)
        sage: check_relation_maxima(x==1)
        True
        sage: check_relation_maxima(x>1)
        False
        sage: check_relation_maxima(x>=1)
        True
        sage: check_relation_maxima(x!=1)
        False
        sage: forget()
        sage: assume(x>0)
        sage: check_relation_maxima(x==0)
        False
        sage: check_relation_maxima(x>-1)
        True
        sage: check_relation_maxima(x!=0)
        True
        sage: check_relation_maxima(x!=1)
        False
        sage: forget()

    TESTS:

    Ensure that ``canonicalize_radical()`` and ``simplify_log`` are not
    used inappropriately, :issue:`17389`. Either one would simplify ``f``
    to zero below::

        sage: x,y = SR.var('x,y')
        sage: assume(y, 'complex')
        sage: f = log(x*y) - (log(x) + log(y))
        sage: f(x=-1, y=i)
        -2*I*pi
        sage: check_relation_maxima(f == 0)
        False
        sage: forget()

    Ensure that the ``sqrt(x^2)`` -> ``abs(x)`` simplification is not
    performed when testing equality::

        sage: assume(x, 'complex')
        sage: f = sqrt(x^2) - abs(x)
        sage: check_relation_maxima(f == 0)
        False
        sage: forget()

    If assumptions are made, ``simplify_rectform()`` is used::

        sage: assume(x, 'real')
        sage: f1 = ( e^(I*x) - e^(-I*x) ) / ( I*e^(I*x) + I*e^(-I*x) )
        sage: f2 = sin(x)/cos(x)
        sage: check_relation_maxima(f1 - f2 == 0)
        True
        sage: forget()

    But not if ``x`` itself is complex::

        sage: assume(x, 'complex')
        sage: f1 = ( e^(I*x) - e^(-I*x) ) / ( I*e^(I*x) + I*e^(-I*x) )
        sage: f2 = sin(x)/cos(x)
        sage: check_relation_maxima(f1 - f2 == 0)
        False
        sage: forget()

    If assumptions are made, then ``simplify_factorial()`` is used::

        sage: n,k = SR.var('n,k')
        sage: assume(n, 'integer')
        sage: assume(k, 'integer')
        sage: f1 = factorial(n+1)/factorial(n)
        sage: f2 = n + 1
        sage: check_relation_maxima(f1 - f2 == 0)
        True
        sage: forget()

    In case an equation is to be solved for non-integers, ''assume()''
    is used::

        sage: k = var('k')
        sage: assume(k,'noninteger')
        sage: solve([k^3==1],k)
        [k == 1/2*I*sqrt(3) - 1/2, k == -1/2*I*sqrt(3) - 1/2]
        sage: assumptions()
        [k is noninteger]
    """
def string_to_list_of_solutions(s):
    """
    Used internally by the symbolic solve command to convert the output
    of Maxima's solve command to a list of solutions in Sage's symbolic
    package.

    EXAMPLES:

    We derive the (monic) quadratic formula::

        sage: var('x,a,b')
        (x, a, b)
        sage: solve(x^2 + a*x + b == 0, x)
        [x == -1/2*a - 1/2*sqrt(a^2 - 4*b), x == -1/2*a + 1/2*sqrt(a^2 - 4*b)]

    Behind the scenes when the above is evaluated the function
    :func:`string_to_list_of_solutions` is called with input the
    string `s` below::

        sage: s = '[x=-(sqrt(a^2-4*b)+a)/2,x=(sqrt(a^2-4*b)-a)/2]'
        sage: sage.symbolic.relation.string_to_list_of_solutions(s)
         [x == -1/2*a - 1/2*sqrt(a^2 - 4*b), x == -1/2*a + 1/2*sqrt(a^2 - 4*b)]
    """
def solve(f, *args, explicit_solutions=None, multiplicities=None, to_poly_solve=None, solution_dict: bool = False, algorithm=None, domain=None):
    '''
    Algebraically solve an equation or system of equations (over the
    complex numbers) for given variables. Inequalities and systems
    of inequalities are also supported.

    INPUT:

    - ``f`` -- equation or system of equations (given by a list or tuple)

    - ``*args`` -- variables to solve for

    - ``solution_dict`` -- boolean (default: ``False``); if ``True`` or nonzero,
      return a list of dictionaries containing the solutions. If there
      are no solutions, return an empty list (rather than a list containing
      an empty dictionary). Likewise, if there\'s only a single solution,
      return a list containing one dictionary with that solution.

    There are a few optional keywords if you are trying to solve a single
    equation.  They may only be used in that context.

    - ``multiplicities`` -- boolean (default: ``False``); if True,
      return corresponding multiplicities.  This keyword is
      incompatible with ``to_poly_solve=True`` and does not make
      any sense when solving inequalities.

    - ``explicit_solutions`` -- boolean (default: ``False``); require that
      all roots be explicit rather than implicit. Not used
      when solving inequalities.

    - ``to_poly_solve`` -- boolean (default: ``False``) or string; use
      Maxima\'s ``to_poly_solver`` package to search for more possible
      solutions, but possibly encounter approximate solutions.
      This keyword is incompatible with ``multiplicities=True``
      and is not used when solving inequalities. Setting ``to_poly_solve``
      to \'force\' (string) omits Maxima\'s solve command (useful when
      some solutions of trigonometric equations are lost).

    - ``algorithm`` -- string (default: ``\'maxima\'``); to use SymPy\'s
      solvers set this to \'sympy\'. Note that SymPy is always used
      for diophantine equations. Another choice, if it is installed,
      is \'giac\'.

    - ``domain`` -- string (default: ``\'complex\'``); setting this to \'real\'
      changes the way SymPy solves single equations; inequalities
      are always solved in the real domain.

    EXAMPLES::

        sage: x, y = var(\'x, y\')
        sage: solve([x+y==6, x-y==4], x, y)
        [[x == 5, y == 1]]
        sage: solve([x^2+y^2 == 1, y^2 == x^3 + x + 1], x, y)
        [[x == -1/2*I*sqrt(3) - 1/2, y == -sqrt(-1/2*I*sqrt(3) + 3/2)],
         [x == -1/2*I*sqrt(3) - 1/2, y == sqrt(-1/2*I*sqrt(3) + 3/2)],
         [x == 1/2*I*sqrt(3) - 1/2, y == -sqrt(1/2*I*sqrt(3) + 3/2)],
         [x == 1/2*I*sqrt(3) - 1/2, y == sqrt(1/2*I*sqrt(3) + 3/2)],
         [x == 0, y == -1],
         [x == 0, y == 1]]
        sage: solve([sqrt(x) + sqrt(y) == 5, x + y == 10], x, y)
        [[x == -5/2*I*sqrt(5) + 5, y == 5/2*I*sqrt(5) + 5], [x == 5/2*I*sqrt(5) + 5, y == -5/2*I*sqrt(5) + 5]]
        sage: solutions = solve([x^2+y^2 == 1, y^2 == x^3 + x + 1], x, y, solution_dict=True)
        sage: for solution in solutions: print("{} , {}".format(solution[x].n(digits=3), solution[y].n(digits=3)))
        -0.500 - 0.866*I , -1.27 + 0.341*I
        -0.500 - 0.866*I , 1.27 - 0.341*I
        -0.500 + 0.866*I , -1.27 - 0.341*I
        -0.500 + 0.866*I , 1.27 + 0.341*I
        0.000 , -1.00
        0.000 , 1.00

    Whenever possible, answers will be symbolic, but with systems of
    equations, at times approximations will be given by Maxima, due to the
    underlying algorithm::

        sage: sols = solve([x^3==y,y^2==x], [x,y]); sols[-1], sols[0] # abs tol 1e-15
        ([x == 0, y == 0],
         [x == (0.3090169943749475 + 0.9510565162951535*I),
          y == (-0.8090169943749475 - 0.5877852522924731*I)])
        sage: sols[0][0].rhs().pyobject().parent()
        Complex Double Field

        sage: solve([y^6==y],y)
        [y == 1/4*sqrt(5) + 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4,
         y == -1/4*sqrt(5) + 1/4*I*sqrt(-2*sqrt(5) + 10) - 1/4,
         y == -1/4*sqrt(5) - 1/4*I*sqrt(-2*sqrt(5) + 10) - 1/4,
         y == 1/4*sqrt(5) - 1/4*I*sqrt(2*sqrt(5) + 10) - 1/4,
         y == 1,
         y == 0]
        sage: solve( [y^6 == y], y)==solve( y^6 == y, y)
        True

    Here we demonstrate very basic use of the optional keywords::

        sage: ((x^2-1)^2).solve(x)
        [x == -1, x == 1]
        sage: ((x^2-1)^2).solve(x,multiplicities=True)
        ([x == -1, x == 1], [2, 2])
        sage: solve(sin(x)==x,x)
        [x == sin(x)]
        sage: solve(sin(x)==x,x,explicit_solutions=True)
        []
        sage: solve(abs(1-abs(1-x)) == 10, x)
        [abs(abs(x - 1) - 1) == 10]
        sage: solve(abs(1-abs(1-x)) == 10, x, to_poly_solve=True)
        [x == -10, x == 12]

        sage: from sage.symbolic.expression import Expression
        sage: Expression.solve(x^2==1,x)
        [x == -1, x == 1]

    We must solve with respect to actual variables::

        sage: z = 5
        sage: solve([8*z + y == 3, -z +7*y == 0],y,z)
        Traceback (most recent call last):
        ...
        TypeError: 5 is not a valid variable

    If we ask for dictionaries containing the solutions, we get them::

        sage: solve([x^2-1],x,solution_dict=True)
        [{x: -1}, {x: 1}]
        sage: solve([x^2-4*x+4],x,solution_dict=True)
        [{x: 2}]
        sage: res = solve([x^2 == y, y == 4],x,y,solution_dict=True)
        sage: for soln in res: print("x: %s, y: %s" % (soln[x], soln[y]))
        x: 2, y: 4
        x: -2, y: 4

    If there is a parameter in the answer, that will show up as
    a new variable.  In the following example, ``r1`` is an arbitrary
    constant (because of the ``r``)::

        sage: forget()
        sage: x, y = var(\'x,y\')
        sage: solve([x+y == 3, 2*x+2*y == 6],x,y)
        [[x == -r1 + 3, y == r1]]

        sage: var(\'b, c\')
        (b, c)
        sage: solve((b-1)*(c-1), [b,c])
        [[b == 1, c == r...], [b == r..., c == 1]]

    Especially with trigonometric functions, the dummy variable may
    be implicitly an integer (hence the ``z``)::

        sage: solve( sin(x)==cos(x), x, to_poly_solve=True)
        [x == 1/4*pi + pi*z...]
        sage: solve([cos(x)*sin(x) == 1/2, x+y == 0],x,y)
        [[x == 1/4*pi + pi*z..., y == -1/4*pi - pi*z...]]

    Expressions which are not equations are assumed to be set equal
    to zero, as with `x` in the following example::

        sage: solve([x, y == 2],x,y)
        [[x == 0, y == 2]]

    If ``True`` appears in the list of equations it is
    ignored, and if ``False`` appears in the list then no
    solutions are returned. E.g., note that the first
    ``3==3`` evaluates to ``True``, not to a
    symbolic equation.

    ::

        sage: solve([3==3, 1.00000000000000*x^3 == 0], x)
        [x == 0]
        sage: solve([1.00000000000000*x^3 == 0], x)
        [x == 0]

    Here, the first equation evaluates to ``False``, so
    there are no solutions::

        sage: solve([1==3, 1.00000000000000*x^3 == 0], x)
        []

    Completely symbolic solutions are supported::

        sage: var(\'s,j,b,m,g\')
        (s, j, b, m, g)
        sage: sys = [ m*(1-s) - b*s*j, b*s*j-g*j ]
        sage: solve(sys,s,j)
        [[s == 1, j == 0], [s == g/b, j == (b - g)*m/(b*g)]]
        sage: solve(sys,(s,j))
        [[s == 1, j == 0], [s == g/b, j == (b - g)*m/(b*g)]]
        sage: solve(sys,[s,j])
        [[s == 1, j == 0], [s == g/b, j == (b - g)*m/(b*g)]]

        sage: z = var(\'z\')
        sage: solve((x-z)^2==2, x)
        [x == z - sqrt(2), x == z + sqrt(2)]

    Inequalities can be also solved::

        sage: solve(x^2>8,x)
        [[x < -2*sqrt(2)], [x > 2*sqrt(2)]]
        sage: x,y = var(\'x,y\'); (ln(x)-ln(y)>0).solve(x)
        [[log(x) - log(y) > 0]]
        sage: x,y = var(\'x,y\'); (ln(x)>ln(y)).solve(x)  # random
        [[0 < y, y < x, 0 < x]]
        [[y < x, 0 < y]]

    A simple example to show the use of the keyword
    ``multiplicities``::

        sage: ((x^2-1)^2).solve(x)
        [x == -1, x == 1]
        sage: ((x^2-1)^2).solve(x,multiplicities=True)
        ([x == -1, x == 1], [2, 2])
        sage: ((x^2-1)^2).solve(x,multiplicities=True,to_poly_solve=True)
        Traceback (most recent call last):
        ...
        NotImplementedError: to_poly_solve does not return multiplicities

    Here is how the ``explicit_solutions`` keyword functions::

        sage: solve(sin(x)==x,x)
        [x == sin(x)]
        sage: solve(sin(x)==x,x,explicit_solutions=True)
        []
        sage: solve(x*sin(x)==x^2,x)
        [x == 0, x == sin(x)]
        sage: solve(x*sin(x)==x^2,x,explicit_solutions=True)
        [x == 0]

    The following examples show the use of the keyword ``to_poly_solve``::

        sage: solve(abs(1-abs(1-x)) == 10, x)
        [abs(abs(x - 1) - 1) == 10]
        sage: solve(abs(1-abs(1-x)) == 10, x, to_poly_solve=True)
        [x == -10, x == 12]

        sage: var(\'Q\')
        Q
        sage: solve(Q*sqrt(Q^2 + 2) - 1, Q)
        [Q == 1/sqrt(Q^2 + 2)]

    The following example is a regression in Maxima 5.39.0.
    It used to be possible to get one more solution here,
    namely ``1/sqrt(sqrt(2) + 1)``, see
    https://sourceforge.net/p/maxima/bugs/3276/::

        sage: solve(Q*sqrt(Q^2 + 2) - 1, Q, to_poly_solve=True)
        [Q == -sqrt(-sqrt(2) - 1), Q == sqrt(sqrt(2) + 1)*(sqrt(2) - 1)]

    An effort is made to only return solutions that satisfy
    the current assumptions::

        sage: solve(x^2==4, x)
        [x == -2, x == 2]
        sage: assume(x<0)
        sage: solve(x^2==4, x)
        [x == -2]
        sage: solve((x^2-4)^2 == 0, x, multiplicities=True)
        ([x == -2], [2])
        sage: solve(x^2==2, x)
        [x == -sqrt(2)]
        sage: z = var(\'z\')
        sage: solve(x^2==2-z, x)
        [x == -sqrt(-z + 2)]
        sage: assume(x, \'rational\')
        sage: solve(x^2 == 2, x)
        []

    In some cases it may be worthwhile to directly use ``to_poly_solve``
    if one suspects some answers are being missed::

        sage: forget()
        sage: solve(cos(x)==0, x)
        [x == 1/2*pi]
        sage: solve(cos(x)==0, x, to_poly_solve=True)
        [x == 1/2*pi]
        sage: solve(cos(x)==0, x, to_poly_solve=\'force\')
        [x == 1/2*pi + pi*z...]

    The same may also apply if a returned unsolved expression has a
    denominator, but the original one did not::

        sage: solve(cos(x) * sin(x) == 1/2, x, to_poly_solve=True)
        [sin(x) == 1/2/cos(x)]
        sage: solve(cos(x) * sin(x) == 1/2, x, to_poly_solve=True, explicit_solutions=True)
        [x == 1/4*pi + pi*z...]
        sage: solve(cos(x) * sin(x) == 1/2, x, to_poly_solve=\'force\')
        [x == 1/4*pi + pi*z...]

    We use ``use_grobner`` in Maxima if no solution is obtained from
    Maxima\'s ``to_poly_solve``::

        sage: x,y = var(\'x y\')
        sage: c1(x,y) = (x-5)^2+y^2-16
        sage: c2(x,y) = (y-3)^2+x^2-9
        sage: solve([c1(x,y),c2(x,y)],[x,y])
        [[x == -9/68*sqrt(55) + 135/68, y == -15/68*sqrt(55) + 123/68],
         [x == 9/68*sqrt(55) + 135/68, y == 15/68*sqrt(55) + 123/68]]

    We use SymPy for Diophantine equations, see
    ``Expression.solve_diophantine``::

        sage: assume(x, \'integer\')
        sage: assume(z, \'integer\')
        sage: solve((x-z)^2==2, x)
        []

        sage: forget()

    The following shows some more of SymPy\'s capabilities that cannot be
    handled by Maxima::

        sage: _ = var(\'t\')
        sage: r = solve([x^2 - y^2/exp(x), y-1], x, y, algorithm=\'sympy\', solution_dict=True)
        sage: (r[0][x], r[0][y])
        (2*lambert_w(-1/2), 1)
        sage: solve(-2*x**3 + 4*x**2 - 2*x + 6 > 0, x, algorithm=\'sympy\')
        [x < 1/3*(1/2)^(1/3)*(9*sqrt(77) + 79)^(1/3) + 2/3*(1/2)^(2/3)/(9*sqrt(77) + 79)^(1/3) + 2/3]
        sage: solve(sqrt(2*x^2 - 7) - (3 - x),x,algorithm=\'sympy\')
        [x == -8, x == 2]
        sage: solve(sqrt(2*x + 9) - sqrt(x + 1) - sqrt(x + 4),x,algorithm=\'sympy\')
        [x == 0]
        sage: r = solve([x + y + z + t, -z - t], x, y, z, t, algorithm=\'sympy\', solution_dict=True)
        sage: (r[0][x], r[0][z])
        (-y, -t)
        sage: r = solve([x^2+y+z, y+x^2+z, x+y+z^2], x, y,z, algorithm=\'sympy\', solution_dict=True)
        sage: (r[0][x], r[0][y])
        (z, -(z + 1)*z)
        sage: (r[1][x], r[1][y])
        (-z + 1, -z^2 + z - 1)
        sage: solve(abs(x + 3) - 2*abs(x - 3),x,algorithm=\'sympy\',domain=\'real\')
        [x == 1, x == 9]

    We cannot translate all results from SymPy but we can at least
    print them::

        sage: solve(sinh(x) - 2*cosh(x),x,algorithm=\'sympy\')
        [ImageSet(Lambda(_n, I*(2*_n*pi + pi/2) + log(sqrt(3))), Integers),
         ImageSet(Lambda(_n, I*(2*_n*pi - pi/2) + log(sqrt(3))), Integers)]
        sage: solve(2*sin(x) - 2*sin(2*x), x,algorithm=\'sympy\')
        [ImageSet(Lambda(_n, 2*_n*pi), Integers),
         ImageSet(Lambda(_n, 2*_n*pi + pi), Integers),
         ImageSet(Lambda(_n, 2*_n*pi + 5*pi/3), Integers),
         ImageSet(Lambda(_n, 2*_n*pi + pi/3), Integers)]

        sage: solve(x^5 + 3*x^3 + 7, x, algorithm=\'sympy\')[0]
        x == complex_root_of(x^5 + 3*x^3 + 7, 0)

    A basic interface to Giac is provided::

        sage: # needs sage.libs.giac
        sage: solve([(2/3)^x-2], [x], algorithm=\'giac\')
        [-log(2)/(log(3) - log(2))]

        sage: # needs sage.libs.giac
        sage: f = (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) - (2*cos(x)*sin(x) - sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))
        sage: solve(f, x, algorithm=\'giac\')
        [-2*arctan(sqrt(2)), 0, 2*arctan(sqrt(2)), pi]

        sage: # needs sage.libs.giac
        sage: x, y = SR.var(\'x,y\')
        sage: solve([x+y-4,x*y-3],[x,y],algorithm=\'giac\')
        [[1, 3], [3, 1]]

    TESTS::

        sage: solve([sin(x)==x,y^2==x],x,y)
        [sin(x) == x, y^2 == x]
        sage: solve(0==1,x)
        []

    Test if the empty list is returned, too, when (a list of)
    dictionaries (is) are requested (:issue:`8553`)::

        sage: solve([SR(0)==1],x)
        []
        sage: solve([SR(0)==1],x,solution_dict=True)
        []
        sage: solve([x==1,x==-1],x)
        []
        sage: solve([x==1,x==-1],x,solution_dict=True)
        []
        sage: solve((x==1,x==-1),x,solution_dict=0)
        []

    Relaxed form, suggested by Mike Hansen (:issue:`8553`)::

        sage: solve([x^2-1],x,solution_dict=-1)
        [{x: -1}, {x: 1}]
        sage: solve([x^2-1],x,solution_dict=1)
        [{x: -1}, {x: 1}]
        sage: solve((x==1,x==-1),x,solution_dict=-1)
        []
        sage: solve((x==1,x==-1),x,solution_dict=1)
        []

    This inequality holds for any real ``x`` (:issue:`8078`)::

        sage: solve(x^4+2>0,x)
        [x < +Infinity]

    Test for user friendly input handling :issue:`13645`::

        sage: poly.<a,b> = PolynomialRing(RR)
        sage: solve([a+b+a*b == 1], a)
        Traceback (most recent call last):
        ...
        TypeError: a is not a valid variable
        sage: a,b = var(\'a,b\')
        sage: solve([a+b+a*b == 1], a)
        [a == -(b - 1)/(b + 1)]
        sage: solve([a, b], (1, a))
        Traceback (most recent call last):
        ...
        TypeError: 1 is not a valid variable
        sage: solve([x == 1], (1, a))
        Traceback (most recent call last):
        ...
        TypeError: 1 is not a valid variable
        sage: x.solve((1,2))
        Traceback (most recent call last):
        ...
        TypeError: 1 is not a valid variable

    Test that the original version of a system in the French Sage book
    now works (:issue:`14306`)::

        sage: var(\'y,z\')
        (y, z)
        sage: solve([x^2 * y * z == 18, x * y^3 * z == 24, x * y * z^4 == 6], x, y, z)
        [[x == 3, y == 2, z == 1],
         [x == (1.337215067... - 2.685489874...*I),
          y == (-1.700434271... + 1.052864325...*I),
          z == (0.9324722294... - 0.3612416661...*I)],
         ...]

    :issue:`13286` fixed::

        sage: solve([x-4], [x])
        [x == 4]

    Test for a list of non-symbolic expressions as first argument
    (:issue:`31714`)::

        sage: solve([1], x)
        Traceback (most recent call last):
        ...
        TypeError: must be a symbolic expression or a list of symbolic expressions

    Automatic computation of the variables to solve for::

        sage: var("x y")
        (x, y)
        sage: solve(x==1)
        [x == 1]
        sage: solve([x == 1, y == 2])  # random
        [[y == 2, x == 1]]
        sage: assert solve([x == 1, y == 2]) in ([[x == 1, y == 2]], [[y == 2, x == 1]])
        sage: solve([x == 1])
        [x == 1]
        sage: solve(x == 1)
        [x == 1]

    Special case::

        sage: solve([], [])
        [[]]

    Coverage test::

        sage: y = function(\'y\')(x)
        sage: solve([diff(y)==x, diff(y)==x], y)
        Traceback (most recent call last):
        ...
        TypeError: y(x) is not a valid variable
        sage: solve([0==1], x, multiplicities=True)
        ([], [])
        sage: solve([0==0], [], multiplicities=True)
        ([[]], [1])
        sage: var("x y")
        (x, y)
        sage: solve([x==1, y==2], [x, y], algorithm=\'sympy\', solution_dict=True)
        [{x: 1, y: 2}]
        sage: solve([x==1, y==2], [x, y], algorithm=\'sympy\')
        [[x == 1, y == 2]]
    '''
def solve_mod(eqns, modulus, solution_dict: bool = False):
    '''
    Return all solutions to an equation or list of equations modulo the
    given integer modulus. Each equation must involve only polynomials
    in 1 or many variables.

    By default the solutions are returned as `n`-tuples, where `n`
    is the number of variables appearing anywhere in the given
    equations. The variables are in alphabetical order.

    INPUT:

    - ``eqns`` -- equation or list of equations

    - ``modulus`` -- integer

    - ``solution_dict`` -- boolean (default: ``False``); if ``True`` or nonzero,
      return a list of dictionaries containing the solutions. If there
      are no solutions, return an empty list (rather than a list containing
      an empty dictionary). Likewise, if there\'s only a single solution,
      return a list containing one dictionary with that solution.

    EXAMPLES::

        sage: var(\'x,y\')
        (x, y)
        sage: solve_mod([x^2 + 2 == x, x^2 + y == y^2], 14)
        [(4, 2), (4, 6), (4, 9), (4, 13)]
        sage: solve_mod([x^2 == 1, 4*x  == 11], 15)
        [(14,)]

    Fermat\'s equation modulo 3 with exponent 5::

        sage: var(\'x,y,z\')
        (x, y, z)
        sage: solve_mod([x^5 + y^5 == z^5], 3)
        [(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 1, 2), (1, 2, 0), (2, 0, 2), (2, 1, 0), (2, 2, 1)]

    We can solve with respect to a bigger modulus if it consists only of small prime factors::

        sage: [d] = solve_mod([5*x + y == 3, 2*x - 3*y == 9], 3*5*7*11*19*23*29, solution_dict = True)
        sage: d[x]
        12915279
        sage: d[y]
        8610183

    For cases where there are relatively few solutions and the prime
    factors are small, this can be efficient even if the modulus itself
    is large::

        sage: sorted(solve_mod([x^2 == 41], 10^20))
        [(4538602480526452429,), (11445932736758703821,), (38554067263241296179,),
        (45461397519473547571,), (54538602480526452429,), (61445932736758703821,),
        (88554067263241296179,), (95461397519473547571,)]

    We solve a simple equation modulo 2::

        sage: x,y = var(\'x,y\')
        sage: solve_mod([x == y], 2)
        [(0, 0), (1, 1)]

    .. warning::

       The current implementation splits the modulus into prime
       powers, then naively enumerates all possible solutions
       (starting modulo primes and then working up through prime
       powers), and finally combines the solution using the Chinese
       Remainder Theorem.  The interface is good, but the algorithm is
       very inefficient if the modulus has some larger prime factors! Sage
       *does* have the ability to do something much faster in certain
       cases at least by using Groebner basis, linear algebra
       techniques, etc. But for a lot of toy problems this function as
       is might be useful. At least it establishes an interface.

    TESTS:

    Make sure that we short-circuit in at least some cases::

        sage: solve_mod([2*x==1], 2*next_prime(10^50))
        []

    Try multi-equation cases::

        sage: x, y, z = var("x y z")
        sage: solve_mod([2*x^2 + x*y, -x*y+2*y^2+x-2*y, -2*x^2+2*x*y-y^2-x-y], 12)
        [(0, 0), (4, 4), (0, 3), (4, 7)]
        sage: eqs = [-y^2+z^2, -x^2+y^2-3*z^2-z-1, -y*z-z^2-x-y+2, -x^2-12*z^2-y+z]
        sage: solve_mod(eqs, 11)
        [(8, 5, 6)]

    Confirm that modulus 1 now behaves as it should::

        sage: x, y = var("x y")
        sage: solve_mod([x==1], 1)
        [(0,)]
        sage: solve_mod([2*x^2+x*y, -x*y+2*y^2+x-2*y, -2*x^2+2*x*y-y^2-x-y], 1)
        [(0, 0)]
    '''
def solve_ineq_univar(ineq):
    """
    Function solves rational inequality in one variable.

    INPUT:

    - ``ineq`` -- inequality in one variable

    OUTPUT:

    - ``list`` -- output is list of solutions as a list of simple inequalities
      output [A,B,C] means (A or B or C) each A, B, C is again a list and
      if A=[a,b], then A means (a and b). The list is empty if there is no
      solution.

    EXAMPLES::

        sage: from sage.symbolic.relation import solve_ineq_univar
        sage: solve_ineq_univar(x-1/x>0)
        [[x > -1, x < 0], [x > 1]]

        sage: solve_ineq_univar(x^2-1/x>0)
        [[x < 0], [x > 1]]

        sage: solve_ineq_univar((x^3-1)*x<=0)
        [[x >= 0, x <= 1]]

    ALGORITHM:

    Calls Maxima command ``solve_rat_ineq``

    AUTHORS:

    - Robert Marik (01-2010)
    """
def solve_ineq_fourier(ineq, vars=None):
    """
    Solve system of inequalities using Maxima and Fourier elimination.

    Can be used for system of linear inequalities and for some types
    of nonlinear inequalities. For examples, see the example section
    below and http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/share/contrib/fourier_elim/rtest_fourier_elim.mac


    INPUT:

    - ``ineq`` -- list with system of inequalities

    - ``vars`` -- optionally list with variables for Fourier elimination

    OUTPUT:

    - ``list`` -- output is list of solutions as a list of simple inequalities
      output [A,B,C] means (A or B or C) each A, B, C is again a list and
      if A=[a,b], then A means (a and b). The list is empty if there is no
      solution.

    EXAMPLES::

        sage: from sage.symbolic.relation import solve_ineq_fourier
        sage: y = var('y')
        sage: solve_ineq_fourier([x+y<9,x-y>4],[x,y])
        [[y + 4 < x, x < -y + 9, y < (5/2)]]
        sage: solve_ineq_fourier([x+y<9,x-y>4],[y,x])[0][0](x=42)
        y < -33

        sage: solve_ineq_fourier([x^2>=0])
        [[x < +Infinity]]

        sage: solve_ineq_fourier([log(x)>log(y)],[x,y])
        [[y < x, 0 < y]]
        sage: solve_ineq_fourier([log(x)>log(y)],[y,x])
        [[0 < y, y < x, 0 < x]]

    Note that different systems will find default variables in different
    orders, so the following is not tested::

        sage: solve_ineq_fourier([log(x)>log(y)])  # random (one of the following appears)
        [[0 < y, y < x, 0 < x]]
        [[y < x, 0 < y]]

    ALGORITHM:

    Calls Maxima command ``fourier_elim``

    AUTHORS:

    - Robert Marik (01-2010)
    """
def solve_ineq(ineq, vars=None):
    """
    Solve inequalities and systems of inequalities using Maxima.
    Switches between rational inequalities
    (sage.symbolic.relation.solve_ineq_rational)
    and Fourier elimination (sage.symbolic.relation.solve_ineq_fouried).
    See the documentation of these functions for more details.

    INPUT:

    - ``ineq`` -- one inequality or a list of inequalities

      Case1: If ``ineq`` is one equality, then it should be rational
      expression in one variable. This input is passed to
      sage.symbolic.relation.solve_ineq_univar function.

      Case2: If ``ineq`` is a list involving one or more
      inequalities, than the input is passed to
      sage.symbolic.relation.solve_ineq_fourier function. This
      function can be used for system of linear inequalities and
      for some types of nonlinear inequalities. See
      http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/share/contrib/fourier_elim/rtest_fourier_elim.mac
      for a big gallery of problems covered by this algorithm.

    - ``vars`` -- (optional) parameter with list of variables. This list
      is used only if Fourier elimination is used. If omitted or if
      rational inequality is solved, then variables are determined
      automatically.

    OUTPUT:

    - ``list`` -- output is list of solutions as a list of simple inequalities
      output [A,B,C] means (A or B or C) each A, B, C is again a list and
      if A=[a,b], then A means (a and b).

    EXAMPLES::

        sage: from sage.symbolic.relation import solve_ineq

    Inequalities in one variable. The variable is detected automatically::

        sage: solve_ineq(x^2-1>3)
        [[x < -2], [x > 2]]

        sage: solve_ineq(1/(x-1)<=8)
        [[x < 1], [x >= (9/8)]]

    System of inequalities with automatically detected inequalities::

        sage: y = var('y')
        sage: solve_ineq([x-y<0,x+y-3<0],[y,x])
        [[x < y, y < -x + 3, x < (3/2)]]
        sage: solve_ineq([x-y<0,x+y-3<0],[x,y])
        [[x < min(-y + 3, y)]]

    Note that although Sage will detect the variables automatically,
    the order it puts them in may depend on the system, so the following
    command is only guaranteed to give you one of the above answers::

        sage: solve_ineq([x-y<0,x+y-3<0])  # random
        [[x < y, y < -x + 3, x < (3/2)]]

    ALGORITHM:

    Calls ``solve_ineq_fourier`` if inequalities are list and
    ``solve_ineq_univar`` of the inequality is symbolic expression. See
    the description of these commands for more details related to the
    set of inequalities which can be solved. The list is empty if
    there is no solution.

    AUTHORS:

    - Robert Marik (01-2010)
    """
