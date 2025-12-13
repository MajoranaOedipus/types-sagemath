from . import Executable as Executable, FeatureNotPresentError as FeatureNotPresentError, FeatureTestResult as FeatureTestResult, StaticFile as StaticFile

latex_url: str
latex_spkg: str

class LaTeX(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``latex``.

    EXAMPLES::

        sage: from sage.features.latex import latex
        sage: latex().is_present()             # optional - latex
        FeatureTestResult('latex', True)
    """
    def __init__(self, name) -> None:
        """
        TESTS::

            sage: from sage.features.latex import latex
            sage: isinstance(latex(), latex)
            True
        """
    def is_functional(self):
        """
        Return whether ``latex`` in the path is functional.

        EXAMPLES::

            sage: from sage.features.latex import latex
            sage: latex().is_functional()             # optional - latex
            FeatureTestResult('latex', True)

        When the feature is not functional, more information on the reason
        can be obtained as follows::

            sage: result = latex().is_functional()    # not tested
            sage: print(result.reason)                # not tested
            Running latex on a sample file
            (with command='latex -interaction=nonstopmode tmp_wmpos8ak.tex')
            returned nonzero exit status='1' with stderr=''
            and stdout='This is pdfTeX,
            ...
            Runaway argument?
            {document
            ! File ended while scanning use of \\end.
            ...
            No pages of output.
            Transcript written on tmp_wmpos8ak.log.'
        """

class latex(LaTeX):
    """
    A :class:`~sage.features.Feature` describing the presence of ``latex``.

    EXAMPLES::

        sage: from sage.features.latex import latex
        sage: latex().is_present()             # optional - latex
        FeatureTestResult('latex', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latex import latex
            sage: isinstance(latex(), latex)
            True
        """

class pdflatex(LaTeX):
    """
    A :class:`~sage.features.Feature` describing the presence of ``pdflatex``.

    EXAMPLES::

        sage: from sage.features.latex import pdflatex
        sage: pdflatex().is_present()             # optional - pdflatex
        FeatureTestResult('pdflatex', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latex import pdflatex
            sage: isinstance(pdflatex(), pdflatex)
            True
        """

class xelatex(LaTeX):
    """
    A :class:`~sage.features.Feature` describing the presence of ``xelatex``.

    EXAMPLES::

        sage: from sage.features.latex import xelatex
        sage: xelatex().is_present()             # optional - xelatex
        FeatureTestResult('xelatex', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latex import xelatex
            sage: isinstance(xelatex(), xelatex)
            True
        """

class lualatex(LaTeX):
    """
    A :class:`~sage.features.Feature` describing the presence of ``lualatex``.

    EXAMPLES::

        sage: from sage.features.latex import lualatex
        sage: lualatex().is_present()             # optional - lualatex
        FeatureTestResult('lualatex', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latex import lualatex
            sage: isinstance(lualatex(), lualatex)
            True
        """

class dvips(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``dvips``.

    EXAMPLES::

        sage: from sage.features.latex import dvips
        sage: dvips().is_present()             # optional - dvips
        FeatureTestResult('dvips', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latex import dvips
            sage: isinstance(dvips(), dvips)
            True
        """

class TeXFile(StaticFile):
    """
    A :class:`sage.features.Feature` describing the presence of a TeX file.

    EXAMPLES::

        sage: from sage.features.latex import TeXFile
        sage: TeXFile('x', 'x.tex').is_present()  # optional - latex
        FeatureTestResult('x', True)
    """
    def __init__(self, name, filename, **kwds) -> None:
        """
        Initialize.

        TESTS::

            sage: from sage.features.latex import TeXFile
            sage: TeXFile('nonexisting', 'xxxxxx-nonexisting-file.tex').is_present()  # optional - latex
            FeatureTestResult('nonexisting', False)
        """
    def absolute_filename(self) -> str:
        """
        The absolute path of the file.

        EXAMPLES::

            sage: from sage.features.latex import TeXFile
            sage: feature = TeXFile('latex_class_article', 'article.cls')
            sage: feature.absolute_filename()  # optional - latex
            '.../latex/base/article.cls'
        """

class LaTeXPackage(TeXFile):
    """
    A :class:`sage.features.Feature` describing the presence of a LaTeX package
    (``.sty`` file).

    EXAMPLES::

        sage: from sage.features.latex import LaTeXPackage
        sage: LaTeXPackage('graphics').is_present()  # optional - latex
        FeatureTestResult('latex_package_graphics', True)
    """
    @staticmethod
    def __classcall__(cls, package_name, **kwds):
        """
        TESTS::

            sage: from sage.features.latex import LaTeXPackage
            sage: LaTeXPackage('graphics') is LaTeXPackage('graphics')
            True
        """

def all_features(): ...
