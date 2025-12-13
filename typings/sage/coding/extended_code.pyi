from .decoder import Decoder as Decoder
from .encoder import Encoder as Encoder
from .linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeNearestNeighborDecoder as LinearCodeNearestNeighborDecoder, LinearCodeSyndromeDecoder as LinearCodeSyndromeDecoder
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector

class ExtendedCode(AbstractLinearCode):
    """
    Representation of an extended code.

    INPUT:

    - ``C`` -- a linear code

    EXAMPLES::

        sage: C = codes.random_linear_code(GF(7), 11, 5)
        sage: Ce = codes.ExtendedCode(C)
        sage: Ce
        Extension of [11, 5] linear code over GF(7)
    """
    def __init__(self, C) -> None:
        """
        TESTS:

        ``C`` must be a linear code::

            sage: C = VectorSpace(GF(7), 11)
            sage: codes.ExtendedCode(C)
            Traceback (most recent call last):
            ...
            ValueError: Provided code must be a linear code
        """
    def __eq__(self, other):
        """
        Test equality between two extended codes.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: C1 = codes.ExtendedCode(C)
            sage: C2 = codes.ExtendedCode(C)
            sage: C1 == C2
            True
        """
    def original_code(self):
        """
        Return the code which was extended to get ``self``.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Ce = codes.ExtendedCode(C)
            sage: Ce.original_code()
            [11, 5] linear code over GF(7)
        """
    @cached_method
    def parity_check_matrix(self):
        """
        Return a parity check matrix of ``self``.

        This matrix is computed directly from :func:`original_code`.

        EXAMPLES::

            sage: C = LinearCode(matrix(GF(2),[[1,0,0,1,1],\\\n            ....:                              [0,1,0,1,0],\\\n            ....:                              [0,0,1,1,1]]))
            sage: C.parity_check_matrix()
            [1 0 1 0 1]
            [0 1 0 1 1]
            sage: Ce = codes.ExtendedCode(C)
            sage: Ce.parity_check_matrix()
            [1 1 1 1 1 1]
            [1 0 1 0 1 0]
            [0 1 0 1 1 0]
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        This random element is computed directly from the original code,
        and does not compute a generator matrix of ``self`` in the process.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 9, 5)
            sage: Ce = codes.ExtendedCode(C)
            sage: c = Ce.random_element() #random
            sage: c in Ce
            True
        """

class ExtendedCodeExtendedMatrixEncoder(Encoder):
    """
    Encoder using original code's generator matrix to compute the extended code's one.

    INPUT:

    - ``code`` -- the associated code of ``self``
    """
    def __init__(self, code) -> None:
        """
        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Ce = codes.ExtendedCode(C)
            sage: E = codes.encoders.ExtendedCodeExtendedMatrixEncoder(Ce)
            sage: E
            Matrix-based Encoder for Extension of [11, 5] linear code over GF(7)
        """
    def __eq__(self, other):
        """
        Test equality between GRSEvaluationVectorEncoder objects.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Ce = codes.ExtendedCode(C)
            sage: D1 = codes.encoders.ExtendedCodeExtendedMatrixEncoder(Ce)
            sage: D2 = codes.encoders.ExtendedCodeExtendedMatrixEncoder(Ce)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    @cached_method
    def generator_matrix(self):
        """
        Return a generator matrix of the associated code of ``self``.

        EXAMPLES::

            sage: C = LinearCode(matrix(GF(2),[[1,0,0,1,1],\\\n            ....:                              [0,1,0,1,0],\\\n            ....:                              [0,0,1,1,1]]))
            sage: Ce = codes.ExtendedCode(C)
            sage: E = codes.encoders.ExtendedCodeExtendedMatrixEncoder(Ce)
            sage: E.generator_matrix()
            [1 0 0 1 1 1]
            [0 1 0 1 0 0]
            [0 0 1 1 1 1]
        """

class ExtendedCodeOriginalCodeDecoder(Decoder):
    """
    Decoder which decodes through a decoder over the original code.

    INPUT:

    - ``code`` -- the associated code of this decoder

    - ``original_decoder`` -- (default: ``None``) the decoder that will be used over the original code.
      It has to be a decoder object over the original code.
      If ``original_decoder`` is set to ``None``, it will use the default decoder of the original code.

    - ``**kwargs`` -- all extra arguments are forwarded to original code's decoder

    EXAMPLES::

        sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
        sage: Ce = codes.ExtendedCode(C)
        sage: D = codes.decoders.ExtendedCodeOriginalCodeDecoder(Ce)
        sage: D
        Decoder of Extension of [15, 7, 9] Reed-Solomon Code over GF(16)
         through Gao decoder for [15, 7, 9] Reed-Solomon Code over GF(16)
    """
    def __init__(self, code, original_decoder=None, **kwargs) -> None:
        """
        TESTS:

        If one tries to use a decoder whose code is not the original code, it returns an error::

            sage: C1 = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Ce = codes.ExtendedCode(C1)
            sage: C2 = codes.GeneralizedReedSolomonCode(GF(13).list()[:12], 7)
            sage: Dc2 = C2.decoder()
            sage: D = codes.decoders.ExtendedCodeOriginalCodeDecoder(Ce, original_decoder = Dc2)
            Traceback (most recent call last):
            ...
            ValueError: Original decoder must have the original code as associated code
        """
    def original_decoder(self):
        """
        Return the decoder over the original code that will be used to decode words of
        :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Ce = codes.ExtendedCode(C)
            sage: D = codes.decoders.ExtendedCodeOriginalCodeDecoder(Ce)
            sage: D.original_decoder()
            Gao decoder for [15, 7, 9] Reed-Solomon Code over GF(16)
        """
    def decode_to_code(self, y, **kwargs):
        """
        Decode ``y`` to an element in :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Ce = codes.ExtendedCode(C)
            sage: D = codes.decoders.ExtendedCodeOriginalCodeDecoder(Ce)
            sage: c = Ce.random_element()
            sage: Chan = channels.StaticErrorRateChannel(Ce.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: y in Ce
            False
            sage: D.decode_to_code(y) == c
            True

        Another example, with a list decoder::

            sage: # needs sage.symbolic
            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Ce = codes.ExtendedCode(C)
            sage: Dgrs = C.decoder('GuruswamiSudan', tau=4)
            sage: D = codes.decoders.ExtendedCodeOriginalCodeDecoder(Ce,
            ....:                                                    original_decoder=Dgrs)
            sage: c = Ce.random_element()
            sage: Chan = channels.StaticErrorRateChannel(Ce.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: y in Ce
            False
            sage: c in D.decode_to_code(y)
            True
        """
    def decoding_radius(self, *args, **kwargs):
        """
        Return maximal number of errors that ``self`` can decode.

        INPUT:

        - ``*args``, ``**kwargs`` -- arguments and optional arguments are
          forwarded to original decoder's ``decoding_radius`` method

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Ce = codes.ExtendedCode(C)
            sage: D = codes.decoders.ExtendedCodeOriginalCodeDecoder(Ce)
            sage: D.decoding_radius()
            4
        """
