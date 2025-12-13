from .free_monoid_element import FreeMonoidElement as FreeMonoidElement
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.structure.richcmp import richcmp as richcmp

def is_StringMonoidElement(x): ...
def is_AlphabeticStringMonoidElement(x): ...
def is_BinaryStringMonoidElement(x): ...
def is_OctalStringMonoidElement(x): ...
def is_HexadecimalStringMonoidElement(x): ...
def is_Radix64StringMonoidElement(x): ...

class StringMonoidElement(FreeMonoidElement):
    """
    Element of a free string monoid.
    """
    def __init__(self, S, x, check: bool = True) -> None:
        """
        Create the element ``x`` of the StringMonoid ``S``.

        This should typically be called by a StringMonoid.
        """
    def __mul__(self, y):
        """
        Multiply 2 free string monoid elements.

        EXAMPLES::

            sage: S = BinaryStrings()
            sage: (x,y) = S.gens()
            sage: x*y
            01
        """
    def __pow__(self, n):
        """
        Return the `n`-th power of the string element.

        EXAMPLES::

            sage: (x,y) = BinaryStrings().gens()
            sage: x**3 * y**5 * x**7
            000111110000000
            sage: x**0


        Note that raising to a negative power is *not* a constructor
        for an element of the corresponding free group (yet).

        ::

            sage: x**(-1)
            Traceback (most recent call last):
            ...
            IndexError: Argument n (= -1) must be nonnegative.
        """
    def __len__(self) -> int:
        """
        Return the number of products that occur in this monoid element.
        For example, the length of the identity is 0, and the length
        of the monoid `x_0^2x_1` is three.

        EXAMPLES::

            sage: S = BinaryStrings()
            sage: z = S('')
            sage: len(z)
            0
            sage: (x,y) = S.gens()
            sage: len(x**2 * y**3)
            5
        """
    def __iter__(self):
        """
        Return an iterator over this element as a string.

        EXAMPLES::

            sage: t = AlphabeticStrings()('SHRUBBERY')
            sage: next(t.__iter__())
            S
            sage: list(t)
            [S, H, R, U, B, B, E, R, Y]
        """
    def __getitem__(self, n):
        """
        Return the n-th string character.

        EXAMPLES::

            sage: t = AlphabeticStrings()('SHRUBBERY')
            sage: t[0]
            S
            sage: t[3]
            U
            sage: t[-1]
            Y
        """
    def decoding(self, padic: bool = False):
        '''
        The byte string associated to a binary or hexadecimal string
        monoid element.

        EXAMPLES::

            sage: S = HexadecimalStrings()
            sage: s = S.encoding("A..Za..z"); s
            412e2e5a612e2e7a
            sage: s.decoding()
            \'A..Za..z\'
            sage: s = S.encoding("A..Za..z",padic=True); s
            14e2e2a516e2e2a7
            sage: s.decoding()
            \'\\x14\\xe2\\xe2\\xa5\\x16\\xe2\\xe2\\xa7\'
            sage: s.decoding(padic=True)
            \'A..Za..z\'
            sage: S = BinaryStrings()
            sage: s = S.encoding("A..Za..z"); s
            0100000100101110001011100101101001100001001011100010111001111010
            sage: s.decoding()
            \'A..Za..z\'
            sage: s = S.encoding("A..Za..z",padic=True); s
            1000001001110100011101000101101010000110011101000111010001011110
            sage: s.decoding()
            \'\\x82ttZ\\x86tt^\'
            sage: s.decoding(padic=True)
            \'A..Za..z\'
        '''
    def coincidence_index(self, prec: int = 0):
        """
        Return the probability of two randomly chosen characters being equal.
        """
    def character_count(self):
        '''
        Return the count of each unique character.

        EXAMPLES:

        Count the character frequency in an object comprised of capital
        letters of the English alphabet::

            sage: M = AlphabeticStrings().encoding("abcabf")
            sage: sorted(M.character_count().items())
            [(A, 2), (B, 2), (C, 1), (F, 1)]

        In an object comprised of binary numbers::

            sage: M = BinaryStrings().encoding("abcabf")
            sage: sorted(M.character_count().items())
            [(0, 28), (1, 20)]

        In an object comprised of octal numbers::

            sage: A = OctalStrings()
            sage: M = A([1, 2, 3, 2, 5, 3])
            sage: sorted(M.character_count().items())
            [(1, 1), (2, 2), (3, 2), (5, 1)]

        In an object comprised of hexadecimal numbers::

            sage: A = HexadecimalStrings()
            sage: M = A([1, 2, 4, 6, 2, 4, 15])
            sage: sorted(M.character_count().items())
            [(1, 1), (2, 2), (4, 2), (6, 1), (f, 1)]

        In an object comprised of radix-64 characters::

            sage: A = Radix64Strings()
            sage: M = A([1, 2, 63, 45, 45, 10]); M
            BC/ttK
            sage: sorted(M.character_count().items())
            [(B, 1), (C, 1), (K, 1), (t, 2), (/, 1)]

        TESTS:

        Empty strings return no counts of character frequency::

            sage: M = AlphabeticStrings().encoding("")
            sage: M.character_count()
            {}
            sage: M = BinaryStrings().encoding("")
            sage: M.character_count()
            {}
            sage: A = OctalStrings()
            sage: M = A([])
            sage: M.character_count()
            {}
            sage: A = HexadecimalStrings()
            sage: M = A([])
            sage: M.character_count()
            {}
            sage: A = Radix64Strings()
            sage: M = A([])
            sage: M.character_count()
            {}
        '''
    def frequency_distribution(self, length: int = 1, prec: int = 0):
        '''
        Return the probability space of character frequencies.

        The output of this method is different from that of the method
        :func:`characteristic_frequency()
        <sage.monoids.string_monoid.AlphabeticStringMonoid.characteristic_frequency>`.

        One can think of the characteristic frequency probability of an
        element in an alphabet `A` as the expected probability of that element
        occurring. Let `S` be a string encoded using elements of `A`. The
        frequency probability distribution corresponding to `S` provides us
        with the frequency probability of each element of `A` as observed
        occurring in `S`. Thus one distribution provides expected
        probabilities, while the other provides observed probabilities.

        INPUT:

        - ``length`` -- (default: ``1``) if ``length=1`` then consider the
          probability space of monogram frequency, i.e. probability
          distribution of single characters. If ``length=2`` then consider
          the probability space of digram frequency, i.e. probability
          distribution of pairs of characters. This method currently
          supports the generation of probability spaces for monogram
          frequency (``length=1``) and digram frequency (``length=2``).

        - ``prec`` -- (default: ``0``) a nonnegative integer representing
          the precision (in number of bits) of a floating-point number. The
          default value ``prec=0`` means that we use 53 bits to represent
          the mantissa of a floating-point number. For more information on
          the precision of floating-point numbers, see the function
          :func:`RealField() <sage.rings.real_mpfr.RealField>` or refer to the module
          :mod:`real_mpfr <sage.rings.real_mpfr>`.

        EXAMPLES:

        Capital letters of the English alphabet::

            sage: M = AlphabeticStrings().encoding("abcd")
            sage: L = M.frequency_distribution().function()
            sage: sorted(L.items())
            <BLANKLINE>
            [(A, 0.250000000000000),
            (B, 0.250000000000000),
            (C, 0.250000000000000),
            (D, 0.250000000000000)]

        The binary number system::

            sage: M = BinaryStrings().encoding("abcd")
            sage: L = M.frequency_distribution().function()
            sage: sorted(L.items())
            [(0, 0.593750000000000), (1, 0.406250000000000)]

        The hexadecimal number system::

            sage: M = HexadecimalStrings().encoding("abcd")
            sage: L = M.frequency_distribution().function()
            sage: sorted(L.items())
            <BLANKLINE>
            [(1, 0.125000000000000),
            (2, 0.125000000000000),
            (3, 0.125000000000000),
            (4, 0.125000000000000),
            (6, 0.500000000000000)]

        Get the observed frequency probability distribution of digrams in the
        string "ABCD". This string consists of the following digrams: "AB",
        "BC", and "CD". Now find out the frequency probability of each of
        these digrams as they occur in the string "ABCD"::

            sage: M = AlphabeticStrings().encoding("abcd")
            sage: D = M.frequency_distribution(length=2).function()
            sage: sorted(D.items())
            [(AB, 0.333333333333333), (BC, 0.333333333333333), (CD, 0.333333333333333)]
        '''
