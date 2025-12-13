from sage.categories.algebras import Algebras as Algebras
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

class QuantumOscillatorAlgebra(CombinatorialFreeModule):
    """
    The quantum oscillator algebra.

    Let `R` be a commutative algebra and `q \\in R` be a unit.
    The *quantum oscillator algebra*, or `q`-oscillator algebra,
    is the unital associative `R`-algebra with generators `a^+`,
    `a^-` and `k^{\\pm 1}` satisfying the following relations:

    .. MATH::

        k a^{\\pm} = q^{\\pm 1} a^{\\pm} k, \\qquad
        a^- a^+ = 1 - q^2 k^2, \\qquad
        a^+ a^- = 1 - k^2.

    INPUT:

    - ``q`` -- (optional) the parameter `q`
    - ``R`` -- (default: `\\QQ(q)`) the base ring that contains ``q``

    EXAMPLES:

    We construct the algebra and perform some basic computations::

        sage: O = algebras.QuantumOscillator()
        sage: ap, am, k, ki = O.algebra_generators()
        sage: q = O.q()
        sage: k^-3 * ap * ki * am^2 * k - q^3 * ap * k^3
        q^5*a-*k^-3 - q^3*a-*k^-1 - q^3*a+*k^3

    We construct representations of the type `A_1` quantum coordinate ring
    using the quantum oscillator algebra and verify the quantum determinant::

        sage: pi = matrix([[am, k], [-q*k, ap]]); pi
        [  a-    k]
        [-q*k   a+]
        sage: pi[0,0] * pi[1,1] - q * pi[0,1] * pi[1,0]
        1

    Next, we use this to build representations for type `A_2`::

        sage: def quantum_det(M):
        ....:     n = M.nrows()
        ....:     return sum((-q)**sigma.length()
        ....:                * prod(M[i,sigma[i]-1] for i in range(n))
        ....:                for sigma in Permutations(n))
        sage: def build_repr(wd, gens):
        ....:     n = gens[0].nrows()
        ....:     ret = gens[wd[0]-1]
        ....:     for ind in wd[1:]:
        ....:         g = gens[ind-1]
        ....:         temp = [[None]*n for _ in range(n)]
        ....:         for i in range(n):
        ....:             for j in range(n):
        ....:                 temp[i][j] = sum(tensor([ret[i,k], g[k,j]]) for k in range(n))
        ....:         ret = matrix(temp)
        ....:     return ret
        sage: pi1 = matrix.block_diagonal(pi, matrix.identity(1)); pi1
        [  a-    k|   0]
        [-q*k   a+|   0]
        [---------+----]
        [   0    0|   1]
        sage: pi2 = matrix.block_diagonal(matrix.identity(1), pi); pi2
        [   1|   0    0]
        [----+---------]
        [   0|  a-    k]
        [   0|-q*k   a+]
        sage: quantum_det(pi1) == 1
        True
        sage: quantum_det(pi2) == 1
        True
        sage: pi12 = build_repr([1,2], [pi1, pi2]); pi12
        [  a- # 1   k # a-    k # k]
        [-q*k # 1  a+ # a-   a+ # k]
        [       0 -q*1 # k   1 # a+]
        sage: quantum_det(pi12)
        1 # 1
        sage: pi121 = build_repr([1,2,1], [pi1, pi2]); pi121
        [   a- # 1 # a- - q*k # a- # k      a- # 1 # k + k # a- # a+                     k # k # 1]
        [-q*k # 1 # a- - q*a+ # a- # k   -q*k # 1 # k + a+ # a- # a+                    a+ # k # 1]
        [                q^2*1 # k # k                 -q*1 # k # a+                    1 # a+ # 1]
        sage: quantum_det(pi121)
        1 # 1 # 1
        sage: pi212 = build_repr([2,1,2], [pi1, pi2]); pi212
        [                   1 # a- # 1                    1 # k # a-                     1 # k # k]
        [                -q*a- # k # 1    a- # a+ # a- - q*k # 1 # k      a- # a+ # k + k # 1 # a+]
        [                q^2*k # k # 1 -q*k # a+ # a- - q*a+ # 1 # k   -q*k # a+ # k + a+ # 1 # a+]
        sage: quantum_det(pi212)
        1 # 1 # 1

    REFERENCES:

    - [Kuniba2022]_ Section 3.2
    """
    @staticmethod
    def __classcall_private__(cls, q=None, R=None):
        """
        Standardize input to ensure a unique representation.

        TESTS::

            sage: O1 = algebras.QuantumOscillator()
            sage: q = PolynomialRing(ZZ, 'q').fraction_field().gen()
            sage: O2 = algebras.QuantumOscillator(q=q)
            sage: O3 = algebras.QuantumOscillator(q, q.parent())
            sage: O1 is O2 and O2 is O3
            True
        """
    def __init__(self, q, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: TestSuite(O).run()
        """
    def q(self):
        """
        Return the `q` of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: O.q()
            q
            sage: O = algebras.QuantumOscillator(q=QQ(-5))
            sage: O.q()
            -5
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: O.algebra_generators()
            Finite family {'am': a-, 'ap': a+, 'k': k, 'ki': k^-1}
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: O.gens()
            (a+, a-, k, k^-1)
        """
    @cached_method
    def one_basis(self) -> tuple:
        """
        Return the index of the basis element of `1`.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: O.one_basis()
            (0, 0)
        """
    def some_elements(self) -> tuple:
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: O.some_elements()
            (a+, a-, k, k^-1, 1, a+^3, a-^4, k^2, k^-5, a+*k,
             a-^4*k^-3, 1 + 3*k + 2*a+ + a+*k)
        """
    def fock_space_representation(self):
        """
        Return the Fock space representation of ``self``.

        .. SEEALSO::

            :class:`~sage.algebras.quantum_oscillator.FockSpaceRepresentation`

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: O.fock_space_representation()
            Fock space representation of Quantum oscillator algebra with q=q
             over Fraction Field of Univariate Polynomial Ring in q over Integer Ring
        """
    @cached_method
    def product_on_basis(self, ml, mr):
        """
        Return the product of the basis elements indexed by ``ml`` and ``mr``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: ap, am, k, ki = O.algebra_generators()
            sage: O.product_on_basis((-2, 3), (-4, 5))
            1/q^12*a-^6*k^8
            sage: O.product_on_basis((2, 3), (4, -5))
            q^12*a+^6*k^-2
            sage: O.product_on_basis((2, 3), (0, -3))
            a+^2
            sage: k^5 * ki^10
            k^-5
            sage: k^10 * ki^5
            k^5
            sage: ap^3 * k^5
            a+^3*k^5
            sage: am^3 * k^5
            a-^3*k^5
            sage: k^5 * ap^3
            q^15*a+^3*k^5
            sage: k^5 * am^3
            1/q^15*a-^3*k^5
            sage: ki^5 * ap^3
            1/q^15*a+^3*k^-5
            sage: ki^5 * am^3
            q^15*a-^3*k^-5
            sage: ap * am
            1 - k^2
            sage: am * ap
            1 - q^2*k^2

            sage: (ap + am + k + ki)^2
            a-^2 + (q+1)*a-*k^-1 + ((q+1)/q)*a-*k + k^-2 + 4 - q^2*k^2
             + ((q+1)/q)*a+*k^-1 + (q+1)*a+*k + a+^2

            sage: (ap)^3 * (am)^5
            a-^2 + ((-q^4-q^2-1)/q^8)*a-^2*k^2 + ((q^4+q^2+1)/q^14)*a-^2*k^4 - 1/q^18*a-^2*k^6
            sage: (ap)^5 * (am)^3
            a+^2 + ((-q^4-q^2-1)/q^4)*a+^2*k^2 + ((q^4+q^2+1)/q^6)*a+^2*k^4 - 1/q^6*a+^2*k^6
            sage: (am)^3 * (ap)^5
            a+^2 + (-q^10-q^8-q^6)*a+^2*k^2 + (q^18+q^16+q^14)*a+^2*k^4 - q^24*a+^2*k^6
            sage: (am)^5 * (ap)^3
            a-^2 + (-q^6-q^4-q^2)*a-^2*k^2 + (q^10+q^8+q^6)*a-^2*k^4 - q^12*a-^2*k^6
        """
    class Element(CombinatorialFreeModule.Element):
        def __invert__(self):
            """
            Return the inverse if ``self`` is a basis element.

            EXAMPLES::

                sage: O = algebras.QuantumOscillator()
                sage: ap, am, k, ki = O.algebra_generators()
                sage: k.inverse()
                k^-1
                sage: ~k^5
                k^-5
                sage: ~ki^2
                k^2
                sage: O.zero().inverse()
                Traceback (most recent call last):
                ...
                ZeroDivisionError
                sage: ~ap
                Traceback (most recent call last):
                ...
                NotImplementedError: only implemented for monomials in k
                sage: ~(k + ki)
                Traceback (most recent call last):
                ...
                NotImplementedError: only implemented for monomials in k
            """

class FockSpaceRepresentation(CombinatorialFreeModule):
    """
    The unique Fock space representation of the
    :class:`~sage.algebras.quantum_oscillator.QuantumOscillatorAlgebra`.
    """
    def __init__(self, oscillator_algebra) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: F = O.fock_space_representation()
            sage: TestSuite(F).run()
        """
    def vacuum(self):
        """
        Return the vacuum element `|0\\rangle` of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: F = O.fock_space_representation()
            sage: F.vacuum()
            |0>
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: O = algebras.QuantumOscillator()
            sage: F = O.fock_space_representation()
            sage: F.some_elements()
            (|0>, |1>, |52>, |0> + 2*|1> + 3*|2> + |42>)
        """
    class Element(CombinatorialFreeModule.Element): ...
