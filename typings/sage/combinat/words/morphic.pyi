from sage.combinat.words.word_infinite_datatypes import WordDatatype_callable as WordDatatype_callable
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import Infinity as Infinity

class WordDatatype_morphic(WordDatatype_callable):
    """
    Datatype for a morphic word defined by a morphism, a starting letter
    and a coding.
    """
    def __init__(self, parent, morphism, letter, coding=None, length=...) -> None:
        '''
        INPUT:

        - ``parent`` -- a parent
        - ``morphism`` -- a word morphism
        - ``letter`` -- a starting letter
        - ``coding`` -- dictionary (default: ``None``); if ``None``
          the identity map is used for the coding
        - ``length`` -- integer or ``\'finite\'`` or ``Infinity`` or
          ``\'unknown\'`` (default: ``Infinity``) the length of the word

        EXAMPLES::

            sage: m = WordMorphism(\'a->ab,b->a\')
            sage: w = m.fixed_point(\'a\')
            sage: w
            word: abaababaabaababaababaabaababaabaababaaba...
            sage: w[555:1000]                                                           # needs sage.modules
            word: abaababaabaababaababaabaababaabaababaaba...
            sage: w.length()
            +Infinity

        ::

            sage: m = WordMorphism(\'a->abc,b->baba,c->ca\')
            sage: m.fixed_point(\'a\')
            word: abcbabacababaabcbabaabccaabcbabaabcbabaa...
            sage: w = m.fixed_point(\'a\')
            sage: w[7]                                                                  # needs sage.modules
            \'c\'
            sage: w[2:7]                                                                # needs sage.modules
            word: cbaba
            sage: w[500:503]                                                            # needs sage.modules
            word: caa

        When the morphic word is finite::

            sage: m = WordMorphism("a->ab,b->")
            sage: w = m.fixed_point("a"); w
            word: ab
            sage: w[0]                                                                  # needs sage.modules
            \'a\'
            sage: w.length()
            2

        Using the coding argument::

            sage: m = WordMorphism(\'a->ab,b->a\')
            sage: W = m.domain()
            sage: from sage.combinat.words.morphic import WordDatatype_morphic
            sage: coding = {\'a\':\'x\', \'b\':\'y\'}
            sage: w = WordDatatype_morphic(W, m, \'a\', coding=coding)
            sage: [w[i] for i in range(10)]                                             # needs sage.modules
            [\'x\', \'y\', \'x\', \'x\', \'y\', \'x\', \'y\', \'x\', \'x\', \'y\']

        TESTS::

            sage: m = WordMorphism(\'a->abcd,b->bbc,c->cddd,d->cba\')
            sage: w = m.fixed_point(\'a\')
            sage: it = iter(w)
            sage: for _ in range(10000): _ = next(it)
            sage: L = [next(it) for _ in range(10)]; L
            [\'d\', \'d\', \'d\', \'c\', \'d\', \'d\', \'d\', \'c\', \'b\', \'a\']
            sage: w[10000:10010]                                                        # needs sage.modules
            word: dddcdddcba
            sage: list(w[10000:10010]) == L                                             # needs sage.modules
            True
        '''
    def __reduce__(self):
        '''
        EXAMPLES::

            sage: m = WordMorphism(\'a->ab,b->a\')
            sage: w = m.fixed_point(\'a\')
            sage: w.__reduce__()
            (<class \'sage.combinat.words.word.InfiniteWord_morphic\'>,
             (Infinite words over {\'a\', \'b\'},
              WordMorphism: a->ab, b->a,
              \'a\',
              {\'a\': \'a\', \'b\': \'b\'},
              +Infinity))

        Below is the behavior for words of finite length::

            sage: m = WordMorphism("a->ab,b->")
            sage: w = m.fixed_point("a")
            sage: w.__reduce__()
            (<class \'sage.combinat.words.word.FiniteWord_morphic\'>,
             (Finite words over {\'a\', \'b\'},
              WordMorphism: a->ab, b->,
              \'a\',
              {\'a\': \'a\', \'b\': \'b\'},
              2))
        '''
    def representation(self, n):
        '''
        Return the representation of the integer n in the numeration system
        associated to the morphism.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: list

        EXAMPLES::

            sage: m = WordMorphism(\'a->ab,b->a\')
            sage: w = m.fixed_point(\'a\')
            sage: w.representation(5)                                                   # needs sage.modules
            [1, 0, 0, 0]

        When the morphic word is finite::

            sage: m = WordMorphism("a->ab,b->,c->cdab,d->dcab")
            sage: w = m.fixed_point("a")
            sage: w.representation(0)                                                   # needs sage.modules
            []
            sage: w.representation(1)                                                   # needs sage.modules
            [1]
            sage: w.representation(2)                                                   # needs sage.modules
            Traceback (most recent call last):
            ...
            IndexError: index (=2) out of range, the fixed point is finite and has length 2

        TESTS:

        Accessing this method from an instance of the current class (no using
        the inherited word classes)::

            sage: m = WordMorphism(\'a->ab,b->a\')
            sage: W = m.domain()
            sage: from sage.combinat.words.morphic import WordDatatype_morphic
            sage: w = WordDatatype_morphic(W, m, \'a\')
            sage: type(w)
            <class \'sage.combinat.words.morphic.WordDatatype_morphic\'>
            sage: w.representation(5)                                                   # needs sage.modules
            [1, 0, 0, 0]
        '''
    def __iter__(self):
        '''
        Return an iterator of the letters of the fixed point of ``self``
        starting with ``letter``.

        If w is the iterated word, then this iterator: outputs the elements
        of morphism[ w[i] ], appends morphism[ w[i+1] ] to w, increments i.

        INPUT:

        - ``self`` -- an endomorphism, must be prolongable on
          letter

        - ``letter`` -- a letter in the domain of ``self``

        OUTPUT: iterator of the fixed point

        EXAMPLES::

            sage: m = WordMorphism("a->ab,b->a")
            sage: w = m.fixed_point("a")
            sage: it = iter(w)
            sage: [next(it) for _ in range(10)]
            [\'a\', \'b\', \'a\', \'a\', \'b\', \'a\', \'b\', \'a\', \'a\', \'b\']

        Works with erasing morphisms::

            sage: m = WordMorphism(\'a->abc,b->,c->\')
            sage: w = m.fixed_point("a")
            sage: list(w)
            [\'a\', \'b\', \'c\']

        The morphism must be prolongable on the letter or the iterator will
        be empty::

            sage: list(m.fixed_point("b"))
            Traceback (most recent call last):
            ...
            TypeError: self must be prolongable on b

        The morphism must be an endomorphism::

            sage: m = WordMorphism(\'a->ac,b->aac\')
            sage: w = m.fixed_point(\'a\')
            Traceback (most recent call last):
            ...
            TypeError: self (=a->ac, b->aac) is not self-composable

        We check that :issue:`8595` is fixed::

            sage: s = WordMorphism({(\'a\', 1):[(\'a\', 1), (\'a\', 2)], (\'a\', 2):[(\'a\', 1)]})
            sage: w = s.fixed_point((\'a\', 1))
            sage: it = iter(w)
            sage: next(it)
            (\'a\', 1)

        This shows that issue :issue:`13668` has been resolved::

            sage: s = WordMorphism({1:[1,2],2:[2,3],3:[4],4:[5],5:[6],6:[7],7:[8],8:[9],9:[10],10:[1]})
            sage: (s^7).fixed_points()
            [word: 1223234234523456234567234567823456789234...,
             word: 2,3,4,5,6,7,8,9,10,1,1,2,1,2,2,3,1,2,2,3,2,3,4,1,2,2,3,2,3,4,2,3,4,5,1,2,2,3,2,3,...]
            sage: (s^7).reversal().fixed_points()
            []
        '''
