from sage.structure.sage_object import SageObject as SageObject

def frequency_table(string):
    '''
    Return the frequency table corresponding to the given string.

    INPUT:

    - ``string`` -- string of symbols over some alphabet

    OUTPUT:

    - A table of frequency of each unique symbol in ``string``. If ``string``
      is an empty string, return an empty table.

    EXAMPLES:

    The frequency table of a non-empty string::

        sage: from sage.coding.source_coding.huffman import frequency_table
        sage: str = "Stop counting my characters!"
        sage: T = sorted(frequency_table(str).items())
        sage: for symbol, code in T:
        ....:     print("{} {}".format(symbol, code))
          3
        ! 1
        S 1
        a 2
        c 3
        e 1
        g 1
        h 1
        i 1
        m 1
        n 2
        o 2
        p 1
        r 2
        s 1
        t 3
        u 1
        y 1

    The frequency of an empty string::

        sage: frequency_table("")
        defaultdict(<... \'int\'>, {})
    '''

class Huffman(SageObject):
    '''
    This class implements the basic functionalities of Huffman codes.

    It can build a Huffman code from a given string, or from the information
    of a dictionary associating to each key (the elements of the alphabet) a
    weight (most of the time, a probability value or a number of occurrences).

    INPUT:

    - ``source`` -- can be either

      - A string from which the Huffman encoding should be created.

      - A dictionary that associates to each symbol of an alphabet a numeric
        value. If we consider the frequency of each alphabetic symbol, then
        ``source`` is considered as the frequency table of the alphabet with
        each numeric (nonnegative integer) value being the number of
        occurrences of a symbol. The numeric values can also represent weights
        of the symbols. In that case, the numeric values are not necessarily
        integers, but can be real numbers.

    In order to construct a Huffman code for an alphabet, we use exactly one of
    the following methods:

    #. Let ``source`` be a string of symbols over an alphabet and feed
       ``source`` to the constructor of this class. Based on the input string, a
       frequency table is constructed that contains the frequency of each unique
       symbol in ``source``. The alphabet in question is then all the unique
       symbols in ``source``. A significant implication of this is that any
       subsequent string that we want to encode must contain only symbols that
       can be found in ``source``.

    #. Let ``source`` be the frequency table of an alphabet. We can feed this
       table to the constructor of this class. The table ``source`` can be a
       table of frequencies or a table of weights.

    In either case, the alphabet must consist of at least two symbols.

    EXAMPLES::

        sage: from sage.coding.source_coding.huffman import Huffman, frequency_table
        sage: h1 = Huffman("There once was a french fry")
        sage: for letter, code in sorted(h1.encoding_table().items()):
        ....:     print("\'{}\' : {}".format(letter, code))
        \' \' : 00
        \'T\' : 11100
        \'a\' : 0111
        \'c\' : 1010
        \'e\' : 100
        \'f\' : 1011
        \'h\' : 1100
        \'n\' : 1101
        \'o\' : 11101
        \'r\' : 010
        \'s\' : 11110
        \'w\' : 11111
        \'y\' : 0110

    We can obtain the same result by "training" the Huffman code with the
    following table of frequency::

        sage: ft = frequency_table("There once was a french fry")
        sage: sorted(ft.items())
        [(\' \', 5),
         (\'T\', 1),
         (\'a\', 2),
         (\'c\', 2),
         (\'e\', 4),
         (\'f\', 2),
         (\'h\', 2),
         (\'n\', 2),
         (\'o\', 1),
         (\'r\', 3),
         (\'s\', 1),
         (\'w\', 1),
         (\'y\', 1)]

        sage: h2 = Huffman(ft)

    Once ``h1`` has been trained, and hence possesses an encoding table,
    it is possible to obtain the Huffman encoding of any string
    (possibly the same) using this code::

        sage: encoded = h1.encode("There once was a french fry"); encoded
        \'11100110010001010000111011101101010000111110111111100001110010110101001101101011000010110100110\'

    We can decode the above encoded string in the following way::

        sage: h1.decode(encoded)
        \'There once was a french fry\'

    Obviously, if we try to decode a string using a Huffman instance which
    has been trained on a different sample (and hence has a different encoding
    table), we are likely to get some random-looking string::

        sage: h3 = Huffman("There once were two french fries")
        sage: h3.decode(encoded)
        \' eierhffcoeft TfewrnwrTrsc\'

    This does not look like our original string.

    Instead of using frequency, we can assign weights to each alphabetic
    symbol::

        sage: from sage.coding.source_coding.huffman import Huffman
        sage: T = {"a":45, "b":13, "c":12, "d":16, "e":9, "f":5}
        sage: H = Huffman(T)
        sage: L = ["deaf", "bead", "fab", "bee"]
        sage: E = []
        sage: for e in L:
        ....:     E.append(H.encode(e))
        ....:     print(E[-1])
        111110101100
        10111010111
        11000101
        10111011101
        sage: D = []
        sage: for e in E:
        ....:     D.append(H.decode(e))
        ....:     print(D[-1])
        deaf
        bead
        fab
        bee
        sage: D == L
        True
    '''
    def __init__(self, source) -> None:
        '''
        Constructor for Huffman.

        See the docstring of this class for full documentation.

        EXAMPLES::

            sage: from sage.coding.source_coding.huffman import Huffman
            sage: str = "Sage is my most favorite general purpose computer algebra system"
            sage: h = Huffman(str)

        TESTS:

        Feeding anything else than a string or a dictionary::

            sage: Huffman(Graph())                                                      # needs sage.graphs
            Traceback (most recent call last):
            ...
            ValueError: Input must be either a string or a dictionary.
        '''
    def encode(self, string):
        '''
        Encode the given string based on the current encoding table.

        INPUT:

        - ``string`` -- string of symbols over an alphabet

        OUTPUT: a Huffman encoding of ``string``

        EXAMPLES:

        This is how a string is encoded and then decoded::

            sage: from sage.coding.source_coding.huffman import Huffman
            sage: str = "Sage is my most favorite general purpose computer algebra system"
            sage: h = Huffman(str)
            sage: encoded = h.encode(str); encoded
            \'11000011010001010101100001111101001110011101001101101111011110111001111010000101101110100000111010101000101000000010111011011000110100101001011100010011011110101011100100110001100101001001110101110101110110001000101011000111101101101111110011111101110100011\'
            sage: h.decode(encoded)
            \'Sage is my most favorite general purpose computer algebra system\'
        '''
    def decode(self, string):
        '''
        Decode the given string using the current encoding table.

        INPUT:

        - ``string`` -- string of Huffman encodings

        OUTPUT: the Huffman decoding of ``string``

        EXAMPLES:

        This is how a string is encoded and then decoded::

            sage: from sage.coding.source_coding.huffman import Huffman
            sage: str = "Sage is my most favorite general purpose computer algebra system"
            sage: h = Huffman(str)
            sage: encoded = h.encode(str); encoded
            \'11000011010001010101100001111101001110011101001101101111011110111001111010000101101110100000111010101000101000000010111011011000110100101001011100010011011110101011100100110001100101001001110101110101110110001000101011000111101101101111110011111101110100011\'
            sage: h.decode(encoded)
            \'Sage is my most favorite general purpose computer algebra system\'

        TESTS:

        Of course, the string one tries to decode has to be a binary one. If
        not, an exception is raised::

            sage: h.decode(\'I clearly am not a binary string\')
            Traceback (most recent call last):
            ...
            ValueError: Input must be a binary string.
        '''
    def encoding_table(self):
        '''
        Return the current encoding table.

        INPUT:

        - None.

        OUTPUT: a dictionary associating an alphabetic symbol to a Huffman encoding

        EXAMPLES::

            sage: from sage.coding.source_coding.huffman import Huffman
            sage: str = "Sage is my most favorite general purpose computer algebra system"
            sage: h = Huffman(str)
            sage: T = sorted(h.encoding_table().items())
            sage: for symbol, code in T:
            ....:     print("{} {}".format(symbol, code))
              101
            S 110000
            a 1101
            b 110001
            c 110010
            e 010
            f 110011
            g 0001
            i 10000
            l 10001
            m 0011
            n 00000
            o 0110
            p 0010
            r 1110
            s 1111
            t 0111
            u 10010
            v 00001
            y 10011
        '''
    def tree(self):
        '''
        Return the Huffman tree corresponding to the current encoding.

        INPUT:

        - None.

        OUTPUT: the binary tree representing a Huffman code

        EXAMPLES::

            sage: from sage.coding.source_coding.huffman import Huffman
            sage: str = "Sage is my most favorite general purpose computer algebra system"
            sage: h = Huffman(str)
            sage: T = h.tree(); T                                                       # needs sage.graphs
            Digraph on 39 vertices
            sage: T.show(figsize=[20,20])                                               # needs sage.graphs sage.plot
            <BLANKLINE>
        '''
