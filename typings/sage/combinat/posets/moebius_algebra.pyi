from sage.categories.algebras import Algebras as Algebras
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent, Realizations as Realizations
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class BasisAbstract(CombinatorialFreeModule, BindableClass):
    """
    Abstract base class for a basis.
    """
    def __getitem__(self, x):
        """
        Return the basis element indexed by ``x``.

        INPUT:

        - ``x`` -- an element of the lattice

        EXAMPLES::

            sage: L = posets.BooleanLattice(4)
            sage: E = L.moebius_algebra(QQ).E()
            sage: E[5]
            E[5]
            sage: C = L.quantum_moebius_algebra().C()
            sage: C[5]
            C[5]
        """

class MoebiusAlgebra(Parent, UniqueRepresentation):
    """
    The Möbius algebra of a lattice.

    Let `L` be a lattice. The *Möbius algebra* `M_L` was originally
    constructed by Solomon [Solomon67]_ and has a natural basis
    `\\{ E_x \\mid x \\in L \\}` with multiplication given by
    `E_x \\cdot E_y = E_{x \\vee y}`. Moreover this has a basis given by
    orthogonal idempotents `\\{ I_x \\mid x \\in L \\}` (so
    `I_x I_y = \\delta_{xy} I_x` where `\\delta` is the Kronecker delta)
    related to the natural basis by

    .. MATH::

        I_x = \\sum_{x \\leq y} \\mu_L(x, y) E_y,

    where `\\mu_L` is the Möbius function of `L`.

    .. NOTE::

        We use the join `\\vee` for our multiplication, whereas [Greene73]_
        and [Etienne98]_ define the Möbius algebra using the meet `\\wedge`.
        This is done for compatibility with :class:`QuantumMoebiusAlgebra`.

    REFERENCES:

    .. [Solomon67] Louis Solomon.
       *The Burnside Algebra of a Finite Group*.
       Journal of Combinatorial Theory, **2**, 1967.
       :doi:`10.1016/S0021-9800(67)80064-4`.

    .. [Greene73] Curtis Greene.
       *On the Möbius algebra of a partially ordered set*.
       Advances in Mathematics, **10**, 1973.
       :doi:`10.1016/0001-8708(73)90106-0`.

    .. [Etienne98] Gwihen Etienne.
       *On the Möbius algebra of geometric lattices*.
       European Journal of Combinatorics, **19**, 1998.
       :doi:`10.1006/eujc.1998.0227`.
    """
    def __init__(self, R, L) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: L = posets.BooleanLattice(3)
            sage: M = L.moebius_algebra(QQ)
            sage: TestSuite(M).run()
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the `B`-basis).

        EXAMPLES::

            sage: L = posets.BooleanLattice(4)
            sage: M = L.moebius_algebra(QQ)
            sage: M.a_realization()
            Moebius algebra of Finite lattice containing 16 elements
             over Rational Field in the natural basis
        """
    def lattice(self):
        """
        Return the defining lattice of ``self``.

        EXAMPLES::

            sage: L = posets.BooleanLattice(4)
            sage: M = L.moebius_algebra(QQ)
            sage: M.lattice()
            Finite lattice containing 16 elements
            sage: M.lattice() == L
            True
        """
    class E(BasisAbstract):
        """
        The natural basis of a Möbius algebra.

        Let `E_x` and `E_y` be basis elements of `M_L` for some lattice `L`.
        Multiplication is given by `E_x E_y = E_{x \\vee y}`.
        """
        def __init__(self, M, prefix: str = 'E') -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: L = posets.BooleanLattice(4)
                sage: M = L.moebius_algebra(QQ)
                sage: TestSuite(M.E()).run()
            """
        def product_on_basis(self, x, y):
            """
            Return the product of basis elements indexed by ``x`` and ``y``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: E = L.moebius_algebra(QQ).E()
                sage: E.product_on_basis(5, 14)
                E[15]
                sage: E.product_on_basis(2, 8)
                E[10]

            TESTS::

                sage: M = posets.BooleanLattice(4).moebius_algebra(QQ)
                sage: E = M.E()
                sage: I = M.I()
                sage: all(I(x)*I(y) == I(x*y) for x in E.basis() for y in E.basis())
                True
            """
        @cached_method
        def one(self):
            """
            Return the element ``1`` of ``self``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: E = L.moebius_algebra(QQ).E()
                sage: E.one()
                E[0]
            """
    natural = E
    class I(BasisAbstract):
        """
        The (orthogonal) idempotent basis of a Möbius algebra.

        Let `I_x` and `I_y` be basis elements of `M_L` for some lattice `L`.
        Multiplication is given by `I_x I_y = \\delta_{xy} I_x` where
        `\\delta_{xy}` is the Kronecker delta.
        """
        def __init__(self, M, prefix: str = 'I') -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: L = posets.BooleanLattice(4)
                sage: M = L.moebius_algebra(QQ)
                sage: TestSuite(M.I()).run()

            Check that the transition maps can be pickled::

                sage: L = posets.BooleanLattice(4)
                sage: M = L.moebius_algebra(QQ)
                sage: E = M.E()
                sage: I = M.I()
                sage: phi = E.coerce_map_from(I)
                sage: loads(dumps(phi))
                Generic morphism:
                ...
            """
        def product_on_basis(self, x, y):
            """
            Return the product of basis elements indexed by ``x`` and ``y``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: I = L.moebius_algebra(QQ).I()
                sage: I.product_on_basis(5, 14)
                0
                sage: I.product_on_basis(2, 2)
                I[2]

            TESTS::

                sage: M = posets.BooleanLattice(4).moebius_algebra(QQ)
                sage: E = M.E()
                sage: I = M.I()
                sage: all(E(x)*E(y) == E(x*y) for x in I.basis() for y in I.basis())
                True
            """
        @cached_method
        def one(self):
            """
            Return the element ``1`` of ``self``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: I = L.moebius_algebra(QQ).I()
                sage: I.one()
                I[0] + I[1] + I[2] + I[3] + I[4] + I[5] + I[6] + I[7] + I[8]
                 + I[9] + I[10] + I[11] + I[12] + I[13] + I[14] + I[15]
            """
        def __getitem__(self, x):
            """
            Return the basis element indexed by ``x``.

            INPUT:

            - ``x`` -- an element of the lattice

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: I = L.moebius_algebra(QQ).I()
                sage: I[5]
                I[5]
            """
    idempotent = I

class QuantumMoebiusAlgebra(Parent, UniqueRepresentation):
    """
    The quantum Möbius algebra of a lattice.

    Let `L` be a lattice, and we define the *quantum Möbius algebra* `M_L(q)`
    as the algebra with basis `\\{ E_x \\mid x \\in L \\}` with
    multiplication given by

    .. MATH::

        E_x E_y = \\sum_{z \\geq a \\geq x \\vee y} \\mu_L(a, z)
        q^{\\operatorname{crk} a} E_z,

    where `\\mu_L` is the Möbius function of `L` and `\\operatorname{crk}`
    is the corank function (i.e., `\\operatorname{crk} a =
    \\operatorname{rank} L - \\operatorname{rank}` a). At `q = 1`, this
    reduces to the multiplication formula originally given by Solomon.
    """
    def __init__(self, L, q=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: L = posets.BooleanLattice(4)
            sage: M = L.quantum_moebius_algebra()
            sage: TestSuite(M).run() # long time

            sage: from sage.combinat.posets.moebius_algebra import QuantumMoebiusAlgebra
            sage: L = posets.Crown(2)
            sage: QuantumMoebiusAlgebra(L)
            Traceback (most recent call last):
            ...
            ValueError: L must be a lattice
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the `B`-basis).

        EXAMPLES::

            sage: L = posets.BooleanLattice(4)
            sage: M = L.quantum_moebius_algebra()
            sage: M.a_realization()
            Quantum Moebius algebra of Finite lattice containing 16 elements
             with q=q over Univariate Laurent Polynomial Ring in q
             over Integer Ring in the natural basis
        """
    def lattice(self):
        """
        Return the defining lattice of ``self``.

        EXAMPLES::

            sage: L = posets.BooleanLattice(4)
            sage: M = L.quantum_moebius_algebra()
            sage: M.lattice()
            Finite lattice containing 16 elements
            sage: M.lattice() == L
            True
        """
    class E(BasisAbstract):
        """
        The natural basis of a quantum Möbius algebra.

        Let `E_x` and `E_y` be basis elements of `M_L` for some lattice `L`.
        Multiplication is given by

        .. MATH::

            E_x E_y = \\sum_{z \\geq a \\geq x \\vee y} \\mu_L(a, z)
            q^{\\operatorname{crk} a} E_z,

        where `\\mu_L` is the Möbius function of `L` and `\\operatorname{crk}`
        is the corank function (i.e., `\\operatorname{crk} a =
        \\operatorname{rank} L - \\operatorname{rank}` a).
        """
        def __init__(self, M, prefix: str = 'E') -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: L = posets.BooleanLattice(4)
                sage: M = L.quantum_moebius_algebra()
                sage: TestSuite(M.E()).run() # long time
            """
        def product_on_basis(self, x, y):
            """
            Return the product of basis elements indexed by ``x`` and ``y``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: E = L.quantum_moebius_algebra().E()
                sage: E.product_on_basis(5, 14)
                E[15]
                sage: E.product_on_basis(2, 8)
                q^2*E[10] + (q-q^2)*E[11] + (q-q^2)*E[14] + (1-2*q+q^2)*E[15]
            """
        @cached_method
        def one(self):
            """
            Return the element ``1`` of ``self``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: E = L.quantum_moebius_algebra().E()
                sage: all(E.one() * b == b for b in E.basis())
                True
            """
    natural = E
    class C(BasisAbstract):
        """
        The characteristic basis of a quantum Möbius algebra.

        The characteristic basis `\\{ C_x \\mid x \\in L \\}` of `M_L`
        for some lattice `L` is defined by

        .. MATH::

            C_x = \\sum_{a \\geq x} P(F^x; q) E_a,

        where `F^x = \\{ y \\in L \\mid y \\geq x \\}` is the principal order
        filter of `x` and `P(F^x; q)` is the characteristic polynomial
        of the (sub)poset `F^x`.
        """
        def __init__(self, M, prefix: str = 'C') -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: L = posets.BooleanLattice(3)
                sage: M = L.quantum_moebius_algebra()
                sage: TestSuite(M.C()).run() # long time
            """
    characteristic_basis = C
    class KL(BasisAbstract):
        """
        The Kazhdan-Lusztig basis of a quantum Möbius algebra.

        The Kazhdan-Lusztig basis `\\{ B_x \\mid x \\in L \\}` of `M_L`
        for some lattice `L` is defined by

        .. MATH::

            B_x = \\sum_{y \\geq x} P_{x,y}(q) E_a,

        where `P_{x,y}(q)` is the Kazhdan-Lusztig polynomial of `L`,
        following the definition given in [EPW14]_.

        EXAMPLES:

        We construct some examples of Proposition 4.5 of [EPW14]_::

            sage: M = posets.BooleanLattice(4).quantum_moebius_algebra()
            sage: KL = M.KL()
            sage: KL[4] * KL[5]
            (q^2+q^3)*KL[5] + (q+2*q^2+q^3)*KL[7] + (q+2*q^2+q^3)*KL[13]
             + (1+3*q+3*q^2+q^3)*KL[15]
            sage: KL[4] * KL[15]
            (1+3*q+3*q^2+q^3)*KL[15]
            sage: KL[4] * KL[10]
            (q+3*q^2+3*q^3+q^4)*KL[14] + (1+4*q+6*q^2+4*q^3+q^4)*KL[15]
        """
        def __init__(self, M, prefix: str = 'KL') -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: L = posets.BooleanLattice(3)
                sage: M = L.quantum_moebius_algebra()
                sage: TestSuite(M.KL()).run() # long time
            """
    kazhdan_lusztig = KL

class MoebiusAlgebraBases(Category_realization_of_parent):
    """
    The category of bases of a Möbius algebra.

    INPUT:

    - ``base`` -- a Möbius algebra

    TESTS::

        sage: from sage.combinat.posets.moebius_algebra import MoebiusAlgebraBases
        sage: M = posets.BooleanLattice(4).moebius_algebra(QQ)
        sage: bases = MoebiusAlgebraBases(M)
        sage: M.E() in bases
        True
    """
    def super_categories(self):
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.posets.moebius_algebra import MoebiusAlgebraBases
            sage: M = posets.BooleanLattice(4).moebius_algebra(QQ)
            sage: bases = MoebiusAlgebraBases(M)
            sage: bases.super_categories()
            [Category of finite dimensional commutative algebras with basis over Rational Field,
             Category of realizations of Moebius algebra of Finite lattice
                containing 16 elements over Rational Field]
        """
    class ParentMethods:
        def product_on_basis(self, x, y):
            """
            Return the product of basis elements indexed by ``x`` and ``y``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: C = L.quantum_moebius_algebra().C()
                sage: C.product_on_basis(5, 14)
                q^3*C[15]
                sage: C.product_on_basis(2, 8)
                q^4*C[10]
            """
        @cached_method
        def one(self):
            """
            Return the element ``1`` of ``self``.

            EXAMPLES::

                sage: L = posets.BooleanLattice(4)
                sage: C = L.quantum_moebius_algebra().C()
                sage: all(C.one() * b == b for b in C.basis())
                True
            """
    class ElementMethods: ...
