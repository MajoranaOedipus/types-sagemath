from _typeshed import Incomplete
from sage.crypto.sbox import SBox as SBox
from sage.misc.functional import is_even as is_even, is_odd as is_odd

def bracken_leander(n):
    """
    Return the Bracken-Leander construction.

    For n = 4*k and odd k, the construction is `x \\mapsto x^{2^{2k} + 2^k + 1}`
    over `\\GF{2^n}`

    INPUT:

    - ``n`` -- size of the S-Box

    EXAMPLES::

        sage: from sage.crypto.sboxes import bracken_leander
        sage: sbox = bracken_leander(12); [sbox(i) for i in range(8)]
        [0, 1, 2742, 4035, 1264, 408, 1473, 1327]
    """
def carlet_tang_tang_liao(n, c=None, bf=None):
    """
    Return the Carlet-Tang-Tang-Liao construction.

    See [CTTL2014]_ for its definition.

    INPUT:

    - ``n`` -- integer; the bit length of inputs and outputs, has to be even
      and `\\geq 6`
    - ``c`` -- element of `\\GF{2^{n-1}}` used in the construction
      (default: random element)
    - ``f`` -- function from `\\GF{2^n} \\to \\GF{2}` or BooleanFunction on `n-1`
      bits (default: ``x -> (1/(x+1)).trace())``)

    EXAMPLES::

        sage: from sage.crypto.sboxes import carlet_tang_tang_liao as cttl
        sage: cttl(6).differential_uniformity() in [4, 64]
        True
    """
def gold(n, i):
    """
    Return the Gold function defined by `x \\mapsto x^{2^i + 1}` over `\\GF{2^n}`.

    INPUT:

    - ``n`` -- size of the S-Box
    - ``i`` -- positive integer

    EXAMPLES::

        sage: from sage.crypto.sboxes import gold
        sage: gold(3, 1)
        (0, 1, 3, 4, 5, 6, 7, 2)
        sage: gold(3, 1).differential_uniformity()
        2
        sage: gold(4, 2)
        (0, 1, 6, 6, 7, 7, 7, 6, 1, 7, 1, 6, 1, 6, 7, 1)
    """
def kasami(n, i):
    """
    Return the Kasami function defined by `x \\mapsto x^{2^{2i} - 2^i + 1}` over `\\GF{2^n}`.

    INPUT:

    - ``n`` -- size of the S-Box
    - ``i`` -- positive integer

    EXAMPLES::

        sage: from sage.crypto.sboxes import kasami
        sage: kasami(3, 1)
        (0, 1, 3, 4, 5, 6, 7, 2)
        sage: from sage.crypto.sboxes import gold
        sage: kasami(3, 1) == gold(3, 1)
        True
        sage: kasami(4, 2)
        (0, 1, 13, 11, 14, 9, 6, 7, 10, 4, 15, 2, 8, 3, 5, 12)
        sage: kasami(4, 2) != gold(4, 2)
        True
    """
def niho(n):
    """
    Return the Niho function over `\\GF{2^n}`.

    It is defined by `x \\mapsto x^{2^t + 2^s - 1}` with `s = t/2` if t is even
    or `s = (3t+1)/2` if t is odd.

    INPUT:

    - ``n`` -- size of the S-Box

    EXAMPLES::

        sage: from sage.crypto.sboxes import niho
        sage: niho(3)
        (0, 1, 7, 2, 3, 4, 5, 6)

        sage: niho(3).differential_uniformity()
        2
    """
def welch(n):
    """
    Return the Welch function defined by `x \\mapsto x^{2^{(n-1)/2} + 3}` over `\\GF{2^n}`.

    INPUT:

    - ``n`` -- size of the S-Box

    EXAMPLES::

        sage: from sage.crypto.sboxes import welch
        sage: welch(3)
        (0, 1, 7, 2, 3, 4, 5, 6)
        sage: welch(3).differential_uniformity()
        2
    """
def monomial_function(n, e):
    """
    Return an S-Box as a function `x^e` defined over `\\GF{2^n}`.

    INPUT:

    - ``n`` -- size of the S-Box (i.e. the degree of the finite field extension)
    - ``e`` -- exponent of the monomial function

    EXAMPLES::

        sage: from sage.crypto.sboxes import monomial_function
        sage: S = monomial_function(7, 3)
        sage: S.differential_uniformity()
        2
        sage: S.input_size()
        7
        sage: S.is_permutation()
        True
    """
def inversion(n):
    """
    Return the S-Box constructed from the inversion mapping over `\\GF{2^n}`
    extending `0 \\mapsto 0`.

    INPUT:

    - ``n`` -- size of the S-Box

    EXAMPLES::

        sage: from sage.crypto.sboxes import inversion
        sage: S4 = inversion(4)
        sage: S4.differential_uniformity()
        4
        sage: S5 = inversion(5)
        sage: S5.differential_uniformity()
        2
    """
def chi(n):
    """
    Return the `\\chi` function defined over `\\GF{2^n}` used in the nonlinear
    layer of Keccak and Xoodyak.

    INPUT:

    - ``n`` -- size of the S-Box

    EXAMPLES::

        sage: from sage.crypto.sboxes import chi
        sage: chi(3)
        (0, 3, 6, 1, 5, 4, 2, 7)
        sage: chi(3).is_permutation()
        True
        sage: chi(4).is_permutation()
        False
        sage: chi(5)
        (0, 9, 18, 11, 5, 12, 22, 15, 10, 3, 24, 1, 13, 4, 30, 7, 20, 21, 6,
        23, 17, 16, 2, 19, 26, 27, 8, 25, 29, 28, 14, 31)
    """

DryGASCON256: Incomplete
AES: Incomplete
FlexAEAD = AES
Anubis: Incomplete
ARIA_s2: Incomplete
BelT: Incomplete
Camellia: Incomplete
CMEA: Incomplete
Chiasmus: Incomplete
CLEFIA_S0: Incomplete
CLEFIA_S1: Incomplete
Crypton_0_5: Incomplete
Crypton_1_0_S0: Incomplete
Crypton_1_0_S1: Incomplete
Crypton_1_0_S2: Incomplete
Crypton_1_0_S3: Incomplete
CS_cipher: Incomplete
CSA: Incomplete
CSS: Incomplete
DBlock: Incomplete
E2: Incomplete
Enocoro: Incomplete
Fantomas: Incomplete
FLY: Incomplete
Fox: Incomplete
Iceberg: Incomplete
Iraqi: Incomplete
iScream: Incomplete
Kalyna_pi0: Incomplete
Kalyna_pi1: Incomplete
Kalyna_pi2: Incomplete
Kalyna_pi3: Incomplete
Khazad: Incomplete
Kuznyechik: Incomplete
Kuznechik = Kuznyechik
Streebog = Kuznyechik
Stribog = Kuznyechik
Lilliput_AE: Incomplete
MD2: Incomplete
newDES: Incomplete
Picaro: Incomplete
Safer: Incomplete
Scream: Incomplete
SEED_S0: Incomplete
SEED_S1: Incomplete
SKINNY_8: Incomplete
ForkSkinny_8 = SKINNY_8
Remus_8 = SKINNY_8
Romulus = SKINNY_8
Skipjack: Incomplete
SNOW_3G_sq: Incomplete
SMS4: Incomplete
Turing: Incomplete
Twofish_p0: Incomplete
Twofish_p1: Incomplete
Whirlpool: Incomplete
Zorro: Incomplete
ZUC_S0: Incomplete
ZUC_S1: Incomplete
WAGE: Incomplete
Fides_6: Incomplete
APN_6: Incomplete
SC2000_6: Incomplete
Ascon: Incomplete
ISAP = Ascon
DryGASCON128: Incomplete
Fides_5: Incomplete
SC2000_5: Incomplete
Shamash: Incomplete
SYCON: Incomplete
Elephant: Incomplete
KNOT: Incomplete
Pyjamask_4: Incomplete
SATURNIN_0: Incomplete
SATURNIN_1: Incomplete
Spook: Incomplete
Clyde = Spook
Shadow = Spook
TRIFLE: Incomplete
Yarara: Incomplete
Coral = Yarara
DES_S1_1: Incomplete
DES_S1_2: Incomplete
DES_S1_3: Incomplete
DES_S1_4: Incomplete
DES_S2_1: Incomplete
DES_S2_2: Incomplete
DES_S2_3: Incomplete
DES_S2_4: Incomplete
DES_S3_1: Incomplete
DES_S3_2: Incomplete
DES_S3_3: Incomplete
DES_S3_4: Incomplete
DES_S4_1: Incomplete
DES_S4_2: Incomplete
DES_S4_3: Incomplete
DES_S4_4: Incomplete
DES_S5_1: Incomplete
DES_S5_2: Incomplete
DES_S5_3: Incomplete
DES_S5_4: Incomplete
DES_S6_1: Incomplete
DES_S6_2: Incomplete
DES_S6_3: Incomplete
DES_S6_4: Incomplete
DES_S7_1: Incomplete
DES_S7_2: Incomplete
DES_S7_3: Incomplete
DES_S7_4: Incomplete
DES_S8_1: Incomplete
DES_S8_2: Incomplete
DES_S8_3: Incomplete
DES_S8_4: Incomplete
Lucifer_S0: Incomplete
Lucifer_S1: Incomplete
GOST_1: Incomplete
GOST_2: Incomplete
GOST_3: Incomplete
GOST_4: Incomplete
GOST_5: Incomplete
GOST_6: Incomplete
GOST_7: Incomplete
GOST_8: Incomplete
GOST2_1: Incomplete
GOST2_2: Incomplete
Magma_1: Incomplete
Magma_2: Incomplete
Magma_3: Incomplete
Magma_4: Incomplete
Magma_5: Incomplete
Magma_6: Incomplete
Magma_7: Incomplete
Magma_8: Incomplete
GOST_IETF_1: Incomplete
GOST_IETF_2: Incomplete
GOST_IETF_3: Incomplete
GOST_IETF_4: Incomplete
GOST_IETF_5: Incomplete
GOST_IETF_6: Incomplete
GOST_IETF_7: Incomplete
GOST_IETF_8: Incomplete
Hummingbird_2_S1: Incomplete
Hummingbird_2_S2: Incomplete
Hummingbird_2_S3: Incomplete
Hummingbird_2_S4: Incomplete
LBlock_0: Incomplete
LBlock_1: Incomplete
LBlock_2: Incomplete
LBlock_3: Incomplete
LBlock_4: Incomplete
LBlock_5: Incomplete
LBlock_6: Incomplete
LBlock_7: Incomplete
LBlock_8: Incomplete
LBlock_9: Incomplete
SERPENT_S0: Incomplete
SERPENT_S1: Incomplete
SERPENT_S2: Incomplete
SERPENT_S3: Incomplete
SERPENT_S4: Incomplete
SERPENT_S5: Incomplete
SERPENT_S6: Incomplete
SERPENT_S7: Incomplete
KLEIN: Incomplete
MIBS: Incomplete
Midori_Sb0: Incomplete
MANTIS = Midori_Sb0
WARP = Midori_Sb0
CRAFT = Midori_Sb0
Midori_Sb1: Incomplete
Noekeon: Incomplete
Piccolo: Incomplete
Panda: Incomplete
PRESENT: Incomplete
CiliPadi = PRESENT
PHOTON = PRESENT
ORANGE = PHOTON
GIFT: Incomplete
HYENA = GIFT
Fountain_1 = GIFT
TGIF = GIFT
Fountain_2: Incomplete
Fountain_3: Incomplete
Fountain_4: Incomplete
Pride: Incomplete
PRINCE: Incomplete
Prost = Pride
Qarma_sigma0: Incomplete
Qarma_sigma1: Incomplete
Qameleon = Qarma_sigma1
Qarma_sigma2: Incomplete
REC_0: Incomplete
Rectangle: Incomplete
SC2000_4: Incomplete
SKINNY_4: Incomplete
ForkSkinny_4 = SKINNY_4
Remus_4 = SKINNY_4
TWINE: Incomplete
Luffa_v1: Incomplete
Luffa: Incomplete
BLAKE_1: Incomplete
BLAKE_2: Incomplete
BLAKE_3: Incomplete
BLAKE_4: Incomplete
BLAKE_5: Incomplete
BLAKE_6: Incomplete
BLAKE_7: Incomplete
BLAKE_8: Incomplete
BLAKE_9: Incomplete
JH_S0: Incomplete
JH_S1: Incomplete
SMASH_256_S1: Incomplete
SMASH_256_S2: Incomplete
SMASH_256_S3: Incomplete
Anubis_S0: Incomplete
Anubis_S1: Incomplete
CLEFIA_SS0: Incomplete
CLEFIA_SS1: Incomplete
CLEFIA_SS2: Incomplete
CLEFIA_SS3: Incomplete
Enocoro_S4: Incomplete
Iceberg_S0 = Anubis_S0
Iceberg_S1 = Anubis_S1
Khazad_P: Incomplete
Khazad_Q: Incomplete
Whirlpool_E: Incomplete
Whirlpool_R: Incomplete
CS_cipher_F: Incomplete
CS_cipher_G: Incomplete
Fox_S1: Incomplete
Fox_S2: Incomplete
Fox_S3: Incomplete
Twofish_Q0_T0: Incomplete
Twofish_Q0_T1: Incomplete
Twofish_Q0_T2: Incomplete
Twofish_Q0_T3: Incomplete
Twofish_Q1_T0: Incomplete
Twofish_Q1_T1: Incomplete
Twofish_Q1_T2: Incomplete
Twofish_Q1_T3: Incomplete
Kuznyechik_nu0: Incomplete
Kuznyechik_nu1: Incomplete
Kuznyechik_sigma: Incomplete
Kuznyechik_phi: Incomplete
Optimal_S0: Incomplete
Optimal_S1: Incomplete
Optimal_S2: Incomplete
Optimal_S3: Incomplete
Optimal_S4: Incomplete
Optimal_S5: Incomplete
Optimal_S6: Incomplete
Optimal_S7: Incomplete
Optimal_S8: Incomplete
Optimal_S9: Incomplete
Optimal_S10: Incomplete
Optimal_S11: Incomplete
Optimal_S12: Incomplete
Optimal_S13: Incomplete
Optimal_S14: Incomplete
Optimal_S15: Incomplete
Serpent_type_S0: Incomplete
Serpent_type_S1: Incomplete
Serpent_type_S2: Incomplete
Serpent_type_S3: Incomplete
Serpent_type_S4: Incomplete
Serpent_type_S5: Incomplete
Serpent_type_S6: Incomplete
Serpent_type_S7: Incomplete
Serpent_type_S8: Incomplete
Serpent_type_S9: Incomplete
Serpent_type_S10: Incomplete
Serpent_type_S11: Incomplete
Serpent_type_S12: Incomplete
Serpent_type_S13: Incomplete
Serpent_type_S14: Incomplete
Serpent_type_S15: Incomplete
Serpent_type_S16: Incomplete
Serpent_type_S17: Incomplete
Serpent_type_S18: Incomplete
Serpent_type_S19: Incomplete
Golden_S0: Incomplete
Golden_S1 = Serpent_type_S4
Golden_S2 = Serpent_type_S3
Golden_S3 = Serpent_type_S5
UDCIKMP11: Incomplete
SEA: Incomplete
PRINTcipher: Incomplete
Pyjamask_3: Incomplete
affine_equiv_classes: Incomplete
sboxes: Incomplete
v: Incomplete
