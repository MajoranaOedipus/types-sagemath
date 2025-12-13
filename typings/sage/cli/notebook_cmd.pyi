import argparse
from _typeshed import Incomplete
from sage.cli.options import CliOptions as CliOptions

class JupyterNotebookCmd:
    @staticmethod
    def extend_parser(parser: argparse.ArgumentParser):
        """
        Extend the parser with the Jupyter notebook command.

        INPUT:

        - ``parsers`` -- the parsers to extend.

        OUTPUT:

        - the extended parser.
        """
    options: Incomplete
    def __init__(self, options: CliOptions) -> None:
        """
        Initialize the command.
        """
    def run(self) -> int:
        """
        Start the Jupyter notebook server.
        """
