from sage.algebras.lie_algebras.lie_algebra import InfinitelyGeneratedLieAlgebra as InfinitelyGeneratedLieAlgebra, LieAlgebraWithGenerators as LieAlgebraWithGenerators
from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElement as LieAlgebraElement
from sage.categories.algebras import Algebras as Algebras
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.family import Family as Family
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators

class OnsagerAlgebra(LieAlgebraWithGenerators, IndexedGenerators):
    """
    The Onsager (Lie) algebra.

    The Onsager (Lie) algebra `\\mathcal{O}` is a Lie algebra with
    generators `A_0, A_1` that satisfy

    .. MATH::

        [A_0, [A_0, [A_0, A_1]]] = -4 [A_0, A_1],
        \\qquad
        [A_1, [A_1, [A_1, A_0]]] = -4 [A_1, A_0].

    .. NOTE::

        We are using a rescaled version of the usual defining generators.

    There exist a basis `\\{A_m, G_n \\mid m \\in \\ZZ, n \\in \\ZZ_{>0}\\}`
    for `\\mathcal{O}` with structure coefficients

    .. MATH::

        [A_m, A_{m'}] = G_{m-m'},
        \\qquad
        [G_n, G_{n'}] = 0,
        \\qquad
        [G_n, A_m] = 2A_{m-n} - 2A_{m+n},

    where `m > m'`.

    The Onsager algebra is isomorphic to the subalgebra of the affine
    Lie algebra `\\widehat{\\mathfrak{sl}}_2 = \\mathfrak{sl}_2 \\otimes
    \\CC[t,t^{-1}] \\oplus \\CC K \\oplus \\CC d` that is invariant under
    the Chevalley involution. In particular, we have

    .. MATH::

        A_i \\mapsto f \\otimes t^i - e \\otimes t^{-i},
        \\qquad
        G_i \\mapsto h \\otimes t^{-i} - h \\otimes t^i.

    where `e,f,h` are the Chevalley generators of `\\mathfrak{sl}_2`.

    EXAMPLES:

    We construct the Onsager algebra and do some basic computations::

        sage: O = lie_algebras.OnsagerAlgebra(QQ)
        sage: O.inject_variables()
        Defining A0, A1

    We verify the defining relations::

        sage: O([A0, [A0, [A0, A1]]]) == -4 * O([A0, A1])
        True
        sage: O([A1, [A1, [A1, A0]]]) == -4 * O([A1, A0])
        True

    We check the embedding into `\\widehat{\\mathfrak{sl}}_2`::

        sage: L = LieAlgebra(QQ, cartan_type=['A',1,1])
        sage: B = L.basis()
        sage: al = RootSystem(['A',1]).root_lattice().simple_root(1)
        sage: ac = al.associated_coroot()
        sage: def emb_A(i): return B[-al,i] - B[al,-i]
        sage: def emb_G(i): return B[ac,i] - B[ac,-i]
        sage: a0 = emb_A(0)
        sage: a1 = emb_A(1)
        sage: L([a0, [a0, [a0, a1]]]) == -4 * L([a0, a1])
        True
        sage: L([a1, [a1, [a1, a0]]]) == -4 * L([a1, a0])
        True

        sage: all(emb_G(n).bracket(emb_A(m)) == 2*emb_A(m-n) - 2*emb_A(m+n)
        ....:     for m in range(-10, 10) for n in range(1,10))
        True
        sage: all(emb_A(m).bracket(emb_A(mp)) == emb_G(m-mp)
        ....:     for m in range(-10,10) for mp in range(m-10, m))
        True

    REFERENCES:

    - [Onsager1944]_
    - [DG1982]_
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: TestSuite(O).run()
        """
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: O.basis()
            Lazy family (Onsager monomial(i))_{i in
             Disjoint union of Family (Integer Ring, Positive integers)}
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: O.lie_algebra_generators()
            Finite family {'A0': A[0], 'A1': A[1]}
        """
    def bracket_on_basis(self, x, y):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``
        where ``x < y``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: O.bracket_on_basis((1,3), (1,9))  # [G, G]
            0
            sage: O.bracket_on_basis((0,8), (1,13))  # [A, G]
            -2*A[-5] + 2*A[21]
            sage: O.bracket_on_basis((0,-9), (0, 7))  # [A, A]
            -G[16]
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: O.some_elements()
            [A[0], A[2], A[-1], G[4], -2*A[-3] + A[2] + 3*G[2]]
        """
    def quantum_group(self, q=None, c=None):
        """
        Return the quantum group of ``self``.

        The corresponding quantum group is the
        :class:`~sage.algebras.lie_algebras.onsager.QuantumOnsagerAlgebra`.
        The parameter `c` must be such that `c(1) = 1`

        INPUT:

        - ``q`` -- (optional) the quantum parameter; the default
          is `q \\in R(q)`, where `R` is the base ring of ``self``
        - ``c`` -- (optional) the parameter `c`; the default is ``q``

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: Q
            q-Onsager algebra with c=q over Fraction Field of
             Univariate Polynomial Ring in q over Rational Field
        """
    def alternating_central_extension(self):
        """
        Return the alternating central extension of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: ACE = O.alternating_central_extension()
            sage: ACE
            Alternating central extension of the Onsager algebra over Rational Field
        """
    Element = LieAlgebraElement

class QuantumOnsagerAlgebra(CombinatorialFreeModule):
    """
    The quantum Onsager algebra.

    The *quantum Onsager algebra*, or `q`-Onsager algebra, is a
    quantum group analog of the Onsager algebra. It is the left
    (or right) coideal subalgebra of the quantum group
    `U_q(\\widehat{\\mathfrak{sl}}_2)` and is the simplest example
    of a quantum symmetric pair coideal subalgebra of affine type.

    The `q`-Onsager algebra depends on a parameter `c` such that
    `c(1) = 1`. The `q`-Onsager algebra with parameter `c` is denoted
    `U_q(\\mathcal{O}_R)_c`, where `R` is the base ring of the
    defining Onsager algebra.

    EXAMPLES:

    We create the `q`-Onsager algebra and its generators::

        sage: O = lie_algebras.OnsagerAlgebra(QQ)
        sage: Q = O.quantum_group()
        sage: G = Q.algebra_generators()

    The generators are given as pairs, where `G[0,n]` is the generator
    `B_{n\\delta+\\alpha_1}` and `G[1,n]` is the generator `B_{n\\delta}`.
    We use the convention that
    `n\\delta + \\alpha_1 \\equiv (-n-1)\\delta + \\alpha_0`. ::

        sage: G[0,5]
        B[5d+a1]
        sage: G[0,-5]
        B[4d+a0]
        sage: G[1,5]
        B[5d]
        sage: (G[0,5] + G[0,-3]) * (G[1,2] - G[0,3])
        B[2d+a0]*B[2d] - B[2d+a0]*B[3d+a1]
         + ((-q^4+1)/q^2)*B[1d]*B[6d+a1]
         + ((q^4-1)/q^2)*B[1d]*B[4d+a1] + B[2d]*B[5d+a1]
         - B[5d+a1]*B[3d+a1] + ((q^2+1)/q^2)*B[7d+a1]
         + ((q^6+q^4-q^2-1)/q^2)*B[5d+a1] + (-q^4-q^2)*B[3d+a1]
        sage: (G[0,5] + G[0,-3] + G[1,4]) * (G[0,2] - G[1,3])
        -B[2d+a0]*B[3d] + B[2d+a0]*B[2d+a1]
         + ((q^4-1)/q^4)*B[1d]*B[7d+a1]
         + ((q^8-2*q^4+1)/q^4)*B[1d]*B[5d+a1]
         + (-q^4+1)*B[1d]*B[3d+a1] + ((q^4-1)/q^2)*B[2d]*B[6d+a1]
         + ((-q^4+1)/q^2)*B[2d]*B[4d+a1] - B[3d]*B[4d]
         - B[3d]*B[5d+a1] + B[4d]*B[2d+a1] + B[5d+a1]*B[2d+a1]
         + ((-q^2-1)/q^4)*B[8d+a1] + ((-q^6-q^4+q^2+1)/q^4)*B[6d+a1]
         + (-q^6-q^4+q^2+1)*B[4d+a1] + (q^6+q^4)*B[2d+a1]

    We check the `q`-Dolan-Grady relations::

        sage: def q_dolan_grady(a, b, q):
        ....:     x = q*a*b - ~q*b*a
        ....:     y = ~q*a*x - q*x*a
        ....:     return a*y - y*a
        sage: A0, A1 = G[0,-1], G[0,0]
        sage: q = Q.q()
        sage: q_dolan_grady(A1, A0, q) == (q^4 + 2*q^2 + 1) * (A0*A1 - A1*A0)
        True
        sage: q_dolan_grady(A0, A1, q) == (q^4 + 2*q^2 + 1) * (A1*A0 - A0*A1)
        True

    REFERENCES:

    - [BK2017]_
    """
    def __init__(self, g, q, c) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: TestSuite(Q).run()  # long time
        """
    def lie_algebra(self):
        """
        Return the underlying Lie algebra of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: Q.lie_algebra()
            Onsager algebra over Rational Field
            sage: Q.lie_algebra() is O
            True
        """
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: Q.algebra_generators()
            Lazy family (generator map(i))_{i in Disjoint union of
             Family (Integer Ring, Positive integers)}
        """
    gens = algebra_generators
    def q(self):
        """
        Return the parameter `q` of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: Q.q()
            q
        """
    def c(self):
        """
        Return the parameter `c` of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group(c=-3)
            sage: Q.c()
            -3
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis element indexing `1`.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: ob = Q.one_basis(); ob
            1
            sage: ob.parent()
            Free abelian monoid indexed by
             Disjoint union of Family (Integer Ring, Positive integers)
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: Q.some_elements()
            [B[a1], B[3d+a1], B[a0], B[1d], B[4d]]
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the basis element indexed by ``m``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: G = Q.algebra_generators()
            sage: B0 = G[0,0]
            sage: B1 = G[0,-1]
            sage: Q.degree_on_basis(B0.leading_support())
            1
            sage: Q.degree_on_basis((B1^10 * B0^10).leading_support())
            20
            sage: ((B0 * B1)^3).maximal_degree()
            6
        """
    @cached_method
    def product_on_basis(self, lhs, rhs):
        """
        Return the product of the two basis elements ``lhs`` and ``rhs``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: I = Q._indices.gens()
            sage: Q.product_on_basis(I[1,21]^2, I[1,31]^3)
            B[21d]^2*B[31d]^3
            sage: Q.product_on_basis(I[1,31]^3, I[1,21]^2)
            B[21d]^2*B[31d]^3
            sage: Q.product_on_basis(I[0,8], I[0,6])
            B[8d+a1]*B[6d+a1]
            sage: Q.product_on_basis(I[0,-8], I[0,6])
            B[7d+a0]*B[6d+a1]
            sage: Q.product_on_basis(I[0,-6], I[0,-8])
            B[5d+a0]*B[7d+a0]
            sage: Q.product_on_basis(I[0,-6], I[1,2])
            B[5d+a0]*B[2d]
            sage: Q.product_on_basis(I[1,6], I[0,2])
            B[6d]*B[2d+a1]

            sage: Q.product_on_basis(I[0,1], I[0,2])
            1/q^2*B[2d+a1]*B[1d+a1] - B[1d]
            sage: Q.product_on_basis(I[0,-3], I[0,-1])
            1/q^2*B[a0]*B[2d+a0] + ((-q^2+1)/q^2)*B[1d+a0]^2 - B[2d]
            sage: Q.product_on_basis(I[0,2], I[0,-1])
            q^2*B[a0]*B[2d+a1] + ((q^4-1)/q^2)*B[1d+a1]*B[a1]
             + (-q^2+1)*B[1d] + q^2*B[3d]
            sage: Q.product_on_basis(I[0,2], I[1,1])
            B[1d]*B[2d+a1] + (q^2+1)*B[3d+a1] + (-q^2-1)*B[1d+a1]
            sage: Q.product_on_basis(I[0,1], I[1,2])
            ((-q^4+1)/q^2)*B[1d]*B[2d+a1] + ((q^4-1)/q^2)*B[1d]*B[a1]
             + B[2d]*B[1d+a1] + (-q^4-q^2)*B[a0]
             + ((q^2+1)/q^2)*B[3d+a1] + ((q^6+q^4-q^2-1)/q^2)*B[1d+a1]
            sage: Q.product_on_basis(I[1,2], I[0,-1])
            B[a0]*B[2d] + ((-q^4+1)/q^2)*B[1d+a0]*B[1d]
             + ((q^4-1)/q^2)*B[1d]*B[a1] + ((q^2+1)/q^2)*B[2d+a0]
             + ((-q^2-1)/q^2)*B[1d+a1]
            sage: Q.product_on_basis(I[1,2], I[0,-4])
            ((q^4-1)/q^2)*B[2d+a0]*B[1d] + B[3d+a0]*B[2d]
             + ((-q^4+1)/q^2)*B[4d+a0]*B[1d] + (-q^4-q^2)*B[1d+a0]
             + ((q^6+q^4-q^2-1)/q^2)*B[3d+a0] + ((q^2+1)/q^2)*B[5d+a0]

        TESTS::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: Q = O.quantum_group()
            sage: G = Q.gens()
            sage: G[0,2]*(G[0,1]*G[0,3]) - (G[0,2]*G[0,1])*G[0,3]
            0
            sage: G[0,-2]*(G[0,-1]*G[0,-3]) - (G[0,-2]*G[0,-1])*G[0,-3]
            0
            sage: G[0,1]*(G[0,3]*G[0,-2]) - (G[0,1]*G[0,3])*G[0,-2]
            0
            sage: G[0,2]*(G[0,1]*G[1,3]) - (G[0,2]*G[0,1])*G[1,3]
            0
            sage: G[0,-2]*(G[0,1]*G[1,3]) - (G[0,-2]*G[0,1])*G[1,3]
            0
            sage: G[0,-2]*(G[1,1]*G[1,3]) - (G[0,-2]*G[1,1])*G[1,3]
            0
        """

class OnsagerAlgebraACE(InfinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    The alternating central extension of the Onsager algebra.

    The *alternating central extension* of the :class:`Onsager algebra
    <sage.algebras.lie_algebras.onsager.OnsagerAlgebra>` is the Lie algebra
    with basis elements `\\{\\mathcal{A}_k, \\mathcal{B}_k\\}_{k \\in \\ZZ}`
    that satisfy the relations

    .. MATH::

        \\begin{aligned}
        [\\mathcal{A}_k, \\mathcal{A}_m] & = \\mathcal{B}_{k-m} - \\mathcal{B}_{m-k},
        \\\\ [\\mathcal{A}_k, \\mathcal{B}_m] & = \\mathcal{A}_{k+m} - \\mathcal{A}_{k-m},
        \\\\ [\\mathcal{B}_k, \\mathcal{B}_m] & = 0.
        \\end{aligned}

    This has a natural injection from the Onsager algebra by the map `\\iota`
    defined by

    .. MATH::

        \\iota(A_k) = \\mathcal{A}_k,
        \\qquad\\qquad
        \\iota(B_k) = \\mathcal{B}_k - \\mathcal{B}_{-k}.

    Note that the map `\\iota` differs slightly from Lemma 4.18 in [Ter2021b]_
    due to our choice of basis of the Onsager algebra.

    .. WARNING::

        We have added an extra basis vector `\\mathcal{B}_0`, which would
        be `0` in the definition given in [Ter2021b]_.

    EXAMPLES:

    We begin by constructing the ACE and doing some sample computations::

        sage: O = lie_algebras.OnsagerAlgebra(QQ)
        sage: ACE = O.alternating_central_extension()
        sage: ACE
        Alternating central extension of the Onsager algebra over Rational Field

        sage: B = ACE.basis()
        sage: A1, A2, Am2 = B[0,1], B[0,2], B[0,-2]
        sage: B1, B2, Bm2 = B[1,1], B[1,2], B[1,-2]
        sage: A1.bracket(Am2)
        -B[-3] + B[3]
        sage: A1.bracket(A2)
        B[-1] - B[1]
        sage: A1.bracket(B2)
        -A[-1] + A[3]
        sage: A1.bracket(Bm2)
        A[-1] - A[3]
        sage: B2.bracket(B1)
        0
        sage: Bm2.bracket(B2)
        0
        sage: (A2 + Am2).bracket(B1 + A2 + B2 + Bm2)
        -A[-3] + A[-1] - A[1] + A[3] + B[-4] - B[4]

    The natural inclusion map `\\iota` is implemented as a coercion map::

        sage: iota = ACE.coerce_map_from(O)
        sage: b = O.basis()
        sage: am1, a2, b4 = b[0,-1], b[0,2], b[1,4]
        sage: iota(am1.bracket(a2)) == iota(am1).bracket(iota(a2))
        True
        sage: iota(am1.bracket(b4)) == iota(am1).bracket(iota(b4))
        True
        sage: iota(b4.bracket(a2)) == iota(b4).bracket(iota(a2))
        True

        sage: am1 + B2
        A[-1] + B[2]
        sage: am1.bracket(B2)
        -A[-3] + A[1]
        sage: Bm2.bracket(a2)
        -A[0] + A[4]

    We have the projection map `\\rho` from Lemma 4.19 in [Ter2021b]_:

    .. MATH::

        \\rho(\\mathcal{A}_k) = A_k,
        \\qquad\\qquad
        \\rho(\\mathcal{B}_k) = \\mathrm{sgn}(k) B_{|k|}.

    The kernel of `\\rho` is the center `\\mathcal{Z}`, which has a basis
    `\\{B_k + B_{-k}\\}_{k \\in \\ZZ}`::

        sage: rho = ACE.projection()
        sage: rho(A1)
        A[1]
        sage: rho(Am2)
        A[-2]
        sage: rho(B1)
        1/2*G[1]
        sage: rho(Bm2)
        -1/2*G[2]
        sage: all(rho(B[1,k] + B[1,-k]) == 0 for k in range(-6,6))
        True
        sage: all(B[0,m].bracket(B[1,k] + B[1,-k]) == 0
        ....:     for k in range(-4,4) for m in range(-4,4))
        True
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: ACE = lie_algebras.AlternatingCentralExtensionOnsagerAlgebra(QQ)
            sage: TestSuite(ACE).run()

            sage: B = ACE.basis()
            sage: A1, A2, Am2 = B[0,1], B[0,2], B[0,-2]
            sage: B1, B2, Bm2 = B[1,1], B[1,2], B[1,-2]
            sage: TestSuite(ACE).run(elements=[A1,A2,Am2,B1,B2,Bm2,ACE.an_element()])
        """
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ).alternating_central_extension()
            sage: O.basis()
            Lazy family (Onsager ACE monomial(i))_{i in
             Disjoint union of Family (Integer Ring, Integer Ring)}
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ).alternating_central_extension()
            sage: O.lie_algebra_generators()
            Lazy family (Onsager ACE monomial(i))_{i in
             Disjoint union of Family (Integer Ring, Integer Ring)}
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ).alternating_central_extension()
            sage: O.some_elements()
            [A[0], A[2], A[-1], B[4], B[-3], -2*A[-3] + A[2] + B[-1] + 3*B[2]]
        """
    def bracket_on_basis(self, x, y):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``
        where ``x < y``.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ).alternating_central_extension()
            sage: O.bracket_on_basis((1,3), (1,9))  # [B, B]
            0
            sage: O.bracket_on_basis((0,8), (1,13))  # [A, B]
            -A[-5] + A[21]
            sage: O.bracket_on_basis((0,-9), (0, 7))  # [A, A]
            B[-16] - B[16]
        """
    def projection(self):
        """
        Return the projection map `\\rho` from Lemma 4.19 in [Ter2021b]_
        to the Onsager algebra.

        EXAMPLES::

            sage: O = lie_algebras.OnsagerAlgebra(QQ)
            sage: ACE = O.alternating_central_extension()
            sage: rho = ACE.projection()
            sage: B = ACE.basis()
            sage: A1, A2, Am2 = B[0,1], B[0,2], B[0,-2]
            sage: B1, B2, Bm2 = B[1,1], B[1,2], B[1,-2]

            sage: rho(A1)
            A[1]
            sage: rho(Am2)
            A[-2]
            sage: rho(B1)
            1/2*G[1]
            sage: rho(B2)
            1/2*G[2]
            sage: rho(Bm2)
            -1/2*G[2]

            sage: rho(A1.bracket(A2))
            -G[1]
            sage: rho(A1).bracket(rho(A2))
            -G[1]
            sage: rho(B1.bracket(Am2))
            A[-3] - A[-1]
            sage: rho(B1).bracket(rho(Am2))
            A[-3] - A[-1]
        """
    Element = LieAlgebraElement
