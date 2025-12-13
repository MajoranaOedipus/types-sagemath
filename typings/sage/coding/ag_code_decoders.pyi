import sage.coding.decoder
import sage.coding.encoder
from sage.coding.decoder import Decoder as Decoder, DecodingError as DecodingError
from sage.coding.encoder import Encoder as Encoder
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.function_field.constructor import FunctionField as FunctionField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Decoder_K:
    """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1334)

        Common base class for the implementation of decoding algorithm K
        for AG codes.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K
            sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    info: File
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def decode(self, received_vector, boolverbose=..., booldetect_decoding_failure=..., booldetect_Q_polynomial=...) -> Any:
        """Decoder_K.decode(self, received_vector, bool verbose=False, bool detect_decoding_failure=True, bool detect_Q_polynomial=True)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1448)

        Return the message vector that corresponds to the corrected codeword
        from the received vector.

        INPUT:

        - ``received_vector`` -- a received vector in the ambient space of the
          code

        - ``verbose`` -- boolean; if ``True``, verbose information is printed

        - ``detect_decoding_failure`` -- boolean; if ``True``, early failure
          detection is activated

        - ``detect_Q_polynomial`` -- boolean; if ``True``, a Q-polynomial is
          detected for fast decoding

        If decoding fails for some reason, :exc:`DecodingError` is raised. The
        message contained in the exception indicates the type of the decoding
        failure.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K  # long time
            sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)              # long time
            sage: rv = vector(F, [1, a, 1, a + 1, a + 1, a + 1, 1, a + 1])  # long time
            sage: circuit.decode(rv)                                        # long time
            (1, 0, a + 1, a + 1, a)"""
    @overload
    def decode(self, rv) -> Any:
        """Decoder_K.decode(self, received_vector, bool verbose=False, bool detect_decoding_failure=True, bool detect_Q_polynomial=True)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1448)

        Return the message vector that corresponds to the corrected codeword
        from the received vector.

        INPUT:

        - ``received_vector`` -- a received vector in the ambient space of the
          code

        - ``verbose`` -- boolean; if ``True``, verbose information is printed

        - ``detect_decoding_failure`` -- boolean; if ``True``, early failure
          detection is activated

        - ``detect_Q_polynomial`` -- boolean; if ``True``, a Q-polynomial is
          detected for fast decoding

        If decoding fails for some reason, :exc:`DecodingError` is raised. The
        message contained in the exception indicates the type of the decoding
        failure.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K  # long time
            sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)              # long time
            sage: rv = vector(F, [1, a, 1, a + 1, a + 1, a + 1, 1, a + 1])  # long time
            sage: circuit.decode(rv)                                        # long time
            (1, 0, a + 1, a + 1, a)"""
    @overload
    def encode(self, message) -> Any:
        """Decoder_K.encode(self, message)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1362)

        Encode ``message`` to a codeword.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K
            sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)  # long time
            sage: F.<a> = GF(4)                                 # long time
            sage: rv = vector([0, 0, 0, a, 0, a, a + 1, 0])     # long time
            sage: msg = circuit.decode(rv)                      # long time
            sage: circuit.decode(circuit.encode(msg)) == msg    # long time
            True"""
    @overload
    def encode(self, msg) -> Any:
        """Decoder_K.encode(self, message)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1362)

        Encode ``message`` to a codeword.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K
            sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)  # long time
            sage: F.<a> = GF(4)                                 # long time
            sage: rv = vector([0, 0, 0, a, 0, a, a + 1, 0])     # long time
            sage: msg = circuit.decode(rv)                      # long time
            sage: circuit.decode(circuit.encode(msg)) == msg    # long time
            True"""

class Decoder_K_extension:
    """Decoder_K_extension(pls, G, Q, decoder_cls, verbose=False)

    File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2317)

    Common base class for decoding algorithm K for AG codes via constant field extension.

    INPUT:

    - ``pls`` -- list of places of a function field

    - ``G`` -- a divisor of the function field

    - ``Q`` -- a non-rational place

    - ``verbose`` -- if ``True``, verbose information is printed

    EXAMPLES::

        sage: A.<x,y> = AffineSpace(GF(4), 2)
        sage: C = Curve(y^2 + y - x^3)
        sage: pls = C.places()
        sage: F = C.function_field()
        sage: G = 1*F.get_place(4)
        sage: code = codes.EvaluationAGCode(pls, G)
        sage: dec = code.decoder('K'); dec  # long time
        Unique decoder for [9, 4] evaluation AG code over GF(4)

    ::

        sage: P.<x,y> = ProjectiveSpace(GF(4), 1)
        sage: C = Curve(P)
        sage: pls = C.places()
        sage: len(pls)
        5
        sage: F = C.function_field()
        sage: G = F.get_place(2).divisor()
        sage: code = codes.EvaluationAGCode(pls, G)
        sage: code.decoder('K')
        Unique decoder for [5, 3] evaluation AG code over GF(4)"""
    info: File
    def __init__(self, pls, G, Q, decoder_cls, verbose=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2360)

                Initialize.

                TESTS::

                    sage: A.<x,y> = AffineSpace(GF(4), 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: F = C.function_field()
                    sage: G = 1*F.get_place(4)
                    sage: code = codes.EvaluationAGCode(pls, G)      # long time
                    sage: dec = code.decoder('K')                    # long time
                    sage: TestSuite(dec).run(skip='_test_pickling')  # long time
        """
    @overload
    def decode(self, received_vector, **kwargs) -> Any:
        """Decoder_K_extension.decode(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2508)

        Decode the received vector to a message.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        TESTS::

            sage: A.<x,y> = AffineSpace(GF(4), 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: F = C.function_field()
            sage: G = 1*F.get_place(4)
            sage: code = codes.EvaluationAGCode(pls, G)     # long time
            sage: decoder = code.decoder('K')               # long time
            sage: cw = code.random_element()                # long time
            sage: circuit = decoder._circuit                # long time
            sage: circuit.encode(circuit.decode(cw)) == cw  # long time
            True"""
    @overload
    def decode(self, cw) -> Any:
        """Decoder_K_extension.decode(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2508)

        Decode the received vector to a message.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        TESTS::

            sage: A.<x,y> = AffineSpace(GF(4), 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: F = C.function_field()
            sage: G = 1*F.get_place(4)
            sage: code = codes.EvaluationAGCode(pls, G)     # long time
            sage: decoder = code.decoder('K')               # long time
            sage: cw = code.random_element()                # long time
            sage: circuit = decoder._circuit                # long time
            sage: circuit.encode(circuit.decode(cw)) == cw  # long time
            True"""
    def encode(self, message, **kwargs) -> Any:
        """Decoder_K_extension.encode(self, message, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2488)

        Encode ``message`` to a codeword.

        TESTS::

            sage: A.<x,y> = AffineSpace(GF(4), 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: pls = C.places()
            sage: F = C.function_field()
            sage: G = 1*F.get_place(4)
            sage: code = codes.EvaluationAGCode(pls, G)     # long time
            sage: decoder = code.decoder('K')               # long time
            sage: cw = code.random_element()                # long time
            sage: circuit = decoder._circuit                # long time
            sage: circuit.encode(circuit.decode(cw)) == cw  # long time
            True"""

class DifferentialAGCodeDecoder_K(Decoder_K):
    """DifferentialAGCodeDecoder_K(pls, G, Q, verbose=False)

    File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2062)

    This class implements the decoding algorithm K for differential AG codes.

    INPUT:

    - ``pls`` -- list of places of a function field

    - ``G`` -- a divisor of the function field

    - ``Q`` -- a rational place not in ``pls``

    - ``verbose`` -- if ``True``, verbose information is printed

    EXAMPLES::

        sage: F.<a> = GF(4)
        sage: P.<x,y> = AffineSpace(F, 2);
        sage: C = Curve(y^2 + y - x^3)
        sage: pls = C.places()
        sage: p = C([0,0])
        sage: Q, = p.places()
        sage: D = [pl for pl in pls if pl != Q]
        sage: G = 5*Q
        sage: from sage.coding.ag_code_decoders import DifferentialAGCodeDecoder_K
        sage: circuit = DifferentialAGCodeDecoder_K(D, G, Q)  # long time
        sage: rv = vector([1, a, 1, a, 1, a, a, a + 1])
        sage: cw = circuit.encode(circuit.decode(rv))  # long time
        sage: rv - cw  # long time
        (0, 0, 0, a + 1, 1, 0, 0, 0)
        sage: circuit.info['designed_distance']  # long time
        5
        sage: circuit.info['decoding_radius']  # long time
        2"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, pls, G, Q, verbose=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2098)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: P.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: p = C([0,0])
                    sage: Q, = p.places()
                    sage: D = [pl for pl in pls if pl != Q]
                    sage: G = 5*Q
                    sage: from sage.coding.ag_code_decoders import DifferentialAGCodeDecoder_K
                    sage: circuit = DifferentialAGCodeDecoder_K(D, G, Q)  # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')   # long time
        """
    @overload
    def __init__(self, D, G, Q) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2098)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: P.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: p = C([0,0])
                    sage: Q, = p.places()
                    sage: D = [pl for pl in pls if pl != Q]
                    sage: G = 5*Q
                    sage: from sage.coding.ag_code_decoders import DifferentialAGCodeDecoder_K
                    sage: circuit = DifferentialAGCodeDecoder_K(D, G, Q)  # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')   # long time
        """
    def __reduce__(self):
        """DifferentialAGCodeDecoder_K.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __reduce_cython__(self) -> Any:
        """DifferentialAGCodeDecoder_K.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __setstate_cython__(self, __pyx_state) -> Any:
        """DifferentialAGCodeDecoder_K.__setstate_cython__(self, __pyx_state)

        File: <stringsource> (starting at line 16)"""

class DifferentialAGCodeDecoder_K_extension(Decoder_K_extension):
    """DifferentialAGCodeDecoder_K_extension(pls, G, Q, verbose=False)

    File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2587)

    This class implements the decoding algorithm K for differential AG codes via
    constant field extension.

    INPUT:

    - ``pls`` -- list of places of a function field

    - ``G`` -- a divisor of the function field

    - ``Q`` -- a non-rational place

    - ``verbose`` -- if ``True``, verbose information is printed

    EXAMPLES::

        sage: F.<a> = GF(4)
        sage: A.<x,y> = AffineSpace(F, 2)
        sage: C = Curve(y^2 + y - x^3)
        sage: pls = C.places()
        sage: F = C.function_field()
        sage: G = 1*F.get_place(4)
        sage: code = codes.DifferentialAGCode(pls, G)
        sage: Q = F.get_place(3)
        sage: from sage.coding.ag_code_decoders import DifferentialAGCodeDecoder_K_extension
        sage: circuit = DifferentialAGCodeDecoder_K_extension(pls, G, Q)  # long time
        sage: cw = code.random_element()
        sage: rv = cw + vector([0,0,a,0,0,0,0,0,0])
        sage: circuit.encode(circuit.decode(circuit._lift(rv))) == circuit._lift(cw)  # long time
        True"""
    @overload
    def __init__(self, pls, G, Q, verbose=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2620)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: A.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: F = C.function_field()
                    sage: G = 1*F.get_place(4)
                    sage: code = codes.DifferentialAGCode(pls, G)   # long time
                    sage: Q = F.get_place(3)                        # long time
                    sage: from sage.coding.ag_code_decoders import DifferentialAGCodeDecoder_K_extension  # long time
                    sage: circuit = DifferentialAGCodeDecoder_K_extension(pls, G, Q)  # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')               # long time
        """
    @overload
    def __init__(self, pls, G, Q) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2620)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: A.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: F = C.function_field()
                    sage: G = 1*F.get_place(4)
                    sage: code = codes.DifferentialAGCode(pls, G)   # long time
                    sage: Q = F.get_place(3)                        # long time
                    sage: from sage.coding.ag_code_decoders import DifferentialAGCodeDecoder_K_extension  # long time
                    sage: circuit = DifferentialAGCodeDecoder_K_extension(pls, G, Q)  # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')               # long time
        """
    def __reduce__(self):
        """DifferentialAGCodeDecoder_K_extension.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __reduce_cython__(self) -> Any:
        """DifferentialAGCodeDecoder_K_extension.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __setstate_cython__(self, __pyx_state) -> Any:
        """DifferentialAGCodeDecoder_K_extension.__setstate_cython__(self, __pyx_state)

        File: <stringsource> (starting at line 16)"""

class DifferentialAGCodeEncoder(sage.coding.encoder.Encoder):
    """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 292)

        Encoder of a differential AG code.

        INPUT:

        - ``code`` -- a differential AG code

        - ``decoder`` -- a decoder of the code

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)
            sage: dec = code.decoder('K', Q)  # long time
            sage: enc = dec.connected_encoder(); enc  # long time
            Encoder for [8, 3] differential AG code over GF(4)
    """
    def __init__(self, code, decoder=...) -> Any:
        """DifferentialAGCodeEncoder.__init__(self, code, decoder=None)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 318)

        Initialize.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)      # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: TestSuite(enc).run(skip='_test_pickling')  # long time"""
    @overload
    def encode(self, message) -> Any:
        """DifferentialAGCodeEncoder.encode(self, message)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 447)

        Return the codeword encoded from the message.

        INPUT:

        - ``message`` -- a vector in the message space

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)      # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: msg = enc.message_space().random_element() # long time
            sage: codeword = enc.encode(msg)                 # long time
            sage: enc.unencode(codeword) == msg              # long time
            True"""
    @overload
    def encode(self, msg) -> Any:
        """DifferentialAGCodeEncoder.encode(self, message)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 447)

        Return the codeword encoded from the message.

        INPUT:

        - ``message`` -- a vector in the message space

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)      # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: msg = enc.message_space().random_element() # long time
            sage: codeword = enc.encode(msg)                 # long time
            sage: enc.unencode(codeword) == msg              # long time
            True"""
    def unencode_nocheck(self, codeword) -> Any:
        """DifferentialAGCodeEncoder.unencode_nocheck(self, codeword)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 476)

        Return the message unencoded from ``codeword``.

        INPUT:

        - ``codeword`` -- a vector in the code

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)      # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: msg = enc.message_space().random_element() # long time
            sage: codeword = enc.encode(msg)                 # long time
            sage: enc.unencode(codeword) in enc.message_space()  # indirect doctest, long time
            True"""
    def __eq__(self, other) -> Any:
        """DifferentialAGCodeEncoder.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 370)

        Test equality.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)      # long time
            sage: dec1 = code.decoder('K', Q)                # long time
            sage: enc1 = dec1.connected_encoder()            # long time
            sage: dec2 = code.decoder('K', Q)                # long time
            sage: enc2 = dec2.connected_encoder()            # long time
            sage: enc1 == enc2                               # long time
            True"""
    def __hash__(self) -> Any:
        """DifferentialAGCodeEncoder.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 347)

        Return the hash of ``self``.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)      # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: {enc: 1}                                   # long time
            {Encoder for [8, 3] differential AG code over GF(4): 1}"""

class DifferentialAGCodeUniqueDecoder(sage.coding.decoder.Decoder):
    """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 914)

        Unique decoder for a differential AG codes.

        INPUT:

        - ``code`` -- an evaluation AG code

        - ``Q`` -- (optional) a place, not one of the places supporting the code

        - ``basis`` -- (optional) a basis of the space of differentials to take residues

        - ``verbose`` -- if ``True``, verbose information is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C(0,0)
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 2)
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: dec = code.decoder('K', Q)  # long time
            sage: enc = dec.connected_encoder()  # long time
            sage: enc.encode(dec.decode_to_message(rv)) in code  # long time
            True

        If ``basis`` is given, that defines the associated residue encoding map::

            sage: basis = tuple((G - sum(D)).basis_differential_space())
            sage: w = basis[0]
            sage: cw = vector(w.residue(p) for p in D)
            sage: dec2 = code.decoder('K', Q, basis)  # long time
            sage: enc2 = dec2.connected_encoder()  # long time
            sage: temp = enc2.unencode(cw); temp  # long time
            (1, 0, 0)
            sage: enc2.encode(temp) == cw  # long time
            True
            sage: w = basis[1]
            sage: cw = vector(w.residue(p) for p in D)
            sage: temp = enc2.unencode(cw); temp  # long time
            (0, 1, 0)
            sage: enc2.encode(temp) == cw  # long time
            True

        The default ``basis`` is given by ``code.basis_differentials()``.
    """
    _decoder_type: ClassVar[set] = ...
    def __init__(self, code, Q=..., basis=..., verbose=...) -> Any:
        """DifferentialAGCodeUniqueDecoder.__init__(self, code, Q=None, basis=None, verbose=False)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 969)

        Initialize.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: TestSuite(dec).run()                   # long time"""
    @overload
    def connected_encoder(self) -> Any:
        """DifferentialAGCodeUniqueDecoder.connected_encoder(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1203)

        Return the connected encoder for this decoder.

        INPUT:

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to the
          constructor of the connected encoder

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: dec.connected_encoder()                # long time
            Encoder for [8, 3] differential AG code over GF(4)"""
    @overload
    def connected_encoder(self, *args, **kwargs) -> Any:
        """DifferentialAGCodeUniqueDecoder.connected_encoder(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1203)

        Return the connected encoder for this decoder.

        INPUT:

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to the
          constructor of the connected encoder

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: dec.connected_encoder()                # long time
            Encoder for [8, 3] differential AG code over GF(4)"""
    @overload
    def decode_to_code(self, received_vector, **kwargs) -> Any:
        """DifferentialAGCodeUniqueDecoder.decode_to_code(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1287)

        Return the codeword decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on
          the decoding process is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: enc = dec.connected_encoder()          # long time
            sage: code = dec.code()                      # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 2) # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: cw = dec.decode_to_code(rv)                # long time
            sage: (cw - rv).hamming_weight() == 2            # long time
            True"""
    @overload
    def decode_to_code(self, rv) -> Any:
        """DifferentialAGCodeUniqueDecoder.decode_to_code(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1287)

        Return the codeword decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on
          the decoding process is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: enc = dec.connected_encoder()          # long time
            sage: code = dec.code()                      # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 2) # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: cw = dec.decode_to_code(rv)                # long time
            sage: (cw - rv).hamming_weight() == 2            # long time
            True"""
    @overload
    def decode_to_message(self, received_vector, **kwargs) -> Any:
        """DifferentialAGCodeUniqueDecoder.decode_to_message(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1252)

        Return the message decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on
          the decoding process is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: enc = dec.connected_encoder()          # long time
            sage: code = dec.code()                      # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 2)  # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: msg = dec.decode_to_message(rv)            # long time
            sage: cw = enc.encode(msg)                       # long time
            sage: (cw - rv).hamming_weight() == 2            # long time
            True"""
    @overload
    def decode_to_message(self, rv) -> Any:
        """DifferentialAGCodeUniqueDecoder.decode_to_message(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1252)

        Return the message decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on
          the decoding process is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: enc = dec.connected_encoder()          # long time
            sage: code = dec.code()                      # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 2)  # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: msg = dec.decode_to_message(rv)            # long time
            sage: cw = enc.encode(msg)                       # long time
            sage: (cw - rv).hamming_weight() == 2            # long time
            True"""
    @overload
    def decoding_radius(self) -> Any:
        """DifferentialAGCodeUniqueDecoder.decoding_radius(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1230)

        Return the decoding radius of the decoder.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: dec.decoding_radius()                  # long time
            2"""
    @overload
    def decoding_radius(self) -> Any:
        """DifferentialAGCodeUniqueDecoder.decoding_radius(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1230)

        Return the decoding radius of the decoder.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: dec.decoding_radius()                  # long time
            2"""
    def __eq__(self, other) -> bool:
        """DifferentialAGCodeUniqueDecoder.__eq__(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1058)

        Check whether ``other`` equals ``self``.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec1 = code.decoder('K', Q)            # long time
            sage: dec2 = code.decoder('K', Q)            # long time
            sage: dec1 == dec2                           # long time
            True"""
    def __hash__(self) -> Any:
        """DifferentialAGCodeUniqueDecoder.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1036)

        Return the hash of ``self``.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.DifferentialAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)             # long time
            sage: {dec: 1}                               # long time
            {Unique decoder for [8, 3] differential AG code over GF(4): 1}"""

class EvaluationAGCodeDecoder_K(Decoder_K):
    """EvaluationAGCodeDecoder_K(pls, G, Q, verbose=False)

    File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1807)

    This class implements the decoding algorithm K for evaluation AG codes.

    INPUT:

    - ``pls`` -- list of places of a function field

    - ``G`` -- a divisor of the function field

    - ``Q`` -- a rational place not in ``pls``

    - ``verbose`` -- if ``True``, verbose information is printed

    EXAMPLES::

        sage: F.<a> = GF(4)
        sage: P.<x,y> = AffineSpace(F, 2);
        sage: C = Curve(y^2 + y - x^3)
        sage: pls = C.places()
        sage: p = C([0,0])
        sage: Q, = p.places()
        sage: D = [pl for pl in pls if pl != Q]
        sage: G = 5*Q
        sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K
        sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)
        sage: rv = vector([a, 0, 0, a, 1, 1, a + 1, 0])
        sage: cw = circuit.encode(circuit.decode(rv))
        sage: rv - cw
        (a + 1, 0, 0, 0, 0, 0, 0, 0)
        sage: circuit.info['designed_distance']
        3
        sage: circuit.info['decoding_radius']
        1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, pls, G, Q, verbose=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1843)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: P.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: p = C([0,0])
                    sage: Q, = p.places()
                    sage: D = [pl for pl in pls if pl != Q]
                    sage: G = 5*Q
                    sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K
                    sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)   # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')  # long time
        """
    @overload
    def __init__(self, D, G, Q) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 1843)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: P.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: p = C([0,0])
                    sage: Q, = p.places()
                    sage: D = [pl for pl in pls if pl != Q]
                    sage: G = 5*Q
                    sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K
                    sage: circuit = EvaluationAGCodeDecoder_K(D, G, Q)   # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')  # long time
        """
    def __reduce__(self):
        """EvaluationAGCodeDecoder_K.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __reduce_cython__(self) -> Any:
        """EvaluationAGCodeDecoder_K.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __setstate_cython__(self, __pyx_state) -> Any:
        """EvaluationAGCodeDecoder_K.__setstate_cython__(self, __pyx_state)

        File: <stringsource> (starting at line 16)"""

class EvaluationAGCodeDecoder_K_extension(Decoder_K_extension):
    """EvaluationAGCodeDecoder_K_extension(pls, G, Q, verbose=False)

    File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2533)

    This class implements the decoding algorithm K for evaluation AG codes via
    constant field extension.

    INPUT:

    - ``pls`` -- list of places of a function field

    - ``G`` -- a divisor of the function field

    - ``Q`` -- a non-rational place

    - ``verbose`` -- if ``True``, verbose information is printed

    EXAMPLES::

        sage: F.<a> = GF(4)
        sage: A.<x,y> = AffineSpace(F, 2)
        sage: C = Curve(y^2 + y - x^3)
        sage: pls = C.places()
        sage: F = C.function_field()
        sage: G = 1*F.get_place(4)
        sage: code = codes.EvaluationAGCode(pls, G)
        sage: Q = F.get_place(3)
        sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K_extension
        sage: circuit = EvaluationAGCodeDecoder_K_extension(pls, G, Q)
        sage: cw = code.random_element()
        sage: rv = cw + vector([0,1,1,0,0,0,0,0,0])
        sage: circuit.encode(circuit.decode(circuit._lift(rv))) == circuit._lift(cw)
        True"""
    @overload
    def __init__(self, pls, G, Q, verbose=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2566)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: A.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: F = C.function_field()
                    sage: G = 1*F.get_place(4)
                    sage: code = codes.EvaluationAGCode(pls, G)     # long time
                    sage: Q = F.get_place(3)                        # long time
                    sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K_extension  # long time
                    sage: circuit = EvaluationAGCodeDecoder_K_extension(pls, G, Q)  # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')             # long time
        """
    @overload
    def __init__(self, pls, G, Q) -> Any:
        """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 2566)

                Initialize.

                TESTS::

                    sage: F.<a> = GF(4)
                    sage: A.<x,y> = AffineSpace(F, 2)
                    sage: C = Curve(y^2 + y - x^3)
                    sage: pls = C.places()
                    sage: F = C.function_field()
                    sage: G = 1*F.get_place(4)
                    sage: code = codes.EvaluationAGCode(pls, G)     # long time
                    sage: Q = F.get_place(3)                        # long time
                    sage: from sage.coding.ag_code_decoders import EvaluationAGCodeDecoder_K_extension  # long time
                    sage: circuit = EvaluationAGCodeDecoder_K_extension(pls, G, Q)  # long time
                    sage: TestSuite(circuit).run(skip='_test_pickling')             # long time
        """
    def __reduce__(self):
        """EvaluationAGCodeDecoder_K_extension.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __reduce_cython__(self) -> Any:
        """EvaluationAGCodeDecoder_K_extension.__reduce_cython__(self)

        File: <stringsource> (starting at line 1)"""
    def __setstate_cython__(self, __pyx_state) -> Any:
        """EvaluationAGCodeDecoder_K_extension.__setstate_cython__(self, __pyx_state)

        File: <stringsource> (starting at line 16)"""

class EvaluationAGCodeEncoder(sage.coding.encoder.Encoder):
    """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 77)

        Encoder of an evaluation AG code.

        INPUT:

        - ``code`` -- an evaluation AG code

        - ``decoder`` -- a decoder of the code

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)
            sage: dec = code.decoder('K', Q)
            sage: enc = dec.connected_encoder()
            sage: enc
            Encoder for [8, 5] evaluation AG code over GF(4)
    """
    def __init__(self, code, decoder=...) -> Any:
        """EvaluationAGCodeEncoder.__init__(self, code, decoder=None)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 104)

        Initialize.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)        # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: TestSuite(enc).run(skip='_test_pickling')  # long time"""
    @overload
    def encode(self, message) -> Any:
        """EvaluationAGCodeEncoder.encode(self, message)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 233)

        Return the codeword encoded from the message.

        INPUT:

        - ``message`` -- a vector in the message space

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)        # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: msg = enc.message_space().random_element() # long time
            sage: codeword = enc.encode(msg)                 # long time
            sage: enc.unencode(codeword) == msg              # long time
            True"""
    @overload
    def encode(self, msg) -> Any:
        """EvaluationAGCodeEncoder.encode(self, message)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 233)

        Return the codeword encoded from the message.

        INPUT:

        - ``message`` -- a vector in the message space

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)        # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: msg = enc.message_space().random_element() # long time
            sage: codeword = enc.encode(msg)                 # long time
            sage: enc.unencode(codeword) == msg              # long time
            True"""
    def unencode_nocheck(self, codeword) -> Any:
        """EvaluationAGCodeEncoder.unencode_nocheck(self, codeword)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 262)

        Return the message unencoded from ``codeword``.

        INPUT:

        - ``codeword`` -- a vector in the code

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)        # long time
            sage: dec = code.decoder('K', Q)                 # long time
            sage: enc = dec.connected_encoder()              # long time
            sage: msg = enc.message_space().random_element() # long time
            sage: codeword = enc.encode(msg)                 # long time
            sage: enc.unencode(codeword) in enc.message_space()  # long time, indirect doctest
            True"""
    def __eq__(self, other) -> Any:
        """EvaluationAGCodeEncoder.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 156)

        Test equality.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec1 = code.decoder('K', Q)          # long time
            sage: enc1 = dec1.connected_encoder()      # long time
            sage: dec2 = code.decoder('K', Q)          # long time
            sage: enc2 = dec2.connected_encoder()      # long time
            sage: enc1 == enc2                         # long time
            True"""
    def __hash__(self) -> Any:
        """EvaluationAGCodeEncoder.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 133)

        Return the hash of ``self``.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: enc = dec.connected_encoder()        # long time
            sage: {enc: 1}                             # long time
            {Encoder for [8, 5] evaluation AG code over GF(4): 1}"""

class EvaluationAGCodeUniqueDecoder(sage.coding.decoder.Decoder):
    """File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 506)

        Unique decoder for evaluation AG codes.

        INPUT:

        - ``code`` -- an evaluation AG code

        - ``Q`` -- (optional) a place, not one of the places supporting the code

        - ``basis`` -- (optional) a basis of the space of functions to evaluate

        - ``verbose`` -- if ``True``, verbose information is printed

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(k, 2);
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C(0,0)
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)
            sage: dec = code.decoder('K', Q)
            sage: enc = dec.connected_encoder()
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 1)
            sage: rv = chan.transmit(code.random_element())
            sage: enc.encode(dec.decode_to_message(rv)) in code
            True

        If ``basis`` is given, that defines the associated evaluation encoding map::

            sage: basis = tuple(G.basis_function_space())
            sage: dec2 = code.decoder('K', Q, basis)
            sage: enc2 = dec2.connected_encoder()
            sage: f = basis[0]
            sage: cw = vector(f.evaluate(p) for p in D)
            sage: enc2.unencode(cw)
            (1, 0, 0, 0, 0)
            sage: enc2.encode(_) == cw
            True
            sage: f = basis[1]
            sage: cw = vector(f.evaluate(p) for p in D)
            sage: enc2.unencode(cw)
            (0, 1, 0, 0, 0)
            sage: enc2.encode(_) == cw
            True

        The default ``basis`` is given by ``code.basis_functions()``.
    """
    _decoder_type: ClassVar[set] = ...
    def __init__(self, code, Q=..., basis=..., verbose=...) -> Any:
        """EvaluationAGCodeUniqueDecoder.__init__(self, code, Q=None, basis=None, verbose=False)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 561)

        Initialize.

        TESTS::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: TestSuite(dec).run()                 # long time"""
    @overload
    def connected_encoder(self) -> Any:
        """EvaluationAGCodeUniqueDecoder.connected_encoder(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 796)

        Return the connected encoder for this decoder.

        INPUT:

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to the
          constructor of the connected encoder

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: dec.connected_encoder()              # long time
            Encoder for [8, 5] evaluation AG code over GF(4)"""
    @overload
    def connected_encoder(self, *args, **kwargs) -> Any:
        """EvaluationAGCodeUniqueDecoder.connected_encoder(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 796)

        Return the connected encoder for this decoder.

        INPUT:

        - ``args``, ``kwargs`` -- all additional arguments are forwarded to the
          constructor of the connected encoder

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: dec.connected_encoder()              # long time
            Encoder for [8, 5] evaluation AG code over GF(4)"""
    @overload
    def decode_to_code(self, received_vector, **kwargs) -> Any:
        """EvaluationAGCodeUniqueDecoder.decode_to_code(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 880)

        Return the codeword decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on the decoding process
          is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: code = dec.code()                    # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 1)  # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: cw = dec.decode_to_code(rv)                # long time
            sage: (cw - rv).hamming_weight() == 1            # long time
            True"""
    @overload
    def decode_to_code(self, rv) -> Any:
        """EvaluationAGCodeUniqueDecoder.decode_to_code(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 880)

        Return the codeword decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on the decoding process
          is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: code = dec.code()                    # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 1)  # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: cw = dec.decode_to_code(rv)                # long time
            sage: (cw - rv).hamming_weight() == 1            # long time
            True"""
    @overload
    def decode_to_message(self, received_vector, **kwargs) -> Any:
        """EvaluationAGCodeUniqueDecoder.decode_to_message(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 845)

        Return the message decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on the decoding process
          is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: enc = dec.connected_encoder()        # long time
            sage: code = dec.code()                    # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 1)  # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: msg = dec.decode_to_message(rv)            # long time
            sage: cw = enc.encode(msg)                       # long time
            sage: (cw - rv).hamming_weight() == 1            # long time
            True"""
    @overload
    def decode_to_message(self, rv) -> Any:
        """EvaluationAGCodeUniqueDecoder.decode_to_message(self, received_vector, **kwargs)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 845)

        Return the message decoded from ``received_vector``.

        INPUT:

        - ``received_vector`` -- a vector in the ambient space of the code

        - ``verbose`` -- boolean; if ``True``, verbose information on the decoding process
          is printed

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: enc = dec.connected_encoder()        # long time
            sage: code = dec.code()                    # long time
            sage: chan = channels.StaticErrorRateChannel(code.ambient_space(), 1)  # long time
            sage: rv = chan.transmit(code.random_element())  # long time
            sage: msg = dec.decode_to_message(rv)            # long time
            sage: cw = enc.encode(msg)                       # long time
            sage: (cw - rv).hamming_weight() == 1            # long time
            True"""
    @overload
    def decoding_radius(self) -> Any:
        """EvaluationAGCodeUniqueDecoder.decoding_radius(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 823)

        Return the decoding radius of the decoder.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: dec.decoding_radius()                # long time
            1"""
    @overload
    def decoding_radius(self) -> Any:
        """EvaluationAGCodeUniqueDecoder.decoding_radius(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 823)

        Return the decoding radius of the decoder.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: dec.decoding_radius()                # long time
            1"""
    def __eq__(self, other) -> bool:
        """EvaluationAGCodeUniqueDecoder.__eq__(self, other) -> bool

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 651)

        Check whether ``other`` equals ``self``.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec1 = code.decoder('K', Q)          # long time
            sage: dec2 = code.decoder('K', Q)          # long time
            sage: dec1 == dec2                         # long time
            True"""
    def __hash__(self) -> Any:
        """EvaluationAGCodeUniqueDecoder.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/coding/ag_code_decoders.pyx (starting at line 629)

        Return the hash of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: P.<x,y> = AffineSpace(F, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: D = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(D, G)  # long time
            sage: dec = code.decoder('K', Q)           # long time
            sage: {dec: 1}                             # long time
            {Unique decoder for [8, 5] evaluation AG code over GF(4): 1}"""
