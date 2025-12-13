from _typeshed import Incomplete
from sage.arith.misc import gcd as gcd, power_mod as power_mod, xgcd as xgcd
from sage.crypto.cryptosystem import PublicKeyCryptosystem as PublicKeyCryptosystem
from sage.crypto.util import is_blum_prime as is_blum_prime, least_significant_bits as least_significant_bits, random_blum_prime as random_blum_prime
from sage.functions.log import log as log
from sage.functions.other import Function_floor as Function_floor
from sage.monoids.string_monoid import BinaryStrings as BinaryStrings
from sage.rings.finite_rings.integer_mod_ring import IntegerModFactory as IntegerModFactory

floor: Incomplete
IntegerModRing: Incomplete

class BlumGoldwasser(PublicKeyCryptosystem):
    '''
    The Blum-Goldwasser probabilistic public-key encryption scheme.

    The Blum-Goldwasser encryption and decryption algorithms as described in
    :func:`encrypt() <BlumGoldwasser.encrypt>` and
    :func:`decrypt() <BlumGoldwasser.decrypt>`, respectively, make use of the
    least significant bit of a binary string. A related concept is the `k`
    least significant bits of a binary string. For example, given a positive
    integer `n`, let `b = b_0 b_1 \\cdots b_{m-1}` be the binary representation
    of `n` so that `b` is a binary string of length `m`. Then the least
    significant bit of `n` is `b_{m-1}`. If `0 < k \\leq m`, then the `k` least
    significant bits of `n` are `b_{m-1-k} b_{m-k} \\cdots b_{m-1}`. The least
    significant bit of an integer is also referred to as its parity bit,
    because this bit determines whether the integer is even or odd. In the
    following example, we obtain the least significant bit of an integer::

        sage: n = 123
        sage: b = n.binary(); b
        \'1111011\'
        sage: n % 2
        1
        sage: b[-1]
        \'1\'

    Now find the 4 least significant bits of the integer `n = 123`::

        sage: b
        \'1111011\'
        sage: b[-4:]
        \'1011\'

    The last two examples could be worked through as follows::

        sage: from sage.crypto.util import least_significant_bits
        sage: least_significant_bits(123, 1)
        [1]
        sage: least_significant_bits(123, 4)
        [1, 0, 1, 1]

    EXAMPLES:

    The following encryption/decryption example is taken from Example 8.57,
    pages 309--310 of [MvOV1996]_::

        sage: # needs sage.symbolic
        sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
        sage: bg = BlumGoldwasser(); bg
        The Blum-Goldwasser public-key encryption scheme.
        sage: p = 499; q = 547
        sage: pubkey = bg.public_key(p, q); pubkey
        272953
        sage: prikey = bg.private_key(p, q); prikey
        (499, 547, -57, 52)
        sage: P = "10011100000100001100"
        sage: C = bg.encrypt(P, pubkey, seed=159201); C
        ([[0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]], 139680)
        sage: M = bg.decrypt(C, prikey); M
        [[1, 0, 0, 1], [1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]]
        sage: M = "".join(str(x) for x in flatten(M)); M
        \'10011100000100001100\'
        sage: M == P
        True

    Generate a pair of random public/private keys. Use the public key to
    encrypt a plaintext. Then decrypt the resulting ciphertext using the
    private key. Finally, compare the decrypted message with the original
    plaintext. ::

        sage: # needs sage.libs.pari sage.symbolic
        sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
        sage: from sage.crypto.util import bin_to_ascii
        sage: bg = BlumGoldwasser()
        sage: pubkey, prikey = bg.random_key(10**4, 10**6)
        sage: P = "A fixed plaintext."
        sage: C = bg.encrypt(P, pubkey)
        sage: M = bg.decrypt(C, prikey)
        sage: bin_to_ascii(flatten(M)) == P
        True

    If `(p, q, a, b)` is a private key, then `n = pq` is the corresponding
    public key. Furthermore, we have `\\gcd(p, q) = ap + bq = 1`. ::

        sage: p, q, a, b = prikey                                                       # needs sage.symbolic
        sage: pubkey == p * q                                                           # needs sage.symbolic
        True
        sage: gcd(p, q) == a*p + b*q == 1                                               # needs sage.symbolic
        True
    '''
    def __init__(self) -> None:
        """
        Construct the Blum-Goldwasser public-key encryption scheme.

        OUTPUT:

        - A ``BlumGoldwasser`` object representing the Blum-Goldwasser
          public-key encryption scheme.

        See the class docstring of ``BlumGoldwasser`` for detailed
        documentation.

        EXAMPLES::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: bg == loads(dumps(bg))
            True
        """
    def __eq__(self, other):
        """
        Compare this ``BlumGoldwasser`` object with ``other``.

        INPUT:

        - ``other`` -- a ``BlumGoldwasser`` object

        OUTPUT: ``True`` if both ``self`` and ``other`` are ``BlumGoldwasser``
        objects; ``False`` otherwise

        Two objects are ``BlumGoldwasser`` objects if their string
        representations are the same.

        EXAMPLES::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg1 = BlumGoldwasser()
            sage: bg2 = BlumGoldwasser()
            sage: bg1 == bg2
            True
        """
    def decrypt(self, C, K):
        """
        Apply the Blum-Goldwasser scheme to decrypt the ciphertext ``C``
        using the private key ``K``.

        INPUT:

        - ``C`` -- a ciphertext resulting from encrypting a plaintext using
          the Blum-Goldwasser encryption algorithm. The ciphertext `C` must
          be of the form `C = (c_1, c_2, \\dots, c_t, x_{t+1})`. Each `c_i`
          is a sub-block of binary string and `x_{t+1}` is the result of the
          `t+1`-th iteration of the Blum-Blum-Shub algorithm.

        - ``K`` -- a private key `(p, q, a, b)` where `p` and `q` are
          distinct Blum primes and `\\gcd(p, q) = ap + bq = 1`

        OUTPUT:

        - The plaintext resulting from decrypting the ciphertext ``C`` using
          the Blum-Goldwasser decryption algorithm.

        ALGORITHM:

        The Blum-Goldwasser decryption algorithm is described in Algorithm
        8.56, page 309 of [MvOV1996]_. The algorithm works as follows:

        #. Let `C` be the ciphertext `C = (c_1, c_2, \\dots, c_t, x_{t+1})`.
           Then `t` is the number of ciphertext sub-blocks and `h` is the
           length of each binary string sub-block `c_i`.
        #. Let `(p, q, a, b)` be the private key whose corresponding
           public key is `n = pq`. Note that `\\gcd(p, q) = ap + bq = 1`.
        #. Compute `d_1 = ((p + 1) / 4)^{t+1} \\bmod{(p - 1)}`.
        #. Compute `d_2 = ((q + 1) / 4)^{t+1} \\bmod{(q - 1)}`.
        #. Let `u = x_{t+1}^{d_1} \\bmod p`.
        #. Let `v = x_{t+1}^{d_2} \\bmod q`.
        #. Compute `x_0 = vap + ubq \\bmod n`.
        #. For `i` from 1 to `t`, do:

           #. Compute `x_i = x_{t-1}^2 \\bmod n`.
           #. Let `p_i` be the `h` least significant bits of `x_i`.
           #. Compute `m_i = p_i \\oplus c_i`.

        #. The plaintext is `m = m_1 m_2 \\cdots m_t`.

        EXAMPLES:

        The following decryption example is taken from Example 8.57, pages
        309--310 of [MvOV1996]_. Here we decrypt a binary string::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: p = 499; q = 547
            sage: C = ([[0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]], 139680)
            sage: K = bg.private_key(p, q); K
            (499, 547, -57, 52)
            sage: P = bg.decrypt(C, K); P
            [[1, 0, 0, 1], [1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]]

        Convert the plaintext sub-blocks into a binary string::

            sage: bin = BinaryStrings()
            sage: bin(flatten(P))
            10011100000100001100

        Decrypt a longer ciphertext and convert the resulting plaintext
        into an ASCII string::

            sage: # needs sage.libs.pari
            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: from sage.crypto.util import bin_to_ascii
            sage: bg = BlumGoldwasser()
            sage: p = 78307; q = 412487
            sage: K = bg.private_key(p, q)
            sage: C = ([[1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            ....:       [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
            ....:       [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            ....:       [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
            ....:       [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            ....:       [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            ....:       [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            ....:       [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            ....:       [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            ....:       [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            ....:       [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            ....:       [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
            ....:       [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]], 3479653279)
            sage: P = bg.decrypt(C, K)
            sage: bin_to_ascii(flatten(P))
            'Blum-Goldwasser encryption'

        TESTS:

        The private key `K = (p, q, a, b)` must be such that `p` and `q` are
        distinct Blum primes. Even if `p` and `q` pass this criterion, they
        must also satisfy the requirement `\\gcd(p, q) = ap + bq = 1`. ::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: C = ([[0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]], 139680)
            sage: K = (7, 7, 1, 2)
            sage: bg.decrypt(C, K)
            Traceback (most recent call last):
            ...
            ValueError: p and q must be distinct Blum primes.
            sage: K = (7, 23, 1, 2)
            sage: bg.decrypt(C, K)
            Traceback (most recent call last):
            ...
            ValueError: a and b must satisfy gcd(p, q) = ap + bq = 1.
            sage: K = (11, 29, 8, -3)
            sage: bg.decrypt(C, K)
            Traceback (most recent call last):
            ...
            ValueError: p and q must be distinct Blum primes.
        """
    def encrypt(self, P, K, seed=None):
        '''
        Apply the Blum-Goldwasser scheme to encrypt the plaintext ``P`` using
        the public key ``K``.

        INPUT:

        - ``P`` -- a non-empty string of plaintext. The string ``""`` is
          an empty string, whereas ``" "`` is a string consisting of one
          white space character. The plaintext can be a binary string or
          a string of ASCII characters. Where ``P`` is an ASCII string, then
          ``P`` is first encoded as a binary string prior to encryption.

        - ``K`` -- a public key, which is the product of two Blum primes

        - ``seed`` -- (default: ``None``) if `p` and `q` are Blum primes and
          `n = pq` is a public key, then ``seed`` is a quadratic residue in
          the multiplicative group `(\\ZZ/n\\ZZ)^{\\ast}`. If ``seed=None``,
          then the function would generate its own random quadratic residue
          in `(\\ZZ/n\\ZZ)^{\\ast}`. Where a value for ``seed`` is provided,
          it is your responsibility to ensure that the seed is a
          quadratic residue in the multiplicative group `(\\ZZ/n\\ZZ)^{\\ast}`.

        OUTPUT:

        - The ciphertext resulting from encrypting ``P`` using the public
          key ``K``. The ciphertext `C` is of the form
          `C = (c_1, c_2, \\dots, c_t, x_{t+1})`. Each `c_i` is a
          sub-block of binary string and `x_{t+1}` is the result of the
          `t+1`-th iteration of the Blum-Blum-Shub algorithm.

        ALGORITHM:

        The Blum-Goldwasser encryption algorithm is described in Algorithm
        8.56, page 309 of [MvOV1996]_. The algorithm works as follows:

        #. Let `n` be a public key, where `n = pq` is the product of two
           distinct Blum primes `p` and `q`.
        #. Let `k = \\lfloor \\log_2(n) \\rfloor` and
           `h = \\lfloor \\log_2(k) \\rfloor`.
        #. Let `m = m_1 m_2 \\cdots m_t` be the message (plaintext) where
           each `m_i` is a binary string of length `h`.
        #. Choose a random seed `x_0`, which is a quadratic residue in
           the multiplicative group `(\\ZZ/n\\ZZ)^{\\ast}`. That is, choose
           a random `r \\in (\\ZZ/n\\ZZ)^{\\ast}` and compute
           `x_0 = r^2 \\bmod n`.
        #. For `i` from 1 to `t`, do:

           #. Let `x_i = x_{i-1}^2 \\bmod n`.
           #. Let `p_i` be the `h` least significant bits of `x_i`.
           #. Let `c_i = p_i \\oplus m_i`.

        #. Compute `x_{t+1} = x_t^2 \\bmod n`.
        #. The ciphertext is `c = (c_1, c_2, \\dots, c_t, x_{t+1})`.

        The value `h` in the algorithm is the sub-block length. If the
        binary string representing the message cannot be divided into blocks
        of length `h` each, then other sub-block lengths would be used
        instead. The sub-block lengths to fall back on are in the
        following order: 16, 8, 4, 2, 1.

        EXAMPLES:

        The following encryption example is taken from Example 8.57,
        pages 309--310 of [MvOV1996]_. Here, we encrypt a binary
        string::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: p = 499; q = 547; n = p * q
            sage: P = "10011100000100001100"
            sage: C = bg.encrypt(P, n, seed=159201); C                                  # needs sage.symbolic
            ([[0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]], 139680)

        Convert the ciphertext sub-blocks into a binary string::

            sage: bin = BinaryStrings()
            sage: bin(flatten(C[0]))                                                    # needs sage.symbolic
            00100000110011100100

        Now encrypt an ASCII string. The result is random; no seed is
        provided to the encryption function so the function generates its
        own random seed::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: K = 32300619509
            sage: P = "Blum-Goldwasser encryption"
            sage: bg.encrypt(P, K)  # random                                            # needs sage.symbolic
            ([[1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0], \\\n            [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1], \\\n            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0], \\\n            [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1], \\\n            [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0], \\\n            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], \\\n            [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0], \\\n            [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1], \\\n            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], \\\n            [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1], \\\n            [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1], \\\n            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0], \\\n            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]], 3479653279)

        TESTS:

        The plaintext cannot be an empty string. ::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: bg.encrypt("", 3)
            Traceback (most recent call last):
            ...
            ValueError: The plaintext cannot be an empty string.
        '''
    def private_key(self, p, q):
        """
        Return the Blum-Goldwasser private key corresponding to the
        distinct Blum primes ``p`` and ``q``.

        INPUT:

        - ``p`` -- a Blum prime

        - ``q`` -- a Blum prime

        OUTPUT: the Blum-Goldwasser private key `(p, q, a, b)` where
        `\\gcd(p, q) = ap + bq = 1`

        Both ``p`` and ``q`` must be distinct Blum primes. Let `p` be a
        positive prime. Then `p` is a Blum prime if `p` is congruent to 3
        modulo 4, i.e. `p \\equiv 3 \\pmod{4}`.

        EXAMPLES:

        Obtain two distinct Blum primes and compute the Blum-Goldwasser
        private key corresponding to those two Blum primes::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: from sage.crypto.util import is_blum_prime
            sage: bg = BlumGoldwasser()
            sage: P = primes_first_n(10); P                                             # needs sage.libs.pari
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            sage: [is_blum_prime(_) for _ in P]                                         # needs sage.libs.pari
            [False, True, False, True, True, False, False, True, True, False]
            sage: bg.private_key(19, 23)
            (19, 23, -6, 5)

        Choose two distinct random Blum primes, compute the Blum-Goldwasser
        private key corresponding to those two primes, and test that the
        resulting private key `(p, q, a, b)` satisfies
        `\\gcd(p, q) = ap + bq = 1`::

            sage: # needs sage.libs.pari
            sage: from sage.crypto.util import random_blum_prime
            sage: p = random_blum_prime(10**4, 10**5)
            sage: q = random_blum_prime(10**4, 10**5)
            sage: while q == p:
            ....:     q = random_blum_prime(10**4, 10**5)
            sage: p, q, a, b = bg.private_key(p, q)
            sage: gcd(p, q) == a*p + b*q == 1
            True

        TESTS:

        Both of the input ``p`` and ``q`` must be distinct Blum primes. ::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: bg.private_key(78307, 78307)
            Traceback (most recent call last):
            ...
            ValueError: p and q must be distinct Blum primes.
            sage: bg.private_key(7, 4)
            Traceback (most recent call last):
            ...
            ValueError: p and q must be distinct Blum primes.
        """
    def public_key(self, p, q):
        """
        Return the Blum-Goldwasser public key corresponding to the
        distinct Blum primes ``p`` and ``q``.

        INPUT:

        - ``p`` -- a Blum prime

        - ``q`` -- a Blum prime

        OUTPUT: the Blum-Goldwasser public key `n = pq`

        Both ``p`` and ``q`` must be distinct Blum primes. Let `p` be a
        positive prime. Then `p` is a Blum prime if `p` is congruent to 3
        modulo 4, i.e. `p \\equiv 3 \\pmod{4}`.

        EXAMPLES:

        Obtain two distinct Blum primes and compute the Blum-Goldwasser
        public key corresponding to those two Blum primes::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: from sage.crypto.util import is_blum_prime
            sage: bg = BlumGoldwasser()
            sage: P = primes_first_n(10); P                                             # needs sage.libs.pari
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            sage: [is_blum_prime(_) for _ in P]                                         # needs sage.libs.pari
            [False, True, False, True, True, False, False, True, True, False]
            sage: bg.public_key(3, 7)
            21

        Choose two distinct random Blum primes, compute the Blum-Goldwasser
        public key corresponding to those two primes, and test that the
        public key factorizes into Blum primes::

            sage: # needs sage.libs.pari
            sage: from sage.crypto.util import random_blum_prime
            sage: p = random_blum_prime(10**4, 10**5)
            sage: q = random_blum_prime(10**4, 10**5)
            sage: while q == p:
            ....:     q = random_blum_prime(10**4, 10**5)
            ...
            sage: n = bg.public_key(p, q)
            sage: f = factor(n)
            sage: is_blum_prime(f[0][0]); is_blum_prime(f[1][0])
            True
            True
            sage: p * q == f[0][0] * f[1][0]
            True

        TESTS:

        The input ``p`` and ``q`` must be distinct Blum primes. ::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: bg.public_key(3, 3)
            Traceback (most recent call last):
            ...
            ValueError: p and q must be distinct Blum primes.
            sage: bg.public_key(23, 29)
            Traceback (most recent call last):
            ...
            ValueError: p and q must be distinct Blum primes.
        """
    def random_key(self, lbound, ubound, ntries: int = 100):
        '''
        Return a pair of random public and private keys.

        INPUT:

        - ``lbound`` -- positive integer; the lower bound on how small each
          random Blum prime `p` and `q` can be. So we have
          ``0 < lower_bound <= p, q <= upper_bound``. The lower bound must
          be distinct from the upper bound.

        - ``ubound`` -- positive integer; the upper bound on how large each
          random Blum prime `p` and `q` can be. So we have
          ``0 < lower_bound <= p, q <= upper_bound``. The lower bound must
          be distinct from the upper bound.

        - ``ntries`` -- (default: ``100``) the number of attempts to generate
          a random public/private key pair. If ``ntries`` is a positive
          integer, then perform that many attempts at generating a random
          public/private key pair.

        OUTPUT:

        - A random public key and its corresponding private key. Each
          randomly chosen `p` and `q` are guaranteed to be Blum primes. The
          public key is `n = pq`, and the private key is `(p, q, a, b)` where
          `\\gcd(p, q) = ap + bq = 1`.

        ALGORITHM:

        The key generation algorithm is described in Algorithm 8.55,
        page 308 of [MvOV1996]_. The algorithm works as follows:

        #. Let `p` and `q` be distinct large random primes, each congruent
           to 3 modulo 4. That is, `p` and `q` are Blum primes.
        #. Let `n = pq` be the product of `p` and `q`.
        #. Use the extended Euclidean algorithm to compute integers `a` and
           `b` such that `\\gcd(p, q) = ap + bq = 1`.
        #. The public key is `n` and the corresponding private key is
           `(p, q, a, b)`.

        .. NOTE::

            Beware that there might not be any primes between the lower and
            upper bounds. So make sure that these two bounds are
            "sufficiently" far apart from each other for there to be primes
            congruent to 3 modulo 4. In particular, there should
            be at least two distinct primes within these bounds, each prime
            being congruent to 3 modulo 4.

        EXAMPLES:

        Choosing a random pair of public and private keys. We then test to see
        if they satisfy the requirements of the Blum-Goldwasser scheme::

            sage: # needs sage.libs.pari
            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: from sage.crypto.util import is_blum_prime
            sage: bg = BlumGoldwasser()
            sage: pubkey, prikey = bg.random_key(10**4, 10**5)
            sage: p, q, a, b = prikey
            sage: is_blum_prime(p); is_blum_prime(q)
            True
            True
            sage: p == q
            False
            sage: pubkey == p*q
            True
            sage: gcd(p, q) == a*p + b*q == 1
            True

        TESTS:

        Make sure that there is at least one Blum prime between the lower and
        upper bounds. In the following example, we have ``lbound=24`` and
        ``ubound=30`` with 29 being the only prime within those bounds. But
        29 is not a Blum prime. ::

            sage: from sage.crypto.public_key.blum_goldwasser import BlumGoldwasser
            sage: bg = BlumGoldwasser()
            sage: pubkey, privkey = bg.random_key(24, 30)                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: No Blum primes within the specified closed interval.
        '''
