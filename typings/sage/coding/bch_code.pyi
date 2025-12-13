from .cyclic_code import CyclicCode as CyclicCode
from .decoder import Decoder as Decoder
from .grs_code import GeneralizedReedSolomonCode as GeneralizedReedSolomonCode
from sage.arith.misc import gcd as gcd
from sage.categories.fields import Fields as Fields
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import vector as vector

class BCHCode(CyclicCode):
    """
    Representation of a BCH code seen as a cyclic code.

    INPUT:

    - ``base_field`` -- the base field for this code

    - ``length`` -- the length of the code

    - ``designed_distance`` -- the designed minimum distance of the code

    - ``primitive_root`` -- (default: ``None``) the primitive root to use when
      creating the set of roots for the generating polynomial over the
      splitting field. It has to be of multiplicative order ``length`` over
      this field. If the splitting field is not ``field``, it also has to be a
      polynomial in ``zx``, where ``x`` is the degree of the extension field.
      For instance, over `\\GF{16}`, it has to be a polynomial in ``z4``.

    - ``offset`` -- (default: ``1``) the first element in the defining set

    - ``jump_size`` -- (default: ``1``) the jump size between two elements of
      the defining set. It must be coprime with the multiplicative order of
      ``primitive_root``.

    - ``b`` -- (default: ``0``) is exactly the same as ``offset``. It is only
      here for retro-compatibility purposes with the old signature of
      :meth:`codes.BCHCode` and will be removed soon.

    EXAMPLES:

    As explained above, BCH codes can be built through various parameters::

        sage: C = codes.BCHCode(GF(2), 15, 7, offset=1)
        sage: C
        [15, 5] BCH Code over GF(2) with designed distance 7
        sage: C.generator_polynomial()
        x^10 + x^8 + x^5 + x^4 + x^2 + x + 1

        sage: C = codes.BCHCode(GF(2), 15, 4, offset=1, jump_size=8)
        sage: C
        [15, 7] BCH Code over GF(2) with designed distance 4
        sage: C.generator_polynomial()
        x^8 + x^7 + x^6 + x^4 + 1

    BCH codes are cyclic, and can be interfaced into the :class:`CyclicCode` class.
    The smallest GRS code which contains a given BCH code can also be computed,
    and these two codes may be equal::

        sage: C = codes.BCHCode(GF(16), 15, 7)
        sage: R = C.bch_to_grs()
        sage: codes.CyclicCode(code=R) == codes.CyclicCode(code=C)
        True

    The `\\delta = 15, 1` cases (trivial codes) also work::

        sage: C = codes.BCHCode(GF(16), 15, 1)
        sage: C.dimension()
        15
        sage: C.defining_set()
        []
        sage: C.generator_polynomial()
        1
        sage: C = codes.BCHCode(GF(16), 15, 15)
        sage: C.dimension()
        1
    """
    def __init__(self, base_field, length, designed_distance, primitive_root=None, offset: int = 1, jump_size: int = 1, b: int = 0) -> None:
        """
        TESTS:

        ``designed_distance`` must be between 1 and ``length`` (inclusive),
        otherwise an exception is raised::

            sage: C = codes.BCHCode(GF(2), 15, 16)
            Traceback (most recent call last):
            ...
            ValueError: designed_distance must belong to [1, n]
        """
    def __eq__(self, other):
        """
        Test equality between BCH Code objects.

        EXAMPLES::

            sage: F = GF(16, 'a')
            sage: n = 15
            sage: C1 = codes.BCHCode(F, n, 2)
            sage: C2 = codes.BCHCode(F, n, 2)
            sage: C1 == C2
            True
        """
    def jump_size(self):
        """
        Return the jump size between two consecutive elements of the defining
        set of ``self``.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2), 15, 4, jump_size = 2)
            sage: C.jump_size()
            2
        """
    def offset(self):
        """
        Return the offset which was used to compute the elements in
        the defining set of ``self``.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2), 15, 4, offset = 1)
            sage: C.offset()
            1
        """
    def designed_distance(self):
        """
        Return the designed distance of ``self``.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2), 15, 4)
            sage: C.designed_distance()
            4
        """
    def bch_to_grs(self):
        """
        Return the underlying GRS code from which ``self`` was derived.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2), 15, 3)
            sage: RS = C.bch_to_grs()
            sage: RS
            [15, 13, 3] Reed-Solomon Code over GF(16)
            sage: C.generator_matrix() * RS.parity_check_matrix().transpose() == 0
            True
        """

class BCHUnderlyingGRSDecoder(Decoder):
    """
    A decoder which decodes through the underlying
    :class:`sage.coding.grs_code.GeneralizedReedSolomonCode` code of the provided
    BCH code.

    INPUT:

    - ``code`` -- the associated code of this decoder

    - ``grs_decoder`` -- the string name of the decoder to use over the
      underlying GRS code

    - ``**kwargs`` -- all extra arguments are forwarded to the GRS decoder
    """
    def __init__(self, code, grs_decoder: str = 'KeyEquationSyndrome', **kwargs) -> None:
        """

        EXAMPLES::

            sage: C = codes.BCHCode(GF(4, 'a'), 15, 3, jump_size=2)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: D
            Decoder through the underlying GRS code of [15, 11] BCH Code over GF(4) with designed distance 3
        """
    def grs_code(self):
        """
        Return the underlying GRS code of :meth:`sage.coding.decoder.Decoder.code`.

        .. NOTE::

            Let us explain what is the underlying GRS code of a BCH code of
            length `n` over `F` with parameters `b, \\delta, \\ell`. Let
            `c \\in F^n` and `\\alpha` a primitive root of the splitting field.
            We know:


            .. MATH::

                \\begin{aligned}
                c \\in \\mathrm{BCH} &\\iff \\sum_{i=0}^{n-1} c_i (\\alpha^{b + \\ell j})^i =0, \\quad j=0,\\dots,\\delta-2\\\\\n                & \\iff H c = 0
                \\end{aligned}


            where `H = A \\times D` with:

            .. MATH::

                \\begin{aligned}
                A = &\\, \\begin{pmatrix}
                      1 & \\dots & 1 \\\\\n                      ~ & ~ & ~ \\\\\n                      (\\alpha^{0 \\times \\ell})^{\\delta-2} & \\dots & (\\alpha^{(n-1) \\ell})^{\\delta-2}
                \\end{pmatrix}\\\\\n                D =&\\, \\begin{pmatrix}
                      1 & 0        & \\dots  & 0 \\\\\n                      0 & \\alpha^b & ~      & ~ \\\\\n                      \\dots &          & \\dots & 0 \\\\\n                      0 & \\dots    & 0      & \\alpha^{b(n-1)} \\end{pmatrix}
                \\end{aligned}

            The BCH code is orthogonal to the GRS code `C'` of dimension
            `\\delta - 1` with evaluation points
            `\\{1 = \\alpha^{0 \\times \\ell}, \\dots, \\alpha^{(n-1) \\ell} \\}`
            and associated multipliers
            `\\{1 = \\alpha^{0 \\times b}, \\dots, \\alpha^{(n-1) b} \\}`.
            The underlying GRS code is the dual code of `C'`.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2), 15, 3)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: D.grs_code()
            [15, 13, 3] Reed-Solomon Code over GF(16)
        """
    def grs_decoder(self):
        """
        Return the decoder used to decode words of :meth:`grs_code`.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(4, 'a'), 15, 3, jump_size=2)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: D.grs_decoder()
            Key equation decoder for [15, 13, 3] Generalized Reed-Solomon Code over GF(16)
        """
    def bch_word_to_grs(self, c):
        """
        Return ``c`` converted as a codeword of :meth:`grs_code`.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(2), 15, 3)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: c = C.random_element()
            sage: y = D.bch_word_to_grs(c)
            sage: y.parent()
            Vector space of dimension 15 over Finite Field in z4 of size 2^4
            sage: y in D.grs_code()
            True
        """
    def grs_word_to_bch(self, c):
        """
        Return ``c`` converted as a codeword of :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(4, 'a'), 15, 3, jump_size=2)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: Cgrs = D.grs_code()
            sage: Fgrs = Cgrs.base_field()
            sage: b = Fgrs.gen()
            sage: c = vector(Fgrs, [0, b^2 + b, 1, b^2 + b, 0, 1, 1, 1,
            ....:                   b^2 + b, 0, 0, b^2 + b + 1, b^2 + b, 0, 1])
            sage: D.grs_word_to_bch(c)
            (0, a, 1, a, 0, 1, 1, 1, a, 0, 0, a + 1, a, 0, 1)
        """
    def decode_to_code(self, y):
        '''
        Decodes ``y`` to a codeword in :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: F = GF(4, \'a\')
            sage: a = F.gen()
            sage: C = codes.BCHCode(F, 15, 3, jump_size=2)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: y = vector(F, [a, a + 1, 1, a + 1, 1, a, a + 1,
            ....:                a + 1, 0, 1, a + 1, 1, 1, 1, a])
            sage: D.decode_to_code(y)
            (a, a + 1, 1, a + 1, 1, a, a + 1, a + 1, 0, 1, a + 1, 1, 1, 1, a)
            sage: D.decode_to_code(y) in C
            True

        We check that it still works when, while list-decoding, the GRS decoder
        output some words which do not lie in the BCH code::

            sage: C = codes.BCHCode(GF(2), 31, 15)
            sage: C
            [31, 6] BCH Code over GF(2) with designed distance 15
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C, "GuruswamiSudan", tau=8)
            sage: Dgrs = D.grs_decoder()
            sage: c = vector(GF(2), [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0,
            ....:                    1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0])
            sage: y = vector(GF(2), [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
            ....:                    1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0])
            sage: print (c in C and (c-y).hamming_weight() == 8)
            True
            sage: Dgrs.decode_to_code(y)
            [(1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
                 0, 1, 1, 0, 1, 0, 0),
             (1, z5^3 + z5^2 + z5 + 1, z5^4 + z5^2 + z5, z5^4 + z5^3 + z5^2 + 1, 0, 0,
                 z5^4 + z5 + 1, 1, z5^4 + z5^2 + z5, 0, 1, z5^4 + z5, 1, 0, 1, 1, 1, 0,
                 0, z5^4 + z5^3 + 1, 1, 0, 1, 1, 1, 1, z5^4 + z5^3 + z5 + 1, 1, 1, 0, 0)]
            sage: D.decode_to_code(y) == [c]
            True
        '''
    def decoding_radius(self):
        """
        Return maximal number of errors that ``self`` can decode.

        EXAMPLES::

            sage: C = codes.BCHCode(GF(4, 'a'), 15, 3, jump_size=2)
            sage: D = codes.decoders.BCHUnderlyingGRSDecoder(C)
            sage: D.decoding_radius()
            1
        """
