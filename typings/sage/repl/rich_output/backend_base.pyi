from sage.structure.sage_object import SageObject as SageObject

class BackendBase(SageObject):
    def get_display_manager(self):
        """
        Return the display manager singleton.

        This is a convenience method to access the display manager
        singleton.

        OUTPUT:

        The unique
        :class:`~sage.repl.rich_output.display_manager.DisplayManager`
        instance.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.get_display_manager()
            The Sage display manager using the doctest backend
        """
    def install(self, **kwds) -> None:
        """
        Hook that will be called once before the backend is used for the
        first time.

        The default implementation does nothing.

        INPUT:

        - ``kwds`` -- optional keyword arguments that are passed
          through by the
          :meth:`~sage.repl.rich_output.display_manager.DisplayManager.switch_backend`
          method.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.install()
        """
    def uninstall(self) -> None:
        """
        Hook that will be called once right before the backend is removed.

        The default implementation does nothing.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.uninstall()
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

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.default_preferences()
            Display preferences:
            * align_latex is not specified
            * graphics is not specified
            * supplemental_plot is not specified
            * text is not specified
        """
    def supported_output(self) -> None:
        """
        Return the outputs that are supported by the backend.

        Subclasses must implement this method.

        OUTPUT:

        Iterable of output container classes, that is, subclass of
        :class:`~sage.repl.rich_output.output_basic.OutputBase`).  May
        be a list/tuple/set/frozenset. The order is ignored. Only used
        internally by the display manager.

        You may return backend-specific subclasses of existing output
        containers. This allows you to attach backend-specific
        functionality to the output container.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.supported_output()
            Traceback (most recent call last):
            ...
            NotImplementedError: derived classes must implement this method
        """
    def is_in_terminal(self):
        """
        Test whether the UI is meant to run in a terminal.

        See
        :meth:`sage.repl.rich_output.display_manager.DisplayManager.is_in_terminal`
        for details.

        OUTPUT: defaults to ``False``

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.is_in_terminal()
            False
        """
    def max_width(self):
        """
        Return the number of characters that fit into one output line.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.max_width()
            79
        """
    def newline(self):
        """
        Return the newline string.

        OUTPUT: string for starting a new line of output

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.newline()
            '\\n'
        """
    def plain_text_formatter(self, obj, **kwds):
        """
        Hook to override how plain text is being formatted.

        If the object does not have a ``_rich_repr_`` method, or if it
        does not return a rich output object
        (:class:`~sage.repl.rich_output.output_basic.OutputBase`),
        then this method is used to generate plain text output.

        INPUT:

        - ``obj`` -- anything

        - ``**kwds`` -- optional keyword arguments to control the
          formatting. Supported are:

            * ``concatenate`` -- boolean (default: ``False``); if
              ``True``, the argument ``obj`` must be iterable and its
              entries will be concatenated. There is a single
              whitespace between entries.

        OUTPUT:

        Instance of
        :class:`~sage.repl.rich_output.output_basic.OutputPlainText`
        containing the string representation of the object.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: out = backend.plain_text_formatter(list(range(30)))
            sage: out
            OutputPlainText container
            sage: out.text
            buffer containing 139 bytes
            sage: out.text.get_str()
            '[0,\\n 1,\\n 2,\\n 3,\\n 4,\\n 5,\\n 6,\\n 7,\\n 8,\\n 9,\\n
            10,\\n 11,\\n 12,\\n 13,\\n 14,\\n 15,\\n 16,\\n 17,\\n 18,\\n
            19,\\n 20,\\n 21,\\n 22,\\n 23,\\n 24,\\n 25,\\n 26,\\n 27,\\n
            28,\\n 29]'

            sage: out = backend.plain_text_formatter(list(range(20)), concatenate=True)
            sage: out.text.get_str()
            '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19'
        """
    def ascii_art_formatter(self, obj, **kwds):
        """
        Hook to override how ascii art is being formatted.

        INPUT:

        - ``obj`` -- anything

        - ``**kwds`` -- optional keyword arguments to control the
          formatting. Supported are:

            * ``concatenate`` -- boolean (default: ``False``); if
              ``True``, the argument ``obj`` must be iterable and its
              entries will be concatenated. There is a single
              whitespace between entries.

        OUTPUT:

        Instance of
        :class:`~sage.repl.rich_output.output_basic.OutputAsciiArt`
        containing the ascii art string representation of the object.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: out = backend.ascii_art_formatter(list(range(30)))
            sage: out
            OutputAsciiArt container
            sage: out.ascii_art
            buffer containing 114 bytes
            sage: print(out.ascii_art.get_str())
            [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
            <BLANKLINE>
             22, 23, 24, 25, 26, 27, 28, 29 ]
            sage: backend.ascii_art_formatter([1,2,3], concatenate=False).ascii_art.get_str()
            '[ 1, 2, 3 ]'
            sage: backend.ascii_art_formatter([1,2,3], concatenate=True).ascii_art.get_str()
            '1 2 3'
        """
    def unicode_art_formatter(self, obj, **kwds):
        """
        Hook to override how unicode art is being formatted.

        INPUT:

        - ``obj`` -- anything

        - ``**kwds`` -- optional keyword arguments to control the
          formatting. Supported are:

            * ``concatenate`` -- boolean (default: ``False``); if
              ``True``, the argument ``obj`` must be iterable and its
              entries will be concatenated. There is a single
              whitespace between entries.

        OUTPUT:

        Instance of
        :class:`~sage.repl.rich_output.output_basic.OutputUnicodeArt`
        containing the unicode art string representation of the object.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: out = backend.unicode_art_formatter(list(range(30)))
            sage: out
            OutputUnicodeArt container
            sage: out.unicode_art
            buffer containing 114 bytes
            sage: print(out.unicode_art.get_str())
            [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
            <BLANKLINE>
            22, 23, 24, 25, 26, 27, 28, 29 ]

            sage: backend.unicode_art_formatter([1,2,3], concatenate=False).unicode_art.get_str()
            '[ 1, 2, 3 ]'
            sage: backend.unicode_art_formatter([1,2,3], concatenate=True).unicode_art.get_str()
            '1 2 3'
        """
    def latex_formatter(self, obj, **kwds):
        """
        Hook to override how latex is being formatted.

        INPUT:

        - ``obj`` -- anything

        - ``**kwds`` -- optional keyword arguments to control the
          formatting. Supported are:

            * ``concatenate`` -- boolean (default: ``False``); if
              ``True``, the argument ``obj`` must be iterable and its
              entries will be concatenated. There is a single
              whitespace between entries.

        OUTPUT:

        Instance of :class:`~sage.repl.rich_output.output_browser.OutputHtml`
        containing the latex string representation of the object.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: out = backend.latex_formatter(1/2)
            sage: out
            OutputHtml container
            sage: out.html
            buffer containing 42 bytes
            sage: out.html.get_str()
            '<html>\\\\(\\\\displaystyle \\\\frac{1}{2}\\\\)</html>'

            sage: # needs sage.symbolic
            sage: out = backend.latex_formatter([1/2, x, 3/4, ZZ], concatenate=False)
            sage: out.html.get_str()
            '<html>\\\\(\\\\displaystyle \\\\newcommand{\\\\Bold}[1]{\\\\mathbf{#1}}\\\\left[\\\\frac{1}{2}, x, \\\\frac{3}{4}, \\\\Bold{Z}\\\\right]\\\\)</html>'
            sage: out = backend.latex_formatter([1/2, x, 3/4, ZZ], concatenate=True)
            sage: out.html.get_str()
            '<html>\\\\(\\\\displaystyle \\\\newcommand{\\\\Bold}[1]{\\\\mathbf{#1}}\\\\frac{1}{2} x \\\\frac{3}{4} \\\\Bold{Z}\\\\)</html>'

        TESTS::

            sage: backend.latex_formatter([], concatenate=False).html.get_str()
            '<html>\\\\(\\\\displaystyle \\\\left[\\\\right]\\\\)</html>'
            sage: backend.latex_formatter([], concatenate=True).html.get_str()
            '<html>\\\\(\\\\displaystyle \\\\)</html>'
        """
    def set_underscore_variable(self, obj) -> None:
        """
        Set the ``_`` builtin variable.

        By default, this sets the special ``_`` variable. Backends
        that organize the history differently (e.g. IPython) can
        override this method.

        INPUT:

        - ``obj`` -- result of the most recent evaluation

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.set_underscore_variable(123)
            sage: _
            123

            sage: 'foo'
            'foo'
            sage: _     # indirect doctest
            'foo'
        """
    def displayhook(self, plain_text, rich_output):
        """
        Backend implementation of the displayhook.

        The value of the last statement on a REPL input line or
        notebook cell are usually handed to the Python displayhook and
        shown on screen.  By overriding this method you define how
        your backend handles output. The difference to the usual
        displayhook is that Sage already converted the value to the
        most suitable rich output container.

        Derived classes must implement this method.

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

        This method may return something, which is then returned from
        the display manager's
        :meth:`~sage.repl.rich_output.display_manager.DisplayManager.displayhook`
        method.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.displayhook(plain_text, plain_text)
            Traceback (most recent call last):
            ...
            NotImplementedError: derived classes must implement this method
        """
    def display_immediately(self, plain_text, rich_output) -> None:
        """
        Show output without going back to the command line prompt.

        This method is similar to the rich output :meth:`displayhook`,
        except that it can be invoked at any time. Typically, it ends
        up being called by :meth:`sage.plot.graphics.Graphics.show`.

        Derived classes must implement this method.

        INPUT:

        Same as :meth:`displayhook`.

        OUTPUT:

        This method may return something so you can implement
        :meth:`displayhook` by calling this method. However, when
        called by the display manager any potential return value is
        discarded: There is no way to return anything without
        returning to the command prompt.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_base import BackendBase
            sage: backend = BackendBase()
            sage: backend.display_immediately(plain_text, plain_text)
            Traceback (most recent call last):
            ...
            NotImplementedError: derived classes must implement this method
        """

class BackendSimple(BackendBase):
    """
    Simple Backend.

    This backend only supports plain text.

    EXAMPLES::

        sage: from sage.repl.rich_output.backend_base import BackendSimple
        sage: BackendSimple()
        simple
    """
    def supported_output(self):
        """
        Return the outputs that are supported by the backend.

        OUTPUT:

        Iterable of output container classes, that is, subclass of
        :class:`~sage.repl.rich_output.output_basic.OutputBase`).
        This backend only supports the plain text output container.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendSimple
            sage: backend = BackendSimple()
            sage: backend.supported_output()
            {<class 'sage.repl.rich_output.output_basic.OutputPlainText'>}
        """
    def display_immediately(self, plain_text, rich_output) -> None:
        """
        Show output without going back to the command line prompt.

        INPUT:

        Same as :meth:`~BackendBase.displayhook`.

        OUTPUT: this backend returns nothing, it just prints to stdout

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_base import BackendSimple
            sage: backend = BackendSimple()
            sage: backend.display_immediately(plain_text, plain_text)
            Example plain text output
        """
