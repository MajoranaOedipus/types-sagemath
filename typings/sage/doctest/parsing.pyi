import doctest
import types
from _typeshed import Incomplete
from re import Pattern
from sage.doctest.check_tolerance import ToleranceExceededError as ToleranceExceededError, check_tolerance_complex_domain as check_tolerance_complex_domain, check_tolerance_real_domain as check_tolerance_real_domain, float_regex as float_regex
from sage.doctest.external import available_software as available_software, external_software as external_software
from sage.doctest.marked_output import MarkedOutput as MarkedOutput
from sage.doctest.rif_tol import RIFtol as RIFtol, add_tolerance as add_tolerance
from sage.misc.cachefunc import cached_function as cached_function
from sage.repl.preparse import preparse as preparse, strip_string_literals as strip_string_literals
from typing import Literal, overload

ansi_escape_sequence: Pattern[str]
special_optional_regex_raw: str
tag_with_explanation_regex_raw: str
optional_regex: Pattern[str]
special_optional_regex: Pattern[str]
tag_with_explanation_regex: Pattern[str]
no_doctest_regex: Pattern[str]
optional_tag_regex: Pattern[str]
optional_file_directive_regex: Pattern[str]

@overload
def parse_optional_tags(string: str) -> dict[str, str | None]: ...
@overload
def parse_optional_tags(string: str, *, return_string_sans_tags: Literal[True]) -> tuple[dict[str, str | None], str, bool]: ...
def parse_file_optional_tags(lines) -> dict[str, str | None]:
    '''
    Scan the first few lines for file-level doctest directives.

    INPUT:

    - ``lines`` -- iterable of pairs ``(lineno, line)``

    OUTPUT: dictionary whose keys are strings (tags);
    see :func:`parse_optional_tags`

    EXAMPLES::

        sage: from sage.doctest.parsing import parse_file_optional_tags
        sage: filename = tmp_filename(ext=\'.pyx\')
        sage: with open(filename, "r") as f:
        ....:     parse_file_optional_tags(enumerate(f))
        {}
        sage: with open(filename, "w") as f:
        ....:     _ = f.write("# nodoctest")
        sage: with open(filename, "r") as f:
        ....:     parse_file_optional_tags(enumerate(f))
        {\'not tested\': None}
        sage: with open(filename, "w") as f:
        ....:     _ = f.write("# sage.doctest: "    # broken in two source lines to avoid the pattern
        ....:                 "optional - xyz")     # of relint (multiline_doctest_comment)
        sage: with open(filename, "r") as f:
        ....:     parse_file_optional_tags(enumerate(f))
        {\'xyz\': None}
    '''
def unparse_optional_tags(tags, prefix: str = '# ') -> str:
    """
    Return a comment string that sets ``tags``.

    INPUT:

    - ``tags`` -- dictionary or iterable of tags, as output by
      :func:`parse_optional_tags`

    - ``prefix`` -- to be put before a nonempty string

    EXAMPLES::

        sage: from sage.doctest.parsing import unparse_optional_tags
        sage: unparse_optional_tags({})
        ''
        sage: unparse_optional_tags({'magma': None})
        '# optional - magma'
        sage: unparse_optional_tags({'fictional_optional': None,
        ....:                        'sage.rings.number_field': None,
        ....:                        'scipy': 'just because',
        ....:                        'bliss': None})
        '# optional - bliss fictional_optional, needs scipy (just because) sage.rings.number_field'
        sage: unparse_optional_tags(['long time', 'not tested', 'p4cka9e'], prefix='')
        'long time, not tested, optional - p4cka9e'
    """

optional_tag_columns: Incomplete
standard_tag_columns: Incomplete

def update_optional_tags(line, tags=None, *, add_tags=None, remove_tags=None, force_rewrite: bool = False):
    """
    Return the doctest ``line`` with tags changed.

    EXAMPLES::

        sage: from sage.doctest.parsing import update_optional_tags, optional_tag_columns, standard_tag_columns
        sage: ruler = ''
        sage: for column in optional_tag_columns:
        ....:     ruler += ' ' * (column - len(ruler)) + 'V'
        sage: for column in standard_tag_columns:
        ....:     ruler += ' ' * (column - len(ruler)) + 'v'
        sage: def print_with_ruler(lines):
        ....:     print('|' + ruler)
        ....:     for line in lines:
        ....:         print('|' + line)
        sage: print_with_ruler([  # the tags are obscured in the source file to avoid relint warnings
        ....:     update_optional_tags('    sage: something()  # opt' 'ional - latte_int',
        ....:                          remove_tags=['latte_int', 'wasnt_even_there']),
        ....:     update_optional_tags('    sage: nothing_to_be_seen_here()',
        ....:                          tags=['scipy', 'long time']),
        ....:     update_optional_tags('    sage: nothing_to_be_seen_here(honestly=True)',
        ....:                          add_tags=['scipy', 'long time']),
        ....:     update_optional_tags('    sage: nothing_to_be_seen_here(honestly=True, very=True)',
        ....:                          add_tags=['scipy', 'long time']),
        ....:     update_optional_tags('    sage: no_there_is_absolutely_nothing_to_be_seen_here_i_am_serious()#opt' 'ional:bliss',
        ....:                          add_tags=['scipy', 'long time']),
        ....:     update_optional_tags('    sage: ntbsh()  # abbrv for above#opt' 'ional:bliss',
        ....:                          add_tags={'scipy': None, 'long time': '30s on the highest setting'}),
        ....:     update_optional_tags('    sage: no_there_is_absolutely_nothing_to_be_seen_here_i_am_serious()  # really, you can trust me here',
        ....:                          add_tags=['scipy']),
        ....: ])
        |                                                V       V       V       V       V   V   v           v                   v                                       v
        |    sage: something()
        |    sage: nothing_to_be_seen_here()             # long time                             # needs scipy
        |    sage: nothing_to_be_seen_here(honestly=True)        # long time                     # needs scipy
        |    sage: nothing_to_be_seen_here(honestly=True, very=True)     # long time             # needs scipy
        |    sage: no_there_is_absolutely_nothing_to_be_seen_here_i_am_serious()         # long time, optional - bliss, needs scipy
        |    sage: ntbsh()  # abbrv for above            # long time (30s on the highest setting), optional - bliss, needs scipy
        |    sage: no_there_is_absolutely_nothing_to_be_seen_here_i_am_serious()  # really, you can trust me here                # needs scipy

    When no tags are changed, by default, the unchanged input is returned.
    We can force a rewrite; unconditionally or whenever standard tags are involved.
    But even when forced, if comments are already aligned at one of the standard alignment columns,
    this alignment is kept even if we would normally realign farther to the left::

        sage: print_with_ruler([
        ....:     update_optional_tags('    sage: unforced()       # opt' 'ional - latte_int'),
        ....:     update_optional_tags('    sage: unforced()  # opt' 'ional - latte_int',
        ....:                          add_tags=['latte_int']),
        ....:     update_optional_tags('    sage: forced()#opt' 'ional- latte_int',
        ....:                          force_rewrite=True),
        ....:     update_optional_tags('    sage: forced()  # opt' 'ional - scipy',
        ....:                          force_rewrite='standard'),
        ....:     update_optional_tags('    sage: aligned_with_below()                                  # opt' 'ional - 4ti2',
        ....:                          force_rewrite=True),
        ....:     update_optional_tags('    sage: aligned_with_above()                                  # opt' 'ional - 4ti2',
        ....:                          force_rewrite=True),
        ....:     update_optional_tags('    sage: also_already_aligned()                                                                                        # ne' 'eds scipy',
        ....:                          force_rewrite='standard'),
        ....:     update_optional_tags('    sage: two_columns_first_preserved()         # lo' 'ng time                             # ne' 'eds scipy',
        ....:                          force_rewrite='standard'),
        ....:     update_optional_tags('    sage: two_columns_first_preserved()                 # lo' 'ng time                                 # ne' 'eds scipy',
        ....:                          force_rewrite='standard'),
        ....: ])
        |                                                V       V       V       V       V   V   v           v                   v                                       v
        |    sage: unforced()       # optional - latte_int
        |    sage: unforced()  # optional - latte_int
        |    sage: forced()                              # optional - latte_int
        |    sage: forced()                                                                      # needs scipy
        |    sage: aligned_with_below()                                  # optional - 4ti2
        |    sage: aligned_with_above()                                  # optional - 4ti2
        |    sage: also_already_aligned()                                                                                        # needs scipy
        |    sage: two_columns_first_preserved()         # long time                             # needs scipy
        |    sage: two_columns_first_preserved()                 # long time                     # needs scipy

    Rewriting a persistent (block-scoped) tag::

        sage: print_with_ruler([
        ....:     update_optional_tags('    sage:    #opt' 'ional:magma sage.symbolic',
        ....:                          force_rewrite=True),
        ....: ])
        |                                                V       V       V       V       V   V   v           v                   v                                       v
        |    sage: # optional - magma, needs sage.symbolic
    """
def parse_tolerance(source, want):
    '''
    Return a version of ``want`` marked up with the tolerance tags
    specified in ``source``.

    INPUT:

    - ``source`` -- string, the source of a doctest
    - ``want`` -- string, the desired output of the doctest

    OUTPUT: ``want`` if there are no tolerance tags specified; a
    :class:`MarkedOutput` version otherwise

    EXAMPLES::

        sage: from sage.doctest.parsing import parse_tolerance
        sage: marked = parse_tolerance("sage: s.update(abs_tol = .0000001)", "")
        sage: type(marked)
        <class \'str\'>
        sage: marked = parse_tolerance("sage: s.update(tol = 0.1); s.rel_tol # abs tol     0.01 ", "")
        sage: marked.tol
        0
        sage: marked.rel_tol
        0
        sage: marked.abs_tol
        0.010000000000000000000...?
    '''
def pre_hash(s) -> str:
    '''
    Prepends a string with its length.

    EXAMPLES::

        sage: from sage.doctest.parsing import pre_hash
        sage: pre_hash("abc")
        \'3:abc\'
    '''
def get_source(example):
    '''
    Return the source with the leading \'sage: \' stripped off.

    EXAMPLES::

        sage: from sage.doctest.parsing import get_source
        sage: from sage.doctest.sources import DictAsObject
        sage: example = DictAsObject({})
        sage: example.sage_source = "2 + 2"
        sage: example.source = "sage: 2 + 2"
        sage: get_source(example)
        \'2 + 2\'
        sage: example = DictAsObject({})
        sage: example.source = "3 + 3"
        sage: get_source(example)
        \'3 + 3\'
    '''
def reduce_hex(fingerprints):
    '''
    Return a symmetric function of the arguments as hex strings.

    The arguments should be 32 character strings consisting of hex
    digits: 0-9 and a-f.

    EXAMPLES::

        sage: from sage.doctest.parsing import reduce_hex
        sage: reduce_hex(["abc", "12399aedf"])
        \'0000000000000000000000012399a463\'
        sage: reduce_hex(["12399aedf","abc"])
        \'0000000000000000000000012399a463\'
    '''

class OriginalSource:
    """
    Context swapping out the pre-parsed source with the original for
    better reporting.

    EXAMPLES::

        sage: from sage.doctest.sources import FileDocTestSource
        sage: from sage.doctest.control import DocTestDefaults
        sage: filename = sage.doctest.forker.__file__
        sage: FDS = FileDocTestSource(filename, DocTestDefaults())
        sage: doctests, extras = FDS.create_doctests(globals())
        sage: ex = doctests[0].examples[0]
        sage: ex.sage_source
        'doctest_var = 42; doctest_var^2\\n'
        sage: ex.source
        'doctest_var = Integer(42); doctest_var**Integer(2)\\n'
        sage: from sage.doctest.parsing import OriginalSource
        sage: with OriginalSource(ex):
        ....:     ex.source
        'doctest_var = 42; doctest_var^2\\n'
    """
    example: Incomplete
    def __init__(self, example) -> None:
        """
        Swaps out the source for the sage_source of a doctest example.

        INPUT:

        - ``example`` -- a :class:`doctest.Example` instance

        EXAMPLES::

            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: from sage.doctest.parsing import OriginalSource
            sage: OriginalSource(ex)
            <sage.doctest.parsing.OriginalSource object at ...>
        """
    def __enter__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: from sage.doctest.parsing import OriginalSource
            sage: with OriginalSource(ex): # indirect doctest
            ....:     ex.source
            'doctest_var = 42; doctest_var^2\\n'
        """
    def __exit__(self, *args) -> None:
        """
        EXAMPLES::

            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: from sage.doctest.parsing import OriginalSource
            sage: with OriginalSource(ex): # indirect doctest
            ....:     ex.source
            'doctest_var = 42; doctest_var^2\\n'
            sage: ex.source # indirect doctest
            'doctest_var = Integer(42); doctest_var**Integer(2)\\n'
        """

class SageDocTestParser(doctest.DocTestParser):
    """
    A version of the standard doctest parser which handles Sage's
    custom options and tolerances in floating point arithmetic.
    """
    long: bool
    file_optional_tags: set[str]
    optional_tags: bool | set[str]
    optional_only: bool
    optionals: dict[str, int]
    probed_tags: bool | set[str]
    def __init__(self, optional_tags=(), long: bool = False, *, probed_tags=(), file_optional_tags=()) -> None:
        '''
        INPUT:

        - ``optional_tags`` -- list or tuple of strings
        - ``long`` -- boolean, whether to run doctests marked as taking a
          long time
        - ``probed_tags`` -- list or tuple of strings
        - ``file_optional_tags`` -- an iterable of strings

        EXAMPLES::

            sage: from sage.doctest.parsing import SageDocTestParser
            sage: DTP = SageDocTestParser((\'sage\',\'magma\',\'guava\'))
            sage: ex = DTP.parse("sage: 2 + 2\\n")[1]
            sage: ex.sage_source
            \'2 + 2\\n\'
            sage: ex = DTP.parse("sage: R.<x> = ZZ[]")[1]
            sage: ex.source
            "R = ZZ[\'x\']; (x,) = R._first_ngens(1)\\n"

        TESTS::

            sage: TestSuite(DTP).run()
        '''
    def __eq__(self, other):
        """
        Comparison.

        EXAMPLES::

            sage: from sage.doctest.parsing import SageDocTestParser
            sage: DTP = SageDocTestParser(('sage','magma','guava'), True)
            sage: DTP2 = SageDocTestParser(('sage','magma','guava'), False)
            sage: DTP == DTP2
            False
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        EXAMPLES::

            sage: from sage.doctest.parsing import SageDocTestParser
            sage: DTP = SageDocTestParser(('sage','magma','guava'), True)
            sage: DTP2 = SageDocTestParser(('sage','magma','guava'), False)
            sage: DTP != DTP2
            True
        """
    def parse(self, string, *args) -> list[doctest.Example | str]:
        '''
        A Sage specialization of :class:`doctest.DocTestParser`.

        INPUT:

        - ``string`` -- the string to parse
        - ``name`` -- (optional) string giving the name identifying string,
          to be used in error messages

        OUTPUT:

        - A list consisting of strings and :class:`doctest.Example`
          instances.  There will be at least one string between
          successive examples (exactly one unless long or optional
          tests are removed), and it will begin and end with a string.

        EXAMPLES::

            sage: from sage.doctest.parsing import SageDocTestParser
            sage: DTP = SageDocTestParser((\'sage\',\'magma\',\'guava\'))
            sage: example = \'Explanatory text::\\n\\n    sage: E = magma("EllipticCurve([1, 1, 1, -10, -10])") # optional: magma\\n\\nLater text\'
            sage: parsed = DTP.parse(example)
            sage: parsed[0]
            \'Explanatory text::\\n\\n\'
            sage: parsed[1].sage_source
            \'E = magma("EllipticCurve([1, 1, 1, -10, -10])") # optional: magma\\n\'
            sage: parsed[2]
            \'\\nLater text\'

        If the doctest parser is not created to accept a given
        optional argument, the corresponding examples will just be
        removed::

            sage: DTP2 = SageDocTestParser((\'sage\',))
            sage: parsed2 = DTP2.parse(example)
            sage: parsed2
            [\'Explanatory text::\\n\\n\', \'\\nLater text\']

        You can mark doctests as having a particular tolerance::

            sage: example2 = \'sage: gamma(1.6) # tol 2.0e-11\\n0.893515349287690\'
            sage: ex = DTP.parse(example2)[1]
            sage: ex.sage_source
            \'gamma(1.6) # tol 2.0e-11\\n\'
            sage: ex.want
            \'0.893515349287690\\n\'
            sage: type(ex.want)
            <class \'sage.doctest.marked_output.MarkedOutput\'>
            sage: ex.want.tol
            2.000000000000000000...?e-11

        You can use continuation lines::

            sage: s = "sage: for i in range(4):\\n....:     print(i)\\n....:\\n"
            sage: ex = DTP2.parse(s)[1]
            sage: ex.source
            \'for i in range(Integer(4)):\\n    print(i)\\n\'

        Optional tags at the start of an example block persist to the end of
        the block (delimited by a blank line)::

            sage: # long time, needs sage.rings.number_field
            sage: QQbar(I)^10000
            1
            sage: QQbar(I)^10000  # not tested
            I

            sage: # needs sage.rings.finite_rings
            sage: GF(7)
            Finite Field of size 7
            sage: GF(10)
            Traceback (most recent call last):
            ...
            ValueError: the order of a finite field must be a prime power

        Test that :issue:`26575` is resolved::

            sage: example3 = \'sage: Zp(5,4,print_mode="digits")(5)\\n...00010\'
            sage: parsed3 = DTP.parse(example3)
            sage: dte = parsed3[1]
            sage: dte.sage_source
            \'Zp(5,4,print_mode="digits")(5)\\n\'
            sage: dte.want
            \'...00010\\n\'

        Style warnings::

            sage: def parse(test_string):
            ....:     return [x if isinstance(x, str)
            ....:               else (getattr(x, \'warnings\', None), x.sage_source, x.source)
            ....:             for x in DTP.parse(test_string)]

            sage: parse(\'sage: 1 # optional guava mango\\nsage: 2 # optional guava\\nsage: 3 # optional guava\\nsage: 4 # optional guava\\nsage: 5 # optional guava\\n\\nsage: 11 # optional guava\')
            [\'\',
             (["Consider using a block-scoped tag by inserting the line \'sage: # optional - guava\' just before this line to avoid repeating the tag 5 times"],
              \'1 # optional guava mango\\n\',
              \'None  # virtual doctest\'),
             \'\',
             (None, \'2 # optional guava\\n\', \'Integer(2) # optional guava\\n\'),
             \'\',
             (None, \'3 # optional guava\\n\', \'Integer(3) # optional guava\\n\'),
             \'\',
             (None, \'4 # optional guava\\n\', \'Integer(4) # optional guava\\n\'),
             \'\',
             (None, \'5 # optional guava\\n\', \'Integer(5) # optional guava\\n\'),
             \'\\n\',
             (None, \'11 # optional guava\\n\', \'Integer(11) # optional guava\\n\'),
             \'\']

            sage: parse(\'sage: 1 # optional guava\\nsage: 2 # optional guava mango\\nsage: 3 # optional guava\\nsage: 4 # optional guava\\nsage: 5 # optional guava\\n\')
            [\'\',
             (["Consider using a block-scoped tag by inserting the line \'sage: # optional - guava\' just before this line to avoid repeating the tag 5 times"],
              \'1 # optional guava\\n\',
              \'Integer(1) # optional guava\\n\'),
             \'\',
             \'\',
             (None, \'3 # optional guava\\n\', \'Integer(3) # optional guava\\n\'),
             \'\',
             (None, \'4 # optional guava\\n\', \'Integer(4) # optional guava\\n\'),
             \'\',
             (None, \'5 # optional guava\\n\', \'Integer(5) # optional guava\\n\'),
             \'\']

            sage: parse(\'sage: # optional mango\\nsage: 1 # optional guava\\nsage: 2 # optional guava mango\\nsage: 3 # optional guava\\nsage: 4 # optional guava\\n sage: 5 # optional guava\\n\')  # optional - guava mango
            [\'\',
             (["Consider updating this block-scoped tag to \'sage: # optional - guava mango\' to avoid repeating the tag 5 times"],
              \'# optional mango\\n\',
              \'None  # virtual doctest\'),
             \'\',
             \'\',
             \'\',
             \'\',
             \'\',
             \'\']

            sage: parse(\'::\\n\\n    sage: 1 # optional guava\\n    sage: 2 # optional guava mango\\n    sage: 3 # optional guava\\n\\n::\\n\\n    sage: 4 # optional guava\\n     sage: 5 # optional guava\\n\')
            [\'::\\n\\n\',
            (None, \'1 # optional guava\\n\', \'Integer(1) # optional guava\\n\'),
            \'\',
            \'\',
            (None, \'3 # optional guava\\n\', \'Integer(3) # optional guava\\n\'),
            \'\\n::\\n\\n\',
            (None, \'4 # optional guava\\n\', \'Integer(4) # optional guava\\n\'),
            \'\',
            (None, \'5 # optional guava\\n\', \'Integer(5) # optional guava\\n\'),
            \'\']

        TESTS::

            sage: parse("::\\n\\n    sage: # needs sage.combinat\\n    sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\\\\n    ....:         import incidence_matrix_to_bit_rep_of_Vrep\\n    sage: P = polytopes.associahedron([\'A\',3])\\n\\n")
            [\'::\\n\\n\',
             \'\',
             (None,
              \'from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\\\\n        import incidence_matrix_to_bit_rep_of_Vrep\\n\',
              \'from sage.geometry.polyhedron.combinatorial_polyhedron.conversions         import incidence_matrix_to_bit_rep_of_Vrep\\n\'),
             \'\',
             (None,
              "P = polytopes.associahedron([\'A\',3])\\n",
              "P = polytopes.associahedron([\'A\',Integer(3)])\\n"),
             \'\\n\']

            sage: example4 = \'::\\n\\n        sage: C.minimum_distance(algorithm="guava")  # optional - guava\\n        ...\\n        24\\n\\n\'
            sage: parsed4 = DTP.parse(example4)
            sage: dte = parsed4[1]
            sage: dte.sage_source
            \'C.minimum_distance(algorithm="guava")  # optional - guava\\n\'
            sage: dte.want
            \'...\\n24\\n\'
        '''

class SageOutputChecker(doctest.OutputChecker):
    """
    A modification of the doctest OutputChecker that can check
    relative and absolute tolerance of answers.

    EXAMPLES::

        sage: from sage.doctest.parsing import SageOutputChecker, MarkedOutput, SageDocTestParser
        sage: import doctest
        sage: optflag = doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
        sage: DTP = SageDocTestParser(('sage','magma','guava'))
        sage: OC = SageOutputChecker()
        sage: example2 = 'sage: gamma(1.6) # tol 2.0e-11\\n0.893515349287690'
        sage: ex = DTP.parse(example2)[1]
        sage: ex.sage_source
        'gamma(1.6) # tol 2.0e-11\\n'
        sage: ex.want
        '0.893515349287690\\n'
        sage: type(ex.want)
        <class 'sage.doctest.marked_output.MarkedOutput'>
        sage: ex.want.tol
        2.000000000000000000...?e-11
        sage: OC.check_output(ex.want, '0.893515349287690', optflag)
        True
        sage: OC.check_output(ex.want, '0.8935153492877', optflag)
        True
        sage: OC.check_output(ex.want, '0', optflag)
        False
        sage: OC.check_output(ex.want, 'x + 0.8935153492877', optflag)
        False
    """
    def human_readable_escape_sequences(self, string):
        """
        Make ANSI escape sequences human readable.

        EXAMPLES::

            sage: print('This is \\x1b[1mbold\\x1b[0m text')
            This is <CSI-1m>bold<CSI-0m> text

        TESTS::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: OC = SageOutputChecker()
            sage: teststr = '-'.join([
            ....:     'bold\\x1b[1m',
            ....:     'red\\x1b[31m',
            ....:     'oscmd\\x1ba'])
            sage: OC.human_readable_escape_sequences(teststr)
            'bold<CSI-1m>-red<CSI-31m>-oscmd<ESC-a>'
        """
    def check_output(self, want, got, optionflags):
        '''
        Check to see if the output matches the desired output.

        If ``want`` is a :class:`MarkedOutput` instance, takes into account the desired tolerance.

        INPUT:

        - ``want`` -- string or :class:`MarkedOutput`
        - ``got`` -- string
        - ``optionflags`` -- integer; passed down to :class:`doctest.OutputChecker`

        OUTPUT: boolean; whether ``got`` matches ``want`` up to the specified
        tolerance

        EXAMPLES::

            sage: from sage.doctest.parsing import MarkedOutput, SageOutputChecker
            sage: import doctest
            sage: optflag = doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
            sage: rndstr = MarkedOutput("I\'m wrong!").update(random=True)
            sage: tentol = MarkedOutput("10.0").update(tol=.1)
            sage: tenabs = MarkedOutput("10.0").update(abs_tol=.1)
            sage: tenrel = MarkedOutput("10.0").update(rel_tol=.1)
            sage: zerotol = MarkedOutput("0.0").update(tol=.1)
            sage: zeroabs = MarkedOutput("0.0").update(abs_tol=.1)
            sage: zerorel = MarkedOutput("0.0").update(rel_tol=.1)
            sage: zero = "0.0"
            sage: nf = "9.5"
            sage: ten = "10.05"
            sage: eps = "-0.05"
            sage: OC = SageOutputChecker()

        ::

            sage: OC.check_output(rndstr,nf,optflag)
            True

            sage: OC.check_output(tentol,nf,optflag)
            True
            sage: OC.check_output(tentol,ten,optflag)
            True
            sage: OC.check_output(tentol,zero,optflag)
            False

            sage: OC.check_output(tenabs,nf,optflag)
            False
            sage: OC.check_output(tenabs,ten,optflag)
            True
            sage: OC.check_output(tenabs,zero,optflag)
            False

            sage: OC.check_output(tenrel,nf,optflag)
            True
            sage: OC.check_output(tenrel,ten,optflag)
            True
            sage: OC.check_output(tenrel,zero,optflag)
            False

            sage: OC.check_output(zerotol,zero,optflag)
            True
            sage: OC.check_output(zerotol,eps,optflag)
            True
            sage: OC.check_output(zerotol,ten,optflag)
            False

            sage: OC.check_output(zeroabs,zero,optflag)
            True
            sage: OC.check_output(zeroabs,eps,optflag)
            True
            sage: OC.check_output(zeroabs,ten,optflag)
            False

            sage: OC.check_output(zerorel,zero,optflag)
            True
            sage: OC.check_output(zerorel,eps,optflag)
            False
            sage: OC.check_output(zerorel,ten,optflag)
            False

        More explicit tolerance checks::

            sage: _ = x  # rel tol 1e10                                                 # needs sage.symbolic
            sage: raise RuntimeError   # rel tol 1e10
            Traceback (most recent call last):
            ...
            RuntimeError
            sage: 1  # abs tol 2
            -0.5
            sage: print("0.9999")    # rel tol 1e-4
            1.0
            sage: print("1.00001")   # abs tol 1e-5
            1.0
            sage: 0  # rel tol 1
            1

        Abs tol checks over the complex domain::

            sage: [1, -1.3, -1.5 + 0.1*I, 0.5 - 0.1*I, -1.5*I]  # abs tol 1.0
            [1, -1, -1, 1, -I]

        Spaces before numbers or between the sign and number are ignored::

            sage: print("[ - 1, 2]")  # abs tol 1e-10
            [-1,2]

        Tolerance on Python 3 for string results with unicode prefix::

            sage: a = \'Cyrano\'; a
            \'Cyrano\'
            sage: b = [\'Fermat\', \'Euler\']; b
            [\'Fermat\',  \'Euler\']
            sage: c = \'you\'; c
            \'you\'

        This illustrates that :issue:`33588` is fixed::

            sage: from sage.doctest.parsing import SageOutputChecker, SageDocTestParser
            sage: import doctest
            sage: optflag = doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
            sage: DTP = SageDocTestParser((\'sage\',\'magma\',\'guava\'))
            sage: OC = SageOutputChecker()
            sage: example = "sage: 1.3090169943749475 # tol 1e-8\\n1.3090169943749475"
            sage: ex = DTP.parse(example)[1]
            sage: OC.check_output(ex.want, \'1.3090169943749475\', optflag)
            True
            sage: OC.check_output(ex.want, \'ANYTHING1.3090169943749475\', optflag)
            False
            sage: OC.check_output(ex.want, \'Long-step dual simplex will be used\\n1.3090169943749475\', optflag)
            True
        '''
    def do_fixup(self, want, got):
        '''
        Perform few changes to the strings ``want`` and ``got``.

        For example, remove warnings to be ignored.

        INPUT:

        - ``want`` -- string or :class:`MarkedOutput`
        - ``got`` -- string

        OUTPUT: a tuple:

        - boolean, ``True`` when some fixup were performed and ``False`` otherwise
        - string, edited wanted string
        - string, edited got string

        .. NOTE::

            Currently, the code only possibly changes the string ``got``
            while keeping ``want`` invariant. We keep open the possibility
            of adding a regular expression which would also change the
            ``want`` string. This is why ``want`` is an input and an output
            of the method even if currently kept invariant.

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: OC = SageOutputChecker()
            sage: OC.do_fixup(\'1.3090169943749475\',\'1.3090169943749475\')
            (False, \'1.3090169943749475\', \'1.3090169943749475\')
            sage: OC.do_fixup(\'1.3090169943749475\',\'ANYTHING1.3090169943749475\')
            (False, \'1.3090169943749475\', \'ANYTHING1.3090169943749475\')
            sage: OC.do_fixup(\'1.3090169943749475\',\'Long-step dual simplex will be used\\n1.3090169943749475\')
            (True, \'1.3090169943749475\', \'\\n1.3090169943749475\')

        When ``want`` is an instance of class :class:`MarkedOutput`::

            sage: from sage.doctest.parsing import SageOutputChecker, SageDocTestParser
            sage: import doctest
            sage: optflag = doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
            sage: DTP = SageDocTestParser((\'sage\',\'magma\',\'guava\'))
            sage: OC = SageOutputChecker()
            sage: example = "sage: 1.3090169943749475\\n1.3090169943749475"
            sage: ex = DTP.parse(example)[1]
            sage: ex.want
            \'1.3090169943749475\\n\'
            sage: OC.do_fixup(ex.want,\'1.3090169943749475\')
            (False, \'1.3090169943749475\\n\', \'1.3090169943749475\')
            sage: OC.do_fixup(ex.want,\'ANYTHING1.3090169943749475\')
            (False, \'1.3090169943749475\\n\', \'ANYTHING1.3090169943749475\')
            sage: OC.do_fixup(ex.want,\'Long-step dual simplex will be used\\n1.3090169943749475\')
            (True, \'1.3090169943749475\\n\', \'\\n1.3090169943749475\')
        '''
    def output_difference(self, example, got, optionflags):
        '''
        Report on the differences between the desired result and what
        was actually obtained.

        If ``want`` is a :class:`MarkedOutput` instance, takes into account the desired tolerance.

        INPUT:

        - ``example`` -- a :class:`doctest.Example` instance
        - ``got`` -- string
        - ``optionflags`` -- integer; passed down to :class:`doctest.OutputChecker`

        OUTPUT: string, describing how ``got`` fails to match ``example.want``

        EXAMPLES::

            sage: from sage.doctest.parsing import MarkedOutput, SageOutputChecker
            sage: import doctest
            sage: optflag = doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
            sage: tentol = doctest.Example(\'\',MarkedOutput("10.0\\n").update(tol=.1))
            sage: tenabs = doctest.Example(\'\',MarkedOutput("10.0\\n").update(abs_tol=.1))
            sage: tenrel = doctest.Example(\'\',MarkedOutput("10.0\\n").update(rel_tol=.1))
            sage: zerotol = doctest.Example(\'\',MarkedOutput("0.0\\n").update(tol=.1))
            sage: zeroabs = doctest.Example(\'\',MarkedOutput("0.0\\n").update(abs_tol=.1))
            sage: zerorel = doctest.Example(\'\',MarkedOutput("0.0\\n").update(rel_tol=.1))
            sage: tlist = doctest.Example(\'\',MarkedOutput("[10.0, 10.0, 10.0, 10.0, 10.0, 10.0]\\n").update(abs_tol=0.987))
            sage: zero = "0.0"
            sage: nf = "9.5"
            sage: ten = "10.05"
            sage: eps = "-0.05"
            sage: L = "[9.9, 8.7, 10.3, 11.2, 10.8, 10.0]"
            sage: OC = SageOutputChecker()

        ::

            sage: print(OC.output_difference(tenabs,nf,optflag))
            Expected:
                10.0
            Got:
                9.5
            Tolerance exceeded:
                10.0 vs 9.5, tolerance 5e-1 > 1e-1

            sage: print(OC.output_difference(tentol,zero,optflag))
            Expected:
                10.0
            Got:
                0.0
            Tolerance exceeded:
                10.0 vs 0.0, tolerance 1e0 > 1e-1

            sage: print(OC.output_difference(tentol,eps,optflag))
            Expected:
                10.0
            Got:
                -0.05
            Tolerance exceeded:
                10.0 vs -0.05, tolerance 2e0 > 1e-1

            sage: print(OC.output_difference(tlist,L,optflag))
            Expected:
                [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
            Got:
                [9.9, 8.7, 10.3, 11.2, 10.8, 10.0]
            Tolerance exceeded in 2 of 6:
                10.0 vs 8.7, tolerance 2e0 > 9.87e-1
                10.0 vs 11.2, tolerance 2e0 > 9.87e-1

        TESTS::

            sage: print(OC.output_difference(tenabs,zero,optflag))
            Expected:
                10.0
            Got:
                0.0
            Tolerance exceeded:
                10.0 vs 0.0, tolerance 1e1 > 1e-1

            sage: print(OC.output_difference(tenrel,zero,optflag))
            Expected:
                10.0
            Got:
                0.0
            Tolerance exceeded:
                10.0 vs 0.0, tolerance 1e0 > 1e-1

            sage: print(OC.output_difference(tenrel,eps,optflag))
            Expected:
                10.0
            Got:
                -0.05
            Tolerance exceeded:
                10.0 vs -0.05, tolerance 2e0 > 1e-1

            sage: print(OC.output_difference(zerotol,ten,optflag))
            Expected:
                0.0
            Got:
                10.05
            Tolerance exceeded:
                0.0 vs 10.05, tolerance 2e1 > 1e-1

            sage: print(OC.output_difference(zeroabs,ten,optflag))
            Expected:
                0.0
            Got:
                10.05
            Tolerance exceeded:
                0.0 vs 10.05, tolerance 2e1 > 1e-1

            sage: print(OC.output_difference(zerorel,eps,optflag))
            Expected:
                0.0
            Got:
                -0.05
            Tolerance exceeded:
                0.0 vs -0.05, tolerance +infinity > 1e-1

            sage: print(OC.output_difference(zerorel,ten,optflag))
            Expected:
                0.0
            Got:
                10.05
            Tolerance exceeded:
                0.0 vs 10.05, tolerance +infinity > 1e-1
        '''
