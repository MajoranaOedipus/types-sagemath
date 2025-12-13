from .decoder import Decoder as Decoder, DecodingError as DecodingError
from .encoder import Encoder as Encoder
from .linear_code import AbstractLinearCode as AbstractLinearCode
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer

class PuncturedCode(AbstractLinearCode):
    """
    Representation of a punctured code.

    - ``C`` -- a linear code

    - ``positions`` -- the positions where ``C`` will be punctured. It can be
      either an integer if one need to puncture only one position, a list or a
      set of positions to puncture. If the same position is passed several
      times, it will be considered only once.

    EXAMPLES::

        sage: C = codes.random_linear_code(GF(7), 11, 5)
        sage: Cp = codes.PuncturedCode(C, 3)
        sage: Cp
        Puncturing of [11, 5] linear code over GF(7) on position(s) [3]

        sage: Cp = codes.PuncturedCode(C, {3, 5})
        sage: Cp
        Puncturing of [11, 5] linear code over GF(7) on position(s) [3, 5]
    """
    def __init__(self, C, positions) -> None:
        """
        TESTS:

        If one of the positions to puncture is bigger than the length of ``C``,
        an exception will be raised::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, {4,8,15})
            Traceback (most recent call last):
            ...
            ValueError: Positions to puncture must be positive integers smaller
            than the length of the provided code
        """
    def __eq__(self, other):
        """
        Test equality between two Punctured codes.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp1 = codes.PuncturedCode(C, 2)
            sage: Cp2 = codes.PuncturedCode(C, 2)
            sage: Cp1 == Cp2
            True
        """
    def punctured_positions(self):
        """
        Return the list of positions which were punctured on the original code.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: Cp.punctured_positions()
            {3}
        """
    def original_code(self):
        """
        Return the linear code which was punctured to get ``self``.

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: Cp.original_code()
            [11, 5] linear code over GF(7)
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: set_random_seed(42)
            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: Cp.dimension()
            5
        """
    def random_element(self, *args, **kwds):
        """
        Return a random codeword of ``self``.

        This method does not trigger the computation of
        ``self``'s :meth:`sage.coding.linear_code_no_metric.generator_matrix`.

        INPUT:

        - ``agrs``, ``kwds`` -- extra positional arguments passed to
          :meth:`sage.modules.free_module.random_element`

        EXAMPLES::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: Cp.random_element() in Cp
            True
        """
    def encode(self, m, original_encode: bool = False, encoder_name=None, **kwargs):
        """
        Transform an element of the message space into an element of the code.

        INPUT:

        - ``m`` -- a vector of the message space of the code

        - ``original_encode`` -- boolean (default: ``False``); if this is set
          to ``True``, ``m`` will be encoded using an Encoder of ``self``'s
          :meth:`original_code`. This allow to avoid the computation of a
          generator matrix for ``self``.

        - ``encoder_name`` -- (default: ``None``) name of the encoder which will be used
          to encode ``word``. The default encoder of ``self`` will be used if
          default value is kept.

        OUTPUT: an element of ``self``

        EXAMPLES::

           sage: M = matrix(GF(7), [[1, 0, 0, 0, 3, 4, 6],
           ....:                    [0, 1, 0, 6, 1, 6, 4],
           ....:                    [0, 0, 1, 5, 2, 2, 4]])
           sage: C_original = LinearCode(M)
           sage: Cp = codes.PuncturedCode(C_original, 2)
           sage: m = vector(GF(7), [1, 3, 5])
           sage: Cp.encode(m)
            (1, 3, 5, 5, 0, 2)
        """
    @cached_method
    def structured_representation(self):
        """
        Return ``self`` as a structured code object.

        If ``self`` has a specific structured representation (e.g. a punctured GRS code is
        a GRS code too), it will return this representation, else it returns a
        :class:`sage.coding.linear_code.LinearCode`.

        EXAMPLES:

        We consider a GRS code::

            sage: C_grs = codes.GeneralizedReedSolomonCode(GF(59).list()[:40], 12)

        A punctured GRS code is still a GRS code::

            sage: Cp_grs = codes.PuncturedCode(C_grs, 3)
            sage: Cp_grs.structured_representation()
            [39, 12, 28] Reed-Solomon Code over GF(59)

        Another example with structureless linear codes::

            sage: set_random_seed(42)
            sage: C_lin  = codes.random_linear_code(GF(2), 10, 5)
            sage: Cp_lin = codes.PuncturedCode(C_lin, 2)
            sage: Cp_lin.structured_representation()
            [9, 5] linear code over GF(2)
        """

class PuncturedCodePuncturedMatrixEncoder(Encoder):
    """
    Encoder using original code generator matrix to compute the punctured code's one.

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: C = codes.random_linear_code(GF(7), 11, 5)
        sage: Cp = codes.PuncturedCode(C, 3)
        sage: E = codes.encoders.PuncturedCodePuncturedMatrixEncoder(Cp)
        sage: E
        Punctured matrix-based encoder for the
         Puncturing of [11, 5] linear code over GF(7) on position(s) [3]
    """
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a ``PuncturedCode``, an exception is raised::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: codes.encoders.PuncturedCodePuncturedMatrixEncoder(C)
            Traceback (most recent call last):
            ...
            TypeError: code has to be an instance of PuncturedCode class
        """
    @cached_method
    def generator_matrix(self):
        """
        Return a generator matrix of the associated code of ``self``.

        EXAMPLES::

            sage: set_random_seed(10)
            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: E = codes.encoders.PuncturedCodePuncturedMatrixEncoder(Cp)
            sage: E.generator_matrix()
            [1 0 0 0 0 5 2 6 0 6]
            [0 1 0 0 0 5 2 2 1 1]
            [0 0 1 0 0 6 2 4 0 4]
            [0 0 0 1 0 0 6 3 3 3]
            [0 0 0 0 1 0 1 3 4 3]
        """

class PuncturedCodeOriginalCodeDecoder(Decoder):
    '''
    Decoder decoding through a decoder over the original code of its punctured code.

    INPUT:

    - ``code`` -- the associated code of this encoder

    - ``strategy`` -- (default: ``None``) the strategy used to decode.
      The available strategies are:

      * ``\'error-erasure\'`` -- uses an error-erasure decoder over the original
        code if available, fails otherwise.

      * ``\'random-values\'`` -- fills the punctured positions with random elements
        in ``code``\'s base field and tries to decode using
        the default decoder of the original code

      * ``\'try-all\'`` -- fills the punctured positions with every possible
        combination of symbols until decoding succeeds, or until every
        combination have been tried

      * ``None`` -- uses ``error-erasure`` if an error-erasure decoder is
        available, switch to ``random-values`` behaviour otherwise

    - ``original_decoder`` -- (default: ``None``) the decoder that will be used over the original code.
      It has to be a decoder object over the original code.
      This argument takes precedence over ``strategy``: if both ``original_decoder`` and ``strategy``
      are filled, ``self`` will use the ``original_decoder`` to decode over the original code.
      If ``original_decoder`` is set to ``None``, it will use the decoder picked by ``strategy``.

    - ``**kwargs`` -- all extra arguments are forwarded to original code\'s decoder

    EXAMPLES::

        sage: C = codes.GeneralizedReedSolomonCode(GF(16, \'a\').list()[:15], 7)
        sage: Cp = codes.PuncturedCode(C, 3)
        sage: codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp)
        Decoder of Puncturing of [15, 7, 9] Reed-Solomon Code over GF(16) on position(s) [3]
         through Error-Erasure decoder for [15, 7, 9] Reed-Solomon Code over GF(16)

    As seen above, if all optional are left blank, and if an error-erasure
    decoder is available, it will be chosen as the original decoder.  Now, if
    one forces ``strategy`` to ``\'try-all\'`` or ``\'random-values\'``, the default
    decoder of the original code will be chosen, even if an error-erasure is
    available::

        sage: C = codes.GeneralizedReedSolomonCode(GF(16, \'a\').list()[:15], 7)
        sage: Cp = codes.PuncturedCode(C, 3)
        sage: D = codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp, strategy=\'try-all\')
        sage: "error-erasure" in D.decoder_type()
        False

    And if one fills ``original_decoder`` and ``strategy`` fields with
    contradictory elements, the ``original_decoder`` takes precedence::

        sage: C = codes.GeneralizedReedSolomonCode(GF(16, \'a\').list()[:15], 7)
        sage: Cp = codes.PuncturedCode(C, 3)
        sage: Dor = C.decoder("Gao")
        sage: D = codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp, original_decoder=Dor,
        ....:                                                     strategy=\'error-erasure\')
        sage: D.original_decoder() == Dor
        True
    '''
    def __init__(self, code, strategy=None, original_decoder=None, **kwargs) -> None:
        """
        TESTS:

        If ``code`` is not a ``PuncturedCode``, an exception is raised::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: codes.decoders.PuncturedCodeOriginalCodeDecoder(C)
            Traceback (most recent call last):
            ...
            TypeError: code has to be an instance of PuncturedCode class

        If one tries to pass an original_decoder whose associated code is not the original
        code of ``self``, it returns an error::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: C2 = codes.GeneralizedReedSolomonCode(GF(7).list()[:6], 3)
            sage: D = Cp.decoder(original_decoder = C2.decoder())
            Traceback (most recent call last):
            ...
            ValueError: Original decoder must have the original code of its associated punctured code as associated code

        If one tries to use ``'error-erasure'`` strategy when the original code has no such
        decoder, it returns an error::

            sage: C = codes.random_linear_code(GF(7), 11, 5)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: D = codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp, strategy = 'error-erasure')
            Traceback (most recent call last):
            ...
            ValueError: Original code has no error-erasure decoder
        """
    def original_decoder(self):
        """
        Return the decoder over the original code that will be used to decode words of
        :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: D = codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp)
            sage: D.original_decoder()
            Error-Erasure decoder for [15, 7, 9] Reed-Solomon Code over GF(16)
        """
    def decode_to_code(self, y):
        """
        Decode ``y`` to an element in :meth:`sage.coding.decoder.Decoder.code`.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: D = codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp)
            sage: c = Cp.random_element()
            sage: Chan = channels.StaticErrorRateChannel(Cp.ambient_space(), 3)
            sage: y = Chan(c)
            sage: y in Cp
            False
            sage: D.decode_to_code(y) == c
            True
        """
    def decoding_radius(self, number_erasures=None):
        """
        Return the maximal number of errors that ``self`` can decode.

        EXAMPLES::

            sage: C = codes.GeneralizedReedSolomonCode(GF(16, 'a').list()[:15], 7)
            sage: Cp = codes.PuncturedCode(C, 3)
            sage: D = codes.decoders.PuncturedCodeOriginalCodeDecoder(Cp)
            sage: D.decoding_radius(2)
            2
        """
