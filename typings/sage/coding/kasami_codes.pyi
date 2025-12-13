import sage.coding.linear_code
from sage.arith.misc import gcd as gcd, is_prime_power as is_prime_power
from sage.coding.linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeGeneratorMatrixEncoder as LinearCodeGeneratorMatrixEncoder
from sage.matrix.constructor import matrix as matrix
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from typing import Any, ClassVar, overload

class KasamiCode(sage.coding.linear_code.AbstractLinearCode):
    """File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 69)

        Representation of a Kasami Code.

        The extended Kasami code with parameters `(s,t)` is defined as

        .. MATH::

            \\{ v \\in \\GF{2}^s \\mid
            \\sum_{a \\in \\GF{s}} v_a =
            \\sum_{a \\in \\GF{s}} a v_a =
            \\sum_{a \\in \\GF{s}} a^{t+1} v_a = 0 \\}

        The only valid parameters `s,t` are given by the below,
        where `q` is a power of 2:

        * `s = q^{2j+1}`, `t = q^m` with `m \\leq j` and `\\gcd(m,2j+1) = 1`
        * `s = q^2`, `t=q`

        The Kasami code `(s,t)` is obtained from the extended
        Kasami code `(s,t)`, via truncation of all words.

        INPUT:

        - ``s``, ``t`` -- integer; the parameters of the Kasami code

        - ``extended`` -- boolean (default: ``True``); if set to ``True``,
          creates an extended Kasami code

        EXAMPLES::

            sage: codes.KasamiCode(16,4)
            [16, 9] Extended (16, 4)-Kasami code
            sage: _.minimum_distance()                                                      # needs sage.libs.gap
            4

            sage: codes.KasamiCode(8, 2, extended=False)
            [7, 1] (8, 2)-Kasami code

            sage: codes.KasamiCode(8,4)
            Traceback (most recent call last):
            ...
            ValueError: The parameters(=8,4) are invalid. Check the documentation

        The extended Kasami code is the extension of the Kasami code::

            sage: C = codes.KasamiCode(16, 4, extended=False)
            sage: Cext = C.extended_code()
            sage: D = codes.KasamiCode(16, 4, extended=True)
            sage: D.generator_matrix() == Cext.generator_matrix()
            True

        .. SEEALSO::

            :mod:`sage.coding.linear_code`.

        REFERENCES:

        For more information on Kasami codes and their use see [BCN1989]_
        or [Kas1966a]_, [Kas1966b]_, [Kas1971]_

        TESTS::

            sage: C1 = codes.KasamiCode(16, 4)
            sage: C2 = codes.KasamiCode(16, 4, extended=False)
            sage: C1.parameters() == C2.parameters()
            True
            sage: C1 == C2
            False
            sage: C1.minimum_distance() == C2.minimum_distance() + 1                        # needs sage.libs.gap
            True
            sage: C = codes.KasamiCode(4,2)
            sage: C.dimension()
            0
            sage: C.generator_matrix()
            []
    """
    _registered_decoders: ClassVar[dict] = ...
    _registered_encoders: ClassVar[dict] = ...
    def __init__(self, s, t, extended=...) -> Any:
        """KasamiCode.__init__(self, s, t, extended=True)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 150)

        Constructor for the ``KasamiCode`` class.

        TESTS::

            sage: codes.KasamiCode(64,8)
            [64, 54] Extended (64, 8)-Kasami code

            sage: codes.KasamiCode(64,8, extended=False)
            [63, 54] (64, 8)-Kasami code

            sage: codes.KasamiCode(3,5)
            Traceback (most recent call last):
            ...
            ValueError: The parameter t(=5) must be a power of 2"""
    @overload
    def generator_matrix(self) -> Any:
        """KasamiCode.generator_matrix(self)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 272)

        Return a generator matrix of ``self``.

        EXAMPLES::

            sage: C = codes.KasamiCode(16, 4, extended=False)
            sage: C.generator_matrix()
            [1 0 0 0 0 0 0 0 0 1 0 0 1 1 1]
            [0 1 0 0 0 0 0 0 0 1 1 0 1 0 0]
            [0 0 1 0 0 0 0 0 0 0 1 1 0 1 0]
            [0 0 0 1 0 0 0 0 0 0 0 1 1 0 1]
            [0 0 0 0 1 0 0 0 0 0 0 0 1 1 0]
            [0 0 0 0 0 1 0 0 0 1 1 0 1 1 1]
            [0 0 0 0 0 0 1 0 0 0 1 1 0 1 1]
            [0 0 0 0 0 0 0 1 0 1 1 1 0 0 1]
            [0 0 0 0 0 0 0 0 1 1 0 1 0 0 0]

        ALGORITHM:

        We build the parity check matrix given by the three equations that
        the codewords must satisfy. Then we generate the parity check matrix
        over `\\GF{2}` and from this the obtain the generator matrix for the
        extended Kasami codes.

        For the Kasami codes, we truncate the last column.

        TESTS::

            sage: C = codes.KasamiCode(4,2)
            sage: C.generator_matrix()
            []
            sage: C = codes.KasamiCode(8,2)
            sage: C.generator_matrix()
            [1 1 1 1 1 1 1 1]
            sage: C.minimum_distance()
            8
            sage: C = codes.KasamiCode(8, 2, extended=False)
            sage: C.generator_matrix()
            [1 1 1 1 1 1 1]
            sage: C.minimum_distance()
            7
            sage: C = codes.KasamiCode(4, 2, extended=False)
            sage: C.generator_matrix()
            []
            sage: C = codes.KasamiCode(16, 4, extended=False)
            sage: C.minimum_distance()
            3"""
    @overload
    def generator_matrix(self) -> Any:
        """KasamiCode.generator_matrix(self)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 272)

        Return a generator matrix of ``self``.

        EXAMPLES::

            sage: C = codes.KasamiCode(16, 4, extended=False)
            sage: C.generator_matrix()
            [1 0 0 0 0 0 0 0 0 1 0 0 1 1 1]
            [0 1 0 0 0 0 0 0 0 1 1 0 1 0 0]
            [0 0 1 0 0 0 0 0 0 0 1 1 0 1 0]
            [0 0 0 1 0 0 0 0 0 0 0 1 1 0 1]
            [0 0 0 0 1 0 0 0 0 0 0 0 1 1 0]
            [0 0 0 0 0 1 0 0 0 1 1 0 1 1 1]
            [0 0 0 0 0 0 1 0 0 0 1 1 0 1 1]
            [0 0 0 0 0 0 0 1 0 1 1 1 0 0 1]
            [0 0 0 0 0 0 0 0 1 1 0 1 0 0 0]

        ALGORITHM:

        We build the parity check matrix given by the three equations that
        the codewords must satisfy. Then we generate the parity check matrix
        over `\\GF{2}` and from this the obtain the generator matrix for the
        extended Kasami codes.

        For the Kasami codes, we truncate the last column.

        TESTS::

            sage: C = codes.KasamiCode(4,2)
            sage: C.generator_matrix()
            []
            sage: C = codes.KasamiCode(8,2)
            sage: C.generator_matrix()
            [1 1 1 1 1 1 1 1]
            sage: C.minimum_distance()
            8
            sage: C = codes.KasamiCode(8, 2, extended=False)
            sage: C.generator_matrix()
            [1 1 1 1 1 1 1]
            sage: C.minimum_distance()
            7
            sage: C = codes.KasamiCode(4, 2, extended=False)
            sage: C.generator_matrix()
            []
            sage: C = codes.KasamiCode(16, 4, extended=False)
            sage: C.minimum_distance()
            3"""
    @overload
    def parameters(self) -> Any:
        """KasamiCode.parameters(self)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 205)

        Return the parameters `s,t` of ``self``.

        EXAMPLES::

            sage: C = codes.KasamiCode(16, 4, extended=True)
            sage: C.parameters()
            (16, 4)
            sage: D = codes.KasamiCode(16, 4, extended=False)
            sage: D.parameters()
            (16, 4)
            sage: C = codes.KasamiCode(8,2)
            sage: C.parameters()
            (8, 2)"""
    @overload
    def parameters(self) -> Any:
        """KasamiCode.parameters(self)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 205)

        Return the parameters `s,t` of ``self``.

        EXAMPLES::

            sage: C = codes.KasamiCode(16, 4, extended=True)
            sage: C.parameters()
            (16, 4)
            sage: D = codes.KasamiCode(16, 4, extended=False)
            sage: D.parameters()
            (16, 4)
            sage: C = codes.KasamiCode(8,2)
            sage: C.parameters()
            (8, 2)"""
    @overload
    def parameters(self) -> Any:
        """KasamiCode.parameters(self)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 205)

        Return the parameters `s,t` of ``self``.

        EXAMPLES::

            sage: C = codes.KasamiCode(16, 4, extended=True)
            sage: C.parameters()
            (16, 4)
            sage: D = codes.KasamiCode(16, 4, extended=False)
            sage: D.parameters()
            (16, 4)
            sage: C = codes.KasamiCode(8,2)
            sage: C.parameters()
            (8, 2)"""
    @overload
    def parameters(self) -> Any:
        """KasamiCode.parameters(self)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 205)

        Return the parameters `s,t` of ``self``.

        EXAMPLES::

            sage: C = codes.KasamiCode(16, 4, extended=True)
            sage: C.parameters()
            (16, 4)
            sage: D = codes.KasamiCode(16, 4, extended=False)
            sage: D.parameters()
            (16, 4)
            sage: C = codes.KasamiCode(8,2)
            sage: C.parameters()
            (8, 2)"""
    @overload
    def __eq__(self, other) -> Any:
        """KasamiCode.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 223)

        Test equality between Kasami Code objects.

        Two Kasami codes are the same if they
        have the same `s,t` values and are both
        extended or both regular.

        EXAMPLES::

            sage: C1 = codes.KasamiCode(8,2)
            sage: C2 = codes.KasamiCode(8,2)
            sage: C1.__eq__(C2)
            True"""
    @overload
    def __eq__(self, C2) -> Any:
        """KasamiCode.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/coding/kasami_codes.pyx (starting at line 223)

        Test equality between Kasami Code objects.

        Two Kasami codes are the same if they
        have the same `s,t` values and are both
        extended or both regular.

        EXAMPLES::

            sage: C1 = codes.KasamiCode(8,2)
            sage: C2 = codes.KasamiCode(8,2)
            sage: C1.__eq__(C2)
            True"""
