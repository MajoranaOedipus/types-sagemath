from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject

VIEWERS: Incomplete

def default_viewer(viewer=None):
    """
    Set up default programs for opening web pages, PDFs, PNGs, and DVI files.

    INPUT:

    - ``viewer`` -- ``None`` or a string; one of ``'browser'``, ``'pdf'``,
      ``'png'``, ``'dvi'``. Return the name of the corresponding program.
      ``None`` is treated the same as ``'browser'``.

    EXAMPLES::

        sage: from sage.misc.viewer import default_viewer
        sage: default_viewer(None) # random -- depends on OS, etc.
        'open'
        sage: default_viewer('pdf') # random -- depends on OS, etc.
        'xdg-open'
        sage: default_viewer('jpg')
        Traceback (most recent call last):
        ...
        ValueError: Unknown type of viewer: jpg.
    """

class Viewer(SageObject):
    """
    Set defaults for various viewing applications: a web browser, a
    dvi viewer, a pdf viewer, and a png viewer.

    EXAMPLES::

        sage: from sage.misc.viewer import viewer
        sage: old_browser = viewer.browser()  # indirect doctest
        sage: viewer.browser('open -a /Applications/Firefox.app')
        sage: viewer.browser()
        'open -a /Applications/Firefox.app'
        sage: viewer.browser(old_browser) # restore old value
    """
    def browser(self, app=None):
        """
        Change the default browser. Return the current setting if arg
        is ``None``, which is the default.

        INPUT:

        - ``app`` -- ``None`` or a string, the program to use

        EXAMPLES::

            sage: from sage.misc.viewer import viewer
            sage: old_browser = viewer.browser()
            sage: viewer.browser('open -a /Applications/Firefox.app') # indirect doctest
            sage: viewer.browser()
            'open -a /Applications/Firefox.app'
            sage: viewer.browser(old_browser) # restore old value
        """
    def dvi_viewer(self, app=None):
        """
        Change the default dvi viewer. Return the current setting if arg
        is ``None``, which is the default.

        INPUT:

        - ``app`` -- ``None`` or a string, the program to use

        EXAMPLES::

            sage: from sage.misc.viewer import viewer
            sage: old_dvi_app = viewer.dvi_viewer()
            sage: viewer.dvi_viewer('/usr/bin/xdvi') # indirect doctest
            sage: viewer.dvi_viewer()
            '/usr/bin/xdvi'
            sage: viewer.dvi_viewer(old_dvi_app) # restore old value
        """
    def pdf_viewer(self, app=None):
        """
        Change the default pdf viewer. Return the current setting if arg
        is ``None``, which is the default.

        INPUT:

        - ``app`` -- ``None`` or a string, the program to use

        EXAMPLES::

            sage: from sage.misc.viewer import viewer
            sage: old_pdf_app = viewer.pdf_viewer()
            sage: viewer.pdf_viewer('/usr/bin/pdfopen') # indirect doctest
            sage: viewer.pdf_viewer()
            '/usr/bin/pdfopen'
            sage: viewer.pdf_viewer(old_pdf_app) # restore old value
        """
    def png_viewer(self, app=None):
        """
        Change the default png viewer. Return the current setting if arg
        is ``None``, which is the default.

        INPUT:

        - ``app`` -- ``None`` or a string, the program to use

        EXAMPLES::

            sage: from sage.misc.viewer import viewer
            sage: old_png_app = viewer.png_viewer()
            sage: viewer.png_viewer('display') # indirect doctest
            sage: viewer.png_viewer()
            'display'
            sage: viewer.png_viewer(old_png_app) # restore old value
        """
    def __call__(self, x=None):
        """
        Return the current setting for a viewer program.

        INPUT:

        - ``x`` -- string

        If ``x`` is ``None`` or starts with 'browse', then return the
        current browser app.  If ``x`` starts with 'dvi', return the
        current dvi viewer, and similarly if ``x`` starts with 'png'
        or 'pdf'.

        EXAMPLES::

            sage: from sage.misc.viewer import viewer
            sage: viewer('pdf') # random -- depends on OS, etc.
            'mozilla'
            sage: viewer('browser') == viewer()
            True
        """

viewer: Incomplete

def browser():
    """
    Return the program used to open a web page.  By default, the
    program used depends on the platform and other factors, like
    settings of certain environment variables.  To use a different
    program, call ``viewer.browser('PROG')``, where 'PROG' is the
    desired program.

    EXAMPLES::

        sage: from sage.misc.viewer import browser
        sage: browser() # random -- depends on OS, etc.
        'open'
    """
def dvi_viewer():
    """
    Return the program used to display a dvi file.  By default, the
    program used depends on the platform and other factors, like
    settings of certain environment variables.  To use a different
    program, call ``viewer.dvi_viewer('PROG')``, where 'PROG' is the
    desired program.

    EXAMPLES::

        sage: from sage.misc.viewer import dvi_viewer
        sage: dvi_viewer() # random -- depends on OS, etc.
        'open'
    """
def pdf_viewer():
    """
    Return the program used to display a pdf file.  By default, the
    program used depends on the platform and other factors, like
    settings of certain environment variables.  To use a different
    program, call ``viewer.pdf_viewer('PROG')``, where 'PROG' is the
    desired program.

    EXAMPLES::

        sage: from sage.misc.viewer import pdf_viewer, viewer
        sage: old_pdf_app = viewer.pdf_viewer()
        sage: viewer.pdf_viewer('acroread')
        sage: pdf_viewer()
        'acroread'
        sage: viewer.pdf_viewer('old_pdf_app')
    """
def png_viewer():
    """
    Return the program used to display a png file. By default, the
    program used depends on the platform and other factors, like
    settings of certain environment variables.  To use a different
    program, call ``viewer.png_viewer('PROG')``, where 'PROG' is the
    desired program.

    EXAMPLES::

        sage: from sage.misc.viewer import png_viewer
        sage: png_viewer() # random -- depends on OS, etc.
        'xdg-open'
    """
