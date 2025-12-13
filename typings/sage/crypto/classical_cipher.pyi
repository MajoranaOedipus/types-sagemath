from .cipher import SymmetricKeyCipher as SymmetricKeyCipher
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.monoids.string_monoid_element import StringMonoidElement as StringMonoidElement

class AffineCipher(SymmetricKeyCipher):
    """
    Affine cipher class. This is the class that does the actual work of
    encryption and decryption. Users should not directly instantiate or
    create objects of this class. Instead, functionalities of this class
    should be accessed via
    :class:`AffineCryptosystem <sage.crypto.classical.AffineCryptosystem>`
    as the latter provides a convenient user interface.
    """
    def __init__(self, parent, key) -> None:
        """
        Create an affine cipher.

        INPUT:

        - ``parent`` -- an ``AffineCryptosystem`` object

        - ``key`` -- a secret key; let `N` be the size of the cipher domain.
          A key of this affine cipher is an ordered pair
          `(a, b) \\in \\ZZ_N \\times \\ZZ_N` such that `\\gcd(a, N) = 1`.

        EXAMPLES:

        Testing of dumping and loading object::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: AC = A(3, 5)
            sage: AC == loads(dumps(AC))
            True
        """
    def __eq__(self, other):
        """
        Comparing this ``AffineCipher`` with ``other``. Two ``AffineCipher``
        objects are the same if they are of the same type, have the same
        parent, and share the same secret key.

        INPUT:

        - ``other`` -- another object to compare with

        OUTPUT: ``True`` if ``self`` and ``other`` are the same
        ``AffineCipher`` object; ``False`` otherwise

        EXAMPLES::

            sage: aff1 = AffineCryptosystem(AlphabeticStrings())
            sage: aff2 = AffineCryptosystem(AlphabeticStrings())
            sage: aff1 == aff2
            True
            sage: aff1(1, 2) == aff2(1, 2)
            True
        """
    def __call__(self, M):
        '''
        Return the ciphertext (respectively, plaintext) corresponding to
        ``M``. This is the main place where encryption and decryption takes
        place.

        INPUT:

        - ``M`` -- a message to be encrypted or decrypted. This message must
          be encoded using the plaintext or ciphertext alphabet. The current
          behaviour is that the plaintext and ciphertext alphabets are the
          same alphabet.

        - ``algorithm`` -- (default: ``\'encrypt\'``) whether to use the
          encryption or decryption algorithm on ``M``. The flag ``\'encrypt\'``
          signifies using the encryption algorithm, while ``\'decrypt\'``
          signifies using the decryption algorithm. The only acceptable
          values for ``algorithm`` are: ``\'encrypt\'`` and ``\'decrypt\'``.

        OUTPUT: the ciphertext or plaintext corresponding to ``M``

        EXAMPLES::

            sage: A = AffineCryptosystem(AlphabeticStrings()); A
            Affine cryptosystem on Free alphabetic string monoid on A-Z
            sage: P = A.encoding("The affine cryptosystem generalizes the shift cipher.")
            sage: P
            THEAFFINECRYPTOSYSTEMGENERALIZESTHESHIFTCIPHER
            sage: a, b = (9, 13)
            sage: E = A(a, b); E
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: C = E(P); C
            CYXNGGHAXFKVSCJTVTCXRPXAXKNIHEXTCYXTYHGCFHSYXK
            sage: aInv, bInv = A.inverse_key(a, b)
            sage: D = A(aInv, bInv); D
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: D(C)
            THEAFFINECRYPTOSYSTEMGENERALIZESTHESHIFTCIPHER
            sage: D(C) == P
            True
            sage: D(C) == P == D(E(P))
            True
        '''

class HillCipher(SymmetricKeyCipher):
    """
    Hill cipher class
    """
    def __init__(self, parent, key) -> None:
        '''
        Create a Hill cipher.

        EXAMPLES::

            sage: # needs sage.modules
            sage: S = AlphabeticStrings()
            sage: E = HillCryptosystem(S,3); E
            Hill cryptosystem on Free alphabetic string monoid on A-Z of block length 3
            sage: M = E.key_space()
            sage: A = M([[1,0,1],[0,1,1],[2,2,3]]); A
            [1 0 1]
            [0 1 1]
            [2 2 3]
            sage: e = E(A); e
            Hill cipher on Free alphabetic string monoid on A-Z of block length 3
            sage: e(S("LAMAISONBLANCHE"))
            JYVKSKQPELAYKPV

        TESTS::

            sage: S = AlphabeticStrings()
            sage: E = HillCryptosystem(S,3)                                             # needs sage.modules
            sage: E == loads(dumps(E))                                                  # needs sage.modules
            True
        '''
    def __eq__(self, right): ...
    def __call__(self, M): ...
    def inverse(self): ...

class ShiftCipher(SymmetricKeyCipher):
    """
    Shift cipher class. This is the class that does the actual work of
    encryption and decryption. Users should not directly instantiate or
    create objects of this class. Instead, functionalities of this class
    should be accessed via
    :class:`ShiftCryptosystem <sage.crypto.classical.ShiftCryptosystem>`
    as the latter provides a convenient user interface.
    """
    def __init__(self, parent, key) -> None:
        '''
        Create a shift cipher.

        INPUT:

        - ``parent`` -- a ``ShiftCryptosystem`` object

        - ``key`` -- a secret key

        EXAMPLES::

            sage: S = ShiftCryptosystem(AlphabeticStrings()); S
            Shift cryptosystem on Free alphabetic string monoid on A-Z
            sage: P = S.encoding("The shift cryptosystem generalizes the Caesar cipher.")
            sage: P
            THESHIFTCRYPTOSYSTEMGENERALIZESTHECAESARCIPHER
            sage: K = 7
            sage: C = S.enciphering(K, P); C
            AOLZOPMAJYFWAVZFZALTNLULYHSPGLZAOLJHLZHYJPWOLY
            sage: S.deciphering(K, C)
            THESHIFTCRYPTOSYSTEMGENERALIZESTHECAESARCIPHER
            sage: S.deciphering(K, C) == P
            True
        '''
    def __eq__(self, other):
        """
        Comparing this ``ShiftCipher`` with ``other``. Two ``ShiftCipher``
        objects are the same if they are of the same type, have the same
        parent, and share the same secret key.

        INPUT:

        - ``other`` -- another object to compare with

        OUTPUT: ``True`` if ``self`` and ``other`` are the same ``ShiftCipher``
        object; ``False`` otherwise.

        EXAMPLES::

            sage: shift1 = ShiftCryptosystem(AlphabeticStrings())
            sage: shift2 = ShiftCryptosystem(AlphabeticStrings())
            sage: shift1 == shift2
            True
            sage: shift1 = ShiftCryptosystem(HexadecimalStrings())
            sage: shift2 = ShiftCryptosystem(BinaryStrings())
            sage: shift1 == shift2
            False
        """
    def __call__(self, M):
        '''
        Return the ciphertext (respectively, plaintext) corresponding to
        ``M``. This is the main place where encryption and decryption takes
        place.

        INPUT:

        - ``M`` -- a message to be encrypted or decrypted. This message must
          be encoded using the plaintext or ciphertext alphabet. The current
          behaviour is that the plaintext and ciphertext alphabets are the
          same alphabet.

        OUTPUT: the ciphertext or plaintext corresponding to ``M``

        EXAMPLES:

        These are indirect doctests. Functionalities of this class are
        usually invoked from
        :class:`ShiftCryptosystem <sage.crypto.classical.ShiftCryptosystem>`.

        ::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: S.enciphering(12, S.encoding("Stop shifting me."))
            EFABETURFUZSYQ
            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: S.enciphering(7, S.encoding("Shift me now."))
            cadfd0ddeb97d4dc97d5d6ee95
            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: S.enciphering(1, S.encoding("OK, enough shifting."))
            1011000010110100110100111101111110011010100100011001000010001010100110001001011111011111100011001001011110010110100110011000101110010110100100011001100011010001
        '''

class SubstitutionCipher(SymmetricKeyCipher):
    """
    Substitution cipher class
    """
    def __init__(self, parent, key) -> None:
        '''
        Create a substitution cipher.

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = SubstitutionCryptosystem(S)
            sage: E
            Substitution cryptosystem on Free alphabetic string monoid on A-Z
            sage: K = S([ 25-i for i in range(26) ])
            sage: K
            ZYXWVUTSRQPONMLKJIHGFEDCBA
            sage: e = E(K)
            sage: m = S("THECATINTHEHAT")
            sage: e(m)
            GSVXZGRMGSVSZG

        TESTS::

            sage: S = AlphabeticStrings()
            sage: E = SubstitutionCryptosystem(S)
            sage: E == loads(dumps(E))
            True
        '''
    def __eq__(self, right): ...
    def __call__(self, M): ...
    def inverse(self): ...

class TranspositionCipher(SymmetricKeyCipher):
    """
    Transition cipher class
    """
    def __init__(self, parent, key) -> None:
        '''
        Create a transposition cipher.

        EXAMPLES::

            sage: # needs sage.groups
            sage: S = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(S,14); E
            Transposition cryptosystem on
             Free alphabetic string monoid on A-Z of block length 14
            sage: K = [ 14-i for i in range(14) ]; K
            [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            sage: e = E(K)
            sage: m = S("THECATINTHEHAT")
            sage: e(m)
            TAHEHTNITACEHT

        EXAMPLES::

            sage: # needs sage.groups
            sage: S = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(S,15)
            sage: m = S("THECATANDTHEHAT")
            sage: G = E.key_space(); G
            Symmetric group of order 15! as a permutation group
            sage: g = G([ 3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13 ])
            sage: e = E(g)
            sage: e(m)
            EHTTACDNAEHTTAH

        TESTS::

            sage: S = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(S,14)                                   # needs sage.groups
            sage: E == loads(dumps(E))                                                  # needs sage.groups
            True
        '''
    def __call__(self, M, mode: str = 'ECB'): ...
    def inverse(self): ...

class VigenereCipher(SymmetricKeyCipher):
    """
    Vigenere cipher class
    """
    def __init__(self, parent, key) -> None:
        '''
        Create a Vigenere cipher.

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = VigenereCryptosystem(S,11)
            sage: K = S("SHAKESPEARE")
            sage: e = E(K)
            sage: m = S("THECATINTHEHAT")
            sage: e(m)
            LOEMELXRTYIZHT

        TESTS::

            sage: S = AlphabeticStrings()
            sage: E = VigenereCryptosystem(S,11)
            sage: E == loads(dumps(E))
            True
        '''
    def __call__(self, M, mode: str = 'ECB'): ...
    def inverse(self): ...
