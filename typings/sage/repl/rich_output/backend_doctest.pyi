from sage.repl.rich_output.output_catalog import *
from sage.repl.rich_output.backend_base import BackendBase as BackendBase

class BackendDoctest(BackendBase):
    def default_preferences(self):
        """
        Return the backend's display preferences.

        Matches the IPython command line display preferences to keep
        the differences between that and the doctests to a minimum.

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
    def install(self, **kwds) -> None:
        """
        Switch to the doctest backend.

        This method is being called from within
        :meth:`~sage.repl.rich_output.display_manager.DisplayManager.switch_backend`. You
        should never call it by hand.

        INPUT:

        - ``**kwds`` -- none of the optional keyword arguments are used in the
          doctest backend

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_doctest import BackendDoctest
            sage: backend = BackendDoctest()
            sage: backend.install()
            sage: backend.uninstall()
        """
    def uninstall(self) -> None:
        """
        Switch away from the doctest backend.

        This method is being called from within
        :meth:`~sage.repl.rich_output.display_manager.DisplayManager.switch_backend`. You
        should never call it by hand.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_doctest import BackendDoctest
            sage: backend = BackendDoctest()
            sage: backend.install()
            sage: backend.uninstall()
        """
    def supported_output(self):
        """
        Return the supported output types.

        OUTPUT:

        Set of subclasses of
        :class:`~sage.repl.rich_output.output_basic.OutputBase`, the
        supported output container types.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_doctest import BackendDoctest
            sage: from sage.repl.rich_output.output_catalog import *
            sage: backend = BackendDoctest()
            sage: OutputPlainText in backend.supported_output()
            True
            sage: OutputSceneJmol in backend.supported_output()
            True
        """
    def displayhook(self, plain_text, rich_output) -> None:
        """
        Display object from displayhook.

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

        EXAMPLES:

        This ends up calling the displayhook::

            sage: plt = plot(sin)                                                       # needs sage.plot sage.symbolic
            sage: plt                                                                   # needs sage.plot sage.symbolic
            Graphics object consisting of 1 graphics primitive
            sage: plt.show()                                                            # needs sage.plot sage.symbolic

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.displayhook(plt)       # indirect doctest                          # needs sage.plot sage.symbolic
            Graphics object consisting of 1 graphics primitive
        """
    def display_immediately(self, plain_text, rich_output) -> None:
        """
        Display object immediately.

        INPUT:

        Same as :meth:`displayhook`.

        EXAMPLES:

        The following example does not call the displayhook. More
        precisely, the ``show()`` method returns ``None`` which is
        ignored by the displayhook. When running the example on a Sage
        display backend capable of displaying graphics outside of the
        displayhook, the plot is still shown. Nothing is shown during
        doctests::

            sage: plt = plot(sin)                                                       # needs sage.plot sage.symbolic
            sage: plt                                                                   # needs sage.plot sage.symbolic
            Graphics object consisting of 1 graphics primitive
            sage: plt.show()                                                            # needs sage.plot sage.symbolic

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.display_immediately(plt)   # indirect doctest                      # needs sage.plot sage.symbolic
        """
    def validate(self, rich_output) -> None:
        """
        Perform checks on ``rich_output``.

        INPUT:

        - ``rich_output`` -- instance of a subclass of
          :class:`~sage.repl.rich_output.output_basic.OutputBase`

        OUTPUT: an assertion is triggered if ``rich_output`` is invalid

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: invalid = dm.types.OutputImagePng('invalid')
            sage: backend = dm._backend;  backend
            doctest
            sage: backend.validate(invalid)
            Traceback (most recent call last):
            ...
            AssertionError
            sage: backend.validate(dm.types.OutputPlainText.example())
            sage: backend.validate(dm.types.OutputAsciiArt.example())
            sage: backend.validate(dm.types.OutputLatex.example())
            sage: backend.validate(dm.types.OutputImagePng.example())
            sage: backend.validate(dm.types.OutputImageGif.example())
            sage: backend.validate(dm.types.OutputImageJpg.example())
            sage: backend.validate(dm.types.OutputImageSvg.example())
            sage: backend.validate(dm.types.OutputImagePdf.example())
            sage: backend.validate(dm.types.OutputImageDvi.example())
            sage: backend.validate(dm.types.OutputSceneJmol.example())
            sage: backend.validate(dm.types.OutputSceneWavefront.example())
            sage: backend.validate(dm.types.OutputSceneCanvas3d.example())
            sage: backend.validate(dm.types.OutputVideoOgg.example())
            sage: backend.validate(dm.types.OutputVideoWebM.example())
            sage: backend.validate(dm.types.OutputVideoMp4.example())
            sage: backend.validate(dm.types.OutputVideoFlash.example())
            sage: backend.validate(dm.types.OutputVideoMatroska.example())
            sage: backend.validate(dm.types.OutputVideoAvi.example())
            sage: backend.validate(dm.types.OutputVideoWmv.example())
            sage: backend.validate(dm.types.OutputVideoQuicktime.example())
        """
