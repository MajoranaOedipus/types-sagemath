from _typeshed import Incomplete
from sage.repl.rich_output.buffer import OutputBuffer as OutputBuffer
from sage.repl.rich_output.output_basic import OutputBase as OutputBase

latex_re: Incomplete

class OutputHtml(OutputBase):
    html: Incomplete
    latex: Incomplete
    def __init__(self, html) -> None:
        """
        HTML Output.

        INPUT:

        - ``html`` --
          :class:`~sage.repl.rich_output.buffer.OutputBuffer`. Alternatively, a
          string (bytes) can be passed directly which will then be converted
          into an :class:`~sage.repl.rich_output.buffer.OutputBuffer`. String
          containing the html fragment code. Excludes the surrounding
          ``<body>`` and ``<html>`` tag.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputHtml
            sage: OutputHtml('<div>Foo<b>B</b>ar</div>')
            OutputHtml container
        """
    @classmethod
    def example(cls):
        """
        Construct a sample Html output container.

        This static method is meant for doctests, so they can easily
        construct an example.

        OUTPUT: an instance of :class:`OutputHtml`

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputHtml
            sage: OutputHtml.example()
            OutputHtml container
            sage: OutputHtml.example().html.get_str()
            '<div>Hello World!</div>'
        """
    def print_to_stdout(self) -> None:
        """
        Write the data to stdout.

        This is just a convenience method to help with debugging.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputHtml
            sage: rich_output = OutputHtml.example()
            sage: rich_output.print_to_stdout()
            <div>Hello World!</div>
        """
    def with_html_tag(self):
        """
        Return the HTML code surrounded by ``<html>`` tag.

        This is just a convenience method.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_catalog import OutputHtml
            sage: rich_output = OutputHtml.example()
            sage: rich_output.print_to_stdout()
            <div>Hello World!</div>
            sage: rich_output.with_html_tag()
            '<html><div>Hello World!</div></html>'
        """
