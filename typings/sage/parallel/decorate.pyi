from . import multiprocessing_sage as multiprocessing_sage
from _typeshed import Incomplete
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.rings.integer import Integer as Integer

def normalize_input(a):
    """
    Convert ``a`` to a pair ``(args, kwds)`` using some rules:

    - if already of that form, leave that way.
    - if ``a`` is a tuple make ``(a,{})``
    - if ``a`` is a dict make ``(tuple(),a)``
    - otherwise make ``((a,),{})``

    INPUT:

    - ``a`` -- object

    OUTPUT:

    - ``args`` -- tuple
    - ``kwds`` -- dictionary

    EXAMPLES::

        sage: sage.parallel.decorate.normalize_input( (2, {3:4}) )
        ((2, {3: 4}), {})
        sage: sage.parallel.decorate.normalize_input( (2,3) )
        ((2, 3), {})
        sage: sage.parallel.decorate.normalize_input( {3:4} )
        ((), {3: 4})
        sage: sage.parallel.decorate.normalize_input( 5 )
        ((5,), {})
    """

class Parallel:
    """
    Create a ``parallel``-decorated function.
    This is the object created by :func:`parallel`.
    """
    p_iter: Incomplete
    def __init__(self, p_iter: str = 'fork', ncpus=None, **kwds) -> None:
        """
        EXAMPLES::

            sage: P = sage.parallel.decorate.Parallel(); P
            <sage.parallel.decorate.Parallel object at 0x...>
        """
    def __call__(self, f):
        """
        Create a callable object that wraps ``f`` and that when called
        with a list of inputs returns an iterator over pairs ``(x,
        f(x))`` in possibly random order. Here ``x`` is replaced by
        its normalized form ``(args, kwds)`` using
        :func:`normalize_inputs`.

        INPUT:

        - ``f`` -- Python callable object or function

        OUTPUT: decorated version of ``f``

        EXAMPLES::

            sage: from sage.parallel.decorate import Parallel
            sage: p = Parallel()
            sage: f = x^2 - 1                                                           # needs sage.symbolic
            sage: p(f)                                                                  # needs sage.symbolic
            <sage.parallel.decorate.ParallelFunction object at ...>

            sage: P = sage.parallel.decorate.Parallel()
            sage: def g(n, m): return n+m
            sage: h = P(g)          # indirect doctest
            sage: list(h([(2,3)]))
            [(((2, 3), {}), 5)]
        """

class ParallelFunction:
    """
    Class which parallelizes a function or class method.
    This is typically accessed indirectly through
    :meth:`Parallel.__call__`.
    """
    parallel: Incomplete
    func: Incomplete
    def __init__(self, parallel, func) -> None:
        """
        .. NOTE::

            This is typically accessed indirectly through
            :meth:`Parallel.__call__`.

        INPUT:

        - ``parallel`` -- a :class:`Parallel` object which controls
          how the parallel execution will be done

        - ``func`` -- Python callable object or function
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: from sage.parallel.decorate import Parallel
            sage: p = Parallel()
            sage: def f(x):
            ....:     return x*x
            sage: pf = p(f); pf
            <sage.parallel.decorate.ParallelFunction object at ...>
            sage: pf(2)
            4
            sage: sorted(pf([2,3]))
            [(((2,), {}), 4), (((3,), {}), 9)]
        """
    def __get__(self, instance, owner):
        """
        Implement part of the descriptor protocol for
        :class:`ParallelFunction` objects.

        .. NOTE::

            This is the key to fixing :issue:`11461`.

        EXAMPLES:

        We verify that the decorated functions work correctly on
        methods, classmethods, and staticmethods, for both the
        parallel and non-parallel versions::

            sage: class Foo():
            ....:     @parallel(2)
            ....:     def square(self, n):
            ....:         return n*n
            ....:     @parallel(2)
            ....:     @classmethod
            ....:     def square_classmethod(cls, n):
            ....:         return n*n
            ....:     @parallel(2)
            ....:     @staticmethod
            ....:     def square_staticmethod(n):
            ....:         return n*n
            sage: a = Foo()
            sage: a.square(3)
            9
            sage: sorted(a.square([2,3]))
            [(((2,), {}), 4), (((3,), {}), 9)]
            sage: a.square_classmethod(3)
            9
            sage: sorted(a.square_classmethod([2,3]))
            [(((2,), {}), 4), (((3,), {}), 9)]
            sage: Foo.square_classmethod(3)
            9
            sage: sorted(Foo.square_classmethod([2,3]))
            [(((2,), {}), 4), (((3,), {}), 9)]
            sage: a.square_staticmethod(3)
            9
            sage: sorted(a.square_staticmethod([2,3]))
            [(((2,), {}), 4), (((3,), {}), 9)]
            sage: Foo.square_staticmethod(3)
            9
            sage: sorted(Foo.square_staticmethod([2,3]))
            [(((2,), {}), 4), (((3,), {}), 9)]
        """

def parallel(p_iter: str = 'fork', ncpus=None, **kwds):
    '''
    This is a decorator that gives a function a parallel interface,
    allowing it to be called with a list of inputs, whose values will
    be computed in parallel.

    .. warning::

         The parallel subprocesses will not have access to data
         created in pexpect interfaces.  This behavior with respect to
         pexpect interfaces is very important to keep in mind when
         setting up certain computations.  It\'s the one big limitation
         of this decorator.

    INPUT:

    - ``p_iter`` -- parallel iterator function or string:
      - ``\'fork\'`` -- (default) use a new forked subprocess for each input
      - ``\'multiprocessing\'`` -- use multiprocessing library
      - ``\'reference\'`` -- use a fake serial reference implementation
    - ``ncpus`` -- integer; maximal number of subprocesses to use at the same time
    - ``timeout`` -- number of seconds until each subprocess is killed (only supported
      by ``\'fork\'``; zero means not at all)
    - ``reseed_rng``: reseed the rng (random number generator) in each subprocess

    .. warning::

         If you use anything but ``\'fork\'`` above, then a whole new
         subprocess is spawned, so none of your local state (variables,
         certain functions, etc.) is available.

    EXAMPLES:

    We create a simple decoration for a simple function.  The number
    of cpus (or cores, or hardware threads) is automatically detected::

        sage: @parallel
        ....: def f(n): return n*n
        sage: f(10)
        100
        sage: sorted(list(f([1,2,3])))
        [(((1,), {}), 1), (((2,), {}), 4), (((3,), {}), 9)]

    We use exactly two cpus::

        sage: @parallel(2)
        ....: def f(n): return n*n


    We create a decorator that uses three subprocesses, and times out
    individual processes after 10 seconds::

        sage: @parallel(ncpus=3, timeout=10)
        ....: def fac(n): return factor(2^n-1)
        sage: for X, Y in sorted(list(fac([101,119,151,197,209]))): print((X,Y))        # needs sage.libs.pari
        (((101,), {}), 7432339208719 * 341117531003194129)
        (((119,), {}), 127 * 239 * 20231 * 131071 * 62983048367 * 131105292137)
        (((151,), {}), 18121 * 55871 * 165799 * 2332951 * 7289088383388253664437433)
        (((197,), {}), 7487 * 26828803997912886929710867041891989490486893845712448833)
        (((209,), {}), 23 * 89 * 524287 * 94803416684681 * 1512348937147247 * 5346950541323960232319657)

        sage: @parallel(\'multiprocessing\')
        ....: def f(N): return N^2
        sage: v = list(f([1,2,4])); v.sort(); v
        [(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
        sage: @parallel(\'reference\')
        ....: def f(N): return N^2
        sage: v = list(f([1,2,4])); v.sort(); v
        [(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]

    For functions that take multiple arguments, enclose the arguments in tuples
    when calling the parallel function::

        sage: @parallel
        ....: def f(a, b): return a*b
        sage: for X, Y in sorted(list(f([(2,3),(3,5),(5,7)]))): print((X, Y))
        (((2, 3), {}), 6)
        (((3, 5), {}), 15)
        (((5, 7), {}), 35)

    For functions that take a single tuple as an argument, enclose it in an
    additional tuple at call time, to distinguish it as the first argument,
    as opposed to a tuple of arguments::

        sage: @parallel
        ....: def firstEntry(aTuple): return aTuple[0]
        sage: for X, Y in sorted(list(firstEntry([((1,2,3,4),),((5,6,7,8),)]))): print((X, Y))
        ((((1, 2, 3, 4),), {}), 1)
        ((((5, 6, 7, 8),), {}), 5)

    The parallel decorator also works with methods, classmethods, and
    staticmethods.  Be sure to apply the parallel decorator after ("above")
    either the ``classmethod`` or ``staticmethod`` decorators::

        sage: class Foo():
        ....:     @parallel(2)
        ....:     def square(self, n):
        ....:         return n*n
        ....:     @parallel(2)
        ....:     @classmethod
        ....:     def square_classmethod(cls, n):
        ....:         return n*n
        sage: a = Foo()
        sage: a.square(3)
        9
        sage: sorted(a.square([2,3]))
        [(((2,), {}), 4), (((3,), {}), 9)]
        sage: Foo.square_classmethod(3)
        9
        sage: sorted(Foo.square_classmethod([2,3]))
        [(((2,), {}), 4), (((3,), {}), 9)]
        sage: Foo.square_classmethod(3)
        9

    By default, all subprocesses use the same random seed and therefore the same deterministic randomness.
    For functions that should be randomized, we can reseed the random seed in each subprocess::

        sage: @parallel(reseed_rng=True)
        ....: def unif(n): return ZZ.random_element(x=0, y=n)
        sage: set_random_seed(42)
        sage: sorted(unif([1000]*3)) # random
        [(((1000,), {}), 444), (((1000,), {}), 597), (((1000,), {}), 640)]

    .. warning::

       Currently, parallel methods do not work with the
       multiprocessing implementation.
    '''

class Fork:
    """
    A ``fork`` decorator class.
    """
    timeout: Incomplete
    verbose: Incomplete
    def __init__(self, timeout: int = 0, verbose: bool = False) -> None:
        """
        INPUT:

        - ``timeout`` -- (default: 0) kill the subprocess after it has run this
          many seconds (wall time), or if ``timeout`` is zero, do not kill it.
        - ``verbose`` -- boolean (default: ``False``); whether to print anything about
          what the decorator does (e.g., killing the subprocess)

        EXAMPLES::

            sage: sage.parallel.decorate.Fork()
            <sage.parallel.decorate.Fork object at 0x...>
            sage: sage.parallel.decorate.Fork(timeout=3)
            <sage.parallel.decorate.Fork object at 0x...>
        """
    def __call__(self, f):
        """
        INPUT:

        - ``f`` -- a function

        OUTPUT: a decorated function

        EXAMPLES::

            sage: F = sage.parallel.decorate.Fork(timeout=3)
            sage: def g(n, m): return n+m
            sage: h = F(g)     # indirect doctest
            sage: h(2,3)
            5
        """

def fork(f=None, timeout: int = 0, verbose: bool = False):
    '''
    Decorate a function so that when called it runs in a forked subprocess.

    This means that it will not have any in-memory side effects on the
    parent Sage process. The pexpect interfaces are all reset.

    INPUT:

    - ``f`` -- a function
    - ``timeout`` -- (default: 0) if positive, kill the subprocess after
      this many seconds (wall time)
    - ``verbose`` -- boolean (default: ``False``); whether to print anything
      about what the decorator does (e.g., killing the subprocess)

    .. warning::

        The forked subprocess will not have access to data created
        in pexpect interfaces.  This behavior with respect to pexpect
        interfaces is very important to keep in mind when setting up
        certain computations.  It\'s the one big limitation of this
        decorator.

    EXAMPLES:

    We create a function and run it with the ``fork`` decorator.  Note
    that it does not have a side effect.  Despite trying to change
    the global variable ``a`` below in ``g``, the variable ``a`` does not
    get changed::

        sage: a = 5
        sage: @fork
        ....: def g(n, m):
        ....:     global a
        ....:     a = 10
        ....:     return factorial(n).ndigits() + m
        sage: g(5, m=5)
        8
        sage: a
        5

    We use ``fork`` to make sure that the function terminates after 100 ms,
    no matter what::

        sage: @fork(timeout=0.1, verbose=True)
        ....: def g(n, m): return factorial(n).ndigits() + m
        sage: g(10^7, m=5)
        Killing subprocess ... with input ((10000000,), {\'m\': 5}) which took too long
        \'NO DATA (timed out)\'

    We illustrate that the state of the pexpect interface is not altered by
    forked functions (they get their own new pexpect interfaces!)::

        sage: # needs sage.libs.pari
        sage: gp.eval(\'a = 5\')
        \'5\'
        sage: @fork()
        ....: def g():
        ....:     gp.eval(\'a = 10\')
        ....:     return gp.eval(\'a\')
        sage: g()
        \'10\'
        sage: gp.eval(\'a\')
        \'5\'

    We illustrate that the forked function has its own pexpect
    interface::

        sage: gp.eval(\'a = 15\')                                                         # needs sage.libs.pari
        \'15\'
        sage: @fork()
        ....: def g(): return gp.eval(\'a\')
        sage: g()                                                                       # needs sage.libs.pari
        \'a\'

    We illustrate that segfaulting subprocesses are no trouble at all::

        sage: cython(\'def f(): print(<char*>0)\')                                        # needs sage.misc.cython
        sage: @fork
        ....: def g():
        ....:     os.environ["CYSIGNALS_CRASH_NDEBUG"]="yes" # skip enhanced backtrace (it is slow)
        ....:     f()
        sage: print("this works"); g()                                                  # needs sage.misc.cython
        this works...
        <BLANKLINE>
        ------------------------------------------------------------------------
        Unhandled SIG...
        ------------------------------------------------------------------------
        \'NO DATA\'
    '''
