from sage.arith.misc import binomial as binomial
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.coding.encoder import Encoder as Encoder
from sage.coding.linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeSyndromeDecoder as LinearCodeSyndromeDecoder
from sage.combinat.subset import Subsets as Subsets
from sage.combinat.tuple import Tuples as Tuples
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def ReedMullerCode(base_field, order, num_of_var):
    """
    Return a Reed-Muller code.

    A Reed-Muller Code of order `r` and number of variables `m` over a finite field `F` is the set:

    .. MATH::

        \\{ (f(\\alpha_i)\\mid \\alpha_i \\in F^m)  \\mid  f \\in F[x_1,x_2,\\ldots,x_m], \\deg f \\leq r \\}

    INPUT:

    - ``base_field`` -- the finite field `F` over which the code is built

    - ``order`` -- the order of the Reed-Muller Code, which is the maximum
      degree of the polynomial to be used in the code

    - ``num_of_var`` -- the number of variables used in polynomial

    .. WARNING::

        For now, this implementation only supports Reed-Muller codes whose order is less than q.
        Binary Reed-Muller codes must have their order less than or
        equal to their number of variables.

    EXAMPLES:

    We build a Reed-Muller code::

        sage: F = GF(3)
        sage: C = codes.ReedMullerCode(F, 2, 2)
        sage: C
        Reed-Muller Code of order 2 and 2 variables over Finite Field of size 3

    We ask for its parameters::

        sage: C.length()
        9
        sage: C.dimension()
        6
        sage: C.minimum_distance()
        3

    If one provides a finite field of size 2, a Binary Reed-Muller code is built::

        sage: F = GF(2)
        sage: C = codes.ReedMullerCode(F, 2, 2)
        sage: C
        Binary Reed-Muller Code of order 2 and number of variables 2
    """

class QAryReedMullerCode(AbstractLinearCode):
    """
    Representation of a `q`-ary Reed-Muller code.

    For details on the definition of Reed-Muller codes, refer to
    :meth:`ReedMullerCode`.

    .. NOTE::

        It is better to use the aforementioned method rather than calling this
        class directly, as :meth:`ReedMullerCode` creates either a binary or a
        `q`-ary Reed-Muller code according to the arguments it receives.

    INPUT:

    - ``base_field`` -- a finite field, which is the base field of the code

    - ``order`` -- the order of the Reed-Muller Code, i.e., the maximum degree
      of the polynomial to be used in the code

    - ``num_of_var`` -- the number of variables used in polynomial

    .. WARNING::

        For now, this implementation only supports Reed-Muller codes whose order
        is less than q.

    EXAMPLES::

        sage: from sage.coding.reed_muller_code import QAryReedMullerCode
        sage: F = GF(3)
        sage: C = QAryReedMullerCode(F, 2, 2)
        sage: C
        Reed-Muller Code of order 2 and 2 variables over Finite Field of size 3
    """
    def __init__(self, base_field, order, num_of_var) -> None:
        """
        TESTS:

        Note that the order given cannot be greater than (q-1). An error is raised if that happens::

            sage: from sage.coding.reed_muller_code import QAryReedMullerCode
            sage: C = QAryReedMullerCode(GF(3), 4, 4)
            Traceback (most recent call last):
            ...
            ValueError: The order must be less than 3

        The order and the number of variable must be integers::

            sage: C = QAryReedMullerCode(GF(3),1.1,4)
            Traceback (most recent call last):
            ...
            ValueError: The order of the code must be an integer

        The base_field parameter must be a finite field::

            sage: C = QAryReedMullerCode(QQ,1,4)
            Traceback (most recent call last):
            ...
            ValueError: the input `base_field` must be a FiniteField
        """
    def order(self):
        """
        Return the order of ``self``.

        Order is the maximum degree of the polynomial used in the Reed-Muller code.

        EXAMPLES::

            sage: from sage.coding.reed_muller_code import QAryReedMullerCode
            sage: F = GF(59)
            sage: C = QAryReedMullerCode(F, 2, 4)
            sage: C.order()
            2
        """
    def number_of_variables(self):
        """
        Return the number of variables of the polynomial ring used in ``self``.

        EXAMPLES::

            sage: from sage.coding.reed_muller_code import QAryReedMullerCode
            sage: F = GF(59)
            sage: C = QAryReedMullerCode(F, 2, 4)
            sage: C.number_of_variables()
            4
        """
    def minimum_distance(self):
        """
        Return the minimum distance between two words in ``self``.

        The minimum distance of a `q`-ary Reed-Muller code with order `d` and
        number of variables `m` is `(q-d)q^{m-1}`

        EXAMPLES::

            sage: from sage.coding.reed_muller_code import QAryReedMullerCode
            sage: F = GF(5)
            sage: C = QAryReedMullerCode(F, 2, 4)
            sage: C.minimum_distance()
            375
        """
    def __eq__(self, other):
        """
        Test equality between Reed-Muller Code objects.

        EXAMPLES::

            sage: from sage.coding.reed_muller_code import QAryReedMullerCode
            sage: F = GF(59)
            sage: C1 = QAryReedMullerCode(F, 2, 4)
            sage: C2 = QAryReedMullerCode(GF(59), 2, 4)
            sage: C1.__eq__(C2)
            True
        """

class BinaryReedMullerCode(AbstractLinearCode):
    """
    Representation of a binary Reed-Muller code.

    For details on the definition of Reed-Muller codes, refer to
    :meth:`ReedMullerCode`.

    .. NOTE::

        It is better to use the aforementioned method rather than calling this
        class directly, as :meth:`ReedMullerCode` creates either a binary or a
        `q`-ary Reed-Muller code according to the arguments it receives.


    INPUT:

    - ``order`` -- the order of the Reed-Muller Code, i.e., the maximum degree
      of the polynomial to be used in the code

    - ``num_of_var`` -- the number of variables used in the polynomial

    EXAMPLES:

    A binary Reed-Muller code can be constructed by simply giving the order of
    the code and the number of variables::

        sage: C = codes.BinaryReedMullerCode(2, 4)
        sage: C
        Binary Reed-Muller Code of order 2 and number of variables 4

    Very large Reed-Muller codes can be constructed without building
    the generator matrix or elements of the code (fixes :issue:`33229`,
    see also :issue:`39110`)::

        sage: C = codes.BinaryReedMullerCode(16, 32)
        sage: C
        Binary Reed-Muller Code of order 16 and number of variables 32
        sage: C.dimension(), C.length()
        (2448023843, 4294967296)
    """
    def __init__(self, order, num_of_var) -> None:
        """
        TESTS:

        If the order given is greater than the number of variables an error is raised::

            sage: C = codes.BinaryReedMullerCode(5, 4)
            Traceback (most recent call last):
            ...
            ValueError: The order must be less than or equal to 4

        The order and the number of variable must be integers::

            sage: C = codes.BinaryReedMullerCode(1.1,4)
            Traceback (most recent call last):
            ...
            ValueError: The order of the code must be an integer
        """
    def order(self):
        """
        Return the order of ``self``.

        Order is the maximum degree of the polynomial used in the Reed-Muller code.

        EXAMPLES::

            sage: C = codes.BinaryReedMullerCode(2, 4)
            sage: C.order()
            2
        """
    def number_of_variables(self):
        """
        Return the number of variables of the polynomial ring used in ``self``.

        EXAMPLES::

            sage: C = codes.BinaryReedMullerCode(2, 4)
            sage: C.number_of_variables()
            4
        """
    def minimum_distance(self):
        """
        Return the minimum distance of ``self``.

        The minimum distance of a binary Reed-Muller code of order `d` and
        number of variables `m` is `q^{m-d}`

        EXAMPLES::

            sage: C = codes.BinaryReedMullerCode(2, 4)
            sage: C.minimum_distance()
            4
        """
    def __eq__(self, other):
        """
        Test equality between Reed-Muller Code objects.

        EXAMPLES::

            sage: C1 = codes.BinaryReedMullerCode(2, 4)
            sage: C2 = codes.BinaryReedMullerCode(2, 4)
            sage: C1.__eq__(C2)
            True
        """

class ReedMullerVectorEncoder(Encoder):
    '''
    Encoder for Reed-Muller codes which encodes vectors into codewords.

    Consider a Reed-Muller code of order `r`, number of variables `m`, length `n`,
    dimension `k` over some finite field `F`.
    Let those variables be `(x_1, x_2, \\dots, x_m)`.
    We order the monomials by lowest power on lowest index variables. If we have
    three monomials `x_1 x_2`, `x_1 x_2^2` and `x_1^2 x_2`, the ordering is:
    `x_1 x_2 < x_1 x_2^2 < x_1^2 x_2`

    Let now `(v_1,v_2,\\ldots,v_k)` be a vector of `F`, which corresponds to the polynomial
    `f = \\Sigma^{k}_{i=1} v_i x_i`.

    Let `(\\beta_1, \\beta_2, \\ldots, \\beta_q)` be the elements of `F` ordered as they are
    returned by Sage when calling ``F.list()``.

    The aforementioned polynomial `f` is encoded as:

    `(f(\\alpha_{11},\\alpha_{12},\\ldots,\\alpha_{1m}),f(\\alpha_{21},\\alpha_{22},\\ldots,
    \\alpha_{2m}),\\ldots,f(\\alpha_{q^m1},\\alpha_{q^m2},\\ldots,\\alpha_{q^mm}))`

    with `\\alpha_{ij}=\\beta_{i \\bmod{q^j}}` for all `i`, `j)`.

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: C1 = codes.ReedMullerCode(GF(2), 2, 4)
        sage: E1 = codes.encoders.ReedMullerVectorEncoder(C1)
        sage: E1
        Evaluation vector-style encoder for
         Binary Reed-Muller Code of order 2 and number of variables 4
        sage: C2 = codes.ReedMullerCode(GF(3), 2, 2)
        sage: E2 = codes.encoders.ReedMullerVectorEncoder(C2)
        sage: E2
        Evaluation vector-style encoder for
         Reed-Muller Code of order 2 and 2 variables over Finite Field of size 3

    Actually, we can construct the encoder from ``C`` directly::

        sage: C=codes.ReedMullerCode(GF(2), 2, 4)
        sage: E = C.encoder("EvaluationVector")
        sage: E
        Evaluation vector-style encoder for
         Binary Reed-Muller Code of order 2 and number of variables 4
    '''
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a Reed-Muller code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.encoders.ReedMullerVectorEncoder(C)
            Traceback (most recent call last):
            ...
            ValueError: the code has to be a Reed-Muller code
        """
    def __eq__(self, other):
        """
        Test equality between ReedMullerVectorEncoder objects.

        EXAMPLES::

            sage: F = GF(11)
            sage: C = codes.ReedMullerCode(F, 2, 4)
            sage: D1 = codes.encoders.ReedMullerVectorEncoder(C)
            sage: D2 = codes.encoders.ReedMullerVectorEncoder(C)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    @cached_method
    def generator_matrix(self):
        """
        Return a generator matrix of ``self``.

        EXAMPLES::

            sage: F = GF(3)
            sage: C = codes.ReedMullerCode(F, 2, 2)
            sage: E = codes.encoders.ReedMullerVectorEncoder(C)
            sage: E.generator_matrix()
            [1 1 1 1 1 1 1 1 1]
            [0 1 2 0 1 2 0 1 2]
            [0 0 0 1 1 1 2 2 2]
            [0 1 1 0 1 1 0 1 1]
            [0 0 0 0 1 2 0 2 1]
            [0 0 0 1 1 1 1 1 1]
        """
    def points(self):
        '''
        Return the points of `F^m`, where `F` is the base field and `m` is the
        number of variables, in order of which polynomials are evaluated on.

        EXAMPLES::

            sage: F = GF(3)
            sage: Fx.<x0,x1> = F[]
            sage: C = codes.ReedMullerCode(F, 2, 2)
            sage: E = C.encoder("EvaluationVector")
            sage: E.points()
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        '''

class ReedMullerPolynomialEncoder(Encoder):
    '''
    Encoder for Reed-Muller codes which encodes appropriate multivariate polynomials into codewords.

    Consider a Reed-Muller code of order `r`, number of variables `m`, length `n`,
    dimension `k` over some finite field `F`.
    Let those variables be `(x_1, x_2, \\dots, x_m)`.
    We order the monomials by lowest power on lowest index variables. If we have three monomials
    `x_1 x_2`, `x_1 x_2^2` and `x_1^2 x_2`, the ordering is:
    `x_1 x_2 < x_1 x_2^2 < x_1^2 x_2`

    Let now `f` be a polynomial of the multivariate polynomial ring `F[x_1, \\dots, x_m]`.

    Let `(\\beta_1, \\beta_2, \\ldots, \\beta_q)` be the elements of `F` ordered as they are
    returned by Sage when calling ``F.list()``.

    The aforementioned polynomial `f` is encoded as:

    `(f(\\alpha_{11},\\alpha_{12},\\ldots,\\alpha_{1m}),f(\\alpha_{21},\\alpha_{22},\\ldots,
    \\alpha_{2m}),\\ldots,f(\\alpha_{q^m1},\\alpha_{q^m2},\\ldots,\\alpha_{q^mm}))`

    with `\\alpha_{ij}=\\beta_{i \\bmod{q^j}}` for all `i`, `j`.

    INPUT:

    - ``code`` -- the associated code of this encoder

    - ``polynomial_ring`` -- (default: ``None``) the polynomial ring from which
      the message is chosen;  if this is set to ``None``, a polynomial ring in
      `x` will be built from the code parameters

    EXAMPLES::

        sage: C1 = codes.ReedMullerCode(GF(2), 2, 4)
        sage: E1 = codes.encoders.ReedMullerPolynomialEncoder(C1)
        sage: E1
        Evaluation polynomial-style encoder for
         Binary Reed-Muller Code of order 2 and number of variables 4
        sage: C2 = codes.ReedMullerCode(GF(3), 2, 2)
        sage: E2 = codes.encoders.ReedMullerPolynomialEncoder(C2)
        sage: E2
        Evaluation polynomial-style encoder for
         Reed-Muller Code of order 2 and 2 variables over Finite Field of size 3

    We can also pass a predefined polynomial ring::

        sage: R = PolynomialRing(GF(3), 2, \'y\')
        sage: C = codes.ReedMullerCode(GF(3), 2, 2)
        sage: E = codes.encoders.ReedMullerPolynomialEncoder(C, R)
        sage: E
        Evaluation polynomial-style encoder for
         Reed-Muller Code of order 2 and 2 variables over Finite Field of size 3

    Actually, we can construct the encoder from ``C`` directly::

        sage: E = C1.encoder("EvaluationPolynomial")
        sage: E
        Evaluation polynomial-style encoder for
         Binary Reed-Muller Code of order 2 and number of variables 4
    '''
    def __init__(self, code, polynomial_ring=None) -> None:
        """
        TESTS:

        If ``code`` is not a Reed-Muller code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.encoders.ReedMullerPolynomialEncoder(C)
            Traceback (most recent call last):
            ...
            ValueError: the code has to be a Reed-Muller code

        If the polynomial ring passed is not according to the requirement (over a different field or different number of variables) then an error is raised::

            sage: F=GF(59)
            sage: R.<x,y,z,w>=F[]
            sage: C=codes.ReedMullerCode(F, 2, 3)
            sage: E=codes.encoders.ReedMullerPolynomialEncoder(C, R)
            Traceback (most recent call last):
            ...
            ValueError: The Polynomial ring should be on Finite Field of size 59 and should have 3 variables
        """
    def __eq__(self, other):
        """
        Test equality between ReedMullerVectorEncoder objects.

        EXAMPLES::

            sage: F = GF(11)
            sage: C = codes.ReedMullerCode(F, 2, 4)
            sage: D1 = codes.encoders.ReedMullerPolynomialEncoder(C)
            sage: D2 = codes.encoders.ReedMullerPolynomialEncoder(C)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    def encode(self, p):
        '''
        Transform the polynomial ``p`` into a codeword of :meth:`code`.

        INPUT:

        - ``p`` -- a polynomial from the message space of ``self`` of degree
          less than ``self.code().order()``

        OUTPUT: a codeword in associated code of ``self``

        EXAMPLES::

            sage: F = GF(3)
            sage: Fx.<x0,x1> = F[]
            sage: C = codes.ReedMullerCode(F, 2, 2)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: p = x0*x1 + x1^2 + x0 + x1 + 1
            sage: c = E.encode(p); c
            (1, 2, 0, 0, 2, 1, 1, 1, 1)
            sage: c in C
            True

        If a polynomial with good monomial degree but wrong monomial
        degree is given, an error is raised::

            sage: p = x0^2*x1
            sage: E.encode(p)
            Traceback (most recent call last):
            ...
            ValueError: The polynomial to encode must have degree at most 2

        If ``p`` is not an element of the proper polynomial ring, an error is raised::

            sage: Qy.<y1,y2> = QQ[]
            sage: p = y1^2 + 1
            sage: E.encode(p)
            Traceback (most recent call last):
            ...
            ValueError: The value to encode must be in
            Multivariate Polynomial Ring in x0, x1 over Finite Field of size 3
        '''
    def unencode_nocheck(self, c):
        '''
        Return the message corresponding to the codeword ``c``.

        Use this method with caution: it does not check if ``c``
        belongs to the code, and if this is not the case, the output is
        unspecified. Instead, use :meth:`unencode`.

        INPUT:

        - ``c`` -- a codeword of :meth:`code`

        OUTPUT:

        - A polynomial of degree less than ``self.code().order()``.

        EXAMPLES::

            sage: F = GF(3)
            sage: C = codes.ReedMullerCode(F, 2, 2)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: c = vector(F, (1, 2, 0, 0, 2, 1, 1, 1, 1))
            sage: c in C
            True
            sage: p = E.unencode_nocheck(c); p
            x0*x1 + x1^2 + x0 + x1 + 1
            sage: E.encode(p) == c
            True

        Note that no error is thrown if ``c`` is not a codeword, and that the
        result is undefined::

            sage: c = vector(F, (1, 2, 0, 0, 2, 1, 0, 1, 1))
            sage: c in C
            False
            sage: p = E.unencode_nocheck(c); p
            -x0*x1 - x1^2 + x0 + 1
            sage: E.encode(p) == c
            False
        '''
    def message_space(self):
        '''
        Return the message space of ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: C = codes.ReedMullerCode(F, 2, 4)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: E.message_space()
            Multivariate Polynomial Ring in x0, x1, x2, x3 over Finite Field of size 11
        '''
    def polynomial_ring(self):
        '''
        Return the polynomial ring associated with ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: C = codes.ReedMullerCode(F, 2, 4)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: E.polynomial_ring()
            Multivariate Polynomial Ring in x0, x1, x2, x3 over Finite Field of size 11
        '''
    def points(self):
        '''
        Return the evaluation points in the appropriate order as used by ``self`` when
        encoding a message.

        EXAMPLES::

            sage: F = GF(3)
            sage: Fx.<x0,x1> = F[]
            sage: C = codes.ReedMullerCode(F, 2, 2)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: E.points()
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        '''
