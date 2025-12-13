from sage.repl.rich_output.output_catalog import *
from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline as BackendIPythonCommandline

class BackendEmacs(BackendIPythonCommandline):
    """
    Emacs Backend.

    This backend is used by Emacs' sage-mode to have typeset output
    and inline images.

    EXAMPLES::

        sage: from sage.repl.rich_output.backend_emacs import BackendEmacs
        sage: BackendEmacs()
        Emacs sage-mode
    """
    def default_preferences(self):
        """
        Return the backend's display preferences.

        Override this method to change the default preferences when
        using your backend.

        OUTPUT:

        Instance of
        :class:`~sage.repl.rich_output.preferences.DisplayPreferences`.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_emacs import BackendEmacs
            sage: backend = BackendEmacs()
            sage: backend.default_preferences()
            Display preferences:
            * align_latex is not specified
            * graphics is not specified
            * supplemental_plot is not specified
            * text is not specified
        """
    def displayhook(self, plain_text, rich_output):
        """
        Backend implementation of the displayhook.

        INPUT:

        - ``plain_text`` -- instance of
          :class:`~sage.repl.rich_output.output_basic.OutputPlainText`. The
          plain text version of the output.

        - ``rich_output`` -- instance of an output container class
          (subclass of
          :class:`~sage.repl.rich_output.output_basic.OutputBase`). Guaranteed
          to be one of the output containers returned from
          :meth:`supported_output`, possibly the same as
          ``plain_text``.

        OUTPUT:

        Because this is based on the IPython commandline display hook,
        it returns the IPython display data, a pair of
        dictionaries. The first dictionary contains mime types as keys
        and the respective output as value. The second dictionary is
        metadata.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText, OutputLatex
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_emacs import BackendEmacs
            sage: backend = BackendEmacs()
            sage: backend.displayhook(plain_text, plain_text)
            ({'text/plain': 'Example plain text output'}, {})
            sage: latex_text = OutputLatex.example()
            sage: backend.displayhook(plain_text, latex_text)
            ({'text/plain': 'BEGIN_TEXT:Example plain text output:END_TEXT\\nBEGIN_LATEX:\\\\newcommand{\\\\Bold}[1]{\\\\mathbf{#1}}\\\\int \\\\sin\\\\left(x\\\\right)\\\\,{d x}:END_LATEX'},
              {})
        """
