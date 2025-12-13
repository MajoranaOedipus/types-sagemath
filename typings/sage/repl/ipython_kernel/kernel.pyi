from _typeshed import Incomplete
from ipykernel.ipkernel import IPythonKernel
from ipykernel.zmqshell import ZMQInteractiveShell
from sage.env import SAGE_VERSION as SAGE_VERSION
from sage.repl.interpreter import SageNotebookInteractiveShell as SageNotebookInteractiveShell
from sage.repl.ipython_extension import SageJupyterCustomizations as SageJupyterCustomizations

class SageZMQInteractiveShell(SageNotebookInteractiveShell, ZMQInteractiveShell): ...

class SageKernel(IPythonKernel):
    implementation: str
    implementation_version = SAGE_VERSION
    shell_class: Incomplete
    def __init__(self, **kwds) -> None:
        """
        The Sage Jupyter Kernel.

        INPUT:

        See the Jupyter documentation.

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.kernel import SageKernel
            sage: SageKernel.__new__(SageKernel)
            <sage.repl.ipython_kernel.kernel.SageKernel object at 0x...>
        """
    @property
    def banner(self):
        """
        The Sage Banner.

        The value of this property is displayed in the Jupyter
        notebook.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.kernel import SageKernel
            sage: sk = SageKernel.__new__(SageKernel)
            sage: print(sk.banner)
            ┌...SageMath version...
        """
    @property
    def help_links(self):
        """
        Help in the Jupyter Notebook.

        OUTPUT: see the Jupyter documentation

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.kernel import SageKernel
            sage: sk = SageKernel.__new__(SageKernel)
            sage: sk.help_links
            [{'text': 'Sage Documentation',
              'url': '.../html/en/index.html'},
             ...]
        """
    saved_sigint_handler: Incomplete
    def pre_handler_hook(self) -> None:
        """
        Restore the signal handlers to their default values at Sage
        startup, saving the old handler at the ``saved_sigint_handler``
        attribute. This is needed because Jupyter needs to change the
        ``SIGINT`` handler.

        See :issue:`19135`.

        TESTS::

            sage: from sage.repl.ipython_kernel.kernel import SageKernel
            sage: k = SageKernel.__new__(SageKernel)
            sage: k.pre_handler_hook()
            sage: k.saved_sigint_handler
            <cyfunction python_check_interrupt at ...>
        """
