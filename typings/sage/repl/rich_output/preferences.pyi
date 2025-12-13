from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject

class Property(property):
    name: Incomplete
    underscore_name: Incomplete
    allowed_values: Incomplete
    __doc__: Incomplete
    def __init__(self, name, allowed_values, doc=None) -> None:
        """
        Preference item.

        INPUT:

        - ``name`` -- string; the name of the property

        - ``allowed_values`` -- list/tuple/iterable of allowed values

        - ``doc`` -- string (optional); the docstring of the property

        EXAMPLES::

            sage: from sage.repl.rich_output.preferences import Property
            sage: prop = Property('foo', [0, 1, 2], 'The Foo Property')
            sage: prop.__doc__
            'The Foo Property\\n\\nAllowed values:\\n\\n* ``None`` (default): no preference\\n\\n* 0\\n\\n* 1\\n\\n* 2'
            sage: prop.allowed_values
            (0, 1, 2)
        """
    def getter(self, prefs):
        """
        Get the current value of the property.

        INPUT:

        - ``prefs`` -- the :class:`PreferencesABC` instance that the
          property is bound to

        OUTPUT: one of the allowed values or ``None`` if not set

        EXAMPLES::

            sage: from sage.repl.rich_output.preferences import Property, PreferencesABC
            sage: prop = Property('foo', [0, 1, 2], 'The Foo Property')
            sage: prefs = PreferencesABC()
            sage: prop.getter(prefs) is None
            True
            sage: prop.setter(prefs, 1)
            sage: prop.getter(prefs)
            1
        """
    def setter(self, prefs, value):
        """
        Get the current value of the property.

        INPUT:

        - ``prefs`` -- the :class:`PreferencesABC` instance that the
          property is bound to

        - ``value`` -- anything. The new value of the
          property. Setting a property to ``None`` is equivalent to
          deleting the value.

        OUTPUT:

        This method does not return anything. A :exc:`ValueError` is
        raised if the given ``value`` is not one of the allowed
        values.

        EXAMPLES::

            sage: from sage.repl.rich_output.preferences import Property, PreferencesABC
            sage: prop = Property('foo', [0, 1, 2], 'The Foo Property')
            sage: prefs = PreferencesABC()
            sage: prop.getter(prefs) is None
            True
            sage: prop.setter(prefs, 1)
            sage: prop.getter(prefs)
            1

            sage: prop.setter(prefs, None)
            sage: prop.getter(prefs) is None
            True
        """
    def deleter(self, prefs) -> None:
        """
        Delete the current value of the property.

        INPUT:

        - ``prefs`` -- the :class:`PreferencesABC` instance that the
          property is bound to

        EXAMPLES::

            sage: from sage.repl.rich_output.preferences import Property, PreferencesABC
            sage: prop = Property('foo', [0, 1, 2], 'The Foo Property')
            sage: prefs = PreferencesABC()
            sage: prop.getter(prefs) is None
            True
            sage: prop.setter(prefs, 1)
            sage: prop.deleter(prefs)
            sage: prop.getter(prefs) is None
            True
        """

class PreferencesABC(SageObject):
    def __init__(self, *args, **kwds) -> None:
        """
        Preferences for displaying graphics.

        These can be preferences expressed by the user or by the
        display backend. They are specified as keyword arguments.

        INPUT:

        - ``*args*`` -- positional arguments are preferences
          instances. The property values will be inherited from left
          to right, that is, later parents override values from
          earlier parents.

        - ``**kwds`` -- keyword arguments; will be used to initialize
          properties, and override inherited values if necessary

        EXAMPLES::

            sage: from sage.repl.rich_output.preferences import DisplayPreferences
            sage: p1 = DisplayPreferences(graphics='vector')
            sage: p2 = DisplayPreferences(graphics='raster')
            sage: DisplayPreferences(p1, p2)
            Display preferences:
            * align_latex is not specified
            * graphics = raster
            * supplemental_plot is not specified
            * text is not specified

        If specified in the opposite order, the setting from ``p1`` is
        inherited::

            sage: DisplayPreferences(p2, p1)
            Display preferences:
            * align_latex is not specified
            * graphics = vector
            * supplemental_plot is not specified
            * text is not specified

        Further keywords override::

            sage: DisplayPreferences(p2, p1, graphics='disable')
            Display preferences:
            * align_latex is not specified
            * graphics = disable
            * supplemental_plot is not specified
            * text is not specified
        """
    def available_options(self):
        """
        Return the available options.

        OUTPUT:

        tuple of the preference items as instances of :class:`Property`

        EXAMPLES::

            sage: from sage.repl.rich_output.preferences import DisplayPreferences
            sage: DisplayPreferences().available_options()
            (align_latex, graphics, supplemental_plot, text)
        """

class DisplayPreferences(PreferencesABC): ...
