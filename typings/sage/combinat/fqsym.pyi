from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.combinat.symmetric_group_algebra import SymmetricGroupAlgebra as SymmetricGroupAlgebra
from sage.combinat.words.word import Word as Word
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FQSymBasis_abstract(CombinatorialFreeModule, BindableClass):
    """
    Abstract base class for bases of FQSym.

    This must define two attributes:

    - ``_prefix`` -- the basis prefix
    - ``_basis_name`` -- the name of the basis and must match one
      of the names that the basis can be constructed from FQSym
    """
    def __init__(self, alg) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: TestSuite(algebras.FQSym(QQ).F()).run()  # long time
        """

class FreeQuasisymmetricFunctions(UniqueRepresentation, Parent):
    '''
    The free quasi-symmetric functions.

    The Hopf algebra `FQSym` of free quasi-symmetric functions
    over a commutative ring `R` is the free `R`-module with basis
    indexed by all permutations (i.e., the indexing set is
    the disjoint union of all symmetric groups).
    Its product is determined by the shifted shuffles of two
    permutations, whereas its coproduct is given by splitting
    a permutation (regarded as a word) into two (at every
    possible point) and standardizing the two pieces.
    This Hopf algebra was introduced in [MR]_.
    See [GriRei18]_ (Chapter 8) for a treatment using modern
    notations.

    In more detail:
    For each `n \\geq 0`, consider the symmetric group `S_n`.
    Let `S` be the disjoint union of the `S_n` over all
    `n \\geq 0`.
    Then, `FQSym` is the free `R`-module with basis
    `(F_w)_{w \\in S}`.
    This `R`-module is graded, with the `n`-th graded
    component being spanned by all `F_w` for `w \\in S_n`.
    A multiplication is defined on `FQSym` as follows:
    For any two permutations `u \\in S_k` and `v \\in S_l`,
    we set

    .. MATH::

        F_u F_v = \\sum F_w ,

    where the sum is over all shuffles of `u` with `v[k]`.
    Here, the permutations `u` and `v` are regarded as words
    (by writing them in one-line notation), and `v[k]` means
    the word obtained from `v` by increasing each letter by
    `k` (for example, `(1,4,2,3)[5] = (6,9,7,8)`); and the
    shuffles `w` are translated back into permutations.
    This defines an associative multiplication on `FQSym`;
    its unity is `F_e`, where `e` is the identity
    permutation in `S_0`.

    In Section 1.3 of [AguSot05]_, Aguiar and Sottile construct a
    different basis of `FQSym`. Their basis, called the
    *monomial basis* and denoted by `(\\mathcal{M}_u)`,
    is also indexed by permutations. It is connected to the
    above F-basis by the relation

    .. MATH::

        F_u = \\sum_v \\mathcal{M}_v ,

    where the sum ranges over all permutations `v` such that each
    inversion of `u` is an inversion of `v`. (An *inversion* of a
    permutation `w` means a pair `(i, j)` of positions satisfying
    `i < j` and `w(i) > w(j)`.) The above relation yields a
    unitriangular change-of-basis matrix, and thus can be used to
    compute the `\\mathcal{M}_u` by Mobius inversion.

    Another classical basis of `FQSym` is `(G_w)_{w \\in S}`,
    where `G_w = F_{w^{-1}}`.
    This is just a relabeling of the basis `(F_w)_{w \\in S}`,
    but is a more natural choice from some viewpoints.

    The algebra `FQSym` is often identified with ("realized as") a
    subring of the ring of all bounded-degree noncommutative power
    series in countably many indeterminates (i.e., elements in
    `R \\langle \\langle x_1, x_2, x_3, \\ldots \\rangle \\rangle` of bounded
    degree). Namely, consider words over the alphabet `\\{1, 2, 3, \\ldots\\}`;
    every noncommutative power series is an infinite `R`-linear
    combination of these words.
    Consider the `R`-linear map that sends each `G_u` to the sum of
    all words whose standardization (also known as "standard
    permutation"; see
    :meth:`~sage.combinat.words.finite_word.FiniteWord_class.standard_permutation`)
    is `u`. This map is an injective `R`-algebra homomorphism, and
    thus embeds `FQSym` into the latter ring.

    As an associative algebra, `FQSym` has the richer structure
    of a dendriform algebra. This means that the associative
    product ``*`` is decomposed as a sum of two binary operations

    .. MATH::

        x y = x \\succ y + x \\prec y

    that satisfy the axioms:

    .. MATH::

        (x \\succ y) \\prec z = x \\succ (y \\prec z),

    .. MATH::

        (x \\prec y) \\prec z = x \\prec (y z),

    .. MATH::

        (x y) \\succ z = x \\succ (y \\succ z).

    These two binary operations are defined similarly to the
    (associative) product above: We set

    .. MATH::

        F_u \\prec F_v = \\sum F_w ,

    where the sum is now over all shuffles of `u` with `v[k]`
    whose first letter is taken from `u` (rather than from
    `v[k]`). Similarly,

    .. MATH::

        F_u \\succ F_v = \\sum F_w ,

    where the sum is over all remaining shuffles of `u` with
    `v[k]`.

    .. TODO::

        Decide what `1 \\prec 1` and `1 \\succ 1` are.

    .. NOTE::

        The usual binary operator ``*`` is used for the
        associative product.

    EXAMPLES::

        sage: F = algebras.FQSym(ZZ).F()
        sage: x,y,z = F([1]), F([1,2]), F([1,3,2])
        sage: (x * y) * z
        F[1, 2, 3, 4, 6, 5] + ...

    The product of `FQSym` is associative::

        sage: x * (y * z) == (x * y) * z
        True

    The associative product decomposes into two parts::

        sage: x * y == F.prec(x, y) + F.succ(x, y)
        True

    The axioms of a dendriform algebra hold::

        sage: F.prec(F.succ(x, y), z) == F.succ(x, F.prec(y, z))
        True
        sage: F.prec(F.prec(x, y), z) == F.prec(x, y * z)
        True
        sage: F.succ(x * y, z) == F.succ(x, F.succ(y, z))
        True

    `FQSym` is also known as the Malvenuto-Reutenauer algebra::

        sage: algebras.MalvenutoReutenauer(ZZ)
        Free Quasi-symmetric functions over Integer Ring

    REFERENCES:

    - [MR]_
    - [LR1998]_
    - [GriRei18]_
    '''
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = algebras.FQSym(QQ); A
            Free Quasi-symmetric functions over Rational Field
            sage: TestSuite(A).run()  # long time (3s)

            sage: F = algebras.FQSym(QQ)
            sage: TestSuite(F).run() # long time (3s)

            sage: F = algebras.FQSym(ZZ).F()
            sage: F.is_commutative()
            False
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the F-basis).

        EXAMPLES::

            sage: FQSym = algebras.FQSym(QQ)
            sage: FQSym.a_realization()
            Free Quasi-symmetric functions over Rational Field in the F basis
        """
    class F(FQSymBasis_abstract):
        """
        The F-basis of `FQSym`.

        This is the basis `(F_w)`, with `w` ranging over all
        permutations. See the documentation of
        :class:`FreeQuasisymmetricFunctions` for details.

        EXAMPLES::

            sage: FQSym = algebras.FQSym(QQ)
            sage: FQSym.F()
            Free Quasi-symmetric functions over Rational Field in the F basis
        """
        def __getitem__(self, r):
            """
            The default implementation of ``__getitem__`` interprets
            the input as a tuple, which in case of permutations
            is interpreted as cycle notation, even though the input
            looks like a one-line notation.
            We override this method to amend this.

            EXAMPLES::

                sage: F = algebras.FQSym(QQ).F()
                sage: F[3, 2, 1]
                F[3, 2, 1]
                sage: F[1]
                F[1]
            """
        def degree_on_basis(self, t):
            """
            Return the degree of a permutation in
            the algebra of free quasi-symmetric functions.

            This is the size of the permutation (i.e., the `n`
            for which the permutation belongs to `S_n`).

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: u = Permutation([2,1])
                sage: A.degree_on_basis(u)
                2
            """
        def product_on_basis(self, x, y):
            """
            Return the `*` associative product of two permutations.

            This is the shifted shuffle of `x` and `y`.

            .. SEEALSO::

                :meth:`succ_product_on_basis`, :meth:`prec_product_on_basis`

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: x = Permutation([1])
                sage: A.product_on_basis(x, x)
                F[1, 2] + F[2, 1]
            """
        def succ_product_on_basis(self, x, y):
            """
            Return the `\\succ` product of two permutations.

            This is the shifted shuffle of `x` and `y` with the additional
            condition that the first letter of the result comes from `y`.

            The usual symbol for this operation is `\\succ`.

            .. SEEALSO::

                - :meth:`product_on_basis`, :meth:`prec_product_on_basis`

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: x = Permutation([1,2])
                sage: A.succ_product_on_basis(x, x)
                F[3, 1, 2, 4] + F[3, 1, 4, 2] + F[3, 4, 1, 2]
                sage: y = Permutation([])
                sage: A.succ_product_on_basis(x, y) == 0
                True
                sage: A.succ_product_on_basis(y, x) == A(x)
                True

            TESTS::

                sage: u = A.one().support()[0] # this is F[]
                sage: A.succ_product_on_basis(x, u)
                0
                sage: A.succ_product_on_basis(u, x)
                F[1, 2]
                sage: A.succ_product_on_basis(u, u)
                Traceback (most recent call last):
                ...
                ValueError: products | < | and | > | are not defined
            """
        def prec_product_on_basis(self, x, y):
            """
            Return the `\\prec` product of two permutations.

            This is the shifted shuffle of `x` and `y` with the additional
            condition that the first letter of the result comes from `x`.

            The usual symbol for this operation is `\\prec`.

            .. SEEALSO::

                :meth:`product_on_basis`, :meth:`succ_product_on_basis`

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: x = Permutation([1,2])
                sage: A.prec_product_on_basis(x, x)
                F[1, 2, 3, 4] + F[1, 3, 2, 4] + F[1, 3, 4, 2]
                sage: y = Permutation([])
                sage: A.prec_product_on_basis(x, y) == A(x)
                True
                sage: A.prec_product_on_basis(y, x) == 0
                True

            TESTS::

                sage: u = A.one().support()[0] # this is F[]
                sage: A.prec_product_on_basis(x, u)
                F[1, 2]
                sage: A.prec_product_on_basis(u, x)
                0
                sage: A.prec_product_on_basis(u, u)
                Traceback (most recent call last):
                ...
                ValueError: products | < | and | > | are not defined
            """
        def coproduct_on_basis(self, x):
            """
            Return the coproduct of `F_{\\sigma}` for `\\sigma` a permutation
            (here, `\\sigma` is ``x``).

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: x = A([1])
                sage: ascii_art(A.coproduct(A.one()))  # indirect doctest
                1 # 1

                sage: ascii_art(A.coproduct(x))  # indirect doctest
                1 # F    + F    # 1
                     [1]    [1]

                sage: A = algebras.FQSym(QQ).F()
                sage: x, y, z = A([1]), A([2,1]), A([3,2,1])
                sage: A.coproduct(z)
                F[] # F[3, 2, 1] + F[1] # F[2, 1] + F[2, 1] # F[1]
                + F[3, 2, 1] # F[]
            """
        class Element(FQSymBasis_abstract.Element):
            def to_symmetric_group_algebra(self, n=None):
                """
                Return the element of a symmetric group algebra
                corresponding to the element ``self`` of `FQSym`.

                INPUT:

                - ``n`` -- integer (default: the maximal degree of ``self``);
                  the rank of the target symmetric group algebra

                EXAMPLES::

                    sage: A = algebras.FQSym(QQ).F()
                    sage: x = A([1,3,2,4]) + 5/2 * A([1,2,4,3])
                    sage: x.to_symmetric_group_algebra()
                    5/2*[1, 2, 4, 3] + [1, 3, 2, 4]
                    sage: x.to_symmetric_group_algebra(n=7)
                    5/2*[1, 2, 4, 3, 5, 6, 7] + [1, 3, 2, 4, 5, 6, 7]
                    sage: a = A.zero().to_symmetric_group_algebra(); a
                    0
                    sage: parent(a)
                    Symmetric group algebra of order 0 over Rational Field

                    sage: y = A([1,3,2,4]) + 5/2 * A([2,1])
                    sage: y.to_symmetric_group_algebra()
                    [1, 3, 2, 4] + 5/2*[2, 1, 3, 4]
                    sage: y.to_symmetric_group_algebra(6)
                    [1, 3, 2, 4, 5, 6] + 5/2*[2, 1, 3, 4, 5, 6]
                """
    class G(FQSymBasis_abstract):
        """
        The G-basis of `FQSym`.

        This is the basis `(G_w)`, with `w` ranging over all
        permutations. See the documentation of
        :class:`FreeQuasisymmetricFunctions` for details.

        EXAMPLES::

            sage: FQSym = algebras.FQSym(QQ)
            sage: G = FQSym.G(); G
            Free Quasi-symmetric functions over Rational Field in the G basis

            sage: G([3, 1, 2]).coproduct()
            G[] # G[3, 1, 2] + G[1] # G[2, 1] + G[1, 2] # G[1]
             + G[3, 1, 2] # G[]

            sage: G([3, 1, 2]) * G([2, 1])
            G[3, 1, 2, 5, 4] + G[4, 1, 2, 5, 3] + G[4, 1, 3, 5, 2]
             + G[4, 2, 3, 5, 1] + G[5, 1, 2, 4, 3] + G[5, 1, 3, 4, 2]
             + G[5, 1, 4, 3, 2] + G[5, 2, 3, 4, 1] + G[5, 2, 4, 3, 1]
             + G[5, 3, 4, 2, 1]
        """
        def __getitem__(self, r):
            """
            The default implementation of ``__getitem__`` interprets
            the input as a tuple, which in case of permutations
            is interpreted as cycle notation, even though the input
            looks like a one-line notation.
            We override this method to amend this.

            EXAMPLES::

                sage: G = algebras.FQSym(QQ).G()
                sage: G[3, 2, 1]
                G[3, 2, 1]
                sage: G[1]
                G[1]
            """
        def degree_on_basis(self, t):
            """
            Return the degree of a permutation in
            the algebra of free quasi-symmetric functions.

            This is the size of the permutation (i.e., the `n`
            for which the permutation belongs to `S_n`).

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).G()
                sage: u = Permutation([2,1])
                sage: A.degree_on_basis(u)
                2
            """
    class M(FQSymBasis_abstract):
        """
        The M-basis of `FQSym`.

        This is the Monomial basis `(\\mathcal{M}_w)`, with `w` ranging
        over all permutations. See the documentation of :class:`FQSym`
        for details.

        EXAMPLES::

            sage: FQSym = algebras.FQSym(QQ)
            sage: M = FQSym.M(); M
            Free Quasi-symmetric functions over Rational Field in the Monomial basis

            sage: M([3, 1, 2]).coproduct()
            M[] # M[3, 1, 2] + M[1] # M[1, 2] + M[3, 1, 2] # M[]
            sage: M([3, 2, 1]).coproduct()
            M[] # M[3, 2, 1] + M[1] # M[2, 1] + M[2, 1] # M[1]
             + M[3, 2, 1] # M[]

            sage: M([1, 2]) * M([1])
            M[1, 2, 3] + 2*M[1, 3, 2] + M[2, 3, 1] + M[3, 1, 2]
        """
        def __init__(self, alg) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: M = algebras.FQSym(QQ).M()
                sage: TestSuite(M).run(elements=M.some_elements()[:-1])  # long time
            """
        def __getitem__(self, r):
            """
            The default implementation of ``__getitem__`` interprets
            the input as a tuple, which in case of permutations
            is interpreted as cycle notation, even though the input
            looks like a one-line notation.
            We override this method to amend this.

            EXAMPLES::

                sage: M = algebras.FQSym(QQ).M()
                sage: M[3, 2, 1]
                M[3, 2, 1]
                sage: M[1]
                M[1]
            """
        def degree_on_basis(self, t):
            """
            Return the degree of a permutation in
            the algebra of free quasi-symmetric functions.

            This is the size of the permutation (i.e., the `n`
            for which the permutation belongs to `S_n`).

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).M()
                sage: u = Permutation([2,1])
                sage: A.degree_on_basis(u)
                2
            """
        def coproduct_on_basis(self, x):
            """
            Return the coproduct of `\\mathcal{M}_{\\sigma}` for `\\sigma`
            a permutation (here, `\\sigma` is ``x``).

            This uses Theorem 3.1 in [AguSot05]_.

            EXAMPLES::

                sage: M = algebras.FQSym(QQ).M()
                sage: x = M([1])
                sage: ascii_art(M.coproduct(M.one()))  # indirect doctest
                1 # 1

                sage: ascii_art(M.coproduct(x))  # indirect doctest
                1 # M    + M    # 1
                     [1]    [1]

                sage: M.coproduct(M([2, 1, 3]))
                M[] # M[2, 1, 3] + M[2, 1, 3] # M[]
                sage: M.coproduct(M([2, 3, 1]))
                M[] # M[2, 3, 1] + M[1, 2] # M[1] + M[2, 3, 1] # M[]
                sage: M.coproduct(M([3, 2, 1]))
                M[] # M[3, 2, 1] + M[1] # M[2, 1] + M[2, 1] # M[1]
                + M[3, 2, 1] # M[]
                sage: M.coproduct(M([3, 4, 2, 1]))
                M[] # M[3, 4, 2, 1] + M[1, 2] # M[2, 1] + M[2, 3, 1] # M[1]
                 + M[3, 4, 2, 1] # M[]
                sage: M.coproduct(M([3, 4, 1, 2]))
                M[] # M[3, 4, 1, 2] + M[1, 2] # M[1, 2] + M[3, 4, 1, 2] # M[]
            """
        class Element(FQSymBasis_abstract.Element):
            def star_involution(self):
                """
                Return the image of the element ``self`` of `FQSym`
                under the star involution.

                See
                :meth:`FQSymBases.ElementMethods.star_involution`
                for a definition of the involution and for examples.

                .. SEEALSO::

                    :meth:`omega_involution`, :meth:`psi_involution`

                EXAMPLES::

                    sage: FQSym = algebras.FQSym(ZZ)
                    sage: M = FQSym.M()
                    sage: M[[2,3,1]].star_involution()
                    M[3, 1, 2]
                    sage: M[[]].star_involution()
                    M[]

                TESTS::

                    sage: F = FQSym.F()
                    sage: all(M(F[w]).star_involution() == M(F[w].star_involution())
                    ....:     for w in Permutations(4))
                    True
                """

class FQSymBases(Category_realization_of_parent):
    """
    The category of graded bases of `FQSym` indexed by permutations.
    """
    def __init__(self, base) -> None:
        """
        Initialize the bases of an `FQSym`.

        INPUT:

        - ``base`` -- an instance of `FQSym`

        TESTS::

            sage: from sage.combinat.fqsym import FQSymBases
            sage: FQSym = algebras.FQSym(ZZ)
            sage: bases = FQSymBases(FQSym)
            sage: FQSym.F() in bases
            True
        """
    def super_categories(self):
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.fqsym import FQSymBases
            sage: FQSym = algebras.FQSym(ZZ)
            sage: bases = FQSymBases(FQSym)
            sage: bases.super_categories()
            [Category of realizations of Free Quasi-symmetric functions over Integer Ring,
             Join of Category of realizations of Hopf algebras over Integer Ring
               and Category of graded algebras over Integer Ring
               and Category of graded coalgebras over Integer Ring,
             Category of graded connected Hopf algebras with basis over Integer Ring]
        """
    class ParentMethods:
        def __getitem__(self, p):
            """
            Return the basis element indexed by ``p``.

            INPUT:

            - ``p`` -- a permutation

            EXAMPLES::

                sage: R = algebras.FQSym(QQ).F()
                sage: R[[1, 3, 2]]
                F[1, 3, 2]
                sage: R[Permutation([1, 3, 2])]
                F[1, 3, 2]
                sage: R[SymmetricGroup(4)(Permutation([1,3,4,2]))]
                F[1, 3, 4, 2]
            """
        def basis(self, degree=None):
            """
            The basis elements (optionally: of the specified degree).

            OUTPUT: Family

            EXAMPLES::

                sage: FQSym = algebras.FQSym(QQ)
                sage: G = FQSym.G()
                sage: G.basis()
                Lazy family (Term map from Standard permutations to Free Quasi-symmetric functions over Rational Field in the G basis(i))_{i in Standard permutations}
                sage: G.basis().keys()
                Standard permutations
                sage: G.basis(degree=3).keys()
                Standard permutations of 3
                sage: G.basis(degree=3).list()
                [G[1, 2, 3], G[1, 3, 2], G[2, 1, 3], G[2, 3, 1], G[3, 1, 2], G[3, 2, 1]]
            """
        def is_field(self, proof: bool = True):
            """
            Return whether this `FQSym` is a field.

            EXAMPLES::

                sage: F = algebras.FQSym(QQ).F()
                sage: F.is_field()
                False
            """
        def some_elements(self):
            """
            Return some elements of the free quasi-symmetric functions.

            EXAMPLES::

                sage: A = algebras.FQSym(QQ)
                sage: F = A.F()
                sage: F.some_elements()
                [F[], F[1], F[1, 2] + F[2, 1], F[] + F[1, 2] + F[2, 1]]
                sage: G = A.G()
                sage: G.some_elements()
                [G[], G[1], G[1, 2] + G[2, 1], G[] + G[1, 2] + G[2, 1]]
                sage: M = A.M()
                sage: M.some_elements()
                [M[], M[1], M[1, 2] + 2*M[2, 1], M[] + M[1, 2] + 2*M[2, 1]]
            """
        @cached_method
        def one_basis(self):
            """
            Return the index of the unit.

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: A.one_basis()
                []
            """
        @lazy_attribute
        def succ(self):
            """
            Return the `\\succ` product.

            On the F-basis of ``FQSym``, this product is determined by
            `F_x \\succ F_y = \\sum F_z`, where the sum ranges over all `z`
            in the shifted shuffle of `x` and `y` with the additional
            condition that the first letter of the result comes from `y`.

            The usual symbol for this operation is `\\succ`.

            .. SEEALSO::

                :meth:`~sage.categories.magmas.Magmas.ParentMethods.product`,
                :meth:`prec`

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: x = A([1])
                sage: A.succ(x, x)
                F[2, 1]
                sage: y = A([3,1,2])
                sage: A.succ(x, y)
                F[4, 1, 2, 3] + F[4, 2, 1, 3] + F[4, 2, 3, 1]
                sage: A.succ(y, x)
                F[4, 3, 1, 2]
            """
        def succ_by_coercion(self, x, y):
            """
            Return `x \\succ y`, computed using coercion to the F-basis.

            See :meth:`succ` for the definition of the objects involved.

            EXAMPLES::

                sage: G = algebras.FQSym(ZZ).G()
                sage: G.succ(G([1]), G([2, 3, 1])) # indirect doctest
                G[2, 3, 4, 1] + G[3, 2, 4, 1] + G[4, 2, 3, 1]
            """
        @lazy_attribute
        def prec(self):
            """
            Return the `\\prec` product.

            On the F-basis of ``FQSym``, this product is determined by
            `F_x \\prec F_y = \\sum F_z`, where the sum ranges over all `z`
            in the shifted shuffle of `x` and `y` with the additional
            condition that the first letter of the result comes from `x`.

            The usual symbol for this operation is `\\prec`.

            .. SEEALSO::

                :meth:`~sage.categories.magmas.Magmas.ParentMethods.product`,
                :meth:`succ`

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: x = A([2,1])
                sage: A.prec(x, x)
                F[2, 1, 4, 3] + F[2, 4, 1, 3] + F[2, 4, 3, 1]
                sage: y = A([2,1,3])
                sage: A.prec(x, y)
                F[2, 1, 4, 3, 5] + F[2, 4, 1, 3, 5] + F[2, 4, 3, 1, 5]
                 + F[2, 4, 3, 5, 1]
                sage: A.prec(y, x)
                F[2, 1, 3, 5, 4] + F[2, 1, 5, 3, 4] + F[2, 1, 5, 4, 3]
                 + F[2, 5, 1, 3, 4] + F[2, 5, 1, 4, 3] + F[2, 5, 4, 1, 3]
            """
        def prec_by_coercion(self, x, y):
            """
            Return `x \\prec y`, computed using coercion to the F-basis.

            See :meth:`prec` for the definition of the objects involved.

            EXAMPLES::

                sage: G = algebras.FQSym(ZZ).G()
                sage: a = G([1])
                sage: b = G([2, 3, 1])
                sage: G.prec(a, b) + G.succ(a, b) == a * b # indirect doctest
                True
            """
        def from_symmetric_group_algebra(self, x):
            """
            Return the element of `FQSym` corresponding to the element
            `x` of a symmetric group algebra.

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).F()
                sage: SGA4 = SymmetricGroupAlgebra(QQ, 4)
                sage: x = SGA4([1,3,2,4]) + 5/2 * SGA4([1,2,4,3])
                sage: A.from_symmetric_group_algebra(x)
                5/2*F[1, 2, 4, 3] + F[1, 3, 2, 4]
                sage: A.from_symmetric_group_algebra(SGA4.zero())
                0
            """
    class ElementMethods:
        def omega_involution(self):
            """
            Return the image of the element ``self`` of `FQSym`
            under the omega involution.

            The `\\omega` involution is defined as the
            linear map `FQSym \\to FQSym` that sends each basis
            element `F_u` of the F-basis of `FQSym`
            to the basis element `F_{u \\circ w_0}`, where `w_0` is
            the longest word (i.e., `w_0(i) = n + 1 - i`) in the
            symmetric group `S_n` that contains `u`. The `\\omega`
            involution is a graded algebra automorphism and a
            coalgebra anti-automorphism of `FQSym`. Every
            permutation `u \\in S_n` satisfies

            .. MATH::

                \\omega(F_u) = F_{u \\circ w_0}, \\qquad
                \\omega(G_u) = G_{w_0 \\circ u},

            where standard notations for classical bases of `FQSym`
            are being used (that is, `F` for the F-basis, and
            `G` for the G-basis).
            In other words, writing permutations in one-line notation,
            we have

            .. MATH::

                \\omega(F_{(u_1, u_2, \\ldots, u_n)})
                = F_{(u_n, u_{n-1}, \\ldots, u_1)}, \\qquad
                \\omega(G_{(u_1, u_2, \\ldots, u_n)})
                = G_{(n+1-u_1, n+1-u_2, \\ldots, n+1-u_n)}.

            If we also consider the `\\omega` involution
            (:meth:`~sage.combinat.ncsf_qsym.qsym.QuasiSymmetricFunctions.Bases.ElementMethods.omega_involution`)
            of the quasisymmetric functions (by slight abuse
            of notation), and if we let `\\pi` be the canonical
            projection `FQSym \\to QSym`, then
            `\\pi \\circ \\omega = \\omega \\circ \\pi`.

            Additionally, consider the `\\psi` involution
            (:meth:`~sage.combinat.ncsf_qsym.ncsf.NonCommutativeSymmetricFunctions.Bases.ElementMethods.psi_involution`)
            of the noncommutative symmetric functions, and if we let
            `\\iota` be the canonical inclusion `NSym \\to FQSym`,
            then `\\omega \\circ \\iota = \\iota \\circ \\psi`.

            .. TODO::

                Duality?

            .. SEEALSO::

                :meth:`psi_involution`, :meth:`star_involution`

            EXAMPLES::

                sage: FQSym = algebras.FQSym(ZZ)
                sage: F = FQSym.F()
                sage: F[[2,3,1]].omega_involution()
                F[1, 3, 2]
                sage: (3*F[[1]] - 4*F[[]] + 5*F[[1,2]]).omega_involution()
                -4*F[] + 3*F[1] + 5*F[2, 1]
                sage: G = FQSym.G()
                sage: G[[2,3,1]].omega_involution()
                G[2, 1, 3]
                sage: M = FQSym.M()
                sage: M[[2,3,1]].omega_involution()
                -M[1, 2, 3] - M[2, 1, 3] - M[3, 1, 2]

            The omega involution is an algebra homomorphism::

                sage: (F[1,2] * F[1]).omega_involution()
                F[2, 1, 3] + F[2, 3, 1] + F[3, 2, 1]
                sage: F[1,2].omega_involution() * F[1].omega_involution()
                F[2, 1, 3] + F[2, 3, 1] + F[3, 2, 1]

            The omega involution intertwines the antipode
            and the inverse of the antipode::

                sage: all( F(I).antipode().omega_involution().antipode()
                ....:      == F(I).omega_involution()
                ....:      for I in Permutations(4) )
                True

            Testing the `\\pi \\circ \\omega = \\omega \\circ \\pi` relation
            noticed above::

                sage: all( M[I].omega_involution().to_qsym()
                ....:      == M[I].to_qsym().omega_involution()
                ....:      for I in Permutations(4) )
                True

            Testing the `\\omega \\circ \\iota = \\iota \\circ \\psi` relation::

                sage: NSym = NonCommutativeSymmetricFunctions(ZZ)
                sage: S = NSym.S()
                sage: all( S[I].psi_involution().to_fqsym() == S[I].to_fqsym().omega_involution()
                ....:      for I in Compositions(4) )
                True

            .. TODO::

                Check further commutative squares.
            """
        def psi_involution(self):
            """
            Return the image of the element ``self`` of `FQSym`
            under the psi involution.

            The `\\psi` involution is defined as the
            linear map `FQSym \\to FQSym` that sends each basis
            element `F_u` of the F-basis of `FQSym`
            to the basis element `F_{w_0 \\circ u}`, where `w_0` is
            the longest word (i.e., `w_0(i) = n + 1 - i`) in the
            symmetric group `S_n` that contains `u`. The `\\psi`
            involution is a graded coalgebra automorphism and
            an algebra anti-automorphism of `FQSym`. Every
            permutation `u \\in S_n` satisfies

            .. MATH::

                \\psi(F_u) = F_{w_0 \\circ u}, \\qquad
                \\psi(G_u) = G_{u \\circ w_0},

            where standard notations for classical bases of `FQSym`
            are being used (that is, `F` for the F-basis, and
            `G` for the G-basis). In other words, writing
            permutations in one-line notation, we have

            .. MATH::

                \\psi(F_{(u_1, u_2, \\ldots, u_n)})
                = F_{(n+1-u_1, n+1-u_2, \\ldots, n+1-u_n)}, \\qquad
                \\psi(G_{(u_1, u_2, \\ldots, u_n)})
                = G_{(u_n, u_{n-1}, \\ldots, u_1)}.

            If we also consider the `\\psi` involution
            (:meth:`~sage.combinat.ncsf_qsym.qsym.QuasiSymmetricFunctions.Bases.ElementMethods.psi_involution`)
            of the quasisymmetric functions (by slight abuse of
            notation), and if we let `\\pi` be the canonical
            projection `FQSym \\to QSym`, then
            `\\pi \\circ \\psi = \\psi \\circ \\pi`.

            Additionally, consider the `\\omega` involution
            (:meth:`~sage.combinat.ncsf_qsym.ncsf.NonCommutativeSymmetricFunctions.Bases.ElementMethods.omega_involution`)
            of the noncommutative symmetric functions, and if we let
            `\\iota` be the canonical inclusion `NSym \\to FQSym`,
            then `\\psi \\circ \\iota = \\iota \\circ \\omega`.

            .. TODO::

                Duality?

            .. SEEALSO::

                :meth:`omega_involution`, :meth:`star_involution`

            EXAMPLES::

                sage: FQSym = algebras.FQSym(ZZ)
                sage: F = FQSym.F()
                sage: F[[2,3,1]].psi_involution()
                F[2, 1, 3]
                sage: (3*F[[1]] - 4*F[[]] + 5*F[[1,2]]).psi_involution()
                -4*F[] + 3*F[1] + 5*F[2, 1]
                sage: G = FQSym.G()
                sage: G[[2,3,1]].psi_involution()
                G[1, 3, 2]
                sage: M = FQSym.M()
                sage: M[[2,3,1]].psi_involution()
                -M[1, 2, 3] - M[1, 3, 2] - M[2, 3, 1]

            The `\\psi` involution intertwines the antipode
            and the inverse of the antipode::

                sage: all( F(I).antipode().psi_involution().antipode()
                ....:      == F(I).psi_involution()
                ....:      for I in Permutations(4) )
                True

            Testing the `\\pi \\circ \\psi = \\psi \\circ \\pi` relation above::

                sage: all( M[I].psi_involution().to_qsym()
                ....:      == M[I].to_qsym().psi_involution()
                ....:      for I in Permutations(4) )
                True

            Testing the `\\psi \\circ \\iota = \\iota \\circ \\omega` relation::

                sage: NSym = NonCommutativeSymmetricFunctions(ZZ)
                sage: S = NSym.S()
                sage: all( S[I].omega_involution().to_fqsym() == S[I].to_fqsym().psi_involution()
                ....:      for I in Compositions(4) )
                True

            .. TODO::

                Check further commutative squares.
            """
        def star_involution(self):
            """
            Return the image of the element ``self`` of `FQSym`
            under the star involution.

            The star involution is defined as the
            linear map `FQSym \\to FQSym` that sends each basis
            element `F_u` of the F-basis of `FQSym`
            to the basis element `F_{w_0 \\circ u \\circ w_0}`, where
            `w_0` is the longest word (i.e., `w_0(i) = n + 1 - i`)
            in the symmetric group `S_n` that contains `u`.
            The star involution is a graded Hopf algebra
            anti-automorphism of `FQSym`.
            It is denoted by `f \\mapsto f^*`. Every permutation
            `u \\in S_n` satisfies

            .. MATH::

                (F_u)^* = F_{w_0 \\circ u \\circ w_0}, \\qquad
                (G_u)^* = G_{w_0 \\circ u \\circ w_0}, \\qquad
                (\\mathcal{M}_u)^* = \\mathcal{M}_{w_0 \\circ u \\circ w_0},

            where standard notations for classical bases of `FQSym`
            are being used (that is, `F` for the F-basis,
            `G` for the G-basis, and `\\mathcal{M}` for the Monomial
            basis). In other words, writing permutations in one-line
            notation, we have

            .. MATH::

                (F_{(u_1, u_2, \\ldots, u_n)})^*
                = F_{(n+1-u_n, n+1-u_{n-1}, \\ldots, n+1-u_1)}, \\qquad
                (G_{(u_1, u_2, \\ldots, u_n)})^*
                = G_{(n+1-u_n, n+1-u_{n-1}, \\ldots, n+1-u_1)},

            and

            .. MATH::

                (\\mathcal{M}_{(u_1, u_2, \\ldots, u_n)})^*
                = \\mathcal{M}_{(n+1-u_n, n+1-u_{n-1}, \\ldots, n+1-u_1)}.

            Let us denote the star involution by `(\\ast)` as well.

            If we also denote by `(\\ast)` the star involution of
            of the quasisymmetric functions
            (:meth:`~sage.combinat.ncsf_qsym.qsym.QuasiSymmetricFunctions.Bases.ElementMethods.star_involution`)
            and if we let `\\pi : FQSym \\to QSym` be the canonical
            projection then `\\pi \\circ (\\ast) = (\\ast) \\circ \\pi`.
            Similar for the noncommutative symmetric functions
            (:meth:`~sage.combinat.ncsf_qsym.ncsf.NonCommutativeSymmetricFunctions.Bases.ElementMethods.star_involution`)
            with `\\pi : NSym \\to FQSym` being the canonical inclusion
            and the word quasisymmetric functions
            (:meth:`~sage.combinat.chas.wqsym.WordQuasiSymmetricFunctions.Bases.ElementMethods.star_involution`)
            with `\\pi : FQSym \\to WQSym` the canonical inclusion.

            .. TODO::

                Duality?

            .. SEEALSO::

                :meth:`omega_involution`, :meth:`psi_involution`

            EXAMPLES::

                sage: FQSym = algebras.FQSym(ZZ)
                sage: F = FQSym.F()
                sage: F[[2,3,1]].star_involution()
                F[3, 1, 2]
                sage: (3*F[[1]] - 4*F[[]] + 5*F[[1,2]]).star_involution()
                -4*F[] + 3*F[1] + 5*F[1, 2]
                sage: G = FQSym.G()
                sage: G[[2,3,1]].star_involution()
                G[3, 1, 2]
                sage: M = FQSym.M()
                sage: M[[2,3,1]].star_involution()
                M[3, 1, 2]

            The star involution commutes with the antipode::

                sage: all( F(I).antipode().star_involution()
                ....:      == F(I).star_involution().antipode()
                ....:      for I in Permutations(4) )
                True

            Testing the `\\pi \\circ (\\ast) = (\\ast) \\circ \\pi` relation::

                sage: all( M[I].star_involution().to_qsym()
                ....:      == M[I].to_qsym().star_involution()
                ....:      for I in Permutations(4) )
                True

            Similar for `NSym`::

                sage: NSym = NonCommutativeSymmetricFunctions(ZZ)
                sage: S = NSym.S()
                sage: all( S[I].star_involution().to_fqsym() == S[I].to_fqsym().star_involution()
                ....:      for I in Compositions(4) )
                True

            Similar for `WQSym`::

                sage: WQSym = algebras.WQSym(ZZ)
                sage: all( F(I).to_wqsym().star_involution()
                ....:      == F(I).star_involution().to_wqsym()
                ....:      for I in Permutations(4) )
                True

            .. TODO::

                Check further commutative squares.
            """
        def to_symmetric_group_algebra(self, n=None):
            """
            Return the element of a symmetric group algebra
            corresponding to the element ``self`` of `FQSym`.

            INPUT:

            - ``n`` -- integer (default: the maximal degree of ``self``);
              the rank of the target symmetric group algebra

            EXAMPLES::

                sage: A = algebras.FQSym(QQ).G()
                sage: x = A([1,3,2,4]) + 5/2 * A([2,3,4,1])
                sage: x.to_symmetric_group_algebra()
                [1, 3, 2, 4] + 5/2*[4, 1, 2, 3]
            """
        def to_wqsym(self):
            """
            Return the image of ``self`` under the canonical
            inclusion map `FQSym \\to WQSym`.

            The canonical inclusion map `FQSym \\to WQSym` is
            an injective homomorphism of Hopf algebras. It sends
            a basis element `G_w` of `FQSym` to the sum of
            basis elements `\\mathbf{M}_u` of `WQSym`, where `u`
            ranges over all packed words whose standardization
            is `w`.

            .. SEEALSO::

                :class:`WordQuasiSymmetricFunctions` for a
                definition of `WQSym`.

            EXAMPLES::

                sage: G = algebras.FQSym(QQ).G()
                sage: x = G[1, 3, 2]
                sage: x.to_wqsym()
                M[{1}, {3}, {2}] + M[{1, 3}, {2}]
                sage: G[1, 2].to_wqsym()
                M[{1}, {2}] + M[{1, 2}]
                sage: F = algebras.FQSym(QQ).F()
                sage: F[3, 1, 2].to_wqsym()
                M[{3}, {1}, {2}] + M[{3}, {1, 2}]
                sage: G[2, 3, 1].to_wqsym()
                M[{3}, {1}, {2}] + M[{3}, {1, 2}]
            """
        def to_qsym(self):
            """
            Return the image of ``self`` under the canonical
            projection `FQSym \\to QSym`.

            The canonical projection `FQSym \\to QSym` is a
            surjective homomorphism of Hopf algebras. It sends a
            basis element `F_w` of `FQSym` to the basis element
            `F_{\\operatorname{Comp} w}` of the fundamental basis
            of `QSym`, where `\\operatorname{Comp} w` stands for
            the descent composition
            (:meth:`sage.combinat.permutation.Permutation.descents_composition`)
            of the permutation `w`.

            .. SEEALSO::

                :class:`QuasiSymmetricFunctions` for a
                definition of `QSym`.

            EXAMPLES::

                sage: G = algebras.FQSym(QQ).G()
                sage: x = G[1, 3, 2]
                sage: x.to_qsym()
                F[2, 1]
                sage: G[2, 3, 1].to_qsym()
                F[1, 2]
                sage: F = algebras.FQSym(QQ).F()
                sage: F[2, 3, 1].to_qsym()
                F[2, 1]
                sage: (F[2, 3, 1] + F[1, 3, 2] + F[1, 2, 3]).to_qsym()
                2*F[2, 1] + F[3]
                sage: F2 = algebras.FQSym(GF(2)).F()
                sage: F2[2, 3, 1].to_qsym()
                F[2, 1]
                sage: (F2[2, 3, 1] + F2[1, 3, 2] + F2[1, 2, 3]).to_qsym()
                F[3]
            """
