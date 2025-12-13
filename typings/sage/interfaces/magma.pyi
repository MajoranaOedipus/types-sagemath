import sage.interfaces.abc
import types
from .expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from _typeshed import Incomplete
from sage.env import DOT_SAGE as DOT_SAGE, SAGE_EXTCODE as SAGE_EXTCODE
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.parent import Parent as Parent

PROMPT: str
SAGE_REF: str
SAGE_REF_RE: Incomplete
INTRINSIC_CACHE: Incomplete
EXTCODE_DIR: Incomplete

def extcode_dir(iface=None) -> str:
    """
    Return directory that contains all the Magma extcode.

    This is put in a writable directory owned by the user, since when
    attached, Magma has to write sig and lck files.

    EXAMPLES::

        sage: sage.interfaces.magma.extcode_dir()
        '...dir_.../data/'
    """

class Magma(ExtraTabCompletion, Expect):
    """
    Interface to the Magma interpreter.

    Type ``magma.[tab]`` for a list of all the functions
    available from your Magma install. Type
    ``magma.Function?`` for Magma's help about a given ``Function``
    Type ``magma(...)`` to create a new Magma
    object, and ``magma.eval(...)`` to run a string using
    Magma (and get the result back as a string).

    .. NOTE::

       If you do not own a local copy of Magma, try using the
       ``magma_free`` command instead, which uses the free demo web
       interface to Magma.

       If you have ssh access to a remote installation of Magma, you can
       also set the ``server`` parameter to use it.

    EXAMPLES:

    You must use nvals = 0 to call a function that doesn't return
    anything, otherwise you'll get an error. (nvals is the number of
    return values.)

    ::

        sage: magma.SetDefaultRealFieldPrecision(200, nvals=0)  # magma >= v2.12; optional - magma
        sage: magma.eval('1.1')   # optional - magma
        '1.1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        sage: magma.SetDefaultRealFieldPrecision(30, nvals=0)  # optional - magma
    """
    def __init__(self, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, user_config: bool = False, seed=None, command=None) -> None:
        """
        INPUT:

        - ``script_subdirectory`` -- directory where scripts
          are read from

        - ``logfile`` -- output logged to this file

        - ``server`` -- address of remote server

        - ``server_tmpdir`` -- temporary directory to use in remote server

        - ``user_config`` -- if ``True``, then local user
          configuration files will be read by Magma. If ``False`` (the default),
          then Magma is started with the -n option which suppresses user
          configuration files.

        - ``seed`` -- seed to use in the random number generator

        - ``command`` -- (default: ``'magma'``) the command to execute to start Magma

        EXAMPLES::

            sage: Magma(logfile=tmp_filename())
            Magma
        """
    def set_seed(self, seed=None):
        """
        Set the seed for the Magma interpreter.

        The seed should be an integer.

        EXAMPLES::

            sage: m = Magma() # optional - magma
            sage: m.set_seed(1) # optional - magma
            1
            sage: [m.Random(100) for i in range(5)] # optional - magma
            [14, 81, 45, 75, 67]
        """
    def __reduce__(self):
        """
        Used to pickle a magma interface instance.

        Unpickling results in the default magma interpreter; this is a
        choice, and perhaps not the most logical one! It means that if you
        make two distinct magma interfaces, pickle both, then unpickle
        them, you get back exactly the same one. We illustrate this
        behavior below.

        OUTPUT: function, empty tuple

        EXAMPLES::

            sage: from sage.interfaces.magma import magma
            sage: loads(dumps(magma)) is magma
            True

        Unpickling always gives the default global magma interpreter::

            sage: m1 = Magma(); m2 = Magma()
            sage: m1 is m2
            False
            sage: loads(dumps(m1)) is loads(dumps(m2))
            True
            sage: loads(dumps(m1)) is magma
            True
        """
    def __getattr__(self, attrname):
        """
        Return a formal wrapper around a Magma function, or raise an
        :exc:`AttributeError` if attrname starts with an underscore.

        INPUT:

        - ``attrname`` -- string

        OUTPUT: :class:`MagmaFunction` instance

        EXAMPLES::

            sage: g = magma.__getattr__('EllipticCurve')
            sage: g
            EllipticCurve
            sage: type(g)
            <class 'sage.interfaces.magma.MagmaFunction'>

        In fact, __getattr__ is called implicitly in the following
        case::

            sage: f = magma.EllipticCurve
            sage: type(f)
            <class 'sage.interfaces.magma.MagmaFunction'>
            sage: f
            EllipticCurve
        """
    def eval(self, x, strip: bool = True, **kwds) -> str:
        '''
        Evaluate the given block x of code in Magma and return the output
        as a string.

        INPUT:

        - ``x`` -- string of code

        - ``strip`` -- ignored

        OUTPUT: string

        EXAMPLES:

        We evaluate a string that involves assigning to a
        variable and printing.

        ::

            sage: magma.eval("a := 10;print 2+a;")      # optional - magma
            \'12\'

        We evaluate a large input line (note that no weird output appears
        and that this works quickly).

        ::

            sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
            \'\'

        Verify that :issue:`9705` is fixed::

            sage: nl=chr(10) # newline character
            sage: magma.eval(  # optional - magma
            ....: "_<x>:=PolynomialRing(Rationals());"+nl+
            ....: "repeat"+nl+
            ....: "  g:=3*b*x^4+18*c*x^3-6*b^2*x^2-6*b*c*x-b^3-9*c^2 where b:=Random([-10..10]) where c:=Random([-10..10]);"+nl+
            ....: "until g ne 0 and Roots(g) ne [];"+nl+
            ....: "print "success";")
            \'success\'

        Verify that :issue:`11401` is fixed::

            sage: nl=chr(10) # newline character
            sage: magma.eval("a:=3;"+nl+"b:=5;") == nl  # optional - magma
            True
            sage: magma.eval("[a,b];")                  # optional - magma
            \'[ 3, 5 ]\'
        '''
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value in the Magma interpreter.

        INPUT:

        - ``var`` -- string; a variable name

        - ``value`` -- string; what to set var equal to

        EXAMPLES::

            sage: magma.set('abc', '2 + 3/5')       # optional - magma
            sage: magma('abc')                      # optional - magma
            13/5
        """
    def get(self, var) -> str:
        """
        Get the value of the variable var.

        INPUT:

        - ``var`` -- string; name of a variable defined in the
          Magma session

        OUTPUT: string representation of the value of the variable

        EXAMPLES::

            sage: magma.set('abc', '2 + 3/5')     # optional - magma
            sage: magma.get('abc')                # optional - magma
            '13/5'
        """
    def objgens(self, value, gens):
        """
        Create a new object with given value and gens.

        INPUT:

        - ``value`` -- something coercible to an element of this Magma
          interface

        - ``gens`` -- string; comma separated list of variable names

        OUTPUT: new Magma element that is equal to value with given gens

        EXAMPLES::

            sage: R = magma.objgens('PolynomialRing(Rationals(),2)', 'alpha,beta')    # optional - magma
            sage: R.gens()          # optional - magma
            (alpha, beta)

        Because of how Magma works you can use this to change the variable
        names of the generators of an object::

            sage: S = magma.objgens(R, 'X,Y')          # optional - magma
            sage: R                                    # optional - magma
            Polynomial ring of rank 2 over Rational Field
            Order: Lexicographical
            Variables: X, Y
            sage: S                                    # optional - magma
            Polynomial ring of rank 2 over Rational Field
            Order: Lexicographical
            Variables: X, Y
        """
    def __call__(self, x, gens=None):
        """
        Coerce x into this Magma interpreter interface.

        INPUT:

        - ``x`` -- object

        - ``gens`` -- string; names of generators of self,
          separated by commas

        OUTPUT: :class:`MagmaElement`

        EXAMPLES::

            sage: # optional - magma
            sage: magma(EllipticCurve('37a'))
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: magma('EllipticCurve([GF(5)|1,2,3,4,1])')
            Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 1 over GF(5)
            sage: magma('PowerSeriesRing(Rationals())', 't')
            Power series ring in t over Rational Field
            sage: magma('PolynomialRing(RationalField(), 3)', 'x,y,z')
            Polynomial ring of rank 3 over Rational Field
            Order: Lexicographical
            Variables: x, y, z

        We test a coercion between different Magma instances::

            sage: m = Magma()
            sage: n = Magma()
            sage: a = n(m(2))           # optional - magma
            sage: a.parent() is n       # optional - magma
            True
            sage: a.parent() is m       # optional - magma
            False

        We test caching::

            sage: # optional - magma
            sage: R.<x> =  ZZ[]
            sage: magma(R) is magma(R)
            True
            sage: m = Magma()
            sage: m(R)
            Univariate Polynomial Ring in x over Integer Ring
            sage: m(R) is magma(R)
            False
            sage: R._magma_cache
            {Magma: Univariate Polynomial Ring in x over Integer Ring,
             Magma: Univariate Polynomial Ring in x over Integer Ring}

            sage: # optional - magma
            sage: P.<x,y> = PolynomialRing(GF(127))
            sage: m = Magma()
            sage: m(P)
            Polynomial ring of rank 2 over GF(127)
            Order: Graded Reverse Lexicographical
            Variables: x, y
            sage: P._magma_cache
            {Magma: Polynomial ring of rank 2 over GF(127)
            Order: Graded Reverse Lexicographical
            Variables: x, y}
        """
    def clear(self, var) -> None:
        """
        Clear the variable named var and make it available to be used
        again.

        INPUT:

        - ``var`` -- string

        EXAMPLES::

            sage: magma = Magma()      # optional - magma
            sage: magma.clear('foo')   # sets foo to 0 in magma; optional - magma
            sage: magma.eval('foo')    # optional - magma
            '0'

        Because we cleared foo, it is set to be used as a variable name in
        the future::

            sage: a = magma('10')      # optional - magma
            sage: a.name()             # optional - magma
            'foo'

        The following tests that the whole variable clearing and freeing
        system is working correctly.

        ::

            sage: # optional - magma
            sage: magma = Magma()
            sage: a = magma('100')
            sage: a.name()
            '_sage_[1]'
            sage: del a
            sage: b = magma('257')
            sage: b.name()
            '_sage_[1]'
            sage: del b
            sage: magma('_sage_[1]')
            0
        """
    def cputime(self, t=None):
        """
        Return the CPU time in seconds that has elapsed since this Magma
        session started. This is a floating point number, computed by
        Magma.

        If t is given, then instead return the floating point time from
        when t seconds had elapsed. This is useful for computing elapsed
        times between two points in a running program.

        INPUT:

        - ``t`` -- float (default: ``None``); if not None, return
          cputime since t

        OUTPUT:

        - ``float`` -- seconds

        EXAMPLES::

            sage: # optional - magma
            sage: type(magma.cputime())
            <... 'float'>
            sage: magma.cputime()  # random
            1.9399999999999999
            sage: t = magma.cputime()
            sage: magma.cputime(t)  # random
            0.02
        """
    def chdir(self, dir) -> None:
        '''
        Change the Magma interpreter\'s current working directory.

        INPUT:

        - ``dir`` -- string

        EXAMPLES::

            sage: magma.chdir(\'/\')                 # optional - magma
            sage: magma.eval(\'System("pwd")\')      # optional - magma
            \'/\'
        '''
    def attach(self, filename) -> None:
        """
        Attach the given file to the running instance of Magma.

        Attaching a file in Magma makes all intrinsics defined in the file
        available to the shell. Moreover, if the file doesn't start with
        the ``freeze;`` command, then the file is reloaded
        whenever it is changed. Note that functions and procedures defined
        in the file are *not* available. For only those, use
        ``magma.load(filename)``.

        INPUT:

        - ``filename`` -- string

        EXAMPLES: Attaching a file that exists is fine::

            sage: SAGE_EXTCODE = SAGE_ENV['SAGE_EXTCODE']               # optional - magma
            sage: magma.attach('%s/magma/sage/basic.m'%SAGE_EXTCODE)    # optional - magma

        Attaching a file that doesn't exist raises an exception::

            sage: SAGE_EXTCODE = SAGE_ENV['SAGE_EXTCODE']                 # optional - magma
            sage: magma.attach('%s/magma/sage/basic2.m'%SAGE_EXTCODE)     # optional - magma
            Traceback (most recent call last):
            ...
            RuntimeError: Error evaluating Magma code...
        """
    Attach = attach
    def attach_spec(self, filename) -> None:
        """
        Attach the given spec file to the running instance of Magma.

        This can attach numerous other files to the running Magma (see the
        Magma documentation for more details).

        INPUT:

        - ``filename`` -- string

        EXAMPLES::

            sage: SAGE_EXTCODE = SAGE_ENV['SAGE_EXTCODE']            # optional - magma
            sage: magma.attach_spec('%s/magma/spec'%SAGE_EXTCODE)    # optional - magma
            sage: magma.attach_spec('%s/magma/spec2'%SAGE_EXTCODE)   # optional - magma
            Traceback (most recent call last):
            ...
            RuntimeError: Can't open package spec file .../magma/spec2 for reading (No such file or directory)
        """
    AttachSpec = attach_spec
    def load(self, filename):
        '''
        Load the file with given filename using the \'load\' command in the
        Magma shell.

        Loading a file in Magma makes all the functions and procedures in
        the file available. The file should not contain any intrinsics (or
        you will get errors). It also runs code in the file, which can
        produce output.

        INPUT:

        - ``filename`` -- string

        OUTPUT: output printed when loading the file

        EXAMPLES::

            sage: from tempfile import NamedTemporaryFile as NTF
            sage: with NTF(mode=\'w+t\', suffix=\'.m\') as f:  # optional - magma
            ....:     _ = f.write(\'function f(n) return n^2; end function;\\nprint "hi";\')
            ....:     print(magma.load(f.name))
            Loading "....m"
            hi
            sage: magma(\'f(12)\')  # optional - magma
            144
        '''
    def function_call(self, function, args=[], params={}, nvals: int = 1):
        """
        Return result of evaluating a Magma function with given input,
        parameters, and asking for nvals as output.

        INPUT:

        - ``function`` -- string, a Magma function name

        - ``args`` -- list of objects coercible into this magma
          interface

        - ``params`` -- Magma parameters, passed in after a
          colon

        - ``nvals`` -- number of return values from the
          function to ask Magma for

        OUTPUT: instance of :class:`MagmaElement` or a tuple of ``nvals`` many
        :class:`MagmaElement` instances

        EXAMPLES::

            sage: magma.function_call('Factorization', 100)    # optional - magma
            [ <2, 2>, <5, 2> ]
            sage: magma.function_call('NextPrime', 100, {'Proof':False})    # optional - magma
            101
            sage: magma.function_call('PolynomialRing', [QQ,2])      # optional - magma
            Polynomial ring of rank 2 over Rational Field
            Order: Lexicographical
            Variables: $.1, $.2

        Next, we illustrate multiple return values::

            sage: magma.function_call('IsSquare', 100)         # optional - magma
            true
            sage: magma.function_call('IsSquare', 100, nvals=2)     # optional - magma
            (true, 10)
            sage: magma.function_call('IsSquare', 100, nvals=3)     # optional - magma
            Traceback (most recent call last):
            ...
            RuntimeError: Error evaluating Magma code...
            Runtime error in :=: Expected to assign 3 value(s) but only computed 2 value(s)
        """
    def bar_call(self, left, name, gens, nvals: int = 1):
        """
        This is a wrapper around the Magma constructor.

        nameleft gens

        returning nvals.

        INPUT:

        - ``left`` -- something coerceable to a magma object

        - ``name`` -- name of the constructor, e.g., sub, quo,
          ideal, etc.

        - ``gens`` -- if a list/tuple, each item is coerced to
          magma; otherwise gens itself is converted to magma

        - ``nvals`` -- positive integer; number of return
          values

        OUTPUT: a single magma object if nvals == 1; otherwise a tuple of
        nvals magma objects.

        EXAMPLES: The bar_call function is used by the sub, quo, and ideal
        methods of Magma elements. Here we illustrate directly using
        bar_call to create quotients::

            sage: # optional - magma
            sage: V = magma.RModule(ZZ,3)
            sage: V
            RModule(IntegerRing(), 3)
            sage: magma.bar_call(V, 'quo', [[1,2,3]], nvals=1)
            RModule(IntegerRing(), 2)
            sage: magma.bar_call(V, 'quo', [[1,2,3]], nvals=2)
            (RModule(IntegerRing(), 2),
             Mapping from: RModule(IntegerRing(), 3) to RModule(IntegerRing(), 2))
            sage: magma.bar_call(V, 'quo', V, nvals=2)
            (RModule(IntegerRing(), 0),
             Mapping from: RModule(IntegerRing(), 3) to RModule(IntegerRing(), 0))
        """
    def console(self) -> None:
        """
        Run a command line Magma session. This session is completely
        separate from this Magma interface.

        EXAMPLES::

            sage: magma.console()             # not tested
            Magma V2.14-9     Sat Oct 11 2008 06:36:41 on one      [Seed = 1157408761]
            Type ? for help.  Type <Ctrl>-D to quit.
            >
            Total time: 2.820 seconds, Total memory usage: 3.95MB
        """
    def version(self):
        """
        Return the version of Magma that you have in your PATH on your
        computer.

        OUTPUT:

        - ``numbers`` -- 3-tuple: major, minor, etc.

        - ``string`` -- version as a string

        EXAMPLES::

            sage: magma.version()       # random, optional - magma
            ((2, 14, 9), 'V2.14-9')
        """
    def help(self, s) -> None:
        '''
        Return Magma help on string s.

        This returns what typing ?s would return in Magma.

        INPUT:

        - ``s`` -- string

        OUTPUT: string

        EXAMPLES::

            sage: magma.help("NextPrime")       # optional - magma
            ===============================================================================
            PATH: /magma/ring-field-algebra/integer/prime/next-previous/NextPrime
            KIND: Intrinsic
            ===============================================================================
            NextPrime(n) : RngIntElt -> RngIntElt
            NextPrime(n: parameter) : RngIntElt -> RngIntElt
            ...
        '''
    def ideal(self, L):
        """
        Return the Magma ideal defined by L.

        INPUT:

        - ``L`` -- list of elements of a Sage multivariate
          polynomial ring

        OUTPUT: the magma ideal generated by the elements of L

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: magma.ideal([x^2, y^3*x])         # optional - magma
            Ideal of Polynomial ring of rank 2 over Rational Field
            Order: Graded Reverse Lexicographical
            Variables: x, y
            Homogeneous
            Basis:
            [
            x^2,
            x*y^3
            ]
        """
    def set_verbose(self, type, level) -> None:
        '''
        Set the verbosity level for a given algorithm, class, etc. in
        Magma.

        INPUT:

        - ``type`` -- string (e.g. \'Groebner\')

        - ``level`` -- integer >= 0

        EXAMPLES::

            sage: magma.set_verbose("Groebner", 2)      # optional - magma
            sage: magma.get_verbose("Groebner")         # optional - magma
            2
        '''
    SetVerbose = set_verbose
    def get_verbose(self, type):
        '''
        Get the verbosity level of a given algorithm class etc. in Magma.

        INPUT:

        - ``type`` -- string (e.g. \'Groebner\'), see Magma
          documentation

        EXAMPLES::

            sage: magma.set_verbose("Groebner", 2)        # optional - magma
            sage: magma.get_verbose("Groebner")           # optional - magma
            2
        '''
    GetVerbose = get_verbose
    def set_nthreads(self, n) -> None:
        """
        Set the number of threads used for parallelized algorithms in Magma.

        INPUT:

        - ``n`` -- number of threads

        EXAMPLES::

            sage: magma.set_nthreads(2)                #optional - magma
            sage: magma.get_nthreads()                 #optional - magma
            2
        """
    SetNthreads = set_nthreads
    def get_nthreads(self):
        """
        Get the number of threads used in Magma.

        EXAMPLES::

            sage: magma.set_nthreads(2)                #optional - magma
            sage: magma.get_nthreads()                 #optional - magma
            2
        """
    GetNthreads = get_nthreads

class MagmaFunctionElement(FunctionElement):
    def __call__(self, *args, **kwds):
        """
        Return the result of calling this Magma function at given inputs.

        Use the optional nvals keyword argument to specify that there are
        multiple return values.

        EXAMPLES: We create a MagmaFunctionElement::

            sage: # optional - magma
            sage: n = magma(-15)
            sage: f = n.Factorisation
            sage: type(f)
            <class 'sage.interfaces.magma.MagmaFunctionElement'>
            sage: f()
            [ <3, 1>, <5, 1> ]

        We verify that the nvals argument works.

        ::

            sage: f(nvals=2)                            # optional - magma
            ([ <3, 1>, <5, 1> ], -1)

        This illustrates the more conventional way of calling a method on
        an object. It's equivalent to the above, but done in all in one
        step.

        ::

            sage: n.Factorization(nvals = 2)            # optional - magma
            ([ <3, 1>, <5, 1> ], -1)
        """

class MagmaFunction(ExpectFunction):
    def __call__(self, *args, **kwds):
        """
        Return the result of calling this Magma function at given inputs.

        Use the optional nvals keyword argument to specify that there are
        multiple return values.

        EXAMPLES: We create a MagmaFunction::

            sage: f = magma.Factorisation                   # optional - magma
            sage: type(f)                                   # optional - magma
            <class 'sage.interfaces.magma.MagmaFunction'>
            sage: f(-15)                                    # optional - magma
            [ <3, 1>, <5, 1> ]

        We verify that the nvals argument works.

        ::

            sage: f(-15, nvals=2)                           # optional - magma
            ([ <3, 1>, <5, 1> ], -1)
            sage: f.__call__(-15, nvals=2)                  # optional - magma
            ([ <3, 1>, <5, 1> ], -1)
        """

def is_MagmaElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`MagmaElement`, and ``False``
    otherwise.

    INPUT:

    - ``x`` -- any object

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.interfaces.magma import is_MagmaElement
        sage: is_MagmaElement(2)
        doctest:...: DeprecationWarning: the function is_MagmaElement is deprecated; use isinstance(x, sage.interfaces.abc.MagmaElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: is_MagmaElement(magma(2))                    # optional - magma
        True
    """

class MagmaElement(ExtraTabCompletion, ExpectElement, sage.interfaces.abc.MagmaElement):
    def __getattr__(self, attrname):
        """
        INPUT:

        - ``attrname`` -- string

        OUTPUT: a Magma function partially evaluated with ``self`` as the first
        input

        .. NOTE::

           If the input ``attrname`` starts with an underscore, an
           :exc:`AttributeError` is raised so that the actual
           Python _ method/value can be accessed.

        EXAMPLES::

            sage: # optional - magma
            sage: n = magma(-15)
            sage: type(n)
            <class 'sage.interfaces.magma.MagmaElement'>
            sage: f = n.__getattr__('Factorization')
            sage: type(f)
            <class 'sage.interfaces.magma.MagmaFunctionElement'>
            sage: f
            Partially evaluated Magma function or intrinsic 'Factorization'
            ...
        """
    def AssignNames(self, names) -> None:
        """
        EXAMPLES::

            sage: # optional - magma
            sage: S = magma.PolynomialRing(magma.Integers(), 2)
            sage: S.AssignNames(['a', 'b'])
            sage: S.1
            a
            sage: S.1^2 + S.2
            a^2 + b
        """
    assign_names = AssignNames
    def gen(self, n):
        """
        Return the `n`-th generator of this Magma element.

        Note that generators are 1-based in Magma rather than 0-based!

        INPUT:

        - ``n`` -- *positive* integer

        OUTPUT: :class:`MagmaElement`

        EXAMPLES::

            sage: k.<a> = GF(9)
            sage: magma(k).gen(1)         # optional -- magma
            a
            sage: R.<s,t,w> = k[]
            sage: m = magma(R)            # optional -- magma
            sage: m.gen(1)                # optional -- magma
            s
            sage: m.gen(2)                # optional -- magma
            t
            sage: m.gen(3)                # optional -- magma
            w
            sage: m.gen(0)                # optional -- magma
            Traceback (most recent call last):
            ...
            IndexError: index must be positive since Magma indexes are 1-based
            sage: m.gen(4)                # optional -- magma
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
        """
    def gens(self) -> tuple:
        '''
        Return generators for ``self``.

        If ``self`` is named X in Magma, this function evaluates X.1, X.2,
        etc., in Magma until an error occurs. It then returns a Sage tuple
        of the resulting X.i. Note - I do not think there is a Magma command
        that returns the list of valid X.i. There are numerous ad hoc
        functions for various classes but nothing systematic. This function
        gets around that problem. Again, this is something that should
        probably be reported to the Magma group and fixed there.

        AUTHORS:

        - William Stein (2006-07-02)

        EXAMPLES::

            sage: magma("VectorSpace(RationalField(),3)").gens()         # optional - magma
            ((1 0 0), (0 1 0), (0 0 1))
            sage: magma("AbelianGroup(EllipticCurve([1..5]))").gens()    # optional - magma
            ($.1,)
        '''
    def gen_names(self):
        """
        Return list of Magma variable names of the generators of ``self``.

        .. NOTE::

           As illustrated below, these are not the print names of the
           the generators of the Magma object, but special variable
           names in the Magma session that reference the generators.

        EXAMPLES::

            sage: R.<x,zw> = QQ[]
            sage: S = magma(R)               # optional - magma
            sage: S.gen_names()              # optional - magma
            ('_sage_[...]', '_sage_[...]')
            sage: magma(S.gen_names()[1])    # optional - magma
            zw
        """
    def evaluate(self, *args):
        """
        Evaluate ``self`` at the inputs.

        INPUT:

        - ``*args`` -- import arguments

        OUTPUT: self(\\*args)

        EXAMPLES::

            sage: # optional - magma
            sage: f = magma('Factorization')
            sage: f.evaluate(15)
            [ <3, 1>, <5, 1> ]
            sage: f(15)
            [ <3, 1>, <5, 1> ]
            sage: f = magma('GCD')
            sage: f.evaluate(15,20)
            5

            sage: m = matrix(QQ, 2, 2, [2,3,5,7])      # optional - magma
            sage: f = magma('ElementaryDivisors')      # optional - magma
            sage: f.evaluate(m)                        # optional - magma
            [ 1, 1 ]
        """
    eval = evaluate
    def __call__(self, *args):
        """
        Coerce something into the object (using the Magma ! notation).

        For function calls, use self.eval(...).

        EXAMPLES::

            sage: # optional - magma
            sage: M = magma.RMatrixSpace(magma.IntegerRing(), 2, 2)
            sage: A = M([1,2,3,4]); A
            [1 2]
            [3 4]
            sage: type(A)
            <class 'sage.interfaces.magma.MagmaElement'>
            sage: A.Type()
            ModMatRngElt
        """
    def __iter__(self):
        """
        Return iterator over this Magma element.

        OUTPUT: generator object

        .. warning::

           Internally this constructs the list of elements in ``self`` in
           Magma, which is not a lazy operation. This is because Magma
           doesn't have a notion of lazy iterators, unfortunately.

        EXAMPLES::

            sage: # optional - magma
            sage: V = magma('VectorSpace(GF(3),2)')
            sage: V
            Full Vector space of degree 2 over GF(3)
            sage: w = V.__iter__(); w
            <generator object ...__iter__ at ...>
            sage: next(w)
            (0 0)
            sage: next(w)
            (1 0)
            sage: list(w)
            [(2 0), (0 1), (1 1), (2 1), (0 2), (1 2), (2 2)]
        """
    def __len__(self) -> int:
        """
        Return cardinality of this Magma element.

        This is the same as ``#self`` in Magma.

        EXAMPLES::

            sage: # optional - magma
            sage: V = magma('VectorSpace(GF(3),2)')
            sage: V
            Full Vector space of degree 2 over GF(3)
            sage: len(V)
            9
            sage: V.__len__()
            9
        """
    def set_magma_attribute(self, attrname, value) -> None:
        '''
        INPUT:

        - ``attrname`` -- string
        - ``value`` -- something coercible to a MagmaElement

        EXAMPLES::

            sage: # optional - magma
            sage: V = magma("VectorSpace(RationalField(),2)")
            sage: V.set_magma_attribute(\'M\',10)
            sage: V.get_magma_attribute(\'M\')
            10
            sage: V.M
            10
        '''
    def get_magma_attribute(self, attrname):
        '''
        Return value of a given Magma attribute. This is like selfattrname
        in Magma.

        OUTPUT: :class:`MagmaElement`

        EXAMPLES::

            sage: # optional - magma
            sage: V = magma("VectorSpace(RationalField(),10)")
            sage: V.set_magma_attribute(\'M\',\'"hello"\')
            sage: V.get_magma_attribute(\'M\')
            hello
            sage: V.M
            hello
        '''
    def list_attributes(self):
        '''
        Return the attributes of self, obtained by calling the
        ListAttributes function in Magma.

        OUTPUT: list of strings

        EXAMPLES: We observe that vector spaces in Magma have numerous
        funny and mysterious attributes. ::

            sage: V = magma("VectorSpace(RationalField(),2)")        # optional - magma
            sage: v = V.list_attributes(); v.sort()               # optional - magma
            sage: print(v)     # optional - magma
            [\'Coroots\', \'Involution\', ..., \'p\', \'ssbasis\', \'weights\']
        '''
    def methods(self, any: bool = False):
        '''
        Return signatures of all Magma intrinsics that can take ``self`` as the
        first argument, as strings.

        INPUT:

        - ``any`` -- boolean (default: ``False``); if ``True``, also
          include signatures with Any as first argument

        OUTPUT: list of strings

        EXAMPLES::

            sage: v = magma(\'2/3\').methods()          # optional - magma
            sage: v[0]                                # optional - magma
            "\'*\'..."
        '''
    def __floordiv__(self, x):
        """
        Quotient of division of ``self`` by ``other``. This is denoted ``//``
        (``div`` in magma).

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: magma(5)//magma(2)     # optional - magma
            2
            sage: m = magma(x*z + x*y)   # optional - magma
            sage: n = magma(x)           # optional - magma
            sage: m//n                   # optional - magma
            y + z
        """
    def __bool__(self) -> bool:
        '''
        Return ``True`` if ``self`` is nonzero according to Magma.

        If Magma cannot decide, i.e., is raising an error
        then also return ``True``.

        EXAMPLES: We define a Magma vector space::

            sage: V = magma(\'VectorSpace(GF(3),2)\'); V    # optional - magma
            Full Vector space of degree 2 over GF(3)

        The first generator is nonzero::

            sage: bool(V.gen(1))                          # optional - magma
            True

        The zero element is zero::

            sage: bool(V(0))                              # optional - magma
            False

        The space itself is nonzero (the default - in Magma no comparison
        to 0 is possible)::

            sage: bool(V)                                 # optional - magma
            True

        Note that ``bool`` calls ``__bool__`` in Python 3.

        Test use in bool conversions of bools::

            sage: # optional - magma
            sage: bool(magma(False))
            False
            sage: bool(magma(True))
            True
            sage: bool(magma(1))
            True
            sage: bool(magma(0))
            False

        TESTS:

        Verify that :issue:`32602` is fixed::

            sage: magma("1 eq 0").bool()                  # optional - magma
            False
            sage: magma("1 eq 1").bool()                  # optional - magma
            True
            sage: Q.<x> = PolynomialRing(GF(3))
            sage: u = x^6+x^4+2*x^3+2*x+1
            sage: F0 = magma.FunctionField(GF(3))         # optional - magma
            sage: bool(F0.1)                              # optional - magma
            True
        '''
    def sub(self, gens):
        """
        Return the sub-object of ``self`` with given gens.

        INPUT:

        - ``gens`` -- object or list/tuple of generators

        EXAMPLES::

            sage: V = magma('VectorSpace(RationalField(),3)')       # optional - magma
            sage: W = V.sub([ [1,2,3], [1,1,2] ]); W                # optional - magma
            Vector space of degree 3, dimension 2 over Rational Field
            Generators:
            (1 2 3)
            (1 1 2)
            Echelonized basis:
            (1 0 1)
            (0 1 1)
        """
    def quo(self, gens, **args):
        """
        Return the quotient of ``self`` by the given object or list of
        generators.

        INPUT:

        - ``gens`` -- object or list/tuple of generators
        - further named arguments that are ignored

        OUTPUT:

        - ``magma element`` -- the quotient object

        - ``magma element`` -- mapping from ``self`` to the
          quotient object

        EXAMPLES::

            sage: V = magma('VectorSpace(RationalField(),3)')       # optional - magma
            sage: V.quo([[1,2,3], [1,1,2]])                         # optional - magma
            (Full Vector space of degree 1 over Rational Field, Mapping from: Full Vector space of degree 3 over Rational Field to Full Vector space of degree 1 over Rational Field)

        We illustrate quotienting out by an object instead of a list of
        generators::

            sage: W = V.sub([ [1,2,3], [1,1,2] ])                   # optional - magma
            sage: V.quo(W)                                          # optional - magma
            (Full Vector space of degree 1 over Rational Field, Mapping from: Full Vector space of degree 3 over Rational Field to Full Vector space of degree 1 over Rational Field)

        We quotient a ZZ module out by a submodule.

        ::

            sage: # optional - magma
            sage: V = magma.RModule(ZZ,3); V
            RModule(IntegerRing(), 3)
            sage: W, phi = V.quo([[1,2,3]])
            sage: W
            RModule(IntegerRing(), 2)
            sage: phi
            Mapping from: RModule(IntegerRing(), 3) to RModule(IntegerRing(), 2)
        """
    def ideal(self, gens):
        """
        Return the ideal of ``self`` with given list of generators.

        INPUT:

        - ``gens`` -- object or list/tuple of generators

        OUTPUT:

        - ``magma element`` -- a Magma ideal

        EXAMPLES::

            sage: # optional - magma
            sage: R = magma('PolynomialRing(RationalField())')
            sage: R.assign_names(['x'])
            sage: x = R.1
            sage: R.ideal([x^2 - 1, x^3 - 1])
            Ideal of Univariate Polynomial Ring in x over Rational Field generated by x - 1
        """

magma: Incomplete

def reduce_load_Magma():
    """
    Used in unpickling a Magma interface.

    This functions just returns the global default Magma interface.

    EXAMPLES::

        sage: sage.interfaces.magma.reduce_load_Magma()
        Magma
    """
def magma_console() -> None:
    """
    Run a command line Magma session.

    EXAMPLES::

        sage: magma_console()             # not tested
        Magma V2.14-9     Sat Oct 11 2008 06:36:41 on one      [Seed = 1157408761]
        Type ? for help.  Type <Ctrl>-D to quit.
        >
        Total time: 2.820 seconds, Total memory usage: 3.95MB
    """

class MagmaGBLogPrettyPrinter:
    """
    A device which filters Magma Groebner basis computation logs.
    """
    cmd_inpt: Incomplete
    app_inpt: Incomplete
    deg_curr: Incomplete
    pol_curr: Incomplete
    verbosity: Incomplete
    style: Incomplete
    curr_deg: int
    curr_npairs: int
    max_deg: int
    storage: str
    sync: Incomplete
    def __init__(self, verbosity: int = 1, style: str = 'magma') -> None:
        '''
        Construct a new Magma Groebner Basis log pretty printer.

        INPUT:

        - ``verbosity`` -- how much information should be printed
          (between 0 and 1)

        - ``style`` -- if "magma" the full Magma log is printed; if
          \'sage\' only the current degree and the number of pairs in
          the queue is printed (default: ``\'magma\'``).

        EXAMPLES::

            sage: P.<x,y,z> = GF(32003)[]
            sage: I = sage.rings.ideal.Cyclic(P)
            sage: _ = I.groebner_basis(\'magma\',prot=\'sage\') # indirect doctest, optional - magma, not tested

            Leading term degree:  2. Critical pairs: 2.
            Leading term degree:  3. Critical pairs: 1.

            Highest degree reached during computation:  3.

            sage: P.<x,y,z> = GF(32003)[]
            sage: I = sage.rings.ideal.Cyclic(P)
            sage: _ = I.groebner_basis(\'magma\',prot=True) # indirect doctest, optional - magma, not tested
            ********************
            FAUGERE F4 ALGORITHM
            ********************
            Coefficient ring: GF(32003)
            Rank: 3
            Order: Graded Reverse Lexicographical
            NEW hash table
            Matrix kind: Modular FP
            Datum size: 4
            No queue sort
            Initial length: 3
            Inhomogeneous

            Initial queue setup time: 0.000
            Initial queue length: 2

            *******
            STEP 1
            Basis length: 3, queue length: 2, step degree: 2, num pairs: 1
            Basis total mons: 8, average length: 2.667
            Number of pair polynomials: 1, at 4 column(s), 0.000
            ...
            Total Faugere F4 time: 0.000, real time: 0.000

            sage: set_random_seed(1)
            sage: sr = mq.SR(1,1,2,4)
            sage: F,s = sr.polynomial_system()
            sage: I = F.ideal()
            sage: _ = I.groebner_basis(\'magma\',prot=\'sage\') # indirect doctest, optional - magma, not tested
            Leading term degree:  1. Critical pairs: 40.
            Leading term degree:  2. Critical pairs: 40.
            Leading term degree:  3. Critical pairs: 38.
            Leading term degree:  2. Critical pairs: 327.
            Leading term degree:  2. Critical pairs: 450.
            Leading term degree:  2. Critical pairs: 416.
            Leading term degree:  3. Critical pairs: 415.
            Leading term degree:  4. Critical pairs: 98 (all pairs of current degree eliminated by criteria).
            Leading term degree:  5. Critical pairs: 3 (all pairs of current degree eliminated by criteria).

            Highest degree reached during computation:  3.
        '''
    def write(self, s) -> None:
        """
        EXAMPLES::

            sage: P.<x,y,z> = GF(32003)[]
            sage: I = sage.rings.ideal.Katsura(P)
            sage: _ = I.groebner_basis('magma',prot=True) # indirect doctest, optional - magma
            ...
            ********************
            FAUGERE F4 ALGORITHM
            ********************
            ...
            Total Faugere F4 time: ..., real time: ...
        """
    def flush(self) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.magma import MagmaGBLogPrettyPrinter
            sage: logs = MagmaGBLogPrettyPrinter()
            sage: logs.flush()
        """

class MagmaGBDefaultContext:
    """
    Context to force preservation of verbosity options for Magma's
    Groebner basis computation.
    """
    magma: Incomplete
    def __init__(self, magma=None) -> None:
        """
        INPUT:

        - ``magma`` -- (default: ``magma_default``)

        EXAMPLES::

            sage: from sage.interfaces.magma import MagmaGBDefaultContext
            sage: magma.SetVerbose('Groebner',1) # optional - magma
            sage: with MagmaGBDefaultContext(): magma.GetVerbose('Groebner')  # optional - magma
            0
        """
    groebner_basis_verbose: Incomplete
    def __enter__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.magma import MagmaGBDefaultContext
            sage: magma.SetVerbose('Groebner',1) # optional - magma
            sage: with MagmaGBDefaultContext(): magma.GetVerbose('Groebner')  # optional - magma
            0
        """
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.magma import MagmaGBDefaultContext
            sage: magma.SetVerbose('Groebner',1) # optional - magma
            sage: with MagmaGBDefaultContext(): magma.GetVerbose('Groebner')  # optional - magma
            0
            sage: magma.GetVerbose('Groebner') # optional - magma
            1
        """

def magma_gb_standard_options(func):
    '''
    Decorator to force default options for Magma.

    EXAMPLES::

        sage: P.<a,b,c,d,e> = PolynomialRing(GF(127))
        sage: J = sage.rings.ideal.Cyclic(P).homogenize()
        sage: from sage.misc.sageinspect import sage_getsource
        sage: "mself" in sage_getsource(J._groebner_basis_magma)
        True
    '''
