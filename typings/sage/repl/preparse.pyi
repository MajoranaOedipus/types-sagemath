from _typeshed import Incomplete
from pathlib import Path
from sage.repl.load import load_wrap as load_wrap
from types import SimpleNamespace

implicit_mul_level: bool
numeric_literal_prefix: str

def implicit_multiplication(level=None):
    """
    Turn implicit multiplication on or off, optionally setting a
    specific ``level``.

    INPUT:

    - ``level`` -- boolean or integer (default: 5); how aggressive to be in
      placing \\*'s

      -  0 -- Do nothing
      -  1 -- Numeric followed by alphanumeric
      -  2 -- Closing parentheses followed by alphanumeric
      -  3 -- Spaces between alphanumeric
      - 10 -- Adjacent parentheses (may mangle call statements)

    OUTPUT: the current ``level`` if no argument is given

    EXAMPLES::

      sage: implicit_multiplication(True)
      sage: implicit_multiplication()
      5
      sage: preparse('2x')
      'Integer(2)*x'
      sage: implicit_multiplication(False)
      sage: preparse('2x')
      '2x'

    Note that the `IPython automagic
    <https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-automagic>`_
    feature cannot be used if ``level >= 3``::

        sage: implicit_multiplication(3)
        sage: preparse('cd Documents')
        'cd*Documents'
        sage: implicit_multiplication(2)
        sage: preparse('cd Documents')
        'cd Documents'
        sage: implicit_multiplication(False)

    In this case, one can use the explicit syntax for IPython magics such as
    ``%cd Documents``.
    """
def isalphadigit_(s) -> bool:
    """
    Return ``True`` if ``s`` is a non-empty string of alphabetic characters
    or a non-empty string of digits or just a single ``_``

    EXAMPLES::

        sage: from sage.repl.preparse import isalphadigit_
        sage: isalphadigit_('abc')
        True
        sage: isalphadigit_('123')
        True
        sage: isalphadigit_('_')
        True
        sage: isalphadigit_('a123')
        False
    """

in_single_quote: bool
in_double_quote: bool
in_triple_quote: bool

def in_quote() -> bool: ...

class QuoteStack:
    """The preserved state of parsing in :func:`strip_string_literals`."""
    def __init__(self) -> None:
        """
        Create a new, empty QuoteStack.

        EXAMPLES::

            sage: qs = sage.repl.preparse.QuoteStack()
            sage: len(qs)
            0
        """
    def __len__(self) -> int:
        '''
        Return the number of frames currently on the stack.

        EXAMPLES::

            sage: qs = sage.repl.preparse.QuoteStack(); len(qs)
            0
            sage: qs.push(sage.repl.preparse.QuoteStackFrame("\'")); len(qs)
            1
            sage: qs.pop()
            QuoteStackFrame(...)
            sage: len(qs)
            0
        '''
    def peek(self):
        '''
        Get the frame at the top of the stack or None if empty.

        EXAMPLES::

            sage: qs = sage.repl.preparse.QuoteStack()
            sage: qs.peek()
            sage: qs.push(sage.repl.preparse.QuoteStackFrame(\'"\'))
            sage: qs.peek()
            QuoteStackFrame(...delim=\'"\'...)
        '''
    def pop(self):
        '''
        Remove and return the frame that was most recently added to the stack.

        Raise an :exc:`IndexError` if the stack is empty.

        EXAMPLES::

            sage: qs = sage.repl.preparse.QuoteStack()
            sage: qs.pop()
            Traceback (most recent call last):
            ...
            IndexError: ...
            sage: qs.push(sage.repl.preparse.QuoteStackFrame(\'"\'))
            sage: qs.pop()
            QuoteStackFrame(...delim=\'"\'...)
        '''
    def push(self, frame) -> None:
        '''
        Add a frame to the stack.

        If the frame corresponds to an F-string, its delimiter is marked as no
        longer being a :meth:`safe_delimiter`.

        EXAMPLES::

            sage: qs = sage.repl.preparse.QuoteStack()
            sage: qs.push(sage.repl.preparse.QuoteStackFrame("\'"))
            sage: len(qs)
            1
        '''
    def safe_delimiter(self):
        '''
        Return a string delimiter that may be safely inserted into the code
        output by :func:`strip_string_literals`, if any.

        ``\'`` is preferred over ``"``. The triple-quoted versions are never
        returned since by the time they would be chosen, they would also be invalid.
        ``\'\'\'`` cannot, for example, appear within an F-string delimited by ``\'``.

        Once marked unsafe, a delimiter is never made safe again, even after the
        stack frame that used it is popped. It may no longer be applicable to parsing,
        but it appears somewhere in the processed code, so it is not safe to insert
        just anywhere. A future enhancement could be to map ranges in the processed
        code to the delimiter(s) that would be safe to insert there.

        EXAMPLES::

            sage: from sage.repl.preparse import QuoteStack, QuoteStackFrame
            sage: s = QuoteStack()
            sage: s.safe_delimiter()
            "\'"
            sage: s.push(QuoteStackFrame("\'"))
            sage: s.safe_delimiter()
            "\'"
            sage: s.pop()
            QuoteStackFrame(...)
            sage: s.push(QuoteStackFrame("\'", f_string=True))
            sage: s.safe_delimiter()
            \'"\'
            sage: s.push(QuoteStackFrame(\'"\', f_string=True))
            sage: s.safe_delimiter() is None
            True
        '''

class QuoteStackFrame(SimpleNamespace):
    """
    The state of a single level of a string literal being parsed.

    Only F-strings have more than one level.
    """
    braces: Incomplete
    brackets: Incomplete
    delim: Incomplete
    f_string: Incomplete
    fmt_spec: Incomplete
    nested_fmt_spec: Incomplete
    parens: Incomplete
    raw: Incomplete
    def __init__(self, delim, raw: bool = False, f_string: bool = False, braces: int = 0, parens: int = 0, brackets: int = 0, fmt_spec: bool = False, nested_fmt_spec: bool = False) -> None:
        '''
        Create a new QuoteStackFrame.

        INPUT:

        - ``delim`` -- string; the quote character(s) used: ``\'``, ``"``, ``\'\'\'``, or ``"""``
        - ``raw`` -- boolean (default: ``False``); whether we are in a raw string
        - ``f_string`` -- boolean (default: ``False``); whether we are in an F-string
        - ``braces`` -- integer (default: 0); in an F-string,
          how many unclosed ``{``\'s have we encountered?
        - ``parens`` -- integer (default: 0); in a replacement section of an F-string
          (``braces > 0``), how many unclosed ``(``\'s have we encountered?
        - ``brackets`` -- integer (default: 0); in a replacement section of an F-string
          (``braces > 0``), how many unclosed ``[``\'s have we encountered?
        - ``fmt_spec`` -- boolean (default: ``False``); in the format specifier portion of a
          replacement section?
        - ``nested_fmt_spec`` -- boolean (default: ``False``); in a nested format specifier?
          For example, the ``X`` in ``f\'{value:{width:X}}\'``. Only one level of nesting
          is currently allowed (as of Python 3.8).

        EXAMPLES::

            sage: qsf = sage.repl.preparse.QuoteStackFrame("\'"); qsf
            QuoteStackFrame(braces=0, brackets=0, delim="\'", f_string=False, fmt_spec=False, nested_fmt_spec=False, parens=0, raw=False)
        '''

ssl_search_chars: Incomplete

def strip_string_literals(code, state=None):
    '''
    Return a string with all literal quotes replaced with labels and
    a dictionary of labels for re-substitution.

    This makes parsing easier.

    INPUT:

    - ``code`` -- string; the input

    - ``state`` -- a :class:`QuoteStack` (default: ``None``); state with which to
      continue processing, e.g., across multiple calls to this function

    OUTPUT:

    - a 3-tuple of the processed code, the dictionary of labels, and
      any accumulated state

    EXAMPLES::

        sage: from sage.repl.preparse import strip_string_literals
        sage: s, literals, state = strip_string_literals(r\'\'\'[\'a\', "b", \'c\', "d\\""]\'\'\')
        sage: s
        \'[%(L1)s, %(L2)s, %(L3)s, %(L4)s]\'
        sage: literals
        {\'L1\': "\'a\'", \'L2\': \'"b"\', \'L3\': "\'c\'", \'L4\': \'"d\\\\""\'}
        sage: print(s % literals)
        [\'a\', "b", \'c\', "d\\""]
        sage: print(strip_string_literals(r\'-"\\\\\\""-"\\\\"-\')[0])
        -%(L1)s-%(L2)s-

    Triple-quotes are handled as well::

        sage: s, literals, state = strip_string_literals("[a, \'\'\'b\'\'\', c, \'\']")
        sage: s
        \'[a, %(L1)s, c, %(L2)s]\'
        sage: print(s % literals)
        [a, \'\'\'b\'\'\', c, \'\']

    Comments are substitute too::

        sage: s, literals, state = strip_string_literals("code \'#\' # ccc \'t\'"); s
        \'code %(L1)s #%(L2)s\'
        sage: s % literals
        "code \'#\' # ccc \'t\'"

    A state is returned so one can break strings across multiple calls to
    this function::

        sage: s, literals, state = strip_string_literals(\'s = "some\'); s
        \'s = %(L1)s\'
        sage: s, literals, state = strip_string_literals(\'thing" * 5\', state); s
        \'%(L1)s * 5\'

    TESTS:

    Even for raw strings, a backslash can escape a following quote::

        sage: s, literals, state = strip_string_literals(r"r\'somethin\\\' funny\'"); s
        \'r%(L1)s\'
        sage: dep_regex = r\'^ *(?:(?:cimport +([\\w\\. ,]+))|(?:from +(\\w+) +cimport)|(?:include *[\\\'"]([^\\\'"]+)[\\\'"])|(?:cdef *extern *from *[\\\'"]([^\\\'"]+)[\\\'"]))\' # Issue 5821

    Some extra tests for escaping with odd/even numbers of backslashes::

        sage: s, literals, state = strip_string_literals(r"\'somethin\\\\\' \'funny\'"); s
        \'%(L1)s %(L2)s\'
        sage: literals
        {\'L1\': "\'somethin\\\\\\\\\'", \'L2\': "\'funny\'"}
        sage: s, literals, state = strip_string_literals(r"\'something\\\\\\\' funny\'"); s
        \'%(L1)s\'
        sage: literals
        {\'L1\': "\'something\\\\\\\\\\\\\' funny\'"}

    Braces do not do anything special in normal strings::

        sage: s, literals, state = strip_string_literals("\'before{during}after\'"); s
        \'%(L1)s\'
        sage: literals
        {\'L1\': "\'before{during}after\'"}

    But they are treated special in F-strings::

        sage: s, literals, state = strip_string_literals("f\'before{during}after\'"); s
        \'f%(L1)s{during}%(L2)s\'
        sage: literals
        {\'L1\': "\'before", \'L2\': "after\'"}

    \'#\' is not handled specially inside a replacement section
    (Python will not allow it anyways)::

        sage: s, literals, state = strip_string_literals("f\'#before {#during}\' #after"); s
        \'f%(L1)s{#during}%(L2)s #%(L3)s\'
        sage: literals
        {\'L1\': "\'#before ", \'L2\': "\'", \'L3\': \'after\'}

    \'{{\' and \'}}\' escape sequences only work in the literal portion of an F-string::

        sage: s, literals, state = strip_string_literals("f\'A{{B}}C}}D{{\'"); s
        \'f%(L1)s\'
        sage: literals
        {\'L1\': "\'A{{B}}C}}D{{\'"}
        sage: s, literals, state = strip_string_literals("f\'{ A{{B}}C }\'"); s
        \'f%(L1)s{ A{{B}}C }%(L2)s\'
        sage: literals
        {\'L1\': "\'", \'L2\': "\'"}

    Nested braces in the replacement section (such as for a dict literal)::

        sage: s, literals, state = strip_string_literals(\'\'\' f\'{ {"x":1, "y":2} }\' \'\'\'); s
        \' f%(L1)s{ {%(L2)s:1, %(L3)s:2} }%(L4)s \'
        sage: literals
        {\'L1\': "\'", \'L2\': \'"x"\', \'L3\': \'"y"\', \'L4\': "\'"}

    Format specifier treated as literal except for braced sections within::

        sage: s, literals, state = strip_string_literals("f\'{value:width}\'"); s
        \'f%(L1)s{value:%(L2)s}%(L3)s\'
        sage: literals[\'L2\']
        \'width\'
        sage: s, literals, state = strip_string_literals("f\'{value:{width}}\'"); s
        \'f%(L1)s{value:%(L2)s{width}%(L3)s}%(L4)s\'
        sage: (literals[\'L2\'], literals[\'L3\']) # empty; not ideal, but not harmful
        (\'\', \'\')

    Nested format specifiers -- inside a braced section in the main format
    specifier -- are treated as literals.
    (Python does not allow any deeper nesting.)::

        sage: s, literals, state = strip_string_literals("f\'{value:{width:10}}\'"); s
        \'f%(L1)s{value:%(L2)s{width:%(L3)s}%(L4)s}%(L5)s\'
        sage: literals[\'L3\']
        \'10\'

    A colon inside parentheses does not start the format specifier in order to
    allow lambdas. (Python requires lambdas in F-strings to be in parentheses.)::

        sage: s, literals, state = strip_string_literals("f\'{(lambda x: x^2)(4)}\'"); s
        \'f%(L1)s{(lambda x: x^2)(4)}%(L2)s\'

    Similarly, a colon inside brackets does not start the format specifier in order
    to allow slices::

        sage: s, literals, state = strip_string_literals("f\'{[0, 1, 2, 3][1:3]}\'"); s
        \'f%(L1)s{[0, 1, 2, 3][1:3]}%(L2)s\'

    \'r\' and \'f\' can be mixed to create raw F-strings::

        sage: s, literals, stack = strip_string_literals("\'"); stack.peek()
        QuoteStackFrame(...f_string=False...raw=False...)
        sage: s, literals, stack = strip_string_literals("f\'"); stack.peek()
        QuoteStackFrame(...f_string=True...raw=False...)
        sage: s, literals, stack = strip_string_literals("r\'"); stack.peek()
        QuoteStackFrame(...f_string=False...raw=True...)
        sage: s, literals, stack = strip_string_literals("rf\'"); stack.peek()
        QuoteStackFrame(...f_string=True...raw=True...)
        sage: s, literals, stack = strip_string_literals("fr\'"); stack.peek()
        QuoteStackFrame(...f_string=True...raw=True...)
        sage: s, literals, stack = strip_string_literals("FR\'"); stack.peek()
        QuoteStackFrame(...f_string=True...raw=True...)

    Verify that state gets carried over correctly between calls with F-strings::

        sage: s, lit = [None] * 10, [None] * 10
        sage: s[0], lit[0], stack = strip_string_literals(\'\'); stack
        []
        sage: s[1], lit[1], stack = strip_string_literals(" f\'", stack); stack
        [QuoteStackFrame(braces=0, brackets=0, delim="\'", f_string=True, fmt_spec=False, nested_fmt_spec=False, parens=0, raw=False)]
        sage: s[2], lit[2], stack = strip_string_literals(\'{\', stack); stack
        [QuoteStackFrame(...braces=1...)]
        sage: s[3], lit[3], stack = strip_string_literals(\'r"abc\', stack); stack
        [QuoteStackFrame(...), QuoteStackFrame(...delim=\'"\'...raw=True)]
        sage: s[4], lit[4], stack = strip_string_literals(\'".upper(\', stack); stack
        [QuoteStackFrame(...parens=1...)]
        sage: s[5], lit[5], stack = strip_string_literals(\')[1:\', stack); stack
        [QuoteStackFrame(...brackets=1...parens=0...)]
        sage: s[6], lit[6], stack = strip_string_literals(\']:\', stack); stack
        [QuoteStackFrame(...brackets=0...fmt_spec=True...)]
        sage: s[7], lit[7], stack = strip_string_literals(\'{width:1\', stack); stack
        [QuoteStackFrame(braces=2...nested_fmt_spec=True...)]
        sage: s[8], lit[8], stack = strip_string_literals(\'0}\', stack); stack
        [QuoteStackFrame(braces=1...nested_fmt_spec=False...)]
        sage: s[9], lit[9], stack = strip_string_literals("}\' ", stack); stack
        []
        sage: s_broken_up = "".join(si % liti for si, liti in zip(s, lit)); s_broken_up
        \' f\\\'{r"abc".upper()[1:]:{width:10}}\\\' \'

    Make sure the end result is the same whether broken up into multiple calls
    or processed all at once::

        sage: s, lit, state = strip_string_literals(\'\'\' f\'{r"abc".upper()[1:]:{width:10}}\' \'\'\')
        sage: s_one_time = s % lit; s_one_time
        \' f\\\'{r"abc".upper()[1:]:{width:10}}\\\' \'
        sage: s_broken_up == s_one_time
        True
    '''
def containing_block(code, idx, delimiters=['()', '[]', '{}'], require_delim: bool = True):
    '''
    Find the code block given by balanced delimiters that contains the position ``idx``.

    INPUT:

    - ``code`` -- string

    - ``idx`` -- integer; a starting position

    - ``delimiters`` -- list of strings (default: [\'()\', \'[]\',
      \'{}\']); the delimiters to balance. A delimiter must be a single
      character and no character can at the same time be opening and
      closing delimiter.

    - ``require_delim`` -- boolean (default: ``True``); whether to raise
      a :exc:`SyntaxError` if delimiters are present. If the delimiters are
      unbalanced, an error will be raised in any case.

    OUTPUT:

    - a 2-tuple ``(a,b)`` of integers, such that ``code[a:b]`` is
      delimited by balanced delimiters, ``a<=idx<b``, and ``a``
      is maximal and ``b`` is minimal with that property. If that
      does not exist, a :exc:`SyntaxError` is raised.

    - If ``require_delim`` is false and ``a,b`` as above can not be
      found, then ``0, len(code)`` is returned.

    EXAMPLES::

        sage: from sage.repl.preparse import containing_block
        sage: s = "factor(next_prime(L[5]+1))"
        sage: s[22]
        \'+\'
        sage: start, end = containing_block(s, 22)
        sage: start, end
        (17, 25)
        sage: s[start:end]
        \'(L[5]+1)\'
        sage: s[20]
        \'5\'
        sage: start, end = containing_block(s, 20); s[start:end]
        \'[5]\'
        sage: start, end = containing_block(s, 20, delimiters=[\'()\']); s[start:end]
        \'(L[5]+1)\'
        sage: start, end = containing_block(s, 10); s[start:end]
        \'(next_prime(L[5]+1))\'

    TESTS::

        sage: containing_block(\'((a{))\',0)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'((a{))\',1)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'((a{))\',2)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'((a{))\',3)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'((a{))\',4)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'((a{))\',5)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'(()()\',1)
        (1, 3)
        sage: containing_block(\'(()()\',3)
        (3, 5)
        sage: containing_block(\'(()()\',4)
        (3, 5)
        sage: containing_block(\'(()()\',0)
        Traceback (most recent call last):
        ...
        SyntaxError: unbalanced delimiters
        sage: containing_block(\'(()()\',0, require_delim=False)
        (0, 5)
        sage: containing_block(\'((})()\',1, require_delim=False)
        (0, 6)
        sage: containing_block(\'abc\',1, require_delim=False)
        (0, 3)
    '''
def parse_ellipsis(code, preparse_step: bool = True):
    '''
    Preparses [0,2,..,n] notation.

    INPUT:

    - ``code`` -- string

    - ``preparse_step`` -- boolean (default: ``True``)

    OUTPUT: string

    EXAMPLES::

        sage: from sage.repl.preparse import parse_ellipsis
        sage: parse_ellipsis("[1,2,..,n]")
        \'(ellipsis_range(1,2,Ellipsis,n))\'
        sage: parse_ellipsis("for i in (f(x) .. L[10]):")
        \'for i in (ellipsis_iter(f(x) ,Ellipsis, L[10])):\'
        sage: [1.0..2.0]                                                                # needs sage.rings.real_mpfr
        [1.00000000000000, 2.00000000000000]

    TESTS:

    Check that nested ellipsis is processed correctly (:issue:`17378`)::

        sage: preparse(\'[1,..,2,..,len([1..3])]\')
        \'(ellipsis_range(Integer(1),Ellipsis,Integer(2),Ellipsis,len((ellipsis_range(Integer(1),Ellipsis,Integer(3))))))\'
    '''
def extract_numeric_literals(code):
    '''
    Pulls out numeric literals and assigns them to global variables.
    This eliminates the need to re-parse and create the literals,
    e.g., during every iteration of a loop.

    INPUT:

    - ``code`` -- string; a block of code

    OUTPUT:

    - a (string, string:string dictionary) 2-tuple; the block with
      literals replaced by variable names and a mapping from names to
      the new variables

    EXAMPLES::

        sage: from sage.repl.preparse import extract_numeric_literals
        sage: code, nums = extract_numeric_literals("1.2 + 5")
        sage: print(code)
        _sage_const_1p2  + _sage_const_5
        sage: print(nums)
        {\'_sage_const_1p2\': "RealNumber(\'1.2\')", \'_sage_const_5\': \'Integer(5)\'}

        sage: extract_numeric_literals("[1, 1.1, 1e1, -1e-1, 1.]")[0]
        \'[_sage_const_1 , _sage_const_1p1 , _sage_const_1e1 , -_sage_const_1en1 , _sage_const_1p ]\'

        sage: extract_numeric_literals("[1.sqrt(), 1.2.sqrt(), 1r, 1.2r, R.1, R0.1, (1..5)]")[0]
        \'[_sage_const_1 .sqrt(), _sage_const_1p2 .sqrt(), 1 , 1.2 , R.1, R0.1, (_sage_const_1 .._sage_const_5 )]\'
    '''

all_num_regex: Incomplete

def preparse_numeric_literals(code, extract: bool = False, quotes: str = "'"):
    '''
    Preparse numerical literals into their Sage counterparts,
    e.g. Integer, RealNumber, and ComplexNumber.

    INPUT:

    - ``code`` -- string; a code block to preparse

    - ``extract`` -- boolean (default: ``False``); whether to create
      names for the literals and return a dictionary of
      name-construction pairs

    - ``quotes`` -- string (default: ``"\'"``); used to surround string
      arguments to RealNumber and ComplexNumber, and Integer when the
      number is longer than 4300 digits. If ``None``, will rebuild the
      string using a list of its Unicode code-points.

    OUTPUT:

    - a string or (string, string:string dictionary) 2-tuple; the
      preparsed block and, if ``extract`` is True, the
      name-construction mapping

    EXAMPLES::

        sage: from sage.repl.preparse import preparse_numeric_literals
        sage: preparse_numeric_literals("5")
        \'Integer(5)\'
        sage: preparse_numeric_literals("5j")
        "ComplexNumber(0, \'5\')"
        sage: preparse_numeric_literals("5jr")
        \'5J\'
        sage: preparse_numeric_literals("5l")
        \'5\'
        sage: preparse_numeric_literals("5L")
        \'5\'
        sage: preparse_numeric_literals("1.5")
        "RealNumber(\'1.5\')"
        sage: preparse_numeric_literals("1.5j")
        "ComplexNumber(0, \'1.5\')"
        sage: preparse_numeric_literals(".5j")
        "ComplexNumber(0, \'.5\')"
        sage: preparse_numeric_literals("5e9j")
        "ComplexNumber(0, \'5e9\')"
        sage: preparse_numeric_literals("5.")
        "RealNumber(\'5.\')"
        sage: preparse_numeric_literals("5.j")
        "ComplexNumber(0, \'5.\')"
        sage: preparse_numeric_literals("5.foo()")
        \'Integer(5).foo()\'
        sage: preparse_numeric_literals("5.5.foo()")
        "RealNumber(\'5.5\').foo()"
        sage: preparse_numeric_literals("5.5j.foo()")
        "ComplexNumber(0, \'5.5\').foo()"
        sage: preparse_numeric_literals("5j.foo()")
        "ComplexNumber(0, \'5\').foo()"
        sage: preparse_numeric_literals("1.exp()")
        \'Integer(1).exp()\'
        sage: preparse_numeric_literals("1e+10")
        "RealNumber(\'1e+10\')"
        sage: preparse_numeric_literals("0x0af")
        \'Integer(0x0af)\'
        sage: preparse_numeric_literals("0x10.sqrt()")
        \'Integer(0x10).sqrt()\'
        sage: preparse_numeric_literals(\'0o100\')
        \'Integer(0o100)\'
        sage: preparse_numeric_literals(\'0b111001\')
        \'Integer(0b111001)\'
        sage: preparse_numeric_literals(\'0xe\')
        \'Integer(0xe)\'
        sage: preparse_numeric_literals(\'0xEAR\')
        \'0xEA\'
        sage: preparse_numeric_literals(\'0x1012Fae\')
        \'Integer(0x1012Fae)\'
        sage: preparse_numeric_literals(\'042\')
        \'Integer(42)\'
        sage: preparse_numeric_literals(\'000042\')
        \'Integer(42)\'

    Check that :issue:`40179` is fixed::

        sage: preparse_numeric_literals("1" * 4300) == f"Integer({\'1\' * 4300})"
        True
        sage: preparse_numeric_literals("1" * 4301) == f"Integer(\'{\'1\' * 4301}\')"
        True
        sage: preparse_numeric_literals("1" * 4301, quotes=None) == f\'Integer(str().join(map(chr, {[49] * 4301})))\'
        True

    Test underscores as digit separators (PEP 515,
    https://www.python.org/dev/peps/pep-0515/)::

        sage: preparse_numeric_literals(\'123_456\')
        \'Integer(123_456)\'
        sage: preparse_numeric_literals(\'123_456.78_9_0\')
        "RealNumber(\'123_456.78_9_0\')"
        sage: preparse_numeric_literals(\'0b11_011\')
        \'Integer(0b11_011)\'
        sage: preparse_numeric_literals(\'0o76_321\')
        \'Integer(0o76_321)\'
        sage: preparse_numeric_literals(\'0xaa_aaa\')
        \'Integer(0xaa_aaa)\'
        sage: preparse_numeric_literals(\'1_3.2_5e-2_2\')
        "RealNumber(\'1_3.2_5e-2_2\')"

        sage: for f in ["1_1.", "11_2.", "1.1_1", "1_1.1_1", ".1_1", ".1_1e1_1", ".1e1_1",
        ....:           "1e12_3", "1_1e1_1", "1.1_3e1_2", "1_1e1_1", "1e1", "1.e1_1",
        ....:           "1.0", "1_1.0"]:
        ....:     preparse_numeric_literals(f)
        ....:     assert preparse(f) == preparse_numeric_literals(f), f
        "RealNumber(\'1_1.\')"
        "RealNumber(\'11_2.\')"
        "RealNumber(\'1.1_1\')"
        "RealNumber(\'1_1.1_1\')"
        "RealNumber(\'.1_1\')"
        "RealNumber(\'.1_1e1_1\')"
        "RealNumber(\'.1e1_1\')"
        "RealNumber(\'1e12_3\')"
        "RealNumber(\'1_1e1_1\')"
        "RealNumber(\'1.1_3e1_2\')"
        "RealNumber(\'1_1e1_1\')"
        "RealNumber(\'1e1\')"
        "RealNumber(\'1.e1_1\')"
        "RealNumber(\'1.0\')"
        "RealNumber(\'1_1.0\')"

    Having consecutive underscores is not valid Python syntax, so
    it is not preparsed, and similarly with a trailing underscore::

        sage: preparse_numeric_literals(\'123__45\')
        \'123__45\'
        sage: 123__45
        Traceback (most recent call last):
        ...
        SyntaxError: invalid ...

        sage: preparse_numeric_literals(\'3040_1_\')
        \'3040_1_\'
        sage: 3040_1_
        Traceback (most recent call last):
        ...
        SyntaxError: invalid ...

    Using the ``quotes`` parameter::

        sage: preparse_numeric_literals(\'5j\', quotes=\'"\')
        \'ComplexNumber(0, "5")\'
        sage: preparse_numeric_literals(\'3.14\', quotes="\'\'\'")
        "RealNumber(\'\'\'3.14\'\'\')"
        sage: preparse_numeric_literals(\'3.14\', quotes=None)
        \'RealNumber(str().join(map(chr, [51, 46, 49, 52])))\'
        sage: preparse_numeric_literals(\'5j\', quotes=None)
        \'ComplexNumber(0, str().join(map(chr, [53])))\'
    '''
def strip_prompts(line):
    '''
    Remove leading sage: and >>> prompts so that pasting of examples
    from the documentation works.

    INPUT:

    - ``line`` -- string to process

    OUTPUT: string stripped of leading prompts

    EXAMPLES::

        sage: from sage.repl.preparse import strip_prompts
        sage: strip_prompts("sage: 2 + 2")
        \'2 + 2\'
        sage: strip_prompts(">>>   3 + 2")
        \'3 + 2\'
        sage: strip_prompts("  2 + 4")
        \'  2 + 4\'
    '''
def preparse_calculus(code):
    '''
    Supports calculus-like function assignment, e.g., transforms::

       f(x,y,z) = sin(x^3 - 4*y) + y^x

    into::

       __tmp__=var("x,y,z")
       f = symbolic_expression(sin(x**3 - 4*y) + y**x).function(x,y,z)

    AUTHORS:

    - Bobby Moretti

      - Initial version - 02/2007

    - William Stein

      - Make variables become defined if they are not already defined.

    - Robert Bradshaw

      - Rewrite using regular expressions (01/2009)

    EXAMPLES::

        sage: preparse("f(x) = x^3-x")
        \'__tmp__=var("x"); f = symbolic_expression(x**Integer(3)-x).function(x)\'
        sage: preparse("f(u,v) = u - v")
        \'__tmp__=var("u,v"); f = symbolic_expression(u - v).function(u,v)\'
        sage: preparse("f(x) =-5")
        \'__tmp__=var("x"); f = symbolic_expression(-Integer(5)).function(x)\'
        sage: preparse("f(x) -= 5")
        \'f(x) -= Integer(5)\'
        sage: preparse("f(x_1, x_2) = x_1^2 - x_2^2")
        \'__tmp__=var("x_1,x_2"); f = symbolic_expression(x_1**Integer(2) - x_2**Integer(2)).function(x_1,x_2)\'

    For simplicity, this function assumes all statements begin and end
    with a semicolon::

        sage: from sage.repl.preparse import preparse_calculus
        sage: preparse_calculus(";f(t,s)=t^2;")
        \';__tmp__=var("t,s"); f = symbolic_expression(t^2).function(t,s);\'
        sage: preparse_calculus(";f( t , s ) = t^2;")
        \';__tmp__=var("t,s"); f = symbolic_expression(t^2).function(t,s);\'

    TESTS:

    The arguments in the definition must be symbolic variables (:issue:`10747`)::

        sage: preparse_calculus(";f(_sage_const_)=x;")
        Traceback (most recent call last):
        ...
        ValueError: argument names should be valid python identifiers

    Although preparse_calculus returns something for f(1)=x, when
    preparsing a file an exception is raised because it is invalid python::

        sage: preparse_calculus(";f(1)=x;")
        \';__tmp__=var("1"); f = symbolic_expression(x).function(1);\'

        sage: from sage.repl.preparse import preparse_file
        sage: preparse_file("f(1)=x")
        Traceback (most recent call last):
        ...
        ValueError: argument names should be valid python identifiers

        sage: from sage.repl.preparse import preparse_file
        sage: preparse_file("f(x,1)=2")
        Traceback (most recent call last):
        ...
        ValueError: argument names should be valid python identifiers

    Check support for unicode characters (:issue:`29278`)::

        sage: preparse("μ(x) = x^2")
        \'__tmp__=var("x"); μ = symbolic_expression(x**Integer(2)).function(x)\'

    Check that the parameter list can span multiple lines (:issue:`30928`)::

        sage: preparse(\'\'\'
        ....: f(a,
        ....:   b,
        ....:   c,
        ....:   d) = a + b*2 + c*3 + d*4
        ....: \'\'\')
        \'\\n__tmp__=var("a,b,c,d"); f = symbolic_expression(a + b*Integer(2) + c*Integer(3) + d*Integer(4)).function(a,b,c,d)\\n\'

    Check that :issue:`30953` is fixed::

        sage: preparse(\'\'\'
        ....: f(x) = (x + (x*x) +  # some comment with matching )
        ....:         1); f\'\'\')
        \'\\n__tmp__=var("x"); f = symbolic_expression((x + (x*x) +  # some comment with matching )\\n        Integer(1))).function(x); f\'
    '''
def preparse_generators(code):
    '''
    Parse generator syntax, converting::

        obj.<gen0,gen1,...,genN> = objConstructor(...)

    into::

        obj = objConstructor(..., names=("gen0", "gen1", ..., "genN"))
        (gen0, gen1, ..., genN,) = obj.gens()

    and::

        obj.<gen0,gen1,...,genN> = R[interior]

    into::

        obj = R[interior]; (gen0, gen1, ..., genN,) = obj.gens()

    INPUT:

    - ``code`` -- string

    OUTPUT: string

    LIMITATIONS:

       - The entire constructor *must* be on one line.

    AUTHORS:

    - 2006-04-14: Joe Wetherell (jlwether@alum.mit.edu)

      - Initial version.

    - 2006-04-17: William Stein

      - Improvements to allow multiple statements.

    - 2006-05-01: William

      - Fix bug that Joe found.

    - 2006-10-31: William

      - Fix so obj does not have to be mutated.

    - 2009-01-27: Robert Bradshaw

      - Rewrite using regular expressions

    TESTS::

        sage: from sage.repl.preparse import preparse, preparse_generators

    Vanilla::

        sage: preparse("R.<x> = ZZ[\'x\']")
        "R = ZZ[\'x\']; (x,) = R._first_ngens(1)"
        sage: preparse("R.<x,y> = ZZ[\'x,y\']")
        "R = ZZ[\'x,y\']; (x, y,) = R._first_ngens(2)"

    No square brackets::

        sage: preparse("R.<x> = PolynomialRing(ZZ, \'x\')")
        "R = PolynomialRing(ZZ, \'x\', names=(\'x\',)); (x,) = R._first_ngens(1)"
        sage: preparse("R.<x,y> = PolynomialRing(ZZ, \'x,y\')")
        "R = PolynomialRing(ZZ, \'x,y\', names=(\'x\', \'y\',)); (x, y,) = R._first_ngens(2)"

    Names filled in::

        sage: preparse("R.<x> = ZZ[]")
        "R = ZZ[\'x\']; (x,) = R._first_ngens(1)"
        sage: preparse("R.<x,y> = ZZ[]")
        "R = ZZ[\'x, y\']; (x, y,) = R._first_ngens(2)"

    Names given not the same as generator names::

        sage: preparse("R.<x> = ZZ[\'y\']")
        "R = ZZ[\'y\']; (x,) = R._first_ngens(1)"
        sage: preparse("R.<x,y> = ZZ[\'u,v\']")
        "R = ZZ[\'u,v\']; (x, y,) = R._first_ngens(2)"

    Number fields::

        sage: preparse("K.<a> = QQ[2^(1/3)]")
        \'K = QQ[Integer(2)**(Integer(1)/Integer(3))]; (a,) = K._first_ngens(1)\'
        sage: preparse("K.<a, b> = QQ[2^(1/3), 2^(1/2)]")
        \'K = QQ[Integer(2)**(Integer(1)/Integer(3)), Integer(2)**(Integer(1)/Integer(2))]; (a, b,) = K._first_ngens(2)\'

    Just the .<> notation::

        sage: preparse("R.<x> = ZZx")
        \'R = ZZx; (x,) = R._first_ngens(1)\'
        sage: preparse("R.<x, y> = a+b")
        \'R = a+b; (x, y,) = R._first_ngens(2)\'
        sage: preparse("A.<x,y,z>=FreeAlgebra(ZZ,3)")
        "A = FreeAlgebra(ZZ,Integer(3), names=(\'x\', \'y\', \'z\',)); (x, y, z,) = A._first_ngens(3)"

    Ensure we do not eat too much::

        sage: preparse("R.<x, y> = ZZ;2")
        \'R = ZZ; (x, y,) = R._first_ngens(2);Integer(2)\'
        sage: preparse("R.<x, y> = ZZ[\'x,y\'];2")
        "R = ZZ[\'x,y\']; (x, y,) = R._first_ngens(2);Integer(2)"
        sage: preparse("F.<b>, f, g = S.field_extension()")
        "F, f, g  = S.field_extension(names=(\'b\',)); (b,) = F._first_ngens(1)"

    For simplicity, this function assumes all statements begin and end
    with a semicolon::

        sage: preparse_generators(";  R.<x>=ZZ[];")
        ";  R = ZZ[\'x\']; (x,) = R._first_ngens(1);"

    See :issue:`16731`::

        sage: preparse_generators(\'R.<x> = \')
        \'R.<x> = \'

    Check support for unicode characters (:issue:`29278`)::

        sage: preparse(\'Ω.<λ,μ> = QQ[]\')
        "Ω = QQ[\'λ, μ\']; (λ, μ,) = Ω._first_ngens(2)"

    Check that :issue:`30953` is fixed::

        sage: preparse(\'\'\'
        ....: K.<a> = QuadraticField(2 +
        ....:                        1)\'\'\')
        "\\nK = QuadraticField(Integer(2) +\\n                       Integer(1), names=(\'a\',)); (a,) = K._first_ngens(1)"
        sage: preparse(\'\'\'
        ....: K.<a> = QuadraticField(2 + (1 + 1) + # some comment
        ....:                        1)\'\'\')
        "\\nK = QuadraticField(Integer(2) + (Integer(1) + Integer(1)) + # some comment\\n                       Integer(1), names=(\'a\',)); (a,) = K._first_ngens(1)"
        sage: preparse(\'\'\'
        ....: K.<a> = QuadraticField(2)  # some comment\'\'\')
        "\\nK = QuadraticField(Integer(2), names=(\'a\',)); (a,) = K._first_ngens(1)# some comment"
    '''

quote_state: Incomplete

def preparse(line, reset: bool = True, do_time: bool = False, ignore_prompts: bool = False, numeric_literals: bool = True):
    '''
    Preparse a line of input.

    INPUT:

    - ``line`` -- string

    - ``reset`` -- boolean (default: ``True``)

    - ``do_time`` -- boolean (default: ``False``)

    - ``ignore_prompts`` -- boolean (default: ``False``)

    - ``numeric_literals`` -- boolean (default: ``True``)

    OUTPUT: string

    EXAMPLES::

        sage: preparse("ZZ.<x> = ZZ[\'x\']")
        "ZZ = ZZ[\'x\']; (x,) = ZZ._first_ngens(1)"
        sage: preparse("ZZ.<x> = ZZ[\'y\']")
        "ZZ = ZZ[\'y\']; (x,) = ZZ._first_ngens(1)"
        sage: preparse("ZZ.<x,y> = ZZ[]")
        "ZZ = ZZ[\'x, y\']; (x, y,) = ZZ._first_ngens(2)"
        sage: preparse("ZZ.<x,y> = ZZ[\'u,v\']")
        "ZZ = ZZ[\'u,v\']; (x, y,) = ZZ._first_ngens(2)"
        sage: preparse("ZZ.<x> = QQ[2^(1/3)]")
        \'ZZ = QQ[Integer(2)**(Integer(1)/Integer(3))]; (x,) = ZZ._first_ngens(1)\'
        sage: QQ[2^(1/3)]                                                               # needs sage.rings.number_field sage.symbolic
        Number Field in a with defining polynomial x^3 - 2 with a = 1.259921049894873?

        sage: preparse("a^b")
        \'a**b\'
        sage: preparse("a^^b")
        \'a^b\'
        sage: 8^1
        8
        sage: 8^^1
        9
        sage: 9^^1
        8

        sage: preparse("A \\\\ B")
        \'A  * BackslashOperator() * B\'
        sage: preparse("A^2 \\\\ B + C")
        \'A**Integer(2)  * BackslashOperator() * B + C\'
        sage: preparse("a \\\\ b \\\\") # There is really only one backslash here, it is just being escaped.
        \'a  * BackslashOperator() * b \\\\\'

        sage: preparse("time R.<x> = ZZ[]", do_time=True)
        \'__time__ = cputime(); __wall__ = walltime(); R = ZZ[\\\'x\\\']; print("Time: CPU {:.2f} s, Wall: {:.2f} s".format(cputime(__time__), walltime(__wall__))); (x,) = R._first_ngens(1)\'

    TESTS:

    Check support for unicode characters (:issue:`29278`)::

        sage: preparse("Ω.0")
        \'Ω.gen(0)\'

    Check support for backslash line continuation (:issue:`30928`)::

        sage: preparse("f(x) = x \\\\\\n+ 1")
        \'__tmp__=var("x"); f = symbolic_expression(x + Integer(1)).function(x)\'

    Check that multi-line strings starting with a comment are still preparsed
    (:issue:`31043`)::

        sage: print(preparse(\'\'\'# some comment
        ....: f(x) = x + 1\'\'\'))
        # some comment
        __tmp__=var("x"); f = symbolic_expression(x + Integer(1)).function(x)

    TESTS::

        sage: from sage.repl.preparse import preparse
        sage: lots_of_numbers = "[%s]" % ", ".join(str(i) for i in range(3000))
        sage: _ = preparse(lots_of_numbers)
        sage: print(preparse("type(100r), type(100)"))
        type(100), type(Integer(100))
    '''
def preparse_file(contents, globals=None, numeric_literals: bool = True):
    '''
    Preparse ``contents`` which is input from a file such as ``.sage`` files.

    Special attentions are given to numeric literals and load/attach
    file directives.

    .. NOTE:: Temporarily, if @parallel is in the input, then
       numeric_literals is always set to False.

    INPUT:

    - ``contents`` -- string

    - ``globals`` -- dictionary or ``None`` (default: ``None``); if given, then
      arguments to load/attach are evaluated in the namespace of this dictionary

    - ``numeric_literals`` -- boolean (default: ``True``); whether to factor
      out wrapping of integers and floats, so they do not get created
      repeatedly inside loops

    OUTPUT: string

    TESTS::

        sage: from sage.repl.preparse import preparse_file
        sage: lots_of_numbers = "[%s]" % ", ".join(str(i) for i in range(3000))
        sage: _ = preparse_file(lots_of_numbers)
        sage: print(preparse_file("type(100r), type(100)"))
        _sage_const_100 = Integer(100)
        type(100 ), type(_sage_const_100 )

    Check that :issue:`4545` is fixed::

        sage: file_contents = \'\'\'
        ....: @parallel(8)
        ....: def func(p):
        ....:     t = cputime()
        ....:     M = ModularSymbols(p^2,sign=1)
        ....:     w = M.atkin_lehner_operator(p)
        ....:     K = (w-1).kernel()\'\'\'
        sage: t = tmp_filename(ext=\'.sage\')
        sage: with open(t, \'w\') as file:
        ....:     file.write(file_contents)
        137
        sage: load(t)
        sage: sorted(list(func([11,17])))                                               # needs sage.modular
        [(((11,), {}), None), (((17,), {}), None)]
    '''
def implicit_mul(code, level: int = 5):
    """
    Insert \\*'s to make implicit multiplication explicit.

    INPUT:

    - ``code`` -- string; the code with missing \\*'s

    - ``level`` -- integer (default: 5); see :func:`implicit_multiplication`
      for a list

    OUTPUT: string

    EXAMPLES::

        sage: from sage.repl.preparse import implicit_mul
        sage: implicit_mul('(2x^2-4x+3)a0')
        '(2*x^2-4*x+3)*a0'
        sage: implicit_mul('a b c in L')
        'a*b*c in L'
        sage: implicit_mul('1r + 1e3 + 5exp(2)')
        '1r + 1e3 + 5*exp(2)'
        sage: implicit_mul('f(a)(b)', level=10)
        'f(a)*(b)'

    TESTS:

    Check handling of Python 3 keywords (:issue:`29391`)::

        sage: implicit_mul('nonlocal a')
        'nonlocal a'

    Although these are not keywords in Python 3, we explicitly avoid implicit
    multiplication in these cases because the error message will be more
    helpful (:issue:`29391`)::

        sage: implicit_mul('print 2')
        'print 2'
        sage: implicit_mul('exec s')
        'exec s'

    Check support for unicode characters (:issue:`29278`)::

        sage: implicit_mul('3λ')
        '3*λ'

    Check support for complex literals (:issue:`30477`)::

        sage: implicit_mul('2r-1JR')
        '2r-1JR'
        sage: implicit_mul('1E3 + 0.3E-3rj')
        '1e3 + 0.3e-3rj'
    """
def handle_encoding_declaration(contents, out):
    """
    Find a PEP 263-style Python encoding declaration in the first or
    second line of ``contents``. If found, output it to ``out`` and return
    ``contents`` without the encoding line; otherwise output a default
    UTF-8 declaration and return ``contents``.

    EXAMPLES::

        sage: from sage.repl.preparse import handle_encoding_declaration
        sage: import sys
        sage: c1='# -*- coding: latin-1 -*-\\nimport os, sys\\n...'
        sage: c2='# -*- coding: iso-8859-15 -*-\\nimport os, sys\\n...'
        sage: c3='# -*- coding: ascii -*-\\nimport os, sys\\n...'
        sage: c4='import os, sys\\n...'
        sage: handle_encoding_declaration(c1, sys.stdout)
        # -*- coding: latin-1 -*-
        'import os, sys\\n...'
        sage: handle_encoding_declaration(c2, sys.stdout)
        # -*- coding: iso-8859-15 -*-
        'import os, sys\\n...'
        sage: handle_encoding_declaration(c3, sys.stdout)
        # -*- coding: ascii -*-
        'import os, sys\\n...'
        sage: handle_encoding_declaration(c4, sys.stdout)
        # -*- coding: utf-8 -*-
        'import os, sys\\n...'

    TESTS:

    These are some of the tests listed in PEP 263::

        sage: contents = '#!/usr/bin/python\\n# -*- coding: latin-1 -*-\\nimport os, sys'
        sage: handle_encoding_declaration(contents, sys.stdout)
        # -*- coding: latin-1 -*-
        '#!/usr/bin/python\\nimport os, sys'

        sage: contents = '# This Python file uses the following encoding: utf-8\\nimport os, sys'
        sage: handle_encoding_declaration(contents, sys.stdout)
        # This Python file uses the following encoding: utf-8
        'import os, sys'

        sage: contents = '#!/usr/local/bin/python\\n# coding: latin-1\\nimport os, sys'
        sage: handle_encoding_declaration(contents, sys.stdout)
        # coding: latin-1
        '#!/usr/local/bin/python\\nimport os, sys'

    Two hash marks are okay; this shows up in SageTeX-generated scripts::

        sage: contents = '## -*- coding: utf-8 -*-\\nimport os, sys\\nprint(x)'
        sage: handle_encoding_declaration(contents, sys.stdout)
        ## -*- coding: utf-8 -*-
        'import os, sys\\nprint(x)'

    When the encoding declaration does not match the specification, we
    spit out a default UTF-8 encoding.

    Incorrect coding line::

        sage: contents = '#!/usr/local/bin/python\\n# latin-1\\nimport os, sys'
        sage: handle_encoding_declaration(contents, sys.stdout)
        # -*- coding: utf-8 -*-
        '#!/usr/local/bin/python\\n# latin-1\\nimport os, sys'

    Encoding declaration not on first or second line::

        sage: contents ='#!/usr/local/bin/python\\n#\\n# -*- coding: latin-1 -*-\\nimport os, sys'
        sage: handle_encoding_declaration(contents, sys.stdout)
        # -*- coding: utf-8 -*-
        '#!/usr/local/bin/python\\n#\\n# -*- coding: latin-1 -*-\\nimport os, sys'

    We do not check for legal encoding names; that is Python's job::

        sage: contents ='#!/usr/local/bin/python\\n# -*- coding: utf-42 -*-\\nimport os, sys'
        sage: handle_encoding_declaration(contents, sys.stdout)
        # -*- coding: utf-42 -*-
        '#!/usr/local/bin/python\\nimport os, sys'

    .. NOTE::

        - :pep:`263` says that Python will interpret a UTF-8
          byte order mark as a declaration of UTF-8 encoding, but I do not
          think we do that; this function only sees a Python string so it
          cannot account for a BOM.

        - We default to UTF-8 encoding even though PEP 263 says that
          Python files should default to ASCII.

        - Also see https://docs.python.org/ref/encodings.html.

    AUTHORS:

    - Lars Fischer
    - Dan Drake (2010-12-08, rewrite for :issue:`10440`)
    """
def preparse_file_named_to_stream(name, out) -> None:
    """
    Preparse file named \\code{name} (presumably a .sage file), outputting to
    stream \\code{out}.
    """
def preparse_file_named(name) -> Path:
    '''
    Preparse file named ``name`` (presumably a ``.sage`` file),
    outputting to a temporary file.

    This returns the temporary file as a :class:`Path` object.

    EXAMPLES::

        sage: from sage.repl.preparse import preparse_file_named
        sage: tmpf = tmp_filename(ext=\'.sage\')
        sage: with open(tmpf, \'w\') as f:
        ....:     out = f.write("a = 2")
        sage: preparse_file_named(tmpf)
        PosixPath(\'...sage.py\')
    '''
