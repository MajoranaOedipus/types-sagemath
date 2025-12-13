import types
from _typeshed import Incomplete
from sage.repl.rich_output.output_basic import OutputAsciiArt as OutputAsciiArt, OutputPlainText as OutputPlainText, OutputUnicodeArt as OutputUnicodeArt
from sage.repl.rich_output.output_browser import OutputHtml as OutputHtml
from sage.repl.rich_output.preferences import DisplayPreferences as DisplayPreferences
from sage.structure.sage_object import SageObject as SageObject
from typing import Any, Self

class DisplayException(Exception):
    """
    Base exception for all rich output-related exceptions.

    EXAMPLES::

        sage: from sage.repl.rich_output.display_manager import DisplayException
        sage: raise DisplayException('foo')
        Traceback (most recent call last):
        ...
        DisplayException: foo
    """
class OutputTypeException(DisplayException):
    """
    Wrong Output container.

    The output containers are the subclasses of
    :class:`~sage.repl.rich_output.output_basic.OutputBase` that
    contain the entire output. The display backends must create output
    containers of a suitable type depending on the displayed Python
    object. This exception indicates that there is a mistake in the
    backend and it returned the wrong type of output container.

    EXAMPLES::

        sage: from sage.repl.rich_output.display_manager import OutputTypeException
        sage: raise OutputTypeException('foo')
        Traceback (most recent call last):
        ...
        OutputTypeException: foo
    """
class RichReprWarning(UserWarning):
    """
    Warning that is throws if a call to ``_rich_repr_`` fails.

    If an object implements ``_rich_repr_`` then it must return a
    value, possibly ``None`` to indicate that no rich output can be
    generated. But it may not raise an exception as it is very
    confusing for the user if the displayhook fails.

    EXAMPLES::

        sage: from sage.repl.rich_output.display_manager import RichReprWarning
        sage: raise RichReprWarning('foo')
        Traceback (most recent call last):
        ...
        RichReprWarning: foo
    """

class restricted_output:
    def __init__(self, display_manager, output_classes) -> None:
        """
        Context manager to temporarily restrict the accepted output types.

        In the context, the output is restricted to the output
        container types listed in ``output_classes``. Additionally,
        display preferences are changed not to show graphics.

        INPUT:

        - ``display_manager`` -- the display manager

        - ``output_classes`` -- iterable of output container types

        EXAMPLES::

            sage: from sage.repl.rich_output.display_manager import (
            ....:     get_display_manager, restricted_output)
            sage: dm = get_display_manager()
            sage: restricted_output(dm, [dm.types.OutputPlainText])
            <sage.repl.rich_output.display_manager.restricted_output object at 0x...>
        """
    def __enter__(self) -> None:
        """
        Enter the restricted output context.

        EXAMPLES::

            sage: from sage.repl.rich_output.display_manager import (
            ....:     get_display_manager, restricted_output)
            sage: dm = get_display_manager()
            sage: len(dm.supported_output()) > 1
            True
            sage: with restricted_output(dm, [dm.types.OutputPlainText]):
            ....:    dm.supported_output()
            frozenset({<class 'sage.repl.rich_output.output_basic.OutputPlainText'>})

            sage: dm.preferences.supplemental_plot
            'never'
            sage: dm.preferences.supplemental_plot = 'always'
            sage: with restricted_output(dm, [dm.types.OutputPlainText]):
            ....:    dm.preferences
            Display preferences:
            * align_latex is not specified
            * graphics = disable
            * supplemental_plot = never
            * text is not specified
            sage: dm.preferences.supplemental_plot = 'never'
        """
    def __exit__(self, exception_type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None:
        """
        Exit the restricted output context.

        EXAMPLES::

            sage: from sage.repl.rich_output.display_manager import (
            ....:     get_display_manager, restricted_output)
            sage: dm = get_display_manager()
            sage: with restricted_output(dm, [dm.types.OutputPlainText]):
            ....:     assert len(dm.supported_output()) == 1
            sage: assert len(dm.supported_output()) > 1
        """

class DisplayManager(SageObject):
    def __init__(self) -> None:
        """
        The Display Manager.

        Used to decide what kind of rich output is best.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: get_display_manager()
            The Sage display manager using the doctest backend
        """
    @classmethod
    def get_instance(cls) -> Self:
        """
        Get the singleton instance.

        This class method is equivalent to
        :func:`get_display_manager`.

        OUTPUT: the display manager singleton

        EXAMPLES::

            sage: from sage.repl.rich_output.display_manager import DisplayManager
            sage: DisplayManager.get_instance()
            The Sage display manager using the doctest backend
        """
    @property
    def types(self):
        """
        Catalog of all output container types.

        Note that every output type must be registered in
        :mod:`sage.repl.rich_output.output_catalog`.

        OUTPUT:

        Returns the :mod:`sage.repl.rich_output.output_catalog`
        module.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.types.OutputPlainText
            <class 'sage.repl.rich_output.output_basic.OutputPlainText'>
        """
    def switch_backend(self, backend, **kwds):
        """
        Switch to a new backend.

        INPUT:

        - ``backend`` -- instance of
          :class:`~sage.repl.rich_output.backend_base.BackendBase`

        - ``kwds`` -- optional keyword arguments that are passed on to
          the :meth:`~sage.repl.rich_output.backend_base.BackendBase.install`
          method

        OUTPUT: the previous backend

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendSimple
            sage: simple = BackendSimple()
            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager();  dm
            The Sage display manager using the doctest backend

            sage: previous = dm.switch_backend(simple)
            sage: dm
            The Sage display manager using the simple backend

        Restore the doctest backend::

            sage: dm.switch_backend(previous) is simple
            True
        """
    @property
    def preferences(self):
        """
        Return the preferences.

        OUTPUT:

        The display preferences as instance of
        :class:`~sage.repl.rich_output.preferences.DisplayPreferences`.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.preferences
            Display preferences:
            * align_latex is not specified
            * graphics is not specified
            * supplemental_plot = never
            * text is not specified
        """
    def is_in_terminal(self):
        """
        Test whether the UI is meant to run in a terminal.

        When this method returns ``True``, you can assume that it is
        possible to use ``raw_input`` or launch external programs that
        take over the input.

        Otherwise, you should assume that the backend runs remotely or
        in a pty controlled by another program. Then you should not
        launch external programs with a (text or graphical) UI.

        This is used to enable/disable interpreter consoles.

        OUTPUT:

        Boolean.
        """
    def check_backend_class(self, backend_class) -> None:
        """
        Check that the current backend is an instance of
        ``backend_class``.

        This is, for example, used by the Sage IPython display
        formatter to ensure that the IPython backend is in use.

        INPUT:

        - ``backend_class`` -- type of a backend class

        OUTPUT:

        This method returns nothing. A :exc:`RuntimeError` is raised if
        ``backend_class`` is not the type of the current backend.

        EXAMPLES::

            sage: from sage.repl.rich_output.backend_base import BackendSimple
            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.check_backend_class(BackendSimple)
            Traceback (most recent call last):
            ...
            RuntimeError: check failed: current backend is invalid
        """
    def graphics_from_save(self, save_function, save_kwds, file_extension, output_container, figsize=None, dpi=None):
        """
        Helper to construct graphics.

        This method can be used to simplify the implementation of a
        ``_rich_repr_`` method of a graphics object if there is
        already a function to save graphics to a file.

        INPUT:

        - ``save_function`` -- callable that can save graphics to a file
          and accepts options like :meth:`sage.plot.graphics.Graphics.save`

        - ``save_kwds`` -- dictionary; keyword arguments that are
          passed to the save function

        - ``file_extension`` -- string starting with ``'.'``; the file
          extension of the graphics file

        - ``output_container`` -- subclass of
          :class:`sage.repl.rich_output.output_basic.OutputBase`. The
          output container to use. Must be one of the types in
          :meth:`supported_output`.

        - ``figsize`` -- pair of integers (optional). The desired graphics
          size in pixels. Suggested, but need not be respected by the
          output.

        - ``dpi`` -- integer (optional). The desired resolution in dots
          per inch. Suggested, but need not be respected by the output.

        OUTPUT: an instance of ``output_container``

        EXAMPLES::

            sage: # needs sage.plot sage.symbolic
            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: plt = plot(sin)
            sage: out = dm.graphics_from_save(plt.save, dict(), '.png',
            ....:                             dm.types.OutputImagePng)
            sage: out
            OutputImagePng container
            sage: out.png.get().startswith(b'\\x89PNG')
            True
            sage: out.png.filename()   # random
            '/home/user/.sage/temp/localhost.localdomain/23903/tmp_pu5woK.png'
        """
    def threejs_scripts(self, online):
        '''
        Return Three.js script tag for the current backend.

        INPUT:

        - ``online`` -- boolean determining script usage context

        OUTPUT: string containing script tag

        .. NOTE::

            This base method handles ``online=True`` case only, serving CDN
            script tag. Location of script for offline usage is
            backend-specific.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: get_display_manager().threejs_scripts(online=True)                    # needs sage.plot
            \'...<script src="https://cdn.jsdelivr.net/gh/sagemath/threejs-sage@...\'
            sage: get_display_manager().threejs_scripts(online=False)                   # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: current backend does not support
            offline threejs graphics
        '''
    def supported_output(self):
        """
        Return the output container classes that can be used.

        OUTPUT:

        Frozen set of subclasses of
        :class:`~sage.repl.rich_output.output_basic.OutputBase`. If
        the backend defines derived container classes, this method
        will always return their base classes.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.types.OutputPlainText in dm.supported_output()
            True
            sage: type(dm.supported_output())
            <... 'frozenset'>
        """
    def displayhook(self, obj: Any) -> None | Any:
        """
        Implementation of the displayhook.

        Every backend must pass the value of the last statement of a
        line / cell to this method. See also
        :meth:`display_immediately` if you want do display rich output
        while a program is running.

        INPUT:

        - ``obj`` -- anything; the object to be shown

        OUTPUT: whatever the backend's displayhook method returned

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.displayhook(1/2)
            1/2
        """
    def display_immediately(self, obj, **rich_repr_kwds) -> None:
        """
        Show output without going back to the command line prompt.

        This method must be called to create rich output from an
        object when we are not returning to the command line prompt,
        for example during program execution. Typically, it is being
        called by :meth:`sage.plot.graphics.Graphics.show`.

        INPUT:

        - ``obj`` -- anything; the object to be shown

        - ``rich_repr_kwds`` -- optional keyword arguments that are
          passed through to ``obj._rich_repr_``

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.display_immediately(1/2)
            1/2
        """

get_display_manager: Incomplete
