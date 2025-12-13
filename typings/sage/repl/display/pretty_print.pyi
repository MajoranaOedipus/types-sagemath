from IPython.lib.pretty import PrettyPrinter
from _typeshed import Incomplete
from sage.repl.display.fancy_repr import LargeMatrixHelpRepr as LargeMatrixHelpRepr, PlainPythonRepr as PlainPythonRepr, SomeIPythonRepr as SomeIPythonRepr, TallListRepr as TallListRepr

class SagePrettyPrinter(PrettyPrinter):
    DEBUG: bool
    pretty_repr: Incomplete
    def toplevel(self):
        """
        Return whether we are currently at the top level.

        OUTPUT:

        boolean; whether we are currently pretty-printing an object at
        the outermost level (``True``), or whether the object is
        inside a container (``False``).

        EXAMPLES::

            sage: from sage.repl.display.pretty_print import SagePrettyPrinter
            sage: from io import StringIO
            sage: stream = StringIO()
            sage: spp = SagePrettyPrinter(stream, 78, '\\n')
            sage: spp.toplevel()
            True
        """
    stack: Incomplete
    def __init__(self, output, max_width, newline, max_seq_length=None) -> None:
        """
        Pretty print Sage objects for the commandline.

        INPUT:

        See IPython documentation.

        EXAMPLES::

            sage: 123
            123

        IPython pretty printers::

            sage: set({1, 2, 3})
            {1, 2, 3}
            sage: dict(zzz=123, aaa=99, xab=10)    # sorted by keys
            {'aaa': 99, 'xab': 10, 'zzz': 123}

        These are overridden in IPython in a way that we feel is somewhat
        confusing, and we prefer to print them like plain Python which is
        more informative. See :issue:`14466` ::

            sage: 'this is a string'
            'this is a string'
            sage: type(123)
            <class 'sage.rings.integer.Integer'>
            sage: type
            <... 'type'>
            sage: import types
            sage: type('name', (), {})
            <class '__main__.name'>
            sage: types.BuiltinFunctionType
            <class 'builtin_function_or_method'>

            sage: def foo(): pass
            sage: foo
            <function foo at 0x...>
        """
    def pretty(self, obj) -> None:
        '''
        Pretty print ``obj``.

        This is the only method that outside code should invoke.

        INPUT:

        - ``obj`` -- anything

        OUTPUT: string representation for object

        EXAMPLES::

            sage: from sage.repl.display.pretty_print import SagePrettyPrinter
            sage: from io import StringIO
            sage: stream = StringIO()
            sage: SagePrettyPrinter(stream, 78, \'\\n\').pretty([type, 123, \'foo\'])
            sage: stream.getvalue()
            "[<... \'type\'>,"
        '''
