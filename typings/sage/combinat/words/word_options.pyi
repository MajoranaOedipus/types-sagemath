from _typeshed import Incomplete
from sage.rings.integer import Integer as Integer

word_options: Incomplete

def WordOptions(**kwargs):
    '''
    Set the global options for elements of the word class.
    The defaults are for words to be displayed in list notation.

    INPUT:

    - ``display`` -- \'string\' (default), or \'list\', words are displayed in
      string or list notation
    - ``truncate`` -- boolean (default: ``True``); whether to truncate the string
      output of long words (see truncate_length below)
    - ``truncate_length`` -- integer (default: 40); if the length of the word
      is greater than this integer, then the word is truncated
    - ``letter_separator`` -- string (default: ``\',\'``); if the string
      representation of letters have length greater than 1, then
      the letters are separated by this string in the string
      representation of the word

    If no parameters are set, then the function returns a copy of the
    options dictionary.

    EXAMPLES::

        sage: w = Word([2,1,3,12])
        sage: u = Word("abba")
        sage: WordOptions(display=\'list\')
        sage: w
        word: [2, 1, 3, 12]
        sage: u
        word: [\'a\', \'b\', \'b\', \'a\']
        sage: WordOptions(display=\'string\')
        sage: w
        word: 2,1,3,12
        sage: u
        word: abba
    '''
