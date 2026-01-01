r"""
Interface to Axiom

.. TODO::

    - Evaluation using a file is not done. Any input line with more than a
      few thousand characters would hang the system, so currently it
      automatically raises an exception.

    - All completions of a given command.

    - Interactive help.

Axiom is a free GPL-compatible (modified BSD license) general
purpose computer algebra system whose development started in 1973
at IBM. It contains symbolic manipulation algorithms, as well as
implementations of special functions, including elliptic functions
and generalized hypergeometric functions. Moreover, Axiom has
implementations of many functions relating to the invariant theory
of the symmetric group `S_n.` For many links to Axiom
documentation see http://wiki.axiom-developer.org.

AUTHORS:

- Bill Page (2006-10): Created this (based on Maxima interface)


  .. NOTE::

     Bill Page put a huge amount of effort into the Sage Axiom
     interface over several days during the Sage Days 2 coding
     sprint. This is contribution is greatly appreciated.

- William Stein (2006-10): misc touchup.

- Bill Page (2007-08): Minor modifications to support axiom4sage-0.3

.. NOTE::

   The axiom4sage-0.3.spkg is based on an experimental version of the
   FriCAS fork of the Axiom project by Waldek Hebisch that uses
   pre-compiled cached Lisp code to build Axiom very quickly with
   clisp.

If the string "error" (case insensitive) occurs in the output of
anything from axiom, a :exc:`RuntimeError` exception is raised.

EXAMPLES: We evaluate a very simple expression in axiom.

::

    sage: axiom('3 * 5')                     #optional - axiom
    15
    sage: a = axiom(3) * axiom(5); a         #optional - axiom
    15

The type of a is AxiomElement, i.e., an element of the axiom
interpreter.

::

    sage: type(a)                            #optional - axiom
    <class 'sage.interfaces.axiom.AxiomElement'>
    sage: parent(a)                          #optional - axiom
    Axiom

The underlying Axiom type of a is also available, via the type
method::

    sage: a.type()                           #optional - axiom
    PositiveInteger

We factor `x^5 - y^5` in Axiom in several different ways.
The first way yields a Axiom object.

::

    sage: F = axiom.factor('x^5 - y^5'); F      #optional - axiom
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
    sage: type(F)                               #optional - axiom
    <class 'sage.interfaces.axiom.AxiomElement'>
    sage: F.type()                              #optional - axiom
    Factored Polynomial Integer

Note that Axiom objects are normally displayed using "ASCII art".

::

    sage: a = axiom(2/3); a          #optional - axiom
      2
      -
      3
    sage: a = axiom('x^2 + 3/7'); a      #optional - axiom
       2   3
      x  + -
           7

The ``axiom.eval`` command evaluates an expression in
axiom and returns the result as a string. This is exact as if we
typed in the given line of code to axiom; the return value is what
Axiom would print out.

::

    sage: print(axiom.eval('factor(x^5 - y^5)'))   # optional - axiom
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
    Type: Factored Polynomial Integer

We can create the polynomial `f` as a Axiom polynomial,
then call the factor method on it. Notice that the notation
``f.factor()`` is consistent with how the rest of Sage
works.

::

    sage: f = axiom('x^5 - y^5')                  #optional - axiom
    sage: f^2                                     #optional - axiom
       10     5 5    10
      y   - 2x y  + x
    sage: f.factor()                              #optional - axiom
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )

Control-C interruption works well with the axiom interface, because
of the excellent implementation of axiom. For example, try the
following sum but with a much bigger range, and hit control-C.

::

    sage:  f = axiom('(x^5 - y^5)^10000')       # not tested
    Interrupting Axiom...
    ...
    <class 'exceptions.TypeError'>: Ctrl-c pressed while running Axiom

::

    sage: axiom('1/100 + 1/101')                  #optional - axiom
       201
      -----
      10100
    sage: a = axiom('(1 + sqrt(2))^5'); a         #optional - axiom
         +-+
      29\|2  + 41

TESTS:

We check to make sure the subst method works with keyword
arguments.

::

    sage: a = axiom(x+2); a  #optional - axiom
    x + 2
    sage: a.subst(x=3)       #optional - axiom
    5

We verify that Axiom floating point numbers can be converted to
Python floats.

::

    sage: float(axiom(2))     #optional - axiom
    2.0
"""
import sage.interfaces.abc
from sage.env import DOT_SAGE as DOT_SAGE
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.multireplace import multiple_replace as multiple_replace
from sage.structure.richcmp import rich_to_bool as rich_to_bool

class PanAxiom(ExtraTabCompletion, Expect):
    """
    Interface to a PanAxiom interpreter.
    """
    def __init__(self, name: str = 'axiom', command: str = 'axiom -nox -noclef', script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, init_code=[')lisp (si::readline-off)']) -> None:
        """
        Create an instance of the Axiom interpreter.

        TESTS::

            sage: from sage.interfaces.axiom import axiom
            sage: axiom == loads(dumps(axiom))
            True
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: axiom.set('xx', '2')    #optional - axiom
            sage: axiom.get('xx')         #optional - axiom
            '2'
        """
    def get(self, var):
        """
        Get the string value of the Axiom variable var.

        EXAMPLES::

            sage: # optional - axiom
            sage: axiom.set('xx', '2')
            sage: axiom.get('xx')
            '2'
            sage: a = axiom('(1 + sqrt(2))^5')
            sage: axiom.get(a.name())
            '     +-+\\r\\r\\n  29\\\\|2  + 41'
        """

class Axiom(PanAxiom):
    def __reduce__(self):
        """
        EXAMPLES::

            sage: Axiom().__reduce__()
            (<function reduce_load_Axiom at 0x...>, ())
            sage: f, args = _
            sage: f(*args)
            Axiom
        """
    def console(self) -> None:
        """
        Spawn a new Axiom command-line session.

        EXAMPLES::

            sage: axiom.console() #not tested
                                    AXIOM Computer Algebra System
                                    Version: Axiom (January 2009)
                           Timestamp: Sunday January 25, 2009 at 07:08:54
            -----------------------------------------------------------------------------
               Issue )copyright to view copyright notices.
               Issue )summary for a summary of useful system commands.
               Issue )quit to leave AXIOM and return to shell.
            -----------------------------------------------------------------------------
        """

class PanAxiomElement(ExpectElement, sage.interfaces.abc.AxiomElement):
    def __call__(self, x):
        """
        EXAMPLES::

            sage: f = axiom(x+2) #optional - axiom
            sage: f(2)           #optional - axiom
            4
        """
    def type(self):
        """
        Return the type of an AxiomElement.

        EXAMPLES::

            sage: axiom(x+2).type()  #optional - axiom
            Polynomial Integer
        """
    def __len__(self) -> int:
        """
        Return the length of a list.

        EXAMPLES::

            sage: v = axiom('[x^i for i in 0..5]')            # optional - axiom
            sage: len(v)                                      # optional - axiom
            6
        """
    def __getitem__(self, n):
        """
        Return the `n`-th element of this list.

        .. NOTE::

           Lists are 1-based.

        EXAMPLES::

            sage: # optional - axiom
            sage: v = axiom('[i*x^i for i in 0..5]'); v
                     2   3   4   5
              [0,x,2x ,3x ,4x ,5x ]
            sage: v[4]
                3
              3x
            sage: v[1]
            0
            sage: v[10]
            Traceback (most recent call last):
            ...
            IndexError: index out of range
        """
    def comma(self, *args):
        """
        Return an Axiom tuple from ``self`` and ``args``.

        EXAMPLES::

            sage: # optional - axiom
            sage: two = axiom(2)
            sage: two.comma(3)
            [2,3]
            sage: two.comma(3,4)
            [2,3,4]
            sage: _.type()
            Tuple PositiveInteger
        """
    def as_type(self, type):
        """
        Return ``self`` as type.

        EXAMPLES::

            sage: a = axiom(1.2); a            #optional - axiom
            1.2
            sage: a.as_type(axiom.DoubleFloat) #optional - axiom
            1.2
            sage: _.type()                     #optional - axiom
            DoubleFloat
        """
    def unparsed_input_form(self):
        """
        Get the linear string representation of this object, if possible
        (often it isn't).

        EXAMPLES::

            sage: a = axiom(x^2+1); a     #optional - axiom
               2
              x  + 1
            sage: a.unparsed_input_form() #optional - axiom
            'x*x+1'
        """
AxiomElement = PanAxiomElement

class PanAxiomFunctionElement(FunctionElement):
    def __init__(self, object, name) -> None:
        '''
        TESTS::

            sage: # optional - axiom
            sage: a = axiom(\'"Hello"\')
            sage: a.upperCase_q
            upperCase?
            sage: a.upperCase_e
            upperCase!
            sage: a.upperCase_e()
            "HELLO"
        '''
AxiomFunctionElement = PanAxiomFunctionElement

class PanAxiomExpectFunction(ExpectFunction):
    def __init__(self, parent, name) -> None:
        """
        TESTS::

            sage: axiom.upperCase_q
            upperCase?
            sage: axiom.upperCase_e
            upperCase!
        """
AxiomExpectFunction = PanAxiomExpectFunction

def is_AxiomElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`AxiomElement`.

    EXAMPLES::

        sage: from sage.interfaces.axiom import is_AxiomElement
        sage: is_AxiomElement(2)
        doctest:...: DeprecationWarning: the function is_AxiomElement is deprecated; use isinstance(x, sage.interfaces.abc.AxiomElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_AxiomElement(axiom(2))  # optional - axiom
        True
    """

axiom: Axiom

def reduce_load_Axiom():
    """
    Return the Axiom interface object defined in
    sage.interfaces.axiom.

    EXAMPLES::

        sage: from sage.interfaces.axiom import reduce_load_Axiom
        sage: reduce_load_Axiom()
        Axiom
    """
def axiom_console() -> None:
    """
    Spawn a new Axiom command-line session.

    EXAMPLES::

        sage: axiom_console() #not tested
                                AXIOM Computer Algebra System
                                Version: Axiom (January 2009)
                       Timestamp: Sunday January 25, 2009 at 07:08:54
        -----------------------------------------------------------------------------
           Issue )copyright to view copyright notices.
           Issue )summary for a summary of useful system commands.
           Issue )quit to leave AXIOM and return to shell.
        -----------------------------------------------------------------------------
    """
