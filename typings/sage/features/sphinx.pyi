from . import PythonModule as PythonModule

class Sphinx(PythonModule):
    """
    A :class:`sage.features.Feature` describing the presence of :ref:`Sphinx <spkg_sphinx>`.

    Sphinx is provided by a standard package in the Sage distribution,
    but it can be disabled by ``configure --disable-doc``.

    EXAMPLES::

        sage: from sage.features.sphinx import Sphinx
        sage: Sphinx().is_present()                     # optional - sphinx
        FeatureTestResult('sphinx', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sphinx import Sphinx
            sage: isinstance(Sphinx(), Sphinx)
            True
        """

class JupyterSphinx(PythonModule):
    """
    A :class:`sage.features.Feature` describing the presence of
    :ref:`jupyter_sphinx <spkg_jupyter_sphinx>`.

    It is provided by a standard package in the Sage distribution,
    but it can be disabled by ``configure --disable-doc`` and
    ``configure --disable-notebook``.

    EXAMPLES::

        sage: from sage.features.sphinx import JupyterSphinx
        sage: JupyterSphinx().is_present()                      # optional - jupyter_sphinx
        FeatureTestResult('jupyter_sphinx', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sphinx import JupyterSphinx
            sage: isinstance(JupyterSphinx(), JupyterSphinx)
            True
        """

def all_features(): ...
