from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent
from sage.combinat.composition import Composition as Composition
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.combinat.tableau import StandardTableaux as StandardTableaux, Tableau as Tableau
from sage.misc.bindable_class import BindableClass as BindableClass
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FSymBasis_abstract(CombinatorialFreeModule, BindableClass):
    """
    Abstract base class for graded bases of `FSym` and of `FSym^*`
    indexed by standard tableaux.

    This must define the following attributes:

    - ``_prefix`` -- the basis prefix
    """
    def __init__(self, alg, graded: bool = True) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: G = algebras.FSym(QQ).G()
            sage: TestSuite(G).run()  # long time

        Checks for the antipode::

            sage: FSym = algebras.FSym(QQ)
            sage: G = FSym.G()
            sage: for b in G.basis(degree=3):
            ....:     print("%s : %s" % (b, b.antipode()))
            G[123] : -G[1|2|3]
            G[13|2] : -G[13|2]
            G[12|3] : -G[12|3]
            G[1|2|3] : -G[123]

            sage: F = FSym.dual().F()
            sage: for b in F.basis(degree=3):
            ....:     print("%s : %s" % (b, b.antipode()))
            F[123] : -F[1|2|3]
            F[13|2] : -F[13|2]
            F[12|3] : -F[12|3]
            F[1|2|3] : -F[123]
        '''
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: G = algebras.FSym(QQ).G()
            sage: G.some_elements()
            [G[], G[1], G[12], G[1] + G[1|2], G[] + 1/2*G[1]]
        """

class FSymBases(Category_realization_of_parent):
    """
    The category of graded bases of `FSym` and `FSym^*` indexed
    by standard tableaux.
    """
    def super_categories(self):
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: from sage.combinat.chas.fsym import FSymBases
            sage: FSym = algebras.FSym(ZZ)
            sage: bases = FSymBases(FSym)
            sage: bases.super_categories()
            [Category of realizations of Hopf algebra of standard tableaux over the Integer Ring,
             Join of Category of realizations of Hopf algebras over Integer Ring
                 and Category of graded algebras over Integer Ring
                 and Category of graded coalgebras over Integer Ring,
             Category of graded connected Hopf algebras with basis over Integer Ring]
        """
    class ParentMethods:
        def __getitem__(self, key):
            """
            Override the ``__getitem__`` method to allow passing a standard
            tableau in a nonstandard form (e.g., as a tuple of rows instead
            of a list of rows; or as a single row for a single-rowed tableau).

            EXAMPLES:

            Construct the basis element indexed by a standard tableau by
            passing data that defines the standard tableau::

                sage: FSym = algebras.FSym(QQ)
                sage: G = FSym.G()
                sage: G[[1,3],[2]]
                G[13|2]
                sage: G[(1,3),(2,)]
                G[13|2]
                sage: G[[1,3],[2]].leading_support() in StandardTableaux()
                True
                sage: G[1,2,3]
                G[123]
            """
        def basis(self, degree=None):
            """
            The basis elements (optionally: of the specified degree).

            OUTPUT: family

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: TG = FSym.G()
                sage: TG.basis()
                Lazy family (Term map from Standard tableaux to Hopf algebra of standard tableaux
                 over the Rational Field in the Fundamental basis(i))_{i in Standard tableaux}
                sage: TG.basis().keys()
                Standard tableaux
                sage: TG.basis(degree=3).keys()
                Standard tableaux of size 3
                sage: TG.basis(degree=3).list()
                [G[123], G[13|2], G[12|3], G[1|2|3]]
            """
        @cached_method
        def one_basis(self):
            """
            Return the basis index corresponding to `1`.

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: TG = FSym.G()
                sage: TG.one_basis()
                []
            """
        def duality_pairing(self, x, y):
            """
            The canonical pairing between `FSym` and `FSym^*`.

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: G = FSym.G()
                sage: F = G.dual_basis()
                sage: t1 = StandardTableau([[1,3,5],[2,4]])
                sage: t2 = StandardTableau([[1,3],[2,5],[4]])
                sage: G.duality_pairing(G[t1], F[t2])
                0
                sage: G.duality_pairing(G[t1], F[t1])
                1
                sage: G.duality_pairing(G[t2], F[t2])
                1
                sage: F.duality_pairing(F[t2], G[t2])
                1

                sage: z = G[[1,3,5],[2,4]]
                sage: all(F.duality_pairing(F[p1] * F[p2], z) == c
                ....:     for (p1, p2), c in z.coproduct())
                True

            TESTS:

            If ``x`` is zero, then the output still has the right
            type::

                sage: z = G.duality_pairing(G.zero(), F.zero()); z
                0
                sage: parent(z)
                Rational Field
            """
        def duality_pairing_matrix(self, basis, degree):
            """
            The matrix of scalar products between elements of `FSym` and
            elements of `FSym^*`.

            INPUT:

            - ``basis`` -- a basis of the dual Hopf algebra
            - ``degree`` -- nonnegative integer

            OUTPUT:

            - the matrix of scalar products between the basis ``self`` and the
              basis ``basis`` in the dual Hopf algebra of degree ``degree``

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: G = FSym.G()
                sage: G.duality_pairing_matrix(G.dual_basis(), 3)
                [1 0 0 0]
                [0 1 0 0]
                [0 0 1 0]
                [0 0 0 1]
            """
        def degree_on_basis(self, t):
            """
            Return the degree of a standard tableau in the algebra
            of free symmetric functions.

            This is the size of the tableau ``t``.

            EXAMPLES::

                sage: G = algebras.FSym(QQ).G()
                sage: t = StandardTableau([[1,3],[2]])
                sage: G.degree_on_basis(t)
                3
                sage: u = StandardTableau([[1,3,4,5],[2]])
                sage: G.degree_on_basis(u)
                5
            """
    class ElementMethods:
        def duality_pairing(self, other):
            """
            Compute the pairing between ``self`` and an element ``other``
            of the dual.

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: G = FSym.G()
                sage: F = G.dual_basis()
                sage: elt = G[[1,3],[2]] - 3*G[[1,2],[3]]
                sage: elt.duality_pairing(F[[1,3],[2]])
                1
                sage: elt.duality_pairing(F[[1,2],[3]])
                -3
                sage: elt.duality_pairing(F[[1,2]])
                0
            """

class FreeSymmetricFunctions(UniqueRepresentation, Parent):
    """
    The free symmetric functions.

    The *free symmetric functions* is a combinatorial Hopf algebra
    defined using tableaux and denoted `FSym`.

    Consider the Hopf algebra `FQSym`
    (:class:`~sage.combinat.fqsym.FreeQuasisymmetricFunctions`)
    over a commutative ring `R`, and its bases `(F_w)` and `(G_w)`
    (where `w`, in both cases, ranges over all permutations in all
    symmetric groups `S_0, S_1, S_2, \\ldots`).
    For each word `w`, let `P(w)` be the P-tableau of `w` (that
    is, the first of the two tableaux obtained by applying the
    RSK algorithm to `w`; see :meth:`~sage.combinat.rsk.RSK`).
    If `t` is a standard tableau of size `n`, then we define
    `\\mathcal{G}_t \\in FQSym` to be the sum of the `F_w` with
    `w` ranging over all permutations of `\\{1, 2, \\ldots, n\\}`
    satisfying `P(w) = t`. Equivalently, `\\mathcal{G}_t` is the
    sum of the `G_w` with `w` ranging over all permutations of
    `\\{1, 2, \\ldots, n\\}` satisfying `Q(w) = t` (where `Q(w)`
    denotes the Q-tableau of `w`).

    The `R`-linear span of the `\\mathcal{G}_t` (for `t` ranging
    over all standard tableaux) is a Hopf subalgebra of `FQSym`,
    denoted by `FSym` and known as the *free symmetric functions*
    or the *Poirier-Reutenauer Hopf algebra of tableaux*. It has been
    introduced in [PoiReu95]_, where it was denoted by
    `(\\ZZ T, \\ast, \\delta)`. (What we call `\\mathcal{G}_t`
    has just been called `t` in [PoiReu95]_.)
    The family `(\\mathcal{G}_t)` (with `t` ranging over all standard
    tableaux) is a basis of `FSym`, called the *Fundamental basis*.

    EXAMPLES:

    As explained above, `FSym` is constructed as a Hopf subalgebra of
    `FQSym`::

        sage: G = algebras.FSym(QQ).G()
        sage: F = algebras.FQSym(QQ).F()
        sage: G[[1,3],[2]]
        G[13|2]
        sage: G[[1,3],[2]].to_fqsym()
        G[2, 1, 3] + G[3, 1, 2]
        sage: F(G[[1,3],[2]])
        F[2, 1, 3] + F[2, 3, 1]

    This embedding is a Hopf algebra morphism::

        sage: all(F(G[t1] * G[t2]) == F(G[t1]) * F(G[t2])
        ....:     for t1 in StandardTableaux(2)
        ....:     for t2 in StandardTableaux(3))
        True

        sage: FF = F.tensor_square()
        sage: all(FF(G[t].coproduct()) == F(G[t]).coproduct()
        ....:     for t in StandardTableaux(4))
        True

    There is a Hopf algebra map from `FSym` onto the Hopf algebra
    of symmetric functions, which maps a tableau `t` to the Schur
    function indexed by the shape of `t`::

        sage: TG = algebras.FSym(QQ).G()
        sage: t = StandardTableau([[1,3],[2,4],[5]])
        sage: TG[t]
        G[13|24|5]
        sage: TG[t].to_symmetric_function()
        s[2, 2, 1]
    """
    def __init__(self, base_ring) -> None:
        """
        TESTS::

            sage: FSym = algebras.FSym(QQ)
            sage: TestSuite(FSym).run()
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the Fundamental basis).

        EXAMPLES::

            sage: FSym = algebras.FSym(QQ)
            sage: FSym.a_realization()
            Hopf algebra of standard tableaux over the Rational Field
             in the Fundamental basis
        """
    def dual(self):
        """
        Return the dual Hopf algebra of `FSym`.

        EXAMPLES::

            sage: algebras.FSym(QQ).dual()
            Dual Hopf algebra of standard tableaux over the Rational Field
        """
    class Fundamental(FSymBasis_abstract):
        """
        The Hopf algebra of tableaux on the Fundamental basis.

        EXAMPLES::

            sage: FSym = algebras.FSym(QQ)
            sage: TG = FSym.G()
            sage: TG
            Hopf algebra of standard tableaux over the Rational Field
             in the Fundamental basis

        Elements of the algebra look like::

            sage: TG.an_element()
            2*G[] + 2*G[1] + 3*G[12]

        TESTS::

            sage: FSym = algebras.FSym(QQ)
            sage: TG = FSym.G()
            sage: TestSuite(TG).run()
        """
        def dual_basis(self):
            """
            Return the dual basis to ``self``.

            EXAMPLES::

                sage: G = algebras.FSym(QQ).G()
                sage: G.dual_basis()
                Dual Hopf algebra of standard tableaux over the Rational Field
                 in the FundamentalDual basis
            """
        @cached_method
        def product_on_basis(self, t1, t2):
            """
            Return the product of basis elements indexed by ``t1`` and ``t2``.

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: G = FSym.G()
                sage: t1 = StandardTableau([[1,2], [3]])
                sage: t2 = StandardTableau([[1,2,3]])
                sage: G.product_on_basis(t1, t2)
                G[12456|3] + G[1256|3|4] + G[1256|34] + G[126|35|4]

                sage: t1 = StandardTableau([[1],[2]])
                sage: t2 = StandardTableau([[1,2]])
                sage: G.product_on_basis(t1, t2)
                G[134|2] + G[14|2|3]

                sage: t1 = StandardTableau([[1,2],[3]])
                sage: t2 = StandardTableau([[1],[2]])
                sage: G.product_on_basis(t1, t2)
                G[12|3|4|5] + G[12|34|5] + G[124|3|5] + G[124|35]
            """
        @cached_method
        def coproduct_on_basis(self, t):
            """
            Return the coproduct of the basis element indexed by ``t``.

            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: G = FSym.G()
                sage: t = StandardTableau([[1,2,5], [3,4]])
                sage: G.coproduct_on_basis(t)
                G[] # G[125|34] + G[1] # G[12|34] + G[1] # G[124|3]
                 + G[1|2] # G[13|2] + G[12] # G[12|3] + G[12] # G[123]
                 + G[12|34] # G[1] + G[123] # G[12] + G[125|34] # G[]
                 + G[13|2] # G[1|2] + G[13|2] # G[12] + G[134|2] # G[1]
            """
        class Element(FSymBasis_abstract.Element):
            def to_fqsym(self):
                """
                Return the image of ``self`` under the natural inclusion
                map to `FQSym`.

                EXAMPLES::

                    sage: FSym = algebras.FSym(QQ)
                    sage: G = FSym.G()
                    sage: t = StandardTableau([[1,3],[2,4],[5]])
                    sage: G[t].to_fqsym()
                    G[2, 1, 5, 4, 3] + G[3, 1, 5, 4, 2] + G[3, 2, 5, 4, 1]
                     + G[4, 1, 5, 3, 2] + G[4, 2, 5, 3, 1]
                """
            def to_symmetric_function(self):
                """
                Return the image of ``self`` under the natural projection
                map to `Sym`.

                The natural projection map `FSym \\to Sym` sends each
                standard tableau `t` to the Schur function `s_\\lambda`,
                where `\\lambda` is the shape of `t`.
                This map is a surjective Hopf algebra homomorphism.

                EXAMPLES::

                    sage: FSym = algebras.FSym(QQ)
                    sage: G = FSym.G()
                    sage: t = StandardTableau([[1,3],[2,4],[5]])
                    sage: G[t].to_symmetric_function()
                    s[2, 2, 1]
                """
    G = Fundamental

class FreeSymmetricFunctions_Dual(UniqueRepresentation, Parent):
    """
    The Hopf dual `FSym^*` of the free symmetric functions `FSym`.

    See :class:`FreeSymmetricFunctions` for the definition of the
    latter.

    Recall that the fundamental basis of `FSym` consists of the
    elements `\\mathcal{G}_t` for `t` ranging over all standard
    tableaux. The dual basis of this is called the *dual
    fundamental basis* of `FSym^*`, and is denoted by
    `(\\mathcal{G}_t^*)`.
    The Hopf dual `FSym^*` is isomorphic to the Hopf algebra
    `(\\ZZ T, \\ast', \\delta')` from [PoiReu95]_; the
    isomorphism sends a basis element `\\mathcal{G}_t^*` to `t`.

    EXAMPLES::

        sage: FSym = algebras.FSym(QQ)
        sage: TF = FSym.dual().F()
        sage: TF[1,2] * TF[[1],[2]]
        F[12|3|4] + F[123|4] + F[124|3] + F[13|2|4] + F[134|2] + F[14|2|3]
        sage: TF[[1,2],[3]].coproduct()
        F[] # F[12|3] + F[1] # F[1|2] + F[12] # F[1] + F[12|3] # F[]

    The Hopf algebra `FSym^*` is a Hopf quotient of `FQSym`;
    the canonical projection sends `F_w` (for a permutation `w`)
    to `\\mathcal{G}_{Q(w)}^*`, where `Q(w)` is the Q-tableau of
    `w`. This projection is implemented as a coercion::

        sage: FQSym = algebras.FQSym(QQ)
        sage: F = FQSym.F()
        sage: TF(F[[1, 3, 2]])
        F[12|3]
        sage: TF(F[[5, 1, 4, 2, 3]])
        F[135|2|4]
    """
    def __init__(self, base_ring) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: FSymD = algebras.FSym(QQ).dual()
            sage: TestSuite(FSymD).run()
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the Fundamental
        dual basis).

        EXAMPLES::

            sage: FSym = algebras.FSym(QQ).dual()
            sage: FSym.a_realization()
            Dual Hopf algebra of standard tableaux over the Rational Field
             in the FundamentalDual basis
        """
    def dual(self):
        """
        Return the dual Hopf algebra of ``self``, which is `FSym`.

        EXAMPLES::

            sage: D = algebras.FSym(QQ).dual()
            sage: D.dual()
            Hopf algebra of standard tableaux over the Rational Field
        """
    class FundamentalDual(FSymBasis_abstract):
        """
        The dual to the Hopf algebra of tableaux,
        on the fundamental dual basis.

        EXAMPLES::

            sage: FSym = algebras.FSym(QQ)
            sage: TF = FSym.dual().F()
            sage: TF
            Dual Hopf algebra of standard tableaux over the Rational Field
             in the FundamentalDual basis

        Elements of the algebra look like::

            sage: TF.an_element()
            2*F[] + 2*F[1] + 3*F[12]

        TESTS::

            sage: FSym = algebras.FSym(QQ)
            sage: TF = FSym.dual().F()
            sage: TestSuite(TF).run()
        """
        def dual_basis(self):
            """
            Return the dual basis to ``self``.

            EXAMPLES::

                sage: F = algebras.FSym(QQ).dual().F()
                sage: F.dual_basis()
                Hopf algebra of standard tableaux over the Rational Field
                 in the Fundamental basis
            """
        @cached_method
        def product_on_basis(self, t1, t2):
            """
            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: TF = FSym.dual().F()
                sage: t1 = StandardTableau([[1,2]])
                sage: TF.product_on_basis(t1, t1)
                F[12|34] + F[123|4] + F[1234] + F[124|3] + F[13|24] + F[134|2]
                sage: t0 = StandardTableau([])
                sage: TF.product_on_basis(t1, t0) == TF[t1] == TF.product_on_basis(t0, t1)
                True
            """
        @cached_method
        def coproduct_on_basis(self, t):
            """
            EXAMPLES::

                sage: FSym = algebras.FSym(QQ)
                sage: TF = FSym.dual().F()
                sage: t = StandardTableau([[1,2,5], [3,4]])
                sage: TF.coproduct_on_basis(t)
                F[] # F[125|34] + F[1] # F[134|2] + F[12] # F[123]
                 + F[12|3] # F[12] + F[12|34] # F[1] + F[125|34] # F[]
            """
        class Element(FSymBasis_abstract.Element):
            def to_quasisymmetric_function(self):
                """
                Return the image of ``self`` under the canonical projection
                `FSym^* \\to QSym` to the ring of quasi-symmetric functions.

                This projection is the adjoint of the canonical injection
                `NSym \\to FSym` (see
                :meth:`~sage.combinat.ncsf_qsym.ncsf.NonCommutativeSymmetricFunctions.Bases.ElementMethods.to_fsym`).
                It sends each tableau `t` to the fundamental quasi-symmetric
                function `F_\\alpha`, where `\\alpha` is the descent composition
                of `t`.

                EXAMPLES::

                    sage: F = algebras.FSym(QQ).dual().F()
                    sage: F[[1,3,5],[2,4]].to_quasisymmetric_function()
                    F[1, 2, 2]
                """
    F = FundamentalDual

def standardize(t):
    """
    Return the standard tableau corresponding to a given
    semistandard tableau ``t`` with no repeated entries.

    .. NOTE::

        This is an optimized version of :meth:`Tableau.standardization`
        for computations in `FSym` by using the assumption of no
        repeated entries in ``t``.

    EXAMPLES::

        sage: from sage.combinat.chas.fsym import standardize
        sage: t = Tableau([[1,3,5,7],[2,4,8],[9]])
        sage: standardize(t)
        [[1, 3, 5, 6], [2, 4, 7], [8]]
        sage: t = Tableau([[3,8,9,15],[5,10,12],[133]])
        sage: standardize(t)
        [[1, 3, 4, 7], [2, 5, 6], [8]]

    TESTS:

    This returns an equal tableau if already standard::

        sage: t = Tableau([[1,3,4,5],[2,6,7],[8]])
        sage: standardize(t)
        [[1, 3, 4, 5], [2, 6, 7], [8]]
        sage: standardize(t) == t
        True
    """
def ascent_set(t):
    """
    Return the ascent set of a standard tableau ``t``
    (encoded as a sorted list).

    The *ascent set* of a standard tableau `t` is defined as
    the set of all entries `i` of `t` such that the number `i+1`
    either appears to the right of `i` or appears in a row above
    `i` or does not appear in `t` at all.

    EXAMPLES::

        sage: from sage.combinat.chas.fsym import ascent_set
        sage: t = StandardTableau([[1,3,4,7],[2,5,6],[8]])
        sage: ascent_set(t)
        [2, 3, 5, 6, 8]
        sage: ascent_set(StandardTableau([]))
        []
        sage: ascent_set(StandardTableau([[1, 2, 3]]))
        [1, 2, 3]
        sage: ascent_set(StandardTableau([[1, 2, 4], [3]]))
        [1, 3, 4]
        sage: ascent_set([[1, 3, 5], [2, 4]])
        [2, 4, 5]
    """
def descent_set(t):
    """
    Return the descent set of a standard tableau ``t``
    (encoded as a sorted list).

    The *descent set* of a standard tableau `t` is defined as
    the set of all entries `i` of `t` such that the number `i+1`
    appears in a row below `i` in `t`.

    EXAMPLES::

        sage: from sage.combinat.chas.fsym import descent_set
        sage: t = StandardTableau([[1,3,4,7],[2,5,6],[8]])
        sage: descent_set(t)
        [1, 4, 7]
        sage: descent_set(StandardTableau([]))
        []
        sage: descent_set(StandardTableau([[1, 2, 3]]))
        []
        sage: descent_set(StandardTableau([[1, 2, 4], [3]]))
        [2]
        sage: descent_set([[1, 3, 5], [2, 4]])
        [1, 3]
    """
def descent_composition(t):
    """
    Return the descent composition of a standard tableau ``t``.

    This is the composition of the size of `t` whose partial
    sums are the elements of the descent set of ``t`` (see
    :meth:`descent_set`).

    EXAMPLES::

        sage: from sage.combinat.chas.fsym import descent_composition
        sage: t = StandardTableau([[1,3,4,7],[2,5,6],[8]])
        sage: descent_composition(t)
        [1, 3, 3, 1]
        sage: descent_composition([[1, 3, 5], [2, 4]])
        [1, 2, 2]
    """
