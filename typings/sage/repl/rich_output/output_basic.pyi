from _typeshed import Incomplete
from sage.repl.rich_output.buffer import OutputBuffer as OutputBuffer
from sage.structure.sage_object import SageObject as SageObject

class OutputBase(SageObject):
    """
    Base class for all rich output containers.
    """
    @classmethod
    def example(cls) -> None:
        """
        Construct a sample instance.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of the :class:`OutputBase` subclass

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputBase
            sage: OutputBase.example()
            Traceback (most recent call last):
            ...
            NotImplementedError: derived classes must implement this class method
        """

class OutputPlainText(OutputBase):
    text: Incomplete
    def __init__(self, plain_text) -> None:
        """
        Plain Text Output.

        INPUT:

        - ``plain_text`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a bytes (string in Python 2.x) or string (unicode in Python
          2.x) can be passed directly which will then be converted
          into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. The
          plain text output.

        This should always be exactly the same as the (non-rich)
        output from the ``_repr_`` method. Every backend object must
        support plain text output as fallback.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputPlainText
            sage: OutputPlainText('foo')
            OutputPlainText container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample plain text output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputPlainText`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputPlainText
            sage: OutputPlainText.example()
            OutputPlainText container
            sage: OutputPlainText.example().text.get_str()
            'Example plain text output'
        """
    def print_to_stdout(self) -> None:
        """
        Write the data to stdout.

        This is just a convenience method to help with debugging.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: plain_text.print_to_stdout()
            Example plain text output
        """

class OutputAsciiArt(OutputBase):
    ascii_art: Incomplete
    def __init__(self, ascii_art) -> None:
        """
        ASCII Art Output.

        INPUT:

        - ``ascii_art`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Ascii
          art rendered into a string.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputAsciiArt
            sage: OutputAsciiArt(':-}')
            OutputAsciiArt container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample ascii art output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputAsciiArt`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputAsciiArt
            sage: OutputAsciiArt.example()
            OutputAsciiArt container
            sage: OutputAsciiArt.example().ascii_art.get_str()
            '[                        *   *   *    * ]\\n[      **   **   *    *  *   *  *    *  ]\\n[ ***, * , *  , **, ** , *, * , * , *   ]'
        """
    def print_to_stdout(self) -> None:
        """
        Write the data to stdout.

        This is just a convenience method to help with debugging.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputAsciiArt
            sage: ascii_art = OutputAsciiArt.example()
            sage: ascii_art.print_to_stdout()
            [                        *   *   *    * ]
            [      **   **   *    *  *   *  *    *  ]
            [ ***, * , *  , **, ** , *, * , * , *   ]
        """

class OutputUnicodeArt(OutputBase):
    unicode_art: Incomplete
    def __init__(self, unicode_art) -> None:
        """
        Unicode Art Output.

        Similar to :class:`OutputAsciiArt` but using the entire
        unicode range.

        INPUT:

        - ``unicode_art`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (unicode in Python 2.x) can be passed directly
          which will then be converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Unicode
          art rendered into a string.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputUnicodeArt
            sage: OutputUnicodeArt(u':-}')
            OutputUnicodeArt container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample unicode art output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputUnicodeArt`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputUnicodeArt
            sage: OutputUnicodeArt.example()
            OutputUnicodeArt container
            sage: print(OutputUnicodeArt.example().unicode_art.get_unicode())
            ⎛-11   0   1⎞
            ⎜  3  -1   0⎟
            ⎝ -1  -1   0⎠
        """
    def print_to_stdout(self) -> None:
        """
        Write the data to stdout.

        This is just a convenience method to help with debugging.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputUnicodeArt
            sage: unicode_art = OutputUnicodeArt.example()
            sage: unicode_art.print_to_stdout()
            ⎛-11   0   1⎞
            ⎜  3  -1   0⎟
            ⎝ -1  -1   0⎠
        """

class OutputLatex(OutputBase):
    latex: Incomplete
    def __init__(self, latex) -> None:
        """
        LaTeX Output.

        .. NOTE::

            The LaTeX commands will only use a subset of LaTeX that
            can be displayed by MathJax.

        INPUT:

        - ``latex`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively,
          a string (bytes) can be passed directly which will then be
          converted into an
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. String
          containing the latex equation code. Excludes the surrounding
          dollar signs / LaTeX equation environment.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputLatex
            sage: OutputLatex(latex(sqrt(x)))                                           # needs sage.symbolic
            OutputLatex container
        """
    def display_equation(self):
        """
        Return the LaTeX code for a display equation.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputLatex
            sage: rich_output = OutputLatex('1')
            sage: rich_output.latex
            buffer containing 1 bytes
            sage: rich_output.latex.get_str()
            '1'
            sage: rich_output.display_equation()
            '\\\\begin{equation}\\n1\\n\\\\end{equation}'
        """
    def inline_equation(self):
        """
        Return the LaTeX code for an inline equation.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputLatex
            sage: rich_output = OutputLatex('1')
            sage: rich_output.latex
            buffer containing 1 bytes
            sage: rich_output.latex.get_str()
            '1'
            sage: rich_output.inline_equation()
            '\\\\begin{math}\\n1\\n\\\\end{math}'
        """
    @classmethod
    def example(cls):
        """
        Construct a sample LaTeX output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputLatex`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputLatex
            sage: OutputLatex.example()
            OutputLatex container
            sage: OutputLatex.example().latex.get_str()
            '\\\\newcommand{\\\\Bold}[1]{\\\\mathbf{#1}}\\\\int \\\\sin\\\\left(x\\\\right)\\\\,{d x}'
        """
    def print_to_stdout(self) -> None:
        """
        Write the data to stdout.

        This is just a convenience method to help with debugging.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputLatex
            sage: rich_output = OutputLatex.example()
            sage: rich_output.print_to_stdout()
            \\newcommand{\\Bold}[1]{\\mathbf{#1}}\\int \\sin\\left(x\\right)\\,{d x}
        """
