from .decoder import Decoder as Decoder, DecodingError as DecodingError
from .encoder import Encoder as Encoder
from .linear_code import AbstractLinearCode as AbstractLinearCode
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import symbolic_sum as symbolic_sum
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class GeneralizedReedSolomonCode(AbstractLinearCode):
    """
    Representation of a (Generalized) Reed-Solomon code.

    INPUT:

    - ``evaluation_points`` -- list of distinct elements of some
      finite field `F`

    - ``dimension`` -- the dimension of the resulting code

    - ``column_multipliers`` -- (default: ``None``) list of nonzero
      elements of `F`; all column multipliers are set to 1 if default
      value is kept

    EXAMPLES:

    Often, one constructs a Reed-Solomon code by taking all nonzero elements of
    the field as evaluation points, and specifying no column multipliers (see
    also :func:`ReedSolomonCode` for constructing classical Reed-Solomon codes
    directly)::

        sage: F = GF(7)
        sage: evalpts = [F(i) for i in range(1,7)]
        sage: C = codes.GeneralizedReedSolomonCode(evalpts, 3)
        sage: C
        [6, 3, 4] Reed-Solomon Code over GF(7)

    More generally, the following is a Reed-Solomon code where the evaluation
    points are a subset of the field and includes zero::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
        sage: C
        [40, 12, 29] Reed-Solomon Code over GF(59)

    It is also possible to specify the column multipliers::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: colmults = F.list()[1:n+1]
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k, colmults)
        sage: C
        [40, 12, 29] Generalized Reed-Solomon Code over GF(59)

    SageMath implements efficient decoding algorithms for GRS codes::

        sage: F = GF(11)
        sage: n, k = 10, 5
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[1:n+1], k)
        sage: r = vector(F, (8, 2, 6, 10, 6, 10, 7, 6, 7, 2))
        sage: C.decode_to_message(r)
        (3, 6, 6, 3, 1)

    TESTS:

    Test that the bug in :issue:`30045` is fixed::

        sage: F = GF(5)
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:5], 2)
        sage: D = codes.decoders.GRSErrorErasureDecoder(C)
        sage: y = (vector(F, [3, 0, 3, 0, 3]), vector(GF(2),[0, 1, 0, 1, 0]))
        sage: D.decode_to_code(y)
        (3, 3, 3, 3, 3)
        sage: D.decode_to_message(y)
        (3, 0)
    """
    def __init__(self, evaluation_points, dimension, column_multipliers=None) -> None:
        """
        TESTS:

        If the evaluation points are not from a finite field, it raises an error::

            sage: C = codes.GeneralizedReedSolomonCode([1,2,3], 1)
            Traceback (most recent call last):
            ...
            ValueError: Evaluation points must be in a finite field (and Integer Ring is not one)

        If the evaluation points are not from the same finite field, it raises an error::

            sage: F2, F3 = GF(2) , GF(3)
            sage: C = codes.GeneralizedReedSolomonCode([F2.zero(),F2.one(),F3(2)], 1)
            Traceback (most recent call last):
            ...
            ValueError: Failed converting all evaluation points to the same field (unable to find a common ring for all elements)

        If the column multipliers cannot be converted into the finite are not from a finite field, or cannot be not in the same
        finite field as the evaluation points, it raises an error::

            sage: F = GF(59)
            sage: F2 = GF(61)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k, [.3]*n )
            Traceback (most recent call last):
            ...
            ValueError: Failed converting all evaluation points and column multipliers to the same field (unable to find a common ring for all elements)

            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k, F2.list()[1:n+1])
            Traceback (most recent call last):
            ...
            ValueError: Failed converting all evaluation points and column multipliers to the same field (unable to find a common ring for all elements)

        The number of column multipliers is checked as well::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k, F.list()[1:n])
            Traceback (most recent call last):
            ...
            ValueError: There must be the same number of evaluation points as column multipliers

        It is not allowed to have 0 as a column multiplier::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k, F.list()[:n])
            Traceback (most recent call last):
            ...
            ValueError: All column multipliers must be nonzero

        And all the evaluation points must be different. Note that they should
        be different after converting into the same field::

            sage: F = GF(5)
            sage: C = codes.GeneralizedReedSolomonCode([ F(0), 1, 2, 3, 5 ], 3)
            Traceback (most recent call last):
            ...
            ValueError: All evaluation points must be different

        The dimension is not allowed to exceed the length::

            sage: F = GF(59)
            sage: n, k = 40, 100
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            Traceback (most recent call last):
            ...
            ValueError: The dimension must be a positive integer at most the length of the code.
        """
    def __eq__(self, other):
        """
        Test equality between Generalized Reed-Solomon codes.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C1 = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C2 = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C1 == C2
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C1 = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C2 = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: hash(C1) == hash(C2)
            True
        """
    def minimum_distance(self):
        """
        Return the minimum distance between any two words in ``self``.

        Since a GRS code is always Maximum-Distance-Separable (MDS),
        this returns ``C.length() - C.dimension() + 1``.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.minimum_distance()
            29
        """
    def evaluation_points(self):
        """
        Return the vector of field elements used for the polynomial evaluations.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.evaluation_points()
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        """
    def column_multipliers(self):
        """
        Return the vector of column multipliers of ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.column_multipliers()
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        """
    def is_generalized(self):
        """
        Return whether ``self`` is a Generalized Reed-Solomon code or
        a regular Reed-Solomon code.

        ``self`` is a Generalized Reed-Solomon code if its column multipliers
        are not all 1.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.column_multipliers()
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            sage: C.is_generalized()
            False
            sage: colmults = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
            sage: C2 = codes.GeneralizedReedSolomonCode(F.list()[:n], k, colmults)
            sage: C2.is_generalized()
            True
        """
    @cached_method
    def multipliers_product(self):
        """
        Return the component-wise product of the column multipliers of ``self``
        with the column multipliers of the dual GRS code.

        This is a simple Cramer's rule-like expression on the evaluation points
        of ``self``. Recall that the column multipliers of the dual GRS code are
        also the column multipliers of the parity check matrix of ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.multipliers_product()
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        """
    @cached_method
    def parity_column_multipliers(self):
        """
        Return the list of column multipliers of the parity check matrix of
        ``self``. They are also column multipliers of the generator matrix for
        the dual GRS code of ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.parity_column_multipliers()
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        """
    @cached_method
    def parity_check_matrix(self):
        """
        Return the parity check matrix of ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.parity_check_matrix()
            [10  9  8  7  6  5  4  3  2  1]
            [ 0  9  5 10  2  3  2 10  5  9]
            [ 0  9 10  8  8  4  1  4  7  4]
            [ 0  9  9  2 10  9  6  6  1  3]
            [ 0  9  7  6  7  1  3  9  8  5]
        """
    @cached_method
    def dual_code(self):
        """
        Return the dual code of ``self``, which is also a GRS code.

        EXAMPLES::

            sage: F =  GF(59)
            sage: colmults = [ F._random_nonzero_element() for i in range(40) ]
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:40], 12, colmults)
            sage: Cd = C.dual_code(); Cd
            [40, 28, 13] Generalized Reed-Solomon Code over GF(59)

        The dual code of the dual code is the original code::

            sage: C == Cd.dual_code()
            True
        """
    def covering_radius(self):
        """
        Return the covering radius of ``self``.

        The covering radius of a linear code `C` is the smallest
        number `r` s.t. any element of the ambient space of `C` is
        at most at distance `r` to `C`.

        As GRS codes are Maximum Distance Separable codes (MDS), their covering
        radius is always `d-1`, where `d` is the minimum distance. This is
        opposed to random linear codes where the covering radius is
        computationally hard to determine.

        EXAMPLES::

            sage: F = GF(2^8, 'a')
            sage: n, k = 256, 100
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.covering_radius()
            156
        """
    @cached_method
    def weight_distribution(self):
        """
        Return the list whose `i`-th entry is the number of words of weight `i`
        in ``self``.

        Computing the weight distribution for a GRS code is very fast. Note that
        for random linear codes, it is computationally hard.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: C.weight_distribution()                                               # needs sage.symbolic
            [1, 0, 0, 0, 0, 0, 2100, 6000, 29250, 61500, 62200]

        TESTS:

        Test that this method agrees with the generic algorithm::

            sage: F = GF(7)
            sage: C = codes.GeneralizedReedSolomonCode(F.list(), 3)
            sage: C.weight_distribution() == super(codes.GeneralizedReedSolomonCode, C).weight_distribution()  # long time, needs sage.symbolic
            True
            sage: F = GF(8)
            sage: C = codes.GeneralizedReedSolomonCode(F.list(), 3)
            sage: C.weight_distribution() == super(codes.GeneralizedReedSolomonCode, C).weight_distribution()  # long time, needs sage.symbolic
            True
        """

def ReedSolomonCode(base_field, length, dimension, primitive_root=None):
    """
    Construct a classical Reed-Solomon code.

    A classical `[n,k]` Reed-Solomon code over `\\GF{q}` with `1 \\le k \\le n` and
    `n | (q-1)` is a Reed-Solomon code whose evaluation points are the
    consecutive powers of a primitive `n`-th root of unity `\\alpha`, i.e.
    `\\alpha_i = \\alpha^{i-1}`, where `\\alpha_1, \\ldots, \\alpha_n` are the
    evaluation points. A classical Reed-Solomon codes has all column multipliers
    equal `1`.

    Classical Reed-Solomon codes are cyclic, unlike most Generalized
    Reed-Solomon codes.

    Use :class:`GeneralizedReedSolomonCode` if you instead wish to construct
    non-classical Reed-Solomon and Generalized Reed-Solomon codes.

    INPUT:

    - ``base_field`` -- the finite field for which to build the classical
      Reed-Solomon code

    - ``length`` -- the length of the classical Reed-Solomon code. Must divide
      `q-1` where `q` is the cardinality of ``base_field``

    - ``dimension`` -- the dimension of the resulting code

    - ``primitive_root`` -- (default: ``None``) a primitive `n`-th root of unity
      to use for constructing the classical Reed-Solomon code; if not supplied,
      one will be computed and can be recovered as ``C.evaluation_points()[1]``
      where `C` is the code returned by this method

    EXAMPLES::

        sage: C = codes.ReedSolomonCode(GF(7), 6, 3); C
        [6, 3, 4] Reed-Solomon Code over GF(7)

    This code is cyclic as can be seen by coercing it into a cyclic code::

        sage: Ccyc = codes.CyclicCode(code=C); Ccyc
        [6, 3] Cyclic Code over GF(7)

        sage: Ccyc.generator_polynomial()
        x^3 + 3*x^2 + x + 6

    Another example over an extension field::

        sage: C = codes.ReedSolomonCode(GF(64,'a'), 9, 4); C
        [9, 4, 6] Reed-Solomon Code over GF(64)

    The primitive `n`-th root of unity can be recovered as the 2nd evaluation point of the code::

        sage: alpha = C.evaluation_points()[1]; alpha
        a^5 + a^4 + a^2 + a

    We can also supply a different primitive `n`-th root of unity::

        sage: beta = alpha^2; beta
        a^4 + a
        sage: beta.multiplicative_order()
        9
        sage: D = codes.ReedSolomonCode(GF(64), 9, 4, primitive_root=beta); D
        [9, 4, 6] Reed-Solomon Code over GF(64)
        sage: C == D
        False
    """

class GRSEvaluationVectorEncoder(Encoder):
    '''
    Encoder for (Generalized) Reed-Solomon codes that encodes vectors
    into codewords.

    Let `C` be a GRS code of length `n` and dimension `k` over some
    finite field `F`. We denote by `\\alpha_i` its evaluations points
    and by `\\beta_i` its column multipliers, where `1 \\leq i \\leq n`.
    Let `m = (m_1, \\dots, m_k)`, a vector over `F`, be the message.
    We build a polynomial using the coordinates of `m` as coefficients:

    .. MATH::

        p = \\Sigma_{i=1}^{m} m_i  x^i.

    The encoding of `m` will be the following codeword:

    .. MATH::

        (\\beta_1  p(\\alpha_1), \\dots, \\beta_n  p(\\alpha_n)).

    INPUT:

    - ``code`` -- the associated code of this encoder

    EXAMPLES::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
        sage: E = codes.encoders.GRSEvaluationVectorEncoder(C)
        sage: E
        Evaluation vector-style encoder for [40, 12, 29] Reed-Solomon Code over GF(59)

    Actually, we can construct the encoder from ``C`` directly::

        sage: E = C.encoder("EvaluationVector")
        sage: E
        Evaluation vector-style encoder for [40, 12, 29] Reed-Solomon Code over GF(59)
    '''
    def __init__(self, code) -> None:
        """
        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = codes.encoders.GRSEvaluationVectorEncoder(C)
            sage: E
            Evaluation vector-style encoder for [40, 12, 29] Reed-Solomon Code over GF(59)
        """
    def __eq__(self, other):
        """
        Test equality between GRSEvaluationVectorEncoder objects.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D1 = codes.encoders.GRSEvaluationVectorEncoder(C)
            sage: D2 = codes.encoders.GRSEvaluationVectorEncoder(C)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    @cached_method
    def generator_matrix(self):
        """
        Return a generator matrix of ``self``.

        Considering a GRS code of length `n`, dimension `k`, with
        evaluation points `(\\alpha_1, \\dots, \\alpha_n)` and column multipliers
        `(\\beta_1, \\dots, \\beta_n)`, its generator matrix `G` is built using
        the following formula:

        .. MATH::

            G = [g_{i,j}], g_{i,j} = \\beta_j \\alpha_{j}^{i}.

        This matrix is a Vandermonde matrix.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10, 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = codes.encoders.GRSEvaluationVectorEncoder(C)
            sage: E.generator_matrix()
            [1 1 1 1 1 1 1 1 1 1]
            [0 1 2 3 4 5 6 7 8 9]
            [0 1 4 9 5 3 3 5 9 4]
            [0 1 8 5 9 4 7 2 6 3]
            [0 1 5 4 3 9 9 3 4 5]
        """

class GRSEvaluationPolynomialEncoder(Encoder):
    '''
    Encoder for (Generalized) Reed-Solomon codes which uses evaluation of
    polynomials to obtain codewords.

    Let `C` be a GRS code of length `n` and dimension `k` over some
    finite field `F`. We denote by `\\alpha_i` its evaluations points
    and by `\\beta_i` its column multipliers, where `1 \\leq i \\leq n`.
    Let `p` be a polynomial of degree at most `k-1` in `F[x]` be the message.

    The encoding of `m` will be the following codeword:

    .. MATH::

        (\\beta_1 p(\\alpha_1), \\dots, \\beta_n p(\\alpha_n)).

    INPUT:

    - ``code`` -- the associated code of this encoder

    - ``polynomial_ring`` -- (default: ``None``) a polynomial ring to specify
      the message space of ``self``, if needed; it is set to `F[x]` (where `F`
      is the base field of ``code``) if default value is kept

    EXAMPLES::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
        sage: E = codes.encoders.GRSEvaluationPolynomialEncoder(C)
        sage: E
        Evaluation polynomial-style encoder for [40, 12, 29] Reed-Solomon Code over GF(59)
        sage: E.message_space()
        Univariate Polynomial Ring in x over Finite Field of size 59

    Actually, we can construct the encoder from ``C`` directly::

        sage: E = C.encoder("EvaluationPolynomial")
        sage: E
        Evaluation polynomial-style encoder for [40, 12, 29] Reed-Solomon Code over GF(59)

    We can also specify another polynomial ring::

        sage: R = PolynomialRing(F, \'y\')
        sage: E = C.encoder("EvaluationPolynomial", polynomial_ring=R)
        sage: E.message_space()
        Univariate Polynomial Ring in y over Finite Field of size 59
    '''
    def __init__(self, code, polynomial_ring=None) -> None:
        """
        TESTS:

        If ``polynomial_ring`` is not a polynomial ring, an exception
        is raised::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = codes.encoders.GRSEvaluationPolynomialEncoder(C, polynomial_ring = F)
            Traceback (most recent call last):
            ...
            ValueError: polynomial_ring has to be a univariate polynomial ring

        Same if ``polynomial_ring`` is a multivariate polynomial ring::

            sage: Fxy.<x,y> = F[]
            sage: E = codes.encoders.GRSEvaluationPolynomialEncoder(C, polynomial_ring = Fxy)
            Traceback (most recent call last):
            ...
            ValueError: polynomial_ring has to be a univariate polynomial ring

        ``polynomial_ring``'s base field and ``code``'s base field have to be the same::

            sage: Gx.<x> = GF(7)[]
            sage: E = codes.encoders.GRSEvaluationPolynomialEncoder(C, polynomial_ring = Gx)
            Traceback (most recent call last):
            ...
            ValueError: polynomial_ring's base field has to be the same as code's
        """
    def __eq__(self, other):
        """
        Test equality between GRSEvaluationPolynomialEncoder objects.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D1 = codes.encoders.GRSEvaluationPolynomialEncoder(C)
            sage: D2 = codes.encoders.GRSEvaluationPolynomialEncoder(C)
            sage: D1 is D2
            False
            sage: D1.__eq__(D2)
            True
            sage: R = PolynomialRing(F, 'y')
            sage: D3 = codes.encoders.GRSEvaluationPolynomialEncoder(C, polynomial_ring=R)
            sage: D1.__eq__(D3)
            False
        """
    def encode(self, p):
        '''
        Transform the polynomial ``p`` into a codeword of :meth:`code`.

        One can use the following shortcut to encode a word with
        an encoder ``E``::

            E(word)

        INPUT:

        - ``p`` -- a polynomial from the message space of ``self`` of degree
          less than ``self.code().dimension()``

        OUTPUT: a codeword in associated code of ``self``

        EXAMPLES::

            sage: F = GF(11)
            sage: Fx.<x> = F[]
            sage: n, k = 10 , 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: p = x^2 + 3*x + 10
            sage: c = E.encode(p); c
            (10, 3, 9, 6, 5, 6, 9, 3, 10, 8)
            sage: c in C
            True

        If a polynomial of too high degree is given, an error is raised::

            sage: p = x^10
            sage: E.encode(p)
            Traceback (most recent call last):
            ...
            ValueError: The polynomial to encode must have degree at most 4

        If ``p`` is not an element of the proper polynomial ring, an error is raised::

            sage: Qy.<y> = QQ[]
            sage: p = y^2 + 1
            sage: E.encode(p)
            Traceback (most recent call last):
            ...
            ValueError: The value to encode must be in
            Univariate Polynomial Ring in x over Finite Field of size 11

        TESTS:

        The bug described in :issue:`20744` is now fixed::

            sage: F = GF(11)
            sage: Fm.<my_variable> = F[]
            sage: n, k = 10 , 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = C.encoder("EvaluationPolynomial", polynomial_ring = Fm)
            sage: p = my_variable^2 + 3*my_variable + 10
            sage: c = E.encode(p)
            sage: c in C
            True
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

        - a polynomial of degree less than ``self.code().dimension()``

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10 , 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: c = vector(F, (10, 3, 9, 6, 5, 6, 9, 3, 10, 8))
            sage: c in C
            True
            sage: p = E.unencode_nocheck(c); p
            x^2 + 3*x + 10
            sage: E.encode(p) == c
            True

        Note that no error is thrown if ``c`` is not a codeword, and that the
        result is undefined::

            sage: c = vector(F, (11, 3, 9, 6, 5, 6, 9, 3, 10, 8))
            sage: c in C
            False
            sage: p = E.unencode_nocheck(c); p
            6*x^4 + 6*x^3 + 2*x^2
            sage: E.encode(p) == c
            False
        '''
    def message_space(self):
        '''
        Return the message space of ``self``.

        EXAMPLES::

            sage: F = GF(11)
            sage: n, k = 10 , 5
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: E = C.encoder("EvaluationPolynomial")
            sage: E.message_space()
            Univariate Polynomial Ring in x over Finite Field of size 11
        '''
    polynomial_ring = message_space

class GRSBerlekampWelchDecoder(Decoder):
    '''
    Decoder for (Generalized) Reed-Solomon codes which uses Berlekamp-Welch
    decoding algorithm to correct errors in codewords.

    This algorithm recovers the error locator polynomial by solving a
    linear system. See [HJ2004]_ pp. 51-52 for details.

    INPUT:

    - ``code`` -- a code associated to this decoder

    EXAMPLES::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
        sage: D = codes.decoders.GRSBerlekampWelchDecoder(C)
        sage: D
        Berlekamp-Welch decoder for [40, 12, 29] Reed-Solomon Code over GF(59)

    Actually, we can construct the decoder from ``C`` directly::

        sage: D = C.decoder("BerlekampWelch")
        sage: D
        Berlekamp-Welch decoder for [40, 12, 29] Reed-Solomon Code over GF(59)
    '''
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a GRS code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.decoders.GRSBerlekampWelchDecoder(C)
            Traceback (most recent call last):
            ...
            ValueError: code has to be a generalized Reed-Solomon code
        """
    def __eq__(self, other):
        """
        Test equality between GRSBerlekampWelchDecoder objects.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D1 = codes.decoders.GRSBerlekampWelchDecoder(C)
            sage: D2 = codes.decoders.GRSBerlekampWelchDecoder(C)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    def decode_to_message(self, r):
        '''
        Decode ``r`` to an element in message space of ``self``.

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be unencoded as is. In that case,
            if ``r`` is not a codeword, the output is unspecified.

        INPUT:

        - ``r`` -- a codeword of ``self``

        OUTPUT: a vector of ``self`` message space

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSBerlekampWelchDecoder(C)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: D.connected_encoder().unencode(c) == D.decode_to_message(y)
            True

        TESTS:

        If one tries to decode a word which is too far from any codeword, an exception is raised::

            sage: e = vector(F,[0, 0, 54, 23, 1, 0, 0, 0, 53, 21, 0, 0, 0, 34, 6, 11, 0, 0, 16, 0, 0, 0, 9, 0, 10, 27, 35, 0, 0, 0, 0, 46, 0, 0, 0, 0, 0, 0, 44, 0]); e.hamming_weight()
            15
            sage: D.decode_to_message(c + e)
            Traceback (most recent call last):
            ...
            DecodingError: Decoding failed because the number of errors exceeded the decoding radius

        If one tries to decode something which is not in the ambient space of the code,
        an exception is raised::

            sage: D.decode_to_message(42)
            Traceback (most recent call last):
            ...
            ValueError: The word to decode has to be in the ambient space of the code

        The bug detailed in :issue:`20340` has been fixed::

            sage: C = codes.GeneralizedReedSolomonCode(GF(59).list()[:40], 12)
            sage: c = C.random_element()
            sage: D = C.decoder("BerlekampWelch")
            sage: E = D.connected_encoder()
            sage: m = E.message_space().random_element()
            sage: c = E.encode(m)
            sage: D.decode_to_message(c) == m
            True
        '''
    def decode_to_code(self, r):
        '''
        Correct the errors in ``r`` and returns a codeword.

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be returned as is.

        INPUT:

        - ``r`` -- a vector of the ambient space of ``self.code()``

        OUTPUT:

        - a vector of ``self.code()``

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSBerlekampWelchDecoder(C)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: c == D.decode_to_code(y)
            True

        TESTS:

        If one tries to decode a word which is too far from any codeword, an exception is raised::

            sage: e = vector(F,[0, 0, 54, 23, 1, 0, 0, 0, 53, 21, 0, 0, 0, 34, 6, 11, 0, 0, 16, 0, 0, 0, 9, 0, 10, 27, 35, 0, 0, 0, 0, 46, 0, 0, 0, 0, 0, 0, 44, 0]); e.hamming_weight()
            15
            sage: D.decode_to_code(c + e)
            Traceback (most recent call last):
            ...
            DecodingError: Decoding failed because the number of errors exceeded the decoding radius

        If one tries to decode something which is not in the ambient space of the code,
        an exception is raised::

            sage: D.decode_to_code(42)
            Traceback (most recent call last):
            ...
            ValueError: The word to decode has to be in the ambient space of the code

        The bug detailed in :issue:`20340` has been fixed::

            sage: C = codes.GeneralizedReedSolomonCode(GF(59).list()[:40], 12)
            sage: c = C.random_element()
            sage: D = C.decoder("BerlekampWelch")
            sage: D.decode_to_code(c) == c
            True
        '''
    def decoding_radius(self):
        """
        Return maximal number of errors that ``self`` can decode.

        OUTPUT: the number of errors as an integer

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSBerlekampWelchDecoder(C)
            sage: D.decoding_radius()
            14
        """

class GRSGaoDecoder(Decoder):
    '''
    Decoder for (Generalized) Reed-Solomon codes which uses Gao
    decoding algorithm to correct errors in codewords.

    Gao decoding algorithm uses early terminated extended Euclidean algorithm
    to find the error locator polynomial. See [Ga02]_ for details.

    INPUT:

    - ``code`` -- the associated code of this decoder

    EXAMPLES::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
        sage: D = codes.decoders.GRSGaoDecoder(C)
        sage: D
        Gao decoder for [40, 12, 29] Reed-Solomon Code over GF(59)

    Actually, we can construct the decoder from ``C`` directly::

        sage: D = C.decoder("Gao")
        sage: D
        Gao decoder for [40, 12, 29] Reed-Solomon Code over GF(59)
    '''
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a GRS code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.decoders.GRSGaoDecoder(C)
            Traceback (most recent call last):
            ...
            ValueError: code has to be a generalized Reed-Solomon code
        """
    def __eq__(self, other):
        """
        Test equality of GRSGaoDecoder objects.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D1 = codes.decoders.GRSGaoDecoder(C)
            sage: D2 = codes.decoders.GRSGaoDecoder(C)
            sage: D1 == D2
            True
            sage: D1 is D2
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D1 = codes.decoders.GRSGaoDecoder(C)
            sage: D2 = codes.decoders.GRSGaoDecoder(C)
            sage: hash(D1) == hash(D2)
            True
        """
    def decode_to_message(self, r):
        '''
        Decode ``r`` to an element in message space of ``self``.

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be unencoded as is. In that case,
            if ``r`` is not a codeword, the output is unspecified.

        INPUT:

        - ``r`` -- a codeword of ``self``

        OUTPUT: a vector of ``self`` message space

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSGaoDecoder(C)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: D.connected_encoder().unencode(c) == D.decode_to_message(y)
            True

        TESTS:

        If one tries to decode a word which is too far from any codeword, an exception is raised::

            sage: e = vector(F,[0, 0, 54, 23, 1, 0, 0, 0, 53, 21, 0, 0, 0, 34, 6, 11, 0, 0, 16, 0, 0, 0, 9, 0, 10, 27, 35, 0, 0, 0, 0, 46, 0, 0, 0, 0, 0, 0, 44, 0]); e.hamming_weight()
            15
            sage: D.decode_to_message(c + e)
            Traceback (most recent call last):
            ...
            DecodingError: Decoding failed because the number of errors exceeded the decoding radius

        If one tries to decode something which is not in the ambient space of the code,
        an exception is raised::

            sage: D.decode_to_message(42)
            Traceback (most recent call last):
            ...
            ValueError: The word to decode has to be in the ambient space of the code

        The bug detailed in :issue:`20340` has been fixed::

            sage: C = codes.GeneralizedReedSolomonCode(GF(59).list()[:40], 12)
            sage: c = C.random_element()
            sage: D = C.decoder("Gao")
            sage: E = D.connected_encoder()
            sage: m = E.message_space().random_element()
            sage: c = E.encode(m)
            sage: D.decode_to_message(c) == m
            True
        '''
    def decode_to_code(self, r):
        '''
        Correct the errors in ``r`` and returns a codeword.

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be returned as is.

        INPUT:

        - ``r`` -- a vector of the ambient space of ``self.code()``

        OUTPUT:

        - a vector of ``self.code()``

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSGaoDecoder(C)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: c == D.decode_to_code(y)
            True

        TESTS:


        If one tries to decode a word which is too far from any codeword, an exception is raised::

            sage: e = vector(F,[0, 0, 54, 23, 1, 0, 0, 0, 53, 21, 0, 0, 0, 34, 6, 11, 0, 0, 16, 0, 0, 0, 9, 0, 10, 27, 35, 0, 0, 0, 0, 46, 0, 0, 0, 0, 0, 0, 44, 0]); e.hamming_weight()
            15
            sage: D.decode_to_code(c + e)
            Traceback (most recent call last):
            ...
            DecodingError: Decoding failed because the number of errors exceeded the decoding radius

        If one tries to decode something which is not in the ambient space of the code,
        an exception is raised::

            sage: D.decode_to_code(42)
            Traceback (most recent call last):
            ...
            ValueError: The word to decode has to be in the ambient space of the code

        The bug detailed in :issue:`20340` has been fixed::

            sage: C = codes.GeneralizedReedSolomonCode(GF(59).list()[:40], 12)
            sage: c = C.random_element()
            sage: D = C.decoder("Gao")
            sage: c = C.random_element()
            sage: D.decode_to_code(c) == c
            True
        '''
    def decoding_radius(self):
        """
        Return maximal number of errors that ``self`` can decode.

        OUTPUT: the number of errors as an integer

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSGaoDecoder(C)
            sage: D.decoding_radius()
            14
        """

class GRSErrorErasureDecoder(Decoder):
    '''
    Decoder for (Generalized) Reed-Solomon codes which is able to correct both
    errors and erasures in codewords.

    Let `C` be a GRS code of length `n` and dimension `k`.
    Considering `y` a codeword with at most `t` errors
    (`t` being the `\\left\\lfloor \\frac{d-1}{2} \\right\\rfloor`
    decoding radius), and `e` the erasure vector,
    this decoder works as follows:

    - Puncture the erased coordinates which are identified in `e`.
    - Create a new GRS code of length `n - w(e)`, where `w` is
      the Hamming weight function, and dimension `k`.
    - Use Gao decoder over this new code one the punctured word built on
      the first step.
    - Recover the original message from the decoded word computed on the
      previous step.
    - Encode this message using an encoder over `C`.

    INPUT:

    - ``code`` -- the associated code of this decoder

    EXAMPLES::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
        sage: D = codes.decoders.GRSErrorErasureDecoder(C)
        sage: D
        Error-Erasure decoder for [40, 12, 29] Reed-Solomon Code over GF(59)

    Actually, we can construct the decoder from ``C`` directly::

        sage: D = C.decoder("ErrorErasure")
        sage: D
        Error-Erasure decoder for [40, 12, 29] Reed-Solomon Code over GF(59)
    '''
    def __init__(self, code) -> None:
        """
        TESTS:

        If ``code`` is not a GRS code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.decoders.GRSErrorErasureDecoder(C)
            Traceback (most recent call last):
            ...
            ValueError: code has to be a generalized Reed-Solomon code
        """
    def __eq__(self, other):
        """
        Test equality of GRSErrorErasureDecoder objects.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D1 = codes.decoders.GRSErrorErasureDecoder(C)
            sage: D2 = codes.decoders.GRSErrorErasureDecoder(C)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    def decode_to_message(self, word_and_erasure_vector):
        """
        Decode ``word_and_erasure_vector`` to an element in message space
        of ``self``

        INPUT:

        - ``word_and_erasure_vector`` -- tuple whose:

          * first element is an element of the ambient space of the code
          * second element is a vector over `\\GF{2}` whose length is the
            same as the code's, containing erasure positions

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be unencoded as is.
            If the number of erasures is exactly `n - k`, where `n` is the
            length of the code associated to ``self`` and `k` its dimension,
            ``r`` will be returned as is.
            In either case, if ``r`` is not a codeword,
            the output is unspecified.

        OUTPUT: a vector of ``self`` message space

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSErrorErasureDecoder(C)
            sage: c = C.random_element()
            sage: n_era = randint(0, C.minimum_distance() - 2)
            sage: Chan = channels.ErrorErasureChannel(C.ambient_space(),
            ....:                                     D.decoding_radius(n_era), n_era)
            sage: y = Chan(c)
            sage: D.connected_encoder().unencode(c) == D.decode_to_message(y)
            True
            sage: n_era = C.minimum_distance() - 1
            sage: Chan = channels.ErrorErasureChannel(C.ambient_space(),
            ....:                                     D.decoding_radius(n_era), n_era)
            sage: y = Chan(c)
            sage: D.connected_encoder().unencode(c) == D.decode_to_message(y)
            True

        TESTS:

        If one tries to decode a word with too many erasures, it returns
        an exception::

            sage: Chan = channels.ErrorErasureChannel(C.ambient_space(), 0, C.minimum_distance() + 1)
            sage: y = Chan(c)
            sage: D.decode_to_message(y)
            Traceback (most recent call last):
            ...
            DecodingError: Too many erasures in the received word

        If one tries to decode something which is not in the ambient space of the code,
        an exception is raised::

            sage: D.decode_to_message((42, random_vector(GF(2), C.length())))
            Traceback (most recent call last):
            ...
            ValueError: The word to decode has to be in the ambient space of the code

        If one tries to pass an erasure_vector which is not a vector over GF(2) of the same length as code's,
        an exception is raised::

            sage: D.decode_to_message((C.random_element(), 42))
            Traceback (most recent call last):
            ...
            ValueError: The erasure vector has to be a vector over GF(2) of the same length as the code
        """
    def decoding_radius(self, number_erasures):
        """
        Return maximal number of errors that ``self`` can decode according
        to how many erasures it receives.

        INPUT:

        - ``number_erasures`` -- the number of erasures when we try to decode

        OUTPUT: the number of errors as an integer

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: D = codes.decoders.GRSErrorErasureDecoder(C)
            sage: D.decoding_radius(5)
            11

        If we receive too many erasures, it returns an exception as codeword will
        be impossible to decode::

            sage: D.decoding_radius(30)
            Traceback (most recent call last):
            ...
            ValueError: The number of erasures exceed decoding capability
        """

class GRSKeyEquationSyndromeDecoder(Decoder):
    '''
    Decoder for (Generalized) Reed-Solomon codes which uses a
    Key equation decoding based on the syndrome polynomial to
    correct errors in codewords.

    This algorithm uses early terminated extended euclidean algorithm
    to solve the key equations, as described in [Rot2006]_, pp. 183-195.

    INPUT:

    - ``code`` -- the associated code of this decoder

    EXAMPLES::

        sage: F = GF(59)
        sage: n, k = 40, 12
        sage: C = codes.GeneralizedReedSolomonCode(F.list()[1:n+1], k)
        sage: D = codes.decoders.GRSKeyEquationSyndromeDecoder(C)
        sage: D
        Key equation decoder for [40, 12, 29] Reed-Solomon Code over GF(59)

    Actually, we can construct the decoder from ``C`` directly::

        sage: D = C.decoder("KeyEquationSyndrome")
        sage: D
        Key equation decoder for [40, 12, 29] Reed-Solomon Code over GF(59)
    '''
    def __init__(self, code) -> None:
        """
        TESTS::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[:n], k)
            sage: codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            Traceback (most recent call last):
            ...
            ValueError: Impossible to use this decoder over a GRS code which contains 0 amongst its evaluation points

        If ``code`` is not a GRS code, an error is raised::

            sage: C  = codes.random_linear_code(GF(11), 10, 4)
            sage: codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            Traceback (most recent call last):
            ...
            ValueError: code has to be a generalized Reed-Solomon code
        """
    def __eq__(self, other):
        """
        Test equality of GRSKeyEquationSyndromeDecoder objects.

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[1:n+1], k)
            sage: D1 = codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            sage: D2 = codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            sage: D1.__eq__(D2)
            True
            sage: D1 is D2
            False
        """
    def decode_to_code(self, r):
        """
        Correct the errors in ``r`` and returns a codeword.

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be returned as is.

        INPUT:

        - ``r`` -- a vector of the ambient space of ``self.code()``

        OUTPUT:

        - a vector of ``self.code()``

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[1:n+1], k)
            sage: D = codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: c == D.decode_to_code(y)
            True

        TESTS:

        If one tries to decode a word with too many errors, it returns
        an exception::

            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(), D.decoding_radius()+1)
            sage: while True:
            ....:     try:
            ....:         y = Chan(c)
            ....:         D.decode_to_message(y)
            ....:     except ZeroDivisionError:
            ....:         pass
            Traceback (most recent call last):
            ...
            DecodingError: Decoding failed because the number of errors exceeded the decoding radius

        If one tries to decode something which is not in the ambient space of the code,
        an exception is raised::

            sage: D.decode_to_code(42)
            Traceback (most recent call last):
            ...
            ValueError: The word to decode has to be in the ambient space of the code
        """
    def decode_to_message(self, r):
        """
        Decode ``r`` to an element in message space of ``self``.

        .. NOTE::

            If the code associated to ``self`` has the same length as its
            dimension, ``r`` will be unencoded as is. In that case,
            if ``r`` is not a codeword, the output is unspecified.

        INPUT:

        - ``r`` -- a codeword of ``self``

        OUTPUT: a vector of ``self`` message space

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[1:n+1], k)
            sage: D = codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            sage: c = C.random_element()
            sage: Chan = channels.StaticErrorRateChannel(C.ambient_space(),
            ....:                                        D.decoding_radius())
            sage: y = Chan(c)
            sage: D.connected_encoder().unencode(c) == D.decode_to_message(y)
            True
        """
    def decoding_radius(self):
        """
        Return maximal number of errors that ``self`` can decode.

        OUTPUT: the number of errors as an integer

        EXAMPLES::

            sage: F = GF(59)
            sage: n, k = 40, 12
            sage: C = codes.GeneralizedReedSolomonCode(F.list()[1:n+1], k)
            sage: D = codes.decoders.GRSKeyEquationSyndromeDecoder(C)
            sage: D.decoding_radius()
            14
        """
