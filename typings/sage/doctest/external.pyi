from _typeshed import Incomplete
from collections.abc import Generator

Array: Incomplete
prefix: str

def has_internet() -> bool:
    '''
    Test if Internet is available.

    Failure of connecting to the site "https://www.sagemath.org" within a second
    is regarded as internet being not available.

    EXAMPLES::

        sage: from sage.doctest.external import has_internet
        sage: has_internet()  # random, optional -- internet
        FeatureTestResult(\'internet\', True)
    '''
def has_latex() -> bool:
    """
    Test if Latex is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_latex
        sage: has_latex() # optional - latex
        FeatureTestResult('latex', True)
    """
def has_xelatex() -> bool:
    """
    Test if xelatex is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_xelatex
        sage: has_xelatex()   # optional - xelatex
        FeatureTestResult('xelatex', True)
    """
def has_pdflatex() -> bool:
    """
    Test if pdflatex is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_pdflatex
        sage: has_pdflatex()   # optional - pdflatex
        FeatureTestResult('pdflatex', True)
    """
def has_lualatex() -> bool:
    """
    Test if lualatex is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_lualatex
        sage: has_lualatex()   # optional - lualatex
        FeatureTestResult('lualatex', True)
    """
def has_magma() -> bool:
    """
    Test if Magma is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_magma
        sage: has_magma() # random, optional - magma
        True
    """
def has_matlab() -> bool:
    """
    Test if Matlab is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_matlab
        sage: has_matlab() # random, optional - matlab
        True
    """
def has_mathematica() -> bool:
    """
    Test if Mathematica is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_mathematica
        sage: has_mathematica() # random, optional - mathematica
        True
    """
def has_maple() -> bool:
    """
    Test if Maple is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_maple
        sage: has_maple() # random, optional - maple
        True
    """
def has_macaulay2() -> bool:
    """
    Test if Macaulay2 is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_macaulay2
        sage: has_macaulay2() # random, optional - macaulay2
        True
    """
def has_octave() -> bool:
    """
    Test if Octave is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_octave
        sage: has_octave() # random, optional - octave
        True
    """
def has_pandoc() -> bool:
    """
    Test if pandoc is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_pandoc
        sage: has_pandoc()      # optional -- pandoc
        FeatureTestResult('pandoc', True)
    """
def has_scilab() -> bool:
    """
    Test if Scilab is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_scilab
        sage: has_scilab() # random, optional - scilab
        True
    """
def has_cplex() -> bool:
    """
    Test if CPLEX is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_cplex
        sage: has_cplex() # random, optional - CPLEX
        FeatureTestResult('cplex', True)
    """
def has_gurobi() -> bool:
    """
    Test if Gurobi is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_gurobi
        sage: has_gurobi() # random, optional - Gurobi
        FeatureTestResult('gurobi', True)
    """
def has_graphviz() -> bool:
    """
    Test if graphviz (dot, twopi, neato) are available.

    EXAMPLES::

        sage: from sage.doctest.external import has_graphviz
        sage: has_graphviz()   # optional -- graphviz
        FeatureTestResult('graphviz', True)
    """
def has_ffmpeg() -> bool:
    """
    Test if ffmpeg is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_ffmpeg
        sage: has_ffmpeg()      # optional -- ffmpeg
        FeatureTestResult('ffmpeg', True)
    """
def has_imagemagick() -> bool:
    """
    Test if ImageMagick (command magick or convert) is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_imagemagick
        sage: has_imagemagick() # optional -- imagemagick
        FeatureTestResult('imagemagick', True)
    """
def has_dvipng() -> bool:
    """
    Test if dvipng is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_dvipng
        sage: has_dvipng() # optional -- dvipng
        FeatureTestResult('dvipng', True)
    """
def has_pdf2svg() -> bool:
    """
    Test if pdf2svg is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_pdf2svg
        sage: has_pdf2svg() # optional -- pdf2svg
        FeatureTestResult('pdf2svg', True)
    """
def has_rubiks() -> bool:
    """
    Test if the rubiks package (``cu2``, ``cubex``, ``dikcube``,
    ``mcube``, ``optimal``, and ``size222``) is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_rubiks
        sage: has_rubiks()   # optional -- rubiks
        FeatureTestResult('rubiks', True)
    """
def has_4ti2() -> bool:
    """
    Test if the 4ti2 package is available.

    EXAMPLES::

        sage: from sage.doctest.external import has_4ti2
        sage: has_4ti2()   # optional -- 4ti2
        FeatureTestResult('4ti2', True)
    """
def external_features() -> Generator[Incomplete, Incomplete]:
    """
    Generate the features that are only to be tested if ``--optional=external`` is used.

    .. SEEALSO::

        :func:`sage.features.all.all_features`

    EXAMPLES::

        sage: from sage.doctest.external import external_features
        sage: next(external_features())
        Feature('internet')
    """

external_software: list[str]

class AvailableSoftware:
    """
    This class keeps the set of available software whose availability is detected lazily
    from the list of external software.

    EXAMPLES::

        sage: from sage.doctest.external import external_software, available_software
        sage: external_software
        ['cplex',
         'dvips',
         'ffmpeg',
         'gurobi',
         'internet',
         'latex',
         'latex_package_tkz_graph',
         'lualatex',
         'macaulay2',
         'magma',
         'maple',
         'mathematica',
         'matlab',
         'octave',
         'pdflatex',
         'scilab',
         'xelatex']
        sage: 'internet' in available_software # random, optional - internet
        True
        sage: available_software.issuperset(set(['internet','latex'])) # random, optional - internet latex
        True
    """
    def __init__(self) -> None:
        """
        Initialization.

        EXAMPLES::

            sage: from sage.doctest.external import AvailableSoftware
            sage: S = AvailableSoftware()
            sage: S.seen() # random
            []
        """
    def __contains__(self, item) -> bool:
        """
        Return ``True`` if ``item`` is available on the system.

        EXAMPLES::

            sage: from sage.doctest.external import available_software
            sage: 'internet' in available_software # random, optional - internet
            True
        """
    def issuperset(self, other):
        """
        Return ``True`` if ``other`` is a subset of ``self``.

        EXAMPLES::

            sage: from sage.doctest.external import available_software
            sage: available_software.issuperset(set(['internet','latex','magma'])) # random, optional - internet latex magma
            True
        """
    def detectable(self):
        """
        Return the list of names of those features for which testing their presence is allowed.
        """
    def seen(self):
        """
        Return the list of detected external software.

        EXAMPLES::

            sage: from sage.doctest.external import available_software
            sage: available_software.seen() # random
            ['internet', 'latex', 'magma']
        """
    def hidden(self):
        """
        Return the list of detected hidden external software.

        EXAMPLES::

            sage: # needs conway_polynomials database_cremona_mini_ellcurve database_ellcurves database_graphs
            sage: from sage.doctest.external import available_software
            sage: from sage.features.databases import all_features
            sage: for f in all_features():
            ....:    f.hide()
            ....:    if f._spkg_type() == 'standard':
            ....:         test = f.name in available_software
            ....:    f.unhide()
            sage: sorted(available_software.hidden())
            [...'conway_polynomials',...
             'database_cremona_mini_ellcurve',...
             'database_ellcurves',...
             'database_graphs'...]
        """

available_software: Incomplete
