from sage.repl.rich_output.output_catalog import *
from sage.repl.rich_output.backend_base import BackendBase as BackendBase

class BackendIPython(BackendBase):
    """
    Common base for the IPython UIs.

    EXAMPLES::

        sage: from sage.repl.rich_output.backend_ipython import BackendIPython
        sage: BackendIPython()._repr_()
        Traceback (most recent call last):
        ...
        NotImplementedError: derived classes must implement this method
    """
    def install(self, **kwds) -> None:
        """
        Switch the Sage rich output to the IPython backend.

        INPUT:

        - ``shell`` -- keyword argument; the IPython shell

        No tests since switching away from the doctest rich output
        backend will break the doctests.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: from sage.repl.rich_output.backend_ipython import BackendIPython
            sage: backend = BackendIPython()
            sage: shell = get_test_shell()
            sage: backend.install(shell=shell)
            sage: shell.run_cell('1+1')
            2
        """
    def set_underscore_variable(self, obj) -> None:
        """
        Set the ``_`` builtin variable.

        Since IPython handles the history itself, this does nothing.

        INPUT:

        - ``obj`` -- anything

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: from sage.repl.rich_output.backend_ipython import BackendIPython
            sage: backend = BackendIPython()
            sage: backend.set_underscore_variable(123)
            sage: _
            0
        """
    def display_immediately(self, plain_text, rich_output) -> None:
        """
        Show output immediately.

        This method is similar to the rich output :meth:`displayhook`,
        except that it can be invoked at any time.

        INPUT:

        Same as :meth:`displayhook`.

        OUTPUT: this method does not return anything

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
            sage: backend = BackendIPythonNotebook()
            sage: _ = backend.display_immediately(plain_text, plain_text)
            Example plain text output
        """

class BackendIPythonCommandline(BackendIPython):
    """
    Backend for the IPython Command Line.

    EXAMPLES::

        sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
        sage: BackendIPythonCommandline()
        IPython command line
    """
    def default_preferences(self):
        """
        Return the backend's display preferences.

        The default for the commandline is to not plot graphs since
        the launching of an external viewer is considered too
        disruptive.

        OUTPUT:

        Instance of
        :class:`~sage.repl.rich_output.preferences.DisplayPreferences`.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: backend.default_preferences()
            Display preferences:
            * align_latex is not specified
            * graphics is not specified
            * supplemental_plot = never
            * text is not specified
        """
    def supported_output(self):
        """
        Return the outputs that are supported by the IPython commandline backend.

        OUTPUT:

        Iterable of output container classes, that is, subclass of
        :class:`~sage.repl.rich_output.output_basic.OutputBase`).
        The order is ignored.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: supp = backend.supported_output();  supp     # random output
            set([<class 'sage.repl.rich_output.output_graphics.OutputImageGif'>,
                 ...,
                 <class 'sage.repl.rich_output.output_graphics.OutputImagePng'>])
            sage: from sage.repl.rich_output.output_basic import OutputLatex
            sage: OutputLatex in supp
            True
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

        The IPython commandline display hook returns the IPython
        display data, a pair of dictionaries. The first dictionary
        contains mime types as keys and the respective output as
        value. The second dictionary is metadata.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: backend.displayhook(plain_text, plain_text)
            ({'text/plain': 'Example plain text output'}, {})

        TESTS:

        We verify that unicode strings work::

            sage: class Foo(sage.structure.sage_object.SageObject):
            ....:     def _rich_repr_(self, dm):
            ....:         return dm.types.OutputPlainText('Motörhead')
            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.displayhook(Foo())
            ({'text/plain': 'Motörhead'}, {})
        """
    def display_immediately(self, plain_text, rich_output) -> None:
        """
        Show output without going back to the command line prompt.

        This method is similar to the rich output :meth:`displayhook`,
        except that it can be invoked at any time. On the Sage command
        line it launches viewers just like :meth:`displayhook`.

        INPUT:

        Same as :meth:`displayhook`.

        OUTPUT: this method does not return anything

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: backend.display_immediately(plain_text, plain_text)
            Example plain text output
        """
    def launch_viewer(self, image_file, plain_text):
        """
        Launch external viewer for the graphics file.

        INPUT:

        - ``image_file`` -- string; file name of the image file

        - ``plain_text`` -- string; the plain text representation of
          the image file

        OUTPUT:

        String. Human-readable message indicating whether the viewer
        was launched successfully.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: backend.launch_viewer('/path/to/foo.bar', 'Graphics object')
            'Launched bar viewer for Graphics object'
        """
    def launch_jmol(self, output_jmol, plain_text):
        """
        Launch the stand-alone jmol viewer.

        INPUT:

        - ``output_jmol`` --
          :class:`~sage.repl.rich_output.output_graphics3d.OutputSceneJmol`; the
          scene to launch Jmol with

        - ``plain_text`` -- string; the plain text representation

        OUTPUT:

        string; human-readable message indicating that the viewer was launched.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: from sage.repl.rich_output.output_graphics3d import OutputSceneJmol
            sage: backend.launch_jmol(OutputSceneJmol.example(), 'Graphics3d object')   # needs sage.plot
            'Launched jmol viewer for Graphics3d object'
        """
    def is_in_terminal(self):
        """
        Test whether the UI is meant to run in a terminal.

        See
        :meth:`sage.repl.rich_output.display_manager.DisplayManager.is_in_terminal`
        for details.

        OUTPUT: ``True`` for the IPython commandline

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: backend.is_in_terminal()
            True
        """
    def threejs_offline_scripts(self):
        """
        Three.js script for the IPython command line.

        OUTPUT: string containing script tag

        EXAMPLES::

            sage: # needs threejs
            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonCommandline
            sage: backend = BackendIPythonCommandline()
            sage: backend.threejs_offline_scripts()
            '...<script ...</script>...'
        """

IFRAME_TEMPLATE: str

class BackendIPythonNotebook(BackendIPython):
    """
    Backend for the IPython Notebook.

    EXAMPLES::

        sage: from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
        sage: BackendIPythonNotebook()
        IPython notebook
    """
    def supported_output(self):
        """
        Return the outputs that are supported by the IPython notebook backend.

        OUTPUT:

        Iterable of output container classes, that is, subclass of
        :class:`~sage.repl.rich_output.output_basic.OutputBase`).
        The order is ignored.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
            sage: backend = BackendIPythonNotebook()
            sage: supp = backend.supported_output();  supp     # random output
            set([<class 'sage.repl.rich_output.output_graphics.OutputPlainText'>,
                 ...,
                 <class 'sage.repl.rich_output.output_graphics.OutputImagePdf'>])
            sage: from sage.repl.rich_output.output_basic import OutputLatex
            sage: OutputLatex in supp
            True
            sage: from sage.repl.rich_output.output_graphics import OutputImageGif
            sage: OutputImageGif in supp
            True
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

        The IPython notebook display hook returns the IPython
        display data, a pair of dictionaries. The first dictionary
        contains mime types as keys and the respective output as
        value. The second dictionary is metadata.

        EXAMPLES::

            sage: from sage.repl.rich_output.output_basic import OutputPlainText
            sage: plain_text = OutputPlainText.example()
            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
            sage: backend = BackendIPythonNotebook()
            sage: backend.displayhook(plain_text, plain_text)
            ({'text/plain': 'Example plain text output'}, {})
        """
    def threejs_offline_scripts(self):
        '''
        Three.js script for the IPython notebook.

        OUTPUT: string containing script tag

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
            sage: backend = BackendIPythonNotebook()
            sage: backend.threejs_offline_scripts()                                     # needs sage.plot
            \'...<script src="/nbextensions/threejs-sage/r.../three.min.js...<\\/script>...\'
        '''
