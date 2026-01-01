r"""
Pexpect Interface to Giac

(You should prefer the cython interface: giacpy_sage and its libgiac command)

(adapted by F. Han from William Stein and Gregg Musiker maple's interface)

You must have the  Giac interpreter installed
and available as the command ``giac`` in your PATH in
order to use this interface. You need a giac version
supporting "giac --sage" ( roughly after 0.9.1 ). In this case you do not have
to install any  optional Sage packages. If giac is not already installed, you can
download binaries or sources or spkg (follow the sources link) from the homepage:

Homepage <https://www-fourier.ujf-grenoble.fr/~parisse/giac.html>

Type ``giac.[tab]`` for a list of all the functions
available from your Giac install. Type
``giac.[tab]?`` for Giac's help about a given
function. Type ``giac(...)`` to create a new Giac
object, and ``giac.eval(...)`` to run a string using
Giac (and get the result back as a string).

If the giac spkg is installed, you should find the full html documentation there::

    $SAGE_LOCAL/share/giac/doc/en/cascmd_local/index.html

EXAMPLES::

    sage: giac('3 * 5')
    15
    sage: giac.eval('ifactor(2005)')
    '5*401'
    sage: giac.ifactor(2005)
    2005
    sage: l=giac.ifactors(2005) ; l; l[2]
    [5,1,401,1]
    401
    sage: giac.fsolve('x^2=cos(x)+4', 'x','0..5')
    [1.9140206190...
    sage: giac.factor('x^4 - y^4')
    (x-y)*(x+y)*(x^2+y^2)
    sage: R.<x,y>=QQ[];f=(x+y)^5;f2=giac(f);(f-f2).normal()
    0
    sage: x,y=giac('x,y'); giac.int(y/(cos(2*x)+cos(x)),x)     # random
    y*2*((-(tan(x/2)))/6+(-2*1/6/sqrt(3))*ln(abs(6*tan(x/2)-2*sqrt(3))/abs(6*tan(x/2)+2*sqrt(3))))


If the string "error" (case insensitive) occurs in the output of
anything from Giac, a :exc:`RuntimeError` exception is raised.

Tutorial
--------

AUTHORS:

- Gregg Musiker (2006-02-02): initial version.

- Frederic Han: adapted to giac.

- Marcelo Forets (2017-04-06): conversions and cleanup.

This tutorial is based on the Maple Tutorial for number theory from
http://www.math.mun.ca/~drideout/m3370/numtheory.html.

Syntax
~~~~~~~

There are several ways to use the Giac Interface in Sage. We will
discuss two of those ways in this tutorial.


#. If you have a giac expression such as

   ::

       factor( (x^4-1));

   We can write that in sage as

   ::

       sage: giac('factor(x^4-1)')
       (x-1)*(x+1)*(x^2+1)

   Notice, there is no need to use a semicolon.

#. Since Sage is written in Python, we can also import giac
   commands and write our scripts in a pythonic way. For example,
   ``factor()`` is a giac command, so we can also factor
   in Sage using

   ::

       sage: giac('(x^4-1)').factor()
       (x-1)*(x+1)*(x^2+1)

   where ``expression.command()`` means the same thing as
   ``command(expression)`` in Giac. We will use this
   second type of syntax whenever possible, resorting to the first
   when needed.

   ::

       sage: giac('(x^12-1)/(x-1)').normal()
       x^11+x^10+x^9+x^8+x^7+x^6+x^5+x^4+x^3+x^2+x+1

Some typical input
~~~~~~~~~~~~~~~~~~

The normal command will reduce a rational function to the
lowest terms. In giac, simplify is slower than normal because it
tries more sophisticated simplifications (ex algebraic extensions)
The factor command will factor a polynomial with
rational coefficients into irreducible factors over the ring of
integers (if your default configuration of giac (cf .xcasrc) has not
allowed square roots). So for example,


::

    sage: giac('(x^12-1)').factor( )
    (x-1)*(x+1)*(x^2+1)*(x^2-x+1)*(x^2+x+1)*(x^4-x^2+1)

::

    sage: giac('(x^28-1)').factor( )
    (x-1)*(x+1)*(x^2+1)*(x^6-x^5+x^4-x^3+x^2-x+1)*(x^6+x^5+x^4+x^3+x^2+x+1)*(x^12-x^10+x^8-x^6+x^4-x^2+1)

Giac console
~~~~~~~~~~~~~

Another important feature of giac is its online help. We can
access this through sage as well. After reading the description of
the command, you can press :kbd:`q` to immediately get back to your
original prompt.

Incidentally you can always get into a giac console by the
command ::

    sage: giac.console()                       # not tested
    sage: !giac                                # not tested

Note that the above two commands are slightly different, and the
first is preferred.

For example, for help on the giac command factors, we type ::

    sage: giac.help('factors')                     # not tested

::

    sage: alpha = giac((1+sqrt(5))/2)
    sage: beta = giac(1-sqrt(5))/2
    sage: f19  = alpha^19 - beta^19/sqrt(5)
    sage: f19
    (sqrt(5)/2+1/2)^19-((-sqrt(5)+1)/2)^19/sqrt(5)
    sage: (f19-(5778*sqrt(5)+33825)/5).normal()
    0

Function definitions
~~~~~~~~~~~~~~~~~~~~

Let's say we want to write a giac program now that squares a
number if it is positive and cubes it if it is negative. In giac,
that would look like

::

    mysqcu := proc(x)
    if x > 0 then x^2;
    else x^3; fi;
    end;

In Sage, we write

::

    sage: mysqcu = giac('proc(x) if x > 0 then x^2 else x^3 fi end')
    sage: mysqcu(5)
    25
    sage: mysqcu(-5)
    -125

More complicated programs should be put in a separate file and
loaded.

Conversions
~~~~~~~~~~~~

The ``GiacElement.sage()`` method tries to convert a Giac object to a Sage
object. In many cases, it will just work. In particular, it should be able to
convert expressions entirely consisting of:

- numbers, i.e. integers, floats, complex numbers;
- functions and named constants also present in Sage, where Sage knows how to
  translate the function or constant's name from Giac's
- symbolic variables whose names don't pathologically overlap with
  objects already defined in Sage.

This method will not work when Giac's output includes functions unknown to Sage.

If you want to convert more complicated Giac expressions, you can
instead call ``GiacElement._sage_()`` and supply a translation dictionary::

    sage: g = giac('NewFn(x)')
    sage: g._sage_(locals={('NewFn', 1): sin})
    sin(x)

Moreover, new conversions can be permanently added using Pynac's
``register_symbol``, and this is the recommended approach for library code.
For more details, see the documentation for ``._sage_()``.

TESTS:

Test that conversion of symbolic functions with latex names works (:issue:`31047`)::

    sage: var('phi')
    phi
    sage: function('Cp', latex_name='C_+')
    Cp
    sage: test = Cp(phi)._giac_()._sage_()
    sage: test.operator() == Cp
    True
    sage: test.operator()._latex_() == 'C_+'
    True
"""
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import DOT_SAGE as DOT_SAGE
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement, gc_disabled as gc_disabled
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.pager import pager as pager
from sage.structure.richcmp import rich_to_bool as rich_to_bool

COMMANDS_CACHE: str

class Giac(Expect):
    """
    Interface to the Giac interpreter.

    You must have the optional  Giac interpreter installed and available as the command ``giac`` in your PATH in order to use this interface. Try the command: print(giac._install_hints()) for more informations on giac installation.

    Type ``giac.[tab]`` for a list of all the functions available from your Giac install.
    Type ``giac.[tab]?`` for Giac's help about a given function.
    Type ``giac(...)`` to create a new Giac object.

    Full html documentation for giac is available from your giac installation at ``$PREFIX``/share/giac/doc/en/cascmd_en/index.html

    EXAMPLES:

    Any Giac instruction can be evaluated as a string by the giac command. You can access the giac functions by adding the ``giac.`` prefix to the usual Giac name.

    ::

      sage: l=giac('normal((y+sqrt(2))^4)'); l
      y^4+4*sqrt(2)*y^3+12*y^2+8*sqrt(2)*y+4
      sage: f=giac('(u,v)->{ if (u<v){ [u,v] } else { [v,u] }}');f(1,2),f(3,1)
      ([1,2], [1,3])

    The output of the giac command is a Giac object, and it can be used for another giac command.

    ::

      sage: l.factors()
      [y+sqrt(2),4]
      sage: giac('(x^12-1)').factor( )
      (x-1)*(x+1)*(x^2+1)*(x^2-x+1)*(x^2+x+1)*(x^4-x^2+1)
      sage: giac('assume(y>0)'); giac('y^2=3').solve('y')
      y
      ...[sqrt(3)]

    You can create some Giac elements and avoid many quotes like this:

    ::

      sage: x,y,z=giac('x,y,z');type(y)
      <class 'sage.interfaces.giac.GiacElement'>
      sage: I1=(1/(cos(2*y)+cos(y))).integral(y,0,pi/4).simplify()
      sage: (I1-((-2*ln((sqrt(3)-3*tan(1/8*pi))/(sqrt(3)+3*tan(1/8*pi)))*sqrt(3)-3*tan(1/8*pi))/9)).normal()
      0
      sage: ((y+z*sqrt(5))*(y-sqrt(5)*z)).normal()
      y^2-5*z^2

    Polynomials or elements of SR can be evaluated directly by the giac interface.

    ::

      sage: R.<a,b> = QQ[]; f = (2+a+b)
      sage: p = giac.gcd(f^3+5*f^5,f^2+f^5); p; R(p.sage())
      sageVARa^2+2*sageVARa*sageVARb+4*sageVARa+sageVARb^2+4*sageVARb+4
      a^2 + 2*a*b + b^2 + 4*a + 4*b + 4

    Variable names in python and giac are independent::

        sage: a=sqrt(2);giac('Digits:=30;a:=5');a,giac('a'),giac(a),giac(a).evalf()
        30
        (sqrt(2), 5, sqrt(2), 1.41421356237309504880168872421)

    TESTS::

        sage: g = giac('euler_gamma').sage();g
        euler_gamma
        sage: g.n()
        0.577215664901533
    """
    def __init__(self, maxread=None, script_subdirectory=None, server=None, server_tmpdir=None, logfile=None) -> None:
        """
        Create an instance of the Giac interpreter.

        EXAMPLES::

            sage: from sage.interfaces.giac import giac
            sage: giac == loads(dumps(giac))
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: Giac().__reduce__()
            (<function reduce_load_Giac at 0x...>, ())
            sage: f, args = _
            sage: f(*args)
            Giac
        """
    def expect(self):
        """
        Return the pexpect object for this Giac session.

        EXAMPLES::

            sage: m = Giac()
            sage: m.expect() is None
            True
            sage: m._start()
            sage: m.expect()
            Giac with PID ... running .../giac --sage
            sage: m.quit()
        """
    def console(self) -> None:
        """
        Spawn a new Giac command-line session.

        EXAMPLES::

            sage: giac_console()                   # not tested - giac
            ...
            Homepage http://www-fourier.ujf-grenoble.fr/~parisse/giac.html
            Released under the GPL license 3.0 or above
            See http://www.gnu.org for license details
            -------------------------------------------------
            Press CTRL and D simultaneously to finish session
            Type ?commandname for help
            0>>
        """
    def completions(self, s):
        """
        Return all commands that complete the command starting with the
        string s.

        EXAMPLES::

            sage: c = giac.completions('cas')
            sage: 'cas_setup' in c
            True
        """
    def cputime(self, t=None):
        """
        Return the amount of CPU time that the Giac session has used.

        If ``t`` is not None, then it returns the difference
        between the current CPU time and ``t``.

        EXAMPLES::

            sage: t = giac.cputime()
            sage: t                     # random
            0.02
            sage: x = giac('x')
            sage: giac.diff(x^2, x)
            2*x
            sage: giac.cputime(t)       # random
            0.0
        """
    def eval(self, code, strip: bool = True, **kwds):
        '''
        Send the code x to the Giac interpreter.
        Remark: To enable multi-lines codes in the notebook magic mode: ``%giac``,
        the ``\\n`` are removed before sending the code to giac.

        INPUT:

        - ``code`` -- str
        - ``strip`` -- default is ``True`` and removes ``\\n``

        EXAMPLES::

            sage: giac.eval("2+2;\\n3")
            \'4,3\'
            sage: giac.eval("2+2;\\n3",False)
            \'4\\n3\'
            sage: s=\'g(x):={\\nx+1;\\nx+2;\\n}\'
            sage: giac(s)
            ...x+1...x+2...
            sage: giac.g(5)
            7
        '''
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: giac.set('xx', '2')
            sage: giac.get('xx')
            '2'
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: giac.set('xx', '2')
            sage: giac.get('xx')
            '2'
        """
    def help(self, string) -> None:
        '''
        Display Giac help about string.

        This is the same as typing "?string" in the Giac console.

        INPUT:

        - ``string`` -- string to search for in the giac help system

        EXAMPLES::

            sage: giac.help(\'Psi\')         # not tested - depends of giac and $LANG
            Psi(a,n)=nth-derivative of the function DiGamma (=ln@Gamma) at point a (Psi(a,0)=Psi(a))...
        '''
    def clear(self, var) -> None:
        """
        Clear the variable named var.

        EXAMPLES::

            sage: giac.set('xx', '2')
            sage: giac.get('xx')
            '2'
            sage: giac.clear('xx')
            sage: giac.get('xx')
            'xx'
        """
    def version(self):
        '''
        Wrapper for giac\'s version().

        EXAMPLES::

            sage: giac.version()
            "giac...
        '''

class GiacFunction(ExpectFunction): ...
class GiacFunctionElement(FunctionElement): ...

class GiacElement(ExpectElement):
    def __float__(self) -> float:
        """
        Return a floating point version of ``self``.

        EXAMPLES::

            sage: float(giac(1/2))
            0.5
            sage: type(_)
            <class 'float'>
        """
    def unapply(self, var):
        """
        Create a Giac function in the given arguments from a Giac symbol.

        EXAMPLES::

            sage: f=giac('y^3+1+t')
            sage: g=(f.unapply('y,t'))
            sage: g
            (y,t)->y^3+1+t
            sage: g(1,2)
            4
        """
    def __hash__(self):
        """
        Return an integer representing the hash of ``self``.

        These examples are optional, and require Giac to be installed. You
        do not need to install any Sage packages for this.

        EXAMPLES::

            sage: m = giac('x^2+y^2')
            sage: hash(m)              # random
            4614285348919569149
        """
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: len(giac([1,2,3]))
            3
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: l = giac([1,2,3])
            sage: list(iter(l))
            [1, 2, 3]
        """
    def __del__(self) -> None:
        """
        Note that clearing object is pointless since it wastes time.
        (Ex: otherwise doing a=0 after a = (giac('x+y+z')^40).normal() is very slow )

        EXAMPLES::

            sage: a = giac(2)
            sage: a.__del__()
            sage: a
            2
            sage: del a
            sage: a
            Traceback (most recent call last):
            ...
            NameError: name 'a' is not defined
        """
    def integral(self, var: str = 'x', min=None, max=None):
        """
        Return the integral of ``self`` with respect to the variable `x`.

        INPUT:

        - ``var`` -- variable

        - ``min`` -- (default: ``None``)

        - ``max`` -- (default: ``None``)

        This returns the definite integral if xmin is not ``None``, otherwise
        an indefinite integral.

        EXAMPLES::

            sage: y=giac('y');f=(sin(2*y)/y).integral(y).simplify(); f
            Si(2*y)
            sage: f.diff(y).simplify()
            sin(2*y)/y

        ::

            sage: f = giac('exp(x^2)').integral('x',0,1) ; f
            1.46265174...
            sage: x,y=giac('x'),giac('y');integrate(cos(x+y),'x=0..pi').simplify()
            -2*sin(y)
        """
    integrate = integral
    def sum(self, var, min=None, max=None):
        """
        Return the sum of ``self`` with respect to the variable `x`.

        INPUT:

        - ``var`` -- variable

        - ``min`` -- (default: ``None``)

        - ``max`` -- (default: ``None``)

        This returns the definite integral if xmin is not ``None``, otherwise
        an indefinite integral.

        EXAMPLES::

            sage: giac('1/(1+k^2)').sum('k',-oo,+infinity).simplify()
            (pi*exp(pi)^2+pi)/(exp(pi)^2-1)
        """

giac: Giac

def reduce_load_Giac():
    """
    Return the giac object created in sage.interfaces.giac.

    EXAMPLES::

        sage: from sage.interfaces.giac import reduce_load_Giac
        sage: reduce_load_Giac()
        Giac
    """
def giac_console() -> None:
    """
    Spawn a new Giac command-line session.

    EXAMPLES::

        sage: giac.console()  # not tested - giac
        ...
        Homepage http://www-fourier.ujf-grenoble.fr/~parisse/giac.html
        Released under the GPL license 3.0 or above
        See http://www.gnu.org for license details
        -------------------------------------------------
        Press CTRL and D simultaneously to finish session
        Type ?commandname for help
    """
