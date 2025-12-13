from sage.coding.encoder import Encoder as Encoder
from sage.coding.linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeGeneratorMatrixEncoder as LinearCodeGeneratorMatrixEncoder
from sage.matrix.constructor import identity_matrix as identity_matrix
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer

class ParityCheckCode(AbstractLinearCode):
    """
    Representation of a parity-check code.

    INPUT:

    - ``base_field`` -- the base field over which ``self`` is defined

    - ``dimension`` -- the dimension of ``self``

    EXAMPLES::

        sage: C = codes.ParityCheckCode(GF(5), 7)
        sage: C
        [8, 7] parity-check code over GF(5)
    """
    def __init__(self, base_field=..., dimension: int = 7) -> None:
        """
        Initialize mandatory parameters for a parity-check code object.

        INPUT:

        - ``base_field`` -- the base field over which ``self`` is defined
          or GF(2) if no base_field

        - ``dimension`` -- the dimension of ``self`` or 7 if no dimension

        EXAMPLES::

            sage: C = codes.ParityCheckCode(GF(5), 7)
            sage: C
            [8, 7] parity-check code over GF(5)
        """
    def __eq__(self, other):
        """
        Test equality of parity-check code objects.

        EXAMPLES::

            sage: C1 = codes.ParityCheckCode(GF(5), 7)
            sage: C2 = codes.ParityCheckCode(GF(5), 7)
            sage: C1 == C2
            True
        """
    def minimum_distance(self):
        """
        Return the minimum distance of ``self``.

        It is always 2 as ``self`` is a parity-check code.

        EXAMPLES::

            sage: C = codes.ParityCheckCode(GF(5), 7)
            sage: C.minimum_distance()
            2
        """

class ParityCheckCodeGeneratorMatrixEncoder(LinearCodeGeneratorMatrixEncoder):
    '''
    Encoder for parity-check codes which uses a generator matrix to obtain
    codewords.

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: C = codes.ParityCheckCode(GF(5), 7)
        sage: E = codes.encoders.ParityCheckCodeGeneratorMatrixEncoder(C)
        sage: E
        Generator matrix-based encoder for [8, 7] parity-check code over GF(5)

    Actually, we can construct the encoder from ``C`` directly::

        sage: E = C.encoder("ParityCheckCodeGeneratorMatrixEncoder")
        sage: E
        Generator matrix-based encoder for [8, 7] parity-check code over GF(5)
    '''
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a parity-check code, an error is raised::

            sage: C = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.encoders.ParityCheckCodeGeneratorMatrixEncoder(C)
            Traceback (most recent call last):
            ...
            ValueError: code has to be a parity-check code
        """
    def generator_matrix(self):
        """
        Return a generator matrix of ``self``.

        EXAMPLES::

            sage: C = codes.ParityCheckCode(GF(5),7)
            sage: E = codes.encoders.ParityCheckCodeGeneratorMatrixEncoder(C)
            sage: E.generator_matrix()
            [1 0 0 0 0 0 0 4]
            [0 1 0 0 0 0 0 4]
            [0 0 1 0 0 0 0 4]
            [0 0 0 1 0 0 0 4]
            [0 0 0 0 1 0 0 4]
            [0 0 0 0 0 1 0 4]
            [0 0 0 0 0 0 1 4]
        """

class ParityCheckCodeStraightforwardEncoder(Encoder):
    '''
    Encoder for parity-check codes which computes the sum of message symbols
    and appends its opposite to the message to obtain codewords.

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: C = codes.ParityCheckCode(GF(5), 7)
        sage: E = codes.encoders.ParityCheckCodeStraightforwardEncoder(C)
        sage: E
        Parity-check encoder for the [8, 7] parity-check code over GF(5)

    Actually, we can construct the encoder from ``C`` directly::

        sage: E = C.encoder("ParityCheckCodeStraightforwardEncoder")
        sage: E
        Parity-check encoder for the [8, 7] parity-check code over GF(5)
    '''
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a parity-check code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.encoders.ParityCheckCodeStraightforwardEncoder(C)
            Traceback (most recent call last):
            ...
            ValueError: code has to be a parity-check code
        """
    def __eq__(self, other):
        """
        Test equality of parity-check code objects.

        EXAMPLES::

            sage: C1 = codes.ParityCheckCode(GF(5), 7)
            sage: C2 = codes.ParityCheckCode(GF(5), 7)
            sage: C1 == C2
            True
        """
    def encode(self, message):
        """
        Transform the vector ``message`` into a codeword of :meth:`code`.

        INPUT:

        - ``message`` -- a ``self.code().dimension()``-vector from the message
          space of ``self``

        OUTPUT: a codeword in associated code of ``self``

        EXAMPLES::

            sage: C = codes.ParityCheckCode(GF(5),7)
            sage: message = vector(C.base_field(),[1,0,4,2,0,3,2])
            sage: C.encode(message)
            (1, 0, 4, 2, 0, 3, 2, 3)
        """
    def unencode_nocheck(self, word):
        """
        Return the message corresponding to the vector ``word``.

        Use this method with caution: it does not check if ``word``
        belongs to the code.

        INPUT:

        - ``word`` -- a ``self.code().length()``-vector from the ambiant space
          of ``self``

        OUTPUT: a vector corresponding to the ``self.code().dimension()``-first
        symbols in ``word``

        EXAMPLES::

            sage: C = codes.ParityCheckCode(GF(5), 7)
            sage: word = vector(C.base_field(), [1, 0, 4, 2, 0, 3, 2, 3])
            sage: E = codes.encoders.ParityCheckCodeStraightforwardEncoder(C)
            sage: E.unencode_nocheck(word)
            (1, 0, 4, 2, 0, 3, 2)
        """
    def message_space(self):
        """
        Return the message space of ``self``.

        EXAMPLES::

            sage: C = codes.ParityCheckCode(GF(5),7)
            sage: E = codes.encoders.ParityCheckCodeStraightforwardEncoder(C)
            sage: E.message_space()
            Vector space of dimension 7 over Finite Field of size 5
        """
