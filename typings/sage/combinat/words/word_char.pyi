import _cython_3_2_1
import sage.combinat.words.word_datatypes
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

reversed_word_iterator: _cython_3_2_1.cython_function_or_method

class WordDatatype_char(sage.combinat.words.word_datatypes.WordDatatype):
    """WordDatatype_char(parent, data)

    File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 53)

    A Fast class for words represented by an array ``unsigned char *``.

    Currently, only handles letters in [0,255]."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, data) -> Any:
        """File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 82)

                Constructor.

                TESTS::

                    sage: W = Words([0,1,2,3])
                    sage: W([0,1,2,3])
                    word: 0123
                    sage: W(iter([0,1,2,3]))
                    word: 0123
        """
    def concatenate(self, other) -> Any:
        """WordDatatype_char.concatenate(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 483)

        Concatenation of ``self`` and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,2,1]).concatenate([0,0,0])
            word: 021000

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1]).concatenate(W([0,0,0]))
            sage: type(w) is W.finite_words()._element_classes['char']
            True"""
    @overload
    def has_prefix(self, other) -> bool:
        """WordDatatype_char.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 585)

        Test whether ``other`` is a prefix of ``self``.

        INPUT:

        - ``other`` -- a word or a sequence (e.g. tuple, list)

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: w = W([0,1,1,0,1,2,0])
            sage: w.has_prefix([0,1,1])
            True
            sage: w.has_prefix([0,1,2])
            False
            sage: w.has_prefix(w)
            True
            sage: w.has_prefix(w[:-1])
            True
            sage: w.has_prefix(w[1:])
            False

        TESTS:

        :issue:`19322`::

            sage: W = Words([0,1,2])
            sage: w = W([0,1,0,2])
            sage: w.has_prefix(words.FibonacciWord())
            False

            sage: w.has_prefix([0,1,0,2,0])
            False
            sage: w.has_prefix([0,1,0,2])
            True
            sage: w.has_prefix([0,1,0])
            True"""
    @overload
    def has_prefix(self, w) -> Any:
        """WordDatatype_char.has_prefix(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 585)

        Test whether ``other`` is a prefix of ``self``.

        INPUT:

        - ``other`` -- a word or a sequence (e.g. tuple, list)

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: w = W([0,1,1,0,1,2,0])
            sage: w.has_prefix([0,1,1])
            True
            sage: w.has_prefix([0,1,2])
            False
            sage: w.has_prefix(w)
            True
            sage: w.has_prefix(w[:-1])
            True
            sage: w.has_prefix(w[1:])
            False

        TESTS:

        :issue:`19322`::

            sage: W = Words([0,1,2])
            sage: w = W([0,1,0,2])
            sage: w.has_prefix(words.FibonacciWord())
            False

            sage: w.has_prefix([0,1,0,2,0])
            False
            sage: w.has_prefix([0,1,0,2])
            True
            sage: w.has_prefix([0,1,0])
            True"""
    @overload
    def is_empty(self) -> Any:
        """WordDatatype_char.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 141)

        Return whether the word is empty.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,2,2]).is_empty()
            False
            sage: W([]).is_empty()
            True"""
    @overload
    def is_empty(self) -> Any:
        """WordDatatype_char.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 141)

        Return whether the word is empty.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,2,2]).is_empty()
            False
            sage: W([]).is_empty()
            True"""
    @overload
    def is_empty(self) -> Any:
        """WordDatatype_char.is_empty(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 141)

        Return whether the word is empty.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,2,2]).is_empty()
            False
            sage: W([]).is_empty()
            True"""
    @overload
    def is_square(self) -> bool:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """WordDatatype_char.is_square(self) -> bool

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 647)

        Return ``True`` if ``self`` is a square, and ``False`` otherwise.

        EXAMPLES::

            sage: w = Word([n % 4 for n in range(48)], alphabet=[0,1,2,3])
            sage: w.is_square()
            True

        ::

            sage: w = Word([n % 4 for n in range(49)], alphabet=[0,1,2,3])
            sage: w.is_square()
            False
            sage: (w*w).is_square()
            True

        TESTS:

        The above tests correspond to the present class (char)::

            sage: type(w)
            <class 'sage.combinat.words.word.FiniteWord_char'>

        ::

            sage: Word([], alphabet=[0,1]).is_square()
            True
            sage: Word([0], alphabet=[0,1]).is_square()
            False
            sage: Word([0,0], alphabet=[0,1]).is_square()
            True"""
    @overload
    def length(self) -> Any:
        """WordDatatype_char.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 170)

        Return the length of the word as a Sage integer.

        EXAMPLES::

            sage: W = Words([0,1,2,3,4])
            sage: w = W([0,1,2,0,3,2,1])
            sage: w.length()
            7
            sage: type(w.length())
            <class 'sage.rings.integer.Integer'>
            sage: type(len(w))
            <class 'int'>"""
    @overload
    def length(self) -> Any:
        """WordDatatype_char.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 170)

        Return the length of the word as a Sage integer.

        EXAMPLES::

            sage: W = Words([0,1,2,3,4])
            sage: w = W([0,1,2,0,3,2,1])
            sage: w.length()
            7
            sage: type(w.length())
            <class 'sage.rings.integer.Integer'>
            sage: type(len(w))
            <class 'int'>"""
    @overload
    def length(self) -> Any:
        """WordDatatype_char.length(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 170)

        Return the length of the word as a Sage integer.

        EXAMPLES::

            sage: W = Words([0,1,2,3,4])
            sage: w = W([0,1,2,0,3,2,1])
            sage: w.length()
            7
            sage: type(w.length())
            <class 'sage.rings.integer.Integer'>
            sage: type(len(w))
            <class 'int'>"""
    @overload
    def letters(self) -> Any:
        """WordDatatype_char.letters(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 187)

        Return the list of letters that appear in this word, listed in the
        order of first appearance.

        EXAMPLES::

            sage: W = Words(5)
            sage: W([1,3,1,2,2,3,1]).letters()
            [1, 3, 2]"""
    @overload
    def letters(self) -> Any:
        """WordDatatype_char.letters(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 187)

        Return the list of letters that appear in this word, listed in the
        order of first appearance.

        EXAMPLES::

            sage: W = Words(5)
            sage: W([1,3,1,2,2,3,1]).letters()
            [1, 3, 2]"""
    @overload
    def longest_common_prefix(self, other) -> Any:
        '''WordDatatype_char.longest_common_prefix(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 690)

        Return the longest common prefix of this word and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,2]).longest_common_prefix([0,1])
            word: 01
            sage: u = W([0,1,0,0,1])
            sage: v = W([0,1,0,2])
            sage: u.longest_common_prefix(v)
            word: 010
            sage: v.longest_common_prefix(u)
            word: 010

        Using infinite words is also possible (and the return type is also a
        of the same type as ``self``)::

            sage: W([0,1,0,0]).longest_common_prefix(words.FibonacciWord())
            word: 0100
            sage: type(_)
            <class \'sage.combinat.words.word.FiniteWord_char\'>

        An example of an intensive usage::

            sage: W = Words([0,1])
            sage: w = words.FibonacciWord()
            sage: w = W(list(w[:5000]))
            sage: L = [[len(w[n:].longest_common_prefix(w[n+fibonacci(i):]))            # needs sage.libs.pari
            ....:      for i in range(5,15)] for n in range(1,1000)]
            sage: for n,l in enumerate(L):                                              # needs sage.libs.pari
            ....:     if l.count(0) > 4:
            ....:         print("{} {}".format(n+1,l))
            375 [0, 13, 0, 34, 0, 89, 0, 233, 0, 233]
            376 [0, 12, 0, 33, 0, 88, 0, 232, 0, 232]
            608 [8, 0, 21, 0, 55, 0, 144, 0, 377, 0]
            609 [7, 0, 20, 0, 54, 0, 143, 0, 376, 0]
            985 [0, 13, 0, 34, 0, 89, 0, 233, 0, 610]
            986 [0, 12, 0, 33, 0, 88, 0, 232, 0, 609]

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1,0,0,1])
            sage: w.longest_common_prefix(0)
            Traceback (most recent call last):
            ...
            TypeError: unsupported input 0

        ::

            sage: Word([2,2], (1,2)).longest_common_prefix([])
            word:'''
    @overload
    def longest_common_prefix(self, v) -> Any:
        '''WordDatatype_char.longest_common_prefix(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 690)

        Return the longest common prefix of this word and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,2]).longest_common_prefix([0,1])
            word: 01
            sage: u = W([0,1,0,0,1])
            sage: v = W([0,1,0,2])
            sage: u.longest_common_prefix(v)
            word: 010
            sage: v.longest_common_prefix(u)
            word: 010

        Using infinite words is also possible (and the return type is also a
        of the same type as ``self``)::

            sage: W([0,1,0,0]).longest_common_prefix(words.FibonacciWord())
            word: 0100
            sage: type(_)
            <class \'sage.combinat.words.word.FiniteWord_char\'>

        An example of an intensive usage::

            sage: W = Words([0,1])
            sage: w = words.FibonacciWord()
            sage: w = W(list(w[:5000]))
            sage: L = [[len(w[n:].longest_common_prefix(w[n+fibonacci(i):]))            # needs sage.libs.pari
            ....:      for i in range(5,15)] for n in range(1,1000)]
            sage: for n,l in enumerate(L):                                              # needs sage.libs.pari
            ....:     if l.count(0) > 4:
            ....:         print("{} {}".format(n+1,l))
            375 [0, 13, 0, 34, 0, 89, 0, 233, 0, 233]
            376 [0, 12, 0, 33, 0, 88, 0, 232, 0, 232]
            608 [8, 0, 21, 0, 55, 0, 144, 0, 377, 0]
            609 [7, 0, 20, 0, 54, 0, 143, 0, 376, 0]
            985 [0, 13, 0, 34, 0, 89, 0, 233, 0, 610]
            986 [0, 12, 0, 33, 0, 88, 0, 232, 0, 609]

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1,0,0,1])
            sage: w.longest_common_prefix(0)
            Traceback (most recent call last):
            ...
            TypeError: unsupported input 0

        ::

            sage: Word([2,2], (1,2)).longest_common_prefix([])
            word:'''
    @overload
    def longest_common_prefix(self, u) -> Any:
        '''WordDatatype_char.longest_common_prefix(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 690)

        Return the longest common prefix of this word and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,2]).longest_common_prefix([0,1])
            word: 01
            sage: u = W([0,1,0,0,1])
            sage: v = W([0,1,0,2])
            sage: u.longest_common_prefix(v)
            word: 010
            sage: v.longest_common_prefix(u)
            word: 010

        Using infinite words is also possible (and the return type is also a
        of the same type as ``self``)::

            sage: W([0,1,0,0]).longest_common_prefix(words.FibonacciWord())
            word: 0100
            sage: type(_)
            <class \'sage.combinat.words.word.FiniteWord_char\'>

        An example of an intensive usage::

            sage: W = Words([0,1])
            sage: w = words.FibonacciWord()
            sage: w = W(list(w[:5000]))
            sage: L = [[len(w[n:].longest_common_prefix(w[n+fibonacci(i):]))            # needs sage.libs.pari
            ....:      for i in range(5,15)] for n in range(1,1000)]
            sage: for n,l in enumerate(L):                                              # needs sage.libs.pari
            ....:     if l.count(0) > 4:
            ....:         print("{} {}".format(n+1,l))
            375 [0, 13, 0, 34, 0, 89, 0, 233, 0, 233]
            376 [0, 12, 0, 33, 0, 88, 0, 232, 0, 232]
            608 [8, 0, 21, 0, 55, 0, 144, 0, 377, 0]
            609 [7, 0, 20, 0, 54, 0, 143, 0, 376, 0]
            985 [0, 13, 0, 34, 0, 89, 0, 233, 0, 610]
            986 [0, 12, 0, 33, 0, 88, 0, 232, 0, 609]

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1,0,0,1])
            sage: w.longest_common_prefix(0)
            Traceback (most recent call last):
            ...
            TypeError: unsupported input 0

        ::

            sage: Word([2,2], (1,2)).longest_common_prefix([])
            word:'''
    @overload
    def longest_common_suffix(self, other) -> Any:
        """WordDatatype_char.longest_common_suffix(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 779)

        Return the longest common suffix between this word and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,2]).longest_common_suffix([2,0,2])
            word: 02
            sage: u = W([0,1,0,0,1])
            sage: v = W([1,2,0,0,1])
            sage: u.longest_common_suffix(v)
            word: 001
            sage: v.longest_common_suffix(u)
            word: 001

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1,0,0,1])
            sage: w.longest_common_suffix(0)
            Traceback (most recent call last):
            ...
            TypeError: unsupported input 0

        ::

            sage: Word([2,2], (1,2)).longest_common_suffix([])
            word:"""
    @overload
    def longest_common_suffix(self, v) -> Any:
        """WordDatatype_char.longest_common_suffix(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 779)

        Return the longest common suffix between this word and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,2]).longest_common_suffix([2,0,2])
            word: 02
            sage: u = W([0,1,0,0,1])
            sage: v = W([1,2,0,0,1])
            sage: u.longest_common_suffix(v)
            word: 001
            sage: v.longest_common_suffix(u)
            word: 001

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1,0,0,1])
            sage: w.longest_common_suffix(0)
            Traceback (most recent call last):
            ...
            TypeError: unsupported input 0

        ::

            sage: Word([2,2], (1,2)).longest_common_suffix([])
            word:"""
    @overload
    def longest_common_suffix(self, u) -> Any:
        """WordDatatype_char.longest_common_suffix(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 779)

        Return the longest common suffix between this word and ``other``.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,2]).longest_common_suffix([2,0,2])
            word: 02
            sage: u = W([0,1,0,0,1])
            sage: v = W([1,2,0,0,1])
            sage: u.longest_common_suffix(v)
            word: 001
            sage: v.longest_common_suffix(u)
            word: 001

        TESTS::

            sage: W = Words([0,1,2])
            sage: w = W([0,2,1,0,0,1])
            sage: w.longest_common_suffix(0)
            Traceback (most recent call last):
            ...
            TypeError: unsupported input 0

        ::

            sage: Word([2,2], (1,2)).longest_common_suffix([])
            word:"""
    def __add__(self, other) -> Any:
        """WordDatatype_char.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 471)

        Concatenation (alias for ``*``).

        TESTS::

            sage: W = Words([0,1,2])
            sage: type(W([0]) + W([1])) is W.finite_words()._element_classes['char']
            True"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, key) -> Any:
        """WordDatatype_char.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 331)

        INPUT:

        - ``key`` -- index

        TESTS::

            sage: W = Words([0,1,2,3])
            sage: w = W([0,1,0,2,0,3,1,2,3])
            sage: w[0]
            0
            sage: w[2]
            0
            sage: w[1:]
            word: 10203123
            sage: w[5::-2]
            word: 321

            sage: w = W([randint(0,3) for _ in range(20)])
            sage: list(w) == [w[i] for i in range(len(w))]
            True

            sage: w['foo':'bar']
            Traceback (most recent call last):
            ...
            TypeError: slice indices must be integers or None or have an __index__ method

        Check a weird behavior of PySlice_GetIndicesEx (:issue:`17056`)::

            sage: w[1:0]
            word:"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype_char.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 227)

        Return the hash value.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,1,0,0,0], datatype='list').__hash__()
            102060647
            sage: W([0,1,0,1,0,0,0], datatype='char').__hash__()
            102060647"""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype_char.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 227)

        Return the hash value.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,1,0,0,0], datatype='list').__hash__()
            102060647
            sage: W([0,1,0,1,0,0,0], datatype='char').__hash__()
            102060647"""
    @overload
    def __hash__(self) -> Any:
        """WordDatatype_char.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 227)

        Return the hash value.

        EXAMPLES::

            sage: W = Words([0,1,2])
            sage: W([0,1,0,1,0,0,0], datatype='list').__hash__()
            102060647
            sage: W([0,1,0,1,0,0,0], datatype='char').__hash__()
            102060647"""
    def __iter__(self) -> Any:
        """WordDatatype_char.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 395)

        Iterator over the letters of ``self``.

        EXAMPLES::

            sage: W = Words([0,1,2,3])
            sage: list(W([0,0,1,0]))  # indirect doctest
            [0, 0, 1, 0]"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """WordDatatype_char.__len__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 155)

        Return the length of the word as a Python integer.

        TESTS::

            sage: W = Words([0,1,2,3])
            sage: w = W([0,1,2,0,3,2,1])
            sage: len(w)
            7
            sage: type(len(w))
            <class 'int'>"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, other) -> Any:
        """WordDatatype_char.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 439)

        Concatenation of ``self`` and ``other``.

        TESTS:

            sage: W = Words(IntegerRange(0,255))
            sage: W([0,1]) * W([2,0])
            word: 0120

        The result is automatically converted to a WordDatatype_char. Currently we can
        even do::

            sage: w = W([0,1,2,3])
            sage: w * [4,0,4,0]
            word: 01234040"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __pow__(self, exp, mod) -> Any:
        """WordDatatype_char.__pow__(self, exp, mod)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 502)

        Power.

        INPUT:

        - ``exp`` -- integer, rational, float, or plus infinity

        TESTS::

            sage: W = Words(range(20))
            sage: w = W([0,1,2,3])
            sage: w
            word: 0123
            sage: w ** (1/2)
            word: 01
            sage: w ** 2
            word: 01230123
            sage: w ** 3
            word: 012301230123
            sage: w ** (7/2)
            word: 01230123012301
            sage: len(((w ** 2) ** 3) ** 5) == len(w) * 2 * 3 * 5
            True

        Infinite exponents::

            sage: W([0,1]) ** Infinity
            word: 0101010101010101010101010101010101010101..."""
    def __radd__(self, other):
        """Return value+self."""
    def __reversed__(self) -> Any:
        """WordDatatype_char.__reversed__(self)

        File: /build/sagemath/src/sage/src/sage/combinat/words/word_char.pyx (starting at line 409)

        Reversed iterator over the letters of ``self``.

        EXAMPLES::

            sage: W = Words([0,1,2,3])
            sage: list(reversed(W([0,0,1,0]))) # indirect doctest
            [0, 1, 0, 0]

        TESTS::

            sage: list(reversed(W([])))
            []
            sage: list(reversed(W([1])))
            [1]"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
