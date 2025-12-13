from sage.matrix.matrix_dense import Matrix_dense as Matrix_dense
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.monoids.string_monoid import BinaryStrings as BinaryStrings
from sage.monoids.string_monoid_element import StringMonoidElement as StringMonoidElement
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class MiniAES(SageObject):
    '''
    This class implements the Mini Advanced Encryption Standard (Mini-AES)
    described in [Pha2002]_. Note that Phan\'s Mini-AES is for educational purposes
    only and is not secure for practical purposes. Mini-AES is a version of
    the AES with all parameters significantly reduced, but at the same time
    preserving the structure of AES. The goal of Mini-AES is to allow a
    beginner to understand the structure of AES, thus laying a foundation
    for a thorough study of AES. Its goal is as a teaching tool and is
    different from the :mod:`SR <sage.crypto.mq.sr>` small scale variants
    of the AES. SR defines a family of parameterizable variants of the AES
    suitable as a framework for comparing different cryptanalytic techniques
    that can be brought to bear on the AES.

    EXAMPLES:

    Encrypt a plaintext::

        sage: from sage.crypto.block_cipher.miniaes import MiniAES
        sage: maes = MiniAES()
        sage: K = FiniteField(16, "x")
        sage: MS = MatrixSpace(K, 2, 2)
        sage: P = MS([K("x^3 + x"), K("x^2 + 1"), K("x^2 + x"), K("x^3 + x^2")]); P
        <BLANKLINE>
        [  x^3 + x   x^2 + 1]
        [  x^2 + x x^3 + x^2]
        sage: key = MS([K("x^3 + x^2"), K("x^3 + x"), K("x^3 + x^2 + x"), K("x^2 + x + 1")]); key
        <BLANKLINE>
        [    x^3 + x^2       x^3 + x]
        [x^3 + x^2 + x   x^2 + x + 1]
        sage: C = maes.encrypt(P, key); C
        [    x^3 + x^2 + 1 x^3 + x^2 + x + 1]
        [                x     x^3 + x^2 + x]

    Decrypt the result::

        sage: plaintxt = maes.decrypt(C, key)
        sage: plaintxt; P
        <BLANKLINE>
        [  x^3 + x   x^2 + 1]
        [  x^2 + x x^3 + x^2]
        <BLANKLINE>
        [  x^3 + x   x^2 + 1]
        [  x^2 + x x^3 + x^2]
        sage: plaintxt == P
        True

    We can also work directly with binary strings::

        sage: from sage.crypto.block_cipher.miniaes import MiniAES
        sage: maes = MiniAES()
        sage: bin = BinaryStrings()
        sage: key = bin.encoding("KE"); key
        0100101101000101
        sage: P = bin.encoding("Encrypt this secret message!"); P
        01000101011011100110001101110010011110010111000001110100001000000111010001101000011010010111001100100000011100110110010101100011011100100110010101110100001000000110110101100101011100110111001101100001011001110110010100100001
        sage: C = maes(P, key, algorithm=\'encrypt\'); C
        11100000101000010110001101101001110110010010111011010001100111100000101000101111100110010010100001110101011100111001000010101000001111000101010011010001100111100111001100000001101100110110101001001000011100000101010110110101
        sage: plaintxt = maes(C, key, algorithm=\'decrypt\')
        sage: plaintxt == P
        True

    Now we work with integers `n` such that `0 \\leq n \\leq 15`::

        sage: from sage.crypto.block_cipher.miniaes import MiniAES
        sage: maes = MiniAES()
        sage: P = [n for n in range(16)]; P
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        sage: key = [2, 3, 11, 0]; key
        [2, 3, 11, 0]
        sage: P = maes.integer_to_binary(P); P
        0000000100100011010001010110011110001001101010111100110111101111
        sage: key = maes.integer_to_binary(key); key
        0010001110110000
        sage: C = maes(P, key, algorithm=\'encrypt\'); C
        0011101000101110010011000101010100011101010000111000100100011010
        sage: plaintxt = maes(C, key, algorithm=\'decrypt\')
        sage: plaintxt == P
        True

    Generate some random plaintext and a random secret key. Encrypt the
    plaintext using that secret key and decrypt the result. Then compare the
    decrypted plaintext with the original plaintext::

        sage: from sage.crypto.block_cipher.miniaes import MiniAES
        sage: maes = MiniAES()
        sage: MS = MatrixSpace(FiniteField(16, "x"), 2, 2)
        sage: P = MS.random_element()
        sage: key = maes.random_key()
        sage: C = maes.encrypt(P, key)
        sage: plaintxt = maes.decrypt(C, key)
        sage: plaintxt == P
        True
    '''
    def __init__(self) -> None:
        '''
        A simplified variant of the Advanced Encryption Standard (AES).

        EXAMPLES::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES(); maes
            Mini-AES block cipher with 16-bit keys
            sage: MS = MatrixSpace(FiniteField(16, "x"), 2, 2)
            sage: P = MS.random_element()
            sage: key = maes.random_key()
            sage: C = maes.encrypt(P, key)
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt == P
            True
        '''
    def __call__(self, B, key, algorithm: str = 'encrypt'):
        '''
        Apply Mini-AES encryption or decryption on the binary string ``B``
        using the key ``key``.  The flag ``algorithm`` controls what action is
        to be performed on ``B``.

        INPUT:

        - ``B`` -- a binary string, where the number of bits is positive and
          a multiple of 16. The number of 16 bits is evenly divided into four
          nibbles. Hence 16 bits can be conveniently represented as a
          `2 \\times 2` matrix block for encryption or decryption.

        - ``key`` -- a secret key; this must be a 16-bit binary string

        - ``algorithm`` -- (default: ``\'encrypt\'``) a string; a flag to signify
          whether encryption or decryption is to be applied to the binary
          string ``B``. The encryption flag is ``\'encrypt\'`` and the decryption
          flag is ``\'decrypt\'``.

        OUTPUT:

        - The ciphertext (respectively plaintext) corresponding to the
          binary string ``B``.

        EXAMPLES::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: bin = BinaryStrings()
            sage: key = bin.encoding("KE"); key
            0100101101000101
            sage: P = bin.encoding("Encrypt this secret message!"); P
            01000101011011100110001101110010011110010111000001110100001000000111010001101000011010010111001100100000011100110110010101100011011100100110010101110100001000000110110101100101011100110111001101100001011001110110010100100001
            sage: C = maes(P, key, algorithm=\'encrypt\'); C
            11100000101000010110001101101001110110010010111011010001100111100000101000101111100110010010100001110101011100111001000010101000001111000101010011010001100111100111001100000001101100110110101001001000011100000101010110110101
            sage: plaintxt = maes(C, key, algorithm=\'decrypt\')
            sage: plaintxt == P
            True

        TESTS:

        The binary string ``B`` must be non-empty and the number of bits must
        be a multiple of 16::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes("B", "key")
            Traceback (most recent call last):
            ...
            TypeError: input B must be a non-empty binary string with number of bits a multiple of 16
            sage: bin = BinaryStrings()
            sage: B = bin.encoding("A")
            sage: maes(B, "key")
            Traceback (most recent call last):
            ...
            ValueError: the number of bits in the binary string B must be positive and a multiple of 16

        The secret key ``key`` must be a 16-bit binary string::

            sage: B = bin.encoding("ABCD")
            sage: maes(B, "key")
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 16-bit binary string
            sage: key = bin.encoding("K")
            sage: maes(B, key)
            Traceback (most recent call last):
            ...
            ValueError: secret key must be a 16-bit binary string

        The value for ``algorithm`` must be either ``\'encrypt\'`` or
        ``\'decrypt\'``::

            sage: B = bin.encoding("ABCD")
            sage: key = bin.encoding("KE")
            sage: maes(B, key, algorithm=\'ABC\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be either \'encrypt\' or \'decrypt\'
            sage: maes(B, key, algorithm=\'e\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be either \'encrypt\' or \'decrypt\'
            sage: maes(B, key, algorithm=\'d\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be either \'encrypt\' or \'decrypt\'
        '''
    def __eq__(self, other):
        """
        Compare ``self`` with ``other``.

        Mini-AES objects are the same if they have the same key size and
        the same S-boxes.

        EXAMPLES::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: m = MiniAES()
            sage: m == loads(dumps(m))
            True
        """
    def add_key(self, block, rkey):
        '''
        Return the matrix addition of ``block`` and ``rkey``. Both ``block``
        and ``rkey`` are `2 \\times 2` matrices over the finite field
        `\\GF{2^4}`. This method just return the matrix addition of
        these two matrices.

        INPUT:

        - ``block`` -- a `2 \\times 2` matrix with entries over
          `\\GF{2^4}`

        - ``rkey`` -- a round key; a `2 \\times 2` matrix with entries over
          `\\GF{2^4}`

        OUTPUT: the matrix addition of ``block`` and ``rkey``

        EXAMPLES:

        We can work with elements of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: D = MS([ [K("x^3 + x^2 + x + 1"), K("x^3 + x")], [K("0"), K("x^3 + x^2")] ]); D
            <BLANKLINE>
            [x^3 + x^2 + x + 1           x^3 + x]
            [                0         x^3 + x^2]
            sage: k = MS([ [K("x^2 + 1"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ]); k
            <BLANKLINE>
            [          x^2 + 1 x^3 + x^2 + x + 1]
            [            x + 1                 0]
            sage: maes.add_key(D, k)
            <BLANKLINE>
            [  x^3 + x   x^2 + 1]
            [    x + 1 x^3 + x^2]

        Or work with binary strings::

            sage: bin = BinaryStrings()
            sage: B = bin.encoding("We"); B
            0101011101100101
            sage: B = MS(maes.binary_to_GF(B)); B
            <BLANKLINE>
            [    x^2 + 1 x^2 + x + 1]
            [    x^2 + x     x^2 + 1]
            sage: key = bin.encoding("KY"); key
            0100101101011001
            sage: key = MS(maes.binary_to_GF(key)); key
            <BLANKLINE>
            [        x^2 x^3 + x + 1]
            [    x^2 + 1     x^3 + 1]
            sage: maes.add_key(B, key)
            <BLANKLINE>
            [        1 x^3 + x^2]
            [    x + 1 x^3 + x^2]

        We can also work with integers `n` such that `0 \\leq n \\leq 15`::

            sage: N = [2, 3, 5, 7]; N
            [2, 3, 5, 7]
            sage: key = [9, 11, 13, 15]; key
            [9, 11, 13, 15]
            sage: N = MS(maes.integer_to_GF(N)); N
            <BLANKLINE>
            [          x       x + 1]
            [    x^2 + 1 x^2 + x + 1]
            sage: key = MS(maes.integer_to_GF(key)); key
            <BLANKLINE>
            [          x^3 + 1       x^3 + x + 1]
            [    x^3 + x^2 + 1 x^3 + x^2 + x + 1]
            sage: maes.add_key(N, key)
            <BLANKLINE>
            [x^3 + x + 1         x^3]
            [        x^3         x^3]

        TESTS:

        The input block and key must each be a matrix::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MSB = MatrixSpace(K, 2, 2)
            sage: B = MSB([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ])
            sage: maes.add_key(B, "key")
            Traceback (most recent call last):
            ...
            TypeError: round key must be a 2 x 2 matrix over GF(16)
            sage: maes.add_key("block", "key")
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the input matrices must each be
        `2 \\times 2`::

            sage: MSB = MatrixSpace(K, 1, 2)
            sage: B = MSB([ [K("x^3 + 1"), K("x^2 + x")] ])
            sage: maes.add_key(B, "key")
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)
            sage: MSB = MatrixSpace(K, 2, 2)
            sage: B = MSB([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ])
            sage: MSK = MatrixSpace(K, 1, 2)
            sage: key = MSK([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")]])
            sage: maes.add_key(B, key)
            Traceback (most recent call last):
            ...
            TypeError: round key must be a 2 x 2 matrix over GF(16)
        '''
    def block_length(self):
        """
        Return the block length of Phan's Mini-AES block cipher. A key in
        Phan's Mini-AES is a block of 16 bits. Each nibble of a key can be
        considered as an element of the finite field `\\GF{2^4}`.
        Therefore the key consists of four elements from `\\GF{2^4}`.

        OUTPUT:

        - The block (or key) length in number of bits.

        EXAMPLES::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.block_length()
            16
        """
    def decrypt(self, C, key):
        '''
        Use Phan\'s Mini-AES to decrypt the ciphertext ``C`` with the secret
        key ``key``. Both ``C`` and ``key`` must be `2 \\times 2` matrices over
        the finite field `\\GF{2^4}`. Let `\\gamma` denote the
        operation of nibble-sub, `\\pi` denote shift-row, `\\theta` denote
        mix-column, and `\\sigma_{K_i}` denote add-key with the round key
        `K_i`. Then decryption `D` using Phan\'s Mini-AES is the function
        composition

        .. MATH::

            D = \\sigma_{K_0} \\circ \\gamma^{-1} \\circ \\pi \\circ \\theta \\circ \\sigma_{K_1} \\circ \\gamma^{-1} \\circ \\pi \\circ \\sigma_{K_2}

        where `\\gamma^{-1}` is the nibble-sub operation that uses the S-box
        for decryption, and the order of execution is from right to left.

        INPUT:

        - ``C`` -- a ciphertext block; must be a `2 \\times 2` matrix over
          the finite field `\\GF{2^4}`

        - ``key`` -- a secret key for this Mini-AES block cipher; must be a
          `2 \\times 2` matrix over the finite field `\\GF{2^4}`

        OUTPUT: the plaintext corresponding to ``C``

        EXAMPLES:

        We encrypt a plaintext, decrypt the ciphertext, then compare the
        decrypted plaintext with the original plaintext. Here we work with
        elements of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: P = MS([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ]); P
            <BLANKLINE>
            [  x^3 + 1   x^2 + x]
            [x^3 + x^2     x + 1]
            sage: key = MS([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ]); key
            <BLANKLINE>
            [        x^3 + x^2 x^3 + x^2 + x + 1]
            [            x + 1                 0]
            sage: C = maes.encrypt(P, key); C
            [            x + 1           x^2 + 1]
            [x^3 + x^2 + x + 1               x^2]
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt; P
            <BLANKLINE>
            [  x^3 + 1   x^2 + x]
            [x^3 + x^2     x + 1]
            <BLANKLINE>
            [  x^3 + 1   x^2 + x]
            [x^3 + x^2     x + 1]
            sage: plaintxt == P
            True

        But we can also work with binary strings::

            sage: bin = BinaryStrings()
            sage: P = bin.encoding("de"); P
            0110010001100101
            sage: P = MS(maes.binary_to_GF(P)); P
            <BLANKLINE>
            [x^2 + x     x^2]
            [x^2 + x x^2 + 1]
            sage: key = bin.encoding("ke"); key
            0110101101100101
            sage: key = MS(maes.binary_to_GF(key)); key
            <BLANKLINE>
            [    x^2 + x x^3 + x + 1]
            [    x^2 + x     x^2 + 1]
            sage: C = maes.encrypt(P, key)
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt == P
            True

        Here we work with integers `n` such that `0 \\leq n \\leq 15`::

            sage: P = [3, 5, 7, 14]; P
            [3, 5, 7, 14]
            sage: key = [2, 6, 7, 8]; key
            [2, 6, 7, 8]
            sage: P = MS(maes.integer_to_GF(P)); P
            <BLANKLINE>
            [        x + 1       x^2 + 1]
            [  x^2 + x + 1 x^3 + x^2 + x]
            sage: key = MS(maes.integer_to_GF(key)); key
            <BLANKLINE>
            [          x     x^2 + x]
            [x^2 + x + 1         x^3]
            sage: C = maes.encrypt(P, key)
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt == P
            True

        TESTS:

        The input block must be a matrix::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: key = MS([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ])
            sage: maes.decrypt("C", key)
            Traceback (most recent call last):
            ...
            TypeError: ciphertext block must be a 2 x 2 matrix over GF(16)
            sage: C = MS([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ])
            sage: maes.decrypt(C, "key")
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the input matrices must be
        `2 \\times 2`::

            sage: MS = MatrixSpace(K, 1, 2)
            sage: C = MS([ [K("x^3 + 1"), K("x^2 + x")]])
            sage: maes.decrypt(C, "key")
            Traceback (most recent call last):
            ...
            TypeError: ciphertext block must be a 2 x 2 matrix over GF(16)
            sage: MSC = MatrixSpace(K, 2, 2)
            sage: C = MSC([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ])
            sage: MSK = MatrixSpace(K, 1, 2)
            sage: key = MSK([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")]])
            sage: maes.decrypt(C, key)
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 2 x 2 matrix over GF(16)
        '''
    def encrypt(self, P, key):
        '''
        Use Phan\'s Mini-AES to encrypt the plaintext ``P`` with the secret
        key ``key``. Both ``P`` and ``key`` must be `2 \\times 2` matrices
        over the finite field `\\GF{2^4}`. Let `\\gamma` denote the
        operation of nibble-sub, `\\pi` denote shift-row, `\\theta` denote
        mix-column, and `\\sigma_{K_i}` denote add-key with the round key
        `K_i`. Then encryption `E` using Phan\'s Mini-AES is the function
        composition

        .. MATH::

            E = \\sigma_{K_2} \\circ \\pi \\circ \\gamma \\circ \\sigma_{K_1} \\circ \\theta \\circ \\pi \\circ \\gamma \\circ \\sigma_{K_0}

        where the order of execution is from right to left. Note that
        `\\gamma` is the nibble-sub operation that uses the S-box for
        encryption.

        INPUT:

        - ``P`` -- a plaintext block; must be a `2 \\times 2` matrix over
          the finite field `\\GF{2^4}`

        - ``key`` -- a secret key for this Mini-AES block cipher; must be a
          `2 \\times 2` matrix over the finite field `\\GF{2^4}`

        OUTPUT: the ciphertext corresponding to ``P``

        EXAMPLES:

        Here we work with elements of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: P = MS([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ]); P
            <BLANKLINE>
            [  x^3 + 1   x^2 + x]
            [x^3 + x^2     x + 1]
            sage: key = MS([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ]); key
            <BLANKLINE>
            [        x^3 + x^2 x^3 + x^2 + x + 1]
            [            x + 1                 0]
            sage: maes.encrypt(P, key)
            [            x + 1           x^2 + 1]
            [x^3 + x^2 + x + 1               x^2]

        But we can also work with binary strings::

            sage: bin = BinaryStrings()
            sage: P = bin.encoding("de"); P
            0110010001100101
            sage: P = MS(maes.binary_to_GF(P)); P
            <BLANKLINE>
            [x^2 + x     x^2]
            [x^2 + x x^2 + 1]
            sage: key = bin.encoding("ke"); key
            0110101101100101
            sage: key = MS(maes.binary_to_GF(key)); key
            <BLANKLINE>
            [    x^2 + x x^3 + x + 1]
            [    x^2 + x     x^2 + 1]
            sage: C = maes.encrypt(P, key)
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt == P
            True

        Now we work with integers `n` such that `0 \\leq n \\leq 15`::

            sage: P = [1, 5, 8, 12]; P
            [1, 5, 8, 12]
            sage: key = [5, 9, 15, 0]; key
            [5, 9, 15, 0]
            sage: P = MS(maes.integer_to_GF(P)); P
            <BLANKLINE>
            [        1   x^2 + 1]
            [      x^3 x^3 + x^2]
            sage: key = MS(maes.integer_to_GF(key)); key
            <BLANKLINE>
            [          x^2 + 1           x^3 + 1]
            [x^3 + x^2 + x + 1                 0]
            sage: C = maes.encrypt(P, key)
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt == P
            True

        TESTS:

        The input block must be a matrix::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: key = MS([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ])
            sage: maes.encrypt("P", key)
            Traceback (most recent call last):
            ...
            TypeError: plaintext block must be a 2 x 2 matrix over GF(16)
            sage: P = MS([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ])
            sage: maes.encrypt(P, "key")
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the input matrices must be
        `2 \\times 2`::

            sage: MS = MatrixSpace(K, 1, 2)
            sage: P = MS([ [K("x^3 + 1"), K("x^2 + x")]])
            sage: maes.encrypt(P, "key")
            Traceback (most recent call last):
            ...
            TypeError: plaintext block must be a 2 x 2 matrix over GF(16)
            sage: MSP = MatrixSpace(K, 2, 2)
            sage: P = MSP([ [K("x^3 + 1"), K("x^2 + x")], [K("x^3 + x^2"), K("x + 1")] ])
            sage: MSK = MatrixSpace(K, 1, 2)
            sage: key = MSK([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")]])
            sage: maes.encrypt(P, key)
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 2 x 2 matrix over GF(16)
        '''
    def mix_column(self, block):
        '''
        Return the matrix multiplication of ``block`` with a constant matrix.
        The constant matrix is

        .. MATH::

            \\begin{bmatrix}
              x + 1 & x \\\\\n              x     & x + 1
            \\end{bmatrix}

        If the input block is

        .. MATH::

            \\begin{bmatrix}
              c_0 & c_2 \\\\\n              c_1 & c_3
            \\end{bmatrix}

        then the output block is

        .. MATH::

            \\begin{bmatrix}
              d_0 & d_2 \\\\\n              d_1 & d_3
            \\end{bmatrix}
            =
            \\begin{bmatrix}
              x + 1 & x \\\\\n              x     & x + 1
            \\end{bmatrix}
            \\begin{bmatrix}
              c_0 & c_2 \\\\\n              c_1 & c_3
            \\end{bmatrix}

        INPUT:

        - ``block`` -- a `2 \\times 2` matrix with entries over
          `\\GF{2^4}`

        OUTPUT:

        - A `2 \\times 2` matrix resulting from multiplying the above constant
          matrix with the input matrix ``block``.

        EXAMPLES:

        Here we work with elements of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: mat = MS([ [K("x^2 + x + 1"), K("x^3 + x^2 + 1")], [K("x^3"), K("x")] ])
            sage: maes.mix_column(mat)
            <BLANKLINE>
            [          x^3 + x                 0]
            [          x^2 + 1 x^3 + x^2 + x + 1]

        Multiplying by the identity matrix should leave the constant matrix
        unchanged::

            sage: eye = MS([ [K("1"), K("0")], [K("0"), K("1")] ])
            sage: maes.mix_column(eye)
            <BLANKLINE>
            [x + 1     x]
            [    x x + 1]

        We can also work with binary strings::

            sage: bin = BinaryStrings()
            sage: B = bin.encoding("rT"); B
            0111001001010100
            sage: B = MS(maes.binary_to_GF(B)); B
            <BLANKLINE>
            [x^2 + x + 1           x]
            [    x^2 + 1         x^2]
            sage: maes.mix_column(B)
            <BLANKLINE>
            [        x + 1 x^3 + x^2 + x]
            [            1           x^3]

        We can also work with integers `n` such that `0 \\leq n \\leq 15`::

            sage: P = [10, 5, 2, 7]; P
            [10, 5, 2, 7]
            sage: P = MS(maes.integer_to_GF(P)); P
            <BLANKLINE>
            [    x^3 + x     x^2 + 1]
            [          x x^2 + x + 1]
            sage: maes.mix_column(P)
            <BLANKLINE>
            [x^3 + 1       1]
            [      1   x + 1]

        TESTS:

        The input block must be a matrix::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.mix_column("mat")
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the input matrix must be `2 \\times 2`::

            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 1, 2)
            sage: mat = MS([[K("x^3 + x^2 + x + 1"), K("0")]])
            sage: maes.mix_column(mat)
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)
        '''
    def nibble_sub(self, block, algorithm: str = 'encrypt'):
        '''
        Substitute a nibble (or a block of 4 bits) using the following S-box:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              Input & Output & Input & Output \\\\\\hline
              0000  & 1110   & 1000  & 0011   \\\\\n              0001  & 0100   & 1001  & 1010   \\\\\n              0010  & 1101   & 1010  & 0110   \\\\\n              0011  & 0001   & 1011  & 1100   \\\\\n              0100  & 0010   & 1100  & 0101   \\\\\n              0101  & 1111   & 1101  & 1001   \\\\\n              0110  & 1011   & 1110  & 0000   \\\\\n              0111  & 1000   & 1111  & 0111   \\\\\\hline
            \\end{tabular}

        The values in the above S-box are taken from the first row of the first
        S-box of the Data Encryption Standard (DES). Each nibble can be
        thought of as an element of the finite field `\\GF{2^4}` of 16
        elements. Thus in terms of `\\GF{2^4}`, the S-box can also be
        specified as:

        .. MATH::

            \\begin{tabular}{ll} \\hline
              Input                & Output               \\\\\\hline
              $0$                  &  $x^3 + x^2 + x$     \\\\\n              $1$                  &  $x^2$               \\\\\n              $x$                  &  $x^3 + x^2 + 1$     \\\\\n              $x + 1$              &  $1$                 \\\\\n              $x^2$                &  $x$                 \\\\\n              $x^2 + 1$            &  $x^3 + x^2 + x + 1$ \\\\\n              $x^2 + x$            &  $x^3 + x + 1$       \\\\\n              $x^2 + x + 1$        &  $x^3$               \\\\\n              $x^3$                &  $x + 1$             \\\\\n              $x^3 + 1$            &  $x^3 + x$           \\\\\n              $x^3 + x$            &  $x^2 + x$           \\\\\n              $x^3 + x + 1$        &  $x^3 + x^2$         \\\\\n              $x^3 + x^2$          &  $x^2 + 1$           \\\\\n              $x^3 + x^2 + 1$      &  $x^3 + 1$           \\\\\n              $x^3 + x^2 + x$      &  $0$                 \\\\\n              $x^3 + x^2 + x + 1$  &  $x^2 + x + 1$       \\\\\\hline
            \\end{tabular}

        Note that the above S-box is used for encryption. The S-box for
        decryption is obtained from the above S-box by reversing the role of
        the Input and Output columns. Thus the previous Input column for
        encryption now becomes the Output column for decryption, and the
        previous Output column for encryption is now the Input column for
        decryption. The S-box used for decryption can be specified as:

        .. MATH::

            \\begin{tabular}{ll} \\hline
              Input               & Output              \\\\\\hline
              $0$                 & $x^3 + x^2 + x$     \\\\\n              $1$                 & $x + 1$             \\\\\n              $x$                 & $x^2$               \\\\\n              $x + 1$             & $x^3$               \\\\\n              $x^2$               & $1$                 \\\\\n              $x^2 + 1$           & $x^3 + x^2$         \\\\\n              $x^2 + x$           & $x^3 + x$           \\\\\n              $x^2 + x + 1$       & $x^3 + x^2 + x + 1$ \\\\\n              $x^3$               & $x^2 + x + 1$       \\\\\n              $x^3 + 1$           & $x^3 + x^2 + 1$     \\\\\n              $x^3 + x$           & $x^3 + 1$           \\\\\n              $x^3 + x + 1$       & $x^2 + x$           \\\\\n              $x^3 + x^2$         & $x^3 + x + 1$       \\\\\n              $x^3 + x^2 + 1$     & $x$                 \\\\\n              $x^3 + x^2 + x$     & $0$                 \\\\\n              $x^3 + x^2 + x + 1$ & $x^2 + 1$           \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``block`` -- a `2 \\times 2` matrix with entries over
          `\\GF{2^4}`

        - ``algorithm`` -- (default: ``\'encrypt\'``) a string; a flag to signify
          whether this nibble-sub operation is used for encryption or
          decryption. The encryption flag is ``\'encrypt\'`` and the decryption
          flag is ``\'decrypt\'``.

        OUTPUT: a `2 \\times 2` matrix resulting from applying an S-box on
        entries of the `2 \\times 2` matrix ``block``.

        EXAMPLES:

        Here we work with elements of the finite field `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: mat = MS([[K("x^3 + x^2 + x + 1"), K("0")], [K("x^2 + x + 1"), K("x^3 + x")]])
            sage: maes.nibble_sub(mat, algorithm=\'encrypt\')
            <BLANKLINE>
            [  x^2 + x + 1 x^3 + x^2 + x]
            [          x^3       x^2 + x]

        But we can also work with binary strings::

            sage: bin = BinaryStrings()
            sage: B = bin.encoding("bi"); B
            0110001001101001
            sage: B = MS(maes.binary_to_GF(B)); B
            <BLANKLINE>
            [x^2 + x       x]
            [x^2 + x x^3 + 1]
            sage: maes.nibble_sub(B, algorithm=\'encrypt\')
            <BLANKLINE>
            [  x^3 + x + 1 x^3 + x^2 + 1]
            [  x^3 + x + 1       x^3 + x]
            sage: maes.nibble_sub(B, algorithm=\'decrypt\')
            <BLANKLINE>
            [      x^3 + x           x^2]
            [      x^3 + x x^3 + x^2 + 1]

        Here we work with integers `n` such that `0 \\leq n \\leq 15`::

            sage: P = [2, 6, 8, 14]; P
            [2, 6, 8, 14]
            sage: P = MS(maes.integer_to_GF(P)); P
            <BLANKLINE>
            [            x       x^2 + x]
            [          x^3 x^3 + x^2 + x]
            sage: maes.nibble_sub(P, algorithm=\'encrypt\')
            <BLANKLINE>
            [x^3 + x^2 + 1   x^3 + x + 1]
            [        x + 1             0]
            sage: maes.nibble_sub(P, algorithm=\'decrypt\')
            <BLANKLINE>
            [        x^2     x^3 + x]
            [x^2 + x + 1           0]

        TESTS:

        The input block must be a matrix::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.nibble_sub("mat")
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the input matrix must be `2 \\times 2`::

            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 1, 2)
            sage: mat = MS([[K("x^3 + x^2 + x + 1"), K("0")]])
            sage: maes.nibble_sub(mat)
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)

        The value for the option ``algorithm`` must be either the string
        ``\'encrypt\'`` or ``\'decrypt\'``::

            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: mat = MS([[K("x^3 + x^2 + x + 1"), K("0")], [K("x^2 + x + 1"), K("x^3 + x")]])
            sage: maes.nibble_sub(mat, algorithm=\'abc\')
            Traceback (most recent call last):
            ...
            ValueError: the algorithm for nibble-sub must be either \'encrypt\' or \'decrypt\'
            sage: maes.nibble_sub(mat, algorithm=\'e\')
            Traceback (most recent call last):
            ...
            ValueError: the algorithm for nibble-sub must be either \'encrypt\' or \'decrypt\'
            sage: maes.nibble_sub(mat, algorithm=\'d\')
            Traceback (most recent call last):
            ...
            ValueError: the algorithm for nibble-sub must be either \'encrypt\' or \'decrypt\'
        '''
    def random_key(self):
        '''
        A random key within the key space of this Mini-AES block cipher. Like
        the AES, Phan\'s Mini-AES is a symmetric-key block cipher. A Mini-AES
        key is a block of 16 bits, or a `2 \\times 2` matrix with entries over
        the finite field `\\GF{2^4}`. Thus the number of possible keys is
        `2^{16} = 16^4`.

        OUTPUT:

        - A `2 \\times 2` matrix over the finite field `\\GF{2^4}`, used
          as a secret key for this Mini-AES block cipher.

        EXAMPLES:

        Each nibble of a key is an element of the finite field
        `\\GF{2^4}`::

            sage: K = FiniteField(16, "x")
            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: key = maes.random_key()
            sage: [key[i][j] in K for i in range(key.nrows()) for j in range(key.ncols())]
            [True, True, True, True]

        Generate a random key, then perform encryption and decryption using
        that key::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: key = maes.random_key()
            sage: P = MS.random_element()
            sage: C = maes.encrypt(P, key)
            sage: plaintxt = maes.decrypt(C, key)
            sage: plaintxt == P
            True
        '''
    def round_key(self, key, n):
        '''
        Return the round key for round ``n``. Phan\'s Mini-AES is defined to
        have two rounds. The round key `K_0` is generated and used prior to
        the first round, with round keys `K_1` and `K_2` being used in rounds
        1 and 2 respectively. In total, there are three round keys, each
        generated from the secret key ``key``.

        INPUT:

        - ``key`` -- the secret key

        - ``n`` -- nonnegative integer; the round number

        OUTPUT: the `n`-th round key

        EXAMPLES:

        Obtaining the round keys from the secret key::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: key = MS([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ])
            sage: maes.round_key(key, 0)
            <BLANKLINE>
            [        x^3 + x^2 x^3 + x^2 + x + 1]
            [            x + 1                 0]
            sage: key
            <BLANKLINE>
            [        x^3 + x^2 x^3 + x^2 + x + 1]
            [            x + 1                 0]
            sage: maes.round_key(key, 1)
            [x^3 + x x^2 + x]
            [x^3 + 1 x^2 + x]
            sage: maes.round_key(key, 2)
            <BLANKLINE>
            [  x^2 + 1   x^3 + x]
            [x^3 + x^2 x^3 + x^2]

        TESTS:

        Only two rounds are defined for this AES variant::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: key = MS([ [K("x^3 + x^2"), K("x^3 + x^2 + x + 1")], [K("x + 1"), K("0")] ])
            sage: maes.round_key(key, -1)
            Traceback (most recent call last):
            ...
            ValueError: Mini-AES only defines two rounds
            sage: maes.round_key(key, 3)
            Traceback (most recent call last):
            ...
            ValueError: Mini-AES only defines two rounds

        The input key must be a matrix::

            sage: maes.round_key("key", 0)
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the key matrix must be `2 \\times 2`::

            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 1, 2)
            sage: key = MS([[K("x^3 + x^2 + x + 1"), K("0")]])
            sage: maes.round_key(key, 2)
            Traceback (most recent call last):
            ...
            TypeError: secret key must be a 2 x 2 matrix over GF(16)
        '''
    def sbox(self):
        """
        Return the S-box of Mini-AES.

        EXAMPLES::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.sbox()
            (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7)
        """
    def shift_row(self, block):
        '''
        Rotate each row of ``block`` to the left by different nibble
        amounts. The first or zero-th row is left unchanged, while the
        second or row one is rotated left by one nibble. This has the effect
        of only interchanging the nibbles in the second row. Let
        `b_0, b_1, b_2, b_3` be four nibbles arranged as the following
        `2 \\times 2` matrix

        .. MATH::

            \\begin{bmatrix}
              b_0 & b_2 \\\\\n              b_1 & b_3
            \\end{bmatrix}

        Then the operation of shift-row is the mapping

        .. MATH::

            \\begin{bmatrix}
              b_0 & b_2 \\\\\n              b_1 & b_3
            \\end{bmatrix}
            \\longmapsto
            \\begin{bmatrix}
              b_0 & b_2 \\\\\n              b_3 & b_1
            \\end{bmatrix}

        INPUT:

        - ``block`` -- a `2 \\times 2` matrix with entries over
          `\\GF{2^4}`

        OUTPUT: a `2 \\times 2` matrix resulting from applying shift-row on ``block``

        EXAMPLES:

        Here we work with elements of the finite field `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: mat = MS([[K("x^3 + x^2 + x + 1"), K("0")], [K("x^2 + x + 1"), K("x^3 + x")]])
            sage: maes.shift_row(mat)
            <BLANKLINE>
            [x^3 + x^2 + x + 1                 0]
            [          x^3 + x       x^2 + x + 1]
            sage: mat
            <BLANKLINE>
            [x^3 + x^2 + x + 1                 0]
            [      x^2 + x + 1           x^3 + x]

        But we can also work with binary strings::

            sage: bin = BinaryStrings()
            sage: B = bin.encoding("Qt"); B
            0101000101110100
            sage: B = MS(maes.binary_to_GF(B)); B
            <BLANKLINE>
            [    x^2 + 1           1]
            [x^2 + x + 1         x^2]
            sage: maes.shift_row(B)
            <BLANKLINE>
            [    x^2 + 1           1]
            [        x^2 x^2 + x + 1]

        Here we work with integers `n` such that `0 \\leq n \\leq 15`::

            sage: P = [3, 6, 9, 12]; P
            [3, 6, 9, 12]
            sage: P = MS(maes.integer_to_GF(P)); P
            <BLANKLINE>
            [    x + 1   x^2 + x]
            [  x^3 + 1 x^3 + x^2]
            sage: maes.shift_row(P)
            <BLANKLINE>
            [    x + 1   x^2 + x]
            [x^3 + x^2   x^3 + 1]

        TESTS:

        The input block must be a matrix::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.shift_row("block")
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)

        In addition, the dimensions of the input matrix must be `2 \\times 2`::

            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 1, 2)
            sage: mat = MS([[K("x^3 + x^2 + x + 1"), K("0")]])
            sage: maes.shift_row(mat)
            Traceback (most recent call last):
            ...
            TypeError: input block must be a 2 x 2 matrix over GF(16)
        '''
    def GF_to_binary(self, G):
        '''
        Return the binary representation of ``G``.
        If ``G`` is an element of the finite field `\\GF{2^4}`, then
        obtain the binary representation of ``G``. If ``G`` is a list of
        elements belonging to `\\GF{2^4}`, obtain the 4-bit
        representation of each element of the list, then concatenate the
        resulting 4-bit strings into a binary string. If ``G`` is a matrix
        with entries over `\\GF{2^4}`, convert each matrix entry to its
        4-bit representation, then concatenate the 4-bit strings. The
        concatenation is performed starting from the top-left corner of the
        matrix, working across left to right, top to bottom. Each element of
        `\\GF{2^4}` can be associated with a unique 4-bit string
        according to the following table:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              4-bit string & $\\GF{2^4}$ & 4-bit string & $\\GF{2^4}$ \\\\\\hline
              0000 & $0$           & 1000 & $x^3$              \\\\\n              0001 & $1$           & 1001 & $x^3 + 1$          \\\\\n              0010 & $x$           & 1010 & $x^3 + x$          \\\\\n              0011 & $x + 1$       & 1011 & $x^3 + x + 1$      \\\\\n              0100 & $x^2$         & 1100 & $x^3 + x^2$        \\\\\n              0101 & $x^2 + 1$     & 1101 & $x^3 + x^2 + 1$    \\\\\n              0110 & $x^2 + x$     & 1110 & $x^3 + x^2 + x$    \\\\\n              0111 & $x^2 + x + 1$ & 1111 & $x^3 + x^2 + x+ 1$ \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``G`` -- an element of `\\GF{2^4}`, a list of elements of
          `\\GF{2^4}`, or a matrix over `\\GF{2^4}`

        OUTPUT: a binary string representation of ``G``

        EXAMPLES:

        Obtain the binary representation of all elements of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: S = Set(K); len(S)  # GF(2^4) has this many elements
            16
            sage: [maes.GF_to_binary(S[i]) for i in range(len(S))]
            <BLANKLINE>
            [0000,
            0001,
            0010,
            0011,
            0100,
            0101,
            0110,
            0111,
            1000,
            1001,
            1010,
            1011,
            1100,
            1101,
            1110,
            1111]

        The binary representation of a list of elements belonging to
        `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: G = [K("x^2 + x + 1"), K("x^3 + x^2"), K("x"), K("x^3 + x + 1"), K("x^3 + x^2 + x + 1"), K("x^2 + x"), K("1"), K("x^2 + x + 1")]
            sage: maes.GF_to_binary(G)
            01111100001010111111011000010111

        The binary representation of a matrix over `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: G = MS([K("x^3 + x^2"), K("x + 1"), K("x^2 + x + 1"), K("x^3 + x^2 + x")]); G
            <BLANKLINE>
            [    x^3 + x^2         x + 1]
            [  x^2 + x + 1 x^3 + x^2 + x]
            sage: maes.GF_to_binary(G)
            1100001101111110
            sage: MS = MatrixSpace(K, 2, 4)
            sage: G = MS([K("x^2 + x + 1"), K("x^3 + x^2"), K("x"), K("x^3 + x + 1"), K("x^3 + x^2 + x + 1"), K("x^2 + x"), K("1"), K("x^2 + x + 1")]); G
            <BLANKLINE>
            [      x^2 + x + 1         x^3 + x^2                 x       x^3 + x + 1]
            [x^3 + x^2 + x + 1           x^2 + x                 1       x^2 + x + 1]
            sage: maes.GF_to_binary(G)
            01111100001010111111011000010111

        TESTS:

        Input must be an element of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(8, "x")
            sage: G = K.random_element()
            sage: maes.GF_to_binary(G)
            Traceback (most recent call last):
            ...
            TypeError: input G must be an element of GF(16), a list of elements of GF(16), or a matrix over GF(16)

        A list of elements belonging to `\\GF{2^4}`::

            sage: maes.GF_to_binary([])
            Traceback (most recent call last):
            ...
            ValueError: input G must be an element of GF(16), a list of elements of GF(16), or a matrix over GF(16)
            sage: G = [K.random_element() for i in range(5)]
            sage: maes.GF_to_binary(G)
            Traceback (most recent call last):
            ...
            KeyError:...

        A matrix over `\\GF{2^4}`::

            sage: MS = MatrixSpace(FiniteField(7, "x"), 4, 5)
            sage: maes.GF_to_binary(MS.random_element())
            Traceback (most recent call last):
            ...
            TypeError: input G must be an element of GF(16), a list of elements of GF(16), or a matrix over GF(16)
        '''
    def GF_to_integer(self, G):
        '''
        Return the integer representation of the finite field element ``G``.
        If ``G`` is an element of the finite field `\\GF{2^4}`, then
        obtain the integer representation of ``G``. If ``G`` is a list of
        elements belonging to `\\GF{2^4}`, obtain the integer
        representation of each element of the list, and return the result
        as a list of integers. If ``G`` is a matrix with entries over
        `\\GF{2^4}`, convert each matrix entry to its integer representation,
        and return the result as a list of integers. The resulting list is
        obtained by starting from the top-left corner of the matrix, working
        across left to right, top to bottom. Each element of `\\GF{2^4}` can
        be associated with a unique integer according to the following table:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              integer & $\\GF{2^4}$ & integer & $\\GF{2^4}$ \\\\\\hline
              0 & $0$           & 8  & $x^3$              \\\\\n              1 & $1$           & 9  & $x^3 + 1$          \\\\\n              2 & $x$           & 10 & $x^3 + x$          \\\\\n              3 & $x + 1$       & 11 & $x^3 + x + 1$      \\\\\n              4 & $x^2$         & 12 & $x^3 + x^2$        \\\\\n              5 & $x^2 + 1$     & 13 & $x^3 + x^2 + 1$    \\\\\n              6 & $x^2 + x$     & 14 & $x^3 + x^2 + x$    \\\\\n              7 & $x^2 + x + 1$ & 15 & $x^3 + x^2 + x+ 1$ \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``G`` -- an element of `\\GF{2^4}`, a list of elements belonging to
          `\\GF{2^4}`, or a matrix over `\\GF{2^4}`

        OUTPUT: the integer representation of ``G``

        EXAMPLES:

        Obtain the integer representation of all elements of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: S = Set(K); len(S)  # GF(2^4) has this many elements
            16
            sage: [maes.GF_to_integer(S[i]) for i in range(len(S))]
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        The integer representation of a list of elements belonging to
        `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: G = [K("x^2 + x + 1"), K("x^3 + x^2"), K("x"), K("x^3 + x + 1"), K("x^3 + x^2 + x + 1"), K("x^2 + x"), K("1"), K("x^2 + x + 1")]
            sage: maes.GF_to_integer(G)
            [7, 12, 2, 11, 15, 6, 1, 7]

        The integer representation of a matrix over `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(16, "x")
            sage: MS = MatrixSpace(K, 2, 2)
            sage: G = MS([K("x^3 + x^2"), K("x + 1"), K("x^2 + x + 1"), K("x^3 + x^2 + x")]); G
            <BLANKLINE>
            [    x^3 + x^2         x + 1]
            [  x^2 + x + 1 x^3 + x^2 + x]
            sage: maes.GF_to_integer(G)
            [12, 3, 7, 14]
            sage: MS = MatrixSpace(K, 2, 4)
            sage: G = MS([K("x^2 + x + 1"), K("x^3 + x^2"), K("x"), K("x^3 + x + 1"), K("x^3 + x^2 + x + 1"), K("x^2 + x"), K("1"), K("x^2 + x + 1")]); G
            <BLANKLINE>
            [      x^2 + x + 1         x^3 + x^2                 x       x^3 + x + 1]
            [x^3 + x^2 + x + 1           x^2 + x                 1       x^2 + x + 1]
            sage: maes.GF_to_integer(G)
            [7, 12, 2, 11, 15, 6, 1, 7]

        TESTS:

        Input must be an element of `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: K = FiniteField(7, "x")
            sage: G = K.random_element()
            sage: maes.GF_to_integer(G)
            Traceback (most recent call last):
            ...
            TypeError: input G must be an element of GF(16), a list of elements of GF(16), or a matrix over GF(16)

        A list of elements belonging to `\\GF{2^4}`::

            sage: maes.GF_to_integer([])
            Traceback (most recent call last):
            ...
            ValueError: input G must be an element of GF(16), a list of elements of GF(16), or a matrix over GF(16)
            sage: G = [K.random_element() for i in range(5)]
            sage: maes.GF_to_integer(G)
            Traceback (most recent call last):
            ...
            KeyError:...

        A matrix over `\\GF{2^4}`::

            sage: MS = MatrixSpace(FiniteField(7, "x"), 4, 5)
            sage: maes.GF_to_integer(MS.random_element())
            Traceback (most recent call last):
            ...
            TypeError: input G must be an element of GF(16), a list of elements of GF(16), or a matrix over GF(16)
        '''
    def binary_to_GF(self, B):
        '''
        Return a list of elements of `\\GF{2^4}` that represents the
        binary string ``B``. The number of bits in ``B`` must be greater
        than zero and a multiple of 4. Each nibble (or 4-bit string) is
        uniquely associated with an element of `\\GF{2^4}` as
        specified by the following table:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              4-bit string & $\\GF{2^4}$ & 4-bit string & $\\GF{2^4}$ \\\\\\hline
              0000 & $0$           & 1000 & $x^3$              \\\\\n              0001 & $1$           & 1001 & $x^3 + 1$          \\\\\n              0010 & $x$           & 1010 & $x^3 + x$          \\\\\n              0011 & $x + 1$       & 1011 & $x^3 + x + 1$      \\\\\n              0100 & $x^2$         & 1100 & $x^3 + x^2$        \\\\\n              0101 & $x^2 + 1$     & 1101 & $x^3 + x^2 + 1$    \\\\\n              0110 & $x^2 + x$     & 1110 & $x^3 + x^2 + x$    \\\\\n              0111 & $x^2 + x + 1$ & 1111 & $x^3 + x^2 + x+ 1$ \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``B`` -- a binary string, where the number of bits is positive and
          a multiple of 4

        OUTPUT:

        - A list of elements of the finite field `\\GF{2^4}` that
          represent the binary string ``B``.

        EXAMPLES:

        Obtain all the elements of the finite field `\\GF{2^4}`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: bin = BinaryStrings()
            sage: B = bin("0000000100100011010001010110011110001001101010111100110111101111")
            sage: maes.binary_to_GF(B)
            <BLANKLINE>
            [0,
            1,
            x,
            x + 1,
            x^2,
            x^2 + 1,
            x^2 + x,
            x^2 + x + 1,
            x^3,
            x^3 + 1,
            x^3 + x,
            x^3 + x + 1,
            x^3 + x^2,
            x^3 + x^2 + 1,
            x^3 + x^2 + x,
            x^3 + x^2 + x + 1]

        TESTS:

        The input ``B`` must be a non-empty binary string, where the number
        of bits is a multiple of 4::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.binary_to_GF("")
            Traceback (most recent call last):
            ...
            ValueError: the number of bits in the binary string B must be positive and a multiple of 4
            sage: maes.binary_to_GF("101")
            Traceback (most recent call last):
            ...
            ValueError: the number of bits in the binary string B must be positive and a multiple of 4
        '''
    def binary_to_integer(self, B):
        '''
        Return a list of integers representing the binary string ``B``. The
        number of bits in ``B`` must be greater than zero and a multiple of
        4. Each nibble (or 4-bit string) is uniquely associated with an
        integer as specified by the following table:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              4-bit string & integer & 4-bit string & integer \\\\\\hline
              0000 & 0 & 1000 & 8  \\\\\n              0001 & 1 & 1001 & 9  \\\\\n              0010 & 2 & 1010 & 10 \\\\\n              0011 & 3 & 1011 & 11 \\\\\n              0100 & 4 & 1100 & 12 \\\\\n              0101 & 5 & 1101 & 13 \\\\\n              0110 & 6 & 1110 & 14 \\\\\n              0111 & 7 & 1111 & 15 \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``B`` -- a binary string, where the number of bits is positive and
          a multiple of 4

        OUTPUT: list of integers that represent the binary string ``B``

        EXAMPLES:

        Obtain the integer representation of every 4-bit string::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: bin = BinaryStrings()
            sage: B = bin("0000000100100011010001010110011110001001101010111100110111101111")
            sage: maes.binary_to_integer(B)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        TESTS:

        The input ``B`` must be a non-empty binary string, where the number
        of bits is a multiple of 4::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.binary_to_integer("")
            Traceback (most recent call last):
            ...
            ValueError: the number of bits in the binary string B must be positive and a multiple of 4
            sage: maes.binary_to_integer("101")
            Traceback (most recent call last):
            ...
            ValueError: the number of bits in the binary string B must be positive and a multiple of 4
        '''
    def integer_to_binary(self, N):
        '''
        Return the binary representation of ``N``. If `N` is an integer such
        that `0 \\leq N \\leq 15`, return the binary representation of ``N``.
        If ``N`` is a list of integers each of which is `\\geq 0` and
        `\\leq 15`, then obtain the binary representation of each integer,
        and concatenate the individual binary representations into a single
        binary string. Each integer between 0 and 15, inclusive, can be
        associated with a unique 4-bit string according to the following
        table:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              4-bit string & integer & 4-bit string & integer \\\\\\hline
              0000 & 0 & 1000 & 8  \\\\\n              0001 & 1 & 1001 & 9  \\\\\n              0010 & 2 & 1010 & 10 \\\\\n              0011 & 3 & 1011 & 11 \\\\\n              0100 & 4 & 1100 & 12 \\\\\n              0101 & 5 & 1101 & 13 \\\\\n              0110 & 6 & 1110 & 14 \\\\\n              0111 & 7 & 1111 & 15 \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``N`` -- nonnegative integer less than or equal to 15, or a list
          of such integers

        OUTPUT: a binary string representing ``N``

        EXAMPLES:

        The binary representations of all integers between 0 and
        15, inclusive::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: lst = [n for n in range(16)]; lst
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: maes.integer_to_binary(lst)
            0000000100100011010001010110011110001001101010111100110111101111

        The binary representation of an integer between 0 and 15,
        inclusive::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.integer_to_binary(3)
            0011
            sage: maes.integer_to_binary(5)
            0101
            sage: maes.integer_to_binary(7)
            0111

        TESTS:

        The input ``N`` can be an integer, but must be bounded such that
        `0 \\leq N \\leq 15`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.integer_to_binary(-1)
            Traceback (most recent call last):
            ...
            KeyError:...
            sage: maes.integer_to_binary("1")
            Traceback (most recent call last):
            ...
            TypeError: N must be an integer 0 <= N <= 15 or a list of such integers
            sage: maes.integer_to_binary("")
            Traceback (most recent call last):
            ...
            TypeError: N must be an integer 0 <= N <= 15 or a list of such integers

        The input ``N`` can be a list of integers, but each integer `n` of
        the list must be `0 \\leq n \\leq 15`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.integer_to_binary([])
            Traceback (most recent call last):
            ...
            ValueError: N must be an integer 0 <= N <= 15 or a list of such integers
            sage: maes.integer_to_binary([""])
            Traceback (most recent call last):
            ...
            KeyError:...
            sage: maes.integer_to_binary([0, 1, 2, 16])
            Traceback (most recent call last):
            ...
            KeyError:...
        '''
    def integer_to_GF(self, N):
        '''
        Return the finite field representation of ``N``. If `N` is an
        integer such that `0 \\leq N \\leq 15`, return the element of
        `\\GF{2^4}` that represents ``N``. If ``N`` is a list of integers
        each of which is `\\geq 0` and `\\leq 15`, then obtain the element
        of `\\GF{2^4}` that represents each such integer, and return a list
        of such finite field representations. Each integer between 0 and 15,
        inclusive, can be associated with a unique element of `\\GF{2^4}`
        according to the following table:

        .. MATH::

            \\begin{tabular}{ll|ll} \\hline
              integer & $\\GF{2^4}$ & integer & $\\GF{2^4}$ \\\\\\hline
              0 & $0$           & 8  & $x^3$              \\\\\n              1 & $1$           & 9  & $x^3 + 1$          \\\\\n              2 & $x$           & 10 & $x^3 + x$          \\\\\n              3 & $x + 1$       & 11 & $x^3 + x + 1$      \\\\\n              4 & $x^2$         & 12 & $x^3 + x^2$        \\\\\n              5 & $x^2 + 1$     & 13 & $x^3 + x^2 + 1$    \\\\\n              6 & $x^2 + x$     & 14 & $x^3 + x^2 + x$    \\\\\n              7 & $x^2 + x + 1$ & 15 & $x^3 + x^2 + x+ 1$ \\\\\\hline
            \\end{tabular}

        INPUT:

        - ``N`` -- nonnegative integer less than or equal to 15, or a list
          of such integers

        OUTPUT: elements of the finite field `\\GF{2^4}`

        EXAMPLES:

        Obtain the element of `\\GF{2^4}` representing an integer `n`, where
        `0 \\leq n \\leq 15`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.integer_to_GF(0)
            0
            sage: maes.integer_to_GF(2)
            x
            sage: maes.integer_to_GF(7)
            x^2 + x + 1

        Obtain the finite field elements corresponding to all nonnegative
        integers less than or equal to 15::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: lst = [n for n in range(16)]; lst
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            sage: maes.integer_to_GF(lst)
            <BLANKLINE>
            [0,
            1,
            x,
            x + 1,
            x^2,
            x^2 + 1,
            x^2 + x,
            x^2 + x + 1,
            x^3,
            x^3 + 1,
            x^3 + x,
            x^3 + x + 1,
            x^3 + x^2,
            x^3 + x^2 + 1,
            x^3 + x^2 + x,
            x^3 + x^2 + x + 1]

        TESTS:

        The input ``N`` can be an integer, but it must be such that
        `0 \\leq N \\leq 15`::

            sage: from sage.crypto.block_cipher.miniaes import MiniAES
            sage: maes = MiniAES()
            sage: maes.integer_to_GF(-1)
            Traceback (most recent call last):
            ...
            KeyError:...
            sage: maes.integer_to_GF(16)
            Traceback (most recent call last):
            ...
            KeyError:...
            sage: maes.integer_to_GF("2")
            Traceback (most recent call last):
            ...
            TypeError: N must be an integer 0 <= N <= 15 or a list of such integers

        The input ``N`` can be a list of integers, but each integer `n` in
        the list must be bounded such that `0 \\leq n \\leq 15`::

            sage: maes.integer_to_GF([])
            Traceback (most recent call last):
            ...
            ValueError: N must be an integer 0 <= N <= 15 or a list of such integers
            sage: maes.integer_to_GF([""])
            Traceback (most recent call last):
            ...
            KeyError:...
            sage: maes.integer_to_GF([0, 2, 3, "4"])
            Traceback (most recent call last):
            ...
            KeyError:...
            sage: maes.integer_to_GF([0, 2, 3, 16])
            Traceback (most recent call last):
            ...
            KeyError:...
        '''
