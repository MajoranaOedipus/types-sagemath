r"""
Interface to Sage

This is an expect interface to *another* copy of the Sage
interpreter.
"""

from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, FunctionElement as FunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.persist import dumps as dumps, load as load

class Sage(ExtraTabCompletion, Expect):
    '''
    Expect interface to the Sage interpreter itself.

    INPUT:

    - ``server`` -- (optional) if specified runs Sage on a
      remote machine with address. You must have ssh keys setup so you
      can login to the remote machine by typing "ssh remote_machine" and
      no password, call _install_hints_ssh() for hints on how to do
      that.


    The version of Sage should be the same as on the local machine,
    since pickling is used to move data between the two Sage process.

    EXAMPLES: We create an interface to a copy of Sage. This copy of
    Sage runs as an external process with its own memory space, etc.

    ::

        sage: s = Sage()

    Create the element 2 in our new copy of Sage, and cube it.

    ::

        sage: a = s(2)
        sage: a^3
        8

    Create a vector space of dimension `4`, and compute its
    generators::

        sage: V = s(\'QQ^4\')
        sage: V.gens()
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))

    Note that V is a not a vector space, it\'s a wrapper around an
    object (which happens to be a vector space), in another running
    instance of Sage.

    ::

        sage: type(V)
        <class \'sage.interfaces.sage0.SageElement\'>
        sage: V.parent()
        Sage
        sage: g = V.0;  g
        (1, 0, 0, 0)
        sage: g.parent()
        Sage

    We can still get the actual parent by using the name attribute of
    g, which is the variable name of the object in the child process.

    ::

        sage: s(\'%s.parent()\' % g.name())
        Vector space of dimension 4 over Rational Field

    Note that the memory space is completely different.

    ::

        sage: x = 10
        sage: s(\'x = 5\')
        5
        sage: x
        10
        sage: s(\'x\')
        5

    We can have the child interpreter itself make another child Sage
    process, so now three copies of Sage are running::

        sage: s3 = s(\'Sage()\')
        sage: a = s3(10)
        sage: a
        10

    This `a=10` is in a subprocess of a subprocess of your
    original Sage.

    ::

        sage: _ = s.eval(\'%s.eval("x=8")\' % s3.name())
        sage: s3(\'"x"\')
        8
        sage: s(\'x\')
        5
        sage: x
        10

    The double quotes are needed because the call to s3 first evaluates
    its arguments using the s interpreter, so the call to s3 is passed
    ``s(\'"x"\')``, which is the string ``\'x\'`` in the s interpreter.
    '''
    def __init__(self, logfile=None, preparse: bool = True, init_code=None, server=None, server_tmpdir=None, remote_cleaner: bool = True, **kwds) -> None:
        """
        EXAMPLES::

            sage: sage0 == loads(dumps(sage0))
            True
        """
    def cputime(self, t=None):
        """
        Return cputime since this Sage subprocess was started.

        EXAMPLES::

            sage: sage0.cputime()     # random output
            1.3530439999999999
            sage: sage0('factor(2^157-1)')
            852133201 * 60726444167 * 1654058017289 * 2134387368610417
            sage: sage0.cputime()     # random output
            1.6462939999999999
        """
    def __call__(self, x):
        """
        EXAMPLES::

            sage: a = sage0(4)
            sage: a.parent()
            Sage
            sage: a is sage0(a)
            True

        TESTS::

            sage: sage0(axiom(x^2+1)) #optional - axiom
            x^2 + 1
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: sage0.__reduce__()
            (<function reduce_load_Sage at 0x...>, ())
        """
    def preparse(self, x):
        """
        Return the preparsed version of the string s.

        EXAMPLES::

            sage: sage0.preparse('2+2')
            'Integer(2)+Integer(2)'
        """
    def eval(self, line, strip: bool = True, **kwds):
        """
        Send the code x to a second instance of the Sage interpreter and
        return the output as a string.

        This allows you to run two completely independent copies of Sage at
        the same time in a unified way.

        INPUT:

        - ``line`` -- input line of code

        - ``strip`` -- ignored

        EXAMPLES::

            sage: sage0.eval('2+2')
            '4'
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: sage0.set('x', '2')
            sage: sage0.get('x')
            '2'
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: sage0.set('x', '2')
            sage: sage0.get('x')
            '2'
        """
    def clear(self, var) -> None:
        """
        Clear the variable named var.

        Note that the exact format of the :exc:`NameError` for a cleared
        variable is slightly platform dependent, see :issue:`10539`.

        EXAMPLES::

            sage: sage0.set('x', '2')
            sage: sage0.get('x')
            '2'
            sage: sage0.clear('x')
            sage: 'NameError' in sage0.get('x')
            True
        """
    def console(self) -> None:
        '''
        Spawn a new Sage command-line session.

        EXAMPLES::

            sage: sage0.console() #not tested
            ----------------------------------------------------------------------
            | SageMath version ..., Release Date: ...                            |
            | Using Python ....   Type "help()" for help.                        |
            ----------------------------------------------------------------------
            ...
        '''
    def version(self):
        """
        EXAMPLES::

            sage: sage0.version()
            'SageMath version ..., Release Date: ...'
            sage: sage0.version() == version()
            True
        """
    def new(self, x):
        """
        EXAMPLES::

            sage: sage0.new(2)
            2
            sage: _.parent()
            Sage
        """

class SageElement(ExpectElement):
    def __getattr__(self, attrname):
        """
        EXAMPLES::

            sage: m = sage0(4)
            sage: four_gcd = m.gcd
            sage: type(four_gcd)
            <class 'sage.interfaces.sage0.SageFunction'>
        """

class SageFunction(FunctionElement):
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: four_gcd = sage0(4).gcd
            sage: four_gcd(6)
            2
        """

sage0: Sage

def reduce_load_Sage():
    """
    EXAMPLES::

        sage: from sage.interfaces.sage0 import reduce_load_Sage
        sage: reduce_load_Sage()
        Sage
    """
def reduce_load_element(s):
    """
    EXAMPLES::

        sage: from sage.interfaces.sage0 import reduce_load_element
        sage: s = dumps(1/2)
        sage: half = reduce_load_element(s); half
        1/2
        sage: half.parent()
        Sage
    """
def sage0_console() -> None:
    '''
    Spawn a new Sage command-line session.

    EXAMPLES::

        sage: sage0_console() #not tested
        ----------------------------------------------------------------------
        | SageMath version ..., Release Date: ...                            |
        | Using Python ....   Type "help()" for help.                        |
        ----------------------------------------------------------------------
        ...
    '''
def sage0_version():
    """
    EXAMPLES::

        sage: from sage.interfaces.sage0 import sage0_version
        sage: sage0_version() == version()
        True
    """
