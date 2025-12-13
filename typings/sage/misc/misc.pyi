import contextlib
import pdb
from _typeshed import Incomplete
from collections.abc import Generator
from sage.env import DOT_SAGE as DOT_SAGE, HOSTNAME as HOSTNAME
from sage.misc.lazy_import import lazy_import as lazy_import

LOCAL_IDENTIFIER: Incomplete

def try_read(obj, splitlines: bool = False):
    """
    Determine if a given object is a readable file-like object and if so
    read and return its contents.

    That is, the object has a callable method named ``read()`` which takes
    no arguments (except ``self``) then the method is executed and the
    contents are returned.

    Alternatively, if the ``splitlines=True`` is given, first ``splitlines()``
    is tried, then if that fails ``read().splitlines()``.

    If either method fails, ``None`` is returned.

    INPUT:

    - ``obj`` -- typically a `file` or `io.BaseIO` object, but any other
      object with a ``read()`` method is accepted

    - ``splitlines`` -- boolean (default: ``False``); if ``True``, return a
      list of lines instead of a string

    EXAMPLES::

        sage: import io
        sage: filename = tmp_filename()
        sage: from sage.misc.misc import try_read
        sage: with open(filename, 'w') as fobj:
        ....:     _ = fobj.write('a\\nb\\nc')
        sage: with open(filename) as fobj:
        ....:     print(try_read(fobj))
        a
        b
        c
        sage: with open(filename) as fobj:
        ....:     try_read(fobj, splitlines=True)
        ['a\\n', 'b\\n', 'c']

    The following example is identical to the above example on Python 3,
    but different on Python 2 where ``open != io.open``::

        sage: with io.open(filename) as fobj:
        ....:     print(try_read(fobj))
        a
        b
        c

    I/O buffers::

        sage: buf = io.StringIO('a\\nb\\nc')
        sage: print(try_read(buf))
        a
        b
        c
        sage: _ = buf.seek(0); try_read(buf, splitlines=True)
        ['a\\n', 'b\\n', 'c']
        sage: buf = io.BytesIO(b'a\\nb\\nc')
        sage: try_read(buf) == b'a\\nb\\nc'
        True
        sage: _ = buf.seek(0)
        sage: try_read(buf, splitlines=True) == [b'a\\n', b'b\\n', b'c']
        True

    Custom readable::

        sage: class MyFile():
        ....:     def read(self): return 'Hello world!'
        sage: try_read(MyFile())
        'Hello world!'
        sage: try_read(MyFile(), splitlines=True)
        ['Hello world!']

    Not readable::

        sage: try_read(1) is None
        True
    """
def exactly_one_is_true(iterable):
    """
    Return whether exactly one element of ``iterable`` evaluates ``True``.

    INPUT:

    - ``iterable`` -- an iterable object

    OUTPUT: boolean

    .. NOTE::

        The implementation is suggested by
        `stackoverflow entry <https://stackoverflow.com/a/16801605/1052778>`_.

    EXAMPLES::

        sage: from sage.misc.misc import exactly_one_is_true
        sage: exactly_one_is_true([])
        False
        sage: exactly_one_is_true([True])
        True
        sage: exactly_one_is_true([False])
        False
        sage: exactly_one_is_true([True, True])
        False
        sage: exactly_one_is_true([False, True])
        True
        sage: exactly_one_is_true([True, False, True])
        False
        sage: exactly_one_is_true([False, True, False])
        True
    """
def strunc(s, n: int = 60):
    """
    Truncate at first space after position n, adding '...' if
    nontrivial truncation.
    """
def newton_method_sizes(N):
    """
    Return a sequence of integers
    `1 = a_1 \\leq a_2 \\leq \\cdots \\leq a_n = N` such that
    `a_j = \\lceil a_{j+1} / 2 \\rceil` for all `j`.

    This is useful for Newton-style algorithms that double the
    precision at each stage. For example if you start at precision 1
    and want an answer to precision 17, then it's better to use the
    intermediate stages 1, 2, 3, 5, 9, 17 than to use 1, 2, 4, 8, 16,
    17.

    INPUT:

    - ``N`` -- positive integer

    EXAMPLES::

        sage: newton_method_sizes(17)
        [1, 2, 3, 5, 9, 17]
        sage: newton_method_sizes(16)
        [1, 2, 4, 8, 16]
        sage: newton_method_sizes(1)
        [1]

    AUTHORS:

    - David Harvey (2006-09-09)
    """
def compose(f, g):
    """
    Return the composition of one-variable functions: `f \\circ g`.

    See also :func:`nest()`

    INPUT:

    - ``f`` -- a function of one variable
    - ``g`` -- another function of one variable

    OUTPUT: a function, such that compose(f,g)(x) = f(g(x))

    EXAMPLES::

        sage: def g(x): return 3*x
        sage: def f(x): return x + 1
        sage: h1 = compose(f, g)
        sage: h2 = compose(g, f)
        sage: _ = var('x')                                                              # needs sage.symbolic
        sage: h1(x)                                                                     # needs sage.symbolic
        3*x + 1
        sage: h2(x)                                                                     # needs sage.symbolic
        3*x + 3

    ::

        sage: _ = function('f g')                                                       # needs sage.symbolic
        sage: _ = var('x')                                                              # needs sage.symbolic
        sage: compose(f, g)(x)                                                          # needs sage.symbolic
        f(g(x))
    """
def nest(f, n, x):
    """
    Return `f(f(...f(x)...))`, where the composition occurs n times.

    See also :func:`compose()` and :func:`self_compose()`

    INPUT:

    - ``f`` -- a function of one variable
    - ``n`` -- nonnegative integer
    - ``x`` -- any input for `f`

    OUTPUT: `f(f(...f(x)...))`, where the composition occurs n times

    EXAMPLES::

        sage: def f(x): return x^2 + 1
        sage: x = var('x')                                                              # needs sage.symbolic
        sage: nest(f, 3, x)                                                             # needs sage.symbolic
        ((x^2 + 1)^2 + 1)^2 + 1

    ::

        sage: _ = function('f')                                                         # needs sage.symbolic
        sage: _ = var('x')                                                              # needs sage.symbolic
        sage: nest(f, 10, x)                                                            # needs sage.symbolic
        f(f(f(f(f(f(f(f(f(f(x))))))))))

    ::

        sage: _ = function('f')                                                         # needs sage.symbolic
        sage: _ = var('x')                                                              # needs sage.symbolic
        sage: nest(f, 0, x)                                                             # needs sage.symbolic
        x
    """

class BackslashOperator:
    '''
    Implement Matlab-style backslash operator for solving systems::

        A \\ b

    The preparser converts this to multiplications using
    ``BackslashOperator()``.

    EXAMPLES::

        sage: preparse("A \\\\ matrix(QQ,2,1,[1/3,\'2/3\'])")
        "A  * BackslashOperator() * matrix(QQ,Integer(2),Integer(1),[Integer(1)/Integer(3),\'2/3\'])"
        sage: preparse("A \\\\ matrix(QQ,2,1,[1/3,2*3])")
        \'A  * BackslashOperator() * matrix(QQ,Integer(2),Integer(1),[Integer(1)/Integer(3),Integer(2)*Integer(3)])\'
        sage: preparse("A \\\\ B + C")
        \'A  * BackslashOperator() * B + C\'
        sage: preparse("A \\\\ eval(\'C+D\')")
        "A  * BackslashOperator() * eval(\'C+D\')"
        sage: preparse("A \\\\ x / 5")
        \'A  * BackslashOperator() * x / Integer(5)\'
        sage: preparse("A^3 \\\\ b")
        \'A**Integer(3)  * BackslashOperator() * b\'
    '''
    left: Incomplete
    def __rmul__(self, left):
        """
        EXAMPLES::

            sage: # needs sage.modules
            sage: A = random_matrix(ZZ, 4)
            sage: while A.rank() != 4:
            ....:     A = random_matrix(ZZ, 4)
            sage: B = random_matrix(ZZ, 4)
            sage: temp = A * BackslashOperator()
            doctest:...:
            DeprecationWarning: the backslash operator has been deprecated
            See https://github.com/sagemath/sage/issues/36394 for details.
            sage: temp.left is A
            True
            sage: X = temp * B
            doctest:...:
            DeprecationWarning: the backslash operator has been deprecated; use A.solve_right(B) instead
            See https://github.com/sagemath/sage/issues/36394 for details.
            sage: A * X == B
            True
        """
    def __mul__(self, right):
        '''
        EXAMPLES::

            sage: # needs scipy sage.modules
            sage: A = matrix(RDF, 5, 5, 2)
            sage: b = vector(RDF, 5, range(5))
            sage: v = A \\ b
            doctest:...:
            DeprecationWarning: the backslash operator has been deprecated; use A.solve_right(B) instead
            See https://github.com/sagemath/sage/issues/36394 for details.
            sage: v.zero_at(1e-19)  # On at least one platform, we get a "negative zero"
            (0.0, 0.5, 1.0, 1.5, 2.0)
            sage: v = A._backslash_(b)
            doctest:...:
            DeprecationWarning: the backslash operator has been deprecated; use A.solve_right(B) instead
            See https://github.com/sagemath/sage/issues/36394 for details.
            sage: v.zero_at(1e-19)
            (0.0, 0.5, 1.0, 1.5, 2.0)
            sage: v = A * BackslashOperator() * b
            doctest:...:
            DeprecationWarning: the backslash operator has been deprecated; use A.solve_right(B) instead
            See https://github.com/sagemath/sage/issues/36394 for details.
            sage: v.zero_at(1e-19)
            (0.0, 0.5, 1.0, 1.5, 2.0)
        '''

def is_iterator(it) -> bool:
    """
    Test if it is an iterator.

    The mantra ``if hasattr(it, 'next')`` was used to tests if ``it`` is an
    iterator. This is not quite correct since ``it`` could have a ``next``
    methods with a different semantic.

    EXAMPLES::

        sage: it = iter([1,2,3])
        sage: is_iterator(it)
        True

        sage: class wrong():
        ....:    def __init__(self): self.n = 5
        ....:    def __next__(self):
        ....:        self.n -= 1
        ....:        if self.n == 0: raise StopIteration
        ....:        return self.n
        sage: x = wrong()
        sage: is_iterator(x)
        False
        sage: list(x)
        Traceback (most recent call last):
        ...
        TypeError: 'wrong' object is not iterable

        sage: class good(wrong):
        ....:    def __iter__(self): return self
        sage: x = good()
        sage: is_iterator(x)
        True
        sage: list(x)
        [4, 3, 2, 1]

        sage: P = Partitions(3)                                                         # needs sage.combinat
        sage: is_iterator(P)                                                            # needs sage.combinat
        False
        sage: is_iterator(iter(P))                                                      # needs sage.combinat
        True
    """
def random_sublist(X, s):
    """
    Return a pseudo-random sublist of the list X where the probability
    of including a particular element is s.

    INPUT:

    - ``X`` -- list

    - ``s`` -- floating point number between 0 and 1

    OUTPUT: list

    EXAMPLES::

        sage: from sage.misc.misc import is_sublist
        sage: S = [1,7,3,4,18]
        sage: sublist = random_sublist(S, 0.5); sublist  # random
        [1, 3, 4]
        sage: is_sublist(sublist, S)
        True
        sage: sublist = random_sublist(S, 0.5); sublist  # random
        [1, 3]
        sage: is_sublist(sublist, S)
        True
    """
def is_sublist(X, Y):
    """
    Test whether ``X`` is a sublist of ``Y``.

    EXAMPLES::

        sage: from sage.misc.misc import is_sublist
        sage: S = [1, 7, 3, 4, 18]
        sage: is_sublist([1, 7], S)
        True
        sage: is_sublist([1, 3, 4], S)
        True
        sage: is_sublist([1, 4, 3], S)
        False
        sage: is_sublist(S, S)
        True
    """
def some_tuples(elements, repeat, bound, max_samples=None):
    """
    Return an iterator over at most ``bound`` number of ``repeat``-tuples of
    ``elements``.

    INPUT:

    - ``elements`` -- an iterable
    - ``repeat`` -- integer (default: ``None``); the length of the tuples to be returned.
      If ``None``, just returns entries from ``elements``.
    - ``bound`` -- the maximum number of tuples returned (ignored if ``max_samples`` given)
    - ``max_samples`` -- nonnegative integer (default: ``None``); if given,
      then a sample of the possible tuples will be returned,
      instead of the first few in the standard order

    OUTPUT:

    If ``max_samples`` is not provided, an iterator over the first
    ``bound`` tuples of length ``repeat``, in the standard nested-for-loop order.

    If ``max_samples`` is provided, a list of at most ``max_samples`` tuples,
    sampled uniformly from the possibilities.  In this case, ``elements``
    must be finite.

    TESTS::

        sage: from sage.misc.misc import some_tuples
        sage: l = some_tuples([0,1,2,3], 2, 3)
        sage: l
        <itertools.islice object at ...>
        sage: len(list(l))
        3

        sage: l = some_tuples(range(50), 3, 10)
        sage: len(list(l))
        10

        sage: l = some_tuples(range(3), 2, None, max_samples=10)
        sage: len(list(l))
        9
    """
def exists(S, P):
    """
    If S contains an element x such that P(x) is ``True``, this function
    returns ``True`` and the element x. Otherwise it returns ``False`` and
    None.

    Note that this function is NOT suitable to be used in an
    if-statement or in any place where a boolean expression is
    expected. For those situations, use the Python built-in

    any(P(x) for x in S)

    INPUT:

    - ``S`` -- object (that supports enumeration)

    - ``P`` -- function that returns ``True`` or ``False``

    OUTPUT:

    - ``bool`` -- whether or not P is ``True`` for some element
      x of S

    - ``object`` -- x

    EXAMPLES: lambda functions are very useful when using the exists
    function::

        sage: exists([1,2,5], lambda x : x > 7)
        (False, None)
        sage: exists([1,2,5], lambda x : x > 3)
        (True, 5)

    The following example is similar to one in the MAGMA handbook. We
    check whether certain integers are a sum of two (small) cubes::

        sage: cubes = [t**3 for t in range(-10,11)]
        sage: exists([(x,y) for x in cubes for y in cubes], lambda v : v[0]+v[1] == 218)
        (True, (-125, 343))
        sage: exists([(x,y) for x in cubes for y in cubes], lambda v : v[0]+v[1] == 219)
        (False, None)
    """
def forall(S, P):
    """
    If `P(x)` is true every x in S, return ``True`` and ``None``. If there is
    some element x in S such that P is not ``True``, return ``False`` and `x`.

    Note that this function is NOT suitable to be used in an
    if-statement or in any place where a boolean expression is
    expected. For those situations, use the Python built-in

    all(P(x) for x in S)

    INPUT:

    - ``S`` -- object (that supports enumeration)

    - ``P`` -- function that returns ``True`` or ``False``

    OUTPUT:

    - ``bool`` -- whether or not P is ``True`` for all elements
      of S

    - ``object`` -- x

    EXAMPLES: lambda functions are very useful when using the forall
    function. As a toy example we test whether certain integers are
    greater than 3.

    ::

        sage: forall([1,2,5], lambda x : x > 3)
        (False, 1)
        sage: forall([1,2,5], lambda x : x > 0)
        (True, None)

    Next we ask whether every positive integer less than 100 is a
    product of at most 2 prime factors::

        sage: forall(range(1,100),  lambda n : len(factor(n)) <= 2)
        (False, 30)

    The answer is no, and 30 is a counterexample. However, every
    positive integer 100 is a product of at most 3 primes.

    ::

        sage: forall(range(1,100),  lambda n : len(factor(n)) <= 3)
        (True, None)
    """
set_trace = pdb.set_trace

def word_wrap(s, ncols: int = 85): ...
def pad_zeros(s, size: int = 3):
    """
    EXAMPLES::

        sage: pad_zeros(100)
        '100'
        sage: pad_zeros(10)
        '010'
        sage: pad_zeros(10, 5)
        '00010'
        sage: pad_zeros(389, 5)
        '00389'
        sage: pad_zeros(389, 10)
        '0000000389'
    """
def is_in_string(line, pos):
    """
    Return ``True`` if the character at position ``pos`` in ``line`` occurs
    within a string.

    EXAMPLES::

        sage: from sage.misc.misc import is_in_string
        sage: line = 'test(\\'#\\')'
        sage: is_in_string(line, line.rfind('#'))
        True
        sage: is_in_string(line, line.rfind(')'))
        False
    """
def get_main_globals():
    '''
    Return the main global namespace.

    EXAMPLES::

        sage: from sage.misc.misc import get_main_globals
        sage: G = get_main_globals()
        sage: bla = 1
        sage: G[\'bla\']
        1
        sage: bla = 2
        sage: G[\'bla\']
        2
        sage: G[\'ble\'] = 5
        sage: ble
        5

    This is analogous to :func:`globals`, except that it can be called
    from any function, even if it is in a Python module::

        sage: def f():
        ....:     G = get_main_globals()
        ....:     assert G[\'bli\'] == 14
        ....:     G[\'blo\'] = 42
        sage: bli = 14
        sage: f()
        sage: blo
        42

    ALGORITHM:

    The main global namespace is discovered by going up the frame
    stack until the frame for the :mod:`__main__` module is found.
    Should this frame not be found (this should not occur in normal
    operation), an exception "ValueError: call stack is not deep
    enough" will be raised by ``_getframe``.

    See :meth:`inject_variable_test` for a real test that this works
    within deeply nested calls in a function defined in a Python
    module.
    '''
def inject_variable(name, value, warn: bool = True) -> None:
    '''
    Inject a variable into the main global namespace.

    INPUT:

    - ``name`` -- string
    - ``value`` -- anything
    - ``warn`` -- boolean (default: ``False``)

    EXAMPLES::

        sage: from sage.misc.misc import inject_variable
        sage: inject_variable("a", 314)
        sage: a
        314

    A warning is issued the first time an existing value is overwritten::

        sage: inject_variable("a", 271)
        doctest:...: RuntimeWarning: redefining global value `a`
        sage: a
        271
        sage: inject_variable("a", 272)
        sage: a
        272

    That\'s because warn seem to not reissue twice the same warning::

        sage: from warnings import warn
        sage: warn("blah")
        doctest:...: UserWarning: blah
        sage: warn("blah")

    Warnings can be disabled::

        sage: b = 3
        sage: inject_variable("b", 42, warn=False)
        sage: b
        42

    Use with care!
    '''
def inject_variable_test(name, value, depth) -> None:
    '''
    A function for testing deep calls to ``inject_variable``.

    EXAMPLES::

        sage: from sage.misc.misc import inject_variable_test
        sage: inject_variable_test("a0", 314, 0)
        sage: a0
        314
        sage: inject_variable_test("a1", 314, 1)
        sage: a1
        314
        sage: inject_variable_test("a2", 314, 2)
        sage: a2
        314
        sage: inject_variable_test("a2", 271, 2)
        doctest:...: RuntimeWarning: redefining global value `a2`
        sage: a2
        271
    '''
def run_once(func):
    '''
    Run a function (successfully) only once.

    The running can be reset by setting the ``has_run`` attribute to False

    TESTS::

        sage: from sage.repl.ipython_extension import run_once
        sage: @run_once
        ....: def foo(work):
        ....:     if work:
        ....:         return \'foo worked\'
        ....:     raise RuntimeError("foo didn\'t work")
        sage: foo(False)
        Traceback (most recent call last):
        ...
        RuntimeError: foo didn\'t work
        sage: foo(True)
        \'foo worked\'
        sage: foo(False)
        sage: foo(True)
    '''
@contextlib.contextmanager
def increase_recursion_limit(increment) -> Generator[None]:
    """
    Context manager to temporarily change the Python maximum recursion depth.

    INPUT:

    - ``increment`` -- increment to add to the current limit

    EXAMPLES::

        sage: from sage.misc.misc import increase_recursion_limit
        sage: def rec(n): None if n == 0 else rec(n-1)
        sage: rec(10000)
        Traceback (most recent call last):
        ...
        RecursionError: maximum recursion depth exceeded...
        sage: with increase_recursion_limit(10000): rec(10000)
        sage: rec(10000)
        Traceback (most recent call last):
        ...
        RecursionError: maximum recursion depth exceeded...
    """
