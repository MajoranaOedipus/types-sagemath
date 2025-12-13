import argparse
from _typeshed import Incomplete
from sage.all import sage_globals as sage_globals
from sage.cli.options import CliOptions as CliOptions
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.repl.load import load_cython as load_cython
from sage.repl.preparse import preparse_file_named as preparse_file_named

class RunFileCmd:
    @staticmethod
    def extend_parser(parser: argparse.ArgumentParser):
        '''
        Extend the parser with the "run file" command.

        INPUT:

        - ``parsers`` -- the parsers to extend.

        OUTPUT:

        - the extended parser.
        '''
    options: Incomplete
    def __init__(self, options: CliOptions) -> None:
        """
        Initialize the command.
        """
    def run(self) -> int:
        """
        Execute the given command.
        """
