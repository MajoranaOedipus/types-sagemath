import types
from .mpolynomialsystemgenerator import MPolynomialSystemGenerator as MPolynomialSystemGenerator
from _typeshed import Incomplete
from sage.matrix.constructor import matrix as matrix, random_matrix as random_matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.flatten import flatten as flatten
from sage.misc.verbose import get_verbose as get_verbose
from sage.modules.vector_modn_dense import Vector_modn_dense as Vector_modn_dense
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial_sequence import PolynomialSequence as PolynomialSequence
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.structure.element import Matrix as Matrix

def SR(n: int = 1, r: int = 1, c: int = 1, e: int = 4, star: bool = False, **kwargs):
    """
    Return a small scale variant of the AES polynomial system
    constructor subject to the following conditions:

    INPUT:

    - ``n`` -- the number of rounds (default: 1)
    - ``r`` -- the number of rows in the state array (default: 1)
    - ``c`` -- the number of columns in the state array (default: 1)
    - ``e`` -- the exponent of the finite extension field (default: 4)
    - ``star`` -- determines if SR\\* or SR should be constructed (default: ``False``)
    - ``aes_mode`` -- as the SR key schedule specification differs
      slightly from the AES key schedule, this parameter controls
      which schedule to use (default: ``True``)
    - ``gf2`` -- generate polynomial systems over `\\GF{2}` rather than
      over `\\GF{2^e}` (default: ``False``)
    - ``polybori`` -- use the ``BooleanPolynomialRing`` as polynomial
      representation (default: ``True``, `\\GF{2}` only)
    - ``order`` -- string to specify the term ordering of the
      variables (default: ``deglex``)
    - ``postfix`` -- string which is appended after the variable name
      (default: ``''``)
    - ``allow_zero_inversions`` -- boolean to control whether zero
      inversions raise an exception (default: ``False``)
    - ``correct_only`` -- only include correct inversion polynomials
      (default: ``False``, `\\GF{2}` only)
    - ``biaffine_only`` -- only include bilinear and biaffine inversion
      polynomials (default: ``True``, `\\GF{2}` only)

    EXAMPLES::

        sage: sr = mq.SR(1, 1, 1, 4)
        sage: ShiftRows = sr.shift_rows_matrix()
        sage: MixColumns = sr.mix_columns_matrix()
        sage: Lin = sr.lin_matrix()
        sage: M = MixColumns * ShiftRows * Lin
        sage: print(sr.hex_str_matrix(M))
         5 1 C 5
         2 2 1 F
         A 4 4 1
         1 8 3 3

    ::

        sage: sr = mq.SR(1, 2, 1, 4)
        sage: ShiftRows = sr.shift_rows_matrix()
        sage: MixColumns = sr.mix_columns_matrix()
        sage: Lin = sr.lin_matrix()
        sage: M = MixColumns * ShiftRows * Lin
        sage: print(sr.hex_str_matrix(M))
         F 3 7 F A 2 B A
         A A 5 6 8 8 4 9
         7 8 8 2 D C C 3
         4 6 C C 5 E F F
         A 2 B A F 3 7 F
         8 8 4 9 A A 5 6
         D C C 3 7 8 8 2
         5 E F F 4 6 C C

    ::

        sage: sr = mq.SR(1, 2, 2, 4)
        sage: ShiftRows = sr.shift_rows_matrix()
        sage: MixColumns = sr.mix_columns_matrix()
        sage: Lin = sr.lin_matrix()
        sage: M = MixColumns * ShiftRows * Lin
        sage: print(sr.hex_str_matrix(M))
         F 3 7 F 0 0 0 0 0 0 0 0 A 2 B A
         A A 5 6 0 0 0 0 0 0 0 0 8 8 4 9
         7 8 8 2 0 0 0 0 0 0 0 0 D C C 3
         4 6 C C 0 0 0 0 0 0 0 0 5 E F F
         A 2 B A 0 0 0 0 0 0 0 0 F 3 7 F
         8 8 4 9 0 0 0 0 0 0 0 0 A A 5 6
         D C C 3 0 0 0 0 0 0 0 0 7 8 8 2
         5 E F F 0 0 0 0 0 0 0 0 4 6 C C
         0 0 0 0 A 2 B A F 3 7 F 0 0 0 0
         0 0 0 0 8 8 4 9 A A 5 6 0 0 0 0
         0 0 0 0 D C C 3 7 8 8 2 0 0 0 0
         0 0 0 0 5 E F F 4 6 C C 0 0 0 0
         0 0 0 0 F 3 7 F A 2 B A 0 0 0 0
         0 0 0 0 A A 5 6 8 8 4 9 0 0 0 0
         0 0 0 0 7 8 8 2 D C C 3 0 0 0 0
         0 0 0 0 4 6 C C 5 E F F 0 0 0 0
    """

class SR_generic(MPolynomialSystemGenerator):
    def __init__(self, n: int = 1, r: int = 1, c: int = 1, e: int = 4, star: bool = False, **kwargs) -> None:
        """
        Small Scale Variants of the AES.

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4)
            sage: ShiftRows = sr.shift_rows_matrix()
            sage: MixColumns = sr.mix_columns_matrix()
            sage: Lin = sr.lin_matrix()
            sage: M = MixColumns * ShiftRows * Lin
            sage: print(sr.hex_str_matrix(M))
             5 1 C 5
             2 2 1 F
             A 4 4 1
             1 8 3 3
        """
    def new_generator(self, **kwds):
        """
        Return a new ``SR`` instance equal to this instance
        except for the parameters passed explicitly to this function.

        INPUT:

        - ``**kwds`` -- see the ``SR`` constructor for accepted
          parameters

        EXAMPLES::

            sage: sr = mq.SR(2,1,1,4); sr
            SR(2,1,1,4)
            sage: sr.ring().base_ring()
            Finite Field in a of size 2^4

        ::

            sage: sr2 = sr.new_generator(gf2=True); sr2
            SR(2,1,1,4)
            sage: sr2.ring().base_ring()
            Finite Field of size 2
            sage: sr3 = sr2.new_generator(correct_only=True)
            sage: len(sr2.inversion_polynomials_single_sbox())
            20
            sage: len(sr3.inversion_polynomials_single_sbox())
            19
        """
    R: Incomplete
    k: Incomplete
    Lin: Incomplete
    ShiftRows: Incomplete
    MixColumns: Incomplete
    M: Incomplete
    Mstar: Incomplete
    def __getattr__(self, attr):
        """
        EXAMPLES::

            sage: sr = mq.SR(1, 2, 1, 4, gf2=True)
            sage: sr.Mstar
            [1 0 1 1 0 0 0 0]
            [1 1 0 1 0 0 0 0]
            [1 1 1 0 0 0 0 0]
            [0 1 1 1 0 0 0 0]
            [0 0 0 0 1 0 1 1]
            [0 0 0 0 1 1 0 1]
            [0 0 0 0 1 1 1 0]
            [0 0 0 0 0 1 1 1]
        """
    def base_ring(self):
        """
        Return the base field of ``self`` as determined by
        ``self.e``.

        EXAMPLES::

            sage: sr = mq.SR(10, 2, 2, 4)
            sage: sr.base_ring().polynomial()
            a^4 + a + 1

        The Rijndael polynomial::

            sage: sr = mq.SR(10, 4, 4, 8)
            sage: sr.base_ring().polynomial()
            a^8 + a^4 + a^3 + a + 1
        """
    def __eq__(self, other):
        """
        Two generators are considered equal if they agree on all parameters
        passed to them during construction.

        EXAMPLES::

            sage: sr1 = mq.SR(2, 2, 2, 4)
            sage: sr1 == sr1
            True

            sage: sr2 = mq.SR(2, 2, 2, 4, gf2=True)
            sage: sr1 == sr2
            False
        """
    def __ne__(self, other):
        """
        Return whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: sr1 = mq.SR(2, 2, 2, 4)
            sage: sr1 != sr1
            False

            sage: sr2 = mq.SR(2, 2, 2, 4, gf2=True)
            sage: sr1 != sr2
            True
        """
    def sub_bytes(self, d):
        """
        Perform the non-linear transform on ``d``.

        INPUT:

        - ``d`` -- state array or something coercible to a state array

        EXAMPLES::

            sage: sr = mq.SR(2, 1, 2, 8, gf2=True)
            sage: k = sr.base_ring()
            sage: A = Matrix(k, 1, 2 , [k(1), k.gen()])
            sage: sr.sub_bytes(A)
            [  a^6 + a^5 + a^4 + a^3 + a^2 a^6 + a^5 + a^4 + a^2 + a + 1]
        """
    def sub_byte(self, b):
        """
        Perform ``SubByte`` on a single byte/halfbyte ``b``.

        A ``ZeroDivision`` exception is raised if an attempt is made
        to perform an inversion on the zero element. This can be
        disabled by passing ``allow_zero_inversion=True`` to the
        constructor. A zero inversion can result in an inconsistent
        equation system.

        INPUT:

        - ``b`` -- an element in ``self.base_ring()``

        EXAMPLES:

        The S-Box table for `\\GF{2^4}`::

            sage: sr = mq.SR(1, 1, 1, 4, allow_zero_inversions=True)
            sage: for e in sr.base_ring():
            ....:    print('% 20s % 20s'%(e, sr.sub_byte(e)))
                            0              a^2 + a
                            a              a^2 + 1
                          a^2                    a
                          a^3              a^3 + 1
                        a + 1                  a^2
                      a^2 + a          a^2 + a + 1
                    a^3 + a^2                a + 1
                  a^3 + a + 1            a^3 + a^2
                      a^2 + 1        a^3 + a^2 + a
                      a^3 + a    a^3 + a^2 + a + 1
                  a^2 + a + 1              a^3 + a
                a^3 + a^2 + a                    0
            a^3 + a^2 + a + 1                  a^3
                a^3 + a^2 + 1                    1
                      a^3 + 1        a^3 + a^2 + 1
                            1          a^3 + a + 1
        """
    def sbox_constant(self):
        """
        Return the S-Box constant which is added after `L(x^{-1})` was
        performed. That is ``0x63`` if ``e == 8`` or ``0x6`` if ``e ==
        4``.

        EXAMPLES::

            sage: sr = mq.SR(10, 1, 1, 8)
            sage: sr.sbox_constant()
            a^6 + a^5 + a + 1
        """
    def sbox(self, inversion_only: bool = False):
        """
        Return an S-Box object for this SR instance.

        INPUT:

        - ``inversion_only`` -- do not include the `\\GF{2}` affine map when
          computing the S-Box (default: ``False``)

        EXAMPLES::

            sage: sr = mq.SR(1,2,2,4, allow_zero_inversions=True)
            sage: S = sr.sbox(); S
            (6, 11, 5, 4, 2, 14, 7, 10, 9, 13, 15, 12, 3, 1, 0, 8)

            sage: sr.sub_byte(0)
            a^2 + a
            sage: sage_eval(str(sr.sub_byte(0)), {'a':2})
            6
            sage: S(0)
            6

            sage: sr.sub_byte(1)
            a^3 + a + 1
            sage: sage_eval(str(sr.sub_byte(1)), {'a':2})
            11
            sage: S(1)
            11

            sage: sr = mq.SR(1,2,2,8, allow_zero_inversions=True)
            sage: S = sr.sbox(); S
            (99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43,
            254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240,
            173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38,
            54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4,
            199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39,
            178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214,
            179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91,
            106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251,
            67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81,
            163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16,
            255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196,
            167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42,
            144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58,
            10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121,
            231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234,
            101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198,
            232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102,
            72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225,
            248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206,
            85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65,
            153, 45, 15, 176, 84, 187, 22)

            sage: sr.sub_byte(0)
            a^6 + a^5 + a + 1

            sage: sage_eval(str(sr.sub_byte(0)), {'a':2})
            99
            sage: S(0)
            99

            sage: sr.sub_byte(1)
            a^6 + a^5 + a^4 + a^3 + a^2

            sage: sage_eval(str(sr.sub_byte(1)), {'a':2})
            124

            sage: S(1)
            124

            sage: sr = mq.SR(1,2,2,4, allow_zero_inversions=True)
            sage: S = sr.sbox(inversion_only=True); S
            (0, 1, 9, 14, 13, 11, 7, 6, 15, 2, 12, 5, 10, 4, 3, 8)

            sage: S(0)
            0
            sage: S(1)
            1

            sage: S(sr.k.gen())
            a^3 + a + 1
        """
    def shift_rows(self, d):
        """
        Perform the ``ShiftRows`` operation on ``d``.

        INPUT:

        - ``d`` -- state array or something coercible to a state array

        EXAMPLES::

            sage: sr = mq.SR(10, 4, 4, 4)
            sage: E = sr.state_array() + 1; E
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

        ::

            sage: sr.shift_rows(E)
            [1 0 0 0]
            [1 0 0 0]
            [1 0 0 0]
            [1 0 0 0]
        """
    def mix_columns(self, d):
        """
        Perform the ``MixColumns`` operation on
        ``d``.

        INPUT:

        - ``d`` -- state array or something coercible to a state array

        EXAMPLES::

            sage: sr = mq.SR(10, 4, 4, 4)
            sage: E = sr.state_array() + 1; E
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]

        ::

            sage: sr.mix_columns(E)
            [    a a + 1     1     1]
            [    1     a a + 1     1]
            [    1     1     a a + 1]
            [a + 1     1     1     a]
        """
    def add_round_key(self, d, key):
        """
        Perform the ``AddRoundKey`` operation on
        ``d`` using ``key``.

        INPUT:

        - ``d`` -- state array or something coercible to a state array

        - ``key`` -- state array or something coercible to a state array

        EXAMPLES::

            sage: sr = mq.SR(10, 4, 4, 4)
            sage: D = sr.random_state_array()
            sage: K = sr.random_state_array()
            sage: sr.add_round_key(D, K) == K + D
            True
        """
    def state_array(self, d=None):
        """
        Convert the parameter to a state array.

        INPUT:

        - ``d`` -- a matrix, a list, or a tuple (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(2, 2, 2, 4)
            sage: k = sr.base_ring()
            sage: e1 = [k.from_integer(e) for e in range(2*2)]; e1
            [0, 1, a, a + 1]
            sage: e2 = sr.phi( Matrix(k, 2*2, 1, e1) )
            sage: sr.state_array(e1) # note the column major ordering
            [    0     a]
            [    1 a + 1]
            sage: sr.state_array(e2)
            [    0     a]
            [    1 a + 1]

        ::

            sage: sr.state_array()
            [0 0]
            [0 0]
        """
    def is_state_array(self, d):
        """
        Return ``True`` if ``d`` is a state array, i.e. has the correct
        dimensions and base field.

        EXAMPLES::

            sage: sr = mq.SR(2, 2, 4, 8)
            sage: k = sr.base_ring()
            sage: sr.is_state_array( matrix(k, 2, 4) )
            True

        ::

            sage: sr = mq.SR(2, 2, 4, 8)
            sage: k = sr.base_ring()
            sage: sr.is_state_array( matrix(k, 4, 4) )
            False
        """
    def random_state_array(self, *args, **kwds):
        """
        Return a random element in ``MatrixSpace(self.base_ring(),
        self.r, self.c)``.

        EXAMPLES::

            sage: sr = mq.SR(2, 2, 2, 4)
            sage: sr.random_state_array().parent()
            Full MatrixSpace of 2 by 2 dense matrices over Finite Field in a of size 2^4
        """
    def random_vector(self, *args, **kwds):
        """
        Return a random vector as it might appear in the algebraic
        expression of ``self``.

        EXAMPLES::

            sage: mq.SR(2, 2, 2, 4).random_vector().parent()
            Full MatrixSpace of 16 by 1 dense matrices over Finite Field in a of size 2^4

        .. NOTE::

           `\\phi` was already applied to the result.
        """
    def random_element(self, elem_type: str = 'vector', *args, **kwds):
        """
        Return a random element for ``self``.  Other arguments and keywords are
        passed to random_* methods.

        INPUT:

        - ``elem_type`` -- either 'vector' or 'state array' (default: ``'vector'``)

        EXAMPLES::

            sage: sr = mq.SR()
            sage: sr.random_element().parent()
            Full MatrixSpace of 4 by 1 dense matrices over Finite Field in a of size 2^4
            sage: sr.random_element('state_array').parent()
            Full MatrixSpace of 1 by 1 dense matrices over Finite Field in a of size 2^4

        Passes extra positional or keyword arguments through::

            sage: sr.random_element(density=0)
            [0]
            [0]
            [0]
            [0]
        """
    def key_schedule(self, kj, i):
        """
        Return `k_i` for a given `i` and `k_j`
        with `j = i-1`.

        EXAMPLES::

            sage: sr = mq.SR(10, 4, 4, 8, star=True, allow_zero_inversions=True)
            sage: ki = sr.state_array()
            sage: for i in range(10):
            ....:     ki = sr.key_schedule(ki, i+1)
            sage: print(sr.hex_str_matrix(ki))
            B4 3E 23 6F
            EF 92 E9 8F
            5B E2 51 18
            CB 11 CF 8E
        """
    def __call__(self, P, K):
        """
        Encrypts the plaintext `P` using the key `K`.

        Both must be given as state arrays or coercible to state arrays.

        INPUT:

        - ``P`` -- plaintext as state array or something coercible to a
          qstate array

        - ``K`` -- key as state array or something coercible to a state
          array

        TESTS:

        The official AES test vectors::

            sage: sr = mq.SR(10, 4, 4, 8, star=True, allow_zero_inversions=True)
            sage: k = sr.base_ring()
            sage: plaintext = sr.state_array([k.from_integer(e) for e in range(16)])
            sage: key = sr.state_array([k.from_integer(e) for e in range(16)])
            sage: print(sr.hex_str_matrix( sr(plaintext, key) ))
            0A 41 F1 C6
            94 6E C3 53
            0B F0 94 EA
            B5 45 58 5A

        Brian Gladman's development vectors (dev_vec.txt)::

            sage: sr = mq.SR(10, 4, 4, 8, star=True, allow_zero_inversions=True, aes_mode=True)
            sage: k = sr.base_ring()
            sage: plain = '3243f6a8885a308d313198a2e0370734'
            sage: key = '2b7e151628aed2a6abf7158809cf4f3c'
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(2)
            sage: cipher = sr(plain, key)
            R[01].start   193DE3BEA0F4E22B9AC68D2AE9F84808
            R[01].s_box   D42711AEE0BF98F1B8B45DE51E415230
            R[01].s_row   D4BF5D30E0B452AEB84111F11E2798E5
            R[01].m_col   046681E5E0CB199A48F8D37A2806264C
            R[01].k_sch   A0FAFE1788542CB123A339392A6C7605
            R[02].start   A49C7FF2689F352B6B5BEA43026A5049
            R[02].s_box   49DED28945DB96F17F39871A7702533B
            R[02].s_row   49DB873B453953897F02D2F177DE961A
            R[02].m_col   584DCAF11B4B5AACDBE7CAA81B6BB0E5
            R[02].k_sch   F2C295F27A96B9435935807A7359F67F
            R[03].start   AA8F5F0361DDE3EF82D24AD26832469A
            R[03].s_box   AC73CF7BEFC111DF13B5D6B545235AB8
            R[03].s_row   ACC1D6B8EFB55A7B1323CFDF457311B5
            R[03].m_col   75EC0993200B633353C0CF7CBB25D0DC
            R[03].k_sch   3D80477D4716FE3E1E237E446D7A883B
            R[04].start   486C4EEE671D9D0D4DE3B138D65F58E7
            R[04].s_box   52502F2885A45ED7E311C807F6CF6A94
            R[04].s_row   52A4C89485116A28E3CF2FD7F6505E07
            R[04].m_col   0FD6DAA9603138BF6FC0106B5EB31301
            R[04].k_sch   EF44A541A8525B7FB671253BDB0BAD00
            R[05].start   E0927FE8C86363C0D9B1355085B8BE01
            R[05].s_box   E14FD29BE8FBFBBA35C89653976CAE7C
            R[05].s_row   E1FB967CE8C8AE9B356CD2BA974FFB53
            R[05].m_col   25D1A9ADBD11D168B63A338E4C4CC0B0
            R[05].k_sch   D4D1C6F87C839D87CAF2B8BC11F915BC
            R[06].start   F1006F55C1924CEF7CC88B325DB5D50C
            R[06].s_box   A163A8FC784F29DF10E83D234CD503FE
            R[06].s_row   A14F3DFE78E803FC10D5A8DF4C632923
            R[06].m_col   4B868D6D2C4A8980339DF4E837D218D8
            R[06].k_sch   6D88A37A110B3EFDDBF98641CA0093FD
            R[07].start   260E2E173D41B77DE86472A9FDD28B25
            R[07].s_box   F7AB31F02783A9FF9B4340D354B53D3F
            R[07].s_row   F783403F27433DF09BB531FF54ABA9D3
            R[07].m_col   1415B5BF461615EC274656D7342AD843
            R[07].k_sch   4E54F70E5F5FC9F384A64FB24EA6DC4F
            R[08].start   5A4142B11949DC1FA3E019657A8C040C
            R[08].s_box   BE832CC8D43B86C00AE1D44DDA64F2FE
            R[08].s_row   BE3BD4FED4E1F2C80A642CC0DA83864D
            R[08].m_col   00512FD1B1C889FF54766DCDFA1B99EA
            R[08].k_sch   EAD27321B58DBAD2312BF5607F8D292F
            R[09].start   EA835CF00445332D655D98AD8596B0C5
            R[09].s_box   87EC4A8CF26EC3D84D4C46959790E7A6
            R[09].s_row   876E46A6F24CE78C4D904AD897ECC395
            R[09].m_col   473794ED40D4E4A5A3703AA64C9F42BC
            R[09].k_sch   AC7766F319FADC2128D12941575C006E
            R[10].s_box   E9098972CB31075F3D327D94AF2E2CB5
            R[10].s_row   E9317DB5CB322C723D2E895FAF090794
            R[10].k_sch   D014F9A8C9EE2589E13F0CC8B6630CA6
            R[10].output  3925841D02DC09FBDC118597196A0B32
            sage: set_verbose(0)
        """
    def hex_str(self, M, typ: str = 'matrix'):
        """
        Return a hex string for the provided AES state array/matrix.

        INPUT:

        - ``M`` -- state array

        - ``typ`` -- controls what to return, either 'matrix'
          or 'vector' (default: ``'matrix'``)

        EXAMPLES::

            sage: sr = mq.SR(2, 2, 2, 4)
            sage: k = sr.base_ring()
            sage: A = matrix(k, 2, 2, [1, k.gen(), 0, k.gen()^2])
            sage: sr.hex_str(A)
            ' 1 2 \\n 0 4 \\n'

        ::

            sage: sr.hex_str(A, typ='vector')
            '1024'
        """
    def hex_str_matrix(self, M):
        """
        Return a two-dimensional AES-like representation of the matrix M.

        That is, show the finite field elements as hex strings.

        INPUT:

        - ``M`` -- an AES state array

        EXAMPLES::

            sage: sr = mq.SR(2, 2, 2, 4)
            sage: k = sr.base_ring()
            sage: A = matrix(k, 2, 2, [1, k.gen(), 0, k.gen()^2])
            sage: sr.hex_str_matrix(A)
            ' 1 2 \\n 0 4 \\n'
        """
    def hex_str_vector(self, M):
        """
        Return a one-dimensional AES-like representation of the matrix M.

        That is, show the finite field elements as hex strings.

        INPUT:

        - ``M`` -- an AES state array

        EXAMPLES::

            sage: sr = mq.SR(2, 2, 2, 4)
            sage: k = sr.base_ring()
            sage: A = matrix(k, 2, 2, [1, k.gen(), 0, k.gen()^2])
            sage: sr.hex_str_vector(A)
            '1024'
        """
    def varformatstr(self, name, n=None, rc=None, e=None):
        """
        Return a format string which is understood by print et al.

        If a numerical value is omitted, the default value of ``self``
        is used.  The numerical values (``n``, ``rc``, ``e``) are used
        to determine the width of the respective fields in the format
        string.

        INPUT:

        - ``name`` -- name of the variable
        - ``n`` -- number of rounds (default: ``None``)
        - ``rc`` -- number of rows \\* number of cols (default: ``None``)
        - ``e`` -- exponent of base field (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(1, 2, 2, 4)
            sage: sr.varformatstr('x')
            'x%01d%01d%01d'
            sage: sr.varformatstr('x', n=1000)
            'x%03d%03d%03d'
        """
    def varstr(self, name, nr, rc, e):
        """
        Return a string representing a variable for the small scale
        AES subject to the given constraints.

        INPUT:

        - ``name`` -- variable name
        - ``nr`` -- number of round to create variable strings for
        - ``rc`` -- row*column index in state array
        - ``e`` -- exponent of base field

        EXAMPLES::

            sage: sr = mq.SR(10, 1, 2, 4)
            sage: sr.varstr('x', 2, 1, 1)
            'x211'
        """
    def varstrs(self, name, nr, rc=None, e=None):
        """
        Return a list of strings representing variables in ``self``.

        INPUT:

        - ``name`` -- variable name
        - ``nr`` -- number of round to create variable strings for
        - ``rc`` -- number of rows * number of columns in the state array (default: ``None``)
        - ``e`` -- exponent of base field (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(10, 1, 2, 4)
            sage: sr.varstrs('x', 2)
            ('x200', 'x201', 'x202', 'x203', 'x210', 'x211', 'x212', 'x213')
        """
    def vars(self, name, nr, rc=None, e=None):
        """
        Return a list of variables in ``self``.

        INPUT:

        - ``name`` -- variable name
        - ``nr`` -- number of round to create variable strings for
        - ``rc`` -- number of rounds * number of columns in the state array (default: ``None``)
        - ``e`` -- exponent of base field (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(10, 1, 2, 4)
            sage: sr.vars('x', 2)
            (x200, x201, x202, x203, x210, x211, x212, x213)
        """
    def variable_dict(self):
        """
        Return a dictionary to access variables in ``self.R`` by their
        names.

        EXAMPLES::

            sage: sr = mq.SR(1,1,1,4)
            sage: sr.variable_dict()
            {'k000': k000,
             'k001': k001,
             'k002': k002,
             'k003': k003,
             'k100': k100,
             'k101': k101,
             'k102': k102,
             'k103': k103,
             's000': s000,
             's001': s001,
             's002': s002,
             's003': s003,
             'w100': w100,
             'w101': w101,
             'w102': w102,
             'w103': w103,
             'x100': x100,
             'x101': x101,
             'x102': x102,
             'x103': x103}

            sage: sr = mq.SR(1,1,1,4,gf2=True)
            sage: sr.variable_dict()                                                    # needs sage.rings.polynomial.pbori
            {'k000': k000,
             'k001': k001,
             'k002': k002,
             'k003': k003,
             'k100': k100,
             'k101': k101,
             'k102': k102,
             'k103': k103,
             's000': s000,
             's001': s001,
             's002': s002,
             's003': s003,
             'w100': w100,
             'w101': w101,
             'w102': w102,
             'w103': w103,
             'x100': x100,
             'x101': x101,
             'x102': x102,
             'x103': x103}
        """
    def block_order(self):
        """
        Return a block order for ``self`` where each round is a block.

        EXAMPLES::

            sage: sr = mq.SR(2, 1, 1, 4)
            sage: sr.block_order()
            Block term order with blocks:
            (Degree lexicographic term order of length 16,
             Degree lexicographic term order of length 16,
             Degree lexicographic term order of length 4)

        ::

            sage: P = sr.ring(order='block')
            sage: print(P.repr_long())
            Polynomial Ring
              Base Ring : Finite Field in a of size 2^4
                   Size : 36 Variables
               Block  0 : Ordering : deglex
                          Names    : k200, k201, k202, k203, x200, x201, x202, x203, w200, w201, w202, w203, s100, s101, s102, s103
               Block  1 : Ordering : deglex
                          Names    : k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003
               Block  2 : Ordering : deglex
                          Names    : k000, k001, k002, k003
        """
    def ring(self, order=None, reverse_variables=None):
        """
        Construct a ring as a base ring for the polynomial system.

        By default, variables are ordered in the reverse of their natural
        ordering, i.e. the reverse of as they appear.

        INPUT:

        - ``order`` -- a monomial ordering (default: ``None``)
        - ``reverse_variables`` -- reverse rounds of variables (default: ``True``)

        The variable assignment is as follows:

        - `k_{i,j,l}` -- subkey round `i` word `j` conjugate/bit `l`
        - `s_{i,j,l}` -- subkey inverse round `i` word `j` conjugate/bit `l`
        - `w_{i,j,l}` -- inversion input round `i` word `j` conjugate/bit `l`
        - `x_{i,j,l}` -- inversion output round `i` word `j` conjugate/bit `l`


        Note that the variables are ordered in column major ordering
        in the state array and that the bits are ordered in little
        endian ordering.

        For example, if `x_{0,1,0}` is a variable over `\\GF{2}` for
        `r=2` and `c=2` then refers to the *most* significant bit of
        the entry in the position (1,0) in the state array matrix.

        EXAMPLES::

            sage: sr = mq.SR(2, 1, 1, 4)
            sage: P = sr.ring(order='block')
            sage: print(P.repr_long())
            Polynomial Ring
              Base Ring : Finite Field in a of size 2^4
                   Size : 36 Variables
               Block  0 : Ordering : deglex
                          Names    : k200, k201, k202, k203, x200, x201, x202, x203, w200, w201, w202, w203, s100, s101, s102, s103
               Block  1 : Ordering : deglex
                          Names    : k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003
               Block  2 : Ordering : deglex
                          Names    : k000, k001, k002, k003
        """
    def round_polynomials(self, i, plaintext=None, ciphertext=None):
        """
        Return list of polynomials for a given round `i`.

        If ``i == 0`` a plaintext must be provided, if ``i == n`` a
        ciphertext must be provided.

        INPUT:

        - ``i`` -- round number

        - ``plaintext`` -- plaintext (optional, mandatory in first round)

        - ``ciphertext`` -- ciphertext (optional, mandatory in last round)

        OUTPUT: tuple

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4)
            sage: k = sr.base_ring()
            sage: p = [k.random_element() for _ in range(sr.r*sr.c)]
            sage: sr.round_polynomials(0, plaintext=p)
            (w100 + k000..., w101 + k001..., w102 + k002..., w103 + k003...)
        """
    def key_schedule_polynomials(self, i):
        """
        Return polynomials for the `i`-th round of the key
        schedule.

        INPUT:

        - ``i`` -- round (`0 \\leq i \\leq n`)

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=False)

        The `0`-th subkey is the user provided key, so only conjugacy
        relations or field polynomials are added.::

            sage: sr.key_schedule_polynomials(0)
            (k000^2 + k000, k001^2 + k001, k002^2 + k002, k003^2 + k003)

        The 1st subkey is derived from the user provided key according to
        the key schedule which is non-linear.::

            sage: sr.key_schedule_polynomials(1)
            (k100 + s000 + s002 + s003,
             k101 + s000 + s001 + s003 + 1,
             k102 + s000 + s001 + s002 + 1,
             k103 + s001 + s002 + s003 + 1,
             k100^2 + k100, k101^2 + k101, k102^2 + k102, k103^2 + k103,
             s000^2 + s000, s001^2 + s001, s002^2 + s002, s003^2 + s003,
             s000*k000 + s000*k003 + s001*k002 + s002*k001 + s003*k000,
             s000*k000 + s000*k001 + s001*k000 + s001*k003 + s002*k002 + s003*k001,
             s000*k001 + s000*k002 + s001*k000 + s001*k001 + s002*k000 + s002*k003 + s003*k002,
             s000*k000 + s000*k001 + s000*k003 + s001*k001 + s002*k000 + s002*k002 + s003*k000 + k000,
             s000*k002 + s001*k000 + s001*k001 + s001*k003 + s002*k001 + s003*k000 + s003*k002 + k001,
             s000*k000 + s000*k001 + s000*k002 + s001*k002 + s002*k000 + s002*k001 + s002*k003 + s003*k001 + k002,
             s000*k001 + s001*k000 + s001*k002 + s002*k000 + s003*k001 + s003*k003 + k003,
             s000*k000 + s000*k002 + s000*k003 + s001*k000 + s001*k001 + s002*k002 + s003*k000 + s000,
             s000*k001 + s000*k003 + s001*k001 + s001*k002 + s002*k000 + s002*k003 + s003*k001 + s001,
             s000*k000 + s000*k002 + s001*k000 + s001*k002 + s001*k003 + s002*k000 + s002*k001 + s003*k002 + s002,
             s000*k001 + s000*k002 + s001*k000 + s001*k003 + s002*k001 + s003*k003 + s003,
             s000*k002 + s001*k001 + s002*k000 + s003*k003 + 1)
        """
    def polynomial_system(self, P=None, K=None, C=None):
        '''
        Return a polynomial system for this small scale AES variant for a
        given plaintext-key pair.

        If neither ``P``, ``K`` nor ``C`` are provided, a random pair
        (``P``, ``K``) will be generated. If ``P`` and ``C`` are
        provided no ``K`` needs to be provided.

        INPUT:

        - ``P`` -- vector, list, or tuple (default: ``None``)
        - ``K`` -- vector, list, or tuple (default: ``None``)
        - ``C`` -- vector, list, or tuple (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)
            sage: P = sr.vector([0, 0, 1, 0])
            sage: K = sr.vector([1, 0, 0, 1])
            sage: F, s = sr.polynomial_system(P, K)                                     # needs sage.rings.polynomial.pbori

        This returns a polynomial system::

            sage: F                                                                     # needs sage.rings.polynomial.pbori
            Polynomial Sequence with 36 Polynomials in 20 Variables

        and a solution::

            sage: s  # random -- maybe we need a better doctest here?                   # needs sage.rings.polynomial.pbori
            {k000: 1, k001: 0, k003: 1, k002: 0}

        This solution is not the only solution that we can learn from the
        Groebner basis of the system.

        ::

            sage: F.groebner_basis()[-3:]                                               # needs sage.rings.polynomial.pbori
            [k000 + 1, k001, k003 + 1]

        In particular we have two solutions::

            sage: len(F.ideal().variety())                                              # needs sage.rings.polynomial.pbori
            2

        In the following example we provide ``C`` explicitly::

           sage: C = sr(P,K)
           sage: F,s = sr.polynomial_system(P=P, C=C)                                   # needs sage.rings.polynomial.pbori
           sage: F                                                                      # needs sage.rings.polynomial.pbori
           Polynomial Sequence with 36 Polynomials in 20 Variables

        Alternatively, we can use symbols for the ``P`` and
        ``C``. First, we have to create a polynomial ring::

            sage: # needs sage.rings.polynomial.pbori
            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)
            sage: R = sr.R
            sage: vn = sr.varstrs("P",0,1,4) + R.variable_names() + sr.varstrs("C",0,1,4)
            sage: R = BooleanPolynomialRing(len(vn),vn)
            sage: sr.R = R


        Now, we can construct the purely symbolic equation system::

            sage: # needs sage.rings.polynomial.pbori
            sage: C = sr.vars("C",0); C
            (C000, C001, C002, C003)
            sage: P = sr.vars("P",0)
            sage: F,s = sr.polynomial_system(P=P,C=C)
            sage: F
            Polynomial Sequence with 36 Polynomials in 28 Variables
            sage: F.part(0)
            (P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003)
            sage: F.part(-2)
            (k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, ...)

        We show that the (returned) key is a solution to the returned system::

            sage: sr = mq.SR(3,4,4,8, star=True, gf2=True, polybori=True)
            sage: while True:  # workaround (see :issue:`31891`)                         # needs sage.rings.polynomial.pbori
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: F.subs(s).groebner_basis()    # long time                             # needs sage.rings.polynomial.pbori
            Polynomial Sequence with 1248 Polynomials in 1248 Variables
        '''

class SR_gf2n(SR_generic):
    """
    Small Scale Variants of the AES polynomial system constructor over
    `\\GF{2^n}`.
    """
    def vector(self, d=None):
        """
        Construct a vector suitable for the algebraic representation of
        SR, i.e. BES.

        INPUT:

        - ``d`` -- values for vector, must be understood by ``self.phi``
          (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR()
            sage: sr
            SR(1,1,1,4)
            sage: k = sr.base_ring()
            sage: A = Matrix(k, 1, 1, [k.gen()])
            sage: sr.vector(A)
            [      a]
            [    a^2]
            [  a + 1]
            [a^2 + 1]
        """
    def is_vector(self, d):
        """
        Return ``True`` if ``d`` can be used as a vector for ``self``.

        EXAMPLES::

            sage: sr = mq.SR()
            sage: sr
            SR(1,1,1,4)
            sage: k = sr.base_ring()
            sage: A = Matrix(k, 1, 1, [k.gen()])
            sage: B = sr.vector(A)
            sage: sr.is_vector(A)
            False
            sage: sr.is_vector(B)
            True
        """
    def phi(self, l):
        """
        The operation `\\phi` from [MR2002]_.

        Projects state arrays to their algebraic representation.

        INPUT:

        - ``l`` -- element to perform `\\phi` on

        EXAMPLES::

            sage: sr = mq.SR(2, 1, 2, 4)
            sage: k = sr.base_ring()
            sage: A = matrix(k, 1, 2, [k.gen(), 0] )
            sage: sr.phi(A)
            [      a       0]
            [    a^2       0]
            [  a + 1       0]
            [a^2 + 1       0]
        """
    def antiphi(self, l):
        """
        The operation `\\phi^{-1}` from [MR2002]_ or the inverse of ``self.phi``.

        INPUT:

        - ``l`` -- a vector in the sense of :meth:`is_vector`

        EXAMPLES::

            sage: sr = mq.SR()
            sage: A = sr.random_state_array()
            sage: sr.antiphi(sr.phi(A)) == A
            True
        """
    def shift_rows_matrix(self):
        """
        Return the ``ShiftRows`` matrix.

        EXAMPLES::

            sage: sr = mq.SR(1, 2, 2, 4)
            sage: s = sr.random_state_array()
            sage: r1 = sr.shift_rows(s)
            sage: r2 = sr.state_array( sr.shift_rows_matrix() * sr.vector(s) )
            sage: r1 == r2
            True
        """
    def lin_matrix(self, length=None):
        """
        Return the ``Lin`` matrix.

        If no ``length`` is provided, the standard state space size is
        used. The key schedule calls this method with an explicit
        length argument because only ``self.r`` S-Box applications are
        performed in the key schedule.

        INPUT:

        - ``length`` -- length of state space (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4)
            sage: sr.lin_matrix()
            [          a^2 + 1                 1         a^3 + a^2           a^2 + 1]
            [                a                 a                 1 a^3 + a^2 + a + 1]
            [          a^3 + a               a^2               a^2                 1]
            [                1               a^3             a + 1             a + 1]
        """
    def mix_columns_matrix(self):
        """
        Return the ``MixColumns`` matrix.

        EXAMPLES::

            sage: sr = mq.SR(1, 2, 2, 4)
            sage: s = sr.random_state_array()
            sage: r1 = sr.mix_columns(s)
            sage: r2 = sr.state_array(sr.mix_columns_matrix() * sr.vector(s))
            sage: r1 == r2
            True
        """
    def inversion_polynomials(self, xi, wi, length):
        """
        Return polynomials to represent the inversion in the AES S-Box.

        INPUT:

        - ``xi`` -- output variables

        - ``wi`` -- input variables

        - ``length`` -- length of both lists

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 8)
            sage: R = sr.ring()
            sage: xi = Matrix(R, 8, 1, sr.vars('x', 1))
            sage: wi = Matrix(R, 8, 1, sr.vars('w', 1))
            sage: sr.inversion_polynomials(xi, wi, 8)
            [x100*w100 + 1,
            x101*w101 + 1,
            x102*w102 + 1,
            x103*w103 + 1,
            x104*w104 + 1,
            x105*w105 + 1,
            x106*w106 + 1,
            x107*w107 + 1]
        """
    def field_polynomials(self, name, i, l=None):
        """
        Return list of conjugacy polynomials for a given round ``i``
        and name ``name``.

        INPUT:

        - ``name`` -- variable name
        - ``i`` -- round number
        - ``l`` -- r\\*c (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(3, 1, 1, 8)
            sage: sr.field_polynomials('x', 2)
            [x200^2 + x201,
            x201^2 + x202,
            x202^2 + x203,
            x203^2 + x204,
            x204^2 + x205,
            x205^2 + x206,
            x206^2 + x207,
            x207^2 + x200]
        """

class SR_gf2(SR_generic):
    def __init__(self, n: int = 1, r: int = 1, c: int = 1, e: int = 4, star: bool = False, **kwargs) -> None:
        """
        Small Scale Variants of the AES polynomial system constructor over
        `\\GF{2}`. See help for SR.

        EXAMPLES::

            sage: sr = mq.SR(gf2=True)
            sage: sr
            SR(1,1,1,4)
        """
    def vector(self, d=None):
        """
        Construct a vector suitable for the algebraic representation of
        SR.

        INPUT:

        - ``d`` -- values for vector (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(gf2=True)
            sage: sr
            SR(1,1,1,4)
            sage: k = sr.base_ring()
            sage: A = Matrix(k, 1, 1, [k.gen()])
            sage: sr.vector(A)
            [0]
            [0]
            [1]
            [0]
        """
    def is_vector(self, d):
        """
        Return ``True`` if the given matrix satisfies the conditions
        for a vector as it appears in the algebraic expression of
        ``self``.

        INPUT:

        - ``d`` -- matrix

        EXAMPLES::

            sage: sr = mq.SR(gf2=True)
            sage: sr
            SR(1,1,1,4)
            sage: k = sr.base_ring()
            sage: A = Matrix(k, 1, 1, [k.gen()])
            sage: B = sr.vector(A)
            sage: sr.is_vector(A)
            False
            sage: sr.is_vector(B)
            True
        """
    def phi(self, l, diffusion_matrix: bool = False):
        """
        The operation `\\phi` from [MR2002]_.

        Given a list/matrix of elements in `\\GF{2^e}`, return a
        matching list/matrix of elements in `\\GF{2}`.

        INPUT:

        - ``l`` -- element to perform `\\phi` on
        - ``diffusion_matrix`` -- if ``True``, the given matrix ``l`` is
          transformed to a matrix which performs the same operation
          over `\\GF{2}` as ``l`` over `\\GF{2^n}` (default: ``False``).

        EXAMPLES::

            sage: sr = mq.SR(2, 1, 2, 4, gf2=True)
            sage: k = sr.base_ring()
            sage: A = matrix(k, 1, 2, [k.gen(), 0] )
            sage: sr.phi(A)                                                             # needs sage.libs.gap
            [0 0]
            [0 0]
            [1 0]
            [0 0]
        """
    def antiphi(self, l):
        """
        The operation `\\phi^{-1}` from [MR2002]_ or the inverse of ``self.phi``.

        INPUT:

        - ``l`` -- a vector in the sense of ``self.is_vector``

        EXAMPLES::

            sage: sr = mq.SR(gf2=True)
            sage: A = sr.random_state_array()
            sage: sr.antiphi(sr.phi(A)) == A                                            # needs sage.libs.gap
            True
        """
    def shift_rows_matrix(self):
        """
        Return the ``ShiftRows`` matrix.

        EXAMPLES::

            sage: sr = mq.SR(1, 2, 2, 4, gf2=True)
            sage: s = sr.random_state_array()
            sage: r1 = sr.shift_rows(s)
            sage: r2 = sr.state_array( sr.shift_rows_matrix() * sr.vector(s) )
            sage: r1 == r2
            True
        """
    def mix_columns_matrix(self):
        """
        Return the ``MixColumns`` matrix.

        EXAMPLES::

            sage: sr = mq.SR(1, 2, 2, 4, gf2=True)
            sage: s = sr.random_state_array()
            sage: r1 = sr.mix_columns(s)
            sage: r2 = sr.state_array(sr.mix_columns_matrix() * sr.vector(s))
            sage: r1 == r2
            True
        """
    def lin_matrix(self, length=None):
        """
        Return the ``Lin`` matrix.

        If no ``length`` is provided, the standard state space size is
        used. The key schedule calls this method with an explicit
        length argument because only ``self.r`` S-Box applications are
        performed in the key schedule.

        INPUT:

        - ``length`` -- length of state space (default: ``None``)

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True)
            sage: sr.lin_matrix()
            [1 0 1 1]
            [1 1 0 1]
            [1 1 1 0]
            [0 1 1 1]
        """
    def inversion_polynomials_single_sbox(self, x=None, w=None, biaffine_only=None, correct_only=None):
        """
        Return inversion polynomials of a single S-Box.

        INPUT:

        - ``xi`` -- output variables
        - ``wi`` -- input variables
        - ``length`` -- length of both lists

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 8, gf2=True)
            sage: len(sr.inversion_polynomials_single_sbox())
            24
            sage: len(sr.inversion_polynomials_single_sbox(correct_only=True))
            23
            sage: len(sr.inversion_polynomials_single_sbox(biaffine_only=False))
            40
            sage: len(sr.inversion_polynomials_single_sbox(biaffine_only=False, correct_only=True))
            39


            sage: sr = mq.SR(1, 1, 1, 8, gf2=True)
            sage: l0 = sr.inversion_polynomials_single_sbox(); len(l0)
            24
            sage: l1 = sr.inversion_polynomials_single_sbox(correct_only=True); len(l1)
            23
            sage: l2 = sr.inversion_polynomials_single_sbox(biaffine_only=False); len(l2)
            40
            sage: l3 = sr.inversion_polynomials_single_sbox(biaffine_only=False, correct_only=True); len(l3)
            39

            sage: set(l0) == set(sr._inversion_polynomials_single_sbox())
            True
            sage: set(l1) == set(sr._inversion_polynomials_single_sbox(correct_only=True))
            True
            sage: set(l2) == set(sr._inversion_polynomials_single_sbox(biaffine_only=False))
            True
            sage: set(l3) == set(sr._inversion_polynomials_single_sbox(biaffine_only=False, correct_only=True))
            True

            sage: sr = mq.SR(1, 1, 1, 4, gf2=True)
            sage: l0 = sr.inversion_polynomials_single_sbox(); len(l0)
            12
            sage: l1 = sr.inversion_polynomials_single_sbox(correct_only=True); len(l1)
            11
            sage: l2 = sr.inversion_polynomials_single_sbox(biaffine_only=False); len(l2)
            20
            sage: l3 = sr.inversion_polynomials_single_sbox(biaffine_only=False, correct_only=True); len(l3)
            19

            sage: set(l0) == set(sr._inversion_polynomials_single_sbox())
            True
            sage: set(l1) == set(sr._inversion_polynomials_single_sbox(correct_only=True))
            True
            sage: set(l2) == set(sr._inversion_polynomials_single_sbox(biaffine_only=False))
            True
            sage: set(l3) == set(sr._inversion_polynomials_single_sbox(biaffine_only=False, correct_only=True))
            True
        """
    def inversion_polynomials(self, xi, wi, length):
        """
        Return polynomials to represent the inversion in the AES S-Box.

        INPUT:

        - ``xi`` -- output variables

        - ``wi`` -- input variables

        - ``length`` -- length of both lists

        EXAMPLES::

            sage: sr = mq.SR(1, 1, 1, 8, gf2=True)
            sage: xi = sr.vars('x', 1)                                                  # needs sage.rings.polynomial.pbori
            sage: wi = sr.vars('w', 1)                                                  # needs sage.rings.polynomial.pbori
            sage: sr.inversion_polynomials(xi, wi, len(xi))[:3]                         # needs sage.rings.polynomial.pbori
            [x100*w100 + x100*w102 + x100*w103 + x100*w107 + x101*w101 + x101*w102 + x101*w106 + x102*w100 + x102*w101 + x102*w105 + x103*w100 + x103*w104 + x104*w103 + x105*w102 + x106*w101 + x107*w100,
             x100*w101 + x100*w103 + x100*w104 + x101*w100 + x101*w102 + x101*w103 + x101*w107 + x102*w101 + x102*w102 + x102*w106 + x103*w100 + x103*w101 + x103*w105 + x104*w100 + x104*w104 + x105*w103 + x106*w102 + x107*w101,
             x100*w102 + x100*w104 + x100*w105 + x101*w101 + x101*w103 + x101*w104 + x102*w100 + x102*w102 + x102*w103 + x102*w107 + x103*w101 + x103*w102 + x103*w106 + x104*w100 + x104*w101 + x104*w105 + x105*w100 + x105*w104 + x106*w103 + x107*w102]
        """
    def field_polynomials(self, name, i, l=None):
        """
        Return list of field polynomials for a given round ``i`` and
        name ``name``.

        INPUT:

        - ``name`` -- variable name
        - ``i`` -- round number
        - ``l`` -- length of variable list (default: ``None`` = r\\*c)

        EXAMPLES::

            sage: sr = mq.SR(3, 1, 1, 8, gf2=True, polybori=False)
            sage: sr.field_polynomials('x', 2)
            [x200^2 + x200, x201^2 + x201,
             x202^2 + x202, x203^2 + x203,
             x204^2 + x204, x205^2 + x205,
             x206^2 + x206, x207^2 + x207]

        ::

            sage: sr = mq.SR(3, 1, 1, 8, gf2=True, polybori=True)
            sage: sr.field_polynomials('x', 2)
            []
        """

class SR_gf2_2(SR_gf2):
    """
    This is an example how to customize the SR constructor.

    In this example, we replace the S-Box inversion polynomials by the
    polynomials generated by the S-Box class.
    """
    def inversion_polynomials_single_sbox(self, x=None, w=None, biaffine_only=None, correct_only=None, groebner: bool = False):
        """
        Return inversion polynomials of a single S-Box.

        INPUT:

        - ``x`` -- output variables (default: ``None``)
        - ``w`` -- input variables  (default: ``None``)
        - ``biaffine_only`` -- ignored (always ``False``)
        - ``correct_only`` -- ignored (always ``True``)
        - ``groebner`` -- precompute the Groebner basis for this S-Box (default: ``False``)

        EXAMPLES::

            sage: from sage.crypto.mq.sr import SR_gf2_2
            sage: e = 4
            sage: sr = SR_gf2_2(1, 1, 1, e)
            sage: P = PolynomialRing(GF(2),['x%d'%i for i in range(e)] + ['w%d'%i for i in range(e)],order='lex')
            sage: X,W = P.gens()[:e],P.gens()[e:]
            sage: sr.inversion_polynomials_single_sbox(X, W, groebner=True)             # needs sage.libs.singular
            [x0 + w0*w1*w2 + w0*w1 + w0*w2 + w0*w3 + w0 + w1 + w2,
             x1 + w0*w1*w3 + w0*w3 + w0 + w1*w3 + w1 + w2*w3,
             x2 + w0*w2*w3 + w0*w2 + w0 + w1*w2 + w1*w3 + w2*w3,
             x3 + w0*w1*w2 + w0 + w1*w2*w3 + w1*w2 + w1*w3 + w1 + w2 + w3]

            sage: from sage.crypto.mq.sr import SR_gf2_2
            sage: e = 4
            sage: sr = SR_gf2_2(1, 1, 1, e)
            sage: sr.inversion_polynomials_single_sbox()                                # needs sage.libs.singular
            [w3*w1 + w3*w0 + w3*x2 + w3*x1 + w3 + w2*w1 + w1 + x3 + x2 + x1,
             w3*w2 + w3*w1 + w3*x3 + w2 + w1 + x3,
             w3*w2 + w3*w1 + w3*x2 + w3 + w2*x3 + x2 + x1,
             w3*w2 + w3*w1 + w3*x3 + w3*x2 + w3*x1 + w3 + w2*x2 + w0 + x3 + x2 + x1 + x0,
             w3*w2 + w3*w1 + w3*x1 + w3*x0 + w2*x1 + w0 + x3 + x0,
             w3*w2 + w3*w1 + w3*w0 + w3*x2 + w3*x1 + w2*w0 + w2*x0 + w0 + x3 + x2 + x1 + x0,
             w3*w2 + w3*x1 + w3 + w2*w0 + w1*w0 + w1 + x3 + x2,
             w3*w2 + w3*w1 + w3*x1 + w1*x3 + x3 + x2 + x1,
             w3*x3 + w3*x2 + w3*x0 + w3 + w1*x2 + w1 + w0 + x2 + x0,
             w3*w2 + w3*w1 + w3*x2 + w3*x1 + w1*x1 + w1 + w0 + x2 + x0,
             w3*w2 + w3*w1 + w3*w0 + w3*x3 + w3*x1 + w2*w0 + w1*x0 + x3 + x2,
             w3*w2 + w3*w1 + w3*x2 + w3*x1 + w3*x0 + w3 + w1 + w0*x3 + x3 + x2,
             w3*w2 + w3*w1 + w3*w0 + w3*x3 + w3 + w2*w0 + w1 + w0*x2 + x3 + x2,
             w3*w0 + w3*x2 + w2*w0 + w0*x1 + w0 + x3 + x1 + x0,
             w3*w0 + w3*x3 + w3*x0 + w2*w0 + w1 + w0*x0 + w0 + x3 + x2,
             w3*w2 + w3 + w1 + x3*x2 + x3 + x1,
             w3*w2 + w3*x3 + w1 + x3*x1 + x3 + x2,
             w3*w2 + w3*w0 + w3*x3 + w3*x2 + w3*x1 + w0 + x3*x0 + x1 + x0,
             w3*w2 + w3*w1 + w3*w0 + w3*x3 + w1 + w0 + x2*x1 + x2 + x0,
             w3*w2 + w2*w0 + w1 + x3 + x2*x0,
             w3*x3 + w3*x1 + w2*w0 + w1 + x3 + x2 + x1*x0 + x1]

        TESTS:

        Note that ``biaffine_only`` and ``correct_only`` are always
        ignored. The former is always false while the second is always
        true. They are only accepted for compatibility with the base
        class.

            sage: from sage.crypto.mq.sr import SR_gf2_2
            sage: e = 4
            sage: sr = SR_gf2_2(1, 1, 1, e)
            sage: l = sr.inversion_polynomials_single_sbox()                            # needs sage.libs.singular
            sage: l == sr.inversion_polynomials_single_sbox(biaffine_only=True, correct_only=False)                     # needs sage.libs.singular
            True
        """

class AllowZeroInversionsContext:
    """
    Temporarily allow zero inversion.
    """
    sr: Incomplete
    def __init__(self, sr) -> None:
        """
        EXAMPLES::

            sage: from sage.crypto.mq.sr import AllowZeroInversionsContext
            sage: sr = mq.SR(1,2,2,4)
            sage: with AllowZeroInversionsContext(sr):
            ....:     sr.sub_byte(0)
            a^2 + a
        """
    allow_zero_inversions: Incomplete
    def __enter__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.crypto.mq.sr import AllowZeroInversionsContext
            sage: sr = mq.SR(1,2,2,4)
            sage: sr.sub_byte(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: A zero inversion occurred during an encryption or key schedule.

            sage: with AllowZeroInversionsContext(sr):
            ....:     sr.sub_byte(0)
            a^2 + a
        """
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None:
        """
        EXAMPLES::

            sage: from sage.crypto.mq.sr import AllowZeroInversionsContext
            sage: sr = mq.SR(1,2,2,4)
            sage: with AllowZeroInversionsContext(sr):
            ....:     sr.sub_byte(0)
            a^2 + a
            sage: sr._allow_zero_inversions
            False
        """

def check_consistency(max_n: int = 2, **kwargs):
    '''
    Test all combinations of ``r``, ``c``, ``e`` and ``n`` in ``(1,
    2)`` for consistency of random encryptions and their polynomial
    systems. `\\GF{2}` and `\\GF{2^e}` systems are tested. This test takes
    a while.

    INPUT:

    - ``max_n`` -- maximal number of rounds to consider (default: 2)
    - ``kwargs`` -- are passed to the SR constructor

    TESTS:

    The following test called with ``max_n`` = 2 requires a LOT of RAM
    (much more than 2GB).  Since this might cause the doctest to fail
    on machines with "only" 2GB of RAM, we test ``max_n`` = 1, which
    has a more reasonable memory usage. ::

        sage: from sage.crypto.mq.sr import check_consistency
        sage: check_consistency(1)  # long time (65s on sage.math, 2012)
        True
    '''
