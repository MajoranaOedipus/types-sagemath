from .classical_cipher import AffineCipher as AffineCipher, HillCipher as HillCipher, ShiftCipher as ShiftCipher, SubstitutionCipher as SubstitutionCipher, TranspositionCipher as TranspositionCipher, VigenereCipher as VigenereCipher
from .cryptosystem import SymmetricKeyCryptosystem as SymmetricKeyCryptosystem
from sage.arith.misc import inverse_mod as inverse_mod, xgcd as xgcd
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.monoids.string_monoid import AlphabeticStringMonoid as AlphabeticStringMonoid, StringMonoid_class as StringMonoid_class
from sage.monoids.string_monoid_element import StringMonoidElement as StringMonoidElement
from sage.monoids.string_ops import strip_encoding as strip_encoding
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class AffineCryptosystem(SymmetricKeyCryptosystem):
    '''
    Create an affine cryptosystem.

    Let `A = \\{ a_0, a_1, a_2, \\dots, a_{n-1} \\}` be a non-empty alphabet
    consisting of `n` unique elements. Define a mapping
    `f : A \\longrightarrow \\ZZ / n\\ZZ` from the alphabet `A` to
    the set `\\ZZ / n\\ZZ` of integers modulo `n`, given by
    `f(a_i) = i`. Thus we can identify each element of the alphabet `A`
    with a unique integer `0 \\leq i < n`. A key of the affine cipher is an
    ordered pair of integers `(a, b) \\in \\ZZ / n\\ZZ \\times \\ZZ / n\\ZZ` such
    that `\\gcd(a, n) = 1`. Therefore the key space is
    `\\ZZ / n\\ZZ \\times \\ZZ / n\\ZZ`. Since we assume that `A` does not have
    repeated elements, the mapping `f : A \\longrightarrow \\ZZ/ n\\ZZ` is
    bijective. Encryption and decryption functions are both affine functions.
    Let `(a,b)` be a secret key, i.e. an element of the key space, and let
    `p` be a plaintext character and consequently `p \\in \\ZZ / n\\ZZ`. Then
    the ciphertext character `c` corresponding to `p` is given by

    .. MATH::

        c \\equiv ap + b \\pmod{n}

    Similarly, given a ciphertext character `c \\in \\ZZ / n\\ZZ` and a secret
    key `(a,b)`, we can recover the corresponding plaintext character as
    follows:

    .. MATH::

        p \\equiv a^{-1} (c - b) \\pmod{n}

    where `a^{-1}` is the inverse of `a` modulo `n`. Use the bijection
    `f : A \\longrightarrow \\ZZ / n\\ZZ` to convert `c` and `p` back to
    elements of the alphabet `A`. Currently, only the following alphabet is
    supported for the affine cipher:

    - capital letters of the English alphabet as implemented in
      :func:`AlphabeticStrings()
      <sage.monoids.string_monoid.AlphabeticStrings>`

    EXAMPLES:

    Encryption and decryption over the capital letters of the English
    alphabet::

        sage: A = AffineCryptosystem(AlphabeticStrings()); A
        Affine cryptosystem on Free alphabetic string monoid on A-Z
        sage: P = A.encoding("The affine cryptosystem generalizes the shift cipher.")
        sage: P
        THEAFFINECRYPTOSYSTEMGENERALIZESTHESHIFTCIPHER
        sage: a, b = (9, 13)
        sage: C = A.enciphering(a, b, P); C
        CYXNGGHAXFKVSCJTVTCXRPXAXKNIHEXTCYXTYHGCFHSYXK
        sage: A.deciphering(a, b, C)
        THEAFFINECRYPTOSYSTEMGENERALIZESTHESHIFTCIPHER
        sage: A.deciphering(a, b, C) == P
        True

    We can also use functional notation to work through the previous
    example::

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

    Encrypting the ciphertext with the inverse key also produces the
    plaintext::

        sage: A = AffineCryptosystem(AlphabeticStrings())
        sage: P = A.encoding("Encrypt with inverse key.")
        sage: a, b = (11, 8)
        sage: C = A.enciphering(a, b, P)
        sage: P; C
        ENCRYPTWITHINVERSEKEY
        AVENMRJQSJHSVFANYAOAM
        sage: aInv, bInv = A.inverse_key(a, b)
        sage: A.enciphering(aInv, bInv, C)
        ENCRYPTWITHINVERSEKEY
        sage: A.enciphering(aInv, bInv, C) == P
        True

    For a secret key `(a,b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ`, if `a = 1` then
    any affine cryptosystem with key `(1, b)` for any `b \\in \\ZZ/n\\ZZ` is
    a shift cryptosystem. Here is how we can create a Caesar cipher using
    an affine cipher::

        sage: caesar = AffineCryptosystem(AlphabeticStrings())
        sage: a, b = (1, 3)
        sage: P = caesar.encoding("abcdef"); P
        ABCDEF
        sage: C = caesar.enciphering(a, b, P); C
        DEFGHI
        sage: caesar.deciphering(a, b, C) == P
        True

    Any affine cipher with keys of the form
    `(a,0) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` is called a decimation cipher on
    the Roman alphabet, or decimation cipher for short::

        sage: A = AffineCryptosystem(AlphabeticStrings())
        sage: P = A.encoding("A decimation cipher is a specialized affine cipher.")
        sage: a, b = (17, 0)
        sage: C = A.enciphering(a, b, P)
        sage: P; C
        ADECIMATIONCIPHERISASPECIALIZEDAFFINECIPHER
        AZQIGWALGENIGVPQDGUAUVQIGAFGJQZAHHGNQIGVPQD
        sage: A.deciphering(a, b, C) == P
        True

    Generate a random key for encryption and decryption::

        sage: A = AffineCryptosystem(AlphabeticStrings())
        sage: P = A.encoding("An affine cipher with a random key.")
        sage: a, b = A.random_key()
        sage: C = A.enciphering(a, b, P)
        sage: A.deciphering(a, b, C) == P
        True

    TESTS:

    The binary number system is currently not a supported alphabet of
    this affine cryptosystem::

        sage: AffineCryptosystem(BinaryStrings())
        Traceback (most recent call last):
        ...
        TypeError: A (= Free binary string monoid) is not supported as a cipher domain of this affine cryptosystem.

    Nor are the octal, hexadecimal, and radix-64 number systems supported::

        sage: AffineCryptosystem(OctalStrings())
        Traceback (most recent call last):
        ...
        TypeError: A (= Free octal string monoid) is not supported as a cipher domain of this affine cryptosystem.
        sage: AffineCryptosystem(HexadecimalStrings())
        Traceback (most recent call last):
        ...
        TypeError: A (= Free hexadecimal string monoid) is not supported as a cipher domain of this affine cryptosystem.
        sage: AffineCryptosystem(Radix64Strings())
        Traceback (most recent call last):
        ...
        TypeError: A (= Free radix 64 string monoid) is not supported as a cipher domain of this affine cryptosystem.

    A secret key `(a,b)` must be an element of `\\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` with
    `\\gcd(a,n) = 1`. This rules out the case `a = 0` irrespective of the
    value of `b`. For the upper-case letters of the English alphabet, where
    the alphabet size is `n = 26`, `a` cannot take on any even value::

        sage: A = AffineCryptosystem(AlphabeticStrings())
        sage: A(0, 1)
        Traceback (most recent call last):
        ...
        ValueError: (a, b) = (0, 1) is outside the range of acceptable values for a key of this affine cryptosystem.
        sage: A(2, 1)
        Traceback (most recent call last):
        ...
        ValueError: (a, b) = (2, 1) is outside the range of acceptable values for a key of this affine cryptosystem.

    REFERENCES:

    - [Sti2006]_
    '''
    def __init__(self, A) -> None:
        """
        See ``AffineCryptosystem`` for full documentation.

        INPUT:

        - ``A`` -- string monoid over some alphabet; this is the non-empty
          alphabet over which the plaintext and ciphertext spaces
          are defined

        OUTPUT: an affine cryptosystem over the alphabet ``A``

        EXAMPLES:

        Testing of dumping and loading objects::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: A == loads(dumps(A))
            True
        """
    def __call__(self, a, b):
        '''
        Create an affine cipher with secret key ``(a,b)``.

        INPUT:

        - ``(a, b)`` -- a secret key; this key is used for both encryption and
          decryption. For the affine cryptosystem whose plaintext and
          ciphertext spaces are `A`, a key is an ordered pair
          `(a,b) \\in \\ZZ / n\\ZZ \\times \\ZZ / n\\ZZ` where `n` is the size or
          cardinality of the set `A` and `\\gcd(a,n) = 1`.

        OUTPUT:

        - An affine cipher with secret key ``(a,b)``.

        EXAMPLES::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: P = A.encoding("Fine here, fine there."); P
            FINEHEREFINETHERE
            sage: a, b = (17, 3)
            sage: E = A(a, b); E
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: E(P)
            KJQTSTGTKJQTOSTGT
            sage: C = E(P)
            sage: C
            KJQTSTGTKJQTOSTGT
            sage: aInv, bInv = A.inverse_key(a, b)
            sage: D = A(aInv, bInv); D
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: P == D(C)
            True
            sage: D(E(P))
            FINEHEREFINETHERE

        TESTS:

        The key must be an ordered pair
        `(a,b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` with `n` being the size of the
        plaintext and ciphertext spaces. Furthermore, `a` must be
        relatively prime to `n`, i.e. `\\gcd(a,n) = 1`::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: A(2, 3)
            Traceback (most recent call last):
            ...
            ValueError: (a, b) = (2, 3) is outside the range of acceptable values for a key of this affine cryptosystem.
        '''
    def rank_by_chi_square(self, C, pdict):
        '''
        Use the chi-square statistic to rank all possible keys. Currently,
        this method only applies to the capital letters of the English
        alphabet.

        ALGORITHM:

        Consider a non-empty alphabet `A` consisting of `n`
        elements, and let `C` be a ciphertext encoded using elements of
        `A`. The plaintext `P` corresponding to `C` is also encoded using
        elements of `A`. Let `M` be a candidate decipherment of `C`,
        i.e. `M` is the result of attempting to decrypt `C` using a key
        `(a,b)` which is not necessarily the same key used to encrypt `P`.
        Suppose `F_A(e)` is the characteristic frequency probability of
        `e \\in A` and let `F_M(e)` be the message frequency probability with
        respect to `M`. The characteristic frequency probability
        distribution of an alphabet is the expected frequency probability
        distribution for that alphabet. The message frequency probability
        distribution of `M` provides a distribution of the ratio of character
        occurrences over message length. One can interpret the
        characteristic frequency probability `F_A(e)` as the expected
        probability, while the message frequency probability `F_M(e)` is
        the observed probability. If `M` is of length `L`, then the observed
        frequency of `e \\in A` is

        .. MATH::

            O_M(e)
            =
            F_M(e) \\cdot L

        and the expected frequency of `e \\in A` is

        .. MATH::

            E_A(e)
            =
            F_A(e) \\cdot L

        The chi-square rank `R_{\\chi^2}(M)` of `M` corresponding to a key
        `(a,b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` is given by

        .. MATH::

            R_{\\chi^2}(M)
            =
            \\sum_{e \\in A} \\frac {\\big( O_M(e) - E_A(e) \\big)^2}
                                 {E_A(e)}

        Cryptanalysis by exhaustive key search produces a candidate
        decipherment `M_{a,b}` for each possible key `(a,b)`. For a set
        `D = \\big\\{M_{a_1,b_1}, M_{a_2,b_2}, \\dots, M_{a_k,b_k} \\big\\}`
        of all candidate decipherments corresponding to a ciphertext `C`,
        the smaller is the rank `R_{\\chi^2}(M_{a_i,b_i})` the more likely
        that `(a_i,b_i)` is the secret key. This key ranking method is
        based on the Pearson chi-square test [PearsonTest]_.

        INPUT:

        - ``C`` -- the ciphertext, a non-empty string. The ciphertext
          must be encoded using the upper-case letters of the English
          alphabet.

        - ``pdict`` -- dictionary of key, possible plaintext
          pairs. This should be the output of :func:`brute_force` with
          ``ranking="none"``.

        OUTPUT:

        - A list ranking the most likely keys first. Each element of the
          list is a tuple of key, possible plaintext pairs.

        EXAMPLES:

        Use the chi-square statistic to rank all possible keys and their
        corresponding decipherment::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 7)
            sage: P = A.encoding("Line.")
            sage: C = A.enciphering(a, b, P)
            sage: Plist = A.brute_force(C)
            sage: Rank = A.rank_by_chi_square(C, Plist)
            sage: Rank[:10]  # display only the top 10 candidate keys
            <BLANKLINE>
            [((1, 1), NETS),
            ((3, 7), LINE),
            ((17, 20), STAD),
            ((5, 2), SLOT),
            ((5, 5), HADI),
            ((9, 25), TSLI),
            ((17, 15), DELO),
            ((15, 6), ETUN),
            ((21, 8), ELID),
            ((7, 17), HCTE)]

        As more ciphertext is available, the reliability of the chi-square
        ranking function increases::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (11, 24)
            sage: P = A.encoding("Longer message is more information for cryptanalysis.")
            sage: C = A.enciphering(a, b, P)
            sage: Plist = A.brute_force(C)
            sage: Rank = A.rank_by_chi_square(C, Plist)
            sage: Rank[:10]  # display only the top 10 candidate keys
            <BLANKLINE>
            [((11, 24), LONGERMESSAGEISMOREINFORMATIONFORCRYPTANALYSIS),
            ((17, 9), INURFSBFLLHRFDLBNSFDUYNSBHEDNUYNSTSVGEHUHIVLDL),
            ((9, 18), RMFIUHYUOOSIUWOYMHUWFBMHYSVWMFBMHGHETVSFSREOWO),
            ((15, 12), VSTACPUCOOGACYOUSPCYTBSPUGNYSTBSPEPIRNGTGVIOYO),
            ((3, 22), PAFOYLKYGGSOYEGKALYEFTALKSBEAFTALILCVBSFSPCGEG),
            ((25, 3), OHSRNADNPPFRNVPDHANVSCHADFEVHSCHAJABWEFSFOBPVP),
            ((7, 25), GHYNVIPVRRLNVFRPHIVFYEHIPLAFHYEHIDITQALYLGTRFR),
            ((5, 2), NEHCIVKISSUCIWSKEVIWHFEVKUPWEHFEVOVABPUHUNASWS),
            ((15, 25), IFGNPCHPBBTNPLBHFCPLGOFCHTALFGOFCRCVEATGTIVBLB),
            ((9, 6), BWPSERIEYYCSEGYIWREGPLWRICFGWPLWRQRODFCPCBOYGY)]

        TESTS:

        The ciphertext cannot be an empty string::

            sage: A.rank_by_chi_square("", Plist)
            Traceback (most recent call last):
            ...
            AttributeError: \'str\' object has no attribute \'parent\'...
            sage: A.rank_by_chi_square(A.encoding(""), Plist)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.
            sage: A.rank_by_chi_square(A.encoding(" "), Plist)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.

        The ciphertext must be encoded using the capital letters of the
        English alphabet as implemented in
        :func:`AlphabeticStrings()
        <sage.monoids.string_monoid.AlphabeticStrings>`::

            sage: H = HexadecimalStrings()
            sage: A.rank_by_chi_square(H.encoding("shift"), Plist)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.
            sage: B = BinaryStrings()
            sage: A.rank_by_chi_square(B.encoding("shift"), Plist)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.

        The dictionary ``pdict`` cannot be empty::

            sage: A.rank_by_chi_square(C, {})
            Traceback (most recent call last):
            ...
            KeyError: (1, 0)
        '''
    def rank_by_squared_differences(self, C, pdict):
        '''
        Use the squared-differences measure to rank all possible keys.
        Currently, this method only applies to the capital letters of
        the English alphabet.

        ALGORITHM:

        Consider a non-empty alphabet `A` consisting of `n`
        elements, and let `C` be a ciphertext encoded using elements of
        `A`. The plaintext `P` corresponding to `C` is also encoded using
        elements of `A`. Let `M` be a candidate decipherment of `C`,
        i.e. `M` is the result of attempting to decrypt `C` using a key
        `(a,b)` which is not necessarily the same key used to encrypt `P`.
        Suppose `F_A(e)` is the characteristic frequency probability of
        `e \\in A` and let `F_M(e)` be the message frequency probability with
        respect to `M`. The characteristic frequency probability
        distribution of an alphabet is the expected frequency probability
        distribution for that alphabet. The message frequency probability
        distribution of `M` provides a distribution of the ratio of character
        occurrences over message length. One can interpret the
        characteristic frequency probability `F_A(e)` as the expected
        probability, while the message frequency probability `F_M(e)` is
        the observed probability. If `M` is of length `L`, then the observed
        frequency of `e \\in A` is

        .. MATH::

            O_M(e)
            =
            F_M(e) \\cdot L

        and the expected frequency of `e \\in A` is

        .. MATH::

            E_A(e)
            =
            F_A(e) \\cdot L

        The squared-differences, or residual sum of squares, rank
        `R_{RSS}(M)` of `M` corresponding to a key
        `(a,b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` is given by

        .. MATH::

            R_{RSS}(M)
            =
            \\sum_{e \\in A} \\big( O_M(e) - E_A(e) \\big)^2

        Cryptanalysis by exhaustive key search produces a candidate
        decipherment `M_{a,b}` for each possible key `(a,b)`. For a set
        `D = \\big\\{M_{a_1,b_1}, M_{a_2,b_2}, \\dots, M_{a_k,b_k} \\big\\}`
        of all candidate decipherments corresponding to a ciphertext `C`,
        the smaller is the rank `R_{RSS}(M_{a_i,b_i})` the more likely
        that `(a_i,b_i)` is the secret key. This key ranking method is
        based on the residual sum of squares measure [RSS]_.

        INPUT:

        - ``C`` -- the ciphertext, a non-empty string. The ciphertext
          must be encoded using the upper-case letters of the English
          alphabet.

        - ``pdict`` -- dictionary of key, possible plaintext
          pairs. This should be the output of :func:`brute_force` with
          ``ranking="none"``.

        OUTPUT:

        - A list ranking the most likely keys first. Each element of the
          list is a tuple of key, possible plaintext pairs.

        EXAMPLES:

        Use the method of squared differences to rank all possible keys
        and their corresponding decipherment::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 7)
            sage: P = A.encoding("Line.")
            sage: C = A.enciphering(a, b, P)
            sage: Plist = A.brute_force(C)
            sage: Rank = A.rank_by_squared_differences(C, Plist)
            sage: Rank[:10]  # display only the top 10 candidate keys
            <BLANKLINE>
            [((1, 1), NETS),
            ((15, 6), ETUN),
            ((7, 17), HCTE),
            ((3, 7), LINE),
            ((17, 15), DELO),
            ((9, 4), EDWT),
            ((9, 9), POHE),
            ((21, 8), ELID),
            ((17, 20), STAD),
            ((7, 18), SNEP)]

        As more ciphertext is available, the reliability of the
        squared-differences ranking function increases::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (11, 24)
            sage: P = A.encoding("Longer message is more information for cryptanalysis.")
            sage: C = A.enciphering(a, b, P)
            sage: Plist = A.brute_force(C)
            sage: Rank = A.rank_by_squared_differences(C, Plist)
            sage: Rank[:10]  # display only the top 10 candidate keys
            <BLANKLINE>
            [((11, 24), LONGERMESSAGEISMOREINFORMATIONFORCRYPTANALYSIS),
            ((9, 14), DYRUGTKGAAEUGIAKYTGIRNYTKEHIYRNYTSTQFHEREDQAIA),
            ((23, 24), DSNEUHIUMMAEUOMISHUONZSHIAROSNZSHKHQXRANADQMOM),
            ((23, 1), ETOFVIJVNNBFVPNJTIVPOATIJBSPTOATILIRYSBOBERNPN),
            ((21, 16), VEBGANYAQQOGAMQYENAMBDENYOTMEBDENUNIHTOBOVIQMQ),
            ((7, 12), TULAIVCIEEYAISECUVISLRUVCYNSULRUVQVGDNYLYTGESE),
            ((5, 20), ZQTOUHWUEEGOUIEWQHUITRQHWGBIQTRQHAHMNBGTGZMEIE),
            ((21, 8), JSPUOBMOEECUOAEMSBOAPRSBMCHASPRSBIBWVHCPCJWEAE),
            ((25, 7), SLWVREHRTTJVRZTHLERZWGLEHJIZLWGLENEFAIJWJSFTZT),
            ((25, 15), ATEDZMPZBBRDZHBPTMZHEOTMPRQHTEOTMVMNIQRERANBHB)]

        TESTS:

        The ciphertext cannot be an empty string::

            sage: A.rank_by_squared_differences("", Plist)
            Traceback (most recent call last):
            ...
            AttributeError: \'str\' object has no attribute \'parent\'...
            sage: A.rank_by_squared_differences(A.encoding(""), Plist)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.
            sage: A.rank_by_squared_differences(A.encoding(" "), Plist)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.

        The ciphertext must be encoded using the capital letters of the
        English alphabet as implemented in
        :func:`AlphabeticStrings()
        <sage.monoids.string_monoid.AlphabeticStrings>`::

            sage: H = HexadecimalStrings()
            sage: A.rank_by_squared_differences(H.encoding("line"), Plist)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.
            sage: B = BinaryStrings()
            sage: A.rank_by_squared_differences(B.encoding("line"), Plist)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.

        The dictionary ``pdict`` cannot be empty::

            sage: A.rank_by_squared_differences(C, {})
            Traceback (most recent call last):
            ...
            KeyError: (1, 0)
        '''
    def brute_force(self, C, ranking: str = 'none'):
        '''
        Attempt a brute force cryptanalysis of the ciphertext ``C``.

        INPUT:

        - ``C`` -- a ciphertext over one of the supported alphabets of this
          affine cryptosystem. See the class :class:`AffineCryptosystem` for
          documentation on the supported alphabets.

        - ``ranking`` -- (default: ``\'none\'``) the method to use for
          ranking all possible keys. If ``ranking="none"``, then do not
          use any ranking function. The following ranking functions are
          supported:

          - ``\'chi_square\'`` -- the chi-square ranking function
            as implemented in the method :func:`rank_by_chi_square`

          - ``\'squared_differences\'`` -- the squared differences ranking
            function as implemented in the method
            :func:`rank_by_squared_differences`.

        OUTPUT:

        - All the possible plaintext sequences corresponding to the
          ciphertext ``C``. This method effectively uses all the possible
          keys in this affine cryptosystem to decrypt ``C``. The method is
          also referred to as exhaustive key search. The output is a
          dictionary of key, candidate decipherment pairs.

        EXAMPLES:

        Cryptanalyze using all possible keys with the option
        ``ranking="none"``::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 7)
            sage: P = A.encoding("Linear"); P
            LINEAR
            sage: C = A.enciphering(a, b, P)
            sage: L = A.brute_force(C)
            sage: sorted(L.items())[:26]  # display 26 candidate decipherments
            <BLANKLINE>
            [((1, 0), OFUTHG),
            ((1, 1), NETSGF),
            ((1, 2), MDSRFE),
            ((1, 3), LCRQED),
            ((1, 4), KBQPDC),
            ((1, 5), JAPOCB),
            ((1, 6), IZONBA),
            ((1, 7), HYNMAZ),
            ((1, 8), GXMLZY),
            ((1, 9), FWLKYX),
            ((1, 10), EVKJXW),
            ((1, 11), DUJIWV),
            ((1, 12), CTIHVU),
            ((1, 13), BSHGUT),
            ((1, 14), ARGFTS),
            ((1, 15), ZQFESR),
            ((1, 16), YPEDRQ),
            ((1, 17), XODCQP),
            ((1, 18), WNCBPO),
            ((1, 19), VMBAON),
            ((1, 20), ULAZNM),
            ((1, 21), TKZYML),
            ((1, 22), SJYXLK),
            ((1, 23), RIXWKJ),
            ((1, 24), QHWVJI),
            ((1, 25), PGVUIH)]

        Use the chi-square ranking function, i.e. ``ranking="chisquare"``::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 7)
            sage: P = A.encoding("Linear functions for encrypting and decrypting."); P
            LINEARFUNCTIONSFORENCRYPTINGANDDECRYPTING
            sage: C = A.enciphering(a, b, P)
            sage: Rank = A.brute_force(C, ranking=\'chisquare\')
            sage: Rank[:10]  # display only the top 10 candidate keys
            <BLANKLINE>
            [((3, 7), LINEARFUNCTIONSFORENCRYPTINGANDDECRYPTING),
            ((23, 25), VYTCGPBMTENYSTOBSPCTEPIRNYTAGTDDCEPIRNYTA),
            ((1, 12), CTIHVUKDIBATLIXKLUHIBUPOATINVIEEHBUPOATIN),
            ((11, 15), HSRYELDAROVSWRQDWLYROLUBVSRIERTTYOLUBVSRI),
            ((25, 1), NWHIUVFMHOPWEHSFEVIHOVABPWHCUHLLIOVABPWHC),
            ((25, 7), TCNOABLSNUVCKNYLKBONUBGHVCNIANRROUBGHVCNI),
            ((15, 4), SHIBVOWZILEHDIJWDOBILOFYEHIRVIGGBLOFYEHIR),
            ((15, 23), PEFYSLTWFIBEAFGTALYFILCVBEFOSFDDYILCVBEFO),
            ((7, 10), IDUFHSYXUTEDNULYNSFUTSVGEDURHUMMFTSVGEDUR),
            ((19, 22), QVETRGABEFUVLENALGTEFGDSUVEHREMMTFGDSUVEH)]

        Use the squared differences ranking function, i.e.
        ``ranking="squared_differences"``::

            sage: Rank = A.brute_force(C, ranking=\'squared_differences\')
            sage: Rank[:10]  # display only the top 10 candidate keys
            <BLANKLINE>
            [((3, 7), LINEARFUNCTIONSFORENCRYPTINGANDDECRYPTING),
            ((23, 6), GJENRAMXEPYJDEZMDANEPATCYJELREOONPATCYJEL),
            ((23, 25), VYTCGPBMTENYSTOBSPCTEPIRNYTAGTDDCEPIRNYTA),
            ((19, 22), QVETRGABEFUVLENALGTEFGDSUVEHREMMTFGDSUVEH),
            ((19, 9), DIRGETNORSHIYRANYTGRSTQFHIRUERZZGSTQFHIRU),
            ((23, 18), KNIRVEQBITCNHIDQHERITEXGCNIPVISSRTEXGCNIP),
            ((17, 16), GHORBEIDOJMHFOVIFEROJETWMHOZBOAARJETWMHOZ),
            ((21, 14), AHEZRMOFEVQHTEBOTMZEVMNIQHEDREKKZVMNIQHED),
            ((1, 12), CTIHVUKDIBATLIXKLUHIBUPOATINVIEEHBUPOATIN),
            ((7, 18), SNEPRCIHEDONXEVIXCPEDCFQONEBREWWPDCFQONEB)]

        TESTS:

        Currently, the binary number system is not supported as an
        alphabet of this affine cryptosystem::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: BinStr = BinaryStrings()
            sage: C = BinStr.encoding("abc")
            sage: A.brute_force(C)
            Traceback (most recent call last):
            ...
            TypeError: Ciphertext must be encoded using one of the supported cipher domains of this affine cryptosystem.

        Nor are the octal, hexadecimal, and radix-64 number systems
        supported::

            sage: OctStr = OctalStrings()
            sage: C = OctStr([1, 2, 3])
            sage: A.brute_force(C)
            Traceback (most recent call last):
            ...
            TypeError: Ciphertext must be encoded using one of the supported cipher domains of this affine cryptosystem.
            sage: HexStr = HexadecimalStrings()
            sage: C = HexStr.encoding("abc")
            sage: A.brute_force(C)
            Traceback (most recent call last):
            ...
            TypeError: Ciphertext must be encoded using one of the supported cipher domains of this affine cryptosystem.
            sage: RadStr = Radix64Strings()
            sage: C = RadStr([1, 2, 3])
            sage: A.brute_force(C)
            Traceback (most recent call last):
            ...
            TypeError: Ciphertext must be encoded using one of the supported cipher domains of this affine cryptosystem.

        Only the chi-square and squared-differences ranking functions are
        currently supported. The keyword ``ranking`` must take on either
        of the values ``\'none\'``, ``\'chisquare\'`` or
        ``\'squared_differences\'``::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 7)
            sage: P = A.encoding("Linear")
            sage: C = A.enciphering(a, b, P)
            sage: A.brute_force(C, ranking=\'chi\')
            Traceback (most recent call last):
            ...
            ValueError: Keyword \'ranking\' must be either \'none\', \'chisquare\', or \'squared_differences\'.
            sage: A.brute_force(C, ranking="")
            Traceback (most recent call last):
            ...
            ValueError: Keyword \'ranking\' must be either \'none\', \'chisquare\', or \'squared_differences\'.
        '''
    def deciphering(self, a, b, C):
        '''
        Decrypt the ciphertext ``C`` with the key ``(a, b)`` using affine
        cipher decryption.

        INPUT:

        - ``a``, ``b`` -- a secret key belonging to the key space of this affine
          cipher. This key must be an element of
          `\\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` such that `\\gcd(a,n) = 1` with `n`
          being the size of the ciphertext and plaintext spaces.

        - ``C`` -- string of ciphertext; possibly an empty string.
          Characters in this string must be encoded using one of the
          supported alphabets. See the method :func:`encoding()` for more
          information.

        OUTPUT: the plaintext corresponding to the ciphertext ``C``

        EXAMPLES:

        Decryption over the capital letters of the English alphabet::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (5, 2)
            sage: P = A.encoding("Affine functions are linear functions.")
            sage: C = A.enciphering(a, b, P); C
            CBBQPWBYPMTQUPOCJWFQPWCJBYPMTQUPO
            sage: P == A.deciphering(a, b, C)
            True

        The previous example can also be worked through using functional
        notation::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (5, 2)
            sage: P = A.encoding("Affine functions are linear functions.")
            sage: E = A(a, b); E
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: C = E(P); C
            CBBQPWBYPMTQUPOCJWFQPWCJBYPMTQUPO
            sage: aInv, bInv = A.inverse_key(a, b)
            sage: D = A(aInv, bInv); D
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: D(C) == P
            True

        If the ciphertext is an empty string, then the plaintext is also
        an empty string regardless of the value of the secret key::

            sage: a, b = A.random_key()
            sage: A.deciphering(a, b, A.encoding(""))
            <BLANKLINE>
            sage: A.deciphering(a, b, A.encoding(" "))
            <BLANKLINE>

        TESTS:

        The key must be an ordered pair
        `(a,b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` with `n` being the size of the
        plaintext and ciphertext spaces. Furthermore, `a` must be
        relatively prime to `n`, i.e. `\\gcd(a,n) = 1`::

            sage: A.deciphering(2, 6, P)
            Traceback (most recent call last):
            ...
            ValueError: (a, b) = (2, 6) is outside the range of acceptable values for a key of this affine cipher.
        '''
    def enciphering(self, a, b, P):
        '''
        Encrypt the plaintext ``P`` with the key ``(a, b)`` using affine cipher
        encryption.

        INPUT:

        - ``a``, ``b`` -- a secret key belonging to the key space of this affine
          cipher. This key must be an element of
          `\\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` such that `\\gcd(a,n) = 1` with `n`
          being the size of the ciphertext and plaintext spaces.

        - ``P`` -- string of plaintext; possibly an empty string.
          Characters in this string must be encoded using one of the
          supported alphabets. See the method :func:`encoding()` for more
          information.

        OUTPUT: the ciphertext corresponding to the plaintext ``P``

        EXAMPLES:

        Encryption over the capital letters of the English alphabet::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 6)
            sage: P = A.encoding("Affine ciphers work with linear functions.")
            sage: A.enciphering(a, b, P)
            GVVETSMEZBSFIUWFKUELBNETSGFVOTMLEWTI

        Now work through the previous example using functional notation::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (3, 6)
            sage: P = A.encoding("Affine ciphers work with linear functions.")
            sage: E = A(a, b); E
            Affine cipher on Free alphabetic string monoid on A-Z
            sage: E(P)
            GVVETSMEZBSFIUWFKUELBNETSGFVOTMLEWTI

        If the plaintext is an empty string, then the ciphertext is also
        an empty string regardless of the value of the secret key::

            sage: a, b = A.random_key()
            sage: A.enciphering(a, b, A.encoding(""))
            <BLANKLINE>
            sage: A.enciphering(a, b, A.encoding(" "))
            <BLANKLINE>

        TESTS:

        The key must be an ordered pair
        `(a,b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` with `n` being the size of the
        plaintext and ciphertext spaces. Furthermore, `a` must be
        relatively prime to `n`, i.e. `\\gcd(a,n) = 1`::

            sage: A.enciphering(2, 6, P)
            Traceback (most recent call last):
            ...
            ValueError: (a, b) = (2, 6) is outside the range of acceptable values for a key of this affine cryptosystem.
        '''
    def encoding(self, S):
        '''
        The encoding of the string ``S`` over the string monoid of this
        affine cipher. For example, if the string monoid of this cryptosystem
        is
        :class:`AlphabeticStringMonoid <sage.monoids.string_monoid.AlphabeticStringMonoid>`,
        then the encoding of ``S`` would be its upper-case equivalent
        stripped of all non-alphabetic characters. Only the following alphabet
        is supported for the affine cipher:

        - capital letters of the English alphabet as implemented in
          :func:`AlphabeticStrings() <sage.monoids.string_monoid.AlphabeticStrings>`

        INPUT:

        - ``S`` -- string, possibly empty

        OUTPUT: the encoding of ``S`` over the string monoid of this
        cryptosystem; if ``S`` is an empty string, return an empty string

        EXAMPLES:

        Encoding over the upper-case letters of the English alphabet::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: A.encoding("Affine cipher over capital letters of the English alphabet.")
            AFFINECIPHEROVERCAPITALLETTERSOFTHEENGLISHALPHABET

        The argument ``S`` can be an empty string, in which case an empty
        string is returned::

            sage: AffineCryptosystem(AlphabeticStrings()).encoding("")
            <BLANKLINE>
        '''
    def inverse_key(self, a, b):
        """
        The inverse key corresponding to the secret key `(a,b)`. If `p` is
        a plaintext character so that `p \\in \\ZZ/n\\ZZ` and `n` is the
        alphabet size, then the ciphertext `c` corresponding to `p` is

        .. MATH::

            c \\equiv ap + b \\pmod{n}

        As `(a,b)` is a key, then the multiplicative inverse `a^{-1}`
        exists and the original plaintext can be recovered as follows

        .. MATH::

            p \\equiv a^{-1} (c - b) \\pmod{n}
              \\equiv a^{-1}c + a^{-1}(-b) \\pmod{n}

        Therefore the ordered pair `(a^{-1}, -ba^{-1})` is the inverse key
        corresponding to `(a,b)`.

        INPUT:

        - ``a``, ``b`` -- a secret key for this affine cipher. The ordered pair
          `(a,b)` must be an element of `\\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` such that
          `\\gcd(a,n) = 1`.

        OUTPUT:

        - The inverse key `(a^{-1}, -ba^{-1})` corresponding to `(a,b)`.

        EXAMPLES::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: a, b = (1, 2)
            sage: A.inverse_key(a, b)
            (1, 24)
            sage: A.inverse_key(3, 2)
            (9, 8)

        Suppose that the plaintext and ciphertext spaces are the capital
        letters of the English alphabet so that `n = 26`. If `\\varphi(n)`
        is the Euler phi function of `n`, then there are `\\varphi(n)`
        integers `0 \\leq a < n` that are relatively prime to `n`. For the
        capital letters of the English alphabet, there are 12 such integers
        relatively prime to `n`::

            sage: euler_phi(A.alphabet_size())                                          # needs sage.libs.pari
            12

        And here is a list of those integers::

            sage: n = A.alphabet_size()
            sage: L = [i for i in range(n) if gcd(i, n) == 1]; L
            [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

        Then a secret key `(a,b)` of this shift cryptosystem is
        such that `a` is an element of the list ``L`` in the last example.
        Any inverse key `(A, B)` corresponding to `(a,b)` is such that
        `A` is also in the list ``L`` above::

            sage: a, b = (3, 9)
            sage: a in L
            True
            sage: aInv, bInv = A.inverse_key(a, b)
            sage: aInv, bInv
            (9, 23)
            sage: aInv in L
            True

        TESTS:

        Any ordered pair of the form `(0, b)` for any integer `b` cannot be
        a secret key of this affine cipher. Hence `(0, b)` does not have
        a corresponding inverse key::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: A.inverse_key(0, 1)
            Traceback (most recent call last):
            ...
            ValueError: (a, b) = (0, 1) is outside the range of acceptable values for a key of this affine cipher.
        """
    def random_key(self):
        """
        Generate a random key within the key space of this affine cipher.
        The generated secret key is an ordered pair
        `(a, b) \\in \\ZZ/n\\ZZ \\times \\ZZ/n\\ZZ` with `n` being the size of
        the cipher domain and `\\gcd(a, n) = 1`. Let `\\varphi(n)` denote
        the Euler phi function of `n`. Then the affine cipher has
        `n \\cdot \\varphi(n)` possible keys (see page 10 of [Sti2006]_).

        OUTPUT:

        - A random key within the key space of this affine cryptosystem.
          The output key is an ordered pair `(a,b)`.

        EXAMPLES::

            sage: A = AffineCryptosystem(AlphabeticStrings())
            sage: A.random_key()  # random
            (17, 25)

        If `(a,b)` is a secret key and `n` is the size of the plaintext and
        ciphertext alphabets, then `\\gcd(a, n) = 1`::

            sage: a, b = A.random_key()
            sage: n = A.alphabet_size()
            sage: gcd(a, n)
            1
        """

class HillCryptosystem(SymmetricKeyCryptosystem):
    '''
    Create a Hill cryptosystem defined by the `m \\times m` matrix space
    over `\\ZZ / N \\ZZ`, where `N` is the alphabet size of
    the string monoid ``S``.

    INPUT:

    - ``S`` -- string monoid over some alphabet

    - ``m`` -- integer `> 0`; the block length of matrices that specify
      block permutations

    OUTPUT: a Hill cryptosystem of block length ``m`` over the alphabet ``S``

    EXAMPLES::

        sage: # needs sage.modules
        sage: S = AlphabeticStrings()
        sage: E = HillCryptosystem(S, 3); E
        Hill cryptosystem on Free alphabetic string monoid on A-Z of block length 3
        sage: R = IntegerModRing(26)
        sage: M = MatrixSpace(R,3,3)
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
        sage: E = HillCryptosystem(S, 3)                                                # needs sage.modules
        sage: E == loads(dumps(E))                                                      # needs sage.modules
        True
    '''
    def __init__(self, S, m) -> None:
        """
        See ``HillCryptosystem`` for full documentation.

        Create a Hill cryptosystem defined by the `m \\times m` matrix space
        over `\\ZZ / N \\ZZ`, where `N` is the alphabet size of
        the string monoid ``S``.

        INPUT:

        - ``S`` -- string monoid over some alphabet

        - ``m`` -- integer `> 0`; the block length of matrices that specify
          block permutations

        OUTPUT: a Hill cryptosystem of block length ``m`` over the alphabet ``S``

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = HillCryptosystem(S, 3); E                                         # needs sage.modules
            Hill cryptosystem on Free alphabetic string monoid on A-Z of block length 3
        """
    def __call__(self, A):
        '''
        Create a Hill cipher.

        INPUT:

        - ``A`` -- a matrix which specifies a block permutation

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
            sage: m = S("LAMAISONBLANCHE")
            sage: e(m)
            JYVKSKQPELAYKPV
            sage: c = e.inverse()
            sage: c(e(m))
            LAMAISONBLANCHE
        '''
    def block_length(self):
        """
        The row or column dimension of a matrix specifying a block
        permutation. Encryption and decryption keys of a Hill cipher are
        square matrices, i.e. the row and column dimensions of an encryption
        or decryption key are the same. This row/column dimension is referred
        to as the *block length*.

        OUTPUT: the block length of an encryption/decryption key

        EXAMPLES::

            sage: A = AlphabeticStrings()
            sage: n = randint(1, A.ngens() - 1)
            sage: H = HillCryptosystem(A, n)                                            # needs sage.modules
            sage: H.block_length() == n                                                 # needs sage.modules
            True
        """
    def random_key(self):
        '''
        A random key within the key space of this Hill cipher. That is,
        generate a random `m \\times m` matrix to be used as a block
        permutation, where `m` is the block length of this Hill cipher. If
        `n` is the size of the cryptosystem alphabet, then there are
        `n^{m^2}` possible keys. However the number of valid keys,
        i.e. invertible `m \\times m` square matrices, is smaller than
        `n^{m^2}`.

        OUTPUT: a random key within the key space of this Hill cipher

        EXAMPLES::

            sage: # needs sage.modules
            sage: A = AlphabeticStrings()
            sage: n = 3
            sage: H = HillCryptosystem(A, n)
            sage: K = H.random_key()
            sage: Ki = H.inverse_key(K)
            sage: M = "LAMAISONBLANCHE"
            sage: e = H(K)
            sage: d = H(Ki)
            sage: d(e(A(M))) == A(M)
            True
        '''
    def inverse_key(self, A):
        '''
        The inverse key corresponding to the key ``A``.

        INPUT:

        - ``A`` -- an invertible matrix of the key space of this Hill cipher

        OUTPUT: the inverse matrix of ``A``

        EXAMPLES::

            sage: # needs sage.modules
            sage: S = AlphabeticStrings()
            sage: E = HillCryptosystem(S, 3)
            sage: A = E.random_key()
            sage: B = E.inverse_key(A)
            sage: M = S("LAMAISONBLANCHE")
            sage: e = E(A)
            sage: c = E(B)
            sage: c(e(M))
            LAMAISONBLANCHE
        '''
    def encoding(self, M):
        '''
        The encoding of the string ``M`` over the string monoid of this
        Hill cipher. For example, if the string monoid of this Hill cipher
        is :class:`AlphabeticStringMonoid`, then the encoding of ``M`` would
        be its upper-case equivalent stripped of all non-alphabetic
        characters.

        INPUT:

        - ``M`` -- string, possibly empty

        OUTPUT: the encoding of ``M`` over the string monoid of this Hill
        cipher

        EXAMPLES::

            sage: M = "The matrix cipher by Lester S. Hill."
            sage: A = AlphabeticStrings()
            sage: H = HillCryptosystem(A, 7)                                            # needs sage.modules
            sage: H.encoding(M) == A.encoding(M)                                        # needs sage.modules
            True
        '''
    def deciphering(self, A, C):
        '''
        Decrypt the ciphertext ``C`` using the key ``A``.

        INPUT:

        - ``A`` -- a key within the key space of this Hill cipher

        - ``C`` -- string (possibly empty) over the string monoid of this
          Hill cipher

        OUTPUT: the plaintext corresponding to the ciphertext ``C``

        EXAMPLES::

            sage: # needs sage.modules
            sage: H = HillCryptosystem(AlphabeticStrings(), 3)
            sage: K = H.random_key()
            sage: M = H.encoding("Good day, mate! How ya going?")
            sage: H.deciphering(K, H.enciphering(K, M)) == M
            True
        '''
    def enciphering(self, A, M):
        '''
        Encrypt the plaintext ``M`` using the key ``A``.

        INPUT:

        - ``A`` -- a key within the key space of this Hill cipher

        - ``M`` -- string (possibly empty) over the string monoid of this
          Hill cipher

        OUTPUT: the ciphertext corresponding to the plaintext ``M``

        EXAMPLES::

            sage: # needs sage.modules
            sage: H = HillCryptosystem(AlphabeticStrings(), 3)
            sage: K = H.random_key()
            sage: M = H.encoding("Good day, mate! How ya going?")
            sage: H.deciphering(K, H.enciphering(K, M)) == M
            True
        '''

class ShiftCryptosystem(SymmetricKeyCryptosystem):
    '''
    Create a shift cryptosystem.

    Let `A = \\{ a_0, a_1, a_2, \\dots, a_{n-1} \\}` be a non-empty alphabet
    consisting of `n` unique elements. Define a mapping
    `f : A \\longrightarrow \\ZZ/ n\\ZZ` from the alphabet `A` to
    the set `\\ZZ / n\\ZZ` of integers modulo `n`, given by
    `f(a_i) = i`. Thus we can identify each element of the alphabet `A`
    with a unique integer `0 \\leq i < n`. A key of the shift cipher is an
    integer `0 \\leq k < n`. Therefore the key space is `\\ZZ / n\\ZZ`. Since
    we assume that `A` does not have repeated elements, the mapping
    `f : A \\longrightarrow \\ZZ/ n\\ZZ` is bijective.
    Encryption works by moving along the alphabet by `k` positions, with
    wrap around. Decryption reverses the process by moving backwards by
    `k` positions, with wrap around. More generally, let `k` be a secret key,
    i.e. an element of the key space, and let `p` be a plaintext
    character and consequently `p \\in \\ZZ / n\\ZZ`. Then the ciphertext
    character `c` corresponding to `p` is given by

    .. MATH::

        c \\equiv p + k \\pmod{n}

    Similarly, given a ciphertext character `c \\in \\ZZ / n\\ZZ` and a secret
    key `k`, we can recover the corresponding plaintext character as follows:

    .. MATH::

        p \\equiv c - k \\pmod{n}

    Use the bijection `f : A \\longrightarrow \\ZZ/ n\\ZZ` to convert `c`
    and `p` back to elements of the alphabet `A`. Currently, the following
    alphabets are supported for the shift cipher:

    - capital letters of the English alphabet as implemented in
      :func:`AlphabeticStrings()
      <sage.monoids.string_monoid.AlphabeticStrings>`

    - the alphabet consisting of the hexadecimal number system as
      implemented in
      :func:`HexadecimalStrings()
      <sage.monoids.string_monoid.HexadecimalStrings>`

    - the alphabet consisting of the binary number system as implemented in
      :func:`BinaryStrings() <sage.monoids.string_monoid.BinaryStrings>`

    EXAMPLES:

    Some examples illustrating encryption and decryption over various
    alphabets. Here is an example over the upper-case letters of the English
    alphabet::

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

    The previous example can also be done as follows::

        sage: S = ShiftCryptosystem(AlphabeticStrings())
        sage: P = S.encoding("The shift cryptosystem generalizes the Caesar cipher.")
        sage: K = 7
        sage: E = S(K); E
        Shift cipher on Free alphabetic string monoid on A-Z
        sage: C = E(P); C
        AOLZOPMAJYFWAVZFZALTNLULYHSPGLZAOLJHLZHYJPWOLY
        sage: D = S(S.inverse_key(K)); D
        Shift cipher on Free alphabetic string monoid on A-Z
        sage: D(C) == P
        True
        sage: D(C) == P == D(E(P))
        True

    Over the hexadecimal number system::

        sage: S = ShiftCryptosystem(HexadecimalStrings()); S
        Shift cryptosystem on Free hexadecimal string monoid
        sage: P = S.encoding("Encryption & decryption shifts along the alphabet."); P
        456e6372797074696f6e20262064656372797074696f6e2073686966747320616c6f6e672074686520616c7068616265742e
        sage: K = 5
        sage: C = S.enciphering(K, P); C
        9ab3b8c7cec5c9beb4b3757b75b9bab8c7cec5c9beb4b375c8bdbebbc9c875b6b1b4b3bc75c9bdba75b6b1c5bdb6b7bac973
        sage: S.deciphering(K, C)
        456e6372797074696f6e20262064656372797074696f6e2073686966747320616c6f6e672074686520616c7068616265742e
        sage: S.deciphering(K, C) == P
        True

    And over the binary number system::

        sage: S = ShiftCryptosystem(BinaryStrings()); S
        Shift cryptosystem on Free binary string monoid
        sage: P = S.encoding("The binary alphabet is very insecure."); P
        01010100011010000110010100100000011000100110100101101110011000010111001001111001001000000110000101101100011100000110100001100001011000100110010101110100001000000110100101110011001000000111011001100101011100100111100100100000011010010110111001110011011001010110001101110101011100100110010100101110
        sage: K = 1
        sage: C = S.enciphering(K, P); C
        10101011100101111001101011011111100111011001011010010001100111101000110110000110110111111001111010010011100011111001011110011110100111011001101010001011110111111001011010001100110111111000100110011010100011011000011011011111100101101001000110001100100110101001110010001010100011011001101011010001
        sage: S.deciphering(K, C)
        01010100011010000110010100100000011000100110100101101110011000010111001001111001001000000110000101101100011100000110100001100001011000100110010101110100001000000110100101110011001000000111011001100101011100100111100100100000011010010110111001110011011001010110001101110101011100100110010100101110
        sage: S.deciphering(K, C) == P
        True

    A shift cryptosystem with key `k = 3` is commonly referred to as the
    Caesar cipher. Create a Caesar cipher over the upper-case letters of the
    English alphabet::

        sage: caesar = ShiftCryptosystem(AlphabeticStrings())
        sage: K = 3
        sage: P = caesar.encoding("abcdef"); P
        ABCDEF
        sage: C = caesar.enciphering(K, P); C
        DEFGHI
        sage: caesar.deciphering(K, C) == P
        True

    Generate a random key for encryption and decryption::

        sage: S = ShiftCryptosystem(AlphabeticStrings())
        sage: P = S.encoding("Shift cipher with a random key.")
        sage: K = S.random_key()
        sage: C = S.enciphering(K, P)
        sage: S.deciphering(K, C) == P
        True

    Decrypting with the key ``K`` is equivalent to encrypting with its
    corresponding inverse key::

        sage: S.enciphering(S.inverse_key(K), C) == P
        True

    TESTS:

    Currently, the octal number system is not supported as an alphabet for
    this shift cryptosystem::

        sage: ShiftCryptosystem(OctalStrings())
        Traceback (most recent call last):
        ...
        TypeError: A (= Free octal string monoid) is not supported as a cipher domain of this shift cryptosystem.

    Nor is the radix-64 number system supported::

        sage: ShiftCryptosystem(Radix64Strings())
        Traceback (most recent call last):
        ...
        TypeError: A (= Free radix 64 string monoid) is not supported as a cipher domain of this shift cryptosystem.

    Testing of dumping and loading objects::

        sage: SA = ShiftCryptosystem(AlphabeticStrings())
        sage: SA == loads(dumps(SA))
        True
        sage: SH = ShiftCryptosystem(HexadecimalStrings())
        sage: SH == loads(dumps(SH))
        True
        sage: SB = ShiftCryptosystem(BinaryStrings())
        sage: SB == loads(dumps(SB))
        True

    The key ``K`` must satisfy the inequality `0 \\leq K < n` with `n`
    being the size of the plaintext, ciphertext, and key spaces. For the
    shift cryptosystem, all these spaces are the same alphabet. This
    inequality must be satisfied for each of the supported alphabets.
    The capital letters of the English alphabet::

        sage: S = ShiftCryptosystem(AlphabeticStrings())
        sage: S(2 + S.alphabet_size())
        Traceback (most recent call last):
        ...
        ValueError: K (=28) is outside the range of acceptable values for a key of this shift cryptosystem.
        sage: S(-2)
        Traceback (most recent call last):
        ...
        ValueError: K (=-2) is outside the range of acceptable values for a key of this shift cryptosystem.

    The hexadecimal number system::

        sage: S = ShiftCryptosystem(HexadecimalStrings())
        sage: S(1 + S.alphabet_size())
        Traceback (most recent call last):
        ...
        ValueError: K (=17) is outside the range of acceptable values for a key of this shift cryptosystem.
        sage: S(-1)
        Traceback (most recent call last):
        ...
        ValueError: K (=-1) is outside the range of acceptable values for a key of this shift cryptosystem.

    The binary number system::

        sage: S = ShiftCryptosystem(BinaryStrings())
        sage: S(1 + S.alphabet_size())
        Traceback (most recent call last):
        ...
        ValueError: K (=3) is outside the range of acceptable values for a key of this shift cryptosystem.
        sage: S(-2)
        Traceback (most recent call last):
        ...
        ValueError: K (=-2) is outside the range of acceptable values for a key of this shift cryptosystem.
    '''
    def __init__(self, A) -> None:
        '''
        See ``ShiftCryptosystem`` for full documentation.

        Create a shift cryptosystem defined over the alphabet ``A``.

        INPUT:

        - ``A`` -- string monoid over some alphabet; this is the non-empty
          alphabet over which the plaintext and ciphertext spaces
          are defined

        OUTPUT: a shift cryptosystem over the alphabet ``A``

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
    def __call__(self, K):
        '''
        Create a shift cipher with key ``K``.

        INPUT:

        - ``K`` -- a secret key; this key is used for both encryption and
          decryption. For the shift cryptosystem whose plaintext and
          ciphertext spaces are `A`, a key is any integer `k` such that
          `0 \\leq k < n` where `n` is the size or cardinality of the set
          `A`.

        OUTPUT: a shift cipher with secret key ``K``

        EXAMPLES::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("Shifting sand."); P
            SHIFTINGSAND
            sage: K = 3
            sage: E = S(K); E
            Shift cipher on Free alphabetic string monoid on A-Z
            sage: E(P)
            VKLIWLQJVDQG
            sage: D = S(S.inverse_key(K)); D
            Shift cipher on Free alphabetic string monoid on A-Z
            sage: D(E(P))
            SHIFTINGSAND

        TESTS:

        The key ``K`` must satisfy the inequality `0 \\leq K < n` with `n`
        being the size of the plaintext, ciphertext, and key spaces. For the
        shift cryptosystem, all these spaces are the same alphabet. This
        inequality must be satisfied for each of the supported alphabets.
        The capital letters of the English alphabet::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: S(2 + S.alphabet_size())
            Traceback (most recent call last):
            ...
            ValueError: K (=28) is outside the range of acceptable values for a key of this shift cryptosystem.
            sage: S(-2)
            Traceback (most recent call last):
            ...
            ValueError: K (=-2) is outside the range of acceptable values for a key of this shift cryptosystem.

        The hexadecimal number system::

            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: S(1 + S.alphabet_size())
            Traceback (most recent call last):
            ...
            ValueError: K (=17) is outside the range of acceptable values for a key of this shift cryptosystem.
            sage: S(-1)
            Traceback (most recent call last):
            ...
            ValueError: K (=-1) is outside the range of acceptable values for a key of this shift cryptosystem.

        The binary number system::

            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: S(1 + S.alphabet_size())
            Traceback (most recent call last):
            ...
            ValueError: K (=3) is outside the range of acceptable values for a key of this shift cryptosystem.
            sage: S(-2)
            Traceback (most recent call last):
            ...
            ValueError: K (=-2) is outside the range of acceptable values for a key of this shift cryptosystem.
        '''
    def rank_by_chi_square(self, C, pdict):
        '''
        Use the chi-square statistic to rank all possible keys. Currently,
        this method only applies to the capital letters of the English
        alphabet.

        ALGORITHM:

        Consider a non-empty alphabet `A` consisting of `n`
        elements, and let `C` be a ciphertext encoded using elements of
        `A`. The plaintext `P` corresponding to `C` is also encoded using
        elements of `A`. Let `M` be a candidate decipherment of `C`,
        i.e. `M` is the result of attempting to decrypt `C` using a key
        `k \\in \\ZZ/n\\ZZ` which is not necessarily the same key used to
        encrypt `P`. Suppose `F_A(e)` is the characteristic frequency
        probability of `e \\in A` and let `F_M(e)` be the message frequency
        probability with respect to `M`. The characteristic frequency
        probability distribution of an alphabet is the expected frequency
        probability distribution for that alphabet. The message frequency
        probability distribution of `M` provides a distribution of the ratio
        of character occurrences over message length. One can interpret the
        characteristic frequency probability `F_A(e)` as the expected
        probability, while the message frequency probability `F_M(e)` is
        the observed probability. If `M` is of length `L`, then the observed
        frequency of `e \\in A` is

        .. MATH::

            O_M(e)
            =
            F_M(e) \\cdot L

        and the expected frequency of `e \\in A` is

        .. MATH::

            E_A(e)
            =
            F_A(e) \\cdot L

        The chi-square rank `R_{\\chi^2}(M)` of `M` corresponding to a key
        `k \\in \\ZZ/n\\ZZ` is given by

        .. MATH::

            R_{\\chi^2}(M)
            =
            \\sum_{e \\in A} \\frac {\\big( O_M(e) - E_A(e) \\big)^2}
                                 {E_A(e)}

        Cryptanalysis by exhaustive key search produces a candidate
        decipherment `M_{k}` for each possible key `k \\in \\ZZ/n\\ZZ`. For
        a set
        `D = \\big\\{M_{k_1}, M_{k_2}, \\dots, M_{k_r} \\big\\}`
        of all candidate decipherments corresponding to a ciphertext `C`,
        the smaller is the rank `R_{\\chi^2}(M_{k_i})` the more likely
        that `k_i` is the secret key. This key ranking method is based on
        the Pearson chi-square test [PearsonTest]_.

        INPUT:

        - ``C`` -- the ciphertext, a non-empty string. The ciphertext
          must be encoded using the upper-case letters of the English
          alphabet.

        - ``pdict`` -- dictionary of key, possible plaintext pairs.
          This should be the output of :func:`brute_force` with
          ``ranking="none"``.

        OUTPUT:

        - A list ranking the most likely keys first. Each element of the
          list is a tuple of key, possible plaintext pairs.

        EXAMPLES:

        Use the chi-square statistic to rank all possible keys and their
        corresponding decipherment::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("Shi."); P
            SHI
            sage: K = 5
            sage: C = S.enciphering(K, P)
            sage: Pdict = S.brute_force(C)
            sage: S.rank_by_chi_square(C, Pdict)
            <BLANKLINE>
            [(9, ODE),
            (5, SHI),
            (20, DST),
            (19, ETU),
            (21, CRS),
            (10, NCD),
            (25, YNO),
            (6, RGH),
            (12, LAB),
            (8, PEF),
            (1, WLM),
            (11, MBC),
            (18, FUV),
            (17, GVW),
            (2, VKL),
            (4, TIJ),
            (3, UJK),
            (0, XMN),
            (16, HWX),
            (15, IXY),
            (23, APQ),
            (24, ZOP),
            (22, BQR),
            (7, QFG),
            (13, KZA),
            (14, JYZ)]

        As more ciphertext is available, the reliability of the chi-square
        ranking function increases::

            sage: P = S.encoding("Shift cipher."); P
            SHIFTCIPHER
            sage: C = S.enciphering(K, P)
            sage: Pdict = S.brute_force(C)
            sage: S.rank_by_chi_square(C, Pdict)
            <BLANKLINE>
            [(5, SHIFTCIPHER),
            (9, ODEBPYELDAN),
            (18, FUVSGPVCURE),
            (2, VKLIWFLSKHU),
            (20, DSTQENTASPC),
            (19, ETURFOUBTQD),
            (21, CRSPDMSZROB),
            (6, RGHESBHOGDQ),
            (7, QFGDRAGNFCP),
            (12, LABYMVBIAXK),
            (17, GVWTHQWDVSF),
            (24, ZOPMAJPWOLY),
            (1, WLMJXGMTLIV),
            (0, XMNKYHNUMJW),
            (11, MBCZNWCJBYL),
            (8, PEFCQZFMEBO),
            (25, YNOLZIOVNKX),
            (10, NCDAOXDKCZM),
            (3, UJKHVEKRJGT),
            (4, TIJGUDJQIFS),
            (22, BQROCLRYQNA),
            (16, HWXUIRXEWTG),
            (15, IXYVJSYFXUH),
            (14, JYZWKTZGYVI),
            (13, KZAXLUAHZWJ),
            (23, APQNBKQXPMZ)]

        TESTS:

        The ciphertext cannot be an empty string::

            sage: S.rank_by_chi_square("", Pdict)
            Traceback (most recent call last):
            ...
            AttributeError: \'str\' object has no attribute \'parent\'...
            sage: S.rank_by_chi_square(S.encoding(""), Pdict)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.
            sage: S.rank_by_chi_square(S.encoding(" "), Pdict)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.

        The ciphertext must be encoded using the capital letters of the
        English alphabet as implemented in
        :func:`AlphabeticStrings()
        <sage.monoids.string_monoid.AlphabeticStrings>`::

            sage: H = HexadecimalStrings()
            sage: S.rank_by_chi_square(H.encoding("shift"), Pdict)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.
            sage: B = BinaryStrings()
            sage: S.rank_by_chi_square(B.encoding("shift"), Pdict)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.

        The dictionary ``pdict`` cannot be empty::

            sage: S.rank_by_chi_square(C, {})
            Traceback (most recent call last):
            ...
            KeyError: 0
        '''
    def rank_by_squared_differences(self, C, pdict):
        '''
        Use the squared-differences measure to rank all possible keys.
        Currently, this method only applies to the capital letters of
        the English alphabet.

        ALGORITHM:

        Consider a non-empty alphabet `A` consisting of `n`
        elements, and let `C` be a ciphertext encoded using elements of
        `A`. The plaintext `P` corresponding to `C` is also encoded using
        elements of `A`. Let `M` be a candidate decipherment of `C`,
        i.e. `M` is the result of attempting to decrypt `C` using a key
        `k \\in \\ZZ/n\\ZZ` which is not necessarily the same key used to
        encrypt `P`. Suppose `F_A(e)` is the characteristic frequency
        probability of `e \\in A` and let `F_M(e)` be the message
        frequency probability with respect to `M`. The characteristic
        frequency probability distribution of an alphabet is the expected
        frequency probability distribution for that alphabet. The message
        frequency probability distribution of `M` provides a distribution
        of the ratio of character occurrences over message length. One can
        interpret the characteristic frequency probability `F_A(e)` as the
        expected probability, while the message frequency probability
        `F_M(e)` is the observed probability. If `M` is of length `L`, then
        the observed frequency of `e \\in A` is

        .. MATH::

            O_M(e)
            =
            F_M(e) \\cdot L

        and the expected frequency of `e \\in A` is

        .. MATH::

            E_A(e)
            =
            F_A(e) \\cdot L

        The squared-differences, or residual sum of squares, rank
        `R_{RSS}(M)` of `M` corresponding to a key
        `k \\in \\ZZ/n\\ZZ` is given by

        .. MATH::

            R_{RSS}(M)
            =
            \\sum_{e \\in A} \\big( O_M(e) - E_A(e) \\big)^2

        Cryptanalysis by exhaustive key search produces a candidate
        decipherment `M_{k}` for each possible key `k \\in \\ZZ/n\\ZZ`. For
        a set
        `D = \\big\\{M_{k_1}, M_{k_2}, \\dots, M_{k_r} \\big\\}`
        of all candidate decipherments corresponding to a ciphertext `C`,
        the smaller is the rank `R_{RSS}(M_{k_i})` the more likely
        that `k_i` is the secret key. This key ranking method is based
        on the residual sum of squares measure [RSS]_.

        INPUT:

        - ``C`` -- the ciphertext, a non-empty string. The ciphertext
          must be encoded using the upper-case letters of the English
          alphabet.

        - ``pdict`` -- dictionary of key, possible plaintext pairs.
          This should be the output of :func:`brute_force` with
          ``ranking="none"``.

        OUTPUT: a list ranking the most likely keys first; each element of the
        list is a tuple of key, possible plaintext pairs

        EXAMPLES:

        Use the method of squared differences to rank all possible keys
        and their corresponding decipherment::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("Shi."); P
            SHI
            sage: K = 5
            sage: C = S.enciphering(K, P)
            sage: Pdict = S.brute_force(C)
            sage: S.rank_by_squared_differences(C, Pdict)
            <BLANKLINE>
            [(19, ETU),
            (9, ODE),
            (20, DST),
            (5, SHI),
            (8, PEF),
            (4, TIJ),
            (25, YNO),
            (21, CRS),
            (6, RGH),
            (10, NCD),
            (12, LAB),
            (23, APQ),
            (24, ZOP),
            (0, XMN),
            (13, KZA),
            (15, IXY),
            (1, WLM),
            (16, HWX),
            (22, BQR),
            (11, MBC),
            (18, FUV),
            (2, VKL),
            (17, GVW),
            (7, QFG),
            (3, UJK),
            (14, JYZ)]

        As more ciphertext is available, the reliability of the squared
        differences ranking function increases::

            sage: P = S.encoding("Shift cipher."); P
            SHIFTCIPHER
            sage: C = S.enciphering(K, P)
            sage: Pdict = S.brute_force(C)
            sage: S.rank_by_squared_differences(C, Pdict)
            <BLANKLINE>
            [(20, DSTQENTASPC),
            (5, SHIFTCIPHER),
            (9, ODEBPYELDAN),
            (19, ETURFOUBTQD),
            (6, RGHESBHOGDQ),
            (16, HWXUIRXEWTG),
            (8, PEFCQZFMEBO),
            (21, CRSPDMSZROB),
            (22, BQROCLRYQNA),
            (25, YNOLZIOVNKX),
            (3, UJKHVEKRJGT),
            (18, FUVSGPVCURE),
            (4, TIJGUDJQIFS),
            (10, NCDAOXDKCZM),
            (7, QFGDRAGNFCP),
            (24, ZOPMAJPWOLY),
            (2, VKLIWFLSKHU),
            (12, LABYMVBIAXK),
            (17, GVWTHQWDVSF),
            (1, WLMJXGMTLIV),
            (13, KZAXLUAHZWJ),
            (0, XMNKYHNUMJW),
            (15, IXYVJSYFXUH),
            (14, JYZWKTZGYVI),
            (11, MBCZNWCJBYL),
            (23, APQNBKQXPMZ)]

        TESTS:

        The ciphertext cannot be an empty string::

            sage: S.rank_by_squared_differences("", Pdict)
            Traceback (most recent call last):
            ...
            AttributeError: \'str\' object has no attribute \'parent\'...
            sage: S.rank_by_squared_differences(S.encoding(""), Pdict)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.
            sage: S.rank_by_squared_differences(S.encoding(" "), Pdict)
            Traceback (most recent call last):
            ...
            ValueError: The ciphertext must be a non-empty string.

        The ciphertext must be encoded using the capital letters of the
        English alphabet as implemented in
        :func:`AlphabeticStrings()
        <sage.monoids.string_monoid.AlphabeticStrings>`::

            sage: H = HexadecimalStrings()
            sage: S.rank_by_squared_differences(H.encoding("shift"), Pdict)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.
            sage: B = BinaryStrings()
            sage: S.rank_by_squared_differences(B.encoding("shift"), Pdict)
            Traceback (most recent call last):
            ...
            TypeError: The ciphertext must be capital letters of the English alphabet.

        The dictionary ``pdict`` cannot be empty::

            sage: S.rank_by_squared_differences(C, {})
            Traceback (most recent call last):
            ...
            KeyError: 0
        '''
    def brute_force(self, C, ranking: str = 'none'):
        '''
        Attempt a brute force cryptanalysis of the ciphertext ``C``.

        INPUT:

        - ``C`` -- a ciphertext over one of the supported alphabets of this
          shift cryptosystem. See the class :class:`ShiftCryptosystem` for
          documentation on the supported alphabets.

        - ``ranking`` -- (default: ``\'none\'``) the method to use for
          ranking all possible keys. If ``ranking="none"``, then do not
          use any ranking function. The following ranking functions are
          supported:

          - ``\'chisquare\'`` -- the chi-square ranking function as
            implemented in the method :func:`rank_by_chi_square`

          - ``\'squared_differences\'`` -- the squared differences ranking
            function as implemented in the method
            :func:`rank_by_squared_differences`.

        OUTPUT:

        - All the possible plaintext sequences corresponding to the
          ciphertext ``C``. This method effectively uses all the possible
          keys in this shift cryptosystem to decrypt ``C``. The method is
          also referred to as exhaustive key search. The output is
          a dictionary of key, plaintext pairs.

        EXAMPLES:

        Cryptanalyze using all possible keys for various alphabets. Over
        the upper-case letters of the English alphabet::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("The shift cryptosystem generalizes the Caesar cipher.")
            sage: K = 7
            sage: C = S.enciphering(K, P)
            sage: Dict = S.brute_force(C)
            sage: for k in range(len(Dict)):
            ....:     if Dict[k] == P:
            ....:         print("key = " + str(k))
            key = 7

        Over the hexadecimal number system::

            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: P = S.encoding("Encryption & decryption shifts along the alphabet.")
            sage: K = 5
            sage: C = S.enciphering(K, P)
            sage: Dict = S.brute_force(C)
            sage: for k in range(len(Dict)):
            ....:     if Dict[k] == P:
            ....:         print("key = " + str(k))
            key = 5

        And over the binary number system::

            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: P = S.encoding("The binary alphabet is very insecure.")
            sage: K = 1
            sage: C = S.enciphering(K, P)
            sage: Dict = S.brute_force(C)
            sage: for k in range(len(Dict)):
            ....:     if Dict[k] == P:
            ....:         print("key = " + str(k))
            key = 1

        Don\'t use any ranking functions, i.e. ``ranking="none"``::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("Shifting using modular arithmetic.")
            sage: K = 8
            sage: C = S.enciphering(K, P)
            sage: pdict = S.brute_force(C)
            sage: sorted(pdict.items())
            <BLANKLINE>
            [(0, APQNBQVOCAQVOUWLCTIZIZQBPUMBQK),
            (1, ZOPMAPUNBZPUNTVKBSHYHYPAOTLAPJ),
            (2, YNOLZOTMAYOTMSUJARGXGXOZNSKZOI),
            (3, XMNKYNSLZXNSLRTIZQFWFWNYMRJYNH),
            (4, WLMJXMRKYWMRKQSHYPEVEVMXLQIXMG),
            (5, VKLIWLQJXVLQJPRGXODUDULWKPHWLF),
            (6, UJKHVKPIWUKPIOQFWNCTCTKVJOGVKE),
            (7, TIJGUJOHVTJOHNPEVMBSBSJUINFUJD),
            (8, SHIFTINGUSINGMODULARARITHMETIC),
            (9, RGHESHMFTRHMFLNCTKZQZQHSGLDSHB),
            (10, QFGDRGLESQGLEKMBSJYPYPGRFKCRGA),
            (11, PEFCQFKDRPFKDJLARIXOXOFQEJBQFZ),
            (12, ODEBPEJCQOEJCIKZQHWNWNEPDIAPEY),
            (13, NCDAODIBPNDIBHJYPGVMVMDOCHZODX),
            (14, MBCZNCHAOMCHAGIXOFULULCNBGYNCW),
            (15, LABYMBGZNLBGZFHWNETKTKBMAFXMBV),
            (16, KZAXLAFYMKAFYEGVMDSJSJALZEWLAU),
            (17, JYZWKZEXLJZEXDFULCRIRIZKYDVKZT),
            (18, IXYVJYDWKIYDWCETKBQHQHYJXCUJYS),
            (19, HWXUIXCVJHXCVBDSJAPGPGXIWBTIXR),
            (20, GVWTHWBUIGWBUACRIZOFOFWHVASHWQ),
            (21, FUVSGVATHFVATZBQHYNENEVGUZRGVP),
            (22, ETURFUZSGEUZSYAPGXMDMDUFTYQFUO),
            (23, DSTQETYRFDTYRXZOFWLCLCTESXPETN),
            (24, CRSPDSXQECSXQWYNEVKBKBSDRWODSM),
            (25, BQROCRWPDBRWPVXMDUJAJARCQVNCRL)]

        Use the chi-square ranking function, i.e. ``ranking="chisquare"``::

            sage: S.brute_force(C, ranking=\'chisquare\')
            <BLANKLINE>
            [(8, SHIFTINGUSINGMODULARARITHMETIC),
            (14, MBCZNCHAOMCHAGIXOFULULCNBGYNCW),
            (20, GVWTHWBUIGWBUACRIZOFOFWHVASHWQ),
            (13, NCDAODIBPNDIBHJYPGVMVMDOCHZODX),
            (1, ZOPMAPUNBZPUNTVKBSHYHYPAOTLAPJ),
            (23, DSTQETYRFDTYRXZOFWLCLCTESXPETN),
            (10, QFGDRGLESQGLEKMBSJYPYPGRFKCRGA),
            (6, UJKHVKPIWUKPIOQFWNCTCTKVJOGVKE),
            (22, ETURFUZSGEUZSYAPGXMDMDUFTYQFUO),
            (15, LABYMBGZNLBGZFHWNETKTKBMAFXMBV),
            (12, ODEBPEJCQOEJCIKZQHWNWNEPDIAPEY),
            (21, FUVSGVATHFVATZBQHYNENEVGUZRGVP),
            (16, KZAXLAFYMKAFYEGVMDSJSJALZEWLAU),
            (25, BQROCRWPDBRWPVXMDUJAJARCQVNCRL),
            (9, RGHESHMFTRHMFLNCTKZQZQHSGLDSHB),
            (24, CRSPDSXQECSXQWYNEVKBKBSDRWODSM),
            (3, XMNKYNSLZXNSLRTIZQFWFWNYMRJYNH),
            (5, VKLIWLQJXVLQJPRGXODUDULWKPHWLF),
            (7, TIJGUJOHVTJOHNPEVMBSBSJUINFUJD),
            (2, YNOLZOTMAYOTMSUJARGXGXOZNSKZOI),
            (18, IXYVJYDWKIYDWCETKBQHQHYJXCUJYS),
            (4, WLMJXMRKYWMRKQSHYPEVEVMXLQIXMG),
            (11, PEFCQFKDRPFKDJLARIXOXOFQEJBQFZ),
            (19, HWXUIXCVJHXCVBDSJAPGPGXIWBTIXR),
            (0, APQNBQVOCAQVOUWLCTIZIZQBPUMBQK),
            (17, JYZWKZEXLJZEXDFULCRIRIZKYDVKZT)]

        Use the squared differences ranking function, i.e.
        ``ranking="squared_differences"``::

            sage: S.brute_force(C, ranking=\'squared_differences\')
            <BLANKLINE>
            [(8, SHIFTINGUSINGMODULARARITHMETIC),
            (23, DSTQETYRFDTYRXZOFWLCLCTESXPETN),
            (12, ODEBPEJCQOEJCIKZQHWNWNEPDIAPEY),
            (2, YNOLZOTMAYOTMSUJARGXGXOZNSKZOI),
            (9, RGHESHMFTRHMFLNCTKZQZQHSGLDSHB),
            (7, TIJGUJOHVTJOHNPEVMBSBSJUINFUJD),
            (21, FUVSGVATHFVATZBQHYNENEVGUZRGVP),
            (22, ETURFUZSGEUZSYAPGXMDMDUFTYQFUO),
            (1, ZOPMAPUNBZPUNTVKBSHYHYPAOTLAPJ),
            (16, KZAXLAFYMKAFYEGVMDSJSJALZEWLAU),
            (20, GVWTHWBUIGWBUACRIZOFOFWHVASHWQ),
            (24, CRSPDSXQECSXQWYNEVKBKBSDRWODSM),
            (14, MBCZNCHAOMCHAGIXOFULULCNBGYNCW),
            (13, NCDAODIBPNDIBHJYPGVMVMDOCHZODX),
            (3, XMNKYNSLZXNSLRTIZQFWFWNYMRJYNH),
            (10, QFGDRGLESQGLEKMBSJYPYPGRFKCRGA),
            (15, LABYMBGZNLBGZFHWNETKTKBMAFXMBV),
            (6, UJKHVKPIWUKPIOQFWNCTCTKVJOGVKE),
            (11, PEFCQFKDRPFKDJLARIXOXOFQEJBQFZ),
            (25, BQROCRWPDBRWPVXMDUJAJARCQVNCRL),
            (17, JYZWKZEXLJZEXDFULCRIRIZKYDVKZT),
            (19, HWXUIXCVJHXCVBDSJAPGPGXIWBTIXR),
            (4, WLMJXMRKYWMRKQSHYPEVEVMXLQIXMG),
            (0, APQNBQVOCAQVOUWLCTIZIZQBPUMBQK),
            (18, IXYVJYDWKIYDWCETKBQHQHYJXCUJYS),
            (5, VKLIWLQJXVLQJPRGXODUDULWKPHWLF)]

        TESTS:

        Currently, the octal number system is not supported as an alphabet for
        this shift cryptosystem::

            sage: SA = ShiftCryptosystem(AlphabeticStrings())
            sage: OctStr = OctalStrings()
            sage: C = OctStr([1, 2, 3])
            sage: SA.brute_force(C)
            Traceback (most recent call last):
            ...
            TypeError: ciphertext must be encoded using one of the supported cipher domains of this shift cryptosystem.

        Nor is the radix-64 alphabet supported::

            sage: Rad64 = Radix64Strings()
            sage: C = Rad64([1, 2, 3])
            sage: SA.brute_force(C)
            Traceback (most recent call last):
            ...
            TypeError: ciphertext must be encoded using one of the supported cipher domains of this shift cryptosystem.
        '''
    def deciphering(self, K, C):
        '''
        Decrypt the ciphertext ``C`` with the key ``K`` using shift cipher
        decryption.

        INPUT:

        - ``K`` -- a secret key; a key belonging to the key space of this
          shift cipher. This key is an integer `k` satisfying the inequality
          `0 \\leq k < n`, where `n` is the size of the cipher domain.

        - ``C`` -- string of ciphertext; possibly an empty string
          Characters in this string must be encoded using one of the
          supported alphabets. See the method :func:`encoding()`
          for more information.

        OUTPUT: the plaintext corresponding to the ciphertext ``C``

        EXAMPLES:

        Let\'s perform decryption over the supported alphabets. Here is
        decryption over the capital letters of the English alphabet::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("Stop shifting me."); P
            STOPSHIFTINGME
            sage: K = 13
            sage: C = S.enciphering(K, P); C
            FGBCFUVSGVATZR
            sage: S.deciphering(K, C) == P
            True

        Decryption over the hexadecimal number system::

            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: P = S.encoding("Shift me now."); P
            5368696674206d65206e6f772e
            sage: K = 7
            sage: C = S.enciphering(K, P); C
            cadfd0ddeb97d4dc97d5d6ee95
            sage: S.deciphering(K, C) == P
            True

        Decryption over the binary number system::

            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: P = S.encoding("OK, enough shifting."); P
            0100111101001011001011000010000001100101011011100110111101110101011001110110100000100000011100110110100001101001011001100111010001101001011011100110011100101110
            sage: K = 1
            sage: C = S.enciphering(K, P); C
            1011000010110100110100111101111110011010100100011001000010001010100110001001011111011111100011001001011110010110100110011000101110010110100100011001100011010001
            sage: S.deciphering(K, C) == P
            True
        '''
    def enciphering(self, K, P):
        '''
        Encrypt the plaintext ``P`` with the key ``K`` using shift cipher
        encryption.

        INPUT:

        - ``K`` -- a key belonging to the key space of this shift cipher.
          This key is an integer `k` satisfying the inequality
          `0 \\leq k < n`, where `n` is the size of the cipher domain.

        - ``P`` -- string of plaintext; possibly an empty string.
          Characters in this string must be encoded using one of the
          supported alphabets. See the method :func:`encoding()` for more
          information.

        OUTPUT: the ciphertext corresponding to the plaintext ``P``

        EXAMPLES:

        Let\'s perform encryption over the supported alphabets. Here is
        encryption over the capital letters of the English alphabet::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: P = S.encoding("Shift your gear."); P
            SHIFTYOURGEAR
            sage: K = 3
            sage: S.enciphering(K, P)
            VKLIWBRXUJHDU

        Encryption over the hexadecimal number system::

            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: P = S.encoding("Capitalize with the shift key."); P
            4361706974616c697a65207769746820746865207368696674206b65792e
            sage: K = 5
            sage: S.enciphering(K, P)
            98b6c5bec9b6b1becfba75ccbec9bd75c9bdba75c8bdbebbc975b0bace73

        Encryption over the binary number system::

            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: P = S.encoding("Don\'t shift."); P
            010001000110111101101110001001110111010000100000011100110110100001101001011001100111010000101110
            sage: K = 1
            sage: S.enciphering(K, P)
            101110111001000010010001110110001000101111011111100011001001011110010110100110011000101111010001
        '''
    def encoding(self, S):
        '''
        The encoding of the string ``S`` over the string monoid of this
        shift cipher. For example, if the string monoid of this cryptosystem
        is
        :class:`AlphabeticStringMonoid <sage.monoids.string_monoid.AlphabeticStringMonoid>`,
        then the encoding of ``S`` would be its upper-case equivalent
        stripped of all non-alphabetic characters. The following alphabets
        are supported for the shift cipher:

        - capital letters of the English alphabet as implemented in
          :func:`AlphabeticStrings() <sage.monoids.string_monoid.AlphabeticStrings>`

        - the alphabet consisting of the hexadecimal number system as
          implemented in
          :func:`HexadecimalStrings() <sage.monoids.string_monoid.HexadecimalStrings>`

        - the alphabet consisting of the binary number system as implemented in
          :func:`BinaryStrings() <sage.monoids.string_monoid.BinaryStrings>`

        INPUT:

        - ``S`` -- string, possibly empty

        OUTPUT: the encoding of ``S`` over the string monoid of this
        cryptosystem; if ``S`` is an empty string, return an empty string

        EXAMPLES:

        Encoding over the upper-case letters of the English alphabet::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: S.encoding("Shift cipher on capital letters of the English alphabet.")
            SHIFTCIPHERONCAPITALLETTERSOFTHEENGLISHALPHABET

        Encoding over the binary system::

            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: S.encoding("Binary")
            010000100110100101101110011000010111001001111001

        Encoding over the hexadecimal system::

            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: S.encoding("Over hexadecimal system.")
            4f7665722068657861646563696d616c2073797374656d2e

        The argument ``S`` can be an empty string, in which case an empty
        string is returned::

            sage: ShiftCryptosystem(AlphabeticStrings()).encoding("")
            <BLANKLINE>
            sage: ShiftCryptosystem(HexadecimalStrings()).encoding("")
            <BLANKLINE>
            sage: ShiftCryptosystem(BinaryStrings()).encoding("")
            <BLANKLINE>
        '''
    def inverse_key(self, K):
        """
        The inverse key corresponding to the key ``K``. For the shift cipher,
        the inverse key corresponding to ``K`` is `-K \\bmod n`, where
        `n > 0` is the size of the cipher domain, i.e. the
        plaintext/ciphertext space. A key `k` of the shift cipher is an
        integer `0 \\leq k < n`. The key `k = 0` has no effect on either the
        plaintext or the ciphertext.

        INPUT:

        - ``K`` -- a key for this shift cipher. This must be an integer `k`
          such that `0 \\leq k < n`, where `n` is the size of the cipher domain

        OUTPUT: the inverse key corresponding to ``K``

        EXAMPLES:

        Some random keys and their respective inverse keys::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: key = S.random_key(); key  # random
            2
            sage: S.inverse_key(key)         # random
            24
            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: key = S.random_key(); key  # random
            12
            sage: S.inverse_key(key)         # random
            4
            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: key = S.random_key(); key  # random
            1
            sage: S.inverse_key(key)         # random
            1
            sage: key = S.random_key(); key  # random
            0
            sage: S.inverse_key(key)         # random
            0

        Regardless of the value of a key, the addition of the key and its
        inverse must be equal to the alphabet size. This relationship holds
        exactly when the value of the key is nonzero::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: K = S.random_key()
            sage: while K == 0:
            ....:     K = S.random_key()
            sage: invK = S.inverse_key(K)
            sage: K + invK == S.alphabet_size()
            True
            sage: invK + K == S.alphabet_size()
            True
            sage: K = S.random_key()
            sage: while K != 0:
            ....:     K = S.random_key()
            sage: invK = S.inverse_key(K)
            sage: K + invK != S.alphabet_size()
            True
            sage: K; invK
            0
            0

        TESTS:

        The key ``K`` must satisfy the inequality `0 \\leq K < n` with `n`
        being the size of the plaintext, ciphertext, and key spaces. For the
        shift cryptosystem, all these spaces are the same alphabet. This
        inequality must be satisfied for each of the supported alphabets.
        The capital letters of the English alphabet::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: S.inverse_key(S.alphabet_size())
            Traceback (most recent call last):
            ...
            ValueError: K (=26) is outside the range of acceptable values for a key of this shift cryptosystem.
            sage: S.inverse_key(-1)
            Traceback (most recent call last):
            ...
            ValueError: K (=-1) is outside the range of acceptable values for a key of this shift cryptosystem.

        The hexadecimal number system::

            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: S.inverse_key(S.alphabet_size())
            Traceback (most recent call last):
            ...
            ValueError: K (=16) is outside the range of acceptable values for a key of this shift cryptosystem.
            sage: S.inverse_key(-1)
            Traceback (most recent call last):
            ...
            ValueError: K (=-1) is outside the range of acceptable values for a key of this shift cryptosystem.

        The binary number system::

            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: S.inverse_key(S.alphabet_size())
            Traceback (most recent call last):
            ...
            ValueError: K (=2) is outside the range of acceptable values for a key of this shift cryptosystem.
            sage: S.inverse_key(-1)
            Traceback (most recent call last):
            ...
            ValueError: K (=-1) is outside the range of acceptable values for a key of this shift cryptosystem.
        """
    def random_key(self):
        """
        Generate a random key within the key space of this shift cipher.
        The generated key is an integer `0 \\leq k < n` with `n` being the
        size of the cipher domain. Thus there are `n` possible keys in the
        key space, which is the set `\\ZZ / n\\ZZ`. The key `k = 0` has no
        effect on either the plaintext or the ciphertext.

        OUTPUT: a random key within the key space of this shift cryptosystem

        EXAMPLES::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: S.random_key()  # random
            18
            sage: S = ShiftCryptosystem(BinaryStrings())
            sage: S.random_key()  # random
            0
            sage: S = ShiftCryptosystem(HexadecimalStrings())
            sage: S.random_key()  # random
            5

        Regardless of the value of a key, the addition of the key and its
        inverse must be equal to the alphabet size. This relationship holds
        exactly when the value of the key is nonzero::

            sage: S = ShiftCryptosystem(AlphabeticStrings())
            sage: K = S.random_key()
            sage: while K == 0:
            ....:     K = S.random_key()
            sage: invK = S.inverse_key(K)
            sage: K + invK == S.alphabet_size()
            True
            sage: invK + K == S.alphabet_size()
            True
            sage: K = S.random_key()
            sage: while K != 0:
            ....:     K = S.random_key()
            sage: invK = S.inverse_key(K)
            sage: K + invK != S.alphabet_size()
            True
            sage: K; invK
            0
            0
        """

class SubstitutionCryptosystem(SymmetricKeyCryptosystem):
    '''
    Create a substitution cryptosystem.

    INPUT:

    - ``S`` -- string monoid over some alphabet

    OUTPUT: a substitution cryptosystem over the alphabet ``S``

    EXAMPLES::

        sage: M = AlphabeticStrings()
        sage: E = SubstitutionCryptosystem(M)
        sage: E
        Substitution cryptosystem on Free alphabetic string monoid on A-Z
        sage: K = M([ 25-i for i in range(26) ])
        sage: K
        ZYXWVUTSRQPONMLKJIHGFEDCBA
        sage: e = E(K)
        sage: m = M("THECATINTHEHAT")
        sage: e(m)
        GSVXZGRMGSVSZG

    TESTS::

        sage: M = AlphabeticStrings()
        sage: E = SubstitutionCryptosystem(M)
        sage: E == loads(dumps(E))
        True
    '''
    def __init__(self, S) -> None:
        """
        See ``SubstitutionCryptosystem`` for full documentation.

        EXAMPLES::

            sage: M = AlphabeticStrings()
            sage: E = SubstitutionCryptosystem(M)
            sage: E
            Substitution cryptosystem on Free alphabetic string monoid on A-Z
        """
    def __call__(self, K):
        '''
        Create a substitution cipher.

        INPUT:

        - ``K`` -- a key which is a permutation of the cryptosystem alphabet

        EXAMPLES::

            sage: M = AlphabeticStrings()
            sage: E = SubstitutionCryptosystem(M)
            sage: E
            Substitution cryptosystem on Free alphabetic string monoid on A-Z
            sage: K = M([ 25-i for i in range(26) ])
            sage: K
            ZYXWVUTSRQPONMLKJIHGFEDCBA
            sage: e = E(K)
            sage: m = M("THECATINTHEHAT")
            sage: e(m)
            GSVXZGRMGSVSZG
        '''
    def random_key(self):
        '''
        Generate a random key within the key space of this substitution
        cipher. The generated key is a permutation of the cryptosystem
        alphabet. Let `n` be the length of the alphabet. Then there are
        `n!` possible keys in the key space.

        OUTPUT: a random key within the key space of this cryptosystem

        EXAMPLES::

            sage: A = AlphabeticStrings()
            sage: S = SubstitutionCryptosystem(A)
            sage: K = S.random_key()
            sage: Ki = S.inverse_key(K)
            sage: M = "THECATINTHEHAT"
            sage: e = S(K)
            sage: d = S(Ki)
            sage: d(e(A(M))) == A(M)
            True
        '''
    def inverse_key(self, K):
        '''
        The inverse key corresponding to the key ``K``. The specified key is a
        permutation of the cryptosystem alphabet.

        INPUT:

        - ``K`` -- a key belonging to the key space of this cryptosystem

        OUTPUT: the inverse key of ``K``

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = SubstitutionCryptosystem(S)
            sage: K = E.random_key()
            sage: L = E.inverse_key(K)
            sage: M = S("THECATINTHEHAT")
            sage: e = E(K)
            sage: c = E(L)
            sage: c(e(M))
            THECATINTHEHAT
        '''
    def encoding(self, M):
        '''
        The encoding of the string ``M`` over the string monoid of this
        substitution cipher. For example, if the string monoid of this
        cryptosystem is :class:`AlphabeticStringMonoid`, then the encoding
        of ``M`` would be its upper-case equivalent stripped of all
        non-alphabetic characters.

        INPUT:

        - ``M`` -- string, possibly empty

        OUTPUT: the encoding of ``M`` over the string monoid of this
        cryptosystem

        EXAMPLES::

            sage: M = "Peter Pan(ning) for gold."
            sage: A = AlphabeticStrings()
            sage: S = SubstitutionCryptosystem(A)
            sage: S.encoding(M) == A.encoding(M)
            True
        '''
    def deciphering(self, K, C):
        '''
        Decrypt the ciphertext ``C`` using the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this substitution cipher

        - ``C`` -- string (possibly empty) over the string monoid of this
          cryptosystem

        OUTPUT: the plaintext corresponding to the ciphertext ``C``

        EXAMPLES::

            sage: S = SubstitutionCryptosystem(AlphabeticStrings())
            sage: K = S.random_key()
            sage: M = S.encoding("Don\'t substitute me!")
            sage: S.deciphering(K, S.enciphering(K, M)) == M
            True
        '''
    def enciphering(self, K, M):
        '''
        Encrypt the plaintext ``M`` using the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this substitution cipher

        - ``M`` -- string (possibly empty) over the string monoid of this
          cryptosystem

        OUTPUT: the ciphertext corresponding to the plaintext ``M``

        EXAMPLES::

            sage: S = SubstitutionCryptosystem(AlphabeticStrings())
            sage: K = S.random_key()
            sage: M = S.encoding("Don\'t substitute me.")
            sage: S.deciphering(K, S.enciphering(K, M)) == M
            True
        '''

class TranspositionCryptosystem(SymmetricKeyCryptosystem):
    '''
    Create a transposition cryptosystem of block length ``n``.

    INPUT:

    - ``S`` -- string monoid over some alphabet

    - ``n`` -- integer `> 0`; a block length of a block permutation

    OUTPUT:

    - A transposition cryptosystem of block length ``n`` over the
      alphabet ``S``.

    EXAMPLES::

        sage: S = AlphabeticStrings()
        sage: E = TranspositionCryptosystem(S,14); E                                    # needs sage.groups
        Transposition cryptosystem on
         Free alphabetic string monoid on A-Z of block length 14
        sage: K = [14 - i for i in range(14)]; K
        [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sage: e = E(K)                                                                  # needs sage.groups
        sage: e(S("THECATINTHEHAT"))                                                    # needs sage.groups
        TAHEHTNITACEHT

    TESTS::

        sage: S = AlphabeticStrings()
        sage: E = TranspositionCryptosystem(S,14)                                       # needs sage.groups
        sage: E == loads(dumps(E))                                                      # needs sage.groups
        True
    '''
    def __init__(self, S, n) -> None:
        """
        See ``TranspositionCryptosystem`` for full documentation.

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(S,14); E                                # needs sage.groups
            Transposition cryptosystem on Free alphabetic string monoid on A-Z of block length 14
        """
    def __call__(self, K):
        '''
        Create a transposition cipher.

        INPUT:

        - ``K`` -- a key which specifies a block permutation

        EXAMPLES::

            sage: M = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(M,14); E                                # needs sage.groups
            Transposition cryptosystem on Free alphabetic string monoid on A-Z of block length 14
            sage: K = [14 - i for i in range(14)]; K
            [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            sage: e = E(K)                                                              # needs sage.groups
            sage: m = M("THECATINTHEHAT")
            sage: e(m)                                                                  # needs sage.groups
            TAHEHTNITACEHT
        '''
    def random_key(self):
        '''
        Generate a random key within the key space of this transposition
        cryptosystem. Let `n > 0` be the block length of this cryptosystem.
        Then there are `n!` possible keys.

        OUTPUT: a random key within the key space of this cryptosystem

        EXAMPLES::

            sage: # needs sage.groups
            sage: S = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(S, 14)
            sage: K = E.random_key()
            sage: Ki = E.inverse_key(K)
            sage: e = E(K)
            sage: d = E(Ki)
            sage: M = "THECATINTHEHAT"
            sage: C = e(S(M))
            sage: d(S(C)) == S(M)
            True
        '''
    def inverse_key(self, K, check: bool = True):
        '''
        The inverse key corresponding to the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this transposition
          cipher

        - ``check`` -- boolean (default: ``True``); check that ``K`` belongs to
          the key space of this cryptosystem

        OUTPUT: the inverse key corresponding to ``K``

        EXAMPLES::

            sage: # needs sage.groups
            sage: S = AlphabeticStrings()
            sage: E = TranspositionCryptosystem(S, 14)
            sage: K = E.random_key()
            sage: Ki = E.inverse_key(K)
            sage: e = E(K)
            sage: d = E(Ki)
            sage: M = "THECATINTHEHAT"
            sage: C = e(S(M))
            sage: d(S(C)) == S(M)
            True
        '''
    def encoding(self, M):
        '''
        The encoding of the string ``M`` over the string monoid of this
        transposition cipher. For example, if the string monoid of this
        cryptosystem is :class:`AlphabeticStringMonoid`, then the encoding
        of ``M`` would be its upper-case equivalent stripped of all
        non-alphabetic characters.

        INPUT:

        - ``M`` -- string, possibly empty

        OUTPUT: the encoding of ``M`` over the string monoid of this
        cryptosystem

        EXAMPLES::

            sage: M = "Transposition cipher is not about matrix transpose."
            sage: A = AlphabeticStrings()
            sage: T = TranspositionCryptosystem(A, 11)                                  # needs sage.groups
            sage: T.encoding(M) == A.encoding(M)                                        # needs sage.groups
            True
        '''
    def deciphering(self, K, C):
        '''
        Decrypt the ciphertext ``C`` using the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this transposition
          cipher

        - ``C`` -- string (possibly empty) over the string monoid of this
          cryptosystem

        OUTPUT: the plaintext corresponding to the ciphertext ``C``

        EXAMPLES::

            sage: # needs sage.groups
            sage: T = TranspositionCryptosystem(AlphabeticStrings(), 14)
            sage: K = T.random_key()
            sage: M = T.encoding("The cat in the hat.")
            sage: T.deciphering(K, T.enciphering(K, M)) == M
            True
        '''
    def enciphering(self, K, M):
        '''
        Encrypt the plaintext ``M`` using the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this transposition
          cipher

        - ``M`` -- string (possibly empty) over the string monoid of this
          cryptosystem

        OUTPUT: the ciphertext corresponding to the plaintext ``M``

        EXAMPLES::

            sage: # needs sage.groups
            sage: T = TranspositionCryptosystem(AlphabeticStrings(), 14)
            sage: K = T.random_key()
            sage: M = T.encoding("The cat in the hat.")
            sage: T.deciphering(K, T.enciphering(K, M)) == M
            True
        '''

class VigenereCryptosystem(SymmetricKeyCryptosystem):
    '''
    Create a Vigenere cryptosystem of block length ``n``.

    INPUT:

    - ``S`` -- string monoid over some alphabet

    - ``n`` -- integer `> 0`; block length of an encryption/decryption key

    OUTPUT:

    - A Vigenere cryptosystem of block length ``n`` over the alphabet
      ``S``.

    EXAMPLES::

        sage: S = AlphabeticStrings()
        sage: E = VigenereCryptosystem(S,14)
        sage: E
        Vigenere cryptosystem on Free alphabetic string monoid on A-Z of period 14
        sage: K = S(\'ABCDEFGHIJKLMN\')
        sage: K
        ABCDEFGHIJKLMN
        sage: e = E(K)
        sage: e
        Cipher on Free alphabetic string monoid on A-Z
        sage: e(S("THECATINTHEHAT"))
        TIGFEYOUBQOSMG

    TESTS::

        sage: S = AlphabeticStrings()
        sage: E = VigenereCryptosystem(S,14)
        sage: E == loads(dumps(E))
        True
    '''
    def __init__(self, S, n) -> None:
        """
        See ``VigenereCryptosystem`` for full documentation.

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = VigenereCryptosystem(S,14)
            sage: E
            Vigenere cryptosystem on Free alphabetic string monoid on A-Z of period 14
        """
    def __call__(self, K):
        '''
        Create a Vigenere cipher.

        INPUT:

        - ``K`` -- a key which specifies a block permutation

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = VigenereCryptosystem(S,14)
            sage: E
            Vigenere cryptosystem on Free alphabetic string monoid on A-Z of period 14
            sage: K = S(\'ABCDEFGHIJKLMN\')
            sage: K
            ABCDEFGHIJKLMN
            sage: e = E(K)
            sage: e
            Cipher on Free alphabetic string monoid on A-Z
            sage: e(S("THECATINTHEHAT"))
            TIGFEYOUBQOSMG
        '''
    def random_key(self):
        '''
        Generate a random key within the key space of this Vigenere
        cryptosystem. Let `n > 0` be the length of the cryptosystem alphabet
        and let `m > 0` be the block length of this cryptosystem. Then there
        are `n^m` possible keys.

        OUTPUT: a random key within the key space of this cryptosystem

        EXAMPLES::

            sage: A = AlphabeticStrings()
            sage: V = VigenereCryptosystem(A, 14)
            sage: M = "THECATINTHEHAT"
            sage: K = V.random_key()
            sage: Ki = V.inverse_key(K)
            sage: e = V(K)
            sage: d = V(Ki)
            sage: d(e(A(M))) == A(M)
            True
        '''
    def inverse_key(self, K):
        '''
        The inverse key corresponding to the key ``K``.

        INPUT:

        - ``K`` -- a key within the key space of this Vigenere cryptosystem

        OUTPUT: the inverse key corresponding to ``K``

        EXAMPLES::

            sage: S = AlphabeticStrings()
            sage: E = VigenereCryptosystem(S,14)
            sage: K = E.random_key()
            sage: L = E.inverse_key(K)
            sage: M = S("THECATINTHEHAT")
            sage: e = E(K)
            sage: c = E(L)
            sage: c(e(M))
            THECATINTHEHAT
        '''
    def encoding(self, M):
        '''
        The encoding of the string ``M`` over the string monoid of this
        Vigenere cipher. For example, if the string monoid of this
        cryptosystem is :class:`AlphabeticStringMonoid`, then the encoding
        of ``M`` would be its upper-case equivalent stripped of all
        non-alphabetic characters.

        INPUT:

        - ``M`` -- string, possibly empty

        OUTPUT: the encoding of ``M`` over the string monoid of this
        cryptosystem

        EXAMPLES::

            sage: A = AlphabeticStrings()
            sage: V = VigenereCryptosystem(A, 24)
            sage: M = "Jack and Jill went up the hill."
            sage: V.encoding(M) == A.encoding(M)
            True
        '''
    def deciphering(self, K, C):
        '''
        Decrypt the ciphertext ``C`` using the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this Vigenere cipher

        - ``C`` -- string (possibly empty) over the string monoid of this
          cryptosystem

        OUTPUT: the plaintext corresponding to the ciphertext ``C``

        EXAMPLES::

            sage: V = VigenereCryptosystem(AlphabeticStrings(), 24)
            sage: K = V.random_key()
            sage: M = V.encoding("Jack and Jill went up the hill.")
            sage: V.deciphering(K, V.enciphering(K, M)) == M
            True
        '''
    def enciphering(self, K, M):
        '''
        Encrypt the plaintext ``M`` using the key ``K``.

        INPUT:

        - ``K`` -- a key belonging to the key space of this Vigenere cipher

        - ``M`` -- string (possibly empty) over the string monoid of this
          cryptosystem

        OUTPUT: the ciphertext corresponding to the plaintext ``M``

        EXAMPLES::

            sage: V = VigenereCryptosystem(AlphabeticStrings(), 24)
            sage: K = V.random_key()
            sage: M = V.encoding("Jack and Jill went up the hill.")
            sage: V.deciphering(K, V.enciphering(K, M)) == M
            True
        '''
