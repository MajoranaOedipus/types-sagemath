import doctest
from .parsing import SageDocTestParser as SageDocTestParser
from .util import NestedName as NestedName
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import SAGE_LIB as SAGE_LIB, SAGE_SRC as SAGE_SRC
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.package_dir import is_package_or_sage_namespace_package_dir as is_package_or_sage_namespace_package_dir
from sage.repl.load import load as load
from sage.structure.dynamic_class import dynamic_class as dynamic_class

triple_quotes: Incomplete
name_regex: Incomplete
begin_verb: Incomplete
end_verb: Incomplete
begin_lstli: Incomplete
end_lstli: Incomplete
skip: Incomplete
link_all: Incomplete
double_colon: Incomplete
code_block: Incomplete
whitespace: Incomplete
bitness_marker: Incomplete
bitness_value: Incomplete
find_prompt: Incomplete
sagestart: Incomplete
untested: Incomplete
pep_0263: Incomplete
doctest_line_number: Incomplete

def get_basename(path):
    """
    This function returns the basename of the given path, e.g.
    ``sage.doctest.sources`` or ``doc.ru.tutorial.tour_advanced``.

    EXAMPLES::

        sage: from sage.doctest.sources import get_basename
        sage: import os
        sage: get_basename(sage.doctest.sources.__file__)
        'sage.doctest.sources'

    ::

        sage: # optional - !meson_editable
        sage: get_basename(os.path.join(sage.structure.__path__[0], 'element.pxd'))
        'sage.structure.element.pxd'

    TESTS::

        sage: # optional - meson_editable
        sage: get_basename(os.path.join(os.path.dirname(sage.structure.__file__), 'element.pxd'))
        'sage.structure.element.pxd'
    """

class DocTestSource:
    """
    This class provides a common base class for different sources of doctests.

    INPUT:

    - ``options`` -- a :class:`sage.doctest.control.DocTestDefaults`
      instance or equivalent
    """
    options: Incomplete
    def __init__(self, options) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = sage.doctest.sources.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: TestSuite(FDS).run()
        """
    def __eq__(self, other):
        """
        Comparison is just by comparison of attributes.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = sage.doctest.sources.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: FDS2 = FileDocTestSource(filename, DD)
            sage: FDS == FDS2
            True
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = sage.doctest.sources.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: FDS2 = FileDocTestSource(filename, DD)
            sage: FDS != FDS2
            False
        """
    @lazy_attribute
    def file_optional_tags(self):
        '''
        Return the set of tags that should apply to all doctests in this source.

        This default implementation just returns the empty set.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import StringDocTestSource, PythonSource
            sage: from sage.structure.dynamic_class import dynamic_class
            sage: s = "\'\'\'\\n    sage: 2 + 2\\n    4\\n\'\'\'"
            sage: PythonStringSource = dynamic_class(\'PythonStringSource\', (StringDocTestSource, PythonSource))
            sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
            sage: PSS.file_optional_tags
            set()
        '''

class StringDocTestSource(DocTestSource):
    '''
    This class creates doctests from a string.

    INPUT:

    - ``basename`` -- string such as \'sage.doctests.sources\', going
      into the names of created doctests and examples

    - ``source`` -- string, giving the source code to be parsed for
      doctests

    - ``options`` -- a :class:`sage.doctest.control.DocTestDefaults`
      or equivalent

    - ``printpath`` -- string, to be used in place of a filename
      when doctest failures are displayed

    - ``lineno_shift`` -- integer (default: 0) by which to shift
      the line numbers of all doctests defined in this string

    EXAMPLES::

        sage: from sage.doctest.control import DocTestDefaults
        sage: from sage.doctest.sources import StringDocTestSource, PythonSource
        sage: from sage.structure.dynamic_class import dynamic_class
        sage: s = "\'\'\'\\n    sage: 2 + 2\\n    4\\n\'\'\'"
        sage: PythonStringSource = dynamic_class(\'PythonStringSource\',(StringDocTestSource, PythonSource))
        sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
        sage: dt, extras = PSS.create_doctests({})
        sage: len(dt)
        1
        sage: extras[\'tab\']
        []
        sage: extras[\'line_number\']
        False

        sage: s = "\'\'\'\\n\\tsage: 2 + 2\\n\\t4\\n\'\'\'"
        sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
        sage: dt, extras = PSS.create_doctests({})
        sage: extras[\'tab\']
        [\'2\', \'3\']

        sage: s = "\'\'\'\\n    sage: import warnings; warnings.warn(\'foo\')\\n    doctest:1: UserWarning: foo \\n\'\'\'"
        sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
        sage: dt, extras = PSS.create_doctests({})
        sage: extras[\'line_number\']
        True
    '''
    qualified_name: Incomplete
    printpath: Incomplete
    source: Incomplete
    lineno_shift: Incomplete
    def __init__(self, basename, source, options, printpath, lineno_shift: int = 0) -> None:
        '''
        Initialization.

        TESTS::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import StringDocTestSource, PythonSource
            sage: from sage.structure.dynamic_class import dynamic_class
            sage: s = "\'\'\'\\n    sage: 2 + 2\\n    4\\n\'\'\'"
            sage: PythonStringSource = dynamic_class(\'PythonStringSource\',(StringDocTestSource, PythonSource))
            sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
            sage: TestSuite(PSS).run()
        '''
    def __iter__(self):
        '''
        Iterating over this source yields pairs ``(lineno, line)``.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import StringDocTestSource, PythonSource
            sage: from sage.structure.dynamic_class import dynamic_class
            sage: s = "\'\'\'\\n    sage: 2 + 2\\n    4\\n\'\'\'"
            sage: PythonStringSource = dynamic_class(\'PythonStringSource\',(StringDocTestSource, PythonSource))
            sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
            sage: for n, line in PSS:
            ....:     print("{} {}".format(n, line))
            0 \'\'\'
            1     sage: 2 + 2
            2     4
            3 \'\'\'
        '''
    def create_doctests(self, namespace) -> tuple[list[doctest.DocTest], dict]:
        '''
        Create doctests from this string.

        INPUT:

        - ``namespace`` -- dictionary or :class:`sage.doctest.util.RecordingDict`

        OUTPUT:

        - ``doctests`` -- list of doctests defined by this string

        - ``extras`` -- dictionary with ``extras[\'tab\']`` either
          ``False`` or a list of linenumbers on which tabs appear

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import StringDocTestSource, PythonSource
            sage: from sage.structure.dynamic_class import dynamic_class
            sage: s = "\'\'\'\\n    sage: 2 + 2\\n    4\\n\'\'\'"
            sage: PythonStringSource = dynamic_class(\'PythonStringSource\',(StringDocTestSource, PythonSource))
            sage: PSS = PythonStringSource(\'<runtime>\', s, DocTestDefaults(), \'runtime\')
            sage: dt, extras = PSS.create_doctests({})
            sage: for t in dt:
            ....:     print("{} {}".format(t.name, t.examples[0].sage_source))
            <runtime> 2 + 2
            sage: extras
            {...\'tab\': []...}
        '''

class FileDocTestSource(DocTestSource):
    """
    This class creates doctests from a file.

    INPUT:

    - ``path`` -- string; the filename

    - ``options`` -- a :class:`sage.doctest.control.DocTestDefaults`
      instance or equivalent

    EXAMPLES::

        sage: from sage.doctest.control import DocTestDefaults
        sage: from sage.doctest.sources import FileDocTestSource
        sage: filename = sage.doctest.sources.__file__
        sage: FDS = FileDocTestSource(filename, DocTestDefaults())
        sage: FDS.basename
        'sage.doctest.sources'

    TESTS::

        sage: TestSuite(FDS).run()

    ::

        sage: from sage.doctest.control import DocTestDefaults
        sage: from sage.doctest.sources import FileDocTestSource
        sage: filename = tmp_filename(ext='.txtt')
        sage: FDS = FileDocTestSource(filename, DocTestDefaults())
        Traceback (most recent call last):
        ...
        ValueError: unknown extension for the file to test (=...txtt),
        valid extensions are: .py, .pyx, .pxd, .pxi, .sage, .spyx, .tex, .rst, .rst.txt
    """
    path: Incomplete
    __class__: Incomplete
    encoding: str
    def __init__(self, path, options) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = sage.doctest.sources.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults(randorder=0))
            sage: FDS.options.randorder
            0
        """
    def __iter__(self):
        '''
        Iterating over this source yields pairs ``(lineno, line)``.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = tmp_filename(ext=\'.py\')
            sage: s = "\'\'\'\\n    sage: 2 + 2\\n    4\\n\'\'\'"
            sage: with open(filename, \'w\') as f:
            ....:     _ = f.write(s)
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: for n, line in FDS:
            ....:     print("{} {}".format(n, line))
            0 \'\'\'
            1     sage: 2 + 2
            2     4
            3 \'\'\'

        The encoding is "utf-8" by default::

            sage: FDS.encoding
            \'utf-8\'

        We create a file with a Latin-1 encoding without declaring it::

            sage: s = b"\'\'\'\\nRegardons le polyn\\xF4me...\\n\'\'\'\\n"
            sage: with open(filename, \'wb\') as f:
            ....:     _ = f.write(s)
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: L = list(FDS)
            Traceback (most recent call last):
            ...
            UnicodeDecodeError: \'utf...8\' codec can...t decode byte 0xf4 in position 18: invalid continuation byte

        This works if we add a PEP 0263 encoding declaration::

            sage: s = b"#!/usr/bin/env python\\n# -*- coding: latin-1 -*-\\n" + s
            sage: with open(filename, \'wb\') as f:
            ....:     _ = f.write(s)
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: L = list(FDS)
            sage: FDS.encoding
            \'latin-1\'
        '''
    @lazy_attribute
    def printpath(self):
        """
        Whether the path is printed absolutely or relatively depends on an option.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: import os
            sage: filename = os.path.realpath(sage.doctest.sources.__file__)
            sage: root = os.path.join(os.path.dirname(filename), '..')
            sage: cwd = os.getcwd()
            sage: os.chdir(root)
            sage: FDS = FileDocTestSource(filename, DocTestDefaults(randorder=0,
            ....:                                                   abspath=False))
            sage: FDS.printpath
            'doctest/sources.py'
            sage: FDS = FileDocTestSource(filename, DocTestDefaults(randorder=0,
            ....:                                                   abspath=True))
            sage: FDS.printpath
            '.../sage/doctest/sources.py'
            sage: os.chdir(cwd)
        """
    @lazy_attribute
    def basename(self):
        """
        The basename of this file source, e.g. ``sage.doctest.sources``.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = os.path.join(SAGE_SRC,'sage','rings','integer.pyx')
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS.basename
            'sage.rings.integer'
        """
    @lazy_attribute
    def in_lib(self):
        '''
        Whether this file is to be treated as a module in a Python package.

        Such files aren\'t loaded before running tests.

        This uses :func:`~sage.misc.package_dir.is_package_or_sage_namespace_package_dir`
        but can be overridden via :class:`~sage.doctest.control.DocTestDefaults`.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: import os
            sage: filename = os.path.join(SAGE_SRC, \'sage\', \'rings\', \'integer.pyx\')
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS.in_lib
            True
            sage: filename = os.path.join(SAGE_SRC, \'sage\', \'doctest\', \'tests\', \'abort.rst\')
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS.in_lib
            False

        You can override the default::

            sage: FDS = FileDocTestSource("hello_world.py", DocTestDefaults())
            sage: FDS.in_lib
            False
            sage: FDS = FileDocTestSource("hello_world.py", DocTestDefaults(force_lib=True))
            sage: FDS.in_lib
            True
        '''
    @lazy_attribute
    def file_optional_tags(self):
        """
        Return the set of tags that should apply to all doctests in this source.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = sage.repl.user_globals.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS.file_optional_tags
            {'sage.modules': None}
        """
    qualified_name: Incomplete
    def create_doctests(self, namespace) -> tuple[list[doctest.DocTest], dict]:
        """
        Return a list of doctests for this file.

        INPUT:

        - ``namespace`` -- dictionary or :class:`sage.doctest.util.RecordingDict`

        OUTPUT:

        - ``doctests`` -- list of doctests defined in this file

        - ``extras`` -- dictionary

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = sage.doctest.sources.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: len(doctests)
            43
            sage: extras['tab']
            False

        We give a self referential example::

            sage: doctests[20].name
            'sage.doctest.sources.FileDocTestSource.create_doctests'
            sage: doctests[20].examples[8].source
            'doctests[Integer(20)].examples[Integer(8)].source\\n'

        TESTS:

        We check that we correctly process results that depend on 32
        vs 64 bit architecture::

            sage: import sys
            sage: bitness = '64' if sys.maxsize > (1 << 32) else '32'
            sage: sys.maxsize == 2^63 - 1
            False # 32-bit
            True  # 64-bit
            sage: ex = doctests[20].examples[11]
            sage: ((bitness == '64' and ex.want == 'True  \\n')
            ....:  or (bitness == '32' and ex.want == 'False \\n'))
            True

        We check that lines starting with a # aren't doctested::

            #sage: raise RuntimeError
        """

class SourceLanguage:
    """
    An abstract class for functions that depend on the programming language of a doctest source.

    Currently supported languages include Python, ReST and LaTeX.
    """
    def parse_docstring(self, docstring, namespace, start) -> list[doctest.DocTest]:
        """
        Return a list of doctest defined in this docstring.

        This function is called by :meth:`DocTestSource._process_doc`.
        The default implementation, defined here, is to use the
        :class:`sage.doctest.parsing.SageDocTestParser` attached to
        this source to get doctests from the docstring.

        INPUT:

        - ``docstring`` -- string containing documentation and tests

        - ``namespace`` -- dictionary or :class:`sage.doctest.util.RecordingDict`

        - ``start`` -- integer; one less than the starting line number

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.parsing import SageDocTestParser
            sage: from sage.doctest.util import NestedName
            sage: filename = sage.doctest.util.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: doctests, _ = FDS.create_doctests({})
            sage: for dt in doctests:
            ....:     FDS.qualified_name = dt.name
            ....:     dt.examples = dt.examples[:-1] # strip off the sig_on() test
            ....:     assert(FDS.parse_docstring(dt.docstring,{},dt.lineno-1)[0] == dt)
        """

class PythonSource(SourceLanguage):
    """
    This class defines the functions needed for the extraction of doctests from python sources.

    EXAMPLES::

        sage: from sage.doctest.control import DocTestDefaults
        sage: from sage.doctest.sources import FileDocTestSource
        sage: filename = sage.doctest.sources.__file__
        sage: FDS = FileDocTestSource(filename, DocTestDefaults())
        sage: type(FDS)
        <class 'sage.doctest.sources.PythonFileSource'>
    """
    start_finish_can_overlap: bool
    code_wrapping: Incomplete
    def starting_docstring(self, line):
        '''
        Determines whether the input line starts a docstring.

        If the input line does start a docstring (a triple quote),
        then this function updates ``self.qualified_name``.

        INPUT:

        - ``line`` -- string; one line of an input file

        OUTPUT: either ``None`` or a Match object

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.util import NestedName
            sage: filename = sage.doctest.sources.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS._init()
            sage: FDS.starting_docstring("r\'\'\'")
            <...Match object...>
            sage: FDS.ending_docstring("\'\'\'")
            <...Match object...>
            sage: FDS.qualified_name = NestedName(FDS.basename)
            sage: FDS.starting_docstring("class MyClass():")
            sage: FDS.starting_docstring("    def hello_world(self):")
            sage: FDS.starting_docstring("        \'\'\'")
            <...Match object...>
            sage: FDS.qualified_name
            sage.doctest.sources.MyClass.hello_world
            sage: FDS.ending_docstring("    \'\'\'")
            <...Match object...>
            sage: FDS.starting_docstring("class NewClass():")
            sage: FDS.starting_docstring("    \'\'\'")
            <...Match object...>
            sage: FDS.ending_docstring("    \'\'\'")
            <...Match object...>
            sage: FDS.qualified_name
            sage.doctest.sources.NewClass
            sage: FDS.starting_docstring("print(")
            sage: FDS.starting_docstring("    \'\'\'Not a docstring")
            sage: FDS.starting_docstring("    \'\'\')")
            sage: FDS.starting_docstring("def foo():")
            sage: FDS.starting_docstring("    \'\'\'This is a docstring\'\'\'")
            <...Match object...>
        '''
    def ending_docstring(self, line):
        '''
        Determines whether the input line ends a docstring.

        INPUT:

        - ``line`` -- string, one line of an input file

        OUTPUT: an object that, when evaluated in a boolean context, gives
        ``True`` or ``False`` depending on whether the input line marks the
        end of a docstring

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.util import NestedName
            sage: filename = sage.doctest.sources.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS._init()
            sage: FDS.quotetype = "\'\'\'"
            sage: FDS.ending_docstring("\'\'\'")
            <...Match object...>
            sage: FDS.ending_docstring(\'\\"\\"\\"\')
        '''

class TexSource(SourceLanguage):
    '''
    This class defines the functions needed for the extraction of
    doctests from a LaTeX source.

    EXAMPLES::

        sage: from sage.doctest.control import DocTestDefaults
        sage: from sage.doctest.sources import FileDocTestSource
        sage: filename = "sage_paper.tex"
        sage: FDS = FileDocTestSource(filename, DocTestDefaults())
        sage: type(FDS)
        <class \'sage.doctest.sources.TexFileSource\'>
    '''
    start_finish_can_overlap: bool
    skipping: bool
    def starting_docstring(self, line):
        '''
        Determines whether the input line starts a docstring.

        Docstring blocks in tex files are defined by verbatim or
        lstlisting environments, and can be linked together by adding
        %link immediately after the \\end{verbatim} or \\end{lstlisting}.

        Within a verbatim (or lstlisting) block, you can tell Sage not to
        process the rest of the block by including a %skip line.

        INPUT:

        - ``line`` -- string, one line of an input file

        OUTPUT: boolean; whether the input line marks the start of a docstring
        (verbatim block)

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = "sage_paper.tex"
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS._init()

        We start docstrings with \\begin{verbatim} or \\begin{lstlisting}::

            sage: FDS.starting_docstring(r"\\begin{verbatim}")
            True
            sage: FDS.starting_docstring(r"\\begin{lstlisting}")
            True
            sage: FDS.skipping
            False
            sage: FDS.ending_docstring("sage: 2+2")
            False
            sage: FDS.ending_docstring("4")
            False

        To start ignoring the rest of the verbatim block, use %skip::

            sage: FDS.ending_docstring("%skip")
            True
            sage: FDS.skipping
            True
            sage: FDS.starting_docstring("sage: raise RuntimeError")
            False

        You can even pretend to start another verbatim block while skipping::

            sage: FDS.starting_docstring(r"\\begin{verbatim}")
            False
            sage: FDS.skipping
            True

        To stop skipping end the verbatim block::

            sage: FDS.starting_docstring(r"\\end{verbatim} %link")
            False
            sage: FDS.skipping
            False

        Linking works even when the block was ended while skipping::

            sage: FDS.linking
            True
            sage: FDS.starting_docstring(r"\\begin{verbatim}")
            True
        '''
    linking: bool
    def ending_docstring(self, line, check_skip: bool = True):
        '''
        Determines whether the input line ends a docstring.

        Docstring blocks in tex files are defined by verbatim or
        lstlisting environments, and can be linked together by adding
        %link immediately after the \\end{verbatim} or \\end{lstlisting}.

        Within a verbatim (or lstlisting) block, you can tell Sage not to
        process the rest of the block by including a %skip line.

        INPUT:

        - ``line`` -- string, one line of an input file

        - ``check_skip`` -- boolean (default: ``True``); used internally in
          ``starting_docstring``

        OUTPUT: boolean; whether the input line marks the end of a docstring
        (verbatim block)

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = "sage_paper.tex"
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS._init()
            sage: FDS.ending_docstring(r"\\end{verbatim}")
            True
            sage: FDS.ending_docstring(r"\\end{lstlisting}")
            True
            sage: FDS.linking
            False

        Use %link to link with the next verbatim block::

            sage: FDS.ending_docstring(r"\\end{verbatim}%link")
            True
            sage: FDS.linking
            True

        %skip also ends a docstring block::

            sage: FDS.ending_docstring("%skip")
            True
        '''

class RestSource(SourceLanguage):
    '''
    This class defines the functions needed for the extraction of
    doctests from ReST sources.

    EXAMPLES::

        sage: from sage.doctest.control import DocTestDefaults
        sage: from sage.doctest.sources import FileDocTestSource
        sage: filename = "sage_doc.rst"
        sage: FDS = FileDocTestSource(filename, DocTestDefaults())
        sage: type(FDS)
        <class \'sage.doctest.sources.RestFileSource\'>
    '''
    start_finish_can_overlap: bool
    link_all: bool
    skipping: bool
    linking: Incomplete
    first_line: bool
    def starting_docstring(self, line):
        '''
        A line ending with a double colon starts a verbatim block in a ReST file,
        as does a line containing ``.. CODE-BLOCK:: language``.

        This function also determines whether the docstring block
        should be joined with the previous one, or should be skipped.

        INPUT:

        - ``line`` -- string; one line of an input file

        OUTPUT: either ``None`` or a Match object

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = "sage_doc.rst"
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS._init()
            sage: FDS.starting_docstring("Hello world::")
            True
            sage: FDS.ending_docstring("    sage: 2 + 2")
            False
            sage: FDS.ending_docstring("    4")
            False
            sage: FDS.ending_docstring("We are now done")
            True
            sage: FDS.starting_docstring(".. link")
            sage: FDS.starting_docstring("::")
            True
            sage: FDS.linking
            True
        '''
    last_indent: Incomplete
    def ending_docstring(self, line):
        '''
        When the indentation level drops below the initial level the
        block ends.

        INPUT:

        - ``line`` -- string; one line of an input file

        OUTPUT: boolean; whether the verbatim block is ending

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: filename = "sage_doc.rst"
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS._init()
            sage: FDS.starting_docstring("Hello world::")
            True
            sage: FDS.ending_docstring("    sage: 2 + 2")
            False
            sage: FDS.ending_docstring("    4")
            False
            sage: FDS.ending_docstring("We are now done")
            True
        '''
    def parse_docstring(self, docstring, namespace, start):
        '''
        Return a list of doctest defined in this docstring.

        Code blocks in a REST file can contain python functions with
        their own docstrings in addition to in-line doctests.  We want
        to include the tests from these inner docstrings, but Python\'s
        doctesting module has a problem if we just pass on the whole
        block, since it expects to get just a docstring, not the
        Python code as well.

        Our solution is to create a new doctest source from this code
        block and append the doctests created from that source.  We
        then replace the occurrences of "sage:" and ">>>" occurring
        inside a triple quote with "safe:" so that the doctest module
        doesn\'t treat them as tests.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.parsing import SageDocTestParser
            sage: from sage.doctest.util import NestedName
            sage: filename = "sage_doc.rst"
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: FDS.parser = SageDocTestParser(set([\'sage\']))
            sage: FDS.qualified_name = NestedName(\'sage_doc\')
            sage: s = "Some text::\\n\\n    def example_python_function(a, \\\n            ....:      b):\\n        \'\'\'\\n        Brief description \\\n            ....:      of function.\\n\\n        EXAMPLES::\\n\\n            \\\n            ....:      sage: test1()\\n            sage: test2()\\n        \\\n            ....:      \'\'\'\\n        return a + b\\n\\n    sage: test3()\\n\\nMore \\\n            ....:      ReST documentation."
            sage: tests = FDS.parse_docstring(s, {}, 100)
            sage: len(tests)
            2
            sage: for ex in tests[0].examples:
            ....:     print(ex.sage_source)
            test3()
            sage: for ex in tests[1].examples:
            ....:     print(ex.sage_source)
            test1()
            test2()
            sig_on_count() # check sig_on/off pairings (virtual doctest)
        '''

class DictAsObject(dict):
    """
    A simple subclass of dict that inserts the items from the initializing dictionary into attributes.

    EXAMPLES::

        sage: from sage.doctest.sources import DictAsObject
        sage: D = DictAsObject({'a':2})
        sage: D.a
        2
    """
    def __init__(self, attrs) -> None:
        """
        Initialization.

        INPUT:

        - ``attrs`` -- dictionary

        EXAMPLES::

            sage: from sage.doctest.sources import DictAsObject
            sage: D = DictAsObject({'a':2})
            sage: D.a == D['a']
            True
            sage: D.a
            2
        """
    def __setitem__(self, ky, val) -> None:
        """
        We preserve the ability to access entries through either the
        dictionary or attribute interfaces.

        EXAMPLES::

            sage: from sage.doctest.sources import DictAsObject
            sage: D = DictAsObject({})
            sage: D['a'] = 2
            sage: D.a
            2
        """
    def __setattr__(self, ky, val) -> None:
        """
        We preserve the ability to access entries through either the
        dictionary or attribute interfaces.

        EXAMPLES::

            sage: from sage.doctest.sources import DictAsObject
            sage: D = DictAsObject({})
            sage: D.a = 2
            sage: D['a']
            2
        """
