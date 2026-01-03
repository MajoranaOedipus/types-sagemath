r"""
Combinatorics on words

**Main modules and their methods:**

- :ref:`sage.combinat.words.abstract_word`
- :ref:`sage.combinat.words.finite_word`
- :ref:`sage.combinat.words.infinite_word`
- :ref:`sage.combinat.words.alphabet`
- :ref:`sage.combinat.words.words`
- :ref:`sage.combinat.words.paths`
- :ref:`sage.combinat.words.morphism`
- :ref:`sage.combinat.words.shuffle_product`
- :ref:`sage.combinat.words.suffix_trees`

Main classes and functions meant to be used by the user:

:func:`~sage.combinat.words.word.Word`,
:class:`~sage.combinat.words.words.FiniteWords`,
:class:`~sage.combinat.words.words.InfiniteWords`,
:func:`~sage.combinat.words.words.Words`,
:func:`~sage.combinat.words.alphabet.Alphabet`,
:class:`~sage.combinat.words.morphism.WordMorphism`,
:class:`~sage.combinat.words.paths.WordPaths`.

A list of common words can be accessed through ``words.<tab>`` and are listed in
the :ref:`words catalog <sage.combinat.words.word_generators>`.

**Internal representation of words:**

- :ref:`sage.combinat.words.word`
- :ref:`sage.combinat.words.word_char`
- :ref:`sage.combinat.words.word_datatypes`
- :ref:`sage.combinat.words.word_infinite_datatypes`

**Options:**

- :ref:`sage.combinat.words.word_options`

See :func:`~sage.combinat.words.word_options.WordOptions`.
"""

from sage.combinat.words.alphabet import Alphabet as Alphabet, build_alphabet as build_alphabet
from sage.combinat.words.lyndon_word import LyndonWord as LyndonWord, LyndonWords as LyndonWords, StandardBracketedLyndonWords as StandardBracketedLyndonWords
from sage.combinat.words.morphism import WordMorphism as WordMorphism
from sage.combinat.words.paths import WordPaths as WordPaths
from sage.combinat.words.word import Word as Word
from sage.combinat.words.word_generators import words as words
from sage.combinat.words.word_options import WordOptions as WordOptions
from sage.combinat.words.words import FiniteWords as FiniteWords, InfiniteWords as InfiniteWords, Words as Words

