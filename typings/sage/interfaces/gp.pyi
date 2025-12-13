import sage.interfaces.abc
from .expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from _typeshed import Incomplete
from sage.env import DOT_SAGE as DOT_SAGE
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.libs.pari import pari as pari
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose

class Gp(ExtraTabCompletion, Expect):
    """
    Interface to the PARI gp interpreter.

    Type ``gp.[tab]`` for a list of all the functions
    available from your Gp install. Type ``gp.[tab]?`` for
    Gp's help about a given function. Type ``gp(...)`` to
    create a new Gp object, and ``gp.eval(...)`` to evaluate a
    string using Gp (and get the result back as a string).

        INPUT:

        - ``stacksize`` -- integer (default: 10000000); the initial PARI
          stacksize in bytes (default: 10MB)
        - ``script_subdirectory`` -- string (default: ``None``); name of the
          subdirectory of ``SAGE_EXTCODE/pari`` from which to read scripts
        - ``logfile`` -- string (default: ``None``); log file for the pexpect
          interface
        - ``server`` -- name of remote server
        - ``server_tmpdir`` -- name of temporary directory on remote server
        - ``init_list_length`` -- integer (default: 1024); length of initial
          list of local variables
        - ``seed`` -- integer (default: random); random number generator seed
          for pari

        EXAMPLES::

            sage: Gp()
            PARI/GP interpreter
    """
    def __init__(self, stacksize: int = 10000000, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, init_list_length: int = 1024, seed=None) -> None:
        """
        Initialization of this PARI gp interpreter.

        INPUT:

        - ``stacksize`` -- integer (default: 10000000); the initial PARI
          stacksize in bytes (default: 10MB)
        - ``script_subdirectory`` -- string (default: ``None``); name of the
          subdirectory of SAGE_EXTCODE/pari from which to read scripts
        - ``logfile`` -- string (default: ``None``); log file for the pexpect
          interface
        - ``server`` -- name of remote server
        - ``server_tmpdir`` -- name of temporary directory on remote server
        - ``init_list_length`` -- integer (default: 1024); length of initial
          list of local variables.
        - ``seed`` -- integer (default random nonzero 31 bit integer); value of
          random seed

        EXAMPLES::

            sage: from sage.interfaces.gp import gp
            sage: gp == loads(dumps(gp))
            True
        """
    def set_seed(self, seed=None):
        """
        Set the seed for gp interpreter.

        The seed should be an integer.

        EXAMPLES::

            sage: g = Gp()
            sage: g.set_seed(1)
            1
            sage: [g.random() for i in range(5)]
            [1546275796, 879788114, 1745191708, 771966234, 1247963869]
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: from sage.interfaces.gp import gp
            sage: gp.__reduce__()
            (<function reduce_load_GP at 0x...>, ())
            sage: f, args = _
            sage: f(*args)
            PARI/GP interpreter
        """
    def get_precision(self):
        """
        Return the current PARI precision for real number computations.

        EXAMPLES::

            sage: gp.get_precision()
            38
        """
    get_real_precision = get_precision
    def set_precision(self, prec):
        """
        Set the PARI precision (in decimal digits) for real
        computations, and returns the old value.

        .. NOTE::

            PARI/GP rounds up precisions to the nearest machine word,
            so the result of :meth:`get_precision` is not always the
            same as the last value inputted to :meth:`set_precision`.

        EXAMPLES::

            sage: old_prec = gp.set_precision(53); old_prec
            38
            sage: gp.get_precision()
            57
            sage: gp.set_precision(old_prec)
            57
            sage: gp.get_precision()
            38
        """
    set_real_precision = set_precision
    def get_series_precision(self):
        """
        Return the current PARI power series precision.

        EXAMPLES::

            sage: gp.get_series_precision()
            16
        """
    def set_series_precision(self, prec=None):
        """
        Set the PARI power series precision, and returns the old precision.

        EXAMPLES::

            sage: old_prec = gp.set_series_precision(50); old_prec
            16
            sage: gp.get_series_precision()
            50
            sage: gp.set_series_precision(old_prec)
            50
            sage: gp.get_series_precision()
            16
        """
    def cputime(self, t=None):
        """
        cputime for pari - cputime since the pari process was started.

        INPUT:

        - ``t`` -- (default: ``None``) if not None, then returns
          time since t


        .. warning::

           If you call gettime explicitly, e.g., gp.eval('gettime'),
           you will throw off this clock.

        EXAMPLES::

            sage: gp.cputime()          # random output
            0.0080000000000000002
            sage: gp.factor('2^157-1')
            [852133201, 1; 60726444167, 1; 1654058017289, 1; 2134387368610417, 1]
            sage: gp.cputime()          # random output
            0.26900000000000002
        """
    def set_default(self, var, value):
        """
        Set a PARI gp configuration variable, and return the old value.

        INPUT:

        - ``var`` -- string; the name of a PARI gp
          configuration variable (see ``gp.default()`` for a list)
        - ``value`` -- the value to set the variable to

        EXAMPLES::

            sage: old_prec = gp.set_default('realprecision', 110)
            sage: gp.get_default('realprecision')
            115
            sage: gp.set_default('realprecision', old_prec)
            115
            sage: gp.get_default('realprecision')
            38
        """
    def get_default(self, var):
        """
        Return the current value of a PARI gp configuration variable.

        INPUT:

        - ``var`` -- string; the name of a PARI gp
          configuration variable (see ``gp.default()`` for a list)

        OUTPUT: string; the value of the variable

        EXAMPLES::

            sage: gp.get_default('log')
            0
            sage: gp.get_default('datadir')
            '.../share/pari'
            sage: gp.get_default('seriesprecision')
            16
            sage: gp.get_default('realprecision')
            38
        """
    def set(self, var, value) -> None:
        """
        Set the GP variable var to the given value.

        INPUT:

        - ``var`` -- string; a valid GP variable identifier
        - ``value`` -- a value for the variable

        EXAMPLES::

            sage: gp.set('x', '2')
            sage: gp.get('x')
            '2'
        """
    def get(self, var):
        """
        Get the value of the GP variable var.

        INPUT:

        - ``var`` -- string; a valid GP variable identifier

        EXAMPLES::

            sage: gp.set('x', '2')
            sage: gp.get('x')
            '2'
        """
    def kill(self, var) -> None:
        """
        Kill the value of the GP variable var.

        INPUT:

        - ``var`` -- string; a valid GP variable identifier

        EXAMPLES::

            sage: gp.set('xx', '22')
            sage: gp.get('xx')
            '22'
            sage: gp.kill('xx')
            sage: gp.get('xx')
            'xx'
        """
    def console(self) -> None:
        """
        Spawn a new GP command-line session.

        EXAMPLES::

            sage: gp.console()  # not tested
            GP/PARI CALCULATOR Version 2.4.3 (development svn-12577)
            amd64 running linux (x86-64/GMP-4.2.1 kernel) 64-bit version
            compiled: Jul 21 2010, gcc-4.6.0 20100705 (experimental) (GCC)
            (readline v6.0 enabled, extended help enabled)
        """
    def version(self):
        """
        Return the version of GP being used.

        EXAMPLES::

            sage: gp.version()  # not tested
            ((2, 4, 3), 'GP/PARI CALCULATOR Version 2.4.3 (development svn-12577)')
        """
    def help(self, command):
        """
        Return GP's help for ``command``.

        EXAMPLES::

            sage: gp.help('gcd')
            'gcd(x,{y}): greatest common divisor of x and y.'
        """
    def new_with_bits_prec(self, s, precision: int = 0):
        """
        Create a GP object from s with ``precision`` bits of
        precision. GP actually automatically increases this precision to
        the nearest word (i.e. the next multiple of 32 on a 32-bit machine,
        or the next multiple of 64 on a 64-bit machine).

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: pi_def = gp(pi); pi_def
            3.1415926535897932384626433832795028842
            sage: pi_def.precision()
            38
            sage: pi_150 = gp.new_with_bits_prec(pi, 150)
            sage: new_prec = pi_150.precision(); new_prec
            48                                             # 32-bit
            57                                             # 64-bit
            sage: old_prec = gp.set_precision(new_prec); old_prec
            38
            sage: pi_150
            3.14159265358979323846264338327950288419716939938  # 32-bit
            3.14159265358979323846264338327950288419716939937510582098  # 64-bit
            sage: gp.set_precision(old_prec)
            48                                             # 32-bit
            57                                             # 64-bit
            sage: gp.get_precision()
            38
        """

class GpElement(ExpectElement, sage.interfaces.abc.GpElement):
    """
    EXAMPLES: This example illustrates dumping and loading GP elements
    to compressed strings.

    ::

        sage: a = gp(39393)
        sage: loads(a.dumps()) == a
        True

    Since dumping and loading uses the string representation of the
    object, it need not result in an identical object from the point of
    view of PARI::

        sage: E = gp('ellinit([1,2,3,4,5])')
        sage: loads(dumps(E)) == E
        True
        sage: x = gp.Pi()/3
        sage: loads(dumps(x)) == x
        False
        sage: x
        1.0471975511965977461542144610931676281
        sage: loads(dumps(x))
        1.0471975511965977461542144610931676281

    The two elliptic curves look the same, but internally the floating
    point numbers are slightly different.
    """
    def is_string(self):
        '''
        Tell whether this element is a string.

        EXAMPLES::

            sage: gp(\'"abc"\').is_string()
            True
            sage: gp(\'[1,2,3]\').is_string()
            False
        '''
    def __float__(self) -> float:
        """
        Return Python float.

        EXAMPLES::

            sage: float(gp(10))
            10.0
        """
    def __bool__(self) -> bool:
        """
        EXAMPLES::

            sage: gp(2).bool()
            True
            sage: bool(gp(2))
            True
            sage: bool(gp(0))
            False
        """
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: len(gp([1,2,3]))
            3
        """
    def __del__(self) -> None:
        """
        Note that clearing object is pointless since it wastes time and
        PARI/GP doesn't really free used memory.

        EXAMPLES::

            sage: a = gp(2)
            sage: a.__del__()
            sage: a
            2
            sage: del a
            sage: a
            Traceback (most recent call last):
            ...
            NameError: name 'a' is not defined
        """
GpFunctionElement = FunctionElement
GpFunction = ExpectFunction

def is_GpElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`GpElement`.

    This function is deprecated; use :func:`isinstance`
    (of :class:`sage.interfaces.abc.GpElement`) instead.

    EXAMPLES::

        sage: from sage.interfaces.gp import is_GpElement
        sage: is_GpElement(gp(2))
        doctest:...: DeprecationWarning: the function is_GpElement is deprecated; use isinstance(x, sage.interfaces.abc.GpElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        True
        sage: is_GpElement(2)
        False
    """

gp: Incomplete

def reduce_load_GP():
    """
    Return the GP interface object defined in ``sage.interfaces.gp``.

    EXAMPLES::

        sage: from sage.interfaces.gp import reduce_load_GP
        sage: reduce_load_GP()
        PARI/GP interpreter
    """
def gp_console() -> None:
    """
    Spawn a new GP command-line session.

    EXAMPLES::

        sage: gp.console()  # not tested
        GP/PARI CALCULATOR Version 2.4.3 (development svn-12577)
        amd64 running linux (x86-64/GMP-4.2.1 kernel) 64-bit version
        compiled: Jul 21 2010, gcc-4.6.0 20100705 (experimental) (GCC)
        (readline v6.0 enabled, extended help enabled)
    """
def gp_version():
    """
    EXAMPLES::

        sage: gp.version()  # not tested
        ((2, 4, 3), 'GP/PARI CALCULATOR Version 2.4.3 (development svn-12577)')
    """
