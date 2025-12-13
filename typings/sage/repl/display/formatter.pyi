from IPython.core.formatters import DisplayFormatter, PlainTextFormatter
from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.repl.display.pretty_print import SagePrettyPrinter as SagePrettyPrinter

IPYTHON_NATIVE_TYPES: Incomplete
PLAIN_TEXT: str
TEXT_LATEX: str
TEXT_HTML: str

class SageDisplayFormatter(DisplayFormatter):
    dm: Incomplete
    def __init__(self, *args, **kwds) -> None:
        """
        This is where the Sage rich objects are translated to IPython.

        INPUT/OUTPUT: see the IPython documentation

        EXAMPLES:

        This is part of how Sage works with the IPython output
        system. It cannot be used in doctests::

            sage: from sage.repl.display.formatter import SageDisplayFormatter
            sage: fmt = SageDisplayFormatter()
            Traceback (most recent call last):
            ...
            RuntimeError: check failed: current backend is invalid
        """
    def format(self, obj, include=None, exclude=None):
        '''
        Use the Sage rich output instead of IPython.

        INPUT/OUTPUT: see the IPython documentation

        EXAMPLES::

            sage: [identity_matrix(i) for i in range(3,7)]                              # needs sage.modules
            [
                                             [1 0 0 0 0 0]
                                [1 0 0 0 0]  [0 1 0 0 0 0]
                     [1 0 0 0]  [0 1 0 0 0]  [0 0 1 0 0 0]
            [1 0 0]  [0 1 0 0]  [0 0 1 0 0]  [0 0 0 1 0 0]
            [0 1 0]  [0 0 1 0]  [0 0 0 1 0]  [0 0 0 0 1 0]
            [0 0 1], [0 0 0 1], [0 0 0 0 1], [0 0 0 0 0 1]
            ]
            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell(\'%display ascii_art\')   # indirect doctest
            sage: shell.run_cell("i = var(\'i\')")                                        # needs sage.symbolic
            sage: shell.run_cell(\'sum(i*x^i, i, 0, 10)\')                                # needs sage.symbolic
                10      9      8      7      6      5      4      3      2
            10*x   + 9*x  + 8*x  + 7*x  + 6*x  + 5*x  + 4*x  + 3*x  + 2*x  + x
            sage: shell.run_cell(\'%display default\')
            sage: shell.quit()

        TESTS::

            sage: import os
            sage: import importlib.resources
            sage: import warnings
            sage: warnings.filterwarnings(\'ignore\', category=DeprecationWarning,
            ....:     message=r\'path is deprecated\\. Use files\\(\\) instead\\.\')
            sage: from sage.repl.rich_output.backend_ipython import BackendIPython
            sage: backend = BackendIPython()
            sage: shell = get_test_shell()
            sage: backend.install(shell=shell)
            sage: shell.run_cell(\'get_ipython().display_formatter\')
            <sage.repl.display.formatter.SageDisplayFormatter object at 0x...>
            sage: shell.run_cell(\'from IPython.display import Image\')
            sage: with importlib.resources.path(sage.repl.rich_output, \'example.png\') as example_png:
            ....:     shell.run_cell(\'ipython_image = Image("{0}")\'.format(example_png))
            sage: shell.run_cell(\'ipython_image\')
            <IPython.core.display.Image object>
            sage: shell.run_cell(\'get_ipython().display_formatter.format(ipython_image)\')
            ({\'image/png\': ...,
              \'text/plain\': \'<IPython.core.display.Image object>\'},
            {})

        Test that IPython images and widgets still work even in latex output mode::

            sage: shell.run_cell(\'%display latex\')   # indirect doctest
            sage: shell.run_cell(\'set(get_ipython().display_formatter.format(ipython_image)[0].keys())\'
            ....:                \' == set(["text/plain", "image/png"])\')
            True

            sage: shell.run_cell(\'import ipywidgets\')
            sage: shell.run_cell(\'slider = ipywidgets.IntSlider()\')
            sage: shell.run_cell(\'get_ipython().display_formatter.format(slider)\')
            ...IntSlider(value=0)..., {})

            sage: shell.run_cell(\'%display default\')
            sage: shell.quit()

        Test that ``__repr__`` is only called once when generating text output::

            sage: class Repper():
            ....:    def __repr__(self):
            ....:        print(\'__repr__ called\')
            ....:        return \'I am repper\'
            sage: Repper()
            __repr__ called
            I am repper
        '''

class SagePlainTextFormatter(PlainTextFormatter):
    def __init__(self, *args, **kwds) -> None:
        """
        Improved plain text IPython formatter.

        In particular, it correctly print lists of matrices or other
        objects (see
        :meth:`sage.structure.parent.Parent._repr_option`).

        .. warning::

            This IPython formatter is NOT used. You could use it to
            enable Sage formatting in IPython, but Sage uses its own
            rich output system that is more flexible and supports
            different backends.

        INPUT/OUTPUT: see the IPython documentation

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.display_formatter.formatters['text/plain']
            <IPython.core.formatters.PlainTextFormatter object at 0x...>
            sage: shell.quit()
        """
    def __call__(self, obj):
        """
        Compute the pretty representation of the object.

        Adapted from ``IPython.core.formatters.PlainTextPrettyPrint``.

        INPUT:

        - ``obj`` -- anything

        OUTPUT: string; the plain text representation

        EXAMPLES::

            sage: from sage.repl.display.formatter import SagePlainTextFormatter
            sage: fmt = SagePlainTextFormatter()
            sage: fmt
            <sage.repl.display.formatter.SagePlainTextFormatter object at 0x...>
            sage: fmt(2)
            ---- calling ipython formatter ----
            '2'
            sage: a = identity_matrix(ZZ, 2)                                            # needs sage.modules
            sage: fmt([a, a])                                                           # needs sage.modules
            ---- calling ipython formatter ----
            '[\\n[1 0]  [1 0]\\n[0 1], [0 1]\\n]'
        """
