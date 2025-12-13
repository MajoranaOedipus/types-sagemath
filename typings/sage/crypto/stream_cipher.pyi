from .cipher import SymmetricKeyCipher as SymmetricKeyCipher
from .lfsr import lfsr_sequence as lfsr_sequence
from sage.monoids.string_monoid_element import StringMonoidElement as StringMonoidElement

class LFSRCipher(SymmetricKeyCipher):
    def __init__(self, parent, poly, IS) -> None:
        '''
        Create a linear feedback shift register (LFSR) cipher.

        INPUT:

        - ``parent`` -- parent

        - ``poly`` -- connection polynomial

        - ``IS`` -- initial state

        EXAMPLES::

            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: E = LFSRCryptosystem(FF)
            sage: E
            LFSR cryptosystem over Finite Field of size 2
            sage: IS = [ FF(a) for a in [0,1,1,1,0,1,1] ]
            sage: g = x^7 + x + 1
            sage: e = E((g,IS))
            sage: B = BinaryStrings()
            sage: m = B.encoding("THECATINTHEHAT")
            sage: e(m)
            0010001101111010111010101010001100000000110100010101011100001011110010010000011111100100100011001101101000001111
            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: LFSR = LFSRCryptosystem(FF)
            sage: e = LFSR((x^2+x+1,[FF(0),FF(1)]))
            sage: B = e.domain()
            sage: m = B.encoding("The cat in the hat.")
            sage: e(m)
            00111001110111101011111001001101110101011011101000011001100101101011001000000011100101101010111100000101110100111111101100000101110101111010111101000011
            sage: m == e(e(m))
            True

        TESTS::

            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: E = LFSRCryptosystem(FF)
            sage: E == loads(dumps(E))
            True
        '''
    def __call__(self, M, mode: str = 'ECB'):
        """
        Generate key stream from the binary string ``M``.

        INPUT:

        - ``M`` -- a StringMonoidElement

        - ``mode`` -- ignored (default: ``'ECB'``)

        EXAMPLES::

            sage: k = GF(2)
            sage: P.<x> = PolynomialRing( k )
            sage: LFSR = LFSRCryptosystem( k )
            sage: e = LFSR((x^2+x+1,[k(0), k(1)]))
            sage: B = e.domain()
            sage: m = B.encoding('The cat in the hat.')
            sage: e(m)
            00111001110111101011111001001101110101011011101000011001100101101011001000000011100101101010111100000101110100111111101100000101110101111010111101000011
        """
    def connection_polynomial(self):
        """
        The connection polynomial defining the LFSR of the cipher.

        EXAMPLES::

            sage: k = GF(2)
            sage: P.<x> = PolynomialRing( k )
            sage: LFSR = LFSRCryptosystem( k )
            sage: e = LFSR((x^2+x+1,[k(0), k(1)]))
            sage: e.connection_polynomial()
            x^2 + x + 1
        """
    def initial_state(self):
        """
        The initial state of the LFSR cipher.

        EXAMPLES::

            sage: k = GF(2)
            sage: P.<x> = PolynomialRing( k )
            sage: LFSR = LFSRCryptosystem( k )
            sage: e = LFSR((x^2+x+1,[k(0), k(1)]))
            sage: e.initial_state()
            [0, 1]
        """

class ShrinkingGeneratorCipher(SymmetricKeyCipher):
    def __init__(self, parent, e1, e2) -> None:
        """
        Create a shrinking generator cipher.

        INPUT:

        - ``parent`` -- parent

        - ``poly`` -- connection polynomial

        - ``IS`` -- initial state

        EXAMPLES::

            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: LFSR = LFSRCryptosystem(FF)
            sage: IS_1 = [ FF(a) for a in [0,1,0,1,0,0,0] ]
            sage: e1 = LFSR((x^7 + x + 1,IS_1))
            sage: IS_2 = [ FF(a) for a in [0,0,1,0,0,0,1,0,1] ]
            sage: e2 = LFSR((x^9 + x^3 + 1,IS_2))
            sage: E = ShrinkingGeneratorCryptosystem()
            sage: e = E((e1,e2))
            sage: e
            Shrinking generator cipher on Free binary string monoid
        """
    def keystream_cipher(self):
        """
        The LFSR cipher generating the output key stream.

        EXAMPLES::

            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: LFSR = LFSRCryptosystem(FF)
            sage: IS_1 = [ FF(a) for a in [0,1,0,1,0,0,0] ]
            sage: e1 = LFSR((x^7 + x + 1,IS_1))
            sage: IS_2 = [ FF(a) for a in [0,0,1,0,0,0,1,0,1] ]
            sage: e2 = LFSR((x^9 + x^3 + 1,IS_2))
            sage: E = ShrinkingGeneratorCryptosystem()
            sage: e = E((e1,e2))
            sage: e.keystream_cipher()
            LFSR cipher on Free binary string monoid
        """
    def decimating_cipher(self):
        """
        The LFSR cipher generating the decimating key stream.

        EXAMPLES::

            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: LFSR = LFSRCryptosystem(FF)
            sage: IS_1 = [ FF(a) for a in [0,1,0,1,0,0,0] ]
            sage: e1 = LFSR((x^7 + x + 1,IS_1))
            sage: IS_2 = [ FF(a) for a in [0,0,1,0,0,0,1,0,1] ]
            sage: e2 = LFSR((x^9 + x^3 + 1,IS_2))
            sage: E = ShrinkingGeneratorCryptosystem()
            sage: e = E((e1,e2))
            sage: e.decimating_cipher()
            LFSR cipher on Free binary string monoid
        """
    def __call__(self, M, mode: str = 'ECB'):
        '''
        INPUT:

        - ``M`` -- a StringMonoidElement

        - ``mode`` -- ignored (default: ``\'ECB\'``)

        EXAMPLES::

            sage: FF = FiniteField(2)
            sage: P.<x> = PolynomialRing(FF)
            sage: LFSR = LFSRCryptosystem(FF)
            sage: IS_1 = [ FF(a) for a in [0,1,0,1,0,0,0] ]
            sage: e1 = LFSR((x^7 + x + 1,IS_1))
            sage: IS_2 = [ FF(a) for a in [0,0,1,0,0,0,1,0,1] ]
            sage: e2 = LFSR((x^9 + x^3 + 1,IS_2))
            sage: E = ShrinkingGeneratorCryptosystem()
            sage: e = E((e1,e2))
            sage: B = BinaryStrings()
            sage: m = B.encoding("THECATINTHEHAT")
            sage: c = e(m)
            sage: c.decoding()
            "t\\xb6\\xc1\'\\x83\\x17\\xae\\xc9ZO\\x84V\\x7fX"
            sage: e(e(m)) == m
            True
            sage: m.decoding()
            \'THECATINTHEHAT\'
        '''
