from sage.categories.algebras import Algebras as Algebras
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.fields import Fields as Fields
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.subset import powerset as powerset
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.sets.family import Family as Family
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet

class QuantumCliffordAlgebra(CombinatorialFreeModule):
    """
    The quantum Clifford algebra.

    The *quantum Clifford algebra*, or `q`-Clifford algebra,
    of rank `n` and twist `k` is the unital associative algebra
    `\\mathrm{Cl}_{q}(n, k)` over a field `F` with generators
    `\\psi_a, \\psi_a^*, \\omega_a` for `a = 1, \\ldots, n` that
    satisfy the following relations:

    .. MATH::

        \\begin{aligned}
        \\omega_a \\omega_b & = \\omega_b \\omega_a,
        & \\omega_a^{4k} & = (1 + q^{-2k}) \\omega_a^{2k} - q^{-2k},
        \\\\ \\omega_a \\psi_b & = q^{\\delta_{ab}} \\psi_b \\omega_a,
        & \\omega_a \\psi^*_b & = \\psi^*_b \\omega_a,
        \\\\ \\psi_a \\psi_b & + \\psi_b \\psi_a = 0,
        & \\psi^*_a \\psi^*_b & + \\psi^*_b \\psi^*_a = 0,
        \\\\ \\psi_a \\psi^*_a & + q^k \\psi^*_a \\psi_a = \\omega_a^{-k},
        & \\psi^*_a \\psi_a & + q^{-k} \\psi^*_a \\psi_a = \\omega_a^k,
        \\\\ \\psi_a \\psi^*_b & + \\psi_b^* \\psi_a = 0
        & & \\text{if } a \\neq b.
        \\end{aligned}

    When `k = 2`, we recover the original definition given by Hayashi in
    [Hayashi1990]_. The `k = 1` version was used in [Kwon2014]_.

    INPUT:

    - ``n`` -- positive integer; the rank
    - ``k`` -- positive integer (default: 1); the twist
    - ``q`` -- (optional) the parameter `q`
    - ``F`` -- (default: `\\QQ(q)`) the base field that contains ``q``

    EXAMPLES:

    We construct the rank 3 and twist 1 `q`-Clifford algebra::

        sage: Cl = algebras.QuantumClifford(3)
        sage: Cl
        Quantum Clifford algebra of rank 3 and twist 1 with q=q over
         Fraction Field of Univariate Polynomial Ring in q over Integer Ring
        sage: q = Cl.q()

    Some sample computations::

        sage: p0, p1, p2, d0, d1, d2, w0, w1, w2 = Cl.gens()
        sage: p0 * p1
        psi0*psi1
        sage: p1 * p0
        -psi0*psi1
        sage: p0 * w0 * p1 * d0 * w2
        (1/(q^3-q))*psi1*w2 + (-q/(q^2-1))*psi1*w0^2*w2
        sage: w0^4
        -1/q^2 + ((q^2+1)/q^2)*w0^2

    We construct the homomorphism from `U_q(\\mathfrak{sl}_3)` to
    `\\mathrm{Cl}(3, 1)` given in (3.17) of [Hayashi1990]_::

        sage: e1 = p0*d1; e2 = p1*d2
        sage: f1 = p1*d0; f2 = p2*d1
        sage: k1 = w0*~w1; k2 = w1*~w2
        sage: k1i = w1*~w0; k2i = w2*~w1
        sage: (e1, e2, f1, f2, k1, k2, k1i, k2i)
        (psi0*psid1, psi1*psid2,
         -psid0*psi1, -psid1*psi2,
         (q^2+1)*w0*w1 - q^2*w0*w1^3, (q^2+1)*w1*w2 - q^2*w1*w2^3,
         (q^2+1)*w0*w1 - q^2*w0^3*w1, (q^2+1)*w1*w2 - q^2*w1^3*w2)

    We check that `k_i` and `k_i^{-1}` are inverses::

        sage: k1 * k1i
        1
        sage: k2 * k2i
        1

    The relations between `e_i`, `f_i`, and `k_i`::

        sage: k1 * f1 == q^-2 * f1 * k1
        True
        sage: k2 * f1 == q^1 * f1 * k2
        True
        sage: k2 * e1 == q^-1 * e1 * k2
        True
        sage: k1 * e1 == q^2 * e1 * k1
        True
        sage: e1 * f1 - f1 * e1 == (k1 - k1i)/(q-q^-1)
        True
        sage: e2 * f1 - f1 * e2
        0

    The `q`-Serre relations::

        sage: e1 * e1 * e2 - (q^1 + q^-1) * e1 * e2 * e1 + e2 * e1 * e1
        0
        sage: f1 * f1 * f2 - (q^1 + q^-1) * f1 * f2 * f1 + f2 * f1 * f1
        0

    This also can be constructed at the special point when `q^{2k} = 1`,
    but the basis used is different::

        sage: Cl = algebras.QuantumClifford(1, 1, -1)
        sage: Cl.inject_variables()
        Defining psi0, psid0, w0
        sage: psi0 * psid0
        psi0*psid0
        sage: psid0 * psi0
        -w0 + psi0*psid0
        sage: w0^2
        1
    """
    @staticmethod
    def __classcall_private__(cls, n, k: int = 1, q=None, F=None):
        """
        Standardize input to ensure a unique representation.

        TESTS::

            sage: Cl1 = algebras.QuantumClifford(3)
            sage: q = PolynomialRing(ZZ, 'q').fraction_field().gen()
            sage: Cl2 = algebras.QuantumClifford(3, q=q)
            sage: Cl3 = algebras.QuantumClifford(3, 1, q, q.parent())
            sage: Cl1 is Cl2 and Cl2 is Cl3
            True
        """
    def __init__(self, n, k, q, F, psi, indices) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(1, 2)
            sage: TestSuite(Cl).run(elements=Cl.basis())
        """
    def q(self):
        """
        Return the `q` of ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3)
            sage: Cl.q()
            q

            sage: Cl = algebras.QuantumClifford(3, q=QQ(-5))
            sage: Cl.q()
            -5
        """
    def twist(self):
        """
        Return the twist `k` of ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3, 2)
            sage: Cl.twist()
            2
        """
    def rank(self):
        """
        Return the rank `k` of ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3, 2)
            sage: Cl.rank()
            3
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3)
            sage: Cl.dimension()
            512

            sage: Cl = algebras.QuantumClifford(4, 2)  # long time
            sage: Cl.dimension()  # long time
            65536
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3)
            sage: Cl.algebra_generators()
            Finite family {'psi0': psi0, 'psi1': psi1, 'psi2': psi2,
                           'psid0': psid0, 'psid1': psid1, 'psid2': psid2,
                           'w0': w0, 'w1': w1, 'w2': w2}
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3)
            sage: Cl.gens()
            (psi0, psi1, psi2, psid0, psid1, psid2, w0, w1, w2)
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the basis element of `1`.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3)
            sage: Cl.one_basis()
            ((0, 0, 0), (0, 0, 0))
        """

class QuantumCliffordAlgebraGeneric(QuantumCliffordAlgebra):
    """
    The quantum Clifford algebra when `q^{2k} \\neq 1`.

    The *quantum Clifford algebra*, or `q`-Clifford algebra,
    of rank `n` and twist `k` is the unital associative algebra
    `\\mathrm{Cl}_{q}(n, k)` over a field `F` with generators
    `\\psi_a, \\psi_a^*, \\omega_a` for `a = 1, \\ldots, n` that
    satisfy the following relations:

    .. MATH::

        \\begin{aligned}
        \\omega_a \\omega_b & = \\omega_b \\omega_a,
        & \\omega_a^{4k} & = (1 + q^{-2k}) \\omega_a^{2k} - q^{-2k},
        \\\\ \\omega_a \\psi_b & = q^{\\delta_{ab}} \\psi_b \\omega_a,
        & \\omega_a \\psi^*_b & = \\psi^*_b \\omega_a,
        \\\\ \\psi_a \\psi_b & + \\psi_b \\psi_a = 0,
        & \\psi^*_a \\psi^*_b & + \\psi^*_b \\psi^*_a = 0,
        \\\\ \\psi_a \\psi^*_a & = \\frac{q^k \\omega_a^{3k} - q^{-k} \\omega_a^k}{q^k - q^{-k}},
        & \\psi^*_a \\psi_a & = \\frac{q^{2k} (\\omega_a - \\omega_a^{3k})}{q^k - q^{-k}},
        \\\\ \\psi_a \\psi^*_b & + \\psi_b^* \\psi_a = 0
        & & \\text{if } a \\neq b,
        \\end{aligned}

    where `q \\in F` such that `q^{2k} \\neq 1`.

    When `k = 2`, we recover the original definition given by Hayashi in
    [Hayashi1990]_. The `k = 1` version was used in [Kwon2014]_.
    """
    def __init__(self, n, k, q, F) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: Cl = algebras.QuantumClifford(1,3)
            sage: TestSuite(Cl).run(elements=Cl.basis())  # long time

            sage: Cl = algebras.QuantumClifford(3)
            sage: elts = Cl.some_elements() + list(Cl.algebra_generators())
            sage: TestSuite(Cl).run(elements=elts)  # long time

            sage: Cl = algebras.QuantumClifford(2, 4)
            sage: elts = Cl.some_elements() + list(Cl.algebra_generators())
            sage: TestSuite(Cl).run(elements=elts)  # long time
        """
    @cached_method
    def product_on_basis(self, m1, m2):
        """
        Return the product of the basis elements indexed by ``m1`` and ``m2``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(3)
            sage: Cl.inject_variables()
            Defining psi0, psi1, psi2, psid0, psid1, psid2, w0, w1, w2
            sage: psi0^2  # indirect doctest
            0
            sage: psid0^2
            0
            sage: w0 * psi0
            q*psi0*w0
            sage: w0 * psid0
            1/q*psid0*w0
            sage: w2 * w0
            w0*w2
            sage: w0^4
            -1/q^2 + ((q^2+1)/q^2)*w0^2
        """
    class Element(CombinatorialFreeModule.Element):
        def inverse(self):
            """
            Return the inverse if ``self`` is a basis element.

            EXAMPLES::

                sage: Cl = algebras.QuantumClifford(2)
                sage: Cl.inject_variables()
                Defining psi0, psi1, psid0, psid1, w0, w1
                sage: w0^-1
                (q^2+1)*w0 - q^2*w0^3
                sage: w0^-1 * w0
                1
                sage: w0^-2
                (q^2+1) - q^2*w0^2
                sage: w0^-2 * w0^2
                1
                sage: w0^-2 * w0 == w0^-1
                True
                sage: w = w0 * w1
                sage: w^-1
                (q^4+2*q^2+1)*w0*w1 + (-q^4-q^2)*w0*w1^3
                 + (-q^4-q^2)*w0^3*w1 + q^4*w0^3*w1^3
                sage: w^-1 * w
                1
                sage: w * w^-1
                1

                sage: (2*w0)^-1
                ((q^2+1)/2)*w0 - q^2/2*w0^3

                sage: (w0 + w1)^-1
                Traceback (most recent call last):
                ...
                ValueError: cannot invert self (= w1 + w0)
                sage: (psi0 * w0)^-1
                Traceback (most recent call last):
                ...
                ValueError: cannot invert self (= psi0*w0)

                sage: Cl = algebras.QuantumClifford(1, 2)
                sage: Cl.inject_variables()
                Defining psi0, psid0, w0
                sage: (psi0 + psid0).inverse()
                psid0*w0^2 + q^2*psi0*w0^2

                sage: Cl = algebras.QuantumClifford(2, 2)
                sage: Cl.inject_variables()
                Defining psi0, psi1, psid0, psid1, w0, w1
                sage: w0^-1
                (q^4+1)*w0^3 - q^4*w0^7
                sage: w0 * w0^-1
                1
            """
        __invert__ = inverse

class QuantumCliffordAlgebraRootUnity(QuantumCliffordAlgebra):
    """
    The quantum Clifford algebra when `q^{2k} = 1`.

    The *quantum Clifford algebra*, or `q`-Clifford algebra,
    of rank `n` and twist `k` is the unital associative algebra
    `\\mathrm{Cl}_{q}(n, k)` over a field `F` with generators
    `\\psi_a, \\psi_a^*, \\omega_a` for `a = 1, \\ldots, n` that
    satisfy the following relations:

    .. MATH::

        \\begin{aligned}
        \\omega_a \\omega_b & = \\omega_b \\omega_a,
        & \\omega_a^{2k} & = 1,
        \\\\ \\omega_a \\psi_b & = q^{\\delta_{ab}} \\psi_b \\omega_a,
        & \\omega_a \\psi^*_b & = \\psi^*_b \\omega_a,
        \\\\ \\psi_a \\psi_b & + \\psi_b \\psi_a = 0,
        & \\psi^*_a \\psi^*_b & + \\psi^*_b \\psi^*_a = 0,
        \\\\ \\psi_a \\psi^*_a & + q^k \\psi^*_a \\psi_a = \\omega_a^k
        & \\psi_a \\psi^*_b & + \\psi_b^* \\psi_a = 0 \\quad (a \\neq b),
        \\end{aligned}

    where `q \\in F` such that `q^{2k} = 1`. This has further relations of

    .. MATH::

        \\begin{aligned}
        \\psi^*_a \\psi_a \\psi^*_a & = \\psi^*_a \\omega_a^k,
        \\\\\n        \\psi_a \\psi^*_a \\psi_a & = q^k \\psi_a \\omega_a^k,
        \\\\\n        (\\psi_a \\psi^*_a)^2 & = \\psi_a \\psi^*_a \\omega_a^k.
        \\end{aligned}
    """
    def __init__(self, n, k, q, F) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Cl = algebras.QuantumClifford(1,2,-1)
            sage: TestSuite(Cl).run(elements=Cl.basis())

            sage: z = CyclotomicField(3).gen()
            sage: Cl = algebras.QuantumClifford(1,3,z)
            sage: TestSuite(Cl).run(elements=Cl.basis())

            sage: Cl = algebras.QuantumClifford(3,1,-1)
            sage: elts = Cl.some_elements() + list(Cl.algebra_generators())
            sage: TestSuite(Cl).run(elements=elts)  # long time

            sage: Cl = algebras.QuantumClifford(2,4,-1)
            sage: elts = Cl.some_elements() + list(Cl.algebra_generators())
            sage: TestSuite(Cl).run(elements=elts)  # long time
        """
    @cached_method
    def product_on_basis(self, m1, m2):
        """
        Return the product of the basis elements indexed by ``m1`` and ``m2``.

        EXAMPLES::

            sage: z = CyclotomicField(3).gen()
            sage: Cl = algebras.QuantumClifford(3, 3, z)
            sage: Cl.inject_variables()
            Defining psi0, psi1, psi2, psid0, psid1, psid2, w0, w1, w2
            sage: psi0^2  # indirect doctest
            0
            sage: psid0^2
            0
            sage: w0 * psi0
            -(-zeta3)*psi0*w0
            sage: w0 * psid0
            -(zeta3+1)*psid0*w0
            sage: psi0 * psid0
            psi0*psid0
            sage: psid0 * psi0
            w0^3 - psi0*psid0
            sage: w2 * w0
            w0*w2
            sage: w0^6
            1
            sage: psi0 * psi1
            psi0*psi1
            sage: psi1 * psi0
            -psi0*psi1
            sage: psi1 * (psi0 * psi2)
            -psi0*psi1*psi2

            sage: z = CyclotomicField(6).gen()
            sage: Cl = algebras.QuantumClifford(3, 3, z)
            sage: Cl.inject_variables()
            Defining psi0, psi1, psi2, psid0, psid1, psid2, w0, w1, w2

            sage: psid1 * (psi1 * psid1)
            psid1*w1^3
            sage: (psi1* psid1) * (psi1 * psid1)
            psi1*psid1*w1^3
            sage: (psi1 * psid1) * psi1
            -psi1*w1^3
        """
    class Element(QuantumCliffordAlgebra.Element):
        def inverse(self):
            """
            Return the inverse if ``self`` is a basis element.

            EXAMPLES::

                sage: Cl = algebras.QuantumClifford(3, 3, -1)
                sage: Cl.inject_variables()
                Defining psi0, psi1, psi2, psid0, psid1, psid2, w0, w1, w2
                sage: w0^-1
                w0^5
                sage: w0^-1 * w0
                1
                sage: w0^-2
                w0^4
                sage: w0^-2 * w0^2
                1
                sage: w0^-2 * w0 == w0^-1
                True
                sage: w = w0 * w1^3
                sage: w^-1
                w0^5*w1^3
                sage: w^-1 * w
                1
                sage: w * w^-1
                1

                sage: (2*w0)^-1
                1/2*w0^5

                sage: Cl = algebras.QuantumClifford(3, 1, -1)
                sage: Cl.inject_variables()
                Defining psi0, psi1, psi2, psid0, psid1, psid2, w0, w1, w2

                sage: (w0 + w1)^-1
                Traceback (most recent call last):
                ...
                ValueError: cannot invert self (= w1 + w0)
                sage: (psi0 * w0)^-1
                Traceback (most recent call last):
                ...
                ValueError: cannot invert self (= psi0*w0)

                sage: z = CyclotomicField(6).gen()
                sage: Cl = algebras.QuantumClifford(1, 3, z)
                sage: Cl.inject_variables()
                Defining psi0, psid0, w0
                sage: (psi0 + psid0).inverse()
                psid0*w0^3 - psi0*w0^3

                sage: Cl = algebras.QuantumClifford(2, 2, -1)
                sage: Cl.inject_variables()
                Defining psi0, psi1, psid0, psid1, w0, w1
                sage: w0^-1
                w0^3
                sage: w0 * w0^-1
                1
            """
        __invert__ = inverse
