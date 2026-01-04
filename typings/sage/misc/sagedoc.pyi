r"""
Format Sage documentation for viewing with IPython and the notebook

AUTHORS:

- William Stein (2005): initial version.
- Nick Alexander (2007): nodetex functions
- Nick Alexander (2008): search_src, search_def improvements
- Martin Albrecht (2008-03-21): parse LaTeX description environments in sagedoc
- John Palmieri (2009-04-11): fix for #5754 plus doctests
- Dan Drake (2009-05-21): refactor search_* functions, use system 'find' instead of sage -grep
- John Palmieri (2009-06-28): don't use 'find' -- use Python (os.walk, re.search) instead.
- Simon King (2011-09): Use os.linesep, avoid destruction of embedding information,
  enable nodetex in a docstring. Consequently use sage_getdoc.

TESTS:

Check that argspecs of extension function/methods appear correctly,
see :issue:`12849`::

    sage: from sage.env import SAGE_DOC
    sage: docfilename = os.path.join(SAGE_DOC, 'html', 'en', 'reference', 'calculus', 'sage', 'symbolic', 'expression.html')
    sage: with open(docfilename) as fobj:                                               # needs sagemath_doc_html
    ....:     for line in fobj:
    ....:         if "#sage.symbolic.expression.Expression.numerical_approx" in line:
    ....:             print(line)
    <span class="sig-name descname"><span class="pre">numerical_approx</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">prec</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">digits</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">algorithm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span>...

Check that sphinx is not imported at Sage start-up::

    sage: os.system("sage -c \"if 'sphinx' in sys.modules: sys.exit(1)\"")
    0
"""

import re
import pydoc
from sage.env import SAGE_DOC as SAGE_DOC, SAGE_SRC as SAGE_SRC
from sage.misc import sageinspect as sageinspect
from sage.misc.temporary_file import tmp_dir as tmp_dir
from sage.misc.viewer import browser as browser

math_substitutes: list[tuple[str, str]]
nonmath_substitutes: list[tuple[str, str]]
itempattern: re.Pattern
itemreplace: str

def detex(s: str, embedded: bool = False) -> str:
    """nodetex
    This strips LaTeX commands from a string; it is used by the
    ``format`` function to process docstrings for display from the
    command line interface.

    INPUT:

    - ``s`` -- string
    - ``embedded`` -- boolean (default: ``False``)

    If ``embedded`` is ``False``, then do the replacements in both
    ``math_substitutes`` and ``nonmath_substitutes``.  If ``True``, then
    only do ``nonmath_substitutes``.

    OUTPUT: string

    EXAMPLES::

        sage: from sage.misc.sagedoc import detex
        sage: detex(r'Some math: `n \\geq k`.  A website: \\url{sagemath.org}.')
        'Some math: n >= k.  A website: sagemath.org.\\n'
        sage: detex(r'More math: `x \\mapsto y`.  {\\bf Bold face}.')
        'More math: x  |-->  y.  { Bold face}.\\n'
        sage: detex(r'`a, b, c, \\ldots, z`')
        'a, b, c, ..., z\\n'
        sage: detex(r'`a, b, c, \\ldots, z`', embedded=True)
        '`a, b, c, \\\\ldots, z`'
        sage: detex(r'`\\left(\\lvert x\\ast y \\rvert\\right]`')
        '(| x * y |]\\n'
        sage: detex(r'`\\left(\\leq\\le\\leftarrow \\rightarrow\\unknownmacro\\to`')
        '(<=<=<-- -->\\\\unknownmacro-->\\n'
    """
def skip_TESTS_block(docstring: str) -> str:
    '''
    Remove blocks labeled "TESTS:" from ``docstring``.

    INPUT:

    - ``docstring`` -- string

    A "TESTS" block is a block starting "TESTS:" (or
    the same with two colons), on a line on its own, and ending either
    with a line indented less than "TESTS", or with a line with the
    same level of indentation -- not more -- matching one of the
    following:

    - a Sphinx directive of the form ".. foo:", optionally followed by
      other text.

    - text of the form "UPPERCASE:", optionally followed by other
      text.

    - lines which look like a reST header: one line containing
      anything, followed by a line consisting only of a string of
      hyphens, equal signs, or other characters which are valid
      markers for reST headers: ``- = ` : \' " ~ _ ^ * + # < >``.
      However, lines only containing double colons `::` do not
      end "TESTS" blocks.

    Return the string obtained from ``docstring`` by removing these
    blocks.

    EXAMPLES::

        sage: from sage.misc.sagedoc import skip_TESTS_block
        sage: start = \' Docstring\\n\\n\'
        sage: test = \' TESTS: \\n\\n Here is a test::\\n     sage: 2+2 \\n     5 \\n\\n\'
        sage: test2 = \' TESTS:: \\n\\n     sage: 2+2 \\n     6 \\n\\n\'

    Test lines starting with "REFERENCES:"::

        sage: refs = \' REFERENCES: \\n text text \\n\'
        sage: skip_TESTS_block(start + test + refs).rstrip() == (start + refs).rstrip()
        True
        sage: skip_TESTS_block(start + test + test2 + refs).rstrip() == (start + refs).rstrip()
        True
        sage: skip_TESTS_block(start + test + refs + test2).rstrip() == (start + refs).rstrip()
        True

    Test Sphinx directives::

        sage: directive = \' .. todo:: \\n     do some stuff \\n\'
        sage: skip_TESTS_block(start + test + refs + test2 + directive).rstrip() == (start + refs + directive).rstrip()
        True

    Test unindented lines::

        sage: unindented = \'NOT INDENTED\\n\'
        sage: skip_TESTS_block(start + test + unindented).rstrip() == (start + unindented).rstrip()
        True
        sage: skip_TESTS_block(start + test + unindented + test2 + unindented).rstrip() == (start + unindented + unindented).rstrip()
        True

    Test headers::

        sage: header = \' Header:\\n ~~~~~~~~\'
        sage: skip_TESTS_block(start + test + header) == start + header
        True

    Not a header because the characters on the second line must all be
    the same::

        sage: fake_header = \' Header:\\n -=-=-=-=-=\'
        sage: skip_TESTS_block(start + test + fake_header).rstrip() == start.rstrip()
        True

    Not a header because it\'s indented compared to \'TEST\' in the
    string ``test``::

        sage: another_fake = \'\\n    blah\\n    ----\'
        sage: skip_TESTS_block(start + test + another_fake).rstrip() == start.rstrip()
        True

    Double colons ``::`` are also not considered as headers (:issue:`27896`)::

        sage: colons = \' ::\\n\\n     sage: 2+2\\n     4\\n\\n\'
        sage: skip_TESTS_block(start + test2 + colons).rstrip() == start.rstrip()
        True
    '''
def process_dollars(s: str) -> str:
    '''nodetex
    Replace dollar signs with backticks.

    More precisely, do a regular expression search.  Replace a plain
    dollar sign ($) by a backtick (`).  Replace an escaped dollar sign
    (\\\\$) by a dollar sign ($).  Don\'t change a dollar sign preceded or
    followed by a backtick (\\`$ or \\$`), because of strings like
    "``$HOME``".  Don\'t make any changes on lines starting with more
    spaces than the first nonempty line in ``s``, because those are
    indented and hence part of a block of code or examples.

    This also doesn\'t replaces dollar signs enclosed in curly braces,
    to avoid nested math environments.

    EXAMPLES::

        sage: from sage.misc.sagedoc import process_dollars
        sage: process_dollars(\'hello\')
        \'hello\'
        sage: process_dollars(\'some math: $x=y$\')
        doctest:warning...
        DeprecationWarning: using dollar signs to mark up math in Sage docstrings
        is deprecated; use backticks instead
        See https://github.com/sagemath/sage/issues/33973 for details.
        \'some math: `x=y`\'

    Replace \\\\$ with $, and don\'t do anything when backticks are involved::

        sage: process_dollars(r\'a ``$REAL`` dollar sign: \\$\')
        \'a ``$REAL`` dollar sign: $\'

    Don\'t make any changes on lines indented more than the first
    nonempty line::

        sage: s = \'\\n first line\\n     indented $x=y$\'
        sage: s == process_dollars(s)
        True

    Don\'t replace dollar signs enclosed in curly braces::

        sage: process_dollars(r\'f(n) = 0 \\text{ if $n$ is prime}\')
        \'f(n) = 0 \\\\text{ if $n$ is prime}\'

    This is not perfect::

        sage: process_dollars(r\'$f(n) = 0 \\text{ if $n$ is prime}$\')
        \'`f(n) = 0 \\\\text{ if $n$ is prime}$\'

    The regular expression search doesn\'t find the last $.
    Fortunately, there don\'t seem to be any instances of this kind of
    expression in the Sage library, as of this writing.
    '''

pythonversion: str
extlinks: dict[str, tuple[str, str|None]]

def process_extlinks(s: str, embedded: bool = False) -> str:
    """nodetex

    In docstrings at the command line, process markup related to the
    Sphinx extlinks extension. For example, replace ``:issue:`NUM```
    with ``https://github.com/sagemath/sage/issues/NUM``, and similarly with
    ``:python:TEXT`` and ``:wikipedia:TEXT``, looking up the url from
    the dictionary ``extlinks`` in ``sage_docbuild.conf``.
    If ``TEXT`` is of the form ``blah <LINK>``, then it uses ``LINK``
    rather than ``TEXT`` to construct the url.

    In the notebook, don't do anything: let sphinxify take care of it.

    INPUT:

    - ``s`` -- string, in practice a docstring
    - ``embedded`` -- boolean (default: ``False``)

    This function is called by :func:`format`, and if in the notebook,
    it sets ``embedded`` to be ``True``, otherwise ``False``.

    EXAMPLES::

        sage: from sage.misc.sagedoc import process_extlinks
        sage: process_extlinks('See :issue:`1234`, :wikipedia:`Wikipedia <Sage_(mathematics_software)>`, and :issue:`4321` ...')
        'See https://github.com/sagemath/sage/issues/1234, https://en.wikipedia.org/wiki/Sage_(mathematics_software), and https://github.com/sagemath/sage/issues/4321 ...'
        sage: process_extlinks('See :issue:`1234` for more information.', embedded=True)
        'See :issue:`1234` for more information.'
        sage: process_extlinks('see :python:`Implementing Descriptors <reference/datamodel.html#implementing-descriptors>` ...')
        'see https://docs.python.org/release/.../reference/datamodel.html#implementing-descriptors ...'
    """
def process_mathtt(s: str) -> str:
    """nodetex
    Replace \\\\mathtt{BLAH} with BLAH in the command line.

    INPUT:

    - ``s`` -- string, in practice a docstring

    This function is called by :func:`format`.

    EXAMPLES::

        sage: from sage.misc.sagedoc import process_mathtt
        sage: process_mathtt(r'e^\\mathtt{self}')
        'e^self'
    """
def process_optional_doctest_tags(s: str) -> str:
    '''
    Remove ``# optional/needs`` doctest tags for present features from docstring ``s``.

    EXAMPLES:

        sage: from sage.misc.sagedoc import process_optional_doctest_tags
        sage: process_optional_doctest_tags("sage: # needs sage.rings.finite_rings\\nsage: K.<x> = FunctionField(GF(5^2,\'a\')); K\\nRational function field in x over Finite Field in a of size 5^2")  # needs sage.rings.finite_rings
        "sage: K.<x> = FunctionField(GF(5^2,\'a\')); K\\nRational function field in x over Finite Field in a of size 5^2"
    '''
def format(s: str, embedded: bool = False) -> str:
    '''noreplace
    Format Sage documentation ``s`` for viewing with IPython.

    This calls :func:`detex` on ``s`` to convert LaTeX commands to plain
    text, unless the directive ``nodetex`` is given in the first line
    of the string.

    Also, if ``s`` contains a string of the form ``<<<obj>>>``, then
    it replaces it with the docstring for ``obj``, unless the
    directive ``noreplace`` is given in the first line. If an error
    occurs under the attempt to find the docstring for ``obj``, then
    the substring ``<<<obj>>>`` is preserved.

    Directives must be separated by a comma.

    INPUT:

    - ``s`` -- string
    - ``embedded`` -- boolean (default: ``False``)

    OUTPUT: string

    Set ``embedded`` equal to ``True`` if formatting for use in the
    notebook; this just gets passed as an argument to :func:`detex`.

    .. SEEALSO::

        :func:`sage.misc.sageinspect.sage_getdoc` to get the formatted
        documentation of a given object.

    EXAMPLES::

        sage: from sage.misc.sagedoc import format
        sage: format(\'Let `A` be an `m` by `n` (0,1)-matrix. We identify `A` with a chessboard\')
        \'Let A be an m by n (0,1)-matrix. We identify A with a chessboard\\n\'

    If the first line of the string is \'nodetex\', remove \'nodetex\' but
    don\'t modify any TeX commands::

        sage: format("nodetex\\n`x \\\\geq y`")
        \'`x \\\\geq y`\'

    Testing a string enclosed in triple angle brackets::

        sage: format(\'<<<identity_matrix\')
        \'<<<identity_matrix\\n\'
        sage: format(\'identity_matrix>>>\')
        \'identity_matrix>>>\\n\'
        sage: format(\'<<<identity_matrix>>>\')                                           # needs sage.modules
        \'...Definition: identity_matrix(...\'
        sage: format(\'<<<identity_matrix>>>\')[:28]                                      # needs sphinx
        \'Definition: identity_matrix(\'

    TESTS:

    We check that the todo Sphinx extension is correctly activated::

        sage: sage.misc.sagedoc.format(sage.combinat.ranker.on_fly.__doc__)             # needs sphinx
        "...Return ...Todo: add tests as in combinat::rankers\\n"

    In the following use case, the ``nodetex`` directive would have been ignored prior
    to :issue:`11815`::

        sage: cython_code = ["def testfunc(x):",
        ....: "    \'\'\'",
        ....: "    nodetex",
        ....: "    This is a doc string with raw latex",
        ....: "",
        ....: "    `x \\\\geq y`",
        ....: "    \'\'\'",
        ....: "    return -x"]
        sage: cython(\'\\n\'.join(cython_code))                                            # needs sage.misc.cython
        sage: from sage.misc.sageinspect import sage_getdoc
        sage: print(sage_getdoc(testfunc))                                              # needs sage.misc.cython
        <BLANKLINE>
            This is a doc string with raw latex
        <BLANKLINE>
            `x \\geq y`
        <BLANKLINE>

    We check that the ``noreplace`` directive works, even combined with
    ``nodetex`` (see :issue:`11817`)::

        sage: print(format(\'\'\'nodetex, noreplace\\n<<<identity_matrix>>>`\\\\not= 0`\'\'\'))
        <<<identity_matrix>>>`\\not= 0`

    If replacement is impossible, then no error is raised::

        sage: print(format(\'<<<bla\\n<<<bla>>>\\n<<<identity_matrix>>>\'))
        <<<bla <<<bla>>>
        <BLANKLINE>
        Definition: identity_matrix(ring, n=0, sparse=False)
        <BLANKLINE>
        This function is available as identity_matrix(...) and
        matrix.identity(...).
        <BLANKLINE>
           Return the n x n identity matrix over the given ring.
        ...

    Check that backslashes are preserved in code blocks (:issue:`29140`)::

        sage: format(\'::\\n\'                                                             # needs sphinx
        ....:        \'\\n\'
        ....:        r\'    sage: print(r"\\\\\\\\.")\' \'\\n\'
        ....:        r\'    \\\\\\\\.\')
        \'   sage: print(r"\\\\\\\\\\\\\\\\.")\\n   \\\\\\\\\\\\\\\\.\\n\'
        sage: format(r\'inline code ``\\\\\\\\.``\')
        \'inline code "\\\\\\\\\\\\\\\\."\\n\'
    '''
def format_src(s: str) -> str:
    '''
    Format Sage source code ``s`` for viewing with IPython.

    If ``s`` contains a string of the form "<<<obj>>>", then it
    replaces it with the source code for "obj".

    INPUT:

    - ``s`` -- string

    OUTPUT: string

    EXAMPLES::

        sage: from sage.misc.sagedoc import format_src
        sage: format_src(\'unladen swallow\')
        \'unladen swallow\'
        sage: format_src(\'<<<Sq>>>\')[5:15]                                              # needs sage.combinat sage.modules
        \'Sq(*nums):\'
    '''
def search_src(string: str, extra1: str = '', extra2: str = '', extra3: str = '', extra4: str = '', extra5: str = '', **kwds) -> str | None:
    '''
    Search Sage library source code for lines containing ``string``.
    The search is case-insensitive by default.

    INPUT:

    - ``string`` -- string to find in the Sage source code

    - ``extra1``, ..., ``extra5`` -- additional strings to require when
      searching.  Lines must match all of these, as well as ``string``

    - ``whole_word`` -- (default: ``False``) if ``True``, search for
      ``string`` and ``extra1`` (etc.) as whole words only.  This
      assumes that each of these arguments is a single word, not a
      regular expression, and it might have unexpected results if used
      with regular expressions.

    - ``ignore_case`` -- boolean (default: ``True``); if ``False``, perform a
      case-sensitive search

    - ``multiline`` -- (default: ``False``) if ``True``, search more
      than one line at a time.  In this case, print any matching file
      names, but don\'t print line numbers.

    - ``interact`` -- boolean (default: ``True``); if ``False``, return
      a string with all the matches. Otherwise, this function returns
      ``None``, and the results are displayed appropriately, according
      to whether you are using the notebook or the command-line
      interface. You should not ordinarily need to use this.

    - ``path_re`` -- (default: ``\'\'``) regular expression which
      the filename (including the path) must match

    - ``module`` -- (default: ``\'sage\'``) the module in which to
      search.  The default is \'sage\', the entire Sage library.  If
      ``module`` doesn\'t start with "sage", then the links in the
      notebook output may not function.

    OUTPUT:

    If ``interact`` is ``False``, then return a string with all of
    the matches, separated by newlines.  On the other hand, if
    ``interact`` is ``True`` (the default), there is no output.  Instead:
    at the command line, the search results are printed on the screen
    in the form ``filename:line_number:line of text``, showing the
    filename in which each match occurs, the line number where it
    occurs, and the actual matching line.  (If ``multiline`` is ``True``,
    then only the filename is printed for each match.)  The file paths
    in the output are relative to ``$SAGE_SRC``.  In the
    notebook, each match produces a link to the actual file in which
    it occurs.

    The ``string`` and ``extraN`` arguments are treated as regular
    expressions, as is ``path_re``, and errors will be raised if they
    are invalid. The matches will be case-insensitive unless
    ``ignore_case`` is ``False``.

    .. NOTE::

        The ``extraN`` parameters are present only because
        ``search_src(string, *extras, interact=False)``
        is not parsed correctly by Python 2.6; see http://bugs.python.org/issue1909.

    EXAMPLES:

    First note that without using ``interact=False``, this function
    produces no output, while with ``interact=False``, the output is a
    string.  These examples almost all use this option, so that they
    have something to which to compare their output.

    You can search for "matrix" by typing ``search_src("matrix")``.
    This particular search will produce many results::

        sage: len(search_src("matrix", interact=False).splitlines())  # random # long time
        9522

    You can restrict to the Sage calculus code with
    ``search_src("matrix", module="sage.calculus")``, and this
    produces many fewer results::

        sage: len(search_src("matrix", module="sage.calculus", interact=False).splitlines())  # random
        26

    Note that you can do tab completion on the ``module`` string.
    Another way to accomplish a similar search::

        sage: len(search_src("matrix", path_re="calc",                                  # needs sage.modules
        ....:                interact=False).splitlines()) > 15
        True

    The following produces an error because the string \'fetch(\' is a
    malformed regular expression::

        sage: try:
        ....:     print(search_src(" fetch(", "def", interact=False))
        ....: except Exception as e:
        ....:     print(e)
        missing ), unterminated subpattern at position 6

    To fix this, *escape* the parenthesis with a backslash::

        sage: print(search_src(r" fetch\\(", "def", interact=False))  # random # long time
        matrix/matrix0.pyx:    cdef fetch(self, key):
        matrix/matrix0.pxd:    cdef fetch(self, key)

        sage: print(search_src(r" fetch\\(", "def", "pyx", interact=False))  # random # long time
        matrix/matrix0.pyx:    cdef fetch(self, key):

    As noted above, the search is case-insensitive, but you can make it
    case-sensitive with the \'ignore_case\' key word::

        sage: s = search_src(\'Matrix\', path_re=\'matrix\', interact=False); s.find(\'x\') > 0
        True

        sage: s = search_src(\'MatRiX\', path_re=\'matrix\', interact=False); s.find(\'x\') > 0
        True

        sage: s = search_src(\'MatRiX\', path_re=\'matrix\',
        ....:                interact=False, ignore_case=False); s.find(\'x\') > 0
        False

    Searches are by default restricted to single lines, but this can
    be changed by setting ``multiline`` to be True.  In the following,
    since ``search_src(string, interact=False)`` returns a string with
    one line for each match, counting the length of
    ``search_src(string, interact=False).splitlines()`` gives the
    number of matches. ::

        sage: len(search_src(\'log\', \'derivative\', interact=False).splitlines()) < 40
        True
        sage: len(search_src(\'log\', \'derivative\',
        ....:                interact=False, multiline=True).splitlines()) > 70
        True

    A little recursive narcissism: let\'s do a doctest that searches for
    this function\'s doctests. Note that you can\'t put "sage:" in the
    doctest string because it will get replaced by the Python ">>>"
    prompt.

    ::

        sage: print(search_src(r\'^ *sage[:] .*search_src\\(\', interact=False))  # long time
        misc/sagedoc.py:... len(search_src("matrix", interact=False).splitlines())...
        misc/sagedoc.py:... len(search_src("matrix", module="sage.calculus", interact=False).splitlines())...
        misc/sagedoc.py:... len(search_src("matrix", path_re="calc"...
        misc/sagedoc.py:... print(search_src(r" fetch\\(", "def", interact=False))...
        misc/sagedoc.py:... print(search_src(r" fetch\\(", "def", "pyx", interact=False))...
        misc/sagedoc.py:... s = search_src(\'Matrix\', path_re=\'matrix\', interact=False); s.find(\'x\') > 0...
        misc/sagedoc.py:... s = search_src(\'MatRiX\', path_re=\'matrix\', interact=False); s.find(\'x\') > 0...
        misc/sagedoc.py:... s = search_src(\'MatRiX\', path_re=\'matrix\',...
        misc/sagedoc.py:... len(search_src(\'log\', \'derivative\', interact=False).splitlines()) < 40...
        misc/sagedoc.py:... len(search_src(\'log\', \'derivative\'...
        misc/sagedoc.py:... print(search_src(r\'^ *sage[:] .*search_src\\(\', interact=False))...
        misc/sagedoc.py:... len(search_src("matrix", interact=False).splitlines()) > 9000...
        misc/sagedoc.py:... print(search_src(\'matrix\', \'column\', \'row\', \'sub\',...
        misc/sagedoc.py:... sage: results = search_src(\'format_search_as_html\',...

    TESTS:

    As of this writing, there are about 9500 lines in the Sage library that
    contain "matrix"; it seems safe to assume we will continue to have
    over 9000 such lines::

        sage: len(search_src("matrix", interact=False).splitlines()) > 9000 # long time
        True

    Check that you can pass 5 parameters::

        sage: print(search_src(\'matrix\', \'column\', \'row\', \'sub\', \'start\', \'index\', interact=False)) # random # long time
        matrix/matrix0.pyx:598:        Get The 2 x 2 submatrix of M, starting at row index and column
        matrix/matrix0.pyx:607:        Get the 2 x 3 submatrix of M starting at row index and column index
        matrix/matrix0.pyx:924:        Set the 2 x 2 submatrix of M, starting at row index and column
        matrix/matrix0.pyx:933:        Set the 2 x 3 submatrix of M starting at row index and column
    '''
def search_doc(string: str, extra1: str = '', extra2: str = '', extra3: str = '', extra4: str = '', extra5: str = '', **kwds) -> str | None:
    """
    Search Sage HTML documentation for lines containing ``string``. The
    search is case-insensitive by default.

    The file paths in the output are relative to ``$SAGE_DOC``.

    INPUT: same as for :func:`search_src`.

    OUTPUT: same as for :func:`search_src`

    EXAMPLES:

    See the documentation for :func:`search_src` for more examples. ::

        sage: search_doc('creates a polynomial', path_re='tutorial', interact=False) # random
        html/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)

    If you search the documentation for 'tree', then you will get too
    many results, because many lines in the documentation contain the
    word 'toctree'.  If you use the ``whole_word`` option, though, you
    can search for 'tree' without returning all of the instances of
    'toctree'.  In the following, since ``search_doc('tree',
    interact=False)`` returns a string with one line for each match,
    counting the length of ``search_doc('tree',
    interact=False).splitlines()`` gives the number of matches. ::

        sage: # long time, needs sagemath_doc_html
        sage: N = len(search_doc('tree', interact=False).splitlines())
        sage: L = search_doc('tree', whole_word=True, interact=False).splitlines()
        sage: len(L) < N
        True
        sage: import re
        sage: tree_re = re.compile(r'(^|\\W)tree(\\W|$)', re.I)
        sage: all(tree_re.search(l) for l in L)
        True
    """
def search_def(name: str, extra1: str = '', extra2: str = '', extra3: str = '', extra4: str = '', extra5: str = '', **kwds) -> str | None:
    '''
    Search Sage library source code for function definitions containing
    ``name``. The search is case-insensitive by default.

    INPUT: same as for :func:`search_src`.

    OUTPUT: same as for :func:`search_src`

    .. NOTE::

        The regular expression used by this function only finds function
        definitions that are preceded by spaces, so if you use tabs on a
        "def" line, this function will not find it. As tabs are not
        allowed in Sage library code, this should not be a problem.

    EXAMPLES:

    See the documentation for :func:`search_src` for more examples. ::

        sage: print(search_def("fetch", interact=False))  # random # long time
        matrix/matrix0.pyx:    cdef fetch(self, key):
        matrix/matrix0.pxd:    cdef fetch(self, key)

        sage: print(search_def("fetch", path_re="pyx", interact=False))  # random # long time
        matrix/matrix0.pyx:    cdef fetch(self, key):
    '''
def format_search_as_html(what: str, results: str | list[str], search: str | list[str]):
    '''
    Format the output from ``search_src``, ``search_def``, or
    ``search_doc`` as html, for use in the notebook.

    INPUT:

    - ``what`` -- string; what was searched (source code or
      documentation)
    - ``results`` -- string or list; the results of the search as a string or list of
      search results
    - ``search`` -- string or list; what was being searched for, either as a
      string which is taken verbatim, or a list of multiple search terms if
      there were more than one

    This function parses ``results``: each line should have either the form
    ``FILENAME`` or ``FILENAME: string`` where FILENAME is the file in which
    the string that matched the search was found.  If FILENAME ends in \'.html\',
    then this is part of the documentation; otherwise, it is in the source
    code.  In either case, an appropriate link is created.

    EXAMPLES::

        sage: from sage.misc.sagedoc import format_search_as_html
        sage: format_search_as_html(\'Source\', \'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then\', \'antipode antihomomorphism\')
        \'<html><font color="black"><h2>Search Source: "antipode antihomomorphism"</h2></font><font color="darkpurple"><ol><li><a href="/src/algebras/steenrod_algebra_element.py" target="_blank"><tt>algebras/steenrod_algebra_element.py</tt></a>\\n</ol></font></html>\'
        sage: format_search_as_html(\'Other\', \'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then\', \'antipode antihomomorphism\')
        \'<html><font color="black"><h2>Search Other: "antipode antihomomorphism"</h2></font><font color="darkpurple"><ol><li><a href="/doc/live/reference/sage/algebras/steenrod_algebra_element.html" target="_blank"><tt>reference/sage/algebras/steenrod_algebra_element.html</tt></a>\\n</ol></font></html>\'

    TESTS:

        Test that results from a ``search_src`` with ``multiline=True`` works
        reasonably::

            sage: results = search_src(\'format_search_as_html\',  # long time
            ....:                      multiline=True, interact=False)
            sage: format_search_as_html(\'Source\', results,  # long time
            ....:                       \'format_search_as_html\')
            \'<html><font color="black"><h2>Search Source: "format_search_as_html"</h2></font><font color="darkpurple"><ol><li><a href="/src/misc/sagedoc.py" target="_blank"><tt>misc/sagedoc.py</tt></a>\\n</ol></font></html>\'
    '''
def my_getsource(obj: object, oname: str = '') -> str | None:
    """
    Retrieve the source code for ``obj``.

    INPUT:

    - ``obj`` -- a Sage object, function, etc.

    - ``oname`` -- string (optional); a name under which the object is
      known. Currently ignored by Sage

    OUTPUT:

    Its documentation (string)

    EXAMPLES::

        sage: from sage.misc.sagedoc import my_getsource
        sage: s = my_getsource(identity_matrix)                                         # needs sage.modules
        sage: s[15:34]                                                                  # needs sage.modules
        'def identity_matrix'
    """

class _sage_doc:
    '''
    Open Sage documentation in a web browser, from either the
    command-line or the notebook.

    - Type "browse_sage_doc.DOCUMENT()" to open the named document --
      for example, "browse_sage_doc.tutorial()" opens the tutorial.
      Available documents are

      - tutorial: the Sage tutorial
      - reference: the Sage reference manual
      - constructions: "how do I construct ... in Sage?"
      - developer: the Sage developer\'s guide.

    - Type "browse_sage_doc(OBJECT, output=FORMAT, view=BOOL)" to view
      the documentation for OBJECT, as in
      "browse_sage_doc(identity_matrix, \'html\').  ``output`` can be
      either \'html\' or \'rst\': the form of the output.  ``view`` is
      only relevant if ``output`` is ``html``; in this case, if
      ``view`` is ``True`` (its default value), then open up the
      documentation in a web browser.  Otherwise, just output the
      documentation as a string.

    EXAMPLES::

        sage: browse_sage_doc._open("reference", testing=True)[0]                       # needs sagemath_doc_html
        \'http://localhost:8000/doc/live/reference/index.html\'
        sage: browse_sage_doc(identity_matrix, \'rst\')[-107:-47]                         # needs sage.modules
        \'...Full MatrixSpace of 3 by 3 sparse matrices...\'
    '''
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: browse_sage_doc._base_url
            'http://localhost:8000/doc/live/'
        """
    def __call__(self, obj: object, output: str = 'html', view: bool = True) -> str:
        '''
        Return the documentation for ``obj``.

        INPUT:

        - ``obj`` -- a Sage object
        - ``output`` -- \'html\', \'rst\', or \'text\': return documentation in this form
        - ``view`` -- only has an effect if output is \'html\': in this
          case, if ``view`` is ``True``, display the documentation in
          a web browser.  Otherwise, return the documentation as a
          string.

        EXAMPLES::

            sage: browse_sage_doc(identity_matrix, \'rst\')                               # needs sage.modules
            "...**File:**...**Type:**...**Definition:** identity_matrix..."
            sage: identity_matrix.__doc__ in browse_sage_doc(identity_matrix, \'rst\')    # needs sage.modules
            True
            sage: browse_sage_doc(identity_matrix, \'html\', False)                       # needs sagemath_doc_html sphinx
            \'...div...File:...Type:...Definition:...identity_matrix...\'

        In the \'text\' version, double colons have been replaced with
        single ones (among other things)::

            sage: \'::\' in browse_sage_doc(identity_matrix, \'rst\')                       # needs sage.modules
            True
            sage: \'::\' in browse_sage_doc(identity_matrix, \'text\')                      # needs sphinx
            False
        '''
    def tutorial(self) -> None:
        """
        The Sage tutorial.  To get started with Sage, start here.

        EXAMPLES::

            sage: tutorial()  # indirect doctest, not tested
        """
    def reference(self) -> None:
        """
        The Sage reference manual.

        EXAMPLES::

            sage: reference()  # indirect doctest, not tested
            sage: manual()  # indirect doctest, not tested
        """
    manual = reference
    def developer(self) -> None:
        """
        The Sage developer's guide.  Learn to develop programs for Sage.

        EXAMPLES::

            sage: developer()  # indirect doctest, not tested
        """
    def constructions(self) -> None:
        '''
        Sage constructions.  Attempts to answer the question "How do I
        construct ... in Sage?"

        EXAMPLES::

            sage: constructions()  # indirect doctest, not tested
        '''

browse_sage_doc: _sage_doc
tutorial = browse_sage_doc.tutorial
reference = browse_sage_doc.reference
manual = browse_sage_doc.reference
developer = browse_sage_doc.developer
constructions = browse_sage_doc.constructions
python_help = pydoc.help

def help(module: object = None) -> None:
    """
    If there is an argument ``module``, print the Python help message
    for ``module``.  With no argument, print a help message about
    getting help in Sage.

    EXAMPLES::

        sage: help()
        Welcome to Sage ...
    """
