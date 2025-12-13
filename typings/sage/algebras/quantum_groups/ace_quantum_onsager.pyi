from sage.categories.algebras import Algebras as Algebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers

class ACEQuantumOnsagerAlgebra(CombinatorialFreeModule):
    """
    The alternating central extension of the `q`-Onsager algebra.

    The *alternating central extension* `\\mathcal{A}_q` of the `q`-Onsager
    algebra `O_q` is a current algebra of `O_q` introduced by Baseilhac
    and Koizumi [BK2005]_. A presentation was given by Baseilhac
    and Shigechi [BS2010]_, which was then reformulated in terms of currents
    in [Ter2021]_ and then used to prove that the generators form a PBW basis.

    .. NOTE::

        This is only for the `q`-Onsager algebra with parameter
        `c = q^{-1} (q - q^{-1})^2`.

    EXAMPLES::

        sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
        sage: AG = A.algebra_generators()

    We construct the generators `\\mathcal{G}_3`, `\\mathcal{W}_{-5}`,
    `\\mathcal{W}_2`, and `\\widetilde{\\mathcal{G}}_{4}` and perform
    some computations::

        sage: G3 = AG[0,3]
        sage: Wm5 = AG[1,-5]
        sage: W2 = AG[1,2]
        sage: Gt4 = AG[2,4]
        sage: [G3, Wm5, W2, Gt4]
        [G[3], W[-5], W[2], Gt[4]]
        sage: Gt4 * G3
        G[3]*Gt[4] + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[-6]*W[1]
         + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[-5]*W[2]
         + ((q^12-3*q^8+3*q^4-1)/q^6)*W[-4]*W[1]
         + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[-4]*W[3]
         + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[-3]*W[-2]
         + ((q^12-3*q^8+3*q^4-1)/q^6)*W[-3]*W[2]
         + ((q^12-3*q^8+3*q^4-1)/q^6)*W[-2]*W[5]
         + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[-1]*W[4]
         + ((q^12-3*q^8+3*q^4-1)/q^6)*W[-1]*W[6]
         + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[0]*W[5]
         + ((q^12-3*q^8+3*q^4-1)/q^6)*W[0]*W[7]
         + ((q^12-3*q^8+3*q^4-1)/q^6)*W[3]*W[4]
        sage: Wm5 * G3
        ((q^2-1)/q^2)*G[1]*W[-7] + ((-q^2+1)/q^2)*G[1]*W[7]
         + ((q^2-1)/q^2)*G[2]*W[-6] + ((-q^2+1)/q^2)*G[2]*W[6] + G[3]*W[-5]
         + ((-q^2+1)/q^2)*G[6]*W[-2] + ((q^2-1)/q^2)*G[6]*W[2]
         + ((-q^2+1)/q^2)*G[7]*W[-1] + ((q^2-1)/q^2)*G[7]*W[1]
         + ((-q^2+1)/q^2)*G[8]*W[0] + ((-q^8+2*q^4-1)/q^5)*W[-8]
         + ((q^8-2*q^4+1)/q^5)*W[8]
        sage: W2 * G3
        (q^2-1)*G[1]*W[-2] + (-q^2+1)*G[1]*W[4] + (-q^2+1)*G[3]*W[0]
         + q^2*G[3]*W[2] + (q^2-1)*G[4]*W[1] + ((-q^8+2*q^4-1)/q^3)*W[-3]
         + ((q^8-2*q^4+1)/q^3)*W[5]
        sage: W2 * Wm5
        (q^4/(q^8+2*q^6-2*q^2-1))*G[1]*Gt[6] + (-q^4/(q^8+2*q^6-2*q^2-1))*G[6]*Gt[1]
         + W[-5]*W[2] + (q/(q^2+1))*G[7] + (-q/(q^2+1))*Gt[7]
        sage: Gt4 * Wm5
        ((q^2-1)/q^2)*W[-8]*Gt[1] + ((q^2-1)/q^2)*W[-7]*Gt[2]
         + ((q^2-1)/q^2)*W[-6]*Gt[3] + W[-5]*Gt[4] + ((-q^2+1)/q^2)*W[-3]*Gt[6]
         + ((-q^2+1)/q^2)*W[-2]*Gt[7] + ((-q^2+1)/q^2)*W[-1]*Gt[8]
         + ((-q^2+1)/q^2)*W[0]*Gt[9] + ((q^2-1)/q^2)*W[1]*Gt[8]
         + ((q^2-1)/q^2)*W[2]*Gt[7] + ((q^2-1)/q^2)*W[3]*Gt[6]
         + ((-q^2+1)/q^2)*W[6]*Gt[3] + ((-q^2+1)/q^2)*W[7]*Gt[2]
         + ((-q^2+1)/q^2)*W[8]*Gt[1] + ((-q^8+2*q^4-1)/q^5)*W[-9]
         + ((q^8-2*q^4+1)/q^5)*W[9]
        sage: Gt4 * W2
        (q^2-1)*W[-3]*Gt[1] + (-q^2+1)*W[0]*Gt[4] + (q^2-1)*W[1]*Gt[5]
         + q^2*W[2]*Gt[4] + (-q^2+1)*W[5]*Gt[1] + ((-q^8+2*q^4-1)/q^3)*W[-4]
         + ((q^8-2*q^4+1)/q^3)*W[6]

    REFERENCES:

    - [BK2005]_
    - [BS2010]_
    - [Ter2021]_
    """
    @staticmethod
    def __classcall_private__(cls, R=None, q=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: A1 = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: R.<q> = QQ[]
            sage: q = R.gen()
            sage: A2 = algebras.AlternatingCentralExtensionQuantumOnsager(R.fraction_field(), q)
            sage: A1 is A2
            True
            sage: A2.q().parent() is R.fraction_field()
            True
            sage: q = R.fraction_field().gen()
            sage: A3 = algebras.AlternatingCentralExtensionQuantumOnsager(q=q)
            sage: A1 is A3
            True
        """
    def __init__(self, R, q) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: TestSuite(A).run()  # long time
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: A.algebra_generators()
            Lazy family (generator map(i))_{i in Disjoint union of
             Family (Positive integers, Integer Ring, Positive integers)}
        """
    gens = algebra_generators
    def q(self):
        """
        Return the parameter `q` of ``self``.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: A.q()
            q
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis element indexing `1`.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: ob = A.one_basis(); ob
            1
            sage: ob.parent()
            Free abelian monoid indexed by Disjoint union of
             Family (Positive integers, Integer Ring, Positive integers)
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: A.some_elements()
            [W[0], W[3], W[-1], W[1], W[-2], G[1], G[2], Gt[1], Gt[2]]
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the basis element indexed by ``m``.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: G = A.algebra_generators()
            sage: A.degree_on_basis(G[0,1].leading_support())
            2
            sage: A.degree_on_basis(G[0,2].leading_support())
            4
            sage: A.degree_on_basis(G[1,-1].leading_support())
            3
            sage: A.degree_on_basis(G[1,0].leading_support())
            1
            sage: A.degree_on_basis(G[1,1].leading_support())
            1
            sage: A.degree_on_basis(G[2,1].leading_support())
            2
            sage: A.degree_on_basis(G[2,2].leading_support())
            4
            sage: [x.degree() for x in A.some_elements()]
            [1, 5, 3, 1, 5, 2, 4, 2, 4]
        """
    @cached_method
    def quantum_onsager_pbw_generator(self, i):
        """
        Return the image of the PBW generator of the `q`-Onsager algebra
        in ``self``.

        INPUT:

        - ``i`` -- a pair ``(k, m)`` such that

          * ``k=0`` and ``m`` is an integer
          * ``k=1`` and ``m`` is a positive integer

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: A.quantum_onsager_pbw_generator((0,0))
            W[1]
            sage: A.quantum_onsager_pbw_generator((0,1))
            (q^3/(q^4-1))*W[1]*Gt[1] - q^2*W[0] + (q^2+1)*W[2]
            sage: A.quantum_onsager_pbw_generator((0,2))
            (q^6/(q^8-2*q^4+1))*W[1]*Gt[1]^2 + (-q^5/(q^4-1))*W[0]*Gt[1]
             + (q^3/(q^2-1))*W[1]*Gt[2] + (q^3/(q^2-1))*W[2]*Gt[1]
             + (-q^4-q^2)*W[-1] - q^2*W[1] + (q^4+2*q^2+1)*W[3]
            sage: A.quantum_onsager_pbw_generator((0,-1))
            W[0]
            sage: A.quantum_onsager_pbw_generator((0,-2))
            (q/(q^4-1))*W[0]*Gt[1] + ((q^2+1)/q^2)*W[-1] - 1/q^2*W[1]
            sage: A.quantum_onsager_pbw_generator((0,-3))
            (q^2/(q^8-2*q^4+1))*W[0]*Gt[1]^2 + (1/(q^3-q))*W[-1]*Gt[1]
             + (1/(q^3-q))*W[0]*Gt[2] - (1/(q^5-q))*W[1]*Gt[1]
             + ((q^4+2*q^2+1)/q^4)*W[-2] - 1/q^2*W[0] + ((-q^2-1)/q^4)*W[2]
            sage: A.quantum_onsager_pbw_generator((1,1))
            ((-q^2+1)/q^2)*W[0]*W[1] + (1/(q^3+q))*G[1] - (1/(q^3+q))*Gt[1]
            sage: A.quantum_onsager_pbw_generator((1,2))
            -1/q*W[0]*W[1]*Gt[1] + (1/(q^6+q^4-q^2-1))*G[1]*Gt[1]
             + ((-q^4+1)/q^4)*W[-1]*W[1] + (q^2-1)*W[0]^2
             + ((-q^4+1)/q^2)*W[0]*W[2] + ((q^2-1)/q^4)*W[1]^2
             - (1/(q^6+q^4-q^2-1))*Gt[1]^2 + 1/q^3*G[2] - 1/q^3*Gt[2]
        """
    @cached_method
    def product_on_basis(self, lhs, rhs):
        """
        Return the product of the two basis elements ``lhs`` and ``rhs``.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: G = A.algebra_generators()
            sage: q = A.q()
            sage: rho = -(q^2 - q^-2)^2

        We verify the PBW ordering::

            sage: G[0,1] * G[1,1]  # indirect doctest
            G[1]*W[1]
            sage: G[1,1] * G[0,1]
            q^2*G[1]*W[1] + ((-q^8+2*q^4-1)/q^3)*W[0] + ((q^8-2*q^4+1)/q^3)*W[2]
            sage: G[1,-1] * G[1,1]
            W[-1]*W[1]
            sage: G[1,1] * G[1,-1]
            W[-1]*W[1] + (q/(q^2+1))*G[2] + (-q/(q^2+1))*Gt[2]
            sage: G[1,1] * G[2,1]
            W[1]*Gt[1]
            sage: G[2,1] * G[1,1]
            q^2*W[1]*Gt[1] + ((-q^8+2*q^4-1)/q^3)*W[0] + ((q^8-2*q^4+1)/q^3)*W[2]
            sage: G[0,1] * G[2,1]
            G[1]*Gt[1]
            sage: G[2,1] * G[0,1]
            G[1]*Gt[1] + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[-1]*W[1]
             + ((-q^12+3*q^8-3*q^4+1)/q^6)*W[0]^2
             + ((q^12-3*q^8+3*q^4-1)/q^6)*W[0]*W[2]
             + ((q^12-3*q^8+3*q^4-1)/q^6)*W[1]^2

        We verify some of the defining relations (see Equations (3-14)
        in [Ter2021]_), which are used to construct the PBW basis::

            sage: G[0,1] * G[0,2] == G[0,2] * G[0,1]
            True
            sage: G[1,-1] * G[1,-2] == G[1,-2] * G[1,-1]
            True
            sage: G[1,1] * G[1,2] == G[1,2] * G[1,1]
            True
            sage: G[2,1] * G[2,2] == G[2,2] * G[2,1]
            True
            sage: G[1,0] * G[1,2] - G[1,2] * G[1,0] == G[1,-1] * G[1,1] - G[1,1] * G[1,-1]
            True
            sage: G[1,0] * G[1,2] - G[1,2] * G[1,0] == (G[2,2] - G[0,2]) / (q + ~q)
            True
            sage: q * G[1,0] * G[0,2] - ~q * G[0,2] * G[1,0] == q * G[2,2] * G[1,0] - ~q * G[1,0] * G[2,2]
            True
            sage: q * G[1,0] * G[0,2] - ~q * G[0,2] * G[1,0] == rho * G[1,-2] - rho * G[1,2]
            True
            sage: q * G[0,2] * G[1,1] - ~q * G[1,1] * G[0,2] == q * G[1,1] * G[2,2] - ~q * G[2,2] * G[1,1]
            True
            sage: q * G[0,2] * G[1,1] - ~q * G[1,1] * G[0,2] == rho * G[1,3] - rho * G[1,-1]
            True
            sage: G[1,-2] * G[1,2] - G[1,2] * G[1,-2] == G[1,-1] * G[1,3] - G[1,3] * G[1,-1]
            True
            sage: G[1,-2] * G[0,2] - G[0,2] * G[1,-2] == G[1,-1] * G[0,3] - G[0,3] * G[1,-1]
            True
            sage: G[1,1] * G[0,2] - G[0,2] * G[1,1] == G[1,2] * G[0,1] - G[0,1] * G[1,2]
            True
            sage: G[1,-2] * G[2,2] - G[2,2] * G[1,-2] == G[1,-1] * G[2,3] - G[2,3] * G[1,-1]
            True
            sage: G[1,1] * G[2,2] - G[2,2] * G[1,1] == G[1,2] * G[2,1] - G[2,1] * G[1,2]
            True
            sage: G[0,1] * G[2,2] - G[2,2] * G[0,1] == G[0,2] * G[2,1] - G[2,1] * G[0,2]
            True
        """
    @lazy_attribute
    def sigma(self):
        """
        The automorphism `\\sigma`.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: G = A.algebra_generators()
            sage: x = A.an_element()^2
            sage: A.sigma(A.sigma(x)) == x
            True
            sage: A.sigma(G[1,-1] * G[1,1]) == A.sigma(G[1,-1]) * A.sigma(G[1,1])
            True
            sage: A.sigma(G[0,2] * G[1,3]) == A.sigma(G[0,2]) * A.sigma(G[1,3])
            True
        """
    @lazy_attribute
    def dagger(self):
        """
        The antiautomorphism `\\dagger`.

        EXAMPLES::

            sage: A = algebras.AlternatingCentralExtensionQuantumOnsager(QQ)
            sage: G = A.algebra_generators()
            sage: x = A.an_element()^2
            sage: A.dagger(A.dagger(x)) == x
            True
            sage: A.dagger(G[1,-1] * G[1,1]) == A.dagger(G[1,1]) * A.dagger(G[1,-1])
            True
            sage: A.dagger(G[0,2] * G[1,3]) == A.dagger(G[1,3]) * A.dagger(G[0,2])
            True
            sage: A.dagger(G[2,2] * G[1,3]) == A.dagger(G[1,3]) * A.dagger(G[2,2])
            True
        """
