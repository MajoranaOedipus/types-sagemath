from _typeshed import Incomplete
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.richcmp import op_EQ as op_EQ, op_GE as op_GE, op_GT as op_GT, op_LE as op_LE, op_LT as op_LT, op_NE as op_NE

class DiscretePseudoValuation(Morphism):
    """
    Abstract base class for discrete pseudo-valuations, i.e., discrete
    valuations which might send more that just zero to infinity.

    INPUT:

    - ``domain`` -- an integral domain

    EXAMPLES::

        sage: v = ZZ.valuation(2); v  # indirect doctest
        2-adic valuation

    TESTS::

        sage: TestSuite(v).run()                # long time                             # needs sage.geometry.polyhedron
    """
    def __init__(self, parent) -> None:
        """
        TESTS::

            sage: from sage.rings.valuation.valuation import DiscretePseudoValuation
            sage: isinstance(ZZ.valuation(2), DiscretePseudoValuation)
            True
        """
    def is_equivalent(self, f, g):
        """
        Return whether ``f`` and ``g`` are equivalent.

        EXAMPLES::

            sage: v = QQ.valuation(2)
            sage: v.is_equivalent(2, 1)
            False
            sage: v.is_equivalent(2, -2)
            True
            sage: v.is_equivalent(2, 0)
            False
            sage: v.is_equivalent(0, 0)
            True
        """
    def __hash__(self):
        """
        The hash value of this valuation.

        We redirect to :meth:`_hash_`, so that subclasses can only override
        :meth:`_hash_` and :meth:`_eq_` if they want to provide a different
        notion of equality but they can leave the partial and total operators
        untouched.

        EXAMPLES::

            sage: v = QQ.valuation(2)
            sage: hash(v) == hash(v)  # indirect doctest
            True
        """
    __reduce__: Incomplete

class InfiniteDiscretePseudoValuation(DiscretePseudoValuation):
    """
    Abstract base class for infinite discrete pseudo-valuations, i.e., discrete
    pseudo-valuations which are not discrete valuations.

    EXAMPLES::

        sage: v = QQ.valuation(2)
        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, v)
        sage: w = v.augmentation(x, infinity); w  # indirect doctest
        [ Gauss valuation induced by 2-adic valuation, v(x) = +Infinity ]

    TESTS::

        sage: from sage.rings.valuation.valuation import InfiniteDiscretePseudoValuation
        sage: isinstance(w, InfiniteDiscretePseudoValuation)
        True
        sage: TestSuite(w).run()                # long time                             # needs sage.geometry.polyhedron sage.rings.padics
    """
    def is_discrete_valuation(self):
        """
        Return whether this valuation is a discrete valuation.

        EXAMPLES::

            sage: v = QQ.valuation(2)
            sage: R.<x> = QQ[]
            sage: v = GaussValuation(R, v)
            sage: v.is_discrete_valuation()
            True
            sage: w = v.augmentation(x, infinity)
            sage: w.is_discrete_valuation()
            False
        """

class NegativeInfiniteDiscretePseudoValuation(InfiniteDiscretePseudoValuation):
    """
    Abstract base class for pseudo-valuations which attain the value `\\infty`
    and `-\\infty`, i.e., whose domain contains an element of valuation `\\infty`
    and its inverse.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, valuations.TrivialValuation(QQ)).augmentation(x, infinity)
        sage: K.<x> = FunctionField(QQ)
        sage: w = K.valuation(v)

    TESTS::

        sage: TestSuite(w).run()                # long time
    """
    def is_negative_pseudo_valuation(self):
        """
        Return whether this valuation attains the value `-\\infty`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: u = GaussValuation(R, valuations.TrivialValuation(QQ))
            sage: v = u.augmentation(x, infinity)
            sage: v.is_negative_pseudo_valuation()
            False
            sage: K.<x> = FunctionField(QQ)
            sage: w = K.valuation(v)
            sage: w.is_negative_pseudo_valuation()
            True
        """

class DiscreteValuation(DiscretePseudoValuation):
    """
    Abstract base class for discrete valuations.

    EXAMPLES::

        sage: v = QQ.valuation(2)
        sage: R.<x> = QQ[]
        sage: v = GaussValuation(R, v)
        sage: w = v.augmentation(x, 1337); w  # indirect doctest
        [ Gauss valuation induced by 2-adic valuation, v(x) = 1337 ]

    TESTS::

        sage: from sage.rings.valuation.valuation import DiscreteValuation
        sage: isinstance(w, DiscreteValuation)
        True
        sage: TestSuite(w).run()                # long time                             # needs sage.geometry.polyhedron sage.rings.padics
    """
    def is_discrete_valuation(self):
        """
        Return whether this valuation is a discrete valuation.

        EXAMPLES::

            sage: v = valuations.TrivialValuation(ZZ)
            sage: v.is_discrete_valuation()
            True
        """
    def mac_lane_approximants(self, G, assume_squarefree: bool = False, require_final_EF: bool = True, required_precision: int = -1, require_incomparability: bool = False, require_maximal_degree: bool = False, algorithm: str = 'serial'):
        """
        Return approximants on `K[x]` for the extensions of this valuation to
        `L=K[x]/(G)`.

        If `G` is an irreducible polynomial, then this corresponds to
        extensions of this valuation to the completion of `L`.

        INPUT:

        - ``G`` -- a monic squarefree integral polynomial in a
          univariate polynomial ring over the domain of this valuation

        - ``assume_squarefree`` -- boolean (default: ``False``); whether to
          assume that ``G`` is squarefree. If ``True``, the squafreeness of
          ``G`` is not verified though it is necessary when
          ``require_final_EF`` is set for the algorithm to terminate.

        - ``require_final_EF`` -- boolean (default: ``True``); whether to
          require the returned key polynomials to be in one-to-one
          correspondence to the extensions of this valuation to ``L`` and
          require them to have the ramification index and residue degree of the
          valuations they correspond to.

        - ``required_precision`` -- a number or infinity (default: -1); whether
          to require the last key polynomial of the returned valuations to have
          at least that valuation.

        - ``require_incomparability`` -- boolean (default: ``False``);
          whether to require the returned valuations to be incomparable
          (with respect to the partial order on valuations defined by comparing
          them pointwise.)

        - ``require_maximal_degree`` -- boolean (default: ``False``); whether
          to require the last key polynomial of the returned valuation to have
          maximal degree. This is most relevant when using this algorithm to
          compute approximate factorizations of ``G``, when set to ``True``,
          the last key polynomial has the same degree as the corresponding
          factor.

        - ``algorithm`` -- one of ``'serial'`` or ``'parallel'`` (default:
          ``'serial'``); whether or not to parallelize the algorithm

        EXAMPLES::

            sage: v = QQ.valuation(2)
            sage: R.<x> = QQ[]
            sage: v.mac_lane_approximants(x^2 + 1)                                      # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 ]]
            sage: v.mac_lane_approximants(x^2 + 1, required_precision=infinity)         # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2,
               v(x^2 + 1) = +Infinity ]]
            sage: v.mac_lane_approximants(x^2 + x + 1)
            [[ Gauss valuation induced by 2-adic valuation, v(x^2 + x + 1) = +Infinity ]]

        Note that ``G`` does not need to be irreducible. Here, we detect a
        factor `x + 1` and an approximate factor `x + 1` (which is an
        approximation to `x - 1`)::

            sage: v.mac_lane_approximants(x^2 - 1)                                      # needs sage.geometry.polyhedron sage.rings.padics
            [[ Gauss valuation induced by 2-adic valuation, v(x + 1) = +Infinity ],
             [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1 ]]

        However, it needs to be squarefree::

            sage: v.mac_lane_approximants(x^2)
            Traceback (most recent call last):
            ...
            ValueError: G must be squarefree

        TESTS:

        Some difficult cases provided by Mark van Hoeij::

            sage: # needs sage.rings.finite_rings sage.rings.function_field
            sage: k = GF(2)
            sage: K.<x> = FunctionField(k)
            sage: R.<y> = K[]
            sage: F = y^21 + x*y^20 + (x^3 + x + 1)*y^18 + (x^3 + 1)*y^17 + (x^4 + x)*y^16 + (x^7 + x^6 + x^3 + x + 1)*y^15 + x^7*y^14 + (x^8 + x^7 + x^6 + x^4 + x^3 + 1)*y^13 + (x^9 + x^8 + x^4 + 1)*y^12 + (x^11 + x^9 + x^8 + x^5 + x^4 + x^3 + x^2)*y^11 + (x^12 + x^9 + x^8 + x^7 + x^5 + x^3 + x + 1)*y^10 + (x^14 + x^13 + x^10 + x^9 + x^8 + x^7 + x^6 + x^3 + x^2 + 1)*y^9 + (x^13 + x^9 + x^8 + x^6 + x^4 + x^3 + x)*y^8 + (x^16 + x^15 + x^13 + x^12 + x^11 + x^7 + x^3 + x)*y^7 + (x^17 + x^16 + x^13 + x^9 + x^8 + x)*y^6 + (x^17 + x^16 + x^12 + x^7 + x^5 + x^2 + x + 1)*y^5 + (x^19 + x^16 + x^15 + x^12 + x^6 + x^5 + x^3 + 1)*y^4 + (x^18 + x^15 + x^12 + x^10 + x^9 + x^7 + x^4 + x)*y^3 + (x^22 + x^21 + x^20 + x^18 + x^13 + x^12 + x^9 + x^8 + x^7 + x^5 + x^4 + x^3)*y^2 + (x^23 + x^22 + x^20 + x^17 + x^15 + x^14 + x^12 + x^9)*y + x^25 + x^23 + x^19 + x^17 + x^15 + x^13 + x^11 + x^5
            sage: x = K._ring.gen()
            sage: v0 = K.valuation(GaussValuation(K._ring, valuations.TrivialValuation(k)).augmentation(x,1))
            sage: v0.mac_lane_approximants(F, assume_squarefree=True)  # assumes squarefree for speed                   # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by (x)-adic valuation, v(y + x + 1) = 3/2 ],
             [ Gauss valuation induced by (x)-adic valuation, v(y) = 1 ],
             [ Gauss valuation induced by (x)-adic valuation, v(y) = 4/3 ],
             [ Gauss valuation induced by (x)-adic valuation, v(y^15 + y^13 + y^12 + y^10 + y^9 + y^8 + y^4 + y^3 + y^2 + y + 1) = 1 ]]
            sage: v0 = K.valuation(GaussValuation(K._ring, valuations.TrivialValuation(k)).augmentation(x+1,1))
            sage: v0.mac_lane_approximants(F, assume_squarefree=True)  # assumes squarefree for speed                   # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by (x + 1)-adic valuation, v(y + x^2 + 1) = 7/2 ],
             [ Gauss valuation induced by (x + 1)-adic valuation, v(y) = 3/4 ],
             [ Gauss valuation induced by (x + 1)-adic valuation, v(y) = 7/2 ],
             [ Gauss valuation induced by (x + 1)-adic valuation, v(y^13 + y^12 + y^10 + y^7 + y^6 + y^3 + 1) = 1 ]]
            sage: v0 = valuations.FunctionFieldValuation(K, GaussValuation(K._ring, valuations.TrivialValuation(k)).augmentation(x^3+x^2+1,1))
            sage: v0.mac_lane_approximants(F, assume_squarefree=True)  # assumes squarefree for speed
            [[ Gauss valuation induced by (x^3 + x^2 + 1)-adic valuation, v(y + x^3 + x^2 + x) = 2, v(y^2 + (x^6 + x^4 + 1)*y + x^14 + x^10 + x^9 + x^8 + x^5 + x^4 + x^3 + x^2 + x) = 5 ],
             [ Gauss valuation induced by (x^3 + x^2 + 1)-adic valuation, v(y^2 + (x^2 + x)*y + 1) = 1 ],
             [ Gauss valuation induced by (x^3 + x^2 + 1)-adic valuation, v(y^3 + (x + 1)*y^2 + (x + 1)*y + x^2 + x + 1) = 1 ],
             [ Gauss valuation induced by (x^3 + x^2 + 1)-adic valuation, v(y^3 + x^2*y + x) = 1 ],
             [ Gauss valuation induced by (x^3 + x^2 + 1)-adic valuation, v(y^4 + (x + 1)*y^3 + x^2*y^2 + (x^2 + x)*y + x) = 1 ],
             [ Gauss valuation induced by (x^3 + x^2 + 1)-adic valuation, v(y^7 + x^2*y^6 + (x + 1)*y^4 + x^2*y^3 + (x^2 + x + 1)*y^2 + x^2*y + x) = 1 ]]

        Cases with trivial residue field extensions::

            sage: K.<x> = FunctionField(QQ)
            sage: S.<y> = K[]
            sage: F = y^2 - x^2 - x^3 - 3
            sage: v0 = GaussValuation(K._ring, QQ.valuation(3))
            sage: v1 = v0.augmentation(K._ring.gen(),1/3)
            sage: mu0 = valuations.FunctionFieldValuation(K, v1)
            sage: mu0.mac_lane_approximants(F)                                          # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by Valuation on rational function field induced by [ Gauss valuation induced by 3-adic valuation, v(x) = 1/3 ], v(y + 2*x) = 2/3 ],
             [ Gauss valuation induced by Valuation on rational function field induced by [ Gauss valuation induced by 3-adic valuation, v(x) = 1/3 ], v(y + x) = 2/3 ]]

        Over a complete base field::

            sage: # needs sage.libs.ntl
            sage: k = Qp(2,10)
            sage: v = k.valuation()
            sage: R.<x> = k[]
            sage: G = x
            sage: v.mac_lane_approximants(G)
            [Gauss valuation induced by 2-adic valuation]
            sage: v.mac_lane_approximants(G, required_precision=infinity)
            [[ Gauss valuation induced by 2-adic valuation, v((1 + O(2^10))*x) = +Infinity ]]
            sage: G = x^2 + 1
            sage: v.mac_lane_approximants(G)                                            # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v((1 + O(2^10))*x + 1 + O(2^10)) = 1/2 ]]
            sage: v.mac_lane_approximants(G, required_precision=infinity)               # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v((1 + O(2^10))*x + 1 + O(2^10)) = 1/2,
               v((1 + O(2^10))*x^2 + 1 + O(2^10)) = +Infinity ]]
            sage: G = x^4 + 2*x^3 + 2*x^2 - 2*x + 2
            sage: v.mac_lane_approximants(G)                                            # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v((1 + O(2^10))*x) = 1/4 ]]
            sage: v.mac_lane_approximants(G, required_precision=infinity)               # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 2-adic valuation, v((1 + O(2^10))*x) = 1/4,
               v((1 + O(2^10))*x^4 + (2 + O(2^11))*x^3 + (2 + O(2^11))*x^2 + (2 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6 + 2^7 + 2^8 + 2^9 + 2^10 + O(2^11))*x + 2 + O(2^11)) = +Infinity ]]

        The factorization of primes in the Gaussian integers can be read off
        the Mac Lane approximants::

            sage: v0 = QQ.valuation(2)
            sage: R.<x> = QQ[]
            sage: G = x^2 + 1
            sage: v0.mac_lane_approximants(G)                                           # needs sage.geometry.polyhedron sage.rings.padics
            [[ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 ]]

            sage: v0 = QQ.valuation(3)
            sage: v0.mac_lane_approximants(G)
            [[ Gauss valuation induced by 3-adic valuation, v(x^2 + 1) = +Infinity ]]

            sage: v0 = QQ.valuation(5)
            sage: v0.mac_lane_approximants(G)                                           # needs sage.geometry.polyhedron sage.rings.padics
            [[ Gauss valuation induced by 5-adic valuation, v(x + 2) = 1 ],
             [ Gauss valuation induced by 5-adic valuation, v(x + 3) = 1 ]]
            sage: v0.mac_lane_approximants(G, required_precision=10)                    # needs sage.geometry.polyhedron sage.rings.padics
            [[ Gauss valuation induced by 5-adic valuation, v(x + 3116/237) = 10 ],
             [ Gauss valuation induced by 5-adic valuation, v(x - 3116/237) = 10 ]]

        The same example over the 5-adic numbers. In the quadratic extension
        `\\QQ[x]/(x^2+1)`, 5 factors `-(x - 2)(x + 2)`, this behaviour can be
        read off the Mac Lane approximants::

            sage: # needs sage.rings.padics
            sage: k = Qp(5,4)
            sage: v = k.valuation()
            sage: R.<x> = k[]                                                           # needs sage.libs.ntl
            sage: G = x^2 + 1
            sage: v1,v2 = v.mac_lane_approximants(G); v1,v2                             # needs sage.geometry.polyhedron
            ([ Gauss valuation induced by 5-adic valuation,
               v((1 + O(5^4))*x + 2 + O(5^4)) = 1 ],
             [ Gauss valuation induced by 5-adic valuation,
               v((1 + O(5^4))*x + 3 + O(5^4)) = 1 ])
            sage: w1, w2 = v.mac_lane_approximants(G, required_precision=2); w1, w2     # needs sage.geometry.polyhedron
            ([ Gauss valuation induced by 5-adic valuation,
               v((1 + O(5^4))*x + 2 + 5 + O(5^4)) = 2 ],
             [ Gauss valuation induced by 5-adic valuation,
               v((1 + O(5^4))*x + 3 + 3*5 + O(5^4)) = 2 ])

        Note how the latter give a better approximation to the factors of `x^2 + 1`::

            sage: # needs sage.geometry.polyhedron sage.rings.padics
            sage: v1.phi() * v2.phi() - G
            O(5^4)*x^2 + (5 + O(5^4))*x + 5 + O(5^4)
            sage: w1.phi() * w2.phi() - G
            O(5^4)*x^2 + (5^2 + O(5^4))*x + 5^3 + O(5^4)

        In this example, the process stops with a factorization of `x^2 + 1`::

            sage: # needs sage.geometry.polyhedron sage.rings.padics
            sage: v.mac_lane_approximants(G, required_precision=infinity)
            [[ Gauss valuation induced by 5-adic valuation,
               v((1 + O(5^4))*x + 2 + 5 + 2*5^2 + 5^3 + O(5^4)) = +Infinity ],
             [ Gauss valuation induced by 5-adic valuation,
               v((1 + O(5^4))*x + 3 + 3*5 + 2*5^2 + 3*5^3 + O(5^4)) = +Infinity ]]

        This obviously cannot happen over the rationals where we only get an
        approximate factorization::

            sage: v = QQ.valuation(5)
            sage: R.<x> = QQ[]
            sage: G = x^2 + 1
            sage: v.mac_lane_approximants(G)                                            # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 5-adic valuation, v(x + 2) = 1 ],
             [ Gauss valuation induced by 5-adic valuation, v(x + 3) = 1 ]]
            sage: v.mac_lane_approximants(G, required_precision=5)                      # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 5-adic valuation, v(x + 79/3) = 5 ],
             [ Gauss valuation induced by 5-adic valuation, v(x - 79/3) = 5 ]]

        Initial versions ran into problems with the trivial residue field
        extensions in this case::

            sage: # needs sage.libs.ntl
            sage: K = Qp(3, 20, print_mode='digits')
            sage: R.<T> = K[]
            sage: alpha = T^3/4
            sage: G = 3^3*T^3*(alpha^4 - alpha)^2 - (4*alpha^3 - 1)^3
            sage: G = G/G.leading_coefficient()
            sage: K.valuation().mac_lane_approximants(G)                                # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 3-adic valuation, v(...1*T + ...2) = 1/9,
               v(...1*T^9 + ...20*T^8 + ...210*T^7 + ...20*T^6 + ...20*T^5 + ...10*T^4
                  + ...220*T^3 + ...20*T^2 + ...110*T + ...122) = 55/27 ]]

        A similar example::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(3)
            sage: G = (x^3 + 3)^3 - 81
            sage: v.mac_lane_approximants(G)                                            # needs sage.geometry.polyhedron sage.rings.padics
            [[ Gauss valuation induced by 3-adic valuation,
               v(x) = 1/3, v(x^3 + 3*x + 3) = 13/9 ]]

        Another problematic case::

            sage: # needs sage.rings.number_field sage.rings.padics
            sage: R.<x> = QQ[]
            sage: Delta = (x^12 + 20*x^11 + 154*x^10 + 664*x^9 + 1873*x^8 + 3808*x^7 + 5980*x^6
            ....:           + 7560*x^5 + 7799*x^4 + 6508*x^3 + 4290*x^2 + 2224*x + 887)
            sage: K.<theta> = NumberField(x^6 + 108)
            sage: K.is_galois()
            True
            sage: vK = QQ.valuation(2).extension(K)
            sage: vK(2)
            1
            sage: vK(theta)
            1/3
            sage: G = Delta.change_ring(K)
            sage: vK.mac_lane_approximants(G)
            [[ Gauss valuation induced by 2-adic valuation,
               v(x + 1) = 1/4, v(x^4 + 1/2*theta^4 + 3*theta + 1) = 3/2 ],
             [ Gauss valuation induced by 2-adic valuation,
               v(x + 1) = 1/4, v(x^4 + 1/2*theta^4 + theta + 1) = 3/2 ],
             [ Gauss valuation induced by 2-adic valuation,
               v(x + 1) = 1/4, v(x^4 + 2*theta + 1) = 3/2 ]]

        An easy case that produced the wrong error at some point::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(2)
            sage: v.mac_lane_approximants(x^2 - 1/2)
            Traceback (most recent call last):
            ...
            ValueError: G must be integral

        Some examples that Sebastian Pauli used in a talk at Sage Days 87.
        Here we use ``assume_squarefree=True`` because :meth:`is_squarefree`
        is not properly implemented yet.

        ::

            sage: R = ZpFM(3, 7, print_mode='terse')
            sage: S.<x> = R[]
            sage: v = R.valuation()
            sage: f = x^4 + 234
            sage: len(v.mac_lane_approximants(f, assume_squarefree=True))               # needs sage.geometry.polyhedron
            ....:
            2

        ::

            sage: R = ZpFM(2, 50, print_mode='terse')
            sage: S.<x> = R[]
            sage: f = (x^32 + 16)*(x^32 + 16 + 2^16*x^2) + 2^34
            sage: v = R.valuation()
            sage: len(v.mac_lane_approximants(f, assume_squarefree=True))               # needs sage.geometry.polyhedron
            ....:
            2

        A case that triggered an assertion at some point::

            sage: v = QQ.valuation(3)
            sage: R.<x> = QQ[]
            sage: f = (x^36 + 60552000*x^33 + 268157412*x^30 + 173881701*x^27 + 266324841*x^24
            ....:       + 83125683*x^21 + 111803814*x^18 + 31925826*x^15 + 205726716*x^12
            ....:       + 17990262*x^9 + 351459648*x^6 + 127014399*x^3 + 359254116)
            sage: v.mac_lane_approximants(f)                                            # needs sage.geometry.polyhedron
            [[ Gauss valuation induced by 3-adic valuation,
               v(x) = 1/3,
               v(x^3 - 3) = 3/2,
               v(x^12 - 3*x^9 + 54*x^6 + 27/2*x^3 + 405/2) = 13/2,
               v(x^36 + 60552000*x^33 + 268157412*x^30 + 173881701*x^27 + 266324841*x^24
                  + 83125683*x^21 + 111803814*x^18 + 31925826*x^15 + 205726716*x^12
                  + 17990262*x^9 + 351459648*x^6 + 127014399*x^3 + 359254116) = +Infinity ]]
        """
    def mac_lane_approximant(self, G, valuation, approximants=None):
        """
        Return the approximant from :meth:`mac_lane_approximants` for ``G``
        which is approximated by or approximates ``valuation``.

        INPUT:

        - ``G`` -- a monic squarefree integral polynomial in a univariate
          polynomial ring over the domain of this valuation

        - ``valuation`` -- a valuation on the parent of ``G``

        - ``approximants`` -- the output of :meth:`mac_lane_approximants`;
          if not given, it is computed

        EXAMPLES::

            sage: v = QQ.valuation(2)
            sage: R.<x> = QQ[]
            sage: G = x^2 + 1

        We can select an approximant by approximating it::

            sage: w = GaussValuation(R, v).augmentation(x + 1, 1/2)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 ]

        As long as this is the only matching approximant, the approximation can
        be very coarse::

            sage: w = GaussValuation(R, v)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 ]

        Or it can be very specific::

            sage: w = GaussValuation(R, v).augmentation(x + 1, 1/2).augmentation(G, infinity)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1/2 ]

        But it must be an approximation of an approximant::

            sage: w = GaussValuation(R, v).augmentation(x, 1/2)
            sage: v.mac_lane_approximant(G, w)
            Traceback (most recent call last):
            ...
            ValueError: The valuation
            [ Gauss valuation induced by 2-adic valuation, v(x) = 1/2 ] is
            not an approximant for a valuation which extends 2-adic valuation
            with respect to x^2 + 1 since the valuation of x^2 + 1
            does not increase in every step

        The ``valuation`` must single out one approximant::

            sage: G = x^2 - 1
            sage: w = GaussValuation(R, v)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: The valuation Gauss valuation induced by 2-adic valuation
            does not approximate a unique extension of 2-adic valuation
            with respect to x^2 - 1

            sage: w = GaussValuation(R, v).augmentation(x + 1, 1)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: The valuation
            [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1 ] does not
            approximate a unique extension of 2-adic valuation with respect to x^2 - 1

            sage: w = GaussValuation(R, v).augmentation(x + 1, 2)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            [ Gauss valuation induced by 2-adic valuation, v(x + 1) = +Infinity ]

            sage: w = GaussValuation(R, v).augmentation(x + 3, 2)
            sage: v.mac_lane_approximant(G, w)                                          # needs sage.geometry.polyhedron sage.rings.padics
            [ Gauss valuation induced by 2-adic valuation, v(x + 1) = 1 ]
        """
    def montes_factorization(self, G, assume_squarefree: bool = False, required_precision=None):
        """
        Factor ``G`` over the completion of the domain of this valuation.

        INPUT:

        - ``G`` -- a monic polynomial over the domain of this valuation

        - ``assume_squarefree`` -- boolean (default: ``False``); whether to
          assume ``G`` to be squarefree

        - ``required_precision`` -- a number or infinity (default:
          infinity); if ``infinity``, the returned polynomials are actual factors of
          ``G``, otherwise they are only factors with precision at least
          ``required_precision``.

        ALGORITHM:

        We compute :meth:`mac_lane_approximants` with ``required_precision``.
        The key polynomials approximate factors of ``G``. This can be very
        slow unless ``required_precision`` is set to zero. Single factor
        lifting could improve this significantly.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: k = Qp(5,4)
            sage: v = k.valuation()
            sage: R.<x> = k[]
            sage: G = x^2 + 1
            sage: v.montes_factorization(G)                                             # needs sage.geometry.polyhedron
            ((1 + O(5^4))*x + 2 + 5 + 2*5^2 + 5^3 + O(5^4))
             * ((1 + O(5^4))*x + 3 + 3*5 + 2*5^2 + 3*5^3 + O(5^4))

        The computation might not terminate over incomplete fields (in
        particular because the factors can not be represented there)::

            sage: R.<x> = QQ[]
            sage: v = QQ.valuation(2)
            sage: v.montes_factorization(x^6 - 1)                                       # needs sage.geometry.polyhedron sage.rings.padics
            (x - 1) * (x + 1) * (x^2 - x + 1) * (x^2 + x + 1)

            sage: v.montes_factorization(x^7 - 1)       # not tested                    # needs sage.rings.padics

            sage: v.montes_factorization(x^7 - 1, required_precision=5)                 # needs sage.geometry.polyhedron sage.rings.padics
            (x - 1) * (x^3 - 5*x^2 - 6*x - 1) * (x^3 + 6*x^2 + 5*x - 1)

        TESTS:

        Some examples that Sebastian Pauli used in a talk at Sage Days 87.

        In this example, ``f`` factors as three factors of degree 50 over an
        unramified extension::

            sage: # needs sage.libs.flint
            sage: R.<u> = ZqFM(125)
            sage: S.<x> = R[]
            sage: f = (x^6+2)^25 + 5
            sage: v = R.valuation()
            sage: v.montes_factorization(f, assume_squarefree=True, required_precision=0)
            (x^50 + 2*5*x^45 + 5*x^40 + 5*x^30 + 2*x^25 + 3*5*x^20 + 2*5*x^10 + 2*5*x^5 + 5*x + 3 + 5) * (x^50 + 3*5*x^45 + 5*x^40 + 5*x^30 + (3 + 4*5)*x^25 + 3*5*x^20 + 2*5*x^10 + 3*5*x^5 + 4*5*x + 3 + 5) * (x^50 + 3*5*x^40 + 3*5*x^30 + 4*5*x^20 + 5*x^10 + 3 + 5)

        In this case, ``f`` factors into degrees 1, 2, and 5 over a totally ramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5)
            sage: S.<w> = R[]
            sage: R.<w> = R.extension(w^3 + 5)
            sage: S.<x> = R[]
            sage: f = (x^3 + 5)*(x^5 + w) + 625
            sage: v = R.valuation()
            sage: v.montes_factorization(f, assume_squarefree=True, required_precision=0)           # needs sage.libs.flint
            ((1 + O(w^60))*x + 4*w + O(w^61)) * ((1 + O(w^60))*x^2 + (w + O(w^61))*x + w^2 + O(w^62)) * ((1 + O(w^60))*x^5 + w + O(w^61))

        REFERENCES:

        The underlying algorithm is described in [Mac1936II]_ and thoroughly
        analyzed in [GMN2008]_.
        """

class MacLaneApproximantNode:
    """
    A node in the tree computed by :meth:`DiscreteValuation.mac_lane_approximants`.

    Leaves in the computation of the tree of approximants
    :meth:`~DiscreteValuation.mac_lane_approximants`. Each vertex consists of a
    tuple ``(v,ef,p,coeffs,vals)`` where ``v`` is an approximant, i.e., a
    valuation, ef is a boolean, ``p`` is the parent of this vertex, and
    ``coeffs`` and ``vals`` are cached values. (Only ``v`` and ``ef`` are
    relevant, everything else are caches/debug info.) The boolean ``ef``
    denotes whether ``v`` already has the final ramification index E and
    residue degree F of this approximant.  An edge V -- P represents the
    relation ``P.v`` `≤` ``V.v`` (pointwise on the polynomial ring K[x]) between the
    valuations.

    TESTS::

        sage: v = ZZ.valuation(3)
        sage: v.extension(GaussianIntegers())  # indirect doctest                       # needs sage.rings.number_field sage.rings.padics
        3-adic valuation
    """
    valuation: Incomplete
    parent: Incomplete
    ef: Incomplete
    principal_part_bound: Incomplete
    coefficients: Incomplete
    valuations: Incomplete
    forced_leaf: bool
    def __init__(self, valuation, parent, ef, principal_part_bound, coefficients, valuations) -> None:
        """
        TESTS::

            sage: from sage.rings.valuation.valuation import MacLaneApproximantNode
            sage: node = MacLaneApproximantNode(QQ.valuation(2), None, 1, None, None, None)
            sage: TestSuite(node).run()
        """
    def __eq__(self, other):
        """
        Return whether this node is equal to ``other``.

        EXAMPLES::

            sage: from sage.rings.valuation.valuation import MacLaneApproximantNode
            sage: n = MacLaneApproximantNode(QQ.valuation(2), None, 1, None, None, None)
            sage: m = MacLaneApproximantNode(QQ.valuation(3), None, 1, None, None, None)
            sage: n == m
            False
            sage: n == n
            True
        """
    def __ne__(self, other):
        """
        Return whether this node is not equal to ``other``.

        EXAMPLES::

            sage: from sage.rings.valuation.valuation import MacLaneApproximantNode
            sage: n = MacLaneApproximantNode(QQ.valuation(2), None, 1, None, None, None)
            sage: m = MacLaneApproximantNode(QQ.valuation(3), None, 1, None, None, None)
            sage: n != m
            True
            sage: n != n
            False
        """
    __hash__: Incomplete
