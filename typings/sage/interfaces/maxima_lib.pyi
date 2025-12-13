from .maxima_abstract import MaximaAbstract as MaximaAbstract, MaximaAbstractElement as MaximaAbstractElement, MaximaAbstractElementFunction as MaximaAbstractElementFunction, MaximaAbstractFunction as MaximaAbstractFunction, MaximaAbstractFunctionElement as MaximaAbstractFunctionElement
from _typeshed import Incomplete
from sage.env import MAXIMA_FAS as MAXIMA_FAS, MAXIMA_SHARE as MAXIMA_SHARE
from sage.libs.ecl import EclObject as EclObject, ecl_eval as ecl_eval
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.rings.number_field.number_field_element_base import NumberFieldElement_base as NumberFieldElement_base
from sage.structure.element import Expression as Expression
from sage.symbolic.expression import symbol_table as symbol_table
from sage.symbolic.operators import FDerivativeOperator as FDerivativeOperator, add_vararg as add_vararg, mul_vararg as mul_vararg
from sage.symbolic.ring import SR as SR

maxima_objdir: Incomplete
import_packages: str
init_code: Incomplete
maxima_eval: Incomplete
maxima_lib_instances: int
maxprint: Incomplete
meval: Incomplete
msetq: Incomplete
mlist: Incomplete
mequal: Incomplete
cadadr: Incomplete
max_integrate: Incomplete
max_sum: Incomplete
max_simplify_sum: Incomplete
max_prod: Incomplete
max_simplify_prod: Incomplete
max_ratsimp: Incomplete
max_limit: Incomplete
max_tlimit: Incomplete
max_plus: Incomplete
max_minus: Incomplete
max_use_grobner: Incomplete
max_to_poly_solve: Incomplete
max_at: Incomplete

def stdout_to_string(s):
    """
    Evaluate command ``s`` and catch Maxima stdout
    (not the result of the command!) into a string.

    INPUT:

    - ``s`` -- string; command to evaluate

    OUTPUT: string

    This is currently used to implement :meth:`~MaximaLibElement.display2d`.

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import stdout_to_string
        sage: stdout_to_string('1+1')
        ''
        sage: stdout_to_string('disp(1+1)')
        '2\\n\\n'
    """
def max_to_string(s):
    """
    Return the Maxima string corresponding to this ECL object.

    INPUT:

    - ``s`` -- ECL object

    OUTPUT: string

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, max_to_string
        sage: ecl = maxima_lib(cos(x)).ecl()
        sage: max_to_string(ecl)
        'cos(_SAGE_VAR_x)'
    """

my_mread: Incomplete

def parse_max_string(s):
    """
    Evaluate string in Maxima without *any* further simplification.

    INPUT:

    - ``s`` -- string

    OUTPUT: ECL object

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import parse_max_string
        sage: parse_max_string('1+1')
        <ECL: ((MPLUS) 1 1)>
    """

class MaximaLib(MaximaAbstract):
    """
    Interface to Maxima as a Library.

    OUTPUT: Maxima interface as a Library

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import MaximaLib, maxima_lib
        sage: isinstance(maxima_lib,MaximaLib)
        True

    Only one such interface can be instantiated::

        sage: MaximaLib()
        Traceback (most recent call last):
        ...
        RuntimeError: Maxima interface in library mode can only
        be instantiated once
    """
    def __init__(self) -> None:
        """
        Create an instance of the Maxima interpreter.
        See ``MaximaLib`` for full documentation.

        TESTS::

            sage: from sage.interfaces.maxima_lib import MaximaLib, maxima_lib
            sage: MaximaLib == loads(dumps(MaximaLib))
            True
            sage: maxima_lib == loads(dumps(maxima_lib))
            True

        We make sure labels are turned off (see :issue:`6816`)::

            sage: 'nolabels : true' in maxima_lib._MaximaLib__init_code
            True
        """
    def __reduce__(self):
        """
        Implement __reduce__ for ``MaximaLib``.

        OUTPUT: a couple consisting of:

        - the function to call for unpickling

        - a tuple of arguments for the function

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: maxima_lib.__reduce__()
            (<function reduce_load_MaximaLib at 0x...>, ())
        """
    eval: Incomplete
    def lisp(self, cmd):
        '''
        Send a lisp command to maxima.

        INPUT:

        - ``cmd`` -- string

        OUTPUT: ECL object

        .. NOTE::

           The output of this command is very raw - not pretty.

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: maxima_lib.lisp("(+ 2 17)")
            <ECL: 19>
        '''
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        INPUT:

        - ``var`` -- string

        - ``value`` -- string

        OUTPUT: none

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: maxima_lib.set('xxxxx', '2')
            sage: maxima_lib.get('xxxxx')
            '2'
        """
    def clear(self, var) -> None:
        """
        Clear the variable named var.

        INPUT:

        - ``var`` -- string

        OUTPUT: none

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: maxima_lib.set('xxxxx', '2')
            sage: maxima_lib.get('xxxxx')
            '2'
            sage: maxima_lib.clear('xxxxx')
            sage: maxima_lib.get('xxxxx')
            'xxxxx'
        """
    def get(self, var):
        """
        Get the string value of the variable ``var``.

        INPUT:

        - ``var`` -- string

        OUTPUT: string

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: maxima_lib.set('xxxxx', '2')
            sage: maxima_lib.get('xxxxx')
            '2'
        """
    def sr_integral(self, *args):
        '''
        Helper function to wrap calculus use of Maxima\'s integration.

        TESTS::

            sage: a,b=var(\'a,b\')
            sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
            Traceback (most recent call last):
            ...
            ValueError: Computation failed since Maxima requested additional
            constraints; using the \'assume\' command before evaluation
            *may* help (example of legal syntax is \'assume(a>0)\', see
            `assume?` for more details)
            Is a positive or negative?
            sage: assume(a>0)
            sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
            2/9*sqrt(3)*b^2*arctan(1/3*sqrt(3)*(2*(b*x + a)^(1/3) + a^(1/3))/a^(1/3))/a^(7/3) - 1/9*b^2*log((b*x + a)^(2/3) + (b*x + a)^(1/3)*a^(1/3) + a^(2/3))/a^(7/3) + 2/9*b^2*log((b*x + a)^(1/3) - a^(1/3))/a^(7/3) + 1/6*(4*(b*x + a)^(5/3)*b^2 - 7*(b*x + a)^(2/3)*a*b^2)/((b*x + a)^2*a^2 - 2*(b*x + a)*a^3 + a^4)
            sage: var(\'x, n\')
            (x, n)
            sage: integral(x^n,x)
            Traceback (most recent call last):
            ...
            ValueError: Computation failed since Maxima requested additional
            constraints; using the \'assume\' command before evaluation
            *may* help (example of legal syntax is \'assume(n>0)\',
            see `assume?` for more details)
            Is n equal to -1?
            sage: assume(n+1>0)
            sage: integral(x^n,x)
            x^(n + 1)/(n + 1)
            sage: forget()
            sage: assumptions()  # Check the assumptions really were forgotten
            []

        Make sure the abs_integrate package is being used,
        :issue:`11483`. The following are examples from the Maxima
        abs_integrate documentation::

            sage: integrate(abs(x), x)
            1/2*x*abs(x)

        ::

            sage: integrate(sgn(x) - sgn(1-x), x)  # known bug
            abs(x - 1) + abs(x)

        This is a known bug in Sage symbolic limits code, see
        :issue:`17892` and https://sourceforge.net/p/maxima/bugs/3237/ ::

            sage: integrate(1 / (1 + abs(x-5)), x, -5, 6) # not tested -- known bug
            log(11) + log(2)

        ::

            sage: integrate(1/(1 + abs(x)), x)  # known bug
            1/2*(log(x + 1) + log(-x + 1))*sgn(x) + 1/2*log(x + 1) - 1/2*log(-x + 1)

        ::

            sage: integrate(cos(x + abs(x)), x)  # known bug
            -1/2*x*sgn(x) + 1/4*(sgn(x) + 1)*sin(2*x) + 1/2*x

        The last example relies on the following simplification::

            sage: maxima("realpart(signum(x))")
            signum(x)

        An example from sage-support thread e641001f8b8d1129::

            sage: f = e^(-x^2/2)/sqrt(2*pi) * sgn(x-1)
            sage: integrate(f, x, -Infinity, Infinity)  # known bug
            -erf(1/2*sqrt(2))

        From :issue:`8624`::

            sage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))
            1/2

        ::

            sage: integrate(sqrt(x + sqrt(x)), x).canonicalize_radical()  # known bug
            1/12*((8*x - 3)*x^(1/4) + 2*x^(3/4))*sqrt(sqrt(x) + 1) + 1/8*log(sqrt(sqrt(x) + 1) + x^(1/4)) - 1/8*log(sqrt(sqrt(x) + 1) - x^(1/4))

        And :issue:`11594`::

            sage: integrate(abs(x^2 - 1), x, -2, 2)  # known bug
            4

        This definite integral returned zero (incorrectly) in at least
        Maxima 5.23. The correct answer is now given (:issue:`11591`)::

            sage: f = (x^2)*exp(x) / (1+exp(x))^2
            sage: integrate(f, (x, -infinity, infinity))
            1/3*pi^2

        The following integral was computed incorrectly in versions of
        Maxima before 5.27 (see :issue:`12947`)::

            sage: a = integrate(x*cos(x^3),(x,0,1/2)).n()
            sage: a.real()
            0.124756040961038
            sage: a.imag().abs() < 3e-17
            True
        '''
    def sr_sum(self, *args):
        """
        Helper function to wrap calculus use of Maxima's summation.

        TESTS:

        Check that :issue:`16224` is fixed::

            sage: k = var('k')
            sage: sum(x^(2*k)/factorial(2*k), k, 0, oo).canonicalize_radical()
            cosh(x)

        ::

            sage: x, y, k, n = var('x, y, k, n')
            sage: sum(binomial(n,k) * x^k * y^(n-k), k, 0, n)
            (x + y)^n
            sage: q, a = var('q, a')
            sage: sum(a*q^k, k, 0, oo)
            Traceback (most recent call last):
            ...
            ValueError: Computation failed since Maxima requested additional
            constraints; using the 'assume' command before evaluation *may* help
            (example of legal syntax is 'assume(abs(q)-1>0)', see `assume?`
            for more details)
            Is abs(q)-1 positive, negative or zero?
            sage: assume(q > 1)
            sage: sum(a*q^k, k, 0, oo)
            Traceback (most recent call last):
            ...
            ValueError: Sum is divergent.
            sage: forget()
            sage: assume(abs(q) < 1)
            sage: sum(a*q^k, k, 0, oo)
            -a/(q - 1)
            sage: forget()
            sage: assumptions() # check the assumptions were really forgotten
            []

        Taking the sum of all natural numbers informs us that the sum
        is divergent.  Maxima (before 5.29.1) used to ask questions
        about `m`, leading to a different error (see :issue:`11990`)::

            sage: m = var('m')
            sage: sum(m, m, 0, infinity)
            Traceback (most recent call last):
            ...
            ValueError: Sum is divergent.

        An error with an infinite sum in Maxima (before 5.30.0,
        see :issue:`13712`)::

            sage: n = var('n')
            sage: sum(1/((2*n-1)^2*(2*n+1)^2*(2*n+3)^2), n, 0, oo)
            3/256*pi^2

        Maxima correctly detects division by zero in a symbolic sum
        (see :issue:`11894`)::

            sage: sum(1/(m^4 + 2*m^3 + 3*m^2 + 2*m)^2, m, 0, infinity)
            Traceback (most recent call last):
            ...
            RuntimeError: ECL says: Zero to negative power computed.

        Similar situation for :issue:`12410`::

            sage: x = var('x')
            sage: sum(1/x*(-1)^x, x, 0, oo)
            Traceback (most recent call last):
            ...
            RuntimeError: ECL says: Zero to negative power computed.
        """
    def sr_prod(self, *args):
        """
        Helper function to wrap calculus use of Maxima's product.

        TESTS::

            sage: from sage.calculus.calculus import symbolic_product
            sage: _ = var('n')
            sage: symbolic_product(x,x,1,n)
            factorial(n)
            sage: symbolic_product(2*x,x,1,n)
            2^n*factorial(n)
        """
    def sr_limit(self, expr, v, a, dir=None):
        '''
        Helper function to wrap calculus use of Maxima\'s limits.

        TESTS::

            sage: f = (1+1/x)^x
            sage: limit(f,x = oo)
            e
            sage: limit(f,x = 5)
            7776/3125

        Domain to real, a regression in 5.46.0, see https://sf.net/p/maxima/bugs/4138 ::

            sage: maxima_calculus.eval("domain:real")
            ...
            sage: limit(f,x = 1.2).n()
            2.06961575467...
            sage: maxima_calculus.eval("domain:complex");
            ...
            sage: var(\'a\')
            a
            sage: limit(x^a,x=0)
            Traceback (most recent call last):
            ...
            ValueError: Computation failed since Maxima requested additional
            constraints; using the \'assume\' command before evaluation
            *may* help (example of legal syntax is \'assume(a>0)\', see `assume?`
            for more details)
            Is a positive, negative or zero?
            sage: assume(a>0)
            sage: limit(x^a,x=0)  # random - not needed for maxima 5.46.0
            Traceback (most recent call last):
            ...
            ValueError: Computation failed ...
            Is a an integer?
            sage: assume(a,\'integer\')
            sage: assume(a,\'even\')  # Yes, Maxima will ask this too
            sage: limit(x^a,x=0)
            0
            sage: forget()
            sage: assumptions() # check the assumptions were really forgotten
            []

        The second limit below was computed incorrectly prior to
        Maxima 5.24 (:issue:`10868`)::

            sage: f(n) = 2 + 1/factorial(n)
            sage: limit(f(n), n=infinity)
            2
            sage: limit(1/f(n), n=infinity)
            1/2

        The limit below was computed incorrectly prior to Maxima 5.30
        (see :issue:`13526`)::

            sage: n = var(\'n\')
            sage: l = (3^n + (-2)^n) / (3^(n+1) + (-2)^(n+1))
            sage: l.limit(n=oo)
            1/3

        The following limit computation used to incorrectly return 0
        or infinity, depending on the domain (see :issue:`15033`)::

            sage: m = sage.calculus.calculus.maxima
            sage: _ = m.eval(\'domain: real\')   # much faster than \'domain: complex\'
            sage: limit(gamma(x + 1/2)/(sqrt(x)*gamma(x)), x=infinity)
            1
            sage: _ = m.eval(\'domain: complex\')
        '''
    def sr_tlimit(self, expr, v, a, dir=None):
        """
        Helper function to wrap calculus use of Maxima's Taylor series limits.

        TESTS::

            sage: f = (1+1/x)^x
            sage: limit(f, x = I, taylor=True)
            (-I + 1)^I
        """

def is_MaximaLibElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`MaximaLibElement`.

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, is_MaximaLibElement
        sage: is_MaximaLibElement(1)
        doctest:...: DeprecationWarning: the function is_MaximaLibElement is deprecated; use isinstance(x, sage.interfaces.abc.MaximaLibElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: m = maxima_lib(1)
        sage: is_MaximaLibElement(m)
        True
    """

class MaximaLibElement(MaximaAbstractElement):
    """
    Element of Maxima through library interface.

    EXAMPLES:

    Elements of this class should not be created directly.
    The targeted parent should be used instead::

        sage: from sage.interfaces.maxima_lib import maxima_lib
        sage: maxima_lib(4)
        4
        sage: maxima_lib(log(x))
        log(_SAGE_VAR_x)
    """
    def ecl(self):
        """
        Return the underlying ECL object of this MaximaLib object.

        OUTPUT: ECL object

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: maxima_lib(x+cos(19)).ecl()
            <ECL: ((MPLUS SIMP) ((%COS SIMP) 19) |$_SAGE_VAR_x|)>
        """
    def to_poly_solve(self, vars, options: str = ''):
        '''
        Use Maxima\'s to_poly_solver package.

        INPUT:

        - ``vars`` -- symbolic expressions

        - ``options`` -- string (default="")

        OUTPUT: Maxima object

        EXAMPLES:

        The zXXX below are names for arbitrary integers and
        subject to change::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: sol = maxima_lib(sin(x) == 0).to_poly_solve(x)
            sage: sol.sage()
            [[x == pi*z...]]
        '''
    def display2d(self, onscreen: bool = True):
        """
        Return the 2d representation of this Maxima object.

        INPUT:

        - ``onscreen`` -- boolean (default: ``True``); whether to print or return

        OUTPUT:

        The representation is printed if onscreen is set to True
        and returned as a string otherwise.

        EXAMPLES::

            sage: from sage.interfaces.maxima_lib import maxima_lib
            sage: F = maxima_lib('x^5 - y^5').factor()
            sage: F.display2d()
                                   4      3    2  2    3      4
                       - (y - x) (y  + x y  + x  y  + x  y + x )
        """
MaximaLibFunctionElement = MaximaAbstractFunctionElement
MaximaLibFunction = MaximaAbstractFunction

class MaximaLibElementFunction(MaximaLibElement, MaximaAbstractElementFunction): ...

maxima_lib: Incomplete
maxima = maxima_lib

def reduce_load_MaximaLib():
    """
    Unpickle the (unique) Maxima library interface.

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import reduce_load_MaximaLib
        sage: reduce_load_MaximaLib()
        Maxima_lib
    """

car: Incomplete
cdr: Incomplete
caar: Incomplete
cadr: Incomplete
cddr: Incomplete
caddr: Incomplete
caaadr: Incomplete
NIL: Incomplete
lisp_length: Incomplete
sage_op_dict: Incomplete
max_op_dict: Incomplete

def sage_rat(x, y):
    """
    Return quotient x/y.

    INPUT:

    - ``x`` -- integer

    - ``y`` -- integer

    OUTPUT: rational

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import sage_rat
        sage: sage_rat(1,7)
        1/7
    """

mplus: Incomplete
mtimes: Incomplete
rat: Incomplete
ratdisrep: Incomplete
mrat: Incomplete
mqapply: Incomplete
max_li: Incomplete
max_psi: Incomplete
max_hyper: Incomplete
max_array: Incomplete
mdiff: Incomplete
max_lambert_w: Incomplete
max_harmo: Incomplete
max_pochhammer: Incomplete

def mrat_to_sage(expr):
    """
    Convert a Maxima MRAT expression to Sage SR.

    INPUT:

    - ``expr`` -- ECL object; a Maxima MRAT expression

    OUTPUT: symbolic expression

    Maxima has an optimised representation for multivariate
    rational expressions. The easiest way to translate those
    to SR is by first asking Maxima to give the generic representation
    of the object. That is what RATDISREP does in Maxima.

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, mrat_to_sage
        sage: var('x y z')
        (x, y, z)
        sage: c = maxima_lib((x+y^2+z^9)/x^6+z^8/y).rat()
        sage: c
        (_SAGE_VAR_y*_SAGE_VAR_z^9+_SAGE_VAR_x^6*_SAGE_VAR_z^8+_SAGE_VAR_y^3+_SAGE_VAR_x*_SAGE_VAR_y)/(_SAGE_VAR_x^6*_SAGE_VAR_y)
        sage: c.ecl()
        <ECL: ((MRAT SIMP (|$_SAGE_VAR_x| |$_SAGE_VAR_y| |$_SAGE_VAR_z|)
        ...>
        sage: mrat_to_sage(c.ecl())
        (x^6*z^8 + y*z^9 + y^3 + x*y)/(x^6*y)
    """
def mqapply_to_sage(expr):
    """
    Special conversion rule for MQAPPLY expressions.

    INPUT:

    - ``expr`` -- ECL object; a Maxima MQAPPLY expression

    OUTPUT: symbolic expression

    MQAPPLY is used for function as li[x](y) and psi[x](y).

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, mqapply_to_sage
        sage: c = maxima_lib('li[2](3)')
        sage: c.ecl()
        <ECL: ((MQAPPLY SIMP) (($LI SIMP ARRAY) 2) 3)>
        sage: mqapply_to_sage(c.ecl())
        dilog(3)
    """
def mdiff_to_sage(expr):
    """
    Special conversion rule for %DERIVATIVE expressions.

    INPUT:

    - ``expr`` -- ECL object; a Maxima %DERIVATIVE expression

    OUTPUT: symbolic expression

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, mdiff_to_sage
        sage: f = maxima_lib('f(x)').diff('x',4)
        sage: f.ecl()
        <ECL: ((%DERIVATIVE SIMP) (($F SIMP) $X) $X 4)>
        sage: mdiff_to_sage(f.ecl())
        diff(f(x), x, x, x, x)
    """
def mlist_to_sage(expr):
    '''
    Special conversion rule for MLIST expressions.

    INPUT:

    - ``expr`` -- ECL object; a Maxima MLIST expression (i.e., a list)

    OUTPUT: a Python list of converted expressions

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, mlist_to_sage
        sage: L=maxima_lib("[1,2,3]")
        sage: L.ecl()
        <ECL: ((MLIST SIMP) 1 2 3)>
        sage: mlist_to_sage(L.ecl())
        [1, 2, 3]
    '''
def max_at_to_sage(expr):
    '''
    Special conversion rule for AT expressions.

    INPUT:

    - ``expr`` -- ECL object; a Maxima AT expression

    OUTPUT: symbolic expression

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, max_at_to_sage
        sage: a=maxima_lib("\'at(f(x,y,z),[x=1,y=2,z=3])")
        sage: a
        \'at(f(x,y,z),[x = 1,y = 2,z = 3])
        sage: max_at_to_sage(a.ecl())
        f(1, 2, 3)
        sage: a=maxima_lib("\'at(f(x,y,z),x=1)")
        sage: a
        \'at(f(x,y,z),x = 1)
        sage: max_at_to_sage(a.ecl())
        f(1, y, z)
    '''
def dummy_integrate(expr):
    """
    We would like to simply tie Maxima's integrate to
    sage.calculus.calculus.dummy_integrate, but we're being
    imported there so to avoid circularity we define it here.

    INPUT:

    - ``expr`` -- ECL object; a Maxima %INTEGRATE expression

    OUTPUT: symbolic expression

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, dummy_integrate
        sage: f = maxima_lib('f(x)').integrate('x')
        sage: f.ecl()
        <ECL: ((%INTEGRATE SIMP) (($F SIMP) $X) $X)>
        sage: dummy_integrate(f.ecl())
        integrate(f(x), x)

    ::

        sage: f = maxima_lib('f(x)').integrate('x',0,10)
        sage: f.ecl()
        <ECL: ((%INTEGRATE SIMP) (($F SIMP) $X) $X 0 10)>
        sage: dummy_integrate(f.ecl())
        integrate(f(x), x, 0, 10)
    """
def max_harmonic_to_sage(expr):
    """
    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, max_to_sr
        sage: c=maxima_lib(harmonic_number(x,2))
        sage: c.ecl()
        <ECL: (($GEN_HARMONIC_NUMBER SIMP) 2 |$_SAGE_VAR_x|)>
        sage: max_to_sr(c.ecl())
        harmonic_number(x, 2)
    """
def max_pochhammer_to_sage(expr):
    """
    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, max_to_sr
        sage: c = maxima_lib('pochhammer(x,n)')
        sage: c.ecl()
        <ECL: (($POCHHAMMER SIMP) $X $N)>
        sage: max_to_sr(c.ecl())
        gamma(n + x)/gamma(x)
    """

special_max_to_sage: Incomplete
special_sage_to_max: Incomplete
sage_sym_dict: Incomplete
max_sym_dict: Incomplete
max_i: Incomplete

def pyobject_to_max(obj):
    """
    Convert a (simple) Python object into a Maxima object.

    INPUT:

    - ``expr`` -- Python object

    OUTPUT: ECL object

    .. NOTE::

       This uses functions defined in sage.libs.ecl.

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import pyobject_to_max
        sage: pyobject_to_max(4)
        <ECL: 4>
        sage: pyobject_to_max('z')
        <ECL: Z>
        sage: var('x')
        x
        sage: pyobject_to_max(x)
        Traceback (most recent call last):
        ...
        TypeError: Unimplemented type for python_to_ecl
    """
def sr_to_max(expr):
    """
    Convert a symbolic expression into a Maxima object.

    INPUT:

    - ``expr`` -- symbolic expression

    OUTPUT: ECL object

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import sr_to_max
        sage: var('x')
        x
        sage: sr_to_max(x)
        <ECL: $X>
        sage: sr_to_max(cos(x))
        <ECL: ((%COS) $X)>
        sage: f = function('f')(x)
        sage: sr_to_max(f.diff())
        <ECL: ((%DERIVATIVE) (($F) $X) $X 1)>

    TESTS:

    We should be able to convert derivatives evaluated at a point,
    :issue:`12796`::

        sage: from sage.interfaces.maxima_lib import sr_to_max, max_to_sr
        sage: f = function('f')
        sage: f_prime = f(x).diff(x)
        sage: max_to_sr(sr_to_max(f_prime(x = 1)))
        D[0](f)(1)
    """

max_to_pynac_table: Incomplete

def max_to_sr(expr):
    """
    Convert a Maxima object into a symbolic expression.

    INPUT:

    - ``expr`` -- ECL object

    OUTPUT: symbolic expression

    EXAMPLES::

        sage: from sage.interfaces.maxima_lib import maxima_lib, max_to_sr
        sage: f = maxima_lib('f(x)')
        sage: f.ecl()
        <ECL: (($F SIMP) $X)>
        sage: max_to_sr(f.ecl())
        f(x)

    TESTS::

        sage: from sage.interfaces.maxima_lib import sr_to_max, max_to_sr
        sage: f = function('f')(x).diff()
        sage: bool(max_to_sr(sr_to_max(f)) == f)
        True
    """
