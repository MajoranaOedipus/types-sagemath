from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.words.word_options import word_options as word_options
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp_item as richcmp_item, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class Word_class(SageObject):
    def parent(self):
        """
        Return the parent of ``self``.

        TESTS::

            sage: Word(iter([1,2,3]), length='unknown').parent()
            Finite words over Set of Python objects of class 'object'
            sage: Word(range(12)).parent()
            Finite words over Set of Python objects of class 'object'
            sage: Word(range(4), alphabet=list(range(6))).parent()
            Finite words over {0, 1, 2, 3, 4, 5}
            sage: Word(iter('abac'), alphabet='abc').parent()
            Finite words over {'a', 'b', 'c'}
        """
    def string_rep(self):
        '''
        Return the (truncated) raw sequence of letters as a string.

        EXAMPLES::

            sage: Word(\'abbabaab\').string_rep()
            \'abbabaab\'
            sage: Word([0, 1, 0, 0, 1]).string_rep()
            \'01001\'
            sage: Word([0,1,10,101]).string_rep()
            \'0,1,10,101\'
            sage: WordOptions(letter_separator=\'-\')
            sage: Word([0,1,10,101]).string_rep()
            \'0-1-10-101\'
            sage: WordOptions(letter_separator=\',\')

        TESTS:

        Insertion in a str::

            sage: from itertools import count
            sage: w = Word((i % 5 for i in count()), length=\'unknown\')
            sage: "w = %s in this string." % w
            \'w = 0123401234012340123401234012340123401234... in this string.\'

        Using LatexExpr::

            sage: from sage.misc.latex import LatexExpr
            sage: LatexExpr(w)
            0123401234012340123401234012340123401234...

        With the print statement::

            sage: print(w)
            0123401234012340123401234012340123401234...

        Truncation is done for possibly infinite words::

            sage: print(w)
            0123401234012340123401234012340123401234...
        '''
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.words.word import Word_class
            sage: w = Word_class()
            sage: w.__iter__()
            Traceback (most recent call last):
            ...
            NotImplementedError: you need to define an iterator in __iter__
        """
    def length(self):
        """
        Return the length of ``self``.

        TESTS::

            sage: from sage.combinat.words.word import Word_class
            sage: w = Word(iter('abba'*100), length='unknown')
            sage: w.length() is None
            True
            sage: w = Word(iter('abba'), length='finite')
            sage: w.length()
            4
            sage: w = Word(iter([0,1,1,0,1,0,0,1]*100), length='unknown')
            sage: w.length() is None
            True
            sage: w = Word(iter([0,1,1,0,1,0,0,1]), length='finite')
            sage: w.length()
            8
        """
    def is_finite(self):
        """
        Return whether this word is known to be finite.

        .. WARNING::

            A word defined by an iterator such that its end has
            never been reached will returns False.

        EXAMPLES::

            sage: Word([]).is_finite()
            True
            sage: Word('a').is_finite()
            True
            sage: TM = words.ThueMorseWord()
            sage: TM.is_finite()
            False

        ::

            sage: w = Word(iter('a'*100))
            sage: w.is_finite()
            False
        """
    def __len__(self) -> int:
        """
        Return the length of ``self`` (as a Python integer).

        .. NOTE::

            For infinite words or words of unknown length,
            use `length()` method instead.

        OUTPUT: positive integer

        EXAMPLES::

            sage: len(Word(lambda n:n, length=1000))
            1000
            sage: len(Word(iter('a'*200), length='finite'))
            200

        We make sure :issue:`8574` is fixed::

            sage: s = WordMorphism('0->000,1->%s'%('1'*100))
            sage: len(s('1'))
            100

        For infinite words::

            sage: len(Word(lambda n:n))
            Traceback (most recent call last):
            ...
            TypeError: Python len method cannot return a non integer value (=+Infinity): use length method instead.
            sage: len(Word(iter('a'*200)))
            Traceback (most recent call last):
            ...
            TypeError: Python len method cannot return a non integer value (=None): use length method instead.

        For words of unknown length::

            sage: len(Word(iter('a'*200), length='unknown'))
            Traceback (most recent call last):
            ...
            TypeError: Python len method cannot return a non integer value (=None): use length method instead.
        """
    def __richcmp__(self, other, op):
        """
        Compare two words lexicographically according to the ordering
        defined by the parent of ``self``.

        This corresponds to Python's built-in
        ordering when no parent nor alphabet was used to defined the word.

        Provides for all normal comparison operators.

        .. NOTE::

            This function will not terminate if ``self`` and ``other``
            are equal infinite words!

        EXAMPLES::

            sage: W = Word
            sage: from itertools import count
            sage: W(range(1,10)) > W(range(10))
            True
            sage: W(range(10)) < W(range(1,10))
            True
            sage: W(range(10)) == W(range(10))
            True
            sage: W(range(10)) < W(count())
            True
            sage: W(count()) > W(range(10))
            True

        ::

            sage: W = Words(['a', 'b', 'c'])
            sage: W('a') > W([])
            True
            sage: W([]) < W('a')
            True

            sage: Word('abc') == Word(['a','b','c'])
            True
            sage: Words([0,1])([0,1,0,1]) == Words([0,1])([0,1,0,1])
            True
            sage: Words([0,1])([0,1,0,1]) == Words([0,1])([0,1,0,0])
            False

        It works even when parents are not the same::

            sage: Words([0,1,2])([0,1,0,1]) ==  Words([0,1])([0,1,0,1])
            True
            sage: Word('ababa') == Words('abcd')('ababa')
            True

        Or when one word is finite while the other is infinite::

            sage: Word(range(20)) == Word(lambda n:n)
            False
            sage: Word(lambda n:n) == Word(range(20))
            False

        Beware the following does not halt! ::

            sage: from itertools import count
            sage: Word(lambda n:n) == Word(count()) #not tested

        Examples for unequality::

            sage: w = Word(range(10))
            sage: z = Word(range(10))
            sage: w != z
            False
            sage: u = Word(range(12))
            sage: u != w
            True

        TESTS::

            sage: Word(count())[:20] == Word(range(20))
            True
            sage: Word(range(20)) == Word(count())[:20]
            True
            sage: Word(range(20)) == Word(lambda n:n)[:20]
            True
            sage: Word(range(20)) == Word(lambda n:n,length=20)
            True
        """
    def longest_common_prefix(self, other, length: str = 'unknown'):
        '''
        Return the longest common prefix of ``self`` and ``other``.

        INPUT:

        - ``other`` -- word

        - ``length`` -- string (default: ``\'unknown\'``)
          the length type of the resulting word if known. It may be one of
          the following:

          - ``\'unknown\'``
          - ``\'finite\'``
          - ``\'infinite\'``

        EXAMPLES::

            sage: f = lambda n : add(Integer(n).digits(2)) % 2
            sage: t = Word(f)
            sage: u = t[:10]
            sage: t.longest_common_prefix(u)
            word: 0110100110

        The longest common prefix of two equal infinite words::

            sage: t1 = Word(f)
            sage: t2 = Word(f)
            sage: t1.longest_common_prefix(t2)
            word: 0110100110010110100101100110100110010110...

        Useful to study the approximation of an infinite word::

            sage: a = 0.618
            sage: g = words.CodingOfRotationWord(alpha=a, beta=1-a, x=a)
            sage: f = words.FibonacciWord()
            sage: p = f.longest_common_prefix(g, length=\'finite\')
            sage: p.length()
            231

        TESTS::

            sage: w = Word(\'12345\')
            sage: y = Word(\'1236777\')
            sage: w.longest_common_prefix(y)
            word: 123
            sage: w.longest_common_prefix(w)
            word: 12345
            sage: y.longest_common_prefix(w)
            word: 123
            sage: y.longest_common_prefix(y)
            word: 1236777
            sage: Word().longest_common_prefix(w)
            word:
            sage: w.longest_common_prefix(Word())
            word:
            sage: w.longest_common_prefix(w[:3])
            word: 123
            sage: Word("11").longest_common_prefix(Word("1"))
            word: 1
            sage: Word("1").longest_common_prefix(Word("11"))
            word: 1

        With infinite words::

            sage: t = words.ThueMorseWord(\'ab\')
            sage: u = t[:10]
            sage: u.longest_common_prefix(t)
            word: abbabaabba
            sage: u.longest_common_prefix(u)
            word: abbabaabba

        Check length::

            sage: w1 = Word(iter(\'ab\'*200))
            sage: w2 = Word(iter(\'bcd\'*200))
            sage: w1.longest_common_prefix(w2, length=19)
            Traceback (most recent call last):
            ...
            ValueError: invalid argument length (=19)
        '''
    def longest_periodic_prefix(self, period: int = 1):
        """
        Return the longest prefix of ``self`` having the given period.

        INPUT:

        - ``period`` -- positive integer (default: 1)

        OUTPUT: word

        EXAMPLES::

            sage: Word([]).longest_periodic_prefix()
            word:
            sage: Word([1]).longest_periodic_prefix()
            word: 1
            sage: Word([1,2]).longest_periodic_prefix()
            word: 1
            sage: Word([1,1,2]).longest_periodic_prefix()
            word: 11
            sage: Word([1,2,1,2,1,3]).longest_periodic_prefix(2)
            word: 12121
            sage: type(_)
            <class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>
            sage: Word(lambda n:0).longest_periodic_prefix()
            word: 0000000000000000000000000000000000000000...
        """
    def is_empty(self):
        """
        Return ``True`` if the length of ``self`` is zero, and ``False`` otherwise.

        EXAMPLES::

            sage: it = iter([])
            sage: Word(it).is_empty()
            True
            sage: it = iter([1,2,3])
            sage: Word(it).is_empty()
            False
            sage: from itertools import count
            sage: Word(count()).is_empty()
            False
        """
    def to_integer_word(self):
        '''
        Return a word over the integers whose letters are those output by
        self._to_integer_iterator()

        EXAMPLES::

            sage: from itertools import count
            sage: w = Word(count()); w
            word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
            sage: w.to_integer_word()
            word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
            sage: w = Word(iter("abbacabba"), length=\'finite\'); w
            word: abbacabba
            sage: w.to_integer_word()
            word: 011020110
            sage: w = Word(iter("abbacabba"), length=\'unknown\'); w
            word: abbacabba
            sage: w.to_integer_word()
            word: 011020110
        '''
    def lex_less(self, other):
        '''
        Return ``True`` if ``self`` is lexicographically less than ``other``.

        EXAMPLES::

            sage: w = Word([1,2,3])
            sage: u = Word([1,3,2])
            sage: v = Word([3,2,1])
            sage: w.lex_less(u)
            True
            sage: v.lex_less(w)
            False
            sage: a = Word("abba")
            sage: b = Word("abbb")
            sage: a.lex_less(b)
            True
            sage: b.lex_less(a)
            False

        For infinite words::

            sage: t = words.ThueMorseWord()
            sage: t.lex_less(t[:10])
            False
            sage: t[:10].lex_less(t)
            True
        '''
    def lex_greater(self, other):
        '''
        Return ``True`` if ``self`` is lexicographically greater than ``other``.

        EXAMPLES::

            sage: w = Word([1,2,3])
            sage: u = Word([1,3,2])
            sage: v = Word([3,2,1])
            sage: w.lex_greater(u)
            False
            sage: v.lex_greater(w)
            True
            sage: a = Word("abba")
            sage: b = Word("abbb")
            sage: a.lex_greater(b)
            False
            sage: b.lex_greater(a)
            True

        For infinite words::

            sage: t = words.ThueMorseWord()
            sage: t[:10].lex_greater(t)
            False
            sage: t.lex_greater(t[:10])
            True
        '''
    def apply_morphism(self, morphism):
        '''
        Return the word obtained by applying the morphism to ``self``.

        INPUT:

        - ``morphism`` -- can be an instance of WordMorphism, or
          anything that can be used to construct one

        EXAMPLES::

            sage: w = Word("ab")
            sage: d = {\'a\':\'ab\', \'b\':\'ba\'}
            sage: w.apply_morphism(d)
            word: abba
            sage: w.apply_morphism(WordMorphism(d))
            word: abba

        ::

            sage: w = Word(\'ababa\')
            sage: d = dict(a=\'ab\', b=\'ba\')
            sage: d
            {\'a\': \'ab\', \'b\': \'ba\'}
            sage: w.apply_morphism(d)
            word: abbaabbaab

        For infinite words::

            sage: t = words.ThueMorseWord([0,1]); t
            word: 0110100110010110100101100110100110010110...
            sage: t.apply_morphism({0:8,1:9})
            word: 8998988998898998988989988998988998898998...
        '''
    def delta(self):
        """
        Return the image of ``self`` under the delta morphism.

        This is the word composed of the length of consecutive runs of
        the same letter in a given word.

        OUTPUT: word over integers

        EXAMPLES:

        For finite words::

            sage: W = Words('0123456789')
            sage: W('22112122').delta()
            word: 22112
            sage: W('555008').delta()
            word: 321
            sage: W().delta()
            word:
            sage: Word('aabbabaa').delta()
            word: 22112

        For infinite words::

            sage: t = words.ThueMorseWord()
            sage: t.delta()
            word: 1211222112112112221122211222112112112221...
        """
    def iterated_right_palindromic_closure(self, f=None, algorithm: str = 'recursive'):
        """
        Return the iterated (`f`-)palindromic closure of ``self``.

        INPUT:

        - ``f`` -- involution (default: ``None``) on the alphabet of ``self``;
          it must be callable on letters as well as words (e.g. WordMorphism)

        - ``algorithm`` -- string (default: ``'recursive'``); specifying which
          algorithm to be used when computing the iterated palindromic closure.
          It must be one of the two following values:

          - ``'definition'`` -- computed using the definition
          - ``'recursive'`` -- computation based on an efficient formula
            that recursively computes the iterated right palindromic closure
            without having to recompute the longest `f`-palindromic suffix
            at each iteration [2].

        OUTPUT: word; the iterated (`f`-)palindromic closure of ``self``

        EXAMPLES::

            sage: Word('123').iterated_right_palindromic_closure()
            word: 1213121

        ::

            sage: w = Word('abc')
            sage: w.iterated_right_palindromic_closure()
            word: abacaba

        ::

            sage: w = Word('aaa')
            sage: w.iterated_right_palindromic_closure()
            word: aaa

        ::

            sage: w = Word('abbab')
            sage: w.iterated_right_palindromic_closure()
            word: ababaabababaababa

        A right `f`-palindromic closure::

            sage: f = WordMorphism('a->b,b->a')
            sage: w = Word('abbab')
            sage: w.iterated_right_palindromic_closure(f=f)
            word: abbaabbaababbaabbaabbaababbaabbaab

        An infinite word::

            sage: t = words.ThueMorseWord('ab')
            sage: t.iterated_right_palindromic_closure()
            word: ababaabababaababaabababaababaabababaabab...

        There are two implementations computing the iterated right
        `f`-palindromic closure, the latter being much more efficient::

            sage: w = Word('abaab')
            sage: u = w.iterated_right_palindromic_closure(algorithm='definition')
            sage: v = w.iterated_right_palindromic_closure(algorithm='recursive')
            sage: u
            word: abaabaababaabaaba
            sage: u == v
            True
            sage: w = words.RandomWord(8)
            sage: u = w.iterated_right_palindromic_closure(algorithm='definition')
            sage: v = w.iterated_right_palindromic_closure(algorithm='recursive')
            sage: u == v
            True

        TESTS:

        The empty word::

            sage: w = Word()
            sage: w.iterated_right_palindromic_closure()
            word:

        The length-`1` word::

            sage: Word('1').iterated_right_palindromic_closure()
            word: 1

        If the word is finite, so is the result::

            sage: w = Word([0,1]*7)
            sage: c = w.iterated_right_palindromic_closure()
            sage: type(c)
            <class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>

        REFERENCES:

        -   [1] A. de Luca, A. De Luca, Pseudopalindrome closure operators
            in free monoids, Theoret. Comput. Sci. 362 (2006) 282--300.
        -   [2] J. Justin, Episturmian morphisms and a Galois theorem on
            continued fractions, RAIRO Theoret. Informatics Appl. 39 (2005)
            207-215.
        """
    def prefixes_iterator(self, max_length=None) -> Generator[Incomplete]:
        """
        Return an iterator over the prefixes of ``self``.

        INPUT:

        - ``max_length`` -- nonnegative integer or ``None`` (default); the
          maximum length of the prefixes

        OUTPUT: iterator

        EXAMPLES::

            sage: w = Word('abaaba')
            sage: for p in w.prefixes_iterator(): p
            word:
            word: a
            word: ab
            word: aba
            word: abaa
            word: abaab
            word: abaaba
            sage: for p in w.prefixes_iterator(max_length=3): p
            word:
            word: a
            word: ab
            word: aba

        You can iterate over the prefixes of an infinite word::

            sage: f = words.FibonacciWord()
            sage: for p in f.prefixes_iterator(max_length=8): p
            word:
            word: 0
            word: 01
            word: 010
            word: 0100
            word: 01001
            word: 010010
            word: 0100101
            word: 01001010

        TESTS::

            sage: list(f.prefixes_iterator(max_length=0))
            [word: ]
        """
    def palindrome_prefixes_iterator(self, max_length=None) -> Generator[Incomplete]:
        """
        Return an iterator over the palindrome prefixes of ``self``.

        INPUT:

        - ``max_length`` -- nonnegative integer or ``None`` (default); the
          maximum length of the prefixes

        OUTPUT: iterator

        EXAMPLES::

            sage: w = Word('abaaba')
            sage: for pp in w.palindrome_prefixes_iterator(): pp
            word:
            word: a
            word: aba
            word: abaaba
            sage: for pp in w.palindrome_prefixes_iterator(max_length=4): pp
            word:
            word: a
            word: aba

        You can iterate over the palindrome prefixes of an infinite word::

            sage: f = words.FibonacciWord()
            sage: for pp in f.palindrome_prefixes_iterator(max_length=20): pp
            word:
            word: 0
            word: 010
            word: 010010
            word: 01001010010
            word: 0100101001001010010
        """
    def partial_sums(self, start, mod=None):
        """
        Return the word defined by the partial sums of its prefixes.

        INPUT:

        - ``self`` -- a word over the integers
        - ``start`` -- integer; the first letter of the resulting word
        - ``mod`` -- (default: ``None``) it can be one of the following:
            - None or 0 : result is over the integers
            - integer : result is over the integers modulo ``mod``.

        EXAMPLES::

            sage: w = Word(range(10))
            sage: w.partial_sums(0)
            word: 0,0,1,3,6,10,15,21,28,36,45
            sage: w.partial_sums(1)
            word: 1,1,2,4,7,11,16,22,29,37,46

        ::

            sage: w = Word([1,2,3,1,2,3,2,2,2,2])
            sage: w.partial_sums(0, mod=None)
            word: 0,1,3,6,7,9,12,14,16,18,20
            sage: w.partial_sums(0, mod=0)
            word: 0,1,3,6,7,9,12,14,16,18,20
            sage: w.partial_sums(0, mod=8)
            word: 01367146024
            sage: w.partial_sums(0, mod=4)
            word: 01323102020
            sage: w.partial_sums(0, mod=2)
            word: 01101100000
            sage: w.partial_sums(0, mod=1)
            word: 00000000000

        TESTS:

        If the word is infinite, so is the result::

            sage: w = Word(lambda n:1)
            sage: u = w.partial_sums(0)
            sage: type(u)
            <class 'sage.combinat.words.word.InfiniteWord_iter_with_caching'>
        """
    def finite_differences(self, mod=None):
        """
        Return the word obtained by the differences of consecutive letters
        of ``self``.

        INPUT:

        - ``self`` -- a word over the integers
        - ``mod`` -- (default: ``None``) it can be one of the following:
            - None or 0 : result is over the integers
            - integer : result is over the integers modulo ``mod``.

        EXAMPLES::

            sage: w = Word([x^2 for x in range(10)])
            sage: w.finite_differences()
            word: 1,3,5,7,9,11,13,15,17
            sage: w.finite_differences(mod=4)
            word: 131313131
            sage: w.finite_differences(mod=0)
            word: 1,3,5,7,9,11,13,15,17

        TESTS::

            sage: w = Word([2,3,6])
            sage: w.finite_differences()
            word: 13
            sage: w = Word([2,6])
            sage: w.finite_differences()
            word: 4
            sage: w = Word([2])
            sage: w.finite_differences()
            word:
            sage: w = Word()
            sage: w.finite_differences()
            word:

        If the word is infinite, so is the result::

            sage: w = Word(lambda n:n)
            sage: u = w.finite_differences()
            sage: u
            word: 1111111111111111111111111111111111111111...
            sage: type(u)
            <class 'sage.combinat.words.word.InfiniteWord_iter_with_caching'>
        """
    def sum_digits(self, base: int = 2, mod=None):
        """
        Return the sequence of the sum modulo ``mod`` of the digits written
        in base ``base`` of ``self``.

        INPUT:

        - ``self`` -- word over natural numbers

        - ``base`` -- integer (default: 2) greater or equal to 2

        - ``mod`` -- modulo (default: ``None``); can take the following
          values:
          - ``integer`` -- the modulo
          - ``None`` -- the value ``base`` is considered for the modulo

        EXAMPLES:

        The Thue-Morse word::

            sage: from itertools import count
            sage: Word(count()).sum_digits()
            word: 0110100110010110100101100110100110010110...

        Sum of digits modulo 2 of the prime numbers written in base 2::

            sage: Word(primes(1000)).sum_digits()                                       # needs sage.libs.pari
            word: 1001110100111010111011001011101110011011...

        Sum of digits modulo 3 of the prime numbers written in base 3::

            sage: Word(primes(1000)).sum_digits(base=3)                                 # needs sage.libs.pari
            word: 2100002020002221222121022221022122111022...
            sage: Word(primes(1000)).sum_digits(base=3, mod=3)                          # needs sage.libs.pari
            word: 2100002020002221222121022221022122111022...

        Sum of digits modulo 2 of the prime numbers written in base 3::

            sage: Word(primes(1000)).sum_digits(base=3, mod=2)                          # needs sage.libs.pari
            word: 0111111111111111111111111111111111111111...

        Sum of digits modulo 7 of the prime numbers written in base 10::

            sage: Word(primes(1000)).sum_digits(base=10, mod=7)                         # needs sage.libs.pari
            word: 2350241354435041006132432241353546006304...

        Negative entries::

            sage: w = Word([-1,0,1,2,3,4,5])
            sage: w.sum_digits()
            Traceback (most recent call last):
            ...
            NotImplementedError: nth digit of Thue-Morse word is not implemented for negative value of n

        TESTS:

        The Thue-Morse word::

            sage: from itertools import count
            sage: w = Word(count()).sum_digits()
            sage: t = words.ThueMorseWord()
            sage: w[:100]  == t[:100]
            True

        ::

            sage: type(Word(range(10)).sum_digits())
            <class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>
        """
    def first_occurrence(self, other, start: int = 0):
        """
        Return the position of the first occurrence of ``other`` in ``self``.

        If ``other`` is not a factor of ``self``, it returns ``None``
        or loops forever when ``self`` is an infinite word.

        INPUT:

        - ``other`` -- a finite word
        - ``start`` -- integer (default: `0`) where the search starts

        OUTPUT: integer or ``None``

        EXAMPLES::

            sage: w = Word('01234567890123456789')
            sage: w.first_occurrence(Word('3456'))
            3
            sage: w.first_occurrence(Word('3456'), start=7)
            13

        When the factor is not present, ``None`` is returned::

            sage: w.first_occurrence(Word('3456'), start=17) is None
            True
            sage: w.first_occurrence(Word('3333')) is None
            True

        Also works for searching a finite word in an infinite word::

            sage: w = Word('0123456789')^oo
            sage: w.first_occurrence(Word('3456'))
            3
            sage: w.first_occurrence(Word('3456'), start=1000)
            1003

        But it will loop for ever if the factor is not found::

            sage: w.first_occurrence(Word('3333')) # not tested -- infinite loop

        The empty word occurs in a word::

            sage: Word('123').first_occurrence(Word(''), 0)
            0
            sage: Word('').first_occurrence(Word(''), 0)
            0
        """
    def factor_occurrences_iterator(self, fact) -> Generator[Incomplete]:
        """
        Return an iterator over all occurrences (including overlapping ones)
        of fact in ``self`` in their order of appearance.

        INPUT:

        - ``fact`` -- a non empty finite word

        OUTPUT: iterator

        EXAMPLES::

            sage: TM = words.ThueMorseWord()
            sage: fact = Word([0,1,1,0,1])
            sage: it = TM.factor_occurrences_iterator(fact)
            sage: next(it)
            0
            sage: next(it)
            12
            sage: next(it)
            24

        ::

            sage: u = Word('121')
            sage: w = Word('121213211213')
            sage: list(w.factor_occurrences_iterator(u))
            [0, 2, 8]
        """
    def return_words_iterator(self, fact) -> Generator[Incomplete]:
        """
        Return an iterator over all the return words of fact in self
        (without unicity).

        INPUT:

        - ``fact`` -- a non empty finite word

        OUTPUT: iterator

        EXAMPLES::

            sage: w = Word('baccabccbacbca')
            sage: b = Word('b')
            sage: list(w.return_words_iterator(b))
            [word: bacca, word: bcc, word: bac]

        ::

            sage: TM = words.ThueMorseWord()
            sage: fact = Word([0,1,1,0,1])
            sage: it = TM.return_words_iterator(fact)
            sage: next(it)
            word: 011010011001
            sage: next(it)
            word: 011010010110
            sage: next(it)
            word: 0110100110010110
            sage: next(it)
            word: 01101001
            sage: next(it)
            word: 011010011001
            sage: next(it)
            word: 011010010110
        """
    def complete_return_words_iterator(self, fact) -> Generator[Incomplete]:
        """
        Return an iterator over all the complete return words of fact in
        ``self`` (without unicity).

        A complete return words `u` of a factor `v`  is a factor starting
        by the given factor `v` and ending just after the next occurrence
        of this factor `v`. See for instance [1].

        INPUT:

        - ``fact`` -- a non empty finite word

        OUTPUT: iterator

        EXAMPLES::

            sage: TM = words.ThueMorseWord()
            sage: fact = Word([0,1,1,0,1])
            sage: it = TM.complete_return_words_iterator(fact)
            sage: next(it)
            word: 01101001100101101
            sage: next(it)
            word: 01101001011001101
            sage: next(it)
            word: 011010011001011001101
            sage: next(it)
            word: 0110100101101
            sage: next(it)
            word: 01101001100101101
            sage: next(it)
            word: 01101001011001101

        REFERENCES:

        -   [1] J. Justin, L. Vuillon, Return words in Sturmian and
            episturmian words, Theor. Inform. Appl. 34 (2000) 343--356.
        """
