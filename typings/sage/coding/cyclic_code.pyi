from .decoder import Decoder as Decoder
from .encoder import Encoder as Encoder
from .linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeNearestNeighborDecoder as LinearCodeNearestNeighborDecoder, LinearCodeSyndromeDecoder as LinearCodeSyndromeDecoder
from sage.arith.misc import gcd as gcd
from sage.categories.homset import Hom as Hom
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer

def find_generator_polynomial(code, check: bool = True):
    """
    Return a possible generator polynomial for ``code``.

    If the code is cyclic, the generator polynomial is the gcd of all the
    polynomial forms of the codewords. Conversely, if this gcd exactly
    generates the code ``code``, then ``code`` is cyclic.

    If ``check`` is set to ``True``, then it also checks that the code is
    indeed cyclic. Otherwise it doesn't.

    INPUT:

    - ``code`` -- a linear code

    - ``check`` -- whether the cyclicity should be checked

    OUTPUT:

    - the generator polynomial of ``code`` (if the code is cyclic).

    EXAMPLES::

        sage: from sage.coding.cyclic_code import find_generator_polynomial
        sage: C = codes.GeneralizedReedSolomonCode(GF(8, 'a').list()[1:], 4)
        sage: find_generator_polynomial(C)
        x^3 + (a^2 + 1)*x^2 + a*x + a^2 + 1
    """
def bch_bound(n, D, arithmetic: bool = False):
    """
    Return the BCH bound obtained for a cyclic code of length ``n`` and
    defining set ``D``.

    Consider a cyclic code `C`, with defining set `D`, length `n`, and minimum
    distance `d`. We have the following bound, called BCH bound, on `d`:
    `d \\geq \\delta + 1`, where `\\delta` is the length of the longest arithmetic
    sequence (modulo `n`) of elements in `D`.

    That is, if `\\exists c, \\gcd(c,n) = 1` such that
    `\\{l, l+c, \\dots, l + (\\delta - 1) \\times c\\} \\subseteq D`,
    then `d \\geq \\delta + 1` [1]

    The BCH bound is often known in the particular case `c = 1`. The user can
    specify by setting ``arithmetic = False``.

    .. NOTE::

        As this is a specific use case of the BCH bound, it is *not* available
        in the global namespace.
        Call it by using ``sage.coding.cyclic_code.bch_bound``. You can also
        load it into the global namespace by typing
        ``from sage.coding.cyclic_code import bch_bound``.

    INPUT:

    - ``n`` -- integer

    - ``D`` -- list of integers

    - ``arithmetic`` -- (default: ``False``) if it is set to ``True``, then it
      computes the BCH bound using the longest arithmetic sequence definition

    OUTPUT:

    - ``(delta + 1, (l, c))`` -- such that ``delta + 1`` is the BCH bound, and
      ``l, c`` are the parameters of the longest arithmetic sequence
      (see below)

    EXAMPLES::

        sage: n = 15
        sage: D = [14,1,2,11,12]
        sage: sage.coding.cyclic_code.bch_bound(n, D)
        (3, (1, 1))

        sage: n = 15
        sage: D = [14,1,2,11,12]
        sage: sage.coding.cyclic_code.bch_bound(n, D, True)
        (4, (2, 12))
    """

class CyclicCode(AbstractLinearCode):
    """
    Representation of a cyclic code.

    We propose three different ways to create a new :class:`CyclicCode`, either by
    providing:

    - the generator polynomial and the length (1)
    - an existing linear code. In that case, a generator polynomial will be
      computed from the provided linear code's parameters (2)
    - (a subset of) the defining set of the cyclic code (3)

    For now, only single-root cyclic codes are implemented. That is, only
    cyclic codes such that its length `n` and field order `q` are coprimes.

    Depending on which behaviour you want, you need to specify the names of the
    arguments to :class:`CyclicCode`. See EXAMPLES section below for details.

    INPUT:

    - ``generator_pol`` -- (default: ``None``) the generator polynomial
      of ``self``; that is, the highest-degree monic polynomial which divides
      every polynomial representation of a codeword in ``self``

    - ``length`` -- (default: ``None``) the length of ``self``; it has to be
      bigger than the degree of ``generator_pol``

    - ``code`` -- (default: ``None``) a linear code

    - ``check`` -- boolean (default: ``False``);  whether the cyclicity of
      ``self`` must be checked while finding the generator polynomial. See
      :meth:`find_generator_polynomial` for details.

    - ``D`` -- (default: ``None``) a list of integers between ``0`` and
      ``length-1``, corresponding to (a subset of) the defining set of the code.
      Will be modified if it is not cyclotomic-closed.

    - ``field`` -- (default: ``None``) the base field of ``self``

    - ``primitive_root`` -- (default: ``None``) the primitive root of
      the splitting field which contains the roots of the generator polynomial.
      It has to be of multiplicative order ``length`` over this field.
      If the splitting field is not ``field``, it also have to be a polynomial
      in ``zx``, where ``x`` is the degree of the extension over the prime
      field. For instance, over ``GF(16)``, it must be a polynomial in ``z4``.

    EXAMPLES:

    We can construct a :class:`CyclicCode` object using three different methods.
    First (1), we provide a generator polynomial and a code length::

        sage: F.<x> = GF(2)[]
        sage: n = 7
        sage: g = x ** 3 + x + 1
        sage: C = codes.CyclicCode(generator_pol=g, length=n)
        sage: C
        [7, 4] Cyclic Code over GF(2)

    We can also provide a code (2). In that case, the program will try to
    extract a generator polynomial (see :meth:`find_generator_polynomial`
    for details)::

        sage: C = codes.GeneralizedReedSolomonCode(GF(8, 'a').list()[1:], 4)
        sage: Cc = codes.CyclicCode(code = C)
        sage: Cc
        [7, 4] Cyclic Code over GF(8)

    Finally, we can give (a subset of) a defining set for the code (3).
    In this case, the generator polynomial will be computed::

        sage: F = GF(16, 'a')
        sage: n = 15
        sage: Cc = codes.CyclicCode(length=n, field=F, D = [1,2])
        sage: Cc
        [15, 13] Cyclic Code over GF(16)
    """
    def __init__(self, generator_pol=None, length=None, code=None, check: bool = True, D=None, field=None, primitive_root=None) -> None:
        """
        TESTS:

        If one provides a generator polynomial and a length, we check that
        the length is bigger than the degree of the polynomial::

            sage: F.<x> = GF(2)[]
            sage: n = 2
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            Traceback (most recent call last):
            ...
            ValueError: Only cyclic codes whose length and field order are coprimes are implemented.

        We also check that the polynomial is defined over a finite field::

            sage: F.<x> = RR[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            Traceback (most recent call last):
            ...
            ValueError: The generator polynomial must be defined over a finite field.

        And we check that the generator polynomial divides `x^{n} - 1`,
        where `n` is provided length::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 2 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            Traceback (most recent call last):
            ...
            ValueError: Provided polynomial must divide x^n - 1, where n is the provided length.

        In the case of a code is passed as argument, if it's not possible
        to extract a generator polynomial, an exception is raised::

            sage: G = matrix(GF(2), [[1, 1, 1], [0, 1, 1]])
            sage: C = codes.LinearCode(G)
            sage: Cc = codes.CyclicCode(code=C)
            Traceback (most recent call last):
            ...
            ValueError: The code is not cyclic.

        If the ``primitive_root`` does not lie in an extension of ``field``,
        or is not a primitive `n`-th root of unity, then
        an exception is raised::

            sage: F = GF(2)
            sage: n = 15
            sage: Dset = [1, 2, 4, 8]
            sage: alpha = GF(3).one()
            sage: Cc = codes.CyclicCode(D=Dset, field=F, length=n, primitive_root=alpha)
            Traceback (most recent call last):
            ...
            ValueError: primitive_root must belong to an extension of the base field
            sage: alpha = GF(16).one()
            sage: Cc = codes.CyclicCode(D=Dset, field=F, length=n, primitive_root=alpha)
            Traceback (most recent call last):
            ...
            ValueError: primitive_root must be a primitive n-th root of unity
            sage: alpha = GF(32).gen()
            sage: Cc = codes.CyclicCode(D=Dset, field=F, length=n, primitive_root=alpha)
            Traceback (most recent call last):
            ...
            ValueError: primitive_root must be a primitive n-th root of unity
        """
    def __contains__(self, word) -> bool:
        """
        Return ``True`` if ``word`` belongs to ``self``, ``False`` otherwise.

        INPUT:

        - ``word`` -- the word to test

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: c = vector(GF(2), (1, 1, 1, 0, 0, 1, 0))
            sage: c in C
            True
        """
    def __eq__(self, other):
        """
        Test equality between CyclicCode objects.

        INPUT:

        - ``other`` -- the code to test

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C1 = codes.CyclicCode(generator_pol=g, length=n)
            sage: C2 = codes.CyclicCode(generator_pol=g, length=n)
            sage: C1 == C2
            True
        """
    def generator_polynomial(self):
        """
        Return the generator polynomial of ``self``.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: C.generator_polynomial()
            x^3 + x + 1
        """
    def field_embedding(self):
        """
        Return the base field embedding into the splitting field.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: C.field_embedding()
            Ring morphism:
              From: Finite Field of size 2
              To:   Finite Field in z3 of size 2^3
              Defn: 1 |--> 1
        """
    def defining_set(self, primitive_root=None):
        """
        Return the set of exponents of the roots of ``self``'s generator
        polynomial over the extension field.

        Of course, it depends on the choice of the primitive root of
        the splitting field.

        INPUT:

        - ``primitive_root`` -- (optional) a primitive root of the extension
          field

        EXAMPLES:

        We provide a defining set at construction time::

            sage: F = GF(16, 'a')
            sage: n = 15
            sage: C = codes.CyclicCode(length=n, field=F, D=[1,2])
            sage: C.defining_set()
            [1, 2]

        If the defining set was provided by the user, it might have been
        expanded at construction time. In this case, the expanded defining set
        will be returned::

            sage: C = codes.CyclicCode(length=13, field=F, D=[1, 2])
            sage: C.defining_set()
            [1, 2, 3, 5, 6, 9]

        If a generator polynomial was passed at construction time,
        the defining set is computed using this polynomial::

            sage: R.<x> = F[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: C.defining_set()
            [1, 2, 4]

        Both operations give the same result::

            sage: C1 = codes.CyclicCode(length=n, field=F, D=[1, 2, 4])
            sage: C1.generator_polynomial() == g
            True

        Another one, in a reversed order::

            sage: n = 13
            sage: C1 = codes.CyclicCode(length=n, field=F, D=[1, 2])
            sage: g = C1.generator_polynomial()
            sage: C2 = codes.CyclicCode(generator_pol=g, length=n)
            sage: C1.defining_set() == C2.defining_set()
            True
        """
    def primitive_root(self):
        """
        Return the primitive root of the splitting field that is used
        to build the defining set of the code.

        If it has not been specified by the user, it is set by default with the
        output of the ``zeta`` method of the splitting field.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: C.primitive_root()
            z3

            sage: F = GF(16, 'a')
            sage: n = 15
            sage: a = F.gen()
            sage: Cc = codes.CyclicCode(length=n, field=F, D=[1,2],
            ....:                       primitive_root=a^2 + 1)
            sage: Cc.primitive_root()
            a^2 + 1
        """
    @cached_method
    def check_polynomial(self):
        """
        Return the check polynomial of ``self``.

        Let `C` be a cyclic code of length `n` and `g` its generator
        polynomial. The following: `h = \\frac{x^n - 1}{g(x)}` is called `C`'s
        check polynomial.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: h = C.check_polynomial()
            sage: h == (x**n - 1)/C.generator_polynomial()
            True
        """
    @cached_method
    def parity_check_matrix(self):
        """
        Return the parity check matrix of ``self``.

        The parity check matrix of a linear code `C` corresponds to the
        generator matrix of the dual code of `C`.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: C.parity_check_matrix()
            [1 0 1 1 1 0 0]
            [0 1 0 1 1 1 0]
            [0 0 1 0 1 1 1]
        """
    def bch_bound(self, arithmetic: bool = False):
        """
        Return the BCH bound of ``self`` which is a bound on ``self``
        minimum distance.

        See :meth:`sage.coding.cyclic_code.bch_bound` for details.

        INPUT:

        - ``arithmetic`` -- (default: ``False``) if it is set to ``True``,
          then it computes the BCH bound using the longest arithmetic sequence
          definition

        OUTPUT:

        - ``(delta + 1, (l, c))`` -- such that ``delta + 1`` is the BCH bound,
          and ``l, c`` are the parameters of the largest arithmetic sequence

        EXAMPLES::

            sage: F = GF(16, 'a')
            sage: n = 15
            sage: D = [14,1,2,11,12]
            sage: C = codes.CyclicCode(field=F, length=n, D = D)
            sage: C.bch_bound()
            (3, (1, 1))

            sage: F = GF(16, 'a')
            sage: n = 15
            sage: D = [14,1,2,11,12]
            sage: C = codes.CyclicCode(field=F, length=n, D = D)
            sage: C.bch_bound(True)
            (4, (2, 12))
        """
    def surrounding_bch_code(self):
        """
        Return the surrounding BCH code of ``self``.

        EXAMPLES::

            sage: C = codes.CyclicCode(field=GF(2), length=63, D=[1, 7, 17])
            sage: C.dimension()
            45
            sage: CC = C.surrounding_bch_code()
            sage: CC
            [63, 51] BCH Code over GF(2) with designed distance 3
            sage: all(r in CC for r in C.generator_matrix())
            True
        """

class CyclicCodePolynomialEncoder(Encoder):
    """
    An encoder encoding polynomials into codewords.

    Let `C` be a cyclic code over some finite field `F`,
    and let `g` be its generator polynomial.

    This encoder encodes any polynomial `p \\in F[x]_{<k}` by computing
    `c = p g` and returning the vector of its coefficients.

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: F.<x> = GF(2)[]
        sage: n = 7
        sage: g = x ** 3 + x + 1
        sage: C = codes.CyclicCode(generator_pol=g, length=n)
        sage: E = codes.encoders.CyclicCodePolynomialEncoder(C)
        sage: E
        Polynomial-style encoder for [7, 4] Cyclic Code over GF(2)
    """
    def __init__(self, code) -> None:
        """
        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodePolynomialEncoder(C)
            sage: E
            Polynomial-style encoder for [7, 4] Cyclic Code over GF(2)
        """
    def __eq__(self, other):
        """
        Test equality between CyclicCodePolynomialEncoder objects.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E1 = codes.encoders.CyclicCodePolynomialEncoder(C)
            sage: E2 = codes.encoders.CyclicCodePolynomialEncoder(C)
            sage: E1 == E2
            True
        """
    def encode(self, p):
        """
        Transform `p` into an element of the associated code of ``self``.

        INPUT:

        - ``p`` -- a polynomial from ``self`` message space

        OUTPUT: a codeword in associated code of ``self``

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodePolynomialEncoder(C)
            sage: m = x ** 2 + 1
            sage: E.encode(m)
            (1, 1, 1, 0, 0, 1, 0)
        """
    def unencode_nocheck(self, c):
        """
        Return the message corresponding to ``c``.
        Does not check if ``c`` belongs to the code.

        INPUT:

        - ``c`` -- a vector with the same length as the code

        OUTPUT: an element of the message space

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodePolynomialEncoder(C)
            sage: c = vector(GF(2), (1, 1, 1, 0, 0, 1, 0))
            sage: E.unencode_nocheck(c)
            x^2 + 1
        """
    def message_space(self):
        """
        Return the message space of ``self``.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodePolynomialEncoder(C)
            sage: E.message_space()                                                     # needs sage.libs.ntl
            Univariate Polynomial Ring in x over Finite Field of size 2 (using GF2X)
        """

class CyclicCodeVectorEncoder(Encoder):
    """
    An encoder which can encode vectors into codewords.

    Let `C` be a cyclic code over some finite field `F`,
    and let `g` be its generator polynomial.

    Let `m = (m_1, m_2, \\dots, m_k)` be a vector in `F^{k}`.
    This codeword can be seen as a polynomial over `F[x]`, as follows:
    `P_m = \\Sigma_{i=0}^{k-1} m_i \\times x^i`.

    To encode `m`, this encoder does the multiplication `P_m  g`.

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: F.<x> = GF(2)[]
        sage: n = 7
        sage: g = x ** 3 + x + 1
        sage: C = codes.CyclicCode(generator_pol=g, length=n)
        sage: E = codes.encoders.CyclicCodeVectorEncoder(C)
        sage: E
        Vector-style encoder for [7, 4] Cyclic Code over GF(2)
    """
    def __init__(self, code) -> None:
        """

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: E
            Vector-style encoder for [7, 4] Cyclic Code over GF(2)
        """
    def __eq__(self, other):
        """
        Test equality between CyclicCodeVectorEncoder objects.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E1 = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: E2 = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: E1 == E2
            True
        """
    def encode(self, m):
        """
        Transform `m` into an element of the associated code of ``self``.

        INPUT:

        - ``m`` -- an element from ``self``'s message space

        OUTPUT: a codeword in the associated code of ``self``

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: m = vector(GF(2), (1, 0, 1, 0))
            sage: E.encode(m)
            (1, 1, 1, 0, 0, 1, 0)
        """
    def unencode_nocheck(self, c):
        """
        Return the message corresponding to ``c``.
        Does not check if ``c`` belongs to the code.

        INPUT:

        - ``c`` -- a vector with the same length as the code

        OUTPUT: an element of the message space

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: c = vector(GF(2), (1, 1, 1, 0, 0, 1, 0))
            sage: E.unencode_nocheck(c)
            (1, 0, 1, 0)
        """
    @cached_method
    def generator_matrix(self):
        """
        Return a generator matrix of ``self``.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: E.generator_matrix()
            [1 1 0 1 0 0 0]
            [0 1 1 0 1 0 0]
            [0 0 1 1 0 1 0]
            [0 0 0 1 1 0 1]
        """
    def message_space(self):
        """
        Return the message space of ``self``.

        EXAMPLES::

            sage: F.<x> = GF(2)[]
            sage: n = 7
            sage: g = x ** 3 + x + 1
            sage: C = codes.CyclicCode(generator_pol=g, length=n)
            sage: E = codes.encoders.CyclicCodeVectorEncoder(C)
            sage: E.message_space()
            Vector space of dimension 4 over Finite Field of size 2
        """

class CyclicCodeSurroundingBCHDecoder(Decoder):
    """
    A decoder which decodes through the surrounding BCH code of the cyclic
    code.

    INPUT:

    - ``code`` -- the associated code of this decoder

    - ``**kwargs`` -- all extra arguments are forwarded to the BCH decoder

    EXAMPLES::

        sage: C = codes.CyclicCode(field=GF(16), length=15, D=[14, 1, 2, 11, 12])
        sage: D = codes.decoders.CyclicCodeSurroundingBCHDecoder(C)
        sage: D
        Decoder through the surrounding BCH code of the [15, 10] Cyclic Code over GF(16)
    """
    def __init__(self, code, **kwargs) -> None:
        """

        EXAMPLES::

            sage: C = codes.CyclicCode(field=GF(16), length=15, D=[14, 1, 2, 11, 12])
            sage: D = codes.decoders.CyclicCodeSurroundingBCHDecoder(C)
            sage: D
            Decoder through the surrounding BCH code of the [15, 10] Cyclic Code over GF(16)
        """
    def __eq__(self, other):
        """
        Test equality between CyclicCodeSurroundingBCHDecoder objects.

        EXAMPLES::

            sage: C = codes.CyclicCode(field=GF(16), length=15, D=[14, 1, 2, 11, 12])
            sage: D1 = C.decoder()
            sage: D2 = C.decoder()
            sage: D1 == D2
            True
        """
    def bch_code(self):
        """
        Return the surrounding BCH code of
        :meth:`sage.coding.encoder.Encoder.code`.

        EXAMPLES::

            sage: C = codes.CyclicCode(field=GF(16), length=15, D=[14, 1, 2, 11, 12])
            sage: D = codes.decoders.CyclicCodeSurroundingBCHDecoder(C)
            sage: D.bch_code()
            [15, 12] BCH Code over GF(16) with designed distance 4
        """
    def bch_decoder(self):
        """
        Return the decoder that will be used over the surrounding BCH code.

        EXAMPLES::

            sage: C = codes.CyclicCode(field=GF(16), length=15, D=[14, 1, 2, 11, 12])
            sage: D = codes.decoders.CyclicCodeSurroundingBCHDecoder(C)
            sage: D.bch_decoder()
            Decoder through the underlying GRS code of [15, 12] BCH Code
             over GF(16) with designed distance 4
        """
    def decode_to_code(self, y):
        """
        Decodes ``r`` to an element in :meth:`sage.coding.encoder.Encoder.code`.

        EXAMPLES::

            sage: F = GF(16, 'a')
            sage: C = codes.CyclicCode(field=F, length=15, D=[14, 1, 2, 11, 12])
            sage: a = F.gen()
            sage: D = codes.decoders.CyclicCodeSurroundingBCHDecoder(C)
            sage: y = vector(F, [0, a^3, a^3 + a^2 + a, 1, a^2 + 1, a^3 + a^2 + 1,
            ....:                a^3 + a^2 + a, a^3 + a^2 + a, a^2 + a, a^2 + 1,
            ....:                a^2 + a + 1, a^3 + 1, a^2, a^3 + a, a^3 + a])
            sage: D.decode_to_code(y) in C
            True
        """
    def decoding_radius(self):
        """
        Return maximal number of errors that ``self`` can decode.

        EXAMPLES::

            sage: C = codes.CyclicCode(field=GF(16), length=15, D=[14, 1, 2, 11, 12])
            sage: D = codes.decoders.CyclicCodeSurroundingBCHDecoder(C)
            sage: D.decoding_radius()
            1
        """
