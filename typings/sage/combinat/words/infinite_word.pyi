from sage.combinat.words.abstract_word import Word_class as Word_class
from sage.combinat.words.word_options import word_options as word_options
from sage.rings.infinity import Infinity as Infinity

class InfiniteWord_class(Word_class):
    def length(self):
        """
        Return the length of ``self``.

        EXAMPLES::

            sage: f = lambda n : n % 6
            sage: w = Word(f); w
            word: 0123450123450123450123450123450123450123...
            sage: w.length()
            +Infinity
        """
