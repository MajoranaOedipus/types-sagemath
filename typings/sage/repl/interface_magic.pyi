from _typeshed import Incomplete
from collections.abc import Generator
from sage.repl.rich_output.display_manager import get_display_manager as get_display_manager

LINE_DOCSTRING: str
CELL_DOCSTRING: str

class InterfaceMagic:
    @classmethod
    def all_iter(cls) -> Generator[Incomplete]:
        """
        Iterate over the available interfaces.

        EXAMPLES::

            sage: from sage.repl.interface_magic import InterfaceMagic
            sage: next(InterfaceMagic.all_iter())
            <sage.repl.interface_magic.InterfaceMagic object at 0x...>
        """
    @classmethod
    def register_all(cls, shell=None) -> None:
        """
        Register all available interfaces.

        EXAMPLES::

            sage: class MockShell():
            ....:     magics = set()
            ....:     def register_magic_function(self, fn, magic_name, magic_kind):
            ....:         self.magics.add(magic_name)
            ....:         print(magic_name, magic_kind)
            sage: from sage.repl.interface_magic import InterfaceMagic
            sage: InterfaceMagic.register_all(MockShell())    # random output
            ('gp', 'line')
            ('gp', 'cell')
            ('mwrank', 'line')
            ('mwrank', 'cell')
            ...
            ('maxima', 'line')
            ('maxima', 'cell')
            sage: 'gap' in MockShell.magics                                             # needs sage.libs.gap
            True
            sage: 'maxima' in MockShell.magics                                          # needs sage.symbolic
            True
        """
    @classmethod
    def find(cls, name):
        """
        Find a particular magic by name.

        This method is for doctesting purposes only.

        INPUT:

        - ``name`` -- string; the name of the interface magic to search for

        OUTPUT: the corresponding :class:`InterfaceMagic` instance

        EXAMPLES::

            sage: from sage.repl.interface_magic import InterfaceMagic
            sage: InterfaceMagic.find('gap')                                            # needs sage.libs.gap
            <sage.repl.interface_magic.InterfaceMagic object at 0x...>
        """
    def __init__(self, name, interface) -> None:
        """
        Interface Magic.

        This class is a wrapper around interface objects to provide
        them with magics.

        INPUT:

        - ``name`` -- string; the interface name

        - ``interface`` -- :class:`sage.interfaces.expect.Expect`; the
          interface to wrap

        EXAMPLES::

            sage: from sage.repl.interface_magic import InterfaceMagic
            sage: InterfaceMagic.find('gap')                                            # needs sage.libs.gap
            <sage.repl.interface_magic.InterfaceMagic object at 0x...>
        """
    def line_magic_factory(self):
        """
        Factory for line magic.

        OUTPUT: a function suitable to be used as line magic

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: from sage.repl.interface_magic import InterfaceMagic
            sage: line_magic = InterfaceMagic.find('gap').line_magic_factory()
            sage: output = line_magic('1+1')
            sage: output
            2
            sage: type(output)
            <class 'sage.interfaces.gap.GapElement'>

        This is how the built line magic is used in practice::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell('%gap 1+1')                                            # needs sage.libs.gap
            2
            sage: shell.run_cell('%gap?')                                               # needs sage.libs.gap
            Docstring:
            Interact with gap
            <BLANKLINE>
            The line magic %gap sends a single line to the gap interface.
            ...
        """
    def cell_magic_factory(self):
        '''
        Factory for cell magic.

        OUTPUT: a function suitable to be used as cell magic

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: from sage.repl.interface_magic import InterfaceMagic
            sage: cell_magic = InterfaceMagic.find(\'gap\').cell_magic_factory()
            sage: output = cell_magic(\'\', \'1+1;\')
            2
            sage: output is None
            True
            sage: cell_magic(\'foo\', \'1+1;\')
            Traceback (most recent call last):
            ...
            SyntaxError: Interface magics have no options, got "foo"

        This is how the built cell magic is used in practice::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell(\'%%gap\\nG:=SymmetricGroup(5);\\n1+1;Order(G);\')         # needs sage.libs.gap
            Sym( [ 1 .. 5 ] )
            2
            120
            sage: shell.run_cell(\'%%gap foo\\n1+1;\\n\')                                   # needs sage.libs.gap
            ...File...<string>...
            SyntaxError: Interface magics have no options, got "foo"
            <BLANKLINE>
            sage: shell.run_cell(\'%%gap?\')                                              # needs sage.libs.gap
            Docstring:
            Interact with gap
            <BLANKLINE>
            The cell magic %%gap sends multiple lines to the gap interface.
            ...
        '''
