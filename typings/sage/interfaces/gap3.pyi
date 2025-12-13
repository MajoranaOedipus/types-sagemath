from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.interfaces.expect import Expect as Expect
from sage.interfaces.gap import GapElement_generic as GapElement_generic, Gap_generic as Gap_generic
from sage.misc.cachefunc import cached_method as cached_method

gap3_cmd: str

class Gap3(Gap_generic):
    """
    A simple Expect interface to GAP3.

    EXAMPLES::

        sage: from sage.interfaces.gap3 import Gap3
        sage: gap3 = Gap3(command='gap3')

    TESTS::

        sage: gap3(2) == gap3(3)                           #optional - gap3
        False
        sage: gap3(2) == gap3(2)                           #optional - gap3
        True
        sage: gap3._tab_completion()                       #optional - gap3
        []

    We test the interface behaves correctly after a keyboard interrupt::

        sage: gap3(2)                                      #optional - gap3
        2
        sage: try:
        ....:     gap3._keyboard_interrupt()
        ....: except KeyboardInterrupt:
        ....:     pass
        sage: gap3(2)                                      #optional - gap3
        2

    We test that the interface busts out of GAP3's break loop correctly::

        sage: f = gap3('function(L) return L[0]; end;;')   #optional - gap3
        sage: f([1,2,3])                                   #optional - gap3
        Traceback (most recent call last):
        ...
        RuntimeError: Gap3 produced error output
        Error, List Element: <position> must be a positive integer at
        return L[0] ...

    AUTHORS:

    - Franco Saliola (Feb 2010)
    """
    def __init__(self, command=...) -> None:
        """
        Initialize the GAP3 interface and start a session.

        INPUT:

        - command -- string (default: ``'gap3'``); points to the gap3
          executable on your system. By default, it is assumed the
          executable is in your path.

        EXAMPLES::

            sage: # optional - gap3
            sage: gap3 = Gap3()
            sage: gap3.is_running()
            False
            sage: gap3._start()
            sage: gap3.is_running()
            True
        """
    def help(self, topic, pager: bool = True) -> None:
        """
        Print help on the given topic.

        INPUT:

        - ``topic`` -- string

        EXAMPLES::

            sage: gap3.help('help', pager=False)           #optional - gap3
            Help _______________________________________________________...
            <BLANKLINE>
            This  section describes  together with  the following sectio...
            help system.  The help system lets you read the manual inter...

        ::

            sage: gap3.help('SymmetricGroup', pager=False) #optional - gap3
            no section with this name was found

        TESTS::

            sage: # optional - gap3
            sage: m = gap3([[1,2,3],[4,5,6]]); m
            [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
            sage: gap3.help('help', pager=False)
            Help _______________________________________________________...
            sage: m
            [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
            sage: m.Print()
            [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
            sage: gap3.help('Group', pager=False)
            Group ______________________________________________________...
            sage: m
            [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
            sage: m.Print()
            [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
        """
    def cputime(self, t=None):
        """
        Return the amount of CPU time that the GAP session has used in seconds.

        If ``t`` is not None, then it returns the difference
        between the current CPU time and ``t``.

        EXAMPLES::

            sage: # optional - gap3
            sage: t = gap3.cputime()
            sage: t  # random
            0.02
            sage: gap3.SymmetricGroup(5).Size()
            120
            sage: gap3.cputime()  # random
            0.14999999999999999
            sage: gap3.cputime(t)  # random
            0.13
        """
    def console(self) -> None:
        """
        Spawn a new GAP3 command-line session.

        EXAMPLES::

            sage: gap3.console()                             # not tested

                         ########            Lehrstuhl D fuer Mathematik
                       ###    ####           RWTH Aachen
                      ##         ##
                     ##          #             #######            #########
                    ##                        #      ##          ## #     ##
                    ##           #           #       ##             #      ##
                    ####        ##           ##       #             #      ##
                     #####     ###           ##      ##             ##    ##
                       ######### #            #########             #######
                                 #                                  #
                                ##           Version 3              #
                               ###           Release 4.4            #
                              ## #           18 Apr 97              #
                             ##  #
                            ##   #  Alice Niemeyer, Werner Nickel,  Martin Schoenert
                           ##    #  Johannes Meier, Alex Wegner,    Thomas Bischops
                          ##     #  Frank Celler,   Juergen Mnich,  Udo Polis
                          ###   ##  Thomas Breuer,  Goetz Pfeiffer, Hans U. Besche
                           ######   Volkmar Felsch, Heiko Theissen, Alexander Hulpke
                                    Ansgar Kaup,    Akos Seress,    Erzsebet Horvath
                                    Bettina Eick
                                    For help enter: ?<return>
            gap>
        """

gap3: Incomplete

class GAP3Element(GapElement_generic):
    """
    A GAP3 element.

    .. NOTE::

        If the corresponding GAP3 element is a GAP3 record,
        then the class is changed to a ``GAP3Record``.

    INPUT:

    - ``parent`` -- the GAP3 session

    - ``value`` -- the GAP3 command as a string

    - ``is_name`` -- boolean (default: ``False``); if ``True``, then ``value`` is
      the variable name for the object

    - ``name`` -- string (default: ``None``); the variable name to use for the
      object. If ``None``, then a variable name is generated

    .. NOTE::

        If you pass ``E``, ``X`` or ``Z`` for ``name``, then an error is
        raised because these are sacred variable names in GAP3 that should
        never be redefined. Sage raises an error because GAP3 does not!

    EXAMPLES::

        sage: # optional - gap3
        sage: from sage.interfaces.gap3 import GAP3Element
        sage: gap3 = Gap3()
        sage: GAP3Element(gap3, value='3+2')
        5
        sage: GAP3Element(gap3, value='sage0', is_name=True)
        5

    TESTS::

        sage: GAP3Element(gap3, value='3+2', is_name=False, name='X') #optional - gap3
        Traceback (most recent call last):
        ...
        ValueError: you are attempting to redefine X; but you should never redefine E, X or Z in gap3 (because things will break!)

    AUTHORS:

    - Franco Saliola (Feb 2010)
    """
    __class__: Incomplete
    def __init__(self, parent, value, is_name: bool = False, name=None) -> None:
        """
        See ``GAP3Element`` for full documentation.

        EXAMPLES::

            sage: # optional - gap3
            sage: from sage.interfaces.gap3 import GAP3Element
            sage: gap3 = Gap3()
            sage: GAP3Element(gap3, value='3+2')
            5
            sage: GAP3Element(gap3, value='sage0', is_name=True)
            5

        TESTS::

            sage: GAP3Element(gap3, value='3+2', is_name=False, name='X') #optional - gap3
            Traceback (most recent call last):
            ...
            ValueError: you are attempting to redefine X; but you should never redefine E, X or Z in gap3 (because things will break!)
        """
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: # optional - gap3
            sage: l = gap3('[1,2,3]')
            sage: l[1]
            1
            sage: a = gap3([1,2,3])
            sage: a[1]
            1
            sage: m = gap3([[1,2,3],[4,5,6],[7,8,9]])
            sage: m[1,3]
            3
            sage: m[2][1]
            4
        """

class GAP3Record(GAP3Element):
    """
    A GAP3 record.

    .. NOTE::

        This class should not be called directly, use GAP3Element instead.
        If the corresponding GAP3 element is a GAP3 record, then the class
        is changed to a ``GAP3Record``.

    AUTHORS:

    - Franco Saliola (Feb 2010)
    """
    def recfields(self):
        """
        Return a list of the fields for the record. (Record fields are akin
        to object attributes in Sage.)

        OUTPUT: list of strings -- the field records

        EXAMPLES::

            sage: S5 = gap3.SymmetricGroup(5)              #optional - gap3
            sage: S5.recfields()                           #optional - gap3
            ['isDomain', 'isGroup', 'identity', 'generators',
             'operations', 'isPermGroup', 'isFinite', '1', '2',
             '3', '4', 'degree']
            sage: S5.degree                                      #optional - gap3
            5
        """
    def operations(self):
        """
        Return a list of the GAP3 operations for the record.

        OUTPUT: list of strings -- operations of the record

        EXAMPLES::

            sage: S5 = gap3.SymmetricGroup(5)              #optional - gap3
            sage: S5.operations()                          #optional - gap3
            [..., 'NormalClosure', 'NormalIntersection', 'Normalizer',
            'NumberConjugacyClasses', 'PCore', 'Radical', 'SylowSubgroup',
            'TrivialSubgroup', 'FusionConjugacyClasses', 'DerivedSeries', ...]
            sage: S5.DerivedSeries()                       #optional - gap3
            [ Group( (1,5), (2,5), (3,5), (4,5) ),
              Subgroup( Group( (1,5), (2,5), (3,5), (4,5) ),
                        [ (1,2,5), (1,3,5), (1,4,5) ] ) ]
        """
    def __getattr__(self, attrname):
        """
        OUTPUT:

        - ``GAP3Record`` -- if ``attrname`` is a field of the GAP record

        - ``ExpectFunction`` -- if ``attrname`` is the name of a GAP3 function

        EXAMPLES::

            sage: # optional - gap3
            sage: S5 = gap3.SymmetricGroup(5)
            sage: S5.__getattr__('Size')
            Size
            sage: gap3.IsFunc(S5.__getattr__('Size'))
            true
            sage: S5.__getattr__('generators')
            [ (1,5), (2,5), (3,5), (4,5) ]
        """

def gap3_console() -> None:
    """
    Spawn a new GAP3 command-line session.

    EXAMPLES::

        sage: gap3.console()                             # not tested

                     ########            Lehrstuhl D fuer Mathematik
                   ###    ####           RWTH Aachen
                  ##         ##
                 ##          #             #######            #########
                ##                        #      ##          ## #     ##
                ##           #           #       ##             #      ##
                ####        ##           ##       #             #      ##
                 #####     ###           ##      ##             ##    ##
                   ######### #            #########             #######
                             #                                  #
                            ##           Version 3              #
                           ###           Release 4.4            #
                          ## #           18 Apr 97              #
                         ##  #
                        ##   #  Alice Niemeyer, Werner Nickel,  Martin Schoenert
                       ##    #  Johannes Meier, Alex Wegner,    Thomas Bischops
                      ##     #  Frank Celler,   Juergen Mnich,  Udo Polis
                      ###   ##  Thomas Breuer,  Goetz Pfeiffer, Hans U. Besche
                       ######   Volkmar Felsch, Heiko Theissen, Alexander Hulpke
                                Ansgar Kaup,    Akos Seress,    Erzsebet Horvath
                                Bettina Eick
                                For help enter: ?<return>
        gap>
    """
def gap3_version():
    """
    Return the version of GAP3 that you have in your PATH on your computer.

    EXAMPLES::

        sage: gap3_version()                                           # random, optional - gap3
        'lib: v3r4p4 1997/04/18, src: v3r4p0 1994/07/10, sys: usg gcc ansi'
    """
