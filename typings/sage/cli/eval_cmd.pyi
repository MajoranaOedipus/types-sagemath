import argparse
from _typeshed import Incomplete
from sage.all import sage_globals as sage_globals
from sage.cli.options import CliOptions as CliOptions
from sage.repl.preparse import preparse as preparse

class EvalCmd:
    @staticmethod
    def extend_parser(parser: argparse.ArgumentParser):
        '''
        Extend the parser with the "run" command.

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
