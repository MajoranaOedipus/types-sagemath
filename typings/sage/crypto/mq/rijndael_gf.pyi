from _typeshed import Incomplete
from sage.matrix.constructor import column_matrix as column_matrix, matrix as matrix
from sage.misc.sageinspect import sage_getargspec as sage_getargspec
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import Element as Element, Matrix as Matrix
from sage.structure.sage_object import SageObject as SageObject

class RijndaelGF(SageObject):
    state_vrs: Incomplete
    subkey_vrs_list: Incomplete
    subkey_vrs: Incomplete
    key_vrs: Incomplete
    def __init__(self, Nb, Nk, state_chr: str = 'a', key_chr: str = 'k') -> None:
        """
        An algebraically generalized version of the AES cipher.

        INPUT:

        - ``Nb`` -- the block length of this instantiation. Must be between 4
          and 8

        - ``Nk`` -- the key length of this instantiation. Must be between 4 and 8

        - ``state_chr`` -- the variable name for polynomials representing
          elements from state matrices

        - ``key_chr`` -- the variable name for polynomials representing
          elements of the key schedule

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(6, 8)
            sage: rgf
            Rijndael-GF block cipher with block length 6, key length 8, and 14 rounds.

        By changing ``state_chr`` we can alter the names of variables in
        polynomials representing elements from state matrices. ::

            sage: rgf = RijndaelGF(4, 6, state_chr='myChr')
            sage: rgf.mix_columns_poly_constr()(3, 2)
            (x + 1)*myChr02 + myChr12 + myChr22 + x*myChr32

        We can also alter the name of variables in polynomials representing
        elements from round keys by changing ``key_chr``. ::

            sage: rgf = RijndaelGF(4, 6, key_chr='myKeyChr')
            sage: rgf.expand_key_poly(1, 2, 1)
            (x^2 + 1)*myKeyChr121^254 +
            (x^3 + 1)*myKeyChr121^253 +
            (x^7 + x^6 + x^5 + x^4 + x^3 + 1)*myKeyChr121^251 +
            (x^5 + x^2 + 1)*myKeyChr121^247 +
            (x^7 + x^6 + x^5 + x^4 + x^2)*myKeyChr121^239 +
            myKeyChr121^223 +
            (x^7 + x^5 + x^4 + x^2 + 1)*myKeyChr121^191 +
            (x^7 + x^3 + x^2 + x + 1)*myKeyChr121^127 +
            myKeyChr010 +
            (x^6 + x^5 + x)
        """
    def __call__(self, text, key, algorithm: str = 'encrypt', format: str = 'hex'):
        '''
        Return the encryption/decryption of ``text`` with key ``key``.

        INPUT:

        - ``text`` -- a plaintext to encrypt or a ciphertext to decrypt

        - ``key`` -- the key to encrypt/decrypt ``text`` with

        - ``algorithm`` -- whether to encrypt or decrypt ``text``. Flag for
          encryption is "encrypt", flag for decryption is "decrypt"

        - ``format`` -- the format of ``text`` and ``key``, either "hex" or
          "binary"

        OUTPUT: the encrypted or decrypted message ``text`` with key ``key``

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: text = \'ef053f7c8b3d32fd4d2a64ad3c93071a\'
            sage: key = \'2d7e86a339d9393ee6570a1101904e16\'
            sage: rgf(text, key)
            \'84e75b142c8fd5a445312c0a9b2d6699\'
            sage: rgf(text, key, algorithm=\'decrypt\')
            \'9bf83275406304f050c826ca72d035e6\'

        We can also use binary strings for ``text`` and ``key``. ::

            sage: text = \'11011100011010000011101111011011\' * 4
            sage: key = \'01000000000011000101101011011110\' * 4
            sage: rgf(text, key, format=\'binary\')
            \'00011000010110010011100100010111010101001000010010100110101010101111001001100000011111011100100011010001010100110011000111110011\'
            sage: rgf(text, key, algorithm=\'decrypt\', format=\'binary\')
            \'11000110011001001110000101011101001001010101110001110010000111110000010111111101000011010101101011111100100001010010111000011010\'
        '''
    def block_length(self):
        """
        Return the block length of this instantiation of Rijndael-GF.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 6)
            sage: rgf.block_length()
            4
        """
    def key_length(self):
        """
        Return the key length of this instantiation of Rijndael-GF.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 8)
            sage: rgf.key_length()
            8
        """
    def number_rounds(self):
        """
        Return the number of rounds used in this instantiation of Rijndael-GF.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(5, 4)
            sage: rgf.number_rounds()
            11
        """
    def encrypt(self, plain, key, format: str = 'hex'):
        '''
        Return the plaintext ``plain`` encrypted with the key ``key``.

        INPUT:

        - ``plain`` -- the plaintext to be encrypted

        - ``key`` -- the key to encrypt ``plain`` with

        - ``format`` -- (default: ``hex``) the string format of ``key`` and
          ``plain``, either "hex" or "binary"

        OUTPUT: string of the plaintext ``plain`` encrypted with the key ``key``

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: key = \'c81677bc9b7ac93b25027992b0261996\'
            sage: plain = \'fde3bad205e5d0d73547964ef1fe37f1\'
            sage: expected_ciphertext = \'e767290ddfc6414e3c50a444bec081f0\'
            sage: rgf.encrypt(plain, key) == expected_ciphertext
            True

        We can encrypt binary strings as well. ::

            sage: key = \'10010111110000011111011011010001\' * 4
            sage: plain = \'00000000101000000000000001111011\' * 4
            sage: expected_ciphertext = (\'11010111100100001010001011110010111\'
            ....: \'1110011000000011111100100011011100101000000001000111000010\'
            ....: \'00100111011011001000111101111110100\')
            sage: result = rgf.encrypt(plain, key, format=\'binary\')
            sage: result == expected_ciphertext
            True
        '''
    def decrypt(self, ciphertext, key, format: str = 'hex'):
        '''
        Return the ciphertext ``ciphertext`` decrypted with the key ``key``.

        INPUT:

        - ``ciphertext`` -- the ciphertext to be decrypted

        - ``key`` -- the key to decrypt ``ciphertext`` with

        - ``format`` -- (default: ``hex``) the string format that both
          ``ciphertext`` and ``key`` must be in, either "hex" or "binary"

        OUTPUT:

        - A string in the format ``format`` of ``ciphertext`` decrypted with
          key ``key``.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: key = \'2dfb02343f6d12dd09337ec75b36e3f0\'
            sage: ciphertext = \'54d990a16ba09ab596bbf40ea111702f\'
            sage: expected_plaintext = \'1e1d913b7274ad9b5a4ab1a5f9133b93\'
            sage: rgf.decrypt(ciphertext, key) == expected_plaintext
            True

        We can also decrypt messages using binary strings. ::

            sage: key = \'00011010000011100011000000111101\' * 4
            sage: ciphertext = \'00110010001110000111110110000001\' * 4
            sage: expected_plaintext = (\'101111111010011100111100101010100111\'
            ....: \'1111010000101101100001101000000000000000010000000100111011\'
            ....: \'0100001111100011010001101101001011\')
            sage: result = rgf.decrypt(ciphertext, key, format=\'binary\')
            sage: result == expected_plaintext
            True
        '''
    def expand_key(self, key):
        """
        Return the expanded key schedule from ``key``.

        INPUT:

        - ``key`` -- the key to build a key schedule from. Must be a matrix
          over `\\GF{2^8}` of dimensions `4 \\times N_k`

        OUTPUT:

        - A length `Nr` list of `4 \\times N_b` matrices corresponding to the
          expanded key. The `n` th entry of the list corresponds to the matrix
          used in the ``add_round_key`` step of the `n` th round.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 6)
            sage: key = '331D0084B176C3FB59CAA0EDA271B565BB5D9A2D1E4B2892'
            sage: key_state = rgf._hex_to_GF(key)
            sage: key_schedule = rgf.expand_key(key_state)
            sage: rgf._GF_to_hex(key_schedule[0])
            '331d0084b176c3fb59caa0eda271b565'
            sage: rgf._GF_to_hex(key_schedule[6])
            '5c5d51c4121f018d0f4f3e408ae9f78c'
        """
    def expand_key_poly(self, row, col, round):
        """
        Return a polynomial representing the ``row,col`` th entry of the
        ``round`` th round key.

        INPUT:

        - ``row`` -- the row position of the element represented by this
          polynomial

        - ``col`` -- the column position of the element represented by this
          polynomial

        OUTPUT:

        - A polynomial representing the ``row,col`` th entry of the ``round``
          th round key in terms of entries of the input key.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: rgf.expand_key_poly(1, 2, 0)
            k012
            sage: rgf.expand_key_poly(1, 2, 1)
            (x^2 + 1)*k023^254 +
            (x^3 + 1)*k023^253 +
            (x^7 + x^6 + x^5 + x^4 + x^3 + 1)*k023^251 +
            (x^5 + x^2 + 1)*k023^247 +
            (x^7 + x^6 + x^5 + x^4 + x^2)*k023^239 +
            k023^223 +
            (x^7 + x^5 + x^4 + x^2 + 1)*k023^191 +
            (x^7 + x^3 + x^2 + x + 1)*k023^127 +
            k010 +
            k011 +
            k012 +
            (x^6 + x^5 + x)

        It should be noted that ``expand_key_poly`` cannot be used with
        ``apply_poly`` or ``compose``, since ``expand_key_poly`` is not a
        ``Round_Component_Poly_Constr`` object. ::

            sage: rgf.compose(rgf.sub_bytes_poly_constr(), rgf.expand_key_poly)
            Traceback (most recent call last):
            ...
            TypeError: keyword 'g' must be a Round_Component_Poly_Constr or
            a polynomial over Finite Field in x of size 2^8
            <BLANKLINE>
            sage: state = rgf._hex_to_GF('00000000000000000000000000000000')
            sage: rgf.apply_poly(state, rgf.expand_key_poly)
            Traceback (most recent call last):
            ...
            TypeError: keyword 'poly_constr' must be a Round_Component_Poly_Constr
        """
    def apply_poly(self, state, poly_constr, algorithm: str = 'encrypt', keys=None, poly_constr_attr=None):
        '''
        Return a state matrix where ``poly_method`` is applied to each entry.

        INPUT:

        - ``state`` -- the state matrix over `\\GF{2^8}` to which
          ``poly_method`` is applied to

        - ``poly_constr`` -- the ``Round_Component_Poly_Constr`` object to
          build polynomials during evaluation

        - ``algorithm`` -- (default: ``\'encrypt\'``) passed directly to
          ``rcpc`` to select encryption or decryption; the
          encryption flag is "encrypt" and the decrypt flag is "decrypt"

        - ``keys`` -- (default: ``None``) an array of `N_r` subkey matrices to
          replace any key variables in any polynomials returned by
          ``poly_method``. Must be identical to the format returned by
          ``expand_key``. If any polynomials have key variables and ``keys``
          is not supplied, the key variables will remain as-is.

        - ``poly_constr_attr`` -- (default: ``None``) a dictionary of keyword
          attributes to pass to ``rcpc`` when it is called

        OUTPUT:

        - A state matrix in `\\GF{2^8}` whose `i,j` th entry equals the
          polynomial ``poly_constr(i, j, algorithm, **poly_constr_attr)``
          evaluated by setting its variables equal to the corresponding
          entries of ``state``.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: state = rgf._hex_to_GF(\'3b59cb73fcd90ee05774222dc067fb68\')
            sage: result = rgf.apply_poly(state, rgf.shift_rows_poly_constr())
            sage: rgf._GF_to_hex(result)
            \'3bd92268fc74fb735767cbe0c0590e2d\'

        Calling ``apply_poly`` with the ``Round_Component_Poly_Constr`` object
        of a round component (e.g. ``sub_bytes_poly``) is identical to
        calling that round component function itself. ::

            sage: state = rgf._hex_to_GF(\'4915598f55e5d7a0daca94fa1f0a63f7\')
            sage: apply_poly_result = rgf.apply_poly(state,
            ....:                                    rgf.sub_bytes_poly_constr())
            sage: direct_result = rgf.sub_bytes(state)
            sage: direct_result == apply_poly_result
            True

        If the ``Round_Component_Poly_Constr`` object\'s ``__call__`` method
        returns a polynomial with state variables as well as key variables, we
        can supply a list of `N_r` round keys ``keys`` whose elements are
        evaluated as the key variables. If this is not provided, the key
        variables will remain as is.::

            sage: state = rgf._hex_to_GF(\'14f9701ae35fe28c440adf4d4ea9c026\')
            sage: key = rgf._hex_to_GF(\'54d990a16ba09ab596bbf40ea111702f\')
            sage: keys = rgf.expand_key(key)
            sage: result = rgf.apply_poly(state,
            ....:                         rgf.add_round_key_poly_constr(),
            ....:                         keys=keys)
            sage: result == rgf.add_round_key(state, key)
            True
            <BLANKLINE>
            sage: rgf.apply_poly(state, rgf.add_round_key_poly_constr())[0,0]
            k000 + (x^4 + x^2)

        We can change the value of the keywords of ``poly_constr`` \'s
        ``__call__`` method when ``apply_poly`` calls it by passing in a
        dictionary ``poly_constr_attr`` mapping keywords to their values. ::

            sage: rgf.apply_poly(rgf.state_vrs,
            ....:                rgf.add_round_key_poly_constr(),
            ....:                poly_constr_attr={\'round\': 5})
            [a00 + k500 a01 + k501 a02 + k502 a03 + k503]
            [a10 + k510 a11 + k511 a12 + k512 a13 + k513]
            [a20 + k520 a21 + k521 a22 + k522 a23 + k523]
            [a30 + k530 a31 + k531 a32 + k532 a33 + k533]
        '''
    def compose(self, f, g, algorithm: str = 'encrypt', f_attr=None, g_attr=None):
        '''
        Return a ``Round_Component_Poly_Constr`` object corresponding to
        `g \\circ f` or the polynomial output of this object\'s ``__call__``
        method.

        INPUT:

        - ``f`` -- a ``Round_Component_Poly_Constr`` object corresponding to
          a round component function `f`

        - ``g`` -- a ``Round_Component_Poly_Constr`` object corresponding to
          a round component function `g` or a polynomial output of this
          object\'s ``__call__`` method.

        - ``algorithm`` -- (default: ``\'encrypt\'``) whether ``f`` and ``g``
          should use their encryption transformations or their decryption
          transformations. Does nothing if ``g`` is a
          ``Round_Component_Poly_Constr`` object. The encryption flag is
          "encrypt" and the decryption flag is "decrypt".

        - ``f_attr`` -- (default: ``None``) a dictionary of keyword attributes to
          pass to ``f`` when it is called

        - ``g_attr`` -- (default: ``None``) a dictionary of keyword attributes to
          pass to ``g`` when it is called; does nothing if ``g`` is a
          polynomial

        OUTPUT:

        - If ``g`` is a ``Round_Component_Poly_Constr`` object corresponding
          to a round component function `g`, then ``compose`` returns a
          ``Round_Component_Poly_Constr`` corresponding to the round
          component function `g \\circ f`, where `f` is the round component
          function corresponding to the first argument ``f``. On the other
          hand, if ``g`` `= g(A)_{i,j}` for a round component function `g`,
          then ``compose`` returns `g(f(A))_{i,j}`, where `A` is an
          arbitrary input state matrix.

        EXAMPLES:

        This function allows us to determine the polynomial representations
        of entries across multiple round functions. For example, if we
        wanted a polynomial representing the ``1,3`` entry of a matrix after
        we first apply ShiftRows and then MixColumns to that matrix, we do::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: mcp = rgf.mix_columns_poly_constr()(1, 3); mcp
            a03 + x*a13 + (x + 1)*a23 + a33
            sage: result = rgf.compose(rgf.shift_rows_poly_constr(), mcp)
            sage: result
            a03 + x*a10 + (x + 1)*a21 + a32

        We can test the correctness of this::

            sage: state = rgf._hex_to_GF(\'fa636a2825b339c940668a3157244d17\')
            sage: new_state = rgf.shift_rows(state)
            sage: new_state = rgf.mix_columns(new_state)
            sage: result(state.list()) == new_state[1,3]
            True

        We can also use ``compose`` to build a new
        ``Round_Component_Poly_Constr`` object corresponding to the composition
        of multiple round functions as such::

            sage: fn = rgf.compose(rgf.shift_rows_poly_constr(),                        # needs sage.libs.gap
            ....:                  rgf.mix_columns_poly_constr())
            sage: fn(1, 3)                                                              # needs sage.libs.gap
            a03 + x*a10 + (x + 1)*a21 + a32

        If we use ``compose`` to make a new ``Round_Component_Poly_Constr``
        object, we can use that object as input to ``apply_poly`` and
        ``compose``::

            sage: state = rgf._hex_to_GF(\'36400926f9336d2d9fb59d23c42c3950\')
            sage: result = rgf.apply_poly(state, fn)                                    # needs sage.libs.gap
            sage: rgf._GF_to_hex(result)
            \'f4bcd45432e554d075f1d6c51dd03b3c\'
            <BLANKLINE>
            sage: new_state = rgf.shift_rows(state)
            sage: new_state = rgf.mix_columns(new_state)
            sage: result == new_state
            True

        ::

            sage: fn2 = rgf.compose(rgf.sub_bytes_poly_constr(), fn)                    # needs sage.libs.gap

        If the second argument is a polynomial, then the value of ``algorithm``
        is passed directly to the first argument `f` during evaluation.
        However, if the second argument is a ``Round_Component_Poly_Constr``
        object, changing ``algorithm`` does nothing since the returned object
        has its own ``algorithm=\'encrypt\'`` keyword. ::

            sage: f = rgf.compose(rgf.sub_bytes_poly_constr(),                          # needs sage.libs.gap
            ....:                 rgf.mix_columns_poly_constr(),
            ....:                 algorithm=\'decrypt\')
            sage: g = rgf.compose(rgf.sub_bytes_poly_constr(),                          # needs sage.libs.gap
            ....:                 rgf.mix_columns_poly_constr())
            sage: all(f(i,j) == g(i,j) for i in range(4) for j in range(4))             # needs sage.libs.gap
            True

        We can change the keyword attributes of the ``__call__`` methods of
        ``f`` and ``g`` by passing dictionaries ``f_attr`` and ``g_attr`` to
        ``compose``. ::

            sage: fn = rgf.compose(rgf.add_round_key_poly_constr(),                     # needs sage.libs.gap
            ....:                  rgf.add_round_key_poly_constr(),
            ....:                  f_attr={\'round\': 4}, g_attr={\'round\': 7})
            sage: fn(1, 2)                                                              # needs sage.libs.gap
            a12 + k412 + k712
        '''
    def add_round_key_poly_constr(self):
        """
        Return the ``Round_Component_Poly_Constr`` object corresponding to
        AddRoundKey.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: ark_pc = rgf.add_round_key_poly_constr()
            sage: ark_pc
            A polynomial constructor for the function 'Add Round Key' of Rijndael-GF
            block cipher with block length 4, key length 4, and 10 rounds.
            sage: ark_pc(0, 1)
            a01 + k001

        When invoking the returned object's ``__call__`` method, changing the
        value of ``algorithm='encrypt'`` does nothing, since the AddRoundKey
        round component function is its own inverse. ::

            sage: with_encrypt = ark_pc(1, 1, algorithm='encrypt')
            sage: with_decrypt = ark_pc(1, 1, algorithm='decrypt')
            sage: with_encrypt == with_decrypt
            True

        When invoking the returned object's ``__call__`` method, one can change
        the round subkey used in the returned polynomial by changing the
        ``round=0`` keyword. ::

            sage: ark_pc(2, 1, round=7)
            a21 + k721

        When passing the returned object to methods such as ``apply_poly`` and
        ``compose``, we can make these methods use a non-default value for
        ``round=0`` by passing in a dictionary mapping ``round`` to a different
        value. ::

            sage: rgf.apply_poly(rgf.state_vrs, ark_pc,
            ....:                poly_constr_attr={'round': 6})
            [a00 + k600 a01 + k601 a02 + k602 a03 + k603]
            [a10 + k610 a11 + k611 a12 + k612 a13 + k613]
            [a20 + k620 a21 + k621 a22 + k622 a23 + k623]
            [a30 + k630 a31 + k631 a32 + k632 a33 + k633]

        ::

            sage: rcpc = rgf.compose(ark_pc, ark_pc,                                    # needs sage.libs.gap
            ....:                    f_attr={'round': 3}, g_attr={'round': 5})
            sage: rcpc(3, 1)                                                            # needs sage.libs.gap
            a31 + k331 + k531
        """
    def add_round_key(self, state, round_key):
        """
        Return the round-key addition of matrices ``state`` and ``round_key``.

        INPUT:

        - ``state`` -- the state matrix to have ``round_key`` added to

        - ``round_key`` -- the round key to add to ``state``

        OUTPUT:

        - A state matrix which is the round key addition of ``state`` and
          ``round_key``. This transformation is simply the entrywise addition
          of these two matrices.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: state = rgf._hex_to_GF('36339d50f9b539269f2c092dc4406d23')
            sage: key = rgf._hex_to_GF('7CC78D0E22754E667E24573F454A6531')
            sage: key_schedule = rgf.expand_key(key)
            sage: result = rgf.add_round_key(state, key_schedule[0])
            sage: rgf._GF_to_hex(result)
            '4af4105edbc07740e1085e12810a0812'
        """
    def sub_bytes_poly_constr(self):
        """
        Return the ``Round_Component_Poly_Constr`` object corresponding to
        SubBytes.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: sb_pc = rgf.sub_bytes_poly_constr(); sb_pc
            A polynomial constructor for the function 'SubBytes' of Rijndael-GF
            block cipher with block length 4, key length 4, and 10 rounds.
            sage: sb_pc(2, 3)
            (x^2 + 1)*a23^254 +
            (x^3 + 1)*a23^253 +
            (x^7 + x^6 + x^5 + x^4 + x^3 + 1)*a23^251 +
            (x^5 + x^2 + 1)*a23^247 +
            (x^7 + x^6 + x^5 + x^4 + x^2)*a23^239 +
            a23^223 +
            (x^7 + x^5 + x^4 + x^2 + 1)*a23^191 +
            (x^7 + x^3 + x^2 + x + 1)*a23^127 +
            (x^6 + x^5 + x + 1)

        The returned object's ``__call__`` method has an additional keyword
        of ``no_inversion=False``, which causes the returned polynomial to
        represent only the affine transformation step of SubBytes. ::

            sage: sb_pc(1, 0, no_inversion=True)
            (x^7 + x^3 + x^2 + x + 1)*a10^128 +
            (x^7 + x^5 + x^4 + x^2 + 1)*a10^64 +
            a10^32 +
            (x^7 + x^6 + x^5 + x^4 + x^2)*a10^16 +
            (x^5 + x^2 + 1)*a10^8 +
            (x^7 + x^6 + x^5 + x^4 + x^3 + 1)*a10^4 +
            (x^3 + 1)*a10^2 +
            (x^2 + 1)*a10 +
            (x^6 + x^5 + x + 1)

        We can build a polynomial representing the inverse transformation
        by setting the keyword ``algorithm='decrypt'``. However, the order of
        the affine transformation and the inversion step in SubBytes means that
        this polynomial has thousands of terms and is very slow to compute.
        Hence, if one wishes to build the decryption polynomial with the
        intention of evaluating that polynomial for a particular input, it is
        strongly recommended to first call
        ``sb_pc(i, j, algorithm='decrypt', no_inversion=True)`` to build a
        polynomial representing only the inverse affine transformation,
        evaluate this polynomial for your intended input, then finally
        calculate the inverse of the result. ::

            sage: poly = sb_pc(1, 2, algorithm='decrypt', no_inversion=True)
            sage: state = rgf._hex_to_GF('39daee38f4f1a82aaf432410c36d45b9')
            sage: result = poly(state.list())
            sage: rgf._GF_to_hex(result * -1)
            '49'

        When passing the returned object to ``apply_poly`` and ``compose``, we
        can make those methods change the keyword ``no_inversion`` of this
        object's ``__call__`` method by passing the dictionary
        ``{'no_inversion': True}`` to them. ::

            sage: result = rgf.apply_poly(state, sb_pc,
            ....:                         poly_constr_attr={'no_inversion': True})
            sage: rgf._GF_to_hex(result)
            '961c72894526f746aa85fc920adcc719'

        ::

            sage: rcpc = rgf.compose(sb_pc, rgf.shift_rows_poly_constr(),               # needs sage.libs.gap
            ....:                    f_attr={'no_inversion': True})

        Note that if we set ``algorithm='decrypt'`` for ``apply_poly``, it
        will perform the necessary performance enhancement described above
        automatically. The structure of ``compose``, however, unfortunately
        does not allow this enhancement to be employed.
        """
    def sub_bytes(self, state, algorithm: str = 'encrypt'):
        '''
        Return the application of SubBytes to the state matrix ``state``.

        INPUT:

        - ``state`` -- the state matrix to apply SubBytes to

        - ``algorithm`` -- (default: ``\'encrypt\'``) whether to apply the
          encryption step of SubBytes or its decryption inverse. The encryption
          flag is "encrypt" and the decryption flag is "decrypt".

        OUTPUT: the state matrix over `\\GF{2^8}` where SubBytes has been
        applied to every entry of ``state``

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: state = rgf._hex_to_GF(\'d1c4941f7955f40fb46f6c0ad68730ad\')
            sage: result = rgf.sub_bytes(state)
            sage: rgf._GF_to_hex(result)
            \'3e1c22c0b6fcbf768da85067f6170495\'
            sage: decryption = rgf.sub_bytes(result, algorithm=\'decrypt\')
            sage: decryption == state
            True
        '''
    def mix_columns_poly_constr(self):
        """
        Return a ``Round_Component_Poly_Constr`` object corresponding to
        MixColumns.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: mc_pc = rgf.mix_columns_poly_constr()
            sage: mc_pc
            A polynomial constructor for the function 'Mix Columns' of Rijndael-GF
            block cipher with block length 4, key length 4, and 10 rounds.
            sage: mc_pc(1, 2)
            a02 + x*a12 + (x + 1)*a22 + a32
            sage: mc_pc(1, 0, algorithm='decrypt')
            (x^3 + 1)*a00 + (x^3 + x^2 + x)*a10 + (x^3 + x + 1)*a20 + (x^3 + x^2 + 1)*a30

        The returned object's ``__call__`` method has no additional keywords,
        unlike ``sub_bytes_poly_constr()`` and ``add_round_key_poly_constr()``.
        """
    def mix_columns(self, state, algorithm: str = 'encrypt'):
        '''
        Return the application of MixColumns to the state matrix ``state``.

        INPUT:

        - ``state`` -- the state matrix to apply MixColumns to

        - ``algorithm`` -- (default: ``\'encrypt\'``) whether to perform the
          encryption version of MixColumns, or its decryption inverse; the
          encryption flag is "encrypt" and the decryption flag is "decrypt"

        OUTPUT: the state matrix over `\\GF{2^8}` which is the result of
        applying MixColumns to ``state``

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: state = rgf._hex_to_GF(\'cd54c7283864c0c55d4c727e90c9a465\')
            sage: result = rgf.mix_columns(state)
            sage: rgf._GF_to_hex(result)
            \'921f748fd96e937d622d7725ba8ba50c\'
            sage: decryption = rgf.mix_columns(result, algorithm=\'decrypt\')
            sage: decryption == state
            True
        '''
    def shift_rows_poly_constr(self):
        """
        Return a ``Round_Component_Poly_Constr`` object corresponding to
        ShiftRows.

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: sr_pc = rgf.shift_rows_poly_constr()
            sage: sr_pc(3, 0)
            a33
            sage: sr_pc(2, 1, algorithm='decrypt')
            a23

        The returned object's ``__call__`` method has no additional keywords,
        unlike ``sub_bytes_poly_constr()`` and ``add_round_key_poly_constr``.
        """
    def shift_rows(self, state, algorithm: str = 'encrypt'):
        '''
        Return the application of ShiftRows to the state matrix ``state``.

        INPUT:

        - ``state`` -- a state matrix over `\\GF{2^8}` to which ShiftRows is
          applied to

        - ``algorithm`` -- (default: ``\'encrypt\'``) whether to perform the
          encryption version of ShiftRows or its decryption inverse; the
          encryption flag is "encrypt" and the decryption flag is "decrypt"

        OUTPUT: a state matrix over `\\GF{2^8}` which is the application of
        ShiftRows to ``state``

        EXAMPLES::

            sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
            sage: rgf = RijndaelGF(4, 4)
            sage: state = rgf._hex_to_GF(\'adcb0f257e9c63e0bc557e951c15ef01\')
            sage: result = rgf.shift_rows(state)
            sage: rgf._GF_to_hex(result)
            \'ad9c7e017e55ef25bc150fe01ccb6395\'
            sage: decryption = rgf.shift_rows(result, algorithm=\'decrypt\')
            sage: decryption == state
            True
        '''
    class Round_Component_Poly_Constr(SageObject):
        def __init__(self, polynomial_constr, rgf, round_component_name=None) -> None:
            '''
            An object which constructs polynomials representing round
            component functions of a RijndaelGF object.

            INPUT:

            - ``polynomial_constr`` -- a function which takes an index
              ``row,col`` and returns a polynomial representing the ``row,col``
              th entry of a matrix after a specific round component function
              has been applied to it. This polynomial must be in terms of
              entries of the input matrix to that round component function and
              of entries of various subkeys. ``polynomial_constr`` must have
              arguments of the form ``polynomial_constr(row, col,
              algorithm=\'encrypt\', **kwargs)`` and  must be able to be called
              as ``polynomial_constr(row, col)``.

            - ``rgf`` -- the RijndaelGF object whose state entries are
              represented by polynomials returned from ``polynomial_constr``

            - ``round_component_name`` -- the name of the round component
              function this object corresponds to as a string; used solely
              for display purposes

            EXAMPLES::

                sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
                sage: rgf = RijndaelGF(4, 4)
                sage: rcpc = RijndaelGF.Round_Component_Poly_Constr(
                ....:            rgf._shift_rows_pc, rgf, "Shift Rows")
                sage: rcpc
                A polynomial constructor for the function \'Shift Rows\' of
                Rijndael-GF block cipher with block length 4, key length 4,
                and 10 rounds.

            If `\\phi` is the round component function to which this object
            corresponds to, then ``__call__(i,j)`` `= \\phi(A)_{i,j}`, where
            `A` is an arbitrary input matrix. Note that the polynomial returned
            by ``__call__(i,j)`` will be in terms of the entries of `A`. ::

                sage: rcpc = RijndaelGF.Round_Component_Poly_Constr(
                ....:            rgf._mix_columns_pc, rgf, "Mix Columns")
                sage: poly = rcpc(1, 2); poly
                a02 + x*a12 + (x + 1)*a22 + a32
                sage: state = rgf._hex_to_GF(\'d1876c0f79c4300ab45594add66ff41f\')
                sage: result = rgf.mix_columns(state)
                sage: result[1,2] == poly(state.list())
                True

            Invoking this objects ``__call__`` method passes its arguments
            directly to ``polynomial_constr`` and returns the result. In a
            sense, ``Round_Component_Poly_Constr`` acts as a wrapper for
            the ``polynomial_constr`` method and helps ensure that each
            ``Round_Component_Poly_Constr`` object will act similarly. ::

                sage: all(rgf._mix_columns_pc(i, j) == rcpc(i, j)
                ....:     for i in range(4) for j in range(4))
                True

            Since all keyword arguments of ``polynomial_constr`` must have a
            default value except for ``row`` and ``col``, we can always call
            a ``Round_Component_Poly_Constr`` object by ``__call__(row, col)``.
            Because of this, methods such as ``apply_poly`` and ``compose``
            will only call ``__call__(row, col)`` when passed a
            ``Round_Component_Poly_Constr`` object. In order to change this
            object\'s behavior and force methods such as ``apply_poly`` to use
            non-default values for keywords we can pass dictionaries mapping
            keywords to non-default values as input to ``apply_poly`` and
            ``compose``. ::

                sage: rgf.apply_poly(rgf.state_vrs,
                ....:                rgf.add_round_key_poly_constr(),
                ....:                poly_constr_attr={\'round\': 9})
                [a00 + k900 a01 + k901 a02 + k902 a03 + k903]
                [a10 + k910 a11 + k911 a12 + k912 a13 + k913]
                [a20 + k920 a21 + k921 a22 + k922 a23 + k923]
                [a30 + k930 a31 + k931 a32 + k932 a33 + k933]

            ::

                sage: fn = rgf.compose(rgf.add_round_key_poly_constr(),                 # needs sage.libs.gap
                ....:                  rgf.add_round_key_poly_constr(),
                ....:                  f_attr={\'round\': 3}, g_attr={\'round\': 7})
                sage: fn(2, 3)                                                          # needs sage.libs.gap
                a23 + k323 + k723

            Because all ``Round_Component_Poly_Constr`` objects are callable
            as ``__call__(row, col, algorithm)``, ``__call__`` will check
            the validity of these three arguments automatically. Any other
            keywords, however, must be checked in ``polynomial_constr``. ::

                sage: def my_poly_constr(row, col, algorithm=\'encrypt\'):
                ....:     return x * rgf._F.one()  # example body with no checks
                sage: rcpc = RijndaelGF.Round_Component_Poly_Constr(
                ....:            my_poly_constr, rgf, "My Poly Constr")
                sage: rcpc(-1, 2)
                Traceback (most recent call last):
                ...
                ValueError: keyword \'row\' must be in range 0 - 3
                sage: rcpc(1, 2, algorithm=5)
                Traceback (most recent call last):
                ...
                ValueError: keyword \'algorithm\' must be either \'encrypt\' or \'decrypt\'
            '''
        def __call__(self, row, col, algorithm: str = 'encrypt', **kwargs):
            '''
            Return ``polynomial_constr(row, col, algorithm, **attr_dict)``.

            INPUT:

            - ``row`` -- the row number to pass to ``polynomial_constr``

            - ``col`` -- the column number to pass to ``polynomial_constr``

            - ``algorithm`` -- (default: ``\'encrypt\'``) the algorithm keyword
              to pass to ``polynomial_constr``

            - ``**kwargs`` -- keyword arguments to pass to
              ``polynomial_constr``. Keyword arguments will vary depending
              on ``polynomial_constr``

            OUTPUT:

            - The output of ``polynomial_constr(row, col, algorithm,
              ** attr_dict)``. This is required to be a polynomial over
              `\\GF{2^8}`.

            EXAMPLES::

                sage: from sage.crypto.mq.rijndael_gf import RijndaelGF
                sage: rgf = RijndaelGF(4, 4)
                sage: rcpc = RijndaelGF.Round_Component_Poly_Constr(
                ....:            rgf._shift_rows_pc, rgf, "Shift Rows")
                sage: rcpc(1, 2)
                a13
                sage: all(rcpc(i, j) == rgf._shift_rows_pc(i, j)
                ....:     for i in range(4) for j in range(4))
                True
            '''
