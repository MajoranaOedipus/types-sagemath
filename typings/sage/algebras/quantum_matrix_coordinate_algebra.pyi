from sage.categories.algebras import Algebras as Algebras
from sage.categories.bialgebras import Bialgebras as Bialgebras
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.sets.family import Family as Family

class QuantumMatrixCoordinateAlgebra_abstract(CombinatorialFreeModule):
    """
    Abstract base class for quantum coordinate algebras of a set
    of matrices.
    """
    @staticmethod
    def __classcall__(cls, q=None, bar=None, R=None, **kwds):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: R.<q> = LaurentPolynomialRing(ZZ)
            sage: O1 = algebras.QuantumMatrixCoordinate(4)
            sage: O2 = algebras.QuantumMatrixCoordinate(4, 4, q=q)
            sage: O3 = algebras.QuantumMatrixCoordinate(4, R=ZZ)
            sage: O4 = algebras.QuantumMatrixCoordinate(4, R=R, q=q)
            sage: O1 is O2 and O2 is O3 and O3 is O4
            True
            sage: O5 = algebras.QuantumMatrixCoordinate(4, R=QQ)
            sage: O1 is O5
            False
        """
    def __init__(self, gp_indices, n, q, bar, R, category, indices_key=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: O = algebras.QuantumMatrixCoordinate(3, 2)
            sage: TestSuite(O).run()
        """
    def n(self):
        """
        Return the value `n`.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: O.n()
            4
            sage: O = algebras.QuantumMatrixCoordinate(4, 6)
            sage: O.n()
            6
        """
    def q(self):
        """
        Return the variable ``q``.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: O.q()
            q
            sage: O.q().parent()
            Univariate Laurent Polynomial Ring in q over Integer Ring
            sage: O.q().parent() is O.base_ring()
            True
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis element indexing `1`.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: O.one_basis()
            1
            sage: O.one()
            1

        TESTS::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: O.one_basis() == O.indices().one()
            True
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self`` as a tuple.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(3)
            sage: O.gens()
            (x[1,1], x[1,2], x[1,3],
             x[2,1], x[2,2], x[2,3],
             x[3,1], x[3,2], x[3,3])
        """
    @cached_method
    def quantum_determinant(self):
        """
        Return the quantum determinant of ``self``.

        The quantum determinant is defined by

        .. MATH::

            \\det_q = \\sum_{\\sigma \\in S_n} (-q)^{\\ell(\\sigma)}
            x_{1, \\sigma(1)} x_{2, \\sigma(2)} \\cdots x_{n, \\sigma(n)}.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(2)
            sage: O.quantum_determinant()
            x[1,1]*x[2,2] - q*x[1,2]*x[2,1]

        We verify that the quantum determinant is central::

            sage: for n in range(2,5):
            ....:     O = algebras.QuantumMatrixCoordinate(n)
            ....:     qdet = O.quantum_determinant()
            ....:     assert all(g * qdet == qdet * g for g in O.algebra_generators())

        We also verify that it is group-like::

            sage: for n in range(2,4):
            ....:     O = algebras.QuantumMatrixCoordinate(n)
            ....:     qdet = O.quantum_determinant()
            ....:     assert qdet.coproduct() == tensor([qdet, qdet])
        """
    def product_on_basis(self, a, b):
        """
        Return the product of basis elements indexed by ``a`` and ``b``.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: x = O.algebra_generators()
            sage: b = x[1,4] * x[2,1] * x[3,4]  # indirect doctest
            sage: b * (b * b) == (b * b) * b
            True
            sage: p = prod(list(O.algebra_generators())[:10])
            sage: p * (p * p) == (p * p) * p  # long time
            True
            sage: x = O.an_element()
            sage: y = x^2 + x[4,4] * x[3,3] * x[1,2]
            sage: z = x[2,2] * x[1,4] * x[3,4] * x[1,1]
            sage: x * (y * z) == (x * y) * z
            True
        """
    def counit_on_basis(self, x):
        """
        Return the counit on the basis element indexed by ``x``.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: G = O.algebra_generators()
            sage: I = [1,2,3,4]
            sage: matrix([[G[i,j].counit() for i in I] for j in I])  # indirect doctest
            [1 0 0 0]
            [0 1 0 0]
            [0 0 1 0]
            [0 0 0 1]
        """
    class Element(CombinatorialFreeModule.Element):
        """
        An element of a quantum matrix coordinate algebra.
        """
        def bar(self):
            """
            Return the image of ``self`` under the bar involution.

            The bar involution is the `\\QQ`-algebra anti-automorphism
            defined by `x_{ij} \\mapsto x_{ji}` and `q \\mapsto q^{-1}`.

            EXAMPLES::

                sage: O = algebras.QuantumMatrixCoordinate(4)
                sage: x = O.an_element()
                sage: x.bar()
                1 + 2*x[1,1] + (q^-16)*x[1,1]^2*x[1,2]^2*x[1,3]^3 + 3*x[1,2]
                sage: x = O.an_element() * O.algebra_generators()[2,4]; x
                x[1,1]^2*x[1,2]^2*x[1,3]^3*x[2,4] + 2*x[1,1]*x[2,4]
                 + 3*x[1,2]*x[2,4] + x[2,4]
                sage: xb = x.bar(); xb
                (q^-16)*x[1,1]^2*x[1,2]^2*x[1,3]^3*x[2,4]
                 + (q^-21-q^-15)*x[1,1]^2*x[1,2]^2*x[1,3]^2*x[1,4]*x[2,3]
                 + (q^-22-q^-18)*x[1,1]^2*x[1,2]*x[1,3]^3*x[1,4]*x[2,2]
                 + (q^-24-q^-20)*x[1,1]*x[1,2]^2*x[1,3]^3*x[1,4]*x[2,1]
                 + 2*x[1,1]*x[2,4] + 3*x[1,2]*x[2,4]
                 + (2*q^-1-2*q)*x[1,4]*x[2,1]
                 + (3*q^-1-3*q)*x[1,4]*x[2,2] + x[2,4]
                sage: xb.bar() == x
                True
            """

class QuantumMatrixCoordinateAlgebra(QuantumMatrixCoordinateAlgebra_abstract):
    """
    A quantum matrix coordinate algebra.

    Let `R` be a commutative ring. The quantum matrix coordinate algebra
    of `M(m, n)` is the associative algebra over `R[q, q^{-1}]`
    generated by `x_{ij}`, for `i = 1, 2, \\ldots, m`, `j = 1, 2, \\ldots, n`,
    and subject to the following relations:

    .. MATH::

        \\begin{array}{ll}
        x_{it} x_{ij} = q^{-1} x_{ij} x_{it}   & \\text{if } j < t, \\\\\n        x_{sj} x_{ij} = q^{-1} x_{ij} x_{sj}   & \\text{if } i < s, \\\\\n        x_{st} x_{ij} = x_{ij} x_{st}          & \\text{if } i < s, j > t, \\\\\n        x_{st} x_{ij} = x_{ij} x_{st} + (q^{-1} - q) x_{it} x_{sj}
                                               & \\text{if } i < s, j < t. \\\\\n        \\end{array}

    The quantum matrix coordinate algebra is denoted by
    `\\mathcal{O}_q(M(m, n))`. For `m = n`, it is also a bialgebra given by

    .. MATH::

        \\Delta(x_{ij}) = \\sum_{k=1}^n x_{ik} \\otimes x_{kj},
        \\varepsilon(x_{ij}) = \\delta_{ij}.

    Moreover, there is a central group-like element called the
    *quantum determinant* that is defined by

    .. MATH::

        \\det_q = \\sum_{\\sigma \\in S_n} (-q)^{\\ell(\\sigma)}
        x_{1,\\sigma(1)} x_{2,\\sigma(2)} \\cdots x_{n,\\sigma(n)}.

    The quantum matrix coordinate algebra also has natural inclusions
    when restricting to submatrices. That is, let
    `I \\subseteq \\{1, 2, \\ldots, m\\}` and `J \\subseteq \\{1, 2, \\ldots, n\\}`.
    Then the subalgebra generated by `\\{ x_{ij} \\mid i \\in I, j \\in J \\}`
    is naturally isomorphic to `\\mathcal{O}_q(M(|I|, |J|))`.

    .. NOTE::

        The `q` considered here is `q^2` in some references, e.g., [ZZ2005]_.

    INPUT:

    - ``m`` -- the integer `m`
    - ``n`` -- the integer `n`
    - ``R`` -- (optional) the ring `R` if `q` is not specified
      (the default is `\\ZZ`); otherwise the ring containing `q`
    - ``q`` -- (optional) the variable `q`; the default is
      `q \\in R[q, q^{-1}]`
    - ``bar`` -- (optional) the involution on the base ring; the
      default is `q \\mapsto q^{-1}`

    EXAMPLES:

    We construct `\\mathcal{O}_q(M(2,3))` and the variables::

        sage: O = algebras.QuantumMatrixCoordinate(2,3)
        sage: O.inject_variables()
        Defining x11, x12, x13, x21, x22, x23

    We do some basic computations::

        sage: x21 * x11
        (q^-1)*x[1,1]*x[2,1]
        sage: x23 * x12 * x11
        (q^-1)*x[1,1]*x[1,2]*x[2,3] + (q^-2-1)*x[1,1]*x[1,3]*x[2,2]
         + (q^-3-q^-1)*x[1,2]*x[1,3]*x[2,1]

    We construct the maximal quantum minors::

        sage: q = O.q()
        sage: qm12 = x11*x22 - q*x12*x21
        sage: qm13 = x11*x23 - q*x13*x21
        sage: qm23 = x12*x23 - q*x13*x22

    However, unlike for the quantum determinant, they are not central::

        sage: all(qm12 * g == g * qm12 for g in O.algebra_generators())
        False
        sage: all(qm13 * g == g * qm13 for g in O.algebra_generators())
        False
        sage: all(qm23 * g == g * qm23 for g in O.algebra_generators())
        False

    REFERENCES:

    - [FRT1990]_
    - [ZZ2005]_
    """
    @staticmethod
    def __classcall_private__(cls, m, n=None, q=None, bar=None, R=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: R.<q> = LaurentPolynomialRing(ZZ)
            sage: O1 = algebras.QuantumMatrixCoordinate(4)
            sage: O2 = algebras.QuantumMatrixCoordinate(4, 4, q=q)
            sage: O3 = algebras.QuantumMatrixCoordinate(4, R=ZZ)
            sage: O4 = algebras.QuantumMatrixCoordinate(4, R=R, q=q)
            sage: O1 is O2 and O2 is O3 and O3 is O4
            True
            sage: O5 = algebras.QuantumMatrixCoordinate(4, R=QQ)
            sage: O1 is O5
            False
        """
    def __init__(self, m, n, q, bar, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: TestSuite(O).run()

            sage: O = algebras.QuantumMatrixCoordinate(10)
            sage: O.variable_names()
            ('x0101', ..., 'x1010')
            sage: O = algebras.QuantumMatrixCoordinate(11,3)
            sage: O.variable_names()
            ('x011', ..., 'x113')
            sage: O = algebras.QuantumMatrixCoordinate(3,11)
            sage: O.variable_names()
            ('x101', ..., 'x311')
        """
    def m(self):
        """
        Return the value `m`.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4, 6)
            sage: O.m()
            4
            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: O.m()
            4
        """
    @cached_method
    def algebra_generators(self) -> Family:
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(2)
            sage: O.algebra_generators()
            Finite family {(1, 1): x[1,1], (1, 2): x[1,2], (2, 1): x[2,1], (2, 2): x[2,2]}
        """
    def coproduct_on_basis(self, x):
        """
        Return the coproduct on the basis element indexed by ``x``.

        EXAMPLES::

            sage: O = algebras.QuantumMatrixCoordinate(4)
            sage: x24 = O.algebra_generators()[2,4]
            sage: O.coproduct_on_basis(x24.leading_support())
            x[2,1] # x[1,4] + x[2,2] # x[2,4] + x[2,3] # x[3,4] + x[2,4] # x[4,4]

        TESTS:

        We check that it is an algebra morphism::

            sage: O = algebras.QuantumMatrixCoordinate(3)
            sage: G = O.algebra_generators()
            sage: all(x.coproduct() * y.coproduct() == (x * y).coproduct()
            ....:     for x in G for y in G)
            True
        """

class QuantumGL(QuantumMatrixCoordinateAlgebra_abstract):
    """
    Quantum coordinate algebra of `GL(n)`.

    The quantum coordinate algebra of `GL(n)`, or quantum `GL(n)`
    for short and denoted by `\\mathcal{O}_q(GL(n))`, is the quantum
    coordinate algebra of `M_R(n, n)` with the addition of the
    additional central group-like element `c` which satisfies
    `c d = d c = 1`, where `d` is the quantum determinant.

    Quantum `GL(n)` is a Hopf algebra where `\\varepsilon(c) = 1`
    and the antipode `S` is given by the (quantum) matrix inverse.
    That is to say, we have `S(c) = c^-1 = d` and

    .. MATH::

        S(x_{ij}) = c * (-q)^{i-j} * \\tilde{t}_{ji},

    where we have the quantum minor

    .. MATH::

        \\tilde{t}_{ij} = \\sum_{\\sigma} (-q)^{\\ell(\\sigma)}
        x_{1, \\sigma(1)} \\cdots x_{i-1, \\sigma(i-1)} x_{i+1, \\sigma(i+1)}
        \\cdots x_{n, \\sigma(n)}

    with the sum over permutations `\\sigma \\colon \\{1, \\ldots, i-1, i+1,
    \\ldots n\\} \\to \\{1, \\ldots, j-1, j+1, \\ldots, n\\}`.

    .. SEEALSO::

        :class:`QuantumMatrixCoordinateAlgebra`

    INPUT:

    - ``n`` -- the integer `n`
    - ``R`` -- (optional) the ring `R` if `q` is not specified
      (the default is `\\ZZ`); otherwise the ring containing `q`
    - ``q`` -- (optional) the variable `q`; the default is
      `q \\in R[q, q^{-1}]`
    - ``bar`` -- (optional) the involution on the base ring; the
      default is `q \\mapsto q^{-1}`

    EXAMPLES:

    We construct `\\mathcal{O}_q(GL(3))` and the variables::

        sage: O = algebras.QuantumGL(3)
        sage: O.inject_variables()
        Defining x11, x12, x13, x21, x22, x23, x31, x32, x33, c

    We do some basic computations::

        sage: x33 * x12
        x[1,2]*x[3,3] + (q^-1-q)*x[1,3]*x[3,2]
        sage: x23 * x12 * x11
        (q^-1)*x[1,1]*x[1,2]*x[2,3] + (q^-2-1)*x[1,1]*x[1,3]*x[2,2]
         + (q^-3-q^-1)*x[1,2]*x[1,3]*x[2,1]
        sage: c * O.quantum_determinant()
        1

    We verify the quantum determinant is in the center and is group-like::

        sage: qdet = O.quantum_determinant()
        sage: all(qdet * g == g * qdet for g in O.algebra_generators())
        True
        sage: qdet.coproduct() == tensor([qdet, qdet])
        True

    We check that the inverse of the quantum determinant is also in
    the center and group-like::

        sage: all(c * g == g * c for g in O.algebra_generators())
        True
        sage: c.coproduct() == tensor([c, c])
        True

    Moreover, the antipode interchanges the quantum determinant and
    its inverse::

        sage: c.antipode() == qdet
        True
        sage: qdet.antipode() == c
        True

    REFERENCES:

    - [DD1991]_
    - [Kar1993]_
    """
    @staticmethod
    def __classcall_private__(cls, n, q=None, bar=None, R=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: R.<q> = LaurentPolynomialRing(ZZ)
            sage: O1 = algebras.QuantumGL(4)
            sage: O2 = algebras.QuantumGL(4, R=ZZ)
            sage: O3 = algebras.QuantumGL(4, R=R, q=q)
            sage: O1 is O2 and O2 is O3
            True
            sage: O4 = algebras.QuantumGL(4, R=QQ)
            sage: O1 is O4
            False
        """
    def __init__(self, n, q, bar, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: O = algebras.QuantumGL(2)
            sage: elts = list(O.algebra_generators())
            sage: elts += [O.quantum_determinant(), O.an_element()]
            sage: TestSuite(O).run(elements=elts) # long time
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumGL(2)
            sage: O.algebra_generators()
            Finite family {(1, 1): x[1,1], (1, 2): x[1,2], (2, 1): x[2,1], (2, 2): x[2,2], 'c': c}
        """
    def product_on_basis(self, a, b):
        """
        Return the product of basis elements indexed by ``a`` and ``b``.

        EXAMPLES::

            sage: O = algebras.QuantumGL(2)
            sage: I = O.indices().monoid_generators()
            sage: O.product_on_basis(I[1,1], I[2,2])
            x[1,1]*x[2,2]
            sage: O.product_on_basis(I[2,2], I[1,1])
            x[1,1]*x[2,2] + (q^-1-q)*x[1,2]*x[2,1]

        TESTS::

            sage: x11,x12,x21,x22,c = O.algebra_generators()
            sage: x11 * x22
            x[1,1]*x[2,2]
            sage: x22 * x12
            (q^-1)*x[1,2]*x[2,2]
            sage: x22 * x11
            x[1,1]*x[2,2] + (q^-1-q)*x[1,2]*x[2,1]
            sage: c * (x11 * O.quantum_determinant())
            x[1,1]
        """
    def antipode_on_basis(self, x):
        """
        Return the antipode of the basis element indexed by ``x``.

        EXAMPLES::

            sage: O = algebras.QuantumGL(3)
            sage: x = O.indices().monoid_generators()
            sage: O.antipode_on_basis(x[1,2])
            -(q^-1)*c*x[1,2]*x[3,3] + c*x[1,3]*x[3,2]
            sage: O.antipode_on_basis(x[2,2])
            c*x[1,1]*x[3,3] - q*c*x[1,3]*x[3,1]
            sage: O.antipode_on_basis(x['c']) == O.quantum_determinant()
            True
        """
    def coproduct_on_basis(self, x):
        """
        Return the coproduct on the basis element indexed by ``x``.

        EXAMPLES::

            sage: O = algebras.QuantumGL(3)
            sage: x = O.indices().monoid_generators()
            sage: O.coproduct_on_basis(x[1,2])
            x[1,1] # x[1,2] + x[1,2] # x[2,2] + x[1,3] # x[3,2]
            sage: O.coproduct_on_basis(x[2,2])
            x[2,1] # x[1,2] + x[2,2] # x[2,2] + x[2,3] # x[3,2]
            sage: O.coproduct_on_basis(x['c'])
            c # c
        """
