import argparse
from sage.version import version as version

class VersionCmd:
    @staticmethod
    def extend_parser(parser: argparse.ArgumentParser):
        """
        Extend the parser with the version command.

        INPUT:

        - ``parsers`` -- the parsers to extend.

        OUTPUT:

        - the extended parser.
        """
