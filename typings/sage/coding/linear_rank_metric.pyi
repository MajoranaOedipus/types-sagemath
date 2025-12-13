from .decoder import Decoder as Decoder
from .linear_code import LinearCodeGeneratorMatrixEncoder as LinearCodeGeneratorMatrixEncoder
from .linear_code_no_metric import AbstractLinearCodeNoMetric as AbstractLinearCodeNoMetric
from sage.categories.fields import Fields as Fields
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import Infinity as Infinity
from sage.structure.element import Matrix as Matrix, Vector as Vector

def to_matrix_representation(v, sub_field=None, basis=None):
    """
    Return a matrix representation of ``v`` over ``sub_field`` in terms of
    ``basis``.

    Let `(b_1, b_2, \\ldots, b_m)`, `b_i \\in GF(q^m)`, be a basis of `\\GF{q^m}` as
    a vector space over `\\GF{q}`. Take an element `x \\in \\GF{q^m}`. We can write
    `x` as `x = u_1 b_1 + u_2 b_2 + \\ldots u_m b_m`, where `u_i \\in GF(q)`. This
    way we can represent an element from `\\GF{q^m}` as a vector of length `m`
    over `\\GF{q}`.

    Given a vector ``v`` of length `n` over some field `\\GF{q^m}`, we can
    represent each entry as a vector of length `m`, yielding an `m \\times n`
    matrix over ``sub_field``. In case ``sub_field`` is not given, we take the
    prime subfield `\\GF{p}` of `\\GF{q^m}`.

    INPUT:

    - ``v`` -- a vector over some field `\\GF{q^m}`

    - ``sub_field`` -- (default: ``None``) a sub field of `\\GF{q^m}`; if not
      specified, it is the prime subfield `\\GF{p}` of `\\GF{q^m}`

    - ``basis`` -- (default: ``None``) a basis of `\\GF{q^m}` as a vector space over
      ``sub_field``. If not specified, the default basis is
      `1,\\beta,\\ldots,\\beta^{m-1}` where `\\beta` is the generator of `\\GF{q^m}`
      given by SageMath.

    EXAMPLES::

        sage: from sage.coding.linear_rank_metric import to_matrix_representation
        sage: x = GF(64).gen()
        sage: a = vector(GF(64), (x + 1, x + 1, 1))
        sage: to_matrix_representation(a, GF(4))
        [1 1 1]
        [1 1 0]
        [0 0 0]

        sage: m = Matrix(GF(4), [[1, 1, 1], [1, 1, 0], [0, 0, 0]])
        sage: to_matrix_representation(m)
        Traceback (most recent call last):
        ...
        TypeError: Input must be a vector
    """
def from_matrix_representation(w, base_field=None, basis=None):
    """
    Return a vector representation of a matrix ``w`` over ``base_field`` in terms
    of ``basis``.

    Given an `m \\times n` matrix over `\\GF{q}` and some ``basis`` of `\\GF{q^m}`
    over `\\GF{q}`, we can represent each of its columns as an element of `\\GF{q^m}`,
    yielding a vector of length `n` over `\\GF{q}`.

    In case ``base_field`` is not given, we take `\\GF{q^m}`, the field extension of
    `\\GF{q}` of degree `m`, the number of rows of ``w``.

    INPUT:

    - ``w`` -- a matrix over some field `\\GF{q}`

    - ``base_field`` -- (default: ``None``) an extension field of `\\GF{q}`. If not
      specified, it is the field `\\GF{q^m}`, where `m` is the number of rows of
      ``w``.

    - ``basis`` -- (default: ``None``) a basis of `\\GF{q^m}` as a vector space over
      `\\GF{q}`. If not specified, the default basis is
      `1,\\beta,\\ldots,\\beta^{m-1}` where `\\beta` is the generator
      of `\\GF{q^m}` given by SageMath.

    EXAMPLES::

        sage: from sage.coding.linear_rank_metric import from_matrix_representation
        sage: m = Matrix(GF(4), [[1, 1, 1], [1, 1, 0], [0, 0, 0]])
        sage: from_matrix_representation(m)
        (z6 + 1, z6 + 1, 1)

        sage: v = vector(GF(4), (1, 0, 0))
        sage: from_matrix_representation(v)
        Traceback (most recent call last):
        ...
        TypeError: Input must be a matrix
    """
def rank_weight(c, sub_field=None, basis=None):
    """
    Return the rank of ``c`` as a matrix over ``sub_field``.

    If ``c`` is a vector over some field `\\GF{q^m}`, the function converts it
    into a matrix over ``sub_field```.

    INPUT:

    - ``c`` -- a vector over some field `\\GF{q^m}`; or a matrix over `\\GF{q}`

    - ``sub_field`` -- (default: ``None``) a sub field of `\\GF{q^m}`; if not
      specified, it is the prime subfield `\\GF{p}` of `\\GF{q^m}`

    - ``basis`` -- (default: ``None``) a basis of `\\GF{q^m}` as a vector space over
      ``sub_field``. If not specified, the default basis is
      `1,\\beta,\\ldots,\\beta^{m-1}` where `\\beta` is the generator
      of `\\GF{q^m}` given by SageMath.

    EXAMPLES::

        sage: from sage.coding.linear_rank_metric import rank_weight
        sage: x = GF(64).gen()
        sage: a = vector(GF(64), (x + 1, x + 1, 1))
        sage: rank_weight(a, GF(4))
        2
    """
def rank_distance(a, b, sub_field=None, basis=None):
    """
    Return the rank of ``a`` - ``b`` as a matrix over ``sub_field``.

    Take two vectors ``a``, ``b`` over some field `\\GF{q^m}`. This function
    converts them to matrices over `\\GF{q}` and calculates the rank of their
    difference.

    If ``sub_field`` is not specified, we take the prime subfield `\\GF{q}` of
    `\\GF{q^m}`.

    INPUT:

    - ``a`` -- a vector over some field `\\GF{q^m}`

    - ``b`` -- a vector over some field `\\GF{q^m}`

    - ``sub_field`` -- (default: ``None``) a sub field of `\\GF{q^m}`; if not
      specified, it is the prime subfield `\\GF{p}` of `\\GF{q^m}`

    - ``basis`` -- (default: ``None``) a basis of `\\GF{q^m}` as a vector space over
      ``sub_field``. If not specified, the default basis is
      `1,\\beta,\\ldots,\\beta^{m-1}` where `\\beta` is the generator
      of `\\GF{q^m}` given by SageMath.

    EXAMPLES::

        sage: from sage.coding.linear_rank_metric import rank_distance
        sage: x = GF(64).gen()
        sage: a = vector(GF(64), (x + 1, x + 1, 1))
        sage: b = vector(GF(64), (1, 0, 0))
        sage: rank_distance(a, b, GF(4))
        2

        sage: c = vector(GF(4), (1, 0, 0))
        sage: rank_distance(a, c, GF(4))
        Traceback (most recent call last):
        ...
        ValueError: The base field of (z6 + 1, z6 + 1, 1) and (1, 0, 0) has to be the same

        sage: d = Matrix(GF(64), (1, 0, 0))
        sage: rank_distance(a, d, GF(64))
        Traceback (most recent call last):
        ...
        TypeError: Both inputs have to be vectors

        sage: e = vector(GF(64), (1, 0))
        sage: rank_distance(a, e, GF(64))
        Traceback (most recent call last):
        ...
        ValueError: The length of (z6 + 1, z6 + 1, 1) and (1, 0) has to be the same
    """

class AbstractLinearRankMetricCode(AbstractLinearCodeNoMetric):
    """
    Abstract class for linear rank metric codes.

    This class contains methods that can be used on families of linear rank
    metric codes. Every linear rank metric code class should inherit from this
    abstract class.

    This class is intended for codes which are linear over the ``base_field``.

    Codewords of rank metric codes have two representations. They can either be
    written as a vector of length `n` over `\\GF{q^m}`, or an `m \\times n` matrix
    over `\\GF{q}`. This implementation principally uses the vector representation.
    However, one can always get the matrix representation using the
    :meth:`sage.coding.linear_rank_metric.AbstractLinearRankMetricCode.to_matrix`
    method. To go back to a vector, use the
    :meth:`sage.coding.linear_rank_metric.AbstractLinearRankMetricCode.from_matrix`
    method.

    Instructions on how to make a new family of rank metric codes is analogous
    to making a new family of linear codes over the Hamming metric, instructions
    for which are in :class:`sage.coding.linear_code.AbstractLinearCode`. For an
    example on, see
    :meth:`sage.coding.linear_rank_metric.AbstractLinearRankMetricCode.__init__`

    .. WARNING::

        A lot of methods of the abstract class rely on the knowledge of a generator matrix.
        It is thus strongly recommended to set an encoder with a generator matrix implemented
        as a default encoder.
    """
    def __init__(self, base_field, sub_field, length, default_encoder_name, default_decoder_name, basis=None) -> None:
        '''
        Initialize mandatory parameters that every linear rank metric code has.

        This method only exists for inheritance purposes as it initializes
        parameters that need to be known by every linear rank metric code.
        The class :class:`sage.coding.linear_rank_metric.AbstractLinearRankMetricCode`
        should never be directly instantiated.

        INPUT:

        - ``base_field`` -- the base field of ``self``

        - ``sub_field`` -- the sub field of ``self``

        - ``length`` -- the length of ``self`` (a Python int or a Sage Integer),
          must be > 0 and at most the degree of the field extension

        - ``default_encoder_name`` -- the name of the default encoder of ``self``

        - ``default_decoder_name`` -- the name of the default decoder of ``self``

        - ``basis`` -- (default: ``None``) a basis of `\\GF{q^m}` as a vector space over
          ``sub_field``. If not specified, the default basis is
          `1,\\beta,\\ldots,\\beta^{m-1}` where `\\beta` is the generator
          of `\\GF{q^m}` given by SageMath.

        EXAMPLES:

        The following example demonstrates how to use subclass
        `AbstractLinearRankMetricCode` for representing a new family of rank
        metric codes. The example is a rank repetition code::

             sage: from sage.coding.linear_rank_metric import AbstractLinearRankMetricCode
             sage: class RankRepetitionCode(AbstractLinearRankMetricCode):
             ....:   def __init__(self, base_field, sub_field, length):
             ....:       super().__init__(base_field, sub_field, length,
             ....:                        "GeneratorMatrix", "NearestNeighbor")
             ....:       beta = base_field.gen()
             ....:       self._generator_matrix = matrix(base_field,
             ....:                                       [[beta^i for i in range(length)]])
             ....:   def generator_matrix(self):
             ....:       return self._generator_matrix
             ....:   def _repr_(self):
             ....:       return "[%d, %d] rank-metric repetition code over GF(%s)" % (self.length(), self.dimension(), self.base_field().cardinality())

        We now instantiate a member of our newly made code family::

            sage: C = RankRepetitionCode(GF(8), GF(2), 3)

        We can check its existence and parameters::

            sage: C
            [3, 1] rank-metric repetition code over GF(8)

        We can encode a vector::

            sage: word = vector(C.base_field(), [1])
            sage: E = codes.encoders.LinearCodeSystematicEncoder(C)
            sage: codeword = E(word)
            sage: codeword
            (1, z3, z3^2)

        We can get the matrix representation of the codeword::

            sage: C.matrix_form_of_vector(codeword)
            [1 0 0]
            [0 1 0]
            [0 0 1]

        We can decode the vector representation of the codeword::

            sage: D = codes.decoders.LinearRankMetricCodeNearestNeighborDecoder(C)
            sage: D.decode_to_code(codeword)
            (1, z3, z3^2)
            sage: D.decode_to_message(codeword)
            (1)

        We can check that it is truly a part of the framework category::

            sage: C.parent()
            <class \'__main__.RankRepetitionCode_with_category\'>
            sage: C.category()
            Category of facade finite dimensional vector spaces with basis
             over Finite Field in z3 of size 2^3

        And any method that works on rank metric linear codes works for our new dummy code::

            sage: C.minimum_distance()
            3
            sage: C.metric()
            \'rank\'

        TESTS:

        If ``sub_field`` is not a field, an error is raised::

            sage: C = RankRepetitionCode(GF(8), ZZ, 3)
            Traceback (most recent call last):
            ...
            ValueError: \'sub_field\' must be a field (and Integer Ring is not one)

        If ``sub_field`` is not a subfield of ``base_field``, an error is raised::

            sage: C = RankRepetitionCode(GF(8), GF(3), 2)
            Traceback (most recent call last):
            ...
            ValueError: \'sub_field\' has to be a subfield of \'base_field\'
        '''
    def sub_field(self):
        """
        Return the sub field of ``self``.

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: C.sub_field()
            Finite Field in z2 of size 2^2
        """
    def extension_degree(self):
        """
        Return `m`, the degree of the field extension of ``self``.

        Let ``base_field`` be `\\GF{q^m}` and ``sub_field`` be `\\GF{q}`. Then this
        function returns `m`.

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: C.extension_degree()
            3
        """
    def field_extension(self):
        """
        Return the field extension of ``self``.

        Let ``base_field`` be some field `\\GF{q^m}` and ``sub_field`` `\\GF{q}`.
        This function returns the vector space of dimension `m` over `\\GF{q}`.

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: C.field_extension()
            Vector space of dimension 3 over Finite Field in z2 of size 2^2
        """
    def rank_distance_between_vectors(self, left, right):
        """
        Return the rank of the matrix of ``left`` - ``right``.

        INPUT:

        - ``left`` -- a vector over the ``base_field`` of ``self``

        - ``right`` -- a vector over the ``base_field`` of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: x = GF(64).gen()
            sage: a = vector(GF(64), (x + 1, x + 1, 1))
            sage: b = vector(GF(64), (1, 0, 0))
            sage: C.rank_distance_between_vectors(a, b)
            2
        """
    def minimum_distance(self):
        """
        Return the minimum distance of ``self``.

        This algorithm simply iterates over all the elements of the code and
        returns the minimum weight.

        EXAMPLES::

            sage: F.<a> = GF(8)
            sage: G = Matrix(F, [[1,a,a^2,0]])
            sage: C = codes.LinearRankMetricCode(G, GF(2))
            sage: C.minimum_distance()
            3
        """
    def rank_weight_of_vector(self, word):
        """
        Return the weight of the word, i.e. its rank.

        INPUT:

        - ``word`` -- a vector over the ``base_field`` of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: x = GF(64).gen()
            sage: a = vector(GF(64), (x + 1, x + 1, 1))
            sage: C.rank_weight_of_vector(a)
            2
        """
    def rank_support_of_vector(self, word, sub_field=None, basis=None):
        """
        Return the rank support of ``word`` over ``sub_field``, i.e. the  vector space over
        ``sub_field`` generated by its coefficients.

        If ``word`` is a vector over some field `\\GF{q^m}`, and ``sub_field`` is a subfield of
        `\\GF{q^m}`, the function converts it into a matrix over ``sub_field``, with
        respect to the basis ``basis``.

        INPUT:

        - ``word`` -- a vector over the ``base_field`` of ``self``.

        - ``sub_field`` -- (default: ``None``) a sub field of the
          ``base_field`` of ``self``; if not specified, it is the prime
          subfield of `\\GF{p}` the ``base_field`` of ``self``.

        - ``basis`` -- (default: ``None``) a basis of ``base_field`` of
          ``self`` as a vector space over ``sub_field``. If not specified,
          the default basis is `1,\\beta,\\ldots,\\beta^{m-1}`, where `\\beta` is
          the generator of `\\GF{q^m}` given by SageMath.

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: a = GF(64).gen()
            sage: c = vector([a^4 + a^3 + 1, a^4 + a^3 + 1, a^4 + a^3 + a^2 + 1])
            sage: c in C
            True
            sage: C.rank_support_of_vector(c)
            Vector space of degree 6 and dimension 2 over Finite Field of size 2
            Basis matrix:
            [1 0 0 1 1 0]
            [0 0 1 0 0 0]

        An example with a non canonical basis::

            sage: K.<a> = GF(2^3)
            sage: G = Matrix(K, [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G)
            sage: c = vector([a^2, a^2, 0])
            sage: basis = [a, a+1, a^2]
            sage: C.rank_support_of_vector(c, basis=basis)
            Vector space of degree 3 and dimension 1 over Finite Field of size 2
            Basis matrix:
            [0 0 1]

        TESTS::

            sage: C.rank_support_of_vector(c, GF(2^4))
            Traceback (most recent call last):
            ...
            TypeError: the input subfield Finite Field in z4 of size 2^4 is not a subfield of Finite Field in a of size 2^3
        """
    def matrix_form_of_vector(self, word):
        """
        Return the matrix representation of a word.

        INPUT:

        - ``word`` -- a vector over the ``base_field`` of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: x = GF(64).gen()
            sage: a = vector(GF(64), (x + 1, x + 1, 1))
            sage: C.matrix_form_of_vector(a)
            [1 1 1]
            [1 1 0]
            [0 0 0]
        """
    def vector_form_of_matrix(self, word):
        """
        Return the vector representation of a word.

        INPUT:

        - ``word`` -- a matrix over the ``sub_field`` of ``self``

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: x = GF(64).gen()
            sage: m = Matrix(GF(4), [[1, 1, 1], [1, 1, 0], [0, 0, 0]])
            sage: C.vector_form_of_matrix(m)
            (z6 + 1, z6 + 1, 1)
        """

class LinearRankMetricCode(AbstractLinearRankMetricCode):
    """
    Linear rank metric codes over a finite field, represented using a
    generator matrix.

    This class should be used for arbitrary and unstructured linear rank metric
    codes. This means that basic operations on the code, such as the computation
    of the minimum distance, will use generic, slow algorithms.

    If you are looking for constructing a code from a more specific family, see
    if the family has been implemented by investigating ``codes.<tab>``. These
    more specific classes use properties particular to that family to allow
    faster algorithms, and could also have family-specific methods.

    EXAMPLES::

        sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
        sage: C = codes.LinearRankMetricCode(G, GF(4))
        sage: C
        [3, 2] linear rank metric code over GF(64)/GF(4)
        sage: C.base_field()
        Finite Field in z6 of size 2^6
        sage: C.sub_field()
        Finite Field in z2 of size 2^2
        sage: C.length()
        3
        sage: C.dimension()
        2
        sage: C[2]
        (z6, z6, 0)
        sage: E = codes.encoders.LinearCodeGeneratorMatrixEncoder(C)
        sage: word = vector(C.base_field(), [1, 0])
        sage: E(word)
        (1, 1, 0)
    """
    def __init__(self, generator, sub_field=None, basis=None) -> None:
        """
        See the docstring for :meth:`LinearRankMetricCode`.

        INPUT:

        - ``generator`` -- a generator matrix over the ``base_field`` with
          dimension `k \\times n`, where `k` is the dimension of the code and
          `n` its length; or a code over a finite field

        - ``sub_field`` -- (default: ``None``) the sub field of ``self``, if not
          specified, it is the prime field of ``base_field``

        - ``basis`` -- (default: ``None``) a basis of `\\GF{q^m}` as a vector space over
          ``sub_field``. If not specified, the default basis is
          `1,\\beta,\\ldots,\\beta^{m-1}` where `\\beta` is the generator `\\GF{q^m}`
          given by SageMath.

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4)) # indirect doctest
            sage: C
            [3, 2] linear rank metric code over GF(64)/GF(4)
        """
    def generator_matrix(self, encoder_name=None, **kwargs):
        """
        Return a generator matrix of ``self``.

        INPUT:

        - ``encoder_name`` -- (default: ``None``) name of the encoder which will be
          used to compute the generator matrix. ``self._generator_matrix``
          will be returned if default value is kept.

        - ``kwargs`` -- all additional arguments are forwarded to the construction of the
          encoder that is used

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: C.generator_matrix()
            [1 1 0]
            [0 0 1]
        """

class LinearRankMetricCodeNearestNeighborDecoder(Decoder):
    """
    Construct a decoder for Linear Rank Metric Codes.

    This decoder will decode to the nearest codeword found.
    """
    def __init__(self, code) -> None:
        """

        INPUT:

        - ``code`` -- a code associated to this decoder

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: D = codes.decoders.LinearRankMetricCodeNearestNeighborDecoder(C)
            sage: D
            Nearest neighbor decoder for [3, 2] linear rank metric code over GF(64)/GF(4)
        """
    def __eq__(self, other):
        """
        Test equality between LinearRankMetricCodeNearestNeighborDecoder objects.

        EXAMPLES::

            sage: G = Matrix(GF(64), [[1,1,0], [0,0,1]])
            sage: C = codes.LinearRankMetricCode(G, GF(4))
            sage: D1 = codes.decoders.LinearRankMetricCodeNearestNeighborDecoder(C)
            sage: D2 = codes.decoders.LinearRankMetricCodeNearestNeighborDecoder(C)
            sage: D1 == D2
            True
        """
    def decode_to_code(self, r):
        """
        Corrects the errors in ``word`` and returns a codeword.

        INPUT:

        - ``r`` -- a codeword of ``self``

        OUTPUT: a vector of ``self``'s message space

        EXAMPLES::

            sage: F.<a> = GF(4)
            sage: G = Matrix(F, [[1,1,0]])
            sage: C = codes.LinearRankMetricCode(G, GF(2))
            sage: D = codes.decoders.LinearRankMetricCodeNearestNeighborDecoder(C)
            sage: D.decode_to_code(vector(F, [a, a, 1]))
            (a, a, 0)
        """
    def decoding_radius(self):
        """
        Return maximal number of errors ``self`` can decode.

        EXAMPLES::

            sage: F.<a> = GF(8)
            sage: G = Matrix(F, [[1,a,a^2,0]])
            sage: C = codes.LinearRankMetricCode(G, GF(2))
            sage: D = codes.decoders.LinearRankMetricCodeNearestNeighborDecoder(C)
            sage: D.decoding_radius()
            1
        """
