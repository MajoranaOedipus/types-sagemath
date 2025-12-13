from _typeshed import Incomplete
from sage.cli.options import CliOptions as CliOptions

class InteractiveShellCmd:
    options: Incomplete
    def __init__(self, options: CliOptions) -> None:
        """
        Initialize the command.
        """
    def run(self) -> int:
        """
        Start the interactive shell.
        """
