from typing import Any, ClassVar, overload

class WordDatatype:
    """File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 19)

        The generic WordDatatype class.

        Any word datatype must contain two attributes (at least):

        - ``_parent``
        - ``_hash``

        They are automatically defined here and it's not necessary (and forbidden)
        to define them anywhere else.

        TESTS::

            sage: w = Word([0,1,1,0,0,1])
            sage: isinstance(w, sage.combinat.words.word_datatypes.WordDatatype)
            True
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    @overload
    def __reduce__(self) -> Any:
        """WordDatatype.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 37)

        Default pickle support.

        TESTS::

            sage: w = Word([0,1,1,0,0,1])
            sage: w.__reduce__()
            (Finite words over Set of Python objects of class 'object', ([0, 1, 1, 0, 0, 1],))"""
    @overload
    def __reduce__(self) -> Any:
        """WordDatatype.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 37)

        Default pickle support.

        TESTS::

            sage: w = Word([0,1,1,0,0,1])
            sage: w.__reduce__()
            (Finite words over Set of Python objects of class 'object', ([0, 1, 1, 0, 0, 1],))"""

class WordDatatype_list(WordDatatype):
    """WordDatatype_list(parent=None, data=None)

    File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 72)

    Datatype class for words defined by lists."""
    def __init__(self, parent=..., data=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 78)

                Construct a word with a given parent.

                .. NOTE::

                   It is slower than WordDatatype_str and WordDatatype_tuple.

                INPUT:

                - ``parent`` -- an instance of :class:`Words_all`
                - ``data`` -- an iterable

                EXAMPLES::

                    sage: w = Word([0,1,1,0])
                    sage: isinstance(w, sage.combinat.words.word_datatypes.WordDatatype_list)
                    True
        """
    @overload
    def length(self) -> Any:
        """WordDatatype_list.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 197)

        Return the length of the word.

        EXAMPLES::

            sage: w = Word([0,1,1,0])
            sage: w.length()
            4"""
    @overload
    def length(self) -> Any:
        """WordDatatype_list.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 197)

        Return the length of the word.

        EXAMPLES::

            sage: w = Word([0,1,1,0])
            sage: w.length()
            4"""
    def number_of_letter_occurrences(self, a) -> Any:
        """WordDatatype_list.number_of_letter_occurrences(self, a)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 263)

        Return the number of occurrences of the letter ``a`` in the word
        ``self``.

        INPUT:

        - ``a`` -- a letter

        OUTPUT: integer

        EXAMPLES::

            sage: w = Word([0,1,1,0,1])
            sage: w.number_of_letter_occurrences(0)
            2
            sage: w.number_of_letter_occurrences(1)
            3
            sage: w.number_of_letter_occurrences(2)
            0

        .. SEEALSO::

            :meth:`sage.combinat.words.finite_word.FiniteWord_class.number_of_factor_occurrences`"""
    def __add__(self, other):
        """WordDatatype_list.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 233)

        Return the concatenation of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word represented by a list

        OUTPUT: word

        EXAMPLES::

            sage: w = Word(list(range(10)))
            sage: w * w
            word: 01234567890123456789

        The type of the concatenation is preserved::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_list'>
            sage: type(w * w)
            <class 'sage.combinat.words.word.FiniteWord_list'>"""
    def __contains__(self, a) -> Any:
        """WordDatatype_list.__contains__(self, a)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 106)

        Test whether ``a`` is a letter of ``self``.

        INPUT:

        - ``a`` -- anything

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word([0,1,1,0])
            sage: 0 in w
            True
            sage: 3 in w
            False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, key) -> Any:
        """WordDatatype_list.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 209)

        Implement :meth:`__getitem__` for words stored as lists.

        INPUT:

        - ``key`` -- integer

        EXAMPLES::

            sage: L = list(range(100))
            sage: w = Word(L)
            sage: w[4]
            4
            sage: w[-1]
            99
            sage: w[3:10:2]
            word: 3579"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    def __iter__(self) -> Any:
        """WordDatatype_list.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 126)

        Return an iterator that iterates through the letters of ``self``.

        EXAMPLES::

            sage: w = Word([0,1,1,0])
            sage: list(iter(w))
            [0, 1, 1, 0]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """WordDatatype_list.__len__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 180)

        Return the length of the word.

        .. NOTE::

           This function will be deprecated in a future version
           of Sage. Use ``self.length()`` instead.

        EXAMPLES::

            sage: w = Word([0,1,1,0])
            sage: len(w)
            4"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, other) -> Any:
        """WordDatatype_list.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 233)

        Return the concatenation of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word represented by a list

        OUTPUT: word

        EXAMPLES::

            sage: w = Word(list(range(10)))
            sage: w * w
            word: 01234567890123456789

        The type of the concatenation is preserved::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_list'>
            sage: type(w * w)
            <class 'sage.combinat.words.word.FiniteWord_list'>"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __rmul__(self, other):
        """Return value*self."""

class WordDatatype_str(WordDatatype):
    """WordDatatype_str(parent=None, data=None)

    File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 290)

    Datatype for words defined by strings."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent=..., data=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 297)

                Construct a word with parent ``parent`` from the string ``data``.

                INPUT:

                - ``parent`` -- instance of :class:`Words_all`
                - ``data`` -- string

                EXAMPLES::

                    sage: w = Word("abba")
                    sage: isinstance(w, sage.combinat.words.word_datatypes.WordDatatype_str)
                    True
        '''
    def find(self, sub, start=..., end=...) -> Any:
        '''WordDatatype_str.find(self, sub, start=0, end=None)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 431)

        Return the index of the first occurrence of sub in self,
        such that sub is contained within self[start:end].
        Returns -1 on failure.

        INPUT:

        - ``sub`` -- string or word to search for
        - ``start`` -- nonnegative integer (default: 0) specifying
          the position from which to start the search.
        - ``end`` -- nonnegative integer (default: ``None``); specifying
          the position at which the search must stop. If ``None``, then
          the search is performed up to the end of the string.

        OUTPUT: nonnegative integer or `-1`

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: w.find("a")
            0
            sage: w.find("a", 4)
            5
            sage: w.find("a", 4, 5)
            -1'''
    @overload
    def has_prefix(self, other) -> bool:
        '''WordDatatype_str.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 834)

        Test whether ``self`` has ``other`` as a prefix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.has_prefix(u)
            True
            sage: u.has_prefix(w)
            False
            sage: u.has_prefix("abbab")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.has_prefix(abba)
            False
            sage: abba.has_prefix(ab)
            True'''
    @overload
    def has_prefix(self, u) -> Any:
        '''WordDatatype_str.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 834)

        Test whether ``self`` has ``other`` as a prefix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.has_prefix(u)
            True
            sage: u.has_prefix(w)
            False
            sage: u.has_prefix("abbab")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.has_prefix(abba)
            False
            sage: abba.has_prefix(ab)
            True'''
    @overload
    def has_prefix(self, w) -> Any:
        '''WordDatatype_str.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 834)

        Test whether ``self`` has ``other`` as a prefix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.has_prefix(u)
            True
            sage: u.has_prefix(w)
            False
            sage: u.has_prefix("abbab")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.has_prefix(abba)
            False
            sage: abba.has_prefix(ab)
            True'''
    @overload
    def has_prefix(self, abba) -> Any:
        '''WordDatatype_str.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 834)

        Test whether ``self`` has ``other`` as a prefix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.has_prefix(u)
            True
            sage: u.has_prefix(w)
            False
            sage: u.has_prefix("abbab")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.has_prefix(abba)
            False
            sage: abba.has_prefix(ab)
            True'''
    @overload
    def has_prefix(self, ab) -> Any:
        '''WordDatatype_str.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 834)

        Test whether ``self`` has ``other`` as a prefix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.has_prefix(u)
            True
            sage: u.has_prefix(w)
            False
            sage: u.has_prefix("abbab")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.has_prefix(abba)
            False
            sage: abba.has_prefix(ab)
            True'''
    @overload
    def has_suffix(self, other) -> bool:
        '''WordDatatype_str.has_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 768)

        Test whether ``self`` has ``other`` as a suffix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.has_suffix(u)
            True
            sage: u.has_suffix(w)
            False
            sage: u.has_suffix("ababa")
            True'''
    @overload
    def has_suffix(self, u) -> Any:
        '''WordDatatype_str.has_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 768)

        Test whether ``self`` has ``other`` as a suffix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.has_suffix(u)
            True
            sage: u.has_suffix(w)
            False
            sage: u.has_suffix("ababa")
            True'''
    @overload
    def has_suffix(self, w) -> Any:
        '''WordDatatype_str.has_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 768)

        Test whether ``self`` has ``other`` as a suffix.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.has_suffix(u)
            True
            sage: u.has_suffix(w)
            False
            sage: u.has_suffix("ababa")
            True'''
    @overload
    def is_prefix(self, other) -> bool:
        '''WordDatatype_str.is_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 797)

        Test whether ``self`` is a prefix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.is_prefix(u)
            False
            sage: u.is_prefix(w)
            True
            sage: u.is_prefix("abbabaabababa")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.is_prefix(abba)
            True
            sage: abba.is_prefix(ab)
            False'''
    @overload
    def is_prefix(self, u) -> Any:
        '''WordDatatype_str.is_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 797)

        Test whether ``self`` is a prefix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.is_prefix(u)
            False
            sage: u.is_prefix(w)
            True
            sage: u.is_prefix("abbabaabababa")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.is_prefix(abba)
            True
            sage: abba.is_prefix(ab)
            False'''
    @overload
    def is_prefix(self, w) -> Any:
        '''WordDatatype_str.is_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 797)

        Test whether ``self`` is a prefix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.is_prefix(u)
            False
            sage: u.is_prefix(w)
            True
            sage: u.is_prefix("abbabaabababa")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.is_prefix(abba)
            True
            sage: abba.is_prefix(ab)
            False'''
    @overload
    def is_prefix(self, abba) -> Any:
        '''WordDatatype_str.is_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 797)

        Test whether ``self`` is a prefix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.is_prefix(u)
            False
            sage: u.is_prefix(w)
            True
            sage: u.is_prefix("abbabaabababa")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.is_prefix(abba)
            True
            sage: abba.is_prefix(ab)
            False'''
    @overload
    def is_prefix(self, ab) -> Any:
        '''WordDatatype_str.is_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 797)

        Test whether ``self`` is a prefix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("abbab")
            sage: w.is_prefix(u)
            False
            sage: u.is_prefix(w)
            True
            sage: u.is_prefix("abbabaabababa")
            True

        TESTS::

            sage: ab = Word(\'ab\')
            sage: abba = Word([\'a\',\'b\',\'b\',\'a\'])
            sage: ab.is_prefix(abba)
            True
            sage: abba.is_prefix(ab)
            False'''
    @overload
    def is_suffix(self, other) -> bool:
        '''WordDatatype_str.is_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 730)

        Test whether ``self`` is a suffix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True
            sage: u.is_suffix("abbabaabababa")
            True

        TESTS::

            sage: w = Word("abbabaabababa")
            sage: u = Word([\'a\',\'b\',\'a\',\'b\',\'a\'])
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True'''
    @overload
    def is_suffix(self, u) -> Any:
        '''WordDatatype_str.is_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 730)

        Test whether ``self`` is a suffix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True
            sage: u.is_suffix("abbabaabababa")
            True

        TESTS::

            sage: w = Word("abbabaabababa")
            sage: u = Word([\'a\',\'b\',\'a\',\'b\',\'a\'])
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True'''
    @overload
    def is_suffix(self, w) -> Any:
        '''WordDatatype_str.is_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 730)

        Test whether ``self`` is a suffix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True
            sage: u.is_suffix("abbabaabababa")
            True

        TESTS::

            sage: w = Word("abbabaabababa")
            sage: u = Word([\'a\',\'b\',\'a\',\'b\',\'a\'])
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True'''
    @overload
    def is_suffix(self, u) -> Any:
        '''WordDatatype_str.is_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 730)

        Test whether ``self`` is a suffix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True
            sage: u.is_suffix("abbabaabababa")
            True

        TESTS::

            sage: w = Word("abbabaabababa")
            sage: u = Word([\'a\',\'b\',\'a\',\'b\',\'a\'])
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True'''
    @overload
    def is_suffix(self, w) -> Any:
        '''WordDatatype_str.is_suffix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 730)

        Test whether ``self`` is a suffix of ``other``.

        INPUT:

        - ``other`` -- a word (an instance of :class:`Word_class`) or a
          :class:`str`

        OUTPUT: boolean

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: u = Word("ababa")
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True
            sage: u.is_suffix("abbabaabababa")
            True

        TESTS::

            sage: w = Word("abbabaabababa")
            sage: u = Word([\'a\',\'b\',\'a\',\'b\',\'a\'])
            sage: w.is_suffix(u)
            False
            sage: u.is_suffix(w)
            True'''
    @overload
    def length(self) -> Any:
        '''WordDatatype_str.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 520)

        Return the length of the word.

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: w.length()
            13'''
    @overload
    def length(self) -> Any:
        '''WordDatatype_str.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 520)

        Return the length of the word.

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: w.length()
            13'''
    def number_of_letter_occurrences(self, letter) -> Any:
        '''WordDatatype_str.number_of_letter_occurrences(self, letter)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 583)

        Count the number of occurrences of ``letter``.

        INPUT:

        - ``letter`` -- a letter

        OUTPUT: integer

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: w.number_of_letter_occurrences(\'a\')
            7
            sage: w.number_of_letter_occurrences(\'b\')
            6
            sage: w.number_of_letter_occurrences(\'c\')
            0

        ::

            sage: w.number_of_letter_occurrences(\'abb\')
            0

        .. SEEALSO::

            :meth:`sage.combinat.words.finite_word.FiniteWord_class.number_of_factor_occurrences`'''
    def partition(self, sep) -> Any:
        '''WordDatatype_str.partition(self, sep)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 684)

        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it. The concatenation of
        the terms in the list gives back the initial word.

        See also the split method.

        .. NOTE::

           This just wraps Python\'s builtin :meth:`str::partition` for
           :class:`str`.

        INPUT:

        - ``sep`` -- string or word

        EXAMPLES::

            sage: w = Word("MyTailorIsPoor")
            sage: w.partition("Tailor")
            [word: My, word: Tailor, word: IsPoor]

        ::

            sage: w = Word("3230301030323212323032321210121232121010")
            sage: l = w.partition("323")
            sage: print(l)
            [word: , word: 323, word: 0301030323212323032321210121232121010]
            sage: sum(l, Word(\'\')) == w
            True

        If the separator is not a string an error is raised::

            sage: w = Word("le papa du papa du papa etait un petit pioupiou")
            sage: w.partition(Word([\'p\',\'a\',\'p\',\'a\']))
            Traceback (most recent call last):
            ...
            ValueError: the separator must be a string'''
    def rfind(self, sub, start=..., end=...) -> Any:
        '''WordDatatype_str.rfind(self, sub, start=0, end=None)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 467)

        Return the index of the last occurrence of sub in self,
        such that sub is contained within self[start:end].
        Returns -1 on failure.

        INPUT:

        - ``sub`` -- string or word to search for
        - ``start`` -- nonnegative integer (default: 0) specifying
          the position at which the search must stop.
        - ``end`` -- nonnegative integer (default: ``None``); specifying
          the position from which to start the search. If ``None``, then
          the search is performed up to the end of the string.

        OUTPUT: nonnegative integer or `-1`

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: w.rfind("a")
            12
            sage: w.rfind("a", 4, 8)
            6
            sage: w.rfind("a", 4, 5)
            -1'''
    def split(self, sep=..., maxsplit=...) -> Any:
        '''WordDatatype_str.split(self, sep=None, maxsplit=None)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 617)

        Return a list of words, using sep as a delimiter string.
        If maxsplit is given, at most maxsplit splits are done.

        See also the partition method.

        .. NOTE::

           This just wraps Python\'s builtin :meth:`str::split` for
           :class:`str`.

        INPUT:

        - ``sep`` -- string or word (default: ``None``)

        - ``maxsplit`` -- positive integer (default: ``None``)

        OUTPUT: list of words

        EXAMPLES:

        You can split along white space to find words in a sentence::

            sage: w = Word("My tailor is poor")
            sage: w.split(" ")
            [word: My, word: tailor, word: is, word: poor]

        The python behavior is kept when no argument is given::

            sage: w.split()
            [word: My, word: tailor, word: is, word: poor]

        You can split in two words letters to get the length of blocks in the
        other letter::

            sage: w = Word("ababbabaaba")
            sage: w.split(\'a\')
            [word: , word: b, word: bb, word: b, word: , word: b, word: ]
            sage: w.split(\'b\')
            [word: a, word: a, word: , word: a, word: aa, word: a]

        You can split along words::

            sage: w = Word("3230301030323212323032321")
            sage: w.split("32")
            [word: , word: 30301030, word: , word: 12, word: 30, word: , word: 1]

        If the separator is not a string a :exc:`ValueError` is raised::

            sage: w = Word("le papa du papa du papa etait un petit pioupiou")
            sage: w.split(Word([\'p\',\'a\',\'p\',\'a\']))
            Traceback (most recent call last):
            ...
            ValueError: the separator must be a string'''
    def __add__(self, other):
        """WordDatatype_str.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 553)

        Return the concatenation of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word represented by a string

        OUTPUT: word

        EXAMPLES::

            sage: w = Word('abcdef')
            sage: w * w
            word: abcdefabcdef

        The type of the concatenation is preserved::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_str'>
            sage: type(w * w)
            <class 'sage.combinat.words.word.FiniteWord_str'>"""
    def __contains__(self, a) -> Any:
        """WordDatatype_str.__contains__(self, a)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 377)

        Test whether ``a`` is a letter of ``self``.

        INPUT:

        - ``a`` -- anything

        EXAMPLES::

            sage: w = Word('abba')
            sage: 'a' in w
            True
            sage: 'c' in w
            False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, key) -> Any:
        """WordDatatype_str.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 532)

        Implement the :meth:`__getitem__`.

        TESTS::

            sage: alphabet = [chr(i) for i in range(97, 123)]
            sage: w = Word(alphabet)
            sage: w[4]
            'e'
            sage: w[-1]
            'z'
            sage: w[3:10:2]
            word: dfhj
            sage: all(chr(i+97) == w[i] for i in range(w.length()))
            True"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    def __iter__(self) -> Any:
        """WordDatatype_str.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 321)

        Return an iterator that iterates through the letters of ``self``.

        EXAMPLES::

            sage: w = Word('abba')
            sage: list(iter(w))
            ['a', 'b', 'b', 'a']"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        '''WordDatatype_str.__len__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 503)

        Return the length of the word.

        .. NOTE::

           This function will be deprecated in a future version
           of Sage. Use ``self.length()`` instead.

        EXAMPLES::

            sage: w = Word("abbabaabababa")
            sage: len(w)
            13'''
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, other) -> Any:
        """WordDatatype_str.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 553)

        Return the concatenation of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word represented by a string

        OUTPUT: word

        EXAMPLES::

            sage: w = Word('abcdef')
            sage: w * w
            word: abcdefabcdef

        The type of the concatenation is preserved::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_str'>
            sage: type(w * w)
            <class 'sage.combinat.words.word.FiniteWord_str'>"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __rmul__(self, other):
        """Return value*self."""

class WordDatatype_tuple(WordDatatype):
    """WordDatatype_tuple(parent=None, data=None)

    File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 872)

    Datatype class for words defined by tuples."""
    def __init__(self, parent=..., data=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 878)

                Construct a word with parent ``parent`` from an iterable ``data``.

                INPUT:

                - ``parent`` -- instance of :class:`Words_all`
                - ``data`` -- iterable

                EXAMPLES::

                    sage: w = Word((0,1,1,0))
                    sage: isinstance(w, sage.combinat.words.word_datatypes.WordDatatype_tuple)
                    True
                    sage: u = Word([0,1,1,0], datatype='tuple')
                    sage: isinstance(u, sage.combinat.words.word_datatypes.WordDatatype_tuple)
                    True
        """
    @overload
    def length(self) -> Any:
        """WordDatatype_tuple.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 978)

        Return the length of the word.

        EXAMPLES::

            sage: w = Word((0,1,1,0))
            sage: w.length()
            4"""
    @overload
    def length(self) -> Any:
        """WordDatatype_tuple.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 978)

        Return the length of the word.

        EXAMPLES::

            sage: w = Word((0,1,1,0))
            sage: w.length()
            4"""
    def __add__(self, other):
        """WordDatatype_tuple.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 1036)

        Return the concatenation of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word represented by a tuple

        OUTPUT: word

        EXAMPLES::

            sage: w = Word((1,2,3,4))
            sage: w * w
            word: 12341234

        The type of the concatenation is preserved::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_tuple'>
            sage: type(w * w)
            <class 'sage.combinat.words.word.FiniteWord_tuple'>
            sage: type(w + w)
            <class 'sage.combinat.words.word.FiniteWord_tuple'>"""
    def __contains__(self, a) -> Any:
        """WordDatatype_tuple.__contains__(self, a)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 990)

        Test whether ``a`` is a letter of ``self``.

        INPUT:

        - ``a`` -- anything

        EXAMPLES::

            sage: w = Word((0,1,1,0))
            sage: 0 in w
            True
            sage: 3 in w
            False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, key) -> Any:
        """WordDatatype_tuple.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 1008)

        Implement ``__getitem__`` for words stored as tuples.

        INPUT:

        - ``key`` -- integer

        OUTPUT:

        - can be anything (an object contained in the word)

        EXAMPLES::

            sage: w = Word(tuple(range(100)))
            sage: w[4]
            4
            sage: w[-1]
            99
            sage: w[3:10:2]
            word: 3579
            sage: all(w[i] == i for i in range(100))
            True"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 49)

        Return the hash for this word.

        TESTS::

             sage: h = hash(Word('abc'))    # indirect test
             sage: Word('abc').__hash__() == Word('abc').__hash__()
             True

             sage: tm = words.ThueMorseWord()
             sage: hash(tm)
             -973965563"""
    def __iter__(self) -> Any:
        """WordDatatype_tuple.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 905)

        Return an iterator that iterates through the letters of ``self``.

        EXAMPLES::

            sage: w = Word((0,1,1,0))
            sage: list(iter(w))
            [0, 1, 1, 0]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """WordDatatype_tuple.__len__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 961)

        Return the length of the word.

        .. NOTE::

           This function will be deprecated in a future version
           of Sage. Use ``self.length()`` instead.

        EXAMPLES::

            sage: w = Word((0,1,1,0))
            sage: len(w)
            4"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, other) -> Any:
        """WordDatatype_tuple.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_datatypes.pyx (starting at line 1036)

        Return the concatenation of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word represented by a tuple

        OUTPUT: word

        EXAMPLES::

            sage: w = Word((1,2,3,4))
            sage: w * w
            word: 12341234

        The type of the concatenation is preserved::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_tuple'>
            sage: type(w * w)
            <class 'sage.combinat.words.word.FiniteWord_tuple'>
            sage: type(w + w)
            <class 'sage.combinat.words.word.FiniteWord_tuple'>"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __rmul__(self, other):
        """Return value*self."""
