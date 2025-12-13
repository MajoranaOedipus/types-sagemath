from _typeshed import Incomplete
from sage.interfaces.interface import Interface as Interface, InterfaceElement as InterfaceElement, InterfaceFunction as InterfaceFunction, InterfaceFunctionElement as InterfaceFunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.richcmp import rich_to_bool as rich_to_bool

class Mathics(Interface):
    """
    Interface to the Mathics interpreter.

    Implemented according to the Mathematica interface but avoiding Pexpect
    functionality.

    EXAMPLES::

        sage: # optional - mathics
        sage: t = mathics('Tan[I + 0.5]')
        sage: t.parent()
        Mathics
        sage: ts = t.sage()
        sage: ts.parent()
        Complex Field with 53 bits of precision
        sage: t == mathics(ts)
        True
        sage: mtan = mathics.Tan
        sage: mt = mtan(I+1/2)
        sage: mt == t
        True
        sage: u = mathics(I+1/2)
        sage: u.Tan() == mt
        True


    More examples can be found in the module header.
    """
    def __init__(self, maxread=None, logfile=None, init_list_length: int = 1024, seed=None) -> None:
        """
        Python constructor.

        EXAMPLES::

            sage: mathics._mathics_init_ == mathics._mathematica_init_
            True
        """
    def eval(self, code, *args, **kwds):
        """
        Evaluates a command inside the Mathics interpreter and returns the output
        in printable form.

        EXAMPLES::

            sage: mathics.eval('1+1')  # optional - mathics
            '2'
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: mathics.set('u', '2*x +E')         # optional - mathics
            sage: bool(mathics('u').sage() == 2*x+e) # optional - mathics
            True
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: mathics.set('u', '2*x +E')        # optional - mathics
            sage: mathics.get('u')                  # optional - mathics
            '2 x + E'
        """
    def chdir(self, dir) -> None:
        """
        Change Mathics's current working directory.

        EXAMPLES::

            sage: mathics.chdir('/')          # optional - mathics
            sage: mathics('Directory[]')      # optional - mathics
            /
        """
    def console(self) -> None:
        """
        Spawn a new Mathics command-line session.

        EXAMPLES::

            sage: mathics.console()  # not tested

            Mathics 2.1.1.dev0
            on CPython 3.9.2 (default, Mar 19 2021, 22:23:28)
            using SymPy 1.7, mpmath 1.2.1, numpy 1.19.5, cython 0.29.21

            Copyright (C) 2011-2021 The Mathics Team.
            This program comes with ABSOLUTELY NO WARRANTY.
            This is free software, and you are welcome to redistribute it
            under certain conditions.
            See the documentation for the full license.

            Quit by evaluating Quit[] or by pressing CONTROL-D.

            In[1]:= Sin[0.5]
            Out[1]= 0.479426

            Goodbye!

            sage:
        """
    def help(self, cmd, long: bool = False):
        """
        Return the Mathics documentation of the given command.

        EXAMPLES::

            sage: mathics.help('Sin')                   # optional - mathics
            'sine function\\n'

            sage: print(_)                              # optional - mathics
            sine function
            <BLANKLINE>

            sage: print(mathics.help('Sin', long=True)) # optional - mathics
            sine function
            <BLANKLINE>
            Attributes[Sin] = {Listable, NumericFunction, Protected}
            <BLANKLINE>

            sage: print(mathics.Factorial.__doc__)  # optional - mathics
            factorial
            <BLANKLINE>

            sage: u = mathics('Pi')                 # optional - mathics
            sage: print(u.Cos.__doc__)              # optional - mathics
            cosine function
            <BLANKLINE>
        """
    def __getattr__(self, attrname):
        """
        EXAMPLES::

            sage: msin = mathics.Sin           # optional - mathics
            sage: msin(0.2)                    # optional - mathics
            0.19866933079506123
            sage: _ == sin(0.2)                # optional - mathics
            True
        """

class MathicsElement(ExtraTabCompletion, InterfaceElement):
    """
    Element class of the Mathics interface.

    Its instances are usually constructed via the instance call of its parent.
    It wrapes the Mathics library for this object. In a session Mathics methods
    can be obtained using tab completion.

    EXAMPLES::

        sage: # optional - mathics
        sage: me=mathics(e); me
        E
        sage: type(me)
        <class 'sage.interfaces.mathics.MathicsElement'>
        sage: P = me.parent(); P
        Mathics
        sage: type(P)
        <class 'sage.interfaces.mathics.Mathics'>

    Access to the Mathics expression objects::

        sage: # optional - mathics
        sage: res = me._mathics_result
        sage: type(res)
        <class 'mathics.core.evaluation.Result'>
        sage: expr = res.last_eval; expr
        <Symbol: System`E>
        sage: type(expr)
        <class 'mathics.core.symbols.Symbol'>

    Applying Mathics methods::

        sage: # optional - mathics
        sage: me.to_sympy()
        E
        sage: me.get_name()
        'System`E'
        sage: me.is_inexact()
        False

    Conversion to Sage::

        sage: bool(me.sage() == e)             # optional - mathics
        True
    """
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: l = mathics('{1, x, .15}')  # optional - mathics
            sage: l[0]                        # optional - mathics
            List
            sage: for i in l: print(i)        # optional - mathics
            1
            x
            0.15
        """
    def __getattr__(self, attrname):
        """
        EXAMPLES::

            sage: # optional - mathics
            sage: a = mathics(5*x)
            sage: res = a._mathics_result
            sage: str(a) == res.result
            True
            sage: t = mathics._eval('5*x')
            sage: t.last_eval  == res.last_eval
            True
        """
    def __float__(self, precision: int = 16) -> float:
        """
        EXAMPLES::

            sage: float(mathics('Pi')) == float(pi)  # optional - mathics
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: mpol = mathics('x + y*z')     # optional - mathics
            sage: loads(dumps(mpol)) == mpol    # optional - mathics
            True
        """
    def __len__(self) -> int:
        """
        Return the object's length, evaluated by mathics.

        EXAMPLES::

            sage: len(mathics([1,1.,2]))    # optional - mathics
            3
        """
    def save_image(self, filename, ImageSize: int = 600) -> None:
        """
        Save a mathics graphics.

        INPUT:

        - ``filename`` -- string; the filename to save as. The
          extension determines the image file format

        - ``ImageSize`` -- integer; the size of the resulting image

        EXAMPLES::

            sage: P = mathics('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathics
            sage: filename = tmp_filename()                  # optional - mathics
            sage: P.save_image(filename, ImageSize=800)      # optional - mathics
        """
    def show(self, ImageSize: int = 600) -> None:
        """
        Show a mathics expression immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        INPUT:

        - ``ImageSize`` -- integer; the size of the resulting image

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES::

            sage: Q = mathics('Sin[x Cos[y]]/Sqrt[1-x^2]')   # optional - mathics
            sage: show(Q)                                    # optional - mathics
            Sin[x Cos[y]] / Sqrt[1 - x ^ 2]

            sage: P = mathics('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathics
            sage: show(P)                                    # optional - mathics
            sage: P.show(ImageSize=800)                      # optional - mathics
        """
    def __bool__(self) -> bool:
        """
        Return whether this Mathics element is not identical to ``False``.

        EXAMPLES::

            sage: bool(mathics(True))   # optional - mathics
            True
            sage: bool(mathics(False))  # optional - mathics
            False

        In Mathics, `0` cannot be used to express falsity::

            sage: bool(mathics(0))     # optional - mathics
            True
        """
    def n(self, *args, **kwargs):
        """
        Numerical approximation by converting to Sage object first.

        Convert the object into a Sage object and return its numerical
        approximation. See documentation of the function
        :func:`sage.misc.functional.n` for details.

        EXAMPLES::

            sage: mathics('Pi').n(10)    # optional -- mathics
            3.1
            sage: mathics('Pi').n()      # optional -- mathics
            3.14159265358979
            sage: mathics('Pi').n(digits=10)   # optional -- mathics
            3.141592654
        """

mathics: Incomplete

def reduce_load(X):
    """
    Used in unpickling a Mathics element.

    This function is just the ``__call__`` method of the interface instance.

    EXAMPLES::

        sage: sage.interfaces.mathics.reduce_load('Denominator[a / b]')  # optional -- mathics
        b
    """
def mathics_console() -> None:
    """
    Spawn a new Mathics command-line session.

    EXAMPLES::

        sage: mathics_console()  # not tested

        Mathics 2.1.1.dev0
        on CPython 3.9.2 (default, Mar 19 2021, 22:23:28)
        using SymPy 1.7, mpmath 1.2.1, numpy 1.19.5, cython 0.29.21

        Copyright (C) 2011-2021 The Mathics Team.
        This program comes with ABSOLUTELY NO WARRANTY.
        This is free software, and you are welcome to redistribute it
        under certain conditions.
        See the documentation for the full license.

        Quit by evaluating Quit[] or by pressing CONTROL-D.

        In[1]:= Sin[0.5]
        Out[1]= 0.479426

        Goodbye!
    """
