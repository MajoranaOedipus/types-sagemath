import sage.interfaces.abc
from _typeshed import Incomplete
from sage.env import DOT_SAGE as DOT_SAGE, LOCAL_IDENTIFIER as LOCAL_IDENTIFIER
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

FRICAS_CONSTANTS: Incomplete
FRICAS_SINGLE_LINE_START: int
FRICAS_MULTI_LINE_START: int
FRICAS_LINE_LENGTH: int
FRICAS_WHAT_OPERATIONS_STRING: str
FRICAS_ERROR_IN_LIBRARY_CODE: str
FRICAS_INIT_CODE: Incomplete
FRICAS_HELPER_CODE: Incomplete
FRICAS_LINENUMBER_OFF_CODE: str
FRICAS_FIRST_PROMPT: str
FRICAS_LINENUMBER_OFF_PROMPT: str

class FriCAS(ExtraTabCompletion, Expect):
    """
    Interface to a FriCAS interpreter.
    """
    def __init__(self, name: str = 'fricas', command=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None) -> None:
        """
        Create an instance of the FriCAS interpreter.

        TESTS::

            sage: fricas == loads(dumps(fricas))
            True

        Check that :issue:`25174` is fixed::

            sage: fricas(I)
            %i

            sage: integrate(sin(x)*exp(I*x), x, -pi, 0, algorithm='fricas')
            1/2*I*pi

            sage: fricas(I*sin(x)).sage()
            I*sin(x)

            sage: fricas(I*x).sage()
            I*x
        """
    def set(self, var, value) -> None:
        """
        Set a variable to a value in FriCAS.

        INPUT:

        - ``var``, ``value`` -- strings; the first representing a valid
          FriCAS variable identifier, the second a FriCAS expression

        OUTPUT: none

        EXAMPLES::

            sage: fricas.set('xx', '2')
            sage: fricas.get('xx')
            '2'
        """
    def get(self, var):
        """
        Get the string representation of the value (more precisely, the
        OutputForm) of a variable or expression in FriCAS.

        If FriCAS cannot evaluate `var` an error is raised.

        EXAMPLES::

            sage: fricas.set('xx', '2')
            sage: fricas.get('xx')
            '2'
            sage: a = fricas('(1 + sqrt(2))^5')
            sage: fricas.get(a.name())
            '    +-+\\n29 \\\\|2  + 41'
            sage: fricas.get('(1 + sqrt(2))^5')
            '    +-+\\n29 \\\\|2  + 41'
            sage: fricas.new('(1 + sqrt(2))^5')
                +-+
            29 \\|2  + 41
        """
    def get_string(self, var):
        '''
        Return the value of a FriCAS string as a string, without checking
        that it is a string.

        TESTS:

        We test that strings are returned properly::

            sage: r = fricas.get_string(\'concat([concat(string(i)," ") for i in 0..299])\')
            sage: r == " ".join(str(i) for i in range(300)) + \' \'
            True

            sage: fricas.get_string(\'concat([string(1) for i in 1..5])\') == "1"*5
            True

            sage: fricas.get_string(\'concat([string(1) for i in 1..10000])\') == "1"*10000
            True

        A problem with leading space::

            sage: s = "unparse((-1234567890123456789012345678901234567890123456789012345678901234567890*n::EXPR INT)::INFORM)"
            sage: fricas.get_string(s)
            \'(-1234567890123456789012345678901234567890123456789012345678901234567890)*n\'

        Check that :issue:`25628` is fixed::

            sage: var("a b"); f = 1/(1+a*cos(x))
            (a, b)
            sage: lF = integrate(f, x, algorithm=\'fricas\')
            sage: (diff(lF[0], x) - f).simplify_trig()
            0
            sage: (diff(lF[1], x) - f).simplify_trig()
            0
            sage: f = 1/(b*x^2+a); lF = integrate(f, x, algorithm=\'fricas\'); lF
            [1/2*log((2*a*b*x + (b*x^2 - a)*sqrt(-a*b))/(b*x^2 + a))/sqrt(-a*b),
             arctan(sqrt(a*b)*x/a)/sqrt(a*b)]
            sage: (diff(lF[0], x) - f).simplify_trig()
            0
            sage: (diff(lF[1], x) - f).simplify_trig()
            0
        '''
    def get_integer(self, var):
        """
        Return the value of a FriCAS integer as an integer, without
        checking that it is an integer.

        TESTS::

            sage: fricas.get_integer('factorial 1111') == factorial(1111)
            True
        """
    def get_boolean(self, var):
        """
        Return the value of a FriCAS boolean as a boolean, without checking
        that it is a boolean.

        TESTS::

            sage: fricas.get_boolean('(1=1)::Boolean') == True
            True

            sage: fricas.get_boolean('(1=2)::Boolean') == False
            True
        """
    def get_unparsed_InputForm(self, var):
        """
        Return the unparsed ``InputForm`` as a string.

        .. TODO::

            - catch errors, especially when InputForm is not available:

                - for example when integration returns ``'failed'``

                - ``UnivariatePolynomial``

            - should we provide workarounds, too?

        TESTS::

            sage: fricas.get_unparsed_InputForm('1..3')
            '(1..3)$Segment(PositiveInteger())'
        """
    def get_InputForm(self, var):
        """
        Return the ``InputForm`` as a string.

        TESTS::

            sage: fricas.get_InputForm('1..3')
            '(($elt (Segment (PositiveInteger)) SEGMENT) 1 3)'
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: FriCAS().__reduce__()
            (<function reduce_load_fricas at 0x...>, ())
            sage: f, args = _
            sage: f(*args)
            FriCAS
        """
    def eval(self, code, strip: bool = True, synchronize: bool = False, locals=None, allow_use_file: bool = True, split_lines: str = 'nofile', reformat: bool = True, **kwds):
        '''
        Evaluate ``code`` using FriCAS.

        Except ``reformat``, all arguments are passed to
        :meth:`sage.interfaces.expect.Expect.eval`.

        INPUT:

        - ``reformat`` -- boolean; remove the output markers when True

        This can also be used to pass system commands to FriCAS.

        EXAMPLES::

            sage: fricas.set("x", "1783"); fricas("x")
            1783
            sage: fricas.eval(")cl val x");
            \'\'
            sage: fricas("x")
            x
        '''
    def console(self) -> None:
        """
        Spawn a new FriCAS command-line session.

        EXAMPLES::

            sage: fricas.console()                                              # not tested
                             FriCAS (AXIOM fork) Computer Algebra System
                                    Version: FriCAS 1.0.5
                     Timestamp: Thursday February 19, 2009 at 06:57:33
            -----------------------------------------------------------------------------
               Issue )copyright to view copyright notices.
               Issue )summary for a summary of useful system commands.
               Issue )quit to leave AXIOM and return to shell.
            -----------------------------------------------------------------------------
        """

class FriCASElement(ExpectElement, sage.interfaces.abc.FriCASElement):
    """
    Instances of this class represent objects in FriCAS.

    Using the method :meth:`sage` we can translate some of them to
    SageMath objects:

    .. automethod:: _sage_
    """
    def __len__(self) -> int:
        """
        Return the length of a list.

        EXAMPLES::

            sage: v = fricas('[x^i for i in 0..5]')
            sage: len(v)
            6

        TESTS:

        Streams are not handled yet::

            sage: oh = fricas('[i for i in 1..]')
            sage: len(oh)
            Traceback (most recent call last):
            ...
            TypeError: ...
        """
    def __iter__(self):
        """
        Return an iterator over ``self``.

        EXAMPLES::

            sage: L = fricas([4,5,6])
            sage: list(L)
            [4, 5, 6]

        TESTS:

        Streams are not handled yet::

            sage: oh = fricas('[i for i in 1..]')
            sage: next(iter(oh))       # known bug
        """
    def __getitem__(self, n):
        '''
        We implement the sage conventions here, translating to 0-based iterables.

        We do not check validity, since many objects in FriCAS are
        iterable, in particular Streams

        TESTS::

            sage: fricas("[1,2,3]")[0]
            1

        Negative indices do work::

            sage: fricas("[1,2,3]")[-1]
            3

            sage: fricas("[1,2,3]")[-2]
            2

        Invalid indices raise exceptions::

            sage: fricas("[1,2,3]")[3]
            Traceback (most recent call last):
            ...
            TypeError: An error occurred when FriCAS evaluated \'elt(...,...)\':
            <BLANKLINE>
            >> Error detected within library code:
            index out of range

        And streams are ok too::

            sage: oh = fricas(\'[i for i in 1..]\')
            sage: oh[4]
            5
        '''
    def __int__(self) -> int:
        """
        TESTS::

            sage: int(fricas(2))
            2
        """
    def bool(self):
        '''
        Coerce the expression into a boolean.

        EXAMPLES::

            sage: fricas("1=1").bool()
            True
            sage: fricas("1~=1").bool()
            False
        '''
    def __bool__(self) -> bool:
        """
        Check whether the expression is different from zero.

        EXAMPLES::

            sage: fricas(0).is_zero()   # indirect doctest
            True
        """
    def __float__(self) -> float:
        """
        TESTS::

            sage: float(fricas(2))
            2.0
        """
    def gen(self, n) -> None:
        """
        Return an error, since the n-th generator in FriCAS is not well defined.
        """

class FriCASFunctionElement(FunctionElement):
    def __init__(self, object, name) -> None:
        '''
        Make FriCAS operation names valid python function identifiers.

        TESTS::

            sage: a = fricas(\'"Hello"\')
            sage: a.upperCase_q
            upperCase?
            sage: a.upperCase_e
            upperCase!
            sage: a.upperCase_e()
            "HELLO"
        '''

class FriCASExpectFunction(ExpectFunction):
    def __init__(self, parent, name) -> None:
        """
        Translate the pythonized function identifier back to a FriCAS
        operation name.

        TESTS::

            sage: fricas.upperCase_q
            upperCase?
            sage: fricas.upperCase_e
            upperCase!
        """

def is_FriCASElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`FriCASElement`.

    EXAMPLES::

        sage: from sage.interfaces.fricas import is_FriCASElement
        sage: is_FriCASElement(2)
        doctest:...: DeprecationWarning: the function is_FriCASElement is deprecated; use isinstance(x, sage.interfaces.abc.FriCASElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_FriCASElement(fricas(2))
        True
    """

fricas: Incomplete

def reduce_load_fricas():
    """
    Return the FriCAS interface object defined in :mod:`sage.interfaces.fricas`.

    EXAMPLES::

        sage: from sage.interfaces.fricas import reduce_load_fricas
        sage: reduce_load_fricas()
        FriCAS
    """
def fricas_console() -> None:
    """
    Spawn a new FriCAS command-line session.

    EXAMPLES::

        sage: fricas_console()                                                  # not tested
                         FriCAS (AXIOM fork) Computer Algebra System
                                    Version: FriCAS 1.0.5
                     Timestamp: Thursday February 19, 2009 at 06:57:33
        -----------------------------------------------------------------------------
           Issue )copyright to view copyright notices.
           Issue )summary for a summary of useful system commands.
           Issue )quit to leave AXIOM and return to shell.
        -----------------------------------------------------------------------------
    """
