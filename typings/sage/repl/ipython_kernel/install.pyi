from _typeshed import Incomplete
from sage.env import SAGE_DOC as SAGE_DOC, SAGE_EXTCODE as SAGE_EXTCODE, SAGE_VENV as SAGE_VENV, SAGE_VERSION as SAGE_VERSION

class SageKernelSpec:
    nbextensions_dir: Incomplete
    kernel_dir: Incomplete
    def __init__(self, prefix=None) -> None:
        """
        Utility to manage SageMath kernels and extensions.

        INPUT:

        - ``prefix`` -- (default: ``sys.prefix``)
          directory for the installation prefix

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: prefix = tmp_dir()
            sage: spec = SageKernelSpec(prefix=prefix)
            sage: spec._display_name    # random output
            'SageMath 6.9'
            sage: spec.kernel_dir == SageKernelSpec(prefix=prefix).kernel_dir
            True
        """
    @classmethod
    def identifier(cls):
        """
        Internal identifier for the SageMath kernel.

        OUTPUT: the string ``'sagemath'``

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: SageKernelSpec.identifier()
            'sagemath'
        """
    def symlink(self, src, dst) -> None:
        """
        Symlink ``src`` to ``dst``.

        This is not an atomic operation.

        Already-existing symlinks will be deleted, already existing
        non-empty directories will be kept.

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: spec = SageKernelSpec(prefix=tmp_dir())
            sage: path = tmp_dir()
            sage: spec.symlink(os.path.join(path, 'a'), os.path.join(path, 'b'))
            sage: os.listdir(path)
            ['b']
        """
    def use_local_threejs(self) -> None:
        """
        Symlink threejs to the Jupyter notebook.

        EXAMPLES::

            sage: # needs threejs
            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: spec = SageKernelSpec(prefix=tmp_dir())
            sage: spec.use_local_threejs()
            sage: threejs = os.path.join(spec.nbextensions_dir, 'threejs-sage')
            sage: os.path.isdir(threejs)
            True
        """
    def kernel_spec(self):
        """
        Return the kernel spec as Python dictionary.

        OUTPUT: a dictionary; see the Jupyter documentation for details

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: spec = SageKernelSpec(prefix=tmp_dir())
            sage: spec.kernel_spec()
            {'argv': ..., 'display_name': 'SageMath ...', 'language': 'sage'}
        """
    @classmethod
    def update(cls, *args, **kwds) -> None:
        """
        Configure the Jupyter notebook for the SageMath kernel.

        This method does everything necessary to use the SageMath kernel,
        you should never need to call any of the other methods
        directly.

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: SageKernelSpec.update(prefix=tmp_dir())
        """
    @classmethod
    def check(cls) -> None:
        """
        Check that the SageMath kernel can be discovered by its name (sagemath).

        This method issues a warning if it cannot -- either because it is not installed,
        or it is shadowed by a different kernel of this name, or Jupyter is
        misconfigured in a different way.

        EXAMPLES::

            sage: from sage.repl.ipython_kernel.install import SageKernelSpec
            sage: SageKernelSpec.check()  # random
        """

def have_prerequisites(debug: bool = True) -> bool:
    """
    Check that we have all prerequisites to run the Jupyter notebook.

    In particular, the Jupyter notebook requires OpenSSL whether or
    not you are using https. See :issue:`17318`.

    INPUT:

    - ``debug`` -- boolean (default: ``True``); whether to print debug
      information in case that prerequisites are missing

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.repl.ipython_kernel.install import have_prerequisites
        sage: have_prerequisites(debug=False) in [True, False]
        True
    """
