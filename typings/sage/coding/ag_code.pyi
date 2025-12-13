from .ag_code_decoders import DifferentialAGCodeEncoder as DifferentialAGCodeEncoder, DifferentialAGCodeUniqueDecoder as DifferentialAGCodeUniqueDecoder, EvaluationAGCodeEncoder as EvaluationAGCodeEncoder, EvaluationAGCodeUniqueDecoder as EvaluationAGCodeUniqueDecoder
from .linear_code import AbstractLinearCode as AbstractLinearCode, LinearCodeGeneratorMatrixEncoder as LinearCodeGeneratorMatrixEncoder, LinearCodeSyndromeDecoder as LinearCodeSyndromeDecoder
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.function_field.place import FunctionFieldPlace as FunctionFieldPlace

class AGCode(AbstractLinearCode):
    """
    Base class of algebraic geometry codes.

    A subclass of this class is required to define ``_function_field``
    attribute that refers to an abstract functiom field or the function field
    of the underlying curve used to construct a code of the class.
    """
    def base_function_field(self):
        """
        Return the function field used to construct the code.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: p = C([0,0])
            sage: Q, = p.places()
            sage: pls.remove(Q)
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(pls, G)
            sage: code.base_function_field()
            Function field in y defined by y^2 + y + x^3
        """

class EvaluationAGCode(AGCode):
    """
    Evaluation AG code defined by rational places ``pls`` and a divisor ``G``.

    INPUT:

    - ``pls`` -- list of rational places of a function field

    - ``G`` -- a divisor whose support is disjoint from ``pls``

    If ``G`` is a place, then it is regarded as a prime divisor.

    EXAMPLES::

        sage: k.<a> = GF(4)
        sage: A.<x,y> = AffineSpace(k, 2)
        sage: C = Curve(y^2 + y - x^3)
        sage: F = C.function_field()
        sage: pls = F.places()
        sage: Q, = C.places_at_infinity()
        sage: pls.remove(Q)
        sage: G = 5*Q
        sage: codes.EvaluationAGCode(pls, G)
        [8, 5] evaluation AG code over GF(4)

        sage: G = F.get_place(5)
        sage: codes.EvaluationAGCode(pls, G)
        [8, 5] evaluation AG code over GF(4)
    """
    def __init__(self, pls, G) -> None:
        """
        Initialize.

        TESTS::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls = [pl for pl in pls if pl != Q]
            sage: G = 5*Q
            sage: code = codes.EvaluationAGCode(pls, G)
            sage: TestSuite(code).run()
        """
    def __eq__(self, other):
        """
        Test equality of ``self`` with ``other``.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: codes.EvaluationAGCode(pls, 5*Q) == codes.EvaluationAGCode(pls, 6*Q)
            False
        """
    def __hash__(self):
        """
        Return the hash value of ``self``.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.EvaluationAGCode(pls, 5*Q)
            sage: {code: 1}
            {[8, 5] evaluation AG code over GF(4): 1}
        """
    def basis_functions(self):
        """
        Return the basis functions associated with the generator matrix.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.EvaluationAGCode(pls, 3*Q)
            sage: code.basis_functions()
            (y + a*x + 1, y + x, (a + 1)*x)
            sage: matrix([[f.evaluate(p) for p in pls] for f in code.basis_functions()])
            [    1     0     0     1     a a + 1     1     0]
            [    0     1     0     1     1     0 a + 1     a]
            [    0     0     1     1     a     a a + 1 a + 1]
        """
    def generator_matrix(self):
        """
        Return a generator matrix of the code.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.EvaluationAGCode(pls, 3*Q)
            sage: code.generator_matrix()
            [    1     0     0     1     a a + 1     1     0]
            [    0     1     0     1     1     0 a + 1     a]
            [    0     0     1     1     a     a a + 1 a + 1]
        """
    def designed_distance(self):
        """
        Return the designed distance of the AG code.

        If the code is of dimension zero, then a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.EvaluationAGCode(pls, 3*Q)
            sage: code.designed_distance()
            5
        """

class DifferentialAGCode(AGCode):
    """
    Differential AG code defined by rational places ``pls`` and a divisor ``G``.

    INPUT:

    - ``pls`` -- list of rational places of a function field

    - ``G`` -- a divisor whose support is disjoint from ``pls``

    If ``G`` is a place, then it is regarded as a prime divisor.

    EXAMPLES::

        sage: k.<a> = GF(4)
        sage: A.<x,y> = AffineSpace(k, 2)
        sage: C = A.curve(y^3 + y - x^4)
        sage: Q = C.places_at_infinity()[0]
        sage: O = C([0,0]).place()
        sage: pls = [p for p in C.places() if p not in [O, Q]]
        sage: G = -O + 3*Q
        sage: codes.DifferentialAGCode(pls, -O + Q)
        [3, 2] differential AG code over GF(4)

        sage: F = C.function_field()
        sage: G = F.get_place(1)
        sage: codes.DifferentialAGCode(pls, G)
        [3, 1] differential AG code over GF(4)
    """
    def __init__(self, pls, G) -> None:
        """
        Initialize.

        TESTS::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.DifferentialAGCode(pls, 3*Q)
            sage: TestSuite(code).run()
        """
    def __eq__(self, other):
        """
        Test equality of ``self`` with ``other``.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: c1 = codes.DifferentialAGCode(pls, 3*Q)
            sage: c2 = codes.DifferentialAGCode(pls, 3*Q)
            sage: c1 is c2
            False
            sage: c1 == c2
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.DifferentialAGCode(pls, 3*Q)
            sage: {code: 1}
            {[8, 5] differential AG code over GF(4): 1}
        """
    def basis_differentials(self):
        """
        Return the basis differentials associated with the generator matrix.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.DifferentialAGCode(pls, 3*Q)
            sage: matrix([[w.residue(p) for p in pls]
            ....:         for w in code.basis_differentials()])
            [    1     0     0     0     0 a + 1 a + 1     1]
            [    0     1     0     0     0 a + 1     a     0]
            [    0     0     1     0     0     a     1     a]
            [    0     0     0     1     0     a     0 a + 1]
            [    0     0     0     0     1     1     1     1]
        """
    def generator_matrix(self):
        """
        Return a generator matrix of the code.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.DifferentialAGCode(pls, 3*Q)
            sage: code.generator_matrix()
            [    1     0     0     0     0 a + 1 a + 1     1]
            [    0     1     0     0     0 a + 1     a     0]
            [    0     0     1     0     0     a     1     a]
            [    0     0     0     1     0     a     0 a + 1]
            [    0     0     0     0     1     1     1     1]
        """
    def designed_distance(self):
        """
        Return the designed distance of the differential AG code.

        If the code is of dimension zero, then a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<a> = GF(4)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 + y - x^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Q, = C.places_at_infinity()
            sage: pls.remove(Q)
            sage: code = codes.DifferentialAGCode(pls, 3*Q)
            sage: code.designed_distance()
            3
        """

class CartierCode(AGCode):
    """
    Cartier code defined by rational places ``pls`` and a divisor ``G`` of a function field.

    INPUT:

    - ``pls`` -- list of rational places

    - ``G`` -- a divisor whose support is disjoint from ``pls``

    - ``r`` -- integer (default: 1)

    - ``name`` -- string; name of the generator of the subfield `\\GF{p^r}`

    OUTPUT: cartier code over `\\GF{p^r}` where `p` is the characteristic of the
    base constant field of the function field

    Note that if ``r`` is 1 the default, then ``name`` can be omitted.

    EXAMPLES::

        sage: F.<a> = GF(9)
        sage: P.<x,y,z> = ProjectiveSpace(F, 2);
        sage: C = Curve(x^3*y + y^3*z + x*z^3)
        sage: F = C.function_field()
        sage: pls = F.places()
        sage: Z, = C(0,0,1).places()
        sage: pls.remove(Z)
        sage: G = 3*Z
        sage: code = codes.CartierCode(pls, G)  # long time
        sage: code.minimum_distance()           # long time
        2
    """
    def __init__(self, pls, G, r: int = 1, name=None) -> None:
        """
        Initialize.

        TESTS::

            sage: F.<a> = GF(9)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2);
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Z, = C(0,0,1).places()
            sage: pls.remove(Z)
            sage: G = 3*Z
            sage: code = codes.CartierCode(pls, G)  # long time
            sage: TestSuite(code).run()             # long time
        """
    def __eq__(self, other):
        """
        Test equality of ``self`` with ``other``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2);
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Z, = C(0,0,1).places()
            sage: pls.remove(Z)
            sage: c1 = codes.CartierCode(pls, 3*Z)  # long time
            sage: c2 = codes.CartierCode(pls, 1*Z)  # long time
            sage: c1 == c2                          # long time
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2);
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Z, = C(0,0,1).places()
            sage: pls.remove(Z)
            sage: G = 3*Z
            sage: code = codes.CartierCode(pls, G)  # long time
            sage: {code: 1}                         # long time
            {[9, 4] Cartier code over GF(3): 1}
        """
    def generator_matrix(self):
        """
        Return a generator matrix of the Cartier code.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2);
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Z, = C(0,0,1).places()
            sage: pls.remove(Z)
            sage: G = 3*Z
            sage: code = codes.CartierCode(pls, G)  # long time
            sage: code.generator_matrix()           # long time
            [1 0 0 2 2 0 2 2 0]
            [0 1 0 2 2 0 2 2 0]
            [0 0 1 0 0 0 0 0 2]
            [0 0 0 0 0 1 0 0 2]
        """
    def designed_distance(self):
        """
        Return the designed distance of the Cartier code.

        The designed distance is that of the differential code of which the
        Cartier code is a subcode.

        EXAMPLES::

            sage: F.<a> = GF(9)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2);
            sage: C = Curve(x^3*y + y^3*z + x*z^3)
            sage: F = C.function_field()
            sage: pls = F.places()
            sage: Z, = C(0,0,1).places()
            sage: pls.remove(Z)
            sage: G = 3*Z
            sage: code = codes.CartierCode(pls, G)  # long time
            sage: code.designed_distance()          # long time
            1
        """
