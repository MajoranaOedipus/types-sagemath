from sage.arith.misc import factorial as factorial
from sage.categories.algebras import Algebras as Algebras
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.finite_dimensional_algebras_with_basis import FiniteDimensionalAlgebrasWithBasis as FiniteDimensionalAlgebrasWithBasis
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent, Realizations as Realizations
from sage.combinat.composition import Compositions as Compositions
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.integer_matrices import IntegerMatrices as IntegerMatrices
from sage.combinat.ncsf_qsym.ncsf import NonCommutativeSymmetricFunctions as NonCommutativeSymmetricFunctions
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.subset import SubsetsSorted as SubsetsSorted
from sage.combinat.symmetric_group_algebra import SymmetricGroupAlgebra as SymmetricGroupAlgebra
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DescentAlgebra(UniqueRepresentation, Parent):
    """
    Solomon's descent algebra.

    The descent algebra `\\Sigma_n` over a ring `R` is a subalgebra of the
    symmetric group algebra `R S_n`. (The product in the latter algebra
    is defined by `(pq)(i) = q(p(i))` for any two permutations `p` and
    `q` in `S_n` and every `i \\in \\{ 1, 2, \\ldots, n \\}`. The algebra
    `\\Sigma_n` inherits this product.)

    There are three bases currently implemented for `\\Sigma_n`:

    - the standard basis `D_S` of (sums of) descent classes, indexed by
      subsets `S` of `\\{1, 2, \\ldots, n-1\\}`,
    - the subset basis `B_p`, indexed by compositions `p` of `n`,
    - the idempotent basis `I_p`, indexed by compositions `p` of `n`,
      which is used to construct the mutually orthogonal idempotents
      of the symmetric group algebra.

    The idempotent basis is only defined when `R` is a `\\QQ`-algebra.

    We follow the notations and conventions in [GR1989]_, apart from the
    order of multiplication being different from the one used in that
    article. Schocker's exposition [Sch2004]_, in turn, uses the
    same order of multiplication as we are, but has different notations
    for the bases.

    INPUT:

    - ``R`` -- the base ring

    - ``n`` -- nonnegative integer

    REFERENCES:

    - [GR1989]_

    - [At1992]_

    - [MR1995]_

    - [Sch2004]_

    EXAMPLES::

        sage: DA = DescentAlgebra(QQ, 4)
        sage: D = DA.D(); D
        Descent algebra of 4 over Rational Field in the standard basis
        sage: B = DA.B(); B
        Descent algebra of 4 over Rational Field in the subset basis
        sage: I = DA.I(); I
        Descent algebra of 4 over Rational Field in the idempotent basis
        sage: basis_B = B.basis()
        sage: elt = basis_B[Composition([1,2,1])] + 4*basis_B[Composition([1,3])]; elt
        B[1, 2, 1] + 4*B[1, 3]
        sage: D(elt)
        5*D{} + 5*D{1} + D{1, 3} + D{3}
        sage: I(elt)
        7/6*I[1, 1, 1, 1] + 2*I[1, 1, 2] + 3*I[1, 2, 1] + 4*I[1, 3]


    As syntactic sugar, one can use the notation ``D[i,...,l]`` to
    construct elements of the basis; note that for the empty set one
    must use ``D[[]]`` due to Python's syntax::

        sage: D[[]] + D[2] + 2*D[1,2]
        D{} + 2*D{1, 2} + D{2}

    The same syntax works for the other bases::

        sage: I[1,2,1] + 3*I[4] + 2*I[3,1]
        I[1, 2, 1] + 2*I[3, 1] + 3*I[4]

    TESTS:

    We check that we can go back and forth between our bases::

        sage: DA = DescentAlgebra(QQ, 4)
        sage: D = DA.D()
        sage: B = DA.B()
        sage: I = DA.I()
        sage: all(D(B(b)) == b for b in D.basis())
        True
        sage: all(D(I(b)) == b for b in D.basis())
        True
        sage: all(B(D(b)) == b for b in B.basis())
        True
        sage: all(B(I(b)) == b for b in B.basis())
        True
        sage: all(I(D(b)) == b for b in I.basis())
        True
        sage: all(I(B(b)) == b for b in I.basis())
        True
    """
    def __init__(self, R, n) -> None:
        """
        EXAMPLES::

            sage: TestSuite(DescentAlgebra(QQ, 4)).run()

        TESTS::

            sage: B = DescentAlgebra(QQ, 4).B()
            sage: B.is_commutative()
            False
            sage: B = DescentAlgebra(QQ, 1).B()
            sage: B.is_commutative()
            True

            sage: B = DescentAlgebra(QQ, 4).B()
            sage: B in Fields()
            False
            sage: B = DescentAlgebra(QQ, 1).B()
            sage: B in Fields()
            True
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the `B`-basis).

        EXAMPLES::

            sage: DA = DescentAlgebra(QQ, 4)
            sage: DA.a_realization()
            Descent algebra of 4 over Rational Field in the subset basis
        """
    class D(CombinatorialFreeModule, BindableClass):
        """
        The standard basis of a descent algebra.

        This basis is indexed by `S \\subseteq \\{1, 2, \\ldots, n-1\\}`,
        and the basis vector indexed by `S` is the sum of all permutations,
        taken in the symmetric group algebra `R S_n`, whose descent set is `S`.
        We denote this basis vector by `D_S`.

        Occasionally this basis appears in literature but indexed by
        compositions of `n` rather than subsets of
        `\\{1, 2, \\ldots, n-1\\}`. The equivalence between these two
        indexings is owed to the bijection from the power set of
        `\\{1, 2, \\ldots, n-1\\}` to the set of all compositions of `n`
        which sends every subset `\\{i_1, i_2, \\ldots, i_k\\}` of
        `\\{1, 2, \\ldots, n-1\\}` (with `i_1 < i_2 < \\cdots < i_k`) to
        the composition `(i_1, i_2-i_1, \\ldots, i_k-i_{k-1}, n-i_k)`.

        The basis element corresponding to a composition `p` (or to
        the subset of `\\{1, 2, \\ldots, n-1\\}`) is denoted `\\Delta^p`
        in [Sch2004]_.

        EXAMPLES::

            sage: DA = DescentAlgebra(QQ, 4)
            sage: D = DA.D()
            sage: list(D.basis())
            [D{}, D{1}, D{2}, D{3}, D{1, 2}, D{1, 3}, D{2, 3}, D{1, 2, 3}]

            sage: DA = DescentAlgebra(QQ, 0)
            sage: D = DA.D()
            sage: list(D.basis())
            [D{}]
        """
        def __init__(self, alg, prefix: str = 'D') -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: TestSuite(DescentAlgebra(QQ, 4).D()).run()
            """
        def product_on_basis(self, S, T):
            """
            Return `D_S D_T`, where `S` and `T` are subsets of `[n-1]`.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: D = DA.D()
                sage: D.product_on_basis((1, 3), (2,))
                D{} + D{1} + D{1, 2} + 2*D{1, 2, 3} + D{1, 3} + D{2} + D{2, 3} + D{3}
            """
        @cached_method
        def one_basis(self) -> tuple:
            """
            Return the identity element, as per
            ``AlgebrasWithBasis.ParentMethods.one_basis``.

            EXAMPLES::

                sage: DescentAlgebra(QQ, 4).D().one_basis()
                ()
                sage: DescentAlgebra(QQ, 0).D().one_basis()
                ()

                sage: all( U * DescentAlgebra(QQ, 3).D().one() == U
                ....:      for U in DescentAlgebra(QQ, 3).D().basis() )
                True
            """
        @cached_method
        def to_B_basis(self, S):
            """
            Return `D_S` as a linear combination of `B_p`-basis elements.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: D = DA.D()
                sage: B = DA.B()
                sage: list(map(B, D.basis()))  # indirect doctest
                [B[4],
                 B[1, 3] - B[4],
                 B[2, 2] - B[4],
                 B[3, 1] - B[4],
                 B[1, 1, 2] - B[1, 3] - B[2, 2] + B[4],
                 B[1, 2, 1] - B[1, 3] - B[3, 1] + B[4],
                 B[2, 1, 1] - B[2, 2] - B[3, 1] + B[4],
                 B[1, 1, 1, 1] - B[1, 1, 2] - B[1, 2, 1] + B[1, 3]
                  - B[2, 1, 1] + B[2, 2] + B[3, 1] - B[4]]
            """
        def to_symmetric_group_algebra_on_basis(self, S):
            """
            Return `D_S` as a linear combination of basis elements in the
            symmetric group algebra.

            EXAMPLES::

                sage: D = DescentAlgebra(QQ, 4).D()
                sage: [D.to_symmetric_group_algebra_on_basis(tuple(b))
                ....:  for b in Subsets(3)]
                [[1, 2, 3, 4],
                 [2, 1, 3, 4] + [3, 1, 2, 4] + [4, 1, 2, 3],
                 [1, 3, 2, 4] + [1, 4, 2, 3] + [2, 3, 1, 4]
                  + [2, 4, 1, 3] + [3, 4, 1, 2],
                 [1, 2, 4, 3] + [1, 3, 4, 2] + [2, 3, 4, 1],
                 [3, 2, 1, 4] + [4, 2, 1, 3] + [4, 3, 1, 2],
                 [2, 1, 4, 3] + [3, 1, 4, 2] + [3, 2, 4, 1]
                  + [4, 1, 3, 2] + [4, 2, 3, 1],
                 [1, 4, 3, 2] + [2, 4, 3, 1] + [3, 4, 2, 1],
                 [4, 3, 2, 1]]
            """
        def __getitem__(self, S):
            """
            Return the basis element indexed by ``S``.

            INPUT:

            - ``S`` -- a subset of `[n-1]`

            EXAMPLES::

                sage: D = DescentAlgebra(QQ, 4).D()
                sage: D[3]
                D{3}
                sage: D[1, 3]
                D{1, 3}
                sage: D[[]]
                D{}

            TESTS::

                sage: D = DescentAlgebra(QQ, 0).D()
                sage: D[[]]
                D{}
            """
    standard = D
    class B(CombinatorialFreeModule, BindableClass):
        '''
        The subset basis of a descent algebra (indexed by compositions).

        The subset basis `(B_S)_{S \\subseteq \\{1, 2, \\ldots, n-1\\}}` of
        `\\Sigma_n` is formed by

        .. MATH::

            B_S = \\sum_{T \\subseteq S} D_T,

        where `(D_S)_{S \\subseteq \\{1, 2, \\ldots, n-1\\}}` is the
        :class:`standard basis <DescentAlgebra.D>`. However it is more
        natural to index the subset basis by compositions
        of `n` under the bijection `\\{i_1, i_2, \\ldots, i_k\\} \\mapsto
        (i_1, i_2 - i_1, i_3 - i_2, \\ldots, i_k - i_{k-1}, n - i_k)`
        (where `i_1 < i_2 < \\cdots < i_k`), which is what Sage uses to
        index the basis.

        The basis element `B_p` is denoted `\\Xi^p` in [Sch2004]_.

        By using compositions of `n`, the product `B_p B_q` becomes a
        sum over the nonnegative-integer matrices `M` with row sum `p`
        and column sum `q`. The summand corresponding to `M` is `B_c`,
        where `c` is the composition obtained by reading `M` row-by-row
        from left-to-right and top-to-bottom and removing all zeroes.
        This multiplication rule is commonly called "Solomon\'s Mackey
        formula".

        EXAMPLES::

            sage: DA = DescentAlgebra(QQ, 4)
            sage: B = DA.B()
            sage: list(B.basis())
            [B[1, 1, 1, 1], B[1, 1, 2], B[1, 2, 1], B[1, 3],
             B[2, 1, 1], B[2, 2], B[3, 1], B[4]]
        '''
        def __init__(self, alg, prefix: str = 'B') -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: TestSuite(DescentAlgebra(QQ, 4).B()).run()
            """
        def product_on_basis(self, p, q):
            """
            Return `B_p B_q`, where `p` and `q` are compositions of `n`.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: B = DA.B()
                sage: p = Composition([1,2,1])
                sage: q = Composition([3,1])
                sage: B.product_on_basis(p, q)
                B[1, 1, 1, 1] + 2*B[1, 2, 1]
            """
        @cached_method
        def one_basis(self):
            """
            Return the identity element which is the composition `[n]`, as per
            ``AlgebrasWithBasis.ParentMethods.one_basis``.

            EXAMPLES::

                sage: DescentAlgebra(QQ, 4).B().one_basis()
                [4]
                sage: DescentAlgebra(QQ, 0).B().one_basis()
                []

                sage: all( U * DescentAlgebra(QQ, 3).B().one() == U
                ....:      for U in DescentAlgebra(QQ, 3).B().basis() )
                True
            """
        @cached_method
        def to_I_basis(self, p):
            """
            Return `B_p` as a linear combination of `I`-basis elements.

            This is done using the formula

            .. MATH::

                B_p = \\sum_{q \\leq p} \\frac{1}{\\mathbf{k}!(q,p)} I_q,

            where `\\leq` is the refinement order and `\\mathbf{k}!(q,p)` is
            defined as follows: When `q \\leq p`, we can write `q` as a
            concatenation `q_{(1)} q_{(2)} \\cdots q_{(k)}` with each `q_{(i)}`
            being a composition of the `i`-th entry of `p`, and then
            we set `\\mathbf{k}!(q,p)` to be
            `l(q_{(1)})! l(q_{(2)})! \\cdots l(q_{(k)})!`, where `l(r)`
            denotes the number of parts of any composition `r`.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: B = DA.B()
                sage: I = DA.I()
                sage: list(map(I, B.basis()))  # indirect doctest
                [I[1, 1, 1, 1],
                 1/2*I[1, 1, 1, 1] + I[1, 1, 2],
                 1/2*I[1, 1, 1, 1] + I[1, 2, 1],
                 1/6*I[1, 1, 1, 1] + 1/2*I[1, 1, 2] + 1/2*I[1, 2, 1] + I[1, 3],
                 1/2*I[1, 1, 1, 1] + I[2, 1, 1],
                 1/4*I[1, 1, 1, 1] + 1/2*I[1, 1, 2] + 1/2*I[2, 1, 1] + I[2, 2],
                 1/6*I[1, 1, 1, 1] + 1/2*I[1, 2, 1] + 1/2*I[2, 1, 1] + I[3, 1],
                 1/24*I[1, 1, 1, 1] + 1/6*I[1, 1, 2] + 1/6*I[1, 2, 1]
                  + 1/2*I[1, 3] + 1/6*I[2, 1, 1] + 1/2*I[2, 2] + 1/2*I[3, 1] + I[4]]
            """
        @cached_method
        def to_D_basis(self, p):
            """
            Return `B_p` as a linear combination of `D`-basis elements.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: B = DA.B()
                sage: D = DA.D()
                sage: list(map(D, B.basis()))  # indirect doctest
                [D{} + D{1} + D{1, 2} + D{1, 2, 3}
                  + D{1, 3} + D{2} + D{2, 3} + D{3},
                 D{} + D{1} + D{1, 2} + D{2},
                 D{} + D{1} + D{1, 3} + D{3},
                 D{} + D{1},
                 D{} + D{2} + D{2, 3} + D{3},
                 D{} + D{2},
                 D{} + D{3},
                 D{}]

            TESTS:

            Check to make sure the empty case is handled correctly::

                sage: DA = DescentAlgebra(QQ, 0)
                sage: B = DA.B()
                sage: D = DA.D()
                sage: list(map(D, B.basis()))
                [D{}]
            """
        def to_nsym(self, p):
            """
            Return `B_p` as an element in `NSym`, the non-commutative
            symmetric functions.

            This maps `B_p` to `S_p` where `S` denotes the Complete basis of
            `NSym`.

            EXAMPLES::

                sage: B = DescentAlgebra(QQ, 4).B()
                sage: S = NonCommutativeSymmetricFunctions(QQ).Complete()
                sage: list(map(S, B.basis()))  # indirect doctest
                [S[1, 1, 1, 1],
                 S[1, 1, 2],
                 S[1, 2, 1],
                 S[1, 3],
                 S[2, 1, 1],
                 S[2, 2],
                 S[3, 1],
                 S[4]]
            """
    subset = B
    class I(CombinatorialFreeModule, BindableClass):
        """
        The idempotent basis of a descent algebra.

        The idempotent basis `(I_p)_{p \\models n}` is a basis for `\\Sigma_n`
        whenever the ground ring is a `\\QQ`-algebra. One way to compute it
        is using the formula (Theorem 3.3 in [GR1989]_)

        .. MATH::

            I_p = \\sum_{q \\leq p}
            \\frac{(-1)^{l(q)-l(p)}}{\\mathbf{k}(q,p)} B_q,

        where `\\leq` is the refinement order and `l(r)` denotes the number
        of parts of any composition `r`, and where `\\mathbf{k}(q,p)` is
        defined as follows: When `q \\leq p`, we can write `q` as a
        concatenation `q_{(1)} q_{(2)} \\cdots q_{(k)}` with each `q_{(i)}`
        being a composition of the `i`-th entry of `p`, and then
        we set `\\mathbf{k}(q,p)` to be the product
        `l(q_{(1)}) l(q_{(2)}) \\cdots l(q_{(k)})`.

        Let `\\lambda(p)` denote the partition obtained from a composition
        `p` by sorting. This basis is called the idempotent basis since for
        any `q` such that `\\lambda(p) = \\lambda(q)`, we have:

        .. MATH::

            I_p I_q = s(\\lambda) I_p

        where `\\lambda` denotes `\\lambda(p) = \\lambda(q)`, and where
        `s(\\lambda)` is the stabilizer of `\\lambda` in `S_n`. (This is
        part of Theorem 4.2 in [GR1989]_.)

        It is also straightforward to compute the idempotents `E_{\\lambda}`
        for the symmetric group algebra by the formula
        (Theorem 3.2 in [GR1989]_):

        .. MATH::

            E_{\\lambda} = \\frac{1}{k!} \\sum_{\\lambda(p) = \\lambda} I_p.

        .. NOTE::

            The basis elements are not orthogonal idempotents.

        EXAMPLES::

            sage: DA = DescentAlgebra(QQ, 4)
            sage: I = DA.I()
            sage: list(I.basis())
            [I[1, 1, 1, 1], I[1, 1, 2], I[1, 2, 1], I[1, 3], I[2, 1, 1], I[2, 2], I[3, 1], I[4]]
        """
        def __init__(self, alg, prefix: str = 'I') -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: TestSuite(DescentAlgebra(QQ, 4).B()).run()
            """
        def product_on_basis(self, p, q):
            """
            Return `I_p I_q`, where `p` and `q` are compositions of `n`.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: I = DA.I()
                sage: p = Composition([1,2,1])
                sage: q = Composition([3,1])
                sage: I.product_on_basis(p, q)
                0
                sage: I.product_on_basis(p, p)
                2*I[1, 2, 1]
            """
        @cached_method
        def one(self):
            """
            Return the identity element, which is `B_{[n]}`, in the `I` basis.

            EXAMPLES::

                sage: DescentAlgebra(QQ, 4).I().one()
                1/24*I[1, 1, 1, 1] + 1/6*I[1, 1, 2] + 1/6*I[1, 2, 1]
                 + 1/2*I[1, 3] + 1/6*I[2, 1, 1] + 1/2*I[2, 2]
                 + 1/2*I[3, 1] + I[4]
                sage: DescentAlgebra(QQ, 0).I().one()
                I[]

            TESTS::

                sage: all( U * DescentAlgebra(QQ, 3).I().one() == U
                ....:      for U in DescentAlgebra(QQ, 3).I().basis() )
                True
            """
        def one_basis(self) -> None:
            """
            The element `1` is not (generally) a basis vector in the `I`
            basis, thus this raises a :exc:`TypeError`.

            EXAMPLES::

                sage: DescentAlgebra(QQ, 4).I().one_basis()
                Traceback (most recent call last):
                ...
                TypeError: 1 is not a basis element in the I basis
            """
        @cached_method
        def to_B_basis(self, p):
            """
            Return `I_p` as a linear combination of `B`-basis elements.

            This is computed using the formula (Theorem 3.3 in [GR1989]_)

            .. MATH::

                I_p = \\sum_{q \\leq p}
                \\frac{(-1)^{l(q)-l(p)}}{\\mathbf{k}(q,p)} B_q,

            where `\\leq` is the refinement order and `l(r)` denotes the number
            of parts of any composition `r`, and where `\\mathbf{k}(q,p)` is
            defined as follows: When `q \\leq p`, we can write `q` as a
            concatenation `q_{(1)} q_{(2)} \\cdots q_{(k)}` with each `q_{(i)}`
            being a composition of the `i`-th entry of `p`, and then
            we set `\\mathbf{k}(q,p)` to be
            `l(q_{(1)}) l(q_{(2)}) \\cdots l(q_{(k)})`.

            EXAMPLES::

                sage: DA = DescentAlgebra(QQ, 4)
                sage: B = DA.B()
                sage: I = DA.I()
                sage: list(map(B, I.basis()))  # indirect doctest
                [B[1, 1, 1, 1],
                 -1/2*B[1, 1, 1, 1] + B[1, 1, 2],
                 -1/2*B[1, 1, 1, 1] + B[1, 2, 1],
                 1/3*B[1, 1, 1, 1] - 1/2*B[1, 1, 2] - 1/2*B[1, 2, 1] + B[1, 3],
                 -1/2*B[1, 1, 1, 1] + B[2, 1, 1],
                 1/4*B[1, 1, 1, 1] - 1/2*B[1, 1, 2] - 1/2*B[2, 1, 1] + B[2, 2],
                 1/3*B[1, 1, 1, 1] - 1/2*B[1, 2, 1] - 1/2*B[2, 1, 1] + B[3, 1],
                 -1/4*B[1, 1, 1, 1] + 1/3*B[1, 1, 2] + 1/3*B[1, 2, 1]
                  - 1/2*B[1, 3] + 1/3*B[2, 1, 1] - 1/2*B[2, 2]
                  - 1/2*B[3, 1] + B[4]]
            """
        def idempotent(self, la):
            """
            Return the idempotent corresponding to the partition ``la``
            of `n`.

            EXAMPLES::

                sage: I = DescentAlgebra(QQ, 4).I()
                sage: E = I.idempotent([3,1]); E
                1/2*I[1, 3] + 1/2*I[3, 1]
                sage: E*E == E
                True
                sage: E2 = I.idempotent([2,1,1]); E2
                1/6*I[1, 1, 2] + 1/6*I[1, 2, 1] + 1/6*I[2, 1, 1]
                sage: E2*E2 == E2
                True
                sage: E*E2 == I.zero()
                True
            """
    idempotent = I

class DescentAlgebraBases(Category_realization_of_parent):
    """
    The category of bases of a descent algebra.
    """
    def __init__(self, base) -> None:
        """
        Initialize the bases of a descent algebra.

        INPUT:

        - ``base`` -- a descent algebra

        TESTS::

            sage: from sage.combinat.descent_algebra import DescentAlgebraBases
            sage: DA = DescentAlgebra(QQ, 4)
            sage: bases = DescentAlgebraBases(DA)
            sage: DA.B() in bases
            True
        """
    def super_categories(self) -> list:
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.descent_algebra import DescentAlgebraBases
            sage: DA = DescentAlgebra(QQ, 4)
            sage: bases = DescentAlgebraBases(DA)
            sage: bases.super_categories()
            [Category of finite dimensional algebras with basis over Rational Field,
             Category of realizations of Descent algebra of 4 over Rational Field]
        """
    class ParentMethods:
        def __getitem__(self, p):
            """
            Return the basis element indexed by ``p``.

            INPUT:

            - ``p`` -- a composition

            EXAMPLES::

                sage: B = DescentAlgebra(QQ, 4).B()
                sage: B[Composition([4])]
                B[4]
                sage: B[1,2,1]
                B[1, 2, 1]
                sage: B[4]
                B[4]
                sage: B[[3,1]]
                B[3, 1]
            """
        @lazy_attribute
        def to_symmetric_group_algebra(self):
            """
            Morphism from ``self`` to the symmetric group algebra.

            EXAMPLES::

                sage: D = DescentAlgebra(QQ, 4).D()
                sage: D.to_symmetric_group_algebra(D[1,3])
                [2, 1, 4, 3] + [3, 1, 4, 2] + [3, 2, 4, 1] + [4, 1, 3, 2] + [4, 2, 3, 1]
                sage: B = DescentAlgebra(QQ, 4).B()
                sage: B.to_symmetric_group_algebra(B[1,2,1])
                [1, 2, 3, 4] + [1, 2, 4, 3] + [1, 3, 4, 2] + [2, 1, 3, 4]
                 + [2, 1, 4, 3] + [2, 3, 4, 1] + [3, 1, 2, 4] + [3, 1, 4, 2]
                 + [3, 2, 4, 1] + [4, 1, 2, 3] + [4, 1, 3, 2] + [4, 2, 3, 1]
            """
        def to_symmetric_group_algebra_on_basis(self, S):
            """
            Return the basis element index by ``S`` as a linear combination
            of basis elements in the symmetric group algebra.

            EXAMPLES::

                sage: B = DescentAlgebra(QQ, 3).B()
                sage: [B.to_symmetric_group_algebra_on_basis(c)
                ....:  for c in Compositions(3)]
                [[1, 2, 3] + [1, 3, 2] + [2, 1, 3]
                  + [2, 3, 1] + [3, 1, 2] + [3, 2, 1],
                 [1, 2, 3] + [2, 1, 3] + [3, 1, 2],
                 [1, 2, 3] + [1, 3, 2] + [2, 3, 1],
                 [1, 2, 3]]
                sage: I = DescentAlgebra(QQ, 3).I()
                sage: [I.to_symmetric_group_algebra_on_basis(c)
                ....:  for c in Compositions(3)]
                [[1, 2, 3] + [1, 3, 2] + [2, 1, 3] + [2, 3, 1]
                  + [3, 1, 2] + [3, 2, 1],
                 1/2*[1, 2, 3] - 1/2*[1, 3, 2] + 1/2*[2, 1, 3]
                  - 1/2*[2, 3, 1] + 1/2*[3, 1, 2] - 1/2*[3, 2, 1],
                 1/2*[1, 2, 3] + 1/2*[1, 3, 2] - 1/2*[2, 1, 3]
                  + 1/2*[2, 3, 1] - 1/2*[3, 1, 2] - 1/2*[3, 2, 1],
                 1/3*[1, 2, 3] - 1/6*[1, 3, 2] - 1/6*[2, 1, 3]
                  - 1/6*[2, 3, 1] - 1/6*[3, 1, 2] + 1/3*[3, 2, 1]]
            """
    class ElementMethods:
        def to_symmetric_group_algebra(self):
            """
            Return ``self`` in the symmetric group algebra.

            EXAMPLES::

                sage: B = DescentAlgebra(QQ, 4).B()
                sage: B[1,3].to_symmetric_group_algebra()
                [1, 2, 3, 4] + [2, 1, 3, 4] + [3, 1, 2, 4] + [4, 1, 2, 3]
                sage: I = DescentAlgebra(QQ, 4).I()
                sage: elt = I(B[1,3])
                sage: elt.to_symmetric_group_algebra()
                [1, 2, 3, 4] + [2, 1, 3, 4] + [3, 1, 2, 4] + [4, 1, 2, 3]
            """
