from _typeshed import Incomplete
from sage.misc.instancedoc import instancedoc as instancedoc

class Option:
    """
    An option.

    Each option for an options class is an instance of this class which
    implements the magic that allows the options to the attributes of the
    options class that can be looked up, set and called.

    By way of example, this class implements the following functionality.

    EXAMPLES::

        sage: # needs sage.combinat
        sage: Partitions.options.display
        list
        sage: Partitions.options.display = 'compact'
        sage: Partitions.options.display('list')
        sage: Partitions.options._reset()

    TESTS::

        sage: TestSuite(Partitions.options.display).run()                               # needs sage.combinat
    """
    __doc__: Incomplete
    def __init__(self, options, name) -> None:
        '''
        Initialise an option by settings its ``name``, "parent" option class
        ``options`` and doc-string.

        EXAMPLES::

            sage: type(Partitions.options.display)    # indirect doctest                # needs sage.combinat
            <class \'sage.structure.global_options.Option\'>
        '''
    def __add__(self, other):
        """
        Return the object obtained by adding ``self`` and ``other``, where
        ``self`` behaves like its value.

        EXAMPLES::

            sage: Tableaux.options.convention + ' is good'                              # needs sage.combinat
            'English is good'
        """
    def __radd__(self, other):
        """
        Return the object obtained by adding ``other`` and ``self``, where
        ``self`` behaves like its value.

        EXAMPLES::

            sage: 'Good ' + Tableaux.options.convention                                 # needs sage.combinat
            'Good English'
        """
    def __mul__(self, other):
        """
        Return the object obtained by adding ``self`` and ``other``, where
        ``self`` behaves like its value.

        EXAMPLES::

            sage: Tableaux.options.convention + ' is good'                              # needs sage.combinat
            'English is good'
        """
    def __rmul__(self, other):
        """
        Return the object obtained by r-adding ``other`` and ``self``, where
        ``self`` behaves like its value.

        EXAMPLES::

            sage: 'Good ' + Tableaux.options.convention                                 # needs sage.combinat
            'Good English'
        """
    def __bool__(self) -> bool:
        """
        Return the value of this option interpreted as a boolean.

        EXAMPLES::

            sage: # needs sage.combinat sage.graphs sage.modules
            sage: RiggedConfigurations.options.half_width_boxes_type_B
            True
            sage: 'yes' if RiggedConfigurations.options.half_width_boxes_type_B else 'no'
            'yes'
            sage: RiggedConfigurations.options.half_width_boxes_type_B = False
            sage: 'yes' if RiggedConfigurations.options.half_width_boxes_type_B else 'no'
            'no'
            sage: RiggedConfigurations.options._reset()
        """
    def __call__(self, *args, **kwds):
        '''
        Get or set value of the option ``self``.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: Partitions.options.display()       # indirect doctest
            \'list\'
            sage: Partitions.options.display(\'exp\')  # indirect doctest
            sage: Partitions.options.display()       # indirect doctest
            \'exp_low\'
            sage: Partitions.options._reset()

        TESTS:

        Check that values can be set to ``None`` (:issue:`30763`)::

            sage: from sage.structure.global_options import GlobalOptions
            sage: class config(GlobalOptions):
            ....:     size = dict(default=42,
            ....:                 description=\'integer or None\',
            ....:                 checker=lambda val: val is None or val >= 0)
            sage: config.size()
            42
            sage: config.size(None)
            sage: config.size() is None
            True
            sage: config._reset()

        Check the deprecation::

            sage: config.size(value=None)
            doctest:...: DeprecationWarning: keyword argument "value" should be replaced by positional argument
            See https://github.com/sagemath/sage/issues/30763 for details.
            sage: config.size() is None
            True
            sage: config.size(1, 2)
            Traceback (most recent call last):
            ...
            TypeError: option takes at most one argument "value"
            sage: config.size(unknown=3)
            Traceback (most recent call last):
            ...
            TypeError: option takes at most one argument "value"
            sage: config.size(4, value=5)
            Traceback (most recent call last):
            ...
            TypeError: option takes at most one argument "value"
        '''
    def __eq__(self, other):
        '''
        Equality testing for an option in based on the value of the attribute.

        EXAMPLES::

            sage: Tableaux.options.convention                                           # needs sage.combinat
            English
            sage: Tableaux.options.convention == "English"                              # needs sage.combinat
            True
            sage: Tableaux.options.convention == "French"                               # needs sage.combinat
            False
        '''
    def __ne__(self, other):
        '''
        Inequality testing for an option in based on the value of
        the attribute.

        EXAMPLES::

            sage: Tableaux.options.convention                                           # needs sage.combinat
            English
            sage: Tableaux.options.convention != "English"                              # needs sage.combinat
            False
            sage: Tableaux.options.convention != "French"                               # needs sage.combinat
            True
        '''
    def __hash__(self):
        """
        Return the hash of ``self``, which is the hash of the corresponding
        value.

        EXAMPLES::

            sage: hash(Tableaux.options.convention) == hash(Tableaux.options('convention'))         # needs sage.combinat
            True
        """

class GlobalOptionsMetaMeta(type):
    def __call__(self, name, bases, dict):
        '''
        Called when subclassing an instance of ``self``.

        Python translates ``class C(B): ...`` to
        ``meta = type(B); C = meta("C", (B,), ...)``.
        If we want to intercept this call ``meta(...)``, we need to
        customize ``__call__`` in the metaclass of ``meta``, which is
        this metametaclass.

        EXAMPLES::

            sage: from sage.structure.global_options import GlobalOptions
            sage: type(GlobalOptions)
            <class \'sage.structure.global_options.GlobalOptionsMeta\'>
            sage: type(type(GlobalOptions))
            <class \'sage.structure.global_options.GlobalOptionsMetaMeta\'>
            sage: class G(GlobalOptions): pass
            sage: type(G)
            <class \'sage.structure.global_options.GlobalOptions\'>

        Since ``G`` is constructed using ``class`` syntax, the object
        gets a ``__module__`` attribute, different from the
        ``__module__`` attribute of its type (:class:`GlobalOptions`)::

            sage: G.__module__
            \'__main__\'
            sage: type(G).__module__
            \'sage.structure.global_options\'

        Multiple base classes are not allowed::

            sage: class G(GlobalOptions, object): pass
            Traceback (most recent call last):
            ...
            TypeError: GlobalOptions must be the only base class
        '''

class GlobalOptionsMeta(type, metaclass=GlobalOptionsMetaMeta):
    """
    Metaclass for :class:`GlobalOptions`.

    This class is itself an instance of :class:`GlobalOptionsMetaMeta`,
    which implements the subclass magic.
    """

class GlobalOptions(metaclass=GlobalOptionsMeta):
    '''
    The :class:`GlobalOptions` class is a generic class for setting and
    accessing global options for Sage objects.

    While it is possible to create instances of :class:`GlobalOptions`
    the usual way, the recommended syntax is to subclass from
    ``GlobalOptions``. Thanks to some metaclass magic, this actually
    creates an instance of ``GlobalOptions`` instead of a subclass.

    INPUT (as "attributes" of the class):

    - ``NAME`` -- specifies a name for the options class (optional;
      default: class name)

    - ``module`` -- gives the module that contains the associated options class

    - ``option_class`` -- gives the name of the associated module class
      (default: ``NAME``)

    - option = ``dict(...)`` -- dictionary specifying an option

    The options are specified by keyword arguments with their values
    being a dictionary which describes the option. The
    allowed/expected keys in the dictionary are:

    - ``alias`` -- defines alias/synonym for option values
    - ``alt_name`` -- alternative name for an option
    - ``checker`` -- a function for checking whether a particular value for
      the option is valid
    - ``default`` -- the default value of the option
    - ``description`` -- documentation string
    - ``link_to`` -- links to an option for this set of options to an
      option in another :class:`GlobalOptions`
    - ``setter`` -- a function (class method) which is called whenever this
      option changes
    - ``values`` -- dictionary of the legal values for this option (this
      automatically defines the corresponding ``checker``); this dictionary
      gives the possible options, as keys, together with a brief description
      of them
    - ``case_sensitive`` -- boolean (default: ``True``); depending on whether
      the values of the option are case sensitive

    Options and their values can be abbreviated provided that this
    abbreviation is a prefix of a unique option.

    EXAMPLES::

        sage: from sage.structure.global_options import GlobalOptions
        sage: class Menu():
        ....:     class options(GlobalOptions):
        ....:         \'\'\'
        ....:         Fancy documentation
        ....:         -------------------
        ....:
        ....:         @OPTIONS@
        ....:
        ....:         End of Fancy documentation
        ....:         \'\'\'
        ....:         NAME = \'menu\'
        ....:         entree = dict(default=\'soup\',
        ....:                     description=\'The first course of a meal\',
        ....:                     values=dict(soup=\'soup of the day\', bread=\'oven baked\'),
        ....:                     alias=dict(rye=\'bread\'))
        ....:         appetizer = dict(alt_name=\'entree\')
        ....:         main = dict(default=\'pizza\', description=\'Main meal\',
        ....:                   values=dict(pizza=\'thick crust\', pasta=\'penne arrabiata\'),
        ....:                   case_sensitive=False)
        ....:         dessert = dict(default=\'espresso\', description=\'Dessert\',
        ....:                      values=dict(espresso=\'life begins again\',
        ....:                                  cake=\'waist begins again\',
        ....:                                  cream=\'fluffy white stuff\'))
        ....:         tip = dict(default=10, description=\'Reward for good service\',
        ....:                  checker=lambda tip: tip in range(20))
        sage: Menu.options
        Current options for menu
          - dessert: espresso
          - entree:  soup
          - main:    pizza
          - tip:     10
        sage: Menu.options(entree=\'s\')         # unambiguous abbreviations are allowed
        sage: Menu.options(t=15)
        sage: (Menu.options[\'tip\'], Menu.options(\'t\'))
        (15, 15)
        sage: Menu.options()
        Current options for menu
          - dessert: espresso
          - entree:  soup
          - main:    pizza
          - tip:     15
        sage: Menu.options._reset(); Menu.options()
        Current options for menu
          - dessert: espresso
          - entree:  soup
          - main:    pizza
          - tip:     10
        sage: Menu.options.tip=40
        Traceback (most recent call last):
        ...
        ValueError: 40 is not a valid value for tip in the options for menu
        sage: Menu.options(m=\'p\')           # ambiguous abbreviations are not allowed
        Traceback (most recent call last):
        ...
        ValueError: p is not a valid value for main in the options for menu

    The documentation for the options class is automatically generated from the
    information which specifies the options:

    .. CODE-BLOCK:: text

        Fancy documentation
        -------------------

        OPTIONS:

        - dessert:  (default: espresso)
          Dessert

          - ``cake``     -- waist begins again
          - ``cream``    -- fluffy white stuff
          - ``espresso`` -- life begins again

        - entree:  (default: soup)
          The first course of a meal

          - ``bread`` -- oven baked
          - ``rye``   -- alias for bread
          - ``soup``  -- soup of the day

        - main:  (default: pizza)
          Main meal

          - ``pasta`` -- penne arrabiata
          - ``pizza`` -- thick crust

        - tip:  (default: 10)
          Reward for good service

        End of Fancy documentation

        See :class:`~sage.structure.global_options.GlobalOptions` for more features of these options.

    The possible values for an individual option can be obtained by
    (trying to) set it equal to \'?\'::

        sage: Menu.options(des=\'?\')
        - ``dessert`` -- (default: ``espresso``)
          Dessert
        <BLANKLINE>
          - ``cake``     -- waist begins again
          - ``cream``    -- fluffy white stuff
          - ``espresso`` -- life begins again
        <BLANKLINE>
        Current value: espresso
    '''
    def __init__(self, NAME=None, module: str = '', option_class: str = '', doc: str = '', end_doc: str = '', **options) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: from sage.structure.global_options import GlobalOptions
            sage: class menu(GlobalOptions):
            ....:     entree = dict(default=\'soup\',
            ....:                 description=\'The first course of a meal\',
            ....:                 values=dict(soup=\'soup of the day\', bread=\'oven baked\'),
            ....:                 alias=dict(rye=\'bread\'))
            ....:     appetizer = dict(alt_name=\'entree\')
            ....:     main = dict(default=\'pizza\', description=\'Main meal\',
            ....:               values=dict(pizza=\'thick crust\', pasta=\'penne arrabiata\'),
            ....:               case_sensitive=False)
            ....:     dessert = dict(default=\'espresso\', description=\'Dessert\',
            ....:                  values=dict(espresso=\'life begins again\',
            ....:                              cake=\'waist begins again\',
            ....:                              cream=\'fluffy white stuff\'))
            ....:     tip = dict(default=10, description=\'Reward for good service\',
            ....:              checker=lambda tip: tip in range(20))
            sage: menu._name  # Default name is class name
            \'menu\'
            sage: class specials(GlobalOptions):
            ....:     entree = dict(link_to=(menu, \'entree\'))
            ....:     main_specials = dict(default=\'salmon\', description=\'main course specials\',
            ....:                   values=dict(salmon=\'a fish\', crab=\'Sebastian\'))
            sage: specials[\'entree\'] = \'rye\'
            sage: menu[\'entree\']
            \'bread\'

            sage: class alias_test(GlobalOptions):
            ....:       "Test aliases with case sensitivity"
            ....:       test_opt = dict(default=\'Upper\',
            ....:           description = \'Starts with an uppercase\',
            ....:           values = dict(Upper="Starts with uppercase",
            ....:                         lower="only lowercase"),
            ....:           case_sensitive = False,
            ....:           alias = dict(UpperAlias=\'Upper\', lower_alias=\'lower\'))
            sage: alias_test[\'test_opt\'] = \'Lower_Alias\'
            sage: alias_test[\'test_opt\']
            \'lower\'
            sage: alias_test[\'test_opt\'] = \'upperalias\'
            sage: alias_test[\'test_opt\']
            \'Upper\'
        '''
    def __call__(self, *get_value, **set_value):
        """
        Get or set value of the option ``option``.

        EXAMPLES::

            sage: from sage.structure.global_options import GlobalOptions
            sage: class FoodOptions(GlobalOptions):
            ....:     NAME = 'daily meal'
            ....:     food = dict(default='apple', values=dict(apple='a fruit', pair='of what?'))
            ....:     drink = dict(default='water', values=dict(water='a drink', coffee='a lifestyle'))
            ....:     beverage = dict(alt_name='drink')
            sage: FoodOptions()
            Current options for daily meal
              - drink: water
              - food:  apple
            sage: FoodOptions('food')
            'apple'
            sage: FoodOptions(food='pair'); FoodOptions()
            Current options for daily meal
              - drink: water
              - food:  pair
            sage: FoodOptions('beverage')
            'water'
            sage: FoodOptions(food='apple', drink='coffee'); FoodOptions()
            Current options for daily meal
              - drink: coffee
              - food:  apple
        """
    def __getitem__(self, option):
        """
        Return the current value of the option ``option``.

        EXAMPLES::

            sage: from sage.structure.global_options import GlobalOptions
            sage: class FoodOptions(GlobalOptions):
            ....:     NAME = 'daily meal'
            ....:     food = dict(default='apple', values=dict(apple='a fruit', pair='of what?'))
            ....:     drink = dict(default='water', values=dict(water='a drink', coffee='a lifestyle'))
            sage: FoodOptions['drink']
            'water'
            sage: FoodOptions['d']
            'water'
        """
    def __setitem__(self, option, value) -> None:
        """
        The ``__setitem__`` method is used to change the current values of the
        options. It also checks that the supplied options are valid and changes
        any alias to its generic value.

        EXAMPLES::

            sage: from sage.structure.global_options import GlobalOptions
            sage: class FoodOptions(GlobalOptions):
            ....:     NAME = 'daily meal'
            ....:     food = dict(default='apple', values=dict(apple='a fruit', pair='of what?'))
            ....:     drink = dict(default='water', values=dict(water='a drink', coffee='a lifestyle'))
            sage: FoodOptions['drink']='coffee'; FoodOptions()
            Current options for daily meal
              - drink: coffee
              - food:  apple
            sage: FoodOptions(drink='w'); FoodOptions()
            Current options for daily meal
              - drink: water
              - food:  apple
            sage: FoodOptions(drink='?')
            - ``drink`` -- (default: ``water``)
            <BLANKLINE>
              - ``coffee`` -- a lifestyle
              - ``water``  -- a drink
            <BLANKLINE>
            Current value: water
        """
    def __setattr__(self, name, value=None):
        '''
        Set the attribute ``name`` of the option class ``self`` equal to
        ``value``, if the attribute ``name`` exists.

        As the attributes of an option class are the actual options we need
        to be able to "trap" invalid options in a sensible way. We do this
        by sending any "non-standard" to :meth:`__setitem__` for processing.

        EXAMPLES::

            sage: Partitions.options.display = \'exp\'                                    # needs sage.combinat
            sage: Partitions.options.dispplay = \'list\'                                  # needs sage.combinat
            Traceback (most recent call last):
            ...
            ValueError: dispplay is not an option for Partitions
            sage: Partitions.options._reset()                                           # needs sage.combinat
        '''
    def __eq__(self, other):
        """
        Two options classes are equal if they return the same :meth:`__getstate__`.

        EXAMPLES::

            sage: Partitions.options == PartitionsGreatestLE.options  # indirect doctest            # needs sage.combinat
            True
            sage: Partitions.options == Tableaux.options                                # needs sage.combinat
            False
        """
