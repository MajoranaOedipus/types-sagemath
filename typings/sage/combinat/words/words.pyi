from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.combinat import CombinatorialObject as CombinatorialObject
from sage.combinat.words.alphabet import build_alphabet as build_alphabet
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.list_clone import ClonableElement as ClonableElement
from sage.structure.parent import Parent as Parent

def Words(alphabet=None, length=None, finite: bool = True, infinite: bool = True):
    """
    Return the combinatorial class of words of length k over an alphabet.

    EXAMPLES::

        sage: Words()
        Finite and infinite words over Set of Python objects of class 'object'
        sage: Words(length=7)
        Words of length 7 over Set of Python objects of class 'object'
        sage: Words(5)
        Finite and infinite words over {1, 2, 3, 4, 5}
        sage: Words(5, 3)
        Words of length 3 over {1, 2, 3, 4, 5}
        sage: Words(5, infinite=False)
        Finite words over {1, 2, 3, 4, 5}
        sage: Words(5, finite=False)
        Infinite words over {1, 2, 3, 4, 5}
        sage: Words('ab')
        Finite and infinite words over {'a', 'b'}
        sage: Words('ab', 2)
        Words of length 2 over {'a', 'b'}
        sage: Words('ab', infinite=False)
        Finite words over {'a', 'b'}
        sage: Words('ab', finite=False)
        Infinite words over {'a', 'b'}
        sage: Words('positive integers', finite=False)
        Infinite words over Positive integers
        sage: Words('natural numbers')
        Finite and infinite words over Non negative integers
    """

class AbstractLanguage(Parent):
    """
    Abstract base class.

    This is *not* to be used by any means. This class gather previous features
    of set of words (prior to :issue:`19619`). In the future that class might
    simply disappear or become a common base class for all languages. In the
    latter case, its name would possibly change to ``Language``.
    """
    sortkey_letters: Incomplete
    def __init__(self, alphabet=None, category=None) -> None:
        """
        INPUT:

        - ``alphabet`` -- the underlying alphabet

        TESTS::

            sage: loads(dumps(FiniteWords('ab'))) == FiniteWords('ab')
            True
            sage: loads(dumps(InfiniteWords('ab'))) == InfiniteWords('ab')
            True

            sage: Words('abc').sortkey_letters
            <bound method AbstractLanguage._sortkey_trivial of ...>
            sage: Words('bac').sortkey_letters
            <bound method AbstractLanguage._sortkey_letters of ...>
        """
    def alphabet(self):
        """
        EXAMPLES::

            sage: Words(NN).alphabet()
            Non negative integer semiring

            sage: InfiniteWords([1,2,3]).alphabet()
            {1, 2, 3}
            sage: InfiniteWords('ab').alphabet()
            {'a', 'b'}

            sage: FiniteWords([1,2,3]).alphabet()
            {1, 2, 3}
            sage: FiniteWords().alphabet()
            Set of Python objects of class 'object'
        """
    def identity_morphism(self):
        """
        Return the identity morphism from ``self`` to itself.

        EXAMPLES::

            sage: W = Words('ab')
            sage: W.identity_morphism()
            WordMorphism: a->a, b->b

        ::

            sage: W = Words(range(3))
            sage: W.identity_morphism()
            WordMorphism: 0->0, 1->1, 2->2

        There is no support yet for infinite alphabet::

            sage: W = Words(alphabet=Alphabet(name='NN'))
            sage: W
            Finite and infinite words over Non negative integers
            sage: W.identity_morphism()
            Traceback (most recent call last):
            ...
            NotImplementedError: size of alphabet must be finite
        """
    def __eq__(self, other) -> bool:
        """
        TESTS::

            sage: FiniteWords() == FiniteWords()
            True
            sage: FiniteWords() == InfiniteWords()
            False
            sage: InfiniteWords() == Words()
            False
            sage: FiniteWords([0,1]) == FiniteWords([0,1,2,3])
            False
        """
    def __ne__(self, other) -> bool:
        """
        TESTS::

            sage: InfiniteWords() != InfiniteWords()
            False
            sage: FiniteWords() != Words()
            True
            sage: Words('ab') != Words('ab')
            False
        """

class FiniteWords(AbstractLanguage):
    """
    The set of finite words over a fixed alphabet.

    EXAMPLES::

        sage: W = FiniteWords('ab')
        sage: W
        Finite words over {'a', 'b'}

    TESTS::

        sage: TestSuite(FiniteWords('ab')).run()
        sage: TestSuite(FiniteWords([])).run()
        sage: TestSuite(FiniteWords(['a'])).run()
    """
    def __init__(self, alphabet=None, category=None) -> None:
        """
        INPUT:

        - ``alphabet`` -- the underlying alphabet
        - ``category`` -- the suggested category of the set
          (normally should be automatically determined)

        TESTS::

            sage: FiniteWords('ab').is_finite()
            False
            sage: FiniteWords('ab').category()
            Category of infinite sets
            sage: FiniteWords([]).is_finite()
            True
            sage: FiniteWords([]).category()
            Category of finite sets
            sage: FiniteWords([], Sets()).category()
            Category of finite sets
        """
    def is_empty(self):
        """
        Return ``False``, because the empty word is in the set.

        TESTS::

            sage: FiniteWords('ab').is_empty()
            False
            sage: FiniteWords([]).is_empty()
            False
        """
    def cardinality(self):
        """
        Return the cardinality of this set.

        EXAMPLES::

            sage: FiniteWords('').cardinality()
            1
            sage: FiniteWords('a').cardinality()
            +Infinity
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(FiniteWords('ab')) # random
            12
        """
    @cached_method
    def shift(self):
        """
        Return the set of infinite words on the same alphabet.

        EXAMPLES::

            sage: FiniteWords('ab').shift()
            Infinite words over {'a', 'b'}
        """
    def factors(self):
        """
        Return itself.

        EXAMPLES::

            sage: FiniteWords('ab').factors()
            Finite words over {'a', 'b'}
        """
    def __call__(self, data=None, length=None, datatype=None, caching: bool = True, check: bool = True):
        '''
        Construct a new word object with parent ``self``.

        INPUT:

        - ``data`` -- (default: ``None``) list, string, tuple, iterator, ``None``
          (shorthand for []), or a callable defined on [0,1,...,length]

        - ``length`` -- integer (default: ``None``); only used if the data is
          an iterator or a callable. It determines the length of the word

        - ``datatype`` -- (default: ``None``) ``None``, "char", "list", "str",
          "tuple", "iter", "callable" or "pickled_function"; if ``None``, then
          the function tries to guess this from the data

        - ``caching`` -- boolean (default: ``True``); whether to keep a cache
          of the letters computed by an iterator or callable

        - ``check`` -- boolean (default: ``True``); whether to check if
          the 40 first letters are in the parent alphabet. This is a
          check done to test for small programming errors. Since we also
          support infinite words, we cannot really implement a more
          accurate check.

        .. NOTE::

           The check makes this method about 10 times slower (20µs instead
           of 2µs), so make sure to set it to False if you know the
           alphabet is OK. Fast creation (about 1µs) of a word can be
           done using the class directly (see :meth:`_element_classes`).

        .. WARNING::

           Be careful when defining words using callables and iterators. It
           appears that islice does not pickle correctly causing various errors
           when reloading. Also, most iterators do not support copying and
           should not support pickling by extension.

        EXAMPLES::

            sage: W = FiniteWords()

        Empty word::

            sage: W()
            word:

        Word with string::

            sage: W("abbabaab")
            word: abbabaab

        Word with string constructed from other types::

            sage: W([0,1,1,0,1,0,0,1], datatype=\'str\')
            word: 01101001
            sage: W((0,1,1,0,1,0,0,1), datatype=\'str\')
            word: 01101001

        Word with list::

            sage: W([0,1,1,0,1,0,0,1])
            word: 01101001

        Word with list constructed from other types::

            sage: W("01101001", datatype=\'list\')
            word: 01101001
            sage: W((0,1,1,0,1,0,0,1), datatype=\'list\')
            word: 01101001

        Word with tuple::

            sage: W((0,1,1,0,1,0,0,1))
            word: 01101001

        Word with tuple constructed from other types::

            sage: W([0,1,1,0,1,0,0,1], datatype=\'tuple\')
            word: 01101001
            sage: W("01101001", datatype=\'str\')
            word: 01101001

        Word with iterator::

            sage: from itertools import count
            sage: W(count(), length=10)
            word: 0123456789
            sage: W(iter("abbabaab"))
            word: abbabaab

        Word with function (a \'callable\')::

            sage: f = lambda n : add(Integer(n).digits(2)) % 2
            sage: W(f, length=12)
            word: 011010011001
            sage: FiniteWords([0,1,2])(f, length=12)
            word: 011010011001

        Word over a string with a parent::

            sage: w = FiniteWords(\'abc\')("abbabaab"); w
            word: abbabaab
            sage: w.parent()
            Finite words over {\'a\', \'b\', \'c\'}

        The fourty first letters of the word are checked if they are in the
        parent alphabet::

            sage: FiniteWords("ab")("abca")
            Traceback (most recent call last):
            ...
            ValueError: c not in alphabet
            sage: FiniteWords("ab")("abca", check=False)
            word: abca

        The default parent is the combinatorial class of all words::

            sage: w = Word("abbabaab"); w
            word: abbabaab
            sage: w.parent()
            Finite words over Set of Python objects of class \'object\'

        Creation of a word from a word::

            sage: FiniteWords([0,1,2,3])(FiniteWords([2,3])([2,2,2,3,3,2]))
            word: 222332
            sage: _.parent()
            Finite words over {0, 1, 2, 3}

        ::

            sage: FiniteWords([3,2,1])(FiniteWords([2,3])([2,2,2,3,3,2]))
            word: 222332
            sage: _.parent()
            Finite words over {3, 2, 1}

        Construction of a word from a word when the parents are the same::

            sage: W = FiniteWords()
            sage: w = W(range(8))
            sage: z = W(w)
            sage: w is z
            True

        Construction of a word path from a finite word::

            sage: W = FiniteWords(\'abcd\')
            sage: P = WordPaths(\'abcd\')                                                 # needs sage.modules
            sage: w = W(\'aaab\')
            sage: P(w)                                                                  # needs sage.modules
            Path: aaab

        Construction of a word path from a Christoffel word::

            sage: w = words.ChristoffelWord(5,8)
            sage: w
            word: 0010010100101
            sage: P = WordPaths([0,1,2,3])                                              # needs sage.modules
            sage: P(w)                                                                  # needs sage.modules
            Path: 0010010100101

        Construction of a word represented by a list from a word
        represented by a str ::

            sage: w = W(\'ababbbabab\')
            sage: type(w)
            <class \'sage.combinat.words.word.FiniteWord_str\'>
            sage: z = Word(w, datatype=\'list\')
            sage: type(z)
            <class \'sage.combinat.words.word.FiniteWord_list\'>
            sage: y = Word(w, alphabet=\'abc\', datatype=\'list\')
            sage: type(y)
            <class \'sage.combinat.words.word.FiniteWord_list\'>

        Creation of a word from a concatenation of words::

            sage: W = FiniteWords()
            sage: w = W() * W(\'a\')
            sage: Z = Words(\'ab\')
            sage: Z(w)
            word: a

        Creation of a word path from a FiniteWord_iter::

            sage: w = words.FibonacciWord()
            sage: f = w[:100]
            sage: P = WordPaths([0,1,2,3])                                              # needs sage.modules
            sage: p = P(f); p                                                           # needs sage.modules
            Path: 0100101001001010010100100101001001010010...
            sage: p.length()                                                            # needs sage.modules
            100

        Creation of a word path from a FiniteWord_callable::

            sage: g = W(lambda n:n%2, length = 100)
            sage: P = WordPaths([0,1,2,3])                                              # needs sage.modules
            sage: p = P(g); p                                                           # needs sage.modules
            Path: 0101010101010101010101010101010101010101...
            sage: p.length()                                                            # needs sage.modules
            100

        Creation of a word from a pickled function::

            sage: f = lambda n : n % 10
            sage: from sage.misc.fpickle import pickle_function
            sage: s = pickle_function(f)
            sage: W(s, length=10, datatype=\'pickled_function\')
            word: 0123456789

        If the alphabet is a subset of [0, 255], then it uses char as datatype::

            sage: type(Word([0,1,1,2,0], alphabet=list(range(256))))
            <class \'sage.combinat.words.word.FiniteWord_char\'>

        If the alphabet is a subset of [0, 255], then the letters must
        convert to an unsigned char. Otherwise an error is raised before
        the check is done::

            sage: type(Word([0,1,1,2,0,257], alphabet=list(range(256))))
            Traceback (most recent call last):
            ...
            OverflowError: value too large to convert to unsigned char
            sage: type(Word([0,1,1,2,0,258], alphabet=list(range(257))))
            Traceback (most recent call last):
            ...
            ValueError: 258 not in alphabet
            sage: type(Word([0,1,1,2,0,103], alphabet=list(range(100))))
            Traceback (most recent call last):
            ...
            ValueError: 103 not in alphabet
        '''
    def iterate_by_length(self, l: int = 1) -> Generator[Incomplete]:
        """
        Return an iterator over all the words of ``self`` of length `l`.

        INPUT:

        - ``l`` -- integer (default: 1); the length of the desired words

        EXAMPLES::

            sage: W = FiniteWords('ab')
            sage: list(W.iterate_by_length(1))
            [word: a, word: b]
            sage: list(W.iterate_by_length(2))
            [word: aa, word: ab, word: ba, word: bb]
            sage: list(W.iterate_by_length(3))
            [word: aaa,
             word: aab,
             word: aba,
             word: abb,
             word: baa,
             word: bab,
             word: bba,
             word: bbb]
            sage: list(W.iterate_by_length('a'))
            Traceback (most recent call last):
            ...
            TypeError: the parameter l (='a') must be an integer

        TESTS::

            sage: W = FiniteWords(NN)
            sage: list(W.iterate_by_length(1))
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot iterate over words for infinite alphabets
        """
    def __iter__(self):
        """
        Return an iterator over all the words of ``self``.

        The iterator outputs the words in shortlex order (see
        :wikipedia:`Shortlex_order`), i.e. first by increasing length and then
        lexicographically.

        EXAMPLES::

            sage: W = Words([4,5], infinite=False)
            sage: for w in W:
            ....:   if len(w)>3:
            ....:       break
            ....:   else:
            ....:       w
            word:
            word: 4
            word: 5
            word: 44
            word: 45
            ...
            word: 554
            word: 555
            sage: W = Words([5,4], infinite=False)
            sage: for w in W:
            ....:   if len(w)>3:
            ....:       break
            ....:   else:
            ....:       w
            word:
            word: 5
            word: 4
            word: 55
            word: 54
            ...
            word: 445
            word: 444
        """
    def __contains__(self, x) -> bool:
        """
        Test whether ``self`` contains ``x``.

        OUTPUT:

            This method returns ``True`` if ``x`` is a word of the appropriate
            length and the alphabets of the parents match. It returns ``False``
            otherwise.

        EXAMPLES::

            sage: W = FiniteWords('ab')
            sage: W('ab') in W
            True
            sage: W('aa') in FiniteWords('aa')
            False
            sage: FiniteWords('a')('aa') in FiniteWords('ab')
            False
            sage: 2 in FiniteWords([1,2,3])
            False
            sage: [2] in FiniteWords([1,2,3])
            False
            sage: [1, 'a'] in FiniteWords([1,2,3])
            False
        """
    def random_element(self, length=None, *args, **kwds):
        """
        Return a random finite word on the given alphabet.

        INPUT:

        - ``length`` -- (optional) the length of the word; if not set, will use
          a uniformly random number between 0 and 10

        - all other argument are transmitted to the random generator of the
          alphabet

        EXAMPLES::

            sage: W = FiniteWords(5)
            sage: W.random_element() # random
            word: 5114325445423521544531411434451152142155...

            sage: W = FiniteWords(ZZ)
            sage: W.random_element() # random
            word: 5,-1,-1,-1,0,0,0,0,-3,-11
            sage: W.random_element(length=4, x=0, y=4) # random
            word: 1003

        TESTS::

            sage: _ = FiniteWords(GF(5)).random_element()                               # needs sage.rings.finite_rings
        """
    def iter_morphisms(self, arg=None, codomain=None, min_length: int = 1) -> Generator[Incomplete]:
        """
        Iterate over all morphisms with domain ``self`` and the given
        codomain.

        INPUT:

        - ``arg`` -- (default: ``None``) it can be one of the following:

          - ``None`` -- then the method iterates through all morphisms

          - tuple `(a, b)` of two integers -- it specifies the range
            ``range(a, b)`` of values to consider for the sum of the length
            of the image of each letter in the alphabet

          - list of nonnegative integers -- the length of the list must be
            equal to the size of the alphabet, and the `i`-th integer of
            ``arg`` determines the length of the word mapped to by the `i`-th
            letter of the (ordered) alphabet

        - ``codomain`` -- (default: ``None``) a combinatorial class of words;
          by default, ``codomain`` is ``self``

        - ``min_length`` -- nonnegative integer (default: 1); if ``arg`` is
          not specified, then iterate through all the morphisms where the
          length of the images of each letter in the alphabet is at least
          ``min_length``. This is ignored if ``arg`` is a list.

        OUTPUT: iterator

        EXAMPLES:

        Iterator over all non-erasing morphisms::

            sage: W = FiniteWords('ab')
            sage: it = W.iter_morphisms()
            sage: for _ in range(7): next(it)
            WordMorphism: a->a, b->a
            WordMorphism: a->a, b->b
            WordMorphism: a->b, b->a
            WordMorphism: a->b, b->b
            WordMorphism: a->aa, b->a
            WordMorphism: a->aa, b->b
            WordMorphism: a->ab, b->a

        Iterator over all morphisms including erasing morphisms::

            sage: W = FiniteWords('ab')
            sage: it = W.iter_morphisms(min_length=0)
            sage: for _ in range(7): next(it)
            WordMorphism: a->, b->
            WordMorphism: a->a, b->
            WordMorphism: a->b, b->
            WordMorphism: a->, b->a
            WordMorphism: a->, b->b
            WordMorphism: a->aa, b->
            WordMorphism: a->ab, b->

        Iterator over morphisms where the sum of the lengths of the images
        of the letters is in a specific range::

            sage: for m in W.iter_morphisms((0, 3), min_length=0): m
            WordMorphism: a->aa, b->
            WordMorphism: a->ab, b->
            WordMorphism: a->ba, b->
            WordMorphism: a->bb, b->
            WordMorphism: a->a, b->a
            WordMorphism: a->a, b->b
            WordMorphism: a->b, b->a
            WordMorphism: a->b, b->b
            WordMorphism: a->a, b->
            WordMorphism: a->b, b->
            WordMorphism: a->, b->aa
            WordMorphism: a->, b->ab
            WordMorphism: a->, b->ba
            WordMorphism: a->, b->bb
            WordMorphism: a->, b->a
            WordMorphism: a->, b->b
            WordMorphism: a->, b->

        ::

            sage: for m in W.iter_morphisms( (2, 4) ): m
            WordMorphism: a->aa, b->a
            WordMorphism: a->aa, b->b
            WordMorphism: a->ab, b->a
            WordMorphism: a->ab, b->b
            WordMorphism: a->ba, b->a
            WordMorphism: a->ba, b->b
            WordMorphism: a->bb, b->a
            WordMorphism: a->bb, b->b
            WordMorphism: a->a, b->aa
            WordMorphism: a->a, b->ab
            WordMorphism: a->a, b->ba
            WordMorphism: a->a, b->bb
            WordMorphism: a->b, b->aa
            WordMorphism: a->b, b->ab
            WordMorphism: a->b, b->ba
            WordMorphism: a->b, b->bb
            WordMorphism: a->a, b->a
            WordMorphism: a->a, b->b
            WordMorphism: a->b, b->a
            WordMorphism: a->b, b->b

        Iterator over morphisms with specific image lengths::

            sage: for m in W.iter_morphisms([0, 0]): m
            WordMorphism: a->, b->
            sage: for m in W.iter_morphisms([0, 1]): m
            WordMorphism: a->, b->a
            WordMorphism: a->, b->b
            sage: for m in W.iter_morphisms([2, 1]): m
            WordMorphism: a->aa, b->a
            WordMorphism: a->aa, b->b
            WordMorphism: a->ab, b->a
            WordMorphism: a->ab, b->b
            WordMorphism: a->ba, b->a
            WordMorphism: a->ba, b->b
            WordMorphism: a->bb, b->a
            WordMorphism: a->bb, b->b
            sage: for m in W.iter_morphisms([2, 2]): m
            WordMorphism: a->aa, b->aa
            WordMorphism: a->aa, b->ab
            WordMorphism: a->aa, b->ba
            WordMorphism: a->aa, b->bb
            WordMorphism: a->ab, b->aa
            WordMorphism: a->ab, b->ab
            WordMorphism: a->ab, b->ba
            WordMorphism: a->ab, b->bb
            WordMorphism: a->ba, b->aa
            WordMorphism: a->ba, b->ab
            WordMorphism: a->ba, b->ba
            WordMorphism: a->ba, b->bb
            WordMorphism: a->bb, b->aa
            WordMorphism: a->bb, b->ab
            WordMorphism: a->bb, b->ba
            WordMorphism: a->bb, b->bb

        The codomain may be specified as well::

            sage: Y = FiniteWords('xyz')
            sage: for m in W.iter_morphisms([0, 2], codomain=Y): m
            WordMorphism: a->, b->xx
            WordMorphism: a->, b->xy
            WordMorphism: a->, b->xz
            WordMorphism: a->, b->yx
            WordMorphism: a->, b->yy
            WordMorphism: a->, b->yz
            WordMorphism: a->, b->zx
            WordMorphism: a->, b->zy
            WordMorphism: a->, b->zz
            sage: for m in Y.iter_morphisms([0,2,1], codomain=W): m
            WordMorphism: x->, y->aa, z->a
            WordMorphism: x->, y->aa, z->b
            WordMorphism: x->, y->ab, z->a
            WordMorphism: x->, y->ab, z->b
            WordMorphism: x->, y->ba, z->a
            WordMorphism: x->, y->ba, z->b
            WordMorphism: x->, y->bb, z->a
            WordMorphism: x->, y->bb, z->b
            sage: it = W.iter_morphisms(codomain=Y)
            sage: for _ in range(10): next(it)
            WordMorphism: a->x, b->x
            WordMorphism: a->x, b->y
            WordMorphism: a->x, b->z
            WordMorphism: a->y, b->x
            WordMorphism: a->y, b->y
            WordMorphism: a->y, b->z
            WordMorphism: a->z, b->x
            WordMorphism: a->z, b->y
            WordMorphism: a->z, b->z
            WordMorphism: a->xx, b->x

        TESTS::

            sage: list(W.iter_morphisms([1,0]))
            [WordMorphism: a->a, b->, WordMorphism: a->b, b->]
            sage: list(W.iter_morphisms([0,0], codomain=Y))
            [WordMorphism: a->, b->]
            sage: list(W.iter_morphisms([0, 1, 2]))
            Traceback (most recent call last):
            ...
            TypeError: arg (=[0, 1, 2]) must be an iterable of 2 integers
            sage: list(W.iter_morphisms([0, 'a']))
            Traceback (most recent call last):
            ...
            TypeError: arg (=[0, 'a']) must be an iterable of 2 integers
            sage: list(W.iter_morphisms([0, 1], codomain='a'))
            Traceback (most recent call last):
            ...
            TypeError: codomain (=a) must be an instance of FiniteWords
        """

class InfiniteWords(AbstractLanguage):
    def cardinality(self):
        """
        Return the cardinality of this set.

        EXAMPLES::

            sage: InfiniteWords('ab').cardinality()
            +Infinity
            sage: InfiniteWords('a').cardinality()
            1
            sage: InfiniteWords('').cardinality()
            0
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(InfiniteWords('ab')) # random
            12
        """
    @cached_method
    def factors(self):
        """
        Return the set of finite words on the same alphabet.

        EXAMPLES::

            sage: InfiniteWords('ab').factors()
            Finite words over {'a', 'b'}
        """
    def shift(self):
        """
        Return itself.

        EXAMPLES::

            sage: InfiniteWords('ab').shift()
            Infinite words over {'a', 'b'}
        """
    def random_element(self, *args, **kwds):
        """
        Return a random infinite word.

        EXAMPLES::

            sage: W = InfiniteWords('ab')
            sage: W.random_element() # random
            word: abbbabbaabbbabbabbaabaabbabbbbbbbbaabbbb...

            sage: W = InfiniteWords(ZZ)
            sage: W.random_element(x=2,y=4) # random
            word: 3333223322232233333223323223222233233233...
        """
    def __call__(self, data=None, datatype=None, caching: bool = True, check: bool = True):
        '''
        Construct a new word object with parent ``self``.

        INPUT:

        - ``data`` -- iterator or a callable

        - ``datatype`` -- (default: ``None``) ``None``, "iter", "callable" or
          "pickled_function"; if ``None``, then the function tries to guess
          this from the data

        - ``caching`` -- boolean (default: ``True``); whether to keep a
          cache of the letters computed by an iterator or callable

        - ``check`` -- boolean (default: ``True``); whether to check if
          the 40 first letters are in the parent alphabet. This is a
          check done to test for small programming errors. Since we also
          support infinite words, we cannot really implement a more
          accurate check.

        .. NOTE::

           The check makes this method about 10 times slower (20µs instead
           of 2µs), so make sure to set it to False if you know the
           alphabet is OK. Fast creation (about 1µs) of a word can be
           done using the class directly (see :meth:`_element_classes`).

        .. WARNING::

           Be careful when defining words using callables and iterators. It
           appears that islice does not pickle correctly causing various errors
           when reloading. Also, most iterators do not support copying and
           should not support pickling by extension.

        EXAMPLES:

        Word with iterator::

            sage: from itertools import count
            sage: InfiniteWords()(count())
            word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...

        Word with function (a \'callable\')::

            sage: f = lambda n : add(Integer(n).digits(2)) % 2
            sage: InfiniteWords()(f)
            word: 0110100110010110100101100110100110010110...

        The fourty first letters of the word are checked if they are in the
        parent alphabet::

            sage: from itertools import count
            sage: InfiniteWords("ab")(("c" if i == 0 else "a" for i in count()))
            Traceback (most recent call last):
            ...
            ValueError: c not in alphabet

        Creation of a word from a word::

            sage: w = InfiniteWords([0,1,2,3])(words.FibonacciWord())
            sage: w
            word: 0100101001001010010100100101001001010010...
            sage: w.parent()
            Infinite words over {0, 1, 2, 3}
            sage: InfiniteWords([0,1,2,3])(w) is w
            True

        Creation of a word from a pickled function::

            sage: f = lambda n : n % 10
            sage: from sage.misc.fpickle import pickle_function
            sage: s = pickle_function(f)
            sage: Word(s, datatype=\'pickled_function\')
            word: 0123456789012345678901234567890123456789...
        '''

class FiniteOrInfiniteWords(AbstractLanguage):
    def __init__(self, alphabet) -> None:
        """
        INPUT:

        - ``alphabet`` -- the underlying alphabet

        TESTS::

            sage: loads(dumps(Words())) == Words()
            True
        """
    def cardinality(self):
        """
        Return the cardinality of this set of words.

        EXAMPLES::

            sage: Words('abcd').cardinality()
            +Infinity
            sage: Words('a').cardinality()
            +Infinity
            sage: Words('').cardinality()
            1
        """
    def __hash__(self):
        """
        TESTS::

            sage: hash(Words('ab')) # random
            12
        """
    @cached_method
    def finite_words(self):
        """
        Return the set of finite words.

        EXAMPLES::

            sage: Words('ab').finite_words()
            Finite words over {'a', 'b'}
        """
    factors = finite_words
    @cached_method
    def infinite_words(self):
        """
        Return the set of infinite words.

        EXAMPLES::

            sage: Words('ab').infinite_words()
            Infinite words over {'a', 'b'}
        """
    shift = infinite_words
    def iterate_by_length(self, length):
        """
        Return an iterator over the words of given length.

        EXAMPLES::

            sage: [w.string_rep() for w in Words('ab').iterate_by_length(3)]
            ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
        """
    def __call__(self, data=None, length=None, datatype=None, caching: bool = True, check: bool = True):
        '''
        Construct a new word object with parent ``self``.

        INPUT:

        - ``data`` -- (default: ``None``) list, string, tuple, iterator, ``None``
          (shorthand for []), or a callable defined on [0,1,...,length]

        - ``length`` -- (default: ``None``) this is dependent on the type of data.
          It is ignored for words defined by lists, strings, tuples,
          etc., because they have a naturally defined length.
          For callables, this defines the domain of definition,
          which is assumed to be [0, 1, 2, ..., length-1].
          For iterators: Infinity if you know the iterator will not
          terminate (default); ``\'unknown\'`` if you do not know whether the
          iterator terminates; ``\'finite\'`` if you know that the iterator
          terminates, but do not know the length.

        - ``datatype`` -- (default: ``None``) ``None``, "char", "list", "str",
          "tuple", "iter", "callable" or "pickled_function"; if ``None``, then
          the function tries to guess this from the data.

        - ``caching`` -- boolean (default: ``True``); whether to keep a cache
          of the letters computed by an iterator or callable

        - ``check`` -- boolean (default: ``True``); whether to check if
          the 40 first letters are in the parent alphabet. This is a
          check done to test for small programming errors. Since we also
          support infinite words, we cannot really implement a more
          accurate check.

        .. NOTE::

           The check makes this method about 10 times slower (20µs instead
           of 2µs), so make sure to set it to False if you know the
           alphabet is OK. Fast creation (about 1µs) of a word can be
           done using the class directly (see :meth:`_element_classes`).

        .. WARNING::

           Be careful when defining words using callables and iterators. It
           appears that islice does not pickle correctly causing various errors
           when reloading. Also, most iterators do not support copying and
           should not support pickling by extension.

        EXAMPLES:

        Empty word::

            sage: Words()()
            word:

        Word with string::

            sage: Words()("abbabaab")
            word: abbabaab

        Word with string constructed from other types::

            sage: Words()([0,1,1,0,1,0,0,1], datatype=\'str\')
            word: 01101001
            sage: Words()((0,1,1,0,1,0,0,1), datatype=\'str\')
            word: 01101001

        Word with list::

            sage: Words()([0,1,1,0,1,0,0,1])
            word: 01101001

        Word with list constructed from other types::

            sage: Words()("01101001", datatype=\'list\')
            word: 01101001
            sage: Words()((0,1,1,0,1,0,0,1), datatype=\'list\')
            word: 01101001

        Word with tuple::

            sage: Words()((0,1,1,0,1,0,0,1))
            word: 01101001

        Word with tuple constructed from other types::

            sage: Words()([0,1,1,0,1,0,0,1], datatype=\'tuple\')
            word: 01101001
            sage: Words()("01101001", datatype=\'str\')
            word: 01101001

        Word with iterator::

            sage: from itertools import count
            sage: Words()(count())
            word: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,...
            sage: Words()(iter("abbabaab")) # iterators default to infinite words
            word: abbabaab
            sage: Words()(iter("abbabaab"), length=\'unknown\')
            word: abbabaab
            sage: Words()(iter("abbabaab"), length=\'finite\')
            word: abbabaab

        Word with function (a \'callable\')::

            sage: f = lambda n : add(Integer(n).digits(2)) % 2
            sage: Words()(f)
            word: 0110100110010110100101100110100110010110...
            sage: Words()(f, length=8)
            word: 01101001

        Word over a string with a parent::

            sage: w = Words(\'abc\')("abbabaab"); w
            word: abbabaab
            sage: w.parent()
            Finite words over {\'a\', \'b\', \'c\'}

        The fourty first letters of the word are checked if they are in the
        parent alphabet::

            sage: Words("ab")("abca")
            Traceback (most recent call last):
            ...
            ValueError: c not in alphabet
            sage: Words("ab")("abca", check=False)
            word: abca

        The default parent is the combinatorial class of all words::

            sage: w = Words()("abbabaab"); w
            word: abbabaab
            sage: w.parent()
            Finite words over Set of Python objects of class \'object\'

        Creation of a word from a word::

            sage: Words([0,1,2,3])(Words([2,3])([2,2,2,3,3,2]))
            word: 222332
            sage: _.parent()
            Finite words over {0, 1, 2, 3}

        ::

            sage: Words([3,2,1])(Words([2,3])([2,2,2,3,3,2]))
            word: 222332
            sage: _.parent()
            Finite words over {3, 2, 1}

        Construction of a word from a word when the parents are the same::

            sage: W = Words()
            sage: w = W(range(8))
            sage: z = W(w)
            sage: w is z
            True

        Construction of a word path from a finite word::

            sage: W = Words(\'abcd\')
            sage: P = WordPaths(\'abcd\')                                                 # needs sage.modules
            sage: w = W(\'aaab\')
            sage: P(w)                                                                  # needs sage.modules
            Path: aaab

        Construction of a word path from a Christoffel word::

            sage: w = words.ChristoffelWord(5,8)
            sage: w
            word: 0010010100101
            sage: P = WordPaths([0,1,2,3])                                              # needs sage.modules
            sage: P(w)                                                                  # needs sage.modules
            Path: 0010010100101

        Construction of a word represented by a list from a word
        represented by a str ::

            sage: w = Word(\'ababbbabab\')
            sage: type(w)
            <class \'sage.combinat.words.word.FiniteWord_str\'>
            sage: z = Word(w, datatype=\'list\')
            sage: type(z)
            <class \'sage.combinat.words.word.FiniteWord_list\'>
            sage: y = Word(w, alphabet=\'abc\', datatype=\'list\')
            sage: type(y)
            <class \'sage.combinat.words.word.FiniteWord_list\'>

        Creation of a word from a concatenation of words::

            sage: W = Words()
            sage: w = W() * W(\'a\')
            sage: Z = Words(\'ab\')
            sage: Z(w)
            word: a

        Creation of a word path from a FiniteWord_iter::

            sage: w = words.FibonacciWord()
            sage: f = w[:100]
            sage: P = WordPaths([0,1,2,3])                                              # needs sage.modules
            sage: p = P(f); p                                                           # needs sage.modules
            Path: 0100101001001010010100100101001001010010...
            sage: p.length()                                                            # needs sage.modules
            100

        Creation of a word path from a :class:`FiniteWord_callable`::

            sage: g = Word(lambda n: n%2, length=100)
            sage: P = WordPaths([0,1,2,3])                                              # needs sage.modules
            sage: p = P(g); p                                                           # needs sage.modules
            Path: 0101010101010101010101010101010101010101...
            sage: p.length()                                                            # needs sage.modules
            100

        Creation of a word from a pickled function::

            sage: f = lambda n: n % 10
            sage: from sage.misc.fpickle import pickle_function
            sage: s = pickle_function(f)
            sage: Word(s, datatype=\'pickled_function\')
            word: 0123456789012345678901234567890123456789...

        If the alphabet is a subset of [0, 255], then it uses char as datatype::

            sage: type(Word([0,1,1,2,0], alphabet=list(range(256))))
            <class \'sage.combinat.words.word.FiniteWord_char\'>

        If the alphabet is a subset of [0, 255], then the letters must
        convert to an unsigned char. Otherwise an error is raised before
        the check is done::

            sage: type(Word([0,1,1,2,0,257], alphabet=list(range(256))))
            Traceback (most recent call last):
            ...
            OverflowError: value too large to convert to unsigned char
            sage: type(Word([0,1,1,2,0,258], alphabet=list(range(257))))
            Traceback (most recent call last):
            ...
            ValueError: 258 not in alphabet
            sage: type(Word([0,1,1,2,0,103], alphabet=list(range(100))))
            Traceback (most recent call last):
            ...
            ValueError: 103 not in alphabet

        Check that the type is rightly guessed for parking functions which are
        callable::

            sage: p = ParkingFunction([2,2,1])
            sage: Word(p).parent()
            Finite words over Set of Python objects of class \'object\'
        '''

class Words_n(Parent):
    """
    The set of words of fixed length on a given alphabet.
    """
    def __init__(self, words, n) -> None:
        """
        INPUT:

        - ``words`` -- set of finite words

        - ``n`` -- nonnegative integer

        TESTS::

            sage: Words([0,1], length=-42)
            Traceback (most recent call last):
            ...
            ValueError: n = -42 must be nonnegative
        """
    def alphabet(self):
        """
        Return the underlying alphabet.

        EXAMPLES::

            sage: Words([0,1], 4).alphabet()
            {0, 1}
        """
    def __call__(self, data, *args, **kwds):
        """
        INPUT:

        - all arguments are sent directly to the underlying set of finite words.
          See the documentation there for the actual input.

        TESTS::

            sage: Words(5,3)([1,2,3])
            word: 123
            sage: Words(5,3)([1,2,3,1])
            Traceback (most recent call last):
            ...
            ValueError: wrong length
        """
    def list(self):
        """
        Return a list of all the words contained in ``self``.

        EXAMPLES::

            sage: Words(0,0).list()
            [word: ]
            sage: Words(5,0).list()
            [word: ]
            sage: Words(['a','b','c'],0).list()
            [word: ]
            sage: Words(5,1).list()
            [word: 1, word: 2, word: 3, word: 4, word: 5]
            sage: Words(['a','b','c'],2).list()
            [word: aa, word: ab, word: ac, word: ba, word: bb, word: bc, word: ca, word: cb, word: cc]
        """
    def random_element(self, *args, **kwds):
        """
        Return a random word in this set.

        EXAMPLES::

            sage: W = Words('ab', 4)
            sage: W.random_element()  # random
            word: bbab
            sage: W.random_element() in W
            True

            sage: W = Words(ZZ, 5)
            sage: W.random_element()  # random
            word: 1,2,2,-1,12
            sage: W.random_element() in W
            True

        TESTS::

            sage: _ = Words(GF(5),4).random_element()                                   # needs sage.rings.finite_rings

        Check that :issue:`18283` is fixed::

            sage: w = Words('abc', 5).random_element()
            sage: w.length()
            5
        """
    def __contains__(self, x) -> bool:
        '''
        EXAMPLES::

            sage: W = Words(3,5)
            sage: W.an_element() in W
            True

            sage: 2 in Words(length=3)
            False
            sage: [1,\'a\',3] in Words(length=3)
            False
            sage: [1,2] in Words(length=3)
            False
            sage: "abc" in Words(length=3)
            False
            sage: Words("abc")("ababc") in Words(length=3)
            False
            sage: Words([0,1])([1,0,1]) in Words([0,1], length=3)
            True
        '''
    def cardinality(self):
        """
        Return the number of words of length `n` from alphabet.

        EXAMPLES::

            sage: Words(['a','b','c'], 4).cardinality()
            81
            sage: Words(3, 4).cardinality()
            81
            sage: Words(0,0).cardinality()
            1
            sage: Words(5,0).cardinality()
            1
            sage: Words(['a','b','c'],0).cardinality()
            1
            sage: Words(0,1).cardinality()
            0
            sage: Words(5,1).cardinality()
            5
            sage: Words(['a','b','c'],1).cardinality()
            3
            sage: Words(7,13).cardinality()
            96889010407
            sage: Words(['a','b','c','d','e','f','g'],13).cardinality()
            96889010407
        """
    __len__ = cardinality
    def __iter__(self):
        """
        TESTS::

            sage: [w for w in Words(['a', 'b'], 2)]
            [word: aa, word: ab, word: ba, word: bb]
            sage: [w for w in Words(['b', 'a'], 2)]
            [word: bb, word: ba, word: ab, word: aa]
            sage: [w for w in Words(['a', 'b'], 0)]
            [word: ]
            sage: [w for w in Words([], 3)]
            []
        """
    def iterate_by_length(self, length):
        """
        All words in this class are of the same length, so use iterator
        instead.

        TESTS::

            sage: W = Words(['a', 'b'], 2)
            sage: list(W.iterate_by_length(2))
            [word: aa, word: ab, word: ba, word: bb]
            sage: list(W.iterate_by_length(1))
            []
        """
