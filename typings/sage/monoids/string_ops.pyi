from .string_monoid_element import StringMonoidElement as StringMonoidElement
from sage.misc.lazy_import import lazy_import as lazy_import

def strip_encoding(S) -> str:
    '''
    Return the upper case string of S stripped of all non-alphabetic characters.

    EXAMPLES::

        sage: S = "The cat in the hat."
        sage: strip_encoding(S)
        \'THECATINTHEHAT\'

    TESTS::

        sage: strip_encoding(44)
        Traceback (most recent call last):
        ...
        TypeError: argument S (= 44) must be a string
    '''
def frequency_distribution(S, n: int = 1, field=None):
    """
    The probability space of frequencies of n-character substrings of S.

    EXAMPLES::

        sage: frequency_distribution('banana not a nana nor ananas', 2)
        Discrete probability space defined by {' a': 0.0740740740740741,
         ' n': 0.111111111111111,
         'a ': 0.111111111111111,
         'an': 0.185185185185185,
         'as': 0.0370370370370370,
         'ba': 0.0370370370370370,
         'na': 0.222222222222222,
         'no': 0.0740740740740741,
         'or': 0.0370370370370370,
         'ot': 0.0370370370370370,
         'r ': 0.0370370370370370,
         't ': 0.0370370370370370}
    """
def coincidence_index(S, n: int = 1):
    '''
    Return the coincidence index of the string ``S``.

    EXAMPLES::

        sage: S = strip_encoding("The cat in the hat.")
        sage: coincidence_index(S)
        0.120879120879121
    '''
def coincidence_discriminant(S, n: int = 2):
    '''
    INPUT:

    - ``S`` --tuple of strings; e.g. produced as decimation of transposition
      ciphertext, or a sample plaintext

    OUTPUT:

    A measure of the difference of probability of association of
    character pairs, relative to their independent one-character probabilities.

    EXAMPLES::

        sage: S = strip_encoding("The cat in the hat.")
        sage: coincidence_discriminant([ S[i:i+2] for i in range(len(S)-1) ])
        0.0827001855677322
    '''
