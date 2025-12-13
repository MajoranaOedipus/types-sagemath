from sage.misc.superseded import experimental as experimental
from sage.structure.sage_object import SageObject as SageObject

class Standalone(SageObject):
    '''
    LaTeX standalone document class.

    INPUT:

    - ``content`` -- string; the content to be added in the document
      between lines ``r\'\\begin{document}\'`` and ``r\'\\end{document}\'``
    - ``document_class_options`` -- list of strings (default: ``[]``);
      latex document class standalone options. Such options appear on the
      line ``\\documentclass[...]{standalone}`` between the brackets.
    - ``standalone_config`` -- list of strings (default: ``[]``);
      standalone configuration options. Such options are defined with
      ``\\standaloneconfig{...}``.
    - ``usepackage`` -- list of strings (default: ``[]``); latex packages
    - ``macros`` -- list of strings (default: ``[]``); stuff you need for the picture
    - ``use_sage_preamble`` -- boolean (default: ``False``); whether to include sage
      latex preamble and sage latex macros, that is, the content of
      :func:`sage.misc.latex.extra_preamble()`,
      :func:`sage.misc.latex.extra_macros()` and
      :func:`sage.misc.latex_macros.sage_latex_macros()`

    EXAMPLES::

        sage: from sage.misc.latex_standalone import Standalone
        sage: content = "\\\\section{Intro}\\nTest\\n"
        sage: t = Standalone(content)
        sage: t
        \\documentclass{standalone}
        \\begin{document}
        \\section{Intro}
        Test
        \\end{document}

    ::

        sage: t = Standalone(content, standalone_config=["border=4mm"],
        ....:                usepackage=[\'amsmath\'])
        sage: t
        \\documentclass{standalone}
        \\standaloneconfig{border=4mm}
        \\usepackage{amsmath}
        \\begin{document}
        \\section{Intro}
        Test
        \\end{document}
    '''
    def __init__(self, content, document_class_options=None, standalone_config=None, usepackage=None, macros=None, use_sage_preamble: bool = False) -> None:
        '''
        See :class:`Standalone` for full information.

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: content = "\\\\section{Intro}\\n\\nTest\\n"
            sage: t = Standalone(content)
        '''
    def content(self):
        '''
        Return the content of the standalone document class file.

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: t.content()
            \'Hello World\'

        ::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: print(t.content())
            \\begin{tikzpicture}
            \\draw (0,0) -- (1,1);
            \\end{tikzpicture}
        '''
    def add_document_class_option(self, option) -> None:
        """
        Add a document class option.

        INPUT:

        - ``option`` -- string

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone('Hello World')
            sage: t.add_document_class_option('beamer')
            sage: t
            \\documentclass[beamer]{standalone}
            \\begin{document}
            Hello World
            \\end{document}
        """
    def add_standalone_config(self, config) -> None:
        '''
        Add a standalone config.

        INPUT:

        - ``config`` -- string

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: t.add_standalone_config("border=4mm")
            sage: t
            \\documentclass{standalone}
            \\standaloneconfig{border=4mm}
            \\begin{document}
            Hello World
            \\end{document}
        '''
    def add_usepackage(self, package) -> None:
        """
        Add a ``usepackage`` line.

        INPUT:

        - ``package`` -- string, name of package

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone('Hello World')
            sage: t.add_usepackage('amsmath')
            sage: t
            \\documentclass{standalone}
            \\usepackage{amsmath}
            \\begin{document}
            Hello World
            \\end{document}
        """
    def add_macro(self, macro) -> None:
        """
        Add a macro.

        INPUT:

        - ``macro`` -- string, newcommand line

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone('Hello World')
            sage: t.add_macro(r'\\newcommand{\\ZZ}{\\mathbb{Z}}')
            sage: t
            \\documentclass{standalone}
            \\newcommand{\\ZZ}{\\mathbb{Z}}
            \\begin{document}
            Hello World
            \\end{document}
        """
    def pdf(self, filename=None, view: bool = True, program=None):
        '''
        Compile the latex code with pdflatex and create a pdf file.

        INPUT:

        - ``filename`` -- string (default: ``None``); the output filename.
          If ``None``, it saves the file in a temporary directory.

        - ``view`` -- boolean (default: ``True``); whether to open the file in a
          pdf viewer. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        - ``program`` -- string (default: ``None``); ``\'pdflatex\'`` or
          ``\'lualatex\'``. If ``None``, it uses ``\'lualatex\'`` if it is
          available, otherwise ``\'pdflatex\'``.

        OUTPUT: string, path to pdf file

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: _ = t.pdf(view=False)                 # long time (1s)    # optional - latex

        Same for instances of :class:`TikzPicture`::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: _ = t.pdf(view=False)                 # not tested

        A filename may be provided where to save the file, in which case
        the viewer does not open the file::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(\'temp\',\'.pdf\')
            sage: path_to_file = t.pdf(filename)        # long time (1s)    # optional - latex
            sage: path_to_file[-4:]                     # long time (fast)  # optional - latex
            \'.pdf\'

        The filename may contain spaces::

            sage: filename = tmp_filename(\'filename with spaces\',\'.pdf\')
            sage: path_to_file = t.pdf(filename)        # long time (1s)    # optional - latex

        TESTS:

        We test the behavior when a wrong tex string is provided::

            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: s_missing_last_character = s[:-1]
            sage: t = TikzPicture(s_missing_last_character)
            sage: _ = t.pdf()                                               # optional - latex
            Traceback (most recent call last):
            ...
            CalledProcessError: Command \'[\'...latex\', \'-interaction=nonstopmode\',
            \'tikz_...tex\']\' returned non-zero exit status 1.
        '''
    def dvi(self, filename=None, view: bool = True, program: str = 'latex'):
        '''
        Compile the latex code with latex and create a dvi file.

        INPUT:

        - ``filename`` -- string (default: ``None``); the output filename.
          If ``None``, it saves the file in a temporary directory

        - ``view`` -- boolean (default: ``True``); whether to open the file in a
          dvi viewer. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        - ``program`` -- string (default: ``\'latex\'``); ``\'latex\'``

        OUTPUT: string, path to dvi file

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: _ = t.dvi(view=False)                 # long time (1s)    # optional - latex

        Same for instances of :class:`TikzPicture`::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: _ = t.dvi(view=False)                 # not tested

        A filename may be provided where to save the file, in which case
        the viewer does not open the file::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(\'temp\',\'.dvi\')
            sage: path_to_file = t.dvi(filename)        # long time (1s)    # optional - latex
            sage: path_to_file[-4:]                     # long time (fast)  # optional - latex
            \'.dvi\'

        The filename may contain spaces::

            sage: filename = tmp_filename(\'filename with spaces\',\'.dvi\')
            sage: path_to_file = t.dvi(filename)        # long time (1s)    # optional - latex

        TESTS:

        We test the behavior when a wrong tex string is provided::

            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: s_missing_last_character = s[:-1]
            sage: t = TikzPicture(s_missing_last_character)
            sage: _ = t.dvi()                                               # optional - latex
            Traceback (most recent call last):
            ...
            CalledProcessError: Command \'[\'latex\', \'-interaction=nonstopmode\',
            \'tikz_...tex\']\' returned non-zero exit status 1.

        We test the behavior when a wrong value is provided::

            sage: t = Standalone(\'Hello World\')
            sage: _ = t.dvi(program=\'farniente\')
            Traceback (most recent call last):
            ...
            ValueError: program(=farniente) should be latex
        '''
    def png(self, filename=None, density: int = 150, view: bool = True):
        '''
        Compile the latex code with pdflatex and converts to a png file.

        INPUT:

        - ``filename`` -- string (default: ``None``); the output filename.
          If ``None``, it saves the file in a temporary directory.

        - ``density`` -- integer (default: ``150``); horizontal and vertical
          density of the image

        - ``view`` -- boolean (default: ``True``); whether to open the file in a
          png viewer. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        OUTPUT: string, path to png file

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: _ = t.png(view=False)             # long time (1s)    # optional - latex imagemagick

        Same for instances of :class:`TikzPicture`::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: _ = t.png(view=False)             # not tested

        ::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(\'temp\',\'.png\')
            sage: path_to_file = t.png(filename)    # long time (1s)    # optional - latex imagemagick
            sage: path_to_file[-4:]                 # long time (fast)  # optional - latex imagemagick
            \'.png\'
        '''
    def svg(self, filename=None, view: bool = True, program: str = 'pdftocairo'):
        '''
        Compile the latex code with pdflatex and converts to a svg file.

        INPUT:

        - ``filename`` -- string (default: ``None``); the output filename.
          If ``None``, it saves the file in a temporary directory.

        - ``view`` -- boolean (default: ``True``); whether to open the file in
          a browser. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        - ``program`` -- string (default: ``\'pdftocairo\'``); ``\'pdftocairo\'`` or
          ``\'pdf2svg\'``

        OUTPUT: string, path to svg file

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: _ = t.svg(view=False)     # not tested

        Same for instances of :class:`TikzPicture`::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: _ = t.svg(view=False)     # not tested

        ::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(\'temp\', \'.svg\')
            sage: path_to_file = t.svg(filename,            # long time (1s)    # optional - latex pdf2svg
            ....:                      program=\'pdf2svg\')
            sage: path_to_file[-4:]                         # long time (fast)  # optional - latex pdf2svg
            \'.svg\'
            sage: path_to_file = t.svg(filename,            # long time (1s)    # optional - latex pdftocairo
            ....:                      program=\'pdftocairo\')
            sage: path_to_file[-4:]                         # long time (fast)  # optional - latex pdftocairo
            \'.svg\'
        '''
    def eps(self, filename=None, view: bool = True, program: str = 'dvips'):
        '''
        Compile the latex code with pdflatex and converts to a eps file.

        INPUT:

        - ``filename`` -- string (default: ``None``); the output filename.
          If ``None``, it saves the file in a temporary directory

        - ``view`` -- boolean (default: ``True``); whether to open the file in
          a browser. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        - ``program`` -- string (default: ``\'dvips\'``);
          ``\'pdftocairo\'`` or ``\'dvips\'``

        OUTPUT: string, path to eps file

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: _ = t.eps(view=False)     # not tested

        Same for instances of :class:`TikzPicture`::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: _ = t.eps(view=False)     # not tested

        We test the creation of the files::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(\'temp\', \'.eps\')
            sage: path_to_file = t.eps(filename,            # long time (1s)    # optional - latex dvips
            ....:                      program=\'dvips\')
            sage: path_to_file[-4:]                         # long time (fast)  # optional - latex dvips
            \'.eps\'
            sage: path_to_file = t.eps(filename,            # long time (1s)    # optional - latex pdftocairo
            ....:                      program=\'pdftocairo\')
            sage: path_to_file[-4:]                         # long time (fast)  # optional - latex pdftocairo
            \'.eps\'

        TESTS:

        We test the behavior when a wrong value is provided::

            sage: t = Standalone(\'Hello World\')
            sage: _ = t.eps(program=\'convert\')
            Traceback (most recent call last):
            ...
            ValueError: program(=convert) should be \'pdftocairo\' or \'dvips\'
        '''
    def tex(self, filename=None, content_only: bool = False, include_header=None):
        '''
        Writes the latex code to a file.

        INPUT:

        - ``filename`` -- string (default: ``None``); the output filename.
          If ``None``, it saves the file in a temporary directory.
        - ``content_only`` -- boolean (default: ``False``); whether to include
          the header latex part. If ``True``, it prints only the
          content to the file.

        OUTPUT: string, path to tex file

        EXAMPLES::

            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone(\'Hello World\')
            sage: _ = t.tex()
            sage: _ = t.tex(content_only=True)

        Same for instances of :class:`TikzPicture`::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: _ = t.tex()
            sage: _ = t.tex(content_only=True)

        Write to a given filename::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename(\'temp\',\'.tex\')
            sage: path_to_file = t.tex(filename)
            sage: path_to_file[-4:]
            \'.tex\'
        '''
    def save(self, filename, **kwds) -> None:
        """
        Save the graphics to an image file.

        INPUT:

        - ``filename`` -- string. The filename and the image format
          given by the extension, which can be one of the following:

            * ``.pdf``,
            * ``.png``,
            * ``.svg``,
            * ``.eps``,
            * ``.dvi``,
            * ``.sobj`` (for a Sage object you can load later),
            * empty extension will be treated as ``.sobj``.

        All other keyword arguments will be passed to the plotter.

        OUTPUT: none

        .. NOTE::

            This method follows the signature of the method
            :meth:`sage.plot.Graphics.save` in order to be compatible with
            with sagetex. In particular so that ``\\sageplot{t}`` written
            in a ``tex`` file works when ``t`` is an instance of
            :class:`Standalone` or :class:`TikzPicture`.

        EXAMPLES::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: from sage.misc.latex_standalone import Standalone
            sage: t = Standalone('Hello World')
            sage: filename = tmp_filename('temp','.pdf')
            sage: t.save(filename)                          # long time (1s)    # optional - latex
            sage: filename = tmp_filename('temp','.eps')
            sage: t.save(filename)                          # long time (1s)    # optional - latex dvips
        """

class TikzPicture(Standalone):
    '''
    A TikzPicture embedded in a LaTeX standalone document class.

    INPUT:

    - ``content`` -- string, tikzpicture code starting with ``r\'\\begin{tikzpicture}\'``
      and ending with ``r\'\\end{tikzpicture}\'``
    - ``standalone_config`` -- list of strings (default: ``[]``);
      latex document class standalone configuration options
    - ``usepackage`` -- list of strings (default: ``[]``); latex
      packages
    - ``usetikzlibrary`` -- list of strings (default: ``[]``); tikz libraries
      to use
    - ``macros`` -- list of strings (default: ``[]``); stuff you need for the picture
    - ``use_sage_preamble`` -- boolean (default: ``False``); whether to include sage
      latex preamble and sage latex macros, that is, the content of
      :func:`sage.misc.latex.extra_preamble()`,
      :func:`sage.misc.latex.extra_macros()` and
      :func:`sage.misc.latex_macros.sage_latex_macros()`

    EXAMPLES:

    Create your own tikz string from scratch and provide it::

        sage: from sage.misc.latex_standalone import TikzPicture
        sage: lines = []
        sage: lines.append(r\'\\begin{tikzpicture}\')
        sage: lines.append(r\'\\draw[very thick,orange,->] (0,0) -- (1,1);\')
        sage: lines.append(r\'\\end{tikzpicture}\')
        sage: s = \'\\n\'.join(lines)
        sage: t = TikzPicture(s)
        sage: t
        \\documentclass[tikz]{standalone}
        \\begin{document}
        \\begin{tikzpicture}
        \\draw[very thick,orange,->] (0,0) -- (1,1);
        \\end{tikzpicture}
        \\end{document}

    Then use it by exporting the tikzpicture to other formats, all of the
    below methods return a string providing the path to the filename, which
    is by default in a temporary folder::

        sage: # not tested
        sage: _ = t.pdf()
        sage: _ = t.png()
        sage: _ = t.svg()
        sage: _ = t.tex()
        sage: _ = t.pdf(filename=\'abc.pdf\')

    Here we create a tikzpicture for the latex representation of a graph.
    This is using tkz-graph tex library::

        sage: # needs sage.graphs
        sage: g = graphs.PetersenGraph()
        sage: s = latex(g)                                              # optional - latex
        sage: t = TikzPicture(s, standalone_config=["border=4mm"],      # optional - latex
        ....:                 usepackage=[\'tkz-graph\'])
        sage: _ = t.pdf(view=False)                     # long time (2s), optional - latex latex_package_tkz_graph

    Here are standalone configurations, packages, tikz libraries and macros
    that can be set::

        sage: options = [\'preview\', \'border=4mm\', \'beamer\', \'float\']
        sage: usepackage = [\'nicefrac\', \'amsmath\', \'pifont\', \'tikz-3dplot\',
        ....:    \'pgfplots\']
        sage: tikzlib = [\'arrows\', \'snakes\', \'backgrounds\', \'patterns\',
        ....:      \'matrix\', \'shapes\', \'fit\', \'calc\', \'shadows\', \'plotmarks\',
        ....:      \'positioning\', \'pgfplots.groupplots\', \'mindmap\']
        sage: macros = [r\'\\newcommand{\\ZZ}{\\mathbb{Z}}\']
        sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
        sage: t = TikzPicture(s, standalone_config=options, usepackage=usepackage,
        ....:        usetikzlibrary=tikzlib, macros=macros)
        sage: _ = t.pdf(view=False)                     # long time (2s), optional - latex
    '''
    def __init__(self, content, standalone_config=None, usepackage=None, usetikzlibrary=None, macros=None, use_sage_preamble: bool = False) -> None:
        '''
        See :class:`TikzPicture` for full information.

        EXAMPLES::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
        '''
    def add_usetikzlibrary(self, library) -> None:
        '''
        Add a ``usetikzlibrary`` line.

        INPUT:

        - ``library`` -- string, name of library

        EXAMPLES::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: t.add_usetikzlibrary(\'arrows\')
            sage: t
            \\documentclass[tikz]{standalone}
            \\usetikzlibrary{arrows}
            \\begin{document}
            \\begin{tikzpicture}
            \\draw (0,0) -- (1,1);
            \\end{tikzpicture}
            \\end{document}
        '''
    @classmethod
    def from_dot_string(cls, dotdata, prog: str = 'dot'):
        '''
        Convert a graph to a tikzpicture using graphviz and dot2tex.

        .. NOTE::

            Prerequisite: dot2tex optional Sage package and graphviz must be
            installed.

        INPUT:

        - ``dotdata`` -- dot format string
        - ``prog`` -- string (default: ``\'dot\'``); the program used for the
          layout corresponding to one of the software of the graphviz
          suite: ``\'dot\'``, ``\'neato\'``, ``\'twopi\'``, ``\'circo\'`` or ``\'fdp\'``

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.latex_standalone import TikzPicture
            sage: G = graphs.PetersenGraph()
            sage: dotdata = G.graphviz_string()
            sage: tikz = TikzPicture.from_dot_string(dotdata)   # long time (3s), optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested

        ::

            sage: # needs sage.graphs
            sage: dotdata = G.graphviz_string(labels=\'latex\')
            sage: tikz = TikzPicture.from_dot_string(dotdata)   # long time (3s), optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested

        ::

            sage: # needs sage.combinat sage.graphs sage.groups
            sage: W = CoxeterGroup(["A",2])
            sage: G = W.cayley_graph()
            sage: dotdata = G.graphviz_string()
            sage: tikz = TikzPicture.from_dot_string(dotdata)   # long time (3s), optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested

        ::

            sage: # needs sage.combinat sage.graphs sage.groups
            sage: dotdata = G.graphviz_string(labels=\'latex\')
            sage: tikz = TikzPicture.from_dot_string(dotdata)   # long time (3s), optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested
        '''
    @classmethod
    def from_graph(cls, graph, merge_multiedges: bool = True, merge_label_function=..., **kwds):
        '''
        Convert a graph to a tikzpicture using graphviz and dot2tex.

        .. NOTE::

            Prerequisite: dot2tex optional Sage package and graphviz must be
            installed.

        .. WARNING::

            This method might be deleted in the future in favor of a method
            in the graph class returning a tikz picture.

        INPUT:

        - ``graph`` -- graph
        - ``merge_multiedges`` -- boolean (default: ``True``); if the graph
          has multiple edges, whether to merge the multiedges into one
          single edge
        - ``merge_label_function`` -- function (default: ``tuple``); a
          function to apply to each list of labels to be merged. It is
          ignored if ``merge_multiedges`` is not ``True`` or if the graph
          has no multiple edges.

        Other inputs are used for latex drawing with dot2tex and graphviz:

        - ``prog`` -- string (default: ``\'dot\'``); the program used for the
          layout corresponding to one of the software of the graphviz
          suite: ``\'dot\'``, ``\'neato\'``, ``\'twopi\'``, ``\'circo\'`` or ``\'fdp\'``
        - ``edge_labels`` -- boolean (default: ``True``)
        - ``color_by_label`` -- boolean (default: ``False``)
        - ``rankdir`` -- string (default: ``\'down\'``)
        - ``subgraph_clusters`` -- (default: ``[]``) a list of lists of
          vertices, if supported by the layout engine, nodes belonging to
          the same cluster subgraph are drawn together, with the entire
          drawing of the cluster contained within a bounding rectangle.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: from sage.misc.latex_standalone import TikzPicture
            sage: g = graphs.PetersenGraph()
            sage: tikz = TikzPicture.from_graph(g)                              # optional - dot2tex graphviz
            doctest:...: FutureWarning: This class/method/function is marked as experimental.
            It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/20343 for details.
            sage: _ = tikz.pdf()      # not tested

        Using ``prog``::

            sage: # needs sage.graphs
            sage: tikz = TikzPicture.from_graph(g, prog=\'neato\',        # long time (3s), optional - dot2tex graphviz
            ....:                               color_by_label=True)
            sage: _ = tikz.pdf()      # not tested

        Using ``rankdir``::

            sage: tikz = TikzPicture.from_graph(g, rankdir=\'right\')     # long time (3s), optional - dot2tex graphviz, needs sage.graphs
            sage: _ = tikz.pdf()      # not tested

        Using ``merge_multiedges``::

            sage: # needs sage.graphs sage.modules sage.symbolic
            sage: alpha = var(\'alpha\')
            sage: m = matrix(2, range(4)); m.set_immutable()
            sage: G = DiGraph([(0,1,alpha), (0,1,0), (0,2,9), (0,2,m)],
            ....:             multiedges=True)
            sage: tikz = TikzPicture.from_graph(G, merge_multiedges=True)       # optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested

        Using ``merge_multiedges`` with ``merge_label_function``::

            sage: # needs sage.graphs
            sage: fn = lambda L: LatexExpr(\',\'.join(map(str, L)))
            sage: edges = [(0,1,\'a\'), (0,1,\'b\'), (0,2,\'c\'), (0,2,\'d\')]
            sage: G = DiGraph(edges, multiedges=True)
            sage: tikz = TikzPicture.from_graph(G,                              # optional - dot2tex graphviz
            ....:           merge_multiedges=True, merge_label_function=fn)
            sage: _ = tikz.pdf()      # not tested

        Using subgraphs clusters (broken when using labels, see
        :issue:`22070`)::

            sage: S = FiniteSetMaps(5)
            sage: I = S((0,1,2,3,4))
            sage: a = S((0,1,3,0,0))
            sage: b = S((0,2,4,1,0))
            sage: roots = [I]
            sage: succ = lambda v: [v*a,v*b,a*v,b*v]
            sage: R = RecursivelyEnumeratedSet(roots, succ)
            sage: G = R.to_digraph()                                                    # needs sage.graphs
            sage: G                                                                     # needs sage.graphs
            Looped multi-digraph on 27 vertices
            sage: C = G.strongly_connected_components()                                 # needs sage.graphs
            sage: tikz = TikzPicture.from_graph(G,                              # optional - dot2tex graphviz, needs sage.graphs
            ....:              merge_multiedges=False, subgraph_clusters=C)
            sage: _ = tikz.pdf()      # not tested

        An example coming from ``graphviz_string`` documentation in SageMath::

            sage: # needs sage.graphs sage.symbolic
            sage: f(x) = -1 / x
            sage: g(x) = 1 / (x + 1)
            sage: G = DiGraph()
            sage: G.add_edges((i, f(i), f) for i in (1, 2, 1/2, 1/4))
            sage: G.add_edges((i, g(i), g) for i in (1, 2, 1/2, 1/4))
            sage: tikz = TikzPicture.from_graph(G)      # optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested
            sage: def edge_options(data):
            ....:     u, v, label = data
            ....:     options = {"color": {f: "red", g: "blue"}[label]}
            ....:     if (u,v) == (1/2, -2): options["label"]       = "coucou"; options["label_style"] = "string"
            ....:     if (u,v) == (1/2,2/3): options["dot"]         = "x=1,y=2"
            ....:     if (u,v) == (1,   -1): options["label_style"] = "latex"
            ....:     if (u,v) == (1,  1/2): options["dir"]         = "back"
            ....:     return options
            sage: tikz = TikzPicture.from_graph(G, edge_options=edge_options)   # optional - dot2tex graphviz
            sage: _ = tikz.pdf()      # not tested
        '''
    @classmethod
    def from_graph_with_pos(cls, graph, scale: int = 1, merge_multiedges: bool = True, merge_label_function=...):
        """
        Convert a graph with positions defined for vertices to a tikzpicture.

        .. WARNING::

            This method might be deleted in the future in favor of a method
            in the graph class returning a tikz picture.

        INPUT:

        - ``graph`` -- graph (with predefined positions)
        - ``scale`` -- number (default: ``1``); tikzpicture scale
        - ``merge_multiedges`` -- boolean (default: ``True``); if the graph
          has multiple edges, whether to merge the multiedges into one
          single edge
        - ``merge_label_function`` -- function (default: ``tuple``); a
          function to apply to each list of labels to be merged. It is
          ignored if ``merge_multiedges`` is not ``True`` or if the graph
          has no multiple edges.

        EXAMPLES::

            sage: from sage.misc.latex_standalone import TikzPicture

            sage: # needs sage.graphs
            sage: g = graphs.PetersenGraph()
            sage: tikz = TikzPicture.from_graph_with_pos(g)
            doctest:...: FutureWarning: This class/method/function is marked as experimental.
            It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/20343 for details.

        ::

            sage: # needs sage.graphs
            sage: edges = [(0,0,'a'),(0,1,'b'),(0,1,'c')]
            sage: kwds = dict(format='list_of_edges', loops=True, multiedges=True)
            sage: G = DiGraph(edges, **kwds)
            sage: G.set_pos({0:(0,0), 1:(1,0)})
            sage: f = lambda label:','.join(label)
            sage: TikzPicture.from_graph_with_pos(G, merge_label_function=f)
            \\documentclass[tikz]{standalone}
            \\standaloneconfig{border=4mm}
            \\begin{document}
            \\begin{tikzpicture}
            [auto,scale=1]
            % vertices
            \\node (node_0) at (0, 0) {0};
            \\node (node_1) at (1, 0) {1};
            % edges
            \\draw[->] (node_0) -- node {b,c} (node_1);
            % loops
            \\draw (node_0) edge [loop above] node {a} ();
            \\end{tikzpicture}
            \\end{document}

        TESTS::

            sage: # needs sage.graphs
            sage: edges = [(0,0,'a'),(0,1,'b'),(0,1,'c')]
            sage: kwds = dict(format='list_of_edges', loops=True, multiedges=True)
            sage: G = DiGraph(edges, **kwds)
            sage: TikzPicture.from_graph_with_pos(G)
            Traceback (most recent call last):
            ...
            ValueError: vertex positions need to be set first
        """
    @classmethod
    def from_poset(cls, poset, **kwds):
        """
        Convert a poset to a tikzpicture using graphviz and dot2tex.

        .. NOTE::

            Prerequisite: dot2tex optional Sage package and graphviz must be
            installed.

        .. WARNING::

            This method might be deleted in the future in favor of a method
            in the graph class returning a tikz picture.

        INPUT:

        - ``poset`` -- poset
        - ``prog`` -- string (default: ``'dot'``); the program used for the
          layout corresponding to one of the software of the graphviz
          suite: ``'dot'``, ``'neato'``, ``'twopi'``, ``'circo'`` or ``'fdp'``
        - ``edge_labels`` -- boolean (default: ``True``)
        - ``color_by_label`` -- boolean (default: ``False``)
        - ``rankdir`` -- string (default: ``'down'``)

        EXAMPLES::

            sage: from sage.misc.latex_standalone import TikzPicture

            sage: # needs sage.graphs sage.modules
            sage: P = posets.PentagonPoset()
            sage: tikz = TikzPicture.from_poset(P)                              # optional - dot2tex graphviz
            doctest:...: FutureWarning: This class/method/function is marked as experimental.
            It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/20343 for details.

        ::

            sage: tikz = TikzPicture.from_poset(P, prog='neato',        # long time (3s), optional - dot2tex, needs sage.graphs sage.modules
            ....:                               color_by_label=True)

        ::

            sage: # needs sage.graphs
            sage: P = posets.SymmetricGroupWeakOrderPoset(4)
            sage: tikz = TikzPicture.from_poset(P)                      # long time (4s), optional - dot2tex graphviz
            sage: tikz = TikzPicture.from_poset(P, prog='neato')        # long time (4s), optional - dot2tex graphviz
        """
    def tikz_picture_code(self):
        '''
        EXAMPLES::

            sage: from sage.misc.latex_standalone import TikzPicture
            sage: s = "\\\\begin{tikzpicture}\\n\\\\draw (0,0) -- (1,1);\\n\\\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: print(t.tikz_picture_code())
            \\begin{tikzpicture}
            \\draw (0,0) -- (1,1);
            \\end{tikzpicture}
        '''
