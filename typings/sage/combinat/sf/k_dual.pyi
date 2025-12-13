from _typeshed import Incomplete
from sage.categories.graded_hopf_algebras import GradedHopfAlgebras as GradedHopfAlgebras
from sage.categories.graded_hopf_algebras_with_basis import GradedHopfAlgebrasWithBasis as GradedHopfAlgebrasWithBasis
from sage.categories.realizations import Category_realization_of_parent as Category_realization_of_parent, Realizations as Realizations
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.partition import Partition as Partition, Partitions as Partitions, PartitionsGreatestLE as PartitionsGreatestLE, Partitions_all_bounded as Partitions_all_bounded
from sage.cpython.getattr import raw_getattr as raw_getattr
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class KBoundedQuotient(UniqueRepresentation, Parent):
    k: Incomplete
    t: Incomplete
    indices: Incomplete
    def __init__(self, Sym, k, t: str = 't') -> None:
        """
        Initialization of the ring of Symmetric functions modulo the ideal of monomial
        symmetric functions which are indexed by partitions whose first part is greater
        than `k`.

        INPUT:

        - ``Sym`` -- an element of class :class:`sage.combinat.sf.sf.SymmetricFunctions`

        - ``k`` -- positive integer

        - ``R`` -- a ring

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: Q = Sym.kBoundedQuotient(3,t=1)
            sage: Q
            3-Bounded Quotient of Symmetric Functions over Rational Field with t=1
            sage: km = Q.km()
            sage: km
            3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded monomial basis
            sage: F = Q.affineSchur()
            sage: F(km(F[3,1,1])) == F[3,1,1]
            True
            sage: km(F(km([3,2]))) == km[3,2]
            True
            sage: F[3,2].lift()
            m[1, 1, 1, 1, 1] + m[2, 1, 1, 1] + m[2, 2, 1] + m[3, 1, 1] + m[3, 2]
            sage: F[2,1]*F[2,1]
            2*F3[1, 1, 1, 1, 1, 1] + 4*F3[2, 1, 1, 1, 1] + 4*F3[2, 2, 1, 1] + 4*F3[2, 2, 2] + 2*F3[3, 1, 1, 1] + 4*F3[3, 2, 1] + 2*F3[3, 3]
            sage: F[1,2]
            Traceback (most recent call last):
            ...
            ValueError: [1, 2] is not an element of 3-Bounded Partitions
            sage: F[4,2]
            Traceback (most recent call last):
            ...
            ValueError: [4, 2] is not an element of 3-Bounded Partitions
            sage: km[2,1]*km[2,1]
            4*m3[2, 2, 1, 1] + 6*m3[2, 2, 2] + 2*m3[3, 2, 1] + 2*m3[3, 3]
            sage: HLPk = Q.kHallLittlewoodP()
            sage: HLPk[2,1]*HLPk[2,1]
            4*HLP3[2, 2, 1, 1] + 6*HLP3[2, 2, 2] + 2*HLP3[3, 2, 1] + 2*HLP3[3, 3]
            sage: dks = Q.dual_k_Schur()
            sage: dks[2,1]*dks[2,1]
            2*dks3[1, 1, 1, 1, 1, 1] + 4*dks3[2, 1, 1, 1, 1] + 4*dks3[2, 2, 1, 1] + 4*dks3[2, 2, 2] + 2*dks3[3, 1, 1, 1] + 4*dks3[3, 2, 1] + 2*dks3[3, 3]

        ::

            sage: Q = Sym.kBoundedQuotient(3)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 't' to a rational
            sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
            sage: Q = Sym.kBoundedQuotient(3)
            sage: km = Q.km()
            sage: F = Q.affineSchur()
            sage: F(km(F[3,1,1])) == F[3,1,1]
            True
            sage: km(F(km([3,2]))) == km[3,2]
            True
            sage: dks = Q.dual_k_Schur()
            sage: HLPk = Q.kHallLittlewoodP()
            sage: dks(HLPk(dks[3,1,1])) == dks[3,1,1]
            True
            sage: km(dks(km([3,2]))) == km[3,2]
            True
            sage: dks[2,1]*dks[2,1]
            (t^3+t^2)*dks3[1, 1, 1, 1, 1, 1] + (2*t^2+2*t)*dks3[2, 1, 1, 1, 1] + (t^2+2*t+1)*dks3[2, 2, 1, 1] + (t^2+2*t+1)*dks3[2, 2, 2] + (t+1)*dks3[3, 1, 1, 1] + (2*t+2)*dks3[3, 2, 1] + (t+1)*dks3[3, 3]

        TESTS::

            sage: TestSuite(Q).run()
        """
    def ambient(self):
        """

        Returns the Symmetric Functions over the same ring as ``self``. This is needed to
        realize our ring as a quotient.

        TESTS::

            sage: Sym = SymmetricFunctions(QQ)
            sage: Q = Sym.kBoundedQuotient(3,t=1)
            sage: Q.ambient()
            Symmetric Functions over Rational Field
        """
    def a_realization(self):
        """
        Return a particular realization of ``self`` (the basis of `k`-bounded monomials
        if `t=1` and the basis of `k`-bounded Hall-Littlewood functions otherwise).

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: Q = Sym.kBoundedQuotient(3,t=1)
            sage: Q.a_realization()
            3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded monomial basis
            sage: Q = Sym.kBoundedQuotient(3,t=2)
            sage: Q.a_realization()
            3-Bounded Quotient of Symmetric Functions over Rational Field with t=2 in the 3-bounded Hall-Littlewood P basis
        """
    def kmonomial(self):
        """
        The monomial basis of the `k`-bounded quotient of symmetric functions, indexed by
        `k`-bounded partitions.

        EXAMPLES::

            sage: SymmetricFunctions(QQ).kBoundedQuotient(2,t=1).kmonomial()
            2-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 2-bounded monomial basis
        """
    km = kmonomial
    def kHallLittlewoodP(self):
        """
        The Hall-Littlewood P basis of the `k`-bounded quotient of symmetric functions,
        indexed by `k`-bounded partitions.  At `t=1` this basis is equal to the
        `k`-bounded monomial basis and calculations will be faster using elements in the
        `k`-bounded monomial basis (see :meth:`kmonomial`).

        EXAMPLES::

            sage: SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(2).kHallLittlewoodP()
            2-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the 2-bounded Hall-Littlewood P basis
        """
    kHLP = kHallLittlewoodP
    def dual_k_Schur(self):
        """
        The dual `k`-Schur basis of the `k`-bounded quotient of symmetric functions,
        indexed by `k`-bounded partitions.  At `t=1` this is also equal to the affine
        Schur basis and calculations will be faster using elements in the :meth:`affineSchur`
        basis.

        EXAMPLES::

            sage: SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(2).dual_k_Schur()
            2-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the dual 2-Schur basis
        """
    dks = dual_k_Schur
    def affineSchur(self):
        """
        The affine Schur basis of the `k`-bounded quotient of symmetric functions,
        indexed by `k`-bounded partitions.  This is also equal to the affine Stanley
        symmetric functions (see :meth:`WeylGroups.ElementMethods.stanley_symmetric_function`)
        indexed by an affine Grassmannian permutation.

        EXAMPLES::

            sage: SymmetricFunctions(QQ).kBoundedQuotient(2,t=1).affineSchur()
            2-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 2-bounded affine Schur basis
        """
    F = affineSchur
    def AffineGrothendieckPolynomial(self, la, m):
        """
        Return the affine Grothendieck polynomial indexed by the partition ``la``.
        Because this belongs to the completion of the algebra, and hence is an infinite
        sum, it computes only up to those symmetric functions of degree at most ``m``.
        See :meth:`_AffineGrothendieckPolynomial` for the code.

        INPUT:

        - ``la`` -- a `k`-bounded partition

        - ``m`` -- integer

        EXAMPLES::

            sage: Q = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1)
            sage: Q.AffineGrothendieckPolynomial([2,1],4)
            2*m3[1, 1, 1] - 8*m3[1, 1, 1, 1] + m3[2, 1] - 3*m3[2, 1, 1] - m3[2, 2]
        """
    def one(self):
        """
        Return the unit of the quotient ring of `k`-bounded symmetric functions. This
        method is here to make the TestSuite run properly.

        EXAMPLES::

            sage: Q = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1)
            sage: Q.one()
            m3[]
        """
    def retract(self, la):
        """
        Give the retract map from the symmetric functions to the quotient ring of
        `k`-bounded symmetric functions. This method is here to make the TestSuite run
        properly.

        INPUT:

        - ``la`` -- a partition

        OUTPUT: the monomial element of the `k`-bounded quotient indexed by ``la``

        EXAMPLES::

            sage: Q = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1)
            sage: Q.retract([2,1])
            m3[2, 1]
        """
    def lift(self, la):
        """
        Give the lift map from the quotient ring of `k`-bounded symmetric functions to
        the symmetric functions. This method is here to make the TestSuite run properly.

        INPUT:

        - ``la`` -- a `k`-bounded partition

        OUTPUT:

        - The monomial element or a Hall-Littlewood P element of the symmetric functions
            indexed by the partition ``la``.

        EXAMPLES::

            sage: Q = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1)
            sage: Q.lift([2,1])
            m[2, 1]
            sage: Q = SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(3)
            sage: Q.lift([2,1])
            HLP[2, 1]
        """
    def realizations(self):
        """
        A list of realizations of the `k`-bounded quotient.

        EXAMPLES::

            sage: kQ = SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(3)
            sage: kQ.realizations()
            [3-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the 3-bounded monomial basis, 3-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the 3-bounded Hall-Littlewood P basis, 3-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the 3-bounded affine Schur basis, 3-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the dual 3-Schur basis]
            sage: HLP = kQ.ambient().hall_littlewood().P()
            sage: all( rzn(HLP[3,2,1]).lift() == HLP[3,2,1] for rzn in kQ.realizations())
            True
            sage: kQ = SymmetricFunctions(QQ).kBoundedQuotient(3,1)
            sage: kQ.realizations()
            [3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded monomial basis, 3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded Hall-Littlewood P basis, 3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded affine Schur basis, 3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the dual 3-Schur basis]
            sage: m = kQ.ambient().m()
            sage: all( rzn(m[3,2,1]).lift() == m[3,2,1] for rzn in kQ.realizations())
            True
        """

class KBoundedQuotientBases(Category_realization_of_parent):
    """
    The category of bases for the `k`-bounded subspace of symmetric functions.
    """
    def __init__(self, base) -> None:
        """
        Initialization of the bases of the `k`-bounded subspace.

        INPUT:

        - ``base`` -- a basis in the `k`-bounded subspace

        TESTS::

            sage: Sym = SymmetricFunctions(QQ['t'])
            sage: from sage.combinat.sf.k_dual import KBoundedQuotientBases
            sage: Q = Sym.kBoundedQuotient(3,t=1)
            sage: KQB = KBoundedQuotientBases(Q); KQB
            Category of k bounded quotient bases of 3-Bounded Quotient of Symmetric Functions over Univariate Polynomial Ring in t over Rational Field with t=1
        """
    def super_categories(self):
        """
        The super categories of ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ['t'])
            sage: from sage.combinat.sf.k_dual import KBoundedQuotientBases
            sage: Q = Sym.kBoundedQuotient(3,t=1)
            sage: KQB = KBoundedQuotientBases(Q)
            sage: KQB.super_categories()
            [Category of realizations of 3-Bounded Quotient of Symmetric Functions over Univariate Polynomial Ring in t over Rational Field with t=1,
             Join of Category of graded Hopf algebras with basis over Univariate Polynomial Ring in t over Rational Field
                 and Category of quotients of algebras over Univariate Polynomial Ring in t over Rational Field
                 and Category of quotients of graded modules with basis over Univariate Polynomial Ring in t over Rational Field]
        """
    class ParentMethods:
        def retract(self, la):
            """
            Give the retract map from the symmetric functions to the quotient ring of
            `k`-bounded symmetric functions. This method is here to make the TestSuite run
            properly.

            INPUT:

            - ``la`` -- a partition

            OUTPUT: the monomial element of the `k`-bounded quotient indexed by ``la``

            EXAMPLES::

                sage: Q = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1)
                sage: Q.retract([2,1])
                m3[2, 1]
            """
        def ambient(self):
            """
            Return the symmetric functions.

            EXAMPLES::

                sage: km = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).km()
                sage: km.ambient()
                Symmetric Functions over Rational Field
            """
        def __getitem__(self, c):
            """
            Implement shorthand for accessing basis elements.

            For a basis `X` indexed by partitions, this method allows for
            `X[[3,2]]` and `X[3,2]` to be equivalent to `X[Partition([3,2])]`.

            Due to limitations in Python syntax, one must use `X[[]]` and not
            `X[]` for the basis element indexed by the empty partition.

            EXAMPLES::

                sage: F = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).affineSchur()
                sage: F[3,2]
                F3[3, 2]
                sage: F[[]]
                F3[]
            """
        @cached_method
        def one_basis(self):
            """
            Return the basis element indexing ``1``.

            EXAMPLES::

                sage: F = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).affineSchur()
                sage: F.one()  # indirect doctest
                F3[]
            """
        def degree_on_basis(self, b):
            """
            Return the degree of the basis element indexed by ``b``.

            INPUT:

            - ``b`` -- a partition

            EXAMPLES::

                sage: F = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).affineSchur()
                sage: F.degree_on_basis(Partition([3,2]))
                5
            """
        def indices(self):
            """
            The set of `k`-bounded partitions of all nonnegative integers.

            EXAMPLES::

                sage: km = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).km()
                sage: km.indices()
                3-Bounded Partitions
            """
        def lift(self, la):
            """
            Implement the lift map from the basis ``self`` to the monomial basis of
            symmetric functions.

            INPUT:

            - ``la`` -- a `k`-bounded partition

            OUTPUT: a symmetric function in the monomial basis

            EXAMPLES::

                sage: F = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).affineSchur()
                sage: F.lift([3,1])
                m[1, 1, 1, 1] + m[2, 1, 1] + m[2, 2] + m[3, 1]
                sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
                sage: dks = Sym.kBoundedQuotient(3).dual_k_Schur()
                sage: dks.lift([3,1])
                t^5*HLP[1, 1, 1, 1] + t^2*HLP[2, 1, 1] + t*HLP[2, 2] + HLP[3, 1]
                sage: dks = Sym.kBoundedQuotient(3,t=1).dual_k_Schur()
                sage: dks.lift([3,1])
                m[1, 1, 1, 1] + m[2, 1, 1] + m[2, 2] + m[3, 1]
            """
        def product(self, x, y):
            """
            Return the product of two elements ``x`` and ``y``.

            INPUT:

            - ``x``, ``y`` -- elements of the `k`-bounded quotient of symmetric functions

            OUTPUT: a `k`-bounded symmetric function in the dual `k`-Schur function basis

            EXAMPLES::

                sage: dks3 = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).dual_k_Schur()
                sage: dks3.product(dks3[2,1],dks3[1,1])
                2*dks3[1, 1, 1, 1, 1] + 2*dks3[2, 1, 1, 1] + 2*dks3[2, 2, 1] + dks3[3, 1, 1] + dks3[3, 2]
                sage: dks3.product(dks3[2,1]+dks3[1], dks3[1,1])
                dks3[1, 1, 1] + 2*dks3[1, 1, 1, 1, 1] + dks3[2, 1] + 2*dks3[2, 1, 1, 1] + 2*dks3[2, 2, 1] + dks3[3, 1, 1] + dks3[3, 2]
                sage: dks3.product(dks3[2,1]+dks3[1], dks3([]))
                dks3[1] + dks3[2, 1]
                sage: dks3.product(dks3([]), dks3([]))
                dks3[]
                sage: dks3.product(dks3([]), dks3([4,1]))
                Traceback (most recent call last):
                ...
                TypeError: do not know how to make x (= [4, 1]) an element of self (=3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the dual 3-Schur basis)

            ::

                sage: dks3 = SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(3).dual_k_Schur()
                sage: dks3.product(dks3[2,1],dks3[1,1])
                (t^2+t)*dks3[1, 1, 1, 1, 1] + (t+1)*dks3[2, 1, 1, 1] + (t+1)*dks3[2, 2, 1] + dks3[3, 1, 1] + dks3[3, 2]
                sage: dks3.product(dks3[2,1]+dks3[1], dks3[1,1])
                dks3[1, 1, 1] + (t^2+t)*dks3[1, 1, 1, 1, 1] + dks3[2, 1] + (t+1)*dks3[2, 1, 1, 1] + (t+1)*dks3[2, 2, 1] + dks3[3, 1, 1] + dks3[3, 2]
                sage: dks3.product(dks3[2,1]+dks3[1], dks3([]))
                dks3[1] + dks3[2, 1]
                sage: dks3.product(dks3([]), dks3([]))
                dks3[]

            ::

                sage: F = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).affineSchur()
                sage: F.product(F[2,1],F[1,1])
                2*F3[1, 1, 1, 1, 1] + 2*F3[2, 1, 1, 1] + 2*F3[2, 2, 1] + F3[3, 1, 1] + F3[3, 2]
                sage: F.product(F[2,1]+F[1], F[1,1])
                F3[1, 1, 1] + 2*F3[1, 1, 1, 1, 1] + F3[2, 1] + 2*F3[2, 1, 1, 1] + 2*F3[2, 2, 1] + F3[3, 1, 1] + F3[3, 2]
                sage: F.product(F[2,1]+F[1], F([]))
                F3[1] + F3[2, 1]
                sage: F.product(F([]), F([]))
                F3[]
                sage: F.product(F([]), F([4,1]))
                Traceback (most recent call last):
                ...
                TypeError: do not know how to make x (= [4, 1]) an element of self (=3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded affine Schur basis)

            ::

                sage: F = SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(3).affineSchur()
                sage: F.product(F[2,1],F[1,1])
                2*F3[1, 1, 1, 1, 1] + 2*F3[2, 1, 1, 1] + 2*F3[2, 2, 1] + F3[3, 1, 1] + F3[3, 2]
                sage: F.product(F[2,1],F[2])
                (t^4+t^3-2*t^2+1)*F3[1, 1, 1, 1, 1] + (-t^2+t+1)*F3[2, 1, 1, 1] + (-t^2+t+2)*F3[2, 2, 1] + (t+1)*F3[3, 1, 1] + (t+1)*F3[3, 2]
                sage: F.product(F[2,1]+F[1], F[1,1])
                F3[1, 1, 1] + 2*F3[1, 1, 1, 1, 1] + F3[2, 1] + 2*F3[2, 1, 1, 1] + 2*F3[2, 2, 1] + F3[3, 1, 1] + F3[3, 2]
                sage: F.product(F[2,1]+F[1], F([]))
                F3[1] + F3[2, 1]
                sage: F.product(F([]), F([]))
                F3[]

            ::

                sage: km = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).km()
                sage: km.product(km[2,1],km[2,1])
                4*m3[2, 2, 1, 1] + 6*m3[2, 2, 2] + 2*m3[3, 2, 1] + 2*m3[3, 3]
                sage: Q3 = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3)
                sage: km = Q3.km()
                sage: km.product(km[2,1],km[2,1])
                (t^5+7*t^4-8*t^3-28*t^2+47*t-19)*m3[1, 1, 1, 1, 1, 1] + (t^4-3*t^3-9*t^2+23*t-12)*m3[2, 1, 1, 1, 1] + (-t^3-3*t^2+11*t-3)*m3[2, 2, 1, 1] + (-t^2+5*t+2)*m3[2, 2, 2] + (6*t-6)*m3[3, 1, 1, 1] + (3*t-1)*m3[3, 2, 1] + (t+1)*m3[3, 3]
                sage: dks = Q3.dual_k_Schur()
                sage: km.product(dks[2,1],dks[1,1])
                20*m3[1, 1, 1, 1, 1] + 9*m3[2, 1, 1, 1] + 4*m3[2, 2, 1] + 2*m3[3, 1, 1] + m3[3, 2]
            """
        def antipode(self, element):
            """
            Return the antipode of ``element`` via lifting to the symmetric
            functions and then retracting into the `k`-bounded quotient basis.

            INPUT:

            - ``element`` -- an element in a basis of the ring of symmetric
              functions

            EXAMPLES::

                sage: dks3 = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).dual_k_Schur()
                sage: dks3[3,2].antipode()
                -dks3[1, 1, 1, 1, 1]
                sage: km = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).km()
                sage: km[3,2].antipode()
                m3[3, 2]
                sage: km.antipode(km[3,2])
                m3[3, 2]
                sage: m = SymmetricFunctions(QQ).m()
                sage: m[3,2].antipode()
                m[3, 2] + 2*m[5]

            ::

                sage: km = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3).km()
                sage: km[1,1,1,1].antipode()
                (t^3-3*t^2+3*t)*m3[1, 1, 1, 1] + (-t^2+2*t)*m3[2, 1, 1] + t*m3[2, 2] + t*m3[3, 1]
                sage: kHP = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3).kHLP()
                sage: kHP[2,2].antipode()
                (t^9-t^6-t^5+t^2)*HLP3[1, 1, 1, 1] + (t^6-t^3-t^2+t)*HLP3[2, 1, 1] + (t^5-t^2+1)*HLP3[2, 2] + (t^4-t)*HLP3[3, 1]
                sage: dks = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3).dks()
                sage: dks[2,2].antipode()
                dks3[2, 2]
                sage: dks[3,2].antipode()
                -t^2*dks3[1, 1, 1, 1, 1] + (t^2-1)*dks3[2, 2, 1] + (-t^5+t)*dks3[3, 2]
            """
        def coproduct(self, element):
            """
            Return the coproduct of ``element`` via lifting to the symmetric
            functions and then returning to the `k`-bounded quotient basis.
            This method is implemented for all `t` but is (weakly) conjectured
            to not be the correct operation for arbitrary `t` because the
            coproduct on dual-`k`-Schur functions does not have a positive
            expansion.

            INPUT:

            - ``element`` -- an element in a basis of the ring of symmetric
              functions

            EXAMPLES::

                sage: Q3 = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1)
                sage: km = Q3.km()
                sage: km[3,2].coproduct()
                m3[] # m3[3, 2] + m3[2] # m3[3] + m3[3] # m3[2] + m3[3, 2] # m3[]
                sage: dks3 = Q3.dual_k_Schur()
                sage: dks3[2,2].coproduct()
                dks3[] # dks3[2, 2] + dks3[1] # dks3[2, 1] + dks3[1, 1] # dks3[1, 1] + dks3[2] # dks3[2] + dks3[2, 1] # dks3[1] + dks3[2, 2] # dks3[]

            ::

                sage: Q3t = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3)
                sage: km = Q3t.km()
                sage: km[3,2].coproduct()
                m3[] # m3[3, 2] + m3[2] # m3[3] + m3[3] # m3[2] + m3[3, 2] # m3[]
                sage: dks = Q3t.dks()
                sage: dks[2,1,1].coproduct()
                dks3[] # dks3[2, 1, 1] + (-t+1)*dks3[1] # dks3[1, 1, 1] + dks3[1] # dks3[2, 1] + (-t+1)*dks3[1, 1] # dks3[1, 1] + dks3[1, 1] # dks3[2] + (-t+1)*dks3[1, 1, 1] # dks3[1] + dks3[2] # dks3[1, 1] + dks3[2, 1] # dks3[1] + dks3[2, 1, 1] # dks3[]
                sage: kHLP = Q3t.kHLP()
                sage: kHLP[2,1].coproduct()
                HLP3[] # HLP3[2, 1] + (-t^2+1)*HLP3[1] # HLP3[1, 1] + HLP3[1] # HLP3[2] + (-t^2+1)*HLP3[1, 1] # HLP3[1] + HLP3[2] # HLP3[1] + HLP3[2, 1] # HLP3[]
                sage: km.coproduct(km[3,2])
                m3[] # m3[3, 2] + m3[2] # m3[3] + m3[3] # m3[2] + m3[3, 2] # m3[]
            """
        def counit(self, element):
            """
            Return the counit of ``element``.

            The counit is the constant term of ``element``.

            INPUT:

            - ``element`` -- an element in a basis

            EXAMPLES::

                sage: km = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3).km()
                sage: f = 2*km[2,1] - 3*km([])
                sage: f.counit()
                -3
                sage: km.counit(f)
                -3
            """
    class ElementMethods: ...

class KBoundedQuotientBasis(CombinatorialFreeModule):
    """
    Abstract base class for the bases of the `k`-bounded quotient.
    """
    k: Incomplete
    t: Incomplete
    def __init__(self, kBoundedRing, prefix) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``kBoundedRing`` -- an element which is of class :class:`KBoundedQuotient`
        - ``prefix`` -- string used to distinguish this basis, and used in printing

        EXAMPLES::

            sage: from sage.combinat.sf.k_dual import kMonomial
            sage: km = kMonomial(SymmetricFunctions(QQ).kBoundedQuotient(4,t=1))
            sage: km.prefix()  # indirect doctest
            'm4'
            sage: isinstance(km, sage.combinat.sf.k_dual.KBoundedQuotientBasis)
            True
        """
    __getitem__: Incomplete

class kMonomial(KBoundedQuotientBasis):
    """
    The basis of monomial symmetric functions indexed by partitions with first
    part less than or equal to `k`.
    """
    def __init__(self, kBoundedRing) -> None:
        """
        Initialize the ring which is the `k`-Bounded monomial quotient basis.

        INPUT:

        - ``kBoundedRing`` -- an element which is of class :class:`KBoundedQuotient`

        EXAMPLES::

            sage: from sage.combinat.sf.k_dual import kMonomial
            sage: km = kMonomial(SymmetricFunctions(QQ).kBoundedQuotient(4,t=1))
            sage: km
            4-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 4-bounded monomial basis
            sage: TestSuite(km).run()
        """
    def retract(self, la):
        """
        Implement the retract function on the monomial basis. Given a partition ``la``,
        the retract will return the corresponding `k`-bounded monomial basis element if
        ``la`` is `k`-bounded; zero otherwise.

        INPUT:

        - ``la`` -- a partition

        OUTPUT: a `k`-bounded monomial symmetric function in the `k`-quotient of symmetric
        functions

        EXAMPLES::

            sage: km = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).km()
            sage: km.retract(Partition([3,1]))
            m3[3, 1]
            sage: km.retract(Partition([4,1]))
            0
            sage: km.retract([])
            m3[]
            sage: m = SymmetricFunctions(QQ).m()
            sage: km(m[3, 1])
            m3[3, 1]
            sage: km(m[4, 1])
            0

        ::

            sage: km = SymmetricFunctions(FractionField(QQ['t'])).kBoundedQuotient(3).km()
            sage: km.retract(Partition([3,1]))
            m3[3, 1]
            sage: km.retract(Partition([4,1]))
            (t^4+t^3-9*t^2+11*t-4)*m3[1, 1, 1, 1, 1] + (-3*t^2+6*t-3)*m3[2, 1, 1, 1] + (-t^2+3*t-2)*m3[2, 2, 1] + (2*t-2)*m3[3, 1, 1] + (t-1)*m3[3, 2]
            sage: m = SymmetricFunctions(FractionField(QQ['t'])).m()
            sage: km(m[3, 1])
            m3[3, 1]
            sage: km(m[4, 1])
            (t^4+t^3-9*t^2+11*t-4)*m3[1, 1, 1, 1, 1] + (-3*t^2+6*t-3)*m3[2, 1, 1, 1] + (-t^2+3*t-2)*m3[2, 2, 1] + (2*t-2)*m3[3, 1, 1] + (t-1)*m3[3, 2]
        """
    def lift(self, la):
        """
        Implement the lift function on the monomial basis. Given a `k`-bounded partition
        ``la``, the lift will return the corresponding monomial basis element.

        INPUT:

        - ``la`` -- a `k`-bounded partition

        OUTPUT: a monomial symmetric function

        EXAMPLES::

            sage: km = SymmetricFunctions(QQ).kBoundedQuotient(3,t=1).km()
            sage: km.lift(Partition([3,1]))
            m[3, 1]
            sage: km.lift([])
            m[]
            sage: km.lift(Partition([4,1]))
            Traceback (most recent call last):
            ...
            TypeError: do not know how to make x (= [4, 1]) an element of self (=3-Bounded Quotient of Symmetric Functions over Rational Field with t=1 in the 3-bounded monomial basis)
        """

class kbounded_HallLittlewoodP(KBoundedQuotientBasis):
    """
    The basis of P Hall-Littlewood symmetric functions indexed by partitions with first
    part less than or equal to `k`.
    """
    def __init__(self, kBoundedRing) -> None:
        """
        Initialize the ring which is the `k`-Bounded Hall-Littlewood P quotient basis.

        INPUT:

        - ``kBoundedRing`` -- an element which is of class :class:`KBoundedQuotient`

        EXAMPLES::

            sage: from sage.combinat.sf.k_dual import kbounded_HallLittlewoodP
            sage: kP = kbounded_HallLittlewoodP(SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(4))
            sage: kP
            4-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the 4-bounded Hall-Littlewood P basis
            sage: TestSuite(kP).run()
        """
    def retract(self, la):
        """
        Implement the retract function on the Hall-Littlewood P basis. Given a partition
        ``la``, the retract will return the corresponding `k`-bounded Hall-Littlewood P
        basis element if ``la`` is `k`-bounded; zero otherwise.

        INPUT:

        - ``la`` -- a partition

        OUTPUT: a `k`-bounded Hall-Littlewood P symmetric function in the `k`-quotient of
        symmetric functions

        EXAMPLES::

            sage: kHLP = SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(3).kHallLittlewoodP()
            sage: kHLP.retract(Partition([3,1]))
            HLP3[3, 1]
            sage: kHLP.retract(Partition([4,1]))
            0
            sage: kHLP.retract([])
            HLP3[]
            sage: m = kHLP.realization_of().ambient().m()
            sage: kHLP(m[2,2])
            (t^4-t^3-t+1)*HLP3[1, 1, 1, 1] + (t-1)*HLP3[2, 1, 1] + HLP3[2, 2]
        """
    def lift(self, la):
        """
        Implement the lift function on the Hall-Littlewood P basis. Given a `k`-bounded
        partition ``la``, the lift will return the corresponding Hall-Littlewood P basis
        element.

        INPUT:

        - ``la`` -- a `k`-bounded partition

        OUTPUT: a Hall-Littlewood symmetric function

        EXAMPLES::

            sage: kHLP = SymmetricFunctions(QQ['t'].fraction_field()).kBoundedQuotient(3).kHallLittlewoodP()
            sage: kHLP.lift(Partition([3,1]))
            HLP[3, 1]
            sage: kHLP.lift([])
            HLP[]
            sage: kHLP.lift(Partition([4,1]))
            Traceback (most recent call last):
            ...
            TypeError: do not know how to make x (= [4, 1]) an element of self (=3-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the 3-bounded Hall-Littlewood P basis)
        """

class DualkSchurFunctions(KBoundedQuotientBasis):
    """
    This basis is dual to the `k`-Schur functions.  The expansion is given
    in Section 4.12 of [LLMSSZ]_.  When `t=1` this basis is equal to the
    :class:`AffineSchurFunctions` and that basis is more efficient in this case.

    REFERENCES:

    .. [LLMSSZ] \\T. Lam, L. Lapointe, J. Morse, A. Schilling, M. Shimozono, M. Zabrocki,
        k-Schur functions and affine Schubert calculus.
    """
    def __init__(self, kBoundedRing) -> None:
        """
        Initialize the ring which is the dual `k`-Schur function basis.

        INPUT:

        - ``kBoundedRing`` -- an element which is of class :class:`KBoundedQuotient`

        EXAMPLES::

            sage: from sage.combinat.sf.k_dual import DualkSchurFunctions
            sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
            sage: dks4 = DualkSchurFunctions(Sym.kBoundedQuotient(4))
            sage: dks4
            4-Bounded Quotient of Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the dual 4-Schur basis
            sage: TestSuite(dks4).run()  # long time (7s on sage.math, 2013)
            sage: dks4 = DualkSchurFunctions(Sym.kBoundedQuotient(4,t=1))
            sage: TestSuite(dks4).run()  # long time (7s on sage.math, 2013)
        """

class AffineSchurFunctions(KBoundedQuotientBasis):
    """
    This basis is dual to the `k`-Schur functions at `t=1`.  This realization
    follows the monomial expansion given by Lam [Lam2006]_.

    REFERENCES:

    .. [Lam2006] \\T. Lam, Schubert polynomials for the affine Grassmannian, J. Amer.
        Math. Soc., 21 (2008), 259-281.
    """
    def __init__(self, kBoundedRing) -> None:
        """
        Initialize the ring which is the `k`-Bounded affine Schur quotient basis.

        INPUT:

        - ``kBoundedRing`` -- an element which is of class :class:`KBoundedQuotient`

        EXAMPLES::

            sage: from sage.combinat.sf.k_dual import AffineSchurFunctions
            sage: F = AffineSchurFunctions(SymmetricFunctions(QQ['t']).kBoundedQuotient(4,t=1))
            sage: F
            4-Bounded Quotient of Symmetric Functions over Univariate Polynomial Ring in t over Rational Field with t=1 in the 4-bounded affine Schur basis
            sage: TestSuite(F).run()  # long time (5s on sage.math, 2013)
        """
