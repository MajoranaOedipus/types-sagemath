from _typeshed import Incomplete
from sage.env import MAXIMA as MAXIMA
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, gc_disabled as gc_disabled
from sage.interfaces.maxima_abstract import MaximaAbstract as MaximaAbstract, MaximaAbstractElement as MaximaAbstractElement, MaximaAbstractElementFunction as MaximaAbstractElementFunction, MaximaAbstractFunction as MaximaAbstractFunction, MaximaAbstractFunctionElement as MaximaAbstractFunctionElement
from sage.misc.instancedoc import instancedoc as instancedoc

class Maxima(MaximaAbstract, Expect):
    """
    Interface to the Maxima interpreter.

    EXAMPLES::

        sage: m = Maxima()
        sage: m == maxima
        False
    """
    def __init__(self, script_subdirectory=None, logfile=None, server=None, init_code=None) -> None:
        """
        Create an instance of the Maxima interpreter.

        TESTS::

            sage:: from sage.interfaces.maxima import Maxima, maxima
            sage: Maxima == loads(dumps(Maxima))
            True
            sage: maxima == loads(dumps(maxima))
            True

        Unpickling a Maxima Pexpect interface gives the default interface::

            sage: m = Maxima()
            sage: maxima == loads(dumps(m))
            True

        We make sure labels are turned off (see :issue:`6816`)::

            sage: 'nolabels : true' in maxima._Expect__init_code
            True
        """
    def set_seed(self, seed=None):
        """
        http://maxima.sourceforge.net/docs/manual/maxima_10.html
        make_random_state (n) returns a new random state object created from an
        integer seed value equal to n modulo 2^32. n may be negative.

        EXAMPLES::

            sage: m = Maxima()
            sage: m.set_seed(1)
            1
            sage: [m.random(100) for i in range(5)]
            [45, 39, 24, 68, 63]
        """
    def __reduce__(self):
        """
        Implementation of __reduce__ for ``Maxima``.

        EXAMPLES::

            sage: maxima.__reduce__()
            (<function reduce_load_Maxima at 0x...>, ())
        """
    def lisp(self, cmd):
        '''
        Send a lisp command to Maxima.

        .. NOTE::

           The output of this command is very raw - not pretty.

        EXAMPLES::

            sage: maxima.lisp("(+ 2 17)")   # random formatted output
             :lisp (+ 2 17)
            19
            (
        '''
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        INPUT:

        - ``var`` -- string

        - ``value`` -- string

        EXAMPLES::

            sage: maxima.set('xxxxx', '2')
            sage: maxima.get('xxxxx')
            '2'
        """
    def clear(self, var) -> None:
        """
        Clear the variable named var.

        EXAMPLES::

            sage: maxima.set('xxxxx', '2')
            sage: maxima.get('xxxxx')
            '2'
            sage: maxima.clear('xxxxx')
            sage: maxima.get('xxxxx')
            'xxxxx'
        """
    def get(self, var):
        """
        Get the string value of the variable var.

        EXAMPLES::

            sage: maxima.set('xxxxx', '2')
            sage: maxima.get('xxxxx')
            '2'
        """

def is_MaximaElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`MaximaElement`.

    EXAMPLES::

        sage: from sage.interfaces.maxima import is_MaximaElement
        sage: is_MaximaElement(1)
        doctest:...: DeprecationWarning: the function is_MaximaElement is deprecated; use isinstance(x, sage.interfaces.abc.MaximaElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: m = maxima(1)
        sage: is_MaximaElement(m)
        True
    """

class MaximaElement(MaximaAbstractElement, ExpectElement):
    """
    Element of Maxima through Pexpect interface.

    EXAMPLES:

    Elements of this class should not be created directly.
    The targeted parent should be used instead::

        sage: maxima(3)
        3
        sage: maxima(cos(x)+e^234)
        cos(_SAGE_VAR_x)+%e^234
    """
    def __init__(self, parent, value, is_name: bool = False, name=None) -> None:
        """
        Create a Maxima element.
        See ``MaximaElement`` for full documentation.

        EXAMPLES::

           sage: maxima(zeta(7))
           zeta(7)

        TESTS::

            sage: from sage.interfaces.maxima import MaximaElement
            sage: loads(dumps(MaximaElement))==MaximaElement
            True
            sage: a = maxima(5)
            sage: type(a)
            <class 'sage.interfaces.maxima.MaximaElement'>
            sage: loads(dumps(a))==a
            True
        """
    def display2d(self, onscreen: bool = True):
        """
        Return the 2d string representation of this Maxima object.

        EXAMPLES::

            sage: F = maxima('x^5 - y^5').factor()
            sage: F.display2d()
                                   4      3    2  2    3      4
                       - (y - x) (y  + x y  + x  y  + x  y + x )
        """
MaximaFunctionElement = MaximaAbstractFunctionElement
MaximaFunction = MaximaAbstractFunction

class MaximaElementFunction(MaximaElement, MaximaAbstractElementFunction):
    """
    Maxima user-defined functions.

    EXAMPLES:

    Elements of this class should not be created directly.
    The method ``function`` of the targeted parent should be used instead::

        sage: maxima.function('x,y','h(x)*y')
        h(x)*y
    """
    def __init__(self, parent, name, defn, args, latex) -> None:
        """
        Create a Maxima function.
        See ``MaximaElementFunction`` for full documentation.

        EXAMPLES::

            sage: maxima.function('x,y','cos(x)+y')
            cos(x)+y

        TESTS::

            sage: f = maxima.function('x,y','x+y^9')
            sage: f == loads(dumps(f))
            True

        Unpickling a Maxima Pexpect interface gives the default interface::

            sage: m = Maxima()
            sage: g = m.function('x,y','x+y^9')
            sage: h = loads(dumps(g))
            sage: g.parent() == h.parent()
            False
        """

maxima: Incomplete

def reduce_load_Maxima():
    """
    Unpickle a Maxima Pexpect interface.

    EXAMPLES::

        sage: from sage.interfaces.maxima import reduce_load_Maxima
        sage: reduce_load_Maxima()
        Maxima
    """
def reduce_load_Maxima_function(parent, defn, args, latex):
    """
    Unpickle a Maxima function.

    EXAMPLES::

        sage: from sage.interfaces.maxima import reduce_load_Maxima_function
        sage: f = maxima.function('x,y','sin(x+y)')
        sage: _,args = f.__reduce__()
        sage: g = reduce_load_Maxima_function(*args)
        sage: g == f
        True
    """
