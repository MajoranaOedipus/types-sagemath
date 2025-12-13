from _typeshed import Incomplete

class Sh:
    """
    Evaluates a shell script and returns the output.

    To use this from the notebook type ``sh`` at the beginning of
    the input cell.  The working directory is then the (usually
    temporary) directory where the Sage worksheet process is
    executing.
    """
    def eval(self, code, globals=None, locals=None):
        '''
        This is difficult to test because the output goes to the
        screen rather than being captured by the doctest program, so
        the following really only tests that the command doesn\'t bomb,
        not that it gives the right output::

            sage: sh.eval(\'\'\'echo "Hello there"\\nif [ $? -eq 0 ]; then\\necho "good"\\nfi\'\'\') # random output
        '''

sh: Incomplete
