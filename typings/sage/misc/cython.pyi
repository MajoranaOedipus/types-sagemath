from _typeshed import Incomplete
from sage.env import SAGE_LOCAL as SAGE_LOCAL, cython_aliases as cython_aliases, sage_include_directories as sage_include_directories
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.sage_ostools import redirection as redirection, restore_cwd as restore_cwd
from sage.misc.temporary_file import spyx_tmp as spyx_tmp, tmp_filename as tmp_filename
from sage.repl.user_globals import get_globals as get_globals

sequence_number: Incomplete

def cython(filename, verbose: int = 0, compile_message: bool = False, use_cache: bool = False, create_local_c_file: bool = False, annotate: bool = True, view_annotate: bool = False, view_annotate_callback=None, sage_namespace: bool = True, create_local_so_file: bool = False):
    '''
    Compile a Cython file. This converts a Cython file to a C (or C++ file),
    and then compiles that. The .c file and the .so file are
    created in a temporary directory.

    INPUT:

    - ``filename`` -- the name of the file to be compiled; should end with
      \'pyx\'

    - ``verbose`` -- integer (default: 0); level of verbosity. A negative
      value ensures complete silence.

    - ``compile_message`` -- boolean (default: ``False``); if ``True``, print
      ``\'Compiling <filename>...\'`` to the standard error

    - ``use_cache`` -- boolean (default: ``False``); if ``True``, check the
      temporary build directory to see if there is already a
      corresponding .so file. If so, and if the .so file is newer than the
      Cython file, don\'t recompile, just reuse the .so file.

    - ``create_local_c_file`` -- boolean (default: ``False``); if ``True``, save a
      copy of the ``.c`` or ``.cpp`` file in the current directory

    - ``annotate`` -- boolean (default: ``True``); if ``True``, create an html file which
      annotates the conversion from .pyx to .c. By default this is only created
      in the temporary directory, but if ``create_local_c_file`` is also True,
      then save a copy of the .html file in the current directory.

    - ``view_annotate`` -- boolean (default: ``False``); if ``True``, open the
      annotated html file in a web browser

    - ``view_annotate_callback`` -- function; a function that takes a string
      being the path to the html file. This can be overridden to change
      what to do with the annotated html file. Have no effect unless
      ``view_annotate`` is ``True``. By default, the html file is opened in a
      web browser.

    - ``sage_namespace`` -- boolean (default: ``True``); if ``True``, import
      ``sage.all``

    - ``create_local_so_file`` -- boolean (default: ``False``); if ``True``, save a
      copy of the compiled .so file in the current directory

    OUTPUT: a tuple ``(name, dir)`` where ``name`` is the name
    of the compiled module and ``dir`` is the directory containing
    the generated files.

    TESTS:

    Before :issue:`12975`, it would have been needed to write ``#clang c++``,
    but upper case ``C++`` has resulted in an error.
    Using pkgconfig to find the libraries, headers and macros. This is a
    work around while waiting for :issue:`22461` which will offer a better
    solution::

        sage: code = [
        ....: "#clang C++",
        ....: "from sage.rings.polynomial.multi_polynomial_libsingular cimport MPolynomial_libsingular",
        ....: "from sage.libs.singular.polynomial cimport singular_polynomial_pow",
        ....: "def test(MPolynomial_libsingular p):",
        ....: "    singular_polynomial_pow(&p._poly, p._poly, 2, p._parent_ring)"]
        sage: cython(os.linesep.join(code))

    The function ``test`` now manipulates internal C data of polynomials,
    squaring them::

        sage: P.<x,y>=QQ[]
        sage: test(x)
        sage: x
        x^2

    Check that compiling C++ code works::

        sage: cython("# distutils: language = c++\\n"+
        ....:        "from libcpp.vector cimport vector\\n"
        ....:        "cdef vector[int] * v = new vector[int](4)\\n")

    Check that compiling C++ code works when creating a local C file,
    first moving to a tempdir to avoid clutter.  Before :issue:`22113`,
    the create_local_c_file argument was not tested for C++ code::

        sage: orig_cwd = os.getcwd()
        sage: import tempfile
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     os.chdir(d)
        ....:     with open("test.pyx", \'w\') as f:
        ....:         _ = f.write("# distutils: language = c++\\n"
        ....:           "from libcpp.vector cimport vector\\n"
        ....:           "cdef vector[int] * v = new vector[int](4)\\n")
        ....:     output = sage.misc.cython.cython("test.pyx",
        ....:                                      create_local_c_file=True)
        ....:     os.chdir(orig_cwd)

    Accessing a ``.pxd`` file from the current directory works::

        sage: orig_cwd = os.getcwd()
        sage: import tempfile
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     os.chdir(d)
        ....:     with open("helper.pxd", \'w\') as f:
        ....:         _ = f.write("cdef inline int the_answer(): return 42")
        ....:     cython(
        ....:           "from helper cimport the_answer\\n"
        ....:           "print(the_answer())"
        ....:     )
        ....:     os.chdir(orig_cwd)
        42

    Warning and error messages generated by Cython are properly
    handled. Warnings are only shown if verbose >= 0::

        sage: code = \'\'\'
        ....: def test_unreachable():
        ....:     raise Exception
        ....:     return 42
        ....: \'\'\'
        sage: cython(code, verbose=-1)
        sage: cython(code, verbose=0)
        warning: ...:4:4: Unreachable code...

        sage: cython("foo = bar\\n")
        Traceback (most recent call last):
        ...
        RuntimeError: Error compiling Cython file:
        ------------------------------------------------------------
        ...
        foo = bar
             ^
        ------------------------------------------------------------
        <BLANKLINE>
        ...:1:6: undeclared name not builtin: bar

        sage: cython("cdef extern from \'no_such_header_file\': pass")
        Traceback (most recent call last):
        ...
        RuntimeError: ...

    As of :issue:`29139` the default is ``cdivision=True``::

        sage: cython(\'\'\'
        ....: cdef size_t foo = 3/2
        ....: \'\'\')

    Check that Cython supports PEP 420 packages::

        sage: cython(\'\'\'
        ....: cimport sage.misc.cachefunc
        ....: \'\'\')

        sage: cython(\'\'\'
        ....: from sage.misc.cachefunc cimport cache_key
        ....: \'\'\')

    Test ``view_annotate``::

        sage: cython(\'\'\'
        ....: def f(int n):
        ....:     return n*n
        ....: \'\'\', view_annotate=True)  # optional -- webbrowser

    ::

        sage: cython(\'\'\'
        ....: def f(int n):
        ....:     return n*n
        ....: \'\'\', view_annotate=True, annotate=False)
        Traceback (most recent call last):
        ...
        ValueError: cannot view annotated file without creating it

    ::

        sage: collected_paths = []
        sage: cython(\'\'\'
        ....: def f(int n):
        ....:     return n*n
        ....: \'\'\', view_annotate=True, view_annotate_callback=collected_paths.append)
        sage: collected_paths
        [\'...\']
        sage: len(collected_paths)
        1
    '''
def cython_lambda(vars, expr, verbose: int = 0, **kwds):
    """
    Create a compiled function which evaluates ``expr`` assuming machine values
    for ``vars``.

    INPUT:

    - ``vars`` -- list of pairs (variable name, c-data type), where the variable
      names and data types are strings, OR a string such as ``'double x, int y,
      int z'``

    - ``expr`` -- an expression involving the vars and constants; you can access
      objects defined in the current module scope ``globals()`` using
      ``sage.object_name``.

    .. warning::

        Accessing ``globals()`` doesn't actually work, see :issue:`12446`.

    EXAMPLES:

    We create a Lambda function in pure Python (using the r to make sure the 3.2
    is viewed as a Python float)::

        sage: f = lambda x,y: x*x + y*y + x + y + 17r*x + 3.2r

    We make the same Lambda function, but in a compiled form. ::

        sage: g = cython_lambda('double x, double y', 'x*x + y*y + x + y + 17*x + 3.2')
        sage: g(2,3)
        55.2
        sage: g(0,0)
        3.2

    In order to access Sage globals, prefix them with ``sage.``::

        sage: f = cython_lambda('double x', 'sage.sin(x) + sage.a')
        sage: f(0)
        Traceback (most recent call last):
        ...
        NameError: global 'a' is not defined
        sage: a = 25
        sage: f(10)
        24.45597888911063
        sage: a = 50
        sage: f(10)
        49.45597888911063
    """
def cython_import(filename, **kwds):
    """
    Compile a file containing Cython code, then import and return the
    module.  Raises an :exc:`ImportError` if anything goes wrong.

    INPUT:

    - ``filename`` -- string; name of a file that contains Cython
      code

    See the function :func:`sage.misc.cython.cython` for documentation
    for the other inputs.

    OUTPUT: the module that contains the compiled Cython code
    """
def cython_import_all(filename, globals, **kwds) -> None:
    """
    Imports all non-private (i.e., not beginning with an underscore)
    attributes of the specified Cython module into the given context.
    This is similar to::

        from module import *

    Raises an :exc:`ImportError` exception if anything goes wrong.

    INPUT:

    - ``filename`` -- string; name of a file that contains Cython
      code

    See the function :func:`sage.misc.cython.cython` for documentation
    for the other inputs.
    """
def sanitize(f):
    """
    Given a filename ``f``, replace it by a filename that is a valid Python
    module name.

    This means that the characters are all alphanumeric or ``_``'s and doesn't
    begin with a numeral.

    EXAMPLES::

        sage: from sage.misc.cython import sanitize
        sage: sanitize('abc')
        'abc'
        sage: sanitize('abc/def')
        'abc_def'
        sage: sanitize('123/def-hij/file.py')
        '_123_def_hij_file_py'
    """
def compile_and_load(code, **kwds):
    '''
    INPUT:

    - ``code`` -- string containing code that could be in a .pyx file
      that is attached or put in a %cython block in the notebook

    See the function :func:`sage.misc.cython.cython` for documentation
    for the other inputs.

    OUTPUT: a module, which results from compiling the given code and
    importing it

    EXAMPLES::

        sage: from sage.misc.cython import compile_and_load
        sage: module = compile_and_load("def f(int n):\\n    return n*n")
        sage: module.f(10)
        100

    TESTS::

        sage: code = \'\'\'
        ....: from sage.rings.rational cimport Rational
        ....: from sage.rings.polynomial.polynomial_rational_flint cimport Polynomial_rational_flint
        ....: from sage.libs.flint.fmpq_poly cimport fmpq_poly_length
        ....: from sage.libs.flint.fmpq_poly_sage cimport fmpq_poly_get_coeff_mpq, fmpq_poly_set_coeff_mpq
        ....:
        ....: def evaluate_at_power_of_gen(Polynomial_rational_flint f, unsigned long n):
        ....:     assert n >= 1
        ....:     cdef Polynomial_rational_flint res = f._new()
        ....:     cdef unsigned long k
        ....:     cdef Rational z = Rational(0)
        ....:     for k in range(fmpq_poly_length(f._poly)):
        ....:         fmpq_poly_get_coeff_mpq(z.value, f._poly, k)
        ....:         fmpq_poly_set_coeff_mpq(res._poly, n*k, z.value)
        ....:     return res
        ....: \'\'\'
        sage: module = compile_and_load(code)  # long time
        sage: R.<x> = QQ[]
        sage: module.evaluate_at_power_of_gen(x^3 + x - 7, 5)  # long time
        x^15 + x^5 - 7
    '''
def cython_compile(code, **kwds):
    """
    Given a block of Cython code (as a text string), this function
    compiles it using a C compiler, and includes it into the global
    namespace.

    AUTHOR: William Stein, 2006-10-31

    .. WARNING::

        Only use this from Python code, not from extension code, since
        from extension code you would change the global scope (i.e.,
        of the Sage interpreter). And it would be stupid, since you're
        already writing Cython!

        Also, never use this in the standard Sage library.  Any code
        that uses this can only run on a system that has a C compiler
        installed, and we want to avoid making that assumption for
        casual Sage usage.  Also, any code that uses this in the
        library would greatly slow down startup time, since currently
        there is no caching.

    .. TODO::

        Need to create a clever caching system so code only gets
        compiled once.
    """
