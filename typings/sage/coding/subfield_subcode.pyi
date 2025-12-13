from .decoder import Decoder as Decoder, DecodingError as DecodingError
from .linear_code import AbstractLinearCode as AbstractLinearCode
from sage.categories.homset import Hom as Hom
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector

class SubfieldSubcode(AbstractLinearCode):
    """
    Representation of a subfield subcode.

    INPUT:

    - ``original_code`` -- the code ``self`` comes from

    - ``subfield`` -- the base field of ``self``

    - ``embedding`` -- (default: ``None``) a homomorphism from ``subfield`` to
      ``original_code``'s base field. If ``None`` is provided, it will default
      to the first homomorphism of the list of homomorphisms Sage can build.

    EXAMPLES::

        sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
        sage: codes.SubfieldSubcode(C, GF(4, 'a'))
        Subfield subcode of [7, 3] linear code over GF(16) down to GF(4)
    """
    def __init__(self, original_code, subfield, embedding=None) -> None:
        """
        TESTS:

        ``subfield`` has to be a finite field, otherwise an error is raised::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs = codes.SubfieldSubcode(C, RR)
            Traceback (most recent call last):
            ...
            ValueError: subfield has to be a finite field

        ``subfield`` has to be a subfield of ``original_code``'s base field,
        otherwise an error is raised::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs = codes.SubfieldSubcode(C, GF(8, 'a'))
            Traceback (most recent call last):
            ...
            ValueError: subfield has to be a subfield of the base field of the original code
        """
    def __eq__(self, other):
        """
        Test equality between Subfield Subcode objects.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs1 = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs2 = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs1 == Cs2
            True
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs.dimension()
            3
        """
    def dimension_upper_bound(self):
        """
        Return an upper bound for the dimension of ``self``.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs.dimension_upper_bound()
            3
        """
    def dimension_lower_bound(self):
        """
        Return a lower bound for the dimension of ``self``.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs.dimension_lower_bound()
            -1
        """
    def original_code(self):
        """
        Return the original code of ``self``.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs.original_code()
            [7, 3] linear code over GF(16)
        """
    def embedding(self):
        """
        Return the field embedding between the base field of ``self`` and
        the base field of its original code.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(16, 'aa'), 7, 3)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs.embedding()
            Ring morphism:
              From: Finite Field in a of size 2^2
              To:   Finite Field in aa of size 2^4
              Defn: a |--> aa^2 + aa
        """
    @cached_method
    def parity_check_matrix(self):
        """
        Return a parity check matrix of ``self``.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cs.parity_check_matrix()
            [    1     0     0     0     0     0     0     0     0     0     1 a + 1 a + 1]
            [    0     1     0     0     0     0     0     0     0     0 a + 1     0     a]
            [    0     0     1     0     0     0     0     0     0     0 a + 1     a     0]
            [    0     0     0     1     0     0     0     0     0     0     0 a + 1     a]
            [    0     0     0     0     1     0     0     0     0     0 a + 1     1 a + 1]
            [    0     0     0     0     0     1     0     0     0     0     1     1     1]
            [    0     0     0     0     0     0     1     0     0     0     a     a     1]
            [    0     0     0     0     0     0     0     1     0     0     a     1     a]
            [    0     0     0     0     0     0     0     0     1     0 a + 1 a + 1     1]
            [    0     0     0     0     0     0     0     0     0     1     a     0 a + 1]
        """

class SubfieldSubcodeOriginalCodeDecoder(Decoder):
    """
    Decoder decoding through a decoder over the original code of ``code``.

    INPUT:

    - ``code`` -- the associated code of this decoder

    - ``original_decoder`` -- (default: ``None``) the decoder that will be used
      over the original code. It has to be a decoder object over the original
      code. If it is set to ``None``, the default decoder over the original
      code will be used.

    - ``**kwargs`` -- all extra arguments are forwarded to original code's decoder

    EXAMPLES::

        sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
        sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
        sage: codes.decoders.SubfieldSubcodeOriginalCodeDecoder(Cs)
        Decoder of Subfield subcode of [13, 5, 9] Reed-Solomon Code over GF(16) down to GF(4)
         through Gao decoder for [13, 5, 9] Reed-Solomon Code over GF(16)
    """
    def __init__(self, code, original_decoder=None, **kwargs) -> None:
        """
        TESTS:

        If the original decoder is not a decoder over ``code``'s original code, an error is
        raised::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: Cbis = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:9], 5)
            sage: D = Cbis.decoder()
            sage: codes.decoders.SubfieldSubcodeOriginalCodeDecoder(Cs, original_decoder=D)
            Traceback (most recent call last):
            ...
            ValueError: original_decoder must have the original code as associated code
        """
    def original_decoder(self):
        """
        Return the decoder over the original code that will be used to decode words of
        :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: D = codes.decoders.SubfieldSubcodeOriginalCodeDecoder(Cs)
            sage: D.original_decoder()
            Gao decoder for [13, 5, 9] Reed-Solomon Code over GF(16)
        """
    def decode_to_code(self, y):
        """
        Return an error-corrected codeword from ``y``.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: D = codes.decoders.SubfieldSubcodeOriginalCodeDecoder(Cs)
            sage: Chan = channels.StaticErrorRateChannel(Cs.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: c = Cs.random_element()
            sage: y = Chan(c)
            sage: c == D.decode_to_code(y)
            True
        """
    def decoding_radius(self, **kwargs):
        """
        Return the maximal number of errors ``self`` can decode.

        INPUT:

        - ``kwargs`` -- optional arguments are forwarded to original decoder's
          :meth:`sage.coding.decoder.Decoder.decoding_radius` method

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'aa').list()[:13], 5)
            sage: Cs = codes.SubfieldSubcode(C, GF(4, 'a'))
            sage: D = codes.decoders.SubfieldSubcodeOriginalCodeDecoder(Cs)
            sage: D.decoding_radius()
            4
        """
