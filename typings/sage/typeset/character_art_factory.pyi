from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject

class CharacterArtFactory(SageObject):
    art_type: Incomplete
    string_type: Incomplete
    magic_method_name: Incomplete
    def __init__(self, art_type, string_type, magic_method_name, parenthesis, square_bracet, curly_brace) -> None:
        """
        Abstract base class for character art factory.

        This class is the common implementation behind
        :func:`~sage.typeset.ascii_art.ascii_art` and
        :func:`~sage.typeset.unicode_art.unicode_art` .

        INPUT:

        - ``art_type`` -- type of the character art (i.e. a subclass of
          :class:`~sage.typeset.character_art.CharacterArt`)

        - ``string_type`` -- type of strings (the lines in the
          character art, e.g. ``str`` or ``unicode``)

        - ``magic_method_name`` -- name of the Sage magic method (e.g.
          ``'_ascii_art_'`` or ``'_unicode_art_'``)

        - ``parenthesis`` -- left/right pair of two multi-line
          symbols. The parenthesis, a.k.a. round brackets (used for printing
          tuples).

        - ``square_bracket`` -- left/right pair of two multi-line
          symbols. The square_brackets (used for printing lists).

        - ``curly_brace`` -- left/right pair of two multi-line
          symbols. The curly braces (used for printing sets).

        EXAMPLES::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: type(factory)
            <class 'sage.typeset.character_art_factory.CharacterArtFactory'>
        """
    def build(self, obj, baseline=None):
        """
        Construct a character art representation.

        INPUT:

        - ``obj`` -- anything; the object whose ascii art representation
          we want
        - ``baseline`` -- (optional) the baseline of the object

        OUTPUT: character art object

        EXAMPLES::

            sage: result = ascii_art(integral(exp(x+x^2)/(x+1), x))                     # needs sage.symbolic
            ...
            sage: result                                                                # needs sage.symbolic
                /
               |
               |   2
               |  x  + x
               | e
               | ------- dx
               |  x + 1
               |
              /

        TESTS::

            sage: n = var('n')                                                          # needs sage.symbolic
            sage: ascii_art(sum(binomial(2 * n, n + 1) * x^n, n, 0, oo))                # needs sage.symbolic
             /        _________    \\\n            -\\2*x + \\/ 1 - 4*x  - 1/
            -------------------------
                       _________
                 2*x*\\/ 1 - 4*x
            sage: ascii_art(list(DyckWords(3)))                                         # needs sage.combinat
            [                                   /\\   ]
            [            /\\    /\\      /\\/\\    /  \\  ]
            [ /\\/\\/\\, /\\/  \\, /  \\/\\, /    \\, /    \\ ]
            sage: ascii_art(1)
            1
        """
    def build_empty(self):
        """
        Return the empty character art object.

        OUTPUT: character art instance

        EXAMPLES::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: str(factory.build_empty())
            ''
        """
    def build_from_magic_method(self, obj, baseline=None):
        """
        Return the character art object created by the object's magic method.

        OUTPUT: character art instance

        EXAMPLES::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: out = factory.build_from_magic_method(identity_matrix(2));  out       # needs sage.modules
            [1 0]
            [0 1]
            sage: type(out)                                                             # needs sage.modules
            <class 'sage.typeset.ascii_art.AsciiArt'>
        """
    def build_from_string(self, obj, baseline: int = 0):
        """
        Return the character art object created from splitting
        the object's string representation.

        INPUT:

        - ``obj`` -- utf-8 encoded byte string or unicode
        - ``baseline`` -- (default: 0) the baseline of the object

        OUTPUT: character art instance

        EXAMPLES::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: out = factory.build_from_string('a\\nbb\\nccc')
            sage: out + out + out
            a  a  a
            bb bb bb
            ccccccccc
            sage: type(out)
            <class 'sage.typeset.ascii_art.AsciiArt'>

        TESTS::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: factory.build_from_string('à\\nbb\\nccc')  # same with unicode
            à
            bb
            ccc

            sage: a = factory.build_from_string('a\\nbb\\nccc', baseline=2)
            sage: a + ascii_art('<-')
            a  <-
            bb
            ccc
        """
    def build_container(self, content, left_border, right_border, baseline: int = 0):
        """
        Return character art for a container.

        INPUT:

        - ``content`` --
          :class:`~sage.typeset.character_art.CharacterArt`; the
          content of the container, usually comma-separated entries

        - ``left_border`` --
          :class:`~sage.typeset.symbols.CompoundSymbol`; the left
          border of the container

        - ``right_border`` --
          :class:`~sage.typeset.symbols.CompoundSymbol`; the right
          border of the container

        - ``baseline`` -- (default: 0) the baseline of the object

        TESTS::

            sage: l = ascii_art(list(DyckWords(3)))  # indirect doctest                 # needs sage.combinat
            sage: l                                                                     # needs sage.combinat
            [                                   /\\   ]
            [            /\\    /\\      /\\/\\    /  \\  ]
            [ /\\/\\/\\, /\\/  \\, /  \\/\\, /    \\, /    \\ ]
            sage: l._breakpoints                                                        # needs sage.combinat
            [9, 17, 25, 33]

        Check that zero-height strings are handled (:issue:`28527`)::

            sage: s = ascii_art(''); s.height()
            0
            sage: sage.typeset.ascii_art._ascii_art_factory.build_container(
            ....:     s,
            ....:     sage.typeset.symbols.ascii_left_parenthesis,
            ....:     sage.typeset.symbols.ascii_right_parenthesis)
            (  )
        """
    def build_set(self, s, baseline: int = 0):
        """
        Return a character art output of a set.

        TESTS:

        When the constructor is passed a set, this method is called.  Since
        iteration over sets is non-deterministic so too is the results of this
        test::

            sage: ascii_art(set(DyckWords(3)))  # indirect doctest random               # needs sage.combinat
            {                                   /\\   }
            {  /\\      /\\/\\              /\\    /  \\  }
            { /  \\/\\, /    \\, /\\/\\/\\, /\\/  \\, /    \\ }

        We can also call this method directly and pass an iterable that is not
        a set, but still obtain the same output formatting::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: factory.build_set(sorted(set(DyckWords(3))))                          # needs sage.combinat
            {                                   /\\   }
            {            /\\    /\\      /\\/\\    /  \\  }
            { /\\/\\/\\, /\\/  \\, /  \\/\\, /    \\, /    \\ }
        """
    def build_dict(self, d, baseline: int = 0):
        """
        Return a character art output of a dictionary.

        TESTS::

            sage: # needs sage.combinat
            sage: from collections import OrderedDict
            sage: d = OrderedDict(enumerate(DyckWords(3)))
            sage: art = ascii_art(d)  # indirect doctest
            sage: art
            {                                             /\\   }
            {                /\\      /\\        /\\/\\      /  \\  }
            { 0:/\\/\\/\\, 1:/\\/  \\, 2:/  \\/\\, 3:/    \\, 4:/    \\ }
            sage: art._breakpoints
            [11, 21, 31, 41]

        Check that :issue:`29447` is fixed::

            sage: ascii_art({'a': '', '': ''})
            { a:, : }
        """
    def build_list(self, l, baseline: int = 0):
        """
        Return a character art output of a list.

        TESTS::

            sage: l = ascii_art(list(DyckWords(3)))  # indirect doctest                 # needs sage.combinat
            sage: l                                                                     # needs sage.combinat
            [                                   /\\   ]
            [            /\\    /\\      /\\/\\    /  \\  ]
            [ /\\/\\/\\, /\\/  \\, /  \\/\\, /    \\, /    \\ ]
            sage: l._breakpoints                                                        # needs sage.combinat
            [9, 17, 25, 33]

        The breakpoints of the object are used as breakpoints::

            sage: l = ascii_art([DyckWords(2).list(), DyckWords(2).list()])             # needs sage.combinat
            sage: l._breakpoints                                                        # needs sage.combinat
            [(2, [7]), 17, (18, [7])]

        The parentheses only stretch as high as the content (:issue:`28527`)::

            sage: ascii_art([ascii_art('a', baseline=1)])
            [ a ]

        Line breaks inside list elements are avoided if possible
        (:issue:`29204`)::

            sage: str(ascii_art([[1..5], [1..5], [1..25], [1..5], [1..15]]))
            '[ [ 1, 2, 3, 4, 5 ], [ 1, 2, 3, 4, 5 ],\\n\\n
              [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,\\n\\n
              22, 23, 24, 25 ], [ 1, 2, 3, 4, 5 ],\\n\\n
              [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ] ]'
        """
    def build_tuple(self, t, baseline: int = 0):
        """
        Return a character art output of a tuple.

        TESTS::

            sage: ascii_art(tuple(DyckWords(3)))  # indirect doctest                    # needs sage.combinat
            (                                   /\\   )
            (            /\\    /\\      /\\/\\    /  \\  )
            ( /\\/\\/\\, /\\/  \\, /  \\/\\, /    \\, /    \\ )
        """
    def concatenate(self, iterable, separator, empty=None, baseline: int = 0, nested: bool = False):
        """
        Concatenate multiple character art instances.

        The breakpoints are set as the breakpoints of the ``separator``
        together with the breakpoints of the objects in ``iterable``.
        If there is ``None``, the end of the separator is used.

        INPUT:

        - ``iterable`` -- iterable of character art

        - ``separable`` -- character art; the separator in-between the
          iterable

        - ``empty`` -- an optional character art which is returned if
          ``iterable`` is empty

        - ``baseline`` -- (default: 0) the baseline of the object

        - ``nested`` -- boolean (default: ``False``); if ``True``, each of the
          character art objects is treated as a nested element, so that
          line breaks at the separator are preferred over line breaks inside
          the character art objects

        EXAMPLES::

            sage: i2 = identity_matrix(2)                                               # needs sage.modules
            sage: ascii_art(i2, i2, i2, sep=ascii_art(1/x))                             # needs sage.modules sage.symbolic
                 1     1
            [1 0]-[1 0]-[1 0]
            [0 1]x[0 1]x[0 1]

        TESTS::

            sage: ascii_art(['aa\\na', ascii_art('bb', baseline=1), 'c',
            ....:     'd\\ndd', ascii_art('e\\ne', baseline=1),
            ....:     ascii_art('f', baseline=-1)])
            [ aa         d      f ]
            [ a ,   , c, dd, e,   ]
            [     bb         e    ]
            sage: ascii_art([''])
            [  ]

        Check that ``empty`` is not prepended to non-empty objects
        (:issue:`28527`)::

            sage: s = 'abc'
            sage: [sage.typeset.ascii_art._ascii_art_factory.concatenate(
            ....:     s[:k], ascii_art(':'), ascii_art('0')) for k in (0..3)]
            [0, a, a:b, a:b:c]
        """
    def parse_keywords(self, kwds):
        """
        Parse the keyword input given by the dict ``kwds``.

        INPUT:

        - ``kwds`` -- dictionary

        OUTPUT:

        A triple:

        - the separator
        - the baseline
        - the baseline of the separator

        .. WARNING::

            The input is a dict, not a list of keyword arguments.

        .. NOTE::

            This will remove ``sep``/``separator`` and ``baseline``
            from ``kwds`` if they are specified.

        TESTS::

            sage: from sage.typeset.ascii_art import _ascii_art_factory as factory
            sage: d = {'sep': '2', 'baseline': 5}
            sage: factory.parse_keywords(d)
            ('2', 5, None)
            sage: d
            {}

        ::

            sage: d = {'foo': '2', 'baseline': 5}
            sage: factory.parse_keywords(d)
            (, 5, None)
            sage: d
            {'foo': '2'}

            sage: d = {'sep': '2', 'separator': '2'}
            sage: factory.parse_keywords(d)
            Traceback (most recent call last):
            ...
            ValueError: cannot specify both 'sep' and 'separator'
        """
